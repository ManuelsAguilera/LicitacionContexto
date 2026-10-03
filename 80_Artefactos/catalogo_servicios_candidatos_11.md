# Análisis de actores, capacidades y fronteras de solución

## Resultado ejecutivo
El análisis preliminar consolida los 24 elementos actuales en diez **fronteras funcionales candidatas** y un control transversal de correspondencia de identidad. El análisis compartido posterior amplía ese resultado a doce fronteras de trabajo —R-01…R-09 para Retail y F-01…F-03 para el Emisor— al incorporar explícitamente abastecimiento y fidelización. Los identificadores C se mantienen en este archivo como etapa intermedia y trazabilidad del razonamiento, no como el catálogo final ya aprobado.

La salida de esta etapa es un mapa del negocio y de sus límites. La decisión técnica posterior puede implementar una frontera mediante uno o varios módulos dentro de un monolito modular, un servicio desplegable o, si se demuestra autonomía suficiente, un microservicio. Los identificadores M-01…M-24 se conservan como alias de trazabilidad hasta aprobar la reasignación de requisitos. Ni el conteo preliminar de diez ni el consolidado de doce equivale automáticamente al número de microservicios. Esta es una propuesta de análisis, no una modificación ya aprobada de las asignaciones RF/SUP de T7-03.

## 1. Objetivos del documento

1. Identificar y normalizar los actores del caso, distinguiendo actor, grupo organizacional, rol, sistema externo y stakeholder sin participación directa.
2. Relacionar actores y roles con los procesos e interacciones en los que participan.
3. Identificar las **capacidades de negocio** necesarias, expresadas sin comprometer tecnología ni estructura de software.
4. Agrupar capacidades relacionadas en fronteras funcionales con lenguaje, reglas, datos y responsabilidades coherentes.
5. Separar las capacidades del negocio de canales, sistemas externos, controles transversales y componentes técnicos de plataforma.
6. Mantener la trazabilidad desde M-01…M-24 y desde los requisitos hacia las nuevas fronteras candidatas.
7. Establecer criterios para decidir posteriormente si cada frontera se implementa como módulos internos, servicio desplegable o uno o más microservicios.
8. Documentar las decisiones y dudas que requieren validación del mandante antes de fijar la arquitectura objetivo.

No es objetivo de este documento fijar todavía el número final de microservicios, diseñar sus APIs ni asignar infraestructura. Esas decisiones requieren arquitectura física, requisitos no funcionales, modelo operativo y validación de equipos y propietarios.

## 2. Vocabulario y niveles de análisis

En este documento, **capacidad** significa exclusivamente **capacidad de negocio**: aquello que la organización debe ser capaz de hacer para producir un resultado. No describe pantallas, componentes, APIs ni productos tecnológicos.

| Concepto | Nivel | Definición adoptada | Ejemplo |
| --- | --- | --- | --- |
| Actor | Negocio | Persona, grupo u organización que interactúa con un proceso o con la solución para alcanzar un objetivo. | Cliente, operación de tienda, transportista. |
| Rol | Negocio/contextual | Papel temporal o específico que un actor desempeña en un flujo. Un actor puede asumir varios roles. | Operación de tienda `[rol: preparador de pedido]`. |
| Capacidad de negocio | Negocio | Habilidad estable que el negocio necesita; expresa **qué** debe poder hacer, no cómo se implementa. | Gestionar disponibilidad comprometible. |
| Proceso o flujo | Negocio | Secuencia mediante la cual actores ejercen capacidades para producir un resultado. | Preparar y entregar un pedido digital. |
| Frontera funcional candidata | Análisis de dominio | Agrupación coherente de capacidades, reglas, conceptos y datos. Es la unidad C-01…C-10 usada en este análisis. | Pedido y cumplimiento omnicanal. |
| Módulo | Diseño de software | Unidad técnica cohesionada de código con una interfaz interna explícita. Puede compartir el mismo proceso de despliegue con otros módulos. | Módulo de reservas dentro de una aplicación modular. |
| Servicio desplegable | Arquitectura de aplicaciones | Unidad ejecutable que ofrece un contrato por red y puede tener ciclo de despliegue propio. Puede ser más amplio que un microservicio. | Servicio de pedidos desplegado como una aplicación independiente. |
| Microservicio | Arquitectura y operación | Servicio pequeño y autónomo, alineado con un contexto de dominio, desplegable independientemente, con contratos explícitos y control de sus datos/estado. | Microservicio de reservas, solo si cumple los criterios de autonomía. |
| Componente de plataforma | Tecnología | Infraestructura que transporta, protege u observa interacciones sin ser dueña de reglas del negocio. | API Gateway, bus de eventos, IAM, observabilidad. |
| Sistema externo | Ecosistema | Sistema existente o de un tercero que conserva una responsabilidad fuera de la solución propuesta. | ERP/DTE, WMS o plataforma marketplace vigente. |

