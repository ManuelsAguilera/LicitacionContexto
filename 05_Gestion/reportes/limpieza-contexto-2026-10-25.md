# Limpieza del contexto — 25 de octubre de 2026

## Resultado y límites

Se implementó la primera etapa autorizada: selección de fuentes, guías, herramientas y matriz de ajustes. SD-04 es referencia de arquitectura y SD-07 de planificación, subordinados a las Bases y al Comunicado 10. Se preservaron las fuentes de contenido; esta etapa no reescribe subdocumentos ni formularios y no asigna revisión humana.

- [Índice activo](../../80_Artefactos/contexto-activo/indice.md): referencias actuales y organización del trabajo del equipo. Los hashes de corte se consultan en `05_Gestion/contexto-referencias-2026-10-25.json`.
- [Matriz de ajustes](../../80_Artefactos/contexto-activo/matriz-ajustes.md): siete agrupaciones, evidencia, acción, prioridad y estado.
- [Manifiesto de traslados](../registro-limpieza-contexto-2026-10-25.json): origen, destino, hash SHA-256, tamaño y motivo por archivo.
- Evidencia de pruebas y baseline: `05_Gestion/build/limpieza-contexto-20261025/` (salida regenerable, excluida de contexto habitual).

## Cambios de entrada y herramientas

Las guías raíz, el índice, los maestros, los README afectados y las skills canónicas ahora distinguen contenido LaTeX de metadatos Markdown. Se retiraron estados de entrega anteriores y rutas inexistentes de los puntos de entrada actualizados. Los cuatro subdocumentos sin LaTeX siguen pendientes.

`brief.py <ID>` conserva la CLI anterior y añade formularios `T-N` y adjuntos registrados `ADJ-NNN`. Prioriza el `.tex` canónico. Para secciones utiliza encabezados explícitos inequívocos; ante ausencia o duplicidad informa el problema y muestra la fuente principal, sin recuperar silenciosamente Markdown antiguo. Conserva la procedencia y el hash aunque se trunque el contenido. Las copias divergentes y de recepción no son fallback.

`estado.py` separa fuente disponible, estado declarado, compilación disponible y revisión humana. Un informe de compilación sin hash no acredita que el PDF corresponda a la fuente actual. `check.py` se identifica como control de metadatos y trazabilidad Markdown; no certifica contenido LaTeX. El detector de desfase ya no declara v3.1 como catálogo oficial ni tacha automáticamente los recuentos de v3.0 de obsoletos.

El README de formularios documenta las dos versiones de T-11 y la falta de una ruta CLI del exportador para compilar la carpeta Formularios. La decisión sobre la versión final de entrega sigue pendiente.

## Archivo reversible realizado

Se trasladaron **9 archivos, 469.850 bytes**, sin eliminación definitiva, a `80_Artefactos/archivo-contexto/2026-10-25/`:

- El borrador de innovaciones `seccion3_innovaciones.md`, que ya se autodeclaraba superado.
- Los archivos existentes del paquete de entrega SD-07 de 12-10-2026. Se conserva el material recibido íntegro; no se inventan los adjuntos que ese paquete ya no contenía.

Se comprobaron los hashes de destino y se ensayó la reconstrucción de las nueve rutas originales en un directorio temporal. El contenido archivado conserva sus bytes. Para restaurar deliberadamente: consultar el manifiesto, comprobar el hash y copiar el archivo al origen solo si esa ruta continúa libre. No reintroducir históricos como fuentes actuales por el mero hecho de restaurarlos.

Se actualizaron referencias en los documentos afectados. Las menciones históricas dentro del material archivado describen su versión original. Los diez `no_usar_*.md` de SD-03 ya estaban archivados y permanecen donde estaban. Las decisiones de SD-04/07/08/09, los dos T-11, las fuentes editables de diagramas y la retroalimentación del profesor se conservaron.

`.ignore` filtra las búsquedas habituales con `rg`; `.graphifyignore` filtra la indexación. Excluyen históricos, archivos trasladados, borradores, recepción, respaldos, compilados y corpus derivados. Para investigar procedencia se abre explícitamente la ruta archivada. Una exclusión no impide el acceso deliberado ni supone eliminación.

## Graphify

El grafo de scripts se regeneró con un corpus acotado de 40 archivos: `05_Gestion/scripts/graphify-out/graph.json`, con 452 nodos, 1.028 relaciones y 15 comunidades. La extracción de código es estructural, sin LLM.

