"""Arquitectura física completa: sitios del Cliente, servicios globales, CLD-01 y CLD-02.

Responde: ¿dónde corre cada componente, por qué red pasa cada flujo y cómo se recupera?
Reúne en una vista lo que las Figuras 4.13 a 4.20 muestran por separado. Solo incluye lo que
declaran SD-04 (4.1.1, 4.2, 4.3) y el Formulario T-11 (Tabla T-11.2).
Cada sitio queda a la altura de la subred del hub en que termina su conexión, y las rutas
largas usan pasillos libres (x = 495, 905, 918, 2108; y = 8, 225, 1430, 1442).
Ejecutar: python3 04_Adjuntos/diagramas/diag-04-21_arquitectura-fisica-completa.py
"""

from pathlib import Path

from _drawio import ACCENT, Diagram

d = Diagram(font=22, zone_font=24)
Z, F = d.zone, d.fill
W = 2.5

# ================= exterior =================
ext = Z(20, 20, 470, 300, "Internet y contrapartes", "plain")
cli, ext01, adm = F(ext, [("users", "Clientes"), ("globe", "EXT-01\ncontrapartes"),
                          ("users", "Administradores")], size=62, top=60)

# ================= servicios globales =================
Z(520, 20, 2260, 190, "Servicios globales de Azure", "plain", align="left")
afd = d.icon(600, 75, "frontdoor", "Front Door Premium + WAF (Private Link a cada ámbito desde Brazil South)", size=62, label_pos="right")
ent = d.icon(1600, 75, "entra", "Entra ID P2 (federado con el directorio del Cliente)", size=62, label_pos="right")
d.icon(2400, 75, "dns", "DNS público", size=62, label_pos="right")

# ================= sitios del Cliente (alineados con el hub) =================
Z(20, 350, 470, 1070, "Sitios del Cliente", "onprem")
sit = Z(35, 405, 440, 300, "SIT-01 · 22 tiendas · 10.100.0.0/16\nenlace ≥ 10 Mbps + respaldo ≥ 5 Mbps", "band")
tda, nodo, fgt = F(sit, [("building", "Tienda tipo\n(6 VLAN)"), ("srv", "Nodo local\n(2 servidores)"),
                         ("fw_site", "Par FortiGate\nSD-WAN")], size=56, top=85)
cds = Z(35, 720, 440, 230, "Centros de distribución\n(2 Mbps reservados)", "band")
cd1, cd2 = F(cds, [("building", "CD-01\n(2 enlaces)"), ("building", "CD-02\n(1 enlace)")], size=52, top=80)
dc1 = Z(35, 965, 440, 285, "DC-01 · casa matriz (140 m²)\nExpressRoute 200 Mbps propuesto", "band")
plat, cinta, fdc = F(dc1, [("server", "ERP/DTE, núcleo\n2009, crédito 2011"), ("san", "Cinta en\ncustodia"),
                           ("fw_site", "Par\nFortiGate")], size=52, top=85)
dc2z = Z(35, 1265, 440, 145, "DC-02 · misma comuna", "band")
dc2, = F(dc2z, [("server", "Sala de respaldo")], size=44, top=42)

# ================= CLD-01 =================
Z(520, 240, 1580, 1180, "CLD-01 · Azure Chile Central · 3 zonas · 10.10.0.0/16", "region", align="left")
hub = Z(540, 300, 352, 1100, "Hub · 10.10.0.0/22\nsuscripción Conectividad", "vnet")
F(Z(552, 372, 328, 110, "", "plain"), [("dns", "DNS\nprivado"), ("nat", "NAT"), ("ddos", "DDoS")], size=36, top=4)
SUBS = [("SD-WAN .1.0/26", [("fw_site", "FortiGate\nVM Z1"), ("fw_site", "FortiGate\nVM Z2")]),
        ("AzureFirewallSubnet .0.128/26", [("firewall", "Firewall Premium\nZ1 · Z2 · Z3")]),
        ("RouteServerSubnet .0.64/26", [("router", "Route Server")]),
        ("AzureBastionSubnet .0.192/26", [("bastion", "Bastion (Entra\nPrivate Access)")]),
        ("GatewaySubnet .0.0/26", [("vpngw", "ExpressRoute"), ("vpngw", "VPN")])]
