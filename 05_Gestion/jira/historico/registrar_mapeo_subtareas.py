import json
import sys
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'scripts'))
from rutas import RUTA_MAPEO_CSV, RUTA_PLAN

sys.stdout.reconfigure(encoding="utf-8")

PLAN = RUTA_PLAN
PRIMERA_NUEVA = 173  # OSS-173

with open(PLAN, encoding="utf-8") as fh:
    plan = json.load(fh)

subtareas = plan["subtareas"]
assert len(subtareas) == 63, len(subtareas)

for i, t in enumerate(subtareas):
    t["nuevaClave"] = "OSS-{}".format(PRIMERA_NUEVA + i)

a_borrar = set(plan["aBorrar"])
origenes = {t["origenClave"] for t in subtareas if t.get("origenClave")}
nuevas_sin_origen = [t for t in subtareas if not t.get("origenClave")]

assert a_borrar == origenes, sorted(a_borrar ^ origenes)
assert len(nuevas_sin_origen) == 1, nuevas_sin_origen

with open(PLAN, "w", encoding="utf-8") as fh:
    json.dump(plan, fh, ensure_ascii=False, indent=2)

secciones = {s["clave"]: s for s in plan["secciones"]}
agrupadoras = {a["id"]: a for a in plan["agrupadoras"]}
lineas = ["origen,nueva,seccion,seccion_resumen,agrupadora,subtarea_resumen,tipo_original,etiquetas"]
for t in subtareas:
    sec = secciones[t["seccion"]]
    lineas.append(
        "{origen},{nueva},{seccion},{seccion_resumen},{agrupadora},{resumen},{tipo},{etiquetas}".format(
            origen=t.get("origenClave", "NUEVA"),
            nueva=t["nuevaClave"],
            seccion=t["seccion"],
            seccion_resumen=sec["resumen"],
            agrupadora=agrupadoras[sec["agrupadora"]]["clave"],
            resumen=t["resumen"],
            tipo=t["tipoOriginal"],
            etiquetas="|".join(t["etiquetas"]),
        )
    )

with open(RUTA_MAPEO_CSV, "w", encoding="utf-8", newline="") as fh:
    fh.write("\n".join(lineas) + "\n")

print("subtareas con nuevaClave:", sum(1 for t in subtareas if t.get("nuevaClave")))
print("rango:", subtareas[0]["nuevaClave"], "->", subtareas[-1]["nuevaClave"])
print("aBorrar coincide con origenes:", a_borrar == origenes, len(a_borrar))
print("subtarea nueva (sin origen):", nuevas_sin_origen[0]["nuevaClave"], "->", nuevas_sin_origen[0]["seccion"])
print("CSV filas:", len(lineas) - 1)
