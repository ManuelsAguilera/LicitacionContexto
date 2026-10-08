# Esfuerzo provisional por UCP (paso 6, puerta G6)

Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/calcular_esfuerzo.py`; no editar a mano. Fecha: 2026-10-08. Estado: **provisional**. Los factores de ambiente los informó el usuario (`09_ef_preguntas.md`, sección 3) salvo E3 (orientación a objetos), que sigue pendiente: se muestran los tres valores posibles 3, 4 y 5. Los escenarios restantes son ilustrativos y no son una propuesta.

## 1. Entradas

UAW 64 + UUCW 645 = UUCP 709 (`07_uucw_uucp.md`). TCF 1,19 (`08_tcf.md`). Lectura B: la fórmula E = UCP × CF da solo la programación y el total del proyecto es E / 0,40; se usa porque es la lectura que desarrolla la clase (convención C1). Reparto del total: análisis 10 %, diseño 20 %, programación 40 %, pruebas 15 %, sobrecarga 15 % (diapositiva 51). El CF se decide con la regla de Karner (diapositiva 49): 20 h por punto con 2 o menos factores desfavorables, 28 con 3 o 4, y no se estima con 5 o más.

## 2. Escenarios del factor de ambiente

| Escenario | EF | Desfavorables | CF | UCP | Programación E (h) | Total del proyecto (h) | Total con el otro CF (h) |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| Equipo, E3 en 3 | 0,785 | 1 | 20 | 662 | 13.246 | 33.116 | 46.362 |
| Equipo, E3 en 4 | 0,755 | 1 | 20 | 637 | 12.740 | 31.850 | 44.590 |
| Equipo, E3 en 5 | 0,725 | 1 | 20 | 612 | 12.234 | 30.584 | 42.818 |
| Mejor posible | 0,425 | 0 | 20 | 359 | 7.172 | 17.929 | 25.100 |
| Favorable | 0,710 | 0 | 20 | 599 | 11.981 | 29.952 | 41.932 |
| Neutro | 0,995 | 0 | 20 | 839 | 16.790 | 41.975 | 58.764 |
| Algo exigente | 1,130 | 3 | 28 | 953 | 26.695 | 66.737 | 47.670 |
| Peor posible | 1,700 | 8 | no estima | 1.434 | | | |

Referencia provisional: «Equipo, E3 en 3». Se elige el valor más bajo posible de E3 (el que da más horas) mientras el equipo no lo informe, para no subestimar. Con los valores informados hay un solo factor desfavorable (E6 en 2), así que el CF es 20 con cualquier E3.

## 3. Reparto por actividad (Equipo, E3 en 3)

| Actividad | % | Horas (CF 20) | Horas (CF 28) |
| :-- | --: | --: | --: |
| Análisis | 10% | 3.312 | 4.636 |
| Diseño | 20% | 6.623 | 9.272 |
| Programación | 40% | 13.246 | 18.545 |
| Pruebas | 15% | 4.967 | 6.954 |
| Sobrecarga | 15% | 4.967 | 6.954 |
| **Total** | 100 % | **33.116** | **46.362** |

## 4. Reparto por etapa y servicio (Equipo, E3 en 3, CF 20)

El tamaño de cada servicio es su UUCW. El UAW (64) se asigna a la Etapa 1, porque los actores de la base tecnológica nacen allí; si el equipo prefiere repartirlo por UUCW, las etapas pasan a 66,7 % y 33,3 %.

| Etapa | Servicio | Puntos (UUCP) | % | Horas totales |
| :-- | :-- | --: | --: | --: |
| 1 | Actores (UAW) | 64 | 9,0% | 2.989 |
| 1 | Existencias | 100 | 14,1% | 4.671 |
| 1 | Base tecnológica | 65 | 9,2% | 3.036 |
| 1 | Oferta comercial | 65 | 9,2% | 3.036 |
| 1 | Ventas | 55 | 7,8% | 2.569 |
| 1 | Originación de crédito | 45 | 6,3% | 2.102 |
| 1 | Cartera de crédito | 35 | 4,9% | 1.635 |
| 1 | Evidencia financiera | 35 | 4,9% | 1.635 |
| 1 | Control de cruces | 30 | 4,2% | 1.401 |
| **1** | **Subtotal** | **494** | **69,7%** | **23.074** |
| 2 | Pedidos | 75 | 10,6% | 3.503 |
| 2 | Marketplace | 55 | 7,8% | 2.569 |
| 2 | Abastecimiento | 25 | 3,5% | 1.168 |
| 2 | Posventa | 25 | 3,5% | 1.168 |
| 2 | Clientes Retail | 20 | 2,8% | 934 |
| 2 | Comisiones | 15 | 2,1% | 701 |
| **2** | **Subtotal** | **215** | **30,3%** | **10.042** |

## 5. Sensibilidad (Equipo, E3 en 3)

| Variación | UCP | Total del proyecto (h) | Diferencia |
| :-- | --: | --: | --: |
| Base (UUCP 709, TCF 1,19, CF 20) | 662 | 33.116 | +0,0% |
| E6 en 3 (requisitos más estables) | 612 | 30.584 | -7,6% |
| E6 en 1 (requisitos más inestables) | 713 | 35.647 | +7,6% |
| E7 en 3 (la mitad del equipo a tiempo parcial) | 738 | 36.912 | +11,5% |
| E8 en 4 (más dificultad de herramientas) | 688 | 34.381 | +3,8% |
| E1 en 3 (menos dominio del modelo) | 738 | 36.912 | +11,5% |
| CF 28 (si el equipo llegara a 3 o 4 factores desfavorables) | 662 | 46.362 | +40,0% |
| TCF bajo (1,11) | 618 | 30.889 | -6,7% |
| TCF alto (1,27) | 707 | 35.342 | +6,7% |
| UUCP bajo (667, `07_uucw_uucp.md`) | 623 | 31.154 | -5,9% |
| UUCP alto (717) | 670 | 33.489 | +1,1% |
| Combinación baja (UUCP 667, TCF 1,11, CF 20) | 581 | 29.060 | -12,2% |
| Combinación alta (UUCP 717, TCF 1,27, CF 28) | 715 | 50.037 | +51,1% |

## 6. Dos vías

La primera vía es la calculadora `estimacion_ucp.py`. La segunda repite las fórmulas de la clase dentro de este script sin importarla. **Coinciden** en UCP, E, total, EF y TCF de los cinco escenarios (tolerancia 1e-9).

## 7. Lo que estas cifras no incluyen

- El valor de E3, que falta. Entre E3 en 3 y en 5 el total varía unas 2.500 horas (≈ 8 %); el CF no cambia.
- Lo que el método no cubre: migración de datos, infraestructura y licencias, capacitación, marcha blanca y operación. Se estiman aparte (paso 7) y se compara con un segundo método para el desarrollo.
- La sobrecarga del 15 % de la diapositiva 51 ya está en el total (lectura B).
- Las horas por paquete de la EDT (formulario T-15) se reparten en el paso 8.
