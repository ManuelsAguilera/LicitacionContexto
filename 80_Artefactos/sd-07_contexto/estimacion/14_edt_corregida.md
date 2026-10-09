# EDT corregida (paso 8b del plan de estimación)

Documento de contexto, no es entregable ni fuente de las Bases. Fecha: 2026-10-08. Estado: **propuesta** de este trabajo, pendiente del visto bueno del equipo. Parte de `[ELISEO]-entregables_edt.md`, que no se modifica, y aplica los hallazgos de `13_evaluacion_edt.md` y las tres decisiones del usuario del 2026-10-08: copia corregida aparte, sin el paquete de portales y app (Opción A) y un nodo por servicio en el desarrollo de software. Reglas: `guia_edt.md`. Controles: `python3 05_Gestion/scripts/verificar_edt.py 80_Artefactos/sd-07_contexto/estimacion/14_edt_corregida.md`. Los códigos son provisorios y se re-secuencian al congelar la EDT para el Formulario T-14. No contiene horas, costos, fechas ni dotación: eso viene después.

**Nivel de los elementos (2026-10-08).** El último nivel de esta EDT son **cuentas de control** (PMBOK 6), no paquetes de trabajo. Por su tamaño ninguna cumple la regla 8/80 de la clase (`20_evaluacion_8_80.md`): se aplica la planificación gradual. Cada cuenta se descompone en paquetes de trabajo de 8 a 80 h y de un mes como máximo cuando entra en la ola cercana (`21_ola_1_paquetes_trabajo.md`); mientras tanto funciona como paquete de planificación. El 2026-10-08 se fusionaron 54 elementos en las cuentas de control de la última sección (207 → 153).

## Cómo leer los atributos

Cada paquete termina con un bloque `{...}` que no forma parte del nombre.

- `casos:` los casos de uso del modelo (`03_casos_de_uso_*.md`) que el paquete entrega. Todos los casos aparecen en un solo paquete. De ahí salen los requerimientos (RF) y las horas del UCP.
- `ucp: no` el paquete no lo cubre el UCP; se estima con tres valores (`12_plantilla_tres_valores.md`).
- `nivel:` `cuenta de control` en todos los elementos de este archivo; los paquetes de trabajo están en los archivos de cada ola.
- `etapa:` Etapa 1, Etapa 2, `1 y 2`, `operación`, `desde el inicio del contrato` o `por definir`. La de los paquetes de software es la del servicio (sd-03); el resto queda `por definir` hasta el cronograma, salvo los que el sd-03 fija.
- `origen:` fuente contractual o nota de frontera. Los códigos externos (artículos, requisitos y formularios) viven aquí y no en el nombre.

### 1.1 Dirección, gobierno y control del proyecto — 11 cuentas de control

- 1.1.1 Plan de dirección integrado (ámbito, cronograma, costos, calidad, riesgos, comunicaciones, interesados y adquisiciones) {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato}
- 1.1.2 EDT y diccionario de paquetes con entregable, criterio de aceptación y responsable {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato; origen: Formulario T-14}
- 1.1.3 Registro de solicitudes de cambio y su resolución {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato; origen: Art. 72}
- 1.1.4 Registros de riesgos, lecciones aprendidas, supuestos y consultas {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato}
- 1.1.6 Calendario de ventanas de congelamiento y de eventos anuales con declaración de impacto por evento {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato}
- 1.1.7 Actas de los comités e informe mensual de avance {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato; origen: Art. 71; RT-19.06}
- 1.1.9 Reporte mensual de consumo de nube {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato; origen: Art. 16.3; RT-03.06}
- 1.1.10 Actas de aceptación por entrega y habilitación de pagos {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato; origen: Art. 18; E-25}
- 1.1.11 Registro de garantías, seguros y certificados laborales vigentes {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato; origen: Art. 75.3}
- 1.1.12 Acta de constitución del proyecto {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato}
- 1.1.13 Línea base de costos y presupuesto {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato; origen: Ronda 0: 2.9; los valores viven solo en la oferta económica}

### 1.2 Levantamiento y línea base de alcance — 7 cuentas de control

- 1.2.1 Mapa de las 14 interfaces e inventario de las 9 plataformas, 6 proveedores y dependencias {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato}
- 1.2.3 Levantamiento de procesos, reglas de negocio y volumetría declarada {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato}
- 1.2.4 Catálogo de requerimientos y matriz de trazabilidad {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato; origen: Anexo B del sd-03}
- 1.2.6 Línea base de alcance por etapa, con exclusiones y supuestos {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato}
- 1.2.7 Estudio de decisión con costeo sobre etiquetas electrónicas de precio {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato; origen: OP-01 a OP-05}
- 1.2.8 Estudio de decisión con costeo sobre el sistema de almacenes de Concepción {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato; origen: OP-08, OP-09}
- 1.2.9 Estudio de decisión con costeo sobre el destino de las plataformas {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato}

### 1.3 Arquitectura y diseño — 7 cuentas de control

