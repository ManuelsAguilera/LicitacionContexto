# Informe de normalización de observaciones del Informe 1

**Licitación ficticia TFEP-01/2026 · Caso 09 Cadena Multitienda · Only Simple Solutions**  
**Fecha:** 2 de octubre de 2026  
**Uso:** contexto de revisión y rúbrica interna para preparar la siguiente entrega; no es un subdocumento T-7 ni reemplaza los formularios oficiales.

## 1. Objeto, fuentes y alcance

Este informe convierte las críticas constructivas de la revisión recibida en condiciones de cierre comprobables por subsección. La fuente es el PDF de 26 páginas `G09-C09-MULTITIENDA-ONLY SIMPLE SOLUTIONS - Revision Informe 1.pdf`, conservado por el usuario en `Downloads`; su [transcripción por página](revision_informe_1_transcripcion.md) tiene SHA-256 `8ffc2e2ebddc8bfa8dab269ba43e978068cf8f6a944a0a7b6fbe22a017850f3c`. Las referencias `p. N` de este informe apuntan a **páginas del PDF de revisión**, no a los folios de los subdocumentos revisados.

Se contrastaron las reglas estructurales con el [Comunicado 10](../00_Bases/Comunicado_10_Estructura_Propuestas_Preparatorias_y_Tecnica_Final.md), la autonomía con las [Bases Administrativas](../00_Bases/Bases_Administrativas.md) y [Transversales](../00_Bases/Bases_Transversales.md), y los umbrales del caso con [Caso 09](../00_Bases/Caso_09_Cadena_Multitienda.md). Rige la precedencia establecida en `AGENTS.md`. El Comunicado 10 complementa el T-7 y T-21 y fija el índice obligatorio de cada capítulo.

La revisión describe **los documentos entregados como Informe 1**, no certifica que cada problema siga presente en los archivos actuales. En particular, los maestros de `02_Propuesta/` todavía contienen una estructura provisional distinta del Comunicado 10. Esta rúbrica usa los **títulos y números oficiales del Comunicado 10** y no modifica esos maestros ni sus estados. Antes de marcar un criterio como resuelto, se debe comprobar el contenido vigente y registrar la revisión humana.

El PDF afirma un puntaje global de **43,8** y remite a una “tabla final”, pero esa tabla no figura en sus 26 páginas. El dato se registra sólo como **afirmación del revisor**; no se recalculan puntajes ni ponderaciones. Los porcentajes del T-21 siguen pendientes de cotejo con la tabla oficial reparada.

## 2. Lectura ejecutiva

La revisión reconoce una cadena técnica sólida: problema y supuestos → módulos → zonas de despliegue → entidades de datos, con separación entre retail y emisor fiscalizado; destaca el ATP con colchón por categoría y punto, la decisión de adelantar la habilitación de la migración crediticia, los escenarios sin enlace y la separación entre precio vigente y vitrina (PDF pp. 9–10, 12–14, 19–20, 25–26). Estos aciertos deben conservarse y explicarse mejor, no perderse al corregir la forma.

Los riesgos de cierre más altos son cuatro: **(1)** la matriz T-12 declara numerosos `No` sin interpretación ni evidencia coherente; **(2)** la arquitectura física omite región de nube, emplazamientos completos y Formulario T-11; **(3)** existen decisiones contradictorias sobre autonomía sin enlace, propagación de precios, merma y conservación de evidencia; **(4)** las cinco innovaciones se presentan como novedad aunque la revisión las considera cumplimiento del piso obligatorio (PDF pp. 9–12, 14–19, 21–25). La ausencia de formularios, acreditaciones, declaración de IA, foliación y lectura humana de cierre agrava esos problemas.

**Prioridades:** `P0` = condición que puede afectar admisibilidad, requisito obligatorio o contradicción central; `P1` = contenido, cálculo o evidencia sustantiva exigida; `P2` = presentación, trazabilidad editorial o claridad. Son prioridades **internas de trabajo**, no puntajes oficiales.

**Escala interna por criterio:** `0` = ausente o contradictorio; `1` = mencionado sin evidencia suficiente; `2` = desarrollado con evidencia, pero aún no conciliado entre capítulos/formularios; `3` = comprobado en la versión ensamblada y validado por una persona. `No aplica` requiere justificación escrita bajo el título obligatorio. La escala no se convierte en puntaje T-21. Un `P0` sólo se considera cerrado en nivel `3`.

**Regla de aceptación de cada criterio:** sólo se marca `cumplido` cuando existe una ruta al texto o formulario final, la evidencia indicada, una comprobación contra Bases y una persona que registró la revisión. `Pendiente`, `redactado` o `Sí` en T-12 sin evidencia no cierran un criterio. El Informe 2 debe incluir una tabla `ID de observación → respuesta → sección/archivo modificado → evidencia → revisor`, conforme al Art. 45.º de las Bases Administrativas.

## 3. Rúbrica transversal de todos los subdocumentos

### TR-01 · Índice, presentación y entrega — P0

