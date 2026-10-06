# Entregables del alcance (borrador)

Documento de trabajo. No es entregable.

Fundamento metodológico: PMBOK 6.ª edición, proceso "Definir el alcance" (salida: enunciado del alcance, con entregables y criterios de aceptación) y "Crear la EDT" (descomposición orientada a entregables, regla del 100 %, diccionario). Apoyo de clase: FEP02, diapositivas 37, 38, 52, 55, 56 y 57.

Fuentes de contenido: `descripcion_alcance_producto.md` (producto, servicios, sistemas) y `Análisis de actores, alcance y arquitectura de servicios.md`. Documentación contractual mínima: Bases Administrativas (documentación como entregable contractual, Art. 18). Valores numéricos: solo los ya documentados en el sd-02 (Tabla 2.2), marcados como tales; el resto queda como `[umbral por definir]`.

## Reglas aplicadas

1. **Definición (FEP02·38).** Entregable es un producto, resultado o capacidad única y verificable. Cada uno lleva su criterio de aceptación; sin criterio no está definido.
2. **Criterio bien escrito (FEP02·38).** Hecho observable, medible y con umbral. Un criterio sin umbral no se puede recibir ni rechazar.
3. **Orientación a entregables (FEP02·EDT).** El primer nivel de la EDT son los entregables, no las fases ni las disciplinas.
4. **Regla del 100 % (FEP02·52).** Los componentes de cada nivel suman todo el trabajo del superior, sin faltante ni duplicado.
5. **Paquete de trabajo (FEP02·56-57).** Cada entregable de último nivel tiene código, descripción, criterio, responsable, hitos, esfuerzo, costo, recursos, supuestos y referencias. Aquí se completan código, descripción, criterio y referencias; el resto lo aporta el plan de trabajo.
6. **Validar vs controlar (FEP02).** Controlar la calidad lo hace el equipo (el entregable es correcto); validar el alcance lo hace el cliente (el entregable es aceptado y firmado).
7. **No es cronograma (FEP02·53).** La lista no ordena en el tiempo. La etapa se asigna aparte.

Convención de código: `1.x` entregables de producto, `2.x` de gestión del proyecto, `3.x` de transición y cierre. Es provisoria hasta alinearla con la EDT del sd-07.

---

## 1. Entregables de producto

