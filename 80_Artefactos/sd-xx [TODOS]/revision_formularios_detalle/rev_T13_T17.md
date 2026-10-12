> Detalle de la revisión de los formularios (2026-10-12). Borrador. **Nota:** cualquier hallazgo que diga que el Comité de Operación debe iniciar en el mes 16 es un falso positivo: el artículo 71 de las Bases fija «mensual desde el mes 13».

# Revisión T-13 (plan de pruebas y validación) y T-17 (protocolo de aceptación)

Archivos: `02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-13.tex` (T13) y `...-T-17.tex` (T17).
Contrastado con: Bases Administrativas (T-13 l. 2290, T-17 l. 2318, art. 17.3 l. 481-491, art. 18 l. 493-503, art. 37 l. 920, art. 70 l. 1420, art. 79-80 l. 1580+), Bases Transversales 20.1 (l. 836-848) y RT-04.11, RT-05.13/14, RT-07.04, RT-09.06, RT-20.08; Caso (RT-09.01 l. 799, congelamientos l. 695-699); sd-04 (l. 386-388), sd-07 (l. 466, 586-596, 688, 765-767), sd-09, Anexo D del sd-03, T-14 y T-18.

Resumen: 4 graves, 9 medianas, 5 bajas.

Lo que sí cumple (verificado):
- T13 contiene lo que pide la definición oficial: niveles y tipos (sec. 1), ambientes y datos (sec. 2), criterios de entrada y salida (sec. 3), automatización (columna 4 de la sec. 1) y calendario (sec. 4). Los criterios de salida coinciden con la tabla 20.1 de las Bases Transversales (70 %, integración sin error, regresión, UAT firmada, carga a 1,5x, resiliencia, DR, pentest sin críticos ni altos, WCAG 2.2 AA, dos ensayos de migración).
- Carga a 1,5 veces el peak: bien (T13 l. 122, 190, 194, 201; coincide con RT-09.06, sd-07 l. 767 y sd-09 l. 331). Estrés por separado: bien.
- Frecuencias de operación (resiliencia/DR semestral, pentest anual) coinciden con 20.1 y sd-09.
- Hitos y meses H2 a H12 de T17 coinciden con sd-07 l. 688-700 y con las Bases (H4 mes 10, H5 12, H6 13, H7 16, H8 14, H9 17, H10 18, H11 19, H12 21).
- T17 cubre lo que pide el T-17: entregables, criterios objetivos, evidencia, plazos (10 + 10 días hábiles, art. 18.3), procedimiento de observaciones y acta. Las seis condiciones del art. 17.3 están completas y bien transcritas (T17 l. 167 y 238). Art. 18.1, 18.2 y 18.4 bien aplicados.
- Línea roja Retail/Emisor respetada en ambos (resultados, conciliaciones y datos por separado, cruces solo por X-01).
- Umbrales máximos (400 ms, 3 s, 25 s, 8 s, 5 min, 2 s, 60 s) coinciden con RT-09.01 del Caso.

## Hallazgos

### Graves

G-1. Falta la prueba de venta con tarjeta propia sin enlace (meses 6 y 7).
- Ubicación: T13 sec. 4 (l. 169-201), toda la tabla de calendario; T17 H3 (l. 194-202) y l. 298.
- Qué dice: el calendario de T13 va de "Meses 1-10" a "Meses 11-12" y no incluye ningún ensayo en los meses 6 y 7. Tampoco aparece en las filas de nivel de la sec. 1 (resiliencia no menciona corte de enlace ni autonomía de 24 h). T17 solo dice en general que las pruebas de desconexión "respetarán las restricciones del Caso" (l. 298) y H3 (mes 6) no la incluye como criterio.
- Debería decir: una fila propia (meses 6-7, fuera de congelamientos y de la semana previa y los tres días del evento anual): corte provocado de 24 h en una de las tres tiendas piloto; venta con tarjeta propia contra el cupo preaprobado del nodo local (topes que fija la filial emisora); operación 24 h, retorno y conciliación; aprobada cuando la conciliación tras el retorno no supera 30 min y la Contraparte Técnica firma el acta. Incluir en T17 el criterio de aceptación y el acta (H3 o hito de piloto). Si los topes no se fijan antes del mes 6 o la prueba falla, la compra con tarjeta propia sin enlace se declara no disponible (sd-04 l. 386).
- Fuente: sd-04 l. 386-388 (cita SD-03 3.2.3); sd-08 O-02 (topes antes del mes 6); T18 l. 115 y 174; verdad_proyecto (autonomía 24 h, Caso dice 8 h, RT-03.10 pide 8 h y las Bases 24 h o el mayor).
- Sugerencia: agregar la fila y el criterio. Confirmado como omisión.

