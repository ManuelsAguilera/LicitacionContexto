#!/usr/bin/env python3
"""Diagrama de red de prueba · tienda tipo SIT-xx.

Enlaces físicos en gris; los flujos de datos se dibujan como líneas concéntricas de color bajo cada enlace,
de modo que una bifurcación se ve donde el color se reparte entre enlaces distintos.
Uso: python3 este.py salida.drawio
"""
import heapq
import html
import math
import sys

G = 10
ICON = 44
W = 2140
CARD_HALF = 60
LH = 12.5

AZ = "image;aspect=fixed;html=1;image=img/lib/azure2/"
CI = "aspect=fixed;html=1;fillColor=%s;strokeColor=#FFFFFF;shape=mxgraph.cisco."
IC = {
    "fd": AZ + "networking/Front_Doors.svg", "ag": AZ + "networking/Application_Gateways.svg",
    "apim": AZ + "integration/API_Management_Services.svg", "aks": AZ + "containers/Kubernetes_Services.svg",
    "pg": AZ + "databases/Azure_Database_PostgreSQL_Server.svg", "vpn": AZ + "networking/Virtual_Network_Gateways.svg",
    "azfw": AZ + "networking/Firewalls.svg",
    "cloud": "aspect=fixed;html=1;fillColor=#5B6573;strokeColor=none;shape=mxgraph.azure.cloud",
    "router": CI % "#005073" + "routers.router", "switch": CI % "#005073" + "switches.layer_3_switch",
    "ap": CI % "#005073" + "misc.access_point", "pc": CI % "#005073" + "computers_and_peripherals.workstation",
    "host": CI % "#005073" + "servers.fileserver", "fw": CI % "#B71C1C" + "security.ios_firewall",
    "xhost": CI % "#C25A10" + "security.ios_firewall", "phone": CI % "#005073" + "modems_and_phones.cell_phone",
    "term": CI % "#005073" + "computers_and_peripherals.terminal", "cam": CI % "#005073" + "computers_and_peripherals.video_camera",
    "nvr": CI % "#005073" + "servers.storage_server", "cpe": CI % "#005073" + "modems_and_phones.modem",
    "printer": CI % "#005073" + "computers_and_peripherals.printer", "witness": CI % "#005073" + "servers.standard_host",
    "web": AZ + "general/Browser.svg",
}

nodos, clusters, enlaces = {}, [], []


def N(id_, cx, cy, texto, icono):
    n = len(texto.split("\n"))
    bottom = int(math.ceil((cy + 26 + LH * n + 6) / 10.0) * 10)
    nodos[id_] = dict(id=id_, cx=cx, cy=cy, texto=texto, icono=icono, card=(cx - CARD_HALF, cy - 34, cx + CARD_HALF, bottom))


def C(id_, label, kind, miembros=None, rect=None, pad=(14, 34, 14, 10), align="left", size=10.5):
    clusters.append(dict(id=id_, label=label, kind=kind, miembros=miembros or [], rect=rect, pad=pad, align=align, size=size))


