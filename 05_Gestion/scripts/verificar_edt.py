#!/usr/bin/env python3
"""Controles mecánicos de una EDT escrita en Markdown (paso 8a del plan de estimación).

Aplica a la lista de control de `80_Artefactos/sd-07_contexto/guia_edt.md` (sección 11) lo que se puede comprobar
sin criterio humano: nombres que empiezan con verbo, fechas, hitos y meses, horas y costos, códigos externos y cifras
en el nombre, varios entregables en un solo nombre, fases o actividades como nodos, nombres antiguos de servicios,
duplicados, cantidad de paquetes por rama y profundidad de los códigos. Solo informa.

Formato esperado: ramas como `### 1.2 Título — N paquetes` y paquetes como `- 1.2.3 Nombre`
(un código de varios niveles, un espacio y el nombre). Una línea `- 1.10.1 … 1.10.5 texto` cuenta como cinco paquetes.

    python3 05_Gestion/scripts/verificar_edt.py [EDT.md] [--informativo]

Código de salida 0 si no hay hallazgos y 1 si los hay. Con --informativo, los hallazgos de tipo «posible» no cuentan.
"""

import argparse
import difflib
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
EDT = RAIZ / "80_Artefactos" / "sd-07_contexto" / "estimacion" / "[ELISEO]-entregables_edt.md"
MAX_NIVELES = 4
RANGO_TOTAL = (100, 250)
MIN_POR_RAMA = 2

NOMBRES_ANTIGUOS = [
    "catálogo, precios y promociones", "abastecimiento y reposición", "inventario, reservas y disponibilidad",
    "pedidos y cumplimiento omnicanal", "registro y conciliación de ventas", "atribución de ventas y comisiones",
    "integración y gobierno del marketplace", "posventa, garantías y devoluciones", "clientes y fidelización retail",
    "originación y autorización de crédito", "cartera, cobranza y repactaciones", "consentimiento y evidencia financiera",
    "autorización y auditoría de cruces", "plataforma común", r"frontera x-01", r"\bx-01\b",
]
SUSTANTIVOS_EN_AR_ER_IR = {"taller", "lugar", "hogar", "mujer", "mayor", "menor", "calendar"}
FASES = r"marcha blanca|hypercare|estabilización|convivencia|acompañamiento|puesta en marcha"

PATRONES = [  # (código, tipo, regex, mensaje)
    ("C2", "falta", r"\bmes(es)?\s*\d+(\s*[–-]\s*\d+)?|\(\s*\d+\s*[–-]\s*\d+\s*\)|\bH\d{1,2}(/\w+)?\b|\b\d+\s*(días|dias|semanas)\b",
     "fecha, mes, hito o duración en el nombre (la EDT no es un cronograma)"),
    ("C2", "posible", r"\bhitos?\b",
     "menciona un hito (verificar que no sea una fecha)"),
    ("C3", "falta", r"\bArts?\.?\s*\d+(\.\d+)?(\s*(y|,)\s*\d+(\.\d+)?)*|\bRT-\d+(\.\d+)?|\bRNF-\d+|\bRF-\d+|\bT-\d{1,2}\b|\bE-25\b|\bRAN\s*[\d-]+|\bISO\s*\d+|\bRR-\d+|\bLey\s*[\d.]+",
     "código externo en el nombre (el nombre debe entenderse sin ellos)"),
    ("C4", "falta", r"[≤≥<>]\s*\d*\s*\w*|\b\d+\s*(ms|s|min|h)\b|\b\d+([.,]\d+)?\s*%",
     "umbral, tiempo o porcentaje en el nombre (va en el criterio de aceptación)"),
]


def leer(ruta):
    ramas, paquetes, rama = [], [], None
    for n, linea in enumerate(Path(ruta).read_text(encoding="utf-8").splitlines(), 1):
        m = re.match(r"###\s+(\d+(?:\.\d+)*)\s+(.*?)(?:\s+—\s+(\d+)\s+paquetes)?\s*$", linea)
        if m:
            rama = {"codigo": m.group(1), "titulo": m.group(2).strip(), "declarados": int(m.group(3)) if m.group(3) else None,
                    "linea": n, "paquetes": []}
            ramas.append(rama)
            continue
        m = re.match(r"-\s+(\d+(?:\.\d+)+)\s+…\s+(\d+(?:\.\d+)+)\s+(.*)$", linea)
        if m and rama is not None:
            ini, fin = int(m.group(1).rsplit(".", 1)[1]), int(m.group(2).rsplit(".", 1)[1])
            base = m.group(1).rsplit(".", 1)[0]
            for i in range(ini, fin + 1):
                p = {"codigo": f"{base}.{i}", "nombre": m.group(3).strip(), "linea": n, "rango": True}
                paquetes.append(p)
                rama["paquetes"].append(p)
            continue
        m = re.match(r"-\s+(\d+(?:\.\d+)+)\s+(.*)$", linea)
        if m and rama is not None:
            p = {"codigo": m.group(1), "nombre": m.group(2).strip(), "linea": n, "rango": False}
            paquetes.append(p)
            rama["paquetes"].append(p)
    return ramas, paquetes


