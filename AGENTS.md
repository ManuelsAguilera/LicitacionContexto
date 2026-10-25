# AGENTS.MD

## Proyecto

Proyecto universitario (PUCV, Escuela de Informática — ICI-5444 Taller de Formulación de Proyectos Informáticos). Se redacta la propuesta técnico-económica para una licitación pública **ficticia** (N° TFEP-01/2026), **Caso 09 — Cadena Multitienda** (Multitiendas Ancoa S.A.). Todo en **español**. La salida es documentación tipo oferta (arquitectura, servicios, requerimientos, plan, riesgos), no código.

**Proponente:** Only Simple Solutions (planilla de consultas col. B, nomenclatura de archivos Art. 43.3, todos los documentos/sobres). **Equipo:** Vicente Rosales (líder), Alex Alfaro, Samira Becerra, Manuel Aguilera, Martin Vasquez, Daniel Cepeda, Eliseo Guarda.

## Regla de exportación LaTeX/PDF (obligatoria, leer antes de tocar LaTeX o PDF)

- Markdown → LaTeX → PDF de los subdocumentos T-7 **solo** con `05_Gestion/scripts/exportar_latex.py`, según `.agents/skills/exportar/SKILL.md`. Orden: `doctor` → `estado` → `importar` (solo si falta el `.tex`) → editar `.tex` → `verificar` → `compilar`.
- **Fuente de verdad** tras importar: `02_Propuesta/latex_final/sd-NN/…Subdocumento N.tex`. Los `.md` de `02_Propuesta/` son solo contexto; los cambios de contenido van en el `.tex`.
- El preámbulo es la plantilla fija `latex_final/plantilla/oss-pandoc.latex` (marcador `% oss-plantilla:` en línea 1); el formato visual vive en `oss.sty`. `verificar`/`compilar` rechazan cualquier desvío.
- **Prohibido:** escribir/editar preámbulos, crear `.tex` a mano, llamar a `pandoc`/`xelatex`/`latexmk`, borrar un `.tex` para reimportarlo, usar `pdf-handling`/WeasyPrint/`docx`/HTML para la propuesta. `importar --reemplazar` solo con instrucción explícita (respalda en `latex_final/respaldo/`).
- Prism: `exportar_latex.py prism-empaquetar` (zips en `05_Gestion/build/prism/`); los cambios vuelven **solo** con `prism-importar --parte T7-NN --zip <archivo>` (antes `--dry-run`). No copiar `.tex` de Prism a mano ni editar preámbulo, `oss.sty` o `recursos/` allí.
- Intérprete: `python3` (Linux/macOS) o `python` (Windows); si falla, probar el otro. Pruebas: `python3 -m unittest discover -s 05_Gestion/tests -v`.

## Reglas de redacción vs. plantilla

- **Redacción (contenido):** `05_Gestion/convenciones/reglas-redaccion.md` (`RR-NN`, del Comunicado 10 y decisiones del equipo). Aplicar al escribir/editar un `.tex`, local o en Prism. Verificación mecánica: `exportar_latex.py verificar-redaccion` (solo informa). Tablas del cuerpo: RR-15 a RR-19.
- **Plantilla (formato):** `reglas-plantilla.md` (`RP-NN`), las cumple `oss.sty`/`plantilla/`. No se replican a mano ni se cambian fuera del flujo de la plantilla.
- **Citas:** aplicar `.agents/skills/citas-proyecto/SKILL.md` (obligatorio para citas y Referencias). Citar solo exigencias particulares y contexto/datos del Caso 09, con documento, capítulo/numeral y **folio impreso** verificado en el PDF. No citar exigencias generales de las Bases Administrativas/Transversales ni indicaciones del profesor (sí conservar sus contenidos obligatorios e IDs técnicos para trazabilidad). Decisiones propias y remisiones internas no generan entradas bibliográficas. Ayudas: `90_Referencia/indice_paginas_caso09.md` y `caso09_ocr_paginado.txt`. Conservar `00_Bases/Caso_09_Cadena_Multitienda.md` como espejo de lectura.

