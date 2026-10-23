"""Vista física 1 de 3: anillos de red, frontera de alcance, capacidad y puertos.

Responde: ¿por qué zonas pasa una petición, dónde corre cada componente, cuánto aguanta y qué es de quién?
Sigue FEP01 (diap. 80, 81 y 93): zonas de red como anillos de izquierda a derecha, nodos con capacidad,
puertos en las líneas, función y producto, redundancia y tres colores de alcance con leyenda.
Fuentes: SD-04 (4.2, 4.3, Tablas 4.10, 4.13 y 4.14), Formulario T-11 y la memoria
04_Adjuntos/tablas/sd-04_s2_dimensionamiento-nodos.md.
Ejecutar: python3 04_Adjuntos/diagramas/diag-04-21_fisica-1-vista-general.py
"""

import re
from pathlib import Path

from _alcance import czone, legend, ring
from _drawio import ACCENT, Diagram

d = Diagram(font=22, zone_font=24)
W = 2.5
S = 56  # tamaño de ícono


def ic(x, y, name, label, **kw):
    return d.icon(x, y, name, label, size=kw.pop("size", S), **kw)


def pos(cid):
    for c in d.cells:
        if f'id="{cid}"' in c:
            x, y, w = re.search(r'x="([\d.]+)" y="([\d.]+)" width="([\d.]+)"', c).groups()
            return float(x), float(y), float(w)


def cx(c):
    x, y, w = pos(c); return x + w / 2


def cy(c):
    x, y, w = pos(c); return y + w / 2


# ================= Internet (terceros) =================
czone(d, 20, 240, 260, 760, "Internet", "tercero")
cli = ic(122, 320, "users", "Clientes")
ext = ic(122, 520, "globe", "Contrapartes\n(EXT-01)")
adm = ic(122, 760, "users", "Administradores")

# ================= Perímetro (global) =================
czone(d, 300, 240, 260, 760, "Zona pública\n(perímetro global)", "oss")
dns = ic(402, 330, "dns", "DNS público")
afd = ic(402, 530, "frontdoor", "Front Door Premium\n(CDN + WAF)")
ddo = ic(402, 790, "ddos", "Anti-DDoS")

# ================= CLD-01 =================
czone(d, 580, 240, 1560, 1060, "CLD-01 · Chile Central · 3 zonas", "oss", align="left")
ring(d, 600, 300, 420, 990, "DMZ · entrada y API")
ring(d, 1040, 300, 300, 990, "Subred privada\nde aplicación")
r_datos = ring(d, 1360, 300, 440, 990, "Subred privada de datos")
ring(d, 1820, 300, 300, 990, "Hub · conexión y gestión")
for yy in (690, 1030):
    d.cells.append(f'<mxCell id="{d._id("l")}" style="endArrow=none;html=1;strokeColor=#B0B0B0;strokeWidth=1.5;" edge="1" parent="1">'
                   f'<mxGeometry relative="1" as="geometry"><mxPoint x="600" y="{yy}" as="sourcePoint"/>'
                   f'<mxPoint x="1800" y="{yy}" as="targetPoint"/></mxGeometry></mxCell>')
for (yy, t) in ((372, "Retail"), (700, "Emisor"), (1040, "Base tecnológica")):
    d.text(610, yy, 400, 30, t, size=21, bold=True, align="left", color="#0078D4")

# Retail
r_ag = ic(645, 430, "appgw", "App Gateway v2\n2 a 10 inst.")
r_ap = ic(845, 430, "apim", "API Management\n3 unidades")
r_ak = ic(1162, 430, "aks", "AKS\n6 × D8ds_v5\n+ 3 × D4ds_v5")
r_pg = ic(1395, 400, "postgres", "PostgreSQL\nD8ds_v5 · 2 TiB")
r_rd = ic(1665, 400, "mredis", "Redis\nB5 · 6 GB")
r_eh = ic(1395, 560, "eventhubs", "Event Hubs\n2 PU")
r_dl = ic(1665, 560, "datalake", "Data Lake\n1 TB")
# Emisor
e_ag = ic(645, 760, "appgw", "App Gateway v2")
e_ap = ic(845, 760, "apim", "API Management\n3 unidades")
e_ak = ic(1162, 760, "aks", "AKS\n3 × D4ds_v5\n+ 3 × D4ds_v5")
e_pg = ic(1395, 740, "postgres", "PostgreSQL\nD4ds_v5 · 512 GiB")
e_eh = ic(1665, 740, "eventhubs", "Event Hubs\n1 PU")
e_bl = ic(1395, 900, "storage", "Blob inmutable\n9 TB")
e_hs = ic(1665, 900, "hsm", "Managed HSM")
# Base tecnológica
b_ak = ic(1162, 1100, "aks", "X-01 y adaptadores\nAKS 3 × D8ds_v5")
b_pg = ic(1395, 1090, "postgres", "PostgreSQL\nD2ds_v5 · 128 GiB")
b_cr = ic(1665, 1090, "acr", "Container Registry\nPremium")
# Hub
d.text(1830, 345, 280, 60, "Todo cruce pasa\npor el Firewall", size=19, align="center", color="#505050")
fw = ic(1942, 430, "firewall", "Azure Firewall\nPremium · Z1-3")
fg = ic(1942, 640, "fw_site", "FortiGate-VM\n2 × F4s_v2")
gw = ic(1942, 860, "vpngw", "ExpressRoute\n+ VPN")
bs = ic(1870, 1110, "bastion", "Bastion", label_pos="right")

