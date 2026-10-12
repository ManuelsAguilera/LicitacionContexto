"""Figura 4.15: ambientes y flujo de despliegue (tercera versión, en vertical).

Responde: ¿por qué ambientes pasa el código hasta llegar a producción, en qué región vive cada uno y qué es de cada ámbito?
Cada ambiente tiene una suscripción y un Key Vault por ámbito (cajas Retail y Emisor).
Vista de detalle (redibujada, no recortada del maestro: RR-13). Letra de 32 sobre ~1700.
Ejecutar: python3 04_Adjuntos/diagramas/diag-04-15_ambientes-y-despliegue.py
"""

from pathlib import Path

from _drawio import ACCENT, Diagram

d = Diagram(font=32, zone_font=32)
Z, F = d.zone, d.fill
W = 3

# ---- Entrega: del código a la imagen firmada ----
ent = Z(20, 20, 1660, 250, "Entrega", "plain", align="left")
F(ent, [("repo", "Repositorio\ndel código"), ("devops", "Entrega continua\n(revisión y firma)"),
        ("acr", "Registro de\nimágenes")], size=70, top=50)

# ---- Regiones ----
Z(20, 340, 1660, 1120, "CLD-01 Chile Central", "region", align="left")
Z(20, 1530, 1660, 330, "CLD-02 Brazil South", "region", align="left")

rows = [("Desarrollo", "se construye", 410), ("QA", "se prueba la calidad", 680),
        ("Preproducción", "se ensaya con carga", 950), ("Producción", "atiende a las tiendas", 1220),
        ("Recuperación", "se crea si hay falla", 1600)]
envs = []
for t, why, y in rows:
    cond = t == "Recuperación"
    e = Z(40, y, 1620, 200, t, "vnet", align="left")
    d.text(60, y + 60, 520, 110, why, size=32)
    Z(600, y + 20, 500, 160, "Retail", "inner")
    d.text(610, y + 80, 480, 90, "suscripción y Key Vault", size=32)
    Z(1130, y + 20, 500, 160, "Emisor (condicionado)" if cond else "Emisor", "vnet_cond" if cond else "inner")
    d.text(1140, y + 80, 480, 90, "suscripción y Key Vault", size=32)
    envs.append(e)

# ---- Aristas ----
d.edge(ent, envs[0], "despliega", width=W, exit=(0.5, 1), entry=(0.5, 0))
d.edge(envs[0], envs[1], "", width=W, exit=(0.5, 1), entry=(0.5, 0))
d.edge(envs[1], envs[2], "", width=W, exit=(0.5, 1), entry=(0.5, 0))
d.edge(envs[2], envs[3], "aprobación", color=ACCENT, width=W + 1, exit=(0.5, 1), entry=(0.5, 0))
d.edge(envs[3], envs[4], "mismo código", line="dashed", width=W, exit=(0.5, 1), entry=(0.5, 0))

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
