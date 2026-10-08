# Decisión de granularidad del modelo de casos de uso (puerta G3)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: opción A aprobada por el usuario el 2026-10-08, con las correcciones de la revisión independiente de G3 aprobadas el mismo día. Pendiente de la firma del equipo. Reglas: `01_reglas_de_conteo.md` (decisión 6 de la diapositiva 31, C8, C12). Casos: `03_casos_de_uso_*.md`.

## 1. Situación

127 casos de uso, 296 transacciones y UUCW 645. Hay 6 casos de 1 transacción, 75 de 2, 44 de 3 y 2 de 4 (CU-EX-04 y CU-OF-02). El 98 % son simples y el promedio es de 2,3 transacciones por caso. La clase (diapositiva 33) espera mayoría de casos medios en un sistema típico. El UAW es 64.

## 2. Opciones evaluadas

Calculadas mecánicamente sobre los archivos de casos (UUCP = UUCW + UAW 64).

| Opción | Casos | UUCW | UUCP | Diferencia con A |
| :-- | --: | --: | --: | --: |
| A. Objetivo del actor, como está | 127 | 645 | 709 | base |
| B. Fundir por servicio y actor principal | 73 | 565 | 629 | −11 % |
| C. Un caso por servicio, partido en bloques de 12 | 33 | 415 | 479 | −32 % |
| D. Fundir pares consecutivos del mismo servicio | 69 | 610 | 674 | −5 % |

## 3. Decisión

Se adopta la opción A. Motivos:

1. Respeta la decisión 6 de la diapositiva 31 y la convención C8: el caso es el objetivo completo del actor, no un paso de interfaz ni un agrupamiento por servicio.
2. Es la opción conservadora. El peso del caso es un escalón (1 a 3 transacciones valen 5 y 4 a 7 valen 10), así que en casos finos cada transacción pesa más que en un caso medio típico. Agrupar baja el UUCW y no lo sube.
3. El rango entre A y B (11 %) queda dentro del umbral de ±25 % con el segundo método.
4. B, C y D crean casos que ningún actor ejecuta, solo para parecerse a la forma de la clase.

Como la clase espera mayoría de casos medios, la desviación se explica por escrito (C12): este proyecto es grande, con 13 servicios y 28 resultados, y sus flujos están descritos como objetivos acotados del actor.

## 4. Revisión independiente de G3 (2026-10-08)

Un agente revisó el modelo en solo lectura y confirmó el recuento. El usuario aprobó aplicar sus correcciones:

1. Se retiró CU-EV-06 y el actor AS-12 (la autoridad solo recibe reportes, C6). UUCW −5 y UAW −2.
2. AH-01 salió del UAW base y las seis consultas del cliente pasaron a AS-04, por la Opción A firmada. UAW −3. El UAW base es 64.
3. CU-VE-04 (se quitó la detección automática del enlace) y CU-EX-08 (se fundieron los campos de parámetros) pasaron a simples. UUCW −10.
4. CU-OR-07 se retituló «Autorizar compra a cuotas sin enlace contra el cupo preaprobado». La sensibilidad de EXC-16 se corrigió a −15, porque CU-VE-11 se mantiene.
5. Nueve transacciones que no eran idas y vueltas con el actor se descontaron (cierre por inactividad, revocaciones automáticas, notificaciones y pasos internos). Las transacciones bajaron de 311 a 296 con el resto de los cambios.
6. Se unificó el criterio de las opciones: presentarlas es una ida y vuelta. En lugar de contar cada opción en CU-PE-07 (lo que habría subido CU-PV-02 a un caso medio), CU-PE-07 pasó a 2 transacciones.
7. Se corrigieron cuatro enlaces de la trazabilidad (resultados 2, 5, 13 y 23) y se declararon dos traslapes más.
8. Se dejaron como están los casos CU-CC-02 y CU-CC-04 (pruebas negativas), porque RF-170 a RF-172 son obligatorios y la línea roja los exige. Su retiro es una sensibilidad.
9. AS-11 se mantiene separado de AS-01 (es el conector de remuneraciones) y su unión es una sensibilidad.

## 5. Sensibilidades que se informan en el paso 6

| Escenario | UUCW | Diferencia con A |
| :-- | --: | --: |
| Base (opción A) | 645 | base |
| Se funden los traslapes 3 y 4 (CU-OF-02 y CU-EX-04 bajan a simples) | 635 | −10 |
| Crédito sin conexión no resulta factible (EXC-16; se retiran CU-VE-07, CU-OR-07 y CU-OR-08) | 630 | −15 |
| Se retiran CU-CC-02 y CU-CC-04 (pruebas negativas) | 635 | −10 |
| Marketplace sin conciliar liquidaciones (se retira CU-MK-11) | 640 | −5 |
| Todas a la vez | 605 | −40 |
| Referencia: agrupación B | 565 | −80 |

La sensibilidad por UAW (62 a 72) está en `02_actores_uaw.md`.

## 6. Efecto en el UCP

El UCP es UUCP × TCF × EF. Entre 605 y 645 de UUCW el UUCP varía entre 669 y 709 (−6 %). El rango completo hasta B (629) es de −11 %. Las cifras definitivas se calculan en el paso 4 con la calculadora.
