---
estado: plan de trabajo
parte: T7-09
actualizado: 2026-10-11
---
# Plan para rehacer el Subdocumento 9

## Resultado buscado y punto de partida

Entregar un **Capítulo 9 legible y verificable**, con las secciones exactas 9.1 Plan de Calidad, 9.2 Estrategia de Aseguramiento de Calidad y 9.3 Alineación con Plan de Trabajo, y dos figuras integradas: puertas de calidad en 9.2 y calendario de calidad en 9.3. El cuerpo explica decisiones y ejemplos de Ancoa; T-13 desarrolla el plan de pruebas y T-17 el protocolo de aceptación. La matriz interna de 115 criterios es fuente de trabajo, no texto para pegar íntegro.

El [LaTeX vigente de SD09](../../02_Propuesta/latex_final/sd-09/OSS-Subdocumento9.tex) conserva portada y títulos, pero aún no contiene el desarrollo del capítulo. Existen una vista previa en Google Docs, la [matriz interna](README.md), el [material docente de calidad](../../90_Referencia/calidad/contextoCalidad.md), su [investigación](../../90_Referencia/calidad/investigacion_calidad.md), la [skill del revisor](../../.agents/skills/revisor-calidad/SKILL.md) y la [propuesta visual acordada](propuesta_figuras.md). El `.tex` será la fuente final; la vista previa se sincronizará tras cerrar su contenido.

## Contenido a reescribir

| Sección | Pregunta que debe responder sin leer anexos | Desarrollo previsto |
| :--- | :--- | :--- |
| **Introducción** | ¿Qué asegura este plan y cómo se conecta con el proyecto? | Calidad de proceso, producto y resultados de negocio; relación con SD06, SD07, arquitectura, riesgo, T-13 y T-17. Alcance de las dos etapas y operación. |
| **9.1 Plan de Calidad** | ¿Qué significa calidad en Ancoa, quién la gobierna y cómo se mide? | Separar calidad de grado, proceso de producto y prevención de control, de manera breve y aplicada. Conservar los ocho títulos contractuales del Art. 24 y explicar su relación con las nueve características de ISO/IEC 25010:2023. Objetivos, responsables y registros; tabla breve de métricas/umbrales y decisiones, incluida cobertura ≥70 % bloqueante, objetivo separado de ≥80 % en código nuevo, deuda ≤5 %, duplicación ≤3 %, y método/umbral de complejidad y acoplamiento por definir y fundamentar. No inventar madurez CMMI, certificación, umbrales ni resultados ejecutados. Mostrar cómo la prevención y corrección se planifican en esfuerzo/EDT, sin imponer la heurística docente de 15–25 %. |
| **9.2 Estrategia de Aseguramiento de Calidad** | ¿Cómo se previene un defecto, cómo se detecta y quién decide el avance? | Revisiones por pares, auditorías, análisis estático/dinámico y puertas de entrega. Figura visual de cinco estaciones con retorno ante fallo. Plan de pruebas conforme a ISO/IEC/IEEE 29119, con niveles, tipos, ambientes, datos, automatización, independencia y evidencias futuras; incluir carga, resiliencia, DR, seguridad, accesibilidad, migración y aceptación. Trazabilidad bidireccional de requisito → diseño → código/configuración → prueba → evidencia → despliegue, con un ejemplo corto de Retail y otro de Emisor. Defectos, repetición, control de cambios y acta de Contraparte. Detalle operativo en T-13 y T-17. |
| **9.3 Alineación con Plan de Trabajo** | ¿En qué EDT e hito se hace cada actividad y qué bloquea las producciones? | Relacionar EDT 1.9 calidad y pruebas, 1.12 marchas blancas/aceptación, 1.8 seguridad, 1.7 migración y operación. Figura de dos carriles: certificación M12/M18, marcha blanca M13–15/M19–20, producción M16/M21 y operación M21–56. Texto para campañas previas, revisión/subsanación Art. 18, pruebas periódicas, responsables y dependencias. Remitir al Gantt de SD07/T-14 sin copiarlo. |

Cada sección comenzará con un párrafo explicativo. Las figuras se citarán antes, llevarán título, numeración y fuente, y se interpretarán después. Los párrafos deben mostrar el efecto sobre Ancoa; las tablas solo concentran medidas paralelas. Ejemplos y umbrales propuestos se marcarán como tales cuando la fuente contractual no los fije. Los hallazgos H03–H05 del [registro de validación](../../90_Referencia/calidad/validacion_revisor.md) deben resolverse en controles: duplicación ≤3 %, rotación **automática** de secretos y cumplimiento de umbrales bajo 1,5× peak. H01–H02 son ajustes de procedencia sin cambiar el resultado comprometido, conforme al criterio expresado por el usuario.

## Secuencia de ejecución

