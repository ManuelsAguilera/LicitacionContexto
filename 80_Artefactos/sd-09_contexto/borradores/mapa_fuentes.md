---
tipo: mapa-de-fuentes
parte: T7-09
estado: borrador
actualizado: 2026-10-11
---
# Mapa de fuentes, cifras, roles y plazos de SD09

Este mapa prepara la integración del Plan de Calidad y de las dos figuras de [propuesta_figuras.md](../propuesta_figuras.md). Sirve para distinguir compromisos de Bases, decisiones de la propuesta y datos todavía abiertos. La precedencia de contenido es Bases Administrativas, Bases Transversales y Caso 09; el Comunicado 10 fija estructura. El Anexo D concreta resultados del Caso. Los capítulos SD06/SD07 son diseño vigente del proponente y no reemplazan esos mandatos.

## Cifras y decisiones que deben conservarse

| Dato | Fuente y carácter | Uso/trazabilidad SD09 |
|---|---|---|
| 70 % cobertura automatizada mínima en lógica de negocio, con bloqueo en CI | Bases Administrativas, cap. 4, línea 649; obligación. SD06, apartado 6.2.5, lo conserva como bloqueo. | Umbral de entrada/salida de CI; identificar población y cálculo en el futuro T-13. No confundir con el 80 % siguiente. |
| 80 % de cobertura en código nuevo | SD06, apartado 6.2.5; objetivo/política interna del proponente, no el mínimo contractual. | Reportarlo por separado del umbral obligatorio de 70 %. |
| Deuda técnica ≤5 % y duplicación ≤3 % | SD06, apartado 6.2.3 (deuda) y límite de duplicación referido por validación_revisor.md, H03, que cita SD06 líneas 3174–3179. Política del proponente. | Medir deuda y duplicación separadamente de cobertura; H03 indica que T02 todavía no expresa bien límite, unidad, población, exclusiones ni decisión de control. |
| Carga a 1,5× peak declarado | Bases Transversales, 20.1; obligatoria antes de cada paso productivo. | H05 pide probar los umbrales del Capítulo 9 bajo 1,5× por escenario. No derivar TPS/throughput de un volumen agregado. |
| 99,9 % disponibilidad mensual; RTO ≤4 h, RPO ≤15 min | Bases Transversales, Art. 20; mínimos críticos, salvo exigencia superior del Caso. | Trazar pruebas de disponibilidad y DR; separar resiliencia/recuperación. Los detalles y referencias están en transversales.md, T05/T10. |
| Meses 1–12 desarrollo E1; 13–15 marcha blanca E1; 16 producción E1; 13–18 desarrollo E2; 19–20 marcha blanca E2; 21 producción E2 e inicio de operación; operación hasta mes 56 | Bases Administrativas, Art. 17.1–17.2; calendario obligatorio, indivisible y no negociable. | Anclas para la figura 9.3 y calendario de campañas. SD07, Tabla 7.5, da fechas equivalentes bajo supuesto de inicio enero 2027. |
| Condiciones copulativas de salida de marcha blanca | Bases Administrativas, Art. 17.3: sin incidentes críticos/altos abiertos; volumen real por ≥4 últimas semanas; disponibilidad/desempeño sostenidos; conciliación sin diferencias inexplicadas; capacitación/certificación; acta de Contraparte Técnica. | Constituyen puertas contractuales antes de M16/M21. Si no se cumplen, la extensión es a costo del adjudicatario y no desplaza las fechas siguientes. |
| 10 días hábiles de revisión + 10 días hábiles para subsanar | Bases Administrativas, Art. 18.3. El acta de Contraparte Técnica es requisito de aceptación (Art. 18.1). | Incluir en planificación de entregables y responsables; segunda presentación con observaciones de igual naturaleza cuenta como atraso imputable. |
| 28 resultados; 115 criterios únicos (58 resultados + 57 transversales); 11 grupos T01–T11; seis pilotos/21 criterios incluidos; 38 brechas (P01–P08, B01–B30) | Anexo D lista R01–R28. Verificación documental SD09 registra los conteos; revisión_revisor los coteja. | Volumen de la matriz interna, no cobertura exhaustiva de todos los RF/RNF/RT ni contenido contractual autónomo. No describirlos como pruebas ejecutadas o aceptaciones. |
| Evidencias ejecutadas 0; aceptaciones 0 | verificacion_documental.md, tabla de conteos. | Todos los escenarios y evidencias son previstos. La matriz tiene estado de diseño con brechas y aceptación humana pendiente. |
| Ventana de tres meses para tasas anuales; inicio enero 2027; mes 24 = diciembre 2028 | Prefacio del Anexo D; ventana y fecha de inicio son propuesta/supuesto SUP-26, no fechas adjudicadas. | Mantener explícito el carácter de supuesto. Las tasas del caso incluyen 0,3 % cancelación anual, <2 % diferencia de inventario, merma <1 % (R02/R04/R05). |
| 104.000 pedidos en tres días | Anexo D, R25; también RNF-22. | Es volumen de carga declarado para prueba; no equivale por sí mismo a tasa peak ni sustituye el perfil presencial/digital separado. |
| 620.000 clientes con saldo; objetivo cero diferencias inexplicadas en migración | Anexo D, R24 (meses 16 y 21); restricción del Caso. | Dos hitos/partes de migración; evidencia de conciliación diaria por tramo. |

