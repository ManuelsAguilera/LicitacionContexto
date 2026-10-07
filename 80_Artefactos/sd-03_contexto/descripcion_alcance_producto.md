# Descripción del alcance del producto

Documento de trabajo. No es entregable.

Fuente única: `Análisis de actores, alcance y arquitectura de servicios.md` (en adelante, "el documento de origen"). Todo lo que no consta allí figura como "Pendiente de verificación". Nomenclatura: servicios R/F/X; responsabilidades A/B/C.

---

## 1. Propósito, problema y causas raíz

**Problema de negocio.** Ancoa no puede cumplir ni demostrar sus cuatro promesas (existencia, precio, entrega y crédito). Las brechas van de 1,9 a 36,5 veces el valor tolerable (sd-02, 2.3). Su origen no es un sistema, sino cinco causas raíz que actúan en conjunto (sd-02, 2.2.2 y 2.3.7). Esta descripción las toma tal como las fija el sd-02.

| Causa raíz (sd-02) | Qué es | Evidencia principal |
| :-- | :-- | :-- |
| **C1 Registro impreciso** | El inventario y el maestro de artículos no reflejan lo físico | 12,4 % de discrepancia; sin conteo cíclico sistemático; sin auditoría del maestro de artículos; merma en una sola cifra indiferenciada |
| **C2 Tejido de integración** | Las plataformas se conectan sin contrato ni mapa y muestran estados distintos | 9 plataformas de 6 proveedores y 14 interfaces punto a punto, la mayoría por lote nocturno; nadie conoce el mapa; sin motor de precios; POS en tres versiones |
| **C3 Frontera difusa** | Retail y filial financiera comparten recursos con separación parcial y no documentada | Fidelización mezcla datos comerciales y financieros; marketing busca usar el comportamiento de pago; el cruce no tiene finalidad, base de licitud ni control técnico escrito |
| **C4 Incentivos y capacidad** | La comisión y la capacidad operativa compiten con los pasos que garantizan las promesas | 3.820 vendedores con comisión variable y 62 % de rotación; 640 terminales compartidas; unos 1.100 repositores externos sin acceso individualizado; 46 personas de TI para nueve plataformas |
| **C5 Territorio y calendario** | Conectividad, red, cumplimiento y calendario limitan cómo y cuándo se puede intervenir | 7 de 15 tiendas sin enlace de respaldo; 13 de 22 sin red segmentada; PCI DSS definido solo para el canal digital; 126 días al año de congelamiento |

Nota de nomenclatura: las causas C1 a C5 del sd-02 no son las responsabilidades C1 a C3 (frontera y controles) de la sección 2. En el sd-03 se escribe siempre "causa C3" o "responsabilidad C3", nunca "C3" a secas.

**Cómo responde el alcance a cada causa.** Propuesta de trazabilidad causa a solución, por validar:

| Causa | Servicios y componentes que la atacan | Alcance relacionado |
| :-- | :-- | :-- |
| C1 | R-03 (existencias, conteos, causas de diferencia, margen de confianza), R-01 (maestro de artículos), R-02 (reposición) | Estrategia de corte de inventario; centro de Concepción se mantiene como está y se evalúa (EXC-13, SP-02) |
| C2 | Plataforma de integración (responsabilidad C3), R-04 (estado único del pedido), R-01 (motor de precios), reemplazo de la plataforma financiera, el sistema central y el POS | Mapa de las 14 integraciones como entrega temprana |
| C3 | X-01, R-09, F-01 a F-03 | Autorización y auditoría de cada cruce; ninguna vista unificada antes de separar los datos |
| C4 | R-06 (atribución de comisiones), R-04 (compensación a la tienda que despacha), IAM individualizado | Capacitación compatible con la rotación; dispositivos solo especificados (EXC-03) |
| C5 | POS y componente on-premise con 24 h de autonomía, plataforma híbrida | Red y enlaces de respaldo solo especificados y costeados (EXC-08, EXC-10); plan que respeta las ventanas de congelamiento |

