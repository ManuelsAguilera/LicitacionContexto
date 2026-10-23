# Guion de la Presentación 2

**Licitación TFEP-01/2026 · Caso 09 Multitiendas Ancoa S.A. · Only Simple Solutions**
**Deck:** `OSS-Presentacion-2-Licitación-Ancoa.pdf` (26 láminas) · **Duración:** 20 minutos de exposición, luego preguntas.

Fuente de las cifras: los PDF vigentes de `02_Propuesta/latex_final/OSS-Informe 2/Informe 2/`. Entre corchetes va la referencia para responder si preguntan; no se lee en voz alta.

---

## 1. Consolidado de la presentación

| Bloque | Láminas | Contenido | Tiempo | Acumulado | Asignado | Suplente |
| :--- | :--- | :--- | ---: | ---: | :--- | :--- |
| B1 · Apertura y correcciones | 1 a 5 | Portada, índice, resumen de correcciones, Subdocumento 3 y esquema de solución | 4:30 | 4:30 | | |
| B2 · La solución | 6 a 11 | Arquitectura lógica (2), arquitectura física, cartera de innovaciones (3) | 4:00 | 8:30 | | |
| B3 · EDT y esfuerzo | 12 a 14 | Quince ramas, esfuerzo por cuenta, reparto 30 / 24 / 46 % | 3:00 | 11:30 | | |
| B4 · Planificación e hitos | 15 a 18 | Cronograma de 56 meses, curva de esfuerzo, hitos H1 a H12, ruta crítica | 4:00 | 15:30 | | |
| B5 · Riesgos y cierre | 19 a 26 | Escalas, matriz, críticos y altos, R-12, R-01, R-33, Monte Carlo y reservas, cierre | 4:30 | 20:00 | | |

**Si se suman Alex y Samira (6 o 7 personas):**
- B2 se divide en B2a, la arquitectura (láminas 6 a 8, 2:35), y B2b, las innovaciones (láminas 9 a 11, 1:25).
- B5 se divide en B5a, con el método, la matriz y los críticos y altos (láminas 19 a 21, 2:00), y B5b, con las fichas, las reservas y el cierre (láminas 22 a 26, 2:30).

**Reglas para el relevo:**
- Quien termina dice la frase de traspaso y nombra a quien sigue.
- Quien sigue no repite la idea anterior y entra directo a su lámina.
- Cada bloque tiene un suplente que conoce su guion.

Ritmo de referencia: 130 palabras por minuto. Los textos de abajo están dentro de ese ritmo. Conviene ensayarlos en voz alta, no memorizarlos palabra por palabra.

---

## 2. Guion por lámina

### B1 · Apertura y correcciones (4:30)

**Lámina 1 · Portada (0:20)**
> Buenos días. Somos Only Simple Solutions y venimos a presentar el segundo informe de nuestra propuesta para Multitiendas Ancoa. Les contamos qué corregimos del primer informe, cómo organizamos el trabajo, cómo lo planificamos dentro de los 56 meses del contrato y qué riesgos vemos, con la forma en que los vamos a gestionar.

**Lámina 2 · Índice (0:15)**
> El orden es este: correcciones, estructura del trabajo, planificación con sus hitos y, al final, los riesgos. La solución la mostramos dentro de las correcciones, porque es la parte que más cambió.

**Lámina 3 · Resumen de correcciones (1:00)**
> El primer informe recibió observaciones en todos los subdocumentos, y las respondimos una a una en el Formulario T-22. Esta tabla muestra el cambio principal en cada subdocumento.
> El Subdocumento 1 incorpora el Formulario T-6, el organigrama y las certificaciones. El 2 se reorganizó en torno a las cuatro promesas que hoy Ancoa no logra cumplir y sus causas.
> El 3 bajó de 203 a 44 páginas, porque la matriz de cumplimiento salió del cuerpo y pasó a su propio formulario. En el 4 la arquitectura física se hizo de nuevo, y el 5 ahora trae un diccionario de datos y la migración por olas.
> En innovaciones cambiamos la cartera completa: las cinco del primer informe eran decisiones de arquitectura que las Bases ya exigían.

*Señalar:* la columna «Cambio principal». [T-22: 124 observaciones, 118 respondidas y 6 pendientes declaradas]