G-2. Contradicción entre documentos sobre dónde se hace el corte de 24 h (por resolver antes de redactar G-1).
- Ubicación: sd-04 l. 388 dice "corte provocado de 24 horas en una de las tres tiendas piloto"; sd-07 l. 765 y T18 l. 115 dicen "piloto técnico en preproducción aislada ... el corte afecta al entorno de prueba mientras los sistemas vigentes sostienen venta y cobro".
- Impacto: define el ambiente de la prueba (T13 sec. 2 no tiene un ambiente "tienda piloto") y qué se acepta. Una tienda real con venta real y una tienda en preproducción son pruebas distintas. Por confirmar con el equipo; T13 debe usar la versión que se elija y la sec. 2 debe agregar el ambiente "tienda piloto".
- Gravedad grave, por confirmar.

G-3. Congelamientos ignorados en el calendario de operación (meses 26, 38 y 50).
- Ubicación: T13 l. 198 ("conmutación real al cierre de cada semestre contractual (meses 26, 32, 38, 44, 50 y 56)").
- Qué pasa: con inicio en enero de 2027, el mes 26 es febrero de 2029, el 38 febrero de 2030 y el 50 febrero de 2031: caen en el congelamiento de la última semana de enero a la primera de marzo (Caso l. 699; sd-07 l. 590-592: las intervenciones productivas se programan fuera de los congelamientos). Una conmutación real de DR hacia producción es una intervención. Los meses 32, 44 y 56 (agosto) no chocan.
- T13 no menciona los congelamientos en ninguna parte (ni la ventana 1-nov a 6-ene sobre los meses 11-12, ni enero-marzo sobre los 13-15, ni la segunda semana de mayo, ni el evento anual).
- Debería decir: que cada ejercicio semestral se programa dentro del semestre fuera de los congelamientos (por ejemplo, en la semana de cierre disponible, sin atarse a febrero) y que las campañas de los meses 11-15 se ejecutan en preproducción y DR aislados. Corregir "al cierre de cada semestre" a "dentro de cada semestre, fuera de los congelamientos".
- Fuente: Caso l. 695-699; sd-07 l. 590-592 y 596; verdad_proyecto (congelamientos). Confirmado (cuenta de meses) y la solución es por confirmar.

G-4. Falta el ensayo del orden de degradación del evento anual y la prueba de 104.000 pedidos.
- Ubicación: T13 l. 130-132 y calendario (l. 189-198); T17 H7 y H12.
- Qué dice: T13 solo dice que la volumetría de 104.000 pedidos "sirve para diseñar escenarios" y que se pedirá un perfil. No hay ninguna campaña para el orden de degradación ni para suspender la publicación de una categoría.
- Debería decir: ensayo del orden de degradación y de la suspensión de publicación de una categoría (inicialmente meses 9-10, revalidado para E1 en el mes 16 y completo para E2 en el mes 18, sd-07 l. 592), y prueba de carga completa del evento (104.000 pedidos en tres días, a 1,5x el peak; RNF-22 corregido a 1,5x) antes del mes 21. Anexo D resultado 25: mes 16 ensayo del orden de degradación, mes 21 prueba de carga completa. Y T17 debe tenerlo como criterio de H7 y H12 (el resultado 25 del Anexo D no aparece en ningún hito).
- Fuente: Anexo D fila 25 (l. 33); sd-07 l. 592; verdad_proyecto (RNF-22 a 1,5 veces el peak, proyección ≈150.000).
- Confirmado.

### Medianas

M-1. H1 en el mes 3 en T17; el resto de la propuesta dice mes 2.
- T17 l. 174 ("H1 · mes 3"). sd-07 l. 466 y 688 ("H1, mes 2"); T14 l. 121, 587, 590 ("H1 (mes 2)"). La tabla de las Bases está ilegible en esa celda (l. 2640, "89"), por lo que no se puede decidir con las Bases. Alinear T17 con el sd-07/T-14 (mes 2) o corregir los tres si el mes 3 es el correcto. Por confirmar con E-25. Nota: la suma de los porcentajes de E-25 (Etapa 1 = 60 %) no sirve para decidir el mes.

