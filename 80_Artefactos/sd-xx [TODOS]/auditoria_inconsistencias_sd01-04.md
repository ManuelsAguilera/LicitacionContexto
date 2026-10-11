# Auditoría de inconsistencias: subdocumentos 1 a 4

Fecha: 2026-10-11. Rama: `main`. Solo lectura: no se editó ningún `.tex`.

## Alcance y criterio

Se compararon `sd-01` (con Anexos y Formulario T-6), `sd-02` (cuerpo y Anexos), `sd-03` y `sd-04`, en `02_Propuesta/latex_final/`. Una inconsistencia es una contradicción entre dos afirmaciones del propio material (cifra, plazo, nombre, alcance, referencia cruzada). Quedan fuera los errores de redacción, el cumplimiento frente a las Bases y las reglas RR-NN, que son la tarea posterior. Lo que parece un error puntual y no una contradicción está en la última sección.

**Abreviaturas de ubicación.** `S1`..`S4` son los cuerpos de sd-01..sd-04, `A2` es `sd-02/OSS-Subdocumento2-Anexos.tex`, `AX1` es `sd-01/OSS-Subdocumento1-Anexos.tex` y `T6` es `sd-01/OSS-Formulario-T-6.tex`. `:N` es la línea del `.tex`. `A2` incluye la matriz A.4 (líneas 1863 a 3237).

**Gravedad.**
- **Grave:** cambia una decisión, una cifra contractual, un plazo, el alcance o la línea roja tienda/emisor, o rompe la trazabilidad completa.
- **Mediano:** contradice un dato, nombre o referencia sin cambiar la decisión de fondo.
- **Bajo:** variante de nombre o criterio de forma.

**Método.** Cuatro fichas de hechos (una por subdocumento), cruce de fichas, y verificación de cada hallazgo abriendo los `.tex`. Los hallazgos con ubicación citada se comprobaron en el original. Los marcados "por confirmar" vienen de la ficha y no se reabrieron.

## Resumen

| Tipo | Grave | Mediano | Bajo | Total |
| :--- | :---: | :---: | :---: | :---: |
| Externas (entre subdocumentos) | 5 | 13 | 3 | 21 |
| Internas sd-01 | 0 | 3 | 2 | 5 |
| Internas sd-02 | 2 | 6 | 3 | 11 |
| Internas sd-03 | 0 | 2 | 1 | 3 |
| Internas sd-04 | 0 | 4 | 3 | 7 |
| **Total** | **7** | **28** | **12** | **47** |

**Las cinco externas más urgentes:**
1. EXT-G-01: la matriz de trazabilidad del sd-02 cita secciones y tablas del sd-03 y sd-04 que no existen.
2. EXT-G-02: el sd-02 usa 24 módulos (M-01..M-24) y el sd-03 y sd-04 usan 13 servicios, sin equivalencia entre ambos.
3. EXT-G-03: el sd-03 compromete la migración de cartera "a más tardar mes 24", pero el sd-02 calcula que el último día intervenible es el 31-oct-2028 (mes 22).
4. EXT-G-05: el sd-02 propone un identificador común de cliente que el sd-03 prohíbe como "maestro único".
5. EXT-G-04: las "nueve plataformas" no son las mismas en el sd-02, sd-03 y sd-04.

Patrón general: el sd-02 (sobre todo sus anexos) quedó escrito contra versiones anteriores del sd-03 y sd-04, y estos dos se rehicieron después. La mayoría de las externas graves vienen de ahí.

## Estado de resolución (2026-10-11)

