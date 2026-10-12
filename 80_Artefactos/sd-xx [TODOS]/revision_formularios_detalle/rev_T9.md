> Detalle de la revisión de los formularios (2026-10-12). Borrador. **Nota:** cualquier hallazgo que diga que el Comité de Operación debe iniciar en el mes 16 es un falso positivo: el artículo 71 de las Bases fija «mensual desde el mes 13».

# Revisión Formulario T-9 (metodología de gestión)

Archivo: `02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-9.tex` (1.777 líneas). Todas las líneas citadas son de ese archivo salvo que se indique otra fuente.
Contraste: Bases Admin. (T-9 en la línea 2268, que remite al Subdocumento 6 letra a, líneas 2066 y 2130 en adelante), sd-01 a sd-04, `verdad_proyecto.md` y el cuerpo del sd-06. Ese cuerpo ya no está en el árbol de trabajo (`OSS-Subdocumento6.tex` figura como borrado), así que se leyó con `git show HEAD:`.

Cobertura de la definición oficial: el T-9 pide adjuntar la información del Subdocumento 6 letra a. Esa letra incluye PMBOK adaptado con enfoques ágiles, interesados, comunicaciones, adquisiciones e integración, y ceremonias, artefactos, cadencias y mecanismos de decisión. El formulario cubre todo eso (T-9.1 a T-9.8). No encontré omisiones de fondo. No hay precios (art. 50 respetado).

## Hallazgos

### Graves

**G-1. Comité de Operación "mensual desde el mes 13" (debe ser mes 16).**
- Ocurrencias en el T-9:
  - Línea 399, Tabla de instancias: "Mensual desde el mes 13".
  - Línea 1262, Matriz de comunicaciones: "Mensual desde el mes 13".
  - Línea 1658, Tabla de gobierno por etapas, fila "Meses 13 a 15": "Comité de Operación desde el mes 13; sala de control diaria".
- Fuente correcta: sd-01 línea 339 ("mensualmente desde el mes 16, cuando la Etapa 1 entra en producción") y `verdad_proyecto` (mes 16).
- Hay un conflicto de fondo que conviene saber. El texto literal de las Bases (art. 71, línea 1458) y el cuerpo del sd-06 (líneas 335, 1250, 1856, 2820) dicen "mes 13". El T-9 copia al sd-06, pero ambos contradicen al sd-01 y a la verdad vigente.
- Sugerencia (confirmado, es la verdad vigente):
  - Cambiar a "desde el mes 16" en las tres ocurrencias.
  - Mover la mención en la tabla por etapas de la fila "Meses 13 a 15" a la fila "Meses 16 a 18". Hoy esa fila solo dice "Cierre de la Etapa 1 en el mes 16" y no menciona al Comité de Operación.
  - En la fila "Meses 21 a 56" ("El Comité de Operación asume el seguimiento ordinario") hay que reformularlo, porque el comité ya existe desde el mes 16.
  - Ajustar el sd-06 (6.1.2, 6.1.5, 6.1.7) en paralelo.
  - Por confirmar con el equipo: cómo se justifica ante las Bases el apartarse de "mes 13". La opción segura es nombrar el comité desde el mes 16 y mantener la sala de control diaria y la preparación de soporte en los meses 13 a 15 dentro del Comité de Proyecto.
- Efecto colateral: en la línea 410 (Tabla de entradas y agenda) la agenda del Comité de Operación incluye "preparación de la marcha blanca". Con inicio en el mes 16, solo cabe la marcha blanca de la Etapa 2 (meses 19 y 20). Hay que precisarlo.

**G-2. Cruces Retail–Emisor: la instancia que aprueba está descrita de tres maneras y ninguna coincide con el sd-03/sd-04.**
- Verdad: el área de cumplimiento aprueba la ficha de cada cruce (sd-04 líneas 372 y 413; sd-03 Tabla 3.8, línea 604 "cumplimiento aprueba"). El único cruce autorizado es X-01.
- En el T-9:
  - Línea 509, escalamiento: "Líder de Datos, Encargado de Seguridad y contraparte de cumplimiento → Comité de Arquitectura → Comité Ejecutivo; no se aprueba sin las tres evaluaciones".
  - Línea 506, rol "Contraparte de cumplimiento": "Su evaluación documentada es previa a toda aprobación de un cruce". Aquí cumplimiento solo evalúa; no aprueba.
  - Línea 831 (tensión 6, columna "Decide"): "Instancia competente, con las evaluaciones documentadas". No nombra a nadie. En la columna "Tratamiento" dice "aprobación de Contraloría y del Negocio Financiero".
