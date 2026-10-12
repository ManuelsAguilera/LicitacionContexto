> Detalle de la revisión de los formularios (2026-10-12). Borrador. **Nota:** cualquier hallazgo que diga que el Comité de Operación debe iniciar en el mes 16 es un falso positivo: el artículo 71 de las Bases fija «mensual desde el mes 13».

# Revisión Formulario T-12, líneas 1 a 740

Archivo: `02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-12.tex`. El tramo contiene los RF-001 a RF-226 (222 filas), los RNF-02 a RNF-76 (75 filas) y RT-02.01 a RT-02.07. Las líneas citadas son las del archivo. Referencias: catálogo v3.1 (`01_Requerimientos/RequerimientosAtomizados_Depuracion_Alcance_v3.1.xlsx`, hoja `1_Catalogo_Vigente`), Bases Transversales (BT), Caso 09 cap. 15, sd-03 y sd-04 en `02_Propuesta/latex_final/`.

## 0. Resumen del diagnóstico

La tabla se construyó con el catálogo v3.0 y con la arquitectura anterior (24 módulos M-01 a M-24, zonas Z1/Z2/Z3, "Site Principal/Secundario", ADR-01 a ADR-12, numeración antigua del sd-04). Los sd-03 y sd-04 vigentes ya no usan nada de eso. Por eso las columnas "Componente" y "Sección de la propuesta" están desactualizadas en casi todas las filas. La causa es única y la corrección es mecánica: remapear cada fila a los 13 servicios (R:M-01, R:V-02, F:C-01, X-01, etc.), a los sitios (SIT-01, CD-01, DC-01, DC-02, CLD-01, CLD-02) y a las tablas y figuras vigentes.

Estructura de la tabla: tiene las 5 columnas que pide el T-12 de las Bases Administrativas (líneas 2282-2288): ID requerimiento, Descripción, Cumple, Componente que lo satisface y Sección de la propuesta. Todas las filas dicen "Sí", sin ningún "Parcial" ni "Condicionado".

## 1. Hallazgos graves

**G-1. Los códigos M-01 a M-24 no existen en los sd-03 y sd-04 (columna "Componente", casi todas las filas).**
- Dónde: líneas 133-725 (por ejemplo M-09 OMS, M-22 Resolución de Identidad de Cliente, M-24, M-20, M-16 WORM).
- Qué dice: el componente que satisface es "M-xx ...".
- Qué debería decir: el servicio del sd-03 §3.3.2 (código R:M-01, R:M-02, R:M-03, R:V-01 a R:V-04, R:CL-01, R:CL-02, F:C-01 a F:C-03, X-01) más el componente del sd-04 (Tabla 4.3, candidatos de despliegue; L-01 a L-03 en la Tabla 4.13).
- Fuentes: `80_Artefactos/sd-xx [TODOS]/glosario_nombres_comunes.md` ("no se usan los códigos M-xx del sd-02 antiguo"). Los sd-03 y sd-04 tienen 0 y 15 apariciones de M-xx respectivamente, y las 15 del sd-04 son R:M-01 y R:M-03.
- Sugerencia: reemplazar el código por el servicio vigente. El catálogo v3.1 ya trae por cada RF la columna "Código" y "Servicio", que sirve de mapeo base. Confirmado.

**G-2. RF-174 (línea 475) declara "Sí" a una tabla de correspondencia y contradice la línea roja.**
- Qué dice: "resolver la correspondencia entre identificadores exclusivamente a través de una tabla de correspondencia custodiada".
- Qué debería decir (v3.1): "únicamente durante un cruce autorizado, sin conservarla en una tabla ni en ningún atributo de ambos ámbitos, y con acceso nominado y registrado".
- Fuentes: catálogo v3.1 RF-174, y verdad_proyecto ("sin identificador común ni maestro ni tabla de correspondencia; único cruce autorizado por X-01").
- Sugerencia: corregir el texto y revisar los RF-165 a RF-176 (líneas 457-479). El componente "M-22 Resolución de Identidad de Cliente" sugiere justamente un maestro de identidad: sustituir por X-01. Confirmado.
- Relacionado: las filas RF-165 a RF-176 citan SUP-03 ("identificador común", sd-02 Anexos A.4.1). Esto es una incoherencia del sd-02 con la línea roja, que afecta la trazabilidad de esas filas. Por confirmar con el revisor del sd-02.