- [ ] Conservar **todos los títulos, números y orden** del Comunicado 10, con introducción bajo cada capítulo y texto explicativo antes de tablas o figuras. Separar subdocumento, anexos y cada formulario en archivos propios; usar la nomenclatura oficial al exportar. **Cierre:** índice y archivos finales cotejados uno a uno con el Comunicado 10. **Origen:** PDF pp. 1–3, 9, 13, 17–18; Comunicado 10, reglas 1–3 y 11.
- [ ] Entregar PDF con texto seleccionable, encabezado identificable, versión y fecha coherentes, índice paginado, folio correlativo y firma según la instancia. **Cierre:** revisión visual de todas las páginas del documento ensamblado y comprobación formal del Art. 40.º. **Origen:** PDF pp. 1–3, 18, 26; Comunicado 10, regla 9.
- [ ] Declarar el carácter ficticio donde lo exige la instancia y el uso real de IA: sección final por subdocumento después de Referencias y consolidación en A-6. No atribuir revisión humana que no ocurrió. **Cierre:** secciones de declaración completas, A-6 coherente y T-22 de la instancia revisado. **Origen:** PDF pp. 1, 3, 25–26; Bases Administrativas Art. 13.5; Comunicado 10, regla 7.

### TR-02 · Integridad editorial y fuentes — P0

- [ ] Eliminar del texto de oferta rastros del proceso de edición (`usuario`, `hallazgo H-`, `borrador previo`, `esta pasada`, `Paso 9`), marcadores y referencias a anexos, figuras, requisitos o secciones inexistentes. **Cierre:** búsqueda de términos y validación manual de **cada** remisión, sin falsos positivos de notas de trabajo. **Origen:** PDF pp. 1–3, 15, 18, 21, 24–26; Comunicado 10, regla 7.1.
- [ ] Mantener una sola versión de nombres de módulos, proveedor, regiones, ADR, RF/RNF, tablas, fechas, autonomías, retenciones y umbrales en todos los capítulos y formularios. **Cierre:** matriz de decisiones compartidas y lectura integral por una persona. **Origen:** PDF pp. 2, 11–12, 25–26; Comunicado 10, regla 3.
- [ ] Citar fuentes externas y Bases en el lugar de uso, con Referencias al final de cada subdocumento; distinguir dato del caso, cálculo propio y supuesto. Ninguna cifra sin origen o memoria de cálculo. **Cierre:** trazabilidad bidireccional cita–referencia y recálculo de cifras relevantes. **Origen:** PDF pp. 3, 5–8, 23–24; Comunicado 10, reglas 3 y 6.
- [ ] Usar tablas para comparar o dimensionar y texto para explicar decisiones; citar y explicar cada figura antes y después de mostrarla. **Cierre:** diagramas legibles sin ampliar, texto de al menos 9 puntos en exportación y sin capítulos dominados por listados. **Origen:** PDF pp. 8–9, 13, 16–18; Comunicado 10, reglas 4–5.

### TR-03 · Matriz de cumplimiento y respuesta a observaciones — P0

- [ ] Revisar **cada** RT del T-12 contra la evidencia vigente: `Sí` requiere sección y prueba suficiente; `No` requiere una explicación expresa de incumplimiento o de alcance de la instancia, usando sólo los estados admitidos por el formulario oficial. No usar un `No` mudo para contenido aún no presentado. **Cierre:** conteos conciliados con el T-12 final y revisión de filas críticas como RT-03.01, RT-03.10, RT-05.01, RT-05.29, RT-07.02 y RT-12.02–04. **Origen:** PDF pp. 9, 11–12, 25–26.
- [ ] Resolver las observaciones de esta revisión en la siguiente instancia con respuesta, sección modificada y evidencia objetiva. **Cierre:** tabla de trazabilidad completa y sin observaciones huérfanas. **Origen:** Bases Administrativas Art. 45.º y 47.1; PDF pp. 3–24.
- [ ] Mantener precios, tarifas y montos de la oferta fuera del Sobre Técnico; en innovaciones describir el impacto económico sin revelar valores de la oferta. **Cierre:** control de separación de sobres. **Origen:** PDF pp. 1, 23–24; Bases Administrativas Art. 50.2; Comunicado 10, reglas 3 y 8.

## 4. Rúbrica por subsección oficial

### Capítulo 1 · Presentación de la empresa

#### 1.1 Presentación de la empresa

- [ ] **S1-01 · P1.** Dar razón social simulada, año de fundación, domicilio, líneas de negocio, productos y servicios, y relacionar cada capacidad con evidencia de proyectos o dotación. Evitar sectores declarados sin caso verificable. **Cierre:** ficha corporativa consistente con el resto de la oferta y sin datos inventados presentados como reales. **Origen:** PDF pp. 3–4.

#### 1.2 Estructura Organizacional

