# Revisión general de SD08 y Formulario T-16 (12 de octubre de 2026)

## Estado de la base

La rama `work` incorpora `origin/main` en `618451a` y no presenta divergencia con esa referencia. La revisión se hizo sobre los archivos canónicos LaTeX de SD08 y T-16, los subdocumentos 2, 3, 4, 7 y 9, el Anexo D, el catálogo de criterios y el Caso 09 original. Los cambios de esta sesión permanecen en el árbol de trabajo.

## Correcciones aplicadas

- T-16.1 distingue los datos del Caso 09 de la identificación y calificación propuestas, con citas de capítulos y folios para los antecedentes destacados. Se precisó en SD08 que los 2,6 % y la meta de menos de 3 % son cálculo y propuesta del apartado 2.2.3; los 400.000 cambios diarios sí son dato del Caso, capítulo 14.1, página 31.
- Se corrigieron los disparadores de R-05, R-18, R-31 y R-34. La desigualdad de R-18 es coherente con la meta de inventario inferior a 2 %, y la de R-34 con la meta de precio inferior a 3 %.
- R-18 abarca los cortes de todas las olas hasta el mes 15. R-17 exige demostrar recuperación geográficamente separada si no se autoriza Brazil South; DC-02 queda como respaldo complementario. R-31 separa las obligaciones del cliente y del proponente.
- Se alineó el resultado 9 del Anexo D y la hoja `9_Criterios_Aceptacion` del catálogo v3.1 con la meta de menos de 3 % del SD02. Manuel Aguilera confirmó que esa cifra queda comprometida en la oferta sin negociación posterior. El catálogo v3.1 sigue identificado como borrador; su adopción requiere el control de cambios previsto por SD09.
- La simulación ya no atribuye al hito del mes 16 un riesgo de peak que ocurre después de ese hito (R-24). Con las mismas extracciones aleatorias, el P80 del mes 16 con respuestas baja de 12,5 a 12,2 semanas en la agregación solapada y de 15,3 a 13,8 en la suma en serie. Se corrigieron la Tabla 8.8 y sus explicaciones. R-24 sigue en el registro y en el cálculo de horas esperadas.

## Comprobaciones y límites

- El registro conserva 37 riesgos y 8 oportunidades. Los productos de probabilidad por impacto, las horas esperadas y las razones de respuesta revisadas son coherentes con sus tablas: 6.496 horas iniciales, 3.688 residuales, 2.808 de reducción y 1.660 de acciones.
- La simulación es indicativa: usa nueve eslabones simplificados y no sustituye la red CPM de T-15. El P80 expresa exposición, no holgura disponible. Manuel Aguilera confirmó una bolsa adicional de 3.688 HH, que eleva el esfuerzo comprometido de 40.946 a 44.634 HH. T-15 la reparte en cuatro frentes y ventanas; la dotación nominal por rol y mes aún debe conciliarse internamente con SD12 antes de afirmar una recuperación concreta del P80.
- La meta de precio inferior a 3 % queda comprometida desde la oferta para las tiendas habilitadas al mes 16 y se mide con pares precio exhibido/precio cobrado por tienda. La residencia y la alternativa de recuperación del Emisor dependen de una decisión jurídica/regulatoria y de pruebas de RTO/RPO; el texto de R-17 las deja como condiciones de diseño, no como cumplimiento probado.
- Se incorporó al SD08 la tabla de uso de IA por sección y Formulario T-16, con Manuel Aguilera como revisor humano declarado y las comprobaciones automáticas diferenciadas.
- Validación local: `check.py --parte T7-08 --dry-run`: 0 errores y 0 avisos; verificaciones de plantilla y redacción: correctas; seis pruebas de simulación: correctas; `git diff --check`: correcto. No se pudo recompilar el PDF en este entorno por ausencia del paquete TeX `ulem.sty`.