- Problemas:
  - Un cruce nuevo aprobado por el Comité de Arquitectura o el Comité Ejecutivo del proyecto contradice que aprueba cumplimiento de Ancoa.
  - "Instancia competente" es una remisión vacía.
  - No se dice qué es "contraparte de cumplimiento" en sd-04 ("área de cumplimiento", sin precisar si es del Cliente o de la filial) frente a "Contraloría y Negocio Financiero" del T-9.
- Sugerencia (por confirmar): unificar. Propuesta: el área de cumplimiento de Ancoa aprueba la ficha de cada cruce en X-01; Líder de Datos y Encargado de Seguridad evalúan antes; el Comité de Arquitectura registra la decisión técnica y el Comité Ejecutivo solo conoce las discrepancias. Reemplazar "Instancia competente" por esa instancia. Nombrar el rol igual que el sd-03/sd-04 ("área de cumplimiento", y si procede su integrante de Ancoa). Alinear la línea 506 ("aprueba" en vez de "evalúa").

**G-3. Marcas Fortinet y Dell presentadas como proveedores.**
- Líneas 1534 y 1535 (Tabla de dependencias por tipo): "Seguridad y conectividad (Fortinet o equivalente justificado)" y "Only Simple Solutions (Dell Technologies u opción técnicamente equivalente)".
- Solo Microsoft Azure está decidida (sd-01 línea 345; `verdad_proyecto`). En el sd-01 a sd-04 no figuran ni Fortinet ni Dell. La línea 1527 ya remite al T-11 para "marca, modelo y soporte".
- Sugerencia (confirmado): quitar las marcas y dejar "Seguridad y conectividad (producto por definir)" y "Componentes on-premise de la solución y su licenciamiento (producto por definir)", o mover la marca al T-11 si allí ya se decidió. Origen del texto: sd-06 HEAD líneas 2294, 2403 y 2424.
- Además la línea 1535 dice que Only Simple Solutions provee los componentes on-premise. Eso coincide con el reparto (proponente provee infraestructura del centro de datos, art. 14.2), pero la fila 1534 dice "instalación física por Ancoa o su integrador cuando corresponda". Conviene precisar que la instalación de hardware de tiendas y centros la hace el Cliente y la del DC-01 y DC-02 el proponente, o dejarlo así si no hay precisión en el sd-04.

### Medianas

**M-1. Roles sin respaldo en el sd-01 (equipo de 16 personas, seis áreas de trabajo).**
- El T-9 (Tabla de roles, líneas 520-533, y varias tablas) usa Líder de Desarrollo, Líder Funcional, Líder de Integración, Scrum Master (uno por equipo) y "Líder de Calidad y Pruebas".
- El sd-01 (líneas 186-198 y 311-328) no define Líder de Desarrollo, Funcional ni Integración. Solo trae Jefe de Proyecto, Arquitecto de Solución con 2 ingenieros, Seguridad con analista, Datos con 2 ingenieros, Calidad con 2 QA, Operación con ingeniero DevOps/Soporte, Implantación con especialista. Total 16. El rol se llama "Líder de Calidad", no "Líder de Calidad y Pruebas".
- Los roles que el T-9 trae vienen del RT-19.02 de las Bases Transversales (Bases_Transversales línea 802-820) y del sd-06.
- Consecuencias:
  - La línea 531 dice "Líder de Desarrollo y Líder Funcional con dedicación completa en implementación", pero esas personas no están en la dotación del sd-01.
  - La línea 529 (Líder de Integración) no aparece en el sd-01.
  - Los "equipos Scrum" y "Scrum Master, uno por equipo" no se pueden contar dentro de 16 personas.
- Sugerencia (por confirmar con sd-01/T-8/T-15): declarar qué área de trabajo acumula cada rol (por ejemplo, Líder de Desarrollo y Funcional dentro del área de Arquitectura, o Integración en Arquitectura), o ampliar el sd-01. La línea 524 ya dice que la composición está en T-8 y T-15 sin duplicar capacidad. Hay que verificar que T-8 y T-15 lo cumplan. Unificar el nombre "Líder de Calidad" (sd-01) con "Líder de Calidad y Pruebas" (RT-19.02).