Toda pieza del alcance debe rastrearse a una causa, y ninguna causa se resuelve con un solo servicio.

Aviso sobre el sd-02: la sección 2.1 afirma que "cada síntoma apunta a la misma causa" (escrituras concurrentes sobre un estado sin fuente única), mientras el resto del documento plantea cinco causas. Conviene unificar la redacción en el sd-02 para que 3.1 y 3.2 no se contradigan con él.

**Para qué existe la solución.** Para que Ancoa pueda cumplir y demostrar cuatro promesas diarias al cliente (sección 2), con el negocio comercial (Retail) y el negocio de crédito fiscalizado (Emisor) mantenidos separados.

**Quién se beneficia.** El documento no define "beneficiarios" como categoría. Identifica a quienes interactúan directamente con los servicios (sección 9): clientes, personal de venta y caja, operación de tiendas y centros de distribución, áreas de negocio, Negocio Financiero, control interno, vendedores de marketplace, repositores externos y transportistas. Pendiente de verificación: priorización de beneficiarios.

---

## 2. Las promesas

Ancoa debe poder cumplir y demostrar:

1. **Existencia:** el producto existe y la disponibilidad publicada considera la calidad real del registro.
2. **Precio:** el precio exhibido, publicado y cobrado coincide y puede acreditarse después.
3. **Entrega:** el pedido tiene un estado único y llega en la fecha comprometida.
4. **Crédito:** las condiciones informadas al cliente son las que este acepta y pueden demostrarse ante una autoridad.

Responsabilidades:

- **A (Retail):** A1 catálogo y oferta; A2 precios y promociones; A3 abastecimiento y reposición; A4 inventario, reservas y disponibilidad; A5 venta y conciliación; A6 canales digitales; A7 pedidos y cumplimiento; A8 marketplace; A9 posventa, cambios y garantías; A10 clientes y fidelización. A11 es el escenario de alta demanda que pone a prueba varias responsabilidades Retail.
- **B (Emisor):** B1 originación y autorización; B2 administración de cartera y cobranza; B3 repactaciones y modificaciones contractuales.
- **C (frontera y controles):** C1 separación y gobierno de datos entre Retail y Emisor; C2 evidencia y trazabilidad probatoria; C3 integración, plataforma y operación técnica.

| Promesa | Responsabilidades | Servicios | Evidencia que permite verificarla |
| :-- | :-- | :-- | :-- |
| Existencia | A3, A4, A11 | R-02, R-03, R-04, R-07 | Exactitud por categoría y nodo; disponibilidad comprometible; reservas; cancelaciones por falta de existencia |
| Precio | A1, A2, C2 | R-01, R-05, R-06 | Historial de precio publicado; estado de etiqueta; venta conciliada; atribución auditable |
| Entrega | A3, A6, A7, A11 | R-02, R-03, R-04, R-07, R-08 | Fecha prometida; estado único; nodo; despacho o retiro; tasa de cumplimiento |
| Crédito | B1, B2, B3, C1, C2 | F-01, F-02, F-03, X-01 | Versión precontractual; consentimiento; expediente recuperable; auditoría de cruces |

Umbrales (Caso 09, cap. 15, RT-09.01 y RT-05.29, medidos en percentil 95 según las Bases Transversales 9.1):

