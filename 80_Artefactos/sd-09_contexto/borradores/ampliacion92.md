# Ampliación aplicada propuesta para 9.2

Documento de trabajo para incorporar selectivamente al capítulo 9.2 de `02_Propuesta/latex_final/sd-09/OSS-Subdocumento9.tex`. No modifica el canónico ni afirma ejecuciones, resultados, niveles de madurez o acuerdos todavía inexistentes. Los criterios y registros siguientes son diseño futuro; las cifras contractuales ya establecidas conservan su fuente. Retail y Emisor mantienen aceptación, datos, responsables y evidencia separados.

## Matriz criterio → ubicación → profundidad → brecha

| Criterio del Comunicado 10 / contexto de calidad | Dónde está hoy en el canónico | Profundidad actual | Brecha que cubre esta ampliación |
|---|---|---|---|
| Puertas de calidad | 9.2, párrafos de prevención y puertas; Figura 9.2; criterios de paso y reversión | Concreta: bloqueos CI, preproducción, expediente y acta | Precisar evidencia mínima por puerta y enlazarla con estado del defecto y responsable; no crear una puerta contractual adicional. |
| Revisión por pares | 9.2, se menciona obligatoriedad y auditoría por muestras | Parcial: el requisito existe; falta un checklist operativo compacto | Dar checklist y registro mínimo, conservando el resto del párrafo actual. |
| Análisis estático y dinámico | 9.1.4 describe indicadores y bloqueo; 9.2 enumera herramientas del pipeline y pruebas | Ya hay lista de controles y vínculo a CI; la distinción está implícita | Añadir solo la definición diferenciadora y el registro mínimo, sin repetir inventario de herramientas. |
| ISO/IEC/IEEE 29119: niveles, tipos, ambientes, datos y automatización | 9.2, párrafos sobre plan, ambientes, datos segregados y pruebas | Amplia y aplicada; no requiere otro inventario | Mantener el texto existente. La tabla propuesta abajo es una ficha resumida para localizar responsabilidades/frecuencia/evidencia/bloqueo si se desea convertir párrafos en subtítulos, no texto acumulativo. |
| Verificación frente a validación | 9.2 identifica QA, Contraparte y dueños de negocio; 9.1 describe métricas | Parcial: responsabilidades aparecen, pero la diferencia conceptual y sus objetos no se declara de forma directa | Distinguir comprobar artefactos contra especificación (V) de confirmar aptitud para el uso con actores del dominio (Val), conservando independencia. |
| Trazabilidad requisito–diseño–código–prueba–despliegue | 9.2, párrafos de trazabilidad y dos ejemplos diferenciados | Concreta: recorrido bidireccional y dominios separados | Añadir gestión de cambios huérfanos y ficha mínima del defecto que cierre el enlace evidencia–corrección–regresión. |
| Registro y tratamiento de defectos | 9.2 describe severidad, repetición del caso y regresión; 9.1 indica registro de incumplimientos | Parcial: el ciclo existe, pero no se especifican estados y datos mínimos de cierre | Formalizar ciclo de vida, severidad por impacto, no conformidad, responsable, evidencia y verificación de cierre. |
| Aceptación de tres entregables | 9.2 remite a T-13/T-17 y regula actas; 9.3 ubica actividades EDT | Los hitos de etapa están desarrollados; falta mostrar aplicación a tres objetos principales | Añadir criterios para plan/casos T-13, paquete de migración por dominio y versión candidata. No repetir aceptación contractual existente. |
| Muestreo de migración: límite, alcance y riesgo | 9.2 distingue muestreo estadístico de dirigido y exige dos ensayos; 9.1/9.2 exigen conciliación por dominio | Adecuada en principio: reconoce población, método y riesgos de aceptación/rechazo | Fijar una propuesta calculable n=299, c=0 para atributos ordinarios; excluir saldos y segregación que exigen censo/conciliación exhaustiva. |

## Bloques LaTeX propuestos

Los bloques son selectivos: incorporar los de revisión, V&V, aceptación y muestreo; no volver a copiar inventarios de niveles, ambientes, herramientas o gates ya desarrollados. Para hacer la sección localizable, se propone ordenar 9.2 en subtítulos 9.2.1 a 9.2.7; el texto actual de puertas/datos migratorios se reasigna bajo el subtítulo correspondiente y se evita repetirlo. Estos son encabezados editoriales propuestos, no nuevos compromisos contractuales.

