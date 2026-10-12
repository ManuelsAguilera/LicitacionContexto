"""Maestro de la arquitectura física completa (fuente de verdad del inventario, no es una figura del documento), sitios del Cliente y Azure.

Responde: ¿qué infraestructura física soporta la solución y cómo se conecta?
Inventario: plan del 2026-10-11 (Caso 09, Bases Transversales RT-03/06/07/08/11/12, SD-04).
Ejecutar: python3 04_Adjuntos/diagramas/diag-04-maestro_arquitectura-fisica-completa.py
"""

from pathlib import Path

from _drawio import ACCENT, Diagram

d = Diagram(font=13, zone_font=16)
Z = d.zone
F = d.fill

# ============ A. Exterior y B. borde global (franja superior) ============
ext = Z(1010, 20, 700, 230, "Exterior", "plain")
cli, rem, cpt, eco = F(ext, [
    ("users", "Clientes web\ny app"),
    ("laptop", "Personas\ntrabajadoras remotas"),
    ("globe", "Contrapartes\n(pagos, marketplace,\ntransporte, SII)"),
    ("browser", "Comercio electrónico\ny fidelización\n(externos)"),
], size=48)

edge_g = Z(1760, 20, 1000, 230, "Borde global de Azure", "plain")
dns, afd, zta = F(edge_g, [
    ("dns", "Azure DNS\npúblico"),
    ("frontdoor", "Front Door Premium\n+ WAF y antibots"),
    ("privateaccess", "Entra Private Access\n(confianza cero)"),
], size=48)

# ============ F. Sitios del Cliente (columna izquierda) ============
# F1 Tienda tipo
Z(20, 280, 960, 740, "Tienda tipo  (×22: 14 en centro comercial, 8 a la calle)", "onprem", align="left")
gab = Z(660, 320, 300, 420, "Gabinete de comunicaciones", "subnet")
ha = Z(675, 358, 270, 125, "Par HA (activo-pasivo)", "inner")
fg1, fg2 = F(ha, [("fw_site", "FortiGate 1\n(activo)"), ("fw_site", "FortiGate 2\n(pasivo)")], size=46)
st = Z(675, 505, 270, 115, "Switches de acceso (pila)", "inner")
sw1, sw2 = F(st, [("switch_acc", "Switch 1"), ("switch_acc", "Switch 2")], size=46)
ups_z = Z(815, 630, 130, 105, "Energía", "inner")
ups, = F(ups_z, [("ups", "UPS")], size=34, top=36)
nodo = Z(660, 760, 300, 240, "Nodo local (RAID 1)", "subnet")
n1, n2 = F(nodo, [("srv", "Servidor 1 (activo)\nL-01 caché · L-02 diario"), ("srv", "Servidor 2 (en espera)\nL-03 sincronizador")], size=50)

vl = Z(40, 320, 600, 680, "Redes por función (una VLAN cada una)", "plain")
v = [Z(55 + (i % 2) * 295, 360 + (i // 2) * 210, 280, 195, t, "subnet") for i, t in enumerate([
    "VLAN cajas", "VLAN administración", "VLAN móviles", "VLAN video",
    "VLAN Wi-Fi clientes", "VLAN Emisor (mesón financiero)"])]
F(v[0], [("pos", "POS"), ("handheld", "Terminal\nde pago"), ("printer", "Impresora\nfiscal")], size=42)
F(v[1], [("workstation", "PC"), ("printer", "Impresora\nde etiquetas")], size=42)
F(v[2], [("cell", "640 terminales\ncompartidas"), ("ap", "AP SSID corporativo\n(certificado)")], size=42)
F(v[3], [("camera", "Cámaras"), ("nvr", "NVR\n30 días")], size=42)
F(v[4], [("ap", "AP SSID clientes\n(aislado)")], size=42)
F(v[5], [("workstation", "Puesto del Emisor\n(túnel propio)")], size=42)


