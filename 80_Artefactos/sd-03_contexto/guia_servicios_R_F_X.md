# Guía de los 13 servicios (R-01 a R-09, F-01 a F-03, X-01)

Documento de contexto, no es entregable. Explica qué es cada servicio y cómo se conecta con el negocio de Ancoa. Fuente: `descripcion_alcance_producto.md` (secciones 2, 5 y 6) y Caso 09. La capa y la etapa salen de `asignacion_etapas.md` (Rondas B a D).

## Qué se hizo en este plan

El Caso y las Bases piden cumplir un calendario de dos etapas (Etapa 1: desarrollo en los meses 1 a 12, marcha blanca en 13 a 15 y producción en el mes 16; Etapa 2: desarrollo en 13 a 18, marcha blanca en 19 y 20 y producción en el mes 21). Había que decidir qué entregable va en cada una. Se hizo en seis rondas, siempre con una sugerencia del asistente y la decisión del equipo:

1. **Ciclo de vida:** se acordó un marco híbrido. Es predictivo en lo contractual (etapas, hitos, 13 servicios, cambios por solicitud formal) y adaptativo en el desarrollo dentro de cada etapa.
2. **Cinco criterios, en este orden:** (1) lo que fijan las Bases, (2) dependencias técnicas, (3) riesgo e hitos externos, (4) capacidad de absorción del cliente, (5) prioridad del comité.
3. **Rondas A a F:** A fijó lo que mandan las Bases y qué es una integración crítica; B ordenó los servicios por dependencias en capas 0 a 4; C ubicó lo financiero por el plazo de 2029; D balanceó la carga del cliente (46 personas de TI para nueve plataformas) y definió el POS en dos olas; E contrastó con el orden del comité; F resolvió los casos especiales.
4. **Resultado:** cada entregable quedó con una etapa en `entregables_alcance.md`. Esta guía explica los 13 servicios y la razón de la etapa de cada uno. El detalle de cada decisión está en `asignacion_etapas.md`.

Capas de dependencia (Ronda B): la capa 0 es la base común (plataforma de integración, identidad, observabilidad y mapa de las 14 integraciones); cada capa siguiente necesita las anteriores.

## Cómo leerlo

- **R-xx** = servicios de **Retail** (la tienda): R-01 a R-09. Nueve servicios.
- **F-xx** = servicios del **Emisor** (el crédito, negocio fiscalizado): F-01 a F-03. Tres servicios.
- **X-01** = servicio de **frontera** entre ambos negocios. Uno.
- Un servicio es una unidad desplegable comprometida. Cada uno es la **autoridad** de ciertos datos: lo que dice ese servicio sobre esos datos es lo que vale. Los demás sistemas lo consultan, no lo pisan.
- Ancoa es a la vez una tienda y un emisor de crédito con dos regímenes jurídicos. Por eso la separación Retail / Emisor es la línea roja de todo el diseño.

## Las cuatro promesas que sostienen los servicios

| Promesa | Qué significa para el cliente | Servicios |
| :-- | :-- | :-- |
| Existencia | Si dice que hay, hay (hoy el registro discrepa 12,4 %) | R-02, R-03, R-04, R-07 |
| Precio | El precio exhibido, publicado y cobrado es el mismo, y se puede acreditar después (hoy hay discrepancia de 11 % fiscalizada) | R-01, R-05, R-06 |
| Entrega | El pedido tiene un estado único y llega cuando se prometió | R-02, R-03, R-04, R-07, R-08 |
| Crédito | Las condiciones informadas son las aceptadas y se pueden demostrar ante la autoridad | F-01, F-02, F-03, X-01 |

## Retail (R)

| Servicio | Qué es | Conexión con el negocio | Capa y etapa | Por qué esta etapa |
| :-- | :-- | :-- | :-- | :-- |
| **R-01** Catálogo, precios y promociones | El maestro de artículos y precios, con vigencias, canales, estado de la etiqueta e historial de lo publicado | Sostiene la promesa de precio: de aquí sale el precio a cajas, sitio y sala. Guarda qué precio estaba publicado en cada momento (5 años) | Capa 1, Etapa 1 | Etapa 1: primera prioridad del comité (precio) y dependencia de R-02, R-03, R-04 y R-05, que usan el artículo y su precio. Sostiene la promesa de precio. |
| **R-02** Abastecimiento y reposición | Órdenes, transferencias, recepciones y propuestas de reposición | Hoy la reposición se calcula sobre un inventario con 12,4 % de error. Coordina qué se pide y a quién. No reemplaza la ejecución física del WMS | Capa 3, Etapa 2 | Etapa 2: necesita R-01 y R-03 estables. El comité prioriza inventario y precio antes que la reposición, y su migración desde el sistema central cierra con el retiro de ese sistema. |
| **R-03** Inventario, reservas y disponibilidad | Existencias por tienda y centro de distribución, reservas y "disponible para vender", con un margen de confianza | Es el corazón del problema de inventario. Dice cuánto se puede prometer en cada canal sin vender dos veces lo mismo | Capa 2, Etapa 1 | Etapa 1: primera prioridad del comité (inventario y disponibilidad). Necesita solo R-01. Del inventario dependen R-04, R-07 y R-08, y las integraciones críticas con el WMS y el e-commerce. |
| **R-04** Pedidos y cumplimiento omnicanal | El ciclo del pedido: reserva, nodo que lo prepara, promesa, despacho, retiro, entrega | Da un estado único del pedido en los cuatro canales y elige desde dónde despachar | Capa 3, Etapa 2 | Etapa 2: necesita R-01, R-03 y R-05. Respeta el orden del comité (después de inventario). |
| **R-05** Registro y conciliación de ventas | El hecho de venta: confirmación, reversa, pago, caja, desconexión, estado del documento tributario | Lo que se vende en caja, incluidas las ventas hechas sin conexión, se registra y se concilia aquí. Emitir el documento lo hace el ERP | Capa 2, Etapa 1 | Etapa 1: sostiene la venta con documento tributario y las ventas sin conexión del POS. Integración crítica POS–R-05. Se descartó moverlo a la Etapa 2 para aliviar al cliente. |
| **R-06** Atribución de ventas y comisiones | Qué vendedor y qué canal merecen crédito por una venta, y la base de la comisión | Resuelve la disputa cuando la venta nace en un canal y se cumple en otro. No gestiona remuneraciones (EXC-05) | Capa 4, Etapa 2 | Etapa 2: necesita R-04 y R-05. Resuelve atribución de comisiones, que no sostiene una promesa de primera prioridad. |
| **R-07** Integración y gobierno del marketplace | Vendedores, ofertas, nivel de servicio, pedidos intermediados, devoluciones y liquidación | Gobierna el marketplace que se mantiene (EXC-04, EXC-12): lo mide y resuelve la devolución en tienda | Capa 4, Etapa 2 | Etapa 2: necesita R-03 estable y el comité pone al marketplace al final. Mientras tanto el marketplace sigue operando como hoy (EXC-12). |
| **R-08** Posventa, garantías y devoluciones | Casos, inspección, cambios, notas de crédito y garantía | La garantía legal es ante la compañía; no se delega al fabricante ni se posterga la respuesta al cliente | Capa 4, Etapa 2 | Etapa 2: necesita R-03 (reingreso a inventario) y R-05 (la venta original). No es de primera prioridad. |
| **R-09** Clientes y fidelización Retail | Identificador de cliente Retail, deduplicación, puntos, segmentos y campañas | La fidelización con finalidad declarada. Nunca incluye saldos, mora ni comportamiento de pago del Emisor | Capa 3, Etapa 2 | Etapa 2: necesita R-01 y X-01. El comité pone la analítica al final, y su integración con fidelización va después de la prueba de separación de datos de la Etapa 1. |