| Cód. | Entregable | Descripción | Trazabilidad | Criterio de aceptación | Etapa |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1.1 | Servicio R-01 Catálogo, precios y promociones | Maestro comercial, reglas de precio, publicación por canal e historial; incluye la función nueva de precios y promociones | A1, A2, C2 | Discrepancia entre precio exhibido y cobrado ≤ 3 % en muestra auditada (sd-02); historial recuperable por canal y fecha | Por asignar |
| 1.2 | Servicio R-02 Abastecimiento y reposición | Planificación y coordinación de órdenes, transferencias y reposición | A3 | Órdenes y transferencias coordinadas con WMS y ERP/DTE sin intervención manual `[umbral por definir]` | Por asignar |
| 1.3 | Servicio R-03 Inventario, reservas y disponibilidad | Existencias por nodo, reservas, disponible para vender, margen de confianza | A4, A11 | Discrepancia en conteo cíclico < 2 % (sd-02); cancelaciones por falta de existencia < 0,3 % (sd-02) | Por asignar |
| 1.4 | Servicio R-04 Pedidos y cumplimiento omnicanal | Ciclo único del pedido, promesa de entrega, selección de nodo | A6, A7, A11 | Pedidos entregados en la fecha ofrecida ≥ 97 % (sd-02); estado único consultable desde todos los puntos de contacto | Por asignar |
| 1.5 | Servicio R-05 Registro y conciliación de ventas | Registro del hecho de venta, reversas y conciliación, incluidas ventas registradas sin conexión | A5, C2 | 100 % de ventas del POS conciliadas, incluidas las de desconexión `[umbral de diferencia por definir]` | Por asignar |
| 1.6 | Servicio R-06 Atribución de ventas y comisiones | Atribución multicanal y base de comisión | A5, A7 | Base de comisión entregada al sistema de remuneraciones con atribución auditable `[umbral por definir]` | Por asignar |
| 1.7 | Servicio R-07 Integración y gobierno de marketplace | Integración con la plataforma vigente, reglas de gobierno y medición de vendedores | A8 | Estados comprensibles para vendedor y Ancoa; medición de nivel de servicio por vendedor `[umbral por definir]` | Por asignar |
| 1.8 | Servicio R-08 Posventa, garantías y devoluciones | Casos, recepción, inspección, resolución y reintegro | A9 | Reingreso a inventario con aptitud registrada; garantía atendida sin derivar al fabricante como condición `[umbral por definir]` | Por asignar |
| 1.9 | Servicio R-09 Clientes y fidelización Retail | Identificador Retail, puntos, segmentos y campañas | A10, C1 | Cero atributos del Emisor en perfiles comerciales, verificado en revisión de segregación | Por asignar |
| 1.10 | Servicio F-01 Originación y autorización de crédito | Evaluación, originación y autorización con condiciones precontractuales | B1 | Evaluación en punto de venta < 10 s (sd-02, por unificar con 8 s de las Bases); versión precontractual registrada en cada solicitud | Por asignar |
| 1.11 | Servicio F-02 Cartera, cobranza y repactaciones | Cartera viva, cobranza y repactación | B2, B3 | Cada repactación consulta evidencia en F-03 antes de confirmarse | Por asignar |
| 1.12 | Servicio F-03 Consentimiento y evidencia financiera | Custodia y recuperación de consentimientos y versiones informadas | B1, B3, C2 | 0 repactaciones sin evidencia recuperable (sd-02); retención de grabaciones y expediente por plazo del crédito + 6 años (sd-02) | Por asignar |
| 1.13 | Servicio X-01 Autorización y auditoría de cruces | Autorización de cruces Retail–Emisor con dato mínimo y registro | C1, C2 | 100 % de los cruces con finalidad, autorización y registro; 0 consultas directas a bases del otro negocio | Por asignar |
| 1.14 | Plataforma de coordinación e integración | Mecanismos que mantienen coherentes a los sistemas con reglas explícitas de acuerdo y sin punto único de falla; incluye puerta de entrada, identidad, observabilidad | C3 | Reglas de acuerdo documentadas por tipo de dato; prueba de falla de un componente sin pérdida de coherencia `[umbral por definir]` | Por asignar |
| 1.15 | Plataforma híbrida | Componentes en nube pública y locales (tiendas, centros de distribución) | C3 | Inventario de componentes con emplazamiento justificado; operación verificada en ambos entornos | Por asignar |
| 1.16 | POS con operación offline | POS adquirido o desarrollado, con operación sin conexión demostrada | A5, F-01 | Operación offline demostrada en prueba; ventas sin conexión conciliadas por R-05; sin originación de crédito nuevo offline | Por asignar. Entregable formal pendiente |
| 1.17 | Reemplazo de la plataforma financiera de 2011 | Migración por olas de la cartera hacia F-01/F-02/F-03 y retiro del sistema anterior | B1, B2, B3 | Cartera migrada íntegra con cuadre de totales sin diferencias (patrón FEP02·38); retiro antes del fin de soporte `[fecha por verificar]` | Por asignar |
| 1.18 | Integraciones con sistemas que se conservan | Conectores con ERP/DTE, marketplace y WMS principal | C3 | Intercambio operando por contrato publicado; ERP/DTE sigue como único emisor tributario | Por asignar |
| 1.19 | Reemplazo del sistema central de retail (condicional) | Reemplazo por etapas si el escenario lo exige | A1 a A4 | Aplica solo con brecha documentada y transición viable `[criterios por definir]` | Condicionado |
| 1.20 | Decisiones condicionales: comercio electrónico, fidelización, WMS Concepción | Informe de pruebas y decisión de mantener, integrar o reemplazar | A6, A10, A3 | Informe de resultados contra las pruebas definidas `[umbrales por definir]` y decisión aprobada | Condicionado |

Pendiente de verificación: la novena plataforma no tiene entregable hasta identificarla.

---

## 2. Entregables de gestión del proyecto (PMBOK 6)

Corresponden a las salidas de los grupos de procesos de Inicio, Planificación, Ejecución, Monitoreo y control, y Cierre.