# --------------------------------------------------------------------------- nodos
# nube e Internet (arriba)
N("cliente", 110, 130, "Cliente web / app\nmóvil o navegador", "phone")
N("pay", 270, 130, "Procesador de pagos\nexterno autorizado", "cloud")
N("fd", 470, 130, "Front Door + WAF\nbalanceo L7 global", "fd")
N("vpn", 640, 130, "VPN Gateway\nIPsec / IKE", "vpn")
N("azfw", 810, 130, "Azure Firewall\ninspección · UDR", "azfw")
N("ag", 980, 130, "Application Gateway\nbalanceo L7 · WAF", "ag")
N("apim", 1150, 130, "API Management\nJWT · cuotas", "apim")
N("aks", 1320, 130, "AKS (pods BIZ)\nbalanceo interno L4", "aks")
N("pg", 1490, 130, "PostgreSQL\nTLS 5432", "pg")
# operadores
N("opA", 780, 330, "Operador WAN A\nInternet / IPsec", "cloud")
N("opB", 1160, 330, "Operador WAN B\nInternet / IPsec", "cloud")
# rack 3: comunicaciones
N("cpeA", 780, 500, "CPE operador A", "cpe")
N("cpeB", 1160, 500, "CPE operador B", "cpe")
N("fwr1", 640, 650, "Firewall / SD-WAN\nRetail 1 · HA", "fw")
N("fwr2", 800, 650, "Firewall / SD-WAN\nRetail 2 · HA", "fw")
N("fwf1", 1180, 650, "Firewall / SD-WAN\nFilial 1 · HA", "fw")
N("fwf2", 1340, 650, "Firewall / SD-WAN\nFilial 2 · HA", "fw")
N("swr1", 640, 820, "Switch LAN Retail 1\nVLAN · VRF-R", "switch")
N("swr2", 800, 820, "Switch LAN Retail 2\nVLAN · VRF-R", "switch")
N("swaux", 970, 820, "Switch auxiliar\nVRF y ACL propias", "switch")
N("swf1", 1180, 820, "Switch LAN Filial 1\nVLAN · VRF-F", "switch")
N("swf2", 1340, 820, "Switch LAN Filial 2\nVLAN · VRF-F", "switch")
# Retail (izquierda)
N("pos1", 110, 580, "Caja 1 · POS\nVLAN 10", "pc")
N("pos2", 260, 580, "Caja 2 · POS\nVLAN 10", "pc")
N("tpv", 410, 580, "TPV de pago\nVLAN 10", "printer")
N("apr", 110, 780, "AP Wi-Fi corporativo\n802.1X · VLAN 12", "ap")
N("movr1", 260, 780, "Terminal móvil sala\napp React Native", "phone")
N("movr2", 410, 780, "Terminal móvil sala\napp React Native", "phone")
# Filial (derecha)
N("pc1", 1700, 580, "Mesón financiero 1\nVLAN 20", "pc")
N("pc2", 1850, 580, "Mesón financiero 2\nVLAN 20", "pc")
N("apf", 1700, 780, "AP Wi-Fi financiero\n802.1X · VLAN 22", "ap")
N("movf", 1850, 780, "Terminal móvil\nfinanciero", "phone")
# racks de servidores
N("hr1", 150, 1100, "SIT-xx-R-01\nventa y diario · VLAN 11", "host")
N("hr2", 310, 1100, "SIT-xx-R-02\nréplica local", "host")
N("wr", 450, 1100, "Testigo Retail\narbitraje del par", "witness")
N("hf1", 1620, 1100, "SIT-xx-F-01\nlibro F · VLAN 21", "host")
N("hf2", 1780, 1100, "SIT-xx-F-02\nréplica F", "host")
N("wf", 1940, 1100, "Testigo Filial\narbitraje del par", "witness")
N("xl1", 1620, 1250, "X-01 local #1\nVLAN 23", "xhost")
N("xl2", 1780, 1250, "X-01 local #2\nVLAN 23", "xhost")
# DMZ (prueba)
N("swdmz", 1070, 1060, "Switch DMZ\nVLAN 80 (prueba)", "switch")
N("aaa", 900, 1220, "AAA / RADIUS\nEAP-TLS", "host")
N("dns", 1070, 1220, "DNS forwarder · NTP\nproxy de salida", "host")
N("coll", 1240, 1220, "Collector de telemetría\ncon buffer local", "host")
# auxiliares (abajo)
N("apg", 150, 1480, "AP invitados\nVLAN 60", "ap")
N("movg1", 310, 1480, "Móvil de cliente\nSSID invitados", "phone")
N("cam", 560, 1480, "Cámaras IP\nVLAN 50", "cam")
N("nvr", 720, 1480, "NVR local\nretención 30 días", "nvr")
N("iot", 970, 1480, "Controlador IoT\nVLAN 40", "term")
N("lock", 1130, 1480, "Lockers y cerraduras\nsolo contrato Pedidos", "term")
N("admin", 1380, 1480, "Estación de gestión\nVLAN 70 · MFA/PIM", "pc")

# --------------------------------------------------------------------------- zonas
C("z_inet", "INTERNET · sin confianza", "inet", ["cliente", "pay"], pad=(14, 34, 14, 10))
C("z_azure", "AZURE · CHILE CENTRAL (resumen del camino hacia los datos)", "azure",
  ["fd", "vpn", "azfw", "ag", "apim", "aks", "pg"], pad=(16, 34, 16, 10))
C("z_wan", "OPERADORES WAN · dos accesos", "inet", ["opA", "opB"], pad=(60, 34, 60, 10))
C("rack3", "RACK 3 · comunicaciones · 24U (15U iniciales) · UPS A/B + PDU A/B", "rack",
  ["cpeA", "cpeB", "fwr1", "fwr2", "fwf1", "fwf2", "swr1", "swr2", "swaux", "swf1", "swf2"], pad=(30, 38, 30, 14), size=11)
