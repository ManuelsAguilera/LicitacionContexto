# Cambios que exigen D4 y D8 (ratificadas 2026-10-11)

Documento de contexto, no entregable. Consolida lo que hay que cambiar o dejar anotado tras ratificar dos decisiones del sd-08. Las líneas se leyeron el 2026-10-11 en `02_Propuesta/latex_final/`; si el archivo difiere, manda el archivo.

## Decisiones ratificadas

- **D4:** SUP-26 se mantiene. El proyecto comienza en enero de 2027 y los 56 meses terminan en agosto de 2031. R-12, R-13, R-24 y R-25 se escriben dependiendo de esa fecha y con una frase que diga que se recalculan si el cliente la cambia.
- **D8:** Para dimensionar y para R-15 se usan **14 tiendas sin enlace de respaldo** (6 en centro comercial y las 8 a la calle, incluida Coyhaique). Es el peor caso de SUP-28. El Caso solo acredita 7 (6 en centro comercial más Coyhaique); el levantamiento de enlaces por tienda (cuenta 1.2.1) confirmará o corregirá el número.

## A. Cambios en otros subdocumentos (obligatorios)

| N.º | Archivo y línea | Qué dice hoy | Qué hay que cambiar | Decisión |
| :-- | :-- | :-- | :-- | :-- |
| C-1 | `sd-02/OSS-Subdocumento2.tex` l. 497 (tabla C5) | «Tiendas sin el enlace de respaldo exigido: 7 de 15, meta 0 de 15» | Cifra y denominador. Con D8 es «14 de 22» (7 acreditadas por el Caso) y la meta «0 de 22». El «15» no coincide con ninguna cifra del Caso (22 tiendas, 14 en centro comercial) | D8 |
| C-2 | `sd-02/OSS-Subdocumento2.tex` l. 211 (resumen C5) | «Seis de las 14 tiendas en centros comerciales y la de Coyhaique carecen de enlace de respaldo» | Es el dato del Caso (7) y está bien. Agregar que el dimensionamiento asume 14 por SUP-28, para que el lector no vea dos cifras sin explicación | D8 |
| C-3 | `sd-02/OSS-Subdocumento2-Anexos.tex` RT-09.05 (l. ~2794) | «Enlace de respaldo de las 14 tiendas dependientes de red de centro comercial» | Mezcla dos conjuntos: las 14 tiendas **de centro comercial** y las 14 **sin respaldo** (6 de centro comercial y 8 a la calle). Reescribir como «las 14 tiendas sin respaldo acreditado (SUP-28)» | D8 |
| C-4 | `sd-02/OSS-Subdocumento2-Anexos.tex` RT-02.11 (l. ~2508) | «enlace de 14 tiendas» como punto único de falla | Misma ambigüedad que C-3; precisar «las 14 tiendas sin respaldo (SUP-28)» | D8 |
| C-5 | `sd-04/OSS-Subdocumento4.tex` l. 421 | Declara el supuesto de las ocho tiendas a la calle y remite a SUP-28 de SD-02 | Sin cambio: está alineado con D8. La copia `latex_final/sd-04.tex` (ver C) no tiene la remisión a SUP-28 | D8 |
| C-6 | `sd-07/OSS-Subdocumento7.tex` l. 273 | La marcha blanca de la Etapa 1 cabe dentro del congelamiento | Con enero de 2027 los meses 13 a 15 (enero a marzo de 2028) caen casi enteros en los congelamientos (hasta el 6 de enero y de la última semana de enero a la primera de marzo). Corregir la afirmación o explicar cómo se absorbe. Era I-03 | D4 |
| C-7 | `sd-02/OSS-Subdocumento2-Anexos.tex` l. 3325 (SUP-26) | «la fecha debe confirmarse antes de cerrar la planificación» | Sin cambio de contenido. Es la condición que el sd-08 hereda; el disparador de reevaluación del 8.1 debe remitir a ella | D4 |

## B. Cambios en el sd-08 y sus documentos de contexto

| N.º | Dónde | Qué hacer |
| :-- | :-- | :-- |
| B-1 | `registro_candidatos.md` pregunta 4 | Marcarla como respondida (D4 ratificada) |
| B-2 | `trazabilidad_riesgos.md` I-06 (l. 72) | Cambiar la sugerencia «rango de 7 a 14» por «14, con 7 acreditadas por el Caso»; cerrar I-06 en cuanto C-1, C-3 y C-4 estén aplicadas |
| B-3 | `registro_candidatos.md` R-15 (l. 52) | Ya dice catorce. Agregar que 7 están acreditadas y que el levantamiento 1.2.1 puede reducir la cifra |
| B-4 | 8.1 Plan de riesgos (F2) | Incluir «cambio de SUP-26 o de SUP-28» como motivo de reevaluación del registro |
| B-5 | 8.2 ficha de R-15 | Usar 14 como cifra del peor caso y justificar la calificación con SUP-28 |
| B-6 | 8.2 fichas de R-12, R-13, R-24, R-25 | Escribir las fechas calendario de enero de 2027 y la frase de recálculo; en R-24 mantener la consulta abierta al mandante sobre «antes de 2029» |
| B-7 | `guia_progreso_sd-08.md` §3 y `relevo_sesion_2026-10-11.md` §3 | D4 y D8 pasan a «ratificada por el usuario el 2026-10-11» |
| B-8 | `avisos_otros_subdocumentos.md` | Agregar C-1 a C-6; I-06 queda apuntando a C-1, C-3, C-4 |

## C. Observaciones aparte (no son de D4 ni D8)

- Existe `02_Propuesta/latex_final/sd-04.tex` en la raíz, junto a `sd-04/OSS-Subdocumento4.tex`. Parece una versión anterior (el texto de la l. 421 es distinto: no cita SUP-28). Confirmar con el equipo cuál rige antes de editar y no corregir la copia equivocada.
- Los cambios C-1 a C-7 se hacen en el `.tex` (manda sobre el `.md`); el `sd-02.md` l. 363 repite «7 de 15» pero es solo contexto.
- Ninguno de estos cambios se aplicó: el sd-08 los necesita coherentes, pero cada archivo pertenece a otro subdocumento y los edita su responsable.