- [ ] **S1-02 · P1.** Presentar organigrama legible y dotación por área, diferenciando capacidad permanente y equipo asignado al contrato. **Cierre:** organigrama explicado y cifras conciliadas con T-8/Capítulo 12. **Origen:** PDF p. 4; Comunicado 10, índice 1.2.

#### 1.3 Gobierno interno Calidad, Seguridad y Conocimiento

- [ ] **S1-03 · P1.** Explicar políticas, instancias, responsables y evidencia de gestión de calidad, seguridad y conocimiento. Separar prácticas “alineadas con” una norma de certificaciones institucionales efectivamente obtenidas. **Cierre:** cada afirmación de cumplimiento o acreditación tiene documento, vigencia y responsable o se formula como plan. **Origen:** PDF pp. 4–5; Comunicado 10, índice 1.3.

#### 1.4 Experiencia y Certificaciones

- [ ] **S1-04 · P0.** Completar el Formulario T-6 en archivo propio con los campos oficiales: proyecto, mandante ficticio, período, monto de contrato cuando corresponda al formulario, alcance, SLA comprometido y alcanzado, modalidad híbrida y contraparte de la simulación. Identificar el proyecto que acredita híbrido y el que acredita disponibilidad ≥99,5 %. **Cierre:** T-6 cotejado con Art. 34.º y citado desde 1.4; no atribuir una experiencia simulada a una empresa real. **Origen:** PDF pp. 3, 5.
- [ ] **S1-05 · P0.** Acreditar cada certificación institucional realmente declarada. Si las Bases permiten un plan para ISO/IEC 27001, presentar sus hitos; comprobar separadamente la exigencia de ISO 9001 vigente. No presentar PCI DSS o una alianza comercial como certificación obtenida sin soporte. **Cierre:** certificados, emisor, código verificable y vigencia, o declaración corregida. **Origen:** PDF p. 4.
- [ ] **S1-06 · P2.** Dar referencias pertinentes a las normas y cerrar el capítulo con síntesis de capacidad para este contrato; revisar la coherencia entre las 12 h offline declaradas en experiencia y la autonomía comprometida para Ancoa. **Origen:** PDF p. 5.

#### 1.5 Estructura para Proyecto

- [ ] **S1-07 · P1.** Mostrar estructura de gobierno, dedicación por rol y período, y cobertura de arquitectura, nube, integración/migración, DBA, seguridad, calidad, operación y mesa de servicio. Remitir las fichas del equipo nominado al Capítulo 12 y al T-8, sin duplicarlas. **Cierre:** organigrama del proyecto y matriz de dedicaciones coherentes con el cronograma de 56 meses. **Origen:** PDF pp. 3–4; Comunicado 10, índice 1.5.
- [ ] **S1-08 · P0.** Preparar T-8 y soportes de certificaciones individuales del Cap. 15.3: contrastar el equipo con las categorías mencionadas por la revisión (gestión de proyectos, ITIL 4, gobierno TI, arquitectura de la nube ofertada, seguridad, motor de base de datos y calidad). **Cierre:** cada credencial exigible tiene persona, vigencia y comprobante; faltantes quedan explícitos y resueltos, sin declararlos como obtenidos. **Origen:** PDF p. 4.

#### 1.6 Alianzas

- [ ] **S1-09 · P0.** Declarar un proveedor de nube coherente con la arquitectura y acreditar la condición de socio exigida, con nivel, identificador y vigencia. Distinguir alianza de la empresa y alianza específica del proyecto (12.3). **Cierre:** evidencia externa o documental verificable y consistencia entre 1.6, 4.1.1, 4.3.1 y T-12. **Origen:** PDF p. 4.

### Capítulo 2 · Introducción al Problema y Necesidad

#### 2.1 Resumen Ejecutivo del problema

- [ ] **S2-01 · P1.** Sintetizar el problema con voz propia de Only Simple Solutions: causas, magnitud, actores y consecuencia para la oferta, sin reproducir el preámbulo ni el criterio de evaluación del caso como si fueran análisis original. Este capítulo delimita el problema; el resumen de la solución pertenece a 3.1. **Cierre:** cada párrafo aporta interpretación o derivación y cita el caso cuando usa sus datos. **Origen:** PDF pp. 6–8; Comunicado 10, índice 2.1 y 3.1.

#### 2.2 Comprensión del problema y de la necesidad

- [ ] **S2-02 · P1.** Investigar y explicar con fuentes pertinentes las 15 materias del numeral 16.2 del caso, incluidos ATP y conteo cíclico, costo total de servir, crédito de casa comercial e información precontractual, medios de pago, colas y degradación, lenguaje claro y cobranza. Corregir la referencia al fiscalizador vigente; no usar “SVS/CMF” como entidad actual. **Cierre:** matriz de cobertura 15/15, citas APA 7 en el texto y Referencias correspondientes, con implicaciones concretas para el caso. **Origen:** PDF pp. 6–8.
- [ ] **S2-03 · P2.** Explicar en prosa la relación causal entre las cuatro promesas al cliente y los registros imprecisos; incorporar una figura de contexto o mapa causal legible que se interprete en el texto. **Origen:** PDF pp. 6–8.