C("v10", "Cajas · VLAN 10 · VRF-R", "vr", ["pos1", "pos2", "tpv"])
C("v12", "Wi-Fi corporativo Retail · VLAN 12 · 802.1X", "vr", ["apr", "movr1", "movr2"])
C("v20", "Mesón financiero · VLAN 20 · VRF-F", "vf", ["pc1", "pc2"])
C("v22", "Wi-Fi financiero · VLAN 22 · 802.1X", "vf", ["apf", "movf"])
C("rack1", "RACK 1 · servidores Retail · VLAN 11", "rack", ["hr1", "hr2", "wr"], pad=(20, 36, 20, 12))
C("rack2", "RACK 2 · servidores Filial · VLAN 21 · X-01 local en VLAN 23", "rack", ["hf1", "hf2", "wf", "xl1", "xl2"], pad=(20, 36, 20, 12))
C("dmz", "DMZ DE TIENDA (propuesta de prueba) · tercera pata del firewall Retail", "dmz", ["swdmz", "aaa", "dns", "coll"], pad=(24, 34, 24, 10))
C("v60", "Invitados · VLAN 60 · solo Internet", "vg", ["apg", "movg1"])
C("v50", "CCTV · VLAN 50 · solo NVR local", "vg", ["cam", "nvr"])
C("v40", "IoT / lockers · VLAN 40 · solo contrato Pedidos", "vg", ["iot", "lock"])
C("v70", "Gestión · VLAN 70", "vg", ["admin"], pad=(20, 34, 20, 10))

ZST = {  # relleno, borde, grosor, trazo, titulo
    "inet": ("#F3F4F6", "#5F6368", 3, ""), "azure": ("#E8F2FC", "#0078D4", 3.5, ""),
    "rack": ("#E4E8EC", "#37474F", 5, ""), "vr": ("#DCEBFA", "#2F78B7", 1.6, ""),
    "vf": ("#E9DFF5", "#7A55A5", 1.6, ""), "vg": ("#F1F2F4", "#8B9099", 1.5, ""),
    "dmz": ("#FDECEA", "#C62828", 3, "dashed=1;dashPattern=10 5;"),
}

cl_id = {c["id"]: c for c in clusters}


def rect_nodo(n):
    return n["card"]


def calc(c):
    if c["rect"]:
        return c["rect"]
    xs0, ys0, xs1, ys1 = [], [], [], []
    for m in c["miembros"]:
        r = calc(cl_id[m]) if m in cl_id else rect_nodo(nodos[m])
        xs0.append(r[0]); ys0.append(r[1]); xs1.append(r[2]); ys1.append(r[3])
    pl, pt, pr, pb = c["pad"]
    x0, y0, x1, y1 = min(xs0) - pl, min(ys0) - pt, max(xs1) + pr, max(ys1) + pb
    tw = len(c["label"]) * c["size"] * 0.56 + 24
    if x1 - x0 < tw:
        ex = tw - (x1 - x0)
        x0 -= ex / 2; x1 += ex / 2
    c["rect"] = (round(x0 / 10) * 10, round(y0 / 10) * 10, round(x1 / 10) * 10, round(y1 / 10) * 10)
    return c["rect"]


for c in clusters:
    calc(c)

# --------------------------------------------------------------------------- enlaces y flujos
# tipo: cu (cobre/fibra), wl (inalámbrico), den (denegado), x (contrato X-01), ha (par HA), ipsec, inet
def L(a, b, tipo="cu", lab=None):
    enlaces.append(dict(a=a, b=b, tipo=tipo, lab=lab, flows=[]))


