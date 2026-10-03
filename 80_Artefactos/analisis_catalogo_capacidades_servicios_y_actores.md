# Análisis inicial del catálogo de capacidades, servicios y actores

> **Vigencia:** este análisis inicial queda supersedido para la recomendación del catálogo. La versión vigente propone 11 candidatos a servicio y conserva la trazabilidad M-01…M-24 en [catalogo_servicios_candidatos_11.md](catalogo_servicios_candidatos_11.md). Este archivo se conserva como antecedente del análisis preliminar.

## Propósito y conclusión

Este documento propone una base para revisar el catálogo actual de M-01 a M-24 del subdocumento T7-03. Separa las capacidades de negocio de los canales, los servicios de plataforma y las iniciativas transitorias; identifica los actores que interactúan con cada capacidad y propone las principales relaciones entre ellas.

La conclusión principal es que una categoría del catálogo no equivale automáticamente a un microservicio. Primero se delimitan las capacidades y sus contextos de negocio; luego se decide si cada contexto se implementa como un solo servicio, varios servicios o módulos dentro de una aplicación. Los identificadores actuales se conservan provisionalmente para proteger la trazabilidad de requisitos.

Este análisis es una propuesta de diseño, no una aprobación de límites de despliegue. En particular, las relaciones y patrones de interacción deberán validarse con el equipo y contrastarse con los requisitos atomizados antes de cambiar la asignación de RF, SUP o IDs.

## 1. Conceptos y niveles del catálogo

| Nivel | Definición para este proyecto | Ejemplo |
| --- | --- | --- |
| Actor | Persona, rol organizacional u organización externa que inicia, ejecuta, autoriza, recibe o es afectada por una operación. | Cliente, vendedor, jefatura, vendedor de marketplace, cumplimiento del emisor. |
| Capacidad de negocio | Resultado o responsabilidad que el negocio debe poder realizar, independientemente de una aplicación concreta. | Mantener precios, controlar exactitud de inventario, resolver una devolución. |
| Contexto delimitado | Frontera dentro de la cual un modelo, lenguaje, reglas y responsabilidad tienen significado consistente. | Crédito del emisor, separado del retail. |
| Servicio de microservicios | Unidad de software autónoma, desplegable y operable de forma independiente, que implementa una responsabilidad cohesionada de un dominio, posee su lógica y sus datos y se comunica mediante contratos explícitos. | Servicio de originación crediticia, si el análisis confirma autonomía suficiente. |
| Canal o aplicación cliente | Interfaz que permite a un actor usar capacidades; puede contener lógica de experiencia, pero no debe convertirse por defecto en dueña de la lógica de negocio. | Portal cliente, POS, Seller Center. |
| Servicio de plataforma | Capacidad técnica compartida para ejecutar, proteger o conectar soluciones; no es por ello una capacidad de negocio. | API Gateway, bus de eventos, IAM, observabilidad. |
| Interacción | Contrato por el cual un servicio solicita una operación o recibe información de otro. Puede ser síncrono o asíncrono. | Pedido consulta disponibilidad; Inventario publica ajuste confirmado. |