**Lámina 4 · Subdocumento 3, antes y después (0:50)**
> Tomamos el Subdocumento 3 como ejemplo. El primer informe tenía un solo diagrama, que mostraba el estado actual de Ancoa y no la solución. La matriz de cumplimiento tenía 171 respuestas «No» sin explicación.
> Ahora el alcance está separado por etapa y los servicios por frente: Retail, la frontera y la filial emisora. Cada servicio indica en qué etapa entra y qué sistemas del Cliente se conservan. La matriz tiene una leyenda de cuatro estados y cada fila dice en qué sección se respalda.

**Lámina 5 · Esquema de solución (2:05)**
> Este esquema resume la propuesta y se lee de izquierda a derecha.
> A la izquierda están las cuatro promesas que hoy Ancoa no cumple bien, cada una con su cifra actual. La diferencia de inventario es de 12,4 %, cuando la meta es bajo 2 %. El precio cobrado distinto del exhibido llega a 11 %. Las entregas a tiempo son 81 %. La evaluación de crédito en caja tarda entre 40 segundos y 3 minutos.
> La causa es común: el mismo dato se escribe en varios sistemas sin una fuente oficial, y hay 14 conexiones punto a punto entre 9 plataformas de 6 proveedores. A eso se suma que la frontera entre la tienda y el negocio de crédito no está clara.
> En la solución cada dato tiene un solo dueño. El paso entre el comercio y la filial emisora es uno solo, el control de cruces, que deja registro de cada consulta y su finalidad.
> La entrega es en dos etapas, con producción en el mes 16 y en el mes 21, y después vienen 36 meses de operación. El resultado se mide con las mismas metas con que empezamos.
>
> *Traspaso:* «[Nombre] les muestra ahora cómo está construida la solución.»

### B2 · La solución (4:00)

**Lámina 6 · Arquitectura lógica, capas (0:50)**
> Esta vista organiza el software en las ocho capas que piden las Bases y se lee de izquierda a derecha. Las personas entran por los canales, pasan por un único acceso público y por una puerta de enlace, y llegan a los servicios de negocio.
> En azul está lo que construimos, en verde lo que es de Ancoa y en naranja lo que pertenece a terceros. La línea roja es el único cruce autorizado entre Retail y la filial emisora. Cada frente tiene sus propios datos y su propia puerta de enlace.

**Lámina 7 · Arquitectura lógica, servicios (0:45)**
> Aquí se ven los servicios de cada frente. Mercadería tiene oferta, abastecimiento y existencias; Venta tiene pedidos, ventas, comisiones y marketplace; Relación con el cliente tiene posventa y clientes.
> Cada servicio escribe solo en sus propios datos. Si otro servicio necesita esa información, consume sus eventos o llama a su contrato; nunca lee su base directamente. Así se elimina la causa de que hoy el mismo producto tenga existencias distintas en cada sistema.

**Lámina 8 · Arquitectura física (1:00)**
> La carga principal corre en la nube, en Azure Chile Central, repartida en tres zonas de disponibilidad. La recuperación ante desastres está en Brazil South.
> En las tiendas y en los centros de distribución queda equipamiento local. Cada tienda tiene un nodo que permite vender hasta 24 horas sin enlace y que, al volver la conexión, sincroniza sin perder documentos.
> El modelo es híbrido, como exige el artículo 16. Los datos de la filial emisora van en una red y una suscripción separadas de las de Retail.

**Lámina 9 · Innovaciones, antes y después (0:30)**
> En innovaciones reemplazamos toda la cartera. Las cinco del primer informe eran decisiones de arquitectura que el caso ya pedía. Las nuevas cinco son de distinto tipo y ninguna es requisito de las Bases.

**Láminas 10 y 11 · Las cinco innovaciones (0:55)**
> La primera son los lockers Ancoa 24/7, para retirar compras fuera del horario del mesón. La segunda es el conteo cíclico predictivo, que ordena los conteos según el riesgo de diferencia y apunta directamente al 12,4 %.
> La tercera es la búsqueda por foto o por descripción en el canal digital. La cuarta es una red de medios, donde los proveedores pagan por promocionar sus productos. La quinta es el Modo Tienda, con fila virtual para los probadores.
> El conteo predictivo entra con la Etapa 1, y las otras cuatro con la Etapa 2.
>
> *Traspaso:* «[Nombre] explica cómo se descompone todo este trabajo.»

### B3 · EDT y esfuerzo (3:00)

