#!/usr/bin/env python3
"""Genera el tablero Markdown de estado y pendientes de cada subdocumento."""
from __future__ import annotations
import argparse, re
from pathlib import Path
from artefactos import ROOT, parse_frontmatter, words

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--dry-run",action="store_true"); ap.add_argument("--salida",type=Path,default=ROOT/"05_Gestion"/"ESTADO.md"); a=ap.parse_args()
    lines=["# Estado de artefactos", "", "Generado desde los maestros y sus archivos de sección. `revisado` y `congelado` requieren decisión humana.", "", "| Parte / artefacto | Estado | Palabras | Requisitos | Adjuntos pendientes |", "|---|---|---:|---:|---:|"]
    prop=ROOT/"02_Propuesta"
    import json
    reg=ROOT/"05_Gestion"/"adjuntos.json"
    records={x["id"]:x for x in json.loads(reg.read_text(encoding="utf-8"))} if reg.exists() else {}
    for folder in sorted(prop.glob("sd-[0-9][0-9]_*")):
        master=next(folder.glob("sd-*.md"),None)
        if not master: continue
        raw=master.read_text(encoding="utf-8-sig"); fm,body=parse_frontmatter(raw); part=f"T7-{int(folder.name[3:5]):02d}"
        rows=re.findall(r"\|\s*(\d+)\s*\|\s*([^|]+)\|\s*`?(sd-\d+_s\d+_[^`|]+\.md)`?",body)
        missing=[row for row in rows if not (folder/row[2].strip()).exists()]
        pending=sum(1 for aid in fm.get("adjuntos",[]) if aid in records and not (ROOT/records[aid]["ruta"]).exists())
        lines.append(f"| `{part}` | {'incompleta: '+str(len(missing))+'/'+str(len(rows))+' secciones ausentes' if missing else fm.get('estado','sin estado')} | {words(body)} | {len(fm.get('requisitos',[]))} | {pending} |")
        for number,title,filename in rows:
            filename=filename.strip(); p=folder/filename; sid=f"{part}-{int(part[3:])}.{int(number)}"
            if p.exists():
                text=p.read_text(encoding="utf-8-sig"); sfm,content=parse_frontmatter(text)
                req_count=len(sfm.get("requisitos",[])) if isinstance(sfm.get("requisitos"),list) else 0
                lines.append(f"| `{sid}` · {title.strip()} | {sfm.get('estado','sin metadatos')} | {words(content)} | {req_count} | 0 |")
            else: lines.append(f"| `{sid}` · {title.strip()} | vacio (archivo ausente) | 0 | 0 | 0 |")
    output="\n".join(lines)+"\n"
    if not a.dry_run: a.salida.write_text(output,encoding="utf-8")
    print(output,end=""); return 0
if __name__=="__main__": raise SystemExit(main())