- Disponibilidad publicada en el canal digital: consulta en 400 ms o menos; actualizada a más tardar 30 s después de una venta en cualquier canal.
- Precio: propagación a las 380 líneas de caja y al canal digital en 5 min o menos; trazabilidad del precio publicado por canal durante 5 años. Fundamento: el Caso fija 3 años para el historial del precio publicado (RT-05.10); la auditoría de los cambios de precio (quién, cuándo y con qué autorización) no la fija el Caso, por lo que rige el mínimo de 5 años de RT-16.10 ("el que fije el caso y, en su defecto, no inferior a cinco años"). Como el historial y su auditoría son juntos la evidencia para acreditar qué precio estaba publicado (restricción 4 del Caso), se conservan ambos 5 años. Los 2 años adicionales del historial son una mejora declarada sobre el Caso, no una exigencia suya.
- Existencia en sala: consulta en 2 s o menos, con el grado de confianza del dato.
- Entrega: estado del pedido en tiempo real y consistente en todos los canales; confirmación de pedido en 3 s o menos durante el evento anual.
- Crédito: evaluación crediticia en el punto de venta en 8 s o menos.
- Venta completa en caja con medio de pago externo: 25 s o menos (el Caso la define; las Transversales delegan en el caso).
- Los demás indicadores quedan para los criterios de aceptación.

---

## 3. Descripción general de la solución

**La solución.** Un conjunto de trece servicios de aplicación (nueve Retail, tres del Emisor y uno de frontera) que asumen las responsabilidades A/B/C, apoyados en una plataforma técnica común (C3). Cada servicio tiene responsabilidad propia, contrato de entrada y salida, datos bajo autoridad definida, actores consumidores, interacciones identificadas y unidad de despliegue. Los sistemas existentes se reemplazan, se conservan o quedan condicionados según la sección 4.

**Organización.**

| Bloque | Qué contiene |
| :-- | :-- |
| Retail (R-01 a R-09) | Catálogo y precios, abastecimiento, inventario y disponibilidad, pedidos, ventas, atribución de comisiones, marketplace, posventa, clientes y fidelización |
| Emisor (F-01 a F-03) | Originación y autorización, cartera y cobranza, consentimiento y evidencia |
| Frontera (X-01) | Autorización y auditoría de cruces entre Retail y Emisor |
| Plataforma (C3) | Componentes técnicos compartidos que habilitan los servicios; no son dueños de reglas de negocio |

---

## 4. Sistemas existentes

### 4.1 Qué se conserva, qué se reemplaza y qué queda condicionado

| Sistema | Destino | Fuente en el documento |
| :-- | :-- | :-- |
| ERP/DTE | Se conserva. Único emisor tributario | Sistemas que interactúan |
| Marketplace (2022) | Se conserva e integra; no se reemplaza | Sistemas que interactúan; R-07 |
| WMS principal | Se conserva; autoridad de ejecución física donde opera | Sistemas que interactúan; R-03 |
| Plataforma financiera (2011) | Reemplazo obligatorio, por olas | F-01, F-02, F-03 |
| POS (2014) | Reemplazo propuesto | Sistemas que interactúan |
| Sistema central de retail (2009) | Reemplazo por etapas con convivencia (Escenario B, SP-01) | Sistemas que interactúan; decisión del equipo |
| Comercio electrónico (2019) | Se evalúa e integra; reemplazo excluido (EXC-15) | Sistemas que interactúan; decisión del equipo |
| Fidelización (2017) | Se evalúa e integra; reemplazo excluido (EXC-15) | R-09; decisión del equipo |
| Centro de distribución de Concepción | Se mantiene como está; se evalúa la extensión del WMS (EXC-13, SP-02) | Sección 3 |
| Planillas de cálculo y listas impresas (novena plataforma) | Reemplazo como sistema de registro (Caso cap. 5); ver cobertura abajo | R-01, R-03, R-08 e identidad (1.14c); Concepción: R-03 y SP-02 |

### 4.2 Condición de cada decisión condicional

- **Sistema central de retail.** Decidido: Escenario B. Se reemplaza por etapas con convivencia, como compromiso firme (supuesto SP-01 de `enunciado_alcance.md`).
- **Comercio electrónico.** Alcance: evaluarlo e integrarlo con pruebas de latencia, disponibilidad, picos de demanda y consistencia de pedidos. Su reemplazo queda excluido (EXC-15) y solo entra por control de cambios si la plataforma falla; si falla la fuente de inventario o su interfaz, se corrige esa dependencia.
- **Fidelización.** Alcance: R-09 la evalúa e integra con la prueba de separación de datos Retail–Emisor. Su reemplazo queda excluido (EXC-15) y solo entra por control de cambios si no supera la prueba.
- **POS.** Como no está acreditada la operación offline actual, se asume que falta y se adquiere o desarrolla un POS que sí la demuestre.
- **Centro de Concepción.** Se mantiene como está (SP-02). Se evalúa la extensión del WMS (1.20c). La planilla de Concepción no es autoridad del registro de existencias: lo es R-03; la planilla queda como herramienta de ubicación física dentro del centro.

