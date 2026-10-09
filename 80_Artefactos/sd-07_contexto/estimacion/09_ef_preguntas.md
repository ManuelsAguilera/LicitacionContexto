# Factores de ambiente (EF): preguntas para el consenso del equipo (paso 5, puerta G5, parte de ambiente)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: **los ocho valores informados por el usuario el 2026-10-08** (E3 se cambió de 3 a 4), pendientes de la firma del equipo; E7 queda como supuesto sin respaldo. Los ocho factores describen al equipo y a su contexto, y los asigna el equipo por consenso (FEP03, diapositivas 42 a 45), no el proponente de la estimación. Dependen del sd-04 (pila tecnológica), del sd-06 (metodología) y del sd-12 (equipo), que todavía no están redactados. Este documento deja las preguntas, los valores informados (sección 3), el rango posible y un cuadro de escenarios ilustrativos. Los escenarios ilustrativos no son una propuesta de valores.

## 1. Cómo funciona

- **EF = 1,4 − 0,03 × Σ (peso × valor)**. Un EF bajo es buena noticia: el trabajo cuesta menos. El rango va de 0,42 (equipo ideal) a 1,70 (equipo sin experiencia y a tiempo parcial).
- **Factor de conversión (CF).** Se cuenta cuántos de E1 a E6 valen menos de 3 y cuántos de E7 y E8 valen más de 3. Con 2 o menos, 20 horas por punto. Con 3 o 4, 28 horas por punto (+40 %). Con 5 o más, el método no estima y se replantea el proyecto (diapositiva 49).
- **Lectura.** Se usa la lectura B (convención C1): la fórmula da la programación y el total del proyecto es E / 0,40.

| Factor | Peso | 0 significa | 5 significa |
| :-- | --: | :-- | :-- |
| E1 Modelo de proyecto | 1,5 | Nunca trabajó con este modelo | Lo domina y lo aplica siempre |
| E2 Experiencia en el negocio | 0,5 | Nadie conoce el negocio del mandante | Lo conoce a fondo |
| E3 Orientación a objetos | 1 | Nunca desarrolló con objetos | Es experto |
| E4 Capacidad del analista | 0,5 | El analista líder es novato | Muy capaz y con experiencia |
| E5 Motivación | 1 | No hay interés | Equipo muy motivado |
| E6 Estabilidad de requisitos | 2 | El alcance cambia todo el tiempo | Cerrados, sin cambios |
| E7 Personal a tiempo parcial | −1 | Todos son de dedicación exclusiva | Casi todos son a tiempo parcial |
| E8 Dificultad del lenguaje | −1 | Lenguaje y herramientas fáciles | Extremadamente difícil |

## 2. Preguntas para el consenso, con sugerencia