#### 2.3 Dimensionamiento del problema

- [ ] **S2-04 · P1.** Calcular magnitudes propias a partir de la volumetría del caso y mostrar fórmula, período, unidad, supuestos y sensibilidad: exposición de las 2.840 cancelaciones, efecto de “cobrar el menor” y carga operativa de 400.000 cambios diarios de precio. No convertir el 11 % de discrepancia muestral en “11 % de multas”. **Cierre:** hoja o tabla de cálculo reproducible, citada desde el texto, sin cifras sin fuente. **Origen:** PDF pp. 6–8.

#### 2.4 Actores y Grupos de Interés

- [ ] **S2-05 · P1.** Conservar el mapa de poder, interés y actitud ya valorado positivamente; derivar de él medidas de adopción y responsables que reaparezcan en 3.4 y en el plan de implantación. **Cierre:** trazabilidad actor → resistencia o interés → acción → indicador. **Origen:** PDF pp. 7–8, 11.

#### 2.5 Resumen de Requerimientos, Supuestos, Exclusiones y Restricciones

- [ ] **S2-06 · P1.** Mantener la cobertura de las 25 decisiones del 16.1, pero fijar parámetros verificables de SUP-04, SUP-12 y SUP-16, y calcular consecuencias de SUP-08. Alinear SUP-17 con las cinco causas de merma del caso. **Cierre:** resumen analítico en el capítulo y detalle en el anexo oficial, con ID, fundamento, responsable, prueba y riesgo de cada supuesto. **Origen:** PDF pp. 7–8.
- [ ] **S2-07 · P0.** Ningún supuesto puede rebajar un obligatorio transversal: reconciliar la autonomía sin enlace y la propagación de precios antes de trasladar SUP a 3.2, 4.2 y T-12. **Cierre:** decisión única aprobada y trazada a Bases. **Origen:** PDF pp. 10, 14, 25; Bases Administrativas Art. 16.4; Transversales RT-03.10.

### Capítulo 3 · Introducción al Alcance de la Solución

#### 3.1 Resumen Ejecutivo de la Solución

- [ ] **S3-01 · P1.** Presentar la propuesta de valor, sus componentes y el ciclo completo: Etapas 1 y 2, marchas blancas, producción en meses 16 y 21 y operación hasta el mes 56. No afirmar que 3.1 “está sin redactar” si existe. **Cierre:** resumen entendible sin recorrer tablas y coherente con capítulos 2, 4 y 5. **Origen:** PDF pp. 2, 6, 9, 12; Comunicado 10, índice 3.1.

#### 3.2 Alcance

- [ ] **S3-02 · P0.** Separar entregables y criterios de asignación de cada etapa; conservar el adelanto de la habilitación técnica del crédito, pero dar un plan alternativo para la operación offline de la Etapa 1 si falla la prueba de la API del core de 2011. **Cierre:** dependencia, fecha de decisión, alternativa, prueba y responsable, sin alterar los 56 meses. **Origen:** PDF pp. 9–11.
- [ ] **S3-03 · P0.** Resolver SUP-09 frente a la propagación de precio ≤5 min a cajas y canal digital y frente al precio de etiqueta física; si se propone una desviación, declararla y fundamentarla según las Bases, sin reinterpretar el RT ni marcar un `No` sin explicación. Dimensionar SUP-08 “cobrar el menor”. **Cierre:** una política operacional y técnica, prueba de tiempo y cálculo de impacto coherentes en S2/S3/S5/T-12. **Origen:** PDF pp. 10, 12, 20, 25; Caso 09 RT-05.29-C y RT-09.01-C.
- [ ] **S3-04 · P0.** Declarar autonomía del componente on-premise **no inferior a 24 h** y describir las funciones que operan degradadas, los folios, pagos y crédito de contingencia. **Cierre:** mismo umbral en RNF, S4, T-12, S13 y pruebas de corte/reconexión. **Origen:** PDF pp. 10, 12, 14, 25; Bases Administrativas Art. 16.4; Transversales RT-03.10.
- [ ] **S3-05 · P1.** Cubrir en el contenido vigente los cinco vacíos operacionales y la contradicción entre restricciones que la versión revisada anunciaba como “3.2.7”; citar una subsección sólo después de crearla conforme al índice oficial. Completar exclusiones, supuestos y los 28 criterios de aceptación del caso con línea base, meta, momento, evidencia y responsable. **Cierre:** todos los criterios del Cap. 18 trazados, sin remisiones inexistentes. **Origen:** PDF pp. 9, 11–12.
- [ ] **S3-06 · P0.** Conciliar el catálogo oficial de requisitos con el Excel v3.0 y su equivalencia de IDs antes de llenar T-12. El recuento 222/223 RF de la revisión es histórico y no debe trasladarse como cifra vigente. **Cierre:** unicidad de IDs, correspondencia RT → RF/RNF/OP → módulo → prueba y T-12 sin filas sin explicación. **Origen:** PDF pp. 2, 11–12, 26; `01_Requerimientos/RequerimientosAtomizados_Depuracion_Alcance.xlsx`.

