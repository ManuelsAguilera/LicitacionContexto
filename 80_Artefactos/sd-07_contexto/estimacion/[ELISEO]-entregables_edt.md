# Entregables de la EDT — sd-07 (documento de trabajo)

Documento de trabajo. No es entregable. No es fuente de las Bases.

Insumo de la sección 7.1 (EDT con el 100 % del alcance y diccionario de paquetes) del subdocumento 7 y del Formulario T-14. Cubre innovación, seguridad, calidad, migración e implantación; cada paquete de último nivel es estimable y asignable.

Fundamento: PMBOK 6.ª edición (Crear la EDT, regla del 100 %, diccionario por paquete), apoyo de clase FEP02 (diapositivas 52, 55, 56, 57). Fuentes contractuales: Bases Administrativas Arts. 17, 18, 57.2, 71, 72; Comunicado 10 §7.1; T-14, T-15, T-19; catálogo RT de `Bases_Transversales.md`.

Convención de código: `1.0` raíz; ramas `1.1`–`1.15`; paquetes `1.N.M`. Los códigos son provisorios: se re-secuencian al congelar la EDT para T-14.

Marcas: **[Nuevo]** = incorporado desde `entregables-actualizado.md` (2ª lista, Ronda 0, 120 entregables). El paréntesis indica el código en esa lista; no confundir con los códigos `1.15.x` propios de la rama de Operación.

Nombres según reglas de Ronda 0: sustantivo/resultado (nunca actividad), tipo de entregable en el nombre, un nombre un entregable, se entiende sin códigos externos, ámbito cuando importa.

---

## 1.0 EDT — Transformación Omnicanal Multitienda Ancoa (56 meses)

### 1.1 Dirección, gobierno y control del proyecto — 9 paquetes

- 1.1.1 Plan de dirección integrado (ámbito, cronograma, costos, calidad, riesgos, comunicaciones, interesados, adquisiciones)
- 1.1.2 EDT y diccionario con entregable, criterio de aceptación y responsable por paquete (T-14)
- 1.1.3 Control integrado de cambios (Art. 72) con medición EVM; registro de riesgos y de lecciones
- 1.1.4 Registro de supuestos (25 decisiones pendientes) y de vacíos/consultas (15 materias)
- 1.1.5 Calendario de ventanas de congelamiento y eventos anuales con declaración de impacto por evento
- 1.1.6 Actas de los 5 comités (Art. 71), informe mensual de avance (RT-19.06) y reporte FinOps mensual (Art. 16.3)
- 1.1.7 Actas de aceptación por hito (Art. 18) y habilitación de pagos E-25; seguimiento de garantías, seguros y certificados laborales (Art. 75.3)
- 1.1.8 Acta de constitución del proyecto **[Nuevo]** (Ronda 0: 2.1)
- 1.1.9 Línea base de costos y presupuesto **[Nuevo]** (Ronda 0: 2.9) — nombre sin cifras (RR-08); los valores viven solo en la oferta económica

### 1.2 Levantamiento y línea base de alcance (hito H1) — 7 paquetes

- 1.2.1 Mapa AS-IS de las 14 interfaces punto a punto — entrega temprana
- 1.2.2 Inventario de las 9 plataformas, 6 proveedores y dependencias
- 1.2.3 Levantamiento de procesos, reglas de negocio y volumetría declarada
- 1.2.4 Catálogo de requerimientos (RF/RNF/OP) trazado al origen
- 1.2.5 Matriz de trazabilidad origen → requerimiento → componente → paquete EDT → prueba → criterio
- 1.2.6 Línea base de alcance: Etapa 1/2 con criterios de asignación, exclusiones y supuestos
- 1.2.7 Estudios de decisión con costeo: etiqueta electrónica, WMS/equipo CD Concepción, destino de plataformas

### 1.3 Arquitectura y diseño (hito H2, mes 4) — 7 paquetes

- 1.3.1 Documento de arquitectura ISO 42010 (5 vistas) y catálogo de ADR
- 1.3.2 Arquitectura física con emplazamiento por componente justificado (Art. 16.2) — zonas a nombrar conforme a sd-04
- 1.3.3 Modelo de datos con dominios segregados Retail/Emisor, frontera documentada y políticas de retención (RT-05.10)
- 1.3.4 Diseño de integración: contratos OpenAPI/AsyncAPI, versionado y gobierno
- 1.3.5 Especificación del modo desconectado (8 h tienda / 4 h CD) y sincronización ≤30 min (RT-03.13)
- 1.3.6 Modelo de capacidad y dimensionamiento actualizado
- 1.3.7 Especificación y costeo de obras de infraestructura del cliente **[Nuevo]** (Ronda 0: 1.28) — canalizaciones y obras civiles: el CLIENTE ejecuta, el proponente especifica, costea, coordina y certifica

