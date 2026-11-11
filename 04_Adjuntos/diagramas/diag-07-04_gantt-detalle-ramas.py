"""Figura SD-07 · Gantt detallado por rama (nivel 3 de PMBOK 6.5.3.2) · anexo del Formulario T-14.

Una lámina por rama (las ramas largas se dividen en varias láminas). Cada fila es un elemento de tercer
nivel de la EDT (X.Y.Z): paquete de trabajo, o cuenta de control en 1.5 y 1.10. Las barras unen las
ventanas de sus actividades en la red v3 por etapa; el borde oscuro marca actividades sin margen.
Columnas: código, nombre, HH, ventana (meses) y margen mínimo en días hábiles.
Paleta validada (dataviz): #196197, #eb6834, #1baf7a, #6250d6.
Uso: <python con matplotlib> diag-07-04_gantt-detalle-ramas.py [rama ...]   (sin argumentos: todas)
"""
import csv, os, sys, collections, math
from bisect import bisect_left
from datetime import date, timedelta
import json
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
CALS = os.path.join(RAIZ, '80_Artefactos/sd-07_contexto/traspaso-2026-11-10/Red_CPM/calendarios.json')
LEDGER = os.path.join(RAIZ, '80_Artefactos/sd-07_contexto/traspaso-2026-11-10/Red_CPM/ledger_275_paquetes.json')

AZUL, NARANJA, AQUA, VIOLETA = '#196197', '#eb6834', '#1baf7a', '#6250d6'
TEXTO, TEXTO2, GRILLA = '#17324D', '#52514e', '#e6e6e3'
plt.rcParams.update({'font.family': 'Lato', 'font.size': 9, 'text.color': TEXTO, 'xtick.color': TEXTO2,
                     'axes.edgecolor': GRILLA})
MESES_ES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
RAMAS = {'1.1': 'Dirección, gobierno y control del proyecto', '1.2': 'Levantamiento y línea base de alcance',
         '1.3': 'Arquitectura y diseño', '1.4': 'Infraestructura híbrida y plataforma base',
         '1.5': 'Desarrollo de software', '1.6': 'Integraciones', '1.7': 'Migración y saneamiento de datos',
         '1.8': 'Seguridad, identidad y cumplimiento', '1.9': 'Calidad, pruebas y certificación',
         '1.10': 'Innovaciones', '1.11': 'Implantación y despliegue',
         '1.12': 'Resultados de las marchas blancas y aceptación por etapa', '1.13': 'Gestión del cambio y capacitación',
         '1.14': 'Documentación, transferencia y reversibilidad', '1.15': 'Operación y soporte'}
CAT = {'E1': ('Etapa 1', AZUL), 'E2': ('Etapa 2', NARANJA), 'MB': ('Marcha blanca', AQUA), 'OP': ('Operación', VIOLETA)}
FILAS_POR_LAMINA = 18
D = date.fromisoformat
M1 = date(2027, 1, 7)
def mes_ini(m):
    y, mm = divmod(M1.month - 1 + m - 1, 12)
    return date(M1.year + y, mm + 1, 7)
def num_mes(d):
    m = (d.year - M1.year) * 12 + d.month - M1.month + 1
    return m if d.day >= 7 else m - 1
def tercer_nivel(edt):
    return '.'.join(edt.split('.')[:3])
def categoria(r):
    t = (r['id'] + ' ' + r['etapa']).upper()
    if 'MB' in t:
        return 'MB'
    if r['etapa'] == 'E2':
        return 'E2'
    if r['inicio'] >= mes_ini(21).isoformat():
        return 'OP'
    return 'E1'
def clave(e):
    return [int(x) for x in e.split('.')]

cals = json.load(open(CALS, encoding='utf-8-sig'))
nombres = {p['edt']: p['name'] for p in json.load(open(LEDGER, encoding='utf-8-sig'))['packages']}
CUENTAS = os.path.join(RV3, 'nombres_cuentas_T14.csv')  # nombres de las cuentas 1.5.x y 1.10.x (diccionario del T-14)
if os.path.exists(CUENTAS):
    for _r in csv.reader(open(CUENTAS, encoding='utf-8-sig'), delimiter=';'):
        if _r and _r[0].startswith('1.'):
            nombres[_r[0]] = _r[1]