### 2.1 Perfil formal de clasificación de actores

La clasificación de un actor no se expresa con una sola etiqueta. Se registra como un perfil compuesto por dimensiones independientes:

`naturaleza + relación con Ancoa + plano de participación + contexto de dominio + rol en el flujo`

Por tanto, **interno/externo** no es una alternativa a **negocio/técnico/control**. Un actor puede ser externo y técnico, interno y de negocio, o externo y de control. La combinación determina sus responsabilidades y restricciones.

#### Relación con Ancoa

| Relación | Definición | Implicaciones para alcance, acceso y responsabilidad |
| :--- | :--- | :--- |
| **Interno** | Persona, colectivo o unidad sometida a la autoridad organizacional de Ancoa. | Identidad corporativa; responsabilidad asignada; acceso por rol; segregación de funciones; capacitación; trazabilidad individual. Ser interno no concede acceso general ni elimina la separación entre Retail y Emisor. |
| **Externo** | Persona u organización fuera de la autoridad de Ancoa que participa por una relación comercial, contractual, legal o de servicio. | Contraparte o patrocinador interno; identidad acotada; mínimo privilegio; minimización de datos; vigencia y revocación del acceso; aislamiento entre organizaciones; trazabilidad contractual. Puede estar dentro del alcance funcional aunque esté fuera de la organización. |

#### Plano de participación

| Plano | Definición | Implicaciones para alcance, acceso y responsabilidad |
| :--- | :--- | :--- |
| **Negocio** | Persigue o entrega un resultado del negocio: comprar, vender, abastecer, transportar, atender, aprobar o administrar una operación. | Sus permisos derivan de una responsabilidad del proceso. Puede ser interno o externo y no obtiene privilegios técnicos por participar en el negocio. |
| **Técnico** | Opera, integra, soporta, protege u observa la plataforma, sin asumir por ello decisiones del negocio. | Cuentas privilegiadas separadas; mínimo privilegio; elevación temporal; registro de sesiones y cambios; acceso excepcional controlado. La capacidad administrativa no autoriza a modificar precios, saldos, crédito o aprobaciones. |
| **Control o fiscalización** | Comprueba cumplimiento, evidencia, riesgos o aplicación de reglas, sin ejecutar rutinariamente el proceso controlado. | Independencia; acceso preferentemente de lectura; evidencia inmutable; trazabilidad; ausencia de facultades operativas salvo mandato explícito. Puede ser interno —auditoría o cumplimiento— o externo —regulador o auditor—. |

#### Contexto de dominio

| Contexto | Qué comprende | Implicación principal |
| :--- | :--- | :--- |
| **Retail** | Venta, catálogo, inventario, pedidos, logística, marketplace, posventa y conciliación comercial. | Los permisos, datos y reglas quedan dentro del negocio retail. |
| **Emisor** | Originación, riesgo, consentimiento, administración de cartera, cobranza y cumplimiento financiero. | Constituye una frontera jurídica y de datos separada de Retail, incluso si una misma persona desempeña roles en ambos contextos. |
| **Transversal controlado** | Cruce entre Retail y Emisor por un mandato definido, por ejemplo auditoría o cumplimiento. | El cruce debe estar justificado, limitado y registrado; no fusiona los dominios. |
| **Transversal de plataforma** | Identidad, seguridad, observabilidad, integración y soporte técnico común. | La transversalidad técnica no autoriza a utilizar datos de negocio sin una necesidad operativa aprobada. |

#### Conceptos relacionados que no son otra etiqueta del mismo eje

- **Sistema actor:** sistema, dispositivo o servicio que intercambia información con la solución desde fuera de la frontera modelada. La externalidad es relativa a esa frontera: un ERP propiedad de Ancoa puede ser actor externo de la solución aunque sea un activo interno de la empresa. API Gateway y bus de eventos son componentes internos, no actores, mientras permanezcan dentro de la frontera.
- **Stakeholder:** parte interesada o afectada. Solo se modela además como actor cuando interactúa directamente con el proceso o sistema analizado.
- **Rol:** conducta o responsabilidad que un actor adopta en un flujo —iniciador, ejecutor, aprobador, proveedor, receptor, supervisor o fiscalizador—. No crea por sí mismo un actor nuevo.