### 1.4 Infraestructura híbrida y plataforma base (hito H3, mes 6) — 16 paquetes

- 1.4.1 Entorno cloud multi-zona con IaC versionado, subredes privadas y etiquetado FinOps
- 1.4.2 Entorno on-premise/edge por sitio: gabinete por tienda, sitio principal, enlace redundante, RAID y endurecimiento CIS
- 1.4.3 Entorno dedicado del ámbito emisor con segregación física/lógica acreditada
- 1.4.4 Ambientes DEV/QA/PREPROD/PROD (+DR) habilitados
- 1.4.5 Malla de integración y plataforma de observabilidad unificada OpenTelemetry con catálogo de alertas
- 1.4.6 Especificación de hardware y dispositivos de terreno para adquisición del CLIENTE (T-11)

**Centro de datos principal (140 m²)**

- 1.4.7 Plano y especificación del recinto técnico del centro de datos — distribución interna, obra civil y blindaje **[Nuevo]** (Ronda 0: 1.15.3)
- 1.4.8 Plan de cierre de brecha del centro de datos frente al informe interno de 2024 **[Nuevo]** (Ronda 0: 1.15.4)
- 1.4.9 Sistema de energía ininterrumpida y generación autónoma de 24 h del centro de datos **[Nuevo]** (Ronda 0: 1.15.5)
- 1.4.10 Sistema de climatización de precisión N+1 con monitoreo ambiental del centro de datos **[Nuevo]** (Ronda 0: 1.15.6)
- 1.4.11 Sistema de detección temprana y extinción automática de incendios del centro de datos **[Nuevo]** (Ronda 0: 1.15.7)
- 1.4.12 Control de acceso físico biométrico y videovigilancia del centro de datos **[Nuevo]** (Ronda 0: 1.15.8)
- 1.4.13 Espacio de operación del personal habilitado, separado de la sala de equipos **[Nuevo]** (Ronda 0: 1.15.11)

**Respaldos**

- 1.4.14 Solución de respaldo 3-2-1-1-0 operando **[Nuevo]** (Ronda 0: 1.15.15)
- 1.4.15 Servicio de custodia de medios de respaldo del centro de datos **[Nuevo]** (Ronda 0: 1.15.12)

**Tiendas**

- 1.4.16 Red segmentada (cajas, administración, videovigilancia y wifi de clientes) en las 13 tiendas que no la tienen **[Nuevo]** (Ronda 0: 1.15.20)

Nota: "operando" significa en servicio y probado; hardware y obras son del cliente.

### 1.5 Desarrollo de software (software E1 → H4/QA; software E2 → H9) — 10 paquetes

- 1.5.1 Retail: catálogo, precios y promociones (motor hoy inexistente) con histórico de precio
- 1.5.2 Retail: inventario, exactitud y abastecimiento (conteo cíclico, merma en 5 causas)
- 1.5.3 Retail: pedidos omnicanal con estado único, reserva y asignación por costo
- 1.5.4 Retail: ventas y caja con operación offline; comisiones
- 1.5.5 Retail: marketplace, posventa, garantía sin derivación y fidelización
- 1.5.6 Financiero: originación (≤8 s), cartera, cobranza, repactación y evidencia de consentimiento
- 1.5.7 Frontera X-01: autorización, auditoría y registro de todo cruce Retail↔Emisor (RT-16.09)
- 1.5.8 Canales digitales: portales público/cliente/vendedor/proveedor y app móvil en 5 perfiles
- 1.5.9 Capa analítica, tableros de negocio y automatizaciones (RT-05 analítico, RT-14.02, RT-18)
- 1.5.10 Plataforma DevSecOps: CI/CD, IaC y automatización de pruebas

### 1.6 Integraciones (rediseño de las 14) — 7 paquetes

- 1.6.1 Catálogo de interfaces rediseñadas con contratos y niveles de servicio de integración
- 1.6.2 Integraciones por dominio: precios/existencia (réplica ≤5 min), existencia ≤30 s, pedidos, crédito↔ERP, marketplace, cobranza, fidelización, prevención de pérdidas
- 1.6.3 Integraciones externas: transportistas, 940 proveedores y reportes a autoridades
- 1.6.4 Certificación de integraciones con evidencia de conciliación
- 1.6.5 Conector con el WMS principal operando **[Nuevo]** (Ronda 0: 1.18c)
- 1.6.6 Conector con la plataforma de comercio electrónico operando **[Nuevo]** (Ronda 0: 1.22)
- 1.6.7 Conector con el sistema de remuneraciones — base de comisión, operando **[Nuevo]** (Ronda 0: 1.24)