## Roles, autoridades y calendario de aseguramiento

| Rol/actor | Responsabilidad respaldada | Fuente |
|---|---|---|
| Líder de Calidad del proponente | Consolidar la estrategia, método, evidencia, resultados y observaciones. Es un rol clave exigido como parte del equipo nominado. | Bases Administrativas, Art. 31/criterios de equipo (línea 850); propuesta_figuras.md resume flujo; SD06, 6.2.5, distingue evidencia CI de expediente y aceptación. |
| Contraparte Técnica del cliente | Revisar entregables y suscribir el acta; firma las aceptaciones de etapa. La aceptación no se automatiza por CI. | Bases Administrativas, Arts. 17.3, 18.1–18.4; SD06, 6.2.5. |
| QA + responsables de dominio/arquitectura/seguridad | Diseñar y ejecutar campañas por nivel; conservar resultados reproducibles, hallazgos y cierres. | Bases Transversales, 20.1; SD06, 6.2.4–6.2.5; detalle interno en matriz SD09. |
| Tercero independiente | Ejecutar prueba ofensiva antes de cada producción y anualmente durante operación. Sin hallazgos críticos/altos abiertos para salida. | Bases Transversales, RT-11.20 y 20.1; SD06, 6.2.4. La atribución fue corregida en verificacion_documental.md. |
| Cliente/operación de tienda o centro de distribución | Ejecutar su parte de resultados compartidos; preparación de personal, conciliación y operación real dependen parcialmente del cliente. | Anexo D, prefacio y R02, R04, R09, R15 y R26. Contraparte Técnica firma. |
| Cumplimiento y responsables del Emisor | Validar obligaciones y evidencias del negocio regulado, preservando separación de datos Retail/Emisor. | Anexo D, R17–R24/R28; SD06 y SD03 (arquitectura); matriz SD09. La separación es decisión crítica del Caso, no intercambiable por una métrica agregada. |

Calendario mínimo de pruebas contractual (Bases Transversales, 20.1): unitarias/componente continuamente; integración tras despliegue a QA; sistema/regresión antes de promoción a Preproducción; UAT antes de certificación; carga/estrés antes de cada producción; resiliencia antes de producción y semestral en Operación; DR antes de producción y semestral; seguridad ofensiva antes de producción y anual; accesibilidad antes de cada producción; dos ensayos de migración previos a migración definitiva. SD07, Tabla 7.6, coloca certificaciones en M12 y M18; marchas blancas M13–15 y M19–20; producciones M16 y M21.

## Lectura de Anexo D por grupos de resultados