L("cliente", "fd", "inet", "HTTPS")
L("pay", "opA", "inet", "HTTPS 443")
L("fd", "opB", "inet", "Internet · HTTPS 443")
L("vpn", "opA", "ipsec", "IPsec 500/4500")
L("vpn", "opB", "ipsec", "IPsec respaldo")
L("fd", "ag", "cu", "Private Link")
L("vpn", "azfw", "cu", None)
L("azfw", "ag", "cu", None)
L("ag", "apim", "cu", None)
L("apim", "aks", "cu", None)
L("aks", "pg", "cu", "PE · TLS 5432")
L("opA", "cpeA", "cu", None)
L("opB", "cpeB", "cu", None)
L("cpeA", "fwr1", "cu", "WAN A")
L("cpeB", "fwr2", "cu", "WAN B")
L("cpeA", "fwf1", "cu", "WAN A")
L("cpeB", "fwf2", "cu", "WAN B")
L("fwr1", "fwr2", "ha", "HA")
L("fwf1", "fwf2", "ha", "HA")
L("fwr1", "swr1", "cu", "trunk VRF-R")
L("fwr2", "swr2", "cu", "trunk VRF-R")
L("fwf1", "swf1", "cu", "trunk VRF-F")
L("fwf2", "swf2", "cu", "trunk VRF-F")
L("swr1", "swr2", "ha", "par")
L("swf1", "swf2", "ha", "par")
L("pos1", "swr1", "cu", "VLAN 10")
L("pos2", "swr1", "cu", "VLAN 10")
L("tpv", "swr1", "cu", "VLAN 10")
L("apr", "swr1", "cu", "VLAN 12 · PoE")
L("movr1", "apr", "wl", "Wi-Fi 802.1X")
L("movr2", "apr", "wl", "Wi-Fi 802.1X")
L("swr1", "hr1", "cu", "VLAN 11")
L("swr2", "hr2", "cu", "VLAN 11")
L("hr1", "hr2", "ha", "réplica · fencing")
L("wr", "swr2", "cu", "VLAN 11")
L("pc1", "swf1", "cu", "VLAN 20")
L("pc2", "swf1", "cu", "VLAN 20")
L("apf", "swf1", "cu", "VLAN 22 · PoE")
L("movf", "apf", "wl", "Wi-Fi 802.1X")
L("swf1", "hf1", "cu", "VLAN 21")
L("swf2", "hf2", "cu", "VLAN 21")
L("hf1", "hf2", "ha", "réplica")
L("wf", "swf2", "cu", "VLAN 21")
L("xl1", "hf1", "x", "dentro del host")
L("xl2", "hf2", "x", "dentro del host")
L("hr2", "xl1", "x", "contrato mínimo")
L("fwr2", "swdmz", "cu", "VLAN 80 DMZ")
L("swdmz", "aaa", "cu", None)
L("swdmz", "dns", "cu", None)
L("swdmz", "coll", "cu", None)
L("swaux", "fwr2", "cu", "VRF aux · solo Internet")
L("swaux", "swr1", "den", "ACL: denegado")
L("apg", "swaux", "cu", "VLAN 60")
L("movg1", "apg", "wl", "Wi-Fi invitados")
L("cam", "swaux", "cu", "VLAN 50")
L("nvr", "swaux", "cu", "VLAN 50")
L("iot", "swaux", "cu", "VLAN 40")
L("lock", "iot", "cu", None)
L("admin", "swaux", "cu", "VLAN 70")

par = {frozenset((e["a"], e["b"])): i for i, e in enumerate(enlaces)}

FLUJOS = {
    "A": dict(color="#D32F2F", nombre="A · Venta POS con tarjeta", pasos=[
        ("pos1", "swr1", "La caja entrega la venta al switch · VLAN 10 dentro de VRF-R"),
        ("swr1", "hr1", "El switch la lleva al host R-01 · API local cifrada, diario durable"),
        ("hr1", "hr2", "BIFURCACIÓN 1 · réplica del diario a R-02 con fencing por testigo"),
        ("tpv", "swr1", "El TPV inicia el cobro en la misma VLAN 10 · el PAN no se guarda en el diario"),
        ("swr1", "fwr1", "Venta y cobro salen por el firewall Retail · ACL y NAT propios"),
        ("fwr1", "cpeA", "Entrega al CPE del operador A"),
        ("cpeA", "opA", "Acceso WAN del operador A"),
        ("opA", "pay", "BIFURCACIÓN 2 · rama pago: TPV → procesador autorizado por HTTPS"),
        ("opA", "vpn", "BIFURCACIÓN 2 · rama sincronización: túnel IPsec al VPN Gateway"),
        ("vpn", "azfw", "Azure Firewall inspecciona · UDR y retorno simétrico"),
        ("azfw", "ag", "Entrada privada con WAF regional"),
        ("ag", "apim", "Listener y política de la API"),
        ("apim", "aks", "Balanceo interno hacia los pods de negocio"),
        ("aks", "pg", "Persistencia en PostgreSQL por Private Endpoint · TLS")]),
    "B": dict(color="#1E6FD9", nombre="B · Consulta desde móvil del personal", pasos=[
        ("movr1", "apr", "Terminal móvil por Wi-Fi corporativo · EAP-TLS"),
        ("apr", "swr1", "AP al switch · VLAN 12 con PoE"),
        ("swr1", "hr1", "BIFURCACIÓN · rama local: oferta vigente servida por R-01"),
        ("swr1", "fwr1", "BIFURCACIÓN · rama nube: sale por el firewall Retail"),
        ("fwr1", "cpeA", "Entrega al CPE del operador A"),
        ("cpeA", "opA", "Acceso WAN del operador A"),
        ("opA", "vpn", "Túnel IPsec al VPN Gateway"),
        ("vpn", "azfw", "Inspección en Azure Firewall"),
        ("azfw", "ag", "Entrada privada con WAF regional"),
        ("ag", "apim", "Política de la API · token de identidad"),
        ("apim", "aks", "Balanceo interno hacia los pods"),
        ("aks", "pg", "Lectura en PostgreSQL por Private Endpoint")]),
    "C": dict(color="#2E9E4F", nombre="C · Consulta web de un cliente en Wi-Fi invitados", pasos=[
        ("movg1", "apg", "Móvil del cliente en el SSID de invitados"),
        ("apg", "swaux", "VLAN 60 · clientes aislados entre sí"),
        ("swaux", "fwr2", "VRF auxiliar hacia el borde · solo Internet (no hay ruta a VLAN 10/11)"),
        ("fwr2", "cpeB", "Entrega al CPE del operador B"),
        ("cpeB", "opB", "Acceso WAN del operador B"),
        ("opB", "fd", "Internet · HTTPS 443 hacia Front Door · WAF de borde"),
        ("fd", "ag", "Private Link hacia Application Gateway"),
        ("ag", "apim", "Política de la API"),
        ("apim", "aks", "Balanceo interno hacia los pods"),
        ("aks", "pg", "Lectura en PostgreSQL por Private Endpoint")]),
}
for k, f in FLUJOS.items():
    for n, (a, b, d) in enumerate(f["pasos"], 1):
        i = par[frozenset((a, b))]
        enlaces[i]["flows"].append((k, n))

