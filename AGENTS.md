# AGENTS.MD

## Qué es este proyecto

Proyecto de universidad (PUCV, Escuela de Informática — Taller de Formulación de Proyectos Informáticos, ICI-5444). El objetivo es redactar la propuesta técnico-económica para una licitación pública **ficticia** (Licitación N° TFEP-01/2026) del caso asignado: **Caso 09 — Cadena Multitienda** (Multitiendas Ancoa S.A.).

Todo el trabajo se desarrolla en **español** (idioma oficial de la licitación). La salida esperada es documentación tipo oferta (arquitectura, servicios, requerimientos, planificación, evaluación de riesgos), no código.

## Identidad del proponente

- **Empresa proponente:** Only Simple Solutions (usar en columna B de la planilla de consultas, nomenclatura de archivos Art. 43.3, y en todos los documentos/sobres).
- **Equipo:** Vicente Rosales (líder), Alex Alfaro, Samira Becerra, Manuel Aguilera, Martin Vasquez, Daniel Cepeda, Eliseo Guarda.

## Fuentes y precedencia

Los tres documentos de `00_Bases/` son la fuente de verdad. Orden de precedencia estricto (Art. 5° de las Bases Administrativas):

1. `00_Bases/Bases_Administrativas.md` — reglas del proceso y del contrato: participación, cronograma obligatorio de 56 meses, modelo de despliegue híbrido, hitos, formularios/sobres, evaluación y las 5 innovaciones obligatorias.
2. `00_Bases/Bases_Transversales.md` — requisitos técnicos comunes a las 13 industrias, codificados como **RT-CC.NN** (Obligatorio / Deseable / Según caso). Deben responderse uno a uno en el **Formulario T-12**.
3. `00_Bases/Caso_09_Cadena_Multitienda.md` — el caso en sí. **No es una especificación de requerimientos**: traducir su narrativa (dolores, contradicciones, vacíos) en alcance, arquitectura, plan y estrategia es exactamente lo que se evalúa.

Regla de precedencia: el caso puede **endurecer** un requisito transversal, nunca **rebajarlo**. Un requisito marcado "Según caso" se completa con la volumetría/valores del documento del caso (si el caso no lo define, rige el valor por defecto del transversal).

### Tablas de las Bases: incompletas, no se reparan por ahora

La extracción de los `.md` de `00_Bases/` perdió parte del contenido de las tablas. El caso más visible es la **ponderación del Formulario T-21** (`00_Bases/Bases_Administrativas.md:2366`): los porcentajes por ítem no se reconstruyen y la fila del Plan de Riesgos es ilegible.

**Regla:** no estimar ni hardcodear cifras que provengan de esas tablas. Dejarlas en blanco con una nota de pendiente que apunte al ítem del T-21. Cuando se reparen las tablas, se completan los maestros de `02_Propuesta/`.

Las **tablas del informe** quedan tal cual por la misma decisión: se arreglan en una etapa posterior.

## Reglas que condicionan todo el diseño

- **Despliegue híbrido obligatorio** (Art. 16): carga principal en nube pública + componentes on-premise. No se admiten propuestas solo-nube ni solo-on-premise.
- **Cronograma de 56 meses innegociable** (Art. 17): Etapa 1 (meses 1–15: desarrollo, marcha blanca, producción mes 16), Etapa 2 (meses 13–20, producción mes 21), Operación 36 meses (21–56). Salidas no negociables.
- **5 innovaciones obligatorias** (Cap. 5 Bases Admin), una por tipo, trazables con arquitectura, EDT y flujo de caja.
- **Línea roja del caso**: la compañía es simultáneamente una tienda y un **emisor de crédito fiscalizado** (dos negocios, dos regímenes jurídicos). Ninguna propuesta que los trate como uno solo o que borre la separación de sus datos será aceptada. Esto gobierna todas las decisiones de arquitectura de datos.
- El problema del caso **no es un sistema legado**, sino el tejido de 9 plataformas de 6 proveedores con 14 interfaces punto a punto y registros imprecisos (12,4% de discrepancia en conteo cíclico). Abordarlo como reemplazo de un sistema es un error conceptual.