#### Regla de uso en diagramas y especificaciones

Se usa el actor canónico como nombre estable y se agrega rol y contexto solo cuando sean necesarios para interpretar la interacción. Ejemplos: `Cliente [titular, Emisor]`, `Personal de venta y caja [cajero, Retail]` y `TI y soporte [administrador IAM, transversal de plataforma]`. Esto evita multiplicar actores por cargo, permiso o etapa del proceso.

La clasificación anterior mezclaba expresiones como «interno Retail», «actor técnico» y «control transversal» bajo una sola idea de tipo. Esas expresiones describen dimensiones diferentes. Desde esta versión, **tipo** responde únicamente a la naturaleza estable del actor y usa uno de cuatro valores cerrados:

| Tipo o naturaleza | Criterio de asignación | Ejemplo |
| --- | --- | --- |
| Persona | Individuo que interactúa por cuenta propia y cuya identidad individual importa para el flujo. | Cliente/consumidor. |
| Colectivo humano | Personas agrupadas porque comparten vínculo y comportamiento, sin afirmar que constituyen una unidad formal con autoridad propia. | Personal de venta y caja. |
| Unidad organizacional | Agrupación interna reconocible con responsabilidad, autoridad o rendición de cuentas. | Operación de tienda; Marketing y canales digitales. |
| Organización | Entidad autónoma con responsabilidad legal o contractual. En este caso se usa principalmente para terceros. | Vendedor marketplace; transportista; proveedor. |

Las demás características se registran en dimensiones independientes:

| Dimensión | Valores permitidos | Pregunta que responde |
| --- | --- | --- |
| Relación | Interna / Externa | ¿El actor pertenece a Ancoa? |
| Contexto | Retail / Emisor / Transversal controlado / Transversal de plataforma | ¿Dentro de qué ámbito actúa en este modelo? |
| Rol | Texto controlado por flujo | ¿Qué función desempeña en esta interacción concreta? |
| Participación | Inicia / ejecuta / aprueba / provee / recibe / fiscaliza | ¿Qué hace en el proceso analizado? |

Reglas de decisión:

1. Si el nombre describe una acción, función o permiso —por ejemplo, cajero, preparador, deudor o auditor— se registra como **rol**, no como tipo.
2. Si describe software, un dispositivo o infraestructura, se registra como **sistema o componente**, fuera de la matriz de actores de negocio.
3. Si solo resulta afectado o interesado, pero no interactúa con el proceso o la solución, se registra como **stakeholder**, no como actor del flujo.
4. Una misma entidad conserva su tipo aunque cambie de rol o contexto. El cliente sigue siendo `Persona` cuando actúa como comprador o deudor.

Aplicación a la matriz canónica:

| Actor canónico | Naturaleza | Relación | Contexto |
| --- | --- | --- | --- |
| Cliente / consumidor | Persona | Externa | Retail o Emisor según el flujo |
| Personal de venta y caja; jefaturas | Colectivo humano | Interna | Retail |
| Operación de tienda; operación de CD; prevención de pérdidas; comercial y compras; logística; marketing; administración y finanzas; atención retail | Unidad organizacional | Interna | Retail |
| Negocio financiero / Emisor | Unidad organizacional | Interna | Emisor |
| Control interno, cumplimiento y auditoría | Unidad organizacional | Interna | Transversal controlado |
| TI y soporte | Unidad organizacional | Interna | Transversal de plataforma |
| Vendedor marketplace; transportista; proveedor de mercadería; autoridad reguladora/auditor externo | Organización | Externa | Retail o Emisor según competencia |
| Repositor externo de proveedor | Colectivo humano | Externa | Retail; patrocinado por el proveedor |

Este perfil adopta de UML e IIBA que un actor desempeña un rol al interactuar con la solución, y de arquitectura empresarial la posibilidad de modelar personas, grupos/unidades y organizaciones. Los cuatro tipos concretos son una convención explícita del proyecto para evitar clasificaciones arbitrarias; no se presentan como una enumeración literal impuesta por un único estándar.

La relación entre estos niveles es:

> actores y roles participan en procesos → los procesos ejercen capacidades de negocio → las capacidades se agrupan en fronteras funcionales → las fronteras se implementan con módulos → los módulos se empaquetan en una o más unidades desplegables → una unidad es microservicio solo cuando demuestra autonomía técnica y operativa.

