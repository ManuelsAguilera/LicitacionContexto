"""
D6 · Migración de la cartera de crédito por tramos
Propuesta técnica Only Simple Solutions · Licitación TFEP-01/2026

Genera d6_migracion_cartera.png (300 dpi) y d6_migracion_cartera.pdf
a 16 cm de ancho, sin título (el título y la fuente van en el documento).

Uso:  python3 d6_migracion_cartera.py
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ------------------------------------------------------------------
# Parámetros editables
# ------------------------------------------------------------------
# Número de tramos de cada grupo: POR DEFINIR.
# Con None se dibuja la forma genérica "1, 2, …, N".
# Cuando el equipo lo fije, poner un entero (por ejemplo 3).
N_TRAMOS_E1 = None
N_TRAMOS_E2 = None

COMPRESION_1_12 = 0.33  # ancho relativo de cada mes 1–12 (meses 13–24 = 1)

# ------------------------------------------------------------------
# Paleta corporativa
# ------------------------------------------------------------------
AZUL_E1 = "#196197"     # Etapa 1
VERDE_E2 = "#7FC6AA"    # Etapa 2
AZUL_OSC = "#17324D"    # textos, líneas
GRIS = "#D9D9D9"        # sistema vigente (borde discontinuo)
BLANCO = "#FFFFFF"

CM = 1 / 2.54
FS = 9  # tamaño mínimo y único de texto (pt), a tamaño final

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "Liberation Sans", "DejaVu Sans"],
    "font.size": FS,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "hatch.linewidth": 0.6,
    "axes.linewidth": 0.6,
})


# ------------------------------------------------------------------
# Escala de tiempo (meses 1–12 comprimidos)
# ------------------------------------------------------------------
def X(m):
    """Posición del límite final del mes m (m=0 es el inicio del mes 1)."""
    if m <= 12:
        return m * COMPRESION_1_12
    return 12 * COMPRESION_1_12 + (m - 12)


def centro_mes(m):
    return (X(m - 1) + X(m)) / 2


X_MAX = X(24)

# ------------------------------------------------------------------
# Lienzo
# ------------------------------------------------------------------
FIG_W, FIG_H = 16.0, 13.8           # cm
AX_L, AX_R = 0.25, 15.75            # cm (márgenes horizontales)
AX_B, AX_H = 4.05, 8.2              # cm (eje principal)

fig = plt.figure(figsize=(FIG_W * CM, FIG_H * CM), facecolor=BLANCO)
ax = fig.add_axes([AX_L / FIG_W, AX_B / FIG_H,
                   (AX_R - AX_L) / FIG_W, AX_H / FIG_H])
ax.set_xlim(-0.05, X_MAX + 0.12)
ax.set_ylim(0, AX_H)                # unidades verticales = cm
ax.set_facecolor(BLANCO)
for s in ("left", "right", "bottom"):
    ax.spines[s].set_visible(False)
ax.spines["top"].set_color(AZUL_OSC)
ax.tick_params(axis="y", left=False, labelleft=False)

# ---- Eje de meses (arriba) ----
ticks = [1, 3, 6, 9, 12] + list(range(13, 25))
ax.xaxis.set_ticks_position("top")
ax.set_xticks([centro_mes(m) for m in ticks])
ax.set_xticklabels([str(m) for m in ticks], fontsize=FS, color=AZUL_OSC)
ax.tick_params(axis="x", length=2.5, width=0.6, color=AZUL_OSC, pad=2)

# Años sobre los números de mes
ax.text(X(12) / 2, AX_H + 0.62, "2027 · meses 1 a 12\n(escala comprimida)",
        ha="center", va="bottom", fontsize=FS, color=AZUL_OSC, linespacing=1.1)
ax.text((X(12) + X(24)) / 2, AX_H + 0.62, "2028 · meses 13 a 24",
        ha="center", va="bottom", fontsize=FS, color=AZUL_OSC)
ax.plot([X(12), X(12)], [AX_H + 0.55, AX_H + 1.35], color=AZUL_OSC, lw=0.6,
        clip_on=False)

# Marca de corte de escala en el eje (//)
for dx in (-0.06, 0.06):
    ax.plot([X(12) + dx - 0.05, X(12) + dx + 0.05], [AX_H - 0.12, AX_H + 0.12],
            color=AZUL_OSC, lw=0.8, clip_on=False)

# Rejilla de meses 13–24 y separación de la zona comprimida
for m in range(12, 25):
    ax.axvline(X(m), color=GRIS, lw=0.5, zorder=0)
ax.axvline(X(12), color=AZUL_OSC, lw=0.5, ls=(0, (2, 2)), zorder=0)

# Meses 22–24 en gris claro (fuera del período resaltado 1–21)
ax.add_patch(Rectangle((X(21), 0), X(24) - X(21), AX_H, facecolor=GRIS,
                       alpha=0.45, edgecolor="none", zorder=0))


# ------------------------------------------------------------------
# Ayudas de dibujo
# ------------------------------------------------------------------
def barra(m_ini, m_fin, y, h, color, texto="", color_txt=BLANCO,
          tramado=False, bold=False):
    """Barra que cubre los meses m_ini..m_fin (inclusive)."""
    x0, x1 = X(m_ini - 1), X(m_fin)
    hatch_color = BLANCO if color == AZUL_E1 else AZUL_OSC
    ax.add_patch(Rectangle((x0, y - h / 2), x1 - x0, h, facecolor=color,
                           edgecolor=color, lw=0.6,
                           hatch="////" if tramado else None,
                           hatchcolor=hatch_color, zorder=2))
    if texto:
        bbox = dict(facecolor=color, edgecolor="none", pad=0.8) if tramado else None
        ax.text((x0 + x1) / 2, y, texto, ha="center", va="center",
                fontsize=FS, color=color_txt, linespacing=1.0,
                fontweight="bold" if bold else "normal", bbox=bbox, zorder=3)


def tramos(m_ini, m_fin, y_base, n, color, color_txt):
    """Bloques escalonados crecientes con un rombo de compuerta antes de cada uno."""
    a, b = X(m_ini - 1), X(m_fin)
    if n is None:
        etiquetas = ["1", "2", "…", "N"]
    else:
        etiquetas = [str(i) for i in range(1, n + 1)]
    n_bloques = sum(1 for e in etiquetas if e != "…")
    alturas = [0.38 + i * (0.50 / max(n_bloques - 1, 1)) for i in range(n_bloques)]

    paso = (b - a) / len(etiquetas)
    i_bloque = 0
    for k, et in enumerate(etiquetas):
        s0 = a + k * paso
        if et == "…":
            ax.text(s0 + paso / 2, y_base + 0.22, "…", ha="center",
                    va="center", fontsize=FS, color=AZUL_OSC, zorder=4)
            continue
        # Compuerta (rombo) antes del tramo
        ax.scatter([s0 + 0.15 * paso], [y_base + 0.16], marker="D", s=20,
                   facecolor=BLANCO, edgecolor=AZUL_OSC, linewidth=0.9,
                   zorder=5, clip_on=False)
        # Bloque del tramo (tamaño ilustrativo, sin escala)
        h = alturas[i_bloque]
        x0, w = s0 + 0.42 * paso, 0.52 * paso
        ax.add_patch(Rectangle((x0, y_base), w, h, facecolor=color,
                               edgecolor=AZUL_OSC, lw=0.6, zorder=4))
        ax.text(x0 + w / 2, y_base + h / 2, et, ha="center", va="center",
                fontsize=FS, color=color_txt, fontweight="bold", zorder=5)
        i_bloque += 1

    # Corchete y rótulo de los tramos
    y_c = y_base + max(alturas) + 0.14
    ax.plot([a, a, b, b], [y_c - 0.07, y_c, y_c, y_c - 0.07],
            color=AZUL_OSC, lw=0.6, zorder=3)
    rotulo = ("Tramos 1 a N (N por definir)" if n is None
              else f"Tramos 1 a {n}")
    ax.text(a, y_c + 0.06, rotulo, ha="left", va="bottom", fontsize=FS,
            color=AZUL_OSC, zorder=3,
            bbox=dict(facecolor=BLANCO, edgecolor="none", pad=0.5))
    return a


def descripcion(y_top, titulo, texto):
    ax.text(0.02, y_top, titulo, ha="left", va="top", fontsize=FS,
            fontweight="bold", color=AZUL_OSC)
    ax.text(0.02, y_top - 0.38, texto, ha="left", va="top", fontsize=FS,
            color=AZUL_OSC, linespacing=1.15)


def hito(x, y0, y1):
    ax.plot([x, x], [y0, y1], color=AZUL_OSC, lw=2.2,
            solid_capstyle="butt", zorder=6, clip_on=False)


# ------------------------------------------------------------------
# Fila superior: contexto de etapas
# ------------------------------------------------------------------
Y_E1, Y_E2, H_ETAPA = 7.65, 6.85, 0.66

barra(1, 12, Y_E1, H_ETAPA, AZUL_E1, "Etapa 1 · Desarrollo", bold=True)
barra(13, 15, Y_E1, H_ETAPA, AZUL_E1, "Marcha\nblanca", tramado=True)
barra(16, 16, Y_E1, H_ETAPA, AZUL_E1)
ax.text(X(16) + 0.12, Y_E1, "Paso a producción (mes 16)", ha="left",
        va="center", fontsize=FS, color=AZUL_OSC)

barra(13, 18, Y_E2, H_ETAPA, VERDE_E2, "Etapa 2 · Desarrollo",
      color_txt=AZUL_OSC, bold=True)
barra(19, 20, Y_E2, H_ETAPA, VERDE_E2, "Marcha\nblanca", color_txt=AZUL_OSC,
      tramado=True)
barra(21, 21, Y_E2, H_ETAPA, VERDE_E2)
ax.text(X(21) + 0.12, Y_E2, "Paso a producción\n(mes 21)", ha="left",
        va="center", fontsize=FS, color=AZUL_OSC, linespacing=1.05)

ax.plot([-0.05, X_MAX + 0.12], [6.32, 6.32], color=AZUL_OSC, lw=0.6)

# ------------------------------------------------------------------
# Filas centrales: olas de migración de los 620.000 clientes con saldo
# ------------------------------------------------------------------
Y_G1_TOP, Y_G1_BASE = 6.12, 4.62
Y_G2_TOP, Y_G2_BASE = 4.30, 2.82

descripcion(Y_G1_TOP, "Grupo Etapa 1",
            "Clientes con saldo al\ndía, sin repactación ni\ncobranza en curso")
x_primer_tramo = tramos(13, 15, Y_G1_BASE, N_TRAMOS_E1, AZUL_E1, BLANCO)

ax.plot([-0.05, X_MAX + 0.12], [4.45, 4.45], color=GRIS, lw=0.6)

descripcion(Y_G2_TOP, "Grupo Etapa 2",
            "Clientes con\nrepactaciones, cobranzas\no juicios en curso")
tramos(19, 20, Y_G2_BASE, N_TRAMOS_E2, VERDE_E2, AZUL_OSC)

ax.plot([-0.05, X_MAX + 0.12], [2.62, 2.62], color=AZUL_OSC, lw=0.6)

# ------------------------------------------------------------------
# Fila inferior: conciliación, convivencia y límite
# ------------------------------------------------------------------
Y_CONC, Y_2011, H_BANDA = 2.15, 1.45, 0.48

# Conciliación diaria de saldos: desde el primer tramo hasta el mes 21
ax.add_patch(Rectangle((x_primer_tramo, Y_CONC - H_BANDA / 2),
                       X(21) - x_primer_tramo, H_BANDA, facecolor=BLANCO,
                       edgecolor=AZUL_OSC, lw=1.1, zorder=2))
ax.text(x_primer_tramo + 0.12, Y_CONC, "Conciliación diaria de saldos",
        ha="left", va="center", fontsize=FS, color=AZUL_OSC, zorder=3)

# Plataforma de crédito de 2011 en convivencia: hasta el mes 22
ax.add_patch(Rectangle((0, Y_2011 - H_BANDA / 2), X(22), H_BANDA,
                       facecolor=GRIS, edgecolor=AZUL_OSC, lw=0.9,
                       ls=(0, (3, 2)), zorder=2))
ax.text(0.10, Y_2011, "Plataforma de crédito de 2011 en convivencia",
        ha="left", va="center", fontsize=FS, color=AZUL_OSC, zorder=3)
ax.text(X(22) - 0.12, Y_2011, "Retiro (octubre 2028)", ha="right",
        va="center", fontsize=FS, color=AZUL_OSC, fontweight="bold", zorder=3)
hito(X(22), Y_2011 - H_BANDA / 2 - 0.12, Y_2011 + H_BANDA / 2 + 0.12)

# Límite: cartera migrada antes de 2029 (fin del mes 24)
hito(X(24), 0.42, 6.32)
ax.text(X(24) - 0.12, 0.62, "Límite: cartera migrada antes de 2029",
        ha="right", va="center", fontsize=FS, color=AZUL_OSC,
        fontweight="bold")

# ------------------------------------------------------------------
# Leyenda y notas (abajo)
# ------------------------------------------------------------------
lg = fig.add_axes([0, 0, 1, AX_B / FIG_H])
lg.set_xlim(0, FIG_W)
lg.set_ylim(0, AX_B)
lg.axis("off")

SW_W, SW_H = 0.55, 0.30
ROW = 0.42


def sw_rect(x, y, **kw):
    lg.add_patch(Rectangle((x, y - SW_H / 2), SW_W, SW_H, **kw))


def sw_txt(x, y, t):
    lg.text(x + SW_W + 0.15, y, t, ha="left", va="center", fontsize=FS,
            color=AZUL_OSC)


x1, x2 = 0.30, 4.65
y0 = AX_B - 0.45
# Columna 1
sw_rect(x1, y0, facecolor=AZUL_E1, edgecolor=AZUL_E1)
sw_txt(x1, y0, "Etapa 1")
sw_rect(x1, y0 - ROW, facecolor=VERDE_E2, edgecolor=VERDE_E2)
sw_txt(x1, y0 - ROW, "Etapa 2")
sw_rect(x1, y0 - 2 * ROW, facecolor=BLANCO, edgecolor=AZUL_OSC, lw=0.6,
        hatch="////", hatchcolor=AZUL_OSC)
sw_txt(x1, y0 - 2 * ROW, "Marcha blanca (tramado)")
lg.scatter([x1 + SW_W / 2], [y0 - 3 * ROW], marker="D", s=20,
           facecolor=BLANCO, edgecolor=AZUL_OSC, linewidth=0.9)
sw_txt(x1, y0 - 3 * ROW, "Compuerta (ver nota)")
# Columna 2
for i, h in enumerate((0.14, 0.22, 0.30)):
    lg.add_patch(Rectangle((x2 + i * 0.19, y0 - SW_H / 2), 0.15, h,
                           facecolor=BLANCO, edgecolor=AZUL_OSC, lw=0.6))
sw_txt(x2, y0, "Tramo (sin escala)")
sw_rect(x2, y0 - ROW, facecolor=GRIS, edgecolor=AZUL_OSC, lw=0.9,
        ls=(0, (3, 2)))
sw_txt(x2, y0 - ROW, "Sistema vigente en convivencia")
lg.plot([x2 + SW_W / 2] * 2, [y0 - 2 * ROW - 0.17, y0 - 2 * ROW + 0.17],
        color=AZUL_OSC, lw=2.2, solid_capstyle="butt")
sw_txt(x2, y0 - 2 * ROW, "Hito")
sw_rect(x2, y0 - 3 * ROW, facecolor=GRIS, alpha=0.45, edgecolor="none")
sw_txt(x2, y0 - 3 * ROW, "Meses 22 a 24")

# Nota de compuerta (recuadro a la derecha)
nx, nw = 10.0, 5.75
ny_top, nh = AX_B - 0.22, 3.25
lg.add_patch(Rectangle((nx, ny_top - nh), nw, nh, facecolor=BLANCO,
                       edgecolor=AZUL_OSC, lw=0.7))
lg.text(nx + 0.15, ny_top - 0.12, "Compuerta antes de cada tramo", ha="left",
        va="top", fontsize=FS, color=AZUL_OSC, fontweight="bold")
lg.text(nx + 0.15, ny_top - 0.55,
        "· convivencia real\n"
        "· conciliación diaria sin diferencias\n"
        "  sin explicar\n"
        "· retorno probado\n"
        "· plan de comunicación a los clientes\n"
        "La cierran la Contraparte Técnica\n"
        "y la filial emisora.",
        ha="left", va="top", fontsize=FS, color=AZUL_OSC, linespacing=1.15)

# Texto sobre la espera de un tramo
lg.text(0.30, 0.30,
        "Si una compuerta no se cumple, el tramo espera; el margen\n"
        "entre el retiro (mes 22) y el fin de soporte (2029) absorbe\n"
        "la espera sin mover hitos.",
        ha="left", va="bottom", fontsize=FS, color=AZUL_OSC,
        style="italic", linespacing=1.15)

fig.savefig("d6_migracion_cartera.png", dpi=300, facecolor=BLANCO)
fig.savefig("d6_migracion_cartera.pdf", facecolor=BLANCO)
print("Listo: d6_migracion_cartera.png y d6_migracion_cartera.pdf")
