# Candidatas para las cinco innovaciones (versión 2)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Mejora el informe de candidatas del mismo día (versión 1, fuera del repositorio) con lo ya resuelto en el sd-03: alcance por etapas, catálogo (Anexo B), criterios de aceptación (Anexo D), supuestos y nomenclatura. **No es el texto del SD-13 ni del Formulario T-19.** Todo lo marcado «propuesta» es del equipo y está por validar. Las cifras provienen del Caso y del sd-03. Lo que falta medir se declara «por medir», nunca se estima aquí.

## 1. Criterios que debe cumplir cada candidata

- Una innovación por cada tipo del art. 28 de las Bases Administrativas, con los siete elementos del art. 29 (problema con dato, tecnología descrita con precisión, madurez con fuentes APA, incorporación a arquitectura, EDT y mes, impacto económico, indicador con línea base, meta y momento, y riesgo con contingencia).
- No califica la adopción de un estándar de la industria, una tendencia sin diseño de incorporación ni una funcionalidad que las Bases Técnicas ya exigen (art. 30). La pertinencia al caso pesa más que la novedad (art. 30.2).
- RT-26.08 (deseable): al menos una innovación se puede medir antes del mes 16, durante la marcha blanca de la Etapa 1.
- Si usa inteligencia artificial, cumple el capítulo 18 de las Transversales completo (RT-26.06 y RT-18.01 a RT-18.09).
- La innovación de modelo de negocio debe considerar que una parte del negocio está fiscalizada (Caso, cap. 19).
- Las etiquetas electrónicas quedan fuera por decisión del equipo (EXC-02). El Caso pide evaluarlas y costearlas, pero no instalarlas.

## 2. Qué cambió respecto de la versión 1

1. Se reemplazan las referencias a «figuras 3.2 a 3.8 del SD-03» (no existen) por las figuras D1 a D6, especificadas como comentarios en el `.tex`, y el catálogo v3.0 por el Anexo B (v3.1, 308 elementos). Los RF citados siguen vigentes.
2. Cada candidata se ancla a un resultado de negocio del Caso con la línea base y la meta ya fijadas en el Anexo D.
3. Cada candidata declara en qué servicio y en qué mes se materializa, con el calendario del sd-03 (desarrollo meses 1 a 12, marcha blanca 13 a 15, producción en el mes 16 en abril de 2028, y Etapa 2 en el mes 21).
4. Se declara lo que cada candidata agrega sobre lo obligatorio, con los requisitos que ya lo cubren. Las candidatas 1 y 2 chocan con RF-131 a RF-139 y RF-152, y con RT-05.30 (analítica predictiva, deseable).
5. Se advierte que las candidatas 1 y 2 comparten servicio y datos, y que la candidata 4 puede quedar en «servicio estándar» si no se redefine.
6. Se agrega la trazabilidad por candidata (sección 5) y la lista de pendientes ordenada por dependencia (sección 6).
7. El borrador anterior `80_Artefactos/seccion3_innovaciones.md` (septiembre) queda superado. Propone etiquetas electrónicas y otras ideas que contradicen decisiones posteriores.

## 3. Cartera candidata

| Tipo | Candidata | Servicio y etapa | Qué agrega sobre lo obligatorio | Estado |
| :-- | :-- | :-- | :-- | :-- |
| Producto o servicio | Diagnóstico de merma asistido por ML | Servicio de existencias, Etapa 1 | Sugiere la causa de cada diferencia con su evidencia, sobre la clasificación manual de RF-138 | Prometedora. Falta historia de causas verificadas |
| Proceso | Conteo cíclico predictivo | Servicio de existencias, Etapa 1 | Prioriza dónde contar por riesgo esperado, sobre la programación fija de RF-134 | Prometedora. Riesgo de solapar con la anterior |
| Tecnología o arquitectura | Plataforma analítica gobernada por ámbito | Base tecnológica y servicio de control de cruces, Etapas 1 y 2 | Políticas por ámbito también en detalle, exportaciones e informes, y linaje hasta el indicador | Por fortalecer |
| Modelo de negocio o contratación | Niveles de servicio por resultado de negocio | Operación, meses 21 a 56 | Compromisos de servicio atados a resultados del Anexo D, solo en el lado retail | La menos madura |
| Experiencia de usuario | Asistencia contextual en el POS | Servicio de ventas, Etapa 1 | Guía situaciones de excepción, sobre los flujos guiados y los errores comprensibles que ya exige RT-13 | Prometedora. Falta línea base |