**G-3. Catálogo desactualizado: se usa la v3.0 y no la v3.1 (308 elementos).**
- Faltan: OP-01 a OP-09 (9 obligaciones del proponente), y RF-227 a RF-231 (5 RF del Servicio de clientes Retail R:CL-02, Etapa 2). Esto da 222 RF y 75 RNF en la tabla, contra 227 RF y 72 RNF vigentes. Las OP no son funciones del sistema, pero el T-12 pide "cada requerimiento de las Bases Técnicas del caso" y el catálogo vigente las incluye.
- Sobran: RNF-61, RNF-62 y RNF-63 (líneas 695-699). La v3.1 los reclasificó a criterios de aceptación (hoja `2_Depuracion_Alcance`, H-21; se tratan en sd-03 §3.2.5). Hoy figuran con "Sí" y una remisión a la "Tabla 3.6".
- Ausentes con razón (correcto): RF-025, RF-026, RF-027, RF-031 y RNF-01 (eliminados por EXC-02).
- Textos distintos del catálogo v3.1:
  - RF-160 (línea 447) y RF-161 (449): dicen "RF-158 y RF-159"; debe decir "RF-058".
  - RF-174: ver G-2.
  - RF-183 (493): dice "RF-026.1"; debe decir "RF-177".
  - RNF-22 y RNF-23 (617, 619): conservan "NFR-06.x", un ID que no existe. El catálogo v3.1 lo conserva, por lo que la corrección es de catálogo.
- Sugerencia: regenerar el listado desde la hoja `1_Catalogo_Vigente`. Observación: el sd-02 (Anexos A.1 a A.3) también está en v3.0 (307 elementos, incluye RF-027); la diferencia con el formulario es RF-027, que el formulario sí omite. Confirmado.

**G-4. RNF-25 (línea 623): "Sí" a 24 h sin enlace del centro de distribución principal, pero el sd-04 solo compromete 4 horas.**
- El sd-04 (línea 626) dice: "El centro de distribución principal debe operar al menos cuatro horas sin enlace según la misma exigencia", lo cual es el valor del Caso (cap. 15, RT-03.10: tienda 8 h, CD principal 4 h).
- BT RT-03.10 exige 24 h "o el mayor que fije el caso", y el caso endurece, no rebaja. El catálogo v3.1 (RNF-25) también dice ≥ 24 h. Hoy el sd-04 rebaja y el formulario afirma cumplimiento con una remisión (sd-03 §3.4.5, sd-04 §4.2) que no lo respalda para CD-01.
- Sugerencia: corregir el sd-04 línea 626 a 24 h para CD-01 (o declarar el diseño que lo logre) y recién entonces dejar "Sí" en RNF-25 y RNF-28. Confirmado como inconsistencia; la solución es a decidir.

**G-5. "Cumple: Sí" afirma cosas que el sd-04 no hace o deja condicionadas.**
- RNF-33, RNF-34, RNF-37, RNF-59 (líneas 639-641, 647, 685): "cifrado de campo, tokenización, HSM". El sd-04 no contiene la palabra tokenización. El cifrado de campo no aparece (solo "repositorios cifran datos en reposo", línea 378). Managed HSM aparece solo para la filial emisora y con estado "Por probar" (línea 442). RT-11.10 del Caso exige cifrado de campo y tokenización para identificación de clientes y medios de pago (también Retail).
- RNF-70, RNF-71, RNF-72, RNF-73 (líneas 713-719): "Cadena DevSecOps (SBOM, SLSA, OWASP ASVS)". Ninguno de los tres términos aparece en sd-03 ni sd-04. La Tabla 4.6 solo da "Terraform y canal CI/CD ... Por probar". Las herramientas DevSecOps son "producto por definir".
- RNF-39 y RNF-40 (651-653): "Gestor de Evidencia (WORM) - firma electrónica avanzada, Ley N°19.799". El sd-04 (líneas 103 y 302) marca la firma electrónica como "componente por acreditar" en ámbar y no menciona la Ley 19.799.
- RT-02.04 (línea 733): dice "fechado". La Tabla 4.5 del sd-04 no tiene columna de fecha. ADR-05, ADR-06 y ADR-07 están "Condicionadas".
- RT-02.06 (737): la idempotencia aparece en el sd-04 (líneas 248, 324, 326), pero la "ventana de deduplicación documentada" que exige RT-02.06 no está.
- Sugerencia: usar "Sí, condicionado" o "Parcial" donde el sd-04 diga "Por probar", "Condicionada" o "por acreditar", e indicar la condición. O bien completar el sd-04. Confirmado.

