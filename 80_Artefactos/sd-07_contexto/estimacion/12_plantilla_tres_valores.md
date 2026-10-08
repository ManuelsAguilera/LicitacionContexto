# Planilla de tres valores para el segundo método (paso 7, puerta G7)

Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/generar_plantilla_tres_valores.py` a partir de `14_edt_corregida.md`; no editar la estructura a mano. Fecha: 2026-10-08. Plantilla **vacía**: no contiene ninguna hora. Cada estimador la copia a un archivo propio (por ejemplo `12_tres_valores_estimador1.md`), llena sus horas sin consultar `10_esfuerzo.md`, `07_uucw_uucp.md` ni `15_mapa_paquetes_ucp.md`, y la entrega. Se comparan con `python3 05_Gestion/scripts/comparar_metodos.py ARCHIVO1.md ARCHIVO2.md`.

## Instrucciones

1. Estima **horas-hombre de todo el trabajo** del paquete (análisis, diseño, construcción, pruebas y gestión propia), como lo haría un equipo que lo ejecuta de principio a fin. Un número por celda, sin texto.
2. **Optimista** es el valor si todo sale bien (casi sin imprevistos). **Probable** es el más realista. **Pesimista** es el valor si salen mal las cosas que sí pueden salir mal. Debe cumplirse optimista ≤ probable ≤ pesimista.
3. Deja en blanco una fila solo si no puedes estimarla. No inventes: una fila en blanco se informa como pendiente.
4. Estima por separado y sin consultar al otro estimador. La independencia es lo que da valor a la comparación.
5. Los **73 paquetes de desarrollo de software** (primera tabla) se comparan con el UCP. Los **134 restantes** (segunda tabla) no los cubre el UCP: se suman por rama.
6. Si dos paquetes comparten trabajo, pon las horas en uno solo y anótalo debajo. Los conectores de cada servicio y la administración de la base tecnológica ya están en los paquetes de software; no los repitas en las ramas de integración, infraestructura o seguridad.
7. Anota en una línea cada supuesto relevante debajo de las tablas.

## Desarrollo de software (se compara con el UCP)

| Código | Paquete | Servicio | Unidad de tamaño | Optimista (h) | Probable (h) | Pesimista (h) |
| :-- | :-- | :-- | :-- | --: | --: | --: |
| 1.5.1.1 | Cambio y propagación del precio, con su consulta en línea | Servicio de oferta comercial | 5 RF. Etapa 1 | | | |
| 1.5.1.2 | Etiquetas de exhibición y estado de exhibición de la tienda | Servicio de oferta comercial | 3 RF. Etapa 1 | | | |
| 1.5.1.3 | Historial del precio publicado | Servicio de oferta comercial | 1 RF. Etapa 1 | | | |
| 1.5.1.4 | Resolución de discrepancias de precio entre la etiqueta y la caja | Servicio de oferta comercial | 4 RF. Etapa 1 | | | |
| 1.5.1.5 | Promociones y su vigencia | Servicio de oferta comercial | 3 RF. Etapa 1 | | | |
| 1.5.1.6 | Maestro de artículos y reportes de calidad | Servicio de oferta comercial | 4 RF. Etapa 1 | | | |
| 1.5.2.1 | Propuesta diaria de reposición y su ajuste | Servicio de abastecimiento | 3 RF. Etapa 2 | | | |
| 1.5.2.2 | Órdenes de reposición a proveedores | Servicio de abastecimiento | 0 RF. Etapa 2 | | | |
| 1.5.2.3 | Transferencias entre tiendas y centros de distribución | Servicio de abastecimiento | 0 RF. Etapa 2 | | | |
| 1.5.2.4 | Recepción de mercadería en tienda | Servicio de abastecimiento | 0 RF. Etapa 2 | | | |
| 1.5.3.1 | Cálculo del disponible con colchón de confianza y su traza | Servicio de existencias | 10 RF. Etapa 1 | | | |
| 1.5.3.2 | Reservas de existencia para el canal digital | Servicio de existencias | 9 RF. Etapa 1 | | | |
| 1.5.3.3 | Consulta de disponibilidad en sala y en línea | Servicio de existencias | 6 RF. Etapa 1 | | | |
| 1.5.3.4 | Conteo cíclico y medición de la exactitud del inventario | Servicio de existencias | 10 RF. Etapa 1 | | | |
| 1.5.3.5 | Clasificación de diferencias e informe mensual de merma | Servicio de existencias | 4 RF. Etapa 1 | | | |
| 1.5.3.6 | Gestión de las unidades en el probador | Servicio de existencias | 4 RF. Etapa 1 | | | |
| 1.5.3.7 | Suspensión y degradación de la publicación por categoría | Servicio de existencias | 5 RF. Etapa 1 | | | |
| 1.5.3.8 | Integración de existencias con el sistema de almacenes y con las planillas de Concepción | Servicio de existencias | 0 RF. Etapa 1 | | | |
| 1.5.4.1 | Fecha prometida de entrega y punto de despacho por costo total de servir | Servicio de pedidos | 6 RF. Etapa 2 | | | |
| 1.5.4.2 | Preautorización, cobro y anulación del pago del pedido | Servicio de pedidos | 7 RF. Etapa 2 | | | |
| 1.5.4.3 | Resolución de pedidos sin existencia, reasignación y alternativas al cliente | Servicio de pedidos | 8 RF. Etapa 2 | | | |
| 1.5.4.4 | Estado único del pedido y sus consultas | Servicio de pedidos | 5 RF. Etapa 2 | | | |
| 1.5.4.5 | Priorización de pedidos por tiempo restante y cumplimiento de la promesa | Servicio de pedidos | 3 RF. Etapa 2 | | | |
| 1.5.4.6 | Elegibilidad del stock de exhibición y límite de unidades por cliente | Servicio de pedidos | 2 RF. Etapa 2 | | | |
| 1.5.4.7 | Seguimiento del pedido con el transportista hasta la entrega | Servicio de pedidos | 0 RF. Etapa 2 | | | |
| 1.5.5.1 | Registro y cobro de ventas, reversas y cierre de caja | Servicio de ventas | 1 RF. Etapa 1 | | | |
| 1.5.5.2 | Operación de la tienda sin enlace | Servicio de ventas | 5 RF. Etapa 1 | | | |
| 1.5.5.3 | Reconciliación de las ventas hechas sin enlace y su informe de excepciones | Servicio de ventas | 5 RF. Etapa 1 | | | |
| 1.5.5.4 | Validación posterior de las operaciones de crédito cursadas sin enlace | Servicio de ventas | 1 RF. Etapa 1 | | | |
| 1.5.5.5 | Desactivación de los medios de pago de mayor fricción | Servicio de ventas | 1 RF. Etapa 1 | | | |
| 1.5.5.6 | Ventas del canal digital y enrutamiento de los documentos tributarios al sistema de gestión empresarial | Servicio de ventas | 1 RF. Etapa 1 | | | |
| 1.5.5.7 | Cobro con la tarjeta de la casa | Servicio de ventas | 0 RF. Etapa 1 | | | |
| 1.5.6.1 | Cálculo de la base de comisión | Servicio de comisiones | 2 RF. Etapa 2 | | | |
| 1.5.6.2 | Entrega de la base de comisión al sistema de remuneraciones | Servicio de comisiones | 1 RF. Etapa 2 | | | |
| 1.5.6.3 | Revisión de la atribución de comisiones | Servicio de comisiones | 0 RF. Etapa 2 | | | |
| 1.5.7.1 | Existencia declarada por el vendedor y su publicación | Servicio de marketplace | 5 RF. Etapa 2 | | | |
| 1.5.7.2 | Consulta del vendedor sobre pedidos, devoluciones y evaluación | Servicio de marketplace | 3 RF. Etapa 2 | | | |
| 1.5.7.3 | Evaluación de vendedores y consecuencias escalonadas | Servicio de marketplace | 6 RF. Etapa 2 | | | |
| 1.5.7.4 | Devolución de productos de marketplace | Servicio de marketplace | 3 RF. Etapa 2 | | | |
| 1.5.7.5 | Identificación del vendedor y de las condiciones en la compra | Servicio de marketplace | 4 RF. Etapa 2 | | | |
| 1.5.7.6 | Separación de la existencia propia en pedidos intermediados | Servicio de marketplace | 2 RF. Etapa 2 | | | |
| 1.5.7.7 | Base de comisión y liquidación de marketplace | Servicio de marketplace | 2 RF. Etapa 2 | | | |
| 1.5.8.1 | Atención de garantía legal en el mesón, con sus plazos | Servicio de posventa | 6 RF. Etapa 2 | | | |
| 1.5.8.2 | Devolución y aptitud de la unidad devuelta | Servicio de posventa | 3 RF. Etapa 2 | | | |
| 1.5.8.3 | Resolución al consumidor y recuperación contra el tercero responsable | Servicio de posventa | 3 RF. Etapa 2 | | | |
| 1.5.9.1 | Consolidación de los registros de clientes | Servicio de clientes Retail | 1 RF. Etapa 2 | | | |
| 1.5.9.2 | Puntos y sincronización con el sistema de fidelización | Servicio de clientes Retail | 2 RF. Etapa 2 | | | |
| 1.5.9.3 | Segmentos y campañas con atributos comerciales | Servicio de clientes Retail | 2 RF. Etapa 2 | | | |
| 1.5.10.1 | Evaluación crediticia y apertura de tarjeta en el mostrador | Servicio de originación de crédito | 6 RF. Etapa 1 | | | |
| 1.5.10.2 | Simulación del costo total del crédito con la tasa máxima vigente | Servicio de originación de crédito | 2 RF. Etapa 1 | | | |
| 1.5.10.3 | Control de los intentos de evaluación | Servicio de originación de crédito | 1 RF. Etapa 1 | | | |
| 1.5.10.4 | Autorización de compra a cuotas sin enlace y sus topes | Servicio de originación de crédito | 5 RF. Etapa 1 | | | |
| 1.5.10.5 | Ampliación de cupo con enlace | Servicio de originación de crédito | 0 RF. Etapa 1 | | | |
| 1.5.11.1 | Gestión de cobranza dentro de los límites normativos | Servicio de cartera de crédito | 3 RF. Etapa 1 y 2 | | | |
| 1.5.11.2 | Repactación y registro de pagos | Servicio de cartera de crédito | 0 RF. Etapa 1 y 2 | | | |
| 1.5.11.3 | Cálculo de la mora y actualización de cuentas | Servicio de cartera de crédito | 0 RF. Etapa 1 y 2 | | | |
| 1.5.11.4 | Estado de cuenta y documentos para el cliente | Servicio de cartera de crédito | 2 RF. Etapa 1 y 2 | | | |
| 1.5.11.5 | Conciliación diaria y convivencia con la plataforma de crédito de 2011 | Servicio de cartera de crédito | 1 RF. Etapa 1 y 2 | | | |
| 1.5.12.1 | Información precontractual entregada, aceptada y consultable | Servicio de evidencia financiera | 9 RF. Etapa 1 | | | |
| 1.5.12.2 | Consentimiento de modificaciones de condiciones y su enlace con la cobranza | Servicio de evidencia financiera | 4 RF. Etapa 1 | | | |
| 1.5.12.3 | Reconstrucción y recuperación de la evidencia del consentimiento | Servicio de evidencia financiera | 2 RF. Etapa 1 | | | |
| 1.5.13.1 | Inventario de flujos de cruce autorizados y registro de los cruces | Servicio de control de cruces | 5 RF. Etapa 1 | | | |
| 1.5.13.2 | Rechazo de cruces no autorizados entre los ámbitos | Servicio de control de cruces | 3 RF. Etapa 1 | | | |
| 1.5.13.3 | Tabla de correspondencia de identificadores | Servicio de control de cruces | 3 RF. Etapa 1 | | | |
| 1.5.13.4 | Evaluación de impacto de las iniciativas sobre la frontera de datos | Servicio de control de cruces | 1 RF. Etapa 1 | | | |
| 1.5.14.1 | Identidad individual y sesión en terminales compartidas | Base tecnológica | 5 RF. Etapa 1 | | | |
| 1.5.14.2 | Habilitación por capacitación y acceso temporal de externos | Base tecnológica | 6 RF. Etapa 1 | | | |
| 1.5.14.3 | Revocación de accesos y conciliación contra la nómina | Base tecnológica | 3 RF. Etapa 1 | | | |
| 1.5.14.4 | Administración de identidades, roles y ámbitos | Base tecnológica | 0 RF. Etapa 1 | | | |
| 1.5.14.5 | Orden de degradación y ventanas de congelamiento | Base tecnológica | 5 RF. Etapa 1 | | | |
| 1.5.14.6 | Plataforma de integración y convivencia con el sistema central de 2009 | Base tecnológica | 0 RF. Etapa 1 | | | |
| 1.5.14.7 | Observabilidad y alertas de la operación | Base tecnológica | 0 RF. Etapa 1 | | | |
| 1.5.14.8 | Capacidad analítica y tableros por ámbito | Base tecnológica | 0 RF. Etapa 1 | | | |

## Lo que el UCP no cubre (se suma por rama, no se compara)

| Código | Paquete | Etapa | Unidad de tamaño | Optimista (h) | Probable (h) | Pesimista (h) |
| :-- | :-- | :-- | :-- | --: | --: | --: |
| 1.1.1 | Plan de dirección integrado (ámbito, cronograma, costos, calidad, riesgos, comunicaciones, interesados y adquisiciones) | desde el inicio del contrato | 56 meses de contrato; comités mensuales, quincenales y semanales (sd-01, 1.5) | | | |
| 1.1.2 | EDT y diccionario de paquetes con entregable, criterio de aceptación y responsable | desde el inicio del contrato | 56 meses de contrato; comités mensuales, quincenales y semanales (sd-01, 1.5) | | | |
| 1.1.3 | Control integrado de cambios | desde el inicio del contrato | 56 meses de contrato; comités mensuales, quincenales y semanales (sd-01, 1.5) | | | |
| 1.1.4 | Registro de riesgos y de lecciones aprendidas | desde el inicio del contrato | 56 meses de contrato; comités mensuales, quincenales y semanales (sd-01, 1.5) | | | |
| 1.1.5 | Registro de supuestos y de vacíos y consultas | desde el inicio del contrato | 56 meses de contrato; comités mensuales, quincenales y semanales (sd-01, 1.5) | | | |
| 1.1.6 | Calendario de ventanas de congelamiento y de eventos anuales con declaración de impacto por evento | desde el inicio del contrato | 56 meses de contrato; comités mensuales, quincenales y semanales (sd-01, 1.5) | | | |
| 1.1.7 | Actas de los comités del proyecto | desde el inicio del contrato | 56 meses de contrato; comités mensuales, quincenales y semanales (sd-01, 1.5) | | | |
| 1.1.8 | Informe mensual de avance | desde el inicio del contrato | 56 meses de contrato; comités mensuales, quincenales y semanales (sd-01, 1.5) | | | |
| 1.1.9 | Reporte mensual de consumo de nube | desde el inicio del contrato | 56 meses de contrato; comités mensuales, quincenales y semanales (sd-01, 1.5) | | | |
| 1.1.10 | Actas de aceptación por entrega y habilitación de pagos | desde el inicio del contrato | 56 meses de contrato; comités mensuales, quincenales y semanales (sd-01, 1.5) | | | |
| 1.1.11 | Seguimiento de garantías, seguros y certificados laborales | desde el inicio del contrato | 56 meses de contrato; comités mensuales, quincenales y semanales (sd-01, 1.5) | | | |
| 1.1.12 | Acta de constitución del proyecto | desde el inicio del contrato | 56 meses de contrato; comités mensuales, quincenales y semanales (sd-01, 1.5) | | | |
| 1.1.13 | Línea base de costos y presupuesto | desde el inicio del contrato | 56 meses de contrato; comités mensuales, quincenales y semanales (sd-01, 1.5) | | | |
| 1.2.1 | Mapa de las 14 interfaces punto a punto existentes | desde el inicio del contrato | 14 interfaces entre 9 plataformas de 6 proveedores | | | |
| 1.2.2 | Inventario de las 9 plataformas, 6 proveedores y dependencias | desde el inicio del contrato | 14 interfaces entre 9 plataformas de 6 proveedores | | | |
| 1.2.3 | Levantamiento de procesos, reglas de negocio y volumetría declarada | desde el inicio del contrato | 14 interfaces entre 9 plataformas de 6 proveedores | | | |
| 1.2.4 | Mantención del catálogo de requerimientos trazado al origen | desde el inicio del contrato | 14 interfaces entre 9 plataformas de 6 proveedores | | | |
| 1.2.5 | Matriz de trazabilidad de origen, requerimiento, componente, paquete, prueba y criterio | desde el inicio del contrato | 14 interfaces entre 9 plataformas de 6 proveedores | | | |
| 1.2.6 | Línea base de alcance por etapa, con exclusiones y supuestos | desde el inicio del contrato | 14 interfaces entre 9 plataformas de 6 proveedores | | | |
| 1.2.7 | Estudio de decisión con costeo sobre etiquetas electrónicas de precio | desde el inicio del contrato | 14 interfaces entre 9 plataformas de 6 proveedores | | | |
| 1.2.8 | Estudio de decisión con costeo sobre el sistema de almacenes de Concepción | desde el inicio del contrato | 14 interfaces entre 9 plataformas de 6 proveedores | | | |
| 1.2.9 | Estudio de decisión con costeo sobre el destino de las plataformas | desde el inicio del contrato | 14 interfaces entre 9 plataformas de 6 proveedores | | | |
| 1.3.1 | Documento de arquitectura con cinco vistas | desde el inicio del contrato | 13 servicios y la base tecnológica; arquitectura híbrida | | | |
| 1.3.2 | Catálogo de decisiones de arquitectura | desde el inicio del contrato | 13 servicios y la base tecnológica; arquitectura híbrida | | | |
| 1.3.3 | Arquitectura física con emplazamiento por componente justificado | desde el inicio del contrato | 13 servicios y la base tecnológica; arquitectura híbrida | | | |
| 1.3.4 | Modelo de datos con dominios segregados Retail y Emisor, frontera documentada y políticas de retención | desde el inicio del contrato | 13 servicios y la base tecnológica; arquitectura híbrida | | | |
| 1.3.5 | Contratos de integración versionados y su gobierno | desde el inicio del contrato | 13 servicios y la base tecnológica; arquitectura híbrida | | | |
| 1.3.6 | Especificación del modo desconectado de 24 horas y de la sincronización tras la reconexión | desde el inicio del contrato | 13 servicios y la base tecnológica; arquitectura híbrida | | | |
| 1.3.7 | Modelo de capacidad y dimensionamiento | desde el inicio del contrato | 13 servicios y la base tecnológica; arquitectura híbrida | | | |
| 1.3.8 | Especificación y costeo de las obras de infraestructura del cliente | desde el inicio del contrato | 13 servicios y la base tecnológica; arquitectura híbrida | | | |
| 1.4.1 | Entorno de nube con infraestructura como código, subredes privadas y etiquetado de costos | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.2 | Configuración del entorno on-premise de borde por sitio | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.3 | Entorno dedicado del ámbito emisor con segregación física y lógica acreditada | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.4 | Ambientes de desarrollo, calidad, preproducción, producción y recuperación ante desastres | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.5 | Plataforma de observabilidad unificada con catálogo de alertas | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.6 | Plataforma de integración y entrega continuas con infraestructura como código | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.7 | Licenciamiento de terceros a nombre del cliente | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.8 | Especificación de hardware y dispositivos de terreno para adquisición del cliente | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.9 | Plano de distribución interna y especificación del recinto técnico del centro de datos | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.10 | Especificación y coordinación de la obra civil de separación del centro de datos | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.11 | Plan de cierre de la brecha del centro de datos frente al informe interno de 2024 | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.12 | Sistema de energía ininterrumpida y generación autónoma del centro de datos | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.13 | Sistema de climatización de precisión con monitoreo ambiental del centro de datos | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.14 | Sistema de detección temprana y extinción automática de incendios del centro de datos | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.15 | Control de acceso físico biométrico y videovigilancia del centro de datos | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.16 | Espacio de operación del personal habilitado, separado de la sala de equipos | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.17 | Solución de respaldo en operación | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.18 | Servicio de custodia de medios de respaldo del centro de datos | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.4.19 | Configuración y certificación de la red segmentada en las 13 tiendas que no la tienen | por definir | Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m² | | | |
| 1.6.1 | Catálogo de interfaces rediseñadas con contratos y niveles de servicio de integración | por definir | 14 interfaces existentes; 940 proveedores | | | |
| 1.6.2 | Rediseño de las integraciones de precios y existencia hacia los canales | por definir | 14 interfaces existentes; 940 proveedores | | | |
| 1.6.3 | Rediseño de la integración de pedidos | por definir | 14 interfaces existentes; 940 proveedores | | | |
| 1.6.4 | Rediseño de la integración del crédito con el sistema de gestión empresarial | por definir | 14 interfaces existentes; 940 proveedores | | | |
| 1.6.5 | Rediseño de la integración con el marketplace | por definir | 14 interfaces existentes; 940 proveedores | | | |
| 1.6.6 | Rediseño de la integración de cobranza | por definir | 14 interfaces existentes; 940 proveedores | | | |
| 1.6.7 | Rediseño de la integración con el sistema de fidelización | por definir | 14 interfaces existentes; 940 proveedores | | | |
| 1.6.8 | Rediseño de la integración de prevención de pérdidas | por definir | 14 interfaces existentes; 940 proveedores | | | |
| 1.6.9 | Canal de intercambio con los proveedores de mercadería | por definir | 14 interfaces existentes; 940 proveedores | | | |
| 1.6.10 | Entrega de reportes a las autoridades fiscalizadoras | por definir | 14 interfaces existentes; 940 proveedores | | | |
| 1.6.11 | Certificación de las integraciones con evidencia de conciliación | por definir | 14 interfaces existentes; 940 proveedores | | | |
| 1.7.1 | Plan de migración con estrategia de corte y de retorno | por definir | 620.000 clientes de la cartera por tramos; 268.000 referencias; 24 instalaciones | | | |
| 1.7.2 | Inventario de datos históricos a migrar | por definir | 620.000 clientes de la cartera por tramos; 268.000 referencias; 24 instalaciones | | | |
| 1.7.3 | Maestro de artículos saneado y validado (268.000 referencias) | por definir | 620.000 clientes de la cartera por tramos; 268.000 referencias; 24 instalaciones | | | |
| 1.7.4 | Corte de inventario en las 24 instalaciones que no cierran | por definir | 620.000 clientes de la cartera por tramos; 268.000 referencias; 24 instalaciones | | | |
| 1.7.5 | Migración del histórico comercial (ventas y pedidos) | por definir | 620.000 clientes de la cartera por tramos; 268.000 referencias; 24 instalaciones | | | |
| 1.7.6 | Migración del padrón de clientes deduplicado, de los vendedores y de las liquidaciones | por definir | 620.000 clientes de la cartera por tramos; 268.000 referencias; 24 instalaciones | | | |
| 1.7.7 | Migración de la cartera viva (620.000 clientes) con convivencia, conciliación diaria y retorno probado | 1 y 2 | 620.000 clientes de la cartera por tramos; 268.000 referencias; 24 instalaciones | | | |
| 1.7.8 | Actas de conciliación de la corrida paralela y de cuadratura previa y posterior a la migración | por definir | 620.000 clientes de la cartera por tramos; 268.000 referencias; 24 instalaciones | | | |
| 1.7.9 | Repositorio de consulta de datos históricos no migrados | por definir | 620.000 clientes de la cartera por tramos; 268.000 referencias; 24 instalaciones | | | |
| 1.7.10 | Plan de retiro de la plataforma de originación y cobranza de 2011 | por definir | 620.000 clientes de la cartera por tramos; 268.000 referencias; 24 instalaciones | | | |
| 1.7.11 | Plataforma de originación y cobranza de 2011 fuera de servicio | por definir | 620.000 clientes de la cartera por tramos; 268.000 referencias; 24 instalaciones | | | |
| 1.7.12 | Sistema central de retail de 2009 retirado | por definir | 620.000 clientes de la cartera por tramos; 268.000 referencias; 24 instalaciones | | | |
| 1.8.1 | Plan de seguridad y matriz de controles | por definir | RNF-33 a RNF-38 y RNF-70 a RNF-76 del Anexo B | | | |
| 1.8.2 | Modelo de amenazas | por definir | RNF-33 a RNF-38 y RNF-70 a RNF-76 del Anexo B | | | |
| 1.8.3 | Declaración de superficie de exposición | por definir | RNF-33 a RNF-38 y RNF-70 a RNF-76 del Anexo B | | | |
| 1.8.4 | Plan de respuesta a incidentes de seguridad | por definir | RNF-33 a RNF-38 y RNF-70 a RNF-76 del Anexo B | | | |
| 1.8.5 | Modelo de identidad, matriz de roles y segregación de funciones, incluido el ámbito emisor | por definir | RNF-33 a RNF-38 y RNF-70 a RNF-76 del Anexo B | | | |
| 1.8.6 | Cifrado y tokenización de los medios de pago | por definir | RNF-33 a RNF-38 y RNF-70 a RNF-76 del Anexo B | | | |
| 1.8.7 | Protección de datos personales y registro de actividades de tratamiento | por definir | RNF-33 a RNF-38 y RNF-70 a RNF-76 del Anexo B | | | |
| 1.8.8 | Matriz de cumplimiento normativo con control y evidencia | por definir | RNF-33 a RNF-38 y RNF-70 a RNF-76 del Anexo B | | | |
| 1.8.9 | Informe de pruebas de intrusión y plan de remediación | por definir | RNF-33 a RNF-38 y RNF-70 a RNF-76 del Anexo B | | | |
| 1.8.10 | Informe de diligencia del proveedor de nube | por definir | RNF-33 a RNF-38 y RNF-70 a RNF-76 del Anexo B | | | |
| 1.8.11 | Atestación de la cadena de suministro de software | por definir | RNF-33 a RNF-38 y RNF-70 a RNF-76 del Anexo B | | | |
| 1.8.12 | Revisión de la arquitectura de confianza cero | por definir | RNF-33 a RNF-38 y RNF-70 a RNF-76 del Anexo B | | | |
| 1.9.1 | Plan de pruebas con niveles, tipos, ambientes, datos y calendario | por definir | RNF-22 a RNF-28 y RNF-32 del Anexo B; 28 criterios de aceptación | | | |
| 1.9.2 | Puertas de calidad con análisis estático, cobertura y umbrales | por definir | RNF-22 a RNF-28 y RNF-32 del Anexo B; 28 criterios de aceptación | | | |
| 1.9.3 | Batería de pruebas funcionales y de requisitos no funcionales | por definir | RNF-22 a RNF-28 y RNF-32 del Anexo B; 28 criterios de aceptación | | | |
| 1.9.4 | Batería de pruebas de carga, estrés y resiliencia | por definir | RNF-22 a RNF-28 y RNF-32 del Anexo B; 28 criterios de aceptación | | | |
| 1.9.5 | Batería de pruebas de recuperación ante desastres | por definir | RNF-22 a RNF-28 y RNF-32 del Anexo B; 28 criterios de aceptación | | | |
| 1.9.6 | Ensayo de la estrategia de degradación del evento anual | por definir | RNF-22 a RNF-28 y RNF-32 del Anexo B; 28 criterios de aceptación | | | |
| 1.9.7 | Informes de aceptación por el usuario y de verificación de los 28 criterios de aceptación del caso | por definir | RNF-22 a RNF-28 y RNF-32 del Anexo B; 28 criterios de aceptación | | | |
| 1.9.8 | Certificación de calidad de la Etapa 1 | 1 | RNF-22 a RNF-28 y RNF-32 del Anexo B; 28 criterios de aceptación | | | |
| 1.9.9 | Certificación de calidad de la Etapa 2 | 2 | RNF-22 a RNF-28 y RNF-32 del Anexo B; 28 criterios de aceptación | | | |
| 1.9.10 | Estándares de codificación y lista de revisión por pares | por definir | RNF-22 a RNF-28 y RNF-32 del Anexo B; 28 criterios de aceptación | | | |
| 1.10.1 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | 5 innovaciones, una por tipo (art. 29) | | | |
| 1.10.2 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | 5 innovaciones, una por tipo (art. 29) | | | |
| 1.10.3 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | 5 innovaciones, una por tipo (art. 29) | | | |
| 1.10.4 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | 5 innovaciones, una por tipo (art. 29) | | | |
| 1.10.5 | Un paquete por innovación, con tipo, indicador, línea base y meta por definir | por definir | 5 innovaciones, una por tipo (art. 29) | | | |
| 1.11.1 | Plan de implantación y puesta en marcha con criterios de éxito medibles | 1 y 2 | Piloto de 3 tiendas; 22 tiendas y 2 centros; 380 líneas de caja; 640 terminales | | | |
| 1.11.2 | Procedimiento de despliegue gradual y de reversión probado | 1 y 2 | Piloto de 3 tiendas; 22 tiendas y 2 centros; 380 líneas de caja; 640 terminales | | | |
| 1.11.3 | Configuración y certificación de los sitios: 22 tiendas, 2 centros de distribución, 380 líneas de caja, 640 terminales y el nodo de borde de cada tienda | 1 y 2 | Piloto de 3 tiendas; 22 tiendas y 2 centros; 380 líneas de caja; 640 terminales | | | |
| 1.11.4 | Plan de convivencia entre la Etapa 1 y la Etapa 2 con una única fuente de verdad | 2 | Piloto de 3 tiendas; 22 tiendas y 2 centros; 380 líneas de caja; 640 terminales | | | |
| 1.12.1 | Plan de la marcha blanca de la Etapa 1 | 1 | Dos marchas blancas, una por etapa | | | |
| 1.12.2 | Informe de resultados de la marcha blanca de la Etapa 1, con medición diaria y conciliación | 1 | Dos marchas blancas, una por etapa | | | |
| 1.12.3 | Evidencia de cierre de la Etapa 1 contra las condiciones del Caso | 1 | Dos marchas blancas, una por etapa | | | |
| 1.12.4 | Acta de aceptación de la Etapa 1 | 1 | Dos marchas blancas, una por etapa | | | |
| 1.12.5 | Plan de la marcha blanca de la Etapa 2, en convivencia con la Etapa 1 en producción | 2 | Dos marchas blancas, una por etapa | | | |
| 1.12.6 | Informe de resultados de la marcha blanca de la Etapa 2 | 2 | Dos marchas blancas, una por etapa | | | |
| 1.12.7 | Acta de aceptación final de la implementación | 2 | Dos marchas blancas, una por etapa | | | |
| 1.12.8 | Garantía de correcto funcionamiento | 2 | Dos marchas blancas, una por etapa | | | |
| 1.12.9 | Informe del soporte de estabilización posterior a la puesta en marcha | 1 y 2 | Dos marchas blancas, una por etapa | | | |
| 1.13.1 | Plan de gestión del cambio con diagnóstico por perfil y medición de adopción | por definir | Unos 1.100 repositores externos; 62 % de rotación; 1.900 incorporaciones de temporada | | | |
| 1.13.2 | Plan de capacitación por rol y materiales editables en español | por definir | Unos 1.100 repositores externos; 62 % de rotación; 1.900 incorporaciones de temporada | | | |
| 1.13.3 | Registro de capacitación ejecutada y certificación de administradores y equipo técnico, condición de cierre de cada marcha blanca | por definir | Unos 1.100 repositores externos; 62 % de rotación; 1.900 incorporaciones de temporada | | | |
| 1.13.4 | Programa de acompañamiento en puesto para el personal de tienda, temporero y externo | por definir | Unos 1.100 repositores externos; 62 % de rotación; 1.900 incorporaciones de temporada | | | |
| 1.14.1 | Documentación técnica y funcional por categoría | por definir | Documentación del art. 77.1; Plan de Reversibilidad dentro de los primeros 90 días, actualizado cada año | | | |
| 1.14.2 | Inventario de componentes de software por artefacto desplegado | por definir | Documentación del art. 77.1; Plan de Reversibilidad dentro de los primeros 90 días, actualizado cada año | | | |
| 1.14.3 | Transferencia tecnológica de código fuente, artefactos de construcción, scripts de infraestructura y procedimientos de despliegue | por definir | Documentación del art. 77.1; Plan de Reversibilidad dentro de los primeros 90 días, actualizado cada año | | | |
| 1.14.4 | Base de conocimiento de incidentes, problemas, soluciones y decisiones de diseño | por definir | Documentación del art. 77.1; Plan de Reversibilidad dentro de los primeros 90 días, actualizado cada año | | | |
| 1.14.5 | Manuales de operación, libros de operación y guías de resolución de fallas | por definir | Documentación del art. 77.1; Plan de Reversibilidad dentro de los primeros 90 días, actualizado cada año | | | |
| 1.14.6 | Plan de Reversibilidad con exportación en formatos abiertos | por definir | Documentación del art. 77.1; Plan de Reversibilidad dentro de los primeros 90 días, actualizado cada año | | | |
| 1.14.7 | Acompañamiento de reversibilidad posterior al cierre | por definir | Documentación del art. 77.1; Plan de Reversibilidad dentro de los primeros 90 días, actualizado cada año | | | |
| 1.14.8 | Acta de cierre y traspaso final a operaciones | por definir | Documentación del art. 77.1; Plan de Reversibilidad dentro de los primeros 90 días, actualizado cada año | | | |
| 1.14.9 | Informe de lecciones aprendidas del proyecto | por definir | Documentación del art. 77.1; Plan de Reversibilidad dentro de los primeros 90 días, actualizado cada año | | | |
| 1.14.10 | Protocolo de aceptación de entregas y del producto final | por definir | Documentación del art. 77.1; Plan de Reversibilidad dentro de los primeros 90 días, actualizado cada año | | | |
| 1.15.1 | Mesa de servicio de tres niveles | operación | 36 meses de operación | | | |
| 1.15.2 | Informe mensual de nivel de servicio | operación | 36 meses de operación | | | |
| 1.15.3 | Pruebas periódicas de recuperación ante desastres | operación | 36 meses de operación | | | |
| 1.15.4 | Mantención correctiva | operación | 36 meses de operación | | | |
| 1.15.5 | Mantención preventiva y evolutiva con mejora continua del nivel de servicio | operación | 36 meses de operación | | | |
| 1.15.6 | Gestión de la infraestructura en operación | operación | 36 meses de operación | | | |
| 1.15.7 | Informe anual de certificaciones y soporte a auditorías e inspecciones | operación | 36 meses de operación | | | |
| 1.15.8 | Jornadas anuales de actualización y capacitación de personal nuevo | operación | 36 meses de operación | | | |

## Supuestos del estimador

(Anota aquí una línea por cada supuesto.)
