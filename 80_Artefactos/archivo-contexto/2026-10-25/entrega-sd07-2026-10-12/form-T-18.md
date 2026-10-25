# Anexo --- Formulario T-18: Implantación y puesta en marcha controlada

Licitación N.° TFEP-01/2026
Multitiendas Ancoa S.A.
Only Simple Solutions

## Objeto

Este anexo acompaña al Subdocumento 7 y describe cómo la solución pasa a producción sin cortes bruscos y con retorno ensayado. La implantación se ordena en una estrategia de despliegue por oleadas, la puesta en servicio separada de cada etapa, el plan de convivencia entre ambas, las pruebas que respaldan cada paso a producción, las condiciones de cierre de cada marcha blanca, el procedimiento de reversión y la aceptación por hito.

La implantación respeta el cronograma de 56 meses del artículo 17 de las Bases Administrativas. La Etapa 1 se desarrolla entre los meses 1 y 12, su marcha blanca ocupa los meses 13 a 15 y pasa a producción en el mes 16. La Etapa 2 se desarrolla entre los meses 13 y 18, su marcha blanca ocupa los meses 19 y 20 y pasa a producción en el mes 21, junto con la aceptación final y el inicio de la Operación, que se extiende hasta el mes 56.

La correspondencia con enero de 2027 a agosto de 2031 es un supuesto de planificación de la oferta. El mes 1 corresponde al primer mes completo de ejecución desde el inicio del contrato, según el artículo 10. Una vez fijada esa fecha, el calendario se comprobará contra los congelamientos del caso sin desplazar las anclas contractuales. Los hitos se relacionan con el Formulario E-25.

## Estrategia de despliegue

El despliegue avanza por oleadas y separa el despliegue de la liberación. Un cambio puede quedar instalado sin estar visible para la persona usuaria hasta que la liberación lo habilita, mediante banderas de función y activación gradual por tienda, por canal y por segmento de usuarios. Esta separación permite instalar, verificar y, si hace falta, retirar un cambio sin exponerlo a la operación real.

- Piloto. El punto de venta nuevo se prueba en tres tiendas en los meses 6 y 7, con acompañamiento en el puesto de trabajo y medición diaria de indicadores. Es un piloto técnico en preproducción aislada dentro de la tienda; la operación vigente sostiene las ventas y conserva el registro oficial. Incluye el ensayo de corte de enlace de 24 horas, sin interrumpir la conectividad ni la venta de la operación vigente. Toda intervención en el sitio se programa en una ventana libre de congelamiento, una vez aceptadas las condiciones de infraestructura de H3. Con el supuesto de inicio en enero de 2027, si el evento anual ocupa la ventana prevista de junio, el piloto se ejecuta en julio dentro del mes 7. La selección de tiendas y categorías se documenta con su volumen, conectividad y posibilidad de retorno; la propuesta no supone una selección ya aprobada por el Cliente. La operación real supervisada corresponde a los meses 13 a 15 y el paso a producción, al mes 16.
- Sustitución progresiva. El punto de venta de 2014 se sustituye tienda por tienda después del cierre conforme de la marcha blanca y desde el paso a producción del mes 16, con retorno probado disponible durante cada ventana.
- Pasos a producción. La Etapa 1 pasa a producción en el mes 16 y la Etapa 2 en el mes 21, cada uno tras el cierre conforme de su marcha blanca.
- Degradación controlada. El orden de degradación de funciones y las ventanas de congelamiento se aplican durante toda la implantación, sin nuevas liberaciones funcionales dentro de un congelamiento. La atención de incidentes utiliza contención y retorno previamente ensayados, sin convertir la urgencia en autorización para ampliar el alcance.

La implantación se apoya en la plataforma de integración y entrega continuas de la rama 1.4 y en el principio de una sola fuente de verdad para los datos compartidos. El despliegue se ensaya primero en los ambientes habilitados y observables de la rama 1.4, y solo después se libera a producción, de modo que todo paso a producción llega con su configuración probada y con su reversión disponible.

### Modalidad por componente y controles del Capítulo 6

