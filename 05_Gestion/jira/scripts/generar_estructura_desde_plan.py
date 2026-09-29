"""Genera los artefactos de la estructura FINAL de Jira (3 niveles) a partir del
plan de reestructuración, sin tocar los artefactos históricos de la importacion
original (estructura plana de 2 niveles).

Genera:
  jira_import_payload_estructurado.json   - 8 agrupadoras > 34 historias > 77 subtareas
  Jira_UserStoryMapping_Estructurado.csv  - 119 filas, con clave Jira y nivel

El plan (restructuracion_2026-09-29_plan.json) queda como unica fuente de verdad.
"""

import csv
import json
import sys
from rutas import RUTA_MAPPING_ESTRUCTURADO, RUTA_PAYLOAD_ESTRUCTURADO, RUTA_PLAN

sys.stdout.reconfigure(encoding="utf-8")

PLAN = RUTA_PLAN
OUT_JSON = RUTA_PAYLOAD_ESTRUCTURADO
OUT_CSV = RUTA_MAPPING_ESTRUCTURADO

CLOUD_ID = "b662438c-9aba-4643-a083-82a2fde025f3"
PROJECT_KEY = "OSS"
REPORTER = "609a0d9f5d67f20069ae5a6e"

TIPO_AGRUPADORA = "Epicas"
TIPO_HISTORIA = "Historia"
TIPO_SUBTAREA = "Subtarea"

with open(PLAN, encoding="utf-8") as fh:
    plan = json.load(fh)

secciones = {s["clave"]: s for s in plan["secciones"]}
subtareas_por_seccion = {}
for t in plan["subtareas"]:
    subtareas_por_seccion.setdefault(t["seccion"], []).append(t)

capitulos = []
filas = []
n = 0
dependencias = {}

for a in plan["agrupadoras"]:
    capitulo = {
        "n": n + 1,
        "clave": a["clave"],
        "issueType": TIPO_AGRUPADORA,
        "summary": a["resumen"],
        "description": a["descripcion"],
        "etiquetas": a["etiquetas"],
        "historias": [],
    }
    n += 1
    filas.append(
        [
            str(n),
            a["resumen"],
            a["descripcion"],
            TIPO_AGRUPADORA,
            PROJECT_KEY,
            "Medio",
            a["clave"],
            "agrupadora",
            "",
            "|".join(a["etiquetas"]),
            "",
        ]
    )

    for clave_sec in a["secciones"]:
        s = secciones[clave_sec]
        historia = {
            "n": n + 1,
            "clave": s["clave"],
            "issueType": TIPO_HISTORIA,
            "summary": s["resumen"],
            "description": s["descripcion"],
            "etiquetas": s["etiquetas"],
            "subtareas": [],
        }
        n += 1
        filas.append(
            [
                str(n),
                s["resumen"],
                s["descripcion"],
                TIPO_HISTORIA,
                PROJECT_KEY,
                "Medio",
                s["clave"],
                "historia",
                a["clave"],
                "|".join(s["etiquetas"]),
                "",
            ]
        )

        for t in subtareas_por_seccion.get(s["clave"], []):
            sub = {
                "n": n + 1,
                "clave": t["nuevaClave"],
                "issueType": TIPO_SUBTAREA,
                "summary": t["resumen"],
                "description": t["descripcion"],
                "etiquetas": t["etiquetas"],
                "tipoOriginal": t["tipoOriginal"],
            }
            if t.get("asignado"):
                sub["asignado"] = t["asignado"]
            if t.get("bloqueadaPor"):
                sub["bloqueadaPor"] = t["bloqueadaPor"]
                dependencias[t["nuevaClave"]] = t["bloqueadaPor"]
            n += 1
            historia["subtareas"].append(sub)
            filas.append(
                [
                    str(n),
                    t["resumen"],
                    t["descripcion"],
                    TIPO_SUBTAREA,
                    PROJECT_KEY,
                    "Medio",
                    t["nuevaClave"],
                    "subtarea",
                    s["clave"],
                    "|".join(t["etiquetas"]),
                    "|".join(t.get("bloqueadaPor", [])),
                ]
            )
        capitulo["historias"].append(historia)
    capitulos.append(capitulo)

payload = {
    "cloudId": CLOUD_ID,
    "projectKey": PROJECT_KEY,
    "reporterAccountId": REPORTER,
    "estructura": "3 niveles: Epicas (capitulo) > Historia (seccion) > Subtarea",
    "capitulos": capitulos,
}

with open(OUT_JSON, "w", encoding="utf-8") as fh:
    json.dump(payload, fh, ensure_ascii=False, indent=2)

cabecera = [
    "ID de incidencia",
    "Resumen",
    "Descripción",
    "Tipo de Incidencia",
    "Clave del proyecto",
    "Prioridad",
    "Clave Jira",
    "Nivel",
    "Historia padre",
    "Etiquetas",
    "Bloqueada por",
]
with open(OUT_CSV, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(cabecera)
    w.writerows(filas)

n_hist = sum(len(c["historias"]) for c in capitulos)
n_sub = sum(len(h["subtareas"]) for c in capitulos for h in c["historias"])
print("estructura generada desde el plan")
print("  capitulos (Epicas)   :", len(capitulos))
print("  historias             :", n_hist)
print("  subtareas             :", n_sub)
print("  incidencias totales   :", len(filas))
print("  subtareas con dependencia:", len(dependencias))
print("archivos:", OUT_JSON, "|", OUT_CSV)
