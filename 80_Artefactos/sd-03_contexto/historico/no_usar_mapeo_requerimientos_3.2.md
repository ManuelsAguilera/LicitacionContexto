> **ARCHIVADO (2026-10-08). No usar como fuente.** Material de trabajo superado por `sd-03.tex`, los Anexos A a D y `ficha_alcance_sd-03.md`. Usa códigos y decisiones antiguas. Se conserva solo por trazabilidad.

# Mapeo propuesto de requerimientos a servicio, etapa y prioridad (insumo de 3.2.4)

> **Nomenclatura (2026-10-07):** los nombres y códigos de los servicios de este documento (R-01 a X-01) fueron reemplazados. Rige `divisiones_negocio_servicios_sd-03.md`, que contiene la tabla de equivalencias.

Documento de contexto, no es entregable. Generado el 2026-10-06 desde el espejo `01_Requerimientos/md/catalogo-de-requerimientos-depurado-v30.md` (hoja 1_Catalogo_Atomico, espejo del 2026-09-29) con reglas automáticas. **Es una propuesta (S) para revisar y cargar en el Excel oficial** `01_Requerimientos/RequerimientosAtomizados_Depuracion_Alcance.xlsx`, que manda sobre este archivo y sobre el espejo. El espejo cuenta 223 RF, 75 RNF y 9 OP; AGENTS.md menciona RF-001..RF-226 y RNF-01..RNF-76: confirmar los totales en el Excel antes de citarlos.

## Reglas usadas

- **Servicio:** por módulo del catálogo (Precios y Etiquetado → R-01; Inventario y Disponibilidad → R-03, o R-02 si trata de reposición, recepción u órdenes; Pedidos y Cumplimiento → R-04, o R-06/R-07/R-03 según palabras clave; Operación de Tienda → R-05 por defecto, con R-01, R-03, R-04, R-08 o identidad según palabras clave; Ventas en Tienda → R-05; Crédito y Cobranza → F-01, F-02 o F-03 según palabras clave; Marketplace → R-07; Devoluciones y Garantía Legal → R-08; Seguridad y Accesos → identidad y gestión de accesos (1.14c); Gobernanza de Datos → X-01; Evento de Alta Concurrencia → R-03, R-04 o plataforma). Los RNF van a la plataforma (transversales) y las OP a gestión del proyecto. La columna "Revisar" marca las asignaciones dudosas.
- **Etapa:** la del servicio (`asignacion_etapas.md`, decisiones A2 y Ronda G). F-02 se reparte por olas.
- **Prioridad (MoSCoW):** Must si el servicio es de primera prioridad (criterios P1 a P3, Etapa 1), si es RNF u obligación del proponente, o si sostiene una restricción no negociable del Caso (garantía legal, restricción 7); Should si es del segundo alcance (Etapa 2); Could y Won't no se asignan automáticamente (Could = mejora sobre lo exigido; Won't = excluido).

## Síntesis (base de la tabla de 3.2.4)

| Servicio o componente | RF | RNF | OP | Etapa |
| :-- | --: | --: | --: | :-- |
| F-01 | 14 | 0 | 0 | 1 |
| F-02 | 5 | 0 | 0 | 1 (ola 1) y 2 (ola 2) |
| F-03 | 14 | 0 | 0 | 1 |
| R-01 | 16 | 0 | 0 | 1 |
| R-02 | 3 | 0 | 0 | 2 |
| R-03 | 49 | 0 | 0 | 1 |
| R-04 | 35 | 0 | 0 | 2 |
| R-05 | 14 | 0 | 0 | 1 |
| R-06 | 3 | 0 | 0 | 2 |
| R-07 | 25 | 0 | 0 | 2 |
| R-08 | 12 | 0 | 0 | 2 |
| X-01 | 12 | 0 | 0 | 1 |
| Gestión del proyecto | 0 | 0 | 9 | Todo el proyecto |
| Identidad (1.14c) | 14 | 0 | 0 | 1 |
| Plataforma | 7 | 75 | 0 | 1 |
| **Total** | **223** | **75** | **9** | |

| Etapa | RF | RNF | OP |
| :-- | --: | --: | --: |
| 1 | 140 | 75 | 0 |
| 1 (ola 1) y 2 (ola 2) | 5 | 0 | 0 |
| 2 | 78 | 0 | 0 |
| Todo el proyecto | 0 | 0 | 9 |

| Prioridad | RF | RNF | OP |
| :-- | --: | --: | --: |
| Must | 150 | 75 | 9 |
| Should | 73 | 0 | 0 |

Asignaciones marcadas para revisar: 26 de 307.

## Detalle por requerimiento

