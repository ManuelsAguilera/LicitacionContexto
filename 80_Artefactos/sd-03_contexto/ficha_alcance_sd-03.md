# Ficha de alcance del sd-03 (Esquema de solución y alcance)

Documento de contexto, no es entregable. Actualizado el 2026-10-08. Resume lo vigente del alcance para quien trabaje el sd-03 o sus vecinos (sd-02, sd-04, sd-07, sd-08) y para cargarlo en el contexto de los agentes. **No es fuente de verdad.** Manda `02_Propuesta/latex_final/sd-03.tex` y, para el detalle, los Anexos A a D en `04_Adjuntos/tablas/`. Si esta ficha difiere de ellos, está desactualizada. Cada dato indica su fuente entre paréntesis.

## 1. Estado de las secciones

| Sección | Estado | Observación |
| :-- | :-- | :-- |
| 3.1 Resumen ejecutivo | Redactada | Faltan figuras y revisión humana |
| 3.2 Alcance (3.2.1 a 3.2.5) | Redactada y evaluada con los dos agentes | Falta el cierre de la sección (sección 7 de esta ficha) |
| Introducción del capítulo 3 | Sin redactar | Se escribe al final |
| 3.3 Esquema de solución y 3.4 Explicación de la solución | Las elabora otro integrante del equipo | Insumos en `insumos_3.3_3.4.md` |

Ningún apartado tiene estado «revisado». Ese estado lo asigna solo una persona.

## 2. Nomenclatura (fuente: `divisiones_negocio_servicios_sd-03.md`)

Jerarquía. El problema se divide en tres **frentes** (retail, filial emisora y frontera). Retail y filial emisora se dividen en **áreas** y cada área se cumple con **servicios**. Son 13 servicios sobre una **base tecnológica** (plataforma de integración, identidad y gestión de accesos, observabilidad). El despliegue híbrido no es un servicio.

| Código | Servicio | Etapa |
| :-- | :-- | :-- |
| R:M-01 | Servicio de oferta comercial | 1 |
| R:M-02 | Servicio de abastecimiento | 2 |
| R:M-03 | Servicio de existencias | 1 |
| R:V-01 | Servicio de pedidos | 2 |
| R:V-02 | Servicio de ventas | 1 |
| R:V-03 | Servicio de comisiones | 2 |
| R:V-04 | Servicio de marketplace | 2 |
| R:CL-01 | Servicio de posventa | 2 |
| R:CL-02 | Servicio de clientes Retail | 2 |
| F:C-01 | Servicio de originación de crédito | 1 |
| F:C-02 | Servicio de cartera de crédito | 1 y 2 (por tramos) |
| F:C-03 | Servicio de evidencia financiera | 1 |
| X-01 | Servicio de control de cruces | 1 |

Reglas de uso. En la prosa se escribe «Servicio de …» y los códigos solo en tablas. Los códigos antiguos (R-01 a X-01) y sus nombres están obsoletos. «Causa C1» a «causa C5» son las causas raíz del sd-02 y no tienen relación con el código `F:C-01`.

## 3. Cronograma y supuestos de fecha (fuente: Bases Administrativas, art. 15 a 17; sd-03.tex 3.2.2 y 3.2.3)

- Etapa 1. Desarrollo meses 1 a 12, marcha blanca meses 13 a 15, producción en el mes 16.
- Etapa 2. Desarrollo meses 13 a 18, marcha blanca meses 19 y 20, producción en el mes 21.
- Operación meses 21 a 56. Total 56 meses, innegociable.
- Mes 1 es enero de 2027 (SUP-26). Mes 16 es abril de 2028, mes 21 es septiembre de 2028 y mes 24 es diciembre de 2028. «Antes de 2029» equivale a mes 24 como máximo.
- La plataforma de crédito de 2011 se retira en octubre de 2028. El sistema central de 2009 se retira durante la operación.
- Los pasos a producción de los meses 16 y 21 quedan fuera de las cinco ventanas de congelamiento (Caso 13.2).
- Autonomía sin enlace: **24 horas** (RT-03.10). No existe otro valor. El «8 h» del sd-02 describe lo que el cliente exige, no lo que compromete la propuesta.
- El período de consultas **ya cerró** (art. 43, del 20-08 al 01-09-2026). Lo pendiente no se «consulta al mandante». Se valida con el cliente al inicio del proyecto.

## 4. Decisiones de alcance vigentes

