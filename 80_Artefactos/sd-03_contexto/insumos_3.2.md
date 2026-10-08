# Insumos para redactar 3.2 Alcance (sd-03)

> **Nomenclatura (2026-10-07):** los nombres y códigos de los servicios de este documento (R-01 a X-01) fueron reemplazados. Rige `divisiones_negocio_servicios_sd-03.md`, que contiene la tabla de equivalencias.

Documento de contexto, no es entregable. Paquete autocontenido para redactar la sección 3.2 en `02_Propuesta/latex_final/sd-03.tex`: el redactor no necesita abrir otros archivos. Todo dato tiene su fuente (Bases o decisión registrada del equipo). Lo que no está decidido se marca **(S)**: propuesta del asistente, por confirmar. Versión 2, 2026-10-06 (la versión 1 se reemplazó completa).

Contenido: 0. Cómo usarlo · 1. Contenido por subsección (3.2.1 a 3.2.5) · 2. Diagramas · 3. Tablas listas · 4. Cifras con fuente · 5. Puntos abiertos · Anexo A (tablas completas para el anexo del subdocumento) · Anexo B (lista de entregables).

---

## 0. Cómo usar este documento

### 0.1 Qué exige el Comunicado 10

Título obligatorio: **3.2 Alcance**. "Alcance de la solución expresado con claridad, demostrando la capacidad de descomponer un problema complejo en componentes manejables". Debe desarrollar:
1. alcance de la Etapa 1 y de la Etapa 2, con separación explícita y criterios de asignación;
2. exclusiones explícitas, supuestos y restricciones;
3. catálogo de requerimientos funcionales y no funcionales, priorizado y trazable (resumen y análisis en el capítulo; trazabilidad completa en el Formulario T-12);
4. criterios de aceptación del alcance comprometido.

### 0.2 Subtítulos propuestos (RR-01 permite niveles menores)

| Subtítulo | Cubre | Diagramas | Tablas (sección 3) |
| :-- | :-- | :-- | :-- |
| 3.2.1 Descomposición del alcance | Causas, frentes, áreas, servicios, base tecnológica, destino de las plataformas | D1, D1b, D5 | — |
| 3.2.2 Alcance de la Etapa 1 y de la Etapa 2 | Criterio en dos pasos, reparto, desviación del comité | D2, D3 | T2 |
| 3.2.3 Exclusiones, supuestos y restricciones | EXC, SP, RC, RS, crédito sin conexión | D4, D6 | T4 |
| 3.2.4 Catálogo de requerimientos | Síntesis por servicio, etapa y prioridad | — | T5 |
| 3.2.5 Criterios de aceptación | Entregable, marcha blanca, resultado de negocio | — | T6, T7 |

### 0.3 Reglas de redacción que más pesan

- **RR-04:** cada título y subtítulo lleva un texto de caída. Ninguna tabla, figura o lista sigue directamente a un título.
- **RR-05:** el capítulo resume y analiza; los listados completos van al anexo (Anexo A de este documento) o al T-12. Si más del 60 % es tabla o lista, falla.
- **RR-10 a RR-14 (figuras):**
  - El texto recorre la figura y concluye.
  - Formato "Figura 3.N: …" y "Fuente: elaboración propia".
  - Se cita antes y se explica después.
  - Diagramas grandes: primero la vista general y luego las partes, cada una dibujada aparte (no recortes).
- **RR-15 a RR-19 (tablas):**
  - Solo para comparar en varias dimensiones; nada de "Concepto | Descripción".
  - Máximo 5 columnas y 25 filas.
  - Formato "Tabla 3.N: …" con su fuente, citada antes y seguida de una conclusión.
- **RR-06:** cada cifra viene de las Bases o de un cálculo mostrado (sección 4).
- **RR-07:** nombres de los servicios idénticos en todo el documento (sección 1.1).
- **RR-08:** sin precios ni montos.
- **RR-22:** sin "pendiente", "por definir", "TODO" ni "[…]", y sin lenguaje académico. Lo abierto se declara como supuesto o se omite.
- **Citas:**
  - En APA 7 con el mandante como autor y sin página: (Multitiendas Ancoa S.A., 2026a, art. 17).
  - 2026a = Bases Administrativas; 2026b = Bases técnicas, Caso 09; 2026c = Bases técnicas transversales. Ya están en la lista de Referencias del `.tex`.
- **Control:** `python3 05_Gestion/scripts/exportar_latex.py verificar-redaccion --parte T7-03` (solo informa).

### 0.4 Qué no hacer

- Repetir el orden del comité sin analizarlo: el Caso 13.1 lo califica de "falta de criterio profesional".
- Presentar el problema como un sistema legado (Caso cap. 5).
- Debilitar la separación Retail–Emisor.
- Escribir análisis de riesgos (va en el sd-08).
- Meter diseño técnico, como el algoritmo de reconciliación o la tecnología del bus (va en 3.3, 3.4 y el sd-04).
- Repetir 3.1: 3.2 detalla y justifica lo que 3.1 resume.

---

## 1. Contenido por subsección

### 1.1 Nombres oficiales (RR-07)

> Esta sección conserva los nombres anteriores de los servicios (R-01 a X-01). Para el texto del `.tex` rigen los nombres y códigos de `divisiones_negocio_servicios_sd-03.md`.

| Código | Nombre | Negocio |
| :-- | :-- | :-- |
| R-01 | Catálogo, precios y promociones | Retail |
| R-02 | Abastecimiento y reposición | Retail |
| R-03 | Inventario, reservas y disponibilidad | Retail |
| R-04 | Pedidos y cumplimiento omnicanal | Retail |
| R-05 | Registro y conciliación de ventas | Retail |
| R-06 | Atribución de ventas y comisiones | Retail |
| R-07 | Integración y gobierno de marketplace | Retail |
| R-08 | Posventa, garantías y devoluciones | Retail |
| R-09 | Clientes y fidelización Retail | Retail |
| F-01 | Originación y autorización de crédito | Emisor |
| F-02 | Cartera, cobranza y repactaciones | Emisor |
| F-03 | Consentimiento y evidencia financiera | Emisor |
| X-01 | Autorización y auditoría de cruces Retail–Emisor | Frontera |

La base común no es R, F ni X. Se compone de:
- 1.14a, plataforma de integración;
- 1.14b, catálogo de reglas de acuerdo por tipo de dato;
- 1.14c, identidad y gestión de accesos;
- 1.14d, observabilidad.

**Texto de caída sugerido para 3.2 (RR-04):** "Esta sección delimita lo que Only Simple Solutions se compromete a entregar. Primero descompone el problema descrito en el Capítulo 2 en componentes manejables. Luego reparte esos componentes entre las dos etapas del cronograma con criterios explícitos, declara lo que queda fuera y bajo qué supuestos, resume el catálogo de requerimientos y fija cómo se aceptará lo entregado."

### 1.2 3.2.1 Descomposición del alcance (reescrita el 2026-10-07)

Los nombres y códigos de esta subsección son los de `divisiones_negocio_servicios_sd-03.md`, que manda sobre los de `guia_servicios_R_F_X.md` y demás archivos.

**Mensaje central.** El problema se descompone de lo general a lo particular, con las causas raíz como base. Cadena: dos negocios bajo un mismo techo con plataformas no coordinadas (desincronización) → no se pueden prometer ni acreditar las cuatro promesas → cinco causas raíz (base de la descomposición, fijan qué debe corregir la solución y permiten comprobar que ninguna queda sin atender) → tres frentes → áreas → trece servicios, sobre una base tecnológica.

**Definiciones (idénticas a las del `.tex`).**
- **Frente:** parte del problema que responde a un mismo régimen jurídico y de datos (retail, filial emisora, frontera).
- **Área:** sección o división del negocio a la que pertenece el servicio. Retail tiene tres (mercadería, venta, relación con el cliente) y la filial emisora una (crédito). La frontera no tiene áreas y se conecta directamente con su servicio.
- **Servicio:** pieza del sistema que se ocupa de un solo tema del negocio. Es la única autorizada para registrar y corregir su información, y las demás piezas la consultan. «Contratos» e independencia de despliegue se dejan para la 3.3.
- **Base tecnológica** (antes «plataforma común»): plataforma de integración (que reemplaza las 14 conexiones directas), identidad y gestión de accesos y observabilidad. El despliegue híbrido no es un servicio ni un componente de esa lista: va en la 3.3.

**Jerarquía y códigos** (`frente:área-número`).

| Frente | Área | Código | Servicio |
| :-- | :-- | :-- | :-- |
| Retail | Mercadería | R:M-01 a R:M-03 | oferta comercial, abastecimiento, existencias |
| Retail | Venta | R:V-01 a R:V-04 | pedidos, ventas, comisiones, marketplace |
| Retail | Relación con el cliente | R:CL-01, R:CL-02 | posventa, clientes Retail |
| Filial emisora | Crédito | F:C-01 a F:C-03 | originación de crédito, cartera de crédito, evidencia financiera |
| Frontera | (sin área) | X-01 | control de cruces |

**Cómo queda redactada.** Seis párrafos y tres figuras. 1) Causas (con «que son:» a pedido del usuario). 2) Jerarquía con las definiciones y la afirmación de que es el alcance del producto, no del proyecto (FEP02 · 34), y que el trabajo del proyecto (migración, marchas blancas y operación) se descompone en la EDT del capítulo 7. 3) Áreas con sus servicios y glosas de los servicios de la filial emisora. 4) Figura de cobertura de causas e interpretación (cada causa queda atendida por al menos un servicio, un servicio atiende varias causas, las causas C4 y C5 se mitigan y no se eliminan, la causa C5 se atiende además con componentes locales de las tiendas). 5) Un solo dueño por tipo de dato (Caso 16.1). 6) Base tecnológica y destino de las nueve plataformas.

**La tabla T1 se eliminó.** La cobertura causa → servicio se muestra en una figura (matriz) y no en tabla, porque la tabla era difícil de leer.

**Cobertura de causas** (insumo de la figura; asignaciones del asistente, la tabla de `descripcion_alcance_producto.md` seguía «por validar»).

| Causa | Servicios y componentes que la atienden |
| :-- | :-- |
| Causa C1, registro impreciso | oferta comercial (maestro de artículos), abastecimiento, existencias, posventa (devoluciones mal reintegradas) |
| Causa C2, tejido de integración | oferta comercial (motor de precios), pedidos, ventas, marketplace, plataforma de integración |
| Causa C3, frontera difusa | clientes Retail, originación de crédito, cartera de crédito, evidencia financiera, control de cruces |
| Causa C4, incentivos y capacidad | comisiones, pedidos (compensación a la tienda que despacha), originación de crédito, evidencia financiera, identidad y gestión de accesos |
| Causa C5, territorio y calendario | ventas (venta sin conexión), componentes locales de las tiendas (el detalle va en la 3.3) |

