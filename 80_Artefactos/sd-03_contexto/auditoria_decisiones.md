# Auditoría de la justificación de las decisiones del sd-03

> **Nomenclatura (2026-10-07):** los nombres y códigos de los servicios de este documento (R-01 a X-01) fueron reemplazados. Rige `divisiones_negocio_servicios_sd-03.md`, que contiene la tabla de equivalencias.

Documento de contexto, no es entregable. Fecha: 2026-10-06. No cambia ninguna decisión: evalúa y recomienda. Las decisiones siguen siendo del equipo.

## 1. Qué se evaluó y cómo

Se revisaron 54 decisiones registradas en `80_Artefactos/sd-03_contexto/` (enunciado, descripción del producto, nombres, entregables, asignación a etapas, guía de servicios) y en `80_Artefactos/sd-04_contexto/notas_dr_nube.md`. Cada cita se confirmó abriendo el archivo fuente (`00_Bases/*.md`, `90_Referencia/clases markdown/`, PDF de `90_Referencia/CMF/`).

Cada decisión recibe de 0 a 2 puntos en cinco dimensiones; la nota es la suma (1 a 10):

| Dimensión | 0 | 1 | 2 |
| :-- | :-- | :-- | :-- |
| **A. Fuente** | Sin fuente o no verificable | Citada sin confirmar, o fuente secundaria | Bases, Caso o clase confirmados en el archivo |
| **B. Cadena lógica** | Conclusión sin razonamiento | Razonamiento implícito o con un salto | Premisas, regla y conclusión explícitas |
| **C. Alternativas** | No se consideró otra opción | Alternativa mencionada sin comparar | Alternativas comparadas con un criterio (o no existe alternativa admisible porque la fija el mandante) |
| **D. Consistencia** | Contradice Bases, precedencia u otra decisión | Consistente con una tensión sin resolver | Consistente |
| **E. Verificabilidad** | No se puede comprobar | Verificable sin umbral | Con umbral o evidencia observable (FEP02, diapositiva 38) |

Bandas: **9–10 sólida**, **7–8 aceptable**, **5–6 débil** (reforzar antes de redactar), **1–4 crítica** (reabrir con el equipo).

Origen: **D** = decidida con el usuario; **S** = sugerida por el asistente sin discusión; **M** = fijada por el mandante.

## 2. Resumen

| Categoría | Decisiones con nota | Promedio |
| :-- | :-- | :-- |
| 1. Objetivos y enfoque | 4 | 8,0 |
| 2. Exclusiones y responsabilidades del cliente | 9 | 6,2 |
| 3. Supuestos | 2 | 7,0 |
| 4. Producto y umbrales | 9 | 7,6 |
| 5. Entregables y nombres | 8 | 7,1 |
| 6. Asignación a etapas | 16 | 6,1 |
| 7. Infraestructura y normativa (sd-04) | 4 | 7,3 |
| **Total** | **52** | **6,8** |

Por banda: sólidas 7; aceptables 24; débiles 16; críticas 5.

**Las cinco más débiles**

| ID | Decisión | Nota | Problema central |
| :-- | :-- | :-- | :-- |
| DEC-40 | Olas de F-02: activa primero, cerrada o castigada después | 2 | La premisa no se sostiene: los 620.000 son "clientes con saldo", es decir, casi toda la cartera es activa. La ola 2 queda casi vacía y la Etapa 1 carga la migración completa. Además, faltan las condiciones del Caso 13.3.5 |
| DEC-10 | EXC-14: novena plataforma sin asignar | 2 | No se razonó cuál es. El Caso cap. 5 sí permite identificarla |
| DEC-13 | EXC-17: no rediseñar procesos comerciales | 2 | Sin fuente ni alternativas. Choca con lo que el Caso espera (atribución, conteo cíclico, despacho desde tienda) |
| DEC-46 | F2: e-commerce y fidelización | 4 | Omite el Caso 13.3.6: probar el cambio de disponibilidad en un subconjunto de categorías, midiendo cancelaciones antes y después. Las pruebas no tienen umbral |
| DEC-49 | Etapas sugeridas de portales y apps | 4 | No se discutieron. El portal público (1.31) se solapa con la plataforma de comercio electrónico que se conserva |