| Hallazgo | Estado | Qué se hizo |
| :--- | :--- | :--- |
| EXT-G-01 | Resuelto | La columna «Sección» de A.4 apunta solo a secciones que existen del sd-03 (3.3.2) y del sd-04 (4.1, 4.2, 4.3); quedan sin tocar las referencias al sd-05 y sd-13 (aún sin redactar) |
| EXT-G-02 | Resuelto | La columna «Componente» de A.4 usa los 13 servicios; no queda ningún M-xx |
| EXT-G-03 | Resuelto | Cartera migrada a más tardar en el mes 22 (31-oct-2028); mes 24 solo cierre de la remediación; regla única de congelamiento en sd-02 y sd-03; riesgo ampliado en R-13 |
| EXT-G-04 | Resuelto | Las nueve plataformas son los ocho sistemas y el motor de precios; las planillas son registro informal con seis usos asignados (invierte DEC-10) |
| EXT-G-05 | Resuelto | Dos identificadores independientes, sin tabla de correspondencia; subsección «Identidad del cliente» en el sd-03, ADR-02 en el sd-04, SUP-03, RF-174 y RN-04 reescritos |
| INT-02-G-01 | Resuelto | «Veinte restricciones»: 15 del Caso y 5 de las Bases; se unificaron RES-18, RES-19 y RES-20 con el anexo del sd-03 |
| INT-02-G-02 | Resuelto | Se acotó la frase: A.4 relaciona los requerimientos funcionales, no funcionales y técnicos vigentes; las OP no se trazan. RF-027 sigue fuera porque el catálogo v3.1 lo eliminó (etiquetas electrónicas) |
| EXT-M-01 | Resuelto | Códigos unificados: EXC-01..EXC-10 (antes EX) y RS-01..RS-20 (antes RES) en el sd-02, iguales a los del sd-03; el sd-02 declara que el sd-03 agrega EXC-11..EXC-19 y SP-01..SP-04. Las diez exclusiones del Caso (cap. 11) se verificaron una a una |
| EXT-M-02 | Resuelto | El sd-02 declara que su catálogo es el recibido (v3.0) y remite al sd-03 3.2.4 como versión vigente 3.1 de 308 elementos; RT-16.04 de A.4 cita la versión vigente |
| EXT-M-03 | Resuelto | Reparto único: el proponente provee la infraestructura on-premise del centro de datos (Bases Administrativas art. 14.2, RT-06.33); el cliente adquiere el hardware de tiendas y centros. El sd-01 deja de nombrar a Dell; EXC-10 del sd-02 declara la provisión del centro de datos |
| EXT-M-04 | Resuelto | Rige el registro de siete ADR del sd-04 (Tabla 4.5). A.4 cita ADR-02 (separación de datos), ADR-05 (partición DDD) y «ADR-01 a ADR-07» |
| EXT-M-05 | Resuelto en parte | A.4 usa el vocabulario del sd-04 (SIT/CD/DC/CLD, Java 25 y Spring Boot 4, Entra ID, Azure Monitor); quedan HSM, tokenización y otras herramientas por confirmar con la lista de tecnologías del equipo (ver `avisos_otros_subdocumentos.md`) |
| EXT-M-06 | Resuelto | Tabla 2.6: «≥ 24 h en tienda, que endurece las 8 h del Caso» |
| EXT-M-07 | Resuelto | Rige 104.000 pedidos en tres días (Caso cap. 1, núm. 14.1); 34.667 pedidos diarios, 6,7 veces el régimen base; proyección de 150.000. Citado en APA 7 como (Multitiendas Ancoa S.A., 2026) y agregado a las referencias del sd-02 |
| EXT-M-08 | Resuelto | Nuevo SUP-28 en el sd-02 (catorce tiendas sin respaldo, supuesto conservador); el sd-04 lo cita. También se corrigió SUP-27 («Concepcion» por «Frutillar», como en el cuerpo) |
| EXT-M-09 | Resuelto | El sd-01 declara solo la alianza con Microsoft Azure; las marcas Fortinet y Dell se quitan hasta cerrar la elección; AWS se quita de RT-23.04. Aviso al responsable del sd-06 |
| EXT-M-10 | Resuelto | A.4 remite a la sección 1.5 para los roles y al Subdocumento 12 y T-8 para nombres y certificaciones; se quitó el nombre del Jefe de Proyecto |
| EXT-M-11 | Resuelto | Comité de Operación desde el mes 16 (Etapa 1 en producción) |
| EXT-M-12 | Resuelto | Decisión tomada (sd-03): venta con tarjeta propia en corte contra cupo preaprobado, prueba en los meses 6 y 7. El sd-04 4.1 lo diseña como decisión tomada; solo quedan por fijar los criterios del cupo de la filial emisora |
| EXT-M-13 | Abierto | Queda por confirmar con la fuente de la matriz |

---

# PARTE 1. Inconsistencias externas

## Graves

### EXT-G-01. La matriz A.4 del sd-02 apunta a secciones y tablas inexistentes del sd-03 y sd-04
- **Qué dice cada lado.**
  - `A2` (matriz A.4, columna "Sección") cita unas 450 veces al sd-04 y unas 250 al sd-03. Ejemplos: "Subdocumento 4, sección 4.1.7" (17 veces), "4.2.8.2, Tabla 4.43" (10 veces), "4.2.11.1, Tabla 4.55", "Tabla 4.57"; y "Subdoc.3 §3.2.6.3 Tabla 3.3" (47 veces), "§3.3.6 Tabla 3.12" (A2:2218).
  - `S4` solo tiene 4.1, 4.1.1, 4.2, 4.2.1, 4.3, 4.3.1 y 4.3.2 (S4:93-598) y 11 tablas.
  - `S3` llega hasta 3.4.6 (S3:649), no tiene 3.2.6 ni 3.3.6 y sus tablas llegan a la 3.7.
  - A2 cita tablas 3.8 a 3.31 y 4.12 a 4.57, que no están en ningún documento.
- **Por qué creemos que pasó.** El sd-02 se cerró cuando el sd-03 y sd-04 tenían otra estructura. El sd-03 y sd-04 se rehicieron después y la matriz no se actualizó. Ya hay un precedente en el repositorio: el contenido anterior del sd-03 se retiró a propósito.
- **Sugerencia.**
  - La matriz debería regenerarse al final, cuando sd-03 a sd-09 estén cerrados, con un script que valide que cada `§` y cada `Tabla` citados existan.
  - Mientras tanto, sustituir las referencias por el servicio o la sección de nivel 3.x/4.x que ya existe.
  - Decidir antes qué manda: la estructura de los subdocumentos o la numeración que supone la matriz.

