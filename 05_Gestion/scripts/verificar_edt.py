#!/usr/bin/env python3
"""Controles mecánicos de una EDT escrita en Markdown (paso 8a del plan de estimación).

Aplica a la lista de control de `80_Artefactos/sd-07_contexto/guia_edt.md` (sección 11) lo que se puede comprobar
sin criterio humano: nombres que empiezan con verbo, fechas, hitos y meses, horas y costos, códigos externos y cifras
en el nombre, varios entregables en un solo nombre, fases o actividades como nodos, nombres antiguos de servicios,
duplicados, cantidad de paquetes por rama y profundidad de los códigos. Solo informa.

Formato esperado: ramas como `### 1.2 Título — N paquetes`, nodos opcionales de servicio como `#### 1.5.1 Título — N paquetes`
y paquetes como `- 1.2.3 Nombre {atributos}` (un código de varios niveles, un espacio y el nombre). Una línea
`- 1.10.1 … 1.10.5 texto` cuenta como cinco paquetes. El bloque final `{casos: ...; etapa: ...; origen: ...}` no forma parte del nombre.
Si algún paquete trae atributos, todos deben traer `etapa:` y `casos:` o `ucp: no`.

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
NODO_MIN, NODO_MAX = 3, 8  # paquetes por servicio, acordado el 2026-10-08

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


CLAVES_ATRIBUTO = {"casos", "ucp", "nivel", "etapa", "origen"}
ATRIBUTOS = re.compile(r"\s*\{([^{}]*)\}\s*$")


def separar_atributos(texto):
    """(nombre, {clave: valor}) separando el bloque final `{k: v; k: v}`."""
    m = ATRIBUTOS.search(texto)
    if not m:
        return texto.strip(), {}
    attrs, ultima = {}, None
    for trozo in m.group(1).split(";"):
        k = trozo.split(":", 1)[0].strip() if ":" in trozo else None
        if k in CLAVES_ATRIBUTO:
            attrs[k] = trozo.split(":", 1)[1].strip()
            ultima = k
        elif ultima and trozo.strip():
            attrs[ultima] += "; " + trozo.strip()  # un «;» dentro del valor, por ejemplo en origen
    return texto[:m.start()].strip(), attrs


def leer(ruta):
    ramas, paquetes, rama, nodo = [], [], None, None
    for n, linea in enumerate(Path(ruta).read_text(encoding="utf-8").splitlines(), 1):
        m = re.match(r"####\s+(\d+(?:\.\d+)+)\s+(.*?)(?:\s+—\s+(\d+)\s+(?:paquetes|cuentas de control))?\s*$", linea)
        if m and rama is not None:
            nodo = {"codigo": m.group(1), "titulo": m.group(2).strip(), "declarados": int(m.group(3)) if m.group(3) else None,
                    "linea": n, "paquetes": []}
            rama.setdefault("nodos", []).append(nodo)
            continue
        m = re.match(r"###\s+(\d+(?:\.\d+)*)\s+(.*?)(?:\s+—\s+(\d+)\s+(?:paquetes|cuentas de control))?\s*$", linea)
        if m:
            rama = {"codigo": m.group(1), "titulo": m.group(2).strip(), "declarados": int(m.group(3)) if m.group(3) else None,
                    "linea": n, "paquetes": []}
            ramas.append(rama)
            nodo = None
            continue
        m = re.match(r"-\s+(\d+(?:\.\d+)+)\s+…\s+(\d+(?:\.\d+)+)\s+(.*)$", linea)
        if m and rama is not None:
            ini, fin = int(m.group(1).rsplit(".", 1)[1]), int(m.group(2).rsplit(".", 1)[1])
            base = m.group(1).rsplit(".", 1)[0]
            for i in range(ini, fin + 1):
                nom, attrs = separar_atributos(m.group(3))
                p = {"codigo": f"{base}.{i}", "nombre": nom, "atributos": attrs, "linea": n, "rango": True}
                paquetes.append(p)
                rama["paquetes"].append(p)
            continue
        m = re.match(r"-\s+(\d+(?:\.\d+)+)\s+(.*)$", linea)
        if m and rama is not None:
            nom, attrs = separar_atributos(m.group(2))
            p = {"codigo": m.group(1), "nombre": nom, "atributos": attrs, "linea": n, "rango": False}
            paquetes.append(p)
            rama["paquetes"].append(p)
            if nodo is not None and p["codigo"].startswith(nodo["codigo"] + "."):
                nodo["paquetes"].append(p)
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
        for nd in r.get("nodos", []):
            k = len(nd["paquetes"])
            if nd["declarados"] is not None and nd["declarados"] != k:
                add("C12", "falta", f"nodo {nd['codigo']}", f"declara {nd['declarados']} paquetes y tiene {k}")
            if not NODO_MIN <= k <= NODO_MAX:
                add("C12", "falta", f"nodo {nd['codigo']}", f"{k} paquetes (el rango acordado por servicio es {NODO_MIN} a {NODO_MAX})")
        n = len(r["paquetes"])
        if r["declarados"] is not None and r["declarados"] != n:
            add("C12", "falta", f"rama {r['codigo']}", f"declara {r['declarados']} paquetes y tiene {n}")
        if n < MIN_POR_RAMA:
            add("C12", "posible", f"rama {r['codigo']}", f"solo {n} paquete(s) (mínimo {MIN_POR_RAMA})")
    total = len(paquetes)
    if not RANGO_TOTAL[0] <= total <= RANGO_TOTAL[1]:
        add("C12", "posible", "EDT", f"{total} paquetes, fuera del rango de control {RANGO_TOTAL[0]} a {RANGO_TOTAL[1]}")
    con_atributos = any(p["atributos"] for p in paquetes)
    for p in paquetes:
        if con_atributos and not p["rango"] or (con_atributos and p["rango"]):
            a = p["atributos"]
            if "etapa" not in a:
                add("C14", "falta", p["codigo"], "falta el atributo etapa")
            if "casos" not in a and a.get("ucp") != "no":
                add("C14", "falta", p["codigo"], "falta el atributo casos o ucp: no")
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
            solo_difieren_en_digitos = nombres[i][1] != nombres[j][1] and re.sub(r"\d", "#", nombres[i][1]) == re.sub(r"\d", "#", nombres[j][1])
            if solo_difieren_en_digitos:
                continue
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
