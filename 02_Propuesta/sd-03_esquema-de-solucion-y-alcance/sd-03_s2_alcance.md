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
actualizado: 2026-10-04
---
# 3.2 Alcance

<!-- contenido migrado desde la fuente; permanece en borrador y requiere revisión humana -->

## Propósito y delimitación del alcance

La solución debe ayudar a Multitiendas Ancoa S.A. a cumplir cuatro promesas: existencia disponible, precio publicado y cobrado, entrega en la fecha informada y condiciones crediticias acreditables. El alcance aborda las causas sistémicas que Ancoa ha descrito: registros con distinta confiabilidad, integraciones punto a punto desactualizadas, una frontera incompleta entre Retail y el Emisor, incentivos y procesos operativos que afectan la ejecución, y diferencias de conectividad y calendario entre tiendas y centros de distribución.

El problema no se atribuye a una sola plataforma. Ancoa declara nueve plataformas de seis proveedores y catorce interfaces punto a punto, la mayoría de archivos y procesos nocturnos; no dispone de un mapa completo. El levantamiento y la documentación de las catorce interfaces forman parte del trabajo. Una flecha de una topología funcional no se cuenta como una interfaz: los extremos, dirección, datos, frecuencia y mecanismo de cada interfaz se confirmarán en el levantamiento.

### Servicios de aplicación comprendidos

Tabla 3.1: Catálogo de servicios de aplicación comprometidos.

El catálogo funcional de esta propuesta comprende trece servicios desplegables: nueve de Retail, tres del Emisor financiero y uno de frontera controlada entre ambos. El número identifica servicios de aplicación; no fija el número de microservicios, módulos internos, APIs ni productos de infraestructura. La decisión sobre esas unidades técnicas depende del diseño detallado y de la evidencia obtenida sobre las plataformas e interfaces existentes.

| Código | Servicio de aplicación | Responsabilidad incluida |
| :--- | :--- | :--- |
| R-01 | Catálogo, precios y promociones | Mantener oferta, vigencias y promociones; habilitar la consistencia y evidencia del precio. |
| R-02 | Abastecimiento y reposición | Gestionar abastecimiento y reposición para tiendas y canales. |
| R-03 | Inventario, reservas y disponibilidad | Controlar movimientos y reservas, y calcular la disponibilidad que puede comprometerse. |
| R-04 | Pedidos y cumplimiento omnicanal | Coordinar pedidos, estado único, asignación y cumplimiento entre canales y nodos. |
| R-05 | Registro y conciliación de ventas | Acreditar ventas, anulaciones y reversas y conciliar los registros pertinentes. |
| R-06 | Atribución de ventas y comisiones | Registrar la atribución de ventas y comisiones según el movimiento y cumplimiento efectivo. |
| R-07 | Integración y gobierno de marketplace | Intercambiar oferta y datos operativos con vendedores externos bajo reglas de Ancoa. |
| R-08 | Posventa, garantías y devoluciones | Gestionar casos posteriores a la venta, devoluciones, garantías y su efecto en inventario. |
| R-09 | Clientes y fidelización Retail | Administrar identidad y fidelización comercial dentro del dominio Retail. |
| F-01 | Originación y autorización de crédito | Evaluar y autorizar operaciones de crédito bajo controles del Emisor. |
| F-02 | Cartera, cobranza y repactaciones | Administrar saldos, cuotas, cobranza y repactaciones del Emisor. |
| F-03 | Consentimiento y evidencia financiera | Acreditar la información precontractual entregada, el consentimiento y la evidencia financiera. |
| X-01 | Autorización y auditoría de cruces Retail–Emisor | Autorizar y registrar cada cruce permitido entre los dos dominios. |

Estos servicios se relacionan con las cuatro promesas y con responsabilidades de negocio A1–A11, B1–B3 y C1–C2. La capa de integración, gestión de identidad y acceso, seguridad y observabilidad los habilita; no constituye servicios adicionales de negocio ni define por sí sola una tecnología o producto.

### Límite funcional por actor

Tabla 3.2: Actores y límites funcionales de interacción.

La presencia de un actor no exige crear un servicio distinto. El alcance cubre sus interacciones con los servicios anteriores; los permisos y datos dependen del negocio, finalidad y rol de cada flujo.

| Actor o grupo que interactúa | Interacción cubierta por el alcance | Límite o condición |
| :--- | :--- | :--- |
| Cliente o consumidor; titular del Emisor | Consulta oferta, precio, disponibilidad y pedido; solicita posventa, crédito o información financiera pertinente. | Las interacciones comerciales y financieras se separan por contexto y finalidad. |
| Personal de venta, caja, tienda y centros de distribución | Consulta y registra precio, ventas, movimientos, preparación, despacho, devoluciones y, cuando está autorizado, inicia una solicitud de crédito. | La atención de crédito requiere facultades vigentes; operar la venta sin enlace no habilita automáticamente originación de nuevos créditos. |
| Comercial, compras, logística, planificación y marketing | Mantiene catálogo, oferta, precio, abastecimiento, campañas y cumplimiento del canal Retail. | Marketing y fidelización Retail no acceden a atributos financieros. |
| Negocio financiero del Emisor | Evalúa y autoriza crédito; administra cartera, cobranza, repactaciones y sus evidencias. | Mantiene autoridad sobre los datos y decisiones financieras. |
| Control interno, cumplimiento y auditoría | Revisa evidencia, finalidades y cruces entre dominios, incluidas las denegaciones. | Sus accesos son nominados y auditables; no son una autorización general para consultar ambos dominios. |
| TI y soporte | Configura, integra y opera identidad, interfaces, seguridad y monitoreo. | El privilegio técnico no habilita modificar reglas de negocio ni consultar datos sin autorización. |
| Vendedores de marketplace, transportistas y repositores externos | Publican o actualizan oferta y reportan hitos de cumplimiento cuando el contrato y la integración lo permitan. | Acceso acotado a la organización, datos y operaciones que les corresponden. |
| Dirección, propiedad y organismos fiscalizadores | Dirección y control aprueban, supervisan y reciben evidencia; propiedad participa como grupo de interés estratégico; los organismos actúan según su competencia. | No se modelan como usuarios operativos salvo interacción directa definida. |

