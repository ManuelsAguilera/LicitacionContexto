#!/usr/bin/env python3
"""Añade metadatos inferibles a maestros/secciones y registra adjuntos esperados."""
from __future__ import annotations
import argparse, json, re
from datetime import date
from pathlib import Path
from artefactos import ROOT, frontmatter_text, parse_frontmatter, status_for

SECTION_ROW=re.compile(r"\|\s*(\d+)\s*\|\s*([^|]+)\|\s*`?(sd-\d+_s\d+_[^`|]+\.md)`?")
ATTACHMENT_RE=re.compile(r"(?:`)?((?:adj|diag|form)-[A-Za-z0-9_.-]+\.[A-Za-z0-9]+)")

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--dry-run",action="store_true"); ap.add_argument("--parte",help="Limita a T7-NN"); a=ap.parse_args()
    prop=ROOT/"02_Propuesta"; folders=sorted(p for p in prop.glob("sd-[0-9][0-9]_*" ) if p.is_dir())
    if a.parte: folders=[p for p in folders if p.name.startswith("sd-"+a.parte[3:]+"_")]
    proposals=[]; registry=[]
    registry_path=ROOT/"05_Gestion"/"adjuntos.json"
    previous=json.loads(registry_path.read_text(encoding="utf-8")) if registry_path.exists() else []
    stable_ids={(x["parte"],x["nombre"]):x["id"] for x in previous}
    next_adj=max((int(x["id"].split("-")[1]) for x in previous if re.fullmatch(r"ADJ-\d{3}",x.get("id",""))),default=0)+1
    for folder in folders:
        part_num=int(folder.name[3:5]); part=f"T7-{part_num:02d}"
        master=next(folder.glob("sd-*.md"),None)
        if not master: continue
        raw=master.read_text(encoding="utf-8-sig"); old,body=parse_frontmatter(raw)
        sections=[]
        for match in SECTION_ROW.finditer(body):
            n,title,filename=match.groups(); sid=f"{part}-{part_num}.{int(n)}"; sections.append(sid)
        attachments=[]
        for filename in ATTACHMENT_RE.findall(body):
            aid=stable_ids.get((part,filename))
            if aid is None: aid=f"ADJ-{next_adj:03d}"; next_adj+=1
            attachments.append(aid); registry.append({"id":aid,"parte":part,"nombre":filename,"ruta":str((folder/filename).relative_to(ROOT)).replace("\\","/"),"declarado_en":str(master.relative_to(ROOT)).replace("\\","/"),"existe":(folder/filename).exists()})
        data={"id":part,"tipo":"parte","parte":part,"titulo":(re.search(r"^#\s+Subdocumento\s+\d+\s*[—-]\s*(.+)$",body,re.M).group(1).strip() if re.search(r"^#\s+Subdocumento\s+\d+\s*[—-]\s*(.+)$",body,re.M) else master.stem),"estado":old.get("estado",status_for(body)),"bases":old.get("bases",[]),"requisitos":sorted(set(re.findall(r"\b(?:RF-\d{3}|RNF-\d{2,3}|OP-\d{2})\b",body))),"depende_de":old.get("depende_de",[]),"adjuntos":attachments,"jira":sorted(set(re.findall(r"\bOSS-\d+\b",body))),"cifras":old.get("cifras",[]),"secciones":sections,"actualizado":date.today().isoformat()}
        if not old:
            proposals.append((master,frontmatter_text(data)+body))
        for secfile in sorted(p for p in folder.glob("sd-*.md") if re.match(r"sd-\d{2}_s\d+_.*\.md$", p.name)):
            secraw=secfile.read_text(encoding="utf-8-sig"); secold,secbody=parse_frontmatter(secraw)
            if secold: continue
            sm=re.search(r"_s(\d+)_",secfile.name); n=int(sm.group(1)) if sm else 1
            heading=re.search(r"^#{1,6}\s+(.+)$",secbody,re.M); title=heading.group(1).strip() if heading else secfile.stem
            sid=f"{part}-{part_num}.{n}"
            sdata={"id":sid,"tipo":"seccion","parte":part,"titulo":title,"estado":status_for(secbody),"bases":[],"requisitos":sorted(set(re.findall(r"\b(?:RF-\d{3}|RNF-\d{2,3}|OP-\d{2})\b",secbody))),"depende_de":[],"adjuntos":[],"jira":sorted(set(re.findall(r"\bOSS-\d+\b",secbody))),"cifras":[],"origen":"","actualizado":date.today().isoformat()}
            proposals.append((secfile,frontmatter_text(sdata)+secbody))
    print(f"{len(proposals)} archivo(s) recibirían frontmatter; {len(registry)} adjunto(s) declarados, {sum(not x['existe'] for x in registry)} no existen aún.")
    for path,new in proposals: print(f"{path.relative_to(ROOT)}: {len(new.splitlines())} líneas resultantes")
    if a.dry_run: return 0
    for path,new in proposals: path.write_text(new,encoding="utf-8")
    registry_path.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"Registro escrito: {registry_path.relative_to(ROOT)}")
    return 0

if __name__=="__main__": raise SystemExit(main())
