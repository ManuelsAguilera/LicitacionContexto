import json
import sys
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'scripts'))
from rutas import RUTA_BORRADO, RUTA_PLAN

sys.stdout.reconfigure(encoding="utf-8")

PLAN = RUTA_PLAN
OUT = RUTA_BORRADO

with open(PLAN, encoding="utf-8") as fh:
    plan = json.load(fh)

a_borrar = list(plan["aBorrar"])
subtareas = {t["origenClave"]: t for t in plan["subtareas"] if t.get("origenClave")}
secciones = {s["clave"]: s for s in plan["secciones"]}

lineas = []
lineas.append("INCIDENCIAS ORIGINALES A BORRAR (62) — OSS")
lineas.append("Reemplazadas por las Subtareas OSS-173..OSS-235 bajo las Historias OSS-69..OSS-104.")
lineas.append("")
lineas.append("JQL para localizarlas de una sola vez:")
lineas.append("project = OSS AND key in (" + ",".join(a_borrar) + ") ORDER BY key ASC")
lineas.append("")
lineas.append("Claves (una por linea):")
for k in a_borrar:
    t = subtareas.get(k)
    dest = t["nuevaClave"] if t else "?"
    resumen = t["resumen"] if t else ""
    lineas.append("{}\t{}\t{}".format(k, dest, resumen))

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write("\n".join(lineas) + "\n")

print("Archivo:", OUT)
print("Total:", len(a_borrar))
print("JQL: project = OSS AND key in (" + ",".join(a_borrar) + ")")