Un módulo, por tanto, **no se convierte automáticamente en servicio**. Puede permanecer como módulo interno. Si su responsabilidad necesita desplegarse, escalarse, protegerse, evolucionar y operarse de manera independiente, puede extraerse conservando un contrato explícito y pasar a ser un servicio. Se considerará microservicio únicamente si además mantiene bajo acoplamiento, propiedad clara de datos/estado, aislamiento de fallas y un equipo capaz de operarlo.

## 3. Criterio para formar fronteras funcionales

Una frontera combina capacidades cuando forman un mismo ciclo y lenguaje de negocio, sus actores y reglas evolucionan juntos y requieren consistencia estrecha. Se mantiene separada cuando existe un modelo o ciclo de vida distinto, una frontera de datos o cumplimiento, o una responsabilidad con propietario claramente diferente.

La separación retail–emisor financiero es obligatoria en todo nivel. Una persona común o una experiencia de canal compartida no autoriza combinar datos, reglas, almacenes ni permisos de ambos negocios.

### 3.1 Puerta de decisión técnica posterior

La implementación parte, por defecto, con límites modulares claros. Una frontera o parte de ella justifica un microservicio cuando existe evidencia suficiente de varias de estas condiciones:

- necesita despliegue y evolución independientes;
- tiene propietario de negocio y equipo operativo definidos;
- controla su propio modelo y estado sin escribir directamente en datos ajenos;
- requiere escalamiento, disponibilidad, seguridad o aislamiento de fallas diferentes;
- puede ofrecer contratos estables sin comunicación excesivamente conversacional;
- acepta y resuelve la consistencia distribuida, reintentos, duplicados y fallas parciales;
- el beneficio de autonomía supera el costo adicional de operación, observabilidad y soporte.

Debe permanecer como módulo interno cuando comparte transacciones y cambios frecuentes con otros módulos, no tiene propietario autónomo, requeriría una base compartida o produciría muchas llamadas de ida y vuelta. Por ello, C-01…C-10 son candidatos para evaluar, no un compromiso de diez microservicios.

## 4. Catálogo preliminar: 10 fronteras funcionales y 1 control transversal

### C-01 · Catálogo comercial y gestión de precios
**Alias:** M-03, M-05, M-06 y M-07 solo si M-07 significa evidencia/historial de precio.
**Responsabilidad:** datos comerciales del artículo necesarios para ofrecerlo; reglas y vigencias de precio/promoción; distribución del precio y estado del recambio de etiqueta; consulta auditable del precio publicado por canal cuando la trazabilidad sea responsabilidad del dominio comercial.
**Actores:** comercial, compras/categorías, gestor de precios, reposición y jefatura; POS, canal digital y marketplace consumen la oferta.
**Límite:** los adaptadores EDI son integración de plataforma, no una función de negocio. M-07 aparece como “Trazabilidad EDI”, aunque se le atribuyen RF sobre historial de precios. Confirmar el significado antes de reasignarlo. Si el historial exige custodia, retención o disponibilidad operativa autónomas, se puede extraer posteriormente; no crear ese servicio anticipadamente.

### C-02 · Inventario y disponibilidad comprometible
**Alias:** M-01 + M-02.
**Responsabilidad:** conteos, ajustes autorizados, causas de diferencias, estado de existencias por nodo, reservas y cálculo ATP con confianza/colchón. Mantiene una única decisión de comprometer stock y evita que cada canal consulte inventario bruto por su cuenta.
**Actores:** reposición, bodega/CD, jefatura, prevención de pérdidas, logística y canales de venta; cliente y vendedor reciben la disponibilidad.
**Límite y coexistencia:** el sistema de gestión de almacenes del centro de distribución principal y el ERP/DTE deben mantenerse e integrarse. Donde exista WMS, este conserva la ejecución física interna del almacén y publica recepciones, movimientos y despachos; C-02 normaliza el inventario, administra reservas y decide la disponibilidad comprometible. Donde no exista WMS —hoy el centro de Concepción opera con planillas— la solución provee el registro operacional necesario o un adaptador aprobado, eliminando las planillas como sistema de registro. El ERP/DTE recibe los eventos requeridos y conserva la emisión tributaria. La autoridad exacta de cada dato se confirma en el levantamiento de integraciones, sin acceso directo entre bases. Fundamento: Caso 09, numerales 2.2, 4.3 y 5.1; RT-05.20 y RT-05.21.