**Destino de las nueve plataformas** (Caso cap. 5, líneas 303 a 321).
- **Se reemplazan por etapas:** el sistema central de retail de 2009 (SP-01), la plataforma de originación y cobranza de 2011 y el punto de venta de 2014.
- **Se conservan e integran:** el sistema de gestión empresarial y facturación (único emisor tributario, restricción 6), el marketplace de 2022 (la plataforma se conserva y el servicio de marketplace es la capa nueva que gobierna su relación con los vendedores), el sistema de almacenes del centro de distribución principal de 2016, el comercio electrónico de 2019 y el sistema de fidelización de 2017 (EXC-15). El de fidelización se integra al servicio de clientes Retail, que gobierna sus datos.
- **La novena plataforma son las planillas y listas impresas.** Dejan de ser el registro oficial. El motor de precios y promociones «no existe como sistema» y nace dentro del servicio de oferta comercial.

**Autoridad por dato.** Cada dato tiene un servicio dueño (existencias para la disponibilidad que se puede prometer, pedidos para el ciclo del pedido). Las copias en otros sistemas se comparan con él y se corrigen según reglas escritas. Responde a la decisión pendiente del Caso 16.1 (primera de 25) sobre cuál es la fuente única de verdad de la existencia, y al art. 17.2. Sin prometer «cero pérdida» ni «confianza declarada»: el detalle técnico va en la 3.3 y 3.4.

**Figuras (marcadores en el `.tex`).** D1: jerarquía (problema, frentes, áreas, servicios, base; la frontera va sin área; es la misma del mapa de la 3.1). D1b: matriz de cobertura de causas (cinco filas, columnas de servicios agrupados por frente y área más la base tecnológica y los componentes locales). D5: destino de las nueve plataformas (año, destino y etapa de cada una, incluidas las planillas).

**Tablas:** ninguna. **Diagramas:** D1, D1b y D5 (sección 2).

### 1.3 3.2.2 Alcance de la Etapa 1 y de la Etapa 2 (reescrita el 2026-10-07)

Los nombres y códigos son los de `divisiones_negocio_servicios_sd-03.md`. Donde el material trasladado de más abajo usa R-01 a X-01, léase con la tabla de equivalencias de ese archivo.

**Mensaje central.** El reparto se hizo en dos pasos declarados antes de la tabla. Paso 1: asignar cada componente con cuatro pruebas de primera prioridad derivadas del Caso. Paso 2: contrastar la asignación con dos condiciones que el Caso pide considerar, los hitos externos y la preferencia del comité. Las dependencias técnicas ya están aplicadas en la cuarta prueba. La capacidad de absorción del cliente se quitó (decisión del usuario, 2026-10-07): la formulación anterior era confusa y no tenía respaldo medible. El Caso 17.3 la menciona; si un evaluador lo señala, hay que incorporarla con un fundamento sólido.

**Paso 1: cuatro pruebas** (Bases art. 15 remite la primera prioridad al Caso; Caso 13.1 y cap. 10). Un componente va a la Etapa 1 si cumple al menos una. Si no cumple ninguna, va a la Etapa 2.

| Prueba | Qué significa | Fuente |
| :-- | :-- | :-- |
| Promesa priorizada | Sostiene una de las dos prioridades del comité, que son dos de las cuatro promesas: existencia con disponibilidad publicada, y precio con su trazabilidad | Caso 13.1; episodio de junio; fiscalización de febrero |
| Objeción registrada | Es condición de la objeción de la contralora (frontera de datos antes de cualquier vista unificada) o de la del gerente del negocio financiero (migrar la cartera antes de 2029) | Caso 13.1, 13.2, 13.3.5 y 13.3.7; restricciones 1 y 8 |
| Registro oficial | Es necesario para que la Etapa 1 sea el registro oficial de la operación desde el mes 16: la tienda vende sin conexión (restricción 5) y el sistema de gestión empresarial sigue como único emisor tributario (restricción 6) | Bases art. 15 y 17; Caso cap. 10 |
| Dependencia | Lo requiere otro componente que cumple alguna de las tres anteriores | Capas de dependencia (más abajo) |

**Paso 2: contraste.**
- **Hitos externos** (Caso 13.2): fechas que Ancoa no controla. Fin de soporte de la plataforma de crédito y último plazo del plan de remediación de la autoridad financiera, ambos en 2029, y las cinco temporadas de venta alta con congelamiento. Efectos: el negocio financiero va en la Etapa 1; la cartera se reparte entre etapas por complejidad; los pasos a producción de los meses 16 y 21 caen fuera de las temporadas de venta alta. El riesgo de incumplir esas fechas se analiza en el capítulo 8 y aquí solo cuenta como razón de ubicación.
- **Preferencia del comité** (Caso 13.1: «una preferencia del mandante, no una definición de alcance»; repetirla sin análisis se evalúa como falta de criterio). Coincide en inventario y precio en la Etapa 1 y marketplace en la Etapa 2. Se aparta en un solo punto: el negocio financiero se adelanta.

**Desviación respecto del comité (tres razones).** 1) El fin de soporte de la plataforma de crédito y el último hito del plan de remediación vencen en 2029 (Caso 13.2). 2) El gerente financiero dejó registrado que migrar 620.000 clientes con saldo no se hace en un semestre y que, si queda en la Etapa 2, no se llega a tiempo (Caso 13.1). 3) El servicio de evidencia financiera es dependencia de la originación y de la cartera. La objeción de la contralora se atiende construyendo el servicio de control de cruces antes que cualquier servicio que combine datos de ambos negocios.

**Reparto** (tabla T2). Etapa 1: desarrollo en los meses 1 a 12, marcha blanca en los meses 13 a 15, producción en el mes 16. Etapa 2: desarrollo en los meses 13 a 18, marcha blanca en los meses 19 y 20, producción en el mes 21. Operación del mes 21 al 56 (retiros de las plataformas de 2011 y 2009). Estos meses y retiros ya están en la 3.1 y no se repiten en el cuerpo de la 3.2.2.

**Puntos sensibles para el texto.**
- Abastecimiento y pedidos también sostienen las promesas de existencia y de entrega. Van en la Etapa 2 porque el comité nombra la exactitud del inventario y la disponibilidad publicada, no la reposición ni el estado del pedido, y porque requieren el servicio de existencias estable.
- La cartera se reparte por complejidad, no por si está activa o cerrada (los 620.000 son clientes con saldo vigente, Caso cap. 2 y restricción 8). Ola 1: saldo al día, sin repactación ni cobranza en curso. Ola 2: repactaciones, cobranzas o juicios en curso.
- El sistema central de 2009 entrega en la Etapa 1 el maestro de artículos, los precios y el inventario, y en la Etapa 2 las órdenes, la recepción y la reposición.

**Qué sale del cuerpo de la 3.2.2 y adónde va.** El ciclo de vida híbrido va al capítulo 6 (Metodologías). El despliegue por olas del punto de venta, la compuerta, la publicación de la disponibilidad por categorías, las apps de sala y el portal van al capítulo 7 (Plan de trabajo) y, en lo que toca a riesgos, al capítulo 8. La lista de integraciones críticas va a la 3.3 y 3.4; en el cuerpo queda su definición en una frase.

**Figuras.** D2 (dependencias y etapa por servicio). D3 (horizonte de 56 meses; es la misma de la 3.1: reutilizar).

**Decisión del 2026-10-07:** no se agrega tabla de familias de entregables a la 3.2.2. La rúbrica S3-02 la sugiere («separar entregables…»), pero la revisión del Informe 1 solo pide el alcance de cada etapa con criterios de asignación (ya cubierto por la Tabla 3.1) y el plan B del crédito; la palabra «entregables» no aparece en la revisión. La descomposición del trabajo del proyecto va en la EDT del capítulo 7.

**Tablas:** T2 y T3. **Diagramas:** D2 y D3.

---

#### Material trasladado de la versión anterior (para los capítulos 6, 7, 8 y la 3.3)

**Ciclo de vida.**
- Es híbrido. El marco es predictivo: suma alzada, línea base, dos etapas con hitos y cambios solo por solicitud formal, con análisis de impacto y aprobación del Comité Ejecutivo (Bases Admin. art. 72).
- El desarrollo es adaptativo, en iteraciones dentro de cada etapa.
- Apoyo de clase: FEP02, diapositiva 8 ("en una licitación a suma alzada el marco es predictivo… un mismo proyecto puede combinar ambos enfoques: eso es un ciclo de vida híbrido").


**Integraciones críticas.** Son las que, si fallan, rompen una promesa o la separación Retail–Emisor:
- POS con R-01;
- POS con R-05;
- WMS con R-03;
- comercio electrónico con R-03;
- plataforma financiera con F-01, F-02, F-03 y X-01;
- ERP/DTE.


**Capas de dependencia.** Son la base del diagrama D2 y de la tabla T3.
- Capa 0: plataforma, identidad y mapa de las 14 integraciones.
- Capa 1: X-01, F-03 y R-01.
- Capa 2: R-03, R-05 y F-01.
- Capa 3: R-02, R-04, F-02 y R-09.
- Capa 4: R-06, R-07 y R-08.


**Despliegue por olas** (Caso 13.3.4: "por tienda, por proceso o por categoría de producto, y no como un único evento").
- **POS:**
  - **Ola 1, piloto en 3 tiendas.** Del entorno de Santiago, de volumen medio o bajo, sin la tienda insignia (17 % de la venta presencial y un mesón financiero por piso; Caso cap. 2). Entre las tres deben cubrir las tres versiones del POS actual.
  - **Ola 2.** Las otras 19 tiendas, en orden creciente de riesgo, antes del mes 16.
  - **Compuerta entre olas, 9 condiciones:**
    1. Cuatro semanas de operación real con un fin de semana de venta alta.
    2. Venta en caja en 25 s o menos.
    3. Precio cobrado igual al exhibido, con cambio de precio en 5 min o menos.
    4. Evaluación de crédito en 8 s o menos.
    5. Corte de enlace provocado de 24 h.
    6. Conciliación en 30 min o menos sin pérdida.
    7. Cero incidentes críticos o altos y acta firmada.
    8. Retorno probado al POS anterior (13.3.1).
    9. Prueba del crédito sin conexión.
  - **Calendario propuesto:** piloto en los meses 6 y 7, ola 2 en los meses 8 a 10 (antes del 1 de noviembre de 2027), con respaldo entre el 8 de marzo de 2028 y el mes 16.
