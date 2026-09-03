# Innovaciones obligatorias — Fichas (Art. 28–29)

**Licitación N° TFEP-01/2026 — Caso 09: Cadena Multitienda (Multitiendas Ancoa S.A.)**
**Proponente:** Only Simple Solutions
**Fecha:** Septiembre 2026
**Estado:** Borrador para revisión interna. Cada ficha sigue los **7 elementos del Art. 29** para el Formulario T-19: (1) problema, (2) tecnología/práctica/modelo, (3) madurez, (4) diseño de incorporación, (5) impacto económico, (6) indicador de verificación, (7) riesgo de adopción.

> **Criterio de pertinencia (Cap. 19 del caso):** las cinco innovaciones deben ser pertinentes al comercio minorista y al crédito de casa comercial, y **no** un catálogo de tecnologías de moda. Por eso cada una nace de un dolor concreto de un módulo del negocio (según `Bases/DivisionNegocios.md`) y se traza con la arquitectura, la EDT y el flujo de caja.
>
> Fuentes citadas en formato APA para las innovaciones de base tecnológica. Ver lista completa en `productos/seccion3_investigacion.md`.

---

## INN-1 — Tipo Producto/Servicio: Crédito en segundos con scoring alternativo y open finance consentido

**1. Problema u oportunidad concreta del caso (con dato/evidencia).**
La evaluación de crédito en el punto de venta tarda **entre 40 segundos y 3 minutos**, tiempo en el que la venta se pierde. El crédito representa **38% de las ventas de la tienda**, así que esa lentitud erosiona el negocio principal. Además, hay clientes —jóvenes e independientes con ingresos estables pero sin historial— que hoy quedan fuera del crédito.

**2. Tecnología/práctica/modelo que la sustenta (descripción técnica, no categoría).**
Originación de crédito en segundos mediante un **motor de scoring alternativo** que complementa el informe tradicional (DICOM/Equifax) con historial de pago de servicios, comportamiento transaccional y facturación electrónica (SII) como proxy de ingresos. En el futuro incorpora la **interoperabilidad de datos financieros (open finance)** con consentimiento del usuario (Ley FinTech 21.521), siempre sobre la **separación de datos retail–financiero** que exige la línea roja del caso (dominio financiero separado, RT-11.10, RT-16.09).

**3. Nivel de madurez de la tecnología.**
TRL 8–9 en aplicación comercial en Chile: fintech locales operan scoring alternativo desde 2026, y la CMF actualizó en jun-2026 las reglas del crédito digital no bancario (capital, sandbox regulatorio de 24 meses, divulgación de CAE, open finance hasta 2027). Fuentes: CréditoLab (2026); CMF Chile (2026).

**4. Diseño de la incorporación (arquitectura + EDT + mes).**
Se inserta en el **Módulo 4 (Negocio Financiero)**, dentro del dominio de datos financiero separado. Lo ejecuta el paquete del módulo financiero de la EDT; se materializa en el **mes 14** (Etapa 1, antes de producción en el mes 16), con el scoring desplegado en los puntos de venta on-premise y en la nube (modelo híbrido, Art. 16).

**5. Impacto económico estimado.**
Inversión acotada al desarrollo del motor de scoring y su integración. Efecto: reducción del tiempo de evaluación de minutos a segundos. Beneficio: recupero de la venta por crédito (38% del giro) y captura de nuevos segmentos; se refleja como aumento de ingresos en el flujo de caja.

**6. Indicador de verificación del beneficio.**
- Línea base: evaluación en hasta 180 segundos; aprobación limitada a clientes con historial.
- Meta: tiempo medio de evaluación < 10 segundos; % de ventas con tarjeta/línea aprobada al alza.
- Momento: medir a los 6 y 12 meses de producción (meses 22 y 28).

**7. Riesgo de adopción y mitigación.**
- Riesgo regulatorio/transparencia (sesgo en algoritmos, consentimiento). Mitigación: trazabilidad de la decisión, consentimiento informado explícito, revisión de sesgos y cumplimiento CAE.
- Riesgo de crédito (mayor cartera). Mitigación: scoring calibrado, límites por perfil y monitoreo de cartera bajo gobernanza del regulador.

---

## INN-2 — Tipo Proceso: SFS + BOPIS con orquestación que no vacíe el piso de venta

