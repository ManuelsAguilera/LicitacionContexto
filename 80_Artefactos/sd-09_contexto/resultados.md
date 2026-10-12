---
id: contexto-sd09-resultados
estado: borrador
fuente: 04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md
---

# Resultados de negocio para el plan de calidad del sd-09

Estas fichas descomponen los 28 resultados del Anexo D en unidades de seguimiento para el plan de calidad. Los códigos `R01`–`R28` y `C-Rnn-01` son identificadores internos de este artefacto; no agregan requisitos ni alteran el Anexo D. La meta y el método se reproducen según la fuente. Cuando el Caso no fija una meta, se marca como propuesta del proponente; las decisiones abiertas quedan pendientes de validación con el cliente al inicio del proyecto.

El calendario es el del Anexo D y del diseño vigente del sd-03: Etapa 1 entra en producción en mes 16 (abril de 2028, supuesto de inicio enero de 2027); Etapa 2 entra en producción en mes 21 (septiembre de 2028); operación termina en mes 56. Para tasas anuales se usa la ventana propuesta de los tres meses consecutivos previos al acta. Los resultados ligados al evento anual se miden en el primer evento posterior al mes 21 y no desplazan el plazo contractual.

El proponente mide y prepara la evidencia; la Contraparte Técnica valida y firma el acta. En R02, R04, R09, R15 y R26 la responsabilidad es compartida con el cliente en la dimensión operativa descrita. Los métodos adicionales que no aparecen como compromiso textual se identifican como propuesta o pendiente, no como criterio oficial. El [Caso, capítulo 18, establece los resultados que juzgan el éxito y pide indicar meta, momento y método](../../00_Bases/Caso_09_Cadena_Multitienda.md#L944); el [sd-03, sección 3.2.5, fija los tres niveles de aceptación y el rol de cada parte](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L316) y explica la consecuencia de incumplir un resultado [en la línea 326](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L326). El Anexo D es la fuente de valores y evidencias por resultado.

## Fichas

<a id="r01"></a>

### R01 — Disponible por categoría y punto

- **Criterio interno:** C-R01-01. El cálculo incorpora el error conocido del registro y publica disponibilidad dinámica por categoría y punto.
- **Trazabilidad:** [Anexo D, resultado 1, línea base, meta, servicio, hito y evidencia](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L9). Diseño: [sd-03.tex, servicio de existencias como fuente de lo que se puede prometer](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L130). Catálogo relacionado: RF-127 a RF-129, según Anexo D.
- **Ámbito / servicio:** Retail; Servicio de existencias (Etapa 1).
- **Escenario, método y umbral:** probar el cálculo del disponible con el colchón de confianza por categoría y punto. Umbral de tolerancia contra conteo: **pendiente** de fijar al inicio del proyecto; no hay cifra en el Caso.
- **Evidencia prevista:** resultados de pruebas por categoría y punto, entradas de conteo y cálculo del colchón; el Anexo D identifica la prueba del cálculo.
- **Calendario y responsables:** despliegue gradual desde mes 16. Mide el jefe de proyecto del proponente; valida y firma la Contraparte Técnica.
- **Dependencia / brecha:** depende de datos de existencias y conteos confiables por tienda/categoría. Definir tolerancia y cobertura de despliegue antes de cerrar línea base. Responsable de cierre: dueño de existencias del proponente acuerda tolerancia y cobertura con jefatura de inventario del cliente antes de cerrar línea base.

<a id="r02"></a>

### R02 — Cancelaciones por falta de existencia (compartido)

- **Criterios internos:** C-R02-01 (tasa anual); C-R02-02 (evento anual).
- **Trazabilidad:** [Anexo D, resultado 2, línea 10](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L10). [Calendario de etapas del sd-03](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L138).
- **Ámbito / servicios:** Retail; Servicios de existencias y pedidos (pedidos en Etapa 2).
- **C-R02-01, escenario/método/umbral:** clasificar cancelaciones por causa durante los tres meses consecutivos previos al acta. Umbral anual <0,3 %. **Evidencia prevista:** exporte de pedidos cancelados, causa, denominador de pedidos y cálculo reproducible. La solución responde por falta de existencia o disponible mal calculado; el cliente, por preparación en tienda/CD.
- **C-R02-02, escenario/método/umbral:** medir todas las cancelaciones por falta de existencia durante el primer evento anual posterior al mes 21. Umbral: cero durante el evento. **Evidencia prevista:** registro de cada pedido/cancelación y reconciliación con el total de pedidos del evento.
- **Calendario y responsables:** C-R02-01, mes 16 parcial para categorías desplegadas y mes 21 completo. C-R02-02, mes 21 en prueba y primer evento anual posterior en operación. Líder de calidad del proponente integra mediciones; jefaturas de tienda y CD responden por preparación; Contraparte Técnica valida y firma.
- **Dependencia / brecha:** requiere causal de cancelación y cobertura del servicio de pedidos. Responsable de cierre: dueño de Pedidos del proponente define clasificación; responsables de operaciones de tienda/CD del cliente validan causas logísticas antes de la línea base. La fecha del evento la fija un tercero; no desplaza mes 56.

<a id="r03"></a>

### R03 — Cobro de unidades no entregables (piloto)

- **Síntesis y fuente:** consultar los criterios atomizados del piloto correspondiente, que conserva los IDs internos, método y evidencia: [pilotos.md](pilotos.md#r03). El [Anexo D, resultado 3, línea 11](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L11) define meta, servicio, hito y evidencia. Esta ficha no duplica criterios.
<a id="r04"></a>

### R04 — Exactitud del inventario (compartido)

- **Criterios internos:** C-R04-01 (diferencia); C-R04-02 (conteo sin cierre); C-R04-03 (medición diaria por categoría).
- **Trazabilidad:** [Anexo D, resultado 4, línea 12](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L12). [Despliegue gradual del sd-03](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L104).
- **Ámbito / servicio:** Retail; Servicio de existencias (Etapa 1).
- **C-R04-01, escenario/método/umbral:** comparar existencia registrada con conteo físico por categoría; diferencia <2 %. **Evidencia prevista:** cálculo por tienda/categoría y detalle de referencias contadas.
- **C-R04-02, escenario/método/umbral:** ejecutar conteo cíclico con la tienda abierta; meta de operación sin cierre, sin umbral numérico adicional. **Evidencia prevista:** calendario de conteos y registros de ejecución con tienda operativa.
- **C-R04-03, escenario/método/umbral:** calcular y publicar exactitud diariamente por categoría conforme a RT-05.29 citado en el Anexo D. **Evidencia prevista:** series diarias, fórmula y registro de actualización.
- **Calendario y responsables:** mes 16 despliegue gradual por tienda/categoría; mes 21, las 22 tiendas. La solución registra y calcula; cliente ejecuta conteos. Líder QA del proponente consolida evidencia; jefatura de inventario del cliente asegura ejecución; Contraparte Técnica firma.
- **Dependencia / brecha:** acordar frecuencia y ola de conteos, fórmula de diferencia y cobertura inicial. Responsable: dueño de existencias del proponente acuerda el método con jefatura de inventario del cliente antes de la línea base.

<a id="r05"></a>

### R05 — Merma por causa

- **Criterios internos:** C-R05-01 (causa en ajustes); C-R05-02 (merma); C-R05-03 (conciliación del desglose).
- **Trazabilidad:** [Anexo D, resultado 5, línea 13](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L13). Referencias: RN-12 y RF-138.
- **Ámbito / servicio:** Retail; Servicio de existencias.
- **C-R05-01, escenario/método/umbral:** revisar el universo mensual de ajustes; 100 % debe tener causa atribuida (propuesta). **Evidencia prevista:** ajustes con causa, universo y cálculo de cobertura.
- **C-R05-02, escenario/método/umbral:** medir merma sobre venta en los tres meses consecutivos previos al acta; umbral <1 % (Caso). **Evidencia prevista:** cálculo mensual con numerador y denominador conciliados.
- **C-R05-03, escenario/método/umbral:** verificar que los componentes del informe sumen el total de merma. **Evidencia prevista:** conciliación aritmética reproducible del informe mensual.
- **Calendario y responsables:** Anexo D fija mes 21. Dueño de existencias del proponente produce reporte y cálculo; jefatura de inventario/finanzas del cliente valida causas y base de ventas; Contraparte Técnica firma.
- **Dependencia / brecha:** Caso enumera cinco causas y RF-138 seis. Responsable de resolverlo: dueño de existencias del proponente concilia ambas taxonomías con jefatura de inventario del cliente al inicio; Contraparte Técnica aprueba catálogo antes de medir.

<a id="r06"></a>

### R06 — Propagación de cambios de precio (piloto)

- **Síntesis y fuente:** consultar los criterios atomizados del piloto correspondiente, que conserva los IDs internos, método y evidencia: [pilotos.md](pilotos.md#r06). El [Anexo D, resultado 6, línea 14](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L14) define meta, servicio, hito y evidencia. Esta ficha no duplica criterios.
<a id="r07"></a>

### R07 — Estado de puntos de exhibición

- **Criterio interno:** C-R07-01. Registrar el estado de todos los puntos de exhibición y cuáles están desactualizados.
- **Trazabilidad:** [Anexo D, resultado 7, línea 15](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L15). Diseño: [servicio de oferta comercial y área de mercadería](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L124).
- **Ámbito / servicio:** Retail; Servicio de oferta comercial (Etapa 1).
- **Escenario, método y umbral:** revisar indicador diario contra el universo de puntos de exhibición; umbral 100 % con estado registrado es propuesta del proponente. Método concreto de conciliación del universo: propuesta a definir con cliente.
- **Evidencia prevista:** indicador diario de puntos desactualizados (RF-029), historial de cambios y denominador de puntos activos.
- **Calendario y responsables:** mes 16. Proponente mide; Contraparte Técnica firma.
- **Dependencia / brecha:** confirmar qué cuenta como punto de exhibición y quién reporta reemplazo/cambio físico de etiqueta; el Caso no fija política de etiquetado en sala. Responsable de cierre: responsable de precios del cliente define el universo de puntos; dueño de oferta comercial del proponente acuerda registro y conciliación antes de línea base.

<a id="r08"></a>

### R08 — Historial de precio publicado

- **Criterios internos:** C-R08-01 (retención); C-R08-02 (recuperación).
- **Trazabilidad:** [Anexo D, resultado 8, línea 16](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L16). [Caso, RT-05.10, retención de la trazabilidad de precios por tres años](../../00_Bases/Caso_09_Cadena_Multitienda.md#L794). Diseño: [servicio de oferta comercial](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L124).
- **Ámbito / servicio:** Retail; Servicio de oferta comercial (Etapa 1).
- **C-R08-01, escenario/método/umbral:** verificar que el precio publicado por canal se conserva para cualquier instante de los últimos tres años. Umbral de retención: tres años, fijado por el Caso RT-05.10. **Evidencia prevista:** muestreo de registros en todo el período, política configurada y pruebas de integridad.
- **C-R08-02, escenario/método/umbral:** consultar precio por fecha, hora y canal; respuesta ≤1 minuto (propuesta del proponente, RNF-44/RNF-58). **Evidencia prevista:** consultas cronometradas con instante solicitado, resultado y duración.
- **Calendario y responsables:** mes 16. Dueño de oferta comercial y líder QA del proponente ejecutan pruebas; responsable de precios del cliente valida canales y datos de muestra; Contraparte Técnica firma.
- **Dependencia / brecha:** definir volumen y combinaciones de consulta para el ensayo. Responsable: dueño de oferta comercial propone la carga; responsable de precios del cliente valida representatividad antes de la línea base.

<a id="r09"></a>

### R09 — Precio cobrado frente al exhibido (compartido)

- **Criterio interno:** C-R09-01. La discrepancia del muestreo propio queda en 0,5 % o menos.
- **Trazabilidad:** [Anexo D, resultado 9, línea 17](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L17). Diseño: [servicios por frente/área](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L124).
- **Ámbito / servicios:** Retail; Servicios de oferta comercial y ventas (Etapa 1).
- **Escenario, método y umbral:** muestrear precios cobrados y exhibidos por tienda. Meta ≤0,5 % propuesta del proponente. La solución responde por precio publicado en cajas/canal digital; el cliente, por etiqueta física en sala.
- **Evidencia prevista:** registro de la muestra y comparación por tienda, con fuente de precio y destino.
- **Calendario y responsables:** mes 16; responsabilidad compartida y firma de Contraparte Técnica.
- **Dependencia / brecha:** SUP-08/SUP-09 y política de precios en sala siguen pendientes. El muestreo requiere tamaño, frecuencia y tolerancia aprobados; no deducirlos como requisito oficial. Responsable de cierre: gerente de precios del cliente resuelve SUP-08/SUP-09 y política física con asesoría correspondiente; dueño de oferta comercial del proponente define protocolo de muestra.

<a id="r10"></a>

### R10 — Estado único del pedido

- **Criterio interno:** C-R10-01. El estado del pedido es consistente y consultable por cliente, tienda, mesón, CD y vendedor externo.
- **Trazabilidad:** [Anexo D, resultado 10, línea 18](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L18). Diseño: [Etapa 2 y servicios de pedidos](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L167).
- **Ámbito / servicio:** Retail; Servicio de pedidos (Etapa 2).
- **Escenario, método y umbral:** auditar el mismo pedido en todos los canales y comparar estado/instante; consistencia conforme a RT-05.29. El umbral temporal de publicación de RT-05.29 requiere verificarse contra su fuente al diseñar el caso de prueba.
- **Evidencia prevista:** auditoría cruzada de estado (RF-052, RNF-04), con IDs de pedido y marcas de tiempo.
- **Calendario y responsables:** mes 21. Proponente mide; Contraparte Técnica firma.
- **Dependencia / brecha:** disponibilidad de interfaces de canales y catálogo de estados común; no confundir estado compartido con promesa de entrega cumplida. Responsable de cierre: dueño de pedidos del proponente acuerda catálogo de estados con responsables de los canales del cliente antes de pruebas integrales.

<a id="r11"></a>

### R11 — Asignación de punto de despacho

- **Criterio interno:** C-R11-01. El 100 % de asignaciones registra costo total y efecto sobre sala de venta.
- **Trazabilidad:** [Anexo D, resultado 11, línea 19](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L19). Diseño: [servicio de pedidos en Etapa 2](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L168).
- **Ámbito / servicio:** Retail; Servicio de pedidos (Etapa 2).
- **Escenario, método y umbral:** auditar cada asignación y verificar que el registro consigne los componentes del costo total; 100 % es propuesta del proponente. RF-076/RF-077 son referencias del Anexo D.
- **Evidencia prevista:** extracto de asignaciones con decisión, costo total y datos usados; conciliación de cobertura sobre el universo de asignaciones.
- **Calendario y responsables:** mes 21. Proponente mide; Contraparte Técnica firma.
- **Dependencia / brecha:** acordar componentes de costo y medida del efecto en sala; no hay fórmula del costo descrita en el Anexo D. Responsable de cierre: gerente de logística del cliente acuerda componentes de costo/efecto; dueño de pedidos del proponente implementa y documenta fórmula.

<a id="r12"></a>

### R12 — Atribución de despacho desde tienda

- **Criterio interno:** C-R12-01. Atribuir al 100 % los despachos desde tienda que surten pedidos de otros canales.
- **Trazabilidad:** [Anexo D, resultado 12, línea 20](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L20). Diseño: [servicio de comisiones, dependiente de pedidos y ventas](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L169).
- **Ámbito / servicio:** Retail; Servicio de comisiones (Etapa 2).
- **Escenario, método y umbral:** conciliar el universo de despachos desde tienda con su atribución; meta 100 % propuesta. RF-071, RF-054 y RF-055 citados por el Anexo D.
- **Evidencia prevista:** registro de atribución ligado al despacho, vendedor/canal y base de comisión.
- **Calendario y responsables:** mes 21. Proponente mide; Contraparte Técnica firma.
- **Dependencia / brecha:** requiere identificación de tienda que despacha y reglas de atribución/comisión vigentes; validar excepciones al inicio. Responsable de cierre: gerente de ventas del cliente valida regla de atribución; dueño de comisiones del proponente acuerda excepciones antes de línea base.

<a id="r13"></a>

### R13 — Aviso de devolución a vendedor marketplace

- **Criterio interno:** C-R13-01. Avisar al vendedor cada devolución en 15 minutos o menos.
- **Trazabilidad:** [Anexo D, resultado 13, línea 21](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L21). Diseño: [servicios de marketplace y posventa, Etapa 2](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L170).
- **Ámbito / servicios:** Retail; Servicios de marketplace y posventa (Etapa 2).
- **Escenario, método y umbral:** medir desde la ocurrencia registrada de cada devolución hasta el aviso al vendedor; ≤15 min (propuesta del proponente/RNF-66).
- **Evidencia prevista:** registro por devolución con tiempos de ocurrencia, emisión y recepción/entrega del aviso.
- **Calendario y responsables:** mes 21. Proponente mide; Contraparte Técnica firma.
- **Dependencia / brecha:** definir evento que inicia el reloj, canal de aviso y tratamiento de vendedor no disponible. La regla operativa de devolución debe quedar acordada. Responsable de cierre: gerente de marketplace del cliente aprueba evento de inicio y canal; dueño de marketplace del proponente fija reloj y reintentos.

<a id="r14"></a>

### R14 — Nivel de servicio de vendedores

- **Criterios internos:** C-R14-01 (cobertura); C-R14-02 (reglas comunicadas); C-R14-03 (consecuencia aplicada).
- **Trazabilidad:** [Anexo D, resultado 14, línea 22](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L22). Diseño: [Servicio de marketplace, Etapa 2](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L170).
- **Ámbito / servicio:** Retail; Servicio de marketplace (Etapa 2).
- **C-R14-01, escenario/método/umbral:** cotejar los 310 vendedores contra el informe mensual; 100 % con nivel de servicio medido (propuesta). **Evidencia prevista:** padrón fechado y resultado individual por vendedor.
- **C-R14-02, escenario/método/umbral:** verificar que cada vendedor recibió las reglas de medición vigentes antes del período evaluado. **Evidencia prevista:** versión de reglas y constancia fechada de comunicación.
- **C-R14-03, escenario/método/umbral:** revisar los casos en que el nivel medido activa una consecuencia acordada y comprobar aplicación consistente. **Umbral:** consecuencia según regla aprobada, sin inventar sanciones. **Evidencia prevista:** nivel calculado, regla aplicable y registro de la decisión/acción.
- **Calendario y responsables:** mes 21 y renovación anual. Dueño de marketplace del proponente genera medición; gerente de marketplace del cliente acuerda y comunica reglas a vendedores; Contraparte Técnica firma.
- **Dependencia / brecha:** deben definirse indicadores, consecuencias y constancia de comunicación. Responsable: gerente de marketplace del cliente aprueba las reglas con asesoría legal; dueño de marketplace del proponente configura medición antes de línea base.

<a id="r15"></a>

### R15 — Garantía legal resuelta en mesón (compartido)

- **Criterio interno:** C-R15-01. Cero derivaciones del cliente al fabricante o vendedor externo para resolver garantía legal.
- **Trazabilidad:** [Anexo D, resultado 15, línea 23](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L23). Diseño: [servicio de posventa en Etapa 2](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L171).
- **Ámbito / servicio:** Retail; Servicio de posventa (Etapa 2).
- **Escenario, método y umbral:** programa de cliente oculto en las 22 tiendas (RNF-69); la herramienta del mesón es responsabilidad de la solución y la atención sin derivación es responsabilidad del cliente. Umbral cero derivaciones, restricción 7 del Caso.
- **Evidencia prevista:** protocolo y registros de cliente oculto por tienda, resultado de cada interacción y derivación observada.
- **Calendario y responsables:** mes 21. Responsabilidad compartida; proponente aporta herramienta, cliente atiende; firma la Contraparte Técnica.
- **Dependencia / brecha:** capacitar al personal y asegurar cobertura del programa en 22 tiendas. Precisar muestra/frecuencia del cliente oculto como método operativo, no meta adicional. Responsable de cierre: gerente de atención del cliente asegura capacitación y cobertura; líder QA del proponente acuerda muestra/frecuencia con la Contraparte Técnica.

<a id="r16"></a>

### R16 — Tiempo de evaluación crediticia (piloto)

- **Síntesis y fuente:** consultar los criterios atomizados del piloto correspondiente, que conserva los IDs internos, método y evidencia: [pilotos.md](pilotos.md#r16). El [Anexo D, resultado 16, línea 24](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L24) define meta, servicio, hito y evidencia. Esta ficha no duplica criterios.
<a id="r17"></a>

### R17 — Constancia de información precontractual

- **Criterios internos:** C-R17-01 (contenido/version); C-R17-02 (medio); C-R17-03 (instante previo a aceptación); C-R17-04 (trazabilidad por operación).
- **Trazabilidad:** [Anexo D, resultado 17, línea 25](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L25). Diseño: [servicios financieros de Etapa 1](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L166).
- **Ámbito / servicio:** Filial emisora; Servicio de evidencia financiera.
- **C-R17-01:** comprobar que cada expediente identifica la versión exacta entregada. **Umbral:** trazabilidad por operación según Caso. **Evidencia:** versión y hash/identificador documental por operación.
- **C-R17-02:** verificar que se registra el medio de entrega usado. **Umbral:** dato de medio presente por operación. **Evidencia:** registro del canal/medio y vínculo al expediente.
- **C-R17-03:** comparar instante de entrega y aceptación. **Umbral:** entrega anterior a aceptación. **Evidencia:** marcas de tiempo sincronizadas y orden verificable.
- **C-R17-04:** recorrer una muestra de operaciones hasta recuperar la constancia completa. **Umbral:** registro estructurado recuperable para cada operación revisada. **Evidencia:** consulta y expediente vinculados a ID de operación.
- **Calendario y responsables:** mes 16. Dueño de evidencia financiera y QA del proponente prueban; oficial de cumplimiento/representante de la filial emisora valida contenido y flujo; Contraparte Técnica firma.
- **Dependencia / brecha:** definir catálogo/versionado del material y regla de reloj. Responsable: filial emisora, con asesoría jurídica, aprueba contenido/medio; dueño de evidencia financiera implementa y documenta versionado antes de línea base.

<a id="r18"></a>

### R18 — Repactación con consentimiento recuperable (piloto)

- **Síntesis y fuente:** consultar los criterios atomizados del piloto correspondiente, que conserva los IDs internos, método y evidencia: [pilotos.md](pilotos.md#r18). El [Anexo D, resultado 18, línea 26](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L26) define meta, servicio, hito y evidencia. Esta ficha no duplica criterios.
<a id="r19"></a>

### R19 — Conservación y recuperación de evidencia

- **Criterios internos:** C-R19-01 (retención); C-R19-02 (recuperación).
- **Trazabilidad:** [Anexo D, resultado 19, línea 27](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L27). Diseño: [Servicio de evidencia financiera, Etapa 1](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L166).
- **Ámbito / servicio:** Filial emisora; Servicio de evidencia financiera.
- **C-R19-01, escenario/método/umbral:** verificar política y configuración de retención desde cada operación durante el plazo del crédito más seis años; simulacro que incluye expediente de diez años. **Evidencia prevista:** política aprobada, configuración y consulta de fechas de vencimiento. El período es propuesta del proponente, RNF-42/43/57.
- **C-R19-02, escenario/método/umbral:** atender requerimiento simulado de la autoridad y recuperar expediente en ≤5 minutos. **Evidencia prevista:** acta, solicitud, ID, tiempo medido, integridad y legibilidad.
- **Calendario y responsables:** mes 16 se demuestra custodia/recuperación; se mantiene durante operación meses 21–56. Responsable de cumplimiento de la filial aprueba plazo y base jurídica; dueño de evidencia financiera opera prueba; Contraparte Técnica firma.
- **Dependencia / brecha:** validar política, capacidad, base jurídica y formatos. Responsable: oficial de cumplimiento/asesoría jurídica de la filial aprueba; arquitectura y dueño de evidencia financiera calculan capacidad antes de cerrar diseño.

<a id="r20"></a>

### R20 — Bloqueo de aceptación sin información completa

- **Criterio interno:** C-R20-01. El proceso rechaza aceptar el crédito si falta información precontractual obligatoria.
- **Trazabilidad:** [Anexo D, resultado 20, línea 28](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L28). Diseño: [originación y evidencia financiera en Etapa 1](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L164).
- **Ámbito / servicios:** Filial emisora; Servicios de originación de crédito y evidencia financiera.
- **Escenario, método y umbral:** prueba negativa de aceptación con uno o más elementos incompletos; la operación se rechaza. Esta meta es propuesta del proponente; referencias RF-199/RF-206.
- **Evidencia prevista:** ejecución de casos negativos, resultado de rechazo y auditoría de que no se creó aceptación/crédito.
- **Calendario y responsables:** mes 16. Proponente mide; Contraparte Técnica firma.
- **Dependencia / brecha:** filial emisora y asesoría jurídica deben confirmar lista de información obligatoria y condición de aceptación; no permitir excepción manual sin trazabilidad. Responsable de cierre: cumplimiento y asesoría jurídica de la filial emisora aprueban la lista; dueño de originación del proponente aplica el bloqueo.

<a id="r21"></a>

### R21 — Separación de datos retail y filial (piloto)

- **Síntesis y fuente:** consultar los criterios atomizados del piloto correspondiente, que conserva los IDs internos, método y evidencia: [pilotos.md](pilotos.md#r21). El [Anexo D, resultado 21, línea 29](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L29) define meta, servicio, hito y evidencia. Esta ficha no duplica criterios.
<a id="r22"></a>

### R22 — Registro de cruces entre ámbitos

- **Criterio interno:** C-R22-01. Registrar el 100 % de cruces con finalidad, base y autorización.
- **Trazabilidad:** [Anexo D, resultado 22, línea 30](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L30). Diseño: [el servicio de control de cruces es el paso entre negocios](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L248).
- **Ámbito / servicio:** Compartido en frontera retail–filial; Servicio de control de cruces (Etapa 1).
- **Escenario, método y umbral:** auditar trimestralmente una muestra de cruces y comprobar campos de finalidad, base y autorización. Meta de 100 % citada como RF-165; auditoría propuesta por el proponente. La fuente indica que la realiza el encargado de cumplimiento del cliente.
- **Evidencia prevista:** extracto del registro y acta de auditoría trimestral, con universo/muestra y excepciones.
- **Calendario y responsables:** mes 16 para capacidad; auditorías trimestrales durante operación hasta mes 56. Proponente mide; encargado de cumplimiento del cliente audita; Contraparte Técnica firma.
- **Dependencia / brecha:** acordar taxonomía de finalidades/bases y acceso del encargado de cumplimiento. El alcance de la muestra y el criterio estadístico están pendientes de acordar. Responsable de cierre: encargado de cumplimiento del cliente aprueba muestra y taxonomía; dueño de control de cruces del proponente asegura campos y extracción.

<a id="r23"></a>

### R23 — Hitos del plan de remediación

- **Criterio interno:** C-R23-01. Cumplir todos los hitos instruidos por la autoridad antes de 2029, a más tardar en mes 24.
- **Trazabilidad:** [Anexo D, resultado 23, línea 31](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L31). Diseño: [prioridad del negocio financiero por fechas externas](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L181).
- **Ámbito / servicios:** Filial emisora; Servicios de originación de crédito, cartera de crédito y evidencia financiera.
- **Escenario, método y umbral:** verificar cada hito del plan contra su fecha y respaldo formal de cumplimiento; fecha límite mes 24 (diciembre de 2028, bajo SUP-26). El Caso fija el resultado.
- **Evidencia prevista:** informe de cumplimiento por hito del proponente que respalde el acta de la autoridad.
- **Calendario y responsables:** operación, a más tardar mes 24. Proponente prepara informe; Contraparte Técnica firma y la autoridad emite/acepta su acta según corresponda.
- **Dependencia / brecha:** obtener plan oficial, hitos, criterios y calendario del expediente de remediación; los servicios deben aportar evidencia regulatoria completa. Responsable de cierre: oficial de cumplimiento de la filial entrega plan/hitos oficiales; líder del proyecto del proponente arma evidencia y calendario de remediación.

<a id="r24"></a>

### R24 — Migración conciliada de cartera (piloto)

- **Síntesis y fuente:** consultar los criterios atomizados del piloto correspondiente, que conserva los IDs internos, método y evidencia: [pilotos.md](pilotos.md#r24). El [Anexo D, resultado 24, línea 32](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L32) define meta, servicio, hito y evidencia. Esta ficha no duplica criterios.
<a id="r25"></a>

### R25 — Degradación y carga del evento anual

- **Criterios internos:** C-R25-01 (orden de degradación); C-R25-02 (suspensión de categoría); C-R25-03 (capacidad de pedidos).
- **Trazabilidad:** [Anexo D, resultado 25, línea 33](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L33). Diseño: [híbrido y 24 horas sin enlace](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L98); [Etapa 2, Servicio de pedidos](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L168).
- **Ámbito / servicios:** Retail y base tecnológica; existencias (Etapa 1), pedidos (Etapa 2).
- **C-R25-01, escenario/método/umbral:** provocar degradaciones definidas y verificar aplicación del orden declarado. **Umbral:** orden documentado y probado (propuesta). **Evidencia:** secuencia de estímulos, decisiones y bitácoras.
- **C-R25-02, escenario/método/umbral:** suspender publicación de una categoría durante degradación y comprobar que no se ofrecen unidades de esa categoría. **Umbral:** capacidad operativa de suspensión, propuesta del proponente. **Evidencia:** cambio de estado, consultas antes/después y trazas.
- **C-R25-03, escenario/método/umbral:** prueba de carga con 104.000 pedidos en tres días (RNF-22). **Evidencia:** configuración, entradas, conteo aceptado/rechazado y reporte de ejecución. No se añade una cifra de throughput o concurrencia.
- **Calendario y responsables:** degradación/suspensión mes 16; carga completa mes 21; operación en primer evento posterior. Arquitectura y dueños de existencias/pedidos del proponente diseñan y ejecutan; responsable de operación retail del cliente aprueba el orden; líder QA registra; Contraparte Técnica firma.
- **Dependencia / brecha:** falta acordar orden y estímulos. Responsable: gerente de operaciones retail del cliente aprueba prioridades; arquitectura y dueños de servicio documentan la respuesta antes del ensayo. Fecha real del evento la fija un tercero y no cambia mes 56.

<a id="r26"></a>

### R26 — Estado, aviso y entrega del pedido (compartido)

- **Criterios internos:** C-R26-01 (estado); C-R26-02 (aviso previo al cobro); C-R26-03 (entrega en fecha).
- **Trazabilidad:** [Anexo D, resultado 26, línea 34](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L34). [Pedidos se incorporan en Etapa 2](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L167).
- **Ámbito / servicios:** Retail; Servicios de pedidos y existencias.
- **C-R26-01, escenario/método/umbral:** consultar un pedido desde cliente, tienda y mesón; comprobar estado común e historial. **Evidencia:** auditoría cruzada con pedido, canal, instante y estado (RF-052).
- **C-R26-02, escenario/método/umbral:** pedido sin unidad disponible; verificar aviso antes del cobro (RT-16.21). **Evidencia:** trazas de disponibilidad, aviso y captura, en orden temporal.
- **C-R26-03, escenario/método/umbral:** medir pedidos entregados en fecha contra promesa; meta >97 % (Caso). **Evidencia:** universo, promesa original, fecha efectiva y cálculo. Solución responde por estado/aviso; el cliente por cumplimiento físico.
- **Calendario y responsables:** mes 21. Dueños de pedidos/existencias y QA del proponente miden estado y aviso; jefe de logística del cliente responde por entrega; Contraparte Técnica valida y firma.
- **Dependencia / brecha:** enlazar pedidos con contactos entrantes y fijar exclusiones justificadas. Responsable: dueño de pedidos del proponente acuerda definición de estado/contacto con servicio al cliente y logística del cliente antes de línea base.

<a id="r27"></a>

### R27 — Causas de diferencias de inventario por tienda

- **Criterio interno:** C-R27-01. Atribuir causa al 100 % de las diferencias de la tienda de la jefatura que valida.
- **Trazabilidad:** [Anexo D, resultado 27, línea 35](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L35). Diseño: [responsabilidad de existencias](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L130).
- **Ámbito / servicio:** Retail; Servicio de existencias (Etapa 2, según hito del Anexo D).
- **Escenario, método y umbral:** revisar informe mensual de merma con una jefatura de tienda; comprobar que todas las diferencias de su tienda tengan causa. 100 % es propuesta del proponente.
- **Evidencia prevista:** informe mensual y acta de revisión con jefatura, tienda y período.
- **Calendario y responsables:** mes 21. Proponente mide; Contraparte Técnica firma.
- **Dependencia / brecha:** acordar tienda de revisión, taxonomía de causas y datos de conteo; pendiente la diferencia entre cinco causas del Caso y seis en RF-138. Responsable de cierre: jefatura de inventario del cliente fija tienda/revisión; dueño de existencias del proponente resuelve taxonomía con el responsable de RF-138.

<a id="r28"></a>

### R28 — Apertura de tarjeta e información completa (piloto)

- **Síntesis:** velocidad e información se verifican por separado para que un buen tiempo no oculte una entrega incompleta. Tiempo: reutiliza C-R16-01 en [pilotos.md](pilotos.md#r16). Bloqueo/constancia: consultar [R20, bloqueo de aceptación sin información completa](#r20) y el criterio de evidencia de R17 en esta página. La meta del resultado 28 es ≤8 s para evaluación y entrega de información obligatoria antes de aceptar.
- **Ámbito / servicios:** Filial emisora; Servicios de originación de crédito y evidencia financiera (Etapa 1).
- **Trazabilidad:** [Anexo D, resultado 28, línea 36](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#L36). [Diseño de Etapa 1](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex#L164).
- **Calendario y responsables:** mes 16. Dueño de originación y QA del proponente coordinan el ensayo; filial emisora valida que medir velocidad no recorte el flujo precontractual; Contraparte Técnica firma.
- **Dependencia / brecha:** asegurar que los relojes de evaluación y constancia midan componentes distintos y correlacionables. Responsable: dueño de originación define los eventos temporales con dueño de evidencia financiera y cumplimiento de la filial antes de la prueba.

## Control de cobertura

Este artefacto contiene 28 fichas, una por cada resultado del Anexo D. Se desarrollan 21 fichas en esta página; seis quedan en síntesis vinculada a los pilotos (R03, R06, R16, R18, R21 y R24), y R28 reutiliza criterios de R16/R17/R20. Los criterios internos están atomizados por método y umbral; los identificadores se mantienen dentro de cada ficha. Los seis pilotos remiten a los IDs desarrollados en pilotos.md. No se han creado IDs RF/RNF/RN ni metas oficiales. Quedan señaladas como propuestas o pendientes las decisiones de umbral, método o datos que el Anexo D atribuye al proponente o deja sin resolver.
