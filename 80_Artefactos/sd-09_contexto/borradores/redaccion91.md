---
tipo: borrador-de-seccion
parte: T7-09
estado: borrador
actualizado: 2026-10-11
---

# Introducción

Este capítulo establece cómo Only Simple Solutions planificará, asegurará y medirá la calidad de los productos y del trabajo que los genera durante las dos etapas de implementación y la operación contractual. Su propósito es que cada incremento y entregable de Ancoa cumpla los requisitos aprobados y llegue a sus hitos con evidencia revisable. El plan conecta las prácticas de desarrollo y DevSecOps del Subdocumento 6 con la arquitectura, los riesgos y el plan de trabajo de los Subdocumentos 4, 8 y 7. El Formulario T-13 desarrollará el plan y los casos de prueba; el T-17 detallará el protocolo de aceptación.

La calidad se observará tanto en el producto como en el proceso. En Ancoa, esto incluye verificar las reglas de venta, inventario y crédito, además de preservar la separación entre Retail y el Emisor fiscalizado en datos, accesos e integraciones. Las mediciones y revisiones producirán registros por versión, ambiente y requisito. Son mecanismos de control previstos, no resultados de pruebas ya ejecutadas ni una declaración de certificación del producto.

## 9.1 Plan de Calidad

El plan convierte los compromisos de las Bases en criterios de trabajo y mediciones para requisitos, arquitectura, código, datos, pruebas y entregas. La calidad es el grado en que el producto satisface los requisitos acordados; el grado describe el conjunto de prestaciones y capacidades elegido para el producto. Por ello, una decisión de alcance puede definir qué funciones se incluyen, pero no reduce la obligación de que cada función comprometida opere conforme a sus criterios. El plan cubre la calidad del proceso, que se controla con prácticas repetibles y revisiones, y la calidad del producto, que se verifica mediante pruebas, inspecciones y métricas. Prevención y evaluación se incorporan al trabajo; la corrección atiende defectos detectados antes o después de una entrega.

### Marco de calidad y características del producto

El Artículo 24 de las Bases Administrativas requiere un marco basado en ISO/IEC 25010 y modelos de madurez, métricas y puertas de calidad. Sus criterios enumeran ocho características con la terminología de la edición 2011: funcionalidad, desempeño, compatibilidad, usabilidad, fiabilidad, seguridad, mantenibilidad y portabilidad. Para organizar la evaluación vigente se utilizará ISO/IEC 25010:2023, que define nueve características del modelo de calidad del producto. La correspondencia mantiene las ocho dimensiones contractuales y las interpreta con los nombres actualizados; capacidad de interacción recoge la dimensión antes denominada usabilidad, flexibilidad recoge la anterior portabilidad y seguridad de funcionamiento completa el modelo 2023. Esta correspondencia no elimina ni rebaja ningún criterio de las Bases.

En Ancoa, la adecuación funcional comprobará los flujos de venta, inventario y crédito; la eficiencia de desempeño se medirá bajo los perfiles y cargas establecidos en las Bases; la compatibilidad cubrirá interfaces con las plataformas que permanecen; la capacidad de interacción atenderá los puestos de tienda y los procesos de atención; la fiabilidad cubrirá disponibilidad y recuperación; la seguridad verificará acceso, integridad y segregación entre Retail y Emisor; la mantenibilidad considerará pruebas y estructura del código; la flexibilidad observará adaptación y escalamiento; y la seguridad de funcionamiento evaluará el comportamiento seguro ante fallas que puedan afectar personas, bienes u operación. Los objetivos numéricos se derivan de las Bases o de decisiones documentadas del proyecto, no del modelo ISO por sí solo.

ISO/IEC 25010 es un modelo para estructurar requisitos y evaluación del producto, no una certificación del software. Los modelos de madurez se emplearán como referencias para revisar y mejorar prácticas de proceso, identificando modelo, escala, alcance y evidencia antes de asignar una calificación. No se atribuye a Only Simple Solutions ni al proyecto un nivel CMMI, una certificación de madurez o una evaluación externa no acreditada. Las certificaciones exigidas a la empresa o a integrantes del equipo se acreditan por los mecanismos y formularios establecidos en las Bases, y no demuestran por sí mismas la calidad de una versión de Ancoa.

### Gobierno, responsabilidades y evidencia

El Líder de Calidad y Pruebas mantendrá el plan, la matriz de criterios, las métricas y el expediente de cada versión. Desarrollo implementará revisiones por pares y corregirá defectos; Arquitectura definirá con los responsables técnicos los criterios estructurales; Seguridad verificará controles y hallazgos; Datos y los responsables funcionales validarán reglas, calidad de información y resultados de negocio. El Jefe de Proyecto integrará estas evaluaciones con los hitos. La Contraparte Técnica de Ancoa revisará la evidencia y emitirá las conformidades que le corresponden; la aceptación contractual no se delega al equipo proponente.

