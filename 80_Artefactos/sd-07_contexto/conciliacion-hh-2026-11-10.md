# Conciliación de horas hombre del SD-07 (2026-11-10)

Documento de trabajo, no entregable. Explica el paso de las 40.946 HH (SD-07, T-14 y T-15 de octubre, en el repositorio) a las 234.493,47 HH (versión de noviembre) y deja registradas las decisiones del equipo. Es el insumo de horas del modelo financiero del Informe 3.

**Fuente de los datos:** traspaso `Traspaso_SD07_costos_y_CPM_2026-11-10.zip`, preparado por el responsable del SD-07; no está versionado. Cifras verificadas el 2026-11-10 leyendo los CSV, sin ejecutar los scripts del traspaso.

## 1. Qué medía cada versión

| | Octubre (repositorio) | Noviembre (traspaso y PDF vigente) |
| :-- | :-- | :-- |
| Qué cuenta | Esfuerzo técnico por paquete de la EDT | Esfuerzo técnico **más** la dotación de personas: campo, dirección, inducción y operación |
| Software (rama 1.5) | 12.116 HH, la parte asignada a la rama | 31.625,44 HH, ciclo completo: 632,5088 UCP × 20 ÷ 0,40 |
| Operación | 8.064 HH de trabajos directos | 149.760 HH: equipo exclusivo de 26 personas × 160 HH × 36 meses |
| Total base | 40.946 HH | **234.493,47 HH** |
| Contingencia | 3.688 HH | 3.688 HH (sin cambio) |

## 2. Composición de las 234.493,47 HH

| Componente | HH | Dotación |
| :-- | --: | :-- |
| Trabajo técnico y viajes | 67.933,47 | Registros fechados por paquete y rol |
| Cobertura de campo M16 | 10.560,00 | 88 implantadores y 88 formadores |
| Dirección y PMO M1–M56 | 5.824,00 | 1 jefe de proyecto y 1 analista PMO |
| Inducción de operación M20 | 416,00 | 16 HH por cada una de las 26 personas de operación |
| Operación M21–M56 | 149.760,00 | 7 L1, 7 NOC, 7 SOC, 2 L2 (DevOps/SRE), 2 L3 y 1 gerente de servicio |
| **Total base** | **234.493,47** | |

Se valorizan aparte, sin sumarse a las HH:
- **Retén M13–M20:** 1.952 unidades de disponibilidad de 12 h; 16 personas del proyecto (8 de desarrollo y 8 de QA) que rotan de a 8 por semana.
- **Contingencia:** 3.688 HH, ligadas a 14 riesgos del SD-08.

## 3. Horas por rama: octubre frente a noviembre

| Rama | Octubre | Noviembre (trabajo) | Noviembre (dotación) | Noviembre (total) |
| :-- | --: | --: | --: | --: |
| 1.1 Dirección | 1.423 | 0 | 5.824 | 5.824,00 |
| 1.2 Levantamiento | 1.087 | 938,67 | — | 938,67 |
| 1.3 Arquitectura | 863 | 952,00 | — | 952,00 |
| 1.4 Infraestructura | 1.622 | 2.709,34 | — | 2.709,34 |
| 1.5 Software | 12.116 | 31.625,44 | — | 31.625,44 |
| 1.6 Integraciones | 1.068 | 3.266,00 | — | 3.266,00 |
| 1.7 Migración | 1.973 | 5.092,01 | — | 5.092,01 |
| 1.8 Seguridad | 949 | 1.400,00 | 40.320 (SOC) | 41.720,00 |
| 1.9 Calidad | 1.539 | 1.525,33 | — | 1.525,33 |
| 1.10 Innovaciones | 9.888 | 8.841,36 | — | 8.841,36 |
| 1.11 Implantación | 795 | 2.578,66 | 10.560 (campo) | 13.138,66 |
| 1.12 Marchas blancas | 532 | 2.646,66 | — | 2.646,66 |
| 1.13 Cambio y capacitación | 916 | 4.611,33 | 416 (inducción) | 5.027,33 |
| 1.14 Documentación | 969 | 986,67 | — | 986,67 |
| 1.15 Operación | 5.206 | 760,00 | 109.440 | 110.200,00 |
| **Total** | **40.946** | **67.933,47** | **166.560** | **234.493,47** |

## 4. Decisiones (2026-11-10)

| # | Decisión | Resolución |
| :-- | :-- | :-- |
| D1 | ¿Estructura de octubre o de noviembre? | **Noviembre.** El Art. 17.2.1 exige demostrar dotación suficiente, no solo esfuerzo técnico |
| D2 | ¿Hay doble conteo del software (ciclo completo) con las ramas 1.2, 1.3 y 1.9? | **No.** Los paquetes de análisis, diseño y pruebas de software (1.2.2, 1.2.3, 1.2.8, 1.3.1, 1.3.3, 1.3.5, 1.9.2 y 1.9.3) tienen 0 HH y están financiados por el UCP. Lo que queda en esas ramas es trabajo distinto: estudios, arquitectura física y pruebas de desempeño |
| D3 | ¿26 personas en operación? | **Se cierra como está**, como supuesto declarado. El SD-10 y el SD-12 no existen todavía y el traspaso marca `SLA_validated: false`. Revisar cuando existan |
| D4 | ¿Desglose de la dotación por rol? | **Resuelto.** 37 roles × 56 meses en `HH_matriz_roles_M1_M56.csv` |

## 5. Comprobaciones hechas

- La suma de `HH_detalle_mes_rol_componente.csv` da 234.493,47 HH.
- `Conciliacion_mensual.csv` da diferencia 0,00 HH en los 56 meses respecto de la figura publicada.
- SD-07, T-14 y T-15 del traspaso declaran las mismas cifras (234.493, 149.760 y 31.625).
- La red CPM (`resumen_red.json`) tiene 853 nodos y 1.836 relaciones, sin holguras negativas ni actividades tardías.
- Mes de mayor carga: M16, con 14.944 HH (salida a producción E1 en 22 tiendas).

## 6. Pendientes

1. **El repositorio sigue en 40.946 HH.** El `.tex` del traspaso es un borrador que no incluye las ediciones finales del PDF vigente; le faltan, por ejemplo, la Tabla 7.8, el texto de la red de 853 nodos, el retén y la nota de 18.192 HH. Se actualizará por pasos.
2. **La Gantt se rehace.** En el cuerpo va un resumen (hitos y ramas) y la Gantt completa va al anexo T-14. Las 28 láminas actuales no se reutilizan.
3. **Horas nominales:** se usan 160 HH por persona al mes. Sirve para el costo; la tarifa del Excel debe considerar horas productivas (FEP02·90).
4. **El calendario de compras (R4) no viene en el traspaso.** Paso C.
