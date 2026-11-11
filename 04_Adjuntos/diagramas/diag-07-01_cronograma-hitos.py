"""Figura SD-07 · Cronograma de hitos (nivel 1 de PMBOK 6.5.3.2).

Fuente de datos: red v3 del SD-07 (80_Artefactos/sd-07_contexto/red-v3-2026-11-10/programacion_v3.csv)
y los hitos contractuales del traspaso. No dibuja nada a mano: todo sale de los datos.
Paleta validada (dataviz, validate_palette): #196197, #eb6834, #1baf7a, #6250d6 sobre blanco.
Excepción a diagramas-ancoa autorizada por el usuario (2026-11-10) para cronogramas.
Uso: <python con matplotlib> diag-07-01_cronograma-hitos.py
"""
import csv, os
from datetime import date, timedelta
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from matplotlib import font_manager

for _f in ('Lato-Regular.ttf', 'Lato-Bold.ttf', 'Lato-Semibold.ttf'):  # tipografía del informe, si está instalada
    _r = os.path.join('/usr/share/fonts/truetype/lato', _f)
    if os.path.exists(_r):
        font_manager.fontManager.addfont(_r)
MESES_ES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
PROG = os.path.join(RAIZ, '80_Artefactos/sd-07_contexto/red-v3-2026-11-10/programacion_v3.csv')
HITOS = os.path.join(RAIZ, '80_Artefactos/sd-07_contexto/traspaso-2026-11-10/Red_CPM/Hitos_contractuales.csv')
SALIDA = os.path.join(AQUI, 'diag-07-01_cronograma-hitos')

AZUL, NARANJA, AQUA, VIOLETA = '#196197', '#eb6834', '#1baf7a', '#6250d6'
TEXTO, TEXTO2, GRILLA = '#17324D', '#52514e', '#e6e6e3'
GRIS_CONG, GRIS_CLASES, GRIS_EVENTO = '#d9d9d6', '#ececea', '#f4f4f2'
plt.rcParams.update({'font.family': 'Lato', 'font.size': 9, 'text.color': TEXTO, 'axes.labelcolor': TEXTO,
                     'xtick.color': TEXTO2, 'ytick.color': TEXTO, 'axes.edgecolor': GRILLA})
D = date.fromisoformat
M1 = D('2027-01-07')
def mes_ini(m):  # inicio del mes contractual m (cada mes empieza el día 7)
    y, mm = divmod(M1.month - 1 + m - 1, 12)
    return date(M1.year + y, mm + 1, 7)

prog = {r['id']: r for r in csv.DictReader(open(PROG, encoding='utf-8-sig'), delimiter=';')}
hitos = list(csv.DictReader(open(HITOS, encoding='utf-8-sig')))
CORTO = {'H1': 'Línea base de alcance y trazabilidad', 'H2': 'Arquitectura, seguridad y modelo de datos',
         'H3': 'Infraestructura híbrida y ambientes', 'H4': 'Software E1 para pruebas (QA superado)',
         'H5': 'Certificación de la Etapa 1', 'H6': 'Inicio de la marcha blanca E1',
         'H7': 'Producción E1 en 22 tiendas', 'H8': 'Línea base y diseño de la Etapa 2',
         'H9': 'Software E2 para pruebas', 'H10': 'Certificación de la Etapa 2',
         'H11': 'Inicio de la marcha blanca E2', 'H12': 'Producción E2 e inicio de la operación'}

FASES = [  # (rótulo, inicio, fin exclusivo, color)
    ('Desarrollo Etapa 1', mes_ini(1), mes_ini(13), AZUL),
    ('Marcha blanca E1', mes_ini(13), mes_ini(16), AQUA),
    ('Desarrollo Etapa 2', mes_ini(13), mes_ini(19), NARANJA),
    ('Marcha blanca E2', mes_ini(19), mes_ini(21), AQUA),
    ('Operación (M21–M56)', mes_ini(21), mes_ini(22) + timedelta(days=12), VIOLETA),
]
BANDAS = [  # restricciones del cliente (SD-07 §7.3.2)
    (D('2027-01-25'), D('2027-03-08'), GRIS_CLASES), (D('2027-04-24'), D('2027-07-03'), GRIS_EVENTO),
    (D('2027-11-01'), D('2028-01-07'), GRIS_CONG), (D('2028-01-25'), D('2028-03-08'), GRIS_CLASES),
    (D('2028-04-24'), D('2028-07-03'), GRIS_EVENTO),
]

