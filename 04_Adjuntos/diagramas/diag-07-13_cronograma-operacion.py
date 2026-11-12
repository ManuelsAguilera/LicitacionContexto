"""Figura SD-07 · Cronograma de la operación, M21–M56 (servicios continuos y trabajos puntuales).

Celdas de un mes, como la vista general. Los servicios continuos (esfuerzo continuo) van rayados y sin dependencias;
los trabajos puntuales de la red del cronograma se pintan en el mes en que ocurren.
Tamaño real: 17,6 cm de ancho.
Uso: <python con matplotlib> diag-07-13_cronograma-operacion.py
"""
import csv, os, shutil
from datetime import date, timedelta
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle, Patch
from matplotlib.lines import Line2D

for _f in ('Lato-Regular.ttf', 'Lato-Bold.ttf'):
    _r = os.path.join('/usr/share/fonts/truetype/lato', _f)
    if os.path.exists(_r):
        font_manager.fontManager.addfont(_r)
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
V = os.path.join(RAIZ, '80_Artefactos/sd-07_contexto/red-v3-2026-11-10')
FIG = os.path.join(RAIZ, '02_Propuesta/latex_final/figuras/sd07-figuras')
OSCURO, LOE = '#196197', '#9aa3ad'
TEXTO, TEXTO2, GRILLA, BANDA, CABECERA = '#17324D', '#52514e', '#e6e6e3', '#f3f3f0', '#17324D'
W = 6.93
plt.rcParams.update({'font.family': 'Lato', 'font.size': 9, 'text.color': TEXTO, 'hatch.color': LOE, 'hatch.linewidth': 0.8})
P = list(csv.DictReader(open(os.path.join(V, 'programacion_v3.csv'), encoding='utf-8-sig'), delimiter=';'))
D = date.fromisoformat
M1 = date(2027, 1, 7)
def ini_mes(m):
    y, mm = divmod(M1.month - 1 + m - 1, 12)
    return date(M1.year + y, mm + 1, 7)
def mes(d):
    m = (d.year - M1.year) * 12 + d.month - M1.month + 1
    return m if d.day >= 7 else m - 1
M0, MF = 21, 56
def pk(r, pre):
    return bool(r['edt']) and any(r['edt'] == e or r['edt'].startswith(e + '.') for e in pre)
OPER = lambda r: r['etapa'] in ('OP',) or (r['inicio'] >= '2028-09-07' and r['etapa'] in ('E1-PROD',))

FILAS = [
 ('Servicios continuos', None, None),
 ('Mesa de servicio, NOC, soporte L2 y L3 (1.15)', 'loe', (21, 56)),
 ('Centro de operaciones de seguridad (1.8.2)', 'loe', (21, 56)),
 ('Dirección del proyecto (1.1)', 'loe', (21, 56)),
 ('Trabajos puntuales', None, None),
 ('Jornadas de actualización del personal', 'act', lambda r: pk(r, ['1.15.6']) and OPER(r)),
 ('Base de conocimiento y manuales de operación', 'act', lambda r: pk(r, ['1.14.3']) and OPER(r)),
 ('Retiro de la plataforma de crédito de 2011', 'act', lambda r: pk(r, ['1.7.9']) and OPER(r)),
 ('Plan de reversibilidad', 'act', lambda r: pk(r, ['1.14.4']) and OPER(r)),
 ('Ensayo de degradación del evento anual', 'act', lambda r: pk(r, ['1.9.5']) and OPER(r)),
 ('Transferencia tecnológica (código y artefactos)', 'act', lambda r: pk(r, ['1.14.2']) and OPER(r)),
 ('Retiro del sistema central de 2009', 'act', lambda r: pk(r, ['1.7.10']) and OPER(r)),
 ('Acta de cierre y acompañamiento de reversibilidad', 'act', lambda r: pk(r, ['1.14.5']) and OPER(r)),
 ('Informe de lecciones aprendidas', 'act', lambda r: pk(r, ['1.14.6']) and OPER(r)),
]
n = len(FILAS)
FILA, CAB, PIE, BANDA_H = 0.23, 0.40, 0.28, 0.30
H = CAB + BANDA_H + n * FILA + PIE
fig = plt.figure(figsize=(W, H))
cols = dict(nom=0.0, ini=2.62, fin=3.15, bar=3.68)
top, bot = 1 - (CAB + BANDA_H) / H, PIE / H
ancho = W - cols['bar'] - 0.03
tx = fig.add_axes([0, bot, cols['bar'] / W, top - bot]); tx.axis('off')
ax = fig.add_axes([cols['bar'] / W, bot, ancho / W, top - bot]); ax.axis('off')
hb = fig.add_axes([cols['bar'] / W, top, ancho / W, BANDA_H / H]); hb.axis('off')
hx = fig.add_axes([0, 1 - CAB / H, 1, CAB / H]); hx.axis('off'); hx.set_xlim(0, W); hx.set_ylim(0, 1)
for a in (tx, ax):
    a.set_ylim(n - 0.5, -0.5)
