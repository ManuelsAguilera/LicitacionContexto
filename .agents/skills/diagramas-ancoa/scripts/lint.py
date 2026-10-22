#!/usr/bin/env python3
"""Revisa archivos de diagrama escritos o editados a mano y rechaza lo que salga del catálogo.

Uso:  python3 scripts/lint.py archivo [archivo ...]
Admite: .json (especificación → delega en validar.py), .py (código de la biblioteca diagrams),
        .drawio (XML de draw.io), .md/.tex/.html (busca bloques de diagrama prohibidos).
Rechaza siempre: .mmd, .mermaid, .puml, .plantuml, .dot, .gv, .excalidraw.
"""
import pathlib
import re
import sys

from _comun import CATALOGO, cargar_spec
from validar import validar

EXT_PROHIBIDAS = {".mmd", ".mermaid", ".puml", ".plantuml", ".pu", ".dot", ".gv", ".excalidraw", ".d2"}
MODULOS_PERMITIDOS = {v["icono"].rsplit(".", 1)[0] for v in CATALOGO["tipos_nodo_logicos"].values()
                      if v.get("icono", "").startswith("diagrams.")}
MODULOS_PERMITIDOS |= {"diagrams", "diagrams.custom"}
CLASES_PERMITIDAS = {v["icono"].rsplit(".", 1)[1] for v in CATALOGO["tipos_nodo_logicos"].values()
                     if v.get("icono", "").startswith("diagrams.")} | {"Diagram", "Cluster", "Edge", "Node", "Custom"}
COLORES = ({s["color"].upper() for s in CATALOGO["semanticas_enlace"].values()}
           | {v.upper() for f in CATALOGO["frentes"].values() for v in f.values() if str(v).startswith("#")}
           | {v.upper() for e in CATALOGO["estados_nodo"].values() for v in (e["borde"], e["relleno"]) if v}
           | {v.upper() for g in CATALOGO["grupos_fisicos"].values() for v in (g["relleno"], g["borde"]) if v.startswith("#")}
           | {CATALOGO["insignia"]["relleno"].upper(), CATALOGO["insignia"]["texto"].upper(),
              "#FFFFFF", "#000000", "#333333", "#1A1A1A", "#4A4A4A", "#7A4A00", "#B0B0B0"})
IMAGENES_DRAWIO = {v.split("image=")[1].split(";")[0] for v in CATALOGO["iconos_fisicos"].values()}


def lint_py(txt):
    err = []
    for m in re.finditer(r"^\s*from\s+(diagrams[\w.]*)\s+import\s+([\w, ()\n]+)", txt, re.M):
        mod = m.group(1)
        if mod not in MODULOS_PERMITIDOS:
            err.append(f"módulo de íconos no permitido: «{mod}» (solo Azure y genéricos del catálogo)")
        for cls in re.findall(r"\w+", m.group(2)):
            if cls not in CLASES_PERMITIDAS:
                err.append(f"clase no permitida: «{cls}» de «{mod}»")
    if re.search(r"^\s*import\s+diagrams\.", txt, re.M):
        err.append("use «from diagrams.x import Clase», no «import diagrams.x» (el linter no puede verificarlo)")
    for prov in CATALOGO["prohibido"]["proveedores_iconos"]:
        if re.search(rf"diagrams\.{prov}\b", txt):
            err.append(f"proveedor de íconos prohibido: «{prov}»")
    for c in set(re.findall(r"#[0-9A-Fa-f]{6}\b", txt)):
        if c.upper() not in COLORES:
            err.append(f"color fuera de la paleta del catálogo: {c}")
    for nombre in re.findall(r"color\s*=\s*[\"']([a-zA-Z]+)[\"']", txt):
        err.append(f"color con nombre libre «{nombre}»: use los hex del catálogo")
    err.append("AVISO: el código escrito a mano no pasa por las reglas de dominio (línea roja, códigos, leyenda). "
               "Prefiera una especificación JSON + render_logico.py.")
    return err


def lint_drawio(txt):
    err = []
    admitidas_embebidas = set()
    if 'image=data:image/png,' in txt:
        from render_capas_referencia import icono_data
        for tipo,definicion in CATALOGO['tipos_nodo_logicos'].items():
            if definicion.get('icono'):
                admitidas_embebidas.add(icono_data(tipo).replace(';base64,',','))
    for img in set(re.findall(r"image=([^;\"&]+)", txt)):
        if img not in IMAGENES_DRAWIO and img not in admitidas_embebidas:
            err.append(f"ícono no permitido en draw.io: {img}")
    for sh in set(re.findall(r"shape=(mxgraph\.[\w.]+)", txt)):
        if not sh.startswith("mxgraph.azure"):
            err.append(f"forma de draw.io no permitida: {sh} (use los íconos del catálogo)")
        else:
            err.append(f"forma heredada «{sh}»: use la biblioteca img/lib/azure2 del catálogo")
    for c in set(re.findall(r"(?:fill|stroke|font)Color=(#[0-9A-Fa-f]{6})", txt)):
        if c.upper() not in COLORES:
            err.append(f"color fuera de la paleta del catálogo: {c}")
    if "Leyenda" not in txt:
        err.append("falta la leyenda dentro de la figura (C4: toda notación se explica)")
    return err


def lint_texto(txt):
    err = []
    if re.search(r"```\s*(mermaid|plantuml|puml|dot|graphviz|d2)", txt, re.I):
        err.append("bloque de diagrama prohibido (Mermaid/PlantUML/DOT/D2). Use un estilo del catálogo.")
    if re.search(r"@startuml|graph\s+(TD|LR|TB)\b|flowchart\s+(TD|LR|TB)|sequenceDiagram|classDiagram|erDiagram|gantt", txt):
        err.append("sintaxis de Mermaid/PlantUML detectada: formato prohibido")
    return err


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    total = 0
    for ruta in sys.argv[1:]:
        p = pathlib.Path(ruta)
        ext = p.suffix.lower()
        if ext in EXT_PROHIBIDAS:
            problemas = [f"formato prohibido ({ext}). Solo se admiten los estilos L1–L6 (diagrams) y F1–F5 (draw.io)."]
        elif ext == ".json":
            e, a = validar(cargar_spec(p))
            problemas = e + ["AVISO: " + x for x in a]
        else:
            txt = p.read_text(encoding="utf-8", errors="replace")
            problemas = (lint_py(txt) if ext == ".py" else lint_drawio(txt) if ext == ".drawio" else lint_texto(txt))
        duros = [x for x in problemas if not x.startswith("AVISO")]
        total += len(duros)
        estado = "✗" if duros else "✓"
        print(f"{estado} {ruta}")
        for x in problemas:
            print("    " + x)
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
