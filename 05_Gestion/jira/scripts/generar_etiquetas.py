import json
import sys
from rutas import RUTA_ETIQUETAS, RUTA_PLAN

sys.stdout.reconfigure(encoding="utf-8")

PLAN = RUTA_PLAN
OUT = RUTA_ETIQUETAS

with open(PLAN, encoding="utf-8") as fh:
    plan = json.load(fh)

etiquetas = {}
for a in plan["agrupadoras"]:
    etiquetas[a["clave"]] = a["etiquetas"]
for s in plan["secciones"]:
    etiquetas[s["clave"]] = s["etiquetas"]
for t in plan["subtareas"]:
    etiquetas[t["nuevaClave"]] = t["etiquetas"]

with open(OUT, "w", encoding="utf-8") as fh:
    json.dump(etiquetas, fh, ensure_ascii=False, indent=2)

print("total incidencias a etiquetar:", len(etiquetas))
print("ejemplos:")
for k in ("OSS-165", "OSS-72", "OSS-173", "OSS-235"):
    print(" ", k, etiquetas[k])
