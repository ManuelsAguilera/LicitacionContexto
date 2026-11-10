# Registro de cambios del SD-04 para la tabla de trazabilidad

**Período:** 06-11-2026 a 09-11-2026. **Base de comparación:** commit `226bca8` (06-11-2026), último antes de esta redacción. Los cambios no tienen commit. **Estado:** sin revisión humana; «revisado» lo asigna el usuario.

**Para qué sirve.** Reúne todo lo que cambió en la redacción del SD-04 y en los documentos de trabajo, con su motivo y su base, para construir después la tabla de trazabilidad (requisito → decisión → sección → cambio). No omite cambios: el detalle completo, frase por frase, está en [`registro-cambios-detalle.md`](registro-cambios-detalle.md), que se regenera con `generar_registro_cambios.py` desde `git`.

**Cómo leerlo.**
- Cada cambio del `.tex` tiene un identificador **CAM-NNN**, y cada cambio del registro de diseño, **REG-NNN**. Los dos están en el detalle.
- La sección 0 del detalle indica qué cambios produjo cada decisión.
- Las decisiones se identifican así:
  - **P-NN:** `pendientes-decisiones.md`.
  - **C-NNN y K-NN:** hallazgos de `informe-cotejo.md`.
  - **S-NN:** supuestos de `registro-diseno-fisica/06_supuestos-pendientes.md`.
  - **Partes 1 a 7 y cierre:** revisión del 09-11.
- La atribución de motivo en el detalle es automática, por contenido y por sección. Un cambio con varias decisiones las lista todas. Revisarla al construir la tabla.
- Los números de tabla de la bitácora, de `pendientes-decisiones.md` y del registro de diseño son **anteriores** a la renumeración del 09-11. La correspondencia está en la sección 5.

## 1. Documentos tocados

| Documento | Qué cambió | Volumen | Detalle |
| :--- | :--- | :--- | :--- |
| `02_Propuesta/latex_final/sd-04/OnlySimpleSolutions-Subdocumento4.tex` | Redacción de 4.1, 4.2 y 4.3, tablas nuevas, figuras físicas nuevas, renumeración de tablas y figuras, citas y Referencias | 183 cambios: 5 agregados, 117 modificados, 3 eliminados y 58 solo de renumeración | CAM-001 a CAM-183 |
| `registro-diseno-fisica/00_registro-de-diseno.md` | Correcciones K-01 y K-04 (§9.1 y §9.5, H-17) | 4 líneas | REG-2NN |
| `registro-diseno-fisica/01_nodos.md` | K-01, K-02, K-03, K-05, K-06, K-07, K-08, K-09; DC-01 con 80 de 168U | 30 líneas | REG-3NN |
| `registro-diseno-fisica/02_conexiones.md` | K-01 (E-55), K-07 (E-54), K-08 (E-03b) | 6 líneas | REG-4NN |
| `registro-diseno-fisica/03_ambientes.md` | K-01 (fila de Service Bus) | 2 líneas | REG-5NN |
| `registro-diseno-fisica/05_capacidad.md` | K-05: pico de Service Bus de 6.667 y 7.802 entregas por segundo | 3 líneas | REG-6NN |
| `registro-diseno-fisica/06_supuestos-pendientes.md` | K-10 y supuestos nuevos S-33 a S-47, S-43b y S-46b | 26 líneas (contra el commit base) | REG-7NN y sección 3 |
| `redaccion-2026-11/` (nuevo) | Informe de cotejo, bitácora, ajustes a otros documentos, pendientes de decisión, este registro y su detalle | Archivos nuevos | — |
| `registro-diseno-fisica/diagramas-laminas/` (nuevo) | Generador `generar_laminas.py`, `construir.sh`, `integrar_en_tex.py`, 14 especificaciones JSON, salida `.drawio` y `.png`, `correspondencia-figuras.json` | Archivos nuevos | Sección 7 |
| `04_Adjuntos/diagramas/diag-04-12_…` a `diag-04-25_…` (nuevos) | Fuente de cada figura: `.json`, `.drawio`, `.png` y `.pdf` | 56 archivos nuevos; los `diag-04-13` a `diag-04-21` antiguos se conservan | Sección 7 |
| `02_Propuesta/latex_final/figuras/diag-04-12_…` a `diag-04-25_…` (nuevos) | Imágenes que usa el `.tex` | 14 archivos nuevos; las antiguas de `recepcion-20261025/` siguen en la carpeta, sin uso en las figuras físicas | Sección 7 |

