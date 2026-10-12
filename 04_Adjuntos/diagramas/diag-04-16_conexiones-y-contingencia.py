"""Figura 4.16: conexiones, puntos de falla y contingencias.

Responde: ¿dónde puede fallar la solución y qué camino alterno existe?
Ocho puntos numerados, cada uno con su camino alterno (línea discontinua) o su respaldo.
Vista de detalle (redibujada, no recortada del maestro: RR-13). Letra de 32 sobre ~1720.
Ejecutar: python3 04_Adjuntos/diagramas/diag-04-16_conexiones-y-contingencia.py
"""

import re
from pathlib import Path

from _drawio import ACCENT, Diagram

d = Diagram(font=32, zone_font=32)
Z, F = d.zone, d.fill
W = 3
MK = 46  # tamaño de los marcadores


def geo(cid):
    m = re.search(r'id="%s"[^>]*><mxGeometry x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"' % cid, "".join(d.cells))
    return tuple(float(g) for g in m.groups())


def cy(cid):
    g = geo(cid)
    return g[1] + g[3] / 2


def mark(cid, n, dx=30, dy=-52):
    x, y, w, h = geo(cid)
    d.marker(int(x + dx), int(y + dy), n, size=MK)


# ---- Sitios del Cliente ----
Z(20, 20, 310, 1010, "Sitios del Cliente", "onprem")
sit_z = Z(35, 70, 280, 945, "", "plain")
sit, cd1, cd2, dc1 = F(sit_z, [
    ("building", "SIT-01\ntiendas"), ("building", "CD-01\nWMS"),
    ("building", "CD-02\nConcepción"), ("server", "DC-01\nERP/DTE")], cols=1, size=70, top=14)

# ---- Conexiones ----
con = Z(370, 20, 280, 1010, "Conexiones", "plain")
inet, lte, erc, vpn = F(con, [("cloud", "Internet\n(SD-WAN)"), ("antenna", "Respaldo\nLTE/5G"),
                              ("ercircuit", "ExpressRoute\n(propuesto)"), ("vpngw", "VPN de\nrespaldo")],
                        cols=1, size=70, top=60)

# ---- Chile Central ----
reg = Z(690, 20, 620, 1010, "CLD-01 Chile Central", "region", align="left")
zs = []
for i in range(3):
    z = Z(710 + i * 195, 90, 185, 380, f"Zona {i + 1}", "subnet")
    zs.append(F(z, [("aks", "Servicios\n(AKS)")], size=70, top=70)[0])
dat = Z(710, 495, 575, 500, "Datos y eventos", "inner")
eh, pg = F(dat, [("eventhubs", "Event Hubs\n(entre zonas)"), ("postgres", "PostgreSQL\nprimario y\nen espera")], size=70, top=70)

# ---- Brazil South ----
bra = Z(1340, 20, 360, 1010, "CLD-02 Brazil South", "region", align="left")
b1, b2, b3 = F(bra, [("aks", "AKS por IaC\n(en espera)"), ("eventhubs", "Event Hubs\n(réplica)"),
                     ("postgres", "PostgreSQL\n(réplica)")], cols=1, size=70, top=60)

# ---- Aristas ----
BUS, BUS2 = 345, 357
for s_ in (sit, cd1, cd2):
    d.edge(s_, inet, "", width=W, exit=(1, 0.5), entry=(0, 0.5), points=[(BUS, cy(s_)), (BUS, cy(inet))])
for s_ in (sit, cd2):
    d.edge(s_, lte, "", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5), points=[(BUS2, cy(s_)), (BUS2, cy(lte))])
d.edge(dc1, erc, "", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5), points=[(BUS, cy(dc1)), (BUS, cy(erc))])
d.edge(dc1, vpn, "", line="dotted", width=W, exit=(1, 0.5), entry=(0, 0.5), points=[(BUS2, cy(dc1)), (BUS2, cy(vpn))])
for c_, ls in ((inet, "solid"), (lte, "dashed"), (erc, "dashed"), (vpn, "dotted")):
    d.edge(c_, reg, "", line=ls, width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(reg, bra, "réplica", line="dashed", width=W, color=ACCENT, exit=(1, 0.5), entry=(0, 0.5), label_dy=-34)

# ---- Marcadores: los ocho puntos de falla ----
mark(sit, 1)            # enlace de tienda
mark(cd2, 2)            # enlace único de CD-02
mark(erc, 3)            # ExpressRoute a DC-01
d.marker(714, 150, 4, size=MK)  # una zona de Chile Central (sobre Zona 1)
d.marker(1288, 28, 5, size=MK)  # la región
mark(dc1, 6)            # ERP/DTE
mark(cd1, 7)            # WMS
mark(eh, 8)             # broker de eventos

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
