"""Vista física 3 de 3: sitios del Cliente, enlaces y recuperación entre regiones.

Responde: ¿con qué equipos y enlaces llega cada sitio a la nube, y cómo se separan replicación y respaldo?
Sigue FEP01 (diap. 93, 105 a 117 y 159): capacidad de cada equipo, RAID por volumen, tipo de enlace con
ancho de banda, tres colores de alcance y replicación declarada aparte del respaldo.
Fuentes: SD-04 (4.2, 4.2.1, 4.3.1, 4.3.2, Tablas 4.13 a 4.15), Formulario T-11 (Tablas T-11.5 y T-11.6)
y la memoria 04_Adjuntos/tablas/sd-04_s2_dimensionamiento-nodos.md.
Ejecutar: python3 04_Adjuntos/diagramas/diag-04-21_fisica-3-sitios-y-recuperacion.py
"""

import re
from pathlib import Path

from _alcance import czone, legend
from _drawio import ACCENT, Diagram

d = Diagram(font=21, zone_font=24)
W = 2.5


def ic(x, y, name, label, size=50, pos="right"):
    return d.icon(x, y, name, label, size=size, label_pos=pos)


def P(cid):
    for c in d.cells:
        if f'id="{cid}"' in c:
            x, y, w = re.search(r'x="([\d.]+)" y="([\d.]+)" width="([\d.]+)"', c).groups()
            return float(x), float(y), float(w)


def cy(c):
    x, y, w = P(c); return y + w / 2


# ================= sitios del Cliente =================
czone(d, 20, 20, 760, 600, "SIT-01 · tienda tipo (× 22)", "cliente", align="left")
t_nodo = ic(45, 85, "srv", "2 nodos locales, activo-pasivo\n4 núcleos · 16 GB · 2 SSD 480 GB en RAID 1\ncaché L-01, diario L-02, sincronizador L-03")
t_fg = ic(700, 215, "fw_site", "Par FortiGate activo-pasivo, SD-WAN", pos="left")
t_sw = ic(45, 310, "switch_acc", "Pila de 2 switches · 6 VLAN (cajas, adm.,\nmóviles, video, Wi-Fi clientes, mesón Emisor)")
t_pos = ic(45, 420, "pos", "POS, terminal de pago e impresora fiscal")
t_ups = ic(45, 510, "ups", "UPS del gabinete · venta 24 h sin enlace")

czone(d, 20, 640, 760, 230, "Centros de distribución", "cliente", align="left")
c1 = ic(700, 700, "building", "CD-01 · 2 enlaces de 2 proveedores\nopera 4 h sin enlace (RT-03.10)", pos="left")
c2 = ic(45, 790, "building", "CD-02 · enlace único + segundo propuesto")

czone(d, 20, 890, 760, 440, "DC-01 · casa matriz (140 m²)", "cliente", align="left")
dc_fg = ic(700, 950, "fw_site", "Par FortiGate activo-pasivo y pila de\nswitches de núcleo", pos="left")
dc_pl = ic(45, 1040, "server", "Plataformas conservadas: ERP/DTE,\nnúcleo 2009 y crédito 2011 · enlace propuesto a DC-02")
dc_na = ic(45, 1130, "san", "NAS Retail y NAS Emisor: arranque RAID 1;\ndatos RAID 10 + 1 disco de reserva (× 2,5)")
dc_tp = ic(45, 1225, "nvr", "Cinta en custodia (copia fuera de línea)\nUPS 30 min · generador 24 h · clima N+1")

czone(d, 20, 1350, 760, 120, "DC-02 · sala de respaldo (misma comuna)", "cliente", align="left")
dc2 = ic(45, 1400, "server", "Respaldo del Emisor si no se aprueba la residencia", size=44)

# ================= terceros: proveedores de enlace =================
czone(d, 820, 20, 250, 1450, "Proveedores de\ntelecomunicaciones", "tercero")
isp = d.icon(915, 300, "cloud", "Internet (principal)\nIPsec 500/4500\n≥ 10 Mbps por tienda\n2 Mbps por centro\nVPN de respaldo DC-01", size=60, shape_fill="#C55A11")
lte = d.icon(915, 520, "cell", "LTE/5G de otro\noperador\n≥ 5 Mbps (respaldo)", size=60, shape_fill="#C55A11")
erp = d.icon(915, 990, "connections", "Circuito\nExpressRoute\n200 Mbps · BGP 179\n(propuesto)", size=60)

# ================= CLD-01 y CLD-02 =================
czone(d, 1110, 20, 600, 700, "CLD-01 · Chile Central (producción)", "oss", align="left")
h1_fg = ic(1135, 90, "fw_site", "FortiGate-VM ×2, F4s_v2\nactivo-pasivo Z1 / Z2")
h1_vpn = ic(1135, 200, "vpngw", "Puerta VPN VpnGw2AZ")
h1_er = ic(1135, 290, "vpngw", "Puerta ExpressRoute ErGw1AZ\n(circuito propuesto)")
p1_pg = ic(1640, 400, "postgres", "PostgreSQL primario Z1 +\nespera Z2 (copia síncrona)", pos="left")
p1_eh = ic(1640, 500, "eventhubs", "Event Hubs: 3 copias entre zonas", pos="left")
p1_bk = ic(1640, 600, "backup", "Bóveda de respaldo inmutable\n(borrar exige 2.ª persona)", pos="left")