Pendiente de verificación: umbrales numéricos de las pruebas de e-commerce y de fidelización (criterios de aceptación). Para el sistema central, "brecha documentada" queda cubierta por SP-01; "transición viable" se demuestra con el plan de convivencia por etapas.

### 4.3 Entregable del reemplazo del POS

El documento indica que se adquiere o desarrolla un POS con operación offline demostrada, y que el POS es "canal de borde" mientras R-05 registra y concilia el hecho de venta. No lo cuenta entre los trece servicios ni le asigna código.

Pendiente de verificación: entregable formal del POS (producto, hito, criterio de aceptación, ubicación en el alcance). El documento no lo define.

### 4.4 Relación entre plataformas reemplazadas y servicios

No es uno a uno. Las plataformas existentes no reciben códigos R/F/X; son sistemas integrados durante la coexistencia o sujetos al destino de cada escenario. Lo que sí está documentado:

- **Plataforma financiera de 2011:** sus responsabilidades pasan a tres servicios, F-01, F-02 y F-03, mediante olas.
- **Sistema central de retail:** R-01, R-02 y R-03 se coordinan con sus datos y funciones durante la coexistencia.
- **POS:** R-01 le entrega precios; R-03 recibe sus movimientos; R-05 registra y concilia sus ventas, incluso durante una desconexión; F-01 requiere conectividad para originar crédito nuevo.
- **Fidelización:** R-09 la integra o la reemplaza.
- **Precios y promociones:** no existe como sistema; se incorpora como función nueva de R-01.

---

## 5. Catálogo de servicios

Los trece servicios son unidades desplegables comprometidas. La decisión de implementarlos como uno o más microservicios es posterior y no agrega códigos.

