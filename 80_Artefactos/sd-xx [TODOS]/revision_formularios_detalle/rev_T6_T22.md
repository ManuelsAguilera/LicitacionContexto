> Detalle de la revisión de los formularios (2026-10-12). Borrador. **Nota:** cualquier hallazgo que diga que el Comité de Operación debe iniciar en el mes 16 es un falso positivo: el artículo 71 de las Bases fija «mensual desde el mes 13».

# Revisión de los Formularios T-6 y T-22

Archivos: `02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-6.tex` y `...-T-22.tex`. Rutas relativas al repo. Solo lectura.

Definición oficial: T-6 en `00_Bases/Bases_Administrativas.md:2042-2062` (y Art. 34.1 en líneas 840-848); T-22 en `Bases_Administrativas.md:2426-2490` (Arts. 45-47 en líneas 1074-1098). Comunicado 10 en `00_Bases/Comunicado_10_...md`.

Nota de alcance: el archivo "T-22" no reproduce el contenido de los tres informes. Es la tabla de trazabilidad observación-respuesta-sección modificada que exige el Art. 46 para el Informe 2 (corregir las observaciones del Informe 1). Eso es coherente con T-22 (Informe 2, primer punto), pero hay que verificar que la tabla cubre las observaciones reales (fuente: `80_Artefactos/revision_informe_1_transcripcion.md`).

Resumen: 4 graves, 9 medianas, 6 bajas.

---

## FORMULARIO T-6

### T6-01 (grave, confirmado) Falta el campo "Alcance ejecutado"
- Ubicación: T-6.tex líneas 131-140 (las 10 filas de la tabla).
- Dice: filas Nombre, Cliente, Industria, Año, Monto, Arquitectura, Nivel de servicio, Volumen, Rol, Contraparte.
- Debería: el T-6 oficial (Bases 2046-2062) pide 11 campos; falta "Alcance ejecutado" (viene entre "Monto del contrato" y "Arquitectura"). La revisión del Informe 1 también lo pedía: "cliente ficticio, período, monto, alcance, SLA, híbrido, contraparte" (transcripción, p. 5, "Qué se espera en el Informe 2").
- Sugerencia: agregar la fila "Alcance ejecutado" con 2-3 líneas por proyecto (el sd-01 1.4 ya describe la capacidad que aportó cada uno: POS con operación sin conexión, consentimiento para emisor fiscalizado, ATP omnicanal con marketplace). Es un campo habilitante: el Art. 34.1 exige el T-6 "con datos verificables".

### T6-02 (grave, confirmado) Contrapartes sin nombre ni contacto
- Ubicación: T-6.tex línea 140.
- Dice: "Gerente de Tecnología de ... -- contacto disponible a solicitud" (x3).
- Debería: el T-6 pide "Contraparte de referencia y contacto" y el Art. 34.1 (Bases 846) exige "datos verificables de contraparte". El CLIENTE "verificará directamente con las contrapartes declaradas" (Bases 2044). "Disponible a solicitud" no es un dato verificable. La revisión del Informe 1 lo marcó como crítico: "contraparte con nombre, cargo y contacto" (transcripción pp. 4-5).
- Sugerencia: poner nombre ficticio, cargo, correo y teléfono (todo ficticio, Art. 93). Además la respuesta 1-4 del T-22 afirma que se declaró la "contraparte por cargo", lo que no cubre lo pedido.

### T6-03 (grave, por confirmar) Cliente real nombrado: "Distribuidora Textil y Calzado Hites & Cía."
- Ubicación: T-6.tex línea 132 (proyecto 3); también "Multitiendas Prat S.A." y "Financiera Solución S.A." (por confirmar si son marcas reales).
- Dice: nombre de una empresa chilena real.
- Debería: la revisión del Informe 1 lo calificó de crítico y causal de exclusión: "una empresa real como cliente (Art. 13.4/93°)" (transcripción p. 5 y "Admisibilidad"), y pidió "reemplazar Hites, CMF y Sernac por nombres ficticios". La observación no está en la tabla del T-22 (ver T22-02) y el T-6 sigue igual.
- Sugerencia: reemplazar por nombres claramente ficticios en los tres proyectos y actualizar de forma consistente el sd-01 (1.4 no nombra clientes; revisar el anexo y las demás menciones). Confirmar si Prat y Solución son marcas reales.

