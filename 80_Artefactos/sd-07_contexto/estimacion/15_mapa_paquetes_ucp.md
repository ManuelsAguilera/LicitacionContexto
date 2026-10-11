# Mapa de paquetes de la EDT a servicios, casos de uso y método (paso 8c)

Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/generar_mapa_paquetes.py` a partir de `14_edt_corregida.md`; no editar a mano. Fecha: 2026-10-08. Cada fila es un paquete. «UCP» significa que sus horas salen del modelo de casos de uso; «tres valores» significa que las estima el equipo (`12_plantilla_tres_valores.md`). El UUCW es el peso de sus casos (5 por caso simple y 10 por caso medio).

164 paquetes: 51 cubiertos por el UCP (127 casos, UUCW 645) y 113 para tres valores.

## 1. Paquetes cubiertos por el UCP

| Paquete | Nombre | Servicio | Casos | RF | UUCW | Etapa |
| :-- | :-- | :-- | :-- | :-- | --: | :-- |
| 1.5.1.1 | Precio: cambio, propagación, consulta e historial | Servicio de oferta comercial | CU-OF-01, CU-OF-02, CU-OF-03, CU-OF-06 | RF-016 a RF-018, RF-021, RF-030, RF-064 | 25 | 1 |
| 1.5.1.2 | Etiquetas de exhibición y discrepancias de precio | Servicio de oferta comercial | CU-OF-04, CU-OF-05, CU-OF-07, CU-OF-08 | RF-019, RF-020, RF-022 a RF-024, RF-028, RF-029 | 20 | 1 |
| 1.5.1.5 | Promociones y su vigencia | Servicio de oferta comercial | CU-OF-09, CU-OF-10 | RF-032 a RF-034 | 10 | 1 |
| 1.5.1.6 | Maestro de artículos y reportes de calidad | Servicio de oferta comercial | CU-OF-11, CU-OF-12 | RF-142, RF-143, RF-147, RF-148 | 10 | 1 |
| 1.5.2.1 | Propuesta diaria de reposición y su ajuste | Servicio de abastecimiento | CU-AB-01, CU-AB-02 | RF-144 a RF-146 | 10 | 2 |
| 1.5.2.2 | Órdenes de reposición a proveedores | Servicio de abastecimiento | CU-AB-03 | — | 5 | 2 |
| 1.5.2.3 | Transferencias y recepción de mercadería | Servicio de abastecimiento | CU-AB-04, CU-AB-05 | — | 10 | 2 |
| 1.5.3.1 | Disponible: cálculo, traza y consulta | Servicio de existencias | CU-EX-03, CU-EX-08, CU-EX-09, CU-EX-01, CU-EX-02 | RF-036, RF-065, RF-066, RF-087, RF-101, RF-127 a RF-130, RF-149 a RF-152, RF-157, RF-160, RF-161 | 25 | 1 |
| 1.5.3.2 | Reservas de existencia para el canal digital | Servicio de existencias | CU-EX-04, CU-EX-05, CU-EX-06, CU-EX-07 | RF-035, RF-037 a RF-042, RF-044, RF-098 | 25 | 1 |
| 1.5.3.4 | Conteo, exactitud del inventario, merma y probador | Servicio de existencias | CU-EX-10, CU-EX-11, CU-EX-12, CU-EX-13, CU-EX-14, CU-EX-15 | RF-131 a RF-141, RF-153 a RF-156, RF-158, RF-159, RF-162 | 30 | 1 |
| 1.5.3.7 | Suspensión y degradación de la publicación por categoría | Servicio de existencias | CU-EX-16, CU-EX-17 | RF-163, RF-164, RF-179, RF-182, RF-183 | 10 | 1 |
| 1.5.3.8 | Integración de existencias con el sistema de almacenes y con las planillas de Concepción | Servicio de existencias | CU-EX-18, CU-EX-19 | — | 10 | 1 |
| 1.5.4.1 | Promesa de entrega, punto de despacho y elegibilidad del stock | Servicio de pedidos | CU-PE-01, CU-PE-02, CU-PE-14 | RF-053, RF-075 a RF-080, RF-180 | 15 | 2 |
| 1.5.4.2 | Preautorización, cobro y anulación del pago del pedido | Servicio de pedidos | CU-PE-03, CU-PE-04, CU-PE-08, CU-PE-09 | RF-043, RF-045, RF-047 a RF-051 | 20 | 2 |
| 1.5.4.3 | Resolución de pedidos sin existencia, reasignación y alternativas al cliente | Servicio de pedidos | CU-PE-05, CU-PE-06, CU-PE-07 | RF-046, RF-056 a RF-061, RF-074 | 15 | 2 |
| 1.5.4.4 | Estado único del pedido y sus consultas | Servicio de pedidos | CU-PE-10, CU-PE-11, CU-PE-12 | RF-052, RF-067, RF-068, RF-072, RF-073 | 15 | 2 |
| 1.5.4.5 | Seguimiento y cumplimiento de la promesa de entrega | Servicio de pedidos | CU-PE-13, CU-PE-15 | RF-062, RF-063, RF-081 | 10 | 2 |
| 1.5.5.1 | Punto de venta nuevo: registro y cobro de ventas, reversas, cierre de caja y medios de pago | Servicio de ventas | CU-VE-01, CU-VE-02, CU-VE-03, CU-VE-08 | RF-001, RF-181 | 20 | 1 |
| 1.5.5.2 | Punto de venta con operación sin conexión: reconciliación y validación posterior | Servicio de ventas | CU-VE-04, CU-VE-05, CU-VE-06, CU-VE-07 | RF-082 a RF-086, RF-088, RF-094 a RF-097, RF-099 | 20 | 1 |
| 1.5.5.6 | Ventas del canal digital y enrutamiento de los documentos tributarios al sistema de gestión empresarial | Servicio de ventas | CU-VE-09, CU-VE-10 | RF-100 | 10 | 1 |
| 1.5.5.7 | Cobro con la tarjeta de la casa | Servicio de ventas | CU-VE-11 | — | 5 | 1 |
| 1.5.6.1 | Cálculo de la base de comisión | Servicio de comisiones | CU-CM-01 | RF-054, RF-071 | 5 | 2 |
| 1.5.6.2 | Entrega de la base de comisión al sistema de remuneraciones | Servicio de comisiones | CU-CM-02 | RF-055 | 5 | 2 |
| 1.5.6.3 | Revisión de la atribución de comisiones | Servicio de comisiones | CU-CM-03 | — | 5 | 2 |
| 1.5.7.1 | Existencia declarada por el vendedor y su publicación | Servicio de marketplace | CU-MK-01, CU-MK-02 | RF-102 a RF-104, RF-109, RF-124 | 10 | 2 |
| 1.5.7.2 | Evaluación de vendedores y su consulta | Servicio de marketplace | CU-MK-03, CU-MK-04, CU-MK-05, CU-MK-06 | RF-105, RF-110 a RF-112, RF-119 a RF-123 | 20 | 2 |
| 1.5.7.4 | Devoluciones, base de comisión y liquidación de marketplace | Servicio de marketplace | CU-MK-07, CU-MK-10, CU-MK-11 | RF-106 a RF-108, RF-125, RF-126 | 15 | 2 |
| 1.5.7.5 | Identificación del vendedor y separación de la existencia propia | Servicio de marketplace | CU-MK-08, CU-MK-09 | RF-113 a RF-118 | 10 | 2 |
| 1.5.8.1 | Atención de garantía legal en el mesón, con sus plazos | Servicio de posventa | CU-PV-01, CU-PV-02, CU-PV-03 | RF-187, RF-188, RF-192 a RF-195 | 15 | 2 |
| 1.5.8.2 | Devolución y aptitud de la unidad devuelta | Servicio de posventa | CU-PV-04 | RF-189 a RF-191 | 5 | 2 |
| 1.5.8.3 | Resolución al consumidor y recuperación contra el tercero responsable | Servicio de posventa | CU-PV-05 | RF-196 a RF-198 | 5 | 2 |
| 1.5.9.1 | Consolidación de los registros de clientes | Servicio de clientes Retail | CU-CL-01 | RF-227 | 5 | 2 |
| 1.5.9.2 | Puntos y sincronización con el sistema de fidelización | Servicio de clientes Retail | CU-CL-02 | RF-228, RF-231 | 5 | 2 |
| 1.5.9.3 | Segmentos y campañas con atributos comerciales | Servicio de clientes Retail | CU-CL-03, CU-CL-04 | RF-229, RF-230 | 10 | 2 |
| 1.5.10.1 | Evaluación crediticia, apertura de tarjeta y ampliación de cupo | Servicio de originación de crédito | CU-OR-01, CU-OR-02, CU-OR-05, CU-OR-09 | RF-220 a RF-226 | 20 | 1 |
| 1.5.10.2 | Simulación del costo total del crédito con la tasa máxima vigente | Servicio de originación de crédito | CU-OR-03, CU-OR-04 | RF-218, RF-219 | 10 | 1 |
| 1.5.10.4 | Autorización de compra a cuotas sin enlace y sus topes | Servicio de originación de crédito | CU-OR-06, CU-OR-07, CU-OR-08 | RF-089 a RF-093 | 15 | 1 |
| 1.5.11.1 | Mora y gestión de cobranza | Servicio de cartera de crédito | CU-CA-01, CU-CA-05 | RF-211 a RF-213 | 10 | 1 y 2 |
| 1.5.11.2 | Repactación, pagos y estado de cuenta | Servicio de cartera de crédito | CU-CA-02, CU-CA-04, CU-CA-03 | RF-069, RF-070 | 15 | 1 y 2 |
| 1.5.11.5 | Conciliación diaria y convivencia con la plataforma de crédito de 2011 | Servicio de cartera de crédito | CU-CA-06, CU-CA-07 | RF-216 | 10 | 1 y 2 |
| 1.5.12.1 | Información precontractual entregada, aceptada y consultable | Servicio de evidencia financiera | CU-EV-01, CU-EV-02, CU-EV-08 | RF-199 a RF-206, RF-217 | 15 | 1 |
| 1.5.12.2 | Consentimiento de modificaciones de condiciones y su enlace con la cobranza | Servicio de evidencia financiera | CU-EV-03, CU-EV-07 | RF-207, RF-208, RF-214, RF-215 | 10 | 1 |
| 1.5.12.3 | Reconstrucción y recuperación de la evidencia del consentimiento | Servicio de evidencia financiera | CU-EV-04, CU-EV-05 | RF-209, RF-210 | 10 | 1 |
| 1.5.13.1 | Inventario de flujos de cruce autorizados y registro de los cruces | Servicio de control de cruces | CU-CC-01, CU-CC-03 | RF-165 a RF-169 | 10 | 1 |
| 1.5.13.2 | Rechazo de cruces no autorizados entre los ámbitos | Servicio de control de cruces | CU-CC-02, CU-CC-04 | RF-170 a RF-172 | 10 | 1 |
| 1.5.13.3 | Correspondencia de identificadores y evaluación de impacto sobre la frontera | Servicio de control de cruces | CU-CC-05, CU-CC-06 | RF-173 a RF-176 | 10 | 1 |
| 1.5.14.1 | Identidad individual y administración de identidades, roles y ámbitos | Base tecnológica | CU-BT-01, CU-BT-12 | RF-002 a RF-006 | 10 | 1 |
| 1.5.14.2 | Habilitación, revocación y conciliación de accesos | Base tecnológica | CU-BT-02, CU-BT-03, CU-BT-04, CU-BT-05, CU-BT-06 | RF-007 a RF-015 | 25 | 1 |
| 1.5.14.5 | Orden de degradación y ventanas de congelamiento | Base tecnológica | CU-BT-07, CU-BT-08 | RF-177, RF-178, RF-184 a RF-186 | 10 | 1 |
| 1.5.14.6 | Plataforma de integración y convivencia con el sistema central de 2009 | Base tecnológica | CU-BT-09, CU-BT-10 | — | 10 | 1 |
| 1.5.14.7 | Observabilidad y capacidad analítica | Base tecnológica | CU-BT-11, CU-BT-13 | — | 10 | 1 |

## 2. Paquetes para tres valores

| Paquete | Nombre | Etapa | Origen o frontera |
| :-- | :-- | :-- | :-- |
| 1.1.1 | Plan de dirección integrado (ámbito, cronograma, costos, calidad, riesgos, comunicaciones, interesados y adquisiciones) | desde el inicio del contrato | — |
| 1.1.2 | EDT y diccionario de paquetes con entregable, criterio de aceptación y responsable | desde el inicio del contrato | Formulario T-14 |
| 1.1.3 | Registro de solicitudes de cambio y su resolución | desde el inicio del contrato | Art. 72 |
| 1.1.4 | Registros de riesgos, lecciones aprendidas, supuestos y consultas | desde el inicio del contrato | sd-03, 3.2.3 (supuestos y Tabla 3.3) |
| 1.1.6 | Calendario de ventanas de congelamiento y de eventos anuales con declaración de impacto por evento | desde el inicio del contrato | sd-03, 3.2.2 y 3.2.3 (ventanas de congelamiento) |
| 1.1.7 | Actas de los comités e informe mensual de avance | desde el inicio del contrato | Art. 71; RT-19.06 |
| 1.1.9 | Reporte mensual de consumo de nube | desde el inicio del contrato | Art. 16.3; RT-03.06 |
| 1.1.10 | Actas de aceptación por entrega y habilitación de pagos | desde el inicio del contrato | Art. 18; E-25 |
| 1.1.11 | Registro de garantías, seguros y certificados laborales vigentes | desde el inicio del contrato | Art. 75.3 |
| 1.1.12 | Acta de constitución del proyecto | desde el inicio del contrato | — |
| 1.1.13 | Línea base de costos y presupuesto | desde el inicio del contrato | Ronda 0: 2.9; los valores viven solo en la oferta económica |
| 1.1.14 | Planes alternativos de las dos condiciones del adelanto del negocio financiero | 1 | sd-03, 3.2.3; el detalle se resuelve en el plan de trabajo y en el análisis de riesgos |
| 1.2.1 | Mapa de las 14 interfaces e inventario de las 9 plataformas, 6 proveedores y dependencias | desde el inicio del contrato | sd-03, 3.3.1 (el levantamiento documenta las catorce interfaces y las nueve plataformas) |
| 1.2.3 | Levantamiento de procesos, reglas de negocio y volumetría declarada | desde el inicio del contrato | sd-03, 3.2.4 (reglas de negocio) y 3.4.1 (volumetría del Caso) |
| 1.2.4 | Catálogo de requerimientos y matriz de trazabilidad | desde el inicio del contrato | Anexo B del sd-03 |
| 1.2.6 | Línea base de alcance por etapa, con exclusiones y supuestos | desde el inicio del contrato | sd-03, 3.2.2 y 3.2.3 (reparto por etapa, exclusiones y supuestos; Tablas 3.1 y 3.3) |
| 1.2.7 | Estudio de decisión con costeo sobre etiquetas electrónicas de precio | desde el inicio del contrato | OP-01 a OP-05 |
| 1.2.8 | Estudio de decisión con costeo sobre el sistema de almacenes de Concepción | desde el inicio del contrato | OP-08, OP-09 |
| 1.2.9 | Estudio de decisión con costeo sobre el destino de las plataformas | desde el inicio del contrato | sd-03, 3.2.1 y 3.3.1 (destino de las nueve plataformas; SD-06 programa la decisión) |
| 1.2.10 | Propuesta de criterios del cupo preaprobado para la filial emisora | 1 | sd-03, 3.2.3; la filial emisora los fija antes de la prueba (RC-11) |
| 1.3.1 | Documento de arquitectura con cinco vistas y catálogo de decisiones | desde el inicio del contrato | ISO 42010 |
| 1.3.3 | Arquitectura física con emplazamiento por componente justificado | desde el inicio del contrato | Art. 16.2; zonas a nombrar conforme al sd-04 |
| 1.3.4 | Modelo de datos con dominios segregados Retail y Emisor, frontera documentada y políticas de retención | desde el inicio del contrato | RT-05.10 |
| 1.3.5 | Contratos de integración versionados y su gobierno | desde el inicio del contrato | sd-03, 3.3.2 (contratos y adaptadores de la plataforma común) |
| 1.3.6 | Especificación del modo desconectado de 24 horas y de la sincronización tras la reconexión | desde el inicio del contrato | RT-03.10 de las Bases Transversales; el código RT-03.13 significa cosas distintas en el Caso y en las Transversales |
| 1.3.7 | Modelo de capacidad y dimensionamiento | desde el inicio del contrato | memoria de capacidad de la sección 3.4.1 del sd-03 |
| 1.3.8 | Especificación y costeo de las obras de infraestructura del cliente | desde el inicio del contrato | El cliente ejecuta; el proponente especifica, costea, coordina y certifica (SP-04) |
| 1.4.1 | Entorno de nube con infraestructura como código, subredes privadas y etiquetado de costos | por definir | sd-03, 3.1 (despliegue híbrido con la carga principal en nube pública) |
| 1.4.2 | Configuración del borde por sitio y certificación de la red segmentada en las 13 tiendas que no la tienen | por definir | El hardware lo adquiere el cliente (SP-04); El cliente adquiere el hardware y ejecuta las obras (EXC-19, SP-04); RT-03.24 del Caso |
| 1.4.3 | Entorno dedicado del ámbito emisor con segregación física y lógica acreditada | por definir | RNF-14 y RNF-36 (Anexo B): separación física acreditada del ámbito emisor |
| 1.4.4 | Ambientes de desarrollo, calidad, preproducción, producción y recuperación ante desastres | por definir | sd-03, 3.4.1 (pruebas en preproducción a 1,5 veces el peak declarado) |
| 1.4.5 | Plataforma de observabilidad unificada con catálogo de alertas | por definir | frontera con el UCP: aquí el aprovisionamiento; las funciones al actor están en la base tecnológica; sd-03, 3.2.1 y 3.3.2 (observabilidad de la base tecnológica) |
| 1.4.6 | Plataforma de integración y entrega continuas con infraestructura como código | por definir | Antes 1.5.10; no está en el UCP |
| 1.4.7 | Licenciamiento de terceros a nombre del cliente | por definir | Agregado desde la guía de la EDT, sección 8 |
| 1.4.8 | Especificación de hardware y dispositivos de terreno para adquisición del cliente | por definir | Formulario T-11; OP-06, OP-07 |
| 1.4.9 | Plano y especificación del recinto técnico del centro de datos y coordinación de su obra civil de separación | por definir | Ronda 0: 1.15.3; RT-06.03; El cliente ejecuta la obra (RT-06.06, RC-04); incluye la especificación del blindaje (RT-06.02) |
| 1.4.11 | Plan de cierre de la brecha del centro de datos frente al informe interno de 2024 | por definir | Ronda 0: 1.15.4; RC-01 (Anexo A): el cliente entrega el informe de 2024 sobre la brecha del centro de datos |
| 1.4.12 | Sistemas de energía y climatización del centro de datos | por definir | RT-06.07, RT-06.08; RT-06.13, RT-06.14 |
| 1.4.14 | Sistemas de seguridad física del centro de datos y espacio de operación del personal | por definir | RT-06.16, RT-06.17; RT-06.20 a RT-06.24; Ronda 0: 1.15.11 |
| 1.4.17 | Solución de respaldo en operación con custodia de medios | por definir | RT-07.09; esquema 3-2-1-1-0; RT-06.26 |
| 1.6.1 | Catálogo de interfaces rediseñadas con contratos y niveles de servicio de integración | por definir | sd-03, 3.2.1 y 3.3.1 (la plataforma de integración reemplaza las catorce conexiones directas) |
| 1.6.2 | Rediseño de las integraciones de la Etapa 1 (precios y existencia, crédito con el sistema de gestión empresarial, cobranza y prevención de pérdidas) | por definir | sd-03, 3.3.1 (plataforma de integración) |
| 1.6.3 | Rediseño de las integraciones de la Etapa 2 (pedidos, marketplace y fidelización) | por definir | sd-03, 3.3.1 (plataforma de integración) |
| 1.6.9 | Canal de intercambio con los proveedores de mercadería | por definir | 940 proveedores; frontera con el caso de uso de órdenes a proveedores del UCP; RNF-53 (Anexo B): estándar de intercambio de órdenes y avisos con proveedores |
| 1.6.10 | Entrega de reportes a las autoridades fiscalizadoras | por definir | sd-03, 3.3.1 (los organismos fiscalizadores reciben los reportes) |
| 1.6.11 | Certificación de las integraciones con evidencia de conciliación | por definir | sd-03, 3.4.5 (conciliación y retorno ensayado entre sistemas) |
| 1.6.12 | Modalidad de contingencia tributaria aprobada y probada con el ERP/DTE | 1 | sd-03, 3.4.5; antes de comprometer la operación sin enlace |
| 1.7.1 | Plan de migración con estrategia de corte y de retorno e inventario de datos históricos | por definir | RT-05.11; RT-05.15 |
| 1.7.3 | Maestro de artículos saneado y validado (268.000 referencias) | por definir | sd-03, 3.2.1 (causa C1: el maestro de artículos) y 3.3.2 |
| 1.7.4 | Corte de inventario en las 24 instalaciones que no cierran | por definir | — |
| 1.7.5 | Migración del histórico comercial (ventas y pedidos) | por definir | EXC-18 (Anexo A): migrar la lista exigida de datos históricos |
| 1.7.6 | Migración del padrón de clientes deduplicado, de los vendedores y de las liquidaciones | por definir | EXC-18 (Anexo A): migrar la lista exigida de datos históricos |
| 1.7.7 | Migración de la cartera viva (620.000 clientes) con sus actas de conciliación | 1 y 2 | Resultado 24 del Anexo D; fuera del UCP (rama de migración) |
| 1.7.9 | Repositorio de consulta de datos históricos no migrados | por definir | Ronda 0: 1.30; EXC-18 (Anexo A): dejar un repositorio de consulta de los datos no migrados |
| 1.7.10 | Plan de retiro de la plataforma de originación y cobranza de 2011 | por definir | Ronda 0: 3.11; sd-03, 3.1 y 3.2.3 (retiro de la plataforma de crédito de 2011 en octubre de 2028) |
| 1.7.11 | Plataforma de originación y cobranza de 2011 fuera de servicio | por definir | Ronda 0: 1.17b; sd-03, 3.1 y 3.2.3 (retiro de la plataforma de crédito de 2011 en octubre de 2028) |
| 1.7.12 | Sistema central de retail de 2009 retirado | por definir | SP-01 y elección del escenario B en el sd-03 |
| 1.7.13 | Sustitución del punto de venta de 2014 tienda por tienda y su retiro | 1 | sd-03, 3.3.1; tras acreditar la operación sin conexión y el retorno |
| 1.7.14 | Actas de compuerta por tramo de la cartera de crédito | 1 y 2 | sd-03, 3.2.3; las cierran la Contraparte Técnica y la filial emisora |
| 1.8.1 | Plan de seguridad, matriz de controles y modelo de amenazas | por definir | — |
| 1.8.3 | Declaración de superficie de exposición y plan de respuesta a incidentes | por definir | — |
| 1.8.5 | Modelo de identidad, matriz de roles y segregación de funciones, incluido el ámbito emisor | por definir | frontera con el UCP: aquí el diseño; la administración al actor está en la base tecnológica; RNF-37 (Anexo B): segregación de funciones entre originación, aprobación, modificación y cobranza |
| 1.8.6 | Cifrado y tokenización de los medios de pago | por definir | RNF-33, RNF-34 |
| 1.8.7 | Protección de datos personales y matriz de cumplimiento normativo | por definir | Ley 21.719; RNF-74 a RNF-76; Art. 27 |
| 1.8.9 | Informe de pruebas de intrusión y plan de remediación | por definir | Anexo D, resultado 21, y RNF-14: informe técnico y prueba de penetración |
| 1.8.10 | Informe de diligencia del proveedor de nube | por definir | Ronda 0: 3.13; fuente de la norma CMF por verificar |
| 1.8.11 | Atestación de la cadena de suministro y revisión de la arquitectura de confianza cero | por definir | RNF-70, RNF-71; agregado desde el catálogo; RNF-73; agregado desde el catálogo |
| 1.9.1 | Plan de pruebas con niveles, tipos, ambientes, datos y calendario | por definir | Formulario T-13 |
| 1.9.2 | Estándares de codificación, revisión por pares y puertas de calidad | por definir | ISO 25010; Ronda 0: 3.2a |
| 1.9.3 | Batería de pruebas funcionales y de requisitos no funcionales | por definir | ISO 29119; Anexo B (requisitos no funcionales con umbral y método de verificación) |
| 1.9.4 | Pruebas de desempeño, resiliencia y recuperación ante desastres | por definir | RNF-22, RNF-23; ensayos a 1,5 veces el peak (RT-09.06); RNF-32 |
| 1.9.6 | Ensayo de la estrategia de degradación del evento anual | por definir | Resultado 25 del Anexo D; lo cita el servicio y se nombra aquí (guía §6) |
| 1.9.7 | Informes de aceptación por el usuario y de verificación de los 28 criterios de aceptación del caso | por definir | Anexo D (28 resultados de negocio) |
| 1.9.8 | Certificación de calidad de la Etapa 1 | 1 | sd-03, 3.2.5 (el equipo del proponente controla la calidad antes de presentar cada entregable) |
| 1.9.9 | Certificación de calidad de la Etapa 2 | 2 | sd-03, 3.2.5 (el equipo del proponente controla la calidad antes de presentar cada entregable) |
| 1.9.11 | Informe de la prueba del corte de enlace provocado de 24 horas con retorno ensayado en el piloto | 1 | sd-03, 3.2.3 y 3.4.5; RT-03.10 |
| 1.9.12 | Informe de evaluación de comercio electrónico y fidelización con las pruebas de la Etapa 1 | 1 | sd-03, 3.3.1; decide si se conservan, remedian o sustituyen antes de la Etapa 2 |
| 1.9.13 | Informe de pruebas de tareas del punto de venta con cajeros nuevos y experimentados | 1 | sd-03, 3.4.6; antes del despliegue; RNF-49 |
| 1.9.14 | Informe de pruebas de comprensión de precios, entrega e información crediticia con clientes y titulares | 1 y 2 | sd-03, 3.4.6 |
| 1.10.1 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | RT-26.02; art. 29; candidatas del equipo de innovación por validar (sd-13) |
| 1.10.2 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | RT-26.02; art. 29; candidatas del equipo de innovación por validar (sd-13) |
| 1.10.3 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | RT-26.02; art. 29; candidatas del equipo de innovación por validar (sd-13) |
| 1.10.4 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | RT-26.02; art. 29; candidatas del equipo de innovación por validar (sd-13) |
| 1.10.5 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | RT-26.02; art. 29; candidatas del equipo de innovación por validar (sd-13) |
| 1.11.1 | Plan de implantación con procedimiento de despliegue gradual y de reversión probado | 1 y 2 | Formulario T-18 |
| 1.11.3 | Configuración y certificación de los sitios: 22 tiendas, 2 centros de distribución, 380 líneas de caja, 640 terminales y el nodo de borde de cada tienda | 1 y 2 | El cliente adquiere y ejecuta (EXC-19, SP-04) |
| 1.11.4 | Plan de convivencia entre la Etapa 1 y la Etapa 2 con una única fuente de verdad | 2 | sd-03, 3.4.5 (continuidad entre etapas por convivencia, conciliación y retorno ensayado) |
| 1.11.5 | Piloto del punto de venta en tres tiendas | 1 | sd-03, 3.2.3 |
| 1.12.1 | Plan de la marcha blanca de la Etapa 1 | 1 | sd-03, 3.1 y 3.2.2 (marchas blancas de los meses 13 a 15 y 19 a 20) |
| 1.12.2 | Informe de resultados y evidencia de cierre de la marcha blanca de la Etapa 1 | 1 | Caso, numeral 17.3 |
| 1.12.4 | Acta de aceptación de la Etapa 1 | 1 | sd-03, 3.2.2 (paso a producción de la Etapa 1 en el mes 16) |
| 1.12.5 | Plan de la marcha blanca de la Etapa 2, en convivencia con la Etapa 1 en producción | 2 | sd-03, 3.1 y 3.2.2 (marchas blancas de los meses 13 a 15 y 19 a 20) |
| 1.12.6 | Informe de resultados de la marcha blanca de la Etapa 2 | 2 | sd-03, 3.1 y 3.2.2 (marchas blancas de los meses 13 a 15 y 19 a 20) |
| 1.12.7 | Acta de aceptación final y garantía de correcto funcionamiento | 2 | sd-03, 3.2.2 (paso a producción de la Etapa 2 en el mes 21) |
| 1.12.9 | Informe del soporte de estabilización posterior a la puesta en marcha | 1 y 2 | — |
| 1.13.1 | Plan de gestión del cambio con diagnóstico por perfil y medición de adopción | por definir | Art. 89 |
| 1.13.2 | Plan de capacitación por rol y materiales editables en español | por definir | Art. 90 |
| 1.13.3 | Registro de capacitación ejecutada y certificación de administradores y equipo técnico, condición de cierre de cada marcha blanca | por definir | sd-03, 3.4.6 (capacitación por rol) y Art. 17.3 (condición de cierre de la marcha blanca) |
| 1.13.4 | Informe de acompañamiento en puesto para el personal de tienda, temporero y externo | por definir | 62 % de rotación anual, 1.900 temporeros y unos 1.100 externos; sd-03, 3.4.6 (rotación anual de 62 % y unos 1.100 repositores externos) |
| 1.13.5 | Plan de comunicación a los clientes de la cartera por tramo | 1 y 2 | sd-03, 3.2.3; condición de cada compuerta de tramo |
| 1.14.1 | Documentación técnica y funcional con inventario de componentes de software | por definir | Art. 91; arquitectura, requerimientos, construcción, pruebas, operación, seguridad, usuario y proyecto; RNF-70 |
| 1.14.3 | Transferencia tecnológica de código fuente, artefactos de construcción, scripts de infraestructura y procedimientos de despliegue | por definir | Art. 77.1 |
| 1.14.4 | Base de conocimiento y manuales de operación | por definir | Art. 77.1; agregado desde la guía |
| 1.14.6 | Plan de Reversibilidad con exportación en formatos abiertos | por definir | Art. 77.2; se entrega dentro de los primeros noventa días y se actualiza cada año |
| 1.14.7 | Acta de cierre, traspaso final y acompañamiento de reversibilidad | por definir | Art. 77.2; Art. 87 |
| 1.14.9 | Informe de lecciones aprendidas del proyecto | por definir | — |
| 1.14.10 | Protocolo de aceptación de entregas y del producto final | por definir | Formulario T-17; base de las actas de aceptación |
| 1.15.1 | Mesa de servicio de tres niveles en operación | operación | Art. 78 |
| 1.15.2 | Informes periódicos de nivel de servicio y de certificaciones | operación | Art. 79.2; Arts. 27, 74.6 |
| 1.15.3 | Pruebas periódicas de recuperación ante desastres | operación | el sd-03 las fija dos veces al año |
| 1.15.4 | Mantención correctiva, preventiva y evolutiva | operación | Agregado desde el sd-03 y las Bases; base del sd-11 |
| 1.15.6 | Infraestructura en operación con su informe de gestión | operación | Agregado desde el sd-03 |
| 1.15.8 | Jornadas anuales de actualización y capacitación de personal nuevo | operación | Art. 90.5 |

## 3. UUCW por servicio

| Servicio | Paquetes | Casos | UUCW |
| :-- | --: | --: | --: |
| Servicio de oferta comercial | 4 | 12 | 65 |
| Servicio de abastecimiento | 3 | 5 | 25 |
| Servicio de existencias | 5 | 19 | 100 |
| Servicio de pedidos | 5 | 15 | 75 |
| Servicio de ventas | 4 | 11 | 55 |
| Servicio de comisiones | 3 | 3 | 15 |
| Servicio de marketplace | 4 | 11 | 55 |
| Servicio de posventa | 3 | 5 | 25 |
| Servicio de clientes Retail | 3 | 4 | 20 |
| Servicio de originación de crédito | 3 | 9 | 45 |
| Servicio de cartera de crédito | 3 | 7 | 35 |
| Servicio de evidencia financiera | 3 | 7 | 35 |
| Servicio de control de cruces | 3 | 6 | 30 |
| Base tecnológica | 5 | 13 | 65 |
| **Total** | **51** | **127** | **645** |

## 4. Paquetes de trabajo de software (uno por caso de uso)

Decisión del usuario del 2026-10-08: en el software, el paquete de trabajo es el entregable de un caso de uso. Cada cuenta de control de la sección 1 contiene los paquetes de sus casos. Son subproyectos y exceden las 80 h por una excepción declarada (FEP02, diapositiva 56). Las horas están en `16_horas_por_paquete.md`.

| Paquete | Caso de uso | Cuenta | RF | Etapa |
| :-- | :-- | :-- | :-- | :-- |
| 1.5.1.1.1 | Cambiar y propagar un precio (CU-OF-01) | 1.5.1.1 | RF-016, RF-018, RF-030 | 1 |
| 1.5.1.1.2 | Entregar la oferta vigente a los canales (CU-OF-02) | 1.5.1.1 | RF-017 | 1 |
| 1.5.1.1.3 | Consultar el precio vigente en línea (CU-OF-03) | 1.5.1.1 | RF-064 | 1 |
| 1.5.1.1.4 | Recuperar el precio publicado en un instante (CU-OF-06) | 1.5.1.1 | RF-021 | 1 |
| 1.5.1.2.1 | Registrar el cambio de etiqueta (CU-OF-04) | 1.5.1.2 | RF-019, RF-020 | 1 |
| 1.5.1.2.2 | Consultar el estado de exhibición de la tienda (CU-OF-05) | 1.5.1.2 | RF-029 | 1 |
| 1.5.1.2.3 | Resolver el precio a cobrar ante diferencia con la etiqueta (CU-OF-07) | 1.5.1.2 | RF-022, RF-023, RF-028 | 1 |
| 1.5.1.2.4 | Revisar los incidentes de discrepancia de precio (CU-OF-08) | 1.5.1.2 | RF-024 | 1 |
| 1.5.1.5.1 | Aplicar las promociones vigentes en la venta (CU-OF-09) | 1.5.1.5 | RF-032 a RF-034 | 1 |
| 1.5.1.5.2 | Administrar las promociones y su vigencia (CU-OF-10) | 1.5.1.5 | — | 1 |
| 1.5.1.6.1 | Mantener el maestro de artículos (CU-OF-11) | 1.5.1.6 | RF-142, RF-143 | 1 |
| 1.5.1.6.2 | Revisar los reportes de calidad del maestro y de publicación (CU-OF-12) | 1.5.1.6 | RF-147, RF-148 | 1 |
| 1.5.2.1.1 | Generar la propuesta diaria de reposición (CU-AB-01) | 1.5.2.1 | RF-144 | 2 |
| 1.5.2.1.2 | Ajustar y confirmar la propuesta de reposición (CU-AB-02) | 1.5.2.1 | RF-145, RF-146 | 2 |
| 1.5.2.2.1 | Colocar y seguir las órdenes a proveedores (CU-AB-03) | 1.5.2.2 | — | 2 |
| 1.5.2.3.1 | Gestionar las transferencias entre tiendas y centros de distribución (CU-AB-04) | 1.5.2.3 | — | 2 |
| 1.5.2.3.2 | Registrar la recepción de mercadería en la tienda (CU-AB-05) | 1.5.2.3 | — | 2 |
| 1.5.3.1.1 | Publicar el disponible a los canales (CU-EX-03) | 1.5.3.1 | RF-127 a RF-129, RF-157 | 1 |
| 1.5.3.1.2 | Parametrizar el colchón de confianza y la vigencia de la reserva (CU-EX-08) | 1.5.3.1 | RF-036, RF-149 a RF-152 | 1 |
| 1.5.3.1.3 | Consultar la traza del cálculo del disponible (CU-EX-09) | 1.5.3.1 | RF-130 | 1 |
| 1.5.3.1.4 | Consultar la disponibilidad para vender en sala (CU-EX-01) | 1.5.3.1 | RF-087, RF-101, RF-161 | 1 |
| 1.5.3.1.5 | Consultar la disponibilidad en línea (CU-EX-02) | 1.5.3.1 | RF-065, RF-066, RF-160 | 1 |
| 1.5.3.2.1 | Reservar una unidad para el canal digital (CU-EX-04) | 1.5.3.2 | RF-035, RF-037, RF-038, RF-041 | 1 |
| 1.5.3.2.2 | Expirar las reservas vencidas (CU-EX-05) | 1.5.3.2 | RF-039, RF-040, RF-042 | 1 |
| 1.5.3.2.3 | Verificar la existencia física antes del cobro (CU-EX-06) | 1.5.3.2 | RF-044 | 1 |
| 1.5.3.2.4 | Resolver el conflicto de existencia comprometida (CU-EX-07) | 1.5.3.2 | RF-098 | 1 |
| 1.5.3.4.1 | Parametrizar el conteo cíclico (CU-EX-10) | 1.5.3.4 | RF-131 a RF-133 | 1 |
| 1.5.3.4.2 | Ejecutar el conteo cíclico (CU-EX-11) | 1.5.3.4 | RF-134 a RF-136 | 1 |
| 1.5.3.4.3 | Consultar la exactitud del inventario y recibir alertas (CU-EX-12) | 1.5.3.4 | RF-137, RF-158, RF-159, RF-162 | 1 |
| 1.5.3.4.4 | Clasificar las diferencias y cerrar el ajuste (CU-EX-13) | 1.5.3.4 | RF-138, RF-139 | 1 |
| 1.5.3.4.5 | Emitir el informe mensual de merma (CU-EX-14) | 1.5.3.4 | RF-140, RF-141 | 1 |
| 1.5.3.4.6 | Gestionar las unidades en el probador (CU-EX-15) | 1.5.3.4 | RF-153 a RF-156 | 1 |
| 1.5.3.7.1 | Suspender la publicación de una categoría (CU-EX-16) | 1.5.3.7 | RF-163, RF-164 | 1 |
| 1.5.3.7.2 | Degradar por cancelaciones (CU-EX-17) | 1.5.3.7 | RF-179, RF-182, RF-183 | 1 |
| 1.5.3.8.1 | Recibir los movimientos del sistema de almacenes (CU-EX-18) | 1.5.3.8 | — | 1 |
| 1.5.3.8.2 | Cargar las existencias de Concepción (CU-EX-19) | 1.5.3.8 | — | 1 |
| 1.5.4.1.1 | Calcular la fecha prometida de entrega (CU-PE-01) | 1.5.4.1 | RF-075, RF-079, RF-080 | 2 |
| 1.5.4.1.2 | Seleccionar el punto de despacho por costo total de servir (CU-PE-02) | 1.5.4.1 | RF-076 a RF-078 | 2 |
| 1.5.4.1.3 | Parametrizar la elegibilidad del stock y el límite por cliente (CU-PE-14) | 1.5.4.1 | RF-053, RF-180 | 2 |
| 1.5.4.2.1 | Aceptar el pedido y preautorizar el medio de pago (CU-PE-03) | 1.5.4.2 | RF-043 | 2 |
| 1.5.4.2.2 | Capturar el cobro al confirmarse la preparación (CU-PE-04) | 1.5.4.2 | RF-045, RF-047, RF-051 | 2 |
| 1.5.4.2.3 | Cancelar el pedido y anular la preautorización (CU-PE-08) | 1.5.4.2 | RF-048, RF-049 | 2 |
| 1.5.4.2.4 | Conciliar las preautorizaciones vencidas sin captura (CU-PE-09) | 1.5.4.2 | RF-050 | 2 |
| 1.5.4.3.1 | Resolver un pedido cuya unidad no existe (CU-PE-05) | 1.5.4.3 | RF-046 | 2 |
| 1.5.4.3.2 | Reasignar el pedido a otro punto de despacho (CU-PE-06) | 1.5.4.3 | RF-056 a RF-058 | 2 |
| 1.5.4.3.3 | Ofrecer al cliente las alternativas de resolución (CU-PE-07) | 1.5.4.3 | RF-059 a RF-061, RF-074 | 2 |
| 1.5.4.4.1 | Consultar el estado único del pedido (CU-PE-10) | 1.5.4.4 | RF-052 | 2 |
| 1.5.4.4.2 | Consultar las compras y las devoluciones (CU-PE-11) | 1.5.4.4 | RF-067, RF-068 | 2 |
| 1.5.4.4.3 | Atender en el mesón la consulta de un pedido (CU-PE-12) | 1.5.4.4 | RF-072, RF-073 | 2 |
| 1.5.4.5.1 | Priorizar los pedidos próximos a vencer su promesa (CU-PE-13) | 1.5.4.5 | RF-062, RF-063, RF-081 | 2 |
| 1.5.4.5.2 | Seguir el pedido con el transportista hasta la entrega (CU-PE-15) | 1.5.4.5 | — | 2 |
| 1.5.5.1.1 | Registrar y cobrar una venta (CU-VE-01) | 1.5.5.1 | RF-001 | 1 |
| 1.5.5.1.2 | Reversar una venta o un pago (CU-VE-02) | 1.5.5.1 | — | 1 |
| 1.5.5.1.3 | Cerrar la caja del turno (CU-VE-03) | 1.5.5.1 | — | 1 |
| 1.5.5.1.4 | Desactivar los medios de pago de mayor fricción (CU-VE-08) | 1.5.5.1 | RF-181 | 1 |
| 1.5.5.2.1 | Operar la tienda sin enlace (CU-VE-04) | 1.5.5.2 | RF-082 a RF-086 | 1 |
| 1.5.5.2.2 | Reconciliar las ventas hechas sin enlace (CU-VE-05) | 1.5.5.2 | RF-088, RF-095 a RF-097 | 1 |
| 1.5.5.2.3 | Revisar el informe de excepciones de la conciliación (CU-VE-06) | 1.5.5.2 | RF-099 | 1 |
| 1.5.5.2.4 | Validar las operaciones cursadas sin enlace (CU-VE-07) | 1.5.5.2 | RF-094 | 1 |
| 1.5.5.6.1 | Registrar las ventas del canal digital (CU-VE-09) | 1.5.5.6 | — | 1 |
| 1.5.5.6.2 | Enrutar los documentos tributarios al ERP/DTE (CU-VE-10) | 1.5.5.6 | RF-100 | 1 |
| 1.5.5.7.1 | Cobrar con la tarjeta de la casa (CU-VE-11) | 1.5.5.7 | — | 1 |
| 1.5.6.1.1 | Calcular la base de comisión por vendedor, tienda y canal (CU-CM-01) | 1.5.6.1 | RF-054, RF-071 | 2 |
| 1.5.6.2.1 | Transmitir la base de comisión al sistema de remuneraciones (CU-CM-02) | 1.5.6.2 | RF-055 | 2 |
| 1.5.6.3.1 | Revisar la atribución de una comisión (CU-CM-03) | 1.5.6.3 | — | 2 |
| 1.5.7.1.1 | Declarar y actualizar la existencia del vendedor (CU-MK-01) | 1.5.7.1 | RF-102 a RF-104 | 2 |
| 1.5.7.1.2 | Publicar la existencia vigente y despublicar la vencida (CU-MK-02) | 1.5.7.1 | RF-109, RF-124 | 2 |
| 1.5.7.2.1 | Consultar los pedidos, las devoluciones y la evaluación (CU-MK-03) | 1.5.7.2 | RF-110 a RF-112 | 2 |
| 1.5.7.2.2 | Calcular los indicadores de nivel de servicio por vendedor (CU-MK-04) | 1.5.7.2 | RF-105 | 2 |
| 1.5.7.2.3 | Dar a conocer las reglas de evaluación al vendedor (CU-MK-05) | 1.5.7.2 | RF-119, RF-120 | 2 |
| 1.5.7.2.4 | Aplicar la consecuencia escalonada de un incumplimiento (CU-MK-06) | 1.5.7.2 | RF-121 a RF-123 | 2 |
| 1.5.7.4.1 | Gestionar una devolución de producto de marketplace (CU-MK-07) | 1.5.7.4 | RF-106 a RF-108 | 2 |
| 1.5.7.4.2 | Informar la base de comisión de marketplace al ERP (CU-MK-10) | 1.5.7.4 | RF-125, RF-126 | 2 |
| 1.5.7.4.3 | Conciliar la liquidación de un vendedor (CU-MK-11) | 1.5.7.4 | — | 2 |
| 1.5.7.5.1 | Identificar al vendedor y las condiciones en la compra (CU-MK-08) | 1.5.7.5 | RF-113 a RF-116 | 2 |
| 1.5.7.5.2 | Impedir que un pedido intermediado use existencia propia (CU-MK-09) | 1.5.7.5 | RF-117, RF-118 | 2 |
| 1.5.8.1.1 | Atender un caso de garantía legal íntegramente en el mesón (CU-PV-01) | 1.5.8.1 | RF-187, RF-188 | 2 |
| 1.5.8.1.2 | Ofrecer y registrar la opción de garantía legal (CU-PV-02) | 1.5.8.1 | RF-192 a RF-194 | 2 |
| 1.5.8.1.3 | Parametrizar el plazo de garantía legal por tipo de producto (CU-PV-03) | 1.5.8.1 | RF-195 | 2 |
| 1.5.8.2.1 | Reingresar una unidad devuelta según su aptitud (CU-PV-04) | 1.5.8.2 | RF-189 a RF-191 | 2 |
| 1.5.8.3.1 | Seguir la resolución al consumidor y la recuperación contra el tercero (CU-PV-05) | 1.5.8.3 | RF-196 a RF-198 | 2 |
| 1.5.9.1.1 | Consolidar los registros duplicados de un cliente (CU-CL-01) | 1.5.9.1 | RF-227 | 2 |
| 1.5.9.2.1 | Mantener los puntos y la fidelización sincronizados (CU-CL-02) | 1.5.9.2 | RF-228, RF-231 | 2 |
| 1.5.9.3.1 | Construir un segmento con atributos comerciales (CU-CL-03) | 1.5.9.3 | RF-229 | 2 |
| 1.5.9.3.2 | Ejecutar una campaña sobre un segmento (CU-CL-04) | 1.5.9.3 | RF-230 | 2 |
| 1.5.10.1.1 | Evaluar la solicitud y abrir una tarjeta en el mostrador (CU-OR-01) | 1.5.10.1 | RF-220 a RF-223, RF-225 | 1 |
| 1.5.10.1.2 | Ofrecer la tarjeta y consultar el resultado (CU-OR-02) | 1.5.10.1 | RF-224 | 1 |
| 1.5.10.1.3 | Controlar los intentos de evaluación (CU-OR-05) | 1.5.10.1 | RF-226 | 1 |
| 1.5.10.1.4 | Solicitar la ampliación de un cupo con enlace (CU-OR-09) | 1.5.10.1 | — | 1 |
| 1.5.10.2.1 | Simular el costo total del crédito (CU-OR-03) | 1.5.10.2 | RF-218 | 1 |
| 1.5.10.2.2 | Mantener la tasa máxima convencional vigente (CU-OR-04) | 1.5.10.2 | RF-219 | 1 |
| 1.5.10.4.1 | Parametrizar los topes y la ventana de enfriamiento (CU-OR-06) | 1.5.10.4 | — | 1 |
| 1.5.10.4.2 | Autorizar compra a cuotas sin enlace contra el cupo preaprobado (CU-OR-07) | 1.5.10.4 | RF-090 a RF-093 | 1 |
| 1.5.10.4.3 | Mantener el cupo preaprobado en la tienda (CU-OR-08) | 1.5.10.4 | RF-089 | 1 |
| 1.5.11.1.1 | Iniciar y registrar una gestión de cobranza (CU-CA-01) | 1.5.11.1 | RF-211 a RF-213 | 1 y 2 |
| 1.5.11.1.2 | Calcular la mora y actualizar las cuentas (CU-CA-05) | 1.5.11.1 | — | 1 y 2 |
| 1.5.11.2.1 | Repactar las condiciones de una deuda (CU-CA-02) | 1.5.11.2 | — | 1 y 2 |
| 1.5.11.2.2 | Registrar el pago de una cuota (CU-CA-04) | 1.5.11.2 | — | 1 y 2 |
| 1.5.11.2.3 | Consultar el estado de cuenta y los documentos (CU-CA-03) | 1.5.11.2 | RF-069, RF-070 | 1 y 2 |
| 1.5.11.5.1 | Revisar la conciliación diaria de la migración (CU-CA-06) | 1.5.11.5 | RF-216 | 1 y 2 |
| 1.5.11.5.2 | Convivir con la plataforma de crédito de 2011 (CU-CA-07) | 1.5.11.5 | — | 1 y 2 |
| 1.5.12.1.1 | Entregar la información precontractual del crédito (CU-EV-01) | 1.5.12.1 | RF-199 a RF-201, RF-203 | 1 |
| 1.5.12.1.2 | Aceptar la información precontractual con firma electrónica (CU-EV-02) | 1.5.12.1 | RF-202, RF-204 a RF-206 | 1 |
| 1.5.12.1.3 | Consultar la información precontractual del crédito (CU-EV-08) | 1.5.12.1 | RF-217 | 1 |
| 1.5.12.2.1 | Registrar el consentimiento de una modificación de condiciones (CU-EV-03) | 1.5.12.2 | RF-207, RF-208 | 1 |
| 1.5.12.2.2 | Enlazar la repactación con su cobranza y su consentimiento (CU-EV-07) | 1.5.12.2 | RF-214, RF-215 | 1 |
| 1.5.12.3.1 | Reconstruir el acto de consentimiento (CU-EV-04) | 1.5.12.3 | RF-209 | 1 |
| 1.5.12.3.2 | Recuperar los antecedentes de una operación desde el archivo (CU-EV-05) | 1.5.12.3 | RF-210 | 1 |
| 1.5.13.1.1 | Mantener el inventario de flujos de cruce autorizados (CU-CC-01) | 1.5.13.1 | RF-168, RF-169 | 1 |
| 1.5.13.1.2 | Revisar los cruces ejecutados y los intentos bloqueados (CU-CC-03) | 1.5.13.1 | RF-165 a RF-167 | 1 |
| 1.5.13.2.1 | Intentar una campaña con atributos de origen financiero (CU-CC-02) | 1.5.13.2 | RF-170, RF-171 | 1 |
| 1.5.13.2.2 | Intentar un proceso crediticio con atributos de origen Retail (CU-CC-04) | 1.5.13.2 | RF-172 | 1 |
| 1.5.13.3.1 | Resolver la correspondencia de identificadores entre ámbitos (CU-CC-05) | 1.5.13.3 | RF-173 a RF-175 | 1 |
| 1.5.13.3.2 | Evaluar el impacto de una iniciativa sobre la frontera de datos (CU-CC-06) | 1.5.13.3 | RF-176 | 1 |
| 1.5.14.1.1 | Ingresar a una terminal compartida con identidad individual (CU-BT-01) | 1.5.14.1 | RF-002 a RF-006 | 1 |
| 1.5.14.1.2 | Administrar identidades, roles y ámbitos (CU-BT-12) | 1.5.14.1 | — | 1 |
| 1.5.14.2.1 | Habilitar y revocar funciones según la capacitación normativa (CU-BT-02) | 1.5.14.2 | RF-007 a RF-009 | 1 |
| 1.5.14.2.2 | Patrocinar el acceso temporal de un repositor externo (CU-BT-03) | 1.5.14.2 | RF-010, RF-011 | 1 |
| 1.5.14.2.3 | Operar como repositor externo con identidad individualizada (CU-BT-04) | 1.5.14.2 | RF-012 | 1 |
| 1.5.14.2.4 | Retirar los accesos al término del vínculo (CU-BT-05) | 1.5.14.2 | RF-013 | 1 |
| 1.5.14.2.5 | Conciliar los accesos contra la nómina activa (CU-BT-06) | 1.5.14.2 | RF-014, RF-015 | 1 |
| 1.5.14.5.1 | Declarar el orden y los criterios de degradación (CU-BT-07) | 1.5.14.5 | RF-177, RF-178 | 1 |
| 1.5.14.5.2 | Parametrizar las ventanas de congelamiento y bloquear intervenciones (CU-BT-08) | 1.5.14.5 | RF-184 a RF-186 | 1 |
| 1.5.14.6.1 | Convivir con el sistema central de 2009 (CU-BT-09) | 1.5.14.6 | — | 1 |
| 1.5.14.6.2 | Administrar la plataforma de integración (CU-BT-10) | 1.5.14.6 | — | 1 |
| 1.5.14.7.1 | Observar la operación y atender alertas (CU-BT-11) | 1.5.14.7 | — | 1 |
| 1.5.14.7.2 | Consultar tableros y exportar informes por ámbito (CU-BT-13) | 1.5.14.7 | — | 1 |
| **Total** | **127** | | | |