**M-2. Dedicaciones: faltan las de varios roles frente a RT-19.02.**
- La Tabla de roles da dedicación a: Jefe de Proyecto (exclusiva en implementación, correcto con RT-19.02), Líder de Datos (permanente), Líder de Desarrollo y Funcional (completa), Líder de Integración (permanente), Operación desde mes 6 y Implantación desde mes 8 (correcto).
- No da dedicación al Arquitecto de Solución ("alta en diseño, permanente en el Comité de Arquitectura"), Encargado de Seguridad ("permanente") ni Líder de Calidad ("permanente").
- Sugerencia (confirmado, fuente RT-19.02): completar esas tres celdas o remitir expresamente al T-8.

**M-3. Hito del plan para la dirección: H1 en el T-9 frente a H2 en el T-14.**
- En el T-9, plan para la dirección "aprobado en H1" (líneas 187, 190, 197, 359) y "Mes 1; aprobación en H1" (línea 676). Tabla por etapas, fila meses 1-12: "Plan para la dirección en H1; arquitectura base en H2 (mes 4)".
- En el T-14, fila 1.1.1 (línea 112) dice "Plan firmado... al terminar el mes 3... H2 (mes 4)". La fila 1.1.10 sitúa el acta de constitución en H1 (mes 2) y "aprobada al inicio del mes 1".
- H1 es el mes 2 (cierre del levantamiento y línea base de alcance, Bases E-25, línea 2636). El plan de dirección debe estar en H2 según el T-14. El T-9 lo coloca en H1 y la línea base de costos en H1 también.
- Sugerencia (por confirmar con el T-14): decir "plan para la dirección y líneas base aprobados en H2 (mes 4)" o ajustar el T-14. Mantener H1 solo para el acta de constitución, el alcance y la matriz de trazabilidad. Las líneas 187-197 (Integración, Comunicaciones, Interesados "aprobado en H1") y 676 deben coincidir.

**M-4. Uso de "frente" y "responsable de frente" con el significado de las áreas de trabajo.**
- Líneas 191, 199, 207 (Tabla de procesos), 275 (Registro de dependencias: "líderes de frente"), 1305 y 1316 ("responsable de cada frente"), 1790 ("transferencia al frente que continúa"), 1822 (lección "Identificador y frente"), entre otras.
- El glosario reserva "frente" para los tres frentes de la solución (Retail, Filial emisora, Frontera); los equipos del sd-01 son "áreas de trabajo".
- Sugerencia (confirmado): reemplazar por "área de trabajo" cuando se hable de equipos; si en las tablas de lecciones se quiere el frente de la solución, decirlo expresamente.

**M-5. Reparto proponente/Cliente en hardware y obras.**
- Línea 1536: "Hardware de terreno y dispositivos de tiendas y centros: Ancoa". Correcto según la verdad (el Cliente adquiere, instala y contrata; el proponente especifica). La fila de "Conectividad, seguridad y canalizaciones del centro local: Only Simple Solutions" (línea 1538) y la de "Obras eléctricas, canalizaciones y cableado de tiendas y centros: Según las exclusiones contractuales" (línea 1539) son ambiguas.
- Problema: no queda claro si "centro local" es el centro de datos de casa matriz (DC-01) o el centro de distribución. La verdad dice que el proponente provee la infraestructura on-premise del centro de datos. Los términos "centro local" y "sitio" no figuran en el glosario (que usa DC-01, DC-02, CD-01, CD-02, SIT-01).
- Sugerencia (por confirmar): sustituir "centro local" por DC-01 y DC-02, y remitir en la fila de obras a las exclusiones EXC-nn concretas del sd-03 Anexo A.

**M-6. Nombre del interesado I-09 / "Negocio Financiero".**
- Líneas 520 (rol "Contraparte de cumplimiento: Ancoa (Contraloría y Negocio Financiero)"), 842 (I-09 "Negocio Financiero (filial emisora)"), 865, 1195 y otras.
- El glosario dice que "Negocio financiero" es la línea de negocio, no la entidad ni el gerente; la entidad es "filial emisora". Aquí se usa "Negocio Financiero" con mayúsculas como si fuera una gerencia u órgano que designa dueño de producto (Tabla de dueños, línea ~1001) y que valida.
- Sugerencia (por confirmar con la fuente, en el Caso hay una "Gerencia del Negocio Financiero"): si el Caso nombra una gerencia, citarla con su nombre; si no, "filial emisora". Revisar contra el sd-02 (mapa de actores).

