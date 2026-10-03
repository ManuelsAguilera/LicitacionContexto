# Gestión del proyecto

Material de gestión: aquí vive la trazabilidad entre el plan de trabajo, los artefactos redactados y
la propuesta.

## Sistema de artefactos

`convenciones/artefactos.md` define IDs y metadatos; `reportes/` contiene reconocimiento, problemas y contradicciones; `scripts/` en la raíz de esta carpeta contiene importación, validación, estado, contexto y exportación. Ejecutar `python 05_Gestion/scripts/<script>.py --help` para ver opciones. Los comandos de importación y compilación admiten `--dry-run`; los importes requieren un mapa revisado para aplicar.

### Flujo operativo

1. Importar un `.docx` (incluida una exportación de Google Docs) o un `.md` completo con `migrar.py --fuente <archivo> --parte T7-NN --dry-run --reporte <json>`. El informe conserva bloques, tablas y referencias detectadas, propone destinos y registra hashes de fuente e índice.
2. Revisar todas las asignaciones y completar un mapa con esos hashes, `aprobado_por`, `aprobado_el` y `asignaciones` por número de bloque. Solo entonces ejecutar `migrar.py` sin `--dry-run --mapa-aprobado <json>`. Nunca sobrescribe secciones o adjuntos existentes.
3. Ejecutar `agregar_frontmatter.py --dry-run` antes de aplicarlo; usar `check.py`, `estado.py` y `brief.py` para revisar trazabilidad, faltantes y contexto.
4. Diseñar desde `plantillas/tema.yml`, `base.css` y los componentes Lua; probar con `build.py --muestra --todo`. Para exportar, ejecutar `build.py --parte T7-NN` o `--todo`.

El PDF se imprime con Edge/Chromium en modo sin interfaz, disponible en Windows; Pandoc se utiliza cuando está instalado para convertir Markdown, con un conversor local acotado como fallback. La salida PDF no reemplaza la validación visual ni la revisión del índice obligatorio. La publicación como Google Docs queda como copia derivada y requiere importación nativa y lectura de vuelta; no tratar el HTML como documento publicado.

La portada usa sangrado a página completa y el logotipo oficial almacenado en `plantillas/recursos/onlysimplesolutions.png`. La composición de marca se ajusta desde `plantillas/tema.yml` y `plantillas/base.css`.

Cada adjunto no-formulario declarado se exporta como PDF individual cuando existe y su tipo es Markdown, SVG o imagen; los formularios conservan su archivo separado. Si falta un adjunto o su tipo no está soportado, el build se detiene antes de publicar el PDF principal. Los bloques Mermaid requieren `mmdc` y se convierten en SVG antes de la impresión. La verificación final exige `pypdf` para comprobar extracción de texto, marcadores, metadatos y fuentes incrustadas.

Para cerrar un subdocumento, debe existir `sd-NN_referencias.md` dentro de su carpeta, con frontmatter en estado `revisado`/`congelado`. Además, el registro IA debe tener una fila verificada por cada sección, adjunto y formulario declarado. El build incorpora Referencias y genera al final la Declaración de uso de IA; sin estas condiciones no publica un PDF final.

El piloto T7-03 parte del Informe 1, pero su mapa actual es una **propuesta no aprobada**: las 55 asignaciones requieren revisión humana y todavía no se han materializado archivos de sección a partir de ellas. Las diferencias entre el maestro provisional y el índice del Comunicado 10 deben resolverse a favor de este último. La fase de exportación final y los anexos se validan tras esa migración aprobada.

La fuente de skills compartidas está en `.agents/skills/`. En Windows, ejecutar `05_Gestion/scripts/link_skills.ps1` para crear junctions hacia `.claude/skills/` y `.opencode/skills/`; el script no reemplaza carpetas con contenido.

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
