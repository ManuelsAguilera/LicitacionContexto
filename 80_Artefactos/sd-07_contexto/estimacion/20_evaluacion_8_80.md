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
| Elementos de software y su rango | 73, de 247 a 1.234 h; 0 con 80 h o menos |
| Paquetes que harían falta para 8/80 solo en software | 398 (a 80 h) a 724 (a 44 h, punto medio) |
| Duración de las ventanas (meses) | 12 de 1; 29 de 2 a 3; 133 de 4 a 12; 28 de más de 12 |

Causas, en orden de peso:

1. **La unidad de estimación es más gruesa que la regla.** El UCP mide por caso de uso y el caso más chico pesa 247 h. Ni siquiera una transacción (108 h) cabe en 80 h. Con la lectura B, cada caso ya trae su análisis, diseño, pruebas y sobrecarga (factor ×2,5). Incluso con la lectura A, la programación de un caso simple pasa las 80 h.
2. **Escala.** Son 56 meses y 31.850 h solo de software; el resto del proyecto todavía no tiene horas (paso 7) y solo suma.
3. **Las reglas que nos pusimos impiden bajar más.** La guía de la EDT prohíbe paquetes por requerimiento, pantalla o persona; el usuario fijó 3 a 8 elementos por servicio; el rango de 100 a 250 paquetes de la guía es una heurística del equipo, no viene de PMBOK ni de la clase.
4. **Ventanas por etapa, no por período.** El cronograma da al software ventanas de 6 a 12 meses: la regla del período de reporte falla por construcción.
5. **Trabajo continuo como un solo elemento.** Gestión, documentación y operación son trabajo de nivel de esfuerzo de 24 a 56 meses: nunca caben en 80 h ni en un mes si no se cortan por período.
6. **La clase tira en dos direcciones.** La diapositiva 55 advierte contra dividir de más y la 56 pide 8/80. PMBOK 6 lo reconcilia: el último nivel de la EDT puede ser una **cuenta de control**; lo lejano se deja como **paquete de planificación** y se descompone en **paquetes de trabajo** cuando se acerca (planificación gradual).

**Conclusión.** No es un error de conteo. Exigir 8/80 a cada elemento de una EDT de entregables de este tamaño obligaría a tener entre 398 y 724 paquetes solo de software, contra la advertencia de la diapositiva 55. La regla se cumple un nivel más abajo, en los paquetes de trabajo de la ola cercana.

## 2. Cumplimiento por rama

| Rama | Elementos | Con horas | Más de 80 h | 8 a 80 h | Menos de 8 h | Sin horas | Más de un mes |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| 1.1 Dirección, gobierno y control del proyecto | 13 | 0 | 0 | 0 | 0 | 13 | 12 |
| 1.2 Levantamiento y línea base de alcance | 9 | 0 | 0 | 0 | 0 | 9 | 9 |
| 1.3 Arquitectura y diseño | 8 | 0 | 0 | 0 | 0 | 8 | 8 |
| 1.4 Infraestructura híbrida y plataforma base | 19 | 0 | 0 | 0 | 0 | 19 | 19 |
| 1.5 Desarrollo de software | 73 | 73 | 73 | 0 | 0 | 0 | 73 |
| 1.6 Integraciones | 11 | 0 | 0 | 0 | 0 | 11 | 11 |
| 1.7 Migración y saneamiento de datos | 12 | 0 | 0 | 0 | 0 | 12 | 11 |
| 1.8 Seguridad, identidad y cumplimiento | 12 | 0 | 0 | 0 | 0 | 12 | 12 |
| 1.9 Calidad, pruebas y certificación | 10 | 0 | 0 | 0 | 0 | 10 | 8 |
| 1.10 Innovaciones | 5 | 0 | 0 | 0 | 0 | 5 | 0 |
| 1.11 Implantación y despliegue | 4 | 0 | 0 | 0 | 0 | 4 | 4 |
| 1.12 Resultados de las marchas blancas y aceptación por etapa | 9 | 0 | 0 | 0 | 0 | 9 | 4 |
| 1.13 Gestión del cambio y capacitación | 4 | 0 | 0 | 0 | 0 | 4 | 4 |
| 1.14 Documentación, transferencia y reversibilidad | 10 | 0 | 0 | 0 | 0 | 10 | 7 |
| 1.15 Operación y soporte | 8 | 0 | 0 | 0 | 0 | 8 | 8 |
| **Total** | **207** | **73** | **73** | **0** | **0** | **134** | **190** |

## 3. Cumplimiento por nivel

Las dos reglas se exigen solo a los paquetes de trabajo. Las cuentas de control y los paquetes de planificación pueden ser mayores: se descomponen cuando entran en la ola cercana.

| Nivel | Elementos | Incumplen 8/80 o el período |
| :-- | --: | --: |
| sin nivel declarado | 207 | 207 |

Paquetes de trabajo que incumplen: **0**.

## 4. Decisiones del usuario (2026-10-08)

1. Se resuelve con la planificación gradual de PMBOK 6: el último nivel de la EDT son cuentas de control; solo la ola cercana se descompone en paquetes de trabajo de 8 a 80 h y de un mes como máximo; lo lejano queda como paquetes de planificación.
2. Período de reporte mensual (RT-19.06).
3. Las fusiones de la opción A se aplican a nivel de cuentas de control.

## 5. Regla de descomposición del software para su ola

Cuando un servicio entra en su ola, cada caso de uso se baja a paquetes de trabajo. Un caso simple (247 h) no cabe en 80 h, así que se parte por transacción y fase: análisis y diseño ≈ 32 h, construcción ≈ 43 h y pruebas ≈ 16 h por transacción; la sobrecarga (16 h por transacción) va a la cuenta de gestión. Son unos 888 paquetes en todo el proyecto, pero nunca todos a la vez: solo los de la ola en curso.