**G-6. Tecnologías con nombre no decididas o retiradas (RT-02.05, línea 735).**
- Dice: "Servicios de negocio sin estado (Go/Java); estado de sesión externalizado en Azure Cache for Redis".
- Vigente: Java 25 y Spring Boot 4 (Go no está en el sd-04), y Azure Managed Redis solo para Retail (Tabla 4.6, línea 439). El propio sd-04 indica que Azure Cache for Redis se retira el 30-sep-2028, dentro del contrato (BT 1.6, soporte durante los 56 meses).
- Además, Redis es solo de Retail. El sd-04 no declara dónde reside el estado de sesión y de proceso del Emisor, y RT-02.05 lo exige para toda la capa de servicios de negocio. Por confirmar con el sd-04.
- Sugerencia: "Java 25 y Spring Boot 4 sin estado; estado en Azure Managed Redis (Retail) y almacén del Emisor por definir". Confirmado.

**G-7. Servicios de dos negocios mezclados en el mismo componente (línea roja).**
- RF-069 y RF-070 (261, 263): consulta de estado de cuenta (catálogo: F:C-02, Filial emisora). Se mapean a "M-09 OMS / M-10 / M-11 Portal del Cliente", componentes Retail. El propio campo Sección cita "Servicio de cartera de crédito". Debería ser F:C-02 con el cruce autorizado por X-01 (sd-03 Tabla 3.9).
- RF-089 a RF-093 (301-309): originación (F:C-01) mapeada a "M-08 POS / M-17".
- RF-211 a RF-216 (cartera, F:C-02) y RF-199 a RF-210 (F:C-03) están bajo el mismo bloque "M-15/M-16/M-18/M-19": en el modelo vigente son tres servicios distintos del Emisor.
- RNF-40, RNF-41, RNF-69, RNF-74, RNF-75, RNF-76 (653-655, 691, 721-725): usan "M-16 Gestor de Evidencia" (Emisor) para evidencia de Retail (conformidad de recepción de mercadería, garantía legal, datos personales de retail). El Emisor no debe custodiar evidencia de Retail.
- Sugerencia: asignar cada fila al servicio de su ámbito (catálogo v3.1, columnas Servicio y Frente). Confirmado.

**G-8. Sitios y zonas antiguos en la columna de componente de la disponibilidad y la recuperación.**
- RNF-02, 24-31 (331, 621-637), RNF-32 y RNF-68 (637, 689): "Nodo de tienda on-premise (Z2) + Nube Multi-AZ (Z1) + Site Principal/Secundario (Z3)", "Site Principal / Site Secundario".
- Debe decir: nodo local de tienda (L-01 a L-03), CLD-01 Chile Central (tres zonas), CLD-02 Brazil South (recuperación), DC-01 y DC-02. El glosario prohíbe "Site Principal", "Site Secundario" y "Z1/Z2/Z3" fuera de la cita de las BT.
- Además, RNF-11 a RNF-14 (595-601): "separación física Z3 (ADR-11, ADR-12)". Esos ADR no existen: vigentes ADR-01 a ADR-07 (sd-04 Tabla 4.5); la separación de datos es ADR-02.
- RT-02.04 (733): "ADR-01 a ADR-12" debe ser "ADR-01 a ADR-07". Confirmado.

## 2. Hallazgos medianos

