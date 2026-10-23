#!/usr/bin/env python3
"""Genera la figura de arquitectura física general con clusters centrados y flechas enrutadas sin pisar íconos ni rótulos."""
import heapq
import html
import json
import sys

G = 10                 # celda del enrutador (px)
ICON = 40
HALF = ICON // 2
W_CANVAS = 2040
CHAR_W = 5.9
LINE_H = 13.5

# --------------------------------------------------------------------------- estilos
AZ = "image;aspect=fixed;html=1;image=img/lib/azure2/"
CI = "aspect=fixed;html=1;fillColor=%s;strokeColor=#FFFFFF;shape=mxgraph.cisco."
ICONOS = {
    "users": AZ + "identity/Users.svg",
    "entra": AZ + "identity/Azure_Active_Directory.svg",
    "fd": AZ + "networking/Front_Doors.svg",
    "ag": AZ + "networking/Application_Gateways.svg",
    "apim": AZ + "integration/API_Management_Services.svg",
    "ilb": AZ + "networking/Load_Balancers.svg",
    "aks": AZ + "containers/Kubernetes_Services.svg",
    "pg": AZ + "databases/Azure_Database_PostgreSQL_Server.svg",
    "vpn": AZ + "networking/Virtual_Network_Gateways.svg",
    "fw": AZ + "networking/Firewalls.svg",
    "soc": AZ + "security/Azure_Sentinel.svg",
    "dr": AZ + "other/Backup_Vault.svg",
    "laptop": "aspect=fixed;html=1;fillColor=#005073;strokeColor=none;shape=mxgraph.azure.laptop",
    "router": CI % "#005073" + "routers.router",
    "switch": CI % "#005073" + "switches.layer_3_switch",
    "ap": CI % "#005073" + "misc.access_point",
    "pc": CI % "#005073" + "computers_and_peripherals.workstation",
    "host": CI % "#005073" + "servers.fileserver",
    "xhost": CI % "#C25A10" + "security.ios_firewall",
    "cam": CI % "#005073" + "computers_and_peripherals.video_camera",
    "nvr": CI % "#005073" + "servers.storage_server",
    "ups": CI % "#8A5A2B" + "misc.ups",
    "cloud": "aspect=fixed;html=1;fillColor=#005073;strokeColor=none;shape=mxgraph.azure.cloud",
    "dc": CI % "#005073" + "servers.fileserver",
    "iot": CI % "#005073" + "computers_and_peripherals.terminal",
}

CLUSTER_ESTILO = {
    "R": ("#E6F0FA", "#2F78B7", ""),
    "F": ("#EFE9F6", "#7A55A5", ""),
    "X": ("#FDEFD9", "#D98A2B", ""),
    "G": ("#F1F2F4", "#8B9099", ""),
    "DR": ("#E7F4F1", "#2A8C7C", "dashed=1;dashPattern=6 3;"),
    "PW": ("#F9F0E6", "#9A6B3B", "dashed=1;dashPattern=1 3;"),
    "CH": ("#FFFFFF", "#5F6368", ""),
    "AZ": ("#FFFFFF", "#0078D4", ""),
    "ST": ("#FFFFFF", "#1F3864", ""),
}

ARISTA_ESTILO = {
    "R": ("#1F6FB5", 1.8, ""),
    "F": ("#7B4FA8", 1.8, ""),
    "X": ("#D1741A", 1.8, ""),
    "ADM": ("#6B7280", 1.5, "dashed=1;dashPattern=6 4;"),
    "IDN": ("#1F3864", 1.5, "dashed=1;dashPattern=1 3;"),
    "DR": ("#1B8A7A", 1.6, "dashed=1;dashPattern=8 4;"),
    "PW": ("#8A5A2B", 1.6, "dashed=1;dashPattern=1 3;"),
    "GEN": ("#3C4043", 1.8, ""),
}

# --------------------------------------------------------------------------- nodos
nodos = {}


def N(id_, cx, cy, texto, icono, lab="b"):
    nodos[id_] = dict(id=id_, cx=cx, cy=cy, texto=texto, icono=icono, lab=lab)


# columnas de bloque: R a la izquierda (c1 = lado de la pasarela), F en espejo
RC = {1: 210, 2: 390, 3: 580, 4: 780}
FC = {1: 1830, 2: 1650, 3: 1460, 4: 1260}
CEN = 1020

Y_T1 = 100
Y_C1, Y_C2, Y_C3 = 336, 524, 712
Y_DR = 890
Y_S1, Y_S2, Y_S3 = 1100, 1288, 1476