- **Cartera de F-02:**
  - Ola 1 (Etapa 1): clientes con saldo al día, sin repactación ni cobranza en curso, por tramos crecientes.
  - Ola 2 (Etapa 2): clientes con repactaciones, cobranza y juicios en curso.
  - Cada tramo pasa una compuerta con las condiciones del Caso 13.3.5: convivencia real, conciliación diaria de saldos, retorno probado y plan de comunicación, sin fecha de corte única.
  - Los 620.000 son "clientes con saldo vigente" (Caso cap. 2; restricción 8). Por eso la división es por complejidad y no por si están activos o cerrados.
- **Disponibilidad publicada:** el nuevo cálculo de R-03 se publica primero en un subconjunto de categorías del comercio electrónico, midiendo la cancelación antes y después (Caso 13.3.6). Hoy la cancelación es de 1,9 % y la meta está bajo 0,3 % (Caso cap. 7).
- **Apps de sala** (vendedor de sala 1.36 y conteo cíclico 1.38): piloto en las mismas 3 tiendas en la Etapa 1 y despliegue al resto en la Etapa 2.
- **Portal público:** 1.31a en la Etapa 1 (catálogo, precio, disponibilidad e información precontractual) y 1.31b en la Etapa 2 (consulta de pedido, que depende de R-04).
- **Sistema central de 2009:**
  - Etapa 1: migra el maestro de artículos y precios (R-01) y el inventario (R-03).
  - Etapa 2: migra las órdenes, la recepción y la reposición (R-02).
  - El inventario contable queda en el ERP.

**Ventanas de congelamiento** (Caso 13.2 y restricción 9):
- del 1 de noviembre al 6 de enero;
- de la última semana de enero a la primera de marzo;
- la segunda semana de mayo;
- el evento anual (tres días entre mayo y junio, más la semana previa; la fecha se anuncia con unas seis semanas);
- la última semana de noviembre.

Con inicio en enero de 2027 (SUP-26 del sd-02), los pasos a producción de los meses 16 (abril de 2028) y 21 (septiembre de 2028) caen fuera de estas ventanas.

**Carga entre etapas** (estimación del equipo con pesos supuestos; si se usa, hay que mostrar el cálculo o decirlo cualitativamente, RR-06):
- La Etapa 1 lleva cerca del 70 % del esfuerzo ponderado y la Etapa 2 cerca del 29 %.
- Por mes, la Etapa 1 es alrededor de un 22 % más intensa, porque tiene 12 meses de desarrollo contra 6.
- Hay solapamiento en los meses 13 a 15 y 19 a 20 (art. 17.2).

**Tablas:** T2 y T3. **Diagramas:** D2 y D3.


### 1.4 3.2.3 Exclusiones, supuestos y restricciones

> **Reescrita el 2026-10-07.** El cuerpo de la 3.2.3 usa una tabla de síntesis de cinco categorías de exclusión (Tabla 3.2) y la tabla de seis supuestos (Tabla 3.3). El listado completo de exclusiones, supuestos, responsabilidades del cliente y restricciones está en el **Anexo A del Subdocumento 3**, que se entrega como documento aparte (`OnlySimpleSolutions-Subdocumento3-Anexos`, según el Comunicado 10) y cuya fuente es `04_Adjuntos/tablas/sd-03_s2_anexo-a_exclusiones-supuestos-restricciones.md`. La dependencia 2 del plan alternativo del crédito (convivencia con la plataforma de 2011) sigue marcada como inferencia del asistente.

> **Ajustes del 2026-10-07 tras los agentes.** Tabla 3.2 sin cambios (se mantienen los códigos EXC). Se agregó: declaración en el cuerpo de que SP-04 se aparta de RT-06.33 y del art. 14.1 en canalizaciones y enlaces (el proponente especifica, costea y certifica; el cliente ejecuta; se validará con el cliente al inicio del proyecto, antes de fijar la línea base); plan alternativo del crédito en forma general con detalle remitido a los capítulos 7 y 8; criterios del cupo propuestos por el proponente y fijados por la filial emisora antes de la prueba; alimentación del registro local desde la plataforma de 2011 para clientes aún no migrados; prueba en los meses 6 y 7 fuera de la semana previa y de los tres días del evento anual; plazo de SP-04; glosas de Comité Ejecutivo y Contraparte Técnica.

> **Párrafo aprobado para la 3.2.3 (2026-10-07): plan alternativo del crédito (S3-02).** La 3.2.2 remite a él. Base: revisión del Informe 1, líneas 503 a 515 y 582 de `80_Artefactos/revision_informe_1_transcripcion.md`; `fundamentacion_credito_sin_conexion.md` §7 y §10; compuerta del punto de venta (condiciones 5 y 9); Caso 13.3.5. El usuario aprobó el párrafo de la dependencia 1 y pidió incluir la dependencia 2.
>
> **Dependencia 1, crédito sin conexión.** La compra con la tarjeta propia durante un corte de enlace se autoriza contra un cupo preaprobado guardado en la tienda, dentro de los topes que fija la filial emisora. Depende de que la filial emisora fije esos topes y de una prueba de factibilidad en las tiendas piloto del punto de venta (meses 6 y 7), con un corte de enlace provocado de 24 horas. Pasa si las compras dentro del tope se autorizan sin perder transacciones, si cada aceptación queda recuperable en el servicio de evidencia financiera y si la conciliación al reconectar termina en 30 minutos o menos sin diferencias sin explicar. Si falla, o los topes no se fijan, la compra con tarjeta propia sin conexión se declara no disponible y la tienda cobra con otro medio de pago. Decide los topes la filial emisora y firma el acta de la prueba la Contraparte Técnica.
>
> **Dependencia 2, convivencia con la plataforma de crédito de 2011 (por validar con el usuario).** Mientras migra la cartera, los clientes que aún no pasan al servicio de cartera de crédito mantienen sus datos en la plataforma de 2011, y la integración con ella debe funcionar. La decisión se toma en la compuerta de cada tramo de la cartera, que exige convivencia real, conciliación diaria de saldos y retorno probado (Caso 13.3.5). Si la integración falla, el tramo no avanza y los clientes pendientes siguen evaluándose en la plataforma de 2011 hasta que se corrija. Esta alternativa es una inferencia del asistente a partir de la compuerta del Caso, no está escrita en el trabajo previo.
>
> **Para ambas.** La alternativa no altera los 56 meses, porque no agrega trabajo al cronograma: la función se declara no disponible o el tramo espera su compuerta.


**Mensaje central.** Cada exclusión dice qué no se hace, qué sí se hace y qué dependencia genera, porque "que algo esté excluido del alcance no significa que pueda ignorarse en el diseño" (Caso cap. 11). Cada supuesto lleva su fundamento y su "Si no se cumple".

**Texto de caída sugerido:** "Delimitar el alcance exige decir con la misma claridad qué no se hará, qué se da por supuesto y qué no puede cambiarse. Esta subsección resume esas tres listas; su detalle está en el anexo."

**Síntesis en el cuerpo.**
- **Exclusiones por origen** (tabla T4):
  - 10 del mandante (EXC-01 a EXC-10, Caso cap. 11);
  - 1 de las Transversales (EXC-11);
  - 7 del proponente (EXC-12, EXC-13 y EXC-15 a EXC-19). EXC-14 está retirada. Total vigente: 18.

  El detalle va en el Anexo A.1.
- **Supuestos con mayor efecto en el alcance:**
  - **SP-01:** el sistema central de 2009 se reemplaza.
  - **SP-02:** Concepción se mantiene como está. El Caso 16.1 n.º 20 admite esta opción; el punto débil se trata en la sección 5.
  - **SP-03:** la compra a cuotas con cupo vigente no exige una nueva entrega de información precontractual.
  - **SP-04:** el cliente provee e instala lo físico. Es una interpretación de las Bases y se declara como tal.
  - Se citan del sd-02 SUP-26 (inicio en enero de 2027) y SUP-27 (11 tiendas cerca de Santiago).

  El detalle va en el Anexo A.2.
- **Responsabilidades del cliente:** son 11 (RC-01 a RC-11). Se mencionan dos o tres en el cuerpo: RC-04 (obras y enlaces), RC-07 (aprobación de cambios en el Comité Ejecutivo) y RC-11 (topes del crédito sin conexión). El detalle va en el Anexo A.3.
- **Restricciones** (propuesta de IDs RS-01 a RS-20, en el Anexo A.4). En el cuerpo se agrupan:
  - separación y evidencia del negocio fiscalizado, RS-01 a RS-03;
  - precio, RS-04;
  - continuidad de la venta, RS-05;
  - sistemas que se conservan, RS-06;
  - garantía, RS-07;
  - cartera, RS-08;
  - calendario, RS-09, RS-10 y RS-19;
  - personas, RS-11 a RS-13;
  - Concepción, RS-14;
  - mapa de integraciones, RS-15;
  - Bases Administrativas, RS-16 a RS-18;
  - requisitos técnicos obligatorios, RS-20.

**Crédito sin conexión.** Merece un párrafo propio, porque el Caso pide que se resuelva "y fundamente, no omitirse" (cap. 15, RT-03.10). Además, la falta de la declaración de RT-03.13 se evalúa como "observación grave".
- **Dos situaciones distintas:**
  - Apertura de tarjeta o ampliación de cupo (unas 520.000 evaluaciones al año, Caso cap. 14): no se hace sin conexión. Lo impiden la restricción 3 (información precontractual antes de la aceptación, sin posponerla), RT-16.14 (firma electrónica en la apertura), la prevención de lavado de activos y la separación de datos.
  - Compra con un cupo ya aprobado: se autoriza contra un caché con topes que fija el Emisor (RC-11), sujeta a la prueba de factibilidad. Si la prueba no pasa, la función queda no disponible.
- **El caché guarda solo** un identificador opaco, un monto máximo, la antigüedad del dato y el estado de bloqueo. No guarda saldo, mora ni comportamiento de pago (restricción 1).
- **El catálogo ya lo recoge** en RF-089 a RF-094 (topes de monto y de número, impedir la apertura y la ampliación, marcar la operación para su validación).
- **Opciones comparadas:** no autorizar crédito sin conexión, caché con topes (la elegida) o un límite fijo para todos.

