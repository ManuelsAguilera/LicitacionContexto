# Conciliación del catálogo de requerimientos con el alcance (sd-03, subsección 3.2.4)

Documento de contexto, no es entregable. Fecha: 2026-10-08 (versión 2, con la auditoría independiente incorporada). Registra las decisiones que el asistente tomó para conciliar el catálogo oficial (`01_Requerimientos/RequerimientosAtomizados_Depuracion_Alcance.xlsx`, v3.0) con el alcance concretado en esta entrega. Autorización del usuario: definir lo que estuviera mal definido, basándose exclusivamente en lo concretado del alcance y en las decisiones de estos chats. Las decisiones se pueden revisar y revertir. Los nombres de servicios son los de `divisiones_negocio_servicios_sd-03.md`. El resultado se publica en `04_Adjuntos/tablas/sd-03_s2_anexo-b_catalogo-requerimientos.md` (Anexo B) y `sd-03_s2_anexo-c_reglas-de-negocio.md` (Anexo C). **El Excel v3.0 no se editó**. Las decisiones se llevaron a un archivo nuevo, `01_Requerimientos/RequerimientosAtomizados_Depuracion_Alcance_v3.1.xlsx`, con formato listo para el anexo. El equipo decide si v3.1 reemplaza a la v3.0 (ver la lista del final).

## Resultado

| | Catálogo del capítulo 2 | Tras la depuración | Con los requerimientos agregados |
| :-- | --: | --: | --: |
| Requerimientos funcionales (RF) | 223 | 222 | 227 |
| Requerimientos no funcionales (RNF) | 75 | 72 | 72 |
| Obligaciones del proponente (OP) | 9 | 9 | 9 |
| Total | 307 | 303 | 308 |

Depuración: se elimina RF-027 y se reclasifican RNF-61, RNF-62 y RNF-63 como criterios de aceptación. **RF-071 se mantiene** (la auditoría mostró que EXC-05 exige la base de comisión entre canales y que RF-054 no considera el canal de cumplimiento). Por eso se llega a 303 y no a los 302 que anticipa el pie de la hoja `7_Depuracion_Alcance`. Ese pie suma «5 eliminaciones, 9 traslados, 1 consolidación y 3 reclasificaciones» (18) para una baja de 9: los traslados a OP no reducen filas porque las OP ya estaban contadas. Las otras cuatro eliminaciones (RF-025, RF-026, RF-031 y RNF-01) ya estaban aplicadas en el catálogo de 307 filas.

**Requerimientos agregados (RF-227 a RF-231).** El servicio de clientes Retail no tenía ningún requerimiento funcional. Se derivaron cinco, solo de lo que el alcance ya fija: lo que incluye el servicio según la nomenclatura vigente (deduplicación de clientes, puntos, segmentos y campañas), la regla RN-03 y EXC-15 (la fidelización se conserva y se integra al servicio): consolidar duplicados, registrar movimientos de puntos, construir segmentos solo con atributos comerciales, ejecutar campañas y sincronizar con la fidelización conservada. La auditoría descartó un sexto (identificador por ámbito) porque RF-173 ya lo cubre. Etapa 2, prioridad media, marcados «Propuesto por el proponente, por validar». No se inventaron umbrales ni cifras.

## Correcciones a lo dicho antes en esta conversación

- Los saltos de numeración (faltan RF-025, RF-026, RF-031 y RNF-01) **no** corresponden a requerimientos divididos. Son eliminaciones de la hoja 7 por presuponer etiquetas electrónicas (EXC-02).
- La hoja `0_Lectura` del Excel conserva totales desactualizados (226 RF, 76 RNF, 311 filas). Los vigentes son los de la hoja `4_Resumen`: 223, 75 y 9. De ahí venía el error «226 y 76» del borrador antiguo de la 3.2.4.

## Decisiones sobre la hoja 7 (28 propuestas)