## Fuentes y precedencia

`00_Bases/` es la fuente de verdad (inmutable). Precedencia (Art. 5° Bases Administrativas):

1. `Bases_Administrativas.md` — proceso y contrato: cronograma de 56 meses, despliegue híbrido, hitos, formularios/sobres, evaluación, 5 innovaciones obligatorias.
2. `Bases_Transversales.md` — requisitos técnicos comunes `RT-CC.NN` (Obligatorio/Deseable/Según caso), respondidos uno a uno en el **Formulario T-12**.
3. `Caso_09_Cadena_Multitienda.md` — **no es una especificación**: traducir su narrativa (dolores, contradicciones, vacíos) en alcance, arquitectura, plan y estrategia es lo que se evalúa.

Complementos con rango de base: `DivisionNegocios.md` (módulos retail, financiero y áreas compartidas de Ancoa; mismo rango que el caso) y el **Comunicado 10** (`Comunicado_10_…md`, correo reenviado sin limpiar): fija la **estructura obligatoria** de la Propuesta Técnica e informes preparatorios (capítulos, títulos, orden, contenido del T-7 por título, reglas de redacción); gobierna forma y ubicación, no añade requisitos, y prevalece sobre `05_Gestion/convenciones/`.

El caso puede **endurecer** un requisito transversal, nunca **rebajarlo**. Un "Según caso" se completa con los valores del caso; si no los define, rige el default del transversal.

**Tablas de las Bases incompletas** (la extracción perdió contenido; p. ej. ponderación del T-21, `Bases_Administrativas.md:2366`, y fila del Plan de Riesgos): no estimar ni hardcodear esas cifras; dejarlas en blanco con nota de pendiente que apunte al ítem del T-21. Las tablas del informe quedan tal cual hasta una etapa posterior.

## Reglas que condicionan el diseño

- **Despliegue híbrido obligatorio** (Art. 16): carga principal en nube pública + componentes on-premise; ni solo-nube ni solo-on-premise.
- **Cronograma de 56 meses innegociable** (Art. 17): Etapa 1 (meses 1–15, producción mes 16), Etapa 2 (meses 13–20, producción mes 21), Operación 36 meses (21–56).
- **5 innovaciones obligatorias** (Cap. 5 Bases Admin), una por tipo, trazables con arquitectura, EDT y flujo de caja.
- **Línea roja:** Ancoa es a la vez una tienda y un **emisor de crédito fiscalizado** (dos negocios, dos regímenes jurídicos). Tratarlos como uno o borrar la separación de sus datos descalifica la propuesta; gobierna toda decisión de arquitectura de datos.
- **Presupuesto efectivamente ilimitado:** nunca se sacrifica calidad, arquitectura ni diseño por costo. Criterio siempre: la mejor solución (correctitud, robustez, escalabilidad, disponibilidad, seguridad, cumplimiento). La oferta económica sostiene esa solución; la única restricción real es el cronograma.
- **No es un sistema legado:** es el tejido de 9 plataformas de 6 proveedores con 14 interfaces punto a punto y registros imprecisos (12,4% de discrepancia en conteo cíclico). Plantearlo como reemplazo de un sistema es un error conceptual.

## Carpetas

Los prefijos numéricos indican la etapa del pipeline. Cada carpeta principal tiene `README.md`: leerlo antes de escribir en ella.