# F2 CD-01 y F3 CD-02
cd1z = Z(20, 1050, 470, 280, "CD-01  Distribución principal", "onprem", valign="bottom")
cd1_fw, cd1_sw, cd1_ap, cd1_wms = F(cd1z, [
    ("fw_site", "FortiGate\npar HA"), ("switch", "Switches de núcleo\n(pila)"),
    ("ap", "Wi-Fi industrial\n(terminales RF)"), ("srv", "Servidores WMS\n(conservados)")], cols=2, size=42)
cd2z = Z(510, 1050, 470, 280, "CD-02  Distribución Concepción", "onprem", valign="bottom")
cd2_fw, cd2_sw, cd2_ws, cd2_lte = F(cd2z, [
    ("fw_site", "FortiGate\npar HA"), ("switch_acc", "Switches de acceso\n(pila)"),
    ("workstation", "Puestos de\ncarga estructurada"), ("antenna", "Respaldo LTE/5G\n(propuesto)")], cols=2, size=42)

# F4 DC-01 y F5 DC-02
Z(20, 1360, 760, 660, "DC-01  Recinto técnico casa matriz (140 m²)", "onprem", align="left")
rc = Z(40, 1436, 230, 404, "Rack de comunicaciones", "subnet", valign="bottom")
dha = Z(55, 1452, 200, 148, "Par HA (activo-pasivo)", "inner", valign="bottom")
dfw1, dfw2 = F(dha, [("fw_site", "FortiGate 1"), ("fw_site", "FortiGate 2")], size=40, top=10)
dco = Z(55, 1615, 200, 150, "Switches de núcleo (pila)", "inner")
csw1, csw2 = F(dco, [("switch", "Switch 1"), ("switch", "Switch 2")], size=40)
rs = Z(290, 1436, 470, 404, "Racks de servidores (plataformas conservadas*)", "subnet")
zr = Z(305, 1476, 215, 160, "Zona Retail", "inner")
erp, nuc = F(zr, [("srv", "ERP/DTE"), ("srv", "Sistema\nnúcleo 2009")], size=40)
ze = Z(530, 1476, 215, 160, "Zona Emisor", "inner")
cre, = F(ze, [("srv", "Crédito 2011")], size=40)
san, bkp, tape = F(Z(305, 1650, 215, 180, "Almacenamiento Retail", "inner"), [
    ("san", "SAN\nRetail"), ("nvr", "Respaldo\nlocal"), ("san", "Cinta fuera\nde línea")], cols=2, size=36)
san_e, bkp_e, tape_e = F(Z(530, 1650, 215, 180, "Almacenamiento Emisor", "inner"), [
    ("san", "SAN\nEmisor"), ("nvr", "Respaldo\nlocal"), ("san", "Cinta fuera\nde línea")], cols=2, size=36)
Z(40, 1855, 720, 150, "Instalaciones del recinto", "band")
d.text(50, 1885, 700, 50,
       "UPS 30 min  ·  generador 24 h  ·  climatización N+1  ·  detección temprana por aspiración  ·  extinción por agente limpio\n"
       "control biométrico  ·  CCTV 30 días  ·  NOC en sala separada", size=13)

dc2z = Z(800, 1360, 180, 300, "DC-02  Respaldo", "onprem")
dc2b, = F(dc2z, [("nvr", "Copia de\nrespaldo")], size=46)

# ============ E. Franja WAN ============
inet = d.icon(1090, 520, "cloud", "Internet\n(overlay SD-WAN IPsec)", size=90, shape_fill="#5EA0EF")
lte = d.icon(1110, 830, "antenna", "Red LTE/5G\n(otro operador)", size=50)
erc1 = d.icon(1070, 1500, "ercircuit", "ExpressRoute\nproveedor A", size=50)
erc2 = d.icon(1070, 1620, "ercircuit", "ExpressRoute proveedor B\n(ruta física distinta)", size=50)