# nivel 1: actores, borde, identidad, administración
N("cliente", 660, Y_T1, "Cliente / titular\nNavegador o app", "users")
N("fd", CEN, Y_T1, "Front Door Premium\nWAF / Private Link · R/F", "fd")
N("entra", 1380, Y_T1, "Entra ID / External ID\nIdentidad por ámbito", "entra")
N("admin", 1720, Y_T1, "Administración autorizada\nMFA / PIM / postura", "laptop")

for s, C, nm in (("r", RC, "Retail"), ("f", FC, "Filial")):
    N("ag_" + s, C[1], Y_C1, "Application Gateway", "ag")
    N("apim_" + s, C[2], Y_C1, "API Management", "apim")
    N("ilb_" + s, C[1], Y_C2, "Load Balancer interno\nVIP / Service por backend", "ilb")
    N("aks_" + s, C[2], Y_C2, "AKS %s\nSYS · BIZ · INT ·\nSTATE · OPS" % nm, "aks")
    N("pg_" + s, C[3], Y_C2, "Datos %s\nPostgreSQL / PaaS\npropios" % nm, "pg")
    N("vpn_" + s, C[1], Y_C3, "VPN Gateway", "vpn")
    N("fw_" + s, C[2], Y_C3, "Azure Firewall", "fw")

N("x01", CEN, Y_C2, "X-01\nControl y bitácora propios", "aks")
N("soc", CEN, Y_C3, "Seguridad / operación\nBastion · Vault/HSM ·\nSentinel", "soc")
N("dr_r", CEN - 160, Y_DR, "DR Retail\nRecursos y datos\npropios", "dr")
N("dr_x", CEN, Y_DR, "DR X-01\nEnclave y bitácora\npropios", "dr")
N("dr_f", CEN + 160, Y_DR, "DR Filial\nRecursos y datos\npropios", "dr")

# sitios Ancoa: Retail (izquierda) y Filial (espejo)
N("sd_r", RC[1], Y_S1, "Routers / SD-WAN\nRetail · HA", "router")
N("sw_r", RC[2], Y_S1, "Switches LAN\nRetail · par", "switch")
N("ap_r", RC[3], Y_S1, "AP Wi-Fi corporativo R\n802.1X / certificado\nVLAN 12", "ap")
N("caja", RC[4], Y_S1, "Cajas / puestos Retail\nCliente local R\nVLAN 10", "pc")
N("sd_f", FC[1], Y_S1, "Routers / SD-WAN\nFilial · HA", "router")
N("sw_f", FC[2], Y_S1, "Switches LAN\nFilial · par", "switch")
N("ap_f", FC[3], Y_S1, "AP Wi-Fi financiero\nIdentidad y red F\nVLAN 22", "ap")
N("mes", FC[4], Y_S1, "Mesón financiero /\ncliente F\nVLAN 20", "pc")
N("dccd", CEN, Y_S1, "DC / CD conservados\nIntegración por contrato", "dc")

N("h_r1", RC[2], Y_S2, "SIT-xx-R-01\nVenta y diario", "host")
N("h_r2", RC[3], Y_S2, "SIT-xx-R-02\nRéplica local Retail", "host")
N("h_f1", FC[2], Y_S2, "SIT-xx-F-01\nAutorizador / libro F", "host")
N("h_f2", FC[3], Y_S2, "SIT-xx-F-02\nRéplica F / X local", "host")
N("x_loc", FC[4], Y_S2, "X-01 local · 2 instancias\nAisladas en F-01/02\nVLAN 23", "xhost")

N("sd_aux", RC[1], Y_S3, "Borde auxiliar\nACL / salida controlada", "router")
N("sw_aux", RC[2], Y_S3, "Switch de acceso auxiliar\nVRF/VLAN aisladas", "switch")
N("iot", RC[3], Y_S3, "Controlador IoT / lockers\nSolo contrato Pedidos\nVLAN 40", "iot")
N("ap_g", 760, Y_S3, "Wi-Fi invitados\nSolo Internet\nVLAN 60", "ap")
N("internet", 880, Y_S3, "Internet\nSalida invitados", "cloud")
N("cam", 1030, Y_S3, "Cámaras IP\nSegmento CCTV\nVLAN 50", "cam")
N("nvr", 1150, Y_S3, "NVR local\nRetención 30 días", "nvr")
N("gen", 1350, Y_S3, "Generador / fuente\nedificio 24 h\nesenciales, por sitio", "ups")
N("ats", 1510, Y_S3, "ATS / tableros A-B\nTransferencia\nsupervisada", "ups")
N("ups", 1670, Y_S3, "UPS A/B online\n30 min a plena carga", "ups")
N("pdu", 1830, Y_S3, "PDU A/B por rack\nA hosts y equipos\nde red", "ups")


