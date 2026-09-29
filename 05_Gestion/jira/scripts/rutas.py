# -*- coding: utf-8 -*-
"""Rutas de los artefactos de Jira, resueltas desde la ubicacion del script.

Antes los scripts usaban rutas relativas a la raiz del repositorio ("jira_batches/..."), lo que
obligaba a ejecutarlos siempre desde alla. Ahora las rutas se derivan de la ubicacion del propio
script, asi que funcionan desde cualquier directorio.
"""

from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
JIRA = SCRIPTS.parent                     # 05_Gestion/jira
GESTION = JIRA.parent                     # 05_Gestion
RAIZ = GESTION.parent                     # raiz del repositorio

PLAN = JIRA / "plan"
MAPEO = JIRA / "mapeo"
HISTORICO = JIRA / "historico"

RUTA_PLAN = PLAN / "restructuracion_2026-09-29_plan.json"
RUTA_ORIGEN = PLAN / "restructuracion_2026-09-29_origen.json"

RUTA_MAPEO_CSV = MAPEO / "restructuracion_2026-09-29_mapeo_subtareas.csv"
RUTA_ETIQUETAS = MAPEO / "restructuracion_2026-09-29_etiquetas.json"
RUTA_PAYLOAD_ESTRUCTURADO = MAPEO / "jira_import_payload_estructurado.json"
RUTA_MAPPING_ESTRUCTURADO = MAPEO / "Jira_UserStoryMapping_Estructurado.csv"
RUTA_MAPPING_VINCULADO = MAPEO / "Jira_UserStoryMapping_Vinculado.csv"

RUTA_PAYLOAD_PLANO = HISTORICO / "jira_import_payload_v2.1-plano.json"
RUTA_BORRADO = HISTORICO / "borrar_manual.txt"


def asegurar_directorios():
    """Crea las carpetas de salida si no existen."""
    for d in (PLAN, MAPEO, HISTORICO):
        d.mkdir(parents=True, exist_ok=True)
