# Guía para proponer los entregables de la EDT (sd-07, sección 7.1)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Está escrito para otra IA (o persona) que deba proponer la EDT del proyecto sin irse a los extremos. Ordena qué leer, qué estructura respetar, hasta dónde descomponer y qué errores evitar. **No es fuente de verdad del alcance**: manda `02_Propuesta/latex_final/sd-03.tex` con los Anexos A a D. Si algo de esta guía difiere de ellos, la guía está desactualizada y se avisa.

## 1. Qué se pide y qué no

**Se pide.** Una EDT con el 100 % del alcance, hasta paquetes de trabajo estimables y asignables, y un diccionario con el entregable, el criterio de aceptación y el responsable de cada paquete (Bases Administrativas, T-7, subdocumento 7). La EDT incluye las innovaciones y las actividades de seguridad, calidad, migración e implantación (art. 57.2).

**No se pide en esta tarea.** Horas, costos, fechas, duraciones, dependencias, secuencia ni nombres de personas. Eso pertenece al plan de trabajo, a la nivelación de recursos (Formulario T-15) y al cronograma. En el diccionario, esfuerzo, costo y recursos se escriben «por estimar».

**Ante un vacío.** Si falta un dato, se escribe «por definir» y se agrega la pregunta a la lista del cierre. Nunca se inventa una cifra, un requisito ni una decisión. Lo no decidido se trata como en el sd-03: se declara.

## 2. Fuentes, en orden de prioridad

1. `80_Artefactos/sd-03_contexto/ficha_alcance_sd-03.md`. Resumen vigente del alcance.
2. `80_Artefactos/sd-03_contexto/divisiones_negocio_servicios_sd-03.md`. Nombres y códigos de los servicios. Los códigos antiguos (R-01 a X-01) no se usan.
3. `04_Adjuntos/tablas/sd-03_s2_anexo-a_*.md` (exclusiones, supuestos, responsabilidades del cliente), `anexo-b` (catálogo de 308 requerimientos), `anexo-c` (reglas de negocio) y `anexo-d` (28 criterios de aceptación).
4. Bases Administrativas: art. 14.2 (alcance), 15 a 17 (etapas, 56 meses, marcha blanca), 18 (aceptación), 28 y 29 (innovaciones), 57.2 (coherencia), 77 (transferencia y reversibilidad), Formularios T-14, T-15, T-17, T-18 y E-25.
5. Bases Transversales: capítulo 20 (implantación y aceptación) y capítulo 26 (innovaciones). Comunicado 10, secciones 7.1 y 9.3.
6. `80_Artefactos/sd-13_contexto/informe_candidatas_innovacion.md`. Las cinco innovaciones son candidatas, no decididas.
   `02_Propuesta/latex_final/sd-03.tex`, secciones 3.3 y 3.4 (integradas por otro integrante, aún sin commit y con hallazgos de forma pendientes: figuras, numeración de tablas y referencias; el recuento de nueve plataformas ya quedó corregido). Definen qué hacen abastecimiento, ventas y posventa y describen los recorridos de punta a punta. Se tratan como «propuesta pendiente de integrar».
   `80_Artefactos/maestro_actores.md` (borrador). Roles y sistemas que interactúan con la solución, con nombres canónicos.
7. Clase FEP02, diapositivas 50 a 60 (EDT).

Precedencia: Bases Administrativas, Bases Transversales, Caso. Una decisión del sd-03 prevalece sobre cualquier borrador anterior. No se usa nada de `80_Artefactos/sd-03_contexto/historico/`.

## 3. Definiciones que no se mezclan

| Término | Qué es | Qué NO es |
| :-- | :-- | :-- |
| Entregable | Producto, resultado o capacidad única y verificable (FEP02, diap. 38) | Una tarea ni una fecha |
| Paquete de trabajo | Entregable del último nivel de la EDT, que no se descompone más | Una actividad |
| Actividad | Trabajo que se hace para producir un paquete. Va en el cronograma | Un nodo de la EDT |
| Hito | Punto del calendario de duración cero con criterio binario | Un entregable ni una fase |
| Etapa | Etapa 1, Etapa 2 y operación (art. 15 a 17) | Un nodo de la EDT. Es un **atributo** de cada paquete |
| Servicio | Pieza del sistema dueña de los datos de un tema (13 servicios) | Un paquete. Un servicio contiene varios |