La guía de Microsoft describe un microservicio como autónomo y enfocado en una capacidad de negocio dentro de un contexto delimitado, con datos privados a cada servicio. Un contexto delimitado puede ser una frontera lógica sin que necesariamente sea un proceso desplegado por separado. Por tanto, una categoría del catálogo es una hipótesis de capacidad o contexto, no una decisión automática de despliegue. [Microsoft, arquitectura de microservicios](https://learn.microsoft.com/en-us/azure/architecture/microservices/) · [Microsoft, soberanía de datos](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/architect-microservice-container-applications/data-sovereignty-per-microservice)

## 2. Criterios para proponer un microservicio

Una capacidad será candidata a servicio independiente cuando exista evidencia razonable de:

- responsabilidad funcional cohesionada y reglas propias;
- datos de los que esa responsabilidad es autoridad, sin acceso directo de otros servicios a su almacén;
- frontera de seguridad y cumplimiento identificable;
- necesidad plausible de evolucionar, desplegar, escalar o recuperarse independientemente;
- contrato estable hacia consumidores y pocos intercambios de ejecución innecesariamente frecuentes.

Una capacidad que no cumpla estos criterios puede permanecer como módulo de un servicio mayor. Si dos servicios se llaman repetidamente para completar cada operación o comparten transacciones y reglas inseparables, se debe revisar si la frontera está demasiado fragmentada. La guía de Microsoft recomienda evitar llamadas excesivamente conversacionales entre servicios; AWS advierte que una descomposición excesiva aumenta la dificultad de integración y descubrimiento. [Microsoft, consideraciones de datos e interacción](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/data-considerations) · [AWS, descomposición por subdominio](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/decompose-subdomain.html)

## 3. Propuesta de clasificación de M-01 a M-24

Los IDs y nombres siguientes se mantienen como referencias de continuidad del esquema vigente. “Candidato de negocio” no significa “microservicio aprobado”. La materialización como uno o varios servicios queda pendiente del análisis de reglas, datos, carga, seguridad y operación.

| ID actual | Capacidad o elemento | Clasificación preliminar | Actores principales |
| --- | --- | --- | --- |
| M-01 | Disponibilidad comprometible (ATP) | Capacidad de decisión de negocio; posible servicio candidato separado del inventario físico/contable. | Canales digitales, vendedor de piso, pedido, planificación comercial. |
| M-02 | Exactitud, conteo y ajuste de inventario | Capacidad de negocio; dueña de conteos, causas de diferencia y ajustes autorizados. | Jefatura, bodega, prevención de pérdidas, reposición. |
| M-03 | Maestro de artículos y calidad del catálogo | Capacidad de negocio. Determina atributos y aptitud de publicación. | Comercial, compras, canales digitales, marketplace. |
| M-04 | Gestión de nodos logísticos | Capacidad de negocio; delimitar inventario por nodo frente a la ejecución WMS y al pedido. | Logística, planificación, tiendas, centros de distribución. |
| M-05 | Precios y promociones | Capacidad de negocio que define reglas y vigencias de oferta. | Comercial, precios, caja, canal digital, cliente. |
| M-06 | Ejecución y evidencia de etiquetas físicas | Capacidad operativa de negocio, candidata a mantenerse ligada al dominio de precio si no requiere autonomía propia. | Reposición, jefaturas, caja, cliente. |
| M-07 | Trazabilidad EDI (nombre actual); RF-021 le asigna historial del precio por canal | Inconsistencia de nombre y responsabilidad: decidir si se renombra/redefine para precio publicado histórico o si EDI y evidencia de precio son capacidades separadas. | Atención al cliente, cumplimiento, comercial, cliente; sistemas externos si se conserva EDI. |
| M-08 | Punto de venta y venta en contingencia | POS es canal/aplicación cliente; la venta y su registro son capacidades. El modo desconectado es una condición operativa, no necesariamente otro dominio. | Cajero, vendedor, cliente, ERP emisor de documentos. |
| M-09 | Ciclo de vida y orquestación del pedido | Capacidad de negocio; coordina aceptación, reserva, nodo, preparación, resolución de quiebres y estados. | Cliente, canales, tienda, bodega, logística, atención. |
| M-10 | Atribución de venta y comisión | Capacidad/reglas de negocio; precisar quién es propietario de la política y del cálculo/liquidación. | Vendedor, jefatura, remuneraciones/finanzas, pedido. |
| M-11 | Portal del cliente | Canal/aplicación cliente, no dueño automático de pedido, precio, pago ni posventa. | Cliente, atención al cliente. |
| M-12 | Gobierno de vendedores de marketplace | Capacidad de negocio del ecosistema de terceros: alta, reglas, ofertas, calidad y desempeño. | Vendedor de marketplace, gestión marketplace, cliente. |
| M-13 | Posventa, garantía y decisión de aptitud de devolución | Capacidad de negocio; la resolución del consumidor no debe depender de la recuperación posterior contra un tercero. | Cliente, atención, tienda, vendedor marketplace, prevención. |
| M-14 | Conciliación y recobros B2B (nombre actual); RF-106/RF-198 le asignan aviso de devolución y recuperación contra tercero | Posible mezcla de responsabilidades: distinguir notificación de recepción, conciliación financiera y recobro; validar si pertenecen a un flujo cohesionado o a capacidades separadas. | Vendedor marketplace, atención, bodega, finanzas retail. |
| M-15 | Originación y evaluación crediticia | Capacidad del contexto financiero del emisor. No pertenece al dominio retail aunque se inicie en caja. | Cliente, ejecutivo financiero, vendedor habilitado, riesgo/crédito. |
| M-16 | Información precontractual, consentimiento y evidencia | Capacidad de control/evidencia del emisor; debe preservar evidencia y retención propias. | Cliente, ejecutivo, cumplimiento, auditoría/contraloría. |
| M-17 | Operación crediticia desconectada contra cupo vigente | Modo/capacidad de contingencia del contexto financiero; validar si se integra en Originación/Crédito o si exige autonomía operacional real. | Cliente, ejecutivo financiero, riesgo, operación TI. |
| M-18 | Servicio del crédito y cobranza | Capacidad propia del emisor: cuenta, atención de deudores, cobranza y repactación. | Deudor, servicio al cliente financiero, cobranza, cumplimiento. |
| M-19 | Migración de cartera | Iniciativa/capacidad transitoria de transición y conciliación; no asumir como servicio permanente del producto final. | Equipos de migración, finanzas, operaciones del emisor, auditoría. |
| M-20 | Bus de eventos + API Gateway (agrupación actual) | Dos componentes distintos de plataforma: separar en el inventario técnico. El bus transporta eventos; el gateway enruta solicitudes API. Ninguno decide reglas de dominio ni es módulo de negocio. | Servicios productores/consumidores, canales y operación TI. |
| M-21 | Gobierno y control de frontera de datos | Capacidad de gobierno/política transversal; regula intercambios entre contextos, no es un permiso genérico para cruzar datos. | Cumplimiento, privacidad, dueños de datos, auditoría, TI. |
| M-22 | Correspondencia controlada de identidad | Servicio/capacidad sensible en zona neutral; no equivale a IAM ni autoriza reutilización comercial de datos financieros. | Custodio autorizado, cumplimiento, procesos expresamente habilitados. |
| M-23 | IAM y gestión de acceso | Servicio de plataforma/seguridad. Aplica autenticación, autorización y ciclo de vida de credenciales; no es módulo funcional de negocio. | Personal propio, externos, jefaturas, administradores de identidad. |
| M-24 | Observabilidad y degradación controlada | Plataforma de operación/resiliencia. Provee telemetría y mecanismos técnicos; las decisiones comerciales de priorización pertenecen al dominio responsable. | Operaciones TI, SRE, responsables de canal y negocio. |

Los adaptadores EDI, API Gateway, transporte de eventos, almacenamiento técnico, monitoreo y CI/CD deben inventariarse en la vista de plataforma e integración, no asignarse como capacidades funcionales de negocio. El bus puede transportar eventos sin ser propietario de las reglas que los producen.

## 4. Actores y capacidades

La relación actor–capacidad es muchos-a-muchos. Cada fila de trabajo detallada debe indicar además el papel del actor: iniciador, ejecutor, aprobador, consumidor/beneficiario, sujeto de la operación o sistema externo.

| Actor/grupo | Capacidades con interacción directa | Precaución de diseño |
| --- | --- | --- |
| Cliente/consumidor | Catálogo, precio, disponibilidad, pedido, pago, retiro/despacho, cambios, devolución/garantía y, cuando corresponde, crédito. | Una persona puede interactuar con retail y con el emisor; identidad común no elimina las fronteras de datos. |
| Vendedor/cajero | Venta en sala, consulta ATP, promoción, atribución de comisión y oferta/derivación a crédito. | Flujo rápido, credenciales individuales y autorización explícita para funciones financieras. |
| Jefatura de tienda/departamento | Ajustes y conteos, operación de sala, revisión de etiquetas, autorización local y métricas. | Diferenciar aprobación, ejecución y auditoría de un ajuste. |
| Reposición/bodega/CD | Recepción, movimiento, conteo, etiqueta, preparación, despacho y recepción física de devoluciones. | Los eventos físicos deben ser evidencia de proceso, con actor, tiempo y ubicación. |
| Prevención de pérdidas | Conteo cíclico, investigación de merma, análisis de diferencias. | No confundir pérdida física con error administrativo sin evidencia. |
| Comercial/compras/precios | Surtido, artículos, precio y promociones. | El dato publicado debe conservar canal y vigencia. |
| Logística/planificación | Reposición, inventario de nodos, selección de capacidad y cumplimiento. | Mantener autoridad de cada nodo y del WMS existente según decisión de arquitectura. |
| Vendedor marketplace | Oferta, disponibilidad declarada, pedidos, reglas de servicio, devoluciones y liquidación. | Acceso limitado al propio catálogo y operaciones; no exposición de datos de clientes ajenos. |
| Personal del emisor financiero | Originación, atención, cobranza, repactación y servicio de crédito. | Contexto financiero y permisos segregados del retail. |
| Cumplimiento/contraloría del emisor | Reglas de evidencia, auditoría, retención y revisión de cruces permitidos. | Autoridad auditora no equivale a operador cotidiano de todas las funciones. |
| TI/operación/SRE | IAM, integración, observabilidad, disponibilidad y respuesta a incidentes. | Operar plataforma no otorga autoridad para cambiar reglas o datos de negocio. |
| Sistemas/terceros externos | ERP emisor de documentos, WMS, proveedor de medios de pago, marketplace y sistemas que se mantienen. | Modelar explícitamente contrato, dueño, latencia, disponibilidad y tratamiento de fallas. |

La separación retail/emisor financiero es un límite legal y de gobierno central del caso. Por ello, el catálogo debe marcar cada contexto como **Retail**, **Emisor financiero** o **Transversal controlado**, y cada interacción entre esos ámbitos debe declarar finalidad, datos mínimos, autorización/base aplicable y registro de auditoría. La clasificación “transversal” no supone que los datos estén abiertos a ambos dominios.

## 5. Catálogo inicial de interacciones entre capacidades

Las modalidades que siguen son propuestas iniciales, no contratos aprobados. La elección síncrono/asíncrono dependerá de latencia requerida, consecuencia de indisponibilidad y consistencia aceptable. En microservicios, la comunicación puede ser directa por API o asíncrona por mensajes/eventos; el servicio propietario conserva sus datos. [Microsoft, interacción y datos](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/data-considerations)

| Origen → destino | Propósito y datos principales | Patrón candidato | Riesgo/decisión a validar |
| --- | --- | --- | --- |
| M-03 Artículos → M-05 Precios | Identificadores, atributos, categoría y estado de venta. | Evento de artículo creado/actualizado; consulta API para validación puntual. | Calidad y versión del artículo; evitar acoplar los esquemas internos. |
| M-05 Precios → M-06 Etiquetas | Precio, vigencia, local/categoría y orden de cambio físico. | Orden de ejecución y acuse por API/evento; registro de quién/cuándo. | Qué ocurre con etiqueta pendiente, discrepancia en caja o canal sin confirmar. |
| M-05 Precios → M-07 Evidencia | Precio y mecánica publicados por canal en un instante. | Evento versionado e inmutable o registro auditable del dueño de precios. | Retención, consulta histórica y fuente autoritativa por canal. |
| M-02 Inventario → M-01 ATP | Existencia, reservas, comprometido, ajustes y señales de confianza. | Eventos de cambios más consulta/reserva síncrona cuando una venta requiere decisión inmediata. | Definir saldo disponible sin tratar el registro bruto como verdad absoluta. |
| M-01 ATP → M-09 Pedido/canales | Disponibilidad calculada, nodo y resultado de reserva/compromiso. | Consulta/reserva síncrona para aceptación; evento al confirmar o liberar reserva. | Idempotencia, expiración de reserva y concurrencia en eventos masivos. |
| M-09 Pedido → M-04 Logística/nodos | Solicitud de preparación, destino, promesa y asignación. | API para crear instrucción; eventos de preparado, despachado, entregado o quiebre. | Evitar una transacción distribuida con el WMS; reglas de reasignación y compensación. |
| M-04 Logística → M-02 Inventario | Movimientos y confirmaciones físicas de recepción/preparación/despacho. | Eventos idempotentes con referencia de operación y nodo. | Reconciliar reintentos y operaciones desconectadas sin duplicar stock. |
| M-08 POS/venta → M-05 Precios | Precio y promoción aplicables en caja. | Consulta síncrona o caché versionada según continuidad y latencia; evidencia de precio cobrado. | Regla legal ante discrepancia entre precio exhibido y cobrado; modo sin enlace. |
| M-08 POS/venta → M-10 Comisión | Venta cobrada, actor vendedor, tienda, canal y origen. | Evento de venta asentada; cálculo/liquidación del lado propietario de comisión. | Definir origen de venta web preparada por tienda y reversas/devoluciones. |
| M-09 Pedido → M-10 Comisión | Pedido web preparado/despachado por una tienda y atribución correspondiente. | Evento de cumplimiento físico confirmado. | No devengar por reserva fallida; ajustar ante devolución o cancelación. |
| M-11 Portal y canales → M-09 Pedido | Creación/consulta de pedido y notificación de cambios de estado. | API para comandos/consultas; eventos o notificaciones de estado. | El portal no se convierte en fuente de verdad del pedido. |
| M-12 Marketplace → M-09 Pedido | Oferta, vendedor, disponibilidad declarada y detalle de orden. | API/eventos con contrato externo y validación de vendedor. | Aislamiento por vendedor, ofertas vencidas y caídas del tercero. |
| M-13 Posventa → M-14 Recuperación marketplace | Recepción, motivo, estado de resolución y evidencia física. | Evento de devolución recibida; flujo separado para conciliación con vendedor. | No bloquear remedio del cliente por disputa o recuperación contra tercero. |
| M-13 Posventa → M-02/M-01 Inventario/ATP | Evaluación de aptitud y destino de unidad devuelta. | Evento de decisión de aptitud; sólo después habilitar reintegro a stock vendible. | Evitar que una devolución no inspeccionada aumente ATP. |
| M-15 Originación → M-16 Evidencia | Solicitud, información precontractual entregada, consentimiento y versión contractual. | API síncrona bloqueante para verificar evidencia antes de aceptar; evento/auditoría persistente. | No permitir originación si falta prueba; integridad y conservación. |
| M-18 Servicio de crédito → M-16 Evidencia | Consentimiento de repactación/cambio de condiciones y evidencia entregada. | Validación síncrona previa al commit más evidencia durable. | No aplicar una modificación sin consentimiento recuperable. |
| M-08 Venta → M-15/M-17 Crédito | Solicitud iniciada desde caja y contexto mínimo permitido. | Llamada autenticada al contexto financiero; M-17 aplica solo contingencia autorizada. | Frontera legal/técnica; en desconexión no abrir tarjeta nueva y limitar a cupo vigente según requisitos. |
| M-21 Gobierno frontera → interacciones retail/finanzas | Política, finalidad, autorización, atributos permitidos y auditoría de cruces. | Punto de control/política más registro de decisión; precisar arquitectura sin imponer un único componente. | No convertir el bus, gateway o M-21 en acceso irrestricto a los datos. |
| M-22 Correspondencia identidad → procesos autorizados | Correspondencia de identificadores solicitada bajo autorización expresa. | API controlada de zona neutral con identidad nominada y auditoría. | No compartir tabla ni exportar identificadores para campañas generales. |
| M-23 IAM → servicios/canales | Identidad, rol, permisos, vigencia y revocación de acceso. | Protocolos estándar de identidad y autorización contextual. | M-23 gestiona permisos; cada servicio valida autorización de su dominio. |
| M-24 Observabilidad ← servicios/plataforma | Métricas, trazas, logs técnicos y señales de salud. | Telemetría; alertas operativas y políticas de degradación controlada. | Minimizar datos personales/financieros en logs; sólo roles aprobados activan degradación comercial. |
| M-19 Migración ↔ M-18 crédito/plataforma antigua | Extractos, saldos, cohortes, conciliación y resultado de corte/ola. | Lotes o eventos controlados de coexistencia; conciliación diaria y freno ante diferencias. | Perímetro temporal, autoridad de saldo por etapa y plan de reversa. |

## 6. Reglas de contrato para las interacciones

Cada vínculo aprobado debería contar con una ficha que responda:

1. ¿Qué caso de uso o regla requiere el intercambio, y qué actor lo origina?
2. ¿Quién es proveedor/autoridad del dato y quién es consumidor?
3. ¿Qué campos mínimos se intercambian y cuáles están prohibidos?
4. ¿Se requiere respuesta inmediata (API) o se acepta propagación posterior (evento)? ¿Qué latencia es admisible?
5. ¿Cómo se gestionan versión del contrato, idempotencia, duplicados, timeout, reintentos, orden, expiración y conciliación?
6. ¿Qué comportamiento ofrece el consumidor si el proveedor no está disponible, especialmente en tienda desconectada?
7. ¿Qué identidad técnica y rol humano se registran? ¿Qué dato sensible debe excluirse de telemetría y auditoría general?
8. ¿Cómo se prueba compatibilidad, seguridad, recuperación y evolución del contrato sin despliegue coordinado de todos los servicios?

No se debe usar una base de datos compartida como atajo de integración. Una copia local o proyección de lectura puede ser válida si tiene propietario, propósito, actualización y tolerancia de consistencia explícitos.

## 7. Decisiones que requieren validación antes de cambiar el catálogo

- Confirmar la definición precisa, reglas y propietario de M-04, M-10, M-13 y M-14; sus nombres actuales no bastan para fijar límites.
- Decidir si M-06 y M-07 pertenecen al mismo contexto de precios o requieren autonomía por evidencia, operación física o auditoría.
- Revisar si M-08, M-11 y M-12 son principalmente canales/aplicaciones, mientras las capacidades de venta, pedido y gobierno marketplace tienen propietarios de negocio separados.
- Delimitar M-21 y M-22 como controles de gobierno/privacidad y servicio neutral de correspondencia, respectivamente; ninguno sustituye a la autoridad de datos de retail o del emisor.
- Validar si M-17 tiene suficientes reglas y necesidades de operación propias para ser servicio o se mantiene como modalidad de contingencia de M-15/M-18.
- Describir qué servicios son candidatos reales a despliegue independiente y cuáles pueden empezar como módulos cohesionados. No imponer microservicios por requisito estético.
- Resolver las alertas de alcance de M-07 (Trazabilidad EDI frente a RF-021 sobre historial de precio) y M-14 (Conciliación/recobros frente a notificación de devolución).
- Completar la matriz de trazabilidad RF/SUP → capacidad → servicio candidato → contrato/interacción → actor → prueba. Conservar IDs previos como alias hasta una migración aprobada.

## 8. Fuentes

- Bases del caso: [Caso 09 — Cadena Multitienda](../00_Bases/Caso_09_Cadena_Multitienda.md), especialmente personas, zonas de operación, ciclos de producto/cliente/crédito, sistemas existentes y frontera del negocio financiero.
- Catálogo y asignaciones actuales: [T7-03, sección de alcance y trazabilidad](../02_Propuesta/sd-03_esquema-de-solucion-y-alcance/sd-03_s2_alcance.md) y esquema de solución vigente de T7-03.
- [Microsoft Azure Architecture Center — Microservices architecture](https://learn.microsoft.com/en-us/azure/architecture/microservices/).
- [Microsoft — Data sovereignty per microservice](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/architect-microservice-container-applications/data-sovereignty-per-microservice).
- [Microsoft Azure Architecture Center — Data considerations for microservices](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/data-considerations).
- [AWS Prescriptive Guidance — Decompose by subdomain](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/decompose-subdomain.html).
