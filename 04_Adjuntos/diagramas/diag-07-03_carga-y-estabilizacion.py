"""Figuras SD-07 · Carga mensual (A) y efecto de la estabilización en el primer solapamiento (B).

A: personas equivalentes (HH ÷ 160, redondeadas hacia arriba) del trabajo programado, M1–M21, un solo color, solapamientos sombreados.
Fuente de las HH: la misma matriz del Formulario T-15 (columna «Proyecto y campo» sin la cobertura de campo).
B: acercamiento a M12–M18, programación sin estabilizar (gris) frente a la estabilizada (azul).
Ambas miden el trabajo de la red; no incluyen la cobertura de campo de M16, la dirección ni la operación.
La programación sin estabilizar devuelve las actividades desplazadas a su inicio original (reparto uniforme en sus días hábiles).
Tamaño real: 17,6 cm de ancho y letra de 9 pt (se insertan sin escalar).
Uso: <python con matplotlib> diag-07-03_carga-y-estabilizacion.py
Salida: diag-07-03_carga-mensual.(png|pdf) y diag-07-08_estabilizacion-solapamiento.(png|pdf)
"""
import csv, json, os, collections, shutil
from bisect import bisect_left
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
PROG = os.path.join(RAIZ, '80_Artefactos/sd-07_contexto/red-v3-2026-11-10/programacion_v3.csv')
CALS = os.path.join(RAIZ, '80_Artefactos/sd-07_contexto/traspaso-2026-11-10/Red_CPM/calendarios.json')
FIG = os.path.join(RAIZ, '02_Propuesta/latex_final/figuras/sd07-figuras')
AZUL, GRIS_BARRA, TEXTO, TEXTO2, GRILLA, SOMBRA = '#196197', '#b4bcc6', '#17324D', '#52514e', '#e6e6e3', '#efefec'
W = 6.93
plt.rcParams.update({'font.family': 'Lato', 'font.size': 9, 'text.color': TEXTO, 'axes.labelcolor': TEXTO,
                     'xtick.color': TEXTO2, 'ytick.color': TEXTO2, 'axes.edgecolor': GRILLA,
                     'xtick.labelsize': 9, 'ytick.labelsize': 9})

M1 = date(2027, 1, 7)
def mes(ds):
    d = date.fromisoformat(ds)
    m = (d.year - M1.year) * 12 + d.month - M1.month + 1
    return m if d.day >= 7 else m - 1
cals = json.load(open(CALS, encoding='utf-8-sig'))
MATRIZ = os.path.join(RAIZ, '80_Artefactos/sd-07_contexto/red-v3-2026-11-10/HH_matriz_roles_M1_M56.csv')
COBERTURAS = os.path.join(RAIZ, '80_Artefactos/sd-07_contexto/traspaso-2026-11-10/HH_detalle_mes_rol_componente.csv')
num = lambda t: float(t.replace('.', '').replace(',', '.')) if t.count(',') == 1 and '.' in t else float(t.replace(',', '.'))
# Estabilizada: matriz de HH del T-15 (trabajo técnico y viajes), sin las coberturas de campo, dirección y operación.
despues = collections.defaultdict(float)
for r in csv.DictReader(open(MATRIZ, encoding='utf-8-sig'), delimiter=';'):
    for m in range(1, 57):
        despues[m] += float(r[f'M{m}'].replace(',', '.'))
for r in csv.DictReader(open(COBERTURAS, encoding='utf-8-sig'), delimiter=';'):
    if r['Componente'] != 'Trabajo técnico y viajes':
        despues[int(r['Mes'][1:])] -= float(r['HH'].replace('.', '').replace(',', '.'))
# Sin estabilizar: la misma matriz, devolviendo cada actividad desplazada a su inicio sin estabilizar.
antes = collections.defaultdict(float, despues)
def reparto(r, a, b, signo, destino):
    ds = cals[r['calendario']]
    dias = ds[bisect_left(ds, a):bisect_left(ds, b)] or [a]
    for d in dias:
        destino[mes(d)] += signo * float(r['HH']) / len(dias)
