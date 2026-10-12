# Revisión y propuesta de ampliación SD09 · apartado 9.3 · revisión 9.3

**Destino:** propuesta de integración en `02_Propuesta/latex_final/sd-09/OSS-Subdocumento9.tex`, exclusivamente en 9.3. Este archivo es material de trabajo, no texto canónico.

**Fuentes revisadas:** `AGENTS.md`; Comunicado 10, capítulo 9; SD09 canónico; SD07 canónico; `90_Referencia/calidad/contextoCalidad.md` completo. Para concretar la relación EDT/hitos se contrastaron el diccionario de contexto de la EDT y la Tabla 7.7 de SD07. Los paquetes no detallados en SD07 canónico se tratan como ramas/cuentas de control; no se inventan paquetes, esfuerzo, ni fechas.

## Matriz criterios → ubicación actual → profundidad → brecha

| Criterio esperado | Dónde aparece hoy en SD09 | Profundidad actual | Brecha que resuelve la ampliación |
|---|---|---|---|
| Actividades de calidad ancladas a EDT y cronograma de Cap. 7 (Comunicado 10, 9.3) | 9.3, párrafos sobre 1.9, 1.8, 1.7, 1.12 y periodos de etapa | Identifica ramas y propósito; refiere a SD07 | Falta una vista compacta de producto verificable, responsable y hito por tramo, que pueda seguirse desde EDT a expediente y recepción. |
| Cobertura de artefactos y evidencia por paquete/hito | 9.2 describe expediente, trazabilidad, QA, pruebas, migración; 9.3 describe certificaciones, marchas blancas y operación | Evidencia bien definida a nivel de ejecución; la asociación EDT↔evidencia está narrada y parcial | Añadir matriz de evidencia para cuentas de control publicadas (1.4, 1.7–1.9, 1.11–1.15) y relación a H1–H12. El T-14 completa asignaciones paquete a paquete; no suponer mapeos E-25 ausentes. |
| Solapamiento real de etapas | 9.3 describe M13–15 y M19–20, fases, pruebas y aceptación por etapa | Fechas y diferencias están descritas | Explicar control de concurrencia de personas, ambientes, cambios, datos, versiones y ventanas operacionales, con evidencia de capacidad; SD07 asigna 1.007 h a marcha blanca E1 y 2.628 h a construcción E2 en M13–15, y 267 h a marcha blanca E2 en M19–20, pero no desglosa aquí la carga mensual de QA. |
| Ambientes, configuración y versiones | 9.2 enumera Desarrollo, QA, Preproducción, Producción y DR; pide equivalencia en preproducción y expediente con versiones/configuración | Controles robustos; integración temporal implícita | Hacer explícita la línea base inmutable de cada candidato, promoción del mismo artefacto, aislamiento de datos y control de versiones/configuración simultáneas en M13–20. No fijar productos ni versiones de herramientas aún no acordados. |
| Gestión de cambios con impacto en criterios, pruebas, EDT y aceptación | Último párrafo de 9.3 remite a control de cambios SD06; 9.2 define puerta de Cambio | Relación formulada, falta circuito operativo de impacto/cierre | Hacer legible el flujo: solicitud/defecto, impacto cruzado, autorización según SD06, actualizar baselines, repetir pruebas dirigidas y regresión, reabrir no conformidad si corresponde; evaluar hito/acta solo conforme a contrato. |
| Gates y tratamiento de no conformidad | 9.2 define puertas de Cambio, CI, QA, Preproducción, Acta, defectos bloqueantes y reejecución; 9.3 define salida de marcha blanca | Criterios técnicos y responsables claros | Completar el encadenamiento EDT→gate→hito, separar gate interno de aceptación contractual y explicar flujo de no conformidad/corrección/reejecución/cierre con registro auditable. |
| Quién produce, verifica y acepta; vínculo a contrato/pago | 9.2 asigna QA, dueños funcionales, Jefe de Proyecto y Contraparte Técnica; cierre dice acta habilita tratamiento de pago; cierre de 9.3 relaciona acta y E-25 | Responsabilidades y límites económicos ya correctos | Integrar el RACI práctico al calendario. Preservar Art. 18 (revisión/subsanación) y E-25 (evidencia y pago); no asignar porcentajes, crear retenciones, aceptación tácita, recepción provisional/definitiva ni condiciones adicionales. |
| Capacidad y protección del esfuerzo de calidad | 9.1 habla de costo de calidad y consumo; 9.3 menciona dependencias y T-15 | Se controla esfuerzo por categoría, pero el solapamiento queda a la nivelación global SD07/T-15 | Explicitar que QA/Seguridad/Datos/Implantación confirman cobertura simultánea según T-15, reservan responsables distintos para ejecución/revisión donde se exige independencia y levantan conflicto de capacidad antes de comprometer un gate. Sin inventar dotación ni horas. |
| Calidad en operación hasta M56 | 9.3 vincula 1.15, prácticas 1.9/1.8, pruebas semestrales/anuales y aceptación final | Cobertura adecuada, evidencias dispersas | Consolidar que cada ciclo de operación conserva release, monitoreo, defectos, regresión y evidencia periódica bajo el mismo registro de criterios y control de cambios. |