LINK = {"cu": ("#5B6573", 1.8, ""), "wl": ("#5B6573", 1.6, "dashed=1;dashPattern=3 4;"), "den": ("#C62828", 1.8, "dashed=1;dashPattern=2 4;"),
        "x": ("#D1741A", 2.0, "dashed=1;dashPattern=6 4;"), "ha": ("#37474F", 2.6, ""), "ipsec": ("#2E3B8F", 2.0, "dashed=1;dashPattern=8 3;"),
        "inet": ("#5B6573", 1.8, "dashed=1;dashPattern=8 3;")}

# --------------------------------------------------------------------------- obstáculos
BAN = 26


def texto_w(c):
    return len(c["label"]) * c["size"] * 0.56 + 14


def header_rect(c):
    x0, y0, x1, y1 = c["rect"]
    w = texto_w(c)
    return (x0 + 8, y0 + 3, x0 + 8 + w, y0 + 22)


OBS = []
for n in nodos.values():
    l, t, r, b = n["card"]
    OBS.append((l - 5, t - 5, r + 5, b + 5, n["id"]))
for c in clusters:
    l, t, r, b = header_rect(c)
    OBS.append((l - 4, t - 2, r + 4, b + 2, "hdr_" + c["id"]))

Y_TABLE = 1640
NX, NY = W // G + 2, (Y_TABLE + 100) // G
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
    for iy in range(0, 3):
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

