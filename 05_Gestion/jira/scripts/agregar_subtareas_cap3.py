"""Registra en el plan de reestructuración las 13 Subtareas nuevas del capítulo 3
creadas en Jira (OSS-237..OSS-249) y regenera el CSV de mapeo y el JSON de etiquetas.

Idempotente: si ya estan registradas, no las duplica.
"""

import json
import sys
from rutas import RUTA_ETIQUETAS, RUTA_MAPEO_CSV, RUTA_PLAN

sys.stdout.reconfigure(encoding="utf-8")

PLAN = RUTA_PLAN
CSV = RUTA_MAPEO_CSV
ETIQUETAS = RUTA_ETIQUETAS

MANUEL = "609a0d9f5d67f20069ae5a6e"
VICENTE = "712020:a9288d98-996a-4d37-9635-d70d8d5dd75d"
MARTIN = "712020:4ca60652-625c-4b3b-b333-fc7430cdd61f"

SEC_INTRO = "Sección del informe: 3. Introducción"
SEC_ALCANCE = "Sección del informe: 3.2 Alcance"
SEC_ESQUEMA = "Sección del informe: 3.3 Esquema de solución"

NUEVAS = [
    {
        "nuevaClave": "OSS-236",
        "seccion": "OSS-86",
        "resumen": "Revisar objetivos, redacción, y alineación con proyecto",
        "descripcion": SEC_ALCANCE,
        "tipoOriginal": "Tareas",
        "etiquetas": ["cap-3", "sec-3-2", "tipo-tarea"],
        "asignado": VICENTE,
    },
    {
        "nuevaClave": "OSS-237",
        "seccion": "OSS-84",
        "resumen": "Verificar que el capítulo 3 responda las 11 preguntas del profesor",
        "descripcion": SEC_INTRO,
        "tipoOriginal": "Tareas",
        "etiquetas": ["cap-3", "sec-3", "tipo-tarea"],
        "asignado": MANUEL,
    },
    {
        "nuevaClave": "OSS-238",
        "seccion": "OSS-86",
        "resumen": "Contrastar los requisitos técnicos (RT) con los requisitos del proyecto (RF/RNF)",
        "descripcion": SEC_ALCANCE,
        "tipoOriginal": "Tareas",
        "etiquetas": ["cap-3", "sec-3-2", "tipo-tarea"],
    },
    {
        "nuevaClave": "OSS-239",
        "seccion": "OSS-86",
        "resumen": "Spike: revisar el PMBOK para entradas y salidas de proceso",
        "descripcion": SEC_ALCANCE,
        "tipoOriginal": "Spikes",
        "etiquetas": ["cap-3", "sec-3-2", "tipo-spike"],
        "asignado": VICENTE,
    },
    {
        "nuevaClave": "OSS-240",
        "seccion": "OSS-86",
        "resumen": "Spike: investigar un enunciado de alcance",
        "descripcion": SEC_ALCANCE,
        "tipoOriginal": "Spikes",
        "etiquetas": ["cap-3", "sec-3-2", "tipo-spike"],
        "asignado": MARTIN,
    },
    {
        "nuevaClave": "OSS-241",
        "seccion": "OSS-86",
        "resumen": "Definir la separación y los criterios de asignación de alcance entre la Etapa 1 y la Etapa 2 (Art. 17)",
        "descripcion": SEC_ALCANCE
        + "\nCubre: Bases_Administrativas.md:2089 — Alcance de la Etapa 1 y de la Etapa 2, con separación explícita y criterios de asignación entre ambas.",
        "tipoOriginal": "Tareas",
        "etiquetas": ["cap-3", "sec-3-2", "tipo-tarea"],
    },
    {
        "nuevaClave": "OSS-242",
        "seccion": "OSS-86",
        "resumen": "Consolidar el catálogo de requerimientos funcionales y no funcionales, priorizado y trazable (RF/RNF ↔ T-12)",
        "descripcion": SEC_ALCANCE
        + "\nCubre: Bases_Administrativas.md:2093 — Catálogo de requerimientos funcionales y no funcionales, priorizado y trazable.",
        "tipoOriginal": "Trabajo Tecnico",
        "etiquetas": ["cap-3", "sec-3-2", "tipo-tt"],
    },
    {
        "nuevaClave": "OSS-243",
        "seccion": "OSS-86",
        "resumen": "Validar los supuestos, exclusiones, requisitos y restricciones del alcance",
        "descripcion": SEC_ALCANCE + "\nSe ejecuta al cerrar el resto del capítulo 3.",
        "tipoOriginal": "Tareas",
        "etiquetas": ["cap-3", "sec-3-2", "tipo-tarea"],
        "bloqueadaPor": [
            "OSS-237",
            "OSS-238",
            "OSS-239",
            "OSS-240",
            "OSS-241",
            "OSS-242",
            "OSS-244",
            "OSS-245",
            "OSS-246",
            "OSS-247",
            "OSS-248",
            "OSS-249",
        ],
    },
    {
        "nuevaClave": "OSS-244",
        "seccion": "OSS-86",
        "resumen": "Definir los criterios de aceptación del alcance comprometido",
        "descripcion": SEC_ALCANCE
        + "\nCubre: Bases_Administrativas.md:2097 — Criterios de aceptación del alcance comprometido.",
        "tipoOriginal": "Tareas",
        "etiquetas": ["cap-3", "sec-3-2", "tipo-tarea"],
    },
    {
        "nuevaClave": "OSS-245",
        "seccion": "OSS-86",
        "resumen": "Definir la estrategia para obtener el apoyo de los grupos de interés clave",
        "descripcion": SEC_ALCANCE
        + "\nCubre: Bases_Administrativas.md:2095 — Estrategia para obtener el apoyo de los grupos de interés clave.",
        "tipoOriginal": "Tareas",
        "etiquetas": ["cap-3", "sec-3-2", "tipo-tarea"],
    },
    {
        "nuevaClave": "OSS-246",
        "seccion": "OSS-86",
        "resumen": "Definir la frontera entre los dos negocios (retail y crédito fiscalizado) antes de cualquier vista unificada",
        "descripcion": SEC_ALCANCE
        + "\nCubre: Caso_09_Cadena_Multitienda.md:988 y :997 — que la frontera entre los dos negocios esté definida antes que cualquier vista unificada.",
        "tipoOriginal": "Tareas",
        "etiquetas": ["cap-3", "sec-3-2", "tipo-tarea"],
    },
    {
        "nuevaClave": "OSS-247",
        "seccion": "OSS-87",
        "resumen": "Spike: investigar el diagrama de contexto de la solución",
        "descripcion": SEC_ESQUEMA,
        "tipoOriginal": "Spikes",
        "etiquetas": ["cap-3", "sec-3-3", "tipo-spike"],
        "asignado": MANUEL,
    },
    {
        "nuevaClave": "OSS-248",
        "seccion": "OSS-87",
        "resumen": "Elaborar el diagrama de contexto de la solución",
        "descripcion": SEC_ESQUEMA,
        "tipoOriginal": "Trabajo Tecnico",
        "etiquetas": ["cap-3", "sec-3-3", "tipo-tt"],
    },
    {
        "nuevaClave": "OSS-249",
        "seccion": "OSS-87",
        "resumen": "Fuente única de verdad de la existencia y del cálculo del disponible: decisión, fundamento y costeo",
        "descripcion": SEC_ESQUEMA
        + "\nCubre: Caso_09_Cadena_Multitienda.md:988 — que la decisión sobre la fuente única de verdad de la existencia y sobre el cálculo del disponible esté tomada, fundada y costeada.",
        "tipoOriginal": "Trabajo Tecnico",
        "etiquetas": ["cap-3", "sec-3-3", "tipo-tt"],
    },
]

