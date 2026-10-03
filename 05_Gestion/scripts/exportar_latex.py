#!/usr/bin/env python3
"""Importa Markdown una vez a LaTeX editable y compila PDF por parte o en lote."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from artefactos import ROOT, parse_frontmatter

LATEX = ROOT / "02_Propuesta" / "latex_final"
FIGURES = LATEX / "figuras"
MANIFEST = LATEX / "manifiesto.json"
BUILD = LATEX / "build"
PREVIEWS = ROOT / "05_Gestion" / "reportes" / "vistas_previas"
OFFICIAL = ROOT / "07_Entregables" / "sobre_2_tecnico"
CONSOLIDATED = ROOT / "07_Entregables" / "pdf_final"
PARTS = [f"T7-{n:02d}" for n in range(1, 15)]
SECTION_ROW = re.compile(r"\|\s*(\d+)\s*\|\s*([^|]+)\|\s*`?(sd-\d+_s\d+_[^`|]+\.md)`?\s*\|")
IMAGE = re.compile(r"(!\[[^\]]*\]\()([^)]*)(\))")


def source_for(part: str) -> tuple[str, list[Path]]:
    number = part.removeprefix("T7-")
    folders = list((ROOT / "02_Propuesta").glob(f"sd-{number}_*"))
    if len(folders) != 1:
        raise ValueError(f"{part}: se esperaba una carpeta; encontradas {len(folders)}")
    folder = folders[0]
    canonical_master = folder / f"{folder.name}.md"
    masters = [canonical_master] if canonical_master.is_file() else [
        p for p in folder.glob(f"sd-{number}_*.md") if not re.search(r"_s\d+_", p.name)
    ]
    if len(masters) != 1:
        raise ValueError(f"{part}: maestro ambiguo o ausente")
    front, body = parse_frontmatter(masters[0].read_text(encoding="utf-8-sig"))
    title = str(front.get("titulo") or f"Subdocumento {int(number)}")
    sections = []
    for line in body.splitlines():
        match = SECTION_ROW.match(line)
        if match:
            path = folder / match.group(3).strip("`")
            if not path.is_file():
                raise ValueError(f"{part}: falta {path.relative_to(ROOT)}")
            sections.append((int(match.group(1)), path))
    if not sections:
        raise ValueError(f"{part}: el maestro no declara secciones materializadas")
    sections.sort(key=lambda item: item[0])
    if len({n for n, _ in sections}) != len(sections):
        raise ValueError(f"{part}: números de sección duplicados")
    return title, [path for _, path in sections]


def latex_escape(value: str) -> str:
    return "".join({"&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}"}.get(ch, ch) for ch in value)


def figure_path(raw: str, section: Path, copied: list[str]) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if re.match(r"^[a-z]+://", target, re.I):
        raise ValueError(f"Imagen remota no admitida en {section.name}: {target}")
    source = (section.parent / target).resolve()
    if not source.is_file():
        raise ValueError(f"Imagen ausente: {source}")
    suffix = source.suffix.lower()
    if suffix not in {".pdf", ".png", ".jpg", ".jpeg", ".svg"}:
        raise ValueError(f"Imagen no admitida: {source}")
    digest = hashlib.sha256(source.read_bytes()).hexdigest()[:10]
    name = f"{source.stem}-{digest}{'.pdf' if suffix == '.svg' else suffix}"
    FIGURES.mkdir(parents=True, exist_ok=True)
    dest = FIGURES / name
    if not dest.exists():
        if suffix == ".svg":
            inkscape = shutil.which("inkscape")
            if not inkscape:
                raise RuntimeError(f"Se requiere Inkscape para convertir SVG: {source}")
            subprocess.run([inkscape, str(source), "--export-type=pdf", f"--export-filename={dest}"], check=True, capture_output=True, text=True)
        else:
            shutil.copy2(source, dest)
    copied.append(str(dest.relative_to(LATEX)))
    return f"figuras/{name}"


def import_part(part: str) -> Path:
    output = LATEX / f"sd-{part[-2:]}.tex"
    if output.exists():
        raise FileExistsError(f"{output.relative_to(ROOT)} ya existe; no se sobrescribe un LaTeX editable")
    title, sections = source_for(part)
    copied: list[str] = []
    bodies = []
    digest = hashlib.sha256()
    for section in sections:
        raw = section.read_text(encoding="utf-8-sig")
        digest.update(section.as_posix().encode() + raw.encode())
        _, body = parse_frontmatter(raw)
        if re.search(r"```\s*mermaid", body, re.I):
            raise ValueError(f"{section.relative_to(ROOT)}: bloque Mermaid obsoleto; incrustar imagen")
        body = IMAGE.sub(lambda match: match.group(1) + figure_path(match.group(2), section, copied) + match.group(3), body)
        bodies.append(body.strip())
    cover = "\n".join([
        r"\ossCover{" + latex_escape(title) + r"}{Subdocumento " + str(int(part[-2:])) + r"}",
        r"\tableofcontents", r"\clearpage", "",
    ])
    source = cover + "\n\n".join(bodies) + "\n\n\\ossFinalPage\n"
    LATEX.mkdir(parents=True, exist_ok=True)
    temp_md = BUILD / f"{part}.import.md"
    BUILD.mkdir(parents=True, exist_ok=True)
    temp_md.write_text(source, encoding="utf-8")
    temp_tex = BUILD / f"{part}.import.tex"
    command = [
        "pandoc", str(temp_md), "--from=markdown+raw_tex+pipe_tables", "--to=latex",
        "--standalone", "--include-in-header", str(LATEX / "oss-header.tex"),
        "--metadata=lang:es-CL", "--variable=geometry:letterpaper,margin=20mm",
        "--variable=fontsize:11pt", "--variable=mainfont:DejaVu Sans",
        "--output", str(temp_tex),
    ]
    result = subprocess.run(command, cwd=LATEX, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(f"Pandoc falló: {result.stderr[-1600:]}")
    temp_tex.replace(output)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {"partes": {}}
    manifest["partes"][part] = {
        "tex": output.name, "titulo": title, "origen_sha256": digest.hexdigest(),
        "origen": [str(p.relative_to(ROOT)) for p in sections],
        "figuras": sorted(set(copied)), "importado_utc": datetime.now(timezone.utc).isoformat(),
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return output


def check_final(tex: Path) -> None:
    body = tex.read_text(encoding="utf-8")
    required = ("Referencias", "Declaración de uso de IA")
    for heading in required:
        if heading not in body:
            raise ValueError(f"{tex.name}: falta {heading} para la exportación final")
    if re.search(r"\bTODO\b|\[VERIFICAR\]", body, re.I):
        raise ValueError(f"{tex.name}: contiene un marcador pendiente")


def compile_part(part: str, final: bool) -> tuple[str, Path, float, int]:
    tex = LATEX / f"sd-{part[-2:]}.tex"
    if not tex.is_file():
        raise FileNotFoundError(f"{part}: falta {tex.relative_to(ROOT)}; importar primero")
    if final:
        check_final(tex)
    start = time.perf_counter()
    outdir = BUILD / part
    outdir.mkdir(parents=True, exist_ok=True)
    command = ["latexmk", "-xelatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", f"-outdir={outdir}", tex.name]
    result = subprocess.run(command, cwd=LATEX, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(f"{part}: LaTeX falló; registro {outdir / tex.with_suffix('.log').name}\n{(result.stdout + result.stderr)[-1800:]}")
    pdf = outdir / tex.with_suffix(".pdf").name
    from pypdf import PdfReader
    reader = PdfReader(str(pdf))
    if not reader.pages or not "".join(page.extract_text() or "" for page in reader.pages).strip():
        raise RuntimeError(f"{part}: PDF vacío o sin texto seleccionable")
    for page in reader.pages:
        width, height = float(page.mediabox.width), float(page.mediabox.height)
        if abs(width - 612) > 2 or abs(height - 792) > 2:
            raise RuntimeError(f"{part}: tamaño distinto de carta ({width:.1f} × {height:.1f} pt)")
    dest = (OFFICIAL if final else PREVIEWS) / (f"OnlySimpleSolutions-Subdocumento{int(part[-2:])}.pdf" if final else f"{part}_latex_preview.pdf")
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(pdf, dest)
    return part, dest, time.perf_counter() - start, len(reader.pages)


def compile_all(final: bool, workers: int) -> None:
    missing = [part for part in PARTS if not (LATEX / f"sd-{part[-2:]}.tex").is_file()]
    available = [part for part in PARTS if part not in missing]
    if missing and final:
        raise FileNotFoundError("Fuentes LaTeX pendientes: " + ", ".join(missing))
    if not available:
        raise FileNotFoundError("No hay fuentes LaTeX disponibles para compilar")
    started = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        results = list(pool.map(lambda part: compile_part(part, final), available))
    from pypdf import PdfWriter
    from pypdf import PdfReader
    writer = PdfWriter()
    page_offset = 0
    for part, pdf, _, pages in results:
        reader = PdfReader(str(pdf))
        for page in reader.pages:
            writer.add_page(page)
        writer.add_outline_item(f"Subdocumento {int(part[-2:])}", page_offset)
        page_offset += pages
    consolidated = (CONSOLIDATED if final else PREVIEWS) / ("OnlySimpleSolutions-PropuestaTecnica.pdf" if final else "OnlySimpleSolutions-PropuestaTecnica-preview.pdf")
    consolidated.parent.mkdir(parents=True, exist_ok=True)
    with consolidated.open("wb") as stream:
        writer.write(stream)
    total = time.perf_counter() - started
    report = {"final": final, "segundos": round(total, 2), "objetivo_menor_60_min": total < 3600,
              "partes": [{"id": part, "pdf": str(pdf.relative_to(ROOT)), "segundos": round(seconds, 2), "paginas": pages} for part, pdf, seconds, pages in results],
              "consolidado": str(consolidated.relative_to(ROOT))}
    BUILD.mkdir(parents=True, exist_ok=True)
    (BUILD / "ultimo-reporte.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    estado = "sí" if total < 3600 else "no"
    print(f"{len(results)} PDF disponibles y consolidado: {total:.1f} s; objetivo < 60 min: {estado}")
    if missing:
        print("Fuentes pendientes: " + ", ".join(missing))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="accion", required=True)
    imp = sub.add_parser("importar", help="convierte una vez sin sobrescribir el .tex")
    imp.add_argument("--parte", choices=PARTS)
    imp.add_argument("--todo", action="store_true")
    comp = sub.add_parser("compilar", help="compila los .tex ya editables")
    comp.add_argument("--parte", choices=PARTS)
    comp.add_argument("--todo", action="store_true")
    comp.add_argument("--final", action="store_true", help="publica en los entregables tras controles mínimos")
    comp.add_argument("--trabajadores", type=int, default=2)
    sub.add_parser("estado", help="muestra fuentes .tex disponibles")
    args = parser.parse_args()
    try:
        if args.accion == "estado":
            for part in PARTS:
                print(f"{part}: {'editable' if (LATEX / f'sd-{part[-2:]}.tex').exists() else 'pendiente'}")
            return 0
        if bool(args.parte) == bool(args.todo):
            raise ValueError("Indicar exactamente --parte T7-NN o --todo")
        if args.accion == "importar":
            requested = [args.parte] if args.parte else PARTS
            failures = []
            for part in requested:
                try:
                    print(f"Importado: {import_part(part).relative_to(ROOT)}")
                except (FileNotFoundError, ValueError) as exc:
                    if args.parte:
                        raise
                    failures.append(f"{part}: {exc}")
            if failures:
                print("Partes no importadas:")
                print("\n".join(failures))
        elif args.todo:
            if args.trabajadores < 1:
                raise ValueError("--trabajadores debe ser positivo")
            compile_all(args.final, args.trabajadores)
        else:
            part, dest, seconds, pages = compile_part(args.parte, args.final)
            print(f"{part}: {dest.relative_to(ROOT)} ({pages} páginas, {seconds:.1f} s)")
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