### 1.7 Migración y saneamiento de datos — 11 paquetes

- 1.7.1 Plan de migración con estrategia de corte y retorno (RT-05.11)
- 1.7.2 Inventario de datos históricos a migrar (RT-05.15)
- 1.7.3 Maestro de artículos saneado y validado (268.000 referencias)
- 1.7.4 Corte de inventario en 24 instalaciones que no cierran
- 1.7.5 Migración de histórico: venta 6 años, pedidos 3 años, padrón deduplicado, vendedores y liquidaciones
- 1.7.6 Migración de cartera viva (620.000 clientes) con convivencia, conciliación diaria, retorno probado y comunicación
- 1.7.7 Actas de conciliación dual-run y cuadratura pre/post migración
- 1.7.8 Repositorio de consulta de datos históricos no migrados **[Nuevo]** (Ronda 0: 1.30)
- 1.7.9 Plan de retiro de la plataforma de originación y cobranza de 2011 **[Nuevo]** (Ronda 0: 3.11)
- 1.7.10 Plataforma de originación y cobranza de 2011 fuera de servicio **[Nuevo]** (Ronda 0: 1.17b)
- 1.7.11 Sistema central de retail de 2009 retirado **[Nuevo, condicionado]** (Ronda 0: 1.19) — condicionado a la decisión de escenario del sd-03 (Escenario A/B); ver Pendientes 5

### 1.8 Seguridad, identidad y cumplimiento — 7 paquetes

- 1.8.1 Plan de seguridad, modelado de amenazas (STRIDE) y matriz de controles
- 1.8.2 Declaración de superficie de exposición y plan de respuesta a incidentes
- 1.8.3 Modelo de identidad, matriz de roles y segregación de funciones (incl. ámbito emisor)
- 1.8.4 Cifrado y tokenización de medios de pago; protección de datos personales (Ley 21.719)
- 1.8.5 Matriz de cumplimiento normativo con control y evidencia (Art. 27)
- 1.8.6 Informe de pruebas de intrusión y plan de remediación (insumo de H5)
- 1.8.7 Informe de diligencia reforzada del proveedor de nube **[Nuevo]** (Ronda 0: 3.13) — origen RAN 20-7 (CMF); se declara como buena práctica verificable, no como norma vigente

### 1.9 Calidad, pruebas y certificación — 6 paquetes

- 1.9.1 Plan de pruebas (T-13): niveles, tipos, ambientes, datos y calendario
- 1.9.2 Puertas de calidad: análisis estático, cobertura y umbrales (ISO 25010)
- 1.9.3 Batería de pruebas: funcionales, RNF, carga, resiliencia, recuperación y seguridad (ISO 29119)
- 1.9.4 Informes de UAT y verificación de los 28 criterios de aceptación del caso
- 1.9.5 Certificación Etapa 1 (H5) y Certificación Etapa 2 (H10)
- 1.9.6 Estándares de codificación y checklist de revisión por pares **[Nuevo]** (Ronda 0: 3.2a)

### 1.10 Innovaciones (5 — una por tipo; paquetes a confirmar con T-19) — 5 paquetes

- 1.10.1 … 1.10.5 Un paquete por innovación con tipo declarado, mes e indicador con línea base y meta (RT-26.02). Candidatas del equipo ajeno — validar pertinencia y no duplicidad de tipo: captura RFID de inventario (fuerte: 12,4 % y "contar sin cerrar"), búsqueda semántica/recomendación, fila virtual/autoservicio, lockers, retail media (pertinencia débil, requiere hardware del CLIENTE)

### 1.11 Implantación y despliegue (T-18) — 5 paquetes

- 1.11.1 Plan de implantación y puesta en marcha (T-18) con criterios de éxito medibles
- 1.11.2 Pipeline de despliegue azul-verde/canario y procedimiento de reversión probado
- 1.11.3 Habilitación de sitios: 22 tiendas, 2 CD, 380 líneas de caja, 640 terminales, edge por tienda
- 1.11.4 Estrategia de degradación y suspensión de publicación por categoría para el evento anual
- 1.11.5 Convivencia Etapa 1/Etapa 2 con única fuente de verdad (meses 19–20)

### 1.12 Marcha blanca y pasos a producción — 5 paquetes

- 1.12.1 Marcha blanca Etapa 1 (13–15): operación supervisada, medición diaria, conciliación y reversión activa
- 1.12.2 Evidencia de cierre 17.3 (6 condiciones) y acta de aceptación E1 (H7, mes 16)
- 1.12.3 Marcha blanca Etapa 2 (19–20) en convivencia con E1 en producción
- 1.12.4 Aceptación final de implementación, Garantía de Correcto Funcionamiento y acta (H12, mes 21)
- 1.12.5 Soporte de estabilización (hypercare) post-puesta en marcha