| Paso | Producto revisable | Condición para continuar |
| :--- | :--- | :--- |
| **1. Congelar el mapa de fuentes** | Inventario de afirmaciones materiales con origen exacto: Bases, Caso, Comunicado 10, SD06/07, Anexo D, matriz y material docente. Decisiones abiertas B01–B30/P01–P08 identificadas sin rellenarlas por intuición. | Cada cifra/obligación del esquema tiene fuente; no se sustituyen tablas ilegibles ni se presenta el borrador v3.1 como catálogo oficial. |
| **2. Redactar por pregunta** | Borradores separados de 9.1 y 9.2–9.3 en `80_Artefactos/sd-09_contexto/borradores/`, con ejemplos y remisiones a T-13/T-17. | El lector entiende quién hace qué, cómo se mide y qué impide avanzar sin buscar los 115 criterios; se conserva toda obligación pertinente. |
| **3. Dibujar las dos figuras** | Fuente editable y PDF vectorial en `04_Adjuntos/diagramas/`: flujo de puertas y línea de tiempo con carriles, según [diseño aprobado](propuesta_figuras.md). | Pocas palabras dentro de formas; fechas/roles correctos; lectura impresa ≥9 puntos; leyenda comprensible en gris. |
| **4. Integrar una sola versión** | Contenido y figuras insertados en el cuerpo del `.tex` vigente por el orquestador Sol; citas, referencias y declaración de IA coherentes. | Sin preámbulo alterado; texto/figuras/tablas consistentes, sin secciones huérfanas ni contradicciones con SD06/07. |
| **5. Revisar con agente de calidad** | Informe del revisor que aplica íntegramente la skill y las 38 páginas docentes a la nueva versión, distinguiendo diseño, ejecución y aceptación. Registro de hallazgos y correcciones. | Hallazgos materiales corregidos o explicitados como decisión pendiente con dueño; una segunda lectura de los pasajes corregidos confirma cierre documental. |
| **6. Compilar y comprobar** | PDF de vista previa del SD09 y reporte de compilación, usando `exportar_latex.py` (`doctor`/`estado`/`verificar`/`verificar-redaccion`/`compilar --parte T7-09`). | Figuras visibles, no cortadas y legibles; referencias, números, encabezados, tablas y páginas revisados. La compilación no declara pruebas del producto ejecutadas ni aprobación de la Contraparte. |
| **7. Actualizar vista de lectura** | Pestaña Preview del Google Doc puesta al día con el contenido consolidado; pestaña Matriz referida sin duplicar todo el capítulo. | La vista previa no diverge de la fuente LaTeX y queda identificada como borrador. |

## Equipo de agentes propuesto

Durante la ejecución habrá **un agente principal `gpt-6.1-sol` activo como orquestador**. El resto será `gpt-6-luna`. El agente raíz supervisa el resultado. Solo el orquestador edita `OSS-Subdocumento9.tex`, integra figuras y decide contradicciones; los Luna escriben en archivos propios o revisan en solo lectura. Así no hay ediciones simultáneas del mismo cuerpo.

| Agente | Modelo | Encargo y entrega |
| :--- | :--- | :--- |
| **Principal SD09** | Sol | Mantener mapa de decisiones, asignar trabajo, integrar secciones/figuras, corregir hallazgos y compilar. Custodio único del `.tex` y del resultado final. |
| **Fuentes y trazabilidad** | Luna | Contrastar Bases, Comunicado 10, SD06/07, Anexo D y matriz; entregar mapa afirmación → fuente, lagunas y dependencias de T-13/T-17. No editar el `.tex`. |
| **Redacción 9.1** | Luna | Borrador de marco, gobierno, métricas, modelos, calidad del código y costo de calidad proporcional al caso. Aplica material docente/investigación sin convertir heurísticas en obligaciones. |
| **Redacción 9.2–9.3** | Luna | Borrador de prevención, pruebas, trazabilidad, puertas, hitos/EDT y operación; ejemplos Retail/Emisor. Coordina vocabulario con 9.1 a través del principal. |
| **Figuras** | Luna | Dos diseños propios con fuente editable, PDF vectorial, paleta consistente, rótulos cortos y cotejo visual de PDF. No repetir Gantt ni arquitectura. |
| **Revisión de calidad** | Luna | Aplicar `.agents/skills/revisor-calidad/SKILL.md` a la versión integrada, de forma independiente y en solo lectura; informar hallazgos con fuente, corrección y cierre. Se activa después de integrar, no revisa borradores aislados como versión final. |

Los cuatro Luna de fuentes, redacción 9.1, redacción 9.2–9.3 y figuras pueden trabajar en paralelo sobre áreas separadas. El revisor Luna entra después. Con el agente raíz y el orquestador Sol, el máximo simultáneo es seis agentes y cabe en la concurrencia disponible de siete. No se presume que el revisor recuerde la sesión anterior: debe abrir de nuevo su skill, transcripción e investigación.

## Criterios de terminado

1. Estructura y texto de caída conformes al Comunicado 10; las dos figuras están en 9.2 y 9.3, citadas, tituladas, con fuente y explicadas, sin texto microscópico.
2. Calidad de proceso, producto y resultado de negocio distinguida; QA preventivo, QC y aceptación humana descritos con roles, método y evidencia; modelos y ediciones citados con precisión.
3. Coberturas, deuda, duplicación, rendimiento, seguridad y continuidad preservan sus umbrales y ámbitos; complejidad/acoplamiento tienen método y decisión justificados o brecha explícita antes de bloquear.
4. Capítulo, SD06, SD07, matriz, T-13/T-17 y figuras cuentan la misma historia de Etapas 1/2, Retail/Emisor, puertas y recepción. La matriz parcial no se presenta como cobertura total del catálogo ni como campaña ejecutada.
5. El script corporativo verifica y compila; se inspeccionan visualmente las páginas con figuras y el PDF completo por referencias/flujo. Se entrega fuente `.tex` y PDF de vista previa, más lista corta de decisiones aún abiertas y revisión humana pendiente.
