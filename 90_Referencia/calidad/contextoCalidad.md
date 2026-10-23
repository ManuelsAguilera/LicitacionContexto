# Contratos, Adquisiciones y Calidad — transcripción

**Fuente:** material de clases del Taller de Formulación y Evaluación de Proyectos (2026), PDF de 38 páginas.
**Procedencia:** archivo fuente entregado por el usuario; copia preservada en [`contextoCalidad.pdf`](contextoCalidad.pdf). SHA-256: `4c613e060757fea773ea32ea6f1a83d6ce6375bbdcbdc0aa83cf5d0e5e5d04c0`.
**Metadatos:** 38 páginas, carta, creado/modificado el 2026-09-24; productor Microsoft PowerPoint para Microsoft 365.

## Cobertura y método

Se transcriben las 38 páginas. Cada página conserva el folio impreso disponible y tiene un ancla `pagina-NN` basada en su número dentro del PDF. Se empleó PyMuPDF y pdfplumber; las tablas con celdas recuperables se representaron como tablas Markdown. Las demás listas y bloques se pasaron a encabezados, listas o párrafos según su función visual. Se cotejaron visualmente las páginas 1, 2, 3, 5, 14, 18, 26, 27, 35 y 37. Las láminas no contienen imágenes incrustadas: las tarjetas y el separador de la página 27 son elementos gráficos con texto, transcritos en su lugar.

La extracción de texto sin procesar se conserva en [`contextoCalidad_texto_original.txt`](contextoCalidad_texto_original.txt), incluidos los rótulos laterales repetidos. La navegación lateral común a las páginas de contenido es: **Adquisiciones · Contratos · Proceso · Economía · Calidad · Aseguramiento · Costo · Cruce · Propuesta**. Las tablas no detectadas como rejillas se transcriben como listas o bloques; los saltos de línea de celdas pueden variar respecto al diseño original.

El pie institucional repetido es: **Pontificia Universidad Católica de Valparaíso · Escuela de Ingeniería Informática · Taller de Formulación y Evaluación de Proyectos · 2026**. Se consigna aquí una vez para facilitar la lectura. Las afirmaciones y cifras de las láminas se preservan como material docente; sus precisiones y actualizaciones están separadas en [`investigacion_calidad.md`](investigacion_calidad.md).

## Mapa de conceptos y páginas

| Concepto | Páginas PDF | Folios impresos aproximados |
|---|---:|---:|
| Fundamentos: calidad, grado, proceso y producto; ISO 25010, McCall y requisitos verificables | 1–9 | 67–75 |
| Recomendaciones para profundizar, sección 5 | 10 | — |
| Planificación y aseguramiento: procesos, plan, niveles, herramientas y pruebas | 11–21 | 77–87 |
| Recomendaciones para profundizar, sección 6 | 22 | — |
| Costo de la calidad, costo óptimo, cambio, presupuesto y evidencia | 23–30 | 89–96 |
| Recomendaciones para profundizar, sección 7 | 31 | — |
| Calidad y contrato: aceptación, niveles de servicio, recepción y trazabilidad | 32–38 | 98–104 |

> Las páginas 11, 23 y 32 son separadores de sección. Los folios impresos comienzan en 67; `pagina-NN` siempre indica número PDF.

<a id="pagina-01"></a>

## Página PDF 01 — Por qué se dedica tiempo a esto

### Por qué se dedica tiempo a esto

*Folio impreso: 67*

La calidad nunca es un accidente: siempre es el resultado de un esfuerzo de la inteligencia. En un proyecto se dedica tiempo a gestionarla por tres razones concretas.

#### Prevenir

- Evitar que los errores y los defectos lleguen a existir.
- Es siempre más barato que detectarlos y muchísimo más barato que repararlos.

#### Ahorrar

- No rehacer trabajo ya hecho.
- El retrabajo consume tiempo y dinero que ningún contrato paga: sale del margen.

#### Conservar

- Tener un cliente satisfecho al final del proyecto.
- En un mercado de licitaciones, la referencia del cliente anterior es el activo comercial.

> Las tres razones son económicas. La calidad no se gestiona por convicción moral: se gestiona porque no gestionarla cuesta más.

<a id="pagina-02"></a>

## Página PDF 02 — Calidad no es grado

*Folio impreso: 68*

Ésta es la distinción que más confusión evita en toda la sección, y la que más veces se pregunta en un examen.

| Grado | Calidad |
|---|---|
| Es la categoría de prestaciones que tiene el producto. | Es el grado en que el producto cumple los requisitos preestablecidos. |
| Más funcionalidades, más potencia, más opciones. | Se mide contra lo que se prometió, no contra lo que existe en el mercado. |
| Es una decisión de diseño y de precio. | Es una obligación, no una elección. |
| Un grado bajo no es un problema si fue una decisión declarada. | Una calidad baja siempre es un problema. |

En un proyecto, la falta de grado no es un problema; la falta de calidad seguramente lo sea.

> La pregunta clásica: ¿qué tiene más calidad, una camioneta usada o un deportivo nuevo? Depende del requisito. Si el requisito es «no romperse en caminos pedregosos», gana la camioneta. Si es «superar los 200 km/h», gana el deportivo.

<a id="pagina-03"></a>

## Página PDF 03 — Las dos calidades de un proyecto TIC

*Folio impreso: 69*

La gestión de la calidad aborda tanto la calidad de la gestión del proyecto como la de sus entregables. Se aplica a todos los proyectos, pero las medidas y las técnicas son específicas del tipo de entregable que se produce.