| Servicio | Responsabilidad | Datos bajo autoridad | Incluye | Excluye |
| :-- | :-- | :-- | :-- | :-- |
| **R-01** Catálogo, precios y promociones | A1, A2; evidencia para C2 | Artículos, atributos, categorías, precios, promociones, vigencias, canales, estado de etiqueta, historial de publicación | Maestro comercial, reglas de precio, distribución y trazabilidad de publicación | Reservas, registro de ventas, remuneraciones, fidelización |
| **R-02** Abastecimiento y reposición | A3; participa en A4 y A7 | Órdenes, transferencias, propuestas de reposición, recepciones, nodos, restricciones, necesidades de abastecimiento | Planificación y coordinación de reposición | Reemplazo automático de la ejecución física del WMS; las planillas de Concepción como autoridad del registro de existencias |
| **R-03** Inventario, reservas y disponibilidad | A4; sostiene A11 | Existencias por nodo, conteos, ajustes autorizados, causas de diferencia, reservas, disponible para vender, margen de confianza, estado de inventario. Autoridad de la disponibilidad comprometible | Normalización, reservas, cálculo de disponibilidad comprometible; incorpora la incertidumbre del registro por categoría y nodo, incluido el nodo Concepción con su margen de confianza declarado (SP-02) | Ejecución física (WMS) y responsabilidades contables y tributarias (ERP/DTE) |
| **R-04** Pedidos y cumplimiento omnicanal | A6, A7; participa en A11 | Pedido, líneas, estado, nodo de preparación, reserva, promesa de entrega, despacho, retiro, entrega, quiebre, compensación. Autoridad del ciclo del pedido | Orquestación del ciclo del pedido; selección de nodo por costo total de servir | API Gateway; reemplazo del WMS; relación contractual completa con el transportista |
| **R-05** Registro y conciliación de ventas | A5; evidencia para C2 | Venta confirmada, reversa, pago, caja, desconexión, conciliación, estado de documento tributario | Registro y conciliación del hecho de venta | Abrir crédito nuevo sin conectividad; emitir documentos tributarios; calcular la comisión final |
| **R-06** Atribución de ventas y comisiones | Atribución dentro de A5 y A7 | Venta, pedido, canal, tienda que prepara, vendedor atribuible, regla de atribución, comisión, reversa, auditoría | Atribución multicanal y cálculo de la base de comisión | Administrar remuneraciones; decidir políticas comerciales |
| **R-07** Integración y gobierno de marketplace | A8 | Vendedor, oferta, estado de habilitación, nivel de servicio, pedido intermediado, devolución, liquidación, recobro B2B | Integración, reglas de gobierno, medición y coordinación de vendedores | Reemplazo de la plataforma marketplace; logística interna del vendedor |
| **R-08** Posventa, garantías y devoluciones | A9 | Caso, venta, motivo, recepción, inspección, elegibilidad, cambio, nota de crédito, garantía, destino de unidad, comunicación de resolución | Recepción y resolución frente al cliente | Postergar la respuesta al consumidor hasta resolver la conciliación B2B; delegar automáticamente la garantía legal al fabricante |
| **R-09** Clientes y fidelización Retail | A10; respeta C1 | Identificador Retail, deduplicación, puntos, segmentos, campañas, preferencias | Fidelización Retail con finalidad declarada | Saldos, mora, cupo o comportamiento de pago del Emisor en un perfil comercial |
| **F-01** Originación y autorización de crédito | B1 | Solicitud, identificación financiera, evaluación, cupo, decisión, condiciones precontractuales, autorización | Evaluación, originación y autorización | Abrir tarjetas o ampliar cupos sin conexión (EXC-16); la compra con cupo ya aprobado se autoriza contra un caché con topes fijados por el Emisor, sujeta a la prueba de factibilidad (`fundamentacion_credito_sin_conexion.md`) |
| **F-02** Cartera, cobranza y repactaciones | B2, B3 | Cuenta, saldo, cuotas, pagos, mora, comunicaciones, cobranza, nueva condición, estado de repactación | Cartera viva, cobranza y repactación | Compartir saldos con R-09; convertir la migración de cartera en función permanente |
| **F-03** Consentimiento y evidencia financiera | B1, B3; C2 | Versión de información precontractual, aceptación, consentimiento, fecha, relación con operación, expediente recuperable | Custodia, recuperación, integridad, retención y control de acceso | Administrar saldos; reemplazar a F-01 o F-02 |
| **X-01** Autorización y auditoría de cruces Retail–Emisor | C1 y la parte de C2 relativa a cada cruce | Finalidad, base de autorización, solicitante, atributos mínimos, respuesta, fecha, evidencia del cruce | Autorización, minimización, auditoría, denegación por omisión | Maestro único de clientes; exponer atributos financieros a Marketing; reemplazar IAM |

**Servicios que integran sistemas que se conservan.** R-02 y R-03 (WMS y ERP/DTE), R-04 (POS, comercio electrónico, WMS, marketplace y transportistas), R-05 (ERP/DTE y POS), R-06 (sistema empresarial de remuneraciones), R-07 (marketplace), R-08 (ERP/DTE).

**Servicios que asumen responsabilidades de un sistema reemplazado.** F-01, F-02 y F-03 (plataforma financiera de 2011).

**Función nueva declarada.** Precios y promociones, dentro de R-01.

Pendiente de verificación: el documento no clasifica como "nuevo" a R-04, R-06, R-08, F-03 ni X-01; no se completa.

---

## 6. Separación Retail–Emisor

**Qué pertenece a cada negocio.**