## 3. Evaluación por categoría

Columnas: A a E = dimensiones; N = nota.

### 3.1 Objetivos y enfoque (promedio 8,0)

| ID | Decisión | Orig. | A | B | C | D | E | N | Justificación actual | Debilidad | Qué la fortalece |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| DEC-01 | Cinco objetivos específicos | D | 1 | 2 | 1 | 2 | 1 | 7 | Derivados de las causas C1–C5 del sd-02 | No se reconfirmó la traza objetivo → causa en el sd-02; sin indicador por objetivo | Tabla objetivo → causa → umbral de `descripcion_alcance_producto.md` §2 |
| DEC-02 | Objetivo general | — | — | — | — | — | — | s/n | Pendiente | No existe | Redactarlo antes de 3.1 |
| DEC-03 | Ciclo de vida híbrido | D | 2 | 2 | 2 | 2 | 1 | 9 | FEP02·8: suma alzada → predictivo; combinación = híbrido; art. 72 cambios formales | Falta decir qué se itera dentro de cada etapa | Declarar duración de iteración y qué aprueba el Comité |
| DEC-04 | Cinco criterios y su orden | D | 2 | 2 | 1 | 2 | 1 | 8 | Caso 13.1 enumera exactamente dependencias, riesgo, hitos 13.2 y absorción; se antepone Bases y se pospone el comité | No se argumentó por qué el riesgo va antes de la absorción | Una línea que lo justifique (los hitos de 2029 no se negocian; la absorción sí se puede ampliar con dotación) |
| DEC-05 | Regla "más exigente prevalece; si la Transversal remite al caso, rige el caso" | D | 2 | 2 | 1 | 1 | 2 | 8 | Precedencia de AGENTS.md y textos de RT | Se aplicó mal en DEC-19 | Revisar cada umbral con la regla |

### 3.2 Exclusiones y responsabilidades del cliente (promedio 6,2)

| ID | Decisión | Orig. | A | B | C | D | E | N | Justificación actual | Debilidad | Qué la fortalece |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| DEC-06 | EXC-01 a EXC-10 | M | — | — | — | — | — | s/n | Transcripción del Caso cap. 11 | Cita verificada: correcta | — |
| DEC-07 | EXC-11 mesa de ayuda sin aplicaciones del cliente | D | 2 | 1 | 0 | 2 | 1 | 6 | Transversales 21.3, nivel 2: "aplicaciones provistas por el ADJUDICATARIO" | Es una inferencia de una definición, no una exclusión explícita | Decirlo así: "se deduce de" |
| DEC-08 | EXC-12 se mantienen marketplace y WMS | M | 2 | 2 | 2 | 2 | 2 | 10 | Caso cap. 5: "Se mantiene" | — | — |
| DEC-09 | EXC-13 Concepción solo evaluada | M | 2 | 2 | 2 | 2 | 2 | 10 | Restricción 14 | — | — |
| DEC-10 | EXC-14 novena plataforma sin asignar | D | 1 | 0 | 0 | 1 | 0 | 2 | "Se asigna al identificarla" | El Caso cap. 5 lista ocho sistemas, más el motor de precios (no existe), las integraciones y las planillas. La novena se puede razonar desde ahí | Identificarla (candidatas: planillas y listas impresas, o el conjunto de integraciones) y borrar la exclusión |
| DEC-11 | EXC-15 no reemplazar e-commerce ni fidelización | D | 2 | 1 | 1 | 2 | 0 | 6 | Caso: "se mantiene o se reemplaza, con justificación" | La justificación depende de pruebas sin umbral | Definir umbrales de las pruebas (pendiente ya registrado) |
| DEC-12 | EXC-16 no originar crédito nuevo sin conexión | D | 2 | 1 | 1 | 1 | 0 | 5 | F-01; prueba de factibilidad del cupo preaprobado | El Caso RT-03.10 exige "resolverse y fundamentarse, no omitirse"; el crédito es el 38 % de la venta. Falta la fundamentación escrita | Escribir la fundamentación (riesgo de crédito sin evaluación, normativa del Emisor) y la declaración RT-03.13 |
| DEC-13 | EXC-17 no rediseñar procesos comerciales | D | 0 | 1 | 0 | 1 | 0 | 2 | "Los servicios adaptan los procesos que tocan" | Sin fuente; el Caso espera cambios de proceso (atribución, conteo, despacho desde tienda, 9.5) | Acotarla a "surtido y política de precios" con fuente, o eliminarla |
| DEC-14 | EXC-18 sin migrar históricos fuera de RT-05.15 | D | 2 | 2 | 1 | 2 | 2 | 9 | Lista cerrada del Caso RT-05.15; repositorio de consulta (Transversal RT-05.15) | — | — |
| DEC-15 | RC-01 a RC-09 | D | 2 | 2 | 0 | 1 | 1 | 6 | Cap. 11, art. 72, 46 personas de TI (confirmados) | RC-04 (obras del cliente) choca con Transversal RT-06.33 ("el PROPONENTE proveerá toda la conectividad… canalizaciones"), que tiene precedencia sobre el Caso | Resolver la tensión: el Caso no rebaja el requisito, solo reparte la ejecución. Escribir el argumento o pedir aclaración |