# ============ C. Azure Chile Central ============
Z(1300, 290, 1460, 1460, "Azure Chile Central (CLD-01)  ·  3 zonas de disponibilidad", "region", align="left")
hub = Z(1330, 340, 300, 1380, "Hub", "vnet")
gws = Z(1350, 380, 260, 190, "GatewaySubnet", "subnet")
ergw, vpngw = F(gws, [("vpngw", "ExpressRoute GW\nzona-redundante"), ("vpngw", "VPN GW\nzona-redundante")])
bas = Z(1350, 582, 260, 130, "AzureBastionSubnet", "subnet")
bst, = F(bas, [("bastion", "Azure Bastion\n(SKU Premium)")])
rss = Z(1350, 724, 260, 140, "RouteServerSubnet", "subnet")
rsv, = F(rss, [("router", "Azure Route Server\n(BGP con los FortiGate-VM)")])
sdw = Z(1350, 876, 260, 220, "Subred SD-WAN  (activo-activo)", "subnet")
fv1, fv2 = F(sdw, [("fw_site", "FortiGate-VM 1\nzona 1 · IP pública"), ("fw_site", "FortiGate-VM 2\nzona 2 · IP pública")], cols=1)
fws = Z(1350, 1108, 260, 180, "AzureFirewallSubnet", "subnet")
afw, afp = F(fws, [("firewall", "Azure Firewall Premium\n3 zonas · IDPS · DNS proxy"), ("fwpolicy", "Firewall\nPolicy")])
dni = Z(1350, 1300, 127, 130, "DNS entrada", "subnet")
dres, = F(dni, [("dnsresolver", "Private\nResolver")], size=40)
dno = Z(1483, 1300, 127, 130, "DNS salida", "subnet")
dres2, = F(dno, [("dnsresolver", "Private\nResolver")], size=40)
hx = Z(1350, 1442, 260, 268, "Servicios del hub", "subnet")
ddos, nat, pdns, conn = F(hx, [("ddos", "DDoS Network\nProtection"), ("nat", "NAT Gateway\n(egreso)"),
                               ("dns", "Zonas DNS privadas\npor ámbito"), ("vm", "Conector de red\nprivada (Entra)")],
                          cols=2, size=40)


def spoke(y, h, title, apim_label, aks_lbl, data, kind="vnet", extra=None):
    sp = Z(1730, y, 1010, h, title, kind, align="left")
    out = {"vnet": sp}
    if apim_label:
        sh = (h - 70) / 2
        out["appgw"], = F(Z(1750, y + 40, 190, sh, "Subred App Gateway", "subnet"),
                          [("appgw", "Application Gateway\n(privado)")])
        out["apim"], = F(Z(1750, y + 50 + sh, 190, sh, "Subred APIM", "subnet"), [("apim", apim_label)])
    ax = 1960 if apim_label else 1750
    aw = 430 if apim_label else 640
    az = Z(ax, y + 40, aw, h - 60, "Subred AKS", "subnet")
    aks = Z(ax + 15, y + 80, aw - 30, h - 115, aks_lbl, "inner")
    out["aks"] = aks
    out["pools"] = F(aks, [("aks", "Pool de sistema\n×3 zonas"), ("aks", "Pool de usuario\n×3 zonas"),
                           ("lb", "Ingress\n(balanceador interno)")] + (extra or []), size=44, top=40)
    dz = Z(2410, y + 40, 310, h - 60, "Subred de datos (puntos privados)", "subnet")
    out["data"] = F(dz, data, cols=2, size=42, top=36)
    out["dz"] = dz
    return out


ret = spoke(340, 440, "Spoke Retail", "API Management\nPremium (3 zonas)", "AKS Retail", [
    ("postgres", "PostgreSQL z1\nprimario :5432"), ("postgres", "PostgreSQL z2\nen espera"),
    ("eventhubs", "Event Hubs\nPremium :9093"), ("mredis", "Azure Managed\nRedis"),
    ("datalake", "ADLS Gen2\n:443"), ("keyvault", "Key Vault\n:443")])
com = spoke(810, 400, "Spoke Compartida (integración y operación)", None,
            "AKS de plataforma: X-01, adaptadores y programador", [
                ("acr", "Container Registry\nPremium :443"), ("keyvault", "Key Vault\n:443"),
                ("devpools", "Agentes CI/CD\n(DevOps Pools)")],
            extra=None)