| Carpeta | Contenido |
| :--- | :--- |
| `00_Bases/` | Documentos rectores, **inmutables**. |
| `01_Requerimientos/` | Excel. **Fuente oficial: `RequerimientosAtomizados_Depuracion_Alcance.xlsx`** (v3.0: `RF-001`..`RF-226`, `RNF-01`..`RNF-76`, `OP-01`..`OP-09`; hojas `6_Equivalencia_IDs` y `7_Depuracion_Alcance`). v2.1 y `RequerimientosHumanos.xlsx` en `historico/`. Espejos `.md` en `md/`. |
| `02_Propuesta/` | **Corazón del proyecto:** los 14 subdocumentos del T-7, una carpeta `sd-NN_*/` cada uno. |
| `03_Formularios/` | `A/` (A-1..A-6), `B/` (T-6..T-22), `C/` (E-21..E-26). |
| `04_Adjuntos/` | `diagramas/` (fuente `.py`/`.drawio`/`.dot` + export PNG/PDF, sin subcarpetas), `hardware/`, `tablas/`. |
| `05_Gestion/` | Scripts, convenciones, tests y `jira/` (plan del proyecto `OSS`). |
| `06_Informes/` | `presentaciones/` (Art. 45°) e `informes/Informe N/` (PDF no versionados; se entregan por Drive). Se arman desde los `.tex`. |
| `07_Entregables/` | `sobre_1_administrativo/`, `sobre_2_tecnico/`, `sobre_3_economico/`, `pdf_final/`. |
| `80_Artefactos/` | Material de trabajo (no entregable): consultas al mandante, auditorías, rúbricas, `sd-NN_contexto/`. |
| `90_Referencia/` | `TrabajosAnteriores_DistriProducto/` (ver abajo), `clases markdown/`, `CMF/` (terceros, no versionado). |
| `.opencode/` | Skills, plugin `activar-skills.ts` y dependencias (`node_modules/`, `opencode-loop/` no versionados). |

## Artefactos

- **Formato:** todo contenido en `.md` (o `.txt` para volcados); `.xlsx/.docx/.pptx/.pdf` solo como lectura/entrega o export final. Exentos: `*.py`, `*.ps1`, `*.json`, `*.csv` de `05_Gestion/`. Los subdocumentos sin `.tex` se redactan en `.md`; una vez importados, manda el `.tex` (importación única a `latex_final/`, no se regenera desde Markdown). El contenido se redacta directamente en el `.tex` con Prism; no hay importación desde Google Docs/DOCX. No existe un segundo renderizador de PDF. Formularios e informes preparatorios quedan fuera del alcance del exportador.
- **Espejos:** un `.xlsx` oficial puede tener espejo `.md`; si difieren, manda el Excel. Se regeneran, no se editan.
- IDs, estados, frontmatter y procedencia: `05_Gestion/convenciones/artefactos.md`. El estado `revisado` lo asigna solo un humano, nunca un script o agente.
- El índice del Comunicado 10 gobierna la estructura: cada maestro reproduce sus capítulos y títulos tal cual.
- `check.py`, `estado.py` y `brief.py` verifican documentación; no sustituyen la revisión técnica ni humana.
- Retroalimentación del Informe 1: `80_Artefactos/revision_informe_1_transcripcion.md` y rúbrica `revision_informe_1_rubrica_de_cierre.md`; usar la rúbrica por subsección, contrastando cada criterio con Bases, Comunicado 10 y estado actual antes de marcarlo cumplido.
- Skills compartidas (redactar, revisar, cerrar, exportar) en `.agents/skills/` (fuente canónica, léanla Codex y OpenCode). Claude Code lee `.claude/skills/`, creada con `python3 05_Gestion/scripts/link_skills.py`. Editar siempre la fuente canónica.

### Nombres

| Tipo | Patrón | Ejemplo |
| :--- | :--- | :--- |
| Maestro | `sd-NN_titulo.md` | `sd-04_arquitectura-logica-y-fisica.md` |
| Sección | `sd-NN_sN_titulo.md` | `sd-04_s2_arquitectura-fisica.md` |
| Adjunto | `sd-NN_sN_titulo.<ext>` | `sd-04_s2_inventario-hardware.xlsx` |
| Diagrama | `diag-NN-SN_titulo.<ext>` | `diag-04-02_arquitectura-fisica.svg` |
| Formulario | `form-<ID>_titulo.<ext>` | `form-T-12_matriz-cumplimiento-tecnico.xlsx` |
| LaTeX subdocumento | `OnlySimpleSolutions-SubdocumentoN[-Anexos].tex` en `latex_final/sd-NN/` | `OnlySimpleSolutions-Subdocumento4.tex` |
| LaTeX formulario | `OnlySimpleSolutions-Formulario-T-N.tex` en `latex_final/Formularios/` | `OnlySimpleSolutions-Formulario-T-16.tex` |