M-2. T13 no cita los RT que usa y no incluye las fichas que T17 y sd-09 le delegan.
- T13 solo cita RT-07.04 (l. 124), la tabla 20.1 y el RT-09.01 del Caso (l. 130). Faltan: RT-09.06 (carga 1,5x y estrés, l. 122 y 190), RT-05.13 (dos ensayos completos de migración en preproducción, l. 127, 189, 190, 193; es el RT que corresponde, no RT-05.15), RT-05.14 (recuentos, sumas de control y muestreo dirigido), RT-04.11 (70 % bloqueante), RT-20.08 (T-17), RT-09.07/09.08 (informe de carga, degradación controlada). Agregar la columna o la nota con el RT en cada fila de la sec. 1 y en el calendario.
- Circularidad: sd-09 (l. 121, 219-225, 359, 145) dice que las fichas, herramientas, umbrales de deuda 5 %, duplicación 3 %, complejidad 15, acoplamiento 0, usabilidad (tamaño de muestra, catálogo de errores) y muestreo n=299 se fijan "en T-13"; T17 (l. 296) dice que los umbrales "se detallarán en T-13"; T17 H5 y H10 dicen "fichados en T-13". Pero T13 (l. 130) remite a "los requisitos comunes del Capítulo 9 que el SD09 relaciona" y no contiene ninguna ficha. Resultado: nadie define el umbral de varias métricas. Incluir en T13 una tabla de umbrales (aunque sea por referencia exacta a la Tabla 9.1 y 9.2 del sd-09) o decir explícitamente que las fichas se emiten antes de cada campaña.

M-3. Lista de umbrales incompleta en T13 (l. 130).
- Faltan: disponibilidad publicada ≤30 s tras una venta (RT-05.29 del Caso), sincronización tras reconexión ≤30 min (Caso RT-03.13; sd-04 l. 388), disponibilidad ≥99,9 % mensual (RT-10.01/14.03), evaluación crediticia ≤8 s (está), "confirmación de pedido ≤3 s" sin la condición "durante el evento anual" (Caso l. 799), "consulta de existencia ≤2 s indicando el grado de confianza del dato" (se omite el grado de confianza). Los P95 comunes (portal, navegación, API) quedan solo en el sd-09.

M-4. Migración de cartera: ensayos y mes 22 no reflejados.
- T13 l. 189-193 habla de ensayos de migración E1 (meses 1-12) y E2 (meses 14-17) sin mencionar la cartera de crédito (620.000 clientes con saldo), los tramos, la convivencia, la conciliación diaria ni el último corte antes del 15-oct-2028 ni el apagado de la plataforma de 2011 antes del 31-oct-2028. Se requiere que el ensayo por tramo y el retorno probado por tramo estén en el calendario (sd-07 l. 767).
- T17: H7 (mes 16) y H12 (mes 21) no tratan la aceptación de la cartera por tramos. Anexo D fila 24 dice mes 16 (primera parte) y mes 21 (segunda parte) y la verdad vigente dice migrada a más tardar en el mes 22 y cierre de remediación en el mes 24 (Anexo D fila 23). El mes 22 queda fuera de H12. Aclarar en T17 qué hito acepta el último tramo (hito mensual de Operación del mes 22) y que el último corte es antes del 15-oct-2028. Por confirmar el hito.

M-5. T17 H12 omite la Garantía de Correcto Funcionamiento.
- T17 l. 288 y 302-304: la aceptación final del mes 21 no menciona la garantía; art. 37.1 la fija como condición para la aceptación final del mes 21 (vigencia de 24 meses). T17 solo dice "ni la garantía establecida en las Bases". Agregar como criterio de H12 la constitución de la garantía (sin montos, Sobre 2 no puede llevar precios; basta citar el art. 37). Confirmado.

M-6. Criterios de T17 no siempre son objetivos con umbral.
- H2 ("documentos completos según alcance", "observaciones de diseño cerradas"), H3 ("pruebas de monitoreo consultables"), H6 ("sin observaciones bloqueantes"), H8, H11 ("usuarios formados/certificados según plan") no traen umbral ni medida. El T-17 oficial pide "criterios de aceptación objetivos". Sugerencia: agregar para cada uno un umbral (100 % de requisitos con IDs únicos, 0 observaciones bloqueantes, 5 ambientes con evidencia de provisión, X % de usuarios certificados definido en el plan de capacitación, etc.). El porcentaje del plan de capacitación es por confirmar con T-18.