| ID | Tipo | Módulo | Descripción (abreviada) | Servicio | Etapa | Prioridad | Revisar |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| RF-001 | RF | Ventas en Tienda | El sistema deberá permitir la venta física de la unidad aunque exista una reserva tempo… | R-05 | 1 | Must |  |
| RF-002 | RF | Seguridad y Accesos | El sistema deberá exigir credenciales individuales al usuario antes de habilitar cualqu… | Identidad (1.14c) | 1 | Must |  |
| RF-003 | RF | Seguridad y Accesos | El sistema debe impedir el acceso anónimo a una terminal. | Identidad (1.14c) | 1 | Must |  |
| RF-004 | RF | Seguridad y Accesos | El sistema debe impedir el acceso mediante credencial compartida. | Identidad (1.14c) | 1 | Must |  |
| RF-005 | RF | Seguridad y Accesos | El sistema deberá permitir el traspaso de sesión nominativa entre usuarios en una termi… | Identidad (1.14c) | 1 | Must |  |
| RF-006 | RF | Seguridad y Accesos | El sistema deberá cerrar automáticamente la sesión por inactividad en la terminal compa… | Identidad (1.14c) | 1 | Must |  |
| RF-007 | RF | Seguridad y Accesos | El sistema deberá impedir la ejecución de la función de originación a un usuario sin ca… | Identidad (1.14c) | 1 | Must |  |
| RF-008 | RF | Seguridad y Accesos | El sistema deberá impedir la ejecución de la función de repactación a un usuario sin ca… | Identidad (1.14c) | 1 | Must |  |
| RF-009 | RF | Seguridad y Accesos | El sistema deberá revocar automáticamente la habilitación funcional del usuario al venc… | Identidad (1.14c) | 1 | Must |  |
| RF-010 | RF | Seguridad y Accesos | El sistema deberá permitir al proveedor patrocinar la habilitación temporal de acceso d… | Identidad (1.14c) | 1 | Must |  |
| RF-011 | RF | Seguridad y Accesos | El sistema deberá caducar automáticamente la habilitación de acceso del personal extern… | Identidad (1.14c) | 1 | Must |  |
| RF-012 | RF | Seguridad y Accesos | El sistema deberá registrar de forma individualizada el acceso y la actividad del perso… | Identidad (1.14c) | 1 | Must |  |
| RF-013 | RF | Seguridad y Accesos | El sistema deberá revocar la totalidad de los accesos y credenciales del trabajador a p… | Identidad (1.14c) | 1 | Must |  |
| RF-014 | RF | Seguridad y Accesos | El sistema debe conciliar los accesos vigentes contra la nómina activa. | Identidad (1.14c) | 1 | Must |  |
| RF-015 | RF | Seguridad y Accesos | El sistema debe informar al oficial de seguridad los accesos huérfanos detectados en la… | Identidad (1.14c) | 1 | Must |  |
| RF-016 | RF | Precios y Etiquetado | El sistema deberá propagar el cambio de precio a las 380 líneas de caja. | R-01 | 1 | Must |  |
| RF-017 | RF | Precios y Etiquetado | El sistema deberá propagar el cambio de precio al canal digital. | R-01 | 1 | Must |  |
| RF-018 | RF | Precios y Etiquetado | El sistema deberá propagar el cambio de precio a los puntos de exhibición física de cad… | R-01 | 1 | Must |  |
| RF-019 | RF | Precios y Etiquetado | El sistema deberá permitir al reponedor registrar la referencia y la tienda de la etiqu… | R-01 | 1 | Must |  |
| RF-020 | RF | Precios y Etiquetado | El sistema deberá registrar la identidad individual del ejecutor del cambio de etiqueta. | R-01 | 1 | Must |  |
| RF-021 | RF | Precios y Etiquetado | El sistema deberá permitir al ejecutivo de cumplimiento recuperar el precio publicado d… | R-01 | 1 | Must |  |
| RF-022 | RF | Precios y Etiquetado | El sistema deberá obtener el precio vigente de la referencia según el último precio pro… | R-01 | 1 | Must |  |
| RF-023 | RF | Precios y Etiquetado | El sistema deberá cobrar el menor de ambos precios para el consumidor. | R-01 | 1 | Must |  |
| RF-024 | RF | Precios y Etiquetado | El sistema deberá generar un registro de incidente de discrepancia de precio consultable. | R-01 | 1 | Must |  |
| OP-01 | OP | Obligación del PROPONENTE | El PROPONENTE debe especificar la alternativa de etiquetas electrónicas frente a las de… | Gestión del proyecto | Todo el proyecto | Must |  |
| OP-02 | OP | Obligación del PROPONENTE | El PROPONENTE debe costear la alternativa de etiquetas electrónicas sin asumir su adqui… | Gestión del proyecto | Todo el proyecto | Must |  |
| RF-027 | RF | Precios y Etiquetado | El sistema debe generar una alerta operativa al jefe de tienda identificando la etiquet… | R-01 | 1 | Must |  |
| OP-03 | OP | Obligación del PROPONENTE | El PROPONENTE debe especificar la cobertura de despliegue de las etiquetas electrónicas. | Gestión del proyecto | Todo el proyecto | Must |  |
| OP-04 | OP | Obligación del PROPONENTE | El PROPONENTE debe especificar el hardware requerido por la alternativa de etiquetas el… | Gestión del proyecto | Todo el proyecto | Must |  |
| OP-05 | OP | Obligación del PROPONENTE | El PROPONENTE debe presentar el costo de la alternativa separadamente del resto de la s… | Gestión del proyecto | Todo el proyecto | Must |  |
| RF-028 | RF | Precios y Etiquetado | El sistema deberá impedir la venta de la referencia al precio nuevo mientras su punto d… | R-01 | 1 | Must |  |
| RF-029 | RF | Precios y Etiquetado | El sistema deberá generar un indicador diario de puntos de exhibición desactualizados c… | R-01 | 1 | Must |  |
| RF-030 | RF | Precios y Etiquetado | El sistema deberá agrupar los cambios de precio de sala en ventanas parametrizadas fuer… | R-01 | 1 | Must |  |
| RF-032 | RF | Precios y Etiquetado | El sistema deberá evaluar la vigencia de cada promoción al instante de emisión del docu… | R-01 | 1 | Must |  |
| RF-033 | RF | Precios y Etiquetado | El sistema deberá evaluar la aplicabilidad de la promoción según el canal de la venta. | R-01 | 1 | Must |  |
| RF-034 | RF | Precios y Etiquetado | El sistema deberá evaluar la aplicabilidad de la promoción según la tienda en que se re… | R-01 | 1 | Must |  |
| RF-035 | RF | Pedidos y Cumplimiento | El sistema deberá crear una reserva temporal para la unidad agregada al carro. | R-03 | 1 | Must | revisar (reserva o pedido) |
| RF-036 | RF | Pedidos y Cumplimiento | El sistema deberá permitir parametrizar el período de vigencia de la reserva temporal. | R-03 | 1 | Must | revisar (reserva o pedido) |
| RF-037 | RF | Pedidos y Cumplimiento | El sistema deberá mantener activa la reserva mientras el cliente mantenga actividad, co… | R-03 | 1 | Must | revisar (reserva o pedido) |
| RF-038 | RF | Pedidos y Cumplimiento | El sistema deberá impedir que una misma unidad sea comprometida simultáneamente en más… | R-04 | 2 | Should |  |
| RF-039 | RF | Pedidos y Cumplimiento | El sistema debe liberar la reserva temporal al expirar su período de vigencia. | R-03 | 1 | Must | revisar (reserva o pedido) |
| RF-040 | RF | Pedidos y Cumplimiento | El sistema debe devolver la unidad liberada al disponible para vender. | R-03 | 1 | Must | revisar (reserva o pedido) |
| RF-041 | RF | Pedidos y Cumplimiento | El sistema deberá liberar de inmediato la reserva digital de esa unidad, sin esperar la… | R-03 | 1 | Must | revisar (reserva o pedido) |
| RF-042 | RF | Pedidos y Cumplimiento | El sistema deberá aplicar el período de vigencia de reserva reducido declarado como par… | R-03 | 1 | Must | revisar (reserva o pedido) |
| RF-043 | RF | Pedidos y Cumplimiento | El sistema deberá preautorizar el medio de pago al aceptar el pedido, sin capturar el c… | R-04 | 2 | Should |  |
| RF-044 | RF | Pedidos y Cumplimiento | El sistema deberá verificar la existencia física real de la unidad en el punto asignado… | R-03 | 1 | Must | revisar (reserva o pedido) |
| RF-045 | RF | Pedidos y Cumplimiento | El sistema deberá capturar el cobro únicamente al registrarse el evento de confirmación… | R-04 | 2 | Should |  |
| RF-046 | RF | Pedidos y Cumplimiento | El sistema deberá determinar automáticamente la alternativa de resolución aplicable seg… | R-04 | 2 | Should |  |
| RF-047 | RF | Pedidos y Cumplimiento | El sistema deberá requerir la aceptación explícita del cliente antes de capturar el cobro. | R-04 | 2 | Should |  |
| RF-048 | RF | Pedidos y Cumplimiento | El sistema deberá anular la preautorización de pago del pedido. | R-04 | 2 | Should |  |
| RF-049 | RF | Pedidos y Cumplimiento | El sistema deberá cancelar el pedido registrando el motivo de la cancelación. | R-04 | 2 | Should |  |
| RF-050 | RF | Pedidos y Cumplimiento | El sistema deberá generar la conciliación diaria de preautorizaciones vencidas sin capt… | R-04 | 2 | Should |  |
| RF-051 | RF | Pedidos y Cumplimiento | El sistema deberá notificar al cliente el cambio de estado de su pedido antes de efectu… | R-04 | 2 | Should |  |
| RF-052 | RF | Pedidos y Cumplimiento | El sistema deberá permitir a todos los actores consultar el estado del pedido desde una… | R-04 | 2 | Should |  |
| RF-053 | RF | Pedidos y Cumplimiento | El sistema deberá permitir marcar como no elegible para cumplimiento digital el stock d… | R-04 | 2 | Should |  |
| RF-054 | RF | Pedidos y Cumplimiento | El sistema debe calcular la base de comisión reconociendo al vendedor y a la tienda de… | R-06 | 2 | Should |  |
| RF-055 | RF | Pedidos y Cumplimiento | El sistema debe condicionar la transmisión de la base de comisión al movimiento real de… | R-06 | 2 | Should |  |
| RF-056 | RF | Pedidos y Cumplimiento | El sistema deberá reasignar el pedido a otro punto de despacho con existencia disponible. | R-03 | 1 | Must | revisar (reserva o pedido) |
| RF-057 | RF | Pedidos y Cumplimiento | El sistema deberá impedir una segunda reasignación del mismo pedido. | R-04 | 2 | Should |  |
| RF-058 | RF | Pedidos y Cumplimiento | El sistema deberá acotar la reasignación a la ventana de tiempo parametrizada. | R-04 | 2 | Should |  |
| RF-059 | RF | Pedidos y Cumplimiento | El sistema deberá ofrecer al cliente un producto equivalente. | R-04 | 2 | Should |  |
| RF-060 | RF | Pedidos y Cumplimiento | El sistema deberá ofrecer al cliente la espera compensada con la compensación parametri… | R-04 | 2 | Should |  |
| RF-061 | RF | Pedidos y Cumplimiento | El sistema deberá ofrecer al cliente la liberacion del pedido con anulación de la preau… | R-04 | 2 | Should |  |
| RF-062 | RF | Pedidos y Cumplimiento | El sistema debe monitorear el tiempo restante de cada pedido respecto de su fecha prome… | R-04 | 2 | Should |  |
| RF-063 | RF | Pedidos y Cumplimiento | El sistema debe priorizar la preparación del pedido al alcanzar el umbral parametrizado… | R-04 | 2 | Should |  |
| RF-064 | RF | Pedidos y Cumplimiento | El sistema debe permitir al cliente no autenticado consultar el precio vigente de una r… | R-04 | 2 | Should |  |
| RF-065 | RF | Pedidos y Cumplimiento | El sistema debe permitir al cliente no autenticado consultar la disponibilidad de la re… | R-04 | 2 | Should |  |
| RF-066 | RF | Pedidos y Cumplimiento | El sistema debe permitir al cliente no autenticado consultar la disponibilidad de la re… | R-04 | 2 | Should |  |
| RF-067 | RF | Pedidos y Cumplimiento | El sistema debe permitir al cliente autenticado consultar sus compras. | R-04 | 2 | Should |  |
| RF-068 | RF | Pedidos y Cumplimiento | El sistema debe permitir al cliente autenticado consultar sus devoluciones. | R-04 | 2 | Should |  |
| RF-069 | RF | Pedidos y Cumplimiento | El sistema debe permitir al cliente autenticado consultar su estado de cuenta. | R-04 | 2 | Should |  |
| RF-070 | RF | Pedidos y Cumplimiento | El sistema debe permitir al cliente autenticado consultar sus documentos. | R-04 | 2 | Should |  |
| RF-071 | RF | Pedidos y Cumplimiento | El sistema deberá calcular la base de comisión considerando el canal de origen y el can… | R-06 | 2 | Should |  |
| RF-072 | RF | Pedidos y Cumplimiento | El sistema debe permitir al ejecutivo de mesón consultar el estado real del pedido. | R-04 | 2 | Should |  |
| RF-073 | RF | Pedidos y Cumplimiento | El sistema debe permitir al ejecutivo de mesón consultar el precio aplicado al pedido. | R-04 | 2 | Should |  |
| RF-074 | RF | Pedidos y Cumplimiento | El sistema debe permitir al ejecutivo de mesón ofrecer al cliente las opciones de resol… | R-04 | 2 | Should |  |
| RF-075 | RF | Pedidos y Cumplimiento | El sistema deberá excluir al centro de distribución de Concepción como origen de promes… | R-04 | 2 | Should |  |
| RF-076 | RF | Pedidos y Cumplimiento | El sistema deberá calcular el costo total de servir de cada punto de despacho candidato… | R-04 | 2 | Should |  |
| RF-077 | RF | Pedidos y Cumplimiento | El sistema deberá seleccionar como punto de despacho aquel de menor costo total de servir. | R-04 | 2 | Should |  |
| RF-078 | RF | Pedidos y Cumplimiento | El sistema deberá registrar el valor de cada término del costo total de servir que fund… | R-04 | 2 | Should |  |
| RF-079 | RF | Pedidos y Cumplimiento | El sistema deberá calcular la fecha prometida de entrega en función del punto de despac… | R-04 | 2 | Should |  |
| RF-080 | RF | Pedidos y Cumplimiento | El sistema deberá impedir la publicación de un plazo fijo de catálogo como fecha promet… | R-04 | 2 | Should |  |
| RF-081 | RF | Pedidos y Cumplimiento | El sistema deberá calcular el cumplimiento de la promesa de entrega por pedido individual. | R-04 | 2 | Should |  |
| RF-082 | RF | Operación de Tienda | El sistema deberá detectar la pérdida del enlace externo y conmutar automáticamente la… | R-05 | 1 | Must |  |
| RF-083 | RF | Operación de Tienda | El sistema deberá permitir al cajero registrar una venta en modo desconectado. | R-05 | 1 | Must |  |
| RF-084 | RF | Operación de Tienda | El sistema deberá permitir al cajero cobrar la venta en modo desconectado. | R-05 | 1 | Must |  |
| RF-085 | RF | Operación de Tienda | El sistema deberá aplicar las promociones vigentes en modo desconectado, evaluadas segú… | R-05 | 1 | Must | revisar |
| RF-086 | RF | Operación de Tienda | El sistema deberá emitir el documento de venta en contingencia utilizando folios previa… | R-05 | 1 | Must |  |
| RF-087 | RF | Operación de Tienda | El sistema deberá permitir al vendedor consultar la existencia local de la tienda en mo… | R-03 | 1 | Must |  |
| RF-088 | RF | Operación de Tienda | El sistema deberá detectar el restablecimiento del enlace y conmutar la tienda a modo c… | R-05 | 1 | Must |  |
| RF-089 | RF | Operación de Tienda | El sistema deberá permitir el otorgamiento de crédito en modo desconectado exclusivamen… | F-01 | 1 | Must | crédito sin conexión (EXC-16) |
| RF-090 | RF | Operación de Tienda | El sistema deberá aplicar el tope de monto parametrizado a cada operación de crédito cu… | F-01 | 1 | Must | crédito sin conexión (EXC-16) |
| RF-091 | RF | Operación de Tienda | El sistema deberá aplicar el tope parametrizado de número de operaciones de crédito en… | F-01 | 1 | Must | crédito sin conexión (EXC-16) |
| RF-092 | RF | Operación de Tienda | El sistema deberá impedir la apertura de una tarjeta nueva en modo desconectado. | F-01 | 1 | Must | crédito sin conexión (EXC-16) |
| RF-093 | RF | Operación de Tienda | El sistema deberá impedir la ampliación de cupo en modo desconectado. | F-01 | 1 | Must | crédito sin conexión (EXC-16) |
| RF-094 | RF | Operación de Tienda | El sistema deberá marcar la operación como cursada en modo desconectado para su validac… | R-05 | 1 | Must | revisar |
| RF-095 | RF | Operación de Tienda | El sistema debe reconciliar hacia los sistemas centrales la totalidad de las ventas reg… | R-05 | 1 | Must |  |
| RF-096 | RF | Operación de Tienda | El sistema debe reconciliar hacia los sistemas centrales la totalidad de los documentos… | R-05 | 1 | Must |  |
| RF-097 | RF | Operación de Tienda | El sistema deberá procesar la reconciliación de forma idempotente, impidiendo la duplic… | R-05 | 1 | Must |  |
| RF-098 | RF | Operación de Tienda | El sistema deberá resolver el conflicto de existencia comprometida aplicando la regla d… | R-03 | 1 | Must |  |
| RF-099 | RF | Operación de Tienda | El sistema deberá generar un informe de excepciones de la reconciliación, identificando… | R-05 | 1 | Must |  |
| RF-100 | RF | Operación de Tienda | El sistema deberá enrutar la emisión de todo documento tributario hacia el sistema de g… | R-05 | 1 | Must |  |
| RF-101 | RF | Operación de Tienda | El sistema deberá permitir al vendedor de piso consultar la disponibilidad para vender… | R-05 | 1 | Must | revisar |
| OP-06 | OP | Obligación del PROPONENTE | El PROPONENTE debe especificar la cantidad de dispositivos móviles requeridos por tiend… | Gestión del proyecto | Todo el proyecto | Must |  |
| OP-07 | OP | Obligación del PROPONENTE | El PROPONENTE debe especificar las características técnicas de los dispositivos móviles… | Gestión del proyecto | Todo el proyecto | Must |  |
| OP-08 | OP | Obligación del PROPONENTE | El PROPONENTE debe presentar el análisis de hacer o comprar del centro de distribución… | Gestión del proyecto | Todo el proyecto | Must |  |
| OP-09 | OP | Obligación del PROPONENTE | El PROPONENTE debe declarar el impacto de la alternativa seleccionada sobre el cumplimi… | Gestión del proyecto | Todo el proyecto | Must |  |
| RF-102 | RF | Marketplace | El sistema debe permitir al vendedor de marketplace declarar la existencia de sus refer… | R-07 | 2 | Should |  |
| RF-103 | RF | Marketplace | El sistema debe permitir al vendedor de marketplace actualizar la existencia previament… | R-07 | 2 | Should |  |
| RNF-02 | RNF | Disponibilidad | La interfaz de declaración de existencia del vendedor de marketplace debe estar disponi… | Plataforma | 1 | Must |  |
| RF-104 | RF | Marketplace | El sistema deberá registrar cada actualización de existencia declarada con su fecha y h… | R-07 | 2 | Should |  |
| RF-105 | RF | Marketplace | El sistema deberá calcular los indicadores de nivel de servicio por vendedor externo se… | R-07 | 2 | Should |  |
| RF-106 | RF | Marketplace | El sistema deberá notificar al vendedor de marketplace la recepción de la devolución en… | R-07 | 2 | Should |  |
| RF-107 | RF | Marketplace | El sistema deberá permitir al ejecutivo registrar que parte asume el costo de la devolu… | R-07 | 2 | Should |  |
| RF-108 | RF | Marketplace | El sistema deberá permitir al ejecutivo registrar la prestación entregada al cliente (r… | R-07 | 2 | Should |  |
| RF-109 | RF | Marketplace | El sistema deberá publicar únicamente la existencia declarada en la última actualizació… | R-07 | 2 | Should |  |
| RF-110 | RF | Marketplace | El sistema debe permitir al vendedor de marketplace consultar el estado de cada pedido… | R-07 | 2 | Should |  |
| RF-111 | RF | Marketplace | El sistema debe permitir al vendedor de marketplace consultar las devoluciones de sus p… | R-07 | 2 | Should |  |
| RF-112 | RF | Marketplace | El sistema debe permitir al vendedor de marketplace consultar su evaluación de desempeñ… | R-07 | 2 | Should |  |
| RF-113 | RF | Marketplace | El sistema debe identificar visiblemente al vendedor de la unidad en el catálogo, la fi… | R-07 | 2 | Should |  |
| RF-114 | RF | Marketplace | El sistema debe identificar visiblemente a quien despacha la unidad en el catálogo, la… | R-07 | 2 | Should |  |
| RF-115 | RF | Marketplace | El sistema debe mostrar las condiciones de devolución aplicables a la unidad. | R-07 | 2 | Should |  |
| RF-116 | RF | Marketplace | El sistema debe mostrar las condiciones de garantía legal aplicables a la unidad. | R-07 | 2 | Should |  |
| RF-117 | RF | Marketplace | El sistema deberá impedir que un pedido intermediado comprometa existencia propia de la… | R-07 | 2 | Should |  |
| RF-118 | RF | Marketplace | El sistema deberá impedir que una unidad de inventario propio sea asignada al cumplimie… | R-07 | 2 | Should |  |
| RF-119 | RF | Marketplace | El sistema deberá registrar el acuse de conocimiento de las reglas de evaluación por pa… | R-07 | 2 | Should |  |
| RF-120 | RF | Marketplace | El sistema deberá impedir la aplicación de una regla de evaluación a un vendedor que no… | R-07 | 2 | Should |  |
| RF-121 | RF | Marketplace | El sistema deberá determinar la consecuencia escalonada aplicable según la matriz de es… | R-07 | 2 | Should |  |
| RF-122 | RF | Marketplace | El sistema deberá requerir la ejecución de la sanción por el rol nominado en la matriz… | R-07 | 2 | Should |  |
| RF-123 | RF | Marketplace | El sistema deberá registrar la trazabilidad de la sanción aplicada, indicando regla inc… | R-07 | 2 | Should |  |
| RF-124 | RF | Marketplace | El sistema deberá despublicar automáticamente la oferta cuyo stock declarado haya super… | R-07 | 2 | Should |  |
| RF-125 | RF | Marketplace | El sistema deberá calcular e informar al sistema de gestión empresarial la base de comi… | R-07 | 2 | Should |  |
| RF-126 | RF | Marketplace | El sistema deberá notificar al sistema de gestión empresarial la anulación de la base d… | R-07 | 2 | Should |  |
| RF-127 | RF | Inventario y Disponibilidad | El sistema deberá calcular la existencia disponible para vender restando de la existenc… | R-03 | 1 | Must |  |
| RF-128 | RF | Inventario y Disponibilidad | El sistema deberá determinar el valor del colchón de confianza aplicable en función de… | R-03 | 1 | Must |  |
| RF-129 | RF | Inventario y Disponibilidad | El sistema deberá determinar el valor del colchón de confianza aplicable en función del… | R-03 | 1 | Must |  |
| RF-130 | RF | Inventario y Disponibilidad | El sistema deberá registrar la traza del cálculo del disponible, incluyendo el valor de… | R-03 | 1 | Must |  |
| RF-131 | RF | Inventario y Disponibilidad | El sistema deberá permitir parametrizar la frecuencia de conteo cíclico por categoría. | R-03 | 1 | Must |  |
| RF-132 | RF | Inventario y Disponibilidad | El sistema deberá permitir parametrizar el método de conteo por categoría. | R-03 | 1 | Must |  |
| RF-133 | RF | Inventario y Disponibilidad | El sistema deberá permitir parametrizar el criterio de gatillo de recuento extraordinar… | R-03 | 1 | Must |  |
| RF-134 | RF | Inventario y Disponibilidad | El sistema deberá generar la programación de conteos cíclicos según la frecuencia param… | R-03 | 1 | Must |  |
| RF-135 | RF | Inventario y Disponibilidad | El sistema debe permitir registrar el resultado del conteo cíclico. | R-03 | 1 | Must |  |
| RNF-03 | RNF | Desempeño | El registro del conteo cíclico no debe bloquear ni degradar la operación de venta de la… | Plataforma | 1 | Must |  |
| RF-136 | RF | Inventario y Disponibilidad | El sistema deberá señalar automáticamente los pasillos o referencias que requieren recu… | R-03 | 1 | Must |  |
| RF-137 | RF | Inventario y Disponibilidad | El sistema deberá calcular la exactitud de inventario resultante por categoría. | R-03 | 1 | Must |  |
| RF-138 | RF | Inventario y Disponibilidad | El sistema deberá permitir clasificar cada diferencia detectada en uno de los component… | R-02 | 2 | Should |  |
| RF-139 | RF | Inventario y Disponibilidad | El sistema deberá impedir el cierre de un ajuste de inventario que no tenga asignado un… | R-03 | 1 | Must |  |
| RF-140 | RF | Inventario y Disponibilidad | El sistema deberá cuantificar el monto y la proporción de cada componente de merma sobr… | R-03 | 1 | Must |  |
| RF-141 | RF | Inventario y Disponibilidad | El sistema deberá generar el informe mensual de merma cuya suma de componentes sea igua… | R-03 | 1 | Must |  |
| RF-142 | RF | Inventario y Disponibilidad | El sistema deberá exigir al analista comercial completar los atributos obligatorios de… | R-03 | 1 | Must |  |
| RF-143 | RF | Inventario y Disponibilidad | El sistema deberá impedir la publicación de esa referencia en el canal digital mientras… | R-03 | 1 | Must |  |
| RF-144 | RF | Inventario y Disponibilidad | El sistema deberá generar automáticamente la propuesta diaria de reposición utilizando… | R-02 | 2 | Should |  |
| RF-145 | RF | Inventario y Disponibilidad | El sistema deberá permitir al planificador de logística ajustar la propuesta de reposic… | R-02 | 2 | Should |  |
| RF-146 | RF | Inventario y Disponibilidad | El sistema deberá registrar el ajuste realizado indicando usuario, valor propuesto, val… | R-03 | 1 | Must |  |
| RF-147 | RF | Inventario y Disponibilidad | El sistema debe generar un reporte periódico de referencias con atributos obligatorios… | R-03 | 1 | Must |  |
| RF-148 | RF | Inventario y Disponibilidad | El sistema debe generar un reporte periódico de publicaciones fallidas indicando la cau… | R-03 | 1 | Must |  |
| RF-149 | RF | Inventario y Disponibilidad | El sistema debe permitir al gerente de logística definir el valor del colchón de confia… | R-03 | 1 | Must |  |
| RF-150 | RF | Inventario y Disponibilidad | El sistema debe permitir al gerente de logística definir el valor del colchón de confia… | R-03 | 1 | Must |  |
| RF-151 | RF | Inventario y Disponibilidad | El sistema deberá registrar quien definio o modifico el colchón, cuando, el valor anter… | R-03 | 1 | Must |  |
| RF-152 | RF | Inventario y Disponibilidad | El sistema deberá sugerir un valor de referencia del colchón calculado a partir del his… | R-03 | 1 | Must |  |
| RF-153 | RF | Inventario y Disponibilidad | El sistema deberá permitir al vendedor de piso registrar las unidades que ingresan al p… | R-03 | 1 | Must |  |
| RF-154 | RF | Inventario y Disponibilidad | El sistema deberá excluir del disponible para vender las unidades registradas en probador. | R-03 | 1 | Must |  |
| RF-155 | RF | Inventario y Disponibilidad | El sistema debe permitir al vendedor de piso confirmar el reingreso a sala de la unidad… | R-03 | 1 | Must |  |
| RF-156 | RF | Inventario y Disponibilidad | El sistema debe permitir al vendedor de piso registrar la venta de la unidad registrada… | R-03 | 1 | Must |  |
| RF-157 | RF | Inventario y Disponibilidad | El sistema deberá impedir que cualquier canal de venta consuma el saldo bruto de invent… | R-03 | 1 | Must |  |
| RF-158 | RF | Inventario y Disponibilidad | El sistema debe calcular el porcentaje de error probable de la referencia en función de… | R-03 | 1 | Must |  |
| RF-159 | RF | Inventario y Disponibilidad | El sistema debe calcular el porcentaje de error probable de la referencia en función de… | R-03 | 1 | Must |  |
| RF-160 | RF | Inventario y Disponibilidad | El sistema deberá mostrar al cliente el porcentaje de error probable calculado en RF-05… | R-03 | 1 | Must |  |
| RF-161 | RF | Inventario y Disponibilidad | El sistema deberá mostrar al vendedor de piso el porcentaje de error probable calculado… | R-03 | 1 | Must |  |
| RF-162 | RF | Inventario y Disponibilidad | El sistema deberá generar una alerta interna dirigida al rol facultado cuando la exacti… | R-03 | 1 | Must |  |
| RF-163 | RF | Inventario y Disponibilidad | El sistema deberá permitir exclusivamente al rol facultado suspender manualmente la pub… | R-03 | 1 | Must |  |
| RF-164 | RF | Inventario y Disponibilidad | El sistema deberá abstenerse de suspender automáticamente la publicación de una categor… | R-03 | 1 | Must |  |
| RF-165 | RF | Gobernanza de Datos | El sistema deberá registrar cada cruce de información ejecutado entre ámbitos, indicand… | X-01 | 1 | Must |  |
| RF-166 | RF | Gobernanza de Datos | El sistema deberá bloquear todo intento de cruce de información que no corresponda a un… | X-01 | 1 | Must |  |
| RF-167 | RF | Gobernanza de Datos | El sistema deberá registrar el intento de cruce bloqueado con el componente origen, el… | X-01 | 1 | Must |  |
| RF-168 | RF | Gobernanza de Datos | El sistema debe permitir al oficial de cumplimiento mantener el inventario de interface… | X-01 | 1 | Must |  |
| RF-169 | RF | Gobernanza de Datos | El sistema debe impedir el registro de una interfaz de cruce que no declare finalidad,… | X-01 | 1 | Must |  |
| RF-170 | RF | Gobernanza de Datos | El sistema deberá excluir del catálogo de atributos disponibles en el motor de campañas… | X-01 | 1 | Must | revisar (cruce con R-09) |
| RF-171 | RF | Gobernanza de Datos | El sistema deberá rechazar la ejecución de toda facilidad comercial que invoque un atri… | X-01 | 1 | Must |  |
| RF-172 | RF | Gobernanza de Datos | El sistema deberá rechazar la ejecución de todo proceso crediticio que invoque un atrib… | X-01 | 1 | Must |  |
| RF-173 | RF | Gobernanza de Datos | El sistema deberá asignar a la misma persona un identificador distinto en el ámbito ret… | X-01 | 1 | Must |  |
| RF-174 | RF | Gobernanza de Datos | El sistema deberá resolver la correspondencia entre identificadores exclusivamente a tr… | X-01 | 1 | Must |  |
| RF-175 | RF | Gobernanza de Datos | El sistema deberá rechazar la persistencia de la clave del ámbito financiero como colum… | X-01 | 1 | Must |  |
| RF-176 | RF | Gobernanza de Datos | El sistema deberá exigir el registro de la evaluación de impacto sobre la frontera de d… | X-01 | 1 | Must |  |
| RF-177 | RF | Evento de Alta Concurrencia | El sistema debe permitir declarar previamente el orden de degradación de los servicios. | Plataforma | 1 | Must | revisar |
| RF-178 | RF | Evento de Alta Concurrencia | El sistema debe permitir parametrizar los criterios que activan cada nivel de degradaci… | Plataforma | 1 | Must | revisar |
| RF-179 | RF | Evento de Alta Concurrencia | El sistema deberá suspender la publicación de la categoría indicada por el orden de deg… | R-03 | 1 | Must |  |
| RF-180 | RF | Evento de Alta Concurrencia | El sistema deberá reducir el límite de unidades por cliente al valor declarado. | Plataforma | 1 | Must | revisar |
| RF-181 | RF | Evento de Alta Concurrencia | El sistema deberá desactivar temporalmente los medios de pago de mayor fricción operati… | Plataforma | 1 | Must | revisar |
| RF-182 | RF | Evento de Alta Concurrencia | El sistema deberá monitorear en tiempo real la tasa de cancelación por falta de existen… | R-03 | 1 | Must |  |
| RF-183 | RF | Evento de Alta Concurrencia | El sistema deberá activar la acción de degradación declarada para esa categoría en RF-0… | R-03 | 1 | Must |  |
| RF-184 | RF | Evento de Alta Concurrencia | El sistema deberá permitir parametrizar las cinco ventanas de congelamiento (1 nov - 6… | Plataforma | 1 | Must | revisar |
| RF-185 | RF | Evento de Alta Concurrencia | El sistema deberá impedir la ejecución del despliegue o intervención en producción dura… | Plataforma | 1 | Must | revisar |
| RF-186 | RF | Evento de Alta Concurrencia | El sistema deberá registrar el intento de despliegue bloqueado, indicando componente, s… | Plataforma | 1 | Must | revisar |
| RF-187 | RF | Devoluciones y Garantía Legal | El sistema debe permitir al ejecutivo de mesón atender íntegramente el caso de garantía… | R-08 | 2 | Must |  |
| RF-188 | RF | Devoluciones y Garantía Legal | El sistema debe impedir que el flujo de atención exija la derivación del consumidor al… | R-08 | 2 | Should |  |
| RF-189 | RF | Devoluciones y Garantía Legal | El sistema deberá permitir al ejecutivo registrar el motivo de la devolución (talla, co… | R-08 | 2 | Should |  |
| RF-190 | RF | Devoluciones y Garantía Legal | El sistema deberá impedir el reingreso de una unidad devuelta al inventario disponible… | R-08 | 2 | Should |  |
| RF-191 | RF | Devoluciones y Garantía Legal | El sistema deberá permitir al ejecutivo registrar la decisión de aptitud de la unidad d… | R-08 | 2 | Should |  |
| RF-192 | RF | Devoluciones y Garantía Legal | El sistema deberá presentar al ejecutivo las tres opciones de garantía legal (reparació… | R-08 | 2 | Must |  |
| RF-193 | RF | Devoluciones y Garantía Legal | El sistema debe registrar la opción de garantía legal ofrecida al consumidor. | R-08 | 2 | Must |  |
| RF-194 | RF | Devoluciones y Garantía Legal | El sistema debe registrar la opción de garantía legal efectivamente elegida por el cons… | R-08 | 2 | Must |  |
| RF-195 | RF | Devoluciones y Garantía Legal | El sistema deberá permitir parametrizar el plazo de garantía legal por tipo de producto… | R-08 | 2 | Must |  |
| RF-196 | RF | Devoluciones y Garantía Legal | El sistema deberá registrar el hito de resolución al consumidor con su fecha propia. | R-08 | 2 | Should |  |
| RF-197 | RF | Devoluciones y Garantía Legal | El sistema deberá registrar el hito de recuperación contra el tercero responsable con u… | R-08 | 2 | Should |  |
| RF-198 | RF | Devoluciones y Garantía Legal | El sistema deberá impedir que el estado de la recuperación contra el tercero condicione… | R-08 | 2 | Should |  |
| RF-199 | RF | Crédito y Cobranza | El sistema deberá exigir la entrega completa de la información precontractual antes de… | F-03 | 1 | Must |  |
| RF-200 | RF | Crédito y Cobranza | El sistema deberá registrar la versión del documento precontractual entregado. | F-03 | 1 | Must |  |
| RF-201 | RF | Crédito y Cobranza | El sistema deberá registrar el instante de entrega de la información precontractual. | F-03 | 1 | Must |  |
| RF-202 | RF | Crédito y Cobranza | El sistema deberá registrar el instante de aceptación del cliente. | F-03 | 1 | Must |  |
| RF-203 | RF | Crédito y Cobranza | El sistema deberá registrar el medio por el cual se entrego y se aceptó la información… | F-03 | 1 | Must |  |
| RF-204 | RF | Crédito y Cobranza | El sistema deberá registrar el contenido exacto aceptado por el cliente o su huella de… | F-03 | 1 | Must |  |
| RF-205 | RF | Crédito y Cobranza | El sistema deberá dejar constancia expresa de que el cliente recibió la información ant… | F-03 | 1 | Must |  |
| RF-206 | RF | Crédito y Cobranza | El sistema deberá impedir el registro de la aceptación del crédito mientras no exista a… | F-03 | 1 | Must |  |
| RF-207 | RF | Crédito y Cobranza | El sistema deberá registrar la evidencia del consentimiento expreso e informado del cli… | F-03 | 1 | Must |  |
| RF-208 | RF | Crédito y Cobranza | El sistema deberá impedir el registro de una modificacion de condiciones del crédito qu… | F-03 | 1 | Must |  |
| RF-209 | RF | Crédito y Cobranza | El sistema deberá reconstruir el acto de consentimiento presentando que se informó, en… | F-03 | 1 | Must |  |
| RF-210 | RF | Crédito y Cobranza | El sistema deberá restaurar desde archivo frío los antecedentes de una operación de cré… | F-01 | 1 | Must |  |
| RF-211 | RF | Crédito y Cobranza | El sistema debe permitir al ejecutivo de cobranza iniciar una gestión de cobranza. | F-02 | 1 (ola 1) y 2 (ola 2) | Must |  |
| RF-212 | RF | Crédito y Cobranza | El sistema debe registrar la gestión de cobranza ejecutada con su medio, su instante y… | F-02 | 1 (ola 1) y 2 (ola 2) | Must |  |
| RF-213 | RF | Crédito y Cobranza | El sistema debe impedir la ejecución de una gestión de cobranza fuera de los límites no… | F-02 | 1 (ola 1) y 2 (ola 2) | Must |  |
| RF-214 | RF | Crédito y Cobranza | El sistema debe enlazar el expediente de la repactación con la gestión de cobranza que… | F-03 | 1 | Must |  |
| RF-215 | RF | Crédito y Cobranza | El sistema debe enlazar el expediente de la repactación con la evidencia de consentimie… | F-03 | 1 | Must |  |
| RF-216 | RF | Crédito y Cobranza | El sistema deberá generar un reporte de conciliación diaria de saldos durante todo el p… | F-02 | 1 (ola 1) y 2 (ola 2) | Must |  |
| RF-217 | RF | Crédito y Cobranza | El sistema deberá permitir al cliente no autenticado consultar la información precontra… | F-03 | 1 | Must |  |
| RF-218 | RF | Crédito y Cobranza | El sistema deberá permitir al cliente no autenticado utilizar un simulador de costo tot… | F-01 | 1 | Must |  |
| RF-219 | RF | Crédito y Cobranza | El sistema deberá mantener cargada la Tasa Máxima Convencional vigente por tipo y tramo… | F-01 | 1 | Must | revisar |
| RF-220 | RF | Crédito y Cobranza | El sistema deberá impedir la originación de una operación cuya tasa supere la Tasa Máxi… | F-01 | 1 | Must |  |
| RF-221 | RF | Crédito y Cobranza | El sistema deberá determinar el cupo exclusivamente a partir de las variables de la eva… | F-02 | 1 (ola 1) y 2 (ola 2) | Must |  |
| RF-222 | RF | Crédito y Cobranza | El sistema deberá excluir el monto de la venta en curso del conjunto de variables de as… | F-01 | 1 | Must |  |
| RF-223 | RF | Crédito y Cobranza | El sistema deberá excluir la solicitud del vendedor del conjunto de variables de asigna… | F-01 | 1 | Must |  |
| RF-224 | RF | Crédito y Cobranza | El sistema deberá impedir al vendedor alterar el resultado de una evaluación crediticia. | F-01 | 1 | Must |  |
| RF-225 | RF | Crédito y Cobranza | El sistema deberá impedir la repetición de la evaluación crediticia del mismo cliente d… | F-01 | 1 | Must |  |
| RF-226 | RF | Crédito y Cobranza | El sistema deberá registrar cada intento de evaluación con la identidad del solicitante… | F-01 | 1 | Must |  |
| RNF-04 | RNF | Consistencia de datos | El estado de un pedido no debe presentar discrepancias entre canales de consulta. | Plataforma | 1 | Must |  |
| RNF-05 | RNF | Desempeño | La actualización del estado de un pedido debe reflejarse en todos los puntos de consult… | Plataforma | 1 | Must |  |
| RNF-06 | RNF | Desempeño | El tiempo de evaluación de una solicitud de crédito en el punto de venta físico no debe… | Plataforma | 1 | Must |  |
| RNF-07 | RNF | Desempeño / Cumplimiento | El tiempo total de originación de crédito en el mesón, con información precontractual a… | Plataforma | 1 | Must |  |
| RNF-08 | RNF | Portabilidad / Migración | La migración de la cartera de crédito viva no debe generar pérdida de datos. | Plataforma | 1 | Must |  |
| RNF-09 | RNF | Portabilidad / Migración | La migración de la cartera de crédito viva no debe interrumpir el servicio de cobro. | Plataforma | 1 | Must |  |
| RNF-10 | RNF | Portabilidad / Migración | La migración de la cartera de crédito viva no debe producir divergencia de saldos. | Plataforma | 1 | Must |  |
| RNF-11 | RNF | Seguridad / Arquitectura | La separación lógica entre los datos del retail y los del negocio financiero debe estar… | Plataforma | 1 | Must |  |
| RNF-12 | RNF | Seguridad / Arquitectura | La separación lógica entre ambos ámbitos debe estar documentada. | Plataforma | 1 | Must |  |
| RNF-13 | RNF | Seguridad / Arquitectura | La separación lógica entre ambos ámbitos debe ser verificada por auditoría independiente. | Plataforma | 1 | Must |  |
| RNF-14 | RNF | Seguridad / Arquitectura | La separación física entre la infraestructura del retail y la de la filial emisora debe… | Plataforma | 1 | Must |  |
| RNF-15 | RNF | Auditabilidad | Toda acción relevante ejecutada en el sistema debe quedar registrada indicando usuario… | Plataforma | 1 | Must |  |
| RNF-16 | RNF | Desempeño | La consulta de disponibilidad en la ficha de producto del canal digital debe responder… | Plataforma | 1 | Must |  |
| RNF-17 | RNF | Desempeño | La confirmación de un pedido durante el evento anual debe completarse dentro del umbral… | Plataforma | 1 | Must |  |
| RNF-18 | RNF | Desempeño | La venta completa en caja con medio de pago externo debe completarse dentro del umbral… | Plataforma | 1 | Must |  |
| RNF-19 | RNF | Desempeño | La propagación de un cambio de precio a las 380 líneas de caja y al canal digital debe… | Plataforma | 1 | Must |  |
| RNF-20 | RNF | Desempeño | El registro de una devolución en el mesón debe completarse dentro del umbral definido. | Plataforma | 1 | Must |  |
| RNF-21 | RNF | Desempeño | La consulta de disponibilidad desde una terminal compartida del piso de venta debe resp… | Plataforma | 1 | Must |  |
| RNF-22 | RNF | Desempeño / Capacidad | La plataforma debe soportar la concurrencia y el volumen del peak digital del evento an… | Plataforma | 1 | Must |  |
| RNF-23 | RNF | Desempeño / Capacidad | La plataforma debe soportar la concurrencia y el volumen del peak presencial de la camp… | Plataforma | 1 | Must |  |
| RNF-24 | RNF | Disponibilidad | Una tienda debe poder operar sin enlace externo durante el período mínimo definido. | Plataforma | 1 | Must |  |
| RNF-25 | RNF | Disponibilidad | El centro de distribución principal debe poder operar sin enlace externo durante el per… | Plataforma | 1 | Must |  |
| RNF-26 | RNF | Disponibilidad | La sincronización tras la reconexión no debe superar el plazo definido. | Plataforma | 1 | Must |  |
| RNF-27 | RNF | Disponibilidad | La sincronización tras la reconexión no debe producir pérdida de ventas ni de documentos. | Plataforma | 1 | Must |  |
| RNF-28 | RNF | Disponibilidad | La operación desconectada autónoma on-premise debe sostenerse durante el período mínimo… | Plataforma | 1 | Must |  |
| RNF-29 | RNF | Disponibilidad | La operación de tiendas y centros de distribución debe estar disponible en la ventana h… | Plataforma | 1 | Must |  |
| RNF-30 | RNF | Disponibilidad | El canal digital debe estar disponible de forma continua. | Plataforma | 1 | Must |  |
| RNF-31 | RNF | Disponibilidad | Los servicios financieros que afectan pagos, estados de cuenta y bloqueo de tarjetas de… | Plataforma | 1 | Must |  |
| RNF-32 | RNF | Recuperabilidad | La solución debe cumplir los objetivos de recuperación ante desastre exigidos. | Plataforma | 1 | Must |  |
| RNF-33 | RNF | Seguridad | Los datos de identificación de clientes, la cartera de crédito, el comportamiento de pa… | Plataforma | 1 | Must |  |
| RNF-34 | RNF | Seguridad | Los datos de medios de pago no deben almacenarse en claro, sino tokenizarse. | Plataforma | 1 | Must |  |
| RNF-35 | RNF | Seguridad | La red de cajas, la administrativa, la de videovigilancia y la inalámbrica de clientes… | Plataforma | 1 | Must |  |
| RNF-36 | RNF | Seguridad | La red y el ámbito de sistemas de la filial emisora deben estar separados de forma acre… | Plataforma | 1 | Must |  |
| RNF-37 | RNF | Seguridad | Debe existir segregación de funciones verificable entre originación, aprobación, modifi… | Plataforma | 1 | Must |  |
| RNF-38 | RNF | Auditabilidad | Debe registrarse todo acceso a la cartera de crédito, al comportamiento de pago y a los… | Plataforma | 1 | Must |  |
| RNF-39 | RNF | Seguridad / Cumplimiento | Los actos de crédito de apertura de tarjeta y de repactación deben contar con un mecani… | Plataforma | 1 | Must |  |
| RNF-40 | RNF | Seguridad / Cumplimiento | La conformidad de recepción de mercadería y la constancia de devolución deben contar co… | Plataforma | 1 | Must |  |
| RNF-41 | RNF | Cumplimiento | Los documentos tributarios y antecedentes de venta deben conservarse por el plazo defin… | Plataforma | 1 | Must |  |
| RNF-42 | RNF | Cumplimiento | Los antecedentes del crédito deben conservarse por el plazo del crédito más el período… | Plataforma | 1 | Must |  |
| RNF-43 | RNF | Cumplimiento | La evidencia de consentimiento de originación y repactación debe conservarse por el mis… | Plataforma | 1 | Must |  |
| RNF-44 | RNF | Cumplimiento | La trazabilidad del precio publicado debe conservarse por el plazo definido. | Plataforma | 1 | Must |  |
| RNF-45 | RNF | Cumplimiento | Los movimientos de inventario y conteos cíclicos deben conservarse por el plazo definido. | Plataforma | 1 | Must |  |
| RNF-46 | RNF | Cumplimiento | Los datos de fidelización deben conservarse por el plazo definido. | Plataforma | 1 | Must |  |
| RNF-47 | RNF | Cumplimiento | Los registros de videovigilancia deben conservarse por el plazo definido. | Plataforma | 1 | Must |  |
| RNF-48 | RNF | Portabilidad / Escalabilidad | La solución debe admitir la apertura de una tienda nueva por parametrización, sin desar… | Plataforma | 1 | Must |  |
| RNF-49 | RNF | Usabilidad | Las interfaces de sala, caja y mesón financiero deben ser operables por personal recién… | Plataforma | 1 | Must |  |
| RNF-50 | RNF | Usabilidad / Cumplimiento | Toda comunicación relativa al crédito debe cumplir criterios verificables de lenguaje c… | Plataforma | 1 | Must |  |
| RNF-51 | RNF | Operabilidad | Las notificaciones definidas funcionalmente deben emitirse y registrarse en el 100% de… | Plataforma | 1 | Must |  |
| RNF-52 | RNF | Interoperabilidad | La solución debe adoptar un estándar identificado y justificado para el catálogo e iden… | Plataforma | 1 | Must |  |
| RNF-53 | RNF | Interoperabilidad | La solución debe adoptar un estándar identificado y justificado para el intercambio de… | Plataforma | 1 | Must |  |
| RNF-54 | RNF | Interoperabilidad | La solución debe adoptar un estándar identificado y justificado para el intercambio con… | Plataforma | 1 | Must |  |
| RNF-55 | RNF | Interoperabilidad | La solución debe adoptar un estándar identificado y justificado para la sincronización… | Plataforma | 1 | Must |  |
| RNF-56 | RNF | Interoperabilidad | La solución debe adoptar el formato normativo vigente de documento tributario electrónico. | Plataforma | 1 | Must |  |
| RNF-57 | RNF | Auditabilidad / Desempeño | La evidencia completa de consentimiento de una operación arbitraria debe recuperarse de… | Plataforma | 1 | Must |  |
| RNF-58 | RNF | Desempeño | La recuperación del precio publicado de una referencia en una fecha, hora y canal arbit… | Plataforma | 1 | Must |  |
| RNF-59 | RNF | Seguridad | La revocación total de accesos de un trabajador debe completarse dentro del plazo máxim… | Plataforma | 1 | Must |  |
| RNF-60 | RNF | Usabilidad / Desempeño | El traspaso de sesión nominativa en una terminal compartida debe completarse dentro del… | Plataforma | 1 | Must |  |
| RNF-61 | RNF | Efectividad de negocio | La tasa de cancelación de pedidos por falta de existencia no debe superar el umbral com… | Plataforma | 1 | Must |  |
| RNF-62 | RNF | Efectividad de negocio | El cumplimiento de la promesa de entrega publicada debe alcanzar el umbral comprometido… | Plataforma | 1 | Must |  |
| RNF-63 | RNF | Efectividad de negocio | La diferencia de inventario por categoría debe reducirse al umbral comprometido. | Plataforma | 1 | Must |  |
| RNF-64 | RNF | Operabilidad | El tiempo entre la detección de un quiebre y el aviso al cliente no debe superar el obj… | Plataforma | 1 | Must |  |
| RNF-65 | RNF | Operabilidad | No debe mantenerse un cobro capturado sobre un pedido declarado no cumplible. | Plataforma | 1 | Must |  |
| RNF-66 | RNF | Operabilidad | La latencia entre la recepción física de una devolución en tienda y la notificación al… | Plataforma | 1 | Must |  |
| RNF-67 | RNF | Operabilidad | No debe permanecer mercadería de marketplace en bodega sin aviso a su propietario. | Plataforma | 1 | Must |  |
| RNF-68 | RNF | Recuperabilidad | La restauración desde archivo frío de una operación de crédito de la cohorte más antigu… | Plataforma | 1 | Must |  |
| RNF-69 | RNF | Cumplimiento | La atención de garantía legal en mesón no debe derivar al consumidor a un tercero como… | Plataforma | 1 | Must |  |
| RNF-70 | RNF | Seguridad / DevSecOps | El ciclo de desarrollo debe producir un inventario de componentes (SBOM) por artefacto… | Plataforma | 1 | Must |  |
| RNF-71 | RNF | Seguridad / DevSecOps | La cadena de suministro de software debe alcanzar el nivel SLSA 3 o superior. | Plataforma | 1 | Must |  |
| RNF-72 | RNF | Seguridad / DevSecOps | La capa expuesta debe cumplir el estándar OWASP ASVS en el nivel comprometido. | Plataforma | 1 | Must |  |
| RNF-73 | RNF | Seguridad / DevSecOps | La arquitectura debe implementar un modelo Zero Trust conforme a NIST SP 800-207. | Plataforma | 1 | Must |  |
| RNF-74 | RNF | Cumplimiento | Todo tratamiento de datos personales debe declarar su finalidad. | Plataforma | 1 | Must |  |
| RNF-75 | RNF | Cumplimiento | Todo tratamiento de datos personales debe invocar una de las bases de licitud de la Ley… | Plataforma | 1 | Must |  |
| RNF-76 | RNF | Cumplimiento | La compañía debe mantener el registro de actividades de tratamiento de datos personales. | Plataforma | 1 | Must |  |