- 1.3.1 Documento de arquitectura con cinco vistas y catálogo de decisiones {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato; origen: ISO 42010}
- 1.3.3 Arquitectura física con emplazamiento por componente justificado {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato; origen: Art. 16.2; zonas a nombrar conforme al sd-04}
- 1.3.4 Modelo de datos con dominios segregados Retail y Emisor, frontera documentada y políticas de retención {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato; origen: RT-05.10}
- 1.3.5 Contratos de integración versionados y su gobierno {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato}
- 1.3.6 Especificación del modo desconectado de 24 horas y de la sincronización tras la reconexión {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato; origen: RT-03.10 de las Bases Transversales; el código RT-03.13 significa cosas distintas en el Caso y en las Transversales}
- 1.3.7 Modelo de capacidad y dimensionamiento {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato; origen: memoria de capacidad de la sección 3.4.1 del sd-03}
- 1.3.8 Especificación y costeo de las obras de infraestructura del cliente {ucp: no; nivel: cuenta de control; etapa: desde el inicio del contrato; origen: El cliente ejecuta; el proponente especifica, costea, coordina y certifica (SP-04)}

### 1.4 Infraestructura híbrida y plataforma base — 13 cuentas de control

- 1.4.1 Entorno de nube con infraestructura como código, subredes privadas y etiquetado de costos {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.4.2 Configuración del borde por sitio y certificación de la red segmentada en las 13 tiendas que no la tienen {ucp: no; nivel: cuenta de control; etapa: por definir; origen: El hardware lo adquiere el cliente (SP-04); El cliente adquiere el hardware y ejecuta las obras (EXC-19, SP-04); RT-03.24 del Caso}
- 1.4.3 Entorno dedicado del ámbito emisor con segregación física y lógica acreditada {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.4.4 Ambientes de desarrollo, calidad, preproducción, producción y recuperación ante desastres {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.4.5 Plataforma de observabilidad unificada con catálogo de alertas {ucp: no; nivel: cuenta de control; etapa: por definir; origen: frontera con el UCP: aquí el aprovisionamiento; las funciones al actor están en la base tecnológica}
- 1.4.6 Plataforma de integración y entrega continuas con infraestructura como código {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Antes 1.5.10; no está en el UCP}
- 1.4.7 Licenciamiento de terceros a nombre del cliente {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Agregado desde la guía de la EDT, sección 8}
- 1.4.8 Especificación de hardware y dispositivos de terreno para adquisición del cliente {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Formulario T-11; OP-06, OP-07}
- 1.4.9 Plano y especificación del recinto técnico del centro de datos y coordinación de su obra civil de separación {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Ronda 0: 1.15.3; RT-06.03; El cliente ejecuta la obra (RT-06.06, RC-04); incluye la especificación del blindaje (RT-06.02)}
- 1.4.11 Plan de cierre de la brecha del centro de datos frente al informe interno de 2024 {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Ronda 0: 1.15.4}
- 1.4.12 Sistemas de energía y climatización del centro de datos {ucp: no; nivel: cuenta de control; etapa: por definir; origen: RT-06.07, RT-06.08; RT-06.13, RT-06.14}
- 1.4.14 Sistemas de seguridad física del centro de datos y espacio de operación del personal {ucp: no; nivel: cuenta de control; etapa: por definir; origen: RT-06.16, RT-06.17; RT-06.20 a RT-06.24; Ronda 0: 1.15.11}
- 1.4.17 Solución de respaldo en operación con custodia de medios {ucp: no; nivel: cuenta de control; etapa: por definir; origen: RT-07.09; esquema 3-2-1-1-0; RT-06.26}

### 1.5 Desarrollo de software — 51 cuentas de control

#### 1.5.1 Servicio de oferta comercial — 4 cuentas de control

- 1.5.1.1 Precio: cambio, propagación, consulta e historial {casos: CU-OF-01, CU-OF-02, CU-OF-03, CU-OF-06; nivel: cuenta de control; etapa: 1}
- 1.5.1.2 Etiquetas de exhibición y discrepancias de precio {casos: CU-OF-04, CU-OF-05, CU-OF-07, CU-OF-08; nivel: cuenta de control; etapa: 1}
- 1.5.1.5 Promociones y su vigencia {casos: CU-OF-09, CU-OF-10; nivel: cuenta de control; etapa: 1}
- 1.5.1.6 Maestro de artículos y reportes de calidad {casos: CU-OF-11, CU-OF-12; nivel: cuenta de control; etapa: 1}

#### 1.5.2 Servicio de abastecimiento — 3 cuentas de control

- 1.5.2.1 Propuesta diaria de reposición y su ajuste {casos: CU-AB-01, CU-AB-02; nivel: cuenta de control; etapa: 2}
- 1.5.2.2 Órdenes de reposición a proveedores {casos: CU-AB-03; nivel: cuenta de control; etapa: 2}
- 1.5.2.3 Transferencias y recepción de mercadería {casos: CU-AB-04, CU-AB-05; nivel: cuenta de control; etapa: 2}

#### 1.5.3 Servicio de existencias — 5 cuentas de control

- 1.5.3.1 Disponible: cálculo, traza y consulta {casos: CU-EX-03, CU-EX-08, CU-EX-09, CU-EX-01, CU-EX-02; nivel: cuenta de control; etapa: 1}
- 1.5.3.2 Reservas de existencia para el canal digital {casos: CU-EX-04, CU-EX-05, CU-EX-06, CU-EX-07; nivel: cuenta de control; etapa: 1}
- 1.5.3.4 Conteo, exactitud del inventario, merma y probador {casos: CU-EX-10, CU-EX-11, CU-EX-12, CU-EX-13, CU-EX-14, CU-EX-15; nivel: cuenta de control; etapa: 1}
- 1.5.3.7 Suspensión y degradación de la publicación por categoría {casos: CU-EX-16, CU-EX-17; nivel: cuenta de control; etapa: 1}
- 1.5.3.8 Integración de existencias con el sistema de almacenes y con las planillas de Concepción {casos: CU-EX-18, CU-EX-19; nivel: cuenta de control; etapa: 1}

#### 1.5.4 Servicio de pedidos — 5 cuentas de control

- 1.5.4.1 Promesa de entrega, punto de despacho y elegibilidad del stock {casos: CU-PE-01, CU-PE-02, CU-PE-14; nivel: cuenta de control; etapa: 2}
- 1.5.4.2 Preautorización, cobro y anulación del pago del pedido {casos: CU-PE-03, CU-PE-04, CU-PE-08, CU-PE-09; nivel: cuenta de control; etapa: 2}
- 1.5.4.3 Resolución de pedidos sin existencia, reasignación y alternativas al cliente {casos: CU-PE-05, CU-PE-06, CU-PE-07; nivel: cuenta de control; etapa: 2}
- 1.5.4.4 Estado único del pedido y sus consultas {casos: CU-PE-10, CU-PE-11, CU-PE-12; nivel: cuenta de control; etapa: 2}
- 1.5.4.5 Seguimiento y cumplimiento de la promesa de entrega {casos: CU-PE-13, CU-PE-15; nivel: cuenta de control; etapa: 2}

#### 1.5.5 Servicio de ventas — 4 cuentas de control

- 1.5.5.1 Registro y cobro de ventas, reversas, cierre de caja y medios de pago {casos: CU-VE-01, CU-VE-02, CU-VE-03, CU-VE-08; nivel: cuenta de control; etapa: 1}
- 1.5.5.2 Operación sin enlace, reconciliación y validación posterior {casos: CU-VE-04, CU-VE-05, CU-VE-06, CU-VE-07; nivel: cuenta de control; etapa: 1}
- 1.5.5.6 Ventas del canal digital y enrutamiento de los documentos tributarios al sistema de gestión empresarial {casos: CU-VE-09, CU-VE-10; nivel: cuenta de control; etapa: 1}
- 1.5.5.7 Cobro con la tarjeta de la casa {casos: CU-VE-11; nivel: cuenta de control; etapa: 1}

#### 1.5.6 Servicio de comisiones — 3 cuentas de control

- 1.5.6.1 Cálculo de la base de comisión {casos: CU-CM-01; nivel: cuenta de control; etapa: 2}
- 1.5.6.2 Entrega de la base de comisión al sistema de remuneraciones {casos: CU-CM-02; nivel: cuenta de control; etapa: 2}
- 1.5.6.3 Revisión de la atribución de comisiones {casos: CU-CM-03; nivel: cuenta de control; etapa: 2}

#### 1.5.7 Servicio de marketplace — 4 cuentas de control

- 1.5.7.1 Existencia declarada por el vendedor y su publicación {casos: CU-MK-01, CU-MK-02; nivel: cuenta de control; etapa: 2}
- 1.5.7.2 Evaluación de vendedores y su consulta {casos: CU-MK-03, CU-MK-04, CU-MK-05, CU-MK-06; nivel: cuenta de control; etapa: 2}
- 1.5.7.4 Devoluciones, base de comisión y liquidación de marketplace {casos: CU-MK-07, CU-MK-10, CU-MK-11; nivel: cuenta de control; etapa: 2}
- 1.5.7.5 Identificación del vendedor y separación de la existencia propia {casos: CU-MK-08, CU-MK-09; nivel: cuenta de control; etapa: 2}

#### 1.5.8 Servicio de posventa — 3 cuentas de control

- 1.5.8.1 Atención de garantía legal en el mesón, con sus plazos {casos: CU-PV-01, CU-PV-02, CU-PV-03; nivel: cuenta de control; etapa: 2}
- 1.5.8.2 Devolución y aptitud de la unidad devuelta {casos: CU-PV-04; nivel: cuenta de control; etapa: 2}
- 1.5.8.3 Resolución al consumidor y recuperación contra el tercero responsable {casos: CU-PV-05; nivel: cuenta de control; etapa: 2}

#### 1.5.9 Servicio de clientes Retail — 3 cuentas de control

- 1.5.9.1 Consolidación de los registros de clientes {casos: CU-CL-01; nivel: cuenta de control; etapa: 2}
- 1.5.9.2 Puntos y sincronización con el sistema de fidelización {casos: CU-CL-02; nivel: cuenta de control; etapa: 2}
- 1.5.9.3 Segmentos y campañas con atributos comerciales {casos: CU-CL-03, CU-CL-04; nivel: cuenta de control; etapa: 2}

#### 1.5.10 Servicio de originación de crédito — 3 cuentas de control

- 1.5.10.1 Evaluación crediticia, apertura de tarjeta y ampliación de cupo {casos: CU-OR-01, CU-OR-02, CU-OR-05, CU-OR-09; nivel: cuenta de control; etapa: 1}
- 1.5.10.2 Simulación del costo total del crédito con la tasa máxima vigente {casos: CU-OR-03, CU-OR-04; nivel: cuenta de control; etapa: 1}
- 1.5.10.4 Autorización de compra a cuotas sin enlace y sus topes {casos: CU-OR-06, CU-OR-07, CU-OR-08; nivel: cuenta de control; etapa: 1}

#### 1.5.11 Servicio de cartera de crédito — 3 cuentas de control

- 1.5.11.1 Mora y gestión de cobranza {casos: CU-CA-01, CU-CA-05; nivel: cuenta de control; etapa: 1 y 2}
- 1.5.11.2 Repactación, pagos y estado de cuenta {casos: CU-CA-02, CU-CA-04, CU-CA-03; nivel: cuenta de control; etapa: 1 y 2}
- 1.5.11.5 Conciliación diaria y convivencia con la plataforma de crédito de 2011 {casos: CU-CA-06, CU-CA-07; nivel: cuenta de control; etapa: 1 y 2}

#### 1.5.12 Servicio de evidencia financiera — 3 cuentas de control

- 1.5.12.1 Información precontractual entregada, aceptada y consultable {casos: CU-EV-01, CU-EV-02, CU-EV-08; nivel: cuenta de control; etapa: 1}
- 1.5.12.2 Consentimiento de modificaciones de condiciones y su enlace con la cobranza {casos: CU-EV-03, CU-EV-07; nivel: cuenta de control; etapa: 1}
- 1.5.12.3 Reconstrucción y recuperación de la evidencia del consentimiento {casos: CU-EV-04, CU-EV-05; nivel: cuenta de control; etapa: 1}

#### 1.5.13 Servicio de control de cruces — 3 cuentas de control

- 1.5.13.1 Inventario de flujos de cruce autorizados y registro de los cruces {casos: CU-CC-01, CU-CC-03; nivel: cuenta de control; etapa: 1}
- 1.5.13.2 Rechazo de cruces no autorizados entre los ámbitos {casos: CU-CC-02, CU-CC-04; nivel: cuenta de control; etapa: 1}
- 1.5.13.3 Correspondencia de identificadores y evaluación de impacto sobre la frontera {casos: CU-CC-05, CU-CC-06; nivel: cuenta de control; etapa: 1}

#### 1.5.14 Base tecnológica — 5 cuentas de control

- 1.5.14.1 Identidad individual y administración de identidades, roles y ámbitos {casos: CU-BT-01, CU-BT-12; nivel: cuenta de control; etapa: 1}
- 1.5.14.2 Habilitación, revocación y conciliación de accesos {casos: CU-BT-02, CU-BT-03, CU-BT-04, CU-BT-05, CU-BT-06; nivel: cuenta de control; etapa: 1}
- 1.5.14.5 Orden de degradación y ventanas de congelamiento {casos: CU-BT-07, CU-BT-08; nivel: cuenta de control; etapa: 1}
- 1.5.14.6 Plataforma de integración y convivencia con el sistema central de 2009 {casos: CU-BT-09, CU-BT-10; nivel: cuenta de control; etapa: 1}
- 1.5.14.7 Observabilidad y capacidad analítica {casos: CU-BT-11, CU-BT-13; nivel: cuenta de control; etapa: 1}

### 1.6 Integraciones (rediseño de las interfaces existentes) — 6 cuentas de control

- 1.6.1 Catálogo de interfaces rediseñadas con contratos y niveles de servicio de integración {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.6.2 Rediseño de las integraciones de la Etapa 1 (precios y existencia, crédito con el sistema de gestión empresarial, cobranza y prevención de pérdidas) {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.6.3 Rediseño de las integraciones de la Etapa 2 (pedidos, marketplace y fidelización) {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.6.9 Canal de intercambio con los proveedores de mercadería {ucp: no; nivel: cuenta de control; etapa: por definir; origen: 940 proveedores; frontera con el caso de uso de órdenes a proveedores del UCP}
- 1.6.10 Entrega de reportes a las autoridades fiscalizadoras {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.6.11 Certificación de las integraciones con evidencia de conciliación {ucp: no; nivel: cuenta de control; etapa: por definir}

### 1.7 Migración y saneamiento de datos — 10 cuentas de control

- 1.7.1 Plan de migración con estrategia de corte y de retorno e inventario de datos históricos {ucp: no; nivel: cuenta de control; etapa: por definir; origen: RT-05.11; RT-05.15}
- 1.7.3 Maestro de artículos saneado y validado (268.000 referencias) {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.7.4 Corte de inventario en las 24 instalaciones que no cierran {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.7.5 Migración del histórico comercial (ventas y pedidos) {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.7.6 Migración del padrón de clientes deduplicado, de los vendedores y de las liquidaciones {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.7.7 Migración de la cartera viva (620.000 clientes) con sus actas de conciliación {ucp: no; nivel: cuenta de control; etapa: 1 y 2; origen: Resultado 24 del Anexo D; fuera del UCP (rama de migración)}
- 1.7.9 Repositorio de consulta de datos históricos no migrados {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Ronda 0: 1.30}
- 1.7.10 Plan de retiro de la plataforma de originación y cobranza de 2011 {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Ronda 0: 3.11}
- 1.7.11 Plataforma de originación y cobranza de 2011 fuera de servicio {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Ronda 0: 1.17b}
- 1.7.12 Sistema central de retail de 2009 retirado {ucp: no; nivel: cuenta de control; etapa: por definir; origen: SP-01 y elección del escenario B en el sd-03}

### 1.8 Seguridad, identidad y cumplimiento — 8 cuentas de control

- 1.8.1 Plan de seguridad, matriz de controles y modelo de amenazas {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.8.3 Declaración de superficie de exposición y plan de respuesta a incidentes {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.8.5 Modelo de identidad, matriz de roles y segregación de funciones, incluido el ámbito emisor {ucp: no; nivel: cuenta de control; etapa: por definir; origen: frontera con el UCP: aquí el diseño; la administración al actor está en la base tecnológica}
- 1.8.6 Cifrado y tokenización de los medios de pago {ucp: no; nivel: cuenta de control; etapa: por definir; origen: RNF-33, RNF-34}
- 1.8.7 Protección de datos personales y matriz de cumplimiento normativo {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Ley 21.719; RNF-74 a RNF-76; Art. 27}
- 1.8.9 Informe de pruebas de intrusión y plan de remediación {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.8.10 Informe de diligencia del proveedor de nube {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Ronda 0: 3.13; fuente de la norma CMF por verificar}
- 1.8.11 Atestación de la cadena de suministro y revisión de la arquitectura de confianza cero {ucp: no; nivel: cuenta de control; etapa: por definir; origen: RNF-70, RNF-71; agregado desde el catálogo; RNF-73; agregado desde el catálogo}

### 1.9 Calidad, pruebas y certificación — 8 cuentas de control

- 1.9.1 Plan de pruebas con niveles, tipos, ambientes, datos y calendario {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Formulario T-13}
- 1.9.2 Estándares de codificación, revisión por pares y puertas de calidad {ucp: no; nivel: cuenta de control; etapa: por definir; origen: ISO 25010; Ronda 0: 3.2a}
- 1.9.3 Batería de pruebas funcionales y de requisitos no funcionales {ucp: no; nivel: cuenta de control; etapa: por definir; origen: ISO 29119}
- 1.9.4 Pruebas de desempeño, resiliencia y recuperación ante desastres {ucp: no; nivel: cuenta de control; etapa: por definir; origen: RNF-22, RNF-23; ensayos a 1,5 veces el peak (RT-09.06); RNF-32}
- 1.9.6 Ensayo de la estrategia de degradación del evento anual {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Resultado 25 del Anexo D; lo cita el servicio y se nombra aquí (guía §6)}
- 1.9.7 Informes de aceptación por el usuario y de verificación de los 28 criterios de aceptación del caso {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.9.8 Certificación de calidad de la Etapa 1 {ucp: no; nivel: cuenta de control; etapa: 1}
- 1.9.9 Certificación de calidad de la Etapa 2 {ucp: no; nivel: cuenta de control; etapa: 2}

### 1.10 Innovaciones — 5 cuentas de control

- 1.10.1 … 1.10.5 Un paquete por innovación, con tipo, indicador, línea base y meta por definir {ucp: no; nivel: cuenta de control; etapa: por definir; origen: RT-26.02; art. 29; candidatas del equipo de innovación por validar (sd-13)}

### 1.11 Implantación y despliegue — 3 cuentas de control

- 1.11.1 Plan de implantación con procedimiento de despliegue gradual y de reversión probado {ucp: no; nivel: cuenta de control; etapa: 1 y 2; origen: Formulario T-18}
- 1.11.3 Configuración y certificación de los sitios: 22 tiendas, 2 centros de distribución, 380 líneas de caja, 640 terminales y el nodo de borde de cada tienda {ucp: no; nivel: cuenta de control; etapa: 1 y 2; origen: El cliente adquiere y ejecuta (EXC-19, SP-04)}
- 1.11.4 Plan de convivencia entre la Etapa 1 y la Etapa 2 con una única fuente de verdad {ucp: no; nivel: cuenta de control; etapa: 2}

### 1.12 Resultados de las marchas blancas y aceptación por etapa — 7 cuentas de control

- 1.12.1 Plan de la marcha blanca de la Etapa 1 {ucp: no; nivel: cuenta de control; etapa: 1}
- 1.12.2 Informe de resultados y evidencia de cierre de la marcha blanca de la Etapa 1 {ucp: no; nivel: cuenta de control; etapa: 1; origen: Caso, numeral 17.3}
- 1.12.4 Acta de aceptación de la Etapa 1 {ucp: no; nivel: cuenta de control; etapa: 1}
- 1.12.5 Plan de la marcha blanca de la Etapa 2, en convivencia con la Etapa 1 en producción {ucp: no; nivel: cuenta de control; etapa: 2}
- 1.12.6 Informe de resultados de la marcha blanca de la Etapa 2 {ucp: no; nivel: cuenta de control; etapa: 2}
- 1.12.7 Acta de aceptación final y garantía de correcto funcionamiento {ucp: no; nivel: cuenta de control; etapa: 2}
- 1.12.9 Informe del soporte de estabilización posterior a la puesta en marcha {ucp: no; nivel: cuenta de control; etapa: 1 y 2}

### 1.13 Gestión del cambio y capacitación — 4 cuentas de control

- 1.13.1 Plan de gestión del cambio con diagnóstico por perfil y medición de adopción {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Art. 89}
- 1.13.2 Plan de capacitación por rol y materiales editables en español {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Art. 90}
- 1.13.3 Registro de capacitación ejecutada y certificación de administradores y equipo técnico, condición de cierre de cada marcha blanca {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.13.4 Informe de acompañamiento en puesto para el personal de tienda, temporero y externo {ucp: no; nivel: cuenta de control; etapa: por definir; origen: 62 % de rotación anual, 1.900 temporeros y unos 1.100 externos}

### 1.14 Documentación, transferencia y reversibilidad — 7 cuentas de control

- 1.14.1 Documentación técnica y funcional con inventario de componentes de software {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Art. 91; arquitectura, requerimientos, construcción, pruebas, operación, seguridad, usuario y proyecto; RNF-70}
- 1.14.3 Transferencia tecnológica de código fuente, artefactos de construcción, scripts de infraestructura y procedimientos de despliegue {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Art. 77.1}
- 1.14.4 Base de conocimiento y manuales de operación {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Art. 77.1; agregado desde la guía}
- 1.14.6 Plan de Reversibilidad con exportación en formatos abiertos {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Art. 77.2; se entrega dentro de los primeros noventa días y se actualiza cada año}
- 1.14.7 Acta de cierre, traspaso final y acompañamiento de reversibilidad {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Art. 77.2; Art. 87}
- 1.14.9 Informe de lecciones aprendidas del proyecto {ucp: no; nivel: cuenta de control; etapa: por definir}
- 1.14.10 Protocolo de aceptación de entregas y del producto final {ucp: no; nivel: cuenta de control; etapa: por definir; origen: Formulario T-17; base de las actas de aceptación}

### 1.15 Operación y soporte — 6 cuentas de control

- 1.15.1 Mesa de servicio de tres niveles en operación {ucp: no; nivel: cuenta de control; etapa: operación; origen: Art. 78}
- 1.15.2 Informes periódicos de nivel de servicio y de certificaciones {ucp: no; nivel: cuenta de control; etapa: operación; origen: Art. 79.2; Arts. 27, 74.6}
- 1.15.3 Pruebas periódicas de recuperación ante desastres {ucp: no; nivel: cuenta de control; etapa: operación; origen: el sd-03 las fija dos veces al año}
- 1.15.4 Mantención correctiva, preventiva y evolutiva {ucp: no; nivel: cuenta de control; etapa: operación; origen: Agregado desde el sd-03 y las Bases; base del sd-11}
- 1.15.6 Infraestructura en operación con su informe de gestión {ucp: no; nivel: cuenta de control; etapa: operación; origen: Agregado desde el sd-03}
- 1.15.8 Jornadas anuales de actualización y capacitación de personal nuevo {ucp: no; nivel: cuenta de control; etapa: operación; origen: Art. 90.5}

---

## Cambios frente a la EDT original

| Rama | Paquetes (antes → ahora) | Qué cambió |
| :-- | :-- | :-- |
| 1.1 | 9 → 13 | Se separaron entregables que compartían nombre (control de cambios, registro de riesgos, informe mensual, reporte de consumo, actas y garantías). Los números de las Bases salieron del nombre (hallazgos 10 y 11) |
| 1.2 | 7 → 9 | El estudio de decisión se dividió en tres (etiquetas electrónicas, sistema de almacenes de Concepción y destino de plataformas). Se quitó «hito H1» del título (hallazgo 3) |
| 1.3 | 7 → 8 | La autonomía sin enlace es de 24 horas (hallazgo 4). El documento de arquitectura y el catálogo de decisiones se separaron. Se quitaron hito y mes del título |
| 1.4 | 16 → 19 | Se agregaron el licenciamiento a nombre del cliente (hallazgo 15) y la plataforma de entrega continua, que venía como software (hallazgo 8). Los paquetes de obra se renombraron como especificación, coordinación, configuración y certificación (hallazgo 12). Se mantuvieron los del centro de datos que el sd-03 asigna al proponente (SP-04) |
| 1.5 | 10 → 73 | Un nodo por servicio y por la base tecnológica, con 3 a 8 paquetes cada uno, que agrupan los 127 casos del modelo. Se quitaron los portales y la app (hallazgo 1), los nombres antiguos (hallazgo 18) y la plataforma de entrega continua. La base tecnológica tiene nodo propio (hallazgo 14) |
| 1.6 | 7 → 11 | Los conectores de la plataforma de almacenes, el comercio electrónico y las remuneraciones, y el de transportistas, salieron: cada uno está en su servicio y el UCP ya lo cuenta (hallazgo 7). Quedan el rediseño de las interfaces existentes, el canal con proveedores y los reportes a las autoridades |
| 1.7 | 11 → 12 | El retiro del sistema central de 2009 ya no es condicional (hallazgo 6). El histórico se dividió en dos |
| 1.8 | 7 → 12 | Se dividieron los planes y modelos, la protección de datos y el cifrado. Se agregaron la atestación de la cadena de suministro y la revisión de confianza cero (desde el catálogo). Se quitó la referencia a la norma CMF del nombre (hallazgo 17) |
| 1.9 | 6 → 10 | Se separaron las baterías por tipo; la prueba de seguridad queda solo en 1.8; se agregó el ensayo de degradación del evento anual (resultado 25). Se quitaron hitos |
| 1.10 | 5 → 5 | Cinco paquetes «por definir», uno por tipo, sin las candidatas de otro equipo (hallazgo 19) |
| 1.11 | 5 → 4 | Se quitó el paquete de degradación (queda en la base tecnológica y en 1.9) y los meses del plan de convivencia |
| 1.12 | 5 → 9 | De fases a entregables: plan e informe de cada marcha blanca, evidencia de cierre y acta de aceptación por etapa (hallazgo 5) |
| 1.13 | 4 → 4 | Se quitaron cifras de los nombres |
| 1.14 | 5 → 10 | Se agregaron la base de conocimiento y los manuales (hallazgo 16), el inventario de componentes y el acompañamiento de reversibilidad. Se quitaron «90 días» y los códigos del nombre |
| 1.15 | 6 → 8 | Se agregaron la mantención correctiva y la gestión de la infraestructura, que las Bases y el sd-03 incluyen en la operación. Se quitaron los meses del título |

Total: 110 → 207 paquetes, y 153 cuentas de control tras las fusiones (última sección). La rama 1.5 tiene 73 porque la guía pide 5 a 10 por servicio; los servicios con pocos casos (comisiones, evidencia financiera, posventa y clientes Retail) quedaron en 3.

## Fronteras con el UCP (para quien estime con tres valores)

El UCP ya cubre, dentro de los paquetes de 1.5, el comportamiento de cada servicio frente a sus actores, incluidos sus conectores propios, y la parte funcional de la base tecnológica. No deben estimarse otra vez:

- Los conectores con el sistema de almacenes, el comercio electrónico, las remuneraciones, los transportistas y la fidelización.
- La administración de la plataforma de integración, la observabilidad y la identidad **como función para el actor** (1.5.14).
- La convivencia con la plataforma de 2011 (cartera) y con el sistema de 2009 (base tecnológica).

Lo que sí es de las ramas con tres valores: el aprovisionamiento de las plataformas (1.4), el diseño de la identidad y de la seguridad (1.8), el rediseño de las interfaces existentes (1.6) y la migración de los datos (1.7).

## Preguntas abiertas para el equipo, con sugerencia

1. ¿Qué cinco innovaciones se confirman? Sugiero dejar «por definir» y cerrarlas con el sd-13.
2. ¿Qué norma de la CMF respalda el paquete de diligencia del proveedor de nube? Sugiero quitar el paquete si no hay fuente en las Bases o el Caso.
3. ¿Dónde se declara que la app existente de AS-04 cubre la exigencia de la aplicación móvil del Caso (RT-17.01)? Sugiero una frase en el sd-03 (alcance) o el sd-04, que remita a la decisión D-08.
4. ¿Quién completa el diccionario por paquete (criterio, responsable en rol y dependencias)? Sugiero dejarlo para el T-14, con «por definir» en lo que dependa del sd-12.
5. ¿Qué paquetes de 1.4 son del proponente entre los del centro de datos? Sugiero mantenerlos todos, porque el sd-03 (SP-04) dice que el proponente provee el centro de datos con su conectividad, su seguridad y sus canalizaciones, y la obra civil de separación es del cliente.

## Pendientes heredados de la EDT original

1. Re-secuenciar códigos al congelar la EDT.
2. Hitos de pago del Formulario E-25: «por definir».
3. Nombres de tecnología y zonas hasta que exista el sd-04.
4. Diccionario por paquete: criterio con umbral, responsable, dependencias, mes, hito y trazas.
5. Ponderaciones del T-21 en blanco en las Bases; no se hardcodean.
6. La fase de oferta (T-12, video, sitio web, prototipo) queda fuera de la EDT.

## Fusiones en cuentas de control (2026-10-08)

Aprobadas por el usuario (opción A). Cada fila deja el código menor del grupo; los demás desaparecen y sus casos de uso, origen y ventana pasan a la cuenta que queda. Criterio: mismo servicio o mismo responsable, misma etapa y el resultado se sigue pudiendo estimar y aceptar como una unidad. También se renombraron cinco elementos que sonaban a actividad: 1.1.3, 1.1.11, 1.13.4, 1.15.1 y 1.15.6.

| Queda | Absorbe | Nombre de la cuenta de control |
| :-- | :-- | :-- |
| 1.5.1.1 | 1.5.1.3 | Precio: cambio, propagación, consulta e historial |
| 1.5.1.2 | 1.5.1.4 | Etiquetas de exhibición y discrepancias de precio |
| 1.5.2.3 | 1.5.2.4 | Transferencias y recepción de mercadería |
| 1.5.3.1 | 1.5.3.3 | Disponible: cálculo, traza y consulta |
| 1.5.3.4 | 1.5.3.5, 1.5.3.6 | Conteo, exactitud del inventario, merma y probador |
| 1.5.4.1 | 1.5.4.6 | Promesa de entrega, punto de despacho y elegibilidad del stock |
| 1.5.4.5 | 1.5.4.7 | Seguimiento y cumplimiento de la promesa de entrega |
| 1.5.5.1 | 1.5.5.5 | Registro y cobro de ventas, reversas, cierre de caja y medios de pago |
| 1.5.5.2 | 1.5.5.3, 1.5.5.4 | Operación sin enlace, reconciliación y validación posterior |
| 1.5.7.2 | 1.5.7.3 | Evaluación de vendedores y su consulta |
| 1.5.7.4 | 1.5.7.7 | Devoluciones, base de comisión y liquidación de marketplace |
| 1.5.7.5 | 1.5.7.6 | Identificación del vendedor y separación de la existencia propia |
| 1.5.10.1 | 1.5.10.3, 1.5.10.5 | Evaluación crediticia, apertura de tarjeta y ampliación de cupo |
| 1.5.11.1 | 1.5.11.3 | Mora y gestión de cobranza |
| 1.5.11.2 | 1.5.11.4 | Repactación, pagos y estado de cuenta |
| 1.5.13.3 | 1.5.13.4 | Correspondencia de identificadores y evaluación de impacto sobre la frontera |
| 1.5.14.1 | 1.5.14.4 | Identidad individual y administración de identidades, roles y ámbitos |
| 1.5.14.2 | 1.5.14.3 | Habilitación, revocación y conciliación de accesos |
| 1.5.14.7 | 1.5.14.8 | Observabilidad y capacidad analítica |
| 1.1.4 | 1.1.5 | Registros de riesgos, lecciones aprendidas, supuestos y consultas |
| 1.1.7 | 1.1.8 | Actas de los comités e informe mensual de avance |
| 1.2.1 | 1.2.2 | Mapa de las 14 interfaces e inventario de las 9 plataformas, 6 proveedores y dependencias |
| 1.2.4 | 1.2.5 | Catálogo de requerimientos y matriz de trazabilidad |
| 1.3.1 | 1.3.2 | Documento de arquitectura con cinco vistas y catálogo de decisiones |
| 1.4.2 | 1.4.19 | Configuración del borde por sitio y certificación de la red segmentada en las 13 tiendas que no la tienen |
| 1.4.9 | 1.4.10 | Plano y especificación del recinto técnico del centro de datos y coordinación de su obra civil de separación |
| 1.4.12 | 1.4.13 | Sistemas de energía y climatización del centro de datos |
| 1.4.14 | 1.4.15, 1.4.16 | Sistemas de seguridad física del centro de datos y espacio de operación del personal |
| 1.4.17 | 1.4.18 | Solución de respaldo en operación con custodia de medios |
| 1.6.2 | 1.6.4, 1.6.6, 1.6.8 | Rediseño de las integraciones de la Etapa 1 (precios y existencia, crédito con el sistema de gestión empresarial, cobranza y prevención de pérdidas) |
| 1.6.3 | 1.6.5, 1.6.7 | Rediseño de las integraciones de la Etapa 2 (pedidos, marketplace y fidelización) |
| 1.7.1 | 1.7.2 | Plan de migración con estrategia de corte y de retorno e inventario de datos históricos |
| 1.7.7 | 1.7.8 | Migración de la cartera viva (620.000 clientes) con sus actas de conciliación |
| 1.8.1 | 1.8.2 | Plan de seguridad, matriz de controles y modelo de amenazas |
| 1.8.3 | 1.8.4 | Declaración de superficie de exposición y plan de respuesta a incidentes |
| 1.8.7 | 1.8.8 | Protección de datos personales y matriz de cumplimiento normativo |
| 1.8.11 | 1.8.12 | Atestación de la cadena de suministro y revisión de la arquitectura de confianza cero |
| 1.9.2 | 1.9.10 | Estándares de codificación, revisión por pares y puertas de calidad |
| 1.9.4 | 1.9.5 | Pruebas de desempeño, resiliencia y recuperación ante desastres |
| 1.11.1 | 1.11.2 | Plan de implantación con procedimiento de despliegue gradual y de reversión probado |
| 1.12.2 | 1.12.3 | Informe de resultados y evidencia de cierre de la marcha blanca de la Etapa 1 |
| 1.12.7 | 1.12.8 | Acta de aceptación final y garantía de correcto funcionamiento |
| 1.14.1 | 1.14.2 | Documentación técnica y funcional con inventario de componentes de software |
| 1.14.4 | 1.14.5 | Base de conocimiento y manuales de operación |
| 1.14.7 | 1.14.8 | Acta de cierre, traspaso final y acompañamiento de reversibilidad |
| 1.15.2 | 1.15.7 | Informes periódicos de nivel de servicio y de certificaciones |
| 1.15.4 | 1.15.5 | Mantención correctiva, preventiva y evolutiva |