## Carpetas

Estructura de pipeline: los prefijos numéricos declaran la etapa del flujo.

| Carpeta | Contenido |
| :--- | :--- |
| `00_Bases/` | Documentos rectores (ver precedencia arriba). **Inmutables**: son la fuente de verdad. |
| `01_Requerimientos/` | Catálogos de requerimientos en Excel. **Fuente oficial: `RequerimientosAtomizados_Depuracion_Alcance.xlsx`** (catálogo v3.0 renumerado y depurado: `RF-001`..`RF-226`, `RNF-01`..`RNF-76`, `OP-01`..`OP-09`), con hojas `6_Equivalencia_IDs` (mapeo de IDs viejos a nuevos) y `7_Depuracion_Alcance` (decisiones ELIMINAR / TRASLADAR / CONSOLIDAR / RECLASIFICAR / CONDICIONAR / REVISAR). `RequerimientosAtomizados.xlsx` (v2.1) y `RequerimientosHumanos.xlsx` (análisis original de personas) quedan en `historico/`. Espejos `.md` en `md/`. |
| `02_Propuesta/` | **Corazón del proyecto.** Los 14 subdocumentos del Formulario T-7, una carpeta `sd-NN_*/` por subdocumento. Ver "Cómo se escribe la propuesta". |
| `03_Formularios/` | Formularios oficiales de los sobres: `A/` (A-1..A-6), `B/` (T-6..T-22), `C/` (E-21..E-26). |
| `04_Adjuntos/` | Derivados que se citan desde la propuesta: `diagramas/` (exports PNG/SVG/PDF), `hardware/` (inventario a proveer), `tablas/` (cálculos de apoyo). |
| `05_Gestion/` | `jira/` con el plan de trabajo del proyecto `OSS`: `plan/`, `mapeo/`, `scripts/`, `historico/`. |
| `06_Informes/` | Los 3 informes y las 3 presentaciones preparatorias (Art. 45°): `informes/`, `presentaciones/`. |
| `07_Entregables/` | Salida final: `sobre_1_administrativo/`, `sobre_2_tecnico/`, `sobre_3_economico/`, `pdf_final/`. |
| `80_Artefactos/` | Material general del proyecto que no pertenece a una etapa: planilla de consultas al mandante, informes internos. |
| `90_Referencia/` | `TrabajosAnteriores_DistriProducto/`: fragmentos de un caso previo. **Solo referencia de forma.** |
| `.opencode/` | Skills versionadas, plugin `activar-skills.ts` y dependencias. `node_modules/` y `opencode-loop/` no se versionan. |

Cada carpeta del pipeline tiene un `README.md` con su propósito. Leer el de la carpeta antes de escribir en ella. Las subcarpetas no lo tienen: su propósito está en la tabla de arriba y en un `.gitkeep` comentado mientras están vacías.

## Convención de formato de los artefactos

**Regla:** todo artefacto de contenido se escribe en **`.md`** (o `.txt` para volcados de datos). Los binarios (`.xlsx`, `.docx`, `.pptx`, `.pdf`) existen **únicamente** como documento de lectura/entrega para el usuario o como export final.

**Consecuencia práctica:** todo capítulo, sección, formulario y cálculo económico se redacta primero en `.md` dentro de `02_Propuesta/`; los `.docx`/`.xlsx` de los sobres se generan al cierre.

**Exentos de la regla:** `*.py`, `*.ps1`, `*.json`, `*.csv` de `05_Gestion/` — son código y datos de máquina que consumen scripts, no documentos.

**Espejos:** cuando un `.xlsx` es la fuente oficial y además hay que leerlo con agentes, se genera un `.md` espejo. **Si el espejo y el Excel difieren, manda el Excel.** Los espejos se regeneran, no se editan a mano.

## Convención de nombres de los artefactos