tx.set_xlim(0, cols['bar'])
for a in (ax, hb):
    a.set_xlim(M0, MF + 1)
hb.set_ylim(0, 1)
hx.add_patch(Rectangle((0, 0.03), cols['bar'] - 0.02, 0.94, color=CABECERA, lw=0))
for x, t, ha in ((cols['nom'] + 0.06, 'Actividad', 'left'), (cols['ini'] + 0.26, 'Inicio', 'center'), (cols['fin'] + 0.26, 'Fin', 'center')):
    hx.text(x, 0.5, t, ha=ha, va='center', fontsize=9, fontweight='bold', color='white')
esc = ancho / (MF + 1 - M0)
anio = None
for m in range(M0, MF + 1):
    xa = cols['bar'] + (m - M0) * esc
    y = ini_mes(m).year if ini_mes(m).month > 1 or True else None
    hx.add_patch(Rectangle((xa + 0.002, 0.03), esc - 0.004, 0.94, color='#dfe6ee' if ini_mes(m).year % 2 else '#eef2f6', lw=0))
    if (m - M0) % 6 == 0:
        hx.text(xa + 0.01, 0.68, f'M{m}', ha='left', va='center', fontsize=7, color=TEXTO)
    if ini_mes(m).year != anio:
        anio = ini_mes(m).year
        hx.text(xa + 0.01, 0.28, str(anio), ha='left', va='center', fontsize=7, color=TEXTO2)
    if ini_mes(m).year % 2:
        ax.axvspan(m, m + 1, color=BANDA, zorder=0, lw=0)
for m, et, sube in ((21, 'H12 · inicio de la operación', 0.55), (57, 'Fin del contrato', 0.55)):
    hb.plot(m, 0.25, marker='D', ms=5.5, color=TEXTO, clip_on=False, zorder=5)
    hb.text(m + (0.3 if m == 21 else -0.3), sube, et, ha='left' if m == 21 else 'right', va='bottom', fontsize=7, color=TEXTO)
for i, (nombre, tipo, dato) in enumerate(FILAS):
    if tipo is None:
        tx.text(cols['nom'] + 0.06, i, nombre, ha='left', va='center', fontsize=9, fontweight='bold')
        for a in (tx, ax):
            a.axhline(i + 0.5, color=TEXTO2, lw=0.6)
        continue
    tx.text(cols['nom'] + 0.06, i, nombre, ha='left', va='center', fontsize=8, color=TEXTO2 if tipo == 'loe' else TEXTO)
    if tipo == 'loe':
        a_, b_ = ini_mes(dato[0]), ini_mes(dato[1] + 1) - timedelta(days=1)
        ax.add_patch(Rectangle((dato[0] + 0.05, i - 0.25), dato[1] - dato[0] + 0.9, 0.5, facecolor='white', edgecolor=LOE, hatch='////', lw=0.6, zorder=3))
    else:
        rs = [r for r in P if dato(r)]
        assert rs, nombre
        a_, b_ = min(D(r['inicio']) for r in rs), max(D(r['fin_exclusivo']) for r in rs) - timedelta(days=1)
        meses = set()
        for r in rs:
            d, q = D(r['inicio']), max(D(r['fin_exclusivo']), D(r['inicio']) + timedelta(days=1))
            while d < q:
                meses.add(mes(d)); d += timedelta(days=1)
        for m in meses:
            if M0 <= m <= MF:
                ax.add_patch(Rectangle((m + 0.06, i - 0.27), 0.88, 0.54, facecolor=OSCURO, lw=0, zorder=3))
    tx.text(cols['ini'] + 0.26, i, a_.strftime('%d-%m-%y'), ha='center', va='center', fontsize=7.5)
    tx.text(cols['fin'] + 0.26, i, b_.strftime('%d-%m-%y'), ha='center', va='center', fontsize=7.5)
    tx.axhline(i + 0.5, color=GRILLA, lw=0.4); ax.axhline(i + 0.5, color=GRILLA, lw=0.4)
ley = [Patch(facecolor='white', edgecolor=LOE, hatch='////', label='Servicio continuo (esfuerzo continuo)'),
       Patch(facecolor=OSCURO, label='Mes con trabajo puntual'), Line2D([], [], marker='D', color=TEXTO, lw=0, ms=5.5, label='Hito')]
fig.legend(handles=ley, loc='lower left', bbox_to_anchor=(0, 0), ncol=3, frameon=False, fontsize=7.5, handlelength=1.5)
base = os.path.join(AQUI, 'diag-07-13_cronograma-operacion')
fig.savefig(base + '.png', dpi=300); fig.savefig(base + '.pdf'); plt.close(fig)
shutil.copyfile(base + '.pdf', os.path.join(FIG, 'diag-07-13_cronograma-operacion.pdf'))
print('ok')
