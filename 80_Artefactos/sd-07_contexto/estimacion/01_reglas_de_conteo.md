# Reglas de conteo y convenciones de la estimación por Puntos de Casos de Uso (puerta G1)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: C5, C8 y el umbral de ±25 % firmados por el usuario el 2026-10-08. Queda la validación del equipo. Método: clase FEP03 (diapositivas 21 a 52). Las decisiones marcadas «propuesta» son de este trabajo y no vienen de la clase.

## 1. Las seis decisiones de la diapositiva 31

| N.º | Decisión | Regla adoptada | Fuente |
| :-- | :-- | :-- | :-- |
| 1 | Flujos alternativos | Se cuentan solo si agregan idas y vueltas completas | FEP03, diap. 31 |
| 2 | Casos incluidos | Se cuentan aparte si tienen valor por sí mismos | FEP03, diap. 31 |
| 3 | Casos de extensión | Se suman al caso base | FEP03, diap. 31 |
| 4 | Casos abstractos | No se cuentan, porque no los ejecuta un actor | FEP03, diap. 31 |
| 5 | Actores no humanos periódicos | Actor simple, declarado | FEP03, diap. 31 |
| 6 | Granularidad | Objetivo completo del actor, no un paso de interfaz | FEP03, diap. 31 y 33 |

Redacción tipo para el anexo de estimación: «El conteo consideró los casos de uso concretos del modelo, contando los flujos alternativos solo cuando agregan transacciones nuevas, y sumando las extensiones al caso base».

## 2. Convenciones del proyecto

| N.º | Tema | Regla (propuesta) |
| :-- | :-- | :-- |
| C1 | Lectura del esfuerzo | Lectura B de la clase. E = UCP × factor de conversión es solo programación. Total del proyecto = E / 0,40 |
| C2 | Reparto del total | Análisis 10 %, diseño 20 %, programación 40 %, pruebas 15 %, sobrecarga 15 % (diap. 51) |
| C3 | Factor de conversión | Regla de Karner (diap. 49). 20 horas por punto con 2 o menos factores de ambiente desfavorables, 28 con 3 o 4. Con 5 o más no se estima. Se informa siempre el escenario de 28 horas como sensibilidad |
| C4 | Decimales | Se conservan hasta el resultado final (diap. 63) |
| C5 | Interfaz de los sistemas | Se clasifican por la interfaz objetivo de la plataforma de integración, tipo 1. No por el archivo actual, tipo 2. Se informa también el UAW con tipo 2 como sensibilidad, porque el mapa de las 14 interfaces aún no existe |
| C6 | Qué es un actor | Un rol o un sistema, no una persona. Quedan fuera los roles de gobierno del proyecto (Contraparte Técnica, Comité Ejecutivo) y las autoridades que solo reciben reportes, mientras el equipo no valide lo contrario |
| C7 | Transacción | Viaje de ida y vuelta completo entre el actor y el sistema. Un evento entre sistemas se cuenta como transacción del actor sistema que lo origina |
| C8 | Máximo por caso | 12 transacciones. Un caso que lo supera se parte por objetivo del actor, nunca por pantalla |
| C9 | Cobertura mínima | El modelo debe incluir casos de administración (TI) y de integración (actores sistema). Su omisión subestima entre 10 % y 20 % (diap. 33) |
| C10 | Supuestos de flujo | Todo flujo que el sd-03 no describa (abastecimiento, comisiones, marketplace, clientes Retail y administración) se declara como supuesto y se rotula «propuesta» |
| C11 | Lo excluido | No genera casos de uso propios. Solo se cuenta lo que el Anexo A dice que «sí se hace» |
| C12 | Prueba de cordura | De 10 a 40 casos de uso en un sistema mediano, con mayoría de casos medios (diap. 33). Este proyecto es grande, así que una desviación se explica por escrito y no se corrige a ciegas |

## 3. Umbral entre métodos

La diferencia aceptable entre el UCP y el segundo método independiente es de ±25 % (propuesta, aprobada por el usuario). Fuera de ese rango se explica la causa antes de continuar a la puerta G8.

## 4. Preguntas para el equipo

1. ¿Se firma la convención C5 (tipo 1 para sistemas)?
2. ¿Se firma el máximo de 12 transacciones por caso (C8)?
3. ¿Se firma el umbral de ±25 % entre métodos?
4. ¿Las autoridades fiscalizadoras y el vendedor de marketplace son actores del sistema o solo destinatarios de reportes (C6)?