**Lámina 12 · Quince ramas (1:15)**
> La estructura de desglose del trabajo tiene quince ramas. Están agrupadas en cuatro bloques: gestionar, construir, asegurar y poner en servicio.
> Aplicamos la regla del 100 %: todo lo comprometido está en alguna rama, también la seguridad, la capacitación, la documentación y la operación de los 36 meses. Las quince ramas suman 164 cuentas de control.
> Las ramas no siguen las fases de un proyecto genérico, sino lo que Ancoa necesita. Hay una rama completa para migrar y sanear datos, que incluye la cartera viva de 620.000 clientes, otra para las integraciones con los sistemas que se conservan y otra para las marchas blancas con su aceptación por etapa.
> Cada rama tiene un entregable principal, un criterio de aceptación y un responsable. Por ejemplo, migración de datos entrega la cartera migrada y conciliada, y responde el Líder de Datos. El detalle de las 164 cuentas está en el Formulario T-14.

**Lámina 13 · Esfuerzo planificado (1:15)**
> El esfuerzo total es de 40.946 horas hombre. El desarrollo de software, la rama 1.5, se descompone en 127 paquetes, uno por caso de uso, y suma 12.116 horas.
> Cada paquete de software tiene un criterio de aceptación: superar los escenarios acordados del caso de uso, las pruebas de integración y seguridad, y los umbrales de su cuenta. El Líder de Desarrollo responde por el paquete, el Líder de Calidad verifica la evidencia y la Contraparte Técnica de Ancoa acepta.
> Las innovaciones tienen su propia rama. Cada una se divide en siete paquetes de implementación y uno de seguimiento durante la operación, lo que da 40 paquetes. Los 35 de implementación tienen holgura cero, porque cada innovación termina justo con su hito de aceptación.

**Lámina 14 · Reparto del esfuerzo (0:30)**
> Visto en proporciones, el software es el 30 % del esfuerzo y las innovaciones el 24 %. El 46 % restante corresponde a diseño, datos, seguridad, calidad, implantación y operación.
> Esto refleja el problema de Ancoa: lo difícil no es programar, sino migrar, integrar, certificar y poner en servicio sin detener las tiendas ni el crédito.
>
> *Traspaso:* «[Nombre] muestra cómo se ordena este trabajo en el tiempo.»

### B4 · Planificación e hitos (4:00)

**Lámina 15 · Cronograma de 56 meses (1:00)**
> El cronograma respeta el del artículo 17. La Etapa 1 se desarrolla entre los meses 1 y 12, tiene marcha blanca entre el 13 y el 15, y entra en producción en el mes 16, abril de 2028. La Etapa 2 se desarrolla entre los meses 13 y 18 y entra en producción en el mes 21, septiembre de 2028. Después vienen 36 meses de operación, hasta el mes 56.
> Agregamos dos objetivos internos: retirar la plataforma de crédito de 2011 en el mes 22 y cerrar la remediación en el mes 24, antes de que termine su soporte en 2029.

**Lámina 16 · Distribución del esfuerzo (0:45)**
> Esta curva muestra las horas de cada mes. El máximo de la implementación es de 2.493 horas, en el mes 16, y coincide con el hito más expuesto: la Etapa 1 entra en producción mientras la Etapa 2 sigue en construcción. En la operación el máximo es de 365 horas, en el mes 22. Esa coincidencia del mes 16 es la que vuelve a aparecer en los riesgos.

**Lámina 17 · Hitos de aceptación (1:00)**
> Son doce hitos y cada uno se acepta con una evidencia concreta, no por llegar a una fecha. En la Etapa 1, H1 es la línea base, H3 los ambientes operativos, H5 la certificación y H7 la producción en el mes 16. En la Etapa 2 están H8, el diseño, H10, la certificación, y H12, la producción y la aceptación final en el mes 21.
> Los hitos coinciden con los del Formulario E-25.

**Lámina 18 · Ruta crítica (1:15)**
> Esta es la red de actividades a nivel agregado, calculada con CPM. En rojo está la ruta crítica, que llega a H7 y a H12 con holgura cero. Eso significa que cualquier atraso en esa cadena mueve un hito contractual.
> Solo hay margen en tres lugares: tres meses en el plan de marcha blanca y en la capacitación de administradores de la Etapa 1, y un mes en los de la Etapa 2.
> Como no hay holgura en lo que importa, el control del plazo se apoya en los riesgos, que vemos a continuación.
>
> *Traspaso:* «[Nombre] presenta los riesgos.»

