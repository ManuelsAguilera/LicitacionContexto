#!/usr/bin/env python3
# Matriz de cobertura de las causas raíz - Multitiendas Ancoa S.A. - Only Simple Solutions
# Uso:  python3 matriz_causas.py   ->  matriz_causas.png (300 dpi) y matriz_causas.pdf
import textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ---------------- Interruptores (por confirmar con el equipo) ----------------
CONFIRMADO_C2_MARKETPLACE = False
CONFIRMADO_C3_CARTERA = False

# ---------------- Datos ----------------
AZUL_OSCURO = "#17324D"
AZUL_CLARO = "#277FA8"
GRIS_AZULADO = "#DCE3EA"   # gris azulado claro (tinte de #17324D); sin hex indicado: por confirmar
FUENTE = 9                 # pt, tamaño final

filas = [
    "Causa C1 · Registro impreciso",
    "Causa C2 · Tejido de integración",
    "Causa C3 · Frontera difusa entre los negocios",
    "Causa C4 · Incentivos y capacidad operativa",
    "Causa C5 · Territorio y calendario",
]

# (frente, área o None, [columnas])
grupos = [
    ("Retail", "Mercadería", ["Oferta comercial", "Abastecimiento", "Existencias"]),
    ("Retail", "Venta", ["Pedidos", "Ventas", "Comisiones", "Marketplace"]),
    ("Retail", "Relación con el cliente", ["Posventa", "Clientes Retail"]),
    ("Filial emisora", "Crédito", ["Originación de crédito", "Cartera de crédito", "Evidencia financiera"]),
    ("Frontera", None, ["Control de cruces"]),
    ("Soporte", None, ["Base tecnológica", "Componentes locales de las tiendas"]),
]
columnas = [c for _, _, cols in grupos for c in cols]
assert len(columnas) == 15 and len(filas) == 5

marcas = {
    0: ["Oferta comercial", "Abastecimiento", "Existencias", "Posventa"],
    1: ["Oferta comercial", "Pedidos", "Base tecnológica"],
    2: ["Control de cruces", "Evidencia financiera", "Clientes Retail"],
    3: ["Comisiones", "Originación de crédito", "Evidencia financiera", "Base tecnológica"],
    4: ["Ventas", "Componentes locales de las tiendas"],
}
if CONFIRMADO_C2_MARKETPLACE:
    marcas[1].append("Marketplace")
if CONFIRMADO_C3_CARTERA:
    marcas[2].append("Cartera de crédito")
for lista in marcas.values():
    assert all(c in columnas for c in lista)

# ---------------- Geometría (pulgadas) ----------------
W = 6.3                      # 16 cm
w_lab, w_tot = 1.50, 0.50
w_col = (W - w_lab - w_tot) / 15
h_A, h_B, h_head, h_row, h_tot = 0.42, 0.50, 2.20, 0.50, 0.30
H = h_A + h_B + h_head + 5 * h_row + h_tot

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "Liberation Sans", "DejaVu Sans"],
    "font.size": FUENTE,
    "pdf.fonttype": 42,
})
fig = plt.figure(figsize=(W, H), facecolor="white")
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(H, 0)           # y crece hacia abajo
ax.axis("off")

def caja(x, y, w, h, fc="white", ec=AZUL_OSCURO, lw=0.6, z=1):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, linewidth=lw, zorder=z))

def texto(x, y, s, rot=0, ha="center", va="center", bold=False):
    ax.text(x, y, s, rotation=rot, ha=ha, va=va, color=AZUL_OSCURO, fontsize=FUENTE,
            fontweight="bold" if bold else "normal", zorder=5, linespacing=1.15)

x0 = w_lab
y_A, y_B = 0.0, h_A
y_head = h_A + h_B
y_body = y_head + h_head

# Encabezados de grupo (dos niveles)
x = x0
frentes = {}
for frente, area, cols in grupos:
    w = w_col * len(cols)
    relleno = GRIS_AZULADO if frente in ("Retail", "Filial emisora") else "white"
    if area is not None:
        caja(x, y_B, w, h_B, fc=relleno)
        texto(x + w / 2, y_B + h_B / 2, "\n".join(textwrap.wrap(area, 10)), bold=True)
    frentes.setdefault(frente, [x, 0.0])
    frentes[frente][1] += w
    x += w

for frente, (fx, fw) in frentes.items():
    if frente in ("Retail", "Filial emisora"):
        caja(fx, y_A, fw, h_A, fc=GRIS_AZULADO)
        texto(fx + fw / 2, y_A + h_A / 2, frente.replace("Filial emisora", "Filial\nemisora"), bold=True)
    elif frente == "Frontera":
        caja(fx, y_A, fw, h_A + h_B, fc="white", ec=AZUL_CLARO, lw=2.6, z=3)
        texto(fx + fw / 2, y_A + (h_A + h_B) / 2, frente, rot=90, bold=True)
    else:  # Soporte
        caja(fx, y_A, fw, h_A + h_B, fc="white")
        texto(fx + fw / 2, y_A + (h_A + h_B) / 2, frente, bold=True)

# Encabezados de columna (rotados 90°) + celdas
for j, nombre in enumerate(columnas):
    cx = x0 + j * w_col
    caja(cx, y_head, w_col, h_head)
    texto(cx + w_col / 2, y_head + h_head - 0.06, nombre, rot=90, va="bottom")
    for i in range(5):
        caja(cx, y_body + i * h_row, w_col, h_row)
        if nombre in marcas[i]:
            texto(cx + w_col / 2, y_body + i * h_row + h_row / 2, "●")
    total_col = sum(nombre in marcas[i] for i in range(5))
    caja(cx, y_body + 5 * h_row, w_col, h_tot)
    texto(cx + w_col / 2, y_body + 5 * h_row + h_tot / 2, str(total_col), bold=True)

# Columna de rótulos de fila y columna "Total"
caja(0, y_head, w_lab, h_head)
for i, nombre in enumerate(filas):
    caja(0, y_body + i * h_row, w_lab, h_row)
    texto(0.06, y_body + i * h_row + h_row / 2, "\n".join(textwrap.wrap(nombre, 25)), ha="left")
caja(0, y_body + 5 * h_row, w_lab, h_tot)
texto(0.06, y_body + 5 * h_row + h_tot / 2, "Total", ha="left", bold=True)

xt = x0 + 15 * w_col
caja(xt, y_head, w_tot, h_head)
texto(xt + w_tot / 2, y_head + h_head - 0.06, "Total", rot=90, va="bottom", bold=True)
for i in range(5):
    caja(xt, y_body + i * h_row, w_tot, h_row)
    texto(xt + w_tot / 2, y_body + i * h_row + h_row / 2, str(len(marcas[i])), bold=True)
caja(xt, y_body + 5 * h_row, w_tot, h_tot)
texto(xt + w_tot / 2, y_body + 5 * h_row + h_tot / 2,
      str(sum(len(v) for v in marcas.values())), bold=True)

fig.savefig("matriz_causas.png", dpi=300, facecolor="white")
fig.savefig("matriz_causas.pdf", facecolor="white")