| N.º | Factor | Pregunta que debe responder el equipo | Lo que el repositorio ya dice | Sugerencia |
| :-- | :-- | :-- | :-- | :-- |
| 1 | Todos | ¿Quién asigna los valores y cómo? | Hay siete integrantes (AGENTS.md). Los valores se informaron el 2026-10-08 (sección 3) | Una sola reunión con todo el equipo. Cada persona anota su valor antes de discutir. Se registran los desacuerdos, porque la clase los considera el mejor diagnóstico (diapositiva 46) |
| 2 | Todos | ¿Cuándo se asignan? | El sd-04, el sd-06 y el sd-12 no están redactados | Esperar a que existan al menos la pila tecnológica, la metodología y la dotación. Mientras tanto, usar solo el rango de la sección 3 y marcar el resultado como provisional |
| 3 | E1 | ¿Qué modelo de gestión usará el proyecto y cuántos del equipo lo han aplicado? | El sd-01 (1.5) describe un PMIS (Jira y SharePoint) y cuatro comités con periodicidad. El modelo híbrido se redacta en el sd-06 | Valorar solo la experiencia real de las personas con ese modelo, no la intención de usarlo. Si el sd-06 combina dos modelos, valorar el más débil |
| 4 | E2 | ¿Cuánto conoce el equipo el negocio de una cadena multitienda con crédito propio? | El sd-01 (1.4) cita tres proyectos de referencia: POS con operación sin conexión, plataforma de consentimiento financiero y motor ATP con marketplace | Valorar por experiencia previa documentable (proyectos, trabajo en retail o banca), no por lo leído en el Caso. Si nadie la tiene, el valor es bajo y se declara |
| 5 | E3 | ¿Cuánto domina el equipo la orientación a objetos con el lenguaje elegido? | Stack informado: Java Spring Boot, TypeScript, Node.js, Go y React (`contexto_sd-04.md`, D-12) | Preguntar a cada integrante cuántos proyectos hizo con objetos. Tomar la mediana, no el mejor |
| 6 | E4 | ¿Quién es el analista líder y qué experiencia tiene en ese rol? | La dotación de 16 profesionales del sd-01 (1.2) no tiene un analista de requisitos; el Arquitecto de Solución trabajó como analista | Valorar al analista que de verdad llevará los casos de uso. Si el rol se reparte, valorar el promedio |
| 7 | E5 | ¿Qué tan motivado está el equipo con este proyecto? | Sin datos propios en el repositorio; el sd-01 (1.1) declara valores de responsabilidad y compromiso | Responder de forma anónima, con una escala de 1 a 5 por integrante. Tomar la mediana |
| 8 | E6 | ¿Cuán estables son los requisitos? | Hay 5 RF de clientes Retail por validar; metas del Anexo D marcadas «propuesta del proponente» por validar con el cliente; decisiones abiertas (portal del proveedor, evaluación de AS-04, factibilidad de EXC-16); los vacíos del catálogo (conciliación contable, retención de bitácora, buró de crédito, administración de reglas de comisión) | Dar un valor medio o bajo mientras esas decisiones sigan abiertas. Revisar la coherencia con el plan de riesgos del sd-08: si este dice que el alcance puede cambiar, E6 no puede valer 5 (diapositiva 45). Un cambio de 2 puntos en E6 mueve el esfuerzo en cerca de 12 % |
| 9 | E7 | ¿Cuántas personas del equipo del proponente trabajarán a tiempo parcial? | El sd-01 asigna 16 profesionales sin decir su dedicación; el sd-12 (sin redactar) la fija. Las 46 personas del cliente (RC-09) no son el equipo del proponente | Contar solo al equipo del proponente. Si el equipo tiene otras obligaciones (estudios u otro trabajo), declararlo, porque es el factor que más sorprende después |
| 10 | E8 | ¿Qué tan difícil es el lenguaje y el conjunto de herramientas del sd-04? | Unas 30 tecnologías y tres alternativas sin decidir (`contexto_sd-04.md`, D-12) | Valorar el conjunto (lenguaje, nube, mensajería, pruebas), no solo el lenguaje. Un entorno muy nuevo para el equipo sube el valor |
| 11 | CF | ¿Se informa siempre el escenario de 28 horas por punto? | La convención C3 ya lo decide | Sí. El CF es el parámetro más sensible del método (+40 %); se informa el escenario base y el de 28 horas, con la regla de Karner declarada |
| 12 | Todos | ¿Cómo se justifican los valores extremos? | La clase exige justificar los 0 y los 5 (diapositivas 40 y 45) | Una frase por cada 0 o 5, con un hecho comprobable. No copiar valores de otro proyecto |

## 3. Valores informados por el usuario (2026-10-08)

Los valores los dio el usuario. Las frases de justificación son un borrador mío a partir de lo que dijo y del sd-01 (`[BORRAR DESPUES] sd-01/sd-01.md`); el equipo debe confirmarlas.

| Factor | Peso | Valor | Justificación (borrador) | Estado |
| :-- | --: | --: | :-- | :-- |
| E1 Modelo de proyecto | 1,5 | 5 | El equipo tiene experiencia con el modelo de gestión híbrido que usará el proyecto (declarado por el usuario). El sd-01, apartado 1.5, describe un gobierno ya definido (PMIS con Jira y SharePoint, comité ejecutivo mensual, comité de proyecto quincenal, comité de arquitectura, comité de operación y seguimiento semanal), y el apartado 1.4 reúne tres proyectos de referencia como contratista principal. El sd-06 debe describir ese modelo híbrido con las mismas instancias | Extremo. Justificación razonable; se sostiene si el sd-06 y la Tabla 1 de credenciales del sd-01 lo confirman. Si no, bajar a 4 (+6,0 % de horas) |
| E2 Experiencia en el negocio | 0,5 | 4 | El equipo conoce el negocio (retail, crédito y omnicanal) por los tres proyectos de referencia del sd-01, apartado 1.4 | Interpretado como E2 («conocemos en un 4»); E3 se informó aparte |
| E3 Orientación a objetos | 1 | 4 | Experiencia significativa: el stack informado usa Java Spring Boot, TypeScript, Node.js, Go y React, y la empresa es una fábrica de software a medida (sd-01, 1.1.1) | Informado el 2026-10-08 (cambió de 3 a 4) |
| E4 Capacidad del analista | 0,5 | 4 | El Arquitecto de Solución trabajó como analista en proyectos anteriores | Confirmado |
| E5 Motivación | 1 | 5 | Autoevaluación del equipo (la clase pide asignar E5 en grupo, diapositiva 43): el equipo se declara muy motivado con el proyecto. Indicadores verificables: trabajo sostenido en el repositorio durante 12 días con actividad entre el 2026-09-01 y el 2026-10-08, con aportes de tres integrantes distintos, y una entrega continua de artefactos (subdocumentos, anexos y estimación). Se refleja en el sd-01 (`80_Artefactos/sd-01_contexto/notas_sd-01.md`, N-01) | Extremo. El historial de git no prueba por sí solo la motivación de los siete integrantes; el equipo puede sumar un hecho propio (por ejemplo, asistencia a las reuniones del proyecto) |
| E6 Estabilidad de requisitos | 2 | 2 | Hay 5 RF por validar, metas del Anexo D por validar con el cliente y decisiones abiertas (pregunta 8) | Coherente con el repositorio |
| E7 Personal a tiempo parcial | −1 | 0 | Supuesto del equipo: todo el personal asignado es de dedicación exclusiva. No se respalda con un hecho porque la dotación y la dedicación son del sd-12, que no forma parte de este avance | Extremo sin respaldo: **supuesto declarado**. Si el sd-12 muestra personal a tiempo parcial, el valor sube (E7 en 3 suma 11,9 % de horas) |
| E8 Dificultad del lenguaje | −1 | 3 | Lenguajes comunes, pero unas 30 tecnologías y tres alternativas sin decidir (`contexto_sd-04.md`, D-12) | Puede subir si se complica el stack |