Los servicios de nube se liberan mediante azul-verde, conservando la versión anterior disponible durante la observación. En tiendas se libera primero en una tienda como canario y después por oleadas autorizadas. El canario pertenece a la liberación del alcance correspondiente y no sustituye el piloto técnico aislado de tres tiendas de M6–7. Cada oleada requiere resultados satisfactorios antes de ampliar su exposición.

El dominio financiero permanece segregado en el entorno local. Sus cambios y migraciones requieren conformidad de datos y seguridad, conciliación por tramo y retorno compatible con las transacciones ya registradas. El despliegue técnico, la habilitación de funcionalidades y la aceptación contractual se registran como decisiones distintas.

La versión candidata E1 se verifica en preproducción antes del 1 de noviembre de 2027, con el inicio supuesto de enero, y se identifica en la entrega H4 de M10. Incluye pruebas de los flujos previstos para marcha blanca y ensayo de retorno. En M11–12 se completa la certificación H5 en ambientes aislados, sin intervenir producción durante el congelamiento. Toda corrección obliga a repetir las pruebas afectadas y registrar la nueva versión. La marcha blanca comienza en la ventana habilitada de M13 después del 6 de enero y antes de vuelta a clases, sin anticipar H7.

El jefe de proyecto reúne las verificaciones de calidad, seguridad, datos, implantación y operación antes de presentar cada liberación al Comité de Proyecto y a la Contraparte Técnica. El Comité de Operación participa mensualmente desde M13, conforme a 6.1.7.

## Puesta en servicio de la Etapa 1

La Etapa 1 se desarrolla entre los meses 1 y 12 y entra en marcha blanca entre los meses 13 y 15. La marcha blanca es operación supervisada con datos y usuarios reales, en convivencia con la operación vigente del Cliente, con plan de reversión activo y medición diaria de indicadores. El paso a producción ocurre en el mes 16, cuando la Etapa 1 pasa a ser el sistema de registro oficial del alcance comprometido.

Con el supuesto de inicio en enero de 2027, la marcha blanca de la Etapa 1 se desarrolla entre enero y marzo de 2028. Coincide parcialmente con el congelamiento navideño, que termina el 6 de enero, y con vuelta a clases, desde la última semana de enero hasta la primera de marzo. Estas ventanas no forman un bloqueo continuo de tres meses. El paquete 1.1.5 registra también la segunda semana de mayo, el evento anual de comercio electrónico durante tres días de mayo o junio y su semana previa, y la última semana de noviembre, incluida en el bloqueo del 1 de noviembre al 6 de enero (Multitiendas Ancoa S.A., 2026, Caso 09, cap. 13, núm. 13.2, p. 29).

Los ambientes, mecanismos de convivencia y procedimientos de retorno se preparan y ensayan antes de la marcha blanca. Durante un congelamiento se mantiene la operación supervisada ya preparada, con conciliación diaria y medición de indicadores, sin introducir nuevas liberaciones funcionales. Los incidentes se atienden mediante los mecanismos de continuidad y retorno previamente ensayados. La capacitación de los usuarios participantes precede a su incorporación; la certificación exigida para el cierre se acredita con el registro del paquete 1.13.3. El plan contempla las incorporaciones de temporada sin exigir intervenciones de producción dentro del congelamiento.

## Puesta en servicio de la Etapa 2

La Etapa 2 se desarrolla entre los meses 13 y 18, en paralelo con la marcha blanca y la estabilización de la Etapa 1. Su marcha blanca ocupa los meses 19 y 20, con la Etapa 1 ya en producción, y su paso a producción ocurre en el mes 21, simultáneo con la aceptación final del proyecto y el inicio de la Operación. Los meses 13 y 14 incluyen el análisis y el diseño detallado cuya aprobación corresponde a H8. La construcción dependiente de esas decisiones comienza tras su aprobación; el trabajo preparatorio explica el inicio contractual de la etapa en el mes 13.

Durante los meses 13 a 15 coinciden el cierre de la Etapa 1 y el desarrollo de la Etapa 2; durante los meses 19 y 20 coinciden la Etapa 1 ya en producción con la marcha blanca de la Etapa 2. El detalle del esfuerzo y del solapamiento está en el Formulario T-15.