**Tabla:** T4. **Diagramas:** D4 (frontera y caché) y, opcionalmente, D6 (responsabilidades físicas).

### 1.5 3.2.4 Catálogo de requerimientos

> **Reescrita el 2026-10-08.** El cuerpo de la 3.2.4 narra la metodología en las cuatro actividades de FEP02 · 17 (extraer, analizar, especificar y verificar), la depuración de alcance, la priorización MoSCoW, la trazabilidad y la línea base, el criterio funcional / no funcional (Caso 17.2, Tabla 3.5) y la distribución por etapa (Tabla 3.4). Cifras vigentes: catálogo del capítulo 2 de 307 elementos (223, 75, 9); tras la depuración 303; con cinco requerimientos nuevos para el servicio de clientes Retail (RF-227 a RF-231), **308 (227 RF, 72 RNF, 9 OP)**. Etapas: 142 RF y 61 RNF en la Etapa 1, 4 RF por tramos, 81 RF y 11 RNF en la Etapa 2. Las cifras de esta sección más abajo (140/75/78, mapeo propuesto) quedaron superadas por `conciliacion_catalogo.md` y por el Anexo B (`04_Adjuntos/tablas/sd-03_s2_anexo-b_catalogo-requerimientos.md`). Registro de reglas de negocio en el Anexo C. No se afirma que los saltos de numeración correspondan a requerimientos divididos: son eliminaciones por EXC-02.

**Mensaje central.** El catálogo atomizado se resume por servicio, etapa y prioridad. El criterio de prioridad es el mismo que el de etapa (P1 a P4), así que alcance y catálogo son coherentes. La trazabilidad completa va en el T-12.

**Texto de caída sugerido:** "El alcance se traduce en un catálogo de requerimientos atómicos, verificables uno a uno. Aquí se resume su distribución y el criterio con que se priorizaron; la trazabilidad completa está en el Formulario T-12."

**Datos.**
- El espejo del catálogo (`01_Requerimientos/md/catalogo-de-requerimientos-depurado-v30.md`, del 2026-09-29) tiene 223 RF, 75 RNF y 9 obligaciones del proponente (OP), 307 filas en total.
- AGENTS.md menciona RF-001 a RF-226 y RNF-01 a RNF-76. **Manda el Excel**: confirmar los totales antes de citarlos.

**Mapeo propuesto (S).** Está en `mapeo_requerimientos_3.2.md`, con una fila por requerimiento y las reglas usadas. Síntesis:

| Etapa | RF | RNF | OP |
| :-- | --: | --: | --: |
| Etapa 1 | 140 | 75 | 0 |
| Etapa 1 y 2 (F-02 por olas) | 5 | 0 | 0 |
| Etapa 2 | 78 | 0 | 0 |
| Todo el proyecto | 0 | 0 | 9 |

- **Por servicio (RF):**
  - Etapa 1: R-03 49, R-01 16, R-05 14, F-01 14, F-03 14, identidad 14, X-01 12, plataforma 7.
  - Etapa 2: R-04 35, R-07 25, R-08 12, R-02 3, R-06 3.
  - Por olas: F-02 5.
- **Por prioridad:** Must 150 RF más 75 RNF y 9 OP; Should 73 RF.
- **Revisión:** 26 asignaciones quedaron marcadas para revisar (reservas dentro de pedidos, degradación del evento, crédito sin conexión).

**Hallazgos del mapeo, para el texto o para corregir el catálogo.**
- **R-09 (clientes y fidelización Retail) no tiene ningún RF propio.** Las exigencias de fidelización aparecen solo como restricciones de cruce en Gobernanza de Datos. Hay que decidir si se agregan RF a R-09 o si se explica que su alcance es integrar la fidelización existente (EXC-15).
- **R-02, R-06 y F-02 tienen pocos RF** (3, 3 y 5). R-02 y R-06 son de la Etapa 2, pero F-02 sostiene la migración de 620.000 clientes. Conviene revisar si las repactaciones y la cobranza están bien cubiertas o quedaron dentro de F-03.
- **Los RNF son transversales:** se construyen con la plataforma en la Etapa 1 y se verifican en ambas marchas blancas.

**Criterio MoSCoW propuesto (S):**
- **Must:** el servicio es de primera prioridad (P1 a P3), el requerimiento es RNF u obligación del proponente, o sostiene una restricción no negociable (por ejemplo, la garantía legal, restricción 7).
- **Should:** segundo alcance (Etapa 2).
- **Could:** mejora sobre lo exigido.
- **Won't:** excluido.

El catálogo oficial no tiene hoy ni prioridad, ni servicio, ni etapa. Hay que cargarlos en el Excel antes de citarlos como "priorizado y trazable", que es lo que exige el Comunicado 10.

**Casos limítrofes (Caso 17.2).** El Caso evalúa "el criterio con que el PROPONENTE resuelve estos casos y la consistencia con que aplica su propio criterio".
- **Criterio propuesto (S):** si el enunciado cambia lo que el sistema hace o registra, es RF; si fija cuán bien, cuán rápido o por cuánto tiempo, es RNF; si tiene ambas cosas, se divide en dos. Es la misma regla de atomicidad del catálogo v3.0 (regla 5, separación RF/RNF).
- **Aplicación a los seis casos:**

| Caso del 17.2 | Parte funcional (RF) | Parte no funcional (RNF) |
| :-- | :-- | :-- |
| Evaluación crediticia en 8 s | Evaluar y entregar la información antes de la aceptación | Latencia de 8 s o menos (RT-09.01) |
| Consentimiento acreditable a diez años | Qué se captura en la aceptación (versión, instante, contenido) | Retención por el plazo del crédito más 6 años; recuperabilidad |
| Separación de datos Retail–Emisor | Qué consulta puede formular cada ámbito (X-01) | Segregación técnica y auditabilidad |
| Precio cobrado igual al exhibido | Propagación y registro del precio publicado | Propagación en 5 min o menos; trazabilidad por 5 años |
| Grado de confianza de la existencia | Calcular y mostrar el margen de confianza al vendedor | Consulta en 2 s o menos |
| Evento anual | Quién suspende la publicación de una categoría y con qué criterio; orden de degradación | Capacidad para el pico |

**Tabla:** T5 (es la primera tabla de esta sección, ya validada).

### 1.6 3.2.5 Criterios de aceptación

**Mensaje central.** El alcance se acepta en tres niveles: cada entregable, cada marcha blanca y los resultados de negocio que el cliente usará para juzgar el proyecto.

**Texto de caída sugerido:** "Un alcance sin criterio de aceptación no se puede recibir ni rechazar. Esta subsección fija cómo se verifica lo comprometido en tres niveles, desde el entregable individual hasta el resultado de negocio."

- **Nivel 1, entregable.** Cada uno de los 122 entregables (Anexo B) tiene un criterio con umbral (FEP02, diapositiva 38). La tabla T6 resume por familia de entregables. Ejemplos:
  - R-03: conteo cíclico con menos de 2 % de discrepancia; cancelaciones bajo 0,3 %; consulta en 400 ms o menos; actualización en 30 s o menos; nodo Concepción con su margen de confianza declarado.
  - R-01: discrepancia de 3 % o menos (sd-02); propagación en 5 min o menos; historial recuperable por 5 años.
  - F-01: evaluación en 8 s o menos y prueba del crédito sin conexión.
  - X-01: 100 % de los cruces con finalidad, autorización y registro.
  - POS: compuerta de 9 condiciones.
  - Infraestructura física: acta y certificado de conformidad (1.15.23).
- **Nivel 2, marcha blanca** (Bases Admin. art. 17.3, condiciones copulativas):
  - sin incidentes críticos ni altos abiertos;
  - volumen real comprometido durante las cuatro últimas semanas;
  - disponibilidad y tiempos de respuesta sostenidos;
  - conciliación sin diferencias no explicadas;
  - personal capacitado y certificado;
  - acta de la Contraparte Técnica.

  Si no se cumplen, la marcha blanca se extiende a costo del adjudicatario, sin mover las fechas siguientes.
- **Nivel 3, resultado de negocio** (Caso cap. 18).
  - El Caso dice que estos son "los que el CLIENTE utilizará para juzgar si el PROYECTO fue exitoso". Exige comprometerse con ellos, "proponer la meta cuando este documento no la fije, indicar en qué momento del cronograma se alcanzará cada uno y cómo se medirá".
  - La tabla T7, con los 28 resultados, cumple esa exigencia. Las metas del Caso salen de su cap. 7; las marcadas (S) son propuestas.
  - Los resultados 26, 27 y 28 (Doña Paula, Doña Marisol y Don Jonathan) "son los que mejor resumen el caso". Conviene un párrafo propio para ellos.
- **Validar frente a controlar** (FEP02): el equipo controla la calidad; la Contraparte Técnica valida y firma (entregable 2.14 y RC-08). Los cambios pasan por el Comité Ejecutivo (art. 72).

---

## 2. Diagramas especificados para 3.2

El equipo los dibuja; aquí solo se especifican.
- **Fuente:** editable `.dot` (Graphviz) o `.puml` (PlantUML).
- **Imagen:** PNG en `04_Adjuntos/diagramas/`, con nombre `diag-03-02_<tema>.png`, como `diag-01-02_estructura-corporativa.*`.
- **No usar Mermaid:** el importador lo rechaza.
- **Al insertarlos:** seguir la skill `exportar` (las figuras van en `latex_final/figuras/`). Cada figura lleva número, título y "Fuente: elaboración propia". Los nombres de los nodos son los de 1.1.
- **En el A-6:** un diagrama dibujado por el equipo a partir de esta especificación se declara como nivel bajo o medio de uso de IA, según cuánto se tome de ella.

| ID | Título sugerido | Subsección | Herramienta |
| :-- | :-- | :-- | :-- |
| D1 | Descomposición del alcance: del problema a los servicios (frentes, áreas, servicios y base tecnológica) | 3.2.1 | Graphviz |
| D1b | Cobertura de las causas raíz por servicio (matriz) | 3.2.1 | Graphviz o tabla ilustrada |
| D2 | Dependencias entre servicios y etapa de cada uno | 3.2.2 | Graphviz |
| D3 | Horizonte de 56 meses: etapas, marchas blancas, olas y ventanas | 3.2.2 | PlantUML (Gantt) |
| D4 | Frontera Retail–Emisor y cruces autorizados | 3.2.3 | Graphviz |
| D5 | Destino de las nueve plataformas | 3.2.1 | Graphviz |
| D6 | Reparto de responsabilidades en la infraestructura física | 3.2.3 | Graphviz (opcional) |