### T6-04 (mediana, confirmado) No se indica qué proyecto acredita la arquitectura híbrida y cuál el SLA >= 99,5 %
- Ubicación: T-6.tex líneas 136-137.
- Dice: P1 híbrida con SLA 99,5 %; P2 nube 99,9 %; P3 híbrida 99,9 %. Cumple materialmente el Art. 34.1 (Bases 848), pero no lo declara.
- Debería: la revisión pidió "indicar cuál proyecto acredita híbrido y cuál SLA >= 99,5 %" (transcripción p. 5).
- Sugerencia: añadir una nota bajo la tabla ("Acreditan arquitectura híbrida: proyectos 1 y 3; acreditan SLA >= 99,5 %: los tres"). También: el Art. 34.1 exige "carta de referencia del mandante" junto al T-6 (Bases 848); no aparece mencionada en el T-6 ni en el sd-01 (no hay "carta de referencia" en ningún `.tex`). Mencionarla como adjunto por acreditar.

### T6-05 (mediana, confirmado) El proyecto 1 declara continuidad sin conexión de 12 h, contra las 24 h comprometidas
- Ubicación: T-6.tex líneas 137-138 ("continuidad offline mínima de 12 h", "operación offline mínima de 12 h").
- Dice: 12 h. La revisión del Informe 1 lo marcó: "el proyecto 1 promete más de lo que la oferta entrega ... tres cifras" (transcripción p. 5). La verdad vigente compromete 24 h (Bases piden 24 h o el mayor).
- Sugerencia: no es contradicción formal (es un proyecto pasado), pero un evaluador lo leerá como capacidad probada de solo 12 h. Redactar como "al menos 12 h verificadas" y explicar en el sd-01 1.4 cómo se llega a las 24 h (piloto de corte de 24 h, meses 6 y 7). Alternativa: declarar para el proyecto 1 la autonomía real lograda si fue mayor.

### T6-06 (mediana, por confirmar) Falta declarar "finalizado y en operación" y su misión crítica
- Ubicación: T-6.tex tabla completa; la introducción (línea 93) solo dice "proyectos de referencia ejecutados ... como contratista principal".
- Debería: Bases 2043 y Art. 34.1: "proyectos finalizados y en operación en los últimos cinco años". Los años (2022-2023, 2024-2024, 2023-2024) cumplen la ventana, pero el formulario no dice que estén en operación ni que sean de misión crítica.
- Sugerencia: agregar en "Año de inicio y de término" el estado ("finalizado en ...; en operación") o una línea en la introducción. En el proyecto 2 el rango "2024 -- 2024" se lee mal; usar "enero -- noviembre de 2024" (fechas que usó el Informe 1).

### T6-07 (mediana, por confirmar) Sectores del sd-01 sin respaldo en el T-6
- Ubicación: sd-01 1.1 (OnlySimpleSolutions-Subdocumento1.tex:108 y 114: "banca, seguros, logística a gran escala, telecomunicaciones y retail"; "14 proyectos desde 2016, 6 vigentes ... banca, retail, logística, telecomunicaciones y seguros") frente a T-6 (retail, servicios financieros, comercio electrónico).
- Dice: el T-6 solo acredita retail, emisor de crédito y comercio electrónico. La revisión del Informe 1 ya lo anotó ("declara sectores bancario, logística, telecomunicaciones ... sin un proyecto ... en la experiencia", transcripción p. 4).
- Sugerencia: no es error del T-6 en sí; confirmar con el equipo si los otros 11 proyectos son de esos sectores. Opción: decir en el sd-01 1.4 que los tres de referencia son los más pertinentes de los 14 y que los demás sectores se respaldan con los 14 proyectos. Los 85 profesionales y la relación con los 6 proyectos vigentes no aparecen en el T-6 (correcto; no lo pide).

### T6-08 (baja, confirmado) Encabezado y numeración
- Ubicación: T-6.tex línea 86 (`\ossCover{...}{Subdocumento 1 · T-6}`) y líneas 96-97 (`\thefigure`/`\thetable` = "1.x").
- Dice: portada "Subdocumento 1 · T-6"; la tabla se numera como Tabla 1.x. Las Bases y el Comunicado 10 piden formulario en archivo propio y no subdocumento; además la numeración 1.x puede chocar con las tablas del sd-01 (el sd-01 tiene tablas 1.x).
- Sugerencia: portada "Formulario T-6" (como el T-22: "Formulario T-22") y numeración propia (Tabla T6-1 o sin número).

