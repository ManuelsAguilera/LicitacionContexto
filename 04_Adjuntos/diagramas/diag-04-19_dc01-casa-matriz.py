"""Figura 4.19: DC-01, recinto técnico de casa matriz.

Responde: ¿qué hay dentro de DC-01 y cómo se separan Retail y la filial emisora?
Vista de detalle (redibujada, no recortada del maestro: RR-13). Letra de 32 sobre ~1720.
Ejecutar: python3 04_Adjuntos/diagramas/diag-04-19_dc01-casa-matriz.py
"""

import re
from pathlib import Path

from _drawio import Diagram

d = Diagram(font=32, zone_font=32)
Z, F = d.zone, d.fill
W = 3

Z(20, 20, 1250, 1090, "DC-01  ·  recinto técnico de casa matriz (140 m²)", "onprem", align="left")

# ---- Servidores y almacenamiento, separados por ámbito ----
zr = Z(40, 85, 270, 770, "Zona Retail", "inner")
F(zr, [("srv", "ERP/DTE"), ("srv", "Sistema\nnúcleo 2009"), ("san", "SAN\nRetail"), ("nvr", "Respaldo\nlocal")],
  cols=1, size=70, top=50)
ze = Z(325, 85, 270, 770, "Zona Emisor", "inner")
F(ze, [("srv", "Crédito\n2011"), ("san", "SAN\nEmisor"), ("nvr", "Respaldo\nlocal")], cols=1, size=70, top=50)
zc = Z(610, 85, 270, 770, "Fuera de línea", "inner")
F(zc, [("san", "Cinta en\ncustodia")], cols=1, size=70, top=50)

# ---- Rack de comunicaciones ----
rc = Z(910, 85, 340, 770, "Comunicaciones", "subnet")
ha = Z(925, 135, 310, 330, "Par HA (activo-pasivo)", "inner")
fg1, fg2 = F(ha, [("fw_site", "FortiGate\n1"), ("fw_site", "FortiGate\n2")], size=70, top=50)
co = Z(925, 495, 310, 330, "Switches de núcleo (pila)", "inner")
F(co, [("switch", "Switch 1"), ("switch", "Switch 2")], size=70, top=50)
d.edge(ha, co, "a ambos switches", width=W, both=True, exit=(0.5, 1), entry=(0.5, 0))

# ---- Instalaciones del recinto ----
Z(40, 880, 1210, 215, "Instalaciones del recinto", "band")
d.text(50, 930, 1190, 160,
       "UPS de 30 minutos  ·  generador de 24 horas  ·  climatización N+1\n"
       "detección temprana por aspiración  ·  extinción por agente limpio\n"
       "control biométrico  ·  CCTV de 30 días  ·  NOC en sala separada", size=32)

# ---- Hacia Azure y DC-02 ----
sal = Z(1310, 20, 380, 1090, "Hacia Azure y DC-02", "plain")
era, erb, vpn, dc2 = F(sal, [("ercircuit", "ExpressRoute\nproveedor A"), ("ercircuit", "ExpressRoute\nproveedor B"),
                             ("vpngw", "VPN de\nrespaldo"), ("server", "DC-02\nsala de respaldo")], cols=1, size=70, top=60)

d.edge(ha, era, "propuesto", line="dashed", width=W, exit=(1, 0.15), entry=(0, 0.5))
d.edge(ha, erb, "", line="dashed", width=W, exit=(1, 0.35), entry=(0, 0.5))
d.edge(ha, vpn, "", line="dotted", width=W, exit=(1, 0.65), entry=(0, 0.5))
d.edge(co, dc2, "", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5))

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
