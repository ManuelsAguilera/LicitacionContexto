# Gestión del proyecto

Material de gestión: aquí vive la trazabilidad entre el plan de trabajo, los artefactos redactados y
la propuesta.

## Sistema de artefactos

`convenciones/artefactos.md` define IDs y metadatos; `reportes/` contiene reconocimiento, problemas y contradicciones; `scripts/` en la raíz de esta carpeta contiene importación, validación, estado, contexto y exportación. Ejecutar `python3 05_Gestion/scripts/<script>.py --help` para ver opciones. Las migraciones tienen modo `--dry-run`; su aplicación requiere un mapa revisado.

### Flujo operativo

1. Importar un `.docx` (incluida una exportación de Google Docs) o un `.md` completo con `migrar.py --fuente <archivo> --parte T7-NN --dry-run --reporte <json>`. El informe conserva bloques, tablas y referencias detectadas, propone destinos y registra hashes de fuente e índice.
2. Revisar todas las asignaciones y completar un mapa con esos hashes, `aprobado_por`, `aprobado_el` y `asignaciones` por número de bloque. Solo entonces ejecutar `migrar.py` sin `--dry-run --mapa-aprobado <json>`. Nunca sobrescribe secciones o adjuntos existentes.
3. Ejecutar `agregar_frontmatter.py --dry-run` antes de aplicarlo; usar `check.py`, `estado.py` y `brief.py` para revisar trazabilidad, faltantes y contexto.
4. Para generar PDF de la propuesta técnica, cargar `.agents/skills/exportar/SKILL.md` y usar exclusivamente `scripts/exportar_latex.py`. `scripts/build.py` fue retirado para impedir una segunda versión de formato.

El exportador LaTeX usa XeLaTeX y `latexmk`; importa Markdown una vez con Pandoc, incorpora recursos gráficos, aplica el formato común definido en `02_Propuesta/latex_final/oss.sty` y valida tamaño carta y texto seleccionable. La fuente editable, reglas de inclusión de figuras, salidas y QA visual están descritos en `.agents/skills/exportar/SKILL.md` y `02_Propuesta/latex_final/README.md`.

El modo `--final` exige referencias y declaración de uso de IA en el `.tex`. Los anexos y formularios que deban entregarse por separado permanecen en sus archivos correspondientes.

El piloto T7-03 parte del Informe 1, pero su mapa actual es una **propuesta no aprobada**: las 55 asignaciones requieren revisión humana y todavía no se han materializado archivos de sección a partir de ellas. Las diferencias entre el maestro provisional y el índice del Comunicado 10 deben resolverse a favor de este último. La fase de exportación final y los anexos se validan tras esa migración aprobada.

La fuente de skills compartidas está en `.agents/skills/`. Codex y OpenCode la leen directamente; para Claude Code ejecutar `python3 05_Gestion/scripts/link_skills.py` (`python` en Windows), que crea symlinks (Linux/macOS) o junctions (Windows) hacia `.claude/skills/`. El script es idempotente y no reemplaza carpetas con contenido; `link_skills.ps1` es solo un envoltorio.

## `jira/`

Estructura del proyecto `OSS` en Jira Cloud, que organiza el trabajo por capítulo.

| Subcarpeta | Contenido |
| :--- | :--- |
| `jira/plan/` | `restructuracion_2026-09-29_plan.json`: **fuente de verdad** de la estructura de 3 niveles (Épica de capítulo > Historia de sección > Subtarea) |
| `jira/mapeo/` | CSV de correspondencia entre subtareas y secciones, payload de importación y JSON de etiquetas |
| `jira/scripts/` | Utilidades Python y PowerShell que generan los artefactos anteriores y consultan la API de Jira |
| `jira/historico/` | Estructura plana de 2 niveles de la importación original, ya reemplazada. Se conserva como referencia; **no se usa para operar** |

### Estructura actual en Jira

8 agrupadoras (capítulos 1 a 5 y 13) > 34 historias > 77 subtareas. Las subtareas
`OSS-173` a `OSS-235` reemplazan a los originales `OSS-105` a `OSS-164`, que ya fueron borrados.
`jira/historico/borrar_manual.txt` describe ese borrado y está obsoleto a propósito.

### Advertencia: dos taxonomías de secciones

Los nombres de sección del plan de Jira **no coinciden** uno a uno con el índice del Informe 1
(ver las observaciones 1 a 5 de `02_Propuesta/indice.md`). El plan sirve para organizar el trabajo;
el índice del informe manda sobre la estructura del documento.

### Credenciales

Los scripts leen el token de `~/.local/share/opencode/mcp-auth.json`. **Nunca** versionar ese
archivo ni escribir tokens en los scripts.