### Delimitación del alcance respecto de las plataformas actuales

Tabla 3.3: Decisiones de alcance relativas a plataformas y capacidades actuales.

La tabla siguiente fija los límites de intervención a partir de lo informado por Ancoa y de las propuestas que el proponente debe justificar. No sustituye el diagnóstico del ecosistema ni presume conexiones, productos, protocolos o capacidades todavía no verificadas.

| Plataforma o capacidad | Tratamiento que delimita el alcance | Estado de decisión |
| :--- | :--- | :--- |
| Plataforma de originación y cobranza de crédito (2011) | Reemplazarla y migrar la cartera activa, saldos y operaciones asociadas con conciliación. El soporte anunciado termina en 2029. | Reemplazo requerido; el plan detallado de migración y sus hitos deben quedar trazados. |
| ERP y emisión tributaria | Mantener el ERP como único emisor de documentos tributarios e integrarlo con los servicios pertinentes. | Permanencia definida por Ancoa; su reemplazo queda fuera del alcance. |
| Marketplace | Mantener la plataforma de vendedores; integrar pedidos, estados, devoluciones, posventa y liquidaciones que correspondan. | Permanencia definida por Ancoa; construir una plataforma sustitutiva de vendedores queda fuera. |
| WMS del centro de distribución principal (2016) | Mantener e integrar sus movimientos operacionales con inventario y pedidos. | Permanencia definida por Ancoa. |
| Centro de distribución de Concepción | Evaluar y costear por separado la eventual implantación o extensión de WMS; actualmente opera con planillas. | Pendiente de decisión; no se da por incluida como implantación comprometida. |
| Sistema central de Retail (2009) | Mantenerlo durante la transición e integrar/desacoplar gradualmente capacidades prioritarias. Evaluar reemplazo por etapas solo si el levantamiento demuestra una brecha funcional, de soporte, control o capacidad que no pueda resolverse integrándolo. | Decisión condicionada a evidencia; no se propone reemplazo integral por defecto. |
| POS de tienda (2014) | El alcance debe entregar la operación de venta sin enlace exigida y la unificación de la experiencia de caja. Verificar primero las capacidades de las versiones instaladas; adquirir, desarrollar o reemplazar el software POS solo si la alternativa actual no satisface los requisitos probados. | Capacidad comprometida; elección de producto y eventual reemplazo condicionados al levantamiento y prueba. |
| Comercio electrónico (2019) | Integrarlo con disponibilidad y pedidos; probar su comportamiento extremo a extremo bajo las cargas, latencias y disponibilidad requeridas. | Mantener si supera la prueba; reemplazar solo si la brecha pertenece a la plataforma y no se resuelve mejorando datos o integración. |
| Fidelización (2017) | Mantenerla integrada con separación efectiva, trazable y auditable de los datos y finalidades de Retail y Emisor. | Mantener si supera la prueba de segregación; reemplazar si no puede impedir cruces no autorizados. |
| Plataforma número nueve | Identificarla y documentar su función, proveedor, interfaces y dependencias. | INCOMPLETO TEMPORALMENTE: no asignar reemplazo, integración ni conexiones hasta conocer su identidad. |
| Precios y promociones | Crear o adquirir la capacidad que hoy no existe como sistema: registrar y propagar precios y promociones que ahora se preparan en planillas y cargas masivas. | Nueva capacidad en alcance; no equivale a reemplazar una plataforma existente. |
| Catorce interfaces punto a punto | Levantar su inventario como entregable temprano y rediseñar su integración gradualmente sin detener la operación. | Rediseño requerido; no significa reemplazar las nueve plataformas ni supone una interfaz por flecha del diagrama. |

Se consideran dos alternativas para estimar y decidir el nivel de renovación. En ambas se mantienen las decisiones fijadas por Ancoa, la nueva capacidad de precios y promociones y el rediseño de interfaces:

- **Escenario A — continuidad selectiva (referencia recomendada):** reemplazar crédito; asegurar la capacidad POS offline, cambiando el software solo si las pruebas lo exigen; mantener e integrar el sistema central, ERP, marketplace y WMS principal; evaluar comercio electrónico y fidelización con las pruebas indicadas; identificar la novena plataforma y evaluar por separado Concepción.
- **Escenario B — renovación ampliada del núcleo:** incluye las decisiones del Escenario A y agrega reemplazar por etapas el sistema central de Retail. También reemplaza comercio electrónico o fidelización únicamente si no superan sus pruebas de capacidad o segregación. Cada sustitución requiere evidencia, convivencia, conciliación y reversa.

El reemplazo se decide por soporte, capacidad, controles, interfaces, costo y riesgo de transición, no por la antigüedad como criterio aislado. La topología y el estado descriptivo de cada plataforma se documentan en la sección de Dimensionamiento del problema; aquí se fija cómo afectan los límites del trabajo comprometido.

### Supuestos y decisiones pendientes de validación

1. Ancoa ha declarado nueve plataformas y catorce interfaces, pero no dispone de un inventario completo de sus extremos. Su levantamiento es una actividad y entregable del proyecto.
2. La conectividad entre cada pareja de plataformas, el sentido de los datos, la frecuencia, el protocolo y la tecnología no se consideran confirmados por la topología inferida.
3. La capacidad offline del POS y la factibilidad de cualquier operación de crédito sin enlace requieren validación técnica y de cumplimiento. La apertura de tarjetas nuevas sin conexión queda excluida; el uso de un cupo previamente aprobado solo podrá incluirse en la contingencia financiera si el Emisor demuestra su factibilidad y controles.
4. El soporte del proveedor de la plataforma de crédito termina en 2029, según lo informado por Ancoa. El reemplazo y la migración deben planificarse para cumplir ese hito sin pérdida ni diferencias de saldos sin conciliar.
5. Toda decisión condicionada sobre sistema central, POS, comercio electrónico, fidelización, WMS de Concepción y plataforma no identificada se cierra con resultados del levantamiento, pruebas y costos trazables. No se presume que una tecnología específica —incluido un bus de eventos o Kafka— haya sido definida por Ancoa.

## Alcance de la Etapa 1 y de la Etapa 2, con criterio de asignación

