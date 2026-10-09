# Evaluación de la EDT contra las reglas 8/80 y del período de reporte

Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/evaluar_tamano_paquetes.py`; no editar a mano. Fecha: 2026-10-08. Reglas: FEP02, diapositiva 56 («un paquete de trabajo debe requerir entre 8 y 80 horas» y «debe caber dentro de un período de reporte») y diapositiva 55 («demasiadas divisiones disminuyen la productividad de la gestión»). Período de reporte: **un mes**, el del informe mensual de avance (RT-19.06), decisión del usuario del 2026-10-08.

## 1. Por qué la EDT no cumple 8/80

| Hecho | Valor |
| :-- | --: |
| Horas de software del UCP (escenario del equipo, lectura B) | 31.850 h |
| Horas de un caso de uso simple / medio | 247 h / 494 h |
| Horas por transacción (296 transacciones) | 108 h |
| Programación de un caso simple (40 %, diap. 51) | 99 h |
| Un caso simple con la lectura A (sin el factor ×2,5) | 99 h |
| Elementos de software y su rango | 51, de 247 a 1.481 h; 0 con 80 h o menos |
| Paquetes que harían falta para 8/80 solo en software | 398 (a 80 h) a 724 (a 44 h, punto medio) |
| Duración de las ventanas (meses) | 9 de 1; 28 de 2 a 3; 101 de 4 a 12; 21 de más de 12 |

Causas, en orden de peso:

1. **La unidad de estimación es más gruesa que la regla.** El UCP mide por caso de uso y el caso más chico pesa 247 h. Ni siquiera una transacción (108 h) cabe en 80 h. Con la lectura B, cada caso ya trae su análisis, diseño, pruebas y sobrecarga (factor ×2,5). Incluso con la lectura A, la programación de un caso simple pasa las 80 h.
2. **Escala.** Son 56 meses y 31.850 h solo de software; el resto del proyecto todavía no tiene horas (paso 7) y solo suma.
3. **Las reglas que nos pusimos impiden bajar más.** La guía de la EDT prohíbe paquetes por requerimiento, pantalla o persona; el usuario fijó 3 a 8 elementos por servicio; el rango de 100 a 250 paquetes de la guía es una heurística del equipo, no viene de PMBOK ni de la clase.
4. **Ventanas por etapa, no por período.** El cronograma da al software ventanas de 6 a 12 meses: la regla del período de reporte falla por construcción.
5. **Trabajo continuo como un solo elemento.** Gestión, documentación y operación son trabajo de nivel de esfuerzo de 24 a 56 meses: nunca caben en 80 h ni en un mes si no se cortan por período.
6. **La clase tira en dos direcciones.** La diapositiva 55 advierte contra dividir de más y la 56 pide 8/80. PMBOK 6 lo reconcilia: el último nivel de la EDT puede ser una **cuenta de control**; lo lejano se deja como **paquete de planificación** y se descompone en **paquetes de trabajo** cuando se acerca (planificación gradual).

**Conclusión.** No es un error de conteo. Exigir 8/80 a cada elemento de una EDT de entregables de este tamaño obligaría a tener entre 398 y 724 paquetes solo de software, contra la advertencia de la diapositiva 55. La regla se cumple un nivel más abajo: en los paquetes de trabajo de la ola cercana y en las actividades del cronograma. En el software, el paquete de trabajo es el entregable de un caso de uso y queda como excepción declarada (sección 5).

## 2. Cumplimiento por rama

| Rama | Elementos | Con horas | Más de 80 h | 8 a 80 h | Menos de 8 h | Sin horas | Más de un mes |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| 1.1 Dirección, gobierno y control del proyecto | 12 | 0 | 0 | 0 | 0 | 12 | 11 |
| 1.2 Levantamiento y línea base de alcance | 8 | 0 | 0 | 0 | 0 | 8 | 8 |
| 1.3 Arquitectura y diseño | 7 | 0 | 0 | 0 | 0 | 7 | 7 |
| 1.4 Infraestructura híbrida y plataforma base | 13 | 0 | 0 | 0 | 0 | 13 | 13 |
| 1.5 Desarrollo de software | 51 | 51 | 51 | 0 | 0 | 0 | 51 |
| 1.6 Integraciones | 7 | 0 | 0 | 0 | 0 | 7 | 7 |
| 1.7 Migración y saneamiento de datos | 12 | 0 | 0 | 0 | 0 | 12 | 11 |
| 1.8 Seguridad, identidad y cumplimiento | 8 | 0 | 0 | 0 | 0 | 8 | 8 |
| 1.9 Calidad, pruebas y certificación | 12 | 0 | 0 | 0 | 0 | 12 | 10 |
| 1.10 Innovaciones | 5 | 0 | 0 | 0 | 0 | 5 | 0 |
| 1.11 Implantación y despliegue | 4 | 0 | 0 | 0 | 0 | 4 | 4 |
| 1.12 Resultados de las marchas blancas y aceptación por etapa | 7 | 0 | 0 | 0 | 0 | 7 | 4 |
| 1.13 Gestión del cambio y capacitación | 5 | 0 | 0 | 0 | 0 | 5 | 5 |
| 1.14 Documentación, transferencia y reversibilidad | 7 | 0 | 0 | 0 | 0 | 7 | 5 |
| 1.15 Operación y soporte | 6 | 0 | 0 | 0 | 0 | 6 | 6 |
| **Total** | **164** | **51** | **51** | **0** | **0** | **113** | **150** |

## 3. Cumplimiento por nivel

Las dos reglas se exigen solo a los paquetes de trabajo. Las cuentas de control y los paquetes de planificación pueden ser mayores: se descomponen cuando entran en la ola cercana.

| Nivel | Elementos | Incumplen 8/80 o el período |
| :-- | --: | --: |
| cuenta de control | 164 | 164 |

Paquetes de trabajo que incumplen: **0**.

## 4. Decisiones del usuario (2026-10-08)

1. Se resuelve con la planificación gradual de PMBOK 6: el último nivel de la EDT son cuentas de control; solo la ola cercana se descompone en paquetes de trabajo de 8 a 80 h y de un mes como máximo; lo lejano queda como paquetes de planificación.
2. Período de reporte mensual (RT-19.06).
3. Las fusiones de la opción A se aplican a nivel de cuentas de control.
4. **En el software, el paquete de trabajo es el entregable: uno por caso de uso.** Es un subproyecto (diap. 56) y supera las 80 h por una excepción declarada; sus fases son actividades del cronograma de 8 a 80 h, no nodos de la EDT.

## 5. Por qué no se parte el software por fase

Una primera versión proyectó 689 «paquetes» de software con una regla de un paquete por caso y fase (análisis, diseño, construcción y pruebas), partido por transacción cuando pasaba de 80 h. Eso era un error de diseño: las fases son actividades, no entregables (la guía de la EDT lo prohíbe y la diapositiva 56 dice que el paquete se descompone en actividades fuera de la EDT). La cantidad dependía de esa regla y no de lo que hay que entregar.

| Estructura | Elementos de software | Tamaño medio |
| :-- | --: | --: |
| Regla descartada: caso × fase, partido por transacción | 689 | 39 h |
| Caso × fase, sin partir | 508 | 53 h |
| Un entregable por transacción | 296 | 108 h |
| **Un entregable por caso de uso (vigente)** | **127** | **251 h** |
| Cuentas de control de software | 51 | 625 h |

Con el paquete igual al caso de uso, la EDT conserva la traza uno a uno al sd-03 (caso, RF y resultados del Anexo D), y las 689 actividades por fase quedan en el cronograma, donde cada una cumple 8/80 y un mes.