## Inserciones LaTeX propuestas

Las inserciones siguientes van en el apartado `\section{9.3 Alineación con Plan de Trabajo}`. Mantienen las explicaciones técnicas existentes de 9.2 y 9.3; aportan las conexiones EDT-calendario-evidencia. Incorporar después del párrafo inicial que presenta las ramas EDT y antes de `\subsection` nueva o de las figuras; distribuir según indicación de ubicación.

### Ubicación 1: después del párrafo inicial de 9.3 — trazabilidad de los paquetes y expediente

```latex
\subsection{9.3.1 Productos de calidad vinculados a la EDT}

Cada cuenta de control de calidad deja un producto comprobable y una relación explícita con los criterios de salida que atiende. La matriz de trazabilidad de QA enlaza identificador y versión del criterio, requisito de origen, paquete EDT, hito E-25 cuando corresponde, caso de prueba, versión candidata, ambiente y evidencia. En el Formulario T-14 se conserva el detalle por paquete; este plan fija el contenido mínimo del expediente para que sus entregables puedan recorrerse desde la EDT y el calendario hasta la decisión de conformidad.

La Tabla 9.4 resume los productos de las ramas habilitantes que alimentan la aceptación. Cuando E-25 no asocia un hito individual a un paquete, la tabla presenta la contribución técnica al hito de etapa sin afirmar que el paquete sea por sí mismo un hito de pago.

\textbf{Tabla 9.4: Productos de calidad, evidencia y conexión con EDT y E-25}

\begin{longtable}{p{0.13\linewidth}p{0.22\linewidth}p{0.23\linewidth}p{0.18\linewidth}p{0.16\linewidth}}
\toprule
EDT / ventana & Producto verificable & Evidencia conservada & Revisión / dueño & Hito relacionado \\
\midrule
\endhead
1.4, 1.9.1--1.9.2; M1--12 & Ambientes habilitados, plan de pruebas y reglas de revisión/gates & Inventario y topología por ambiente; permisos y separación de datos; configuración y versiones; plan versionado; reglas de promoción & Arquitectura/DevOps entrega; QA verifica; Contraparte revisa el entregable aplicable & H3 (M6) para ambientes; H4 (M10) software E1 para pruebas \\
1.7 y 1.9.3--1.9.4; M5--12 & Ensayos de migración y campañas funcionales/no funcionales de E1 & Casos, datos y perfil; recuentos y sumas de control; resultados, defectos, conciliación por dominio; informes de desempeño, resiliencia y recuperación & Líder de Datos y dueños de Retail/Emisor validan su dominio; QA verifica evidencia & H4 y H5 (M10 y M12), según entregable aceptado \\
1.8 y 1.9.3--1.9.8; hasta H5 & Controles de seguridad y certificación de calidad E1 & Matriz de controles; informe independiente de intrusión y retest; trazabilidad de criterios, cobertura de pruebas, defectos y resolución; informe de certificación & Seguridad y QA preparan; dueños de negocio validan sus reglas; Contraparte Técnica acepta el hito & H5 (M12), base de H6 y H7 \\
1.11--1.13; M13--16 & Despliegue reversible, marcha blanca y cierre E1 & Hash/identificador del artefacto; bitácoras de despliegue/retorno; serie de mediciones e incidencias; conciliación; capacitación certificada; acta del hito & Implantación y QA operan/verifican; responsables de dominio confirman; Contraparte suscribe el acta & H6 (M13) inicio; H7 (M16) paso a producción y cierre \\
1.2, 1.3, 1.5, 1.8--1.9; M13--18 & Línea base, software, controles y certificación E2 & Baseline E2; revisión de impacto; pruebas funcionales/no funcionales, seguridad, desempeño, migración e integración; versión candidata y defectos cerrados & Líderes de cada rama entregan; QA verifica; dueños de negocio validan resultados de dominio & H8 (M14), H9 (M17), H10 (M18) \\
1.11--1.13; M19--21 & Marcha blanca E2 con E1 en producción y aceptación final & Evidencia por etapa; conciliación entre servicios según diseño aprobado; monitoreo E1/E2 por separado; fallos, retornos y resolución; capacitación; acta final & Operación protege E1; Implantación y QA acompañan E2; Contraparte acepta el hito & H11 (M19) inicio; H12 (M21) paso a producción y aceptación final \\
1.9, 1.8 y 1.15; M21--56 & Calidad del servicio y campañas periódicas comprometidas & Versión desplegada; métricas y eventos; regresión afectada; incidentes y correcciones; informes de resiliencia/DR semestrales y pentest anual & Operación/SRE conserva; QA verifica; Seguridad coordina tercero independiente; Contraparte revisa conforme a hitos aplicables & H12 y los hitos mensuales de operación definidos por E-25 \\
\bottomrule
\end{longtable}

\textbf{Fuente:} Elaboración propia a partir del SD07, Formulario E-25 y ramas EDT; el detalle por paquete permanece en el Formulario T-14.

Para cada ejecución, QA conserva un expediente con criterio y requisito, paquete y etapa, identificador/hash del artefacto, commit o versión fuente, configuración desplegada, ambiente, datos y perfil, método e instrumento, resultado esperado y observado, evidencia primaria, defectos, responsable y decisión de revisión. Si el mismo candidato se prueba en más de una etapa o ambiente, cada ejecución conserva su propio registro y su vínculo al candidato promovido. Una certificación resume evidencia trazable; no reemplaza los resultados de origen ni convierte pruebas no ejecutadas en conformes.
```

