# FEP03 · Estimación de Software

> Transcripción a Markdown de la presentación original (75 diapositivas). Los diagramas se representan con su texto; los elementos puramente gráficos no se incluyen.

## Índice de secciones

- [SECCIÓN 1 · Medir el tamaño del software](#diapositiva-2) — diapositiva 2
- [SECCIÓN 2 · Estimación por Punto Función](#diapositiva-12) — diapositiva 12
- [SECCIÓN 3 · Punto de Casos de Uso](#diapositiva-21) — diapositiva 21
- [SECCIÓN 4 · Factores técnicos y de ambiente](#diapositiva-35) — diapositiva 35
- [SECCIÓN 5 · Del tamaño al esfuerzo](#diapositiva-47) — diapositiva 47
- [SECCIÓN 6 · Ejemplo completo, paso a paso](#diapositiva-57) — diapositiva 57
- [SECCIÓN 7 · Aclaraciones y glosario](#diapositiva-71) — diapositiva 71

---

<a id="diapositiva-1"></a>

## Diapositiva 1 · Portada

Pontificia Universidad Católica de Valparaíso Escuela de Informática

**Formulación de Proyectos Informáticos**

**ICI-5542**

**2026**

**Antonio Moya Villegas**

antonio.moya@pucv.cl

v4.1.0 - 2026

---

<a id="diapositiva-2"></a>

## Diapositiva 2 · ▶ SECCIÓN 1 · Medir el tamaño del software

**MEDIR**

**01**

SECCIÓN 1

**Medir el tamaño del software**

- Por qué hay que medir antes de estimar, y qué se mide exactamente
- Tamaño, esfuerzo, plazo y costo: cuatro cosas distintas y encadenadas
- La idea común a todas las métricas funcionales
- Qué métodos existen y cuándo sirve cada uno
- En qué momento de una licitación se estima, y con qué información

---

<a id="diapositiva-3"></a>

## Diapositiva 3 · El problema: cotizar algo que no se puede pesar

Toda industria que vende construcción tiene una unidad de medida acordada. El software no la tuvo durante sus primeras dos décadas, y todavía discute cuál es.

| Producto | Unidad de medida | Qué permite hacer |
|---|---|---|
| Una casa | Metros cuadrados construidos | Cotizar, comparar constructoras, estimar plazo |
| Una carretera | Kilómetros y metros cúbicos | Licitar por unidad y controlar avance |
| Un contenedor | TEU y toneladas | Tarificar y planificar capacidad |
| Un software | ¿…? | Es lo que esta clase viene a resolver |

La primera respuesta histórica fue la línea de código. Funciona para comparar dos programas del mismo lenguaje y del mismo equipo, y falla en todo lo demás: depende del lenguaje, del estilo, del programador y de decisiones de diseño que nada tienen que ver con el valor entregado.

> ⚠️ Lo que hay que medir no es cuánto código se escribe: es cuánta funcionalidad recibe el usuario. Esa idea, y no la fórmula, es lo que separa a las métricas funcionales de las métricas de producto.

Una misma funcionalidad puede costar 200 o 2.000 líneas según el lenguaje. El usuario recibe exactamente lo mismo y paga lo mismo.

---

<a id="diapositiva-4"></a>

## Diapositiva 4 · Para qué sirve medir el tamaño

**Estimar esfuerzo**

Convertir tamaño en horas-hombre con un factor de conversión conocido, y de ahí a plazo y a precio.

**Medir productividad**

Horas por unidad de tamaño. Es la única forma de saber si el equipo mejora o empeora entre proyectos.

**Medir calidad**

Defectos por unidad de tamaño. Sin denominador, el número de defectos no dice nada.

**Comparar ofertas**

El mandante puede comparar dos propuestas de tamaño distinto sobre una misma base.

**Defender un precio**

Permite responder «¿por qué cuesta esto?» con un cálculo y no con una afirmación.

En un proyecto interno la medición sirve sobre todo para mejorar el proceso. En una licitación con precio fijo sirve para algo más inmediato: es la diferencia entre un precio calculado y un precio inventado.

> ⚠️ Sin una medida del tamaño no hay productividad, no hay calidad comparable y no hay estimación defendible. Hay opinión de experto, que a veces acierta y nunca se puede auditar.

El objetivo no es que la estimación sea exacta: es que sea explicable, repetible y mejorable con la experiencia de cada proyecto.

---

<a id="diapositiva-5"></a>

## Diapositiva 5 · Tamaño, esfuerzo, plazo y costo: la cadena completa

Los cuatro conceptos se encadenan, pero no son intercambiables. Cada paso de la cadena introduce supuestos propios que hay que declarar.

| Concepto | Qué mide | Unidad | De qué depende |
|---|---|---|---|
| Tamaño funcional | Cuánta funcionalidad se entrega | PF o UCP | Sólo de los requisitos |
| Esfuerzo | Cuánto trabajo cuesta construirlo | Horas-hombre | Del tamaño y la productividad |
| Plazo | Cuánto tiempo calendario toma | Semanas o meses | Del esfuerzo y la dotación |
| Costo | Cuánto dinero cuesta | Pesos | Del esfuerzo, tarifas e insumos |

Dos consecuencias prácticas. La primera: el tamaño no cambia si cambia el equipo, pero el esfuerzo sí. La segunda: duplicar la dotación no reduce el plazo a la mitad, porque el esfuerzo no se reparte de forma lineal.

> ⚠️ El error más frecuente en una oferta es saltarse un eslabón: pasar de los requisitos al precio sin haber calculado tamaño ni esfuerzo. Ese salto es el que después no se puede defender ante el evaluador.

En este curso los cuatro eslabones aparecen en documentos distintos: el tamaño en el anexo de estimación, el esfuerzo en la EDT, el plazo en el cronograma y el costo en la oferta económica.

---

<a id="diapositiva-6"></a>

## Diapositiva 6 · La idea común a todas las métricas funcionales

Todas las métricas funcionales hacen lo mismo: convierten requisitos en un número. Cambia la unidad, no el procedimiento.

**1**

**2**

**Identificar**

**Clasificar**

Listar lo que se va a construir, en la unidad que la métrica reconoce.

Asignar a cada elemento un grado de dificultad discreto.

**3**

**4**

**Ponderar**

**Sumar**

Cada grado tiene un peso numérico validado empíricamente.

El total de pesos es el tamaño sin ajustar del sistema.

**5**

**Ajustar y convertir**

Factores de ajuste y un factor de conversión a horas.

Los pesos y los factores no se inventan: provienen de la observación de cientos de proyectos reales y están publicados. Lo que sí decide el equipo es la clasificación de cada elemento, y ahí es donde se gana o se pierde la calidad de la estimación.

> ⚠️ El paso 2 es el único subjetivo, y por eso hay que dejar escrito el criterio con que se clasificó cada elemento. Sin ese criterio, dos personas del mismo equipo obtienen tamaños distintos para el mismo sistema.

---

<a id="diapositiva-7"></a>

## Diapositiva 7 · Qué métodos de estimación existen y cuándo sirve cada uno

| Método | En qué se basa | Cuándo conviene | Precisión típica |
|---|---|---|---|
| Juicio de expertos | Experiencia de quien estima | Muy temprano, o para validar otro | Muy variable |
| Analogía | Un proyecto anterior parecido | Cuando hay histórico comparable | Media |
| Descomposición y EDT | Sumar el esfuerzo de cada paquete | Cuando el alcance está detallado | Buena si la EDT es completa |
| Punto Función | Funcionalidad vista por el usuario | Con requisitos definidos | Buena |
| Punto de Casos de Uso | Actores y casos de uso del modelo | Si hay modelo de casos de uso | Buena |
| Modelos paramétricos | Ecuaciones calibradas con histórico | Con base de datos de proyectos | Buena si hay calibración |
| Tres valores y simulación | Rango optimista, probable, pesimista | Siempre, sobre los anteriores | Da rango, no punto |

> ⚠️ Regla de oficio: nunca se estima con un solo método. Se estima con dos independientes y se explica la diferencia. La diferencia entre ambos es la primera medida honesta de la incertidumbre del proyecto.

Esta clase cubre los dos métodos funcionales de la lista: Punto Función, como fundamento, y Punto de Casos de Uso, que es el que van a aplicar en su propuesta.

---

<a id="diapositiva-8"></a>

## Diapositiva 8 · En qué momento de una licitación se estima

En una licitación el precio se fija con la peor información del proyecto. La métrica funcional existe precisamente para poder estimar en ese momento.

| Momento | Qué información hay | Qué método aplica |
|---|---|---|
| Al leer las bases | Requisitos redactados por el mandante, sin detalle | Analogía y juicio de expertos |
| Al modelar el problema | Actores y casos de uso identificados | Punto de Casos de Uso |
| Al definir el alcance | Funciones, archivos y transacciones estimadas | Punto Función, Punto de Casos de Uso |
| Al construir la EDT | Paquetes de trabajo y responsables | Descomposición ascendente |
| Al cerrar la oferta | Todo lo anterior, comparado | Triangulación y rango declarado |
| Durante la ejecución | Avance real y productividad observada | Recalibración con datos propios |

> ⚠️ La secuencia importa: primero el modelo de casos de uso, después el tamaño, después el esfuerzo, después la EDT, y sólo al final el precio. Hacerlo al revés produce una EDT que se ajusta al precio que alguien ya prometió.

En el curso, esta clase se dicta después de Requisitos y EDT precisamente para poder comparar los dos caminos sobre el mismo caso.

---

<a id="diapositiva-9"></a>

## Diapositiva 9 · Qué queda dentro de la estimación funcional y qué queda fuera

**Lo que la métrica sí cubre**

- Análisis y especificación de la funcionalidad
- Diseño de la solución
- Construcción del software
- Pruebas de la funcionalidad construida
- Gestión y sobrecarga asociada al desarrollo
- Documentación técnica del producto

**Lo que hay que sumar aparte**

- Migración de datos históricos y su saneamiento
- Infraestructura, licencias de terceros y ambientes
- Capacitación y gestión del cambio
- Puesta en producción, marcha blanca y soporte inicial
- Operación y niveles de servicio del contrato
- Garantías, seguros y costos financieros

En el caso del curso, esa segunda columna pesa tanto como la primera: sobre un contrato de 10 meses de proyecto y 24 meses de operación, el servicio posterior es una parte mayor del precio que la construcción.

> ⚠️ Una oferta que confunde el esfuerzo de desarrollo con el costo del contrato deja fuera la mitad del precio. Es el error que más veces convierte un contrato ganado en una pérdida.

---

<a id="diapositiva-10"></a>

## Diapositiva 10 · Lo que esta clase va a producir

| Sección | Qué se construye | Resultado |
|---|---|---|
| 2 · Punto Función | Categorías, complejidad, puntos sin ajustar y factor de ajuste | Tamaño en puntos función |
| 3 · Punto de Casos de Uso | Peso de actores y de casos de uso | Puntos de casos de uso sin ajustar |
| 4 · Factores | Trece factores técnicos y ocho de ambiente | Los coeficientes TCF y EF |
| 5 · Esfuerzo | Puntos ajustados, factor de conversión y reparto | Horas-hombre por etapa |
| 6 · Ejemplo | El caso completo, paso a paso, con todas las tablas llenas | La plantilla que van a reutilizar |
| 7 · Aclaraciones | Tres distinciones de fondo y el glosario del método | El vocabulario del anexo |

> ⚠️ Al terminar deben poder tomar su propio modelo de casos de uso, aplicar el método completo y llegar a un número de horas por etapa que puedan justificar tabla por tabla.

Las secciones 2 a 5 son el método. La 6 es el ejemplo completo, con el caso del curso y todos sus números. La 7 cierra con el vocabulario y las distinciones que hay que tener claras.

---

<a id="diapositiva-11"></a>

## Diapositiva 11 · Recomendaciones para profundizar · Sección 1 · Medir el tamaño del software

RECOMENDACIONES PARA PROFUNDIZAR

**Sección 1 · Medir el tamaño del software**

**1**

**Buscar su histórico**

Si su empresa ficticia declara experiencia previa, defina cuántas horas por unidad de tamaño rindió en esos proyectos. Ese número es su factor de conversión propio.

**2**

**Separar los cuatro**

Revise su propuesta y verifique que tamaño, esfuerzo, plazo y costo aparecen como cifras distintas y encadenadas, y no como una sola.

**3**

**Listar lo que va aparte**

Escriba qué partes de su contrato no cubre la métrica funcional: migración, infraestructura, capacitación, operación. Ésa es la mitad que se olvida.

**4**

**Leer el manual IFPUG**

Revise el manual de prácticas de conteo de puntos función. No hace falta leerlo entero: los capítulos de definiciones bastan para no equivocarse en la clasificación.

**5**

**Elegir dos métodos**

Decida hoy con qué dos métodos independientes va a estimar su caso. Comparar es obligatorio en la propuesta.

---

<a id="diapositiva-12"></a>

## Diapositiva 12 · ▶ SECCIÓN 2 · Estimación por Punto Función

**P. FUNCIÓN**

**02**

SECCIÓN 2

**Estimación por Punto Función**

- De dónde viene el método y qué mide exactamente
- La fórmula de Albrecht y sus dos fases
- La frontera del conteo: funciones de datos y de transacción
- Las cinco categorías y los pesos por complejidad
- Los catorce factores de ajuste y el factor de complejidad técnica

---

<a id="diapositiva-13"></a>

## Diapositiva 13 · Qué es el Punto Función y qué mide

El método fue propuesto por Allan Albrecht en IBM a fines de los años setenta y hoy lo mantiene el IFPUG con un manual de prácticas de conteo. Es la métrica funcional más usada y la única con norma internacional.

**Qué mide**

El tamaño de la funcionalidad que el producto entrega al usuario: qué entra, qué sale, qué se consulta y qué se almacena.

**De qué es independiente**

Del lenguaje, de la tecnología, del equipo y del método de desarrollo. Dos soluciones distintas al mismo problema miden lo mismo.

**Cuándo se puede calcular**

Apenas existe la definición de requisitos. No hace falta diseño ni código, y por eso sirve para cotizar.

**Quién lo puede calcular**

No requiere perfil técnico: lo puede contar un analista funcional, e incluso el propio cliente si conoce el método.

> ⚠️ El punto función mide lo que el usuario recibe, no lo que el equipo escribe. Ésa es la propiedad que lo hace utilizable en una licitación: el mandante puede comparar dos ofertas sobre la misma base.

Hoy se usa sobre todo como variable de entrada de un modelo de estimación de esfuerzo, y no como estimación en sí misma.

---

<a id="diapositiva-14"></a>

## Diapositiva 14 · La fórmula de Albrecht y sus dos fases

**FP = UFP × TCF**

| Símbolo | Nombre | Qué es |
|---|---|---|
| FP | Puntos función ajustados | El tamaño funcional final del sistema |
| UFP | Puntos función sin ajustar | Suma de la funcionalidad clasificada y ponderada |
| TCF | Factor de complejidad técnica | Ajuste entre 0,65 y 1,35 según catorce características |

**Fase 1 · Contar**

- Identificar las funciones de usuario
- Clasificarlas en una de cinco categorías
- Asignar a cada una complejidad baja, media o alta
- Multiplicar por el peso y sumar: se obtiene UFP

**Fase 2 · Ajustar**

- Evaluar catorce características generales del sistema
- Puntuar cada una de 0 a 5 según su influencia
- Sumar los catorce valores
- Calcular TCF y multiplicar: se obtiene FP

---

<a id="diapositiva-15"></a>

## Diapositiva 15 · El modelo de conteo: la frontera, los datos y las transacciones

El conteo se organiza alrededor de una frontera. Dentro está la aplicación que se va a construir; fuera están sus usuarios y los otros sistemas. Se cuentan dos cosas que cruzan o residen en esa frontera: datos y transacciones.

**Funciones de datos · qué se almacena**

- ILF · Archivos lógicos internos: grupos de datos que la aplicación mantiene dentro de su frontera
- EIF · Archivos de interfaz externos: grupos de datos que la aplicación sólo consulta y que otro sistema mantiene
- Se cuentan por grupo lógico identificable por el usuario, no por tabla de base de datos

**Funciones de transacción · qué se hace**

- EI · Entradas externas: datos que entran y modifican un archivo interno o el comportamiento del sistema
- EO · Salidas externas: datos que salen e incluyen cálculo, derivación o actualización
- EQ · Consultas externas: datos que salen sin cálculo ni actualización, tal como están almacenados

> ⚠️ La distinción entre salida y consulta es la que más errores produce: si el dato que sale fue calculado o derivado, es una salida; si sale tal como está guardado, es una consulta.

Un grupo lógico de datos puede corresponder a varias tablas físicas. El conteo es funcional, no físico.

---

<a id="diapositiva-16"></a>

## Diapositiva 16 · Las cinco categorías, con su definición

| Categoría | Sigla | Definición | Ejemplo típico |
|---|---|---|---|
| Entrada externa | EI | Proceso elemental en que datos cruzan la frontera desde afuera hacia adentro y mantienen un archivo interno o controlan el sistema | Enviar una solicitud de trámite |
| Salida externa | EO | Proceso elemental que envía datos hacia afuera incluyendo datos derivados o calculados, y que puede actualizar un archivo interno | Emitir el certificado con el número de folio calculado |
| Consulta externa | EQ | Proceso elemental que recupera datos y los envía hacia afuera sin cálculo ni actualización | Consultar el estado de un trámite |
| Archivo lógico interno | ILF | Grupo de datos identificable por el usuario, mantenido dentro de la frontera de la aplicación | La solicitud de trámite y su historial |
| Archivo de interfaz externo | EIF | Grupo de datos identificable por el usuario, mantenido por otra aplicación y sólo referenciado | El padrón de contribuyentes del sistema contable |

> ⚠️ Regla práctica para clasificar: si la función mantiene datos, es EI. Si los muestra con cálculo o derivación, es EO. Si los muestra tal como están guardados, es EQ. Las tres se distinguen por el propósito, no por la pantalla.

Las dos categorías de datos, ILF y EIF, se distinguen por quién mantiene el grupo lógico: si lo mantiene la aplicación que se cuenta, es ILF; si lo mantiene otra, es EIF.

---

<a id="diapositiva-17"></a>

## Diapositiva 17 · Los pesos por categoría y complejidad

Cada combinación de categoría y complejidad tiene un peso fijo. La suma de todos los pesos es el total de puntos función sin ajustar.

| Categoría | Baja | Media | Alta |
|---|---|---|---|
| Entradas externas (EI) | 3 | 4 | 6 |
| Salidas externas (EO) | 4 | 5 | 7 |
| Consultas externas (EQ) | 3 | 4 | 6 |
| Archivos lógicos internos (ILF) | 7 | 10 | 15 |
| Archivos de interfaz externos (EIF) | 5 | 7 | 10 |

Obsérvese la escala: un archivo lógico interno de complejidad alta pesa cinco veces más que una consulta simple. El método afirma que mantener datos cuesta bastante más que mostrarlos, y eso es coherente con la experiencia.

> ⚠️ UFP se calcula multiplicando la cantidad de elementos de cada casilla por su peso y sumando las quince casillas. Es una sola tabla y una sola suma.

Estos pesos provienen del manual de prácticas de conteo del IFPUG y son los mismos en todas las versiones del método.

---

<a id="diapositiva-18"></a>

## Diapositiva 18 · Las catorce características generales del sistema

El ajuste considera catorce características generales que describen el entorno técnico y operacional del sistema. Cada una se puntúa de 0 a 5.

**Características 1 a 7**

- F1 · Comunicación de datos
- F2 · Procesamiento distribuido de datos
- F3 · Rendimiento
- F4 · Configuración fuertemente utilizada
- F5 · Frecuencia de transacciones
- F6 · Entrada de datos en línea
- F7 · Eficiencia del usuario final

**Características 8 a 14**

- F8 · Actualización en línea
- F9 · Procesamiento complejo
- F10 · Reusabilidad
- F11 · Facilidad de instalación
- F12 · Facilidad de operación
- F13 · Instalación en distintos lugares
- F14 · Facilidad de cambio

| Valor | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Influencia | Ninguna | Incidental | Moderada | Media | Significativa | Fuerte |

La suma de las catorce puntuaciones va de 0 a 70 y se conoce como grado de influencia total.

---

<a id="diapositiva-19"></a>

## Diapositiva 19 · El factor de complejidad técnica y su rango

**TCF = 0,65 + 0,01 × Σ Fi**

| Suma de los catorce factores | TCF resultante | Interpretación |
|---|---|---|
| 0 · ninguna característica influye | 0,65 | Sistema muy sencillo: el tamaño baja 35% |
| 35 · influencia media en todo | 1,00 | Sistema típico: el ajuste no modifica el tamaño |
| 42 · algo por sobre la media | 1,07 | Algo por sobre lo típico: el tamaño sube 7% |
| 70 · influencia fuerte en todo | 1,35 | Sistema muy exigente: el tamaño sube 35% |

> ⚠️ El ajuste técnico no puede salvar un conteo funcional mal hecho. Si el UFP está mal, el TCF sólo lo mueve un tercio en el mejor de los casos. Por eso el esfuerzo del equipo debe ir a contar bien, no a discutir los factores.

Algunas versiones más recientes del método prescinden del ajuste y trabajan sólo con puntos función sin ajustar. Si su propuesta lo hace, declárelo.

---

<a id="diapositiva-20"></a>

## Diapositiva 20 · Recomendaciones para profundizar · Sección 2 · Estimación por Punto Función

RECOMENDACIONES PARA PROFUNDIZAR

**Sección 2 · Estimación por Punto Función**

**1**

**Contar su sistema**

Tome su propio caso y liste los archivos lógicos internos y de interfaz externa. Suelen ser entre seis y quince, y son los que más pesan en el resultado.

**2**

**Declarar el criterio**

Escriba en dos líneas el criterio con que va a clasificar la complejidad. Sin él, dos integrantes del equipo obtendrán tamaños distintos.

**3**

**Puntuar los catorce**

Asigne los catorce factores de su sistema y justifique en una línea los que valgan 0 o 5. Son los que el evaluador va a preguntar.

**4**

**Distinguir EO de EQ**

Recorra sus salidas y separe las que traen un dato calculado o derivado de las que muestran el dato tal como está guardado. Es el error de clasificación más frecuente.

**5**

**Leer el manual**

Revise el manual de prácticas de conteo del IFPUG, en particular las matrices de complejidad por categoría. Son cinco tablas y se leen en veinte minutos.

---

<a id="diapositiva-21"></a>

## Diapositiva 21 · ▶ SECCIÓN 3 · Punto de Casos de Uso

**P. CASO USO**

**03**

SECCIÓN 3

**Punto de Casos de Uso**

- De dónde viene el método y qué necesita para funcionar
- La cadena completa: de los actores al esfuerzo por etapa
- Factor de peso de los actores sin ajustar (UAW)
- Qué es una transacción y cómo se cuentan bien
- Factor de peso de los casos de uso sin ajustar (UUCW)

---

<a id="diapositiva-22"></a>

## Diapositiva 22 · Qué es el Punto de Casos de Uso

El método fue propuesto por Gustav Karner en 1993 y refinado después por otros autores. Estima el esfuerzo de un proyecto asignando pesos a los actores y a los casos de uso, y ajustando el resultado por dos conjuntos de factores.

**Qué necesita**

Un modelo de casos de uso completo, con actores identificados y con el flujo de cada caso descrito en pasos.

**Qué produce**

Un tamaño en puntos de casos de uso y, con un factor de conversión, un esfuerzo en horas- hombre.

**Qué lo diferencia**

Incorpora en la fórmula la capacidad del equipo, cosa que el punto función deja fuera y resuelve con la productividad histórica.

**Cuándo conviene**

Cuando el análisis se documentó con casos de uso o parecido, que es lo habitual en proyectos de sistemas de información.

> ⚠️ La gran ventaja sobre el punto función: el método trae incorporado el ajuste por experiencia del equipo. La gran desventaja: el resultado depende del nivel de detalle con que se escribieron los casos de uso.

---

<a id="diapositiva-23"></a>

## Diapositiva 23 · La cadena completa del método

Los actores se clasifican según la complejidad de su interacción con el sistema

**Punto de Casos de Uso sin Ajustar UUCP (Unadjusted Use Case Points)**

Los casos de uso se clasifican según la cantidad de transacciones de su flujo

**Factores Técnicos TCF (Technical Complexity Factor)**

**Punto de Casos de Uso · UCP**

**Estimación de Esfuerzo**

**Factores de Ambiente EF (Environmental Factor)**

Dos clasificaciones, una suma, dos ajustes y una conversión. Las secciones 3 y 4 construyen las cajas de arriba; la sección 5 baja del UCP a las horas de cada etapa.

---

<a id="diapositiva-24"></a>

## Diapositiva 24 · Las cinco fórmulas del método

El método completo son cinco fórmulas. Ninguna tiene dificultad aritmética: toda la dificultad está en clasificar bien y en asignar los factores con honestidad.

| Paso | Fórmula | Qué entrega | Se ve en |
|---|---|---|---|
| Tamaño sin ajustar | UUCP = UAW + UUCW | Puntos brutos del modelo | Sección 3 |
| Ajuste técnico | TCF = 0,6 + 0,01 × Σ (peso × valor) | Coeficiente de 0,60 a 1,30 | Sección 4 |
| Ajuste de ambiente | EF = 1,4 − 0,03 × Σ (peso × valor) | Coeficiente de 0,42 a 1,70 | Sección 4 |
| Tamaño ajustado | UCP = UUCP × TCF × EF | Puntos de casos de uso | Sección 4 |
| Esfuerzo | E = UCP × CF | Horas-hombre | Sección 5 |

**UCP = ( UAW + UUCW ) × TCF × EF**

**E = UCP × CF**

> ⚠️ Las dos fórmulas del recuadro son todo el método. Lo demás son dos tablas de pesos, dos tablas de factores y una tabla de distribución por etapa.

Conviene armar estas cinco filas en una planilla parametrizada: al cambiar el alcance, el resultado se recalcula solo.

---

<a id="diapositiva-25"></a>

## Diapositiva 25 · Puntos de casos de uso sin ajustar

**UUCP = UAW + UUCW**

| Símbolo | Nombre | Qué mide |
|---|---|---|
| UUCP | Puntos de casos de uso sin ajustar | El tamaño funcional bruto del sistema |
| UAW | Factor de peso de los actores sin ajustar | Cuántos actores hay y cuán compleja es su interacción |
| UUCW | Factor de peso de los casos de uso sin ajustar | Cuántos casos de uso hay y cuántas transacciones tienen |

El peso de los actores es siempre mucho menor que el de los casos de uso: en un sistema típico aporta entre el 5% y el 15% del total. Aun así se cuenta, porque distingue un sistema con un solo usuario de uno que se integra con seis sistemas externos.

> ⚠️ Los dos términos se calculan con el mismo procedimiento: clasificar cada elemento en tres niveles, multiplicar por el peso del nivel y sumar. Cambia sólo el criterio de clasificación y la tabla de pesos.

---

<a id="diapositiva-26"></a>

## Diapositiva 26 · Factor de peso de los actores sin ajustar (UAW)

Los actores se clasifican según la complejidad de su interacción con el sistema, no según su jerarquía ni su frecuencia de uso.

| Tipo de actor | Descripción | Peso |
|---|---|---|
| Simple | Otro sistema que interactúa mediante una interfaz de programación | 1 |
| Medio | Otro sistema que interactúa por protocolo o interfaz de texto | 2 |
| Complejo | Una persona que interactúa mediante una interfaz gráfica | 3 |

**UAW = Σ ( cantidad de actores de cada tipo × peso del tipo )**

La lógica del peso: integrarse con un sistema por una interfaz documentada es lo más barato; hacerlo por un protocolo de texto obliga a interpretar y validar; y construir una interfaz gráfica para una persona, con su usabilidad, sus validaciones y sus mensajes de error, es lo más caro de los tres.

> ⚠️ Un actor no es un usuario: es un rol. Cinco mil vecinos que usan la plataforma son un solo actor «Vecino» y aportan 3 puntos, no quince mil.

---

<a id="diapositiva-27"></a>

## Diapositiva 27 · Errores frecuentes al contar actores

| Error | Por qué está mal | Cómo se corrige |
|---|---|---|
| Contar usuarios en vez de roles | El actor es un rol, no una persona | Un actor por rol distinto de interacción |
| Olvidar los sistemas externos | También son actores y aportan peso | Revisar el diagrama de contexto |
| Clasificar por importancia | El peso mide la interfaz, no la jerarquía | Preguntar cómo interactúa, no quién es |
| Contar el reloj o el temporizador | Depende del autor; conviene declararlo | Fijar un criterio y aplicarlo siempre |
| Duplicar un actor que hereda de otro | La generalización no crea un actor nuevo | Contar sólo los actores concretos |

El caso del temporizador merece una decisión explícita: un proceso automático que se dispara por calendario no es una persona ni un sistema externo, pero sí genera trabajo. Varios autores lo cuentan como actor simple. Elija una postura y declárela.

> ⚠️ En una plataforma de integración los actores no humanos suelen ser más que los humanos, y cada uno esconde una interfaz que hay que construir, probar y mantener. Olvidarlos subestima el tamaño y, sobre todo, el riesgo.

El peso de los actores es pequeño, pero la lista de actores es el mejor inventario de integraciones que existe. Vale la pena hacerlo bien por esa razón sola.

---

<a id="diapositiva-28"></a>

## Diapositiva 28 · Qué es una transacción y por qué importa

El peso de un caso de uso depende de cuántas transacciones contiene. Por eso hay que tener una definición precisa y aplicarla siempre igual.

«Una transacción es un viaje de ida y vuelta que va desde el usuario hasta el sistema y vuelve al usuario. Termina cuando el sistema queda esperando un nuevo estímulo de entrada.» · Ivar Jacobson

**1**

**2**

**El actor actúa**

**El sistema procesa**

Ejecuta una acción que representa una entrada para el sistema.

Recibe la entrada, la valida y ejecuta la lógica correspondiente.

**3**

**4**

**El sistema responde**

**Vuelve a empezar**

Devuelve un resultado al actor y queda esperando.

Cuando el actor reacciona al resultado, comienza una transacción nueva.

> ⚠️ Una transacción es atómica: se ejecuta completa o no se ejecuta. Un paso interno del sistema que el actor no ve y que no le devuelve nada no es una transacción, aunque cueste trabajo construirlo.

---

<a id="diapositiva-29"></a>

## Diapositiva 29 · Factor de peso de los casos de uso sin ajustar (UUCW)

Los casos de uso se clasifican según la cantidad de transacciones que contiene su flujo, incluidos los flujos alternativos relevantes.

| Tipo de caso de uso | Descripción | Peso |
|---|---|---|
| Simple | El caso de uso contiene de 1 a 3 transacciones | 5 |
| Medio | El caso de uso contiene de 4 a 7 transacciones | 10 |
| Complejo | El caso de uso contiene 8 o más transacciones | 15 |

**UUCW = Σ ( cantidad de casos de uso de cada tipo × peso del tipo )**

Algunos autores agregan un cuarto nivel para casos de uso muy grandes, con peso 20, y otros clasifican por número de clases de análisis en lugar de transacciones. Cualquiera de las variantes es admisible: lo que no es admisible es mezclarlas dentro del mismo conteo.

> ⚠️ Si un caso de uso supera con holgura las ocho transacciones, conviene revisarlo: probablemente contiene dos objetivos distintos y debería dividirse. El método castiga poco los casos gigantes, y ése es su punto ciego.

---

<a id="diapositiva-30"></a>

## Diapositiva 30 · Cómo se cuentan las transacciones de un caso de uso

Se recorre el flujo principal y se marca cada ida y vuelta completa entre el actor y el sistema. El caso de uso «Iniciar y enviar una solicitud de trámite» del caso queda así:

| N° | Acción del actor | Respuesta del sistema |
|---|---|---|
| 1 | Selecciona el trámite que desea iniciar | Despliega el formulario correspondiente |
| 2 | Completa los datos del formulario y confirma | Valida los datos y marca los errores |
| 3 | Adjunta los documentos requeridos | Recibe los archivos y verifica formato y tamaño |
| 4 | Solicita la vista previa de la solicitud | Genera y muestra la vista previa |
| 5 | Confirma el envío | Registra la solicitud y devuelve el número de folio |
| 6 | Recibe el comprobante de recepción | Envía el comprobante por correo y mensaje |

**6 transacciones → entre 4 y 7 → caso de uso Medio → peso 10**

Los flujos alternativos se cuentan sólo si agregan idas y vueltas nuevas. Un mensaje de error dentro de una validación ya contada no es una transacción adicional.

---

<a id="diapositiva-31"></a>

## Diapositiva 31 · Reglas de conteo que conviene fijar antes de empezar

| Decisión | Opciones | Recomendación para el curso |
|---|---|---|
| Flujos alternativos | Siempre o sólo si agregan transacciones | Sólo si agregan idas y vueltas |
| Casos de uso incluidos | Contarlos aparte o dentro del que los incluye | Aparte, si tienen valor por sí mismos |
| Casos de uso de extensión | Contarlos aparte o sumarlos al base | Sumarlos al caso base |
| Casos de uso abstractos | Contarlos o no contarlos | No contarlos: no los ejecuta un actor |
| Actores no humanos periódicos | Actor simple o no contarlos | Actor simple, declarándolo |
| Granularidad | Objetivo del actor o paso de interfaz | Objetivo completo del actor |

Ninguna de estas seis decisiones tiene una respuesta universalmente correcta. Lo que sí es incorrecto es no tomarlas, o tomarlas distinto en cada caso de uso. Media página del anexo de estimación se dedica a declararlas.

> ⚠️ Redacción tipo para el anexo: «El conteo consideró los casos de uso concretos del modelo, contando los flujos alternativos sólo cuando agregan transacciones nuevas, y sumando las extensiones al caso base».

---

<a id="diapositiva-32"></a>

## Diapositiva 32 · Un ejemplo mínimo, para fijar el procedimiento

Un sistema de gestión de órdenes con un único actor humano y cuatro casos de uso, todos de 1 a 3 transacciones. Éste es su diagrama de casos de uso.

**Usuario**

**Agregar orden**

**1 actor humano, con interfaz gráfica**

**UAW = 1 × 3 = 3**

**Encontrar orden**

**Modificar orden**

**Eliminar orden**

**4 casos de uso simples, de 1 a 3 transacciones cada uno**

**UUCW = 4 × 5 = 20**

**UUCP = UAW + UUCW = 3 + 20 = 23 puntos de casos de uso sin ajustar**

Con esos 23 puntos todavía no hay estimación: falta ajustar por los factores técnicos y de ambiente, que es la sección siguiente, y convertir a horas, que es la que viene después.

---

<a id="diapositiva-33"></a>

## Diapositiva 33 · Errores frecuentes en el conteo de casos de uso

| Error | Efecto sobre el tamaño | Cómo se detecta |
|---|---|---|
| Granularidad desigual | Distorsión grande en cualquier sentido | Casos con 2 y con 25 transacciones |
| Contar pantallas como casos de uso | Infla el número de casos simples | Muchos casos de uso de una transacción |
| Un caso de uso por módulo | Subestima gravemente el tamaño | Menos de diez casos en un sistema grande |
| Olvidar los de administración | Subestima entre 10% y 20% | No hay mantenedores ni perfiles |
| Olvidar los casos de integración | Subestima y esconde riesgo técnico | Ningún caso de uso con actor no humano |
| Contar dos veces los alternativos | Infla los casos hacia complejo | Todos los casos resultan complejos |

> ⚠️ Prueba de cordura: en un sistema de información de tamaño mediano, la relación típica es de 10 a 40 casos de uso, con una mayoría de casos medios. Si su conteo se aleja mucho de eso, revise la granularidad antes que la aritmética.

Los dos errores de omisión —administración e integración— son los que más veces explican una estimación que resulta corta al ejecutar el proyecto.

---

<a id="diapositiva-34"></a>

## Diapositiva 34 · Recomendaciones para profundizar · Sección 3 · Punto de Casos de Uso

RECOMENDACIONES PARA PROFUNDIZAR

**Sección 3 · Punto de Casos de Uso**

**1**

**Fijar la granularidad**

Escriba la regla de granularidad de su modelo y revise que todos sus casos de uso la cumplan. Es la decisión que más afecta el resultado.

**2**

**Inventariar los actores**

Liste todos los actores, humanos y no humanos. Cada actor no humano es una integración que hay que construir, probar y mantener.

**3**

**Contar un caso completo**

Tome su caso de uso más importante y desglose sus transacciones como en la lámina del ejemplo. Verá si su descripción está a nivel utilizable.

**4**

**Buscar lo que falta**

Revise si su modelo tiene casos de administración, de mantenedores, de perfiles y de integración. Suelen faltar y pesan entre 10% y 20%.

**5**

**Declarar las seis reglas**

Escriba las seis decisiones de conteo en el anexo de estimación. Son media página y evitan toda discusión posterior.

**6**

**Leer a Karner**

Busque el trabajo original de Gustav Karner de 1993 y alguno de los refinamientos posteriores. Verá que las variantes del método son más de las que parece.

---

<a id="diapositiva-35"></a>

## Diapositiva 35 · ▶ SECCIÓN 4 · Factores técnicos y de ambiente

**FACTORES**

**04**

SECCIÓN 4

**Factores técnicos y de ambiente**

- Por qué el método ajusta dos veces y qué mide cada ajuste
- Los trece factores técnicos, sus pesos y qué evalúa cada uno
- Los ocho factores de ambiente y qué significa el valor asignado
- Las dos fórmulas y el rango real de cada coeficiente
- La lectura contraintuitiva del factor de ambiente

---

<a id="diapositiva-36"></a>

## Diapositiva 36 · Por qué el método ajusta dos veces

Dos proyectos con el mismo tamaño sin ajustar pueden costar muy distinto. La diferencia viene de dos lugares, y el método los separa.

**TCF · Factor de complejidad técnica**

- Habla del sistema que hay que construir
- Trece factores de exigencia técnica
- Sube el esfuerzo cuando el sistema es exigente
- Rango: de 0,60 a 1,30
- No cambia si cambia el equipo

**EF · Factor de ambiente**

- Habla del equipo que lo va a construir
- Ocho factores de experiencia y de contexto
- Baja el esfuerzo cuando el equipo es bueno
- Rango: de 0,42 a 1,70
- No cambia si cambia el sistema

> ⚠️ Ésta es la diferencia esencial con el punto función, que sólo tiene el primer ajuste. El punto de casos de uso incorpora al equipo dentro de la fórmula, y por eso su resultado ya es un esfuerzo y no sólo un tamaño.

Consecuencia práctica: dos empresas que ofertan el mismo sistema deberían obtener el mismo UUCP y distinto UCP. Si obtienen el mismo UCP, alguna de las dos no evaluó su propio equipo.

---

<a id="diapositiva-37"></a>

## Diapositiva 37 · Puntos de casos de uso ajustados

**UCP = UUCP × TCF × EF**

| Símbolo | Nombre | Rango | Qué lo mueve |
|---|---|---|---|
| UUCP | Puntos de casos de uso sin ajustar | Sin límite | El tamaño del modelo funcional |
| TCF | Factor de complejidad técnica | 0,60 a 1,30 | Exigencias técnicas del sistema |
| EF | Factor de ambiente | 0,42 a 1,70 | Condiciones del equipo y del contexto |
| UCP | Puntos de casos de uso ajustados | Resultado | El producto de los tres anteriores |

En el peor escenario combinado, TCF y EF multiplican el tamaño por 2,21; en el mejor, lo multiplican por 0,25. Es un rango enorme comparado con el ±35% del punto función, y significa que aquí los factores sí deciden el resultado.

> ⚠️ Por eso cada valor asignado a un factor debe poder justificarse en una línea. Un evaluador que quiera desarmar una estimación por puntos de casos de uso va a atacar por los factores, no por el conteo.

---

<a id="diapositiva-38"></a>

## Diapositiva 38 · Los trece factores técnicos y sus pesos

Cada factor tiene un peso fijo que define el método y un valor de 0 a 5 que asigna el equipo. La suma de los productos es el factor técnico total.

| Factor | Descripción | Peso | Factor | Descripción | Peso |
|---|---|---|---|---|---|
| T1 | Sistema distribuido | 2 | T8 | Portabilidad | 2 |
| T2 | Objetivos de desempeño | 1 | T9 | Facilidad de cambio | 1 |
| T3 | Eficiencia del usuario final | 1 | T10 | Concurrencia | 1 |
| T4 | Procesamiento interno complejo | 1 | T11 | Objetivos de seguridad | 1 |
| T5 | Código reutilizable | 1 | T12 | Acceso de terceras partes | 1 |
| T6 | Facilidad de instalación | 0,5 | T13 | Entrenamiento a usuarios | 1 |
| T7 | Facilidad de uso | 0,5 |  | Suma de los pesos | 14 |

La suma de los pesos es 14. Como cada valor va de 0 a 5, el factor técnico total va de 0 a 70, igual que en el punto función, aunque la fórmula del coeficiente sea distinta.

> ⚠️ Los factores de peso 2 son los que más mueven el resultado: un sistema distribuido con alta exigencia de portabilidad suma 20 de los 70 posibles con sólo dos respuestas.

---

<a id="diapositiva-39"></a>

## Diapositiva 39 · Qué evalúa cada factor técnico · T1 a T7

Cada factor es una pregunta sobre el sistema que hay que construir; el valor asignado responde cuánto pesa esa exigencia en este proyecto. T1 y T8 son los de mayor peso del método.

| Factor | Qué evalúa | La pregunta que hay que responder |
|---|---|---|
| T1 · Sistema distribuido (peso 2) | Si la solución se reparte entre varios nodos, servicios o capas que deben comunicarse | ¿Cuánto del procesamiento ocurre fuera de un único servidor? |
| T2 · Objetivos de desempeño (peso 1) | Si hay tiempos de respuesta o volúmenes comprometidos por contrato | ¿El desempeño es un requisito exigible o basta con que responda? |
| T3 · Eficiencia del usuario final (peso 1) | Si el usuario necesita completar su tarea rápido y con pocos pasos | ¿La productividad del usuario es un objetivo del sistema? |
| T4 · Procesamiento interno complejo (peso 1) | Cálculos, reglas de negocio, validaciones y algoritmos no triviales | ¿Cuánta lógica hay detrás de las pantallas? |
| T5 · Código reutilizable (peso 1) | Si hay que construir componentes pensados para reutilizarse en otros sistemas | ¿Se pide diseñar para reutilizar, y no sólo para funcionar? |
| T6 · Facilidad de instalación (peso 0,5) | Cuán exigente es el despliegue en los ambientes del mandante | ¿Instalar y actualizar es un trámite o un proyecto? |
| T7 · Facilidad de uso (peso 0,5) | Cuánta exigencia de usabilidad, accesibilidad y aprendizaje trae el sistema | ¿Lo va a usar un experto entrenado o cualquier ciudadano? |

---

<a id="diapositiva-40"></a>

## Diapositiva 40 · Qué evalúa cada factor técnico · T8 a T13

| Factor | Qué evalúa | La pregunta que hay que responder |
|---|---|---|
| T8 · Portabilidad (peso 2) | Si el sistema debe funcionar en más de una plataforma, navegador, dispositivo o nube | ¿Cuántos entornos distintos tiene que soportar? |
| T9 · Facilidad de cambio (peso 1) | Si se exige que la solución sea configurable y fácil de modificar después | ¿Los cambios los va a hacer el mandante sin programar? |
| T10 · Concurrencia (peso 1) | Si muchos usuarios o procesos operan al mismo tiempo sobre los mismos datos | ¿Cuántos usuarios simultáneos y qué pasa si chocan? |
| T11 · Objetivos de seguridad (peso 1) | Exigencias de autenticación, cifrado, trazabilidad y protección de datos personales | ¿Qué daño produce una filtración o un acceso indebido? |
| T12 · Acceso de terceras partes (peso 1) | Integraciones y accesos desde sistemas u organizaciones externas | ¿Cuántos sistemas ajenos entran o salen del mío? |
| T13 · Entrenamiento a usuarios (peso 1) | Cuánta capacitación y material de apoyo hay que producir y ejecutar | ¿Cuántas personas hay que capacitar y con qué profundidad? |

> ⚠️ Regla para asignarlos: responda la pregunta de la tercera columna en una frase y recién entonces ponga el número. Si no puede escribir la frase, todavía no sabe qué valor corresponde.

Los trece valores, con su frase de justificación, ocupan una tabla del anexo de estimación. Es lo primero que revisa un evaluador técnico.

---

<a id="diapositiva-41"></a>

## Diapositiva 41 · La escala de los factores técnicos y la fórmula del TCF

| Valor | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Aporte del factor | Irrelevante | Incidental | Moderado | Medio | Significativo | Muy importante |

**TCF = 0,6 + 0,01 × Σ ( peso i × valor i )**

| Situación | Factor técnico total | TCF | Efecto sobre el tamaño |
|---|---|---|---|
| Todos los factores en 0 | 0 | 0,60 | Reduce el tamaño en 40% |
| Todos los factores en 3 | 42 | 1,02 | Prácticamente neutro |
| Sistema algo exigente | 49,5 | 1,095 | Aumenta el tamaño en 9,5% |
| Todos los factores en 5 | 70 | 1,30 | Aumenta el tamaño en 30% |

> ⚠️ Asignar 3 a los trece factores da TCF ≈ 1,02, es decir, no ajustar nada. Es una respuesta legítima si el sistema es realmente promedio, pero hay que decirlo: no puede parecer que el equipo no evaluó.

Obsérvese que la base es 0,6 y no 0,65 como en el punto función: son métodos distintos y las constantes no se intercambian.

---

<a id="diapositiva-42"></a>

## Diapositiva 42 · Los ocho factores de ambiente: qué significa el valor

El valor de cada factor va de 0 a 5 y no es una nota: describe al equipo y al contexto. En los seis primeros factores un valor alto es una buena noticia; en E7 y E8 es una mala, y por eso su peso es negativo.

| Factor | Peso | Poner 0 significa | Poner 5 significa |
|---|---|---|---|
| E1 · Modelo de proyecto | 1,5 | Nunca trabajó con este modelo | Domina el modelo y lo aplica siempre |
| E2 · Experiencia en el negocio | 0,5 | Nadie conoce el negocio del mandante | Conoce el negocio del mandante a fondo |
| E3 · Orientación a objetos | 1 | Nunca desarrolló con objetos | Es experto en orientación a objetos |
| E4 · Capacidad del analista | 0,5 | El analista líder es novato en el rol | Analista muy capaz y con experiencia |
| E5 · Motivación | 1 | No hay interés en el proyecto | El equipo está muy motivado |
| E6 · Estabilidad de requisitos | 2 | El alcance cambia todo el tiempo | Requerimientos cerrados, sin cambios |
| E7 · Personal a tiempo parcial | −1 | Todos son de dedicación exclusiva | Casi todos son a tiempo parcial |
| E8 · Dificultad del lenguaje | −1 | Lenguaje y herramientas fáciles | Lenguaje extremadamente difícil |

> ⚠️ Los dos últimos factores tienen peso negativo porque su valor alto es malo: mucho personal a tiempo parcial y un lenguaje difícil aumentan el esfuerzo, y por eso restan en la suma y suben el coeficiente.

---

<a id="diapositiva-43"></a>

## Diapositiva 43 · La escala de cada factor de ambiente

| Factores | Valor 0 | Valor 3 | Valor 5 |
|---|---|---|---|
| E1 a E4 · experiencia | Sin experiencia | Experiencia media | Amplia experiencia, experto |
| E5 · motivación | Sin motivación por el proyecto | Motivación media | Alta motivación |
| E6 · estabilidad | Requerimientos muy inestables | Estabilidad media | Estables, sin cambios previstos |
| E7 · personal parcial | Nadie es a tiempo parcial | Mitad y mitad | Todo el personal es a tiempo parcial |
| E8 · dificultad del lenguaje | Lenguaje fácil de usar | Dificultad media | Lenguaje extremadamente difícil |

En los seis primeros factores, más es mejor: un valor alto describe un equipo experto, motivado y con requerimientos estables. En los dos últimos ocurre al revés, y por eso su peso es negativo: un valor alto describe una situación que encarece el proyecto.

> ⚠️ Al asignar estos ocho valores el equipo se está evaluando a sí mismo. Es el único punto del método donde hay incentivo a mentir, y también el único donde mentir se paga dos años después, en horas extra.

Consejo práctico: asigne los factores de ambiente en grupo y por consenso, no los delegue en una persona. La discusión vale más que el número.

---

<a id="diapositiva-44"></a>

## Diapositiva 44 · La fórmula del factor de ambiente y su lectura correcta

**EF = 1,4 − 0,03 × Σ ( peso i × valor i )**

| Situación del equipo | Factor total | EF | Efecto sobre el esfuerzo |
|---|---|---|---|
| Equipo experto, motivado, requisitos estables | 32,5 | 0,42 | Reduce el esfuerzo en 58% |
| Equipo bueno, requisitos algo inestables | 18,0 | 0,86 | Reduce el esfuerzo en 14% |
| Equipo medio en todo | 13,3 | 1,00 | Neutro |
| Equipo sin experiencia y a tiempo parcial | −10,0 | 1,70 | Aumenta el esfuerzo en 70% |

La suma de los pesos positivos es 6,5 y la de los negativos es −2, de modo que el factor de ambiente total va de −10 a 32,5. La segunda fila es la del equipo del caso que se desarrolla en la sección 6; la tercera muestra el punto neutro: con 13,3 el coeficiente vale 1,00 y no modifica el tamaño.

> ⚠️ Lectura correcta: el EF no mide cuán bueno es el equipo, mide cuánto trabajo le va a costar. Un EF bajo es una buena noticia. Confundirse con el signo es el error de cálculo más frecuente del método.

El rango de 0,42 a 1,70 significa que el mismo sistema, construido por dos equipos distintos, puede costar cuatro veces más en uno que en otro. El método no exagera: eso ocurre.

---

<a id="diapositiva-45"></a>

## Diapositiva 45 · Errores frecuentes al asignar los factores

| Error | Cómo se reconoce | Consecuencia |
|---|---|---|
| Poner 3 a todo | TCF ≈ 1,02 y EF ≈ 1,00 | El ajuste no aporta nada y se nota |
| Poner 5 a todo en el ambiente | EF muy bajo y esfuerzo optimista | Se compromete un plazo imposible |
| Invertir el signo de E7 y E8 | EF fuera del rango razonable | Error que altera todo el resultado |
| Confundir peso con valor | Productos que no cuadran | El total no corresponde a la tabla |
| No justificar los extremos | Valores 0 y 5 sin explicación | El evaluador los descuenta |
| Copiar factores de otro proyecto | Los mismos valores en casos distintos | El ajuste no describe este proyecto |
| Ignorar E6 con alcance abierto | Estabilidad alta y requisitos sin definir | Optimismo en toda la estimación |

> ⚠️ El último error es el más costoso y el más común en una licitación: declarar requerimientos estables cuando las bases dicen «y todo lo necesario para su correcto funcionamiento». Ese solo valor puede cambiar el esfuerzo en 20%.

Regla de coherencia: los factores de ambiente deben decir lo mismo que el registro de riesgos. Si el riesgo dice que el alcance es inestable, E6 no puede valer 5.

---

<a id="diapositiva-46"></a>

## Diapositiva 46 · Recomendaciones para profundizar · Sección 4 · Factores técnicos y de ambiente

RECOMENDACIONES PARA PROFUNDIZAR

**Sección 4 · Factores técnicos y de ambiente**

**1**

**Asignar sus trece**

Complete la tabla de factores técnicos de su caso con peso, valor y producto. Justifique en una línea cada valor 0 y cada valor 5.

**2**

**Autoevaluarse en grupo**

Asigne los ocho factores de ambiente en una conversación de equipo, no en solitario. Anote los desacuerdos: suelen ser el mejor diagnóstico del grupo.

**3**

**Probar la sensibilidad**

Cambie un solo factor de ambiente en dos puntos y recalcule. Verá cuánto se mueve el esfuerzo y entenderá por qué hay que justificar cada valor.

**4**

**Cruzar con los riesgos**

Verifique que E6, estabilidad de los requerimientos, dice lo mismo que su registro de riesgos. Es la incoherencia que más veces aparece.

**5**

**Buscar las variantes**

Varios autores proponen pesos distintos o factores adicionales. Revise al menos una variante y decida cuál va a usar, dejándolo declarado.

---

<a id="diapositiva-47"></a>

## Diapositiva 47 · ▶ SECCIÓN 5 · Del tamaño al esfuerzo

**ESFUERZO**

**05**

SECCIÓN 5

**Del tamaño al esfuerzo**

- La fórmula del esfuerzo y el factor de conversión
- Cómo se decide el factor de conversión a partir de los factores de ambiente
- Cuándo el método dice que hay que replantear el proyecto
- La distribución del esfuerzo entre las etapas del proyecto
- Del esfuerzo al plazo y del esfuerzo al precio

---

<a id="diapositiva-48"></a>

## Diapositiva 48 · La fórmula del esfuerzo

**E = UCP × CF**

| Símbolo | Nombre | Unidad | De dónde sale |
|---|---|---|---|
| E | Esfuerzo estimado | Horas-hombre | El resultado de la multiplicación |
| UCP | Puntos de casos de uso ajustados | Puntos | UUCP × TCF × EF |
| CF | Factor de conversión | Horas por punto | Del histórico propio o de Karner |

Karner propuso originalmente un valor único de 20 horas-hombre por punto de casos de uso, obtenido de los proyectos que Objectory AB tenía documentados. Refinamientos posteriores introdujeron una regla que ajusta ese valor según la situación del equipo.

> ⚠️ Un cambio de 20 a 28 horas por punto aumenta el esfuerzo en 40%. Es, con diferencia, el parámetro más sensible del método, y el que hay que justificar con más cuidado.

---

<a id="diapositiva-49"></a>

## Diapositiva 49 · Cómo se decide el factor de conversión

El refinamiento más difundido decide el factor de conversión contando cuántos factores de ambiente están en el lado desfavorable.

| Paso | Qué se cuenta |
|---|---|
| 1 | Cuántos de los factores E1 a E6 están por debajo del valor medio, es decir, con valor menor que 3 |
| 2 | Cuántos de los factores E7 y E8 están por encima del valor medio, es decir, con valor mayor que 3 |
| 3 | Se suman ambas cuentas y se obtiene un total entre 0 y 8 |

| Factores desfavorables | Factor de conversión | Qué significa |
|---|---|---|
| 2 o menos | 20 horas por punto | Situación favorable: el contexto ayuda |
| 3 o 4 | 28 horas por punto | Situación exigente: el esfuerzo sube 40% |
| 5 o más | No se estima: se replantea | El riesgo de fracaso es demasiado alto |

> ⚠️ La tercera fila es la más interesante y la que nadie usa: el método se declara incompetente cuando el equipo no está en condiciones. No entrega un número mayor, entrega una advertencia.

---

<a id="diapositiva-50"></a>

## Diapositiva 50 · El factor de conversión es el punto débil del método

Las 20 horas por punto provienen de un conjunto de proyectos de Objectory AB de comienzos de los años noventa, con tecnologías y prácticas de esa época. Usarlas sin más es una decisión que hay que justificar.

| Origen del factor de conversión | Ventaja | Riesgo |
|---|---|---|
| El valor de Karner: 20 o 28 horas | Está publicado y es defendible | No conoce a este equipo |
| Histórico propio de la empresa | Refleja al equipo real | Exige haber medido antes |
| Promedio de la industria | Sirve de contraste | Muy disperso: de 15 a 30 horas |
| Calibración durante el proyecto | Corrige el número con datos reales | Llega tarde para fijar el precio |

La práctica recomendable es doble: calcular con el valor de Karner para tener una referencia comparable con cualquier lector, y calcular también con el histórico propio si existe. Si ambos difieren mucho, esa diferencia es información sobre el equipo.

> ⚠️ Redacción tipo para el anexo: «Se utilizó el factor de conversión de 20 horas-hombre por punto de casos de uso, conforme a la regla de Karner. Se declaró además un escenario alternativo con 28 horas por punto, que es el valor que la misma regla asigna si dos factores de ambiente más se deterioran».

---

<a id="diapositiva-51"></a>

## Diapositiva 51 · La distribución del esfuerzo entre las etapas

El esfuerzo del proyecto no se reparte de forma uniforme entre las actividades. El criterio más difundido en la literatura del método propone esta distribución.

| Actividad | Porcentaje | Qué incluye |
|---|---|---|
| Análisis | 10% | Levantamiento, modelado y especificación de la funcionalidad |
| Diseño | 20% | Arquitectura, diseño detallado, datos y experiencia de usuario |
| Programación | 40% | Construcción del software y pruebas unitarias |
| Pruebas | 15% | Integración, sistema, aceptación y corrección |
| Sobrecarga | 15% | Gestión del proyecto, calidad, documentación y coordinación |

Obsérvese que la programación es sólo el 40%. Un equipo que estima únicamente lo que va a programar deja fuera el 60% del esfuerzo del proyecto, y ese 60% también se paga.

> ⚠️ Estos valores no son absolutos: varían con la organización, con el dominio y con el tipo de contrato. Lo que no varía es la lección de fondo: construir es menos de la mitad del trabajo.

---

<a id="diapositiva-52"></a>

## Diapositiva 52 · Las dos lecturas de la distribución, y cuál usa el curso

La literatura del método admite dos interpretaciones del resultado de E = UCP × CF, y la diferencia entre ambas es de dos veces y media. Hay que elegir una y declararla.

**Lectura A · el esfuerzo total**

- E = UCP × CF es el esfuerzo del proyecto completo
- La tabla de porcentajes sólo lo reparte entre actividades
- El total no cambia: se distribuye
- Es la lectura literal de la fórmula original
- Produce estimaciones más bajas

- E = UCP × CF corresponde a la actividad de programación
- Las demás actividades se agregan con la tabla
- El total del proyecto es E dividido por 0,40
- Es la lectura que sigue el texto clásico del método
- Produce estimaciones dos veces y media mayores

**Lectura B · el esfuerzo de programación**

> ⚠️ Convención del curso: se adopta la lectura B. El esfuerzo obtenido con E = UCP × CF corresponde a la programación, y el total del proyecto se obtiene dividiendo por 0,40. Debe quedar declarado en el anexo de estimación.

Cualquiera de las dos es defendible. Lo indefendible es no decir cuál se usó, porque entonces el número no se puede verificar ni comparar.

---

<a id="diapositiva-53"></a>

## Diapositiva 53 · Del esfuerzo al plazo: no es una división

Convertir horas en semanas parece una división y no lo es. Cuatro factores impiden que el plazo baje proporcionalmente al aumentar la dotación.

**Dependencias**

Hay trabajo que no puede empezar hasta que otro termine. La ruta crítica manda sobre la dotación.

**Comunicación**

Cada persona nueva agrega canales de coordinación y resta tiempo productivo al resto.

**Curva de aprendizaje**

Quien entra en la mitad del proyecto produce poco durante varias semanas y consume tiempo de otros.

**Horas productivas**

Una jornada de 8 horas rinde alrededor de 6,5 horas de trabajo de proyecto.

El procedimiento correcto es el de la clase de planificación: repartir el esfuerzo entre los paquetes de trabajo, asignar recursos por paquete, construir la red de actividades y leer la ruta crítica. El plazo sale de la red, no del cociente.

> ⚠️ Regla práctica: use el cociente sólo como cota inferior imposible de mejorar, y el cronograma como fuente del plazo que se compromete.

---

<a id="diapositiva-54"></a>

## Diapositiva 54 · Del esfuerzo al costo: la cadena de la tarifa

El esfuerzo se convierte en dinero multiplicando por una tarifa de venta por hora. Esa tarifa no es el costo del profesional: incluye la cadena completa.

| Paso | Concepto | Qué agrega |
|---|---|---|
| 1 | Sueldo bruto del perfil | El valor de mercado de la persona |
| 2 | Costo empresa | Leyes sociales, provisiones y beneficios |
| 3 | Costo por hora productiva | Descuenta reuniones, licencias y capacitación |
| 4 | Gastos generales | Arriendo, administración, licencias y ventas |
| 5 | Margen | La utilidad esperada de la empresa |
| = | Tarifa de venta por hora | La cifra que multiplica al esfuerzo en la oferta |

En el caso, esa cadena produce una tarifa de venta de $ 28.000 por hora. El costo de la estimación es simplemente el esfuerzo total multiplicado por esa tarifa, más los insumos que no son horas: licencias, infraestructura y garantías.

> ⚠️ Una estimación de esfuerzo no es una oferta económica. Entre ambas hay una tarifa, unos insumos y una reserva de contingencia, y cada una de las tres se justifica por separado.

---

<a id="diapositiva-55"></a>

## Diapositiva 55 · Errores frecuentes al convertir tamaño en esfuerzo

| Error | Cómo se reconoce | Consecuencia |
|---|---|---|
| Usar 20 sin verificar la regla | No hay cuenta de desfavorables | Puede ser 28 y falta 40% de esfuerzo |
| No declarar la lectura elegida | No se dice si E es total o programación | El número no se puede verificar |
| Estimar sólo la programación | El total es igual al de construir | Falta el 60% del esfuerzo |
| Olvidar lo que la métrica no cubre | No hay migración ni capacitación | Falta una parte grande del contrato |
| Dividir horas por dotación | El plazo sale de una división | Plazo imposible y multa segura |
| Usar el costo en vez de la tarifa | No hay gastos generales ni margen | Se vende al costo y se pierde el proyecto |
| Ignorar la advertencia del método | Cinco o más desfavorables y se estima igual | Se compromete lo que no se puede hacer |

> ⚠️ El sexto error tiene un nombre en la industria: vender al costo. Ocurre cuando alguien multiplica las horas por el sueldo dividido en 180 y presenta eso como precio. La empresa gana el contrato y pierde el año.

Los siete errores se evitan con una sola práctica: escribir el cálculo completo, paso a paso, en el anexo de estimación, con cada supuesto declarado.

---

<a id="diapositiva-56"></a>

## Diapositiva 56 · Recomendaciones para profundizar · Sección 5 · Del tamaño al esfuerzo

RECOMENDACIONES PARA PROFUNDIZAR

**Sección 5 · Del tamaño al esfuerzo**

**1**

**Aplicar la regla del CF**

Cuente los factores desfavorables de su equipo y determine su factor de conversión. Si le da 5 o más, tiene una conversación pendiente con su grupo.

**2**

**Declarar la lectura**

Escriba en el anexo si el esfuerzo calculado es el total o el de programación. Es una línea y evita que el número sea inverificable.

**3**

**Repartir por etapa**

Aplique la distribución de cinco actividades a su esfuerzo total y compare con el reparto que resultó de su propia EDT. Las diferencias son el hallazgo.

**4**

**Reconstruir la tarifa**

Rehaga la cadena de sueldo a tarifa de venta con los valores de su empresa ficticia. Debe poder mostrarla si el evaluador la pide.

**5**

**Buscar la calibración**

Investigue qué rangos de horas por punto reporta la literatura para su tipo de sistema. Le servirá para justificar su elección o para dudar de ella.

---

<a id="diapositiva-57"></a>

## Diapositiva 57 · ▶ SECCIÓN 6 · Ejemplo completo, paso a paso

**EJEMPLO**

**06**

SECCIÓN 6

**Ejemplo completo, paso a paso**

- El sistema a estimar y su modelo de casos de uso
- Los diez pasos del método, con todas las tablas llenas
- De los actores al esfuerzo de cada etapa del proyecto
- De las horas de cada etapa a los pesos y a las UF de la oferta
- Qué tan sensible es el resultado a cada parámetro

---

<a id="diapositiva-58"></a>

## Diapositiva 58 · El caso que vamos a estimar

Una municipalidad licita una plataforma para que sus vecinos hagan trámites por internet. Una empresa de software prepara la oferta y necesita saber, antes de poner un precio, cuántas horas cuesta construirla. Todo lo que sigue estima el alcance de la derecha y ningún otro: si ese alcance cambia, hay que recalcular.

**El encargo**

- Mandante: I. Municipalidad de Costa Azul (85.000 habitantes)
- Licitación pública ID 3456-12-LP26
- Objeto: una plataforma web donde el vecino inicia, paga y sigue sus trámites sin ir al municipio
- Plazo: 10 meses de proyecto y 24 de operación
- Presupuesto: $ 320.000.000 IVA incluido
- Oferente: Integra TIC SpA, casa de software
- Tarifa de venta: $ 28.000 por hora

**El alcance que se compromete**

- 8 de los 12 trámites pedidos; los 4 restantes son etapa opcional
- Canales: portal del vecino y del funcionario
- Cinco integraciones: ClaveÚnica, contabilidad, pagos, Registro Civil y notificaciones
- Transversales: autenticación, notificaciones, pagos, reportería y auditoría
- Administración: catálogo de trámites, flujos, usuarios y perfiles
- Fuera: digitalizar expedientes, la etapa 2 y cambiar el sistema contable
- Del análisis: 14 casos de uso y 8 actores

---

<a id="diapositiva-59"></a>

## Diapositiva 59 · Paso 1 · Peso de los actores (UAW)

Cada actor se clasifica según la forma de su interacción con el sistema y se le asigna el peso correspondiente.

| Actor | Forma de interacción | Tipo | Peso |
|---|---|---|---|
| Vecino | Persona que interactúa mediante interfaz gráfica | Complejo | 3 |
| Funcionario municipal | Persona que interactúa mediante interfaz gráfica | Complejo | 3 |
| Administrador del sistema | Persona que interactúa mediante interfaz gráfica | Complejo | 3 |
| Servicio de notificaciones | Otro sistema, protocolo de texto (SMTP y SMS) | Medio | 2 |
| ClaveÚnica | Otro sistema, interfaz de programación | Simple | 1 |
| Sistema financiero-contable | Otro sistema, interfaz de programación | Simple | 1 |
| Pasarela de pago | Otro sistema, interfaz de programación | Simple | 1 |
| Registro Civil | Otro sistema, interfaz de programación | Simple | 1 |
| UAW · peso de los actores | 3 complejos, 1 medio y 4 simples |  | 15 |

**UAW = 3 × 3 + 1 × 2 + 4 × 1 = 15**

Los cinco actores no humanos representan las cinco integraciones del proyecto. Aportan poco peso, pero son la mitad del riesgo técnico del contrato.

---

<a id="diapositiva-60"></a>

## Diapositiva 60 · Paso 2 · Peso de los casos de uso (UUCW)

Los catorce casos de uso del modelo, con el número de transacciones de su flujo, el tipo que les corresponde y su peso.

| ID | Caso de uso | Trans. | Peso | ID | Caso de uso | Trans. | Peso |
|---|---|---|---|---|---|---|---|
| CU-01 | Autenticarse con ClaveÚnica | 3 | 5 | CU-08 | Adjuntar y validar documentos | 5 | 10 |
| CU-02 | Consultar el estado de un trámite | 2 | 5 | CU-09 | Pagar derechos en línea | 6 | 10 |
| CU-03 | Descargar comprobante o certificado | 2 | 5 | CU-10 | Revisar y observar una solicitud | 5 | 10 |
| CU-04 | Consultar deuda municipal | 3 | 5 | CU-11 | Resolver y firmar una solicitud | 7 | 10 |
| CU-05 | Administrar usuarios y perfiles | 3 | 5 | CU-12 | Notificar al vecino | 4 | 10 |
| CU-06 | Bandeja del funcionario | 3 | 5 | CU-13 | Configurar el flujo de un trámite | 11 | 15 |
| CU-07 | Iniciar y enviar una solicitud | 6 | 10 | CU-14 | Conciliar pagos con contabilidad | 9 | 15 |

| Tipo | Cantidad | Peso unitario | Subtotal |
|---|---|---|---|
| Simple · 1 a 3 transacciones | 6 | 5 | 30 |
| Medio · 4 a 7 transacciones | 6 | 10 | 60 |
| Complejo · 8 o más transacciones | 2 | 15 | 30 |
| UUCW | 14 |  | 120 |

---

<a id="diapositiva-61"></a>

## Diapositiva 61 · Paso 3 · Puntos de casos de uso sin ajustar (UUCP)

| Componente | Detalle | Puntos | Participación |
|---|---|---|---|
| UAW · actores | 3 complejos, 1 medio, 4 simples | 15 | 11,1% |
| UUCW · casos de uso | 6 simples, 6 medios, 2 complejos | 120 | 88,9% |
| UUCP | Tamaño funcional sin ajustar | 135 | 100% |

**UUCP = UAW + UUCW = 15 + 120 = 135 puntos sin ajustar**

Este número mide sólo el modelo funcional. No sabe nada de la tecnología que se va a usar ni del equipo que va a construir: eso entra en los dos pasos siguientes.

> ⚠️ Verificación de cordura: 135 puntos sin ajustar para una plataforma de ocho trámites con cinco integraciones es un valor razonable. Si hubiese dado 40 o 400, habría que revisar la granularidad del modelo antes de seguir.

El reparto de 11% en actores y 89% en casos de uso es el típico de un sistema de información. Un valor muy distinto suele indicar actores mal contados.

---

<a id="diapositiva-62"></a>

## Diapositiva 62 · Pasos 4 y 5 · Los dos coeficientes de ajuste

**TCF · complejidad técnica**

- Trece factores evaluados de 0 a 5
- Valores altos: seguridad 5, facilidad de uso 5
- Valores bajos: instalación 2
- Factor técnico total = 49,5
- TCF = 0,6 + 0,01 × 49,5 = 1,095
- El sistema es 9,5% más exigente que el promedio

**EF · ambiente del equipo**

- Ocho factores evaluados de 0 a 5
- Valores altos: modelo 4, motivación 4
- Valores bajos: dominio 2, estabilidad 2
- Factor de ambiente total = 18
- EF = 1,4 − 0,03 × 18 = 0,86
- El equipo reduce el esfuerzo en 14%

Los dos coeficientes empujan en sentidos opuestos: el sistema es algo más exigente que el promedio y el equipo es algo mejor que el promedio. El producto de ambos es 0,94, es decir, casi neutro.

> ⚠️ Que el ajuste combinado quede cerca de 1 no significa que no haya que calcularlo: significa que este proyecto y este equipo se compensan, y eso es un hallazgo que hay que poder mostrar.

---

<a id="diapositiva-63"></a>

## Diapositiva 63 · Paso 6 · Puntos de casos de uso ajustados (UCP)

**UCP = UUCP × TCF × EF**

**135 × 1,095 × 0,86 = 127,13 puntos de casos de uso**

| Paso del cálculo | Operación | Resultado | Efecto acumulado |
|---|---|---|---|
| Tamaño sin ajustar | UAW + UUCW | 135 puntos | Punto de partida |
| Ajuste técnico | 135 × 1,095 | 147,83 puntos | +9,5% |
| Ajuste de ambiente | 147,83 × 0,86 | 127,13 puntos | −5,8% neto |
| Tamaño ajustado | UCP | 127,1 puntos | El valor que va a horas |

> ⚠️ El resultado neto es 5,8% menor que el tamaño sin ajustar. Ese porcentaje es la respuesta cuantificada a la pregunta «¿cuánto ayuda o estorba el contexto de este proyecto?».

Se conservan dos decimales durante el cálculo y se redondea sólo al final. Redondear en cada paso puede mover el resultado varias decenas de horas.

---

<a id="diapositiva-64"></a>

## Diapositiva 64 · Paso 7 · Factor de conversión

Se cuentan los factores de ambiente que están del lado desfavorable: E1 a E6 con valor menor que 3, y E7 y E8 con valor mayor que 3.

| Grupo | Factores | Condición | Cuántos cumplen |
|---|---|---|---|
| E1 a E6 | Modelo, dominio, objetos, analista, motivación, estabilidad | Menor que 3 | 2 · dominio (E2) y estabilidad (E6) |
| E7 y E8 | Personal a tiempo parcial y dificultad del lenguaje | Mayor que 3 | 0 |
| Total |  |  | 2 |

**Total = 2 → 2 o menos → CF = 20 horas-hombre por punto de casos de uso**

Los dos factores desfavorables son precisamente los que el registro de riesgos identificó como críticos: es la primera plataforma municipal de este equipo y los trámites del alcance todavía no tienen sus flujos formalizados. La estimación y el registro de riesgos dicen lo mismo, y eso es coherencia.

> ⚠️ Si esos dos factores empeoraran y se sumaran dos más, el factor de conversión pasaría a 28 y el esfuerzo del proyecto subiría 40% sin cambiar una sola línea del alcance.

---

<a id="diapositiva-65"></a>

## Diapositiva 65 · Paso 8 · El esfuerzo

**E = UCP × CF = 127,1 × 20 = 2.542 horas-hombre de programación**

Conforme a la convención adoptada, esas horas corresponden a la actividad de programación, que representa el 40% del esfuerzo del proyecto. El total se obtiene dividiendo por 0,40.

**Esfuerzo total = 2.542 ÷ 0,40 = 6.355 horas-hombre**

| Concepto | Valor |
|---|---|
| Puntos de casos de uso ajustados | 127,1 UCP |
| Factor de conversión | 20 horas por punto |
| Esfuerzo de programación | 2.542 horas |
| Esfuerzo total del proyecto | 6.355 horas |

Si se hubiese adoptado la otra lectura, el esfuerzo total sería de 2.542 horas. La diferencia entre ambas convenciones es de dos veces y media: por eso hay que declarar cuál se usó.

---

<a id="diapositiva-66"></a>

## Diapositiva 66 · Paso 9 · La estimación por etapa

Aplicando al esfuerzo total de 6.355 horas la distribución por actividad de la sección 5, la estimación por etapa queda así.

| Etapa | % | Horas | Qué incluye |
|---|---|---|---|
| Análisis | 10% | 636 | Levantamiento, modelado de casos de uso y especificación |
| Diseño | 20% | 1.271 | Arquitectura, diseño detallado y modelo de datos |
| Programación | 40% | 2.542 | Construcción del software, integraciones y pruebas unitarias |
| Pruebas | 15% | 953 | Integración, sistema, aceptación y corrección de defectos |
| Sobrecarga (otras actividades) | 15% | 953 | Gestión, calidad, documentación y coordinación |
| Total del proyecto | 100% | 6.355 | Etapa 1 completa, sin operación ni insumos |

Estas cinco cifras son las que después se reparten entre los paquetes de trabajo de la EDT y las que fijan la dotación de cada etapa en el cronograma. No es una tabla decorativa: es la entrada del plan de trabajo.

> ⚠️ Prueba de coherencia obligatoria: la suma de horas de su EDT debe coincidir con este total, y el reparto por actividad debe parecerse a estos porcentajes. Si su EDT asigna a pruebas mucho menos del 15%, revísela antes de fijar el precio.

---

<a id="diapositiva-67"></a>

## Diapositiva 67 · Paso 10 · De horas a pesos y a UF

Con la tarifa de venta de $ 28.000 por hora, el esfuerzo se convierte en dinero etapa por etapa. Se expresa además en UF, porque un contrato de 34 meses no se puede cotizar en pesos nominales sin perder valor.

| Etapa | Horas | Costo en pesos | Costo en UF |
|---|---|---|---|
| Análisis | 636 | $ 17.808.000 | 435,83 UF |
| Diseño | 1.271 | $ 35.588.000 | 870,97 UF |
| Programación | 2.542 | $ 71.176.000 | 1.741,95 UF |
| Pruebas | 953 | $ 26.684.000 | 653,06 UF |
| Sobrecarga (otras actividades) | 953 | $ 26.684.000 | 653,06 UF |
| Total de servicios profesionales | 6.355 | $ 177.940.000 | 4.354,87 UF |

**Supuesto declarado: 1 UF = $ 40.860 al 21 de agosto de 2026**

> ⚠️ **Tarifa = $ 28.000 / hora = 0,6853 UF / hora**

Los $ 177.940.000 son sólo servicios profesionales de la etapa 1. Faltan licencias, infraestructura, migración, capacitación, los 24 meses de operación y la reserva de contingencia. Sobre el presupuesto disponible de $ 320.000.000 con IVA, eso deja poco margen y hay que decidirlo antes de presentar.

---

<a id="diapositiva-68"></a>

## Diapositiva 68 · Qué tan sensible es el resultado a cada parámetro

Se cambia un parámetro a la vez, se rehace el cálculo completo y se compara con el caso base. La variación mide cuánto se movería el esfuerzo total —y con él el precio— si sólo cambiara ese dato.

| Escenario | Qué cambia | Cómo se recalcula | Esfuerzo | Variación |
|---|---|---|---|---|
| Caso base | El cálculo de los pasos 1 a 9 | UCP 127,1 × 20 ÷ 0,40 | 6.355 h | — |
| Factor de conversión 28 | Se deterioran dos factores más | UCP 127,1 × 28 ÷ 0,40 | 8.900 h | +40% |
| Tres casos de uso medios más | Tres funciones más: UUCP 165 | UCP 155,4 × 20 ÷ 0,40 | 7.770 h | +22% |
| Equipo promedio, EF = 1,00 | El equipo es sólo promedio | UCP 147,8 × 20 ÷ 0,40 | 7.390 h | +16% |
| Sistema promedio, TCF = 1,00 | Menos seguridad y usabilidad | UCP 116,1 × 20 ÷ 0,40 | 5.805 h | −9% |

**Variación = ( esfuerzo del escenario − 6.355 ) ÷ 6.355**

**Ejemplo: ( 8.900 − 6.355 ) ÷ 6.355 = +40%**

El parámetro dominante es el factor de conversión: un solo escalón mueve el total en 40%. El segundo es la completitud del modelo: tres casos de uso olvidados valen 22%. El ajuste técnico, en cambio, casi no mueve la aguja.

> ⚠️ Conclusión operativa: dedique el tiempo del equipo a completar el modelo y a evaluarse con honestidad. Discutir si un factor técnico vale 3 o 4 es tiempo perdido.

---

<a id="diapositiva-69"></a>

## Diapositiva 69 · La cadena completa en una sola lámina

| Paso | Concepto | Cálculo | Resultado |
|---|---|---|---|
| 1 | Peso de los actores | 3×3 + 1×2 + 4×1 | 15 |
| 2 | Peso de los casos de uso | 6×5 + 6×10 + 2×15 | 120 |
| 3 | Puntos sin ajustar | UUCP = 15 + 120 | 135 |
| 4 | Factor de complejidad técnica | TCF = 0,6 + 0,01 × 49,5 | 1,095 |
| 5 | Factor de ambiente | EF = 1,4 − 0,03 × 18 | 0,86 |
| 6 | Puntos ajustados | UCP = 135 × 1,095 × 0,86 | 127,1 |
| 7 | Factor de conversión | 2 factores desfavorables | 20 h/UCP |
| 8 | Esfuerzo de programación | E = 127,1 × 20 | 2.542 h |
| 9 | Esfuerzo total del proyecto | 2.542 ÷ 0,40 | 6.355 h |
| 10 | Costo de servicios profesionales | 6.355 × $ 28.000 | $ 177.940.000 |

> ⚠️ Diez pasos, cuatro tablas de factores y una división. Todo cabe en una planilla y en una página del anexo, y cualquier evaluador puede rehacer el cálculo con los datos que la propuesta entrega.

Ésa es la propiedad que hace defendible una estimación: que otro pueda repetirla y llegar al mismo número.

---

<a id="diapositiva-70"></a>

## Diapositiva 70 · Recomendaciones para profundizar · Sección 6 · Ejemplo completo, paso a paso

RECOMENDACIONES PARA PROFUNDIZAR

**Sección 6 · Ejemplo completo, paso a paso**

**1**

**Repetir los diez pasos**

Aplique la misma secuencia a su propio caso. La tabla de la última lámina es la plantilla: rellénela con sus números y no se salte ninguna fila.

**2**

**Armar la planilla**

Construya una planilla con los diez pasos parametrizados. Le va a permitir recalcular en segundos cuando cambie el alcance, que va a cambiar.

**3**

**Hacer la sensibilidad**

Repita los cuatro escenarios alternativos con sus propios datos. El rango que resulte es su estimación honesta, y el punto es lo que compromete.

**4**

**Comparar con su EDT**

Ponga lado a lado la estimación por UCP y la de su propia EDT, etapa por etapa. Las diferencias por etapa son el hallazgo, no el total.

**5**

**Revisar sus pruebas**

Si su EDT asigna a pruebas mucho menos del 15% del total, revísela antes de fijar el precio: es la actividad que más veces queda subestimada.

**6**

**Declarar los supuestos**

Escriba los supuestos del cálculo: alcance, granularidad, lectura de la distribución y origen del factor de conversión. Son cuatro líneas.

---

<a id="diapositiva-71"></a>

## Diapositiva 71 · ▶ SECCIÓN 7 · Aclaraciones y glosario

**GLOSARIO**

**07**

SECCIÓN 7

**Aclaraciones y glosario**

- Esfuerzo no es lo mismo que plazo
- Costo no es lo mismo que venta
- Lo que se estima es esfuerzo y costo, no plazo ni precio
- El glosario del método, para el anexo de estimación

---

<a id="diapositiva-72"></a>

## Diapositiva 72 · Tres distinciones que hay que tener claras

Antes de cerrar, tres pares de conceptos que en las propuestas aparecen mezclados. Confundirlos no es un error de redacción: cambia el número que se compromete.

| No es lo mismo | Qué es cada uno | Qué pasa cuando se confunden |
|---|---|---|
| Esfuerzo no es Plazo | El esfuerzo son horas-hombre: cuánto trabajo cuesta. El plazo son semanas de calendario: cuánto tiempo transcurre. Salen de cosas distintas: el esfuerzo del tamaño, el plazo de la red de actividades y de la dotación. | Se anuncia una fecha dividiendo horas por personas. El esfuerzo no se reparte de forma lineal: la ruta crítica no se acorta agregando gente. |
| Costo no es Venta | El costo es lo que la empresa gasta en producir: sueldos, leyes sociales, infraestructura y gastos generales. La venta es el precio que se ofrece al mandante, que incluye margen, riesgo y decisión comercial. | Se cotiza al costo y se gana el contrato perdiendo el año. O se rebaja el precio bajando el esfuerzo estimado, que es peor: se compromete un trabajo que no alcanza. |
| Se estima Esfuerzo y Costo | Los métodos de esta clase estiman dos cosas y sólo dos: el esfuerzo, en horas, y el costo, en pesos o en UF. El plazo se obtiene después, del cronograma; el precio de venta se decide después, con criterio comercial. | Se presenta un plazo o un precio como si fueran resultado del cálculo, y no se puede explicar de dónde salieron cuando el evaluador pregunta. |

> ⚠️ Regla de redacción para el anexo: el cálculo entrega esfuerzo y costo. El plazo se declara con el cronograma detrás y el precio con la política comercial detrás. Tres números, tres orígenes distintos.

---

<a id="diapositiva-73"></a>

## Diapositiva 73 · Glosario del método

| Sigla | Nombre | Qué es |
|---|---|---|
| UAW | Unadjusted Actor Weight | Factor de peso de los actores sin ajustar |
| UUCW | Unadjusted Use Case Weight | Factor de peso de los casos de uso sin ajustar |
| UUCP | Unadjusted Use Case Points | Puntos de casos de uso sin ajustar: UAW + UUCW |
| TCF | Technical Complexity Factor | Factor de complejidad técnica: 0,6 + 0,01 × ΣT |
| EF | Environmental Factor | Factor de ambiente: 1,4 − 0,03 × ΣE |
| UCP | Use Case Points | Puntos de casos de uso ajustados: UUCP × TCF × EF |
| CF | Conversion Factor | Horas-hombre por punto de casos de uso |
| Transacción | Round trip de Jacobson | Una ida y vuelta completa entre el actor y el sistema |
| UFP | Unadjusted Function Points | Puntos función sin ajustar |
| FP | Function Points | Puntos función ajustados: UFP × TCF |
| EI · EO · EQ | External Input, Output, Query | Las tres funciones de transacción del punto función |
| ILF · EIF | Internal Logical File, External Interface File | Las dos funciones de datos del punto función |

---

<a id="diapositiva-74"></a>

## Diapositiva 74 · Lo que hay que llevarse de esta clase

**Se mide funcionalidad**

No líneas de código: lo que el usuario recibe, con independencia de cómo se construya.

**Tamaño no es esfuerzo**

Entre uno y otro hay un factor de conversión, y ése es el parámetro más sensible.

**Programar es el 40%**

El resto es análisis, diseño, pruebas y gestión, y también se paga.

**Esfuerzo y costo**

Es lo que el método estima. El plazo sale del cronograma y el precio, de una decisión.

**Se compromete un valor**

Y se declara un rango. Un número solo parece precisión y es una apuesta.

En el caso del curso, el método produjo un tamaño de 127,1 puntos de casos de uso y un esfuerzo de 6.355 horas repartidas en cinco etapas, que a la tarifa de venta equivalen a $ 177.940.000, es decir 4.354,87 UF al valor declarado en el ejemplo.

> ⚠️ Nada de eso es un anexo: todo eso es la base del precio. Ésa es la diferencia entre una oferta calculada y una oferta estimada a ojo.

Referencias: Albrecht y el manual de prácticas de conteo del IFPUG para punto función; Gustav Karner, Objectory AB, 1993, y sus refinamientos posteriores para punto de casos de uso.

---

<a id="diapositiva-75"></a>

## Diapositiva 75 · Recomendaciones para profundizar · Sección 7 · Aclaraciones y glosario

RECOMENDACIONES PARA PROFUNDIZAR

**Sección 7 · Aclaraciones y glosario**

**1**

**Separar los tres números**

Revise su propuesta y verifique que esfuerzo, plazo y precio aparecen como tres cifras distintas, cada una con su origen explicado.

**2**

**Reconstruir la tarifa**

Rehaga la cadena de sueldo bruto a tarifa de venta con los valores de su empresa ficticia. Debe poder mostrarla si el evaluador la pide.

**3**

**Cotizar en UF**

Exprese también en UF el total de su oferta. En un contrato de varios años, cotizar en pesos nominales es regalar la inflación.

**4**

**Usar el vocabulario**

Escriba el anexo de estimación con las siglas del glosario y su significado en la primera aparición. Es lo que hace que el documento se lea como profesional.

**5**

**Leer las fuentes**

El trabajo de Karner de 1993 y el manual de conteo del IFPUG. Después de esta clase se leen rápido y aclaran las variantes del método.
