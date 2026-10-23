#!/usr/bin/env python3
"""Arquitectura física general, lectura de arriba hacia abajo.

Usuarios arriba; debajo las zonas por las que cruza una petición: on-premise, Internet y operadores WAN,
Azure Chile Central (detalle) y Azure Brazil South (réplica resumida).
Uso: python3 este.py salida.drawio
"""
import heapq
import html
import math
import sys

G = 10
ICON = 44
W = 1940
CARD_HALF = 60
LH = 12.5

AZ = "image;aspect=fixed;html=1;image=img/lib/azure2/"
CI = "aspect=fixed;html=1;fillColor=%s;strokeColor=#FFFFFF;shape=mxgraph.cisco."
IC = {
    "users": AZ + "identity/Users.svg", "entra": AZ + "identity/Azure_Active_Directory.svg",
    "fd": AZ + "networking/Front_Doors.svg", "ag": AZ + "networking/Application_Gateways.svg",
    "apim": AZ + "integration/API_Management_Services.svg", "ilb": AZ + "networking/Load_Balancers.svg",
    "aks": AZ + "containers/Kubernetes_Services.svg", "pg": AZ + "databases/Azure_Database_PostgreSQL_Server.svg",
    "vpn": AZ + "networking/Virtual_Network_Gateways.svg", "fw": AZ + "networking/Firewalls.svg",
    "pe": AZ + "networking/Private_Endpoint.svg", "bastion": AZ + "networking/Bastions.svg",
    "sent": AZ + "security/Azure_Sentinel.svg", "defender": AZ + "security/Azure_Defender.svg",
    "acr": AZ + "containers/Container_Registries.svg", "dns": AZ + "networking/DNS_Zones.svg",
    "dr": AZ + "other/Backup_Vault.svg", "phone": CI % "#005073" + "modems_and_phones.cell_phone",
    "cloud": "aspect=fixed;html=1;fillColor=#5B6573;strokeColor=none;shape=mxgraph.azure.cloud",
    "router": CI % "#005073" + "routers.router", "switch": CI % "#005073" + "switches.layer_3_switch",
    "ap": CI % "#005073" + "misc.access_point", "pc": CI % "#005073" + "computers_and_peripherals.workstation",
    "host": CI % "#005073" + "servers.fileserver", "fwl": CI % "#B71C1C" + "security.ios_firewall",
    "xhost": CI % "#C25A10" + "security.ios_firewall", "cpe": CI % "#005073" + "modems_and_phones.modem",
    "printer": CI % "#005073" + "computers_and_peripherals.printer", "dc": CI % "#005073" + "servers.storage_server",
    "mix": CI % "#5B6573" + "misc.access_point",
}
OSI_COL = {"L1": "#6D4C41", "L2": "#E65100", "L3": "#1565C0", "L4": "#00897B", "L7": "#7B1FA2", "L3-7": "#37474F"}

nodos, clusters, aristas = {}, [], []


def N(id_, cx, cy, texto, icono, osi=None):
    n = len(texto.split("\n"))
    bottom = int(math.ceil((cy + 26 + LH * n + 6) / 10.0) * 10)
    nodos[id_] = dict(id=id_, cx=cx, cy=cy, texto=texto, icono=icono, osi=osi, card=(cx - CARD_HALF, cy - 34, cx + CARD_HALF, bottom))


def C(id_, label, kind, miembros=None, rect=None, pad=(14, 34, 14, 10), size=10.5, align="left"):
    clusters.append(dict(id=id_, label=label, kind=kind, miembros=miembros or [], rect=rect, pad=pad, size=size, align=align))


def E(a, b, flujo, pill=None, grosor=None):
    aristas.append(dict(a=a, b=b, flujo=flujo, pill=pill, grosor=grosor))


# --------------------------------------------------------------------------- grilla fija
# columnas: Retail | centro | Filial (mismas x en on-premise y en Azure); filas con el mismo y en todas las zonas
Wc = 1940
CX_R, CX_C, CX_F = 415, 915, 1415
COLR = (160, 670)
COLC = (710, 1120)
COLF = (1160, 1670)
ZX = (30, 1800)
RS = (250, 415, 580)                          # on-premise Retail: slots A, B, C
FS = (1580, 1415, 1250)                       # on-premise Filial espejo: A', B', C'
CS = (830, 1000)                              # centro (dos tarjetas)
R2 = (330, 500)                               # Chile Retail: exterior, interior
X2 = (830, 1000)
F2 = (1500, 1330)                             # Chile Filial: exterior, interior
YD, YA, YM, YP = 330, 480, 630, 780           # on-premise: dispositivos, acceso, servidores, perímetro
Y_NET = 1030
YH, YE, YC, YDT = 1295, 1445, 1595, 1745      # Azure: hub, entrada, cómputo, datos
Y_DR = 2000
Y_USR = 130

