# Cierre J · espacio físico, racks y reservas de implantación

Fecha: 23-10-2026. Estado: diseño inicial de implantación, sin levantamiento ni aceptación humana. Uso de IA: Alto. Complementa [DC/CD](05-dc-cd-externos.md), [tienda](03-tienda.md) e [inventario](../inventario-fisico-integral-2026-10-23.md). Las dimensiones propuestas constituyen requisitos del proyecto; no describen salas medidas.

## Espacio acreditado y límites de la información

El espejo del Caso 09 acredita en cap. 6 un recinto de datos de **140 m²** en casa matriz, habilitado en 2011, y una sala de respaldo en la misma comuna sin superficie informada. El informe interno de brechas de 2024 será entregado por el mandante. En cap. 2.2 describe 22 tiendas (14 en centros comerciales y ocho a la calle), insignia de 14.000 m² en cinco pisos, Coyhaique de 1.800 m² y 96.000 m² de venta en conjunto. Los CD tienen 42.000 m² (RM) y 9.000 m² (Concepción). **Ninguna de esas superficies comerciales/logísticas equivale a una sala técnica disponible.** Cap. 15 precisa gabinete de tienda dimensionado para continuidad y separación acreditada del ámbito financiero.

Trazabilidad de búsqueda: [Caso 09](../../../00_Bases/Caso_09_Cadena_Multitienda.md), cap. 2.2, 6 y 15, líneas 103–113, 324–334 y 798 del espejo. Esta ficha interna no declara folio impreso verificado y no debe trasladarse como cita bibliográfica de oferta sin cotejar el PDF. No se conocen ancho/largo, pilares, altura libre, puertas, rutas de evacuación, capacidad de losa ni ocupación actual del recinto de 140 m². No se afirma que la instalación completa ya cabe.

## Criterio de selección y envolvente

