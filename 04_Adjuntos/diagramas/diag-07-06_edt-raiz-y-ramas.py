"""Figuras SD-07 · EDT por rama (Figuras 7.2 a 7.16) en formato estándar: padre arriba y sus hijos en una fila.

- Nombres y códigos: diccionario del Formulario T-14 (fuente única; iguales a las láminas Gantt diag-07-04).
- Cada rama se divide en partes de hasta 5 hijos; cada parte repite el padre. Las partes se apilan en páginas.
- Tamaño real: ancho 17,6 cm (ancho útil de la página carta) y letra de 9 pt; LaTeX la inserta sin escalar.
- Cajas del mismo tamaño y formato en toda la rama, con el texto centrado.
- La rama 1.5 muestra sus 51 cuentas de control; la 1.10, sus 5 cuentas (los paquetes están en el T-14).
Uso: <python con matplotlib> diag-07-06_edt-raiz-y-ramas.py
Salida: diag-07-06_edt-1-N[_pK].(png|pdf) aquí y sd07-edt1.N[-K].png en latex_final/figuras/sd07-figuras/,
        más diag-07-06_paginas.json con el número de páginas por rama (lo usa el .tex).
"""
import os, re, json, shutil, collections
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
FIG = os.path.join(RAIZ, '02_Propuesta/latex_final/figuras/sd07-figuras')
T14 = os.path.join(RAIZ, '02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-14.tex')
NAVY, CAJA, BORDE, LINEA, ACENTO, TEXTO, GRIS = '#17324D', '#EEF3F8', '#B9C7D6', '#7A8794', '#196197', '#17324D', '#52514e'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'text.color': TEXTO})

PT = 9                       # letra mínima de las cajas (pt)
W = 6.93                     # 17,6 cm
POR_FILA = 5
GX = 0.12                    # separación entre cajas (pulgadas)
BW = (W - 0.04 - (POR_FILA - 1) * GX) / POR_FILA
PAD = 0.07
ALTO_PAGINA = 8.4            # alto máximo de una página de figura (pulgadas)
NUEVOS = set()  # todas las cajas iguales: el documento se lee como una sola versión

# ---------------- datos: diccionario del T-14 ----------------
s = open(T14, encoding='utf-8').read()
ramas = {m.group(1): m.group(2) for m in re.finditer(r'\\subsubsection\{Rama (1\.\d+) - ([^}]*)\}', s)}
hijos = collections.defaultdict(list)
for m in re.finditer(r'^(1\.(\d+)\.\d+) & ([^&]*) &', s, re.M):
    r = '1.' + m.group(2)
    if m.group(1) not in [c for c, _ in hijos[r]]:
        hijos[r].append((m.group(1), m.group(3).strip()))

# ---------------- medición y ajuste de texto ----------------
_fig = plt.figure(figsize=(W, 2)); _ax = _fig.add_axes([0, 0, 1, 1]); _r = _fig.canvas.get_renderer()
def ancho(t, **kw):
    tt = _ax.text(0, 0, t, **kw); w = tt.get_window_extent(renderer=_r).width / _fig.dpi; tt.remove(); return w
def lineas(texto, w, **kw):
    pal = []
    for x in texto.split():
        if ancho(x, **kw) > w and '/' in x:
            p = x.split('/'); pal += [y + '/' for y in p[:-1]] + [p[-1]]
        elif ancho(x, **kw) > w:
            # palabra más ancha que la caja: se divide con guion después de una vocal, en el corte más largo que cabe
            for i in range(len(x) - 2, 2, -1):
                if x[i - 1] in 'aeiouáéíóú' and x[i] not in 'aeiouáéíóú' and ancho(x[:i] + '-', **kw) <= w:
                    pal += [x[:i] + '-', x[i:]]; break
            else:
                pal.append(x)
        else:
            pal.append(x)
    out, act = [], ''
    for p in pal:
        prueba = (act + ('' if act.endswith(('/', '-')) and not act.endswith(' -') else ' ') + p).strip()
        if act and ancho(prueba, **kw) > w:
            out.append(act); act = p
        else:
            act = prueba
    out.append(act)
    assert all(ancho(l, **kw) <= w + 1e-6 for l in out), (texto, out)
    return out
LH = PT * 1.22 / 72          # alto de línea (pulgadas)

def caja(ax, x, y, w, h, fc=CAJA, ec=BORDE, lw=0.8):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=0.05', fc=fc, ec=ec, lw=lw, zorder=2))