### 3.3 Supuestos (promedio 7,0)

| ID | Decisión | Orig. | A | B | C | D | E | N | Justificación actual | Debilidad | Qué la fortalece |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| DEC-16 | SP-01 reemplazo firme del sistema central 2009 | D | 2 | 2 | 1 | 2 | 1 | 8 | "Corazón del problema" (Caso l. 309), 12,4 %, 11 %, 14 integraciones sin documentar; el único informe de brecha es el del centro de datos (todo confirmado) | La opción condicional se descartó por esfuerzo, no por mérito | Agregar el argumento técnico: un sistema por lotes nocturnos no cumple ≤ 30 s ni ≤ 5 min (RT-09.01) |
| DEC-17 | Inicio en enero de 2027 (SUP-26 del sd-02) | D | 1 | 1 | 0 | 2 | 2 | 6 | Supuesto del sd-02 | Todas las fechas del reparto dependen de él | Declararlo con "Si no se cumple" (recalcular meses 16, 21 y 24) |

### 3.4 Producto y umbrales (promedio 7,6)

| ID | Decisión | Orig. | A | B | C | D | E | N | Justificación actual | Debilidad | Qué la fortalece |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| DEC-18 | Operación sin conexión de 24 h | D | 2 | 2 | 1 | 2 | 2 | 9 | Transversal RT-03.10: "24 horas… o el mayor que fije el caso"; Caso 8 h | — | — |
| DEC-19 | Trazabilidad del precio por 5 años | D | 2 | 0 | 1 | 0 | 2 | 5 | "Rige RT-16.10, más exigente que 3 años" | RT-16.10 dice "el que fije el caso"; el Caso fija 3 años (RT-05.10, l. 794 y l. 918). Por la propia regla DEC-05 rige 3 | Elegir: 3 años (rige el Caso) o 5 años como mejora voluntaria declarada, sin atribuirla a RT-16.10 |
| DEC-20 | Evaluación crediticia ≤ 8 s | D | 2 | 2 | 1 | 1 | 2 | 8 | Caso RT-09.01 (confirmado) | El sd-02 sigue diciendo 10 s | Corregir el sd-02 |
| DEC-21 | Umbrales de RT-09.01 (400 ms, 3 s, 25 s, 5 min, 2 s) | M | 2 | 2 | 2 | 2 | 2 | 10 | Caso l. 799 (confirmado) | "≤ 30 s tras una venta" cita RT-05.29, sin confirmar | Confirmar RT-05.29 |
| DEC-22 | Consentimiento: plazo del crédito + 6 años | M | 2 | 2 | 2 | 1 | 2 | 9 | Caso RT-05.10 y l. 381 | El Caso también habla de recuperar "a diez años" (l. 830, 918) | Aclarar que 10 años es el horizonte típico y plazo + 6 el que rige |
| DEC-23 | Autoridad por dato + reglas de reconciliación | D | 1 | 2 | 2 | 2 | 1 | 8 | Caso 16.1 n.º 1 (confirmado); consenso o reconciliación determinista comparados | Art. 17.2 no reconfirmado; "confianza degradada" sin umbral | Confirmar art. 17.2; fijar umbral de confianza en el catálogo 1.14b |
| DEC-24 | Ley 21.719 en el objetivo 4 | D | 2 | 2 | 1 | 1 | 1 | 7 | Caso cap. 12 l. 669; Bases Admin. l. 195 y 635 | `descripcion_alcance_producto.md` dice que no está en el cap. 12: es falso | Borrar esa nota pendiente |
| DEC-25 | Custodia de X-01 (control interno, cumplimiento y auditoría) | D | 1 | 1 | 0 | 2 | 1 | 5 | Análisis de actores | Sin cita del Caso (la objeción de la contralora en 13.1 lo apoya) | Citar Caso 13.1 y 13.3.7 |
| DEC-26 | Reemplazo del POS (no unificar las tres versiones) | D | 2 | 1 | 1 | 2 | 1 | 7 | El POS actual no acredita operación sin conexión; restricción 5 | El Caso pide fundamentar "unificación o reemplazo"; no se compararon | Tabla corta: unificar vs reemplazar frente a las 24 h y RT-09.01 |