nombres.update({'1.4.2': 'Red de sitio y segmentación (25 sitios)',  # actualizado en la red v2 (traspaso del SD-04)
                '1.4.3': 'Entornos dedicados de la Filial y del Control de cruces',
                # Paquetes nuevos de las redes v2 y v3 (traspaso del SD-04)
                '1.4.14': 'Levantamiento físico de 25 sitios', '1.4.15': 'Tienda de laboratorio en Preproducción',
                '1.4.16': 'Suministro de DC-01 y del lote 1', '1.4.17': 'Tres tiendas piloto instaladas',
                '1.4.18': 'Suministro del lote 2 (19 tiendas y 2 CD)', '1.4.19': 'Instalación del lote 2',
                '1.4.20': 'Recuperación en Brazil South completa', '1.4.21': 'Plataforma de datos y analítica',
                '1.4.22': 'Equipamiento TI y redes de DC-01', '1.4.23': 'Pila local de tienda (25 sitios)',
                '1.4.24': 'Replicación entre regiones', '1.8.9': 'Controles de seguridad desplegados'})
prog = list(csv.DictReader(open(os.path.join(RV3, 'programacion_v3.csv'), encoding='utf-8-sig'), delimiter=';'))
elem = collections.defaultdict(lambda: dict(hh=0.0, tramos=collections.defaultdict(list), crit=[], margen=None, nombre=''))
for r in prog:
    if not r['edt'] or float(r['HH'] or 0) <= 0:
        continue
    e = tercer_nivel(r['edt'])
    x = elem[e]
    x['hh'] += float(r['HH'])
    x['nombre'] = nombres.get(e) or x['nombre'] or r['nombre'].split(' · ')[0]
    a, b = D(r['inicio']), D(r['fin_exclusivo'])
    x['tramos'][categoria(r)].append((a, b))
    ds = cals[r['calendario']]
    mg = bisect_left(ds, r['inicio_tardio']) - bisect_left(ds, r['inicio'])
    x['margen'] = mg if x['margen'] is None else min(x['margen'], mg)
    if mg <= 0:
        x['crit'].append((a, b))
for e in nombres:  # elementos sin actividades propias (cobertura o pool): se listan sin barra
    if e.count('.') == 2 and e not in elem:
        elem[e]['nombre'] = nombres[e]

def unir(iv, hueco=7):
    out = []
    for a, b in sorted(iv):
        if out and (a - out[-1][1]).days <= hueco:
            out[-1] = (out[-1][0], max(out[-1][1], b))
        else:
            out.append((a, b))
    return out

