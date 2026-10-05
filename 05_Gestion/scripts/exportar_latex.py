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
BACKUPS = LATEX / "respaldo"
TEMPLATE_DIR = ROOT / "02_Propuesta" / "latex_final" / "plantilla"
TEMPLATE = TEMPLATE_DIR / "oss-pandoc.latex"
LUA_FILTER = TEMPLATE_DIR / "oss.lua"
REQUIRED_MACROS = (r"\ossCover{", r"\tableofcontents", r"\ossFinalPage")
FORBIDDEN_IN_BODY = re.compile(
    r"\\(documentclass|usepackage|RequirePackage|pagecolor|newgeometry|geometry\{|setmainfont|"
    r"AddToShipoutPicture|hypersetup)|\\(re)?newcommand\*?\{?\\oss|\\def\\oss"
)
MIN_PANDOC = (3, 1)
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


def template_preamble() -> str:
    """Preámbulo obligatorio: todo lo anterior a \\begin{document} en la plantilla fija."""
    text = TEMPLATE.read_text(encoding="utf-8")
    return text[: text.index("\\begin{document}")]


def template_version() -> str:
    first = TEMPLATE.read_text(encoding="utf-8").splitlines()[0]
    return first.removeprefix("% oss-plantilla:").strip()


def verify_tex(tex: Path) -> list[str]:
    """Devuelve los problemas que apartan un sd-NN.tex del formato corporativo (vacía si está bien)."""
    text = tex.read_text(encoding="utf-8")
    problems = []
    if text.count("\\begin{document}") != 1 or text.count("\\end{document}") != 1:
        return ["debe tener exactamente un \\begin{document} y un \\end{document}"]
    preamble, body = text.split("\\begin{document}")
    if not text.startswith(f"% oss-plantilla: {template_version()}\n"):
        problems.append(f"falta el marcador '% oss-plantilla: {template_version()}' en la línea 1")
    if preamble != template_preamble():
        problems.append("el preámbulo no coincide con plantilla/oss-pandoc.latex; no editar el preámbulo a mano")
    for macro in REQUIRED_MACROS:
        if macro not in body:
            problems.append(f"falta {macro.rstrip('{')} en el cuerpo")
    match = FORBIDDEN_IN_BODY.search(body)
    if match:
        line = text[: text.index(body) + match.start()].count("\n") + 1
        problems.append(f"línea {line}: '{match.group(0)}' no se permite en el cuerpo; el formato lo define oss.sty")
    tail = body.split("\\end{document}")[0].rstrip()
    if not tail.endswith("\\ossFinalPage"):
        problems.append("\\ossFinalPage debe ser lo último antes de \\end{document}")
    return problems


def require_valid(tex: Path) -> None:
    problems = verify_tex(tex)
    if problems:
        raise ValueError(f"{tex.name} está fuera de la plantilla corporativa:\n  - " + "\n  - ".join(problems))