### 3.5 Entregables y nombres (promedio 7,1)

| ID | Decisión | Orig. | A | B | C | D | E | N | Justificación actual | Debilidad | Qué la fortalece |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| DEC-27 | Regla de nombres (cinco reglas) | D | 1 | 2 | 1 | 2 | 2 | 8 | Ejemplos reales y FEP02·38 | Los ejemplos no son norma del curso | Citar FEP02·38 como base y los ejemplos como apoyo |
| DEC-28 | Separar 1.14 en a–d | D | 2 | 2 | 1 | 2 | 1 | 8 | Art. 15 nombra seguridad y observabilidad por separado | Sin criterios con umbral (1.14c) | Umbrales en la ronda de criterios |
| DEC-29 | Bloque 1.15.x (23 entregables) | D | 1 | 2 | 1 | 1 | 1 | 6 | Transversales caps. 6 a 8 y Caso | Varias RT no reconfirmadas; tensión RT-06.33 frente a cap. 11 (igual que DEC-15) | Reconfirmar RT; resolver la tensión |
| DEC-30 | Portales y apps como entregables separados | D | 2 | 2 | 1 | 2 | 1 | 8 | Caso RT-16.30 (cuatro portales) y RT-17.01 (cinco perfiles), confirmados | Sin criterios | Criterios con RT de desempeño (página ≤ 2 s) |
| DEC-31 | Separar 2.x y 3.x en documentos | D | 1 | 2 | 1 | 2 | 1 | 7 | Salidas PMBOK; Comunicado 10 | Comunicado 10 (3.4) no reconfirmado | Confirmar |
| DEC-32 | 3.12 plan de salida y 3.13 diligencia reforzada | S | 2 | 1 | 1 | 2 | 1 | 7 | RAN 20-7 (confirmado) | 20-7 es para bancos; se usa por analogía | Declararlo como buena práctica, o citar la norma propia del emisor |
| DEC-33 | 3.14 registro I28 (condicional) | S | 2 | 1 | 1 | 1 | 0 | 5 | Informe CMF abril 2026 (confirmado) | Es propuesta, no norma; el reporte lo envía el emisor, no el proveedor | Reformular como "datos para el archivo I28" o descartar |
| DEC-34 | 1.15.23 acta de recepción de obras por sitio | S | 2 | 2 | 0 | 2 | 2 | 8 | Cap. 11 (obras y hardware del cliente) | No se discutió con el usuario | Aprobar |

