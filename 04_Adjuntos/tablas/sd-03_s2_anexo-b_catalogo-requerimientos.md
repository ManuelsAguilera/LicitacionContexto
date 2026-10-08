# Anexo B del Subdocumento 3. Catálogo de requerimientos clasificado

Fuente del anexo que acompaña al Subdocumento 3 (Esquema de solución y alcance). Se entrega como documento aparte, `OnlySimpleSolutions-Subdocumento3-Anexos`, según el Comunicado 10. El cuerpo del subdocumento (subsección 3.2.4) resume este catálogo y remite a este anexo. Los nombres de los servicios son los vigentes en el cuerpo (`80_Artefactos/sd-03_contexto/divisiones_negocio_servicios_sd-03.md`). Fecha: 2026-10-08. Estado: borrador por revisar. Generado con un script a partir de `01_Requerimientos/RequerimientosAtomizados_Depuracion_Alcance.xlsx` (hoja `1_Catalogo_Atomico`) y de las decisiones de depuración y de clasificación registradas en `80_Artefactos/sd-03_contexto/conciliacion_catalogo.md`. Si este anexo y el Excel difieren, manda el Excel.

El catálogo de 307 filas que resume el capítulo 2 (223 requerimientos funcionales, 75 no funcionales y 9 obligaciones del proponente) queda, tras la depuración de alcance, en **303 filas** (sección B.2). A ellas se suman **5 requerimientos funcionales nuevos** para el servicio de clientes Retail, que no tenía ninguno (RF-227 a RF-231, sección B.2). El catálogo vigente tiene **308 filas**: **227 requerimientos funcionales (RF), 72 no funcionales (RNF) y 9 obligaciones del proponente (OP)**. Las reglas de negocio que el catálogo cita como «propuesta» se identifican RN-P01 a RN-P05 y están en el Anexo C.

## B.1 Resumen

**Por tipo y etapa.** Los requerimientos no funcionales se asignan a la etapa del servicio que miden.

| Etapa | RF | RNF | OP |
| :-- | --: | --: | --: |
| 1 | 142 | 61 | 0 |
| 1 y 2 | 4 | 0 | 0 |
| 2 | 81 | 11 | 0 |
| Todo el proyecto | 0 | 0 | 9 |
| **Total** | **227** | **72** | **9** |

**Por tipo y prioridad.** Alta corresponde a MoSCoW «Must» y Media a «Should».

| Prioridad | RF | RNF | OP |
| :-- | --: | --: | --: |
| Alta | 152 | 72 | 9 |
| Media | 75 | 0 | 0 |

**Requerimientos funcionales por servicio.**

| Código | Servicio | RF | Etapa |
| :-- | :-- | --: | :-- |
| R:M-01 | Servicio de oferta comercial | 20 | 1 |
| R:M-02 | Servicio de abastecimiento | 3 | 2 |
| R:M-03 | Servicio de existencias | 48 | 1 |
| R:V-01 | Servicio de pedidos | 31 | 2 |
| R:V-02 | Servicio de ventas | 14 | 1 |
| R:V-03 | Servicio de comisiones | 3 | 2 |
| R:V-04 | Servicio de marketplace | 25 | 2 |
| R:CL-01 | Servicio de posventa | 12 | 2 |
| R:CL-02 | Servicio de clientes Retail | 5 | 2 |
| F:C-01 | Servicio de originación de crédito | 14 | 1 |
| F:C-02 | Servicio de cartera de crédito | 6 | 1 y 2 |
| F:C-03 | Servicio de evidencia financiera | 15 | 1 |
| X-01 | Servicio de control de cruces | 12 | 1 |
| — | Base tecnológica | 19 | 1 |
| | **Total** | **227** | |

Los servicios de abastecimiento, comisiones y cartera de crédito tienen pocos requerimientos funcionales. Es un tema de completitud del catálogo que queda como pendiente al llenar el Formulario T-12.

## B.2 Depuración de alcance y requerimientos agregados

Decisiones sobre las 28 propuestas de la hoja `7_Depuracion_Alcance`, tomadas con el alcance concretado en la subsección 3.2.3 (exclusiones EXC-02, EXC-03, EXC-05 y EXC-13, supuestos y plan alternativo del crédito) y con los criterios de aceptación de la subsección 3.2.5.

| ID | Propuesta | Decisión | Fundamento |
| :-- | :-- | :-- | :-- |
| RF-025 | Eliminar | Eliminado (ya fuera del catálogo vigente) | Presupone etiquetas electrónicas, excluidas por EXC-02. |
| RF-026 | Eliminar | Eliminado (ya fuera del catálogo vigente) | Presupone etiquetas electrónicas, excluidas por EXC-02. |
| RF-031 | Eliminar | Eliminado (ya fuera del catálogo vigente) | Presupone etiquetas electrónicas, excluidas por EXC-02. |
| RNF-01 | Eliminar | Eliminado (ya fuera del catálogo vigente) | Presupone etiquetas electrónicas, excluidas por EXC-02. |
| RF-027 | Eliminar | Eliminado | Presupone etiquetas electrónicas, excluidas por EXC-02 (solo se evalúa, especifica y costea la alternativa). |
| OP-01 | Trasladar | Mantenida como obligación del proponente | No es función del sistema: es una obligación de la oferta sobre etiquetas electrónicas (EXC-02). |
| OP-02 | Trasladar | Mantenida como obligación del proponente | No es función del sistema: es una obligación de la oferta sobre etiquetas electrónicas (EXC-02). |
| OP-03 | Trasladar | Mantenida como obligación del proponente | No es función del sistema: es una obligación de la oferta sobre etiquetas electrónicas (EXC-02). |
| OP-04 | Trasladar | Mantenida como obligación del proponente | No es función del sistema: es una obligación de la oferta sobre etiquetas electrónicas (EXC-02). |
| OP-05 | Trasladar | Mantenida como obligación del proponente | No es función del sistema: es una obligación de la oferta sobre etiquetas electrónicas (EXC-02). |
| OP-06 | Trasladar | Mantenida como obligación del proponente | No es función del sistema: es una obligación de la oferta sobre dispositivos móviles (EXC-03). |
| OP-07 | Trasladar | Mantenida como obligación del proponente | No es función del sistema: es una obligación de la oferta sobre dispositivos móviles (EXC-03). |
| OP-08 | Trasladar | Mantenida como obligación del proponente | No es función del sistema: es una obligación de la oferta sobre centro de distribución de Concepción (EXC-13). |
| OP-09 | Trasladar | Mantenida como obligación del proponente | No es función del sistema: es una obligación de la oferta sobre centro de distribución de Concepción (EXC-13). |
| RF-071 | Consolidar | Mantenido | EXC-05 exige calcular la base de comisión entre canales. RF-054 reconoce al vendedor y a la tienda de origen pero no considera el canal de cumplimiento, y RF-071 es el enunciado más específico. |
| RNF-61 | Reclasificar | Reclasificado a criterio de aceptación | Meta de negocio (tasa de cancelación) que depende también de la operación del cliente. Se trata como resultado del capítulo 18 en la subsección 3.2.5. La hoja `3_Hallazgos_v3` (H-21) las conservaba como efectividad de negocio. Se reclasifican por la hoja 7 y porque son resultados del capítulo 18 compartidos con la operación del cliente. |
| RNF-62 | Reclasificar | Reclasificado a criterio de aceptación | Meta de negocio (cumplimiento de la promesa de entrega). Se trata en la subsección 3.2.5. La hoja `3_Hallazgos_v3` (H-21) las conservaba como efectividad de negocio. Se reclasifican por la hoja 7 y porque son resultados del capítulo 18 compartidos con la operación del cliente. |
| RNF-63 | Reclasificar | Reclasificado a criterio de aceptación | Meta de negocio (exactitud de inventario). Se trata en la subsección 3.2.5. La hoja `3_Hallazgos_v3` (H-21) las conservaba como efectividad de negocio. Se reclasifican por la hoja 7 y porque son resultados del capítulo 18 compartidos con la operación del cliente. |
| RF-153 | Revisar | Mantenido | Mantenido: las unidades en probador son una causa de la imprecisión del registro (causa C1 del capítulo 2). |
| RF-154 | Revisar | Mantenido | Mantenido: las unidades en probador son una causa de la imprecisión del registro (causa C1 del capítulo 2). |
| RF-155 | Revisar | Mantenido | Mantenido: las unidades en probador son una causa de la imprecisión del registro (causa C1 del capítulo 2). |
| RF-156 | Revisar | Mantenido | Mantenido: las unidades en probador son una causa de la imprecisión del registro (causa C1 del capítulo 2). |
| RNF-46 | Revisar | Mantenido | Tenía un servicio dueño ausente. Pasa al servicio de clientes Retail, que gobierna los datos de fidelización (EXC-15). |
| RF-170 | Revisar | Mantenido | Control de frontera en el servicio de control de cruces, junto con RF-171. |
| RF-089 | Condicionar | Mantenido con marca de dependencia | Depende de los topes de la filial emisora y de la prueba de factibilidad del crédito sin conexión (subsección 3.2.3). |
| RF-090 | Condicionar | Mantenido con marca de dependencia | Depende de los topes de la filial emisora y de la prueba de factibilidad del crédito sin conexión (subsección 3.2.3). |
| RF-091 | Condicionar | Mantenido con marca de dependencia | Depende de los topes de la filial emisora y de la prueba de factibilidad del crédito sin conexión (subsección 3.2.3). |
| RF-094 | Condicionar | Mantenido con marca de dependencia | Depende de los topes de la filial emisora y de la prueba de factibilidad del crédito sin conexión (subsección 3.2.3). |

**Requerimientos agregados.** El servicio de clientes Retail no tenía ningún requerimiento funcional propio. Se proponen cinco, derivados de lo que el servicio incluye según la nomenclatura vigente (deduplicación de clientes, puntos, segmentos y campañas), de la regla RN-03 y de EXC-15 (el sistema de fidelización se conserva y se integra al servicio). La identificación del cliente por ámbito ya existe en RF-173. Quedan marcados «Propuesto por el proponente» y se validan en el período de consultas.

| ID | Requerimiento | Deriva de |
| :-- | :-- | :-- |
| RF-227 | El sistema deberá consolidar en un único registro retail los registros duplicados de un mismo cliente. | — |
| RF-228 | El sistema deberá registrar cada movimiento de puntos de fidelización de un cliente. | — |
| RF-229 | El sistema deberá construir los segmentos de clientes del retail exclusivamente con atributos comerciales. | RN-03, RN-05 |
| RF-230 | El sistema deberá ejecutar campañas sobre los segmentos de clientes del retail. | — |
| RF-231 | El sistema deberá sincronizar con el sistema de fidelización conservado los datos de fidelización del cliente. | — |