### 9.2.1 Revisiones y análisis de cambio — adición breve

```latex
\subsubsection{Revisión por pares y análisis de cambio}

El autor adjuntará al cambio el requisito/defecto, alcance, riesgo, análisis y pruebas. Un revisor distinto del autor comprobará criterio aprobado, contratos e interfaces, separación Retail/Emisor, rutas negativas y ausencia de datos, secretos o dependencias no autorizados. En cambios de datos revisa también el dueño del dominio; Seguridad revisa controles de seguridad y Arquitectura cambios estructurales. La lista de comprobación registra: (i) criterio vinculado; (ii) impacto en componentes, interfaces, datos y permisos; (iii) rutas positivas, negativas y de recuperación; (iv) resultados de pruebas y análisis; (v) observaciones con severidad y disposición; y (vi) aprobación fechada e identidades autor/revisor. Ningún cambio se integra sin checklist completo y aprobación distinta del autor. El dueño de negocio valida sus reglas y la Contraparte acepta los hitos; una revisión técnica no suplanta estas decisiones.

El análisis estático inspecciona código, dependencias, configuración e infraestructura sin ejecutar el sistema; el dinámico observa el comportamiento con estímulos controlados. Cada resultado conservará herramienta/versión, alcance, exclusiones, regla, artefacto, salida y vínculo al cambio. Calidad audita checklist y evidencia en cada intervalo SD06 y antes de certificaciones. Un fallo de regla bloqueante de 9.1.4 o las Bases impide integrar/promover; una alerta no bloqueante requiere disposición y dueño antes de cerrar el cambio.
```

### 9.2.2 Organización de pruebas ISO/IEC/IEEE 29119 — conservar texto actual; ficha opcional de control

El párrafo existente que inicia “El plan de pruebas organiza niveles...” ya satisface el desarrollo narrativo. Si se desea una ficha operacional breve, insertar como otro bloque LaTeX:

```latex
\subsubsection{Niveles, tipos, ambientes y automatización de pruebas}

\textbf{Tabla 9.X: Control de niveles, ambientes y evidencia de prueba}

\begin{longtable}{p{0.13\linewidth}p{0.22\linewidth}p{0.2\linewidth}p{0.19\linewidth}p{0.17\linewidth}}
\toprule
Nivel/tipo & Ambiente y responsable & Datos / automatización & Frecuencia de diseño & Bloqueo y evidencia \\
\midrule
\endhead
Unidad/componente; funcional y estático & Desarrollo; autor ejecuta, par revisa y CI informa. & Sintéticos o anonimizados; automatizados por cambio. & Cada cambio. & Fallo de prueba o regla bloqueante impide integrar; log versionado. \\
Integración/contrato y regresión & QA aislado; QA responde por campaña. & Conjuntos controlados y restablecibles; automatizar interfaces repetibles. & Por integración y antes de promover. & Error en flujo o regresión impide promover; reporte por interfaz. \\
Sistema; carga, estrés, seguridad, accesibilidad y resiliencia aplicables & Preproducción equivalente; QA con Operaciones, Seguridad y tercero cuando corresponda. & Volumen representativo segregado; automatizar carga/regresión y conservar revisión experta. & Antes de certificación/salida y frecuencias contractuales durante operación. & Incumplimiento de umbral contractual bloquea certificación; reporte de campaña por versión. \\
Aceptación de usuario y contrato & Preproducción; dueño Retail o Emisor valida su dominio; Contraparte acepta hito. & Datos protegidos y escenarios aprobados; ejecución humana con asistencia automatizada. & Cada entregable/hito sujeto a aceptación. & Solo acta habilita aceptación contractual; casos, observaciones y acta. \\
Producción/DR; observabilidad y ejercicios autorizados & Entorno restringido; Operaciones/SRE ejecuta y QA revisa evidencia. & Datos operativos bajo control; telemetría/auditoría y automatización autorizada. & Monitoreo continuo y calendario contractual. & Evento fuera de criterio abre defecto/incidente y acción; trazas y bitácora. \\
\bottomrule
\end{longtable}
```

Completar en T-13 campaña y calendario exactos que ya estén fijados contractualmente; no presentar esta tabla como prueba de ejecución.

