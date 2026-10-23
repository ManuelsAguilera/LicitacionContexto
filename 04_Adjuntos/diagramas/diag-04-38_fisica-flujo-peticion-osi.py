#!/usr/bin/env python3
"""Figura física general orientada al flujo: zonas, subredes, nodos como tarjetas, insignias OSI y matriz de encapsulación por salto.

Uso: python3 este.py salida.drawio [unica|normal|conm|capas]
  unica  Brazil South como sitio secundario (figura del informe)
  normal operación normal: Brasil en espera recibiendo copias
  conm   conmutación: Chile no disponible, Brasil en servicio
  capas  un .drawio con capas «Operación normal» y «Conmutación a Brasil» (la segunda oculta)
"""
import heapq
import html
import math
import sys

MODE = sys.argv[2] if len(sys.argv) > 2 else "unica"
MODES = ("unica", "normal", "conm")
PAR = "1"

G = 10
ICON = 48
W = 2110
LW = 5.3       # ancho medio de carácter a 10 px
LH = 12.5
CARD_W = 128

# --------------------------------------------------------------------------- iconos
AZ = "image;aspect=fixed;html=1;image=img/lib/azure2/"
CI = "aspect=fixed;html=1;fillColor=%s;strokeColor=#FFFFFF;shape=mxgraph.cisco."
IC = {
    "users": AZ + "identity/Users.svg", "entra": AZ + "identity/Azure_Active_Directory.svg",
    "fd": AZ + "networking/Front_Doors.svg", "ag": AZ + "networking/Application_Gateways.svg",
    "apim": AZ + "integration/API_Management_Services.svg", "ilb": AZ + "networking/Load_Balancers.svg",
    "aks": AZ + "containers/Kubernetes_Services.svg", "pg": AZ + "databases/Azure_Database_PostgreSQL_Server.svg",
    "vpn": AZ + "networking/Virtual_Network_Gateways.svg", "fw": AZ + "networking/Firewalls.svg",
    "pe": AZ + "networking/Private_Endpoint.svg", "kv": AZ + "security/Key_Vaults.svg",
    "sb": AZ + "analytics/Event_Hubs.svg", "bastion": AZ + "networking/Bastions.svg",
    "sent": AZ + "security/Azure_Sentinel.svg", "defender": AZ + "security/Azure_Defender.svg",
    "policy": AZ + "management_governance/Policy.svg", "acr": AZ + "containers/Container_Registries.svg",
    "devops": AZ + "devops/Azure_DevOps.svg", "dns": AZ + "networking/DNS_Zones.svg",
    "globe": AZ + "general/Globe.svg", "powerbi": AZ + "analytics/Power_BI_Embedded.svg", "vm": AZ + "compute/Virtual_Machine.svg",
    "laptop": "aspect=fixed;html=1;fillColor=#005073;strokeColor=none;shape=mxgraph.azure.laptop",
    "router": CI % "#005073" + "routers.router", "switch": CI % "#005073" + "switches.layer_3_switch",
    "ap": CI % "#005073" + "misc.access_point", "pc": CI % "#005073" + "computers_and_peripherals.workstation",
    "host": CI % "#005073" + "servers.fileserver", "xhost": CI % "#C25A10" + "security.ios_firewall",
    "cam": CI % "#005073" + "computers_and_peripherals.video_camera", "nvr": CI % "#005073" + "servers.storage_server",
    "ups": CI % "#8A5A2B" + "misc.ups", "iot": CI % "#005073" + "computers_and_peripherals.terminal",
    "dc": CI % "#005073" + "servers.fileserver",
}

OSI_COL = {"L1": "#6D4C41", "L2": "#E65100", "L3": "#1565C0", "L4": "#00897B", "L7": "#7B1FA2", "L3-7": "#37474F"}

# --------------------------------------------------------------------------- modelo
nodos, clusters, aristas, textos = {}, [], [], []


def N(id_, cx, cy, texto, icono, osi=None, ic=None):
    n = len(texto.split("\n"))
    bottom = cy + 26 + LH * n + 6
    bottom = int(math.ceil(bottom / 10.0) * 10)
    nodos[id_] = dict(id=id_, cx=cx, cy=cy, texto=texto, icono=icono, osi=osi,
                      card=(cx - 60, cy - 34, cx + 60, bottom))


def C(id_, label, kind, miembros=None, rect=None, align="left", pad=(10, 0, 10, 8), size=10.5):
    clusters.append(dict(id=id_, label=label, kind=kind, miembros=miembros or [], rect=rect, align=align, pad=pad, size=size))


def E(a, b, f=None, pill=None, grosor=None, **kw):
    v = {m: (f, pill) for m in MODES} if f else {}
    for k, val in kw.items():
        if val is None:
            v.pop(k, None)
        else:
            v[k] = val
    aristas.append(dict(a=a, b=b, v=v, grosor=grosor))


def EC(a, b, f, pill=None, **kw):
    """Arista de Chile: desaparece en el escenario de conmutación."""
    E(a, b, f, pill, conm=None, **kw)


def EB(a, b, f_conm, pill=None, **kw):
    """Arista de Brasil: tenue en espera; con color de flujo al conmutar."""
    E(a, b, None, None, unica=("mut", None), normal=("mut", None), conm=(f_conm, pill), **kw)


# columnas de las subredes (cx de cada nodo) y bordes de cajas
COL = dict(vpn=640, fw=790, ag=940, apim=1090, ilb=1240, aks=1390, pe=1540, pg=1690, sb=1840, kv=1990)
SUB = dict(  # (x0, x1) de cada subred
    vpn=(570, 710), fw=(720, 860), ag=(870, 1010), apim=(1020, 1160), aks=(1170, 1460), pe=(1470, 1610), paas=(1620, 2060))

PITCH = 196
ROW_H = 184
REG = {}
BANNER = 26