## Plan de convivencia entre etapas

El plan de convivencia del paquete 1.11.3 mantiene una única fuente de verdad para los datos compartidos por ambos alcances y evita toda doble digitación. La conciliación y el retorno ensayado de la rama 1.6 sostienen la continuidad entre la Etapa 1 y la Etapa 2. La plataforma de integración y entrega continuas permite subir cambios de forma gradual durante el solapamiento, sin degradar los niveles de servicio comprometidos. La sincronización entre frentes se apoya en los comités del Subdocumento 6 y en el informe mensual de avance, que es el período de reporte de la RT-19.06.

La operación de retail y la operación del emisor de crédito mantienen dominios de datos segregados. La fuente de verdad compartida entre etapas se define por cada entidad y por su dominio autorizado; no supone reunir ambos negocios en una base de datos común. La segregación se verifica con pruebas de acceso y evidencia auditable antes de construir cualquier vista unificada de cliente (Multitiendas Ancoa S.A., 2026, Caso 09, cap. 13, núm. 13.3, condición 7, p. 30).

## Pruebas que respaldan el paso a producción

La Tabla 1 resume las pruebas que condicionan el avance. Sus resultados se incorporan al expediente de certificación de cada etapa y al plan de calidad del Subdocumento 9.

Tabla 1: Pruebas y su alcance. Fuente: Elaboración propia a partir del Caso 09, cap. 13, núm. 13.3, pp. 29–30, y cap. 17, núm. 17.6, p. 43; condiciones técnicas del proyecto.

| **Prueba** | **Alcance** | **Momento** |
| --- | --- | --- |
| Certificación de calidad de la etapa | Pruebas funcionales y de requisitos no funcionales del alcance de la etapa | Antes de cada marcha blanca |
| Desempeño | Carga de 1,5 veces el peak declarado y verificación de los tiempos exigidos | Antes de cada paso a producción |
| Estrés | Incremento de carga hasta identificar el punto de quiebre, degradación y recuperación | Antes de cada paso a producción |
| Resiliencia y recuperación | Recuperación ante desastres y conmutación de componentes | Antes de cada paso a producción |
| Corte de enlace provocado | Operación desconectada de 24 horas con retorno ensayado | En el piloto, antes del paso a producción de la Etapa 1 |
| Seguridad ofensiva | Pruebas de intrusión y remediación de hallazgos | Antes de cada paso a producción |
| Degradación del evento anual | Orden de degradación, suspensión de publicación y continuidad de transacciones | Antes de exponer cada alcance al evento y antes de certificar cada etapa |

La aprobación de H3 acredita los cinco ambientes operativos, incluido recuperación ante desastres, conforme a RT-04.01. Las pruebas de certificación posteriores utilizan esos ambientes. El ensayo de degradación de la cuenta 1.9.5 y sus repeticiones se programan con el calendario del T-14; su aceptación no se posterga hasta el mes 21 si la Etapa 1 debe enfrentar antes los eventos de 2028. Cada año se conserva una versión ensayada antes del congelamiento y se verifica su capacidad con la demanda prevista.

## Criterios de éxito medibles

La puesta en servicio no se declara lograda hasta que los resultados de negocio del capítulo 18 se verifican con evidencia (Multitiendas Ancoa S.A., 2026, Caso 09, cap. 18, pp. 44–45). La medición se hace contra la línea base del levantamiento y se reporta en el informe de resultados de cada marcha blanca. Los resultados que el caso compromete son la exactitud del inventario, la disponibilidad y continuidad de la venta, el cumplimiento de la promesa de entrega, la integridad de la información financiera y la reducción del esfuerzo manual, cada uno con su línea base y su meta.

El registro diario identifica el alcance, las transacciones observadas, la fuente de datos, los fallos y el resultado de cada indicador. Para las funciones presentes en cada etapa se comprueban los umbrales del capítulo 15 del caso, entre ellos consulta de disponibilidad de hasta 400 milisegundos, venta en caja con pago externo de hasta 25 segundos, evaluación crediticia de hasta 8 segundos y propagación del precio de hasta 5 minutos (Multitiendas Ancoa S.A., 2026, Caso 09, cap. 15, RT-09.01, p. 34). La verificación aplica el método y percentil que correspondan según las Bases Transversales y el catálogo de requisitos; una media diaria no sustituye ese criterio. Se registran por separado disponibilidad, latencia y errores de cada servicio.

