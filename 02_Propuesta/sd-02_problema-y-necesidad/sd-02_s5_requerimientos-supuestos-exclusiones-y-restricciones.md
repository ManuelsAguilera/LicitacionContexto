---
id: T7-02-2.5
tipo: seccion
parte: T7-02
titulo: "Resumen de Requerimientos, Supuestos, Exclusiones y Restricciones"
estado: borrador
bases: []
requisitos: []
depende_de: []
adjuntos: []
jira: []
cifras: []
origen: "Informes(5).md#bloques-18,19,20,21,22,23,24,25"
actualizado: 2026-10-02
---
# 2.5 Resumen de Requerimientos, Supuestos, Exclusiones y Restricciones



<!-- contenido migrado desde la fuente; permanece en borrador y requiere revisión humana -->



<!-- origen: Informes(5).md | bloque 18 -->

Esta sección resume y analiza lo que el cliente requiere, los supuestos que el equipo declara para interpretar la información disponible, con su respectivo fundamento, y las exclusiones y restricciones que impone el caso. Su propósito es dejar explícito, antes de describir la solución, qué se debe cumplir, que se da por supuesto y lo que queda fuera de la propuesta.

El detalle de cada elemento con su identificador individual, se encuentra en el archivo de anexos correspondiente a este subdocumento, contiene el listado de requerimientos, el listado de supuestos, exclusiones y restricciones y otros listados de apoyo.

<!-- origen: Informes(5).md | bloque 19 -->

### Resumen de requerimientos

Los requerimientos se obtuvieron en base a lo estipulado por el cliente, de modo que exprese una sola condición verificable. Se clasificaron en tres tipos, 223 requerimientos funcionales (RF), que describen lo que el sistema debe hacer, 75 requerimientos no funcionales (RFN), que fijan un umbral medible y su método de verificación, que corresponden a compromisos de la oferta y no a funciones del sistema por lo que no admiten caso de prueba d software.

La Tabla 2.1 resume su distribución por categoría.

Tabla 2.1:** Requerimientos del CLIENTE por tipo y categoría.

<!-- tabla dividida: extensa y multidimensional; se conservan sus dimensiones -->

**Tabla — bloque 1 de 3.**

| Tipo y categoría | N.º | Síntesis de lo que exige el CLIENTE |
| :--- | :--- | :--- |
| RF Pedidos y cumplimiento | 47 | Promesa de entrega confiable, elección del punto de despacho por costo total de servir, y retiro o despacho desde tienda. |
| RF  Inventario y disponibilidad | 38 | Cálculo centralizado del disponible para vender, conteo cíclico por clasificación ABC y clasificación obligatoria de la merma. |
| RF Crédito y cobranza | 28 | Evaluación y cupo en el punto de venta, evidencia del consentimiento y de la información precontractual, y migración de la cartera. |
| RF – Marketplace | 25 | Reglas de desempeño y sanciones para los vendedores externos, gestión de catálogo y devoluciones. |
| RF – Operación de tienda | 20 | Continuidad en modo desconectado: venta, cobro, promociones y documento de venta en contingencia. |
| RF – Precios y etiquetado | 16 | Coherencia entre el precio exhibido y el cobrado, y evidencia del precio publicado. |
| RF – Seguridad y accesos | 14 | Credenciales individuales, sin acceso anónimo ni credenciales compartidas. |
| RF – Gobernanza de datos | 12 | Separación de datos entre retail y filial financiera, finalidad declarada e inventario de interfaces. |
| RF – Devoluciones y garantía legal | 12 | Atención íntegra en el mesón, sin derivar al cliente, y decisión de aptitud antes de reingresar una unidad al stock. |
| RF – Evento de alta concurrencia | 10 | Degradación controlada de servicios y bloqueo de despliegues en las cinco ventanas de congelamiento. |

**Tabla — bloque 2 de 3.**

| Tipo y categoría | N.º | Síntesis de lo que exige el CLIENTE |
| :--- | :--- | :--- |
| RF – Ventas en tienda | 1 | Prioridad de la venta física sobre una reserva digital temporal. |
| **Subtotal RF** | **223** |  |
| RNF – Seguridad | 16 | Arquitectura segura, segmentación de red en las 22 tiendas, separación acreditada de la filial, tokenización de medios de pago y DevSecOps. |
| RNF – Desempeño y capacidad | 15 | Tiempos de respuesta (evaluación crediticia ≤ 8 s, confirmación de pedido ≤ 3 s, propagación de precios ≤ 5 min) y soporte del peak del evento anual. |
| RNF – Cumplimiento y auditabilidad | 13 | Plazos de conservación de la evidencia, base de licitud y registro de actividades de tratamiento de datos. |
| RNF – Disponibilidad y recuperabilidad | 11 | Operación sin enlace externo (≥ 8 h en tienda), recuperación ante desastres (RTO ≤ 4 h; RPO ≤ 15 min). |
| RNF – Operabilidad e interoperabilidad | 10 | Notificaciones y avisos oportunos al cliente, y estándares de intercambio con proveedores. |
| RNF – Migración, portabilidad y escalabilidad | 4 | Migración de 620.000 clientes con saldo sin pérdida, interrupción ni divergencias; apertura de tiendas por parametrización. |
| RNF – Efectividad de negocio | 3 | Metas sobre la línea base: cancelación \< 0,3 %, cumplimiento de entrega ≥ 97 % y diferencia de inventario \< 2 %. |
| RNF – Usabilidad | 2 | Operación con capacitación mínima y lenguaje claro en las comunicaciones del crédito. |