| Grupo | IDs | Decisión | Fundamento en el alcance concretado |
| :-- | :-- | :-- | :-- |
| Eliminar | RF-025, RF-026, RF-031, RNF-01 | Ya eliminados | EXC-02 |
| Eliminar | RF-027 | Eliminado ahora | EXC-02 |
| Trasladar | OP-01 a OP-09 | Se mantienen como OP | EXC-02, EXC-03 y EXC-13: obligaciones de la oferta |
| Consolidar | RF-071 | **Se mantiene** (decisión corregida) | EXC-05: base de comisión entre canales |
| Reclasificar | RNF-61, RNF-62, RNF-63 | Pasan a criterios de aceptación | Metas del capítulo 18 compartidas con la operación del cliente (3.2.5). La hoja `3_Hallazgos_v3` (H-21) las conservaba como efectividad de negocio y la hoja 7 propone reclasificarlas: se sigue la hoja 7. El capítulo 2 las cuenta aún como RNF (75) |
| Revisar | RF-153 a RF-156 | Se mantienen | Unidades en probador: causa C1 del capítulo 2 (el Caso las trata como punto ciego) |
| Revisar | RNF-46 | Se mantiene, servicio de clientes Retail, Etapa 2 | EXC-15 |
| Revisar | RF-170 | Se mantiene en control de cruces | Control de frontera, junto con RF-171 |
| Condicionar | RF-089, 090, 091, 094 | Se mantienen con marca | Plan alternativo del crédito sin conexión (3.2.3); si la prueba falla, función no disponible |

Nueve filas con «??» (hallazgo H-19) no se confirman: quedan como riesgo de requisitos no validados.

## Reasignaciones de servicio (regla: el servicio dueño del dato lleva el requerimiento)

Las 26 asignaciones dudosas del mapeo y las que la auditoría independiente detectó:

| IDs | De | A | Motivo |
| :-- | :-- | :-- | :-- |
| RF-038 | Pedidos | Existencias (Etapa 1, alta) | Es doble compromiso de la unidad: reserva |
| RF-056 | Existencias | Pedidos (Etapa 2, media) | Reasignar el pedido es ciclo del pedido |
| RF-064 | Pedidos | Oferta comercial (Etapa 1, alta) | Precio vigente; portal público de la Etapa 1 |
| RF-065, RF-066 | Pedidos | Existencias (Etapa 1, alta) | Disponibilidad; portal público de la Etapa 1 |
| RF-069, RF-070 | Pedidos | Cartera de crédito (Etapa 2, media) | Estado de cuenta y documentos son datos de la filial emisora y pasan por el control de cruces |
| RF-101 | Ventas | Existencias (Etapa 1, alta) | Consulta de disponibilidad |
| RF-138 | Abastecimiento | Existencias (Etapa 1, alta) | Clasificar la merma de un ajuste, igual que RF-139 a RF-141 |
| RF-142, 143, 147, 148 | Existencias | Oferta comercial (Etapa 1, alta) | Atributos del maestro de artículos y publicación |
| RF-146 | Existencias | Abastecimiento (Etapa 2, media) | Ajuste de la propuesta de reposición |
| RF-180 | Base tecnológica | Pedidos (Etapa 2, media) | Límite de unidades por cliente es parámetro del pedido; su aplicación en el primer evento anual se confirma en arquitectura y riesgos |
| RF-181 | Base tecnológica | Ventas (Etapa 1, alta) | Medios de pago |
| RF-210 | Originación | Evidencia financiera (Etapa 1, alta) | Recuperar antecedentes del crédito |
| RF-221 | Cartera | Originación (Etapa 1, alta) | Determinar el cupo, igual que RF-218 a RF-220 |
| RNF-46 | Base tecnológica | Clientes Retail (Etapa 2) | EXC-15 |

Se confirman sin cambio: RF-035 a RF-037, 039 a 042 y 044 (existencias), RF-085 y RF-094 (ventas), RF-089 a RF-093 y RF-219 (originación), RF-170 (control de cruces), RF-177, 178, 184, 185 y 186 (base tecnológica). RF-188 sube a prioridad alta (sostiene la restricción 7).

