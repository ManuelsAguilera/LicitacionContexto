#!/usr/bin/env python3
"""Pruebas del modelo de casos de uso (puerta G3 del plan de estimación).

Solo informa. Lee las tablas de `80_Artefactos/sd-07_contexto/estimacion/03_casos_de_uso_*.md`
y aplica las pruebas P3.1, P3.4, P3.5 y P3.6 de `prompt_estimacion_ucp.md`. P3.2 y P3.3 necesitan
todos los servicios y el Anexo D: con `--completo` se exigen, y sin él se informan como pendientes.

    python3 05_Gestion/scripts/verificar_casos_uso.py [--dir RUTA] [--anexo-b RUTA] [--anexo-a RUTA]
                                                      [--actores RUTA] [--completo]

Formato esperado de cada archivo: una tabla con la cabecera
`| Código | Servicio | Caso de uso ... | Actor principal | Trans. | Origen | Supuestos ... |` y otra con
`| Código | Transacciones ... |` donde cada transacción empieza con `T1`, `T2`, etc. En la columna
Origen, los rangos se escriben `RF-127 a RF-129`.

Código de salida 0 si no hay hallazgos y 1 si los hay.
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DIR = RAIZ / "80_Artefactos" / "sd-07_contexto" / "estimacion"
ANEXO_A = RAIZ / "04_Adjuntos" / "tablas" / "sd-03_s2_anexo-a_exclusiones-supuestos-restricciones.md"
ANEXO_B = RAIZ / "04_Adjuntos" / "tablas" / "sd-03_s2_anexo-b_catalogo-requerimientos.md"
ACTORES = DIR / "02_actores_uaw.md"
MAX_TRANS = 12  # C8
# Verbos que indicarían que un caso implementa algo excluido o a cargo del cliente (Anexo A).
VERBOS_EXCLUIDOS = r"\b(instalar|adquirir|comprar|operar la cobranza judicial|gestionar remuneraciones|emitir documentos? tributarios?|reemplazar el sistema de gesti)"


def celdas(linea):
    return [c.strip() for c in linea.strip().strip("|").split("|")]


def tablas(texto):
    """Devuelve una lista de tablas Markdown como (cabecera, filas)."""
    out, actual = [], []
    for linea in texto.splitlines() + [""]:
        if linea.startswith("|"):
            actual.append(celdas(linea))
        elif actual:
            filas = [f for f in actual if not set("".join(f)) <= set(":- ")]
            if len(filas) >= 2:
                out.append((filas[0], filas[1:]))
            actual = []
    return out


def expandir(origen):
    """IDs RF citados en una celda de origen, con rangos `RF-127 a RF-129` expandidos."""
    ids = set()
    for a, b in re.findall(r"RF-(\d+)\s+a\s+RF-(\d+)", origen):
        ids.update(f"RF-{n:03d}" for n in range(int(a), int(b) + 1))
    sin_rangos = re.sub(r"RF-\d+\s+a\s+RF-\d+", "", origen)
    ids.update(f"RF-{int(n):03d}" for n in re.findall(r"RF-(\d+)", sin_rangos))
    return ids


def leer_casos(directorio):
    """Casos de uso de todos los archivos 03_casos_de_uso_*.md y sus transacciones declaradas."""
    casos, trans = [], {}
    for p in sorted(Path(directorio).glob("03_casos_de_uso_*.md")):
        for cab, filas in tablas(p.read_text(encoding="utf-8")):
            if cab[:2] == ["Código", "Servicio"] and len(cab) >= 7:
                for f in filas:
                    casos.append({"codigo": f[0], "servicio": f[1], "nombre": f[2], "actor": f[3], "trans": f[4],
                                  "origen": f[5], "archivo": p.name})
            elif cab[0] == "Código" and cab[1].startswith("Transacciones"):
                for f in filas:
                    trans[f[0]] = len(re.findall(r"\bT\d+\b", f[1]))
    return casos, trans


def catalogo_rf(ruta):
    """{ID RF: nombre del servicio} desde el Anexo B."""
    out = {}
    for cab, filas in tablas(Path(ruta).read_text(encoding="utf-8")):
        if cab[0] == "ID" and "Servicio" in cab:
            i = cab.index("Servicio")
            for f in filas:
                if f[0].startswith("RF-"):
                    out[f[0]] = f[i]
    return out


def ids_anexo_a(ruta):
    return set(re.findall(r"\|\s*((?:EXC|SP|RC|SUP)-\d+)\s*\|", Path(ruta).read_text(encoding="utf-8")))


def verificar(directorio=DIR, anexo_b=ANEXO_B, anexo_a=ANEXO_A, actores=ACTORES, completo=False):
    casos, trans = leer_casos(directorio)
    h = []
    if not casos:
        return ["P3.0 no hay casos de uso en las tablas de " + str(directorio)]
    rf_servicio = catalogo_rf(anexo_b)
    validos_a = ids_anexo_a(anexo_a)
    codigos_actor = set(re.findall(r"\|\s*(A[HS]-\d+)\s*\|", Path(actores).read_text(encoding="utf-8")))

    # P3.1 cada RF de un servicio presente está en un caso y cada caso cita una fuente válida
    por_rf = defaultdict(list)
    for c in casos:
        c["rf"] = expandir(c["origen"])
        for r in c["rf"]:
            por_rf[r].append(c["codigo"])
        citas = c["rf"] | set(re.findall(r"\b(?:EXC|SP|RC|OP)-\d+\b", c["origen"])) | set(re.findall(r"\b3\.[34]\.\d+\b", c["origen"]))
        if not citas:
            h.append(f"P3.1 {c['codigo']} no cita un RF, una exclusión, una obligación ni un recorrido")
        for r in c["rf"]:
            if r not in rf_servicio:
                h.append(f"P3.1 {c['codigo']} cita {r}, que no está en el Anexo B")
        for x in re.findall(r"\b(?:EXC|SP|RC)-\d+\b", c["origen"]):
            if x not in validos_a:
                h.append(f"P3.1 {c['codigo']} cita {x}, que no está en el Anexo A")
    servicios = {rf_servicio[r] for c in casos for r in c["rf"] if r in rf_servicio}
    for r, s in sorted(rf_servicio.items()):
        if s in servicios and r not in por_rf:
            h.append(f"P3.1 {r} ({s}) no está en ningún caso de uso")

    # P3.2 y P3.3 necesitan todos los servicios y el Anexo D
    todos = set(rf_servicio.values())
    faltan = sorted(todos - servicios)
    if faltan and completo:
        h.append("P3.2 servicios sin casos de uso: " + ", ".join(faltan))
    # P3.7 actores de la lista sin ningún caso (solo con --completo; antes se informan como pendientes)
    if completo:
        h += [f"P3.7 el actor {a} no es actor principal de ningún caso" for a in actores_sin_caso(casos, codigos_actor)]
    # P3.4 nada excluido como trabajo propio
    for c in casos:
        if re.search(VERBOS_EXCLUIDOS, c["nombre"], re.I):
            h.append(f"P3.4 {c['codigo']} parece implementar algo excluido o a cargo del cliente: «{c['nombre']}»")
    # P3.5 granularidad
    for c in casos:
        try:
            n = int(c["trans"])
        except ValueError:
            h.append(f"P3.5 {c['codigo']} tiene un número de transacciones no válido: «{c['trans']}»")
            continue
        if n < 1 or n > MAX_TRANS:
            h.append(f"P3.5 {c['codigo']} tiene {n} transacciones (máximo {MAX_TRANS})")
        if c["codigo"] not in trans:
            h.append(f"P3.5 {c['codigo']} no detalla sus transacciones")
        elif trans[c["codigo"]] != n:
            h.append(f"P3.5 {c['codigo']} declara {n} transacciones y detalla {trans[c['codigo']]}")
        if c["actor"] not in codigos_actor:
            h.append(f"P3.5 {c['codigo']} usa el actor {c['actor']}, que no está en la lista de actores")
    ns = [int(c["trans"]) for c in casos if c["trans"].isdigit()]
    if ns:
        if sum(1 for n in ns if n == 1) / len(ns) > 0.3:
            h.append("P3.5 más del 30 % de los casos tiene una sola transacción (posible conteo de pantallas)")
        if all(n >= 8 for n in ns):
            h.append("P3.5 todos los casos son complejos (posible doble conteo de alternativos)")
    # P3.6 RF en dos casos
    for r, cs in sorted(por_rf.items()):
        if len(cs) > 1:
            h.append(f"P3.6 {r} está en {len(cs)} casos ({', '.join(cs)}) y debe declararse")
    return h


def actores_sin_caso(casos, codigos_actor):
    return sorted(codigos_actor - {c["actor"] for c in casos})


def pendientes(directorio=DIR, anexo_b=ANEXO_B, actores=ACTORES):
    casos, _ = leer_casos(directorio)
    rf_servicio = catalogo_rf(anexo_b)
    hechos = {rf_servicio[r] for c in casos for r in expandir(c["origen"]) if r in rf_servicio}
    out = ["P3.2 servicios aún sin casos de uso: " + ", ".join(sorted(set(rf_servicio.values()) - hechos))]
    sin = actores_sin_caso(casos, set(re.findall(r"\|\s*(A[HS]-\d+)\s*\|", Path(actores).read_text(encoding="utf-8"))))
    out.append("P3.7 actores aún sin caso como actor principal: " + (", ".join(sin) or "ninguno"))
    out.append("P3.3 los 28 resultados del Anexo D se rastrean al terminar todos los servicios")
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", default=str(DIR))
    ap.add_argument("--anexo-b", default=str(ANEXO_B))
    ap.add_argument("--anexo-a", default=str(ANEXO_A))
    ap.add_argument("--actores", default=str(ACTORES))
    ap.add_argument("--completo", action="store_true", help="exige P3.2 sobre todos los servicios")
    a = ap.parse_args(argv)
    hallazgos = verificar(a.dir, a.anexo_b, a.anexo_a, a.actores, a.completo)
    for h in hallazgos:
        print(h)
    if not a.completo:
        for p in pendientes(a.dir, a.anexo_b, a.actores):
            print("(pendiente) " + p)
    print(f"{len(hallazgos)} hallazgo(s)")
    return 1 if hallazgos else 0


if __name__ == "__main__":
    sys.exit(main())
