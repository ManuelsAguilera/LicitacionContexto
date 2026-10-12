"""Figura 4.20: centro de datos secundario, Azure Brazil South, y pasos de la conmutación.

Responde: ¿qué se replica a Brazil South y en qué orden se conmuta ante una falla de la región principal?
Seis marcadores numerados siguen los seis pasos del procedimiento de 4.3.2.
Vista de detalle (redibujada, no recortada del maestro: RR-13). Letra de 32 sobre ~1700.
Ejecutar: python3 04_Adjuntos/diagramas/diag-04-20_data-center-secundario.py
"""

import re
from pathlib import Path

from _drawio import ACCENT, Diagram

d = Diagram(font=32, zone_font=32)
Z, F = d.zone, d.fill
W = 3
MK = 46


def geo(cid):
    m = re.search(r'id="%s"[^>]*><mxGeometry x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"' % cid, "".join(d.cells))
    return tuple(float(g) for g in m.groups())


def cx(cid):
    g = geo(cid)
    return g[0] + g[2] / 2


def cy(cid):
    g = geo(cid)
    return g[1] + g[3] / 2


# ---- Fila superior ----
ope = d.icon(120, 60, "users", "Equipo de\noperación", size=70)
afd = d.icon(1010, 60, "frontdoor", "Front Door", size=70, label_pos="left")
tie = d.icon(1250, 60, "building", "Tiendas\n(nodo local)", size=70)
dc1 = d.icon(1590, 60, "server", "DC-01\ncasa matriz", size=70, label_pos="left")

RY = [350, 565, 780, 995]

# ---- Región principal ----
Z(20, 260, 690, 1230, "CLD-01 Chile Central", "region", align="left")
ap1 = d.icon(310, RY[0], "apim", "API Management\n(tres zonas)", size=70)
eh1 = d.icon(310, RY[1], "eventhubs", "Event Hubs\nPremium", size=70)
pg1 = d.icon(310, RY[2], "postgres", "PostgreSQL\nprimario", size=70)
ak1 = d.icon(310, RY[3], "aks", "AKS\n(en servicio)", size=70)

# ---- Región de recuperación ----
Z(930, 260, 750, 1230, "CLD-02 Brazil South", "region", align="center")
agw2 = d.icon(1010, RY[0], "appgw", "Application Gateway\n(Private Link)", size=70)
ap2 = d.icon(1420, RY[0], "apim", "Gateway regional\nde API Management", size=70)
eh2 = d.icon(1010, RY[1], "eventhubs", "Event Hubs\n(geo-réplica)", size=70)
pg2 = d.icon(1010, RY[2], "postgres", "PostgreSQL\n(réplica)", size=70)
ak2 = d.icon(1010, RY[3], "aks", "AKS por IaC\n(en espera)", size=70)
d.icon(1420, RY[1], "storage", "Storage\n(copia explícita)", size=70)
d.icon(1420, RY[2], "keyvault", "Key Vault propio\n(por IaC)", size=70)
d.icon(1420, RY[3], "backup", "Segunda bóveda\nde respaldo", size=70)

# ---- Hubs ----
h1 = Z(60, 1220, 610, 240, "Hub de CLD-01", "vnet")
fw1, vg1 = F(h1, [("firewall", "Azure\nFirewall"), ("vpngw", "Puerta VPN y\nExpressRoute")], size=70, top=85)
h2 = Z(960, 1220, 690, 240, "Hub de CLD-02", "vnet")
fw2, fg2, vg2 = F(h2, [("firewall", "Azure\nFirewall"), ("fw_site", "FortiGate-VM"), ("vpngw", "Puerta VPN")], size=70, top=85)

# ---- Aristas ----
d.edge(afd, agw2, "Private Link", color=ACCENT, width=W + 1, exit=(0.5, 1), entry=(0.5, 0), label_dy=-30)
d.edge(agw2, ap2, "", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(eh1, eh2, "retraso < 15 min", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5), label_dy=-34)
d.edge(pg1, pg2, "asíncrona", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5), label_dy=-34)
d.edge(ak1, ak2, "se crea con IaC", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5), label_dy=-34)
d.edge(dc1, vg2, "VPN", line="dashed", width=W, exit=(0.5, 1), entry=(1, 0.5), points=[(1625, cy(vg2))], label_dy=-30)

# ---- Marcadores de los seis pasos ----
def mk(x, y, n):
    d.marker(int(x), int(y), n, size=MK)


mk(205, 55, 1)    # declarar la contingencia
mk(900, RY[1] - 55, 2)   # promover Event Hubs
mk(900, RY[2] - 55, 3)   # promover PostgreSQL y habilitar su alta disponibilidad
mk(900, RY[3] - 55, 4)   # levantar AKS con la definición de infraestructura
mk(1120, 60, 5)   # Front Door redirige
mk(1335, 55, 6)   # verificar tiendas y conciliar

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
