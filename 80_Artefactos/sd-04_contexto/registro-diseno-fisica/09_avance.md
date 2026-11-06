# Avance del registro de diseño de la física

**Última actualización del documento:** 2026-10-29
Cómo se mantiene: al cerrar cada tarea se actualiza su fila (porcentaje, fecha y hora del último cambio) y la línea de arriba. Los pesos son criterio de Claude sobre el esfuerzo de cada entregable, no vienen de las Bases; sirven de orientación.

**Avance total estimado: ≈ 99 %**  (suma de peso × hecho; «100 %» significa borrador completo sin revisión humana, no documento aprobado)

| Entregable | Peso | Hecho | Último cambio | Qué falta |
| :--- | ---: | ---: | :--- | :--- |
| `00` Registro: control, matriz, restricciones, decisiones | 8 % | 100 % | 2026-10-29 | Solo falta la sec. 9 (mapeo) |
| `01` Nodos | 20 % | 100 % | 2026-10-29 | — |
| `02` Conexiones | 12 % | 100 % | 2026-10-29 | — |
| `03` Ambientes | 5 % | 100 % | 2026-10-29 | — |
| `04` Continuidad | 8 % | 100 % | 2026-10-29 | — |
| `05` Capacidad | 5 % | 100 % | 2026-10-29 | — |
| `06` Supuestos y pendientes | 5 % | 100 % | 2026-10-29 | Verificados contra Microsoft (S-19 a S-22 nuevos); se amplía con los del mapeo |
| `07` Costos (interno) | 7 % | 100 % | 2026-10-29 | Cifras se cotizan en la oferta económica |
| `08` Glosario de equivalentes | 5 % | 100 % | 2026-10-29 | — |
| Sec. 9: mapeo lógica↔física, reglas de chequeo, discrepancias | 15 % | 100 % | 2026-10-29 | — |
| Diagrama N3 (6 hojas) y diagrama atómico gigante | 10 % | 92 % | 2026-10-29 | Afinar a mano los últimos cruces en draw.io y revisión humana |

## Bloques de `01_nodos.md`

| Bloque | Estado | Último cambio |
| :--- | :--- | :--- |
| 1 · Tienda tipo | hecho, nombres aprobados | 2026-10-28 |
| 2 · Chile Central: red y entrada | hecho; nombres de red pendientes de aprobar | 2026-10-28 17:10 |
| 3 · Chile Central: cómputo y datos | hecho, nombres aprobados | 2026-10-28 17:45 |
| 3b · Chile Central: identidad, claves, seguridad, observabilidad | hecho, nombres por aprobar | 2026-10-28 18:05 |
| 3c · Chile Central: entrega, ambientes y herramientas con estado | hecho, nombres por aprobar | 2026-10-28 18:30 |
| 4 · Brazil South | hecho, nombres por aprobar | 2026-10-28 19:00 |
| 5 · Casa matriz y centros de distribución | hecho, nombres por aprobar | 2026-10-29 |
| 6 · Contrapartes externas | hecho | 2026-10-29 |

## Cierre de la sesión de recopilación (2026-11-06)

- Supuestos revisados por tipo de evidencia (buscador, Learn, documentos); adoptados S-24 a S-32; S-09 retirado; S-10 y S-23 corregidos. Mediciones (M) quedan para la Etapa 1.
- Sección 9 revisada con el usuario (bloques 1 y 2 cerrados con S-29 a S-32). Recuento: 79 elementos.
- Riesgos: solo anotados (`10_riesgos-para-sd-08.md`); corrección en otra sesión.
- Redacción del `.tex`: pendiente en otra sesión; todo reunido en `11_traspaso-redaccion.md` (incluye H-16).
- Diagramas: van en una sesión paralela (cruce de IDs E-NN, revisión N3 y gigante físico legible).
- Nada commiteado; nada «revisado» (lo asigna una persona).