Regla central. En la EDT solo hay **entregables**. Los nodos intermedios (cada servicio, cada rama) se nombran «Servicio de X» o con el nombre de la rama y agrupan paquetes. La tabla de la EDT lista solo los paquetes, los nodos intermedios se muestran en el código. Las marchas blancas, los pasos a producción y los cierres no son nodos. Sí lo son sus entregables, como el plan de marcha blanca o el informe de cierre (T-18).

## 4. Estructura del primer nivel (propuesta a validar por el equipo)

El primer nivel se arma por entregables y no por fases (FEP02, diap. 54, que recomienda esta orientación). La etapa de cada paquete se marca como atributo. La IA no agrega ni quita ramas sin justificarlo por escrito.

| Código | Rama | Contenido |
| :-- | :-- | :-- |
| 1 | Gestión del proyecto | Gobierno, plan de gestión, control de cambios (art. 72), riesgos, comunicaciones, adquisiciones |
| 2 | Base tecnológica e infraestructura híbrida | Plataforma de integración, identidad y gestión de accesos, observabilidad, nube pública, centro de datos on-premise, componentes de borde, licenciamiento, especificación del hardware de terreno |
| 3 | Servicios de retail | Nueve servicios, numerados 3.1 a 3.9 en el orden de la tabla de nomenclatura. No hay nivel de área en la EDT |
| 4 | Servicios de la filial emisora | Tres servicios, numerados 4.1 a 4.3: originación de crédito, cartera de crédito y evidencia financiera |
| 5 | Frontera | Servicio de control de cruces |
| 6 | Datos, migración e integraciones | Saneamiento y migración (cartera de 620.000 clientes por tramos), mapa y rediseño de las 14 interfaces |
| 7 | Seguridad y cumplimiento | Transversal a todos los servicios: política, modelado de amenazas, controles, pruebas de seguridad |
| 8 | Calidad y pruebas | Plan de calidad y niveles de prueba (aceptación, desempeño, estrés, resiliencia, recuperación ante desastres) |
| 9 | Implantación | Plan de implantación por etapa (T-18), marchas blancas, pasos a producción, reversión, capacitación y gestión del cambio |
| 10 | Innovaciones | Un conjunto de paquetes por cada una de las cinco innovaciones (art. 29, RT-26.02) |
| 11 | Operación y soporte | Mesa de ayuda, mantención correctiva, preventiva y evolutiva, gestión de la infraestructura, durante 36 meses |
| 12 | Transferencia y reversibilidad | Programa de transferencia tecnológica y Plan de Reversibilidad (art. 77) |

Atención al lugar y al momento. La ubicación en la EDT no fija cuándo ocurre. El Plan de Reversibilidad, por ejemplo, va en la rama 12 y se entrega dentro de los primeros noventa días del contrato (art. 77.2). Eso lo dice el atributo de etapa o de plazo, no la rama.

## 5. Hechos que no se pueden contradecir

- Contrato de 56 meses. Etapa 1 con desarrollo en los meses 1 a 12, marcha blanca en los 13 a 15 y producción desde el 16. Etapa 2 con desarrollo en los 13 a 18, marcha blanca en los 19 y 20 y producción desde el 21. Operación del 21 al 56. El mes 1 es enero de 2027 (supuesto SUP-26).
- 13 servicios y una base tecnológica. Etapa 1: oferta comercial, existencias, ventas, originación de crédito, evidencia financiera, control de cruces y la mayor parte de la cartera de crédito. Etapa 2: abastecimiento, pedidos, comisiones, marketplace, posventa, clientes Retail y la segunda parte de la cartera.
- Catálogo de 308 elementos (227 funcionales, 72 no funcionales y 9 obligaciones del proponente), repartidos por servicio en el Anexo B. Un paquete cita el rango de requerimientos que cubre y no los repite.
- Reparto físico (SP-04). El proponente provee el centro de datos on-premise con su conectividad, seguridad y canalizaciones. El cliente adquiere el hardware de tiendas y centros de distribución, ejecuta sus obras y contrata sus enlaces. El proponente los especifica, costea, coordina, certifica y configura.
- Exclusiones y responsabilidades del cliente (Anexo A). Lo excluido no se descompone como trabajo propio. Sí se incluye lo que el Anexo A dice que «sí se hace», como especificar, costear o integrar.
- Autonomía de las tiendas sin enlace: 24 horas. Piloto de punto de venta en tres tiendas. 22 tiendas y 2 centros de distribución.
- Innovaciones: cinco, una por tipo. Hoy son candidatas y cuatro de ellas están por validar. La EDT deja un conjunto de paquetes por cada tipo con el nombre «innovación por definir» si no se ha decidido.