def region(p, y0, nombre, sub_banner, drlabel="", seq=False):
    """Crea nodos y contenedores de una región (Chile: p='c', Brasil: p='b')."""
    ys = {"r": y0 + 36, "x": y0 + 36 + PITCH, "f": y0 + 36 + 2 * PITCH}
    ystrip = y0 + 36 + 3 * PITCH
    sfx = ""
    for s, T in (("r", ys["r"]), ("f", ys["f"])):
        nm = "Retail" if s == "r" else "Filial"
        cy = T + 94
        N(f"{p}_vpn_{s}", COL["vpn"], cy, "VPN Gateway\nIPsec · IKE" + sfx, "vpn", "L3")
        N(f"{p}_fw_{s}", COL["fw"], cy, "Azure Firewall\nPremium · inspección" + sfx, "fw", "L3-7")
        N(f"{p}_ag_{s}", COL["ag"], cy, "Application Gateway\nBalanceo L7 · WAF" + sfx, "ag", "L7")
        N(f"{p}_apim_{s}", COL["apim"], cy, "API Management\nJWT · cuotas" + sfx, "apim", "L7")
        N(f"{p}_ilb_{s}", COL["ilb"], cy, "Load Balancer interno\nBalanceo L4 · VIP" + sfx, "ilb", "L4")
        N(f"{p}_aks_{s}", COL["aks"], cy, f"AKS {nm}\nSYS·BIZ·INT·STATE·OPS" + sfx, "aks", "L7")
        N(f"{p}_pe_{s}", COL["pe"], cy, "Private Endpoint\nsin IP pública" + sfx, "pe", "L3")
        N(f"{p}_pg_{s}", COL["pg"], cy, f"PostgreSQL {nm}\nTLS 5432 · propio" + sfx, "pg", "L7")
        N(f"{p}_sb_{s}", COL["sb"], cy, f"Service Bus {nm}\nAMQPS 5671" + sfx, "sb", "L7")
        N(f"{p}_kv_{s}", COL["kv"], cy, f"Key Vault {nm}\nclaves y secretos" + sfx, "kv", "L7")
    # ámbito X
    T = ys["x"]
    cy = T + 94
    N(f"{p}_ilbx", COL["ilb"], cy, "Entrada privada X-01\nlistener contractual" + sfx, "ilb", "L4")
    N(f"{p}_aksx", COL["aks"], cy, "AKS-X · X-01\ncontrol y bitácora" + sfx, "aks", "L7")
    N(f"{p}_pex", COL["pe"], cy, "Private Endpoint X\nsin IP pública" + sfx, "pe", "L3")
    N(f"{p}_pgx", COL["pg"], cy, "pg-x01\nbitácora propia" + sfx, "pg", "L7")
    # plano transversal
    cs = ystrip + 62
    strip = [("bastion", COL["vpn"], "Azure Bastion\nacceso con MFA/PIM", "bastion"),
             ("sent", COL["fw"], "Log Analytics\nSentinel R/F/X", "sent"),
             ("defender", COL["ag"], "Defender for Cloud\npostura y protección", "defender"),
             ("policy", COL["apim"], "Azure Policy\nconfiguración", "policy"),
             ("acr", COL["ilb"], "Container Registry\nimágenes por digest", "acr"),
             ("devops", COL["aks"], "Pipelines + Terraform\nagentes efímeros", "devops")]
    strip += [("bi", COL["pe"], "Gateways BI\nVM Retail y Filial", "powerbi"),
              ("ir", COL["pg"], "SHIR y Private Access\nVM auxiliares", "vm")]
    for k, cx, t, ic in strip:
        N(f"{p}_{k}", cx, cs, t + sfx, ic, "L7")
    # contenedores
    for s, T in (("r", ys["r"]), ("f", ys["f"])):
        nm = "Retail" if s == "r" else "Filial"
        blk = "10.64.0.0/16" if (s == "r" and p == "c") else "10.65.0.0/16" if p == "c" else "10.68.0.0/16" if s == "r" else "10.69.0.0/16"
        C(f"{p}_row_{s}", f"Ámbito {nm} · bloque {blk} (reserva de diseño) · tres VNets: hub, aplicación y datos",
          "row" + s, rect=(552, T, 2080, T + ROW_H), size=10.5)
        vtop, vbot = T + 24, T + ROW_H - 8
        C(f"{p}_vn_hub_{s}", "VNet hub", "vnet", rect=(558, vtop, 865, vbot), size=9.5)
        C(f"{p}_vn_app_{s}", "VNet aplicación", "vnet", rect=(866, vtop, 1466, vbot), size=9.5)
        C(f"{p}_vn_dat_{s}", "VNet de acceso privado a datos y PaaS administrado", "vnet", rect=(1467, vtop, 2074, vbot), size=9.5)
        sb_top, sb_bot = T + 44, T + ROW_H - 14
        for key, lab in (("vpn", "GatewaySubnet"), ("fw", "AzureFirewallSubnet"), ("ag", "Subred entrada"),
                         ("apim", "Subred APIM"), ("aks", "Subred nodos AKS"), ("pe", "Subred Private Endpoints")):
            C(f"{p}_sn_{key}_{s}", lab, "subred", rect=(SUB[key][0], sb_top, SUB[key][1], sb_bot), size=9)
        C(f"{p}_paas_{s}", "PaaS administrado (fuera de la VNet)", "paas", rect=(SUB["paas"][0], sb_top, SUB["paas"][1], sb_bot), size=9)
    T = ys["x"]
    C(f"{p}_row_x", f"Ámbito X-01 (frontera) · bloque {'10.66.0.0/16' if p == 'c' else '10.70.0.0/16'} (reserva de diseño) · sin Front Door público: solo contratos autorizados",
      "rowx", rect=(552, T, 2080, T + ROW_H), size=10.5)
    vtop, vbot = T + 24, T + ROW_H - 8
    C(f"{p}_vn_app_x", "VNet aplicación X", "vnet", rect=(1166, vtop, 1466, vbot), size=9.5)
    C(f"{p}_vn_dat_x", "VNet de acceso privado a datos X", "vnet", rect=(1467, vtop, 1766, vbot), size=9.5)
    sb_top, sb_bot = T + 44, T + ROW_H - 14
    C(f"{p}_sn_aks_x", "Subred nodos AKS-X", "subred", rect=(SUB["aks"][0], sb_top, SUB["aks"][1], sb_bot), size=9)
    C(f"{p}_sn_pe_x", "Subred Private Endpoints", "subred", rect=(SUB["pe"][0], sb_top, SUB["pe"][1], sb_bot), size=9)
    C(f"{p}_paas_x", "PaaS administrado", "paas", rect=(1620, sb_top, 1760, sb_bot), size=9)
    textos.append(dict(id=f"{p}_notax", x=575, y=T + 70, w=560, h=70,
                       t="X-01 no expone pila pública. Recibe solo el contrato «compra autorizable» desde Retail,\nlo valida y consulta a Filial con respuesta limitada. Bitácora propia; sin acceso\nR↔F y sin credenciales de base Filial."))
    C(f"{p}_strip", "Plano transversal de seguridad, operación y entrega · instancias propias por ámbito R / F / X", "strip",
      rect=(552, ystrip, 2080, ystrip + 150), size=10.5)
    yb = ystrip + 150 + 14 + (44 if seq else 0)
    REG[p] = (540, y0, 2092, yb, y0 + BANNER, ystrip + 150 + 14 + 6)
    C(f"{p}_region", nombre, "region" + p, rect=(540, y0, 2092, yb), size=13)
    return ys, yb


# ------------------------------------------------------------------ zona superior
TOP_CY = 160
N("ext1", 610, TOP_CY, "Canales conservados\nproveedor externo", "globe", "L7")
N("ext2", 770, TOP_CY, "Pagos y transporte\nfirma · mensajería", "globe", "L7")
N("cliente", 950, TOP_CY, "Cliente / titular\nnavegador o app", "users", "L7")
N("dns", 1110, TOP_CY, "DNS público\nresuelve el canal", "dns", "L7")
N("fd", 1290, TOP_CY, "Front Door Premium\nL7 global · WAF", "fd", "L7")
N("entra", 1450, TOP_CY, "Entra ID\nExternal ID · PIM", "entra", "L7")
N("admin", 1630, TOP_CY, "Administración\nautorizada · MFA/PIM", "laptop", "L7")
C("z_ext", "CANALES Y SOCIOS EXTERNOS", "zinet", rect=(540, 70, 842, 248), size=11)
C("z_inet", "INTERNET", "zinet", rect=(876, 70, 1184, 248), size=11)
C("z_borde", "BORDE GLOBAL AZURE", "zborde", rect=(1200, 70, 1524, 248), size=11)
C("z_admin", "ADMINISTRACIÓN", "zinet", rect=(1540, 70, 1710, 248), size=11)

ys_c, yb_c = region("c", 270, "AZURE · CHILE CENTRAL · SITIO PRINCIPAL · producción R / F / X", "")
ys_b, yb_b = region("b", yb_c + 24, "AZURE · BRAZIL SOUTH · SITIO SECUNDARIO · recuperación R / F / X", "", seq=True)

# ------------------------------------------------------------------ on-premise (columna izquierda)
OC = (100, 245, 390)
r_cy1 = ys_c["r"] + 94
f_cy1 = ys_c["f"] + 94
N("caja", OC[0], r_cy1, "Cajas Retail\nPOS · VLAN 10", "pc", "L7")
N("sw_r", OC[1], r_cy1, "Switches LAN Retail\npar · VLAN/VRF-R", "switch", "L2")
N("sd_r", OC[2], r_cy1, "Routers / SD-WAN\nRetail · HA", "router", "L3")
N("ap_r", OC[0], r_cy1 + 135, "AP Wi-Fi Retail\n802.1X · VLAN 12", "ap", "L2")
N("h_r1", OC[1], r_cy1 + 135, "SIT-xx-R-01\nventa y diario", "host", "L7")
N("h_r2", OC[2], r_cy1 + 135, "SIT-xx-R-02\nréplica local Retail", "host", "L7")
N("mes", OC[0], f_cy1, "Mesón financiero\ncliente F · VLAN 20", "pc", "L7")
N("sw_f", OC[1], f_cy1, "Switches LAN Filial\npar · VLAN/VRF-F", "switch", "L2")
N("sd_f", OC[2], f_cy1, "Routers / SD-WAN\nFilial · HA", "router", "L3")
N("ap_f", OC[0], f_cy1 + 135, "AP Wi-Fi financiero\n802.1X · VLAN 22", "ap", "L2")
N("h_f1", OC[1], f_cy1 + 135, "SIT-xx-F-01\nautorizador / libro F", "host", "L7")
N("h_f2", OC[2], f_cy1 + 135, "SIT-xx-F-02\nréplica F / X local", "host", "L7")
N("x_loc", OC[1], f_cy1 + 270, "X-01 local · 2 inst.\naisladas en par F", "xhost", "L7")
dc_cy = f_cy1 + 270 + 162
N("sd_dc", OC[0], dc_cy, "Router / FW DC-01\ntúneles por ámbito", "router", "L3")
N("dc", OC[1], dc_cy, "Sistemas conservados\nERP · crédito · 2009", "dc", "L7")
N("cd", OC[2], dc_cy, "CD-01 / CD-02\ncaptura local · WMS", "host", "L7")
sv = dc_cy + 162
N("iot", OC[0], sv, "IoT / lockers\nsolo contrato Pedidos", "iot", "L7")
N("aux", OC[1], sv, "Switch / borde aux.\nVRF y ACL propias", "switch", "L2")
N("guest", OC[2], sv, "Wi-Fi invitados\nVLAN 60 · Internet", "ap", "L2")
N("cam", OC[0], sv + 135, "Cámaras IP\nCCTV · VLAN 50", "cam", "L7")
N("nvr", OC[1], sv + 135, "NVR local\nretención 30 días", "nvr", "L7")
N("gen", OC[2], sv + 135, "Generador / edificio\n24 h esenciales", "ups", "L1")
N("ats", OC[2], sv + 270, "ATS / tableros A-B\ntransferencia", "ups", "L1")
N("ups", OC[1], sv + 270, "UPS A/B online\n30 min a plena carga", "ups", "L1")
N("pdu", OC[0], sv + 270, "PDU A/B por rack\na hosts y red", "ups", "L1")
yb_on = max(yb_b, sv + 270 + 100)

