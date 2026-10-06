# FEP04 · Gestión de los Riesgos en Proyectos TIC

> Transcripción a Markdown de la presentación original (127 diapositivas). Los diagramas se representan con su texto; los elementos puramente gráficos no se incluyen.

## Índice de secciones

- [SECCIÓN 1 · Qué es un riesgo](#diapositiva-2) — diapositiva 2
- [SECCIÓN 2 · El proceso de gestión de riesgos](#diapositiva-15) — diapositiva 15
- [SECCIÓN 3 · Identificar los riesgos](#diapositiva-27) — diapositiva 27
- [SECCIÓN 4 · Analizar los riesgos](#diapositiva-41) — diapositiva 41
- [SECCIÓN 5 · Responder a los riesgos](#diapositiva-57) — diapositiva 57
- [SECCIÓN 6 · Riesgos de la licitación](#diapositiva-71) — diapositiva 71
- [SECCIÓN 7 · Del riesgo a la solución](#diapositiva-87) — diapositiva 87
- [SECCIÓN 8 · Declarar el riesgo y su etapa](#diapositiva-102) — diapositiva 102
- [SECCIÓN 9 · En su propuesta](#diapositiva-116) — diapositiva 116

---

<a id="diapositiva-1"></a>

## Diapositiva 1 · Portada

Pontificia Universidad Católica de Valparaíso Escuela de Informática

**Taller Formulación de Proyectos Informáticos**

**ICI-5444**

**Antonio Moya Villegas**

antonio.moya@pucv.cl

v3.1.0 - 2026

---

<a id="diapositiva-2"></a>

## Diapositiva 2 · ▶ SECCIÓN 1 · Qué es un riesgo

**RIESGO**

**01**

SECCIÓN 1

**Qué es un riesgo**

- Incertidumbre, riesgo, problema: tres cosas distintas que se confunden
- Probabilidad, impacto, exposición, marco de tiempo y evento de disparo
- Amenazas y oportunidades: por qué el riesgo también se puede ganar
- Por qué los proyectos TIC fallan y en qué momento se decide su fracaso
- El riesgo es caro tarde y barato temprano: la curva que gobierna la clase

---

<a id="diapositiva-3"></a>

## Diapositiva 3 · Incertidumbre, riesgo y problema

El riesgo nace de la incertidumbre, pero no es lo mismo que ella, y sobre todo no es lo mismo que un problema. Los tres se gestionan con instrumentos distintos.

**Incertidumbre**

Falta de certeza: un estado de conocimiento limitado que impide describir la situación actual o los resultados futuros. Es la materia prima, no el objeto de gestión.

**Riesgo**

Evento o condición incierta que, de ocurrir, tiene un efecto sobre uno o más objetivos del proyecto. Todavía no pasó. Se gestiona con respuestas planificadas y reservas.

**Problema**

Un hecho que ya ocurrió y que está afectando al proyecto ahora. Se gestiona con acciones correctivas, no con probabilidad. Si está en su registro de riesgos, está en el lugar equivocado.

Fuente conceptual: PMBOK, área de conocimiento Gestión de los Riesgos del Proyecto. El vocabulario importa porque las bases de licitación lo usan.

> ⚠️ Regla de escritura: si puede poner el verbo en pasado, no es un riesgo. «El proveedor no entregó la API» es un problema; «puede que el proveedor no entregue la API» es un riesgo.

---

<a id="diapositiva-4"></a>

## Diapositiva 4 · Definición formal y las dos caras del riesgo

«Un riesgo es un evento o condición incierta que, si ocurre, tiene un efecto positivo o negativo sobre uno o más objetivos del proyecto». La palabra que casi nadie lee es positivo.

**Amenaza (riesgo negativo)**

- Si ocurre, empeora el plazo, el costo, el alcance o la calidad
- Respuestas: escalar, evitar, transferir, mitigar o aceptar
- Ejemplo TIC: la interfaz del sistema legado no está documentada
- Se financia con reserva de contingencia

**Oportunidad (riesgo positivo)**

- Si ocurre, mejora el plazo, el costo, el alcance o la calidad
- Respuestas: escalar, explotar, compartir, mejorar o aceptar
- Ejemplo TIC: el cliente ya tiene licencias de nube reutilizables
- Se transforma en mejor precio o en más alcance por el mismo precio

En el lenguaje corriente «riesgo» se usa sólo para la amenaza. En una propuesta conviene usar el vocabulario formal: da la impresión, correcta, de que se sabe lo que se está haciendo.

> ⚠️ Buscar oportunidades no es optimismo: es la única forma legítima de bajar el precio sin bajar el alcance ni sacrificar el margen.

---

<a id="diapositiva-5"></a>

## Diapositiva 5 · La idea rectora de esta clase

Hay dos formas de tratar el riesgo en una propuesta. Sólo una de ellas se evalúa bien, y no es la que se hace habitualmente.

**Riesgo como anexo**

- Se escribe al final, con el alcance, la arquitectura y el precio ya cerrados
- Lista genérica: «retraso», «cambios de alcance», «rotación de personal»
- Respuestas sin dueño ni fecha: «monitorear», «coordinar», «gestionar»
- No cambia una sola línea de la oferta
- El evaluador lo lee en treinta segundos y lo descuenta

- Se identifica leyendo las bases, antes de fijar alcance y arquitectura
- Es específico de este cliente, este sistema y esta operación
- Cada respuesta tiene acción, dueño, costo, disparador y etapa
- Cambia el alcance, un requisito, la arquitectura o el precio
- El evaluador rastrea el riesgo hasta la solución ofertada

**Riesgo como decisión**

> ⚠️ Un riesgo que no modificó nada de la propuesta no fue gestionado: fue mencionado. Esta clase enseña a hacer la diferencia y a dejarla escrita.

---

<a id="diapositiva-6"></a>

## Diapositiva 6 · Los cinco elementos que definen un riesgo

| Elemento | Qué es | Cómo se expresa | Qué pasa si falta |
|---|---|---|---|
| Probabilidad | Posibilidad de que el evento incierto se materialice | Discreta (alta, media, baja) o continua (0 a 100%) | No se puede priorizar ni calcular valor esperado |
| Impacto | Magnitud del efecto sobre un objetivo si el evento ocurre | Discreto (alto, medio, bajo) o en la unidad del objetivo: días, pesos, funciones | No se puede dimensionar la reserva |
| Exposición | Combinación de ambos: el nivel de riesgo | E = Probabilidad × Impacto | No hay criterio objetivo para decidir dónde gastar |
| Marco de tiempo | Ventana del proyecto en que el riesgo puede materializarse | «Entre la semana 6 y la 14», «durante la marcha blanca» | La respuesta se planifica tarde o se paga todo el proyecto |
| Evento de disparo | Señal observable de que el riesgo se está materializando | «Si a la semana 8 no hay ambiente de pruebas del cliente» | El plan de contingencia nunca se activa a tiempo |

> ⚠️ Exposición = Probabilidad × Impacto. Es la fórmula más simple de la clase y la que ordena todas las decisiones que vienen después.

---

<a id="diapositiva-7"></a>

## Diapositiva 7 · Escalas de probabilidad e impacto: hay que definirlas antes

«Alto» y «bajo» no significan nada si no están definidos. Antes de calificar el primer riesgo hay que fijar la escala y dejarla escrita en el plan de gestión de riesgos.

| Escala | Probabilidad | Impacto en plazo | Impacto en costo | Impacto en alcance y calidad |
|---|---|---|---|---|
| Muy alto | > 70% | > 6 semanas | > 5% del contrato | Efecto muy significativo sobre la funcionalidad comprometida |
| Alto | 51 –70% | 3 a 6 semanas | 2 –5% del contrato | Efecto significativo sobre la funcionalidad comprometida |
| Medio | 31 –50% | 1 a 3 semanas | 1 –2% del contrato | Efecto sobre áreas funcionales clave |
| Bajo | 11 –30% | 2 días a 1 semana | 0,5 –1% del contrato | Efecto menor sobre la funcionalidad general |
| Muy bajo | 1 –10% | < 2 días | < 0,5% del contrato | Efecto menor sobre funciones secundarias |

Los umbrales de la columna de costo están expresados como porcentaje del contrato, no en pesos: así la misma escala sirve para un proyecto de $ 50 millones y para uno de $ 500 millones.

---

<a id="diapositiva-8"></a>

## Diapositiva 8 · La matriz de exposición y las zonas de acción

Cruzando probabilidad e impacto se obtiene la exposición. Lo importante no es el color: es la regla de acción asociada a cada zona, que también se declara antes de empezar.

| Zona | Rango de exposición | Regla de acción declarada | Dónde se ve en la oferta |
|---|---|---|---|
| Crítica | P ×I ≥ 0,40 | Se cambia el diseño para que el riesgo deje de existir, o no se oferta | Alcance, arquitectura o exclusión explícita |
| Alta | 0,20 ≤ P ×I < 0,40 | Acción de mitigación con costo y plazo dentro del plan de trabajo | Actividad en la EDT y en el cronograma |
| Media | 0,08 ≤ P ×I < 0,20 | Se acepta activamente: reserva de contingencia y disparador definido | Línea de reserva en la oferta económica |
| Baja | P ×I < 0,08 | Se acepta pasivamente: queda en observación y se revisa cada mes | Registro de riesgos, sin costo asociado |

> ⚠️ El umbral que separa «crítica» de «alta» es la decisión más importante del plan de riesgos: define a partir de qué punto la empresa prefiere cambiar la solución antes que pagar la consecuencia.

Los rangos son los de este curso. Cada organización fija los suyos según su apetito al riesgo, y debe declararlos.

---

<a id="diapositiva-9"></a>

## Diapositiva 9 · Apetito, tolerancia y umbral: tres palabras que no son sinónimos

**Apetito al riesgo**

Cuánta incertidumbre la organización está dispuesta a asumir a cambio de la recompensa esperada. Es una postura estratégica: una empresa que entra a un mercado nuevo tiene más apetito que una que defiende su cartera.

**Tolerancia al riesgo**

Cuánta desviación acepta en un objetivo concreto. Se expresa con número: «aceptamos hasta 10% de sobrecosto», «no aceptamos ningún día de atraso en el hito contractual».

**Umbral de riesgo**

El punto exacto en que se dispara una acción o un escalamiento. Es operativo: «si la exposición total supera $ 15 millones, el gerente general debe autorizar seguir».

En una licitación las tres se traducen en decisiones concretas y distintas: el apetito decide si la empresa se presenta o no; la tolerancia decide cuánta reserva se carga al precio; el umbral decide en qué momento de la ejecución hay que escalar al directorio.

> ⚠️ Si el equipo no ha declarado estas tres cosas antes de cotizar, el precio que va a entregar no es una decisión: es una apuesta que nadie autorizó.

En el curso, la declaración de apetito y tolerancia se escribe una vez y se cita en el plan de riesgos de la propuesta.

---

<a id="diapositiva-10"></a>

## Diapositiva 10 · La curva que gobierna toda la clase

Al principio del proyecto la incertidumbre es máxima y el costo de cambiar algo es mínimo. Al final ocurre exactamente lo contrario. Las dos curvas se cruzan una sola vez.

| Momento | Incertidumbre | Costo de cambiar | Qué se puede hacer todavía |
|---|---|---|---|
| Preparación de la oferta | Máxima | Casi nulo | Consultar, suponer, excluir, rediseñar, no ofertar |
| Diseño e implementac ión | Alta | Bajo a medio | Prototipar, probar integraciones, cambiar componentes |
| Implantación | Media | Alto | Desplegar por olas, volver atrás, reforzar soporte |
| Operación | Baja | Máximo | Pagar multas, absorber costos, renegociar |

> ⚠️ La paradoja del riesgo: hay que decidir cuando menos se sabe, porque es el único momento en que decidir todavía es barato. Por eso el trabajo de riesgos empieza leyendo las bases y no después de adjudicar.

Ésta es la razón por la que el curso exige el plan de riesgos dentro de la propuesta y no como un entregable posterior.

---

<a id="diapositiva-11"></a>

## Diapositiva 11 · Por qué fallan los proyectos TIC

La literatura de fracasos es notablemente estable en el tiempo. Casi ninguna causa es tecnológica, y casi todas son detectables antes de empezar a construir.

| Causa frecuente de fracaso | Cómo se ve en un proyecto TIC | Cuándo se decidió |
|---|---|---|
| Metas mal definidas o poco realistas | Se comprometió una fecha que nadie estimó | Al ofertar |
| Requisitos mal definidos | «Y todo lo necesario para su correcto funcionamiento» | Al leer las bases |
| Estimaciones inexactas de recursos | Se cotizó con horas de un perfil que no existe enla empresa | Al ofertar |
| Riesgos no gestionados | Se sabía del sistema legado y nadie hizo nada | Al ofertar |
| Tecnología inmadura | Se eligió un componente sin experiencia previa del equipo | Al ofertar |
| Comunicación pobre entre involucrados | El área usuaria se entera del proyecto en la capacitación | Al planificar |
| Reporte de estado deficiente | El avance se informa en porcentaje y nadie sabe qué mide | Al planificar |
| Incapacidad de manejar la complejidad | Cinco integraciones simultáneas sin dueño técnico | Al estimary diseñar |
| Relaciones políticas de los interesados | Dos direcciones del cliente quieren cosas incompatibles | Al levantar |
| Presión comercial | Se bajó el precio 20% sin sacar alcance | Al ofertar |

---

<a id="diapositiva-12"></a>

## Diapositiva 12 · Riesgo del proyecto, riesgo del producto y riesgo del negocio

Los tres aparecen en la misma propuesta y se responden en lugares distintos. Confundirlos hace que el plan de riesgos hable de lo que al cliente no le preocupa.

**Riesgo del proyecto**

Amenaza el plazo, el costo o el alcance de la construcción.

Ejemplo: la migración de datos toma el doble de lo estimado.

Se responde en el plan de trabajo y en la reserva.

**Riesgo del producto**

Amenaza que la solución funcione como se prometió.

Ejemplo: el trámite en línea no soporta el peak de pago de permisos de circulación en marzo.

Se responde en la arquitectura y en las pruebas.

**Riesgo del negocio**

Amenaza que el cliente obtenga el beneficio que buscaba.

Ejemplo: la plataforma funciona pero los usuarios van al mesón.

Se responde en la implantación y en la gestión del cambio.

> ⚠️ Una propuesta que sólo gestiona riesgos del proyecto le está diciendo al evaluador que le importa terminar, no que le importa servir. El tercero es el que se recuerda a los dos años.

---

<a id="diapositiva-13"></a>

## Diapositiva 13 · El caso que vamos a usar

Caso: La oferta ya está armada, con su alcance, su EDT, su cronograma y su precio. Hoy la vamos a mirar desde el riesgo.

| Dato | Valor |
|---|---|
| Mandante | Ilustre Municipalidad de Costa Azul (85.000 habitantes) |
| Oferente | Integra TIC SpA |
| Licitación | ID 3456-12-LP26 en Mercado Público |
| Objeto | Plataforma de trámites en línea, integración financiero-contable, ClaveÚnica y soporte |
| Presupuesto disponible | $ 320.000.000 IVA incluido |
| Plazo máximo de bases | 10 meses (unas 43 semanas) |
| Evaluación | Técnica 60% · Económica 30% · Experiencia 10% |
| Alcance ofertado | 8 trámites en etapa 1, de los 12 solicitados |
| Esfuerzo etapa 1 | 5.020 horas · tarifa $ 28.000/hora |
| Ruta crítica del cronograma | 34 semanas: A → B → D → G → I → K → L |
| Oferta presentada | $ 295.173.312 IVA incluido (92,2% del presupuesto) |
| Reserva de contingencia incluida | 8% de los costos directos = $ 12.684.800 |

---

<a id="diapositiva-14"></a>

## Diapositiva 14 · Recomendaciones para profundizar · Sección 1 · Qué es un riesgo

RECOMENDACIONES PARA PROFUNDIZAR

**Sección 1 · Qué es un riesgo**

**1**

**Leer el PMBOK**

Capítulo de Gestión de los Riesgos del Proyecto, en particular las definiciones de riesgo individual y riesgo general del proyecto. Fíjese en cuántas veces aparece la palabra «oportunidad».

**2**

**Revisar un fracaso real**

Busque el informe de una auditoría a un proyecto TIC público chileno. Identifique cuáles de las diez causas de fracaso de esta sección aparecen y en qué momento se decidieron.

**3**

**Fijar su escala**

Con su grupo, defina hoy la escala de probabilidad e impacto que van a usar todo el semestre. Escríbanla con umbrales numéricos y no la cambien después.

**4**

**Declarar su apetito**

Escriba en una frase cuánto está dispuesta a perder su empresa ficticia en este contrato. Esa frase decide después cuánta reserva van a cargar al precio.

**5**

**Releer sus bases**

Tome las bases de su caso y marque con lápiz cada frase que le produzca dudas. Todavía no las resuelva: sólo márquelas. Esa lista es su primer registro de riesgos.

---

<a id="diapositiva-15"></a>

## Diapositiva 15 · ▶ SECCIÓN 2 · El proceso de gestión de riesgos

**PROCESO**

**02**

SECCIÓN 2

**El proceso de gestión de riesgos**

- Los siete procesos del PMBOK y en qué orden se ejecutan
- El plan de gestión de riesgos: qué se decide antes de identificar el primer riesgo
- La estructura de desglose de riesgos (RBS) y una RBS propia para proyectos TIC
- El registro de riesgos y el informe de riesgos: dos documentos distintos
- Cómo se adapta el proceso al tamaño y a la complejidad del proyecto

---

<a id="diapositiva-16"></a>

## Diapositiva 16 · Los siete procesos de la gestión de riesgos

El PMBOK organiza la gestión del riesgo en siete procesos. Seis son de planificación y uno es de seguimiento, pero todos se repiten a lo largo del proyecto.

| # | Proceso | Qué produce | Grupo |
|---|---|---|---|
| 1 | Planificar la gestión de los riesgos | El plan de gestión de riesgos: método, escalas, roles, umbrales y financiamiento | Planificación |
| 2 | Identificar los riesgos | El registro de riesgos y el informe de riesgos | Planificación |
| 3 | Realizar el análisis cualitativo | Riesgos priorizados y categorizados por exposición | Planificación |
| 4 | Realizar el análisis cuantitativo | Efecto numérico sobre plazo y costo; riesgo general del proyecto | Planificación |
| 5 | Planificar la respuesta a los riesgos | Estrategias, acciones, dueños, costos, disparadores y reservas | Planificación |
| 6 | Implementar la respuesta a los riesgos | Las acciones efectivamente ejecutadas | Ejecución |
| 7 | Monitorear los riesgos | Riesgos reevaluados, nuevos riesgos, efectividad de las respuestas | Monitoreo y control |

> ⚠️ El proceso 4, análisis cuantitativo, es opcional según el PMBOK. En una licitación con precio fijo deja de ser opcional: sin él no hay forma de justificar la reserva que se va a cargar al cliente.

---

<a id="diapositiva-17"></a>

## Diapositiva 17 · El flujo completo, de la identificación al cierre

El proceso no es una lista que se recorre una vez: es un ciclo que se cierra sobre sí mismo cada vez que aparece información nueva.

**1**

**2**

**Planificar**

**Identificar**

Se fijan escalas, umbrales, roles, frecuencia y presupuesto.

Se lista qué puede pasar y por qué. Abre el registro de riesgos.

**4**

**5**

**Responder**

**Implementar**

Estrategia, acción, dueño, costo y fecha para lo significativo.

Se ejecutan las acciones: tienen horas en el cronograma.

**3**

**Analizar**

Cualitativo para priorizar y cuantitativo para poner número.

**6**

**Monitorear**

Se vigilan disparadores, se reevalúa y aparecen nuevos riesgos.

> ⚠️ El filtro está entre analizar y responder: un riesgo bajo umbral no recibe acción, recibe observación. Gastar en todos los riesgos es tan malo como no gastar en ninguno.

Los riesgos que quedan después de aplicar una respuesta se llaman riesgos residuales, y también se registran.

---

<a id="diapositiva-18"></a>

## Diapositiva 18 · El plan de gestión de riesgos: qué se decide antes de empezar

Antes de identificar el primer riesgo hay que decidir cómo se va a trabajar. Eso es el plan de gestión de riesgos, y es un entregable en sí mismo.

| Contenido del plan | Qué se define | Ejemplo del caso |
|---|---|---|
| Metodología | Enfoque, herramientas y fuentes de datos | Cualitativo para todos; cuantitativo por valor esperado para los de exposición alta y crítica |
| Roles y responsabilidades | Quién identifica, califica, decide y escala | El jefe de proyecto mantiene el registro; el gerente autoriza gastos sobre $ 3 millones |
| Financiamiento | De dónde sale la plata de acciones y reservas | Contingencia dentro del precio; reserva de gestión con cargo al margen de la empresa |
| Calendario | Cuándo y con qué frecuencia se ejecuta cada proceso | Revisión completa en cada hito; revisión rápida en el comité quincenal |
| Categorías | La RBS que se usará para clasificar y para no dejar huecos | RBS TIC de siete ramas, adaptada a proyectos de integración |
| Escalas y umbrales | Probabilidad, impacto y apetito al riesgo | Escala de cinco niveles; umbral de escalamiento en exposición 0,40 |
| Formatos de informe | Cómo se comunica el riesgo y a quién | Registro completo interno; extracto de diez riesgos en el informe mensual |
| Seguimiento | Cómo se auditan las respuestas | Auditoría de riesgos en cada cierre de etapa |

---

<a id="diapositiva-19"></a>

## Diapositiva 19 · La estructura de desglose de riesgos (RBS)

La RBS es a los riesgos lo que la EDT es al trabajo: una descomposición jerárquica que sirve para no dejar categorías sin revisar. También permite ver en qué rama se concentra la exposición.

**1 · Técnico**

Definición del alcance · Definición de requisitos · Estimaciones, supuestos y restricciones · Procesos técnicos · Tecnología · Interfaces técnicas

**2 · De gestión**

Dirección de proyectos · Dirección del programa · Gestión de las operaciones · Organización · Dotación de recursos · Comunicación

**3 · Comercial**

Términos y condiciones contractuales · Contratación interna · Proveedores y vendedores · Subcontratos · Estabilidad del cliente · Asociaciones

**4 · Externo**

Legislación · Tasas de cambio · Sitios e instalaciones · Ambiental y clima · Competencia · Normativo

Ejemplo de RBS genérica del PMBOK. Es un punto de partida: en un proyecto concreto conviene adaptarla, porque una rama vacía es tan informativa como una rama llena.

> ⚠️ Uso práctico: al terminar la identificación, cuente cuántos riesgos cayeron en cada rama. Una rama con cero riesgos casi nunca significa que no hay riesgo: significa que nadie miró ahí.

---

<a id="diapositiva-20"></a>

## Diapositiva 20 · Una RBS para proyectos TIC de integración

La RBS genérica sirve para cualquier industria. Ésta está construida para lo que ustedes van a ofertar: un sistema que se integra con lo que el cliente ya tiene y que lo usa gente que no lo pidió.

| Rama | Categorías de nivel 2 | Pregunta guía |
|---|---|---|
| 1 · Solución y tecnología | Requisitos · Arquitectura · Componentes de terceros · Rendimiento y capacidad · Seguridad · Datos y migración | ¿Qué parte de la solución nunca hemos construido antes? |
| 2 · Integración y legado | Interfaces · Documentación del sistema existente · Proveedor incumbente · Ambientes · Ventanas de corte | ¿De qué dependemos que no controlamos y que no es nuestro? |
| 3 · Operación del cliente | Disponibilidad de la contraparte · Calidad del dato · Continuidad · Ventanas de intervención · Infraestructura | ¿Qué de la operación real puede impedir que trabajemos? |
| 4 · Personas y adopción | Usuario final y adoptante crítico · Capacitación · Gestión del cambio · Terceros no contratados · Sindicatos y jefaturas | ¿Quién puede decidir no usar lo que entreguemos? |
| 5 · Contrato y licitación | Ambigüedad de las bases · Criterios de aceptación · Multas · Cambios de alcance · Propiedad intelectual · Garantías | ¿Qué firmamos que no sabemos cuánto cuesta? |
| 6 · Regulatorio y externo | Datos personales · Normativa sectorial · Auditorías y certificaciones · Tipo de cambio · Proveedor único | ¿Qué puede cambiar afuera y obligarnos a rehacer? |
| 7 · Empresa proveedora | Dotación y rotación · Competencias · Carga de otros proyectos · Flujo de caja · Subcontratistas | ¿Qué de nuestra propia empresa puede fallar? |

---

<a id="diapositiva-21"></a>

## Diapositiva 21 · El registro de riesgos: los campos que no pueden faltar

El registro de riesgos es el documento vivo de la gestión. Se abre en la identificación y se cierra con el proyecto. Cada proceso le agrega columnas.

| Campo | En qué proceso se llena | Por qué importa |
|---|---|---|
| Identificador y categoría RBS | Identificar | Permite citarlo en la propuesta y ver ramas vacías |
| Enunciado causa –riesgo –efecto | Identificar | Obliga a separar la causa, el riesgo y el efecto |
| Dueño del riesgo | Identificar | Un riesgo sin dueño no se vigila |
| Probabilidad e impacto | Análisis cualitativo | Define la prioridad y la zona de acción |
| Exposición y prioridad | Análisis cualitativo | Ordena dónde se gasta primero |
| Valor esperado y efecto en plazo | Análisis cuantitativo | Justifica el monto de la reserva |
| Estrategia de respuesta | Planificar la respuesta | Escalar, evitar, transferir, mitigar o aceptar |
| Acción concreta y su costo | Planificar la respuesta | Es lo que entra a la EDT y al presupuesto |
| Etapa en que actúa la acción | Planificar la respuesta | Propuesta, implementación, implantación u operación |
| Disparador y plan de contingencia | Planificar la respuesta | Dice cuándo activar el plan B |
| Riesgo residual y secundario | Planificar la respuesta | Lo que queda y lo que la respuesta creó |
| Estado y fecha de revisión | Monitorear | Distingue vigente, materializado y cerrado |

---

<a id="diapositiva-22"></a>

## Diapositiva 22 · Riesgo individual, variabilidad y ambigüedad

No toda la incertidumbre tiene forma de evento. Reconocer las tres fuentes evita el error de meterlo todo en el registro como si fueran riesgos.

**Evento incierto**

Algo que puede ocurrir o no.

Ejemplo: el proveedor del sistema legado no entrega la documentación de la interfaz.

Se trata con el registro de riesgos y con respuestas planificadas.

**Variabilidad**

Algo que va a ocurrir, pero no se sabe con qué magnitud.

Ejemplo: la productividad del equipo, el número de defectos, la cantidad de trámites que el municipio pedirá ajustar.

Se trata con estimación de tres valores y simulación.

**Ambigüedad**

Algo que no se entiende todavía.

Ejemplo: el requisito «integración con los sistemas municipales» sin decir cuáles.

Se trata con consultas, prototipos, juicio de expertos y desarrollo incremental.

> ⚠️ En una licitación la ambigüedad es la fuente dominante, y es la única que se puede reducir gratis: preguntando dentro del plazo de consultas.

---

<a id="diapositiva-23"></a>

## Diapositiva 23 · Cómo se adapta el proceso al proyecto

Cada proyecto es único y el esfuerzo dedicado a la gestión del riesgo debe ser proporcional. Cuatro variables deciden cuánto proceso corresponde.

| Variable | Proceso reducido si… | Proceso detallado si… |
|---|---|---|
| Tamaño | Presupuesto y plazo pequeños, equipo de pocas personas, un solo entregable | Contrato de cientos de millones, plazo de varios trimestres, equipo multidisciplinario |
| Complejidad | Tecnología conocida, sin integraciones, un solo interesado | Innovación, tecnologías nuevas, dependencias externas, muchas integraciones |
| Importancia estratégica | Proyecto rutinario, con precedentes internos | Proyecto que abre un mercado, que expone la marca o que es la referencia comercial |
| Enfoque de desarrollo | Cascada con alcance estable: los procesos se recorren en orden | Iterativo: el riesgo se revisa al comienzo de cada iteración y durante la ejecución |

> ⚠️ El caso del curso está en la columna derecha en las cuatro filas: contrato grande, integraciones múltiples, primera referencia de la empresa ficticia y alcance que se detalla por etapas. Corresponde proceso detallado.

La decisión de cuánto proceso aplicar se escribe en el plan de gestión de riesgos y se justifica. No se deja implícita.

---

<a id="diapositiva-24"></a>

## Diapositiva 24 · Dónde vive el riesgo en el resto del plan del proyecto

La gestión de riesgos no es un capítulo aislado: deja rastro en casi todas las otras áreas del plan. Ese rastro es la evidencia de que existió.

| Área del plan | Qué deja el riesgo ahí | Cómo se ve en la propuesta |
|---|---|---|
| Alcance | Exclusiones explícitas y decisiones de acotar o de dividir en etapas | Enunciado del alcance y lista de exclusiones |
| Requisitos | Requisitos no funcionales nacidos de un riesgo | Matriz de requisitos con la columna de origen |
| Arquitectura | Componentes y patrones elegidos para eliminar un riesgo | Diagramas y decisiones de arquitectura registradas |
| Cronograma | Actividades de mitigación y holguras deliberadas | EDT, red de actividades y ruta crítica |
| Costos | Costo de las acciones y reserva de contingencia | Oferta económica, línea de reserva |
| Calidad | Pruebas, criterios de aceptación y auditorías | Plan de calidad y criterios de recepción conforme |
| Adquisiciones | Riesgos transferidos por contrato o por seguro | Contratos con subcontratistas y garantías |
| Interesados | Riesgos de adopción y de resistencia | Plan de gestión del cambio y de comunicaciones |
| Recursos | Rotación, competencias escasas y reemplazos | Organigrama del proyecto y currículos con respaldo |

---

<a id="diapositiva-25"></a>

## Diapositiva 25 · Cuándo se repite cada proceso

Los riesgos siguen apareciendo durante toda la vida del proyecto. Los procesos se ejecutan de manera iterativa, con distinta frecuencia cada uno.

| Momento | Qué procesos se ejecutan | Producto |
|---|---|---|
| Al preparar la oferta | Los seis de planificación, completos | Plan de riesgos y registro inicial que forman parte de la propuesta |
| Al iniciar el contrato | Identificar y analizar de nuevo, con la información que el cliente entrega recién ahora | Registro revisado y línea base acordada con el mandante |
| En cada comité quincenal | Monitorear: estado, disparadores y riesgos nuevos | Registro actualizado y acciones abiertas |
| En cada cierre de etapa | Los siete, completos: la etapa siguiente tiene riesgos propios | Informe de riesgos y ajuste de la reserva remanente |
| Ante un cambio de alcance | Identificar, analizar y responder sobre el cambio | Riesgos asociados a la solicitud de cambio, valorizados |
| Al cerrar el proyecto | Monitorear por última vez y documentar | Lecciones aprendidas y activos para el próximo proyecto |

> ⚠️ La reserva no se gasta sola: cada vez que un riesgo se cierra sin materializarse, esa parte de la reserva se libera y mejora el margen. Eso también se informa.

---

<a id="diapositiva-26"></a>

## Diapositiva 26 · Recomendaciones para profundizar · Sección 2 · El proceso de gestión de riesgos

RECOMENDACIONES PARA PROFUNDIZAR

**Sección 2 · El proceso de gestión de riesgos**

**1**

**Leer los siete procesos**

PMBOK, entradas, herramientas y salidas de cada uno de los siete procesos de riesgo. Fíjese en qué documentos entran y salen: casi todos son el registro de riesgos en distinto estado de llenado.

**2**

**Escribir su plan**

Redacte el plan de gestión de riesgos de su grupo en una página, con las ocho secciones de esta clase. Es el documento que hace que el resto del trabajo sea rápido.

**3**

**Adaptar la RBS**

Tome la RBS TIC de siete ramas y quítele o agréguele lo que corresponda a su industria. Una RBS de portuaria no es la misma que una de salud.

**4**

**Abrir el registro**

Cree hoy la planilla del registro de riesgos con las doce columnas. Ábrala aunque todavía no tenga riesgos: el formato guía la identificación.

**5**

**Buscar el informe**

Busque en internet un informe de riesgos real de un proyecto público. Compare cuánto habla de riesgos individuales y cuánto del riesgo general del proyecto.

---

<a id="diapositiva-27"></a>

## Diapositiva 27 · ▶ SECCIÓN 3 · Identificar los riesgos

**IDENTIFICAR**

**03**

SECCIÓN 3

**Identificar los riesgos**

- Quién identifica, cuándo y con qué técnicas
- Supuestos y restricciones: la fábrica de riesgos de toda propuesta
- Lectura adversarial de las bases: qué frases producen riesgo
- Un catálogo de riesgos propio de los proyectos TIC de integración
- Cómo se escribe un riesgo para que sirva: causa, riesgo y efecto

---

<a id="diapositiva-28"></a>

## Diapositiva 28 · Qué significa identificar bien

Identificar es determinar qué riesgos pueden afectar al proyecto y documentar sus características. Suena simple y es donde se pierde la mitad del valor de la gestión.

| Dimensión | Práctica pobre | Práctica que se evalúa bien |
|---|---|---|
| Quién participa | Dos personas del equipo técnico | Todo el equipo, más el comercial, más alguien que haya hecho un proyecto parecido |
| Cuándo se hace | Al final, cuando la propuesta ya está escrita | Al leer las bases, antes de definir el alcance y la arquitectura |
| Con qué se hace | De memoria | Con las bases, con la RBS, con listas de verificación y con lecciones aprendidas |
| Cuánto se busca | Hasta llenar la tabla | Hasta que dos vueltas seguidas no aportan riesgos nuevos |
| Cómo se escribe | «Retraso en el cronograma» | «Dado que… entonces puede que… teniendo como consecuencia…» |
| Qué se hace después | Se archiva | Se prioriza, se responde y se cambia la propuesta |

> ⚠️ Criterio de término: la identificación se cierra cuando dos rondas consecutivas, hechas con técnicas distintas, no agregan ningún riesgo nuevo. No cuando se acabó el tiempo.

---

<a id="diapositiva-29"></a>

## Diapositiva 29 · Técnicas para recopilar riesgos

**Listas de verificación**

Recorrer un catálogo conocido de riesgos de la industria. Es la técnica más rápida y la que más riesgos produce por minuto. Su límite: no encuentra lo que no está en la lista.

**Tormenta de ideas**

Sesión abierta con el equipo, guiada por la RBS rama por rama. Sirve para lo específico de este cliente. Requiere moderación: sin ella se convierte en una discusión técnica.

**Entrevistas**

Conversación individual con quien conoce el terreno: el jefe de proyecto de un contrato parecido, el vendedor, el arquitecto. Se obtiene lo que nadie dice en grupo.

**Juicio de expertos**

Consultar a alguien con experiencia comprobada en esa tecnología, ese cliente o esa industria. La forma estructurada y anónima de hacerlo se llama técnica Delphi.

Ninguna técnica basta sola. La combinación mínima razonable para una propuesta es: lista de verificación por RBS, luego una sesión de equipo de noventa minutos, luego una entrevista con alguien externo al equipo.

> ⚠️ La fuente más barata y más ignorada es el histórico de la propia empresa: los informes de cierre de los proyectos anteriores contienen los riesgos que efectivamente se materializaron.

En el curso, el equivalente son las actas de respuestas a consultas de licitaciones anteriores del mismo mandante, que son públicas.

---

<a id="diapositiva-30"></a>

## Diapositiva 30 · Técnicas de análisis para descubrir riesgos que nadie mencionó

| Técnica | En qué consiste | Qué encuentra que las otras no encuentran |
|---|---|---|
| Análisis de causa raíz | Partir de un efecto indeseado conocido y remontar hasta las causas que lo producirían | Riesgos distintos que comparten una misma causa, y por lo tanto una misma respuesta |
| Análisis de supuestos y restricciones | Listar todo lo que se está dando por cierto sin evidencia, y probar qué pasa si es falso | Los riesgos que el equipo no ve porque ya los aceptó como verdad |
| Análisis FODA | Revisar fortalezas, oportunidades, debilidades y amenazas de la propia empresa frente a este contrato | Riesgos internos del proveedor: capacidad, competencias, carga de otros proyectos |
| Análisis de documentos | Revisión estructurada de bases, anexos, actas de consultas, contratos anteriores y documentación técnica del cliente | Contradicciones entre documentos y requisitos escondidos en anexos |
| Listas rápidas de disparadores | Preguntas cortas y provocadoras: ¿qué pasa si el cliente cambia de jefatura? ¿si el proveedor actual no coopera? | Riesgos organizacionales y políticos que no aparecen en ninguna lista técnica |

> ⚠️ El análisis de documentos es obligatorio en una licitación: la contradicción entre las bases administrativas y las técnicas es una de las fuentes de riesgo más frecuentes y más fáciles de encontrar.

---

<a id="diapositiva-31"></a>

## Diapositiva 31 · Supuestos y restricciones: la fábrica de riesgos de toda propuesta

Un supuesto es algo que se da por cierto sin haberlo verificado. Toda propuesta está llena de ellos, y cada uno es un riesgo que ya está escrito: sólo hay que darlo vuelta.

| Supuesto declarado en la propuesta | El riesgo que contiene | Efecto si el supuesto es falso |
|---|---|---|
| El sistema financiero-contable expone servicios documentados | Que no los exponga y haya que construir una capa intermedia | 6 semanas y unas 400 horas de desarrollo no previstas |
| La habilitación de ClaveÚnica demora ocho semanas | Que el trámite institucional demore el doble | Un hito contractual que no se puede cerrar a tiempo |
| El municipio entregará los datos con una calidad razonable | Que los datos tengan duplicados, campos vacíos y códigos inconsistentes | Saneamiento no cotizado y una migración que se debe repetir |
| La contraparte validará cada entregable en cinco días hábiles | Que la validación demore semanas por vacaciones o cambio de jefatura | Atraso en cadena de todo el cronograma |
| Los doce trámites tienen un flujo similar | Que cada dirección municipal exija variantes propias | Multiplicación del esfuerzo del motor de formularios |
| La infraestructura del cliente soporta la solución | Que haya que dimensionar y comprar infraestructura adicional | Costo de inversión no considerado en la oferta |

> ⚠️ Regla mecánica: por cada supuesto de su propuesta, escriba el riesgo de que sea falso. Si no está dispuesto a escribir ese riesgo, es que el supuesto no era un supuesto: era una esperanza.

---

<a id="diapositiva-32"></a>

## Diapositiva 32 · Lectura adversarial: qué frases de las bases producen riesgo

Hay expresiones que aparecen en casi todas las bases y que siempre significan lo mismo: costo indeterminado. Reconocerlas es la mitad de la identificación de riesgos de una licitación.

| Frase típica de las bases | Lo que realmente dice | Qué hacer con ella |
|---|---|---|
| «…y todo lo necesario para su correcto funcionamiento» | El alcance no tiene borde: cualquier cosa cabe adentro | Consultar el límite y declarar exclusiones explícitas |
| «…se integrará con los sistemas del mandante» | No dice cuáles, ni cuántos, ni con qué tecnología | Consultar el listado exacto y suponer un número máximo |
| «…según requiera la contraparte técnica» | El costo lo define alguien que no firma el contrato | Pedir criterio objetivo o acotar por cantidad |
| «…a satisfacción del mandante» | El criterio de recepción es subjetivo | Proponer criterios de aceptación medibles en la propuesta |
| «…considerar la migración de la información histórica» | Sin volumen, sin años, sin calidad y sin formato | Consultar volumen y calidad; suponer un límite |
| «…deberá garantizar disponibilidad permanente» | Puede ser 99% o 99,99%: hay dos órdenes de magnitud de costo entre medio | Consultar el nivel exigido y ofertar contra ese número |
| «…capacitación a los usuarios» | No dice cuántos, dónde, en cuántas sesiones ni cuándo | Suponer cantidad, modalidad y sesiones, y dejarlo escrito |
| «…el plazo se contará desde la firma del contrato» | El proveedor no controla cuándo firma el cliente | Consultar plazos administrativos y declarar hitos condicionados |

---

<a id="diapositiva-33"></a>

## Diapositiva 33 · Catálogo de riesgos TIC · Solución, tecnología e integración

**1 · Solución y tecnología**

- Requisitos ambiguos o que aparecen recién en la construcción
- Componente de terceros con licencia o certificación no prevista
- Rendimiento insuficiente en el peak real de la operación
- Volumen de datos muy superior al declarado en las bases
- Requisito de seguridad tardío: cifrado, auditoría, doble factor
- Tecnología que el equipo nunca ha usado en producción
- Deuda técnica heredada de un componente que se reutiliza

**2 · Integración y sistema legado**

- El sistema existente no expone interfaz, o no la documenta
- El proveedor incumbente no coopera o cobra por cada consulta
- No existe ambiente de pruebas del lado del cliente
- La interfaz existe pero su rendimiento no soporta el volumen
- Cambio de versión del sistema del cliente durante el proyecto
- Ventana de corte para el cambio de sistema muy estrecha
- Dependencia de un servicio externo cuyo contrato vence antes

Cada línea de este catálogo se convierte en riesgo sólo cuando se escribe con la causa concreta de su caso. Copiado tal cual, es una lista genérica y se evalúa como tal.

---

<a id="diapositiva-34"></a>

## Diapositiva 34 · Catálogo de riesgos TIC · Operación del cliente y adopción

**3 · Operación del cliente**

- La contraparte no valida en los plazos supuestos
- Cambio de autoridad o de jefatura en el proyecto
- Calidad del dato peor que la declarada en las bases
- Ventanas de intervención acotadas por la temporada
- No se puede detener el servicio para migrar
- Infraestructura o conectividad del cliente insuficiente
- Área de tecnología del cliente sin dotación

**4 · Personas y adopción**

- El usuario final no participó en el diseño
- La interfaz ignora las condiciones reales de uso
- Alta rotación del personal ya capacitado
- Terceros que deben usarlo y no son empleados
- Resistencia por pérdida de control o de poder
- Capacitación demasiado lejos de la puesta en marcha
- Exige registrar lo que antes nadie registraba

> ⚠️ Regla práctica: si su solución exige que alguien registre algo que hoy no registra, tiene un riesgo de adopción de primera magnitud, aunque el software sea impecable.

---

<a id="diapositiva-35"></a>

## Diapositiva 35 · Catálogo de riesgos TIC · Contrato, entorno y empresa proveedora

**5 · Contrato y licitación**

Alcance abierto y sin borde · Criterios de recepción subjetivos · Multas sin tope · Mecanismo de cambios inexistente · Propiedad intelectual del código · Garantías mal constituidas · Plazo que corre desde un hecho que no se controla

**6 · Regulatorio y entorno**

Datos personales y Ley 21.719 · Normativa sectorial que cambia · Auditorías y certificaciones no anunciadas · Licencias en dólares y tipo de cambio · Proveedor único de un componente crítico · Accesibilidad y estándares de gobierno digital

**7 · Empresa proveedora**

Rotación del perfil clave · Competencia que no se tiene y hay que contratar · Sobrecarga por otros contratos simultáneos · Flujo de caja frente a pagos contra hito · Subcontratista que no responde · Optimismo en la estimación original

Estas tres ramas casi nunca aparecen en los planes de riesgo de los alumnos, y son exactamente las que hacen perder plata en un contrato real. La rama 5 se identifica leyendo; la 6, investigando; la 7, mirándose hacia adentro.

La Ley N° 21.719 de protección de datos personales entra en plena vigencia el 1 de diciembre de 2026: cae dentro del horizonte de ejecución de cualquier proyecto que se formule este semestre.

---

<a id="diapositiva-36"></a>

## Diapositiva 36 · Cómo se escribe un riesgo para que sirva

Un riesgo mal escrito no se puede analizar ni responder. La estructura estándar obliga a separar la causa, el evento incierto y el efecto.

Dado que <causa: hecho o condición cierta> entonces puede que <riesgo: evento incierto> teniendo como consecuencia <efecto sobre un objetivo>

**Causa**

Un hecho o condición que ya es cierto hoy. No tiene probabilidad: es verdad. Es el terreno donde el riesgo puede crecer.

**Riesgo**

El evento incierto. Es lo único que lleva probabilidad. Se escribe con «puede que» y en futuro.

**Efecto**

La consecuencia sobre un objetivo del proyecto, dicha en la unidad del objetivo: días, pesos, funciones, disponibilidad.

> ⚠️ Prueba rápida: si al leer su riesgo no queda claro sobre qué objetivo pega, no está terminado. «Afecta al proyecto» no es un efecto: es un relleno.

Error frecuente: escribir la causa en el lugar del riesgo. «El equipo no tiene experiencia en la tecnología» es una causa, no un riesgo.

---

<a id="diapositiva-37"></a>

## Diapositiva 37 · Ejemplos: así no, así sí

| Así no se escribe | Por qué no sirve | Así sí se escribe |
|---|---|---|
| Retraso en el cronograma | Es un efecto, no un riesgo. No dice qué lo produce ni cuánto | Dado que la habilitación de ClaveÚnica depende de un trámite institucional que no controlamos, entonces puede que la credencial productiva llegue después de la semana 12, teniendo como consecuencia el atraso del hito de autenticación en hasta 4 semanas |
| Cambios de alcance | Es una categoría, no un evento. Cabe cualquier cosa adentro | Dado que las bases piden 12 trámites sin definir sus flujos, entonces puede que cada dirección exija variantes propias, teniendo como consecuencia hasta 300 horas adicionales en el motor de formularios |
| Falta de compromiso del cliente | Es un juicio, no un evento observable ni medible | Dado que la contraparte técnica es una sola persona con otras funciones, entonces puede que las validaciones excedan los 5 días hábiles supuestos, teniendo como consecuencia atraso en cadena de la ruta crítica |
| Problemas de integración | No dice con qué sistema, ni qué problema, ni qué cuesta | Dado que el sistema financiero-contable es una versión de 2011 sin documentación de interfaces, entonces puede que no exponga servicios utilizables, teniendo como consecuencia el desarrollo de una capa intermedia de unas 400 horas |

> ⚠️ La columna de la derecha es más larga, y ésa es exactamente la diferencia: contiene el sistema concreto, el número de semanas, la cantidad de horas y el objetivo afectado. Con eso se puede calificar, cuantificar y responder; con la columna izquierda no se puede hacer nada.

---

<a id="diapositiva-38"></a>

## Diapositiva 38 · Errores frecuentes en la identificación

| Error | Cómo se reconoce | Cómo se corrige |
|---|---|---|
| Confundir riesgo con problema | El verbo está en pasado | Sacarlo del registro: es una acción correctiva |
| Confundir riesgo con causa | Describe una condición actual, no un evento | Ponerlo en el «dado que» y buscar el evento |
| Confundir riesgo con efecto | Dice «atraso», «sobrecosto», «mala calidad» | Preguntarse qué evento produciría ese efecto |
| Riesgos genéricos | Servirían para cualquier proyecto del mundo | Agregar el dato concreto: sistema, número, fecha |
| Riesgos sin dueño | Nadie es responsable de vigilarlo | Asignar una persona, no un área |
| Sólo amenazas | Cero oportunidades en todo el registro | Recorrer la RBS buscando qué puede salir mejor |
| Todo en una sola rama | Quince riesgos técnicos y ninguno de personas | Revisar la RBS rama por rama, sin saltarse ninguna |
| Riesgos que nadie va a responder | Cuarenta filas y ninguna acción asociada | Menos riesgos, mejor escritos y con respuesta |

> ⚠️ Un registro de doce riesgos bien escritos y respondidos vale más que uno de cuarenta genéricos. El evaluador cuenta acciones, no filas.

---

<a id="diapositiva-39"></a>

## Diapositiva 39 · El resultado de la identificación en el caso

Tras la lectura de las bases, una sesión de equipo y una entrevista con el arquitecto, el registro de Integra TIC SpA quedó con diez riesgos significativos.

| ID | Título del Riesgo identificado | Rama de la RBS |
|---|---|---|
| R-01 | El sistema financiero-contable no expone una interfaz documentada | 2 · Integración y legado |
| R-02 | La habilitación de ClaveÚnica demora más que las 8 semanas supuestas | 2 · Integración y legado |
| R-03 | Los 12 trámites no están normalizados y cada dirección pide variantes | 1 · Solución y tecnología |
| R-04 | Los datos a migrar tienen peor calidad que la declarada en las bases | 3 · Operación del cliente |
| R-05 | Rotación del arquitecto o del integrador durante el proyecto | 7 · Empresa proveedora |
| R-06 | La contraparte municipal no está disponible para validar en plazo | 3 · Operación del cliente |
| R-07 | La Ley 21.719 exige controles de datos personales no previstos | 6 · Regulatorio y entorno |
| R-08 | La pasarela de pago cambia su esquema de certificación o comisiones | 2 · Integración y legado |
| R-09 | Los funcionarios rechazan la marcha blanca y vuelven al mesón | 4 · Personas y adopción |
| R-10 | Observaciones de la prueba de intrusión obligan a retrabajo | 1 · Solución y tecnología |

La RBS se recorrió rama por rama. Los de la rama 5, contrato y licitación, se registran aparte y se tratan completos en la sección 6.

---

<a id="diapositiva-40"></a>

## Diapositiva 40 · Recomendaciones para profundizar · Sección 3 · Identificar los riesgos

RECOMENDACIONES PARA PROFUNDIZAR

**Sección 3 · Identificar los riesgos**

**1**

**Hacer la sesión completa**

Reserve noventa minutos con todo el grupo, con las bases impresas y la RBS al lado. No se detenga a discutir cada riesgo: primero listar, después depurar.

**2**

**Cazar las frases**

Busque en sus bases las ocho frases de riesgo de esta sección. Anote la página exacta: la va a necesitar para redactar la consulta formal.

**3**

**Invertir los supuestos**

Escriba los diez supuestos de su propuesta y, al lado, el riesgo de que cada uno sea falso. Es el ejercicio que más riesgos produce por minuto.

**4**

**Reescribir con la fórmula**

Tome sus cinco riesgos peor escritos y páselos a «dado que… entonces puede que… teniendo como consecuencia…». Verá que dos de ellos eran el mismo.

**5**

**Entrevistar a alguien**

Converse con alguien que haya trabajado en la industria de su caso. Una sola conversación de treinta minutos suele producir dos riesgos que ninguna lista contiene.

**6**

**Buscar oportunidades**

Recorra la RBS por segunda vez preguntando qué podría salir mejor de lo previsto. Necesita al menos dos oportunidades en su registro.

---

<a id="diapositiva-41"></a>

## Diapositiva 41 · ▶ SECCIÓN 4 · Analizar los riesgos

**ANALIZAR**

**04**

SECCIÓN 4

**Analizar los riesgos**

- Análisis cualitativo: priorizar sin números y por qué eso ya es mucho
- Análisis cuantitativo: valor monetario esperado y árbol de decisión
- De la suma de valores esperados a la reserva de contingencia del precio
- Estimación de tres valores y lectura de la curva de probabilidad del plazo
- Análisis de sensibilidad: dónde conviene concentrar la gestión

---

<a id="diapositiva-42"></a>

## Diapositiva 42 · Dos análisis distintos, con propósitos distintos

**Análisis cualitativo**

- Objetivo: priorizar. Ordenar los riesgos por importancia relativa
- Se aplica a todos los riesgos del registro
- Usa la escala de cinco niveles con umbrales definidos
- Es rápido: un registro de veinte riesgos se califica en una hora
- Su salida es una lista ordenada y una matriz de exposición
- Su límite: no dice cuánta plata hay que reservar

**Análisis cuantitativo**

- Objetivo: dimensionar. Poner número al plazo y al costo
- Se aplica sólo a los riesgos priorizados en el cualitativo
- Usa probabilidad en porcentaje e impacto en pesos o días
- Es caro: exige estimar cada impacto con fundamento
- Su salida es el valor esperado, la reserva y el plazo a comprometer
- Su límite: el número vale lo que valga el supuesto

> ⚠️ El cualitativo decide dónde mirar. El cuantitativo decide cuánto pagar. Una propuesta con precio fijo necesita los dos, y en ese orden.

---

<a id="diapositiva-43"></a>

## Diapositiva 43 · Qué se evalúa en el análisis cualitativo

Probabilidad e impacto son lo mínimo. Hay cinco atributos más que ayudan a decidir cuál de dos riesgos con la misma exposición se atiende primero.

| Atributo | Pregunta que responde | Para qué sirve en la propuesta |
|---|---|---|
| Probabilidad | ¿Qué tan posible es que ocurra? | Calificar y calcular el valor esperado |
| Impacto | ¿Cuánto duele y sobre qué objetivo? | Dimensionar la reserva y la acción |
| Urgencia | ¿En cuánto tiempo hay que responder? | Decidir qué acciones van en la propuesta y cuáles después |
| Proximidad | ¿Cuándo puede materializarse? | Ubicar la acción en el cronograma, no antes ni después |
| Controlabilidad | ¿Depende de nosotros o de un tercero? | Elegir entre mitigar, transferir o escalar |
| Detectabilidad | ¿Nos daremos cuenta a tiempo? | Definir el evento de disparo y el indicador que lo vigila |
| Conectividad | ¿Este riesgo dispara otros? | Encontrar la causa común y responder una sola vez |

> ⚠️ Un riesgo de baja detectabilidad se comporta como uno de impacto mayor: cuando se nota, ya es un problema. En integraciones, la baja detectabilidad es la regla.

---

<a id="diapositiva-44"></a>

## Diapositiva 44 · La matriz de exposición aplicada al caso

Con la escala definida en la sección 1 y el registro de diez riesgos, la calificación cualitativa reparte el trabajo en tres grupos.

| Grupo | Riesgos | Exposición | Qué se hace con ellos |
|---|---|---|---|
| Atención prioritaria | R-01 · R-03 · R-04 | 0,20 a 0,30 | Mitigación con costo y plazo en el plan |
| Gestión activa | R-02 · R-06 · R-07 | 0,14 a 0,18 | Aceptación activa con reserva y disparador |
| Observación | R-05 · R-08 · R-09 · R-10 | 0,04 a 0,07 | Revisión mensual, sin acción ni costo |

La lectura por rama de la RBS es igual de útil: siete de los diez riesgos, y el 82% de la exposición, están en las ramas 1, 2 y 3, es decir en la solución, la integración y la operación del cliente. Eso ya dice dónde debe reforzarse la arquitectura y dónde el plan de trabajo.

> ⚠️ La matriz no sirve para pintar colores: sirve para decidir a qué riesgos se les va a dedicar horas y plata, y a cuáles solamente atención. Esa decisión hay que poder defenderla.

Los tres grupos se corresponden con las zonas de acción declaradas en el plan de gestión de riesgos. La correspondencia debe ser explícita: si no, la matriz parece arbitraria.

---

<a id="diapositiva-45"></a>

## Diapositiva 45 · Cuándo vale la pena el análisis cuantitativo

El análisis cuantitativo cuesta tiempo y exige estimar impactos con fundamento. No siempre se justifica. Estas cinco condiciones dicen cuándo sí.

**Precio fijo**

El proveedor absorbe la desviación. Sin número, la reserva es una apuesta.

**Monto relevante**

El contrato pesa en el resultado del año de la empresa proveedora.

**Plazo comprometido**

Hay multas por atraso y hay que decidir qué fecha prometer.

**Integraciones**

Hay dependencias de terceros que no se controlan.

**Hay que justificar**

El evaluador va a preguntar de dónde salió la reserva del precio.

Las técnicas principales son tres, y se usan para cosas distintas: el valor monetario esperado dimensiona la reserva de costo; el árbol de decisión compara alternativas de solución; la estimación de tres valores y la simulación dimensionan el plazo que conviene comprometer.

> ⚠️ Ninguna de las tres exige software especial. Las tres se hacen en una planilla y caben en media página de la propuesta.

---

<a id="diapositiva-46"></a>

## Diapositiva 46 · Valor monetario esperado: la fórmula y su lectura correcta

**Valor monetario esperado = Probabilidad × Impacto**

Ejemplo: el riesgo R-01, que el sistema financiero-contable no exponga una interfaz utilizable, tiene probabilidad estimada de 50% e impacto de $ 6.400.000. Su valor esperado es $ 3.200.000.

**Qué sí significa**

Es la cantidad que habría que reservar, en promedio, si este mismo proyecto se ejecutara muchas veces. Es la base objetiva para dimensionar la reserva de contingencia del conjunto.

**Qué no significa**

No significa que este riesgo vaya a costar 3,2 millones. Va a costar 6,4 millones o cero. El valor esperado no ocurre nunca en un caso individual.

**Por qué sirve igual**

Porque los riesgos se suman. Sobre diez riesgos independientes, la suma de los valores esperados es una estimación razonable del costo total de la incertidumbre.

> ⚠️ Los impactos positivos entran con signo positivo. Una oportunidad de 40% de ahorrar 5 millones aporta un valor esperado de 2 millones que reduce la reserva total.

---

<a id="diapositiva-47"></a>

## Diapositiva 47 · El registro cuantificado del caso

| ID | Riesgo | Prob. | Impacto | Valor esperado |
|---|---|---|---|---|
| R-01 | El sistema financiero-contable no expone una interfaz documentada | 50% | $ 6.400.000 | $ 3.200.000 |
| R-02 | La habilitación de ClaveÚnica demora más que las 8 semanas supuestas | 40% | $ 3.500.000 | $ 1.400.000 |
| R-03 | Los 12 trámites no están normalizados y cada dirección pide variantes | 50% | $ 4.200.000 | $ 2.100.000 |
| R-04 | Los datos a migrar tienen peor calidad que la declarada en las bases | 45% | $ 3.600.000 | $ 1.620.000 |
| R-05 | Rotación del arquitecto o del integrador durante el proyecto | 30% | $ 3.000.000 | $ 900.000 |
| R-06 | La contraparte municipal no está disponible para validar en plazo | 50% | $ 2.400.000 | $ 1.200.000 |
| R-07 | La Ley 21.719 exige controles de datos personales no previstos | 35% | $ 2.800.000 | $ 980.000 |
| R-08 | La pasarela de pago cambia su esquema de certificación o comisiones | 25% | $ 2.000.000 | $ 500.000 |
| R-09 | Los funcionarios rechazan la marcha blanca y vuelven al mesón | 20% | $ 1.800.000 | $ 360.000 |
| R-10 | Observaciones de la prueba de intrusión obligan a retrabajo | 30% | $ 1.400.000 | $ 420.000 |
|  | TOTAL |  | $ 31.100.000 | $ 12.680.000 |

> ⚠️ Si todos los riesgos se materializaran, el sobrecosto sería $ 31.100.000. Eso no va a pasar. El valor esperado del conjunto es $ 12.680.000, y ésa es la cifra que se lleva al precio.

---

<a id="diapositiva-48"></a>

## Diapositiva 48 · De la suma de valores esperados a la reserva del precio

| Paso | Cálculo | Resultado |
|---|---|---|
| 1. Suma de valores esperados del registro | Diez riesgos cuantificados | $ 12.680.000 |
| 2. Costos directos de la etapa 1 | Servicios profesionales, licencias e infraestructura | $ 158.560.000 |
| 3. Reserva necesaria como porcentaje | $ 12.680.000 ÷ $ 158.560.000 | 8,0% |
| 4. Reserva declarada | 8% de los costos directos | $ 12.684.800 |
| 5. Holgura sobre el valor esperado | $ 12.684.800 − $ 12.680.000 | $ 4.800 |

La reserva de contingencia forma parte de la línea base de costos y se declara como una línea propia de la oferta económica. No se esconde dentro de las horas: esconderla impide defenderla y hace que se gaste sin control.

> ⚠️ Redacción tipo para la propuesta: «La reserva de contingencia de $ 12.684.800 corresponde al 8% de los costos directos y cubre el valor esperado de los diez riesgos cuantificados en el anexo de gestión de riesgos, que asciende a $ 12.680.000».

Un evaluador exigente pide exactamente esa trazabilidad. Un porcentaje sin tabla detrás se lee como un colchón, y los colchones se descuentan en la evaluación económica.

---

<a id="diapositiva-49"></a>

## Diapositiva 49 · Reserva de contingencia y reserva de gestión

**Reserva de contingencia**

- Cubre riesgos identificados y cuantificados
- Forma parte de la línea base de costos
- Su monto sale del valor esperado del registro
- La usa el jefe de proyecto, con el riesgo declarado
- Se libera cuando el riesgo se cierra sin ocurrir
- En el caso: $ 12.684.800

**Reserva de gestión**

- Cubre riesgos no identificados: lo que no se vio venir
- No forma parte de la línea base, sí del presupuesto total

- Su monto sale de la experiencia histórica de la empresa
- La libera la gerencia, no el jefe de proyecto
- Usarla exige actualizar la línea base
- En el caso: la absorbe el margen de la empresa oferente

Presupuesto total = línea base de costos + reserva de gestión. Línea base de costos = costos estimados de los paquetes de trabajo + reserva de contingencia. El orden importa porque el control del proyecto se mide contra la línea base, no contra el presupuesto total.

En una licitación de precio fijo la reserva de gestión rara vez se declara al cliente: se financia con el margen. La de contingencia sí se declara, porque es la que sostiene el precio.

---

<a id="diapositiva-50"></a>

## Diapositiva 50 · Árbol de decisión: comparar alternativas de solución

Frente al riesgo R-01, la integración con el sistema financiero-contable, hay dos alternativas de solución. El árbol de decisión permite compararlas incluyendo el costo del riesgo.

| Alternativa | Costo cierto | Riesgo asociado | Si ocurre | Esperado |
|---|---|---|---|---|
| A · Desarrollo a medida | $ 6.000.000 | 50% de que no haya servicios útiles | $ 6.400.000 | $ 9.200.000 |
| B · Conector comercial con soporte | $ 11.000.000 | 10% de que igual haya que adaptarlo | $ 3.000.000 | $ 11.300.000 |

Alternativa A: $ 6.000.000 + 0,50 × $ 6.400.000 = $ 9.200.000 Alternativa B: $ 11.000.000 + 0,10 × $ 3.000.000 = $ 11.300.000

> ⚠️ Con estos números conviene desarrollar a medida: cuesta $ 2.100.000 menos en valor esperado. Pero la conclusión depende por completo del 50%, y ese 50% es una estimación, no un dato.

El árbol de decisión es la técnica que más directamente cambia la arquitectura ofertada. Su resultado se registra como decisión de diseño y se cita en el capítulo de arquitectura de la propuesta.

---

<a id="diapositiva-51"></a>

## Diapositiva 51 · El punto de indiferencia: hasta dónde aguanta la decisión

Una decisión tomada con una probabilidad estimada debe venir acompañada de la pregunta obvia: ¿cuánto tendría que equivocarme para que la decisión cambie?

**$ 6.000.000 + p × $ 6.400.000 = $ 11.300.000**

**→**

**p = $ 5.300.000 ÷ $ 6.400.000 = 82,8%**

| Si la probabilidad real de que no haya interfaz es… | Costo esperado de A | Decisión correcta |
|---|---|---|
| 25% | $ 7.600.000 | Desarrollar a medida |
| 50% (la estimación del equipo) | $ 9.200.000 | Desarrollar a medida |
| 82,8% (punto de indiferencia) | $ 11.300.000 | Da lo mismo |
| 95% | $ 12.080.000 | Comprar el conector |

> ⚠️ La decisión aguanta hasta 83%. Como la estimación fue 50%, hay margen amplio. Aun así conviene gastar en reducir la incertidumbre: una consulta a las bases pidiendo la documentación de interfaces cuesta cero y puede mover ese 50% muy abajo.

---

<a id="diapositiva-52"></a>

## Diapositiva 52 · Estimación de tres valores: poner rango donde había un número

Un solo número esconde la incertidumbre. Estimar tres —optimista, más probable y pesimista— la hace visible y permite calcular el valor esperado y su dispersión.

| Paquete 3.2 · Motor de formularios y flujo de trámites | Horas |
|---|---|
| Optimista (O): los 12 trámites comparten el mismo flujo | 520 h |
| Másprobable (M): tres trámites con variantes propias | 640 h |
| Pesimista (P): cada dirección municipal exige su variante | 900 h |
| Valor esperado E = (O + 4M + P) / 6 | 663 h |
| Desviación σ = (P − O) / 6 | ±63 h |

La EDT de la clase anterior estimaba 640 horas para este paquete. El cálculo con tres valores da 663 horas: la estimación original era 23 horas optimista. Con una desviación de 63 horas, hay cerca de dos tercios de probabilidad de que el paquete quede entre 600 y 726 horas.

> ⚠️ La diferencia entre el número original y el valor esperado no se agrega a la estimación del paquete: se agrega a la reserva de contingencia, que es donde se financia la variabilidad.

La distribución triangular, E = (O + M + P)/3, también es válida y más conservadora. Elija una, declárela y úsela para todos los paquetes.

---

<a id="diapositiva-53"></a>

## Diapositiva 53 · Simulación del cronograma: qué plazo conviene comprometer

Aplicando tres valores a todas las actividades y simulando muchas veces la red del cronograma, se obtiene una distribución de duraciones y no una fecha única.

| Percentil | Duración | Interpretación |
|---|---|---|
| P50 | 34 semanas | La ruta crítica determinista de la clase anterior |
| P70 | 37 semanas | Tres semanas de holgura sobre la ruta crítica |
| P80 | 38 semanas | El plazo que conviene comprometer en la oferta |
| P95 | 41 semanas | Todavía dentro del máximo de bases |

El plazo máximo de las bases es de 43 semanas (10 meses). La ruta crítica calculada en la clase anterior daba 34 semanas: comprometerla significaría cumplir sólo la mitad de las veces. Comprometer 38 semanas da 80% de probabilidad de cumplir y deja cinco semanas de holgura contractual.

> ⚠️ Regla práctica para una licitación con multas: comprometa el P80 y planifique internamente el P50. La diferencia entre ambos es la reserva de cronograma, y se gestiona igual que la de costo.

La simulación se hace con una planilla y unos cientos de iteraciones. No es necesario un software especializado para obtener una curva utilizable.

---

<a id="diapositiva-54"></a>

## Diapositiva 54 · Análisis de sensibilidad: dónde conviene concentrar la gestión

El análisis de sensibilidad ordena los riesgos por cuánto mueven el resultado total del proyecto. Se representa con un gráfico de barras horizontales ordenadas de mayor a menor, llamado diagrama de tornado.

| Orden | Riesgo | Valor esperado | % del total | Acumulado |
|---|---|---|---|---|
| 1 | R-01 · Interfaz del sistema financiero-contable | $ 3.200.000 | 25,2% | 25,2% |
| 2 | R-03 · Variantes por dirección en los trámites | $ 2.100.000 | 16,6% | 41,8% |
| 3 | R-04 · Calidad de los datos a migrar | $ 1.620.000 | 12,8% | 54,6% |
| 4 | R-02 · Demora en la habilitación de ClaveÚnica | $ 1.400.000 | 11,0% | 65,6% |
| 5 | R-06 · Disponibilidad de la contraparte | $ 1.200.000 | 9,5% | 75,1% |
| 6 a 10 | Los cinco riesgos restantes | $ 3.160.000 | 24,9% | 100% |

> ⚠️ Cinco riesgos concentran el 75% de la exposición. Si el equipo sólo puede trabajar en cinco cosas, ya sabe cuáles son, y son precisamente las que deben aparecer modificando el alcance, la arquitectura y el plan.

La columna de porcentaje acumulado es la que se lleva a la propuesta: demuestra que la priorización tiene fundamento y no es una opinión.

---

<a id="diapositiva-55"></a>

## Diapositiva 55 · Errores frecuentes en el análisis

| Error | Por qué es un error | Cómo se corrige |
|---|---|---|
| Calificar sin escala definida | «Alto» significa cosas distintas para cada integrante del equipo | Definir la escala antes de calificar y declararla |
| Poner todos los riesgos en «media» | Una calificación sin dispersión no prioriza nada | Forzar una distribución: no más de un tercio en cada zona |
| Sumar los impactos brutos | Da una cifra enorme que nadie va aaceptar en el precio | Sumar valores esperados, no impactos |
| Estimar el impacto sin fundamento | El número parece riguroso y no lo es | Anotar de dónde sale cada impacto: horas, tarifa, multa, licencia |
| Cuantificar los cuarenta riesgos | Esfuerzo enorme para mover decimales | Cuantificar sólo los priorizados en el cualitativo |
| Ignorar las correlaciones | Riesgos con causa común ocurren juntos y la suma subestima | Agrupar por causa y analizar el escenario conjunto |
| Comprometer el plazo determinista | Equivale a prometer una fecha con 50% de probabilidad | Comprometer un percentil alto y declarar cuál |
| Olvidar las oportunidades | Se pierde la única vía legítima de bajar el precio | Cuantificarlas con signo positivo y restarlas de la reserva |

> ⚠️ El análisis no busca acertar: busca que la cifra que se lleva al precio tenga un origen que se pueda explicar en treinta segundos.

---

<a id="diapositiva-56"></a>

## Diapositiva 56 · Recomendaciones para profundizar · Sección 4 · Analizar los riesgos

RECOMENDACIONES PARA PROFUNDIZAR

**Sección 4 · Analizar los riesgos**

**1**

**Cuantificar sus cinco**

Tome los cinco riesgos de mayor exposición de su registro y estime probabilidad e impacto con fundamento escrito. Anote de dónde sale cada impacto: horas por tarifa, multa por día, licencia.

**2**

**Calcular su reserva**

Sume los valores esperados y exprese el total como porcentaje de sus costos directos. Ése es el número que va a defender en la presentación.

**3**

**Armar un árbol**

Elija la decisión de arquitectura más discutida de su propuesta y compárela con un árbol de decisión de dos ramas. Calcule el punto de indiferencia.

**4**

**Reestimar con tres valores**

Vuelva al paquete de trabajo más grande de su EDT y estímelo con optimista, más probable y pesimista. Compare con lo que había puesto.

**5**

**Leer el capítulo**

PMBOK, procesos de análisis cualitativo y cuantitativo. Preste atención a la lista de herramientas: hay varias que esta clase no alcanzó a cubrir.

**6**

**Simular en planilla**

Arme una simulación simple de su cronograma con función aleatoria y trescientas iteraciones. Compare el P50 con el P80 y decida cuál va a comprometer.

---

<a id="diapositiva-57"></a>

## Diapositiva 57 · ▶ SECCIÓN 5 · Responder a los riesgos

**RESPONDER**

**05**

SECCIÓN 5

**Responder a los riesgos**

- Las cinco estrategias frente a una amenaza y las cinco frente a una oportunidad
- Cómo se elige la estrategia: controlabilidad, exposición y costo de la respuesta
- Cuánto conviene gastar en una respuesta, con el cálculo hecho
- La escalera de costo: de la consulta gratis a la reparación en operación
- Riesgo residual, riesgo secundario, disparador y plan de contingencia

---

<a id="diapositiva-58"></a>

## Diapositiva 58 · Qué debe contener una respuesta para que exista

Planificar la respuesta es desarrollar opciones, elegir una y acordar las acciones. El resultado no es una frase: son ocho datos por cada riesgo atendido.

| Campo | Qué se escribe | Ejemplo del caso (riesgo R-01) |
|---|---|---|
| Estrategia | Una de las cinco: escalar, evitar, transferir, mitigar, aceptar | Mitigar |
| Acción concreta | Un verbo con objeto, no una intención | Consultar en el foro y ejecutar una prueba de concepto de integración |
| Dueño | Una persona con nombre, no un área | Arquitecto de soluciones |
| Costo de la acción | En pesos o en horas, dentro del presupuesto | 40 horas · $ 1.120.000 |
| Etapa en que actúa | Propuesta, implementación, implantación u operación | Consulta en la propuesta; prueba de concepto en la semana 2 |
| Efecto esperado | Cuánto baja la probabilidad o el impacto | Probabilidad de 50% a 15% |
| Disparador | Señal observable que activa el plan de contingencia | Si al día 15 no hay documentación de la interfaz |
| Riesgo residual | Lo que queda después de la respuesta | 15% ×$ 6.400.000 = $ 960.000 |

---

<a id="diapositiva-59"></a>

## Diapositiva 59 · Las cinco estrategias frente a una amenaza

| Estrategia | En qué consiste | Ejemplo TIC | Cuándo conviene |
|---|---|---|---|
| Escalar | Trasladar la decisión a un nivel superior porque excede la autoridad del jefe de proyecto o el alcance del proyecto | La normativa de datos personales exige una definición corporativa que este proyecto no puede tomar | Cuando la respuesta está fuera del control del proyecto |
| Evitar | Cambiar el plan o el diseño para que el riesgo deje de existir | No integrarse con el sistema legado: reemplazar el módulo completo, o excluir esa integración del alcance | Exposición crítica y respuesta viable dentro del presupuesto |
| Transferir | Pasar la titularidad del riesgo a un tercero, normalmente pagando una prima | Subcontratar la integración a la empresa que mantiene el sistema legado, con precio cerrado | El tercero controla mejor el riesgo o lo puede absorber |
| Mitigar | Reducir la probabilidad, el impacto o ambos, sin eliminar el riesgo | Prueba de concepto temprana, prototipo, redundancia, incorporar aalguien con experiencia | Exposición alta y respuesta más barata que el valor esperado |
| Aceptar | Reconocer el riesgo y no actuar de forma proactiva. Activa si hay reserva y disparador; pasiva si sólo hay vigilancia | Se acepta la posibilidad de que la pasarela de pago cambie su certificación, con reserva asignada | Exposición baja, o ninguna respuesta rentable disponible |

Evitar y mitigar cambian la solución ofertada. Transferir cambia el modelo de contratación. Aceptar cambia el precio. Escalar cambia quién decide. Ninguna es gratis.

---

<a id="diapositiva-60"></a>

## Diapositiva 60 · Las cinco estrategias frente a una oportunidad

| Estrategia | En qué consiste | Ejemplo TIC en una licitación |
|---|---|---|
| Escalar | Trasladar la oportunidad a un nivel superior porque el beneficio excede aeste proyecto | El conector que se va a construir sirve para otros diez municipios: la decisión de convertirlo en producto es de la gerencia |
| Explotar | Asegurarse de que la oportunidad ocurra, eliminando su incertidumbre | Asignar al proyecto al arquitecto que ya integró ese mismo sistema en otro cliente |
| Compartir | Asociarse con un tercero mejor posicionado para capturar el beneficio | Consorcio con la empresa que ya tiene la certificación de la pasarela de pago exigida |
| Mejorar | Aumentar la probabilidad o el beneficio de la oportunidad | Adelantar la reunión con el área de informática del cliente para confirmar que sus licencias de nube son reutilizables |
| Aceptar | Reconocerla y aprovecharla si se presenta, sin actuar para provocarla | Si el mandante finalmente entrega los datos ya saneados, se libera la reserva asociada |

> ⚠️ En una licitación con evaluación económica de 30%, capturar dos oportunidades de tres millones cada una puede valer más puntos que toda la sección técnica de innovación. Y aparecen sólo si alguien las busca.

Las oportunidades también se escriben con la fórmula «dado que… entonces puede que…», y también se cuantifican con valor esperado, con signo positivo.

---

<a id="diapositiva-61"></a>

## Diapositiva 61 · Cómo se elige la estrategia: dos preguntas y una regla

La elección de estrategia no es una preferencia de estilo. Se decide con dos preguntas encadenadas y una comparación numérica.

**1 · ¿Quién controla el riesgo?**

Nosotros → evitar o mitigar. Un tercero → transferir. Nadie dentro del proyecto → escalar. Es la pregunta que ordena la mitad de las decisiones.

**2 · ¿La respuesta cuesta menos que el riesgo?**

Compare el costo de la acción con la reducción del valor esperado que produce. Si cuesta más de lo que ahorra, la estrategia correcta es aceptar y reservar.

**3 · La regla del umbral**

Si la exposición supera el umbral declarado en el plan de gestión, no basta con mitigar: hay que cambiar el diseño para que el riesgo deje de existir, o no ofertar.

| Situación | Estrategia que corresponde |
|---|---|
| Exposición crítica, el riesgo está bajo nuestro control | Evitar: cambiar alcance o arquitectura |
| Exposición alta, respuesta más barata que el ahorro esperado | Mitigar con acción costeada en el plan |
| Exposición alta, el riesgo lo controla un tercero competente | Transferir por contrato o por seguro |
| Exposición media, ninguna respuesta rentable | Aceptar de forma activa: reserva y disparador |
| Exposición baja | Aceptar de forma pasiva: sólo observación |

---

<a id="diapositiva-62"></a>

## Diapositiva 62 · Cuánto conviene gastar en una respuesta

Una respuesta se justifica si reduce el valor esperado más de lo que cuesta. Sobre el riesgo R-01 hay dos acciones posibles y conviene comparar ambas.

| Acción de respuesta | Costo | Prob. | VE después | Ahorro |
|---|---|---|---|---|
| Ninguna: aceptar el riesgo | 0 | 50% | $ 3.200.000 | — |
| Consulta formal en el foro de la licitación | 0 | 30% | $ 1.920.000 | $ 1.280.000 |
| Prueba de concepto de 40 horas | $ 1.120.000 | 20% | $ 1.280.000 | $ 1.920.000 |
| Ambas: consultar primero y luego probar | $ 1.120.000 | 15% | $ 960.000 | $ 2.240.000 |

La consulta no cuesta nada y baja la probabilidad de 50% a 30%: es la respuesta con mejor retorno de toda la propuesta y la que más veces se deja pasar por vencimiento del plazo. Las dos acciones juntas cuestan 40 horas y ahorran, en valor esperado, exactamente el doble de lo que cuestan.

> ⚠️ Criterio para decidir: haga la acción si el ahorro esperado supera su costo, y hágala en la etapa más temprana en que sea posible. El mismo dinero gastado antes compra más reducción de riesgo.

El retorno se calcula como ahorro esperado dividido por costo de la acción. Una acción de costo cero con efecto positivo tiene retorno infinito: por eso las consultas se responden siempre primero.

---

<a id="diapositiva-63"></a>

## Diapositiva 63 · La escalera de costo de la respuesta

El mismo riesgo se puede atender en ocho momentos distintos. El costo de atenderlo crece con cada peldaño, y la capacidad de cambiar la solución disminuye.

| Peldaño | Instrumento | Etapa | Costo relativo |
|---|---|---|---|
| 1 | Consulta formal en el foro de la licitación | Propuesta | Cero |
| 2 | Supuesto declarado en la propuesta | Propuesta | Cero |
| 3 | Exclusión explícita del alcance | Propuesta | Cero |
| 4 | Decisión de arquitectura que elimina el riesgo | Propuesta | Horas de diseño |
| 5 | Prueba de concepto o prototipo temprano | Implementación | Decenas de horas |
| 6 | Reserva de contingencia y plan de contingencia | Todas | Porcentaje del precio |
| 7 | Rehacer el componente durante la construcción | Implementación | Cientos de horas |
| 8 | Reparar en producción, con el cliente operando | Operación | Horas, multas y reputación |

> ⚠️ Los tres primeros peldaños son gratis y son los que más veces se dejan pasar, porque tienen plazo: el foro de consultas cierra en una fecha y después no se puede preguntar nada.

Regla de oro de esta clase: gestionar el riesgo es bajarlo de peldaño. Toda la sección 6 trata de cómo bajar riesgos al peldaño 1.

---

<a id="diapositiva-64"></a>

## Diapositiva 64 · Riesgo residual, riesgo secundario y disparador

**Riesgo residual**

Lo que queda del riesgo después de aplicar la respuesta. Nunca es cero.

Ejemplo: tras la prueba de concepto, R-01 baja de 50% a 15%. El residual es 15% × $ 6.400.000 = $ 960.000, y es lo que financia la reserva.

**Riesgo secundario**

El riesgo nuevo que crea la propia respuesta.

Ejemplo: subcontratar la integración al proveedor del sistema legado elimina el riesgo técnico y crea uno comercial, porque ese proveedor es competencia y conoce el precio.

**Disparador**

La señal observable que dice que el riesgo se está materializando y que hay que activar el plan de contingencia.

Ejemplo: si al día 15 del proyecto no hay documentación de la interfaz en manos del equipo.

> ⚠️ Todo riesgo residual se registra y se financia. Todo riesgo secundario se identifica y se analiza como cualquier otro. Y todo plan de contingencia sin disparador es un documento que nadie va a abrir.

Prueba rápida: si su plan de riesgos no tiene ni un solo riesgo residual escrito, es que sus respuestas se declararon perfectas. Ninguna lo es.

---

<a id="diapositiva-65"></a>

## Diapositiva 65 · Plan de contingencia y plan de reversa

**Plan de contingencia**

- Se activa cuando el disparador se cumple
- Está escrito antes, no se improvisa
- Tiene dueño, pasos y presupuesto asignado
- Se financia con la reserva de contingencia
- Ejemplo: si no hay interfaz, integrar por archivo plano con conciliación diaria

**Plan de reversa**

- Se activa cuando la contingencia tampoco resulta
- Devuelve la operación al estado anterior
- Debe estar probado, no sólo escrito
- Define qué pasa con los datos capturados en el intervalo
- Ejemplo: volver al procedimiento manual por mesón y reprogramar el corte

En la etapa de implantación el plan de reversa deja de ser una buena práctica y pasa a ser una exigencia contractual: el cliente necesita saber qué ocurre si el día del corte el sistema nuevo no responde.

> ⚠️ Un criterio de reversa se escribe con número y con hora: «si a las 06:00 del lunes la conciliación no cuadra en el 99,5% de los registros, se revierte».

---

<a id="diapositiva-66"></a>

## Diapositiva 66 · Las respuestas planificadas en el caso

| ID | Estrategia | Acción de respuesta | Etapa en que actúa |
|---|---|---|---|
| R-01 | Mitigar | Consulta por las interfaces y prueba de concepto de 40 horas | Propuesta e implementación |
| R-02 | Mitigar | Iniciar el trámite de habilitación en la semana 1 y no en la 8 | Implementación |
| R-03 | Evitar | Acotar la etapa 1 a8 trámites; los otros 4 en etapa opcional | Propuesta |
| R-04 | Mitigar | Perfilamiento de datos en la semana 3 y criterio de corte declarado | Implementación |
| R-05 | Mitigar | Rol con reemplazo declarado y decisiones de arquitectura escritas | Propuesta y operación |
| R-06 | Escalar | Supuesto de 5 días hábiles y hitos condicionados en el contrato | Propuesta |
| R-07 | Mitigar | Diseñar con seudonimización, bitácora y registro de consentimiento | Propuesta e implementación |
| R-08 | Transferir | Contrato con la pasarela con precio y certificación cerrados | Implementación |
| R-09 | Mitigar | Piloto con 12 funcionarios y despliegue por olas con soporte | Implantación |
| R-10 | Aceptar | Reserva asignada y prueba de intrusión anticipada | Implementación |

Cinco de las diez respuestas actúan, total o parcialmente, en la etapa de propuesta, y nueve tienen alguna acción antes de la implantación. Ésa es la señal de que el riesgo se anticipó.

---

<a id="diapositiva-67"></a>

## Diapositiva 67 · Implementar la respuesta: el proceso que más se olvida

Planificar la respuesta y ejecutarla son procesos distintos. Entre uno y otro se pierde la mayor parte del valor de la gestión de riesgos.

| Por qué no se ejecuta la respuesta | Cómo se evita |
|---|---|
| La acción no está en el cronograma, sólo en el registro de riesgos | Toda acción de respuesta es una actividad de la EDT, con duración y responsable |
| No tiene presupuesto asignado | El costo de la acción entra en el presupuesto del paquete correspondiente |
| El dueño es un área y no una persona | Nombre y apellido en la columna de dueño |
| El riesgo dejó de estar visible en las reuniones | Punto fijo de riesgos en el comité, con los cinco de mayor exposición |
| Nadie mide si la respuesta sirvió | Se reevalúa la probabilidad después de ejecutar la acción y se registra el cambio |
| La urgencia del día se come la prevención | Las acciones de la propuesta se ejecutan antes de que empiece la construcción |

> ⚠️ Prueba de existencia: busque en su cronograma las actividades que corresponden a sus respuestas de riesgo. Si no están, su plan de riesgos no se va a ejecutar y usted todavía no lo sabe.

---

<a id="diapositiva-68"></a>

## Diapositiva 68 · Monitorear: qué se hace con el registro durante la ejecución

**Vigilar disparadores**

Revisar si alguna señal definida se cumplió y activar el plan de contingencia correspondiente.

**Reevaluar**

Actualizar probabilidad e impacto de los riesgos vigentes con la información nueva del proyecto.

**Identificar nuevos**

Cada etapa trae riesgos que no existían al ofertar. El registro nunca deja de crecer.

**Medir efectividad**

Comprobar si las respuestas ejecutadas bajaron la exposición como se esperaba.

**Controlar la reserva**

Cuánta reserva se consumió, cuánta queda y qué riesgos siguen abiertos contra ella.

| Salida del monitoreo | Qué provoca |
|---|---|
| Información de desempeño del trabajo | Alimenta el informe de estado y el informe de riesgos al mandante |
| Solicitudes de cambio | Acciones correctivas y preventivas sobre la línea base |
| Actualizaciones del plan y de los documentos | Registro de riesgos, cronograma, presupuesto y lecciones aprendidas |
| Reserva liberada | Riesgos cerrados sin materializarse: la reserva vuelve al margen |

> ⚠️ La auditoría de riesgos evalúa algo distinto del riesgo: evalúa si el proceso de gestión está funcionando. Se hace al cierre de cada etapa y se documenta.

---

<a id="diapositiva-69"></a>

## Diapositiva 69 · Errores frecuentes en la respuesta

| Error | Cómo se reconoce | Cómo se corrige |
|---|---|---|
| Respuestas que son verbos | «Monitorear», «coordinar», «gestionar», «hacer seguimiento» | Escribir una acción con objeto, dueño, costo y fecha |
| Mitigar todo | Las diez respuestas dicen mitigar | Usar las cinco estrategias: hay riesgos que se evitan y otros que se aceptan |
| Respuesta más cara que el riesgo | Nadie calculó el ahorro esperado | Comparar costo de la acción con reducción del valor esperado |
| Aceptar sin reserva | Se dice «se acepta» y no hay plata detrás | La aceptación activa exige reserva y disparador; si no, es negligencia |
| Ignorar el riesgo secundario | La respuesta se declara sin consecuencias | Preguntar qué riesgo nuevo crea cada respuesta |
| Contingencia sin disparador | «Si ocurre, activaremos el plan B» | Definir la señal observable con fecha, número o condición |
| Respuestas fuera del cronograma | El plan de riesgos no aparece en la EDT | Cada acción es una actividad con duración y responsable |
| No decir en qué etapa actúa | La acción es correcta pero no se sabe cuándo ocurre | Declarar propuesta, implementación, implantación u operación |

> ⚠️ El error de fondo es siempre el mismo: escribir la respuesta como una promesa de esfuerzo en vez de como un compromiso verificable.

---

<a id="diapositiva-70"></a>

## Diapositiva 70 · Recomendaciones para profundizar · Sección 5 · Responder a los riesgos

RECOMENDACIONES PARA PROFUNDIZAR

**Sección 5 · Responder a los riesgos**

**1**

**Elegir con el algoritmo**

Aplique las dos preguntas y la regla del umbral a sus diez riesgos. Anote la estrategia de cada uno y verifique que no todas digan «mitigar».

**2**

**Calcular el retorno**

Para sus tres riesgos mayores, calcule el ahorro esperado de la respuesta y divídalo por su costo. Descarte las respuestas con retorno menor que uno.

**3**

**Bajar de peldaño**

Revise cada riesgo y pregunte si se puede atender un peldaño más arriba en la escalera de costo. Todo lo que llegue al peldaño 1, 2 o 3 es ganancia pura.

**4**

**Escribir dos disparadores**

Elija los dos riesgos con plan de contingencia y escriba su disparador con fecha, número o condición observable. Sin eso el plan no se activa nunca.

**5**

**Buscar el secundario**

Para cada respuesta, escriba qué riesgo nuevo crea. Al menos dos de sus respuestas van a resultar más caras de lo que parecían.

**6**

**Cruzar con el cronograma**

Verifique que cada acción de respuesta tenga una actividad en su EDT. Las que no la tengan, o entran al cronograma o salen del plan.

---

<a id="diapositiva-71"></a>

## Diapositiva 71 · ▶ SECCIÓN 6 · Riesgos de la licitación

**LICITACIÓN**

**06**

SECCIÓN 6

**Riesgos de la licitación**

- Por qué el riesgo de la licitación se gestiona antes y no después
- Riesgos del proceso, riesgos del contrato y riesgos que las bases no cuentan
- Las cinco palancas de anticipación y su costo
- Cómo se escribe una consulta, un supuesto y una exclusión que sirvan
- Cuándo la respuesta correcta es no presentarse

---

<a id="diapositiva-72"></a>

## Diapositiva 72 · Por qué el riesgo de una licitación es un riesgo distinto

**Se decide con la peor información del proyecto**

Hay que fijar alcance, arquitectura, plazo y precio conociendo al cliente sólo por un documento. Nunca se va a saber menos que en ese momento, y nunca se va a decidir más.

**La ventana para actuar tiene fecha de cierre**

El foro de consultas cierra. Después de esa fecha, la única forma de reducir incertidumbre es suponer, excluir o cambiar el diseño. Ya no se puede preguntar.

**El error se congela en el precio**

Adjudicada la licitación, el precio y el plazo quedan fijos. Todo lo que no se vio se paga con el margen del proveedor durante los 34 meses siguientes.

Por eso la gestión de riesgos de una licitación no se parece a la de un proyecto en curso. No se trata de vigilar: se trata de decidir, con poco tiempo y menos información, qué se pregunta, qué se supone, qué se excluye y qué se rediseña.

> ⚠️ El objetivo de esta sección: que cada riesgo identificado en las bases produzca una decisión visible en la oferta, y que esa decisión diga en qué etapa actúa. Un riesgo que no produjo decisión sigue existiendo, pero ahora sin dueño.

---

<a id="diapositiva-73"></a>

## Diapositiva 73 · La línea de tiempo del proceso y dónde se puede actuar

Un proceso de licitación tiene hitos con fecha. La capacidad de reducir riesgo cae abruptamente en el momento del cierre de consultas y desaparece en el cierre de ofertas.

| Hito del proceso | Qué se puede hacer todavía | Costo de actuar |
|---|---|---|
| Publicación de las bases | Leer con lectura adversarial y decidir si se oferta | Cero |
| Visita a terreno | Ver la operación real y medir lo que no está escrito | Horas de viaje |
| Plazo de consultas | Preguntar todo lo que produce costo indeterminado | Cero |
| Acta de respuestas | Releer: las respuestas modifican las bases ya costeadas | Rehacer estimaciones |
| Preparación de la oferta | Suponer, excluir, rediseñar, ajustar precio y reserva | Horas de diseño |
| Cierre y apertura de ofertas | Nada. La oferta es irrevocable tal como se presentó | Imposible |
| Evaluación y aclaraciones | Responder consultas del mandante sin alterar la oferta | Imposible |
| Adjudicación y firma | Negociar sólo lo que las bases permiten, que suele ser nada | Imposible |
| Ejecución del contrato | Gestionar lo que quedó: cambios, reserva y contingencias | Alto |

Los tres primeros hitos concentran toda la capacidad de reducir riesgo a costo cero, y ocupan menos de tres semanas del calendario.

---

<a id="diapositiva-74"></a>

## Diapositiva 74 · Riesgos del proceso mismo, antes de la adjudicación

| Riesgo | Cómo se materializa | Anticipación |
|---|---|---|
| Inadmisibilidad por formalidad | Falta un anexo o la garantía está mal glosada | Verificación documental 48 h antes |
| Garantía mal constituida | Monto, vigencia o glosa distintos | Emitirla temprano y hacerla revisar |
| Bases contradictorias entre sí | Lo administrativo y lo técnico chocan | Consulta citando ambos artículos |
| Requisito abierto o «según caso» | Un requisito cuyo alcance se define después | Consultar el límite o suponerlo |
| Criterio de evaluación no costeado | Se premia algo que la oferta no incluyó | Costear cada criterio de la pauta |
| Plazo de consultas vencido | Se entendieron las bases después del cierre | Leer y consultar la primera semana |
| Acta que cambia el alcance | Agrega trabajo con la estimación ya hecha | No cerrar el precio antes del acta |
| Presupuesto insuficiente | Lo pedido no cabe en el monto disponible | Ofertar por etapas, resto opcional |
| Licitación desierta o readjudicada | El proceso se cae y el esfuerzo se pierde | Costear la preparación de la oferta |

Ninguno de estos nueve riesgos es técnico, y los nueve pueden costar el contrato completo antes de escribir una línea de código.

---

<a id="diapositiva-75"></a>

## Diapositiva 75 · Riesgos del contrato · alcance, aceptación y plazo

Presentar una oferta es aceptar las bases completas. Los cinco riesgos siguientes viven en la letra del contrato y se delatan por una frase.

| Riesgo contractual | Frase que lo delata | Anticipación |
|---|---|---|
| Alcance elástico con precio fijo | «y todo lo necesario para el correcto funcionamiento» | Exclusiones explícitas y supuestos con número |
| Recepción conforme subjetiva | «aentera satisfacción del mandante» | Proponer criterios de aceptación medibles en la propuesta |
| Multas sin tope | «multa diaria de 1 UTM por cada día de atraso» | Calcular el peor caso y comprometer el plazo P80, no el P50 |
| Sin mecanismo de cambios | Las bases no dicen cómo se aprueba un aumento de alcance | Proponer el procedimiento de control de cambios en la propuesta |
| Propiedad intelectual | «todo producto será de propiedad del mandante» | Distinguir el código del proyecto de los componentes propios previos |

> ⚠️ Los cinco se anticipan escribiendo en la propuesta algo que las bases no exigen: exclusiones, criterios de aceptación y procedimiento de cambios. Nada de eso está prohibido y todo mejora la posición contractual.

Ofrecer criterios de aceptación medibles es, además, un diferenciador técnico: casi ningún oferente lo hace.

---

<a id="diapositiva-76"></a>

## Diapositiva 76 · Riesgos del contrato · dinero, datos y terceros

| Riesgo contractual | Cómo aparece | Anticipación |
|---|---|---|
| Encargo de tratamiento de datos personales | El proveedor procesará datos de terceros por cuenta del mandante | Definir rol, medidas de seguridad y responsabilidad. La Ley 21.719 entra en plena vigencia el 1 de diciembre de 2026 |
| Niveles de servicio en operación | «disponibilidad permanente», sin número ni horario | Consultar y ofertar contra un número: porcentaje, ventana y tiempos de respuesta |
| Reajuste y moneda | Licencias en dólares con precio en pesos por 24 meses | Cláusula de reajuste o cobertura, y precio con moneda y fecha de referencia |
| Solidaridad laboral | Se subcontrata parte del servicio o de la operación | Exigir certificados de cumplimiento y retener pagos contra ellos |
| Garantías | Vigencia que excede el plazo del proyecto y cubre la operación | Costear la garantía por todo el período, no sólo por la construcción |

> ⚠️ Los cinco tienen precio y casi nunca se cotizan: la garantía por los 34 meses del contrato, la cobertura de tipo de cambio, la dotación que sostiene un nivel de servicio y el costo de cumplir la normativa de datos personales.

Regla práctica: todo lo que el contrato obliga a mantener durante la operación se cotiza por mes y por la duración completa, no por una vez.

---

<a id="diapositiva-77"></a>

## Diapositiva 77 · Los riesgos que las bases no cuentan

Las bases describen lo que el mandante sabe y quiere contar. El riesgo mayor está en lo que no aparece porque para el mandante es obvio, o porque él mismo no lo sabe.

| Lo que las bases no dicen | Por qué importa | Cómo se descubre |
|---|---|---|
| Cuán documentado está el sistema legado | Son 200 o 600 horas de integración | Consulta formal y visita técnica |
| Si el proveedor actual va a cooperar | Suele competir en esta licitación | Averiguar quién mantiene hoy el sistema |
| Cuál es la calidad real de los datos | Define si se cotiza saneamiento | Pedir una muestra o un perfil de datos |
| Cuántas personas y en qué condiciones | Cambia interfaz y capacitación | Visita a terreno: turnos y dispositivos |
| Cuándo se puede intervenir la operación | Puede haber temporadas intocables | Preguntar el calendario operacional |
| Quién decide la recepción conforme | Un contrato se atasca en una firma | Identificar a la contraparte técnica |
| Qué pasó con el proyecto anterior | Un fracaso previo endurece todo | Buscar adjudicaciones anteriores |
| Capacidad del área TI del cliente | Cuánto trabajo suyo hay que asumir | Preguntar dotación y quién administrará |

---

<a id="diapositiva-78"></a>

## Diapositiva 78 · Las cinco palancas de anticipación

Frente a un riesgo detectado en las bases hay exactamente cinco cosas que se pueden hacer antes de presentar la oferta. Las tres primeras no cuestan dinero.

**1 · Consultar**

Preguntar en el foro para que el mandante aclare o corrija. Elimina la ambigüedad de raíz y la respuesta pasa a formar parte de las bases.

**2 · Suponer**

Declarar en la propuesta el valor que se está asumiendo. Convierte una incertidumbre en una frontera contractual verificable.

**3 · Excluir**

Decir explícitamente qué no está incluido. Lo que no está en el alcance no se debe entregar ni se debe cobrar después.

**4 · Rediseñar**

Cambiar el alcance, un requisito o la arquitectura para que el riesgo deje de existir o baje de magnitud.

**5 · No ofertar**

Retirarse. Es una decisión legítima y a veces la única correcta. Cuesta el esfuerzo comercial ya invertido.

> ⚠️ Las tres primeras palancas cuestan cero pesos y son las que más veces se dejan pasar. La cuarta es la que se evalúa mejor, porque demuestra comprensión. La quinta es la que salva empresas.

Toda respuesta de riesgo en una licitación es alguna de estas cinco, o una combinación. Si su respuesta no es ninguna de las cinco, probablemente sea sólo una intención.

---

<a id="diapositiva-79"></a>

## Diapositiva 79 · Palanca 1 · Cómo se escribe una consulta que sirva

El mandante responde por escrito y su respuesta pasa a formar parte de las bases. Una consulta bien escrita cambia el contrato; una mal escrita se responde con «remítase a las bases».

**Consulta que no sirve**

- «¿Puede aclarar el punto 5.3?»
- No cita el artículo exacto
- No dice qué parte es ambigua
- No propone interpretación
- Es abierta: se responde con una generalidad
- Respuesta típica: «remítase a las bases»

**Consulta que sirve**

- Cita el numeral y transcribe la frase
- Explica por qué admite dos lecturas
- Propone una interpretación concreta
- Pide confirmar o corregir esa interpretación
- Es cerrada: se responde sí o no
- Respuesta: una definición que se puede costear

«Respecto del numeral 5.3, que indica “el sistema se integrará con los sistemas del mandante”, se solicita confirmar que los sistemas a integrar son exclusivamente el financiero-contable y el de recursos humanos, y que el mandante entregará la documentación de sus interfaces en un plazo de 15 días desde la firma del contrato.»

Redacción tipo. Cita, transcribe, interpreta y pide confirmación con un plazo. La respuesta, cualquiera que sea, reduce el riesgo.

---

<a id="diapositiva-80"></a>

## Diapositiva 80 · Palanca 2 · Cómo se declara un supuesto para que proteja

Un supuesto declarado convierte una incertidumbre en una frontera del contrato. Si el supuesto resulta falso, el cambio de alcance es del cliente y no del proveedor.

| Supuesto que no protege | Por qué no protege | Supuesto que sí protege |
|---|---|---|
| Se asume que el cliente entregará la información oportunamente | No dice qué información, ni cuándo, ni qué pasa si no llega | El mandante entregará la documentación de interfaces dentro de los 15 días siguientes a la firma. Cada día de atraso desplaza el hito 2 en igual cantidad |
| Se asume una calidad razonable de los datos | «Razonable» no es verificable | Se asume que los registros a migrar no superan 180.000 y que la tasa de registros con campos obligatorios vacíos no supera el 5%. Sobre ese umbral, el saneamiento se cotiza aparte |
| Se asume disponibilidad de la contraparte | No hay número ni consecuencia | La contraparte validará cada entregable en 5 días hábiles. Transcurrido ese plazo el entregable se entiende aprobado para efectos del cronograma |
| Se asume que la capacitación es acotada | Ni cantidad ni modalidad ni sedes | La capacitación considera 4 sesiones de 3 horas para un máximo de 60 funcionarios, en dependencias del mandante y en horario hábil |

> ⚠️ Un supuesto protege cuando tiene tres cosas: un número, un plazo y una consecuencia declarada si no se cumple. Sin esas tres, es una frase de relleno.

---

<a id="diapositiva-81"></a>

## Diapositiva 81 · Palanca 3 · La exclusión explícita

**Qué se excluye legítimamente**

- Lo que las bases no pidieron y podría suponerse
- Lo que depende de un tercero fuera de control
- Licencias e infraestructura que ya tiene el cliente
- Trabajo sobre sistemas ajenos al objeto
- Migración fuera del alcance temporal acordado
- Soporte a usuarios que no son del mandante

**Cómo se escribe sin parecer un recorte**

- Nombrar la exclusión con precisión, no en general
- Explicar en una línea por qué queda fuera
- Indicar quién lo asume, si corresponde
- Ofrecerlo como línea opcional cotizada
- Ubicarlo en el alcance, no en letra chica
- Ser coherente con los supuestos declarados

«No forma parte del alcance la intervención del sistema financiero-contable del mandante. La integración se resuelve mediante servicios expuestos por dicho sistema; cualquier modificación de éste será ejecutada por su proveedor de mantenimiento.»

Redacción tipo. Nombra, explica y asigna. Ese párrafo evita una discusión de tres meses durante la ejecución.

---

<a id="diapositiva-82"></a>

## Diapositiva 82 · Palanca 4 · Rediseñar para que el riesgo deje de existir

Cuando la consulta no basta y el supuesto no alcanza, queda cambiar la solución. Es la palanca más cara de las tres primeras y la que más puntos gana, porque demuestra comprensión del problema.

| Riesgo detectado en las bases | Rediseño que lo elimina o lo reduce | Qué cambia |
|---|---|---|
| Los 12 trámites con flujos distintos | Ofertar 8 en etapa 1 y 4 en etapa opcional cotizada | Alcance |
| Legado sin interfaz utilizable | Capa de integración con dos modos: servicios y archivo | Arquitectura |
| Conectividad intermitente en terreno | Operación fuera de línea con sincronización diferida | Requisito no funcional |
| Disponibilidad exigida sin definir | Ofertar 99,5% en horario hábil como compromiso | Requisito no funcional |
| El usuario de terreno puede rechazarlo | Piloto con usuarios reales antes del despliegue masivo | Plan de trabajo |
| Cambio normativo en datos personales | Seudonimización, bitácora y consentimiento | Arquitectura |
| Volumen de datos a migrar desconocido | Migración por tramos con hito de conciliación | Alcance y plan |

> ⚠️ Cada línea de esta tabla es una decisión que hay que poder rastrear: en la propuesta debe verse el riesgo, la decisión que produjo y el lugar de la solución donde quedó.

---

<a id="diapositiva-83"></a>

## Diapositiva 83 · Palanca 5 · Cuándo la respuesta correcta es no presentarse

Presentarse a una licitación cuesta dinero y ganarla mal cuesta mucho más. Existen condiciones en que la decisión correcta es retirarse antes de invertir en la propuesta.

| Señal de retiro | Por qué es determinante |
|---|---|
| El presupuesto no alcanza para el alcance mínimo viable | Ganar significa perder plata desde el primer día |
| Hay un requisito habilitante que no se cumple | Experiencia, certificación o patrimonio: oferta inadmisible |
| Las multas máximas superan el margen del contrato | Un solo atraso convierte el contrato en pérdida |
| El alcance es abierto y el mandante no aclaró | No hay forma de fijar un precio defendible |
| El riesgo crítico depende de un tercero que compite | El incumbente controla el éxito y no tiene incentivo |
| El perfil clave no está disponible en esas fechas | Se estaría comprometiendo un equipo que no existe |
| El plazo exigido es inferior al P95 simulado | El atraso no es un riesgo: es una certeza con fecha |

> ⚠️ La decisión de ofertar o no es la primera respuesta de riesgo del proyecto, y es la única que se toma antes de gastar. En la propuesta del curso se pide declarar por qué sí se ofertó pese a los riesgos detectados.

---

<a id="diapositiva-84"></a>

## Diapositiva 84 · El acta de respuestas: el riesgo que aparece después de costear

Las respuestas del mandante a las consultas forman parte de las bases y pueden modificar el alcance, los plazos y los formularios. Llegan cuando el equipo ya avanzó en la propuesta.

| Qué puede traer el acta | Efecto | Cómo se anticipa |
|---|---|---|
| Una aclaración que amplía el alcance | Sube el esfuerzo estimado y puede romper el presupuesto | No cerrar la estimación antes del acta; dejar la EDT parametrizada |
| Una aclaración que reduce el alcance | Oportunidad: permite bajar el precio o subir el margen | Tener identificado qué se sacaría y cuánto vale |
| Un cambio de plazo o de fecha de cierre | Reordena la agenda interna de preparación | Agenda con holgura entre el acta y el cierre |
| Un formulario nuevo o modificado | Riesgo de inadmisibilidad si se usa la versión antigua | Revisar los anexos contra el acta antes de firmar la oferta |
| Una respuesta evasiva a la consulta clave | El riesgo sigue vivo y ahora sin salida gratuita | Pasar a la palanca 2 o 3: suponer o excluir, y dejarlo escrito |
| Respuestas a consultas de la competencia | Revelan qué preocupa a los otros oferentes | Leer el acta completa, no sólo las respuestas propias |

> ⚠️ La última fila es gratis y casi nadie la usa: el acta muestra las consultas de todos los oferentes. Es la única ventana que existe para ver cómo está leyendo las bases la competencia.

---

<a id="diapositiva-85"></a>

## Diapositiva 85 · Los riesgos de licitación del caso y la palanca aplicada

En la licitación 3456-12-LP26 se identificaron siete riesgos propios del proceso y del contrato. Ésta es la palanca aplicada a cada uno.

| Riesgo de la licitación | Palanca | Decisión adoptada |
|---|---|---|
| «Se integrará con los sistemas del mandante», sin decir cuáles | Consultar | Consulta 3 del foro: se confirmaron dos sistemas y un plazo de entrega de documentación |
| Los 12 trámites no tienen flujo definido | Rediseñar | Etapa 1 con 8 trámites; los 4 restantes como línea opcional cotizada |
| Migración de información histórica sin volumen ni calidad | Suponer | Supuesto de 180.000 registros y 5% de campos vacíos, con umbral declarado |
| «Disponibilidad permanente» sin número | Consultar | Consulta 7: el mandante confirmó 99,5% en horario hábil |
| Intervención del sistema financiero-contable | Excluir | Exclusión explícita: la modifica su proveedor de mantenimiento |
| Validación de entregables sin plazo definido | Suponer | Supuesto de 5 días hábiles con aprobación tácita para efectos del cronograma |
| Multa diaria sin tope y plazo máximo de 10 meses | Rediseñar | Se compromete el P80 de 38 semanas y no la ruta crítica de 34 |

Cinco de las siete respuestas costaron cero pesos. Las dos que costaron algo cambiaron el alcance y el plazo comprometido, y ambas mejoran la evaluación técnica en vez de empeorarla.

---

<a id="diapositiva-86"></a>

## Diapositiva 86 · Recomendaciones para profundizar · Sección 6 · Anticipar los riesgos de la licitación

RECOMENDACIONES PARA PROFUNDIZAR

**Sección 6 · Anticipar los riesgos de la licitación**

**1**

**Escribir cinco consultas**

Redacte cinco consultas para su caso con la estructura de esta sección: cita, transcripción, interpretación propuesta y petición de confirmación. Compárelas con las que iba a escribir.

**2**

**Redactar sus supuestos**

Reescriba los supuestos de su propuesta hasta que cada uno tenga número, plazo y consecuencia. Descarte los que no pueda escribir así.

**3**

**Listar sus exclusiones**

Escriba entre cinco y ocho exclusiones explícitas para su caso, cada una con su razón en una línea. Verifique que ninguna contradiga un supuesto.

**4**

**Leer un acta real**

Busque en Mercado Público un acta de respuestas a consultas de una licitación TIC. Observe cuántas consultas se responden con «remítase a las bases» y por qué.

**5**

**Revisar las multas**

Calcule la multa máxima posible de su caso y compárela con su margen. Si la supera, ese solo dato debería cambiar el plazo que van a comprometer.

**6**

**Decidir si se oferta**

Recorra las siete señales de retiro con su caso. Si ninguna aplica, escriba en dos líneas por qué se justifica ofertar: eso va en la propuesta.

---

<a id="diapositiva-87"></a>

## Diapositiva 87 · ▶ SECCIÓN 7 · Del riesgo a la solución

**SOLUCIÓN**

**07**

SECCIÓN 7

**Del riesgo a la solución**

- La cadena de trazabilidad: riesgo, decisión, lugar de la solución y evidencia
- Cómo un riesgo cambia el alcance y cómo cambia un requisito
- Patrones de arquitectura que existen para mitigar un riesgo concreto
- Cómo un riesgo cambia el plan de trabajo, la implantación y la operación
- Cómo se refleja todo eso en la oferta económica

---

<a id="diapositiva-88"></a>

## Diapositiva 88 · La cadena de trazabilidad que se evalúa

Un riesgo bien gestionado deja un rastro de cinco eslabones. Si falta cualquiera de ellos, la cadena se corta y el trabajo no se puede verificar.

**1**

**2**

**Riesgo**

**Decisión**

Escrito como causa, evento y efecto, con probabilidad e impacto.

Consultar, suponer, excluir o rediseñar. Con su fundamento.

**3**

**4**

**Lugar**

**Etapa**

Alcance, requisito, arquitectura, plan de trabajo u operación.

Propuesta, implementación, implantación u operación.

**5**

**Evidencia**

El párrafo, el componente, la actividad o la línea de precio.

El quinto eslabón es el que casi siempre falta. No basta con decir que se rediseñó: hay que poder señalar en qué página de la propuesta está el resultado de esa decisión.

> ⚠️ Prueba de la cadena, en los dos sentidos: para cada riesgo alto, ¿qué cambió en la propuesta? Y para cada componente inusual de su arquitectura, ¿qué riesgo lo justifica? Si alguna pregunta no tiene respuesta, falta trabajo.

---

<a id="diapositiva-89"></a>

## Diapositiva 89 · Los cuatro lugares donde un riesgo cambia la solución

| Lugar | Qué se modifica | Ejemplo | Dónde queda escrito |
|---|---|---|---|
| Alcance | Qué entra, qué sale, qué se divide en etapas | 8 trámites en etapa 1 y 4 en etapa opcional | Enunciado del alcance y exclusiones |
| Requisitos | Aparecen requisitos que las bases no pidieron | Operar 72 horas sin conexión y sincronizar después | Matriz de requisitos, columna de origen |
| Arquitectura | Componentes y patrones que existen por un riesgo | Capa de integración con dos modos de operación | Diagramas y decisiones de arquitectura |
| Plan y operación | Secuencia, hitos, marcha blanca y niveles de servicio | Despliegue por olas con soporte en sitio 60 días | EDT, cronograma y plan de servicios |

Los cuatro se pueden usar sobre el mismo riesgo, y muchas veces conviene. El riesgo de que el sistema legado no exponga interfaz se atiende excluyendo su modificación (alcance), exigiendo conciliación diaria (requisito), diseñando dos modos de integración (arquitectura) y probando en la semana 2 (plan).

> ⚠️ El orden de preferencia es siempre el mismo: primero se intenta resolver en el alcance, porque es gratis; después en el requisito; después en la arquitectura; y sólo al final en la operación, que es donde se paga mes a mes.

Cada una de estas modificaciones debe poder rastrearse hasta el riesgo que la produjo. Si no, parece capricho técnico.

---

<a id="diapositiva-90"></a>

## Diapositiva 90 · Cómo un riesgo cambia el alcance

Cambiar el alcance no significa ofrecer menos: significa ofrecer con borde. Hay seis mecanismos y todos son legítimos si se explican.

| Mecanismo | En qué consiste | Riesgo que resuelve |
|---|---|---|
| Dividir en etapas | Comprometer una etapa 1 acotada y verificable | Alcance mayor que el presupuesto o plazo |
| Excluir explícitamente | Nombrar lo que queda fuera y por qué | Alcance elástico y expectativas implícitas |
| Línea opcional cotizada | Ofrecer lo dudoso con precio, fuera del total | Requisito de valor incierto |
| Acotar por volumen | Poner número máximo: registros, sedes, usuarios | Volumen desconocido o sin respaldo |
| Acotar por variantes | Fijar cuántas variantes se construirán | Proliferación de casos particulares |
| Criterio de aceptación | Definir cuándo un entregable está terminado | Recepción conforme subjetiva |

«La etapa 1 considera 8 trámites, seleccionados con el mandante por volumen de atención. Los 4 restantes se ofrecen como etapa 2 opcional, cotizada en el anexo económico, y pueden contratarse sin rehacer la solución.»

Redacción tipo. Acota, justifica, cotiza lo excluido y garantiza que la decisión no encarece el futuro.

---

<a id="diapositiva-91"></a>

## Diapositiva 91 · Cómo un riesgo se convierte en un requisito

Muchos requisitos no funcionales no vienen de las bases: vienen de un riesgo. Y como no vienen de las bases, hay que declararlos con número para que se puedan verificar.

| Riesgo observado | Requisito que nace de él |
|---|---|
| La conectividad en el punto de atención es intermitente | La aplicación debe operar sin conexión hasta 72 horas y sincronizar sin pérdida al recuperar el enlace |
| El sistema legado puede caerse durante la integración | Toda operación de integración debe ser idempotente y reintentable, con cola persistente y bitácora |
| El peak de demanda es ocho veces la carga media | El sistema debe sostener 400 transacciones por minuto con tiempo de respuesta bajo 2 segundos en el percentil 95 |
| El usuario de terreno trabaja con guantes y a pleno sol | La interfaz debe operarse con área táctil mínima de 12 milímetros y contraste legible bajo luz directa |
| Los datos personales quedan bajo tratamiento del proveedor | Los datos sensibles deben almacenarse seudonimizados y todo acceso debe quedar en bitácora inalterable |
| La contraparte puede exigir reconstruir una operación pasada | El sistema debe permitir reconstruir el estado de cualquier trámite en cualquier fecha, en menos de 5 minutos |

> ⚠️ Todo requisito que nace de un riesgo se anota con su origen en la matriz de requisitos. Esa columna es la que demuestra que el análisis sirvió para algo.

---

<a id="diapositiva-92"></a>

## Diapositiva 92 · Cómo un riesgo cambia la arquitectura

Buena parte de los patrones de arquitectura existen para mitigar un riesgo. Elegirlos sin nombrar el riesgo es decoración; nombrarlo es ingeniería.

| Patrón o decisión | Riesgo que mitiga | Costo aproximado |
|---|---|---|
| Capa de integración con doble modo | El legado no expone servicios utilizables | Diseño y un conector adicional |
| Cola persistente con reintento | Indisponibilidad temporal de un externo | Componente de mensajería |
| Operaciones idempotentes | Duplicación de transacciones por reintento | Sin costo si se define temprano |
| Operación fuera de línea | Conectividad intermitente en terreno | Cliente local y conciliación |
| Interruptor de funcionalidad | Una función nueva puede fallar en producción | Bajo: apagar sin desplegar |
| Seudonimización y bitácora de acceso | Tratamiento de datos personales y auditoría | Diseño, almacenamiento y desempeño |
| Redundancia y balanceo | Indisponibilidad con nivel de servicio exigido | Infraestructura duplicada |
| Réplica y respaldo con RTO y RPO | Pérdida de datos o caída prolongada | Infraestructura y ensayos |
| Adaptador por sistema externo | Cambio de versión del sistema del cliente | Diseño; evita rehacer el núcleo |

En la propuesta, cada uno de estos componentes se presenta con una línea que dice qué riesgo lo justifica. Sin esa línea, el evaluador lo lee como sobreingeniería.

---

<a id="diapositiva-93"></a>

## Diapositiva 93 · El riesgo en la arquitectura lógica y en la física

**Arquitectura lógica**

- Aislar lo incierto detrás de una interfaz propia
- Separar en módulos lo que puede cambiar por separado
- Definir contratos de datos explícitos entre componentes
- Diseñar para degradación parcial y no para todo o nada
- Dejar puntos de extensión donde el alcance puede crecer

**Arquitectura física**

- Dimensionar para el peak declarado y no para el promedio
- Redundar sólo lo que el nivel de servicio exige
- Separar ambientes: el de pruebas es un riesgo si no existe
- Definir RTO y RPO con número y probar la recuperación
- Elegir nube u on-premise según quién asume la continuidad

Toda decisión de arquitectura física tiene costo mensual durante los 24 meses de operación. Una redundancia mal justificada encarece la oferta y una redundancia faltante pone en riesgo el nivel de servicio comprometido.

> ⚠️ Regla de dimensionamiento frente al riesgo: si el nivel de servicio es exigible con multa, la redundancia deja de ser opcional y pasa a ser parte del costo del contrato.

---

<a id="diapositiva-94"></a>

## Diapositiva 94 · Cómo un riesgo cambia el plan de trabajo y la implantación

| Instrumento del plan | Riesgo que atiende | Etapa |
|---|---|---|
| Prueba de concepto de integración, semana 2 | Incertidumbre técnica sobre el legado | Implementación |
| Perfilamiento de datos antes de la migración | Calidad real de los datos desconocida | Implementación |
| Hito de conciliación entre nuevo y antiguo | Migración incompleta o inconsistente | Implementación |
| Prueba de carga antes de la marcha blanca | Peak de demanda superior al estimado | Implementación |
| Prueba de intrusión anticipada | Observaciones de seguridad con retrabajo | Implementación |
| Piloto con usuarios reales | Rechazo del usuario y del adoptante crítico | Implantación |
| Despliegue por olas y no en un solo evento | Falla masiva sin forma de contener el daño | Implantación |
| Doble operación durante la marcha blanca | El sistema nuevo no responde el día del corte | Implantación |
| Criterio de reversa escrito y probado | La contingencia tampoco resulta | Implantación |
| Soporte reforzado en sitio los primeros 60 días | Curva de aprendizaje y errores de uso | Operación |

> ⚠️ Cada una de estas diez actividades tiene horas, responsable y fecha. Si están en el plan de riesgos y no en la EDT, no van a ocurrir y el precio ofertado no las contiene.

---

<a id="diapositiva-95"></a>

## Diapositiva 95 · Cómo un riesgo cambia la operación y el servicio

Terminada la implantación, el riesgo no desaparece: cambia de forma. Pasa de riesgo de proyecto a riesgo de servicio, y se gestiona con instrumentos distintos.

| Instrumento de operación | Riesgo que atiende | Cómo se cotiza |
|---|---|---|
| Nivel de servicio con número y ventana | Indisponibilidad y discusión de lo prometido | Dotación y redundancia |
| Mesa de ayuda con niveles de escalamiento | Volumen de incidentes superior al estimado | Personas por turno y por mes |
| Monitoreo y alertas sobre indicadores | Detección tardía de una degradación | Herramienta y operación |
| Plan de continuidad con RTO y RPO | Caída prolongada o pérdida de datos | Infraestructura y ensayos |
| Gestión de cambios y versiones | Una actualización rompe algo en producción | Horas de despliegue y pruebas |
| Revisión periódica del registro de riesgos | Riesgos nuevos que aparecen en operación | Horas del jefe de servicio |
| Informe mensual con indicadores | Discrepancia sobre el cumplimiento | Horas de gestión |

> ⚠️ Un nivel de servicio que se compromete sin dimensionar la dotación que lo sostiene es una multa diferida. Y el que compromete la disponibilidad sin controlar la infraestructura, transfiere a su empresa un riesgo que no puede gestionar.

---

<a id="diapositiva-96"></a>

## Diapositiva 96 · La matriz de trazabilidad riesgo → solución

| ID | Decisión adoptada | Dónde queda | Etapa |
|---|---|---|---|
| R-01 | Capa de integración con dos modos y prueba de concepto | Arquitectura y EDT | Propuesta e implementación |
| R-02 | Habilitación en semana 1 e hito condicionado | Plan y contrato | Implementación |
| R-03 | Etapa 1 con 8 trámites; 4 como línea opcional | Alcance y oferta económica | Propuesta |
| R-04 | Perfilamiento de datos y umbral de calidad declarado | Alcance, EDT y supuestos | Propuesta e implementación |
| R-05 | Reemplazo declarado por rol y decisiones documentadas | Equipo y arquitectura | Propuesta y operación |
| R-06 | Supuesto de 5 días hábiles con aprobación tácita | Supuestos y cronograma | Propuesta |
| R-07 | Seudonimización, bitácora y consentimiento | Arquitectura y requisitos | Propuesta e implementación |
| R-08 | Contrato con la pasarela con precio cerrado | Adquisiciones | Implementación |
| R-09 | Piloto, despliegue por olas y soporte en sitio | Plan de implantación | Implantación |
| R-10 | Prueba de intrusión anticipada y reserva asignada | EDT y reserva | Implementación |

Diez riesgos, diez decisiones, cuatro lugares de la solución y cuatro etapas. Ésta es la tabla que convierte el plan de riesgos en parte de la ingeniería y no en un anexo.

---

<a id="diapositiva-97"></a>

## Diapositiva 97 · Cómo se refleja todo esto en la oferta económica

El riesgo entra en el precio por cuatro caminos, y sólo uno de ellos es la reserva de contingencia. Confundirlos hace que la oferta parezca cara sin explicación.

| Camino | Qué contiene | Ejemplo del caso |
|---|---|---|
| Horas de acciones de mitigación | Actividades de la EDT por un riesgo | 40 h de prueba y 60 h de perfilamiento |
| Componentes de la arquitectura | Desarrollo o licencias de un patrón | Segundo modo de integración y cola |
| Infraestructura y operación | Redundancia, ambientes y dotación | Ambiente de pruebas propio |
| Reserva de contingencia | Valor esperado de los riesgos aceptados | 8% de los costos directos: $ 12.684.800 |

Los tres primeros caminos están dentro de los costos directos y se defienden mostrando la actividad o el componente. El cuarto se defiende mostrando la tabla de valor esperado. Los cuatro juntos son la respuesta completa a la pregunta «¿por qué su oferta cuesta esto?».

> ⚠️ Una oferta que gestionó el riesgo suele ser algo más cara que una que lo ignoró, y bastante más barata que ésa misma al final del contrato. Esa diferencia hay que saber explicarla en la presentación.

En una evaluación con 60% técnico y 30% económico, el punto que se gana explicando el riesgo suele valer más que el punto que se pierde por el precio.

---

<a id="diapositiva-98"></a>

## Diapositiva 98 · El mismo método en otras industrias

El caso del curso es municipal, pero la mecánica es idéntica en cualquier industria. Cambia el riesgo dominante y con él el lugar de la solución que se modifica.

| Industria | Riesgo dominante | Decisión que produce |
|---|---|---|
| Portuaria | Ventana de atraque y sistema de patio antiguo | Integración desacoplada y despliegue en ventana |
| Agroindustria | Planta y campo no comparten ventana | Plan con dos ventanas de intervención distintas |
| Salud | Continuidad de la atención y dato sensible | Doble operación y seudonimización |
| Transporte de carga | El dato lo genera un tercero externo | Portal del transportista y plan de adhesión |
| Retail y multitienda | Peak estacional y dos regímenes normativos | Dimensionamiento por peak y separación de flujos |
| Servicios financieros | Fiscalización y trazabilidad de operaciones | Bitácora inalterable y reportería regulatoria |
| Minería | Conectividad y condiciones en terreno | Operación fuera de línea y equipo apto para faena |

> ⚠️ En las siete industrias el riesgo dominante no es tecnológico: es operacional. La tecnología es la respuesta, no el problema. Una propuesta que se abre hablando de tecnología ya perdió el punto de comprensión.

---

<a id="diapositiva-99"></a>

## Diapositiva 99 · Innovación y riesgo: cómo proponer algo nuevo sin comprometerse de más

Innovar aumenta el riesgo por definición: se propone algo que el equipo no ha hecho antes. La salida no es dejar de innovar, sino separar lo que se compromete de lo que se explora.

**Innovación comprometida**

Va en el alcance con criterio de aceptación. Debe ser algo que el equipo puede sostener aunque falle el resto.

**Innovación con prueba previa**

Se compromete después de una prueba de concepto con criterio de continuidad declarado en el plan.

**Innovación opcional**

Se ofrece cotizada aparte, con su propio riesgo y su propio plan. El cliente decide si la quiere.

**Innovación de hoja de ruta**

Se describe como evolución futura, sin compromiso contractual en este contrato.

> ⚠️ La innovación que se compromete se costea y se le asigna riesgo como a cualquier otro componente. La que no se costea no se compromete: se enuncia como hoja de ruta y se dice explícitamente que lo es.

Un evaluador experimentado castiga la innovación prometida sin plan y premia la innovación acotada con prueba previa. La diferencia es el tratamiento del riesgo.

---

<a id="diapositiva-100"></a>

## Diapositiva 100 · Rediseños que no resuelven nada

| Rediseño aparente | Por qué no resuelve | Qué sí resolvería |
|---|---|---|
| Agregar microservicios | Si el riesgo es la interfaz del legado, dividir lo propio no ayuda | Capa de integración con doble modo y conciliación |
| Poner todo en la nube | La nube no arregla un dato de mala calidad ni una contraparte ausente | Perfilamiento temprano y supuesto con umbral |
| Agregar un tablero de control | Ver el problema no es resolverlo | Alerta con umbral y responsable de actuar |
| Prometer metodología ágil | El alcance sigue siendo fijo por contrato | Alcance por etapas y control de cambios acordado |
| Aumentar el equipo | Máspersonas no reducen incertidumbre técnica | Prueba de concepto y decisión con árbol |
| Subir el porcentaje de reserva | Cubre el costo pero no evita el atraso | Mitigación temprana sobre los riesgos de mayor exposición |
| Agregar capacitación | La resistencia no siempre es falta de conocimiento | Participación temprana del adoptante crítico |

> ⚠️ Prueba para distinguir un rediseño real de uno aparente: pregunte cuánto baja la probabilidad o el impacto del riesgo, y con qué evidencia. Si no hay número, el rediseño es decorativo.

---

<a id="diapositiva-101"></a>

## Diapositiva 101 · Recomendaciones para profundizar · Sección 7 · Del riesgo a la solución

RECOMENDACIONES PARA PROFUNDIZAR

**Sección 7 · Del riesgo a la solución**

**1**

**Construir su matriz**

Arme la matriz riesgo → decisión → lugar → etapa para sus diez riesgos. Es el entregable de esta sección y el que más peso tiene en la evaluación.

**2**

**Auditar su arquitectura**

Recorra su diagrama componente por componente y escriba qué riesgo justifica cada uno. Los que no tengan riesgo detrás, justifíquelos de otra forma o sáquelos.

**3**

**Requisitos ocultos**

Revise sus riesgos operacionales y escriba el requisito no funcional que cada uno produce, con número. Añádalos a la matriz de requisitos con su origen.

**4**

**Cruzar riesgos y EDT**

Verifique que las diez actividades de mitigación de esta sección, o sus equivalentes, estén en su EDT con horas y responsable.

**5**

**Costear el riesgo**

Separe en su oferta los cuatro caminos por los que el riesgo entra al precio. Sabrá defender la cifra y encontrará algo que estaba cobrando dos veces.

**6**

**Acotar su innovación**

Clasifique cada una de sus innovaciones en los cuatro niveles de compromiso. Al menos una debería bajar de nivel.

---

<a id="diapositiva-102"></a>

## Diapositiva 102 · ▶ SECCIÓN 8 · Declarar el riesgo y su etapa

**DECLARAR**

**08**

SECCIÓN 8

**Declarar el riesgo y su etapa**

- Por qué conviene declarar el riesgo en vez de esconderlo
- La ficha de riesgo completa, campo por campo
- Las cuatro etapas y qué acción corresponde a cada una
- Catálogo de acciones por etapa: propuesta, implementación, implantación y operación
- El registro entregable, el gobierno del riesgo y el cierre

---

<a id="diapositiva-103"></a>

## Diapositiva 103 · Por qué conviene declarar el riesgo y no esconderlo

La intuición dice que mostrar riesgos debilita una oferta. En una evaluación técnica ocurre lo contrario, y hay cuatro razones concretas.

**Demuestra comprensión**

Sólo puede nombrar el riesgo quien entendió la operación. Es la prueba más rápida de que se leyó bien.

**Justifica el precio**

La reserva, las horas de mitigación y los componentes de la arquitectura dejan de parecer relleno.

**Fija la frontera**

El supuesto y la exclusión declarados protegen al proveedor cuando el supuesto resulta falso.

**Ordena la ejecución**

El equipo que llega el primer día sabe qué vigilar, con qué disparador y con qué presupuesto.

El riesgo que no se declara no desaparece: cambia de dueño en silencio. Si el proveedor lo detectó y no lo dijo, lo va a pagar él. Si no lo detectó, lo va a descubrir el proyecto por su cuenta.

> ⚠️ Hay un límite: declarar un riesgo sin respuesta se lee como una advertencia de fracaso. Todo riesgo declarado en la propuesta debe ir acompañado de la acción y de la etapa en que ésta actúa.

---

<a id="diapositiva-104"></a>

## Diapositiva 104 · Dónde se declara cada cosa dentro de la propuesta

| Qué se declara | Dónde va en la propuesta | Qué pasa si falta |
|---|---|---|
| Supuestos | Capítulo de alcance, sección numerada | El cambio de alcance lo paga usted |
| Exclusiones | Capítulo de alcance, a continuación | Hay que entregar lo que no se cotizó |
| Requisitos nacidos de un riesgo | Matriz de requisitos, columna de origen | Parecen exigencias inventadas |
| Decisiones de arquitectura | Capítulo de arquitectura, justificadas | Se leen como sobreingeniería |
| Acciones de mitigación | EDT, cronograma y presupuesto | No se ejecutan y no están pagadas |
| Registro de riesgos | Capítulo o anexo de gestión de riesgos | No hay evidencia de método |
| Reserva de contingencia | Oferta económica, línea propia | El precio no se puede defender |
| Plan de gestión de riesgos | Capítulo de gestión del proyecto | El proceso parece improvisado |

> ⚠️ La coherencia entre estos ocho lugares es lo que separa una propuesta armada de una propuesta cosida. Un supuesto que no aparece en el registro de riesgos, o una acción que no está en la EDT, delata que el trabajo se hizo por partes.

Antes de entregar, recorra los ocho lugares y verifique que dicen lo mismo. Es una revisión de una hora que cambia la nota.

---

<a id="diapositiva-105"></a>

## Diapositiva 105 · La ficha de riesgo completa, con un ejemplo lleno

| Campo | Contenido para el riesgo R-01 |
|---|---|
| Identificador y categoría | R-01 · Rama 2 de la RBS: integración y sistema legado |
| Enunciado | Dado que el sistema financiero-contable es de 2011 y no documenta sus interfaces, puede que no exponga servicios utilizables, con la consecuencia de desarrollar una capa intermedia de 400 horas |
| Dueño | Arquitecto de soluciones del proyecto |
| Probabilidad e impacto | 50% · $ 6.400.000 · exposición 0,25 · valor esperado $ 3.200.000 |
| Marco de tiempo | Entre la firma del contrato y la semana 6 |
| Estrategia | Mitigar |
| Acción 1 · propuesta | Consulta formal pidiendo la documentación de interfaces y un plazo. Costo: cero |
| Acción 2 · implementación | Prueba de concepto de integración en la semana 2. Costo: 40 horas, $ 1.120.000 |
| Efecto esperado | Probabilidad de 50% a 15% tras ambas acciones |
| Disparador | Si al día 15 el equipo no tiene la documentación de la interfaz en su poder |
| Plan de contingencia | Integración por archivo con conciliación diaria; capa lista para ambosmodos |
| Riesgo residual | 15% ×$ 6.400.000 = $ 960.000, cubierto por la reserva de contingencia |
| Riesgo secundario | La integración por archivo introduce latencia de un día en la conciliación contable |

---

<a id="diapositiva-106"></a>

## Diapositiva 106 · Las cuatro etapas en que puede actuar una acción

| Etapa | Cuándo ocurre | Qué se puede hacer | Costo |
|---|---|---|---|
| 1 · Propuesta | Antes de presentar la oferta | Consultar, suponer, excluir, rediseñar, dimensionar, reservar, decidir el plazo comprometido | Muy bajo |
| 2 · Implementación | Desde la firma hasta el término de la construcción | Probar, prototipar, integrar temprano, conciliar, medir, revisar seguridad, controlar cambios | Medio |
| 3 · Implantación | Puesta en marcha y estabilización | Marcha blanca, doble operación, olas, capacitación, reversa, soporte en sitio | Alto |
| 4 · Operación | Los 24 meses de servicio posteriores | Niveles de servicio, monitoreo, continuidad, mejora, revisión periódica del registro | Mensual y permanente |

La regla es una sola: la acción se ubica en la etapa más temprana en que sea posible ejecutarla. Un riesgo que sólo se puede atender en operación es un riesgo que se aceptó al ofertar, y eso debe estar dicho.

> ⚠️ Un plan de riesgos sano tiene la mayoría de sus acciones en las etapas 1 y 2. Si la mayoría está en las etapas 3 y 4, lo que se escribió no es un plan de riesgos: es un plan de reparaciones.

En el caso del curso, cinco de las diez respuestas actúan total o parcialmente en la etapa de propuesta y nueve tienen alguna acción antes de la implantación.

---

<a id="diapositiva-107"></a>

## Diapositiva 107 · Etapa 1 · Acciones que sólo se pueden tomar en la propuesta

**Acciones sobre las bases y el contrato**

- Consulta formal en el foro, dentro del plazo
- Supuesto declarado con número, plazo y consecuencia
- Exclusión explícita con su justificación
- Criterios de aceptación propuestos por el oferente
- Procedimiento de control de cambios propuesto
- Hitos condicionados a una entrega del mandante
- Decisión fundada de ofertar o de retirarse

**Acciones sobre la solución y el precio**

- Alcance por etapas y líneas opcionales cotizadas
- Requisitos no funcionales declarados con número
- Decisiones de arquitectura que eliminan un riesgo
- Dimensionamiento por peak y no por promedio
- Plazo comprometido en un percentil alto y declarado
- Reserva de contingencia calculada y visible
- Equipo con reemplazos declarados por rol

> ⚠️ Catorce acciones y trece de ellas cuestan cero pesos. Es la etapa con mejor relación entre lo que se gana y lo que se gasta de todo el ciclo del proyecto.

---

<a id="diapositiva-108"></a>

## Diapositiva 108 · Etapa 2 · Acciones durante la implementación

| Acción | Riesgo que atiende | Cuándo |
|---|---|---|
| Prueba de concepto de la integración crítica | Incertidumbre técnica sobre un sistema externo | Primeras semanas |
| Prototipo navegable validado con usuarios | Requisitos mal entendidos o incompletos | Antes de construir |
| Perfilamiento de la información a migrar | Calidad y volumen reales de los datos | Antes de diseñar la migración |
| Integración temprana y continua | Descubrir el problema de interfaz al final | Desde el primer incremento |
| Prueba de carga contra el peak declarado | Rendimiento insuficiente en producción | Antes de la marcha blanca |
| Revisión de seguridad y prueba de intrusión | Retrabajo por observaciones tardías | Antes de la marcha blanca |
| Hito de conciliación con el sistema antiguo | Migración incompleta o inconsistente | Al cierre de cada tramo |
| Control de cambios con impacto valorizado | Crecimiento silencioso del alcance | Permanente |
| Revisión quincenal del registro de riesgos | Riesgos nuevos y disparadores no vistos | Cada comité |

> ⚠️ El principio común de las nueve acciones es el mismo: adelantar el momento en que se descubre el problema. No reducen la dificultad técnica; reducen el costo de enfrentarla.

---

<a id="diapositiva-109"></a>

## Diapositiva 109 · Etapa 3 · Acciones durante la implantación

| Acción | Riesgo que atiende | Cómo se declara en la propuesta |
|---|---|---|
| Marcha blanca con conciliación | El sistema nuevo da resultados distintos | Duración, criterio de éxito y dueño |
| Doble operación temporal | El corte falla y no hay cómo atender | Cuánto dura y quién paga el doble esfuerzo |
| Despliegue por olas | Falla masiva sin forma de contenerla | Cuántas olas, con qué criterio y orden |
| Piloto con usuarios reales | Rechazo del usuario final | Cuántos usuarios, cuánto dura y qué se mide |
| Criterio de reversa probado | La contingencia tampoco resulta | Condición, hora y destino de los datos |
| Capacitación cercana al corte | Se capacita y se olvida antes de usar | Sesiones, fechas y modalidad |
| Soporte en sitio los primeros días | Errores de uso en el peor momento | Personas, turnos y duración |
| Datos de corte y congelamiento | Transacciones en tránsito que se pierden | Ventana de congelamiento y aviso |

> ⚠️ La implantación es la etapa que menos se planifica y la que más determina la percepción del proyecto. Un sistema técnicamente correcto que se implanta mal queda registrado como un fracaso.

En las bases del curso, la estrategia de puesta en producción es un producto evaluado con peso propio. Estas ocho acciones son su contenido.

---

<a id="diapositiva-110"></a>

## Diapositiva 110 · Etapa 4 · Acciones durante la operación

| Acción | Riesgo que atiende | Cómo se cotiza |
|---|---|---|
| Nivel de servicio comprometido con número | Discusión sobre qué se prometió | Dotación y redundancia mensual |
| Mesa de ayuda con escalamiento definido | Volumen de incidentes mayor al previsto | Personas por turno y por mes |
| Monitoreo con alertas y umbrales | Detección tardía de una degradación | Herramienta y horas de operación |
| Plan de continuidad con RTO y RPO probados | Caída prolongada o pérdida de datos | Infraestructura y ensayos |
| Gestión de versiones y ventanas de cambio | Una actualización rompe producción | Horas de despliegue y pruebas |
| Revisión trimestral del registro de riesgos | Riesgos nuevos propios de la operación | Horas del jefe de servicio |
| Informe mensual con indicadores acordados | Discrepancia sobre el cumplimiento | Horas de gestión |
| Plan de transferencia y salida | Fin del contrato sin continuidad asegurada | Horas del último trimestre |

> ⚠️ La última fila casi nunca se escribe y es la que el mandante agradece: decir desde la propuesta cómo se entrega el servicio al final del contrato es una señal de seriedad que casi ningún oferente da.

Toda acción de esta etapa se cotiza por mes y por la duración completa del servicio, no por una vez.

---

<a id="diapositiva-111"></a>

## Diapositiva 111 · Cómo se distribuyen las acciones del caso en las cuatro etapas

| Etapa | Riesgos con acción en esta etapa | N° | Costo asociado |
|---|---|---|---|
| 1 · Propuesta | R-01 · R-03 · R-05 · R-06 · R-07 | 5 | Cero: consultas, supuestos y diseño |
| 2 · Implementación | R-01 · R-02 · R-04 · R-07 · R-08 · R-10 | 6 | 160 horas, dentro de la EDT |
| 3 · Implantación | R-09 | 1 | Piloto, olas y soporte: 120 horas |
| 4 · Operación | R-05 | 1 | Documentación y traspaso del servicio |

Un mismo riesgo puede tener acción en más de una etapa, y en general conviene: la consulta actúa en la propuesta y la prueba de concepto en la implementación, y juntas bajan la probabilidad más que cualquiera de las dos por separado.

| Lectura de la distribución | Qué significa |
|---|---|
| Mayoría en etapas 1 y 2 | El riesgo se anticipó. Es la distribución que se busca |
| Mayoría en etapa 3 | Se está confiando en la marcha blanca para descubrir problemas |
| Mayoría en etapa 4 | Se está trasladando el riesgo al servicio, donde se paga por mes |
| Ninguna acción en etapa 1 | No se usó la única ventana gratuita que tenía el proyecto |

---

<a id="diapositiva-112"></a>

## Diapositiva 112 · El registro de riesgos que se entrega con la propuesta

El registro que se adjunta a la propuesta es una versión resumida del registro interno. Estas son las columnas mínimas y el orden recomendado.

| Columna | Contenido | Por qué está |
|---|---|---|
| ID | Código correlativo por rama de la RBS | Permite citarlo en el resto de la propuesta |
| Enunciado | Causa, evento y efecto en una frase | Demuestra que el riesgo es de este caso |
| P · I · E | Probabilidad, impacto y exposición | Justifica la prioridad |
| Valor esperado | Producto de probabilidad por impacto | Sostiene la reserva del precio |
| Estrategia | Escalar, evitar, transferir, mitigar, aceptar | Muestra criterio y no un verbo repetido |
| Acción | Verbo con objeto, dueño y costo | Es lo que se compromete |
| Etapa | Propuesta, implementación, implantación, operación | Es la columna que el curso exige |
| Disparador | Señal observable que activa la contingencia | Hace ejecutable el plan de contingencia |
| Residual | Exposición que queda tras la acción | Demuestra honestidad y cierra el cálculo |

> ⚠️ Entre doce y quince riesgos bien tratados es el tamaño correcto para una propuesta. Cuarenta filas genéricas se leen como un formulario llenado a última hora, y así se evalúan.

---

<a id="diapositiva-113"></a>

## Diapositiva 113 · Gobierno del riesgo durante el contrato

| Instancia | Frecuencia | Quién participa | Qué produce |
|---|---|---|---|
| Revisión rápida del registro | Quincenal | Equipo de proyecto | Estado de los cinco mayores |
| Comité con el mandante | Mensual | Jefes de proyecto de ambos | Informe y escalamientos |
| Revisión completa | Cierre de etapa | Equipo ampliado y arquitecto | Registro y reserva recalculados |
| Auditoría de la gestión | Cierre de etapa | Aseguramiento de calidad | Evalúa el proceso, no el riesgo |
| Escalamiento | Sobre el umbral | Gerencia de ambas partes | Decisión de alcance o plazo |

Proponer estas cinco instancias en la propuesta cuesta media página y demuestra que el oferente sabe cómo se ejecuta un contrato largo. Casi ningún competidor lo hace, y el mandante lo agradece porque le resuelve un problema de control que él tampoco tiene resuelto.

> ⚠️ El umbral de escalamiento se declara con número desde la propuesta: por ejemplo, cualquier riesgo cuya exposición supere el 2% del valor del contrato se informa al comité en la sesión siguiente.

El gobierno del riesgo se declara en el plan de gestión del proyecto, no en el registro. Son documentos distintos con lectores distintos.

---

<a id="diapositiva-114"></a>

## Diapositiva 114 · Cierre: liberación de reserva y lecciones aprendidas

**Liberación de la reserva**

- Cada riesgo cerrado sin materializarse libera su parte
- La liberación se informa y se registra, no se gasta sola
- Al cierre de cada etapa se recalcula la reserva restante
- La reserva sobrante mejora el margen del contrato
- Nunca se reasigna a otro riesgo sin decisión escrita

**Lecciones aprendidas**

- Qué riesgos ocurrieron y cuáles no, con su probabilidad real
- Qué respuestas funcionaron y cuáles fueron caras e inútiles
- Qué riesgos aparecieron y no estaban en el registro inicial
- Cuánto se desvió el impacto real del impacto estimado
- Todo esto alimenta la lista de verificación del próximo caso

La comparación entre el impacto estimado y el impacto real es el único mecanismo que existe para que la próxima estimación sea mejor. Una empresa que no lo hace repite sus errores de estimación durante años y no sabe por qué.

> ⚠️ Redacción tipo para el cierre: «De los diez riesgos del registro inicial se materializaron tres, con un costo real de $ 4.100.000 frente a una reserva de $ 12.684.800. Se liberaron $ 8.584.800».

---

<a id="diapositiva-115"></a>

## Diapositiva 115 · Recomendaciones para profundizar · Sección 8 · Declarar el riesgo y su etapa

RECOMENDACIONES PARA PROFUNDIZAR

**Sección 8 · Declarar el riesgo y su etapa**

**1**

**Llenar tres fichas**

Complete la ficha de trece campos para sus tres riesgos de mayor exposición. Son las que se citan en el cuerpo de la propuesta.

**2**

**Clasificar por etapa**

Asigne etapa a cada una de sus acciones y cuente cuántas caen en cada una. Si la etapa 1 tiene menos de un tercio, vuelva a la sección 6.

**3**

**Armar el registro**

Construya la tabla de nueve columnas con doce a quince riesgos. Ése es el anexo de gestión de riesgos de su propuesta.

**4**

**Revisar los ocho lugares**

Verifique que sus supuestos, exclusiones, requisitos, arquitectura, EDT, registro, reserva y plan digan lo mismo. Es una revisión de una hora.

**5**

**Escribir el gobierno**

Redacte en media página las instancias de revisión, el umbral de escalamiento con número y el formato del informe mensual.

**6**

**Preparar el cierre**

Escriba desde ahora cómo se liberará la reserva y cómo se documentarán las lecciones. Es un párrafo que casi nadie incluye y que se nota.

---

<a id="diapositiva-116"></a>

## Diapositiva 116 · ▶ SECCIÓN 9 · En su propuesta

**PROPUESTA**

**09**

SECCIÓN 9

**En su propuesta**

- Qué productos de la propuesta dependen del trabajo de riesgos
- Estructura del capítulo de gestión de riesgos y contenido mínimo
- Qué busca el evaluador y qué es lo que más descuenta
- Cómo contar el riesgo en tres minutos de presentación oral
- La ruta de trabajo de la semana, paso a paso

---

<a id="diapositiva-117"></a>

## Diapositiva 117 · Qué productos de la propuesta dependen de este trabajo

La gestión de riesgos no es un capítulo de la propuesta: es una capa que atraviesa casi todos los productos exigidos.

| Producto de la propuesta | Qué aporta el trabajo de riesgos |
|---|---|
| Esquema de solución y alcance | Etapas, exclusiones y líneas opcionales |
| Matriz de requisitos | Requisitos no funcionales con su origen |
| Arquitectura lógica y física | Componentes y patrones justificados por un riesgo |
| EDT y cronograma | Actividades de mitigación y plazo comprometido |
| Oferta económica | Reserva de contingencia y costos de las acciones |
| Estrategia de puesta en producción | Marcha blanca, reversa y soporte inicial |
| Servicios de operación | Niveles de servicio, continuidad y monitoreo |
| Plan y registro de riesgos | El documento propiamente tal |

> ⚠️ Por eso el trabajo de riesgos se hace antes que casi todo lo demás. Un equipo que lo deja para el final tiene que rehacer el alcance, la arquitectura y el precio, o entregar una propuesta incoherente.

---

<a id="diapositiva-118"></a>

## Diapositiva 118 · Estructura recomendada del capítulo de gestión de riesgos

| N° | Sección | Contenido |
|---|---|---|
| 1 | Enfoque y plan de gestión | Método, escalas, umbrales, roles, financiamiento y calendario |
| 2 | Riesgo general del proyecto | Cuán riesgoso es este proyecto y dónde se concentra |
| 3 | Riesgos principales | De ocho a doce fichas resumidas, las de mayor exposición |
| 4 | Trazabilidad riesgo → solución | La matriz de decisiones, con lugar y etapa |
| 5 | Supuestos y exclusiones | Remisión al capítulo de alcance, sin repetir |
| 6 | Reserva de contingencia | Cálculo, monto y política de uso y liberación |
| 7 | Gobierno durante el contrato | Instancias, frecuencia, umbral de escalamiento e informes |
| A | Anexo: registro completo | De doce a quince riesgos con las nueve columnas |

> ⚠️ Cuatro o cinco páginas y un anexo. Si el capítulo pasa de ocho páginas, casi con seguridad contiene teoría de riesgos, y la teoría no se evalúa: se evalúa lo que usted decidió con ella.

---

<a id="diapositiva-119"></a>

## Diapositiva 119 · Contenido mínimo exigible: lista de cotejo

**Debe estar presente**

- Escala de probabilidad e impacto declarada
- Al menos doce riesgos propios del caso
- Al menos dos oportunidades, no sólo amenazas
- Todas las ramas de la RBS revisadas
- Cada riesgo con causa, evento y efecto
- Los cinco mayores cuantificados en pesos
- Reserva calculada y trazable a esa tabla

**Y además**

- Estrategia distinta según el riesgo, no todo mitigar
- Acción con dueño, costo y fecha
- Etapa declarada para cada acción
- Disparador en los riesgos con contingencia
- Riesgo residual escrito
- Matriz de trazabilidad riesgo a solución
- Coherencia con alcance, EDT y oferta económica

> ⚠️ Catorce puntos. Un grupo que pueda marcar los catorce tiene, sin excepción, una propuesta mejor que la de un grupo que marca seis, aunque el software propuesto sea el mismo.

---

<a id="diapositiva-120"></a>

## Diapositiva 120 · Qué busca el evaluador en cada criterio

| Criterio de evaluación | Qué se busca en materia de riesgo |
|---|---|
| Comprensión del problema | Que los riesgos sean de esta operación y no de cualquier proyecto |
| Esquema de solución y alcance | Que las exclusiones y las etapas se expliquen por un riesgo |
| Arquitectura lógica y física | Que cada componente inusual tenga un riesgo que lo justifique |
| Plan de trabajo, EDT y cronograma | Que las acciones de mitigación existan como actividades |
| Plan de riesgos | Que haya método, número, dueño, etapa y riesgo residual |
| Servicios de operación | Que los niveles comprometidos estén sostenidos por dotación |
| Consolidación y coherencia | Que el riesgo diga lo mismo en todos los capítulos |
| Oferta económica | Que la reserva tenga una tabla detrás y no un porcentaje |

> ⚠️ El trabajo de riesgos aporta puntos en ocho criterios distintos de la pauta. Es, por lejos, el capítulo con mayor rendimiento por hora invertida de toda la propuesta.

Y a la inversa: un plan de riesgos genérico contamina la lectura de los otros siete criterios, porque revela que el equipo no entendió la operación.

---

<a id="diapositiva-121"></a>

## Diapositiva 121 · Los errores que más descuentan

| Error | Cómo lo ve el evaluador | Costo en la pauta |
|---|---|---|
| Riesgos genéricos | Copiados de un manual, sirven para cualquier caso | Comprensión del problema |
| Todo mitigado | No hubo criterio, hubo un verbo repetido | Plan de riesgos |
| Sin etapa declarada | No se sabe cuándo actúa la acción | Plan de riesgos |
| Reserva sin cálculo | Un porcentaje de costumbre | Oferta económica |
| Acciones fuera de la EDT | El plan no se va aejecutar | Plan de trabajo |
| Arquitectura sin justificar | Componentes que parecen decorativos | Arquitectura |
| Cero oportunidades | Sólo se miró la mitad del problema | Comprensión del problema |
| Contradicción entre capítulos | El alcance dice una cosa y el riesgo otra | Consolidación |
| Cuarenta riesgos sin respuesta | Un formulario llenado, no un análisis | Plan de riesgos |

> ⚠️ Ninguno de los nueve errores es un error de conocimiento: los nueve son de oficio. Se corrigen con una revisión final ordenada, y esa revisión toma menos de dos horas.

---

<a id="diapositiva-122"></a>

## Diapositiva 122 · Cómo contar el riesgo en tres minutos de presentación

En la presentación no hay tiempo para el registro completo. Hay tiempo para una estructura de cuatro movimientos, y conviene ensayarla.

**1 · El riesgo que manda**

Nombre el riesgo de mayor exposición en una frase, con su número. «El 25% de nuestra exposición está en la integración con el sistema de 2011».

**2 · Qué decidimos**

Diga la decisión, no la intención. «Por eso diseñamos la integración con dos modos y consultamos la documentación en el foro».

**3 · Dónde se ve**

Señale el lugar. «Está en la lámina de arquitectura, en la actividad 4.1 de la EDT y en las 40 horas de la semana 2».

**4 · Qué queda**

Cierre con el residual y la reserva. «Queda un residual de $ 960.000, dentro de la reserva de $ 12.684.800».

> ⚠️ Tres minutos, un solo riesgo contado completo, y la mención de que los otros nueve están en el anexo con el mismo tratamiento. Eso comunica mucho más que enumerar diez riesgos a medias.

Si la comisión pregunta por otro riesgo, la respuesta correcta empieza por el número: probabilidad, impacto, decisión y etapa. Ténganlos a mano en una hoja.

---

<a id="diapositiva-123"></a>

## Diapositiva 123 · La ruta de trabajo, paso a paso

| N° | Paso | Quién |
|---|---|---|
| 1 | Escribir el plan de gestión de riesgos: escalas, umbrales y roles | Jefe de proyecto |
| 2 | Lectura adversarial de las bases, marcando las frases de riesgo | Todo el equipo |
| 3 | Sesión de identificación recorriendo la RBS rama por rama | Todo el equipo |
| 4 | Invertir los supuestos y depurar el registro a doce o quince | Dos personas |
| 5 | Calificar, priorizar y cuantificar los cinco mayores | Jefe y arquitecto |
| 6 | Elegir estrategia, definir acción, dueño, costo y etapa | Todo el equipo |
| 7 | Redactar consultas, supuestos y exclusiones | Dos personas |
| 8 | Cruzar con alcance, arquitectura, EDT y oferta económica | Jefe de proyecto |

Doce horas de equipo, repartidas en dos semanas. El paso 2 y el paso 7 tienen fecha límite externa: el foro de consultas cierra y después no hay vuelta atrás.

> ⚠️ El orden importa. Hacer el paso 6 antes del paso 5 produce respuestas caras para riesgos pequeños; hacer el paso 8 al final es lo que evita que la propuesta se contradiga a sí misma.

---

<a id="diapositiva-124"></a>

## Diapositiva 124 · Glosario · de amenaza a matriz de exposición

| Término | Significado |
|---|---|
| Amenaza | Riesgo con efecto negativo sobre un objetivo del proyecto |
| Análisis cualitativo | Priorización de riesgos por probabilidad e impacto en escalas |
| Análisis cuantitativo | Estimación numérica del efecto de los riesgos sobre plazo y costo |
| Apetito al riesgo | Cuánta incertidumbre la organización está dispuesta aasumir |
| Disparador | Señal observable de que un riesgo se está materializando |
| Estimación de tres valores | Optimista, más probable y pesimista, para calcular valor esperado |
| Evento de riesgo | El hecho incierto que puede ocurrir o no |
| Exposición | Producto de probabilidad por impacto; el nivel de riesgo |
| Impacto | Magnitud del efecto sobre un objetivo si el riesgo ocurre |
| Línea base de costos | Costos estimados más la reserva de contingencia |
| Matriz de exposición | Cruce de probabilidad e impacto con zonas de acción |

---

<a id="diapositiva-125"></a>

## Diapositiva 125 · Glosario · de oportunidad a valor monetario esperado

| Término | Significado |
|---|---|
| Oportunidad | Riesgo con efecto positivo sobre un objetivo del proyecto |
| Percentil de cronograma | Duración que se cumple con una probabilidad dada: P50, P80 |
| Plan de contingencia | Respuesta preparada que se activa cuando el disparador se cumple |
| Plan de reversa | Vuelta al estado anterior cuando la contingencia no resulta |
| RBS | Estructura de desglose de riesgos: descomposición por categorías |
| Registro de riesgos | Documento vivo con los riesgos individuales y su tratamiento |
| Reserva de contingencia | Fondo para riesgos identificados; parte de la línea base |
| Reserva de gestión | Fondo para riesgos no identificados; fuera de la línea base |
| Riesgo residual | Exposición que queda después de aplicar la respuesta |
| Riesgo secundario | Riesgo nuevo creado por la propia respuesta a otro riesgo |
| Valor monetario esperado | Probabilidad por impacto, expresado en dinero |

---

<a id="diapositiva-126"></a>

## Diapositiva 126 · Lo que hay que llevarse de esta clase

**El riesgo es una decisión**

Un riesgo que no cambió nada de la propuesta no fue gestionado: fue mencionado.

**Temprano es barato**

Consultar, suponer y excluir cuestan cero. Reparar en producción cuesta el margen.

**Con número o no existe**

Probabilidad, impacto, valor esperado, costo de la acción y residual.

**Cada acción tiene etapa**

Propuesta, implementación, implantación u operación. Declararla es parte del trabajo.

**Y todo debe cerrar**

Alcance, requisitos, arquitectura, EDT y precio tienen que decir lo mismo.

En el caso de Integra TIC SpA, el trabajo de riesgos produjo siete consultas, cuatro supuestos declarados, tres exclusiones, dos cambios de alcance, cuatro decisiones de arquitectura, diez actividades en la EDT, un plazo comprometido distinto del determinista y una reserva de $ 12.684.800 respaldada por $ 12.680.000 de valor esperado.

> ⚠️ Nada de eso es un anexo. Todo eso es la oferta. Ésa es la diferencia entre una propuesta que gestionó el riesgo y una que lo mencionó.

Material de referencia: PMBOK, área de conocimiento Gestión de los Riesgos del Proyecto; Bases Administrativas FEP01.26 y Bases Técnicas Transversales FEP02.26 del curso.

---

<a id="diapositiva-127"></a>

## Diapositiva 127 · Recomendaciones para profundizar · Sección 9 · En su propuesta

RECOMENDACIONES PARA PROFUNDIZAR

**Sección 9 · En su propuesta**

**1**

**Ejecutar la ruta**

Los ocho pasos, en ese orden, en las próximas dos semanas. Asigne responsable y fecha a cada paso hoy mismo, no cuando toque.

**2**

**Marcar la lista de cotejo**

Recorra los catorce puntos del contenido mínimo antes de entregar. Cada punto sin marcar es un descuento que ya sabe dónde está.

**3**

**Ensayar los tres minutos**

Practique la estructura de cuatro movimientos con el riesgo mayor de su caso. Cronometre: si pasa de tres minutos, sobra descripción y falta decisión.

**4**

**Hacer la revisión cruzada**

Una persona del equipo que no escribió el capítulo de riesgos debe verificar la coherencia con alcance, arquitectura, EDT y precio.

**5**

**Leer el PMBOK**

El área de conocimiento completa. Después de esta clase se lee en una hora y media, y va a reconocer cada proceso.

**6**

**Guardar el registro**

Al terminar el semestre, anote qué riesgos habrían ocurrido de verdad. Es el primer activo de lecciones aprendidas de su vida profesional.
