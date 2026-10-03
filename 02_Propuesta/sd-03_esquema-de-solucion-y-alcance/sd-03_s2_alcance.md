---
id: T7-03-3.2
tipo: seccion
parte: T7-03
titulo: Alcance
estado: borrador
bases: []
requisitos:
  - RF-004
  - RF-007
  - RF-013
  - RF-020
  - RF-021
  - RF-023
  - RF-028
  - RF-043
  - RF-045
  - RF-046
  - RF-051
  - RF-052
  - RF-055
  - RF-077
  - RF-084
  - RF-086
  - RF-089
  - RF-092
  - RF-095
  - RF-097
  - RF-100
  - RF-106
  - RF-119
  - RF-124
  - RF-127
  - RF-128
  - RF-137
  - RF-139
  - RF-143
  - RF-157
  - RF-161
  - RF-163
  - RF-165
  - RF-166
  - RF-170
  - RF-174
  - RF-185
  - RF-188
  - RF-190
  - RF-198
  - RF-199
  - RF-206
  - RF-208
  - RF-210
  - RF-213
  - RF-216
  - RF-220
  - RNF-05
  - RNF-06
  - RNF-10
  - RNF-16
  - RNF-17
  - RNF-18
  - RNF-19
  - RNF-20
  - RNF-21
  - RNF-22
  - RNF-23
  - RNF-24
  - RNF-25
  - RNF-26
  - RNF-27
  - RNF-28
  - RNF-30
  - RNF-31
  - RNF-32
  - RNF-42
  - RNF-44
  - RNF-57
  - RNF-58
depende_de: []
adjuntos: []
jira: []
cifras: []
origen: "05_Gestion/migraciones/fuentes/T7-03_Informes4_source.md#bloques-3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54"
actualizado: 2026-09-30
---
# 3.2 Alcance



<!-- contenido migrado desde la fuente; permanece en borrador y requiere revisión humana -->



<!-- origen: T7-03_Informes4_source.md | bloque 3 -->

<!-- origen: T7-03_Informes4_source.md | bloque 4 -->

### Alcance de la Etapa 1 y de la Etapa 2

<!-- origen: T7-03_Informes4_source.md | bloque 5 -->

## Objetivos del proyecto

Los objetivos se formulan bajo el estándar SMART: resultados específicos, metas cuantificadas, viabilidad arquitectónica y un horizonte anclado a los 56 meses del contrato. Ningún objetivo se redacta como intención ni admite verificación subjetiva.

<!-- origen: T7-03_Informes4_source.md | bloque 6 -->

### Objetivo General

Dotar a Multitiendas Ancoa S.A. de una plataforma híbrida orientada a eventos que garantice sus cuatro promesas comerciales (existencia, precio, entrega y condiciones crediticias). Esto exige operar sobre registros de exactitud comprobable, asegurar una separación auditable entre el retail y la filial emisora, y no degradar la continuidad operativa de las 22 sucursales ni exceder las ventanas de intervención.

El éxito global exige el cumplimiento de las 12 métricas específicas, una auditoría de dominios sin hallazgos y la migración total de la cartera sin divergencias contables.

<!-- origen: T7-03_Informes4_source.md | bloque 7 -->

### Objetivos Específicos

Tabla 3.13:** Objetivos específicos del proyecto, métricas y medios de verificación.

**ID / Dimensión:** **OE-01 Existencia**. **Objetivo Específico:** Reducir la discrepancia de inventario físico-lógico mediante conteo continuo ABC y clasificación de ajustes.. **Línea Base a Meta:** 12,4 % a ≤ 2 % por categoría. **Medio de Verificación:** Indicador diario de exactitud y auditoría independiente..

**ID / Dimensión:** **OE-02 Existencia**. **Objetivo Específico:** Eliminar cancelaciones por promesas sin respaldo físico mediante cálculo de disponibilidad con colchón dinámico.. **Línea Base a Meta:** 1,9 % a ≤ 0,3 % anual y cero quiebres en evento. **Medio de Verificación:** Medición mensual de pedidos aceptados..

**ID / Dimensión:** **OE-03 Existencia**. **Objetivo Específico:** Segregar la merma aislando la pérdida física del descuadre administrativo mediante tipificación obligatoria.. **Línea Base a Meta:** 0 % a 100 % de ajustes clasificados en 6 tipologías. **Medio de Verificación:** Reporte mensual conciliado con cierre contable..

**ID / Dimensión:** **OE-04 Precio**. **Objetivo Específico:** Eliminar divergencia entre precio exhibido y cobrado, condicionando el POS a la confirmación de recambio físico.. **Línea Base a Meta:** 11 % a ≤ 0,5 % de discrepancia. **Medio de Verificación:** Muestreo interno periódico y registro de incidentes..

**ID / Dimensión:** **OE-05 Precio**. **Objetivo Específico:** Acreditar el precio histórico publicado ante requerimientos regulatorios en cualquier canal e instante.. **Línea Base a Meta:** Nula a 100 % de consultas resueltas en ≤ 1 min. **Medio de Verificación:** Prueba de recuperación sobre ventana histórica de 3 años..

**ID / Dimensión:** **OE-06 Entrega**. **Objetivo Específico:** Elevar el cumplimiento de fecha de entrega sustituyendo asignación por proximidad por Costo Total de Servir.. **Línea Base a Meta:** 81 % a ≥ 97 % de pedidos en plazo. **Medio de Verificación:** Medición continua sobre estado único del pedido..

**ID / Dimensión:** **OE-07 Entrega**. **Objetivo Específico:** Suprimir la captura financiera sobre unidades no disponibles mediante preautorización sin captura.. **Línea Base a Meta:** Cobro inicial a Cero cobros sostenidos por pedidos no cumplibles. **Medio de Verificación:** Conciliación diaria de preautorizaciones y capturas..

**ID / Dimensión:** **OE-08 Crédito**. **Objetivo Específico:** Acreditar el consentimiento y entrega de información precontractual en toda repactación u originación.. **Línea Base a Meta:** 1.240 repactaciones sin respaldo a Cero operaciones sin evidencia. **Medio de Verificación:** Auditoría censal y prueba de recuperación WORM..

**ID / Dimensión:** **OE-09 Crédito**. **Objetivo Específico:** Reducir el tiempo de evaluación crediticia en POS sin diferir el flujo de cumplimiento normativo.. **Línea Base a Meta:** 40s a 3m a ≤ 8s (p95) sin mayor tiempo de atención. **Medio de Verificación:** Medición E2E instrumentada en mesón y caja..

**ID / Dimensión:** **OE-10 Crédito**. **Objetivo Específico:** Migrar cartera viva (620k clientes) mitigando el riesgo normativo de la plataforma obsoleta.. **Línea Base a Meta:** Plataforma 2011 a 100 % migrado con cero divergencias. **Medio de Verificación:** Conciliación diaria automatizada por ola de migración..

**ID / Dimensión:** **OE-11 Frontera**. **Objetivo Específico:** Implementar y auditar separación lógica entre retail y filial de crédito, registrando todo cruce.. **Línea Base a Meta:** Separación parcial a Auditoría sin hallazgos y 100 % de cruces registrados. **Medio de Verificación:** Informe de auditoría independiente..

**ID / Dimensión:** **OE-12 Continuidad**. **Objetivo Específico:** Asegurar venta y crédito offline ante pérdida de enlace, con reconciliación automática post-contingencia.. **Línea Base a Meta:** Detención total a ≥ 8 hrs operación autónoma; cuadratura ≤ 30 min. **Medio de Verificación:** Prueba de desconexión en horario comercial..

<!-- origen: T7-03_Informes4_source.md | bloque 8 -->

### Responsabilidad sobre la adopción y los indicadores

El modelo de gobierno del proyecto distingue estrictamente entre la capacidad técnica de la plataforma y la disciplina operativa de la compañía.

* **Indicadores garantizados (100% sistémicos):** Los objetivos OE-03, OE-05 y OE-07 a OE-12 dependen íntegramente de la arquitectura entregada. Se comprometen y garantizan sin condición de adopción por parte del usuario.

* **Indicadores compartidos (Sistémicos \+ Operativos):** Los objetivos comerciales OE-01, OE-02, OE-04 y OE-06 requieren un esfuerzo conjunto. La solución técnica provee la capacidad (ej. algoritmo ATP, ruteo de etiquetas), pero el CLIENTE ejecuta el proceso físico en sala (conteo, escaneo, picking). El acta de aceptación técnica aislará el rendimiento del software de la adopción humana, desplegando estas funciones primero en pilotos acotados para detectar desviaciones operativas antes del escalamiento.

<!-- origen: T7-03_Informes4_source.md | bloque 9 -->

### Supuestos

El Capítulo 16 de las Bases Técnicas enumera 25 decisiones estructurales que Ancoa delegó intencionalmente en los proponentes. Cada una admite múltiples enfoques arquitectónicos con impactos divergentes en costo, riesgo y continuidad operativa.

Este capítulo resuelve la totalidad de estas decisiones. Ninguna se traslada a una fase posterior ni se resuelve por omisión. Cada resolución queda inscrita en el registro consolidado de supuestos bajo la nomenclatura SUP-nn. Cuando una decisión depende de un dato empírico que la compañía hoy no posee, la arquitectura define un valor inicial fundamentado y un mecanismo de recalibración durante la fase de levantamiento. Desde la ingeniería del proyecto, se establece que es preferible comprometer y gobernar un parámetro explícito antes que diseñar sobre vacíos operacionales.

Cinco de estas decisiones condicionan la viabilidad central del proyecto y se desarrollan en extenso, respondiendo a interrogantes críticas de arquitectura, riesgo y cumplimiento regulatorio:

1. ¿De dónde se extrae el dato de inventario que rige la promesa de venta?

2. ¿Cuál es la estrategia de reemplazo para el sistema central monolítico de 2009?

