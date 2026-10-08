# Condiciones del Caso 13.3 (estrategia de puesta en producción) y su cobertura

> **Nomenclatura (2026-10-07):** los nombres y códigos de los servicios de este documento (R-01 a X-01) fueron reemplazados. Rige `divisiones_negocio_servicios_sd-03.md`, que contiene la tabla de equivalencias.

Documento de contexto, no es entregable. Fuente: `00_Bases/Caso_09_Cadena_Multitienda.md`, numeral 13.3, líneas 706 a 719. El Caso no impone una estrategia, pero declara diez condiciones que cualquiera debe respetar. Actualizado el 2026-10-06.

| N.º | Condición | Cobertura en el sd-03 | Estado |
| :-- | :-- | :-- | :-- |
| 1 | Nada entra en producción sin haber convivido con la forma actual durante la marcha blanca correspondiente, con conciliación y posibilidad de volver atrás | Conciliación: art. 17.3. POS: convivencia y retorno probado en la compuerta (`asignacion_etapas.md`, D2, condición 8) | Cubierta |
| 2 | Ninguna actividad impide que una tienda venda y cobre ni interrumpe un centro de distribución en día hábil | Operación sin conexión de 24 h (1.16, 1.15.19); olas por tienda | Cubierta |
| 3 | El paso a producción no ocurre dentro de ninguna ventana de congelamiento (13.2) | Pasos a producción en los meses 16 y 21; instalaciones en tiendas en ventanas libres, con calendario propuesto (D2) | Cubierta; calendario por confirmar en el sd-07 |
| 4 | El despliegue puede hacerse por tienda, por proceso o por categoría | POS en dos olas, apps en dos olas, cartera por tramos, piloto por categorías | Cubierta |
| 5 | Cartera: convivencia real, conciliación diaria, retorno probado, plan de comunicación, sin corte único | C2, opción B | Cubierta |
| 6 | Todo cambio que afecte la disponibilidad publicada se prueba primero en un subconjunto de categorías, midiendo la tasa de cancelación antes y después | F2 y criterio de 1.20a | Cubierta |
| 7 | La separación de datos Retail–Emisor se verifica antes de construir cualquier vista unificada de cliente | X-01 en la capa 1; prueba de separación de fidelización (1.20b) | Cubierta |
| 8 | La capacitación considera rotación de 62 %, 1.900 personas de temporada en pleno congelamiento y 1.100 externos sin vínculo laboral | 3.7a y 3.7b; los externos se cubren solo con acceso individualizado (1.14c) | Parcial |
| 9 | El acompañamiento posterior a cada paso a producción tiene dotación y duración declaradas, con presencia en tienda en horario de venta, incluidos fines de semana | Sin entregable propio | Pendiente (plan de implantación, sd-07) |
| 10 | El plan declara qué hace la solución en el evento anual de comercio electrónico durante cada año del proyecto, incluida la posibilidad de congelar componentes ya desplegados | Sin entregable propio | Pendiente (plan de trabajo y operación) |
