# Bases Técnicas — Caso 09: Cadena Multitienda

**Multitiendas Ancoa S.A. — cuatro promesas diarias sobre registros imprecisos**

*Licitación N° TFEP-01/2026 — Pontificia Universidad Católica de Valparaíso, Escuela de Informática*  
*Versión 1.0 — Fecha Documento: 18-08-2026*

---

| Asignatura | Taller de Formulación de Proyectos Informáticos — ICI-5444 |
| --- | --- |
| Unidad académica | Escuela de Informática, Pontificia Universidad Católica de Valparaíso |
| Profesor | Antonio Moya Villegas — antonio.moya@pucv.cl |
| Industria | Comercio minorista por departamentos, con marketplace de terceros y emisión de crédito propio |
| Mandante | Multitiendas Ancoa S.A. (empresa ficticia) |
| Operación | 22 tiendas en 11 regiones, 2 centros de distribución, 458.000 referencias, 31 millones de documentos de venta y 1.380.000 tarjetas emitidas |
| Condición especial | Es simultáneamente una tienda y un emisor de crédito fiscalizado. Dos negocios, dos regímenes 4 jurídicos, un mismo cliente 4 y un mismo y mostrador |
| Documentos que rigen | Bases Administrativas FEP01.26 y Bases Técnicas Transversales FEP02.26 |
| Duración del contrato | 56 meses: implementación en dos etapas y 36 meses de operación |
| Versión | 1.0 — agosto de 2026 |

> Este documento no es una especificación de requerimientos. Es la descripción de una operación real, con sus datos, sus dolores, sus contradicciones internas y sus vacíos. Identificar qué es funcional y qué no lo es, completar lo que falta con supuestos declarados y con reglas de negocio propias de la industria, investigar aquello que el documento no explica, y traducir todo ello en un alcance, una arquitectura, un plan y una estrategia de puesta en producción, es exactamente el trabajo que se está licitando y lo que será evaluado.

## Contenido

| Título | Contenido | Capítulos |
| --- | --- | --- |
| I · El mandante y el encargo | Cómo llegamos a esta licitación, la compañía, sus tiendas, sus cifras, sus personas y las zonas de la operación. | 1 – 3 |
| II · La operación tal como es hoy | Los ciclos del producto, del cliente y del crédito, los sistemas existentes, la conectividad y los indicadores del problema. | 4 – 7 |
| III · Lo que dicen quienes operan | Diez entrevistas de levantamiento, incluidas las de una vendedora de marketplace y una clienta, con sus contradicciones intactas. | 8 |
| IV · Lo que el mandante espera | Expectativas de negocio, restricciones no negociables, exclusiones, marco normativo y prioridades. | 9 – 13 |
| V · Antecedentes para el dimensionamiento | Volumetría entregada y volumetría a estimar, parámetros del caso y decisiones deliberadamente no resueltas. | 14 – 16 |
| VI · Lo que debe producir el proponente | El trabajo de traducción exigido, los criterios de aceptación y cómo se evaluará este caso. | 17 – 19 |
| VII · Anexos del caso | Mapa de sistemas y flujos actuales, calendario comercial y glosario de la industria. | A – C |

### Cómo leer este documento

Los Títulos I y II describen la operación. Se entregan con detalle porque de ellos dependen todas las decisiones de diseño: no hay atajo que permita saltarlos.

El Título III recoge las voces de quienes operan y también las de dos personas que no trabajan en la compañía: una vendedora de marketplace y una clienta cuyo pedido fue cancelado. No están de acuerdo entre sí, y esa discrepancia es información, no ruido: revela dónde el proyecto va a encontrar resistencia y qué tensiones habrá que arbitrar.

El Título IV expresa lo que el mandante espera, deliberadamente en lenguaje de negocio y no de requerimientos. El Título V entrega los datos duros que la compañía conoce, señala cuáles debe estimar el proponente, fija los parámetros de los requisitos que las Bases Técnicas Transversales dejaron abiertos al caso, y enumera veinticinco decisiones que el cliente no ha tomado.

El Título VI describe el trabajo exigido y los criterios con que se juzgará. Conviene leerlo primero y volver a él al final.

> Tres particularidades de este caso. La primera es que el mandante es dos negocios con dos regímenes jurídicos bajo el mismo techo: una tienda y un emisor de crédito fiscalizado. Comparten el cliente, el mostrador, el vendedor y la marca, pero no comparten las obligaciones ni pueden compartir libremente los datos. Toda decisión de arquitectura de este caso tropieza tarde o temprano con esa frontera, y el directorio la declaró línea roja. La segunda es que aquí no hay un sistema legado: hay nueve plataformas de seis proveedores y quince años, unidas por catorce interfaces punto a punto que corren de noche y cuyo mapa completo no posee nadie en la compañía. Levantar ese mapa es parte del trabajo, no una entrega previa del cliente. La tercera es que la compañía hace cuatro promesas cada día —que el producto existe, que el precio es el exhibido, que la entrega llega en la fecha ofrecida y que las condiciones del crédito son las informadas— y las cuatro se apoyan en registros que ella misma sabe imprecisos. El objeto de este proyecto no es corregir esos registros, que tomará años, sino permitir que la compañía haga promesas que pueda cumplir y, sobre todo, acreditar.

# Título I. El mandante y el encargo

## Capítulo 1. CÓMO LLEGAMOS A ESTA LICITACIÓN

El evento de comercio electrónico de junio de 2026 fue el mejor de la historia de la compañía durante treinta y dos horas.

En tres días se recibieron ciento cuatro mil pedidos, casi el doble del año anterior. El sitio no se cayó. El equipo de canales digitales celebró el martes por la noche.

El problema empezó el jueves, cuando la operación intentó preparar los pedidos.

Dos mil ochocientos cuarenta pedidos no se pudieron cumplir. El sistema decía que había existencia y no la había: unidades que figuraban en una tienda y no aparecieron, unidades dañadas que nadie había dado de baja, unidades que estaban en el probador de la tienda de Antofagasta desde marzo.

Se cancelaron todos. Muchos eran productos comprados a precio de campaña, que ya no existía. La compañía ofreció devolución y un cupón; casi nadie lo consideró suficiente.

En las tres semanas siguientes se recibieron mil novecientos reclamos formales y la autoridad de protección del consumidor abrió un procedimiento.

«Vendimos dos mil ochocientas cuarenta veces algo que no teníamos», dijo Amparo Ganderats Vial, gerenta general, en el directorio del 30 de junio. «Y quiero que quede claro que nadie mintió. El sistema decía que estaba. Nuestro problema es que el sistema dice cosas que no son ciertas, y llevamos años tomando decisiones sobre eso.»

Sobre la mesa había un dato interno que hasta entonces se veía como un asunto de bodega: el conteo cíclico encuentra diferencias en el doce coma cuatro por ciento de las referencias que audita.

Cuatro meses antes había llegado algo más pequeño y más incómodo.

Una fiscalización de la autoridad del consumidor revisó ciento veinte productos en cuatro tiendas y encontró que en el once por ciento de los casos el precio cobrado en caja no era el precio exhibido en la sala. Ninguna diferencia era grande. Todas eran infracciones.

La explicación es prosaica: los precios se cambian centralmente, y en campaña se cambian varias veces al día. Las etiquetas físicas las reemplaza el personal de la tienda, de noche, con una lista impresa que se genera al cierre. Cuando un precio cambia a las once de la mañana, la etiqueta queda mal hasta la noche siguiente. Nadie en la compañía sabe, en un momento dado, cuántas etiquetas están equivocadas.

Y en mayo llegó lo que en el comité de cumplimiento se trató a puerta cerrada.

Una revisión interna del negocio financiero encontró mil doscientos cuarenta repactaciones de deuda del ejercicio 2025 respecto de las cuales la compañía no puede acreditar el consentimiento del cliente a las nuevas condiciones. No hubo fraude. Las repactaciones se ofrecen por teléfono, el cliente acepta verbalmente y la llamada se graba. El problema es que las grabaciones se conservan noventa días y las revisiones ocurren después.

«Que no haya habido mala fe no me sirve de nada», dijo Cecilia Bordalí Ruz, contralora, en ese comité. «En este negocio, un consentimiento que no se puede acreditar es un consentimiento que no existe. Y esta industria ya tuvo una vez ese problema en Chile, y todos sabemos cómo terminó.»

La autoridad fiscalizadora del mercado financiero instruyó un plan de remediación con hitos verificables. El último vence en 2029, que es también el año en que el proveedor de la plataforma de originación y cobranza —en operación desde 2011— anunció el fin de su soporte.

El directorio aprobó licitar el proyecto. En el acta quedó consignada una condición que la contralora pidió incorporar textualmente: «esta compañía es al mismo tiempo una tienda y un emisor de crédito fiscalizado. Ninguna solución que trate esos dos negocios como si fueran uno solo, o que borre la separación entre sus datos, será aceptada, por buena que sea comercialmente».

> Este documento es el resultado de siete meses de levantamiento en las veintidós tiendas, en los dos centros de distribución, en las cajas, en el mesón de crédito y en la casa matriz, en temporada baja y durante el evento de junio, y de cuarenta y una entrevistas. No es una especificación. Es la descripción, lo más honesta que el CLIENTE ha sido capaz de hacer, de una operación real con sus datos, sus dolores, sus contradicciones internas y sus vacíos. Traducir esto en requerimientos es el trabajo del PROPONENTE, y es precisamente lo que se evalúa.

## Capítulo 2. LA COMPAÑÍA

### 2.1 Identificación

| Antecedente | Detalle |
| --- | --- |
| Razón social | Multitiendas Ancoa S.A. |
| Giro | Comercio al por menor en tiendas por departamento: vestuario, calzado, electrohogar, línea blanca, deco, juguetería y belleza. Intermediación de venta de terceros. Emisión y administración de una tarjeta de crédito de casa comercial. |
| Condición | Sociedad anónima cerrada. El negocio financiero se desarrolla a través de una filial emisora. sujeta: a la fiscalización alisios de la autoridad. del mercado financiero.. |
| Cobertura | 22 tiendas en 11 regiones, 2 centros de distribución y canal en línea con cobertura nacional. |
| Inicio de operaciones | 1972. Apertura del canal en línea en 2019 y del marketplace de terceros en 2022. |
| Ingresos consolidados | $ 474.000 millones. |
| Estructura del ingreso | Retail propio 87 %, negocio financiero 10 %, comisiones de marketplace 3 %. La tarjeta propia participa en el 38 % de las ventas de las tiendas. |
| Propiedad | Sociedad anónima cerrada. 54 % de un grupo familiar controlador; 46 % distribuido entre tres fondos de inversión. |

> Esta compañía es dos negocios bajo un mismo techo y con un mismo cliente. Vende mercadería, con las obligaciones de cualquier comercio, y emite crédito, con las obligaciones de un actor fiscalizado del mercado financiero. Los dos comparten a la persona, comparten el punto de venta, comparten al vendedor y comparten la marca, pero no comparten el régimen jurídico ni pueden compartir libremente los datos. Toda decisión de arquitectura de este caso tropieza tarde o temprano con esa frontera.

### 2.2 Las tiendas

| Formato | Cantidad | Detalle |
| --- | --- | --- |
| Tiendas en centros comerciales | 14 | Horario, acceso del público, estacionamiento y parte de la conectividad dependen del administrador del centro comercial. a |
| Tiendas a la calle | 8 | En ciudades regionales. Horario propio, acceso propio y enlace propio. 4 Incluyen los dos locales más antiguos de la cadena. |
| Tienda insignia | 1, en Santiago | 14.000 m² en cinco pisos. Concentra el 17 % de la venta presencial y es la única con mesón dedicado del negocio financiero en cada piso. |
| Tienda más LE pequeña | 1, en Coyhaique | 1.800 m². Enlace único sin respaldo y la logística de abastecimiento más larga de la cadena. |
| Superficie total de sala de venta | 96.000 m² | Distribuida en departamentos con dotación, metas y comisiones propias. |
| Centro de distribución principal | 1, Región Metropolitana | 42.000 m². Opera con sistema de gestión de almacenes desde 2016. |
| Centro de distribución secundario | 1, Concepción | 9.000 m². Abierto en 2023 para abastecer el sur. Opera con planillas de cálculo. |

### 2.3 Cifras de la operación

| Indicador | Valor |
| --- | --- |
| Referencias activas propias | 268.000, con explosión por talla, color y temporada |
| Referencias de vendedores de marketplace | 190.000 |
| Proveedores propios | 940 |
| Vendedores de marketplace | 310 |
| Documentos de venta emitidos al año | ≈ 31.000.000 |
| Pedidos del canal en línea al año | ≈ 1.900.000 |
| Participación del canal en línea en la venta | 19 %, en crecimiento |
| Pedidos que se retiran en tienda | 41 % del canal en línea |
| Pedidos que se despachan desde una tienda | 17 % del canal en línea |
| Devoluciones | 9 % en el canal en línea; 3 % en el presencial |
| Tarjetas emitidas | 1.380.000, de las cuales 620.000 con saldo vigente |
| Stock de colocaciones de la tarjeta | $ 186.000 millones |
| Participación de la tarjeta propia en la venta de tiendas | 38% |
| Merma o pérdida desconocida | 1,9 % de la venta, equivalente a $ 7.800 millones al año |

| indicador | Valor |
| --- | --- |
| Diferencias detectadas en el conteo cíclico de inventario | 12,4 % de las referencias auditadas |
| Evento de comercio electrónico de junio | En 3 días se procesa el equivalente a 22 días de venta en línea normal |

### 2.4 Las personas

| Categoría | Dotación | Régimen |
| --- | --- | --- |
| Personal propio | ≈ 6,400, hasta 8.300 en peak de noviembre y diciembre | La diferencia son 1.900 personas de temporada. |
| Vendedores de piso y cajeros | 3.820 | Remuneración con componente variable por comisión. Rotación anual del 62 %. Son quienes ofrecen la tarjeta y quienes entregan la información del crédito. |
| Reposición y bodega de tienda | 780 | Turnos que incluyen trabajo nocturno para reposición y cambio de etiquetas. |
| Centros de distribución | 620 | Turnos. 520 en el centro principal y 100 en Concepción. |
| Jefaturas de tienda y de departamento | 240 | Responsables de la operación de sala y de las metas de su departamento. |
| Prevención de pérdidas | 180 | Control de sala, auditoría de inventario e investigación de merma. |
| Negocio financiero | 320 | Originación, servicio al cliente, cobranza y control interno de la filial emisora. |
| Comercial y compras | 140 | Definen surtido, precios y campañas para 268.000 referencias. |
| Logística y planificación de abastecimiento | 90 | Reposición a tiendas y planificación de temporada. |
| Marketing y canales digitales | 60 | Sitio, aplicación, marketplace y fidelización. |
| Administración y finanzas | 110 | Jornada ordinaria. |
| Área de tecnologías de información | 46 | Distribuidas en cuatro equipos que mantienen nueve plataformas distintas. |
| Repositores externos de proveedores | ≈ 1.100 personas | Trabajan en la sala de venta sin ser trabajadores de la compañía. Ordenan, reponen y montan la exhibición de sus propias marcas. |

> Dos particularidades de la dotación condicionan todo el diseño. La primera es que el vendedor de piso trabaja con comisión: su ingreso depende de cerrar la venta y aumenta cuando la venta se paga con la tarjeta propia. Cualquier requerimiento que le agregue tiempo o que le reste venta competirá con su remuneración, y esa competencia la gana la remuneración. La segunda es que hay aproximadamente mil cien personas trabajando en la sala de venta que no son trabajadores de la compañía y sobre las cuales la compañía no puede imponer herramientas ni capacitación por la vía laboral.

## Capítulo 3. LAS ZONAS DE LA OPERACIÓN

Una tienda por departamento es varios negocios sucediendo en el mismo piso: un local de vestuario, uno de electrohogar, una sucursal financiera, un punto de retiro de compras en línea y una bodega. Cada uno tiene su propio cliente, su propio ritmo y sus propias reglas.

