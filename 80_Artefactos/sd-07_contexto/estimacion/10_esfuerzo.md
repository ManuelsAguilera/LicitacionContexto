# Esfuerzo provisional por UCP (paso 6, puerta G6)

Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/calcular_esfuerzo.py`; no editar a mano. Fecha: 2026-10-08. Estado: **provisional**. Los factores de ambiente los asigna el equipo (`09_ef_preguntas.md`); aquí se usan cinco escenarios ilustrativos para mostrar el rango. Ninguna cifra de EF es una propuesta.

## 1. Entradas

UAW 64 + UUCW 645 = UUCP 709 (`07_uucw_uucp.md`). TCF 1,19 (`08_tcf.md`). Lectura B: la fórmula E = UCP × CF da solo la programación y el total del proyecto es E / 0,40; se usa porque es la lectura que desarrolla la clase (convención C1). Reparto del total: análisis 10 %, diseño 20 %, programación 40 %, pruebas 15 %, sobrecarga 15 % (diapositiva 51). El CF se decide con la regla de Karner (diapositiva 49): 20 h por punto con 2 o menos factores desfavorables, 28 con 3 o 4, y no se estima con 5 o más.

## 2. Escenarios del factor de ambiente

| Escenario | EF | Desfavorables | CF | UCP | Programación E (h) | Total del proyecto (h) | Total con el otro CF (h) |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| Mejor posible | 0,425 | 0 | 20 | 359 | 7.172 | 17.929 | 25.100 |
| Favorable | 0,710 | 0 | 20 | 599 | 11.981 | 29.952 | 41.932 |
| Neutro | 0,995 | 0 | 20 | 839 | 16.790 | 41.975 | 58.764 |
| Algo exigente | 1,130 | 3 | 28 | 953 | 26.695 | 66.737 | 47.670 |
| Peor posible | 1,700 | 8 | no estima | 1.434 | | | |

Referencia provisional: el escenario «Neutro» (los ocho factores en 3). Se elige porque es el punto en que el método no ajusta nada (diapositiva 44), no porque sea una predicción del equipo.

## 3. Reparto por actividad (escenario Neutro)

| Actividad | % | Horas (CF 20) | Horas (CF 28) |
| :-- | --: | --: | --: |
| Análisis | 10% | 4.197 | 5.876 |
| Diseño | 20% | 8.395 | 11.753 |
| Programación | 40% | 16.790 | 23.506 |
| Pruebas | 15% | 6.296 | 8.815 |
| Sobrecarga | 15% | 6.296 | 8.815 |
| **Total** | 100 % | **41.975** | **58.764** |

## 4. Reparto por etapa y servicio (escenario Neutro, CF 20)

El tamaño de cada servicio es su UUCW. El UAW (64) se asigna a la Etapa 1, porque los actores de la base tecnológica nacen allí; si el equipo prefiere repartirlo por UUCW, las etapas pasan a 66,7 % y 33,3 %.

| Etapa | Servicio | Puntos (UUCP) | % | Horas totales |
| :-- | :-- | --: | --: | --: |
| 1 | Actores (UAW) | 64 | 9,0% | 3.789 |
| 1 | Existencias | 100 | 14,1% | 5.920 |
| 1 | Base tecnológica | 65 | 9,2% | 3.848 |
| 1 | Oferta comercial | 65 | 9,2% | 3.848 |
| 1 | Ventas | 55 | 7,8% | 3.256 |
| 1 | Originación de crédito | 45 | 6,3% | 2.664 |
| 1 | Cartera de crédito | 35 | 4,9% | 2.072 |
| 1 | Evidencia financiera | 35 | 4,9% | 2.072 |
| 1 | Control de cruces | 30 | 4,2% | 1.776 |
| **1** | **Subtotal** | **494** | **69,7%** | **29.246** |
| 2 | Pedidos | 75 | 10,6% | 4.440 |
| 2 | Marketplace | 55 | 7,8% | 3.256 |
| 2 | Abastecimiento | 25 | 3,5% | 1.480 |
| 2 | Posventa | 25 | 3,5% | 1.480 |
| 2 | Clientes Retail | 20 | 2,8% | 1.184 |
| 2 | Comisiones | 15 | 2,1% | 888 |
| **2** | **Subtotal** | **215** | **30,3%** | **12.729** |

## 5. Sensibilidad (EF Neutro)

| Variación | UCP | Total del proyecto (h) | Diferencia |
| :-- | --: | --: | --: |
| Base (UUCP 709, TCF 1,19, CF 20) | 839 | 41.975 | +0,0% |
| CF 28 (regla de Karner con 3 o 4 desfavorables) | 839 | 58.764 | +40,0% |
| TCF bajo (1,11) | 783 | 39.153 | -6,7% |
| TCF alto (1,27) | 896 | 44.796 | +6,7% |
| UUCP bajo (667, `07_uucw_uucp.md`) | 790 | 39.488 | -5,9% |
| UUCP alto (717) | 849 | 42.448 | +1,1% |
| Combinación baja (UUCP 667, TCF 1,11, CF 20) | 737 | 36.833 | -12,2% |
| Combinación alta (UUCP 717, TCF 1,27, CF 28) | 906 | 63.423 | +51,1% |

## 6. Dos vías

La primera vía es la calculadora `estimacion_ucp.py`. La segunda repite las fórmulas de la clase dentro de este script sin importarla. **Coinciden** en UCP, E, total, EF y TCF de los cinco escenarios (tolerancia 1e-9).

## 7. Lo que estas cifras no incluyen

- Los factores de ambiente reales: el rango del cuadro 2 (de 17.929 a 66.737 horas sin el peor caso) refleja esa incertidumbre, no un error del método.
- Lo que el método no cubre: migración de datos, infraestructura y licencias, capacitación, marcha blanca y operación. Se estiman aparte (paso 7) y se compara con un segundo método para el desarrollo.
- La sobrecarga del 15 % de la diapositiva 51 ya está en el total (lectura B).
- Las horas por paquete de la EDT (formulario T-15) se reparten en el paso 8.