**D1, descomposición del alcance (vista general y tres partes).**
- **Muestra:** un árbol de izquierda a derecha.
  - Primer nivel: las 4 promesas.
  - Segundo nivel: las responsabilidades.
  - Tercer nivel: los 13 servicios.
  - Base: la plataforma común (1.14a a 1.14d).
  - Colores distintos para Retail, Emisor y frontera.
- **Aristas:**
  - Existencia → A3, A4, A11 → R-02, R-03, R-04, R-07.
  - Precio → A1, A2, C2 → R-01, R-05, R-06.
  - Entrega → A3, A6, A7, A11 → R-02, R-03, R-04, R-07, R-08.
  - Crédito → B1, B2, B3, C1, C2 → F-01, F-02, F-03, X-01.
- **Partes (RR-12):** una para Retail, una para Emisor y una para frontera con la plataforma. Cada parte se dibuja aparte, sin recortar la vista general (RR-13).
- **Conclusión del texto:** los 13 servicios cubren todas las responsabilidades sin duplicar autoridad, y la frontera es un servicio y no una regla dispersa.

**D2, dependencias y etapa.**
- **Muestra:**
  - Un grafo por capas, de la 0 abajo a la 4 arriba, con flechas "requiere a".
  - El relleno de cada nodo indica su etapa; F-02 lleva dos tonos.
  - Las integraciones críticas aparecen como nodos externos con borde grueso: POS, WMS, comercio electrónico, ERP/DTE y plataforma financiera.
- **Conclusión del texto:** la Etapa 1 contiene todo lo que necesita en sus capas inferiores, y la Etapa 2 solo agrega servicios que dependen de la Etapa 1 sin rehacerla (art. 15). Es la evidencia visual de P3 y P4.

**D3, horizonte de 56 meses.**
- **Muestra:** un Gantt de los meses 1 a 56, de enero de 2027 a agosto de 2031 con el inicio supuesto.
  - Etapa 1: desarrollo en los meses 1 a 12, marcha blanca en los meses 13 a 15 y producción en el mes 16.
  - Etapa 2: desarrollo en los meses 13 a 18, marcha blanca en los meses 19 y 20 y producción en el mes 21.
  - Operación: meses 21 a 56.
  - Hitos: los meses 16 y 21, el retiro de la plataforma de 2011 en el mes 24 y el límite de 2029.
  - Olas: piloto del POS en los meses 6 y 7, ola 2 en los meses 8 a 10, y tramos de la cartera.
  - Franjas sombreadas con las ventanas de congelamiento de 1.3.
- **Conclusión del texto:** los pasos a producción y las olas caen en ventanas libres, y el retiro queda con margen frente a 2029.
- **Ojo:** en 3.2 no se analiza el solapamiento de la marcha blanca de la Etapa 1 con los congelamientos de enero a marzo de 2028. Es materia de riesgos (sd-08). Si el diagrama queda grande, hacer una vista general y luego el detalle de los meses 1 a 24.

**D4, frontera Retail–Emisor.**
- **Muestra:**
  - Dos dominios en recuadros separados.
  - X-01 en el borde, como único paso, con su finalidad, base de autorización, dato mínimo y registro.
  - Flechas tachadas para lo prohibido: un maestro único de clientes, atributos financieros hacia Marketing y saldos de F-02 hacia R-09.
  - Una línea punteada para el caché del crédito sin conexión (identificador opaco y monto, sin saldo).
- **Conclusión del texto:** la separación es estructural y auditable, y está construida antes de cualquier vista unificada (13.3.7; restricción 1).

**D5, destino de las nueve plataformas.**
- **Muestra:** las 9 plataformas a la izquierda y el servicio o la integración que asume cada una a la derecha. El color indica el destino: se conserva, se reemplaza por etapas, se evalúa o se cubre con servicios. Las 14 interfaces punto a punto aparecen como un haz que pasa a la plataforma de integración.
- **Conclusión del texto:** la solución reordena un tejido de sistemas; no reemplaza un sistema legado (Caso cap. 5).

**D6, infraestructura física (opcional).**
- **Muestra:** dos carriles.
  - Cliente: provee, instala y contrata (obras, equipos y enlaces).
  - Proponente: especifica, costea, coordina, certifica y configura; emite el acta y el certificado (1.15.23).
- **Conclusión del texto:** quién responde por qué (SP-04 y EXC-19).

---

## 3. Tablas listas (síntesis para el cuerpo, máximo 5 columnas)

**T1 (eliminada).** La 3.2.1 ya no lleva tabla. La cobertura de causas va en la figura D1b.

**T2, prueba de primera prioridad y etapa de cada componente (3.2.2).** Tabla 3.1 del `.tex`.

| Componente | Prueba que cumple | Etapa |
| :-- | :-- | :-- |
| Base tecnológica e infraestructura híbrida | Registro oficial desde el mes 16 | 1 |
| Servicio de oferta comercial | Promesa priorizada (precio) | 1 |
| Servicio de existencias | Promesa priorizada (existencia) | 1 |
| Servicio de ventas | Registro oficial (venta con documento y sin conexión) | 1 |
| Punto de venta con operación sin conexión | Registro oficial (la tienda vende sin enlace) | 1 |
| Servicio de control de cruces | Objeción registrada (frontera de datos) | 1 |
| Servicio de originación de crédito | Objeción registrada (2029) y registro oficial | 1 |
| Servicio de cartera de crédito | Objeción registrada (2029), por tramos | 1 y 2 |
| Servicio de evidencia financiera | Dependencia de la originación y de la cartera | 1 |
| Servicio de abastecimiento | Ninguna, requiere el servicio de existencias estable | 2 |
| Servicio de pedidos | Ninguna, requiere los servicios de existencias y de ventas | 2 |
| Servicio de comisiones | Ninguna, requiere los servicios de pedidos y de ventas | 2 |
| Servicio de marketplace | Ninguna, requiere el servicio de existencias | 2 |
| Servicio de posventa | Ninguna, requiere los servicios de existencias y de ventas | 2 |
| Servicio de clientes Retail | Ninguna, requiere los servicios de oferta comercial y de control de cruces | 2 |

**T3, capas de dependencia (3.2.2).**

| Capa | Contenido | Requiere a |
| :-- | :-- | :-- |
| 0 | Plataforma, identidad, mapa de las 14 integraciones | — |
| 1 | X-01, F-03, R-01 | Capa 0 |
| 2 | R-03, R-05, F-01 | Capa 1 |
| 3 | R-02, R-04, F-02, R-09 | Capa 2 |
| 4 | R-06, R-07, R-08 | Capa 3 |

**T4, exclusiones por origen (3.2.3).**

| Origen | Cantidad | Ejemplos | Fuente |
| :-- | :-- | :-- | :-- |
| Mandante | 10 (EXC-01 a 10) | ERP, etiquetas electrónicas, dispositivos, cobranza judicial, obras, hardware | Caso cap. 11 |
| Transversales | 1 (EXC-11) | Mesa de ayuda sin aplicaciones del cliente no provistas | Transversales 21.3 |
| Equipo | 8 (EXC-12, 13, 15 a 19) | Concepción como está; sin crédito nuevo sin conexión; lo físico lo provee el cliente | Decisión fundamentada (Anexo A.1) |

**T5, requerimientos por etapa (3.2.4).** Es la tabla de la sección 1.5, o su versión por servicio una vez validada en el Excel.

**T6, familias de entregables (3.2.5).** Conteo desde el Anexo B (122 vigentes):

| Familia | Códigos | Entregables | Etapa | Criterio tipo |
| :-- | :-- | :-- | :-- | :-- |
| Servicios de negocio | 1.1 a 1.13 | 13 | 1 y 2 | Umbrales de RT-09.01 y metas del Caso cap. 7 |
| Plataforma, sistemas, conectores, informes y especificaciones | 1.14a a 1.30 | 24 | 1 y 2 | Contrato publicado; integraciones críticas; informes con alternativas costeadas |
| Infraestructura y sitios | 1.15.1 a 1.15.23 (sin 1.15.18) | 22 | 1 | Instalado por el cliente y certificado por el proponente |
| Portales y aplicaciones | 1.31a a 1.39 | 10 | 1 y 2 | En producción conforme a RT-16.30 y RT-17.01 |
| Gestión del proyecto | 2.1 a 2.16b | 20 | Todo el proyecto | Aprobado por el patrocinador o la Contraparte Técnica |
| Documentación técnica y de transición | 3.1a a 3.15 | 33 | 1 y 2 | Revisado antes de cada paso a producción |

Total: 122 entregables vigentes, contados desde el Anexo B.

**T7, resultados del Caso cap. 18 (3.2.5).** El Caso exige "comprometerse… proponer la meta cuando este documento no la fije, indicar en qué momento del cronograma se alcanzará cada uno y cómo se medirá". Son 28 filas, así que en el cuerpo puede ir una versión agrupada por promesa y la tabla completa en el anexo (RR-18).