El cronograma contractual de 56 meses se mantiene: Etapa 1, desarrollo en meses 1–15 y producción desde el mes 16; Etapa 2, desarrollo en meses 13–20 y producción desde el mes 21; operación hasta el mes 56. El detalle de servicios, requerimientos y entregables por etapa debe preservar estas fechas y la migración de crédito antes del fin de soporte informado para 2029.

La asignación se gobierna por dependencias, riesgo, hitos externos y capacidad de adopción del CLIENTE. La continuidad selectiva del Escenario A es la referencia; cualquier ampliación al Escenario B requiere justificar brechas comprobadas y plan de transición. El trabajo se organizará de forma ágil e incremental: ciclos cortos, backlog priorizado, validación frecuente con actores de Ancoa, despliegue gradual con coexistencia y reversa, y revisión de prioridades cuando cambien el soporte o las interfaces de las plataformas. La metodología adapta la ejecución a un sistema que permanece en operación; no amplía el alcance funcional acordado.

### Criterios de asignación

La asignación se realiza con estos criterios: (1) precedencia de capacidades y dependencias técnicas demostradas; (2) separación Retail–Emisor antes de habilitar cruces; (3) migración del crédito de acuerdo con el fin de soporte de 2029; (4) prioridad para los flujos que sostienen existencia, precio y entrega; y (5) capacidad de Ancoa para absorber cambios mientras las tiendas y plataformas siguen operando. El mapa de las catorce interfaces y las pruebas de las decisiones condicionadas alimentan la secuencia. No se fija un producto de integración ni se asignan conexiones por inferencia.

### Habilitación temprana de la migración financiera

La plataforma de crédito debe reemplazarse y la cartera migrarse antes del fin de soporte anunciado para 2029. Por el volumen informado —620.000 clientes con saldo— el trabajo de migración no se posterga íntegramente hasta la etapa final: la Etapa 1 debe habilitar el inventario de datos, las reglas de conciliación, los controles de la frontera y las pruebas de migración que se necesitan antes de ejecutar cortes. La migración y su cierre deben seguir las fechas contractuales y los hitos externos aplicables. El orden de olas, la coexistencia y las condiciones de corte se validan con Ancoa y con el Emisor.

### Ventanas y calendario operativo

**INCOMPLETO TEMPORALMENTE.** Alinear el plan de liberaciones con el calendario de eventos comerciales, las ventanas de congelamiento que Ancoa confirme y las fechas de evaluación de crédito. No se fijan fechas de adjudicación, Cyber ni días de congelamiento hasta contar con el calendario aprobado. Los ciclos ágiles incluyen planificación de releases y bloqueo de cambios productivos en las ventanas confirmadas.

### Fase de Operación

Se despliegan 36 meses continuos de operación y soporte de misión crítica (meses 21 a 56). La estrategia operativa incorpora soporte 24x7x365 para el canal digital y los componentes financieros, y atención en horario comercial extendido (09:00 a 23:00) para las sucursales y operaciones físicas. Se contempla cobertura reforzada documentada para los tres eventos anuales masivos y soporte especializado presencial distribuido en las 11 regiones de operación.

## Exclusiones explícitas, supuestos y restricciones

### Exclusiones explícitas

Tabla 3.4: Exclusiones y límites del trabajo comprometido.

| Elemento | Delimitación |
| :--- | :--- |
| Reemplazo del ERP y de la emisión tributaria | Excluidos: Ancoa mantiene el ERP como emisor tributario único. La integración y conciliación necesarias sí forman parte del alcance. |
| Reemplazo general de las plataformas existentes | Excluido: las sustituciones se limitan a la plataforma de crédito y a decisiones condicionadas justificadas por evidencia. |
| Sustitución del marketplace y del WMS principal | Excluida: ambos se mantienen; las integraciones requeridas están incluidas. |
| Plataforma de vendedores propia | Excluida: se integra la solución de marketplace existente con los servicios de Ancoa. |
| WMS para Concepción | No se considera implantación comprometida en el alcance base; se evalúa y costea separadamente antes de decidir. |
| Compra de hardware y dispositivos de tienda | La adquisición de equipos no se presume incluida. La solución debe especificar los requerimientos y demostrar la capacidad offline. Cualquier compra se asignará según el alcance contractual aprobado. |
| Sustitución de proveedores de transporte o flotas | Excluida: se integran hitos e incidencias de proveedores vigentes en las interacciones requeridas. |
| Plataforma número nueve no identificada | No se define reemplazo ni integración hasta identificarla; su levantamiento sí está incluido. |

### Supuestos

Tabla 3.5: Supuestos y validaciones pendientes.

| ID | Supuesto o dato sujeto a confirmación | Efecto sobre el alcance | Validación prevista |
| :--- | :--- | :--- | :--- |
| S-01 | El inventario funcional disponible identifica ocho de las nueve plataformas que Ancoa declara. | Impide cerrar el mapa de dependencias y el destino de todos los sistemas. | Identificación temprana de plataforma, proveedor, función e interfaces. |
| S-02 | Las relaciones funcionales del diagrama de topología no acreditan interfaces actuales ni su cardinalidad. | Evita dimensionar esfuerzo sobre flechas como si fueran interfaces confirmadas. | Levantamiento de los catorce contratos de interfaz con extremos, datos, frecuencia y mecanismo. |
| S-03 | No está comprobada la capacidad offline actual del POS. | Condiciona si se mantiene, integra, adquiere o reemplaza el software POS, no la obligación de entregar la capacidad de continuidad requerida. | Prueba de desconexión, operación y reconciliación con usuarios de tienda. |
| S-04 | La permanencia de comercio electrónico y fidelización depende de que superen pruebas de capacidad y segregación, respectivamente. | Una sustitución solo se incluye si la brecha es atribuible a la plataforma y no se resuelve con datos o integración. | Pruebas de extremo a extremo y de controles de datos. |
| S-05 | La continuidad de crédito desconectado puede depender de cupos preaprobados y controles del Emisor. | No se presume originación nueva ni consumo offline hasta demostrar factibilidad y aprobación de cumplimiento. | Prueba y validación formal por el Emisor. |
| S-06 | La extensión de WMS a Concepción no está decidida. | Se mantiene fuera de la implantación base hasta disponer de evaluación y costo. | Análisis separado de procesos, alcance, costo y dependencias. |