Cada medición o prueba conservará requisito relacionado, versión, ambiente, datos y condiciones de ejecución, método, resultado esperado y obtenido, evidencia, defectos y resolución. La matriz interna de SD09 organiza 115 criterios asociados a 28 resultados del Anexo D y obligaciones transversales identificadas. Es una base de trabajo parcial; no representa cobertura total del catálogo RF/RNF/RT ni acredita pruebas ejecutadas. T-13 y T-17 contendrán el detalle verificable y el protocolo de aceptación, respectivamente.

### Métricas y puertas del código

La integración continua bloqueará el cambio si la cobertura automatizada del código de lógica de negocio es inferior a 70 %, conforme a RT-04.11 de las Bases Transversales. SD06 establece además como objetivo de calidad alcanzar al menos 80 % en código nuevo de lógica de negocio, medido de forma independiente; este objetivo no sustituye ni compensa el mínimo contractual. La medición documentará herramienta, unidad cubierta, población y exclusiones justificadas.

SD06 también fija como política de Only Simple Solutions una razón de deuda técnica no superior a 5 % y duplicación de código no superior a 3 %. La razón de deuda se calculará como esfuerzo estimado de remediación respecto del esfuerzo de desarrollo del código evaluado; la duplicación declarará población, unidad y exclusiones. Antes de aplicar el bloqueo se dejarán fijados el método, la herramienta y la evidencia. Son compromisos internos de SD06, no umbrales impuestos textualmente por las Bases.

Las Bases Administrativas requieren umbrales bloqueantes para complejidad y acoplamiento, pero no entregan valores numéricos. Para complejidad se usará análisis estático de complejidad ciclomática por función o método y revisión de unidades que excedan el límite aprobado; para acoplamiento se evaluará el grafo de dependencias entre módulos y servicios, incluidos los ciclos y las dependencias entrantes y salientes. Arquitectura y Calidad fijarán los valores bloqueantes y excepciones justificadas por tipo de componente antes de habilitar la puerta correspondiente, mediante una decisión registrada y reproducible en el pipeline. La decisión considerará línea base medida, límites de módulo y consecuencias para mantenibilidad, pruebas y despliegue independiente. Hasta que se aprueben esos valores, no se afirmará que existe un umbral numérico acordado ni se presentará la métrica como condición contractual ya satisfecha.

| Indicador | Criterio de control | Tratamiento |
| :--- | :--- | :--- |
| Cobertura automatizada de lógica de negocio | ≥70 % | Mínimo contractual bloqueante en integración continua. |
| Cobertura de código nuevo de lógica de negocio | ≥80 % | Objetivo adicional de SD06, medido por separado. |
| Razón de deuda técnica | ≤5 % | Política SD06; fórmula y población documentadas antes del bloqueo. |
| Duplicación de código | ≤3 % | Política SD06; unidad, población y exclusiones declaradas. |
| Complejidad ciclomática | Umbral numérico por aprobar antes de activar la puerta | Métrica por función/método; análisis estático y excepciones justificadas. |
| Acoplamiento entre componentes | Umbral numérico por aprobar antes de activar la puerta | Grafo de dependencias, ciclos y dependencias entrantes/salientes. |

Las métricas se interpretarán junto con el riesgo funcional y de operación. En un servicio que procese transacciones del Emisor, por ejemplo, un promedio favorable no compensará una ruta crítica sin pruebas ni una dependencia que rompa la segregación. La puerta registra la condición de avance y el motivo de cualquier excepción permitida; las obligaciones contractuales de seguridad y calidad no se dispensan mediante una decisión interna.

### Planificación del costo de calidad

El esfuerzo de calidad se incorporará en la EDT, las estimaciones y la capacidad de cada etapa, incluyendo prevención, revisión, automatización, pruebas, corrección y estabilización. El costo de calidad (COQ) se observará mediante costos de prevención y evaluación, y de fallas internas y externas, con datos propios del proyecto cuando estén disponibles. No se impondrá un porcentaje fijo del presupuesto como objetivo ni se trasladarán estimaciones sectoriales a Ancoa. Los registros servirán para identificar retrabajo, fallas y oportunidades de prevención; no alterarán por sí mismos el alcance ni los hitos contractuales.

## Referencias

Bases Administrativas de la Licitación TFEP-01/2026, Artículo 24 y estructura del Subdocumento 9.

Bases Técnicas Transversales de la Licitación TFEP-01/2026, RT-04.11.

Only Simple Solutions. (2026). *Subdocumento 6: Metodologías*, secciones 6.1.2, 6.2.3.2–6.2.3.3 y 6.2.5.

ISO/IEC. (2011). *ISO/IEC 25010:2011 Systems and software engineering—Systems and software Quality Requirements and Evaluation (SQuaRE)—System and software quality models*.

ISO/IEC. (2023). *ISO/IEC 25010:2023 Systems and software engineering—Systems and software Quality Requirements and Evaluation (SQuaRE)—Product quality model*.

## Declaración de uso de IA

La redacción fue preparada con asistencia de OpenAI Codex a partir de las fuentes internas indicadas. No ha recibido revisión humana ni constituye evidencia de cumplimiento o aceptación.