**No se editaron**, pero tienen ajustes pendientes por este trabajo: SD-03, SD-05, SD-06, SD-07, SD-08 y SD-13, y los formularios T-10, T-11 (y su copia local), T-12, T-14 y T-22. Ver la sección 8 y `ajustes-otros-documentos.md`.

## 2. Decisiones y su aplicación

| N.º | Fecha | Decisión | Quién | Dónde se aplicó | Base | Cambios |
| ---: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 06-11 | Criterio de qué entra en el SD-04: sin riesgos ni costos en cifras, fallas sí; DC-01 solo con lo que provee el proponente; puertos solo en enlaces críticos; 4.1 con rol propio | Usuario | Todo el `.tex` | Comunicado 10; FEP01·17, ·74, ·93 | Transversal |
| 2 | 06-11 | Informe de cotejo y sugerencias por subsección contrastadas con las Bases | Usuario | `informe-cotejo.md` §10 | Bases Administrativas, Transversales, Caso 09 | — |
| 3 | 06-11 | Corrección del catálogo K-01 a K-10 (Service Bus sin geo-replicación, dos perfiles de Front Door, Bastion con Private Access, recorrido privado, carga de Service Bus, enlace de Concepción, doce réplicas, supuestos resueltos, encabezado de `01`, fila S-27) | Usuario | Registro de diseño `00` a `06` | RT-07.03; Art. 16.3 | REG |
| 4 | 06-11 | Exigencias de las Bases sin supuesto, registradas como S-33 (tipología), S-34 (RAID 1), S-35 (CIS y parches) y S-36 (FinOps y reversibilidad) | Usuario | `06`; `.tex` 4.2.1, 4.2.2, 4.2.3 | Transversales §6.1; RT-03.14; RT-03.15 | REG; Sesión A; Ciclo 4.2.1 |
| 5 | 06-11 | Ciclo 4.3.1: HSM condicionado (C-053), accesos de DC-01 (C-021), tipología principal de DC-01 (C-068), Concepción con par de captura sin WMS (C-070) y ajustes de los agentes | Usuario y agentes | 4.3.1 | RT-06.01 a RT-06.24; Caso cap. 5 p. 13 y cap. 6 p. 14 | Ciclo 4.3.1 |
| 6 | 06-11 | Ciclo 4.3.2: reconexión al VPN Gateway de Brasil (C-074), grupo elástico (C-075), puntos privados de Front Door (C-076), norma de externalización CMF (C-079), sin matriz de riesgos (C-080), alternativa de Sentinel (C-081), zona única como limitación temporal (C-083), declaración con dos sondas (C-084) | Usuario y agentes | 4.3.2, 4.3.2.1, 4.3.2.2 | RT-07.01 a RT-07.12; Art. 16.3 | Ciclo 4.3.2 |
| 7 | 08-11 | Ciclo 4.2.1: DC-01 como puntero a 4.3.1, RAID 1, copia local cifrada, CIS e Intune, UPS en kVA, sin VLAN numeradas | Usuario y agentes | 4.2.1 | RT-03.14; RT-03.15; RT-03.18 | Ciclo 4.2.1 |
| 8 | 08-11 | El par local de captura de los centros lo provee el proponente | Usuario | 4.2.1 y tabla de suministro (hoy Tabla 4.15) | Art. 14.2; Art. 16.4 | Ciclo 4.2.1 |
| 9 | 08-11 | RT-06.33 se aplica al recinto de DC-01; en tiendas y centros, el Cliente ejecuta obras y red (alternativa A, S-37) | Usuario | 4.2.1 | RT-06.33; Caso cap. 11, p. 27 | Ciclo 4.2.1 |
| 10 | 08-11 | Software de los servidores locales: contenedores por negocio, sin hipervisor en tienda; DC-01 con virtualización por fijar (S-37) | Usuario | 4.2.1 | `cierre-inventario/03` L80 | Ciclo 4.2.1 |
| 11 | 08-11 | Folio del Caso para el hardware: p. 27 y no p. 26 | Claude, verificado en OCR | 4.2.1 | `caso09_ocr_paginado.txt` | Ciclo 4.2.1 |
| 12 | 08-11 | Sesión A del bloque 4.2: tabla de seis factores del Art. 16.2, servicios contratados, puertos, ambientes, puntos únicos, mapeo y dimensionamiento | Usuario y agentes | 4.2 intro, 4.2.2 a 4.2.8 | Art. 16.2; Art. 16.4; RT-09.x | Sesión A |
| 13 | 08-11 | Ordenar los pendientes por impacto en la nota en cuatro niveles | Usuario | `pendientes-decisiones.md` | Bases | — |
| 14 | 09-11 | P-01: opción 2 elegida; sin región sudamericana con alta disponibilidad entre zonas (tabla de Microsoft); queda el texto vigente y se cita la fuente | Usuario | 4.3.2.2; Referencias (2026t) | Art. 16.3 | P-01 |
| 15 | 09-11 | P-02: tabla de funciones no disponibles sin enlace con procedimiento manual | Usuario | 4.1.12, hoy Tabla 4.11 | RT-03.13; S-46; S-46b | P-02 |
| 16 | 09-11 | P-03: ocho puntos únicos de falla alineados con T-12 | Usuario | 4.2.6 | RT-02.11 | P-03 |
| 17 | 09-11 | P-04: objetivo de conmutación de 30 segundos | Usuario | 4.2.6 | RT-03.17; S-38 | P-04 |
| 18 | 09-11 | P-05: RTO desde la interrupción declarada; servicios críticos con el Cliente en el diseño detallado | Usuario | 4.3.2.2 | RT-07.04; SD-09 L185 | P-05 |
| 19 | 09-11 | P-06: tabla de retención y copia por dominio, en 4.3.2 y no en anexo | Usuario | 4.3.2.1, hoy Tabla 4.26 | RT-07.09 a RT-07.13; Caso cap. 15, p. 33 | P-06 |
| 20 | 09-11 | P-07: copia de claves en el Key Vault de Brasil con custodia dual y ensayo | Usuario | 4.3.2.1 | RT-07.10; S-39 | P-07 |
| 21 | 09-11 | P-08: recinto de DC-01 de uso exclusivo de la solución y de los sistemas conservados | Usuario | 4.3.1 | RT-06.01; S-40 | P-08 |
| 22 | 09-11 | P-09: frontera en el rack; el proponente provee canalizaciones y el Cliente ejecuta el cableado | Usuario | 4.3.1 y tabla de suministro | RT-06.33; S-41 | P-09 |
| 23 | 09-11 | P-10: efecto e identificador en la misma transacción; corte común por marca de tiempo | Usuario | 4.1.8 y 4.3.2 | RT-02.06; RT-07.04; S-42 | P-10 |
| 24 | 09-11 | P-11: tipología vigente | Usuario | Sin cambios | S-33 | — |
| 25 | 09-11 | P-12: tabla Brasil frente al sitio alternativo en Chile | Usuario | 4.3.2.1, hoy Tabla 4.27 | RT-07.02; RT-07.04; S-44 | P-12 |
| 26 | 09-11 | P-13: aprobación de residencia «antes de cerrar el diseño detallado» | Usuario | 4.3.2.1 | Art. 23; Ley 21.719 | P-13 |
| 27 | 09-11 | P-14: origen de Brasil en Front Door deshabilitado hasta la penúltima etapa | Usuario | 4.3.2 y 4.3.2.2 | RT-07.05; S-45 | P-14 |
| 28 | 09-11 | P-15: ventana de deduplicación (opción 2), corregida en la parte 1 (S-43b) | Usuario | 4.3.2 | RT-02.06; S-43; S-43b | P-15 |
| 29 | 09-11 | P-16: 24 horas con conciliación en 30 minutos | Usuario | 4.2.6 | RT-03.10 | P-16 |
| 30 | 09-11 | P-17: Service Bus zonal confirmado por el usuario | Usuario | Tabla de recuperación por servicio (hoy 4.21) | RT-07.01 | P-17 |
| 31 | 09-11 | P-18, P-22, P-23: opción vigente | Usuario | Sin cambios | — | — |
| 32 | 09-11 | P-19: formularios después de 4.1 y de los diagramas, uno por uno | Usuario | Sin cambios | — | — |
| 33 | 09-11 | P-20: se quita la resolución RAEX202503748 | Usuario | 4.3.2.1; Referencias | Ley 21.719 | P-20 |
| 34 | 09-11 | P-21: tabla de direcciones IP se queda en 4.2.4 | Usuario | Sin cambios | — | — |
| 35 | 09-11 | Sesión B de 4.1: API Management, Redis, HSM, Front Door, Azure Pipelines, motor local PostgreSQL, 25 actores, un tenant, fila virtual, figura 4.11, Power BI en ADR-09 | Usuario (criterio aprobado) y Claude | 4.1.1 a 4.1.16 | C-002 a C-018; S-13; S-47 | C-NNN; Sesión B |
| 36 | 09-11 | Ajustes de los tres agentes sobre 4.1 y 4.3.2 (tablas nuevas, puntos únicos, actores, Front Door, ventana, External ID, motor local) | Agentes; aplicado por Claude | 4.1, 4.2.6, 4.3.2 | Informes de los agentes | Varios |
| 37 | 09-11 | Parte 1: ventana de deduplicación, opción 1 (S-43b) | Usuario | 4.3.2 | RT-02.06 | P-15 |
| 38 | 09-11 | Parte 2: no aplicar la aclaración de 4.2.6 (no hay contradicción) | Usuario | Sin cambios | — | — |
| 39 | 09-11 | Parte 3: definir namespace, broker, idempotencia y cupo preemitido en su primera mención | Usuario | 4.1.1, 4.1.6, 4.1.12 | Lector no técnico | Parte 3 |
| 40 | 09-11 | Parte 4: tabla del sitio alternativo sin cambios | Usuario | Sin cambios | — | — |
| 41 | 09-11 | Parte 5: alcance de las alternativas evaluadas («de la Tabla 4.13», tabla de ADR) | Usuario | Introducción del capítulo | FEP01·273 | Parte 5 |
| 42 | 09-11 | Parte 6: nodo de la vista logística y de las capacidades comunes; F:C-04 candidato | Usuario | Tabla de mapeo (hoy 4.22) | Comunicado 10 (mapeo al 100 %) | Parte 6 |
| 43 | 09-11 | Parte 7: origen de 31 de 72U y de los 43 minutos | Usuario | 4.2.1 y 4.2.6 | `cierre-inventario/12`; RT-10.01 | Parte 7 |
| 44 | 09-11 | Cierre 1: renumeración de las 28 tablas por orden de aparición | Usuario | Todo el `.tex` | Comunicado 10 | Cierre parte 1 |
| 45 | 09-11 | Cierre 2: «Data Lake» y sin nombres internos; «Emisor» y «Frontera» se conservan como en el SD-03 | Usuario | 4.1.10, 4.2.4, 4.2.7, 4.3.1 | Glosario 08 | Cierre parte 2 |
| 46 | 09-11 | Cierre 3: referencias completas; capítulo y folio del Caso; título y URL de 2026t | Usuario | Referencias; fuente de la Tabla 4.26 | citas-proyecto | Cierre parte 3 |
| 47 | 09-11 | Cierre 4: transversales solo registradas | Usuario | `ajustes-otros-documentos.md` | — | — |
| 48 | 09-11 | Cierre 5: formularios y citas externas después de los diagramas | Usuario | Pendiente | — | — |
| 49 | 09-11 | Cuatro láminas de arquitectura física (A a D), sin E-NN, para el SD-04 y la presentación | Usuario | `diagramas-laminas/` | diagramas-ancoa (F1, F2, F4, F5) | Sección 7 |
| 50 | 09-11 | No omitir elementos en los diagramas y agregar las figuras que el texto necesite; el usuario revisa en el documento | Usuario | 14 figuras físicas en el `.tex` (Figuras 4.12 a 4.25) | 01_nodos.md; máximo de nodos de la skill | Figuras |
| 51 | 09-11 | Registrar todos los cambios para la tabla de trazabilidad | Usuario | Este documento y `registro-cambios-detalle.md` | — | — |