Nueve filas del catálogo previo conservan el valor «??» en la columna de revisión (hallazgo H-19 del Excel). No se confirman: se tratan como riesgo de requisitos no validados y se llevan al período de consultas.

## B.3 Requerimientos funcionales (RF)

| ID | Requerimiento | Código | Servicio | Etapa | Prioridad | RN vinculada | Nota |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| RF-001 | El sistema deberá permitir la venta física de la unidad aunque exista una reserva temporal activa en el canal digital. | R:V-02 | Servicio de ventas | 1 | Alta | RN-10 | — |
| RF-002 | El sistema deberá exigir credenciales individuales al usuario antes de habilitar cualquier acción. | — | Base tecnológica | 1 | Alta | RN-50, RN-52 | — |
| RF-003 | El sistema debe impedir el acceso anónimo a una terminal. | — | Base tecnológica | 1 | Alta | RN-50, RN-52 | — |
| RF-004 | El sistema debe impedir el acceso mediante credencial compartida. | — | Base tecnológica | 1 | Alta | RN-50, RN-52 | — |
| RF-005 | El sistema deberá permitir el traspaso de sesión nominativa entre usuarios en una terminal compartida. | — | Base tecnológica | 1 | Alta | RN-50 | — |
| RF-006 | El sistema deberá cerrar automáticamente la sesión por inactividad en la terminal compartida. | — | Base tecnológica | 1 | Alta | RN-50 | — |
| RF-007 | El sistema deberá impedir la ejecución de la función de originación a un usuario sin capacitación normativa acreditada y vigente. | — | Base tecnológica | 1 | Alta | RN-53 | — |
| RF-008 | El sistema deberá impedir la ejecución de la función de repactación a un usuario sin capacitación normativa acreditada y vigente. | — | Base tecnológica | 1 | Alta | RN-53 | — |
| RF-009 | El sistema deberá revocar automáticamente la habilitación funcional del usuario al vencer su acreditación de capacitación. | — | Base tecnológica | 1 | Alta | RN-53, RN-52 | — |
| RF-010 | El sistema deberá permitir al proveedor patrocinar la habilitación temporal de acceso de su repositor externo, con fecha de término declarada. | — | Base tecnológica | 1 | Alta | RN-51 | — |
| RF-011 | El sistema deberá caducar automáticamente la habilitación de acceso del personal externo al cumplirse su vigencia. | — | Base tecnológica | 1 | Alta | RN-51 | — |
| RF-012 | El sistema deberá registrar de forma individualizada el acceso y la actividad del personal externo. | — | Base tecnológica | 1 | Alta | RN-51 | — |
| RF-013 | El sistema deberá revocar la totalidad de los accesos y credenciales del trabajador a partir del término efectivo de su vínculo. | — | Base tecnológica | 1 | Alta | RN-52 | — |
| RF-014 | El sistema debe conciliar los accesos vigentes contra la nómina activa. | — | Base tecnológica | 1 | Alta | RN-52, RN-51 | — |
| RF-015 | El sistema debe informar al oficial de seguridad los accesos huérfanos detectados en la conciliación. | — | Base tecnológica | 1 | Alta | RN-52, RN-51 | — |
| RF-016 | El sistema deberá propagar el cambio de precio a las 380 líneas de caja. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-16, RN-18 | — |
| RF-017 | El sistema deberá propagar el cambio de precio al canal digital. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-16, RN-17 | — |
| RF-018 | El sistema deberá propagar el cambio de precio a los puntos de exhibición física de cada tienda afectada. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-18, RN-19 | — |
| RF-019 | El sistema deberá permitir al reponedor registrar la referencia y la tienda de la etiqueta cambiada, con el instante del cambio. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-19 | — |
| RF-020 | El sistema deberá registrar la identidad individual del ejecutor del cambio de etiqueta. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-19, RN-50 | — |
| RF-021 | El sistema deberá permitir al ejecutivo de cumplimiento recuperar el precio publicado de una referencia para una fecha, hora y canal determinados. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-17 | — |
| RF-022 | El sistema deberá obtener el precio vigente de la referencia según el último precio propagado a la etiqueta de esa tienda en la fecha de la venta. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-16, RN-18 | — |
| RF-023 | El sistema deberá cobrar el menor de ambos precios para el consumidor. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-16 | — |
| RF-024 | El sistema deberá generar un registro de incidente de discrepancia de precio consultable. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-16 | — |
| RF-028 | El sistema deberá impedir la venta de la referencia al precio nuevo mientras su punto de exhibición no confirme la actualización, salvo que el artículo se encuentre bloqueado para venta. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-18, RN-16 | — |
| RF-029 | El sistema deberá generar un indicador diario de puntos de exhibición desactualizados con identificación individual de cada punto. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-18 | — |
| RF-030 | El sistema deberá agrupar los cambios de precio de sala en ventanas parametrizadas fuera del horario de atención. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-19 | — |
| RF-032 | El sistema deberá evaluar la vigencia de cada promoción al instante de emisión del documento. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-20 | — |
| RF-033 | El sistema deberá evaluar la aplicabilidad de la promoción según el canal de la venta. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-20 | — |
| RF-034 | El sistema deberá evaluar la aplicabilidad de la promoción según la tienda en que se realiza la venta. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-20 | — |
| RF-035 | El sistema deberá crear una reserva temporal para la unidad agregada al carro. | R:M-03 | Servicio de existencias | 1 | Alta | RN-10 | La reserva es dato del servicio de existencias. |
| RF-036 | El sistema deberá permitir parametrizar el período de vigencia de la reserva temporal. | R:M-03 | Servicio de existencias | 1 | Alta | RN-10 | La reserva es dato del servicio de existencias. |
| RF-037 | El sistema deberá mantener activa la reserva mientras el cliente mantenga actividad, conforme al período parametrizado. | R:M-03 | Servicio de existencias | 1 | Alta | RN-10 | La reserva es dato del servicio de existencias. |
| RF-038 | El sistema deberá impedir que una misma unidad sea comprometida simultáneamente en más de una operación de venta digital. | R:M-03 | Servicio de existencias | 1 | Alta | RN-10, RN-08 | Impedir el doble compromiso de una unidad es parte de la reserva, dato del servicio de existencias. |
| RF-039 | El sistema debe liberar la reserva temporal al expirar su período de vigencia. | R:M-03 | Servicio de existencias | 1 | Alta | RN-10 | La reserva es dato del servicio de existencias. |
| RF-040 | El sistema debe devolver la unidad liberada al disponible para vender. | R:M-03 | Servicio de existencias | 1 | Alta | RN-10 | La reserva es dato del servicio de existencias. |
| RF-041 | El sistema deberá liberar de inmediato la reserva digital de esa unidad, sin esperar la expiración del período. | R:M-03 | Servicio de existencias | 1 | Alta | RN-10 | La reserva es dato del servicio de existencias. |
| RF-042 | El sistema deberá aplicar el período de vigencia de reserva reducido declarado como parámetro para el evento anual. | R:M-03 | Servicio de existencias | 1 | Alta | RN-10, RN-57 | La reserva es dato del servicio de existencias. |
| RF-043 | El sistema deberá preautorizar el medio de pago al aceptar el pedido, sin capturar el cobro. | R:V-01 | Servicio de pedidos | 2 | Media | RN-21 | — |
| RF-044 | El sistema deberá verificar la existencia física real de la unidad en el punto asignado antes de habilitar la captura del cobro. | R:M-03 | Servicio de existencias | 1 | Alta | RN-21 | La reserva es dato del servicio de existencias. |
| RF-045 | El sistema deberá capturar el cobro únicamente al registrarse el evento de confirmación de la preparacion física. | R:V-01 | Servicio de pedidos | 2 | Media | RN-21 | — |
| RF-046 | El sistema deberá determinar automáticamente la alternativa de resolución aplicable según el motor de reglas (cancelar, sustituir, derivar a tercero o entrega diferida). | R:V-01 | Servicio de pedidos | 2 | Media | RN-23 | — |
| RF-047 | El sistema deberá requerir la aceptación explícita del cliente antes de capturar el cobro. | R:V-01 | Servicio de pedidos | 2 | Media | RN-23, RN-21 | — |
| RF-048 | El sistema deberá anular la preautorización de pago del pedido. | R:V-01 | Servicio de pedidos | 2 | Media | RN-21, RN-23 | — |
| RF-049 | El sistema deberá cancelar el pedido registrando el motivo de la cancelación. | R:V-01 | Servicio de pedidos | 2 | Media | RN-23 | — |
| RF-050 | El sistema deberá generar la conciliación diaria de preautorizaciones vencidas sin captura. | R:V-01 | Servicio de pedidos | 2 | Media | RN-21 | — |
| RF-051 | El sistema deberá notificar al cliente el cambio de estado de su pedido antes de efectuar cualquier cobro definitivo. | R:V-01 | Servicio de pedidos | 2 | Media | RN-23 | — |
| RF-052 | El sistema deberá permitir a todos los actores consultar el estado del pedido desde una única fuente de verdad. | R:V-01 | Servicio de pedidos | 2 | Media | RN-23, RN-28 | — |
| RF-053 | El sistema deberá permitir marcar como no elegible para cumplimiento digital el stock de exhibición de las categorías declaradas. | R:V-01 | Servicio de pedidos | 2 | Media | RN-22, RN-08 | — |
| RF-054 | El sistema debe calcular la base de comisión reconociendo al vendedor y a la tienda de origen de la unidad. | R:V-03 | Servicio de comisiones | 2 | Media | RN-54 | — |
| RF-055 | El sistema debe condicionar la transmisión de la base de comisión al movimiento real de inventario verificado en bodega. | R:V-03 | Servicio de comisiones | 2 | Media | RN-54 | — |
| RF-056 | El sistema deberá reasignar el pedido a otro punto de despacho con existencia disponible. | R:V-01 | Servicio de pedidos | 2 | Media | RN-23 | Reasignar el pedido es parte del ciclo del pedido. |
| RF-057 | El sistema deberá impedir una segunda reasignación del mismo pedido. | R:V-01 | Servicio de pedidos | 2 | Media | RN-23 | — |
| RF-058 | El sistema deberá acotar la reasignación a la ventana de tiempo parametrizada. | R:V-01 | Servicio de pedidos | 2 | Media | RN-23 | — |
| RF-059 | El sistema deberá ofrecer al cliente un producto equivalente. | R:V-01 | Servicio de pedidos | 2 | Media | RN-23 | — |
| RF-060 | El sistema deberá ofrecer al cliente la espera compensada con la compensación parametrizada. | R:V-01 | Servicio de pedidos | 2 | Media | RN-23 | — |
| RF-061 | El sistema deberá ofrecer al cliente la liberacion del pedido con anulación de la preautorización. | R:V-01 | Servicio de pedidos | 2 | Media | RN-23, RN-21 | — |
| RF-062 | El sistema debe monitorear el tiempo restante de cada pedido respecto de su fecha prometida de entrega. | R:V-01 | Servicio de pedidos | 2 | Media | RN-24 | — |
| RF-063 | El sistema debe priorizar la preparación del pedido al alcanzar el umbral parametrizado de tiempo restante. | R:V-01 | Servicio de pedidos | 2 | Media | RN-24 | — |
| RF-064 | El sistema debe permitir al cliente no autenticado consultar el precio vigente de una referencia. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-17, RN-11 | El precio vigente es dato del servicio de oferta comercial. La consulta pública es parte del portal de la Etapa 1. |
| RF-065 | El sistema debe permitir al cliente no autenticado consultar la disponibilidad de la referencia por tienda. | R:M-03 | Servicio de existencias | 1 | Alta | RN-17, RN-11 | La disponibilidad es dato del servicio de existencias. La consulta pública es parte del portal de la Etapa 1. |
| RF-066 | El sistema debe permitir al cliente no autenticado consultar la disponibilidad de la referencia para despacho. | R:M-03 | Servicio de existencias | 1 | Alta | RN-17, RN-11 | La disponibilidad es dato del servicio de existencias. La consulta pública es parte del portal de la Etapa 1. |
| RF-067 | El sistema debe permitir al cliente autenticado consultar sus compras. | R:V-01 | Servicio de pedidos | 2 | Media | RN-02, RN-04 | — |
| RF-068 | El sistema debe permitir al cliente autenticado consultar sus devoluciones. | R:V-01 | Servicio de pedidos | 2 | Media | RN-02, RN-04 | — |
| RF-069 | El sistema debe permitir al cliente autenticado consultar su estado de cuenta. | F:C-02 | Servicio de cartera de crédito | 2 | Media | RN-02, RN-04 | El estado de cuenta es dato de la filial emisora y la consulta pasa por el control de cruces (RF-165 y RF-174). Portal del cliente de la Etapa 2. |
| RF-070 | El sistema debe permitir al cliente autenticado consultar sus documentos. | F:C-02 | Servicio de cartera de crédito | 2 | Media | RN-02, RN-04 | Los documentos del crédito son datos de la filial emisora y la consulta pasa por el control de cruces (RF-165 y RF-174). Portal del cliente de la Etapa 2. |
| RF-071 | El sistema deberá calcular la base de comisión considerando el canal de origen y el canal de cumplimiento cuando estos difieran. | R:V-03 | Servicio de comisiones | 2 | Media | RN-54 | Mantenido: EXC-05 exige calcular la base de comisión entre canales y RF-054 no considera el canal de cumplimiento. |
| RF-072 | El sistema debe permitir al ejecutivo de mesón consultar el estado real del pedido. | R:V-01 | Servicio de pedidos | 2 | Media | RN-16, RN-23 | — |
| RF-073 | El sistema debe permitir al ejecutivo de mesón consultar el precio aplicado al pedido. | R:V-01 | Servicio de pedidos | 2 | Media | RN-16, RN-23 | — |
| RF-074 | El sistema debe permitir al ejecutivo de mesón ofrecer al cliente las opciones de resolución definidas en RF-059, RF-060 y RF-061. | R:V-01 | Servicio de pedidos | 2 | Media | RN-16, RN-23 | — |
| RF-075 | El sistema deberá excluir al centro de distribución de Concepción como origen de promesa de entrega en el canal digital mientras no este acreditado su sistema de gestión de almacenes. | R:V-01 | Servicio de pedidos | 2 | Media | RN-15 | — |
| RF-076 | El sistema deberá calcular el costo total de servir de cada punto de despacho candidato, incorporando costo logístico, costo de oportunidad de sala y plazo comprometido. | R:V-01 | Servicio de pedidos | 2 | Media | RN-22 | — |
| RF-077 | El sistema deberá seleccionar como punto de despacho aquel de menor costo total de servir. | R:V-01 | Servicio de pedidos | 2 | Media | RN-22 | — |
| RF-078 | El sistema deberá registrar el valor de cada término del costo total de servir que fundamento la seleccion. | R:V-01 | Servicio de pedidos | 2 | Media | RN-22 | — |
| RF-079 | El sistema deberá calcular la fecha prometida de entrega en función del punto de despacho, la capacidad de preparacion y el transportista asignado. | R:V-01 | Servicio de pedidos | 2 | Media | RN-24 | — |
| RF-080 | El sistema deberá impedir la publicación de un plazo fijo de catálogo como fecha prometida de entrega. | R:V-01 | Servicio de pedidos | 2 | Media | RN-24 | — |
| RF-081 | El sistema deberá calcular el cumplimiento de la promesa de entrega por pedido individual. | R:V-01 | Servicio de pedidos | 2 | Media | RN-24 | — |
| RF-082 | El sistema deberá detectar la pérdida del enlace externo y conmutar automáticamente la tienda a modo desconectado. | R:V-02 | Servicio de ventas | 1 | Alta | RN-46 | — |
| RF-083 | El sistema deberá permitir al cajero registrar una venta en modo desconectado. | R:V-02 | Servicio de ventas | 1 | Alta | RN-46 | — |
| RF-084 | El sistema deberá permitir al cajero cobrar la venta en modo desconectado. | R:V-02 | Servicio de ventas | 1 | Alta | RN-46 | — |
| RF-085 | El sistema deberá aplicar las promociones vigentes en modo desconectado, evaluadas según RF-032, RF-033 y RF-034. | R:V-02 | Servicio de ventas | 1 | Alta | RN-46, RN-20 | El punto de venta aplica la promoción con datos del servicio de oferta comercial. |
| RF-086 | El sistema deberá emitir el documento de venta en contingencia utilizando folios previamente asignados por el sistema de gestión empresarial. | R:V-02 | Servicio de ventas | 1 | Alta | RN-46, RN-49 | — |
| RF-087 | El sistema deberá permitir al vendedor consultar la existencia local de la tienda en modo desconectado. | R:M-03 | Servicio de existencias | 1 | Alta | RN-46 | — |
| RF-088 | El sistema deberá detectar el restablecimiento del enlace y conmutar la tienda a modo conectado. | R:V-02 | Servicio de ventas | 1 | Alta | RN-48 | — |
| RF-089 | El sistema deberá permitir el otorgamiento de crédito en modo desconectado exclusivamente contra cupo preaprobado vigente almacenado en caché local. | F:C-01 | Servicio de originación de crédito | 1 | Alta | RN-47 | Condicionado al crédito sin conexión (EXC-16, plan alternativo de la subsección 3.2.3). Si la prueba falla, la función se declara no disponible (RT-03.13). |
| RF-090 | El sistema deberá aplicar el tope de monto parametrizado a cada operación de crédito cursada en modo desconectado. | F:C-01 | Servicio de originación de crédito | 1 | Alta | RN-47 | Condicionado al crédito sin conexión (EXC-16, plan alternativo de la subsección 3.2.3). Si la prueba falla, la función se declara no disponible (RT-03.13). |
| RF-091 | El sistema deberá aplicar el tope parametrizado de número de operaciones de crédito en modo desconectado. | F:C-01 | Servicio de originación de crédito | 1 | Alta | RN-47 | Condicionado al crédito sin conexión (EXC-16, plan alternativo de la subsección 3.2.3). Si la prueba falla, la función se declara no disponible (RT-03.13). |
| RF-092 | El sistema deberá impedir la apertura de una tarjeta nueva en modo desconectado. | F:C-01 | Servicio de originación de crédito | 1 | Alta | RN-47 | Aplica EXC-16: no hay apertura ni ampliación de cupo sin conexión. |
| RF-093 | El sistema deberá impedir la ampliación de cupo en modo desconectado. | F:C-01 | Servicio de originación de crédito | 1 | Alta | RN-47 | Aplica EXC-16: no hay apertura ni ampliación de cupo sin conexión. |
| RF-094 | El sistema deberá marcar la operación como cursada en modo desconectado para su validación posterior. | R:V-02 | Servicio de ventas | 1 | Alta | RN-47, RN-48 | Condicionado al crédito sin conexión (EXC-16, plan alternativo de la subsección 3.2.3). Si la prueba falla, la función se declara no disponible (RT-03.13). |
| RF-095 | El sistema debe reconciliar hacia los sistemas centrales la totalidad de las ventas registradas en modo desconectado. | R:V-02 | Servicio de ventas | 1 | Alta | RN-48 | — |
| RF-096 | El sistema debe reconciliar hacia los sistemas centrales la totalidad de los documentos emitidos en modo desconectado. | R:V-02 | Servicio de ventas | 1 | Alta | RN-48 | — |
| RF-097 | El sistema deberá procesar la reconciliación de forma idempotente, impidiendo la duplicación de ventas o documentos ante reintentos. | R:V-02 | Servicio de ventas | 1 | Alta | RN-48 | — |
| RF-098 | El sistema deberá resolver el conflicto de existencia comprometida aplicando la regla de precedencia declarada, produciendo el mismo resultado ante repetición. | R:M-03 | Servicio de existencias | 1 | Alta | RN-48, RN-08 | — |
| RF-099 | El sistema deberá generar un informe de excepciones de la reconciliación, identificando cada conflicto resuelto y su regla aplicada. | R:V-02 | Servicio de ventas | 1 | Alta | RN-48 | — |
| RF-100 | El sistema deberá enrutar la emisión de todo documento tributario hacia el sistema de gestión empresarial como único emisor. | R:V-02 | Servicio de ventas | 1 | Alta | RN-49 | — |
| RF-101 | El sistema deberá permitir al vendedor de piso consultar la disponibilidad para vender de una referencia. | R:M-03 | Servicio de existencias | 1 | Alta | RN-09, RN-P05 | La disponibilidad para vender es dato del servicio de existencias; la consulta sin conexión usa su copia local. |
| RF-102 | El sistema debe permitir al vendedor de marketplace declarar la existencia de sus referencias. | R:V-04 | Servicio de marketplace | 2 | Media | RN-32 | — |
| RF-103 | El sistema debe permitir al vendedor de marketplace actualizar la existencia previamente declarada. | R:V-04 | Servicio de marketplace | 2 | Media | RN-32 | — |
| RF-104 | El sistema deberá registrar cada actualización de existencia declarada con su fecha y hora. | R:V-04 | Servicio de marketplace | 2 | Media | RN-32 | — |
| RF-105 | El sistema deberá calcular los indicadores de nivel de servicio por vendedor externo según las reglas publicadas. | R:V-04 | Servicio de marketplace | 2 | Media | RN-30 | — |
| RF-106 | El sistema deberá notificar al vendedor de marketplace la recepción de la devolución en el momento en que se registra. | R:V-04 | Servicio de marketplace | 2 | Media | RN-28 | — |
| RF-107 | El sistema deberá permitir al ejecutivo registrar que parte asume el costo de la devolución. | R:V-04 | Servicio de marketplace | 2 | Media | RN-28, RN-33 | — |
| RF-108 | El sistema deberá permitir al ejecutivo registrar la prestación entregada al cliente (reparación, reposición o devolución del precio). | R:V-04 | Servicio de marketplace | 2 | Media | RN-28, RN-29 | — |
| RF-109 | El sistema deberá publicar únicamente la existencia declarada en la última actualización vigente del vendedor. | R:V-04 | Servicio de marketplace | 2 | Media | RN-32 | — |
| RF-110 | El sistema debe permitir al vendedor de marketplace consultar el estado de cada pedido intermediado. | R:V-04 | Servicio de marketplace | 2 | Media | RN-30 | — |
| RF-111 | El sistema debe permitir al vendedor de marketplace consultar las devoluciones de sus pedidos. | R:V-04 | Servicio de marketplace | 2 | Media | RN-30 | — |
| RF-112 | El sistema debe permitir al vendedor de marketplace consultar su evaluación de desempeño vigente. | R:V-04 | Servicio de marketplace | 2 | Media | RN-30 | — |
| RF-113 | El sistema debe identificar visiblemente al vendedor de la unidad en el catálogo, la ficha de producto y el proceso de compra. | R:V-04 | Servicio de marketplace | 2 | Media | RN-P03, RN-25 | — |
| RF-114 | El sistema debe identificar visiblemente a quien despacha la unidad en el catálogo, la ficha de producto y el proceso de compra. | R:V-04 | Servicio de marketplace | 2 | Media | RN-P03, RN-25 | — |
| RF-115 | El sistema debe mostrar las condiciones de devolución aplicables a la unidad. | R:V-04 | Servicio de marketplace | 2 | Media | RN-P03, RN-26 | — |
| RF-116 | El sistema debe mostrar las condiciones de garantía legal aplicables a la unidad. | R:V-04 | Servicio de marketplace | 2 | Media | RN-P03, RN-26 | — |
| RF-117 | El sistema deberá impedir que un pedido intermediado comprometa existencia propia de la compañía. | R:V-04 | Servicio de marketplace | 2 | Media | RN-25 | — |
| RF-118 | El sistema deberá impedir que una unidad de inventario propio sea asignada al cumplimiento de un pedido de marketplace. | R:V-04 | Servicio de marketplace | 2 | Media | RN-25 | — |
| RF-119 | El sistema deberá registrar el acuse de conocimiento de las reglas de evaluación por parte de cada vendedor externo. | R:V-04 | Servicio de marketplace | 2 | Media | RN-30 | — |
| RF-120 | El sistema deberá impedir la aplicación de una regla de evaluación a un vendedor que no tenga acuse de conocimiento previo de esa regla. | R:V-04 | Servicio de marketplace | 2 | Media | RN-30 | — |
| RF-121 | El sistema deberá determinar la consecuencia escalonada aplicable según la matriz de escalamiento parametrizada (advertencia, restricción de publicación, suspensión). | R:V-04 | Servicio de marketplace | 2 | Media | RN-31 | — |
| RF-122 | El sistema deberá requerir la ejecución de la sanción por el rol nominado en la matriz de escalamiento. | R:V-04 | Servicio de marketplace | 2 | Media | RN-31 | — |
| RF-123 | El sistema deberá registrar la trazabilidad de la sanción aplicada, indicando regla incumplida, consecuencia, rol ejecutor e instante. | R:V-04 | Servicio de marketplace | 2 | Media | RN-31 | — |
| RF-124 | El sistema deberá despublicar automáticamente la oferta cuyo stock declarado haya superado el plazo de vigencia sin actualización. | R:V-04 | Servicio de marketplace | 2 | Media | RN-32 | — |
| RF-125 | El sistema deberá calcular e informar al sistema de gestión empresarial la base de comisión de marketplace sobre la venta efectivamente cumplida | R:V-04 | Servicio de marketplace | 2 | Media | RN-33 | — |
| RF-126 | El sistema deberá notificar al sistema de gestión empresarial la anulación de la base de comisión calculada cuando ocurra una devolución o cancelación. | R:V-04 | Servicio de marketplace | 2 | Media | RN-33 | — |
| RF-127 | El sistema deberá calcular la existencia disponible para vender restando de la existencia registrada las reservas vigentes, el comprometido no despachado y el colchón de confianza aplicable. | R:M-03 | Servicio de existencias | 1 | Alta | RN-08, RN-09 | — |
| RF-128 | El sistema deberá determinar el valor del colchón de confianza aplicable en función de la categoría del artículo. | R:M-03 | Servicio de existencias | 1 | Alta | RN-09 | — |
| RF-129 | El sistema deberá determinar el valor del colchón de confianza aplicable en función del punto de existencia. | R:M-03 | Servicio de existencias | 1 | Alta | RN-09 | — |
| RF-130 | El sistema deberá registrar la traza del cálculo del disponible, incluyendo el valor de cada término de la fórmula y la versión de parámetros aplicada. | R:M-03 | Servicio de existencias | 1 | Alta | RN-09 | — |
| RF-131 | El sistema deberá permitir parametrizar la frecuencia de conteo cíclico por categoría. | R:M-03 | Servicio de existencias | 1 | Alta | RN-13 | — |
| RF-132 | El sistema deberá permitir parametrizar el método de conteo por categoría. | R:M-03 | Servicio de existencias | 1 | Alta | RN-13 | — |
| RF-133 | El sistema deberá permitir parametrizar el criterio de gatillo de recuento extraordinario por categoría. | R:M-03 | Servicio de existencias | 1 | Alta | RN-13 | — |
| RF-134 | El sistema deberá generar la programación de conteos cíclicos según la frecuencia parametrizada de cada categoría. | R:M-03 | Servicio de existencias | 1 | Alta | RN-13 | — |
| RF-135 | El sistema debe permitir registrar el resultado del conteo cíclico. | R:M-03 | Servicio de existencias | 1 | Alta | RN-13 | — |
| RF-136 | El sistema deberá señalar automáticamente los pasillos o referencias que requieren recuento extraordinario. | R:M-03 | Servicio de existencias | 1 | Alta | RN-13 | — |
| RF-137 | El sistema deberá calcular la exactitud de inventario resultante por categoría. | R:M-03 | Servicio de existencias | 1 | Alta | RN-13, RN-11 | — |
| RF-138 | El sistema deberá permitir clasificar cada diferencia detectada en uno de los componentes de merma definidos (pérdida física, daño no dado de baja, error de recepción, unidad mal ubicada, devolución mal reintegrada, error de digitación). | R:M-03 | Servicio de existencias | 1 | Alta | RN-12 | Clasificar la merma de un ajuste de inventario es parte del servicio de existencias, igual que RF-139 a RF-141. |
| RF-139 | El sistema deberá impedir el cierre de un ajuste de inventario que no tenga asignado un componente de merma. | R:M-03 | Servicio de existencias | 1 | Alta | RN-12 | — |
| RF-140 | El sistema deberá cuantificar el monto y la proporción de cada componente de merma sobre el total del período. | R:M-03 | Servicio de existencias | 1 | Alta | RN-12 | — |
| RF-141 | El sistema deberá generar el informe mensual de merma cuya suma de componentes sea igual al total registrado en el período. | R:M-03 | Servicio de existencias | 1 | Alta | RN-12 | — |
| RF-142 | El sistema deberá exigir al analista comercial completar los atributos obligatorios de la referencia (categoría, dimensiones, fragilidad, volumen, restricción de despacho) antes de guardar el registro como apto para uso operativo. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-P01 | Los atributos del maestro de artículos son datos del servicio de oferta comercial. |
| RF-143 | El sistema deberá impedir la publicación de esa referencia en el canal digital mientras no cuente con los atributos obligatorios completos. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-P01 | La publicación de la referencia es función del servicio de oferta comercial. |
| RF-144 | El sistema deberá generar automáticamente la propuesta diaria de reposición utilizando el disponible para vender calculado en RF-127. | R:M-02 | Servicio de abastecimiento | 2 | Media | RN-08, RN-09 | — |
| RF-145 | El sistema deberá permitir al planificador de logística ajustar la propuesta de reposición antes de confirmar el envío. | R:M-02 | Servicio de abastecimiento | 2 | Media | RN-09 | — |
| RF-146 | El sistema deberá registrar el ajuste realizado indicando usuario, valor propuesto, valor confirmado e instante. | R:M-02 | Servicio de abastecimiento | 2 | Media | RN-09 | Ajustar la propuesta de reposición es parte del servicio de abastecimiento, igual que RF-144 y RF-145. |
| RF-147 | El sistema debe generar un reporte periódico de referencias con atributos obligatorios incompletos. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-P01 | Los atributos del maestro de artículos son datos del servicio de oferta comercial. |
| RF-148 | El sistema debe generar un reporte periódico de publicaciones fallidas indicando la causa del error. | R:M-01 | Servicio de oferta comercial | 1 | Alta | RN-P01 | La publicación de la referencia es función del servicio de oferta comercial. |
| RF-149 | El sistema debe permitir al gerente de logística definir el valor del colchón de confianza por categoría. | R:M-03 | Servicio de existencias | 1 | Alta | RN-09 | — |
| RF-150 | El sistema debe permitir al gerente de logística definir el valor del colchón de confianza por punto de existencia. | R:M-03 | Servicio de existencias | 1 | Alta | RN-09 | — |
| RF-151 | El sistema deberá registrar quien definio o modifico el colchón, cuando, el valor anterior y el valor nuevo. | R:M-03 | Servicio de existencias | 1 | Alta | RN-09 | — |
| RF-152 | El sistema deberá sugerir un valor de referencia del colchón calculado a partir del histórico de ventas y quiebres de la categoría. | R:M-03 | Servicio de existencias | 1 | Alta | RN-09 | — |
| RF-153 | El sistema deberá permitir al vendedor de piso registrar las unidades que ingresan al probador. | R:M-03 | Servicio de existencias | 1 | Alta | RN-P02 | Mantenido: las unidades en probador son una causa de la imprecisión del registro (causa C1 del capítulo 2). |
| RF-154 | El sistema deberá excluir del disponible para vender las unidades registradas en probador. | R:M-03 | Servicio de existencias | 1 | Alta | RN-P02, RN-09 | Mantenido: las unidades en probador son una causa de la imprecisión del registro (causa C1 del capítulo 2). |
| RF-155 | El sistema debe permitir al vendedor de piso confirmar el reingreso a sala de la unidad registrada en probador. | R:M-03 | Servicio de existencias | 1 | Alta | RN-P02 | Mantenido: las unidades en probador son una causa de la imprecisión del registro (causa C1 del capítulo 2). |
| RF-156 | El sistema debe permitir al vendedor de piso registrar la venta de la unidad registrada en probador. | R:M-03 | Servicio de existencias | 1 | Alta | RN-P02 | Mantenido: las unidades en probador son una causa de la imprecisión del registro (causa C1 del capítulo 2). |
| RF-157 | El sistema deberá impedir que cualquier canal de venta consuma el saldo bruto de inventario para publicar o comprometer existencia. | R:M-03 | Servicio de existencias | 1 | Alta | RN-08 | — |
| RF-158 | El sistema debe calcular el porcentaje de error probable de la referencia en función de su categoría. | R:M-03 | Servicio de existencias | 1 | Alta | RN-11 | — |
| RF-159 | El sistema debe calcular el porcentaje de error probable de la referencia en función de su punto de existencia. | R:M-03 | Servicio de existencias | 1 | Alta | RN-11 | — |
| RF-160 | El sistema deberá mostrar al cliente el porcentaje de error probable calculado en RF-058 junto a la disponibilidad publicada. | R:M-03 | Servicio de existencias | 1 | Alta | RN-11 | — |
| RF-161 | El sistema deberá mostrar al vendedor de piso el porcentaje de error probable calculado en RF-058. | R:M-03 | Servicio de existencias | 1 | Alta | RN-11, RN-P05 | — |
| RF-162 | El sistema deberá generar una alerta interna dirigida al rol facultado cuando la exactitud de una categoría caiga bajo el umbral definido. | R:M-03 | Servicio de existencias | 1 | Alta | RN-11 | — |
| RF-163 | El sistema deberá permitir exclusivamente al rol facultado suspender manualmente la publicación de una categoría. | R:M-03 | Servicio de existencias | 1 | Alta | RN-11, RN-57 | — |
| RF-164 | El sistema deberá abstenerse de suspender automáticamente la publicación de una categoría que no tenga una regla de degradación declarada y aprobada previamente. | R:M-03 | Servicio de existencias | 1 | Alta | RN-11, RN-57 | — |
| RF-165 | El sistema deberá registrar cada cruce de información ejecutado entre ámbitos, indicando el dato cruzado, la finalidad, la base de licitud, la autorización nominada y el instante. | X-01 | Servicio de control de cruces | 1 | Alta | RN-02 | — |
| RF-166 | El sistema deberá bloquear todo intento de cruce de información que no corresponda a una interfaz declarada en el inventario de flujos autorizados. | X-01 | Servicio de control de cruces | 1 | Alta | RN-02, RN-05 | — |
| RF-167 | El sistema deberá registrar el intento de cruce bloqueado con el componente origen, el dato solicitado y el instante. | X-01 | Servicio de control de cruces | 1 | Alta | RN-02 | — |
| RF-168 | El sistema debe permitir al oficial de cumplimiento mantener el inventario de interfaces de cruce declaradas. | X-01 | Servicio de control de cruces | 1 | Alta | RN-02 | — |
| RF-169 | El sistema debe impedir el registro de una interfaz de cruce que no declare finalidad, base de licitud y autorización nominada. | X-01 | Servicio de control de cruces | 1 | Alta | RN-02 | — |
| RF-170 | El sistema deberá excluir del catálogo de atributos disponibles en el motor de campañas todo atributo de origen financiero (mora, deuda, cupo utilizado, comportamiento de pago). | X-01 | Servicio de control de cruces | 1 | Alta | RN-03 | Mantenido en el servicio de control de cruces porque es un control de frontera, igual que RF-171. El servicio de clientes Retail respeta el catálogo de atributos que ese control define. |
| RF-171 | El sistema deberá rechazar la ejecución de toda facilidad comercial que invoque un atributo de origen financiero sin un registro de cruce autorizado asociado. | X-01 | Servicio de control de cruces | 1 | Alta | RN-05, RN-02 | — |
| RF-172 | El sistema deberá rechazar la ejecución de todo proceso crediticio que invoque un atributo de origen retail sin un registro de cruce autorizado asociado. | X-01 | Servicio de control de cruces | 1 | Alta | RN-05, RN-02 | — |
| RF-173 | El sistema deberá asignar a la misma persona un identificador distinto en el ámbito retail y en el ámbito fiscalizado. | X-01 | Servicio de control de cruces | 1 | Alta | RN-04 | — |
| RF-174 | El sistema deberá resolver la correspondencia entre identificadores exclusivamente a través de una tabla de correspondencia custodiada, con acceso nominado y registrado. | X-01 | Servicio de control de cruces | 1 | Alta | RN-04, RN-02 | — |
| RF-175 | El sistema deberá rechazar la persistencia de la clave del ámbito financiero como columna o atributo en cualquier entidad del ámbito retail. | X-01 | Servicio de control de cruces | 1 | Alta | RN-04, RN-01 | — |
| RF-176 | El sistema deberá exigir el registro de la evaluación de impacto sobre la frontera de datos antes de habilitar el estado 'aprobada' de una iniciativa. | X-01 | Servicio de control de cruces | 1 | Alta | RN-06 | — |
| RF-177 | El sistema debe permitir declarar previamente el orden de degradación de los servicios. | — | Base tecnológica | 1 | Alta | RN-57, RN-11 | Mecanismo de degradación y de congelamiento de la base tecnológica. |
| RF-178 | El sistema debe permitir parametrizar los criterios que activan cada nivel de degradación declarado. | — | Base tecnológica | 1 | Alta | RN-57, RN-11 | Mecanismo de degradación y de congelamiento de la base tecnológica. |
| RF-179 | El sistema deberá suspender la publicación de la categoría indicada por el orden de degradación declarado. | R:M-03 | Servicio de existencias | 1 | Alta | RN-57, RN-11 | — |
| RF-180 | El sistema deberá reducir el límite de unidades por cliente al valor declarado. | R:V-01 | Servicio de pedidos | 2 | Media | RN-57 | El límite de unidades por cliente es un parámetro del pedido. Su aplicación en el primer evento anual se confirma en la arquitectura y en el plan de riesgos. |
| RF-181 | El sistema deberá desactivar temporalmente los medios de pago de mayor fricción operativa declarados. | R:V-02 | Servicio de ventas | 1 | Alta | RN-57 | Los medios de pago son datos del servicio de ventas. |
| RF-182 | El sistema deberá monitorear en tiempo real la tasa de cancelación por falta de existencia por categoría. | R:M-03 | Servicio de existencias | 1 | Alta | RN-57, RN-09 | — |
| RF-183 | El sistema deberá activar la acción de degradación declarada para esa categoría en RF-026.1. | R:M-03 | Servicio de existencias | 1 | Alta | RN-57, RN-11 | — |
| RF-184 | El sistema deberá permitir parametrizar las cinco ventanas de congelamiento (1 nov - 6 ene; evento anual y su semana previa; evento de noviembre; semana del Día de la Madre; última semana de enero a primera de marzo). | — | Base tecnológica | 1 | Alta | RN-55 | Mecanismo de degradación y de congelamiento de la base tecnológica. |
| RF-185 | El sistema deberá impedir la ejecución del despliegue o intervención en producción durante la ventana de congelamiento. | — | Base tecnológica | 1 | Alta | RN-55 | Mecanismo de degradación y de congelamiento de la base tecnológica. |
| RF-186 | El sistema deberá registrar el intento de despliegue bloqueado, indicando componente, solicitante e instante. | — | Base tecnológica | 1 | Alta | RN-55 | Mecanismo de degradación y de congelamiento de la base tecnológica. |
| RF-187 | El sistema debe permitir al ejecutivo de mesón atender íntegramente el caso de garantía legal en la tienda. | R:CL-01 | Servicio de posventa | 2 | Alta | RN-26 | — |
| RF-188 | El sistema debe impedir que el flujo de atención exija la derivación del consumidor al fabricante, al servicio técnico o al vendedor de marketplace como condición para ser atendido. | R:CL-01 | Servicio de posventa | 2 | Alta | RN-26 | Sostiene la restricción 7 (la garantía legal se ejerce ante la compañía, sin derivar al consumidor). |
| RF-189 | El sistema deberá permitir al ejecutivo registrar el motivo de la devolución (talla, color, expectativa, falla). | R:CL-01 | Servicio de posventa | 2 | Media | RN-14 | — |
| RF-190 | El sistema deberá impedir el reingreso de una unidad devuelta al inventario disponible mientras no exista una decisión de aptitud registrada. | R:CL-01 | Servicio de posventa | 2 | Media | RN-14 | — |
| RF-191 | El sistema deberá permitir al ejecutivo registrar la decisión de aptitud de la unidad devuelta, identificando al responsable de la decisión y su instante. | R:CL-01 | Servicio de posventa | 2 | Media | RN-14 | — |
| RF-192 | El sistema deberá presentar al ejecutivo las tres opciones de garantía legal (reparación, reposición y devolución del precio) para que el consumidor elija. | R:CL-01 | Servicio de posventa | 2 | Alta | RN-29 | — |
| RF-193 | El sistema debe registrar la opción de garantía legal ofrecida al consumidor. | R:CL-01 | Servicio de posventa | 2 | Alta | RN-29 | — |
| RF-194 | El sistema debe registrar la opción de garantía legal efectivamente elegida por el consumidor. | R:CL-01 | Servicio de posventa | 2 | Alta | RN-29 | — |
| RF-195 | El sistema deberá permitir parametrizar el plazo de garantía legal por tipo de producto, sin requerir modificacion de código. | R:CL-01 | Servicio de posventa | 2 | Alta | RN-29 | — |
| RF-196 | El sistema deberá registrar el hito de resolución al consumidor con su fecha propia. | R:CL-01 | Servicio de posventa | 2 | Media | RN-27 | — |
| RF-197 | El sistema deberá registrar el hito de recuperación contra el tercero responsable con una fecha independiente de la resolución al consumidor. | R:CL-01 | Servicio de posventa | 2 | Media | RN-27 | — |
| RF-198 | El sistema deberá impedir que el estado de la recuperación contra el tercero condicione el cierre de la resolución al consumidor. | R:CL-01 | Servicio de posventa | 2 | Media | RN-27, RN-26 | — |
| RF-199 | El sistema deberá exigir la entrega completa de la información precontractual antes de habilitar la evaluación de la solicitud de crédito. | F:C-03 | Servicio de evidencia financiera | 1 | Alta | RN-34 | — |
| RF-200 | El sistema deberá registrar la versión del documento precontractual entregado. | F:C-03 | Servicio de evidencia financiera | 1 | Alta | RN-35 | — |
| RF-201 | El sistema deberá registrar el instante de entrega de la información precontractual. | F:C-03 | Servicio de evidencia financiera | 1 | Alta | RN-35 | — |
| RF-202 | El sistema deberá registrar el instante de aceptación del cliente. | F:C-03 | Servicio de evidencia financiera | 1 | Alta | RN-35 | — |
| RF-203 | El sistema deberá registrar el medio por el cual se entrego y se aceptó la información precontractual. | F:C-03 | Servicio de evidencia financiera | 1 | Alta | RN-35, RN-P04 | — |
| RF-204 | El sistema deberá registrar el contenido exacto aceptado por el cliente o su huella de integridad verificable. | F:C-03 | Servicio de evidencia financiera | 1 | Alta | RN-35, RN-41 | — |
| RF-205 | El sistema deberá dejar constancia expresa de que el cliente recibió la información antes de aceptar, mediante un mecanismo distinto de la sola firma en papel archivado. | F:C-03 | Servicio de evidencia financiera | 1 | Alta | RN-34, RN-35 | — |
| RF-206 | El sistema deberá impedir el registro de la aceptación del crédito mientras no exista acreditación de entrega previa de la información precontractual completa. | F:C-03 | Servicio de evidencia financiera | 1 | Alta | RN-34 | — |
| RF-207 | El sistema deberá registrar la evidencia del consentimiento expreso e informado del cliente mediante un mecanismo verificable de integridad. | F:C-03 | Servicio de evidencia financiera | 1 | Alta | RN-40, RN-41 | — |
| RF-208 | El sistema deberá impedir el registro de una modificacion de condiciones del crédito que no tenga evidencia de consentimiento asociada. | F:C-03 | Servicio de evidencia financiera | 1 | Alta | RN-40 | — |
| RF-209 | El sistema deberá reconstruir el acto de consentimiento presentando que se informó, en que versión y que aceptó el cliente. | F:C-03 | Servicio de evidencia financiera | 1 | Alta | RN-41, RN-35 | — |
| RF-210 | El sistema deberá restaurar desde archivo frío los antecedentes de una operación de crédito de cualquier cohorte dentro del plazo de conservación. | F:C-03 | Servicio de evidencia financiera | 1 | Alta | RN-36 | Recuperar los antecedentes de una operación de crédito es función de la evidencia financiera. |
| RF-211 | El sistema debe permitir al ejecutivo de cobranza iniciar una gestión de cobranza. | F:C-02 | Servicio de cartera de crédito | 1 y 2 | Alta | RN-40 | — |
| RF-212 | El sistema debe registrar la gestión de cobranza ejecutada con su medio, su instante y su ejecutor. | F:C-02 | Servicio de cartera de crédito | 1 y 2 | Alta | RN-40 | — |
| RF-213 | El sistema debe impedir la ejecución de una gestión de cobranza fuera de los límites normativos de horario y de medio de contacto. | F:C-02 | Servicio de cartera de crédito | 1 y 2 | Alta | RN-40 | — |
| RF-214 | El sistema debe enlazar el expediente de la repactación con la gestión de cobranza que la originó. | F:C-03 | Servicio de evidencia financiera | 1 | Alta | RN-40, RN-41 | — |
| RF-215 | El sistema debe enlazar el expediente de la repactación con la evidencia de consentimiento registrada en RF-207. | F:C-03 | Servicio de evidencia financiera | 1 | Alta | RN-40, RN-41 | — |
| RF-216 | El sistema deberá generar un reporte de conciliación diaria de saldos durante todo el proceso de migración. | F:C-02 | Servicio de cartera de crédito | 1 y 2 | Alta | RN-58 | — |
| RF-217 | El sistema deberá permitir al cliente no autenticado consultar la información precontractual del crédito. | F:C-03 | Servicio de evidencia financiera | 1 | Alta | RN-34 | — |
| RF-218 | El sistema deberá permitir al cliente no autenticado utilizar un simulador de costo total del crédito. | F:C-01 | Servicio de originación de crédito | 1 | Alta | RN-34, RN-37 | — |
| RF-219 | El sistema deberá mantener cargada la Tasa Máxima Convencional vigente por tipo y tramo de operación, con su fecha de vigencia. | F:C-01 | Servicio de originación de crédito | 1 | Alta | RN-37 | Parte de la evaluación y autorización del crédito. |
| RF-220 | El sistema deberá impedir la originación de una operación cuya tasa supere la Tasa Máxima Convencional vigente a la fecha de la operación. | F:C-01 | Servicio de originación de crédito | 1 | Alta | RN-37 | — |
| RF-221 | El sistema deberá determinar el cupo exclusivamente a partir de las variables de la evaluación de capacidad de pago documentada. | F:C-01 | Servicio de originación de crédito | 1 | Alta | RN-38 | Determinar el cupo es parte de la evaluación de la originación, igual que RF-218 a RF-220. |
| RF-222 | El sistema deberá excluir el monto de la venta en curso del conjunto de variables de asignación de cupo. | F:C-01 | Servicio de originación de crédito | 1 | Alta | RN-38 | — |
| RF-223 | El sistema deberá excluir la solicitud del vendedor del conjunto de variables de asignación de cupo. | F:C-01 | Servicio de originación de crédito | 1 | Alta | RN-38, RN-39 | — |
| RF-224 | El sistema deberá impedir al vendedor alterar el resultado de una evaluación crediticia. | F:C-01 | Servicio de originación de crédito | 1 | Alta | RN-39 | — |
| RF-225 | El sistema deberá impedir la repetición de la evaluación crediticia del mismo cliente dentro de la ventana de enfriamiento parametrizada. | F:C-01 | Servicio de originación de crédito | 1 | Alta | RN-39 | — |
| RF-226 | El sistema deberá registrar cada intento de evaluación con la identidad del solicitante y el resultado obtenido. | F:C-01 | Servicio de originación de crédito | 1 | Alta | RN-39 | — |
| RF-227 | El sistema deberá consolidar en un único registro retail los registros duplicados de un mismo cliente. | R:CL-02 | Servicio de clientes Retail | 2 | Media | — | Propuesto por el proponente. Deriva de la función de deduplicación que incluye el servicio. Por validar. |
| RF-228 | El sistema deberá registrar cada movimiento de puntos de fidelización de un cliente. | R:CL-02 | Servicio de clientes Retail | 2 | Media | — | Propuesto por el proponente. Deriva de los datos de puntos del sistema de fidelización que el servicio gobierna (Caso cap. 5, EXC-15). Por validar. |
| RF-229 | El sistema deberá construir los segmentos de clientes del retail exclusivamente con atributos comerciales. | R:CL-02 | Servicio de clientes Retail | 2 | Media | RN-03, RN-05 | Propuesto por el proponente. Deriva de RN-03 y RN-05. El control de frontera lo hacen RF-170 y RF-171. Por validar. |
| RF-230 | El sistema deberá ejecutar campañas sobre los segmentos de clientes del retail. | R:CL-02 | Servicio de clientes Retail | 2 | Media | — | Propuesto por el proponente. Deriva de las campañas del sistema de fidelización que el servicio gobierna (Caso cap. 5, EXC-15). Por validar. |
| RF-231 | El sistema deberá sincronizar con el sistema de fidelización conservado los datos de fidelización del cliente. | R:CL-02 | Servicio de clientes Retail | 2 | Media | — | Propuesto por el proponente. Deriva de EXC-15: la fidelización se conserva y se integra al servicio. Por validar. |