|  | Calidad del proceso | Calidad del producto |
| --- | --- | --- |
| Qué asegura | Que la forma de trabajar sea eficiente y repetible | Que el resultado cumpla los estándares establecidos |
| Se evalúa con | Auditorías, revisiones de proceso, madurez | Pruebas, inspecciones, métricas del producto |
| Ejemplo | Toda historia pasa por revisión de código antes de integrarse | La página de consulta responde en menos de 2 segundos con 300 usuarios concurrentes |
| Quién responde | El jefe de proyecto y la organización | El equipo técnico y el responsable de calidad |
| Norma típica | ISO 9001, CMMI, ISO/IEC 20000-1 | ISO/IEC 25010, ISO/IEC/IEEE 29119 |
| Si falla | El producto puede salir bien, pero por casualidad y una sola vez | El producto sale mal aunque el proceso se haya seguido |

> Un buen proceso no garantiza un buen producto, pero un mal proceso garantiza que el buen producto no se repita en el proyecto siguiente.
<a id="pagina-04"></a>

## Página PDF 04 — Qué significa calidad cuando el producto es software

*Folio impreso: 70*

Existen muchas definiciones. La que usaremos en el curso es operativa y tiene tres partes, porque las tres se pueden verificar.

#### Concordancia explícita

- Cumple los requisitos funcionales y de rendimiento que fueron establecidos por escrito.
- Se verifica contra la especificación.

#### Concordancia documentada

- Cumple los estándares y procesos de desarrollo que la organización dejó documentados.
- Se verifica con auditorías y revisiones.

#### Características implícitas

- Cumple lo que se espera de todo software desarrollado profesionalmente aunque nadie lo haya escrito.
- Es la parte que produce las discusiones.

> La tercera parte es la peligrosa: nadie escribe «el sistema no debe perder datos», pero todos lo dan por supuesto. En una licitación, las expectativas implícitas del mandante son riesgo puro.

<a id="pagina-05"></a>

## Página PDF 05 — El modelo de calidad vigente: ISO/IEC 25010:2023

*Folio impreso: 71*

La versión 2023 reemplazó a la de 2011 y pasó de ocho a nueve características. Si su bibliografía habla de «usabilidad» y «portabilidad» como características de primer nivel, está desactualizada.

| Característica | Qué evalúa | Ejemplo de métrica verificable |
| --- | --- | --- |
| Adecuación funcional | Que haga lo que se pidió, completo y correcto | 100% de los casos de uso críticos aprobados |
| Eficiencia de desempeño | Tiempos, uso de recursos y capacidad | Bajo 2 s en el percentil 95 con 300 usuarios |
| Compatibilidad | Coexistencia e interoperabilidad con otros sistemas | Interopera con el servicio del mandante |
| Capacidad de interacción | Antes «usabilidad»: aprendizaje y prevención de errores | Un usuario nuevo completa el trámite en 5 minutos |
| Fiabilidad | Madurez, disponibilidad, tolerancia a fallos | Disponibilidad mensual de 99,5% en horario hábil |
| Seguridad | Confidencialidad, integridad, no repudio, resistencia | Sin hallazgos críticos en la prueba de intrusión |
| Mantenibilidad | Modularidad, reutilización y capacidad de prueba | Cobertura de pruebas unitarias sobre el 70% |
| Flexibilidad | Antes «portabilidad»: adaptabilidad y escalabilidad | Escala a 600 usuarios sin cambio de arquitectura |
| Seguridad de funcionamiento | Nueva: evitar daño a personas, bienes o entorno | Degrada de forma controlada ante falla de red |

ISO/IEC 25010:2023, publicada el 15 de noviembre de 2023, segunda edición.
<a id="pagina-06"></a>

## Página PDF 06 — El modelo histórico de McCall: por qué todavía se enseña

*Folio impreso: 72*

Es anterior a la norma ISO y sigue siendo útil porque cada factor está formulado como una pregunta que un usuario haría en voz alta.

| Factor | Qué mide | La pregunta que responde |
| --- | --- | --- |
| Corrección | Si satisface la especificación y cumple el objetivo del cliente | ¿Hace lo que quiero? |
| Fiabilidad | Si ejecuta sus funciones con la precisión requerida | ¿Lo hace de forma fiable todo el tiempo? |
| Eficiencia | Los recursos de cómputo y de código que necesita | ¿Correrá bien en mi hardware? |
| Integridad | Si el acceso al software y a los datos está controlado | ¿Es seguro? |
| Facilidad de uso | El esfuerzo de aprenderlo y de operarlo | ¿Está diseñado para ser usado? |
| Facilidad de mantenimiento | El esfuerzo de localizar y arreglar un error | ¿Se puede corregir con relativa facilidad? |
| Flexibilidad | El esfuerzo de modificar un programa en operación | ¿Se puede cambiar con relativa facilidad? |
| Facilidad de prueba | El esfuerzo de probar que hace lo que debe | ¿Se puede probar con relativa facilidad? |
| Portabilidad | El esfuerzo de llevarlo a otro entorno | ¿Podré usarlo en otra plataforma? |
| Reusabilidad | Si sus partes sirven en otras aplicaciones | ¿Podré reutilizar alguna parte? |
| Interoperación | El esfuerzo de acoplarlo a otro sistema | ¿Podrá interactuar con otros sistemas? |
<a id="pagina-07"></a>

## Página PDF 07 — Cómo se escribe un requisito de calidad

*Folio impreso: 73*