| Tipo | Patrón | Ejemplo |
| :--- | :--- | :--- |
| Maestro de subdocumento | `sd-NN_titulo.md` | `sd-04_arquitectura-logica-y-fisica.md` |
| Texto de sección | `sd-NN_sN_titulo.md` | `sd-04_s2_arquitectura-fisica.md` |
| Adjunto | `sd-NN_sN_titulo.<ext>` | `sd-04_s2_inventario-hardware.xlsx` |
| Diagrama exportado | `diag-NN-SN_titulo.<ext>` | `diag-04-02_arquitectura-fisica.svg` |
| Formulario oficial | `form-<ID>_titulo.<ext>` | `form-T-12_matriz-cumplimiento-tecnico.xlsx` |

El prefijo + id oficial hace que el orden alfabético de los archivos coincida con el orden del informe.

## Cómo se escribe la propuesta

La Propuesta Técnica se estructura en **14 subdocumentos** (Formulario T-7, `00_Bases/Bases_Administrativas.md:2066`).

- Cada subdocumento es una carpeta `02_Propuesta/sd-NN_<titulo>/` con un **`.md` maestro** (identificación, contenido exigido por el T-7, tabla de secciones con estado, trazabilidad con Jira, adjuntos esperados y checklist) y **un archivo por sección**.
- El maestro es la **fuente de verdad del estado**: al empezar o terminar una sección, actualizar su fila en la tabla de secciones.
- `02_Propuesta/indice.md` es el índice general: los 14 subdocumentos, la cobertura por informe preparatorio, la convención de nombres y **las reglas de ensamblado** del documento final.
- Los números de sección del informe **no coinciden** con los del plan de Jira: mandan los del maestro.

### Informes preparatorios (Art. 45°)

Son tres informes y tres presentaciones, no uno. El `Informe 1` (en `06_Informes/informes/`) cubre los subdocumentos 1 a 5 y el 13; los subdocumentos 6 a 12 y el 14 corresponden a los informes 2 y 3.

## TrabajosAnteriores: cuándo consultarlos (solo referencia de forma)

Regla de uso: consultar **únicamente** para copiar la estructura de cada capítulo de la propuesta (títulos, orden de secciones, tablas, anexos). **Nunca** trasladar contenido: tecnologías, módulos, volúmenes, cifras ni servicios no aplican al caso actual (Cadena Multitienda). La fuente de verdad del contenido sigue siendo `00_Bases/`.

| Subdocumento | Capítulo (DistriProducto) | Cuándo ir a leerlo |
| :--- | :--- | :--- |
| `subdocumento_2.md` | Cap 3 — Alcance del Servicio | Para estructurar el alcance: contexto, problema, objetivos, entregables/hitos, módulos, ventajas/desventajas |
| `subdocumento_3.md` | Cap 4 — Descripción Lógica de la Solución | Para armar el capítulo de solución lógica: capas, módulos, arquitectura de bloques |
| `subdocumento_4.md` | Cap 5 — Descripción Física de la Solución | Para el capítulo físico: zonas/segmentación de red, infraestructura, especificaciones |
| `Subdocumento_6.md` | Cap 7 — Metodologías | Para estructurar metodología de gestión + desarrollo (PMBOK/ágil) |
| `Subdocumento_7.md` | Cap 8 — Plan de Trabajo | Para plantear EDT, carta gantt e implantación |
| `Subdocumento_8.md` | Cap 9 — Plan de Riesgo | Para RBS, análisis cualitativo/cuantitativo y plan de acción |
| `Subdocumento_9.md` | Cap 10 — Plan de Calidad | Para plan QA: gobernanza, niveles de prueba, métricas |
| `Subdocumento_10.md` | Cap 11 — Servicios de Operación | Para call center, SLA y soporte técnico |
| `Subdocumento_11.md` | Cap 12 — Planes en Operación | Para mantención preventiva/evolutiva |
| `Subdocumento_12.md` | Cap 13 — Equipo, Subcontrataciones y Alianzas | Para estructura organizacional, competencias y alianzas |

## Estado real del proyecto (leído del Jira el 2026-09-29)

