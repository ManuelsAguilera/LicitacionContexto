"""Figura 4.18: centro de datos primario, Azure Chile Central.

Responde: ¿qué servicios corren en cada zona de la región principal y cuáles se reparten entre zonas?
Se dibuja el ámbito Retail. El de la filial emisora sigue el mismo patrón, sin Redis.
Vista de detalle (redibujada, no recortada del maestro: RR-13). Letra de 32 sobre ~1700.
Ejecutar: python3 04_Adjuntos/diagramas/diag-04-18_data-center-primario.py
"""

from pathlib import Path

from _drawio import ACCENT, Diagram

d = Diagram(font=32, zone_font=32)
Z = d.zone
W = 3

Z(20, 20, 1660, 1090, "CLD-01 Chile Central  ·  ámbito Retail", "region", align="left")

XC = [40, 585, 1130]  # columnas de las tres zonas
ZW = 520
zones = [Z(x, 85, ZW, 640, f"Zona {i + 1}", "subnet") for i, x in enumerate(XC)]
ix = [x + ZW // 2 - 35 for x in XC]  # x de los íconos, centrados en cada zona

# fila 1: API Management, una unidad por zona
for i in range(3):
    d.icon(ix[i], 155, "apim", f"API Management\n(unidad {i + 1})", size=70)
# fila 2: AKS con sus dos pools
aks = [d.icon(ix[i], 345, "aks", "AKS\n(pool de sistema\ny de usuario)", size=70) for i in range(3)]
# fila 3: PostgreSQL primario en la zona 1 y en espera en la zona 2
pg1 = d.icon(ix[0], 555, "postgres", "PostgreSQL\nprimario", size=70)
pg2 = d.icon(ix[1], 555, "postgres", "PostgreSQL\nen espera", size=70)
d.edge(pg1, pg2, "copia síncrona", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5))

# ---- Servicios que se reparten entre zonas ----
band = Z(40, 750, 1620, 270, "Servicios repartidos entre las tres zonas", "inner")
items = [("eventhubs", "Event Hubs\nPremium"), ("mredis", "Azure Managed\nRedis"), ("datalake", "Data Lake\nStorage Gen2"),
         ("keyvault", "Key Vault"), ("firewall", "Azure Firewall\nPremium"), ("fw_site", "FortiGate-VM\n(zonas 1 y 2)")]
d.fill(band, items, size=70, top=60)

d.text(40, 1040, 1620, 56, "Ámbito Emisor: mismo patrón, sin Redis y con Managed HSM", size=32, bold=True, color=ACCENT)

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