with open(PLAN, encoding="utf-8") as fh:
    plan = json.load(fh)

subtareas = plan["subtareas"]
registradas = {t["nuevaClave"] for t in subtareas}

faltan = [n for n in NUEVAS if n["nuevaClave"] not in registradas]
if faltan:
    subtareas.extend(faltan)

subtareas.sort(key=lambda t: int(t["nuevaClave"].split("-")[1]))

claves_nuevas = [n["nuevaClave"] for n in NUEVAS]
assert len(claves_nuevas) == len(set(claves_nuevas)), "claves duplicadas"
assert len(subtareas) == len({t["nuevaClave"] for t in subtareas}), "nuevaClave repetida"

con_origen = {t["origenClave"] for t in subtareas if t.get("origenClave")}
a_borrar = set(plan["aBorrar"])
assert a_borrar == con_origen, sorted(a_borrar ^ con_origen)
sin_origen = [t for t in subtareas if not t.get("origenClave")]
assert len(sin_origen) == 15, len(sin_origen)

secciones = {s["clave"] for s in plan["secciones"]}
for t in subtareas:
    assert t["seccion"] in secciones, t

with open(PLAN, "w", encoding="utf-8") as fh:
    json.dump(plan, fh, ensure_ascii=False, indent=2)

# --- CSV de mapeo ---
secciones_map = {s["clave"]: s for s in plan["secciones"]}
agrupadoras = {a["id"]: a for a in plan["agrupadoras"]}
lineas = ["origen,nueva,seccion,seccion_resumen,agrupadora,subtarea_resumen,tipo_original,etiquetas"]
for t in subtareas:
    sec = secciones_map[t["seccion"]]
    lineas.append(
        "{origen},{nueva},{seccion},{seccion_resumen},{agrupadora},{resumen},{tipo},{etiquetas}".format(
            origen=t.get("origenClave", "NUEVA"),
            nueva=t["nuevaClave"],
            seccion=t["seccion"],
            seccion_resumen=sec["resumen"],
            agrupadora=agrupadoras[sec["agrupadora"]]["clave"],
            resumen=t["resumen"],
            tipo=t["tipoOriginal"],
            etiquetas="|".join(t["etiquetas"]),
        )
    )

with open(CSV, "w", encoding="utf-8", newline="") as fh:
    fh.write("\n".join(lineas) + "\n")

# --- JSON de etiquetas ---
etiquetas = {}
for a in plan["agrupadoras"]:
    etiquetas[a["clave"]] = a["etiquetas"]
for s in plan["secciones"]:
    etiquetas[s["clave"]] = s["etiquetas"]
for t in subtareas:
    etiquetas[t["nuevaClave"]] = t["etiquetas"]

with open(ETIQUETAS, "w", encoding="utf-8") as fh:
    json.dump(etiquetas, fh, ensure_ascii=False, indent=2)

print("agregadas ahora:", len(faltan), "| subtareas en plan:", len(subtareas))
print("rango total:", subtareas[0]["nuevaClave"], "->", subtareas[-1]["nuevaClave"])
print("sin origen (nuevas de usuario):", len(sin_origen))
print("aBorrar intacto:", len(a_borrar))
print("CSV filas:", len(lineas) - 1)
print("incidencias a etiquetar:", len(etiquetas))
for k in claves_nuevas:
    print("  ", k, etiquetas[k])
