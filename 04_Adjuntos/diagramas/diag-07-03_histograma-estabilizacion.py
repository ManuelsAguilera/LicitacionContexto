"""Figura SD-07 · Histograma de recursos antes y después de la estabilización (PMBOK 6.5.2.3 y 6.5.3.3).

Compara, sobre la misma red v3, los inicios propuestos del traspaso (sin estabilizar) con la
programación estabilizada con margen mínimo de 10 días. Muestra el trabajo de la red (M1–M21) en
personas equivalentes (FTE = HH ÷ 160) por grupo de perfiles; excluye la cobertura de campo de M16,
la dirección y la operación, que no se estabilizan. Las HH de cada actividad se reparten de forma
uniforme en sus días hábiles.
Paleta validada (dataviz, validate_palette, 7 categorías sobre blanco).
Uso: <python con matplotlib> diag-07-03_histograma-estabilizacion.py
"""
import csv, json, os, collections
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
SALIDA = os.path.join(AQUI, 'diag-07-03_histograma-estabilizacion')

TEXTO, TEXTO2, GRILLA, SOMBRA = '#17324D', '#52514e', '#e6e6e3', '#f1f1ef'
plt.rcParams.update({'font.family': 'Lato', 'font.size': 9, 'text.color': TEXTO, 'axes.labelcolor': TEXTO,
                     'xtick.color': TEXTO2, 'ytick.color': TEXTO2, 'axes.edgecolor': GRILLA})
GRUPOS = [  # (grupo, color validado, perfiles de la red)
    ('Desarrollo', '#196197', {'Desarrollador', 'Líder técnico / coordinación de desarrollo'}),
    ('Arquitectura', '#eb6834', {'Arquitecto / diseñador técnico'}),
    ('Análisis y UX', '#1baf7a', {'Analista de negocio', 'UX / investigador'}),
    ('Calidad', '#eda100', {'Ingeniero QA', 'QA / probador'}),
    ('Datos', '#e87ba4', {'Especialista de datos', 'Científico de datos / ML'}),
    ('Infraestructura y plataforma', '#008300', {'SRE / plataforma', 'Ingeniero infraestructura física',
                                                  'Especialista de redes', 'Especialista IoT / hardware', 'Implantador'}),
    ('Otros perfiles', '#6250d6', None),
]
def grupo(rol):
    for g, _, roles in GRUPOS:
        if roles and rol in roles:
            return g
    return 'Otros perfiles'

M1 = date(2027, 1, 7)
def mes(ds):
    d = date.fromisoformat(ds)
    m = (d.year - M1.year) * 12 + d.month - M1.month + 1
    return m if d.day >= 7 else m - 1
cals = json.load(open(CALS, encoding='utf-8-sig'))
carga = {k: collections.defaultdict(float) for k in ('antes', 'despues')}
for r in csv.DictReader(open(PROG, encoding='utf-8-sig'), delimiter=';'):
    roles = json.loads(r['HH_por_rol_json'])
    if not roles or float(r['HH']) <= 0 or r['id'].startswith(('CAMPO', 'FIELD')):
        continue
    ds = cals[r['calendario']]
    for clave, (a, b) in {'antes': (r['inicio_sin_estabilizar'], r['fin_sin_estabilizar']),
                          'despues': (r['inicio'], r['fin_exclusivo'])}.items():
        dias = ds[bisect_left(ds, a):bisect_left(ds, b)] or [a]
        for rol, hh in roles.items():
            for d in dias:
                carga[clave][(mes(d), grupo(rol))] += hh / len(dias)

MESES = list(range(1, 22))
fig, axes = plt.subplots(2, 1, figsize=(9.7, 6.6), sharex=True, sharey=True)
titulos = {'antes': 'Programación sin estabilizar (inicios propuestos del traspaso)',
           'despues': 'Programación estabilizada con margen mínimo de 10 días (red v3)'}
for ax, clave in zip(axes, ('antes', 'despues')):
    for a, b in ((12.5, 15.5), (18.5, 20.5)):
        ax.axvspan(a, b, color=SOMBRA, zorder=0, lw=0)
    base = [0.0] * len(MESES)
    for g, color, _ in GRUPOS:
        v = [carga[clave][(m, g)] / 160 for m in MESES]
        ax.bar(MESES, v, bottom=base, width=0.78, color=color, edgecolor='white', linewidth=0.8, zorder=3)
        base = [x + y for x, y in zip(base, v)]
    pico = max(range(len(MESES)), key=lambda i: base[i])
    ax.annotate(f'{base[pico]:.1f}', xy=(MESES[pico], base[pico]), xytext=(0, 3), textcoords='offset points',
                ha='center', fontsize=9, color=TEXTO)
    for m in (15,):
        i = MESES.index(m)
        if i != pico:
            ax.annotate(f'{base[i]:.1f}', xy=(m, base[i]), xytext=(0, 3), textcoords='offset points',
                        ha='center', fontsize=9, color=TEXTO)
    ax.set_title(titulos[clave], loc='left', fontsize=9, fontweight='bold', color=TEXTO)
    ax.set_ylabel('Personas equivalentes (FTE)')
    ax.grid(axis='y', color=GRILLA, lw=0.8, zorder=1)
    for s in ('top', 'right', 'left'):
        ax.spines[s].set_visible(False)
    ax.tick_params(axis='y', length=0)
tope = max(ax.get_ylim()[1] for ax in axes) * 1.18  # espacio para los rótulos sobre las barras
for ax in axes:
    ax.set_ylim(0, tope)
for ax in axes:
    ax.text(14, ax.get_ylim()[1] * 0.97, 'Solapamiento M13–M15', ha='center', va='top', fontsize=9, color=TEXTO2)
    ax.text(19.5, ax.get_ylim()[1] * 0.97, 'M19–M20', ha='center', va='top', fontsize=9, color=TEXTO2)
axes[1].set_xticks(MESES)
axes[1].set_xticklabels([f'M{m}' for m in MESES], fontsize=9)
fig.legend(handles=[Patch(color=c, label=g) for g, c, _ in GRUPOS], loc='lower center', ncol=4, frameon=False,
           bbox_to_anchor=(0.5, 0.035), fontsize=9)
fig.text(0.01, 0.005, 'Fuente: elaboración propia a partir de la red CPM v3. Trabajo de la red; excluye la cobertura de campo '
         'de M16, la dirección y la operación.', fontsize=9, color=TEXTO2)
fig.tight_layout(rect=(0, 0.1, 1, 1))
fig.savefig(SALIDA + '.png', dpi=300)
fig.savefig(SALIDA + '.pdf')
print('ok', SALIDA)
