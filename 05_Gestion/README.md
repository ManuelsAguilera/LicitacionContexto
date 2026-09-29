# Gestión del proyecto

Material de gestión: aquí vive la trazabilidad entre el plan de trabajo, los artefactos redactados y
la propuesta.

## `jira/`

Estructura del proyecto `OSS` en Jira Cloud, que organiza el trabajo por capítulo.

| Subcarpeta | Contenido |
| :--- | :--- |
| `plan/` | `restructuracion_2026-09-29_plan.json`: **fuente de verdad** de la estructura de 3 niveles (Épica de capítulo > Historia de sección > Subtarea) |
| `mapeo/` | CSV de correspondencia entre subtareas y secciones, payload de importación y JSON de etiquetas |
| `scripts/` | Utilidades Python y PowerShell que generan los artefactos anteriores y consultan la API de Jira |
| `historico/` | Estructura plana de 2 niveles de la importación original, ya reemplazada. Se conserva como referencia; **no se usa para operar** |

### Estructura actual en Jira

8 agrupadoras (capítulos 1 a 5 y 13) > 34 historias > 77 subtareas. Las subtareas
`OSS-173` a `OSS-235` reemplazan a los originales `OSS-105` a `OSS-164`, que ya fueron borrados.
`historico/borrar_manual.txt` describe ese borrado y está obsoleto a propósito.

### Advertencia: dos taxonomías de secciones

Los nombres de sección del plan de Jira **no coinciden** uno a uno con el índice del Informe 1
(ver las observaciones 1 a 5 de `02_Propuesta/indice.md`). El plan sirve para organizar el trabajo;
el índice del informe manda sobre la estructura del documento.

### Credenciales

Los scripts leen el token de `~/.local/share/opencode/mcp-auth.json`. **Nunca** versionar ese
archivo ni escribir tokens en los scripts.
