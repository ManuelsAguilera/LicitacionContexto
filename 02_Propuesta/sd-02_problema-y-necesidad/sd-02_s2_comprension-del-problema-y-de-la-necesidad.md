---
id: T7-02-2.2
tipo: seccion
parte: T7-02
titulo: Comprensión del problema y de la necesidad
estado: borrador
bases: []
requisitos: []
depende_de: []
adjuntos: []
jira: []
cifras: []
origen: "Informes(5).md#bloques-3,4,5,6,7"
actualizado: 2026-10-02
---
# 2.2 Comprensión del problema y de la necesidad



<!-- contenido migrado desde la fuente; permanece en borrador y requiere revisión humana -->



<!-- origen: Informes(5).md | bloque 3 -->

Esta sección profundiza en las condiciones propias de la industria y de la operación que explican el problema presentado anteriormente. Para ello, se consideran las características del modelo omnicanal, la convivencia entre el retail y el negocio financiero, el marco regulatorio aplicable y la estacionalidad del comercio, sin abordar todavía el dimensionamiento detallado del problema ni las decisiones asociadas a su solución.

<!-- origen: Informes(5).md | bloque 4 -->

### Contexto de la industria

La operación de Multitiendas Ancoa S.A. combina una red tiendas físicas con un alcance a nivel nacional con canales digitales y un marketplace de terceros. A esta actividad se suma el negocio financiero, desarrollado mediante una filial emisora de tarjeta de casa comercial. De esta forma, Ancoa participa simultáneamente en la industria del comercio minorista y en el sector financiero, actividades que se relacionan directamente en el punto de venta y frente a un mismo cliente.

La compañía mantiene 22 tiendas distribuidas en 11 regiones, de las cuales 14 funcionan dentro de centros comerciales y ocho corresponden a tiendas con acceso a la calle. En conjunto, estas instalaciones suman 96.000 m² de superficie de venta y presentan condiciones operativas distintas entre sí, desde la tienda insignia ubicada en Santiago hasta establecimientos más pequeños y aislados, como el ubicado en Coyhaique, que presentan restricciones de conectividad y abastecimiento.

El funcionamiento físico de la tienda se complementa con el canal en línea y el marketplace. Su canal digital representa un 19% de las ventas y procesa aproximadamente 1,9 millones de pedidos al año. A la vez, cerca del 71% de las referencias del catálogo corresponden a vendedores externos del marketplace, mientras que el 29% restante corresponde a referencias del catálogo propio. Esto implica que Ancoa no se limita al modelo tradicional de compra y venta en el local, sino que debe coordinar productos, inventario y atención al cliente entre canales propios y de terceros.

Como referencia del sector, la Cámara de Comercio de Santiago estimó que durante 2025 el comercio electrónico representó un 12,6% de las ventas del comercio minorista en Chile y un 16,1% en el caso de las tiendas por departamento. Además, las ventas online crecieron un 11,6% nominal durante ese año. En este contexto, la participación digital de Ancoa, equivalente al 19% de sus ventas, se encuentra por sobre la referencia informada para las tiendas por departamento y confirma que el canal digital tiene un peso relevante dentro de su operación (Cámara de Comercio de Santiago \[CCS\], 2026a).

Las tiendas tampoco se limitan a participar en la venta presencial. Un 41% de los pedidos en línea son retirados en tienda, y también despachan a un 17% de estos. Por esto parte de la infraestructura y del personal de sala participa directamente en el cumplimiento de los pedidos digitales. Las mesas de atención también realizan los cambios, devoluciones y reciben los reclamos de distintos canales. Es por esto que la tienda física, el canal digital y el marketplace funcionan mediante procesos que ocupan, en cierto grado, la misma infraestructura y personal.

<!-- origen: Informes(5).md | bloque 5 -->

### Particularidades operacionales