### C-03 · Pedido y cumplimiento omnicanal
**Alias:** M-04 + M-09.
**Responsabilidad:** ciclo de vida del pedido; selección/asignación de nodo; instrucciones de preparación, retiro o despacho; cambios de estado, quiebres, reasignación y compensación.
**Actores:** cliente, canales, tienda, bodega/CD, logística, transportista y atención.
**Límite y patrón OMS:** C-03 es el *Order Management System* (OMS) lógico y la única autoridad sobre el ciclo y el estado del pedido. No es una pasarela por la que funcionen todos los servicios. Solicita reservas a C-02 y coordina tienda, WMS, transportistas y marketplace mediante APIs o eventos versionados, idempotentes y auditables; cada dominio conserva sus datos y reglas. Solo las decisiones del ciclo del pedido se orquestan en el OMS. Esta decisión debe propagarse a las vistas lógica, de integración, datos y despliegue de los subdocumentos 3, 4 y 5. Fundamento: Caso 09, numerales 9.4 y 15.1; RT-05.17, RT-05.20, RT-05.21 y RT-16.21.

### C-04 · Registro y conciliación de ventas
**Alias:** parte funcional de M-08.
**Responsabilidad:** registrar la venta confirmada y sus reversas; cuadrar los eventos capturados en tienda, incluidos los producidos durante desconexión, y su confirmación de documentos/impuestos.
**Actores:** cajero, vendedor, jefatura, cliente, finanzas retail y sistema autorizado de documentos tributarios.
**Límite:** POS es canal/aplicación de borde, no el servicio en sí. La interfaz POS puede conservar un componente local para continuidad, pero no debe abrir crédito nuevo offline. La emisión de DTE permanece con el sistema externo designado hasta resolver autoridad y transición.

### C-05 · Atribución de venta y comisiones
**Alias:** M-10.
**Responsabilidad:** reglas para atribuir una venta a vendedor, tienda, canal u origen, y cálculo o reversa de la base de comisión conforme a la política aprobada. No gestiona remuneraciones ni liquida sueldos.
**Actores:** vendedor, jefatura y Administración y finanzas como contraparte funcional asumida.
**Límite:** permanece separado de la captura POS porque la atribución cruza tienda y pedido omnicanal. Consume ventas asentadas y cumplimiento verificado, y entrega la base calculada al sistema empresarial existente, que mantiene remuneraciones. Se adopta como supuesto que Administración y finanzas valida la política y recibe la base de comisión; el mandante deberá confirmar la unidad responsable durante el levantamiento. Fundamento: Caso 09, dotación del numeral 2.4 y exclusión del numeral 11.2.

### C-06 · Gobierno e integración de vendedores marketplace
**Alias:** M-12 + M-14 en las responsabilidades de vendedor, conciliación B2B y recobro.
**Responsabilidad:** integrar la plataforma marketplace existente; sincronizar la habilitación y el estado de los vendedores; medir reglas y niveles de servicio conocidos por ellos; intercambiar estados de pedidos y devoluciones; y apoyar la conciliación, liquidación y recobro entre Ancoa y cada vendedor. «Alta» significa reflejar en la solución al vendedor ya habilitado por la plataforma vigente, no reemplazar su proceso contractual de incorporación.
**Actores:** vendedor marketplace, Marketing y canales digitales como administración marketplace, Administración y finanzas y Atención al cliente retail como consumidor de estados.
**Límite:** se mantiene la plataforma marketplace de 2022 y no se desarrolla la plataforma interna de los vendedores ni se opera su logística. C-06 integra, mide y gobierna; C-07 resuelve la atención y devolución frente al consumidor sin esperar la conciliación B2B. La notificación al vendedor y la evidencia de devolución llegan a C-06 después de la recepción. Fundamento: Caso 09, numerales 4.8, 5.1, 9.6 y 11.2; RT-05.23, RT-16.21 y RT-16.30.

### C-07 · Posventa, garantías y devoluciones
**Alias:** M-13 + los requisitos hoy asignados a M-14 que describan recepción, inspección, elegibilidad o resolución de una devolución del cliente.
**Responsabilidad:** administrar el caso de posventa después de la venta: recepción y evidencia física, cambios, retracto, garantía legal, decisión de aptitud y destino de la unidad, devolución y comunicación de la resolución al cliente.
**Actores:** cliente, atención, personal de tienda/mesón, inspector o bodega, cumplimiento retail y vendedor externo cuando proceda.
**Límite:** la obligación frente al cliente es independiente de la conciliación/recobro B2B. Publica a C-02 el resultado de aptitud para inventario y entrega evidencia de vendedor a C-06 cuando exista recuperación.

