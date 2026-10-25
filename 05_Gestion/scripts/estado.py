#!/usr/bin/env python3
"""Tablero de disponibilidad, estado declarado, compilación y revisión humana."""
from __future__ import annotations
import argparse
from pathlib import Path
from artefactos import ROOT
from contexto_fuentes import main_tex, master, metadata, compilation, review


def render(root):
    lines = ["# Estado de artefactos", "",
             "Disponibilidad y compilación no acreditan consistencia ni revisión humana. Referencias actuales: SD-04 y SD-07; resto por conciliar. Los maestros conservan el estado declarado.", "",
             "| Parte / artefacto | Fuente disponible | Estado declarado | Compilación disponible | Revisión humana |",
             "|---|---|---|---|---|"]
    for number in range(1, 15):
        part = f"T7-{number:02d}"
        tex = main_tex(root, part)
        m = master(root, part)
        fm = metadata(m)
        availability = (f"[LaTeX](../{tex.relative_to(root).as_posix()})" if tex.is_file() else
                        f"[Markdown; pendiente LaTeX](../{m.relative_to(root).as_posix()})" if m else "sin fuente")
        lines.append(f"| `{part}` | {availability} | {fm.get('estado', 'sin estado declarado')} | {compilation(root, part) if tex.is_file() else 'no aplica: sin LaTeX'} | {review(fm)} |")
    for p in sorted((root / "02_Propuesta/latex_final/Formularios").glob("OnlySimpleSolutions-Formulario-T-*.tex")):
        artifact = p.stem.replace("OnlySimpleSolutions-Formulario-", "")
        lines.append(f"| `{artifact}` | [LaTeX](../{p.relative_to(root).as_posix()}) | sin estado declarado | CLI del exportador sin ruta de formularios | sin revisión humana registrada |")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--salida", type=Path, default=ROOT / "05_Gestion/ESTADO.md")
    args = ap.parse_args()
    output = render(ROOT)
    if not args.dry_run: args.salida.write_text(output, encoding="utf-8")
    print(output, end="")
    return 0


if __name__ == "__main__": raise SystemExit(main())