### Restricciones

Restricciones de Continuidad y Operación Física (Edge Computing):

* La solución debe garantizar la autonomía del componente local y la continuidad de venta y cobro por los períodos definidos en los RNF. Esto no implica originar nuevos créditos sin enlace; el uso de un cupo previamente aprobado queda condicionado a la factibilidad y aprobación del Emisor.

* Restablecimiento de red y sincronización bidireccional forzosa en un máximo de 30 minutos sin pérdida de DTEs ni solapamiento de stock.

* Tolerancia nula a la indisponibilidad de terminales por rotación; la sesión cajero-vendedor emplea rotación de credenciales (hot-swapping).

* Cinco ventanas de congelamiento de infraestructura inamovibles, implementadas como barreras automatizadas de CI/CD para bloquear despliegues durante peaks comerciales.

Restricciones legales y protección de datos:

* Separación lógica entre Retail y el Emisor, con autorización explícita de los cruces definidos, registro de cada cruce y auditoría de operaciones permitidas y denegadas.

* Inmutabilidad probatoria de largo plazo: los registros precontractuales, el timestamp de entrega de información y el consentimiento de repactación se archivan en almacenamiento frío por el plazo de vigencia de la deuda más 6 años.

* Derivación de garantías prohibida por diseño. El flujo comercial de postventa absorbe financieramente las contingencias en primera línea, delegando la liquidación B2B al plano administrativo trasero.

Restricciones contractuales del proyecto:

* Plazo contractual de 56 meses y adopción obligatoria del despliegue en nube híbrida.

* Integración auditable de cinco modelos de innovación valorizados económicamente, incluyendo algoritmos de aprendizaje automático controlados perimetralmente para no comprometer datos sensibles.

* No incorporar precios unitarios, tarifas ni cálculos financieros en esta sección técnica.

## Catálogo de requerimientos funcionales core

El Anexo Técnico X consolida 223 requerimientos funcionales atomizados. Esta sección expone estrictamente el subconjunto core: aquellos requerimientos cuya omisión vulnera las restricciones innegociables del CLIENTE o bloquea la habilitación de dependencias arquitectónicas estructurales.

> **Aclaración de trazabilidad:** los códigos M-01–M-24 agrupan requerimientos y no representan servicios desplegables. El cruce individual de cada RF/RNF con los servicios R/F/X se completará en la matriz T-12; no se infiere equivalencia entre un módulo y un servicio.

* Criterio de selección: Un requerimiento integra el núcleo core si (1) implementa de forma directa una de las quince restricciones no negociables, (2) materializa una decisión estructural de arquitectura, o (3) constituye un prerrequisito técnico bloqueante para el resto de su módulo.

* Prioridad: Se aplica el marco MoSCoW. La totalidad del catálogo core está clasificado como M (Obligatorio/Must), condicionando el éxito de los pasos a producción.

### Gobernanza de datos y frontera regulatoria

Tabla 3.6:** Requerimientos funcionales core de gobernanza de datos y frontera regulatoria.

**ID:** RF-166. **Requerimiento:** Bloquear todo intento de cruce de información que no corresponda a una interfaz declarada en el inventario de flujos autorizados.. **Agrupación de requisitos:** M-21. **Etapa:** 1. **Trazabilidad:** Restricción N°1.

**ID:** RF-165. **Requerimiento:** Registrar cada cruce ejecutado entre ámbitos indicando dato, finalidad, base de licitud, autorización nominada e instante.. **Agrupación de requisitos:** M-21. **Etapa:** 1.

**ID:** RF-170. **Requerimiento:** Excluir del catálogo de atributos disponibles en el motor de campañas todo atributo de origen financiero.. **Agrupación de requisitos:** M-21. **Etapa:** 1. **Trazabilidad:** Restricción N°1.

**ID:** RF-174. **Requerimiento:** Resolver la correspondencia entre identificadores exclusivamente a través de la tabla custodiada en zona neutral, con acceso nominado y registrado.. **Agrupación de requisitos:** M-22. **Etapa:** 1.

### Disponibilidad e inventario

Tabla 3.7:** Requerimientos funcionales core de disponibilidad e inventario.

**ID:** RF-127. **Requerimiento:** Calcular la existencia disponible para vender restando de la existencia registrada las reservas vigentes, el comprometido no despachado y el colchón de confianza.. **Agrupación de requisitos:** M-01. **Etapa:** 1.

**ID:** RF-128. **Requerimiento:** Determinar el valor del colchón de confianza en función de la categoría del artículo.. **Agrupación de requisitos:** M-01. **Etapa:** 1.

**ID:** RF-157. **Requerimiento:** Impedir que cualquier canal de venta consuma el saldo bruto de inventario para publicar o comprometer existencia.. **Agrupación de requisitos:** M-01. **Etapa:** 1.

**ID:** RF-161. **Requerimiento:** Mostrar al vendedor de piso el porcentaje de error probable junto a la disponibilidad publicada.. **Agrupación de requisitos:** M-01. **Etapa:** 1.

**ID:** RF-137. **Requerimiento:** Calcular la exactitud de inventario resultante por categoría.. **Agrupación de requisitos:** M-02. **Etapa:** 1.

**ID:** RF-139. **Requerimiento:** Impedir el cierre de un ajuste de inventario que no tenga asignado un componente de merma.. **Agrupación de requisitos:** M-02. **Etapa:** 1.

**ID:** RF-143. **Requerimiento:** Impedir la publicación de una referencia en el canal digital mientras no cuente con los atributos obligatorios completos.. **Agrupación de requisitos:** M-03. **Etapa:** 1. **Trazabilidad:** Vacío V-03.

### Precio y evidencia fiscal

Tabla 3.8:** Requerimientos funcionales core de precio y evidencia fiscal.

**ID:** RF-028. **Requerimiento:** Impedir la venta de la referencia al precio nuevo mientras su punto de exhibición no confirme la actualización física.. **Agrupación de requisitos:** M-06. **Etapa:** 1. **Trazabilidad:** Restricción N°4.