## Cómo se escribe la propuesta

Son **14 subdocumentos** (Formulario T-7, `Bases_Administrativas.md:2066`). Cada `02_Propuesta/sd-NN_<titulo>/` conserva un **`.md` maestro** de identificación, estructura, estado y trazabilidad; los archivos Markdown de contenido previo son antecedentes cuando ya existe fuente LaTeX. El maestro es la **fuente de verdad del estado**: actualizar su fila al empezar o terminar una sección. `02_Propuesta/indice.md` contiene el índice general, la cobertura por informe y las reglas de ensamblado. La numeración del informe no coincide con la del plan Jira: manda el maestro.

**Informes preparatorios (Art. 45°):** tres informes y tres presentaciones. El Informe 1 cubre los sd 1–5 y 13; los sd 6–12 y 14 van en los informes 2 y 3.

## Clases del profesor (evaluar críticamente)

`90_Referencia/clases markdown/` tiene las clases FEP01–FEP05 y `Guia_de_Navegacion_FEP01-FEP05.md` (índice por diapositiva; empezar por ella y abrir solo la transcripción pertinente, son grandes). Úsalas para contrastar definiciones, criterios y errores comunes (criterio de aceptación con umbral, regla del 100 % de la EDT, validar vs. controlar alcance) y cita la diapositiva que apoye un juicio. No aportan hechos ni cifras de Ancoa; si contradicen las Bases o el Comunicado 10, mandan estos.

## TrabajosAnteriores: no usar salvo instrucción expresa

No consultar `TrabajosAnteriores_DistriProducto/` salvo que el usuario lo indique. Solo sirve para copiar la **estructura** de un capítulo (títulos, orden, tablas, anexos); **nunca** trasladar tecnologías, módulos, volúmenes, cifras ni servicios. Mapeo (archivo → capítulo): sd-02 `subdocumento_2.md` (Cap 3 Alcance), sd-03 `subdocumento_3.md` (Cap 4 Lógica), sd-04 `subdocumento_4.md` (Cap 5 Física), sd-06 `Subdocumento_6.md` (Cap 7 Metodologías), sd-07 `_7` (Cap 8 Plan de Trabajo), sd-08 `_8` (Cap 9 Riesgo), sd-09 `_9` (Cap 10 Calidad), sd-10 `_10` (Cap 11 Operación), sd-11 `_11` (Cap 12 Planes en Operación), sd-12 `_12` (Cap 13 Equipo y Alianzas).

## Estado del proyecto y contexto de inicio (2026-10-25)

- **Referencias de consistencia indicadas por el usuario:** SD-04 para arquitectura, tecnologías, infraestructura y suministro; SD-07 para EDT, planificación, esfuerzo e implantación. Las Bases y el Comunicado 10 mantienen su precedencia. Una contradicción entre ambas referencias se registra como decisión pendiente; no se resuelve por inferencia.
- **Entrada de contexto:** `80_Artefactos/contexto-activo/indice.md`; referencias de trabajo del equipo. Los hashes de corte están en `05_Gestion/contexto-referencias-2026-10-25.json`, para consulta de vigencia; no cargar ese registro como contenido de redacción. Cargar únicamente las decisiones y pendientes pertinentes a la tarea y confirmar en el `.tex` actual. No cargar recursivamente todos los antecedentes.
- Hay fuentes LaTeX para SD-01 a SD-09 y SD-13. El resto debe conciliarse con SD-04 y SD-07; una importación reciente no acredita consistencia. SD-10, SD-11, SD-12 y SD-14 siguen pendientes de fuente LaTeX.
- Los 13 formularios recibidos están en `02_Propuesta/latex_final/Formularios/`. T-11 tiene además una copia local divergente en `sd-04/OSS-Formulario-T-11.tex`: conservar ambas hasta su conciliación; no elegir contenido por nombre o fecha.
- **Estados separados:** fuente disponible, estado declarado en el maestro, compilación disponible y revisión humana. Importado o compilado no significa consistente, revisado ni aceptado.
- `brief.py <ID>` selecciona LaTeX cuando existe; admite partes, secciones, formularios T-N y adjuntos ADJ-NNN. `estado.py` muestra esas dimensiones separadas. `check.py` controla metadatos y trazabilidad, no certifica el contenido LaTeX.
- Contextos históricos, paquetes de recepción, respaldos y derivados quedan fuera de las búsquedas habituales; consultarlos deliberadamente cuando se necesite procedencia. Ver el manifiesto y el registro de limpieza en `05_Gestion/registro-limpieza-contexto-2026-10-25.json` y `05_Gestion/reportes/limpieza-contexto-2026-10-25.md`.
- La información anterior sobre ramas, commits de entrega y diagnósticos de herramientas describe instantáneas históricas; no sustituye las fuentes actuales. Jira debe consultarse en su estado real si la tarea lo necesita.