- El plan de trabajo vive en el proyecto Jira `OSS`: **8 agrupadoras → 34 historias → 77 subtareas** (119 incidencias etiquetadas), más `OSS-250` como tarea suelta.
- Los 62 originales `OSS-105`..`OSS-164` **ya fueron borrados**; `05_Gestion/jira/historico/borrar_manual.txt` está obsoleto a propósito.
- La taxonomía de secciones del plan de Jira **no coincide** con el índice del Informe 1. Ver las observaciones de `02_Propuesta/indice.md`.
- Estado de redacción por subdocumento: los subdocumentos 1 a 3 están mayormente desarrollados; el 4 y el 5 tienen solo títulos; el 13 tiene la estructura de fichas sin contenido.

## Verificación

No hay build, test ni lint (solo markdown y Excel). La "verificación" del trabajo es la coherencia entre documentos: respetar la precedencia, trazabilidad de requerimientos (requisito RT → módulo → entregable) y consistencia de cifras/plazos con el cronograma obligatorio.

## Skills útiles y su activación

Las skills se cargan con la herramienta `skill`. El skill **`licitacion-workflow`** (`.opencode/skills/licitacion-workflow/`) es el orquestador: **cárgalo al iniciar cualquier avance de la propuesta**; indica qué skill activar en cada fase. El plugin **`.opencode/plugins/activar-skills.ts`** refuerza esa activación inyectándola en el prompt de sistema.

Nota: `opencode.jsonc` agrega el plugin `opencode-mermaid-renderer` (render ASCII de bloques Mermaid en la terminal). Requiere opencode ≥ 1.0.137 y **reiniciar opencode** tras cualquier cambio de config.

Skills del proyecto, **versionadas en `.opencode/skills/`** (openCode las detecta al clonar el repo, no dependen de la config global de cada máquina) y su fase:

| Skill | Uso en la propuesta |
| :--- | :--- |
| `licitacion-workflow` | Orquestación: qué skill activar en cada fase (cargar siempre) |
| `xlsx` | Requerimientos/volumetría, oferta económica (CLP/UF/USD) y flujo de caja (Excel) |
| `docx` | Llenar formularios/plantillas oficiales (.docx) de los sobres |
| `pptx` | Las 3 presentaciones preparatorias |
| `pdf-handling` | Conformar/exportar la propuesta final en PDF |
| `architecture-diagrams` | Diagramas de arquitectura (lógica/física/datos/seguridad/despliegue) |
| `cloud-architecture` | Justificar la arquitectura híbrida nube+on-premise (RT-03) |
| `sre-practices` | Disponibilidad 99,9%, RTO/RPO, SLOs, observabilidad |
| `project-estimation` | Estimación de esfuerzo y desglose por rol (nivelación T-15) |
| `legal-risk-assessment` / `risk-assessment` | Evaluación de riesgos contractuales y técnicos |
| `deep-research` | Investigar lo que el caso no explica (normativa, estándares, mercado) |
| `technical-writing` | Redacción de documentos técnicos extensos |
| `mermaid-diagrams` | Diagramas en Markdown (```mermaid```) que GitHub renderiza nativo; ver "Renderizado de diagramas" |
| `plantuml-diagrams` | Diagramas UML/C4 formales (.puml) renderizados a PNG/SVG vía Kroki (curl); ver "Renderizado de diagramas" |
| `jira-workflow` | Integración opcional con Jira Cloud: tomar tareas, marcarlas asignadas/en progreso/completadas, consultar sprint/board y comentar |

Nota: se eliminó la skill global `risk-manager-financiero` (era de trading financiero, no aplica al caso).

## Integración con Jira (opcional)

Este proyecto puede conectarse a **Jira Cloud** vía el servidor MCP oficial de Atlassian (Rovo) para gestionar tareas mientras se trabaja: **tomar una tarea, marcarla como asignada/en progreso/completada, consultar sprints/boards y registrar comentarios** — todo restringido a los permisos del usuario autenticado.

**Estado actual:** el bloque `mcp.jira` está en `opencode.jsonc` con `"enabled": true` y autenticado en esta máquina. Quien clone el repo sin cuenta **no queda bloqueado**: las herramientas `jira_*` solo aparecen tras autenticar, y el resto de las herramientas sigue disponible.

**Los agentes deben:** si notan tareas por gestionar o el servidor `jira` activo, **recomendar de forma proactiva** conectar/activar Jira y explicar cómo (pasos abajo). Si el usuario no tiene cuenta o el MCP está desactivado, **no bloquear el trabajo**: mencionarlo brevemente y seguir.