## 3. Supuestos nuevos o modificados

Todos están en `registro-diseno-fisica/06_supuestos-pendientes.md`.

| ID | Supuesto | Origen | Sección |
| :--- | :--- | :--- | :--- |
| S-33 | Tipología on-premise por sitio: DC-01 sala técnica principal; tienda y centros sala técnica secundaria o de sitio | C-087; Transversales §6.1 | 4.2.2, 4.3.1 |
| S-34 | RAID 1 con dos discos de 960 GB por servidor; copia local cifrada aparte | C-088; RT-03.14 | 4.2.1 |
| S-35 | CIS, gestión de parches, Intune y administración remota de dispositivos | C-090; RT-03.15; RT-03.18 | 4.2.1 |
| S-36 | FinOps (etiquetado, presupuestos, alertas, reporte mensual) y reversibilidad | C-089 | 4.2.3 |
| S-37 | RT-06.33 en DC-01 y alternativa A en tiendas y centros; contenedores sin hipervisor en tienda | Usuario 08-11 | 4.2.1 |
| S-38 | Conmutación entre accesos de tienda con objetivo de 30 segundos | P-04 | 4.2.6 |
| S-39 | Copia de claves en el Key Vault de Brasil con custodia dual y ensayo | P-07 | 4.3.2.1 |
| S-40 | Recinto técnico de DC-01 de uso exclusivo | P-08 | 4.3.1 |
| S-41 | Frontera de canalizaciones y cableado en el rack | P-09 | 4.3.1 |
| S-42 | Transacción única de efecto e identificador; corte común por marca de tiempo | P-10 | 4.1.8, 4.3.2 |
| S-43 | Ventana de deduplicación, primera fórmula | P-15 | Reemplazado por S-43b |
| S-43b | Ventana no menor que 15 min + 4 h, ampliada por el retraso medido; claves de venta de tienda 24 h | Hilo lógico; parte 1 (aprobado) | 4.3.2 |
| S-44 | Sitio alternativo en Chile con capacidad equivalente para los servicios críticos | P-12 | Tabla 4.27 |
| S-45 | Origen de Brasil en Front Door deshabilitado hasta la penúltima etapa | P-14 | 4.3.2, 4.3.2.2 |
| S-46 | Procedimientos manuales de las ocho funciones no disponibles sin enlace | P-02 | Tabla 4.11 |
| S-46b | La jefatura de tienda ejecuta los procedimientos; la filial emisora define los dos primeros | Agentes | 4.1.12 |
| S-47 | 25 actores del diagrama de contexto en lugar de los 31 del análisis UAW | C-008 | 4.1.2 |