3. ¿Cuál es la frontera lógica de datos entre el negocio de retail y la filial de crédito?

4. ¿Cómo se unifica la identidad del cliente sin vulnerar dicha frontera?

5. ¿Cómo se garantiza la operación crediticia offline sin violar el mandato fiduciario?

6. ¿Cómo se migra una cartera viva de 620.000 deudores mitigando el riesgo sistémico?

Las diecinueve decisiones restantes se presentan agrupadas por ámbito de negocio. Finalmente, la sección 3.2.7 aborda cinco vacíos operacionales detectados por este proponente, incluyendo la resolución de una contradicción directa entre dos restricciones catalogadas como no negociables en las bases.

<!-- origen: T7-03_Informes4_source.md | bloque 10 -->

### SUP-01: El origen y cálculo de la disponibilidad de inventario

Las auditorías de conteo cíclico evidencian una discrepancia de inventario del 12,4 %; sin embargo, la disponibilidad del canal digital se calcula sobre esta base inexacta aplicando un margen de seguridad estático y obsoleto heredado de 2019\. Al ser un parámetro transversal que omite la varianza de exactitud entre categorías y sucursales, este modelo generó un impacto operacional y comercial crítico en el evento de junio de 2026, donde se autorizaron 2.840 transacciones sin respaldo físico. Este incidente no responde a una falla de ejecución de código, sino a una falencia estructural en las reglas de negocio: la ausencia de un índice de confianza dinámico que pondere la calidad del dato de inventario antes de comprometer la promesa de venta.

Se establece la creación de un servicio centralizado, Available to Promise (ATP), que pasa a ser la única fuente de verdad para los cuatro canales, prohibiendo por diseño técnico el acceso directo al inventario en bruto. Este componente calcula la cantidad comprometible restando del registro las unidades reservadas, los pedidos aceptados y un colchón de incertidumbre dinámico. Este parámetro se obtiene de la exactitud histórica medida por el conteo cíclico para esa categoría en ese punto de venta: una categoría con buen historial arriesga poco margen; una con historial de errores arriesga mucho más. El colchón se amplía automáticamente durante el evento anual, y el servicio entrega la disponibilidad acompañada de un nivel de confianza, evitando compromisos comerciales insostenibles.

Publicar con colchón implica mostrar menos disponibilidad aparente y asumir una menor venta en el corto plazo. Se acepta esta restricción deliberadamente: una venta que no se puede cumplir genera un daño mayor al negocio. El colchón deja de ser una variable rígida en el código y se consolida como un parámetro gobernable que la Gerencia de Logística define, firma y versiona. El riesgo inverso (un colchón sobrecalibrado) se monitorea comparando la tasa de cancelación resultante contra el 1,9 % anual actual.

<!-- origen: T7-03_Informes4_source.md | bloque 11 -->

### SUP-02: Integración y transición del sistema central de retail de 2009

El sistema central de retail implantado en 2009 es una de las nueve plataformas del entorno y participa en capacidades relevantes como el maestro de artículos, las compras, el inventario contable y los precios. No constituye por sí solo el problema que aborda el proyecto: este reside en la interacción entre nueve plataformas de seis proveedores mediante catorce interfaces punto a punto, en su mayoría nocturnas y sin un mapa completo disponible para el mandante. Por ello, la solución no plantea reemplazar de una vez una plataforma ni atribuye a este sistema la totalidad de las brechas operativas. Se levantará y documentará el mapa de integraciones como trabajo del proyecto, se evitarán nuevas conexiones punto a punto y se priorizará el desacoplamiento gradual de los flujos según criticidad y dependencias.

La transición comienza con el levantamiento de las catorce interfaces y sus dependencias; el mapa resultante será un entregable del proyecto, no un insumo que se presume disponible. Sobre esa evidencia se definirá qué flujos conviene desacoplar mediante integración orientada a eventos y cuáles requieren una fachada de API u otro mecanismo compatible con cada plataforma. La intervención se desplegará gradualmente, priorizando los flujos de disponibilidad y precio, con pruebas de interceptación y reversa antes de ampliar cada cambio. La convivencia con las plataformas existentes se mantendrá mientras las capacidades y obligaciones operativas lo requieran; cualquier reemplazo o retiro se decidirá por capacidad y evidencia, no por una premisa de sustitución integral.

La estrategia queda sujeta a confirmar durante el levantamiento la observabilidad, las interfaces disponibles y las restricciones de cada proveedor; no se presume que todas las integraciones puedan sustituirse individualmente ni que el sistema central admita una fachada sin cambios. Para reducir el riesgo de flujos paralelos no documentados —incluidas escrituras directas a bases de datos— se ejecutará una prueba piloto de interceptación sobre un flujo de carga de precios. Sus resultados determinarán el mecanismo de transición aplicable y los controles necesarios antes de escalar.

<!-- origen: T7-03_Informes4_source.md | bloque 12 -->

### SUP-03 y SUP-04: Frontera de datos e Identidad Unificada del Cliente

El gobierno de datos impone resolver la fricción legal entre el negocio de retail (sujeto a la Ley del Consumidor) y el negocio financiero (entidad fiscalizada). La construcción de una vista unificada de cliente exige establecer primero las barreras de privacidad, garantizando una separación lógica auditable.

El perímetro de cruce de datos se establece en tres dimensiones. Sobre el contenido, sólo transita la información declarada en un inventario de interfaces autorizadas, fundamentada en bases de licitud explícitas (Ley N° 21.719). Sobre la direccionalidad, la restricción es bidireccional; el motor de originación crediticia no puede invocar atributos comerciales sin respaldo legal. Sobre el control técnico, un gestor de consentimientos deniega por omisión (Zero Trust) todo flujo no autorizado, registrando tanto cruces efectivos como intentos bloqueados. Consecuentemente, el motor de marketing excluye por diseño los atributos financieros.

La identidad (SUP-03) se resuelve mediante una arquitectura en dos capas. En el dominio retail, un motor de resolución unifica interacciones (RUT \+ coincidencia probabilística) mediante eventos asíncronos. Hacia el dominio financiero, la interoperabilidad se ejecuta estrictamente mediante consultas síncronas bajo demanda (ej. solicitud explícita de estado de cuenta), contra una zona neutral que expone únicamente identificadores técnicos anonimizados. Se asume el costo operacional de latencia en consultas transfronterizas como una condición innegociable para asegurar el cumplimiento regulatorio.

<!-- origen: T7-03_Informes4_source.md | bloque 13 -->

### SUP-07: Continuidad de la operatoria de crédito ante desconexión de sucursales

El diseño arquitectónico debe resolver la fricción directa entre la exigencia de continuidad operativa y el cumplimiento normativo financiero. Por un lado, el negocio exige garantizar la venta y cobro offline durante un mínimo de ocho horas; un escenario de contingencia de alta probabilidad considerando que 14 de las 22 sucursales dependen de redes de terceros. Dado que la tarjeta propia concentra el 38 % de las transacciones, inhabilitarla invalida la continuidad real. Por otro lado, la filial emisora opera como entidad fiscalizada, imponiendo la restricción ineludible de acreditar y controlar el riesgo de cada operación.

Se establece un modelo de contingencia offline basado en la preautorización de cupos. Sin conexión, el punto de venta local no ejecuta evaluación de riesgo, sino que consume un cupo rotativo previamente aprobado y sincronizado en el servidor local, encolando la operación para su consolidación diferida. La exposición se mitiga mediante cuatro umbrales dinámicos calculados según el volumen real de la tienda: (1) límite transaccional unitario, (2) límite acumulado por cliente, (3) umbral de transacciones consecutivas y (4) ventana de caducidad por reconexión. Acciones que exigen perfilamiento crediticio (apertura de tarjeta, aumento de cupo) quedan bloqueadas por diseño sin enlace.

La asimetría del riesgo fundamenta la decisión: el riesgo real no es crediticio (el cupo fue evaluado pre-contingencia), sino el fraude por doble consumo. Bajo los parámetros del caso, la exposición por tienda ronda los \$150.000 frente a la mitigación de una pérdida de venta proyectada en \$10.000.000 por evento.

<!-- origen: T7-03_Informes4_source.md | bloque 14 -->

### SUP-25: Estrategia de migración de la cartera activa de crédito

La migración se define como el traslado concurrente de 620.000 clientes con saldo vigente, repactaciones y procesos de cobranza/judiciales en curso. Dada la naturaleza de la entidad fiscalizada, se impone tolerancia nula a la divergencia de saldos. La restricción temporal es inamovible (2029), dictaminada por el fin de soporte del core de 2011 y el hito de remediación normativo.

Se descarta el reemplazo big bang. La transición se ejecutará mediante olas de coexistencia, operando ambas plataformas en paralelo con una conciliación diaria automatizada. Un umbral de discrepancia predefinido actuará como freno de emergencia (circuit breaker), deteniendo el avance de la ola ante divergencias contables. El mecanismo de rollback se mantendrá activo y validado durante toda la ventana de coexistencia.

El cronograma contractual se mantiene inalterado; la estrategia radica en separar la habilitación técnica de la ejecución operativa. El corte final ocurre en la Etapa 2, pero los componentes habilitantes (gestor de consentimientos, saneamiento de datos y motor de conciliación) se despliegan en la Etapa 1\. Adelantar la ingeniería de datos financieros a la fase inicial es la única vía crítica viable para asegurar un margen de maniobra ante el límite regulatorio de 2029\.

<!-- origen: T7-03_Informes4_source.md | bloque 15 -->

### Resolución de las decisiones restantes

<!-- origen: T7-03_Informes4_source.md | bloque 16 -->

#### La existencia física: cómo se cuenta, cómo se reserva y dónde se almacena

Tabla 3.1:** Resolución de decisiones de existencia física, canal y merma.

