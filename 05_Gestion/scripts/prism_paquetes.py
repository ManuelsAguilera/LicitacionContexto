#!/usr/bin/env python3
"""Paquetes por subdocumento para edición colaborativa en Prism.

latex_final/ sigue siendo la fuente de verdad. Aquí se generan zips autocontenidos
(sd-NN.zip) para subir a Prism y se reimportan los cambios validándolos con la plantilla.
Se usa desde exportar_latex.py (prism-prueba, prism-empaquetar, prism-importar).
"""

from __future__ import annotations

import difflib
import hashlib
import json
import posixpath
import re
import shutil
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import exportar_latex as ex

FIGURE_REF = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")
RESOURCE_REF = re.compile(r"\{(recursos/[^}]+)\}")
FIXED_DATE = (2026, 1, 1, 0, 0, 0)
ALLOWED_SUFFIXES = {".tex", ".sty", ".pdf", ".png", ".jpg", ".jpeg", ".txt"}
IMAGE_SUFFIXES = {".pdf", ".png", ".jpg", ".jpeg"}
MAX_FILES = 500
MAX_BYTES = 100 * 1024 * 1024

README_PRISM = """Paquete de edición colaborativa para Prism: {title} (Subdocumento {number}).

Cómo usarlo
1. En Prism, crear un proyecto nuevo importando este zip. El archivo principal es {name}.tex.
2. Compilar y editar. Todo el equipo puede editar el cuerpo del documento.

Qué NO tocar
- El preámbulo de {name}.tex (todo lo anterior a \\begin{{document}}).
- oss.sty y la carpeta recursos/: los mantiene quien administra la plantilla.
- \\ossCover, \\tableofcontents y \\ossFinalPage deben seguir en el cuerpo.
- No agregar \\usepackage, \\documentclass, \\pagecolor ni \\newgeometry.

Figuras nuevas: subirlas a la carpeta figuras/ (PDF, PNG o JPEG) y enlazarlas con
\\includegraphics{{figuras/archivo.png}}.

Cómo devolver los cambios al repositorio
1. En Prism, descargar el proyecto como zip.
2. La persona responsable del subdocumento ejecuta, desde la raíz del repositorio:
   python3 05_Gestion/scripts/exportar_latex.py prism-importar --parte T7-{number:02d} --zip <archivo.zip> --dry-run
   y, si el resumen es correcto, el mismo comando sin --dry-run.
3. Compilar el PDF oficial con: python3 05_Gestion/scripts/exportar_latex.py compilar --parte T7-{number:02d}
La vista previa de Prism puede diferir en tipografía del PDF oficial.
"""


def out_dir() -> Path:
    return ex.ROOT / "05_Gestion" / "build" / "prism"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def referenced_figures(tex_text: str) -> list[str]:
    names = sorted({m.group(1).strip() for m in FIGURE_REF.finditer(tex_text) if m.group(1).startswith("figuras/")})
    return names


def referenced_resources() -> list[str]:
    sty = (ex.LATEX / "oss.sty").read_text(encoding="utf-8")
    return sorted(set(RESOURCE_REF.findall(sty)))


