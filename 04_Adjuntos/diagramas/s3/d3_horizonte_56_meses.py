"""
D3 · Horizonte de 56 meses (Gantt)
Propuesta técnica Only Simple Solutions · Licitación TFEP-01/2026 · Caso 09 Multitiendas Ancoa S.A.

Uso:
    python3 d3_horizonte_56_meses.py
Genera, junto al script:
    d3_horizonte_56_meses.png  (300 dpi, 16 x 8 cm)
    d3_horizonte_56_meses.pdf  (vectorial, 16 x 8 cm, fuentes incrustadas)

NOTA AL PIE (no va en la imagen):
    Supuesto SUP-26: el proyecto comienza en enero de 2027 (mes 1 = enero de 2027,
    mes 56 = agosto de 2031). Si cambia el inicio, basta modificar INICIO_ANIO /
    INICIO_MES: los meses calendario, las ventanas de congelamiento y la
    verificación de los hitos 16 y 21 se recalculan solos.

Aproximaciones de calendario (ajustar si el Caso, núm. 13.2, da días exactos):
    "última semana de enero"  = 25 al 31 de enero
    "primera semana de marzo" = 1 al 7 de marzo
    "segunda semana de mayo"  = 8 al 14 de mayo
    Evento anual de comercio electrónico + semana previa: fecha variable; se
    dibuja como banda más clara entre el 1 de mayo y el 30 de junio.
"""
import calendar

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import transforms as mtransforms
from matplotlib.patches import Rectangle

# ---------------------------------------------------------------- paleta
AZUL = "#196197"        # Etapa 1
VERDE = "#7FC6AA"       # Etapa 2
AZUL_OSC = "#17324D"    # operación, textos y líneas
AMBAR = "#F2B134"       # ventanas de congelamiento
BLANCO = "#FFFFFF"

# ---------------------------------------------------------------- tipografía
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "Liberation Sans", "DejaVu Sans"],
    "font.size": 9,               # mínimo 9 pt al tamaño final (16 x 8 cm)
    "text.color": AZUL_OSC,
    "axes.edgecolor": AZUL_OSC,
    "xtick.color": AZUL_OSC,
    "xtick.labelcolor": AZUL_OSC,
    "hatch.linewidth": 0.7,
    "pdf.fonttype": 42,           # TrueType incrustada en el PDF
    "savefig.facecolor": BLANCO,
})
FS = 9

# ---------------------------------------------------------------- calendario
INICIO_ANIO, INICIO_MES = 2027, 1     # SUP-26
N_MESES = 56
X_MIN, X_MAX = 0.5, N_MESES + 0.5     # el mes m ocupa [m - 0.5, m + 0.5]
MESES_ABR = ["ene", "feb", "mar", "abr", "may", "jun",
             "jul", "ago", "sep", "oct", "nov", "dic"]


def mes_proyecto(anio, mes):
    return (anio - INICIO_ANIO) * 12 + (mes - INICIO_MES) + 1


def mes_calendario(m):
    """Mes del proyecto -> (año, mes calendario)."""
    total = (INICIO_MES - 1) + (m - 1)
    return INICIO_ANIO + total // 12, total % 12 + 1


def x_fecha(anio, mes, dia, fin=False):
    """Posición continua de un día; fin=True devuelve el final de ese día."""
    m = mes_proyecto(anio, mes)
    nd = calendar.monthrange(anio, mes)[1]
    return m - 0.5 + (dia if fin else dia - 1) / nd