### C-08 · Originación y autorización de crédito
**Alias:** M-15 + M-17.
**Responsabilidad:** evaluación y originación en línea. La contingencia desconectada se limita, como opción condicionada, al uso de un cupo previamente aprobado y vigente almacenado localmente, con topes, caducidad, marca de contingencia y conciliación posterior; no forma parte del compromiso firme hasta superar la prueba de factibilidad con la plataforma financiera vigente.
**Actores:** cliente/deudor, ejecutivo financiero, vendedor expresamente habilitado, riesgo y operación del emisor.
**Límite:** pertenece al Emisor, incluso cuando el trámite comienza en POS. Sin conectividad no se evalúa una nueva línea ni se abre una tarjeta. RF-089, RF-090, RF-091 y RF-094 están condicionados al supuesto S-C: si la prueba demuestra que la plataforma de 2011 no puede exponer el cupo con garantías suficientes, el crédito queda fuera del modo desconectado y se aplica el procedimiento manual declarado. M-17 es un modo de C-08, no otro servicio. Fundamento: Caso 09, RT-03.10; Bases Transversales, RT-03.13; catálogo v3.0, decisiones de alcance de RF-089 a RF-094.

### C-09 · Consentimiento y evidencia financiera
**Alias:** M-16.
**Responsabilidad:** registrar la información precontractual efectivamente entregada, su versión, la aceptación y el consentimiento expreso e informado; impedir la aceptación o modificación de condiciones sin evidencia asociada; y preservar un expediente íntegro, enlazado y recuperable para originaciones y repactaciones.
**Actores:** cliente, ejecutivo del emisor, cumplimiento y auditoría/contraloría.
**Límite:** mantiene almacén, permisos y retención segregados del Retail. La evidencia se conserva durante todo el plazo del crédito y seis años adicionales, y debe permitir reconstruir qué se informó, en qué versión y qué aceptó el cliente. C-08 y C-10 consultan su resultado antes de confirmar actos financieros, sin copiar el expediente completo. Fundamento: Caso 09, numerales 4.11 y 9.9, RT-05.10 y RT-16.14; RF-205 a RF-210; RNF-39, RNF-43 y RNF-57.

### C-10 · Administración y cobranza de crédito
**Alias:** M-18.
**Responsabilidad:** mantener la cuenta después de originación; movimientos/saldo, estados, pagos, atención financiera, cobranza, mora y repactación, según los límites del sistema financiero contratado.
**Actores:** deudor, servicio al cliente financiero, cobranza y cumplimiento.
**Límite:** el emisor es autoridad de los saldos. Cada repactación debe obtener evidencia de C-09 antes de confirmar el cambio. La migración de cartera no se convierte en funcionalidad permanente de este servicio.

### C-11 · Correspondencia controlada de identidad (control transversal)
**Alias:** M-22.
**Responsabilidad:** resolver una correspondencia mínima y seudonimizada entre identificadores de Retail y Emisor únicamente para un caso de uso autorizado. La zona neutral devuelve el identificador técnico mínimo o una respuesta puntual; no expone atributos financieros ni construye una vista única de cliente.
**Actores:** Control interno, cumplimiento y auditoría como custodio asumido; el responsable del proceso de Retail o del Emisor que solicita el cruce; y los dueños de los datos de ambos ámbitos como aprobadores. El supuesto de custodia deberá ratificarse con la estructura de gobierno del mandante.
**Límite y decisión:** no es IAM, no constituye un maestro compartido y no es un servicio de negocio independiente. Se implementa dentro de los controles de frontera y gobierno de datos, con denegación por omisión, finalidad y base de licitud declaradas, minimización, autorización de ambos ámbitos y auditoría de cada intento. Se prohíben consultas masivas, exportación del mapa y uso de comportamiento financiero para campañas. El catálogo queda en diez candidatos a servicio. Fundamento: línea roja del Caso 09; Caso 09, sistema de fidelización y RT-16.09; Bases Administrativas, art. 85; RT-05.09; RNF-74 a RNF-76.

## 5. Elementos fuera del catálogo de fronteras de negocio
M-11 Portal del cliente y los canales POS/Seller Center: interfaces/aplicaciones cliente. Invocan servicios; no son dueños por defecto de pedidos, precios, ventas, crédito ni devoluciones.
M-20: separar en inventario de plataforma el API Gateway (entrada/ruteo de solicitudes) y el broker/bus (transporte de mensajes/eventos). Son componentes técnicos, no módulos de negocio ni propietarios de políticas.
M-21 Gobierno de frontera: políticas, custodios, autorizaciones, finalidades, minimización y auditoría transversales. Se implementan como controles, no como un servicio central al que todos entregan datos indiscriminadamente.
M-23 IAM y M-24 observabilidad: capacidades compartidas de plataforma/operación. Se mantienen en la vista técnica, fuera del catálogo de servicios de dominio.
M-19 Migración de cartera: programa de transición temporal con olas, conciliación, umbrales de detención y reversa. No es un módulo permanente del producto.
WMS, ERP/DTE, pasarela de pago, adaptadores EDI y sistemas de vendedores: sistemas externos o adaptadores de integración hasta que exista decisión de reemplazo fundada.