#### 3.3 Esquema de solución

- [ ] **S3-07 · P0.** Sustituir el mapa del estado actual usado como “solución” por uno o varios diagramas de la arquitectura propuesta: módulos, actores, integraciones y frontera retail/financiero. **Cierre:** cada figura es legible a tamaño de página, se cita por número y se explica elemento por elemento; nombres idénticos a 3.4 y 4.1. **Origen:** PDF p. 9; Comunicado 10, índice 3.3 y regla 4.

#### 3.4 Explicación de la Solución

- [ ] **S3-08 · P1.** Explicar cómo cada módulo resuelve un dolor de negocio, cómo se implanta sin detener tiendas y crédito y qué ocurre ante falla o degradación; convertir las tablas de inventario en anexos cuando no sostienen un análisis. **Cierre:** recorrido textual problema → módulo → flujo → aceptación, más estrategia de apoyo de actores de 2.4. **Origen:** PDF pp. 9–12; Comunicado 10, índice 3.4.
- [ ] **S3-09 · P1.** Costear técnicamente la decisión ATP con supuestos y trade-off, sin incluir montos de oferta en este subdocumento; remitir su valorización al Sobre Económico. **Cierre:** memoria de capacidad/operación y correspondencia con EDT y flujo de caja. **Origen:** PDF p. 9; Bases Administrativas Art. 50.2.

### Capítulo 4 · Arquitectura lógica y física de la solución

#### 4.1 Arquitectura lógica

- [ ] **S4-01 · P1.** Conservar las ocho capas, límites de contexto, separación de dominios, estrangulador y decisiones ADR que el revisor valoró, pero representar **todos los módulos** en vistas legibles: vista general y vistas de retail, financiero, integración y borde. Dibujar la frontera entre negocios como límite efectivo; mostrar nodo de tienda, modo desconectado e integraciones externas. **Cierre:** concordancia al 100 % con 3.3/3.4 y explicación de cada figura. **Origen:** PDF pp. 12–13, 16.
- [ ] **S4-02 · P1.** Corregir la asignación de “Gestión de cobranza” al módulo que realmente la posee, depurar los códigos ADR y explicar las interfaces con contratos, versionado, idempotencia y reacción a fallas. **Cierre:** trazabilidad módulo → responsabilidad → integración → entidad, sin códigos huérfanos. **Origen:** PDF pp. 2, 13.
- [ ] **S4-03 · P1.** Completar los aspectos pendientes del dimensionamiento del numeral 14.2, incluidos datos generados sin enlace, drenaje tras reconexión, ancho de banda de centros de distribución y dotación operativa. Recalcular la conversión de 400 TB/30 días a bit/s, las instancias de M-01 y los 500 GB frente a 1,8 TB. **Cierre:** memoria de cálculo reproducible, unidades explícitas y cifras coherentes entre tablas. **Origen:** PDF pp. 13, 15–16.

#### 4.1.1 Especificaciones Tecnologías de Software a utilizar

- [ ] **S4-04 · P1.** Elegir y describir una arquitectura consistente por función: Event Hubs o Kafka autoadministrado; Cosmos DB compatible con Cassandra o clúster Cassandra; Elastic Cloud/OpenSearch; Redis/Valkey. Dimensionar cada servicio según su modelo real de contratación, no con parámetros de otro producto. **Cierre:** tabla de decisiones con alternativas, región, operación, soporte y costes operativos remitidos al Sobre Económico. **Origen:** PDF pp. 14–16.
- [ ] **S4-05 · P1.** Justificar la capacidad humana de operar AKS/Kubernetes/K3s y demás servicios autoadministrados, o seleccionar servicios gestionados; indicar fin de soporte verificable durante los 56 meses y esfuerzo de portabilidad, incluyendo Cosmos DB. **Cierre:** inventario de versiones, soporte, roles por turno, plan de actualización y salida. **Origen:** PDF pp. 14–16.

#### 4.2 Arquitectura física

- [ ] **S4-06 · P0.** Entregar un diagrama **físico** de la solución: región y zonas de nube; Site Principal y Secundario con distancia; 22 tiendas (con al menos una tienda tipo y variaciones de capacidad); dos centros de distribución; enlaces y anchos de banda; redes, equipos y cantidades. El texto debe recorrer cada sitio y explicar el emplazamiento híbrido. **Cierre:** figura legible que se corresponde con inventario, T-11 y zonas lógicas. **Origen:** PDF pp. 16–19; Comunicado 10, índice 4.2.
- [ ] **S4-07 · P0.** Dimensionar la continuidad de tienda para 24 h, incluidos almacenamiento de ventas y folios, caché de cupos, energía, UPS/generación y drenaje en la reconexión. Distinguir continuidad de tienda de sala técnica principal y de centro de distribución. **Cierre:** cálculo y ensayo de desconexión/reconexión con pérdida cero de documentos. **Origen:** PDF pp. 13–14, 18–19.
- [ ] **S4-08 · P1.** Incorporar configuración y conectividad de ambos centros de distribución y las diferencias de las 22 tiendas; evaluar la brecha del centro de datos existente con el informe de 2024 del cliente, en vez de reemplazarlo por un supuesto. **Cierre:** matriz de sitios, brecha y acciones por emplazamiento. **Origen:** PDF pp. 14, 17–18.

