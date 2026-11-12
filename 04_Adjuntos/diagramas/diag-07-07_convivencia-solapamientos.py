"""Figura SD-07 · Qué convive en cada solapamiento (M13–M15 y M19–M20) y qué hito lo cierra.

Dos paneles con cuatro franjas cada uno. Fechas: Formulario E-25 (hitos), Formulario T-18 (habilitación,
cohortes de cartera, evidencia de cuatro semanas) y red del cronograma (inducción de operación).
Tamaño real: 17,6 cm de ancho y letra de 9 pt.
Uso: <python con matplotlib> diag-07-07_convivencia-solapamientos.py
"""
import os, shutil
from datetime import date
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Patch

for _f in ('Lato-Regular.ttf', 'Lato-Bold.ttf'):
    _r = os.path.join('/usr/share/fonts/truetype/lato', _f)
    if os.path.exists(_r):
        font_manager.fontManager.addfont(_r)
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
FIG = os.path.join(RAIZ, '02_Propuesta/latex_final/figuras/sd07-figuras')
NOMBRE = 'diag-07-07_convivencia-solapamientos'
AZUL, NARANJA, VERDE, VIOLETA = '#196197', '#eb6834', '#1baf7a', '#6250d6'
TEXTO, TEXTO2, GRILLA, RESTR = '#17324D', '#52514e', '#e6e6e3', '#d9d9d5'
W = 6.93
plt.rcParams.update({'font.family': 'Lato', 'font.size': 9, 'text.color': TEXTO, 'xtick.color': TEXTO2,
                     'xtick.labelsize': 9, 'hatch.color': 'white', 'hatch.linewidth': 1.0})
D = lambda s: date.fromisoformat(s).toordinal()

def barra(ax, y, a, b, color, texto='', hatch=None, alfa=1.0, color_texto='white'):
    ax.barh(y, D(b) - D(a), left=D(a), height=0.5, color=color, alpha=alfa, hatch=hatch, edgecolor='white', lw=0.6, zorder=3)
    if texto:
        ax.text((D(a) + D(b)) / 2, y, texto, ha='center', va='center', fontsize=9, color=color_texto, zorder=4)

def hito(ax, y, f, etiqueta, arriba=True):
    ax.plot(D(f), y, marker='D', ms=6.5, color=TEXTO, zorder=5)
    ax.text(D(f), y - 0.3, etiqueta, ha='center', va='bottom', fontsize=9, color=TEXTO, zorder=5)

def panel(ax, ini, fin, carriles, meses, titulo):
    ax.set_xlim(D(ini) - 2, D(fin) + 2)
    ax.set_ylim(len(carriles) - 0.45, -0.85)
    ax.set_yticks(range(len(carriles))); ax.set_yticklabels(carriles, fontsize=9, color=TEXTO)
    ax.set_xticks([D(m) for m, _ in meses]); ax.set_xticklabels([t for _, t in meses])
    for m, _ in meses:
        ax.axvline(D(m), color=GRILLA, lw=0.8, zorder=1)
    for s in ('top', 'right', 'left'):
        ax.spines[s].set_visible(False)
    ax.spines['bottom'].set_color(GRILLA)
    ax.tick_params(axis='y', length=0)
    ax.set_title(titulo, loc='left', fontsize=9, fontweight='bold', color=TEXTO, pad=4)

fig, (a1, a2) = plt.subplots(2, 1, figsize=(W, 6.3), gridspec_kw=dict(hspace=0.62))

# ---------- Panel 1: M13–M15 ----------
c1 = ['Marcha blanca E1', 'Desarrollo E2', 'Cartera (filial)', 'Restricción']
panel(a1, '2028-01-07', '2028-04-07', c1,
      [('2028-01-07', '7 ene'), ('2028-02-07', '7 feb'), ('2028-03-07', '7 mar'), ('2028-04-07', '7 abr')],
      'Solapamiento M13–M15 (7 de enero a 6 de abril de 2028)')
barra(a1, 0, '2028-01-12', '2028-03-10', NARANJA, 'operación real supervisada', alfa=0.35, color_texto=TEXTO)
barra(a1, 0, '2028-01-07', '2028-01-12', NARANJA)
a1.text(D('2028-01-13'), -0.3, 'habilitación de las 22 tiendas (7 al 11 de enero)', ha='left', va='bottom', fontsize=9, color=TEXTO)
barra(a1, 0, '2028-03-10', '2028-04-07', NARANJA, 'evidencia de 4 semanas')
hito(a1, 0, '2028-01-07', 'H6'); hito(a1, 0, '2028-04-07', 'H7')
barra(a1, 1, '2028-01-07', '2028-03-07', AZUL, 'diseño y línea base', alfa=0.55)
barra(a1, 1, '2028-03-07', '2028-04-07', AZUL, 'construcción (hasta H9)')
hito(a1, 1, '2028-03-07', 'H8')
barra(a1, 2, '2028-01-10', '2028-01-24', VERDE, 'T1')
barra(a1, 3, '2028-01-25', '2028-03-07', RESTR, 'vuelta a clases', color_texto=TEXTO)
a1.text(0.0, -0.2, 'Los equipos de desarrollo reservan el 30 % de su capacidad para incidencias de la marcha blanca\n'
        'y el 15 % para deuda técnica; el 55 % restante construye la Etapa 2.', transform=a1.transAxes,
        fontsize=9, color=TEXTO2, va='top', ha='left')

# ---------- Panel 2: M19–M20 ----------
c2 = ['E1 en producción', 'Marcha blanca E2', 'Cartera (filial)', 'Operación']
panel(a2, '2028-07-07', '2028-09-07', c2,
      [('2028-07-07', '7 jul'), ('2028-08-07', '7 ago'), ('2028-09-07', '7 sep')],
      'Solapamiento M19–M20 (7 de julio a 6 de septiembre de 2028)')
barra(a2, 0, '2028-07-07', '2028-09-07', AZUL, 'estabilización, continúa hasta M24', alfa=0.85)
barra(a2, 1, '2028-07-07', '2028-08-10', NARANJA, 'operación real supervisada', alfa=0.35, color_texto=TEXTO)
barra(a2, 1, '2028-08-10', '2028-09-07', NARANJA, 'evidencia de 4 semanas')
hito(a2, 1, '2028-07-07', 'H11'); hito(a2, 1, '2028-09-07', 'H12')
barra(a2, 2, '2028-07-07', '2028-07-21', VERDE, 'T2')
barra(a2, 2, '2028-07-21', '2028-08-04', VERDE, 'T3')
hito(a2, 2, '2028-08-04', 'cohortes conciliadas')
barra(a2, 3, '2028-08-24', '2028-08-27', VIOLETA)
a2.text(D('2028-08-23'), 3, 'inducción del equipo de 26 personas', ha='right', va='center', fontsize=9, color=TEXTO)
a2.annotate('', xy=(D('2028-09-07'), 3), xytext=(D('2028-08-28'), 3),
            arrowprops=dict(arrowstyle='->', color=VIOLETA, lw=1.2))
a2.text(D('2028-09-06'), 2.7, 'inicio M21', ha='right', va='bottom', fontsize=9, color=TEXTO2)

fig.subplots_adjust(left=0.19, right=0.975, top=0.955, bottom=0.05)
base = os.path.join(AQUI, NOMBRE)
fig.savefig(base + '.png', dpi=300); fig.savefig(base + '.pdf')
shutil.copyfile(base + '.pdf', os.path.join(FIG, NOMBRE + '.pdf'))
print('ok', NOMBRE)