### 3.6 Asignación a etapas (promedio 6,1)

| ID | Decisión | Orig. | A | B | C | D | E | N | Justificación actual | Debilidad | Qué la fortalece |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| DEC-35 | A1 definición y lista de integraciones críticas | D | 2 | 2 | 1 | 2 | 1 | 8 | Art. 15; restricciones 1, 4, 5 y 6 | Sin criterio de aceptación por integración | Umbral por integración (por ejemplo, latencia y conciliación) |
| DEC-36 | A2 definición de "primera prioridad" | D | 1 | 1 | 0 | 2 | 1 | 5 | Propia del equipo | El art. 15 dice "definido en las Bases Técnicas del caso"; no se buscó si el Caso la define, ni se derivó | Derivarla del Caso: 13.1 (inventario y precio), 13.3.7 (frontera) y 13.2 (2029) |
| DEC-37 | A3 marketplace en la Etapa 2 | D | 2 | 2 | 1 | 2 | 1 | 8 | Comité 13.1; dependencia de R-03 | No se consideró la renovación anual con los 310 vendedores (13.2) | Fijar la integración tras una renovación anual |
| DEC-38 | B capas de dependencia 0 a 4 | D | 1 | 2 | 0 | 2 | 1 | 6 | Datos bajo autoridad de cada servicio | Inferidas del diseño, sin comparar órdenes alternativos | Una matriz de dependencias por dato (quién lee qué de quién) |
| DEC-39 | C1 financiero en la Etapa 1 | D | 2 | 2 | 1 | 2 | 1 | 8 | Objeción del gerente financiero (13.1, confirmada); 2029 (13.2) | — | — |
| DEC-40 | C2 olas: cartera activa y luego cerrada o castigada | D | 0 | 0 | 0 | 1 | 1 | 2 | Sugerencia del asistente | Los 620.000 son "clientes con saldo" (Caso l. 310 y restricción 8), así que casi todo es activo. La ola 2 queda casi vacía y el balance no se logra. Faltan conciliación diaria, retorno probado y plan de comunicación (13.3.5) | Rediseñar las olas por cohortes (producto, región o tienda de origen), con las condiciones de 13.3.5 como compuerta |
| DEC-41 | C3 retiro en Operación, objetivo diciembre de 2028 | D | 2 | 2 | 1 | 1 | 2 | 8 | Art. 17.3 y 13.3.1 (volver atrás) | Depende de DEC-40 y DEC-17 | Recalcular cuando se rediseñen las olas |
| DEC-42 | D1 reparto de 7 y 6 servicios | D | 2 | 1 | 1 | 2 | 0 | 6 | 46 TI y 62 % de rotación (confirmados) | Cuenta servicios, no carga real (usuarios a capacitar, tiendas, integraciones) | Medida de carga por etapa (personas a capacitar, sitios, migraciones) |
| DEC-43 | D2 POS en dos olas, 3 pilotos, compuerta de 7 condiciones | D | 2 | 2 | 1 | 1 | 2 | 8 | 13.3.4 (por tienda), 17.6 n.º 1, 17.3 (cuatro semanas), RT-09.01 | 13.3.1 exige "posibilidad de volver atrás" y la compuerta no la incluye. El Caso pregunta por la tienda insignia y no se respondió. La ventana de instalación frente a 13.3.3 está sin verificar | Agregar la condición de retorno probado; decir por qué no se empieza por la insignia |
| DEC-44 | E1 desviación: financiero antes que el comité | D | 2 | 2 | 1 | 2 | 1 | 8 | 13.1 "ingeniería, no obediencia" | No se documenta que también se atiende la objeción de la contralora | Agregarla (X-01 en capa 1, 13.3.7) |
| DEC-45 | F1 sistema central por etapas; inventario contable en el ERP | D (en bloque) | 2 | 1 | 1 | 2 | 1 | 7 | Caso l. 309 y l. 316 (el ERP ya lleva la contabilidad) | No se verificó que el ERP pueda valorizar inventario | Supuesto con "Si no se cumple" |
| DEC-46 | F2 e-commerce y fidelización | D (en bloque) | 2 | 1 | 0 | 1 | 0 | 4 | Pruebas en la Etapa 1 | Omite 13.3.6 (probar en un subconjunto de categorías midiendo cancelaciones); pruebas sin umbral | Agregar 13.3.6 y umbrales |
| DEC-47 | F3 corte de inventario en la Etapa 1 | D (en bloque) | 2 | 1 | 0 | 2 | 1 | 6 | RT-05.15 y Caso 17.5 | La estrategia no está definida (conteo total o corte por categoría) | Elegir la estrategia en sd-07 y declararla aquí |
| DEC-48 | F4 gestión y documentación por proceso | D (en bloque) | 1 | 1 | 0 | 2 | 1 | 5 | Grupos de procesos PMBOK | Asignación genérica | Aceptable; verificar con la EDT del sd-07 |
| DEC-49 | Etapas sugeridas de portales y apps (1.31 a 1.39) | S | 1 | 1 | 0 | 1 | 1 | 4 | Dependencias de la Ronda B | No discutidas; 1.31 portal público se solapa con el e-commerce que se conserva | Ronda corta con el usuario; decidir si 1.31 es el e-commerce integrado o un portal nuevo |
| DEC-50 | Etapas sugeridas de 1.23 a 1.28, 1.30 y 1.15.18 | S | 1 | 1 | 0 | 2 | 1 | 5 | Dependencias | No discutidas | Confirmar con el usuario |