BLOQ = ["rack3", "rack1", "rack2", "dmz", "v10", "v12", "v20", "v22", "v60", "v50", "v40", "v70", "z_inet", "z_wan"]
ZMIEMBROS = {z: set(cl_id[z]["miembros"]) for z in BLOQ}
ZC = {}
for z in BLOQ:
    x0, y0, x1, y1 = cl_id[z]["rect"]
    for iy in range(int((y0 + 4) // G) + 1, int((y1 - 4) // G) + 1):
        for ix in range(int((x0 + 4) // G) + 1, int((x1 - 4) // G) + 1):
            if x0 + 4 < ix * G < x1 - 4 and y0 + 4 < iy * G < y1 - 4:
                ZC.setdefault((ix, iy), set()).add(z)


def puertos(nid):
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
            res.append(dict(nid=nid, side=side, off=off, ix=ix, iy=iy, dir=d))
    return res


def ruta(src, dst):
    S, T = puertos(src), puertos(dst)
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


res, fallos = {}, []
orden = sorted(range(len(enlaces)), key=lambda i: (-len(enlaces[i]["flows"]) > -1, dist(enlaces[i])))
orden = sorted(range(len(enlaces)), key=lambda i: dist(enlaces[i]))
for i in orden:
    e = enlaces[i]
    r = ruta(e["a"], e["b"])
    if r is None:
        fallos.append((e["a"], e["b"]))
        continue
    o, d, cam = r
    usados.add((o["nid"], o["side"], o["off"]))
    usados.add((d["nid"], d["side"], d["off"]))
    margen = 1 if e["flows"] else 0
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
                viol.add((enlaces[i]["a"], enlaces[i]["b"], tag))
print("violaciones:", len(viol), sorted(viol)[:10])
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
print("cruces entre enlaces:", cr)

# --------------------------------------------------------------------------- etiquetas de enlace (flujos + texto)
def cruza_rect(p, q, rect):
    l, t, r, b = rect
    (x0, y0), (x1, y1) = p, q
    if y0 == y1:
        return t <= y0 <= b and max(min(x0, x1), l) < min(max(x0, x1), r)
    return l <= x0 <= r and max(min(y0, y1), t) < min(max(y0, y1), b)


etq_rects, etqs, txts = [], {}, {}


def colocar(i, pw, ph, preferir_largo=True):
    o, d, pts = res[i]
    cand = []
    for k in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[k], pts[k + 1]
        L_ = abs(x1 - x0) + abs(y1 - y0)
        horizontal = y0 == y1
        if L_ < (pw if horizontal else ph) + 6:
            continue
        for fr in (0.5, 0.35, 0.65, 0.25, 0.75, 0.15, 0.85):
            cand.append((-L_, x0 + (x1 - x0) * fr, y0 + (y1 - y0) * fr))
    cand.sort(key=lambda c: c[0])
    otros = [s_ for s_ in segs if s_[0] != i]
    for _, cx, cy in cand:
        rect = (cx - pw / 2, cy - ph / 2, cx + pw / 2, cy + ph / 2)
        ok = True
        for (ol, ot, orr, ob, tag) in OBS:
            if tag in nodos:
                ol, ot, orr, ob = ol + 5, ot + 5, orr - 5, ob - 5
            if rect[0] < orr and rect[2] > ol and rect[1] < ob and rect[3] > ot:
                ok = False; break
        if ok:
            for (pl, pt, pr_, pb) in etq_rects:
                if rect[0] < pr_ + 2 and rect[2] > pl - 2 and rect[1] < pb + 2 and rect[3] > pt - 2:
                    ok = False; break
        if ok:
            for (i2, p0, p1) in otros:
                if cruza_rect(p0, p1, rect):
                    ok = False; break
        if ok:
            etq_rects.append(rect)
            return rect
    return None


for i in sorted(res, key=lambda i: -len(enlaces[i]["flows"])):
    e = enlaces[i]
    flows = sorted(e["flows"])
    if flows:
        r = colocar(i, len(flows) * 22, 20)
        if r is None:
            print("círculos sin lugar:", e["a"], e["b"], flows, file=sys.stderr)
        else:
            etqs[i] = r
for i in sorted(res):
    e = enlaces[i]
    if e["lab"]:
        w = len(e["lab"]) * 5.2 + 10
        r = colocar(i, w, 18)
        if r is None:
            print("texto sin lugar:", e["a"], e["b"], e["lab"], file=sys.stderr)
        else:
            txts[i] = r

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
    fill, stroke, sw, dash = ZST[c["kind"]]
    es_rack = c["kind"] == "rack"
    vertex(f"g_{c['id']}", c["label"],
           f"rounded={0 if es_rack else 1};arcSize=3;html=1;whiteSpace=nowrap;fillColor={fill};strokeColor={stroke};strokeWidth={sw};{dash}"
           f"verticalAlign=top;align=left;spacingLeft=8;spacingTop=2;fontStyle=1;fontSize={c['size']};fontColor=#1A1A1A;fontFamily=Helvetica;", x0, y0, x1 - x0, y1 - y0)


def edge_xml(id_, i, color, w, dash, flecha=False, opac=100):
    e = enlaces[i]
    o, d, pts = res[i]
    n1, n2 = nodos[e["a"]], nodos[e["b"]]

    def fr(p, n):
        l, t, r, b = n["card"]
        return ((p[0] - l) / (r - l), (p[1] - t) / (b - t))

    ex, ey = fr(pts[0], n1)
    nx, ny = fr(pts[-1], n2)
    st = (f"html=1;rounded=0;endArrow=none;startArrow=none;strokeColor={color};strokeWidth={w};{dash}opacity={opac};"
          f"exitX={ex:.3f};exitY={ey:.3f};exitPerimeter=0;entryX={nx:.3f};entryY={ny:.3f};entryPerimeter=0;")
    puntos = "".join(f'<mxPoint x="{x}" y="{y}"/>' for x, y in pts[1:-1])
    cells.append(f'<mxCell id="{id_}" value="" style="{st}" edge="1" parent="1" source="n_{e["a"]}" target="n_{e["b"]}">'
                 f'<mxGeometry relative="1" as="geometry"><Array as="points">{puntos}</Array></mxGeometry></mxCell>')


# subcapa de flujos (líneas concéntricas) y encima el enlace físico
for i in sorted(res):
    fl = sorted(set(k for k, _ in enlaces[i]["flows"]))
    k = len(fl)
    for j, f in enumerate(fl):
        w = 7 + 5 * (k - 1 - j)
        edge_xml(f"u{i}_{f}", i, FLUJOS[f]["color"], w, "", opac=90)
for i in sorted(res):
    col, w, dash = LINK[enlaces[i]["tipo"]]
    edge_xml(f"l{i}", i, col, w, dash)

# nodos
for n in nodos.values():
    l, t, r, b = n["card"]
    vertex(f"n_{n['id']}", n["texto"],
           "rounded=1;arcSize=8;html=1;fillColor=#FFFFFF;strokeColor=#8D97A5;strokeWidth=1.2;verticalAlign=bottom;align=center;"
           "fontSize=10;fontColor=#1A1A1A;fontFamily=Helvetica;spacingBottom=3;whiteSpace=nowrap;", l, t, r - l, b - t)
    cells.append(f'<mxCell id="i_{n["id"]}" value="" style="{IC[n["icono"]]};" vertex="1" parent="1">'
                 f'<mxGeometry x="{n["cx"] - ICON // 2}" y="{n["cy"] - ICON // 2 - 4}" width="{ICON}" height="{ICON}" as="geometry"/></mxCell>')

# etiquetas: círculos de flujo y texto del enlace
for i, rect in etqs.items():
    flows = sorted(enlaces[i]["flows"])
    x = rect[0]
    cy = (rect[1] + rect[3]) / 2
    for j, (f, n) in enumerate(flows):
        vertex(f"q{i}_{j}", f"{f}{n}", f"ellipse;html=1;fillColor={FLUJOS[f]['color']};strokeColor=#FFFFFF;strokeWidth=1.5;fontColor=#FFFFFF;fontStyle=1;fontSize=8;fontFamily=Helvetica;align=center;verticalAlign=middle;spacing=0;",
               x, cy - 10, 20, 20)
        x += 22
for i, rect in txts.items():
    e = enlaces[i]
    col = LINK[e["tipo"]][0]
    vertex(f"t{i}", e["lab"], f"rounded=1;arcSize=40;html=1;fillColor=#FFFFFF;strokeColor={col};strokeWidth=1;fontColor={col};fontSize=8.5;fontFamily=Helvetica;align=center;verticalAlign=middle;spacing=0;",
           rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1])

# marcas de bifurcación
for nid, txt in (("hr1", "BIF A1"), ("opA", "BIF A2"), ("swr1", "BIF A·B")):
    l, t, r, b = nodos[nid]["card"]
    w = len(txt) * 5.4 + 12
    vertex(f"bif_{nid}", txt, "rounded=1;arcSize=30;html=1;fillColor=#FFC107;strokeColor=#FFFFFF;strokeWidth=1;fontColor=#3E2723;fontStyle=1;fontSize=8;fontFamily=Helvetica;align=center;verticalAlign=middle;spacing=0;",
           l + 3, t + 3, w, 14)

# título, leyenda y tablas de ruta
vertex("titulo", "Diagrama de red de prueba · tienda tipo SIT-xx · bifurcaciones del dato",
       "text;html=1;align=center;verticalAlign=middle;fontSize=20;fontStyle=1;fontFamily=Helvetica;fontColor=#1A1A1A;", 300, 6, 1600, 28)
vertex("subtitulo", "Los enlaces grises son físicos o inalámbricos; el color que los acompaña es el dato que viaja por ellos. Donde el color se reparte entre dos enlaces hay una bifurcación. Diseño de prueba: no sigue al 100 % la propuesta (la DMZ de tienda es hipotética).",
       "text;html=1;align=center;verticalAlign=middle;fontSize=10.5;fontFamily=Helvetica;fontColor=#333333;", 150, 34, 1840, 20)

ly = Y_TABLE - 70
vertex("leyenda_t", "Leyenda de enlaces", "text;html=1;align=left;verticalAlign=middle;fontSize=10;fontStyle=1;fontFamily=Helvetica;", 20, ly - 2, 200, 16)
leyenda = [("cu", "cobre / fibra"), ("wl", "inalámbrico"), ("ha", "par HA / réplica"), ("ipsec", "túnel IPsec"), ("inet", "Internet"), ("x", "contrato X-01"), ("den", "denegado por ACL")]
x = 20
for k, (t_, txt) in enumerate(leyenda):
    col, w, dash = LINK[t_]
    cells.append(f'<mxCell id="ll{k}" value="" style="html=1;endArrow=none;strokeColor={col};strokeWidth={w};{dash}" edge="1" parent="1">'
                 f'<mxGeometry relative="1" as="geometry"><mxPoint x="{x}" y="{ly + 24}" as="sourcePoint"/><mxPoint x="{x + 38}" y="{ly + 24}" as="targetPoint"/></mxGeometry></mxCell>')
    vertex(f"llt{k}", txt, "text;html=1;align=left;verticalAlign=middle;fontSize=9;fontFamily=Helvetica;whiteSpace=nowrap;", x + 42, ly + 16, 110, 16)
    x += 160
x += 20
for k, d in FLUJOS.items():
    vertex(f"lf{k}", d["nombre"], f"rounded=1;arcSize=40;html=1;fillColor={d['color']};strokeColor=#FFFFFF;fontColor=#FFFFFF;fontStyle=1;fontSize=9;fontFamily=Helvetica;align=center;verticalAlign=middle;whiteSpace=nowrap;",
           x, ly + 14, len(d["nombre"]) * 5.4 + 16, 20)
    x += len(d["nombre"]) * 5.4 + 24

# tablas de ruta
ty = Y_TABLE
colw = (W - 40 - 40) / 3
for j, (k, d) in enumerate(FLUJOS.items()):
    x0 = 20 + j * (colw + 20)
    vertex(f"th{k}", d["nombre"], f"rounded=0;html=1;fillColor={d['color']};strokeColor={d['color']};fontColor=#FFFFFF;fontStyle=1;fontSize=11;align=left;spacingLeft=8;verticalAlign=middle;fontFamily=Helvetica;",
           x0, ty, colw, 24)
    for n, (a, b, desc) in enumerate(d["pasos"], 1):
        y = ty + 24 + (n - 1) * 24
        vertex(f"tn{k}{n}", f"{k}{n}", f"ellipse;html=1;fillColor={d['color']};strokeColor=#FFFFFF;fontColor=#FFFFFF;fontStyle=1;fontSize=8;fontFamily=Helvetica;align=center;verticalAlign=middle;spacing=0;",
               x0 + 4, y + 2, 20, 20)
        bif = desc.startswith("BIFURCACIÓN")
        vertex(f"td{k}{n}", desc, f"rounded=0;html=1;whiteSpace=wrap;fillColor={'#FFF8E1' if bif else '#FFFFFF'};strokeColor=#CFD8DC;fontSize=9;fontStyle={1 if bif else 0};fontColor=#1A1A1A;fontFamily=Helvetica;align=left;spacingLeft=30;verticalAlign=middle;",
               x0, y, colw, 24)
maxrows = max(len(d["pasos"]) for d in FLUJOS.values())
yend = ty + 24 + maxrows * 24
vertex("pie", "Fuente: elaboración propia a partir del inventario físico integral (23-10-2026) y de decisiones del usuario; diagrama de prueba, no es despliegue acreditado. Uso de IA Alto. "
       "Racks 1 y 2: servidores por negocio; rack 3: comunicaciones. Cuatro hosts por tienda (dos Retail, dos Filial) y X-01 local dentro del par Filial.",
       "text;html=1;align=center;verticalAlign=top;fontSize=9.5;fontFamily=Helvetica;fontColor=#1A1A1A;whiteSpace=wrap;", 100, yend + 10, W - 200, 34)

H = int(yend + 60)
xml = ('<mxfile host="diagramas-ancoa" type="device"><diagram id="d1" name="Red de tienda de prueba">'
       f'<mxGraphModel dx="1200" dy="800" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" pageScale="1" pageWidth="{W}" pageHeight="{H}" background="#FFFFFF" math="0" shadow="0">'
       f'<root>{"".join(cells)}</root></mxGraphModel></diagram></mxfile>')
open(sys.argv[1] if len(sys.argv) > 1 else "red.drawio", "w", encoding="utf-8").write(xml)
print("lienzo", W, H)
for c in clusters:
    if c["id"] in ("rack3", "rack1", "rack2", "dmz", "z_azure"):
        print(c["id"], c["rect"])
