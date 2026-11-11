"""Figura SD-07 · Cronograma resumen por rama de la EDT (nivel 2 de PMBOK 6.5.3.2).

Una fila por rama (1.1–1.15). Las barras unen las ventanas de las actividades de la red v3 por etapa;
el borde oscuro marca tramos con actividades sin margen (ruta crítica de la programación estabilizada).
La columna «Recibe trabajo de» lista las ramas que entregan insumos a cada rama, siguiendo las
relaciones reales de la red a través de hitos y controles intermedios.
La dotación que no es actividad de la red (dirección, campo de M16, operación) sale de Dotacion_coberturas.csv.
Paleta validada (dataviz): #196197, #eb6834, #1baf7a, #6250d6; transversal en trama neutra.
Uso: <python con matplotlib> diag-07-02_cronograma-resumen-ramas.py
"""
import csv, json, os, collections
from datetime import date, timedelta
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Patch, Rectangle

for _f in ('Lato-Regular.ttf', 'Lato-Bold.ttf'):
    _r = os.path.join('/usr/share/fonts/truetype/lato', _f)
    if os.path.exists(_r):
        font_manager.fontManager.addfont(_r)
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
RV3 = os.path.join(RAIZ, '80_Artefactos/sd-07_contexto/red-v3-2026-11-10')
SALIDA = os.path.join(AQUI, 'diag-07-02_cronograma-resumen-ramas')

AZUL, NARANJA, AQUA, VIOLETA = '#196197', '#eb6834', '#1baf7a', '#6250d6'
TEXTO, TEXTO2, GRILLA = '#17324D', '#52514e', '#e6e6e3'
plt.rcParams.update({'font.family': 'Lato', 'font.size': 9, 'text.color': TEXTO, 'axes.labelcolor': TEXTO,
                     'xtick.color': TEXTO2, 'ytick.color': TEXTO, 'axes.edgecolor': GRILLA, 'hatch.linewidth': 0.6})
MESES_ES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
RAMAS = {'1.1': 'Dirección y control', '1.2': 'Levantamiento y alcance', '1.3': 'Arquitectura y diseño',
         '1.4': 'Infraestructura híbrida', '1.5': 'Desarrollo de software', '1.6': 'Integraciones',
         '1.7': 'Migración de datos', '1.8': 'Seguridad y cumplimiento', '1.9': 'Calidad y certificación',
         '1.10': 'Innovaciones', '1.11': 'Implantación', '1.12': 'Marchas blancas y actas',
         '1.13': 'Cambio y capacitación', '1.14': 'Documentación y traspaso', '1.15': 'Operación y soporte'}
CAT = {'E1': ('Etapa 1', AZUL), 'E2': ('Etapa 2', NARANJA), 'MB': ('Marcha blanca', AQUA),
       'OP': ('Operación', VIOLETA), 'TR': ('Transversal (dirección y gobierno)', None)}
D = date.fromisoformat
M1 = date(2027, 1, 7)
def mes_ini(m):
    y, mm = divmod(M1.month - 1 + m - 1, 12)
    return date(M1.year + y, mm + 1, 7)
FIN_VISTA = mes_ini(25)

def rama(edt):
    p = edt.split('.')
    return '.'.join(p[:2]) if len(p) >= 2 else ''
def categoria(r):
    t = (r['id'] + ' ' + r['etapa']).upper()
    if 'MB' in t:
        return 'MB'
    if r['etapa'] == 'E2':
        return 'E2'
    if r['inicio'] >= mes_ini(21).isoformat():
        return 'OP'
    return 'E1'

prog = {r['id']: r for r in csv.DictReader(open(os.path.join(RV3, 'programacion_v3.csv'), encoding='utf-8-sig'), delimiter=';')}
tramos = collections.defaultdict(list)   # (rama, cat) -> [(ini, fin)]
criticos = collections.defaultdict(list)  # rama -> [(ini, fin)]
for k, r in prog.items():
    ra = rama(r['edt'])
    if ra not in RAMAS or float(r['HH'] or 0) <= 0:
        continue
    a, b = D(r['inicio']), D(r['fin_exclusivo'])
    tramos[(ra, categoria(r))].append((a, b))
    if r['inicio'] >= r['inicio_tardio']:   # sin margen en la programación estabilizada
        criticos[ra].append((a, b))
# Dotación fuera de la red (Dotacion_coberturas.csv)
tramos[('1.1', 'TR')].append((mes_ini(1), mes_ini(57)))
tramos[('1.15', 'OP')].append((mes_ini(21), mes_ini(57)))
tramos[('1.8', 'OP')].append((mes_ini(21), mes_ini(57)))
tramos[('1.11', 'E1')].append((D('2028-04-07'), D('2028-04-21')))
tramos[('1.13', 'E2')].append((mes_ini(20), mes_ini(21)))

def unir(iv, hueco=10):
    iv = sorted(iv); out = []
    for a, b in iv:
        if out and (a - out[-1][1]).days <= hueco:
            out[-1] = (out[-1][0], max(out[-1][1], b))
        else:
            out.append((a, b))
    return out

# Dependencias entre ramas: de cada actividad, recorrer predecesoras pasando por nodos sin EDT (hitos, controles)
rel = json.load(open(os.path.join(RV3, 'Red_CPM/relaciones.json'), encoding='utf-8-sig'))
pred = collections.defaultdict(list)
for e in rel:
    pred[e['succ']].append(e['pred'])