| Zona | Qué ocurre allí | Condiciones relevantes |
| --- | --- | --- |
| Sala de venta por departamento | Exhibición, atención y venta asistida por vendedores con comisión. | 96.000 m² en 22 tiendas, con precio exhibido en etiqueta física que se actualiza de noche con una lista impresa. |
| Probadores | Prueba de vestuario y calzado. | Punto ciego del inventario: unidades que entran y no siempre vuelven a su ubicación ni al registro. |
| Líneas de caja | Cobro, emisión del documento y aplicación de promociones. | Peak concentrado en tardes de fin de semana y en campaña. Es donde se detecta la diferencia entre precio exhibido y precio cobrado. |
| Mesón del negocio financiero | Originación de la tarjeta, entrega de información del crédito, repactaciones y atención de deudores. | Actividad de un emisor fiscalizado ocurriendo dentro de una tienda, con obligaciones de información y de acreditación propias. |
| Mesón de atención al cliente | Cambios, devoluciones, garantía legal y reclamos, incluidos los de productos de terceros. | Recibe devoluciones de todos los canales y de productos que la compañía no vendió sino que intermedió. |
| Zona de retiro de compras en línea | Entrega de pedidos comprados en el canal digital. | 41 % de los pedidos en línea. Compite por espacio y por personal con la operación de sala. |
| Bodega de tienda y andén | Recepción de mercadería, almacenamiento de respaldo y preparación de despachos desde tienda. | Es el origen físico del 17 % de los pedidos en línea, con personal que no fue contratado para preparar pedidos. |
| Oficina de prevención de pérdidas | Control de sala, videovigilancia, conteo cíclico e investigación de merma. | 180 personas para una merma de $ 7.800 millones al año, de la cual no se conoce qué parte es pérdida física y qué parte es error de registro. |
| Centro de distribución principal | Recepción, almacenamiento, preparación y despacho a las 22 tiendas y al canal en línea. | 42.000 m² con sistema de gestión de almacenes desde 2016. |
| Centro de distribución de Concepción | Abastecimiento del sur, abierto en 2023. | 9.000 m² operados con planillas de cálculo. No tiene sistema de gestión de almacenes. |
| Casa matriz | Comercial, precios, campañas, logística, marketing, negocio financiero, cumplimiento y tecnologías de información. | Donde se define el precio de 268.000 referencias y donde conviven las dos naturalezas de la compañía. |

# Título II. La operación tal como es hoy

## Capítulo 4. LOS TRES CICLOS: EL PRODUCTO, EL CLIENTE Y EL CRÉDITO

Lo que sigue es la descripción del proceso tal como ocurre, no como debería ocurrir. Se entrega con este nivel de detalle porque de él dependen las decisiones de alcance, de arquitectura y de trazabilidad que el PROPONENTE deberá tomar.

En esta compañía conviven tres ciclos. El del producto, que empieza en una orden de compra a un proveedor y termina cuando alguien se lo lleva o lo devuelve. El del cliente, que empieza cuando entra a la tienda o al sitio y termina cuando queda satisfecho o reclama. Y el del crédito, que empieza cuando esa misma persona firma en el mesón y puede durar treinta y seis meses después de que el producto dejó de existir.

Los tres se cruzan en el mismo mostrador y con la misma persona, y están regidos por reglas distintas.

### 4.1 El surtido, el maestro de artículos y la temporada

El área comercial define el surtido de cada temporada. Doscientas sesenta y ocho mil referencias activas propias, que en vestuario y calzado se multiplican por talla y color, y que rotan completamente dos veces al año.

Cada referencia se crea en el maestro de artículos del sistema central. La calidad de esa creación —atributos, categoría, dimensiones, si es frágil, si es voluminoso, si tiene restricción de despacho— determina después si el producto se puede vender en línea, cómo se despacha y cuánto cuesta enviarlo.

Nadie audita esa calidad. Canales digitales estima que un porcentaje relevante de las referencias no tiene atributos suficientes para publicarse bien, y las completa a mano cuando alcanza.

### 4.2 El precio, la promoción y la etiqueta

El precio de las doscientas sesenta y ocho mil referencias lo define comercial y se carga centralmente. En temporada normal cambia una o dos veces por semana. En campaña puede cambiar varias veces al día.

El precio viaja desde el sistema central a las cajas y al canal digital. A las etiquetas físicas de la sala no viaja: al cierre del día se imprime la lista de los precios que cambiaron y el personal de reposición las reemplaza de noche.

Eso significa que un precio que cambia a las once de la mañana queda mal exhibido durante el resto del día.

La fiscalización de febrero revisó ciento veinte productos en cuatro tiendas y encontró once por ciento de discrepancia entre el precio exhibido y el precio cobrado. La compañía no puede estimar cuántas etiquetas están equivocadas en un momento cualquiera, porque no existe ningún registro de qué etiqueta se cambió, cuándo ni quién.

Tampoco existe un registro histórico consultable de qué precio estaba publicado en cada canal en un instante determinado. Cuando un cliente reclama que el sitio mostraba otro precio, la compañía no tiene con qué contestarle, ni a favor ni en contra.

### 4.3 El abastecimiento y la reposición a tiendas

La mercadería llega al centro de distribución principal, se recibe, se almacena y se distribuye a las veintidós tiendas según una propuesta de reposición que calcula el área de planificación.

Esa propuesta se calcula con el inventario que registra el sistema. Como el registro tiene error, la reposición reparte mal: hay tiendas que reciben lo que ya tenían y tiendas que quedan sin lo que necesitaban.

El centro de distribución de Concepción, abierto en 2023 para acortar el abastecimiento del sur, opera con planillas: la ubicación de la mercadería la conocen las personas que trabajan allí.

### 4.4 El inventario, y por qué no es cierto

Éste es el problema de fondo de la compañía y conviene enunciarlo sin adornos: el registro de inventario está equivocado, se sabe que está equivocado, y se sabe aproximadamente cuánto.

El conteo cíclico —el recuento periódico de una muestra de referencias— encuentra diferencia en el doce coma cuatro por ciento de lo que audita. Las causas son varias y conocidas: unidades sustraídas, unidades dañadas que nunca se dieron de baja, unidades mal recibidas, unidades mal ubicadas, unidades que quedaron en un probador, devoluciones mal reintegradas y errores de digitación.

Lo que no se conoce es la proporción. La compañía llama a todo eso «merma» y lo cuantifica en un uno coma nueve por ciento de la venta, siete mil ochocientos millones de pesos al año. Prevención de pérdidas sostiene que una parte importante no es pérdida física sino error administrativo, y que se está investigando como robo algo que en buena medida es un problema de registro. No hay forma de demostrarlo con los datos actuales.

Durante años esto fue un asunto de bodega. Dejó de serlo cuando la compañía empezó a vender en línea, porque el canal digital publica y compromete existencia contra ese registro.

### 4.5 La venta en sala

El vendedor de piso atiende, recomienda, busca la talla, y cierra la venta. Su remuneración tiene un componente variable por comisión, y esa comisión es mayor cuando la venta se paga con la tarjeta propia.

Cuando el producto no está en su tienda, el vendedor consulta si hay en otra. El sistema le muestra el mismo registro que se sabe errado, de modo que «te lo traigo de Rancagua» es una promesa que a veces no se cumple.

En caja se cobra, se aplican las promociones vigentes y se emite el documento. Si el cliente paga con la tarjeta propia y no tiene cupo suficiente, se ofrece ampliarlo, lo que abre una operación de crédito en medio de una fila.

### 4.6 El pedido en línea y su cumplimiento

El canal en línea es el diecinueve por ciento de la venta y crece. Publica el catálogo propio y el de los vendedores de marketplace, muestra disponibilidad y acepta el pedido.

La disponibilidad que muestra se calcula sumando el inventario registrado del centro de distribución y el de las veintidós tiendas, con un descuento fijo de seguridad que alguien definió en 2019 y que nadie ha revisado desde entonces.

Cuando un pedido se acepta, se asigna a un punto de despacho y alguien va a buscar la unidad. Si no está, se busca en otro punto. Si no está en ninguno, el pedido se cancela.

El uno coma nueve por ciento de los pedidos en línea del año se canceló por falta de existencia. En el evento de junio esa cifra fue del dos coma siete por ciento sobre un volumen siete veces mayor, que en unidades absolutas fueron dos mil ochocientos cuarenta pedidos en tres días.

El tiempo medio entre la compra y la entrega es de cuatro coma dos días. La promesa publicada en el sitio es de dos a cinco días hábiles, y se cumple en el ochenta y uno por ciento de los casos.

### 4.7 El retiro en tienda y el despacho desde tienda

El cuarenta y uno por ciento de los pedidos en línea se retira en tienda. La tienda recibe el pedido, lo separa y lo entrega en un mesón que comparte espacio y personal con la operación de sala.

El diecisiete por ciento de los pedidos se despacha desde una tienda: el sistema decide que la unidad más cercana al cliente está en la tienda de Valdivia y le pide a esa tienda que la prepare y la entregue al transportista.

Ese mecanismo acorta la entrega y es lo que hace competitivo al canal en línea. También genera dos fricciones que nadie ha resuelto. La primera es operativa: el personal de la tienda no fue contratado para preparar pedidos y lo hace además de su trabajo. La segunda es de incentivos: cuando una unidad sale de la tienda de Valdivia para cumplir un pedido en línea, el vendedor de Valdivia perdió una venta presencial que ya no podrá hacer, y no recibe comisión por ella.

En las tiendas donde eso ocurre con frecuencia, la mercadería destinada al despacho en línea aparece con menos frecuencia de la que el sistema esperaría.

### 4.8 El marketplace de terceros

Desde 2022 la compañía intermedia la venta de trescientos diez vendedores externos, con ciento noventa mil referencias. Aporta el tres por ciento de los ingresos y un margen alto, porque la compañía no compra el producto: cobra una comisión.

El cliente no distingue. Compra en el sitio de la compañía, recibe una comunicación de la compañía y, cuando algo sale mal, va a la tienda de la compañía.

El mesón de atención al cliente recibe devoluciones y reclamos de productos que la compañía nunca tuvo, cuyo estado desconoce y cuyo vendedor no siempre responde. No existe un acuerdo de nivel de servicio medido con los vendedores de marketplace, ni un mecanismo para evaluarlos, ni una regla escrita de qué hace la tienda cuando el vendedor externo no responde.

### 4.9 La devolución, el cambio y la garantía legal

El nueve por ciento de las ventas en línea y el tres por ciento de las presenciales se devuelven. Los motivos son talla, color, expectativa y falla.

La devolución se recibe en el mesón. El producto se revisa, se decide si vuelve a la venta, y se emite la nota de crédito o el cambio. El reingreso al inventario lo hace una persona manualmente, y es una de las causas conocidas de diferencia de registro.

Cuando la devolución es por falla, entra en juego la garantía legal. La normativa vigente obliga a que el consumidor pueda ejercerla directamente ante el vendedor, sin ser derivado al fabricante ni a un servicio técnico. En la práctica, el mesón deriva: al servicio técnico de la marca en electrohogar, al vendedor de marketplace cuando el producto era de un tercero.

La compañía sabe que eso no corresponde. No tiene hoy ni el proceso ni el sistema para hacerlo de otra manera.

### 4.10 La originación del crédito en el punto de venta

La tarjeta propia participa en el treinta y ocho por ciento de las ventas de las tiendas. Se ofrece en el mesón del negocio financiero y también en la caja, cuando el cliente no tiene cupo o cuando el vendedor la propone.

Abrir una tarjeta implica identificar al cliente, evaluar su capacidad de pago, asignar un cupo, entregar la información precontractual del crédito —el costo total, la carga anual equivalente, los cargos asociados— y obtener la aceptación.

Todo eso ocurre en un mesón de tienda, muchas veces con el cliente apurado y con una fila detrás, y lo ejecuta una persona cuya remuneración mejora si la venta se cierra con la tarjeta.

La información precontractual se entrega impresa. No queda registro estructurado de qué versión del documento se entregó, ni de que el cliente la recibió antes de aceptar. La constancia es la firma en un formulario que se archiva.

La evaluación crediticia demora entre cuarenta segundos y tres minutos según la carga del sistema. Cuando demora, la venta se pierde o se cierra con otro medio de pago.

### 4.11 La cobranza, la repactación y el consentimiento

Seiscientas veinte mil tarjetas tienen saldo. Cuando una cuota se atrasa, empieza la cobranza: comunicaciones, llamados y, eventualmente, gastos de cobranza cuyos límites están regulados.

A los clientes con dificultades se les ofrece repactar: reordenar la deuda en nuevas condiciones de plazo y cuota. La repactación es un contrato nuevo y requiere el consentimiento expreso e informado del cliente. Hoy ese consentimiento se obtiene por teléfono. La llamada se graba y la grabación se conserva noventa días. La nueva condición se refleja en la plataforma de crédito y el cliente recibe una comunicación.

La revisión interna de mayo encontró mil doscientas cuarenta repactaciones de 2025 en las que no es posible recuperar la evidencia del consentimiento: la grabación ya no existe y el registro de la plataforma no acredita qué se le informó al cliente ni qué aceptó.

No hay indicio de que fueran indebidas. El problema es que la compañía no puede demostrarlo, y en un negocio fiscalizado la carga de acreditar recae en ella.

### 4.12 El evento de comercio electrónico

Tres días al año, en una fecha que fija la asociación gremial del comercio electrónico y que se anuncia con unas seis semanas de anticipación, el canal digital procesa el equivalente a veintidós días de venta normal.

Para ese evento la compañía prepara precios especiales, refuerza el centro de distribución y contrata capacidad adicional de infraestructura. Lo que no prepara es el inventario: los precios de campaña se cargan sobre el mismo registro de existencia de siempre, con el mismo descuento de seguridad de 2019, y el sitio compromete unidades a un ritmo que la operación descubre tres días después.

El resultado de junio de 2026 ya se describió. La compañía sabe que se repetirá si nada cambia, y sabe la fecha aproximada en que ocurrirá.

## Capítulo 5. LOS SISTEMAS QUE EXISTEN HOY

El PROPONENTE deberá integrarse a este panorama, que reúne nueve plataformas de seis proveedores distintos. La columna de destino indica la decisión ya tomada por el CLIENTE; donde dice «decisión del proponente», la decisión no está tomada y debe fundamentarse en la propuesta.

| Sistema | Función | Destino |
| --- | --- | --- |
| Sistema central de retail, implantado en 2009 | Maestro de artículos, órdenes de compra, recepción, inventario contable, precios y base de la reposición. | Decisión del PROPONENTE. Es el corazón del problema de inventario y la decisión de arquitectura más importante del caso, junto con la del numeral siguiente. |
| Plataforma de originación y cobranza de créditos, en operación desde 2011 | Evaluación, originación, cupos, estados de cuenta, cobranza y repactación de la filial emisora. | Se reemplaza. El proveedor anunció el fin de soporte para 2029 y la autoridad instruyó un plan de remediación con hitos verificables al mismo año. La migración es de una cartera viva de 620.000 clientes con saldo. |
| Punto de venta de tienda, implantado en 2014 | Cobro, promociones, emisión de documentos y consulta de existencia. | Decisión del PROPONENTE: hay tres versiones distintas desplegadas en las 22 tiendas y su unificación o reemplazo debe fundamentarse. |
| Plataforma de comercio electrónico, 2019 | Catálogo, disponibilidad publicada, carro y pedido del canal propio. | Se mantiene o se reemplaza, con justificación. Es la plataforma más nueva y la que expone al público el registro de inventario errado. |
| Plataforma de marketplace, 2022 | Catálogo de terceros, gestión de vendedores y liquidación de comisiones. | Se mantiene. Su integración con atención al cliente, devoluciones y garantía legal es parte del alcance. |
| Sistema de gestión de almacenes del centro de distribución principal, 2016 | Ubicaciones, preparación y despacho del centro de 42.000 m² | Se mantiene. Su extensión al centro de Concepción, que hoy opera con planillas, debe evaluarse y costearse. |
| Sistema de fidelización, 2017 | Puntos, segmentos y campañas. | Se reemplaza o se integra. Es uno de los puntos donde hoy se mezclan datos comerciales y datos del negocio financiero. |
| Sistema de gestión empresarial y facturación | Contabilidad, cuentas por pagar, remuneraciones y emisión de documentos tributarios. | Se mantiene. Es el único emisor de documentos tributarios. |
| Motor de precios y promociones | No existe como sistema. Los precios y las mecánicas promocionales se arman en planillas y se cargan masivamente. | Debe existir. Es la causa directa de la discrepancia entre precio exhibido y precio cobrado. |
| Integraciones punto a punto | 14 interfaces construidas por 6 proveedores distintos a lo largo de 15 años, la mayoría por archivo y por lote nocturno. | Se rediseñan. No existe documentación completa de ellas y ninguna persona en la compañía conoce el mapa entero. |
| Planillas de cálculo y listas impresas | Precios de campaña, cambio de etiquetas, operación del centro de distribución de Concepción, control de repositores externos, seguimiento de reclamos y control de devoluciones. | Deben desaparecer como sistema de registro. Ese es, en buena medida, el objeto de esta licitación. |

> Este caso no tiene un sistema legado: tiene nueve plataformas de seis proveedores y quince años, unidas por catorce interfaces punto a punto que en su mayoría transfieren archivos de noche. El problema del CLIENTE no es ningún sistema en particular, sino el tejido entre ellos: el mismo producto tiene un estado distinto en cada plataforma según la hora del día, y el mismo cliente existe varias veces con identificadores distintos. El PROPONENTE que aborde este caso como el reemplazo de un sistema habrá entendido mal el problema.

## Capítulo 6. CONECTIVIDAD, SEGURIDAD Y CONDICIONES DEL SITIO