**1. Problema u oportunidad concreta del caso.**
**17% de los pedidos online vacían el piso de venta** de la tienda física, degradando la rentabilidad y la experiencia del canal que aún concentra la mayor parte del negocio. Además, hubo **2.840 pedidos cancelados en 3 días** por promesas de entrega insostenibles.

**2. Tecnología/práctica/modelo que la sustenta.**
Un **Order Management System (OMS)** con **orquestación multicriterio de cumplimiento**: elige el punto de despacho (CD o tienda) ponderando **costo total, disponibilidad real y efecto sobre la sala de venta**, con umbrales de stock de seguridad por tienda. Incluye retiro en tienda (BOPIS) y despacho desde tienda (SFS), con preparación ágil en bodega.

**3. Nivel de madurez.**
TRL 9 en comercio: SFS/BOPIS son estándar probado; marcas con OMS reportan ~25% más de venta online al enviar desde tiendas (OneStock, 2026; Solution Logistics, 2025). Lo novedoso para Ancoa es la **restricción de no vaciar el piso**, que la hace propia de este caso.

**4. Diseño de la incorporación.**
Se inserta en el **Módulo 3 (Cumplimiento de Pedidos)**. Lo ejecuta el paquete OMS de la EDT; se materializa en **mes 15** (Etapa 1) con piloto en 2 ciudades/tiendas y escalado por oleadas en la Etapa 2.

**5. Impacto económico estimado.**
Inversión en el OMS y su integración con caja, canal digital y ERP. Efecto: menos quiebres, menos transporte y mayor rotación de stock de tienda. Beneficio: reducción de cancelaciones y de venta perdida; se refleja como menor costo de cumplimiento y mayor margen.

**6. Indicador de verificación.**
- Línea base: 2.840 cancelaciones/3 días; 17% de pedidos impactan el piso.
- Meta: tasa de cancelación < 2%; fill rate > 95%; OTIF ≥ objetivo; 0% de pedidos que vacían el piso.
- Momento: a los 6 y 12 meses de producción.

**7. Riesgo de adopción.**
- Riesgo de operación (tiendas sin preparación para cumplimiento). Mitigación: formación, zona de preparación en bodega y piloto controlado.
- Riesgo de inventario desincronizado. Mitigación: inventario unificado del Módulo 1 como prerrequisito.

---

## INN-3 — Tipo Tecnológica/Arquitectura: Capa de inventario unificado en tiempo real + ESL + endless aisle

**1. Problema u oportunidad concreta del caso.**
El **12,4% de discrepancia en el conteo cíclico** sobre 9 plataformas de 6 proveedores y 14 interfaces punto a punto hace que las **4 promesas diarias** (el producto existe, el precio está bien exhibido, la entrega llega, el crédito está informado) descansen sobre registros imprecisos. El error conceptual sería abordar esto como reemplazo del ERP: es un tejido de plataformas a articular.

**2. Tecnología/práctica/modelo que la sustenta.**
**Capa de visibilidad/inventario unificado** (middleware y APIs) que integra las 9 plataformas **sin reemplazarlas**, publicando el ATP real en tiempo real por nodo y categoría; **etiquetas electrónicas de precio (ESL)** para la promesa de precio; y **endless aisle** para vender el catálogo completo (458.000 SKUs) desde tienda consultando el stock de la red. Se apoya en el modelo **híbrido nube + on-premise** (Art. 16, RT-03): la capa de datos en nube elástica y los componentes de tienda on-premise.

**3. Nivel de madurez.**
ESL: TRL 9 (US$8–40 por unidad según tecnología/segmento). Inventario unificado/ATP y endless aisle: TRL 9 en comercio (IBM, 2025; Mecalux, 2023; Solution Logistics, 2025).

**4. Diseño de la incorporación.**
Se inserta en el **Módulo 1 (Inventario y Disponibilidad)** y en los **Módulos 2 y 6** (ESL, analítica). Lo ejecuta el paquete de integración/middleware de la EDT; se materializa en **meses 8–13** (Etapa 1), con la capa ATP antes de producción en el mes 16 y ESL desplegado por oleadas.

**5. Impacto económico estimado.**
Inversión en middleware, integración y ESL (priorizado a alto tráfico). Efecto: corrección del 12,4% de discrepancia y consistencia de precio. Beneficio: menos quiebres y sobreventa, menos merma y cumplimiento de la promesa; se refleja en menor costo operacional.

**6. Indicador de verificación.**
- Línea base: 12,4% de discrepancia.
- Meta: exactitud de inventario > 98%; precio exhibido = precio cobrado en 100% de las tiendas con ESL.
- Momento: a los 6 y 12 meses de producción.