#### 4.2.1 Especificaciones Implementos a proveer (Hardware y Software)

- [ ] **S4-09 · P0.** Entregar T-11 como archivo propio, citado en 4.2.1. Para cada implemento: marca/modelo o equivalencia técnica, cantidad, capacidad, ubicación, justificación, redundancia, soporte y vigencia. Incluir servidores, switches, UPS, generador, HSM, nodos de tienda, periféricos, red de las tiendas y repuestos; recalcular repuestos de terminales de pago sobre el parque realmente comprometido. **Cierre:** T-11 completo y conciliado con diagrama, memoria de capacidad y oferta económica. **Origen:** PDF pp. 18–19; Comunicado 10, índice 4.2.1.

#### 4.3 Data center

- [ ] **S4-10 · P1.** Introducir la estrategia conjunta de centro primario y recuperación, con amenazas comunes, ubicación de datos por dominio, responsabilidades del proveedor y procedimiento de conmutación antes de 4.3.1/4.3.2. **Cierre:** texto de caída bajo 4.3 y matriz de dependencia entre sitios. **Origen:** PDF pp. 17–19; Comunicado 10, índice 4.3.

#### 4.3.1 Especificaciones Data Center Primaria

- [ ] **S4-11 · P0.** Declarar proveedor, región primaria y zonas de disponibilidad, servicios contratados y residencia de datos por dominio; acreditar que la elección cumple los artículos de nube y datos de las Bases. **Cierre:** región explícita en el texto, diagrama, ADR, T-11/T-12 y evidencia de socio. **Origen:** PDF pp. 16–19; Bases Administrativas Arts. 16 y 23.
- [ ] **S4-12 · P1.** Precisar racks, potencia, UPS/generador, climatización y seguridad del sitio on-premise con cálculo de capacidad y brecha del recinto actual. **Cierre:** especificación cuantitativa y plano/diagrama consistente. **Origen:** PDF pp. 16–18.

#### 4.3.2 Especificaciones Data Center Secundario

- [ ] **S4-13 · P0.** Resolver el sitio secundario en la misma comuna frente a RT-07.02: seleccionar distancia y amenazas independientes, o documentar una desviación sólo si las Bases la permiten, con mitigación efectiva y aceptación formal. No presentar una decisión del proceso de redacción como justificación técnica. **Cierre:** análisis geográfico y de riesgos, ubicación, RPO/RTO y prueba de conmutación. **Origen:** PDF pp. 17–19.
- [ ] **S4-14 · P1.** Especificar región/sitio de recuperación, replicación, respaldo 3-2-1-1-0, conmutación y reversión, separando objetivos de infraestructura y servicio de negocio. **Cierre:** procedimientos y calendario de ensayos documentados. **Origen:** PDF pp. 16–19; Comunicado 10, índice 4.3.2.

### Capítulo 5 · Modelo y gestión de datos

#### 5.1 Modelo

- [ ] **S5-01 · P0.** Presentar modelos por dominio y diagramas entidad–relación legibles, con cardinalidades y frontera retail/financiero; adjuntar diccionario por atributo con nombre, tipo, dominio de valores, obligatoriedad, propietario y sensibilidad. **Cierre:** RT-05.01 sólo puede marcarse `Sí` si el diccionario y los diagramas existen y son trazables a las entidades. **Origen:** PDF pp. 19–20, 22; Transversales RT-05.01; Comunicado 10, índice 5.1.
- [ ] **S5-02 · P1.** Modelar explícitamente identidad neutral y bitácora de cruces M-21/M-22, sin unión directa de bases; alinear el perfil comprador con la ley de datos personales indicada en el caso y separar sus obligaciones de consumo. **Cierre:** permisos, flujos permitidos, denegación por omisión y evidencia de cruces. **Origen:** PDF pp. 19–21; Caso 09, capítulo de datos y privacidad.

#### 5.2 Gestión de datos