### T6-09 (baja) Formato
- Los montos y el SLA van en negrita y los campos tienen negrita desigual; la introducción dice "tres proyectos de referencia ejecutados como contratista principal" y la remisión a "sección 1.4 del Subdocumento 1" es correcta (existe 1.4). Sin otros hallazgos. Los montos de contratos anteriores son rangos pasados, no precios de esta oferta; no infringen el Art. 50.

Contrastes sin hallazgo: el rol "Contratista principal" coincide con sd-01 1.4 (línea 281); los tres proyectos y sus capacidades coinciden con las viñetas de sd-01 1.4; el sd-01 1.1 declara 14 proyectos y 85 profesionales y ninguno de esos datos se contradice en el T-6.

---

## FORMULARIO T-22 (tabla de correcciones del Informe 1)

### T22-01 (grave, confirmado) Observaciones del Informe 1 sin fila en la tabla
El Art. 46 exige "la resolución explícita de las observaciones". Se compararon las secciones "Qué se espera en el Informe 2" de la transcripción con las filas del T-22. No tienen fila (o quedan cubiertas solo en parte):
- Sd-1: Formulario T-8 con currículos y certificaciones individuales (ITIL, gobierno TI, motor de base de datos); reemplazo de clientes reales; indicar qué proyecto acredita híbrido y SLA; acreditar nivel o identificador de socio de Azure (1-8 solo dice "una sola alianza"); sectores sin proyecto; las 12 h del proyecto 1 (transcripción pp. 3-5).
- Sd-2: dar valor a SUP-04, SUP-12 y SUP-16 y a las horas de etiquetado manual (2-10 cubre otros cálculos).
- Sd-3: leyenda de la T-12 (cumple / se entrega en el Informe N / no aplica / no cumple con desviación fundada) y revisión de los 98 "No" y los "Sí" sin evidencia (RT-05.01, RT-03.10).
- Sd-4.1: completar las cuatro dimensiones faltantes del numeral 14.2 (datos en la ventana sin enlace, sincronización, ancho de banda por CD, dotación); dimensionar el nodo de tienda para 24 h (folios, caché, GB, UPS, drenaje). 4-10 solo "retira" las cifras erróneas.
- Sd-4.2: Formulario T-11 completo, UPS y autonomía del nodo; condición de socio de Microsoft.
- Sd-5: plan de comunicación a los 620.000 clientes; re-sellado de firmas y migración de formato a diez años del expediente de consentimiento.
- Transversal: folio correlativo único y media firma (Art. 40); el revisor listó la ausencia de T-22, A-6, folio y firma como causal.
- Sugerencia: agregar las filas con su respuesta o con la remisión al formulario donde se resuelve (T-8, T-11, T-12). Si algo no se corrigió, decirlo así. Al ser vinculantes (Art. 47.1), la omisión se evalúa como observación grave.

### T22-02 (grave, confirmado) La fila 1-4 oculta que el cliente real no se corrigió
- Ubicación: T-22.tex línea ~175 (fila 1-4) y T-6.tex línea 132.
- Dice: "Se elaboró el Formulario T-6 ... con monto en rango, arquitectura, SLA comprometido y contraparte por cargo para cada proyecto".
- Debería: la revisión pedía además nombre, cargo y contacto de contraparte, alcance, y clientes ficticios. La respuesta afirma un cumplimiento que el T-6 no tiene (ver T6-01 a T6-03). Una respuesta inexacta en la tabla de trazabilidad es peor que no tenerla.
- Sugerencia: corregir primero el T-6 y luego reescribir la fila 1-4 con la lista exacta de campos, o abrir filas separadas para cada observación (real vs. ficticio, contacto, qué proyecto acredita qué).