### 3.7 Infraestructura y normativa, sd-04 (promedio 7,3)

| ID | Decisión | Orig. | A | B | C | D | E | N | Justificación actual | Debilidad | Qué la fortalece |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| DEC-51 | Reparto sd-03 (qué) / sd-04 (cómo y dónde) | D | 1 | 2 | 1 | 2 | 1 | 7 | Comunicado 10 | No reconfirmado en esta sesión | Citar la línea del Comunicado 10 |
| DEC-52 | Sitio secundario en región de nube | D (preferencia) | 2 | 1 | 1 | 1 | 1 | 6 | Bases Admin. art. 20 "sitio o región" (l. 537); l. 415: región en Chile o Sudamérica | Bases Admin. l. 635: residencia de datos sujeta a aprobación del cliente y transferencia internacional conforme a la Ley 21.719. Sin resolver | Tratarlo en el sd-04: región, residencia y base de licitud |
| DEC-53 | Capítulo 20-7 de la RAN: no obliga a la filial emisora | S | 2 | 2 | 1 | 2 | 1 | 8 | PDF leídos | No se leyó la norma propia del emisor (Circular 1, NCG) | Leerla |
| DEC-54 | Descartar afirmaciones no verificadas de otra IA | D | 2 | 2 | 1 | 2 | 1 | 8 | Contraste con fuentes primarias | — | — |

## 4. Hallazgos transversales