czone(d, 1110, 760, 600, 710, "CLD-02 · Brazil South (recuperación)", "oss", align="left")
h2_vpn = ic(1135, 830, "vpngw", "Puerta VPN: túnel desde DC-01\ny túnel entre hubs (hub espejo\ncon Firewall y FortiGate-VM ×2)")
p2_pg = ic(1640, 950, "postgres", "PostgreSQL réplica, mismo\ntamaño; se promueve con HA", pos="left")
p2_eh = ic(1640, 1060, "eventhubs", "Event Hubs geo-réplica", pos="left")
p2_bk = ic(1640, 1160, "backup", "Segunda bóveda de respaldo", pos="left")
p2_kv = ic(1135, 1260, "keyvault", "Key Vault propio (los secretos\nse reinyectan, no se replican)")
p2_ak = ic(1135, 1360, "aks", "AKS creado por IaC al conmutar")

# ================= enlaces =================
d.edge(t_fg, isp, "", width=W, exit=(1, 0.5), entry=(0, 0.5), points=[(800, cy(t_fg)), (800, cy(isp))], label_pos=0.75)
d.edge(t_fg, lte, "", width=W, line="dashed", exit=(1, 0.8), entry=(0, 0.5), points=[(808, cy(t_fg) + 10), (808, cy(lte))], label_pos=0.6)
d.edge(c1, isp, "", width=W, exit=(1, 0.5), entry=(0, 0.8), points=[(795, cy(c1)), (795, cy(isp) + 12)], label_pos=-0.6)
d.edge(dc_fg, erp, "", width=W, line="dashed", exit=(1, 0.5), entry=(0, 0.5), points=[(785, cy(dc_fg)), (785, cy(erp))], label_pos=0.8)
d.edge(dc_fg, isp, "", width=W, line="dashed", exit=(1, 0.3), entry=(0, 0.2),
       points=[(790, cy(dc_fg) - 8), (790, cy(isp) - 12)])
d.edge(isp, h1_fg, "", width=W, exit=(1, 0.3), entry=(0, 0.5), points=[(1090, P(isp)[1] + 18), (1090, cy(h1_fg))], label_pos=0.2)
d.edge(isp, h1_vpn, "", width=W, line="dashed", exit=(1, 0.6), entry=(0, 0.5), points=[(1098, P(isp)[1] + 36), (1098, cy(h1_vpn))])
d.edge(erp, h1_er, "", width=W, line="dashed", exit=(1, 0.5), entry=(0, 0.5), points=[(1082, cy(erp)), (1082, cy(h1_er))], label_pos=0.1)
d.edge(isp, h2_vpn, "", width=W, line="dashed", exit=(1, 0.9), entry=(0, 0.5),
       points=[(1074, P(isp)[1] + 54), (1074, cy(h2_vpn))], label_pos=0.45)
d.edge(dc_pl, dc2, "", width=W, line="dashed", exit=(0, 0.5), entry=(0, 0.5), points=[(32, cy(dc_pl)), (32, cy(dc2))], label_pos=0.6)
# replicación entre regiones
d.edge(p1_pg, p2_pg, "", width=W, line="dashed", color="#0078D4", exit=(1, 0.5), entry=(1, 0.5), points=[(1740, cy(p1_pg)), (1740, cy(p2_pg))])
d.edge(p1_eh, p2_eh, "", width=W, line="dashed", color="#0078D4", exit=(1, 0.5), entry=(1, 0.5), points=[(1730, cy(p1_eh)), (1730, cy(p2_eh))])
d.edge(p1_bk, p2_bk, "", width=W, line="dashed", color="#0078D4", exit=(1, 0.5), entry=(1, 0.5), points=[(1720, cy(p1_bk)), (1720, cy(p2_bk))])

# ================= replicación, respaldo y conmutación =================
czone(d, 1750, 20, 760, 450, "Replicación (da disponibilidad)", "oss", align="left", fill=False)
d.text(1770, 70, 720, 270,
       "• Entre zonas, síncrona: PostgreSQL primario Z1 → espera Z2, conmutación en 60 a 120 s sin pérdida; Event Hubs con 3 copias.\n"
       "• Entre regiones, asíncrona: PostgreSQL con retraso medido y alertado (RT-07.03); Event Hubs con retraso máximo < 15 min; registro de imágenes y almacenamiento copiados.\n"
       "• Emisor hacia CLD-02 solo si el Cliente aprueba la residencia; si no, su copia queda en DC-02.\n"
       "• Objetivo: RPO ≤ 15 min y RTO ≤ 4 h (RT-07.04).", size=21, align="left")
czone(d, 1750, 500, 760, 450, "Respaldo 3-2-1-1-0 (protege contra pérdida y ransomware)", "oss", align="left", fill=False)
d.text(1770, 550, 720, 220,
       "• 3 copias: producción, bóveda de CLD-01 y bóveda de CLD-02.\n"
       "• 2 medios: almacenamiento de Azure y cinta en custodia de DC-01.\n"
       "• 1 fuera del sitio: CLD-02 (o DC-02 para el Emisor sin residencia aprobada).\n"
       "• 1 inmutable: la bóveda; borrar exige una segunda persona.\n"
       "• 0 errores: restauración de prueba mensual con tiempo medido (RT-07.12).", size=21, align="left")
czone(d, 1750, 980, 760, 300, "Conmutación a CLD-02, activo-pasivo", "oss", align="left", fill=False)
d.text(1770, 1030, 720, 150,
       "1 declarar contingencia · 2 promover Event Hubs · 3 promover PostgreSQL y habilitar HA · 4 crear AKS por IaC · "
       "5 activar el origen de Brazil South en Front Door · 6 conciliar diarios de tienda. Ensayo dos veces al año; las tiendas venden durante todo el proceso.",
       size=21, align="left")
legend(d, 1750, 1300, 760, extra=[("dashed", "#1F1F1F", 2.5, "Propuesto o respaldo"),
                                  ("dashed", "#0078D4", 2.5, "Réplica entre regiones")])

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