hubids = []
for k, (t, items) in enumerate(SUBS):
    sz = Z(552, 495 + k * 152, 328, 140, t, "subnet")
    hubids.append(F(sz, items, size=44, top=38))
(fv1, fv2), (afw,), (rsv,), (bst,), (ergw, vpngw) = hubids


def spoke(y, h, title, cols):
    z = Z(930, y, 1150, h, title, "vnet", align="left")
    subs, icons, x = [], [], 942
    for (st, w, items, ncol) in cols:
        sz = Z(x, y + 62, w, h - 80, st, "subnet")
        subs.append(sz)
        icons.append(F(sz, items, cols=ncol, size=46, top=58))
        x += w + 8
    return z, subs, icons


ret, r_sub, ((r_ag,), (r_apim,), (r_aks, r_ml), r_dat) = spoke(300, 400, "Ámbito Retail · 10.10.16.0/20 · suscripción Retail-Producción", [
    ("Entrada .16.0/24", 200, [("appgw", "App\nGateway")], 1),
    ("APIM .17.0/28", 200, [("apim", "API Mgmt\n3 unid. Z1-3")], 1),
    ("Aplicación .20.0/22", 270, [("aks", "AKS\nZ1-3"), ("aks", "Nodos\npredictivos")], 2),
    ("Datos .24.0/24 · puntos privados", 432, [("postgres", "PostgreSQL\nZ1 + Z2"), ("mredis", "Managed\nRedis"),
                                                ("eventhubs", "Event Hubs\nPremium"), ("datalake", "Data Lake\nGen2"),
                                                ("keyvault", "Key Vault"), ("powerbi", "Power BI")], 3)])
emi, e_sub, ((e_ag,), (e_apim,), (e_aks,), e_dat) = spoke(715, 400, "Ámbito Emisor · 10.10.32.0/20 · suscripción Emisor-Producción", [
    ("Entrada .32.0/24", 200, [("appgw", "App\nGateway")], 1),
    ("APIM .33.0/28", 200, [("apim", "API Mgmt\n3 unid. Z1-3")], 1),
    ("Aplicación .36.0/22", 270, [("aks", "AKS\nZ1-3")], 1),
    ("Datos .40.0/24 · puntos privados", 432, [("postgres", "PostgreSQL\nZ1 + Z2"), ("eventhubs", "Event Hubs\nPremium"),
                                                ("datalake", "Data Lake\nGen2"), ("storage", "Blob\ninmutable"),
                                                ("keyvault", "Key Vault"), ("hsm", "Managed\nHSM")], 3)])
bas, b_sub, ((x01,), (age,), (acr,)) = spoke(1130, 270, "Base tecnológica · 10.10.48.0/21 · suscripción Base-Producción", [
    ("Aplicación .48.0/22", 380, [("aks", "X-01 y adaptadores\n(único cruce Retail–Emisor)")], 1),
    ("Agentes .52.0/24", 340, [("devpools", "Agentes CI/CD")], 1),
    ("Registro .53.0/24", 390, [("acr", "Container Registry\n(réplica a CLD-02)")], 1)])

# ================= CLD-02 =================
Z(2120, 240, 660, 1180, "CLD-02 · Azure Brazil South\nactivo-pasivo · 10.20.0.0/16", "region", align="left")
rdr = Z(2140, 335, 620, 380, "Retail · Recuperación\nréplica PostgreSQL asíncrona\nEvent Hubs geo-réplica < 15 min", "vnet")
b_ag, b_apim, b_aks, b_pg, b_eh, b_kv = F(rdr, [("appgw", "App\nGateway"), ("apim", "Gateway\nAPIM"),
                                                 ("aks", "AKS\n(por IaC)"), ("postgres", "PostgreSQL\nréplica"),
                                                 ("eventhubs", "Event Hubs\nréplica"), ("keyvault", "Key Vault\npropio")],
                                          cols=3, size=44, top=110)
edr = Z(2140, 735, 620, 340, "Emisor · Recuperación\nsolo si el Cliente aprueba\nla residencia de sus datos", "vnet_cond")
F(edr, [("postgres", "PostgreSQL\nréplica"), ("storage", "Copia del Blob\ninmutable")], size=44, top=120)
hb2 = Z(2140, 1095, 620, 310, "Hub en espejo (Conectividad)", "vnet")
b_fw, b_fgt, b_vpn, b_rs, b_bst = F(hb2, [("firewall", "Firewall\nPremium"), ("fw_site", "FortiGate\nVM ×2"),
                                          ("vpngw", "VPN"), ("router", "Route\nServer"), ("bastion", "Bastion")],
                                    cols=3, size=44, top=48)