| Elemento | Situación actual |
| --- | --- |
| Enlace de las tiendas en centro comercial | Catorce tiendas se conectan a través de la infraestructura del centro comercial, con un enlace propio de respaldo en ocho de ellas. Las mantenciones del centro comercial no se comunican. |
| Enlace de las tiendas a la calle | Ocho tiendas con enlace propio de un proveedor. Coyhaique no tiene respaldo contratado. |
| Centros de distribución | El principal cuenta con enlace redundante de dos proveedores. El de Concepción tiene un enlace único. |
| Centro de datos | Recinto propio de 140 m² habilitado en 2011 en la casa matriz, con sala de respaldo en la misma comuna. Cumple parcialmente los estándares del Capítulo 6 de las Bases Técnicas Transversales; la brecha está documentada en un informe interno de 2024 que el CLIENTE entregará al ADJUDICATARIO. |
| Segmentación de red en tienda | La red de cajas, la red administrativa, la red de videovigilancia y la red inalámbrica para clientes están segmentadas en 9 de las 22 tiendas. En las 13 restantes comparten infraestructura. |
| Medios de pago | Terminales en todas las líneas de caja, en los mesones del negocio financiero y en el canal digital, más la propia emisión de tarjetas. El alcance de cumplimiento de la norma de la industria de medios de pago está definido para el canal digital y no lo está para las tiendas. |
| Separación del negocio financiero | La filial emisora comparte centro de datos, red y equipo de tecnologías de información con el retail. La separación lógica entre ambos ámbitos está implementada de forma parcial y no está documentada. |
| Videovigilancia | 1.840 cámaras en 22 tiendas y 2 centros de distribución, con grabación local de 30 días. |
| Dispositivos en sala | El personal de venta dispone de 640 terminales móviles compartidas para consulta de existencia, repartidas de forma desigual entre tiendas y departamentos. No hay dispositivo asignado por persona. |
| Impresión de etiquetas | Impresoras de etiqueta en la bodega de cada tienda. El cambio de etiquetas se hace de noche, a partir de una lista impresa generada al cierre. |
| Condiciones del trabajo en sala | De pie, en jornada que incluye fines de semana y festivos, con peaks concentrados y con remuneración variable por comisión. Rotación anual del 62 %. |
| Condiciones del trabajo en caja | Con cliente al frente y fila detrás. Es el punto donde se resuelven simultáneamente el cobro, la promoción y, con frecuencia, una operación de crédito. |

> La compañía ha sido explícita en cuatro puntos. Primero: la separación entre el negocio de retail y el negocio financiero fiscalizado debe quedar implementada y documentada, y ninguna facilidad comercial puede debilitarla. Segundo: una tienda debe poder vender y cobrar aunque se caiga el enlace, incluidas las catorce cuya conectividad depende de un centro comercial. Tercero: el precio que se cobra y el precio que se exhibe deben ser el mismo, y la compañía debe poder acreditar cuál era el precio publicado en un momento dado. Cuarto: ninguna solución puede suponer un dispositivo asignado a cada vendedor, porque no existe y no está en el alcance adquirirlo.

## Capítulo 7. LO QUE DUELE: INDICADORES DEL PROBLEMA

Los siguientes datos corresponden al ejercicio 2025 y al primer semestre de 2026, y provienen de los registros de la compañía. Se entregan porque dimensionan el problema y porque el PROPONENTE deberá comprometer mejoras verificables sobre ellos.

### 7.1 Inventario y cumplimiento de la promesa

| indicador | Valor | Referencia |
| --- | --- | --- |
| Diferencias detectadas en el conteo cíclico | 12,4 % de las referencias auditadas | bajo 2% |
| Merma o pérdida desconocida | 1,9 % de la venta; > $ 7.800 millones | bajo. 1% |
| Pp roporción ión de le la merma que es error de registro ist y no pérdida física |  |  |
| Pedidos en línea cancelados por falta de existencia, año 2025 | 19% | bajo 0,3 % |
| Pedidos cancelados en el evento de junio de 2026 | dla equivalentes i a l 2,7% | cero |
| Reclamos formales derivados. de esas cancelaciones | 1.900, con procedimiento abierto por la autoridad | cero |
| Descuento de seguridad aplicado a la existencia publicada | un valor fijo definido en 2019 y nunca revisado | dinámico y por categoría |
| Cumplimiento de la promesa de entrega publicada | 81% | sobre 97 % |
| Tiempo medio entre compra en línea y entrega | 4,2 días | — |
| Centros de distribución con sistema de gestión de almacenes | 1de 2 | 2de2 |

### 7.2 Precio, venta y canales

| indicador | Valor |
| --- | --- |
| Discrepancia entre precio exhibido y precio cobrado en la fiscalización de febrero | 11 % de 120 productos revisados en 4 tiendas |
| Registro de qué etiqueta se cambió, cuándo y quién | inexistente |
| Registro histórico consultable del precio publicado en cada canal | inexistente |
| Frecuencia de cambio de precio en campaña | varias veces al día, sobre 268.000 referencias |
| Latencia entre el cambio de precio y el cambio de la etiqueta física | hasta 24 horas |
| Pedidos que se retiran en tienda | 41 % del canal en línea |
| Pedidos que se despachan desde una tienda | 17 % del canal en línea |
| Compensación al vendedor de la tienda que despacha un pedido en línea | inexistente |
| Acuerdo de nivel de servicio medido con los 310 vendedores de marketplace | inexistente |
| Regla escrita para atender la devolución de un producto de marketplace en tienda | inexistente |

### 7.3 Negocio financiero y cumplimiento

| Indicador | Valor | Referencia |
| --- | --- | --- |
| Repactaciones de 2025 sin evidencia recuperable del consentimiento | 1.240 | cero |
| Plazo de conservación de las grabaciones de originación y repactación | emelen | plazo del crédito y 6 años más |
| Registro, estructurado de la. información precontractual entregada al cliente. | inexistente; la constancia es una firma en un formulario archivado. | trazable por operación |
| Tiempo de evaluación crediticia en el punto de venta | de 40 segundos a 3 minutos | bajo 10 segundos |
| Separación técnica documentada entre los datos del retail y los del negocio financiero | parcial y no documentada | implementada y documentada |
| Hitos del plan de remediación instruido por la autoridad | el último vence en 2029 | cumplidos |
| Fin de soporte de la plataforma de crédito de 2011 | 2029 | — |

### 7.4 Personas, sistemas y operación

| Indicador | Valor |
| --- | --- |
| Rotación anual del personal de venta y caja | 62 %, más 1.900 personas de temporada al año |
| Repositores E externos de proveedores y que trabajan y en sala | ≈ 1,100, sin control de actividad ni de acceso individualizado OS |
| Plataformas distintas que sostienen la operación | 9, de 6 proveedores, con hasta 17 años de antigúedad |
| Integraciones punto a punto entre plataformas | 14, la mayoría por archivo y lote nocturno |

| indicador | Valor |
| --- | --- |
| Personas que conocen el mapa completo de integraciones | ninguna |
| Tiendas con red segmentada | 9 de 22 |
| Alcance de cumplimiento de la norma de medios de pago definido | sólo para el canal digital |
| Personal del área de tecnologías de información | 46, para 9 plataformas, 22 tiendas y 2 centros de distribución |

> Ninguno de estos indicadores se resuelve comprando software. Esta compañía promete cuatro cosas cada día: que el producto existe, que el precio es el de la etiqueta, que la entrega llega en la fecha ofrecida y que las condiciones del crédito son las informadas. Las cuatro se construyen sobre registros que la propia empresa sabe imprecisos, y ninguna puede acreditarse después. El PROPONENTE que entienda que el objeto de este proyecto no es un sistema de inventario sino la capacidad de hacer promesas que se puedan cumplir y demostrar tendrá una ventaja evidente sobre quien ofrezca módulos.

# Título III. Lo que dicen quienes operan

## Capítulo 8. ENTREVISTAS DE LEVANTAMIENTO

Las siguientes son transcripciones editadas de las entrevistas de levantamiento sostenidas entre enero y julio de 2026, en temporada baja y durante el evento de junio, en tiendas de mall y de calle y en los dos centros de distribución. Se entregan con sus contradicciones intactas, porque las contradicciones son parte del problema.

El PROPONENTE debe leerlas como lo que son: la palabra de personas que conocen muy bien su parte de la operación y que no tienen por qué conocer la de los demás, ni tienen por qué saber de sistemas. Distinguir el hecho de la opinión, la necesidad del capricho y el problema de la solución que la persona ya se imaginó es parte del trabajo profesional que se está licitando.

#### Amparo Ganderats Vial — Gerenta General

Le voy a resumir el problema de esta empresa en una frase: prometemos cosas que no podemos garantizar y después no podemos demostrar qué prometimos.

Prometemos que el producto existe, y en junio dos mil ochocientas cuarenta veces no existía. Prometemos que el precio es el de la etiqueta, y en la fiscalización el once por ciento no lo era. Prometemos condiciones de crédito, y en mil doscientos cuarenta casos no podemos acreditar lo que el cliente aceptó. Es el mismo problema tres veces.

Y quiero desactivar de entrada una idea que va a aparecer: esto no se arregla comprando un sistema de inventario. Nuestro registro está malo en un doce coma cuatro por ciento y va a seguir estando malo un buen tiempo. Lo que necesito es poder hacer promesas sobre un dato que sé imperfecto, y saber cuánto margen me estoy dando.

El directorio puso una condición y la voy a repetir porque es la única línea roja: somos una tienda y somos un emisor de crédito fiscalizado. Son dos negocios con dos regímenes. Cualquier propuesta que los trate como uno solo, o que borre la frontera entre sus datos porque es más cómodo, no la vamos a aceptar.

Última cosa. Tenemos nueve plataformas de seis proveedores y quince años, pegadas con catorce interfaces que corren de noche. Nadie en esta empresa tiene el mapa completo. Si alguien viene a decirme que va a reemplazar todo en dos etapas, no le voy a creer.

#### Rodrigo Sanhueza Bustos — Gerente Comercial

Yo manejo doscientas sesenta y ocho mil referencias y en vestuario eso se multiplica por talla y por color. Rotamos el surtido completo dos veces al año.

Los precios los defino yo y en campaña los cambio varias veces al día. Eso es el negocio: si el competidor bajó, yo bajo. No voy a dejar de hacerlo porque un sistema no alcance.

El problema es la etiqueta. Yo cambio el precio a las once de la mañana, llega a las cajas y al sitio en minutos, y a la etiqueta de la sala llega esa noche cuando alguien la imprime y la pega. Doce horas de diferencia, y eso es la infracción que nos encontraron.

Me han propuesto etiquetas electrónicas. Son doscientas sesenta y ocho mil referencias en veintidós tiendas; el costo es enorme. Yo no digo que no, digo que alguien tiene que ponerle un número a eso y compararlo con la multa y con lo que perdemos por no poder cambiar precio de verdad.

Y tengo un tema con el maestro de artículos que nadie mira. Cuando yo creo un producto, si no le pongo bien los atributos, después no se puede publicar en el sitio, o se publica mal, o se calcula mal el despacho. Nadie audita eso y no hay nadie a quien reclamarle.

Del descuento de seguridad que le aplicamos a la existencia publicada: lo puso alguien el 2019 y es un número fijo. Yo no sé quién fue y nunca lo hemos revisado.

#### Marisol Tapia Verdugo — Jefa de Tienda, Temuco

Yo tengo cuatro mil metros de sala, ochenta personas y como cincuenta repositores de proveedores que entran todos los días y no son mis trabajadores.

El cambio de etiquetas es de noche, con una lista impresa. Cuando la lista trae ochocientos cambios, no alcanzamos. Se priorizan las góndolas de adelante y las de atrás quedan para el día siguiente. Eso todo el mundo lo sabe.

Del inventario le voy a decir algo que en la casa matriz cuesta que entiendan: el probador es un agujero negro. Entran diez prendas y vuelven ocho, y las dos que faltan pueden estar en el suelo detrás de una puerta, pueden haberse ido, o pueden haberse colgado en otro perchero. Las tres cosas se ven igual en el sistema.

Cuando prevención hace conteo cíclico y encuentra diferencia, eso se anota como merma. Yo llevo doce años acá y le puedo asegurar que buena parte de eso no se lo robaron: está mal puesto o mal recibido. Pero no tengo cómo demostrarlo, y a mí me miden por la merma.

Y ahora tengo lo del despacho desde tienda, que es lo que más me enoja. El sistema me pide que prepare un pedido que compró alguien en Santiago, con una unidad que yo tenía en la sala. Se la saco al vendedor de la mano. Él pierde la comisión y a mí me baja la venta de la tienda, y esa unidad igual se descuenta de mi inventario.

Le voy a ser franca: en algunas tiendas esa unidad no aparece. Nadie lo dice, pero pasa.

#### Nicolás Errázuriz Domeyko — Gerente de Canales Digitales

El evento de junio fue el mejor y el peor de nuestra historia con dos días de diferencia. El sitio aguantó ciento cuatro mil pedidos y no se cayó. Y el jueves descubrimos que dos mil ochocientos cuarenta de esos pedidos eran humo.

Yo publico la existencia que me entrega el sistema central. Sumo el centro de distribución más las veintidós tiendas, le resto un descuento de seguridad y eso es lo que ofrezco. El descuento es un número fijo del 2019.

Cuando le pido a logística que me den un número más confiable, me dicen que el registro está malo en doce por ciento. Y cuando les propongo que entonces publiquemos menos, me dicen que dejamos de vender. Las dos cosas son verdad y llevamos tres años así.

El marketplace me da margen y me da surtido: ciento noventa mil referencias que no tengo que comprar. Pero el cliente no distingue: compra en nuestro sitio, recibe nuestro correo, y cuando el producto no llega va a nuestro mesón. No tenemos acuerdo de servicio medido con los trescientos diez vendedores ni forma de sacar al que lo hace mal.

Lo que necesito es simple de decir: que cuando yo digo «disponible», sea verdad. Y si no puedo saberlo con certeza, que al menos yo sepa con qué probabilidad lo estoy diciendo, y pueda decidir cuánto riesgo tomo por categoría.

La fecha del evento la fija la asociación gremial y la anuncian con seis semanas. No la elijo yo y no se puede mover.

#### Fernanda Quilaqueo Nahuelpán — Gerenta de Logística y Centros de Distribución

Mi centro principal tiene cuarenta y dos mil metros y sistema de gestión de almacenes desde el 2016. Ahí sé dónde está cada cosa.

El de Concepción lo abrimos el 2023 para acortar el sur y funciona con planillas. Nueve mil metros y la ubicación de la mercadería está en la cabeza de las personas que trabajan ahí. Cuando alguien falta, se nota.

El problema grande no está en mis centros: está en las tiendas. La tienda no es una bodega, no fue diseñada como bodega y su personal no fue contratado para preparar pedidos. Y hoy el diecisiete por ciento de los pedidos en línea sale desde una tienda.

Y todo mi cálculo de reposición se hace con el inventario del sistema. Si el registro está malo, yo repongo mal: mando a una tienda lo que ya tenía y dejo sin stock a otra. Eso no es un error del algoritmo, es basura entrando.

Sobre la merma: yo estoy de acuerdo con las jefas de tienda. Le llamamos merma a la diferencia y adentro hay robo, hay daño no dado de baja, hay recepción mal hecha y hay devoluciones mal reintegradas. Son cuatro problemas distintos con cuatro soluciones distintas y nosotros los tratamos como uno.

Si tuviera que pedir una sola cosa sería poder contar sin cerrar la tienda, seguido, y saber por categoría cuánto le puedo creer a mi propio registro.

#### Álvaro Peña Iturriaga — Gerente del Negocio Financiero

Un millón trescientas ochenta mil tarjetas, seiscientas veinte mil con saldo, ciento ochenta y seis mil millones colocados. Somos el diez por ciento de los ingresos y bastante más del resultado.

Y somos una filial fiscalizada. Eso significa que todo lo que hacemos tiene que poder acreditarse: qué le informamos al cliente, cuándo, qué aceptó y en qué condiciones.

Lo de las repactaciones nos golpeó fuerte. No hubo un solo caso de mala fe, y da lo mismo: la grabación se borraba a los noventa días y la plataforma del 2011 guarda el resultado pero no guarda la conversación. Es un problema de diseño de hace quince años que nos explotó ahora.

La plataforma se acaba el 2029 y el plan de remediación también vence el 2029. Migrar una cartera viva de seiscientas veinte mil personas con saldo, con sus cuotas, sus repactaciones y sus juicios en curso, no es una migración de datos: es una operación de alto riesgo con clientes reales en el medio.

Ahora, voy a decir la parte impopular. Yo necesito que la evaluación crediticia en caja tome segundos, no minutos. Hoy se demora hasta tres minutos y ahí se pierde la venta. Y necesito que el vendedor ofrezca la tarjeta, porque es el treinta y ocho por ciento de la venta de la tienda.

Sé que eso choca con lo que va a decir Cecilia. Choca de verdad, no es un malentendido, y alguien tiene que resolverlo con un diseño y no con una circular.

#### Cecilia Bordalí Ruz — Contralora y Jefa de Cumplimiento

Voy a partir donde termina Álvaro. Sí, choca. Y mi posición la velocidad puede por es que no comprarse con información no entregada.