def rect_etiqueta(n):
    lineas = n["texto"].split("\n")
    w = max(len(l) for l in lineas) * CHAR_W + 8
    h = len(lineas) * LINE_H + 4
    if n["lab"] == "b":
        return (n["cx"] - w / 2, n["cy"] + HALF + 2, n["cx"] + w / 2, n["cy"] + HALF + 2 + h)
    raise ValueError


def rect_nodo(n):
    l, t, r, b = n["cx"] - HALF, n["cy"] - HALF, n["cx"] + HALF, n["cy"] + HALF
    el = rect_etiqueta(n)
    return (min(l, el[0]), t, max(r, el[2]), max(b, el[3]))


# --------------------------------------------------------------------------- clusters
clusters = []


def C(id_, label, estilo, miembros, align="left", pad=(8, 36, 8, 10), tamano=11.5):
    clusters.append(dict(id=id_, label=label, estilo=estilo, miembros=miembros, align=align, pad=pad, tamano=tamano))


# tier 1
C("t_borde", "Borde global · perfiles R / F", "G", ["fd"], pad=(26, 34, 26, 10))
C("t_ident", "Identidad por ámbito", "G", ["entra"], pad=(26, 34, 26, 10))
C("t_admin", "Administración autorizada · VLAN 70", "G", ["admin"], pad=(26, 34, 26, 10))
# Chile Central
C("c_ent_r", "Entrada Retail · subredes propias", "R", ["ag_r", "apim_r"], align="right")
C("c_aks_r", "AKS Retail · nodos / Services privados", "R", ["ilb_r", "aks_r"], align="right")
C("c_dat_r", "Datos R · acceso privado", "R", ["pg_r"], align="right")
C("c_hub_r", "Hub Retail · VPN / firewall", "R", ["vpn_r", "fw_r"], align="right")
C("c_ent_f", "Entrada Filial · subredes propias", "F", ["ag_f", "apim_f"])
C("c_aks_f", "AKS Filial · nodos / Services privados", "F", ["ilb_f", "aks_f"])
C("c_dat_f", "Datos F · acceso privado", "F", ["pg_f"])
C("c_hub_f", "Hub Filial · VPN / firewall", "F", ["vpn_f", "fw_f"])
C("c_x", "X-01 · control / bitácora", "X", ["x01"], align="center")
C("c_soc", "Seguridad / operación · R / F / X", "G", ["soc"], align="center")
C("chile", "Chile Central · producción R / F / X",
  "CH", ["c_ent_r", "c_aks_r", "c_dat_r", "c_hub_r", "c_ent_f", "c_aks_f", "c_dat_f", "c_hub_f", "c_x", "c_soc"],
  pad=(58, 30, 58, 22), tamano=12.5)
C("brazil", "Brazil South · DR R / F / X separados", "DR", ["dr_r", "dr_x", "dr_f"], align="center", pad=(26, 34, 26, 10), tamano=12)
C("azure", "Microsoft Azure · nube de la solución", "AZ", ["chile", "brazil"], pad=(20, 30, 20, 20), tamano=13)

# sitios
C("s_vrf_r", "Retail · VRF-R · switches / SD-WAN", "R", ["sd_r", "sw_r"], align="right")
C("s_wifi_r", "Wi-Fi R · VLAN 12", "R", ["ap_r"], align="center")
C("s_caja", "Cajas · VLAN 10", "R", ["caja"], align="center")
C("s_vrf_f", "Filial · VRF-F · switches / SD-WAN", "F", ["sd_f", "sw_f"])
C("s_wifi_f", "Wi-Fi F · VLAN 22", "F", ["ap_f"], align="center")
C("s_mes", "Mesón · VLAN 20", "F", ["mes"], align="center")
C("s_dccd", "DC / CD · sistemas conservados", "G", ["dccd"], align="center")
C("s_hosts_r", "Retail · dos hosts HA · VLAN 11", "R", ["h_r1", "h_r2"], align="right")
C("s_hosts_f", "Filial · dos hosts HA · VLAN 21", "F", ["h_f1", "h_f2"])
C("s_xloc", "X local · VLAN 23 · dentro del par F", "X", ["x_loc"], align="center")
C("s_aux", "Acceso auxiliar · ACL / VRF propias · IoT · VLAN 40", "G", ["sd_aux", "sw_aux", "iot"], align="right")
C("s_guest", "Invitados · VLAN 60 · solo Internet", "G", ["ap_g", "internet"], align="center")
C("s_cctv", "CCTV · VLAN 50 · solo NVR local", "G", ["cam", "nvr"], align="center")
C("s_energia", "Energía por sitio · no es red IP", "PW", ["pdu", "ups", "ats", "gen"])
C("sitios", "Instalaciones Ancoa · patrón de tienda y sistemas conservados", "ST",
  ["s_vrf_r", "s_wifi_r", "s_caja", "s_vrf_f", "s_wifi_f", "s_mes", "s_dccd", "s_hosts_r", "s_hosts_f", "s_xloc",
   "s_aux", "s_guest", "s_cctv", "s_energia"], pad=(40, 30, 40, 22), tamano=12.5)

