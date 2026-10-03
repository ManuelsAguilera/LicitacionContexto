#!/usr/bin/env python3
"""Propone mapeo conservador de documento completo a artefactos Markdown."""
from __future__ import annotations
import argparse, base64, hashlib, json, re, sys, zipfile
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as ET
from artefactos import ROOT, extract_docx_media, frontmatter_text, parse_frontmatter, source_blocks

def pilot_sections(part):
    cfg=ROOT/"05_Gestion"/"migraciones"/(part+".json")
    if not cfg.exists(): raise ValueError(f"No hay índice/mapa de migración configurado para {part}")
    return json.loads(cfg.read_text(encoding="utf-8"))

def chapter_chunks(blocks, part):
    num=int(part[3:]); start=re.compile(rf"^\s*{num}\.?\s*CAP[IÍ]TULO\s+{['','I','II','III','IV','V','VI','VII','VIII','IX','X'][num]}\b",re.I)
    end=re.compile(rf"^\s*{num+1}\.?\s*CAP[IÍ]TULO\b",re.I)
    standalone_start=re.compile(
        rf"^{num}\.\s*(?:introducci[oó]n y alcance|esquema de soluci[oó]n|comprensi[oó]n del problema y (?:de )?la necesidad)",
        re.I,
    )
    standalone=any(b["kind"]=="heading" and standalone_start.search(clean_heading(b["text"])) for b in blocks)
    active=False; chunks=[]; current=None; outside=[]
    for index,b in enumerate(blocks,1):
        title=clean_heading(b["text"]) if b["kind"]=="heading" else b["text"].strip()
        if b["kind"]=="heading" and ((standalone and standalone_start.search(title)) or (not standalone and start.search(title))):
            active=True; current={"heading":title,"blocks":[]} if standalone else None; continue
        if b["kind"]=="heading" and active and ((standalone and re.match(r"^(?:referencias|a\.\s*anexos|declaraci[oó]n de uso de ia)\b",title,re.I)) or (not standalone and end.search(title))):
            if current: chunks.append(current)
            active=False; current=None; continue
        if not active:
            outside.append({"bloque_origen":index,**b}); continue
        if b["kind"]=="heading":
            if current: chunks.append(current)
            current={"heading":title,"level":b.get("level",""),"blocks":[]}
        else:
            if current is None: current={"heading":"(texto previo al primer encabezado)","blocks":[]}
            current["blocks"].append(b)
    if current: chunks.append(current)
    return chunks,outside

def clean_heading(title):
    title=re.sub(r"\s*\{#.*\}\s*$","",str(title)).strip()
    title=re.sub(r"^\*+|\*+$","",title).strip()
    title=re.sub(r"\\([.])",r"\1",title)
    if re.match(r"^3\.?\s+Objetivos del proyecto\b",title,re.I): title=re.sub(r"^3\.?\s+","3.5 ",title)
    return re.sub(r"\s+"," ",title)

def table_rows(table_text):
    rows=[[cell.strip() for cell in line.split(" | ")] for line in str(table_text).splitlines() if line.strip()]
    if not rows: return []
    width=max(len(row) for row in rows)
    return [row+[""]*(width-len(row)) for row in rows]

def table_markdown(rows):
    if not rows: return ""
    header=rows[0]
    return "\n".join([
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(":---" for _ in header) + " |",
        *("| " + " | ".join(row) + " |" for row in rows[1:]),
    ])

def table_paragraphs(table_text):
    rows=table_rows(table_text)
    if len(rows)<2: return ["; ".join(rows[0])] if rows else []
    headers=rows[0]; paragraphs=[]
    for row in rows[1:]:
        populated=[(headers[i] if headers[i] else f"Campo {i+1}",value) for i,value in enumerate(row) if value]
        if len(headers)==2 and len(populated)==2:
            paragraphs.append(f"**{populated[0][1].rstrip().removesuffix('.')}:** {populated[1][1].rstrip().removesuffix('.')}.")
        else:
            pairs=[f"**{header}:** {value.rstrip().removesuffix('.')}" for header,value in populated]
            if pairs: paragraphs.append(". ".join(pairs)+".")
    return paragraphs