- [ ] **S5-03 · P1.** Para cada entidad, justificar motor, consistencia, disponibilidad y postura CAP; incluir M-21/M-22 y separar almacenamiento transaccional de analítico. Conciliar Redis/Valkey y Cassandra/Cosmos con 4.1.1. **Cierre:** matriz entidad → motor → CAP → propietario → zona → respaldo, sin tecnología duplicada para el mismo rol. **Origen:** PDF pp. 19–21.
- [ ] **S5-04 · P0.** Usar **una sola taxonomía de merma** basada en las cinco causas del caso y compartirla entre S2/S3/S5, incluyendo devolución mal reintegrada y error de digitación. **Cierre:** catálogo versionado y reglas de atribución, sin cajón de sastre que oculte error de registro. **Origen:** PDF pp. 20–22, 25.
- [ ] **S5-05 · P1.** Mantener precio vigente autoritativo e historia reconstruible separada de la proyección de vitrina; corregir la cita de retención a RT-05.10-C, definir códigos como `C-02` si se usan y no cambiar el alcance del compromiso de ≤5 min para salvar SUP-09. **Cierre:** consulta reproducible del precio por canal/tienda/instante y una política coherente con 3.2. **Origen:** PDF pp. 20–22.
- [ ] **S5-06 · P0.** Definir **un solo horizonte normativo** para expediente de crédito/consentimiento y **un solo tiempo de recuperación**, compatibles con T-12 y el contrato; incluir preservación de firmas, resellado y migración de formatos a largo plazo. **Cierre:** política por tipo de evidencia, prueba de recuperación y cadena de custodia. **Origen:** PDF pp. 20–22, 25; Caso 09 RT-05.10-C.
- [ ] **S5-07 · P1.** Completar calidad, archivado y eliminación segura por dominio; corregir la conservación de DTE y el fundamento legal del perfil comprador. Incluir cifrado a nivel de campo y tokenización exigidos, o remisión precisa a controles de 4.1/4.2. **Cierre:** políticas con responsable, plazo, base legal/requisito, prueba y excepción. **Origen:** PDF pp. 20–22.

#### 5.3 Estrategia de migración

- [ ] **S5-08 · P1.** Conservar las cuatro fases y conciliación diaria, pero mostrar volumetría, ventanas, al menos dos ensayos completos, umbrales de conciliación justificados y rollback comprobable. Evitar un umbral monetario `>$0` sin tratamiento de redondeo. **Cierre:** plan de ensayos, actas, reconciliación y criterio de corte por ola. **Origen:** PDF pp. 20–22; Transversales RT-05.13.
- [ ] **S5-09 · P1.** Incorporar comunicación y atención a los titulares afectados por la migración de la cartera y enlace explícito a las cifras de S4. **Cierre:** plan por segmento, responsable, calendario y evidencia de recepción, sin exponer datos deudores al retail. **Origen:** PDF pp. 20–22.

#### 5.4 Estrategia de desempeño

- [ ] **S5-10 · P1.** Dimensionar índices, particiones, cachés, consultas y capa analítica desde la volumetría del caso; explicar degradación y recuperación del caché local tras 24 h sin enlace. **Cierre:** cálculo de carga/latencia, plan de pruebas y coherencia con 4.2 y RT de desempeño. **Origen:** PDF pp. 19–22; Comunicado 10, índice 5.4.

### Capítulo 13 · Innovaciones

**Regla común INN-00 · P0:** cada ficha debe superar el piso obligatorio del caso y del Art. 30.º, corresponder a **un tipo distinto** y completar los siete elementos del Art. 29.º: problema, práctica/tecnología, madurez con evidencia, incorporación en arquitectura/EDT/mes, impacto económico sin montos de la oferta técnica, indicador con línea base y meta, y riesgo con mitigación/contingencia. T-19 va en archivo separado. Ningún campo verificable queda “Pendiente (Informe 2–3)”. Los códigos de arquitectura deben existir en S4 y el nombre de cada innovación reaparecer en S3/S4/S5 cuando corresponda. **Origen:** PDF pp. 22–24; Bases Administrativas Arts. 28–30; Comunicado 10, índice 13 y regla 8.

#### 13.1 Innovación 1 — Producto o servicio

- [ ] **INN-01 · P0.** Replantear el “cliente único federado” si sólo cumple la identificación obligatoria; demostrar un producto o servicio adicional con usuario, beneficio medible, adopción y ventaja sobre el requisito base. **Cierre:** ficha T-19 completa y comparación `obligatorio vs. valor incremental`. **Origen:** PDF p. 23.

#### 13.2 Innovación 2 — Proceso

- [ ] **INN-02 · P0.** Reemplazar o ampliar el patrón estrangulador, que es método de implantación exigido, por un proceso novedoso y medible. Si aborda el legado, distinguir sistema central de retail, ERP emisor tributario que permanece y plataforma de crédito 2011 con fin de soporte 2029. **Cierre:** proceso, métrica y trazabilidad correctos sin atribuir al sistema de 2009 funciones que no tiene. **Origen:** PDF p. 23.

#### 13.3 Innovación 3 — Tecnológica o de arquitectura

- [ ] **INN-03 · P0.** Sustituir la mera postura CAP/propagación de precios por una innovación que exceda RT-05.02 y el umbral de ≤5 min. Si se consideran etiquetas electrónicas, evaluar y costear frente a alternativas, pero probar qué es incremental respecto del encargo; los 310.000 puntos del caso son **etiquetas físicas**. **Cierre:** diseño, comparación tecnológica, riesgo y beneficio verificable; sin confundir CDN con cambio de etiqueta. **Origen:** PDF p. 23; Caso 09, decisión 9.