cl_por_id = {c["id"]: c for c in clusters}


def texto_ancho(c):
    return len(c["label"]) * (c["tamano"] * 0.56) + 14


def calcular_rect(c):
    if "rect" in c:
        return c["rect"]
    xs0, ys0, xs1, ys1 = [], [], [], []
    for m in c["miembros"]:
        r = calcular_rect(cl_por_id[m]) if m in cl_por_id else rect_nodo(nodos[m])
        xs0.append(r[0]); ys0.append(r[1]); xs1.append(r[2]); ys1.append(r[3])
    pl, pt, pr, pb = c["pad"]
    x0, y0, x1, y1 = min(xs0) - pl, min(ys0) - pt, max(xs1) + pr, max(ys1) + pb
    mw = texto_ancho(c) + 12
    if x1 - x0 < mw:
        extra = mw - (x1 - x0)
        if c["align"] == "right":
            x0 -= extra
        elif c["align"] == "center":
            x0 -= extra / 2; x1 += extra / 2
        else:
            x1 += extra
    c["rect"] = (x0, y0, x1, y1)
    return c["rect"]


for c in clusters:
    calcular_rect(c)

# --- ajustes de alineación de filas dentro de las bandas (mismo alto y bordes alineados)
def fijar(id_, **kw):
    r = list(cl_por_id[id_]["rect"])
    for k, v in kw.items():
        r["x0 y0 x1 y1".split().index(k)] = v
    cl_por_id[id_]["rect"] = tuple(r)

# --------------------------------------------------------------------------- aristas
# (origen, destino, tipo, etiqueta)
aristas = [
    ("cliente", "fd", "GEN", None),
    ("cliente", "entra", "IDN", None),
    ("admin", "entra", "ADM", None),
    ("admin", "soc", "ADM", None),
    ("fd", "ag_r", "R", None),
    ("fd", "ag_f", "F", None),
    ("ag_r", "apim_r", "R", None), ("ag_f", "apim_f", "F", None),
    ("ag_r", "ilb_r", "R", None), ("ag_f", "ilb_f", "F", None),
    ("apim_r", "ilb_r", "R", None), ("apim_f", "ilb_f", "F", None),
    ("ilb_r", "aks_r", "R", None), ("ilb_f", "aks_f", "F", None),
    ("aks_r", "pg_r", "R", None), ("aks_f", "pg_f", "F", None),
    ("vpn_r", "fw_r", "R", None), ("vpn_f", "fw_f", "F", None),
    ("fw_r", "ag_r", "R", None), ("fw_f", "ag_f", "F", None),
    ("aks_r", "x01", "X", None),
    ("x01", "ag_f", "X", None),
    ("pg_r", "dr_r", "DR", None), ("pg_f", "dr_f", "DR", None), ("x01", "dr_x", "DR", None),
    ("fw_r", "soc", "ADM", None), ("fw_f", "soc", "ADM", None),
    ("aks_r", "dccd", "ADM", None), ("aks_f", "dccd", "ADM", None),
    # sitio Retail
    ("caja", "sw_r", "R", None), ("ap_r", "sw_r", "R", None),
    ("sw_r", "h_r1", "R", None), ("h_r1", "h_r2", "R", None),
    ("sw_r", "sd_r", "R", None), ("sd_r", "vpn_r", "R", None),
    # sitio Filial
    ("mes", "sw_f", "F", None), ("ap_f", "sw_f", "F", None),
    ("sw_f", "h_f1", "F", None), ("h_f1", "h_f2", "F", None),
    ("sw_f", "sd_f", "F", None), ("sd_f", "vpn_f", "F", None),
    # cruce offline y X local
    ("h_r2", "x_loc", "X", "Compra offline · contrato mínimo"),
    ("x_loc", "h_f2", "X", None),
    ("x_loc", "x01", "DR", None),
    # auxiliares
    ("iot", "sw_aux", "R", None), ("sw_aux", "sd_aux", "R", None), ("sd_aux", "sd_r", "R", None),
    ("ap_g", "internet", "ADM", None), ("cam", "nvr", "ADM", None),
    # energía
    ("gen", "ats", "PW", None), ("ats", "ups", "PW", "Alimentación y bypass"),
    ("ups", "pdu", "PW", None),
]