emi = spoke(1240, 480, "Spoke Emisor (suscripción, red y claves propias)", "API Management\nPremium (3 zonas)",
            "AKS Emisor", [
                ("postgres", "PostgreSQL z1\nprimario :5432"), ("postgres", "PostgreSQL z2\nen espera"),
                ("eventhubs", "Event Hubs\nPremium :9093"), ("datalake", "ADLS Gen2\n:443"),
                ("storage", "Storage inmutable\nWORM :443"), ("hsm", "Managed HSM\n:443")])

# ============ D. Azure Brazil South (activo-pasivo) ============
Z(2800, 290, 480, 1460, "Azure Brazil South (CLD-02)  ·  recuperación", "region", align="left")
dhub = Z(2830, 340, 420, 230, "Hub (espejo por IaC)", "vnet")
d_fw, d_vpn, d_fv = F(dhub, [("firewall", "Azure Firewall"), ("vpngw", "VPN GW"), ("fw_site", "FortiGate-VM\n(SD-WAN, por IaC)")])
dret = Z(2830, 600, 420, 430, "Spoke Retail (pasivo)", "vnet")
d_r = F(dret, [("apim", "Gateway regional\nde APIM"), ("aks", "AKS por IaC\n(en espera)"),
               ("eventhubs", "Event Hubs\n(geo-réplica)"), ("postgres", "PostgreSQL\n(réplica asíncrona)"),
               ("storage", "Storage\n(replicado)"), ("keyvault", "Key Vault")], cols=2, size=42)
demi = Z(2830, 1060, 420, 430, "Spoke Emisor (condicionado a residencia)", "vnet_cond")
d_e = F(demi, [("apim", "Gateway regional\nde APIM"), ("aks", "AKS por IaC\n(en espera)"),
               ("eventhubs", "Event Hubs\n(geo-réplica)"), ("postgres", "PostgreSQL\n(réplica asíncrona)"),
               ("storage", "Storage\n(replicado)"), ("hsm", "Managed HSM\n(réplica)")], cols=2, size=42)
dcom = Z(2830, 1520, 420, 200, "Compartida", "vnet")
d_acr, d_bk = F(dcom, [("acr", "ACR geo-réplica"), ("backup", "Backup Vault\n(copia entre regiones)")])

# ============ C5. Bandas transversales ============
Z(1010, 1790, 2270, 230, "Servicios transversales (por ámbito y ambiente)", "band")
bands = [
    ("Identidad", [("entra", "Entra ID\n(federado)"), ("pim", "PIM"), ("condaccess", "Acceso\ncondicional")]),
    ("Seguridad", [("sentinel", "Sentinel\n(SIEM)"), ("defender", "Defender for Cloud\ny Servers (EDR)")]),
    ("Observabilidad", [("monitor", "Azure\nMonitor"), ("loganalytics", "Log Analytics\n(por ámbito)"), ("arc", "Azure Arc\n(on-prem)")]),
    ("Gobierno", [("policy", "Azure\nPolicy"), ("cost", "Costos\ny etiquetas")]),
    ("Respaldo", [("backup", "Backup Vault\ninmutable"), ("rguard", "Resource Guard\n(aprobación doble)")]),
    ("Entrega", [("devops", "Repos y\nPipelines")]),
    ("Analítica", [("powerbi", "Power BI\npor ámbito")]),
]
bx = 1025
widths = [390, 300, 390, 270, 300, 190, 190]
bid = {}
for (title, items), w in zip(bands, widths):
    zid = Z(bx, 1830, w - 10, 180, title, "subnet")
    bid[title] = F(zid, items, size=40, top=32)
    bx += w + 10

# ============ Aristas ============
def cx(cid):
    import re
    m = re.search(r'id="%s"[^>]*><mxGeometry x="([\d.]+)" y="[\d.]+" width="([\d.]+)"' % cid, "".join(d.cells))
    return float(m.group(1)) + float(m.group(2)) / 2


def gy(cid, frac):
    import re
    m = re.search(r'id="%s"[^>]*><mxGeometry x="[\d.]+" y="([\d.]+)" width="[\d.]+" height="([\d.]+)"' % cid, "".join(d.cells))
    return float(m.group(1)) + float(m.group(2)) * frac


