"""Figuras SD-07 · Ruta crítica hacia H7 y hacia H12 (extraída de la red del cronograma).

La cadena se obtiene recorriendo hacia atrás, desde cada hito, las relaciones cuyo predecesor tiene holgura total 0
según el motor CPM del equipo (red v3, 2.127 relaciones). Cada fila agrupa nodos de la cadena; las flechas siguen el
tipo real de la relación: FI (fin–inicio, desde el fin de la barra) e II (inicio–inicio, desde el inicio).
Las actividades con holgura 0 por fecha fija propia que no están en la cadena se muestran en gris, como contexto.
Tamaño real: 17,6 cm de ancho, escala semanal.
Uso: <python con matplotlib> diag-07-11_ruta-critica.py <dir traspaso con Red_CPM/verificacion>
"""
import csv, json, os, sys, shutil, collections
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
CALS = os.path.join(RAIZ, '80_Artefactos/sd-07_contexto/traspaso-2026-11-10/Red_CPM/calendarios.json')
FIG = os.path.join(RAIZ, '02_Propuesta/latex_final/figuras/sd07-figuras')
sys.path.insert(0, os.path.join(sys.argv[1], 'Red_CPM/verificacion'))
from motor_cpm_verificado_20261105 import Network
ROJO, GRIS, TEXTO, TEXTO2, GRILLA, BANDA, CABECERA = '#d03b3b', '#9aa3ad', '#17324D', '#52514e', '#e6e6e3', '#f3f3f0', '#17324D'
W = 6.93
MESES_ES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
plt.rcParams.update({'font.family': 'Lato', 'font.size': 9, 'text.color': TEXTO})
D = date.fromisoformat
rd = lambda p: json.load(open(p, encoding='utf-8-sig'))
NODOS, REL = rd(os.path.join(V, 'Red_CPM/nodos.json')), rd(os.path.join(V, 'Red_CPM/relaciones.json'))
net = Network(NODOS, REL, rd(CALS))
CPM = {r['id']: r for r in net.calculate()}
PRED = collections.defaultdict(list)
for r in REL:
    PRED[r['succ']].append(r)

def cadena(hito):
    vis, pila, aristas = {hito}, [hito], []
    while pila:
        k = pila.pop()
        for r in PRED[k]:
            p = r['pred']
            if CPM.get(p, {}).get('slack_days') == 0:
                aristas.append((p, k, r['type']))
                if p not in vis:
                    vis.add(p); pila.append(p)
    return vis, aristas

FIGURAS = [
 ('diag-07-11_ruta-critica-h7', 'A:H7', (date(2027, 12, 1), date(2028, 4, 28)), [
   ('Revisión del cliente de la certificación E1', lambda k: k == 'A:ACCEPT:E1:REVIEW'),
   ('Reserva para subsanar observaciones', lambda k: k == 'A:ACCEPT:E1:REWORK'),
   ('H5 · Certificación E1', lambda k: k == 'A:H5'),
   ('H6 · Inicio de marcha blanca E1', lambda k: k == 'A:H6'),
   ('Marcha blanca E1: operación supervisada', lambda k: k in ('1.12.2:MB1:MB-E1:118', 'CONTINUIDAD:MB1', 'A:C0132:S', 'A:C0133:S')),
   ('Cuatro últimas semanas de evidencia', lambda k: k in ('A:OBSERVACION-28:E1', 'A:EVIDENCE_28:E1')),
   ('Revisión progresiva del expediente', lambda k: k == 'A:REV-FINAL-MB:E1'),
   ('H7 · Producción E1', lambda k: k == 'A:H7'),
   ('Viaje del equipo de acompañamiento', lambda k: k.startswith('CAMPO:')),
   ('Entrada oficial de las 22 tiendas', lambda k: k.startswith('A:FIELD_ACT:')),
  ], [('Habilitación de las 22 tiendas (fecha fija)', lambda r: r['edt'] == '1.11.2' and '2028-01-01' <= r['inicio'] < '2028-03-01'),
      ('Cartera: tramo T1 (fecha fija)', lambda r: r['id'].startswith('FIN:T1'))]),
 ('diag-07-11_ruta-critica-h12', 'A:H12', (date(2028, 6, 1), date(2028, 9, 14)), [
   ('Revisión del cliente de la certificación E2', lambda k: k == 'A:ACCEPT:E2:REVIEW'),
   ('Reserva para subsanar observaciones', lambda k: k == 'A:ACCEPT:E2:REWORK'),
   ('H10 · Certificación E2', lambda k: k == 'A:H10'),
   ('H11 · Inicio de marcha blanca E2', lambda k: k == 'A:H11'),
   ('Marcha blanca E2: operación supervisada', lambda k: k in ('1.12.5:MB2:MB-E2:119', 'A:C0135:S', 'A:C0136:S')),
   ('Cuatro últimas semanas de evidencia', lambda k: k in ('A:OBSERVACION-28:E2', 'A:EVIDENCE_28:E2')),
   ('Revisión progresiva del expediente', lambda k: k == 'A:REV-FINAL-MB:E2'),
   ('Continuidad del servicio de la Etapa 1', lambda k: k in ('CONTINUIDAD:MB1', 'CONTINUIDAD:E1-PROD')),
   ('H12 · Producción E2 y aceptación', lambda k: k == 'A:H12'),
  ], [('Cartera: tramos T2 y T3 (fecha fija)', lambda r: r['id'].startswith(('FIN:T2', 'FIN:T3')))]),
]
P = list(csv.DictReader(open(os.path.join(V, 'programacion_v3.csv'), encoding='utf-8-sig'), delimiter=';'))