## 6. Reglas de descomposición

**Regla del 100 %.** Todo el trabajo de un nivel inferior suma el 100 % del superior, sin trabajo huérfano ni duplicado (FEP02, diap. 52). Se verifica contra cinco listas: los 13 servicios y la base, el art. 14.2, el art. 77, las cinco innovaciones y los 28 resultados del Anexo D (cada uno debe poder rastrearse a un paquete).

**Dónde detenerse (FEP02, diap. 55 y 56).** El paquete se puede estimar con precisión, tiene un responsable único y se puede medir y dar por terminado. La orientación de 8 a 80 horas es una referencia donde el control lo exige, no una obligación en todos los paquetes. La clase advierte que demasiadas divisiones reducen la productividad de la gestión.

**Profundidad.** Hasta cuatro niveles de código (por ejemplo 3.4.2.1). Si algo necesita más, es una actividad.

**Rangos de control.** Son una heurística de este equipo, no un requisito. Del orden de 5 a 10 paquetes por servicio y 100 a 250 paquetes en total. El mínimo razonable es 2 paquetes por servicio. Un servicio de más de 40 requerimientos funcionales, como existencias con 48, puede superar 10. Un servicio de 3 requerimientos, como abastecimiento o comisiones, puede quedar bajo 5. Si la EDT sale de esos rangos, la IA lo declara y explica por qué. En la prueba de la guía, la rama 3 sola dio 49 paquetes, lo que es coherente con el rango total.

**Conectores.** El conector propio de un servicio (transportistas, remuneraciones, fidelización) va en la rama de ese servicio. El mapa y el rediseño de las 14 interfaces existentes van en la rama 6.

**Un paquete agrupa requerimientos coherentes.** Nunca hay un paquete por requerimiento, por pantalla ni por persona.

**Etapa del paquete.** Es la etapa del servicio al que pertenece. Si un requerimiento no funcional del Anexo B tiene otra etapa (por ejemplo RNF-20 de posventa), se declara la diferencia en el diccionario y no se parte el paquete.

**Atribución de requerimientos no funcionales.** El Anexo B no da servicio a casi ninguno. La IA los asigna por su contenido, lo marca como «asignación propuesta» y lista las asignaciones en el informe de verificación. Los de la base tecnológica (por ejemplo RNF-22, RNF-23, RNF-25 y RNF-28) van a las ramas 2 y 8.

**Nombres.** Un sustantivo que nombra un entregable («Cálculo del disponible con colchón de confianza»), nunca un verbo de actividad («Desarrollar», «Probar», «Coordinar»).

**Pruebas y seguridad.** Todas las pruebas van en la rama 8 y la seguridad en la 7, subdivididas por servicio cuando haga falta. Dentro de un servicio solo van los entregables funcionales y sus conectores. El ensayo de un umbral (por ejemplo el orden de degradación del evento anual) se nombra en la rama 8 y se cita desde el servicio. No se repite el mismo entregable en dos ramas.

**Ejemplo con el servicio de existencias** (requerimientos del Anexo B).

| Nivel | Ejemplo | Por qué |
| :-- | :-- | :-- |
| Demasiado grueso | «Desarrollo del servicio de existencias» | No se puede estimar ni medir |
| Demasiado fino | «Crear la pantalla de registro de conteo» | Es una actividad |
| Adecuado | «Cálculo del disponible con colchón de confianza» (RF-127 a RF-130) | Entregable verificable y estimable |
| Adecuado | «Programación y registro de conteos cíclicos» (RF-131 a RF-137) | Agrupa requerimientos coherentes |
| Adecuado | «Clasificación e informe mensual de merma» (RF-138 a RF-141) | Se acepta con el resultado 5 del Anexo D |

## 7. Los extremos que hay que evitar