**ID:** RF-023. **Requerimiento:** Cobrar el menor de ambos precios para el consumidor ante discrepancia detectada en línea de caja.. **Agrupación de requisitos:** M-06. **Etapa:** 1. **Trazabilidad:** Restricción N°4.

**ID:** RF-020. **Requerimiento:** Registrar la identidad individual del ejecutor del cambio de etiqueta.. **Agrupación de requisitos:** M-06. **Etapa:** 1.

**ID:** RF-021. **Requerimiento:** Recuperar el precio publicado de una referencia para una fecha, hora y canal determinados.. **Agrupación de requisitos:** M-07. **Etapa:** 1. **Trazabilidad:** Restricción N°4.

### Pedido, cumplimiento y comisión

Tabla 3.9:** Requerimientos funcionales core de pedido, cumplimiento y comisión.

**ID:** RF-043. **Requerimiento:** Preautorizar el medio de pago al aceptar el pedido, sin capturar el cobro.. **Agrupación de requisitos:** M-09. **Etapa:** 1.

**ID:** RF-045. **Requerimiento:** Capturar el cobro únicamente al registrarse el evento de confirmación de la preparación física.. **Agrupación de requisitos:** M-09. **Etapa:** 1.

**ID:** RF-046. **Requerimiento:** Determinar automáticamente la alternativa de resolución aplicable según el motor de reglas ante quiebres de inventario.. **Agrupación de requisitos:** M-09. **Etapa:** 1.

**ID:** RF-051. **Requerimiento:** Notificar al cliente el cambio de estado de su pedido antes de efectuar cualquier cobro definitivo.. **Agrupación de requisitos:** M-11. **Etapa:** 1.

**ID:** RF-052. **Requerimiento:** Permitir a todos los actores consultar el estado del pedido desde una única fuente de verdad.. **Agrupación de requisitos:** M-09. **Etapa:** 1.

**ID:** RF-077. **Requerimiento:** Seleccionar como punto de despacho aquel de menor costo total de servir.. **Agrupación de requisitos:** M-09. **Etapa:** 1.

**ID:** RF-055. **Requerimiento:** Condicionar la transmisión de la base de comisión al movimiento real de inventario verificado en bodega.. **Agrupación de requisitos:** M-10. **Etapa:** 1.

### Operación de tienda y contingencia

Tabla 3.10:** Requerimientos funcionales core de operación de tienda y contingencia.

**ID:** RF-084. **Requerimiento:** Permitir al cajero cobrar la venta en modo desconectado.. **Agrupación de requisitos:** M-08. **Etapa:** 1. **Trazabilidad:** Restricción N°5.

**ID:** RF-086. **Requerimiento:** Emitir el documento de venta en contingencia utilizando folios previamente asignados por el ERP.. **Agrupación de requisitos:** M-08. **Etapa:** 1. **Trazabilidad:** Restricciones N°5 y N°6 Vacío V-01.

**ID:** RF-100. **Requerimiento:** Enrutar la emisión de todo documento tributario hacia el sistema de gestión empresarial como único emisor.. **Agrupación de requisitos:** M-08. **Etapa:** 1. **Trazabilidad:** Restricción N°6 X-01.

**ID:** RF-089. **Requerimiento:** Permitir el uso desconectado de un cupo previamente aprobado solo si el Emisor valida factibilidad, vigencia y controles; impedir la apertura de tarjetas nuevas sin enlace.. **Agrupación de requisitos:** M-17. **Etapa:** 1 y 2. **Trazabilidad:** S-05.

**ID:** RF-092. **Requerimiento:** Impedir la apertura de una tarjeta nueva en modo desconectado.. **Agrupación de requisitos:** M-17. **Etapa:** 2. **Trazabilidad:** Restricción N°3.

**ID:** RF-095. **Requerimiento:** Reconciliar hacia los sistemas centrales la totalidad de las ventas registradas en modo desconectado.. **Agrupación de requisitos:** M-08. **Etapa:** 1.

**ID:** RF-097. **Requerimiento:** Procesar la reconciliación de forma idempotente, impidiendo la duplicación de ventas o documentos.. **Agrupación de requisitos:** M-08. **Etapa:** 1.

### Post-venta, garantía legal y marketplace

Tabla 3.11:** Requerimientos funcionales core de postventa, garantía legal y marketplace.

**ID:** RF-188. **Requerimiento:** Impedir que el flujo de atención exija la derivación del consumidor al fabricante, al servicio técnico o al vendedor externo.. **Agrupación de requisitos:** M-13. **Etapa:** 1. **Trazabilidad:** Restricción N°7.

**ID:** RF-198. **Requerimiento:** Impedir que el estado de la recuperación contra el tercero condicione el cierre de la resolución al consumidor.. **Agrupación de requisitos:** M-14. **Etapa:** 1.

**ID:** RF-190. **Requerimiento:** Impedir el reingreso de una unidad devuelta al inventario disponible mientras no exista decisión de aptitud registrada.. **Agrupación de requisitos:** M-13. **Etapa:** 1.

**ID:** RF-106. **Requerimiento:** Notificar al vendedor de marketplace la recepción de la devolución en el instante en que se registra.. **Agrupación de requisitos:** M-14. **Etapa:** 2.

**ID:** RF-119. **Requerimiento:** Registrar el acuse de conocimiento de las reglas de evaluación por parte de cada vendedor externo.. **Agrupación de requisitos:** M-12. **Etapa:** 2.

**ID:** RF-124. **Requerimiento:** Despublicar automáticamente la oferta cuyo stock declarado haya superado el plazo de vigencia sin actualización.. **Agrupación de requisitos:** M-12. **Etapa:** 2.

### Crédito, consentimiento y migración

Tabla 3.12:** Requerimientos funcionales core de crédito, consentimiento y migración.

**ID:** RF-199. **Requerimiento:** Exigir la entrega completa de la información precontractual antes de habilitar la evaluación de la solicitud.. **Agrupación de requisitos:** M-15. **Etapa:** 2. **Trazabilidad:** Restricción N°3 .

**ID:** RF-206. **Requerimiento:** Impedir el registro de la aceptación del crédito mientras no exista acreditación de entrega previa de la información precontractual.. **Agrupación de requisitos:** M-16. **Etapa:** 2. **Trazabilidad:** Restricción N°3 .