## Emisor (F)

| Servicio | Qué es | Conexión con el negocio | Capa y etapa | Por qué esta etapa |
| :-- | :-- | :-- | :-- | :-- |
| **F-01** Originación y autorización de crédito | Solicitud, evaluación, cupo, decisión y autorización del crédito | El crédito es el 38 % de la venta de tiendas. Evalúa en 8 s o menos en el punto de venta. No abre crédito nuevo sin conectividad (EXC-16) | Capa 2, Etapa 1 | Etapa 1: el soporte de la plataforma de 2011 termina en 2029 y el gerente financiero objetó dejar lo financiero al final. Necesita F-03 y X-01, que van antes. Es una desviación documentada del orden del comité. |
| **F-02** Cartera, cobranza y repactaciones | Cuenta, saldo, cuotas, pagos, mora, cobranza y repactación | La cartera viva de 620.000 clientes con saldo. Es lo que se migra de la plataforma de 2011 (primera ola en Etapa 1 con los clientes al día; segunda en Etapa 2 con repactaciones, cobranza y juicios). No comparte saldos con R-09 | Capa 3, Etapa 1 (ola 1) y Etapa 2 (ola 2) | Etapa 1 (ola 1, cartera activa) y Etapa 2 (ola 2, cartera cerrada o castigada): migrar 620.000 clientes necesita más de una marcha blanca para conciliarse y debe terminar antes de enero de 2029. Necesita F-03. |
| **F-03** Consentimiento y evidencia financiera | Versión de la información precontractual entregada, aceptación, consentimiento y expediente recuperable | Es la prueba ante la autoridad de que se informó y se aceptó. Retención de la evidencia por el plazo del crédito más 6 años | Capa 1, Etapa 1 | Etapa 1: es dependencia técnica de F-01 y F-02 (versión precontractual y evidencia de repactación), por lo que no puede quedar al final. |

## Frontera (X)

| Servicio | Qué es | Conexión con el negocio | Capa y etapa | Por qué esta etapa |
| :-- | :-- | :-- | :-- | :-- |
| **X-01** Autorización y auditoría de cruces Retail–Emisor | El único paso permitido para que un negocio use datos del otro, con finalidad declarada, dato mínimo y registro de cada cruce. Deniega por omisión | Hace cumplir la línea roja del Caso. Ejemplo: Marketing no ve saldos del Emisor. Custodia: control interno, cumplimiento y auditoría | Capa 1, Etapa 1 | Etapa 1: la objeción del Caso exige la frontera de datos antes de cualquier servicio que cruce datos. Es base de F-01, F-02 y R-09. |

## Qué NO es ninguno de estos servicios

- No reemplazan el ERP/DTE (único emisor tributario), el marketplace ni el WMS principal (EXC-01, EXC-12): los integran.
- Los servicios son los 13 comprometidos; implementarlos como uno o varios microservicios es decisión posterior y no agrega códigos.
- La plataforma de integración (1.14), la identidad y la observabilidad no son R, F ni X: son la base común (capa 0).
- Los nombres de los 13 servicios se usan como "Servicio de … (R-0x/F-0x/X-01) en producción" en los entregables.

## Correcciones respecto de lo dicho antes en la conversación

- R-09 es **Clientes y fidelización Retail**, no una "vista del cliente".
- F-02 **no** comparte saldos con R-09. Está prohibido (sección 6 de `descripcion_alcance_producto.md`).
- X-01 no es la vista unificada de cliente: es el control de autorización y auditoría de los cruces que debe existir antes de construir cualquier vista unificada (Caso 13.1, objeción de la contralora, y 13.3.7). Por eso "X-01 antes de cualquier vista unificada" era una formulación correcta; una corrección anterior de esta guía la dio por errónea y se restituye.