Cuando abrimos una tarjeta en el mesón de una tienda, tenemos que entregar la información precontractual completa antes de que el cliente acepte. Hoy la entregamos impresa y la constancia es una firma en un formulario que se archiva. No hay registro de qué versión del documento se entregó ni de que el cliente la tuvo antes de firmar.

Eso es lo mismo que nos pasó con las repactaciones. En un negocio fiscalizado, un consentimiento que no se puede acreditar es un consentimiento que no existe, y la carga de probar la tenemos nosotros. Esta industria ya vivió eso en Chile y no hace falta que recuerde cómo terminó.

El segundo tema es el que menos se discute y el que más me preocupa. Marketing quiere usar el comportamiento de pago de nuestros clientes para segmentar ofertas de la tienda. Comercialmente es obvio y jurídicamente no lo es: esa información se recogió en un negocio regulado, con una finalidad, y hoy compartimos centro de datos, red y equipo de tecnología con el retail sin una separación documentada.

Yo no estoy diciendo que nunca se pueda. Estoy diciendo que alguien tiene que definir qué se puede, con qué base y con qué control técnico, y que eso quede escrito y auditable. Hoy no está escrito y por eso en la práctica pasa cualquier cosa.

Y sobre el vendedor: no me sirve capacitarlo. Su comisión sube si cierra rápido y si cierra con tarjeta. Mientras eso sea así, el proceso tiene que hacer imposible saltarse un paso, no confiar en que no se lo salte.

#### Jonathan Millán Curihual — Vendedor de piso, 4 años, departamento de electrohogar

Yo gano un sueldo base y comisión. La comisión es lo que hace la diferencia, y sube si el cliente paga con nuestra tarjeta. Eso no es un secreto, está en mi contrato.

Un sábado en la tarde yo atiendo a diez personas a la vez. Si un cliente se decide, lo que menos quiero es demorarme. Y abrir una tarjeta hoy son tres minutos de evaluación más el papeleo. Muchas veces el cliente dice «déjalo, pago con débito» y ahí perdí la mitad de mi comisión.

Me van a preguntar si le leo todo el documento al cliente. Le voy a contestar honestamente: se lo entrego y le digo lo principal. Con fila detrás no hay otra forma. Y sé que eso no es lo que corresponde.

Del sistema: yo consulto stock en un aparato que compartimos entre varios del piso. A veces no hay uno libre. Y cuando dice que hay en Rancagua, yo se lo ofrezco al cliente, y como una de cada ocho veces después no llega. Esa llamada me la hace el cliente a mí.

Lo del despacho desde tienda me tiene molesto y no soy el único. Vienen de bodega a buscar una unidad que yo tenía apalabrada con un cliente, porque alguien la compró por internet. Esa venta no es mía y la unidad tampoco está.

Si me preguntan qué me serviría: que el aparato me diga la verdad, y que abrir una tarjeta sea rápido de verdad. Si me hacen el proceso más largo para cumplir algo, yo voy a dejar de ofrecerla, y no soy el único.

#### Solange Bittner Ampuero — Vendedora de marketplace, empresa de 6 personas

Nosotros vendemos artículos de decoración y llevamos tres años en el marketplace de Ancoa. Nos ha ido bien y no quiero que suene a reclamo.

Mi problema es que trabajo a ciegas. Yo publico, me llega un pedido y despacho. Después no sé nada más. Si el cliente reclamó, si devolvió, si quedó conforme, no me entero salvo que alguien me escriba.

Y he tenido varias veces esto: un cliente devuelve mi producto en una tienda de Ancoa, en Concepción, y a mí nadie me avisa. El producto queda en una bodega de ellos, yo sigo esperando y el cliente ya tiene su plata de vuelta. Después aparece la nota de crédito en mi liquidación y yo tengo que salir a preguntar dónde está mi mercadería.

Tampoco tengo idea de cómo me evalúan. Sé que hay vendedores que despachan tarde y que eso nos perjudica a todos, pero no hay una nota, no hay un ranking, no hay nada que me diga si lo estoy haciendo bien.

Lo que necesito es poco: saber en qué estado está cada pedido mío, enterarme de una devolución cuando ocurre y no cuando llega la liquidación, y saber con qué regla me miden. Con eso yo me acomodo.

Y una cosa que quizá les sirve: cuando ellos publican mi stock, publican lo que yo declaré la última vez que sincronicé. Si yo vendí las últimas tres unidades en otro canal, ellos siguen ofreciéndolas.

#### Paula Antileo Huenchur — Clienta. Pedido cancelado en el evento de junio

Compré un refrigerador el primer día del evento, a las siete de la mañana, porque estaba con un precio muy bueno y yo lo tenía visto hace meses.

Me llegó la confirmación de compra, me cobraron, y me dijeron entre dos y cinco días hábiles. Al quinto día no había llegado nada. Al octavo me llegó un correo diciendo que no había stock y que me devolvían el dinero más un cupón de veinte mil pesos.

Yo entiendo que las cosas fallen. Lo que no entiendo es que me hayan cobrado por algo que no tenían, y que el mismo refrigerador estuviera a la venta esa misma semana a cincuenta mil pesos más caro.

Llamé cuatro veces. La primera me dijeron que esperara. La segunda que reclamara en el sitio. La tercera me dieron un número de caso. La cuarta me dijeron que el caso estaba cerrado y nadie me había avisado.

Fui a la tienda de mi ciudad, porque pensé que en persona iba a ser distinto. La señorita del mesón fue muy amable y me dijo la verdad: que ella no ve los pedidos de internet, que eso lo maneja otra área y que no me podía ayudar.

Al final puse el reclamo en el organismo del consumidor. No por los veinte mil pesos: porque en ninguna de las cinco veces que hablé con ellos alguien supo decirme qué había pasado con mi compra.

> Sobre las contradicciones. El PROPONENTE habrá advertido que estas entrevistas no son consistentes entre sí. Canales digitales necesita publicar más existencia y logística sostiene que el registro no lo permite. Comercial cambia precios varias veces al día y la tienda cambia etiquetas una vez por noche. El negocio financiero necesita una evaluación crediticia de segundos y cumplimiento exige entregar y acreditar información precontractual completa, mientras el vendedor —cuya comisión sube si cierra rápido y con tarjeta— reconoce que hoy no lo hace. Marketing quiere usar el comportamiento de pago para segmentar y la contralora advierte que ese dato pertenece a un negocio regulado. El despacho desde tienda hace competitivo al canal en línea y le quita la venta al vendedor que tenía la unidad en la mano. Y la vendedora de marketplace y la clienta describen, desde dos lados opuestos, el mismo agujero: nadie sabe en qué estado está un pedido. Estas tensiones son reales y no se resolverán antes de la adjudicación. Resolverlas —o, cuando no sea posible, proponer una arquitectura que permita convivir con ellas y dejar constancia de la decisión y de su costo— es parte de lo que se está licitando.

# Título IV. Lo que el mandante espera

## Capítulo 9. EXPECTATIVAS DE NEGOCIO

Las siguientes son las expectativas del CLIENTE expresadas como resultados de negocio. Deliberadamente no están escritas como requerimientos. Traducirlas en requerimientos funcionales y no funcionales, priorizarlos, asignarlos a una etapa y hacerlos verificables es trabajo del PROPONENTE.

### 9.1 Que la compañía sólo prometa lo que puede entregar

El CLIENTE espera dejar de comprometer existencia que no tiene. No espera que el registro de inventario se vuelva perfecto —sabe que eso tomará años—, sino disponer de una noción de disponibilidad que incorpore el error conocido, que se calcule de forma distinta según la categoría y el punto de existencia, y que permita decidir cuánto riesgo se asume al publicar.

Esta es la primera expectativa y es la que originó la licitación.

### 9.2 Que se sepa cuánto vale el propio registro

El CLIENTE espera medir la exactitud del inventario de forma continua y por categoría, contar sin cerrar la tienda, y separar de una vez la merma en sus componentes: lo que se perdió físicamente y lo que nunca se registró bien.

Espera dejar de investigar como robo lo que es un error administrativo, y de tratar como error administrativo lo que sí es robo.

### 9.3 Que el precio exhibido y el precio cobrado sean el mismo

El CLIENTE espera que un cambio de precio llegue a todos los puntos donde el precio se comunica —cajas, canal digital y sala de venta— dentro de un plazo comprometido, y espera saber en todo momento cuántos puntos de exhibición están desactualizados y cuáles.

Espera además poder acreditar, meses después, qué precio estaba publicado en cada canal en un instante determinado.

### 9.4 Que un pedido tenga un solo estado y todos lo vean

El CLIENTE espera que un pedido tenga un estado único y consultable por el cliente, por el vendedor, por el mesón de atención, por el centro de distribución, por la tienda que despacha y —cuando corresponda— por el vendedor de marketplace.

Espera que nadie vuelva a decirle a un cliente que no ve los pedidos de internet.

### 9.5 Que el despacho desde tienda deje de castigar a la tienda

El CLIENTE espera que la decisión de desde dónde se despacha un pedido considere el costo total y no sólo la distancia, y espera resolver el conflicto de incentivos que hoy hace que una unidad comprometida para un despacho en línea a veces no aparezca.

### 9.6 Que el marketplace se administre y no sólo se aloje

El CLIENTE espera medir a sus trescientos diez vendedores externos con reglas conocidas por ellos, conocer el estado real de cada pedido intermediado, y tener un procedimiento definido para atender en tienda la devolución de un producto que la compañía no vendió sino que intermedió.

### 9.7 Que la garantía legal se ejerza donde corresponde

El CLIENTE espera que un cliente que ejerce la garantía legal sea atendido en el mesón sin ser derivado al fabricante, al servicio técnico ni al vendedor de marketplace, y que la compañía resuelva después con quien corresponda.

### 9.8 Que el crédito se otorgue rápido y se pueda acreditar

El CLIENTE espera reducir a segundos la evaluación crediticia en el punto de venta, y espera al mismo tiempo que quede registro estructurado de qué información precontractual se entregó, en qué versión, en qué momento y qué aceptó exactamente el cliente.

El mandante ha sido explícito en que estas dos cosas no se negocian entre sí: la velocidad no se compra con información no entregada.

### 9.9 Que toda repactación tenga consentimiento acreditable

El CLIENTE espera que ninguna modificación de las condiciones de un crédito pueda registrarse sin evidencia recuperable del consentimiento informado del cliente, y que esa evidencia se conserve por todo el plazo del crédito y el período posterior que la normativa exija.

### 9.10 Que la frontera entre los dos negocios esté implementada

El CLIENTE espera que la separación entre los datos del retail y los del negocio financiero fiscalizado esté definida, implementada técnicamente, documentada y auditable, y que exista una regla explícita —y no una práctica— sobre qué información puede cruzar esa frontera, con qué base y con qué autorización.

### 9.11 Que el evento de junio deje de ser una ruleta

El CLIENTE espera enfrentar el evento anual de comercio electrónico con una preparación que incluya el inventario y no sólo la infraestructura, con una estrategia de degradación definida de antemano y con la capacidad de suspender la publicación de una categoría antes de comprometer unidades que no existen.

## Capítulo 10. RESTRICCIONES NO NEGOCIABLES

Las siguientes condiciones no están en discusión. Una propuesta que no las respete será evaluada como falta de comprensión del caso.

| N? | Restricción |
| --- | --- |
| 1 | El negocio de retail y el negocio financiero son dos negocios con regímenes distintos. La separación de sus datos debe quedar definida, implementada técnicamente, documentada y auditable. Ninguna facilidad comercial puede debilitarla. |
| 2 | Ninguna modificación de las condiciones de un crédito puede registrarse sin evidencia recuperable del consentimiento informado del cliente, conservada por todo el plazo del crédito y el período posterior que la normativa exija. |
| 3 | La información precontractual del crédito debe entregarse antes de la aceptación y su entrega debe quedar acreditada de forma estructurada. Ningún requisito de rapidez comercial puede omitirla ni posponerla. |
| 4 | El precio cobrado debe ser el precio exhibido. La compañía debe poder acreditar qué precio estaba publicado en cada canal en un momento determinado. |
| 5 | Una tienda debe seguir vendiendo y cobrando ante la pérdida del enlace hacia el exterior, incluidas las 14 cuya conectividad depende del administrador de un centro comercial. |
| 6 | El sistema de gestión empresarial se mantiene y sigue siendo el único emisor de documentos tributarios. |
| 7 | La garantía legal se ejerce ante la compañía. Ninguna solución puede diseñar un flujo que derive al consumidor al fabricante, al servicio técnico o al vendedor de marketplace como condición para ser atendido. |
| 8 | La migración de la cartera de crédito involucra 620.000 clientes con saldo vigente, con cuotas, repactaciones y cobranzas en curso. No admite pérdida, interrupción del servicio ni divergencia de saldos. |
| 9 | Prohibido intervenir sistemas entre el 1 de noviembre y el 6 de enero, durante los tres días del evento anual de comercio electrónico y la semana previa, durante el evento de noviembre, en la semana del Día de la Madre y entre la última semana de enero y la primera de marzo. |
| 10 | La fecha del evento anual de comercio electrónico la fija la asociación gremial y se anuncia con unas seis semanas. El plan debe absorberla sin desplazar hitos contractuales. |
| 11 | El personal de venta no tiene dispositivo asignado: hay 640 terminales compartidas para 3.820 personas. Ninguna solución puede suponer un dispositivo por vendedor, y su adquisición no está en el alcance. |
| 12 | Aproximadamente 1.100 repositores de proveedores trabajan en la sala de venta sin ser trabajadores de la compañía. No se les puede imponer herramientas ni capacitación por la vía laboral. |
| 13 | La rotación anual del personal de venta y caja es del 62 % y se incorporan 1.900 personas de temporada en noviembre y diciembre, período en que además está prohibido intervenir. |
| 14 | El centro de distribución de Concepción opera hoy con planillas. Su incorporación a un sistema de gestión de almacenes debe evaluarse y costearse; no puede darse por supuesta. |
| 15 | La compañía no dispone de documentación completa de las 14 integraciones punto a punto existentes y ninguna persona conoce el mapa entero. Levantarlo es parte del trabajo y no una condición previa que el CLIENTE vaya a entregar resuelta. |

## Capítulo 11. EXCLUSIONES EXPLÍCITAS

Para evitar sorpresas, el CLIENTE declara expresamente qué NO está pidiendo:

- No se pide reemplazar el sistema de gestión empresarial ni la emisión de documentos tributarios.
- No se pide instalar etiquetas electrónicas en las 22 tiendas, aunque sí evaluar la alternativa, especificarla y costearla frente a las demás opciones de resolver la discrepancia de precio.
- No se pide adquirir dispositivos móviles para el personal de venta, aunque sí especificar cuántos se requerirían y con qué características.
- No se pide desarrollar la plataforma de los vendedores de marketplace ni operar su logística; sí integrarla, medirla y resolver la devolución en tienda.
- No se pide gestión de remuneraciones, aunque sí el cálculo de la base de comisión cuando la venta se origina en un canal y se cumple en otro.
- No se pide operar la cobranza judicial; sí mantener el expediente trazable de cada operación de cobranza y de cada repactación.
- No se pide sustituir a las empresas de transporte de última milla; sí integrarlas y trazar el estado del pedido hasta la entrega.
- No se pide construir infraestructura: canalizaciones, obras eléctricas y cableado que la solución requiera deben especificarse y costearse, y los ejecuta el CLIENTE.
- No se pide resolver la relación con los administradores de los centros comerciales; sí diseñar para que su indisponibilidad no detenga la venta.
- El hardware —terminales de caja, dispositivos de sala, lectores, impresoras de etiqueta, equipamiento de red y de centro de distribución— lo adquiere el CLIENTE; el PROPONENTE debe especificar exactamente qué comprar, cuánto y con qué características, conforme al Capítulo 8 de las Bases Técnicas Transversales.

> Que algo esté excluido del alcance no significa que pueda ignorarse en el diseño. La solución debe convivir con todo lo excluido, y las dependencias que ello genera deben estar identificadas, documentadas y consideradas en el plan y en el riesgo.

## Capítulo 12. MARCO NORMATIVO Y COMPROMISOS CON TERCEROS

El PROPONENTE deberá identificar, investigar y considerar en su propuesta el marco que aplica a esta industria. El CLIENTE entrega la orientación inicial; la profundización es parte del trabajo.