**ID:** RF-208. **Requerimiento:** Impedir el registro de una modificación de condiciones del crédito que no posea evidencia de consentimiento asociada.. **Agrupación de requisitos:** M-16. **Etapa:** 2. **Trazabilidad:** Restricción N°2 .

**ID:** RF-210. **Requerimiento:** Restaurar desde archivo frío los antecedentes de una operación de crédito de cualquier cohorte dentro del plazo de retención.. **Agrupación de requisitos:** M-16. **Etapa:** 2.

**ID:** RF-220. **Requerimiento:** Impedir la originación de una operación cuya tasa supere la Tasa Máxima Convencional vigente.. **Agrupación de requisitos:** M-15. **Etapa:** 2.

**ID:** RF-213. **Requerimiento:** Impedir la ejecución de una gestión de cobranza fuera de los límites normativos de horario y de medio.. **Agrupación de requisitos:** M-18. **Etapa:** 2.

**ID:** RF-216. **Requerimiento:** Generar el reporte de conciliación diaria de saldos durante todo el proceso de migración por olas de coexistencia.. **Agrupación de requisitos:** M-19. **Etapa:** 1 y 2. **Trazabilidad:** Restricción N°8.

### Accesos, evento anual y ventanas de congelamiento

Tabla 3.13:** Requerimientos funcionales core de accesos, eventos anuales y congelamiento.

**ID:** RF-004. **Requerimiento:** Impedir el acceso mediante credencial compartida en líneas de caja o terminales de piso.. **Agrupación de requisitos:** M-23. **Etapa:** 1. **Trazabilidad:** Restricción N°11.

**ID:** RF-013. **Requerimiento:** Revocar la totalidad de los accesos y credenciales del trabajador a partir del término efectivo de su vínculo.. **Agrupación de requisitos:** M-23. **Etapa:** 1.

**ID:** RF-007. **Requerimiento:** Impedir la ejecución de la función de originación a un usuario sin capacitación normativa acreditada vigente.. **Agrupación de requisitos:** M-23. **Etapa:** 2.

**ID:** RF-163. **Requerimiento:** Permitir exclusivamente al rol facultado suspender manualmente la publicación comercial de una categoría.. **Agrupación de requisitos:** M-24. **Etapa:** 1.

**ID:** RF-185. **Requerimiento:** Bloquear por diseño la ejecución de despliegues en producción durante las ventanas de congelamiento.. **Agrupación de requisitos:** M-24. **Etapa:** 1. **Trazabilidad:** Restricción N°9.

## Catálogo de requerimientos no funcionales core

El Anexo consolida 75 requerimientos no funcionales (RNF) asociados a desempeño, resiliencia y seguridad. Esta sección expone exclusivamente aquellos **con valor numérico verificable**, los cuales gobiernan la certificación y paso a producción de cada etapa. Los valores rotulados como supuesto serán recalibrados empíricamente durante el levantamiento inicial.

### Desempeño y tiempo de respuesta

Tabla 3.14:** Requerimientos no funcionales core de desempeño y tiempo de respuesta.

**ID:** RNF-16. **Requerimiento:** Consulta de disponibilidad en la ficha de producto del canal digital.. **Umbral:** ≤ 400 ms. **Método de verificación:** Prueba de carga con perfil del evento anual y monitoreo en producción..

**ID:** RNF-21. **Requerimiento:** Consulta de disponibilidad desde terminal compartida del piso de venta.. **Umbral:** ≤ 2 s. **Método de verificación:** Prueba en terreno sobre las 640 terminales, en tienda insignia y de calle..

**ID:** RNF-17. **Requerimiento:** Confirmación de un pedido durante el evento anual.. **Umbral:** ≤ 3 s. **Método de verificación:** Prueba de carga con el peak declarado..

**ID:** RNF-18. **Requerimiento:** Venta completa en caja con medio de pago externo.. **Umbral:** ≤ 25 s. **Método de verificación:** Medición instrumentada en peak de diciembre..

**ID:** RNF-06. **Requerimiento:** Evaluación de una solicitud de crédito en el punto de venta físico.. **Umbral:** ≤ 8 s (base actual: 40s a 3m). **Método de verificación:** Medición extremo a extremo en mesón y caja..

**ID:** RNF-19. **Requerimiento:** Propagación de un cambio de precio a las 380 líneas de caja y al canal digital.. **Umbral:** ≤ 5 min. **Método de verificación:** Prueba con carga de campaña de 400.000 cambios en un día..

**ID:** RNF-20. **Requerimiento:** Registro de una devolución en el mesón de atención.. **Umbral:** ≤ 60 s. **Método de verificación:** Medición instrumentada con muestreo por tienda..

**ID:** RNF-05. **Requerimiento:** Desfase entre el cambio real de estado de un pedido y su reflejo omnicanal.. **Umbral:** Umbral declarado (\<= 30 s). **Método de verificación:** Auditoría cruzada de estado entre los cuatro canales..

### Capacidad

Tabla 3.15:** Requerimientos no funcionales core de capacidad operativa.

**ID:** RNF-22. **Requerimiento:** Soporte del peak digital del evento anual sin degradar los umbrales de desempeño.. **Umbral:** 104.000 pedidos en 3 días (proyección 150.000). **Método de verificación:** Prueba de carga al 120 % del peak proyectado..

**ID:** RNF-23. **Requerimiento:** Soporte del peak presencial de la campaña de noviembre y diciembre.. **Umbral:** Carga concurrente sobre 380 líneas de caja. **Método de verificación:** Prueba de carga presencial sostenida..

### Seguridad y frontera de datos

Tabla 3.16:** Requerimientos no funcionales core de seguridad, resiliencia y disponibilidad.

**ID:** RNF-28. **Requerimiento:** Operación desconectada autónoma del componente on-premise.. **Umbral:** ≥ 24 h continuas. **Método de verificación:** Prueba de desconexión prolongada del nodo físico..

**ID:** RNF-24. **Requerimiento:** Operación comercial de tienda sin enlace externo (venta y cobro efectivos).. **Umbral:** ≥ 8 h continuas. **Método de verificación:** Corte real del enlace en tienda piloto, en horario comercial..

