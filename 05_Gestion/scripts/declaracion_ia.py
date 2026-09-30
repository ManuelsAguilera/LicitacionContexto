#!/usr/bin/env python3
"""Consolida el registro de uso de IA de una parte para revisión y A-6."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path
from artefactos import ROOT

LEVELS={"Ninguno","Bajo","Medio","Alto"}

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("--parte",required=True,help="T7-NN"); ap.add_argument("--salida",type=Path)
    a=ap.parse_args()
    if not re.fullmatch(r"T7-\d{2}",a.parte): ap.error("--parte debe ser T7-NN")
    path=ROOT/"05_Gestion"/"ia"/"registro.json"; data=json.loads(path.read_text(encoding="utf-8"))
    rows=[r for r in data.get("registros",[]) if r.get("artefacto")==a.parte or str(r.get("artefacto","")).startswith(a.parte+"-") or (str(r.get("artefacto","")).startswith("ADJ-") and r.get("parte")==a.parte)]
    errors=[]; seen=set()
    for row in rows:
        aid=row.get("artefacto")
        if aid in seen: errors.append(f"Registro duplicado: {aid}")
        seen.add(aid)
        for field in ("herramienta","finalidad","nivel_texto","nivel_diagramas","verificador","comprobaciones","fecha"):
            if field not in row or row[field] in (None,""): errors.append(f"{aid}: falta {field}")
        for key in ("nivel_texto","nivel_diagramas"):
            if row.get(key) not in LEVELS: errors.append(f"{aid}: nivel inválido en {key}")
    lines=[f"# Declaración de uso de IA · {a.parte}","","Consolidado desde `05_Gestion/ia/registro.json`. Verificar y transcribir al Formulario A-6; este reporte no lo reemplaza.","","| Artefacto | Herramienta | Finalidad | Texto | Diagramas | Verificador / comprobaciones | Fecha |","|---|---|---|---|---|---|---|"]
    for r in rows:
        checks="; ".join(r.get("comprobaciones",[])) or "—"
        values=(r.get("artefacto",""),r.get("herramienta",""),r.get("finalidad",""),r.get("nivel_texto",""),r.get("nivel_diagramas",""),str(r.get("verificador",""))+": "+checks,r.get("fecha",""))
        lines.append("| "+" | ".join(str(x).replace("|","\\|").replace("\n"," ") for x in values)+" |")
    lines += ["",f"Registros: {len(rows)} · Errores de forma: {len(errors)}",""]
    if not rows: lines.append("No hay registros declarados todavía; ausencia de registro no significa uso Ninguno.")
    if errors: lines += ["## Errores",*("- "+e for e in errors)]
    out="\n".join(lines)+"\n"
    if a.salida: a.salida.write_text(out,encoding="utf-8")
    print(out,end=""); return 1 if errors else 0

if __name__=="__main__": raise SystemExit(main())