CLIX, CPTX, REMX, AFDX, ZTAX = cx(cli), cx(cpt), cx(rem), cx(afd), cx(zta)
CD1X, CD2X, VPNX = cx(cd1_fw), cx(cd2_fw), cx(vpngw)


def rx(zid, fr):  # x a una fracción del ancho de una zona
    r = d.rects[zid]
    return r[0] + r[2] * fr


def yf(zid, fr):  # y a una fracción del alto de una zona
    r = d.rects[zid]
    return r[1] + r[3] * fr


# Exterior -> borde global -> spokes
d.edge(cli, afd, "HTTPS :443", exit=(0.5, 0), entry=(0.5, 0), points=[(CLIX, 54), (AFDX, 54)])
d.edge(cpt, afd, "", exit=(0.5, 0), entry=(0.5, 0), points=[(CPTX, 54), (AFDX, 54)])
d.edge(afd, ret["appgw"], "Private Link :443", exit=(0.5, 1), entry=(0, 0.5),
       points=[(AFDX, 330), (1740, 330), (1740, gy(ret["appgw"], 0.5))])
d.edge(afd, emi["appgw"], "Private Link :443", exit=(1, 0.5), entry=(0, 0.5), label_pos=0.55,
       points=[(2780, 116), (2780, 1233), (1740, 1233), (1740, gy(emi["appgw"], 0.5))])
d.edge(rem, zta, "", line="dashed", exit=(0.5, 1), entry=(0.5, 1), points=[(REMX, 238), (ZTAX, 238)])
d.edge(zta, bst, "acceso administrativo", line="dashed", exit=(1, 0.5), entry=(1, 0.5),
       points=[(ZTAX + 95, gy(zta, 0.5)), (ZTAX + 95, 268), (1700, 268), (1700, gy(bst, 0.5))])

# Tienda -> WAN -> hub
d.edge(ha, st, "cada FortiGate a ambos switches", both=True, exit=(0.5, 1), entry=(0.5, 0))
d.edge(fg1, fg2, "HA", line="dotted", both=True, exit=(1, 0.5), entry=(0, 0.5))
d.edge(n1, st, "", exit=(0.5, 0), entry=((cx(n1) - 675) / 270, 1))
d.edge(st, vl, "troncal 802.1Q", exit=(0, 0.5), entry=(1, 0.5))
d.edge(ha, inet, "Enlace principal", exit=(1, 0.3), entry=(0, 0.5), points=[(995, gy(ha, 0.3)), (995, 565)])
d.edge(ha, lte, "Respaldo LTE/5G", line="dashed", exit=(1, 0.8), entry=(0, 0.5), points=[(1012, gy(ha, 0.8)), (1012, 855)])
d.edge(cd1_fw, inet, "2 proveedores", exit=(0.5, 0), entry=(0, 0.7), points=[(CD1X, 1028), (990, 1028), (990, 590)])
d.edge(cd2_fw, lte, "", line="dashed", exit=(0.5, 0), entry=(0, 0.7), points=[(CD2X, 1042), (1005, 1042), (1005, 865)])
d.edge(inet, fv1, "SD-WAN IPsec", exit=(1, 0.4), entry=(0, 0.5))
d.edge(inet, fv2, "", exit=(1, 0.6), entry=(0, 0.5))
d.edge(lte, fv1, "", line="dashed", exit=(1, 0.4), entry=(0, 0.3))
d.edge(lte, fv2, "", line="dashed", exit=(1, 0.6), entry=(0, 0.7))

# DC-01 -> dos circuitos ExpressRoute (proveedores distintos) / VPN de respaldo
d.edge(dha, erc1, "", line="dashed", exit=(0.25, 0), entry=(0, 0.5), points=[(105, 1404), (990, 1404), (990, gy(erc1, 0.5))])
d.edge(dha, erc2, "", line="dashed", exit=(0.5, 0), entry=(0, 0.5), points=[(155, 1412), (1000, 1412), (1000, gy(erc2, 0.5))])
d.edge(dha, csw1, "", both=True, exit=(0.5, 1), entry=(0.5, 0)) if False else None
ERY = gy(ergw, 0.5)
d.edge(erc1, ergw, "ExpressRoute (propuesto)", line="dashed", exit=(1, 0.5), entry=(0, 0.5),
       points=[(1316, gy(erc1, 0.5)), (1316, ERY)])
