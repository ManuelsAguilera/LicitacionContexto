import json
import sys
from rutas import RUTA_PLAN

sys.stdout.reconfigure(encoding="utf-8")

PLAN = RUTA_PLAN

with open(PLAN, encoding="utf-8") as fh:
    plan = json.load(fh)

secciones = {s["clave"]: s for s in plan["secciones"]}
actual = None
n = 0
for t in plan["subtareas"]:
    if t["seccion"] != actual:
        actual = t["seccion"]
        n = 0
        print()
        print("== {} | {}".format(actual, secciones[actual]["resumen"]))
    n += 1
    print("  {}. [{}] {}  # origen {}".format(n, t["tipoOriginal"], t["resumen"], t.get("origenClave", "NUEVA")))
print()
print("TOTAL", len(plan["subtareas"]))
