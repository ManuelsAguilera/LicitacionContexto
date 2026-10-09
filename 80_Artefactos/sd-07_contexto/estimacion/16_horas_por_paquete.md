# Horas por paquete y por etapa para el Formulario T-15 (paso 9)

Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/repartir_horas_paquetes.py`; no editar a mano. Fecha: 2026-10-08. Estado: **parcial**. Los paquetes del UCP tienen horas; los demás esperan las planillas de tres valores del equipo (`12_plantilla_tres_valores.md`) y siguen «por estimar». El calendario por paquete y la curva por mes están en `17_cronograma_edt.md`; la dotación (P8.2) queda aparte.

## 1. Resumen

- Paquetes: 164. Con horas del UCP: 51. Con tres valores: 0. Por estimar: 113.
- Total del UCP (escenario del equipo, lectura B): 31.850 h, repartido en proporción al UUCW de los casos de cada paquete.
- Horas con valor hoy: 31.850 h.

## 2. Por rama

| Rama | Paquetes | Con horas | Horas |
| :-- | --: | --: | --: |
| 1.1 Dirección, gobierno y control del proyecto | 12 | 0 | por estimar |
| 1.2 Levantamiento y línea base de alcance | 8 | 0 | por estimar |
| 1.3 Arquitectura y diseño | 7 | 0 | por estimar |
| 1.4 Infraestructura híbrida y plataforma base | 13 | 0 | por estimar |
| 1.5 Desarrollo de software | 51 | 51 | 31.850 |
| 1.6 Integraciones | 7 | 0 | por estimar |
| 1.7 Migración y saneamiento de datos | 12 | 0 | por estimar |
| 1.8 Seguridad, identidad y cumplimiento | 8 | 0 | por estimar |
| 1.9 Calidad, pruebas y certificación | 12 | 0 | por estimar |
| 1.10 Innovaciones | 5 | 0 | por estimar |
| 1.11 Implantación y despliegue | 4 | 0 | por estimar |
| 1.12 Resultados de las marchas blancas y aceptación por etapa | 7 | 0 | por estimar |
| 1.13 Gestión del cambio y capacitación | 5 | 0 | por estimar |
| 1.14 Documentación, transferencia y reversibilidad | 7 | 0 | por estimar |
| 1.15 Operación y soporte | 6 | 0 | por estimar |
| **Total** | **164** | **51** | **31.850** |

## 3. Por etapa

La etapa de los paquetes de software es la de su servicio (sd-03); la cartera de crédito es de las dos etapas y no se reparte entre ellas sin un dato. Los paquetes que no son de software tienen la etapa «por definir» salvo los que el sd-03 fija. El UAW no tiene paquete propio: sus horas están dentro del reparto proporcional al UUCW. Por eso las cifras de la Etapa 1 y de la Etapa 2 difieren de las de `10_esfuerzo.md`, que asigna el UAW y toda la cartera de crédito a la Etapa 1.

| Etapa | Paquetes | Con horas | Horas |
| :-- | --: | --: | --: |
| 1 | 39 | 27 | 19.505 |
| 1 y 2 | 10 | 3 | 1.728 |
| 2 | 26 | 21 | 10.617 |
| desde el inicio del contrato | 25 | 0 | por estimar |
| operación | 6 | 0 | por estimar |
| por definir | 58 | 0 | por estimar |

## 4. Por paquete del UCP

| Paquete | Nombre | Servicio | UUCW | Etapa | Horas |
| :-- | :-- | :-- | --: | :-- | --: |
| 1.5.1.1 | Precio: cambio, propagación, consulta e historial | Servicio de oferta comercial | 25 | 1 | 1.234 |
| 1.5.1.2 | Etiquetas de exhibición y discrepancias de precio | Servicio de oferta comercial | 20 | 1 | 988 |
| 1.5.1.5 | Promociones y su vigencia | Servicio de oferta comercial | 10 | 1 | 494 |
| 1.5.1.6 | Maestro de artículos y reportes de calidad | Servicio de oferta comercial | 10 | 1 | 494 |
| 1.5.2.1 | Propuesta diaria de reposición y su ajuste | Servicio de abastecimiento | 10 | 2 | 494 |
| 1.5.2.2 | Órdenes de reposición a proveedores | Servicio de abastecimiento | 5 | 2 | 247 |
| 1.5.2.3 | Transferencias y recepción de mercadería | Servicio de abastecimiento | 10 | 2 | 494 |
| 1.5.3.1 | Disponible: cálculo, traza y consulta | Servicio de existencias | 25 | 1 | 1.234 |
| 1.5.3.2 | Reservas de existencia para el canal digital | Servicio de existencias | 25 | 1 | 1.234 |
| 1.5.3.4 | Conteo, exactitud del inventario, merma y probador | Servicio de existencias | 30 | 1 | 1.481 |
| 1.5.3.7 | Suspensión y degradación de la publicación por categoría | Servicio de existencias | 10 | 1 | 494 |
| 1.5.3.8 | Integración de existencias con el sistema de almacenes y con las planillas de Concepción | Servicio de existencias | 10 | 1 | 494 |
| 1.5.4.1 | Promesa de entrega, punto de despacho y elegibilidad del stock | Servicio de pedidos | 15 | 2 | 741 |
| 1.5.4.2 | Preautorización, cobro y anulación del pago del pedido | Servicio de pedidos | 20 | 2 | 988 |
| 1.5.4.3 | Resolución de pedidos sin existencia, reasignación y alternativas al cliente | Servicio de pedidos | 15 | 2 | 741 |
| 1.5.4.4 | Estado único del pedido y sus consultas | Servicio de pedidos | 15 | 2 | 741 |
| 1.5.4.5 | Seguimiento y cumplimiento de la promesa de entrega | Servicio de pedidos | 10 | 2 | 494 |
| 1.5.5.1 | Punto de venta nuevo: registro y cobro de ventas, reversas, cierre de caja y medios de pago | Servicio de ventas | 20 | 1 | 988 |
| 1.5.5.2 | Punto de venta con operación sin conexión: reconciliación y validación posterior | Servicio de ventas | 20 | 1 | 988 |
| 1.5.5.6 | Ventas del canal digital y enrutamiento de los documentos tributarios al sistema de gestión empresarial | Servicio de ventas | 10 | 1 | 494 |
| 1.5.5.7 | Cobro con la tarjeta de la casa | Servicio de ventas | 5 | 1 | 247 |
| 1.5.6.1 | Cálculo de la base de comisión | Servicio de comisiones | 5 | 2 | 247 |
| 1.5.6.2 | Entrega de la base de comisión al sistema de remuneraciones | Servicio de comisiones | 5 | 2 | 247 |
| 1.5.6.3 | Revisión de la atribución de comisiones | Servicio de comisiones | 5 | 2 | 247 |
| 1.5.7.1 | Existencia declarada por el vendedor y su publicación | Servicio de marketplace | 10 | 2 | 494 |
| 1.5.7.2 | Evaluación de vendedores y su consulta | Servicio de marketplace | 20 | 2 | 988 |
| 1.5.7.4 | Devoluciones, base de comisión y liquidación de marketplace | Servicio de marketplace | 15 | 2 | 741 |
| 1.5.7.5 | Identificación del vendedor y separación de la existencia propia | Servicio de marketplace | 10 | 2 | 494 |
| 1.5.8.1 | Atención de garantía legal en el mesón, con sus plazos | Servicio de posventa | 15 | 2 | 741 |
| 1.5.8.2 | Devolución y aptitud de la unidad devuelta | Servicio de posventa | 5 | 2 | 247 |
| 1.5.8.3 | Resolución al consumidor y recuperación contra el tercero responsable | Servicio de posventa | 5 | 2 | 247 |
| 1.5.9.1 | Consolidación de los registros de clientes | Servicio de clientes Retail | 5 | 2 | 247 |
| 1.5.9.2 | Puntos y sincronización con el sistema de fidelización | Servicio de clientes Retail | 5 | 2 | 247 |
| 1.5.9.3 | Segmentos y campañas con atributos comerciales | Servicio de clientes Retail | 10 | 2 | 494 |
| 1.5.10.1 | Evaluación crediticia, apertura de tarjeta y ampliación de cupo | Servicio de originación de crédito | 20 | 1 | 988 |
| 1.5.10.2 | Simulación del costo total del crédito con la tasa máxima vigente | Servicio de originación de crédito | 10 | 1 | 494 |
| 1.5.10.4 | Autorización de compra a cuotas sin enlace y sus topes | Servicio de originación de crédito | 15 | 1 | 741 |
| 1.5.11.1 | Mora y gestión de cobranza | Servicio de cartera de crédito | 10 | 1 y 2 | 494 |
| 1.5.11.2 | Repactación, pagos y estado de cuenta | Servicio de cartera de crédito | 15 | 1 y 2 | 741 |
| 1.5.11.5 | Conciliación diaria y convivencia con la plataforma de crédito de 2011 | Servicio de cartera de crédito | 10 | 1 y 2 | 494 |
| 1.5.12.1 | Información precontractual entregada, aceptada y consultable | Servicio de evidencia financiera | 15 | 1 | 741 |
| 1.5.12.2 | Consentimiento de modificaciones de condiciones y su enlace con la cobranza | Servicio de evidencia financiera | 10 | 1 | 494 |
| 1.5.12.3 | Reconstrucción y recuperación de la evidencia del consentimiento | Servicio de evidencia financiera | 10 | 1 | 494 |
| 1.5.13.1 | Inventario de flujos de cruce autorizados y registro de los cruces | Servicio de control de cruces | 10 | 1 | 494 |
| 1.5.13.2 | Rechazo de cruces no autorizados entre los ámbitos | Servicio de control de cruces | 10 | 1 | 494 |
| 1.5.13.3 | Correspondencia de identificadores y evaluación de impacto sobre la frontera | Servicio de control de cruces | 10 | 1 | 494 |
| 1.5.14.1 | Identidad individual y administración de identidades, roles y ámbitos | Base tecnológica | 10 | 1 | 494 |
| 1.5.14.2 | Habilitación, revocación y conciliación de accesos | Base tecnológica | 25 | 1 | 1.234 |
| 1.5.14.5 | Orden de degradación y ventanas de congelamiento | Base tecnológica | 10 | 1 | 494 |
| 1.5.14.6 | Plataforma de integración y convivencia con el sistema central de 2009 | Base tecnológica | 10 | 1 | 494 |
| 1.5.14.7 | Observabilidad y capacidad analítica | Base tecnológica | 10 | 1 | 494 |

## 5. Por paquete que el UCP no cubre

| Paquete | Nombre | Etapa | Fuente | Horas |
| :-- | :-- | :-- | :-- | --: |
| 1.1.1 | Plan de dirección integrado (ámbito, cronograma, costos, calidad, riesgos, comunicaciones, interesados y adquisiciones) | desde el inicio del contrato | por estimar | por estimar |
| 1.1.2 | EDT y diccionario de paquetes con entregable, criterio de aceptación y responsable | desde el inicio del contrato | por estimar | por estimar |
| 1.1.3 | Registro de solicitudes de cambio y su resolución | desde el inicio del contrato | por estimar | por estimar |
| 1.1.4 | Registros de riesgos, lecciones aprendidas, supuestos y consultas | desde el inicio del contrato | por estimar | por estimar |
| 1.1.6 | Calendario de ventanas de congelamiento y de eventos anuales con declaración de impacto por evento | desde el inicio del contrato | por estimar | por estimar |
| 1.1.7 | Actas de los comités e informe mensual de avance | desde el inicio del contrato | por estimar | por estimar |
| 1.1.9 | Reporte mensual de consumo de nube | desde el inicio del contrato | por estimar | por estimar |
| 1.1.10 | Actas de aceptación por entrega y habilitación de pagos | desde el inicio del contrato | por estimar | por estimar |
| 1.1.11 | Registro de garantías, seguros y certificados laborales vigentes | desde el inicio del contrato | por estimar | por estimar |
| 1.1.12 | Acta de constitución del proyecto | desde el inicio del contrato | por estimar | por estimar |
| 1.1.13 | Línea base de costos y presupuesto | desde el inicio del contrato | por estimar | por estimar |
| 1.1.14 | Planes alternativos de las dos condiciones del adelanto del negocio financiero | 1 | por estimar | por estimar |
| 1.2.1 | Mapa de las 14 interfaces e inventario de las 9 plataformas, 6 proveedores y dependencias | desde el inicio del contrato | por estimar | por estimar |
| 1.2.3 | Levantamiento de procesos, reglas de negocio y volumetría declarada | desde el inicio del contrato | por estimar | por estimar |
| 1.2.4 | Catálogo de requerimientos y matriz de trazabilidad | desde el inicio del contrato | por estimar | por estimar |
| 1.2.6 | Línea base de alcance por etapa, con exclusiones y supuestos | desde el inicio del contrato | por estimar | por estimar |
| 1.2.7 | Estudio de decisión con costeo sobre etiquetas electrónicas de precio | desde el inicio del contrato | por estimar | por estimar |
| 1.2.8 | Estudio de decisión con costeo sobre el sistema de almacenes de Concepción | desde el inicio del contrato | por estimar | por estimar |
| 1.2.9 | Estudio de decisión con costeo sobre el destino de las plataformas | desde el inicio del contrato | por estimar | por estimar |
| 1.2.10 | Propuesta de criterios del cupo preaprobado para la filial emisora | 1 | por estimar | por estimar |
| 1.3.1 | Documento de arquitectura con cinco vistas y catálogo de decisiones | desde el inicio del contrato | por estimar | por estimar |
| 1.3.3 | Arquitectura física con emplazamiento por componente justificado | desde el inicio del contrato | por estimar | por estimar |
| 1.3.4 | Modelo de datos con dominios segregados Retail y Emisor, frontera documentada y políticas de retención | desde el inicio del contrato | por estimar | por estimar |
| 1.3.5 | Contratos de integración versionados y su gobierno | desde el inicio del contrato | por estimar | por estimar |
| 1.3.6 | Especificación del modo desconectado de 24 horas y de la sincronización tras la reconexión | desde el inicio del contrato | por estimar | por estimar |
| 1.3.7 | Modelo de capacidad y dimensionamiento | desde el inicio del contrato | por estimar | por estimar |
| 1.3.8 | Especificación y costeo de las obras de infraestructura del cliente | desde el inicio del contrato | por estimar | por estimar |
| 1.4.1 | Entorno de nube con infraestructura como código, subredes privadas y etiquetado de costos | por definir | por estimar | por estimar |
| 1.4.2 | Configuración del borde por sitio y certificación de la red segmentada en las 13 tiendas que no la tienen | por definir | por estimar | por estimar |
| 1.4.3 | Entorno dedicado del ámbito emisor con segregación física y lógica acreditada | por definir | por estimar | por estimar |
| 1.4.4 | Ambientes de desarrollo, calidad, preproducción, producción y recuperación ante desastres | por definir | por estimar | por estimar |
| 1.4.5 | Plataforma de observabilidad unificada con catálogo de alertas | por definir | por estimar | por estimar |
| 1.4.6 | Plataforma de integración y entrega continuas con infraestructura como código | por definir | por estimar | por estimar |
| 1.4.7 | Licenciamiento de terceros a nombre del cliente | por definir | por estimar | por estimar |
| 1.4.8 | Especificación de hardware y dispositivos de terreno para adquisición del cliente | por definir | por estimar | por estimar |
| 1.4.9 | Plano y especificación del recinto técnico del centro de datos y coordinación de su obra civil de separación | por definir | por estimar | por estimar |
| 1.4.11 | Plan de cierre de la brecha del centro de datos frente al informe interno de 2024 | por definir | por estimar | por estimar |
| 1.4.12 | Sistemas de energía y climatización del centro de datos | por definir | por estimar | por estimar |
| 1.4.14 | Sistemas de seguridad física del centro de datos y espacio de operación del personal | por definir | por estimar | por estimar |
| 1.4.17 | Solución de respaldo en operación con custodia de medios | por definir | por estimar | por estimar |
| 1.6.1 | Catálogo de interfaces rediseñadas con contratos y niveles de servicio de integración | por definir | por estimar | por estimar |
| 1.6.2 | Rediseño de las integraciones de la Etapa 1 (precios y existencia, crédito con el sistema de gestión empresarial, cobranza y prevención de pérdidas) | por definir | por estimar | por estimar |
| 1.6.3 | Rediseño de las integraciones de la Etapa 2 (pedidos, marketplace y fidelización) | por definir | por estimar | por estimar |
| 1.6.9 | Canal de intercambio con los proveedores de mercadería | por definir | por estimar | por estimar |
| 1.6.10 | Entrega de reportes a las autoridades fiscalizadoras | por definir | por estimar | por estimar |
| 1.6.11 | Certificación de las integraciones con evidencia de conciliación | por definir | por estimar | por estimar |
| 1.6.12 | Modalidad de contingencia tributaria aprobada y probada con el ERP/DTE | 1 | por estimar | por estimar |
| 1.7.1 | Plan de migración con estrategia de corte y de retorno e inventario de datos históricos | por definir | por estimar | por estimar |
| 1.7.3 | Maestro de artículos saneado y validado (268.000 referencias) | por definir | por estimar | por estimar |
| 1.7.4 | Corte de inventario en las 24 instalaciones que no cierran | por definir | por estimar | por estimar |
| 1.7.5 | Migración del histórico comercial (ventas y pedidos) | por definir | por estimar | por estimar |
| 1.7.6 | Migración del padrón de clientes deduplicado, de los vendedores y de las liquidaciones | por definir | por estimar | por estimar |
| 1.7.7 | Migración de la cartera viva (620.000 clientes) con sus actas de conciliación | 1 y 2 | por estimar | por estimar |
| 1.7.9 | Repositorio de consulta de datos históricos no migrados | por definir | por estimar | por estimar |
| 1.7.10 | Plan de retiro de la plataforma de originación y cobranza de 2011 | por definir | por estimar | por estimar |
| 1.7.11 | Plataforma de originación y cobranza de 2011 fuera de servicio | por definir | por estimar | por estimar |
| 1.7.12 | Sistema central de retail de 2009 retirado | por definir | por estimar | por estimar |
| 1.7.13 | Sustitución del punto de venta de 2014 tienda por tienda y su retiro | 1 | por estimar | por estimar |
| 1.7.14 | Actas de compuerta por tramo de la cartera de crédito | 1 y 2 | por estimar | por estimar |
| 1.8.1 | Plan de seguridad, matriz de controles y modelo de amenazas | por definir | por estimar | por estimar |
| 1.8.3 | Declaración de superficie de exposición y plan de respuesta a incidentes | por definir | por estimar | por estimar |
| 1.8.5 | Modelo de identidad, matriz de roles y segregación de funciones, incluido el ámbito emisor | por definir | por estimar | por estimar |
| 1.8.6 | Cifrado y tokenización de los medios de pago | por definir | por estimar | por estimar |
| 1.8.7 | Protección de datos personales y matriz de cumplimiento normativo | por definir | por estimar | por estimar |
| 1.8.9 | Informe de pruebas de intrusión y plan de remediación | por definir | por estimar | por estimar |
| 1.8.10 | Informe de diligencia del proveedor de nube | por definir | por estimar | por estimar |
| 1.8.11 | Atestación de la cadena de suministro y revisión de la arquitectura de confianza cero | por definir | por estimar | por estimar |
| 1.9.1 | Plan de pruebas con niveles, tipos, ambientes, datos y calendario | por definir | por estimar | por estimar |
| 1.9.2 | Estándares de codificación, revisión por pares y puertas de calidad | por definir | por estimar | por estimar |
| 1.9.3 | Batería de pruebas funcionales y de requisitos no funcionales | por definir | por estimar | por estimar |
| 1.9.4 | Pruebas de desempeño, resiliencia y recuperación ante desastres | por definir | por estimar | por estimar |
| 1.9.6 | Ensayo de la estrategia de degradación del evento anual | por definir | por estimar | por estimar |
| 1.9.7 | Informes de aceptación por el usuario y de verificación de los 28 criterios de aceptación del caso | por definir | por estimar | por estimar |
| 1.9.8 | Certificación de calidad de la Etapa 1 | 1 | por estimar | por estimar |
| 1.9.9 | Certificación de calidad de la Etapa 2 | 2 | por estimar | por estimar |
| 1.9.11 | Informe de la prueba del corte de enlace provocado de 24 horas con retorno ensayado en el piloto | 1 | por estimar | por estimar |
| 1.9.12 | Informe de evaluación de comercio electrónico y fidelización con las pruebas de la Etapa 1 | 1 | por estimar | por estimar |
| 1.9.13 | Informe de pruebas de tareas del punto de venta con cajeros nuevos y experimentados | 1 | por estimar | por estimar |
| 1.9.14 | Informe de pruebas de comprensión de precios, entrega e información crediticia con clientes y titulares | 1 y 2 | por estimar | por estimar |
| 1.10.1 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | por estimar | por estimar |
| 1.10.2 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | por estimar | por estimar |
| 1.10.3 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | por estimar | por estimar |
| 1.10.4 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | por estimar | por estimar |
| 1.10.5 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | por estimar | por estimar |
| 1.11.1 | Plan de implantación con procedimiento de despliegue gradual y de reversión probado | 1 y 2 | por estimar | por estimar |
| 1.11.3 | Configuración y certificación de los sitios: 22 tiendas, 2 centros de distribución, 380 líneas de caja, 640 terminales y el nodo de borde de cada tienda | 1 y 2 | por estimar | por estimar |
| 1.11.4 | Plan de convivencia entre la Etapa 1 y la Etapa 2 con una única fuente de verdad | 2 | por estimar | por estimar |
| 1.11.5 | Piloto del punto de venta en tres tiendas | 1 | por estimar | por estimar |
| 1.12.1 | Plan de la marcha blanca de la Etapa 1 | 1 | por estimar | por estimar |
| 1.12.2 | Informe de resultados y evidencia de cierre de la marcha blanca de la Etapa 1 | 1 | por estimar | por estimar |
| 1.12.4 | Acta de aceptación de la Etapa 1 | 1 | por estimar | por estimar |
| 1.12.5 | Plan de la marcha blanca de la Etapa 2, en convivencia con la Etapa 1 en producción | 2 | por estimar | por estimar |
| 1.12.6 | Informe de resultados de la marcha blanca de la Etapa 2 | 2 | por estimar | por estimar |
| 1.12.7 | Acta de aceptación final y garantía de correcto funcionamiento | 2 | por estimar | por estimar |
| 1.12.9 | Informe del soporte de estabilización posterior a la puesta en marcha | 1 y 2 | por estimar | por estimar |
| 1.13.1 | Plan de gestión del cambio con diagnóstico por perfil y medición de adopción | por definir | por estimar | por estimar |
| 1.13.2 | Plan de capacitación por rol y materiales editables en español | por definir | por estimar | por estimar |
| 1.13.3 | Registro de capacitación ejecutada y certificación de administradores y equipo técnico, condición de cierre de cada marcha blanca | por definir | por estimar | por estimar |
| 1.13.4 | Informe de acompañamiento en puesto para el personal de tienda, temporero y externo | por definir | por estimar | por estimar |
| 1.13.5 | Plan de comunicación a los clientes de la cartera por tramo | 1 y 2 | por estimar | por estimar |
| 1.14.1 | Documentación técnica y funcional con inventario de componentes de software | por definir | por estimar | por estimar |
| 1.14.3 | Transferencia tecnológica de código fuente, artefactos de construcción, scripts de infraestructura y procedimientos de despliegue | por definir | por estimar | por estimar |
| 1.14.4 | Base de conocimiento y manuales de operación | por definir | por estimar | por estimar |
| 1.14.6 | Plan de Reversibilidad con exportación en formatos abiertos | por definir | por estimar | por estimar |
| 1.14.7 | Acta de cierre, traspaso final y acompañamiento de reversibilidad | por definir | por estimar | por estimar |
| 1.14.9 | Informe de lecciones aprendidas del proyecto | por definir | por estimar | por estimar |
| 1.14.10 | Protocolo de aceptación de entregas y del producto final | por definir | por estimar | por estimar |
| 1.15.1 | Mesa de servicio de tres niveles en operación | operación | por estimar | por estimar |
| 1.15.2 | Informes periódicos de nivel de servicio y de certificaciones | operación | por estimar | por estimar |
| 1.15.3 | Pruebas periódicas de recuperación ante desastres | operación | por estimar | por estimar |
| 1.15.4 | Mantención correctiva, preventiva y evolutiva | operación | por estimar | por estimar |
| 1.15.6 | Infraestructura en operación con su informe de gestión | operación | por estimar | por estimar |
| 1.15.8 | Jornadas anuales de actualización y capacitación de personal nuevo | operación | por estimar | por estimar |

## 6. Pruebas de la puerta

- P8.1 (las sumas por paquete, nodo y rama coinciden con el total): cumple.
- P8.2 (personas en el pico frente a la dotación): **pendiente**; la dotación es del sd-12, fuera de esta entrega.
- P8.3 (la curva por etapa cuadra con los meses 1 a 12, 13 a 18 y 21 a 56): **cumple para las horas del UCP** (`17_cronograma_edt.md`); la curva completa espera las horas de los demás paquetes.
- P8.4 (los totales coinciden con la memoria de capacidad y esfuerzo de la sección 3.4.1): **pendiente**; esa memoria no existe todavía.