**ID:** RNF-25. **Requerimiento:** Operación del centro de distribución principal sin enlace externo.. **Umbral:** ≥ 4 h continuas. **Método de verificación:** Prueba de desconexión programada..

**ID:** RNF-26. **Requerimiento:** Sincronización tras la reconexión de sucursal.. **Umbral:** ≤ 30 min (tras 8 h de desconexión). **Método de verificación:** Prueba de reconexión cronometrada..

**ID:** RNF-27. **Requerimiento:** Integridad de la sincronización.. **Umbral:** 0 ventas y 0 DTE perdidos/duplicados. **Método de verificación:** Cuadratura del universo transaccional tras la contingencia..

**ID:** RNF-32. **Requerimiento:** Objetivos de recuperación ante desastre.. **Umbral:** RTO ≤ 4 h RPO ≤ 15 min. **Método de verificación:** Ejercicio semestral de conmutación real..

**ID:** RNF-30. **Requerimiento:** Disponibilidad del canal digital.. **Umbral:** 24x7x365 (≥ 99,9 %). **Método de verificación:** Monitoreo mensual contra el SLA contractual..

**ID:** RNF-31. **Requerimiento:** Disponibilidad de servicios financieros (pagos, estados de cuenta, bloqueos).. **Umbral:** 24x7x365 (≥ 99,9 %). **Método de verificación:** Monitoreo segregado reportado a la filial emisora..

### Retención, trazabilidad y migración

Tabla 3.17:** Requerimientos no funcionales core de retención, trazabilidad y migración.

**ID:** RNF-42. **Requerimiento:** Conservación de los antecedentes e historial del crédito.. **Umbral:** Plazo del crédito \+ 6 años. **Método de verificación:** Pruebas de recuperación de archivo frío..

**ID:** RNF-57. **Requerimiento:** Recuperación de la evidencia de consentimiento de operaciones históricas.. **Umbral:** ≤ 5 min. **Método de verificación:** Recuperación por muestreo censal auditado..

**ID:** RNF-44. **Requerimiento:** Retención de la trazabilidad del precio publicado por canal.. **Umbral:** 3 años. **Método de verificación:** Auditoría de política de ciclo de vida de datos..

**ID:** RNF-58. **Requerimiento:** Recuperación del precio publicado en fecha, hora y canal arbitrarios.. **Umbral:** ≤ 1 min (sobre ventana de 3 años). **Método de verificación:** Consultas índice sobre el histórico inmutable..

**ID:** RNF-10. **Requerimiento:** Divergencia de saldos durante migración de cartera financiera.. **Umbral:** 0 divergencias no conciliadas. **Método de verificación:** Freno automático (circuit breaker) ante excepciones..

### Precisión sobre Continuidad y Métricas de Negocio

El diseño distingue la autonomía de infraestructura de la continuidad comercial. RNF-28 define autonomía para el componente *on-premise* y RNF-24 define ocho horas de venta y cobro en tienda. Estas condiciones no autorizan por sí mismas la originación ni el consumo de crédito sin enlace; cualquier excepción con cupo preaprobado queda condicionada a las pruebas y aprobación del Emisor.

Asimismo, las metas de exactitud de inventario o tasa de cancelación no se tabulan como requerimientos no funcionales aislados, ya que su éxito depende de la conjunción entre el software entregado y la ejecución operativa del CLIENTE (conteo físico en sala, clasificación de mermas). Su cumplimiento se gestiona mediante los Criterios de Aceptación y Objetivos de Negocio del proyecto global.

## Criterios de aceptación del alcance comprometido

La aceptación no se declara por la entrega de un artefacto sino por la verificación de un hecho observable. Un entregable producido, documentado y presentado en plazo no se da por recibido si el comportamiento que debía habilitar no se demuestra con evidencia objetiva.

El modelo opera en tres niveles encadenados y no sustituibles entre sí: aceptación por entregable, que verifica conformidad técnica; aceptación por marcha blanca, que verifica comportamiento en operación real; y aceptación por resultado de negocio, que verifica que la plataforma efectivamente movió los indicadores que motivaron la licitación. Superar el primer nivel no anticipa el segundo, y superar los dos primeros no exime del tercero.

### Nivel 1: aceptación por entregable

Cada entregable se somete a revisión formal de la Contraparte Técnica y se acepta mediante acta suscrita, previa concurrencia de cuatro condiciones: el artefacto conforme a lo especificado; la evidencia objetiva de su verificación, no la declaración de haberla ejecutado; la trazabilidad explícita hacia los requerimientos del catálogo que satisface, incluyendo la agrupación lógica de requerimientos y la etapa a que pertenece; y el cierre documentado de las observaciones formuladas en revisiones previas.

La aceptación de un entregable que dependa de otro no procede mientras el precedente permanezca observado. El plan de trabajo debe mantener y evidenciar estas dependencias.

### Nivel 2: aceptación de la marcha blanca

El cierre de cada marcha blanca —meses 13 a 15 para la Etapa 1 y meses 19 y 20 para la Etapa 2— exige el cumplimiento copulativo de las seis condiciones siguientes. La ausencia de cualquiera de ellas impide el paso a producción.

Tabla 3.18:** Condiciones obligatorias para el cierre y aceptación de la marcha blanca.

**N°:** **1**. **Condición de cierre:** Ningún incidente abierto de severidad crítica o alta atribuible a la solución.. **Verificación:** Registro de incidentes con clasificación acordada y trazabilidad de cierre..

**N°:** **2**. **Condición de cierre:** Volumen de operación real comprometido alcanzado y sostenido durante al menos las cuatro últimas semanas del período.. **Verificación:** Telemetría de producción contrastada con el perfil transaccional declarado..

**N°:** **3**. **Condición de cierre:** Indicadores de disponibilidad y de tiempo de respuesta cumplidos de forma sostenida en ese mismo lapso, no en mediciones aisladas.. **Verificación:** Medición continua contra los umbrales RNF aplicables que se aprueben para cada etapa..

**N°:** **4**. **Condición de cierre:** Conciliación sin diferencias no explicadas contra los registros del sistema vigente.. **Verificación:** Cuadratura de universos, ejecutada diariamente durante el período..