### 9.2.3 Datos de prueba — mantener separados Retail y Emisor

El párrafo actual de los conjuntos de prueba es sustantivo y debe conservarse bajo este subtítulo, sin repetirlo aquí. La decisión de aceptación seguirá siendo por dominio, incluidos sus datos y permisos.

```latex
\subsubsection{Datos de prueba por dominio}
```

### 9.2.4 Verificación y validación — aclaración conceptual

```latex
\subsubsection{Ambientes, datos y automatización}

Desarrollo contendrá datos sintéticos o anonimizados y permisos restringidos; QA usará conjuntos controlados, versionados y restablecibles; Preproducción reproducirá topología, versiones, configuración y volumen representativo de producción con diferencias declaradas; Producción y Recuperación ante Desastres conservarán acceso restringido y evidencia mediante telemetría, auditoría y ejercicios autorizados. Los datos de Retail y Emisor se clasificarán, custodiarán y reinicializarán por separado. No se copiarán datos productivos a ambientes de prueba salvo autorización, minimización y controles documentados. Cada campaña indicará qué porción se automatiza, por qué y qué revisión manual requiere; la automatización repetible se ejecutará en integración continua y antes de promover, mientras UAT, accesibilidad contextual y aceptación contractual conservan intervención humana.

\subsubsection{Verificación y validación}

La verificación comprueba que el artefacto satisface una especificación aprobada; la validación confirma con usuarios y dueño del dominio que resuelve el uso previsto. Retail valida sus flujos comerciales; el Emisor valida por separado sus procesos, autorizaciones y resultados financieros. QA organiza y revisa evidencia; el autor no aprueba su cambio; dueños de negocio validan reglas; la Contraparte acepta hitos conforme a las Bases. Ninguna de estas decisiones se sustituye entre sí.
```

### 9.2.5 Trazabilidad y tratamiento de defectos

```latex
\subsubsection{Trazabilidad y tratamiento de defectos}

La matriz ya descrita en 9.2 conserva enlaces bidireccionales entre requisito, diseño, componente/configuración, cambio, prueba, ejecución, evidencia, defecto y despliegue. Añadir un estado de enlace incompleto cuando falte cualquiera de esos elementos: impide cerrar la campaña afectada; un cambio de línea base identifica enlaces y regresiones que deben reevaluarse. Las vistas de Retail, Emisor y controles compartidos autorizados permanecen separadas.

El registro de defecto añadirá identificador, dominio, requisito, versión/ambiente, reproducción, esperado/observado, evidencia, impacto, severidad, responsable, estado, disposición, cambio correctivo y pruebas de confirmación/regresión. El ciclo será detectado → clasificado → asignado → corregido/dispuesto por autoridad habilitada → verificado por QA → cerrado; si falla al repetir, vuelve a asignación. La severidad considera operación, datos, seguridad, cumplimiento y usuarios. QA revisa defectos abiertos antes de cada certificación; los bloqueantes impiden certificar y toda excepción interna conserva su responsable/plazo, sin dispensar exigencias contractuales.
```

### 9.2.6 Aceptación aplicada a tres entregables — fichas en prosa

La aceptación de los tres objetos siguientes se resuelve dentro de SD09. El Líder QA verifica el plan y la versión candidata; el Líder de Datos prepara la migración; el dueño de Retail o Emisor aprueba su dominio; la Contraparte Técnica acepta los hitos mediante acta. QA revisa cada expediente antes de elevarlo. T-13 y T-17 registran casos, calendario y forma de recepción; los criterios de decisión quedan establecidos aquí y en las Bases. Las mediciones se informan después de ejecutar cada campaña.