### EXT-G-02. 24 módulos (sd-02) frente a 13 servicios (sd-03 y sd-04), sin tabla de equivalencia
- **Qué dice cada lado.**
  - `A2` nombra los componentes que satisfacen cada requisito como M-01..M-24 (Motor de Disponibilidad ATP, Orquestador de Pedidos, Gestor de Evidencia y Consentimiento, Resolución de Identidad de Cliente, etc.).
  - `S3` (S3:98, S3:124, S3:416-458) y `S4` (S4:149, S4:186) estructuran la solución en 13 servicios de negocio con códigos R:M-01..03, R:V-01..04, R:CL-01..02, F:C-01..03 y X-01. Además agregan nueve componentes propios (L-01..L-03, SIT, CD, DC, CLD).
  - Ninguno de los 24 módulos del sd-02 aparece por nombre en sd-03 ni sd-04. Los códigos incluso chocan: `M-01` en sd-02 es el Motor de Disponibilidad y `R:M-01` en sd-03 y sd-04 es un servicio de Mercadería.
  - El Comunicado 10 exige nombres de componentes, módulos y servicios idénticos en todos los subdocumentos.
- **Por qué creemos que pasó.** El sd-02 propuso un esquema de módulos antes de definirse el modelo de 13 servicios (decisión del sd-03, escenario B). El sd-03 fijó los servicios y el sd-04 se alineó con el sd-03, pero nadie reconcilió el sd-02.
- **Sugerencia.** El sd-03 manda sobre el sd-02 en la estructura de la solución. Opciones: (a) reescribir la columna "Componente" de A.4 con los 13 servicios; o (b) mantener los M-xx como "capacidades" del sd-02 y agregar una tabla de correspondencia M-xx a servicio en el Anexo del sd-03. Recomendada: (a), porque mantener dos taxonomías multiplicará las contradicciones en los sd-05 a sd-09.

### EXT-G-03. Fecha límite de la migración de cartera: mes 24 (sd-03) frente a último día útil en el mes 22 (sd-02)
- **Qué dice cada lado.**
  - `S2:442`: con inicio en enero de 2027, y como "entre el 1 de noviembre y el 6 de enero no se pueden intervenir los sistemas", "el último día útil es el 31 de octubre de 2028" (670 días calendario, 191 congelados, 479 intervenibles). La cartera "debe migrarse íntegra antes de 2029".
  - `S3:346` (Tabla de resultados): "Frontera y cumplimiento ... cartera migrada sin diferencias ... Meses 16 a 21 y, a más tardar, mes 24". Con inicio en enero de 2027, el mes 24 es diciembre de 2028, dentro de la ventana de congelamiento de Navidad.
  - `S3:108` y `S3:252` fijan el retiro de la plataforma de crédito en octubre de 2028 (mes 22), consistente con el sd-02, pero no con "mes 24".
- **Por qué creemos que pasó.** El sd-03 contó el plazo en meses de contrato sin cruzar con el calendario de congelamiento que el sd-02 sí calcula. El "mes 24" parece un colchón añadido al resultado de negocio.
- **Sugerencia.** Alinear los dos sobre el calendario con congelamientos: o el resultado vence a fines de octubre de 2028 (mes 22), o se explica qué se hace entre noviembre y diciembre de 2028. Debe quedar un solo hito de cartera para el sd-07 (EDT) y el sd-08 (riesgos).

### EXT-G-04. El noveno elemento de las "nueve plataformas" es distinto en sd-02, sd-03 y sd-04
- **Qué dice cada lado.**
  - `S2:154,179,183-203`: "nueve plataformas de seis proveedores". La lista tiene 9 viñetas, pero la última es el motor de precios, que es una ausencia ("no existe un motor de precios", S2:179). Quedan 8 plataformas reales. Los seis proveedores no se nombran.
  - `S3:132,364`: las nueve incluyen "planillas y listas impresas" como novena, que "dejan de ser registro oficial".
  - `S4:223-231` (Tabla 4.4): 9 filas, la novena es el motor de precios ("no existe; capacidad nueva"). Ahí las planillas de Concepción aparecen aparte.
  - `S1:314` y `S1:301` repiten "nueve plataformas y catorce interfaces" sin enumerar.
- **Por qué creemos que pasó.** El Caso habla de nueve plataformas sin listarlas. Cada subdocumento reconstruyó la lista por su cuenta y llegó a un noveno elemento distinto.
- **Sugerencia.** Definir una tabla maestra única (nombre, año, destino, proveedor) y reutilizarla. Decidir si las nueve son las ocho reales más las planillas (propuesta del sd-03) o las ocho más el motor de precios, y registrar la decisión como consulta al mandante si el Caso no la resuelve. Hoy es el dato que más aparece en los cuatro subdocumentos.