## 6. Resumen de fusiones y separaciones
Fusiones recomendadas: M-01 con M-02; M-03 con M-05 y M-06; M-04 con M-09; M-12 con las funciones B2B de M-14; M-15 con M-17. M-07 se suma a C-01 únicamente si representa evidencia/historial de precio.
Separaciones conservadas: M-10 respecto del registro de venta; M-13 respecto de recobros a vendedores; M-16 respecto de originación y administración de crédito; contexto financiero respecto de retail. M-22 se reclasifica como control transversal de correspondencia, sin autonomía de servicio de negocio.
No se está recomendando fusionar indiscriminadamente solo para reducir el número. Tampoco se mantiene como “módulo” algo que en realidad es una pantalla, infraestructura compartida o fase temporal.

## 7. Interacciones principales entre fronteras
C-01 → C-02/C-04: eventos versionados de artículo y precio; C-04 usa el precio vigente/autorizado en caja y registra evidencia necesaria. Definir caché/localidad y regla ante discrepancia o caída.
C-02 ↔ C-03: C-03 consulta y solicita reserva síncrona al aceptar el pedido; C-02 confirma/libera con idempotencia y publica ajustes relevantes. Los eventos físicos de C-03/WMS actualizan C-02.
C-03 → C-05: evento de pedido web preparado/entregado por tienda para atribución; no devengar por mera creación o reserva fallida.
C-04 → C-05: evento de venta asentada con referencia de vendedor/canal/tienda; reversas y devoluciones generan ajuste atribuible.
C-06 ↔ C-03: C-06 valida oferta/vendedor y entrega datos contractuales de pedido; C-03 gobierna el estado de cumplimiento único. Evitar acceso directo del vendedor a pedidos de otros vendedores.
C-07 → C-02/C-06: solo tras inspección publica aptitud para reintegro; pasa a C-06 la evidencia mínima para una eventual conciliación/recobro, sin bloquear la respuesta al cliente.
C-08 ↔ C-09: validación de evidencia requerida previa al commit financiero, con resultado correlacionable; no guardar copia de expediente innecesaria en el dominio retail.
C-10 ↔ C-09: solicitar/confirmar evidencia antes de aplicar repactaciones o cambios de condición; respuesta durable y auditable.
C-04 → C-08: derivación explícita de contexto mínimo y autorizado desde tienda; el sistema del emisor decide. En desconexión se opera solo el cupo vigente delegado y se concilia al reconectar.
C-11, como control transversal, media únicamente consultas nominadas de C-08, C-09 u otro proceso aprobado, con datos mínimos, propósito validado, autorización y auditoría; jamás admite consulta masiva ni exportación de un mapa de identidades.
Todos los candidatos usan IAM para identidad/roles y envían telemetría minimizada a la plataforma de observabilidad. Gateway y bus transportan contratos; no ejecutan reglas del dominio ni reemplazan controles de autorización dentro del servicio.

## 8. Contratos y límites de datos
Para cada interacción registrar: caso de uso y actor iniciador; servicio dueño del dato; campos permitidos/prohibidos; API o evento y latencia; idempotencia, duplicados, reintentos, versionado y expiración; modo degradado; identidad técnica y humana; correlación/auditoría; política de retención; compatibilidad y prueba.

No permitir lecturas/escrituras de otro servicio sobre tablas internas. Una proyección local puede ser útil si declara dueño, finalidad, campos, frescura y tolerancia de consistencia. La transacción de cliente no exige consistencia fuerte en todos los servicios; las fronteras que involucran reserva, autorización crediticia, consentimiento y saldo sí deben explicitar en qué paso se valida o confirma y cómo se compensa una falla parcial.

Para cualquier cruce Retail ↔ Emisor: declarar finalidad y base autorizante, minimizar atributos, autenticar servicio y actor, aplicar autorización en destino, registrar decisiones permitidas/denegadas y excluir datos financieros innecesarios de logs, búsquedas y analítica retail.