```latex
\subsubsection{Aceptación del plan de pruebas y catálogo T-13}

QA verificará que todos los requisitos de la línea base aprobada para la etapa tengan método, resultado esperado, ambiente y evidencia previstos, y que cada caso identifique nivel, tipo, datos, automatización y responsable. Los requisitos y casos se revisarán por Retail y Emisor en vistas separadas. El Líder QA aprobará la integridad del plan tras resolver observaciones de revisión por pares; la Contraparte Técnica aceptará el entregable cuando corresponda a un hito. La evidencia será el plan versionado, la matriz de cobertura y el registro de observaciones resueltas. La cobertura del universo aprobado debe ser completa para cerrar el plan; una brecha no se contará como prueba aprobada.

\subsubsection{Aceptación del paquete de migración por dominio y ola}

Datos preparará el plan, perfilado, saneamiento, transformaciones, conciliación y retorno de cada ola. QA comprobará el expediente y los dueños de Retail y Emisor aprobarán por separado las reglas y resultados de su dominio. El criterio de aceptación requiere al menos dos ensayos completos en Preproducción conforme a RT-05.13, conciliación reproducible de recuentos y sumas de control, tratamiento documentado de cada diferencia y ejecución del retorno previsto. Ninguna diferencia inexplicada permite autorizar el corte. La evidencia incluye plan y bitácoras fechadas, versiones del proceso y los datos, conciliación, registro de defectos, decisión del dueño del dominio y resultado del retorno; la Contraparte Técnica acepta el hito mediante acta.

\subsubsection{Aceptación de versión candidata de etapa}

QA verificará regresión y campañas funcionales y no funcionales aplicables; Seguridad presentará la evaluación independiente prevista; Operaciones demostrará despliegue y reversión; cada dueño de negocio confirmará los resultados de su dominio. La versión candidata cumple cuando satisface los umbrales contractuales aplicables, no mantiene defectos que bloqueen la liberación conforme a las puertas definidas y presenta el expediente trazable por versión y ambiente. La Contraparte Técnica acepta la etapa mediante el acta exigida antes de producción. La evidencia comprende resultados de campaña, matriz y registro de defectos, informe independiente aplicable, despliegue/retorno y acta. Ninguna aprobación interna habilita por sí sola producción.

\\textbf{Fuente:} Diseño propuesto a partir de Bases Transversales RT-05.11--05.14, Bases Administrativas art. 18 y Formularios T-13/T-17. No representa resultados observados.
```

### 9.2.7 Muestreo de migración, alcance y regla conservadora

```latex
\subsubsection{Plan de muestreo de migración}

Para atributos de registros migrados no financieros que admitan muestreo se propone un plan interno de tamaño fijo n=299 y aceptación c=0: la probabilidad de observar cero defectos si la proporción real alcanza 1 % es $0{,}99^{299}\approx0{,}0495$, por lo que el plan detecta esa proporción con probabilidad aproximada de 95,05 %. Esta regla no es umbral contractual ni estimación de calidad de Ancoa; se declara para que la Contraparte evalúe una regla calculable antes de la campaña. Si el lote contiene 299 registros o menos, se inspecciona el censo. En lotes mayores se extraen 299 registros aleatorios mediante semilla reproducible. La aceptación estadística requiere cero defectos; cualquier defecto observado rechaza el lote, inicia análisis de causa y exige censo o repetición integral de la transformación afectada. Así se limita el riesgo de aceptación del consumidor ante una tasa de defectos de 1 % o superior; el riesgo de rechazo del productor se acepta conscientemente por c=0 y se informará en T-13.

La regla se limita a atributos de registros ordinarios no cubiertos por controles exhaustivos. No se muestrean saldos ni operaciones vivas del Emisor, totales de control críticos, autorización/consentimiento ni segregación: estos se concilian o prueban al 100 %. La tolerancia para diferencias financieras o de frontera es cero; cualquier discrepancia inexplicada detiene aceptación y corte. El muestreo dirigido busca anomalías raras/extremas, pero no estima prevalencia. Retail y Emisor conservan poblaciones, propietarios, reglas y decisiones separadas. Una diferencia financiera o de frontera detiene la aceptación de la ola. Toda corrección sistémica requiere repetir la transformación completa afectada.
```

## Puntos de integración

- La matriz es diagnóstica; los bloques LaTeX son candidatos para el canónico después de revisión editorial.
- Mantener las remisiones existentes a T-13, T-17 y T-18 para registrar ejecuciones, población y evidencia; aplicar n=299,c=0 solo a los atributos ordinarios para los que se diseñó.
- No convertir “al menos dos ensayos completos”, “1,5 veces el peak”, 70 %, 80 %, 5 %, 3 % ni los diez días hábiles de revisión/subsanación en resultados ya observados: son compromisos o umbrales cuya fuente y estado se conservan.
- Mantener por separado certificación técnica interna, validación de negocio por Retail y Emisor, y aceptación contractual por acta de la Contraparte.