Un adjetivo no es un requisito. Un requisito de calidad tiene cinco partes y las cinco se pueden verificar.

| Parte | Qué aporta | En el ejemplo |
| --- | --- | --- |
| Atributo | Qué característica de calidad se compromete | Tiempo de respuesta de la consulta de estado del trámite |
| Métrica | Con qué se mide y en qué unidad | Segundos transcurridos entre la solicitud y la respuesta completa |
| Valor objetivo | El número comprometido, con su estadístico | Menor o igual a 2 segundos en el percentil 95 |
| Condición | Bajo qué carga, en qué ambiente y en qué horario | Con 300 usuarios concurrentes, en ambiente de producción, en horario hábil |
| Método de verificación | Con qué prueba y con qué instrumento se demuestra | Prueba de carga con herramienta acordada, informe firmado por ambas partes |

> Así no: «el sistema debe ser rápido y amigable». Así sí: las cinco filas de arriba, escritas en una sola frase, en el anexo técnico de la oferta.
<a id="pagina-08"></a>

## Página PDF 08 — Los principios que ordenan la gestión de calidad

*Folio impreso: 74*

- **Enfoque en el cliente.** La satisfacción del cliente es el criterio final. No es lo mismo que darle la razón: es entender qué necesita y comprometerlo por escrito.
- **Liderazgo.** Alguien tiene que alinear la visión de calidad en todos los niveles. Si la calidad no tiene dueño, es de nadie.
- **Compromiso de todos.** Cada miembro del equipo contribuye. La calidad no es un departamento que revisa al final.
- **Mejora continua.** El proceso se corrige a sí mismo con la evidencia que va produciendo, no una vez al año.
- **Decisiones basadas en datos.** Se decide con mediciones, no con impresiones. Ésta es la que más cuesta y la que más diferencia.

> Los cinco principios se pueden declarar en un párrafo de la propuesta. Sólo valen algo si después aparecen convertidos en actividades con horas asignadas en la EDT.

<a id="pagina-09"></a>

## Página PDF 09 — Las normas que se citan, y qué certifica cada una

*Folio impreso: 75*

| Norma | Qué certifica exactamente | Versión vigente |
| --- | --- | --- |
| ISO 9001 | El sistema de gestión de la calidad de una organización: procesos, no productos | 2015, con una nueva edición en proceso de publicación durante 2026 |
| ISO/IEC 20000-1 | El sistema de gestión de servicios de TI de la organización | 2018, con enmienda de 2024 |
| ISO/IEC 27001 | El sistema de gestión de seguridad de la información | 2022, con enmienda de 2024 |
| ISO/IEC 25010 | No se certifica: es el modelo de calidad del producto de software | 2023 |
| ISO/IEC/IEEE 29119 | No se certifica como sistema: define procesos, documentación y técnicas de pruebas | Por partes, entre 2021 y 2022 |
| CMMI | No es una certificación: es un modelo evaluado mediante appraisal, con nivel de madurez de 1 a 5 | V3.0, de 2023 |

> Error frecuente en propuestas: escribir «somos CMMI nivel 3» o «cumplimos ISO 25010». Lo primero requiere un appraisal vigente y verificable; lo segundo no existe como certificación.
<a id="pagina-10"></a>

## Página PDF 10 — Recomendaciones para profundizar — sección 5: Calidad

### Recomendaciones para profundizar

**Sección 5 · Calidad**

1. **Separar calidad de grado.** Revise su propuesta y marque qué compromisos son de grado y cuáles de calidad. Los de grado se pueden negociar; los de calidad, no.
2. **Actualizar el modelo.** Reemplace cualquier referencia a las ocho características de ISO 25010:2011 por las nueve de la edición 2023.
3. **Reescribir cinco requisitos.** Tome cinco requisitos no funcionales de sus bases y reescríbalos con las cinco partes: atributo, métrica, valor, condición y verificación.
4. **Listar lo implícito.** Escriba las cinco expectativas que el mandante no puso por escrito pero que va a dar por supuestas. Ésas son riesgo.
5. **Verificar lo que declara.** Si su empresa ficticia declara una norma o un nivel de madurez, prepare cómo lo acreditaría si se lo piden en la defensa.

<a id="pagina-11"></a>

## Página PDF 11 — SECCIÓN 6 — Cómo se planifica y se asegura

- Los tres procesos de calidad del PMBOK y qué produce cada uno.
- El plan de gestión de la calidad: qué se decide antes de escribir código.
- Los cinco niveles de gestión de la calidad, del más caro al más barato.
- Aseguramiento y control: la distinción que casi todos confunden.
- Las herramientas: causa raíz, Pareto, Ishikawa, muestreo y pruebas.

**ASEGURAMIENTO**

<a id="pagina-12"></a>

## Página PDF 12 — Los tres procesos de la gestión de la calidad

*Folio impreso: 78*

| Proceso | Qué se hace | Qué produce |
| --- | --- | --- |
| Planificar la gestión de la calidad | Identificar los requisitos y estándares aplicables al proyecto y a sus entregables, y documentar cómo se demostrará el cumplimiento | Plan de gestión de la calidad, métricas de calidad, lista de verificación |
| Gestionar la calidad | Convertir el plan en actividades ejecutables e incorporar las prácticas de calidad al trabajo diario. Es aseguramiento | Informes de calidad, documentos de prueba, solicitudes de cambio y de mejora |
| Controlar la calidad | Monitorear y registrar los resultados de las actividades para evaluar el desempeño y verificar los entregables | Mediciones de control, entregables verificados, información de desempeño |