### EXT-G-05. Identificador común de cliente (sd-02) frente a "maestro único de clientes" prohibido (sd-03 y sd-04)
- **Qué dice cada lado.**
  - `A2:3279` (SUP-03): "se propone relacionar la identidad de una misma persona mediante un identificador común, conservando separados sus registros comerciales y financieros". `A2:2218-2222` asigna RF-165 a RF-167 al módulo "M-22 Resolución de Identidad de Cliente".
  - `S3:248`: queda prohibido "un maestro único de clientes".
  - `S4:318-344`: el servicio de control de cruces X-01 "no almacena perfiles unificados"; no hay repositorio común.
  - Ni sd-03 ni sd-04 mencionan una resolución de identidad ni un identificador común.
- **Por qué creemos que pasó.** El sd-02 trata la identidad compartida como un supuesto aceptable mientras los registros estén separados. El sd-03 endureció la línea roja después y la convirtió en prohibición de maestro único, sin retirar el supuesto.
- **Sugerencia.** Es la línea roja del caso, así que conviene resolverlo explícitamente. Decidir si existe un identificador común y quién lo custodia (por ejemplo, solo dentro de X-01, sin atributos). Luego dejarlo escrito en sd-03 (donde hoy solo hay prohibición), en sd-04 (qué componente lo resuelve) y en la matriz del sd-02.

## Medianas

### EXT-M-01. Listas de exclusiones, supuestos y restricciones distintas entre sd-02 y sd-03
- **Dice.**
  - `A2:3364-3382`: 10 exclusiones (EX-01..EX-10), 27 supuestos (SUP-01..SUP-27), 20 restricciones (RES-01..RES-20).
  - `S3:191-209`: 18 exclusiones vigentes con otro código (EXC-01..EXC-19, sin EXC-14; "10 del cliente, 1 deducida de Transversales, 7 del proponente"); 6 supuestos (SP-01..SP-04, SUP-26, SUP-27).
  - Los dos dicen que su lista vive en un Anexo (A2 A.5 y "Anexo A" del sd-03, que no existe).
  - El cuerpo del sd-02 dice "quince restricciones" frente a 20 en su propio anexo (ver INT-02-G-01).
- **Por qué.** El sd-03 reelaboró las listas (agregó exclusiones del proponente y supuestos propios) y no las devolvió al sd-02.
- **Sugerencia.** Una sola numeración y una sola ubicación. El sd-02 debería mantener solo lo que viene del Caso (EX/SUP) y el sd-03 sumar lo propio con códigos distintos y una nota de qué agregó.

### EXT-M-02. Catálogo de requerimientos: 307 (sd-02) frente a 308 vigente (sd-03)
- **Dice.** `S2:657,694-720` y `A2` A.1 a A.3: 307 (223 RF, 75 RNF, 9 OP). `S3:256-284`: parte de 307, elimina 1 (etiquetas electrónicas), reclasifica 3 y agrega 5 RF, quedando 308 (227 RF, 72 RNF, 9 OP, "versión 3.1"). El sd-03 lo explica, pero el sd-02 no refleja el cambio y A.4 sigue mapeando el catálogo anterior.
- **Por qué.** El sd-03 es la fuente del cambio, pero el sd-02 no se reabrió.
- **Sugerencia.** Elegir una versión de catálogo para toda la propuesta y citarla igual en ambos. Si el sd-02 describe el catálogo recibido y el sd-03 el vigente, decirlo en el sd-02 con una nota o remitir al sd-03.

### EXT-M-03. Quién adquiere el hardware on-premise
- **Dice.**
  - `S1:347`: alianza con Dell para servidores y componentes físicos, "directamente o mediante un integrador".
  - `A2:3382` (EX-10): se excluye la adquisición por el proponente del hardware cuya compra corresponde al cliente.
  - `S3:233` (SP-04): el cliente adquiere los equipos; `S3:242`: el proponente provee la infraestructura on-premise según las Bases.
  - `S4:575`: para DC-01 el proponente habilita el recinto técnico "con su especificación, equipos, conectividad..." y el cliente aporta el espacio y la obra civil.
- **Por qué.** El Caso y las Bases reparten la responsabilidad de forma ambigua y cada subdocumento la resolvió con otro matiz. Hay una tensión interna del sd-03 entre SP-04 y la provisión por el proponente.
- **Sugerencia.** Una sola frase de reparto (compra, instalación, configuración, certificación) que se reutilice en sd-01 (alianza), sd-02 (exclusiones), sd-03 (supuestos) y sd-04 (Tabla 4.11). Si no se puede decidir, consulta al mandante. Impacta directamente la oferta económica.

### EXT-M-04. Numeración de ADR distinta
- **Dice.** `A2` cita ADR-01 (arquitectura modular con límites de contexto), ADR-06 (migración de cartera) y ADR-11/ADR-12 (separación física Z3). `S4:363-372` (Tabla 4.5) tiene siete: ADR-01 es "escenario B", ADR-06 es "Event Hubs y API Management", y no existen ADR-11 ni ADR-12.
- **Por qué.** El sd-02 se escribió contra un registro de decisiones anterior (hasta 12). El sd-04 definió su propio registro de 7.
- **Sugerencia.** Un solo registro, con los números que ya usa el sd-04, y actualizar A.4. Si el registro llega a más de siete decisiones, extenderlo en el sd-04.