1. **Error de regla (DEC-19):** la trazabilidad de 5 años contradice la regla que el propio equipo fijó. Es el único caso en que una decisión se justificó con una cita mal leída.
2. **Premisa falsa (DEC-40):** las olas de la cartera se armaron sobre un supuesto ("activa / cerrada") que el Caso no sostiene. Arrastra DEC-41 y la carga de la Etapa 1 (DEC-42).
3. **Caso 13.3 no se usó:** las diez condiciones de la estrategia de puesta en producción no se consultaron al decidir las rondas. Faltan 13.3.1 (volver atrás) en el POS, 13.3.5 (cartera) y 13.3.6 (categorías piloto). El 13.3.4 (despliegue por tienda) y el 13.3.7 (frontera antes de la vista unificada) sí respaldan lo decidido.
4. **Corrección propia que no correspondía:** en `guia_servicios_R_F_X.md` se dijo que "X-01 antes de cualquier vista unificada" estaba mal formulado. El Caso usa exactamente esa expresión (13.1, contralora; 13.3.7). La frase original era correcta y conviene restituirla citando la fuente.
5. **Notas obsoletas:** `descripcion_alcance_producto.md` dice que la Ley 21.719 no está en el cap. 12 (sí está, l. 669). El sd-02 sigue con 10 s para la evaluación crediticia.
6. **Tensión Transversales–Caso sin resolver:** RT-06.33 (el proponente provee conectividad y canalizaciones) frente al cap. 11 (las obras las ejecuta el cliente). Afecta a RC-04 y a todo el bloque 1.15.x.
7. **Decisiones aceptadas en bloque:** F1 a F5 y todas las marcadas (S) tienen menos alternativas comparadas (dimensión C promedio cercana a 0). No es un error, pero baja la defensa ante el evaluador del Caso 17.3.
8. **Dependencia de la fecha de inicio:** meses 16, 21 y 24 dependen de SUP-26 (enero de 2027). Debe declararse como supuesto con su consecuencia.

## 5. Recomendaciones priorizadas

**Bloquean la redacción de 3.2 (reabrir con el equipo):**
1. Rediseñar las olas de la cartera (DEC-40) por cohortes, con la conciliación diaria, el retorno probado y el plan de comunicación del Caso 13.3.5. Recalcular DEC-41 y DEC-42.
2. Decidir la trazabilidad del precio (DEC-19): 3 años o 5 años como mejora declarada.
3. Identificar la novena plataforma y cerrar EXC-14 (DEC-10).
4. Revisar EXC-17 (DEC-13): acotarla con fuente o eliminarla.
5. Agregar a la compuerta del POS la condición de retorno probado (13.3.1) y responder por qué no se parte por la tienda insignia (DEC-43).
6. Agregar a F2 el piloto por categorías del Caso 13.3.6 (DEC-46).

**Antes de entregar el sd-03:**
7. Escribir la fundamentación del crédito sin conexión (DEC-12) y la declaración de RT-03.13.
8. Resolver y escribir la tensión RT-06.33 frente al cap. 11 (DEC-15, DEC-29).
9. Derivar "primera prioridad" del Caso (DEC-36).
10. Discutir las etapas (S) de portales y apps, y el solape de 1.31 con el comercio electrónico (DEC-49, DEC-50).
11. Declarar SUP-26 con "Si no se cumple" (DEC-17).

**Limpieza (sin decisión nueva):**
12. Restituir la frase de X-01 con la cita del Caso 13.1 y 13.3.7 en la guía de servicios.
13. Borrar la nota falsa sobre la Ley 21.719 y corregir los 10 s del sd-02.
14. Reconfirmar RT-05.29, art. 17.2 y Comunicado 10 (3.4).

## 6. Seguimiento (2026-10-06, después del informe)