| N.º | Resultado (abreviado) | Meta | Servicio | Se alcanza |
| :-- | :-- | :-- | :-- | :-- |
| 1 | Disponible con el error del registro, por categoría y punto | Dinámico y por categoría (Caso cap. 7) | R-03 | Mes 16; piloto por categorías |
| 2 | Cancelaciones por falta de existencia en el umbral | Bajo 0,3 % al año y cero en el evento (Caso cap. 7) | R-03, R-04 | Primer evento anual después del mes 16 |
| 3 | Nadie cobrado por una unidad que no se puede entregar | Cero casos (S) | R-03, R-04 | Mes 21 |
| 4 | Exactitud medida continua y por categoría, sin cerrar la tienda | Conteo cíclico con discrepancia bajo 2 % (Caso cap. 7) | R-03; app 1.38 | Mes 16 en el piloto; mes 21 en las 22 tiendas |
| 5 | Merma separada por causa | 100 % de ajustes con causa (S); merma bajo 1 % (Caso cap. 7) | R-03, R-08 | Mes 21 |
| 6 | Cambio de precio en plazo en caja, canal digital y sala | 5 min o menos en caja y canal digital (RT-09.01); sala según la alternativa del informe 1.25 (S) | R-01 | Mes 16 |
| 7 | Saber qué puntos de exhibición están desactualizados | 100 % de los puntos con estado registrado (S) | R-01 | Mes 16 |
| 8 | Acreditar el precio publicado en un instante | Historial recuperable por 5 años | R-01 | Mes 16 |
| 9 | Precio cobrado igual al exhibido, por muestreo propio | Discrepancia de 3 % o menos (sd-02) (S) | R-01, R-05 | Mes 16 |
| 10 | Estado único del pedido para todos | Tiempo real y consistente (Caso RT-05.29) | R-04 | Mes 21 |
| 11 | Punto de despacho por costo total | 100 % de las asignaciones con costo total (S) | R-04 | Mes 21 |
| 12 | Reconocimiento a la tienda que entrega | 100 % de los despachos desde tienda atribuidos (S) | R-06 | Mes 21 |
| 13 | Devolución de marketplace con procedimiento y aviso al vendedor | Aviso automático en cada devolución (S) | R-07, R-08 | Mes 21 |
| 14 | 310 vendedores evaluados con reglas conocidas | 100 % con nivel de servicio medido (S) | R-07 | Mes 21; renovación anual (13.2) |
| 15 | Garantía legal resuelta en el mesón | Cero derivaciones (restricción 7) | R-08 | Mes 21 |
| 16 | Evaluación crediticia en el umbral | 8 s o menos (RT-09.01; el cap. 7 dice bajo 10 s) | F-01 | Mes 16 |
| 17 | Registro estructurado de la información precontractual | Trazable por operación (Caso cap. 7) | F-03 | Mes 16 |
| 18 | Ninguna repactación sin evidencia | Cero (Caso cap. 7) | F-02, F-03 | Mes 16 (cartera migrada) |
| 19 | Evidencia conservada por el plazo del crédito más el período exigido | Plazo del crédito más 6 años (RT-05.10) | F-03 | Mes 16 |
| 20 | La entrega de información no depende del vendedor | El proceso impide aceptar sin la información (S) | F-01, F-03 | Mes 16 |
| 21 | Separación implementada, documentada y auditada | Implementada y documentada (Caso cap. 7) | X-01 | Mes 16 |
| 22 | Todo cruce registrado | 100 % con finalidad, base y autorización | X-01 | Mes 16 |
| 23 | Hitos de remediación antes de 2029 | Cumplidos (Caso cap. 7) | F-01, F-02, F-03 | Operación, antes de 2029 |
| 24 | Cartera migrada sin pérdida ni divergencia | Cero diferencias no explicadas (restricción 8) | F-02 | Mes 16 (ola 1) y mes 21 (ola 2) |
| 25 | Evento anual con degradación definida y suspensión por categoría | Orden de degradación declarado y probado (S) | Plataforma, R-03 | Mes 16 y cada evento |
| 26 | Doña Paula conoce el estado y se le avisa antes de cobrar | Aviso previo al cobro (Caso RT-16.21) | R-04, R-03 | Mes 21 |
| 27 | Doña Marisol separa pérdida física de error de registro | Diferencias de su tienda con causa atribuida (S) | R-03 | Mes 21 |
| 28 | Don Jonathan abre la tarjeta más rápido y el cliente recibe la información completa | 8 s o menos, con la información obligatoria antes de aceptar | F-01, F-03 | Mes 16 |

Esta tabla tiene 5 columnas y 28 filas: supera RR-18, así que en el cuerpo va agrupada y completa en el anexo.

**Tensión que hay que tratar.** El Caso cap. 7 tiene como referencia "centros de distribución con sistema de gestión de almacenes: 1 de 2, referencia 2 de 2". Esto choca con SP-02 (Concepción se mantiene como está). Defensa: la restricción 14 dice que la incorporación "debe evaluarse y costearse; no puede darse por supuesta", y el 16.1 n.º 20 admite "se mantiene como está". La referencia "2 de 2" queda como meta condicionada al resultado de la evaluación 1.20c y a una eventual solicitud de cambio (art. 72). Hay que decirlo así en 3.2.3 o en 3.2.5.

---

## 4. Cifras con su fuente (RR-06)

| Cifra | Fuente |
| :-- | :-- |
| 9 plataformas, 6 proveedores, 14 interfaces | Caso cap. 5 |
| 22 tiendas en 11 regiones (14 en mall, 8 a la calle), 2 centros de distribución | Caso cap. 2 |
| Insignia: 14.000 m², 17 % de la venta presencial, mesón financiero por piso | Caso cap. 2 |
| 620.000 clientes con saldo vigente; 1.380.000 tarjetas | Caso cap. 2 y cap. 14 |
| 2029: fin de soporte y último hito de remediación | Caso 13.2 |
| Conteo cíclico con 12,4 % de discrepancia; meta bajo 2 % | Caso cap. 7 |
| Merma de 1,9 % de la venta; meta bajo 1 % | Caso cap. 7 |
| Cancelaciones: 1,9 % en el año (meta bajo 0,3 %), 2,7 % en el evento (meta cero), 2.840 casos | Caso cap. 7 y cap. 18 |
| Cumplimiento de la promesa de entrega: 81 %; meta sobre 97 % | Caso cap. 7 |
| Discrepancia de precio: 11 % de 120 productos en 4 tiendas | Caso cap. 7 |
| 1.240 repactaciones sin evidencia; meta cero | Caso cap. 7 |
| Tarjeta propia en el 38 % de la venta de tiendas; unas 520.000 evaluaciones al año | Caso 4.10 y cap. 14 |
| 46 personas de TI; rotación de 62 %; 1.900 de temporada; 1.100 repositores | Caso cap. 2 y cap. 10 |
| Red segmentada en 9 de 22 tiendas | Caso cap. 6 y cap. 7 |
| Meses 1 a 12, 13 a 15, 16, 13 a 18, 19 y 20, 21, 21 a 56 | Bases Admin. art. 17 |
| RTO de 4 h o menos y RPO de 15 min o menos; prueba dos veces al año | Bases Admin. art. 20; Transversales RT-07.07 |
| Operación sin conexión de 24 h | Transversales RT-03.10 (prevalece sobre las 8 h del Caso) |
| Sincronización en 30 min o menos tras la reconexión | Caso RT-03.13 (fijado para 8 h; ver la sección 5) |
| 400 ms, 3 s, 25 s, 8 s, 5 min, 2 s, 60 s | Caso RT-09.01 |
| Disponibilidad actualizada en 30 s; precio en 5 min | Caso RT-05.29 |
| Precio: historial de 3 años (Caso RT-05.10) y auditoría de 5 años (Transversales RT-16.10); se conservan ambos por 5 | Decisión del equipo |
| Consentimiento por el plazo del crédito más 6 años | Caso RT-05.10 |
| 223 RF, 75 RNF, 9 OP | Espejo del catálogo; confirmar en el Excel |

---

## 5. Puntos abiertos (no van como marcadores en el `.tex`)

- **SUP-27 sin validar.** Si no se valida, cae el criterio de zona del piloto del POS.
- **Sincronización tras la reconexión.** El Caso RT-03.13 fija 30 min tras 8 h de desconexión. Nosotros comprometemos 24 h de autonomía y hemos escrito "30 min tras la reconexión". Hay que decidir si los 30 min valen también tras 24 h, que es más exigente, o declarar otro valor con su cálculo. El Caso cap. 14 deja "a estimar" el volumen de datos de una tienda en 8 h.
- **Tensión del Caso cap. 7** ("2 de 2" centros con WMS) frente a SP-02: ver la tabla T7.
- **Paginación de las Bases**, que falta en las citas (RR-20).
- **Etapas marcadas C** en `entregables_alcance.md`, por confirmar.
- **Objetivo general del proyecto**, sin definir.
- **IDs RS-NN:** son una propuesta (Anexo A.4) y requieren aprobación.
- **Catálogo:** falta cargar prioridad, servicio y etapa en el Excel; R-09 no tiene RF y F-02 tiene pocos.
- **Anexo A.4.2 del sd-02** (SUP, EXC y RES): sin conciliar con los IDs del sd-03.
- **Diseño, para el sd-04:** el formato y la periodicidad de la carga de existencias de Concepción, y el pago de cuota y la devolución con reverso sin conexión.
- **Calendario de obras y compras del cliente:** coordinarlo con las ventanas libres en el sd-07.

---

## Anexo A. Tablas completas para el anexo del subdocumento

### A.1 Exclusiones (EXC)

| ID | No se hace | Sí se hace (dependencia) | Fuente |
| :-- | :-- | :-- | :-- |
| EXC-01 | Reemplazar el ERP/DTE ni la emisión de documentos tributarios | Integrarlo como único emisor tributario | Caso cap. 11; restricción 6 |
| EXC-02 | Instalar etiquetas electrónicas en las 22 tiendas | Evaluar, especificar y costear la alternativa (1.25) | Caso cap. 11 |
| EXC-03 | Adquirir dispositivos móviles para el personal de venta | Especificar cuántos y con qué características (1.26) | Caso cap. 11; restricción 11 |
| EXC-04 | Desarrollar la plataforma de vendedores de marketplace ni operar su logística | Integrarla, medirla y resolver la devolución en tienda (R-07, R-08) | Caso cap. 11 |
| EXC-05 | Gestionar remuneraciones | Calcular la base de comisión entre canales (R-06, 1.24) | Caso cap. 11 |
| EXC-06 | Operar la cobranza judicial | Mantener el expediente trazable de cobranza y repactación (F-02, F-03) | Caso cap. 11 |
| EXC-07 | Sustituir a los transportistas de última milla | Integrarlos y trazar el pedido hasta la entrega (R-04, 1.23) | Caso cap. 11 |
| EXC-08 | Construir infraestructura (canalizaciones, obras eléctricas, cableado) | Especificarla y costearla (1.28); la ejecuta el cliente | Caso cap. 11 |
| EXC-09 | Resolver la relación con los administradores de centros comerciales | Diseñar para que su indisponibilidad no detenga la venta (24 h sin conexión) | Caso cap. 11; restricción 5 |
| EXC-10 | Adquirir hardware de tiendas y centros de distribución | Especificar qué comprar, cuánto y con qué características (1.27) | Caso cap. 11 |
| EXC-11 | Atender en la mesa de ayuda las aplicaciones del cliente no provistas | Derivarlas al cliente; la mesa cubre lo provisto | Transversales 21.3, nivel 2 (inferencia) |
| EXC-12 | Reemplazar el marketplace ni el WMS principal | Integrarlos y gobernarlos (R-07, R-03, R-04) | Caso cap. 5 ("se mantiene") |
| EXC-13 | Incorporar Concepción al WMS ni instalar componentes allí | Evaluar y costear (1.20c); R-03 lo modela como nodo con confianza declarada (SP-02) | Caso cap. 5, restricción 14, 16.1 n.º 20 |
| EXC-14 | (Retirada; las planillas son la novena plataforma y se cubren con servicios) | — | Caso cap. 5 |
| EXC-15 | Reemplazar el comercio electrónico ni la fidelización | Evaluarlos e integrarlos con pruebas con umbral (1.20a, 1.20b); el reemplazo solo por cambio | Caso cap. 5 ("se mantiene o se reemplaza, con justificación") |
| EXC-16 | Abrir tarjetas ni ampliar cupos sin conexión | La compra con cupo vigente se autoriza contra un caché con topes del Emisor, sujeta a prueba | Caso 16.1 n.º 7; RT-03.10 y RT-03.13; restricciones 1 a 3 y 5 |
| EXC-17 | Decidir el surtido ni la política de precios | Rediseñar los procesos operativos que los servicios requieren | Caso 9.5 y cap. 16 (decisiones 9 y 18) |
| EXC-18 | Migrar datos históricos fuera de la lista de RT-05.15 | Migrar la lista exigida y dejar un repositorio de consulta (1.30) | Caso RT-05.15; Transversales RT-05.15 |
| EXC-19 | Proveer o instalar equipamiento físico, ejecutar obras o contratar enlaces | Especificar, costear, coordinar, certificar y configurar (SP-04) | Caso cap. 11; Bases Admin. 14.2; RT-06.06 |