# ================= operación y gobierno =================
ops = Z(20, 1462, 2760, 200, "Operación, seguridad y gobierno · suscripción Gestión y un área de trabajo por ámbito", "band", align="left")
F(ops, [("monitor", "Azure Monitor\n+ OpenTelemetry"), ("loganalytics", "Log Analytics\n(por ámbito)"),
        ("sentinel", "Sentinel"), ("defender", "Defender\nfor Cloud"), ("policy", "Azure Policy\n(nombres y etiquetas)"),
        ("arc", "Azure Arc"), ("cost", "Gestión de\ncostos"), ("backup", "Backup Vault\nCLD-01 y CLD-02"),
        ("devops", "Azure Pipelines"), ("repo", "Terraform\n(repositorio)")], size=50, top=50)

# ================= flujos =================
import re


def pos(cid):
    """(x, y, tamaño) real de un ícono, leído de la celda ya generada."""
    for c in d.cells:
        if f'id="{cid}"' in c:
            x, y, w = re.search(r'x="([\d.]+)" y="([\d.]+)" width="([\d.]+)"', c).groups()
            return float(x), float(y), float(w)


def cx(cid):
    x, y, w = pos(cid); return x + w / 2


def cy(cid):
    x, y, w = pos(cid); return y + w / 2


# entrada pública
d.edge(ext, afd, "HTTPS", width=W, exit=(1, 0.27), entry=(0, 0.5))
for dst in (r_ag, e_ag):
    d.edge(afd, dst, "", width=W, exit=(0.5, 1), entry=(0, 0.5),
           points=[(cx(afd), 225), (905, 225), (905, cy(dst))])
d.edge(afd, b_ag, "origen secundario", line="dashed", width=W, exit=(0.5, 0), entry=(0, 0.5),
       points=[(cx(afd), 8), (2108, 8), (2108, cy(b_ag))], label_pos=0.3)
# sitios
d.edge(fgt, fv1, "", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(cds, fv2, "", width=W, exit=(1, 0.5), entry=(0.5, 1), points=[(500, 835), (500, 655), (cx(fv2), 655)])
d.edge(fdc, ergw, "", line="dashed", width=W, exit=(1, 0.4), entry=(0, 0.5),
       points=[(505, cy(fdc) - 5), (505, cy(ergw))])
d.edge(fdc, vpngw, "", line="dashed", width=W, exit=(1, 0.8), entry=(0.5, 1),
       points=[(513, pos(fdc)[1] + 42), (513, 1257), (cx(vpngw), 1257)])
d.edge(plat, dc2, "propuesto", line="dashed", width=W, exit=(0.5, 1), entry=(0.5, 0))
d.edge(adm, bst, "", line="dashed", width=W, exit=(0.5, 1), entry=(0, 0.5),
       points=[(cx(adm), 336), (495, 336), (495, cy(bst))])
d.edge(dc1, b_vpn, "VPN de DC-01 a CLD-02", line="dashed", width=W, exit=(1, 0.97), entry=(0.7, 1),
       points=[(500, 1442), (cx(b_vpn) + 9, 1442)], label_pos=0.15)
d.edge(vpngw, b_vpn, "VPN entre hubs", line="dashed", width=W, exit=(0.7, 1), entry=(0.3, 1),
       points=[(cx(vpngw) + 9, 1430), (cx(b_vpn) - 9, 1430)], label_pos=-0.3)
# único cruce Retail–Emisor (por Azure Firewall)
d.edge(r_sub[2], x01, "", color=ACCENT, width=4, exit=(0.3, 1), entry=(0, 0.5),
       points=[(r_sub_x := 942 + 200 + 8 + 200 + 8 + 270 * 0.3, 690), (918, 690), (918, cy(x01))])
d.edge(x01, e_sub[2], "", color=ACCENT, width=4, exit=(0.5, 0), entry=(0.5, 1),
       points=[(cx(x01), 1122), (942 + 200 + 8 + 200 + 8 + 135, 1122)])
# recuperación
d.edge(r_sub[3], rdr, "", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(e_sub[3], edr, "", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5))

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
