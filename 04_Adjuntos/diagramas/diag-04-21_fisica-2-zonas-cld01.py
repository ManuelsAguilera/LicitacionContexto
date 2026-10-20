"""Vista física 2 de 3: CLD-01 por zona de disponibilidad (lectura de fallas).

Responde: ¿qué nodo corre en cada zona, cuánto aguanta y qué pasa si cae una zona?
Filas por ámbito y columnas por zona (FEP01, diap. 93 y 101: redundancia explícita y N+1).
Fuente: SD-04, Tabla 4.13, y la memoria 04_Adjuntos/tablas/sd-04_s2_dimensionamiento-nodos.md.
Ejecutar: python3 04_Adjuntos/diagramas/diag-04-21_fisica-2-zonas-cld01.py
"""

from pathlib import Path

from _alcance import czone, ring
from _drawio import ACCENT, Diagram

d = Diagram(font=21, zone_font=24)

X0, LW = 20, 250          # columna de rótulos
COLS = [("Zona 1", 500), ("Zona 2", 500), ("Zona 3", 500), ("Repartido por el servicio entre zonas", 560)]
ROWS = [("Retail\n10.10.16.0/20", 330), ("Emisor\n10.10.32.0/20", 300), ("Base tecnológica\n10.10.48.0/21", 250),
        ("Hub\n(Conectividad)", 250)]

czone(d, X0, 20, LW + sum(w for _, w in COLS) + 20 * len(COLS) + 20, 110 + sum(h for _, h in ROWS) + 20 * len(ROWS),
      "CLD-01 · Azure Chile Central · Producción", "oss", align="left")
xs, x = [], X0 + LW + 20
for t, w in COLS:
    ring(d, x, 80, w, 50 + sum(h for _, h in ROWS) + 20 * len(ROWS), t)
    xs.append(x)
    x += w + 20
ys, y = [], 140
for t, h in ROWS:
    d.text(X0 + 10, y, LW - 10, h, t, size=23, bold=True, align="left", color="#0078D4")
    ys.append(y)
    y += h + 20
    if len(ys) < len(ROWS):
        d.cells.append(f'<mxCell id="{d._id("l")}" style="endArrow=none;html=1;strokeColor=#9AB8D8;strokeWidth=2;" edge="1" parent="1">'
                       f'<mxGeometry relative="1" as="geometry"><mxPoint x="{X0 + 10}" y="{y - 10}" as="sourcePoint"/>'
                       f'<mxPoint x="{x - 20}" y="{y - 10}" as="targetPoint"/></mxGeometry></mxCell>')


def cell(r, c, items):
    """Íconos en columna con su rótulo a la derecha."""
    x, y = xs[c] + 18, ys[r] + 8
    h = (ROWS[r][1] - 10) / max(len(items), 1)
    ids = []
    for name, label in items:
        ids.append(d.icon(x, round(y + (h - 46) / 2), name, label, size=46, label_pos="right"))
        y += h
    return ids


AKS_R = "AKS: 2 × D8ds_v5 usuario\n+ 1 × D4ds_v5 sistema"
cell(0, 0, [("appgw", "App Gateway v2, instancia"), ("apim", "API Management, unidad 1"), ("aks", AKS_R),
            ("postgres", "PostgreSQL D8ds_v5 · PRIMARIO\n2 TiB · 7.500 IOPS")])
cell(0, 1, [("appgw", "App Gateway v2, instancia"), ("apim", "API Management, unidad 2"), ("aks", AKS_R),
            ("postgres", "PostgreSQL D8ds_v5 · EN ESPERA\ncopia síncrona")])
cell(0, 2, [("apim", "API Management, unidad 3"), ("aks", AKS_R), ("aks", "Grupo predictivo\n0 a 2 × D8ds_v5")])
cell(0, 3, [("eventhubs", "Event Hubs Premium, 2 PU\ntres copias entre zonas"), ("mredis", "Managed Redis B5 6 GB\nprimario y réplica"),
            ("datalake", "Data Lake Gen2 ZRS, 1 TB"), ("keyvault", "Key Vault Premium")])
AKS_E = "AKS: 1 × D4ds_v5 usuario\n+ 1 × D4ds_v5 sistema"
cell(1, 0, [("apim", "API Management, unidad 1"), ("aks", AKS_E), ("postgres", "PostgreSQL D4ds_v5 · PRIMARIO\n512 GiB · 2.300 IOPS")])
cell(1, 1, [("apim", "API Management, unidad 2"), ("aks", AKS_E), ("postgres", "PostgreSQL D4ds_v5 · EN ESPERA")])
cell(1, 2, [("apim", "API Management, unidad 3"), ("aks", AKS_E)])
cell(1, 3, [("eventhubs", "Event Hubs Premium, 1 PU"), ("storage", "Blob inmutable ZRS, 9 TB"),
            ("hsm", "Managed HSM"), ("keyvault", "Key Vault Premium")])
AKS_B = "AKS: 1 × D8ds_v5 usuario\n+ 1 × D4ds_v5 sistema"
cell(2, 0, [("aks", AKS_B), ("postgres", "PostgreSQL X-01 D2ds_v5\nPRIMARIO · 128 GiB")])
cell(2, 1, [("aks", AKS_B), ("postgres", "PostgreSQL X-01 · EN ESPERA")])
cell(2, 2, [("aks", AKS_B)])
cell(2, 3, [("acr", "Container Registry Premium\nréplica a CLD-02"), ("devpools", "Agentes CI/CD, 2 × D4ds_v5")])
cell(3, 0, [("fw_site", "FortiGate-VM F4s_v2 · ACTIVO"), ("firewall", "Azure Firewall, instancia")])
cell(3, 1, [("fw_site", "FortiGate-VM F4s_v2 · PASIVO"), ("firewall", "Azure Firewall, instancia")])
cell(3, 2, [("firewall", "Azure Firewall, instancia")])
cell(3, 3, [("vpngw", "ErGw1AZ y VpnGw2AZ\nredundantes entre zonas"), ("bastion", "Bastion y Route Server"),
            ("ddos", "DDoS, NAT y DNS privado")])

# ---- prueba de falla ----
yb = 140 + sum(h for _, h in ROWS) + 20 * len(ROWS) + 40
czone(d, X0, yb, LW + sum(w for _, w in COLS) + 20 * len(COLS) + 20, 200, "Prueba de falla: cae la Zona 1", "oss", align="left", fill=False)
d.text(X0 + 20, yb + 48, LW + sum(w for _, w in COLS) + 20 * len(COLS) - 20, 140,
       "AKS sigue en dos zonas: Retail al 93 %, Emisor al 81 % y base tecnológica al 66 % de uso en el peak, y escala hasta su máximo.   "
       "PostgreSQL promueve la espera de la Zona 2 en 60 a 120 s, sin pérdida de datos.   API Management y App Gateway atienden desde "
       "las otras zonas.   Event Hubs, Redis, Key Vault y Firewall no pierden datos.   El FortiGate pasivo de la Zona 2 asume los túneles en segundos.",
       size=22, align="left")

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