**Cómo activarlo (una vez por máquina/usuario):**

1. En `opencode.jsonc`, poner `"enabled": true` en el bloque `mcp.jira` (ya está así en el repo).
2. Reiniciar opencode (los cambios de MCP requieren reinicio).
3. Autenticar con el flujo OAuth de Atlassian (abre el navegador):
   ```bash
   opencode mcp auth jira
   ```
4. Verificar: `opencode mcp list`

Requisitos: cuenta **Jira Cloud**; endpoint oficial `https://mcp.atlassian.com/v1/mcp/authv2`; no se crea app en Atlassian (Dynamic Client Registration). El token OAuth se guarda localmente en `~/.local/share/opencode/mcp-auth.json` y **nunca en el repositorio**.

Para el flujo "tomar tarea → marcarla → completar al cerrar", cargar el skill **`jira-workflow`** (`.opencode/skills/jira-workflow/`).

## MCP de búsqueda documental: `ragdocs`

`opencode.jsonc` declara un segundo servidor MCP, **`ragdocs`** (`mcp-server-ragdocs`), que indexa documentación en una base de vectores **Qdrant Cloud** y permite buscar por significado en lugar de por palabra clave. Es la herramienta para preguntas como "¿dónde dice el caso que el inventario discrepa?" en lugar de leer 3.000 líneas de `.md`.

**Viene en `enabled: false`**: no arranca hasta que exista la configuración. Para activarlo:

1. Copiar `.env.example` a `.env` y completar `QDRANT_URL` y `QDRANT_API_KEY` (del dashboard de Qdrant Cloud) más las variables del proveedor de embeddings.
2. Poner `"enabled": true` en el bloque `mcp.ragdocs` de `opencode.jsonc` y reiniciar opencode.

**Reglas de uso:**

- **Indexar solo texto**: el servidor no lee `.xlsx`, `.docx` ni `.pdf`. Se indexan `00_Bases/`, los espejos `.md` de `01_Requerimientos/` y `02_Propuesta/**`. Para indexar un Excel, usar antes su espejo `.md`.
- **La base vectorial es caché, no fuente de verdad.** Toda respuesta se contrasta contra el archivo original: el RAG puede devolver un fragmento descontextualizado o de una versión vieja del documento. Para citar en la propuesta, abrir el archivo y confirmar la línea.
- **Nunca indexar material sensible**: el Formulario A-1 y los datos de la contraparte quedan fuera.
- Las claves van por `{env:...}` en `opencode.jsonc`; los valores viven en `.env`, que está en `.gitignore`.

## Renderizado de diagramas

Regla de selección:

| Tipo de diagrama | Herramienta | Dónde se ve | Export para `.docx`/`.pdf` |
| :--- | :--- | :--- | :--- |
| Flujo, arquitectura, secuencia, ER, C4 de la propuesta | **Mermaid** (bloque ```mermaid``` en el `.md`) | **GitHub renderiza nativo** → todo el equipo lo ve en la web sin tooling | `npx -y @mermaid-js/mermaid-cli` → `mmdc -i archivo.mmd -o archivo.svg/png/pdf` |
| UML/C4 formal, componente, secuencia estricta | **PlantUML** (`.puml`) | GitHub **no** lo renderiza: exportar siempre a imagen | `curl https://kroki.io/plantuml/png -d 'diagram_source=...'` (o kroki docker local) |
| Diagrama interactivo/animado (presentaciones, sobres) | **`architecture-diagrams`** | HTML en navegador (GitHub no lo muestra) | screenshot del HTML → PNG |

Convención: la **fuente de los diagramas es texto** dentro de los `.md` de la propuesta (versionable y revisable en PR). Los **PNG/SVG/PDF exportados** se guardan en `04_Adjuntos/diagramas/` y de ahí se incrustan en Word (`docx`) y en el PDF final (`pdf-handling`). Usar Mermaid por defecto; reservar PlantUML para UML/C4 formales y `architecture-diagrams` para lo interactivo.