def write_zip(path: Path, files: dict[str, bytes]) -> None:
    """Zip determinista: orden alfabético, fecha fija, permisos fijos."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        for name in sorted(files):
            info = zipfile.ZipInfo(name, FIXED_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, files[name])


def collect_files(part: str) -> tuple[dict[str, bytes], str]:
    number = part[-2:]
    tex = ex.LATEX / f"sd-{number}.tex"
    if not tex.is_file():
        raise FileNotFoundError(f"{part}: falta {tex.relative_to(ex.ROOT)}; importar primero")
    ex.require_valid(tex)
    text = tex.read_text(encoding="utf-8")
    files: dict[str, bytes] = {f"sd-{number}.tex": text.encode("utf-8"), "oss.sty": (ex.LATEX / "oss.sty").read_bytes()}
    for rel in referenced_resources():
        source = ex.LATEX / rel
        if not source.is_file():
            raise FileNotFoundError(f"oss.sty referencia {rel}, que no existe")
        files[rel] = source.read_bytes()
    for rel in referenced_figures(text):
        source = ex.LATEX / rel
        if not source.is_file():
            raise FileNotFoundError(f"{tex.name} referencia {rel}, que no existe")
        files[rel] = source.read_bytes()
    manifest_title = ""
    if ex.MANIFEST.exists():
        manifest_title = json.loads(ex.MANIFEST.read_text(encoding="utf-8")).get("partes", {}).get(part, {}).get("titulo", "")
    files["LEEME-PRISM.txt"] = README_PRISM.format(title=manifest_title or f"Subdocumento {int(number)}", number=int(number), name=f"sd-{number}").encode("utf-8")
    return files, sha256(files[f"sd-{number}.tex"])


def update_manifest(part: str, **values: str) -> None:
    manifest = json.loads(ex.MANIFEST.read_text(encoding="utf-8")) if ex.MANIFEST.exists() else {"partes": {}}
    entry = manifest["partes"].setdefault(part, {"tex": f"sd-{part[-2:]}.tex"})
    entry.setdefault("prism", {}).update(values)
    ex.MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def package_part(part: str) -> Path:
    files, digest = collect_files(part)
    destination = out_dir() / f"sd-{part[-2:]}.zip"
    write_zip(destination, files)
    update_manifest(part, empaquetado_sha256=digest, empaquetado_utc=datetime.now(timezone.utc).isoformat())
    return destination


def package_probe(part: str = "T7-03") -> list[Path]:
    """Dos zips de prueba del motor de Prism, con la misma estructura plana de un paquete real.

    A: la plantilla real (XeLaTeX + fontspec). B: variante mínima que usa oss.sty con pdfLaTeX.
    """
    files, _ = collect_files(part)
    number = part[-2:]
    shared = {n: d for n, d in files.items() if n == "oss.sty" or n.startswith(("recursos/", "figuras/"))}
    figure = next((n for n in files if n.startswith("figuras/")), None)
    image = f"\\includegraphics[width=0.4\\linewidth]{{{figure}}}" if figure else "Sin figura"
    main_b = (
        "\\documentclass[11pt]{article}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n"
        "\\usepackage[letterpaper,margin=20mm]{geometry}\n\\usepackage[spanish]{babel}\n"
        "\\usepackage{longtable,booktabs,array}\n\\usepackage{oss}\n\\begin{document}\n"
        "\\ossCover{Prueba de motor}{Subdocumento 0}\n\\tableofcontents\n\\clearpage\n"
        "\\section{Tildes y eñes}\nÑandú, canción, año, 100\\% de cobertura.\n\n"
        "\\begin{longtable}{@{}ll@{}}\n\\toprule\nCódigo & Descripción\\\\\n\\midrule\nR-01 & Primera fila\\\\\n\\bottomrule\n\\end{longtable}\n\n"
        f"{image}\n\n\\ossFinalPage\n\\end{{document}}\n"
    )
    questions = (
        "\nAnotar:\n"
        " 1. ¿Compila? Si falla, copiar la primera línea del error del registro (log).\n"
        " 2. ¿Qué motor indica el registro (pdfTeX, XeTeX, LuaTeX)? ¿Hay selector de motor o de archivo principal?\n"
        " 3. ¿Se ven la portada con foto, la marca de agua, el pie con logo y la tabla?\n"
        " 4. ¿Aceptó el zip con subcarpetas recursos/ y figuras/?\n"
        " 5. ¿Se puede descargar el proyecto como zip? ¿Con qué estructura de carpetas?\n"
    )
    variants = {
        "prueba-A-xelatex.zip": {
            **shared, f"sd-{number}.tex": files[f"sd-{number}.tex"],
            "LEEME.txt": (f"Prueba A: plantilla real. Archivo principal: sd-{number}.tex (XeLaTeX + fontspec, DejaVu Sans).\n" + questions).encode("utf-8"),
        },
        "prueba-B-pdflatex.zip": {
            **shared, "main.tex": main_b.encode("utf-8"),
            "LEEME.txt": ("Prueba B: main.tex mínimo con T1/utf8; comprueba si oss.sty (portada TikZ, marca de agua) sirve con pdfLaTeX.\n" + questions).encode("utf-8"),
        },
    }
    paths = []
    for name, content in variants.items():
        write_zip(out_dir() / name, content)
        paths.append(out_dir() / name)
    return paths


def normalize_names(names: list[str]) -> dict[str, str]:
    """Devuelve {nombre original: nombre normalizado}; valida rutas y quita una carpeta raíz común."""
    entries = [n for n in names if not n.endswith("/")]
    if len(entries) > MAX_FILES:
        raise ValueError(f"El zip tiene {len(entries)} archivos (máximo {MAX_FILES})")
    cleaned = {}
    for name in entries:
        if name.startswith(("/", "\\")) or "\\" in name or re.match(r"^[A-Za-z]:", name):
            raise ValueError(f"Ruta no admitida en el zip: {name}")
        norm = posixpath.normpath(name)
        if norm.startswith("..") or "/../" in f"/{norm}/" or norm == ".":
            raise ValueError(f"Ruta no admitida en el zip: {name}")
        cleaned[name] = norm
    roots = {n.split("/")[0] for n in cleaned.values() if "/" in n}
    at_root = any("/" not in n for n in cleaned.values())
    if len(roots) == 1 and not at_root:
        root = roots.pop()
        cleaned = {k: v[len(root) + 1:] for k, v in cleaned.items()}
    return cleaned


def import_part(part: str, zip_path: Path, dry_run: bool = False, force: bool = False) -> list[str]:
    number = part[-2:]
    repo_tex = ex.LATEX / f"sd-{number}.tex"
    if not repo_tex.is_file():
        raise FileNotFoundError(f"{part}: falta {repo_tex.relative_to(ex.ROOT)}")
    messages: list[str] = []
    with zipfile.ZipFile(zip_path) as archive:
        mapping = normalize_names([i.filename for i in archive.infolist()])
        total = sum(i.file_size for i in archive.infolist() if not i.is_dir())
        if total > MAX_BYTES:
            raise ValueError(f"El zip descomprimido pesa {total // (1024 * 1024)} MB (máximo {MAX_BYTES // (1024 * 1024)} MB)")
        for original, norm in mapping.items():
            if Path(norm).suffix.lower() not in ALLOWED_SUFFIXES:
                raise ValueError(f"Tipo de archivo no admitido en el zip: {norm}")
        by_name = {norm: original for original, norm in mapping.items()}
        main = next((n for n in (f"sd-{number}.tex", "main.tex") if n in by_name), None)
        if main is None:
            raise ValueError(f"El zip no contiene sd-{number}.tex ni main.tex en su raíz")
        received = archive.read(by_name[main]).decode("utf-8").replace("\r\n", "\n")
        extra = {n: archive.read(o) for n, o in by_name.items() if n != main}

    with tempfile.TemporaryDirectory() as tmp:
        candidate = Path(tmp) / f"sd-{number}.tex"
        candidate.write_text(received, encoding="utf-8")
        problems = ex.verify_tex(candidate)
    if problems:
        raise ValueError(f"{main} del zip está fuera de la plantilla corporativa:\n  - " + "\n  - ".join(problems))

    current = repo_tex.read_text(encoding="utf-8")
    manifest = json.loads(ex.MANIFEST.read_text(encoding="utf-8")) if ex.MANIFEST.exists() else {"partes": {}}
    packaged = manifest.get("partes", {}).get(part, {}).get("prism", {}).get("empaquetado_sha256")
    if not force:
        if packaged is None:
            raise ValueError(f"{part}: no hay registro de empaquetado; usar prism-empaquetar antes o --forzar")
        if sha256(current.encode("utf-8")) != packaged:
            raise ValueError(
                f"{repo_tex.name} cambió en el repositorio desde que se empaquetó para Prism; "
                "revisar los cambios y repetir el empaquetado, o usar --forzar para reemplazarlo"
            )

    for name, data in sorted(extra.items()):
        if name == "oss.sty" or name.startswith("recursos/"):
            reference = ex.LATEX / name
            if not reference.is_file() or reference.read_bytes() != data:
                messages.append(f"Aviso: {name} del zip difiere del repositorio; se ignora (solo cambia quien mantiene la plantilla)")
    new_figures = []
    for name, data in sorted(extra.items()):
        if not name.startswith("figuras/"):
            continue
        if Path(name).suffix.lower() not in IMAGE_SUFFIXES:
            raise ValueError(f"Figura no admitida: {name}")
        dest = ex.LATEX / name
        if dest.exists():
            if dest.read_bytes() != data:
                messages.append(f"Aviso: {name} ya existe con otro contenido; no se sobrescribe (usar otro nombre)")
        else:
            new_figures.append((dest, data))
    for rel in referenced_figures(received):
        if not (ex.LATEX / rel).is_file() and rel not in extra:
            messages.append(f"Aviso: {main} referencia {rel}, que no está en el zip ni en el repositorio")

    if received == current:
        messages.append(f"{repo_tex.name}: sin cambios")
    else:
        diff = list(difflib.unified_diff(current.splitlines(), received.splitlines(), lineterm="", n=0))
        added = sum(1 for line in diff if line.startswith("+") and not line.startswith("+++"))
        removed = sum(1 for line in diff if line.startswith("-") and not line.startswith("---"))
        messages.append(f"{repo_tex.name}: +{added} -{removed} líneas")
    for dest, _ in new_figures:
        messages.append(f"Figura nueva: {dest.relative_to(ex.ROOT)}")
    if dry_run:
        messages.append("--dry-run: no se escribió nada")
        return messages

    if received != current:
        ex.BACKUPS.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        backup = ex.BACKUPS / f"sd-{number}.{stamp}.tex"
        shutil.copy2(repo_tex, backup)
        messages.append(f"Respaldo: {backup.relative_to(ex.ROOT)}")
        repo_tex.write_bytes(received.encode("utf-8"))
    for dest, data in new_figures:
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    update_manifest(part, empaquetado_sha256=sha256(received.encode("utf-8")), importado_utc=datetime.now(timezone.utc).isoformat())
    return messages