### B5 · Riesgos y cierre (4:30)

**Lámina 19 · Escalas y zonas (0:40)**
> Calificamos cada riesgo por probabilidad e impacto, y la multiplicación da su exposición. Sobre 0,40 el riesgo es crítico y obliga a cambiar el diseño o a escalarlo al Comité Ejecutivo. Si un evento atrasa un hito sin holgura, su impacto se califica como muy alto.
> El registro tiene 37 riesgos, mirados desde la solución, el desarrollo y la implantación.

**Lámina 20 · Matriz (0:30)**
> La matriz los distribuye así: 3 críticos, 11 altos, 21 medios y 2 bajos. Los tres críticos tienen la misma calificación: probabilidad 0,60 e impacto 0,80.

**Lámina 21 · Críticos y altos (0:45)**
> Estos son los 14 que exigen respuesta dentro del plan. Los tres críticos son el evento anual con un servicio a medio desplegar, la marcha blanca dentro de los congelamientos y la cartera que no alcance a migrar antes de retirar la plataforma de 2011.
> Dos de ellos, R-02 y R-13, siguen en 0,32 después de la respuesta. No los escondemos: quedan bajo seguimiento del Comité Ejecutivo.

**Lámina 22 · R-12, implantación (0:40)**
> Un ejemplo por cada mirada. En implantación está R-12: la marcha blanca de la Etapa 1 cae casi entera en los congelamientos de Ancoa. Lo evitamos certificando en Preproducción en el mes 12, desplegando entre el 7 y el 24 de enero y corrigiendo en la ventana de marzo. La exposición baja de 0,48 a 0,16.

**Lámina 23 · R-01, solución (0:30)**
> En la solución está R-01: una diferencia de saldos al migrar la cartera expondría a la filial ante la CMF. Por eso el corte se hace por tramos, con conciliación diaria y un criterio de detención acordado con la filial.

**Lámina 24 · R-33, desarrollo (0:25)**
> En el desarrollo está R-33: entre los meses 13 y 15 el mismo equipo sostiene la marcha blanca y construye la Etapa 2. La respuesta es nivelar la carga y reforzar el equipo en ese período.

**Lámina 25 · Monte Carlo y reservas (0:45)**
> Simulamos 10.000 veces el efecto de los riesgos sobre los hitos. Con las respuestas aplicadas, el percentil 80 indica una exposición de 12,2 semanas antes del mes 16. Como el hito no se mueve, esa cifra no es una fecha nueva: es el atraso que tenemos que recuperar con capacidad adicional.
> Para eso reservamos 3.688 horas de contingencia, sobre las 40.946 del plan base. Los riesgos que no están en el registro se cubren con una reserva de gestión, que solo libera el Comité Ejecutivo.

**Lámina 26 · Cierre (0:15)**
> En síntesis, corregimos lo observado, ordenamos el trabajo en 164 cuentas con responsable y atamos el plazo a riesgos medidos. Muchas gracias; quedamos atentos a sus preguntas.

---

## 3. Preguntas probables del profesor y respuestas

Formato: **pregunta** · *qué falla busca* · respuesta para decir · [respaldo].

### Correcciones

1. **¿Están resueltas todas las observaciones del Informe 1?**
   *Busca:* que digamos «todas» sin serlo.
   No. De 124 observaciones, 118 tienen respuesta y 6 quedan pendientes, declaradas como tales en el T-22. Son el Formulario T-8, la acreditación de socio de Microsoft, los sectores sin proyecto en la experiencia, el plan de comunicación a los clientes de la cartera con el re-sellado de firmas, y el folio. Las del T-8 y el equipo corresponden al Subdocumento 12, que no forma parte de este informe.
   [T-22, filas G-8, 1-14, 1-15, 1-16, 4-35 y 5-16]

2. **El T-12 sigue teniendo muchos «No». ¿No era esa una observación?**
   *Busca:* «No» mudos.
   La observación era que los «No» no tenían explicación. Ahora la leyenda tiene cuatro estados, y cada «No» indica en qué subdocumento se completa, porque varios requisitos pertenecen a capítulos del Informe 3, como operación, calidad y equipo. No es un incumplimiento declarado.
   [T-12, introducción; contar los «No» antes de citar una cifra]