#### 13.4 Innovación 4 — Modelo de negocio o de contratación

- [ ] **INN-04 · P0.** Proponer un esquema contractual o de negocio realmente distinto, con incentivos, asignación de riesgo, medición y tratamiento del ámbito financiero fiscalizado. Nube híbrida y separación de dominios son obligaciones de la oferta, no la innovación. **Cierre:** términos de contratación, actor que asume cada riesgo e indicador de resultado, compatibles con Bases y flujo de caja. **Origen:** PDF pp. 22–23.

#### 13.5 Innovación 5 — Experiencia de usuario, sostenibilidad o impacto social

- [ ] **INN-05 · P0.** Diseñar una intervención y un indicador de experiencia, sostenibilidad o impacto social medible; continuidad offline y respaldo satelital son requisitos y mitigaciones. **Cierre:** población objetivo, línea base, meta, método y momento de medición, más riesgo de adopción. **Origen:** PDF pp. 23–24.

## 5. Decisiones transversales que requieren una única versión

| Decisión | Regla de cierre | Secciones y formularios a reconciliar | Evidencia del PDF |
| :--- | :--- | :--- | :--- |
| Autonomía sin enlace | Compromiso no inferior a 24 h, funciones, energía y sincronización calculadas. | 2.5, 3.2, 4.2, 4.2.1, 5.4, T-11, T-12, innovaciones. | pp. 10, 13–14, 18, 25 |
| Precio multicanal | Una política de propagación ≤5 min a cajas y canal digital y control del precio físico; dimensionar “cobrar el menor”. | 2.3/2.5, 3.2, 4.1, 5.2, T-12. | pp. 7, 10, 20, 25 |
| Merma | Cinco causas del caso y reglas de atribución comunes. | 2.5, 3.4, 5.2 y analítica. | pp. 7, 21–22, 25 |
| Consentimiento | Un plazo de retención y un objetivo de recuperación; evidencia preservable durante todo el horizonte. | 3.2, 4.2, 5.2, T-12. | pp. 20–22, 25 |
| Nube y sitio secundario | Región, residencia, socio verificable y distancia/amenazas comunes. | 1.6, 4.2–4.3.2, T-11, T-12. | pp. 4, 16–19, 25 |
| Nomenclatura | Módulos, zonas, ADR, RF/RNF/OP y nombres de innovaciones únicos. | 3.3–3.4, 4.1–4.2, 5.1–5.4, 13.1–13.5, T-12/T-19. | pp. 2, 11, 24–25 |

## 6. Observaciones del PDF que no se adoptan literalmente

1. **“Reemplazar Hites, CMF y Sernac por nombres ficticios” (p. 5).** Se debe eliminar cualquier atribución de experiencia a una empresa real ajena a la simulación. **CMF y SERNAC son autoridades reales**, por lo que sus nombres no se sustituyen por reguladores ficticios en una explicación normativa; se verifica la denominación vigente y la fuente aplicable.
2. **Candidatos de innovación (pp. 23–24).** Merma, repositores, marketplace, lenguaje claro, etiquetas y comisión omnicanal son espacios de diseño, no innovaciones aprobadas por esa sola mención. Cada candidato debe pasar la prueba de novedad del Art. 30.º y la distribución por tipo.
3. **Porcentajes, puntajes y recuentos históricos.** El 43,8 y las ponderaciones citadas por el revisor no sustituyen el T-21 oficial; la tabla final a la que alude no está en el PDF. Los 222/223 RF y 75 RNF describen los documentos que revisó; el catálogo vigente es el Excel v3.0 de `01_Requerimientos/`.
4. **Afirmaciones sobre el estado actual.** “No existe” o “sin redactar” describe el paquete revisado, no una auditoría de este checkout. Se comprueba cada criterio en los artefactos actuales antes de actualizar estados del maestro.

## 7. Uso en el siguiente ciclo

1. Asignar cada ID de esta rúbrica a un responsable y al archivo oficial de la subsección, respetando el mapa de migración del Comunicado 10 antes de mover contenido.
2. Resolver primero los `P0` y las seis decisiones transversales; registrar una decisión única con fundamento en las Bases.
3. Redactar o corregir cada subsección con cálculo, figura y cita donde correspondan; trasladar listados extensos al anexo o formulario.
4. Revisar T-12, T-11, T-6, T-8 y T-19 contra el texto final. Preparar la tabla de respuesta a observaciones del Informe 2.
5. Hacer lectura humana integral y registrar quién revisó cada sección, figura, cifra, enlace y declaración de IA antes de cambiar su estado a `revisado`.

**Fuente de respaldo:** [transcripción del PDF por página](revision_informe_1_transcripcion.md). Ante duda de lectura, prevalece el PDF original; ante duda de requisito, prevalecen las Bases y el Comunicado 10 según su alcance.