def table_profile(table_text):
    rows=table_rows(table_text)
    columns=len(rows[0]) if rows else 0
    data_rows=max(0,len(rows)-1)
    multidimensional=columns>=3
    extensive=data_rows>12 or columns>5 or any(len(cell)>280 for row in rows for cell in row)
    paragraphs=table_paragraphs(table_text)
    paragraph_length=len("\n\n".join(paragraphs))
    table_length=len(table_markdown(rows))
    paragraph_is_shorter=bool(paragraphs) and paragraph_length<table_length
    return {
        "rows":rows,
        "columns":columns,
        "data_rows":data_rows,
        "multidimensional":multidimensional,
        "extensive":extensive,
        "paragraphs":paragraphs,
        "paragraph_is_shorter":paragraph_is_shorter,
    }

def split_multidimensional_table(rows, max_data_rows=10):
    """Divide tablas largas por filas y tablas muy anchas por grupos de dimensiones."""
    if not rows: return []
    header=rows[0]; column_groups=[]
    if len(header)>5:
        anchors=list(range(min(2,len(header))))
        for start in range(2,len(header),3): column_groups.append(anchors+list(range(start,min(start+3,len(header)))))
    else:
        column_groups=[list(range(len(header)))]
    rendered=[]
    data=rows[1:]
    row_groups=[data[i:i+max_data_rows] for i in range(0,len(data),max_data_rows)] or [[]]
    total=len(column_groups)*len(row_groups); number=0
    for columns in column_groups:
        for group in row_groups:
            number+=1
            selected=[[row[i] for i in columns] for row in [header,*group]]
            if total>1: rendered.append(f"**Tabla — bloque {number} de {total}.**")
            rendered.append(table_markdown(selected))
    return rendered

def render_table(table_text, selective=False):
    profile=table_profile(table_text)
    if not selective:
        return [table_markdown(profile["rows"])]
    if profile["extensive"] and not profile["multidimensional"] and profile["paragraph_is_shorter"]:
        return ["<!-- tabla convertida: extensa, no multidimensional y más breve como prosa -->",*profile["paragraphs"]]
    if profile["extensive"] and profile["multidimensional"]:
        return ["<!-- tabla dividida: extensa y multidimensional; se conservan sus dimensiones -->",*split_multidimensional_table(profile["rows"])]
    reason="compara múltiples dimensiones" if profile["multidimensional"] else "la prosa no sería más breve y clara"
    return [f"<!-- tabla conservada: {reason} -->",table_markdown(profile["rows"])]

def normalize_heading(text):
    import unicodedata
    text=unicodedata.normalize("NFKD",text.casefold())
    return re.sub(r"[^a-z0-9]+"," ","".join(c for c in text if not unicodedata.combining(c))).strip()

def source_subheading(title, target_title):
    cleaned=clean_heading(title)
    unnumbered=re.sub(r"^\d+(?:\.\d+)*\.?\s*","",cleaned)
    if normalize_heading(unnumbered)==normalize_heading(target_title): return None
    numbered=re.match(r"^(\d+(?:\.\d+)*)\.?\s+(.+)$",cleaned)
    if numbered: return min(5,max(2,len(numbered.group(1).split(".")))),numbered.group(2).strip()
    if re.match(r"^3\.\s*Introducci[oó]n y alcance",cleaned,re.I): return 2,"Introducción del subdocumento"
    return 3,cleaned

