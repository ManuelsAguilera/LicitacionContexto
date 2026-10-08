# Factores de ambiente (EF): preguntas para el consenso del equipo (paso 5, puerta G5, parte de ambiente)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: **sin valores asignados**. Los ocho factores describen al equipo y a su contexto, y los asigna el equipo por consenso (FEP03, diapositivas 42 a 45), no el proponente de la estimación. Dependen del sd-04 (pila tecnológica), del sd-06 (metodología) y del sd-12 (equipo), que todavía no están redactados. Este documento deja las preguntas, el rango posible y un cuadro de escenarios ilustrativos para que el equipo vea cuánto pesa cada respuesta. Los escenarios no son una propuesta de valores.

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
| 1 | Todos | ¿Quién asigna los valores y cómo? | Hay siete integrantes (AGENTS.md) | Una sola reunión con todo el equipo. Cada persona anota su valor antes de discutir. Se registran los desacuerdos, porque la clase los considera el mejor diagnóstico (diapositiva 46) |
| 2 | Todos | ¿Cuándo se asignan? | El sd-04, el sd-06 y el sd-12 no están redactados | Esperar a que existan al menos la pila tecnológica, la metodología y la dotación. Mientras tanto, usar solo el rango de la sección 3 y marcar el resultado como provisional |
| 3 | E1 | ¿Qué modelo de gestión usará el proyecto y cuántos del equipo lo han aplicado? | La metodología es del sd-06, sin redactar | Valorar solo la experiencia real de las personas con ese modelo, no la intención de usarlo. Si el sd-06 combina dos modelos, valorar el más débil |
| 4 | E2 | ¿Cuánto conoce el equipo el negocio de una cadena multitienda con crédito propio? | El conocimiento viene de las Bases, el Caso y las clases; no hay experiencia declarada del proponente en el rubro | Valorar por experiencia previa documentable (proyectos, trabajo en retail o banca), no por lo leído en el Caso. Si nadie la tiene, el valor es bajo y se declara |
| 5 | E3 | ¿Cuánto domina el equipo la orientación a objetos con el lenguaje elegido? | El lenguaje y el marco se fijan en el sd-04 | Preguntar a cada integrante cuántos proyectos hizo con objetos. Tomar la mediana, no el mejor |
| 6 | E4 | ¿Quién es el analista líder y qué experiencia tiene en ese rol? | El líder del proyecto figura en AGENTS.md; el rol de analista se fija en el sd-12 | Valorar al analista que de verdad llevará los casos de uso. Si el rol se reparte, valorar el promedio |
| 7 | E5 | ¿Qué tan motivado está el equipo con este proyecto? | Sin datos en el repositorio | Responder de forma anónima, con una escala de 1 a 5 por integrante. Tomar la mediana |
| 8 | E6 | ¿Cuán estables son los requisitos? | Hay 5 RF de clientes Retail por validar; metas del Anexo D marcadas «propuesta del proponente» por validar con el cliente; decisiones abiertas (portal del proveedor, evaluación de AS-04, factibilidad de EXC-16); los vacíos del catálogo (conciliación contable, retención de bitácora, buró de crédito, administración de reglas de comisión) | Dar un valor medio o bajo mientras esas decisiones sigan abiertas. Revisar la coherencia con el plan de riesgos del sd-08: si este dice que el alcance puede cambiar, E6 no puede valer 5 (diapositiva 45). Un cambio de 2 puntos en E6 mueve el esfuerzo en cerca de 12 % |
| 9 | E7 | ¿Cuántas personas del equipo del proponente trabajarán a tiempo parcial? | El sd-12 fija la dotación; las 46 personas del cliente (RC-09) acompañan, pero no son el equipo del proponente | Contar solo al equipo del proponente. Si el equipo tiene otras obligaciones (estudios u otro trabajo), declararlo, porque es el factor que más sorprende después |
| 10 | E8 | ¿Qué tan difícil es el lenguaje y el conjunto de herramientas del sd-04? | La pila no está fijada; el despliegue híbrido y la arquitectura de nube exigen varias herramientas | Valorar el conjunto (lenguaje, nube, mensajería, pruebas), no solo el lenguaje. Un entorno muy nuevo para el equipo sube el valor |
| 11 | CF | ¿Se informa siempre el escenario de 28 horas por punto? | La convención C3 ya lo decide | Sí. El CF es el parámetro más sensible del método (+40 %); se informa el escenario base y el de 28 horas, con la regla de Karner declarada |
| 12 | Todos | ¿Cómo se justifican los valores extremos? | La clase exige justificar los 0 y los 5 (diapositivas 40 y 45) | Una frase por cada 0 o 5, con un hecho comprobable. No copiar valores de otro proyecto |

## 3. Rango y escenarios ilustrativos

Con UUCP 709 y TCF 1,19 (`08_tcf.md`), el tamaño sin EF es 843,7 puntos. Los escenarios muestran cómo cambia el esfuerzo; **no son valores asignados**.

| Escenario ilustrativo | EF | Factores desfavorables | CF (h/punto) | UCP | Programación E (h) | Total del proyecto (h) |
| :-- | --: | --: | --: | --: | --: | --: |
| Mejor posible (E1 a E6 en 5; E7 y E8 en 0) | 0,425 | 0 | 20 | 359 | 7.172 | 17.929 |
| Favorable (E1 a E6 en 4; E7 en 1; E8 en 2) | 0,710 | 0 | 20 | 599 | 11.981 | 29.952 |
| Neutro (los ocho en 3) | 0,995 | 0 | 20 | 839 | 16.790 | 41.975 |
| Algo exigente (E1 y E6 en 2; E7 en 4; el resto en 3) | 1,130 | 3 | 28 | 953 | 26.695 | 66.737 |
| Peor posible (E1 a E6 en 0; E7 y E8 en 5) | 1,700 | 8 | no estima | 1.434 | | |

Dos observaciones:

1. **El salto del CF pesa más que el EF.** Pasar de 2 a 3 factores desfavorables cambia las horas por punto de 20 a 28. En el escenario «algo exigente» el EF sube solo de 0,995 a 1,130 (+14 %), pero el total sube de 41.975 a 66.737 horas (+59 %).
2. **Efecto de cada factor.** Desde el escenario neutro, subir un factor de 3 a 5 mueve el EF así: E1 −9,0 %, E2 −3,0 %, E3 −6,0 %, E4 −3,0 %, E5 −6,0 %, E6 −12,1 %, y E7 y E8 +6,0 % cada uno. Los que más conviene discutir son E6, E1 y el cruce con el CF.

Las horas son del desarrollo del software con la lectura B. No incluyen lo que el método no cubre (migración, infraestructura, capacitación, marcha blanca, operación), que se estima aparte en el paso 7.

## 4. Pruebas de la puerta (paso 5)

Cuando el equipo asigne los valores se comprobará: ocho valores entre 0 y 5, E7 y E8 con el signo correcto, no todos en 3 ni todos en 5, justificación de cada 0 y cada 5, y EF entre 0,42 y 1,70. La calculadora `estimacion_ucp.py` ya aplica la regla de Karner y se niega a estimar con 5 o más factores desfavorables.
