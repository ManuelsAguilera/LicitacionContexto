"""Figuras SD-07 · Vistas de detalle del cronograma por tramo (actividades reales, dependencias y holgura).

Cada fila es un paquete del Formulario T-14 (nombre del diccionario) o un grupo explícito; los hitos son filas con rombo.
Barras: actividades de la red del cronograma, coloreadas por holgura total:
  rojo = en la ruta crítica hacia H7 o H12; gris = holgura 0 por fecha fija propia (fuera de la ruta crítica);
  ámbar = 10 días hábiles o menos; azul = más de 10.
Flechas: relaciones de la red entre filas de la vista (contrayendo nodos que no están en la vista y sin atravesar
hitos ajenos a ella), según su tipo: FI (fin–inicio, línea continua) e II (inicio–inicio, línea punteada).
Escala: semanal si la ventana supera 45 días; diaria si no.
Tamaño real: 17,6 cm de ancho.
Uso: <python con matplotlib> diag-07-12_cronograma-detalle.py <dir traspaso con Red_CPM/verificacion>
"""
import csv, json, os, re, sys, shutil, collections
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
HITOS_CSV = os.path.join(RAIZ, 'Economica/insumos-sd07/Hitos_contractuales.csv')
T14 = os.path.join(RAIZ, '02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-14.tex')
sys.path.insert(0, os.path.join(sys.argv[1], 'Red_CPM/verificacion'))
from motor_cpm_verificado_20261105 import Network
AZUL, AMBAR, ROJO, GRIS = '#196197', '#eda100', '#d03b3b', '#9aa3ad'
TEXTO, TEXTO2, GRILLA, BANDA, CABECERA = '#17324D', '#52514e', '#e6e6e3', '#f3f3f0', '#17324D'
W = 6.93
MESES_ES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
plt.rcParams.update({'font.family': 'Lato', 'font.size': 9, 'text.color': TEXTO})
D = date.fromisoformat
rd = lambda p: json.load(open(p, encoding='utf-8-sig'))
NODOS, REL = rd(os.path.join(V, 'Red_CPM/nodos.json')), rd(os.path.join(V, 'Red_CPM/relaciones.json'))
net = Network(NODOS, REL, rd(CALS)); CPM = {r['id']: r for r in net.calculate()}
P = list(csv.DictReader(open(os.path.join(V, 'programacion_v3.csv'), encoding='utf-8-sig'), delimiter=';'))
PID = {r['id']: r for r in P}
HITOS = {r['hito']: D(r['fecha']) for r in csv.DictReader(open(HITOS_CSV, encoding='utf-8-sig'))}
NOMBRE = {m.group(1): m.group(2).strip() for m in re.finditer(r'^(1\.[\d.]+) & ([^&]*) &', open(T14, encoding='utf-8').read(), re.M)}
HITO_CORTO = {'H1': 'Línea base aprobada', 'H2': 'Arquitectura aprobada', 'H3': 'Infraestructura y ambientes',
              'H4': 'Software E1 para pruebas', 'H5': 'Certificación E1', 'H6': 'Inicio de marcha blanca E1',
              'H7': 'Producción E1', 'H8': 'Línea base y diseño E2', 'H9': 'Software E2 para pruebas',
              'H10': 'Certificación E2', 'H11': 'Inicio de marcha blanca E2', 'H12': 'Producción E2 y aceptación'}
PRED, SUCC = collections.defaultdict(list), collections.defaultdict(list)
for r in REL:
    PRED[r['succ']].append(r); SUCC[r['pred']].append(r)
CRITICA = set()
for h in ('A:H7', 'A:H12'):
    pila = [h]
    while pila:
        k = pila.pop()
        for r in PRED[k]:
            if CPM.get(r['pred'], {}).get('slack_days') == 0 and r['pred'] not in CRITICA:
                CRITICA.add(r['pred']); pila.append(r['pred'])