## 4. Tablas nuevas

| Tabla (número actual) | Contenido | Decisión |
| :--- | :--- | :--- |
| 4.11 | Funciones no disponibles sin enlace y procedimiento manual (8 filas) | P-02 |
| 4.16 | Seis factores del Art. 16.2 por grupo de componentes (reescrita, 11 filas) | Sesión A |
| 4.26 | Retención y copia en Brazil South por dominio de datos (8 filas) | P-06 |
| 4.27 | Brazil South y sitio alternativo en Chile (6 filas) | P-12 |

## 5. Renumeración de tablas (09-11)

| Antes | Ahora | Antes | Ahora |
| :--- | :--- | :--- | :--- |
| 4.12 | 4.1 | 4.22 | 4.15 |
| 4.1 a 4.9 | 4.2 a 4.10 | 4.14 a 4.21 | 4.16 a 4.23 |
| 4.28 | 4.11 | 4.23 | 4.24 |
| 4.10 | 4.12 | 4.24 | 4.25 |
| 4.11 | 4.13 | 4.25 | 4.26 |
| 4.13 | 4.14 | 4.26 | 4.27 |
| — | — | 4.27 | 4.28 |

Los documentos que citan números antiguos se listan en `ajustes-otros-documentos.md`: T-12 con 185 citas, T-11 con 51, T-22 con 30, y SD-06, SD-08 y T-10 con una cada uno. Varias de esas citas ya estaban desfasadas antes de la renumeración. Las figuras no se renumeraron.