## 9. Trazabilidad de M-01 a M-24
M-01 + M-02 → C-02.
M-03 + M-05 + M-06 → C-01.
M-07 → C-01 solo si se confirma historial/evidencia de precio; si es EDI, inventariar como adaptador de integración, no servicio de dominio.
M-04 + M-09 → C-03.
M-08 → canal POS más la capacidad C-04; POS no se cuenta como backend de negocio.
M-10 → C-05.
M-11 → canal/portal.
M-12 + M-14 (conciliación/recobro de vendedor) → C-06.
M-13 + requisitos de M-14 relativos a recepción/resolución de devolución del consumidor → C-07. La asignación RF debe resolverse semánticamente, no duplicar el mismo requisito.
M-15 + M-17 → C-08.
M-16 → C-09.
M-18 → C-10.
M-19 → iniciativa temporal de migración.
M-20 → Gateway y bus/broker, componentes separados de plataforma.
M-21 → gobierno y control transversal.
M-22 → C-11 como control transversal de frontera; no se cuenta como servicio de negocio.
M-23 → IAM/plataforma.
M-24 → observabilidad/plataforma.

## 10. Validaciones antes de cambiar los IDs/asignaciones oficiales
- Resolver el conflicto de M-07 con el texto exacto de RF-021 y RNF-44/RNF-58: historial de precio o EDI. No heredar ambos alcances bajo un nombre ambiguo.
- Revisar individualmente RF-106 y RF-198 hoy asignados a M-14: determinar si describen notificación/recepción de devolución del cliente (C-07) o conciliación/recobro B2B (C-06).
- Confirmar fuentes autoritativas y responsables de artículo, precio, stock/nodos, documentos tributarios, comisión y saldos.
- Validar reglas y evidencia de modo de crédito offline; C-08 no podrá inventar límites que no estén en bases/requisitos aprobados.
- Ratificar con el mandante el supuesto de que Control interno, cumplimiento y auditoría custodia C-11; mantenerlo como control transversal de frontera, no como servicio de negocio.
- Remapear cada RF/SUP desde requisito individual a C-01…C-10 o al control transversal C-11, actor, dato/contrato, etapa y prueba. No asignar un requisito a un nuevo ID solo porque estaba en el mismo M anterior.
- Revisar con negocio y arquitectura que las fronteras candidatas tienen coherencia, propiedad de datos y límites operables. Solo entonces sustituir alias M-01…M-24 en T7-03.
- Clasificar cada frontera como `módulo`, `servicio desplegable` o `microservicio aprobado`, registrando la evidencia de la puerta de decisión. La categoría inicial es `sin decisión de despliegue`.

## 11. Fuentes y carácter de la recomendación
Fuentes del proyecto:
- [Caso 09 — Cadena Multitienda](../00_Bases/Caso_09_Cadena_Multitienda.md): actores, sistemas, operación y frontera Retail/Emisor.
- [T7-03 — Alcance y trazabilidad](../02_Propuesta/sd-03_esquema-de-solucion-y-alcance/sd-03_s2_alcance.md): objetivos, supuestos, asignaciones de requisitos y nombres M actuales.
- [T7-03 — Esquema de solución](../02_Propuesta/sd-03_esquema-de-solucion-y-alcance/sd-03_s3_esquema-de-solucion.md): diagrama vigente.

Los límites C-01…C-10 y el control transversal C-11 son una inferencia de diseño para reducir fragmentación, preservar la separación normativa y evitar llamadas innecesarias entre servicios; deben ratificarse con responsables del negocio y cotejarse contra el catálogo de requisitos antes de incorporarlos a la oferta técnica.

Fuentes técnicas:
- [OMG — Unified Modeling Language 2.5.1](https://www.omg.org/spec/UML/2.5.1): actor como tipo de rol que una entidad desempeña al interactuar con el sujeto modelado.
- [IIBA — Glosario BABOK](https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/glossary/): actor, stakeholder, organización, unidad organizacional, regulador y proveedor.
- [Microsoft Learn — Microservices architecture style](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices).
- [Microsoft Learn — Domain analysis](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis).
- [Microsoft Learn — Identify microservice boundaries](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/microservice-boundaries).
- [Microsoft Learn — Data considerations for microservices](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/data-considerations).
- [AWS Prescriptive Guidance — Decompose by subdomain](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/decompose-subdomain.html).

Estas guías sustentan los criterios de análisis de dominio, despliegue independiente, autonomía de datos y control de acoplamiento. También advierten que un contexto delimitado es un candidato, no una equivalencia automática con un microservicio. Los límites concretos del caso deben validarse con el negocio, los requisitos no funcionales y el modelo operativo.
