"""Vista lógica 1 de 3: las ocho capas de RT-02.01, de izquierda a derecha (estilo D de FEP01, diap. 66).

Responde: ¿cómo se organiza el software, qué capa habla con cuál y qué es de quién?
Reglas de FEP01 (diap. 17 y 61): sin marcas ni productos de nube (eso es la vista física), nombres de negocio
y no códigos, una sola dirección de lectura, una sola idea por lámina, sistemas externos distinguibles por color
y leyenda. Los nombres coinciden con SD-03 (3.3.2) y SD-04 (4.1); los códigos R:/F:/X-01 se trazan en la Tabla 4.13.
Fuente: SD-03 (3.3), SD-04 (4.1, Tablas 4.1 y 4.2) y Bases Transversales (2.1 y RT-02.01 a RT-02.14).
Ejecutar: python3 04_Adjuntos/diagramas/diag-04-22_logica-1-capas.py
"""

from pathlib import Path

from _alcance import box, container, header, legend, pic
from _drawio import ACCENT, Diagram

d = Diagram(font=24, zone_font=27)
W = 3

# ------------------------------------------------------------------ columnas (x, ancho)
C = {"act": (20, 250), "pre": (305, 330), "bor": (670, 220), "gat": (925, 240), "ser": (1200, 560),
     "dat": (1795, 300), "int": (2130, 330), "ext": (2495, 360)}
YH, Y0 = 95, 195

header(d, C["act"][0], YH, C["act"][1], "", "Actores", "users")
header(d, C["pre"][0], YH, C["pre"][1], "", "Presentación", "monitor")
header(d, C["bor"][0], YH, C["bor"][1], "", "Borde y\nexposición", "globe")
header(d, C["gat"][0], YH, C["gat"][1], "", "Puerta de\nenlace", "gateway")
header(d, C["ser"][0], YH, C["ser"][1], "", "Servicios de negocio", "services")
header(d, C["dat"][0], YH, C["dat"][1], "", "Datos", "database")
header(d, C["int"][0], YH, C["int"][1], "", "Integración\ny eventos", "exchange")
header(d, C["ext"][0], YH, C["ext"][1], "", "Sistemas externos", "building")

# ------------------------------------------------------------------ servicios de negocio (capa 4)
sx, sw = C["ser"]
ret = container(d, sx, Y0 + 20, sw, 560, "Frente Retail")
m1 = box(d, sx + 14, Y0 + 85, sw - 28, 130, "Mercadería", ["Oferta comercial · Abastecimiento", "Existencias"], icon="package", icon_pos="left")
m2 = box(d, sx + 14, Y0 + 230, sw - 28, 150, "Venta", ["Pedidos · Ventas", "Comisiones · Marketplace"], icon="cart", icon_pos="left")
m3 = box(d, sx + 14, Y0 + 395, sw - 28, 130, "Relación con el cliente", ["Posventa · Clientes Retail"], icon="users", icon_pos="left")
x01 = box(d, sx, Y0 + 610, sw, 115, "Control de cruces (frontera)", ["Finalidad, datos mínimos y bitácora"], scope="oss", icon="shield", icon_pos="left")
emi = container(d, sx, Y0 + 760, sw, 235, "Filial emisora")
e1 = box(d, sx + 14, Y0 + 825, sw - 28, 165, "Crédito", ["Originación · Cartera", "Evidencia financiera"], icon="card", icon_pos="left")

# ------------------------------------------------------------------ resto de capas
ax, aw = C["act"]
a1 = box(d, ax, Y0 + 40, aw, 190, "Clientes, titulares\ny vendedores\nexternos", scope="tercero", tsize=22, icon="person")
a2 = box(d, ax, Y0 + 265, aw, 210, "Personal de tiendas,\ncentros de\ndistribución y\noficinas", scope="cliente", tsize=22, icon="users")
a3 = box(d, ax, Y0 + 770, aw, 190, "Ejecutivos y\npersonal financiero\nde la filial", scope="cliente", tsize=22, icon="person")

px, pw = C["pre"]
p1 = box(d, px, Y0 + 40, pw, 470, "Canales de Retail", ["Caja de tienda con nodo local", "(vende hasta 24 h sin enlace)", "", "Móviles y mesón", "Comercio electrónico*", "Consolas y portales", "Portal de vendedor"],
         scope="oss", lsize=23, icon="mobile")
p2 = box(d, px, Y0 + 770, pw, 190, "Canal financiero", ["Portal y sesión", "financiera separada"], scope="oss", icon="card")

