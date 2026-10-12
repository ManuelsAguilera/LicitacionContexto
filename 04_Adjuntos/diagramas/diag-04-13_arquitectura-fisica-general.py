"""Figura 4.13: arquitectura física general, vista de conjunto.

Responde: ¿dónde está cada cosa y cómo se conecta?
Vista general simplificada (15 elementos). Letra de 32 unidades sobre un lienzo de ~1510:
a ancho de página (~450 pt) queda en cerca de 9 pt. El detalle por parte va en las figuras 4.14 a 4.19.
El maestro completo está en diag-04-maestro_arquitectura-fisica-completa.*
Ejecutar: python3 04_Adjuntos/diagramas/diag-04-13_arquitectura-fisica-general.py
"""

import re
from pathlib import Path

from _drawio import ACCENT, Diagram

d = Diagram(font=32, zone_font=33)
Z, F = d.zone, d.fill
W = 3  # grosor de línea

# ---- Exterior y borde global (fila superior) ----
ext = Z(380, 20, 570, 190, "Exterior", "plain")
cli, cpt = F(ext, [("users", "Clientes\ny app"), ("globe", "Contrapartes\n(EXT-01)")], size=70, top=40)
brd = Z(985, 20, 300, 190, "Borde de Azure", "plain")
afd, = F(brd, [("frontdoor", "Front Door\n+ WAF")], size=70, top=40)

# ---- Sitios del Cliente ----
Z(20, 20, 330, 940, "Sitios del Cliente", "onprem")
sit_z = Z(35, 70, 300, 875, "", "plain")
sit, cd1, cd2, dc1, dc2 = F(sit_z, [
    ("building", "SIT-01\n22 tiendas"), ("building", "CD-01\ndistribución"),
    ("building", "CD-02\nConcepción"), ("server", "DC-01\ncasa matriz"),
    ("server", "DC-02\nsala de respaldo")], cols=1, size=70, top=6)

# ---- Conexiones ----
con = Z(380, 230, 270, 730, "Conexiones", "plain")
inet, erc = F(con, [("cloud", "Internet\n(red SD-WAN)"), ("ercircuit", "ExpressRoute\n(propuesto)")], cols=1, size=70, top=50)

# ---- Azure Chile Central ----
Z(680, 230, 625, 730, "CLD-01 Chile Central", "region", align="left")
hub = Z(705, 295, 205, 645, "Hub", "vnet")
fgv, ergw, afw = F(hub, [("fw_site", "FortiGate-VM\n(SD-WAN)"), ("vpngw", "Puerta\nExpressRoute"),
                         ("firewall", "Azure\nFirewall")], cols=1, size=70, top=40)
ret = Z(985, 295, 300, 200, "Ámbito Retail", "vnet")
reti, = F(ret, [("aks", "Servicios y\ndatos Retail")], size=70, top=50)
com = Z(985, 510, 300, 200, "Base tecnológica", "vnet")
comi, = F(com, [("aks", "X-01 y\nadaptadores")], size=70, top=50)
emi = Z(985, 725, 300, 215, "Ámbito Emisor", "vnet")
emii, = F(emi, [("aks", "Servicios y\ndatos Emisor")], size=70, top=50)

# ---- Azure Brazil South ----
Z(1330, 230, 210, 730, "CLD-02\nBrazil South", "region", align="left")
dret = Z(1345, 335, 180, 180, "Retail", "vnet")
dreti, = F(dret, [("aks", "en espera")], size=60, top=72)
demi = Z(1345, 530, 180, 180, "Emisor", "vnet_cond")
demii, = F(demi, [("aks", "condicionada")], size=60, top=72)
dhub = Z(1345, 725, 180, 215, "Hub", "vnet")
dhubi, = F(dhub, [("firewall", "Firewall y\npuerta VPN")], size=60, top=72)


def cy(cid):
    m = re.search(r'id="%s"[^>]*><mxGeometry x="[\d.]+" y="([\d.]+)" width="[\d.]+" height="([\d.]+)"' % cid, "".join(d.cells))
    return float(m.group(1)) + float(m.group(2)) / 2


def yz(zid, fr):
    r = d.rects[zid]
    return r[1] + r[3] * fr


def xz(zid, fr):
    r = d.rects[zid]
    return r[0] + r[2] * fr


# ---- Aristas ----
BUS = 365
for s_ in (sit, cd1, cd2):
    d.edge(s_, inet, "", width=W, exit=(1, 0.5), entry=(0, 0.5), points=[(BUS, cy(s_)), (BUS, cy(inet))])
d.edge(dc1, erc, "propuesto", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5), points=[(BUS, cy(dc1)), (BUS, cy(erc))])
d.edge(dc1, dc2, "", line="dashed", width=W, exit=(0, 0.5), entry=(0, 0.5), points=[(52, cy(dc1)), (52, cy(dc2))])

d.edge(inet, fgv, "SD-WAN", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(erc, ergw, "", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5))

d.edge(ext, brd, "HTTPS", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(brd, ret, "", width=W, exit=(0.5, 1), entry=(0.5, 0))
d.edge(brd, emi, "", width=W, exit=(0.5, 1), entry=(0.5, 0), points=[(1135, 278), (962, 278), (962, 717), (1135, 717)])

# Único cruce entre ámbitos: siempre por Azure Firewall hacia X-01
acc = dict(color=ACCENT, width=W + 1, both=True)
d.edge(ret, afw, "cruce X-01", exit=(0, 0.5), entry=(1, 0.25), label_pos=-0.85,
       points=[(927, yz(ret, 0.5)), (927, cy(afw) - 18)], **acc)
d.edge(com, afw, "", exit=(0, 0.5), entry=(1, 0.5), points=[(939, yz(com, 0.5)), (939, cy(afw))], **acc)
d.edge(emi, afw, "", exit=(0, 0.5), entry=(1, 0.75), points=[(951, yz(emi, 0.5)), (951, cy(afw) + 18)], **acc)

d.edge(ret, dret, "réplica", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5), label_dy=-34)
d.edge(emi, demi, "", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5))

d.edge(dhub, hub, "VPN entre hubs", line="dashed", width=W, exit=(0.5, 1), entry=(0.5, 1), points=[(1435, 990), (807, 990)], label_dy=-26)

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