def suggested(rows, rules):
    by_prefix={x["origen"]:x for x in rules}
    for row in rows:
        row["titulo_origen"]=clean_heading(row["titulo_origen"])
        m=re.match(r"^\s*(\d+(?:\.\d+)*)\b",row["titulo_origen"])
        if not m:
            if re.search(r"\bsupuestos\b",row["titulo_origen"],re.I) and by_prefix.get("3.2"):
                rule=by_prefix["3.2"]; row.update({"seccion_sugerida":rule["destino"],"revision":"sugerida_revisar","motivo":rule["motivo"]}); continue
            row.update({"seccion_sugerida":"","revision":"sin_correspondencia","motivo":"sin numeración reconocible"}); continue
        parts=m.group(1).split("."); base=".".join(parts[:2]) if len(parts)>1 else parts[0]; rule=by_prefix.get(base)
        if not rule:
            row.update({"seccion_sugerida":"","revision":"sin_correspondencia","motivo":"sin regla de asignación"}); continue
        row.update({"seccion_sugerida":rule["destino"],"revision":"sugerida_revisar","motivo":rule["motivo"]})
    return rows

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--fuente",type=Path,required=True); ap.add_argument("--parte",required=True); ap.add_argument("--dry-run",action="store_true"); ap.add_argument("--mapa-aprobado",type=Path); ap.add_argument("--reporte",type=Path); ap.add_argument("--plantilla-mapa",type=Path,help="Escribe asignaciones sugeridas sin declararlas aprobadas"); ap.add_argument("--tablas-a-parrafos",action="store_true",help="Aplica conversión selectiva: solo pasa a prosa tablas extensas, no multidimensionales y más breves como párrafos; divide las extensas multidimensionales"); ap.add_argument("--actualizar-migrados",action="store_true",help="Permite regenerar únicamente artefactos borrador provenientes de la misma fuente")
    a=ap.parse_args()
    if not re.fullmatch(r"T7-\d{2}",a.parte): ap.error("--parte debe ser T7-NN")
    try:
        spec=pilot_sections(a.parte); blocks=source_blocks(a.fuente); chunks,outside=chapter_chunks(blocks,a.parte)
        rows=[]
        for i,c in enumerate(chunks,1): rows.append({"bloque":i,"titulo_origen":c["heading"],"contenido":c["blocks"]})
        rows=suggested(rows,spec.get("reglas_sugeridas",[]))
    except Exception as exc: print(f"Error: {exc}",file=sys.stderr); return 2
    digest=hashlib.sha256(a.fuente.read_bytes()).hexdigest(); spec_digest=hashlib.sha256((ROOT/"05_Gestion"/"migraciones"/(a.parte+".json")).read_bytes()).hexdigest()
    report={"parte":a.parte,"fuente":str(a.fuente),"sha256_fuente":digest,"sha256_especificacion":spec_digest,"bloques_fuera_del_capitulo":len(outside),"fragmentos_fuera_del_capitulo":outside,"secciones_destino":spec["secciones"],"bloques":rows,"resumen":{"bloques_capitulo":len(rows),"asignados_sugeridos":sum(bool(x["seccion_sugerida"]) for x in rows),"requieren_revision":sum(x["revision"]!="coincidencia_exacta" for x in rows),"sin_correspondencia":sum(not x["seccion_sugerida"] for x in rows),"figuras":sum(b["kind"]=="figure" for r in rows for b in r["contenido"]),"figuras_fuera_capitulo":sum(b["kind"]=="figure" for b in outside),"tablas":sum(b["kind"]=="table" for r in rows for b in r["contenido"]),"tablas_fuera_capitulo":sum(b["kind"]=="table" for b in outside)}}
    if a.reporte: a.reporte.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    if a.plantilla_mapa:
        template={"sha256_fuente":digest,"sha256_especificacion":spec_digest,"aprobado_por":"","aprobado_el":"","asignaciones":{str(r["bloque"]):r["seccion_sugerida"] for r in rows}}
        a.plantilla_mapa.write_text(json.dumps(template,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    if a.dry_run:
        summary={k:v for k,v in report.items() if k not in {"bloques","fragmentos_fuera_del_capitulo","secciones_destino"}}
        if a.reporte: print(json.dumps(summary,ensure_ascii=True,indent=2))
        else: print(json.dumps(summary | {"mapeo":[{k:r[k] for k in ("bloque","titulo_origen","seccion_sugerida","revision","motivo")} for r in rows]},ensure_ascii=True,indent=2))
        return 0
    if not a.mapa_aprobado: print("Aplicación detenida: revise el reporte y proporcione --mapa-aprobado.",file=sys.stderr); return 3
    approval=json.loads(a.mapa_aprobado.read_text(encoding="utf-8"))
    if approval.get("sha256_fuente")!=digest or approval.get("sha256_especificacion")!=spec_digest: print("El mapa aprobado corresponde a otra versión de la fuente o índice.",file=sys.stderr); return 4
    if not approval.get("aprobado_por") or not approval.get("aprobado_el"):
        print("El mapa debe incluir aprobado_por y aprobado_el tras revisión humana.",file=sys.stderr); return 4
    assignments=approval.get("asignaciones",{}); valid={s["id"] for s in spec["secciones"]}
    for row in rows:
        row["seccion_sugerida"]=assignments.get(str(row["bloque"]),row["seccion_sugerida"])
        if not row["seccion_sugerida"] or row["seccion_sugerida"] not in valid: print(f"Bloque {row['bloque']} sin destino aprobado; no se escribió nada.",file=sys.stderr); return 5
    folder=next(iter((ROOT/"02_Propuesta").glob(f"sd-{a.parte[3:]}_*")),None)
    if folder is None: print("Carpeta T-7 no encontrada",file=sys.stderr); return 6
    staged=[]; media_refs={b.get("media_ref","") for r in rows for b in r["contenido"] if b["kind"]=="figure"}
    media_dest=ROOT/"04_Adjuntos"/"migracion"/a.parte
    if a.fuente.suffix.casefold()==".docx":
        media_files={ref: media_dest/Path(ref).name for ref in media_refs if ref}
        collisions=[p for p in media_files.values() if p.exists() and not a.actualizar_migrados]
        if collisions: print(f"No se sobrescriben recursos existentes: {collisions}",file=sys.stderr); return 8
    else:
        media_files={}
        for ref in media_refs:
            if not ref or ref.startswith(("http:","https:")): continue
            if ref.startswith("data:image/"):
                mime=re.match(r"data:image/([^;]+);base64,",ref)
                if not mime: print("Formato de imagen data URI no reconocido; no se escribe ningún artefacto.",file=sys.stderr); return 9
                ext={"jpeg":".jpg","svg+xml":".svg"}.get(mime.group(1),"."+mime.group(1).split("+")[0])
                dest=media_dest/("figura-"+hashlib.sha256(ref.encode("utf-8")).hexdigest()[:12]+ext)
            else:
                source_media=(a.fuente.parent/ref).resolve()
                if not source_media.is_file():
                    print(f"Figura no localizada: {ref}; no se escribe ningún artefacto.",file=sys.stderr); return 9
                dest=media_dest/source_media.name
            if dest.exists() and not a.actualizar_migrados: print(f"No se sobrescribe recurso existente: {dest}",file=sys.stderr); return 8
            media_files[ref]=dest
    for section in spec["secciones"]:
        chosen=[r for r in rows if r["seccion_sugerida"]==section["id"]]
        if not chosen: continue
        source_nums=[]; plain=[]
        for row in chosen:
            source_nums.append(str(row["bloque"]))
            if row["titulo_origen"]: plain.append(row["titulo_origen"])
            for b in row["contenido"]:
                if b["kind"]=="figure" and b.get("media_ref") in media_files:
                    rel=Path("../..")/"04_Adjuntos"/"migracion"/a.parte/media_files[b["media_ref"]].name
                    plain += [f"![{b['text']}]({rel.as_posix()})"]
                elif b["kind"]=="table": plain += [b["text"]]
                else: plain += [str(b["text"])]
        heading_number=section["id"].split("-",2)[2]
        body=[f"# {heading_number} {section['titulo']}","", "<!-- contenido migrado desde la fuente; permanece en borrador y requiere revisión humana -->", ""]
        for row in chosen:
            body.append(f"<!-- origen: {a.fuente.name} | bloque {row['bloque']} -->")
            subheading=source_subheading(row["titulo_origen"],section["titulo"])
            if subheading: body.append("#"*subheading[0]+" "+subheading[1])
            for b in row["contenido"]:
                if b["kind"]=="figure" and b.get("media_ref") in media_files:
                    rel=Path("../..")/"04_Adjuntos"/"migracion"/a.parte/media_files[b["media_ref"]].name
                    body.append(f"![{b['text']}]({rel.as_posix()})")
                elif b["kind"]=="table": body.extend(render_table(b["text"],a.tablas_a_parrafos))
                elif b["kind"]=="figure": body.append(f"![{b['text']}]({b.get('media_ref','')})")
                elif b["kind"]=="paragraph": body.append(re.sub(r"\s*\{#.*\}\s*$","",str(b["text"])).strip())
                else: body.append(str(b["text"]))
        target=folder/section["archivo"]
        if target.exists():
            existing_fm,_=parse_frontmatter(target.read_text(encoding="utf-8-sig"))
            same_source=a.fuente.name in str(existing_fm.get("origen",""))
            if not (a.actualizar_migrados and existing_fm.get("estado")=="borrador" and same_source):
                print(f"No se sobrescribe: {target}",file=sys.stderr); return 7
        section_text="\n\n".join(body).strip()+"\n"
        try: source_origin=a.fuente.resolve().relative_to(ROOT.resolve()).as_posix()
        except ValueError: source_origin=a.fuente.name
        section_fm={"id":section["id"],"tipo":"seccion","parte":a.parte,"titulo":section["titulo"],"estado":"borrador","bases":[],"requisitos":sorted(set(re.findall(r"\b(?:RF-\d{3}|RNF-\d{2,3}|OP-\d{2})\b","\n".join(plain)))),"depende_de":[],"adjuntos":[],"jira":sorted(set(re.findall(r"\bOSS-\d+\b","\n".join(plain)))),"cifras":[],"origen":f"{source_origin}#bloques-{','.join(source_nums)}","actualizado":date.today().isoformat()}
        staged.append((target,frontmatter_text(section_fm)+section_text))
    master=next(folder.glob("sd-*.md")); master_raw=master.read_text(encoding="utf-8-sig"); master_fm,master_body=parse_frontmatter(master_raw)
    master_fm["secciones"]=[s["id"] for s in spec["secciones"]]; master_fm["actualizado"]=date.today().isoformat()
    table=["## Secciones","","| N | Sección | Archivo | Estado |","| :--- | :--- | :--- | :--- |"]
    table += [f"| {i} | {s['titulo']} | `{s['archivo']}` | Borrador migrado; revisar |" for i,s in enumerate(spec["secciones"],1)]
    table += ["", "### Nota de migración", "", "La estructura entregable sigue las cuatro secciones obligatorias del Comunicado 10. El contenido importado conserva su procedencia y permanece en estado borrador hasta revisión humana.", ""]
    master_body=re.sub(r"(?ms)^## Secciones\s*\n.*?(?=^## Trazabilidad con Jira\s*$)","\n".join(table)+"\n",master_body,count=1)
    staged.append((master,frontmatter_text(master_fm)+master_body))
    if media_files:
        if a.fuente.suffix.casefold()==".docx": extract_docx_media(a.fuente,media_refs,media_dest)
        else:
            media_dest.mkdir(parents=True,exist_ok=True)
            for ref,dest in media_files.items():
                if ref.startswith("data:image/"): dest.write_bytes(base64.b64decode(ref.split(",",1)[1]))
                else: dest.write_bytes((a.fuente.parent/ref).read_bytes())
    for target,text in staged: target.write_text(text,encoding="utf-8")
    print("\n".join(f"Creado: {p.relative_to(ROOT)}" for p,_ in staged)); return 0

if __name__=="__main__": raise SystemExit(main())