# usuarios
N("personal", RS[0], Y_USR, "Personal de tienda\ncajas, mesón y móviles", "users", "L7")
N("cliente", 1840, Y_USR, "Cliente web / app\nmóvil o navegador", "phone", "L7")
# on-premise Retail
N("caja", RS[0], YD, "Caja 1 · POS\nVLAN 10", "pc", "L7")
N("tpv", RS[1], YD, "TPV de pago\nVLAN 10", "printer", "L7")
N("movr", RS[2], YD, "Terminal móvil sala\nWi-Fi 802.1X", "phone", "L7")
N("swr", RS[1], YA, "Switch LAN Retail\npar · VRF-R", "switch", "L2")
N("apr", RS[2], YA, "AP Wi-Fi corporativo\nVLAN 12", "ap", "L2")
N("hr2", RS[0], YM, "SIT-xx-R-02\nréplica local", "host", "L7")
N("hr1", RS[1], YM, "SIT-xx-R-01\nventa y diario", "host", "L7")
N("fwr", RS[2], YP, "Firewall / SD-WAN\nRetail · HA", "fwl", "L3-7")
# on-premise Filial (espejo)
N("mes", FS[0], YD, "Mesón financiero\nVLAN 20", "pc", "L7")
N("movf", FS[2], YD, "Terminal móvil\nfinanciero", "phone", "L7")
N("swf", FS[1], YA, "Switch LAN Filial\npar · VRF-F", "switch", "L2")
N("apf", FS[2], YA, "AP Wi-Fi financiero\nVLAN 22", "ap", "L2")
N("hf2", FS[0], YM, "SIT-xx-F-02\nréplica F", "host", "L7")
N("hf1", FS[1], YM, "SIT-xx-F-01\nlibro F", "host", "L7")
N("xl", FS[2], YM, "X-01 local\n2 instancias · VLAN 23", "xhost", "L7")
N("fwf", FS[2], YP, "Firewall / SD-WAN\nFilial · HA", "fwl", "L3-7")
# centro on-premise
N("aux", CS[0], YA, "Segmentos auxiliares\nVLAN 40/50/60/70", "mix", "L2")
N("dc", CS[1], YA, "DC / CD conservados\nintegración por contrato", "dc", "L7")
N("cpeA", CS[0], YP, "CPE operador A", "cpe", "L1")
N("cpeB", CS[1], YP, "CPE operador B", "cpe", "L1")
# Internet y operadores
N("opA", CS[0], Y_NET, "Operador WAN A\nIPsec / Internet", "cloud")
N("opB", CS[1], Y_NET, "Operador WAN B\nIPsec / Internet", "cloud")
N("dns", FS[2], Y_NET, "DNS público\nresuelve el canal", "dns", "L7")
N("entra", FS[1], Y_NET, "Entra ID\nExternal ID · PIM", "entra", "L7")
N("fd", FS[0], Y_NET, "Front Door + WAF\nbalanceo L7 global", "fd", "L7")
# Chile: Retail (cadena en serpiente: VPN → FW ↓ AGW → APIM ↓ ILB → AKS ↓ PE → PG)
N("vpn_r", R2[0], YH, "VPN Gateway\nIPsec · IKE", "vpn", "L3")
N("fw_r", R2[1], YH, "Azure Firewall\nPremium · UDR", "fw", "L3-7")
N("apim_r", R2[0], YE, "API Management\nJWT · cuotas", "apim", "L7")
N("ag_r", R2[1], YE, "Application Gateway\nbalanceo L7 · WAF", "ag", "L7")
N("ilb_r", R2[0], YC, "Load Balancer interno\nbalanceo L4 · VIP", "ilb", "L4")
N("aks_r", R2[1], YC, "AKS Retail\nSYS·BIZ·INT·STATE·OPS", "aks", "L7")
N("pg_r", R2[0], YDT, "PostgreSQL Retail\nTLS 5432 · propio", "pg", "L7")
N("pe_r", R2[1], YDT, "Private Endpoint\nsin IP pública", "pe", "L3")
# Chile: Filial (espejo)
N("vpn_f", F2[0], YH, "VPN Gateway\nIPsec · IKE", "vpn", "L3")
N("fw_f", F2[1], YH, "Azure Firewall\nPremium · UDR", "fw", "L3-7")
N("apim_f", F2[0], YE, "API Management\nJWT · cuotas", "apim", "L7")
N("ag_f", F2[1], YE, "Application Gateway\nbalanceo L7 · WAF", "ag", "L7")
N("ilb_f", F2[0], YC, "Load Balancer interno\nbalanceo L4 · VIP", "ilb", "L4")
N("aks_f", F2[1], YC, "AKS Filial\nSYS·BIZ·INT·STATE·OPS", "aks", "L7")
N("pg_f", F2[0], YDT, "PostgreSQL Filial\nTLS 5432 · propio", "pg", "L7")
N("pe_f", F2[1], YDT, "Private Endpoint\nsin IP pública", "pe", "L3")
# Chile: centro = transversal (arriba) y frontera X-01 (abajo)
N("bastion", X2[0], YH, "Azure Bastion\nMFA/PIM", "bastion", "L7")
N("sent", X2[1], YH, "Log Analytics\nSentinel R/F/X", "sent", "L7")
N("defender", X2[0], YE, "Defender · Policy\npostura y control", "defender", "L7")
N("acr", X2[1], YE, "Registry + Pipelines\nimágenes por digest", "acr", "L7")
N("ilb_x", X2[0], YC, "Entrada privada X-01\nlistener contractual", "ilb", "L4")
N("aks_x", X2[1], YC, "AKS-X · X-01\ncontrol y bitácora", "aks", "L7")
N("pg_x", X2[0], YDT, "pg-x01\nbitácora propia", "pg", "L7")
N("pe_x", X2[1], YDT, "Private Endpoint X\nsin IP pública", "pe", "L3")
# Brasil: réplica resumida, alineada bajo cada base de datos
N("dr_r", R2[0], Y_DR, "Retail DR\npila idéntica", "dr")
N("dr_x", X2[0], Y_DR, "X-01 DR\npila idéntica", "dr")
N("dr_f", F2[0], Y_DR, "Filial DR\npila idéntica", "dr")
N("dr_in", 1730, Y_DR, "Entrada DR\nApp Gateway · APIM", "dr")

# --------------------------------------------------------------------------- zonas (rectángulos explícitos)
def top(cy):
    return cy - 60


def bot(cy):
    return cy + 80