| Ámbito | Referencia | Por qué importa aquí |
| --- | --- | --- |
| Protección del consumidor | Ley N° 19.496 y sus reformas posteriores, incluida la que refuerza los derechos del consumidor en materia de garantía y de atención. | Es el marco de la garantía legal, del derecho a retracto, de la información de precios y de la obligación de no derivar al consumidor. |
| Información y publicidad de precios | Normativa sobre información del precio al consumidor y consecuencias de la discrepancia entre el precio exhibido y el cobrado. | Es el origen de la fiscalización de febrero y del 11 % de discrepancia detectado. |
| Contratación a distancia | Reglas aplicables a la venta por medios electrónicos, formación del consentimiento, confirmación de la compra y derecho a retracto. | Un pedido aceptado y cobrado que después se cancela por falta de existencia se juzga bajo estas reglas. |
| Garantía legal | Régimen de garantía del producto y derecho del consumidor a dirigirse directamente al vendedor. | Hoy el mesón deriva al fabricante o al vendedor de marketplace, y la compañía sabe que no corresponde. |
| Emisores de tarjetas de casa comercial | Régimen aplicable a los emisores de tarjetas de crédito no bancarias y su fiscalización por la autoridad del mercado financiero. | Determina las obligaciones de la filial emisora, incluidos gobierno, control interno y reporte. |
| Protección del consumidor financiero | Obligaciones de información precontractual, contenido mínimo del contrato, costo total del crédito y carga anual equivalente. | Es lo que hoy se entrega impreso en un mesón, sin registro estructurado de su entrega. |
| Repactación de deudas | Requisitos de consentimiento expreso e informado para modificar las condiciones de un crédito y su acreditación. | Es el origen de los 1.240 casos sin evidencia recuperable y del plan de remediación instruido. |
| Cobranza extrajudicial | Límites a los gastos de cobranza, a las comunicaciones y a las prácticas admisibles. | Involucra a una parte de los 620.000 clientes con saldo vigente. |
| Tasa máxima convencional | Límite legal a la tasa de interés aplicable a las operaciones de crédito. | Condiciona la oferta y el cálculo de toda operación. |
| Prevención de lavado de activos | Obligaciones de conocimiento del cliente, reporte de operaciones y conservación de antecedentes aplicables al emisor. | Aplica a la originación en el punto de venta y a la administración de la cartera. |
| Protección de datos personales | Ley N° 21.719, con especial atención al uso del comportamiento de pago con finalidad comercial y al perfilamiento. | Es la frontera entre los dos negocios y hoy no está documentada. |
| Medios de pago con tarjeta | Norma de seguridad de la industria de medios de pago, aplicable simultáneamente a cajas presenciales, comercio electrónico y emisión propia. | El alcance de cumplimiento está definido para el canal digital y no para las tiendas. |
| Documentos tributarios electrónicos | Normativa de la autoridad tributaria sobre boleta y factura electrónica en alto volumen. | ≈ 31 millones de documentos al año. |
| Intermediación en plataformas digitales | Reglas aplicables a quien intermedia la venta de terceros y a la información que debe entregar al consumidor. | 310 vendedores y 190.000 referencias que el cliente no distingue de las propias. |
| Normativa laboral | Jornada en comercio, trabajo en días festivos, contratación de temporada y presencia de personal externo en las instalaciones. | Involucra 62 % de rotación, 1.900 contrataciones de temporada y 1.100 repositores externos. |

> Este listado es orientador, no exhaustivo. El PROPONENTE es responsable de identificar la normativa aplicable completa y de acreditar en su propuesta cómo la solución la satisface. Invocar una norma sin explicar qué control concreto la implementa se evaluará como no acreditada. En este caso, además, la propuesta debe distinguir con claridad qué obligaciones recaen sobre el retail y cuáles sobre la filial emisora fiscalizada.

## Capítulo 13. HORIZONTE, PRIORIDADES Y ETAPAS

### 13.1 Lo que el comité quiere primero

El comité expresó, sin transformarlo en instrucción técnica, un orden de urgencia: primero la exactitud del inventario y la disponibilidad publicada, porque de ahí salió el episodio de junio y porque hay un procedimiento abierto; luego el precio y su trazabilidad; y por último el negocio financiero, el marketplace y la analítica.

El gerente del negocio financiero dejó una objeción registrada que conviene tomar en serio: «el plan de remediación instruido por la autoridad vence en 2029 y la plataforma de crédito deja de tener soporte el mismo año. Migrar una cartera viva de seiscientos veinte mil clientes con saldo no se hace en un semestre. Si eso queda en la Etapa 2, no llegamos».

La contralora dejó otra: «la frontera entre los datos de los dos negocios hay que definirla antes de construir cualquier vista unificada de cliente, no después. Si primero se construye y después se separa, no se separa nunca».

Ese orden es una preferencia del mandante, no una definición de alcance. La distribución concreta entre la Etapa 1 y la Etapa 2 la propone el PROPONENTE y debe justificarla en función de las dependencias técnicas, del riesgo, de los hitos externos del numeral 13.2 y de la capacidad de absorción del CLIENTE.

> Una propuesta que se limite a repetir el orden de preferencia del comité sin analizarlo será evaluada como falta de criterio profesional. Si el PROPONENTE considera que hay una dependencia técnica que obliga a alterar ese orden, debe decirlo y fundamentarlo. El CLIENTE contrata ingeniería, no obediencia.

### 13.2 Hitos externos que condicionan el proyecto

| Fecha | Hito externo | Consecuencia |
| --- | --- | --- |
| 1 de noviembre al 6 de enero | Campaña de Navidad y liquidación de enero. Peak anual de venta presencial, con 1.900 personas de temporada incorporadas. | Congelamiento total, coincidente con el peak de personal nuevo en sala. |
| Tres días entre mayo y junio | Evento anual de comercio electrónico. Se procesa el equivalente a 22 días de venta en línea normal. | Congelamiento del evento y de la semana previa. La fecha la fija la asociación gremial y se anuncia con unas seis semanas. |
| Última semana de noviembre | Segundo evento de descuentos de alcance internacional. | Congelamiento adicional de una semana. |
| Segunda semana de mayo | Día de la Madre. Peak corto y muy concentrado en la venta presencial. | Congelamiento de una semana. |
| Última semana de enero a primera de marzo | Vuelta a clases. Peak sostenido en categorías específicas. | Congelamiento del período. |
| 2029 | Vencimiento del último hito del plan de remediación instruido por la autoridad del mercado financiero. | Su incumplimiento tiene consecuencias para la filial emisora, que aporta el 10 % de los ingresos y una parte mayor del resultado. |
| 2029 | Fin de soporte de la plataforma de originación y cobranza de créditos, en operación desde 2011. | Coincide con el hito anterior. La migración involucra 620.000 clientes con saldo y Operaciones en curso. |
| En curso | Procedimiento abierto por la autoridad de protección del consumidor a raíz de las 2.840 cancelaciones de junio. | Su resultado puede imponer obligaciones adicionales durante la ejecución del proyecto. |
| Anual | Renovación de los acuerdos con los 310 vendedores de marketplace y con los proveedores de última milla | Oportunidad natural para incorporar niveles de servicio medidos, hoy inexistentes. |
| 2031 — 2033 | Evaluación de abrir tres tiendas y un tercer centro de distribución en el norte. | No es seguro. Si ocurre, el CLIENTE espera incorporarlos sin rehacer la solución. |

### 13.3 Estrategia de puesta en producción esperada

El CLIENTE no impone una estrategia de implantación, pero sí declara las condiciones que cualquier estrategia debe respetar:

1. Nada entra en producción sin haber convivido con la forma actual de trabajar durante la marcha blanca correspondiente, con conciliación entre ambas y con la posibilidad de volver atrás.
2. Ninguna actividad puede impedir que una tienda venda y cobre, ni interrumpir la operación de un centro de distribución en día hábil.
3. a producción no puede ocurrir dentro de ninguna de las ventanas de congelamiento del numeral 132.
4. El despliegue debe poder hacerse por tienda, por proceso o por categoría de producto, y no como un único evento sobre 22 tiendas, 2 centros de distribución y cuatro canales.
5. La migración de la cartera de crédito exige convivencia real, conciliación diaria de saldos, un procedimiento de retorno probado y un plan de comunicación a 620.000 clientes con saldo. No admite una fecha de corte única sin respaldo.
6. Todo cambio que afecte la disponibilidad publicada debe probarse primero en un subconjunto acotado de categorías, midiendo la tasa de cancelación antes y después.
7. La separación de datos entre retail y negocio financiero debe estar implementada y verificada antes de que se construya cualquier vista unificada de cliente.
8. La capacitación debe considerar una rotación anual del 62 %, la incorporación de 1.900 personas de temporada en pleno congelamiento, y la existencia de 1.100 personas externas en sala sobre las que no hay vínculo laboral.
9. posterior a cada paso a producción debe tener dotación y duración declaradas, y contemplar presencia en tienda en horario de venta, incluidos fines de semana.
10. El plan debe declarar qué hace la solución en el evento anual de comercio electrónico durante cada año del proyecto, incluida la posibilidad de congelar deliberadamente componentes ya desplegados.

> El CLIENTE hace cuatro promesas cada día: que el producto existe, que el precio es el exhibido, que la entrega llega en la fecha ofrecida y que las condiciones del crédito son las informadas. Las cuatro se apoyan hoy en registros que la propia compañía sabe imprecisos, y ninguna de las cuatro puede acreditarse después. Un error durante la marcha blanca no se traduce en un dato mal registrado: se traduce en un cliente al que se le cobró algo que no existía, o en un consentimiento que no se puede probar ante una autoridad. La estrategia de puesta en producción pesa, en la evaluación de este caso, tanto como la arquitectura.

# Título V. Antecedentes para el dimensionamiento

## Capítulo 14. VOLUMETRÍA: LO QUE SE ENTREGA Y LO QUE SE DEBE ESTIMAR

El CLIENTE entrega los volúmenes que efectivamente conoce, porque son los que gobierna su operación. Los volúmenes propios del dimensionamiento de un sistema —concurrencia, transacciones por segundo, almacenamiento, integraciones— no los conoce, y no tiene por qué conocerlos: derivarlos es trabajo de ingeniería del PROPONENTE.

> Las celdas marcadas como «a estimar» deben completarse en la propuesta con el valor estimado, el método de estimación y los supuestos empleados. Entregar la propuesta con esas celdas vacías, o con valores sin derivación, se evaluará como dimensionamiento no realizado.

### 14.1 Volumetría operacional entregada por el CLIENTE

| Dimensión | Valor actual | Proyección a 3 años |
| --- | --- | --- |
| Tiendas | 22 | hasta 25 |
| Centros de distribución | 2 | 3 |
| Referencias activas propias | 268.000 | ≈ 310.000 |
| Referencias de vendedores de marketplace | 190.000 | ≈ 340.000 |
| Proveedores propios y vendedores de marketplace | 940 y 310 | 1.050 y 520 |
| Documentos de venta emitidos al año | ≈ 31.000.000 | ≈ 36.000.000 |
| Líneas de venta al año | ≈ 71.000.000 | ≈ 83.000.000 |
| Pedidos del canal en línea al año | ≈ 1.900.000 | ≈ 3.100.000 |
| Pedidos en los 3 días del evento anual | 104.000 | ≈ 150.000 |
| Devoluciones al año, todos los canales | ≈ 620.000 | ≈ 780.000 |
| Cambios de precio al año | ≈ 14.000.000; hasta 400.000 en un día de campaña | ≈ 17.000.000 |
| Puntos de exhibición física de precio | ≈ 310.000 etiquetas en 22 tiendas | ≈ 360.000 |
| Líneas de caja | 380 | 430 |
| Tarjetas emitidas y con saldo vigente | 1.380.000 y 620.000 | 1.700.000 y 760.000 |
| Transacciones de venta pagadas con la tarjeta propia al año | ≈ 11.800.000 | ≈ 14.000.000 |
| Evaluaciones crediticias en el punto de venta al año | ≈ 520.000, entre aperturas y ampliaciones de cupo | ≈ 640.000 |
| Repactaciones al año | ≈ 46.000 | ≈ 52.000 |
| Gestiones de cobranza al año | ≈ 2.900.000 | ≈ 3.400.000 |
| Estados de cuenta emitidos al mes | 620.000 | 760.000 |
| Terminales móviles compartidas en sala | 640, para 3.820 vendedores | por definir |
| Cámaras de videovigilancia | 1.840 | 2.100 |
| Personal con acceso a sistemas | ≈ 6.400, hasta 8.300 en peak | 7.200, hasta 9.400 |
| Altas y bajas de acceso al año, por rotación y temporada | ≈ 6.100 | ≈ 7.000 |
| Repositores externos de proveedores en sala | ≈ 1.100 personas | ≈ 1.300 |

### 14.2 Volumetría de sistema que el proponente debe estimar

| Dimensión | Valor |
| --- | --- |
| Transacciones por segundo en régimen normal | A estimar y declarar como supuesto |
| Transacciones por segundo en el peak del primer día del evento anual de comercio electrónico | A estimar y declarar como supuesto |
| Consultas de disponibilidad por segundo en ese peak, y personas concurrentes en el canal digital | A estimar y declarar como supuesto |
| Transacciones por segundo en el peak de un sábado de diciembre, sumando las 380 líneas de caja | A estimar y declarar como supuesto |
| Evaluaciones crediticias por segundo en el peak del punto de venta | A estimar y declarar como supuesto |
| Eventos por segundo durante una carga masiva de precios de campaña | A estimar y declarar como supuesto |
| Volumen de mensajes de sincronización de existencia entre 22 tiendas, 2 centros de distribución y 4 canales | A estimar y declarar como supuesto |
| Volumen anual de almacenamiento transaccional | A estimar y declarar como supuesto |
| Volumen anual de almacenamiento de la trazabilidad del precio publicado por canal | A estimar y declarar como supuesto |
| Volumen de almacenamiento de las grabaciones y evidencias de consentimiento, conservadas por el plazo del crédito y el período posterior exigido | A estimar y declarar como supuesto |
| Volumen total de datos históricos a migrar desde el sistema central de 2009 y desde la plataforma de crédito de 2011 | A estimar y declarar como supuesto |
| Número de integraciones tras el rediseño y volumen de mensajes por integración | A estimar y declarar como supuesto |
| Ancho de banda por tienda y por centro de distribución | A estimar y declarar como supuesto |
| Volumen de datos generado por una tienda durante 8 horas sin enlace hacia el exterior | A estimar y declarar como supuesto |
| Tiempo de sincronización de una tienda tras 8 horas de operación desconectada | A estimar y declarar como supuesto |
| Contactos mensuales a la mesa de ayuda, distinguiendo personal interno de clientes y de vendedores de marketplace | A estimar y declarar como supuesto |
| Dotación de la mesa de ayuda y del equipo de operación, considerando que el CLIENTE aporta 46 personas para 9 plataformas | A estimar y declarar como supuesto |

> Preste atención a tres particularidades del perfil de carga de este caso. La primera es que hay dos peaks de naturaleza distinta y en épocas distintas: el evento de comercio electrónico, que es digital, brutal, de tres días y de fecha fijada por un tercero; y la campaña de Navidad, que es presencial, sostenida durante dos meses y distribuida en 380 líneas de caja. Dimensionar para uno no resuelve el otro. La segunda es que el volumen de eventos de precio —hasta cuatrocientos mil en un día de campaña, propagándose a las cajas, al canal digital y a trescientas diez mil etiquetas— es una carga que hoy no se mide y que ninguna de las nueve plataformas fue diseñada para sostener. La tercera es que la conservación de la evidencia de consentimiento por el plazo del crédito más el período posterior exigido implica un horizonte de almacenamiento de una década, con requisitos de integridad y recuperabilidad que no se parecen a los del resto de la operación.

## Capítulo 15. PARÁMETROS DEL CASO PARA LOS REQUISITOS «SEGÚN CASO»

Las Bases Técnicas Transversales marcan un conjunto de requisitos como «Según caso»: son obligatorios, pero su valor concreto lo fija cada industria. Los valores para el Caso 09 son los siguientes. Cuando este capítulo endurece un umbral del documento transversal, prevalece el más exigente.