def rama_paginas(cod, nombre, elems):
    kw = dict(fontsize=PT)
    textos = {c: lineas(n, BW - 2 * PAD, **kw) for c, n in elems}
    nl = max(len(v) for v in textos.values())
    BH = 2 * PAD + LH * (nl + 1) + 0.04                       # código + nombre, igual para toda la rama
    pkw = dict(fontsize=PT + 0.5, fontweight='bold')
    plineas = lineas(f'{cod} · {nombre}', 4.6 - 2 * PAD, **pkw)
    PH = 2 * PAD + LH * len(plineas) + 0.02
    partes = [elems[i:i + POR_FILA] for i in range(0, len(elems), POR_FILA)]
    n = len(partes)
    ETQ = 0.22 if n > 1 else 0.0
    ALTO_PARTE = ETQ + PH + 0.30 + BH + 0.18
    por_pagina = max(1, int(ALTO_PAGINA // ALTO_PARTE))
    npag = -(-n // por_pagina)
    por_pagina = -(-n // npag)  # reparto parejo entre páginas
    paginas = [partes[i:i + por_pagina] for i in range(0, n, por_pagina)]
    figs = []
    k = 0
    for pag in paginas:
        H = ALTO_PARTE * len(pag)
        fig = plt.figure(figsize=(W, H)); ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')
        y0 = H
        for parte in pag:
            k += 1
            if n > 1:
                ax.text(0.02, y0 - 0.02, f'Parte {k} de {n} ({parte[0][0]} a {parte[-1][0]})', ha='left', va='top',
                        fontsize=PT - 0.5, color=GRIS, style='italic')
            py = y0 - ETQ - PH
            pw = 4.6
            caja(ax, (W - pw) / 2, py, pw, PH, fc=NAVY, ec=NAVY)
            ax.text(W / 2, py + PH / 2, '\n'.join(plineas), ha='center', va='center', color='white',
                    linespacing=1.15, zorder=3, **pkw)
            m = len(parte)
            x0 = (W - (m * BW + (m - 1) * GX)) / 2
            cxs = [x0 + i * (BW + GX) + BW / 2 for i in range(m)]
            ybar = py - 0.15; ytop = py - 0.30
            ax.plot([W / 2, W / 2], [py, ybar], color=LINEA, lw=0.9, zorder=1)
            if m > 1:
                ax.plot([cxs[0], cxs[-1]], [ybar, ybar], color=LINEA, lw=0.9, zorder=1)
            for cx in cxs:
                ax.plot([cx, cx], [ybar, ytop], color=LINEA, lw=0.9, zorder=1)
            for i, (c, _) in enumerate(parte):
                x = x0 + i * (BW + GX); y = ytop - BH
                nuevo = c in NUEVOS
                caja(ax, x, y, BW, BH, ec=ACENTO if nuevo else BORDE, lw=1.3 if nuevo else 0.8)
                bloque = LH * (len(textos[c]) + 1)
                yc = y + BH / 2 + bloque / 2
                ax.text(x + BW / 2, yc, c, ha='center', va='top', fontsize=PT, fontweight='bold', color=ACENTO, zorder=3)
                ax.text(x + BW / 2, yc - LH, '\n'.join(textos[c]), ha='center', va='top', fontsize=PT,
                        linespacing=1.22, zorder=3)
            y0 -= ALTO_PARTE
        figs.append(fig)
    return figs

def guardar(fig, base, destino):
    fig.savefig(base + '.png', dpi=300)
    fig.savefig(base + '.pdf')
    plt.close(fig)
    shutil.copyfile(base + '.png', os.path.join(FIG, destino))

paginas = {}
for r in sorted(ramas, key=lambda x: int(x.split('.')[1])):
    figs = rama_paginas(r, ramas[r], hijos[r])
    paginas[r] = len(figs)
    for i, f in enumerate(figs, 1):
        suf = '' if i == 1 else f'_p{i}'
        guardar(f, os.path.join(AQUI, f"diag-07-06_edt-{r.replace('.', '-')}{suf}"), f"sd07-edt{r}{'' if i == 1 else f'-{i}'}.png")
    print(r, len(hijos[r]), 'hijos,', len(figs), 'página(s)')
json.dump(paginas, open(os.path.join(AQUI, 'diag-07-06_paginas.json'), 'w'), indent=0)