## 4. Fichas

### 4.1 Diagnóstico de merma asistido por ML (producto o servicio)

- **Problema y línea base.** La merma es 1,9 % de la venta, más de $ 7.800 millones al año, y hoy se trata como un solo concepto (Caso, cap. 7). El resultado 5 del Caso exige separarla en sus causas y el 27 exige que la jefa de tienda pueda demostrar qué parte de su diferencia es pérdida física y qué parte es error de registro.
- **Lo obligatorio que ya existe.** RF-138 clasifica cada diferencia, RF-139 impide cerrar un ajuste sin causa, RF-140 cuantifica los componentes y RF-141 emite el informe mensual. La innovación no puede ser clasificar. Su aporte es sugerir la causa probable con la evidencia que la sustenta, para reducir el tiempo de investigación y subir la proporción de diferencias con causa confirmada.
- **Gobierno de la IA.** La persona confirma siempre la causa (RT-18.03). El procedimiento manual de RF-138 es el respaldo (RT-18.06). Se indica que la causa es una sugerencia automática (RT-18.07) y se registra entrada, salida y decisión humana (RT-18.05). Se declaran variables, métrica, deriva y reentrenamiento (RT-18.08). Una predicción nunca acredita por sí sola un hurto ni autoriza un ajuste.
- **Incorporación (propuesta).** Se ubica en el servicio de existencias. El perfilado de datos y el etiquetado van en el desarrollo de la Etapa 1 (meses 1 a 12). El modelo corre en modo sombra durante la marcha blanca (meses 13 a 15), lo que permite medirlo antes del mes 16 (RT-26.08). Entra en uso desde el mes 16. Los paquetes de la EDT los define el capítulo 7.
- **Indicador.** Tiempo desde la detección de una diferencia hasta su causa confirmada, y proporción de diferencias con causa confirmada. La línea base de ambos está **por medir**: no existe medición y se define un protocolo en la marcha blanca. El Anexo D ya fija «100 % de los ajustes con causa» como meta del resultado 5 (propuesta del proponente).
- **Riesgos.** Causas históricas sin verificar, sesgo del modelo hacia las causas más frecuentes y deriva. Contingencia: se mantiene la clasificación manual y el modelo se desactiva sin afectar el resto del servicio.
- **Pendiente.** Madurez con escala y fuentes APA (RT-26.03). Impacto económico para el flujo de caja.

### 4.2 Conteo cíclico predictivo (proceso)

- **Problema y línea base.** El conteo cíclico encuentra diferencias en 12,4 % de las referencias auditadas, y la meta del Caso es bajo 2 % (resultado 4 del Anexo D). La frecuencia de conteo hoy no depende del riesgo.
- **Lo obligatorio que ya existe.** RF-131 a RF-133 parametrizan frecuencia, método y gatillo por categoría. RF-134 genera la programación, RF-136 señala los recuentos extraordinarios y RF-137 calcula la exactitud por categoría. RF-152 sugiere un colchón de confianza desde ventas y quiebres. RT-05.30 valora la analítica predictiva. La innovación debe ir más allá de una programación parametrizada.
- **Aporte.** Estima el riesgo y la magnitud de la diferencia por referencia, ubicación y período, y ordena los conteos para encontrar más diferencias relevantes con las mismas horas de conteo. Sus resultados alimentan la calibración del colchón de confianza, cuya tolerancia el Anexo D deja «por fijar al inicio del proyecto».
- **Control del sesgo.** Una parte de los conteos es aleatoria o estratificada y no la dirige el modelo. Sin ella, priorizar lo riesgoso sesgaría la estimación del error general.
- **Separación de la candidata 4.1.** Esta decide dónde y cuándo contar. La 4.1 decide qué causa investigar una vez que hay una diferencia. Los dos pueden usar el mismo modelo, pero se miden por separado. Si el equipo prefiere una sola, se fusionan y se sustituye esta por otra idea de proceso para no perder un tipo.
- **Incorporación (propuesta).** Mismo servicio y mismo calendario que la 4.1: modo sombra en los meses 13 a 15 y uso desde el mes 16.
- **Indicador.** Diferencias relevantes encontradas por cada 100 conteos, con la ventana de medición del Anexo D (últimos tres meses antes del acta), y cancelaciones por falta de existencia frente a unidades retenidas por el colchón. Líneas base **por medir**.
- **Riesgos.** Mala calidad de las ubicaciones, historial de conteo insuficiente y horas de conteo disponibles. Contingencia: vuelve la programación fija de RF-134.
- **Pendiente.** Perfilar el historial de conteos antes de fijar metas.