| Código | Materia | Valor para el Caso 09 |
| --- | --- | --- |
| RT-02.12 | Replicación a nuevas unidades | Exigible. La compañía evalúa abrir tres tiendas y un tercer centro de distribución entre 2031 y 2033. La solución debe admitir una tienda nueva, con sus líneas de caja, su bodega, su mesón financiero y su rol en el cumplimiento de pedidos en línea, por parametrización y en un plazo compatible con una apertura comercial. |
| RT-03.10 | Operación desconectada del componente on-premise | Mínimo 8 horas continuas de operación de una tienda sin enlace hacia el exterior: venta, cobro, aplicación de promociones vigentes, emisión de documentos y consulta de la existencia local. El centro de distribución principal: mínimo 4 horas. El comportamiento del otorgamiento de crédito en modo desconectado es una decisión pendiente del numeral 16.1 y debe resolverse y fundamentarse, no omitirse. |
| RT-03.13 | Sincronización tras la reconexión | No debe superar 30 minutos tras 8 horas de desconexión, sin pérdida de ninguna venta ni de ningún documento, y con resolución determinista de la existencia comprometida en otros canales durante la desconexión. |
| RT-03.24 | Red de los sitios operacionales | Exigible la segregación efectiva de la red de cajas, la red administrativa, la red de videovigilancia y la red inalámbrica de clientes en las 13 tiendas donde hoy no existe. Exigible un enlace de respaldo en las 14 tiendas que dependen de un centro comercial y en Coyhaique. Exigible, además, la separación acreditada de la red y del ámbito de sistemas de la filial emisora respecto del retail. |
| RT-05.10 | Retención de datos históricos y de auditoría | Documentos tributarios y antecedentes de venta: 6 años. Antecedentes del crédito —evaluación, información precontractual entregada, aceptación, repactaciones, comunicaciones y gestiones de cobranza—: por todo el plazo del crédito y 6 años más. Grabaciones y demás soportes del consentimiento de originación y de repactación: el mismo plazo, sustituyendo la práctica actual de 90 días. Antecedentes de prevención de lavado de activos: conforme a la normativa aplicable. Trazabilidad del precio publicado en cada canal: 3 años. Movimientos de inventario, conteos cíclicos y ajustes: 6 años. Datos de fidelización: mientras dure la relación y 2 años más. Videovigilancia: 30 días. |
| RT-05.15 | Datos históricos a migrar | Maestro de artículos completo, con auditoría y completitud de atributos. Inventario al momento del corte, con conteo físico total o con una estrategia de corte declarada y fundamentada. Venta: 6 años. Cartera de crédito completa: saldos, cuotas, repactaciones, garantías, cobranzas y juicios en curso de 620.000 clientes con saldo. Pedidos del canal en línea: 3 años. Padrón de clientes deduplicado. Vendedores de marketplace y su histórico de liquidaciones. El sistema central data de 2009 y la plataforma de crédito de 2011; no existe documentación completa de sus 14 integraciones. |
| RT-05.23 | Estándares sectoriales de intercambio | Estándares de identificación y catálogo de producto aplicables al comercio minorista. Estándares de intercambio de órdenes, avisos de despacho y facturación con los 940 proveedores. Estándares de intercambio con transportistas de última milla. Estándar de sincronización de catálogo, existencia y pedido con los vendedores de marketplace. Formato de boleta y factura electrónica. Formatos de reporte a la autoridad del mercado financiero y presentación normalizada del costo total del crédito. El PROPONENTE deberá identificar cada uno por su denominación y justificar su elección. |
| RT-05.29 | Latencia de la capa analítica | Disponibilidad publicada: actualizada no más de 30 segundos después de una venta en cualquier canal. Precio en las 380 líneas de caja y en el canal digital: no más de 5 minutos desde el cambio. Estado de un pedido: en tiempo real y consistente en todos los canales. Indicador de exactitud de inventario por categoría: actualización diaria. Posición consolidada del negocio financiero: disponible antes de las 07:00 del día siguiente. |
| RT-06.01 | Tipología del emplazamiento on-premise | Centro de datos propio de 140 m² habilitado en 2011 con sala de respaldo en la misma comuna; su brecha respecto del Capítulo 6 del documento transversal está documentada en un informe interno de 2024 que el CLIENTE entregará. Gabinete por tienda dimensionado para sostener RT-03.10. Para el ámbito de la filial emisora se exige separación acreditada, física o lógica, con su justificación técnica y su verificación. |
| RT-09.01 | Transacción operacional crítica | Consulta de disponibilidad en la ficha de producto del canal digital: no superior a 400 milisegundos. Confirmación de un pedido durante el evento anual: no superior a 3 segundos. Venta completa en caja con medio de pago externo: no superior a 25 segundos. Evaluación crediticia en el punto de venta: no superior a 8 segundos. Propagación de un cambio de precio a las 380 líneas de caja y al canal digital: no superior a 5 minutos. Consulta de existencia desde una terminal de sala: no superior a 2 segundos, indicando el grado de confianza del dato. Registro de una devolución en el mesón: no superior a 60 segundos. |
| RT-09.02 | Concurrencia y volumen de transacciones | El PROPONENTE lo deriva de la volumetría del numeral 14.1, considerando los dos peaks de naturaleza distinta descritos en el numeral 14.2, y lo declara conforme a ese numeral. |
| RT-10.05 | Ventana operacional protegida | Congelamiento del 1 de noviembre al 6 de enero; durante los tres días del evento anual de comercio electrónico y la semana previa; durante el evento de descuentos de fines de noviembre; en la semana del Día de la Madre; y entre la última semana de enero y la primera de marzo. La fecha del evento anual la fija la asociación gremial y se anuncia con unas seis semanas: el plan debe absorberla sin desplazar hitos contractuales. |
| RT-11.10 | Cifrado a nivel de campo | Exigible para los datos de identificación de clientes, para los antecedentes de la cartera de crédito y el comportamiento de pago, para los antecedentes de evaluación crediticia y para todo dato asociado a medios de pago, que además no debe almacenarse sino tokenizarse. El comportamiento de pago recibe tratamiento reforzado por ser información recogida en el ámbito del negocio fiscalizado. |
| RT-12.11 | Autenticación en el perfil operacional | Rotación anual del 62 % y 1.900 incorporaciones de temporada. 640 terminales compartidas para 3.820 vendedores y líneas de caja operadas por varias personas en un mismo turno. Aproximadamente 1.100 repositores externos sin vínculo laboral con la compañía. En el ámbito de la filial emisora se exige además segregación de funciones verificable entre originación, aprobación, modificación de condiciones y cobranza. |
| RT-12.12 | Personas usuarias externas | Clientes compradores y titulares de tarjeta; los 310 vendedores de marketplace; los 940 proveedores; las empresas de transporte de última milla; los repositores externos, en lo que corresponda; y la autoridad fiscalizadora del mercado financiero y la de protección del consumidor, en lo que la normativa disponga. |
| RT-13.08 | Interfaces de terreno y de atención | Sala de venta con terminal compartida y con el cliente esperando. Línea de caja con fila detrás, resolviendo simultáneamente cobro, promoción y, en el 38 % de los casos, una operación de crédito. Mesón financiero con obligaciones de información que deben cumplirse en un entorno comercial. Bodega y andén de tienda con personal que no fue contratado para preparar pedidos. Centro de distribución con lectores y terminales. Toda interfaz destinada al vendedor debe considerar que su remuneración tiene componente variable y que cada segundo adicional compite con su ingreso. |
| RT-13.12 | Idioma y lenguaje de las comunicaciones | Español obligatorio. Y, con carácter obligatorio y por sobre lo que exige el documento transversal, toda comunicación relativa al crédito —información precontractual, contrato, estado de cuenta, aviso de mora y oferta de repactación— debe cumplir criterios verificables de lenguaje claro, validados con personas usuarias reales y no sólo con revisión legal. |
| RT-15.02 | Certificaciones sectoriales del adjudicatario | Conocimiento acreditado de la normativa aplicable a emisores de tarjetas de casa comercial y de las obligaciones de información al consumidor financiero. Experiencia comprobable en inventario omnicanal y en cumplimiento de pedidos desde tienda. Experiencia comprobable en migración de carteras de crédito vivas. |
| RT-16.09 | Registro de consultas a información sensible | Exigible sobre el acceso a la cartera de crédito, al comportamiento de pago y a los antecedentes de evaluación crediticia. Exigible además, con carácter específico de este caso, el registro de todo cruce de información entre el ámbito del retail y el de la filial emisora, indicando qué dato cruzó, con qué finalidad, con qué base y quién lo autorizó. |
| RT-16.14 | Firma electrónica | Exigible en la apertura de la tarjeta y en la aceptación de la información precontractual, en toda repactación o modificación de condiciones del crédito, en la conformidad de recepción de mercadería del proveedor y en la constancia de devolución entregada al cliente, en la modalidad que la normativa admita para cada caso. |
| RT-16.21 | Canales de notificación | Aviso al cliente ante cada cambio de estado de su pedido y, en particular, aviso de indisponibilidad antes de efectuar el cobro y no después. Comunicaciones de cobranza dentro de los límites y en los medios que la normativa permite, con registro íntegro de cada envío. Aviso al vendedor de marketplace ante una devolución recibida en tienda. Alerta interna cuando la exactitud de inventario de una categoría cae bajo el umbral definido, con capacidad de suspender su publicación. |
| RT-16.30 | Portal público | Obligatorio. Sin autenticación: catálogo con precio vigente y disponibilidad indicada por tienda y para despacho, información precontractual del crédito con simulador de costo total y carga anual equivalente, y consulta del estado de un pedido con su número. Autenticado: cuenta del cliente con sus compras, sus devoluciones, su estado de cuenta y sus documentos; portal del vendedor de marketplace con el estado de cada pedido, las devoluciones y su evaluación; y portal del proveedor con órdenes y recepciones. |
| RT-17.01 | Aplicación móvil | Exigible en cinco perfiles: cliente, con compra, seguimiento del pedido, devolución y estado de cuenta; vendedor de sala, con consulta de existencia que informe su grado de confianza, en terminal compartida y en no más de 2 segundos; preparación de pedidos en tienda; conteo cíclico y prevención de pérdidas; y recepción de mercadería en tienda y en centro de distribución. Los perfiles internos deben operar sin conexión conforme a RT-03.10. |
| RT-17.06 | Periféricos a integrar | Lectores de código en las 380 líneas de caja y en sala; las 640 terminales móviles compartidas; impresoras de etiqueta de precio en las 22 tiendas; terminales de pago y el equipamiento de emisión de la filial; lectores y terminales del centro de distribución principal; el equipamiento que requiera el centro de Concepción si se incorpora a un sistema de gestión de almacenes; y las 1.840 cámaras de videovigilancia. |
| RT-21.06 | Horario del centro de atención | De 09:00 a 23:00 todos los días del año para la operación de tiendas y centros de distribución. 24x7x365 para el canal digital y para los servicios del negocio financiero que afecten a pagos, estados de cuenta y bloqueo de tarjetas. Cobertura reforzada durante todas las ventanas de congelamiento del numeral 13.2, que son también los períodos de mayor venta. |
| RT-21.16 | Traslado a sitios alejados | Exigible. 22 tiendas en 11 regiones, entre Arica y Coyhaique. Coyhaique tiene además la logística de abastecimiento más larga de la cadena y un enlace único sin respaldo. |
| RT-22.04 | Restricción de la capacitación | Rotación anual del 62 % en el personal de venta y caja. 1.900 incorporaciones de temporada concentradas en noviembre y diciembre, que son período de congelamiento. Aproximadamente 1.100 personas externas en sala sobre las que no existe vínculo laboral. El personal del ámbito financiero requiere además capacitación normativa acreditable y renovable. |

## Capítulo 16. LO QUE ESTE DOCUMENTO DELIBERADAMENTE NO RESUELVE

Las decisiones que siguen son necesarias para que la solución sea coherente. El CLIENTE no las ha tomado, y no las va a tomar por el PROPONENTE. Resolverlas, dejarlas escritas como supuesto y hacerse cargo de sus consecuencias en la arquitectura, en el alcance y en el costo forma parte del trabajo profesional que se licita.

### 16.1 Decisiones de diseño pendientes

| N? | Decisión no tomada | Por qué importa |
| --- | --- | --- |
| 1 | Cuál es la fuente única de verdad de la existencia y cómo se calcula el «disponible para vender» sobre un registro que se sabe errado en un 12,4 %, con qué margen y con qué diferencia por categoría y por punto. | Es la decisión de arquitectura más importante del caso. No se trata de corregir el dato, sino de diseñar una promesa que se pueda cumplir sobre un dato imperfecto. |
| 2 | Qué se hace con el sistema central de 2009 y con las 14 integraciones punto a punto de 6 proveedores, cuyo mapa completo nadie conoce. | El problema no es una plataforma sino el tejido entre nueve. Levantar ese mapa es parte del trabajo y no una entrega previa del CLIENTE. |
| 3 | Qué es un cliente único cuando la misma persona es compradora en cuatro canales y deudora de una filial fiscalizada, y qué identificador los relaciona. | Sin esto no hay vista de cliente; con esto mal hecho se vulnera la frontera entre los dos negocios. |
| 4 | Qué datos pueden cruzar entre el ámbito del retail y el de la filial emisora, en qué dirección, con qué base y con qué control técnico que lo impida cuando no corresponda. | La contralora exige definirlo antes de construir cualquier vista unificada. Si primero se construye y después se separa, no se separa nunca. |
| 5 | Cómo se acredita el consentimiento de una repactación y de una apertura de tarjeta: en qué soporte, con qué contenido mínimo y con qué mecanismo de recuperación a diez años. | Es el origen de los 1.240 casos sin evidencia y del plan de remediación con hito en 2029. |
| 6 | Cómo se registra que la información precontractual del crédito fue entregada, en qué versión y antes de la aceptación, sin agregar tiempo al mesón nia la caja. | Cumplimiento exige que el proceso haga imposible saltarse el paso; el vendedor advierte que si el proceso se alarga dejará de ofrecer la tarjeta. |
| 7 | Qué ocurre en caja cuando no hay enlace y hay que decidir si se otorga crédito contra un cupo preaprobado en caché, con qué límite y con qué riesgo asumido. | La restricción no negociable N° 5 exige seguir vendiendo, y el crédito es el 38 % de la venta de tiendas. |
| 8 | Cuál es el precio válido cuando difieren la etiqueta de sala, la caja y el canal digital, quién responde y qué hace el sistema al detectar la diferencia. | Es la infracción detectada en febrero, y la respuesta obvia — cobrar el menor— tiene consecuencias que hay que dimensionar. |
| 9 | Cómo se propaga un cambio de precio a los puntos de exhibición física: etiqueta electrónica, cambio manual con verificación, o restricción de la frecuencia de cambio en sala. | Son 310.000 etiquetas en 22 tiendas y hasta 400.000 cambios en un día de campaña. Cada alternativa tiene un costo muy distinto. |
| 10 | Cómo se conserva y se recupera la evidencia de qué precio estaba publicado en cada canal en un instante determinado. | Hoy la compañía no puede contestarle a un cliente ni a un fiscalizador, ni a favor ni en contra. |
| 11 | Qué se hace con un pedido aceptado y cobrado cuya unidad no existe: cancelar, sustituir por un equivalente, adquirir a un tercero, o entregar fuera de plazo con compensación. | Fueron 2.840 casos en tres días y el procedimiento está abierto ante la autoridad. |
| 12 | Cómo y por cuánto tiempo se reserva la existencia durante el carro de compra, y qué ocurre al expirar. | Determina cuánto se sobrevende y cuánto se deja de vender, y su efecto se multiplica en el evento anual. |
| 13 | Con qué criterio se decide desde dónde se despacha un pedido: centro de distribución, tienda más cercana, tienda con mayor existencia o menor costo total. | Hoy la regla es la distancia y su consecuencia es que el 17 % de los pedidos vacía la sala de venta. |
| 14 | Cómo se reconoce al vendedor y a la tienda la unidad que sale para cumplir un pedido de otro canal. | Sin resolverlo, la unidad seguirá no apareciendo, y eso no es un problema de sistema sino de incentivo. |
| 15 | Cómo se atiende en tienda la devolución de un producto de marketplace: qué se le entrega al cliente, quién asume el costo y cómo se le informa al vendedor externo. | Hoy no hay regla escrita y la mercadería queda en una bodega sin que su dueño lo sepa. |
| 16 | Con qué reglas se evalúa a los 310 vendedores de marketplace, qué consecuencia tiene una mala evaluación y quién la aplica. | El cliente no distingue al vendedor externo de la compañía, pero la compañía responde igual. |
| 17 | Cómo se separa la merma en sus componentes — pérdida física, daño no registrado, error de recepción, devolución mal reintegrada y error de digitación— y qué se hace con cada uno. | Son $ 7.800 millones tratados como un solo problema, y prevención sostiene que buena parte no es robo. |
| 18 | Con qué frecuencia y con qué método se cuenta cada categoría sin cerrar la tienda, y qué gatilla un recuento extraordinario. | De ello depende conocer y mejorar el 12,4 %, y también poder confiar más en unas categorías que en otras. |
| 19 | Cómo se controla el acceso y la actividad de 1.100 repositores externos que no son trabajadores de la compañía y a quienes no se les puede imponer una herramienta. | Están en la sala todos los días, mueven mercadería y no aparecen en ningún registro. |
| 20 | Qué se hace con el centro de distribución de Concepción, que opera con planillas: se incorpora al sistema de gestión de almacenes, se le da una solución propia, o se mantiene como está. | Abastece al sur y su inexactitud entra directamente en el registro nacional de existencia. |
| 21 | Cómo se atiende la garantía legal en el mesón sin derivar al cliente, y cómo se recupera después con el fabricante o con el vendedor de marketplace. | La normativa no admite la derivación y hoy el proceso completo consiste en derivar. |
| 22 | Cómo se gestiona el derecho a retracto de las compras a distancia, su plazo, su devolución y su efecto sobre el inventario. | Hoy se resuelve caso a caso y su reingreso al registro es una de las causas conocidas de diferencia. |
| 23 | Qué se degrada, en qué orden y con qué criterio durante el evento anual de comercio electrónico, y quién tiene la facultad de suspender la publicación de una categoría. | La fecha la fija un tercero y el volumen es siete veces el normal. Improvisar esa decisión durante el evento es exactamente lo que ocurrió. |
| 24 | Cómo se habilitan y se revocan ≈ 6.100 accesos al año, con 62 % de rotación y con 1.900 incorporaciones concentradas en el período de congelamiento. | Cada baja no revocada es un acceso vigente a una caja o a la cartera de crédito. |
| 25 | Cómo se migra una cartera viva de 620.000 clientes con saldo, cuotas, repactaciones y cobranzas en curso, con qué estrategia de corte y con qué plan de retorno. | Es la operación de mayor riesgo del proyecto y sus dos plazos —el fin de soporte y el hito de remediación— vencen el mismo año. |