for r in csv.DictReader(open(PROG, encoding='utf-8-sig'), delimiter=';'):
    if float(r['HH']) > 0 and r['inicio'] != r['inicio_sin_estabilizar']:
        reparto(r, r['inicio'], r['fin_exclusivo'], -1, antes)
        reparto(r, r['inicio_sin_estabilizar'], r['fin_sin_estabilizar'], +1, antes)
carga = {'antes': antes, 'despues': despues}
import math
# personas equivalentes redondeadas hacia arriba: no se asigna una fracción de persona
fte = {k: {m: math.ceil(v / 160 - 1e-9) for m, v in d.items()} for k, d in carga.items()}

def ejes(ax):
    ax.grid(axis='y', color=GRILLA, lw=0.8, zorder=1)
    for s in ('top', 'right', 'left'):
        ax.spines[s].set_visible(False)
    ax.tick_params(axis='y', length=0)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f'{v:.0f}'))

def guardar(fig, nombre):
    base = os.path.join(AQUI, nombre)
    fig.savefig(base + '.png', dpi=300); fig.savefig(base + '.pdf'); plt.close(fig)
    shutil.copyfile(base + '.pdf', os.path.join(FIG, nombre + '.pdf'))
    print('ok', nombre)

# ---------- A: carga mensual ----------
MESES = list(range(1, 22))
v = [fte['despues'].get(m, 0) for m in MESES]
fig, ax = plt.subplots(figsize=(W, 2.9))
for a, b, t in ((12.5, 15.5, 'Solapamiento M13–M15'), (18.5, 20.5, 'Solapamiento M19–M20')):
    ax.axvspan(a, b, color=SOMBRA, zorder=0, lw=0)
    ax.text((a + b) / 2, 47, t, ha='center', va='top', fontsize=9, color=TEXTO2)
ax.bar(MESES, v, width=0.72, color=AZUL, zorder=3)
for m in MESES:
    ax.annotate(str(v[m - 1]), xy=(m, v[m - 1]), xytext=(0, 2), textcoords='offset points', ha='center', fontsize=7.5, color=TEXTO2)
ax.set_xticks(MESES); ax.set_xticklabels([f'M{m}' for m in MESES])
ax.set_xlim(0.4, 21.6); ax.set_ylim(0, 48)
ax.set_ylabel('Personas equivalentes')
ejes(ax)
fig.tight_layout(pad=0.3)
guardar(fig, 'diag-07-03_carga-mensual')

# ---------- B: estabilización en M12–M18 ----------
MB = list(range(12, 19))
a_ = [fte['antes'].get(m, 0) for m in MB]; d_ = [fte['despues'].get(m, 0) for m in MB]
fig, ax = plt.subplots(figsize=(W, 2.9))
ax.axvspan(12.5, 15.5, color=SOMBRA, zorder=0, lw=0)
ax.text(14, 59, 'Solapamiento M13–M15', ha='center', va='top', fontsize=9, color=TEXTO2)
x = list(range(len(MB)))
ax.bar([m - 0.19 for m in MB], a_, width=0.36, color=GRIS_BARRA, zorder=3, label='Sin estabilizar')
ax.bar([m + 0.19 for m in MB], d_, width=0.36, color=AZUL, zorder=3, label='Estabilizada')
for m, va, vd in zip(MB, a_, d_):
    ax.annotate(str(va), xy=(m - 0.19, va), xytext=(0, 2), textcoords='offset points', ha='center', fontsize=7.5, color=TEXTO2)
    ax.annotate(str(vd), xy=(m + 0.19, vd), xytext=(0, 2), textcoords='offset points', ha='center', fontsize=7.5, color=TEXTO)
ax.set_xticks(MB); ax.set_xticklabels([f'M{m}' for m in MB])
ax.set_xlim(11.4, 18.6); ax.set_ylim(0, 60)
ax.set_ylabel('Personas equivalentes')
ax.legend(loc='upper right', frameon=False, fontsize=9)
ejes(ax)
fig.tight_layout(pad=0.3)
guardar(fig, 'diag-07-08_estabilizacion-solapamiento')
print('antes', fte['antes']); print('despues', fte['despues'])