def ventanas_congelamiento():
    """Ventanas de cada año dentro del horizonte, recortadas a los 56 meses."""
    anio_fin = mes_calendario(N_MESES)[0]
    v = []
    for a in range(INICIO_ANIO - 1, anio_fin + 1):
        v += [
            ("Navidad y liquidación", x_fecha(a, 11, 1), x_fecha(a + 1, 1, 6, True), "fija"),
            ("Vuelta a clases", x_fecha(a, 1, 25), x_fecha(a, 3, 7, True), "fija"),
            ("Día de la Madre", x_fecha(a, 5, 8), x_fecha(a, 5, 14, True), "fija"),
            ("Evento anual + semana previa", x_fecha(a, 5, 1), x_fecha(a, 6, 30, True), "variable"),
        ]
    return [(n, max(x0, X_MIN), min(x1, X_MAX), t)
            for n, x0, x1, t in v if x1 > X_MIN and x0 < X_MAX]


def choques(mes, ventanas):
    a, b = mes - 0.5, mes + 0.5
    return [f"{n} ({x0:.2f}-{x1:.2f})" for n, x0, x1, _ in ventanas if x0 < b and x1 > a]


VENTANAS = ventanas_congelamiento()

# Verificación obligatoria: los pasos a producción (meses 16 y 21) fuera de toda banda.
for mes_pp in (16, 21):
    c = choques(mes_pp, VENTANAS)
    a, mc = mes_calendario(mes_pp)
    print(f"Mes {mes_pp} ({MESES_ABR[mc - 1]} {a}): "
          + ("FUERA de toda ventana de congelamiento" if not c else f"CHOCA con {c}"))
    assert not c, f"El hito del mes {mes_pp} cae dentro de una ventana de congelamiento"
# Control informativo de los demás hitos (no bloquea la generación).
for mes_h in (6, 7, 22, 24):
    c = choques(mes_h, VENTANAS)
    a, mc = mes_calendario(mes_h)
    print(f"  (info) mes {mes_h} ({MESES_ABR[mc - 1]} {a}): {c if c else 'sin choque'}")

# ---------------------------------------------------------------- figura
CM = 1 / 2.54
fig = plt.figure(figsize=(16 * CM, 8 * CM))
L, R, B, T = 3.95 * CM / (16 * CM), 0.15 / 16, 41 / 226.8, 3 / 226.8
ax = fig.add_axes([L, B, 1 - L - R, 1 - B - T])
Y_MIN, Y_MAX = -0.3, 14.4
ax.set_xlim(X_MIN, X_MAX)
ax.set_ylim(Y_MIN, Y_MAX)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_linewidth(0.8)
ax.set_yticks([])

Y_BANDAS_TOP = 6.6   # las bandas cubren la zona de barras, no la de rótulos

# ---- bandas ámbar (fondo)
for nombre, x0, x1, tipo in VENTANAS:
    if tipo == "variable":
        cara, trama = (0.949, 0.694, 0.204, 0.13), ".."
    else:
        cara, trama = (0.949, 0.694, 0.204, 0.30), "\\\\\\"
    ax.add_patch(Rectangle((x0, Y_MIN), x1 - x0, Y_BANDAS_TOP - Y_MIN,
                           facecolor=cara, edgecolor="none", linewidth=0,
                           hatch=trama, hatchcolor=(0.949, 0.694, 0.204, 0.85),
                           zorder=0))

# ---- inicio de cada año
for m in range(1, N_MESES + 1):
    a, mc = mes_calendario(m)
    if mc == 1 and m > 1:
        x = m - 0.5
        ax.plot([x, x], [Y_MIN, Y_BANDAS_TOP], color=AZUL_OSC, lw=0.6,
                alpha=0.45, zorder=1)
        # bajo el eje: marca de inicio de año en las filas de mes calendario y año
        # (no cruza los números de mes)
        sep = mtransforms.offset_copy(ax.get_xaxis_transform(), fig=fig,
                                      y=-15.5, units="points")
        ax.plot([x, x], [0, -0.13], transform=sep, color=AZUL_OSC, lw=0.6,
                clip_on=False)