**M-7. Referencias a tablas y figuras del sd-06 posiblemente inexistentes.**
- El T-9 remite a "Tabla 6.3" (línea ~896), "Tabla 6.5" (línea ~1115), "Tabla 6.8" (línea ~1506), "Figuras 6.1 y 6.2" (línea ~1190) y "sección 6.1.4.1" del Subdocumento 6.
- El sd-06 en HEAD numera "Tabla 3", "Tabla 5", "Tabla 8" y "Figura 1", "Figura 2" (líneas 993, 1217, 2611, 809, 912). La sección 6.1.4.1 sí existe (línea 671).
- El cuerpo actual del sd-06 no está en el árbol de trabajo, así que no se puede verificar la numeración vigente.
- Sugerencia (por confirmar): verificar cuando se publique el sd-06 y alinear las remisiones.

### Bajas

**B-1. "Plazo de 2029" en la tensión 7 (línea 836).** Dice "Prioridad del inventario frente al plazo de 2029 (I-02 e I-09)". Es la lectura del Caso (fin de soporte y último hito de remediación en 2029), pero el cronograma del proyecto migra la cartera a más tardar en el mes 22 y apaga la plataforma antes del 31-oct-2028; la remediación cierra en el mes 24. Sugerencia: "plazo de la plataforma de crédito (fin de soporte 2029; migración de cartera hasta el mes 22)". Por confirmar el texto exacto con el sd-02/sd-03.

**B-2. Variantes "cliente" y "Cliente".** Se usa "cliente" en minúscula con el sentido de parte contratante (líneas 168, 231, etc.). Glosario: "Cliente" con mayúscula para la parte; "cliente" para el comprador de tienda. En esta tabla: líneas 262, 337, 1305 (varias). También "mandante" no aparece (correcto).

**B-3. "Meses 16 a 18: Producción de la Etapa 1 y construcción de la Etapa 2".** La Etapa 2 se desarrolla en los meses 13 a 18 (según la verdad). La fila 13-15 dice "desarrollo de la Etapa 2" y la 16-18 "construcción de la Etapa 2": coherente en contenido, pero se podría unificar "desarrollo".

**B-4. "Comité Ejecutivo mensual".** La verdad lo trae como Comité Ejecutivo (art. 72). Las Bases (art. 71) y el sd-01 coinciden con "Mensual". Sin hallazgo; solo se anota que la fila de la Tabla de enfoque (línea 215) dice "Comité de Proyecto quincenal y Comité Ejecutivo mensual", correcto.

**B-5. Roles en la Tabla de comunicaciones (línea ~1266).** "Developers" como emisor del Daily Scrum, anglicismo, mientras todo el resto está en español. Sugerencia: "Equipo de desarrollo".

**B-6. Cifras del T-9 revisadas y consistentes con las Bases:** diez días hábiles para pronunciarse y diez para subsanar (art. 18.3, línea 501); desviación mayor al 10 % y cinco días hábiles (RT-19.10); incidente crítico en dos horas (RT-11.18); brecha en 24 horas y causa raíz en cinco días hábiles (RT-11.19); modificaciones hasta 20 % (línea 1472); subcontratación hasta 40 % (línea 1486); cierre del mes 16, 21 y 56; 26 interesados; 22 agentes de cambio. Ningún hallazgo.

## Puntos revisados sin hallazgo
- Versión del catálogo: el T-9 no menciona la versión (ni 3.0 ni 3.1) ni el número de elementos. No hay incoherencia. Si se agrega una referencia, usar 3.1 (308 elementos). El sd-06 HEAD dice v3.0 con 307 elementos (línea 2959), desactualizado respecto de la verdad; corregir allí.
- Meses de inicio de Operación (21) y producción (16 y 21), marcha blanca (13-15 y 19-20): consistentes.
- Hitos citados (H1, H2 mes 4, H6): H2 mes 4 correcto. H6 es el inicio de marcha blanca de la Etapa 1 (mes 13); la regla "agente de cambio en las 22 tiendas antes de H6" es coherente.
- Microsoft Azure como única alianza: correcto (líneas 1533 y PMIS).
- Herramientas PMIS (Jira, SharePoint, Slack): sin base contraria en sd-01 a sd-04; por confirmar si el equipo las ha decidido. El sd-01 no las menciona.

## Resumen de conteo
Graves 3 (G-1 a G-3), medianas 7 (M-1 a M-7), bajas 5 útiles (B-1, B-2, B-3, B-5, y B-4/B-6 como notas de verificación).