- R01–R09: existencias, cancelaciones, exactitud, merma y precios. Hitos principalmente M16 o M21; R02, R04 y R09 son compartidos. Fuentes exactas: Anexo D, filas/líneas 9–17. Hay metas del proponente y políticas aún por acordar (por ejemplo, tolerancia R01, política de precio en sala R06/R09).
- R10–R15: pedidos, despacho, comisiones, marketplace y posventa; M21. R15 es compartido. Fuentes: Anexo D, líneas 18–23.
- R16–R24 y R28: originación, evidencia financiera, separación Emisor/Retail, remediación regulatoria y migración; principalmente M16/M21 y operación hasta M24 para remediación. Fuentes: Anexo D, líneas 24–32 y 36. La retención crédito + seis años de R19 es obligación RT-05.10 (Caso), mientras recuperación en cinco minutos/diez años es propuesta; H01 exige separar ambas.
- R25–R27: resiliencia/evento de carga, experiencia de pedido y atribución de merma; M16/M21 y primer evento posterior cuando aplica. Fuentes: Anexo D, líneas 33–35. No convertir 104.000 pedidos/3 días en TPS peak.

## Brechas materiales para resolver antes de cerrar el capítulo

1. **No presentar cifras internas como mínimos contractuales.** Separar 70 % obligatorio de 80 % objetivo; 5 %/3 % son política SD06; 1,5× peak sí es obligación. Revisar población, unidad y evidencia de cada porcentaje.
2. **Unir desempeño y nivel de carga.** H05 de validacion_revisor.md: T07 separa carga a 1,5× peak y medición de umbrales; el protocolo debe comprobar los umbrales bajo esa carga por escenario, aparte del estrés hasta quiebre.
3. **Corregir trazabilidad de requisitos.** H01: R19 atribuye a propuesta una retención obligatoria del Caso RT-05.10; separar obligación de recuperación propuesta. H02: proyección trimestral de capacidad tiene frecuencia obligatoria RT-09.09/Art. 25, no opción. H03: explicitar ≤3 % duplicación SD06. H04: rotación automática de secretos según RT-04.09.
4. **Completar la aceptación humana.** No hay pruebas ejecutadas ni actas. Las metas propuestas en Anexo D requieren validación del cliente; el registro interno es parcial y no cubre todo el catálogo ni T-12/T-13.
5. **Resolver parámetros y aplicabilidad abiertos** identificados por verificacion_documental.md: tolerancia R01; indicadores por tarea/perfil T06-02; aplicabilidad T06-07; alerta T05-06; estímulos/límites T10-05; marco, madurez e indicadores T11-01/02/03; además de decisiones distribuidas en las 38 brechas.
6. **Evitar que fecha supuesta parezca contractual.** Anexo D/SD07 usa enero de 2027 como inicio supuesto y mes 24/diciembre de 2028; mantener el calendario expresado primero en meses contractuales.

## Referencias de consulta

- [Bases Administrativas](../../../00_Bases/Bases_Administrativas.md), Arts. 17–18, 31 y capítulo 4.
- [Bases Transversales](../../../00_Bases/Bases_Transversales.md), sección 20.1 y RT-11.20.
- [Comunicado 10](../../../00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md), capítulos SD09 9.1–9.3 y reglas de figuras.
- [SD06 LaTeX](../../../02_Propuesta/latex_final/sd-06/OSS-Subdocumento6.tex), apartados 6.2.3–6.2.5 (política, DevSecOps, pruebas y evidencia).
- [SD07 LaTeX](../../../02_Propuesta/latex_final/sd-07/OSS-Subdocumento7.tex), Tabla 7.5 y apartados 7.3/Tabla 7.6 (fechas, hitos y camino crítico).
- [Anexo D](../../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md), filas R01–R28 (líneas 9–36).
- [Validación del revisor](../../../90_Referencia/calidad/validacion_revisor.md), hallazgos H01–H05 y límites del examen.
- [Verificación documental SD09](../verificacion_documental.md), conteos, límites, estado de pruebas y referencias.
- [Propuesta de figuras](../propuesta_figuras.md), ubicación y contenido previsto de figuras 9.2/9.3.