> El primero es de planificación, el segundo de ejecución y el tercero de monitoreo y control. El error habitual es tener sólo el tercero: probar al final y llamarlo gestión de calidad.
<a id="pagina-13"></a>

## Página PDF 13 — Aseguramiento y control: la diferencia que importa

*Folio impreso: 79*

Aseguramiento · gestionar la calidad

Control · controlar la calidad

- Mira el proceso, no el producto

- Mira el producto, no el proceso

- Es preventivo: busca que el defecto no ocurra

- Es detectivo: busca los defectos que ya existen

- Se hace durante todo el proyecto

- Se hace sobre cada entregable

- Herramientas: auditorías, revisiones de proceso, análisis causa raíz

- Herramientas: pruebas, inspecciones, mediciones, muestreo

- Pregunta: ¿estamos trabajando de la forma correcta?

- Pregunta: ¿este entregable cumple lo comprometido?

> Los dos son necesarios y ninguno reemplaza al otro. Sólo controlar es caro; sólo asegurar es ingenuo.


<a id="pagina-14"></a>

## Página PDF 14 — Qué contiene el plan de gestión de la calidad

*Folio impreso: 80*

| Contenido | Qué define | Ejemplo escrito |
| --- | --- | --- |
| Estándares aplicables | Qué normas y guías rigen el trabajo | Guía de estilo de código, ISO/IEC 25010 como modelo de atributos |
| Objetivos de calidad | Qué se compromete y con qué valor | Densidad de defectos menor a 0,5 por punto de función en aceptación |
| Roles | Quién asegura, quién controla y quién acepta | El líder técnico asegura; el ingeniero de QA controla; el mandante acepta |
| Actividades | Qué se hará y en qué momento del ciclo | Revisión de código por pares, pruebas automatizadas, dos auditorías internas |
| Métricas | Qué se mide, cómo, con qué frecuencia y quién informa | Cobertura, defectos abiertos por severidad, cumplimiento de hitos |
| Criterios de aceptación | Cuándo un entregable se da por recibido | Cero defectos críticos, máximo tres mayores con plan de corrección |
| Herramientas | Con qué se registra y se rastrea | Gestor de incidencias, integración continua, informes semanales |

> Si el plan de calidad no dice quién acepta y con qué criterio, no es un plan: es una declaración de intenciones. Y las intenciones no se pueden auditar.
<a id="pagina-15"></a>

## Página PDF 15 — Los cinco niveles de gestión de la calidad

*Folio impreso: 81*

Están ordenados de peor a mejor, y también del más caro al más barato. La organización se ubica en uno de ellos, sepa o no que existen.

1 · El cliente encuentra los defectos El enfoque más caro: problemas de garantía, retiros, pérdida de reputación y costos de retrabajo.

2 · Se detectan antes de entregar Control de calidad sobre los entregables. Aparecen costos de evaluación y de fallas internas, pero no externas.

3 · Se corrige el proceso Aseguramiento: se examina y corrige el proceso en sí mismo y no sólo los defectos particulares.

4 · La calidad se incorpora al diseño La calidad entra en la planificación y en el diseño del proyecto y del producto, no después.

5 · Cultura de calidad Toda la organización está consciente y comprometida con la calidad de los procesos y de los productos.

> Subir de nivel cuesta dinero una vez. Quedarse en el primero cuesta dinero todos los meses, y además cuesta clientes.


<a id="pagina-16"></a>

## Página PDF 16 — El ejemplo que se ve en todos los proyectos

*Folio impreso: 82*

Dos decisiones que parecen de gestión del cronograma y en realidad son decisiones de calidad con consecuencias económicas.

Hacer trabajar horas extras al equipo para cumplir con el cliente

Apurar las inspecciones de calidad para cumplir el cronograma

- Disminuye las ganancias por el costo del sobretiempo

- Deja errores sin detectar que llegan al cliente

- Incrementa el nivel de riesgo general del proyecto

- Reduce las ganancias por el retrabajo posterior

- Provoca renuncias en un mercado donde reemplazar cuesta meses

- Incrementa los riesgos después de la implantación, cuando corregir es más caro

- Produce errores y retrabajo, que es lo que se quería evitar

- Destruye la evidencia con la que se defendería una controversia

> Las dos decisiones se toman por razones de plazo y se pagan en la línea de calidad. Es el mecanismo por el cual un problema de estimación se transforma en un problema de calidad.


<a id="pagina-17"></a>

## Página PDF 17 — Las herramientas de gestión de la calidad

*Folio impreso: 83*

| Herramienta | Para qué sirve | Cuándo se usa |
| --- | --- | --- |
| Lista de verificación | Revisar que se estén cumpliendo los requisitos de calidad acordados | En cada entrega y en cada revisión |
| Análisis de documentación | Revisar los reportes que produce el control de calidad y detectar lo que está fuera de control | Semanal, sobre los informes de prueba y de desempeño |
| Análisis del proceso | Examinar problemas potenciales, restricciones y actividades que no agregan valor | Al cierre de cada etapa, para identificar mejoras |
| Análisis causa raíz | Investigar las razones que causan las variaciones, riesgos o defectos, para resolver el problema y no el síntoma | Ante todo defecto grave o recurrente |
| Auditoría de calidad | Verificar de forma independiente que se sigan los estándares y los procesos comprometidos | Al menos dos veces durante el proyecto |

> El análisis causa raíz es el que más rendimiento produce: corrige la fuente en vez del síntoma, y por eso reduce la cantidad de defectos futuros en vez de sólo la de defectos actuales.
<a id="pagina-18"></a>

