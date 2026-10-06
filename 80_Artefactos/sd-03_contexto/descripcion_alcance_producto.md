# Descripción del alcance del producto

Documento de trabajo. No es entregable.

Fuente única: `Análisis de actores, alcance y arquitectura de servicios.md` (en adelante, "el documento de origen"). Todo lo que no consta allí figura como "Pendiente de verificación". Nomenclatura: servicios R/F/X; responsabilidades A/B/C.

---

## 1. Propósito y problema

**Problema de negocio.** El documento de origen no contiene una narrativa del problema. Solo recoge, de forma dispersa:

- el registro de inventario tiene una discrepancia de conteo del 12,4 % (R-03);
- no existe un motor de precios y promociones como sistema (R-01);
- el despacho desde tienda no debe castigar a la tienda que entrega la unidad, por el incentivo de comisión (R-06);
- los consentimientos de crédito deben ser recuperables durante el plazo exigido (F-03);
- la plataforma financiera de 2011 se reemplaza por obsolescencia (F-01);
- la separación de datos entre Retail y Emisor debe ser técnica, documentada y auditable (X-01);
- el centro de distribución de Concepción opera con planillas (R-02).

Pendiente de verificación: enunciado del problema de negocio que origina el proyecto (el documento remite al Caso 09, numerales 4.x, 9.x y 18, cuyo texto no está en el documento de origen).

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

Pendiente de verificación: umbrales numéricos de cada evidencia (el documento solo nombra el tipo de evidencia).

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
| Sistema central de retail (2009) | Decisión condicional (escenarios A/B) | Sistemas que interactúan |
| Comercio electrónico (2019) | Decisión condicional | Sistemas que interactúan |
| Fidelización (2017) | Decisión condicional | R-09 |
| Extensión de WMS a Concepción | Se evalúa | Sección 3 |
| Novena plataforma | Sin asignar | Sistemas que interactúan |

### 4.2 Condición de cada decisión condicional

- **Sistema central de retail.** Escenario A: se mantiene e integra durante la transición. Escenario B: se reemplaza por etapas si se demuestra una brecha y existe una transición viable.
- **Comercio electrónico.** Se mantiene e integra si supera pruebas de latencia, disponibilidad, picos de demanda y consistencia de pedidos. Si falla la plataforma, se reemplaza. Si falla la fuente de inventario o su interfaz, se corrige esa dependencia.
- **Fidelización.** R-09 la integra solo si supera la prueba de separación de datos Retail–Emisor; si no, se reemplaza.
- **POS.** Como no está acreditada la operación offline actual, se asume que falta y se adquiere o desarrolla un POS que sí la demuestre.
- **WMS en Concepción.** Se evalúa. Mientras tanto, las planillas de Concepción no se convierten en autoridad permanente.

Pendiente de verificación: umbrales numéricos de cada prueba y definición de "brecha documentada" y "transición viable".

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
| **R-02** Abastecimiento y reposición | A3; participa en A4 y A7 | Órdenes, transferencias, propuestas de reposición, recepciones, nodos, restricciones, necesidades de abastecimiento | Planificación y coordinación de reposición | Reemplazo automático de la ejecución física del WMS; planillas de Concepción como autoridad permanente |
| **R-03** Inventario, reservas y disponibilidad | A4; sostiene A11 | Existencias por nodo, conteos, ajustes autorizados, causas de diferencia, reservas, disponible para vender, margen de confianza, estado de inventario. Autoridad de la disponibilidad comprometible | Normalización, reservas, cálculo de disponibilidad comprometible; incorpora la incertidumbre del registro por categoría y nodo | Ejecución física (WMS) y responsabilidades contables y tributarias (ERP/DTE) |
| **R-04** Pedidos y cumplimiento omnicanal | A6, A7; participa en A11 | Pedido, líneas, estado, nodo de preparación, reserva, promesa de entrega, despacho, retiro, entrega, quiebre, compensación. Autoridad del ciclo del pedido | Orquestación del ciclo del pedido; selección de nodo por costo total de servir | API Gateway; reemplazo del WMS; relación contractual completa con el transportista |
| **R-05** Registro y conciliación de ventas | A5; evidencia para C2 | Venta confirmada, reversa, pago, caja, desconexión, conciliación, estado de documento tributario | Registro y conciliación del hecho de venta | Abrir crédito nuevo sin conectividad; emitir documentos tributarios; calcular la comisión final |
| **R-06** Atribución de ventas y comisiones | Atribución dentro de A5 y A7 | Venta, pedido, canal, tienda que prepara, vendedor atribuible, regla de atribución, comisión, reversa, auditoría | Atribución multicanal y cálculo de la base de comisión | Administrar remuneraciones; decidir políticas comerciales |
| **R-07** Integración y gobierno de marketplace | A8 | Vendedor, oferta, estado de habilitación, nivel de servicio, pedido intermediado, devolución, liquidación, recobro B2B | Integración, reglas de gobierno, medición y coordinación de vendedores | Reemplazo de la plataforma marketplace; logística interna del vendedor |
| **R-08** Posventa, garantías y devoluciones | A9 | Caso, venta, motivo, recepción, inspección, elegibilidad, cambio, nota de crédito, garantía, destino de unidad, comunicación de resolución | Recepción y resolución frente al cliente | Postergar la respuesta al consumidor hasta resolver la conciliación B2B; delegar automáticamente la garantía legal al fabricante |
| **R-09** Clientes y fidelización Retail | A10; respeta C1 | Identificador Retail, deduplicación, puntos, segmentos, campañas, preferencias | Fidelización Retail con finalidad declarada | Saldos, mora, cupo o comportamiento de pago del Emisor en un perfil comercial |
| **F-01** Originación y autorización de crédito | B1 | Solicitud, identificación financiera, evaluación, cupo, decisión, condiciones precontractuales, autorización | Evaluación, originación y autorización | Abrir crédito nuevo offline; la contingencia con cupo previamente aprobado queda condicionada a una prueba de factibilidad |
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