La cancelación atribuible a disponibilidad se mide como pedidos cancelados por falta de existencia divididos por pedidos confirmados del mismo conjunto de categorías y período. El ensayo compara el resultado antes y después de la intervención antes de extenderla al catálogo. La exactitud del inventario se mide por categoría mediante conteo físico sin cerrar la tienda; el 12,4 % de discrepancia es un antecedente de la situación actual (Multitiendas Ancoa S.A., 2026, Caso 09, cap. 18, resultado 4, p. 44). Ese valor no constituye la meta de aceptación. La conciliación financiera se ejecuta diariamente por cuenta y saldo, y cualquier diferencia no explicada detiene el avance de la migración. El retorno conserva y concilia las transacciones posteriores al corte; restaurar una copia sin ese tratamiento no acredita continuidad.

El volumen real exigido para las últimas cuatro semanas se registra por etapa, tienda, canal y proceso en el plan aprobado antes de su marcha blanca. La volumetría del caso sirve para dimensionar esa propuesta (Multitiendas Ancoa S.A., 2026, Caso 09, cap. 14, núm. 14.1, p. 31). Por ejemplo, 31.000.000 de documentos de venta anuales equivalen a aproximadamente 2.378.082 en 28 días mediante 31.000.000 $×$ 28 / 365; 1.900.000 pedidos en línea equivalen a aproximadamente 145.753 mediante el mismo cálculo. Son referencias medias de toda la compañía, sujetas a estacionalidad, y no cuotas de un piloto de tres tiendas. La cartera contiene 620.000 clientes con saldo, cuyo universo debe conciliarse cuando corresponda su migración. El plan fija la parte de esos universos que cubre cada etapa y las metas de mejora antes de solicitar su aceptación; estos valores no acreditan por sí solos un volumen comprometido o aprobado.

## Condiciones de cierre de cada marcha blanca

Una marcha blanca solo se da por concluida y habilita el paso a producción cuando cumple simultáneamente las seis condiciones del artículo 17.3 de las Bases Administrativas.

- No existen incidentes abiertos de severidad crítica ni alta atribuibles a la solución.
- Se alcanzó el volumen de operación real comprometido, durante al menos las cuatro últimas semanas del período.
- Los indicadores de disponibilidad y de tiempo de respuesta se cumplieron de forma sostenida durante ese mismo período.
- La conciliación entre la solución y el sistema o registro vigente no presenta diferencias no explicadas.
- El personal del Cliente fue capacitado y certificado conforme al plan aprobado, condición que acredita el paquete 1.13.3.
- La Contraparte Técnica suscribió el acta de aceptación correspondiente.

Si al término del período no se satisfacen las condiciones anteriores, la marcha blanca se extiende a costo del adjudicatario, sin cargo adicional para el Cliente y sin desplazar las fechas contractuales de las fases siguientes, con aplicación de las multas por atraso previstas en el artículo 80. La medición de las cuatro últimas semanas debe cubrir también cualquier período adicional que sea necesario para acreditar el cierre.

### Observación y activación del retorno

Antes de exponer una versión, el Líder de Calidad y el Líder de Operación registran los indicadores aplicables, sus umbrales contractuales, el período de observación y las fuentes de medición. Los parámetros quedan asociados a la versión y al alcance de la oleada. Sin esta configuración comprobada no se autoriza la liberación. Un incidente crítico o alto atribuible a la versión, una diferencia financiera no explicada o una vulneración de la segregación bloquean inmediatamente la ampliación.

El retorno automático previsto en 6.2.5 se habilita para cambios de aplicación cuya compatibilidad con los datos haya sido ensayada. Al detectar el incumplimiento configurado, el pipeline detiene la expansión, devuelve el tráfico o la versión al estado anterior y conserva los registros del incidente. El Líder de Operación verifica la recuperación y comunica el resultado al jefe de proyecto. Cuando el retorno afecta datos, el sistema contiene la exposición y el Líder de Datos dirige la conciliación antes de reanudar el servicio afectado. Se preservan las operaciones confirmadas posteriores al corte.