### A.2 Supuestos (SP)

| ID | Supuesto | Fundamento | Si no se cumple |
| :-- | :-- | :-- | :-- |
| SP-01 | El sistema central de 2009 no sostiene los objetivos y se reemplaza por etapas | "Corazón del problema de inventario" (cap. 5); lote nocturno; 12,4 %; 11 %; 14 integraciones sin documentar | Si el cliente aporta evidencia en contra, el cambio entra por control de cambios |
| SP-02 | Concepción se mantiene como está durante el contrato | Caso 16.1 n.º 20 (tercera opción); restricción 14; capacidad del cliente | Sin entrega de existencias: confianza mínima del nodo. Si se decide incorporarlo: cambio por el art. 72 |
| SP-03 | La compra a cuotas con cupo vigente no exige nueva información precontractual, o se registra sin conexión | La restricción 3 aplica a la apertura (Caso 4.10) | Se limita o queda no disponible (declarado en RT-03.13) |
| SP-04 | El cliente provee, instala y contrata lo físico | Caso cap. 11; RT-06.06; Bases Admin. 14.2 (interpretación declarada frente a 14.1, RT-06.33 y RT-08.06) | Retraso del cliente: impedimento registrado. Exigencia del mandante: cambio por el art. 72 |
| SUP-26 (sd-02) | Inicio en enero de 2027 | Supuesto de calendario | Se recalculan los meses 16, 21 y 24 y las ventanas |
| SUP-27 (sd-02) | 11 tiendas en el entorno de Santiago | Supuesto de distribución | Se rehace la selección del piloto según la ficha de sitios |

### A.3 Responsabilidades del cliente (RC)

| ID | Responsabilidad | Fuente |
| :-- | :-- | :-- |
| RC-01 | Entregar el informe interno de 2024 sobre la brecha del centro de datos | Caso cap. 5 y RT-06.01 |
| RC-02 | Adquirir, instalar y poner en servicio el hardware y el equipamiento físico especificado | Caso cap. 11; SP-04 |
| RC-03 | Adquirir los dispositivos móviles para el personal de venta | Caso cap. 11; restricción 11 |
| RC-04 | Ejecutar las obras y contratar los enlaces especificados y costeados | Caso cap. 11; RT-06.06; SP-04 |
| RC-05 | Operar la cobranza judicial y gestionar las remuneraciones | Caso cap. 11 |
| RC-06 | Mantener la relación con los administradores de centros comerciales y con los transportistas | Caso cap. 11 |
| RC-07 | Aprobar los cambios mediante el Comité Ejecutivo | Bases Admin. art. 72 |
| RC-08 | Validar y firmar las actas mediante la Contraparte Técnica | Entregable 2.14 |
| RC-09 | Aportar el personal de TI (46 personas) para coordinar, validar y acompañar | Caso cap. 2 y cap. 14 |
| RC-10 | Operar Concepción con sus planillas y entregar sus existencias a R-03 | SP-02 |
| RC-11 | Fijar el apetito de riesgo del crédito sin conexión (topes, antigüedad del caché, exclusiones) | Caso 16.1 n.º 7 |

### A.4 Restricciones (RS), propuesta de IDs (S)

| ID | Restricción | Fuente | Cómo la atiende la solución |
| :-- | :-- | :-- | :-- |
| RS-01 | Separación de datos Retail–Emisor definida, implementada, documentada y auditable | Caso restricción 1 | X-01; segregación de red (1.15.22); D4 |
| RS-02 | Ninguna modificación de crédito sin evidencia recuperable del consentimiento | Caso restricción 2 | F-03; retención por el plazo del crédito más 6 años |
| RS-03 | Información precontractual antes de la aceptación, acreditada de forma estructurada | Caso restricción 3 | F-01 y F-03; el proceso impide omitirla |
| RS-04 | Precio cobrado igual al exhibido, y acreditable por canal e instante | Caso restricción 4 | R-01 (historial, estado de etiqueta), R-05 |
| RS-05 | La tienda sigue vendiendo y cobrando sin enlace | Caso restricción 5 | POS y componente local con 24 h; compuerta del POS |
| RS-06 | El ERP sigue siendo el único emisor tributario | Caso restricción 6 | EXC-01; integración crítica ERP/DTE |
| RS-07 | La garantía legal se ejerce ante la compañía | Caso restricción 7 | R-08; cero derivaciones |
| RS-08 | La migración de 620.000 clientes sin pérdida, sin interrupción ni divergencia | Caso restricción 8 | F-02 por olas y tramos; 13.3.5 |
| RS-09 | Prohibido intervenir sistemas en las ventanas de congelamiento | Caso restricción 9; 13.2; RT-10.05 | Pasos a producción en los meses 16 y 21; olas en ventanas libres |
| RS-10 | La fecha del evento anual la fija un tercero (con unas seis semanas de aviso) | Caso restricción 10 | Degradación definida (T7, n.º 25); holgura en el sd-07 |
| RS-11 | Sin dispositivo por vendedor (640 terminales para 3.820 personas) | Caso restricción 11 | Apps en terminal compartida; EXC-03 |
| RS-12 | No se pueden imponer herramientas a los 1.100 repositores externos | Caso restricción 12 | Solo acceso individualizado (1.14c) |
| RS-13 | Rotación del 62 % y 1.900 incorporaciones de temporada en congelamiento | Caso restricción 13 | Capacitación y certificación (3.7a, 3.7b) |
| RS-14 | Concepción: evaluar y costear; no dar por supuesta su incorporación | Caso restricción 14 | EXC-13, SP-02, 1.20c |
| RS-15 | El mapa de 14 integraciones lo levanta el proponente | Caso restricción 15 | 1.21, primera entrega |
| RS-16 | Despliegue híbrido obligatorio | Bases Admin. art. 16 | Bloque 1.15.x |
| RS-17 | Cronograma de 56 meses, sin plazos alternativos | Bases Admin. art. 17 | Reparto de 3.2.2 |
| RS-18 | Cambios solo por solicitud formal aprobada por el Comité Ejecutivo; límite de 20 % | Bases Admin. art. 72 | RC-07; registro de cambios 2.13 |
| RS-19 | Fin de soporte de la plataforma de crédito y último hito de remediación en 2029 | Caso 13.2 | Financiero en la Etapa 1; retiro con fecha objetivo octubre de 2028 |
| RS-20 | Requisitos técnicos obligatorios de las Transversales | Bases Transversales | Respuesta uno a uno en el Formulario T-12 |

---

## Anexo B. Entregables por etapa (122)

Fuente: `entregables_alcance.md`, versión vigente. Marcas: D = decidido con el usuario; C = derivado de los criterios P1 a P4, por confirmar.