**ID:** **SUP-12**. **El dolor operativo y comercial:** La colisión de canales genera pérdida de venta cierta. Cuando un cliente digital reserva una unidad en el carro, el vendedor presencial queda bloqueado para facturar esa misma unidad física.. **La resolución arquitectónica y de negocio:** Se implementa una reserva temporal parametrizable al agregar al carro. La prelación de venta favorece al canal presencial: si la transacción física se concreta, la reserva digital se revoca automáticamente y el pedido web se enruta al motor de compensación, protegiendo la comisión y la venta confirmada de la sala..

**ID:** **SUP-17**. **El dolor operativo y comercial:** La merma (1,9 % de las ventas) se consolida bajo un indicador único, impidiendo a las jefaturas de tienda aislar la pérdida por hurto de los descuadres puramente administrativos.. **La resolución arquitectónica y de negocio:** Todo ajuste de inventario exigirá clasificación obligatoria en seis tipologías tipificadas (incluyendo error de recepción y daño). Este paso forzoso en el flujo de sistema permite segregar contablemente la merma y auditar la gestión real del inventario..

**ID:** **SUP-18**. **El dolor operativo y comercial:** El cálculo del margen de confianza (SUP-01) depende de medir dónde falla el inventario, pero los conteos paralizan la operación comercial.. **La resolución arquitectónica y de negocio:** Se establece un modelo de conteo continuo ABC (A: semanal, B: mensual, C: trimestral) ejecutado en la ventana valle de flujo (10:00 \- 13:00). Se configuran disparadores de conteo ciego automático ante quiebres de stock en preparación, obsolescencia anómala o saldos negativos, sin exigir cierres de local..

**ID:** **SUP-20**. **El dolor operativo y comercial:** El CD de Concepción opera sobre procesos manuales, inyectando inexactitud directa al registro nacional y comprometiendo las promesas de entrega en la zona sur.. **La resolución arquitectónica y de negocio:** Se excluye temporalmente este nodo logístico como origen de disponibilidad para el canal digital hasta su estabilización. Su integración futura al WMS corporativo se condiciona a un caso de negocio de modernización. Se asume la degradación temporal de tiempos de entrega en el sur para proteger la exactitud de la promesa global..

<!-- origen: T7-03_Informes4_source.md | bloque 17 -->

#### El precio: consistencia omnicanal y evidencia fiscal

Tabla 3.2:** Resolución de decisiones de consistencia de precios y trazabilidad fiscal.

**ID:** **SUP-08**. **El dolor operativo y comercial:** La asincronía entre el maestro de precios y el etiquetado físico (11 % de discrepancia) genera fricción en caja y vulnerabilidad ante fiscalizaciones de protección al consumidor.. **La resolución arquitectónica y de negocio:** Se establece primacía del precio exhibido físicamente. Ante una discrepancia detectada en caja, el sistema adopta automáticamente el valor menor, imputando la diferencia como pérdida operativa de la sucursal. Esta penalización financiera directa fuerza la alineación logística del etiquetado local..

**ID:** **SUP-09**. **El dolor operativo y comercial:** Las ventanas de actualización manual dejan un margen de hasta 24 horas donde el sistema central y la sala operan con listas de precios desfasadas.. **La resolución arquitectónica y de negocio:** La actualización de precios centralizados no impacta el POS hasta que la tienda física escanea y confirma el recambio de la etiqueta de góndola. El sistema retiene el precio anterior en caja, eliminando la discrepancia estructural, apoyado en un dashboard de desactualización para auditoría de cumplimiento..

**ID:** **SUP-10**. **El dolor operativo y comercial:** La compañía carece de trazabilidad para demostrar el precio publicado en una fecha u hora específica ante reclamos formales.. **La resolución arquitectónica y de negocio:** La arquitectura de datos implementa versionado de precios (Slowly Changing Dimensions). Se mantiene una réplica local ligera para operar offline y un repositorio centralizado inmutable (3 años de retención) que permite recuperar la fotografía exacta del precio por canal mediante consultas indexadas por timestamp..

<!-- origen: T7-03_Informes4_source.md | bloque 18 -->

#### El pedido: lógica de cobro, asignación y comisión

Tabla 3.3:** Resolución de decisiones de lógica de cobro, asignación de pedidos y comisiones.

**ID:** **SUP-11**. **El dolor operativo y comercial:** La cancelación de pedidos por quiebre de stock derivó en capturas financieras sobre mercadería inexistente, generando contingencias legales y operativas.. **La resolución arquitectónica y de negocio:** El checkout digital transiciona a un modelo de "Preautorización sin Captura". El cargo efectivo solo se liquida tras la confirmación de picking. Ante quiebres, un motor orquesta soluciones alternativas (re-enrutamiento, sustitución). Si se requiere cancelación, la preautorización se libera sin impacto financiero para el cliente..

**ID:** **SUP-13**. **El dolor operativo y comercial:** La asignación de fulfillment basada puramente en distancia geográfica vacía sistemáticamente las salas de venta de mayor rotación (17 %).. **La resolución arquitectónica y de negocio:** El orquestador de pedidos (OMS) sustituye la variable de proximidad por un algoritmo de "Costo Total de Servir", que pondera el costo logístico de última milla contra el costo de oportunidad comercial de extraer la unidad de una sala de alta conversión, respetando siempre el SLA de entrega del cliente..

<!-- origen: T7-03_Informes4_source.md | bloque 19 -->

#### Postventa, Marketplace y Logística Inversa

Tabla 3.4:** Resolución de decisiones de postventa, marketplace y logística inversa.

**ID:** **SUP-15**. **El dolor operativo y comercial:** La devolución física de mercadería de sellers externos queda inmovilizada en bodegas propias sin trazabilidad, generando fricción en las liquidaciones financieras.. **La resolución arquitectónica y de negocio:** Se implementa notificación transaccional en tiempo real. Al procesar la recepción física en la tienda, el sistema dispara un evento al portal del vendedor (Seller Center) con el estado, motivo y ubicación del activo, registrando la responsabilidad financiera del reingreso en el mismo acto..

**ID:** **SUP-16**. **El dolor operativo y comercial:** La ausencia de SLAs formales impide penalizar o excluir a los sellers externos que degradan la calidad del servicio de Ancoa.. **La resolución arquitectónica y de negocio:** Se activa un motor de gobernanza marketplace condicionado a la aceptación digital de políticas (T\&C). El sistema mide automáticamente cinco KPIs críticos (tasa de cancelación, puntualidad, devoluciones por falla, lead time de respuesta y calidad de catálogo). Los incumplimientos gatillan suspensiones sistémicas automáticas..

**ID:** **SUP-21**. **El dolor operativo y comercial:** El modelo actual de derivación de garantías (hacia fabricantes o externos) vulnera la normativa de protección al consumidor y genera alta fricción en mesón.. **La resolución arquitectónica y de negocio:** La arquitectura asume la resolución en "Primera Línea". Ancoa absorbe la prestación legal directamente frente al cliente en la sucursal. En segundo plano, un módulo de conciliación gestiona los recobros B2B contra el proveedor o seller, aislando al consumidor de la disputa financiera interna..

**ID:** **SUP-22**. **El dolor operativo y comercial:** El procesamiento de retractos a distancia carece de estandarización temporal y contamina el inventario disponible con unidades mermadas.. **La resolución arquitectónica y de negocio:** El plazo legal de retracto se abstrae como un parámetro gobernable. Toda devolución reingresa a un estado de "Cuarentena Lógica"; el WMS bloquea su disponibilidad comercial hasta que un usuario identificado registre la inspección física y certifique su aptitud de reventa..

<!-- origen: T7-03_Informes4_source.md | bloque 20 -->

#### El crédito: acreditación del consentimiento

Tabla 3.5:** Resolución de decisiones de acreditación de consentimiento y crédito.

**ID:** **SUP-05**. **El dolor operativo y comercial:** La dependencia de grabaciones telefónicas con purga a 90 días expone a la filial emisora a sanciones por incapacidad probatoria de repactaciones.. **La resolución arquitectónica y de negocio:** Sustitución completa hacia expedientes digitales estructurados. Se captura el contrato, metadatos de sesión (IP, canal, timestamp) y se sella criptográficamente. El archivo se rige por políticas WORM (inmutabilidad) en almacenamiento frío, asegurando retención legal (duración \+ 6 años) y recuperación demostrable..

**ID:** **SUP-06**. **El dolor operativo y comercial:** La obligación normativa de entregar información precontractual compite con los tiempos de atención; el personal comercial tiende a evadir procesos lentos.. **La resolución arquitectónica y de negocio:** El registro de entrega precontractual se embebe como requisito sistémico bloqueante en el flujo del POS/App, sin añadir clicks o firmas en papel. El sistema impide cursar la aceptación final si no existe el registro de timestamp previo que certifique el despliegue del simulador de condiciones..

<!-- origen: T7-03_Informes4_source.md | bloque 21 -->

#### Identidad, Accesos y Seguridad Transaccional

Tabla 3.6:** Resolución de decisiones de identidad, accesos y seguridad transaccional.

**ID:** **SUP-19**. **El dolor operativo y comercial:** Más de 1.100 repositores externos operan en sala e interactúan con sistemas sin relación laboral formal ni control de acceso directo.. **La resolución arquitectónica y de negocio:** Se delega la administración del ciclo de vida al proveedor B2B. A través del portal corporativo, el empleador externo aprovisiona y define la caducidad de las credenciales de su personal. El sistema aplica revocación por omisión: sin renovación explícita, el acceso expira automáticamente..

