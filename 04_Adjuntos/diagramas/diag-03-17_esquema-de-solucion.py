"""Esquema de la solución: del problema de Ancoa a lo que se entrega y al resultado que se mide.

Responde: ¿qué problema resuelve la propuesta, con qué piezas, en qué orden y cómo se sabrá que funcionó?
Un solo nivel (conceptual), de izquierda a derecha: problema, causa, solución, entrega y resultado. Sin marcas ni
productos; nombres de negocio. Cifras de SD-02 (Tabla 2.3) y reparto por etapa de SD-03 (Tabla 3.1 y 3.2.2).
Ejecutar: python3 04_Adjuntos/diagramas/diag-03-17_esquema-de-solucion.py
"""

from pathlib import Path

from _alcance import box, container, header, legend, pic
from _drawio import ACCENT, Diagram

d = Diagram(font=24, zone_font=27)
W = 3
YH, Y0 = 95, 190
C = {"pro": (20, 520), "cau": (590, 400), "sol": (1040, 640), "ent": (1730, 440), "res": (2220, 520)}

header(d, C["pro"][0], YH, C["pro"][1], "", "El problema", "users")
header(d, C["cau"][0], YH, C["cau"][1], "", "La causa", "exchange")
header(d, C["sol"][0], YH, C["sol"][1], "", "La solución", "services")
header(d, C["ent"][0], YH, C["ent"][1], "", "La entrega", "package")
header(d, C["res"][0], YH, C["res"][1], "", "El resultado", "shield")

# ------------------------------------------------------------------ el problema: cuatro promesas
px, pw = C["pro"]
P = [("1  El producto existe", ["Diferencia de conteo: 12,4 %", "Meta: menos de 2 %"]),
     ("2  El precio es el exhibido", ["Precio distinto al cobrado: 11 %", "Meta: menos de 3 %"]),
     ("3  La entrega llega en la fecha", ["Entregas a tiempo: 81 %", "Meta: más de 97 %"]),
     ("4  Las condiciones del crédito", ["Evaluación en caja: 40 s a 3 min", "Meta: menos de 8 s"])]
prom = [box(d, px, Y0 + 20 + k * 230, pw, 200, t, ls, scope="cliente", tsize=24, lsize=23) for k, (t, ls) in enumerate(P)]
dos = box(d, px, Y0 + 20 + 4 * 230, pw, 170, "Dos negocios, un mostrador",
          ["Comercio minorista y crédito fiscalizado:", "datos y reglas que no se pueden mezclar"], scope="cliente", tsize=24, lsize=22)

# ------------------------------------------------------------------ la causa
cx, cw = C["cau"]
cau = box(d, cx, Y0 + 20, cw, 460, "Un estado sin fuente única",
          ["", "Varias escrituras a la vez sobre", "la misma existencia y precio,", "sin una fuente oficial"], scope="neutro", tsize=25, lsize=23, icon="database")
cau2 = box(d, cx, Y0 + 540, cw, 460, "Integraciones sin contrato",
           ["", "9 plataformas de 6 proveedores,", "14 conexiones punto a punto", "sin mapa ni contrato"], scope="neutro", tsize=25, lsize=23, icon="exchange")
fron = box(d, cx, Y0 + 1060, cw, 250, "Frontera difusa entre los negocios", [], scope="neutro", tsize=22)

# ------------------------------------------------------------------ la solución
sx, sw = C["sol"]
ret = container(d, sx, Y0 + 20, sw, 560, "Frente Retail")
box(d, sx + 14, Y0 + 80, sw - 28, 140, "Mercadería", ["Oferta · Abastecimiento · Existencias"], icon="package", icon_pos="left", lsize=23)
box(d, sx + 14, Y0 + 240, sw - 28, 140, "Venta", ["Pedidos · Ventas · Comisiones · Marketplace"], icon="cart", icon_pos="left", lsize=22)
box(d, sx + 14, Y0 + 400, sw - 28, 130, "Relación con el cliente", ["Posventa · Clientes Retail"], icon="users", icon_pos="left", lsize=23)
x01 = box(d, sx, Y0 + 640, sw, 130, "Control de cruces", ["Un solo paso autorizado entre los dos negocios"], icon="shield", icon_pos="left", lsize=22)
emi = container(d, sx, Y0 + 800, sw, 200, "Filial emisora")
box(d, sx + 14, Y0 + 860, sw - 28, 120, "Crédito", ["Originación · Cartera · Evidencia"], icon="card", icon_pos="left", lsize=23)
base = box(d, sx, Y0 + 1040, sw, 270, "Base tecnológica común",
           ["Integración por contrato · identidad ·", "observabilidad · tienda que vende 24 h sin enlace"], icon="gateway", icon_pos="left", lsize=22)