def cat(k):
    h = int(PID[k]['holgura_dias'])
    if h == 0:
        return 'critica' if k in CRITICA else 'fija'
    return 'casi' if h <= 10 else 'normal'
PRIO = {'critica': 4, 'fija': 3, 'casi': 2, 'normal': 1}
COLOR = {'critica': ROJO, 'fija': GRIS, 'casi': AMBAR, 'normal': AZUL}
def pk(r, pre):
    return bool(r['edt']) and any(r['edt'] == e or r['edt'].startswith(e + '.') for e in pre)
paq = lambda codigo, etapas: (NOMBRE[codigo], lambda r: pk(r, [codigo]) and r['etapa'] in etapas)
E1, E1MB, E2 = ('E1',), ('E1', 'MB1'), ('E2',)
fase = lambda r: r['id'].split(':')[2] if r['id'].count(':') >= 3 else ''

VISTAS = [
 ('diag-07-12_detalle-infraestructura-h3', (date(2027, 3, 1), date(2027, 7, 12)), [
   paq('1.3.5', E1), paq('1.4.1', E1), paq('1.4.4', E1), paq('1.4.6', E1), paq('1.4.3', E1), paq('1.4.5', E1),
   'H2',
   paq('1.4.16', E1), paq('1.4.11', E1), paq('1.4.12', E1), paq('1.4.22', E1), paq('1.4.2', E1),
   ('Sitios piloto y laboratorio (1.4.15, 1.4.17, 1.4.23)', lambda r: pk(r, ['1.4.15', '1.4.17', '1.4.23']) and r['etapa'] in E1),
   paq('1.9.9', E1),
   'H3']),
 ('diag-07-12_detalle-piloto', (date(2027, 6, 1), date(2027, 7, 9)), [
   paq('1.4.15', E1), paq('1.4.17', E1),
   ('Red de sitio en las tiendas piloto (1.4.2)', lambda r: pk(r, ['1.4.2']) and r['etapa'] in E1 and '2027-06-01' <= r['inicio'] < '2027-06-30'),
   paq('1.4.23', E1), paq('1.9.9', E1), 'H3']),
 ('diag-07-12_detalle-certificacion-h5', (date(2027, 9, 24), date(2028, 1, 12)), [
   ('Versión candidata verificada (hito interno)', lambda r: r['id'] == 'E1:CANDIDATA'),
   paq('1.6.6', E1), paq('1.10.2.6', E1), paq('1.9.4', E1), paq('1.8.6', E1),
   'H4',
   paq('1.9.6', E1), paq('1.7.3', E1), paq('1.13.3', E1), paq('1.14.4', E1),
   ('Revisión del cliente y reserva de subsanación', lambda r: r['id'] in ('A:ACCEPT:E1:REVIEW', 'A:ACCEPT:E1:REWORK')),
   'H5']),
 ('diag-07-12_detalle-diseno-h8', (date(2028, 1, 3), date(2028, 3, 14)), [
   ('Análisis y diseño detallado del software E2', lambda r: pk(r, ['1.5']) and r['etapa'] == 'E2' and fase(r) == 'DIS'),
   ('Diseño de las cuatro innovaciones de la Etapa 2', lambda r: pk(r, ['1.10.1.1', '1.10.3.1', '1.10.4.1', '1.10.5.1'])),
   ('Evaluación en sombra del conteo predictivo', lambda r: pk(r, ['1.10.2.7'])),
   ('Corte de inventario y datos históricos E2', lambda r: pk(r, ['1.7.3', '1.7.4', '1.7.7']) and r['etapa'] == 'E2'),
   'H8',
   paq('1.9.5', E2)]),
 ('diag-07-12_detalle-construccion-h9', (date(2028, 3, 1), date(2028, 6, 14)), [
   ('Construcción del software E2', lambda r: pk(r, ['1.5']) and r['etapa'] == 'E2' and fase(r) == 'DEV'),
   ('Pruebas del software E2', lambda r: pk(r, ['1.5']) and r['etapa'] == 'E2' and fase(r) == 'QA'),
   ('Integraciones E2 (1.6.3, 1.6.4)', lambda r: pk(r, ['1.6.3', '1.6.4']) and r['etapa'] == 'E2'),
   ('Lockers Ancoa 24/7', lambda r: pk(r, ['1.10.1.2', '1.10.1.3', '1.10.1.4', '1.10.1.5'])),
   ('Búsqueda vectorial multimodal', lambda r: pk(r, ['1.10.3.2', '1.10.3.3', '1.10.3.4', '1.10.3.5'])),
   ('Retail Media Network', lambda r: pk(r, ['1.10.4.2', '1.10.4.3', '1.10.4.4', '1.10.4.5'])),
   ('Modo Tienda con fila virtual', lambda r: pk(r, ['1.10.5.2', '1.10.5.3', '1.10.5.4', '1.10.5.5'])),
   paq('1.12.4', E2),
   ('Capacitación E2 sobre procesos y reglas (parte anticipada)', lambda r: r['id'] == 'F:1.13.3:E2-ANT'),
   'H9']),
 ('diag-07-12_detalle-certificacion-h10', (date(2028, 5, 1), date(2028, 7, 14)), [
   paq('1.6.6', E2), paq('1.9.4', E2), paq('1.8.6', E2),
   ('Pruebas y certificación de las innovaciones', lambda r: pk(r, ['1.10.1.6', '1.10.1.7', '1.10.3.6', '1.10.3.7', '1.10.4.6', '1.10.4.7', '1.10.5.6', '1.10.5.7']) and r['etapa'] == 'E2'),
   paq('1.9.6', E2),
   ('Capacitación E2 sobre el software', lambda r: r['id'] == '1.13.3:E2:E2:237'),
   paq('1.14.3', E2),
   ('Revisión del cliente y reserva de subsanación', lambda r: r['id'] in ('A:ACCEPT:E2:REVIEW', 'A:ACCEPT:E2:REWORK')),
   'H10', 'H11']),
]

