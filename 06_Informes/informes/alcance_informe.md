# Alcance del Informe — Oferta Técnica

**Fuente:** `Informe Estado/Informe020926-8:39.docx` (Capítulo III — Esquema de Solución y Alcance)
**Caso:** 9 — Multitiendas Ancoa S.A.
**Proponente:** Only Simple Solutions
**Fecha de conversión:** Septiembre 2026

> Este documento es la **transcripción a Markdown del Capítulo III** del informe (.docx), que concentra el alcance de la solución. Se incluye también el análisis de si las etiquetas electrónicas de góndola (**ESL**) están dentro del alcance, a solicitud del equipo.

---

## 3. CAPÍTULO III — ESQUEMA DE SOLUCIÓN Y ALCANCE

### 3.1. Descripción de la solución propuesta y coherencia con el problema definido

*(Sección correspondiente en el docx; el contenido se mantiene en la fuente. La solución se articula sobre los 24 módulos que se detallan en 3.3 y la resolución de las 25 decisiones en 3.2.)*

---

### 3.2. Resolución de las decisiones pendientes declaradas por el CLIENTE

El Capítulo 16 de las Bases Técnicas enumera 25 decisiones estructurales que Ancoa delegó intencionalmente en los proponentes. Cada una admite múltiples enfoques arquitectónicos con impactos divergentes en costo, riesgo y continuidad operativa.

Este capítulo resuelve la totalidad de estas decisiones. Ninguna se traslada a una fase posterior ni se resuelve por omisión. Cada resolución queda inscrita en el registro consolidado de supuestos bajo la nomenclatura **SUP-nn**. Cuando una decisión depende de un dato empírico que la compañía hoy no posee, la arquitectura define un valor inicial fundamentado y un mecanismo de recalibración durante la fase de levantamiento. Desde la ingeniería del proyecto, se establece que **es preferible comprometer y gobernar un parámetro explícito antes que diseñar sobre vacíos operacionales**.

Cinco de estas decisiones condicionan la viabilidad central del proyecto y se desarrollan en extenso:

- ¿De dónde se extrae el dato de inventario que rige la promesa de venta?
- ¿Cuál es la estrategia de reemplazo para el sistema central monolítico de 2009?
- ¿Cuál es la frontera lógica de datos entre el negocio de retail y la filial de crédito?
- ¿Cómo se unifica la identidad del cliente sin vulnerar dicha frontera?
- ¿Cómo se garantiza la operación crediticia offline sin violar el mandato fiduciario?
- ¿Cómo se migra una cartera viva de 620.000 deudores mitigando el riesgo sistémico?

Las diecinueve decisiones restantes se presentan agrupadas por ámbito de negocio. La sección 3.2.7 aborda además cinco vacíos operacionales detectados por el proponente, incluyendo la resolución de una contradicción directa entre dos restricciones catalogadas como no negociables en las bases.

#### 3.2.1. SUP-01: El origen y cálculo de la disponibilidad de inventario

Las auditorías de conteo cíclico evidencian una discrepancia de inventario del **12,4 %**; sin embargo, la disponibilidad del canal digital se calcula sobre esta base inexacta aplicando un margen de seguridad estático y obsoleto heredado de 2019. Al ser un parámetro transversal que omite la varianza de exactitud entre categorías y sucursales, este modelo generó un impacto operacional y comercial crítico en el evento de junio de 2026, donde se autorizaron **2.840 transacciones sin respaldo físico**. Este incidente no responde a una falla de ejecución de código, sino a una falencia estructural en las reglas de negocio: la ausencia de un índice de confianza dinámico que pondere la calidad del dato de inventario antes de comprometer la promesa de venta.

Se establece la creación de un servicio centralizado, **Available to Promise (ATP)**, que pasa a ser la única fuente de verdad para los cuatro canales, prohibiendo por diseño técnico el acceso directo al inventario en bruto. Este componente calcula la cantidad comprometible restando del registro las unidades reservadas, los pedidos aceptados y un **colchón de incertidumbre dinámico**. Este parámetro se obtiene de la exactitud histórica medida por el conteo cíclico para esa categoría en ese punto de venta: una categoría con buen historial arriesga poco margen; una con historial de errores arriesga mucho más. El colchón se amplía automáticamente durante el evento anual, y el servicio entrega la disponibilidad acompañada de un **nivel de confianza**, evitando compromisos comerciales insostenibles.

Publicar con colchón implica mostrar menos disponibilidad aparente y asumir una menor venta en el corto plazo. Se acepta esta restricción deliberadamente: **una venta que no se puede cumplir genera un daño mayor al negocio**. El colchón deja de ser una variable rígida en el código y se consolida como un parámetro gobernable que la Gerencia de Logística define, firma y versiona. El riesgo inverso (un colchón sobrecalibrado) se monitorea comparando la tasa de cancelación resultante contra el 1,9 % anual actual.

#### 3.2.2. SUP-02: Estrategia de transición para el sistema central de 2009

El ecosistema tecnológico actual se caracteriza por una arquitectura fragmentada de **nueve plataformas** interactuando mediante **catorce integraciones punto a punto (P2P)** sin documentación centralizada. El sistema de 2009 opera como el nodo monolítico más crítico, gestionando el maestro de productos, compras, inventario contable y precios. Ante este nivel de acoplamiento, se descarta una estrategia de reemplazo total en un único corte por su alto impacto en la continuidad operativa y su incompatibilidad con las cinco ventanas anuales de congelamiento de TI. Simultáneamente, se rechaza preservar el status quo añadiendo nuevas conexiones directas, ya que esto incrementaría críticamente la deuda técnica y el riesgo operacional sobre una infraestructura no gobernable.

La arquitectura de transición se estructura en tres fases:

1. El **levantamiento exhaustivo** de las catorce integraciones, asumiendo este mapa topológico como un **entregable crítico del proyecto**, no como un insumo previo del cliente.
2. La implementación de un **bus de eventos (Event-Driven Architecture)** que desacopla la comunicación, prohibiendo nuevas conexiones P2P y retirando progresivamente las existentes, priorizando las que alimentan disponibilidad y precio.
3. La habilitación de un **API Gateway** frente al sistema de 2009 (**Patrón Estrangulador**), enrutando el tráfico para reemplazar capacidades progresivamente sin interrumpir la operación, manteniendo el **ERP actual intacto** como único emisor de documentos tributarios.

Se asume como restricción que este modelo transicional requiere mayor tiempo de ejecución que una reescritura total, y que una porción del núcleo de 2009 seguirá activa al finalizar el contrato. Para mitigar el riesgo de flujos paralelos no documentados (escritura directa en base de datos), se define una prueba de interceptación sobre un flujo piloto (carga de precios) antes de escalar el enrutamiento.

#### 3.2.3. SUP-03 y SUP-04: Frontera de datos e Identidad Unificada del Cliente

El gobierno de datos impone resolver la fricción legal entre el negocio de retail (sujeto a la Ley del Consumidor) y el negocio financiero (entidad fiscalizada). La construcción de una vista unificada de cliente exige establecer primero las barreras de privacidad, garantizando una separación lógica auditable.

El perímetro de cruce de datos se establece en tres dimensiones:

- **Sobre el contenido:** solo transita la información declarada en un inventario de interfaces autorizadas, fundamentada en bases de licitud explícitas (Ley N° 21.719).
- **Sobre la direccionalidad:** la restricción es bidireccional; el motor de originación crediticia no puede invocar atributos comerciales sin respaldo legal.
- **Sobre el control técnico:** un gestor de consentimientos deniega por omisión (**Zero Trust**) todo flujo no autorizado, registrando tanto cruces efectivos como intentos bloqueados. El motor de marketing excluye por diseño los atributos financieros.

La identidad (**SUP-03**) se resuelve mediante una arquitectura en dos capas. En el dominio retail, un motor de resolución unifica las interacciones (RUT + coincidencia probabilística) mediante **eventos asíncronos**. Hacia el dominio financiero, la interoperabilidad se ejecuta estrictamente mediante **consultas síncronas bajo demanda** (ej. solicitud explícita de estado de cuenta), contra una zona neutral que expone únicamente identificadores técnicos anonimizados. Se asume el costo operacional de latencia en consultas transfronterizas como una condición innegociable para asegurar el cumplimiento regulatorio.

#### 3.2.4. SUP-07: Continuidad de la operatoria de crédito ante desconexión de sucursales

El diseño arquitectónico debe resolver la fricción directa entre la exigencia de continuidad operativa y el cumplimiento normativo financiero. Por un lado, el negocio exige garantizar la venta y cobro **offline** durante un mínimo de **ocho horas**; un escenario de contingencia de alta probabilidad considerando que 14 de las 22 sucursales dependen de redes de terceros. Dado que la tarjeta propia concentra el 38 % de las transacciones, inhabilitarla invalida la continuidad real. Por otro lado, la filial emisora opera como entidad fiscalizada, imponiendo la restricción ineludible de acreditar y controlar el riesgo de cada operación.

Se establece un **modelo de contingencia offline basado en la preautorización de cupos**. Sin conexión, el punto de venta local no ejecuta evaluación de riesgo, sino que consume un cupo rotativo previamente aprobado y sincronizado en el servidor local, encolando la operación para su consolidación diferida. La exposición se mitiga mediante **cuatro umbrales dinámicos** calculados según el volumen real de la tienda:

1. límite transaccional unitario,
2. límite acumulado por cliente,
3. umbral de transacciones consecutivas, y
4. ventana de caducidad por reconexión.

Acciones que exigen perfilamiento crediticio (apertura de tarjeta, aumento de cupo) quedan bloqueadas por diseño sin enlace.

La asimetría del riesgo fundamenta la decisión: el riesgo real no es crediticio (el cupo fue evaluado pre-contingencia), sino el **fraude por doble consumo**. Bajo los parámetros del caso, la exposición por tienda ronda los **$150.000** frente a la mitigación de una pérdida de venta proyectada en **$10.000.000** por evento.

#### 3.2.5. SUP-25: Estrategia de migración de la cartera activa de crédito

La migración se define como el traslado concurrente de **620.000 clientes** con saldo vigente, repactaciones y procesos de cobranza/judiciales en curso. Dada la naturaleza de la entidad fiscalizada, se impone **tolerancia nula a la divergencia de saldos**. La restricción temporal es inamovible (**2029**), dictaminada por el fin de soporte del core de 2011 y el hito de remediación normativo.

Se descarta el reemplazo big bang. La transición se ejecutará mediante **olas de coexistencia**, operando ambas plataformas en paralelo con una **conciliación diaria automatizada**. Un umbral de discrepancia predefinido actuará como freno de emergencia (circuit breaker), deteniendo el avance de la ola ante divergencias contables. El mecanismo de rollback se mantendrá activo y validado durante toda la ventana de coexistencia.

El cronograma contractual se mantiene inalterado; la estrategia radica en **separar la habilitación técnica de la ejecución operativa**. El corte final ocurre en la Etapa 2, pero los componentes habilitantes (gestor de consentimientos, saneamiento de datos y motor de conciliación) se despliegan en la Etapa 1. Adelantar la ingeniería de datos financieros a la fase inicial es la única vía crítica viable para asegurar un margen de maniobra ante el límite regulatorio de 2029.

#### 3.2.6. Resolución de las decisiones restantes

**3.2.6.1. La existencia física: cómo se cuenta, cómo se reserva y dónde se almacena**