### T22-03 (mediana, confirmado) Remisiones al "Anexo A.5.1" del sd-02 que no existe
- Ubicación: T-22.tex filas 2-5, 2-7, 2-12, 2-15, 2-16, 2-17 y 2-19 (columna "Sección modificada").
- Dice: "Anexo A.5.1" (SUP-07, 08, 17, 19, 25).
- Debería: en `sd-02/OnlySimpleSolutions-Subdocumento2-Anexos.tex` los supuestos están en "A.4.1 Listado de Supuestos" (línea 1827; SUP-07 en 1870, SUP-25 en 1906). No hay A.5. El sd-02 mismo remite al "Anexo A.4" (Subdocumento2.tex:785). El glosario común también dice "sd-02 A.5", así que el error nació ahí.
- Sugerencia: cambiar a "Anexo A.4.1" en el T-22 (y corregir el glosario). Es el mismo tipo de error (remisiones inexistentes) que la fila G-5 dice haber eliminado.

### T22-04 (mediana, confirmado) Fila 3-2: descripción de las figuras del sd-03 desactualizada
- Ubicación: T-22.tex fila 3-2.
- Dice: "ocho figuras de la solución: selección del escenario, contexto con los tres frentes, Retail, Emisor, intercambios, recorrido Retail, originación y compra con tarjeta ... 3.3.1 (Figura 3.1); 3.3.2 (Figuras 3.2 a 3.5); 3.4.3 y 3.4.4 (Figuras 3.6 a 3.8)".
- Debería: el sd-03 actual (OnlySimpleSolutions-Subdocumento3.tex) tiene las Figuras 3.1-3.8 en 3.1 y 3.2 (mapa de servicios, horizonte de 56 meses, cobertura de causas, destino de plataformas, dependencias, migración de cartera, frontera y cruces, niveles de aceptación; líneas 104-374) y las figuras de selección de escenario, contexto, Retail, Emisor, escenarios de cruce, recorrido, originación y autorización de compra en 3.3 y 3.4 numeradas 3.9 a 3.16 (líneas 452-705). Son 16 figuras, no 8, y las secciones citadas son otras.
- Sugerencia: reescribir la fila: "dieciséis figuras (3.1 a 3.16): 3.1-3.8 en 3.1 y 3.2; 3.9-3.16 en 3.3 y 3.4". Confirmar la numeración final tras el cambio de Prism (commits recientes "Apunta las figuras 3.1 a 3.8 ...").

### T22-05 (mediana, por confirmar) Fila 3-5: tabla equivocada
- Dice: "3.4.2 La promesa de precio; 3.2.4 (Tabla 3.5)".
- Debería: los supuestos (donde estaba SUP-09) están en 3.2.3, Tabla 3.3 (sd-03:261). La Tabla 3.5 es el criterio de casos limítrofes del catálogo (línea 342). Además, el SUP-09 actual del sd-02 trata de etiquetas electrónicas, no de retención de precio; la fila describe lo que se retiró del texto antiguo (aceptable) pero la remisión debe apuntar al sitio vigente.
- Sugerencia: "3.4.2; 3.2.3 (Tabla 3.3)".

### T22-06 (mediana, confirmado) Filas 4-x: números de tabla del sd-04 desfasados
- Ubicación: T-22.tex filas 4-5, 4-7, 4-18, 4-21, 4-25, 4-27, 4-28, 4-29.
- Dice (ejemplos): 4-7 "Tablas 4.8 y 4.9" (sitios y tecnologías); 4-21 "Tablas 4.7 y 4.8"; 4-28 "Tabla 4.8; 4.2.1 (Tabla 4.11)" para enlaces; 4-5 "4.2 (Tabla 4.10)".
- Debería: según sd-04 vigente: tecnologías = Tabla 4.6; emplazamiento por sitio = 4.7; red = 4.9; subredes = 4.10; puntos de falla = 4.11; fallas por zona = 4.12; dimensionamiento = 4.14; hardware = 4.15; sitios/fallas de DC = 4.16 (Subdocumento4.tex:419, 502, 540, 574, 608, 642, 685, 738, 760). La Tabla 4.5 (ADR) sí coincide.
- Sugerencia: regenerar todas las remisiones del sd-04 contra el texto vigente. También: la fila 4-1 dice "Figuras 4.1 a 4.11" y 4-3 "doce figuras"; el sd-04 tiene 4.1 a 4.12 en la sección 4.1 (las seis vistas de bloque son 4.4 a 4.9).