# ================= Sitios del Cliente =================
czone(d, 2170, 240, 300, 1060, "Sitios del Cliente", "cliente")
st = ic(2292, 560, "building", "22 tiendas\n2 nodos c/u\n≥ 10 Mbps")
cd = ic(2292, 780, "building", "CD-01 y CD-02\n2 Mbps")
dc = ic(2292, 940, "server", "DC-01\nplataformas\nactuales")
d2 = ic(2292, 1150, "server", "DC-02\nrespaldo")

# ================= Identidad, secretos y observabilidad =================
czone(d, 20, 1030, 540, 270, "Identidad, secretos y observabilidad", "oss")
for k, (n, t) in enumerate([("entra", "Entra ID"), ("keyvault", "Key Vault"),
                            ("monitor", "Monitor"), ("sentinel", "Sentinel")]):
    ic(50 + k * 130, 1085, n, t, size=48)

# ================= CLD-02 =================
czone(d, 580, 1340, 1560, 190, "CLD-02 · Brazil South · recuperación", "oss", align="left")
dr = [("appgw", "App Gateway"), ("apim", "API Mgmt\n1 unidad"), ("aks", "AKS\n(0 nodos)"),
      ("postgres", "PostgreSQL\nréplica"), ("eventhubs", "Event Hubs\nréplica"),
      ("keyvault", "Key Vault"), ("backup", "Respaldo"), ("firewall", "Hub espejo")]
drids = [ic(660 + k * 190, 1420, n, t, size=46) for k, (n, t) in enumerate(dr)]

# ================= Leyenda =================
legend(d, 20, 1330, 540, extra=[("solid", "#1F1F1F", 2.5, "Flujo con puerto"),
                                ("dashed", "#1F1F1F", 2.5, "Propuesto o réplica"),
                                ("solid", ACCENT, 4, "Cruce Retail–Emisor")])

# ================= Flujos con protocolo y puerto =================
d.edge(cli, afd, "443", width=W, exit=(1, 0.5), entry=(0, 0.3))
d.edge(ext, afd, "443", width=W, exit=(1, 0.5), entry=(0, 0.6))
d.edge(afd, r_ag, "443", width=W, exit=(1, 0.3), entry=(0, 0.5), points=[(590, cy(afd) - 11), (590, cy(r_ag))], label_pos=-0.8)
d.edge(afd, e_ag, "", width=W, exit=(1, 0.7), entry=(0, 0.5), points=[(590, cy(afd) + 11), (590, cy(e_ag))])
d.edge(r_ag, r_ap, "443", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(e_ag, e_ap, "443", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(r_ap, r_ak, "443", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(e_ap, e_ak, "443", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(r_ak, r_pg, "5432", width=W, exit=(1, 0.3), entry=(0, 0.5), points=[(1280, pos(r_ak)[1] + 17), (1280, cy(r_pg))], label_pos=0.75)
d.edge(r_ak, r_rd, "10000", width=W, exit=(0.5, 0), entry=(0.5, 0), points=[(cx(r_ak), 382), (cx(r_rd), 382)], label_pos=0.4)
d.edge(r_ak, r_eh, "9093", width=W, exit=(1, 0.8), entry=(0, 0.5), points=[(1300, pos(r_ak)[1] + 45), (1300, cy(r_eh))], label_pos=0.75)
d.edge(e_ak, e_pg, "5432", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(b_ak, b_pg, "5432", width=W, exit=(1, 0.5), entry=(0, 0.5))
# único cruce
d.edge(r_ak, b_ak, "", color=ACCENT, width=4, exit=(0, 0.8), entry=(0, 0.3),
       points=[(1062, pos(r_ak)[1] + 45), (1062, pos(b_ak)[1] + 17)])
d.text(615, 1120, 400, 80, "Único cruce\nRetail–Emisor (X-01)", size=21, bold=True, color=ACCENT)
d.edge(b_ak, e_ak, "", color=ACCENT, width=4, exit=(0, 0.7), entry=(0, 0.85), points=[(1050, pos(b_ak)[1] + 39), (1050, pos(e_ak)[1] + 48)])
# sitios y administración
d.edge(st, fg, "IPsec", width=W, exit=(0, 0.5), entry=(1, 0.5), points=[(2150, cy(st)), (2150, cy(fg))])
d.edge(cd, fg, "IPsec", width=W, exit=(0, 0.5), entry=(1, 0.8), points=[(2160, cy(cd)), (2160, cy(fg) + 11)], label_pos=-0.3)
d.edge(dc, gw, "200 Mbps", line="dashed", width=W, exit=(0, 0.5), entry=(1, 0.5), label_pos=-0.45)
d.edge(adm, bs, "", line="dashed", width=W, exit=(0.5, 1), entry=(0.5, 1),
       points=[(cx(adm), 1012), (575, 1012), (575, 1315), (cx(bs), 1315)], label_pos=0.55)
d.edge(dc, d2, "", line="dashed", width=W, exit=(1, 0.5), entry=(1, 0.5), points=[(2450, cy(dc)), (2450, cy(d2))])
# recuperación
d.edge(r_datos, drids[3], "", line="dashed", width=W, exit=(0.5, 1), entry=(0.5, 0),
       points=[(1580, 1318), (cx(drids[3]), 1318)])

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