| ID | El dolor operativo y comercial | La resolución arquitectónica y de negocio |
| :--- | :--- | :--- |
| SUP-12 | La colisión de canales genera pérdida de venta cierta. Cuando un cliente digital reserva una unidad en el carro, el vendedor presencial queda bloqueado para facturar esa misma unidad física. | Se implementa una reserva temporal parametrizable al agregar al carro. La prelación de venta favorece... *(contenido completo en la fuente .docx)* |
| SUP-17 | La merma (1,9 % de las ventas) se consolida bajo un indicador único, impidiendo a las jefaturas aislar la pérdida por hurto de los descuadres administrativos. | Todo ajuste de inventario exige clasificación obligatoria en seis tipologías tipificadas (incluyendo error administrativo). *(contenido completo en la fuente .docx)* |

**3.2.6.2. El precio: consistencia omnicanal y evidencia fiscal**

| ID | El dolor operativo y comercial | La resolución arquitectónica y de negocio |
| :--- | :--- | :--- |
| SUP-08 | La asincronía entre el maestro de precios y el etiquetado físico (11 % de discrepancia) genera fricción en caja y vulnerabilidad ante fiscalizaciones de protección al consumidor. | Se establece **primacía del precio exhibido físicamente**. Ante una discrepancia detectada en caja, el sistema adopta... *(contenido completo en la fuente)* |
| SUP-09 | Las ventanas de actualización manual dejan un margen de hasta 24 horas donde el sistema central y la sala operan con listas de precios desfasadas. | La actualización de precios centralizados **no impacta el POS hasta que la tienda física escanea y confirma el recambio de la etiqueta de góndola** *(M-06)*. |

**3.2.6.3. El pedido: lógica de cobro, asignación y comisión**

| ID | El dolor operativo y comercial | La resolución arquitectónica y de negocio |
| :--- | :--- | :--- |
| SUP-11 | La cancelación de pedidos por quiebre de stock derivó en capturas financieras sobre mercadería inexistente, generando contingencias legales y operativas. | El checkout digital transiciona a un modelo de **"Preautorización sin Captura"**. El cargo efectivo solo se liquida tras la confirmación de... *(contenido completo en la fuente)* |
| SUP-13 | La asignación de fulfillment basada puramente en distancia geográfica vacía sistemáticamente las salas de venta de mayor rotación (17 %). | El orquestador de pedidos (**OMS**) sustituye la variable de proximidad por un algoritmo de **"Costo Total de Servir"**, que pondera el costo logístico de última... *(contenido completo en la fuente)* |

**3.2.6.4. Postventa, Marketplace y Logística Inversa**

| ID | El dolor operativo y comercial | La resolución arquitectónica y de negocio |
| :--- | :--- | :--- |
| SUP-15 | La devolución física de mercadería de sellers externos queda inmovilizada en bodegas propias sin trazabilidad, generando fricción en las liquidaciones financieras. | Se implementa notificación transaccional en tiempo real. Al procesar la recepción física en la tienda, el sistema dispara un... *(contenido completo en la fuente)* |
| SUP-16 | La ausencia de SLAs formales impide penalizar o excluir a los sellers externos que degradan la calidad del servicio. | Se activa un motor de gobernanza marketplace condicionado a la aceptación digital de políticas (T&C). El sistema mide automáticamente cinco KPIs críticos (tasa de...). *(contenido completo en la fuente)* |

**3.2.6.5. El crédito: acreditación del consentimiento**

| ID | El dolor operativo y comercial | La resolución arquitectónica y de negocio |
| :--- | :--- | :--- |
| SUP-05 | La dependencia de grabaciones telefónicas con purga a 90 días expone a la filial emisora a sanciones por incapacidad probatoria de repactaciones. | Sustitución completa hacia **expedientes digitales estructurados**. Se captura el contrato, metadatos de sesión (IP, canal, timestamp) y se sella... *(contenido completo en la fuente)* |
| SUP-06 | La obligación normativa de entregar información precontractual compite con los tiempos de atención; el personal comercial tiende a evadir procesos lentos. | El registro de entrega precontractual se embebe como **requisito sistémico bloqueante** en el flujo del POS/App, sin añadir clicks ni firma... *(contenido completo en la fuente)* |

**3.2.6.6. Identidad, Accesos y Seguridad Transaccional**

| ID | El dolor operativo y comercial | La resolución arquitectónica y de negocio |
| :--- | :--- | :--- |
| SUP-19 | Más de 1.100 repositores externos operan en sala e interactúan con sistemas sin relación laboral formal ni control de acceso directo. | Se delega la administración del ciclo de vida al proveedor B2B. A través del portal corporativo, el empleador externo aprovisiona y define la caducidad de... *(contenido completo en la fuente)* |
| SUP-23 | El desbordamiento de tráfico durante eventos masivos deriva en caídas catastróficas al no existir protocolos de degradación predefinidos. | Se implementa un **modelo de resiliencia escalonado**. La primera línea (salas de espera, limitación de concurrencia) escala automáticamente por... *(contenido completo en la fuente)* |

---

### 3.3. Módulos funcionales de la solución

La plataforma se estructura en **módulos** que responden directamente a los dolores operativos, asignando responsabilidades claras. La segmentación no obedece a una división técnica arbitraria: cada módulo encapsula un dominio de negocio con un dueño funcional identificable, un actor primario que lo opera y una o más decisiones estructurales de la sección anterior que lo justifican.

La agrupación replica la frontera regulatoria definida en SUP-04. **Los módulos del dominio retail y los del dominio financiero no comparten persistencia ni plano de red**, y toda interacción entre ambos transita por la capa transversal bajo el gobierno del gestor de consentimientos. Esta separación es la condición de admisibilidad de la propuesta y determina el emplazamiento físico descrito en el Capítulo IV.