bx, bw = C["bor"]
b1 = box(d, bx, Y0 + 40, bw, 470, "Único acceso público", ["Distribución", "y protección", "contra ataques"], scope="oss", lsize=23)
gx, gw = C["gat"]
g1 = box(d, gx, Y0 + 40, gw, 470, "Puerta de enlace", ["Identidad, cuotas,", "versiones y trazas", "de cada contrato", "", "Una por frente"], scope="oss", lsize=23)
g2 = box(d, gx, Y0 + 770, gw, 190, "Puerta de enlace", ["propia del frente"], scope="oss", lsize=23)

dx, dw = C["dat"]
dr = box(d, dx, Y0 + 40, dw, 200, "Datos de Retail", ["Transaccionales y", "analíticos separados"], scope="oss", lsize=23)
df = box(d, dx, Y0 + 610, dw, 115, "Datos de la frontera", ["Políticas y bitácora"], scope="oss", lsize=23)
de = box(d, dx, Y0 + 770, dw, 120, "Datos del Emisor", ["Evidencia y analítica"], scope="oss", lsize=23)

ix, iw = C["int"]
i1 = box(d, ix, Y0 + 40, iw, 960, "Integración y eventos",
         ["", "Hechos confirmados", "con reintento y", "deduplicación", "", "", "Adaptadores y", "contratos por sistema", "con tiempo límite,", "cortacircuitos y", "modo degradado"], scope="oss")
ex, ew = C["ext"]
x1 = box(d, ex, Y0 + 40, ew, 330, "Sistemas del Cliente\nque se conservan", ["ERP y facturación", "Almacén (WMS)", "Marketplace", "Comercio electrónico*", "Fidelización*"], scope="cliente", lsize=23, icon="building")
x2 = box(d, ex, Y0 + 400, ew, 270, "Plataformas actuales\nen convivencia", ["Núcleo Retail 2009", "Crédito 2011", "Punto de venta 2014"], scope="cliente", dashed=True, lsize=23, icon="server")
x3 = box(d, ex, Y0 + 700, ew, 310, "Terceros", ["Medios de pago", "Transportistas", "Proveedores", "Fiscalización", "y regulador"], scope="tercero", lsize=23, icon="truck")

# ------------------------------------------------------------------ transversales (capas 7 y 8)
tx, tw = C["pre"][0], C["ext"][0] + C["ext"][1] - C["pre"][0]
sec = box(d, tx, Y0 + 1040, tw, 90, "Seguridad transversal", [], scope="neutro")
pic(d, tx + 14, Y0 + 1052, "shield", 54)
d.text(tx + 20, Y0 + 1080, tw - 40, 40, "Identidad por frente, roles y finalidad · secretos y cifrado · auditoría en ambos extremos del cruce", size=22)
obs = box(d, tx, Y0 + 1150, tw, 90, "Observabilidad transversal", [], scope="neutro")
pic(d, tx + 14, Y0 + 1162, "pulse", 54)
d.text(tx + 20, Y0 + 1190, tw - 40, 40, "Métricas, registros y trazas correlacionadas de nube, tiendas y centros", size=22)

# ------------------------------------------------------------------ leyenda
legend(d, 20, Y0 + 1040, 270, extra=[("solid", "#1F1F1F", 3, "Llamada con respuesta"), ("dashed", "#1F1F1F", 3, "Hecho confirmado"), ("solid", ACCENT, 5, "Cruce autorizado")])
d.text(20, Y0 + 1380, 560, 60, "* Se conservan al inicio; su destino lo decide la Etapa 1.", size=20, align="left")

# ------------------------------------------------------------------ flujos
d.edge(a1, p1, "", width=W, exit=(1, 0.5), entry=(0, 0.2))
d.edge(a2, p1, "", width=W, exit=(1, 0.5), entry=(0, 0.6))
d.edge(a3, p2, "", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(p1, b1, "", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(b1, g1, "", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(p2, g2, "", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(g1, ret, "", width=W, exit=(1, 0.5), entry=(0, 0.455))
d.edge(g2, e1, "", width=W, exit=(1, 0.5), entry=(0, 0.24))
# cruce autorizado
d.edge(ret, x01, "", color=ACCENT, width=5, exit=(0.5, 1), entry=(0.5, 0))
d.edge(x01, emi, "", color=ACCENT, width=5, exit=(0.5, 1), entry=(0.5, 0))
# datos
d.edge(m1, dr, "", width=W, exit=(1, 0.5), entry=(0, 0.55))
d.edge(x01, df, "", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(e1, de, "", width=W, exit=(1, 0.21), entry=(0, 0.75))
# eventos y adaptadores
d.edge(ret, i1, "", line="dashed", width=W, exit=(1, 0.679), entry=(0, 0.375))
d.edge(emi, i1, "", line="dashed", width=W, exit=(1, 0.809), entry=(0, 0.948))
d.edge(i1, x1, "", width=W, exit=(1, 0.15), entry=(0, 0.5))
d.edge(i1, x2, "", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(i1, x3, "", width=W, exit=(1, 0.85), entry=(0, 0.5))

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
