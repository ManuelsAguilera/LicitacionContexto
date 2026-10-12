"""Figura 4.14: red y segmentación del despliegue en nube.

Responde: ¿cómo se separa y se protege la red, y por dónde pasa el único cruce entre ámbitos?
Vista de detalle del hub y los tres spokes (redibujada, no recortada del maestro: RR-13).
Letra de 32 unidades sobre un lienzo de ~1640: a ancho de página (~499 pt) queda sobre 9 pt.
Ejecutar: python3 04_Adjuntos/diagramas/diag-04-14_red-y-segmentacion.py
"""

import re
from pathlib import Path

from _drawio import ACCENT, Diagram

d = Diagram(font=32, zone_font=32)
Z, F = d.zone, d.fill
W = 3

# ---- Fila superior: exterior y borde de Azure ----
ext = Z(20, 20, 260, 190, "Exterior", "plain")
cli, = F(ext, [("users", "Clientes y\ncontrapartes")], size=70, top=44)
brd = Z(790, 20, 820, 190, "Borde de Azure", "plain")
afd, = F(brd, [("frontdoor", "Front Door + WAF")], size=70, top=44)

# ---- Hub ----
hub = Z(320, 250, 380, 1190, "Hub", "vnet")
gws = Z(335, 295, 350, 195, "GatewaySubnet", "subnet")
ergw, vpngw = F(gws, [("vpngw", "Puerta\nExpressRoute"), ("vpngw", "Puerta\nVPN")], size=60, top=52)
rss = Z(335, 530, 350, 195, "RouteServerSubnet", "subnet")
rsv, = F(rss, [("router", "Route Server")], size=60, top=52)
sdw = Z(335, 765, 350, 195, "Subred SD-WAN", "subnet")
fv1, fv2 = F(sdw, [("fw_site", "FortiGate\nVM zona 1"), ("fw_site", "FortiGate\nVM zona 2")], size=60, top=52)
fws = Z(335, 1000, 350, 195, "AzureFirewallSubnet", "subnet")
afw, = F(fws, [("firewall", "Azure Firewall\nPremium")], size=60, top=52)
bas = Z(335, 1235, 350, 195, "AzureBastionSubnet", "subnet")
bst, = F(bas, [("bastion", "Azure Bastion")], size=60, top=52)

# ---- Spokes (de arriba abajo: Retail, Emisor, base tecnológica) ----
COLX = [805, 1005, 1205, 1405]


def band(y, h, title, subs, kind="vnet"):
    z = Z(790, y, 820, h, title, kind, align="left")
    ids = []
    for x, (st, icon, label) in zip(COLX, subs):
        sz = Z(x, y + 55, 190, h - 75, st, "subnet")
        ids.append(F(sz, [(icon, label)], size=70, top=50)[0])
    return z, ids


ret, (r_ag, r_apim, r_aks, r_dat) = band(250, 375, "Ámbito Retail", [
    ("Entrada", "appgw", "App\nGateway"), ("APIM", "apim", "API\nManagement"),
    ("Aplicación", "aks", "Servicios\n(AKS)"), ("Datos", "pe", "Datos\n(puntos\nprivados)")])
emi, (e_ag, e_apim, e_aks, e_dat) = band(650, 375, "Ámbito Emisor", [
    ("Entrada", "appgw", "App\nGateway"), ("APIM", "apim", "API\nManagement"),
    ("Aplicación", "aks", "Servicios\n(AKS)"), ("Datos", "pe", "Datos\n(puntos\nprivados)")])
com, (c_aks, c_age, c_acr) = band(1050, 390, "Base tecnológica", [
    ("Aplicación", "aks", "X-01 y\nadaptadores"), ("Agentes", "devpools", "Agentes\nCI/CD"),
    ("Registro", "acr", "Registro de\nimágenes")])


def cy(cid):
    m = re.search(r'id="%s"[^>]*><mxGeometry x="[\d.]+" y="([\d.]+)" width="[\d.]+" height="([\d.]+)"' % cid, "".join(d.cells))
    return float(m.group(1)) + float(m.group(2)) / 2


def yz(zid, fr):
    r = d.rects[zid]
    return r[1] + r[3] * fr


# ---- Fuera de Azure ----
out = Z(20, 250, 260, 1190, "Fuera de Azure", "plain")
tie = d.icon(115, int(cy(fv1) - 35), "building", "Tiendas y\ncentros", size=70)
dc = d.icon(115, int(cy(ergw) - 35), "server", "DC-01", size=70)
adm = d.icon(115, int(cy(bst) - 35), "users", "Administradores\n(Entra Private\nAccess)", size=70)

# ---- Aristas ----
d.edge(cli, brd, "HTTPS", width=W, exit=(1, 0.5), entry=(0, 0.4))
d.edge(tie, fv1, "SD-WAN", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(dc, ergw, "propuesto", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(adm, bst, "", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(rss, sdw, "BGP", line="dotted", width=W, exit=(0.5, 1), entry=(0.5, 0))
d.edge(sdw, fws, "UDR", width=W, exit=(0.5, 1), entry=(0.5, 0))

# Front Door -> entrada de Retail y de Emisor por Private Link
d.edge(brd, r_ag, "Private Link", width=W, exit=(0, 0.85), entry=(0, 0.5), label_pos=-0.78,
       points=[(772, 181), (772, cy(r_ag))])
d.edge(brd, e_ag, "", width=W, exit=(0, 0.85), entry=(0, 0.5), points=[(772, 181), (772, cy(e_ag))])

# Flujo dentro de cada ámbito
for a, b, c, e in ((r_ag, r_apim, r_aks, r_dat), (e_ag, e_apim, e_aks, e_dat)):
    d.edge(a, b, "", width=W, exit=(1, 0.5), entry=(0, 0.5))
    d.edge(b, c, "", width=W, exit=(1, 0.5), entry=(0, 0.5))
    d.edge(c, e, "", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(c_aks, c_age, "", width=W, exit=(1, 0.5), entry=(0, 0.5))

# Único cruce entre ámbitos: siempre por Azure Firewall hacia X-01
acc = dict(color=ACCENT, width=W + 1, both=True)
d.edge(ret, fws, "cruce X-01", exit=(0, 0.2), entry=(1, 0.2), label_pos=0.05,
       points=[(718, yz(ret, 0.2)), (718, yz(fws, 0.2))], **acc)
d.edge(emi, fws, "", exit=(0, 0.2), entry=(1, 0.5), points=[(733, yz(emi, 0.2)), (733, yz(fws, 0.5))], **acc)
d.edge(com, fws, "", exit=(0, 0.5), entry=(1, 0.8), points=[(748, yz(com, 0.5)), (748, yz(fws, 0.8))], **acc)

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