#### 3.3.1. Dominio Retail: Núcleo de inventario y disponibilidad

| Módulo | Responsabilidad | Actor primario | Dolor que resuelve |
| :--- | :--- | :--- | :--- |
| **M-01 Motor de Disponibilidad (ATP)** | Constituirse en fuente única de verdad de la cantidad comprometible. Calcula el disponible descontando reservas, pedidos aceptados y colchón de incertidumbre dinámico, y publica el resultado con su nivel de confianza asociado. Bloquea por diseño el acceso directo... | ... | ... |
| **M-02 Gestión de Inventario, Conteo Cíclico y Merma** | Administrar el modelo de conteo continuo ABC en ventana valle, ejecutar los disparadores de conteo ciego, calcular la exactitud por categoría y punto que alimenta el colchón del M-01, y exigir la clasificación obligatoria de todo ajuste en las seis... | ... | ... |

*(Tabla completa M-01 a M-04 en la fuente .docx)*

#### 3.3.2. Dominio Retail: Precio y cumplimiento comercial

| Módulo | Responsabilidad | Actor primario | Dolor que resuelve |
| :--- | :--- | :--- | :--- |
| **M-05 Motor de Precios y Promociones** | Centralizar la carga, vigencia y propagación de precios y mecánicas promocionales hacia las 380 líneas de caja y el canal digital, aplicando el tope diario de modificaciones por referencia. | Gerencia Comercial. | Los cambios centralizados alcanzan hasta 400.000... |
| **M-06 Gobierno de Etiquetado Físico** | Generar las rutas de recambio por zona de sala, exigir el escaneo confirmatorio de cada etiqueta reemplazada y condicionar la activación del precio nuevo en POS a esa confirmación. Expone el tablero de desactualización por tienda. | Jefatura de tienda y personal... | ... |

*(Tabla completa M-05 a M-07 en la fuente .docx)*

> **Nota clave (ESL):** la solución **integra la posibilidad de etiquetas electrónicas (ESL)**. Hoy el módulo **M-06** gobierna el etiquetado físico (papel) con escaneo confirmatorio y condicionamiento del POS; la arquitectura queda **ESL-ready**, de modo que si el CLIENTE despliega etiquetas electrónicas (hardware que él adquiere, ver X-02 en 3.7.1), el sistema se integra **sin fricción ni re-ingeniería**: mismatch su T-06/M-07 ya resuelve la sincronización precio-exhibido/precio-cobrado y el ESL solo sustituye el medio físico de actualización.

#### 3.3.3. Dominio Retail: Venta, pedido y cumplimiento

| Módulo | Responsabilidad | Actor primario | Dolor que resuelve |
| :--- | :--- | :--- | :--- |
| **M-08 Punto de Venta y Nodo de Tienda** | Sostener la venta, el cobro, la aplicación de promociones vigentes y la emisión en contingencia con folios preasignados durante un mínimo de ocho horas sin enlace, y ejecutar la reconciliación idempotente al restablecerse la conexión. Provee el traspaso rápido... | ... | ... |
| **M-09 Orquestador de Pedidos (OMS)** | Gestionar la reserva temporal y su prelación entre canales, ejecutar la preautorización sin captura, asignar el nodo de cumplimiento por Costo Total de Servir, operar el motor de compensación ante quiebre y mantener el estado único del pedido consultable por todo... | ... | ... |

*(Tabla completa M-08 a M-11 en la fuente .docx)*

#### 3.3.4. Dominio Retail: Postventa, marketplace y logística inversa

*(Módulos M-12 a M-14; contenido en la fuente .docx)*

#### 3.3.5. Dominio Financiero: Filial emisora fiscalizada

Los módulos de esta capa operan bajo persistencia y plano de red segregados. Ninguno es invocable directamente desde el dominio retail.

| Módulo | Responsabilidad | Actor primario | Dolor que resuelve |
| :--- | :--- | :--- | :--- |
| **M-15 Originación y Evaluación Crediticia** | Ejecutar la evaluación en línea, determinar cupo bajo variables de capacidad de pago, aplicar el límite de tasa máxima convencional y exponer el simulador de costo total en lenguaje normalizado. | Ejecutivo de mesón financiero y vendedor de sala. | La evaluación... |
| **M-16 Gestor de Evidencia y Consentimiento** | Capturar el expediente digital estructurado con contrato, metadatos de sesión y sellado criptográfico; custodiarlo bajo política de inmutabilidad en almacenamiento frío con retención legal; y bloquear sistémicamente la aceptación que no cuente con registro... | ... | ... |

*(Tabla completa M-15 a M-19 en la fuente .docx)*

#### 3.3.6. Capa transversal: Integración, identidad y resiliencia

| Módulo | Responsabilidad | Actor primario | Dolor que resuelve |
| :--- | :--- | :--- | :--- |
| **M-20 Bus de Eventos y API Gateway** | Desacoplar la comunicación entre plataformas mediante publicación y suscripción, enrutar el tráfico hacia el núcleo de 2009 o hacia las capacidades ya reemplazadas, y gobernar el retiro progresivo de las integraciones punto a punto conforme al mapa topológico levantado... | ... | ... |
| **M-21 Gobierno de Frontera de Datos** | Mantener el inventario de interfaces autorizadas con su base de licitud, denegar por omisión todo cruce no declarado o con base revocada, y registrar de forma inalterable tanto los cruces efectivos como los intentos bloqueados. | Oficial de Cumplimiento y Contraloría... | ... |

*(Tabla completa M-20 a M-24 en la fuente .docx)*

#### 3.3.7. Cobertura y lectura del mapa modular

Los **veinticuatro módulos** cubren la totalidad de las decisiones resueltas en la sección anterior y de los vacíos identificados. Tres criterios explican la segmentación adoptada y anticipan la arquitectura del Capítulo IV.

