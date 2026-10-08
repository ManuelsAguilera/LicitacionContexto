#!/usr/bin/env python3
"""Genera la entrada de la calculadora de UCP (paso 4, puerta G4) desde las tablas del modelo.

Lee los tipos de actor de `02_actores_uaw.md` y las transacciones de los `03_casos_de_uso_*.md`
(vía `verificar_casos_uso.py`) y escribe el JSON con `actores`, `casos` y el detalle por actor y caso.
No incluye `tcf` ni `ef`: los fijan los pasos 5 y 6. Calcula UAW, UUCW y UUCP con `estimacion_ucp.py`.

    python3 05_Gestion/scripts/generar_entrada_ucp.py [--salida RUTA.json] [--dir RUTA] [--actores RUTA]
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import estimacion_ucp as calc  # noqa: E402
import verificar_casos_uso as vcu  # noqa: E402

ETAPA_1 = {"EX", "OF", "VE", "OR", "EV", "CC", "CA", "BT"}
SALIDA = vcu.DIR / "07_entrada_calculadora.json"


def leer_actores(ruta):
    """[{codigo, nombre, tipo}] desde las filas `| AH-01 | nombre | 3 | ... |` de `02_actores_uaw.md`."""
    out = []
    for linea in Path(ruta).read_text(encoding="utf-8").splitlines():
        c = vcu.celdas(linea) if linea.startswith("|") else []
        if len(c) >= 3 and re.fullmatch(r"A[HS]-\d+", c[0]) and c[2] in ("1", "2", "3"):
            out.append({"codigo": c[0], "nombre": c[1], "tipo": int(c[2])})
    return out


def generar(directorio=vcu.DIR, actores=vcu.ACTORES):
    casos, _ = vcu.leer_casos(directorio)
    act = leer_actores(actores)
    detalle = []
    for c in casos:
        pref = c["codigo"].split("-")[1]
        detalle.append({"codigo": c["codigo"], "servicio": pref, "etapa": 1 if pref in ETAPA_1 else 2,
                        "transacciones": int(c["trans"])})
    entrada = {
        "actores": [a["tipo"] for a in act],
        "casos": [d["transacciones"] for d in detalle],
        "actores_detalle": act,
        "casos_detalle": detalle,
    }
    entrada["resultado"] = {"UAW": calc.uaw(entrada["actores"]), "UUCW": calc.uucw(entrada["casos"]),
                            "UUCP": calc.uucp(entrada["actores"], entrada["casos"])}
    return entrada


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--salida", default=str(SALIDA))
    ap.add_argument("--dir", default=str(vcu.DIR))
    ap.add_argument("--actores", default=str(vcu.ACTORES))
    a = ap.parse_args(argv)
    e = generar(a.dir, a.actores)
    Path(a.salida).write_text(json.dumps(e, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    r = e["resultado"]
    print(f"{len(e['actores'])} actores, {len(e['casos'])} casos -> UAW {r['UAW']}  UUCW {r['UUCW']}  UUCP {r['UUCP']}")
    print(f"escrito en {a.salida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