El grafo documental anterior de las 26 fuentes LaTeX sigue en `graphify-out/documentos-20261025/graph.json`: extracción semántica enfocada, no exhaustiva, confirmada contra las fuentes originales. El grafo mixto legado `graphify-out/graph.json` se conserva como antecedente. El MCP ya configurado en el proyecto sigue apuntando a este último; las guías indican seleccionar explícitamente el grafo correcto y no usar la conexión predeterminada para decidir vigencia de contenido.

## Validación

- Las **30 fuentes y archivos de plantilla protegidos** mantienen exactamente su SHA-256 inicial, incluidas las dos versiones T-11. SD-04 y SD-07 coinciden además con los hashes fijados en el índice activo.
- `exportar_latex.py verificar`: diez partes disponibles correctas. No hubo recompilación porque los contenidos y la plantilla no se modificaron.
- **15 pruebas nuevas correctas**: prioridad LaTeX, selección de secciones, ambigüedad/ausencia, fallback Markdown, formularios y adjuntos, exclusión de históricos, compilación con y sin hash y separación de dimensiones de estado; dos casos adicionales comprueban que el detector respeta el catálogo oficial y no promueve v3.1.
- Cuatro skills modificadas válidas mediante `quick_validate.py`; su dependencia PyYAML se instaló únicamente en el build del proyecto para esa comprobación.
- Patrones de Graphify comprobados: históricos/derivados excluidos y fuentes actuales/índice activo incluidos.
- Comprobación final de enlaces nuevos y de los maestros enlazados al LaTeX; detalle en `validacion.json` del build.
- `git diff --check` sobre los cambios de esta etapa sin errores de espacio en blanco. No se crearon commits ni PR.

## Fallos previos de la suite completa

Antes de modificar herramientas: **241 pruebas, 7 fallos y 1 error**. La pasada completa posterior: **254 pruebas, 6 fallos y 1 error**, incluidas las primeras 13 pruebas nuevas. Una pasada focalizada posterior ejecutó las **15 pruebas nuevas**, incluidas las dos comprobaciones adicionales del catálogo, todas correctas. No se añadieron fallos a la suite. Se corrigió el fallo previo que esperaba el encabezado «Regla de exportación» en AGENTS.md.

Se conservan para su resolución separada:

| Prueba | Clasificación y alcance |
|---|---|
| `test_diccionario.TestDiccionario.test_el_diccionario_publicado_esta_actualizado` | Diferencia previa entre el diccionario publicado y el generado; requiere conciliación documental con SD-04/07. No se regeneró ese contenido durante esta etapa. |
| `test_integracion.LinkSkillsTest.test_crea_enlaces_y_es_idempotente` | Restricción previa de creación de junction en el sandbox de Windows. |
| `test_plantilla.MotoresTest.test_compila_con_xelatex_y_pdflatex` (dos motores) | Fallos previos de acceso/configuración MiKTeX dentro del sandbox. |
| `test_compilar_humo.CompilarHumoTest.test_importar_y_compilar` | Error previo de compilación en ese entorno de pruebas. |
| `test_prism.PrismTest.test_manifiesto_registra_el_empaquetado` | Desigualdad previa de hashes en el escenario de empaquetado (normalización de saltos de línea por revisar). |
| `test_redaccion.SegmentacionTest.test_cada_regla_cita_su_fuente_y_verificacion` | Exigencia previa de la prueba sobre la columna de procedencia C10 de las reglas; no se alteraron las reglas editoriales. |

La matriz no equivale a una revisión contractual exhaustiva: los cruces no cotejados completos siguen «por verificar» y los cambios de catálogo, responsabilidades o condiciones contractuales siguen «requiere decisión» cuando corresponda.

## Pendiente técnico separado del trabajo de contenido

| Grupo | Documento / sección | Texto o cifra afectada | Evidencia | Acción | Relacionados | Prioridad | Estado |
|---|---|---|---|---|---|---|---|
| 4 | Formularios T-14 / T-15 / T-18 de recepción 25-10 | Anomalías de formato y verificación estática | Los preparativos de integración registran T-14/T-15 con estructura de preámbulo distinta y `\ossFinalPage` ausente; T-18 también carece de esa macro. Se conservaron cuerpos/formato propio; no se han compilado en este encargo. | Resolver por el dueño de integración cómo comprobarlos con su formato oficial. No adaptar a plantilla SD por analogía ni anunciar compilación. | SD-07, T-14, T-15, T-18, exportar | Media | por verificar |
