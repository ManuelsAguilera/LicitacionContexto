#!/usr/bin/env python3
"""Verificador de reglas de redacción sobre los sd-NN.tex (reglas RR-NN de convenciones/reglas-redaccion.md).

Solo informa: nunca edita ni convierte contenido. Revisa lo que se puede comprobar de forma
mecánica; el resto de las reglas queda para revisión humana (columna Verificación de la convención).
ERROR: incumplimiento claro. AVISO: heurística que requiere criterio humano.
Se usa desde exportar_latex.py (verificar-redaccion).
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import exportar_latex as ex

ENVIRONMENTS = {"longtable": "table", "figure": "figure", "itemize": "list", "enumerate": "list", "description": "list"}
BEGIN_END = re.compile(r"\\(begin|end)\{(" + "|".join(ENVIRONMENTS) + r")\}")
HEADING = re.compile(r"^(?:\\hypertarget\{[^}]*\}\{%\s*)?\\(section|subsection|subsubsection|paragraph|subparagraph)\*?\{")
HEADING_TITLE = re.compile(r"\\(?:section|subsection|subsubsection|paragraph|subparagraph)\*?\{(.*?)\}\s*(?:\\label|$)", re.S)
SKIP_LINES = re.compile(r"^(?:\\clearpage|\\newpage|\\tableofcontents|\\ossCover\{[^\n]*\}\{[^\n]*\}|\\ossFinalPage|\\end\{document\})[ \t]*$", re.M)
SKIP_ONLY = re.compile(r"^(?:\}|\\label\{[^}]*\}\}?)$")
TABLE_TITLE = re.compile(r"^Tabla\s+\d")
FIGURE_TITLE = re.compile(r"^Figura\s+\d")
SENTENCE_BREAK = re.compile(r"[.!?](?=\s+[A-ZÁÉÍÓÚÑ])")
STRONG_MARKERS = re.compile(
    r"\bTODO\b|\[VERIFICAR\]|(?i:\[INSERTAR|\[cite:|Anexo \?\?|por indicaci[oó]n del usuario|pendiente de validar|\bborrador\b)")
ACADEMIC_WORDS = re.compile(r"\b(docente|estudiantes?|propuesta acad[eé]mica|asignatura)\b", re.I)
PRICE_HINT = re.compile(r"\bCLP\b|\bUF\s?\d|\bUSD\b|\bUS\\\$|valor(?:es)? unitarios?|\btarifas?\b", re.I)
MAX_COLUMNS = 5
MAX_ROWS_PER_PAGE = 25


@dataclass
class Finding:
    rule: str
    level: str  # ERROR | AVISO
    line: int
    message: str

    def __str__(self) -> str:
        return f"{self.level} {self.rule} línea {self.line}: {self.message}"


@dataclass
class Block:
    kind: str  # heading | text | table | figure | list
    text: str
    line: int
    level: int = 0


def environment_spans(body: str) -> list[tuple[int, int, str]]:
    """Intervalos (inicio, fin, tipo) de los entornos de nivel superior, tolerando anidamiento."""
    spans, stack = [], []
    for match in BEGIN_END.finditer(body):
        if match.group(1) == "begin":
            stack.append((match.start(), match.group(2)))
        elif stack:
            start, name = stack.pop()
            if not stack:
                spans.append((start, match.end(), ENVIRONMENTS[name]))
    return spans


def parse_blocks(text: str) -> list[Block]:
    start = text.index("\\begin{document}") + len("\\begin{document}")
    body = SKIP_LINES.sub("", text[start:])
    base_line = text[:start].count("\n") + 1
    blocks: list[Block] = []

    def add_text(chunk_start: int, chunk: str) -> None:
        offset = 0
        for part in re.split(r"\n\s*\n", chunk):
            index = chunk.index(part, offset) if part else offset
            offset = index + len(part)
            stripped = part.strip()
            if not stripped or SKIP_ONLY.match(stripped):
                continue
            line = base_line + body[: chunk_start + index].count("\n") + part[: len(part) - len(part.lstrip())].count("\n")
            heading = HEADING.match(stripped)
            if heading:
                level = ["section", "subsection", "subsubsection", "paragraph", "subparagraph"].index(heading.group(1)) + 1
                title = HEADING_TITLE.search(stripped)
                blocks.append(Block("heading", re.sub(r"\s+", " ", title.group(1)).strip() if title else stripped[:60], line, level))
            else:
                blocks.append(Block("text", stripped, line))

    cursor = 0
    for begin, end, kind in environment_spans(body):
        add_text(cursor, body[cursor:begin])
        blocks.append(Block(kind, body[begin:end], base_line + body[:begin].count("\n")))
        cursor = end
    add_text(cursor, body[cursor:])
    return blocks


def plain(text: str) -> str:
    text = re.sub(r"\\(?:begin|end)\{[^}]*\}(?:\[[^\]]*\])?", " ", text)
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?", " ", text)
    return re.sub(r"[{}\\]|\s+", " ", text).strip()


def table_rows(table: str) -> list[list[str]]:
    marker = max(table.rfind("\\endlastfoot"), table.rfind("\\endhead"))
    rows_text = table[marker:].split("\n", 1)[1] if marker >= 0 and "\n" in table[marker:] else ""
    rows_text = rows_text.split("\\end{longtable}")[0]
    rows = [r for r in re.split(r"\\\\\s*\n", rows_text) if r.strip()]
    return [[c.strip() for c in row.split(" & ")] for row in rows]


def header_cells(table: str) -> list[str]:
    head = table.split("\\midrule")[0]
    cells = re.findall(r"\\begin\{minipage\}\[b\]\{\\linewidth\}\\raggedright\s*(.*?)\s*\\end\{minipage\}", head, re.S)
    return [plain(c) for c in cells]


def check_blocks(blocks: list[Block]) -> list[Finding]:
    findings: list[Finding] = []
    for i, block in enumerate(blocks):
        following = blocks[i + 1] if i + 1 < len(blocks) else None
        previous = blocks[i - 1] if i else None
        if block.kind == "heading" and following is not None:
            if following.kind == "heading":
                findings.append(Finding("RR-04", "ERROR", block.line, f"el título «{block.text}» va seguido directamente de otro título"))
            elif following.kind in ("table", "figure", "list"):
                names = {"table": "una tabla", "figure": "una figura", "list": "una lista"}
                findings.append(Finding("RR-04", "ERROR", block.line, f"el título «{block.text}» va seguido de {names[following.kind]} sin texto de caída"))
        if block.kind == "table":
            rows = table_rows(block.text)
            columns = max((len(r) for r in rows), default=0)
            if columns > MAX_COLUMNS:
                findings.append(Finding("RR-17", "ERROR", block.line, f"la tabla tiene {columns} columnas (máximo {MAX_COLUMNS})"))
            if len(rows) > MAX_ROWS_PER_PAGE:
                findings.append(Finding("RR-18", "AVISO", block.line, f"la tabla tiene {len(rows)} filas; probablemente excede una página (listado completo al anexo, síntesis en el cuerpo)"))
            heads = header_cells(block.text)
            if len(heads) == 2 and re.match(r"(descripci|definici|explicaci|significado)", heads[1], re.I):
                findings.append(Finding("RR-16", "AVISO", block.line, f"tabla «{heads[0]} | {heads[1]}»: es texto puesto en una tabla"))
            long_cells = sum(1 for row in rows for cell in row if SENTENCE_BREAK.search(plain(cell)))
            if long_cells:
                findings.append(Finding("RR-16", "AVISO", block.line, f"{long_cells} celda(s) con más de una frase: ese contenido corresponde a texto"))
            titled = any(b is not None and b.kind == "text" and TABLE_TITLE.match(b.text) for b in (previous, following))
            if not titled:
                findings.append(Finding("RR-19", "AVISO", block.line, "tabla sin título numerado («Tabla N.N: …») inmediatamente antes o después"))
            if following is None or following.kind != "text" or TABLE_TITLE.match(following.text):
                findings.append(Finding("RR-19", "AVISO", block.line, "la tabla no va seguida de texto que diga qué se concluye de ella"))
        if block.kind == "figure":
            caption = re.search(r"\\caption\{(.*?)\}\s*(?:\\end|$)", block.text, re.S)
            if not caption:
                findings.append(Finding("RR-11", "AVISO", block.line, "figura sin leyenda (\\caption)"))
            titled = any(b is not None and b.kind == "text" and FIGURE_TITLE.match(b.text) for b in (previous, following))
            if not titled and not (caption and re.search(r"Figura\s+\d", caption.group(1))):
                findings.append(Finding("RR-11", "AVISO", block.line, "figura sin título numerado («Figura N.N: …»)"))
            context = " ".join(b.text for b in (previous, following) if b is not None and b.kind == "text")
            if not re.search(r"fuente|elaboraci[oó]n propia|\(.*\d{4}\)", (caption.group(1) if caption else "") + " " + context, re.I):
                findings.append(Finding("RR-14", "AVISO", block.line, "figura sin fuente (elaboración propia o referencia APA 7)"))
    return findings


def check_sections(blocks: list[Block]) -> list[Finding]:
    """RR-05: un capítulo dominado por tablas y listas no cumple lo solicitado."""
    findings: list[Finding] = []
    chapters: list[list[Block]] = []
    for block in blocks:
        if block.kind == "heading" and block.level == 1:
            chapters.append([block])
        elif chapters:
            chapters[-1].append(block)
    for chapter in chapters:
        words = {"table": 0, "list": 0, "text": 0}
        for block in chapter[1:]:
            if block.kind in words:
                words[block.kind] += len(plain(block.text).split())
        total = sum(words.values())
        if total and (words["table"] + words["list"]) / total > 0.6:
            findings.append(Finding("RR-05", "AVISO", chapter[0].line, f"«{chapter[0].text}»: {round(100 * (words['table'] + words['list']) / total)} % del contenido son tablas y listas"))
    return findings


def check_text(text: str) -> list[Finding]:
    findings: list[Finding] = []
    start = text.index("\\begin{document}")
    for number, line in enumerate(text.splitlines(), 1):
        if number <= text[:start].count("\n") + 1:
            continue
        for pattern, rule, level, label in (
            (STRONG_MARKERS, "RR-22", "ERROR", "marcador de borrador o del asistente"),
            (ACADEMIC_WORDS, "RR-22", "AVISO", "lenguaje de contexto académico"),
            (PRICE_HINT, "RR-08", "AVISO", "posible precio o tarifa (la Oferta Técnica no puede contener valores)"),
        ):
            match = pattern.search(line)
            if match:
                findings.append(Finding(rule, level, number, f"{label}: «{match.group(0)}»"))
    body = text[start:]
    sections = re.findall(r"\\section\*?\{(.*?)\}", body, re.S)
    names = [re.sub(r"\s+", " ", s).strip().lower() for s in sections]
    if "referencias" not in names or "declaración de uso de ia" not in names:
        findings.append(Finding("RR-21", "AVISO", 1, "faltan las secciones finales sin numerar «Referencias» y «Declaración de uso de IA»"))
    elif names.index("referencias") > names.index("declaración de uso de ia"):
        findings.append(Finding("RR-21", "ERROR", 1, "«Referencias» debe ir antes de «Declaración de uso de IA»"))
    return findings


def check_file(tex: Path) -> list[Finding]:
    text = tex.read_text(encoding="utf-8")
    blocks = parse_blocks(text)
    return sorted(check_blocks(blocks) + check_sections(blocks) + check_text(text), key=lambda f: (f.line, f.rule))


def report(parts: list[str]) -> int:
    """Imprime los hallazgos por parte; devuelve 1 si hay algún ERROR."""
    errors = 0
    for part in parts:
        tex = ex.LATEX / f"sd-{part[-2:]}.tex"
        if not tex.is_file():
            continue
        findings = check_file(tex)
        n_err = sum(f.level == "ERROR" for f in findings)
        errors += n_err
        print(f"{part}: {n_err} error(es), {len(findings) - n_err} aviso(s)")
        for finding in findings:
            print(f"  {finding}")
    return 1 if errors else 0