### Ubicación 2: luego de la explicación del solapamiento M13–15 y M19–20 — capacidad y configuración

```latex
\subsection{9.3.2 Capacidad, ambientes y versiones durante el solapamiento}

La coordinación de calidad en los meses 13 a 20 se trata como dos corrientes de trabajo con prioridades y líneas base separadas: cierre y operación supervisada de la Etapa 1, y construcción y certificación de la Etapa 2. En M13--15 SD07 estima aproximadamente 1.007 horas para marcha blanca/estabilización de E1 y 2.628 horas para construcción de E2; en M19--20 estima aproximadamente 267 horas de marcha blanca de E2, mientras E1 ya está en producción. Estas magnitudes describen el plan total de trabajo y no asignan por sí solas capacidad específica de QA.

Antes de cada ventana de certificación, el Líder de Calidad y Pruebas contrasta la curva mensual y por frente del Formulario T-15 con el calendario de campañas de T-13: ejecución funcional y no funcional, revisión independiente, triage y repetición de pruebas, preparación del expediente y atención de observaciones. Líderes de Desarrollo, Seguridad, Datos, Implantación y Operación confirman disponibilidad de las personas que producen o validan evidencia. La asignación preserva la independencia ya establecida en 9.2: quien desarrolla no aprueba su propio cambio y las pruebas de intrusión las ejecuta un tercero independiente. Si dos campañas requieren simultáneamente un mismo recurso crítico, el Jefe de Proyecto coordina la nivelación antes de fijar la fecha interna del gate y registra impacto, decisión y recuperación en el plan integrado; no declara capacidad disponible sin respaldo de T-15.

Los ambientes de Desarrollo, QA, Preproducción, Producción y Recuperación ante Desastres se mantienen identificados por inventario de componentes, topología, configuración, permisos y versión. Desarrollo usa datos sintéticos o anonimizados; QA utiliza conjuntos controlados y versionados; Producción y DR mantienen acceso restringido y auditado. Durante el solapamiento se registra por separado el propósito y ventana de uso de cada ambiente, los cambios autorizados y la versión de datos sintéticos o enmascarados, de manera que una prueba de E2 no modifique datos, configuración ni telemetría de operación de E1.

Cada candidato queda identificado por una versión inmutable del código y del artefacto desplegable, con dependencias, imágenes, configuración externalizada y resultados de pipeline asociados. La promoción a Preproducción y Producción reutiliza el mismo artefacto aprobado, sin recompilar; solo cambia la configuración declarada del ambiente. El expediente registra hash o identificador equivalente, versiones de componentes y herramientas que afecten la medición, parámetros y resultados. Las versiones concretas de herramientas, navegadores, motores y dependencias se fijan en la línea base de configuración aprobada para la campaña, no se presuponen en este plan. El control de configuración y la separación entre despliegue y liberación permiten observar E1 en producción y validar E2 sin exponer funciones no aceptadas; los calendarios de congelamiento de SD07 siguen rigiendo las ventanas operativas.

La evidencia de carga separa los perfiles presencial y digital y conserva cada perfil del Caso, su volumen, concurrencia y tasa de llegada definida para el ensayo. La concurrencia temporal no habilita a agregar cargas incompatibles ni a reducir umbrales: T-13 identificará campaña, ambiente, versión y recursos compartidos para interpretar cada resultado. Antes de un gate se adjunta la comparación entre perfil observado, perfil requerido y configuración usada; una desviación de ambiente o capacidad requiere registrar su impacto y repetir la prueba en condiciones válidas cuando el criterio no pueda demostrarse con la evidencia disponible.
```