# --------------------------------------------------------------------------- enrutador
def construir_obstaculos():
    obs = []
    for n in nodos.values():
        l, t, r, b = n["cx"] - HALF - 6, n["cy"] - HALF - 6, n["cx"] + HALF + 6, n["cy"] + HALF + 6
        obs.append((l, t, r, b, n["id"]))
        el = rect_etiqueta(n)
        obs.append((el[0] - 7, el[1] - 4, el[2] + 7, el[3] + 4, n["id"]))
    for c in clusters:
        x0, y0, x1, y1 = c["rect"]
        w = texto_ancho(c)
        if c["align"] == "left":
            hx = x0 + 6
        elif c["align"] == "right":
            hx = x1 - 6 - w
        else:
            hx = (x0 + x1) / 2 - w / 2
        obs.append((hx - 6, y0 + 2, hx + w + 6, y0 + 32, "hdr_" + c["id"]))
        c["hdr"] = (hx, y0 + 2, hx + w, y0 + 24)
    return obs


OBS = construir_obstaculos()
# título y rótulo de cabecera de la figura
X_MAX = W_CANVAS
Y_MAX = max(c["rect"][3] for c in clusters) + 20

NX = X_MAX // G + 2
NY = int(Y_MAX) // G + 6
bloqueado = [[False] * NX for _ in range(NY)]
for (l, t, r, b, _) in OBS:
    for iy in range(max(0, int(t // G)), min(NY, int(b // G) + 1)):
        for ix in range(max(0, int(l // G)), min(NX, int(r // G) + 1)):
            cx_, cy_ = ix * G, iy * G
            if l < cx_ < r and t < cy_ < b:
                bloqueado[iy][ix] = True
# bordes fuera del lienzo
for iy in range(NY):
    for ix in list(range(0, 5)) + list(range(NX - 5, NX)):
        bloqueado[iy][ix] = True
for ix in range(NX):
    for iy in (0, 1, 2, 3, 4, NY - 1):
        bloqueado[iy][ix] = True

# costo de ir pegado a un borde de cluster
borde_h = {}
borde_v = {}
for c in clusters:
    x0, y0, x1, y1 = c["rect"]
    for y in (y0, y1):
        iy = round(y / G)
        for ix in range(int(x0 // G), int(x1 // G) + 1):
            borde_h[(ix, iy)] = True
    for x in (x0, x1):
        ix = round(x / G)
        for iy in range(int(y0 // G), int(y1 // G) + 1):
            borde_v[(ix, iy)] = True

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ocup_h, ocup_v = set(), set()
puertos_usados = set()


def puertos(nid):
    n = nodos[nid]
    res = []
    for side, (dx, dy) in zip(("right", "bottom", "left", "top"), DIRS):
        for off in (0, -10, 10):
            if side in ("right", "left"):
                px, py = n["cx"] + dx * (HALF + 10), n["cy"] + off
            else:
                px, py = n["cx"] + off, n["cy"] + dy * (HALF + 10)
            ix, iy = px // G, py // G
            if bloqueado[iy][ix] or (nid, side, off) in puertos_usados:
                continue
            res.append(dict(nid=nid, side=side, off=off, ix=ix, iy=iy, dir=DIRS.index((dx, dy))))
    return res


def ruta(src, dst):
    S = puertos(src)
    T = puertos(dst)
    if not S or not T:
        return None
    tset = {}
    for t in T:
        tset[(t["ix"], t["iy"], (t["dir"] + 2) % 4)] = t
    tpos = [(t["ix"], t["iy"]) for t in T]

    def h(ix, iy):
        return min(abs(ix - a) + abs(iy - b) for a, b in tpos)

    pq = []
    best = {}
    padre = {}
    for s in S:
        st = (s["ix"], s["iy"], s["dir"])
        c0 = 0 if s["off"] == 0 else 0.5
        best[st] = c0
        heapq.heappush(pq, (c0 + h(s["ix"], s["iy"]), c0, st))
        padre[st] = (None, s)
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
            if not (0 <= jx < NX and 0 <= jy < NY) or bloqueado[jy][jx]:
                continue
            horiz = nd in (0, 2)
            costo = 1.0
            if nd != d:
                costo += 7.0
            # solapamiento con otras aristas
            if horiz:
                if (jx, jy) in ocup_h:
                    continue
                if (jx, jy - 1) in ocup_h or (jx, jy + 1) in ocup_h:
                    costo += 5
                if (jx, jy) in ocup_v:
                    costo += 12
                if (jx, jy) in borde_h:
                    costo += 6
            else:
                if (jx, jy) in ocup_v:
                    continue
                if (jx - 1, jy) in ocup_v or (jx + 1, jy) in ocup_v:
                    costo += 5
                if (jx, jy) in ocup_h:
                    costo += 12
                if (jx, jy) in borde_v:
                    costo += 6
            ns = (jx, jy, nd)
            ng = g + costo
            if ng < best.get(ns, 1e18) - 1e-9:
                best[ns] = ng
                padre[ns] = (st, None)
                heapq.heappush(pq, (ng + h(jx, jy), ng, ns))
    if fin is None:
        return None
    cam = []
    cur = fin
    while True:
        p, s = padre[cur]
        cam.append(cur)
        if p is None:
            origen = s
            break
        cur = p
    cam.reverse()
    destino = tset[fin]
    return origen, destino, [(ix * G, iy * G) for ix, iy, _ in cam]


def borde_punto(p):
    n = nodos[p["nid"]]
    x, y = n["cx"], n["cy"]
    if p["side"] == "right":
        return (x + HALF, y + p["off"])
    if p["side"] == "left":
        return (x - HALF, y + p["off"])
    if p["side"] == "top":
        return (x + p["off"], y - HALF)
    return (x + p["off"], y + HALF)


def simplificar(pts):
    out = []
    for p in pts:
        if out and out[-1] == p:
            continue
        out.append(p)
    ch = True
    while ch:
        ch = False
        for i in range(1, len(out) - 1):
            a, b, c = out[i - 1], out[i], out[i + 1]
            if (a[0] == b[0] == c[0]) or (a[1] == b[1] == c[1]):
                del out[i]
                ch = True
                break
    return out


rutas = []


def dist(a):
    na, nb = nodos[a[0]], nodos[a[1]]
    return abs(na["cx"] - nb["cx"]) + abs(na["cy"] - nb["cy"])


orden = sorted(range(len(aristas)), key=lambda i: dist(aristas[i]))
resultado = {}
fallos = []
for i in orden:
    a = aristas[i]
    r = ruta(a[0], a[1])
    if r is None:
        fallos.append(a)
        continue
    origen, destino, cam = r
    puertos_usados.add((origen["nid"], origen["side"], origen["off"]))
    puertos_usados.add((destino["nid"], destino["side"], destino["off"]))
    # puertos vecinos del mismo lado también quedan reservados para dejar aire
    for k in range(len(cam) - 1):
        (x0, y0), (x1, y1) = cam[k], cam[k + 1]
        if y0 == y1:
            ocup_h.add((x0 // G, y0 // G))
        else:
            ocup_v.add((x0 // G, y0 // G))
    for (x, y) in cam:
        pass
    # marcar todas las celdas del trazado
    for k in range(len(cam)):
        pass
    pts_cam = cam
    # rellenar celdas intermedias
    for k in range(len(pts_cam) - 1):
        (x0, y0), (x1, y1) = pts_cam[k], pts_cam[k + 1]
        if y0 == y1:
            ocup_h.add((x1 // G, y1 // G))
        else:
            ocup_v.add((x1 // G, y1 // G))
    ptos = [borde_punto(origen)] + pts_cam + [borde_punto(destino)]
    resultado[i] = (origen, destino, simplificar(ptos))

if fallos:
    print("SIN RUTA:", fallos, file=sys.stderr)


# --------------------------------------------------------------------------- verificaciones
def seg_cruza_rect(p, q, r):
    l, t, rr, b = r
    (x0, y0), (x1, y1) = p, q
    if y0 == y1:
        return t < y0 < b and max(min(x0, x1), l) < min(max(x0, x1), rr)
    return l < x0 < rr and max(min(y0, y1), t) < min(max(y0, y1), b)


viol = []
for i, (o, d, pts) in resultado.items():
    for k in range(len(pts) - 1):
        for (l, t, r, b, tag) in OBS:
            # los extremos tocan el propio icono: se permite en el primer/último tramo
            if tag in (aristas[i][0], aristas[i][1]) and (k == 0 or k == len(pts) - 2):
                # permitir solo la caja del icono, no su rótulo
                n = nodos[tag]
                if abs((l + r) / 2 - n["cx"]) < 1 and abs(r - l - (ICON + 12)) < 1:
                    continue
            if seg_cruza_rect(pts[k], pts[k + 1], (l + 5, t + 5, r - 5, b - 5)):
                viol.append((aristas[i][0], aristas[i][1], tag))
print("violaciones arista-obstáculo:", len(viol), set(viol) if viol else "")

# cruces entre aristas
segs = []
for i, (o, d, pts) in resultado.items():
    for k in range(len(pts) - 1):
        segs.append((i, pts[k], pts[k + 1]))
cruces = 0
for a in range(len(segs)):
    for b in range(a + 1, len(segs)):
        ia, p0, p1 = segs[a]
        ib, q0, q1 = segs[b]
        if ia == ib:
            continue
        hz_a, hz_b = p0[1] == p1[1], q0[1] == q1[1]
        if hz_a == hz_b:
            continue
        if hz_a:
            h0, h1, v0, v1 = p0, p1, q0, q1
        else:
            h0, h1, v0, v1 = q0, q1, p0, p1
        if min(h0[0], h1[0]) < v0[0] < max(h0[0], h1[0]) and min(v0[1], v1[1]) < h0[1] < max(v0[1], v1[1]):
            cruces += 1
print("cruces entre flechas:", cruces)

# --------------------------------------------------------------------------- salida draw.io
def esc(t):
    return html.escape(t, quote=True).replace("\n", "&#xa;")


celdas = ['<mxCell id="0"/>', '<mxCell id="1" parent="0"/>']
# clusters: de mayor a menor área para que los internos queden encima
for c in sorted(clusters, key=lambda c: -((c["rect"][2] - c["rect"][0]) * (c["rect"][3] - c["rect"][1]))):
    x0, y0, x1, y1 = c["rect"]
    fill, stroke, dash = CLUSTER_ESTILO[c["estilo"]]
    arc = 3 if c["estilo"] in ("AZ", "CH", "ST") else 4
    st = (f"rounded=1;arcSize={arc};whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};strokeWidth=1.2;{dash}"
          f"verticalAlign=top;align={c['align']};spacingLeft=8;spacingRight=8;spacingTop=3;fontStyle=1;fontSize={c['tamano']};"
          "fontColor=#1A1A1A;fontFamily=Helvetica;container=0;")
    celdas.append(f'<mxCell id="g_{c["id"]}" value="{esc(c["label"])}" style="{st}" vertex="1" parent="1">'
                  f'<mxGeometry x="{x0:.0f}" y="{y0:.0f}" width="{x1 - x0:.0f}" height="{y1 - y0:.0f}" as="geometry"/></mxCell>')

# aristas (debajo de nodos y rótulos)
for i, (o, d, pts) in sorted(resultado.items()):
    a = aristas[i]
    col, grosor, dash = ARISTA_ESTILO[a[2]]
    n1, n2 = nodos[a[0]], nodos[a[1]]

    def fr(p, n):
        return ((p[0] - (n["cx"] - HALF)) / ICON, (p[1] - (n["cy"] - HALF)) / ICON)

    ex, ey = fr(pts[0], n1)
    nx, ny = fr(pts[-1], n2)
    st = (f"html=1;rounded=0;endArrow=block;endFill=1;endSize=5;strokeColor={col};strokeWidth={grosor};{dash}"
          f"exitX={ex:.3f};exitY={ey:.3f};exitPerimeter=0;entryX={nx:.3f};entryY={ny:.3f};entryPerimeter=0;"
          "jettySize=auto;")
    puntos = "".join(f'<mxPoint x="{x}" y="{y}"/>' for x, y in pts[1:-1])
    celdas.append(f'<mxCell id="e{i}" value="" style="{st}" edge="1" parent="1" source="n_{a[0]}" target="n_{a[1]}">'
                  f'<mxGeometry relative="1" as="geometry"><Array as="points">{puntos}</Array></mxGeometry></mxCell>')

# etiquetas de arista: sobre el tramo más largo
etq_rects = []
for i, (o, d, pts) in sorted(resultado.items()):
    a = aristas[i]
    if not a[3]:
        continue
    mejor = None
    for k in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[k], pts[k + 1]
        L = abs(x1 - x0) + abs(y1 - y0)
        if y0 == y1 and (mejor is None or L > mejor[0]):
            mejor = (L, (x0 + x1) / 2, y0)
    if mejor is None:
        continue
    lineas = a[3].split(" / ")
    w = max(len(x) for x in lineas) * 5.4 + 10
    h = 14 * len(lineas) + 2
    etq_rects.append((a[3], mejor[1], mejor[2], w, h))
    celdas.append(f'<mxCell id="el{i}" value="{esc(a[3])}" style="text;html=1;align=center;verticalAlign=middle;fontSize=10;'
                  f'fontColor=#1A1A1A;fillColor=#FFFFFF;fontFamily=Helvetica;spacing=1;" vertex="1" parent="1">'
                  f'<mxGeometry x="{mejor[1] - w / 2:.0f}" y="{mejor[2] - h / 2:.0f}" width="{w:.0f}" height="{h:.0f}" as="geometry"/></mxCell>')

for n in nodos.values():
    base = ICONOS[n["icono"]]
    st = (base + ";verticalLabelPosition=bottom;verticalAlign=top;labelPosition=center;align=center;fontSize=11;"
          "fontColor=#1A1A1A;fontFamily=Helvetica;spacingTop=-2;")
    celdas.append(f'<mxCell id="n_{n["id"]}" value="{esc(n["texto"])}" style="{st}" vertex="1" parent="1">'
                  f'<mxGeometry x="{n["cx"] - HALF}" y="{n["cy"] - HALF}" width="{ICON}" height="{ICON}" as="geometry"/></mxCell>')

# título, subtítulo y pie
az_rect = cl_por_id["azure"]["rect"]
celdas.append(f'<mxCell id="titulo" value="Arquitectura física general · nube y sitios Ancoa" style="text;html=1;align=center;verticalAlign=middle;'
              f'fontSize=18;fontStyle=1;fontFamily=Helvetica;fontColor=#1A1A1A;" vertex="1" parent="1">'
              f'<mxGeometry x="{CEN - 500}" y="6" width="1000" height="26" as="geometry"/></mxCell>')
celdas.append(f'<mxCell id="subtitulo" value="Chile Central: producción · Brazil South: recuperación · Cuatro hosts por tienda · Redes Retail / Filial separadas" '
              f'style="text;html=1;align=center;verticalAlign=middle;fontSize=11;fontFamily=Helvetica;fontColor=#1A1A1A;" vertex="1" parent="1">'
              f'<mxGeometry x="{CEN - 500}" y="30" width="1000" height="18" as="geometry"/></mxCell>')
y_pie = max(c["rect"][3] for c in clusters) + 14
pie = ("Retail: azul · Filial: violeta · Cruce X-01: naranja · Administración y operación: gris discontinuo · Identidad: azul oscuro punteado · "
       "Copias/DR: verde azulado discontinuo · Energía: marrón punteado · Front Door→Application Gateway: Private Link propio / HTTPS\n"
       "Los marcos identifican sitios y segmentos reales; VLAN/VRF más firewall e identidad definen los límites. No hay acceso libre R↔F. "
       "Pares locales y equipos LAN/SD-WAN: Cisco. PaaS y AKS: Azure. Símbolos agrupados por ámbito, sin prescribir fabricante del hardware.\n"
       "Invitados: solo Internet. CCTV: NVR local. IoT: solo contrato Pedidos. Generador→ATS→UPS→PDU es suministro eléctrico, no ruta IP.\n"
       "Fuente: elaboración propia desde Bases, Caso 09, inventario y decisiones del usuario. Uso de IA Alto. Diseño sujeto a pruebas; no es despliegue acreditado.")
celdas.append(f'<mxCell id="pie" value="{esc(pie)}" style="text;html=1;align=center;verticalAlign=top;fontSize=10;fontFamily=Helvetica;fontColor=#1A1A1A;" '
              f'vertex="1" parent="1"><mxGeometry x="{CEN - 800}" y="{y_pie:.0f}" width="1600" height="64" as="geometry"/></mxCell>')

xml = ('<mxfile host="diagramas-ancoa" type="device"><diagram id="d1" name="Figura 4.52 ordenada">'
       '<mxGraphModel dx="1200" dy="800" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" '
       f'pageScale="1" pageWidth="{W_CANVAS}" pageHeight="{int(y_pie + 90)}" background="#FFFFFF" math="0" shadow="0"><root>{"".join(celdas)}</root></mxGraphModel></diagram></mxfile>')
open(sys.argv[1] if len(sys.argv) > 1 else "fig.drawio", "w", encoding="utf-8").write(xml)
print("lienzo:", W_CANVAS, "x", int(y_pie + 90))
for c in clusters:
    if c["id"] in ("azure", "chile", "brazil", "sitios"):
        print(c["id"], [round(v) for v in c["rect"]])