- **Criterio de reparto por etapa.** Un componente va a la Etapa 1 si cumple al menos una de cuatro pruebas: sostiene una promesa priorizada por el comité (existencia, precio), es condición de una objeción registrada (frontera de datos de la contralora, migración de la cartera antes de 2029), es necesario para que la Etapa 1 sea el registro oficial desde el mes 16 o es dependencia de otro que cumple alguna. Lo que no cumple ninguna va a la Etapa 2 (sd-03.tex 3.2.2, Tabla 3.1).
- **Adelanto del negocio financiero.** Se aparta de la preferencia del comité, que lo ubicó al final, por el fin de soporte de 2029 y la migración de 620.000 clientes con saldo, que migran por tramos y sin corte único.
- **Capacidad de absorción.** Se descartó como criterio de reparto. No se menciona en el cuerpo.
- **Crédito sin conexión.** No se abren tarjetas ni se amplían cupos sin enlace (EXC-16). La compra con cupo vigente usa un cupo preaprobado en caché con topes que fija el emisor (opción B2, RC-11, SP-03). Hay un plan alternativo si falla la habilitación técnica.
- **Plataformas.** Se reemplazan por etapas el sistema central de retail (2009), la plataforma de crédito (2011) y el punto de venta (2014). Se conservan e integran el sistema de gestión empresarial, el marketplace (2022), el sistema de almacenes del centro de distribución principal, el comercio electrónico y la fidelización. Las planillas dejan de ser el registro oficial. Concepción se evalúa y se costea, no se incorpora (EXC-13, SP-02).
- **Fuente única de la existencia.** El servicio de existencias decide lo que se puede prometer (Caso 16.1).
- **Historial de precios.** Tres años, no cinco (RNF-44, RNF-58).
- **Supuestos (revisados el 2026-10-08).** El Caso exige declarar como supuesto toda decisión que el proponente tomó por el cliente, incluidas las 25 del numeral 16.1 (Caso cap. 16, 17.1 y criterio de evaluación del cap. 17). En el capítulo 2, SUP-n es la decisión n del 16.1. SP-02 es el SUP-20 (Concepción no es origen de promesa digital mientras opere con planillas, RN-15). SUP-26 (inicio en enero de 2027) se infiere de T-20, art. 68 y el congelamiento hasta el 6 de enero. Con inicio en diciembre o febrero, el mes 16 cae en un congelamiento. SP-03 se valida con la filial emisora y su asesoría jurídica. **SP-04 (decidido el 2026-10-08, opción b):** el proponente provee el centro de datos on-premise con su conectividad, seguridad y canalizaciones (RT-06.33 y art. 14.2) y el cliente hace la obra civil de separación (RT-06.06). Para tiendas y centros de distribución el cliente adquiere el hardware, ejecuta las obras y contrata los enlaces, y el proponente los especifica, costea, coordina, certifica y configura (Caso cap. 11).
- **Exclusiones, supuestos, responsabilidades del cliente y restricciones.** Anexo A (EXC-01 a EXC-19, SP-01 a SP-04, SUP-26 y SUP-27, RC-01 a RC-11).

## 5. Catálogo de requerimientos (fuente: Anexo B; Excel v3.1 como propuesta)

- Cifras vigentes: **308 elementos, 227 RF, 72 RNF y 9 OP**. Partieron de 307 (223, 75 y 9). La depuración dejó 303 y se agregaron 5 RF para el servicio de clientes Retail (RF-227 a RF-231).
- Por etapa: Etapa 1 con 142 RF y 61 RNF, Etapa 2 con 81 RF y 11 RNF, 4 RF en ambas etapas y 9 OP en todo el proyecto. Prioridad: alta 152 RF, 72 RNF y 9 OP, y media 75 RF.
- Los códigos RF, RNF, OP y RN se leen en el Anexo B y en el registro de reglas de negocio (Anexo C: RN-01 a RN-60 y RN-P01 a RN-P05).
- RNF-61, RNF-62 y RNF-63 se reclasificaron como criterios de aceptación (resultados 2, 26 y 4 del Anexo D).
- Cada RNF lleva umbral y método de verificación. La trazabilidad completa con las Bases Transversales vive en el Formulario T-12, no en el sd-03.
- Cambios al catálogo se tramitan como solicitud formal ante el Comité Ejecutivo del contrato (art. 72).
- El **Excel oficial sigue en v3.0**. Los cambios del v3.1 los traslada el equipo (lista en `conciliacion_catalogo.md`).

## 6. Criterios de aceptación (fuente: sd-03.tex 3.2.5 y Anexo D)