| Extremo | Cómo se ve | Corrección |
| :-- | :-- | :-- |
| Demasiado grueso | Un paquete por servicio, «Desarrollo», «Pruebas», «Implantación» | Bajar hasta entregables estimables |
| Demasiado fino | Tareas, pantallas, un paquete por requerimiento o por persona | Subir al entregable que agrupa |
| Genérico | Paquetes válidos para cualquier proyecto (las Bases lo evalúan «con severidad») | Citar el servicio, el requerimiento o la regla del caso |
| Con secuencia | Fechas, duraciones, flechas, horas o costos | Quitarlos. La EDT no es un cronograma (FEP02, diap. 53) |
| Fases como entregables | «Etapa 1», «Marcha blanca» como nodos | Dejar la etapa como atributo. Los entregables sí van |
| Duplicación | El mismo entregable en un servicio y en calidad | Dejarlo en una rama |
| Alcance ajeno | Incluir lo excluido o lo que hace el cliente como trabajo propio | Revisar el Anexo A |
| Alcance olvidado | Sin seguridad, calidad, migración, implantación, innovaciones u operación | Revisar la tabla de cobertura (sección 8) |
| Datos inventados | Cifras de esfuerzo, plazos o costos sin fuente | «Por estimar» |
| Nombres antiguos | Códigos R-01 a X-01 o «plataforma común» | Usar la nomenclatura vigente |

## 8. Cobertura obligatoria

| Exigencia | Rama de la EDT |
| :-- | :-- |
| Arquitectura lógica, física, de datos, de integración, de seguridad y de despliegue (art. 14.2) | 2, con el detalle de cada servicio en 3 a 5 |
| Construcción y configuración del software, servicios de integración y componentes de borde | 2 a 5 |
| Infraestructura en nube y on-premise, y licenciamiento a nombre del cliente | 2 |
| Especificación del hardware de terreno y de los dispositivos | 2 |
| Migración, saneamiento y validación de datos históricos, e integraciones | 6 |
| Pruebas unitarias, de integración, de sistema, de aceptación, de carga, de estrés, de resiliencia, de recuperación ante desastres y de seguridad ofensiva | 8 (por servicio) y 7 (seguridad) |
| Implantación, marcha blanca, paso a producción y estabilización (T-18, RT-20) | 9 |
| Protocolo de aceptación de cada hito (T-17) y definición de terminado (RT-20.07) | 9 |
| Gestión del cambio, capacitación certificada por perfil y rol | 9 y 12 |
| Soporte, mantención y operación durante 36 meses | 11 |
| Documentación, código fuente, scripts de infraestructura, base de conocimiento y manuales (art. 77.1) | 12 |
| Plan de Reversibilidad (art. 77.2) | 12 |
| Cinco innovaciones, con paquetes y mes (art. 29, RT-26.02) | 10 |
| Obligaciones del proponente OP-01 a OP-05 (etiquetas electrónicas, alternativa evaluada y costeada) | Servicio de oferta comercial |
| OP-06 y OP-07 (especificación de dispositivos móviles) | 2, con el hardware de terreno |
| OP-08 y OP-09 (análisis de Concepción e impacto sobre RN-15) | Servicio de existencias, salvo que el equipo decida la rama 2 |
| Actividades de calidad (Comunicado 10, 9.3) | 8 |

## 9. Formato de salida

**Tabla de la EDT** (cinco columnas como máximo).

| Código | Nombre del entregable | Origen | Etapa | Criterio de aceptación |
| :-- | :-- | :-- | :-- | :-- |
| 3.3.1 | Cálculo del disponible con colchón de confianza | Servicio de existencias, RF-127 a RF-130 | 1 | Hecho observable con umbral, tomado del Anexo B o D. Si no existe, «por definir» |

La etapa admite 1, 2, 1 y 2, operación, «desde el inicio del contrato» o «por definir». La columna Origen cita el servicio y el rango de requerimientos del Anexo B. Los paquetes que no tienen requerimientos (porque el Anexo B declara un vacío o porque el alcance es una exclusión «sí se hace») citan la exclusión, la obligación del proponente (OP) o la nomenclatura, y se listan aparte en el informe de verificación para que el equipo decida si el vacío se llena en el catálogo. Las referencias obsoletas del catálogo (RF-160, RF-161, RF-183) se citan tal cual y se listan en las preguntas abiertas.

El criterio de aceptación es una frase con un hecho observable y, si lo hay, un umbral. Se toma del Anexo B (umbrales no funcionales) o del Anexo D (28 resultados), no se inventa.