## 6. Referencias

| Entrada | Cambio | Decisión |
| :--- | :--- | :--- |
| Comisión para el Mercado Financiero (2019) | Agregada | C-079 |
| Subsecretaría de Economía y Empresas de Menor Tamaño (2025), RAEX202503748 | Agregada en el ciclo 4.3.2 y quitada el 09-11 | C-079; P-20 |
| Microsoft (2026t), *What is Azure Database for PostgreSQL flexible server?* | Agregada; la anterior 2026t (*What is Azure Managed Redis?*) pasa a 2026u | P-01; cierre 3 |
| Cita del Caso en la Tabla 4.26 | Cap. 15, requisito RT-05.10, p. 33 | Cierre 3 |
| Cita del Caso del hardware | Cap. 11, p. 27 (antes p. 26) | Decisión 11 |

## 7. Diagramas (figuras físicas)

**Qué se hizo (09-11).**
- Se reemplazaron las 17 figuras físicas del SD-04 por 14 figuras nuevas, generadas con la skill `diagramas-ancoa`. Cada una está validada contra el catálogo y queda dentro de su máximo de nodos.
- Ninguna figura lleva IDs E-NN, y todas las líneas tienen rótulo en palabras.
- Las cuatro láminas aprobadas (A a D) no cabían en el máximo de nodos sin omitir elementos. Por eso se dividieron como pide la skill: B en cuatro figuras, C en tres, D en cuatro, y se agregaron E1 (entrega y ambientes) y F4 (puntos de falla).
- Las figuras se renumeraron por orden de aparición, y la correspondencia completa está en `diagramas-laminas/correspondencia-figuras.json`.
- La revisión de cada figura buscó cruces y rótulos tapados. Se corrigieron en iteraciones: orden de celdas, rejillas de igual altura y frentes en filas para que la Figura 4.15 quepa en una página vertical.