## Página PDF 18 — Las herramientas gráficas clásicas

*Folio impreso: 84*

Diagrama causa-efecto (Ishikawa)

Histograma

Diagrama de Pareto

- Identifica de forma esquemática las causas posibles de un problema

- Representa la distribución de frecuencias agrupadas en clases o categorías

- Ordena las causas de falla por frecuencia, de mayor a menor

- Permite detectar rápidamente los pocos factores que originan la mayoría de las fallas

- Sirve para estimular ideas y ordenar la discusión del equipo

- Muestra la forma de la variación: dónde se concentra y dónde hay cola

- Se organiza por categorías: personas, proceso, herramientas, datos, entorno

- Es la herramienta que decide dónde poner el esfuerzo de corrección

- Útil para tiempos de respuesta y para tiempos de resolución

> El orden de uso es siempre el mismo: Pareto para decidir qué problema atacar, Ishikawa para encontrar sus causas, y causa raíz para elegir cuál corregir.


<a id="pagina-19"></a>

## Página PDF 19 — Las pruebas: qué se prueba y en qué orden

*Folio impreso: 85*

| Tipo de prueba | Qué verifica | Quién la ejecuta y cuándo |
| --- | --- | --- |
| Unitaria | Que cada componente haga lo suyo de forma aislada | El desarrollador, de forma automatizada y continua |
| Integración | Que los componentes conversen entre sí y con los sistemas externos | El equipo técnico, al integrar cada incremento |
| Sistema | Que la solución completa cumpla los requisitos funcionales | El equipo de QA, antes de entregar |
| Rendimiento y carga | Que cumpla los tiempos y la concurrencia comprometidos | Especialista, sobre ambiente equivalente a producción |
| Seguridad | Que resista los ataques previsibles y proteja los datos | Tercero independiente, antes de la puesta en marcha |
| Regresión | Que lo que funcionaba siga funcionando después de cada cambio | Automatizada, en cada integración |
| Aceptación (UAT) | Que el usuario final confirme que resuelve su necesidad | El mandante, contra criterios acordados de antemano |

> La prueba de aceptación no se diseña al final: se diseña junto con el requisito. Si el criterio de aceptación se escribe recién cuando hay que aceptar, se negocia en vez de verificarse.
<a id="pagina-20"></a>

## Página PDF 20 — Muestreo de aceptación: cuando no se puede revisar todo

*Folio impreso: 86*

Consiste en inspeccionar una muestra extraída de un lote para aceptar o rechazar el lote completo. Ahorra costo de inspección a cambio de aceptar un riesgo estadístico.

Aceptación por atributos

Aceptación por variables

- Se toma una muestra aleatoria y cada elemento se califica como aceptado o defectuoso

- Se toma una muestra y a cada elemento se le mide una variable continua

- Si el porcentaje de defectos supera el límite preestablecido, se rechaza todo el lote

- Con la media y la desviación estándar de la muestra se compara contra los límites acordados

- Ejemplo TIC: registros migrados que se validan como correctos o incorrectos

- Ejemplo TIC: tiempo de respuesta medido sobre una muestra de transacciones

En proyectos de migración de datos, el muestreo de aceptación es casi siempre la única técnica viable: revisar el 100% de los registros no es económicamente posible.

> Los dos riesgos que hay que declarar: aprobar elementos defectuosos que no fueron revisados, y rechazar elementos correctos que estaban dentro de un lote rechazado.


<a id="pagina-21"></a>

## Página PDF 21 — La deuda técnica: la parte de la calidad que se paga con interés

*Folio impreso: 87*

Es el trabajo pendiente que se acumula cuando se elige la solución rápida en vez de la correcta. No es un defecto: es una decisión con costo diferido.

| Tipo | De dónde viene | Cómo se controla |
| --- | --- | --- |
| Deliberada y documentada | Se decide entregar antes y se registra qué quedó pendiente | Se agenda su pago en una iteración futura |
| Deliberada y no documentada | Se toma el atajo y no se anota en ninguna parte | No se controla: aparece cuando alguien más toca el código |
| Involuntaria | Se descubre después que había una forma mejor de hacerlo | Se registra al detectarla y se prioriza como cualquier otro trabajo |
| Por obsolescencia | El componente de terceros dejó de tener soporte | Se vigila el ciclo de vida de cada dependencia desde el inicio |

> El informe CISQ de 2022 estima la deuda técnica acumulada en Estados Unidos en US$ 1,52 billones. Es una estimación modelada por un consorcio de la industria y así hay que citarla, pero da el orden de magnitud.
<a id="pagina-22"></a>

## Página PDF 22 — Recomendaciones para profundizar — sección 6: Aseguramiento

### Recomendaciones para profundizar

**Sección 6 · Aseguramiento**

1. **Escribir el plan.** Redacte el plan de calidad de su caso con las siete filas de la lámina correspondiente. Sin ellas es una declaración de intenciones.
2. **Ubicarse en el nivel.** Determine en qué nivel de gestión de la calidad trabaja hoy su grupo y qué actividad concreta lo sube un escalón.
3. **Definir tres métricas.** Elija tres métricas de calidad, con instrumento, frecuencia y responsable. Tres bien definidas valen más que quince enunciadas.
4. **Diseñar la aceptación.** Escriba los criterios de aceptación de sus tres entregables principales antes de construirlos.
5. **Dimensionar el muestreo.** Si su caso incluye migración de datos, defina ahora el tamaño de muestra y el límite de defectos aceptable.

