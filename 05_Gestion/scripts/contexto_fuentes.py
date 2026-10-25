"""Selección de fuentes actuales para briefing y estado, sin modificar documentos."""
from __future__ import annotations
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
from artefactos import parse_frontmatter, normalize

PART = re.compile(r"^T7-(0[1-9]|1[0-4])(?:-(.+))?$")
FORM = re.compile(r"^T-(\d{1,2})$")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main_tex(root: Path, part: str) -> Path:
    return root / f"02_Propuesta/latex_final/sd-{part[3:5]}/OnlySimpleSolutions-Subdocumento{int(part[3:5])}.tex"


def metadata(path: Path | None) -> dict:
    return parse_frontmatter(path.read_text(encoding="utf-8-sig"))[0] if path else {}


def master(root: Path, part: str) -> Path | None:
    folders = sorted((root / "02_Propuesta").glob(f"sd-{part[3:5]}_*"))
    if len(folders) != 1: return None
    canonical = folders[0] / f"{folders[0].name}.md"
    if canonical.is_file(): return canonical
    candidates = [p for p in sorted(folders[0].glob("*.md")) if metadata(p).get("id") == part]
    if len(candidates) == 1: return candidates[0]
    files = list(folders[0].glob("*.md"))
    return files[0] if len(files) == 1 else None


def section_text(text: str, section_id: str) -> tuple[str, str | None]:
    """Solo títulos identificados explícitamente; nunca infiere numeración."""
    levels = {"section": 1, "subsection": 2, "subsubsection": 3, "paragraph": 4, "subparagraph": 5}
    headings = []
    for match in re.finditer(r"(?m)^[ \t]*\\(section|subsection|subsubsection|paragraph|subparagraph)\*?\{", text):
        pos, depth, end = match.end(), 1, match.end()
        while end < len(text) and depth:
            if text[end] == "{" and text[end - 1] != "\\": depth += 1
            if text[end] == "}" and text[end - 1] != "\\": depth -= 1
            end += 1
        title = text[pos:end - 1]
        number = re.match(r"\s*(\d+(?:\.\d+)*)(?=\s|$|[·:])", title)
        named = normalize(re.sub(r"\\[A-Za-z]+", "", title)).strip()
        found = ((section_id == "REF" and named == "referencias") or
                 (section_id == "IA" and named == "declaracion de uso de ia") or
                 (number is not None and number[1] == section_id))
        headings.append((match.start(), levels[match[1]], found))
    matches = [i for i, h in enumerate(headings) if h[2]]
    if len(matches) != 1:
        return text.split(r"\begin{document}", 1)[-1], "Sección sin correspondencia inequívoca en LaTeX; se muestra la fuente principal."
    i = matches[0]
    start, level, _ = headings[i]
    finish = next((h[0] for h in headings[i + 1:] if h[1] <= level), len(text))
    return text[start:finish], None


@dataclass
class Source:
    requested_id: str
    part: str | None
    path: Path
    text: str
    meta: dict
    warning: str | None = None


def resolve(root: Path, artifact_id: str) -> Source:
    match = PART.fullmatch(artifact_id)
    if match:
        part, m = artifact_id[:5], master(root, artifact_id[:5])
        tex = main_tex(root, part)
        if tex.is_file():
            text = tex.read_text(encoding="utf-8-sig")
            text, warning = section_text(text, match[2]) if match[2] else (text.split(r"\begin{document}", 1)[-1], None)
            return Source(artifact_id, part, tex, text, metadata(m), warning)
        if m:
            candidates = [p for p in sorted(m.parent.glob("*.md")) if metadata(p).get("id") == artifact_id]
            if artifact_id == part and not candidates: candidates = [m]
            if len(candidates) == 1:
                p = candidates[0]
                fm, body = parse_frontmatter(p.read_text(encoding="utf-8-sig"))
                return Source(artifact_id, part, p, body, fm, "Fuente Markdown: todavía no existe LaTeX importado para esta parte.")
    form = FORM.fullmatch(artifact_id)
    if form:
        p = root / f"02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-{int(form[1])}.tex"
        if p.is_file():
            return Source(artifact_id, None, p, p.read_text(encoding="utf-8-sig").split(r"\begin{document}", 1)[-1], {})
        raise ValueError(f"{artifact_id}: falta la fuente de Formularios; no se usa una copia de recepción")
    if re.fullmatch(r"ADJ-\d{3}", artifact_id):
        registry = root / "05_Gestion/adjuntos.json"
        items = [r for r in json.loads(registry.read_text(encoding="utf-8")) if r["id"] == artifact_id] if registry.is_file() else []
        if len(items) == 1:
            item = items[0]
            form_id = re.search(r"form-(T-\d+)_", item.get("nombre", ""), re.I)
            if form_id:
                try:
                    result = resolve(root, form_id[1].upper())
                    result.requested_id = artifact_id
                    return result
                except ValueError: pass
            p = (root / item["ruta"]).resolve()
            if not p.is_relative_to(root.resolve()) or any(x in p.parts for x in ("historico", "archivo-contexto", "build", "respaldo")):
                raise ValueError(f"{artifact_id}: ruta histórica o fuera del contexto activo")
            if p.is_file():
                if p.suffix.lower() not in {".tex", ".md", ".txt"}:
                    raise ValueError(f"{artifact_id}: adjunto binario; consultar {p.relative_to(root)} con su herramienta de lectura")
                fm, body = parse_frontmatter(p.read_text(encoding="utf-8-sig"))
                return Source(artifact_id, item.get("parte"), p, body, fm)
    raise ValueError(f"No se encontró fuente vigente para {artifact_id}")


def compilation(root: Path, part: str) -> str:
    report = root / "02_Propuesta/latex_final/build/ultimo-reporte.json"
    if not report.is_file(): return "sin registro disponible"
    try:
        data = json.loads(report.read_text(encoding="utf-8"))
        row = next((r for r in data.get("partes", []) if r.get("id") == part), None)
        if row:
            pdf = root / row["pdf"].replace("\\", "/")
            if not pdf.is_file(): return "registro disponible, PDF ausente"
            if row.get("fuente_sha256"):
                return "correcta, hash coincidente" if row["fuente_sha256"] == sha256(main_tex(root, part)) else "registro de una fuente anterior"
            return "PDF disponible; vigencia de fuente no acreditada por hash"
    except (ValueError, KeyError, OSError): return "registro ilegible; por verificar"
    return "sin registro disponible"


def review(meta: dict) -> str:
    if meta.get("estado") in {"revisado", "congelado"}:
        return "declarada; comprobar persona y evidencia en el maestro"
    return "sin revisión humana registrada"