### EXT-M-05. Nombres de sitios, zonas y tecnología
- **Dice.** `A2` (A.4) usa "Site Principal / Site Secundario", zonas Z1 (nube Multi-AZ), Z2 (nodo de tienda), Z3 (separación física) y "servicios de negocio sin estado (Go/Java)" (A2:2496). `S4` usa SIT-01, CD-01/02, DC-01/02, CLD-01/02, y una sola pila de servicios en Java 25 y Spring Boot 4 (S4:388).
- **Por qué.** Mismo origen que EXT-M-04.
- **Sugerencia.** Adoptar el vocabulario del sd-04 (es el que se dibuja en las figuras) y corregir la matriz. Retirar "Go" si el sd-04 define solo Java.

### EXT-M-06. Operación sin enlace: 8 h (sd-02) frente a 24 h
- **Dice.** `S2:710` (Tabla 2.6): "Operación sin enlace externo (≥ 8 h en tienda)". `A2` (RNF-24, RNF-28, SUP-07, RES-05), `S3:98,645` y `S4:248,352,369` usan 24 horas. RNF-28 menciona el mínimo de 8 h de RN-46 como punto de partida.
- **Por qué.** El cuerpo del sd-02 conservó el mínimo de las Bases (8 h) y el resto de la propuesta adoptó el endurecimiento a 24 h (RT-03.10).
- **Sugerencia.** Corregir la Tabla 2.6 a 24 h con una nota de que endurece el mínimo de 8 h. Es el valor que hoy sostiene la arquitectura de nodo local.

### EXT-M-07. Volumen del evento anual: 114.520 pedidos (sd-02) frente a 104.000 (sd-02 anexo y sd-03)
- **Dice.** `S2:276`: 114.520 pedidos en 3 días (22 x 5.205), 7,33 veces. `S2:434` y RNF-22 en `A2`: 104.000 pedidos en 3 días. `S3:309` usa 104.000. `S2:418` implica unos 105.000 (2.840 cancelados al 2,7 %).
- **Por qué.** Dos cálculos del mismo evento: uno desde la venta diaria (5.205 x 22) y otro desde el dato del Caso.
- **Sugerencia.** Elegir una cifra (la del Caso, 104.000) y explicar la otra como proyección si se quiere conservar.

### EXT-M-08. Tiendas sin enlace de respaldo: 7 (sd-02) frente a 14 (sd-04)
- **Dice.** `S2:211` y `S2:497`: 7 de 15 tiendas sin respaldo (6 de las 14 en centros comerciales más Coyhaique). `S4:417`: 8 tiendas con doble enlace y 14 sin respaldo acreditado, "seis en centro comercial y ocho a la calle". El sd-04 declara que supone que las 8 a la calle no tienen respaldo (S4:421).
- **Por qué.** El sd-04 dimensionó la red de forma conservadora y lo declaró como supuesto; el sd-02 se quedó con el dato del Caso. La contradicción está declarada pero no está referida desde el sd-02.
- **Sugerencia.** Mantener el supuesto del sd-04, pero citarlo en el sd-02 (SUP nuevo) para que el dato conste en ambos lados.

### EXT-M-09. Alianzas de seguridad y red del sd-01 sin reflejo en el sd-04
- **Dice.** `S1:345,347`: alianza con Fortinet para cortafuegos, segmentación y conectividad segura, y con Dell para servidores. `S4` nombra Azure Firewall y "router y firewall" en tienda sin marca (S4:462,562) y no menciona Fortinet ni Dell.
- **Por qué.** El sd-01 describe alianzas corporativas, el sd-04 solo detalla lo que el diseño necesita.
- **Sugerencia.** Nombrar el fabricante de tienda y de DC-01 en el sd-04 (T-11 de implementos) o quitar la marca del sd-01 si la decisión aún no está tomada.

### EXT-M-10. El sd-02 anticipa del sd-01 contenido que el sd-01 no tiene
- **Dice.** `A2:2964,3074,3174` remiten a "sección 1.6 Frente de jefaturas", a "1.4 Experiencia relevante" y nombran al Jefe de Proyecto con certificación PMP y certificaciones individuales. `S1`: la sección 1.6 es "Alianzas"; el sd-01 solo describe roles y remite los nombres al capítulo 12 y al T-8 (S1:102); los nombres solo aparecen en la Declaración de uso de IA.
- **Por qué.** La matriz asumía un sd-01 con el equipo nominado.
- **Sugerencia.** Corregir las referencias (1.5 Estructura para Proyecto, 1.2) y apuntar al capítulo 12 / T-8 para nombres y certificaciones.

### EXT-M-11. Comité de Operación "desde el mes 13"
- **Dice.** `S1:335`: el Comité de Operación se reúne mensualmente desde el mes 13. `S3:104,108` y `S4:97`: la operación son los meses 21 a 56, la Etapa 1 pasa a producción en el mes 16, y los meses 13 a 15 son marcha blanca.
- **Por qué.** El sd-01 se redactó con un cronograma de operación anterior o mezcló marcha blanca con operación.
- **Sugerencia.** Corregir a mes 16 (inicio de producción de la Etapa 1) o aclarar que el comité arranca en marcha blanca.