**Tabla — bloque 3 de 3.**

| Tipo y categoría | N.º | Síntesis de lo que exige el CLIENTE |
| :--- | :--- | :--- |
| RNF – Consistencia de datos | 1 | Mismo estado del pedido en todos los canales de consulta. |
| **Subtotal RNF** | **75** |  |
| OP – Obligaciones del proponente | 9 | Alternativa de etiquetas electrónicas, dispositivos móviles por tienda y análisis de hacer o comprar del CD de Concepción. |
| **Total** | **307** |  |

<!-- origen: Informes(5).md | bloque 20 -->

### Fuente: Elaboración propia a partir de EMPRESA-Subdocumento2-Anexos, Anexos A.1 a A.3.

La distribución muestra que el 62 % de los requerimientos funcionales (138 de 223\) se concentra en cuatro categorías: pedidos y cumplimiento, inventario y disponibilidad, crédito y cobranza, y marketplace. Esta concentración es coherente con el diagnóstico, porque esas categorías sostienen directamente tres de las cuatro promesas de Ancoa: que el producto existe, que la entrega llegará en la fecha informada y que las condiciones del crédito son aceptadas. La cuarta promesa, que el precio cobrado coincida con el exhibido, se aborda en la categoría de precios y etiquetado, que tiene menos requerimientos, pero un alto impacto regulatorio.

Los requerimientos no funcionales, por su parte, convierten el problema dimensionado en metas verificables. Tres de ellos fijan la mejora esperada respecto de la línea base: reducir la cancelación por falta de existencia a menos de 0,3 % anual, elevar el cumplimiento de la fecha de entrega desde 81 % a 97 % o más, y bajar la diferencia de inventario por categoría desde 12,4 % a menos de 2 %. Otros tres exigen que la migración de los 620.000 clientes con saldo se complete sin pérdida de datos, sin interrupción del cobro y sin divergencias de saldo antes de 2029\. Las obligaciones del proponente, en cambio, no describen funciones del sistema, sino entregables de la oferta, como el análisis de hacer o comprar del CD de Concepción.

A estos requerimientos se suman los 374 requisitos técnicos (RT) de las Bases. La relación entre cada requerimiento, el componente que lo satisface y la sección de la propuesta donde se desarrolla se presenta en la matriz de cumplimiento y trazabilidad del Anexo A.5.2.

<!-- origen: Informes(5).md | bloque 21 -->

### Resumen de supuestos

Cuando las Bases describen un problema, pero no definen la regla con la que debe resolverse, el equipo declara un supuesto. Se declararon 25 supuestos (SUP-01 a SUP-25), cada uno con su fundamento en los datos del caso o en la normativa aplicable. Se agrupan en seis temas:

●       **Inventario y disponibilidad (SUP-01, SUP-12, SUP-17, SUP-18 y SUP-20):** el disponible para vender se calcula de forma centralizada con un colchón de seguridad dinámico por categoría y tienda, las reservas del carro digital expiran, todo ajuste de inventario se clasifica según su causa y el CD de Concepción queda fuera del disponible mientras opere con planillas manuales.

●       **Precios (SUP-08 a SUP-10):** ante una discrepancia prevalece el precio exhibido más bajo, el precio nuevo se activa en caja solo cuando se confirma el cambio de etiqueta y el historial de precios publicados se conserva de forma inalterable.

●       **Pedidos y logística (SUP-11, SUP-13, SUP-14 y SUP-22):** ante un quiebre se ofrece sustitución, compra a terceros o entrega compensada antes de cobrar; el origen del despacho se elige por costo total de servir; la comisión se atribuye a la tienda que abastece el pedido; y el producto devuelto por retracto se inspecciona antes de reingresar al stock.

●       **Marketplace y postventa (SUP-15, SUP-16 y SUP-21):** las garantías y devoluciones se resuelven en el mesón sin derivar al cliente, y los 310 vendedores externos operan con reglas de desempeño y sanciones automatizadas.

●       **Crédito y datos personales (SUP-03 a SUP-07 y SUP-25):** identidad del cliente en dos capas, frontera de datos entre retail y filial cerrada por defecto, evidencia digital inalterable del consentimiento y de la hoja resumen, venta con crédito en modo desconectado contra un cupo preaprobado, y migración de la cartera por etapas con conciliación diaria y reversión.

●       **Tecnología y personas (SUP-02, SUP-19, SUP-23 y SUP-24):** transición gradual sin reemplazo «Big Bang», con el ERP como único emisor tributario; degradación escalonada en eventos de alta demanda; y accesos individuales con altas y bajas automáticas para el personal propio, temporal y externo.

