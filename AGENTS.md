# AGENTS.MD

## Qué es este proyecto

Proyecto de universidad (PUCV, Escuela de Informática — Taller de Formulación de Proyectos Informáticos, ICI-5444). El objetivo es redactar la propuesta técnico-económica para una licitación pública **ficticia** (Licitación N° TFEP-01/2026) del caso asignado: **Caso 09 — Cadena Multitienda** (Multitiendas Ancoa S.A.).

Todo el trabajo se desarrolla en **español** (idioma oficial de la licitación). La salida esperada es documentación tipo oferta (arquitectura, servicios, requerimientos, planificación, evaluación de riesgos), no código.

## Identidad del proponente

- **Empresa proponente:** Only Simple Solutions (usar en columna B de la planilla de consultas, nomenclatura de archivos Art. 43.3, y en todos los documentos/sobres).
- **Equipo:** Vicente Rosales (líder), Alex Alfaro, Samira Becerra, Manuel Aguilera, Martin Vasquez, Daniel Cepeda, Eliseo Guarda.

## Fuentes y precedencia

Los tres documentos de `Bases/` son la fuente de verdad. Orden de precedencia estricto (Art. 5° de las Bases Administrativas):

1. `Bases/Bases_Administrativas.md` — reglas del proceso y del contrato: participación, cronograma obligatorio de 56 meses, modelo de despliegue híbrido, hitos, formularios/sobres, evaluación y las 5 innovaciones obligatorias.
2. `Bases/Bases_Transversales.md` — requisitos técnicos comunes a las 13 industrias, codificados como **RT-CC.NN** (Obligatorio / Deseable / Según caso). Deben responderse uno a uno en el **Formulario T-12**.
3. `Bases/Caso_09_Cadena_Multitienda.md` — el caso en sí. **No es una especificación de requerimientos**: traducir su narrativa (dolores, contradicciones, vacíos) en alcance, arquitectura, plan y estrategia es exactamente lo que se evalúa.

Regla de precedencia: el caso puede **endurecer** un requisito transversal, nunca **rebajarlo**. Un requisito marcado "Según caso" se completa con la volumetría/valores del documento del caso (si el caso no lo define, rige el valor por defecto del transversal).

## Reglas que condicionan todo el diseño

- **Despliegue híbrido obligatorio** (Art. 16): carga principal en nube pública + componentes on-premise. No se admiten propuestas solo-nube ni solo-on-premise.
- **Cronograma de 56 meses innegociable** (Art. 17): Etapa 1 (meses 1–15: desarrollo, marcha blanca, producción mes 16), Etapa 2 (meses 13–20, producción mes 21), Operación 36 meses (21–56). Salidas no negociables.
- **5 innovaciones obligatorias** (Cap. 5 Bases Admin), una por tipo, trazables con arquitectura, EDT y flujo de caja.
- **Línea roja del caso**: la compañía es simultáneamente una tienda y un **emisor de crédito fiscalizado** (dos negocios, dos regímenes jurídicos). Ninguna propuesta que los trate como uno solo o que borre la separación de sus datos será aceptada. Esto gobierna todas las decisiones de arquitectura de datos.
- El problema del caso **no es un sistema legado**, sino el tejido de 9 plataformas de 6 proveedores con 14 interfaces punto a punto y registros imprecisos (12,4% de discrepancia en conteo cíclico). Abordarlo como reemplazo de un sistema es un error conceptual.

## Carpetas

- `Bases/` — documentos rectores (ver precedencia arriba).
- `Requerimientos/` — dos archivos Excel: `RequerimientosHumanos.xlsx` (análisis hecho por personas) y `RequerimientosAtomizados.xlsx` (versión atomizada/desglosada de la anterior). **Preferir el atomizado** como base para el trabajo de requerimientos.
- `productos/` — salidas entregables: consultas al mandante (`.docx`), planilla de consultas con nomenclatura Art. 43.3 (`.xlsx`) y registro de decisiones del caso (`.xlsx`).
- `TrabajosAnteriores/` — 10 subdocumentos de un **caso previo distinto** (DistriProducto, industria de logística/bodegas — WMS/TMS/YMS). Son fragmentos (índice + introducción) que solo sirven de **referencia de forma**; cada subdocumento N corresponde al capítulo N+1 de aquella propuesta.
- `.opencode/` — configuración local de opencode: skills versionadas (`.opencode/skills/`), plugin `activar-skills.ts` y dependencias. `node_modules/` y `opencode-loop/` (sesiones locales) no se versionan (ver `.gitignore`).
- `Diagramas/` — PNG/SVG/PDF exportados de diagramas (Mermaid/PlantUML) para incrustar en `.docx` y PDF final. La fuente de los diagramas vive en los `.md` (ver "Renderizado de diagramas"). Este archivo `.gitkeep` solo marca la convención.

### TrabajosAnteriores: cuándo consultarlos (solo referencia de forma)

Regla de uso: consultar **únicamente** para copiar la estructura de cada capítulo de la propuesta (títulos, orden de secciones, tablas, anexos). **Nunca** trasladar contenido: tecnologías, módulos, volúmenes, cifras ni servicios no aplican al caso actual (Cadena Multitienda). La fuente de verdad del contenido sigue siendo `Bases/`.

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

Nota: se eliminó la skill global `risk-manager-financiero` (era de trading financiero, no aplica al caso).

## Renderizado de diagramas

Regla de selección:

| Tipo de diagrama | Herramienta | Dónde se ve | Export para `.docx`/`.pdf` |
| :--- | :--- | :--- | :--- |
| Flujo, arquitectura, secuencia, ER, C4 de la propuesta | **Mermaid** (bloque ```mermaid``` en el `.md`) | **GitHub renderiza nativo** → todo el equipo lo ve en la web sin tooling | `npx -y @mermaid-js/mermaid-cli` → `mmdc -i archivo.mmd -o archivo.svg/png/pdf` |
| UML/C4 formal, componente, secuencia estricta | **PlantUML** (`.puml`) | GitHub **no** lo renderiza: exportar siempre a imagen | `curl https://kroki.io/plantuml/png -d 'diagram_source=...'` (o kroki docker local) |
| Diagrama interactivo/animado (presentaciones, sobres) | **`architecture-diagrams`** | HTML en navegador (GitHub no lo muestra) | screenshot del HTML → PNG |

Convención: la **fuente de los diagramas es texto** dentro de los `.md` de la propuesta (versionable y revisable en PR). Los **PNG/SVG/PDF exportados** se guardan en `Diagramas/` y de ahí se incrustan en Word (`docx`) y en el PDF final (`pdf-handling`). Usar Mermaid por defecto; reservar PlantUML para UML/C4 formales y `architecture-diagrams` para lo interactivo.