### EXT-M-12. Crédito sin conexión: compromiso (sd-03) frente a decisión pendiente (sd-04)
- **Dice.** `S3:250`: la primera condición del adelanto del negocio financiero es autorizar ventas con tarjeta propia en corte de enlace contra un cupo preaprobado, con prueba en los meses 6 y 7. `S4:352` dice que sin enlace no se originan tarjetas ni se amplían cupos, y `S4:375` lista como entrega previa al cierre de 4.1 la "decisión de riesgo para crédito sin enlace".
- **Por qué.** El sd-03 declara la modalidad como diseño comprometido; el sd-04 la trata como decisión aún por tomar.
- **Sugerencia.** Alinear el estado: o es decisión tomada (el sd-04 la diseña) o es condición sujeta a decisión (el sd-03 lo dice).

### EXT-M-13. Significado de "Cumple: No" en la matriz A.4
- **Dice.** `A2` (A.4): 171 de 374 requisitos técnicos aparecen con "No" y sin componente (por ejemplo RT-16.01, A2:2968). `S3:244,256,288` dice que las RT se responden una a una en el Formulario T-12. Los otros subdocumentos no explican qué significa "No".
- **Por qué.** La columna mezcla probablemente "no aplica en esta etapa" con "no cumple".
- **Sugerencia.** Definir la columna en el propio anexo (por ejemplo, "Sí", "Parcial", "A resolver en sd-N") y alinearla con T-12. **Por confirmar:** hace falta abrir la fuente de la matriz para saber la intención.

## Bajas

### EXT-B-01. Variantes de nombre de una misma cosa
Núcleo Retail / sistema central de retail / sistema central / núcleo de 2009; plataforma de crédito 2011 / plataforma de originación y cobranza / plataforma financiera; filial emisora / Emisor / Negocio Financiero; portal de proveedor (S4:107) / portal de vendedor (S4:278); evento anual / evento de junio de 2026 / mayo o junio (S2:276,310,418). **Causa:** cada autor eligió su forma. **Sugerencia:** un glosario común de nombres que el Comunicado 10 pide idénticos.

### EXT-B-02. "Frente" significa cosas distintas
`S1:170` habla de seis frentes de trabajo del equipo (Arquitectura y Datos, Seguridad y Calidad...). `S3`/`S4` usan "tres frentes" de la solución (Retail, Filial emisora, Frontera) y `A2` cita "frente 1" de `S4 §4.1.7`. **Sugerencia:** llamar "áreas de trabajo" o "equipos" a los del sd-01.

### EXT-B-03. Vigencia de la Ley 21.719
`S2:117,264` presenta los dos regímenes como alcanzados por la Ley 21.719. `S3:521` distingue que rige desde el 1-dic-2026 y que a octubre de 2026 rige la Ley 19.628. **Sugerencia:** el sd-02 puede agregar la fecha de vigencia.

---

# PARTE 2. Inconsistencias internas

## sd-01

### Medianas
- **INT-01-M-01. Seis frentes: dos listas distintas.** `S1:170` los llama Arquitectura y Datos, Seguridad y Calidad, Operación y Gestión del Cambio. `S1:301` dice "arquitectura, desarrollo, datos, seguridad, calidad y operación" (cambia Gestión del Cambio por "desarrollo"). La sección 1.5 dice que la estructura repite "los mismos roles del punto 1.2" (16 personas) pero solo lista 7 roles (`S1:312-324`). **Causa probable:** la 1.5 se escribió resumida sobre otra versión del equipo. **Sugerencia:** una lista de frentes y listar en la 1.5 todos los roles de la 1.2 o decir que son los líderes.
- **INT-01-M-02. Certificaciones.** `S1:205` habla de "tres sistemas de gestión" (9001, 27001/27002, 22301). `S1:229` suma 27017, 27018, PCI DSS y 27701. `S1:281-297` (1.4.1) presenta cuatro certificaciones como obtenidas, mientras la 1.3 las llama "normas certificables" a las que se conforma el sistema. **Causa:** la 1.3 y la 1.4 se redactaron aparte. **Sugerencia:** separar "certificadas" de "alineadas" y dar una sola lista.
- **INT-01-M-03. Anexo A.2 inexistente.** `S1:279` remite los tres proyectos de referencia al "Anexo A.2". `AX1` solo tiene A.1 (sitio web) y el detalle está en el Formulario T-6 (`S1:102`). **Causa:** el anexo se movió al formulario y quedó la remisión antigua. **Sugerencia:** apuntar al T-6.

### Bajas
- **INT-01-B-01. Variantes de rol.** "Jefe de Proyecto" y "Jefe de Proyectos" (`S1:263`); "Líder de Calidad" corporativo (`S1:216`) y "del proyecto" (`S1:222`) sin decir cuál de los 16 es. Unificar.
- **INT-01-B-02. Sectores de experiencia.** `S1:106` lista banca, logística, telecomunicaciones y retail; `S1:110` agrega seguros; `S1:267` menciona comercio electrónico y servicios financieros. Unificar la lista.