C("on_r", "Tienda SIT-xx · Retail · VRF-R", "onr", rect=(28, r_cy1 - 94, 468, r_cy1 + 135 + 98), size=10)
C("on_f", "Tienda SIT-xx · Filial · VRF-F", "onf", rect=(28, f_cy1 - 94, 468, f_cy1 + 270 + 98), size=10)
C("on_dc", "DC / CD · sistemas conservados", "ong", rect=(28, dc_cy - 64, 468, dc_cy + 98), size=10)
C("on_sv", "Segmentos auxiliares, CCTV y soporte físico (capa 1)", "ong", rect=(28, sv - 64, 468, sv + 270 + 98), size=10)
C("onprem", "ON-PREMISE · tiendas, CD y DC de Ancoa", "zonprem", rect=(15, 270, 480, yb_on), size=13)

# ------------------------------------------------------------------ leyenda superior izquierda
C("leyenda", "Cómo leer la figura", "leyenda", rect=(15, 70, 480, 250), size=10.5)

# --------------------------------------------------------------------------- aristas
# flujos: dig (canal digital), tie (tienda), com (camino común), x (cruce X-01), dr (copias y conmutación),
# sec (dependencia de servicio), id (identidad), adm (administración), pw (energía)
E("cliente", "dns", "dig", "1", 2.2)
E("cliente", "fd", "dig", "2")
for s_ in ("r", "f"):
    EC("fd", f"c_ag_{s_}", "dig", "3")
    EC(f"c_ag_{s_}", f"c_apim_{s_}", "com", "4")
    EC(f"c_apim_{s_}", f"c_ilb_{s_}", "com", "5")
    EC(f"c_ilb_{s_}", f"c_aks_{s_}", "com", "6")
    EC(f"c_aks_{s_}", f"c_pe_{s_}", "com", "7")
    EC(f"c_pe_{s_}", f"c_pg_{s_}", "com")
    EC(f"c_pe_{s_}", f"c_sb_{s_}", "sec")
    EC(f"c_pe_{s_}", f"c_kv_{s_}", "sec")
    EC("entra", f"c_apim_{s_}", "id", "Token")
    E("entra", f"b_apim_{s_}", None, conm=("id", "Token"))
    EC(f"c_vpn_{s_}", f"c_fw_{s_}", "tie", "S4")
    EC(f"c_fw_{s_}", f"c_ag_{s_}", "tie")
EC("c_aks_r", "c_ilbx", "x", "8")
EC("c_ilbx", "c_aksx", "x")
EC("c_aksx", "c_ag_f", "x", "9")
EC("c_aksx", "c_pex", "sec")
EC("c_pex", "c_pgx", "sec")
E("admin", "entra", "id", "MFA")
EC("c_fw_r", "ext1", "adm", "HTTPS C21")
EC("c_fw_f", "ext2", "adm", "HTTPS C21")
# Brasil: misma pila; tenue en espera, con color de flujo al conmutar
for s_ in ("r", "f"):
    EB(f"b_vpn_{s_}", f"b_fw_{s_}", "tie", "S4")
    EB(f"b_fw_{s_}", f"b_ag_{s_}", "tie")
    EB(f"b_ag_{s_}", f"b_apim_{s_}", "com", "4")
    EB(f"b_apim_{s_}", f"b_ilb_{s_}", "com", "5")
    EB(f"b_ilb_{s_}", f"b_aks_{s_}", "com", "6")
    EB(f"b_aks_{s_}", f"b_pe_{s_}", "com", "7")
    EB(f"b_pe_{s_}", f"b_pg_{s_}", "com")
    E(f"b_pe_{s_}", f"b_sb_{s_}", None, conm=("sec", None))
    E(f"b_pe_{s_}", f"b_kv_{s_}", None, conm=("sec", None))
EB("b_ilbx", "b_aksx", "x")
EB("b_aksx", "b_pex", "sec")
EB("b_pex", "b_pgx", "sec")
E("b_aks_r", "b_ilbx", None, conm=("x", "8"))
E("b_aksx", "b_ag_f", None, conm=("x", "9"))
# copia continua Chile -> Brasil (solo en operación)
E("c_pg_r", "b_pg_r", None, unica=("rep", "10 réplica"), normal=("rep", "10 réplica"))
E("c_pg_f", "b_pg_f", None, unica=("rep", "10 réplica"), normal=("rep", "10 réplica"))
E("c_pgx", "b_pgx", None, unica=("rep", "10 bitácora"), normal=("rep", "10 bitácora"))
E("c_acr", "b_acr", None, unica=("rep", "10 imágenes"), normal=("rep", "10 imágenes"))
# conmutación de la entrada pública
E("fd", "b_ag_r", None, unica=("dr", "11"), conm=("dig", "3"))
E("fd", "b_ag_f", None, unica=("dr", "11"), conm=("dig", "3"))
# tienda
for s_, caja, sw, sd, h1, h2, ap in (("r", "caja", "sw_r", "sd_r", "h_r1", "h_r2", "ap_r"), ("f", "mes", "sw_f", "sd_f", "h_f1", "h_f2", "ap_f")):
    E(caja, sw, "tie", "S1")
    E(sw, sd, "tie", "S2")
    EC(sd, f"c_vpn_{s_}", "tie", "S3")
    E(sd, f"b_vpn_{s_}", None, unica=("dr", None), normal=("dr", None), conm=("tie", "S3"))
    E(ap, sw, "sec")
    E(sw, h1, "sec")
    E(h1, h2, "sec")
E("h_r2", "x_loc", "x", "Compra offline")
E("x_loc", "h_f2", "x")
EC("x_loc", "c_aksx", "dr", "Replay")
E("x_loc", "b_aksx", None, conm=("dr", "Replay"))
EC("sd_dc", "c_vpn_r", "tie", "S3")
EC("sd_dc", "c_vpn_f", "tie", "S3")
E("sd_dc", "b_vpn_r", None, unica=("dr", None), normal=("dr", None), conm=("tie", "S3"))
E("sd_dc", "b_vpn_f", None, unica=("dr", None), normal=("dr", None), conm=("tie", "S3"))
E("dc", "sd_dc", "sec")
E("cd", "sd_dc", "sec")
E("iot", "aux", "sec")
E("guest", "aux", "sec")
E("cam", "nvr", "sec")
E("gen", "ats", "pw")
E("ats", "ups", "pw")
E("ups", "pdu", "pw")

FLUJO = {  # color, grosor, trazo
    "dig": ("#C62828", 3.0, ""), "tie": ("#2E7D32", 3.0, ""), "com": ("#1A237E", 3.0, ""),
    "x": ("#E07B00", 3.0, ""), "dr": ("#168F80", 2.0, "dashed=1;dashPattern=8 4;"),
    "sec": ("#7C8794", 1.4, ""), "id": ("#1F3864", 1.6, "dashed=1;dashPattern=2 3;"),
    "adm": ("#6B7280", 1.6, "dashed=1;dashPattern=6 4;"), "pw": ("#8A5A2B", 1.8, "dashed=1;dashPattern=2 3;"),
    "rep": ("#0E7C6B", 3.6, ""), "mut": ("#9AA5AD", 1.3, "dashed=1;dashPattern=4 4;"),
}