| Figura nueva | Lámina | Estilo | Contenido | Reemplaza (número antiguo) | Archivo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 4.12 | A | F1 | Sitios, conexiones, regiones, servicios globales y plataformas conservadas | 4.12 | `diag-04-12_topologia-general` |
| 4.13 | D1 | F5 | Tienda tipo: servidores, árbitros, copias locales, terminales, red, accesos y túneles | 4.19 | `diag-04-13_tienda-red-servidores` |
| 4.14 | D2 | F5 | Tienda tipo: racks, PDU, UPS, transferidor, grupo electrógeno, clima y sensores | 4.20 | `diag-04-14_tienda-energia-espacio` |
| 4.15 | B1 | F2 | Red y entrada de Chile Central por frente, con X-01 | 4.13 y 4.14 | `diag-04-15_red-chile-central` |
| 4.16 | E1 | F3 | Canal de entrega y ambientes por frente, con tienda de laboratorio y recuperación | 4.15 y 4.16 | `diag-04-16_entrega-ambientes` |
| 4.17 | F4 | F4 | Los 13 puntos de falla con la numeración de la Tabla 4.20 | 4.17 y 4.18 | `diag-04-17_puntos-falla` |
| 4.18 | B2 | F5 | Clústeres de AKS por grupos de nodos y máquinas de apoyo | 4.21 (y las máquinas de 4.24) | `diag-04-18_computo-chile-central` |
| 4.19 | B3 | F5 | 12 bases PostgreSQL, mensajería, caché, almacenamiento y bóvedas de respaldo | 4.22 y 4.23 | `diag-04-19_datos-chile-central` |
| 4.20 | B4 | F5 | Identidad, claves, seguridad, observabilidad, datos de analítica y entrega | 4.24 | `diag-04-20_seguridad-operacion` |
| 4.21 | D3 | F5 | DC-01: recinto técnico, redes por negocio, integración, sistemas conservados y salida | 4.25 | `diag-04-21_dc01-casa-matriz` |
| 4.22 | D4 | F5 | CD-01 y CD-02 con su par de captura, red, enlaces y WMS | 4.26 | `diag-04-22_centros-distribucion` |
| 4.23 | C1 | F5 | Brazil South: red y entrada por frente | 4.27 (parte) | `diag-04-23_brazil-red-entrada` |
| 4.24 | C2 | F5 | Brazil South: cómputo y datos en espera por frente | 4.27 (parte), nueva | `diag-04-24_brazil-computo-datos` |
| 4.25 | C3 | F4 | Conmutación: declaración y siete etapas | 4.28 | `diag-04-25_conmutacion` |

