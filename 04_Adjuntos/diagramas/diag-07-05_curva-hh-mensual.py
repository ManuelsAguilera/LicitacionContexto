"""Figura SD-07 · Distribución mensual de HH, M1–M56 (red v3).

Suma mensual de la matriz de HH por rol de la red v3 (trabajo, campo, dirección, inducción y operación).
Dos series: implementación (M1–M20) y período de operación (M21–M56). Paleta validada (dataviz).
Uso: <python con matplotlib> diag-07-05_curva-hh-mensual.py
"""
import csv, os
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
MATRIZ = os.path.join(RAIZ, '80_Artefactos/sd-07_contexto/red-v3-2026-11-10/HH_matriz_roles_M1_M56.csv')
SALIDA = os.path.join(AQUI, 'diag-07-05_curva-hh-mensual')
AZUL, VIOLETA, TEXTO, TEXTO2, GRILLA = '#196197', '#6250d6', '#17324D', '#52514e', '#e6e6e3'
plt.rcParams.update({'font.family': 'Lato', 'font.size': 9, 'text.color': TEXTO, 'xtick.color': TEXTO2,
                     'ytick.color': TEXTO2, 'axes.edgecolor': GRILLA})

num = lambda s: float(s.replace(',', '.'))
filas = list(csv.DictReader(open(MATRIZ, encoding='utf-8-sig'), delimiter=';'))
meses = list(range(1, 57))
total = [sum(num(r[f'M{m}']) for r in filas) for m in meses]
fig, ax = plt.subplots(figsize=(9.7, 4.0))
colores = [AZUL if m <= 20 else VIOLETA for m in meses]
ax.bar(meses, total, width=0.8, color=colores, edgecolor='white', linewidth=0.6, zorder=3)
pico = max(range(20), key=lambda i: total[i])
ax.annotate(f'M{meses[pico]}: {total[pico]:,.0f} HH'.replace(',', '.'), xy=(meses[pico], total[pico]), xytext=(6, 2),
            textcoords='offset points', fontsize=9, color=TEXTO)
ax.annotate(f'Operación: {total[29]:,.0f} HH/mes aprox.'.replace(',', '.'), xy=(38, total[37]), xytext=(0, 10),
            textcoords='offset points', ha='center', fontsize=9, color=TEXTO)
ax.set_xticks([1] + list(range(6, 57, 6)))
ax.set_xticklabels([f'M{m}' for m in [1] + list(range(6, 57, 6))])
ax.set_ylabel('HH por mes')
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f'{v:,.0f}'.replace(',', '.')))
ax.grid(axis='y', color=GRILLA, lw=0.8, zorder=1)
for s in ('top', 'right', 'left'):
    ax.spines[s].set_visible(False)
ax.tick_params(axis='y', length=0)
ax.legend(handles=[Patch(color=AZUL, label='Implementación (M1–M20)'), Patch(color=VIOLETA, label='Período de operación (M21–M56)')],
          loc='upper right', frameon=False, fontsize=9)
total_txt = f'{sum(total):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
fig.text(0.01, 0.01, f'Fuente: elaboración propia a partir de la red CPM v3. Total: {total_txt} HH.',
         fontsize=9, color=TEXTO2)
fig.tight_layout(rect=(0, 0.04, 1, 1))
fig.savefig(SALIDA + '.png', dpi=300)
fig.savefig(SALIDA + '.pdf')
print('ok', SALIDA)