3. **¿Por qué el Subdocumento 3 bajó de 203 a 44 páginas? ¿Sacaron contenido?**
   *Busca:* pérdida de alcance.
   No sacamos contenido. 130 de esas páginas eran la matriz T-12 metida dentro del cuerpo, que ahora es un formulario aparte. El catálogo y las reglas de negocio pasaron a los Anexos B y C.
   [T-22, fila 3-10; Subdocumento 3, Anexos B y C]

4. **La merma: ¿son cinco causas o seis?**
   *Busca:* inconsistencia entre documentos.
   El Subdocumento 5 registra las cinco causas del caso: pérdida física, daño no registrado, error de recepción, devolución mal reintegrada y error de digitación. El T-22 menciona una sexta, la unidad mal ubicada; eso hay que corregirlo para que coincida con el Subdocumento 5.
   [Subdocumento 5, 5.1.3; T-22, fila 5-6. **Pendiente del equipo: corregir el T-22 antes de entregar.**]

### Solución y arquitectura

5. **¿Por qué Azure y por qué Chile Central con Brazil South?**
   *Busca:* elección sin fundamento.
   Chile Central mantiene los datos en el país y ofrece tres zonas de disponibilidad. Brazil South es la región más cercana con servicios equivalentes para recuperarse de un desastre, a una distancia que evita amenazas comunes. La decisión y su alternativa descartada están en la decisión de arquitectura ADR-07.
   [Subdocumento 4, 4.1.1, 4.3.1 y 4.3.2]

6. **¿Cómo garantizan la separación entre la tienda y el negocio de crédito?**
   *Busca:* la línea roja del caso.
   Cada negocio tiene sus propios datos, su propia puerta de enlace, su propia red y su propia suscripción. El único paso entre los dos es el control de cruces, que exige una finalidad aprobada, entrega solo los datos mínimos y deja registro de cada cruce. Por omisión, todo cruce se niega.
   [Subdocumento 4, 4.1, Tabla 4.13; Subdocumento 5, dominio Frontera]

7. **¿Qué pasa si una tienda pierde el enlace?**
   *Busca:* la autonomía de 24 h que antes tenía tres cifras distintas.
   El nodo local permite vender, cobrar y consultar hasta 24 horas sin enlace. Al volver la conexión, sincroniza sin perder documentos. Lo comprobamos con un corte provocado de 24 horas en una tienda piloto.
   [T-22, fila G-7; Subdocumento 3, 3.4.5]

8. **¿Es una arquitectura de microservicios? ¿Puede operarla el equipo?**
   *Busca:* complejidad excesiva.
   Son servicios por dominio de negocio, cada uno dueño de sus datos, no microservicios llevados al extremo. Para reducir la operación propia usamos servicios gestionados de la nube: base de datos, mensajería y Kubernetes administrado.
   [T-22, fila 4-16; Subdocumento 4, 4.1.1]

9. **¿Qué pasa con los 14 enlaces punto a punto actuales?**
   *Busca:* reemplazo «big bang».
   Cada uno se reemplaza por un adaptador con contrato, y los sistemas actuales conviven con los nuevos durante la transición. El retiro se hace por etapa y siempre con la posibilidad de volver atrás.
   [Subdocumento 3, 3.2; Subdocumento 4, vista de integración]

### EDT

10. **¿Por qué todas las innovaciones tienen exactamente 7 + 1 paquetes? Parece una plantilla.**
    *Busca:* descomposición genérica.
    Las cinco siguen el mismo ciclo: diseño, construcción, pruebas, instalación y aceptación, más un seguimiento del beneficio en operación. Lo que cambia es el contenido y la duración de cada paquete, que va de uno a cinco meses según la innovación. Las horas también son distintas: 2.336 en el conteo predictivo y 1.784 en Retail Media.
    [T-14, Tabla T-14.10 y red T-14.18; T-15, Tablas T-15.9 a T-15.13]
    *Ojo:* el informe no nombra los siete paquetes en texto. Si piden el detalle, hay que decir que está en la red del T-14 y el cronograma del T-15, no inventar nombres.

11. **¿Cómo verifican la regla del 100 %?**
    *Busca:* trabajo fuera de la EDT.
    Cada requisito del catálogo y cada obligación del contrato está trazada a una cuenta de control del T-14. Además, la suma de las cuentas cuadra con el total de horas: 40.946.
    [Subdocumento 7, 7.1; T-15, Tabla T-15.3]