**ID:** **SUP-23**. **El dolor operativo y comercial:** El desbordamiento de tráfico durante eventos masivos (Cyber) deriva en caídas catastróficas al no existir protocolos de degradación predefinidos.. **La resolución arquitectónica y de negocio:** Se implementa un modelo de resiliencia escalonado. La primera línea (salas de espera, limitación de concurrencia) escala automáticamente por telemetría. La degradación crítica (apagón de pasarelas de crédito, bloqueo de categorías completas) requiere orquestación manual exclusiva por un rol facultado, protegiendo ingresos de impacto mayor..

**ID:** **SUP-24**. **El dolor operativo y comercial:** La alta rotación de personal (62 %) y las contrataciones de temporada dejan perfiles huérfanos con accesos críticos activos en cajas y carteras.. **La resolución arquitectónica y de negocio:** Erradicación de credenciales compartidas en el POS, sustituidas por traspasos rápidos de sesión (hot-swapping). Se implementa un conector bidireccional con el sistema de RRHH: los finiquitos contractuales disparan eventos asíncronos que revocan inmediatamente el acceso en todas las capas lógicas y físicas de la plataforma..

<!-- origen: T7-03_Informes4_source.md | bloque 24 -->

## Alcance de la Etapa 1 y de la Etapa 2, con criterio de asignación

El cronograma contractual de 56 meses se asume como indivisible e inalterable: la Etapa 1 contempla desarrollo entre los meses 1 y 12, marcha blanca entre el 13 y el 15, y paso a producción en el mes 16; la Etapa 2 comprende desarrollo entre los meses 13 y 18, marcha blanca entre el 19 y el 20, y producción en el mes 21; finalmente, la fase de Operación abarca los meses 21 a 56\. La definición de alcance no consiste en redistribuir estos plazos, sino en determinar qué capacidades arquitectónicas se construyen y liberan en cada ventana.

La preferencia de urgencia manifestada por el Comité Directivo (inventario y disponibilidad como prioridad, seguido de precio, y finalmente el negocio financiero, marketplace y analítica) se adopta como directriz base. Sin embargo, se aplica una corrección estructural en su tramo final para mitigar el riesgo sistémico de la migración financiera y garantizar el cumplimiento normativo, conforme a los siguientes criterios de asignación.

<!-- origen: T7-03_Informes4_source.md | bloque 25 -->

### Criterios de asignación

Se establecen seis criterios excluyentes, en estricto orden de precedencia, para la asignación de módulos. Ninguna carga de trabajo se distribuye por afinidad temática o comodidad del equipo:

1. **Dependencia técnica dura:** Las capacidades habilitantes anteceden obligatoriamente a las dependientes. La frontera de datos precede a cualquier vista unificada de cliente; el motor de disponibilidad precede a la promesa de entrega y publicación digital; el bus de eventos precede a la estrangulación del núcleo de 2009\.

2. **Irreversibilidad arquitectónica:** Los componentes cuya separación a posteriori es inviable se ejecutan primero. Específicamente, la segregación lógica y física entre el dominio retail y el negocio financiero fiscalizado.

3. **Hitos regulatorios externos:** Cumplimiento ineludible de la fecha límite inamovible (2029) impuesta por el plan de remediación de la autoridad financiera y el fin de soporte de la plataforma de originación de 2011\.

4. **Exposición legal vigente:** Priorización de los componentes vinculados a pasivos normativos en curso, como el procedimiento derivado de las 2.840 cancelaciones y la fiscalización de precios de febrero de 2026\.

5. **Capacidad de absorción operacional:** La asignación de trabajo concurrente se dimensiona sobre la capacidad real del área de TI del CLIENTE (46 profesionales para sostener 9 plataformas, 22 sucursales y 2 centros de distribución), evitando el colapso operativo en hitos paralelos.

6. **Ventanas de congelamiento de TI:** Adaptación de los despliegues a los cinco períodos de bloqueo anuales, concentrando las intervenciones mayores exclusivamente en las únicas dos ventanas viables: marzo abril y julio octubre.

<!-- origen: T7-03_Informes4_source.md | bloque 26 -->

### La corrección al orden de urgencia declarado

El análisis de riesgo valida la imposibilidad de migrar una cartera viva de 620.000 clientes con saldo durante la limitada ventana de seis meses de desarrollo asignada a la Etapa 2\.

La estrategia de mitigación no altera la fecha del corte final de la cartera (que se mantiene en la Etapa 2 para respetar el orden comercial), sino que escinde la habilitación técnica de la ejecución operativa. Se establece el despliegue temprano en la Etapa 1 de los componentes habilitantes críticos: el gobierno de la frontera de datos, la captura estructurada de consentimientos, el archivo inmutable de largo plazo, el saneamiento de los 620.000 registros y el motor de conciliación. De este modo, la Etapa 2 recibe un ecosistema pre-validado contra la plataforma de 2011, no un diseño desde cero.

Respecto a la analítica predictiva y los modelos de aprendizaje automático (Machine Learning), su despliegue se introduce de manera controlada y acotada a través de la Cartera de Innovaciones. Estos modelos operarán estrictamente sobre datos anonimizados, condicionando su activación a la auditoría técnica que certifique que la frontera de datos entre el retail y el negocio financiero es infranqueable, asegurando cero vulneraciones normativas.

<!-- origen: T7-03_Informes4_source.md | bloque 27 -->

### Colisiones de calendario declaradas

Asumiendo la adjudicación en diciembre de 2026 y la formalización contractual, el Mes 1 inicia efectivamente en enero de 2027\. Esto sitúa las salidas a producción en abril de 2028 (Etapa 1\) y septiembre de 2028 (Etapa 2), esquivando exitosamente los bloqueos anuales. Las colisiones residuales se abordan mediante planes de mitigación técnicos:

Tabla 3.15:** Estrategias de tratamiento para colisiones de calendario declaradas.

**Momento:** **Meses 11–12**. **Colisión Operativa / Normativa:** El cierre de desarrollo (Etapa 1\) choca con el congelamiento de Navidad y el pico de 1.900 altas de temporada.. **Estrategia de Tratamiento:** Congelamiento absoluto de despliegues productivos. Las pruebas integrales y de estrés se ejecutan en Preproducción asimilando el volumen real del *peak*..

**Momento:** **Mes 13**. **Colisión Operativa / Normativa:** El inicio de la marcha blanca coincide con la última semana del congelamiento de fin de año (hasta el 6 de enero).. **Estrategia de Tratamiento:** Inicio efectivo de la marcha blanca diferido al 7 de enero. La desviación técnica (6 días) se absorbe con la reserva de contingencia sin desplazar el hito de Producción..

**Momento:** **Meses 13–15**. **Colisión Operativa / Normativa:** La marcha blanca convive con el congelamiento "Vuelta a Clases".. **Estrategia de Tratamiento:** Aprovechamiento del alto volumen transaccional para telemetría. La estabilización y corrección de código se concentra en marzo, previo a la certificación final..

**Momento:** **Meses 13–15**. **Colisión Operativa / Normativa:** Solapamiento contractual de Marcha Blanca (Etapa 1\) y Desarrollo (Etapa 2).. **Estrategia de Tratamiento:** Segregación física de frentes de trabajo y dotación, evidenciada y garantizada en la matriz de Nivelación de Recursos del cronograma..

**Momento:** **Mes 17 o 18**. **Colisión Operativa / Normativa:** El *Cyber* de 2028 (fecha móvil dictada por terceros) irrumpe con la Etapa 1 en producción y la Etapa 2 en desarrollo.. **Estrategia de Tratamiento:** Congelamiento del código (6 semanas de preaviso). Validación previa del motor ATP sobre un subconjunto de alto riesgo y activación de protocolos de degradación preventiva..

<!-- origen: T7-03_Informes4_source.md | bloque 28 -->

### Fase de Operación

Se despliegan 36 meses continuos de operación y soporte de misión crítica (meses 21 a 56). La estrategia operativa incorpora soporte 24x7x365 para el canal digital y los componentes financieros, y atención en horario comercial extendido (09:00 a 23:00) para las sucursales y operaciones físicas. Se contempla cobertura reforzada documentada para los tres eventos anuales masivos y soporte especializado presencial distribuido en las 11 regiones de operación.

<!-- origen: T7-03_Informes4_source.md | bloque 29 -->

## Exclusiones explícitas, supuestos y restricciones

<!-- origen: T7-03_Informes4_source.md | bloque 30 -->

### Exclusiones explícitas

Los siguientes componentes quedan excluidos del alcance de implementación. La arquitectura se diseña asumiendo la convivencia y la orquestación con estos elementos:

Tabla 3.16:** Exclusiones explícitas del alcance y diseño compensatorio.

**N°:** **X-01**. **Exclusión:** Reemplazo del ERP central y emisión de documentos tributarios.. **Diseño Compensatorio y Convivencia Arquitectónica:** El ERP permanece como emisor único de DTEs. La solución actúa como enrutador y provee conciliación y foliado local para contingencias offline..

**N°:** **X-02**. **Exclusión:** Adquisición física de etiquetas electrónicas para góndola.. **Diseño Compensatorio y Convivencia Arquitectónica:** Se especifica la tecnología y su costo; el diseño asume la retención del precio anterior en el POS hasta el escaneo físico manual como mitigación base..

**N°:** **X-03**. **Exclusión:** Adquisición de dispositivos móviles para vendedores de sala.. **Diseño Compensatorio y Convivencia Arquitectónica:** La arquitectura asume la restricción de infraestructura existente (640 terminales para 3.820 personas) y resuelve la fricción mediante traspasos nominativos rápidos de sesión..

**N°:** **X-04**. **Exclusión:** Desarrollo del portal interno de vendedores de Marketplace y su logística.. **Diseño Compensatorio y Convivencia Arquitectónica:** La integración se limita al onboarding, sincronización de stock, monitoreo de SLAs (5 KPIs) y notificación de devoluciones físicas..

