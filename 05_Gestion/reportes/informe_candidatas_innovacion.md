# Informe de candidatas para las cinco innovaciones

**Fecha:** 8 de octubre de 2026
**Estado:** investigación preliminar para decidir la cartera; no constituye todavía el texto de SD-13 ni del Formulario T-19.

## 1. Propósito y criterio de evaluación

Este informe ordena las ideas discutidas para el Caso 09 en los cinco tipos exigidos por el artículo 28 de las Bases Administrativas. Cada ficha futura deberá acreditar problema, solución concreta, madurez y fuentes, incorporación a arquitectura y EDT, mes de entrega, impacto económico, indicador con línea base y meta, y riesgo de adopción. Las Bases excluyen la simple adopción de una tecnología estándar y la presentación de un requisito obligatorio como innovación. Véanse los [artículos 28 a 30](../../00_Bases/Bases_Administrativas.md#artículo-28-cartera-obligatoria-de-cinco-innovaciones) y [RT-26](../../00_Bases/Bases_Transversales.md#capítulo-26-innovaciones).

Las etiquetas electrónicas quedan fuera de esta cartera por decisión del equipo. Las cinco propuestas de abajo son **candidatas**: se incorporarán a la oferta como innovaciones solo si se documenta un aporte adicional y verificable sobre el alcance obligatorio.

## 2. Cartera candidata

| Tipo obligatorio | Candidata | Aporte adicional a demostrar | Indicadores propuestos | Estado |
| :--- | :--- | :--- | :--- | :--- |
| Producto o servicio | **Servicio de diagnóstico de merma asistido por ML.** Sugiere causas probables de una discrepancia y muestra la evidencia para su revisión por Prevención de Pérdidas. | Menor tiempo de investigación y mayor proporción de diferencias con causa confirmada, sobre la clasificación e informe por causas ya exigidos. | Tiempo desde conteo hasta causa confirmada; proporción de casos con causa confirmada; desempeño por clase del modelo. | Prometedora; requiere causas históricas verificadas o una fase de etiquetado. |
| Proceso | **Conteo cíclico predictivo.** Estima riesgo y magnitud de discrepancia por referencia, ubicación y período para priorizar conteos. Sus resultados alimentan la revisión del descuento de seguridad. | Más diferencias relevantes detectadas con la misma capacidad de conteo y un descuento calibrado con evidencia, frente a la programación y sugerencia básica ya previstas. | Diferencias relevantes por 100 conteos; cobertura con horas fijas; calibración del riesgo; cancelaciones por falta de stock y unidades retenidas por el descuento. | Prometedora; exige una muestra de conteos de control no dirigida por el modelo. |
| Tecnología o arquitectura | **Plataforma analítica gobernada por ámbito.** Espacios analíticos independientes para Retail y Emisor, conjuntos de datos aprobados por finalidad y linaje automatizado hasta el indicador. | Análisis reproducible y trazable, con políticas efectivas también en consultas de detalle, exportaciones e informes programados. Debe superar los tableros y el autoservicio obligatorios. | Tiempo de preparación de un conjunto de datos aprobado; proporción de indicadores con linaje verificable; intentos de acceso indebido bloqueados en pruebas; tiempo de reconstrucción de un indicador. | Por fortalecer; un Data Lake por sí solo no califica. |
| Modelo de negocio o contratación | **Servicio gestionado de evolución analítica.** Responsabilidad definida sobre operación, calidad de datos, monitoreo y mejora de modelos e indicadores durante el contrato. | Compromisos de servicio y mejora continua con medición y efecto económico propios, compatibles con los hitos y pagos establecidos. | Disponibilidad de indicadores críticos; tiempo de corrección de defectos de datos; cumplimiento del ciclo de evaluación de modelos. | La candidata menos madura; requiere análisis contractual y económico. |
| Experiencia de usuario | **Asistencia contextual en el nuevo POS.** Guía al personal ante discrepancia de precio, stock incierto, venta sin conexión y derivación al rol financiero. | Menos errores y menor tiempo de resolución y aprendizaje que un POS que solo cumpla los mínimos de accesibilidad y flujos guiados. | Tiempo y tasa de éxito por tarea; errores; intervenciones de supervisor; tiempo de aprendizaje por perfil. | Prometedora; faltan línea base y pruebas con cajeros nuevos y experimentados. |

## 3. Alcance existente y diferencia incremental

### 3.1 Modelos de inventario y merma

El Caso 09 señala que el descuento de seguridad aplicado a la existencia publicada es un número fijo definido en 2019. También informa que el 12,4 % de las **referencias auditadas** presenta diferencias y que la composición de la merma no se conoce. Esto fundamenta investigar una estimación basada en conteos, pero impide inferir sin más la tasa de error de todo el catálogo. Véanse el [testimonio sobre el descuento](../../00_Bases/Caso_09_Cadena_Multitienda.md#marisol-tapia-verdugo--jefa-de-tienda-temuco) y la [situación de merma](../../00_Bases/Caso_09_Cadena_Multitienda.md).

El [catálogo depurado](../../01_Requerimientos/md/catalogo-de-requerimientos-depurado-v30.md) ya incluye RF-127 a RF-130 para el disponible y su colchón por categoría y punto, RF-131 a RF-137 para conteos, RF-138 a RF-141 para clasificación e informe de merma, y RF-152 para sugerir un colchón desde ventas y quiebres. SD-03 deja pendiente calibrar el margen. Por ello, las candidatas se evaluarán contra esas reglas existentes, no contra la ausencia de sistema. El término de trabajo será **descuento de seguridad** al referirse al problema actual y **colchón de confianza** al referirse al parámetro de la solución; en la redacción se explicará su relación.

El modelo predictivo propone **dónde y cuándo contar**; el clasificador propone **qué causa investigar** una vez observada la diferencia. Para ajustar el colchón debe probarse además que el riesgo predicho se traduce en un valor útil para la promesa de disponibilidad, comparando cancelaciones con unidades que se dejan de ofrecer. Un mismo modelo predictivo podría producir ambos insumos, pero su calidad se medirá para cada decisión. La clasificación de causas exige confirmación humana; una predicción no acreditará por sí sola hurto ni autorizará un ajuste.

El muestreo de evaluación combinará conteos priorizados con conteos aleatorios o estratificados. Sin este control, priorizar artículos de riesgo sesgaría la estimación del error general. Antes de fijar metas se necesita perfilar historial de conteos y movimientos, calidad de ubicaciones, causas confirmadas y horas disponibles para contar. Toda incorporación de ML deberá cumplir [RT-18](../../00_Bases/Bases_Transversales.md#capítulo-18-inteligencia-artificial-y-automatización): finalidad, ubicación y versión del modelo, métricas, deriva, auditoría, validación humana, desactivación y respaldo manual. Las Bases citan el [AI Risk Management Framework de NIST](https://www.nist.gov/itl/ai-risk-management-framework) y la [norma ISO/IEC 42001](https://www.iso.org/standard/81230.html) para gobernar estos riesgos.

### 3.2 BI, Data Lake y frontera de datos

La [capa analítica obligatoria](../../00_Bases/Bases_Transversales.md#54-analítica-e-inteligencia-de-negocio) ya exige tableros, filtros, profundización a la transacción, autoservicio, exportación e informes programados; RT-05.05 exige separar almacenamiento analítico y transaccional. El catálogo de datos con linaje automatizado de RT-05.10 es deseable. La innovación tecnológica tendría que concretar una mejora sobre esos mínimos, demostrar su beneficio y justificar el patrón elegido.

La arquitectura investigada propone una zona analítica de Retail para ventas, existencias, conteos, pedidos y devoluciones, y otra del Emisor para información financiera, con autoridades, identidades, modelos semánticos y permisos separados. La interfaz puede compartir componentes visuales, pero cada sesión solo accederá a los datos de su ámbito. Los controles deben cubrir consulta, profundización, exportación y envío programado. La [arquitectura vigente](../../02_Propuesta/latex_final/sd-04.tex) mantiene saldos, mora, cupos y comportamiento de pago fuera del perfil comercial. X-01 gobierna cruces específicos aprobados; no es el repositorio analítico ni una autorización general para mezclar datos. La elección de tecnología física para el Data Lake queda sujeta a la memoria de capacidad y a la comparación de alternativas.

### 3.3 Experiencia en el nuevo POS

Las figuras 3.2 a 3.8 de [SD-03](../../02_Propuesta/latex_final/sd-03.tex) describen vistas arquitectónicas y recorridos de negocio; aún no especifican pantallas POS. La investigación de UX debe convertir tareas de cajero, vendedor, posventa y rol financiero en vistas y estados comprobables, incluyendo excepciones. [RT-13](../../00_Bases/Bases_Transversales.md#capítulo-13-usabilidad-accesibilidad-y-experiencia-de-usuario) ya exige accesibilidad, investigación con usuarios, flujos guiados, manejo comprensible de errores y métricas por perfil. El prototipo navegable del Informe 3 también es obligatorio. La innovación propuesta debe acreditar una mejora adicional mediante pruebas comparables de tareas reales.

### 3.4 Modelo contractual

Un servicio gestionado debe añadir compromisos verificables a la operación y evolución de la analítica y reflejar inversión, costo operacional y beneficio en la propuesta económica. No se asumirá un pago por éxito ni una modificación de hitos: primero debe comprobarse la compatibilidad con el contrato de 56 meses, su calendario de pagos y las reglas de modificación. Si no aparece una diferencia contractual genuina y admisible, esta candidata debe sustituirse.

## 4. Trazabilidad prevista para la redacción

| Documento | Incorporación prevista después de validar la cartera |
| :--- | :--- |
| SD-03, esquema y explicación | Responsabilidades, datos de entrada y salida y recorridos de las capacidades seleccionadas; diferenciar alcance obligatorio e incremental. |
| SD-04, arquitectura lógica | Ubicación de modelos y plataforma analítica; contratos, separación de ámbitos, seguridad y modos de respaldo. |
| SD-05, modelo y gestión de datos | Autoridad, calidad, linaje, retención y política de conjuntos de datos analíticos. |
| SD-13 y Formulario T-19 | Una ficha por tipo, con los siete elementos del artículo 29 y los requisitos RT-26. |
| EDT, cronograma y oferta económica | Paquetes, mes de entrega, inversión, costo operacional y beneficio de cada innovación. |

## 5. Decisiones y evidencia pendientes

1. **Validar la cartera de cinco tipos.** En particular, decidir si el servicio gestionado y la plataforma analítica tienen un aporte incremental suficiente o si corresponde sustituir alguna candidata.
2. **Perfilar los datos de inventario.** Confirmar historial de conteos, causas verificadas, capacidad de conteo y calidad por tienda y categoría antes de seleccionar modelos o fijar metas.
3. **Definir las líneas base.** Medir la regla actual del descuento, el rendimiento de conteos, el tiempo de investigación de merma, la preparación de análisis y las tareas POS. Cuando no exista medición, declararla pendiente y definir su protocolo; no inventar cifras.
4. **Comparar alternativas técnicas y contractuales.** Documentar madurez, fuentes APA, impacto económico y riesgos antes de comprometer tecnología, proveedor o niveles de servicio.
5. **Validar con responsables.** Logística y Prevención deben aprobar las decisiones de conteo y clasificación; los responsables de Retail, Emisor y Cumplimiento, los conjuntos de datos y permisos; operación de tienda, los recorridos POS.

La redacción de las secciones de la oferta comenzará cuando la cartera y sus diferencias frente al alcance obligatorio estén validadas.