d.edge(erc2, ergw, "", line="dashed", exit=(1, 0.5), entry=(0, 0.5), points=[(1316, gy(erc2, 0.5)), (1316, ERY)])
d.edge(dha, vpngw, "VPN de respaldo", line="dotted", exit=(0.75, 0), entry=(0.5, 0),
       points=[(205, 1420), (1290, 1420), (1290, 318), (VPNX, 318)])
d.edge(dha, dco, "cada FortiGate a ambos switches", both=True, exit=(0.5, 1), entry=(0.5, 0))
d.edge(rs, dc2z, "enlace propuesto", line="dashed", exit=(1, 0.3), entry=(0, 0.3), both=True)

# Hub interno: Route Server (BGP) y UDR hacia el Firewall; peering a los spokes
d.edge(rss, sdw, "BGP", line="dotted", exit=(0.5, 1), entry=(0.5, 0))
d.edge(sdw, fws, "UDR", exit=(0.5, 1), entry=(0.5, 0))
for sp, yy in ((ret, 560), (com, 1010), (emi, 1480)):
    d.edge(hub, sp["vnet"], "peering" if sp is ret else "", line="dotted", both=True,
           exit=(1, round((yy - 340) / 1380, 3)), entry=(0, 0.5))

# Único cruce Retail -> X-01 -> Emisor: siempre por Azure Firewall (sin peering directo)
RA, CA, EA = ret["aks"], com["aks"], emi["aks"]
d.edge(RA, fws, "cruce X-01 por Azure Firewall", color=ACCENT, width=2.2, exit=(0.7, 1), entry=(1, 0.2),
       points=[(rx(RA, 0.7), 788), (1650, 788), (1650, yf(fws, 0.2))])
d.edge(fws, CA, "", color=ACCENT, width=2.2, exit=(1, 0.4), entry=(0.9, 0),
       points=[(1660, yf(fws, 0.4)), (1660, 800), (rx(CA, 0.9), 800)])
d.edge(CA, fws, "", color=ACCENT, width=2.2, exit=(0.7, 1), entry=(1, 0.6),
       points=[(rx(CA, 0.7), 1214), (1670, 1214), (1670, yf(fws, 0.6))])
d.edge(fws, EA, "", color=ACCENT, width=2.2, exit=(1, 0.8), entry=(0.9, 0),
       points=[(1680, yf(fws, 0.8)), (1680, 1224), (rx(EA, 0.9), 1224)])

# AKS -> datos (los puertos van en el rótulo de cada servicio)
d.edge(ret["aks"], ret["dz"], "", exit=(1, 0.5), entry=(0, 0.5))
d.edge(emi["aks"], emi["dz"], "", exit=(1, 0.5), entry=(0, 0.5))
d.edge(com["aks"], com["dz"], "", exit=(1, 0.5), entry=(0, 0.5))
for sp in (ret, emi):
    d.edge(sp["appgw"], sp["apim"], "", exit=(1, 0.5), entry=(1, 0.5),
           points=[(1915, gy(sp["appgw"], 0.5)), (1915, gy(sp["apim"], 0.5))])
    d.edge(sp["apim"], sp["aks"], "", exit=(1, 0.8), entry=(0, 0.5))

# Recuperación
d.edge(ret["dz"], dret, "geo-réplica y réplica asíncrona\n(RPO ≤ 15 min)", line="dashed",
       exit=(1, 0.5), entry=(0, 0.3))
d.edge(emi["dz"], demi, "condicionada", line="dashed", exit=(1, 0.5), entry=(0, 0.5))

# Marcadores: recorrido de una venta en línea (1-4) y en tienda (5-6)
d.marker(CLIX - 50, 70, 1)
d.marker(1738, 600, 2)
d.marker(1972, 735, 3)
d.marker(2420, 735, 4)
d.marker(670, 770, 5)
d.marker(1060, 500, 6)

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