def limpiar(nombre):
    return re.sub(r"\*\*\[[^\]]*\]\*\*|\[Nuevo[^\]]*\]|\(Ronda 0:[^)]*\)", "", nombre).strip()


def verificar(ruta=EDT):
    ramas, paquetes = leer(ruta)
    h = []

    def add(cod, tipo, donde, msg):
        h.append({"codigo": cod, "tipo": tipo, "donde": donde, "mensaje": msg})
    if not paquetes:
        return [{"codigo": "C0", "tipo": "falta", "donde": str(ruta), "mensaje": "no se encontraron paquetes"}]
    for r in ramas:
        for cod, tipo, rx, msg in PATRONES[:1]:
            if re.search(rx, r["titulo"]):
                add(cod, tipo, f"rama {r['codigo']}", msg + f": «{r['titulo']}»")
        n = len(r["paquetes"])
        if r["declarados"] is not None and r["declarados"] != n:
            add("C12", "falta", f"rama {r['codigo']}", f"declara {r['declarados']} paquetes y tiene {n}")
        if n < MIN_POR_RAMA:
            add("C12", "posible", f"rama {r['codigo']}", f"solo {n} paquete(s) (mínimo {MIN_POR_RAMA})")
    total = len(paquetes)
    if not RANGO_TOTAL[0] <= total <= RANGO_TOTAL[1]:
        add("C12", "posible", "EDT", f"{total} paquetes, fuera del rango de control {RANGO_TOTAL[0]} a {RANGO_TOTAL[1]}")
    nombres, lineas_rango = [], set()
    for p in paquetes:
        if p["rango"]:
            if p["linea"] in lineas_rango:
                continue
            lineas_rango.add(p["linea"])
        nombre = limpiar(p["nombre"])
        donde = f"{p['codigo']}"
        nombres.append((p["codigo"], nombre))
        if p["codigo"].count(".") + 1 > MAX_NIVELES:
            add("C0", "falta", donde, f"más de {MAX_NIVELES} niveles de código")
        primera = re.match(r"[A-Za-zÁÉÍÓÚÑáéíóúñ]+", nombre)
        if primera:
            w = primera.group(0)
            if len(w) >= 5 and re.search(r"(ar|er|ir)$", w, re.I) and w.lower() not in SUSTANTIVOS_EN_AR_ER_IR:
                add("C6", "falta", donde, f"el nombre empieza con un verbo en infinitivo: «{w}»")
        for cod, tipo, rx, msg in PATRONES:
            m = re.search(rx, nombre, 0 if cod == "C2" and tipo == "falta" else re.I)
            if m:
                add(cod, tipo, donde + (" a " + [q["codigo"] for q in paquetes if q["linea"] == p["linea"]][-1] if p["rango"] else ""), f"{msg}: «{m.group(0).strip()}»")
        sin_parentesis = re.sub(r"\([^)]*\)", "", nombre)
        if (";" in sin_parentesis or " + " in sin_parentesis or len(re.findall(r" y ", sin_parentesis)) >= 2
                or re.search(r" y [A-ZÁÉÍÓÚ]", sin_parentesis) or sin_parentesis.count(",") >= 3
                or (":" in sin_parentesis and "," in sin_parentesis)):
            add("C8", "posible", donde, "posibles varios entregables en un solo nombre")
        if re.search(FASES, nombre, re.I) and not re.search(r"\b(plan|informe|acta|evidencia|protocolo|estrategia|certificaci)", nombre, re.I):
            add("C5", "posible", donde, "posible fase o actividad como nodo, no un entregable")
        if re.search(r"^\s*(" + "|".join(NOMBRES_ANTIGUOS) + ")", nombre, re.I) or any(re.search(a, nombre, re.I) for a in NOMBRES_ANTIGUOS):
            add("C13", "falta", donde, "nombre antiguo de un servicio (usar la nomenclatura vigente del sd-03)")
    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            if nombres[i][1] and nombres[i][1] == nombres[j][1] or difflib.SequenceMatcher(None, nombres[i][1].lower(), nombres[j][1].lower()).ratio() >= 0.9:
                if nombres[i][1] != "" and not re.search(r"…|innovación", nombres[i][1]):
                    add("C9", "posible", f"{nombres[i][0]} y {nombres[j][0]}", "nombres casi idénticos (posible duplicado)")
    return h


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("edt", nargs="?", default=str(EDT))
    ap.add_argument("--informativo", action="store_true", help="los hallazgos «posible» no cuentan para el código de salida")
    a = ap.parse_args(argv)
    hs = verificar(a.edt)
    for x in hs:
        print(f"{x['codigo']} [{x['tipo']}] {x['donde']}: {x['mensaje']}")
    firmes = [x for x in hs if x["tipo"] == "falta"]
    print(f"{len(hs)} hallazgo(s): {len(firmes)} firmes y {len(hs) - len(firmes)} posibles")
    cuenta = firmes if a.informativo else hs
    return 1 if cuenta else 0


if __name__ == "__main__":
    sys.exit(main())