## B.4 Requerimientos no funcionales (RNF)

El ámbito (retail, filial emisora o ambos) y la etapa (la del servicio que mide el requerimiento) se proponen según el contenido. Se confirman al llenar el Formulario T-12.

| ID | Requerimiento | Umbral o criterio | Método de verificación | Ámbito | Prioridad | Etapa | RN vinculada | Nota |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| RNF-02 | La interfaz de declaración de existencia del vendedor de marketplace debe estar disponible de forma continua. | 24x7x365; disponibilidad >= 99,5 % (supuesto fundamentado). | Medición mensual de disponibilidad de la interfaz de sincronización de catálogo. | Retail | Alta | 2 | RN-32 | Mide el servicio de marketplace, de la Etapa 2. |
| RNF-03 | El registro del conteo cíclico no debe bloquear ni degradar la operación de venta de la sala. | 0 bloqueos de la línea de caja durante el conteo; degradación del tiempo de venta <= 5 % respecto de la línea base de RNF-18. | Prueba de conteo cíclico ejecutado en horario de venta con medición simultánea del tiempo de transacción en caja. | Retail | Alta | 1 | RN-13 | — |
| RNF-04 | El estado de un pedido no debe presentar discrepancias entre canales de consulta. | 0% de discrepancias en auditoría cruzada. | Prueba de sincronización cruzada entre canales tras cada cambio de estado. | Retail | Alta | 2 | RN-23, RN-28 | Mide el servicio de pedidos, de la Etapa 2. |
| RNF-05 | La actualización del estado de un pedido debe reflejarse en todos los puntos de consulta dentro del plazo máximo definido. | Desfase máximo entre cambio real de estado y su reflejo en cualquier canal: POR DEFINIR (propuesta: 30 s). | Medicion de latencia de propagación por canal. | Retail | Alta | 2 | RN-23, RN-28 | Mide el servicio de pedidos, de la Etapa 2. |
| RNF-06 | El tiempo de evaluación de una solicitud de crédito en el punto de venta físico no debe exceder el umbral objetivo. | <= 8 segundos. | Prueba de tiempo de respuesta en punto de venta bajo carga representativa. | Filial emisora | Alta | 1 | RN-34 | — |
| RNF-07 | El tiempo total de originación de crédito en el mesón, con información precontractual acreditada, no debe superar el tiempo del proceso actual. | <= 3 minutos (tiempo actual declarado en el caso). | Medicion de tiempo de originación extremo a extremo en mesón, con y sin acreditación. | Filial emisora | Alta | 1 | RN-34 | — |
| RNF-08 | La migración de la cartera de crédito viva no debe generar pérdida de datos. | 0 registros perdidos respecto del universo de 620.000 clientes con saldo. | Conteo y cuadratura de universos origen y destino en cada corte de migración. | Filial emisora | Alta | 1 | RN-58 | — |
| RNF-09 | La migración de la cartera de crédito viva no debe interrumpir el servicio de cobro. | 0 interrupciones del servicio de cobro durante la ventana de migración. | Monitoreo continuo de disponibilidad del servicio de cobro durante cada etapa de coexistencia. | Filial emisora | Alta | 1 | RN-58 | — |
| RNF-10 | La migración de la cartera de crédito viva no debe producir divergencia de saldos. | 0 divergencias no conciliadas en la conciliación diaria; migración completa antes de 2029. | Conciliación diaria automatizada de saldos entre entorno origen y destino (RF-216). | Filial emisora | Alta | 1 | RN-58 | — |
| RNF-11 | La separación lógica entre los datos del retail y los del negocio financiero debe estar implementada. | Separación lógica operativa en todos los componentes que tratan datos de ambos ámbitos. | Revisión de arquitectura desplegada y prueba de acceso denegado desde el ámbito retail. | Ambos | Alta | 1 | RN-01, RN-06 | — |
| RNF-12 | La separación lógica entre ambos ámbitos debe estar documentada. | Documento de separación vigente y versionado, aprobado por la Contraloría interna. | Revisión documental contra el diseño desplegado. | Ambos | Alta | 1 | RN-01, RN-06 | — |
| RNF-13 | La separación lógica entre ambos ámbitos debe ser verificada por auditoría independiente. | Informe de auditoría aprobado con 0 hallazgos críticos abiertos, previo a cualquier vista unificada. | Auditoría independiente con informe formal y seguimiento de hallazgos. | Ambos | Alta | 1 | RN-01, RN-06 | — |
| RNF-14 | La separación física entre la infraestructura del retail y la de la filial emisora debe estar implementada y acreditada. | Informe técnico de separación física acreditado; prueba de penetracion que demuestre que un componente del retail no alcanza datos de crédito. | Prueba de penetracion e inspeccion de infraestructura. | Ambos | Alta | 1 | RN-01 | — |
| RNF-15 | Toda acción relevante ejecutada en el sistema debe quedar registrada indicando usuario individual, acción e instante. | 100% de acciones relevantes con registro de auditoría. | Auditoría de logs sobre muestra de transacciones. | Ambos | Alta | 1 | RN-50, RN-51, RN-52 | — |
| RNF-16 | La consulta de disponibilidad en la ficha de producto del canal digital debe responder dentro del umbral definido. | <= 400 ms. | Prueba de tiempo de respuesta bajo carga representativa. | Retail | Alta | 1 | RN-09 | — |
| RNF-17 | La confirmación de un pedido durante el evento anual debe completarse dentro del umbral definido. | <= 3 s. | Prueba de carga con volumetria del evento anual. | Retail | Alta | 2 | RN-57 | Mide el servicio de pedidos, de la Etapa 2. |
| RNF-18 | La venta completa en caja con medio de pago externo debe completarse dentro del umbral definido. | <= 25 s. | Prueba de tiempo de respuesta en linea de caja. | Retail | Alta | 1 | RN-46 | — |
| RNF-19 | La propagación de un cambio de precio a las 380 líneas de caja y al canal digital debe completarse dentro del umbral definido. | <= 5 minutos. | Medicion de latencia de propagación por destino. | Retail | Alta | 1 | RN-16, RN-18 | — |
| RNF-20 | El registro de una devolución en el mesón debe completarse dentro del umbral definido. | <= 60 s. | Prueba de tiempo de respuesta en mesón de atención. | Retail | Alta | 1 | RN-14, RN-26 | — |
| RNF-21 | La consulta de disponibilidad desde una terminal compartida del piso de venta debe responder dentro del umbral definido. | <= 2 s. | Prueba de tiempo de respuesta en terminal de sala. | Retail | Alta | 1 | RN-09, RN-P05 | — |
| RNF-22 | La plataforma debe soportar la concurrencia y el volumen del peak digital del evento anual sin degradar los umbrales de NFR-06.x. | Perfil declarado por el PROPONENTE sobre 104.000 pedidos en 3 días (proyección 150.000), equivalente a 22 días de venta en línea. | Prueba de carga con perfil del evento anual al 120 % del peak proyectado. | Ambos | Alta | 1 | RN-57 | — |
| RNF-23 | La plataforma debe soportar la concurrencia y el volumen del peak presencial de la campaña de noviembre y diciembre sin degradar los umbrales de NFR-06.x. | Perfil declarado por el PROPONENTE sobre 380 líneas de caja (430 proyectadas) en peak de sábado de diciembre. | Prueba de carga con perfil presencial sostenido, independiente de la prueba del peak digital. | Ambos | Alta | 1 | RN-57 | — |
| RNF-24 | Una tienda debe poder operar sin enlace externo durante el período mínimo definido. | >= 24 horas continuas. | Prueba de desconexion controlada en tienda. | Retail | Alta | 1 | RN-46 | Umbral unificado a 24 horas (autonomía única, Bases Técnicas Transversales RT-03.10 y art. 16.4 de las Bases Administrativas). El catálogo previo decía 8 horas. |
| RNF-25 | El centro de distribución principal debe poder operar sin enlace externo durante el período mínimo definido. | >= 24 horas continuas. | Prueba de desconexión controlada en el centro de distribución. | Retail | Alta | 1 | RN-46 | Se eleva de 4 a 24 horas: RT-03.10 y el art. 16.4 no admiten menos de 24 horas para el componente on-premise. El valor de 4 horas del Caso queda por debajo y rige el más exigente. Se consulta al mandante. |
| RNF-26 | La sincronización tras la reconexión no debe superar el plazo definido. | <= 30 minutos tras 24 horas de desconexión. | Prueba de reconexión cronometrada tras desconexión programada de 24 horas. | Retail | Alta | 1 | RN-48 | Alineado a la autonomía única de 24 horas. El volumen tras 24 horas es un supuesto por estimar. El catálogo previo decía 8 horas. |
| RNF-27 | La sincronización tras la reconexión no debe producir pérdida de ventas ni de documentos. | 0 ventas y 0 documentos perdidos o duplicados. | Cuadratura del universo de transacciones de la ventana desconectada contra el sistema central. | Retail | Alta | 1 | RN-48 | — |
| RNF-28 | La operación desconectada autónoma on-premise debe sostenerse durante el período mínimo exigido por las bases técnicas. | >= 24 horas continuas (Bases Técnicas Transversales). | Prueba de desconexion extendida. | Retail | Alta | 1 | RN-46 | Se retira la referencia al mínimo de 8 horas de RN-46: rige el valor más exigente. Coincide con RNF-24 en tiendas y se mantiene para el componente on-premise. |
| RNF-29 | La operación de tiendas y centros de distribución debe estar disponible en la ventana horaria definida. | 09:00 a 23:00, todos los dias del ano. | Monitoreo continuo de disponibilidad por servicio. | Retail | Alta | 1 | RN-46 | — |
| RNF-30 | El canal digital debe estar disponible de forma continua. | 24x7x365; disponibilidad >= 99,5 % (supuesto fundamentado, equivalente a Tier 2). | Medición mensual de disponibilidad contra el nivel de servicio comprometido. | Retail | Alta | 1 | RN-46, RN-58 | — |
| RNF-31 | Los servicios financieros que afectan pagos, estados de cuenta y bloqueo de tarjetas deben estar disponibles de forma continua. | 24x7x365; disponibilidad >= 99,5 % (supuesto fundamentado). | Medición mensual segregada por ámbito, informada a la filial emisora. | Filial emisora | Alta | 1 | RN-46, RN-58 | — |
| RNF-32 | La solución debe cumplir los objetivos de recuperación ante desastre exigidos. | RTO <= 4 h; RPO <= 15 min. | Ensayo de recuperación ante desastre con medicion de RTO y RPO efectivos. | Ambos | Alta | 1 | RN-48, RN-58 | — |
| RNF-33 | Los datos de identificación de clientes, la cartera de crédito, el comportamiento de pago y los antecedentes de evaluación crediticia deben cifrarse a nivel de campo. | 100% de campos sensibles cifrados. | Auditoría de esquema de datos y prueba de exfiltracion controlada. | Filial emisora | Alta | 1 | RN-01, RN-03 | — |
| RNF-34 | Los datos de medios de pago no deben almacenarse en claro, sino tokenizarse. | 0% de datos de medios de pago almacenados sin tokenizar. | Auditoría de esquema y prueba de exfiltracion controlada. | Ambos | Alta | 1 | RN-01 | — |
| RNF-35 | La red de cajas, la administrativa, la de videovigilancia y la inalámbrica de clientes deben estar segmentadas en las 22 tiendas. | 22/22 tiendas con segmentacion verificada (hoy 9). | Auditoría de configuracion de red por tienda. | Retail | Alta | 1 | RN-01 | — |
| RNF-36 | La red y el ámbito de sistemas de la filial emisora deben estar separados de forma acreditada respecto del retail. | Separación acreditada mediante informe técnico. | Auditoría de arquitectura de red. | Filial emisora | Alta | 1 | RN-01 | — |
| RNF-37 | Debe existir segregación de funciones verificable entre originación, aprobación, modificacion de condiciones y cobranza. | 0 usuarios con permisos combinados de originación+aprobación o de modificacion+cobranza sobre un mismo caso. | Auditoría de matriz de roles y permisos. | Filial emisora | Alta | 1 | RN-39, RN-53 | — |
| RNF-38 | Debe registrarse todo acceso a la cartera de crédito, al comportamiento de pago y a los antecedentes de evaluación crediticia. | 100% de accesos a información sensible con registro (usuario, dato, finalidad, instante). | Auditoría de logs de acceso sobre muestra representativa. | Filial emisora | Alta | 1 | RN-02, RN-03 | — |
| RNF-39 | Los actos de crédito de apertura de tarjeta y de repactación deben contar con un mecanismo de consentimiento de integridad verificable. | 100 % de aperturas y repactaciones con evidencia de integridad verificable, en la modalidad que la normativa admita para cada canal. | Auditoría censal del período y verificación de la huella de integridad por muestreo. | Filial emisora | Alta | 1 | RN-35, RN-40, RN-41, RN-P04 | — |
| RNF-40 | La conformidad de recepción de mercadería y la constancia de devolución deben contar con un mecanismo de consentimiento de integridad verificable. | 100 % de conformidades y constancias con evidencia de integridad verificable. | Verificación de la validez de la firma y de la integridad del documento por muestreo. | Retail | Alta | 1 | RN-35, RN-40, RN-41, RN-P04 | — |
| RNF-41 | Los documentos tributarios y antecedentes de venta deben conservarse por el plazo definido. | 6 años. | Auditoría de politicas de retencion por tipo de dato. | Retail | Alta | 1 | RN-49 | — |
| RNF-42 | Los antecedentes del crédito deben conservarse por el plazo del crédito más el período posterior exigido. | Plazo del crédito + 6 años (sustituye la practica actual de 90 dias para grabaciones). | Auditoría de retencion y prueba de restauración desde archivo frío. | Filial emisora | Alta | 1 | RN-36 | — |
| RNF-43 | La evidencia de consentimiento de originación y repactación debe conservarse por el mismo plazo que el crédito. | Plazo del crédito + 6 años; recuperable a 10 años según RN-35. | Auditoría de retencion y prueba de recuperación. | Filial emisora | Alta | 1 | RN-35, RN-36, RN-40 | — |
| RNF-44 | La trazabilidad del precio publicado debe conservarse por el plazo definido. | 3 años. | Auditoría de retencion. | Retail | Alta | 1 | RN-17 | — |
| RNF-45 | Los movimientos de inventario y conteos cíclicos deben conservarse por el plazo definido. | 6 años. | Auditoría de retencion. | Retail | Alta | 1 | RN-13 | — |
| RNF-46 | Los datos de fidelización deben conservarse por el plazo definido. | Duracion de la relacion + 2 años. | Auditoría de retencion. | Retail | Alta | 2 | RN-03 | Antes sin servicio dueño. Los datos de fidelización son del servicio de clientes Retail (EXC-15). La retención rige desde que el servicio los gobierna, en la Etapa 2. |
| RNF-47 | Los registros de videovigilancia deben conservarse por el plazo definido. | 30 dias. | Auditoría de retencion. | Retail | Alta | 1 | RN-01 | — |
| RNF-48 | La solución debe admitir la apertura de una tienda nueva por parametrización, sin desarrollo a medida. | Alta de tienda por configuracion en <= 10 dias habiles (supuesto fundamentado, compatible con una apertura comercial). | Prueba de aprovisionamiento de una tienda simulada. | Retail | Alta | 1 | - | — |
| RNF-49 | Las interfaces de sala, caja y mesón financiero deben ser operables por personal recién incorporado con capacitación mínima. | Tiempo de capacitación operativa basica <= 4 horas (supuesto fundamentado), medido con personal de temporada. | Prueba de usabilidad con personal recién incorporado en condiciones reales. | Ambos | Alta | 1 | RN-50, RN-53 | — |
| RNF-50 | Toda comunicación relativa al crédito debe cumplir criterios verificables de lenguaje claro, validados con personas usuarias reales. | 100% de plantillas validadas con pruebas de comprension lectora con usuarios reales. | Prueba de comprension lectora sobre muestra de plantillas. | Filial emisora | Alta | 1 | RN-34, RN-41 | — |
| RNF-51 | Las notificaciones definidas funcionalmente deben emitirse y registrarse en el 100% de los eventos que las gatillan. | 100% de eventos definidos con notificacion generada y registrada. | Prueba de disparo de eventos y verificacion del registro. | Ambos | Alta | 1 | RN-23, RN-28, RN-11 | — |
| RNF-52 | La solución debe adoptar un estándar identificado y justificado para el catálogo e identificación de producto. | Estándar identificado por su denominación y justificado en la Oferta Técnica. | Prueba de interoperabilidad con al menos una contraparte real del dominio. | Retail | Alta | 1 | RN-49, RN-32 | — |
| RNF-53 | La solución debe adoptar un estándar identificado y justificado para el intercambio de órdenes y avisos de despacho con los proveedores. | Estándar identificado y justificado; 100 % de las interfaces con proveedores mapeadas a él. | Prueba de intercambio con un proveedor piloto. | Retail | Alta | 1 | RN-49, RN-32 | — |
| RNF-54 | La solución debe adoptar un estándar identificado y justificado para el intercambio con los transportistas de última milla. | Estándar identificado y justificado; trazabilidad del estado del pedido hasta la entrega. | Prueba de integración con un transportista piloto. | Retail | Alta | 1 | RN-49, RN-32 | — |
| RNF-55 | La solución debe adoptar un estándar identificado y justificado para la sincronización de catálogo, existencia y pedido con los vendedores de marketplace. | Estándar identificado y justificado; 100 % de vendedores sincronizados por él. | Prueba de sincronización con un vendedor piloto. | Retail | Alta | 2 | RN-49, RN-32 | Mide el servicio de marketplace, de la Etapa 2. |
| RNF-56 | La solución debe adoptar el formato normativo vigente de documento tributario electrónico. | 100 % de los documentos emitidos conforme al formato vigente de la autoridad tributaria. | Validación de esquema sobre una muestra de documentos emitidos. | Retail | Alta | 1 | RN-49, RN-32 | — |
| RNF-57 | La evidencia completa de consentimiento de una operación arbitraria debe recuperarse dentro del plazo objetivo, a diez años. | Recuperación <= 5 minutos (supuesto fundamentado) sobre operaciones de hasta 10 años de antiguedad. | Simulacro de requerimiento de la autoridad fiscalizadora. | Filial emisora | Alta | 1 | RN-35, RN-41 | — |
| RNF-58 | La recuperación del precio publicado de una referencia en una fecha, hora y canal arbitrarios debe completarse dentro del plazo objetivo. | <= 1 minuto, sobre una ventana de 3 años. | Consulta de auditoría sobre fecha/hora/canal aleatorios. | Retail | Alta | 1 | RN-17 | — |
| RNF-59 | La revocación total de accesos de un trabajador debe completarse dentro del plazo máximo de la política interna. | <= 4 horas desde el término efectivo del vínculo (supuesto fundamentado). | Auditoría de accesos vigentes contra nómina activa. | Ambos | Alta | 1 | RN-52 | — |
| RNF-60 | El traspaso de sesión nominativa en una terminal compartida debe completarse dentro del plazo objetivo. | <= 5 segundos (supuesto fundamentado). | Medicion de tiempo de traspaso en terminal de sala. | Ambos | Alta | 1 | RN-50 | — |
| RNF-64 | El tiempo entre la detección de un quiebre y el aviso al cliente no debe superar el objetivo declarado. | <= 30 minutos (supuesto fundamentado). | Medición de la latencia entre el evento de quiebre y el envío de la notificación. | Retail | Alta | 2 | RN-23 | Mide el servicio de pedidos, de la Etapa 2. |
| RNF-65 | No debe mantenerse un cobro capturado sobre un pedido declarado no cumplible. | 0 casos de cobro sostenido sobre pedido no cumplible. | Auditoría de conciliación diaria de preautorizaciones y capturas (RF-050). | Retail | Alta | 2 | RN-23 | Mide el servicio de pedidos, de la Etapa 2. |
| RNF-66 | La latencia entre la recepción física de una devolución en tienda y la notificación al vendedor de marketplace no debe superar el objetivo declarado. | <= 15 minutos (supuesto fundamentado). | Medición de la latencia entre el registro de recepción y el envío de la notificación. | Retail | Alta | 2 | RN-28 | Mide el servicio de marketplace, de la Etapa 2. |
| RNF-67 | No debe permanecer mercadería de marketplace en bodega sin aviso a su propietario. | 0 unidades en bodega sin notificación asociada al cierre de cada día. | Conciliación diaria entre recepciones registradas y notificaciones emitidas. | Retail | Alta | 2 | RN-28 | Mide el servicio de marketplace, de la Etapa 2. |
| RNF-68 | La restauración desde archivo frío de una operación de crédito de la cohorte más antigua debe completarse dentro del plazo objetivo. | <= 24 horas (supuesto fundamentado). | Prueba de restauración desde archivo frío. | Filial emisora | Alta | 1 | RN-36 | — |
| RNF-69 | La atención de garantía legal en mesón no debe derivar al consumidor a un tercero como condición de atención, en ninguna tienda. | 0 derivaciones como condición de atención, medido con cliente oculto en las 22 tiendas. | Programa de cliente oculto en las 22 tiendas. | Retail | Alta | 2 | RN-26 | Mide el servicio de posventa, de la Etapa 2. |
| RNF-70 | El ciclo de desarrollo debe producir un inventario de componentes (SBOM) por artefacto desplegado. | SBOM del 100 % de los artefactos desplegados. | Verificación del SBOM en cada liberación. | Ambos | Alta | 1 | RN-01, RN-06 | — |
| RNF-71 | La cadena de suministro de software debe alcanzar el nivel SLSA 3 o superior. | Nivel SLSA 3 o superior acreditado. | Atestación de la cadena de construcción por artefacto. | Ambos | Alta | 1 | RN-01, RN-06 | — |
| RNF-72 | La capa expuesta debe cumplir el estándar OWASP ASVS en el nivel comprometido. | 0 hallazgos críticos abiertos en el nivel ASVS comprometido. | Análisis estático y dinámico por ciclo y prueba de seguridad ofensiva. | Ambos | Alta | 1 | RN-01, RN-06 | — |
| RNF-73 | La arquitectura debe implementar un modelo Zero Trust conforme a NIST SP 800-207. | Verificación explícita en cada solicitud y denegación por omisión en el 100 % de los puntos de control. | Revisión de arquitectura contra los principios de NIST SP 800-207. | Ambos | Alta | 1 | RN-01, RN-06 | — |
| RNF-74 | Todo tratamiento de datos personales debe declarar su finalidad. | 100 % de los flujos con finalidad declarada. | Revisión del registro de actividades de tratamiento. | Ambos | Alta | 1 | RN-02, RN-03, RN-05 | — |
| RNF-75 | Todo tratamiento de datos personales debe invocar una de las bases de licitud de la Ley N° 21.719. | 100 % de los flujos con base de licitud declarada; 0 tratamientos con consentimiento presunto. | Auditoría de conformidad por el oficial de cumplimiento. | Ambos | Alta | 1 | RN-02, RN-03, RN-05 | — |
| RNF-76 | La compañía debe mantener el registro de actividades de tratamiento de datos personales. | Registro completo y vigente, actualizado ante cada cambio de flujo. | Revisión documental periódica contra el inventario de interfaces de RF-168. | Ambos | Alta | 1 | RN-02, RN-03, RN-05 | — |