La principal particularidad del funcionamiento de Ancoa es que las actividades de los sectores de retail y financiero coinciden en el mismo entorno operacional. El negocio financiero funciona mediante una filial distinta, pero comparte con el retail la marca, el cliente y parte de los puntos de atención. Durante una visita a la tienda, la misma persona puede comprar un producto, pagar con su tarjeta propia y realizar gestiones relacionadas al crédito. Es por esta convivencia que procesos de ambos negocios se pueden realizar frente al mismo cliente, y en algunos casos por el mismo personal.

A esto se suma la naturaleza fragmentada del entorno tecnológico. El negocio funciona gracias a nueve plataformas de seis proveedores, conectadas mediante catorce interfaces punto a punto a lo largo de quince años. Varias de estas plataformas comparten información mediante procesos nocturnos, y Ancoa no cuenta con un mapa completo de todas las conexiones entre sistemas. Esto implica que la información utilizada por el negocio puede encontrarse distribuida entre distintas plataformas, y no actualizarse al mismo tiempo.

Otra condición sensible es la relación entre el retail y la filial financiera. Ambos comparten centros de datos, red y equipos de tecnologías de la información, mientras que su separación lógica está implementada de manera parcial, y no completamente documentada. Por lo tanto, aunque comparte la infraestructura tecnológica, la información de ambos negocios no puede tratarse sin hacer la distinción necesaria.

La fuerza laboral también condiciona la forma en que se ejecutan los procesos. La compañía cuenta con 3.820 vendedores de piso y cajeros, cuya remuneración posee un componente variable asociado a comisiones y cuya rotación anual alcanza el 62%. La comisión aumenta cuando una venta se paga mediante la tarjeta propia, por lo que el tiempo requerido para completar los procesos comerciales y financieros forma parte de las condiciones habituales de trabajo del vendedor.

En las salas de venta trabajan aproximadamente 1.100 repositores que están contratados por proveedores externos, y no tienen relación laboral directa con Ancoa. A esto se suma que los vendedores comparten 640 terminales móviles para consultar la existencia de productos, las cuales están distribuidas de forma desigual entre las tiendas. Estas condiciones deben considerarse para comprender una operación en la que interactúan personal propio, personal externo, equipos compartidos y procesos presenciales y digitales.

<!-- origen: Informes(5).md | bloque 6 -->

### Particularidades regulatorias

La coexistencia de ambos dominios hace que Ancoa se rige por regímenes jurídicos de distinta naturaleza.

En lo que respecta al dominio del retail,  materia de protección al consumidor, la Ley N.º 19.496 establece obligaciones relacionadas con la información proporcionada al cliente y los precios de los bienes y servicios. Su artículo 30 exige que el precio sea informado de forma claramente visible antes de perfeccionarse el acto de consumo y contempla también la oferta de productos realizada mediante sitios de Internet (Ley N.º 19.496, 1997). Esto es relevante en una operación donde un mismo producto puede tener un precio registrado centralmente, uno publicado en el canal digital y una etiqueta física exhibida en tienda.

Por otro lado y dentro del mismo dominio, el canal digital está sujeto al decreto N°6 del 2021, Reglamento del comercio electrónico. Esta normativa establece los deberes de información en las ventas realizadas mediante medios digitales y distingue las obligaciones de los vendedores y operadores de las plataformas electrónicas. (Decreto N.º 6, 2021\)

En particular, el reglamento exige informar aspectos como el costo total de la compra, la inexistencia de stock, los plazos de despacho o retiro y los canales de contacto para consultas, cambios o devoluciones. Estas obligaciones resultan especialmente relevantes en operaciones que combinan comercio electrónico, retiro en tienda y marketplace (Servicio Nacional del Consumidor \[SERNAC\], 2022).

La filial financiera se encuentra bajo un marco distinto para cada una de sus áreas. Por un lado los emisores de tarjetas de crédito no bancarias forman parte de las entidades reguladas y supervisadas por la Comisión para el Mercado Financiero, mientras que las operaciones de crédito de dinero se encuentran reguladas por la Ley N.º 18.010 (Ley N.º 18.010, 1981). Por lo que, procesos como la originación, modificación de condiciones, repactación y cobranza poseen exigencias distintas a las de una venta de retail.

