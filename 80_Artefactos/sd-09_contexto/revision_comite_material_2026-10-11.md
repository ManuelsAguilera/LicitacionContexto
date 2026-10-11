---
tipo: informe-interno
parte: T7-09
estado: diagnostico
actualizado: 2026-10-11
---

# Revisión material del Subdocumento 9 desde un lector del comité de Ancoa

Se aplicó la skill [`revisor-comite-ancoa`](../../.agents/skills/revisor-comite-ancoa/SKILL.md). Su [índice de rúbricas](../../.agents/skills/revisor-comite-ancoa/referencias/rubricas-t7.md) condujo al [apartado del Subdocumento 9](../../00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md#L879) del Comunicado 10. Esta es una simulación editorial, no una aceptación del CLIENTE. No se editó la propuesta. La revisión no juzga colores, tipografía, páginas, plantilla ni densidad visual por sí sola.

**Versión examinada.** [Fuente canónica](../../02_Propuesta/latex_final/sd-09/OSS-Subdocumento9.tex), SHA-256 `e17f1a93aa54cf98b0a9dd88f21470e95d1ae08a1b4a8b11e8bf22e45bfa0c5b`; [PDF de vista previa](../../05_Gestion/reportes/vistas_previas/T7-09_latex_preview.pdf), SHA-256 `ca452f265edf7f5ce785e1d3625efd0d8bec442aee4ccfacecbcef3aa600ae03`. Se leyeron el capítulo completo y sus tres figuras, y se contrastaron las afirmaciones de aceptación con las Bases Administrativas, las Transversales y el Caso 09. Las líneas siguientes son del `.tex`.

## Cobertura de la rúbrica

| Exigencia del Comunicado 10 | Resultado de lectura |
| :--- | :--- |
| Introducción y remisiones a anexos/formularios | Presentes: propósito, relación con otros subdocumentos y T-13/T-17 (`.tex` L91–95). |
| 9.1 Marco ISO/IEC 25010, madurez, métricas y umbrales bloqueantes | Desarrollados. Se elige explícitamente CMMI nivel 3 como **meta**, sin presentarlo como acreditación obtenida; la cobertura, complejidad y acoplamiento tienen reglas de bloqueo (`.tex` L107–117, L194–224). |
| 9.2 Puertas, pares, análisis, pruebas según 29119, verificación, validación y trazabilidad | Desarrollados con ambientes, datos, automatización, criterios y responsables (`.tex` L240–341). Quedan dos ambigüedades de representación de autoridad señaladas abajo. |
| 9.3 Actividades de calidad en EDT y cronograma del capítulo 7 | Se nombran las ramas y los hitos; el texto coincide en lo esencial con el cronograma del capítulo 7 (`.tex` L343–403). La relación simultánea entre rama, producto, responsable y hito exige reconstrucción de varios párrafos. |

No se identificó un título obligatorio ausente. Las propuestas de tablas siguientes se limitan a resumir relaciones que el capítulo ya describe; los casos y protocolos detallados deben permanecer en T-13 y T-17. No se justifica agregar otra subsección ni otra figura en esta pasada.

## Hallazgos comprobados

| ID · prioridad · categoría | Ubicación y contraste | Consecuencia para Ancoa y cambio concreto |
| :--- | :--- | :--- |
| **C01 · alta · corrección** | [Tabla 9.1, L130](../../02_Propuesta/latex_final/sd-09/OSS-Subdocumento9.tex#L130): «100 % aprobados y firmados» para los casos de aceptación. En [L321 y L329–331](../../02_Propuesta/latex_final/sd-09/OSS-Subdocumento9.tex#L321), QA revisa casos y la Contraparte acepta el **entregable o hito** mediante acta. [Bases Administrativas, art. 18.1–18.2](../../00_Bases/Bases_Administrativas.md#L493). Rúbrica C10, [9.1–9.2](../../00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md#L885). | La tabla sugiere que la Contraparte debe firmar individualmente cada caso, aunque el procedimiento desarrollado firma el acta del hito. Separar el resultado de los casos de la autoridad contractual: «100 % de casos aplicables aprobados; entregable aceptado por acta de la Contraparte». |
| **C02 · alta · figura** | [Figura 9.1, L197–205](../../02_Propuesta/latex_final/sd-09/OSS-Subdocumento9.tex#L197) presentaba «Dueño de dato Ancoa» también dentro de «Emisor fiscalizado», mientras «Datos ejecuta · QA verifica» no identificaba a OSS. El ciclo inferior decía «QA valida resultado», aunque el texto reserva la conformidad de negocio al dueño de cada dominio. El [Caso 09 distingue la filial emisora](../../00_Bases/Caso_09_Cadena_Multitienda.md#L663). Rúbrica C10, [9.1 y reglas de figuras §4](../../00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md#L885). | La figura podía atribuir a Ancoa Retail la decisión sobre datos de la filial o a QA la validación funcional. En la figura actual se nombran por separado los responsables de negocio, Datos (OSS) y QA (OSS); el texto reserva la conformidad al dueño del dominio y la aceptación del hito a la Contraparte. |
| **C03 · alta · figura** | [Figura 9.2, L282–294](../../02_Propuesta/latex_final/sd-09/OSS-Subdocumento9.tex#L282) dibujaba una cadena única «Cambio → CI → QA → Preprod → Acta → Producción». El texto de L294 aclara que el acta corresponde a hitos contractuales, no a cada integración. [Bases Administrativas, art. 18.1](../../00_Bases/Bases_Administrativas.md#L493). Rúbrica C10, [9.2 y §4](../../00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md#L891). | El circuito central podía interpretarse como una firma de Ancoa por cada versión ordinaria. La figura actual separa el flujo técnico de la ruta condicional del acta para el paso de etapa y conserva la explicación textual del retorno ante fallas. |
| **C04 · alta · corrección** | [L441 y L443](../../02_Propuesta/latex_final/sd-09/OSS-Subdocumento9.tex#L441) hablaban de «fórmulas o ponderaciones ilegibles de las tablas extraídas» y de no trasladar «una recepción provisional, retención o plazo tomado de ejemplos externos». Rúbrica C10, [9.3](../../00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md#L907) y [§7.1.d sobre notas internas en la oferta](../../00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md#L344). | Se retiraron esas notas internas. El texto ahora explica que Calidad aporta evidencia y seguimiento de acciones, mientras la Contraparte y el Administrador del Contrato aplican el procedimiento contractual. |
| **C05 · alta, antes de entregar · tabla** | La [Declaración de uso de IA, L454–464](../../02_Propuesta/latex_final/sd-09/OSS-Subdocumento9.tex#L454) contenía solo un párrafo. El [Comunicado 10, §7.2](../../00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md#L354) exige, además del texto breve, una tabla con una fila por sección y por anexo o formulario asociado, y columnas para herramienta, finalidad, niveles de uso y revisión humana. | La declaración actual incluye la tabla y registra que la revisión humana no se ha realizado. Aún debe cotejarse con los formularios asociados y con A-6 antes de presentar. |
| **C06 · alta, antes de entregar · corrección** | El [párrafo de declaración, L457](../../02_Propuesta/latex_final/sd-09/OSS-Subdocumento9.tex#L457) indica con claridad que no se reporta revisión humana de las secciones en esta versión. [Comunicado 10, §7.1–7.2](../../00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md#L326). | Sigue sin cerrarse: una persona del equipo debe revisar contenido, cifras, decisiones y figuras, y registrar qué comprobó por sección. Después habrá que actualizar la tabla de declaración y cotejar A-6. No inventar que esa revisión ocurrió. |

## Estructuras recomendadas

| ID · prioridad · categoría | Ubicación y justificación | Contenido propuesto |
| :--- | :--- | :--- |
| **S01 · media · tabla** | [9.1.3, L167–190](../../02_Propuesta/latex_final/sd-09/OSS-Subdocumento9.tex#L167): había responsabilidades de OSS, dueños de dominio y Contraparte repartidas entre varios párrafos. La [rúbrica 9.1 y 9.2](../../00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md#L885) requiere que la autoridad de revisión y avance pueda evaluarse. | Tabla 9.3 añadida con cuatro columnas para control, ejecución, verificación y conformidad/aceptación. El párrafo posterior distingue la recomendación técnica, la conformidad del dominio y la aceptación contractual; T-13/T-17 conservan el detalle. |
| **S02 · media · tabla** | [9.3.1, L372–397](../../02_Propuesta/latex_final/sd-09/OSS-Subdocumento9.tex#L372): la rama EDT, su producto de calidad y el mes/hito aparecían en pasajes separados. La [rúbrica 9.3](../../00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md#L907) pide mostrar dónde quedan esas actividades en la EDT y el cronograma del capítulo 7. | Tabla 9.4 añadida con ramas 1.7, 1.8, 1.9, 1.12 y 1.15, sus productos, ventanas e intervinientes, cotejados con el [capítulo 7](../../02_Propuesta/latex_final/sd-07/OSS-Subdocumento7.tex#L97). El texto aclara que la tabla resume T-14/T-15 y no sustituye hitos ni condiciones de aceptación. |

## Seguimiento de la mejora

| ID | Estado después de la edición |
| :--- | :--- |
| C01 | Corregido en la Tabla 9.1: se exige aprobar los casos y aceptar el hito mediante acta. |
| C02 | Corregido en la Figura 9.1 y su explicación: se distinguen Retail, filial emisora, equipo de OSS, QA y Contraparte. |
| C03 | Corregido en la Figura 9.2: el acta aparece como requisito del paso de etapa; el flujo técnico queda separado. |
| C04 | Corregido en 9.3.3: retiradas las dos frases sobre tablas ilegibles y ejemplos externos, y aclarado quién aplica el procedimiento contractual. |
| C05 | Estructura de la declaración y tabla requeridas por C10 §7.2 añadidas. Se registra el uso de IA y que aún no hay revisión humana. T-13/T-17 y A-6 deben cotejarse al integrar esos formularios. |
| C06 | No puede cerrarse aquí: la revisión humana real de cada sección no se ha realizado y no se atribuye a nadie. Debe hacerla el equipo antes de presentar la oferta y actualizarse la declaración y el A-6. |
| S01 | Tabla 9.3 de responsabilidades añadida en 9.1.3. |
| S02 | Tabla 9.4 de EDT, productos, ventanas y responsables añadida en 9.3.1. |

La fuente canónica pasó `exportar_latex.py verificar` y compiló como vista previa PDF de 24 páginas. `verificar-redaccion` reporta una excepción: la tabla obligatoria de uso de IA tiene seis columnas, como pide C10 §7.2; el máximo de cinco de RR-17 y C10 §5 se aplica a las tablas del cuerpo. El mismo reporte incluye avisos heurísticos de título de tabla y proporción de tablas en la sección de declaración, que no sustituyen la revisión manual.

Versión compilada después de los cambios: `.tex` SHA-256 `0be743e7d51a2b4b92858913fdc3a726c758ed23e95d6060c82b8204aa05ca8d`; PDF SHA-256 `e402b88f1352ce9a4cc0012f6940b0a75cdd754c500d5dfc55f46dc10de38bb6`.

**Orden de tratamiento restante.** Completar la revisión humana de las secciones y los formularios asociados, cotejar la declaración con A-6 y cerrar la revisión de contenido antes de presentar la oferta. La skill no cambia el estado del subdocumento por sí sola.

El [registro anterior](revision_lectura_comite_ancoa_2026-10-11.md) permanece como antecedente histórico y no forma parte de esta selección de hallazgos.