fig, ax = plt.subplots(figsize=(9.7, 6.0))
x0, x1 = mes_ini(1) - timedelta(days=4), mes_ini(22) + timedelta(days=16)
filas = [f[0] for f in FASES] + [h['hito'] for h in hitos]
y = {nombre: i for i, nombre in enumerate(filas)}
for a, b, c in BANDAS:
    ax.axvspan(a, b, color=c, zorder=0, lw=0)
for nombre, a, b, c in FASES:
    ax.barh(y[nombre], (b - a).days, left=a, height=0.62, color=c, edgecolor='white', linewidth=2, zorder=3)
ax.annotate('continúa hasta el 6-9-2031', xy=(FASES[-1][2], y[FASES[-1][0]]), xytext=(4, 0),
            textcoords='offset points', va='center', fontsize=9, color=TEXTO2)
for h in hitos:
    k = 'A:' + h['hito']
    fecha = D(prog[k]['fin_exclusivo'])
    temprana = D(prog[k]['inicio_temprano'])
    holg = (fecha - temprana).days
    yy = y[h['hito']]
    if holg > 0:
        ax.plot([temprana, fecha], [yy, yy], color=TEXTO2, lw=2, solid_capstyle='round', zorder=4)
    ax.scatter([fecha], [yy], marker='D', s=46, color=TEXTO if holg > 0 else NARANJA,
               edgecolor='white', linewidth=1.5, zorder=5)
    txt = f"M{h['mes_contractual']} · {fecha.strftime('%d-%m-%Y')} · " + (f'holgura {holg} d' if holg > 0 else 'sin holgura')
    ax.annotate(txt, xy=(fecha, yy), xytext=(7, 0), textcoords='offset points', va='center', fontsize=9,
                color=TEXTO if holg > 0 else NARANJA)
ax.set_yticks(range(len(filas)))
ax.set_yticklabels([f[0] for f in FASES] + [f"{h['hito']}  {CORTO[h['hito']]}" for h in hitos])
ax.invert_yaxis()
ax.axhline(len(FASES) - 0.5, color=GRILLA, lw=1)
ax.set_xlim(x0, x1)
ticks = [mes_ini(m) for m in range(1, 23, 2)]
ax.set_xticks(ticks)
ax.set_xticklabels([f"M{m}\n{MESES_ES[mes_ini(m).month - 1]} {mes_ini(m).year % 100:02d}" for m in range(1, 23, 2)],
                   fontsize=9)
ax.grid(axis='x', color=GRILLA, lw=0.8, zorder=1)
ax.tick_params(axis='y', length=0)
for s in ('top', 'right', 'left'):
    ax.spines[s].set_visible(False)
leyenda = [Patch(color=AZUL, label='Etapa 1'), Patch(color=NARANJA, label='Etapa 2'),
           Patch(color=AQUA, label='Marcha blanca'), Patch(color=VIOLETA, label='Operación'),
           Line2D([], [], color=TEXTO2, lw=2, label='Holgura del hito (fecha temprana → contractual)'),
           Line2D([], [], marker='D', color='none', markerfacecolor=NARANJA, markeredgecolor='white', markersize=7,
                  label='Hito sin holgura'),
           Patch(color=GRIS_CONG, label='Congelamiento de fin de año'), Patch(color=GRIS_CLASES, label='Vuelta a clases'),
           Patch(color=GRIS_EVENTO, label='Envolvente de eventos')]
ax.legend(handles=leyenda, loc='upper center', bbox_to_anchor=(0.5, -0.11), ncol=3, frameon=False, fontsize=9)
fig.text(0.01, 0.005, 'Fuente: elaboración propia a partir de la red CPM v3 del plan de trabajo (978 nodos) y del Formulario E-25.',
         fontsize=9, color=TEXTO2)
fig.tight_layout(rect=(0, 0.02, 1, 1))
fig.savefig(SALIDA + '.png', dpi=300)
fig.savefig(SALIDA + '.pdf')
print('ok', SALIDA)