La diferencia entre ambos dominios también trae consigo responsabilidades distintas respecto al tratamiento de la información. La empresa tiene interés en utilizar los antecedentes de sus clientes del dominio de retail para análisis y campañas, mientras que la información del dominio de la filial ha sido utilizada para finalidades asociadas al crédito. El cruce de información entre ambos ámbitos requiere determinar previamente qué datos pueden utilizarse, con qué finalidad y bajo qué fundamento.

Durante el horizonte del proyecto también deberá considerarse la Ley N.º 21.719, que regula la protección y el tratamiento de los datos personales y crea la Agencia de Protección de Datos Personales. La norma fue publicada el 13 de diciembre de 2024 y su entrada en vigencia está fijada para el 1 de diciembre de 2026 (Ley N.º 21.719, 2024). Esto es especialmente relevante por la cantidad y diversidad de información de clientes procesada entre los canales comerciales y el negocio financiero.

Por estas razones, una interacción con un cliente está sujeta a restricciones distintas dependiendo del ámbito del negocio con el que esté interactuando. La particularidad regulatoria de Ancoa radica en que estas actividades están estrechamente relacionadas en la operación diaria, aunque no se encuentran sometidas a un único régimen jurídico.

<!-- origen: Informes(5).md | bloque 7 -->

### Particularidades estacionales

Durante el transcurso del año hay períodos en que la demanda aumenta a niveles considerablemente distintos del régimen normal. Entre el 1 de noviembre y el 6 de enero se desarrolla la campaña de navidad, y la posterior liquidación de enero, lo que corresponde al nivel de demanda más alto de las ventas. Durante esta etapa, la dotación aumenta desde aproximadamente 6.400 hasta 8.300 trabajadores mediante la incorporación de cerca de 1.900 personas de temporada.

También existen otros períodos de mayor actividad durante el año. La temporada de vuelta a clases se extiende aproximadamente desde la última semana de enero hasta la primera semana de marzo y concentra la demanda en determinadas categorías. A esto se suma el Día de la Madre durante mayo y otros eventos comerciales de descuentos. Estas variaciones afectan de forma distinta a las categorías de productos y a los canales de venta, por lo que la carga operacional no se distribuye uniformemente durante el año.

En la industria chilena, algunos de los principales eventos promocionales poseen fechas definidas externamente a cada retailer. CyberDay y CyberMonday son organizados por el Comité de Comercio Electrónico de la Cámara de Comercio de Santiago, entidad que anuncia las fechas correspondientes a cada edición. En 2026, CyberDay se realizó entre el 1 y el 3 de junio, mientras que CyberMonday fue fijado entre el 5 y el 7 de octubre (CCS, 2026b, 2026c).

La CCS también organiza una versión oficial de Black Friday. Por ejemplo, la edición de 2025 se realizó entre el 28 de noviembre y el 1 de diciembre. La propia Cámara distingue esta versión oficial de otras iniciativas comerciales que utilizan la denominación Black Friday sin encontrarse vinculadas al gremio (CCS, 2025). Por lo tanto, para los retailers participantes estos eventos constituyen hitos externos del calendario comercial a los que deben adaptar previamente su capacidad operativa, logística y tecnológica.

El principal peak del canal digital corresponde al evento anual de comercio electrónico desarrollado entre mayo y junio. Durante tres días, el canal procesa un volumen equivalente a aproximadamente 22 días de venta normal en línea. Esta concentración afecta simultáneamente al canal digital, los centros de distribución, las tiendas que preparan pedidos, los puntos de retiro y la capacidad de despacho.

La estacionalidad, por lo tanto, no corresponde únicamente a un aumento temporal de las ventas. Los períodos de mayor demanda modifican la dotación disponible, el volumen de pedidos, la utilización de las tiendas como puntos logísticos y la carga sobre los sistemas que sostienen la operación. Estas condiciones permiten comprender el entorno en que se manifiesta el problema, mientras que sus efectos cuantitativos específicos se desarrollarán posteriormente en el dimensionamiento.