<a id="pagina-23"></a>

## Página PDF 23 — SECCIÓN 7 — Cuánto cuesta la calidad

- Las cuatro categorías del costo de la calidad y cómo se comportan entre sí.
- El costo óptimo: por qué invertir más deja de convenir en algún punto.
- El mismo proyecto con y sin prevención, con las cifras completas.
- La curva del costo del cambio: qué dice de verdad y qué se le atribuye sin fundamento.
- Qué línea del presupuesto de su oferta representa todo esto.

**COSTO DE LA CALIDAD**

<a id="pagina-24"></a>

## Página PDF 24 — Qué es el costo de la calidad

*Folio impreso: 90*

El costo de la calidad incluye todos los costos incurridos durante la vida del producto por invertir en prevenir la no conformidad, por evaluar la conformidad y por el incumplimiento de los requisitos. Estos últimos también se llaman costos por calidad deficiente.

| Categoría | Qué comprende | Ejemplos |
|---|---|---|
| Prevención | Evitar que la calidad deficiente llegue a existir | Estándares, capacitación, revisiones de diseño, automatización de pruebas, herramientas |
| Evaluación | Comprobar si lo producido cumple | Pruebas, inspecciones, auditorías, mediciones, revisión de entregables |
| Fallas internas | Las constata el equipo antes de entregar | Retrabajo, corrección de defectos, repetición de pruebas, reprocesos |
| Fallas externas | Las constata el cliente | Garantía, soporte no previsto, multas, pérdida de reputación, retiro del servicio |

> Las dos primeras son inversión voluntaria y ocurren temprano. Las dos últimas son consecuencia y ocurren tarde. La suma de las cuatro es lo que realmente costó la calidad del proyecto.

<a id="pagina-25"></a>

## Página PDF 25 — El costo óptimo de la calidad

*Folio impreso: 91*

Los modelos muestran que existe un costo óptimo: el punto donde invertir más en prevención y evaluación deja de ser beneficioso porque ya no evita costos por fallas equivalentes.

| Zona | Qué está pasando | Qué se ve en el proyecto |
| --- | --- | --- |
| Inversión insuficiente | Se ahorra en prevención y evaluación, y las fallas crecen más rápido que el ahorro | Retrabajo constante, entregas rechazadas, equipo apagando incendios |
| Zona óptima | El costo total de la calidad es mínimo: cada peso invertido evita al menos un peso de falla | Defectos detectados temprano, entregas aceptadas a la primera |
| Sobreinversión | Se agrega control que ya no encuentra defectos suficientes para justificarse | Procesos que nadie usa, documentación que nadie lee, ceremonias vacías |

> La zona óptima no es un número universal: depende del costo de la falla en ese negocio. Un sistema de recaudación tributaria y una aplicación interna de reservas de sala no se prueban con la misma intensidad.
<a id="pagina-26"></a>

## Página PDF 26 — El mismo proyecto, con y sin prevención

*Folio impreso: 92*

Dos proyectos con el mismo alcance y el mismo costo directo de $ 200 millones. El primero invierte en prevención; el segundo la recorta para llegar antes.

| Categoría | Proyecto A · previene | Proyecto B · recorta | Diferencia |
| --- | --- | --- | --- |
| Prevención | $ 10.000.000 | $ 2.000.000 | − 8.000.000 |
| Evaluación | $ 18.000.000 | $ 6.000.000 | − 12.000.000 |
| Fallas internas | $ 14.000.000 | $ 26.000.000 | + 12.000.000 |
| Fallas externas | $ 6.000.000 | $ 44.000.000 | + 38.000.000 |
| Costo total de la calidad | $ 48.000.000 · 24% | $ 78.000.000 · 39% | + 30.000.000 |

Cifras ilustrativas y coherentes. Las fallas externas del proyecto B se descomponen en retrabajo en producción, multas contractuales, soporte no presupuestado y horas de gerencia dedicadas a la crisis.

> El proyecto B ahorró $ 20 millones en prevención y evaluación, y pagó $ 50 millones adicionales en fallas. El saldo son $ 30 millones de margen que desaparecieron sin que cambiara una línea de alcance.
<a id="pagina-27"></a>

## Página PDF 27 — El problema de fondo

> **Nadie descubre que ahorró mal en calidad mientras está ahorrando.**
>
> **Se descubre siempre después de entregar.**

<a id="pagina-28"></a>

## Página PDF 28 — La curva del costo del cambio: qué dice y qué no

*Folio impreso: 94*

Es la cifra más citada de la ingeniería de software y también una de las peor entendidas. Vale la pena usarla, pero citándola por lo que realmente es.

| Etapa en que se detecta | Multiplicador de costo | Advertencia |
| --- | --- | --- |
| Requisitos | 1× | El rango proviene de Boehm, 1981, sobre proyectos grandes en cascada de los años setenta |
| Diseño | 3× a 8× | Son rangos, no un número fijo |
| Codificación | 5× a 20× | La evidencia base es de TRW, con corroboración de IBM, GTE y Bell Labs |
| Pruebas de desarrollo | 10× a 50× | El propio Boehm revisó el hallazgo en 2001 y encontró curvas mucho más planas en equipos ágiles |
| Pruebas de aceptación | 30× a 100× | La versión popular «1-10-100» es una heurística, no una medición |
| Operación | 50× a 200× | Lo citable es la dirección del efecto y el rango original, siempre con atribución |