1. **Separación de dominios:** los módulos M-15 a M-19 constituyen un perímetro cerrado cuya única vía de interacción con el retail son los módulos M-21 y M-22 de la capa transversal. Ningún componente comercial invoca directamente la cartera, el cupo ni el comportamiento de pago.
2. **Autonomía del borde:** los módulos M-01, M-05, M-07, M-08 y M-17 mantienen réplica operativa en el nodo de tienda, porque son los únicos que deben sostener venta, precio, cobro y crédito durante la contingencia de ocho horas. El resto opera exclusivamente en el plano central.
3. **Trazabilidad como responsabilidad asignada:** la evidencia del precio publicado tiene un módulo dueño (M-07), la del consentimiento tiene otro (M-16) y la de los cruces entre dominios un tercero (M-21). Ninguna quedó repartida entre componentes que puedan atribuirse mutuamente la omisión.

---

### 3.4. Diagrama conceptual de solución e interacción de actores

Mostrando la frontera entre retail y filial emisora. *(Diagrama en la fuente .docx)*

---

### 3.5. Objetivos del proyecto

Los objetivos se formulan bajo el estándar SMART: resultados específicos, metas cuantificadas, viabilidad arquitectónica y un horizonte anclado a los 56 meses del contrato. Ningún objetivo se redacta como intención ni admite verificación subjetiva.

#### 3.5.1. Objetivo General

Dotar a Multitiendas Ancoa S.A. de una **plataforma híbrida orientada a eventos** que garantice sus cuatro promesas comerciales (existencia, precio, entrega y condiciones crediticias). Esto exige operar sobre registros de exactitud comprobable, asegurar una separación auditable entre el retail y la filial emisora, y no degradar la continuidad operativa de las 22 sucursales ni exceder las ventanas de intervención.

El éxito global exige el cumplimiento de las **12 métricas específicas**, una auditoría de dominios sin hallazgos y la migración total de la cartera sin divergencias contables.

#### 3.5.2. Objetivos Específicos

| ID / Dimensión | Objetivo Específico | Línea Base a Meta | Medio de Verificación |
| :--- | :--- | :--- | :--- |
| OE-01 / Existencia | Reducir la discrepancia de inventario físico-lógico mediante conteo continuo ABC y clasificación de ajustes. | 12,4 % a ≤ 2 % por categoría | Indicador diario de exactitud y auditoría independiente. |
| OE-02 / Existencia | Eliminar cancelaciones por promesas sin respaldo físico mediante cálculo de disponibilidad con colchón dinámico. | 1,9 % a ≤ 0,3 % anual y cero quiebres en evento | Medición mensual de pedidos aceptados. |

*(Tabla completa de objetivos en la fuente .docx)*

#### 3.5.3. Responsabilidad sobre la adopción y los indicadores

El modelo de gobierno distingue estrictamente entre la capacidad técnica de la plataforma y la disciplina operativa de la compañía.

- **Indicadores garantizados (100 % sistémicos):** OE-03, OE-05 y OE-07 a OE-12 dependen íntegramente de la arquitectura entregada. Se comprometen y garantizan sin condición de adopción.
- **Indicadores compartidos (sistémicos + operativos):** OE-01, OE-02, OE-04 y OE-06 requieren esfuerzo conjunto. La solución provee la capacidad (ej. algoritmo ATP, ruteo de etiquetas), pero el CLIENTE ejecuta el proceso físico en sala (conteo, escaneo, picking). El acta de aceptación técnica aislará el rendimiento del software de la adopción humana, desplegando estas funciones primero en pilotos acotados antes del escalamiento.

---

### 3.6. Alcance de la Etapa 1 y de la Etapa 2, con criterio de asignación

El cronograma contractual de 56 meses se asume como indivisible e inalterable:

- **Etapa 1:** desarrollo meses 1–12, marcha blanca 13–15, producción mes 16.
- **Etapa 2:** desarrollo 13–18, marcha blanca 19–20, producción mes 21.
- **Operación:** meses 21–56.

La definición de alcance no consiste en redistribuir estos plazos, sino en **determinar qué capacidades se construyen y liberan en cada ventana**. La preferencia de urgencia del Comité Directivo (inventario → precio → negocio financiero/marketplace/analítica) se adopta como directriz base, con una corrección estructural en su tramo final para mitigar el riesgo sistémico de la migración financiera.

#### 3.6.1. Criterios de asignación

Se establecen **seis criterios excluyentes**, en estricto orden de precedencia:

1. **Dependencia técnica dura:** las capacidades habilitantes anteceden a las dependientes (la frontera de datos precede a cualquier vista unificada; el motor de disponibilidad precede a la promesa de entrega; el bus de eventos precede a la estrangulación del núcleo de 2009).
2. **Irreversibilidad arquitectónica:** los componentes cuya separación a posteriori es inviable se ejecutan primero (segregación lógica/física retail vs. financiero).
3. **Hitos regulatorios externos:** cumplimiento ineludible de la fecha 2029 (remediación + fin de soporte del core de 2011).
4. **Exposición legal vigente:** priorización de lo vinculado a pasivos normativos en curso (2.840 cancelaciones; fiscalización de precios de febrero 2026).
5. **Capacidad de absorción operacional:** dimensionamiento sobre la capacidad real del área de TI del CLIENTE (46 profesionales), evitando el colapso en hitos paralelos.
6. **Ventanas de congelamiento de TI:** concentrar intervenciones mayores en las dos ventanas viables (marzo–abril y julio–octubre).

#### 3.6.2. La corrección al orden de urgencia declarado

