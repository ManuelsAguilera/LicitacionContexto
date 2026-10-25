#!/usr/bin/env python3
"""Contexto de la fuente vigente: T7-NN, sección, T-N o ADJ-NNN."""
from __future__ import annotations
import argparse
import re
from artefactos import ROOT
from contexto_fuentes import resolve, sha256, review


def render(root, artifact_id, max_words=1800):
    source = resolve(root, artifact_id)
    parts = [f"# {artifact_id} · {source.meta.get('titulo', source.path.stem)}",
             f"Fuente: {source.path.relative_to(root).as_posix()}",
             f"SHA-256: {sha256(source.path)}",
             f"Estado declarado: {source.meta.get('estado', 'sin estado declarado')}",
             f"Revisión humana: {review(source.meta)}",
             "Referencia de consistencia: SD-04 (arquitectura) y SD-07 (planificación), subordinados a las Bases y al Comunicado 10.",
             "Decisiones y pendientes activos: 80_Artefactos/contexto-activo/indice.md"]
    if source.warning: parts += [f"Aviso: {source.warning}"]
    parts += ["", "## Contenido de la fuente vigente"]
    content = source.text.strip()
    tokens = list(re.finditer(r"\S+", content))
    if len(tokens) > max_words:
        content = content[:tokens[max_words - 1].end()] + "\n[Contenido truncado por límite de palabras]"
    return "\n".join(parts + [content]) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("id", help="T7-04, T7-04-4.1, T7-04-REF, T-11 o ADJ-001")
    ap.add_argument("--max-palabras", type=int, default=1800)
    args = ap.parse_args()
    if args.max_palabras < 1: ap.error("--max-palabras debe ser positivo")
    try:
        print(render(ROOT, args.id, args.max_palabras), end="")
    except ValueError as error:
        print(error)
        return 2
    return 0


if __name__ == "__main__": raise SystemExit(main())
