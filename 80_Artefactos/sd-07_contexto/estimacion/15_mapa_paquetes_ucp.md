# Mapa de paquetes de la EDT a servicios, casos de uso y método (paso 8c)

Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/generar_mapa_paquetes.py` a partir de `14_edt_corregida.md`; no editar a mano. Fecha: 2026-10-08. Cada fila es un paquete. «UCP» significa que sus horas salen del modelo de casos de uso; «tres valores» significa que las estima el equipo (`12_plantilla_tres_valores.md`). El UUCW es el peso de sus casos (5 por caso simple y 10 por caso medio).

207 paquetes: 73 cubiertos por el UCP (127 casos, UUCW 645) y 134 para tres valores.

## 1. Paquetes cubiertos por el UCP

| Paquete | Nombre | Servicio | Casos | RF | UUCW | Etapa |
| :-- | :-- | :-- | :-- | :-- | --: | :-- |
| 1.5.1.1 | Cambio y propagación del precio, con su consulta en línea | Servicio de oferta comercial | CU-OF-01, CU-OF-02, CU-OF-03 | RF-016 a RF-018, RF-030, RF-064 | 20 | 1 |
| 1.5.1.2 | Etiquetas de exhibición y estado de exhibición de la tienda | Servicio de oferta comercial | CU-OF-04, CU-OF-05 | RF-019, RF-020, RF-029 | 10 | 1 |
| 1.5.1.3 | Historial del precio publicado | Servicio de oferta comercial | CU-OF-06 | RF-021 | 5 | 1 |
| 1.5.1.4 | Resolución de discrepancias de precio entre la etiqueta y la caja | Servicio de oferta comercial | CU-OF-07, CU-OF-08 | RF-022 a RF-024, RF-028 | 10 | 1 |
| 1.5.1.5 | Promociones y su vigencia | Servicio de oferta comercial | CU-OF-09, CU-OF-10 | RF-032 a RF-034 | 10 | 1 |
| 1.5.1.6 | Maestro de artículos y reportes de calidad | Servicio de oferta comercial | CU-OF-11, CU-OF-12 | RF-142, RF-143, RF-147, RF-148 | 10 | 1 |
| 1.5.2.1 | Propuesta diaria de reposición y su ajuste | Servicio de abastecimiento | CU-AB-01, CU-AB-02 | RF-144 a RF-146 | 10 | 2 |
| 1.5.2.2 | Órdenes de reposición a proveedores | Servicio de abastecimiento | CU-AB-03 | — | 5 | 2 |
| 1.5.2.3 | Transferencias entre tiendas y centros de distribución | Servicio de abastecimiento | CU-AB-04 | — | 5 | 2 |
| 1.5.2.4 | Recepción de mercadería en tienda | Servicio de abastecimiento | CU-AB-05 | — | 5 | 2 |
| 1.5.3.1 | Cálculo del disponible con colchón de confianza y su traza | Servicio de existencias | CU-EX-03, CU-EX-08, CU-EX-09 | RF-036, RF-127 a RF-130, RF-149 a RF-152, RF-157 | 15 | 1 |
| 1.5.3.2 | Reservas de existencia para el canal digital | Servicio de existencias | CU-EX-04, CU-EX-05, CU-EX-06, CU-EX-07 | RF-035, RF-037 a RF-042, RF-044, RF-098 | 25 | 1 |
| 1.5.3.3 | Consulta de disponibilidad en sala y en línea | Servicio de existencias | CU-EX-01, CU-EX-02 | RF-065, RF-066, RF-087, RF-101, RF-160, RF-161 | 10 | 1 |
| 1.5.3.4 | Conteo cíclico y medición de la exactitud del inventario | Servicio de existencias | CU-EX-10, CU-EX-11, CU-EX-12 | RF-131 a RF-137, RF-158, RF-159, RF-162 | 15 | 1 |
| 1.5.3.5 | Clasificación de diferencias e informe mensual de merma | Servicio de existencias | CU-EX-13, CU-EX-14 | RF-138 a RF-141 | 10 | 1 |
| 1.5.3.6 | Gestión de las unidades en el probador | Servicio de existencias | CU-EX-15 | RF-153 a RF-156 | 5 | 1 |
| 1.5.3.7 | Suspensión y degradación de la publicación por categoría | Servicio de existencias | CU-EX-16, CU-EX-17 | RF-163, RF-164, RF-179, RF-182, RF-183 | 10 | 1 |
| 1.5.3.8 | Integración de existencias con el sistema de almacenes y con las planillas de Concepción | Servicio de existencias | CU-EX-18, CU-EX-19 | — | 10 | 1 |
| 1.5.4.1 | Fecha prometida de entrega y punto de despacho por costo total de servir | Servicio de pedidos | CU-PE-01, CU-PE-02 | RF-075 a RF-080 | 10 | 2 |
| 1.5.4.2 | Preautorización, cobro y anulación del pago del pedido | Servicio de pedidos | CU-PE-03, CU-PE-04, CU-PE-08, CU-PE-09 | RF-043, RF-045, RF-047 a RF-051 | 20 | 2 |
| 1.5.4.3 | Resolución de pedidos sin existencia, reasignación y alternativas al cliente | Servicio de pedidos | CU-PE-05, CU-PE-06, CU-PE-07 | RF-046, RF-056 a RF-061, RF-074 | 15 | 2 |
| 1.5.4.4 | Estado único del pedido y sus consultas | Servicio de pedidos | CU-PE-10, CU-PE-11, CU-PE-12 | RF-052, RF-067, RF-068, RF-072, RF-073 | 15 | 2 |
| 1.5.4.5 | Priorización de pedidos por tiempo restante y cumplimiento de la promesa | Servicio de pedidos | CU-PE-13 | RF-062, RF-063, RF-081 | 5 | 2 |
| 1.5.4.6 | Elegibilidad del stock de exhibición y límite de unidades por cliente | Servicio de pedidos | CU-PE-14 | RF-053, RF-180 | 5 | 2 |
| 1.5.4.7 | Seguimiento del pedido con el transportista hasta la entrega | Servicio de pedidos | CU-PE-15 | — | 5 | 2 |
| 1.5.5.1 | Registro y cobro de ventas, reversas y cierre de caja | Servicio de ventas | CU-VE-01, CU-VE-02, CU-VE-03 | RF-001 | 15 | 1 |
| 1.5.5.2 | Operación de la tienda sin enlace | Servicio de ventas | CU-VE-04 | RF-082 a RF-086 | 5 | 1 |
| 1.5.5.3 | Reconciliación de las ventas hechas sin enlace y su informe de excepciones | Servicio de ventas | CU-VE-05, CU-VE-06 | RF-088, RF-095 a RF-097, RF-099 | 10 | 1 |
| 1.5.5.4 | Validación posterior de las operaciones de crédito cursadas sin enlace | Servicio de ventas | CU-VE-07 | RF-094 | 5 | 1 |
| 1.5.5.5 | Desactivación de los medios de pago de mayor fricción | Servicio de ventas | CU-VE-08 | RF-181 | 5 | 1 |
| 1.5.5.6 | Ventas del canal digital y enrutamiento de los documentos tributarios al sistema de gestión empresarial | Servicio de ventas | CU-VE-09, CU-VE-10 | RF-100 | 10 | 1 |
| 1.5.5.7 | Cobro con la tarjeta de la casa | Servicio de ventas | CU-VE-11 | — | 5 | 1 |
| 1.5.6.1 | Cálculo de la base de comisión | Servicio de comisiones | CU-CM-01 | RF-054, RF-071 | 5 | 2 |
| 1.5.6.2 | Entrega de la base de comisión al sistema de remuneraciones | Servicio de comisiones | CU-CM-02 | RF-055 | 5 | 2 |
| 1.5.6.3 | Revisión de la atribución de comisiones | Servicio de comisiones | CU-CM-03 | — | 5 | 2 |
| 1.5.7.1 | Existencia declarada por el vendedor y su publicación | Servicio de marketplace | CU-MK-01, CU-MK-02 | RF-102 a RF-104, RF-109, RF-124 | 10 | 2 |
| 1.5.7.2 | Consulta del vendedor sobre pedidos, devoluciones y evaluación | Servicio de marketplace | CU-MK-03 | RF-110 a RF-112 | 5 | 2 |
| 1.5.7.3 | Evaluación de vendedores y consecuencias escalonadas | Servicio de marketplace | CU-MK-04, CU-MK-05, CU-MK-06 | RF-105, RF-119 a RF-123 | 15 | 2 |
| 1.5.7.4 | Devolución de productos de marketplace | Servicio de marketplace | CU-MK-07 | RF-106 a RF-108 | 5 | 2 |
| 1.5.7.5 | Identificación del vendedor y de las condiciones en la compra | Servicio de marketplace | CU-MK-08 | RF-113 a RF-116 | 5 | 2 |
| 1.5.7.6 | Separación de la existencia propia en pedidos intermediados | Servicio de marketplace | CU-MK-09 | RF-117, RF-118 | 5 | 2 |
| 1.5.7.7 | Base de comisión y liquidación de marketplace | Servicio de marketplace | CU-MK-10, CU-MK-11 | RF-125, RF-126 | 10 | 2 |
| 1.5.8.1 | Atención de garantía legal en el mesón, con sus plazos | Servicio de posventa | CU-PV-01, CU-PV-02, CU-PV-03 | RF-187, RF-188, RF-192 a RF-195 | 15 | 2 |
| 1.5.8.2 | Devolución y aptitud de la unidad devuelta | Servicio de posventa | CU-PV-04 | RF-189 a RF-191 | 5 | 2 |
| 1.5.8.3 | Resolución al consumidor y recuperación contra el tercero responsable | Servicio de posventa | CU-PV-05 | RF-196 a RF-198 | 5 | 2 |
| 1.5.9.1 | Consolidación de los registros de clientes | Servicio de clientes Retail | CU-CL-01 | RF-227 | 5 | 2 |
| 1.5.9.2 | Puntos y sincronización con el sistema de fidelización | Servicio de clientes Retail | CU-CL-02 | RF-228, RF-231 | 5 | 2 |
| 1.5.9.3 | Segmentos y campañas con atributos comerciales | Servicio de clientes Retail | CU-CL-03, CU-CL-04 | RF-229, RF-230 | 10 | 2 |
| 1.5.10.1 | Evaluación crediticia y apertura de tarjeta en el mostrador | Servicio de originación de crédito | CU-OR-01, CU-OR-02 | RF-220 a RF-225 | 10 | 1 |
| 1.5.10.2 | Simulación del costo total del crédito con la tasa máxima vigente | Servicio de originación de crédito | CU-OR-03, CU-OR-04 | RF-218, RF-219 | 10 | 1 |
| 1.5.10.3 | Control de los intentos de evaluación | Servicio de originación de crédito | CU-OR-05 | RF-226 | 5 | 1 |
| 1.5.10.4 | Autorización de compra a cuotas sin enlace y sus topes | Servicio de originación de crédito | CU-OR-06, CU-OR-07, CU-OR-08 | RF-089 a RF-093 | 15 | 1 |
| 1.5.10.5 | Ampliación de cupo con enlace | Servicio de originación de crédito | CU-OR-09 | — | 5 | 1 |
| 1.5.11.1 | Gestión de cobranza dentro de los límites normativos | Servicio de cartera de crédito | CU-CA-01 | RF-211 a RF-213 | 5 | 1 y 2 |
| 1.5.11.2 | Repactación y registro de pagos | Servicio de cartera de crédito | CU-CA-02, CU-CA-04 | — | 10 | 1 y 2 |
| 1.5.11.3 | Cálculo de la mora y actualización de cuentas | Servicio de cartera de crédito | CU-CA-05 | — | 5 | 1 y 2 |
| 1.5.11.4 | Estado de cuenta y documentos para el cliente | Servicio de cartera de crédito | CU-CA-03 | RF-069, RF-070 | 5 | 1 y 2 |
| 1.5.11.5 | Conciliación diaria y convivencia con la plataforma de crédito de 2011 | Servicio de cartera de crédito | CU-CA-06, CU-CA-07 | RF-216 | 10 | 1 y 2 |
| 1.5.12.1 | Información precontractual entregada, aceptada y consultable | Servicio de evidencia financiera | CU-EV-01, CU-EV-02, CU-EV-08 | RF-199 a RF-206, RF-217 | 15 | 1 |
| 1.5.12.2 | Consentimiento de modificaciones de condiciones y su enlace con la cobranza | Servicio de evidencia financiera | CU-EV-03, CU-EV-07 | RF-207, RF-208, RF-214, RF-215 | 10 | 1 |
| 1.5.12.3 | Reconstrucción y recuperación de la evidencia del consentimiento | Servicio de evidencia financiera | CU-EV-04, CU-EV-05 | RF-209, RF-210 | 10 | 1 |
| 1.5.13.1 | Inventario de flujos de cruce autorizados y registro de los cruces | Servicio de control de cruces | CU-CC-01, CU-CC-03 | RF-165 a RF-169 | 10 | 1 |
| 1.5.13.2 | Rechazo de cruces no autorizados entre los ámbitos | Servicio de control de cruces | CU-CC-02, CU-CC-04 | RF-170 a RF-172 | 10 | 1 |
| 1.5.13.3 | Tabla de correspondencia de identificadores | Servicio de control de cruces | CU-CC-05 | RF-173 a RF-175 | 5 | 1 |
| 1.5.13.4 | Evaluación de impacto de las iniciativas sobre la frontera de datos | Servicio de control de cruces | CU-CC-06 | RF-176 | 5 | 1 |
| 1.5.14.1 | Identidad individual y sesión en terminales compartidas | Base tecnológica | CU-BT-01 | RF-002 a RF-006 | 5 | 1 |
| 1.5.14.2 | Habilitación por capacitación y acceso temporal de externos | Base tecnológica | CU-BT-02, CU-BT-03, CU-BT-04 | RF-007 a RF-012 | 15 | 1 |
| 1.5.14.3 | Revocación de accesos y conciliación contra la nómina | Base tecnológica | CU-BT-05, CU-BT-06 | RF-013 a RF-015 | 10 | 1 |
| 1.5.14.4 | Administración de identidades, roles y ámbitos | Base tecnológica | CU-BT-12 | — | 5 | 1 |
| 1.5.14.5 | Orden de degradación y ventanas de congelamiento | Base tecnológica | CU-BT-07, CU-BT-08 | RF-177, RF-178, RF-184 a RF-186 | 10 | 1 |
| 1.5.14.6 | Plataforma de integración y convivencia con el sistema central de 2009 | Base tecnológica | CU-BT-09, CU-BT-10 | — | 10 | 1 |
| 1.5.14.7 | Observabilidad y alertas de la operación | Base tecnológica | CU-BT-11 | — | 5 | 1 |
| 1.5.14.8 | Capacidad analítica y tableros por ámbito | Base tecnológica | CU-BT-13 | — | 5 | 1 |

## 2. Paquetes para tres valores

| Paquete | Nombre | Etapa | Origen o frontera |
| :-- | :-- | :-- | :-- |
| 1.1.1 | Plan de dirección integrado (ámbito, cronograma, costos, calidad, riesgos, comunicaciones, interesados y adquisiciones) | desde el inicio del contrato | — |
| 1.1.2 | EDT y diccionario de paquetes con entregable, criterio de aceptación y responsable | desde el inicio del contrato | Formulario T-14 |
| 1.1.3 | Control integrado de cambios | desde el inicio del contrato | Art. 72 |
| 1.1.4 | Registro de riesgos y de lecciones aprendidas | desde el inicio del contrato | — |
| 1.1.5 | Registro de supuestos y de vacíos y consultas | desde el inicio del contrato | — |
| 1.1.6 | Calendario de ventanas de congelamiento y de eventos anuales con declaración de impacto por evento | desde el inicio del contrato | — |
| 1.1.7 | Actas de los comités del proyecto | desde el inicio del contrato | Art. 71 |
| 1.1.8 | Informe mensual de avance | desde el inicio del contrato | RT-19.06 |
| 1.1.9 | Reporte mensual de consumo de nube | desde el inicio del contrato | Art. 16.3 |
| 1.1.10 | Actas de aceptación por entrega y habilitación de pagos | desde el inicio del contrato | Art. 18 |
| 1.1.11 | Seguimiento de garantías, seguros y certificados laborales | desde el inicio del contrato | Art. 75.3 |
| 1.1.12 | Acta de constitución del proyecto | desde el inicio del contrato | — |
| 1.1.13 | Línea base de costos y presupuesto | desde el inicio del contrato | Ronda 0: 2.9 |
| 1.2.1 | Mapa de las 14 interfaces punto a punto existentes | desde el inicio del contrato | — |
| 1.2.2 | Inventario de las 9 plataformas, 6 proveedores y dependencias | desde el inicio del contrato | — |
| 1.2.3 | Levantamiento de procesos, reglas de negocio y volumetría declarada | desde el inicio del contrato | — |
| 1.2.4 | Mantención del catálogo de requerimientos trazado al origen | desde el inicio del contrato | Anexo B del sd-03 |
| 1.2.5 | Matriz de trazabilidad de origen, requerimiento, componente, paquete, prueba y criterio | desde el inicio del contrato | — |
| 1.2.6 | Línea base de alcance por etapa, con exclusiones y supuestos | desde el inicio del contrato | — |
| 1.2.7 | Estudio de decisión con costeo sobre etiquetas electrónicas de precio | desde el inicio del contrato | OP-01 a OP-05 |
| 1.2.8 | Estudio de decisión con costeo sobre el sistema de almacenes de Concepción | desde el inicio del contrato | OP-08, OP-09 |
| 1.2.9 | Estudio de decisión con costeo sobre el destino de las plataformas | desde el inicio del contrato | — |
| 1.3.1 | Documento de arquitectura con cinco vistas | desde el inicio del contrato | ISO 42010 |
| 1.3.2 | Catálogo de decisiones de arquitectura | desde el inicio del contrato | — |
| 1.3.3 | Arquitectura física con emplazamiento por componente justificado | desde el inicio del contrato | Art. 16.2 |
| 1.3.4 | Modelo de datos con dominios segregados Retail y Emisor, frontera documentada y políticas de retención | desde el inicio del contrato | RT-05.10 |
| 1.3.5 | Contratos de integración versionados y su gobierno | desde el inicio del contrato | — |
| 1.3.6 | Especificación del modo desconectado de 24 horas y de la sincronización tras la reconexión | desde el inicio del contrato | RT-03.10 de las Bases Transversales |
| 1.3.7 | Modelo de capacidad y dimensionamiento | desde el inicio del contrato | memoria de capacidad de la sección 3.4.1 del sd-03 |
| 1.3.8 | Especificación y costeo de las obras de infraestructura del cliente | desde el inicio del contrato | El cliente ejecuta |
| 1.4.1 | Entorno de nube con infraestructura como código, subredes privadas y etiquetado de costos | por definir | — |
| 1.4.2 | Configuración del entorno on-premise de borde por sitio | por definir | El hardware lo adquiere el cliente (SP-04) |
| 1.4.3 | Entorno dedicado del ámbito emisor con segregación física y lógica acreditada | por definir | — |
| 1.4.4 | Ambientes de desarrollo, calidad, preproducción, producción y recuperación ante desastres | por definir | — |
| 1.4.5 | Plataforma de observabilidad unificada con catálogo de alertas | por definir | frontera con el UCP: aquí el aprovisionamiento |
| 1.4.6 | Plataforma de integración y entrega continuas con infraestructura como código | por definir | Antes 1.5.10 |
| 1.4.7 | Licenciamiento de terceros a nombre del cliente | por definir | Agregado desde la guía de la EDT, sección 8 |
| 1.4.8 | Especificación de hardware y dispositivos de terreno para adquisición del cliente | por definir | Formulario T-11 |
| 1.4.9 | Plano de distribución interna y especificación del recinto técnico del centro de datos | por definir | Ronda 0: 1.15.3 |
| 1.4.10 | Especificación y coordinación de la obra civil de separación del centro de datos | por definir | El cliente ejecuta la obra (RT-06.06, RC-04) |
| 1.4.11 | Plan de cierre de la brecha del centro de datos frente al informe interno de 2024 | por definir | Ronda 0: 1.15.4 |
| 1.4.12 | Sistema de energía ininterrumpida y generación autónoma del centro de datos | por definir | RT-06.07, RT-06.08 |
| 1.4.13 | Sistema de climatización de precisión con monitoreo ambiental del centro de datos | por definir | RT-06.13, RT-06.14 |
| 1.4.14 | Sistema de detección temprana y extinción automática de incendios del centro de datos | por definir | RT-06.16, RT-06.17 |
| 1.4.15 | Control de acceso físico biométrico y videovigilancia del centro de datos | por definir | RT-06.20 a RT-06.24 |
| 1.4.16 | Espacio de operación del personal habilitado, separado de la sala de equipos | por definir | Ronda 0: 1.15.11 |
| 1.4.17 | Solución de respaldo en operación | por definir | RT-07.09 |
| 1.4.18 | Servicio de custodia de medios de respaldo del centro de datos | por definir | RT-06.26 |
| 1.4.19 | Configuración y certificación de la red segmentada en las 13 tiendas que no la tienen | por definir | El cliente adquiere el hardware y ejecuta las obras (EXC-19, SP-04) |
| 1.6.1 | Catálogo de interfaces rediseñadas con contratos y niveles de servicio de integración | por definir | — |
| 1.6.2 | Rediseño de las integraciones de precios y existencia hacia los canales | por definir | — |
| 1.6.3 | Rediseño de la integración de pedidos | por definir | — |
| 1.6.4 | Rediseño de la integración del crédito con el sistema de gestión empresarial | por definir | — |
| 1.6.5 | Rediseño de la integración con el marketplace | por definir | — |
| 1.6.6 | Rediseño de la integración de cobranza | por definir | — |
| 1.6.7 | Rediseño de la integración con el sistema de fidelización | por definir | — |
| 1.6.8 | Rediseño de la integración de prevención de pérdidas | por definir | — |
| 1.6.9 | Canal de intercambio con los proveedores de mercadería | por definir | 940 proveedores |
| 1.6.10 | Entrega de reportes a las autoridades fiscalizadoras | por definir | — |
| 1.6.11 | Certificación de las integraciones con evidencia de conciliación | por definir | — |
| 1.7.1 | Plan de migración con estrategia de corte y de retorno | por definir | RT-05.11 |
| 1.7.2 | Inventario de datos históricos a migrar | por definir | RT-05.15 |
| 1.7.3 | Maestro de artículos saneado y validado (268.000 referencias) | por definir | — |
| 1.7.4 | Corte de inventario en las 24 instalaciones que no cierran | por definir | — |
| 1.7.5 | Migración del histórico comercial (ventas y pedidos) | por definir | — |
| 1.7.6 | Migración del padrón de clientes deduplicado, de los vendedores y de las liquidaciones | por definir | — |
| 1.7.7 | Migración de la cartera viva (620.000 clientes) con convivencia, conciliación diaria y retorno probado | 1 y 2 | Resultado 24 del Anexo D |
| 1.7.8 | Actas de conciliación de la corrida paralela y de cuadratura previa y posterior a la migración | por definir | — |
| 1.7.9 | Repositorio de consulta de datos históricos no migrados | por definir | Ronda 0: 1.30 |
| 1.7.10 | Plan de retiro de la plataforma de originación y cobranza de 2011 | por definir | Ronda 0: 3.11 |
| 1.7.11 | Plataforma de originación y cobranza de 2011 fuera de servicio | por definir | Ronda 0: 1.17b |
| 1.7.12 | Sistema central de retail de 2009 retirado | por definir | SP-01 y elección del escenario B en el sd-03 |
| 1.8.1 | Plan de seguridad y matriz de controles | por definir | — |
| 1.8.2 | Modelo de amenazas | por definir | — |
| 1.8.3 | Declaración de superficie de exposición | por definir | — |
| 1.8.4 | Plan de respuesta a incidentes de seguridad | por definir | — |
| 1.8.5 | Modelo de identidad, matriz de roles y segregación de funciones, incluido el ámbito emisor | por definir | frontera con el UCP: aquí el diseño |
| 1.8.6 | Cifrado y tokenización de los medios de pago | por definir | RNF-33, RNF-34 |
| 1.8.7 | Protección de datos personales y registro de actividades de tratamiento | por definir | Ley 21.719 |
| 1.8.8 | Matriz de cumplimiento normativo con control y evidencia | por definir | Art. 27 |
| 1.8.9 | Informe de pruebas de intrusión y plan de remediación | por definir | — |
| 1.8.10 | Informe de diligencia del proveedor de nube | por definir | Ronda 0: 3.13 |
| 1.8.11 | Atestación de la cadena de suministro de software | por definir | RNF-70, RNF-71 |
| 1.8.12 | Revisión de la arquitectura de confianza cero | por definir | RNF-73 |
| 1.9.1 | Plan de pruebas con niveles, tipos, ambientes, datos y calendario | por definir | Formulario T-13 |
| 1.9.2 | Puertas de calidad con análisis estático, cobertura y umbrales | por definir | ISO 25010 |
| 1.9.3 | Batería de pruebas funcionales y de requisitos no funcionales | por definir | ISO 29119 |
| 1.9.4 | Batería de pruebas de carga, estrés y resiliencia | por definir | RNF-22, RNF-23 |
| 1.9.5 | Batería de pruebas de recuperación ante desastres | por definir | RNF-32 |
| 1.9.6 | Ensayo de la estrategia de degradación del evento anual | por definir | Resultado 25 del Anexo D |
| 1.9.7 | Informes de aceptación por el usuario y de verificación de los 28 criterios de aceptación del caso | por definir | — |
| 1.9.8 | Certificación de calidad de la Etapa 1 | 1 | — |
| 1.9.9 | Certificación de calidad de la Etapa 2 | 2 | — |
| 1.9.10 | Estándares de codificación y lista de revisión por pares | por definir | Ronda 0: 3.2a |
| 1.10.1 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | RT-26.02 |
| 1.10.2 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | RT-26.02 |
| 1.10.3 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | RT-26.02 |
| 1.10.4 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | RT-26.02 |
| 1.10.5 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | RT-26.02 |
| 1.11.1 | Plan de implantación y puesta en marcha con criterios de éxito medibles | 1 y 2 | Formulario T-18 |
| 1.11.2 | Procedimiento de despliegue gradual y de reversión probado | 1 y 2 | — |
| 1.11.3 | Configuración y certificación de los sitios: 22 tiendas, 2 centros de distribución, 380 líneas de caja, 640 terminales y el nodo de borde de cada tienda | 1 y 2 | El cliente adquiere y ejecuta (EXC-19, SP-04) |
| 1.11.4 | Plan de convivencia entre la Etapa 1 y la Etapa 2 con una única fuente de verdad | 2 | — |
| 1.12.1 | Plan de la marcha blanca de la Etapa 1 | 1 | — |
| 1.12.2 | Informe de resultados de la marcha blanca de la Etapa 1, con medición diaria y conciliación | 1 | — |
| 1.12.3 | Evidencia de cierre de la Etapa 1 contra las condiciones del Caso | 1 | Caso, numeral 17.3 |
| 1.12.4 | Acta de aceptación de la Etapa 1 | 1 | — |
| 1.12.5 | Plan de la marcha blanca de la Etapa 2, en convivencia con la Etapa 1 en producción | 2 | — |
| 1.12.6 | Informe de resultados de la marcha blanca de la Etapa 2 | 2 | — |
| 1.12.7 | Acta de aceptación final de la implementación | 2 | — |
| 1.12.8 | Garantía de correcto funcionamiento | 2 | — |
| 1.12.9 | Informe del soporte de estabilización posterior a la puesta en marcha | 1 y 2 | — |
| 1.13.1 | Plan de gestión del cambio con diagnóstico por perfil y medición de adopción | por definir | Art. 89 |
| 1.13.2 | Plan de capacitación por rol y materiales editables en español | por definir | Art. 90 |
| 1.13.3 | Registro de capacitación ejecutada y certificación de administradores y equipo técnico, condición de cierre de cada marcha blanca | por definir | — |
| 1.13.4 | Programa de acompañamiento en puesto para el personal de tienda, temporero y externo | por definir | 62 % de rotación anual, 1.900 temporeros y unos 1.100 externos |
| 1.14.1 | Documentación técnica y funcional por categoría | por definir | Art. 91 |
| 1.14.2 | Inventario de componentes de software por artefacto desplegado | por definir | RNF-70 |
| 1.14.3 | Transferencia tecnológica de código fuente, artefactos de construcción, scripts de infraestructura y procedimientos de despliegue | por definir | Art. 77.1 |
| 1.14.4 | Base de conocimiento de incidentes, problemas, soluciones y decisiones de diseño | por definir | Art. 77.1 |
| 1.14.5 | Manuales de operación, libros de operación y guías de resolución de fallas | por definir | Art. 77.1 |
| 1.14.6 | Plan de Reversibilidad con exportación en formatos abiertos | por definir | Art. 77.2 |
| 1.14.7 | Acompañamiento de reversibilidad posterior al cierre | por definir | Art. 77.2 |
| 1.14.8 | Acta de cierre y traspaso final a operaciones | por definir | Art. 87 |
| 1.14.9 | Informe de lecciones aprendidas del proyecto | por definir | — |
| 1.14.10 | Protocolo de aceptación de entregas y del producto final | por definir | Formulario T-17 |
| 1.15.1 | Mesa de servicio de tres niveles | operación | Art. 78 |
| 1.15.2 | Informe mensual de nivel de servicio | operación | Art. 79.2 |
| 1.15.3 | Pruebas periódicas de recuperación ante desastres | operación | el sd-03 las fija dos veces al año |
| 1.15.4 | Mantención correctiva | operación | Agregado desde el sd-03 y las Bases |
| 1.15.5 | Mantención preventiva y evolutiva con mejora continua del nivel de servicio | operación | base del sd-11 |
| 1.15.6 | Gestión de la infraestructura en operación | operación | Agregado desde el sd-03 |
| 1.15.7 | Informe anual de certificaciones y soporte a auditorías e inspecciones | operación | Arts. 27, 74.6 |
| 1.15.8 | Jornadas anuales de actualización y capacitación de personal nuevo | operación | Art. 90.5 |

## 3. UUCW por servicio

| Servicio | Paquetes | Casos | UUCW |
| :-- | --: | --: | --: |
| Servicio de oferta comercial | 6 | 12 | 65 |
| Servicio de abastecimiento | 4 | 5 | 25 |
| Servicio de existencias | 8 | 19 | 100 |
| Servicio de pedidos | 7 | 15 | 75 |
| Servicio de ventas | 7 | 11 | 55 |
| Servicio de comisiones | 3 | 3 | 15 |
| Servicio de marketplace | 7 | 11 | 55 |
| Servicio de posventa | 3 | 5 | 25 |
| Servicio de clientes Retail | 3 | 4 | 20 |
| Servicio de originación de crédito | 5 | 9 | 45 |
| Servicio de cartera de crédito | 5 | 7 | 35 |
| Servicio de evidencia financiera | 3 | 7 | 35 |
| Servicio de control de cruces | 4 | 6 | 30 |
| Base tecnológica | 8 | 13 | 65 |
| **Total** | **73** | **127** | **645** |