**Etapa de los RNF.** Cada RNF toma la etapa del servicio que mide. Diez pasan a la Etapa 2: RNF-04, 05, 17, 64 y 65 (pedidos), RNF-02, 55, 66 y 67 (marketplace) y RNF-69 (posventa), más RNF-46. Quedan 61 en la Etapa 1 y 11 en la Etapa 2. La prioridad sigue alta para todo RNF.

**Ámbito de los RNF** (retail, filial emisora o ambos): se corrigieron 14 filas que la heurística por palabras clave había clasificado mal (RNF-03, 11, 14, 20, 31, 40, 41, 46, 47, 52, 54, 56, 64 y 70). Sigue siendo una propuesta que se confirma al llenar el Formulario T-12.

## Campos que el Caso 17.1 pide

- Actor, precondición y resultado esperado: se cubren con la estructura canónica del enunciado y con el criterio de prueba de la subsección 3.2.5. No se agregan columnas. La auditoría lo señala como cumplimiento parcial (el Anexo B no tiene columna de origen en el Caso distinta de la RN). Queda como mejora del Excel.
- Ámbito retail, filial emisora o ambos: se marca en el Anexo B.

## Autonomía sin enlace: valor único de 24 horas

La revisión del Informe 1 pidió comprometer una sola autonomía. Se fija 24 horas (subsecciones 3.1 y 3.2.3, art. 16.4 de las Bases Administrativas y RT-03.10, «24 horas o el mayor que fije el caso»; el Caso fija mínimos de 8 horas en tienda y 4 horas en el centro de distribución, que quedan por debajo y no prevalecen). Se unifican en el Anexo B: RNF-24 (de 8 a 24), RNF-25 (centro de distribución, de 4 a 24, con nota de validación con el cliente), RNF-26 (30 minutos tras 24 horas) y RNF-28 (se retira la referencia al mínimo de 8 horas). RN-46 conserva su texto del Caso, con una nota en el Anexo C.

## Otras correcciones por la auditoría

- Tabla 3.5 de la 3.2.4: el historial del precio publicado es de tres años (RNF-44, RNF-58), no cinco.
- La 3.2.4 dice ahora que todo RNF tiene «umbral o criterio de aceptación verificable» (siete RNF tienen criterio documental, no numérico) y que cada requerimiento remite a su regla de negocio «cuando existe».
- Las cinco reglas citadas como «propuesta» (RN-07, 42, 43, 44 y 45) colisionaban con reglas definidas del registro. Se renombraron RN-P01 a RN-P05 y se describen en el Anexo C.
- Anexo C: se retiró el marcador «insertar ventana de tiempo aquí» de RN-02 y se reescribió el criterio de RN-04. RN-39 y RN-53 conservan origen y criterio vacíos (pendiente).

## Pendientes declarados (no resueltos por suposición)