El análisis de riesgo valida la imposibilidad de migrar una cartera viva de 620.000 clientes con saldo durante la limitada ventana de seis meses de desarrollo de la Etapa 2. La estrategia **no altera la fecha del corte final** (se mantiene en Etapa 2 para respetar el orden comercial), sino que **escinde la habilitación técnica de la ejecución operativa**: despliegue temprano en Etapa 1 de los habilitantes críticos (gobierno de la frontera de datos, captura estructurada de consentimientos, archivo inmutable de largo plazo, saneamiento de los 620.000 registros y motor de conciliación).

La **analítica predictiva y los modelos de ML** se introducen de manera controlada a través de la **Cartera de Innovaciones**, estrictamente sobre datos anonimizados, condicionando su activación a una auditoría técnica que certifique que la frontera de datos es infranqueable.

#### 3.6.3. Asignación de alcance por módulo (Regla del 100 %)

La matriz asigna cada uno de los veinticuatro módulos a una etapa contractual. Para los módulos de despliegue progresivo, se delimita explícitamente la entrega parcial, erradicando duplicidades.

| Módulo | Alcance Etapa 1 | Alcance Etapa 2 |
| :--- | :--- | :--- |
| M-01 Motor de Disponibilidad | Servicio completo, colchón dinámico y publicación del nivel de confianza. | - |
| M-02 Inventario y Merma | Modelo ABC, disparadores, clasificación de merma e indicador de exactitud. | - |
| M-03 Maestro de Artículos | Validación de completitud como condición de publicación e indicador de calidad. | - |
| M-04 Gestión de Nodos Logísticos | Habilitabilidad de nodos y exclusión del CD de Concepción. | - |
| M-05 Motor de Precios | Carga, vigencia, propagación y tope diario de modificaciones. | - |
| M-06 Etiquetado Físico | Rutas de recambio, escaneo confirmatorio y condicionamiento del POS. | - |
| M-07 Trazabilidad de Precio | Versionado, réplica local y repositorio central inmutable (retención de tres años). | - |
| M-08 Punto de Venta (POS) | Venta, cobro, promociones y emisión en contingencia con folios preasignados. | - |
| M-09 Orquestador de Pedidos | Reserva, preautorización sin captura, asignación por costo total de servir. | - |
| M-10 Atribución de Venta | Imputación al origen y liberación contra confirmación física de movimiento. | - |
| M-11 Portal del Cliente | Consulta pública de precio, disponibilidad y estado de pedido; notificación retail. | Consulta autenticada de estado de cuenta y documentos financieros, bajo control de cruce. |
| M-12 Gobernanza Marketplace | - | Onboarding, sincronización de catálogo, SLAs y suspensiones escalonadas. |
| M-13 Postventa / Log. Inversa | Garantía legal en primera línea, retracto parametrizable y cuarentena lógica. | - |
| M-14 Conciliación Recobros B2B | Registro del expediente de recuperación asociado a cada prestación. | Liquidación automática, notificación al vendedor e imputación de cobro. |
| M-15 Originación Crediticia | - | Evaluación en línea, determinación de cupo, límite de tasa máxima y simulador. |
| M-16 Gestor de Evidencia | Captura estructurada, sellado criptográfico y archivo inmutable a largo plazo. | Bloqueo sistémico de la aceptación sin registro previo en originación. |
| M-17 Contingencia Offline | Replicación del cupo preaprobado desde la plataforma vigente vía fachada. | Contingencia nativa con umbrales dinámicos y ventana de caducidad. |
| M-18 Administración de Cartera | - | Saldos, facturación, prelación de imputación y límites normativos de cobranza. |
| M-19 Migración de Cartera | Saneamiento de los 620.000 registros; motor de conciliación validado. | Olas de coexistencia, corte final y decomiso de la plataforma de 2011. |
| M-20 Bus de Eventos y API | Mapa topológico, bus, fachada y retiro de integraciones críticas (disponibilidad/precio). | Retiro de las integraciones restantes por prioridad del mapa. |
| M-21 Frontera de Datos | Inventario de interfaces, denegación por omisión y registro de cruces inalterable. | - |
| M-22 Resolución de Identidad | Unificación en dominio retail y consolidación de zona neutral de identificadores. | Consulta síncrona transfronteriza habilitada para operaciones financieras. |
| M-23 Identidad y Accesos (IAM) | Credencial individual, traspaso de sesión y conector automatizado de RRHH. | Aprovisionamiento delegado de perfiles externos con caducidad automatizada. |
| M-24 Observabilidad | Instrumentación, niveles de degradación y bloqueo automático de despliegues. | - |

#### 3.6.4. Colisiones de calendario declaradas

Asumiendo la adjudicación en diciembre de 2026 y la formalización contractual, el Mes 1 inicia en enero de 2027, situando las salidas a producción en abril de 2028 (Etapa 1) y septiembre de 2028 (Etapa 2), esquivando los bloqueos anuales. Las colisiones residuales se abordan con planes de mitigación técnicos:

| Momento | Colisión Operativa / Normativa | Estrategia de Tratamiento |
| :--- | :--- | :--- |
| Meses 11–12 | El cierre de desarrollo (Etapa 1) choca con el congelamiento de Navidad y el pico de 1.900 altas de temporada. | Congelamiento absoluto de despliegues productivos. Las pruebas integrales y de estrés se ejecutan en Preproducción asimilando el volumen real del peak. |
| Mes 13 | El inicio de la marcha blanca coincide con la última semana del congelamiento de fin de año (hasta el 6 de enero). | Inicio efectivo de la marcha blanca diferido al 7 de enero. La desviación (6 días) se absorbe con reserva de contingencia sin desplazar el hito de Producción. |

#### 3.6.5. Fase de Operación

Se despliegan **36 meses continuos de operación y soporte de misión crítica** (meses 21 a 56). La estrategia incluye soporte **24x7x365** para el canal digital y los componentes financieros, y atención en horario comercial extendido (09:00–23:00) para sucursales y operaciones físicas. Cobertura reforzada documentada para los tres eventos anuales masivos y soporte especializado presencial distribuido en las 11 regiones.