**N°:** **X-05**. **Exclusión:** Motor de cálculo contable y liquidación de remuneraciones.. **Diseño Compensatorio y Convivencia Arquitectónica:** Se procesa y exporta la base bruta de cálculo para atribuir comisiones cruzadas (ej. despacho desde tienda), pero el pago lo ejecuta el sistema del CLIENTE..

**N°:** **X-06**. **Exclusión:** Sistema de cobranza judicial y ejecución de embargos.. **Diseño Compensatorio y Convivencia Arquitectónica:** El perímetro abarca exclusivamente el registro inmutable y la trazabilidad de las gestiones extrajudiciales y repactaciones..

**N°:** **X-07**. **Exclusión:** Flotas y sustitución de proveedores de última milla.. **Diseño Compensatorio y Convivencia Arquitectónica:** Integración API para trazabilidad del ciclo de vida del despacho, excluyendo la ruteo interno de los camiones de terceros..

**N°:** **X-08**. **Exclusión:** Obras civiles, canalización eléctrica y cableado estructurado.. **Diseño Compensatorio y Convivencia Arquitectónica:** El diseño entrega la planimetría y el cálculo de potencia/refrigeración; la ejecución es responsabilidad exclusiva del CLIENTE..

**N°:** **X-09**. **Exclusión:** Adquisición de hardware (POS, red, infraestructura de edge).. **Diseño Compensatorio y Convivencia Arquitectónica:** Dimensionamiento y especificación técnica exhaustiva suministrada en la Oferta Técnica para la compra directa por el CLIENTE..

**N°:** **X-10**. **Exclusión:** Contratos de telecomunicaciones de centros comerciales.. **Diseño Compensatorio y Convivencia Arquitectónica:** La arquitectura Edge (servidores locales) absorbe las caídas de red de terceros garantizando la autonomía comercial..

**N°:** **X-11**. **Exclusión:** Implementación del WMS en el centro de distribución de Concepción.. **Diseño Compensatorio y Convivencia Arquitectónica:** La infraestructura logística se excluye como punto de promesa digital hasta que abandone el control manual basado en planillas..

**N°:** **X-12**. **Exclusión:** Saneamiento retroactivo de la base histórica del inventario físico.. **Diseño Compensatorio y Convivencia Arquitectónica:** La arquitectura gestiona el margen de error conocido (12,4%) para calcular el disponible; no se ejecutarán conteos ciegos correctivos masivos fuera del modelo cíclico ABC..

<!-- origen: T7-03_Informes4_source.md | bloque 31 -->

### Supuestos

Los parámetros de dimensionamiento y capacidad que condicionan la planificación se formulan como supuestos gobernables, sujetos a re-validación en la fase de levantamiento:

Tabla 3.17:** Supuestos estructurales, impacto y mecanismo de validación.

**ID:** **S-A**. **Supuesto estructural:** El mes 1 del contrato corresponde a enero de 2027\.. **Impacto operacional:** Desplazamientos que expongan los hitos de producción al congelamiento de Navidad forzarían la reprogramación total del proyecto.. **Mecanismo de validación:** Aprobación del Acta de Inicio en Mes 1\..

**ID:** **S-B**. **Supuesto estructural:** El evento Cyber de 2028 se fija entre mayo y junio, notificado con 6 semanas de anticipación. **Impacto operacional:** Un adelanto anómalo reduce la ventana de estabilización post-paso a producción (Etapa 1\). **Mecanismo de validación:** Anuncio oficial de la Cámara de Comercio..

**ID:** **S-C**. **Supuesto estructural:** El core de originación (2011) soporta exposición de cupos preaprobados vía API hacia el nodo local de contingencia.. **Impacto operacional:** Inviabilidad técnica inhabilitaría el consumo crediticio offline en tiendas (38% de la venta) durante la Etapa 1\.. **Mecanismo de validación:** Prueba de concepto técnica (POC)..

**ID:** **S-D**. **Supuesto estructural:** El corte de inventario para la migración se resuelve por estrategia declarada y no por conteo físico total simultáneo en las 24 instalaciones.. **Impacto operacional:** Un recuento físico global simultáneo en las 24 instalaciones generaría sobrecostos laborales y de horas extra no presupuestados.. **Mecanismo de validación:** Aprobación del Plan de Migración..

**ID:** **S-E**. **Supuesto sujeto a validación:** Se evaluará si el sistema central admite una fachada de API sin modificar su código y qué interfaces pueden observarse o sustituirse individualmente; estas capacidades no se presuponen para el conjunto de plataformas. **Impacto operacional:** Las escrituras directas en bases de datos u otros flujos no observables podrían eludir la integración acordada y exigir mecanismos de captura o conciliación adicionales. **Mecanismo de validación:** Levantamiento técnico y prueba piloto de un flujo de carga de precios antes de seleccionar y escalar el patrón de transición.

<!-- origen: T7-03_Informes4_source.md | bloque 32 -->

### Restricciones

Restricciones de Continuidad y Operación Física (Edge Computing):

* Continuidad operacional offline estricta en infraestructura on-premise por 24 horas continuas para garantizar la venta, cobro y contingencia crediticia exigida durante 8 horas en tiendas. Para el CD Concepción, la exigencia de autonomía se fija en 4 horas.

* Restablecimiento de red y sincronización bidireccional forzosa en un máximo de 30 minutos sin pérdida de DTEs ni solapamiento de stock.

* Tolerancia nula a la indisponibilidad de terminales por rotación; la sesión cajero-vendedor emplea rotación de credenciales (hot-swapping).

* Cinco ventanas de congelamiento de infraestructura inamovibles, implementadas como barreras automatizadas de CI/CD para bloquear despliegues durante peaks comerciales.

Restricciones Legales y Normativas (Zero Trust y Protección de Datos):

* Arquitectura de segregación lógica y auditoría inmutable estricta que garantice la incomunicación por defecto entre la filial de crédito y el retail comercial.

* Inmutabilidad probatoria de largo plazo: los registros precontractuales, el timestamp de entrega de información y el consentimiento de repactación se archivan en almacenamiento frío por el plazo de vigencia de la deuda más 6 años.

* Derivación de garantías prohibida por diseño. El flujo comercial de postventa absorbe financieramente las contingencias en primera línea, delegando la liquidación B2B al plano administrativo trasero.

Restricciones Contractuales del Proceso de Licitación:

* Plazo contractual de 56 meses y adopción obligatoria del despliegue en nube híbrida.

* Integración auditable de cinco modelos de innovación valorizados económicamente, incluyendo algoritmos de aprendizaje automático controlados perimetralmente para no comprometer datos sensibles.

* Censura absoluta de información tarifaria, precios unitarios y cálculos financieros en el cuerpo de la Oferta Técnica (Sobre N°2).

<!-- origen: T7-03_Informes4_source.md | bloque 33 -->

## Catálogo de requerimientos funcionales core

El Anexo Técnico X consolida 223 requerimientos funcionales atomizados. Esta sección expone estrictamente el subconjunto core: aquellos requerimientos cuya omisión vulnera las restricciones innegociables del CLIENTE o bloquea la habilitación de dependencias arquitectónicas estructurales.

* Criterio de selección: Un requerimiento integra el núcleo core si (1) implementa de forma directa una de las quince restricciones no negociables, (2) materializa una decisión estructural de arquitectura, o (3) constituye un prerrequisito técnico bloqueante para el resto de su módulo.

* Prioridad: Se aplica el marco MoSCoW. La totalidad del catálogo core está clasificado como M (Obligatorio/Must), condicionando el éxito de los pasos a producción.

<!-- origen: T7-03_Informes4_source.md | bloque 34 -->

### Gobernanza de datos y frontera regulatoria

Tabla 3.18:** Requerimientos funcionales core de gobernanza de datos y frontera regulatoria.

**ID:** RF-166. **Requerimiento:** Bloquear todo intento de cruce de información que no corresponda a una interfaz declarada en el inventario de flujos autorizados.. **Módulo:** M-21. **Etapa:** 1. **Trazabilidad:** Restricción N°1  SUP-04  OE-11.

**ID:** RF-165. **Requerimiento:** Registrar cada cruce ejecutado entre ámbitos indicando dato, finalidad, base de licitud, autorización nominada e instante.. **Módulo:** M-21. **Etapa:** 1. **Trazabilidad:** SUP-04  OE-11.

**ID:** RF-170. **Requerimiento:** Excluir del catálogo de atributos disponibles en el motor de campañas todo atributo de origen financiero.. **Módulo:** M-21. **Etapa:** 1. **Trazabilidad:** Restricción N°1  SUP-04.

**ID:** RF-174. **Requerimiento:** Resolver la correspondencia entre identificadores exclusivamente a través de la tabla custodiada en zona neutral, con acceso nominado y registrado.. **Módulo:** M-22. **Etapa:** 1. **Trazabilidad:** SUP-03.

<!-- origen: T7-03_Informes4_source.md | bloque 35 -->

### Disponibilidad e inventario

Tabla 3.19:** Requerimientos funcionales core de disponibilidad e inventario.

**ID:** RF-127. **Requerimiento:** Calcular la existencia disponible para vender restando de la existencia registrada las reservas vigentes, el comprometido no despachado y el colchón de confianza.. **Módulo:** M-01. **Etapa:** 1. **Trazabilidad:** SUP-01  OE-02.

**ID:** RF-128. **Requerimiento:** Determinar el valor del colchón de confianza en función de la categoría del artículo.. **Módulo:** M-01. **Etapa:** 1. **Trazabilidad:** SUP-01  OE-02.

**ID:** RF-157. **Requerimiento:** Impedir que cualquier canal de venta consuma el saldo bruto de inventario para publicar o comprometer existencia.. **Módulo:** M-01. **Etapa:** 1. **Trazabilidad:** SUP-01.

**ID:** RF-161. **Requerimiento:** Mostrar al vendedor de piso el porcentaje de error probable junto a la disponibilidad publicada.. **Módulo:** M-01. **Etapa:** 1. **Trazabilidad:** SUP-01.