**Diccionario por paquete** (campos de la clase, diap. 57).
- Código y nombre. Descripción del trabajo, con lo que queda fuera. Entregable (el artefacto concreto: componente, documento o evidencia; no repite el nombre). Criterio de aceptación.
- Responsable, siempre como **rol** (por ejemplo «líder técnico del Servicio de X», con un rol de apoyo si hace falta, y «Contraparte Técnica» para la aceptación). Nunca nombres propios. La lista de roles definitiva depende del sd-12 y del Formulario T-15, de modo que mientras tanto se usa «líder técnico del servicio» y se anota la pregunta.
- Hitos asociados. Se escribe «por definir con el E-25».
- Referencias, es decir los requerimientos, reglas y resultados del Anexo D que cubre.
- Supuestos. Esfuerzo, costo y recursos: «por estimar (T-15)».

## 10. Proceso en cinco pasos (FEP02, diap. 59)

1. **Identificar** los entregables principales por rama, con las cinco listas de la regla del 100 %.
2. **Estructurar** el primer nivel con la tabla de la sección 4.
3. **Descomponer** cada rama hasta paquetes, con los rangos de la sección 6.
4. **Codificar** con códigos jerárquicos únicos de hasta cuatro niveles.
5. **Verificar**: aplicar la lista de control de la sección 11. Los pasos se repiten hasta que la verificación pase.

Al cerrar, la IA entrega la EDT, el diccionario y un **informe de verificación** con el resultado de cada control, las desviaciones de los rangos con su justificación y las preguntas abiertas.

## 11. Lista de control

1. ¿Cada uno de los 13 servicios y la base tecnológica tiene paquetes, y cada paquete cita su rango de requerimientos?
2. ¿Los 28 resultados del Anexo D se pueden rastrear a un paquete?
3. ¿Aparece cada elemento de la tabla de cobertura de la sección 8?
4. ¿Hay un conjunto de paquetes por cada una de las cinco innovaciones?
5. ¿Ningún nodo es una fase, un hito o una actividad?
6. ¿Ningún nombre empieza con un verbo?
7. ¿No hay fechas, meses, horas de esfuerzo, costos, duraciones de trabajo ni dependencias? (Los umbrales de desempeño del Anexo B y D, como «5 minutos» o «24 horas», sí son válidos en el criterio de aceptación.)
8. ¿Ningún entregable aparece en dos ramas?
9. ¿Nada excluido ni a cargo del cliente figura como trabajo propio?
10. ¿Cada paquete tiene un responsable único, expresado como rol?
11. ¿Todo criterio de aceptación sale del Anexo B o D, o dice «por definir»?
12. ¿El total y los paquetes por servicio caen en los rangos, o se justifica?
13. ¿Se usaron solo los nombres y códigos vigentes?
14. ¿Hay alguna cifra sin fuente?

## 12. Preguntas abiertas para el equipo

- ¿Se validan las doce ramas del primer nivel o se agrupan algunas, por ejemplo calidad con seguridad?
- ¿Cómo se reflejan los hitos de pago del Formulario E-25 en los paquetes? Hoy se dejan «por definir».
- ¿Quién asume la gestión del cambio organizacional y la capacitación (equipo propio o subcontratado)? Depende del sd-12.
- ¿Cuántos tramos tendrá la migración de la cartera? El sd-03 no lo fija y condiciona los paquetes de la rama 6.
- ¿Qué innovaciones se confirman? Condiciona la rama 10.
- Abastecimiento (3 RF), comisiones (3) y cartera (6) tienen pocos requerimientos en el Anexo B. Ventas (14) y posventa (12) sí tienen catálogo. La sección 3.3.2 de `sd-03.tex` define abastecimiento (órdenes, transferencias, propuestas de reposición y recepciones), ventas (ventas, pagos, reversas y registros de caja, incluidas las operaciones sin enlace) y posventa (cambios, devoluciones, retracto y garantía, con notas de crédito vía ERP/DTE). Los paquetes de los servicios con pocos requerimientos que dependan de esa definición se marcan «alcance según 3.3.2, sin requerimientos» hasta que el catálogo se complete.
- ¿Qué roles hay además del líder técnico de cada servicio? Los roles del cliente (jefaturas de tienda, Logística, Cumplimiento, Emisor) salen del maestro de actores. Los roles del proponente dependen del sd-12.
- ¿El Anexo B puede agregar una columna de servicio a los requerimientos no funcionales?
- ¿El nivel de detalle de los servicios de la Etapa 2 es el mismo que el de la Etapa 1? Los de la Etapa 2 se precisarán con menos información, y la clase acepta refinar la EDT a medida que el alcance se precisa (diap. 59).
