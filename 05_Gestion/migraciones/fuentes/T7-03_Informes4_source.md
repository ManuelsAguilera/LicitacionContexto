

# 						

    Subdocumento 3  
Propuesta solución \- Multitienda Ancoa S.A.

Septiembre 2026

# **ÍNDICE GENERAL** {#índice-general}

[ÍNDICE GENERAL	2](#índice-general)

[LISTA DE FIGURAS	5](#lista-de-figuras)

[LISTA DE TABLAS	6](#lista-de-tablas)

[LISTA DE ACRÓNIMOS	8](#lista-de-acrónimos)

[**INTRODUCCIÓN	9**](#heading=h.mg3bxw7zdcq5)

[3\. ESQUEMA DE SOLUCIÓN Y ALCANCE	1](#3.-introducción-y-alcance-de-la-solución)

[3.1. Descripción general de la solución propuesta y coherencia con el problema definido	1](#3.1.-resumen-ejecutivo-de-la-solución)

[3.2. Resolución de las decisiones pendientes declaradas por el CLIENTE	2](#3.2.-alcance)

[3.2.1. SUP-01: El origen y cálculo de la disponibilidad de inventario	3](#3.2.1.-sup-01:-el-origen-y-cálculo-de-la-disponibilidad-de-inventario)

[3.2.2. SUP-02: Estrategia de transición para el sistema central de 2009	3](#3.2.2.-sup-02:-estrategia-de-transición-para-el-sistema-central-de-2009)

[3.2.3. SUP-03 y SUP-04: Frontera de datos e Identidad Unificada del Cliente	4](#3.2.3.-sup-03-y-sup-04:-frontera-de-datos-e-identidad-unificada-del-cliente)

[3.2.4. SUP-07: Continuidad de la operatoria de crédito ante desconexión de sucursales	4](#3.2.4.-sup-07:-continuidad-de-la-operatoria-de-crédito-ante-desconexión-de-sucursales)

[3.2.5. SUP-25: Estrategia de migración de la cartera activa de crédito	5](#3.2.5.-sup-25:-estrategia-de-migración-de-la-cartera-activa-de-crédito)

[3.2.6. Resolución de las decisiones restantes	5](#3.2.6.-resolución-de-las-decisiones-restantes)

[3.2.6.1. La existencia física: cómo se cuenta, cómo se reserva y dónde se almacena	5](#3.2.6.1.-la-existencia-física:-cómo-se-cuenta,-cómo-se-reserva-y-dónde-se-almacena)

[3.2.6.2. El precio: consistencia omnicanal y evidencia fiscal	6](#3.2.6.2.-el-precio:-consistencia-omnicanal-y-evidencia-fiscal)

[3.2.6.3. El pedido: lógica de cobro, asignación y comisión	7](#3.2.6.3.-el-pedido:-lógica-de-cobro,-asignación-y-comisión)

[3.2.6.4. Postventa, Marketplace y Logística Inversa	7](#3.2.6.4.-postventa,-marketplace-y-logística-inversa)

[3.2.6.5. El crédito: acreditación del consentimiento	8](#3.2.6.5.-el-crédito:-acreditación-del-consentimiento)

[3.2.6.6. Identidad, Accesos y Seguridad Transaccional	8](#3.2.6.6.-identidad,-accesos-y-seguridad-transaccional)

[3.3. Módulos funcionales de la solución	9](#3.3.-módulos-funcionales-de-la-solución)

[3.3.1. Dominio Retail: Núcleo de inventario y disponibilidad	9](#heading=h.5h4fkjih8hbw)

[3.3.2. Dominio Retail: Precio y cumplimiento comercial	10](#heading=h.quzd40y2b103)

[3.3.3. Dominio Retail: Venta, pedido y cumplimiento	11](#heading=h.eh6i4lhhgb3)

[3.3.4. Dominio Retail: Postventa, marketplace y logística inversa	12](#heading=h.h5x1n830sca8)

[3.3.5. Dominio Financiero: Filial emisora fiscalizada	13](#heading=h.9aa954jnnavq)

[3.3.6. Capa transversal: Integración, identidad y resiliencia	15](#heading=h.mth4g3uwvb08)

[3.3.7. Cobertura y lectura del mapa modular	17](#heading=h.m1jo31apppvx)

[3.4. Diagrama conceptual de solución e interacción de actores	17](#3.4.-diagrama-conceptual-de-solución-e-interacción-de-actores)

[3.5. Objetivos del proyecto	17](#3.-objetivos-del-proyecto)

[3.5.1. Objetivo General	18](#3.5.1.-objetivo-general)

[3.5.2. Objetivos Específicos	18](#3.5.2.-objetivos-específicos)

[3.5.3. Responsabilidad sobre la adopción y los indicadores	19](#3.5.3.-responsabilidad-sobre-la-adopción-y-los-indicadores)

[3.6. Alcance de la Etapa 1 y de la Etapa 2, con criterio de asignación	20](#3.6.-alcance-de-la-etapa-1-y-de-la-etapa-2,-con-criterio-de-asignación)

[3.6.1. Criterios de asignación	20](#3.6.1.-criterios-de-asignación)

[3.6.2. La corrección al orden de urgencia declarado	20](#3.6.2.-la-corrección-al-orden-de-urgencia-declarado)

[3.6.3. Asignación de alcance por módulo (Regla del 100 %)	21](#heading=h.qwql5kdxylho)

[3.6.4. Colisiones de calendario declaradas	23](#3.6.4.-colisiones-de-calendario-declaradas)

[3.6.5. Fase de Operación	24](#3.6.5.-fase-de-operación)

[3.7. Exclusiones explícitas, supuestos y restricciones	24](#3.7.-exclusiones-explícitas,-supuestos-y-restricciones)

[3.7.1. Exclusiones explícitas	24](#3.7.1.-exclusiones-explícitas)

[3.7.2. Supuestos	25](#3.7.2.-supuestos)

[3.7.3. Restricciones	26](#3.7.3.-restricciones)

[3.8. Catálogo de requerimientos funcionales core	27](#3.8.-catálogo-de-requerimientos-funcionales-core)

[3.8.1. Gobernanza de datos y frontera regulatoria	27](#3.8.1.-gobernanza-de-datos-y-frontera-regulatoria)

[3.8.2. Disponibilidad e inventario	27](#3.8.2.-disponibilidad-e-inventario)

[3.8.3. Precio y evidencia fiscal	28](#3.8.3.-precio-y-evidencia-fiscal)

[3.8.4. Pedido, cumplimiento y comisión	28](#3.8.4.-pedido,-cumplimiento-y-comisión)

[3.8.5. Operación de tienda y contingencia	29](#3.8.5.-operación-de-tienda-y-contingencia)

[3.8.6. Post-venta, garantía legal y marketplace	30](#3.8.6.-post-venta,-garantía-legal-y-marketplace)

[3.8.7. Crédito, consentimiento y migración	30](#3.8.7.-crédito,-consentimiento-y-migración)

[3.8.8. Accesos, evento anual y ventanas de congelamiento	31](#3.8.8.-accesos,-evento-anual-y-ventanas-de-congelamiento)

[3.9. Catálogo de requerimientos no funcionales core	32](#3.9.-catálogo-de-requerimientos-no-funcionales-core)

[3.9.1. Desempeño y tiempo de respuesta	32](#3.9.1.-desempeño-y-tiempo-de-respuesta)

[3.9.2. Capacidad	33](#3.9.2.-capacidad)

[3.9.3. Seguridad y frontera de datos	33](#3.9.3.-seguridad-y-frontera-de-datos)

[3.9.4. Retención, trazabilidad y migración	34](#3.9.4.-retención,-trazabilidad-y-migración)

[3.9.5. Precisión sobre Continuidad y Métricas de Negocio	34](#3.9.5.-precisión-sobre-continuidad-y-métricas-de-negocio)

[3.10. Estrategia para obtener el apoyo de los grupos de interés clave	34](#3.10.-estrategia-para-obtener-el-apoyo-de-los-grupos-de-interés-clave)

[3.11. Criterios de aceptación del alcance comprometido	37](#3.11.-criterios-de-aceptación-del-alcance-comprometido)

[3.11.1. Nivel 1: aceptación por entregable	37](#3.11.1.-nivel-1:-aceptación-por-entregable)

[3.11.2. Nivel 2: aceptación de la marcha blanca	37](#3.11.2.-nivel-2:-aceptación-de-la-marcha-blanca)

[3.11.3. Nivel 3: aceptación por resultado de negocio	38](#3.11.3.-nivel-3:-aceptación-por-resultado-de-negocio)

[3.11.4. Criterios de aceptación de naturaleza cualitativa	40](#3.11.4.-criterios-de-aceptación-de-naturaleza-cualitativa)

[3.11.5. Reparto de responsabilidad y arbitraje del incumplimiento	40](#3.11.5.-reparto-de-responsabilidad-y-arbitraje-del-incumplimiento)

[REFERENCIAS	41](#referencias)

[DECLARACIÓN USO IA	42](#declaración-uso-ia)

[A. ANEXOS	43](#heading=h.1b1y44tpiiuj)

[A.1. Listado de Requerimientos Funcionales (RF)	43](#heading=h.32zfefi9jhjy)

[A.1.1. Listado de Requerimientos Funcionales: Ventas en Tienda	43](#heading=h.n5z3wz7nwf4f)

[A.1.2. Listado de Requerimientos Funcionales: Seguridad y Accesos	44](#heading=h.4oy67qgvtnm)

[A.1.3. Listado de Requerimientos Funcionales: Precios y Etiquetado	44](#heading=h.7xgfdfp0xdlc)

[A.1.4. Listado de Requerimientos Funcionales: Pedidos y Cumplimiento	45](#heading=h.u7oi40hxgr68)

[A.1.5. Listado de Requerimientos Funcionales: Operación de Tienda	48](#heading=h.ah3jist1v4wm)

[A.1.6. Listado de Requerimientos Funcionales: Marketplace	49](#heading=h.f9zoufcsgfd6)

[A.1.7. Listado de Requerimientos Funcionales: Inventario y Disponibilidad	50](#heading=h.pqin9lno2xw7)

[A.1.8. Listado de Requerimientos Funcionales: Gobernanza de Datos	52](#heading=h.1cskw9hbl1rk)

[A.1.9. Listado de Requerimientos Funcionales: Evento de Alta Concurrencia	53](#heading=h.sqv9b1t3mr1b)

[A.1.10. Listado de Requerimientos Funcionales: Devoluciones y Garantía Legal	54](#heading=h.7v7o1akg4kuu)

[A.1.11. Listado de Requerimientos Funcionales: Crédito y Cobranza	54](#heading=h.h2330mb4towv)

[A.2. Listado de Requerimientos No Funcionales (RNF)	56](#heading=h.bntsfod5zaxi)

[A.2.1. Listado de Requerimientos No Funcionales: Disponibilidad	56](#heading=h.ik9ufb72j0oe)

[A.2.2. Listado de Requerimientos No Funcionales: Desempeño	57](#heading=h.hsjoh3v9qhry)

[A.2.3. Listado de Requerimientos No Funcionales: Consistencia de datos	58](#heading=h.3g6jduj7titi)

[A.2.4. Listado de Requerimientos No Funcionales: Desempeño / Cumplimiento	58](#heading=h.r25bfnauteee)

[A.2.5. Listado de Requerimientos No Funcionales: Portabilidad / Migración	59](#heading=h.v5kri1rwkowg)

[A.2.6. Listado de Requerimientos No Funcionales: Seguridad / Arquitectura	59](#heading=h.ljswruxoknio)

[A.2.7. Listado de Requerimientos No Funcionales: Auditabilidad	60](#heading=h.i725bxft20e0)

[A.2.8. Listado de Requerimientos No Funcionales: Desempeño / Capacidad	60](#heading=h.hi7ccsgyf7fi)

[A.2.9. Listado de Requerimientos No Funcionales: Recuperabilidad	61](#heading=h.n76xguglgwas)

[A.2.10. Listado de Requerimientos No Funcionales: Seguridad	61](#heading=h.w3pdfryqixqi)

[A.2.11. Listado de Requerimientos No Funcionales: Seguridad / Cumplimiento	62](#heading=h.wzenwc9j04ag)

[A.2.12. Listado de Requerimientos No Funcionales: Cumplimiento	63](#heading=h.axyuturwc6cr)

[A.2.13. Listado de Requerimientos No Funcionales: Portabilidad / Escalabilidad	64](#heading=h.qr1s3iihkidx)

[A.2.14. Listado de Requerimientos No Funcionales: Usabilidad	64](#heading=h.72s2yq1nj437)

[A.2.15. Listado de Requerimientos No Funcionales: Usabilidad / Cumplimiento	65](#heading=h.rp7bmmyhu1ee)

[A.2.16. Listado de Requerimientos No Funcionales: Operabilidad	65](#heading=h.lxzdb7i4px0z)

[A.2.17. Listado de Requerimientos No Funcionales: Interoperabilidad	66](#heading=h.jyl4zw7oihpb)

[A.2.18. Listado de Requerimientos No Funcionales: Auditabilidad / Desempeño	67](#heading=h.oihjqhv3t8ra)

[A.2.19. Listado de Requerimientos No Funcionales: Usabilidad / Desempeño	67](#heading=h.7q87jmh14sq9)

[A.2.20. Listado de Requerimientos No Funcionales: Efectividad de negocio	67](#heading=h.iangps83re87)

[A.2.21. Listado de Requerimientos No Funcionales: Seguridad / DevSecOps	68](#heading=h.e7pn06mjqbl5)

[A.3. Listado de Obligaciones del Proponente (OP)	68](#heading=h.p6bgxn57fw8p)

[A.4. Matriz de cumplimiento y trazabilidad	69](#heading=h.zc9zhxm13vfz)

# **LISTA DE FIGURAS** {#lista-de-figuras}

[Figura 3.1: Diagrama conceptual de solución e interacción de actores.	17](#figura-3.1:-diagrama-conceptual-de-solución-e-interacción-de-actores.)

# **LISTA DE TABLAS** {#lista-de-tablas}

[Tabla 3.1: Resolución de decisiones de existencia física, canal y merma.	5](#tabla-3.1:-resolución-de-decisiones-de-existencia-física,-canal-y-merma.)

[Tabla 3.2: Resolución de decisiones de consistencia de precios y trazabilidad fiscal.	6](#tabla-3.2:-resolución-de-decisiones-de-consistencia-de-precios-y-trazabilidad-fiscal.)

[Tabla 3.3: Resolución de decisiones de lógica de cobro, asignación de pedidos y comisiones.	7](#tabla-3.3:-resolución-de-decisiones-de-lógica-de-cobro,-asignación-de-pedidos-y-comisiones.)

[Tabla 3.4: Resolución de decisiones de postventa, marketplace y logística inversa.	7](#tabla-3.4:-resolución-de-decisiones-de-postventa,-marketplace-y-logística-inversa.)

[Tabla 3.5: Resolución de decisiones de acreditación de consentimiento y crédito.	8](#tabla-3.5:-resolución-de-decisiones-de-acreditación-de-consentimiento-y-crédito.)

[Tabla 3.6: Resolución de decisiones de identidad, accesos y seguridad transaccional.	8](#tabla-3.6:-resolución-de-decisiones-de-identidad,-accesos-y-seguridad-transaccional.)

[Tabla 3.7: Catálogo del Dominio Retail: Núcleo de inventario y disponibilidad.	9](#heading=h.ue6dhqvc5my8)

[Tabla 3.8: Catálogo del Dominio Retail: Precio y cumplimiento comercial.	10](#heading=h.vsx8maczr7gb)

[Tabla 3.9: Catálogo del Dominio Retail: Venta, pedido y cumplimiento.	11](#heading=h.5pl0zkfh9fq1)

[Tabla 3.10: Catálogo del Dominio Retail: Postventa, marketplace y logística inversa.	13](#heading=h.vfixqb2fh5xq)

[Tabla 3.11: Catálogo del Dominio Financiero: Filial emisora fiscalizada.	14](#heading=h.7hl68knd3cbx)

[Tabla 3.12: Catálogo de la Capa transversal: Integración, identidad y resiliencia.	15](#heading=h.dvo7w8vjr4f0)

[Tabla 3.13: Objetivos específicos del proyecto, métricas y medios de verificación.	18](#tabla-3.13:-objetivos-específicos-del-proyecto,-métricas-y-medios-de-verificación.)

[Tabla 3.14: Matriz de asignación de alcance modular por etapa contractual.	21](#heading=h.7mkmumo1ec5x)

[Tabla 3.15: Estrategias de tratamiento para colisiones de calendario declaradas.	23](#tabla-3.15:-estrategias-de-tratamiento-para-colisiones-de-calendario-declaradas.)

[Tabla 3.16: Exclusiones explícitas del alcance y diseño compensatorio.	24](#tabla-3.16:-exclusiones-explícitas-del-alcance-y-diseño-compensatorio.)

[Tabla 3.17: Supuestos estructurales, impacto y mecanismo de validación.	25](#tabla-3.17:-supuestos-estructurales,-impacto-y-mecanismo-de-validación.)

[Tabla 3.18: Requerimientos funcionales core de gobernanza de datos y frontera regulatoria.	27](#tabla-3.18:-requerimientos-funcionales-core-de-gobernanza-de-datos-y-frontera-regulatoria.)

[Tabla 3.19: Requerimientos funcionales core de disponibilidad e inventario.	27](#tabla-3.19:-requerimientos-funcionales-core-de-disponibilidad-e-inventario.)

[Tabla 3.20: Requerimientos funcionales core de precio y evidencia fiscal.	28](#tabla-3.20:-requerimientos-funcionales-core-de-precio-y-evidencia-fiscal.)

[Tabla 3.21: Requerimientos funcionales core de pedido, cumplimiento y comisión.	28](#tabla-3.21:-requerimientos-funcionales-core-de-pedido,-cumplimiento-y-comisión.)

[Tabla 3.22: Requerimientos funcionales core de operación de tienda y contingencia.	29](#tabla-3.22:-requerimientos-funcionales-core-de-operación-de-tienda-y-contingencia.)

[Tabla 3.23: Requerimientos funcionales core de postventa, garantía legal y marketplace.	30](#tabla-3.23:-requerimientos-funcionales-core-de-postventa,-garantía-legal-y-marketplace.)

[Tabla 3.24: Requerimientos funcionales core de crédito, consentimiento y migración.	30](#tabla-3.24:-requerimientos-funcionales-core-de-crédito,-consentimiento-y-migración.)

[Tabla 3.25: Requerimientos funcionales core de accesos, eventos anuales y congelamiento.	31](#tabla-3.25:-requerimientos-funcionales-core-de-accesos,-eventos-anuales-y-congelamiento.)

[Tabla 3.26: Requerimientos no funcionales core de desempeño y tiempo de respuesta.	32](#tabla-3.26:-requerimientos-no-funcionales-core-de-desempeño-y-tiempo-de-respuesta.)

[Tabla 3.27: Requerimientos no funcionales core de capacidad operativa.	33](#tabla-3.27:-requerimientos-no-funcionales-core-de-capacidad-operativa.)

[Tabla 3.28: Requerimientos no funcionales core de seguridad, resiliencia y disponibilidad.	33](#tabla-3.28:-requerimientos-no-funcionales-core-de-seguridad,-resiliencia-y-disponibilidad.)

[Tabla 3.29: Requerimientos no funcionales core de retención, trazabilidad y migración.	34](#tabla-3.29:-requerimientos-no-funcionales-core-de-retención,-trazabilidad-y-migración.)

[Tabla 3.30: Condiciones obligatorias para el cierre y aceptación de la marcha blanca.	37](#tabla-3.30:-condiciones-obligatorias-para-el-cierre-y-aceptación-de-la-marcha-blanca.)

[Tabla 3.31: Criterios de aceptación por resultado de negocio y metas comprometidas.	38](#tabla-3.31:-criterios-de-aceptación-por-resultado-de-negocio-y-metas-comprometidas.)

[Tabla 3.32: Criterios de aceptación cualitativa y forma de verificación.	40](#tabla-3.32:-criterios-de-aceptación-cualitativa-y-forma-de-verificación.)

[Tabla A.1.1: Requerimientos Funcionales \- Ventas en Tienda.	41](#heading=h.fhhjwgsz5n9j)

[Tabla A.1.2: Requerimientos Funcionales \- Seguridad y Accesos.	41](#heading=h.bhw37etqr86j)

[Tabla A.1.3: Requerimientos Funcionales \- Precios y Etiquetado.	42](#heading=h.2qwxqvw1tgrj)

[Tabla A.1.4: Requerimientos Funcionales \- Pedidos y Cumplimiento.	43](#heading=h.2xv7azy9yi6l)

[Tabla A.1.5: Requerimientos Funcionales \- Operación de Tienda.	45](#heading=h.o9z0t1hshxoy)

[Tabla A.1.6: Requerimientos Funcionales \- Marketplace.	46](#heading=h.tzwwfhl373il)

[Tabla A.1.7: Requerimientos Funcionales \- Inventario y Disponibilidad.	48](#heading=h.q89u98ykqjeo)

[Tabla A.1.8: Requerimientos Funcionales \- Gobernanza de Datos.	50](#heading=h.iueilxjhdumy)

[Tabla A.1.9: Requerimientos Funcionales \- Evento de Alta Concurrencia.	50](#heading=h.bcwr23w8d93s)

[Tabla A.1.10: Requerimientos Funcionales \- Devoluciones y Garantía Legal.	51](#heading=h.aphcpd2ahp5x)

[Tabla A.1.11: Requerimientos Funcionales \- Crédito y Cobranza.	52](#heading=h.5twbkcg7ax8n)

[Tabla A.2.1: Requerimientos No Funcionales \- Disponibilidad.	54](#heading=h.v2836rrq7is0)

[Tabla A.2.2: Requerimientos No Funcionales \- Desempeño.	55](#heading=h.82e5cmnzvhjm)

[Tabla A.2.3: Requerimientos No Funcionales \- Consistencia de datos.	56](#heading=h.2gfp0pccu62a)

[Tabla A.2.4: Requerimientos No Funcionales \- Desempeño / Cumplimiento.	56](#heading=h.xus1hqbb0cyc)

[Tabla A.2.5: Requerimientos No Funcionales \- Portabilidad / Migración.	56](#heading=h.ebzo4zauunun)

[Tabla A.2.6: Requerimientos No Funcionales \- Seguridad / Arquitectura.	57](#heading=h.5shy262fk7lw)

[Tabla A.2.7: Requerimientos No Funcionales \- Auditabilidad.	58](#heading=h.5osnu8rkgtwr)

[Tabla A.2.8: Requerimientos No Funcionales \- Desempeño / Capacidad.	58](#heading=h.1lx7k8bdy6lu)

[Tabla A.2.9: Requerimientos No Funcionales \- Recuperabilidad.	59](#heading=h.squlkxwi7ve3)

[Tabla A.2.10: Requerimientos No Funcionales \- Seguridad.	59](#heading=h.6uj63eigt2mg)

[Tabla A.2.11: Requerimientos No Funcionales \- Seguridad / Cumplimiento.	60](#heading=h.3mlxaessixkd)

[Tabla A.2.12: Requerimientos No Funcionales \- Cumplimiento.	60](#heading=h.6p50uxftq1gr)

[Tabla A.2.13: Requerimientos No Funcionales \- Portabilidad / Escalabilidad.	62](#heading=h.3pcp4bbcw92y)

[Tabla A.2.14: Requerimientos No Funcionales \- Usabilidad.	62](#heading=h.lt4vciei743u)

[Tabla A.2.15: Requerimientos No Funcionales \- Usabilidad / Cumplimiento.	62](#heading=h.rdd7n5pnlmln)

[Tabla A.2.16: Requerimientos No Funcionales \- Operabilidad.	63](#heading=h.nr68y9oddwvr)

[Tabla A.2.17: Requerimientos No Funcionales \- Interoperabilidad.	63](#heading=h.g7oqz68z81kf)

[Tabla A.2.18: Requerimientos No Funcionales \- Auditabilidad / Desempeño.	64](#heading=h.d8s0t77vgjta)

[Tabla A.2.19: Requerimientos No Funcionales \- Usabilidad / Desempeño.	64](#heading=h.fzgsivtw1ejw)

[Tabla A.2.20: Requerimientos No Funcionales \- Efectividad de negocio.	65](#heading=h.v855nnrxqeqc)

[Tabla A.2.21: Requerimientos No Funcionales \- Seguridad / DevSecOps.	65](#heading=h.piqi0u4nakh8)

[Tabla A.3.1: Obligación del PROPONENTE.	66](#heading=h.j4s31fwcdhrb)

[Tabla A.4.1: Matriz de cumplimiento y trazabilidad.	66](#heading=h.3k8c97kffpu7)

# **LISTA DE ACRÓNIMOS** {#lista-de-acrónimos}

**ABC:** Clasificación ABC (gestión de inventario valor/rotación: A semanal, B mensual, C trimestral)  
**API:** Application Programming Interface / Interfaz de Programación de Aplicaciones  
**ASVS:** Application Security Verification Standard  
**ATP:** Available to Promise  
**B2B:** Business to Business (relaciones entre empresas, recobros)  
**CD:** Centro de distribución  
**CDC:** Change Data Capture  
**CI/CD:** Continuous Integration / Continuous Delivery  
**DDD:** Domain-Driven Design  
**DTE:** Documento Tributario Electrónico  
**E2E:** End to End  
**EDA:** Event-Driven Architecture  
**ERP:** Enterprise Resource Planning  
**IAM:** Identity and Access Management  
**IP:** Internet Protocol  
**K3s:** Distribución ligera de Kubernetes certificada CNCF (nodo de tienda)  
**KPI:** Key Performance Indicator  
**ML:** Machine Learning  
**MoSCoW:** Marco de priorización Must/Should/Could/Would  
**NIST:** National Institute of Standards and Technology  
**OMS:** Order Management System  
**OWASP:** Open Web Application Security Project  
**P2P:** Punto a punto  
**POC:** Proof of Concept  
**POS:** Point of Sale  
**RRHH:** Recursos Humanos  
**RTO:** Recovery Time Objective  
**RPO:** Recovery Point Objective  
**RUT:** Rol Único Tributario  
**S.A.:** Sociedad Anónima  
**SBOM:** Software Bill of Materials  
**SLA:** Service Level Agreement  
**SLSA:** Supply chain Levels for Software Artifacts  
**SMART:** Specific, Measurable, Achievable, Relevant, Time-bound  
**T\&C:** Terms and Conditions  
**WMS:** Warehouse Management System  
**WORM:** Write Once Read Many

# 

# **3\. Introducción y alcance de la solución** {#3.-introducción-y-alcance-de-la-solución}

## **3.1. Resumen Ejecutivo de la Solución**  {#3.1.-resumen-ejecutivo-de-la-solución}

La solución propuesta por Only Simple Solutions para Multitiendas Ancoa S.A. no se limita a una modernización informática convencional. Asume el desafío central de la compañía: una operación dual donde convergen, bajo un mismo mostrador y para un mismo cliente, un negocio de comercio minorista masivo y un emisor de crédito fiscalizado sujeto a la supervisión de la autoridad del mercado financiero.

La incoherencia operativa actual caracterizada por registros de inventario inexactos (12,4% de discrepancia), discrepancias de precios en sala (11%), falta de trazabilidad en las repactaciones de crédito (1.240 casos sin respaldo) y una fragmentación de nueve plataformas unidas por 14 interfaces punto a punto sin documentación se aborda mediante una arquitectura de microservicios sin estado, híbrida y orientada a eventos (EDA), estrictamente alineada con los mandatos normativos y los requerimientos transversales de la licitación (RT-02.02, RT-02.05, RT-02.10).

En estricto cumplimiento del RT-02.02 y de la restricción no negociable del directorio de Ancoa, la plataforma abandona el monolito lógico fragmentado y adopta una Arquitectura Modular de Microservicios Sin Estado (Stateless) agrupada en Límites de Contexto estrictos (Domain-Driven Design).

## **3.2. Alcance** {#3.2.-alcance}

### **3.2.1 Alcance de la Etapa 1 y de la Etapa 2**

## **3\. Objetivos del proyecto** {#3.-objetivos-del-proyecto}

Los objetivos se formulan bajo el estándar SMART: resultados específicos, metas cuantificadas, viabilidad arquitectónica y un horizonte anclado a los 56 meses del contrato. Ningún objetivo se redacta como intención ni admite verificación subjetiva.

### **3.5.1. Objetivo General** {#3.5.1.-objetivo-general}

Dotar a Multitiendas Ancoa S.A. de una plataforma híbrida orientada a eventos que garantice sus cuatro promesas comerciales (existencia, precio, entrega y condiciones crediticias). Esto exige operar sobre registros de exactitud comprobable, asegurar una separación auditable entre el retail y la filial emisora, y no degradar la continuidad operativa de las 22 sucursales ni exceder las ventanas de intervención.

El éxito global exige el cumplimiento de las 12 métricas específicas, una auditoría de dominios sin hallazgos y la migración total de la cartera sin divergencias contables.

### **3.5.2. Objetivos Específicos** {#3.5.2.-objetivos-específicos}

##### **Tabla 3.13:** Objetivos específicos del proyecto, métricas y medios de verificación. {#tabla-3.13:-objetivos-específicos-del-proyecto,-métricas-y-medios-de-verificación.}

| ID / Dimensión | Objetivo Específico | Línea Base a Meta  | Medio de Verificación |
| :---- | :---- | :---- | :---- |
| **OE-01 Existencia** | Reducir la discrepancia de inventario físico-lógico mediante conteo continuo ABC y clasificación de ajustes. | 12,4 % a ≤ 2 % por categoría  | Indicador diario de exactitud y auditoría independiente. |
| **OE-02 Existencia** | Eliminar cancelaciones por promesas sin respaldo físico mediante cálculo de disponibilidad con colchón dinámico. | 1,9 % a ≤ 0,3 % anual y cero quiebres en evento  | Medición mensual de pedidos aceptados. |
| **OE-03 Existencia** | Segregar la merma aislando la pérdida física del descuadre administrativo mediante tipificación obligatoria. | 0 % a 100 % de ajustes clasificados en 6 tipologías  | Reporte mensual conciliado con cierre contable. |
| **OE-04 Precio** | Eliminar divergencia entre precio exhibido y cobrado, condicionando el POS a la confirmación de recambio físico. | 11 % a ≤ 0,5 % de discrepancia  | Muestreo interno periódico y registro de incidentes. |
| **OE-05 Precio** | Acreditar el precio histórico publicado ante requerimientos regulatorios en cualquier canal e instante. | Nula a 100 % de consultas resueltas en ≤ 1 min  | Prueba de recuperación sobre ventana histórica de 3 años. |
| **OE-06 Entrega** | Elevar el cumplimiento de fecha de entrega sustituyendo asignación por proximidad por Costo Total de Servir. | 81 % a ≥ 97 % de pedidos en plazo  | Medición continua sobre estado único del pedido. |
| **OE-07 Entrega** | Suprimir la captura financiera sobre unidades no disponibles mediante preautorización sin captura. | Cobro inicial a Cero cobros sostenidos por pedidos no cumplibles  | Conciliación diaria de preautorizaciones y capturas. |
| **OE-08 Crédito** | Acreditar el consentimiento y entrega de información precontractual en toda repactación u originación. | 1.240 repactaciones sin respaldo a Cero operaciones sin evidencia  | Auditoría censal y prueba de recuperación WORM. |
| **OE-09 Crédito** | Reducir el tiempo de evaluación crediticia en POS sin diferir el flujo de cumplimiento normativo. | 40s a 3m a ≤ 8s (p95) sin mayor tiempo de atención  | Medición E2E instrumentada en mesón y caja. |
| **OE-10 Crédito** | Migrar cartera viva (620k clientes) mitigando el riesgo normativo de la plataforma obsoleta. | Plataforma 2011 a 100 % migrado con cero divergencias  | Conciliación diaria automatizada por ola de migración. |
| **OE-11 Frontera** | Implementar y auditar separación lógica entre retail y filial de crédito, registrando todo cruce. | Separación parcial a Auditoría sin hallazgos y 100 % de cruces registrados | Informe de auditoría independiente. |
| **OE-12 Continuidad** | Asegurar venta y crédito offline ante pérdida de enlace, con reconciliación automática post-contingencia. | Detención total a ≥ 8 hrs operación autónoma; cuadratura ≤ 30 min | Prueba de desconexión en horario comercial. |

 

### **3.5.3. Responsabilidad sobre la adopción y los indicadores** {#3.5.3.-responsabilidad-sobre-la-adopción-y-los-indicadores}

El modelo de gobierno del proyecto distingue estrictamente entre la capacidad técnica de la plataforma y la disciplina operativa de la compañía.

* **Indicadores garantizados (100% sistémicos):** Los objetivos OE-03, OE-05 y OE-07 a OE-12 dependen íntegramente de la arquitectura entregada. Se comprometen y garantizan sin condición de adopción por parte del usuario.  
* **Indicadores compartidos (Sistémicos \+ Operativos):** Los objetivos comerciales OE-01, OE-02, OE-04 y OE-06 requieren un esfuerzo conjunto. La solución técnica provee la capacidad (ej. algoritmo ATP, ruteo de etiquetas), pero el CLIENTE ejecuta el proceso físico en sala (conteo, escaneo, picking). El acta de aceptación técnica aislará el rendimiento del software de la adopción humana, desplegando estas funciones primero en pilotos acotados para detectar desviaciones operativas antes del escalamiento.

## **Supuestos**

El Capítulo 16 de las Bases Técnicas enumera 25 decisiones estructurales que Ancoa delegó intencionalmente en los proponentes. Cada una admite múltiples enfoques arquitectónicos con impactos divergentes en costo, riesgo y continuidad operativa.

Este capítulo resuelve la totalidad de estas decisiones. Ninguna se traslada a una fase posterior ni se resuelve por omisión. Cada resolución queda inscrita en el registro consolidado de supuestos bajo la nomenclatura SUP-nn. Cuando una decisión depende de un dato empírico que la compañía hoy no posee, la arquitectura define un valor inicial fundamentado y un mecanismo de recalibración durante la fase de levantamiento. Desde la ingeniería del proyecto, se establece que es preferible comprometer y gobernar un parámetro explícito antes que diseñar sobre vacíos operacionales.

Cinco de estas decisiones condicionan la viabilidad central del proyecto y se desarrollan en extenso, respondiendo a interrogantes críticas de arquitectura, riesgo y cumplimiento regulatorio:

1. ¿De dónde se extrae el dato de inventario que rige la promesa de venta?  
2. ¿Cuál es la estrategia de reemplazo para el sistema central monolítico de 2009?  
3. ¿Cuál es la frontera lógica de datos entre el negocio de retail y la filial de crédito?  
4. ¿Cómo se unifica la identidad del cliente sin vulnerar dicha frontera?  
5. ¿Cómo se garantiza la operación crediticia offline sin violar el mandato fiduciario?  
6. ¿Cómo se migra una cartera viva de 620.000 deudores mitigando el riesgo sistémico?

Las diecinueve decisiones restantes se presentan agrupadas por ámbito de negocio. Finalmente, la sección 3.2.7 aborda cinco vacíos operacionales detectados por este proponente, incluyendo la resolución de una contradicción directa entre dos restricciones catalogadas como no negociables en las bases.

### **3.2.1. SUP-01: El origen y cálculo de la disponibilidad de inventario** {#3.2.1.-sup-01:-el-origen-y-cálculo-de-la-disponibilidad-de-inventario}

Las auditorías de conteo cíclico evidencian una discrepancia de inventario del 12,4 %; sin embargo, la disponibilidad del canal digital se calcula sobre esta base inexacta aplicando un margen de seguridad estático y obsoleto heredado de 2019\. Al ser un parámetro transversal que omite la varianza de exactitud entre categorías y sucursales, este modelo generó un impacto operacional y comercial crítico en el evento de junio de 2026, donde se autorizaron 2.840 transacciones sin respaldo físico. Este incidente no responde a una falla de ejecución de código, sino a una falencia estructural en las reglas de negocio: la ausencia de un índice de confianza dinámico que pondere la calidad del dato de inventario antes de comprometer la promesa de venta.

Se establece la creación de un servicio centralizado, Available to Promise (ATP), que pasa a ser la única fuente de verdad para los cuatro canales, prohibiendo por diseño técnico el acceso directo al inventario en bruto. Este componente calcula la cantidad comprometible restando del registro las unidades reservadas, los pedidos aceptados y un colchón de incertidumbre dinámico. Este parámetro se obtiene de la exactitud histórica medida por el conteo cíclico para esa categoría en ese punto de venta: una categoría con buen historial arriesga poco margen; una con historial de errores arriesga mucho más. El colchón se amplía automáticamente durante el evento anual, y el servicio entrega la disponibilidad acompañada de un nivel de confianza, evitando compromisos comerciales insostenibles.

Publicar con colchón implica mostrar menos disponibilidad aparente y asumir una menor venta en el corto plazo. Se acepta esta restricción deliberadamente: una venta que no se puede cumplir genera un daño mayor al negocio. El colchón deja de ser una variable rígida en el código y se consolida como un parámetro gobernable que la Gerencia de Logística define, firma y versiona. El riesgo inverso (un colchón sobrecalibrado) se monitorea comparando la tasa de cancelación resultante contra el 1,9 % anual actual.

### **3.2.2. SUP-02: Estrategia de transición para el sistema central de 2009** {#3.2.2.-sup-02:-estrategia-de-transición-para-el-sistema-central-de-2009}

El ecosistema tecnológico actual se caracteriza por una arquitectura fragmentada de nueve plataformas interactuando mediante catorce integraciones punto a punto (P2P) sin documentación centralizada. El sistema de 2009 opera como el nodo monolítico más crítico, gestionando el maestro de productos, compras, inventario contable y precios. Ante este nivel de acoplamiento, se descarta una estrategia de reemplazo total en un único corte por su alto impacto en la continuidad operativa y su incompatibilidad con las cinco ventanas anuales de congelamiento de TI. Simultáneamente, se rechaza preservar el status quo añadiendo nuevas conexiones directas, ya que esto incrementaría críticamente la deuda técnica y el riesgo operacional sobre una infraestructura no gobernable.

La arquitectura de transición se estructura en tres fases. Primero, el levantamiento exhaustivo de las catorce integraciones, asumiendo este mapa topológico como un entregable crítico del proyecto, no como un insumo previo del cliente. Segundo, la implementación de un bus de eventos (Event-Driven Architecture) que desacopla la comunicación, prohibiendo nuevas conexiones P2P y retirando progresivamente las existentes, priorizando las que alimentan disponibilidad y precio. Tercero, la habilitación de un API Gateway frente al sistema de 2009 (Patrón Estrangulador), enrutando el tráfico para reemplazar capacidades progresivamente sin interrumpir la operación, manteniendo el ERP actual intacto como único emisor de documentos tributarios.

Se asume como restricción que este modelo transicional requiere mayor tiempo de ejecución que una reescritura total, y que una porción del núcleo de 2009 seguirá activa al finalizar el contrato. Para mitigar el riesgo de flujos paralelos no documentados (escritura directa en base de datos), se define una prueba de interceptación sobre un flujo piloto (carga de precios) antes de escalar el enrutamiento.

### **3.2.3. SUP-03 y SUP-04: Frontera de datos e Identidad Unificada del Cliente**  {#3.2.3.-sup-03-y-sup-04:-frontera-de-datos-e-identidad-unificada-del-cliente}

El gobierno de datos impone resolver la fricción legal entre el negocio de retail (sujeto a la Ley del Consumidor) y el negocio financiero (entidad fiscalizada). La construcción de una vista unificada de cliente exige establecer primero las barreras de privacidad, garantizando una separación lógica auditable.

El perímetro de cruce de datos se establece en tres dimensiones. Sobre el contenido, sólo transita la información declarada en un inventario de interfaces autorizadas, fundamentada en bases de licitud explícitas (Ley N° 21.719). Sobre la direccionalidad, la restricción es bidireccional; el motor de originación crediticia no puede invocar atributos comerciales sin respaldo legal. Sobre el control técnico, un gestor de consentimientos deniega por omisión (Zero Trust) todo flujo no autorizado, registrando tanto cruces efectivos como intentos bloqueados. Consecuentemente, el motor de marketing excluye por diseño los atributos financieros.

La identidad (SUP-03) se resuelve mediante una arquitectura en dos capas. En el dominio retail, un motor de resolución unifica interacciones (RUT \+ coincidencia probabilística) mediante eventos asíncronos. Hacia el dominio financiero, la interoperabilidad se ejecuta estrictamente mediante consultas síncronas bajo demanda (ej. solicitud explícita de estado de cuenta), contra una zona neutral que expone únicamente identificadores técnicos anonimizados. Se asume el costo operacional de latencia en consultas transfronterizas como una condición innegociable para asegurar el cumplimiento regulatorio.

### **3.2.4. SUP-07: Continuidad de la operatoria de crédito ante desconexión de sucursales** {#3.2.4.-sup-07:-continuidad-de-la-operatoria-de-crédito-ante-desconexión-de-sucursales}

El diseño arquitectónico debe resolver la fricción directa entre la exigencia de continuidad operativa y el cumplimiento normativo financiero. Por un lado, el negocio exige garantizar la venta y cobro offline durante un mínimo de ocho horas; un escenario de contingencia de alta probabilidad considerando que 14 de las 22 sucursales dependen de redes de terceros. Dado que la tarjeta propia concentra el 38 % de las transacciones, inhabilitarla invalida la continuidad real. Por otro lado, la filial emisora opera como entidad fiscalizada, imponiendo la restricción ineludible de acreditar y controlar el riesgo de cada operación.

Se establece un modelo de contingencia offline basado en la preautorización de cupos. Sin conexión, el punto de venta local no ejecuta evaluación de riesgo, sino que consume un cupo rotativo previamente aprobado y sincronizado en el servidor local, encolando la operación para su consolidación diferida. La exposición se mitiga mediante cuatro umbrales dinámicos calculados según el volumen real de la tienda: (1) límite transaccional unitario, (2) límite acumulado por cliente, (3) umbral de transacciones consecutivas y (4) ventana de caducidad por reconexión. Acciones que exigen perfilamiento crediticio (apertura de tarjeta, aumento de cupo) quedan bloqueadas por diseño sin enlace.  
La asimetría del riesgo fundamenta la decisión: el riesgo real no es crediticio (el cupo fue evaluado pre-contingencia), sino el fraude por doble consumo. Bajo los parámetros del caso, la exposición por tienda ronda los \$150.000 frente a la mitigación de una pérdida de venta proyectada en \$10.000.000 por evento.

### **3.2.5. SUP-25: Estrategia de migración de la cartera activa de crédito** {#3.2.5.-sup-25:-estrategia-de-migración-de-la-cartera-activa-de-crédito}

La migración se define como el traslado concurrente de 620.000 clientes con saldo vigente, repactaciones y procesos de cobranza/judiciales en curso. Dada la naturaleza de la entidad fiscalizada, se impone tolerancia nula a la divergencia de saldos. La restricción temporal es inamovible (2029), dictaminada por el fin de soporte del core de 2011 y el hito de remediación normativo.

Se descarta el reemplazo big bang. La transición se ejecutará mediante olas de coexistencia, operando ambas plataformas en paralelo con una conciliación diaria automatizada. Un umbral de discrepancia predefinido actuará como freno de emergencia (circuit breaker), deteniendo el avance de la ola ante divergencias contables. El mecanismo de rollback se mantendrá activo y validado durante toda la ventana de coexistencia.

El cronograma contractual se mantiene inalterado; la estrategia radica en separar la habilitación técnica de la ejecución operativa. El corte final ocurre en la Etapa 2, pero los componentes habilitantes (gestor de consentimientos, saneamiento de datos y motor de conciliación) se despliegan en la Etapa 1\. Adelantar la ingeniería de datos financieros a la fase inicial es la única vía crítica viable para asegurar un margen de maniobra ante el límite regulatorio de 2029\.

### **3.2.6. Resolución de las decisiones restantes** {#3.2.6.-resolución-de-las-decisiones-restantes}

#### **3.2.6.1. La existencia física: cómo se cuenta, cómo se reserva y dónde se almacena** {#3.2.6.1.-la-existencia-física:-cómo-se-cuenta,-cómo-se-reserva-y-dónde-se-almacena}

##### **Tabla 3.1:** Resolución de decisiones de existencia física, canal y merma. {#tabla-3.1:-resolución-de-decisiones-de-existencia-física,-canal-y-merma.}

| ID | El dolor operativo y comercial | La resolución arquitectónica y de negocio |
| :---- | :---- | :---- |
| **SUP-12** | La colisión de canales genera pérdida de venta cierta. Cuando un cliente digital reserva una unidad en el carro, el vendedor presencial queda bloqueado para facturar esa misma unidad física. | Se implementa una reserva temporal parametrizable al agregar al carro. La prelación de venta favorece al canal presencial: si la transacción física se concreta, la reserva digital se revoca automáticamente y el pedido web se enruta al motor de compensación, protegiendo la comisión y la venta confirmada de la sala. |
| **SUP-17** | La merma (1,9 % de las ventas) se consolida bajo un indicador único, impidiendo a las jefaturas de tienda aislar la pérdida por hurto de los descuadres puramente administrativos. | Todo ajuste de inventario exigirá clasificación obligatoria en seis tipologías tipificadas (incluyendo error de recepción y daño). Este paso forzoso en el flujo de sistema permite segregar contablemente la merma y auditar la gestión real del inventario. |
| **SUP-18** | El cálculo del margen de confianza (SUP-01) depende de medir dónde falla el inventario, pero los conteos paralizan la operación comercial. | Se establece un modelo de conteo continuo ABC (A: semanal, B: mensual, C: trimestral) ejecutado en la ventana valle de flujo (10:00 \- 13:00). Se configuran disparadores de conteo ciego automático ante quiebres de stock en preparación, obsolescencia anómala o saldos negativos, sin exigir cierres de local. |
| **SUP-20** | El CD de Concepción opera sobre procesos manuales, inyectando inexactitud directa al registro nacional y comprometiendo las promesas de entrega en la zona sur. | Se excluye temporalmente este nodo logístico como origen de disponibilidad para el canal digital hasta su estabilización. Su integración futura al WMS corporativo se condiciona a un caso de negocio de modernización. Se asume la degradación temporal de tiempos de entrega en el sur para proteger la exactitud de la promesa global. |

#### **3.2.6.2. El precio: consistencia omnicanal y evidencia fiscal** {#3.2.6.2.-el-precio:-consistencia-omnicanal-y-evidencia-fiscal}

##### **Tabla 3.2:** Resolución de decisiones de consistencia de precios y trazabilidad fiscal. {#tabla-3.2:-resolución-de-decisiones-de-consistencia-de-precios-y-trazabilidad-fiscal.}

| ID | El dolor operativo y comercial | La resolución arquitectónica y de negocio |
| :---- | :---- | :---- |
| **SUP-08** | La asincronía entre el maestro de precios y el etiquetado físico (11 % de discrepancia) genera fricción en caja y vulnerabilidad ante fiscalizaciones de protección al consumidor. | Se establece primacía del precio exhibido físicamente. Ante una discrepancia detectada en caja, el sistema adopta automáticamente el valor menor, imputando la diferencia como pérdida operativa de la sucursal. Esta penalización financiera directa fuerza la alineación logística del etiquetado local. |
| **SUP-09** | Las ventanas de actualización manual dejan un margen de hasta 24 horas donde el sistema central y la sala operan con listas de precios desfasadas. | La actualización de precios centralizados no impacta el POS hasta que la tienda física escanea y confirma el recambio de la etiqueta de góndola. El sistema retiene el precio anterior en caja, eliminando la discrepancia estructural, apoyado en un dashboard de desactualización para auditoría de cumplimiento. |
| **SUP-10** | La compañía carece de trazabilidad para demostrar el precio publicado en una fecha u hora específica ante reclamos formales. | La arquitectura de datos implementa versionado de precios (Slowly Changing Dimensions). Se mantiene una réplica local ligera para operar offline y un repositorio centralizado inmutable (3 años de retención) que permite recuperar la fotografía exacta del precio por canal mediante consultas indexadas por timestamp. |

#### **3.2.6.3. El pedido: lógica de cobro, asignación y comisión** {#3.2.6.3.-el-pedido:-lógica-de-cobro,-asignación-y-comisión}

##### **Tabla 3.3:** Resolución de decisiones de lógica de cobro, asignación de pedidos y comisiones. {#tabla-3.3:-resolución-de-decisiones-de-lógica-de-cobro,-asignación-de-pedidos-y-comisiones.}

| ID | El dolor operativo y comercial | La resolución arquitectónica y de negocio |
| :---- | :---- | :---- |
| **SUP-11** | La cancelación de pedidos por quiebre de stock derivó en capturas financieras sobre mercadería inexistente, generando contingencias legales y operativas. | El checkout digital transiciona a un modelo de "Preautorización sin Captura". El cargo efectivo solo se liquida tras la confirmación de picking. Ante quiebres, un motor orquesta soluciones alternativas (re-enrutamiento, sustitución). Si se requiere cancelación, la preautorización se libera sin impacto financiero para el cliente. |
| **SUP-13** | La asignación de fulfillment basada puramente en distancia geográfica vacía sistemáticamente las salas de venta de mayor rotación (17 %). | El orquestador de pedidos (OMS) sustituye la variable de proximidad por un algoritmo de "Costo Total de Servir", que pondera el costo logístico de última milla contra el costo de oportunidad comercial de extraer la unidad de una sala de alta conversión, respetando siempre el SLA de entrega del cliente. |

#### **3.2.6.4. Postventa, Marketplace y Logística Inversa** {#3.2.6.4.-postventa,-marketplace-y-logística-inversa}

##### **Tabla 3.4:** Resolución de decisiones de postventa, marketplace y logística inversa. {#tabla-3.4:-resolución-de-decisiones-de-postventa,-marketplace-y-logística-inversa.}

| ID | El dolor operativo y comercial | La resolución arquitectónica y de negocio |
| :---- | :---- | :---- |
| **SUP-15** | La devolución física de mercadería de sellers externos queda inmovilizada en bodegas propias sin trazabilidad, generando fricción en las liquidaciones financieras. | Se implementa notificación transaccional en tiempo real. Al procesar la recepción física en la tienda, el sistema dispara un evento al portal del vendedor (Seller Center) con el estado, motivo y ubicación del activo, registrando la responsabilidad financiera del reingreso en el mismo acto. |
| **SUP-16** | La ausencia de SLAs formales impide penalizar o excluir a los sellers externos que degradan la calidad del servicio de Ancoa. | Se activa un motor de gobernanza marketplace condicionado a la aceptación digital de políticas (T\&C). El sistema mide automáticamente cinco KPIs críticos (tasa de cancelación, puntualidad, devoluciones por falla, lead time de respuesta y calidad de catálogo). Los incumplimientos gatillan suspensiones sistémicas automáticas. |
| **SUP-21** | El modelo actual de derivación de garantías (hacia fabricantes o externos) vulnera la normativa de protección al consumidor y genera alta fricción en mesón. | La arquitectura asume la resolución en "Primera Línea". Ancoa absorbe la prestación legal directamente frente al cliente en la sucursal. En segundo plano, un módulo de conciliación gestiona los recobros B2B contra el proveedor o seller, aislando al consumidor de la disputa financiera interna. |
| **SUP-22** | El procesamiento de retractos a distancia carece de estandarización temporal y contamina el inventario disponible con unidades mermadas. | El plazo legal de retracto se abstrae como un parámetro gobernable. Toda devolución reingresa a un estado de "Cuarentena Lógica"; el WMS bloquea su disponibilidad comercial hasta que un usuario identificado registre la inspección física y certifique su aptitud de reventa. |

#### **3.2.6.5. El crédito: acreditación del consentimiento** {#3.2.6.5.-el-crédito:-acreditación-del-consentimiento}

##### **Tabla 3.5:** Resolución de decisiones de acreditación de consentimiento y crédito. {#tabla-3.5:-resolución-de-decisiones-de-acreditación-de-consentimiento-y-crédito.}

| ID | El dolor operativo y comercial | La resolución arquitectónica y de negocio |
| :---- | :---- | :---- |
| **SUP-05** | La dependencia de grabaciones telefónicas con purga a 90 días expone a la filial emisora a sanciones por incapacidad probatoria de repactaciones. | Sustitución completa hacia expedientes digitales estructurados. Se captura el contrato, metadatos de sesión (IP, canal, timestamp) y se sella criptográficamente. El archivo se rige por políticas WORM (inmutabilidad) en almacenamiento frío, asegurando retención legal (duración \+ 6 años) y recuperación demostrable. |
| **SUP-06** | La obligación normativa de entregar información precontractual compite con los tiempos de atención; el personal comercial tiende a evadir procesos lentos. | El registro de entrega precontractual se embebe como requisito sistémico bloqueante en el flujo del POS/App, sin añadir clicks o firmas en papel. El sistema impide cursar la aceptación final si no existe el registro de timestamp previo que certifique el despliegue del simulador de condiciones. |

 

#### **3.2.6.6. Identidad, Accesos y Seguridad Transaccional** {#3.2.6.6.-identidad,-accesos-y-seguridad-transaccional}

##### **Tabla 3.6:** Resolución de decisiones de identidad, accesos y seguridad transaccional. {#tabla-3.6:-resolución-de-decisiones-de-identidad,-accesos-y-seguridad-transaccional.}

| ID | El dolor operativo y comercial | La resolución arquitectónica y de negocio |
| :---- | :---- | :---- |
| **SUP-19** | Más de 1.100 repositores externos operan en sala e interactúan con sistemas sin relación laboral formal ni control de acceso directo. | Se delega la administración del ciclo de vida al proveedor B2B. A través del portal corporativo, el empleador externo aprovisiona y define la caducidad de las credenciales de su personal. El sistema aplica revocación por omisión: sin renovación explícita, el acceso expira automáticamente. |
| **SUP-23** | El desbordamiento de tráfico durante eventos masivos (Cyber) deriva en caídas catastróficas al no existir protocolos de degradación predefinidos. | Se implementa un modelo de resiliencia escalonado. La primera línea (salas de espera, limitación de concurrencia) escala automáticamente por telemetría. La degradación crítica (apagón de pasarelas de crédito, bloqueo de categorías completas) requiere orquestación manual exclusiva por un rol facultado, protegiendo ingresos de impacto mayor. |
| **SUP-24** | La alta rotación de personal (62 %) y las contrataciones de temporada dejan perfiles huérfanos con accesos críticos activos en cajas y carteras. | Erradicación de credenciales compartidas en el POS, sustituidas por traspasos rápidos de sesión (hot-swapping). Se implementa un conector bidireccional con el sistema de RRHH: los finiquitos contractuales disparan eventos asíncronos que revocan inmediatamente el acceso en todas las capas lógicas y físicas de la plataforma. |

## **3.3. Módulos funcionales de la solución** {#3.3.-módulos-funcionales-de-la-solución}

## **3.4. Diagrama conceptual de solución e interacción de actores** {#3.4.-diagrama-conceptual-de-solución-e-interacción-de-actores}

*![][image1]*

###### **Figura 3.1:** Diagrama conceptual de solución e interacción de actores. {#figura-3.1:-diagrama-conceptual-de-solución-e-interacción-de-actores.}

## **3.6. Alcance de la Etapa 1 y de la Etapa 2, con criterio de asignación** {#3.6.-alcance-de-la-etapa-1-y-de-la-etapa-2,-con-criterio-de-asignación}

El cronograma contractual de 56 meses se asume como indivisible e inalterable: la Etapa 1 contempla desarrollo entre los meses 1 y 12, marcha blanca entre el 13 y el 15, y paso a producción en el mes 16; la Etapa 2 comprende desarrollo entre los meses 13 y 18, marcha blanca entre el 19 y el 20, y producción en el mes 21; finalmente, la fase de Operación abarca los meses 21 a 56\. La definición de alcance no consiste en redistribuir estos plazos, sino en determinar qué capacidades arquitectónicas se construyen y liberan en cada ventana.

La preferencia de urgencia manifestada por el Comité Directivo (inventario y disponibilidad como prioridad, seguido de precio, y finalmente el negocio financiero, marketplace y analítica) se adopta como directriz base. Sin embargo, se aplica una corrección estructural en su tramo final para mitigar el riesgo sistémico de la migración financiera y garantizar el cumplimiento normativo, conforme a los siguientes criterios de asignación.

## 

### **3.6.1. Criterios de asignación** {#3.6.1.-criterios-de-asignación}

Se establecen seis criterios excluyentes, en estricto orden de precedencia, para la asignación de módulos. Ninguna carga de trabajo se distribuye por afinidad temática o comodidad del equipo:

1. **Dependencia técnica dura:** Las capacidades habilitantes anteceden obligatoriamente a las dependientes. La frontera de datos precede a cualquier vista unificada de cliente; el motor de disponibilidad precede a la promesa de entrega y publicación digital; el bus de eventos precede a la estrangulación del núcleo de 2009\.  
2. **Irreversibilidad arquitectónica:** Los componentes cuya separación a posteriori es inviable se ejecutan primero. Específicamente, la segregación lógica y física entre el dominio retail y el negocio financiero fiscalizado.  
3. **Hitos regulatorios externos:** Cumplimiento ineludible de la fecha límite inamovible (2029) impuesta por el plan de remediación de la autoridad financiera y el fin de soporte de la plataforma de originación de 2011\.  
4. **Exposición legal vigente:** Priorización de los componentes vinculados a pasivos normativos en curso, como el procedimiento derivado de las 2.840 cancelaciones y la fiscalización de precios de febrero de 2026\.  
5. **Capacidad de absorción operacional:** La asignación de trabajo concurrente se dimensiona sobre la capacidad real del área de TI del CLIENTE (46 profesionales para sostener 9 plataformas, 22 sucursales y 2 centros de distribución), evitando el colapso operativo en hitos paralelos.  
6. **Ventanas de congelamiento de TI:** Adaptación de los despliegues a los cinco períodos de bloqueo anuales, concentrando las intervenciones mayores exclusivamente en las únicas dos ventanas viables: marzo abril y julio octubre.

### **3.6.2. La corrección al orden de urgencia declarado** {#3.6.2.-la-corrección-al-orden-de-urgencia-declarado}

El análisis de riesgo valida la imposibilidad de migrar una cartera viva de 620.000 clientes con saldo durante la limitada ventana de seis meses de desarrollo asignada a la Etapa 2\.

La estrategia de mitigación no altera la fecha del corte final de la cartera (que se mantiene en la Etapa 2 para respetar el orden comercial), sino que escinde la habilitación técnica de la ejecución operativa. Se establece el despliegue temprano en la Etapa 1 de los componentes habilitantes críticos: el gobierno de la frontera de datos, la captura estructurada de consentimientos, el archivo inmutable de largo plazo, el saneamiento de los 620.000 registros y el motor de conciliación. De este modo, la Etapa 2 recibe un ecosistema pre-validado contra la plataforma de 2011, no un diseño desde cero.

Respecto a la analítica predictiva y los modelos de aprendizaje automático (Machine Learning), su despliegue se introduce de manera controlada y acotada a través de la Cartera de Innovaciones. Estos modelos operarán estrictamente sobre datos anonimizados, condicionando su activación a la auditoría técnica que certifique que la frontera de datos entre el retail y el negocio financiero es infranqueable, asegurando cero vulneraciones normativas.

### **3.6.4. Colisiones de calendario declaradas** {#3.6.4.-colisiones-de-calendario-declaradas}

Asumiendo la adjudicación en diciembre de 2026 y la formalización contractual, el Mes 1 inicia efectivamente en enero de 2027\. Esto sitúa las salidas a producción en abril de 2028 (Etapa 1\) y septiembre de 2028 (Etapa 2), esquivando exitosamente los bloqueos anuales. Las colisiones residuales se abordan mediante planes de mitigación técnicos:

##### **Tabla 3.15:** Estrategias de tratamiento para colisiones de calendario declaradas. {#tabla-3.15:-estrategias-de-tratamiento-para-colisiones-de-calendario-declaradas.}

| Momento | Colisión Operativa / Normativa | Estrategia de Tratamiento |
| :---- | :---- | :---- |
| **Meses 11–12** | El cierre de desarrollo (Etapa 1\) choca con el congelamiento de Navidad y el pico de 1.900 altas de temporada. | Congelamiento absoluto de despliegues productivos. Las pruebas integrales y de estrés se ejecutan en Preproducción asimilando el volumen real del *peak*. |
| **Mes 13** | El inicio de la marcha blanca coincide con la última semana del congelamiento de fin de año (hasta el 6 de enero). | Inicio efectivo de la marcha blanca diferido al 7 de enero. La desviación técnica (6 días) se absorbe con la reserva de contingencia sin desplazar el hito de Producción. |
| **Meses 13–15** | La marcha blanca convive con el congelamiento "Vuelta a Clases". | Aprovechamiento del alto volumen transaccional para telemetría. La estabilización y corrección de código se concentra en marzo, previo a la certificación final. |
| **Meses 13–15** | Solapamiento contractual de Marcha Blanca (Etapa 1\) y Desarrollo (Etapa 2). | Segregación física de frentes de trabajo y dotación, evidenciada y garantizada en la matriz de Nivelación de Recursos del cronograma. |
| **Mes 17 o 18** | El *Cyber* de 2028 (fecha móvil dictada por terceros) irrumpe con la Etapa 1 en producción y la Etapa 2 en desarrollo. | Congelamiento del código (6 semanas de preaviso). Validación previa del motor ATP sobre un subconjunto de alto riesgo y activación de protocolos de degradación preventiva. |

#####  

### **3.6.5. Fase de Operación** {#3.6.5.-fase-de-operación}

Se despliegan 36 meses continuos de operación y soporte de misión crítica (meses 21 a 56). La estrategia operativa incorpora soporte 24x7x365 para el canal digital y los componentes financieros, y atención en horario comercial extendido (09:00 a 23:00) para las sucursales y operaciones físicas. Se contempla cobertura reforzada documentada para los tres eventos anuales masivos y soporte especializado presencial distribuido en las 11 regiones de operación.

## **3.7. Exclusiones explícitas, supuestos y restricciones** {#3.7.-exclusiones-explícitas,-supuestos-y-restricciones}

## 

### **3.7.1. Exclusiones explícitas** {#3.7.1.-exclusiones-explícitas}

Los siguientes componentes quedan excluidos del alcance de implementación. La arquitectura se diseña asumiendo la convivencia y la orquestación con estos elementos:

##### **Tabla 3.16:** Exclusiones explícitas del alcance y diseño compensatorio. {#tabla-3.16:-exclusiones-explícitas-del-alcance-y-diseño-compensatorio.}

| N° | Exclusión | Diseño Compensatorio y Convivencia Arquitectónica |
| :---- | :---- | :---- |
| **X-01** | Reemplazo del ERP central y emisión de documentos tributarios. | El ERP permanece como emisor único de DTEs. La solución actúa como enrutador y provee conciliación y foliado local para contingencias offline. |
| **X-02** | Adquisición física de etiquetas electrónicas para góndola. | Se especifica la tecnología y su costo; el diseño asume la retención del precio anterior en el POS hasta el escaneo físico manual como mitigación base. |
| **X-03** | Adquisición de dispositivos móviles para vendedores de sala. | La arquitectura asume la restricción de infraestructura existente (640 terminales para 3.820 personas) y resuelve la fricción mediante traspasos nominativos rápidos de sesión. |
| **X-04** | Desarrollo del portal interno de vendedores de Marketplace y su logística. | La integración se limita al onboarding, sincronización de stock, monitoreo de SLAs (5 KPIs) y notificación de devoluciones físicas. |
| **X-05** | Motor de cálculo contable y liquidación de remuneraciones. | Se procesa y exporta la base bruta de cálculo para atribuir comisiones cruzadas (ej. despacho desde tienda), pero el pago lo ejecuta el sistema del CLIENTE. |
| **X-06** | Sistema de cobranza judicial y ejecución de embargos. | El perímetro abarca exclusivamente el registro inmutable y la trazabilidad de las gestiones extrajudiciales y repactaciones. |
| **X-07** | Flotas y sustitución de proveedores de última milla. | Integración API para trazabilidad del ciclo de vida del despacho, excluyendo la ruteo interno de los camiones de terceros. |
| **X-08** | Obras civiles, canalización eléctrica y cableado estructurado. | El diseño entrega la planimetría y el cálculo de potencia/refrigeración; la ejecución es responsabilidad exclusiva del CLIENTE. |
| **X-09** | Adquisición de hardware (POS, red, infraestructura de edge). | Dimensionamiento y especificación técnica exhaustiva suministrada en la Oferta Técnica para la compra directa por el CLIENTE. |
| **X-10** | Contratos de telecomunicaciones de centros comerciales. | La arquitectura Edge (servidores locales) absorbe las caídas de red de terceros garantizando la autonomía comercial. |
| **X-11** | Implementación del WMS en el centro de distribución de Concepción. | La infraestructura logística se excluye como punto de promesa digital hasta que abandone el control manual basado en planillas. |
| **X-12** | Saneamiento retroactivo de la base histórica del inventario físico. | La arquitectura gestiona el margen de error conocido (12,4%) para calcular el disponible; no se ejecutarán conteos ciegos correctivos masivos fuera del modelo cíclico ABC. |

 

### **3.7.2. Supuestos** {#3.7.2.-supuestos}

Los parámetros de dimensionamiento y capacidad que condicionan la planificación se formulan como supuestos gobernables, sujetos a re-validación en la fase de levantamiento:

##### **Tabla 3.17:** Supuestos estructurales, impacto y mecanismo de validación. {#tabla-3.17:-supuestos-estructurales,-impacto-y-mecanismo-de-validación.}

| ID | Supuesto estructural | Impacto operacional | Mecanismo de validación |
| :---- | :---- | :---- | :---- |
| **S-A** | El mes 1 del contrato corresponde a enero de 2027\. | Desplazamientos que expongan los hitos de producción al congelamiento de Navidad forzarían la reprogramación total del proyecto. | Aprobación del Acta de Inicio en Mes 1\. |
| **S-B** | El evento Cyber de 2028 se fija entre mayo y junio, notificado con 6 semanas de anticipación | Un adelanto anómalo reduce la ventana de estabilización post-paso a producción (Etapa 1\) | Anuncio oficial de la Cámara de Comercio. |
| **S-C** | El core de originación (2011) soporta exposición de cupos preaprobados vía API hacia el nodo local de contingencia. | Inviabilidad técnica inhabilitaría el consumo crediticio offline en tiendas (38% de la venta) durante la Etapa 1\. | Prueba de concepto técnica (POC). |
| **S-D** | El corte de inventario para la migración se resuelve por estrategia declarada y no por conteo físico total simultáneo en las 24 instalaciones. | Un recuento físico global simultáneo en las 24 instalaciones generaría sobrecostos laborales y de horas extra no presupuestados. | Aprobación del Plan de Migración. |
| **S-E** | El sistema central de 2009 admite ser antepuesto por una capa de API Gateway sin modificar su código, y sus catorce integraciones pueden observarse y sustituirse individualmente. | La escritura clandestina en tablas elude la fachada estranguladora, obligando a emplear costosos esquemas de replicación CDC (Change Data Capture) a nivel de disco. | Auditoría del flujo piloto (Carga de Precios). |

### **3.7.3. Restricciones** {#3.7.3.-restricciones}

Restricciones de Continuidad y Operación Física (Edge Computing):

* Continuidad operacional offline estricta en infraestructura on-premise por 24 horas continuas para garantizar la venta, cobro y contingencia crediticia exigida durante 8 horas en tiendas. Para el CD Concepción, la exigencia de autonomía se fija en 4 horas.  
* Restablecimiento de red y sincronización bidireccional forzosa en un máximo de 30 minutos sin pérdida de DTEs ni solapamiento de stock.  
* Tolerancia nula a la indisponibilidad de terminales por rotación; la sesión cajero-vendedor emplea rotación de credenciales (hot-swapping).  
* Cinco ventanas de congelamiento de infraestructura inamovibles, implementadas como barreras automatizadas de CI/CD para bloquear despliegues durante peaks comerciales.

Restricciones Legales y Normativas (Zero Trust y Protección de Datos):

* Arquitectura de segregación lógica y auditoría inmutable estricta que garantice la incomunicación por defecto entre la filial de crédito y el retail comercial.  
* Inmutabilidad probatoria de largo plazo: los registros precontractuales, el timestamp de entrega de información y el consentimiento de repactación se archivan en almacenamiento frío por el plazo de vigencia de la deuda más 6 años.  
* Derivación de garantías prohibida por diseño. El flujo comercial de postventa absorbe financieramente las contingencias en primera línea, delegando la liquidación B2B al plano administrativo trasero.

Restricciones Contractuales del Proceso de Licitación:

* Plazo contractual de 56 meses y adopción obligatoria del despliegue en nube híbrida.  
* Integración auditable de cinco modelos de innovación valorizados económicamente, incluyendo algoritmos de aprendizaje automático controlados perimetralmente para no comprometer datos sensibles.  
* Censura absoluta de información tarifaria, precios unitarios y cálculos financieros en el cuerpo de la Oferta Técnica (Sobre N°2).

## **3.8. Catálogo de requerimientos funcionales core** {#3.8.-catálogo-de-requerimientos-funcionales-core}

El Anexo Técnico X consolida 223 requerimientos funcionales atomizados. Esta sección expone estrictamente el subconjunto core: aquellos requerimientos cuya omisión vulnera las restricciones innegociables del CLIENTE o bloquea la habilitación de dependencias arquitectónicas estructurales.

* Criterio de selección: Un requerimiento integra el núcleo core si (1) implementa de forma directa una de las quince restricciones no negociables, (2) materializa una decisión estructural de arquitectura, o (3) constituye un prerrequisito técnico bloqueante para el resto de su módulo.  
* Prioridad: Se aplica el marco MoSCoW. La totalidad del catálogo core está clasificado como M (Obligatorio/Must), condicionando el éxito de los pasos a producción.

### **3.8.1. Gobernanza de datos y frontera regulatoria** {#3.8.1.-gobernanza-de-datos-y-frontera-regulatoria}

##### **Tabla 3.18:** Requerimientos funcionales core de gobernanza de datos y frontera regulatoria. {#tabla-3.18:-requerimientos-funcionales-core-de-gobernanza-de-datos-y-frontera-regulatoria.}

| ID | Requerimiento | Módulo | Etapa | Trazabilidad |
| :---- | :---- | :---- | :---- | :---- |
| RF-166 | Bloquear todo intento de cruce de información que no corresponda a una interfaz declarada en el inventario de flujos autorizados. | M-21 | 1 | Restricción N°1  SUP-04  OE-11 |
| RF-165 | Registrar cada cruce ejecutado entre ámbitos indicando dato, finalidad, base de licitud, autorización nominada e instante. | M-21 | 1 | SUP-04  OE-11 |
| RF-170 | Excluir del catálogo de atributos disponibles en el motor de campañas todo atributo de origen financiero. | M-21 | 1 | Restricción N°1  SUP-04 |
| RF-174 | Resolver la correspondencia entre identificadores exclusivamente a través de la tabla custodiada en zona neutral, con acceso nominado y registrado. | M-22 | 1 | SUP-03 |

### **3.8.2. Disponibilidad e inventario** {#3.8.2.-disponibilidad-e-inventario}

##### **Tabla 3.19:** Requerimientos funcionales core de disponibilidad e inventario. {#tabla-3.19:-requerimientos-funcionales-core-de-disponibilidad-e-inventario.}

| ID | Requerimiento | Módulo | Etapa | Trazabilidad |
| :---- | :---- | :---- | :---- | :---- |
| RF-127 | Calcular la existencia disponible para vender restando de la existencia registrada las reservas vigentes, el comprometido no despachado y el colchón de confianza. | M-01 | 1 | SUP-01  OE-02 |
| RF-128 | Determinar el valor del colchón de confianza en función de la categoría del artículo. | M-01 | 1 | SUP-01  OE-02 |
| RF-157 | Impedir que cualquier canal de venta consuma el saldo bruto de inventario para publicar o comprometer existencia. | M-01 | 1 | SUP-01 |
| RF-161 | Mostrar al vendedor de piso el porcentaje de error probable junto a la disponibilidad publicada. | M-01 | 1 | SUP-01 |
| RF-137 | Calcular la exactitud de inventario resultante por categoría. | M-02 | 1 | SUP-18  OE-01 |
| RF-139 | Impedir el cierre de un ajuste de inventario que no tenga asignado un componente de merma. | M-02 | 1 | SUP-17  OE-03 |
| RF-143 | Impedir la publicación de una referencia en el canal digital mientras no cuente con los atributos obligatorios completos. | M-03 | 1 | Vacío V-03 |

### **3.8.3. Precio y evidencia fiscal** {#3.8.3.-precio-y-evidencia-fiscal}

##### **Tabla 3.20:** Requerimientos funcionales core de precio y evidencia fiscal. {#tabla-3.20:-requerimientos-funcionales-core-de-precio-y-evidencia-fiscal.}

| ID | Requerimiento | Módulo | Etapa | Trazabilidad |
| :---- | :---- | :---- | :---- | :---- |
| RF-028 | Impedir la venta de la referencia al precio nuevo mientras su punto de exhibición no confirme la actualización física. | M-06 | 1 | Restricción N°4  SUP-09  OE-04 |
| RF-023 | Cobrar el menor de ambos precios para el consumidor ante discrepancia detectada en línea de caja. | M-06 | 1 | Restricción N°4  SUP-08 |
| RF-020 | Registrar la identidad individual del ejecutor del cambio de etiqueta. | M-06 | 1 | SUP-09 |
| RF-021 | Recuperar el precio publicado de una referencia para una fecha, hora y canal determinados. | M-07 | 1 | Restricción N°4  SUP-10  OE-05 |

### **3.8.4. Pedido, cumplimiento y comisión** {#3.8.4.-pedido,-cumplimiento-y-comisión}

##### **Tabla 3.21:** Requerimientos funcionales core de pedido, cumplimiento y comisión. {#tabla-3.21:-requerimientos-funcionales-core-de-pedido,-cumplimiento-y-comisión.}

| ID | Requerimiento | Módulo | Etapa | Trazabilidad |
| :---- | :---- | :---- | :---- | :---- |
| RF-043 | Preautorizar el medio de pago al aceptar el pedido, sin capturar el cobro. | M-09 | 1 | SUP-11  OE-07 |
| RF-045 | Capturar el cobro únicamente al registrarse el evento de confirmación de la preparación física. | M-09 | 1 | SUP-11  OE-07 |
| RF-046 | Determinar automáticamente la alternativa de resolución aplicable según el motor de reglas ante quiebres de inventario. | M-09 | 1 | SUP-11 |
| RF-051 | Notificar al cliente el cambio de estado de su pedido antes de efectuar cualquier cobro definitivo. | M-11 | 1 | SUP-11  OE-07 |
| RF-052 | Permitir a todos los actores consultar el estado del pedido desde una única fuente de verdad. | M-09 | 1 | SUP-11 |
| RF-077 | Seleccionar como punto de despacho aquel de menor costo total de servir. | M-09 | 1 | SUP-13  OE-06 |
| RF-055 | Condicionar la transmisión de la base de comisión al movimiento real de inventario verificado en bodega. | M-10 | 1 | SUP-14 |

### **3.8.5. Operación de tienda y contingencia** {#3.8.5.-operación-de-tienda-y-contingencia}

##### **Tabla 3.22:** Requerimientos funcionales core de operación de tienda y contingencia. {#tabla-3.22:-requerimientos-funcionales-core-de-operación-de-tienda-y-contingencia.}

| ID | Requerimiento | Módulo | Etapa | Trazabilidad |
| :---- | :---- | :---- | :---- | :---- |
| RF-084 | Permitir al cajero cobrar la venta en modo desconectado. | M-08 | 1 | Restricción N°5  OE-12 |
| RF-086 | Emitir el documento de venta en contingencia utilizando folios previamente asignados por el ERP. | M-08 | 1 | Restricciones N°5 y N°6  Vacío V-01 |
| RF-100 | Enrutar la emisión de todo documento tributario hacia el sistema de gestión empresarial como único emisor. | M-08 | 1 | Restricción N°6  X-01 |
| RF-089 | Permitir el otorgamiento de crédito en modo desconectado exclusivamente contra cupo preaprobado vigente. | M-17 | 1 y 2 | SUP-07  Supuesto S-C |
| RF-092 | Impedir la apertura de una tarjeta nueva en modo desconectado. | M-17 | 2 | SUP-07  Restricción N°3 |
| RF-095 | Reconciliar hacia los sistemas centrales la totalidad de las ventas registradas en modo desconectado. | M-08 | 1 | OE-12 |
| RF-097 | Procesar la reconciliación de forma idempotente, impidiendo la duplicación de ventas o documentos. | M-08 | 1 | OE-12 |

### **3.8.6. Post-venta, garantía legal y marketplace** {#3.8.6.-post-venta,-garantía-legal-y-marketplace}

##### **Tabla 3.23:** Requerimientos funcionales core de postventa, garantía legal y marketplace. {#tabla-3.23:-requerimientos-funcionales-core-de-postventa,-garantía-legal-y-marketplace.}

| ID | Requerimiento | Módulo | Etapa | Trazabilidad |
| :---- | :---- | :---- | :---- | :---- |
| RF-188 | Impedir que el flujo de atención exija la derivación del consumidor al fabricante, al servicio técnico o al vendedor externo. | M-13 | 1 | Restricción N°7  SUP-21 |
| RF-198 | Impedir que el estado de la recuperación contra el tercero condicione el cierre de la resolución al consumidor. | M-14 | 1 | SUP-21 |
| RF-190 | Impedir el reingreso de una unidad devuelta al inventario disponible mientras no exista decisión de aptitud registrada. | M-13 | 1 | SUP-22 |
| RF-106 | Notificar al vendedor de marketplace la recepción de la devolución en el instante en que se registra. | M-14 | 2 | SUP-15 |
| RF-119 | Registrar el acuse de conocimiento de las reglas de evaluación por parte de cada vendedor externo. | M-12 | 2 | SUP-16 |
| RF-124 | Despublicar automáticamente la oferta cuyo stock declarado haya superado el plazo de vigencia sin actualización. | M-12 | 2 | SUP-16 |

### **3.8.7. Crédito, consentimiento y migración** {#3.8.7.-crédito,-consentimiento-y-migración}

##### **Tabla 3.24:** Requerimientos funcionales core de crédito, consentimiento y migración. {#tabla-3.24:-requerimientos-funcionales-core-de-crédito,-consentimiento-y-migración.}

| ID | Requerimiento | Módulo | Etapa | Trazabilidad |
| :---- | :---- | :---- | :---- | :---- |
| RF-199 | Exigir la entrega completa de la información precontractual antes de habilitar la evaluación de la solicitud. | M-15 | 2 | Restricción N°3  SUP-06  OE-08 |
| RF-206 | Impedir el registro de la aceptación del crédito mientras no exista acreditación de entrega previa de la información precontractual. | M-16 | 2 | Restricción N°3  SUP-06  OE-08 |
| RF-208 | Impedir el registro de una modificación de condiciones del crédito que no posea evidencia de consentimiento asociada. | M-16 | 2 | Restricción N°2  SUP-05  OE-08 |
| RF-210 | Restaurar desde archivo frío los antecedentes de una operación de crédito de cualquier cohorte dentro del plazo de retención. | M-16 | 2 | SUP-05  OE-08 |
| RF-220 | Impedir la originación de una operación cuya tasa supere la Tasa Máxima Convencional vigente. | M-15 | 2 | SUP-06 |
| RF-213 | Impedir la ejecución de una gestión de cobranza fuera de los límites normativos de horario y de medio. | M-18 | 2 | SUP-05 |
| RF-216 | Generar el reporte de conciliación diaria de saldos durante todo el proceso de migración por olas de coexistencia. | M-19 | 1 y 2 | Restricción N°8  SUP-25  OE-10 |

### **3.8.8. Accesos, evento anual y ventanas de congelamiento** {#3.8.8.-accesos,-evento-anual-y-ventanas-de-congelamiento}

##### **Tabla 3.25:** Requerimientos funcionales core de accesos, eventos anuales y congelamiento. {#tabla-3.25:-requerimientos-funcionales-core-de-accesos,-eventos-anuales-y-congelamiento.}

| ID | Requerimiento | Módulo | Etapa | Trazabilidad |
| :---- | :---- | :---- | :---- | :---- |
| RF-004 | Impedir el acceso mediante credencial compartida en líneas de caja o terminales de piso. | M-23 | 1 | Restricción N°11  SUP-24 |
| RF-013 | Revocar la totalidad de los accesos y credenciales del trabajador a partir del término efectivo de su vínculo. | M-23 | 1 | SUP-24 |
| RF-007 | Impedir la ejecución de la función de originación a un usuario sin capacitación normativa acreditada vigente. | M-23 | 2 | SUP-24 |
| RF-163 | Permitir exclusivamente al rol facultado suspender manualmente la publicación comercial de una categoría. | M-24 | 1 | SUP-23 |
| RF-185 | Bloquear por diseño la ejecución de despliegues en producción durante las ventanas de congelamiento. | M-24 | 1 | Restricción N°9 |

## **3.9. Catálogo de requerimientos no funcionales core** {#3.9.-catálogo-de-requerimientos-no-funcionales-core}

El Anexo consolida 75 requerimientos no funcionales (RNF) asociados a desempeño, resiliencia y seguridad. Esta sección expone exclusivamente aquellos **con valor numérico verificable**, los cuales gobiernan la certificación y paso a producción de cada etapa. Los valores rotulados como supuesto serán recalibrados empíricamente durante el levantamiento inicial.

## 

### **3.9.1. Desempeño y tiempo de respuesta** {#3.9.1.-desempeño-y-tiempo-de-respuesta}

##### **Tabla 3.26:** Requerimientos no funcionales core de desempeño y tiempo de respuesta. {#tabla-3.26:-requerimientos-no-funcionales-core-de-desempeño-y-tiempo-de-respuesta.}

| ID | Requerimiento | Umbral | Método de verificación |
| :---- | :---- | :---- | :---- |
| RNF-16 | Consulta de disponibilidad en la ficha de producto del canal digital. | ≤ 400 ms | Prueba de carga con perfil del evento anual y monitoreo en producción. |
| RNF-21 | Consulta de disponibilidad desde terminal compartida del piso de venta. | ≤ 2 s | Prueba en terreno sobre las 640 terminales, en tienda insignia y de calle.  |
| RNF-17 | Confirmación de un pedido durante el evento anual. | ≤ 3 s | Prueba de carga con el peak declarado.  |
| RNF-18 | Venta completa en caja con medio de pago externo. | ≤ 25 s | Medición instrumentada en peak de diciembre. |
| RNF-06 | Evaluación de una solicitud de crédito en el punto de venta físico. | ≤ 8 s (base actual: 40s a 3m) | Medición extremo a extremo en mesón y caja. |
| RNF-19 | Propagación de un cambio de precio a las 380 líneas de caja y al canal digital. | ≤ 5 min | Prueba con carga de campaña de 400.000 cambios en un día.  |
| RNF-20 | Registro de una devolución en el mesón de atención. | ≤ 60 s | Medición instrumentada con muestreo por tienda. |
| RNF-05 | Desfase entre el cambio real de estado de un pedido y su reflejo omnicanal. | Umbral declarado (\<= 30 s) | Auditoría cruzada de estado entre los cuatro canales. |

### **3.9.2. Capacidad** {#3.9.2.-capacidad}

##### **Tabla 3.27:** Requerimientos no funcionales core de capacidad operativa. {#tabla-3.27:-requerimientos-no-funcionales-core-de-capacidad-operativa.}

| ID | Requerimiento | Umbral | Método de verificación |
| :---- | :---- | :---- | :---- |
| RNF-22 | Soporte del peak digital del evento anual sin degradar los umbrales de desempeño. | 104.000 pedidos en 3 días (proyección 150.000) | Prueba de carga al 120 % del peak proyectado. |
| RNF-23 | Soporte del peak presencial de la campaña de noviembre y diciembre. | Carga concurrente sobre 380 líneas de caja | Prueba de carga presencial sostenida. |

### **3.9.3. Seguridad y frontera de datos** {#3.9.3.-seguridad-y-frontera-de-datos}

##### **Tabla 3.28:** Requerimientos no funcionales core de seguridad, resiliencia y disponibilidad. {#tabla-3.28:-requerimientos-no-funcionales-core-de-seguridad,-resiliencia-y-disponibilidad.}

| ID | Requerimiento | Umbral | Método de verificación |
| :---- | :---- | :---- | :---- |
| RNF-28 | Operación desconectada autónoma del componente on-premise. | ≥ 24 h continuas | Prueba de desconexión prolongada del nodo físico. |
| RNF-24 | Operación comercial de tienda sin enlace externo (venta y cobro efectivos). | ≥ 8 h continuas | Corte real del enlace en tienda piloto, en horario comercial. |
| RNF-25 | Operación del centro de distribución principal sin enlace externo. | ≥ 4 h continuas | Prueba de desconexión programada. |
| RNF-26 | Sincronización tras la reconexión de sucursal. | ≤ 30 min (tras 8 h de desconexión) | Prueba de reconexión cronometrada. |
| RNF-27 | Integridad de la sincronización. | 0 ventas y 0 DTE perdidos/duplicados | Cuadratura del universo transaccional tras la contingencia. |
| RNF-32 | Objetivos de recuperación ante desastre. | RTO ≤ 4 h  RPO ≤ 15 min | Ejercicio semestral de conmutación real. |
| RNF-30 | Disponibilidad del canal digital. | 24x7x365 (≥ 99,9 %) | Monitoreo mensual contra el SLA contractual. |
| RNF-31 | Disponibilidad de servicios financieros (pagos, estados de cuenta, bloqueos). | 24x7x365 (≥ 99,9 %) | Monitoreo segregado reportado a la filial emisora. |

### **3.9.4. Retención, trazabilidad y migración** {#3.9.4.-retención,-trazabilidad-y-migración}

##### **Tabla 3.29:** Requerimientos no funcionales core de retención, trazabilidad y migración. {#tabla-3.29:-requerimientos-no-funcionales-core-de-retención,-trazabilidad-y-migración.}

| ID | Requerimiento | Umbral | Método de verificación |
| :---- | :---- | :---- | :---- |
| RNF-42 | Conservación de los antecedentes e historial del crédito. | Plazo del crédito \+ 6 años | Pruebas de recuperación de archivo frío. |
| RNF-57 | Recuperación de la evidencia de consentimiento de operaciones históricas. | ≤ 5 min | Recuperación por muestreo censal auditado. |
| RNF-44 | Retención de la trazabilidad del precio publicado por canal. | 3 años | Auditoría de política de ciclo de vida de datos. |
| RNF-58 | Recuperación del precio publicado en fecha, hora y canal arbitrarios. | ≤ 1 min (sobre ventana de 3 años) | Consultas índice sobre el histórico inmutable. |
| RNF-10 | Divergencia de saldos durante migración de cartera financiera. | 0 divergencias no conciliadas | Freno automático (circuit breaker) ante excepciones. |

### **3.9.5. Precisión sobre Continuidad y Métricas de Negocio** {#3.9.5.-precisión-sobre-continuidad-y-métricas-de-negocio}

El diseño arquitectónico distingue estrictamente la continuidad de infraestructura de la continuidad comercial. El RNF-28 exige 24 horas de autonomía ininterrumpida para el nodo físico *on-premise*, protegiendo el almacenamiento local. Sobre esa infraestructura se despliega el RNF-24, que delimita la ventana de 8 horas exigida para sostener operativamente la venta, el cobro y la contingencia de crédito en la sala de la sucursal.

Asimismo, las metas de exactitud de inventario o tasa de cancelación no se tabulan como requerimientos no funcionales aislados, ya que su éxito depende de la conjunción entre el software entregado y la ejecución operativa del CLIENTE (conteo físico en sala, clasificación de mermas). Su cumplimiento se gestiona mediante los Criterios de Aceptación y Objetivos de Negocio del proyecto global. 

## **3.10. Estrategia para obtener el apoyo de los grupos de interés clave** {#3.10.-estrategia-para-obtener-el-apoyo-de-los-grupos-de-interés-clave}

**Estrategia para el vendedor comisionista:** El vendedor de sala opera  bajo escasez de recursos y su remuneración depende directamente de la fluidez del sistema. Si el nuevo sistema es percibido como un obstáculo este será evadido. La estrategia para este grupo se basa en 3 pilares.

* **Protección de la comisión (M10):** Mediante la implementación del módulo de atribución de venta, se garantiza que el vendedor no pierda su comisión cuando una unidad de su sala sea despachada para un pedido web, ni cuando se realice una venta presencial con inventario en otra sucursal.  
* **Reducción de tiempo en la evaluación crediticia:** El principal motivo actual de evasión por parte de los vendedores es que los procesos de cumplimiento normativo son excesivamente lentos. Actualmente, la evaluación crediticia tarda entre 40 segundos y 3 minutos. En un entorno de alta demanda, un cliente apurado con fila detrás frecuentemente prefiere no realizar la compra o cerrarla con otro medio de pago debido al tiempo de espera, lo que se traduce en una pérdida directa de la comisión por colocación financiera. La solución tecnológica propuesta reduce el tiempo de evaluación a ≤ 8 segundos ( M-15) y embebe el registro de la información precontractual y el consentimiento como un requisito sistémico bloqueante, sin añadir clics adicionales ni requerir firmas en papel (M-16). De este modo, el cumplimiento normativo se vuelve "invisible" para el vendedor: ya no le cuesta tiempo, no penaliza su productividad comercial y, por lo tanto, desaparece el incentivo perverso para evitarlo.

**Estrategia para las jefaturas de Tienda:** El dolor principal de los gerentes y jefes de local es la perdida de control sobre sus indicadores. por ejemplo la merma se ve como un número agregado; no puede aislar hurto vs descuadre administrativo , La discrepancia de inventario , Conteo que paraliza la operación.

* **Empoderamiento sobre los KPIs locales (M-02  Gestión de Inventario)**: se apalancará su apoyo demostrando cómo el M-02 les permitirá, por primera vez, aislar el descuadre administrativo del hurto real, protegiendo el indicador de merma de su tienda y su desempeño ante la gerencia.  
* **Comisión y venta de la sala protegidas:** La imputación al origen (**M-10, SUP-12 / SUP-14**) resuelve el conflicto del despacho omnicanal. Se elimina la fricción de tener que "sacarle al vendedor de la mano" una unidad para despacharla a otra ciudad, perdiendo la comisión y bajando la venta del local.  
* **Control sobre personal externo:** Para mitigar el riesgo de tener decenas de repositores externos operando diariamente en la sala, se delegará el control de accesos a los proveedores a través del IAM (**M-23**). Esto libera a la jefatura de la carga administrativa y de seguridad de gobernar credenciales ajenas. 

**Estrategia para los vendedores del marketplace:** El dolor principal de los 310 vendedores externos es operar en un entorno de total oscuridad transaccional no saben que sucede con su pedido después de realizar su despacho. Sufren por devoluciones que quedan inmovilizadas en bodegas de Ancoa sin previo aviso hasta que impactan sus liquidaciones, y por la incertidumbre de su evaluación operativa no existe un método por los cuales los evalúen . Su exigencia es concreta: "saber en qué estado está cada pedido mío, enterarme de una devolución cuando ocurre y saber con qué regla me miden". El apoyo de este grupo se asegurará mediante previsibilidad y transparencia: 

* **Estado del pedido y aviso de devolución en tiempo real**: A través del M-14 , se implementa una notificación transaccional que se dispara en el momento exacto de la recepción física del producto en la tienda. Esto resuelve directamente su exigencia de "enterarme de una devolución cuando ocurre" (y no a fin de mes con la nota de crédito), registrando la responsabilidad financiera y física del activo de manera inmediata.   
* **Reglas de medición conocidas y predecibles:**La aceptación digital de políticas fija las reglas del juego y el ranking por cinco KPIs (cancelación, puntualidad, devoluciones, lead time y calidad de catálogo) hace visible y predecible la evaluación que hoy no existe. El vendedor sabe con exactitud qué se le mide y con qué consecuencia, premia a quienes rinden y sanciona de forma sistémica a quienes degradan el servicio, eliminando la arbitrariedad. 

**Estrategia para la Gerencia del Negocio Financiero:** La Gerencia del Negocio Financiero y la Contraloría enfrentan una exposición regulatoria crítica debido a que los procesos actuales dependen de la correcta ejecución manual, lo cual imposibilita demostrar la probidad de las operaciones ante el ente fiscalizador. A esto se suma el riesgo sistémico de obsolescencia tecnológica y el vencimiento del plan de remediación normativo fijado para 2029\. Ambas áreas reconocen la tensión estructural entre la necesidad comercial de vender rápidamente en caja y la obligación legal de entregar información previa al contrato. 

* **Acreditación inmutable del consentimiento**: Ante la máxima regulatoria de que *"un consentimiento que no se puede acreditar es un consentimiento que no existe"*, el Gestor de Evidencia (M-16) elimina la vulnerabilidad de los 1.240 casos sin respaldo. Implementa un expediente digital estructurado, sellado criptográficamente y custodiado en almacenamiento inmutable por todo el ciclo de vida del crédito más el periodo legal de retención.   
* **Frontera de datos técnica y auditable:** Ante la preocupación por el uso comercial del comportamiento de pago, el **Gobierno de Frontera (M-21)** define reglas estrictas: qué se puede cruzar, con qué base legal y bajo qué control técnico. Deniega por omisión cualquier consulta no autorizada y registra cada evento de forma inalterable, cumpliendo la condición fundamental de la contralora: *"que quede escrito y auditable"*.   
* **Migración de cartera mitigada:** Asumiendo que trasladar a 620.000 clientes con saldo *"no es una migración de datos: es una operación de alto riesgo"*, el **M-19 (Migración de Cartera)** descarta el corte abrupto. Ejecuta el traslado mediante olas de coexistencia con conciliación diaria, utilizando un umbral de discrepancia como freno automático de avance. Esto asegura el cumplimiento del hito regulatorio de 2029 sin exponer a la entidad financiera.

**Estrategia para la Gerencia de Canales Digitales:** El principal punto de dolor de esta gerencia es la vulnerabilidad de su promesa comercial, al verse forzada a publicar y transaccionar sobre existencias que no tienen respaldo físico real. Esta situación derivó en la crisis operativa del evento de junio, donde miles de pedidos debieron ser cancelados por falta de stock. Se conoce que el registro logístico posee un margen de error basal del 12 %, pero los intentos de restringir la exposición del inventario para evitar quiebres chocan con la resistencia interna por el temor a disminuir las ventas inmediatas.

* **Disponibilidad con grado de confianza:** Para resolver el problema de las ventas sobre inventario inexistente, el Motor de Disponibilidad (M-01) transforma la manera en que se compromete el stock. En lugar de ofrecer unidades a ciegas asumiendo el registro central como absoluto, el motor calcula un colchón dinámico y expone la disponibilidad acompañada de un índice de confianza estadística. Esto le entrega a la gerencia exactamente la palanca de control que requiere: la capacidad de parametrizar el nivel de exposición al riesgo comercial por categoría, tomando decisiones informadas para proteger la promesa de entrega.   
* **Gobernanza y depuración del marketplace:** Para solucionar la incapacidad de gestionar el desempeño de los actores externos, el Seller Center (M-12) automatiza el control de calidad y las reglas del ecosistema. El módulo evalúa de forma continua cinco indicadores clave de nivel de servicio de los vendedores externos y ejecuta rutinas de suspensión sistémica escalonada sobre aquellos que degradan la experiencia de compra. Esto protege la reputación del dominio principal y estandariza la calidad exigida para operar bajo la marca de la compañía.  
* **Protección proactiva del evento anual masivo:** Considerando que las fechas de los grandes eventos de comercio electrónico son fijadas por entidades gremiales externas con plazos de preaviso acotados y no modificables, la plataforma no puede depender de escalamientos puramente reactivos ante picos de 104.000 pedidos. El módulo de Observabilidad y Degradación Controlada **(M-24)** garantiza que las variaciones extremas de tráfico se gestionen mediante protocolos técnicos predefinidos. Esto asegura que la plataforma degrade funciones accesorias de forma controlada antes de colapsar, protegiendo la transacción y evitando las cancelaciones masivas. 


## **3.11. Criterios de aceptación del alcance comprometido** {#3.11.-criterios-de-aceptación-del-alcance-comprometido}

La aceptación no se declara por la entrega de un artefacto sino por la verificación de un hecho observable. Un entregable producido, documentado y presentado en plazo no se da por recibido si el comportamiento que debía habilitar no se demuestra con evidencia objetiva.

El modelo opera en tres niveles encadenados y no sustituibles entre sí: aceptación por entregable, que verifica conformidad técnica; aceptación por marcha blanca, que verifica comportamiento en operación real; y aceptación por resultado de negocio, que verifica que la plataforma efectivamente movió los indicadores que motivaron la licitación. Superar el primer nivel no anticipa el segundo, y superar los dos primeros no exime del tercero.

### **3.11.1. Nivel 1: aceptación por entregable** {#3.11.1.-nivel-1:-aceptación-por-entregable}

Cada entregable se somete a revisión formal de la Contraparte Técnica y se acepta mediante acta suscrita, previa concurrencia de cuatro condiciones: el artefacto conforme a lo especificado; la evidencia objetiva de su verificación, no la declaración de haberla ejecutado; la trazabilidad explícita hacia los requerimientos del catálogo que satisface, incluyendo el módulo y la etapa a que pertenece; y el cierre documentado de las observaciones formuladas en revisiones previas.

La aceptación de un entregable que dependa de otro no procede mientras el precedente permanezca observado. Esta regla es la que impide que la cadena de dependencias declarada en el numeral 3.6.1 se rompa por conveniencia de calendario.

### **3.11.2. Nivel 2: aceptación de la marcha blanca** {#3.11.2.-nivel-2:-aceptación-de-la-marcha-blanca}

El cierre de cada marcha blanca meses 13 a 15 para la Etapa 1, meses 19 y 20 para la Etapa 2 exige el cumplimiento copulativo de las seis condiciones siguientes. La ausencia de cualquiera de ellas impide el paso a producción.

##### **Tabla 3.30:** Condiciones obligatorias para el cierre y aceptación de la marcha blanca. {#tabla-3.30:-condiciones-obligatorias-para-el-cierre-y-aceptación-de-la-marcha-blanca.}

| N° | Condición de cierre | Verificación |
| :---- | :---- | :---- |
| **1** | Ningún incidente abierto de severidad crítica o alta atribuible a la solución. | Registro de incidentes con clasificación acordada y trazabilidad de cierre. |
| **2** | Volumen de operación real comprometido alcanzado y sostenido durante al menos las cuatro últimas semanas del período. | Telemetría de producción contrastada con el perfil transaccional declarado. |
| **3** | Indicadores de disponibilidad y de tiempo de respuesta cumplidos de forma sostenida en ese mismo lapso, no en mediciones aisladas. | Medición continua contra los umbrales del numeral 3.9. |
| **4** | Conciliación sin diferencias no explicadas contra los registros del sistema vigente. | Cuadratura de universos, ejecutada diariamente durante el período. |
| **5** | Personal del CLIENTE capacitado y certificado en los procesos afectados, considerando el perfil de rotación declarado. | Registro de capacitación con evaluación de competencia posterior. |
| **6** | Mecanismo de reversión probado y operativo, con ensayo ejecutado en ambiente equivalente. | Acta del ensayo de reversión, con tiempo efectivo medido. |

Dos condiciones adicionales se aplican de forma específica a la Etapa 2 y responden a restricciones no negociables: la aceptación no procede sin el informe de auditoría independiente que acredite la separación de dominios sin hallazgos críticos abiertos, y no procede sin la conciliación diaria de saldos de la cartera cerrada sin divergencias pendientes.

### **3.11.3. Nivel 3: aceptación por resultado de negocio** {#3.11.3.-nivel-3:-aceptación-por-resultado-de-negocio}

Los criterios de este nivel son los que el caso define como razón de la licitación. Se miden sobre operación real, con la línea base declarada por la propia compañía, y se distinguen según el reparto de responsabilidad establecido en el numeral 3.5.3.

##### **Tabla 3.31:** Criterios de aceptación por resultado de negocio y metas comprometidas. {#tabla-3.31:-criterios-de-aceptación-por-resultado-de-negocio-y-metas-comprometidas.}

| Resultado comprometido | Línea base | Umbral de aceptación | Momento de medición | Responsabilidad |
| :---- | :---- | :---- | :---- | :---- |
| **Discrepancia de inventario detectada en conteo cíclico** | 12,4 % de las referencias auditadas | ≤ 2 % por categoría, sostenido en dos ciclos consecutivos | Cierre del mes 36 | Compartida |
| **Cancelación de pedidos por falta de existencia** | 1,9 % anual; 2,7 % en el evento de junio de 2026 | ≤ 0,3 % anual y cero cancelaciones por quiebre durante el evento anual | Desde el mes 16, medición mensual | Compartida |
| **Merma desagregada por causa atribuible** | 0 % de los ajustes clasificados | 100 % de los ajustes clasificados, con informe mensual cuadrado contra contabilidad | Desde el mes 16 | Sistémica |
| **Discrepancia entre precio exhibido y precio cobrado** | 11 % en la fiscalización de febrero de 2026 | ≤ 0,5 %, verificado por muestreo propio | Desde el mes 16 | Compartida |
| **Acreditación del precio publicado en un instante arbitrario** | Capacidad inexistente | 100 % de las consultas resueltas dentro del umbral, sobre ventana de tres años | Desde el mes 16 | Sistémica |
| **Cumplimiento de la fecha de entrega comprometida** | 81 % de los pedidos | ≥ 97 %, medido por pedido individual y no por promedio de canal | Cierre del mes 36 | Compartida |
| **Cobro sostenido sobre pedido no cumplible** | Captura al aceptar el pedido | Cero casos | Desde el mes 16 | Sistémica |
| **Operaciones de crédito sin evidencia recuperable de consentimiento** | 1.240 repactaciones de 2025 | Cero operaciones, con retención acreditada y recuperación demostrada | Desde el mes 21 | Sistémica |
| **Tiempo de evaluación crediticia en punto de venta** | Entre 40 segundos y 3 minutos | ≤ 8 segundos en percentil 95, sin incremento del tiempo total de atención | Desde el mes 21 | Sistémica |
| **Migración de la cartera activa** | 620.000 clientes en plataforma sin soporte desde 2029 | 100 % migrado con cero divergencias no conciliadas | Antes del cierre de 2029 | Sistémica |
| **Cruces de información entre ámbitos registrados** | Registro inexistente | 100 % de los cruces registrados y auditoría sin hallazgos críticos  | Antes del mes 16 | Sistémica |
| **Continuidad de venta y cobro ante pérdida de enlace** | Detención de la operación | ≥ 8 horas de operación autónoma con reconciliación íntegra | Desde el mes 16 | Sistémica |

### **3.11.4. Criterios de aceptación de naturaleza cualitativa** {#3.11.4.-criterios-de-aceptación-de-naturaleza-cualitativa}

Cuatro criterios del caso no admiten expresión numérica y se verifican por observación directa. Se adoptan como criterios de aceptación de pleno derecho y no como ilustración del propósito del proyecto.

##### **Tabla 3.32:** Criterios de aceptación cualitativa y forma de verificación. {#tabla-3.32:-criterios-de-aceptación-cualitativa-y-forma-de-verificación.}

| Criterio | Forma de verificación |
| :---- | :---- |
| Ningún consumidor es derivado al fabricante, al servicio técnico o al vendedor externo como condición para que se le atienda una garantía legal. | Programa de cliente oculto ejecutado en las 22 tiendas, con resultado cero derivaciones. |
| Una clienta con un pedido en curso conoce su estado real sin necesidad de contactar reiteradamente a la compañía, y es informada antes de cualquier cobro definitivo. | Auditoría del estado único del pedido y de la trazabilidad de notificaciones, contrastada con el registro de contactos entrantes por el mismo caso. |
| Una jefatura de tienda puede demostrar qué proporción de su diferencia de inventario corresponde a error de registro y no a pérdida física. | Revisión del informe mensual de merma desagregada con una jefatura de tienda real, verificando que la explicación se sostiene con los datos del sistema. |
| Un vendedor abre una tarjeta en menos tiempo que hoy sin que el cliente reciba menos información precontractual. | Medición comparada de tiempo de atención y auditoría censal de la constancia de entrega precontractual del mismo período. |

### **3.11.5. Reparto de responsabilidad y arbitraje del incumplimiento** {#3.11.5.-reparto-de-responsabilidad-y-arbitraje-del-incumplimiento}

Cuatro de los resultados del numeral 3.11.3 dependen conjuntamente de la plataforma entregada y de la ejecución operativa del CLIENTE: la plataforma provee el algoritmo de disponibilidad, la ruta de recambio de etiquetas y el orquestador de pedidos, pero el conteo, el escaneo y la preparación física los ejecuta el personal de sala. El acta de aceptación de cada uno de estos indicadores aislará el componente atribuible al sistema del componente atribuible a la adopción, y su medición se ejecuta primero sobre un piloto acotado de categorías, de modo que la desviación se detecte sobre un universo controlado antes del escalamiento.

Ante el incumplimiento de un criterio, el procedimiento es escalonado y no discrecional. En el nivel de entregable, la observación suspende la aceptación y abre plazo de subsanación, sin que ello habilite el avance de los entregables dependientes. En el nivel de marcha blanca, el incumplimiento de cualquiera de las condiciones copulativas impide el paso a producción y desplaza el hito, con la salvedad de que ningún desplazamiento puede reubicar una puesta en producción dentro de una ventana de congelamiento. En el nivel de resultado de negocio, el incumplimiento activa un plan de remediación conjunto con causa atribuida, cuya ejecución se somete a los mismos criterios de verificación.

Ninguna aceptación puede otorgarse de forma tácita por el transcurso del plazo, ni durante una ventana de congelamiento, ni de manera condicional sujeta a compromisos posteriores.

# **REFERENCIAS** {#referencias}

#  

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# 

# **DECLARACIÓN USO IA** {#declaración-uso-ia}

#  

El equipo declara que el uso de herramientas de inteligencia artificial generativa en este subdocumento se limitó a las actividades indicadas en la siguiente tabla. Todo contenido, dato, cálculo, decisión de diseño, diagrama, conclusión y referencia fue revisado y verificado por las personas identificadas, quienes asumen como propio el resultado final y la responsabilidad íntegra sobre su exactitud, originalidad y coherencia técnica.

| Sección  | Herramienta | Finalidad de uso  | Nivel en texto  | Nivel en diagramas | Revisión humana  |
| :---- | :---- | :---- | ----- | ----- | :---- |
| \[Sección o capítulo\] | \[Herramienta y versión / No aplica\] | \[Uso concreto / No se utilizó IA\] | \[Seleccione\] | \[Seleccione\] | \[Nombre y verificación realizada\] |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

A continuación, se detalla la escala de niveles para completar la tabla anterior.

| Nivel | Texto | Diagramas |
| ----- | ----- | ----- |
| **Ninguno** | Sin uso de IA. | Sin uso de IA. |
| **Bajo** | Corrección ortográfica, de estilo o reformulación de frases escritas por el grupo. | Sugerencias de formato o disposición sobre un diagrama elaborado por el grupo. |
| **Medio** | Borradores o síntesis de partes que el grupo reescribió y verificó. | Diagrama generado con asistencia (por ejemplo, código Mermaid o PlantUML) a partir de un modelo definido por el grupo. |
| **Alto** | Texto generado sustancialmente por IA y editado por el grupo. | Diagrama generado sustancialmente por IA. |

# 

[image1]: <data:image/png;base64,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>