**ID:** RF-137. **Requerimiento:** Calcular la exactitud de inventario resultante por categoría.. **Módulo:** M-02. **Etapa:** 1. **Trazabilidad:** SUP-18  OE-01.

**ID:** RF-139. **Requerimiento:** Impedir el cierre de un ajuste de inventario que no tenga asignado un componente de merma.. **Módulo:** M-02. **Etapa:** 1. **Trazabilidad:** SUP-17  OE-03.

**ID:** RF-143. **Requerimiento:** Impedir la publicación de una referencia en el canal digital mientras no cuente con los atributos obligatorios completos.. **Módulo:** M-03. **Etapa:** 1. **Trazabilidad:** Vacío V-03.

<!-- origen: T7-03_Informes4_source.md | bloque 36 -->

### Precio y evidencia fiscal

Tabla 3.20:** Requerimientos funcionales core de precio y evidencia fiscal.

**ID:** RF-028. **Requerimiento:** Impedir la venta de la referencia al precio nuevo mientras su punto de exhibición no confirme la actualización física.. **Módulo:** M-06. **Etapa:** 1. **Trazabilidad:** Restricción N°4  SUP-09  OE-04.

**ID:** RF-023. **Requerimiento:** Cobrar el menor de ambos precios para el consumidor ante discrepancia detectada en línea de caja.. **Módulo:** M-06. **Etapa:** 1. **Trazabilidad:** Restricción N°4  SUP-08.

**ID:** RF-020. **Requerimiento:** Registrar la identidad individual del ejecutor del cambio de etiqueta.. **Módulo:** M-06. **Etapa:** 1. **Trazabilidad:** SUP-09.

**ID:** RF-021. **Requerimiento:** Recuperar el precio publicado de una referencia para una fecha, hora y canal determinados.. **Módulo:** M-07. **Etapa:** 1. **Trazabilidad:** Restricción N°4  SUP-10  OE-05.

<!-- origen: T7-03_Informes4_source.md | bloque 37 -->

### Pedido, cumplimiento y comisión

Tabla 3.21:** Requerimientos funcionales core de pedido, cumplimiento y comisión.

**ID:** RF-043. **Requerimiento:** Preautorizar el medio de pago al aceptar el pedido, sin capturar el cobro.. **Módulo:** M-09. **Etapa:** 1. **Trazabilidad:** SUP-11  OE-07.

**ID:** RF-045. **Requerimiento:** Capturar el cobro únicamente al registrarse el evento de confirmación de la preparación física.. **Módulo:** M-09. **Etapa:** 1. **Trazabilidad:** SUP-11  OE-07.

**ID:** RF-046. **Requerimiento:** Determinar automáticamente la alternativa de resolución aplicable según el motor de reglas ante quiebres de inventario.. **Módulo:** M-09. **Etapa:** 1. **Trazabilidad:** SUP-11.

**ID:** RF-051. **Requerimiento:** Notificar al cliente el cambio de estado de su pedido antes de efectuar cualquier cobro definitivo.. **Módulo:** M-11. **Etapa:** 1. **Trazabilidad:** SUP-11  OE-07.

**ID:** RF-052. **Requerimiento:** Permitir a todos los actores consultar el estado del pedido desde una única fuente de verdad.. **Módulo:** M-09. **Etapa:** 1. **Trazabilidad:** SUP-11.

**ID:** RF-077. **Requerimiento:** Seleccionar como punto de despacho aquel de menor costo total de servir.. **Módulo:** M-09. **Etapa:** 1. **Trazabilidad:** SUP-13  OE-06.

**ID:** RF-055. **Requerimiento:** Condicionar la transmisión de la base de comisión al movimiento real de inventario verificado en bodega.. **Módulo:** M-10. **Etapa:** 1. **Trazabilidad:** SUP-14.

<!-- origen: T7-03_Informes4_source.md | bloque 38 -->

### Operación de tienda y contingencia

Tabla 3.22:** Requerimientos funcionales core de operación de tienda y contingencia.

**ID:** RF-084. **Requerimiento:** Permitir al cajero cobrar la venta en modo desconectado.. **Módulo:** M-08. **Etapa:** 1. **Trazabilidad:** Restricción N°5  OE-12.

**ID:** RF-086. **Requerimiento:** Emitir el documento de venta en contingencia utilizando folios previamente asignados por el ERP.. **Módulo:** M-08. **Etapa:** 1. **Trazabilidad:** Restricciones N°5 y N°6  Vacío V-01.

**ID:** RF-100. **Requerimiento:** Enrutar la emisión de todo documento tributario hacia el sistema de gestión empresarial como único emisor.. **Módulo:** M-08. **Etapa:** 1. **Trazabilidad:** Restricción N°6  X-01.

**ID:** RF-089. **Requerimiento:** Permitir el otorgamiento de crédito en modo desconectado exclusivamente contra cupo preaprobado vigente.. **Módulo:** M-17. **Etapa:** 1 y 2. **Trazabilidad:** SUP-07  Supuesto S-C.

**ID:** RF-092. **Requerimiento:** Impedir la apertura de una tarjeta nueva en modo desconectado.. **Módulo:** M-17. **Etapa:** 2. **Trazabilidad:** SUP-07  Restricción N°3.

**ID:** RF-095. **Requerimiento:** Reconciliar hacia los sistemas centrales la totalidad de las ventas registradas en modo desconectado.. **Módulo:** M-08. **Etapa:** 1. **Trazabilidad:** OE-12.

**ID:** RF-097. **Requerimiento:** Procesar la reconciliación de forma idempotente, impidiendo la duplicación de ventas o documentos.. **Módulo:** M-08. **Etapa:** 1. **Trazabilidad:** OE-12.

<!-- origen: T7-03_Informes4_source.md | bloque 39 -->

### Post-venta, garantía legal y marketplace

Tabla 3.23:** Requerimientos funcionales core de postventa, garantía legal y marketplace.

**ID:** RF-188. **Requerimiento:** Impedir que el flujo de atención exija la derivación del consumidor al fabricante, al servicio técnico o al vendedor externo.. **Módulo:** M-13. **Etapa:** 1. **Trazabilidad:** Restricción N°7  SUP-21.

**ID:** RF-198. **Requerimiento:** Impedir que el estado de la recuperación contra el tercero condicione el cierre de la resolución al consumidor.. **Módulo:** M-14. **Etapa:** 1. **Trazabilidad:** SUP-21.

**ID:** RF-190. **Requerimiento:** Impedir el reingreso de una unidad devuelta al inventario disponible mientras no exista decisión de aptitud registrada.. **Módulo:** M-13. **Etapa:** 1. **Trazabilidad:** SUP-22.

**ID:** RF-106. **Requerimiento:** Notificar al vendedor de marketplace la recepción de la devolución en el instante en que se registra.. **Módulo:** M-14. **Etapa:** 2. **Trazabilidad:** SUP-15.

**ID:** RF-119. **Requerimiento:** Registrar el acuse de conocimiento de las reglas de evaluación por parte de cada vendedor externo.. **Módulo:** M-12. **Etapa:** 2. **Trazabilidad:** SUP-16.

**ID:** RF-124. **Requerimiento:** Despublicar automáticamente la oferta cuyo stock declarado haya superado el plazo de vigencia sin actualización.. **Módulo:** M-12. **Etapa:** 2. **Trazabilidad:** SUP-16.

<!-- origen: T7-03_Informes4_source.md | bloque 40 -->

### Crédito, consentimiento y migración

Tabla 3.24:** Requerimientos funcionales core de crédito, consentimiento y migración.

**ID:** RF-199. **Requerimiento:** Exigir la entrega completa de la información precontractual antes de habilitar la evaluación de la solicitud.. **Módulo:** M-15. **Etapa:** 2. **Trazabilidad:** Restricción N°3  SUP-06  OE-08.

**ID:** RF-206. **Requerimiento:** Impedir el registro de la aceptación del crédito mientras no exista acreditación de entrega previa de la información precontractual.. **Módulo:** M-16. **Etapa:** 2. **Trazabilidad:** Restricción N°3  SUP-06  OE-08.

**ID:** RF-208. **Requerimiento:** Impedir el registro de una modificación de condiciones del crédito que no posea evidencia de consentimiento asociada.. **Módulo:** M-16. **Etapa:** 2. **Trazabilidad:** Restricción N°2  SUP-05  OE-08.

**ID:** RF-210. **Requerimiento:** Restaurar desde archivo frío los antecedentes de una operación de crédito de cualquier cohorte dentro del plazo de retención.. **Módulo:** M-16. **Etapa:** 2. **Trazabilidad:** SUP-05  OE-08.

**ID:** RF-220. **Requerimiento:** Impedir la originación de una operación cuya tasa supere la Tasa Máxima Convencional vigente.. **Módulo:** M-15. **Etapa:** 2. **Trazabilidad:** SUP-06.

**ID:** RF-213. **Requerimiento:** Impedir la ejecución de una gestión de cobranza fuera de los límites normativos de horario y de medio.. **Módulo:** M-18. **Etapa:** 2. **Trazabilidad:** SUP-05.

**ID:** RF-216. **Requerimiento:** Generar el reporte de conciliación diaria de saldos durante todo el proceso de migración por olas de coexistencia.. **Módulo:** M-19. **Etapa:** 1 y 2. **Trazabilidad:** Restricción N°8  SUP-25  OE-10.

<!-- origen: T7-03_Informes4_source.md | bloque 41 -->

### Accesos, evento anual y ventanas de congelamiento

Tabla 3.25:** Requerimientos funcionales core de accesos, eventos anuales y congelamiento.

**ID:** RF-004. **Requerimiento:** Impedir el acceso mediante credencial compartida en líneas de caja o terminales de piso.. **Módulo:** M-23. **Etapa:** 1. **Trazabilidad:** Restricción N°11  SUP-24.

