# Memoria de capacidad (sd-04, 4.2)

Documento de apoyo del subdocumento 4. Responde a las seis primeras de las diecisiete dimensiones que el Caso 09 pide estimar y declarar como supuesto en el capítulo 14, numeral 14.2 (p. 32). Las once restantes se derivan en el diseño detallado de la Etapa 1. Son estimaciones y no mediciones. Se corrigen con el levantamiento y la prueba de carga de la Etapa 1. Para cambiar un supuesto se edita `sd-04_s2_memoria-capacidad.py` y se vuelve a ejecutar.

## Datos de partida del Caso 09

| Dato | Valor |
| :--- | ---: |
| Documentos de venta emitidos al año, proyección a 3 años (p. 31) | 36.000.000 |
| Líneas de venta al año, proyección a 3 años (p. 31) | 83.000.000 |
| Pedidos del canal en línea al año, proyección a 3 años (p. 31) | 3.100.000 |
| Pedidos en los 3 días del evento anual, proyección a 3 años (p. 31) | 150.000 |
| Líneas de caja, proyección a 3 años (p. 31); el numeral 14.2 habla de las 380 de hoy | 430 |
| Evaluaciones crediticias en el punto de venta al año, proyección a 3 años (p. 31) | 640.000 |
| Cambios de precio en un día de campaña (p. 31) | 400.000 |
| Plazo máximo de propagación de precio a cajas y canal digital: 5 minutos (RT-05.29, p. 34) | 300 |

## Supuestos del proponente

| Supuesto | Valor |
| :--- | ---: |
| Las tiendas venden 12 horas al día (inferencia del perfil, que muestra apertura a las 10:00 y cierre entre las 20:00 y las 23:00, apéndice B, núm. B.1, p. 48); los pedidos en línea se cuentan aparte, y si ya están en los documentos de venta la cifra sobrestima | 12 |
| La hora peak normal es 2,5 veces el promedio horario | 2,5 |
| El 50 % de los pedidos del evento cae el primer día | 0,5 |
| La mitad del primer día cae en la franja peak digital | 0,5 |
| Peak digital de 18:00 a 22:00 (apéndice B, núm. B.1, p. 48) | 4 |
| El 10 % de los pedidos del evento llega en los primeros 5 minutos de la apertura | 0,1 |
| Duración de la ráfaga de apertura del evento: 5 minutos | 300 |
| Cada visita hace 50 consultas de disponibilidad durante su sesión | 50 |
| 2 % de las visitas termina en pedido | 0,02 |
| La sesión media dura 4 minutos | 240 |
| Cada línea de caja atiende 60 clientes por hora (uno por minuto) en un sábado de diciembre | 60 |
| El peak de Navidad triplica el promedio diario de evaluaciones crediticias | 3 |
| Peak presencial de 13:00 a 20:00 (apéndice B, núm. B.1, p. 48) | 7 |
| Consumidores de un cambio de precio: cajas, móviles, canal digital, etiquetas y analítica (supuesto; el Caso menciona cajas, canal digital y 310.000 etiquetas, y RT-05.29 fija 5 minutos por cambio, de modo que exigir los 400.000 cambios en ese plazo es una lectura conservadora) | 5 |

## Resultados

| Cifra del Caso 14.2 | Valor | Derivación |
| :--- | :--- | :--- |
| Transacciones por segundo en régimen normal | 2,5 promedio y 6,2 en hora peak | (documentos de venta + pedidos en línea) ÷ (365 días × 12 h × 3.600 s), y la hora peak es 2,5 veces el promedio |
| Transacciones por segundo en el peak del primer día del evento | 2,6 pedidos por segundo sostenidos y 50 en la ráfaga de apertura | 150.000 pedidos × 50 % (primer día) × 50 % (franja de 4 h) ÷ 14.400 s, y 150.000 × 10 % ÷ 300 s en la ráfaga |
| Consultas de disponibilidad por segundo y personas concurrentes en ese peak | 6.510 consultas por segundo y unas 31.250 personas concurrentes | visitas por segundo (pedidos ÷ 2 %) × 50 consultas por visita, y visitas por segundo × 240 s de sesión |
| Transacciones por segundo un sábado de diciembre, sumando las líneas de caja (430 proyectadas, 380 hoy) | 7,2 ventas por segundo y 16,5 líneas por segundo | 430 líneas de caja × 60 clientes por hora ÷ 3.600 s, con 2,3 líneas por documento |
| Evaluaciones crediticias por segundo en el peak del punto de venta | 0,21 por segundo | 640.000 ÷ 365 días × 3 (peak de Navidad) ÷ (7 h × 3.600 s) |
| Eventos por segundo en una carga masiva de precios de campaña | 1.333 publicados y 6.667 entregados por segundo | 400.000 cambios ÷ 300 s (plazo de 5 minutos), y cada cambio llega a 5 tipos de consumidor |

## Uso en el diseño

De estas cifras se derivan en el diseño detallado las unidades de API Management, las particiones de Event Hubs, la capacidad de PostgreSQL, los nodos de AKS, el ancho de banda de cada enlace y el tamaño de cada subred.