**7. Riesgo de adopción.**
- Riesgo de integración (9 plataformas heterogéneas). Mitigación: capa de middleware gradual, levantamiento del mapa de interfaces y piloto en tienda/categoría.
- Riesgo de inversión en hardware (ESL). Mitigación: despliegue priorizado y ROI por categoría.

---

## INN-4 — Tipo Modelo de Negocio/Contratación: Plataforma de datos de cruce controlado habilitada por la nube y el cumplimiento

**1. Problema u oportunidad concreta del caso.**
Ancoa genera datos comerciales valiosos (transacciones de tienda y programa de lealtad) que hoy no se aprovechan, precisamente porque **la frontera entre el retail y la filial fiscalizada no está definida**. La contralora fue explícita: hay que definir qué puede cruzar, con qué base y con qué control **antes** de construir cualquier vista unificada (decisión de diseño N° 4; RT-16.09). Definida esa frontera con control técnico y auditable, el dato del retail se vuelve un servicio legal, seguro y explotable.

**2. Tecnología/práctica/modelo que la sustenta (descripción técnica, no categoría).**
Construir una **plataforma de datos de cruce controlado y auditable** que separa físicamente los dos dominios (retail y financiero) y solo permite pasar entre ellos lo autorizado, con registro de **qué cruzó, con qué finalidad, con qué base y quién lo autorizó** (RT-16.09). Se apoya en la **nube** (Art. 16, RT-03) para el data lake retail de la compañía, con tenant aislado del giro financiero, y en los controles de ISO 27001/27017/27018 y la Ley de Protección de Datos Personales (Ley 21.719, plena vigencia 1-dic-2026). El modelo de negocio NO es un "retail media" libre sobre datos regulados: es ofrecer **servicios sobre datos comerciales del retail** (segmentación, analítica, insights a marcas y proveedores, programas de lealtad) que viven en el dominio retail, anonimizados o agregados, sin tocar jamás el comportamiento de pago ni la cartera del negocio fiscalizado.

**3. Nivel de madurez.**
TRL 5–6 (novedoso como diseño de cumplimiento para un emisor regulado). Las prácticas subyacentes son maduras —data lakes en nube (TRL 9), gestión de consentimiento y registro de tratamientos (Ley 21.719)—, pero su valor diferencial está en **hacer legal y auditable el cruce entre dos regímenes**, que es precisamente lo que hoy no existe en Ancoa. El retail media en sí es maduro en Chile (REM Media, 2026), pero aquí se le subordina a la frontera regulada: **primero la gobernanza, después la monetización**.

**4. Diseño de la incorporación.**
Se inserta en el **Módulo 6 (Datos, Analítica y Gobernanza)** y en el **Módulo 2** (lealtad/señalización). Lo ejecuta el paquete de datos/gobernanza de la EDT; la **separación técnica y el control de cruces** se materializan en la **Etapa 1 (mes 12, antes de producción)**, porque son prerrequisito de cualquier explotación de datos y del plan de remediación 2029. Los servicios comerciales sobre el dominio retail se activan en la **Etapa 2 (mes 20)** y operan en la fase de Operación.

**5. Impacto económico estimado.**
Inversión en la plataforma de datos, gobernanza y controles. Efecto directo: cierra un requisito de la contralora y del plan de remediación (evita el riesgo de que la autoridad requiera evidencia de cruces que nadie guarda). Efecto indirecto: habilita una nueva línea de ingreso B2B de **margen alto** sobre datos comerciales del retail, reflejada como ingreso incremental en el flujo de caja de Operación. El mayor beneficio es de **riesgo** (protección del 10% de los ingresos financieros y de la licencia operativa), no solo de ingreso.

**6. Indicador de verificación.**
- Línea base: 0% de cruces registrados; frontera no definida.
- Meta: 100% de los cruces retail–financiero registrados y auditables (RT-16.09); 0 cruces no autorizados; N marcas/proveedores atendidos con datos del dominio retail y M$ de ingresos B2B anuales.
- Momento: la auditoría de cruces se verifica desde producción (mes 16 y en cada paso a producción); los ingresos B2B se miden semestral en Operación (meses 30, 42, 54).