> Cítela como rango y con fuente. Si en su propuesta escribe «está demostrado que corregir en producción cuesta 100 veces más», un evaluador informado le va a pedir el estudio, y ese estudio no existe con esa precisión.
<a id="pagina-29"></a>

## Página PDF 29 — Cuánto se invierte en la práctica

*Folio impreso: 95*

#### Regla de partida

Entre 15% y 25% del esfuerzo total del proyecto en actividades de prevención y evaluación. Es práctica de industria, no norma: úsela como punto de partida y ajústela con el riesgo del sistema.

#### Se ajusta hacia arriba

Sistemas con dinero, con datos personales, con vidas, con integraciones múltiples o con una ventana de operación crítica.

#### Se ajusta hacia abajo

Sistemas internos, de bajo volumen, sin integración y con usuarios tolerantes al error. Existen, pero son menos de los que uno cree.

#### Se declara siempre

El porcentaje elegido va escrito en la propuesta, con la razón. Un número justificado se defiende; un número heredado, no.

#### Se protege por contrato

Si el cronograma se comprime, lo primero que se recorta es la evaluación. Dejarlo comprometido por escrito es la forma de impedirlo.

> El error más caro no es invertir poco en calidad: es no saber cuánto se está invirtiendo. Si en su presupuesto no hay una línea identificable de calidad, el número real es cero.

<a id="pagina-30"></a>

## Página PDF 30 — El orden de magnitud del problema, con fuente

*Folio impreso: 96*

| Cifra | Qué representa | Fuente y salvedad indicadas en la lámina |
|---|---|---|
| US$ 2,41 billones | Costo estimado de la mala calidad del software en Estados Unidos en 2022 | Fuente: CISQ, informe de diciembre de 2022. Estimación modelada por un consorcio de la industria, patrocinada por un proveedor; se cita atribuyéndola. |
| US$ 1,52 billones | Deuda técnica acumulada dentro de esa cifra | Es el trabajo pendiente que alguien tendrá que pagar. |
| 19% | Tasa de fracaso de proyectos considerada en el informe CISQ de 2020 | El informe anterior, de 2020, estimaba US$ 2,08 billones totales: la tendencia es al alza. Coincide en orden de magnitud con otras fuentes, todas discutibles. |

Ninguna de estas cifras es una medición auditada: son modelos.

> La forma correcta de usarlas en una propuesta es como orden de magnitud y con la atribución escrita. La forma incorrecta es presentarlas como hechos verificados.

<a id="pagina-31"></a>

## Página PDF 31 — Recomendaciones para profundizar — sección 7: Costo de la calidad

### Recomendaciones para profundizar

**Sección 7 · Costo de la calidad**

1. **Poner la línea.** Cree en su presupuesto una línea explícita de calidad, separada de desarrollo, con horas y responsable.
2. **Calcular su COQ.** Estime las cuatro categorías para su propio caso. No busque precisión: busque el orden de magnitud y la coherencia.
3. **Justificar el porcentaje.** Escriba en tres líneas por qué su proyecto invierte el porcentaje que invierte, en función del riesgo del sistema.
4. **Revisar sus citas.** Busque en su propuesta toda cifra sin fuente. O le pone fuente, o la saca.
5. **Blindar la evaluación.** Identifique qué actividades de calidad se caerían si el cronograma se comprimiera, y protéjalas por contrato.

<a id="pagina-32"></a>

## Página PDF 32 — SECCIÓN 8 — Donde el contrato compra calidad

- Por qué las dos materias de esta clase son en realidad una sola.
- El criterio de aceptación como cláusula contractual y no como buena intención.
- Niveles de servicio, multas y descuentos: cuando la calidad tiene precio unitario.
- Recepción provisional, definitiva y período de garantía.
- La cadena que hay que poder recorrer: requisito, métrica, prueba, hito, pago.

**CRUCE**

<a id="pagina-33"></a>

## Página PDF 33 — Las dos materias son la misma conversación

*Folio impreso: 99*

El contrato es el instrumento con el que se compra calidad. Todo lo que no quedó escrito como obligación verificable es, en la práctica, calidad que nadie compró y que nadie está obligado a entregar.

| Concepto de calidad | Dónde vive en el contrato | Qué pasa si no está |
| --- | --- | --- |
| Requisito no funcional | Anexo técnico y especificaciones | Se discute al final, con el sistema ya construido |
| Criterio de aceptación | Cláusula de recepción de entregables | Acepta quien tenga más poder en la reunión |
| Métrica de servicio | Acuerdo de nivel de servicio | El servicio se evalúa por percepción |
| Consecuencia del incumplimiento | Cláusula de multas y descuentos | No hay consecuencia, o la hay desproporcionada |
| Respaldo del cumplimiento | Garantías y retenciones | El riesgo lo carga íntegramente el comprador |
| Corrección posterior | Período de garantía y soporte | Cada corrección se negocia como trabajo nuevo |

> Regla que resume la sección: una exigencia de calidad que no tiene una cláusula asociada no es una exigencia, es una expectativa.
<a id="pagina-34"></a>

## Página PDF 34 — El criterio de aceptación como cláusula

*Folio impreso: 100*

Un criterio de aceptación bien escrito responde cuatro preguntas y no deja ninguna a la interpretación.

#### ¿Qué se verifica?

El entregable concreto y su alcance exacto: no «el módulo de pagos», sino «el módulo de pagos con las tres pasarelas indicadas en el anexo 3».

#### ¿Con qué prueba?

El método, el ambiente, el conjunto de datos y la herramienta. Si el instrumento es del proveedor, el comprador debe tener acceso a él.

#### ¿Qué valor se exige?

