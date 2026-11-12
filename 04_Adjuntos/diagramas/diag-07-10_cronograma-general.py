"""Figuras SD-07 · Cronograma general del desarrollo (nivel 1), en dos vistas: Etapa 1 (M1–M16) y Etapa 2 (M13–M21).

Sin ruta crítica ni dependencias. El tiempo se dibuja en celdas de un mes: si una actividad trabaja en un mes,
aunque sea un día, el mes se pinta completo, de modo que las actividades cortas siguen a la vista.
  tono oscuro = meses que reúnen el 80 % del trabajo de la fila (HH; si no tiene HH, días);
  tono claro  = meses con trabajo menor.
Cada vista muestra los hitos de su etapa (Formulario E-25) solo en la parte gráfica.
Filas: las actividades clave aprobadas para las Etapas 1 y 2 (paquetes del Formulario T-14).
Tamaño real: 17,6 cm de ancho.
Uso: <python con matplotlib> diag-07-10_cronograma-general.py
"""
import csv, os, shutil, collections
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
HITOS_CSV = os.path.join(RAIZ, 'Economica/insumos-sd07/Hitos_contractuales.csv')
OSCURO, CLARO = '#196197', '#b9cfe0'
TEXTO, TEXTO2, GRILLA, BANDA, CABECERA = '#17324D', '#52514e', '#e6e6e3', '#f3f3f0', '#17324D'
W = 6.93
MESES_ES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
plt.rcParams.update({'font.family': 'Lato', 'font.size': 9, 'text.color': TEXTO})

P = list(csv.DictReader(open(os.path.join(V, 'programacion_v3.csv'), encoding='utf-8-sig'), delimiter=';'))
HITOS = {r['hito']: date.fromisoformat(r['fecha']) for r in csv.DictReader(open(HITOS_CSV, encoding='utf-8-sig'))}
M1 = date(2027, 1, 7)
D = date.fromisoformat
def ini_mes(m):
    y, mm = divmod(M1.month - 1 + m - 1, 12)
    return date(M1.year + y, mm + 1, 7)
def mes(d):
    m = (d.year - M1.year) * 12 + d.month - M1.month + 1
    return m if d.day >= 7 else m - 1
fecha = lambda d: d.strftime('%d-%m-%y')
def pk(r, pre):
    return bool(r['edt']) and any(r['edt'] == e or r['edt'].startswith(e + '.') for e in pre)
E1 = lambda r: r['etapa'] in ('E1', 'MB1', 'E1-PROD') or r['edt'] == '1.10.2.7'
E2 = lambda r: r['etapa'] in ('E2', 'MB2') and r['edt'] != '1.10.2.7'
fase = lambda r: r['id'].split(':')[2] if r['id'].count(':') >= 3 else ''