| Decisión | Resolución | Nota esperada |
| :-- | :-- | :-- |
| DEC-40 olas de la cartera | Opción B: por complejidad, tramos crecientes y condiciones del Caso 13.3.5 como compuerta (`asignacion_etapas.md`, C2). Queda como supuesto la proporción de cada ola | de 2 a 8 |
| DEC-10 novena plataforma | Son las planillas; EXC-14 retirada; cobertura en `descripcion_alcance_producto.md` §4.2 | de 2 a 8 |
| DEC-13 EXC-17 | Reformulada con fuente y frontera clara | de 2 a 7 |
| DEC-46 e-commerce y fidelización | Piloto por categorías (13.3.6) y umbrales agregados | de 4 a 8 |
| DEC-49 portales | Lectura aceptada: ventanas sobre los servicios; nombres de 1.31 a 1.34 redefinidos. Etapas por discutir | de 4 a 7 (1.31 y apps de sala decididos; faltan 1.32 a 1.35, 1.37 y 1.39) |
| Concepción (nueva, EXC-13 y SP-02) | Centro se mantiene como está (Caso 16.1 n.º 20, tercera opción); puntos débiles declarados como dependencias con "Si no se cumple"; 1.15.18 retirado; RC-10 agregado | Nota inicial esperada: 7 |
| DEC-19 trazabilidad del precio a 5 años | Se mantiene en 5 años con fundamento corregido: historial 3 años (Caso, RT-05.10) y auditoría de cambios 5 años (RT-16.10); la diferencia del historial es mejora declarada | de 5 a 8 |
| DEC-43 compuerta del POS | Agregado el retorno probado (condición 8), la convivencia, el porqué de no partir por una insignia y las ventanas de instalación (Caso 13.3.1 y 13.3.3) | de 8 a 9 |
| DEC-12 EXC-16 y crédito sin conexión | Fundamentación escrita (`fundamentacion_credito_sin_conexion.md`): dos situaciones, tres opciones comparadas, caché mínimo, topes del Emisor (RC-11), prueba de factibilidad y tabla RT-03.13; SP-03 agregado | de 5 a 8 |
| DEC-15 y DEC-29 obras y equipos | Resueltas: SP-04 y EXC-19 con la interpretación declarada de Bases Admin. 14.1 y 14.2 y de RT-06.33 y RT-08.06, y "Si no se cumple"; RC-02 y RC-04 reescritas | DEC-15 de 6 a 7; DEC-29 de 6 a 7 (queda como interpretación que podría objetarse) |
| DEC-43 selección de tiendas piloto | Método integrado: 3 tiendas del entorno de Santiago de volumen medio o bajo, insignia fuera del primer corte (17 % de la venta presencial), cobertura de las tres versiones del POS y seis criterios de ficha. Depende de SUP-27 (sin validar) | de 9 a 9 (se mantiene; mejora la defensa frente al Caso 17.6) |
| DEC-36 primera prioridad | Derivada del Caso con cuatro criterios (P1 a P4: comité, objeciones, sistema de registro oficial de la Etapa 1, dependencia técnica) y aplicada servicio por servicio; el orden del comité es una entrada, no la respuesta (Caso 13.1) | de 5 a 8 |
| DEC-49 y DEC-50 etapas sugeridas | Derivadas con los criterios P1 a P4 (Ronda G); una cambia (3.14 a la Etapa 2); marca C por confirmar | DEC-49 de 7 a 8; DEC-50 de 5 a 8 |

### Reconfirmaciones hechas el 2026-10-06
- **RT-05.29:** confirmado en el Caso (cap. 15): disponibilidad publicada actualizada en 30 s o menos tras una venta en cualquier canal; precio en 5 min o menos; estado del pedido en tiempo real. Respalda DEC-21.
- **Bases Admin. art. 17.2 (punto 2):** confirmado: "una única fuente de verdad para los datos compartidos por ambos alcances y evitar toda doble digitación". Respalda DEC-23.
- **Comunicado 10:** confirmado que 3.4 incluye la estrategia para obtener el apoyo de los grupos de interés de 2.4, y que 4.2, 4.2.1, 4.3.1 y 4.3.2 son del sd-04 (física, implementos, data center primario y secundario con región o sitio, replicación, RPO, RTO y conmutación). Respalda DEC-31 y DEC-51. Se precisó en 2.2b que la estrategia está dentro de 3.4, no es un capítulo aparte.
- **Limpiezas aplicadas:** frase de X-01 restituida en la guía de servicios; nota falsa sobre la Ley 21.719 corregida en `descripcion_alcance_producto.md`; evaluación crediticia de 8 s corregida en `sd-02.tex` y su espejo `.md` (con la razón recalculada: 5 a 22,5 veces).
