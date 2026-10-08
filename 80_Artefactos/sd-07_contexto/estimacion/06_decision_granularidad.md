# Decisión de granularidad del modelo de casos de uso (puerta G3)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: opción A aprobada por el usuario el 2026-10-08, pendiente de la firma del equipo. Reglas: `01_reglas_de_conteo.md` (decisión 6 de la diapositiva 31, C8, C12). Casos: `03_casos_de_uso_*.md`.

## 1. Situación

128 casos de uso, 311 transacciones y UUCW 660. Hay 71 casos de 2 transacciones, 50 de 3, 4 de 4 y 3 de 1. El 97 % son simples y el promedio es de 2,4 transacciones por caso. La clase (diapositiva 33) espera mayoría de casos medios en un sistema típico.

## 2. Opciones evaluadas

Calculadas mecánicamente sobre los archivos de casos (UUCP = UUCW + UAW 69).

| Opción | Casos | UUCW | UUCP | Diferencia con A |
| :-- | --: | --: | --: | --: |
| A. Objetivo del actor, como está | 128 | 660 | 729 | base |
| B. Fundir por servicio y actor principal | 78 | 590 | 659 | −11 % |
| C. Un caso por servicio, partido en bloques de 12 | 34 | 425 | 494 | −36 % |
| D. Fundir pares consecutivos del mismo servicio | 69 | 625 | 694 | −5 % |

## 3. Decisión

Se adopta la opción A. Motivos:

1. Respeta la decisión 6 de la diapositiva 31 y la convención C8: el caso es el objetivo completo del actor, no un paso de interfaz ni un agrupamiento por servicio.
2. Es la opción conservadora. El peso del caso es un escalón (1 a 3 transacciones valen 5 y 4 a 7 valen 10), así que en casos finos cada transacción pesa 2,1 puntos frente a 1,8 en un caso medio típico. Agrupar baja el UUCW y no lo sube.
3. El rango entre A y B (11 %) queda dentro del umbral de ±25 % con el segundo método.
4. B, C y D crean casos que ningún actor ejecuta, solo para parecerse a la forma de la clase.

Como la clase espera mayoría de casos medios, la desviación se explica por escrito (C12): este proyecto es grande, con 13 servicios y 28 resultados, y sus flujos están descritos como objetivos acotados del actor.

## 4. Sensibilidades que se informan en el paso 6

| Escenario | UUCW | Diferencia con A |
| :-- | --: | --: |
| Base (opción A) | 660 | base |
| Se funden los traslapes 3, 4 y 10 de `05_traslapes_entre_servicios.md` (CU-OF-02, CU-EX-04, CU-VE-04 bajan a simples) | 645 | −15 |
| Crédito sin conexión no resulta factible (EXC-16; se retiran CU-VE-07, CU-VE-11, CU-OR-07, CU-OR-08) | 640 | −20 |
| Ambos | 625 | −35 |
| Referencia: agrupación B | 590 | −70 |
| Marketplace sin conciliar liquidaciones (se retira CU-MK-11) | 655 | −5 |

La sensibilidad por UAW (66 a 77) está en `02_actores_uaw.md`.

## 5. Efecto en el UCP

El UCP es UUCP × TCF × EF. Entre 625 y 660 de UUCW el UUCP varía entre 694 y 729 (−5 %). El rango completo hasta B (659) es de −10 %. Las cifras definitivas se calculan en el paso 4 con la calculadora.