**7. Riesgo de adopción.**
- Riesgo de gobernanza de datos (mezclar los dos ámbitos). Mitigación: tenant financiero aislado de red y de datos, control técnico de cruces con registro, anonimización/agregación del dominio retail y auditoría externa (RT-11, RT-16).
- Riesgo regulatorio (uso indebido del comportamiento de pago). Mitigación: la monetización usa **solo** datos del dominio retail; el comportamiento de pago y la cartera quedan fuera del alcance comercial y con tratamiento reforzado (RT-11.10).
- Riesgo comercial (baja adopción). Mitigación: arranque con los proveedores y la red de lealtad existentes, con medición de incrementalidad.

---

## INN-5 — Tipo UX/Sostenibilidad/Impacto Social: BORIS + experiencia omnicanal fluida + inclusión financiera

**1. Problema u oportunidad concreta del caso.**
La fricción entre canales (devoluciones costosas, cancelaciones, espera de crédito) degrada la experiencia; el caso lo resume en que "Doña Paula llama cinco veces y nadie sabe decirle qué pasó". La **inclusión financiera** de clientes sin historial es, además, un impacto social concreto y medible.

**2. Tecnología/práctica/modelo que la sustenta.**
**Devolución en tienda (BORIS)** para reembolsos ágiles y recupero de stock; **retiro y despacho desde tienda (BOPIS/SFS)** para flexibilidad; y una experiencia omnicanal fluida (precio e inventario consistente, estado único de pedido). Junto con la **inclusión financiera** que habilita el scoring alternativo de INN-1 (acceso a crédito a clientes sin historial bancario).

**3. Nivel de madurez.**
TRL 9 para BORIS/omnicanalidad (Solution Logistics, 2025; IBM, 2025). Inclusión financiera por scoring alternativo: TRL 8–9 en fintech chilenas (CréditoLab, 2026).

**4. Diseño de la incorporación.**
Se inserta en el **Módulo 3 (Cumplimiento de Pedidos)** y en el **Módulo 4 (Negocio Financiero)**. Lo ejecutan los paquetes de OMS y módulo financiero; BORIS se materializa en la **Etapa 2 (mes 20)**; la inclusión financiera acompaña a INN-1 desde el mes 14.

**5. Impacto económico estimado.**
Inversión mínima incremental (reutiliza OMS y motor de scoring). Efecto: reducción de devoluciones y cancelaciones y de venta abandonada, más captura de nuevos segmentos de crédito. Beneficio: retención de clientes y nuevo volumen; se refleja en menor costo de envío/devolución y mayores ventas.

**6. Indicador de verificación.**
- Línea base: 2.840 cancelaciones/3 días; devoluciones y abandono no medidos por segmento.
- Meta: reducción de cancelaciones < 2%; NPS/CSAT omnicanal ≥ objetivo; % de clientes nuevos con crédito aprobado (sin historial) ≥ X%.
- Momento: semestral en Operación.

**7. Riesgo de adopción.**
- Riesgo de experiencia (procesos de devolución no uniformes). Mitigación: formación y procedimiento único por tienda.
- Riesgo de impacto social mal comunicado (apariencia de "crédito fácil"). Mitigación: comunicación responsable, CAE clara y límites por perfil.

---

## Resumen de trazabilidad (arquitectura · EDT · flujo de caja)

| Innovación | Tipo (Art. 28) | Módulo(s) | EDT (paquete) | Mes de materialización | Efecto en flujo de caja |
| :--- | :--- | :--- | :--- | :--- | :--- |
| INN-1 | Producto/Servicio | M4 | Módulo financiero | 14 | ↑ ingresos crédito |
| INN-2 | Proceso | M3 | OMS | 15 (piloto), Etapa 2 | ↓ costo cumplimiento, ↑ margen |
| INN-3 | Tecnológica/Arquitectura | M1, M2, M6 | Integración/middleware | 8–13 (ATP), ESL oleadas | ↓ costo operacional |
| INN-4 | Modelo de Negocio | M6, M2 | Datos/gobernanza | 12 (frontera), 20 (servicios) | ↑ ingreso B2B; ↓ riesgo financiero |
| INN-5 | UX/Sostenibilidad/Impacto Social | M3, M4 | OMS + financiero | 14 / 20 | ↓ devoluciones, ↑ retención |

Las innovaciones 1 y 4 dependen de la **separación de datos retail–financiero** (línea roja) para su validez; INN-4 la convierte en su núcleo (primero la gobernanza, después el negocio), y todas son trazables a la arquitectura (dominios de datos separados), a la EDT (paquete de gobernanza) y al flujo de caja (beneficio o ahorro de riesgo).