**N°:** **5**. **Condición de cierre:** Personal del CLIENTE capacitado y certificado en los procesos afectados, considerando el perfil de rotación declarado.. **Verificación:** Registro de capacitación con evaluación de competencia posterior..

**N°:** **6**. **Condición de cierre:** Mecanismo de reversión probado y operativo, con ensayo ejecutado en ambiente equivalente.. **Verificación:** Acta del ensayo de reversión, con tiempo efectivo medido..

Dos condiciones adicionales se aplican de forma específica a la Etapa 2 y responden a restricciones no negociables: la aceptación no procede sin el informe de auditoría independiente que acredite la separación de dominios sin hallazgos críticos abiertos, y no procede sin la conciliación diaria de saldos de la cartera cerrada sin divergencias pendientes.

### Nivel 3: aceptación por resultado de negocio

Los criterios de este nivel verifican las promesas y resultados que motivan el trabajo. Se miden sobre operación real, con la línea base declarada por la propia compañía, y se distinguen entre resultados sistémicos y compartidos, según la responsabilidad del software y la operación de Ancoa.

Tabla 3.19: Indicadores de resultado y umbrales por confirmar.

Los antecedentes siguientes son líneas base informadas en el material de trabajo. Los umbrales de aceptación que no constan como requisito cuantificado se mantienen pendientes; no constituyen compromisos aprobados por sí solos.

| Resultado | Línea base disponible | Umbral de aceptación | Responsabilidad |
| :--- | :--- | :--- | :--- |
| Exactitud de inventario | 12,4 % de discrepancia en conteos cíclicos. | **INCOMPLETO TEMPORALMENTE:** acordar método, universo y meta. | Compartida |
| Pedidos cancelados por falta de existencia | 1,9 % anual; 2,7 % en el evento citado. | **INCOMPLETO TEMPORALMENTE:** acordar meta y período de medición. | Compartida |
| Diferencia entre precio exhibido y cobrado | 11 % en fiscalización informada. | **INCOMPLETO TEMPORALMENTE:** acordar muestreo y meta. | Compartida |
| Cumplimiento de fecha de entrega | Línea base pendiente de confirmar con fuente y período. | **INCOMPLETO TEMPORALMENTE:** acordar métrica y meta. | Compartida |
| Evidencia de consentimiento y repactaciones | Se informan 1.240 repactaciones sin evidencia recuperable. | Cero operaciones sin evidencia exigible; definir período y prueba de recuperación. | Sistémica |
| Migración de cartera | 620.000 clientes con saldo; soporte anunciado hasta 2029. | 100 % migrado con cero divergencias no conciliadas antes del fin de soporte. | Sistémica |
| Cruces Retail–Emisor | Separación parcial; no se dispone de un registro completo de cruces. | Registrar y auditar los cruces autorizados; **INCOMPLETO TEMPORALMENTE:** fijar criterio de auditoría y aceptación. | Sistémica |
| Continuidad de venta y cobro sin enlace | Ancoa informa detención de operación durante pérdida de enlace. | Ocho horas continuas según el RNF aplicable, con reconciliación íntegra. | Sistémica |
| Evaluación de crédito en POS | Se informa un rango de 40 segundos a 3 minutos. | Aplicar el RNF-06 y validar el extremo a extremo con cumplimiento del Emisor. | Sistémica |

### Criterios de aceptación de naturaleza cualitativa

Los criterios cualitativos siguientes no admiten expresión numérica y se verifican por observación directa. Se adoptan como criterios de aceptación de pleno derecho y no como ilustración del propósito del proyecto.

Tabla 3.20:** Criterios de aceptación cualitativa y forma de verificación.

**Criterio:** Ningún consumidor es derivado al fabricante, al servicio técnico o al vendedor externo como condición para que se le atienda una garantía legal.. **Forma de verificación:** Programa de cliente oculto ejecutado en las 22 tiendas, con resultado cero derivaciones..

**Criterio:** Una clienta con un pedido en curso conoce su estado real sin necesidad de contactar reiteradamente a la compañía, y es informada antes de cualquier cobro definitivo.. **Forma de verificación:** Auditoría del estado único del pedido y de la trazabilidad de notificaciones, contrastada con el registro de contactos entrantes por ese pedido..

**Criterio:** Una jefatura de tienda puede demostrar qué proporción de su diferencia de inventario corresponde a error de registro y no a pérdida física.. **Forma de verificación:** Revisión del informe mensual de merma desagregada con una jefatura de tienda real, verificando que la explicación se sostiene con los datos del sistema..

**Criterio:** Un vendedor abre una tarjeta en menos tiempo que hoy sin que el cliente reciba menos información precontractual.. **Forma de verificación:** Medición comparada de tiempo de atención y auditoría censal de la constancia de entrega precontractual del mismo período..

### Reparto de responsabilidad y arbitraje del incumplimiento

Los resultados de exactitud de inventario, cancelaciones, precio y entrega dependen conjuntamente de la plataforma entregada y de la ejecución operativa del CLIENTE: la plataforma provee el algoritmo de disponibilidad, la ruta de recambio de etiquetas y el orquestador de pedidos, pero el conteo, el escaneo y la preparación física los ejecuta el personal de sala. El acta de aceptación de cada uno de estos indicadores aislará el componente atribuible al sistema del componente atribuible a la adopción, y su medición se ejecuta primero sobre un piloto acotado de categorías, de modo que la desviación se detecte sobre un universo controlado antes del escalamiento.

Ante el incumplimiento de un criterio, el procedimiento es escalonado y no discrecional. En el nivel de entregable, la observación suspende la aceptación y abre plazo de subsanación, sin que ello habilite el avance de los entregables dependientes. En el nivel de marcha blanca, el incumplimiento de cualquiera de las condiciones copulativas impide el paso a producción y desplaza el hito, con la salvedad de que ningún desplazamiento puede reubicar una puesta en producción dentro de una ventana de congelamiento. En el nivel de resultado de negocio, el incumplimiento activa un plan de remediación conjunto con causa atribuida, cuya ejecución se somete a los mismos criterios de verificación.

Ninguna aceptación puede otorgarse de forma tácita por el transcurso del plazo, ni durante una ventana de congelamiento, ni de manera condicional sujeta a compromisos posteriores.