Esta lista no es exhaustiva. Encontrar los demás vacíos es parte del ejercicio, y el PROPONENTE que identifique vacíos no listados aquí será evaluado favorablemente por ello.

### 16.2 Materias que el proponente deberá investigar

El CLIENTE no espera que el PROPONENTE conozca el comercio minorista ni el crédito de casa comercial. Sí espera que los estudie. Las siguientes materias no se explican en este documento:

- Gestión de inventario omnicanal: exactitud de registro, conteo cíclico, disponible para prometer y existencia de seguridad por canal.
- Modelos de cumplimiento de pedidos: despacho desde centro de distribución, desde tienda y retiro en tienda, con sus reglas de asignación y su costo total de servir.
- Maestro de artículos en vestuario y electrohogar: jerarquía, atributos, explosión por talla y color, y calidad de datos como condición para vender en línea.
- Gestión de precios y promociones: propagación multicanal, etiquetado físico y etiqueta electrónica, y normativa de información del precio al consumidor.
- Ley del consumidor: garantía legal, derecho a retracto, prohibición de derivar al consumidor y formación del consentimiento electrónico.
- Régimen y fiscalización de los emisores de tarjetas de crédito no bancarias, incluida la tasa máxima convencional.
- Obligaciones de información al consumidor financiero: información precontractual, contenido mínimo del contrato, costo total y carga anual equivalente.
- Repactación de deudas: consentimiento expreso e informado, información previa y formas de acreditación admitidas.
- Cobranza extrajudicial: límites a los gastos, a las comunicaciones y a las prácticas admisibles, y prevención de lavado de activos aplicable a emisores de crédito.
- Protección de datos personales aplicada al perfilamiento comercial y al uso del comportamiento de pago obtenido en un negocio regulado.
- Norma de seguridad de medios de pago aplicada a cajas, comercio electrónico y emisión propia de tarjetas.
- Marketplace: intermediación, responsabilidad frente al consumidor, evaluación de vendedores y devoluciones.
- Prevención de pérdidas: composición de la merma y métodos para distinguir el hurto del error administrativo.
- Eventos de venta de alta concurrencia: dimensionamiento, colas de espera, degradación controlada y preparación del inventario.
- Lenguaje claro en comunicaciones financieras: criterios, métodos de validación con personas usuarias y evidencia de cumplimiento.

> Una propuesta que ofrezca «inventario en tiempo real» sin entender que el problema no es la latencia sino la exactitud, o que prometa una vista única de cliente sin notar que la mitad de esos datos pertenecen a un negocio fiscalizado, quedará en evidencia frente a la Comisión de Expertos.

# Título VI. Lo que debe producir el proponente

## Capítulo 17. EL TRABAJO DE TRADUCCIÓN EXIGIDO

Este documento describe una operación y sus problemas. No contiene un catálogo de requerimientos. Construirlo es la primera tarea del PROPONENTE y la que condiciona todas las demás.

### 17.1 De la necesidad al requerimiento

El PROPONENTE deberá recorrer este documento y producir un catálogo de requerimientos trazable a su origen. Cada requerimiento debe indicar de qué párrafo, entrevista, indicador o restricción proviene, de modo que el CLIENTE pueda verificar que nada quedó fuera y que nada se inventó.

| Producto | Contenido esperado |
| --- | --- |
| Catálogo de requerimientos funcionales | Qué debe hacer la solución, expresado en términos verificables, con identificador, descripción, actor, precondición, resultado esperado, prioridad y origen en este documento. |
| Catálogo de requerimientos no funcionales | Desempeño, disponibilidad, seguridad, usabilidad, operabilidad, mantenibilidad, portabilidad y cumplimiento, con umbral numérico y método de verificación. Deben incorporar los parámetros del Capítulo 15 y los requisitos del documento transversal, y distinguir los que aplican al retail de los que aplican a la filial emisora. |
| Registro de supuestos | Toda decisión que el PROPONENTE tomó por el CLIENTE, con su fundamento, su impacto si resulta equivocada y la instancia en que se validará. Incluye obligatoriamente las veinticinco decisiones del numeral 16.1, y en particular la primera, la cuarta y la vigesimoquinta. |
| Registro de reglas de negocio | Las reglas propias del comercio y del crédito que la solución debe respetar y que este documento no explicita: cálculo del disponible para vender, prelación de puntos de despacho, expiración de la reserva de existencia, tratamiento del retracto, base de cálculo de la comisión del vendedor, criterios de evaluación crediticia y reglas de imputación de pagos, entre otras. |
| Matriz de trazabilidad | Correspondencia entre origen, requerimiento, componente de la arquitectura, paquete de la EDT, prueba de verificación y criterio de aceptación. |
| Mapa de integraciones existente | Levantamiento de las 14 interfaces punto a punto actuales, que el CLIENTE no posee y no entregará. Su construcción es parte del trabajo y una de las primeras entregas exigibles. |
| Registro de vacíos y consultas | Aquello que el PROPONENTE no puede resolver por sí solo y que someterá al CLIENTE durante el período de consultas. |

> Un requerimiento no es una frase copiada de este documento. «No se debe vender lo que no existe» no es un requerimiento: es un resultado esperado. El requerimiento indica cómo se calcula el disponible a partir de un registro con error conocido, con qué margen y con qué diferencia por categoría, cómo se reserva la unidad al agregarla al carro, cuándo expira esa reserva, qué ocurre cuando la existencia comprometida no aparece en el punto asignado, en qué momento se le avisa al cliente y —cuestión central en este caso— en qué momento se le cobra.

### 17.2 Distinguir lo funcional de lo no funcional

Buena parte de lo que este documento describe puede leerse de las dos maneras, y la clasificación no es indiferente: determina quién lo verifica, cómo se prueba y en qué momento del proyecto se comprueba. Se ofrecen deliberadamente sin resolver algunos casos limítrofes:

e «La evaluación crediticia debe tomar menos de ocho segundos»: ¿es desempeño, o es funcional porque de ello depende que el vendedor ofrezca la tarjeta y por lo tanto que exista el negocio? e «El consentimiento debe poder acreditarse a diez años»: ¿es retención de datos, es cumplimiento normativo, o es un requerimiento funcional sobre qué se captura en el momento de la aceptación? e «Los datos del retail y los del negocio financiero deben estar separados»: ¿es seguridad, es arquitectura, o es un conjunto de requerimientos funcionales sobre qué consulta puede formularse desde cada ámbito? e «El precio cobrado debe ser el exhibido»: ¿es un requerimiento funcional de propagación, uno no funcional de latencia, o un requerimiento de trazabilidad para poder acreditarlo después? e «La consulta de existencia debe informar su grado de confianza»: ¿es usabilidad, es calidad de datos, o es funcionalidad que el vendedor necesita para decidir qué le promete al cliente? e «El sistema debe soportar el evento anual»: ¿es capacidad, es una estrategia de degradación definida de antemano, o es un requerimiento funcional sobre quién puede suspender la publicación de una categoría y con qué criterio? Se evaluará el criterio con que el PROPONENTE resuelve estos casos y la consistencia con que aplica su propio criterio a lo largo de la propuesta, no la coincidencia con una respuesta preestablecida.

### 17.3 Definir el alcance y su reparto entre etapas

A partir del catálogo, el PROPONENTE deberá delimitar el alcance de la Etapa 1 y de la Etapa 2, declarar las exclusiones y justificar el reparto en función de las dependencias técnicas, del riesgo, de los hitos externos del numeral 13.2 y de la capacidad de absorción del CLIENTE.

La justificación debe hacerse cargo explícitamente de la preferencia del comité del numeral 13.1 y de las dos objeciones registradas allí mismo: que la migración de una cartera viva de seiscientos veinte mil clientes no cabe en un semestre y sus dos plazos vencen en 2029, y que la frontera entre los datos de los dos negocios debe definirse antes de construir cualquier vista unificada de cliente y no después.

### 17.4 Diseñar la arquitectura

La arquitectura lógica y física debe ser propia de este caso y reconocible como tal. Debe hacerse cargo, como mínimo, de los siguientes asuntos, todos ellos derivados de lo descrito en este documento:

1. Cómo se establece la fuente única de verdad de la existencia y cómo se calcula el disponible para vender sobre un registro con error conocido, con margen diferenciado por categoría y por punto.
2. Cómo se reserva y se libera la existencia entre cuatro canales que compiten por las mismas unidades, y qué ocurre en el peak del evento anual.
Ponti ificia Universidad Católica de Valparaíso - Escuela de Informática Bases Técnicas del Caso 09 — Cadena Multitienda

Cómo se rediseñan las 14 integraciones punto a punto entre nueve plataformas de seis proveedores, y en qué orden, sin detener la operación. Cómo se propaga un cambio de precio a 380 líneas de caja, al canal digital y a 310.000 puntos de exhibición física dentro del plazo comprometido. Cómo se conserva y se recupera la trazabilidad del precio publicado en cada canal en cualquier instante de los últimos tres años. Cómo se implementa técnicamente la frontera entre el ámbito del retail y el de la filial emisora, y cómo se registra cada cruce autorizado. Cómo se captura, se protege y se recupera a diez años la evidencia del consentimiento y de la información precontractual entregada. Cómo se logra una evaluación crediticia de ocho segundos en el punto de venta sin omitir ni posponer la entrega de información. Cómo opera una tienda durante ocho horas sin enlace, incluido el comportamiento del otorgamiento de crédito, y cómo se concilia después.

10. Cómo se decide el punto de despacho de cada pedido considerando costo total, disponibilidad real y efecto sobre la sala de venta.
11. Cómo se integra el marketplace de modo que el estado de un pedido sea único para el cliente, para la tienda y para el vendedor externo.
12. Cómo se instrumenta el conteo cíclico y la atribución de la merma a sus causas, sin cerrar la tienda.
13. Cómo se migra una cartera viva de 620.000 clientes con saldo, cuotas, repactaciones y cobranzas en curso, con conciliación diaria y retorno probado.
14. Cómo se sostiene el evento anual de comercio electrónico y qué se degrada, en qué orden, cuando la capacidad no alcanza. Qué crecimiento admite el diseño ante tres tiendas y un tercer centro de distribución, y qué componente se satura primero en cada uno de los dos peaks.

### 17.5 Planificar de forma realista

El lan de trabajo debe ser específico de esta compañía. Un cronograma que podría servir para cualquier proyecto será evaluado como deficiente. En particular deberá reflejar:

El cronograma contractual obligatorio de 56 meses del Artículo 17* de las Bases Administrativas, sin proponer plazos alternativos. Las cinco ventanas de congelamiento del numeral 13.2, que en conjunto ocupan cerca de cinco meses del año en bloques discontinuos. Que la fecha del evento anual de comercio electrónico la fija la asociación gremial y se anuncia con unas seis semanas. El plan debe declarar cuánta holgura reserva para ello y sobre qué base la calculó. El levantamiento del mapa de las 14 integraciones existentes como una de las primeras entregas, y no como una condición previa que el CLIENTE vaya a proveer. La migración de la cartera de crédito de 620.000 clientes con saldo, con sus dos plazos —fin de soporte y hito de remediación— venciendo en 2029. El conteo físico o la estrategia de corte de inventario al momento de la migración, en 22 tiendas y 2 centros de distribución que no cierran. La evaluación, especificación y costeo de la alternativa de etiqueta electrónica frente a las demás formas de resolver la discrepancia de precio.

La eventual incorporación del centro de distribución de Concepción a un sistema de gestión de almacenes, hoy operado con planillas. La capacitación de un personal con 62 % de rotación y 1.900 incorporaciones de temporada que ocurren dentro de un período de congelamiento. La imposibilidad de imponer herramientas o capacitación a los 1.100 repositores externos por la vía laboral. El solapamiento de los meses 13 a 15 y 19 a 20, con la dotación efectivamente necesaria para sostener dos frentes simultáneos en 22 tiendas y 11 regiones.

### 17.6 Proponer una estrategia de puesta en producción y de operación

El CLIENTE hace cuatro promesas cada día y hoy no puede acreditar ninguna. La propuesta deberá contener una estrategia explícita y no una declaración de intenciones:

1. Qué entra en producción primero, en qué tienda o categoría y con qué criterio de avance. Se espera fundamento sobre si conviene empezar por la tienda insignia, por una tienda de calle o por una categoría acotada. Cómo se prueba el nuevo cálculo de disponible en un subconjunto de categorías, midiendo la tasa de cancelación antes y después, antes de aplicarlo a todo el catálogo. Cómo se hace la marcha blanca de la migración de la cartera de crédito: qué se concilia, con qué frecuencia, con qué umbral de discrepancia se detiene el avance y cómo se comunica a 620.000 clientes con saldo. Cómo se verifica que la separación entre los datos del retail y los del negocio financiero está efectivamente implementada, con qué prueba y con qué evidencia auditable. Qué indicadores se medirán durante la marcha blanca y con qué umbral se declara cerrada, conforme al Artículo 17.3 de las Bases Administrativas. Cómo se revierte un paso a producción fallido un sábado de diciembre, con las 22 tiendas vendiendo y el canal digital abierto. Qué dotación de acompañamiento habrá en terreno, en horario de venta y en fin de semana, en 11 regiones simultáneamente. Cómo se capacita a un personal con 62 % de rotación cuyas mayores incorporaciones ocurren en pleno congelamiento, y qué se hace con 1.100 personas externas sin vínculo laboral. Cómo se logra la adopción de un vendedor cuya remuneración variable compite con cada segundo que el proceso agregue, y cómo se verifica que el cumplimiento no depende de su voluntad.
10. Qué hace la solución en cada uno de los eventos anuales de comercio electrónico que ocurrirán durante el proyecto, incluida la posibilidad de congelar deliberadamente componentes ya desplegados.
11. Cómo se transfiere la operación a un equipo de 46 personas y qué queda como servicio permanente del ADJUDICATARIO durante los 36 meses, distinguiendo lo que corresponde al retail de lo que corresponde a la filial fiscalizada.

## Capítulo 18. CRITERIOS DE ACEPTACIÓN DEL CASO

Los siguientes resultados de negocio son los que el CLIENTE utilizará para juzgar si el PROYECTO fue exitoso. El PROPONENTE deberá comprometerse con ellos, proponer la meta cuando este documento no la fije, indicar en qué momento del cronograma se alcanzará cada uno y cómo se medirá.

| N? | Resultado esperado | Situación actual |
| --- | --- | --- |
| 1 | El disponible que se publica incorpora el error conocido del registro y se calcula por categoría y por punto. | Suma de existencias menos un descuento fijo definido en 2019. |
| 2 | Los pedidos cancelados por falta de existencia bajan al umbral comprometido, también durante el evento anual. | 1,9 % en el año; 2,7 % en el evento; 2.840 casos en 3 días. |
| 3 | Ningún cliente es cobrado por una unidad que la compañía no puede entregar. | Se cobró y se devolvió ocho días después. |
| 4 | La exactitud del inventario se mide de forma continua y por categoría, contando sin cerrar la tienda. | Conteo cíclico con 12,4 % de diferencia y sin desglose. |
| 5 | La merma está separada en sus causas: pérdida física, daño, error de recepción, devolución mal reintegrada y error de digitación. | $ 7.800 millones tratados como un solo problema. |
| 6 | Un cambio de precio llega a las cajas, al canal digital y a la sala dentro del plazo comprometido. | Cajas y sitio en minutos; etiqueta hasta 24 horas después. |
| 7 | La compañía sabe, en todo momento, cuántos puntos de exhibición están desactualizados y cuáles. | No existe registro de qué etiqueta se cambió ni cuándo. |
| 8 | Se puede acreditar qué precio estaba publicado en cada canal en un instante determinado. | Inexistente; no se puede responder nia favor ni en contra. |
| 9 | El precio cobrado es el precio exhibido, verificado por muestreo propio y no por fiscalización externa. | 11 % de discrepancia en la fiscalización de febrero. |
| 10 | Un pedido tiene un estado único, consultable por el cliente, la tienda, el mesón, el centro de distribución y el vendedor externo. | Cada canal ve un estado distinto; el mesón no ve los pedidos en línea. |
| 11 | La decisión del punto de despacho considera el costo total y el efecto sobre la sala de venta. | Se decide por distancia. |
| 12 | La tienda que entrega una unidad para un pedido de otro canal recibe el reconocimiento correspondiente. | Inexistente; la unidad a veces no aparece. |
| 13 | La devolución de un producto de marketplace tiene un procedimiento definido y el vendedor externo se entera cuando ocurre. | No hay regla escrita; el vendedor se entera en la liquidación. |
| 14 | Los 310 vendedores de marketplace se evalúan con reglas que ellos conocen y que tienen consecuencia. | No hay acuerdo de nivel de servicio medido. |
| 15 | La garantía legal se resuelve en el mesón sin derivar al cliente al fabricante ni al vendedor externo. | El proceso completo consiste en derivar. |
| 16 | La evaluación crediticia en el punto de venta se resuelve en el umbral comprometido. | Entre 40 segundos y 3 minutos. |
| 17 | Queda registro estructurado de qué información precontractual se entregó, en qué versión y antes de la aceptación. | Una firma en un formulario que se archiva. |
| 18 | Ninguna repactación puede registrarse sin evidencia recuperable del consentimiento informado. | 1.240 casos de 2025 sin evidencia recuperable. |
| 19 | La evidencia del consentimiento se conserva y se recupera por el plazo del crédito y el período posterior exigido. | Grabaciones conservadas 90 días. |
| 20 | El cumplimiento de la entrega de información no depende de la voluntad del vendedor: el proceso impide omitirla. | Depende de que el vendedor tenga tiempo. A |
| 21 | La separación entre los datos del retail y y los de la filial emisora está. implementada, documentada y auditada.. | Parcial y no documentada. |
| 22 | Todo cruce de información entre ambos ámbitos queda registrado con su finalidad, su base y su autorización. | No existe registro. de cruces. |
| 23 | Los hitos del plan de remediación instruido por la autoridad se cumplen antes de 2029. | En curso, con el último ds hito en 2029. |
| 24 | La cartera de 620.000 clientes con saldo migra sin pérdida, sin interrupción y sin divergencia de saldos. | Plataforma de 2011 con fin de soporte en 2029. |
| 25 | El evento anual se enfrenta con una estrategia de degradación definida y con capacidad. de suspender la publicación o de una categoría. | Se improvisó durante el evento. |
| 26 | Doña Paula sabe en qué estado está su pedido sin llamar cinco veces, y si: la unidad: no existe: se le avisa: antes de cobrarle, no ocho días después. | Cinco conversaciones y nadie supo decirle. qué pasó. |
| 27 | Doña Marisol puede demostrar qué parte de la diferencia de su tienda es pérdida física y qué parte es error de registro. | Todo se anota como merma y a ella se la mide por eso. |
| 28 | Don Jonathan abre una tarjeta más rápido que hoy y el cliente recibe la información completa, sin que una cosa dependa de la otra. | \| Tres minutos, y la información se entrega como se puede. |