| Código | Entregable | Etapa |
| :-- | :-- | :-- |
| 1.1 | Servicio de catálogo, precios y promociones (R-01) en producción | 1 (D) |
| 1.2 | Servicio de abastecimiento y reposición (R-02) en producción | 2 (D) |
| 1.3 | Servicio de inventario, reservas y disponibilidad (R-03) en producción | 1 (D) |
| 1.4 | Servicio de pedidos y cumplimiento omnicanal (R-04) en producción | 2 (D) |
| 1.5 | Servicio de registro y conciliación de ventas (R-05) en producción | 1 (D) |
| 1.6 | Servicio de atribución de ventas y comisiones (R-06) en producción | 2 (D) |
| 1.7 | Servicio de integración y gobierno de marketplace (R-07) en producción | 2 (D) |
| 1.8 | Servicio de posventa, garantías y devoluciones (R-08) en producción | 2 (D) |
| 1.9 | Servicio de clientes y fidelización Retail (R-09) en producción | 2 (D) |
| 1.10 | Servicio de originación y autorización de crédito (F-01) en producción | 1 (D) |
| 1.11 | Servicio de cartera, cobranza y repactaciones (F-02) en producción | 1 ola 1 y 2 ola 2 (D) |
| 1.12 | Servicio de consentimiento y evidencia financiera (F-03) en producción | 1 (D) |
| 1.13 | Servicio de autorización y auditoría de cruces Retail–Emisor (X-01) en producción | 1 (D) |
| 1.14a | Plataforma de integración en producción | 1 (D, Bases art. 15) |
| 1.14b | Catálogo de reglas de acuerdo por tipo de dato (autoridad, copias y reconciliación) | 1 (D) |
| 1.14c | Servicio de identidad y gestión de accesos en producción | 1 (D, Bases art. 15) |
| 1.14d | Plataforma de observabilidad en producción | 1 (D, Bases art. 15) |
| 1.16 | POS con operación sin conexión de 24 h instalado en las 22 tiendas | 1: ola 1 piloto de 3 tiendas, ola 2 las otras 19 antes del mes 16 (D) |
| 1.17a | Cartera de 620.000 clientes migrada y conciliada | 1 ola 1 y 2 ola 2 (D) |
| 1.17b | Plataforma de originación y cobranza de 2011 retirada | Operación; fecha objetivo octubre de 2028 (D) |
| 1.18a | Conector con el ERP/DTE operando | 1 (D, integración crítica) |
| 1.18b | Conector con el marketplace operando | 2 (D) |
| 1.18c | Conector con el WMS principal operando | 1 (D, integración crítica) |
| 1.19 | Sistema central de retail de 2009 retirado | Migración en 1 y 2; retiro al cierre de la marcha blanca de la Etapa 2 (D) |
| 1.20a | Informe de evaluación del comercio electrónico | 1 (D) |
| 1.20b | Informe de evaluación de fidelización (prueba de separación de datos) | 1 (D) |
| 1.20c | Informe de evaluación y costeo del WMS en el centro de distribución de Concepción | 1 (D) |
| 1.21 | Mapa documentado de las 14 integraciones existentes | 1, primera entrega (D) |
| 1.22 | Conector con la plataforma de comercio electrónico operando | 1 (D, integración crítica) |
| 1.23 | Conectores con empresas de transporte de última milla operando | 2 (C) |
| 1.24 | Conector con el sistema de remuneraciones operando (base de comisión) | 2 (C) |
| 1.25 | Informe de evaluación, especificación y costeo de etiquetas electrónicas | 1 (C) |
| 1.26 | Especificación de dispositivos móviles para el personal de venta (cantidad y características) | 1 (C) |
| 1.27 | Especificación, costeo y calendario de compra del hardware y equipamiento físico que adquiere e instala el cliente (centro de datos, tiendas y centros de distribución) | 1 (C) |
| 1.28 | Especificación, costeo y calendario de obras de infraestructura y enlaces que ejecuta y contrata el cliente | 1 (C) |
| 1.29 | Estrategia de corte de inventario | 1 (D) |
| 1.30 | Repositorio de consulta de datos históricos no migrados | 2 (C) |
| 1.15.1 | Entorno en nube pública multi-zona en producción, con región primaria y secundaria declaradas | 1 (D) |
| 1.15.2 | Repositorio de infraestructura como código del entorno completo | 1 (D) |
| 1.15.3 | Plano y especificación del recinto técnico del centro de datos | 1 (D) |
| 1.15.4 | Plan de cierre de brecha del centro de datos frente al capítulo 6 | 1 (D) |
| 1.15.5 | Sistema de energía ininterrumpida y generación autónoma de 24 h del centro de datos | 1 (D) |
| 1.15.6 | Sistema de climatización de precisión N+1 con monitoreo ambiental del centro de datos | 1 (D) |
| 1.15.7 | Sistema de detección temprana y extinción automática de incendios del centro de datos | 1 (D) |
| 1.15.8 | Sistema de control de acceso físico biométrico y videovigilancia del centro de datos | 1 (D) |
| 1.15.9 | Cómputo, almacenamiento y red del centro de datos operando | 1 (D) |
| 1.15.10 | Rutas de comunicaciones redundantes del centro de datos | 1 (D) |
| 1.15.11 | Espacio de operación del personal habilitado, separado de la sala de equipos | 1 (D) |
| 1.15.12 | Servicio de custodia de medios de respaldo del centro de datos | 1 (D) |
| 1.15.13 | Sitio o región secundaria de recuperación ante desastres operando, con replicación continua | 1 (D) |
| 1.15.14 | Plan de recuperación ante desastres (RTO ≤ 4 h, RPO ≤ 15 min) | 1 (D) |
| 1.15.15 | Solución de respaldo 3-2-1-1-0 operando | 1 (D) |
| 1.15.16 | Informe de prueba de conmutación al sitio secundario (con RTO y RPO medidos) | 1 (D); se repite semestralmente en Operación |
| 1.15.17 | Componentes on-premise operando en el centro de distribución principal, con 24 h de autonomía | 1 (D) |
| 1.15.18 | (Retirado el 2026-10-06; ID conservado) El centro de Concepción se mantiene como está (EXC-13, SP-02) | — |
| 1.15.19 | Gabinete on-premise operando en las 22 tiendas, con 24 h de autonomía | 1 (D); antes de la ola correspondiente del POS |
| 1.15.20 | Red segmentada (cajas, administración, videovigilancia y wifi de clientes) en las 13 tiendas que no la tienen | 1 (D) |
| 1.15.21 | Enlace de respaldo operando en las 7 tiendas que no lo tienen (6 en centro comercial y Coyhaique) | 1 (D) |
| 1.15.22 | Separación acreditada de la red y del ámbito de sistemas de la filial emisora respecto del retail | 1 (D) |
| 1.15.23 | Acta de recepción y certificado de conformidad de obras y equipamiento del cliente (una por sitio) | 1 (C) |
| 1.31a | Portal público (catálogo con precio y disponibilidad e información precontractual con simulador de costo), integrado con la plataforma de comercio electrónico, en producción | 1 (D) |
| 1.31b | Consulta pública del estado de un pedido con su número, integrada con la plataforma de comercio electrónico, en producción | 2 (D) |
| 1.32 | Portal del cliente autenticado (compras, devoluciones, estado de cuenta y documentos), integrado con la plataforma de comercio electrónico, en producción | 2 (C) |
| 1.33 | Vista del vendedor de marketplace (estado de cada pedido, devoluciones y evaluación) sobre el servicio R-07, sin administrar vendedores (EXC-04), en producción | 2 (C) |
| 1.34 | Portal del proveedor (órdenes y recepciones) sobre el servicio R-02 en producción | 2 (C) |
| 1.35 | Aplicación móvil del cliente (compra, seguimiento, devolución y estado de cuenta) en producción | 2 (C) |
| 1.36 | Aplicación móvil del vendedor de sala (consulta de existencia con grado de confianza, en 2 s o menos) en producción en las 22 tiendas | 1 ola 1 (piloto de 3 tiendas) y 2 ola 2 (resto) (D) |
| 1.37 | Aplicación móvil de preparación de pedidos en tienda en producción | 2 (C) |
| 1.38 | Aplicación móvil de conteo cíclico y prevención de pérdidas en producción en las 22 tiendas | 1 ola 1 (piloto de 3 tiendas) y 2 ola 2 (resto) (D) |
| 1.39 | Aplicación móvil de recepción de mercadería en tienda y centro de distribución en producción | 2 (C) |
| 2.1 | Acta de constitución del proyecto | Inicio (D) |
| 2.2a | Registro de interesados | Inicio (D) |
| 2.2b | Estrategia de involucramiento de interesados | Inicio (D) |
| 2.3 | Plan para la dirección del proyecto | Inicio (D) |
| 2.4 | Enunciado del alcance del proyecto | Inicio (D) |
| 2.5a | Documento de requisitos | Inicio (D) |
| 2.5b | Matriz de trazabilidad de requisitos | Inicio (D) |
| 2.6a | EDT | Inicio (D) |
| 2.6b | Diccionario de la EDT | Inicio (D) |
| 2.7 | Línea base del alcance | Inicio (D) |
| 2.8 | Cronograma del proyecto con hitos (línea base) | Inicio (D) |
| 2.9 | Línea base de costos | Inicio (D) |
| 2.10 | Registro de riesgos con plan de respuesta | Inicio (D) |
| 2.11 | Plan de gestión de la calidad | Inicio (D) |
| 2.12 | Informes de desempeño del trabajo | Continuo (D) |
| 2.13 | Registro de solicitudes de cambio | Continuo (D) |
| 2.14 | Actas de aceptación de entregables | Continuo (D) |
| 2.15 | Registro de lecciones aprendidas | Continuo (D) |
| 2.16a | Informe de cierre del proyecto | Cierre (D) |
| 2.16b | Acta de cierre del proyecto | Cierre (D) |
| 3.1a | Documento de arquitectura de la solución | 1, actualiza 2 (C) |
| 3.1b | Registro de decisiones de arquitectura | 1, actualiza 2 (C) |
| 3.2a | Estándares de codificación | 1 (C) |
| 3.2b | Documentación de interfaces | 1, actualiza 2 (C) |
| 3.2c | Diccionario de datos | 1, actualiza 2 (C) |
| 3.2d | Inventario de componentes | 1, actualiza 2 (C) |
| 3.3a | Plan de pruebas | 1, actualiza 2 (C) |
| 3.3b | Casos de prueba | 1, actualiza 2 (C) |
| 3.3c | Informe de pruebas de carga | 1 y 2 (C) |
| 3.3d | Informe de pruebas de resiliencia | 1 y 2 (C) |
| 3.3e | Informe de pruebas de seguridad | 1 y 2 (C) |
| 3.4a | Política de seguridad | 1 (C) |
| 3.4b | Modelo de amenazas | 1, actualiza 2 (C) |
| 3.4c | Matriz de controles de seguridad | 1, actualiza 2 (C) |
| 3.4d | Plan de remediación de seguridad | 1, actualiza 2 (C) |
| 3.5a a 3.5e | Manual de operación; libros de operación; guías de resolución de incidentes; matriz de escalamiento; plan de continuidad y recuperación | 1 y 2 (D) |
| 3.6a | Plan de migración de datos | 1 y 2 (D) |
| 3.6b | Plan de convivencia entre sistemas antiguos y nuevos | 1 y 2 (D) |
| 3.7a | Plan de capacitación del personal del cliente | 1 y 2 (D) |
| 3.7b | Programa de certificación del personal del cliente | 1 y 2 (D) |
| 3.8a | Manuales de usuario por perfil | 1 y 2 (C) |
| 3.8b | Guía de gestión del cambio | 1 y 2 (C) |
| 3.9 | Protocolo de aceptación de hitos y de producto final | 1 y 2 (D) |
| 3.10 | Informe de cierre de marcha blanca (uno por etapa) | 1 y 2 (D) |
| 3.11 | Plan de retiro de la plataforma de originación y cobranza de 2011 | 1 (D) |
| 3.12 | Plan de salida del proveedor de nube | 1 (C) |
| 3.13 | Informe de diligencia reforzada del proveedor de nube | 1 (C) |
| 3.14 | Registro de proveedores externos y servicios externalizados, en el formato del archivo I28 (condicional) | 2, condicional: antes de la primera entrega semestral que exija la norma (C) |
| 3.15 | Política de retención y custodia de datos | 1 (D) |

Nota: 3.5a a 3.5e (manual de operación, libros de operación, guías de resolución de incidentes, matriz de escalamiento y plan de continuidad y recuperación) van en una sola fila, pero son cinco entregables. 1.15.18 está retirado y no se cuenta.