---

### 3.7. Exclusiones explícitas, supuestos y restricciones

#### 3.7.1. Exclusiones explícitas

Los siguientes componentes quedan **excluidos del alcance de implementación**. La arquitectura se diseña asumiendo la convivencia y la orquestación con estos elementos:

| N° | Exclusión | Diseño Compensatorio y Convivencia Arquitectónica |
| :--- | :--- | :--- |
| X-01 | Reemplazo del ERP central y emisión de documentos tributarios. | El ERP permanece como emisor único de DTEs. La solución actúa como enrutador y provee conciliación y foliado local para contingencias offline. |
| **X-02** | **Adquisición física de etiquetas electrónicas para góndola (ESL).** | La adquisición del hardware la efectúa el CLIENTE; el proponente especifica la tecnología y su costo. La arquitectura queda **ESL-ready**: M-06/M-07 ya resuelven la sincronización precio-exhibido/precio-cobrado, y el ESL se integra sin fricción cuando el CLIENTE lo despliegue. Mientras tanto, la mitigación base mantiene la retención del precio anterior en el POS hasta el escaneo físico manual. |
| X-03 | Adquisición de dispositivos móviles para vendedores de sala. | La arquitectura asume la restricción existente (640 terminales para 3.820 personas) y resuelve la fricción mediante traspasos nominativos rápidos de sesión. |
| X-04 | Desarrollo del portal interno de vendedores de Marketplace y su logística. | La integración se limita al onboarding, sincronización de stock, monitoreo de SLAs (5 KPIs) y notificación de devoluciones físicas. |
| X-05 | Motor de cálculo contable y liquidación de remuneraciones. | Se procesa y exporta la base bruta de cálculo para atribuir comisiones cruzadas, pero el pago lo ejecuta el sistema del CLIENTE. |
| X-06 | Sistema de cobranza judicial y ejecución de embargos. | El perímetro abarca exclusivamente el registro inmutable y la trazabilidad de las gestiones extrajudiciales y repactaciones. |
| X-07 | Flotas y sustitución de proveedores de última milla. | Integración API para trazabilidad del ciclo de vida del despacho, excluyendo el ruteo interno de los camiones de terceros. |
| X-08 | Obras civiles, canalización eléctrica y cableado estructurado. | El diseño entrega la planimetría y el cálculo de potencia/refrigeración; la ejecución es responsabilidad exclusiva del CLIENTE. |
| X-09 | Adquisición de hardware (POS, red, infraestructura de edge). | Dimensionamiento y especificación técnica exhaustiva en la Oferta Técnica para la compra directa por el CLIENTE. |
| X-10 | Contratos de telecomunicaciones de centros comerciales. | La arquitectura Edge (servidores locales) absorbe las caídas de red de terceros garantizando la autonomía comercial. |
| X-11 | Implementación del WMS en el CD de Concepción. | La infraestructura logística se excluye como punto de promesa digital hasta que abandone el control manual basado en planillas. |
| X-12 | Saneamiento retroactivo de la base histórica del inventario físico. | La arquitectura gestiona el margen de error conocido (12,4 %) para calcular el disponible; no se ejecutan conteos ciegos correctivos masivos fuera del modelo cíclico ABC. |

#### 3.7.2. Supuestos

Los parámetros de dimensionamiento y capacidad que condicionan la planificación se formulan como supuestos gobernables, sujetos a re-validación en la fase de levantamiento:

| ID | Supuesto estructural | Impacto operacional | Mecanismo de validación |
| :--- | :--- | :--- | :--- |
| S-A | El mes 1 del contrato corresponde a enero de 2027. | Desplazamientos que expongan los hitos de producción al congelamiento de Navidad forzarían la reprogramación total del proyecto. | Aprobación del Acta de Inicio en Mes 1. |
| S-B | El evento Cyber de 2028 se fija entre mayo y junio, notificado con 6 semanas de anticipación. | Un adelanto anómalo reduce la ventana de estabilización post-paso a producción (Etapa 1). | Anuncio oficial de la Cámara de Comercio. |

*(Lista completa de supuestos en la fuente .docx)*

#### 3.7.3. Restricciones

**Restricciones de Continuidad y Operación Física (Edge Computing):**
- Continuidad operacional offline estricta en infraestructura on-premise por **24 horas continuas** (venta, cobro y contingencia crediticia; 8 horas en tiendas). Para el CD Concepción, autonomía de 4 horas.
- Restablecimiento de red y sincronización bidireccional forzosa en máximo **30 minutos** sin pérdida de DTEs ni solapamiento de stock.
- Tolerancia nula a la indisponibilidad de terminales por rotación; sesión cajero-vendedor con rotación de credenciales (hot-swapping).
- Cinco ventanas de congelamiento inamovibles, implementadas como barreras automatizadas de CI/CD.

**Restricciones Legales y Normativas (Zero Trust y Protección de Datos):**
- Arquitectura de segregación lógica y auditoría inmutable estricta (incomunicación por defecto entre la filial de crédito y el retail).
- Inmutabilidad probatoria de largo plazo: registros precontractuales, timestamp de entrega de información y consentimiento de repactación archivados en almacenamiento frío **por vigencia de la deuda más 6 años**.
- Derivación de garantías prohibida por diseño; la postventa absorbe contingencias en primera línea.

**Restricciones Contractuales del Proceso de Licitación:**
- Plazo contractual de 56 meses y adopción obligatoria del despliegue en nube híbrida.
- Integración auditable de **cinco modelos de innovación** valorizados económicamente, incluyendo algoritmos de ML controlados perimetralmente.
- Censura absoluta de información tarifaria, precios unitarios y cálculos financieros en el cuerpo de la Oferta Técnica (Sobre N°2).