# ---- barras
H = 0.7
FILAS = [
    # rótulo, mes inicio, mes fin, color, tramado, color de la trama, y
    ("Etapa 1 · desarrollo", 1, 12, AZUL, None, None, 6.0),
    ("Etapa 1 · marcha blanca", 13, 15, AZUL, "////", BLANCO, 5.0),
    ("Etapa 2 · desarrollo", 13, 18, VERDE, None, None, 4.0),
    ("Etapa 2 · marcha blanca", 19, 20, VERDE, "////", AZUL_OSC, 3.0),
    ("Operación (36 meses)", 21, 56, AZUL_OSC, None, None, 2.0),
]
for rotulo, m0, m1, color, trama, c_trama, y in FILAS:
    ax.add_patch(Rectangle((m0 - 0.5, y - H / 2), m1 - m0 + 1, H,
                           facecolor=color, edgecolor=color, linewidth=0.6,
                           hatch=trama, hatchcolor=c_trama or color, zorder=3))
    ax.text(0.15, y, rotulo, ha="right", va="center", fontsize=FS)

# ---- retiro del sistema central de 2009 (sin fecha: dentro de la Operación)
Y09 = 0.65
ax.text(0.15, Y09, "Retiro del sistema central\nde 2009", ha="right",
        va="center", multialignment="right", fontsize=FS, linespacing=1.05)
ax.annotate("", xy=(56.45, Y09), xytext=(20.55, Y09),
            arrowprops=dict(arrowstyle="<|-|>", color=AZUL_OSC, lw=0.9,
                            mutation_scale=7, shrinkA=0, shrinkB=0), zorder=3)
ax.text(38.5, Y09, "fecha en el capítulo 7", ha="center", va="center",
        fontsize=FS, style="italic", zorder=4,
        bbox=dict(boxstyle="square,pad=0.15", facecolor=BLANCO, edgecolor="none"))

# ---- corchete sobre 2029 (sin mes exacto)
x29a, x29b = mes_proyecto(2029, 1) - 0.5, mes_proyecto(2029, 12) + 0.5
yc0, yc1 = 2.5, 2.78
ax.plot([x29a, x29a, x29b, x29b], [yc0, yc1, yc1, yc0], color=AZUL_OSC,
        lw=0.9, zorder=4, solid_joinstyle="miter")
ax.plot([(x29a + x29b) / 2] * 2, [yc1, yc1 + 0.18], color=AZUL_OSC, lw=0.9, zorder=4)
ax.text(x29a + 0.1, yc1 + 0.32,
        "Fin de soporte de la plataforma de 2011\n"
        "y último hito del plan de remediación\n(2029)",
        ha="left", va="bottom", fontsize=FS, linespacing=1.05, zorder=4,
        bbox=dict(boxstyle="square,pad=0.12", facecolor=(1, 1, 1, 1.0),
                  edgecolor="none"))

# ---- hitos (rombos); escalonados para que ningún rótulo cruce una guía
HITOS = [
    # x, y, rótulo (a la izquierda del rombo), tramo (mes inicial, mes final) o None
    (24, 13.75, "Límite de la migración de la cartera (diciembre 2028)", None),
    (22, 12.45, "Retiro de la plataforma de crédito de 2011\n(octubre 2028)", None),
    (21, 11.15, "Paso a producción Etapa 2 (septiembre 2028)", None),
    (16, 10.15, "Paso a producción Etapa 1 (abril 2028)", None),
    (6.5, 8.75, "Prueba de corte de enlace\nde 24 h (junio–julio 2027)", (6, 7)),
]
for x, y, rotulo, tramo in HITOS:
    ax.plot([x, x], [Y_MIN, y - 0.3], color=AZUL_OSC, lw=0.6, ls=(0, (1, 1.5)),
            zorder=2)
    if tramo:
        ax.plot([tramo[0] - 0.5, tramo[1] + 0.5], [y, y], color=AZUL_OSC,
                lw=1.0, marker="|", markevery=[0, 1], ms=6, zorder=4)
        x_txt = tramo[0] - 0.5 - 0.35
    else:
        x_txt = x - 0.75
    ax.plot(x, y, marker="D", ms=5.2, color=AZUL_OSC, mec=BLANCO, mew=0.6,
            zorder=5)
    ax.text(x_txt, y, rotulo, ha="right", va="center", multialignment="right",
            fontsize=FS, linespacing=1.05, zorder=5)