SECCIONES = [
 ('Etapa 1', E1, [
  ('Levantamiento y línea base de alcance', lambda r: pk(r, ['1.2'])),
  ('Arquitectura, modelo de datos y seguridad', lambda r: pk(r, ['1.3', '1.8.1', '1.8.3', '1.8.7'])),
  ('Nube, ambientes y plataforma de integración', lambda r: pk(r, ['1.4.1', '1.4.3', '1.4.4', '1.4.5', '1.4.6', '1.4.7', '1.4.20', '1.4.21', '1.4.24'])),
  ('Centro de datos DC-01', lambda r: pk(r, ['1.4.8', '1.4.9', '1.4.10', '1.4.11', '1.4.12', '1.4.13', '1.4.16', '1.4.22'])),
  ('Sitios: levantamiento, laboratorio y piloto', lambda r: pk(r, ['1.4.14', '1.4.15', '1.4.17', '1.4.23'])),
  ('Piloto técnico y prueba de corte de enlace', lambda r: pk(r, ['1.9.9'])),
  ('Sitios: suministro e instalación del lote 2', lambda r: pk(r, ['1.4.2', '1.4.18', '1.4.19'])),
  ('Construcción del software E1', lambda r: pk(r, ['1.5'])),
  ('Integraciones E1', lambda r: pk(r, ['1.6'])),
  ('Seguridad desplegada y pruebas de intrusión', lambda r: pk(r, ['1.8.2', '1.8.4', '1.8.5', '1.8.6', '1.8.8', '1.8.9'])),
  ('Conteo cíclico predictivo', lambda r: pk(r, ['1.10.2'])),
  ('Pruebas y certificación E1', lambda r: pk(r, ['1.9.1', '1.9.2', '1.9.3', '1.9.4', '1.9.5', '1.9.6', '1.9.7', '1.9.8', '1.9.10', '1.9.11', '1.9.12'])),
  ('Migración y saneamiento de datos', lambda r: pk(r, ['1.7']) and not r['id'].startswith('FIN:T1') and r['edt'] != '1.7.3'),
  ('Corte de inventario', lambda r: pk(r, ['1.7.3'])),
  ('Gestión del cambio y capacitación E1', lambda r: pk(r, ['1.13'])),
  ('Planes de implantación y marcha blanca', lambda r: pk(r, ['1.11.1', '1.11.3', '1.12.1'])),
  ('Habilitación de las 22 tiendas', lambda r: pk(r, ['1.11.2']) and r['inicio'] < '2028-03-01'),
  ('Cartera: tramo T1', lambda r: r['id'].startswith('FIN:T1')),
  ('Marcha blanca E1 y acta', lambda r: pk(r, ['1.12.2', '1.12.3'])),
  ('Entrada en producción de las 22 tiendas', lambda r: pk(r, ['1.11.2']) and r['inicio'] >= '2028-03-01'),
 ]),
 ('Etapa 2', E2, [
  ('Análisis y diseño detallado E2', lambda r: pk(r, ['1.5']) and fase(r) == 'DIS'),
  ('Construcción del software E2', lambda r: pk(r, ['1.5']) and fase(r) == 'DEV'),
  ('Pruebas del software E2', lambda r: pk(r, ['1.5']) and fase(r) == 'QA'),
  ('Integraciones E2', lambda r: pk(r, ['1.6'])),
  ('Lockers Ancoa 24/7', lambda r: pk(r, ['1.10.1'])),
  ('Búsqueda vectorial multimodal', lambda r: pk(r, ['1.10.3'])),
  ('Retail Media Network', lambda r: pk(r, ['1.10.4'])),
  ('Modo Tienda con fila virtual de probadores', lambda r: pk(r, ['1.10.5'])),
  ('Pruebas de intrusión y cadena de suministro E2', lambda r: pk(r, ['1.8'])),
  ('Pruebas y certificación E2', lambda r: pk(r, ['1.9'])),
  ('Migración y saneamiento de datos E2', lambda r: pk(r, ['1.7']) and not r['id'].startswith(('FIN:T2', 'FIN:T3'))),
  ('Base de conocimiento y manuales', lambda r: pk(r, ['1.14'])),
  ('Capacitación E2 y comunicación a clientes', lambda r: pk(r, ['1.13'])),
  ('Plan de marcha blanca E2', lambda r: pk(r, ['1.12.4'])),
  ('Cartera: tramos T2 y T3', lambda r: r['id'].startswith(('FIN:T2', 'FIN:T3'))),
  ('Marcha blanca E2 y acta', lambda r: pk(r, ['1.12.5'])),
 ]),
]

def celdas(rs, M0, MF):
    """Peso por mes (HH o, si no hay, días) y meses oscuros que reúnen el 80 % del peso."""
    peso = collections.defaultdict(float)
    for r in rs:
        a, b = D(r['inicio']), D(r['fin_exclusivo'])
        b = max(b, a + timedelta(days=1))
        dias = (b - a).days
        w = float(r['HH'] or 0) or dias
        d = a
        while d < b:
            peso[mes(d)] += w / dias
            d += timedelta(days=1)
    tot, acum, oscuros = sum(peso.values()), 0.0, set()
    for m, v in sorted(peso.items(), key=lambda x: -x[1]):
        if acum >= 0.8 * tot:
            break
        oscuros.add(m); acum += v
    return {m: ('oscuro' if m in oscuros else 'claro') for m in peso if M0 <= m <= MF}