### 1.13 Gestión del cambio y capacitación — 4 paquetes

- 1.13.1 Plan de gestión del cambio con diagnóstico por perfil y medición de adopción (Art. 89)
- 1.13.2 Plan de capacitación por rol y materiales editables en español (Art. 90)
- 1.13.3 Capacitación ejecutada y certificación de administradores y equipo técnico — condición de cierre de cada marcha blanca
- 1.13.4 Acompañamiento en puesto (62 % rotación, 1.900 temporeros, 1.100 externos) y 2 jornadas anuales en operación

### 1.14 Documentación, transferencia y reversibilidad (Arts. 91, 77, 87) — 5 paquetes

- 1.14.1 Documentación por categoría: arquitectura, requerimientos, construcción + SBOM, pruebas, operación, seguridad, usuario y proyecto
- 1.14.2 Transferencia tecnológica: código fuente, artefactos de construcción, scripts IaC y procedimientos de despliegue
- 1.14.3 Plan de reversibilidad (90 días iniciales, actualizado anual) con exportación en formatos abiertos y acompañamiento 90 días
- 1.14.4 Cierre contractual, traspaso final a operaciones y lecciones aprendidas
- 1.14.5 Protocolo de aceptación de hitos y del producto final (T-17) **[Nuevo]** (Ronda 0: 3.9) — base de las actas de 1.1.7

### 1.15 Operación (meses 21–56) — 6 paquetes

- 1.15.1 Mesa de servicio N1/N2/N3 conforme a los niveles del Art. 78
- 1.15.2 Informe mensual de nivel de servicio (Art. 79.2)
- 1.15.3 Prueba semestral de recuperación (RPO/RTO = 100 %) y cero vulnerabilidades críticas abiertas
- 1.15.4 Mantención preventiva y evolutiva (base del sd-11) con mejora continua de SLA
- 1.15.5 Informe anual de certificaciones y soporte a auditorías e inspecciones (Arts. 27, 74.6)
- 1.15.6 Jornadas anuales de actualización y capacitación de personal nuevo (Art. 90.5)

---

## Cobertura frente a la 2ª lista (Ronda 0, 120 entregables)

| Estado frente a la 2ª lista | Cantidad |
| :-- | --: |
| Presente en esta EDT | 65 |
| Parcial (incorporar detalle o promover a paquete propio) | 32 |
| Ausente → incorporado en esta versión **[Nuevo]** | 23 |
| **Total** | **120** |

Distribución de los 23 nuevos: 1.1 (+2), 1.3 (+1), 1.4 (+10), 1.6 (+3), 1.7 (+4), 1.8 (+1), 1.9 (+1), 1.14 (+1).

Total de paquetes: **110** (87 previos + 23). Ramas sin cambios: 1.2, 1.5, 1.10, 1.11, 1.12, 1.13, 1.15.

---

## Pendientes

1. Re-secuenciar códigos al congelar la EDT (orden dentro de cada rama) antes de volcar a T-14.
2. Hito E-25 de H1, H4, H8, H9 ilegibles en las tablas de las Bases: anclarlos a la ventana del Art. 17; no inventar cifras.
3. Nombres de tecnología y zonas (AKS, K3s, tri-zona) provisionales hasta redactar `02_Propuesta/latex_final/sd-04.tex` (RR-07 exige nombres idénticos).
4. Reparto Etapa 1 / Etapa 2 de cada paquete según los criterios de sd-03.
5. 1.7.11 condicionado a la decisión de escenario del sd-03 (Escenario A/B): el supuesto SP-01 que lo volvería incondicional no está registrado en el repositorio.
6. Ponderaciones del T-21 en blanco (tablas de `Bases_Administrativas.md` incompletas); no hardcodear cifras.
7. Autonomía: declarar 24 h (Art. 16.4) y 8 h tienda / 4 h CD (RT-03.10, paquete 1.3.5) — reconciliar en la redacción.
8. Resolver los 32 parciales de la Ronda 0: promover a paquete propio donde corresponda (p. ej. plan de recuperación ante desastres, diccionario de datos, catálogo de reglas por tipo de dato, servicio de identidad, plan de convivencia).
9. La fase de oferta (T-12, video, sitio web, prototipo) queda fuera de la EDT.
10. Faltan los campos del diccionario por paquete para T-14: criterio de aceptación con umbral, responsable, esfuerzo/horas, dependencias, mes, hito E-25 y trazas RT/RF.
