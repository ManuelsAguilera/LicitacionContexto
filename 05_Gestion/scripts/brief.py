#!/usr/bin/env python3
"""Imprime el contexto compacto registrado para una parte, sección o adjunto."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
from artefactos import ROOT, parse_frontmatter

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("id"); ap.add_argument("--max-palabras",type=int,default=1800); a=ap.parse_args()
    registry_path=ROOT/"05_Gestion"/"adjuntos.json"; registry=json.loads(registry_path.read_text(encoding="utf-8")) if registry_path.exists() else []
    target=None
    for p in (ROOT/"02_Propuesta").rglob("*.md"):
        fm,_=parse_frontmatter(p.read_text(encoding="utf-8-sig"))
        if fm.get("id")==a.id: target=(p,fm); break
    if target is None:
        print(f"No se encontró artefacto Markdown con ID {a.id}"); return 2
    p,fm=target; _,body=parse_frontmatter(p.read_text(encoding="utf-8-sig")); parts=[]
    parts += [f"# {fm.get('id')} · {fm.get('titulo')}",f"Estado: {fm.get('estado')}",f"Fuente: {p.relative_to(ROOT).as_posix()}","", "## Bases citadas", ", ".join(fm.get("bases",[])) or "Sin citas declaradas.","", "## Requisitos", ", ".join(fm.get("requisitos",[])) or "Sin mapeo explícito.","", "## Dependencias", ", ".join(fm.get("depende_de",[])) or "Ninguna declarada.","", "## Jira", ", ".join(fm.get("jira",[])) or "Sin asociación.","", "## Cifras", ", ".join(fm.get("cifras",[])) or "Sin claves declaradas.","", "## Contenido",body.strip()]
    for aid in fm.get("adjuntos",[]) if isinstance(fm.get("adjuntos"),list) else []:
        item=next((x for x in registry if x["id"]==aid),None)
        if item: parts += ["",f"Adjunto {aid}: {item['nombre']} — {'presente' if item['existe'] else 'pendiente'}"]
    result="\n".join(parts); tokens=re.findall(r"\S+",result)
    if len(tokens)>a.max_palabras: result=" ".join(tokens[:a.max_palabras])+"\n[Contexto truncado por límite]"
    print(result); return 0
if __name__=="__main__": raise SystemExit(main())