**Resultado con los valores informados.** Suma ponderada = 17,5 + 4 = 21,5. **EF = 1,4 − 0,03 × 21,5 = 0,755**: el trabajo cuesta un 24,5 % menos que con un equipo neutro. Hay un solo factor desfavorable (E6 en 2), así que el factor de conversión es **20 horas por punto**. La puerta se cumple: ocho valores entre 0 y 5, E7 y E8 con el signo correcto, no todos en 3 ni en 5, y EF entre 0,42 y 1,70. El esfuerzo está en `10_esfuerzo.md` y la prueba `05_Gestion/tests/test_ef.py` guarda estos valores.

**Lo que queda por cerrar.**
1. **E1 en 5.** La justificación está redactada con el sd-01; el sd-06 debe describir el modelo híbrido y la Tabla 1 de credenciales del sd-01 (no está en el borrador) debe confirmar las certificaciones de gestión. Si no se sostiene, E1 baja a 4.
2. **E7 en 0** queda como supuesto declarado, sin respaldo, hasta que exista el sd-12. Debe constar así en la memoria de cálculo.
3. **E5 en 5.** La justificación es una autoevaluación con indicadores verificables; el equipo puede agregar un hecho propio.
4. **Coherencia de E6 con el plan de riesgos (sd-08)** cuando exista.
5. **La firma del equipo** sobre los ocho valores.

## 4. Rango y escenarios ilustrativos

Con UUCP 709 y TCF 1,19 (`08_tcf.md`), el tamaño sin EF es 843,7 puntos. La primera fila son los valores informados por el usuario; los demás escenarios muestran cómo cambia el esfuerzo y **no son valores asignados**.

| Escenario ilustrativo | EF | Factores desfavorables | CF (h/punto) | UCP | Programación E (h) | Total del proyecto (h) |
| :-- | --: | --: | --: | --: | --: | --: |
| **Equipo (valores informados, sección 3)** | **0,755** | **1** | **20** | **637** | **12.740** | **31.850** |
| Mejor posible (E1 a E6 en 5; E7 y E8 en 0) | 0,425 | 0 | 20 | 359 | 7.172 | 17.929 |
| Favorable (E1 a E6 en 4; E7 en 1; E8 en 2) | 0,710 | 0 | 20 | 599 | 11.981 | 29.952 |
| Neutro (los ocho en 3) | 0,995 | 0 | 20 | 839 | 16.790 | 41.975 |
| Algo exigente (E1 y E6 en 2; E7 en 4; el resto en 3) | 1,130 | 3 | 28 | 953 | 26.695 | 66.737 |
| Peor posible (E1 a E6 en 0; E7 y E8 en 5) | 1,700 | 8 | no estima | 1.434 | | |

Dos observaciones:

1. **El salto del CF pesa más que el EF.** Pasar de 2 a 3 factores desfavorables cambia las horas por punto de 20 a 28. En el escenario «algo exigente» el EF sube solo de 0,995 a 1,130 (+14 %), pero el total sube de 41.975 a 66.737 horas (+59 %).
2. **Efecto de cada factor.** Desde el escenario neutro, subir un factor de 3 a 5 mueve el EF así: E1 −9,0 %, E2 −3,0 %, E3 −6,0 %, E4 −3,0 %, E5 −6,0 %, E6 −12,1 %, y E7 y E8 +6,0 % cada uno. Los que más conviene discutir son E6, E1 y el cruce con el CF.

Las horas son del desarrollo del software con la lectura B. No incluyen lo que el método no cubre (migración, infraestructura, capacitación, marcha blanca, operación), que se estima aparte en el paso 7.

## 5. Pruebas de la puerta (paso 5)

Cuando el equipo asigne los valores se comprobará: ocho valores entre 0 y 5, E7 y E8 con el signo correcto, no todos en 3 ni todos en 5, justificación de cada 0 y cada 5, y EF entre 0,42 y 1,70. La calculadora `estimacion_ucp.py` ya aplica la regla de Karner y se niega a estimar con 5 o más factores desfavorables.
