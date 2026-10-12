"""Figura 4.17: tienda tipo y segmentación local.

Responde: ¿qué equipo se instala en una tienda y cómo se separan sus redes?
Vista de detalle (redibujada, no recortada del maestro: RR-13). Letra de 33 sobre ~1760:
a ancho de página (~499 pt) queda sobre 9 pt.
Ejecutar: python3 04_Adjuntos/diagramas/diag-04-17_tienda-tipo.py
"""

import re
from pathlib import Path

from _drawio import Diagram

d = Diagram(font=33, zone_font=33)
Z, F = d.zone, d.fill
W = 3

# ---- Redes por función (una VLAN cada una) ----
Z(20, 20, 980, 1010, "Redes por función (una VLAN cada una)", "plain")
v = [Z(35 + (i % 2) * 470, 75 + (i // 2) * 315, 455, 295, t, "subnet") for i, t in enumerate([
    "VLAN cajas", "VLAN administración", "VLAN móviles", "VLAN video",
    "VLAN Wi-Fi clientes", "VLAN del Emisor"])]
F(v[0], [("pos", "POS"), ("handheld", "Terminal\nde pago"), ("printer", "Impresora\nfiscal")], size=70, top=60)
F(v[1], [("workstation", "PC"), ("printer", "Impresora\nde etiquetas")], size=70, top=60)
F(v[2], [("cell", "Móviles\ncompartidos"), ("ap", "AP\ncorporativo")], size=70, top=60)
F(v[3], [("camera", "Cámaras"), ("nvr", "NVR\n30 días")], size=70, top=60)
F(v[4], [("ap", "AP de clientes\n(aislado)")], size=70, top=60)
F(v[5], [("workstation", "Puesto del Emisor\n(túnel propio)")], size=70, top=60)

# ---- Gabinete de comunicaciones y nodo local ----
Z(1090, 20, 380, 1010, "Gabinete y nodo local", "onprem")
ha = Z(1105, 75, 350, 225, "Par HA (activo-pasivo)", "inner")
fg1, fg2 = F(ha, [("fw_site", "FortiGate 1\n(activo)"), ("fw_site", "FortiGate 2\n(pasivo)")], size=70, top=56)
st = Z(1105, 320, 350, 225, "Switches (pila)", "inner")
sw1, sw2 = F(st, [("switch_acc", "Switch 1"), ("switch_acc", "Switch 2")], size=70, top=56)
nd = Z(1105, 565, 350, 225, "Nodo local (RAID 1)", "inner")
n1, n2 = F(nd, [("srv", "Servidor 1\n(activo)"), ("srv", "Servidor 2\n(en espera)")], size=70, top=56)
up = Z(1105, 810, 350, 200, "Energía", "inner")
ups, = F(up, [("ups", "UPS")], size=70, top=56)

# ---- Salida hacia Azure ----
sal = Z(1510, 20, 230, 1010, "Hacia Azure", "plain")
inet, lte = F(sal, [("cloud", "Internet\n(SD-WAN)"), ("antenna", "Respaldo\nLTE/5G")], cols=1, size=70, top=60)

# ---- Aristas ----
d.edge(st, v[2].replace('z', 'z') if False else "z1", "", width=W) if False else None
blk = [k for k, r in d.rects.items() if r[0] == 20 and r[1] == 20][0]
d.edge(st, blk, "troncal", width=W, exit=(0, 0.5), entry=(1, 0.5))
d.edge(ha, st, "a ambos switches", width=W, both=True, exit=(0.5, 1), entry=(0.5, 0))
d.edge(nd, st, "", width=W, exit=(0.5, 0), entry=(0.5, 1))
d.edge(ha, inet, "", width=W, exit=(1, 0.3), entry=(0, 0.5))
d.edge(ha, lte, "", line="dashed", width=W, exit=(1, 0.7), entry=(0, 0.5))

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