ZONA = {  # (relleno, borde, banner, grosor)
    "zinet": ("#F3F4F6", "#5F6368", "#5F6368", 3.5), "zborde": ("#E8F2FC", "#0078D4", "#0078D4", 3.5),
    "regionc": ("#F4F7FD", "#0B3D91", "#0B3D91", 5), "regionb": ("#F1FAF7", "#0F7B6C", "#0F7B6C", 5),
    "zonprem": ("#FFFAF0", "#7A4B00", "#7A4B00", 5),
}
SUBZ = {
    "rowr": ("#DCEBFA", "#2F78B7", 1.5, ""), "rowf": ("#E9DFF5", "#7A55A5", 1.5, ""), "rowx": ("#FDE8CB", "#D98A2B", 1.5, ""),
    "vnet": ("none", "#5B6573", 1.2, ""), "subred": ("#FFFFFF", "#5B6573", 1.0, "dashed=1;dashPattern=4 3;"),
    "paas": ("#FFFFFF", "#5B6573", 1.4, ""), "strip": ("#EEF0F3", "#7B8794", 1.4, ""),
    "onr": ("#DCEBFA", "#2F78B7", 1.5, ""), "onf": ("#E9DFF5", "#7A55A5", 1.5, ""), "ong": ("#F1F2F4", "#8B9099", 1.4, ""),
    "leyenda": ("#FFFFFF", "#9AA3AE", 1.0, ""),
}

# --------------------------------------------------------------------------- geometría de clusters
cl_id = {c["id"]: c for c in clusters}
BANNER = 26


def cluster_rect(c):
    return c["rect"]


def zona_banner_h(c):
    return BANNER if c["kind"] in ZONA else 0


def texto_w(c):
    return len(c["label"]) * c["size"] * 0.56 + 14


def header_rect(c):
    x0, y0, x1, y1 = c["rect"]
    w = texto_w(c)
    if c["kind"] in ZONA:
        return (x0 + 10, y0 + 3, x0 + 10 + w, y0 + BANNER - 3)
    if c["kind"] in ("subred", "paas"):
        return (x0 + 5, y0 + 2, x0 + 5 + w, y0 + 18)
    if c["kind"] == "vnet":
        return (x0 + 6, y0 + 1, x0 + 6 + w, y0 + 17)
    if c["kind"] in ("rowr", "rowf", "rowx"):
        return (x0 + 8, y0 + 3, x0 + 8 + w, y0 + 21)
    if c["kind"] in ("onr", "onf", "ong", "leyenda"):
        return (x0 + 8, y0 + 3, x0 + 8 + w, y0 + 21)
    return (x0 + 8, y0 + 3, x0 + 8 + w, y0 + 21)


# --------------------------------------------------------------------------- obstáculos y cuadrícula
OBS = []
for n in nodos.values():
    l, t, r, b = n["card"]
    OBS.append((l - 5, t - 5, r + 5, b + 5, n["id"]))
for c in clusters:
    if c["kind"] == "leyenda":
        OBS.append((*c["rect"], c["id"]))
        continue
    l, t, r, b = header_rect(c)
    OBS.append((l - 4, t - 2, r + 4, b + 2, "hdr_" + c["id"]))
for t in textos:
    OBS.append((t["x"] - 4, t["y"] - 4, t["x"] + t["w"] + 4, t["y"] + t["h"] + 4, t["id"]))
OBS.append((540, 248, 1800, 262, "hueco_banner"))  # no usado: mantiene aire bajo la zona superior
OBS.append((1480, REG["b"][1], 2092, REG["b"][1] + BANNER + 2, "kpi"))
OBS.append((1480, REG["c"][1], 2092, REG["c"][1] + BANNER + 2, "kpi_c"))