| Cód. | Entregable | Grupo de procesos / PMBOK 6 | Criterio de aceptación |
| :-- | :-- | :-- | :-- |
| 2.1 | Acta de constitución del proyecto | Inicio | Firmada por el patrocinador; objetivos, interesados clave y restricciones iniciales |
| 2.2 | Registro de interesados y estrategia de involucramiento | Inicio | Cobertura de los grupos identificados en sd-02 §2.4; estrategia por grupo |
| 2.3 | Plan para la dirección del proyecto con planes subsidiarios (alcance, requisitos, cronograma, costos, calidad, recursos, comunicaciones, riesgos, adquisiciones, interesados, cambios, configuración) | Planificación | Aprobado formalmente; cada plan con responsable y método de control |
| 2.4 | Enunciado del alcance del proyecto | Planificación (Definir el alcance) | Seis contenidos presentes: alcance del producto, entregables, criterios de aceptación, exclusiones, supuestos, restricciones; aprobado |
| 2.5 | Documentación de requisitos y matriz de trazabilidad | Planificación (Recopilar requisitos) | Cada requisito con origen, prioridad y vínculo a diseño, prueba y entregable |
| 2.6 | EDT y diccionario de la EDT | Planificación (Crear la EDT) | Regla del 100 % verificada; paquetes con responsable único y criterio de aceptación; aprobada por el patrocinador |
| 2.7 | Línea base del alcance (enunciado + EDT + diccionario) | Planificación | Versionada y aprobada; base de comparación de cambios |
| 2.8 | Cronograma e hitos (línea base) | Planificación | Alineado con el cronograma contractual obligatorio; hitos de pago identificados |
| 2.9 | Línea base de costos y presupuesto | Planificación | Consistente con la oferta económica `[detalle por definir]` |
| 2.10 | Registro de riesgos y plan de respuesta | Planificación | Riesgos con probabilidad, impacto, responsable y respuesta |
| 2.11 | Plan de calidad y métricas | Planificación | Métricas con umbral por entregable |
| 2.12 | Informes de desempeño del trabajo | Monitoreo y control | Entregados con la periodicidad del plan de comunicaciones |
| 2.13 | Registro y solicitudes de cambio aprobadas | Monitoreo y control (Control integrado de cambios) | Todo cambio al catálogo de trece servicios con aprobación registrada |
| 2.14 | Entregables validados (actas de aceptación) | Monitoreo y control (Validar el alcance) | Acta firmada por la Contraparte Técnica para cada entregable |
| 2.15 | Registro de lecciones aprendidas | Ejecución, Monitoreo y control, Cierre | Actualizado al cierre de cada etapa |
| 2.16 | Informe y acta de cierre | Cierre | Entregables recibidos y pendientes listados; liquidación y reversibilidad según contrato |

---

## 3. Entregables de documentación técnica, transición y operación

| Cód. | Entregable | Criterio de aceptación |
| :-- | :-- | :-- |
| 3.1 | Documento de arquitectura (lógica, física, datos, integración, seguridad) y registro de decisiones | Cada decisión con alternativas y criterio; diagramas propios de la solución |
| 3.2 | Estándares de codificación, documentación de interfaces, diccionario de datos e inventario de componentes | Interfaces documentadas para cada servicio; diccionario con propietario por dominio |
| 3.3 | Plan y casos de prueba, evidencia y informes de carga, resiliencia y seguridad | Evidencia de ejecución archivada para cada servicio |
| 3.4 | Política de seguridad, modelado de amenazas, matriz de controles y plan de remediación | Controles trazables a entregables |
| 3.5 | Manual de operación, libros de operación, guías de resolución, matriz de escalamiento, plan de continuidad y recuperación | Revisados por operación antes de cada paso a producción |
| 3.6 | Plan de migración y convivencia por etapa | Cubre sistemas conservados, reemplazados y condicionados |
| 3.7 | Plan de capacitación y certificación del personal del cliente | Personal certificado conforme al plan, condición de cierre de marcha blanca |
| 3.8 | Manuales por perfil de usuario y guía de cambios | Un manual por actor principal con interacción directa |
| 3.9 | Protocolo de aceptación de hito y de producto final | Entregables, criterios, evidencia, plazos y procedimiento de observaciones definidos |
| 3.10 | Informes de cierre de marcha blanca | Sin incidentes críticos ni altos abiertos, volumen comprometido alcanzado, conciliación sin diferencias no explicadas |
| 3.11 | Plan de retiro de la plataforma de crédito actual | Fecha y condiciones de apagado `[por verificar]` |

---

## Verificación de la regla del 100 %

Los tres bloques cubren el producto (1.x), la gestión (2.x) y la transición y documentación (3.x). Cada servicio del catálogo de trece tiene un entregable propio (1.1 a 1.13). Quedan por revisar al construir la EDT:

- Que 1.14 a 1.18 no dupliquen trabajo entre sí (plataforma, integraciones, híbrido).
- Que 3.1 a 3.5 no dupliquen 2.3 y 2.11.

## Pendientes

1. Etapa 1 o Etapa 2 de cada entregable (decisión servicio por servicio, abierta en `plan_3.2.md`).
2. Hito y porcentaje de pago (Formulario E-25) de cada entregable.
3. Umbrales marcados `[umbral por definir]`.
4. Unificar 10 s (sd-02) con 8 s (Bases) en 1.10.
5. Entregable formal del POS (1.16) y su código.
6. Criterios del reemplazo del sistema central (1.19) y de las decisiones condicionales (1.20).
7. Responsable por paquete y esfuerzo, que salen del plan de trabajo (sd-07).
8. Alinear la numeración con la EDT del sd-07.