- Tres niveles encadenados. Cada entregable (con artefacto, evidencia, trazabilidad y observaciones resueltas, art. 18.2; diez días hábiles para revisar y diez para subsanar, art. 18.3). Cada marcha blanca (art. 17.3, más la posibilidad de volver atrás; si se extiende, multa de 1 % del valor del hito por semana con tope de 10 %, art. 80). Y los 28 resultados de negocio del cap. 18 del Caso.
- El proponente controla la calidad. La Contraparte Técnica valida y firma el acta. El juicio de éxito de los 28 resultados es del cliente.
- Anexo D. Cada resultado lleva línea base (la del Caso), meta, servicio, momento, evidencia y responsable. Las metas que el Caso no fija se rotulan «propuesta del proponente».
- Resultados compartidos con la operación del cliente: 2, 4, 9, 15 y 26.
- Resultados en dos hitos: el 2 y el 25 (mes 16 con existencias y degradación, mes 21 con pedidos y prueba de carga completa).
- Ventana de medición: las metas anuales se miden con los últimos tres meses consecutivos antes del acta. Lo que depende del evento anual (fecha fijada por un tercero) queda como compromiso de operación.
- Compromisos del proponente sin respaldo textual en las Bases: el acta de recepción y el certificado de conformidad por tienda y centro de distribución.

## 7. Pendientes

**Redacción del sd-03.** Cierre de la 3.2 (renumerar tablas, coherencia de nombres y citas, figuras D1 a D5 sin duplicar con la 3.1, evaluador PMBOK sobre la sección completa, fila final del maestro y declaración de uso de IA). Introducción del capítulo 3. Armar los Anexos A a D como documento aparte. Dibujar las figuras. Revisión humana.

**Catálogo y Excel.** Trasladar al Excel oficial las decisiones del v3.1. Huecos de contenido, declarados y no inventados: abastecimiento (3 RF), comisiones (3) y cartera (6) con pocos requerimientos, imputación de pagos (RN-42), derecho de retracto, gastos de cobranza, publicación de la disponibilidad en 30 s (RT-05.29), corte de las 07:00, exactitud diaria del inventario y enlace de respaldo en 14 tiendas y Coyhaique. RNF-05 «por definir». SUP-08 y SUP-09 sin resolver (precio de etiqueta física frente a la propagación). RF-138 lista seis componentes de merma y el Caso, cinco. Referencias obsoletas en el Excel (RF-160, RF-161, RF-183, RNF-22, RNF-23). RN-39 y RN-53 sin origen ni criterio. Ubicación de RF-180 y RF-181 por confirmar. Requisitos de transición por revisar. Siete productos del Caso 17.1 que viven fuera del sd-03 (mapa de integraciones, registro de vacíos).

**Otros subdocumentos.** sd-02: aclarar «≥ 8 h en tienda», RNF-61 a RNF-63 contados como RNF, «Tabla 2.1» y «Tabla 2.6» para el mismo catálogo, y la cifra de discrepancia del 3 % sin fuente.

**Validar con el cliente al inicio del proyecto.** Los 16 supuestos por umbrales ausentes, los umbrales y metas propuestas por el proponente y la cobertura exacta del despliegue gradual del mes 16.

## 8. Reglas de redacción que más se incumplen

- Formal. Sin dos puntos ni punto y coma para explicar (RR-25). Sin cifras de impacto del problema. Citar Bases o Caso solo en decisiones grandes.
- «Causa C3», nunca «C3». «Filial emisora». Jerga de proyectos sin definir se evita. No repetir definiciones dadas antes.
- Texto de caída bajo cada título. Tablas con cinco columnas como máximo, celdas de una frase, con fuente y texto que concluye. Figuras citadas antes y explicadas después, escritas como comentarios `%` en el `.tex`.
- Detalle técnico va al capítulo que le corresponde (3.3, 3.4, sd-04, sd-07, sd-08).
- Se redacta con la skill humanizer, acotada por RR-24. Después se corre `exportar_latex.py verificar` y `verificar-redaccion --parte T7-03`, y se evalúa con los agentes `lector-no-tecnico` (dos fases) y `evaluador-pmbok`. Cada hallazgo se contrasta con las fuentes antes de aplicarlo.

## 9. Dónde está cada cosa

| Qué | Dónde |
| :-- | :-- |
| Texto vigente | `02_Propuesta/latex_final/sd-03.tex` |
| Anexos A a D | `04_Adjuntos/tablas/sd-03_s2_anexo-*.md` |
| Catálogo propuesto v3.1 | `01_Requerimientos/RequerimientosAtomizados_Depuracion_Alcance_v3.1.xlsx` |
| Nomenclatura | `80_Artefactos/sd-03_contexto/divisiones_negocio_servicios_sd-03.md` |
| Conciliación del catálogo y cambios al Excel | `80_Artefactos/sd-03_contexto/conciliacion_catalogo.md` |
| Condiciones del Caso 13.3 | `80_Artefactos/sd-03_contexto/condiciones_caso_13_3.md` |
| Crédito sin conexión | `80_Artefactos/sd-03_contexto/fundamentacion_credito_sin_conexion.md` |
| Historial de decisiones | `80_Artefactos/sd-03_contexto/auditoria_decisiones.md` (consulta puntual) |
| Material superado | `80_Artefactos/sd-03_contexto/historico/` (no usar) |