C("z_usr", "USUARIOS Y CANALES", "zusr", rect=(30, 60, 1910, 200))
C("z_onp", "ON-PREMISE · tienda tipo SIT-xx · cuatro hosts por tienda", "zonp", rect=(ZX[0], 215, ZX[1], 890), size=12.5)
C("o_r", "Retail · VRF-R · racks 1 y 3", "sr", rect=(COLR[0], 255, COLR[1], 868), size=10.5)
C("o_c", "Compartido de sitio · rack 3", "sg", rect=(COLC[0], 255, COLC[1], 868), size=10.5)
C("o_f", "Filial · VRF-F · racks 2 y 3", "sf", rect=(COLF[0], 255, COLF[1], 868), size=10.5)
C("z_net", "INTERNET Y OPERADORES WAN", "znet", rect=(ZX[0], 915, ZX[1], 1130), size=12.5)
C("n_wan", "Operadores WAN · dos accesos", "sg", rect=(COLC[0], 972, COLC[1], 1116))
C("n_borde", "Borde global Azure · canal digital", "sb", rect=(1170, 972, 1660, 1116))
CT, CB = YH - 80, YDT + 102
C("z_chile", "AZURE · CHILE CENTRAL · SITIO PRINCIPAL · producción R / F / X", "zchile", rect=(ZX[0], CT - 65, ZX[1], CB + 22), size=12.5)
C("col_r", "Ámbito Retail · 10.64.0.0/16", "cr", rect=(COLR[0], CT, COLR[1], CB))
C("col_c", "Transversal de seguridad y frontera X-01 · 10.66.0.0/16", "cc", rect=(COLC[0], CT, COLC[1], CB))
C("col_f", "Ámbito Filial · 10.65.0.0/16", "cf", rect=(COLF[0], CT, COLF[1], CB))
for p_, (xa, xb), col in (("r", (COLR[0] + 15, COLR[1] - 15), "r"), ("f", (COLF[0] + 15, COLF[1] - 15), "f")):
    C(f"c_hub_{p_}", "VNet hub · GatewaySubnet y AzureFirewallSubnet", "sub", rect=(xa, top(YH) + 8, xb, bot(YH)), size=9)
    C(f"c_app_{p_}", "VNet aplicación · subredes de APIM y entrada", "sub", rect=(xa, top(YE) + 8, xb, bot(YE)), size=9, align="right" if p_ == "f" else "left")
    C(f"c_aks_{p_}", "Subred de nodos AKS", "sub", rect=(xa, top(YC) + 8, xb, bot(YC)), size=9)
    C(f"c_dat_{p_}", "VNet de datos · PaaS administrado y Private Endpoint", "sub", rect=(xa, top(YDT) + 8, xb, bot(YDT)), size=9, align="right" if p_ == "f" else "left")
xa, xb = COLC[0] + 15, COLC[1] - 15
C("c_sec", "Seguridad, operación y entrega · instancias R/F/X", "strip", rect=(xa, top(YH) + 8, xb, bot(YE)), size=9.5)
C("c_aks_x", "Frontera X-01 · subred de nodos AKS-X", "subx", rect=(xa, top(YC) + 8, xb, bot(YC)), size=9)
C("c_dat_x", "Frontera X-01 · datos propios y Private Endpoint", "subx", rect=(xa, top(YDT) + 8, xb, bot(YDT)), size=9)
BR_T = CB + 22 + 36
C("z_br", "BRAZIL SOUTH · SECUNDARIO", "zbr", rect=(ZX[0], BR_T, ZX[1], BR_T + 215), size=12.5)

ZST = {
    "zusr": ("#F3F4F6", "#5F6368", 3.5, "", "#5F6368"), "zonp": ("#FFFAF0", "#7A4B00", 5, "", "#7A4B00"),
    "znet": ("#F3F4F6", "#5F6368", 3.5, "", "#5F6368"), "zchile": ("#F4F7FD", "#0B3D91", 5, "", "#0B3D91"),
    "zbr": ("#F6FBF9", "#0F7B6C", 5, "dashed=1;dashPattern=14 7;", "#2B8F80"),
}
SUBS = {
    "sr": ("#DCEBFA", "#2F78B7", 1.5, ""), "sf": ("#E9DFF5", "#7A55A5", 1.5, ""), "sg": ("#EEF0F3", "#8B9099", 1.4, ""),
    "sb": ("#E8F2FC", "#0078D4", 1.6, ""), "cr": ("#DCEBFA", "#2F78B7", 1.5, ""), "cf": ("#E9DFF5", "#7A55A5", 1.5, ""),
    "cc": ("#FDF1DE", "#D98A2B", 1.5, ""), "sub": ("#FFFFFF", "#5B6573", 1.0, "dashed=1;dashPattern=4 3;"),
    "subx": ("#FFFFFF", "#D98A2B", 1.2, "dashed=1;dashPattern=4 3;"), "strip": ("#EEF0F3", "#7B8794", 1.4, ""),
}
cl_id = {c["id"]: c for c in clusters}

# etiquetas de fila (mismo alto en on-premise y en Azure)
ROWLAB = [(YD, "Puestos y terminales"), (YA, "Acceso · Wi-Fi y switches"), (YM, "Servidores locales"), (YP, "Perímetro y CPE")]
ROWLAB_C = [(YH, "Hub de conectividad"), (YE, "Entrada y APIM"), (YC, "Cómputo AKS"), (YDT, "Datos y PaaS")]

# --------------------------------------------------------------------------- aristas
E("personal", "caja", "V", "1")
E("caja", "swr", "V", "2")
E("swr", "hr1", "V", "3")
E("hr1", "hr2", "V", "3b")
E("swr", "fwr", "V", "4")
E("fwr", "cpeA", "V", "5")
E("cpeA", "opA", "V", "6")
E("opA", "vpn_r", "V", "7")
E("vpn_r", "fw_r", "K", "8")
E("fw_r", "ag_r", "K", "9")
E("ag_r", "apim_r", "K", "10")
E("apim_r", "ilb_r", "K", "11")
E("ilb_r", "aks_r", "K", "12")
E("aks_r", "pe_r", "K", "13")
E("pe_r", "pg_r", "K")
E("pg_r", "dr_r", "R", "14")
E("cliente", "fd", "W", "W1")
E("fd", "ag_r", "W", "W2")
E("fd", "ag_f", "W", "W2")
E("aks_r", "ilb_x", "X", "X")
E("ilb_x", "aks_x", "X")
E("aks_x", "ag_f", "X", "X")
E("aks_x", "pe_x", "S")
E("pe_x", "pg_x", "S")
E("pg_x", "dr_x", "R", "14")
E("pg_f", "dr_f", "R", "14")
E("fd", "dr_in", "Z", "C")
E("opB", "vpn_f", "S")
E("vpn_f", "fw_f", "F")
E("fw_f", "ag_f", "F")
E("ag_f", "apim_f", "F")
E("apim_f", "ilb_f", "F")
E("ilb_f", "aks_f", "F")
E("aks_f", "pe_f", "F")
E("pe_f", "pg_f", "F")
E("tpv", "swr", "S")
E("movr", "apr", "S")
E("apr", "swr", "S")
E("mes", "swf", "S")
E("movf", "apf", "S")
E("apf", "swf", "S")
E("swf", "hf1", "S")
E("hf1", "hf2", "S")
E("swf", "fwf", "S")
E("fwf", "cpeB", "S")
E("cpeB", "opB", "S")