def vista(archivo, ventana, defs):
    x0, x1 = ventana
    filas, fila_de = [], {}
    for d in defs:
        if isinstance(d, str):
            filas.append(('hito', f'{d} · {HITO_CORTO[d]}', ['A:' + d])); fila_de['A:' + d] = len(filas) - 1
            continue
        nombre, f = d
        ks = [r['id'] for r in P if f(r) and (float(r['HH'] or 0) > 0 or r['id'].startswith(('A:ACCEPT', 'E1:CANDIDATA'))) and r['inicio'] < x1.isoformat() and r['fin_exclusivo'] >= x0.isoformat()]
        assert ks, nombre
        filas.append(('act', nombre, ks))
        for k in ks:
            fila_de[k] = len(filas) - 1
    # flechas por tipo, contrayendo nodos fuera de la vista y sin atravesar hitos ajenos
    arcos = {}
    for k, i in fila_de.items():
        pila, vistos = [(r['succ'], r['type']) for r in SUCC[k]], set()
        while pila:
            s, t = pila.pop()
            if s in vistos:
                continue
            vistos.add(s)
            j = fila_de.get(s)
            if j is None:
                if s.startswith('A:H') and s[3:].isdigit():
                    continue
                pila.extend((r['succ'], t) for r in SUCC[s]); continue
            if j != i:
                arcos.setdefault((i, j), (t, k, s))
    # reducción transitiva: se omite una flecha si la dependencia ya llega por otra fila de la vista
    ady = collections.defaultdict(set)
    for i, j in arcos:
        ady[i].add(j)
    def alcanza(a, b, saltar):
        pila, vistos = [x for x in ady[a] if (a, x) != saltar], set()
        while pila:
            x = pila.pop()
            if x == b:
                return True
            if x not in vistos:
                vistos.add(x); pila.extend(ady[x])
        return False
    arcos = {k: v for k, v in arcos.items() if not alcanza(k[0], k[1], k)}
    n = len(filas)
    FILA, CAB, PIE = 0.255, 0.40, 0.30
    H = CAB + n * FILA + PIE
    fig = plt.figure(figsize=(W, H))
    cols = dict(nom=0.0, ini=2.92, fin=3.42, bar=3.94)
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
    diaria = (x1 - x0).days <= 45
    hx.add_patch(Rectangle((0, 0.03), cols['bar'] - 0.02, 0.94, color=CABECERA, lw=0))
    for x, t, ha in ((cols['nom'] + 0.06, 'Actividad', 'left'), (cols['ini'] + 0.25, 'Inicio', 'center'), (cols['fin'] + 0.25, 'Fin', 'center')):
        hx.text(x, 0.5, t, ha=ha, va='center', fontsize=9, fontweight='bold', color='white')
    d, k = date(x0.year, x0.month, 1), 0
    while d < x1:
        nxt = date(d.year + d.month // 12, d.month % 12 + 1, 1)
        a, b = max(d, x0), min(nxt, x1)
        xa, xb = cols['bar'] + (X(a) - X(x0)) * esc, cols['bar'] + (X(b) - X(x0)) * esc
        hx.add_patch(Rectangle((xa + 0.004, 0.52 if diaria else 0.03), xb - xa - 0.008, 0.45 if diaria else 0.94, color='#dfe6ee' if k % 2 else '#eef2f6', lw=0))
        hx.text((xa + xb) / 2, 0.75 if diaria else 0.5, f'{MESES_ES[d.month - 1]} {d.year}' if xb - xa > 0.5 else MESES_ES[d.month - 1], ha='center', va='center', fontsize=7.5, color=TEXTO)
        if not diaria and k % 2:
            ax.axvspan(X(a), X(b), color=BANDA, zorder=0, lw=0)
        d, k = nxt, k + 1
    w = x0
    while w < x1:
        if diaria:
            if w.weekday() >= 5:
                ax.axvspan(X(w), X(w) + 1, color=BANDA, zorder=0, lw=0)
            if w.weekday() == 0:
                hx.text(cols['bar'] + (X(w) - X(x0) + 0.5) * esc, 0.28, str(w.day), ha='center', va='center', fontsize=7, color=TEXTO2)
                ax.axvline(X(w), color=GRILLA, lw=0.5, zorder=0)
        elif w.weekday() == 0:
            ax.axvline(X(w), color=GRILLA, lw=0.4, zorder=0)
        w += timedelta(days=1)
    rangos = []
    for i, (t, nombre, ks) in enumerate(filas):
        if t == 'hito':
            dh = HITOS[nombre.split(' ')[0]]
            tx.text(cols['nom'] + 0.06, i, nombre, ha='left', va='center', fontsize=8.5, fontweight='bold', color=TEXTO)
            for c in ('ini', 'fin'):
                tx.text(cols[c] + 0.25, i, dh.strftime('%d-%m-%y'), ha='center', va='center', fontsize=8, fontweight='bold')
            ax.plot(X(dh), i, marker='D', ms=6.5, color=TEXTO, zorder=5)
            rangos.append((dh, dh, True)); continue
        a = min(D(PID[k]['inicio']) for k in ks); b = max(D(PID[k]['fin_exclusivo']) for k in ks)
        tx.text(cols['nom'] + 0.06, i, nombre if len(nombre) <= 52 else nombre[:51] + '…', ha='left', va='center', fontsize=8.5, color=TEXTO)
        tx.text(cols['ini'] + 0.25, i, a.strftime('%d-%m-%y'), ha='center', va='center', fontsize=8)
        tx.text(cols['fin'] + 0.25, i, (b - timedelta(days=1)).strftime('%d-%m-%y'), ha='center', va='center', fontsize=8)
        if all(PID[k]['inicio'] == PID[k]['fin_exclusivo'] for k in ks):
            ax.plot(X(a), i, marker='D', ms=6.5, markerfacecolor='white', markeredgecolor=TEXTO, color=TEXTO, zorder=5)
            tx.texts[-1].set_text(a.strftime('%d-%m-%y'))
            rangos.append((a, a, True)); continue
        dia = {}
        for k in ks:
            p, q = D(PID[k]['inicio']), max(D(PID[k]['fin_exclusivo']), D(PID[k]['inicio']) + timedelta(days=1))
            c = cat(k)
            while p < q:
                if p not in dia or PRIO[c] > PRIO[dia[p]]:
                    dia[p] = c
                p += timedelta(days=1)
        dias = sorted(dd for dd in dia if x0 <= dd < x1)
        ini = None
        for m, dd in enumerate(dias):
            if ini is None:
                ini, c0 = dd, dia[dd]
            nx = dias[m + 1] if m + 1 < len(dias) else None
            if nx is None or (nx - dd).days > 1 or dia[nx] != c0:
                ax.add_patch(Rectangle((X(ini), i - 0.2), max(X(dd) + 1 - X(ini), 0.8), 0.4, facecolor=COLOR[c0], lw=0, zorder=3))
                ini = None
        if a < x0:
            ax.plot(X(x0) + (0.4 if diaria else 1.5), i, marker='<', ms=5, color=TEXTO2, zorder=4)
        rangos.append((a, b, False))
    for i in range(n):
        tx.axhline(i + 0.5, color=GRILLA, lw=0.4); ax.axhline(i + 0.5, color=GRILLA, lw=0.4)
    for (i, j), (t, kp, ks_) in sorted(arcos.items()):
        if kp in PID:
            xo = X(D(PID[kp]['inicio'])) if t == 'SS' else X(D(PID[kp]['fin_exclusivo']))
        else:
            xo = X(rangos[i][0])
        xd = X(D(PID[ks_]['inicio'])) if ks_ in PID else X(rangos[j][0])
        xo, xd = min(max(xo, X(x0)), X(x1)), min(max(xd, X(x0)), X(x1))
        sgn = 1 if j > i else -1
        estilo = '-' if t == 'FS' else (0, (3, 2))
        ax.plot([xo, xo], [i + (0 if rangos[i][2] else 0.2 * sgn), j], color=TEXTO2, lw=0.7, ls=estilo, zorder=4)
        if abs(xd - xo) > 0.6:
            ax.annotate('', xy=(xd, j), xytext=(xo, j), arrowprops=dict(arrowstyle='-|>', color=TEXTO2, lw=0.7, mutation_scale=7, ls=estilo), zorder=4)
    usadas = {cat(k) for t, _, ks in filas if t == 'act' for k in ks}
    ley = [(Patch(facecolor=ROJO, label='Ruta crítica'), 'critica'), (Patch(facecolor=GRIS, label='Holgura 0 por fecha fija'), 'fija'),
           (Patch(facecolor=AMBAR, label='Holgura ≤ 10 días hábiles'), 'casi'), (Patch(facecolor=AZUL, label='Holgura > 10 días hábiles'), 'normal')]
    ley = [h for h, c in ley if c in usadas] + [Line2D([], [], marker='D', color=TEXTO, lw=0, ms=6, label='Hito'),
           Line2D([], [], color=TEXTO2, lw=0.8, label='Fin–inicio (FI)'), Line2D([], [], color=TEXTO2, lw=0.8, ls=(0, (3, 2)), label='Inicio–inicio (II)')]
    fig.legend(handles=ley, loc='lower left', bbox_to_anchor=(0, 0), ncol=len(ley), frameon=False, fontsize=7, handlelength=1.5, columnspacing=0.8)
    base = os.path.join(AQUI, archivo)
    fig.savefig(base + '.png', dpi=300); fig.savefig(base + '.pdf'); plt.close(fig)
    shutil.copyfile(base + '.pdf', os.path.join(FIG, archivo + '.pdf'))
    print('ok', archivo, 'filas', n, 'flechas', len(arcos), collections.Counter(v[0] for v in arcos.values()))

for v in VISTAS:
    vista(*v)