Se eligen gabinetes de piso de 19 pulgadas; 24U para tienda y 42U para DC y 24U para CD. La referencia dimensional, sin imponer marca de compra, es 600 mm de ancho y 1.070 mm de fondo. Las fichas oficiales de Schneider [24U AR3104](https://www.se.com/us/en/product/AR3104/apc-netshelter-sx-server-rack-enclosure-24u-black-1198-5h-x-600w-x-1070d-mm-taa/) y [42U AR3100](https://www.se.com/us/en/product/AR3100/apc-netshelter-sx-server-rack-enclosure-42u-black-1991h-x-600w-x-1070d-mm-taa/) indican alturas aproximadas de 1.199 y 1.991 mm. Consulta: 23-10-2026. AR3100 está reemplazado por AR3100B2; se usa como referencia geométrica, no como producto contratado. El equipo definitivo debe superar comprobación de profundidad, raíles, puertas, peso y ventilación.

Como decisión de distribución se reservan 1,20 m frontales, 1,00 m posteriores y 0,60 m libres en extremos de la fila. Son márgenes de proyecto, **no mínimos normativos certificados**; se incrementan si el fabricante, evacuación o accesibilidad lo exige. Los pasillos no almacenan cajas, combustible ni repuestos. Se instalan puertas perforadas, paneles ciegos y PDU verticales 0U con cableado separado de entrada de aire. Generadores, combustible, condensadores y baterías centrales ocupan zonas propias, no U de servidor.

RT-06.05 obliga a separar racks de cómputo y comunicaciones; se mantiene en todas las tipologías. La separación R/F incluye hosts distintos, redes y administración propias; compartir sala o gabinete de comunicaciones no habilita puertos compartidos entre negocios.

## Tienda tipo: tres racks, cuatro hosts

Se fijan dos gabinetes 24U de servidores (uno R y otro F) y un gabinete 24U de comunicaciones. El gabinete de comunicaciones contiene equipos R y F dedicados, con secciones etiquetadas, paneles y control de acceso; las VLAN no sustituyen la separación de hosts acordada. X-01 aislado reside dentro del par F y no añade un host ni un rack.

| Gabinete por tienda | U iniciales presupuestadas | Libre / crecimiento | Potencia IT de diseño |
| --- | --- | --- | --- |
| SIT-RACK-SRV-R, 24U | Dos hosts de hasta 2U =4U; copia separada/appliance hasta 2U; consola/gestión y reserva técnica 2U: **8U** | 16U (67 %); no reutilizar para F o cámaras | 0,8 kW techo de partida del conjunto R; medir con un host caído |
| SIT-RACK-SRV-F, 24U | Dos hosts de hasta 2U =4U; copia propia hasta 2U; consola/gestión y reserva técnica 2U: **8U** | 16U (67 %); X sin U adicionales | 0,8 kW techo de partida F/X |
| SIT-RACK-COM, 24U | Dos CPE de operador 2U; dos pares SD-WAN/firewall R/F 4U; cuatro switches de distribución R/F 4U; dos paneles fibra/cobre 2U; organizadores 2U; reserva OOB/testigo 1U: **15U** | 9U (37,5 %); switches de acceso adicionales se cuentan aparte por puertos | 0,8 kW sin PoE de acceso; PoE se suma explícitamente |

Son envolventes máximas por familia para elegir productos, no fichas de fabricante certificadas. Un firewall/SD-WAN convergente se cuenta una sola vez. Se incluyen dos pares de edge separados R/F; no reutilizar un par común para reducir el cómputo. PDU A/B 0U en cada rack; UPS y baterías en armario eléctrico externo segregado: sus medidas y peso se agregan al plano y no se descuentan del margen U anterior. No instalar baterías sobre servidores.

Fila: tres racks ×0,60=1,80 m; con extremos de 0,60 m resulta **3,00 m**. Fondo con pasillos: 1,07+1,20+1,00=**3,27 m**; reserva de servicio **9,81 m²**. Se asigna **objetivo mínimo de 12 m² técnicos útiles**, incluyendo una reserva inicial de 2,19 m² para armario UPS/baterías y maniobra; ese remanente debe verificarse con el modelo de baterías, puertas y evacuación. Si no alcanza se amplía el recinto o se ubica energía en un recinto eléctrico separado. No reducir hosts, pasillos o separación para hacerlos caber.

En centro comercial se solicita autorización de recinto, ductos y generador/ATS antes de implantación. La instalación del centro comercial solo se acredita como fuente de respaldo si demuestra capacidad, transferencia y autonomía para la carga de la solución. En tienda a la calle se reserva área exterior segura para generador y combustible; no se supone superficie existente. Coyhaique usa el mismo patrón de cuatro hosts y doble enlace; su menor sala de venta no justifica retirar redundancia.

La insignia requiere estudio de recorridos por cinco pisos e IDF de acceso donde lo exija longitud/puertos. Provisión de diseño: un IDF de comunicaciones por piso servido, gabinete inicial 12U, sin duplicar cómputo R/F en cada piso. El número final puede variar según plano, fibra vertical, rutas separadas y cantidad de dispositivos. No asignar dimensiones comerciales a IDF. Para cada IDF reservar UPS, monitoreo, puesta a tierra y mantenimiento; el PoE de móviles/AP/cámaras pertenece al balance energético y no está incluido en 2,4 kW base.

## DC-01: reserva dentro de 140 m²

Se reserva una fila inicial de **cuatro racks 42U**: dos de servidores segregados R y F, uno de comunicaciones y uno de custodia/backup con compartimientos y claves separados. La producción financiera nueva sigue en la nube. El rack F conserva únicamente infraestructura transitoria acreditada del legado y los servicios de custodia expresamente justificados. No se presupone una nueva cartera operativa local.

| Rack | Ocupación presupuestada de arranque | Reserva |
| --- | --- | --- |
| DC-SRV-R 42U | Dos hosts de integración/virtualización hasta 2U cada uno=4U; reserva de alojamiento legado por levantar 16U; consola 1U: **21U** | 21U libres; las 16U son reserva y no 8 servidores confirmados |
| DC-SRV-F 42U | Dos hosts transitorios hasta 2U=4U; reserva legado F hasta 12U; consola 1U: **17U** | 25U libres; retirar cómputo transitorio tras corte |
| DC-COM 42U | CPE 2U, firewall/SD-WAN 4U, distribución R/F 4U, OOB 2U, paneles 4U, organización 4U: **20U** | 22U libres; rutas y puertos segregados |
| DC-BKP 42U | Custodia/backup R y F hasta 8U cada uno; gestión 2U; conexión a medios transportables 4U: **22U** | 20U libres; no presupone librería ni almacenamiento ya existente |

Total: **80/168U presupuestadas**, 88U libres (52 %); parte de las 80U es reserva para legado desconocido, no ocupación instalada. Huella de gabinetes: 4×0,60×1,07=2,568 m². Envolvente de servicio de fila: (2,40+1,20)×3,27=**11,772 m²**. Este cálculo demuestra que la fila nueva tiene una envolvente reducida respecto de 140 m², pero no demuestra encaje de toda la instalación existente.

Presupuesto de áreas de proyecto, suma 140 m²: sala IT y ampliación 45; UPS/baterías y tableros 18; climatización interior/mantenimiento 10; custodia de medios 10; esclusa/control de acceso 10; operación separada 15; circulación, particiones e incertidumbre 32. Estos números son una asignación de diseño, **no un plano del edificio**. El generador/combustible y unidades exteriores requieren zona exterior autorizada; no están dentro de esos 140 m². Si no existe área exterior, no puede afirmarse cumplimiento espacial: el proyecto civil debe habilitarla o acreditar otra fuente autónoma admisible. El enrolamiento se dispone fuera del recinto técnico. Mantener ruta de acceso de equipos, mantenimiento de UPS y evacuación sin invadir las zonas de control.

DC-02, sala existente de respaldo: dimensiones desconocidas. Reservar funcionalmente dos racks 42U separados (custodia/cómputo y comunicaciones) con envolvente (1,20+1,20)×3,27=**7,848 m²**, más energía, enfriamiento, control de acceso y custodia. **No declarar 8 m² como sala suficiente:** solo es envolvente de esos racks. Dimensionar desde cero con plano y medición. Estar en la misma comuna no acredita independencia ante desastre; Brazil South continúa como recuperación regional.

## Centros de distribución

CD-01 y CD-02: dos gabinetes 24U por centro como reserva inicial (servidores y comunicaciones independientes). Servidores: par local de hasta 2U por host=4U, copia 2U, consola 1U: **7/24U**. Comunicaciones: CPE 2U, edge 2U, switches distribución 2U, OOB 1U, paneles 4U, organización 4U: **15/24U**, ampliar según puertos. Rack adicional R/F solo si se acredita legado que requiera residencia allí; el WMS no implica por sí solo un host en CD.

Envolvente para dos racks: **7,848 m²**; objetivo de sala técnica útil **12 m² más espacio de energía** según carga y batería. Los 42.000/9.000 m² logísticos no garantizan esa reserva. Se proyectan IDF de acceso a lo largo de la nave por distancia, conectados por fibra en rutas distintas; la cantidad y gabinete se determinan en plano de cobertura y puertos. No añadir su PoE a la reserva de distribución sin recalcular autonomía.

## Energía, calor y crecimiento

Para tienda la [ficha de soporte](11-soporte-fisico.md) fija carga IT de **2,57 kW**: cuatro hosts ×0,35=1,40 kW; cuatro SD-WAN ×0,08=0,32; cuatro switches ×0,15=0,60; dos CPE ×0,05=0,10; sensores, quorum y copia=0,15. Añadir una sola vez 30 % da **3,341 kW**, antes de PoE/IDF, cajas y periféricos que deban seguir operando. Cada rama A y B sostiene toda la carga después de falla de la otra. Se adoptan **dos UPS de 6 kVA/6 kW**, cada una con autonomía mínima de **30 min a 6 kW** y baterías externas por curva del producto, envejecimiento y temperatura. La cuenta ideal por rama es 6×0,5=**3 kWh útiles**; a eficiencia provisional 90 % y factor de envejecimiento 80 %, **4,17 kWh nominales por rama**, antes de corrección por descarga/temperatura. Es una cuenta de energía, no selección definitiva de batería. La potencia de 6 kW deja 2,659 kW sobre los 3,341 kW previstos; esa reserva no se consume sin verificar autonomía y calor.

La carga IT base de 2,57 kW produce aproximadamente **8.769 BTU/h**; con margen, 3,341 kW equivalen a **11.400 BTU/h**, usando 3.412 BTU/h por kW. Añadir pérdidas UPS, ocupantes, envolvente y radiación. Se requiere refrigeración continua redundante según tipología contractual, con cada capacidad remanente N cubriendo la carga de diseño. No usar climatización comercial que se apague con la tienda. La ficha de soporte adopta generador inicial de **20 kVA**, sujeto a incluir clima, arranque, carga crítica real, factor de potencia y autonomía de combustible de 24 h. En DC la carga de legado y UPS no está medida: adoptar envolvente IT de **12 kW** como reserva inicial, equivalente a 40.944 BTU/h de calor IT; un PUE objetivo provisional 1,6 da 19,2 kW de instalación. Selección eléctrica/generador y precisión de clima deben verificarse a la carga completa más motores, arranque y condiciones locales. PUE es objetivo, no medición lograda.

Para todos los sitios: capacidad útil de U, potencia, refrigeración, puertos, peso por losa y baterías se verifican separadamente; U libres no prueban capacidad eléctrica. Umbral de ampliación a 70 % de cualquier recurso planificado o pérdida del margen N+1. Mantener paneles ciegos y separar aire frío/caliente; DC adopta contención de pasillo frío donde el plano y sistema contra incendio lo permitan (RT-06.15 deseable). Añadir medición PDU por rama, sensores de agua bajo UPS/clima, temperatura frontal alta/media/baja, humedad y apertura de puerta como mejoras verificables (RT-06.34).

## Evidencia de aceptación de encaje

Antes de comprar: plano acotado con mobiliario/ocupación existente y rutas de evacuación; verificación de todos los equipos por profundidad/peso/U y radios de cable; cálculo estructural del piso y carga puntual de baterías; rutas A/B e ingreso WAN separado; plano de generador/combustible/escape; carga y autonomía reales; balance térmico con falla de una unidad; puesta a tierra; detección/extinción sin obstrucciones. La visita del mandante confirma las medidas que el Caso no entrega. El resultado exigido es un plano con BOM, U, potencia, calor y accesibilidad que conserve los márgenes aquí definidos, no una declaración de cumplimiento basada solo en m².