> Los criterios 26, 27 y 28 parecen anecdóticos y son los tres que mejor resumen el caso. El 26 mide si el PROPONENTE entendió que el daño no fue la cancelación sino la incapacidad de explicarla. El 27 mide si entendió que hay una persona a la que se le mide por un número que mezcla cuatro problemas distintos. Y el 28 es el más exigente de los tres: pide que la rapidez y el cumplimiento dejen de ser una disyuntiva, lo que sólo se logra si el proceso hace imposible omitir un paso en lugar de confiar en que nadie lo omita.

## Capítulo 19. CÓMO SE EVALUARÁ ESTE CASO

La evaluación se rige por el Título V de las Bases Administrativas y por la ponderación del Formulario T-21. Este

capítulo precisa qué se buscará específicamente en el Caso 09 al aplicar esos criterios.

| Ítem | Qué se buscará en este caso |
| --- | --- |
| Comprensión del problema | Que el PROPONENTE entienda que esta compañía es dos negocios con dos regímenes bajo un mismo techo y con un mismo cliente, y que su problema común es que hace cuatro promesas diarias sobre registros que sabe imprecisos y que después no puede acreditar. Que entienda, además, que no existe un sistema legado sino nueve plataformas unidas por catorce interfaces cuyo mapa nadie posee. |
| Esquema de solución y alcance | Que la decisión sobre la fuente única de verdad de la existencia y sobre el cálculo del disponible esté tomada, fundada y costeada. Que la frontera entre los dos negocios esté definida antes que cualquier vista unificada. Que las exclusiones sean explícitas. |
| Arquitectura lógica y física | Que resuelva de forma verificable la reserva de existencia entre cuatro canales, el rediseño de las integraciones sin detener la operación, la propagación de precio a 310.000 puntos de exhibición, la operación de 8 horas sin enlace incluido el crédito, y la separación técnica del ámbito fiscalizado. Que sea propia de esta compañía y no un diagrama de referencia con el nombre cambiado. |
| Modelo y gestión de datos | Que la captura y conservación de la evidencia de consentimiento esté diseñada para un horizonte de una década. Que el cruce de datos entre ámbitos sea controlado y registrado. Que las veinticinco decisiones pendientes del numeral 16.1 estén resueltas y declaradas como supuesto. |
| Plan de trabajo, EDT y cronograma | Que refleje las cinco ventanas de congelamiento, el levantamiento del mapa de integraciones como entrega temprana, el corte de inventario en 24 instalaciones que no cierran, y la migración de la cartera con sus dos plazos venciendo en 2029. Que declare y cuantifique la holgura reservada para la fecha del evento anual. |
| Plan de riesgos | Que los riesgos sean de este proyecto: divergencia de saldos en la migración de la cartera, un evento anual con la solución a medio desplegar, un cruce de datos indebido entre ámbitos, una integración no documentada que aparece en producción, la rotación del 62 % que borra la capacitación, y un vendedor cuya remuneración compite con el proceso que se le pide seguir. |
| Servicios de operación y niveles de servicio | Que el modelo de soporte cubra el horario comercial en 11 regiones y 24x7 el canal digital y los servicios financieros críticos. Que distinga las obligaciones de servicio del retail de las de la filial fiscalizada. Que la dotación esté dimensionada con método considerando que el CLIENTE aporta 46 personas para nueve plataformas. |
| Innovaciones | Que las cinco innovaciones sean pertinentes al comercio minorista y al crédito de casa comercial, y no un catálogo de tecnologías de moda. Que la innovación de modelo de negocio o de contratación considere que una parte del negocio está fiscalizada y no admite cualquier diseño. |
| Consolidación | Que la propuesta sea internamente coherente: que la arquitectura sostenga el alcance, que la EDT contenga la arquitectura, que el cronograma refleje la EDT y que el costo derive de todo lo anterior. |

> Una advertencia final del mandante. En el acta del directorio quedó consignada la condición que la contralora pidió incorporar textualmente: esta compañía es al mismo tiempo una tienda y un emisor de crédito fiscalizado, y ninguna solución que trate esos dos negocios como si fueran uno solo, o que borre la separación entre sus datos, será aceptada, por buena que sea comercialmente. Una propuesta que construya una vista de cliente espectacular cruzando el comportamiento de pago con el historial de compra será superada por una propuesta más sobria que defina primero qué puede cruzar, con qué base y con qué control. En este negocio el error no aparece en un informe de operación: aparece en un requerimiento de la autoridad, tres años después, pidiendo la evidencia de algo que nadie guardó.

# Título VII. Anexos del caso

## Capítulo A. MAPA DE SISTEMAS Y FLUJOS DE INFORMACIÓN ACTUALES

Descripción de los flujos de información tal como ocurren hoy. La columna «cómo viaja» es la que explica buena

parte de los problemas descritos en el Capítulo 7.

| Origen | Destino | Qué información | Cómo viaja hoy |
| --- | --- | --- | --- |
| Comercial | Sistema central de retail | Alta de referencia y sus atributos | Carga manual; nadie audita la completitud |
| Comercial | Sistema central de retail | Precio y mecánica promocional | Planilla y carga masiva; hasta 400.000 cambios en un día de campaña |
| Sistema central | 380 líneas de caja | Precio vigente | Réplica en minutos |
| Sistema central | Canal digital | Precio y catálogo | Interfaz; minutos |
| Sistema central | Bodega de tienda | Lista de etiquetas a cambiar | Impresión al cierre del día; el cambio se hace de noche |
| Bodega de tienda | Nadie | Etiqueta efectivamente cambiada | No se registra |
| Proveedor | Centro de distribución | Mercadería y aviso de despacho | Documento en papel y correo; sin estándar común entre los 940 |
| Centro de distribución principal | Sistema central | Recepción, ubicación y despacho | Sistema de gestión de almacenes desde 2016 |
| Centro de distribución de Concepción | Sistema central | Recepción y despacho | Planillas; la ubicación vive en la memoria de las personas |
| Planificación | 22 tiendas | Propuesta de reposición | Calculada sobre el inventario del sistema, con 12,4 % de error |
| Sistema central | Plataforma de comercio electrónico | Existencia consolidada | Lote nocturno; se publica con un descuento fijo de 2019 |
| Vendedor de marketplace | Plataforma de marketplace | Catálogo y existencia declarada | Sincronización periódica; puede estar desactualizada |
| Plataforma de comercio electrónico | Tiendas y centro de distribución | Pedido asignado a un punto de despacho | Interfaz; la asignación se hace por distancia |
| Tienda | Cliente | Preparación y entrega de pedido en línea | Personal de sala, además de su trabajo, sin compensación al vendedor |
| Cliente | Mesón de atención | Devolución, cambio o garantía legal | Presencial; el mesón no ve los pedidos del canal en línea |
| Mesón de atención | Inventario | Reingreso de producto devuelto | Manual; causa conocida de diferencia de registro |
| Mesón de atención | Fabricante o vendedor de marketplace | Derivación del cliente por garantía | Verbal; la normativa no admite la derivación |
| Vendedor o mesón financiero | Plataforma de crédito | Evaluación, De apertura y cupo | En línea; entre 40 segundos y 3 minutos |
| Mesón financiero | Cliente. | Información precontractual del crédito | Documento impreso; la constancia es una firma archivada |
| Cobranza | Cliente | Oferta y aceptación de repactación | Llamada telefónica grabada; grabación conservada 90 días |
| Plataforma de crédito | Sistema de gestión empresarial | Devengo, provisiones y contabilidad de la cartera | Interfaz por lote |
| Sistema de fidelización | Marketing | Segmentos y campañas | Cruce de datos comerciales y de comportamiento de pago, sin regla documentada |
| Prevención de pérdidas | Sistema central | Ajuste por conteo cíclico | Registro del ajuste; sin atribución de causa |
| 9 plataformas entre sí |  | Todo lo anterior | 14 interfaces punto a punto de 6 proveedores, la mayoría por archivo y lote nocturno; sin mapa completo |

## Capítulo B. CALENDARIO Y PERFIL OPERACIONAL DE REFERENCIA

### B.1 Perfil de un día

| Tramo horario | Qué ocurre | Carga sobre la solución |
| --- | --- | --- |
| 00:00 — 07:00 | Procesos por lote: consolidación de venta, cálculo de reposición, sincronización de existencia con los canales y generación de la lista de etiquetas. | Es la ventana donde hoy ocurre casi toda la integración entre las nueve plataformas, y la razón por la que el estado de un producto difiere según la hora. |
| 02:00 — 06:00 | Cambio de etiquetas de precio en sala, con la lista impresa al cierre. | Cuando la lista trae cientos de cambios, se prioriza y el resto queda para la noche siguiente. |
| 07:00 — 10:00 | Recepción de mercadería en el andén de tienda y preparación de pedidos en línea. | Personal de bodega atendiendo dos flujos con el mismo equipo y el mismo espacio. |
| 10:00 — 13:00 | Apertura y venta de mañana. Flujo bajo y estable. | Ventana natural para conteo cíclico, hoy poco aprovechada. |
| 13:00 — 20:00 | Peak de venta presencial, especialmente los fines de semana. Originación de crédito en mesón y en caja. | Peak de las 380 líneas de caja y del mesón financiero, con evaluación crediticia en línea. |
| 18:00 — 22:00 | Peak del canal digital. | Se superpone parcialmente con el peak presencial: ambos consultan la misma existencia. |
| 20:00 — 23:00 | Cierre de tiendas y cuadratura de caja. | Alimenta la consolidación nocturna. |
| Todo el día | Gestiones de cobranza y atención de titulares de tarjeta. | ≈ 2.900.000 gestiones al año, sujetas a límites normativos de horario y de medio. |

### B.2 Calendario comercial y ventanas

| Período | Efecto | Consecuencia para el proyecto |
| --- | --- | --- |
| 1 de noviembre al 6 de enero | Campaña de Navidad y liquidación de enero. Peak anual de venta presencial, con 1.900 personas de temporada. | Congelamiento total, coincidente con el máximo de personal nuevo en sala. |
| Tres días entre mayo y junio | Evento anual de comercio electrónico. Equivale a 22 días de venta en línea normal. | Congelamiento del evento y de la semana previa. La fecha la fija la asociación gremial con unas seis semanas de aviso. |
| Última semana de noviembre | Evento internacional de descuentos, dentro del congelamiento de Navidad. | Refuerza el bloqueo del período de noviembre y diciembre. |
| Segunda semana de mayo | Día de la Madre. Peak corto y muy concentrado en venta presencial. | Congelamiento a de una semana. |
| Última semana de enero a primera de marzo | Vuelta a clases. Peak sostenido en categorías específicas. | Congelamiento del período. |
| Marzo a abril y julio a octubre | Períodos de venta normal, con cambio de temporada de surtido en marzo y en septiembre. | Únicas ventanas de intervención mayor del año, en dos bloques discontinuos. |
| Dos veces al año | Rotación completa del surtido por cambio de temporada. | Alta de decenas de miles de referencias nuevas y liquidación de las salientes, con impacto directo en el maestro de artículos. |
| Mensual | Emisión de 620.000 estados de cuenta y ciclo de facturación de la tarjeta. | Hito recurrente del negocio financiero que no admite atraso ni error. |

## Capítulo C. GLOSARIO DE LA INDUSTRIA

Vocabulario mínimo para leer este documento. No sustituye la investigación exigida en el numeral 16.2.

| Término | Significado |
| --- | --- |
| Carga anual equivalente | Indicador que expresa el costo total de un crédito en términos anuales, permitiendo comparar ofertas. Debe informarse al consumidor antes de contratar. |
| Conteo cíclico | Recuento periódico de una muestra de referencias sin detener la operación, para medir y corregir la exactitud del inventario. |
| Cumplimiento de pedido | Conjunto de operaciones que llevan un pedido desde su aceptación hasta la entrega: asignación de punto, preparación, despacho y entrega. |
| Derecho a retracto | Facultad del consumidor de dejar sin efecto una compra a distancia dentro del plazo legal, con devolución de lo pagado. |
| Despacho desde tienda | Cumplimiento de un pedido del canal digital utilizando la existencia de una tienda en lugar de la del centro de distribución. |
| Disponible para vender | Cantidad que el sistema considera comprometible frente a un cliente. No es el inventario registrado: es el inventario ajustado por reservas, error conocido y política de riesgo. |
| Estado de cuenta | Documento periódico que informa al titular de una tarjeta sus movimientos, cargos, intereses y saldo adeudado. |
| Exactitud de inventario | Proporción de referencias cuyo registro coincide con el conteo físico. Es el indicador que gobierna la confiabilidad de toda promesa de existencia. |
| Garantía legal | Derecho del consumidor a la reparación, el cambio o la devolución de un producto defectuoso, ejercible directamente ante el vendedor. |
| Información precontractual | Antecedentes que deben entregarse al consumidor antes de contratar un crédito, incluidos el costo total, la carga anual equivalente y los cargos asociados. |
| Maestro de artículos | Registro central de todas las referencias, con sus atributos, jerarquía de categorías y datos logísticos. Su calidad determina qué se puede vender y cómo se despacha. |
| Marketplace | Modelo en que la compañía intermedia la venta de productos de terceros en su propio canal, cobrando una comisión sin adquirir la mercadería. |
| Merma o pérdida desconocida | Diferencia entre el inventario registrado y el existente que no tiene explicación documentada. Mezcla hurto, daño no registrado y error administrativo. |
| Omnicanalidad | Operación en que los canales de venta comparten inventario, precio, cliente y estado de pedido, de modo que la experiencia sea continua entre ellos. |
| Originación | Proceso de evaluar, aprobar y abrir una operación de crédito, incluida la entrega de la información precontractual y la obtención del consentimiento. |
| Referencia | Unidad mínima de identificación de un producto en el maestro de artículos. En vestuario se multiplica por talla y color. |
| Repactación | Modificación de las condiciones de un crédito vigente, habitualmente de plazo y cuota. Constituye un contrato nuevo y requiere consentimiento expreso e informado. |
| Reposición | Envío de mercadería desde el centro de distribución a las tiendas según una propuesta calculada sobre la existencia registrada. |
| Reserva de existencia | Bloqueo temporal de una unidad mientras un cliente completa su compra, para evitar comprometerla dos veces. |
| Retiro en tienda | Modalidad en que el cliente compra en el canal digital y retira el producto en una tienda. |
| Tarjeta de casa comercial | Medio de pago con crédito emitido por una empresa del retail, sujeto a fiscalización de la autoridad del mercado financiero. |
| Tasa máxima convencional | Límite legal a la tasa de interés que puede pactarse en una operación de crédito. |
| Temporada | Ciclo comercial de surtido. En esta compañía el surtido rota completamente dos veces al año. |
| Última milla | Tramo final de la entrega, desde el punto de despacho hasta el domicilio del cliente, habitualmente ejecutado por un tercero. |

