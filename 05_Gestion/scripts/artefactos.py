"""Helpers de formato para el sistema local de artefactos (solo stdlib)."""
from __future__ import annotations
import re, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)

def parse_frontmatter(text: str):
    match = FM_RE.match(text)
    if not match: return {}, text
    data, current = {}, None
    for line in match.group(1).splitlines():
        if line.startswith("  - ") and current: data[current].append(unquote(line[4:]))
        elif ":" in line:
            key, value = line.split(":", 1); key, value = key.strip(), value.strip(); current = key
            if value == "[]": data[key] = []
            elif value: data[key] = unquote(value)
            else: data[key] = []
    return data, text[match.end():]

def unquote(value):
    return value[1:-1] if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'" else value

def quote(value):
    text = str(value)
    if not text or re.search(r"[:#\[\]{}&,*!|>'\"%@`]|^\s|\s$", text):
        return '"' + text.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return text

def frontmatter_text(data):
    lines = ["---"]
    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f"{key}: []" if not value else f"{key}:")
            if value: lines.extend(f"  - {quote(item)}" for item in value)
        else: lines.append(f"{key}: {quote(value)}")
    return "\n".join(lines + ["---", ""])

def words(text):
    _, body = parse_frontmatter(text); body = re.sub(r"```.*?```", " ", body, flags=re.S)
    return len(re.findall(r"\b[\wÁÉÍÓÚÜÑáéíóúüñ.-]+\b", body))

def status_for(text):
    count = words(text)
    return "vacio" if count < 5 else "esqueleto" if count < 35 else "borrador"

def normalize(text):
    import unicodedata
    text = unicodedata.normalize("NFKD", text.casefold())
    return "".join(ch for ch in text if not unicodedata.combining(ch))

def docx_blocks(path):
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    with zipfile.ZipFile(path) as zf:
        doc = ET.fromstring(zf.read("word/document.xml")); styles = {}
        rels = {}
        if "word/_rels/document.xml.rels" in zf.namelist():
            relroot=ET.fromstring(zf.read("word/_rels/document.xml.rels"))
            rels={x.attrib.get("Id",""):x.attrib.get("Target","") for x in list(relroot)}
        if "word/styles.xml" in zf.namelist():
            root = ET.fromstring(zf.read("word/styles.xml"))
            for style in root.findall(".//w:style", ns):
                sid = style.attrib.get("{%s}styleId" % ns["w"], ""); name = style.find("w:name", ns)
                if sid and name is not None: styles[sid] = name.attrib.get("{%s}val" % ns["w"], "")
        body = doc.find("w:body", ns); blocks = []
        if body is None: return blocks
        for el in list(body):
            tag = el.tag.rsplit("}", 1)[-1]
            if tag == "p":
                text = "".join(t.text or "" for t in el.findall(".//w:t", ns)).strip()
                blip=el.find(".//{http://schemas.openxmlformats.org/drawingml/2006/main}blip")
                if not text and blip is None: continue
                if blip is not None:
                    rid=blip.attrib.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed","")
                    target=rels.get(rid,"").replace("\\","/")
                    blocks.append({"kind":"figure","level":"","text":text or "Figura incrustada","media_ref":target})
                    if not text: continue
                ppr = el.find("w:pPr/w:pStyle", ns); sid = ppr.attrib.get("{%s}val" % ns["w"], "") if ppr is not None else ""
                name = styles.get(sid, sid); match = re.search(r"(?:heading|t[ií]tulo)\s*(\d+)", name, re.I)
                blocks.append({"kind": "heading" if match else "paragraph", "level": match.group(1) if match else "", "text": text})
            elif tag == "tbl":
                rows = []
                for row in el.findall(".//w:tr", ns):
                    cells = []
                    for cell in row.findall("w:tc", ns):
                        cells.append(" ".join("".join(t.text or "" for t in p.findall(".//w:t", ns)).strip() for p in cell.findall("w:p", ns)).strip())
                    rows.append(" | ".join(cells))
                if rows: blocks.append({"kind": "table", "level": "", "text": "\n".join(rows)})
    return blocks

def extract_docx_media(path, references, destination):
    """Copia medios referenciados por bloques DOCX; no procesa archivos no referenciados."""
    copied={}
    with zipfile.ZipFile(path) as zf:
        for ref in references:
            if not ref or ref.startswith("/") or ".." in Path(ref).parts: continue
            member="word/"+ref
            if member not in zf.namelist(): continue
            name=Path(ref).name
            out=destination/name
            out.parent.mkdir(parents=True,exist_ok=True)
            if not out.exists(): out.write_bytes(zf.read(member))
            copied[ref]=out
    return copied

def source_blocks(path):
    if path.suffix.casefold() == ".docx": return docx_blocks(path)
    if path.suffix.casefold() != ".md": raise ValueError("Formato de origen no soportado; use .md o .docx")
    _, text = parse_frontmatter(path.read_text(encoding="utf-8-sig")); blocks = []
    lines=text.splitlines(); i=0
    while i<len(lines):
        line=lines[i]
        if not line.strip(): i+=1; continue
        heading=re.match(r"^(#{1,6})\s+(.*)$",line)
        figure=re.match(r"^!\[([^]]*)\]\(([^)]+)\)",line.strip())
        if heading: blocks.append({"kind":"heading","level":str(len(heading.group(1))),"text":heading.group(2).strip()}); i+=1; continue
        if figure: blocks.append({"kind":"figure","level":"","text":figure.group(1) or "Figura","media_ref":figure.group(2)}); i+=1; continue
        if line.lstrip().startswith("|"):
            rows=[]
            while i<len(lines) and lines[i].lstrip().startswith("|"):
                rows.append([cell.strip() for cell in lines[i].strip().strip("|").split("|")]); i+=1
            blocks.append({"kind":"table","level":"","text":"\n".join(" | ".join(row) for row in rows)}); continue
        if line.lstrip().startswith("```"):
            lang=line.strip()[3:].strip(); code=[]; i+=1
            while i<len(lines) and not lines[i].lstrip().startswith("```"): code.append(lines[i]); i+=1
            if i<len(lines): i+=1
            blocks.append({"kind":"paragraph","level":"", "text":"```"+lang+"\n"+"\n".join(code)+"\n```"}); continue
        blocks.append({"kind":"paragraph","level":"","text":line.rstrip()}); i+=1
    return blocks
