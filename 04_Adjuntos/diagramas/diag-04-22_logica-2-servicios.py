"""Vista lógica 2 de 3: servicios de negocio y sus flujos, con la frontera entre Retail y la filial emisora.

Responde: ¿qué hace cada servicio, quién le entrega qué y por dónde cruza una persona o un dato de un negocio al otro?
Un solo nivel (módulos); sin marcas ni códigos técnicos (FEP01, diap. 61). Mismo estilo de columnas que la vista 1.
Fuente: SD-03 (3.3.2) y SD-04 (4.1, Tablas 4.2 y 4.13). Los códigos R:/F:/X-01 se trazan en la Tabla 4.13.
Ejecutar: python3 04_Adjuntos/diagramas/diag-04-22_logica-2-servicios.py
"""

from pathlib import Path

from _alcance import box, container, legend, pic
from _drawio import ACCENT, Diagram

d = Diagram(font=24, zone_font=27)
W = 3
X = [300, 900, 1500]   # columnas de áreas
CW, BW = 540, 480      # ancho de contenedor y de caja

# ------------------------------------------------------------------ Frente Retail
ret = container(d, 280, 100, 1800, 850, "Frente Retail")
m = container(d, X[0], 160, CW, 750, "Mercadería")
v = container(d, X[1], 160, CW, 750, "Venta")
r = container(d, X[2], 160, CW, 750, "Relación con el cliente")


ICON = {'Oferta comercial': 'database', 'Abastecimiento': 'truck', 'Existencias': 'package', 'Pedidos': 'cart', 'Marketplace': 'globe', 'Comisiones': 'card', 'Ventas': 'monitor', 'Posventa': 'users', 'Clientes Retail': 'person'}


def svc(col, y, title, lines):
    return box(d, X[col] + 30, y, BW, 120, title, lines, lsize=22, tsize=25, icon=ICON[title], icon_pos="left")


oferta = svc(0, 230, "Oferta comercial", ["Artículos, precios y promociones", "vigentes por canal"])
abast = svc(0, 410, "Abastecimiento", ["Órdenes, transferencias y reposición"])
exist = svc(0, 590, "Existencias", ["Disponible, reservas y conteos"])
pedidos = svc(1, 230, "Pedidos", ["Estado único y nodo de preparación"])
market = svc(1, 410, "Marketplace", ["Vendedores externos y devoluciones"])
comis = svc(1, 590, "Comisiones", ["Atribuye la venta a canal y vendedor"])
ventas = svc(1, 770, "Ventas", ["Cajas y canal digital, con o sin enlace"])
posv = svc(2, 590, "Posventa", ["Devoluciones, reclamos y garantía"])
clien = svc(2, 770, "Clientes Retail", ["Identidad comercial y consentimientos"])

# ------------------------------------------------------------------ Frontera y Filial emisora
x01 = box(d, 900, 1000, 1140, 110, "Control de cruces", ["Finalidad aprobada, datos mínimos y bitácora de cada cruce"], lsize=23, icon="shield", icon_pos="left")
emi = container(d, 900, 1160, 1140, 330, "Filial emisora · Crédito")
cart = box(d, 930, 1230, 340, 220, "Cartera", ["Saldos, cuotas", "y cobranza"], lsize=22, tsize=25, icon="card")
orig = box(d, 1300, 1230, 340, 220, "Originación", ["Evalúa y aprueba", "la compra a crédito"], lsize=22, tsize=25, icon="exchange")
evid = box(d, 1670, 1230, 340, 220, "Evidencia financiera", ["Consentimiento y", "documentos del crédito"], lsize=22, tsize=25, icon="shield")

# ------------------------------------------------------------------ puertas de enlace
g1 = box(d, 20, 400, 230, 330, "Puerta de enlace", ["de Retail", "", "Toda entrada a", "los servicios"], lsize=22, icon="gateway")
g2 = box(d, 20, 1260, 230, 200, "Puerta de enlace", ["propia de la filial"], lsize=22, icon="gateway")

# ------------------------------------------------------------------ flujos
d.edge(g1, m, "", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(g1, v, "", width=W, exit=(0.5, 0), entry=(0.5, 0), points=[(135, 60), (1170, 60)])
d.edge(g1, r, "", width=W, exit=(0.5, 0), entry=(0.5, 0), points=[(135, 60), (1770, 60)])
d.edge(g2, emi, "", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(oferta, pedidos, "precio", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(pedidos, exist, "reserva", width=W, exit=(0, 0.8), entry=(1, 0.3), points=[(870, 326), (870, 626)])
d.edge(abast, exist, "", width=W, exit=(0.5, 1), entry=(0.5, 0))
d.edge(ventas, comis, "venta", line="dashed", width=W, exit=(0.5, 0), entry=(0.5, 1))
d.edge(ventas, posv, "venta", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5), points=[(1470, 830), (1470, 650)])
d.edge(ventas, x01, "", color=ACCENT, width=5, exit=(0.5, 1), entry=(0.2, 0))
d.edge(clien, x01, "", color=ACCENT, width=5, exit=(0.5, 1), entry=(0.8, 0))
d.edge(x01, orig, "", color=ACCENT, width=5, exit=(0.5, 1), entry=(0.5, 0))
d.edge(orig, cart, "", width=W, exit=(0, 0.5), entry=(1, 0.5))
d.edge(orig, evid, "", width=W, exit=(1, 0.5), entry=(0, 0.5))

# ------------------------------------------------------------------ leyenda y notas
legend(d, 2130, 960, 330, extra=[("solid", "#1F1F1F", 3, "Llamada con respuesta"), ("dashed", "#1F1F1F", 3, "Hecho confirmado"),
                                  ("solid", ACCENT, 5, "Cruce autorizado")])
d.text(2130, 1320, 400, 160, "Cada servicio escribe solo en sus datos. Los demás consumen sus hechos o llaman a su contrato; ninguno lee su base.",
       size=21, align="left")

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