## B.5 Obligaciones del proponente (OP)

| ID | Obligación | Verificación |
| :-- | :-- | :-- |
| OP-01 | El PROPONENTE debe especificar la alternativa de etiquetas electrónicas frente a las demás opciones de resolución de la discrepancia de precio. | — |
| OP-02 | El PROPONENTE debe costear la alternativa de etiquetas electrónicas sin asumir su adquisición dentro del alcance. | — |
| OP-03 | El PROPONENTE debe especificar la cobertura de despliegue de las etiquetas electrónicas. | — |
| OP-04 | El PROPONENTE debe especificar el hardware requerido por la alternativa de etiquetas electrónicas. | — |
| OP-05 | El PROPONENTE debe presentar el costo de la alternativa separadamente del resto de la solución. | — |
| OP-06 | El PROPONENTE debe especificar la cantidad de dispositivos móviles requeridos por tienda y por departamento. | — |
| OP-07 | El PROPONENTE debe especificar las características técnicas de los dispositivos móviles requeridos. | — |
| OP-08 | El PROPONENTE debe presentar el análisis de hacer o comprar del centro de distribución de Concepción con sus tres alternativas. | — |
| OP-09 | El PROPONENTE debe declarar el impacto de la alternativa seleccionada sobre el cumplimiento de RN-15. | — |
