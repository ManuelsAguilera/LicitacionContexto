# Dónde declarar los supuestos de plataformas e interfaces

**Decisión editorial:** los supuestos sobre el **estado actual desconocido** pertenecen primero al Subdocumento 2, sección 2.5.2 y su anexo de supuestos. El Subdocumento 3, subsección 3.2.3, solo recoge los que **condicionan el alcance, las responsabilidades, el costo o la aceptación**. El Subdocumento 4 desarrolla cómo se modela la solución con esos supuestos en 4.1 (interacción) y 4.2 (ubicación física). No se presentan productos comparables como si fueran los instalados por Ancoa.

Esta distribución sigue el [Comunicado 10, capítulos 2–4](../../00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md#L560): 2.5 exige resumen y fundamento de supuestos con detalle en `EMPRESA-Subdocumento2-Anexos`; 3.2 exige supuestos y restricciones **del alcance**; 4.1 y 4.2 explican la arquitectura propia de la solución. El [SD-02 actual](../../02_Propuesta/latex_final/sd-02.tex#L586) ya declara 27 supuestos en 2.5.2, y el [anexo de SD-03](../../04_Adjuntos/tablas/sd-03_s2_anexo-a_exclusiones-supuestos-restricciones.md#L33) mantiene supuestos de alcance `SP`. Cualquier incorporación a SD-02 requiere conciliar su numeración y el total 27 antes de editar el texto final.

## Regla para no mezclar hechos, hipótesis y decisiones

| Clase de información | Destino principal | Tratamiento |
| --- | --- | --- |
| Hecho expresamente declarado en las Bases o el Caso | SD-02, 2.2 y 2.3; citado de la fuente | No se numera como supuesto. En SD-04 se reutiliza para justificar el diseño. |
| Ubicación, alojamiento o interfaz **actual** no declarada que se adopta para estimar | SD-02, 2.5.2; detalle en `Subdocumento2-Anexos` | Supuesto metodológico con fuente análoga, motivo, impacto si falla y prueba de validación. En SD-04 4.2 se dibuja como ubicación provisional y se explica en el texto, sin siglas o signos sobre la figura. |
| Decisión del proponente sobre lo que **hará o no hará** la solución | SD-03, 3.2.3; detalle en anexo de alcance | Supuesto, restricción o exclusión de alcance según corresponda. Debe incluir efecto contractual, responsable y aceptación. No se deduce automáticamente de dónde se cree que está un servidor actual. |
| Interfaz o mecanismo de la **solución propuesta** | SD-03, 3.3–3.4 y SD-04, 4.1 | En SD-03 se indica responsabilidad funcional; en SD-04, contrato, mediación y modo. El protocolo exacto de un tercero queda condicionado a su contrato. |
| Elección de tecnología nueva | SD-04, 4.1.1 y 4.2 | Justificar selección y despliegue. Oracle, Microsoft, Mirakl y Salesforce citados como analogías no son elecciones de producto de la oferta. |
| Tarea para resolver una incertidumbre | SD-06, plan de trabajo y registro de riesgos | Levantamiento de las 14 interfaces, contratos, pruebas de enlace y corrección de capacidad/costo. |

## Ubicación de los supuestos reunidos

Los identificadores P y C remiten a la [matriz de plataformas y conexiones](supuestos_plataformas_y_conexiones.md). La matriz es material de trabajo y conserva la evidencia detallada; la oferta solo lleva el resumen adecuado a cada capítulo.

| Elemento de la matriz | Qué está declarado y qué se supone | Dónde debe quedar en la oferta |
| --- | --- | --- |
| P-01 núcleo Retail, P-02 crédito, P-08 ERP/DTE | El centro de datos compartido existe; **no constan los hosts individuales**. Ubicarlos allí es hipótesis. | SD-02 2.5.2 y su anexo: un supuesto de alojamiento central que agrupe las tres plataformas, con validación por inventario de hosts. SD-04 4.2: ubicación provisional y alternativa si están fuera. SD-03 3.2.3 solo si cambia la provisión de capacidad, conectividad o migración. |
| P-03 POS 2014 | La presencia de cajas en las tiendas es un hecho; la base/caché local y la autonomía del POS actual no constan. | SD-02 2.2: hecho de despliegue y versiones; SD-02 2.5.2/anexo: únicamente la hipótesis de almacenamiento local actual si se utiliza. La **autonomía de 24 h del POS nuevo** es compromiso de SD-03 3.2 y diseño de SD-04. |
| P-04 comercio electrónico, P-05 marketplace, P-07 fidelización | Funciones y decisiones de conservar/evaluar constan; alojarlos como SaaS externo es hipótesis. | SD-02 2.5.2/anexo: supuesto de alojamiento externo para estimación. SD-04 4.2: perímetro y dependencia externa provisional. SD-03 3.2.3: conservar/integrar/evaluar según decisión vigente, sin convertir la hipótesis SaaS en exclusión o garantía del proveedor. |
| P-06 WMS del CD principal | El CD usa WMS; **no consta dónde corre su servidor**. Ubicar servidor y base en el CD es hipótesis. | SD-02 2.5.2/anexo: supuesto y efecto sobre enlace/continuidad. SD-04 4.2: emplazamiento provisional y alternativa en casa matriz. SD-03 3.2.3: solo la decisión vigente de conservar WMS y evaluar/costear Concepción. |
| C-16: enlace centro principal ↔ sala de respaldo | Ambos sitios existen, pero su relación técnica no consta. Se propone un enlace de réplica/recuperación **entre centros**, sin afirmar que exista hoy. | SD-02 2.5.2/anexo: hipótesis física para estimación; SD-03 3.2.3 si fija costo, provisión o responsabilidad del enlace; SD-04 4.2 define arquitectura de continuidad y alternativas de ruta. SD-06 verifica sitio, capacidad y pruebas de recuperación. |
| P-09 planillas y listas, motor de precios inexistente | Son hechos del Caso, no supuestos nuevos. | SD-02 2.2: diagnóstico. SD-03 3.2–3.4: retiro como registro oficial y capacidad nueva de oferta/precios. SD-04: componentes y migración que materializan esa decisión. |
| C-01–C-10, C-12, C-14–C-15 | El Caso declara la función o cadencia de estos intercambios; **no declara todos sus protocolos, rutas ni pares técnicos**. | SD-02 2.2: solo los flujos y fallas conocidos; SD-02 2.5.2/anexo: supuesto general de topología para estimación, sin asignar una a una las 14 interfaces. SD-03 3.2.3: levantamiento de interfaces dentro del alcance. SD-04 4.1–4.2: rutas y adaptadores provisionales explicados en texto. |
| C-11 marketplace ↔ comercio electrónico | El sitio publica productos de terceros; el par técnico directo y su contrato son inferencia. | No afirmarlo como conexión actual en SD-02. En SD-03 3.3–3.4, explicar el intercambio funcional objetivo; en SD-04 4.1, definir una interfaz mediada y condicionada al contrato real. |
| C-13 POS/ventas ↔ ERP/DTE | El POS entrega documentos y ERP/DTE es emisor único; el par técnico preciso se desconoce. | SD-02 2.2: ambos hechos separados. SD-03 3.2.3: integrar la emisión tributaria sin sustituir el ERP. SD-04 4.1: flujo objetivo y contrato por verificar; SD-06: prueba de contingencia antes de comprometerla. |

## Texto breve sugerido para cada capítulo

- **SD-02 2.5.2:** «Para modelar y estimar la red existente se supone provisionalmente que las plataformas centrales operan desde el centro de datos de casa matriz, el WMS desde el CD principal y los canales digitales conservados desde alojamiento externo. El Caso no identifica los servidores ni contratos de integración; su localización se comprobará en el levantamiento temprano. La lista detallada y el efecto de cada desviación constan en el anexo». Ajustar este resumen y el conteo de supuestos una vez incorporado el anexo.
- **SD-03 3.2.3:** «El alcance incluye levantar las catorce interfaces actuales, integrar las plataformas que se conservan y ajustar los adaptadores al contrato comprobado. La ubicación provisional de los sistemas existentes es una base de estimación, no una exclusión de la integración comprometida». Si una topología distinta altera costo, plazo o reparto de responsabilidades, tratarlo mediante las reglas de cambio del contrato.
- **SD-04 4.1/4.2:** «La vista del estado actual usa las ubicaciones provisionales declaradas en SD-02. Las conexiones representan procesos conocidos o intercambios funcionales propuestos; la selección de protocolo y el emplazamiento definitivo se cierran tras inventariar plataformas, enlaces e interfaces». Acompañar el diagrama con el listado de ubicaciones provisionales en el pie o párrafo interpretativo, sin marcas de incertidumbre sobre los componentes.

## Consecuencia para la edición

1. Mantener esta nota y la matriz P/C como soporte de trabajo; no copiar sus dieciséis filas de conexión en el cuerpo de SD-02.
2. Preparar el detalle para `EMPRESA-Subdocumento2-Anexos` y decidir si se agrupan en tres supuestos nuevos: alojamiento central, WMS local y canales digitales externos. Conciliar con los 27 supuestos ya declarados y evitar duplicar `SUP-26/27` o los `SP` de SD-03.
3. Resumir en SD-02 2.5.2 solo lo que afecta la interpretación y el dimensionamiento del problema; llevar a SD-03 únicamente las consecuencias de alcance. SD-04 cita esos supuestos al justificar su mapa físico y sus interfaces.
4. Tras el levantamiento, sustituir la ubicación provisional por la comprobada y revisar capacidad, conectividad, seguridad, costos y planificación sin presentar la analogía de mercado como descubrimiento sobre Ancoa.