### Ubicación 3: después de capacidad/configuración — cambio y no conformidad vinculados a gates

```latex
\subsection{9.3.3 Control de cambios, no conformidades y gates de aceptación}

Todo cambio de requisito aprobado, diseño, datos, interfaz, código, dependencia, configuración o ambiente que pueda alterar un criterio abre una evaluación de impacto antes de incorporarse. El solicitante vincula la petición o defecto con requisito, servicio, etapa y paquete EDT; el responsable técnico analiza los componentes y versiones afectados; QA determina casos, datos, criterios y evidencia que deben actualizarse o repetirse; Seguridad y los dueños de Retail o Emisor revisan los impactos de su dominio. El Jefe de Proyecto coordina la decisión por el procedimiento de control de cambios del SD06 y actualiza línea base, EDT, calendario y trazabilidad según corresponda. Una modificación aprobada no se considera verificada hasta que el candidato resultante completa las pruebas afectadas y la regresión definida. Si cambia el alcance o una condición de aceptación contractual, se aplica el procedimiento y la autoridad que establecen las Bases y el contrato; este plan no amplía unilateralmente esos compromisos.

QA registra como no conformidad todo criterio medido que no satisface su umbral, prueba bloqueada por una condición inválida, evidencia incompleta o defecto que impida demostrar cumplimiento. El registro contiene el criterio y requisito, EDT/hito relacionado, versión, ambiente, dato de prueba, resultado, severidad, impacto de dominio, responsable y acción correctiva. El dueño técnico corrige; QA revisa la causa y el alcance de regresión, repite el caso y confirma que la evidencia nueva corresponda al mismo candidato o a uno identificado como sucesor. Los dueños de Retail y Emisor validan las reglas y conciliaciones de su dominio. La no conformidad solo se cierra cuando el criterio vuelve a cumplir y QA registra la verificación. Si persiste, la puerta aplicable permanece cerrada y el defecto se escala por gobierno de SD06; no se marca conforme por decisión administrativa.

La secuencia de gates se lee junto con las ramas EDT y los hitos del Capítulo 7. El gate de integración y CI comprueba revisión, compilación, pruebas automáticas y políticas; habilita la entrega a QA, pero no constituye aceptación del CLIENTE. El gate de QA reúne la evidencia funcional y no funcional y deja las no conformidades identificadas. El gate de Preproducción verifica la campaña de etapa, seguridad independiente, migración y conciliación pertinente, carga, resiliencia y reversión con topología y versiones controladas. La certificación de la rama 1.9 prepara el expediente de la etapa. La marcha blanca de 1.12 aporta resultados reales supervisados y su cierre se sujeta a las condiciones del Artículo 17 ya expuestas en este capítulo. El gate contractual se completa con la revisión del entregable y el acta de la Contraparte Técnica conforme al Artículo 18; solo la evidencia y recepción conforme del hito definido en E-25 habilitan su tratamiento de pago.

Los criterios técnicos internos pueden exigir controles de promoción más estrictos para proteger datos y operación, pero no sustituyen el protocolo contractual ni añaden causas de multa, retención, recepción tácita, plazo de pago o aceptación provisional/definitiva. Una excepción técnica solo puede tramitarse dentro de las atribuciones previstas en el gobierno del proyecto y no dispensa umbrales obligatorios, hallazgos críticos o altos bloqueantes ni controles de separación Retail--Emisor. Las observaciones y subsanaciones siguen los plazos y consecuencias del Artículo 18; el Jefe de Proyecto programa la entrega del expediente para hacer viable esa revisión y registra la respuesta del adjudicatario.

La relación documental para cada hito se conserva como una cadena de consulta: requisito o criterio aprobado $\rightarrow$ prueba y resultado $\rightarrow$ evidencia del candidato y ambiente $\rightarrow$ paquete EDT $\rightarrow$ entregable/hito E-25 $\rightarrow$ acta de recepción conforme de la Contraparte Técnica. El expediente de QA permite recorrer esa cadena en ambos sentidos. La referencia al pago identifica el hito aplicable según E-25; no incorpora ponderaciones o montos al Plan de Calidad.
```