12. **¿Por qué las innovaciones son el 24 % del esfuerzo? ¿No es mucho para algo opcional?**
    *Busca:* desproporción.
    Las Bases obligan a presentar cinco innovaciones, cada una con arquitectura, EDT y medición de su resultado. El esfuerzo incluye construirlas, ponerlas en servicio y hacer su seguimiento hasta el mes 56, y está dimensionado para un piloto. Si se amplía la cobertura, se actualiza.
    [T-15, «Las cargas corresponden al piloto dimensionado»]

13. **¿Quiénes son el líder funcional, el de desarrollo y el de integración? No aparecen en el organigrama del Subdocumento 1.**
    *Busca:* equipo incoherente con las actividades, un requisito explícito de este informe.
    El Subdocumento 1 muestra las jefaturas de área. Los líderes funcional, de desarrollo y de integración responden por ramas de la EDT, y su dotación nominal se detalla en el Subdocumento 12.
    [**Debilidad real.** Conviene agregar esos tres roles al apartado 1.5 antes de la entrega.]

### Planificación y CPM

14. **¿Usaron CPM o PERT?**
    *Busca:* que se confundan.
    CPM para la red y las holguras. PERT solo para el esfuerzo, con tres valores por rama. La incertidumbre del plazo la medimos con Monte Carlo sobre los riesgos.
    [Subdocumento 7, 7.3.3; Subdocumento 8, Tabla 8.8]

15. **¿Por qué la red está agregada y no tiene las 164 cuentas?**
    *Busca:* red de juguete.
    La red agregada muestra la ruta que define los hitos contractuales. La secuencia completa, con sus dependencias entre cuentas y paquetes, está en el Formulario T-14, Tabla T-14.18.
    [T-14, Tabla T-14.18; Subdocumento 7, 7.3.3]

16. **Si la ruta crítica tiene holgura cero, ¿cómo absorben un atraso?**
    *Busca:* plan sin colchón.
    De tres maneras. Hay márgenes en el plan de marcha blanca: tres meses en la Etapa 1 y uno en la Etapa 2. Hay ventanas de corrección fuera de los congelamientos, en enero y en marzo de 2028. Y está la reserva de 3.688 horas, que el jefe de proyecto activa por disparador.
    [Subdocumento 8, 8.3, «Reserva de contingencia»]

17. **El pico de carga del mes 16 coincide con el hito más expuesto. ¿No es un error de planificación?**
    *Busca:* sobreasignación.
    Es una consecuencia del solapamiento que imponen las Bases: la Etapa 2 empieza en el mes 13, mientras la Etapa 1 está en marcha blanca. Lo identificamos como el riesgo R-33 y lo respondemos con nivelación y refuerzo, en la cuenta 1.11.3.
    [Subdocumento 8, R-33; T-15, Tabla T-15.7]

18. **¿Por qué retirar la plataforma de 2011 en el mes 22 y no después?**
    *Busca:* fecha arbitraria.
    El soporte de esa plataforma termina en 2029, y el último corte de la cartera tiene que caer antes de los congelamientos de fin de año. El mes 22 deja la remediación cerrada en el mes 24, con margen frente a esa fecha.
    [Subdocumento 8, R-13; Caso 09, numeral 7.3]

### Riesgos

19. **¿Por qué eligieron R-01 y R-33 como ejemplos si R-02 y R-13 son más graves?**
    *Busca:* elegir los ejemplos cómodos.
    Mostramos uno por cada mirada. R-02 y R-13 aparecen en la tabla de críticos con su residual de 0,32 y están escalados al Comité Ejecutivo. R-02 se responde con ocho semanas sin despliegues antes del evento anual. R-13 se responde con la secuencia de cortes fijada desde el mes 16, con el último antes del 15 de octubre de 2028.
    [Subdocumento 8, 8.3, «Respuesta a los riesgos críticos»]