# ---- leyenda compacta (arriba a la derecha)
LX = 29.5                 # inicio de la leyenda, en meses
HW, HH = 1.7, 0.62        # tamaño de cada muestra (meses x filas)


def muestra(x, y, cara, trama=None, c_trama=None, borde=None):
    ax.add_patch(Rectangle((x, y - HH / 2), HW, HH, facecolor=cara,
                           edgecolor=borde or cara, linewidth=0.6, hatch=trama,
                           hatchcolor=c_trama or cara, zorder=5, clip_on=False))
    return x + HW + 0.5


def rotulo(x, y, txt):
    ax.text(x, y, txt, ha="left", va="center", fontsize=FS, zorder=5)


y = 13.8
rotulo(muestra(LX, y, AZUL), y, "Etapa 1")
rotulo(muestra(LX + 8.0, y, VERDE), y, "Etapa 2")
rotulo(muestra(LX + 16.0, y, AZUL_OSC), y, "Operación")
y = 12.7
rotulo(muestra(LX, y, BLANCO, "////", AZUL_OSC, AZUL_OSC), y, "Marcha blanca (tramado)")
ax.plot(LX + 19.6 + HW / 2, y, marker="D", ms=5.2, color=AZUL_OSC, mec=BLANCO,
        mew=0.6, zorder=5)
rotulo(LX + 19.6 + HW + 0.5, y, "Hito")
y = 11.6
rotulo(muestra(LX, y, (0.949, 0.694, 0.204, 0.30), "\\\\\\",
               (0.949, 0.694, 0.204, 0.85), AMBAR), y, "Ventana de congelamiento")
y = 10.35
ax.text(muestra(LX, y + 0.5, (0.949, 0.694, 0.204, 0.13), "..",
                (0.949, 0.694, 0.204, 0.85), AMBAR), y,
        "Evento anual y semana previa\n(fecha variable)", ha="left", va="center",
        fontsize=FS, linespacing=1.05, zorder=5)

# ---- eje X: fila 1 = mes del proyecto, fila 2 = mes calendario, fila 3 = año
MAYORES = [1, 6, 12, 16, 21, 24, 30, 36, 42, 48, 56]
ax.set_xticks(MAYORES)
ax.set_xticks(range(1, N_MESES + 1), minor=True)
ax.tick_params(axis="x", which="major", length=3.5, width=0.8, pad=1.5,
               labelsize=FS)
ax.tick_params(axis="x", which="minor", length=1.8, width=0.5)
XA = ax.get_xaxis_transform()


def bajo_eje(x, dy, txt, **kw):
    ax.annotate(txt, xy=(x, 0), xycoords=XA, xytext=(0, -dy),
                textcoords="offset points", ha=kw.pop("ha", "center"),
                va="top", fontsize=FS, annotation_clip=False, **kw)


bajo_eje(0.15, 5.0, "Mes del proyecto", ha="right")
for m in range(1, N_MESES + 1):
    a, mc = mes_calendario(m)
    if mc in (1, 7):   # rótulo alineado al inicio del mes, a la derecha de la marca de año
        bajo_eje(m - 0.5 + 0.35, 16.5, MESES_ABR[mc - 1], ha="left")
anios = {}
for m in range(1, N_MESES + 1):
    anios.setdefault(mes_calendario(m)[0], []).append(m)
for a, ms in anios.items():
    bajo_eje((ms[0] + ms[-1]) / 2, 27.5, str(a), fontweight="bold")

# ---------------------------------------------------------------- exportar
for ext in ("png", "pdf"):
    fig.savefig(f"d3_horizonte_56_meses.{ext}", dpi=300)
print("Listo: d3_horizonte_56_meses.png y d3_horizonte_56_meses.pdf")