### T22-07 (mediana, confirmado) Fila 4-14: "Azure Cache for Redis"
- Dice: "Se definió un solo producto, Azure Cache for Redis".
- Debería: el sd-04 usa "Azure Managed Redis" (líneas 439, 535, 772) y explica que Azure Cache for Redis se retira el 30-sep-2028 (línea 439). La verdad vigente: "Azure Managed Redis (solo Retail)".
- Sugerencia: corregir a Azure Managed Redis. Además el sd-04 (línea 445) deja el motor local de la tienda "Valkey u otro motor local, por decidir", mientras la fila 5-4 y el sd-05 (355, 425) dicen "PostgreSQL local para el diario de tienda"; la fila 4-14 dice solo "su propio diario y caché de oferta". Confirmar cuál es el vigente y alinearlos (esto es una incoherencia sd-04 / sd-05 que el T-22 repite).

### T22-08 (mediana, por confirmar) Fila 5-11: "cartera de 620.000 tarjetas con saldo"
- Dice: "la cartera de 620.000 tarjetas con saldo".
- Debería: la verdad vigente y el Caso (línea 129 y 310) distinguen 1.380.000 tarjetas emitidas y 620.000 clientes con saldo. El sd-05 mismo mezcla (línea 528 "620.000 clientes con saldo"; tabla de 542 "620.000 tarjetas con saldo vigente"). Es la misma confusión de unidad (cuentas, clientes, tarjetas).
- Sugerencia: escribir "620.000 clientes con saldo" y corregir también la tabla del sd-05.

### T22-09 (baja, confirmado) Fila G-1: declaración de uso de IA en cuatro subdocumentos
- Dice: "Subdocumentos 1, 2, 5 y 13". Los sd-03 y sd-04 también incluyen la sección (Declaración de uso de IA, 2 menciones cada uno) y el Informe 1 cubre 1, 2, 3, 4, 5 y 13.
- Sugerencia: "Subdocumentos 1, 2, 3, 4, 5 y 13".

### T22-10 (baja, por confirmar) Cifras que cambian: "13 entradas" y "16 entradas" de referencias
- Filas 2-4 (sd-02: 13) y 4-20 (sd-04: 16). El sd-02 vigente tiene 14 referencias (Subdocumento2.tex:787 en adelante); el sd-04 parece tener más de 16. Recontar antes de cerrar.

### T22-11 (baja) Lenguaje de glosario y rol
- Fila 1-7: "comités con el mandante"; el glosario: "mandante" solo en la licitación, usar "Cliente" en ejecución. Fila 4-29: "Cliente" correcto. Sin otros nombres fuera de glosario.

### T22-12 (baja, por confirmar) El archivo no lleva sección de Referencias ni Declaración de uso de IA
- El Comunicado 10 (secciones 7.2, 8, 9, líneas 141 y 354) lo exige al final de cada subdocumento; un formulario no es subdocumento, pero el sd-01 lista el T-6 en su tabla de declaración de IA y el T-22 no tiene fila en ningún subdocumento. Si la tabla de trazabilidad se arma con asistente, conviene declararlo en el sd-01 o en el propio archivo.

### Contrastes sin hallazgo (T-22)
- Cita del Art. 46 correcta (Bases 1092).
- Cifras que coinciden con la verdad vigente: 24 h de autonomía (G-7, 3-6, 4-7, 4-27), RTO 4 h / RPO 15 min (4-26), siete ADR (G-6), Event Hubs Premium, PostgreSQL Flexible, Java 25 y Spring Boot 4, 227 RF + 72 RNF + 9 OP, versión 3.1, piloto de corte de 24 h en meses 6 y 7 con conciliación en 30 min (3-7, coincide con sd-03:300), marchas blancas 13-15 y 19-20, 56 meses hasta el mes 56, ensayos de migración (sd-05 Tabla 5.14), Ley 21.719 desde el 1-dic-2026, 51 entidades / 314 campos / 81 relaciones (Anexo del sd-05), 264,5 GB, retención de 6 años y plazo del crédito más 6.
- Respecto del encargo: el Informe 2 corresponde a los sd 1-9 y 13 (Bases T-22), no a "6-12 y 14" (la nota de `CLAUDE.md`/`AGENTS.md` del repo está desfasada: dice que 6 a 12 y 14 son de los informes 2 y 3). El T-22 solo contiene las correcciones del Informe 1 (sd 1-5 y 13), lo cual es correcto para este formulario.