En conjunto, los supuestos comparten un mismo criterio: tratar los registros actuales como imperfectos y exigir evidencia verificable de cada promesa. Los más sensibles para la propuesta son SUP-02, SUP-04 y SUP-25, porque condicionan la estrategia de transición, la separación entre ambos negocios y la migración de la cartera financiera; si alguno de ellos no se confirma, cambia el plan de implantación. El listado completo, con el enunciado y el fundamento de cada supuesto, se encuentra en el Anexo A.4.1.

<!-- origen: Informes(5).md | bloque 22 -->

### Resumen de exclusiones

Las exclusiones delimitan lo que la propuesta no asume, ya sea porque las Bases lo dejan fuera del alcance o porque la información disponible no permite sostenerlo. Se identificaron ocho exclusiones (EXC-01 a EXC-08), de dos tipos:

●       **De alcance (EXC-01 a EXC-06):** la adquisición de etiquetas electrónicas, que se especifica y costea por separado sin incluir su compra; el CD de Concepción como origen de la promesa de entrega mientras no acredite su sistema de gestión de almacenes; el reemplazo del ERP heredado como emisor tributario; la sustitución simultánea de las nueve plataformas actuales; la gestión laboral y la capacitación de los repositores externos; y cualquier flujo que derive al cliente a terceros en garantías o devoluciones.

●       **Del análisis (EXC-07 y EXC-08):** no se proyecta el 11 % de discrepancia de precios más allá de la muestra fiscalizada, ni se descompone la merma histórica entre pérdida física y error de registro, porque las Bases no entregan información suficiente para hacerlo.

Declarar estas exclusiones evita comprometer resultados que dependen de decisiones del CLIENTE o de información que hoy no existe. El detalle y el origen de cada exclusión se presentan en el Anexo A.4.2.

<!-- origen: Informes(5).md | bloque 23 -->

### Resumen de restricciones

Las restricciones son condiciones del caso que la solución no puede modificar y dentro de las cuales debe operar. Se identificaron 15 restricciones (RES-01 a RES-15), que la Tabla 2.2 agrupa por tipo junto con su efecto sobre la propuesta.

Tabla 2.2:** Síntesis de restricciones por tipo.

<!-- tabla conservada: compara múltiples dimensiones -->

| Tipo | Restricciones principales | Efecto en la propuesta |
| :--- | :--- | :--- |
| Regulatoria (RES-01 a RES-05) | Ley N.º 19.496; Decreto N.º 6 de 2021; Ley N.º 18.010 y fiscalización de la CMF; Ley N.º 21.719, vigente desde el 1 de diciembre de 2026; plazos de conservación de la evidencia. | Cada operación debe dejar evidencia verificable y respetar el régimen del negocio al que pertenece. El cruce de datos entre retail y filial queda cerrado por defecto. |
| Temporal (RES-06 a RES-08) | Fin del soporte de la plataforma de originación y cobranza, y último hito del plan de remediación, en 2029; cinco ventanas anuales de congelamiento; eventos comerciales con fechas fijadas externamente. | El plan de implantación debe calzar entre las ventanas de congelamiento y terminar la migración financiera antes de 2029\. |
| Tecnológica y de infraestructura (RES-09 a RES-11) | Nueve plataformas y catorce interfaces punto a punto sin mapa completo; infraestructura compartida con la filial; 14 tiendas dependientes del enlace del centro comercial y 13 sin segmentación de red. | La transición debe ser gradual, con operación desconectada en tienda y separación acreditada de la filial. |
| Migración (RES-12) | 620.000 clientes con saldo que deben migrarse sin pérdida de datos, interrupción del cobro ni divergencias de saldo. | Migración por etapas, con coexistencia de plataformas y conciliación diaria de saldos. |
| Humana y organizacional (RES-13 a RES-15) | 3.820 vendedores y cajeros con rotación anual del 62 %; 1.900 contrataciones de temporada; 640 terminales compartidos; 1.100 repositores externos; 46 profesionales de TI en el CLIENTE. | Interfaces operables con capacitación mínima, traspaso rápido de sesión en terminales compartidos y una carga de cambio acotada para el equipo del CLIENTE. |

<!-- origen: Informes(5).md | bloque 24 -->

### Fuente: Elaboración propia a partir de EMPRESA-Subdocumento2-Anexos, Anexo A.4.3.

El análisis de las restricciones muestra que el principal límite del proyecto no es tecnológico, sino regulatorio y temporal: la solución debe separar dos negocios que comparten cliente e infraestructura y, al mismo tiempo, migrar la cartera financiera antes de 2029 sin intervenir la operación durante las ventanas de congelamiento. El detalle de cada restricción y su origen se encuentra en el Anexo A.4.3.

<!-- origen: Informes(5).md | bloque 25 -->

### Otros listados

Como apoyo, el Anexo A.5 incluye dos listados adicionales: los indicadores con su línea base y la meta comprometida (Anexo A.5.1), que conectan el dimensionamiento de la sección 2.3 con los requerimientos no funcionales, y la matriz de cumplimiento y trazabilidad (Anexo A.5.2), que relaciona cada requerimiento con el componente que lo satisface y la sección de la propuesta donde se desarrolla.