El umbral numérico y su estadístico: cero defectos críticos, máximo tres mayores con plan de corrección comprometido.

#### ¿Qué pasa si no cumple?

El plazo de corrección, la consecuencia del incumplimiento reiterado y qué ocurre con el pago asociado a ese hito.

> El plazo de revisión del comprador también es un criterio: si las bases no dicen cuánto tiene el mandante para aceptar o rechazar, el proyecto puede quedarse detenido indefinidamente sin culpa del proveedor.

<a id="pagina-35"></a>

## Página PDF 35 — Multas y descuentos por nivel de servicio

*Folio impreso: 101*

Es el lugar donde una métrica de calidad se convierte en dinero. Hay que leerlo con calculadora, no con optimismo.

| Elemento | Qué hay que verificar | Riesgo si se ignora |
| --- | --- | --- |
| Base de cálculo | Si la multa se calcula sobre el hito, sobre el mes o sobre el contrato completo | Un atraso menor puede castigarse sobre el monto total |
| Unidad de tiempo | Si se cuenta por día corrido, día hábil u hora | Un fin de semana puede triplicar la multa |
| Tope acumulado | Cuál es el máximo que pueden sumar todas las multas | Sin tope, el contrato puede llegar a costar más que su precio |
| Causales eximentes | Qué atrasos no son imputables: demoras del mandante, fuerza mayor, terceros | Se paga por atrasos que no dependían de usted |
| Procedimiento | Notificación, plazo de descargos y resolución fundada | Multas aplicadas sin posibilidad real de defensa |
| Forma de cobro | Si se descuenta del estado de pago o se cobra la garantía | Impacto directo e inmediato sobre la caja |

> En Chile no existe un tope legal de multas expresado en porcentaje del contrato: el procedimiento y los montos se fijan en las bases de cada licitación, con derecho a descargos del proveedor. Los topes de 10% o 20% que circulan son práctica, no norma.
<a id="pagina-36"></a>

## Página PDF 36 — Recepción, garantía y el dinero retenido

*Folio impreso: 102*

| Momento | Qué significa | Qué se juega el proveedor |
| --- | --- | --- |
| Recepción provisional | El mandante acepta que el sistema entró en operación, con o sin observaciones | Se libera un porcentaje del pago; comienza a correr el plazo de observaciones |
| Período de marcha blanca | Operación real con soporte reforzado y corrección de observaciones | Es el período donde aparecen las fallas que las pruebas no encontraron |
| Recepción definitiva | Se declaran subsanadas las observaciones y cerrado el suministro | Se libera el saldo retenido y termina la exposición principal |
| Período de garantía | Plazo posterior en que el proveedor corrige defectos sin costo adicional | Consume horas no facturables que hay que haber presupuestado |
| Vigencia de la garantía de fiel cumplimiento | El instrumento sigue vigente después del término del contrato | Capital de trabajo inmovilizado más allá del cierre del proyecto |

Verifique siempre en las bases del caso el porcentaje, el plazo y los instrumentos admitidos: el nuevo reglamento acepta certificados de fianza y formatos electrónicos, no sólo boleta bancaria.

> La garantía de fiel cumplimiento en compras públicas chilenas se mantiene vigente hasta 60 días hábiles después del término del contrato, y sobre ella se pueden hacer efectivas las multas.
<a id="pagina-37"></a>

## Página PDF 37 — La cadena que el evaluador recorre

*Folio impreso: 103*

En una defensa, la pregunta que más descoloca es «¿dónde se ve eso?». La respuesta es una cadena de cinco eslabones que se puede recorrer en los dos sentidos.

| Eslabón | Documento donde vive | Ejemplo completo |
| --- | --- | --- |
| Requisito | Anexo técnico de la oferta | La consulta de estado responde en 2 s o menos, percentil 95, con 300 usuarios concurrentes |
| Métrica | Plan de gestión de la calidad | Tiempo de respuesta medido con la herramienta acordada sobre 10.000 transacciones |
| Prueba | Plan de pruebas | Prueba de carga en ambiente equivalente a producción, informe firmado por ambas partes |
| Hito | Carta Gantt y EDT | Hito 4: certificación de desempeño, semana 22 |
| Pago | Cláusula de estados de pago | 15% del precio se paga contra aprobación del hito 4 |

> Si usted puede recorrer esta cadena para sus tres requisitos más críticos, su propuesta está amarrada. Si se corta en algún eslabón, ahí es exactamente donde va a aparecer el conflicto.
<a id="pagina-38"></a>

## Página PDF 38 — Errores frecuentes en el amarre

*Folio impreso: 104*

#### Del lado del oferente

- Comprometer niveles de servicio que la arquitectura ofrecida no puede sostener.
- Aceptar criterios de aceptación redactados como opinión del mandante.
- No declarar exclusiones ni supuestos, y descubrirlos durante la ejecución.
- Presupuestar cero horas de garantía y de administración de contrato.
- No leer la fórmula de multas antes de fijar el precio.

#### Del lado del mandante

- Escribir requisitos de calidad con adjetivos y sin métrica.
- No fijar plazo para pronunciarse sobre los entregables.
- Exigir garantías desproporcionadas que expulsan a las empresas pequeñas.
- Fijar multas que superan el margen del contrato y vuelven irracional ejecutarlo.
- No definir quién arbitra una discrepancia técnica.

> Los errores de las dos columnas producen el mismo resultado: un proyecto que se ejecuta discutiendo. Y discutir no está presupuestado en ninguna de las dos partes.