FLUJO = {
    "V": ("#2E7D32", 3.4, ""), "K": ("#1A237E", 3.4, ""), "W": ("#C62828", 3.2, ""), "X": ("#E07B00", 3.2, ""),
    "R": ("#0E7C6B", 3.6, ""), "S": ("#8A949E", 1.4, ""), "F": ("#3949AB", 2.0, ""), "Z": ("#168F80", 2.2, "dashed=1;dashPattern=8 4;"),
}

# --------------------------------------------------------------------------- obstáculos y enrutado
BAN = 26


def texto_w(c):
    return len(c["label"]) * c["size"] * 0.56 + 14


def header_rect(c):
    x0, y0, x1, y1 = c["rect"]
    w = texto_w(c)
    if c["kind"] in ZST:
        return (x0 + 10, y0 + 3, x0 + 10 + w, y0 + BAN - 3)
    if c.get("align") == "right":
        return (x1 - 8 - w, y0 + 3, x1 - 8, y0 + 21)
    return (x0 + 8, y0 + 3, x0 + 8 + w, y0 + 21)


OBS = []
for n in nodos.values():
    l, t, r, b = n["card"]
    OBS.append((l - 5, t - 5, r + 5, b + 5, n["id"]))
for c in clusters:
    if c["id"] == "z_usr":
        l, t, r, b = header_rect(c)
        OBS.append((l - 4, t - 2, r + 4, b + 2, "hdr_" + c["id"]))
        continue
    l, t, r, b = header_rect(c)
    OBS.append((l - 4, t - 2, r + 4, b + 2, "hdr_" + c["id"]))

for yy_, t_ in ROWLAB:
    OBS.append((36, yy_ - 28, 156, yy_ + 4, "rowlab"))
for yy_, t_ in ROWLAB_C:
    OBS.append((36, yy_ - 28, 156, yy_ + 4, "rowlabc"))