El Líder de Calidad verifica nuevamente los flujos críticos y los indicadores; la Contraparte Técnica recibe la evidencia del incidente y del retorno. Una nueva liberación requiere corregir la causa, repetir el ensayo y obtener la autorización correspondiente. El retorno de una versión se distingue del Plan de Reversibilidad contractual, destinado a transferir la operación al Cliente o a un tercero.

## Procedimiento de reversión

Cada paso a producción exige que el procedimiento de reversión haya sido probado antes. Los mecanismos siguientes cubren la aplicación, los datos y la decisión de retorno.

- Separación entre despliegue y liberación. Desactivar la bandera de función repone el comportamiento anterior sin volver a desplegar.
- Respaldo y retorno de datos. Las bases de datos cuentan con respaldo previo a cada paso y con procedimiento de restauración probado.
- Plan de retorno por componente. El plan del paquete 1.11.1 define el retorno por componente y el umbral que dispara la vuelta atrás.

El Plan de Reversibilidad se entrega dentro de los primeros 90 días del contrato y se actualiza anualmente, de modo que el Cliente o un tercero puedan asumir la operación sin interrupción del servicio. Cada componente crítico se revierte en ambiente controlado antes de que su paso a producción quede habilitado. Desactivar una bandera solo basta cuando el ensayo demuestra que los cambios de datos y las transacciones ya confirmadas conservan su integridad; en los demás casos se ejecuta el retorno por componente y la conciliación correspondiente.

## Aceptación por hito

La Tabla 2 relaciona cada hito de aceptación del Anexo E-25 con su mes, su evidencia de aceptación y el paso de la implantación que habilita. Los hitos del cierre de la marcha blanca y del paso a producción de cada etapa son los que ordenan la puesta en servicio controlada.

Tabla 2: Hitos de aceptación y su evidencia. Fuente: elaboración propia a partir del Anexo E-25.

| **Hito** | **Mes** | **Evidencia de aceptación** | **Paso de la implantación que habilita** |
| --- | --- | --- | --- |
| H1 - cierre del levantamiento, línea base de alcance y matriz de trazabilidad | 2 | Acta de cierre del levantamiento y línea base aprobada | Habilita la arquitectura y el diseño |
| H2 - arquitectura, plan de seguridad y modelo de datos | 4 | Documento de arquitectura y catálogo de decisiones aprobado | Habilita la plataforma y los ambientes |
| H3 - infraestructura híbrida y ambientes con observabilidad | 6 | Cinco ambientes operativos con observabilidad y segregación verificadas | Completa la plataforma para integración, pruebas y piloto |
| H4 - software de la Etapa 1 para pruebas, QA superado | 10 | Software de la Etapa 1 con cobertura de pruebas | Habilita la certificación de la Etapa 1 |
| H5 - certificación de la Etapa 1 | 12 | Certificación de calidad de la Etapa 1 | Habilita el inicio de la marcha blanca de la Etapa 1 |
| H6 - inicio de la marcha blanca de la Etapa 1 | 13 | Inicio de la marcha blanca con reversión activa y usuarios capacitados | Marcha blanca de la Etapa 1 |
| H8 - línea base de alcance de la Etapa 2 y diseño detallado | 14 | Línea base de alcance y diseño de la Etapa 2 aprobados | Habilita la construcción dependiente del diseño aprobado |
| H7 - paso a producción de la Etapa 1 y cierre de la marcha blanca | 16 | Acta de aceptación de la Etapa 1 | Paso a producción de la Etapa 1 |
| H9 - software de la Etapa 2 para pruebas, QA superado | 17 | Software de la Etapa 2 con cobertura de pruebas | Habilita la certificación de la Etapa 2 |
| H10 - certificación de la Etapa 2 y cierre del desarrollo | 18 | Certificación de calidad de la Etapa 2 | Habilita la marcha blanca de la Etapa 2 |
| H11 - inicio de la marcha blanca de la Etapa 2 | 19 | Inicio de la marcha blanca de la Etapa 2 con la Etapa 1 en producción | Marcha blanca de la Etapa 2 |
| H12 - paso a producción de la Etapa 2 y aceptación final | 21 | Acta de aceptación final y garantía de correcto funcionamiento | Paso a producción de la Etapa 2 e inicio de la Operación |

