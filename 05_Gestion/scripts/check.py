#!/usr/bin/env python3
"""Valida metadatos, trazabilidad y referencias locales de los artefactos."""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path
from artefactos import ROOT, parse_frontmatter, words

REQUIRED={"id","tipo","parte","titulo","estado","bases","requisitos","depende_de","adjuntos","jira","cifras","actualizado"}
REQ_RE=re.compile(r"\b(?:RF-\d{3}|RNF-\d{2,3}|OP-\d{2})\b")

def read_ids_from_catalog():
    p=ROOT/"01_Requerimientos"/"md"/"catalogo-de-requerimientos-depurado-v30.md"
    return set(REQ_RE.findall(p.read_text(encoding="utf-8-sig"))) if p.exists() else set()

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--parte",action="append"); ap.add_argument("--salida",type=Path); ap.add_argument("--dry-run",action="store_true"); a=ap.parse_args()
    errors=[]; warnings=[]; files=[]; ids={}; all_ids=set(); registry_path=ROOT/"05_Gestion"/"adjuntos.json"; dependencies=[]; catalog_ids=read_ids_from_catalog()
    for candidate in (ROOT/"02_Propuesta").rglob("*.md"):
        if candidate.name=="indice.md": continue
        candidate_fm,_=parse_frontmatter(candidate.read_text(encoding="utf-8-sig"))
        if candidate_fm.get("id"): all_ids.add(candidate_fm["id"])
    registry={x["id"]:x for x in json.loads(registry_path.read_text(encoding="utf-8"))} if registry_path.exists() else {}
    ai_path=ROOT/"05_Gestion"/"ia"/"registro.json"
    ai_records=json.loads(ai_path.read_text(encoding="utf-8")).get("registros",[]) if ai_path.exists() else []
    registered_ai={x.get("artefacto") for x in ai_records}
    for p in (ROOT/"02_Propuesta").rglob("*.md"):
        if p.name=="indice.md": continue
        if a.parte and not any(p.parts[-2].startswith("sd-"+x[3:]+"_") for x in a.parte): continue
        files.append(p); text=p.read_text(encoding="utf-8-sig"); fm,body=parse_frontmatter(text)
        rel=p.relative_to(ROOT).as_posix()
        if not fm: errors.append(f"{rel}: falta frontmatter"); continue
        for key in REQUIRED:
            if key not in fm: errors.append(f"{rel}: falta campo {key}")
        aid=fm.get("id")
        if aid in ids: errors.append(f"ID duplicado {aid}: {ids[aid]} y {rel}")
        elif aid: ids[aid]=rel
        if fm.get("tipo")=="parte":
            part_num=int(fm.get("parte","T7-00")[3:])
            refs=p.parent/f"sd-{part_num:02d}_referencias.md"
            if not refs.is_file(): warnings.append(f"{rel}: falta la sección final obligatoria Referencias ({refs.name})")
            expected=list(fm.get("secciones",[])) + (fm.get("adjuntos",[]) if isinstance(fm.get("adjuntos",[]),list) else [])
            for expected_id in expected:
                if expected_id not in registered_ai: warnings.append(f"{rel}: falta registro de uso de IA para {expected_id}")
        if fm.get("estado") in {"revisado","congelado"}:
            review=fm.get("revision_humana",{})
            if not isinstance(review,dict) or not review.get("revisor") or not review.get("evidencia"):
                errors.append(f"{rel}: estado {fm.get('estado')} sin revision_humana.revisor/evidencia")
        elif fm.get("estado") not in {"vacio","esqueleto","borrador"}: errors.append(f"{rel}: estado inválido {fm.get('estado')}")
        for dep in fm.get("depende_de",[]) if isinstance(fm.get("depende_de"),list) else []: dependencies.append((rel,dep))
        for adj in fm.get("adjuntos",[]) if isinstance(fm.get("adjuntos"),list) else []:
            record=registry.get(adj)
            if not record: errors.append(f"{rel}: adjunto no registrado: {adj}")
            elif not (ROOT/record["ruta"]).exists(): warnings.append(f"{rel}: adjunto declarado pendiente: {record['ruta']}")
        for key in REQ_RE.findall(body):
            if key not in catalog_ids: warnings.append(f"{rel}: requisito no encontrado en catálogo: {key}")
        for href in re.findall(r"\]\(([^)]+)\)",body):
            if href.startswith(("http://","https://","mailto:","#","data:")): continue
            target=(p.parent/href.split("#",1)[0]).resolve()
            if not target.exists(): warnings.append(f"{rel}: enlace local no resuelto: {href}")
        if re.search(r"\bp[aá]gina\s+\d+\b",body,re.I): warnings.append(f"{rel}: revisar referencia de página fija a otro documento")
        if re.search(r"\bTODO\b|\[VERIFICAR\]",body,re.I): warnings.append(f"{rel}: contiene marcador TODO/[VERIFICAR]")
    for rel,dep in dependencies:
        if dep not in all_ids: errors.append(f"{rel}: depende_de no resuelto: {dep}")
    catalog=read_ids_from_catalog(); covered=set()
    for p in files:
        fm,body=parse_frontmatter(p.read_text(encoding="utf-8-sig")); covered.update(fm.get("requisitos",[]) if isinstance(fm.get("requisitos"),list) else []); covered.update(REQ_RE.findall(body))
    missing=sorted(catalog-covered) if not a.parte else []
    extra=sorted(covered-catalog)
    for x in extra: warnings.append(f"ID de requerimiento fuera de catálogo: {x}")
    plan_ids=set()
    for directory in (ROOT/"05_Gestion"/"jira"/"plan",ROOT/"05_Gestion"/"jira"/"mapeo"):
        for p in directory.glob("*.*"):
            try: plan_ids.update(re.findall(r"\bOSS-\d+\b",p.read_text(encoding="utf-8-sig",errors="ignore")))
            except OSError: pass
    for p in files:
        fm,_=parse_frontmatter(p.read_text(encoding="utf-8-sig"))
        for jira in fm.get("jira",[]) if isinstance(fm.get("jira"),list) else []:
            if jira not in plan_ids: warnings.append(f"{p.relative_to(ROOT)}: Jira no encontrado en plan/mapeo: {jira}")
    data_file=ROOT/"02_Propuesta"/"datos.yml"; data_text=data_file.read_text(encoding="utf-8-sig") if data_file.exists() else ""
    data_values=set(re.findall(r"^\s+valor:\s*[\"']?([^\"'\r\n]+)",data_text,re.M)); data_keys=set(re.findall(r"^([a-z][a-z0-9_]+):\s*$",data_text,re.M))
    exception_file=ROOT/"05_Gestion"/"validacion"/"excepciones_cifras.txt"
    exceptions=[x.strip() for x in exception_file.read_text(encoding="utf-8-sig").splitlines() if x.strip() and not x.lstrip().startswith("#")] if exception_file.exists() else []
    for p in files:
        fm,body=parse_frontmatter(p.read_text(encoding="utf-8-sig"))
        for key in fm.get("cifras",[]) if isinstance(fm.get("cifras"),list) else []:
            if key not in data_keys: warnings.append(f"{p.relative_to(ROOT)}: clave de cifra no registrada en datos.yml: {key}")
        if fm.get("tipo")=="seccion":
            for line_no,line in enumerate(body.splitlines(),1):
                if line.lstrip().startswith("#") or REQ_RE.search(line) or re.search(r"\bOSS-\d+\b|\bT7-\d{2}(?:-[\d.]+)?\b|\b20\d{2}-\d{2}-\d{2}\b",line): continue
                for number in re.findall(r"(?<![\w-])\d+(?:[.,]\d+)?%?",line):
                    bare=number.rstrip("%").replace(",",".")
                    if number in data_values or bare in data_values or any(re.search(pattern,line) for pattern in exceptions): continue
                    if re.search(r"\bp(?:á|a)g(?:ina)?\.?\s*"+re.escape(number),line,re.I): continue
                    warnings.append(f"{p.relative_to(ROOT)}:{line_no}: cifra no localizada en datos.yml (revisar): {number}")
    report=[f"Artefactos revisados: {len(files)}",f"Errores: {len(errors)}",f"Avisos: {len(warnings)}",f"Requisitos catálogo: {len(catalog)}; cubiertos por referencia/texto: {len(catalog & covered)}; sin cobertura: {len(missing)}" if not a.parte else f"Requisitos catálogo: {len(catalog)}; cobertura global omitida (validación parcial: {', '.join(a.parte)})"]
    report += ["", "ERRORES", *(["- "+x for x in errors] or ["- ninguno"]), "", "AVISOS", *(["- "+x for x in warnings] or ["- ninguno"]), "", "REQUISITOS SIN COBERTURA", *(["- "+x for x in missing] or ["- ninguno"])]
    output="\n".join(report)+"\n"
    if a.salida and not a.dry_run: a.salida.write_text(output,encoding="utf-8")
    print(output,end="")
    return 1 if errors else 0

if __name__=="__main__": raise SystemExit(main())