- **Retail:** catálogo, precios, inventario, ventas, pedidos, marketplace, posventa y fidelización. Servicios R-01 a R-09.
- **Emisor:** originación, autorización, cartera, cobranza, repactaciones, consentimiento y evidencia financiera. Servicios F-01 a F-03. Es un negocio fiscalizado con frontera jurídica y de datos separada de Retail, incluso cuando la misma persona actúa en ambos.

Pendiente de verificación: reglas de negocio específicas de cada dominio más allá de las fichas de servicio.

**Cruces permitidos.** Solo a través de X-01, con:

- finalidad declarada por el servicio solicitante;
- base de autorización de los dueños de datos Retail y Emisor;
- entrega del dato mínimo necesario o de una respuesta puntual;
- registro de cada decisión (finalidad, solicitante, atributos, respuesta, fecha, evidencia);
- denegación por omisión.

Solicitantes citados: R-09, F-01, F-02 u otros servicios autorizados. X-01 no consulta directamente las bases de otro negocio. Los actores transversales controlados (auditoría, cumplimiento) cruzan solo por un mandato definido, justificado, limitado y registrado.

**Auditoría.** X-01 registra cada solicitud y decisión. Control interno, cumplimiento y auditoría actúa como custodio y aprobador. Custodia de X-01 ratificada: control interno, cumplimiento y auditoría como custodio y aprobador.

**Prohibido cruzar.**

- Crear un maestro único de clientes.
- Exponer atributos financieros a Marketing.
- Incorporar saldos, mora, cupo o comportamiento de pago del Emisor a un perfil comercial (R-09).
- Compartir saldos de F-02 con R-09.
- Consultar directamente las bases del otro negocio.

---

## 7. Plataforma e integración (C3)

**Componentes comunes.**

| Componente | Función | Estado |
| :-- | :-- | :-- |
| API Gateway | Entrada, ruteo, autenticación técnica, políticas de exposición | Declarado |
| Bus de eventos y adaptadores | Transporte de eventos y conexión con POS, comercio electrónico, WMS, ERP/DTE, marketplace y plataforma financiera | Declarado. Kafka puede evaluarse; el producto no está fijado |
| IAM y gestión de secretos | Identidad, autorización técnica, segregación de Retail y Emisor, mínimo privilegio | Declarado |
| Observabilidad | Logs, métricas, trazas, alertas, evidencia operacional | Declarado |
| Plataforma híbrida | Nube pública y componentes locales en tiendas, centros de distribución y sistemas que deban permanecer allí | Declarado, conforme al despliegue híbrido obligatorio |

También se menciona middleware como componente técnico de C3. Ninguno de estos componentes es un servicio de negocio ni posee reglas de dominio.

**Decisiones abiertas.** Tecnología del bus de eventos (Kafka es solo una opción), contratos de integración y fuente autoritativa de artículo, precio, inventario, DTE, comisión y saldo.

**Expectativa verificable sobre estado de la información y punto único de falla.** Decisión: se mantiene una autoridad por tipo de dato (R-03 para la disponibilidad comprometible, R-04 para el ciclo del pedido, entre otras). Esto responde a la "fuente única de verdad de la existencia" que pide el Caso (cap. 16.1, n.º 1) y el art. 17.2 de las Bases Administrativas. Las reglas explícitas de acuerdo son el mecanismo que reconcilia las copias en las demás plataformas, de modo que ningún sistema concentre el riesgo de falla.

Criterio verificable: si cae una autoridad de dato, los demás servicios siguen operando con una confianza degradada declarada, y al volver se reconcilian según una regla escrita (consenso entre réplicas o reconciliación determinista), sin pérdida de transacciones.

El algoritmo concreto (por ejemplo, consenso por quórum entre réplicas de una misma autoridad) es decisión de diseño y va en 3.3 y 3.4, no en el alcance. En el borde desconectado rige la reconciliación determinista, porque una tienda sin enlace no puede alcanzar quórum (RT-03.10, RT-03.13).