## sd-02

### Graves
- **INT-02-G-01. Restricciones: quince frente a veinte.** `S2:767` dice "quince restricciones" y las numera R1..R15 (`S2:769-779`). `A2:3394-3455` (A.5.3) tiene RES-01..RES-20 (las RES-16..RES-20 son híbrido, 56 meses, innovaciones, 2029 y umbrales). (Corrección del 2026-10-11: el artículo 28 sí está en el anexo, citado como capítulo 5 en RES-18; ya se unificó la cita.) **Causa:** el anexo creció después de redactar el cuerpo. **Sugerencia:** actualizar el cuerpo a 20, y usar el mismo código (RES) en los dos.
- **INT-02-G-02. La matriz A.4 no relaciona "cada requerimiento".** `S2:107,727,785` afirman que A.4 relaciona todos los requerimientos. A.4 tiene 222 RF (falta RF-027), 75 RNF y 374 RT, y ninguna de las 9 OP. **Causa:** la matriz se armó desde las secciones A.1 a A.2 y no se incorporó A.3. **Sugerencia:** agregar las OP y RF-027, o acotar la frase.

### Medianas
- **INT-02-M-01. Umbral de evaluación crediticia.** La Tabla 2.3 pone "< 10 s" y brecha "5 a 22,5 veces" (`S2:386`); el texto (`S2:440,708`), RES-20 y RNF-06 dicen 8 s. La brecha 5 a 22,5 solo cuadra con 8 s (40/8 y 180/8). **Sugerencia:** corregir la tabla a 8 s.
- **INT-02-M-02. Retención de grabaciones.** `S2:388`: brecha "24,3 veces o más"; `S2:438`: "36,5 veces inferior" (plazo de 36 meses + 6 años); `S2:323`: rango de brechas "entre 1,9 y 36,5 veces" y `S2:391` "más de veinte veces". **Causa:** dos supuestos de plazo del crédito. **Sugerencia:** fijar el plazo y calcular una sola brecha.
- **INT-02-M-03. Tabla 2.2: las filas suman 133, el total dice 126.** 67 + 42 + 10 + 7 + 7 (`S2:308-312`) frente a "126 (34,5 %)" (`S2:314`). Cuadra solo si el evento de noviembre se superpone con Navidad (que va del 1 de noviembre al 6 de enero), traslape que no se declara. **Sugerencia:** declarar el traslape o corregir la suma.
- **INT-02-M-04. SUP-27: Frutillar o Concepción.** `S2:745` supone las ubicaciones de Illapel, Valparaíso, Talca y Frutillar; `A2:3327` dice "Concepcion". **Sugerencia:** unificar (y recordar que Concepción ya es el nombre del centro de distribución).
- **INT-02-M-05. A.4 como listado de indicadores.** `S2:454` y `S2:785` dicen que el listado de indicadores con su línea base está en A.4. A.4 es solo la matriz de cumplimiento. **Sugerencia:** mover o quitar la promesa.
- **INT-02-M-06. Referencia de tabla.** `S2:657` cita la "Tabla 2.1" para el catálogo de 307 elementos; la 2.1 es el marco regulatorio y el catálogo está en la 2.6. **Sugerencia:** corregir la referencia.

### Bajas
- **INT-02-B-01. IDs con huecos.** Faltan RF-025, RF-026, RF-031 y RNF-01; RF-183 (`A2:711`) cita un "RF-026.1" que no existe. **Sugerencia:** confirmar contra el catálogo oficial.
- **INT-02-B-02. Brecha "veces" con tres definiciones.** Valor/umbral (12,4/2 = 6,2) en unos casos; atraso/umbral (19/3 = 6,3) en otros, y decimales con punto ("3.7 veces") y con coma. Unificar la definición.
- **INT-02-B-03. A.1 anuncia más de lo que contiene.** `A2:100` dice que consolida RF, RNF y OP; A.1 es solo RF (RNF en A.2, OP en A.3).

## sd-03

### Medianas
- **INT-03-M-01. Numeración de tablas duplicada.** Hay dos "Tabla 3.5" (`S3:292` casos limítrofes F/NF y `S3:376` alternativas del núcleo Retail) y dos "Tabla 3.6" (`S3:328` resultados de negocio y `S3:527` control de cruces). Las referencias "la Tabla 3.5" (`S3:290,374`) y "la Tabla 3.6" (`S3:326,525`) quedan ambiguas. **Causa:** las secciones 3.1/3.2 y 3.3/3.4 se escribieron por separado (el sd-04 cita después "Tabla 3.7" para control de cruces). **Sugerencia:** renumerar en orden de aparición y actualizar las citas, también las del sd-04.
- **INT-03-M-02. Dependencias entre etapas.** `S3:579` dice que el Servicio de existencias (Etapa 1) recibe reservas del Servicio de pedidos (Etapa 2); `S3:595` dice que ventas (Etapa 1) consulta a clientes Retail (Etapa 2). La Tabla 3.1 dice que la Etapa 2 solo agrega servicios que dependen de los de la Etapa 1. **Sugerencia:** declarar la interfaz provisional de la Etapa 1 o ajustar la tabla.