**ID:** RF-013. **Requerimiento:** Revocar la totalidad de los accesos y credenciales del trabajador a partir del término efectivo de su vínculo.. **Módulo:** M-23. **Etapa:** 1. **Trazabilidad:** SUP-24.

**ID:** RF-007. **Requerimiento:** Impedir la ejecución de la función de originación a un usuario sin capacitación normativa acreditada vigente.. **Módulo:** M-23. **Etapa:** 2. **Trazabilidad:** SUP-24.

**ID:** RF-163. **Requerimiento:** Permitir exclusivamente al rol facultado suspender manualmente la publicación comercial de una categoría.. **Módulo:** M-24. **Etapa:** 1. **Trazabilidad:** SUP-23.

**ID:** RF-185. **Requerimiento:** Bloquear por diseño la ejecución de despliegues en producción durante las ventanas de congelamiento.. **Módulo:** M-24. **Etapa:** 1. **Trazabilidad:** Restricción N°9.

<!-- origen: T7-03_Informes4_source.md | bloque 42 -->

## Catálogo de requerimientos no funcionales core

El Anexo consolida 75 requerimientos no funcionales (RNF) asociados a desempeño, resiliencia y seguridad. Esta sección expone exclusivamente aquellos **con valor numérico verificable**, los cuales gobiernan la certificación y paso a producción de cada etapa. Los valores rotulados como supuesto serán recalibrados empíricamente durante el levantamiento inicial.

<!-- origen: T7-03_Informes4_source.md | bloque 43 -->

### Desempeño y tiempo de respuesta

Tabla 3.26:** Requerimientos no funcionales core de desempeño y tiempo de respuesta.

**ID:** RNF-16. **Requerimiento:** Consulta de disponibilidad en la ficha de producto del canal digital.. **Umbral:** ≤ 400 ms. **Método de verificación:** Prueba de carga con perfil del evento anual y monitoreo en producción..

**ID:** RNF-21. **Requerimiento:** Consulta de disponibilidad desde terminal compartida del piso de venta.. **Umbral:** ≤ 2 s. **Método de verificación:** Prueba en terreno sobre las 640 terminales, en tienda insignia y de calle..

**ID:** RNF-17. **Requerimiento:** Confirmación de un pedido durante el evento anual.. **Umbral:** ≤ 3 s. **Método de verificación:** Prueba de carga con el peak declarado..

**ID:** RNF-18. **Requerimiento:** Venta completa en caja con medio de pago externo.. **Umbral:** ≤ 25 s. **Método de verificación:** Medición instrumentada en peak de diciembre..

**ID:** RNF-06. **Requerimiento:** Evaluación de una solicitud de crédito en el punto de venta físico.. **Umbral:** ≤ 8 s (base actual: 40s a 3m). **Método de verificación:** Medición extremo a extremo en mesón y caja..

**ID:** RNF-19. **Requerimiento:** Propagación de un cambio de precio a las 380 líneas de caja y al canal digital.. **Umbral:** ≤ 5 min. **Método de verificación:** Prueba con carga de campaña de 400.000 cambios en un día..

**ID:** RNF-20. **Requerimiento:** Registro de una devolución en el mesón de atención.. **Umbral:** ≤ 60 s. **Método de verificación:** Medición instrumentada con muestreo por tienda..

**ID:** RNF-05. **Requerimiento:** Desfase entre el cambio real de estado de un pedido y su reflejo omnicanal.. **Umbral:** Umbral declarado (\<= 30 s). **Método de verificación:** Auditoría cruzada de estado entre los cuatro canales..

<!-- origen: T7-03_Informes4_source.md | bloque 44 -->

### Capacidad

Tabla 3.27:** Requerimientos no funcionales core de capacidad operativa.

**ID:** RNF-22. **Requerimiento:** Soporte del peak digital del evento anual sin degradar los umbrales de desempeño.. **Umbral:** 104.000 pedidos en 3 días (proyección 150.000). **Método de verificación:** Prueba de carga al 120 % del peak proyectado..

**ID:** RNF-23. **Requerimiento:** Soporte del peak presencial de la campaña de noviembre y diciembre.. **Umbral:** Carga concurrente sobre 380 líneas de caja. **Método de verificación:** Prueba de carga presencial sostenida..

<!-- origen: T7-03_Informes4_source.md | bloque 45 -->

### Seguridad y frontera de datos

Tabla 3.28:** Requerimientos no funcionales core de seguridad, resiliencia y disponibilidad.

**ID:** RNF-28. **Requerimiento:** Operación desconectada autónoma del componente on-premise.. **Umbral:** ≥ 24 h continuas. **Método de verificación:** Prueba de desconexión prolongada del nodo físico..

**ID:** RNF-24. **Requerimiento:** Operación comercial de tienda sin enlace externo (venta y cobro efectivos).. **Umbral:** ≥ 8 h continuas. **Método de verificación:** Corte real del enlace en tienda piloto, en horario comercial..

**ID:** RNF-25. **Requerimiento:** Operación del centro de distribución principal sin enlace externo.. **Umbral:** ≥ 4 h continuas. **Método de verificación:** Prueba de desconexión programada..

**ID:** RNF-26. **Requerimiento:** Sincronización tras la reconexión de sucursal.. **Umbral:** ≤ 30 min (tras 8 h de desconexión). **Método de verificación:** Prueba de reconexión cronometrada..

**ID:** RNF-27. **Requerimiento:** Integridad de la sincronización.. **Umbral:** 0 ventas y 0 DTE perdidos/duplicados. **Método de verificación:** Cuadratura del universo transaccional tras la contingencia..

**ID:** RNF-32. **Requerimiento:** Objetivos de recuperación ante desastre.. **Umbral:** RTO ≤ 4 h  RPO ≤ 15 min. **Método de verificación:** Ejercicio semestral de conmutación real..

**ID:** RNF-30. **Requerimiento:** Disponibilidad del canal digital.. **Umbral:** 24x7x365 (≥ 99,9 %). **Método de verificación:** Monitoreo mensual contra el SLA contractual..

**ID:** RNF-31. **Requerimiento:** Disponibilidad de servicios financieros (pagos, estados de cuenta, bloqueos).. **Umbral:** 24x7x365 (≥ 99,9 %). **Método de verificación:** Monitoreo segregado reportado a la filial emisora..

<!-- origen: T7-03_Informes4_source.md | bloque 46 -->

### Retención, trazabilidad y migración

Tabla 3.29:** Requerimientos no funcionales core de retención, trazabilidad y migración.

**ID:** RNF-42. **Requerimiento:** Conservación de los antecedentes e historial del crédito.. **Umbral:** Plazo del crédito \+ 6 años. **Método de verificación:** Pruebas de recuperación de archivo frío..

**ID:** RNF-57. **Requerimiento:** Recuperación de la evidencia de consentimiento de operaciones históricas.. **Umbral:** ≤ 5 min. **Método de verificación:** Recuperación por muestreo censal auditado..

**ID:** RNF-44. **Requerimiento:** Retención de la trazabilidad del precio publicado por canal.. **Umbral:** 3 años. **Método de verificación:** Auditoría de política de ciclo de vida de datos..

**ID:** RNF-58. **Requerimiento:** Recuperación del precio publicado en fecha, hora y canal arbitrarios.. **Umbral:** ≤ 1 min (sobre ventana de 3 años). **Método de verificación:** Consultas índice sobre el histórico inmutable..

**ID:** RNF-10. **Requerimiento:** Divergencia de saldos durante migración de cartera financiera.. **Umbral:** 0 divergencias no conciliadas. **Método de verificación:** Freno automático (circuit breaker) ante excepciones..

<!-- origen: T7-03_Informes4_source.md | bloque 47 -->

### Precisión sobre Continuidad y Métricas de Negocio

El diseño arquitectónico distingue estrictamente la continuidad de infraestructura de la continuidad comercial. El RNF-28 exige 24 horas de autonomía ininterrumpida para el nodo físico *on-premise*, protegiendo el almacenamiento local. Sobre esa infraestructura se despliega el RNF-24, que delimita la ventana de 8 horas exigida para sostener operativamente la venta, el cobro y la contingencia de crédito en la sala de la sucursal.

Asimismo, las metas de exactitud de inventario o tasa de cancelación no se tabulan como requerimientos no funcionales aislados, ya que su éxito depende de la conjunción entre el software entregado y la ejecución operativa del CLIENTE (conteo físico en sala, clasificación de mermas). Su cumplimiento se gestiona mediante los Criterios de Aceptación y Objetivos de Negocio del proyecto global.

<!-- origen: T7-03_Informes4_source.md | bloque 49 -->

## Criterios de aceptación del alcance comprometido

La aceptación no se declara por la entrega de un artefacto sino por la verificación de un hecho observable. Un entregable producido, documentado y presentado en plazo no se da por recibido si el comportamiento que debía habilitar no se demuestra con evidencia objetiva.

El modelo opera en tres niveles encadenados y no sustituibles entre sí: aceptación por entregable, que verifica conformidad técnica; aceptación por marcha blanca, que verifica comportamiento en operación real; y aceptación por resultado de negocio, que verifica que la plataforma efectivamente movió los indicadores que motivaron la licitación. Superar el primer nivel no anticipa el segundo, y superar los dos primeros no exime del tercero.

<!-- origen: T7-03_Informes4_source.md | bloque 50 -->

### Nivel 1: aceptación por entregable

Cada entregable se somete a revisión formal de la Contraparte Técnica y se acepta mediante acta suscrita, previa concurrencia de cuatro condiciones: el artefacto conforme a lo especificado; la evidencia objetiva de su verificación, no la declaración de haberla ejecutado; la trazabilidad explícita hacia los requerimientos del catálogo que satisface, incluyendo el módulo y la etapa a que pertenece; y el cierre documentado de las observaciones formuladas en revisiones previas.