**M-1. Remisiones a secciones, tablas y figuras que no corresponden o no existen.**
- "Anexo A.5.1 (SUP-nn)" en las filas que citan el sd-03 (por ejemplo línea 133, 135, 163, 193). No existe un Anexo A.5.1. Los SUP están en el sd-02 Anexos A.4.1 (supuestos), y el sd-03 usa SP-nn en su Tabla 3.3 (SUP-19, 20, 26, 27 se citan en el texto). Corregir a "sd-02, Anexo A.4.1".
- "Subdoc.3 §3.2.4 (Tabla 3.5)" y "§3.2.5" en RNF-03, 05, 16, 17-21, 58 y RF-177 (líneas 335, 585, 603-613, 677 y otras). El sd-03 §3.2.4 es el "Catálogo de requerimientos" y su Tabla 3.5 es el "Criterio aplicado a los casos limítrofes". No hay en sd-03 ni sd-04 un "presupuesto de latencia por componente" (cero apariciones). El componente descrito, "Arquitectura orientada a eventos con presupuesto de latencia por componente (M-01, M-05, M-08, M-09, M-11)", es una afirmación sin respaldo. Las latencias están como metas en el sd-04 (líneas 386-388) y la Tabla 3.6 de sd-03 (resultados).
- "Subdoc.4 §4.2 (Tabla 4.9)" para alta disponibilidad, respaldos y puntos de falla (RNF-02, 24-31, 68 y RT-02.08, RT-02.09). La Tabla 4.9 del sd-04 es "Servicios contratados en Azure agrupados por función". Corresponden la Tabla 4.11 (puntos de falla y contingencia) y la Tabla 4.12 (pérdida y recuperación por zona y región).
- "Subdoc.4 §4.1 (Tabla 4.2; 'Recorridos y consistencia')": la Tabla 4.2 es "Servicios y autoridad del dato", que sirve para autoridad pero no para recorridos (esos están en la Figura 4.10).
- Subsecciones del sd-04 §4.1 que siguen existiendo con ese nombre: "Capas e interfaces", "Recorridos y consistencia", "Vista de datos y seguridad", "Seguridad, continuidad y observabilidad", "Decisiones y condiciones de aceptación", "Estilo y límites de contexto", "Vistas y actores de la solución": correctas. La mayor parte de las figuras citadas (4.3 a 4.12, 4.14, 4.17) existen.
- Sugerencia: reescribir la columna "Sección" tras remapear (G-1) y verificar cada Tabla y Figura contra los pies de figura de los sd-03 y sd-04. Confirmado.

**M-2. RNF-06 y RNF-07 (585-587).** El catálogo v3.1 define RNF-06 como evaluación crediticia ≤ 8 s en el POS y RNF-07 como tiempo total de originación ≤ 3 minutos. El formulario pone "evaluación ≤8s embebida en flujo POS" en RNF-07 y deja RNF-06 con el componente genérico de latencia. Intercambiar. Confirmado.

**M-3. RNF-02, RNF-30 y RNF-31 (331, 633, 635) sin umbral ni alineación con RT-10.01.** El catálogo v3.1 pone "disponibilidad ≥ 99,5 % (supuesto fundamentado)", pero BT RT-10.01 exige 99,9 % mensual para servicios críticos, y la verdad vigente declara ≥ 99,9 %. El caso solo puede endurecer. La descripción del formulario omite el valor y el "Sí" queda ambiguo. Sugerencia: declarar ≥ 99,9 % para el canal digital y los servicios financieros críticos, y corregir el catálogo. Por confirmar (si 99,5 % es una cifra del catálogo que el equipo quiere mantener, el formulario no puede asumirla).

**M-4. RNF-22 y RNF-23 (617, 619): carga de prueba.** BT RT-09.06 exige pruebas de carga a 1,5 veces el peak (la verdad vigente confirma 1,5). La fila solo declara "escalamiento elástico Z1 y capacidad fija Z2/Z3", sin el volumen (104.000 pedidos en tres días, proyección ≈ 150.000; 380 líneas de caja, 430 proyectadas) ni la prueba. El sd-04 trata el dimensionamiento en "Dimensionamiento y plan de capacidad" y la Tabla 4.14. Citar ambos y la prueba.

**M-5. RNF-41 a RNF-47 (655-667) comparten un componente que no corresponde.** RNF-41 a RNF-47 usan "M-16 / M-13 / M-21 / Tabla 3.8" para retenciones de: documentos tributarios (ERP/DTE), movimientos de inventario (R:M-03), trazabilidad de precio (R:M-01), fidelización (R:CL-02, según el catálogo) y videovigilancia. La Tabla 3.8 del sd-03 es la del servicio de control de cruces. Asignar cada retención a su servicio y a la sección que la trate. Confirmado para RNF-44, 45, 46, 47.

**M-6. RT-02.02 (729).** Cita ADR-01 (escenario B) como respaldo de la modularidad. Corresponde ADR-05 (partición DDD, condicionada). Además dice "Microservicios", pero el sd-04 (línea 194) establece diez servicios como microservicio, dos como módulo y uno por decidir. BT 2.3 advierte contra microservicios sin justificación. Ajustar el nombre a "módulos con límites de contexto; diez de trece servicios como microservicio".