**Auditoría.** X-01 registra cada solicitud y decisión. Control interno, cumplimiento y auditoría actúa como custodio y aprobador. Pendiente de verificación: ratificación de la custodia de X-01 (el documento la deja abierta).

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

**Expectativa verificable sobre estado de la información y punto único de falla.** Pendiente de verificación: el documento no formula un criterio verificable de coherencia entre sistemas ni de evitar un punto único de falla. Además, el documento asigna una "autoridad" por tipo de dato (R-03 para la disponibilidad comprometible, R-04 para el ciclo del pedido, entre otras), y deja abierta la validación de la fuente autoritativa. Esa asignación debe contrastarse con el enfoque de reglas explícitas de acuerdo antes de fijar la línea base.

**Convivencia durante la transición.**

- ERP/DTE, marketplace y WMS principal permanecen integrados con sus servicios.
- La plataforma financiera de 2011 se reemplaza por olas F-01/F-02/F-03.
- R-05 recibe y concilia las ventas del POS, incluso las registradas durante una desconexión.
- El sistema central de retail coexiste con R-01, R-02 y R-03 mientras se aplica el escenario elegido.
- La novena plataforma no tiene servicio ni integración asignados hasta identificarla.
- Los incrementos pueden ejecutarse iterativamente con la operación en marcha. Las prioridades se revisan por riesgo.

---

## 8. Características y restricciones de la solución

**Condiciones obligatorias que constan en el documento.**

- **Despliegue híbrido:** nube pública y componentes locales ("despliegue híbrido obligatorio").
- **Operación offline del POS:** no está acreditada; se adquiere o desarrolla un POS que la demuestre.
- **Consentimientos de crédito:** recuperables durante el plazo exigido (F-03: custodia, recuperación, integridad, retención, control de acceso). Pendiente de verificación: el plazo exigido no consta en el documento.
- **Trazabilidad probatoria (C2):** evidencia de precio publicado, venta conciliada, consentimiento y cruces.
- **Separación Retail–Emisor:** técnica, documentada y auditable (X-01).
- **ERP/DTE** permanece como único emisor de documentos tributarios.
- **WMS principal** permanece como autoridad de ejecución física donde opera.

**Operación sin conectividad.**

- Se asume que el POS actual no tiene operación offline acreditada.
- R-05 recibe y concilia las ventas registradas durante una desconexión.
- No se permite originar crédito nuevo sin conectividad (F-01 requiere conectividad).
- Una contingencia con cupo previamente aprobado queda condicionada a una prueba de factibilidad definida en el caso. Pendiente de verificación: el contenido de esa prueba.

**Marco normativo por negocio.** Pendiente de verificación: el documento de origen no enumera normas ni reguladores para Retail ni para el Emisor. Solo remite a numerales del Caso 09 (2, 4.x, 5.1, 9.x, 14.1, 17.5, 18) y menciona RT-05.20 y RT-05.21 (inventario).

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
| Escenarios A/B del sistema central de retail | El documento define ambos y no registra cuál se adopta |
| Novena plataforma | Sin servicio ni integración hasta identificarla |
| WMS en Concepción | Se evalúa |
| Comercio electrónico | Se mantiene o se reemplaza según pruebas |
| Fidelización | Se integra o se reemplaza según prueba de segregación |
| Contingencia de F-01 | Condicionada a prueba de factibilidad |
| Custodia de X-01 | Por ratificar |
| Entregable del POS | No definido (ver 4.3) |

**Decisiones que requieren aprobación.** El documento establece que los cambios al catálogo de trece servicios requieren aprobación. Pendiente de verificación: quién aprueba. No consta.

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

## Preguntas con respuesta pendiente

1. **Bloque 1:** enunciado del problema de negocio (el documento remite al Caso 09, no lo contiene) y priorización de beneficiarios.
2. **Bloque 2:** umbrales numéricos de la evidencia de cada promesa.
3. **Bloque 4:** umbrales de las pruebas de cada decisión condicional; definición de "brecha documentada" y "transición viable"; escenario (A o B) que se adopta; entregable formal del reemplazo del POS.
4. **Bloque 5:** clasificación de R-04, R-06, R-08, F-03 y X-01 como función nueva o integración.
5. **Bloque 6:** reglas de negocio específicas de cada dominio; ratificación de la custodia de X-01.
6. **Bloque 7:** criterio verificable de coherencia entre sistemas y de ausencia de punto único de falla; tecnología del bus de eventos; coherencia entre la autoridad por dato del documento y el enfoque de reglas de acuerdo.
7. **Bloque 8:** plazo de retención de consentimientos; contenido de la prueba de factibilidad de F-01; normas y reguladores aplicables a cada negocio.
8. **Bloque 9:** quién aprueba los cambios al catálogo; resolución de los elementos condicionales.
9. **Fecha de fin de soporte de la plataforma financiera de 2011 (2029):** no consta en el documento de origen; el documento solo habla de obsolescencia y plan de remediación.
10. **Bloque 10:** las cinco verificaciones abiertas del documento.