def lamina(rama, filas, parte, total):
    todos = [t for e in filas for c in elem[e]['tramos'].values() for t in c]
    if todos:
        mi, ma = num_mes(min(a for a, _ in todos)), num_mes(max(b for _, b in todos) - timedelta(days=1))
    else:
        mi, ma = 1, 21
    mi, ma = max(1, mi - 1), min(56, ma + 1)
    x0, x1 = mes_ini(mi), mes_ini(ma + 1)
    alto = 1.5 + 0.27 * len(filas)
    fig = plt.figure(figsize=(9.7, max(3.2, alto)))
    gs = fig.add_gridspec(1, 2, width_ratios=[4.3, 3.3], wspace=0.02)
    axt, ax = fig.add_subplot(gs[0]), fig.add_subplot(gs[1])
    for i, e in enumerate(filas):
        x = elem[e]
        for c, (_, color) in CAT.items():
            for a, b in unir(x['tramos'].get(c, [])):
                ax.barh(i, (b - a).days, left=a, height=0.56, color=color, edgecolor='white', linewidth=1, zorder=3)
        for a, b in unir(x['crit'], 3):
            ax.add_patch(Rectangle((matplotlib.dates.date2num(a), i - 0.33), (b - a).days, 0.66, fill=False,
                                   edgecolor=TEXTO, linewidth=1.3, zorder=4))
        if not x['tramos']:
            ax.text(x0 + timedelta(days=3), i, 'Sin actividades propias: se ejecuta dentro de la dirección o la operación',
                    va='center', fontsize=9, color=TEXTO2, style='italic')
        vent = [t for c in x['tramos'].values() for t in c]
        vtxt = (f"M{num_mes(min(a for a, _ in vent))}–M{num_mes(max(b for _, b in vent) - timedelta(days=1))}"
                if vent else '—')
        nombre = x['nombre'] if len(x['nombre']) <= 40 else x['nombre'][:39] + '…'
        axt.text(0.0, i, e, va='center', fontsize=9, color=TEXTO)
        axt.text(0.11, i, nombre, va='center', fontsize=9, color=TEXTO)
        axt.text(0.78, i, f"{x['hh']:,.0f}".replace(',', '.') if x['hh'] else '—', va='center', ha='right', fontsize=9, color=TEXTO2)
        axt.text(0.80, i, vtxt, va='center', fontsize=9, color=TEXTO2)
        mtx = '—' if x['margen'] is None else ('0' if x['margen'] <= 0 else str(x['margen']))
        axt.text(0.99, i, mtx, va='center', ha='right', fontsize=9, color=NARANJA if mtx == '0' else TEXTO2)
    for axx in (ax, axt):
        axx.set_ylim(len(filas) - 0.5, -1.3)
    for col, txt, ha in ((0.0, 'Código', 'left'), (0.11, 'Paquete o cuenta de control', 'left'), (0.78, 'HH', 'right'),
                         (0.80, 'Ventana', 'left'), (1.0, 'Margen', 'right')):
        axt.text(col, -1.0, txt, fontsize=9, fontweight='bold', ha=ha, color=TEXTO)
    axt.set_xlim(0, 1); axt.axis('off')
    ax.set_xlim(x0, x1)
    paso = 1 if ma - mi <= 8 else (2 if ma - mi <= 20 else (3 if ma - mi <= 36 else 6))
    ticks = list(range(mi, ma + 2, paso))
    ax.set_xticks([mes_ini(m) for m in ticks])
    ax.set_xticklabels([f'M{m}\n{MESES_ES[mes_ini(m).month - 1]} {mes_ini(m).year % 100:02d}' for m in ticks], fontsize=9)
    ax.set_yticks([]); ax.grid(axis='x', color=GRILLA, lw=0.8, zorder=1)
    for s in ('top', 'right', 'left'):
        ax.spines[s].set_visible(False)
    sufijo = f' (lámina {parte} de {total})' if total > 1 else ''
    fig.suptitle(f'Rama {rama} · {RAMAS[rama]}{sufijo}', x=0.01, ha='left', fontsize=10, fontweight='bold', color=TEXTO)
    ley = [Patch(color=c, label=n) for n, c in CAT.values()] + \
          [Patch(facecolor='white', edgecolor=TEXTO, linewidth=1.3, label='Actividades sin margen')]
    fig.legend(handles=ley, loc='upper left', ncol=5, frameon=False, fontsize=9,
               bbox_to_anchor=(0.005, 1 - 0.3 / fig.get_figheight()))
    fig.text(0.01, 0.012, 'Fuente: elaboración propia a partir de la red CPM v3. Margen: días hábiles hasta el inicio tardío (0 = sin margen).',
             fontsize=9, color=TEXTO2)
    fig.subplots_adjust(left=0.01, right=0.99, top=1 - 0.95 / fig.get_figheight(), bottom=0.75 / fig.get_figheight())
    nombre_arch = f"diag-07-04_gantt-rama-{rama.replace('.', '-')}" + (f'_{parte}' if total > 1 else '')
    salida = os.path.join(AQUI, nombre_arch)
    fig.savefig(salida + '.png', dpi=300); fig.savefig(salida + '.pdf'); plt.close(fig)
    return nombre_arch

ramas = sys.argv[1:] or sorted(RAMAS, key=clave)
for ra in ramas:
    filas = sorted([e for e in elem if e.startswith(ra + '.') and e.count('.') == 2], key=clave)
    partes = max(1, math.ceil(len(filas) / FILAS_POR_LAMINA))
    tam = math.ceil(len(filas) / partes)
    for p in range(partes):
        print(lamina(ra, filas[p * tam:(p + 1) * tam], p + 1, partes))