Y_END = int(yb_on) + 40
NX, NY = W // G + 2, (Y_END + 700) // G
bloq = [[False] * NX for _ in range(NY)]
for (l, t, r, b, tag) in OBS:
    if tag == "hueco_banner":
        continue
    for iy in range(max(0, int(t // G)), min(NY, int(b // G) + 1)):
        for ix in range(max(0, int(l // G)), min(NX, int(r // G) + 1)):
            if l < ix * G < r and t < iy * G < b:
                bloq[iy][ix] = True
for iy in range(NY):
    for ix in list(range(0, 3)) + list(range(NX - 3, NX)):
        bloq[iy][ix] = True
for ix in range(NX):
    for iy in range(0, 5):
        bloq[iy][ix] = True

bh, bv = set(), set()
for c in clusters:
    x0, y0, x1, y1 = c["rect"]
    for y in (y0, y1):
        for ix in range(int(x0 // G), int(x1 // G) + 1):
            bh.add((ix, round(y / G)))
    for x in (x0, x1):
        for iy in range(int(y0 // G), int(y1 // G) + 1):
            bv.add((round(x / G), iy))

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
oh, ov, usados = set(), set(), set()


def puertos(nid):
    n = nodos[nid]
    l, t, r, b = n["card"]
    cx, cy = n["cx"], n["cy"]
    res = []
    for side, d in zip(("right", "bottom", "left", "top"), range(4)):
        offs = (0, -20, 20) if side in ("right", "left") else (0, -30, 30)
        for off in offs:
            if side == "right":
                p = (r + 10, cy + off)
            elif side == "left":
                p = (l - 10, cy + off)
            elif side == "top":
                p = (cx + off, t - 10)
            else:
                p = (cx + off, b + 10)
            ix, iy = int(p[0] // G), int(p[1] // G)
            if bloq[iy][ix] or (nid, side, off) in usados:
                continue
            res.append(dict(nid=nid, side=side, off=off, ix=ix, iy=iy, dir=d))
    return res


def ruta(src, dst):
    S, T = puertos(src), puertos(dst)
    if not S or not T:
        return None
    tset = {(t["ix"], t["iy"], (t["dir"] + 2) % 4): t for t in T}
    tpos = [(t["ix"], t["iy"]) for t in T]

    def h(ix, iy):
        return min(abs(ix - a) + abs(iy - b) for a, b in tpos)

    pq, best, padre = [], {}, {}
    for s in S:
        st = (s["ix"], s["iy"], s["dir"])
        c0 = 0 if s["off"] == 0 else 0.4
        best[st] = c0
        padre[st] = (None, s)
        heapq.heappush(pq, (c0 + h(s["ix"], s["iy"]), c0, st))
    fin = None
    while pq:
        f, g, st = heapq.heappop(pq)
        if best.get(st, 1e18) < g - 1e-9:
            continue
        if st in tset:
            fin = st
            break
        ix, iy, d = st
        for nd in (d, (d + 1) % 4, (d + 3) % 4):
            dx, dy = DIRS[nd]
            jx, jy = ix + dx, iy + dy
            if not (0 <= jx < NX and 0 <= jy < NY) or bloq[jy][jx]:
                continue
            hz = nd in (0, 2)
            cst = 1.0 + (7.0 if nd != d else 0)
            if hz:
                if (jx, jy) in oh:
                    continue
                if (jx, jy - 1) in oh or (jx, jy + 1) in oh:
                    cst += 5
                if (jx, jy) in ov:
                    cst += 14
                if (jx, jy) in bh:
                    cst += 6
            else:
                if (jx, jy) in ov:
                    continue
                if (jx - 1, jy) in ov or (jx + 1, jy) in ov:
                    cst += 5
                if (jx, jy) in oh:
                    cst += 14
                if (jx, jy) in bv:
                    cst += 6
            ns = (jx, jy, nd)
            ng = g + cst
            if ng < best.get(ns, 1e18) - 1e-9:
                best[ns] = ng
                padre[ns] = (st, None)
                heapq.heappush(pq, (ng + h(jx, jy), ng, ns))
    if fin is None:
        return None
    cam, cur = [], fin
    while True:
        p, s = padre[cur]
        cam.append(cur)
        if p is None:
            origen = s
            break
        cur = p
    cam.reverse()
    return origen, tset[fin], [(ix * G, iy * G) for ix, iy, _ in cam]


def punto_borde(p):
    n = nodos[p["nid"]]
    l, t, r, b = n["card"]
    if p["side"] == "right":
        return (r, n["cy"] + p["off"])
    if p["side"] == "left":
        return (l, n["cy"] + p["off"])
    if p["side"] == "top":
        return (n["cx"] + p["off"], t)
    return (n["cx"] + p["off"], b)


def simplificar(pts):
    out = []
    for p in pts:
        if not out or out[-1] != p:
            out.append(p)
    ch = True
    while ch:
        ch = False
        for i in range(1, len(out) - 1):
            a, b, c = out[i - 1], out[i], out[i + 1]
            if a[0] == b[0] == c[0] or a[1] == b[1] == c[1]:
                del out[i]
                ch = True
                break
    return out


def dist(e):
    a, b = nodos[e["a"]], nodos[e["b"]]
    return abs(a["cx"] - b["cx"]) + abs(a["cy"] - b["cy"])


SEL = [i for i, e in enumerate(aristas) if (MODE == 'capas' and e['v']) or (MODE in MODES and MODE in e['v'])]
res = {}
fallos = []
prio = {"com": 0, "dig": 0, "tie": 0, "x": 1, "id": 2, "adm": 2, "dr": 3, "sec": 3, "pw": 3, "rep": 1, "mut": 3}


def fl0(e):
    for m in ("conm", "normal", "unica"):
        if m in e["v"]:
            return e["v"][m][0]


orden = sorted(SEL, key=lambda i: (dist(aristas[i]) // 400, prio[fl0(aristas[i])], dist(aristas[i])))
for i in orden:
    e = aristas[i]
    r = ruta(e["a"], e["b"])
    if r is None:
        fallos.append((e["a"], e["b"]))
        continue
    o, d, cam = r
    usados.add((o["nid"], o["side"], o["off"]))
    usados.add((d["nid"], d["side"], d["off"]))
    for k in range(len(cam) - 1):
        (x0, y0), (x1, y1) = cam[k], cam[k + 1]
        if y0 == y1:
            oh.add((x0 // G, y0 // G)); oh.add((x1 // G, y1 // G))
        else:
            ov.add((x0 // G, y0 // G)); ov.add((x1 // G, y1 // G))
    res[i] = (o, d, simplificar([punto_borde(o)] + cam + [punto_borde(d)]))
if fallos:
    print("SIN RUTA:", fallos, file=sys.stderr)

# --------------------------------------------------------------------------- verificación
def cruza(p, q, r):
    l, t, rr, b = r
    (x0, y0), (x1, y1) = p, q
    if y0 == y1:
        return t < y0 < b and max(min(x0, x1), l) < min(max(x0, x1), rr)
    return l < x0 < rr and max(min(y0, y1), t) < min(max(y0, y1), b)


viol = set()
for i, (o, d, pts) in res.items():
    e = aristas[i]
    for k in range(len(pts) - 1):
        for (l, t, r, b, tag) in OBS:
            if tag == "hueco_banner":
                continue
            if cruza(pts[k], pts[k + 1], (l + 6, t + 6, r - 6, b - 6)):
                viol.add((e["a"], e["b"], tag))
print("violaciones:", len(viol), sorted(viol)[:12])
segs = []
for i, (o, d, pts) in res.items():
    for k in range(len(pts) - 1):
        segs.append((i, pts[k], pts[k + 1]))
cr = 0
for a in range(len(segs)):
    for b in range(a + 1, len(segs)):
        ia, p0, p1 = segs[a]; ib, q0, q1 = segs[b]
        if ia == ib:
            continue
        ha, hb = p0[1] == p1[1], q0[1] == q1[1]
        if ha == hb:
            continue
        h0, h1, v0, v1 = (p0, p1, q0, q1) if ha else (q0, q1, p0, p1)
        if min(h0[0], h1[0]) < v0[0] < max(h0[0], h1[0]) and min(v0[1], v1[1]) < h0[1] < max(v0[1], v1[1]):
            cr += 1
print("cruces entre flechas:", cr)

# --------------------------------------------------------------------------- píldoras (números de salto)
pill_rects = []


def libre(rect):
    l, t, r, b = rect
    for (ol, ot, orr, ob, tag) in OBS:
        if tag == "hueco_banner":
            continue
        if l < orr and r > ol and t < ob and b > ot:
            return False
    for (pl, pt, pr, pb) in pill_rects:
        if l < pr + 2 and r > pl - 2 and t < pb + 2 and b > pt - 2:
            return False
    for (i2, p0, p1) in segs:
        if cruza_rect(p0, p1, rect):
            return False
    return True


def cruza_rect(p, q, rect):
    l, t, r, b = rect
    (x0, y0), (x1, y1) = p, q
    if y0 == y1:
        return t <= y0 <= b and max(min(x0, x1), l) < min(max(x0, x1), r)
    return l <= x0 <= r and max(min(y0, y1), t) < min(max(y0, y1), b)


pills = {}


def pill_txt(e):
    t = [v[1] for v in e["v"].values() if v[1]]
    return max(t, key=len) if t else None


for i in sorted(res):
    e = aristas[i]
    txt = pill_txt(e)
    if not txt:
        continue
    o, d, pts = res[i]
    esnum = len(txt) <= 3 and (txt.isdigit() or txt[0] == "S")
    pw = 20 if esnum else len(txt) * 5.6 + 12
    ph = 20 if esnum else 17
    cand = []
    for k in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[k], pts[k + 1]
        L = abs(x1 - x0) + abs(y1 - y0)
        for fr in (0.5, 0.35, 0.65, 0.2, 0.8):
            cx, cy = x0 + (x1 - x0) * fr, y0 + (y1 - y0) * fr
            if L >= (pw if y0 == y1 else ph) + 4:
                cand.append((-(L), fr, cx, cy))
    cand.sort(key=lambda c: c[0])
    otros_segs = [s_ for s_ in segs if s_[0] != i]
    colocado = False
    for _, fr, cx, cy in cand:
        rect = (cx - pw / 2, cy - ph / 2, cx + pw / 2, cy + ph / 2)
        ok = True
        for (ol, ot, orr, ob, tag) in OBS:
            if tag == "hueco_banner":
                continue
            if tag in nodos:
                ol, ot, orr, ob = ol + 5, ot + 5, orr - 5, ob - 5
            if rect[0] < orr and rect[2] > ol and rect[1] < ob and rect[3] > ot:
                ok = False; break
        if ok:
            for (pl, pt, pr_, pb) in pill_rects:
                if rect[0] < pr_ + 2 and rect[2] > pl - 2 and rect[1] < pb + 2 and rect[3] > pt - 2:
                    ok = False; break
        if ok:
            for (i2, p0, p1) in otros_segs:
                if cruza_rect(p0, p1, rect):
                    ok = False; break
        if ok:
            pill_rects.append(rect); pills[i] = rect; colocado = True
            break
    if not colocado:
        print("píldora sin lugar:", txt, e["a"], e["b"], file=sys.stderr)
        if cand:
            _, fr, cx, cy = cand[0]
            rect = (cx - pw / 2, cy - ph / 2, cx + pw / 2, cy + ph / 2)
            pill_rects.append(rect); pills[i] = rect

# --------------------------------------------------------------------------- salida draw.io
def esc(t):
    return html.escape(t, quote=True).replace("\n", "&#xa;")


cells = ['<mxCell id="0"/>', '<mxCell id="1" value="Base" parent="0"/>']
if MODE == "capas":
    cells.append('<mxCell id="lay_n" value="Operación normal" parent="0"/>')
    cells.append('<mxCell id="lay_c" value="Conmutación a Brasil" parent="0" visible="0"/>')


def vertex(id_, val, style, x, y, w, h):
    cells.append(f'<mxCell id="{id_}" value="{esc(val)}" style="{style}" vertex="1" parent="{PAR}">'
                 f'<mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')


def area(c):
    x0, y0, x1, y1 = c["rect"]
    return (x1 - x0) * (y1 - y0)


for c in sorted(clusters, key=lambda c: -area(c)):
    x0, y0, x1, y1 = c["rect"]
    k = c["kind"]
    if k in ZONA:
        fill, stroke, banner, sw = ZONA[k]
        dash = "dashed=1;dashPattern=14 7;" if k == "regionb" else ""
        vertex(f"g_{c['id']}", "", f"rounded=1;arcSize=2;html=1;fillColor={fill};strokeColor={stroke};strokeWidth={sw};{dash}", x0, y0, x1 - x0, y1 - y0)
        vertex(f"b_{c['id']}", c["label"],
               f"rounded=0;html=1;fillColor={banner};strokeColor={banner};strokeWidth=1;fontColor=#FFFFFF;fontStyle=1;"
               f"fontSize={c['size']};align=left;spacingLeft=10;verticalAlign=middle;fontFamily=Helvetica;", x0 + 1, y0 + 1, x1 - x0 - 2, BANNER - 1)
    elif k == "leyenda":
        pass
    else:
        fill, stroke, sw, dash = SUBZ[k]
        fc = fill if fill != "none" else "none"
        vertex(f"g_{c['id']}", c["label"],
               f"rounded={0 if k in ('vnet',) else 1};arcSize=3;html=1;whiteSpace=nowrap;fillColor={fc};strokeColor={stroke};strokeWidth={sw};{dash}"
               f"verticalAlign=top;align=left;spacingLeft=5;spacingTop=0;fontStyle={0 if k in ('subred','vnet') else 1};fontSize={c['size']};"
               f"fontColor=#2A2F36;fontFamily=Helvetica;", x0, y0, x1 - x0, y1 - y0)

# nodos: tarjeta + ícono + insignia OSI
for n in nodos.values():
    l, t, r, b = n["card"]
    vertex(f"n_{n['id']}", n["texto"],
           "rounded=1;arcSize=8;html=1;fillColor=#FFFFFF;strokeColor=#8D97A5;strokeWidth=1.2;verticalAlign=bottom;align=center;"
           "fontSize=10;fontColor=#1A1A1A;fontFamily=Helvetica;spacingBottom=3;whiteSpace=nowrap;", l, t, r - l, b - t)
    cells.append(f'<mxCell id="i_{n["id"]}" value="" style="{IC[n["icono"]]};" vertex="1" parent="{PAR}">'
                 f'<mxGeometry x="{n["cx"] - ICON // 2}" y="{n["cy"] - ICON // 2 - 4}" width="{ICON}" height="{ICON}" as="geometry"/></mxCell>')
    if n["osi"]:
        c = OSI_COL[n["osi"]]
        bw = 30 if "-" not in n["osi"] else 44
        vertex(f"o_{n['id']}", n["osi"],
               f"rounded=1;arcSize=30;html=1;fillColor={c};strokeColor=#FFFFFF;strokeWidth=1;fontColor=#FFFFFF;fontStyle=1;fontSize=9;fontFamily=Helvetica;align=center;verticalAlign=middle;",
               r - bw - 3, t + 3, bw, 15)

for t in textos:
    vertex(t["id"], t["t"], "text;html=1;align=left;verticalAlign=top;fontSize=10;fontColor=#4A3A12;fontFamily=Helvetica;fontStyle=2;whiteSpace=nowrap;",
           t["x"], t["y"], t["w"], t["h"])

# chips en los banners: Brasil con sus metas; Chile marcado como principal
def chips_derecha(x1, y, items, fill, stroke, color, tag):
    x = x1 - 10
    for k, txt in enumerate(reversed(items)):
        w = len(txt) * 5.3 + 16
        x -= w
        vertex(f"{tag}{k}", txt, f"rounded=1;arcSize=50;html=1;fillColor={fill};strokeColor={stroke};strokeWidth=1;fontColor={color};fontStyle=1;fontSize=9;fontFamily=Helvetica;align=center;verticalAlign=middle;",
               x, y + 5, w, 17)
        x -= 6


bx0, by0, bx1, by1, *_ = REG["b"]
chips_derecha(bx1, by0, ["RTO ≤ 4 h", "RPO ≤ 15 min en críticos", "50 VM de espera + 4 BI apagadas", "metas sujetas a ensayo"], "#FFFFFF", "#FFFFFF", "#0F5F53", "kb")
cx0, cy0, cx1, cy1, *_ = REG["c"]
chips_derecha(cx1, cy0, ["54 VM de producción · 12 PostgreSQL", "carga principal"], "#FFFFFF", "#FFFFFF", "#0B3D91", "kc")

# ---------------- escenarios (mut -> sombreado -> flujos activos -> píldoras -> estados -> secuencia)
TAGS = {"ESPERA": ("#F9A825", "#3E2723"), "RÉPLICA": ("#168F80", "#FFFFFF"), "APAGADO": ("#78909C", "#FFFFFF"),
        "ACTIVO": ("#2E7D32", "#FFFFFF"), "PROMOVIDA": ("#00695C", "#FFFFFF"), "REPRODUCIR": ("#EF6C00", "#FFFFFF")}
EST_ESPERA = {"vpn", "fw", "ag", "apim", "ilb", "aks", "pe", "kv", "sb", "ilbx", "aksx", "pex", "bastion", "sent", "defender", "policy", "devops", "ir"}
EST_REPL = {"pg", "pgx", "acr"}
SEQ = ["D1 Identidad y claves", "D2 Red y DNS", "D3 Datos y mensajería", "D4 Cómputo y herramientas", "D5 Servicios", "D6 Entrada pública", "D7 Validación funcional"]


def edge_cell(i, flujo, parent, tag):
    e = aristas[i]
    o, d, pts = res[i]
    col, gr, dash = FLUJO[flujo]
    gr = e["grosor"] or gr
    n1, n2 = nodos[e["a"]], nodos[e["b"]]

    def fr(p, n):
        l, t, r, b = n["card"]
        return ((p[0] - l) / (r - l), (p[1] - t) / (b - t))

    ex, ey = fr(pts[0], n1)
    nx, ny = fr(pts[-1], n2)
    st = (f"html=1;rounded=0;endArrow=block;endFill=1;endSize={6 if gr > 2 else 4};strokeColor={col};strokeWidth={gr};{dash}"
          f"exitX={ex:.3f};exitY={ey:.3f};exitPerimeter=0;entryX={nx:.3f};entryY={ny:.3f};entryPerimeter=0;")
    puntos = "".join(f'<mxPoint x="{x}" y="{y}"/>' for x, y in pts[1:-1])
    cells.append(f'<mxCell id="e{i}_{tag}" value="" style="{st}" edge="1" parent="{parent}" source="n_{e["a"]}" target="n_{e["b"]}">'
                 f'<mxGeometry relative="1" as="geometry"><Array as="points">{puntos}</Array></mxGeometry></mxCell>')


def pill_cell(i, flujo, txt, tag):
    rect = pills.get(i)
    if not rect or not txt:
        return
    col = FLUJO[flujo][0]
    if len(txt) <= 3 and (txt.isdigit() or txt[0] == "S"):
        vertex(f"p{i}_{tag}", txt, f"ellipse;html=1;fillColor={col};strokeColor=#FFFFFF;strokeWidth=1.5;fontColor=#FFFFFF;fontStyle=1;fontSize=9;fontFamily=Helvetica;align=center;verticalAlign=middle;spacing=0;",
               (rect[0] + rect[2]) / 2 - 10, (rect[1] + rect[3]) / 2 - 10, 20, 20)
    else:
        w = len(txt) * 5.6 + 12
        vertex(f"p{i}_{tag}", txt, f"rounded=1;arcSize=50;html=1;fillColor=#FFFFFF;strokeColor={col};strokeWidth=1;fontColor={col};fontStyle=1;fontSize=9;fontFamily=Helvetica;align=center;verticalAlign=middle;",
               (rect[0] + rect[2]) / 2 - w / 2, (rect[1] + rect[3]) / 2 - 8.5, w, 17)


def estado(nid, mode):
    k = nid.split("_", 1)[1].rsplit("_", 1)[0] if nid.count("_") >= 2 else nid.split("_", 1)[1]
    if k in EST_ESPERA:
        return "ESPERA" if mode != "conm" else "ACTIVO"
    if k in EST_REPL:
        return "RÉPLICA" if mode != "conm" else ("ACTIVO" if k == "acr" else "PROMOVIDA")
    if k in ("bi",):
        return "APAGADO" if mode != "conm" else "REPRODUCIR"
    return None


def escenario(mode, parent, tag, solo_propias):
    global PAR
    PAR = parent
    sel = [i for i in sorted(res) if mode in aristas[i]["v"]]
    if solo_propias:
        sel = [i for i in sel if aristas[i]["v"].get("normal") != aristas[i]["v"].get("conm")]
    for i in sel:
        if aristas[i]["v"][mode][0] == "mut":
            edge_cell(i, "mut", parent, tag)
    # sombreado del sitio que no está en servicio
    if mode in ("unica", "normal"):
        x0, y0, x1, y1, ytop, yseq = REG["b"]
        vertex(f"dim_b_{tag}", "", f"rounded=0;html=1;fillColor=#FFFFFF;fillOpacity={55 if mode == 'normal' else 48};strokeColor=none;", x0 + 3, ytop, x1 - x0 - 6, yseq - 6 - ytop)
    if mode == "conm":
        x0, y0, x1, y1, ytop, yseq = REG["c"]
        vertex(f"dim_c_{tag}", "", "rounded=0;html=1;fillColor=#FFFFFF;fillOpacity=62;strokeColor=none;", x0 + 3, ytop, x1 - x0 - 6, y1 - ytop - 4)
        chips_derecha(x1 - 360, y0, ["CHILE CENTRAL NO DISPONIBLE · escenario de ensayo"], "#B71C1C", "#FFFFFF", "#FFFFFF", f"kx{tag}")
    for i in sel:
        f, p = aristas[i]["v"][mode]
        if f != "mut":
            edge_cell(i, f, parent, tag)
    for i in sel:
        f, p = aristas[i]["v"][mode]
        if f != "mut":
            pill_cell(i, f, p, tag)
    # estados de los nodos de Brasil
    for nid, n in nodos.items():
        if not nid.startswith("b_"):
            continue
        est = estado(nid, mode)
        if not est:
            continue
        bg, fg = TAGS[est]
        w = len(est) * 5.3 + 12
        l, t, r, b = n["card"]
        vertex(f"t_{nid}_{tag}", est, f"rounded=1;arcSize=30;html=1;fillColor={bg};strokeColor=#FFFFFF;strokeWidth=1;fontColor={fg};fontStyle=1;fontSize=8;fontFamily=Helvetica;align=center;verticalAlign=middle;spacing=0;",
               l + 3, t + 3, w, 14)
    # secuencia de arranque
    yseq = REG["b"][5]
    activo = mode == "conm"
    vertex(f"seqt_{tag}", "Orden de arranque en la conmutación:", "text;html=1;align=left;verticalAlign=middle;fontSize=10;fontStyle=1;fontFamily=Helvetica;fontColor=#0F5F53;whiteSpace=nowrap;", 560, yseq + 2, 230, 24)
    x = 800
    for k, t_ in enumerate(SEQ):
        w = len(t_) * 5.4 + 16
        fill, col = ("#0F7B6C", "#FFFFFF") if activo else ("#FFFFFF", "#0F5F53")
        vertex(f"seq{k}_{tag}", t_, f"rounded=1;arcSize=50;html=1;fillColor={fill};strokeColor=#0F7B6C;strokeWidth=1.5;fontColor={col};fontStyle=1;fontSize=9;fontFamily=Helvetica;align=center;verticalAlign=middle;",
               x, yseq + 3, w, 22)
        x += w + 8
    PAR = "1"


if MODE == "capas":
    PAR = "1"
    for i in sorted(res):
        v = aristas[i]["v"]
        if v.get("normal") and v.get("normal") == v.get("conm"):
            edge_cell(i, v["normal"][0], "1", "b")
            pill_cell(i, v["normal"][0], v["normal"][1], "b")
    escenario("normal", "lay_n", "n", True)
    escenario("conm", "lay_c", "c", True)
else:
    escenario(MODE, "1", MODE[0], False)

# título
vertex("titulo", "Arquitectura física general · recorrido de una petición por zonas, subredes y capas OSI",
       "text;html=1;align=center;verticalAlign=middle;fontSize=20;fontStyle=1;fontFamily=Helvetica;fontColor=#1A1A1A;", 300, 6, 1600, 28)
ESC = {"unica": "Chile Central, sitio principal; Brazil South, sitio secundario en espera", "normal": "Escenario: operación normal · Brazil South en espera y recibiendo copias", "conm": "Escenario: conmutación a Brazil South · Chile Central no disponible", "capas": "Escenario: operación normal (active la capa «Conmutación a Brasil» en draw.io)"}[MODE]
vertex("subtitulo", "Los números siguen el dato salto a salto; la matriz inferior explica, por capa OSI, qué viaja, cómo se cifra y qué lo protege. " + ESC + " · Cuatro hosts por tienda",
       "text;html=1;align=center;verticalAlign=middle;fontSize=10.5;fontFamily=Helvetica;fontColor=#333333;", 200, 36, 1800, 20)

# leyenda superior izquierda
lx, ly = 15, 70
vertex("g_leyenda", "Cómo leer la figura", "rounded=1;arcSize=3;html=1;fillColor=#FFFFFF;strokeColor=#9AA3AE;strokeWidth=1;verticalAlign=top;align=left;spacingLeft=8;fontStyle=1;fontSize=10.5;fontFamily=Helvetica;fontColor=#1A1A1A;", lx, ly, 465, 182)
fl = [("dig", "Canal digital → borde → entrada"), ("tie", "Tienda / DC → túnel IPsec → hub"),
      ("com", "Camino común → AKS → datos"), ("x", "Cruce autorizado por X-01"),
      ("rep", "Copia continua Chile → Brasil"), ("dr", "Conmutación y túneles alternos"),
      ("mut", "Ruta en espera (sin tráfico)"), ("sec", "Dependencia · identidad · admin")]
for k, (f, t) in enumerate(fl):
    col, gr, dash = FLUJO[f]
    xx = lx + (0 if k % 2 == 0 else 232)
    yy = ly + 34 + (k // 2) * 18
    cells.append(f'<mxCell id="lf{k}" value="" style="html=1;endArrow=block;endFill=1;endSize=4;strokeColor={col};strokeWidth={min(gr, 3)};{dash}" edge="1" parent="1">'
                 f'<mxGeometry relative="1" as="geometry"><mxPoint x="{xx + 10}" y="{yy + 8}" as="sourcePoint"/><mxPoint x="{xx + 46}" y="{yy + 8}" as="targetPoint"/></mxGeometry></mxCell>')
    vertex(f"lt{k}", t, "text;html=1;align=left;verticalAlign=middle;fontSize=9;fontFamily=Helvetica;fontColor=#1A1A1A;whiteSpace=nowrap;", xx + 52, yy, 175, 16)
yy = ly + 34 + 4 * 18 + 4
vertex("lo_t", "Insignia en cada nodo = capa OSI en que actúa:", "text;html=1;align=left;verticalAlign=middle;fontSize=9;fontStyle=1;fontFamily=Helvetica;whiteSpace=nowrap;", lx + 8, yy, 300, 14)
for k, (cap, txt) in enumerate((("L7", "L7"), ("L4", "L4"), ("L3", "L3"), ("L2", "L2"), ("L1", "L1"), ("L3-7", "L3-7"))):
    c = OSI_COL[cap]
    bw = 30 if cap != "L3-7" else 44
    vertex(f"lb{k}", txt, f"rounded=1;arcSize=30;html=1;fillColor={c};strokeColor=#FFFFFF;fontColor=#FFFFFF;fontStyle=1;fontSize=9;fontFamily=Helvetica;align=center;verticalAlign=middle;",
           lx + 10 + k * 40 + (6 if k == 5 else 0), yy + 16, bw, 15)
vertex("lo_t2", "Estado en Brazil South:", "text;html=1;align=left;verticalAlign=middle;fontSize=9;fontStyle=1;fontFamily=Helvetica;whiteSpace=nowrap;", lx + 8, yy + 36, 200, 14)
xx = lx + 10
for k, est in enumerate(("ESPERA", "RÉPLICA", "APAGADO", "ACTIVO", "PROMOVIDA", "REPRODUCIR")):
    bg, fg = TAGS[est]
    w = len(est) * 5.3 + 12
    vertex(f"lg{k}", est, f"rounded=1;arcSize=30;html=1;fillColor={bg};strokeColor=#FFFFFF;fontColor={fg};fontStyle=1;fontSize=8;fontFamily=Helvetica;align=center;verticalAlign=middle;spacing=0;", xx, yy + 52, w, 14)
    xx += w + 6

# --------------------------------------------------------------------------- matriz OSI por salto
HOPS = [
    ("1", "Cliente → DNS público", "Internet", "dig",
     ["Consulta DNS del canal", "—", "—", "UDP/TCP 53", "IP pública del resolutor", "Acceso del usuario", "Fuera de la administración de Ancoa"]),
    ("2", "Cliente → Front Door", "Internet → borde", "dig",
     ["HTTPS · WAF de borde · host y autenticación del canal", "TLS hasta el borde global", "Sesión y token del canal (Entra External ID)", "TCP 443", "IP pública", "Operador de acceso", "Redes de operadores"]),
    ("3", "Front Door → Application Gateway", "Borde → Chile", "dig",
     ["Origen privado, sondeo de salud y certificado válidos", "TLS hacia el origen (re-cifrado)", "—", "TCP 443", "Private Link: el origen no expone IP pública", "Red de Microsoft", "Centro de datos Azure"]),
    ("4", "Application Gateway → APIM", "Chile · VNet aplicación", "com",
     ["Listener, ruta API y WAF regional", "TLS 443, certificados propios", "—", "TCP 443", "Subredes propias · NSG", "Red virtual Azure", "Centro de datos Azure"]),
    ("5", "APIM → balanceador interno", "Chile · VNet aplicación", "com",
     ["Políticas, cuotas y contrato por ámbito", "TLS 443", "Token validado contra Entra (JWT)", "TCP 443", "NSG y UDR · retorno simétrico", "Red virtual Azure", "Centro de datos Azure"]),
    ("6", "Balanceador → pods BIZ", "Chile · subred AKS", "com",
     ["Service y pods seleccionados · sondeos", "TLS según configuración", "—", "Reparto L4 por VIP (Standard LB)", "CNI Overlay · NetworkPolicy", "Nodos en varias zonas", "Hosts del clúster"]),
    ("7", "AKS → Private Endpoint → PostgreSQL", "Chile · datos", "com",
     ["Rol y base propios del servicio", "TLS", "Workload Identity de la carga", "TCP 5432", "Private Endpoint, sin IP pública", "Red virtual Azure", "Almacenamiento administrado"]),
    ("8", "AKS Retail → X-01", "Chile · frontera", "x",
     ["Contrato «compra autorizable», finalidad y datos mínimos", "HTTPS privado", "Identidad X-01", "TCP 443", "Listener contractual · sin ruta R↔F", "Red virtual Azure", "Centro de datos Azure"]),
    ("9", "X-01 → entrada Filial", "Chile · frontera → Filial", "x",
     ["Respuesta limitada · sin credencial de base F", "HTTPS privado", "Identidad X-01", "TCP 443", "Entrada financiera autorizada", "Red virtual Azure", "Centro de datos Azure"]),
    ("10", "Chile → Brazil South (copias)", "Chile → Brasil", "dr",
     ["Réplica o restauración según el producto", "TLS y claves propias por ámbito", "—", "TCP 5432 / 443", "Red de Azure entre regiones · sin enlace R↔F", "Red de Microsoft", "Centros de datos Azure"]),
    ("11", "Front Door → entrada DR", "Borde → Brasil", "dr",
     ["Sondeos de salud y selección de origen", "TLS", "—", "TCP 443", "Private Link a la entrada de recuperación", "Red de Microsoft", "Centro de datos Azure"]),
    ("S1", "Caja / mesón → switch", "On-premise · tienda", "tie",
     ["API local cifrada · diario durable", "Cifrado de API local (por definir)", "Identidad nominal; 802.1X en Wi-Fi", "TCP", "VRF propio de cada negocio", "VLAN 10/11/12 (R) · 20/21/22 (F)", "Cat 6 LSZH · fibra OS2"]),
    ("S2", "Switch → router SD-WAN", "On-premise · tienda", "tie",
     ["—", "—", "—", "—", "ACL y VRF-R / VRF-F", "Troncal VLAN", "Cobre o fibra"]),
    ("S3", "Router → VPN Gateway", "Tienda / DC → Chile", "tie",
     ["—", "IPsec (túnel por ámbito)", "IKE autentica el túnel", "UDP 500/4500 (NAT-T)", "IP del operador → GatewaySubnet", "Dos accesos y operadores", "CPE y enlaces WAN"]),
    ("S4", "VPN → firewall → entrada", "Chile · hub", "tie",
     ["Inspección Premium según política", "—", "—", "Filtro por política", "UDR y retorno simétrico · sin acceso libre a bases", "Red virtual Azure", "Centro de datos Azure"]),
]
CAPAS = [("L7", "Aplicación", "L7"), ("L6", "Presentación · cifrado", "L7"), ("L5", "Sesión · identidad", "L7"),
         ("L4", "Transporte", "L4"), ("L3", "Red · aislamiento", "L3"), ("L2", "Enlace", "L2"), ("L1", "Físico", "L1")]
my0 = yb_on + 30
rowlab_w = 150
cw = (W - 30 - rowlab_w) / len(HOPS)
vertex("m_titulo", "Encapsulación del dato por salto · qué viaja y qué lo protege en cada capa OSI",
       "rounded=0;html=1;fillColor=#263238;strokeColor=#263238;fontColor=#FFFFFF;fontStyle=1;fontSize=12;align=left;spacingLeft=10;verticalAlign=middle;fontFamily=Helvetica;",
       15, my0, W - 30, 26)
hy = my0 + 26
HZ = {"dig": "#C62828", "tie": "#2E7D32", "com": "#1A237E", "x": "#E07B00", "dr": "#168F80"}
vertex("m_h0", "Salto · zona", "rounded=0;html=1;fillColor=#ECEFF1;strokeColor=#B0BEC5;fontStyle=1;fontSize=9;fontFamily=Helvetica;align=left;spacingLeft=6;verticalAlign=middle;", 15, hy, rowlab_w, 62)
for j, (num, tr, zona, fl_, cap) in enumerate(HOPS):
    x = 15 + rowlab_w + j * cw
    col = HZ[fl_]
    vertex(f"m_hh{j}", f"{num} · {tr}\n{zona}", f"rounded=0;html=1;fillColor={col};strokeColor=#FFFFFF;fontColor=#FFFFFF;fontStyle=1;fontSize=8.5;fontFamily=Helvetica;align=center;verticalAlign=middle;whiteSpace=wrap;", x, hy, cw, 62)
CH = 50
for r, (cod, nom, ck) in enumerate(CAPAS):
    y = hy + 62 + r * CH
    c = OSI_COL[ck]
    vertex(f"m_r{r}", f"{cod} · {nom}", f"rounded=0;html=1;fillColor={c};strokeColor=#FFFFFF;fontColor=#FFFFFF;fontStyle=1;fontSize=9.5;fontFamily=Helvetica;align=left;spacingLeft=8;verticalAlign=middle;", 15, y, rowlab_w, CH)
    for j, (num, tr, zona, fl_, cap) in enumerate(HOPS):
        x = 15 + rowlab_w + j * cw
        t = cap[r]
        vacio = t == "—"
        vertex(f"m_c{r}_{j}", t, f"rounded=0;html=1;whiteSpace=wrap;fillColor={'#FAFAFA' if vacio else '#FFFFFF'};strokeColor=#CFD8DC;fontSize=8.5;fontColor={'#9AA3AE' if vacio else '#1A1A1A'};fontFamily=Helvetica;align=center;verticalAlign=middle;spacing=3;", x, y, cw, CH)
yend = hy + 62 + len(CAPAS) * CH
pie = ("Retail: azul · Filial: violeta · X-01: naranja · Insignia: capa OSI principal del nodo (el firewall actúa de L3 a L7). Los marcos de contorno grueso separan zonas reales: Internet y socios, borde global, "
       "Chile Central, Brazil South y on-premise; las cajas punteadas son subredes; las cajas con borde continuo son VNets o servicios PaaS fuera de la VNet.\n"
       "Brazil South es el sitio secundario (activo-pasivo templado): repite la pila de Chile por ámbito, recibe copias continuas y entra en servicio por conmutación de Front Door o túnel alternativo. Los 4 gateways BI se reproducen apagados; Redis Retail se reconstruye y no se agrega Redis Filial. Bloques IP: reservas de diseño.\n"
       "El cifrado de la API local de tienda, la conmutación y el RTO/RPO se acreditan con pruebas. Fuente: elaboración propia desde Bases, Caso 09, inventario físico integral (23-10-2026) y decisiones del usuario. Uso de IA Alto; diseño sujeto a pruebas, no es despliegue acreditado.")
vertex("pie", pie, "text;html=1;align=center;verticalAlign=top;fontSize=9.5;fontFamily=Helvetica;fontColor=#1A1A1A;whiteSpace=wrap;", 100, yend + 10, W - 200, 62)

H = int(yend + 90)
xml = ('<mxfile host="diagramas-ancoa" type="device"><diagram id="d1" name="Figura 4.52 flujo OSI">'
       f'<mxGraphModel dx="1200" dy="800" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1" pageWidth="{W}" pageHeight="{H}" background="#FFFFFF" math="0" shadow="0">'
       f'<root>{"".join(cells)}</root></mxGraphModel></diagram></mxfile>')
open(sys.argv[1] if len(sys.argv) > 1 else "fig2.drawio", "w", encoding="utf-8").write(xml)
print("lienzo", W, H, "| Chile", yb_c, "Brasil", yb_b, "matriz y", my0)