20. **Con respuestas, el P80 da 12,2 semanas de atraso en el mes 16. ¿Entonces no cumplen el hito?**
    *Busca:* contradicción entre el plan y el riesgo. **Es la pregunta más probable.**
    El hito es contractual y no se mueve. Las 12,2 semanas no son una fecha nueva: son la exposición en plazo que hay que recuperar. Se recupera con la reserva de capacidad, con las ventanas de corrección y con el escalamiento al Comité Ejecutivo cuando la exposición supera lo recuperable. El mismo Subdocumento 8 declara que el valor esperado no garantiza por sí solo absorber ese percentil, y por eso cada activación recalcula la red.
    [Subdocumento 8, 8.2 después de la Tabla 8.8, y 8.3]

21. **¿Por qué R-02 y R-13 se «mitigan» o «evitan» si quedan en zona alta?**
    *Busca:* estrategia mal nombrada.
    La estrategia describe la acción: R-13 se evita al fijar la secuencia antes de que ocurra el atraso. El impacto, en cambio, sigue en 0,80 por la regla del hito, así que la exposición no puede bajar de 0,32 si la probabilidad solo baja a 0,40. Por eso no se aceptan en silencio: se escalan.
    [Subdocumento 8, 8.3]

22. **¿De dónde salen las 3.688 horas?**
    *Busca:* cifra inventada.
    Es el valor esperado residual de los 14 riesgos críticos y altos, es decir, la probabilidad residual por las horas que costaría cada evento. No se mezcla con la reserva de 15 % para deuda técnica ni con la de 30 % para estabilización.
    [Subdocumento 8, 8.3; T-15, «Reserva de contingencia de riesgos»]

23. **¿Cuánto vale la reserva de gestión?**
    *Busca:* montos en el sobre técnico.
    Su valor está en la oferta económica. El sobre técnico no lleva cifras monetarias.
    [Subdocumento 8, «Reserva de gestión»; Bases Administrativas, art. 50.2]

### Innovaciones

24. **¿No son también requisito los lockers o la búsqueda vectorial?**
    *Busca:* que se repita el error del Informe 1.
    No. El caso exige retiro en tienda y un buscador; lo que proponemos va más allá. El retiro sin pasar por el mesón y fuera del horario, y la búsqueda por foto o por intención, se comparan contra esa base, con su línea base y su meta.
    [Subdocumento 13, introducción y fichas; T-19]

25. **Retail Media genera ingresos. ¿Dónde están los números?**
    *Busca:* montos fuera de lugar.
    El impacto se describe con indicadores, y su valorización va en la oferta económica, como piden las Bases.
    [Subdocumento 13, 13.4; Bases Administrativas, art. 30.1]

### Equipo y forma

26. **¿Por qué 16 personas en el pico y solo 3 en operación?**
    *Busca:* subdotación de la operación.
    Son personas equivalentes calculadas a partir de las horas. En operación el soporte de primer nivel y la mesa de servicio se dimensionan en el Subdocumento 10, que va en el Informe 3. La dotación nominal por rol se concilia con el Subdocumento 12.
    [T-15, Tabla T-15.2]

27. **¿Qué parte de este trabajo hizo la inteligencia artificial?**
    *Busca:* la declaración exigida.
    Cada subdocumento cierra con una declaración de uso de IA, con su herramienta, su finalidad, su nivel de uso y la revisión humana. Lo consolidamos en el Formulario A-6.
    [T-22, fila G-1]

---

## 4. Observaciones al deck antes de exponer

No se modificó el PDF. Estas son cosas que el profesor puede notar:

1. **El índice no calza con el orden de las láminas.** Pone «04 · La solución» después de la planificación, pero la solución se muestra en las láminas 5 a 11, dentro de las correcciones. Conviene mover ese ítem al segundo lugar o fusionarlo con «Correcciones».
2. **La numeración se repite:** 4, 4, 5, 5, 5, 6, 6, 6. Es mejor que sea correlativa.
3. **La portada dice «Septiembre de 2026».** Debería decir octubre de 2026.
4. **Quedaron fuera dos láminas que las Bases piden para este informe:**
   - la tabla de trazabilidad observación, respuesta y sección modificada (art. 46; la tenemos en el T-22);
   - el equipo, que debe ser «coherente con las actividades».
   Ambas estaban en el pptx generado. Si no entran por tiempo, conviene tenerlas como respaldo para las preguntas 1 y 13.
5. **La lámina 14 dice «Todo lo demás 18.942 HH».** Al sumar 12.116, 9.888 y 18.942 se obtienen 40.946, así que la cifra es correcta. «Todo lo demás» suena coloquial; puede decir «Resto de las ramas».