Y_MAT = int(cl_id["z_br"]["rect"][3]) + 40
NX, NY = W // G + 2, (Y_MAT + 100) // G
bloq = [[False] * NX for _ in range(NY)]
for (l, t, r, b, tag) in OBS:
    for iy in range(max(0, int(t // G)), min(NY, int(b // G) + 1)):
        for ix in range(max(0, int(l // G)), min(NX, int(r // G) + 1)):
            if l < ix * G < r and t < iy * G < b:
                bloq[iy][ix] = True
for iy in range(NY):
    for ix in list(range(0, 3)) + list(range(NX - 3, NX)):
        bloq[iy][ix] = True
for ix in range(NX):
    for iy in range(0, 4):
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

BLOQ = ["c_hub_r", "c_app_r", "c_aks_r", "c_dat_r", "c_hub_f", "c_app_f", "c_aks_f", "c_dat_f", "c_sec", "c_aks_x", "c_dat_x", "n_wan", "n_borde"]


def contiene(rect):
    l, t, r, b = rect
    return {n["id"] for n in nodos.values() if n["card"][0] >= l and n["card"][2] <= r and n["card"][1] >= t and n["card"][3] <= b}


ZMIEMBROS = {z: contiene(cl_id[z]["rect"]) for z in BLOQ}
ZC = {}
for z in BLOQ:
    x0, y0, x1, y1 = cl_id[z]["rect"]
    for iy in range(int((y0 + 4) // G) + 1, int((y1 - 4) // G) + 1):
        for ix in range(int((x0 + 4) // G) + 1, int((x1 - 4) // G) + 1):
            if x0 + 4 < ix * G < x1 - 4 and y0 + 4 < iy * G < y1 - 4:
                ZC.setdefault((ix, iy), set()).add(z)

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
oh, ov, usados = set(), set(), set()


SIN_ENTRADA_ABAJO = {"ag_r", "ag_f"}


def puertos(nid, destino=False):
    n = nodos[nid]
    l, t, r, b = n["card"]
    cx, cy = n["cx"], n["cy"]
    res = []
    for side, d in zip(("right", "bottom", "left", "top"), range(4)):
        offs = (0, -20, 20) if side in ("right", "left") else (0, -30, 30)
        for off in offs:
            p = {"right": (r + 10, cy + off), "left": (l - 10, cy + off), "top": (cx + off, t - 10), "bottom": (cx + off, b + 10)}[side]
            ix, iy = int(p[0] // G), int(p[1] // G)
            if bloq[iy][ix] or (nid, side, off) in usados:
                continue
            if destino and side == "bottom" and nid in SIN_ENTRADA_ABAJO:
                continue
            res.append(dict(nid=nid, side=side, off=off, ix=ix, iy=iy, dir=d))
    return res


def ruta(src, dst):
    S, T = puertos(src), puertos(dst, True)
    if not S or not T:
        return None
    perm = {z for z in BLOQ if src in ZMIEMBROS[z] or dst in ZMIEMBROS[z]}
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
            zc = ZC.get((jx, jy))
            if zc and not zc <= perm:
                continue
            hz = nd in (0, 2)
            cst = 1.0 + (7.0 if nd != d else 0)
            # preferir bajar: las flechas que suben cuestan más
            if nd == 3:
                cst += 1.5
            if hz:
                if (jx, jy) in oh:
                    continue
                if (jx, jy) in ov:
                    cst += 14
                if (jx, jy) in bh:
                    cst += 6
            else:
                if (jx, jy) in ov:
                    continue
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
    return {"right": (r, n["cy"] + p["off"]), "left": (l, n["cy"] + p["off"]),
            "top": (n["cx"] + p["off"], t), "bottom": (n["cx"] + p["off"], b)}[p["side"]]


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


prio = {"F": -1, "V": 0, "K": 0, "W": 1, "X": 2, "R": 2, "Z": 3, "S": 4}
res, fallos = {}, []
orden = sorted(range(len(aristas)), key=lambda i: (prio[aristas[i]["flujo"]], dist(aristas[i])))
for i in orden:
    e = aristas[i]
    r = ruta(e["a"], e["b"])
    if r is None:
        fallos.append((e["a"], e["b"]))
        continue
    o, d, cam = r
    usados.add((o["nid"], o["side"], o["off"]))
    usados.add((d["nid"], d["side"], d["off"]))
    margen = 1 if e["flujo"] in ("V", "K", "W", "X", "R") else 0
    for k in range(len(cam) - 1):
        (x0, y0), (x1, y1) = cam[k], cam[k + 1]
        if y0 == y1:
            for xx in (x0 // G, x1 // G):
                for dy in range(-margen, margen + 1):
                    oh.add((xx, y0 // G + dy))
        else:
            for yy in (y0 // G, y1 // G):
                for dx in range(-margen, margen + 1):
                    ov.add((x0 // G + dx, yy))
    res[i] = (o, d, simplificar([punto_borde(o)] + cam + [punto_borde(d)]))
if fallos:
    print("SIN RUTA:", fallos, file=sys.stderr)


def cruza(p, q, r):
    l, t, rr, b = r
    (x0, y0), (x1, y1) = p, q
    if y0 == y1:
        return t < y0 < b and max(min(x0, x1), l) < min(max(x0, x1), rr)
    return l < x0 < rr and max(min(y0, y1), t) < min(max(y0, y1), b)


viol = set()
for i, (o, d, pts) in res.items():
    for k in range(len(pts) - 1):
        for (l, t, r, b, tag) in OBS:
            if cruza(pts[k], pts[k + 1], (l + 6, t + 6, r - 6, b - 6)):
                viol.add((aristas[i]["a"], aristas[i]["b"], tag))
print("violaciones:", len(viol), sorted(viol)[:8])
segs = [(i, pts[k], pts[k + 1]) for i, (o, d, pts) in res.items() for k in range(len(pts) - 1)]
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


def cruza_rect(p, q, rect):
    l, t, r, b = rect
    (x0, y0), (x1, y1) = p, q
    if y0 == y1:
        return t <= y0 <= b and max(min(x0, x1), l) < min(max(x0, x1), r)
    return l <= x0 <= r and max(min(y0, y1), t) < min(max(y0, y1), b)


# --------------------------------------------------------------------------- píldoras
pill_rects, pills = [], {}
for i in sorted(res):
    e = aristas[i]
    if not e["pill"]:
        continue
    o, d, pts = res[i]
    txt = e["pill"]
    pw = ph = 22
    cand = []
    for k in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[k], pts[k + 1]
        L_ = abs(x1 - x0) + abs(y1 - y0)
        if L_ < 28:
            continue
        for fr in (0.5, 0.4, 0.6, 0.3, 0.7, 0.2, 0.8):
            cand.append((-L_, x0 + (x1 - x0) * fr, y0 + (y1 - y0) * fr))
    cand.sort(key=lambda c: c[0])
    otros = [s_ for s_ in segs if s_[0] != i]
    puesto = False
    for _, cx, cy in cand:
        rect = (cx - pw / 2, cy - ph / 2, cx + pw / 2, cy + ph / 2)
        ok = True
        for (ol, ot, orr, ob, tag) in OBS:
            if tag in nodos:
                ol, ot, orr, ob = ol + 5, ot + 5, orr - 5, ob - 5
            if rect[0] < orr and rect[2] > ol and rect[1] < ob and rect[3] > ot:
                ok = False; break
        if ok:
            for (pl, pt, pr_, pb) in pill_rects:
                if rect[0] < pr_ + 2 and rect[2] > pl - 2 and rect[1] < pb + 2 and rect[3] > pt - 2:
                    ok = False; break
        if ok:
            for (i2, p0, p1) in otros:
                if cruza_rect(p0, p1, rect):
                    ok = False; break
        if ok:
            pill_rects.append(rect); pills[i] = rect; puesto = True
            break
    if not puesto:
        print("píldora sin lugar:", txt, e["a"], e["b"], file=sys.stderr)
        if cand:
            _, cx, cy = cand[0]
            rect = (cx - pw / 2, cy - ph / 2, cx + pw / 2, cy + ph / 2)
            pill_rects.append(rect); pills[i] = rect

# --------------------------------------------------------------------------- salida draw.io
def esc(t):
    return html.escape(t, quote=True).replace("\n", "&#xa;")


cells = ['<mxCell id="0"/>', '<mxCell id="1" parent="0"/>']


def vertex(id_, val, style, x, y, w, h):
    cells.append(f'<mxCell id="{id_}" value="{esc(val)}" style="{style}" vertex="1" parent="1">'
                 f'<mxGeometry x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')


def area(c):
    x0, y0, x1, y1 = c["rect"]
    return (x1 - x0) * (y1 - y0)


for c in sorted(clusters, key=lambda c: -area(c)):
    x0, y0, x1, y1 = c["rect"]
    k = c["kind"]
    if k in ZST:
        fill, stroke, sw, dash, banner = ZST[k]
        vertex(f"g_{c['id']}", "", f"rounded=1;arcSize=2;html=1;fillColor={fill};strokeColor={stroke};strokeWidth={sw};{dash}", x0, y0, x1 - x0, y1 - y0)
        vertex(f"b_{c['id']}", c["label"],
               f"rounded=0;html=1;fillColor={banner};strokeColor={banner};strokeWidth=1;fontColor=#FFFFFF;fontStyle=1;"
               f"fontSize={c['size']};align=left;spacingLeft=10;verticalAlign=middle;fontFamily=Helvetica;", x0 + 1, y0 + 1, x1 - x0 - 2, BAN - 1)
    else:
        fill, stroke, sw, dash = SUBS[k]
        vertex(f"g_{c['id']}", c["label"],
               f"rounded=1;arcSize=3;html=1;whiteSpace=nowrap;fillColor={fill};strokeColor={stroke};strokeWidth={sw};{dash}"
               f"verticalAlign=top;align={c.get('align', 'left')};spacingLeft=6;spacingRight=6;spacingTop=1;fontStyle={0 if k == 'sub' else 1};fontSize={c['size']};"
               f"fontColor=#2A2F36;fontFamily=Helvetica;", x0, y0, x1 - x0, y1 - y0)

for k, (yy_, t_) in enumerate(ROWLAB + ROWLAB_C):
    vertex(f"rl{k}", t_, "text;html=1;align=left;verticalAlign=middle;fontSize=9.5;fontStyle=1;fontFamily=Helvetica;fontColor=#5B6573;whiteSpace=wrap;", 38, yy_ - 28, 112, 32)
for n in nodos.values():
    l, t, r, b = n["card"]
    vertex(f"n_{n['id']}", n["texto"],
           "rounded=1;arcSize=8;html=1;fillColor=#FFFFFF;strokeColor=#8D97A5;strokeWidth=1.2;verticalAlign=bottom;align=center;"
           "fontSize=10;fontColor=#1A1A1A;fontFamily=Helvetica;spacingBottom=3;whiteSpace=nowrap;", l, t, r - l, b - t)
    cells.append(f'<mxCell id="i_{n["id"]}" value="" style="{IC[n["icono"]]};" vertex="1" parent="1">'
                 f'<mxGeometry x="{n["cx"] - ICON // 2}" y="{n["cy"] - ICON // 2 - 4}" width="{ICON}" height="{ICON}" as="geometry"/></mxCell>')
    if n["osi"]:
        c = OSI_COL[n["osi"]]
        bw = 30 if "-" not in n["osi"] else 44
        vertex(f"o_{n['id']}", n["osi"],
               f"rounded=1;arcSize=30;html=1;fillColor={c};strokeColor=#FFFFFF;strokeWidth=1;fontColor=#FFFFFF;fontStyle=1;fontSize=9;fontFamily=Helvetica;align=center;verticalAlign=middle;",
               r - bw - 3, t + 3, bw, 15)

for i in sorted(res):
    e = aristas[i]
    o, d, pts = res[i]
    col, gr, dash = FLUJO[e["flujo"]]
    gr = e["grosor"] or gr
    n1, n2 = nodos[e["a"]], nodos[e["b"]]

    def fr(p, n):
        l, t, r, b = n["card"]
        return ((p[0] - l) / (r - l), (p[1] - t) / (b - t))

    ex, ey = fr(pts[0], n1)
    nx, ny = fr(pts[-1], n2)
    st = (f"html=1;rounded=0;endArrow=block;endFill=1;endSize={6 if gr > 2.5 else 4};strokeColor={col};strokeWidth={gr};{dash}"
          f"exitX={ex:.3f};exitY={ey:.3f};exitPerimeter=0;entryX={nx:.3f};entryY={ny:.3f};entryPerimeter=0;")
    puntos = "".join(f'<mxPoint x="{x}" y="{y}"/>' for x, y in pts[1:-1])
    cells.append(f'<mxCell id="e{i}" value="" style="{st}" edge="1" parent="1" source="n_{e["a"]}" target="n_{e["b"]}">'
                 f'<mxGeometry relative="1" as="geometry"><Array as="points">{puntos}</Array></mxGeometry></mxCell>')

for i, rect in pills.items():
    e = aristas[i]
    col = FLUJO[e["flujo"]][0]
    vertex(f"p{i}", e["pill"], f"ellipse;html=1;fillColor={col};strokeColor=#FFFFFF;strokeWidth=1.5;fontColor=#FFFFFF;fontStyle=1;fontSize=9;fontFamily=Helvetica;align=center;verticalAlign=middle;spacing=0;",
           (rect[0] + rect[2]) / 2 - 11, (rect[1] + rect[3]) / 2 - 11, 22, 22)

# estados de Brasil
for nid, est, bg, fg in (("dr_r", "ESPERA · RÉPLICA", "#F9A825", "#3E2723"), ("dr_x", "ESPERA · RÉPLICA", "#F9A825", "#3E2723"),
                         ("dr_f", "ESPERA · RÉPLICA", "#F9A825", "#3E2723"), ("dr_in", "ESPERA", "#F9A825", "#3E2723")):
    l, t, r, b = nodos[nid]["card"]
    w = len(est) * 5.0 + 12
    vertex(f"t_{nid}", est, f"rounded=1;arcSize=30;html=1;fillColor={bg};strokeColor=#FFFFFF;strokeWidth=1;fontColor={fg};fontStyle=1;fontSize=8;fontFamily=Helvetica;align=center;verticalAlign=middle;spacing=0;", l + 3, t + 3, w, 14)

# chips de Brasil y secuencia de arranque
bx0, by0, bx1, by1 = cl_id["z_br"]["rect"]
x = bx1 - 10
for k, txt in enumerate(reversed(["RTO ≤ 4 h", "RPO ≤ 15 min en críticos", "50 VM de espera + 4 BI apagadas", "metas sujetas a ensayo"])):
    w = len(txt) * 5.3 + 16
    x -= w
    vertex(f"kb{k}", txt, "rounded=1;arcSize=50;html=1;fillColor=#FFFFFF;strokeColor=#FFFFFF;fontColor=#0F5F53;fontStyle=1;fontSize=9;fontFamily=Helvetica;align=center;verticalAlign=middle;", x, by0 + 5, w, 17)
    x -= 6
SEQ = ["D1 Identidad y claves", "D2 Red y DNS", "D3 Datos y mensajería", "D4 Cómputo y herramientas", "D5 Servicios", "D6 Entrada pública", "D7 Validación"]
vertex("seqt", "Orden de arranque en la conmutación:", "text;html=1;align=left;verticalAlign=middle;fontSize=10;fontStyle=1;fontFamily=Helvetica;fontColor=#0F5F53;whiteSpace=nowrap;", 60, by1 - 36, 230, 24)
x = 300
for k, t_ in enumerate(SEQ):
    w = len(t_) * 5.4 + 16
    vertex(f"seq{k}", t_, "rounded=1;arcSize=50;html=1;fillColor=#FFFFFF;strokeColor=#0F7B6C;strokeWidth=1.5;fontColor=#0F5F53;fontStyle=1;fontSize=9;fontFamily=Helvetica;align=center;verticalAlign=middle;", x, by1 - 35, w, 22)
    x += w + 8

# título y leyenda
vertex("titulo", "Arquitectura física general · recorrido de una petición, de los usuarios a las zonas",
       "text;html=1;align=center;verticalAlign=middle;fontSize=20;fontStyle=1;fontFamily=Helvetica;fontColor=#1A1A1A;", 200, 6, 1400, 28)
vertex("subtitulo", "Se lee de arriba hacia abajo: usuarios → on-premise → Internet y operadores → Azure Chile Central (producción) → Brazil South (réplica). Los números siguen una venta con tarjeta en tienda; el canal web entra por el borde global.",
       "text;html=1;align=center;verticalAlign=middle;fontSize=10.5;fontFamily=Helvetica;fontColor=#333333;", 100, 34, 1600, 20)
lx, ly = 530, 82
vertex("g_ley", "Cómo leer la figura", "rounded=1;arcSize=3;html=1;fillColor=#FFFFFF;strokeColor=#9AA3AE;strokeWidth=1;verticalAlign=top;align=left;spacingLeft=8;fontStyle=1;fontSize=10;fontFamily=Helvetica;fontColor=#1A1A1A;", lx, ly, 880, 118)
fl = [("V", "Venta POS: tienda → túnel IPsec (pasos 1–7)"), ("K", "Camino común en Azure (pasos 8–13)"), ("W", "Canal web / app (W1–W2)"),
      ("X", "Cruce autorizado por X-01"), ("R", "Copia continua hacia Brasil (14)"), ("Z", "Conmutación del canal web (C)")]
for k, (f, t) in enumerate(fl):
    col, gr, dash = FLUJO[f]
    xx = lx + 10 + (k % 3) * 285
    yy = ly + 26 + (k // 3) * 20
    cells.append(f'<mxCell id="lf{k}" value="" style="html=1;endArrow=block;endFill=1;endSize=4;strokeColor={col};strokeWidth={min(gr, 3)};{dash}" edge="1" parent="1">'
                 f'<mxGeometry relative="1" as="geometry"><mxPoint x="{xx}" y="{yy + 9}" as="sourcePoint"/><mxPoint x="{xx + 34}" y="{yy + 9}" as="targetPoint"/></mxGeometry></mxCell>')
    vertex(f"lt{k}", t, "text;html=1;align=left;verticalAlign=middle;fontSize=9;fontFamily=Helvetica;whiteSpace=nowrap;", xx + 40, yy, 240, 18)
vertex("lo_t", "Insignia = capa OSI del nodo:", "text;html=1;align=left;verticalAlign=middle;fontSize=9;fontStyle=1;fontFamily=Helvetica;whiteSpace=nowrap;", lx + 10, ly + 70, 170, 14)
for k, cap in enumerate(("L7", "L4", "L3", "L2", "L1", "L3-7")):
    bw = 30 if cap != "L3-7" else 44
    vertex(f"lb{k}", cap, f"rounded=1;arcSize=30;html=1;fillColor={OSI_COL[cap]};strokeColor=#FFFFFF;fontColor=#FFFFFF;fontStyle=1;fontSize=9;fontFamily=Helvetica;align=center;verticalAlign=middle;",
           lx + 190 + k * 38 + (4 if k == 5 else 0), ly + 69, bw, 15)
vertex("lo_t2", "Hosts: dos Retail y dos Filial por tienda; X-01 local dentro del par Filial. Brasil repite la pila de Chile (no se detalla servicio a servicio).",
       "text;html=1;align=left;verticalAlign=middle;fontSize=9;fontFamily=Helvetica;fontColor=#333333;whiteSpace=nowrap;", lx + 10, ly + 94, 860, 16)

# --------------------------------------------------------------------------- matriz OSI
HOPS = [
    ("1–2", "Caja POS → switch", "On-premise", "V",
     ["Venta o consulta por API local", "Cifrado de API local (por definir)", "Identidad nominal del puesto", "TCP", "VRF-R · ACL", "VLAN 10 · 802.1X en Wi-Fi", "Cat 6 LSZH · fibra OS2"]),
    ("3", "Switch → host R-01 (+ réplica R-02)", "On-premise", "V",
     ["API local, diario durable y réplica del diario", "Cifrado de la réplica (por definir)", "Fencing con testigo", "TCP", "VLAN 11 · VRF-R", "VLAN 11", "Cobre o fibra"]),
    ("4–6", "Switch → firewall → CPE → operador", "On-premise → WAN", "V",
     ["—", "—", "—", "Filtro por política", "ACL y NAT propios · dos accesos", "Troncal VRF-R", "CPE y enlace WAN A"]),
    ("7", "Operador → VPN Gateway", "WAN → Chile", "V",
     ["—", "IPsec (túnel por ámbito)", "IKE autentica el túnel", "UDP 500/4500 (NAT-T)", "IP del operador → GatewaySubnet", "Acceso del operador", "Enlace WAN"]),
    ("8–9", "VPN → Azure Firewall → App Gateway", "Chile · hub y entrada", "K",
     ["Inspección Premium y WAF regional", "TLS en la entrada", "—", "TCP 443", "UDR, NSG y retorno simétrico", "Red virtual Azure", "Centro de datos Azure"]),
    ("10–11", "App Gateway → APIM → balanceador", "Chile · aplicación", "K",
     ["Listener, ruta API, JWT y cuotas", "TLS 443", "Token validado contra Entra", "TCP 443", "Subredes propias · NSG", "Red virtual Azure", "Centro de datos Azure"]),
    ("12", "Balanceador → pods de negocio", "Chile · AKS", "K",
     ["Service y pods seleccionados", "TLS según configuración", "—", "Reparto L4 por VIP y sondeos", "CNI Overlay · NetworkPolicy", "Nodos en varias zonas", "Hosts del clúster"]),
    ("13", "AKS → Private Endpoint → PostgreSQL", "Chile · datos", "K",
     ["Rol y base propios del servicio", "TLS", "Workload Identity", "TCP 5432", "Private Endpoint sin IP pública", "Red virtual Azure", "Almacenamiento administrado"]),
    ("14", "PostgreSQL → Brazil South", "Chile → Brasil", "R",
     ["Réplica o restauración según el producto", "TLS y claves propias por ámbito", "—", "TCP 5432 / 443", "Red de Azure entre regiones · sin enlace R↔F", "Red de Microsoft", "Centros de datos Azure"]),
    ("W1", "Cliente → Front Door", "Internet → borde", "W",
     ["HTTPS · WAF de borde", "TLS hasta el borde global", "Sesión y token del canal", "TCP 443", "IP pública", "Operador de acceso", "Redes de operadores"]),
    ("W2", "Front Door → App Gateway", "Borde → Chile", "W",
     ["Origen privado y sondeo de salud", "TLS hacia el origen (re-cifrado)", "—", "TCP 443", "Private Link", "Red de Microsoft", "Centro de datos Azure"]),
    ("X", "AKS Retail → X-01 → Filial", "Chile · frontera", "X",
     ["Compra autorizable · datos mínimos", "HTTPS privado", "Identidad X-01", "TCP 443", "Listener contractual · sin ruta R↔F", "Red virtual Azure", "Centro de datos Azure"]),
]
CAPAS = [("L7", "Aplicación", "L7"), ("L6", "Presentación · cifrado", "L7"), ("L5", "Sesión · identidad", "L7"),
         ("L4", "Transporte", "L4"), ("L3", "Red · aislamiento", "L3"), ("L2", "Enlace", "L2"), ("L1", "Físico", "L1")]
HZ = {"V": "#2E7D32", "K": "#1A237E", "W": "#C62828", "X": "#E07B00", "R": "#0E7C6B"}
my0 = Y_MAT
rl = 150
cw = (W - 30 - rl) / len(HOPS)
vertex("m_titulo", "Encapsulación del dato por salto · qué viaja y qué lo protege en cada capa OSI", "rounded=0;html=1;fillColor=#263238;strokeColor=#263238;fontColor=#FFFFFF;fontStyle=1;fontSize=12;align=left;spacingLeft=10;verticalAlign=middle;fontFamily=Helvetica;", 15, my0, W - 30, 26)
hy = my0 + 26
vertex("m_h0", "Salto · zona", "rounded=0;html=1;fillColor=#ECEFF1;strokeColor=#B0BEC5;fontStyle=1;fontSize=9;fontFamily=Helvetica;align=left;spacingLeft=6;verticalAlign=middle;", 15, hy, rl, 62)
for j, (num, tr, zona, f_, cap) in enumerate(HOPS):
    vertex(f"m_hh{j}", f"{num} · {tr}\n{zona}", f"rounded=0;html=1;fillColor={HZ[f_]};strokeColor=#FFFFFF;fontColor=#FFFFFF;fontStyle=1;fontSize=8.5;fontFamily=Helvetica;align=center;verticalAlign=middle;whiteSpace=wrap;", 15 + rl + j * cw, hy, cw, 62)
CH = 50
for r, (cod, nom, ck) in enumerate(CAPAS):
    y = hy + 62 + r * CH
    vertex(f"m_r{r}", f"{cod} · {nom}", f"rounded=0;html=1;fillColor={OSI_COL[ck]};strokeColor=#FFFFFF;fontColor=#FFFFFF;fontStyle=1;fontSize=9.5;fontFamily=Helvetica;align=left;spacingLeft=8;verticalAlign=middle;", 15, y, rl, CH)
    for j, (num, tr, zona, f_, cap) in enumerate(HOPS):
        t = cap[r]
        vacio = t == "—"
        vertex(f"m_c{r}_{j}", t, f"rounded=0;html=1;whiteSpace=wrap;fillColor={'#FAFAFA' if vacio else '#FFFFFF'};strokeColor=#CFD8DC;fontSize=8.5;fontColor={'#9AA3AE' if vacio else '#1A1A1A'};fontFamily=Helvetica;align=center;verticalAlign=middle;spacing=3;", 15 + rl + j * cw, y, cw, CH)
yend = hy + 62 + len(CAPAS) * CH
vertex("pie", "Retail: azul · Filial: violeta · X-01: naranja. Zonas de contorno grueso: usuarios, on-premise, Internet y operadores, Azure Chile Central (principal) y Azure Brazil South (secundario, réplica resumida). Cajas punteadas: subredes; cajas continuas: VNets, racks y ámbitos.\n"
       "Brazil South repite la pila de Chile por ámbito, recibe copias continuas y entra en servicio por conmutación de Front Door o túnel alternativo; metas RTO/RPO sujetas a ensayo. Bloques IP: reservas de diseño. Cifrado de la API local de tienda: por definir.\n"
       "Fuente: elaboración propia desde Bases, Caso 09, inventario físico integral (23-10-2026) y decisiones del usuario. Uso de IA Alto; diseño sujeto a pruebas, no es despliegue acreditado.",
       "text;html=1;align=center;verticalAlign=top;fontSize=9.5;fontFamily=Helvetica;fontColor=#1A1A1A;whiteSpace=wrap;", 60, yend + 10, W - 120, 52)

H = int(yend + 80)
xml = ('<mxfile host="diagramas-ancoa" type="device"><diagram id="d1" name="Arquitectura física por zonas">'
       f'<mxGraphModel dx="1200" dy="800" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1" pageWidth="{W}" pageHeight="{H}" background="#FFFFFF" math="0" shadow="0">'
       f'<root>{"".join(cells)}</root></mxGraphModel></diagram></mxfile>')
open(sys.argv[1] if len(sys.argv) > 1 else "arq.drawio", "w", encoding="utf-8").write(xml)
print("lienzo", W, H)
for z in ("z_onp", "z_net", "z_chile", "z_br"):
    print(z, cl_id[z]["rect"])