### Ubicación 4: al cierre de 9.3, antes de Referencias — ejecución hasta M56

```latex
\subsection{9.3.4 Continuidad del control durante la operación}

Desde el H12, Operación/SRE actualiza el expediente al promover cada versión y conserva telemetría, incidentes, cambios, defectos, regresiones y medidas correctivas vinculadas con los mismos criterios y servicios. QA verifica la integridad de la trazabilidad en las revisiones previstas; Seguridad y el tercero independiente entregan las evidencias de intrusión con la frecuencia comprometida, y Operación registra las pruebas semestrales de resiliencia y recuperación ante desastres. Un cambio operacional que afecte un control o umbral vuelve al análisis de impacto y a las pruebas correspondientes antes de su liberación. Los informes y evidencias se relacionan con los hitos mensuales de operación que fija E-25; la aceptación y el pago se rigen por ese instrumento y por el contrato durante los meses 21 a 56.
```

## Notas de integración y límites

- Mantener texto actual de SD09 sobre hitos M12/M18, marcha blanca y condiciones del Art. 17: la propuesta aporta relaciones EDT/evidencia y no las reemplaza.
- La tabla usa paquetes existentes del diccionario de trabajo (1.9.1–1.9.8, 1.9.6 y 1.9.7 se listan cuando procede) solo donde están publicados. La numeración de los subpaquetes 1.9.5 o cualquier otro no se debe inferir.
- El diccionario del contexto marca varios detalles, hitos y esfuerzos como pendientes/propuesta; la tabla refiere a ramas y contribuciones por etapa hasta conciliar T-14/T-15 con SD07. En particular, no asigna paquete a un hito E-25 si esa relación no está aprobada.
- Se usan únicamente las condiciones contractuales existentes: cronograma Art. 17; recepción, revisión y subsanación Art. 18; compromisos técnicos del Art. 24/Transversales; hitos y evidencia E-25. Sin porcentajes económicos, umbrales de pago adicionales, tiempos de pago, retenciones, multas nuevas ni reglas de recepción tomadas del material docente.
- La propuesta desarrolla el enfoque en el texto de 9.3. T-13, T-14, T-15 y T-17 conservan detalle operativo, planificación, recursos y protocolo de aceptación; su mención no deja la alineación requerida remitida únicamente a esos formularios.