### 4.3 Plataforma analítica gobernada por ámbito (tecnología o arquitectura)

- **Problema.** La compañía es una tienda y un emisor de crédito fiscalizado, con dos regímenes. Hoy la separación es parcial y no documentada (Anexo D, resultado 21). Una capa analítica común mezclaría ambos negocios.
- **Lo obligatorio que ya existe.** RT-05.05 separa lo transaccional de lo analítico. RT-05.25 a RT-05.28 exigen tableros, filtros, profundización, autoservicio, exportación e informes programados. RT-05.10 (deseable) pide un catálogo de datos con linaje. Un lago de datos por sí solo no califica.
- **Aporte.** Espacios analíticos independientes para retail y para la filial emisora, con identidades, permisos y modelos semánticos propios. Las políticas valen también en la consulta de detalle, en las exportaciones y en los informes programados. Los conjuntos de datos se aprueban por finalidad, y el linaje se automatiza hasta el indicador. El servicio de control de cruces autoriza y audita los cruces puntuales y no es el repositorio analítico.
- **Conexión con el sd-03.** Los 28 resultados del Anexo D son los primeros indicadores con linaje verificable. El resultado 22 (todo cruce queda registrado) se prueba con esta misma capa.
- **Incorporación (propuesta).** Espacio de retail con los indicadores de existencias en la Etapa 1, y los de pedidos en la Etapa 2. Espacio de la filial emisora con evidencia financiera en la Etapa 1. La tecnología física queda sujeta a la memoria de capacidad (capítulo 4).
- **Indicador.** Tiempo de preparación de un conjunto de datos aprobado, proporción de indicadores con linaje verificable, intentos de acceso indebido bloqueados en pruebas y tiempo de reconstrucción de un indicador. Líneas base **por medir**.
- **Riesgos.** Que se perciba como los mínimos obligatorios con otro nombre. Contingencia: reducir el alcance a lo diferencial (linaje y políticas por ámbito) y dejar lo demás en la capa obligatoria.
- **Pendiente.** Fuentes APA de madurez y el patrón arquitectónico elegido con sus alternativas (RT-26.03).

### 4.4 Niveles de servicio por resultado de negocio (modelo de negocio o contratación)

- **Problema.** Los resultados de negocio del Caso son lo que el cliente usará para juzgar el proyecto, y hoy solo tienen un plan de corrección si no se cumplen (sd-03, 3.2.5). La operación dura 36 meses, del mes 21 al 56.
- **Lo obligatorio que ya existe.** La operación, la mantención correctiva, preventiva y evolutiva y los niveles de servicio técnicos son parte del contrato (art. 14.2). Un servicio gestionado de operación por sí solo no califica.
- **Aporte propuesto.** Niveles de servicio atados a resultados del Anexo D que dependen de la solución, como la exactitud del inventario o las cancelaciones por falta de existencia, medidos con la ventana de tres meses. Con créditos de servicio o un escalamiento definido si no se cumplen. Se aplican solo al lado retail. La filial emisora está fiscalizada y no admite cualquier diseño de este tipo (Caso, cap. 19).
- **Límites.** No se asume pago por éxito ni cambio de hitos o de pagos (art. 18.1 y Formulario E-25) sin revisar su compatibilidad con el contrato de 56 meses y con las reglas de modificación (art. 72).
- **Incorporación (propuesta).** Desde el inicio de la operación (mes 21). Debe reflejarse en la estructura de costos y en el flujo de caja (art. 28).
- **Indicador.** Cumplimiento de cada nivel por período y efecto económico propio. Líneas base según los resultados del Anexo D.
- **Riesgos.** Que el cliente lo vea como una multa disfrazada, y que no sea admisible contractualmente. Si el análisis no encuentra una diferencia genuina, esta candidata debe sustituirse.
- **Pendiente.** Análisis contractual y económico. Es la candidata menos madura.

### 4.5 Asistencia contextual en el POS (experiencia de usuario)

