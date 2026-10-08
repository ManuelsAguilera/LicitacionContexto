#!/usr/bin/env python3
"""Segunda vía independiente para UAW, UUCW y UUCP (paso 4, puerta G4).

No importa ningún otro script del repositorio. Relee los archivos de Markdown con su propia lectura
(cuenta las transacciones `T1`, `T2`... del detalle de cada caso, no la columna declarada), aplica los
pesos de la clase (diap. 26 y 29) y compara con el JSON de `generar_entrada_ucp.py`. Informa también el
reparto de casos, el UUCW por servicio y etapa y la participación de los actores en el UUCP.

    python3 05_Gestion/scripts/recalcular_uucp.py [--json RUTA] [--dir RUTA] [--actores RUTA]

Código de salida 0 si las dos vías coinciden exactamente y 1 si no.
"""

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DIR = RAIZ / "80_Artefactos" / "sd-07_contexto" / "estimacion"
ETAPA_1 = ("EX", "OF", "VE", "OR", "EV", "CC", "CA", "BT")


def peso_caso(n):
    return 5 if n <= 3 else (10 if n <= 7 else 15)


def leer(directorio, actores):
    por_caso = {}
    for p in sorted(Path(directorio).glob("03_casos_de_uso_*.md")):
        for linea in p.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\|\s*(CU-[A-Z]{2}-\d+)\s*\|(.*)\|\s*$", linea)
            if not m:
                continue
            resto = m.group(2)
            if re.search(r"\bT1\b", resto):  # fila de la tabla de transacciones
                por_caso[m.group(1)] = len(re.findall(r"\bT\d+\b", resto))
    tipos = {}
    for linea in Path(actores).read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(A[HS]-\d+)\s*\|[^|]*\|\s*([123])\s*\|", linea)
        if m:
            tipos[m.group(1)] = int(m.group(2))
    return por_caso, tipos


def calcular(por_caso, tipos):
    uaw = sum(tipos.values())  # el tipo coincide con el peso: 1, 2 o 3
    uucw = sum(peso_caso(n) for n in por_caso.values())
    reparto = {"simple": 0, "medio": 0, "complejo": 0}
    por_servicio, por_etapa = {}, {1: 0, 2: 0}
    for cod, n in por_caso.items():
        pref = cod.split("-")[1]
        reparto["simple" if n <= 3 else "medio" if n <= 7 else "complejo"] += 1
        por_servicio[pref] = por_servicio.get(pref, 0) + peso_caso(n)
        por_etapa[1 if pref in ETAPA_1 else 2] += peso_caso(n)
    return {"UAW": uaw, "UUCW": uucw, "UUCP": uaw + uucw, "reparto": reparto,
            "por_servicio": por_servicio, "por_etapa": por_etapa, "casos": len(por_caso), "actores": len(tipos),
            "transacciones": sum(por_caso.values())}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", default=str(DIR / "07_entrada_calculadora.json"))
    ap.add_argument("--dir", default=str(DIR))
    ap.add_argument("--actores", default=str(DIR / "02_actores_uaw.md"))
    a = ap.parse_args(argv)
    por_caso, tipos = leer(a.dir, a.actores)
    r = calcular(por_caso, tipos)
    j = json.loads(Path(a.json).read_text(encoding="utf-8"))["resultado"]
    print(f"Segunda vía: {r['actores']} actores, {r['casos']} casos, {r['transacciones']} transacciones")
    print(f"UAW {r['UAW']}  UUCW {r['UUCW']}  UUCP {r['UUCP']}")
    print(f"Reparto: {r['reparto']['simple']} simples, {r['reparto']['medio']} medios, {r['reparto']['complejo']} complejos")
    print("UUCW por etapa: " + ", ".join(f"Etapa {e} = {v}" for e, v in sorted(r["por_etapa"].items())))
    print("UUCW por servicio: " + ", ".join(f"{k} {v}" for k, v in sorted(r["por_servicio"].items())))
    print(f"Participación de los actores en el UUCP: {r['UAW'] / r['UUCP']:.1%}")
    ok = all(r[k] == j[k] for k in ("UAW", "UUCW", "UUCP"))
    print(f"Primera vía (calculadora): UAW {j['UAW']}  UUCW {j['UUCW']}  UUCP {j['UUCP']}")
    print("COINCIDEN" if ok else "NO COINCIDEN")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