def dibujar(secciones, M0, MF, hitos, nombre_arch):
    filas = []
    for titulo, filtro, defs in secciones:
        filas.append(('seccion', titulo, None))
        for nombre, f in defs:
            rs = [r for r in P if r['edt'] and filtro(r) and f(r)]
            assert rs, nombre
            filas.append(('act', nombre, rs))

    n = len(filas)
    FILA, CAB, PIE, BANDA_H = 0.205, 0.40, 0.28, 0.42
    H = CAB + BANDA_H + n * FILA + PIE
    fig = plt.figure(figsize=(W, H))
    cols = dict(nom=0.0, ini=2.45, fin=2.98, bar=3.52)
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
    # cabecera
    hx.add_patch(Rectangle((0, 0.03), cols['bar'] - 0.02, 0.94, color=CABECERA, lw=0))
    for x, t, ha in ((cols['nom'] + 0.06, 'Actividad', 'left'), (cols['ini'] + 0.26, 'Inicio', 'center'), (cols['fin'] + 0.26, 'Fin', 'center')):
        hx.text(x, 0.5, t, ha=ha, va='center', fontsize=9, fontweight='bold', color='white')
    esc = ancho / (MF + 1 - M0)
    for m in range(M0, MF + 1):
        xa = cols['bar'] + (m - M0) * esc
        hx.add_patch(Rectangle((xa + 0.004, 0.03), esc - 0.008, 0.94, color='#dfe6ee' if m % 2 else '#eef2f6', lw=0))
        hx.text(xa + esc / 2, 0.68, f'M{m}', ha='center', va='center', fontsize=7 if MF - M0 < 12 else 6, color=TEXTO)
        hx.text(xa + esc / 2, 0.30, MESES_ES[ini_mes(m).month - 1], ha='center', va='center', fontsize=7 if MF - M0 < 12 else 6, color=TEXTO2)
    # bandas de mes y solapamientos
    for m in range(M0, MF + 1):
        if m % 2:
            ax.axvspan(m, m + 1, color=BANDA, zorder=0, lw=0)
    # hitos: solo gráficos (banda superior + línea punteada)
    xm = lambda d: mes(d) + ((d - ini_mes(mes(d))).days / (ini_mes(mes(d) + 1) - ini_mes(mes(d))).days)
    por_fecha = collections.defaultdict(list)
    for h, d in HITOS.items():
        if h in hitos:
            por_fecha[d].append(h)
    for k, (d, hs) in enumerate(sorted(por_fecha.items())):
        x = xm(d)
        hb.plot(x, 0.22, marker='D', ms=5.5, color=TEXTO, zorder=5, clip_on=False)
        hb.text(x, 0.48 if k % 2 == 0 else 0.78, '·'.join(sorted(hs, key=lambda s: int(s[1:]))), ha='center', va='bottom', fontsize=7, color=TEXTO)
        ax.axvline(x, color=TEXTO2, lw=0.6, ls=(0, (2, 3)), zorder=1)
    # filas
    for i, (t, nombre, rs) in enumerate(filas):
        if t == 'seccion':
            tx.text(cols['nom'] + 0.06, i, nombre, ha='left', va='center', fontsize=9, fontweight='bold', color=TEXTO)
            for a in (tx, ax):
                a.axhline(i + 0.5, color=TEXTO2, lw=0.6)
            continue
        a_, b_ = min(D(r['inicio']) for r in rs), max(D(r['fin_exclusivo']) for r in rs) - timedelta(days=1)
        tx.text(cols['nom'] + 0.06, i, nombre, ha='left', va='center', fontsize=8, color=TEXTO)
        tx.text(cols['ini'] + 0.26, i, fecha(a_), ha='center', va='center', fontsize=7.5)
        tx.text(cols['fin'] + 0.26, i, fecha(b_), ha='center', va='center', fontsize=7.5)
        for m, tono in celdas(rs, M0, MF).items():
            ax.add_patch(Rectangle((m + 0.06, i - 0.3), 0.88, 0.6, facecolor=OSCURO if tono == 'oscuro' else CLARO, lw=0, zorder=3))
        tx.axhline(i + 0.5, color=GRILLA, lw=0.4); ax.axhline(i + 0.5, color=GRILLA, lw=0.4)
    ley = [Patch(facecolor=OSCURO, label='Meses con el trabajo principal (80 % de las horas)'),
           Patch(facecolor=CLARO, label='Meses con trabajo menor'),
           Line2D([], [], marker='D', color=TEXTO, lw=0, ms=5.5, label='Hito del contrato (Formulario E-25)')]
    fig.legend(handles=ley, loc='lower left', bbox_to_anchor=(0.0, 0.0), ncol=3, frameon=False, fontsize=7.5, handlelength=1.3, columnspacing=1.0)
    base = os.path.join(AQUI, nombre_arch)
    fig.savefig(base + '.png', dpi=300); fig.savefig(base + '.pdf'); plt.close(fig)
    shutil.copyfile(base + '.pdf', os.path.join(FIG, nombre_arch + '.pdf'))
    print('ok', round(H, 2), 'pulgadas de alto,', n, 'filas')

dibujar(SECCIONES[:1], 1, 16, {f'H{k}' for k in range(1, 8)}, 'diag-07-10_cronograma-etapa-1')
dibujar(SECCIONES[1:], 13, 21, {f'H{k}' for k in range(8, 13)}, 'diag-07-10_cronograma-etapa-2')