**M-7. RT-02.07 y RT-02.05 (739, 735): "M-20", "Azure Event Hubs compatible Kafka".** El producto está elegido en el sd-04 (Event Hubs Premium) pero "Condicionada" (ADR-06). "M-20" no existe (G-1). Indicar el estado condicionado.

**M-8. RNF-35 (643) y RNF-48 (669).** Remiten al sd-04 §4.2.1 Figura 4.17 (existe) y a Tabla 4.11. Verificar que "Tabla 4.11" sea la de segmentación: es de puntos de falla. Falta citar la Figura 4.14 (red) para RNF-35. RNF-48 cita "RT-02.12-C" (ID que no existe como tal; es RT-02.12 con el parámetro del Caso cap. 15).

**M-9. Columnas pedidas por BT 1.5 que el formulario no tiene.** BT 1.5 pide por cada RT: cumple / parcialmente / no cumple, componente "individualizado por nombre y versión", sección y página de la Oferta Técnica, y la evidencia de verificación. La tabla no tiene versión, página ni evidencia (el T-12 de las Bases Administrativas pide solo 5 columnas, así que esto no incumple el formulario, pero BT 1.5 dice que "cumple" sin componente y sin lugar equivale a no declarar). Sugerencia: agregar página y evidencia, o una columna de condición. Por confirmar.

**M-10. Sin intro ni nota de pendientes.** La sección (línea 94) abre la tabla sin explicar que el catálogo se cita en su versión vigente ni la regla de las tablas incompletas. No es un error de las Bases.

## 3. Hallazgos bajos

- B-1 (línea 102): la etiqueta de la tabla es `tab:a-1` (herencia de un anexo del sd-02), con rótulo "T-12.n".
- B-2 (línea 619 y otras): "\%" y "100\%" mezclan el formato con el catálogo (RNF-51 línea 679 "100\%" frente a "100%"). Sin efecto.
- B-3: mayúsculas y nombres: "canal digital" en RF-017 y RNF-30 (el glosario lo marca como nombre provisional por definir). "Postventa" (M-13) frente a "posventa" (glosario). Se resuelve con G-1.
- B-4: "Registro de Decisiones de Arquitectura" en singular (RT-02.04) frente a "Decisiones de arquitectura" de la Tabla 4.5 del sd-04. Sin efecto.
- B-5: orden: los RNF se intercalan entre los RF según el grupo funcional (RNF-02 entre RF-103 y RF-104, etc.), y RNF-04 a RNF-76 van tras RF-226. Funciona, pero un revisor no encuentra un RNF por ID. Sugerencia: separar en bloques RF, RNF, OP, RT.

## 4. Verificaciones sin hallazgos

- RT obligatorios del tramo: RT-02.01 a RT-02.07 están presentes, sin duplicados ni faltantes, con carácter "Obligatorio". No hay RT en el Capítulo 1. RT-02.08 en adelante están fuera del tramo.
- Duplicados de RF y RNF: ninguno. Los RF-001 a RF-226 y RNF-02 a RNF-76 están completos salvo los ya citados.
- Umbrales: ninguna fila del tramo declara un valor menor que el RT o el Caso en la descripción. El problema es que no lo repiten (M-3, M-4) y que RNF-25 se apoya en un sd-04 que dice 4 horas (G-4).
- Productos y marcas del tramo: no aparecen HSM como producto, SIEM, Fortinet ni Dell. Aparece "HSM" genérico (RNF-33 a RNF-37, RNF-59, seis filas) respaldado en el sd-04 solo como "Managed HSM, por probar" para el Emisor; Go/Java y Azure Cache for Redis (G-6); Event Hubs (M-7). Sentinel y FortiGate sí figuran en el sd-04 (líneas 536 y 552), pero no en este tramo.
- Diferencias con el sd-02: el sd-02 (Anexos A.1 a A.3 y Tabla 2.6) también está en v3.0 (307 elementos, 223 RF, 75 RNF, 9 OP). Diferencias con el formulario: el sd-02 sí lista OP-01 a OP-09 y RF-027; el formulario no. Ambos deben pasar a v3.1. El sd-02 remite la trazabilidad al T-12 ("matriz de cumplimiento y trazabilidad del Formulario T-12", línea 727), pero cita "374 requisitos técnicos (RT)" en total; la tabla del formulario debe cerrar esa cuenta en el otro tramo (RT-02.08 en adelante).