def import_part(part: str, replace: bool = False) -> Path:
    output = LATEX / f"sd-{part[-2:]}.tex"
    if output.exists() and not replace:
        raise FileExistsError(
            f"{output.relative_to(ROOT)} ya existe; no se sobrescribe un LaTeX editable "
            "(usar --reemplazar solo por instrucción explícita del usuario)"
        )
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
        "pandoc", str(temp_md), "--from=markdown+raw_tex+pipe_tables-yaml_metadata_block", "--to=latex",
        "--template", str(TEMPLATE), "--lua-filter", str(LUA_FILTER),
        "--wrap=preserve", "--output", str(temp_tex),
    ]
    result = subprocess.run(command, cwd=LATEX, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(f"Pandoc falló: {result.stderr[-1600:]}")
    require_valid(temp_tex)
    if output.exists():
        BACKUPS.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        backup = BACKUPS / f"{output.stem}.{stamp}.tex"
        shutil.copy2(output, backup)
        print(f"Respaldo: {backup.relative_to(ROOT)}")
    temp_tex.replace(output)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {"partes": {}}
    manifest["partes"][part] = {
        "tex": output.name, "titulo": title, "plantilla": template_version(),
        "origen_sha256": digest.hexdigest(),
        "origen": [str(p.relative_to(ROOT)) for p in sections],
        "figuras": sorted(set(copied)), "importado_utc": datetime.now(timezone.utc).isoformat(),
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return output


def doctor() -> int:
    """Revisa herramientas requeridas; devuelve la cantidad de faltantes."""
    missing = 0

    def report(ok: bool, name: str, hint: str) -> None:
        nonlocal missing
        missing += not ok
        print(f"[{'ok' if ok else 'FALTA'}] {name}" + ("" if ok else f" -> {hint}"))

    pandoc = shutil.which("pandoc")
    version = ()
    if pandoc:
        out = subprocess.run([pandoc, "--version"], capture_output=True, text=True).stdout
        found = re.search(r"pandoc\S*\s+(\d+)\.(\d+)", out)
        version = (int(found.group(1)), int(found.group(2))) if found else ()
    report(bool(version) and version >= MIN_PANDOC, f"pandoc >= {'.'.join(map(str, MIN_PANDOC))}",
           "instalar desde https://pandoc.org/installing.html")
    report(bool(shutil.which("xelatex")), "xelatex", "instalar TeX Live o MiKTeX con XeLaTeX")
    report(bool(shutil.which("latexmk")), "latexmk", "instalar latexmk (TeX Live/MiKTeX)")
    fonts = ""
    if shutil.which("fc-list"):
        fonts = subprocess.run(["fc-list"], capture_output=True, text=True).stdout
    report("DejaVu Sans" in fonts or not shutil.which("fc-list"), "fuente DejaVu Sans", "instalar fonts-dejavu")
    try:
        import pypdf  # noqa: F401
        has_pypdf = True
    except ImportError:
        has_pypdf = False
    report(has_pypdf, "pypdf", "python3 -m pip install -r 05_Gestion/requirements.txt")
    has_svg = any(
        target.strip("<> ").lower().endswith(".svg")
        for md in (ROOT / "02_Propuesta").glob("sd-*/*.md")
        for _, target, _ in IMAGE.findall(md.read_text(encoding="utf-8-sig"))
    )
    if has_svg:
        report(bool(shutil.which("inkscape")), "inkscape (hay SVG en el repo)", "instalar Inkscape para convertir SVG a PDF")
    report(TEMPLATE.is_file() and LUA_FILTER.is_file(), "plantilla/oss-pandoc.latex y oss.lua", "restaurar desde git")
    report((ROOT / ".agents" / "skills" / "exportar" / "SKILL.md").is_file(), "skill exportar en .agents/skills (Codex, OpenCode)", "restaurar desde git")
    report((ROOT / ".claude" / "skills" / "exportar" / "SKILL.md").is_file(), "skill exportar visible para Claude Code (.claude/skills)",
           "ejecutar: python3 05_Gestion/scripts/link_skills.py")
    claude_md = ROOT / "CLAUDE.md"
    report(claude_md.is_file() and "@AGENTS.md" in claude_md.read_text(encoding="utf-8"), "CLAUDE.md importa @AGENTS.md", "agregar la línea @AGENTS.md a CLAUDE.md")
    print(f"Intérprete en uso: {sys.executable}")
    return missing


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
    require_valid(tex)
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
    imp.add_argument("--reemplazar", action="store_true",
                     help="regenera un .tex existente tras respaldarlo en respaldo/ (solo por orden explícita)")
    comp = sub.add_parser("compilar", help="compila los .tex ya editables")
    comp.add_argument("--parte", choices=PARTS)
    comp.add_argument("--todo", action="store_true")
    comp.add_argument("--final", action="store_true", help="publica en los entregables tras controles mínimos")
    comp.add_argument("--trabajadores", type=int, default=2)
    sub.add_parser("estado", help="muestra fuentes .tex disponibles y si respetan la plantilla")
    ver = sub.add_parser("verificar", help="comprueba que los .tex respeten la plantilla corporativa")
    ver.add_argument("--parte", choices=PARTS)
    sub.add_parser("doctor", help="revisa pandoc, XeLaTeX, latexmk, fuentes y dependencias Python")
    args = parser.parse_args()
    try:
        if args.accion == "estado":
            for part in PARTS:
                tex = LATEX / f"sd-{part[-2:]}.tex"
                if not tex.exists():
                    print(f"{part}: pendiente")
                else:
                    print(f"{part}: editable, {'plantilla ok' if not verify_tex(tex) else 'FUERA DE PLANTILLA (ver verificar)'}")
            return 0
        if args.accion == "doctor":
            return 1 if doctor() else 0
        if args.accion == "verificar":
            parts = [args.parte] if args.parte else PARTS
            failed = 0
            for part in parts:
                tex = LATEX / f"sd-{part[-2:]}.tex"
                if not tex.exists():
                    if args.parte:
                        raise FileNotFoundError(f"{part}: falta {tex.relative_to(ROOT)}")
                    continue
                problems = verify_tex(tex)
                failed += bool(problems)
                print(f"{part}: " + ("ok" if not problems else "FUERA DE PLANTILLA\n  - " + "\n  - ".join(problems)))
            return 1 if failed else 0
        if bool(args.parte) == bool(args.todo):
            raise ValueError("Indicar exactamente --parte T7-NN o --todo")
        if args.accion == "importar":
            requested = [args.parte] if args.parte else PARTS
            failures = []
            for part in requested:
                try:
                    print(f"Importado: {import_part(part, args.reemplazar).relative_to(ROOT)}")
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