Tras el H12, la Operación se paga con un hito mensual durante los 36 meses de operación (meses 21 a 56). El retiro de la plataforma de crédito de 2011 en el mes 22 y el cierre de la remediación en el mes 24 son objetivos internos anticipados de la oferta. El fin de soporte y el último hito de remediación se sitúan en 2029 (Multitiendas Ancoa S.A., 2026, Caso 09, cap. 13, núm. 13.2, p. 29). El resultado de aceptación exige cumplir los hitos de remediación antes de ese año (Multitiendas Ancoa S.A., 2026, Caso 09, cap. 18, resultado 23, p. 45). Las fechas exactas se confirman durante el levantamiento y se controlan en el registro de restricciones externas. La revisión de esos objetivos internos exige demostrar que conserva los vencimientos externos y las fechas contractuales; su posición en el calendario no prueba una holgura CPM nula.

## Definición del volumen y de las metas de aceptación

El plan de cada marcha blanca registra antes de su inicio el volumen real por proceso y sitio, la línea base, la meta, el método de medición y el responsable de producir la evidencia. El Subdocumento 11 desarrolla el volumen operacional y el Subdocumento 14 los resultados de negocio. La aprobación de ese registro es condición previa al inicio de la marcha blanca. Las medias corporativas no sustituyen las metas de aceptación por proceso y sitio.

## Incorporación de las innovaciones del Subdocumento 13

Conteo cíclico predictivo se evalúa en sombra durante M13–15 y requiere aceptación antes de su uso operativo en M16. Su retorno conserva el conteo base. Lockers, búsqueda multimodal, Retail Media Network y fila virtual se verifican en M19–20 para su habilitación técnica desde M21. Las pruebas y metas particulares se registran en T-19 conforme a las fichas del SD-13, además de cumplir las condiciones comunes de marcha blanca.

Los pilotos dimensionados consideran tres emplazamientos de lockers y tres tiendas con fila virtual. La ampliación se estima por unidad y requiere calendario y recursos adicionales. En lockers se prueban credenciales de uso único y retorno al mesón; en búsqueda, relevancia, disponibilidad y vuelta al buscador base; en publicidad, presupuesto y eventos conciliados, con continuidad del canal orgánico; en fila virtual, accesibilidad, persistencia y ausencia de doble asignación. La publicidad requiere un anunciante para acreditar operación comercial; la capacidad técnica no demuestra ingresos. Los mecanismos de contingencia mantienen el negocio, pero no sustituyen la aceptación del beneficio innovador.

## Coordinación con el CPM y traspaso final

Las entregas parciales del CPM permiten preparar instalación y capacitación con una versión candidata; las pruebas finales y la aceptación exigen completar ambas y superar los criterios de esta sección. El margen cero de los paquetes de innovación no reemplaza las autorizaciones de liberación.

El traspaso 1.14.2 se programa en M48–56 y el acompañamiento final 1.14.5 en M54–56, con inicio efectivo al menos 90 días antes del fin contractual, conforme al artículo 77.2. Se mantienen sus 64 HH: 48 de acompañamiento y 16 de cierre. Esta dedicación parcial requiere verificar suficiencia por rol y no sustituye la continuidad del servicio. La entrega del código por liberación y la custodia semestral exigidas por el artículo 84 siguen vigentes durante todo el contrato. El plan de reversibilidad inicial y sus actualizaciones tampoco se postergan al cierre.

## Referencias

Multitiendas Ancoa S.A. (2026). Bases Técnicas del Caso 09 - Cadena Multitienda. Licitación TFEP-01/2026.

## Declaración de uso de IA

Se utilizó Codex para apoyar la organización del contenido, la comprobación de cálculos y la revisión de redacción. Se aplicaron las pautas de humanizer para conservar un registro formal y retirar expresiones de relleno. La asistencia automatizada no sustituye la aprobación técnica y contractual del proponente.