**Convivencia durante la transición.**

- ERP/DTE, marketplace y WMS principal permanecen integrados con sus servicios.
- La plataforma financiera de 2011 se reemplaza por olas F-01/F-02/F-03.
- R-05 recibe y concilia las ventas del POS, incluso las registradas durante una desconexión.
- El sistema central de retail coexiste con R-01, R-02 y R-03 mientras se aplica el escenario elegido.
- Las planillas y listas impresas son la novena plataforma. El Caso (cap. 5) dice que "deben desaparecer como sistema de registro". Cobertura: precios de campaña y cambio de etiquetas, R-01; control de devoluciones y seguimiento de reclamos, R-08; control de repositores externos, acceso individualizado y registro de actividad por identidad (1.14c), sin imponerles herramientas ni capacitación (restricción 12 del Caso); centro de distribución de Concepción, R-03 es el registro de sus existencias, que recibe por carga estructurada, y la planilla queda solo como herramienta de ubicación física dentro del centro (SP-02).
- Los incrementos pueden ejecutarse iterativamente con la operación en marcha. Las prioridades se revisan por riesgo.

---

## 8. Características y restricciones de la solución

**Condiciones obligatorias que constan en el documento.**

- **Despliegue híbrido:** nube pública y componentes locales ("despliegue híbrido obligatorio").
- **Operación offline del POS:** no está acreditada; se adquiere o desarrolla un POS que la demuestre.
- **Consentimientos de crédito:** recuperables durante el plazo exigido (F-03: custodia, recuperación, integridad, retención, control de acceso). Plazo: el del crédito más 6 años, incluidas las grabaciones y soportes del consentimiento, que reemplazan la práctica actual de 90 días (Caso, RT-05.10).
- **Trazabilidad probatoria (C2):** evidencia de precio publicado, venta conciliada, consentimiento y cruces.
- **Separación Retail–Emisor:** técnica, documentada y auditable (X-01).
- **ERP/DTE** permanece como único emisor de documentos tributarios.
- **WMS principal** permanece como autoridad de ejecución física donde opera.

**Operación sin conectividad.**

- El componente on-premise opera de forma autónoma al menos 24 horas continuas sin enlace (RT-03.10 de las Transversales, mayor que las 8 h en tienda y 4 h en el CD principal del Caso). Al reconectar, la sincronización no supera 30 minutos, sin pérdida de ventas ni documentos y con resolución determinista de la existencia comprometida en otros canales (RT-03.13 del Caso, aplicado a 24 h).
- Se asume que el POS actual no tiene operación offline acreditada.
- R-05 recibe y concilia las ventas registradas durante una desconexión.
- No se permite originar crédito nuevo sin conectividad (F-01 requiere conectividad).
- La compra con un cupo previamente aprobado se autoriza contra un caché con topes que fija el Emisor, condicionada a la prueba de factibilidad definida en `fundamentacion_credito_sin_conexion.md` (secciones 6 y 7).

**Marco normativo por negocio** (Caso 09, cap. 12, orientador y no exhaustivo; el proponente debe completarlo).

- **Retail:** protección del consumidor (Ley 19.496), información y publicidad de precios, contratación a distancia, garantía legal, intermediación en plataformas digitales, documentos tributarios electrónicos, medios de pago con tarjeta, normativa laboral.
- **Emisor:** régimen de emisores de tarjetas de casa comercial y fiscalización de la autoridad del mercado financiero, protección del consumidor financiero, repactación de deudas, cobranza extrajudicial, tasa máxima convencional, prevención de lavado de activos.

Cerrado: la Ley 21.719 sí figura en el cap. 12 del Caso (protección de datos personales, con atención al perfilamiento y al uso del comportamiento de pago con finalidad comercial) y está en el objetivo (4).

---

## 9. Actores y condicionales

**Actores principales y servicios con los que interactúan.**