pr = box(d, sx + 650 - 0, Y0 + 0, 0, 0, "", []) if False else None

# ------------------------------------------------------------------ la entrega
ex, ew = C["ent"]
e1 = box(d, ex, Y0 + 20, ew, 420, "Etapa 1 · mes 16", ["Oferta · Existencias · Ventas", "Tienda sin enlace", "Originación · Evidencia", "Control de cruces · Cartera (parte)"], tsize=25, lsize=22, icon="package")
e2 = box(d, ex, Y0 + 480, ew, 340, "Etapa 2 · mes 21", ["Abastecimiento · Pedidos", "Comisiones · Marketplace", "Posventa · Clientes Retail", "Cartera (resto)"], tsize=25, lsize=22, icon="package")
e3 = box(d, ex, Y0 + 860, ew, 200, "Operación · 36 meses", ["Meses 21 a 56"], tsize=25, lsize=22)
inn = box(d, ex, Y0 + 1100, ew, 210, "Cinco innovaciones", ["Lockers · conteo predictivo · búsqueda", "vectorial · medios de retail · fila virtual"], tsize=24, lsize=20)

# ------------------------------------------------------------------ el resultado
rx, rw = C["res"]
R = [("Existencia fiable", ["Diferencia de conteo bajo 2 %"]), ("Precio único", ["Cobrado igual al exhibido: menos de 3 % de diferencia"]),
     ("Entrega prometida", ["Más de 97 % a tiempo, con estado único del pedido"]), ("Crédito claro y rápido", ["Evaluación en menos de 8 s, con evidencia por la vida del crédito"])]
res = [box(d, rx, Y0 + 20 + k * 230, rw, 200, t, ls, tsize=24, lsize=22) for k, (t, ls) in enumerate(R)]
sep = box(d, rx, Y0 + 20 + 4 * 230, rw, 170, "Dos negocios separados", ["Sin cruces sin finalidad", "ni vista unificada"], tsize=24, lsize=22)

legend(d, 20, Y0 + 1180, 360, extra=[("solid", "#1F1F1F", 3, "De la causa a la solución"), ("solid", ACCENT, 5, "Frontera entre negocios")])
d.text(2220, Y0 + 1180, 520, 150, "Cifras de hoy y metas: Subdocumento 2, Tabla 2.3.\nAlcance por etapa: Subdocumento 3, Tabla 3.1.", size=20, align="left")

for k in range(4):
    d.edge(prom[k], cau if k < 2 else cau2, "", width=2, line="dashed", exit=(1, 0.5), entry=(0, 0.25 + 0.5 * (k % 2)))
d.edge(dos, fron, "", width=2, line="dashed", exit=(1, 0.5), entry=(0, 0.5))
d.edge(cau, ret, "", width=W, exit=(1, 0.5), entry=(0, 0.3))
d.edge(cau2, base, "", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(fron, x01, "", color=ACCENT, width=5, exit=(1, 0.5), entry=(0, 0.5))
d.edge(ret, e1, "", width=W, exit=(1, 0.3), entry=(0, 0.3))
d.edge(emi, e2, "", width=W, exit=(1, 0.5), entry=(0, 0.8))
d.edge(e1, e2, "", width=W, exit=(0.5, 1), entry=(0.5, 0))
d.edge(e2, e3, "", width=W, exit=(0.5, 1), entry=(0.5, 0))
for k in range(4):
    d.edge(e1 if k < 2 else e2, res[k], "", width=2, exit=(1, 0.5), entry=(0, 0.5))
d.edge(x01, sep, "", color=ACCENT, width=4, exit=(1, 0.5), entry=(0, 0.5), points=[(1700, 1050), (1700, 1000), (2200, 1000), (2200, 1155)]) if False else None

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
