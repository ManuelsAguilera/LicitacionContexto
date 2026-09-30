#!/usr/bin/env python3
"""Propone mapeo conservador de documento completo a artefactos Markdown."""
from __future__ import annotations
import argparse, hashlib, json, re, sys, zipfile
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
    active=False; chunks=[]; current=None; outside=[]
    for index,b in enumerate(blocks,1):
        title=b["text"].strip()
        if b["kind"]=="heading" and start.search(title):
            active=True; current=None; continue
        if b["kind"]=="heading" and active and end.search(title):
            if current: chunks.append(current)
            active=False; current=None; continue
        if not active:
            outside.append({"bloque_origen":index,**b}); continue
        if b["kind"]=="heading":
            if current: chunks.append(current)
            current={"heading":title,"blocks":[]}
        else:
            if current is None: current={"heading":"(texto previo al primer encabezado)","blocks":[]}
            current["blocks"].append(b)
    if current: chunks.append(current)
    return chunks,outside

def suggested(rows, rules):
    by_prefix={x["origen"]:x for x in rules}
    for row in rows:
        m=re.match(r"^\s*(\d+(?:\.\d+)+)\b",row["titulo_origen"])
        if not m:
            row.update({"seccion_sugerida":"","revision":"sin_correspondencia","motivo":"sin numeración reconocible"}); continue
        num=m.group(1); base=".".join(num.split(".")[:2]); rule=by_prefix.get(base)
        if not rule:
            row.update({"seccion_sugerida":"","revision":"sin_correspondencia","motivo":"sin regla de asignación"}); continue
        row.update({"seccion_sugerida":rule["destino"],"revision":"sugerida_revisar","motivo":rule["motivo"]})
    return rows

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--fuente",type=Path,required=True); ap.add_argument("--parte",required=True); ap.add_argument("--dry-run",action="store_true"); ap.add_argument("--mapa-aprobado",type=Path); ap.add_argument("--reporte",type=Path); ap.add_argument("--plantilla-mapa",type=Path,help="Escribe asignaciones sugeridas sin declararlas aprobadas")
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
        collisions=[p for p in media_files.values() if p.exists()]
        if collisions: print(f"No se sobrescriben recursos existentes: {collisions}",file=sys.stderr); return 8
    else:
        media_files={}
        for ref in media_refs:
            if not ref or ref.startswith(("http:","https:","data:")): continue
            source_media=(a.fuente.parent/ref).resolve()
            if not source_media.is_file():
                print(f"Figura no localizada: {ref}; no se escribe ningún artefacto.",file=sys.stderr); return 9
            dest=media_dest/source_media.name
            if dest.exists(): print(f"No se sobrescribe recurso existente: {dest}",file=sys.stderr); return 8
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
        body=[f"# {heading_number} {section['titulo']}","", "<!-- contenido migrado sin edición; revisar la jerarquía de títulos -->", ""]
        for row in chosen:
            body += [f"<!-- origen: {a.fuente.name} | bloque {row['bloque']} -->",f"### {row['titulo_origen']}"]
            for b in row["contenido"]:
                if b["kind"]=="figure" and b.get("media_ref") in media_files:
                    rel=Path("../..")/"04_Adjuntos"/"migracion"/a.parte/media_files[b["media_ref"]].name; body += [f"![{b['text']}]({rel.as_posix()})"]
                elif b["kind"]=="table":
                    table=[ [cell.strip() for cell in line.split("|")] for line in str(b["text"]).splitlines() if line.strip() ]
                    if table:
                        width=max(map(len,table)); table=[row+([""]*(width-len(row))) for row in table]
                        body += ["| "+" | ".join(table[0])+" |", "| "+" | ".join(["---"]*width)+" |"]+["| "+" | ".join(row)+" |" for row in table[1:]]
                else: body.append(str(b["text"]))
        target=folder/section["archivo"]
        if target.exists(): print(f"No se sobrescribe: {target}",file=sys.stderr); return 7
        section_text="\n\n".join(body).strip()+"\n"
        section_fm={"id":section["id"],"tipo":"seccion","parte":a.parte,"titulo":section["titulo"],"estado":"borrador","bases":[],"requisitos":sorted(set(re.findall(r"\b(?:RF-\d{3}|RNF-\d{2,3}|OP-\d{2})\b","\n".join(plain)))),"depende_de":[],"adjuntos":[],"jira":sorted(set(re.findall(r"\bOSS-\d+\b","\n".join(plain)))),"cifras":[],"origen":f"{a.fuente.relative_to(ROOT).as_posix()}#bloques-{','.join(source_nums)}","actualizado":date.today().isoformat()}
        staged.append((target,frontmatter_text(section_fm)+section_text))
    master=next(folder.glob("sd-*.md")); master_raw=master.read_text(encoding="utf-8-sig"); master_fm,master_body=parse_frontmatter(master_raw)
    master_fm["secciones"]=[s["id"] for s in spec["secciones"]]; master_fm["actualizado"]=date.today().isoformat()
    table=["## Secciones","","| N | Sección | Archivo | Estado |","| :--- | :--- | :--- | :--- |"]
    table += [f"| {i} | {s['titulo']} | `{s['archivo']}` | Borrador migrado; revisar |" for i,s in enumerate(spec["secciones"],1)]
    master_body=re.sub(r"(?ms)^## Secciones\s*\n.*?(?=^### |^## (?!Secciones)|\Z)","\n".join(table)+"\n\n",master_body,count=1)
    staged.append((master,frontmatter_text(master_fm)+master_body))
    if media_files:
        if a.fuente.suffix.casefold()==".docx": extract_docx_media(a.fuente,media_refs,media_dest)
        else:
            media_dest.mkdir(parents=True,exist_ok=True)
            for ref,dest in media_files.items(): dest.write_bytes((a.fuente.parent/ref).read_bytes())
    for target,text in staged: target.write_text(text,encoding="utf-8")
    print("\n".join(f"Creado: {p.relative_to(ROOT)}" for p,_ in staged)); return 0

if __name__=="__main__": raise SystemExit(main())