- **Problema y línea base.** Abrir una tarjeta toma hoy tres minutos y la información precontractual se entrega «como se puede» (resultado 28). La garantía legal hoy se resuelve derivando al cliente (resultado 15). Hay 62 % de rotación anual en el personal de venta y caja y 1.900 incorporaciones de temporada concentradas en el congelamiento (Transversales, RT-22.04).
- **Lo obligatorio que ya existe.** RT-13.04 exige indicadores de usabilidad por perfil. RT-13.06 y RT-13.07 exigen errores comprensibles y flujos guiados. RNF-49 pide que sala, caja y mesón financiero sean operables por personal recién incorporado con capacitación mínima (≤ 4 horas, supuesto fundamentado). La innovación debe ir más allá de esos mínimos.
- **Aporte.** Asistencia en el momento de la excepción, no solo un flujo guiado. Cuando el precio exhibido difiere del cobrado, cuando la disponibilidad es incierta (con su grado de confianza), cuando no hay conexión (venta con cupo preaprobado dentro de los topes de la filial, SP-03) y cuando hay que derivar al rol financiero, el POS indica qué hacer y deja el registro.
- **Dependencias.** La política de precio en sala está pendiente (SUP-08 y SUP-09). Abrir tarjetas sin conexión queda fuera (EXC-16).
- **Incorporación (propuesta).** Servicio de ventas en la Etapa 1, con el piloto de tres tiendas (3.1 del sd-03). Medición durante la marcha blanca, antes del mes 16 (RT-26.08).
- **Indicador.** Tiempo y tasa de éxito por tarea, errores, intervenciones de supervisor y tiempo de aprendizaje por perfil, medidos con cajeros nuevos y experimentados. El tiempo de apertura de tarjeta (tres minutos) es la única línea base disponible. Las demás están **por medir**.
- **Riesgos.** Dependencia de la política de precios, sobrecarga de mensajes que los cajeros ignoren y falta de pruebas con usuarios reales (RT-13.03).
- **Pendiente.** Línea base y protocolo de prueba.

## 5. Trazabilidad prevista

| Candidata | Servicio | Mes de materialización (propuesta) | Resultado del Anexo D | Requisitos aplicables |
| :-- | :-- | :-- | :-- | :-- |
| Diagnóstico de merma | Existencias | Medición meses 13 a 15, uso desde el 16 | 5 y 27 | RT-26.06, RT-18 completo, RF-138 a RF-141 |
| Conteo predictivo | Existencias | Medición meses 13 a 15, uso desde el 16 | 4 y 1 | RT-26.06, RT-18 completo, RF-131 a RF-137, RF-152, RT-05.30 |
| Plataforma analítica | Base tecnológica y control de cruces | Etapas 1 y 2 | 21 y 22 | RT-26.03, RT-05.05, RT-05.10, RT-05.25 a RT-05.28 |
| Niveles de servicio | Operación | Mes 21 en adelante | 2, 4 y otros | Art. 14.2, 18 y 72, Caso cap. 19 |
| Asistencia en el POS | Ventas | Medición meses 13 a 15, uso desde el 16 | 15, 16 y 28 | RT-13.03, RT-13.04, RT-13.06, RT-13.07, RNF-49 |

Los paquetes de la EDT (RT-26.02), la ubicación en la arquitectura (RT-26.01) y el flujo de caja se completan cuando los capítulos 4 y 7 y la oferta económica los definan.

## 6. Decisiones y pendientes

1. **Validar la cartera.** Decidir si las candidatas 1 y 2 son dos innovaciones o una. Decidir si la 4 tiene un aporte contractual admisible y, si no, sustituirla.
2. **Perfilar los datos de inventario.** Historial de conteos, causas verificadas, capacidad de conteo y calidad por tienda y categoría, antes de elegir modelos o fijar metas.
3. **Definir las líneas base por medir.** Regla actual del colchón, rendimiento de los conteos, tiempo de investigación de merma, preparación de análisis y tareas del POS. Cuando no hay medición, se declara pendiente con su protocolo.
4. **Reunir madurez y fuentes APA** de cada candidata de base tecnológica (RT-26.03), y los NIST AI RMF 1.0 e ISO/IEC 42001 que las Bases exigen para la IA (RT-18.04).
5. **Valorizar** inversión, costo operacional y beneficio de cada una, para el flujo de caja (art. 29).
6. **Validar con los responsables.** Logística y Prevención de Pérdidas (conteo y clasificación), responsables de retail, emisor y cumplimiento (conjuntos de datos y permisos) y operación de tienda (recorridos del POS).
7. **Desde el sd-03.** Resolver SUP-08 y SUP-09 antes de especificar la asistencia por discrepancia de precio. Confirmar la selección de las tres tiendas piloto con SUP-27.

La redacción del SD-13 y del Formulario T-19 comienza cuando la cartera esté validada.