def figura(archivo, hito, ventana, defs, contexto):
    vis, aristas = cadena(hito)
    fila_de = {}
    for i, (_, f) in enumerate(defs):
        for k in vis:
            if f(k):
                fila_de[k] = i
    sin_fila = [k for k in vis if k not in fila_de]
    assert not [k for k in sin_fila if not k.startswith(('A:CLIENT', 'A:ACCEPT:E', 'CONTINUIDAD:', 'A:H'))], sin_fila
    # relaciones entre filas (contrayendo nodos sin fila)
    suc = collections.defaultdict(list)
    for p, s, t in aristas:
        suc[p].append((s, t))
    arcos = {}
    for p in fila_de:
        pila, vistos = [(s, t) for s, t in suc[p]], set()
        while pila:
            s, t = pila.pop()
            if s in vistos:
                continue
            vistos.add(s)
            if s in fila_de:
                if fila_de[s] != fila_de[p]:
                    arcos.setdefault((fila_de[p], fila_de[s]), (t, p, s))
            else:
                pila.extend(suc[s])
    filas = []
    for i, (nombre, _) in enumerate(defs):
        ks = [k for k in fila_de if fila_de[k] == i]
        a = min(D(CPM[k]['ES']) for k in ks); b = max(D(CPM[k]['EF']) for k in ks)
        filas.append((nombre, a, b, nombre[:1] == 'H' and nombre[1:3].strip(' ·').isdigit(), 'critica'))
    for nombre, f in contexto:
        rs = [r for r in P if f(r)]
        filas.append((nombre, min(D(r['inicio']) for r in rs), max(D(r['fin_exclusivo']) for r in rs), False, 'contexto'))
    n = len(filas)
    x0, x1 = ventana
    FILA, CAB, PIE = 0.26, 0.40, 0.30
    H = CAB + n * FILA + PIE
    fig = plt.figure(figsize=(W, H))
    cols = dict(nom=0.0, ini=2.62, fin=3.17, bar=3.72)
    top, bot = 1 - CAB / H, PIE / H
    ancho = W - cols['bar'] - 0.03
    tx = fig.add_axes([0, bot, cols['bar'] / W, top - bot]); tx.axis('off')
    ax = fig.add_axes([cols['bar'] / W, bot, ancho / W, top - bot]); ax.axis('off')
    hx = fig.add_axes([0, 1 - CAB / H, 1, CAB / H]); hx.axis('off'); hx.set_xlim(0, W); hx.set_ylim(0, 1)
    for a in (tx, ax):
        a.set_ylim(n - 0.5, -0.5)
    tx.set_xlim(0, cols['bar'])
    X = lambda d: d.toordinal()
    ax.set_xlim(X(x0), X(x1))
    esc = ancho / (X(x1) - X(x0))
    hx.add_patch(Rectangle((0, 0.03), cols['bar'] - 0.02, 0.94, color=CABECERA, lw=0))
    for x, t, ha in ((cols['nom'] + 0.06, 'Actividad', 'left'), (cols['ini'] + 0.26, 'Inicio', 'center'), (cols['fin'] + 0.26, 'Fin', 'center')):
        hx.text(x, 0.5, t, ha=ha, va='center', fontsize=9, fontweight='bold', color='white')
    # meses (franja superior) y semanas (líneas finas)
    d = date(x0.year, x0.month, 1)
    k = 0
    while d < x1:
        nxt = date(d.year + (d.month // 12), d.month % 12 + 1, 1)
        a, b = max(d, x0), min(nxt, x1)
        xa, xb = cols['bar'] + (X(a) - X(x0)) * esc, cols['bar'] + (X(b) - X(x0)) * esc
        hx.add_patch(Rectangle((xa + 0.004, 0.03), xb - xa - 0.008, 0.94, color='#dfe6ee' if k % 2 else '#eef2f6', lw=0))
        hx.text((xa + xb) / 2, 0.5, f'{MESES_ES[d.month - 1]} {d.year}', ha='center', va='center', fontsize=7.5, color=TEXTO)
        if k % 2:
            ax.axvspan(X(a), X(b), color=BANDA, zorder=0, lw=0)
        d, k = nxt, k + 1
    w = x0
    while w < x1:
        if w.weekday() == 0:
            ax.axvline(X(w), color=GRILLA, lw=0.4, zorder=0)
        w += timedelta(days=1)
    for i, (nombre, a, b, es_hito, tipo) in enumerate(filas):
        tx.text(cols['nom'] + 0.06, i, nombre, ha='left', va='center', fontsize=8.5, color=TEXTO if tipo == 'critica' else TEXTO2,
                fontweight='bold' if es_hito else 'normal')
        tx.text(cols['ini'] + 0.26, i, a.strftime('%d-%m-%y'), ha='center', va='center', fontsize=8)
        tx.text(cols['fin'] + 0.26, i, (b - timedelta(days=1) if b > a else b).strftime('%d-%m-%y'), ha='center', va='center', fontsize=8)
        if es_hito:
            ax.plot(X(a), i, marker='D', ms=6.5, color=TEXTO, zorder=5)
        else:
            if a < x0:
                ax.plot(X(x0) + 1.5, i, marker='<', ms=5, color=TEXTO2, zorder=4)
            ax.add_patch(Rectangle((X(max(a, x0)) + (3 if a < x0 else 0), i - 0.2), max(X(min(b, x1)) - X(max(a, x0)), 1.2), 0.4,
                                   facecolor=ROJO if tipo == 'critica' else GRIS, lw=0, zorder=3))
        tx.axhline(i + 0.5, color=GRILLA, lw=0.4); ax.axhline(i + 0.5, color=GRILLA, lw=0.4)
    # flechas por tipo: FI desde el fin del predecesor, II desde su inicio
    for (i, j), (t, p, s) in sorted(arcos.items()):
        ai, bi = filas[i][1], filas[i][2]
        aj = filas[j][1]
        xo = X(ai) if t == 'SS' else X(bi)
        xd = X(aj)
        sgn = 1 if j > i else -1
        y0 = i + (0 if filas[i][3] else 0.2 * sgn)
        ax.plot([xo, xo], [y0, j], color=TEXTO2, lw=0.7, ls='-' if t == 'FS' else (0, (3, 2)), zorder=4)
        if abs(xd - xo) > 1:
            ax.annotate('', xy=(xd - (2 if filas[j][3] else 0), j), xytext=(xo, j),
                        arrowprops=dict(arrowstyle='-|>', color=TEXTO2, lw=0.7, mutation_scale=7, ls='-' if t == 'FS' else (0, (3, 2))), zorder=4)
        else:
            ax.annotate('', xy=(xo, j - 0.22 * sgn), xytext=(xo, j - 0.5 * sgn),
                        arrowprops=dict(arrowstyle='-|>', color=TEXTO2, lw=0.7, mutation_scale=7), zorder=4)
    ley = [Patch(facecolor=ROJO, label='Ruta crítica (holgura 0)'), Patch(facecolor=GRIS, label='Fecha fija, fuera de la ruta crítica'),
           Line2D([], [], marker='D', color=TEXTO, lw=0, ms=6, label='Hito'),
           Line2D([], [], color=TEXTO2, lw=0.8, label='Fin–inicio (FI)'), Line2D([], [], color=TEXTO2, lw=0.8, ls=(0, (3, 2)), label='Inicio–inicio (II)')]
    fig.legend(handles=ley, loc='lower left', bbox_to_anchor=(0, 0), ncol=5, frameon=False, fontsize=7.5, handlelength=1.6, columnspacing=0.9)
    base = os.path.join(AQUI, archivo)
    fig.savefig(base + '.png', dpi=300); fig.savefig(base + '.pdf'); plt.close(fig)
    shutil.copyfile(base + '.pdf', os.path.join(FIG, archivo + '.pdf'))
    print('ok', archivo, 'nodos de la cadena', len(vis), 'relaciones', len(aristas), collections.Counter(t for *_, t in aristas), 'flechas', len(arcos))
    for (i, j), (t, p, s) in sorted(arcos.items()):
        print(f'   {filas[i][0][:38]:38s} -{t}-> {filas[j][0][:38]}')

for f in FIGURAS:
    figura(*f)