1. Abastecimiento (3), comisiones (3) y cartera de crédito (6) tienen pocos requerimientos funcionales.
2. Huecos de contenido que la auditoría detectó y que no se inventaron: imputación de pagos (RN-42 sin requerimiento), derecho de retracto (Caso 16.1 n.º 22), gastos de cobranza, disponibilidad publicada en 30 s o menos (RT-05.29), hora de corte de las 07:00, exactitud de inventario diaria y enlace de respaldo en 14 tiendas y Coyhaique (RT-03.24). Reglas sin requerimiento: RN-43 a RN-45 (ahora RN-P03 a RN-P05 tienen requerimientos), RN-56 y RN-59 a RN-61.
3. RNF-05 conserva «POR DEFINIR (propuesta: 30 s)» frente al «tiempo real» del Caso.
4. Resolución de SUP-08 y SUP-09 (criterio S3-03 de la rúbrica): afecta a RF-023, RF-028 y RNF-19.
5. El Excel tiene referencias obsoletas: RF-160 y RF-161 citan «RF-058» (hoy RF-158 y RF-159), RF-183 cita «RF-026.1» (hoy RF-177 y RF-178), RNF-22 y RNF-23 citan «NFR-06.x» (hoy RNF-16 a RNF-21).
6. El capítulo 2 (sd-02, Tabla 2.6, línea 506) dice «≥ 8 h en tienda» y lista RNF-61 a RNF-63 como RNF. Describe lo que exige el cliente; conviene aclarar allí que la propuesta compromete 24 horas.
7. Requisitos de transición (migración de datos, capacitación, marcha blanca; FEP02 · 18): hoy aparecen como OP y en el plan de trabajo. Verificar que ningún RF de transición quede huérfano.
8. Los 16 supuestos por umbrales ausentes y los umbrales propuestos por el proponente se validan con el cliente al inicio del proyecto.
9. Columnas del Caso 17.1 (precondición, resultado esperado y origen en el Caso por requerimiento) y matriz de trazabilidad completa: viven en el Formulario T-12.

## Ajustes tras los agentes sobre la 3.2.4 (2026-10-08)

- **El período de consultas ya cerró.** El art. 43 de las Bases lo limita al 20-08 al 01-09-2026 (Formulario T-20) y el art. 5.4 dice que lo no planteado ahí se asume aceptado al presentar la oferta. La planilla de consultas ya se entregó (`CONSULTAS_ONLYSIMPLESOLUTIONS_20260901.xlsx`). Por eso donde decía «se consultará al mandante» o «se validan en el período de consultas» ahora dice «se validan con el cliente al inicio del proyecto, antes de fijar la línea base» (3.2.3, 3.2.4, Anexos A, B y C, Excel v3.1 y este registro).
- **Correspondencia con los requisitos transversales (RT).** No se agrega una columna «RT origen» al Anexo B ni al Excel. Esa correspondencia es el trabajo del Formulario T-12. La 3.2.4 dice que los requisitos de las Bases Técnicas Transversales se responden uno a uno en el T-12.
- **Método de verificación.** La 3.2.4 acota la afirmación: cada RNF tiene umbral y método, los RF se verifican con los criterios de aceptación de la 3.2.5 y las OP con la revisión del entregable.
- **Regla 4 de atomicidad.** Se reescribe (no se divide) el enunciado que no sigue la estructura canónica. Reglas 1, 2, 3 y 5 dividen.
- **Comité Ejecutivo.** Pasa a «del contrato» (art. 71: asistencia obligatoria para ambas partes).
- **Tabla 3.5.** Lenguaje claro y cifras del catálogo: RNF-06 (8 s), RNF-19 (5 min), RNF-44 (3 años), RNF-21 (2 s), RNF-42, 43 y 57 (plazo del crédito más 6 años y recuperación a 10 años) y RNF-22 (104.000 pedidos en 3 días).
- **Pendientes que se mantienen.** Los siete productos del Caso 17.1 que no viven en esta subsección (mapa de integraciones y registro de vacíos y consultas), y que el sd-02 diga «Tabla 2.1» y «Tabla 2.6» para el mismo catálogo.

## Cambios que el equipo debe trasladar al Excel oficial

- Eliminar RF-027. Reclasificar RNF-61, RNF-62 y RNF-63 (a criterios de aceptación).
- Reasignar los requerimientos de la tabla de reasignaciones. Actualizar RNF-24, RNF-25, RNF-26 y RNF-28 a 24 horas.
- Agregar RF-227 a RF-231 (servicio de clientes Retail) y las reglas RN-P01 a RN-P05.
- Agregar columnas de servicio, etapa, prioridad y ámbito (hoy solo están en el Anexo B).
- Corregir la hoja `0_Lectura` (totales) y las referencias obsoletas del punto 5.
- Completar el campo «Decisión del equipo» de la hoja 7 con lo anterior.