**Cobertura del inventario (`registro-diseno-fisica/01_nodos.md`).** Cada fila del inventario aparece al menos en una figura:
- Bloque 1, tienda: 4.13 y 4.14, y la tienda de laboratorio en 4.16.
- Bloque 2, red y entrada de Chile: 4.15.
- Bloque 3, cómputo y datos: 4.18 y 4.19.
- Bloque 3b, identidad, seguridad y observabilidad: 4.15 (Bastion, DDoS), 4.18 (conectores, pila de observabilidad) y 4.20.
- Bloque 3c, entrega y ambientes: 4.16 y 4.20.
- Bloque 4, Brazil South: 4.23 y 4.24, y los puntos privados de Front Door en 4.15.
- Bloque 5, casa matriz y centros: 4.12, 4.21 y 4.22.
- Bloque 6, contrapartes: 4.12, 4.21 y 4.22.
- Bloque 7, servicios globales: 4.12, 4.15, 4.19 y 4.20.

Se muestran agrupados en un solo icono, con la cantidad en el rótulo, para no superar el máximo de nodos:
- grupos de nodos de AKS;
- pares de máquinas de apoyo;
- PDU dentro de su rack;
- sondas de Brasil dentro de las máquinas templadas.

**Texto ajustado a las figuras.**
- Las referencias a figuras fusionadas apuntan a la figura nueva.
- Se reescribieron estas frases:
  - «red de un frente tipo» pasa a «red de los tres frentes»;
  - los puntos de falla «de los accesos» pasan a «de los sitios y de la nube»;
  - la región se describe en «tres figuras» en lugar de cuatro;
  - las máquinas auxiliares aparecen en la Figura 4.18;
  - Brasil se muestra en las Figuras 4.23 y 4.24.
- Se quitó la frase del rótulo de búsqueda de OpenMetadata, porque la figura nueva no tiene ese rótulo.
- Se agregó una frase entre las Figuras 4.23 y 4.24.
- La declaración de uso de IA (Tabla 4.28) ahora nombra Codex y Claude y las figuras, con la revisión de noviembre pendiente.
- Cada cambio está en el detalle (CAM).

**Limitaciones conocidas.**
- Algunos rótulos de línea quedan muy cerca de otros elementos (Figura 4.12). Se pueden ajustar a mano en draw.io sin cambiar íconos ni trazos, como permite la skill.
- En la Figura 4.15, la línea magenta de compra sale del clúster de Retail pero se dibuja junto al balanceador.
- Los íconos de clima, incendio y generador usan el ícono más cercano del catálogo (monitor y UPS), porque no hay uno propio.
- En la vista previa compilada (91 páginas), la Figura 4.15 ocupa el ancho de la página con rótulos pequeños.

## 8. Pendientes que la trazabilidad debe recoger

**Sin aplicar, a decisión del usuario o por falta de dato:**
- Cifras sin fuente citada: 2.600 km y 40 a 55 ms (cálculo en `calculos/latencia-santiago-sao-paulo.py`), 2,57 y 3,341 kW (`cierre-inventario/10` y `11`).
- Umbral de conciliación de 30 minutos frente a «no crea otro plazo contractual de drenaje» (4.1.12).
- Vigencia máxima de la lista de precios sin enlace.
- Tabla 4.1 (antes 4.12): siete filas dicen «Ninguna otra evaluada todavía». La parte 5 precisó el alcance de la introducción y las filas siguen así.
- Términos del lector sin definir: Private Link antes de 4.2.4, sonda, subencargado.
- H-17 del catálogo (K-04) por corregir.
- Fuentes no verificadas en el PDF visible: folios del Caso (verificados en el OCR paginado).
- Pruebas del exportador: `test_diccionario` y `test_redaccion` fallan por causas ajenas al SD-04 (diccionario desactualizado frente al SD-03 y regla RR-20 sin fuente del Comunicado 10).

**En otros documentos (sin editar):** ver `ajustes-otros-documentos.md`.
- SD-03: equipamiento de tiendas, Concepción, «ámbito», norma CMF, canalizaciones.
- SD-05: Event Hubs frente a Service Bus, y el motor local.
- SD-07: 31 actores, tienda de laboratorio, custodia de medios, despliegue azul-verde.
- SD-13: adaptador de lockers, fila local, equipos de tienda, inferencia, memoria de capacidad.
- T-11, T-12, T-14 y T-22: ExpressRoute, ocho puntos únicos, par de captura de los centros, árbitro, folio p. 27 y citas de tabla y de figura.
- SD-06, SD-08 y T-10: citas de tabla.
