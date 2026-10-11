---
tipo: informe-interno
parte: T7-09
estado: borrador
actualizado: 2026-10-11
---
# Matriz interna de cobertura, verificación y aceptación de SD09

La matriz prepara el Plan de Calidad y el Plan de Pruebas. Es un instrumento de análisis para el equipo; no constituye aprobación, certificación ni evidencia de pruebas ejecutadas. El alcance de esta primera versión son los 28 resultados del Anexo D y las obligaciones transversales pertinentes identificadas en las fichas. No acredita cobertura completa de todos los RF, RNF, OP o RT del proyecto.

Se lee en tres vistas enlazadas. [Cobertura](cobertura.md) relaciona resultado, fuente y servicio/diseño; [verificación](verificacion.md) permite localizar escenarios, métodos, umbrales y evidencia prevista; [aceptación](aceptacion.md) organiza calendario, responsables y dependencias. Las decisiones pendientes están en [brechas](brechas.md). Las fichas sustantivas viven en [resultados](resultados.md), [pilotos](pilotos.md) y [transversales](transversales.md); las vistas remiten a ellas para evitar repetir requisitos y tablas extensas.

La [propuesta de figuras](propuesta_figuras.md) ubica dos esquemas visuales en las secciones 9.2 y 9.3 del futuro capítulo, con alternativas de composición, fuentes y controles de legibilidad.

El [plan de reescritura](plan_reescritura.md) define contenido por sección, secuencia de integración, equipo Sol/Luna y criterios de terminado para convertir la matriz en el SD09 definitivo.

R01–R28 identifica resultados originales por número. Tnn identifica agrupaciones internas de obligaciones. C-Rnn-mm y C-Tnn-mm identifica criterios de prueba internos. Estos códigos no son IDs RF/RNF/RT oficiales y no reemplazan el catálogo. Las síntesis referencian criterios; su definición pertenece a una sola ficha. Una misma prueba puede apoyar varios resultados, pero debe conservar trazabilidad individual a cada criterio.

## Fuentes y límites de precedencia

Las Bases Administrativas, Transversales y Caso rigen en ese orden; el Comunicado 10 gobierna estructura. El Caso puede endurecer el transversal. El diseño vigente se consulta en `02_Propuesta/latex_final/`; los Markdown de propuesta son contexto. El [README de requerimientos](../../01_Requerimientos/README.md) conserva v3.0 como catálogo oficial; v3.1 es borrador conciliado, fuente del Anexo B, pendiente de decisión del equipo. Se leyó cada Excel directamente con openpyxl; los libros no se modificaron.

La fuente oficial v3.0 está en [Excel v3.0](../../01_Requerimientos/RequerimientosAtomizados_Depuracion_Alcance.xlsx), hoja `1_Catalogo_Atomico`. La asignación conciliada de servicios/etapas y el Anexo B se contrasta con [Excel v3.1](../../01_Requerimientos/RequerimientosAtomizados_Depuracion_Alcance_v3.1.xlsx), hoja `1_Catalogo_Vigente`. Los seis pilotos registran filas exactas de ambas versiones para los IDs utilizados. Los demás resultados conservan los IDs citados por Anexo D como relación de fuente, sin afirmar haber verificado exhaustivamente equivalencias o todos sus textos en ambos libros. La descripción del Anexo B menciona v3.0 como origen de generación; debe conciliarse con el README y el libro v3.1 antes de fijar línea base.

La ventana de tres meses para tasas anuales y la recuperación histórica propuesta son decisiones del Anexo D, sujetas a validación, no reinterpretaciones de los máximos del Caso. No convertir 104.000 pedidos en tres días en TPS peak, ni usar percentiles para rebajar máximos. El ensayo debe declarar perfil presencial y digital por separado. Los hitos de producción permanecen en meses 16 y 21 y la operación acaba en mes 56. Enero de 2027 y mes 24/diciembre de 2028 son supuestos del Anexo D, no fechas adjudicadas.

## Cómo usar y cerrar la matriz

QA mantiene versión, dueño y estado de cada criterio. Arquitectura y responsables del negocio resuelven las brechas antes de diseñar campañas. Cada ejecución futura registra versión, ambiente, datos, método, esperado/obtenido, resultado, evidencia y defectos. La Contraparte Técnica revisa el expediente y firma cuando corresponde; el proponente conserva observaciones y correcciones. La matriz requiere revisión humana y completar catálogo, formularios T-12/T-13 y diseños aún pendientes antes de pretender cobertura total de etapa.

Se aplicaron `licitacion-workflow`, `xlsx`, `technical-writing` y `humanizer`, con alcance formal de RR-24. Elaboración y revisión asistidas por OpenAI Codex: principal Sol, agentes Luna para resultados, obligaciones y revisión independiente; nivel de texto Alto, diagramas Ninguno. La revisión humana no ha ocurrido. La revisión independiente entre agentes identifica errores documentales; no cambia el estado `borrador` a `revisado`.

## Referencias metodológicas

[NASA, Appendix D: Requirements Verification Matrix](https://www.nasa.gov/reference/appendix-d-requirements-verification-matrix/) orienta la separación de requisito, método y evidencia; [ISTQB CTFL v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf) orienta trazabilidad y diseño de pruebas; [SEI, Quality Attribute Workshop Collection](https://www.sei.cmu.edu/library/quality-attribute-workshop-collection/) orienta escenarios de atributos de calidad. Estas referencias metodológicas no aportan umbrales contractuales de Ancoa. La investigación fue provista por la coordinación; esta matriz conserva los enlaces sin declarar certificación o validación externa.

Resultado de revisión: [verificación documental y conteos](verificacion_documental.md).