| Actor | Servicios |
| :-- | :-- |
| Cliente / consumidor | R-01, R-03, R-04, R-08, R-09; F-01, F-02, F-03 |
| Personal de venta y caja | R-01, R-03, R-04, R-05, R-06; F-01 bajo autorización |
| Jefaturas de tienda o departamento | R-01 a R-06 y R-08, según permisos |
| Operación de sala y bodega de tienda | R-02, R-03, R-04, R-08 |
| Operación de centros de distribución | R-02, R-03, R-04 |
| Prevención de Pérdidas | R-03 |
| Comercial y compras | R-01, R-02 |
| Logística y planificación | R-02, R-03, R-04 |
| Marketing y canales digitales | R-01, R-04, R-07, R-09 |
| Administración y finanzas | R-05, R-06, R-07 |
| Atención al cliente Retail | R-04, R-07, R-08 |
| Negocio financiero / Emisor | F-01, F-02, F-03 |
| Control interno, cumplimiento y auditoría | F-03, X-01; controles de R-01, R-05, R-09 |
| TI y soporte | Todos, como soporte; no es servicio de negocio |
| Vendedor marketplace | R-04, R-07, R-08 |
| Repositor externo de proveedor | R-01, R-02, cuando corresponda |
| Transportista | R-04 |

Grupos de interés no operativos: Dirección y control, Propiedad, organismos externos (autoridad financiera, autoridad de protección al consumidor, autoridad tributaria).

**Elementos condicionales o sin asignar.**

| Elemento | Estado |
| :-- | :-- |
| Escenarios A/B del sistema central de retail | Resuelto: Escenario B (SP-01) |
| Planillas (novena plataforma) | Cubiertas por R-01, R-08, 1.14c y R-03 |
| Centro de Concepción | Se mantiene como está; extensión del WMS solo evaluada (SP-02) |
| Comercio electrónico | Se evalúa e integra; reemplazo excluido (EXC-15) |
| Fidelización | Se evalúa e integra; reemplazo excluido (EXC-15) |
| Contingencia de F-01 | Condicionada a prueba de factibilidad |
| Custodia de X-01 | Ratificada |
| Entregable del POS | No definido (ver 4.3) |

**Decisiones que requieren aprobación.** El documento establece que los cambios al catálogo de trece servicios requieren aprobación. Aprueba el Comité Ejecutivo, mediante solicitud formal de cambio con análisis de impacto (Bases Administrativas, art. 72).

---

## 10. Cierre: verificaciones abiertas antes de fijar la línea base

Según el documento de origen, quedan abiertas:

1. Confirmar la asignación individual de cada RF/SUP.
2. Validar la fuente autoritativa de artículo, precio, inventario, DTE, comisión y saldo.
3. Confirmar los contratos de integración.
4. Probar la contingencia de F-01.
5. Ratificar la custodia de X-01.

Estas verificaciones no cambian el catálogo de trece servicios, pero pueden ajustar contratos, etapas o sistemas integrados.

---

## Pendientes tras las decisiones

Cerrado: problema de negocio, umbrales de las promesas, escenario del sistema central, e-commerce y fidelización, autoridad por dato, criterio de punto único de falla, operación sin conexión (24 h), retención de consentimientos, fecha 2029, marco normativo (cap. 12 del Caso), custodia de X-01, aprobador de cambios, clasificación "nuevo o integración" (descartada por no afectar el alcance).

Pendiente:

1. (Resuelto) Umbrales de las pruebas de e-commerce y de fidelización en `asignacion_etapas.md` (F2); prueba de factibilidad de F-01 en `fundamentacion_credito_sin_conexion.md`; los topes los fija el Emisor (RC-11).
2. (Resuelto) Entregable formal del POS: 1.16, con su compuerta de 9 condiciones.
3. Reglas de negocio específicas de cada dominio más allá de las fichas.
4. Tecnología del bus de eventos y contratos de integración (diseño, 3.3 y 3.4).
5. (Resuelto) Ley 21.719 en el objetivo (4).
6. Objetivo general del proyecto.