def ramas_previas(k, limite=60):
    vistos, pila, hallado = {k}, sorted(pred[k], reverse=True), set()
    while pila and len(vistos) < limite:
        p = pila.pop()
        if p in vistos:
            continue
        vistos.add(p)
        ra = rama(prog[p]['edt']) if p in prog and prog[p]['edt'] else ''
        if ra in RAMAS:
            hallado.add(ra)
        else:
            pila.extend(sorted(pred[p], reverse=True))
    return hallado
recibe = collections.defaultdict(collections.Counter)
for k in sorted(prog):
    r = prog[k]
    ra = rama(r['edt'])
    if ra in RAMAS:
        for q in ramas_previas(k):
            if q != ra:
                recibe[ra][q] += 1
orden = sorted(RAMAS, key=lambda x: int(x.split('.')[1]))
def recibe_txt(ra):
    clave_r = lambda q: [int(x) for x in q.split('.')]
    top = [q for q, _ in sorted(recibe[ra].items(), key=lambda t: (-t[1], clave_r(t[0])))[:3]]
    return ', '.join(top) if top else '—'

fig = plt.figure(figsize=(9.7, 6.3))
gs = fig.add_gridspec(1, 2, width_ratios=[2.15, 4.6], wspace=0.01)
axt, ax = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])
ax.axvspan(D('2027-11-01'), D('2028-01-07'), color='#ececea', lw=0, zorder=0)
for i, ra in enumerate(orden):
    for c, (nombre, color) in CAT.items():
        for a, b in unir(tramos.get((ra, c), [])):
            a2, b2 = max(a, mes_ini(1)), min(b, FIN_VISTA)
            if a2 >= b2:
                continue
            if color:
                ax.barh(i, (b2 - a2).days, left=a2, height=0.56, color=color, edgecolor='white', linewidth=1, zorder=3)
            else:
                ax.barh(i, (b2 - a2).days, left=a2, height=0.56, color='white', edgecolor=TEXTO2, hatch='////',
                        linewidth=0.6, zorder=2)
            if b > FIN_VISTA:
                ax.annotate('→ M56', xy=(FIN_VISTA, i), xytext=(3, 0), textcoords='offset points', va='center',
                            fontsize=9, color=TEXTO2, annotation_clip=False)
    for a, b in unir(criticos.get(ra, []), hueco=3):
        a2, b2 = max(a, mes_ini(1)), min(b, FIN_VISTA)
        if a2 < b2:
            ax.add_patch(Rectangle((matplotlib.dates.date2num(a2), i - 0.33), (b2 - a2).days, 0.66, fill=False,
                                   edgecolor=TEXTO, linewidth=1.4, zorder=4))
ax.set_yticks(range(len(orden)))
ax.set_yticklabels([])
ax.invert_yaxis()
ax.set_xlim(mes_ini(1) - timedelta(days=4), FIN_VISTA)
ticks = list(range(1, 26, 2))
ax.set_xticks([mes_ini(m) for m in ticks])
ax.set_xticklabels([f'M{m}\n{MESES_ES[mes_ini(m).month - 1]} {mes_ini(m).year % 100:02d}' for m in ticks], fontsize=9)
ax.grid(axis='x', color=GRILLA, lw=0.8, zorder=1)
ax.tick_params(axis='y', length=0)
for s in ('top', 'right', 'left'):
    ax.spines[s].set_visible(False)
# Columna de dependencias (a la izquierda del eje, alineada por fila)
axt.set_ylim(ax.get_ylim()); axt.axis('off')
axt.set_xlim(0, 1)
axt.text(0.0, -0.9, 'Rama de la EDT', fontsize=9, fontweight='bold', color=TEXTO, va='bottom')
axt.text(0.68, -0.9, 'Recibe de', fontsize=9, fontweight='bold', color=TEXTO, va='bottom')
for i, ra in enumerate(orden):
    axt.text(0.0, i, f'{ra}  {RAMAS[ra]}', fontsize=9, color=TEXTO, va='center')
    axt.text(0.68, i, recibe_txt(ra), fontsize=9, color=TEXTO2, va='center')
ax.text(mes_ini(1), -0.9, 'Ventana de trabajo', fontsize=9, fontweight='bold', color=TEXTO, va='bottom')
leyenda = [Patch(color=AZUL, label='Etapa 1'), Patch(color=NARANJA, label='Etapa 2'), Patch(color=AQUA, label='Marcha blanca'),
           Patch(color=VIOLETA, label='Operación (continúa hasta M56)'),
           Patch(facecolor='white', edgecolor=TEXTO2, hatch='////', label='Transversal (dirección)'),
           Patch(facecolor='white', edgecolor=TEXTO, linewidth=1.4, label='Tramo con actividades sin margen'),
           Patch(color='#ececea', label='Congelamiento de fin de año')]
fig.legend(handles=leyenda, loc='lower center', ncol=4, frameon=False, bbox_to_anchor=(0.55, 0.035), fontsize=9)
fig.text(0.01, 0.005, 'Fuente: elaboración propia a partir de la red CPM v3 (978 nodos) y Dotacion_coberturas.csv. '
         'El detalle por paquete está en el Formulario T-14.', fontsize=9, color=TEXTO2)
fig.subplots_adjust(left=0.01, right=0.95, top=0.94, bottom=0.2)
fig.savefig(SALIDA + '.png', dpi=300)
fig.savefig(SALIDA + '.pdf')
print('ok', SALIDA)