La aceptación de un entregable que dependa de otro no procede mientras el precedente permanezca observado. Esta regla es la que impide que la cadena de dependencias declarada en el numeral 3.6.1 se rompa por conveniencia de calendario.

<!-- origen: T7-03_Informes4_source.md | bloque 51 -->

### Nivel 2: aceptación de la marcha blanca

El cierre de cada marcha blanca meses 13 a 15 para la Etapa 1, meses 19 y 20 para la Etapa 2 exige el cumplimiento copulativo de las seis condiciones siguientes. La ausencia de cualquiera de ellas impide el paso a producción.

Tabla 3.30:** Condiciones obligatorias para el cierre y aceptación de la marcha blanca.

**N°:** **1**. **Condición de cierre:** Ningún incidente abierto de severidad crítica o alta atribuible a la solución.. **Verificación:** Registro de incidentes con clasificación acordada y trazabilidad de cierre..

**N°:** **2**. **Condición de cierre:** Volumen de operación real comprometido alcanzado y sostenido durante al menos las cuatro últimas semanas del período.. **Verificación:** Telemetría de producción contrastada con el perfil transaccional declarado..

**N°:** **3**. **Condición de cierre:** Indicadores de disponibilidad y de tiempo de respuesta cumplidos de forma sostenida en ese mismo lapso, no en mediciones aisladas.. **Verificación:** Medición continua contra los umbrales del numeral 3.9..

**N°:** **4**. **Condición de cierre:** Conciliación sin diferencias no explicadas contra los registros del sistema vigente.. **Verificación:** Cuadratura de universos, ejecutada diariamente durante el período..

**N°:** **5**. **Condición de cierre:** Personal del CLIENTE capacitado y certificado en los procesos afectados, considerando el perfil de rotación declarado.. **Verificación:** Registro de capacitación con evaluación de competencia posterior..

**N°:** **6**. **Condición de cierre:** Mecanismo de reversión probado y operativo, con ensayo ejecutado en ambiente equivalente.. **Verificación:** Acta del ensayo de reversión, con tiempo efectivo medido..

Dos condiciones adicionales se aplican de forma específica a la Etapa 2 y responden a restricciones no negociables: la aceptación no procede sin el informe de auditoría independiente que acredite la separación de dominios sin hallazgos críticos abiertos, y no procede sin la conciliación diaria de saldos de la cartera cerrada sin divergencias pendientes.

<!-- origen: T7-03_Informes4_source.md | bloque 52 -->

### Nivel 3: aceptación por resultado de negocio

Los criterios de este nivel son los que el caso define como razón de la licitación. Se miden sobre operación real, con la línea base declarada por la propia compañía, y se distinguen según el reparto de responsabilidad establecido en el numeral 3.5.3.

Tabla 3.31:** Criterios de aceptación por resultado de negocio y metas comprometidas.

**Resultado comprometido:** **Discrepancia de inventario detectada en conteo cíclico**. **Línea base:** 12,4 % de las referencias auditadas. **Umbral de aceptación:** ≤ 2 % por categoría, sostenido en dos ciclos consecutivos. **Momento de medición:** Cierre del mes 36. **Responsabilidad:** Compartida.

**Resultado comprometido:** **Cancelación de pedidos por falta de existencia**. **Línea base:** 1,9 % anual; 2,7 % en el evento de junio de 2026. **Umbral de aceptación:** ≤ 0,3 % anual y cero cancelaciones por quiebre durante el evento anual. **Momento de medición:** Desde el mes 16, medición mensual. **Responsabilidad:** Compartida.

**Resultado comprometido:** **Merma desagregada por causa atribuible**. **Línea base:** 0 % de los ajustes clasificados. **Umbral de aceptación:** 100 % de los ajustes clasificados, con informe mensual cuadrado contra contabilidad. **Momento de medición:** Desde el mes 16. **Responsabilidad:** Sistémica.

**Resultado comprometido:** **Discrepancia entre precio exhibido y precio cobrado**. **Línea base:** 11 % en la fiscalización de febrero de 2026. **Umbral de aceptación:** ≤ 0,5 %, verificado por muestreo propio. **Momento de medición:** Desde el mes 16. **Responsabilidad:** Compartida.

**Resultado comprometido:** **Acreditación del precio publicado en un instante arbitrario**. **Línea base:** Capacidad inexistente. **Umbral de aceptación:** 100 % de las consultas resueltas dentro del umbral, sobre ventana de tres años. **Momento de medición:** Desde el mes 16. **Responsabilidad:** Sistémica.

**Resultado comprometido:** **Cumplimiento de la fecha de entrega comprometida**. **Línea base:** 81 % de los pedidos. **Umbral de aceptación:** ≥ 97 %, medido por pedido individual y no por promedio de canal. **Momento de medición:** Cierre del mes 36. **Responsabilidad:** Compartida.

**Resultado comprometido:** **Cobro sostenido sobre pedido no cumplible**. **Línea base:** Captura al aceptar el pedido. **Umbral de aceptación:** Cero casos. **Momento de medición:** Desde el mes 16. **Responsabilidad:** Sistémica.

**Resultado comprometido:** **Operaciones de crédito sin evidencia recuperable de consentimiento**. **Línea base:** 1.240 repactaciones de 2025. **Umbral de aceptación:** Cero operaciones, con retención acreditada y recuperación demostrada. **Momento de medición:** Desde el mes 21. **Responsabilidad:** Sistémica.

**Resultado comprometido:** **Tiempo de evaluación crediticia en punto de venta**. **Línea base:** Entre 40 segundos y 3 minutos. **Umbral de aceptación:** ≤ 8 segundos en percentil 95, sin incremento del tiempo total de atención. **Momento de medición:** Desde el mes 21. **Responsabilidad:** Sistémica.

**Resultado comprometido:** **Migración de la cartera activa**. **Línea base:** 620.000 clientes en plataforma sin soporte desde 2029. **Umbral de aceptación:** 100 % migrado con cero divergencias no conciliadas. **Momento de medición:** Antes del cierre de 2029. **Responsabilidad:** Sistémica.

**Resultado comprometido:** **Cruces de información entre ámbitos registrados**. **Línea base:** Registro inexistente. **Umbral de aceptación:** 100 % de los cruces registrados y auditoría sin hallazgos críticos. **Momento de medición:** Antes del mes 16. **Responsabilidad:** Sistémica.

**Resultado comprometido:** **Continuidad de venta y cobro ante pérdida de enlace**. **Línea base:** Detención de la operación. **Umbral de aceptación:** ≥ 8 horas de operación autónoma con reconciliación íntegra. **Momento de medición:** Desde el mes 16. **Responsabilidad:** Sistémica.

<!-- origen: T7-03_Informes4_source.md | bloque 53 -->

### Criterios de aceptación de naturaleza cualitativa

Cuatro criterios del caso no admiten expresión numérica y se verifican por observación directa. Se adoptan como criterios de aceptación de pleno derecho y no como ilustración del propósito del proyecto.

Tabla 3.32:** Criterios de aceptación cualitativa y forma de verificación.

**Criterio:** Ningún consumidor es derivado al fabricante, al servicio técnico o al vendedor externo como condición para que se le atienda una garantía legal.. **Forma de verificación:** Programa de cliente oculto ejecutado en las 22 tiendas, con resultado cero derivaciones..

**Criterio:** Una clienta con un pedido en curso conoce su estado real sin necesidad de contactar reiteradamente a la compañía, y es informada antes de cualquier cobro definitivo.. **Forma de verificación:** Auditoría del estado único del pedido y de la trazabilidad de notificaciones, contrastada con el registro de contactos entrantes por el mismo caso..

**Criterio:** Una jefatura de tienda puede demostrar qué proporción de su diferencia de inventario corresponde a error de registro y no a pérdida física.. **Forma de verificación:** Revisión del informe mensual de merma desagregada con una jefatura de tienda real, verificando que la explicación se sostiene con los datos del sistema..

**Criterio:** Un vendedor abre una tarjeta en menos tiempo que hoy sin que el cliente reciba menos información precontractual.. **Forma de verificación:** Medición comparada de tiempo de atención y auditoría censal de la constancia de entrega precontractual del mismo período..

<!-- origen: T7-03_Informes4_source.md | bloque 54 -->

### Reparto de responsabilidad y arbitraje del incumplimiento

Cuatro de los resultados del numeral 3.11.3 dependen conjuntamente de la plataforma entregada y de la ejecución operativa del CLIENTE: la plataforma provee el algoritmo de disponibilidad, la ruta de recambio de etiquetas y el orquestador de pedidos, pero el conteo, el escaneo y la preparación física los ejecuta el personal de sala. El acta de aceptación de cada uno de estos indicadores aislará el componente atribuible al sistema del componente atribuible a la adopción, y su medición se ejecuta primero sobre un piloto acotado de categorías, de modo que la desviación se detecte sobre un universo controlado antes del escalamiento.

Ante el incumplimiento de un criterio, el procedimiento es escalonado y no discrecional. En el nivel de entregable, la observación suspende la aceptación y abre plazo de subsanación, sin que ello habilite el avance de los entregables dependientes. En el nivel de marcha blanca, el incumplimiento de cualquiera de las condiciones copulativas impide el paso a producción y desplaza el hito, con la salvedad de que ningún desplazamiento puede reubicar una puesta en producción dentro de una ventana de congelamiento. En el nivel de resultado de negocio, el incumplimiento activa un plan de remediación conjunto con causa atribuida, cuya ejecución se somete a los mismos criterios de verificación.

Ninguna aceptación puede otorgarse de forma tácita por el transcurso del plazo, ni durante una ventana de congelamiento, ni de manera condicional sujeta a compromisos posteriores.