M-7. Roles y nombres que no coinciden con el resto de la propuesta.
- T13 sec. 6 (l. 236-251): "Líder QA", "Arquitectura de rendimiento / Canales", "SRE/Operaciones", "UX/Accesibilidad", "Datos/Migración" no coinciden con los roles del sd-07/sd-09: Líder de Calidad y Pruebas (más dos Ingenieros QA), Líder de Datos, Encargado de Seguridad de la Información, Operaciones/SRE, Líder de Implantación y Cambio, Líder Funcional/Arquitecto. T13 no menciona al Jefe de Proyecto (que en sd-09 l. 169 reserva tiempo y recursos para corregir y repetir pruebas) ni a la Junta de no conformidades ni al Comité de Proyecto/Arquitectura para escalar. "Canales" no es un área de OSS (áreas de trabajo del sd-01: arquitectura, datos, seguridad, calidad, operación, gestión del cambio). Por confirmar con el sd-01/sd-06.
- T17: H1 "Líderes Retail y Emisor" (l. 182) y "Infraestructura/DevOps" (l. 202) también son nombres no usados en otros documentos.

M-8. T17 y art. 79 en la aceptación mensual de Operación (l. 306-312).
- No cita art. 79.2 (informe de nivel de servicio dentro de los primeros cinco días hábiles de cada mes) ni 79.3 (ante discrepancias prevalece la medición del CLIENTE salvo error metodológico acreditado). T17 dice "Ante discrepancias se preservan datos originales, fórmula y justificación", sin decir quién prevalece. Agregar ambas reglas. Confirmado.
- Tampoco recuerda la consecuencia del art. 17.3 / art. 80 por extender una marcha blanca por causa imputable (T17 l. 167 la omite; solo dice "a costo del ADJUDICATARIO"). Baja si se prefiere no citar multas (el Sobre 2 no lleva precios).

M-9. Datos de prueba: tensión entre T13 y la migración de cartera.
- T13 l. 154-159 y 127: preproducción con datos "sintéticos/anonimizados"; "no se trasladan datos productivos salvo autorización formal". Pero los dos ensayos de migración de cartera viva (RT-05.13, sd-09 l. 329) se ejecutan en preproducción con datos reales del Emisor. T13 debe decir expresamente que los ensayos de migración usan datos productivos del Emisor bajo autorización, controles y segregación, o cómo se enmascaran sin perder la conciliación de saldos. Por confirmar con el dueño del Emisor.
- La fila DR (l. 156) dice "Réplicas bajo controles de continuidad", sin decir si la conmutación real de los meses 11-12 y 18 (T13 l. 190, 194) se hace sobre producción o sobre el ambiente de recuperación, lo que es clave para G-3.

### Bajas

B-1. Nombres: T13 l. 225 y T17 l. 120 escriben "Filial Emisora" con mayúscula; el glosario fija "filial emisora" (minúscula). T13 l. 251 "Ancoa/Filial".
B-2. T17 usa ADJUDICATARIO y CLIENTE en voz propia (l. 118-143, 153-167, 290) y T13 usa "Cliente"; el glosario reserva ADJUDICATARIO/CLIENTE para citar las Bases y pide "Cliente" en el resto. Unificar.
B-3. T13 l. 165 y sd-09 l. 347 usan listas de estados ligeramente distintas ("ejecutado conforme/no conforme" vs "conforme/no conforme"). Alinear.
B-4. T17 l. 137: "La revisión de la nueva entrega se computa conforme al artículo 18.3 y al contrato" no precisa si el CLIENTE vuelve a tener diez días hábiles (el art. 18.3 no lo dice). Por confirmar y declarar el plazo.
B-5. T13 automatización (columna 4 de la sec. 1): se dice "ejecución continua en CI", sin herramienta, porcentaje de automatización ni qué pruebas se automatizan (sd-09 l. 219 y 323 sí lo hace en parte, y fija las herramientas en T-13 "antes del primer pipeline"). Agregar una frase con la regla (qué se automatiza y qué es manual) o remitir a la sec. del sd-09.

## Observaciones que no son de T13/T17 (para otros revisores)
- sd-09 l. 194 dice "catálogo oficial v3.0"; la verdad vigente es v3.1 (308 elementos).
- sd-09 l. 329 cita RT-05.15 de las Bases Transversales para "cartera viva"; en el Caso el RT-05.15 (l. 795) sí incluye la cartera completa, por lo que es correcto, pero el RT-05.13 (dos ensayos) es el que corresponde al criterio de aceptación (el sd-09 l. 363 sí lo cita).
- Anexo D fila 24 dice "mes 21 (segunda parte)" para la cartera; la verdad vigente dice a más tardar mes 22.