### Baja
- **INT-03-B-01. Legislación y referencias.** `S3:542` dice que la legislación está "citada en referencias", pero la lista de Referencias (`S3:664-673`) solo trae las Bases y el PMBOK. Falta cualquier ley.

## sd-04

### Medianas
- **INT-04-M-01. Event Hubs y API Management: por ámbito o compartidos.** `S4:105` y `S4:268,288`: cada ámbito tiene su propio API Management y sus Event Hubs. `S4:417`: la plataforma compartida "ofrece borde, integración, eventos y red". `S4:596`: un API Management con tres unidades y un Event Hubs zonal. No queda claro si son una o dos instancias ni si las tres unidades son totales o por ámbito. **Sugerencia:** una frase en la Tabla 4.6 con el número de instancias por ámbito.
- **INT-04-M-02. Identidad, secretos y monitoreo.** `S4:105,298` los presentan por ámbito; `S4:596` dice que Entra ID, Azure Monitor y Log Analytics "completan la plataforma", y `S4:462` habla de suscripciones por ambiente y ámbito mientras `S4:486` habla de una suscripción por ambiente. **Sugerencia:** decidir qué es común (y qué se separa) y unificar las tres frases.
- **INT-04-M-03. Condición de residencia: todo CLD-02 o solo el Emisor.** `S4:330` y `S4:454`: la región de recuperación Brazil South está "condicionada a la aprobación de residencia". `S4:417,608`: la condición afecta solo a la réplica del Emisor, y Retail replica sin condición. **Sugerencia:** precisar a qué alcanza la condición.
- **INT-04-M-04. Segmentación de red en tienda.** `S4:474`: la separación por función en tienda "hoy solo existe en nueve tiendas". `S4:562` (Figura 4.17) presenta una "tienda tipo" con redes por función como configuración de cada tienda. No dice si las 22 tiendas reciben el equipo o solo 13. **Sugerencia:** aclarar la cobertura en la Tabla 4.11.

### Bajas
- **INT-04-B-01. Redis.** La Tabla 4.6 (`S4:395`) lo presenta como capacidad general; `S4:462,596` lo limitan a Retail.
- **INT-04-B-02. Figuras de la Tabla 4.10.** Servicios como R:M-03 y F:C-01 remiten a la Figura 4.18 (centro de datos primario), que no es una vista funcional (`S4:528-542`). **Por confirmar:** conviene revisar fila por fila contra las figuras.
- **INT-04-B-03. RTO/RPO.** `S4:432` habla de RTO/RPO "por servicio", pero `S4:610` fija un solo par (4 h / 15 min) para los servicios críticos y no define nada para los no críticos.

---

# Descartado o pasa a la auditoría de errores

- **Párrafo duplicado y secciones repetidas del sd-02** (`S2:101,103,109,111`): dos `\section` y el mismo párrafo de introducción dos veces. Es un error de armado, no una contradicción.
- **Marcas `PENDIENTE` y celdas "Fuente:" vacías** en las Tablas 2.1, 2.3 y 2.4 del sd-02 (`S2:253,377,487`): estado de redacción.
- **Referencias vacías** del sd-01 (`S1:351`) y referencias citadas que faltan en el sd-02 (Leyes 21.398, 20.555, 19.913): incumplimiento de forma.
- **Declaración de uso de IA:** el sd-03 solo cubre 3.1 y 3.2 y el sd-04 declara no haber pasado revisión humana. Es cumplimiento del Comunicado 10, no contradicción.
- **Formato de encabezados** (`1.4.1` sin punto frente a `1.1.1.`) y capitalizaciones ("ancoa" en minúscula en el encabezado de la Tabla 2.3).
- **Figuras `D1`..`D6` del sd-03 aún como comentario** (sin imagen) y anexos A a D del sd-03 que aún no existen: pendientes de redacción.
- **Discrepancias de numeración de capítulos del sd-02** ("Capítulo 2 · Introducción" y "2. Comprensión..."): estructura, no contradicción.

# Orden sugerido de resolución

1. **Primero lo que gobierna lo demás:** EXT-G-03 (hito de cartera), EXT-G-04 (tabla maestra de plataformas) y EXT-G-05 (identidad). Alimentan los sd-05 a sd-09.
2. **Taxonomía de la solución:** EXT-G-02 y EXT-M-04/05, antes de regenerar la matriz.
3. **Regenerar la matriz A.4 al final** (EXT-G-01), con verificación automática de las referencias.
4. **Reparto de responsabilidades:** EXT-M-01, EXT-M-03 y EXT-M-12, que afectan la oferta económica y el plan de trabajo.
5. **Cifras sueltas y nombres:** el resto de las medianas y bajas, junto con las correcciones internas.