---

### 3.8. Catálogo de requerimientos funcionales core

El Anexo Técnico X consolida **223 requerimientos funcionales atomizados**. Esta sección expone estrictamente el subconjunto **core**: aquellos cuya omisión vulnera las restricciones innegociables del CLIENTE o bloquea dependency arquitectónicas estructurales.

**Criterio de selección:** un requerimiento integra el núcleo core si (1) implementa directamente una de las quince restricciones no negociables, (2) materializa una decisión estructural de arquitectura, o (3) constituye un prerrequisito técnico bloqueante para el resto de su módulo.

**Prioridad:** se aplica el marco MoSCoW; la totalidad del catálogo core es **M (Must)**.

*(Subsecciones 3.8.1 a 3.8.8, tablas de RF con trazabilidad a Módulo/Etapa/Restricción en la fuente .docx.)*

---

### 3.9. Catálogo de requerimientos no funcionales core

Con valor numérico verificable (RTO, RPO, tiempos de sincronización, latencia de consulta). *(Detalle en la fuente .docx; marcado como "Revisar dado el alcance, y recortar".)*

---

### 3.10. Estrategia para obtener el apoyo de los grupos de interés clave

**El vendedor comisionista.** El vendedor de sala opera bajo escasez de recursos y su remuneración depende de la fluidez del sistema. Si el nuevo sistema es percibido como un obstáculo, será evadido. La estrategia se basa en tres pilares:

1. **Protección de la comisión (M-10):** el módulo de atribución de venta garantiza que el vendedor no pierda su comisión cuando una unidad de su sala se despacha para un pedido web, ni cuando se realiza una venta presencial con inventario en otra sucursal.
2. **Reducción del tiempo en la evaluación crediticia:** el principal motivo de evasión es que los procesos de cumplimiento normativo son lentos (actualmente 40 segundos a 3 minutos, SUP-06). La solución reduce la evaluación a **≤ 8 segundos** (OE-09, M-15) y embebe el registro de información precontractual y consentimiento como requisito sistémico bloqueante sin clics adicionales ni firma en papel (M-16). El cumplimiento normativo se vuelve "invisible" para el vendedor.
3. *(Detalle de estrategia para jefaturas de tienda en la fuente .docx.)*

---

### 3.11. Criterios de aceptación del alcance comprometido

Alineados a los resultados de negocio del caso. *(Sección marcada como "Trabajar" en la fuente .docx.)*

---

## Análisis: ¿Las etiquetas electrónicas de góndola (ESL) entran dentro del alcance?

### Decisión del equipo (confirmada)

La solución **integra la posibilidad de tener ESL** (arquitectura **ESL-ready**), pero el **hardware ESL queda fuera** del alcance de implementación del proponente (lo adquiere el CLIENTE, conforme a la regla del caso: "el hardware lo adquiere el CLIENTE; el proponente especifica").

**Postura técnica:** la mejor solución al dolor del **11 % de discrepancia precio exhibido vs. cobrado** no exige que el proponente instale el hardware. Exige que el **sistema** gobierne la sincronización precio-exhibido/precio-cobrado (M-06/M-07) y que el **ESL se integre sin fricción** cuando el CLIENTE lo despliegue. Por eso:

- **Hardware ESL: NO** en el alcance de implementación (X-02). Lo especifica y costea el proponente; lo adquiere el CLIENTE.
- **Integración ESL-ready: SÍ** en la arquitectura. M-06/M-07 quedan preparados para que el ESL sustituya el medio físico de actualización sin re-ingeniería.

### Evidencia en el informe

1. **Exclusión X-02 (Tabla 16):** "Adquisición física de etiquetas electrónicas para góndola" queda como **exclusión de la ADQUISICIÓN de hardware**, no de la integración. El diseño compensatorio declara: *"La arquitectura queda ESL-ready... el ESL se integra sin fricción cuando el CLIENTE lo despliegue."*
2. **Módulo M-06:** sigue siendo el **gobierno del etiquetado** (hoy físico con escaneo confirmatorio), pero diseñado como **ESL-ready** (canal de actualización intercambiable: papel o electrónico).
3. **Contexto (Cap. 2.1.4):** el caso indica "instalar etiquetas electrónicas (sí evaluarlas y costearlas)", es decir, **evaluarlas y costearlas sí**, **adquirirlas/instalarlas no** por parte del proponente.

### Coherencia con el principio "presupuesto ilimitado / mejor solución" (AGENTS.md)

El principio **no se contradice** con mantener el hardware fuera del alcance de implementación:

- La **mejor solución** se entrega a nivel de **sistema**: M-06/M-07 resuelven el dolor de precio con exactitud comprobable y evidencia fiscal (OE-04, OE-05), con o sin ESL.
- El **ESL** es un habilitador de hardware cuya **posibilidad queda integrada** en la arquitectura. Si el CLIENTE quiere el beneficio adicional del despliegue electrónico, la solución ya lo soporta sin costo de re-ingeniería.
- Costear y especificar el ESL por parte del proponente cumple con el caso y alinea la decisión con el principio: **se ofrece la mejor solución completa**, y el hardware, cuyo dueño contractual es el CLIENTE, se integra sin fricción.

**Conclusión registrada:** el ESL queda como **innovación valorizada (INN-3)** y como **capacidad ESL-ready** de la arquitectura (M-06/M-07), no como hardware de implementación. No se requiere modificar la EDT ni el flujo de caja por este concepto; solo se refuerza que el sistema soporta el despliegue de ESL por el CLIENTE.

---

*Documento generado a partir de `Informe Estado/Informe020926-8:39.docx` (Capítulo III). Para contenido completo de tablas no transcritas (módulos, RF, supuestos), ver el archivo .docx original.*