## Flujo git

- `main` solo recibe cambios por **Pull Request** revisado por otra persona; no se commitea directo.
- Una rama corta por tarea (`sdNN/<tema>`, `feat/`, `fix/`, `chore/`) desde `origin/main` actualizado; se borra al mergear y no se reutiliza.
- Commits atómicos por tema, en español e imperativo; no mezclar subdocumentos distintos, figuras, scripts y limpieza.
- Nunca versionar PDF de informes, zips, descargas de Prism (`* (1).tex`), documentos de terceros ni derivados regenerables (`.gitignore`). Los `.tex` vuelven de Prism solo con `prism-importar`.
- Antes del PR: `python3 -m unittest discover -s 05_Gestion/tests` y `exportar_latex.py verificar`.
- Un worktree por persona salvo necesidad puntual; eliminarlos al terminar.

## Verificación

No hay build ni lint. Hay pruebas del exportador y `exportar_latex.py verificar` (cada `.tex` respeta la plantilla). La verificación del trabajo es la coherencia entre documentos: precedencia, trazabilidad (RT → módulo → entregable) y consistencia de cifras/plazos con el cronograma obligatorio.

## Skills y herramientas

Cargar el skill orquestador **`licitacion-workflow`** (`.opencode/skills/`) al iniciar cualquier avance de la propuesta; indica qué skill usar en cada fase (el plugin `.opencode/plugins/activar-skills.ts` refuerza la activación). Las skills del proyecto están versionadas en `.opencode/skills/`:

| Skill | Uso |
| :--- | :--- |
| `licitacion-workflow` | Orquestación (cargar siempre) |
| `xlsx` / `docx` / `pptx` | Requerimientos, oferta económica y flujo de caja / formularios de sobres / las 3 presentaciones |
| `exportar` (`.agents/skills/`) | Única ruta a LaTeX corporativo y PDF; `pdf-handling` no se usa |
| `architecture-diagrams` | Diagramas de arquitectura (lógica/física/datos/seguridad/despliegue) |
| `cloud-architecture` / `sre-practices` | Arquitectura híbrida (RT-03) / disponibilidad 99,9 %, RTO/RPO, SLOs |
| `project-estimation` | Esfuerzo y desglose por rol (nivelación T-15) |
| `legal-risk-assessment` / `risk-assessment` | Riesgos contractuales y técnicos |
| `deep-research` / `technical-writing` | Investigar lo que el caso no explica / redacción técnica extensa |
| `mermaid-diagrams` | **No usar**: el importador rechaza Mermaid |
| `plantuml-diagrams` | UML/C4 formal (.puml) → PNG/SVG vía Kroki |
| `jira-workflow` | Tomar tareas, cambiar estado, consultar sprint/board, comentar |

`opencode.jsonc` agrega `opencode-mermaid-renderer` (requiere opencode ≥ 1.0.137; reiniciar opencode tras cambiar la config).

### Jira (opcional)

