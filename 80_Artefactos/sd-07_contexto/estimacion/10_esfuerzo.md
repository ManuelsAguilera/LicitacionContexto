# Esfuerzo provisional por UCP (paso 6, puerta G6)

Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/calcular_esfuerzo.py`; no editar a mano. Fecha: 2026-10-08. Estado: **todos los datos informados; pendiente de la firma del equipo**. Los factores de ambiente los informó el usuario (`09_ef_preguntas.md`, sección 3) y están pendientes de la firma del equipo. Los demás escenarios del cuadro 2 son ilustrativos y no son una propuesta.

## 1. Entradas

UAW 64 + UUCW 645 = UUCP 709 (`07_uucw_uucp.md`). TCF 1,19 (`08_tcf.md`). Lectura B: la fórmula E = UCP × CF da solo la programación y el total del proyecto es E / 0,40; se usa porque es la lectura que desarrolla la clase (convención C1). Reparto del total: análisis 10 %, diseño 20 %, programación 40 %, pruebas 15 %, sobrecarga 15 % (diapositiva 51). El CF se decide con la regla de Karner (diapositiva 49): 20 h por punto con 2 o menos factores desfavorables, 28 con 3 o 4, y no se estima con 5 o más.

## 2. Escenarios del factor de ambiente

| Escenario | EF | Desfavorables | CF | UCP | Programación E (h) | Total del proyecto (h) | Total con el otro CF (h) |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| Equipo | 0,755 | 1 | 20 | 637 | 12.740 | 31.850 | 44.590 |
| Mejor posible | 0,425 | 0 | 20 | 359 | 7.172 | 17.929 | 25.100 |
| Favorable | 0,710 | 0 | 20 | 599 | 11.981 | 29.952 | 41.932 |
| Neutro | 0,995 | 0 | 20 | 839 | 16.790 | 41.975 | 58.764 |
| Algo exigente | 1,130 | 3 | 28 | 953 | 26.695 | 66.737 | 47.670 |
| Peor posible | 1,700 | 8 | no estima | 1.434 | | | |

Referencia: «Equipo», con los valores informados. Hay un solo factor desfavorable (E6 en 2), así que el CF es 20 horas por punto.

## 3. Reparto por actividad (Equipo)

| Actividad | % | Horas (CF 20) | Horas (CF 28) |
| :-- | --: | --: | --: |
| Análisis | 10% | 3.185 | 4.459 |
| Diseño | 20% | 6.370 | 8.918 |
| Programación | 40% | 12.740 | 17.836 |
| Pruebas | 15% | 4.778 | 6.689 |
| Sobrecarga | 15% | 4.778 | 6.689 |
| **Total** | 100 % | **31.850** | **44.590** |

## 4. Reparto por etapa y servicio (Equipo, CF 20)

El tamaño de cada servicio es su UUCW. El UAW (64) se asigna a la Etapa 1, porque los actores de la base tecnológica nacen allí; si el equipo prefiere repartirlo por UUCW, las etapas pasan a 66,7 % y 33,3 %.

| Etapa | Servicio | Puntos (UUCP) | % | Horas totales |
| :-- | :-- | --: | --: | --: |
| 1 | Actores (UAW) | 64 | 9,0% | 2.875 |
| 1 | Existencias | 100 | 14,1% | 4.492 |
| 1 | Base tecnológica | 65 | 9,2% | 2.920 |
| 1 | Oferta comercial | 65 | 9,2% | 2.920 |
| 1 | Ventas | 55 | 7,8% | 2.471 |
| 1 | Originación de crédito | 45 | 6,3% | 2.022 |
| 1 | Cartera de crédito | 35 | 4,9% | 1.572 |
| 1 | Evidencia financiera | 35 | 4,9% | 1.572 |
| 1 | Control de cruces | 30 | 4,2% | 1.348 |
| **1** | **Subtotal** | **494** | **69,7%** | **22.192** |
| 2 | Pedidos | 75 | 10,6% | 3.369 |
| 2 | Marketplace | 55 | 7,8% | 2.471 |
| 2 | Abastecimiento | 25 | 3,5% | 1.123 |
| 2 | Posventa | 25 | 3,5% | 1.123 |
| 2 | Clientes Retail | 20 | 2,8% | 898 |
| 2 | Comisiones | 15 | 2,1% | 674 |
| **2** | **Subtotal** | **215** | **30,3%** | **9.658** |

## 5. Sensibilidad (Equipo)

| Variación | UCP | Total del proyecto (h) | Diferencia |
| :-- | --: | --: | --: |
| Base (UUCP 709, TCF 1,19, CF 20) | 637 | 31.850 | +0,0% |
| E6 en 3 (requisitos más estables) | 586 | 29.319 | -7,9% |
| E6 en 1 (requisitos más inestables) | 688 | 34.381 | +7,9% |
| E7 en 3 (la mitad del equipo a tiempo parcial) | 713 | 35.647 | +11,9% |
| E8 en 4 (más dificultad de herramientas) | 662 | 33.116 | +4,0% |
| E1 en 3 (menos dominio del modelo) | 713 | 35.647 | +11,9% |
| CF 28 (si el equipo llegara a 3 o 4 factores desfavorables) | 637 | 44.590 | +40,0% |
| TCF bajo (1,11) | 594 | 29.709 | -6,7% |
| TCF alto (1,27) | 680 | 33.991 | +6,7% |
| UUCP bajo (667, `07_uucw_uucp.md`) | 599 | 29.963 | -5,9% |
| UUCP alto (717) | 644 | 32.209 | +1,1% |
| Combinación baja (UUCP 667, TCF 1,11, CF 20) | 559 | 27.949 | -12,2% |
| Combinación alta (UUCP 717, TCF 1,27, CF 28) | 687 | 48.125 | +51,1% |

## 6. Dos vías

La primera vía es la calculadora `estimacion_ucp.py`. La segunda repite las fórmulas de la clase dentro de este script sin importarla. **Coinciden** en UCP, E, total, EF y TCF de todos los escenarios (tolerancia 1e-9).

## 7. Lo que estas cifras no incluyen

- La firma del equipo sobre los ocho valores. E7 en 0 es un supuesto sin respaldo (el sd-12 no existe), E1 en 5 depende del sd-06 y E5 en 5 es una autoevaluación del equipo.
- Lo que el método no cubre: migración de datos, infraestructura y licencias, capacitación, marcha blanca y operación. Se estiman aparte (paso 7) y se compara con un segundo método para el desarrollo.
- La sobrecarga del 15 % de la diapositiva 51 ya está en el total (lectura B).
- Las horas por paquete de la EDT (formulario T-15) se reparten en el paso 8.