MCP oficial de Atlassian (Rovo) vía `mcp.jira` en `opencode.jsonc` (`"enabled": true`, autenticado en esta máquina). Sin cuenta no se bloquea nada: las herramientas `jira_*` solo aparecen tras autenticar. Si hay tareas por gestionar, recomendar activarlo, sin bloquear el trabajo. Activación (una vez por usuario): `enabled: true` en `mcp.jira` → reiniciar opencode → `opencode mcp auth jira` (OAuth en el navegador) → verificar con `opencode mcp list`. Requiere Jira Cloud; endpoint `https://mcp.atlassian.com/v1/mcp/authv2`; el token queda en `~/.local/share/opencode/mcp-auth.json`, nunca en el repo. Flujo tomar → marcar → completar: skill `jira-workflow`.

### MCP `ragdocs` (búsqueda semántica)

Servidor `mcp-server-ragdocs` sobre Qdrant Cloud, para preguntas como "¿dónde dice el caso que el inventario discrepa?". Viene en `enabled: false`: copiar `.env.example` a `.env` (`QDRANT_URL`, `QDRANT_API_KEY`, proveedor de embeddings), poner `enabled: true` en `mcp.ragdocs` y reiniciar opencode. Reglas:

- Solo texto: no lee `.xlsx/.docx/.pdf`; indexar `00_Bases/`, espejos `.md` de `01_Requerimientos/` y `02_Propuesta/**`.
- La base vectorial es caché, no fuente de verdad: contrastar con el archivo original antes de citar.
- Nunca indexar material sensible (Formulario A-1, datos de la contraparte).
- Claves por `{env:...}`; los valores viven en `.env` (en `.gitignore`).

## Diagramas

- Los diagramas de la propuesta se entregan como imágenes PNG/SVG/PDF en `04_Adjuntos/diagramas/`, con la fuente editable (`.dot`, `.puml`, etc.) al lado; se enlazan en Markdown con rutas relativas y el importador los copia a `latex_final/figuras/`. Sin bloques Mermaid.
- UML/C4 formal: PlantUML exportado a imagen (GitHub no lo renderiza): `curl https://kroki.io/plantuml/png -d 'diagram_source=...'`. Interactivos/animados (presentaciones, sobres): `architecture-diagrams` (HTML → screenshot PNG).
- **Diagramas de arquitectura de esta propuesta:** cargar `.agents/skills/diagramas-ancoa/SKILL.md` (estilos lógicos L1–L6 y físicos F1–F5; validar la especificación JSON antes de renderizar). Su procedimiento prevalece sobre las recomendaciones generales; sus ejemplos no son decisiones de alcance. El MCP local `diagramas-ancoa` expone catálogo, validación y renderizado (instalación: `references/instalacion-mcp.md`). El contenido se sigue contrastando con las Bases y los subdocumentos vigentes.

Grafo de scripts actualizado y acotado: `05_Gestion/scripts/graphify-out/graph.json` (40 archivos, 452 nodos, 1028 relaciones). Consultarlo con `graphify query "pregunta" --graph 05_Gestion/scripts/graphify-out/graph.json`; regenerar con `graphify update 05_Gestion/scripts`. El grafo mixto anterior de la raíz se conserva como antecedente y no determina vigencia del contexto.

## Graphify

- `graphify-out/graph.json`: grafo anterior de scripts y contexto, con contenido histórico; no representa el LaTeX actualizado ni determina vigencia de decisiones. El MCP por defecto apunta a él.
- `graphify-out/documentos-20261025/graph.json`: grafo documental de las 26 fuentes integradas, extracción enfocada y no exhaustiva. Consultar con `graphify query "pregunta" --graph graphify-out/documentos-20261025/graph.json` y confirmar siempre en los `.tex`.
- Búsqueda habitual: `rg` respeta `.ignore`; Graphify usa `.graphifyignore`. Los históricos pueden leerse explícitamente para investigar procedencia. Ningún grafo sustituye las Bases o las fuentes actuales. Skill en `.codex/skills/graphify/`.
- Tras cambios de scripts, actualizar el grafo de scripts con el corpus filtrado y registrar su alcance; no ampliar automáticamente el corpus a todos los documentos del repositorio.
