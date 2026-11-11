# Registro de cambios: detalle completo

**Generado** con `generar_registro_cambios.py` comparando con el commit `226bca8` (06-11-2026, antes de la redacción de noviembre). Lista **todos** los cambios, frase por frase. Se regenera; no se edita a mano. El resumen y las decisiones están en `registro-cambios-trazabilidad.md`.

Columnas: **ID**; **Línea** del `.tex` actual; **Sección**; **Tipo**; **Se quitó** y **Se agregó** (frases completas); **Motivo** (decisión o ciclo de la bitácora); **Base** (requisito, supuesto o documento).

## 0. Índice: decisión o ciclo → cambios del `.tex`

| Decisión o ciclo | Cambios |
| :--- | :--- |
| C-002 | CAM-004 |
| C-003 | CAM-007, CAM-084, CAM-123 |
| C-004 | CAM-008 |
| C-005 | CAM-006 |
| C-006 | CAM-009 |
| C-007 | CAM-009, CAM-038, CAM-039 |
| C-008 | CAM-012 |
| C-009 | CAM-015 |
| C-013 | CAM-036 |
| C-015 | CAM-038 |
| C-016 | CAM-045 |
| C-017 | CAM-046 |
| C-018 | CAM-050 |
| Ciclo 4.2.1 | CAM-059, CAM-060, CAM-061, CAM-064, CAM-068, CAM-072, CAM-074 |
| Ciclo 4.3.1 | CAM-139 |
| Ciclo 4.3.2 | CAM-159, CAM-160, CAM-161, CAM-164, CAM-166, CAM-167, CAM-171, CAM-172 |
| Cierre parte 1 | CAM-002, CAM-003, CAM-005, CAM-010, CAM-016, CAM-017, CAM-018, CAM-019, CAM-020, CAM-021, CAM-023, CAM-024, CAM-025, CAM-026, CAM-027, CAM-028, CAM-029, CAM-030, CAM-031, CAM-033, CAM-034, CAM-035, CAM-037, CAM-040, CAM-042, CAM-043, CAM-044, CAM-047, CAM-048, CAM-049, CAM-054, CAM-055, CAM-058, CAM-070, CAM-071, CAM-079, CAM-080, CAM-082, CAM-090, CAM-091, CAM-092, CAM-093, CAM-095, CAM-098, CAM-110, CAM-115, CAM-117, CAM-121, CAM-127, CAM-128, CAM-129, CAM-133, CAM-134, CAM-135, CAM-158, CAM-180, CAM-181, CAM-183 |
| Cierre parte 2 | CAM-081, CAM-097, CAM-124, CAM-142 |
| Cierre parte 3 | CAM-162 |
| P-01 | CAM-085, CAM-174, CAM-179 |
| P-02 | CAM-041 |
| P-03 | CAM-114 |
| P-04 | CAM-107 |
| P-05 | CAM-177 |
| P-06 | CAM-162 |
| P-07 | CAM-169 |
| P-08 | CAM-150 |
| P-09 | CAM-073, CAM-145 |
| P-10 | CAM-032, CAM-162 |
| P-12 | CAM-173 |
| P-13 | CAM-165, CAM-170, CAM-173 |
| P-14 | CAM-112, CAM-157, CAM-174 |
| P-15 | CAM-162, CAM-163 |
| P-16 | CAM-113 |
| P-17 | CAM-116 |
| P-20 | CAM-168 |
| Parte 3 | CAM-006, CAM-011, CAM-022, CAM-041 |
| Parte 5 | CAM-001 |
| Parte 6 | CAM-126 |
| Parte 7 | CAM-065, CAM-119 |
| Sesión A | CAM-053, CAM-056, CAM-057, CAM-075, CAM-076, CAM-077, CAM-078, CAM-083, CAM-089, CAM-094, CAM-096, CAM-101, CAM-103, CAM-108, CAM-111, CAM-118, CAM-120, CAM-122, CAM-125, CAM-130, CAM-131, CAM-132 |
| Sesión B | CAM-013, CAM-014 |

## 1. `02_Propuesta/latex_final/sd-04/OnlySimpleSolutions-Subdocumento4.tex`

Totales del `.tex`: 183 cambios (5 agregados, 117 modificados, 3 eliminados y 58 solo de renumeración).

### CAM-001 · línea 91 · Capítulo 4 · Arquitectura lógica y física de la solución · Modificado

- **Se quitó:** Cada decisión de arquitectura se registra con las alternativas evaluadas y el criterio de selección.
- **Se agregó:** Cada decisión de arquitectura de la Tabla 4.13 se registra con las alternativas evaluadas y el criterio de selección.
- **Motivo:** Parte 5 (opción 1): alcance de las alternativas evaluadas
- **Base:** FEP01·273

### CAM-002 · línea 101 · 4.1 Arquitectura lógica · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.3 → 4.4)
- **Base:** Comunicado 10

### CAM-003 · línea 119 · 4.1.1 Especificaciones Tecnologías de Software a utilizar · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.12 → 4.1)
- **Base:** Comunicado 10

### CAM-004 · línea 127 · 4.1.1 Especificaciones Tecnologías de Software a utilizar · Modificado

- **Se quitó:** La documentación consultada no confirma que API Management Premium clásico esté disponible en el par de regiones elegido, y los demás servicios seleccionados se comprueban del mismo modo.
- **Se agregó:** El buscador de productos por región de Azure confirma que los servicios centrales de la tabla, como AKS, PostgreSQL, Service Bus y API Management, existen en Chile Central y Brazil South, pero no prueba sus funciones ni sus niveles.
- **Motivo:** C-002: existencia de productos verificada; además, renumeración de tablas o figuras
- **Base:** 06 (buscador 02-11)

### CAM-005 · línea 131 · 4.1.1 Especificaciones Tecnologías de Software a utilizar · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.12 → 4.1)
- **Base:** Comunicado 10

### CAM-006 · línea 139 · 4.1.1 Especificaciones Tecnologías de Software a utilizar · Modificado

- **Se quitó:** Mensajería & Azure Service Bus Premium, un namespace por negocio, con colas, tópicos, suscripciones y cola de mensajes no entregables propios. & Condicionada. & Event Hubs y Kafka en AKS, descartados por ADR-06. & Probar duplicados, orden por agregado, errores persistentes y capacidad frente al pico de cambios de precio.
- **Se quitó:** Borde y entrada pública & Azure Front Door Premium con WAF, Private Link y Application Gateway v2, un perfil y una puerta por frente. & Condicionada. & Un gateway compartido por ambos negocios, descartado por ADR-08. & Validar la región del Private Link, TLS por salto y rutas por frente.
- **Se agregó:** Mensajería & Azure Service Bus Premium, un namespace por negocio, que es su espacio aislado dentro del servicio, con colas, tópicos, suscripciones y cola de mensajes no entregables propios. & Condicionada. & Event Hubs y Kafka en AKS, descartados por ADR-06. & Probar duplicados, orden por agregado, errores persistentes y capacidad frente al pico de cambios de precio.
- **Se agregó:** Borde y entrada pública & Azure Front Door Premium con WAF, Private Link y Application Gateway v2, un perfil y una puerta propios de Retail y de la filial emisora, sin entrada pública para X-01. & Condicionada. & Un gateway compartido por ambos negocios, descartado por ADR-08. & Validar la región del Private Link, TLS por salto y rutas por frente.
- **Motivo:** C-005: Front Door con perfil de Retail y de la filial; Parte 3 (opción 1): términos definidos en su primera mención
- **Base:** K-02; Lector no técnico

### CAM-007 · línea 144 · 4.1.1 Especificaciones Tecnologías de Software a utilizar · Modificado

- **Se quitó:** Caché & Azure Managed Redis, solo para datos reconstruibles de Retail. & Por probar. & Azure Cache for Redis se retira el 30 de septiembre de 2028 (Microsoft, 2026k), y Valkey queda como alternativa por evaluar. & Verificar su disponibilidad en Chile Central y el nivel antes de fijarlo.
- **Se agregó:** Caché & Azure Managed Redis, solo para datos reconstruibles de Retail. & Por probar. & Azure Cache for Redis se retira el 30 de septiembre de 2028 (Microsoft, 2026k), y Valkey queda como alternativa por evaluar. & Nivel Balanced B20 de 24 GB, que está disponible en Chile Central y Brazil South y se confirma en la suscripción.
- **Motivo:** C-003: Redis B20 verificado
- **Base:** S-26

### CAM-008 · línea 149 · 4.1.1 Especificaciones Tecnologías de Software a utilizar · Modificado

- **Se quitó:** Identidad y secretos & Microsoft Entra ID P2 federado con el directorio del Cliente, Entra External ID, Intune, Workload Identity, Azure Key Vault y PIM, y Managed HSM para Filial y X-01. & Por probar. & Ninguna otra evaluada todavía. & Confirmar la identidad existente y sus protocolos antes de fijar la federación, y la disponibilidad de Managed HSM en la región.
- **Se agregó:** Identidad y secretos & Microsoft Entra ID P2 federado con el directorio del Cliente, Entra External ID, Intune, Workload Identity, Azure Key Vault y PIM, y Managed HSM para Filial y X-01. & Por probar. & Ninguna otra evaluada todavía. & Confirmar la identidad existente y sus protocolos antes de fijar la federación, y la capacidad de Managed HSM en Brazil South, que se prueba al crear la réplica.
- **Motivo:** C-004: capacidad de HSM en Brasil
- **Base:** S-20

### CAM-009 · línea 152 · 4.1.1 Especificaciones Tecnologías de Software a utilizar · Modificado

- **Se quitó:** Infraestructura y entrega & Terraform y canal CI/CD con registro de artefactos y despliegue auditado. & Por probar. & Reutilizar el canal del Cliente. & Reutilizarlo si satisface revisión, firma y trazabilidad.
- **Se quitó:** Tienda desconectada & Nodo local redundante con diario transaccional y sincronizador. & Por probar. & Valkey u otro motor local, por decidir. & Fijar motor y empaquetado tras inventario de hardware, periféricos y ensayo de 24 horas.
- **Se agregó:** Infraestructura y entrega & Terraform y Azure Pipelines con registro de artefactos y despliegue auditado. & Por probar. & Reutilizar el canal del Cliente. & Reutilizarlo si satisface revisión, firma y trazabilidad.
- **Se agregó:** Tienda desconectada & Nodo local redundante con PostgreSQL como diario transaccional y sincronizador. & Por probar. & Valkey, descartado porque RT-03.11 y RT-03.12 piden un registro local íntegro. & Fijar el empaquetado tras el inventario de hardware, de periféricos y el ensayo de 24 horas.
- **Motivo:** C-007 e hilo lógico: motor local PostgreSQL; C-006: canal de entrega nombrado
- **Base:** RT-03.11; RT-03.12; S-04

### CAM-010 · línea 156 · 4.1.1 Especificaciones Tecnologías de Software a utilizar · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.12 → 4.1)
- **Base:** Comunicado 10

### CAM-011 · línea 158 · 4.1.1 Especificaciones Tecnologías de Software a utilizar · Modificado

- **Se quitó:** Cada propietario conserva su registro de salida y su corte autorizado, de modo que las proyecciones se reconstruyen desde esas fuentes y desde ADLS, y no desde el broker.
- **Se agregó:** Cada propietario conserva su registro de salida y su corte autorizado, de modo que las proyecciones se reconstruyen desde esas fuentes y desde ADLS, y no desde el broker, que es el intermediario que transporta los mensajes.
- **Motivo:** Parte 3 (opción 1): términos definidos en su primera mención
- **Base:** Lector no técnico

### CAM-012 · línea 168 · 4.1.2 Vistas y actores de la solución · Modificado

- **Se quitó:** La Tabla 4.1 agrupa por entrada y frente los treinta y un actores del análisis UAW (peso de actores sin ajustar, parte del método de estimación por puntos de caso de uso).
- **Se quitó:** Los códigos AH identifican a los actores humanos y los AS a los actores sistema.
- **Se quitó:** La tabla es un mapa de cobertura y no una nueva estimación, y conserva fuera de la vista principal a los actores que las figuras por capa no dibujan.
- **Se quitó:** AH-17 usa un contrato de API de vendedor externo cuyo canal se resuelve con el Servicio de marketplace (R:V-04), porque las figuras no le dibujan un canal propio.
- **Se quitó:** AS-11 representa el módulo de remuneraciones de AS-01 y AS-14 un disparador periódico.
- **Se agregó:** La Tabla 4.2 agrupa por entrada y frente los veinticinco actores del diagrama de contexto, que son catorce personas y once sistemas externos.
- **Se agregó:** Los códigos AH identifican a los actores humanos y los AS a los actores sistema de SD-03, y algunos se reúnen en un mismo actor porque comparten canal y destino.
- **Se agregó:** De los 18 códigos AH, AH-17, el vendedor externo, pasa a los sistemas porque entra por un contrato de API que se resuelve con el Servicio de marketplace (R:V-04), y las parejas AH-03 y AH-04, AH-06 y AH-08, y AH-16 y AH-18 se reúnen, lo que deja catorce personas.
- **Se agregó:** De los 13 códigos AS en uso, AS-14, un disparador periódico, queda fuera porque es interno, y las parejas AS-09 y AS-10, y AS-01 con AS-11, que es el módulo de remuneraciones de AS-01, se reúnen, lo que deja diez, y con AH-17 son once sistemas.
- **Se agregó:** La tabla es un mapa de cobertura y no una nueva estimación.
- **Motivo:** C-008 y agentes: 25 actores del diagrama de contexto
- **Base:** S-47

### CAM-013 · línea 172 · 4.1.2 Vistas y actores de la solución · Modificado

- **Se quitó:** Fuente: elaboración propia a partir de SD-03 y del análisis de actores del SD-07.\par\nopagebreak
- **Se agregó:** Fuente: elaboración propia a partir de SD-03 y del diagrama de contexto de la solución.\par\nopagebreak
- **Motivo:** Sesión B (09-11): bloque 4.1 según informe de cotejo; además, renumeración de tablas o figuras
- **Base:** Ver bitácora

### CAM-014 · línea 188 · 4.1.2 Vistas y actores de la solución · Modificado

- **Se quitó:** La tabla conserva todos los códigos AH-01 a AH-18 y AS-01 a AS-14, salvo AS-06.
- **Se agregó:** La tabla conserva todos los códigos AH-01 a AH-18 y AS-01 a AS-14, salvo AS-06, y AS-14 consta como interno.
- **Motivo:** Sesión B (09-11): bloque 4.1 según informe de cotejo
- **Base:** Ver bitácora

### CAM-015 · línea 198 · 4.1.3 Estilo y límites de contexto · Modificado

- **Se quitó:** La base tecnológica y los símbolos agregados de las figuras no comparten datos, inquilinos de identidad (tenants) ni permisos entre negocios.
- **Se agregó:** La base tecnológica y los símbolos agregados de las figuras no comparten datos, claves ni permisos entre negocios.
- **Se agregó:** Hay un solo inquilino de identidad (tenant) de Entra ID, el del Cliente, y los negocios se separan en él por roles y grupos.
- **Se agregó:** Entra External ID, que autentica a los clientes, se configura por separado en cada negocio.
- **Motivo:** C-009 y hilo lógico: un solo tenant; External ID por negocio
- **Base:** S-13

### CAM-016 · línea 216 · 4.1.4 Capas 1 a 3: presentación, borde y puerta de enlace · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.2 → 4.3)
- **Base:** Comunicado 10

### CAM-017 · línea 220 · 4.1.4 Capas 1 a 3: presentación, borde y puerta de enlace · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.2 → 4.3)
- **Base:** Comunicado 10

### CAM-018 · línea 261 · 4.1.5 Catálogo de componentes y autoridad · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.3 → 4.4)
- **Base:** Comunicado 10

### CAM-019 · línea 265 · 4.1.5 Catálogo de componentes y autoridad · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.3 → 4.4)
- **Base:** Comunicado 10

### CAM-020 · línea 286 · 4.1.5 Catálogo de componentes y autoridad · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.4 → 4.5)
- **Base:** Comunicado 10

### CAM-021 · línea 290 · 4.1.5 Catálogo de componentes y autoridad · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.4 → 4.5)
- **Base:** Comunicado 10

### CAM-022 · línea 317 · 4.1.6 Cruce de la compra con tarjeta propia por X-01 · Modificado

- **Se quitó:** La ficha y el contrato de compra se aprueban antes de habilitar el cruce, e incluyen la identidad de X-01 ante la filial emisora, el plazo máximo de espera y la clave de idempotencia de la operación.
- **Se agregó:** La ficha y el contrato de compra se aprueban antes de habilitar el cruce, e incluyen la identidad de X-01 ante la filial emisora, el plazo máximo de espera y la clave de idempotencia de la operación, que permite repetirla sin que se aplique dos veces.
- **Motivo:** Parte 3 (opción 1): términos definidos en su primera mención
- **Base:** Lector no técnico

### CAM-023 · línea 321 · 4.1.7 Capacidades comunes e innovaciones · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.5 → 4.6)
- **Base:** Comunicado 10

### CAM-024 · línea 325 · 4.1.7 Capacidades comunes e innovaciones · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.5 → 4.6)
- **Base:** Comunicado 10

### CAM-025 · línea 339 · 4.1.7 Capacidades comunes e innovaciones · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.6 → 4.7)
- **Base:** Comunicado 10

### CAM-026 · línea 343 · 4.1.7 Capacidades comunes e innovaciones · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.6 → 4.7)
- **Base:** Comunicado 10

### CAM-027 · línea 370 · 4.1.8 Capas e interfaces · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.7 → 4.8)
- **Base:** Comunicado 10

### CAM-028 · línea 376 · 4.1.8 Capas e interfaces · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.7 → 4.8)
- **Base:** Comunicado 10

### CAM-029 · línea 393 · 4.1.8 Capas e interfaces · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.1 → 4.2)
- **Base:** Comunicado 10

### CAM-030 · línea 395 · 4.1.8 Capas e interfaces · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.8 → 4.9)
- **Base:** Comunicado 10

### CAM-031 · línea 399 · 4.1.8 Capas e interfaces · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.8 → 4.9)
- **Base:** Comunicado 10

### CAM-032 · línea 411 · 4.1.8 Capas e interfaces · Modificado

- **Se agregó:** El efecto de un hecho y su identificador se confirman en la misma transacción y en el mismo servidor, y el corte común entre los 12 servidores de PostgreSQL se fija por una marca de tiempo para la recuperación.
- **Motivo:** P-10 (opción 1): corte común por marca de tiempo
- **Base:** S-42; RT-02.06; RT-07.04

### CAM-033 · línea 466 · 4.1.10 Vista de datos y analítica · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.9 → 4.10)
- **Base:** Comunicado 10

### CAM-034 · línea 470 · 4.1.10 Vista de datos y analítica · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.9 → 4.10)
- **Base:** Comunicado 10

### CAM-035 · línea 488 · 4.1.10 Vista de datos y analítica · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.4 → 4.5)
- **Base:** Comunicado 10

### CAM-036 · línea 492 · 4.1.10 Vista de datos y analítica · Modificado

- **Se quitó:** El rótulo de búsqueda del grupo de estado de la filial emisora en la Figura 4.21 corresponde al índice técnico de OpenMetadata, sin acceso al índice comercial de Retail.
- **Motivo:** Texto ajustado a las figuras físicas nuevas (09-11); C-013: rótulo de la figura movido a 4.3.1
- **Base:** diagramas-laminas/correspondencia-figuras.json; Criterio incluye/excluye

### CAM-037 · línea 498 · 4.1.11 Vista de despliegue lógico y sitios · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.25 → 4.21)
- **Base:** Comunicado 10

### CAM-038 · línea 506 · 4.1.12 Continuidad local de tienda · Modificado

- **Se agregó:** El diario durable (L-02) es un PostgreSQL local de la tienda, distinto del PostgreSQL R de la nube.
- **Se agregó:** La fila virtual del Modo Tienda corre en el par de servidores de Retail de la tienda, de modo que sin enlace el personal atiende con registro local y sincroniza después.
- **Motivo:** C-007 e hilo lógico: motor local PostgreSQL; C-015: fila virtual en la continuidad local; además, renumeración de tablas o figuras
- **Base:** RT-03.11; RT-03.12; S-32

### CAM-039 · línea 508 · 4.1.12 Continuidad local de tienda · Modificado

- **Se quitó:** El sincronizador no escribe directamente en PostgreSQL y no considera conciliada una venta solo porque fue enviada.
- **Se agregó:** El sincronizador no escribe directamente en el PostgreSQL de la nube y no considera conciliada una venta solo porque fue enviada.
- **Motivo:** C-007 e hilo lógico: motor local PostgreSQL
- **Base:** RT-03.11; RT-03.12

### CAM-040 · línea 510 · 4.1.12 Continuidad local de tienda · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.18 → 4.20)
- **Base:** Comunicado 10

### CAM-041 · línea 512 · 4.1.12 Continuidad local de tienda · Modificado

- **Se quitó:** Se autoriza contra un cupo preemitido de la filial emisora, que se guarda en la tienda con almacenamiento, red y clave propios de la filial, aunque resida en una instalación de tienda, y dentro de los topes que fija la filial emisora.
- **Se agregó:** Se autoriza contra un cupo preemitido de la filial emisora, que es un monto de compra que la filial autoriza de antemano y que se guarda en la tienda con almacenamiento, red y clave propios de la filial, aunque resida en una instalación de tienda, y dentro de los topes que fija la filial emisora.
- **Se agregó:** La Tabla 4.11 declara las funciones que no están disponibles sin enlace y el procedimiento manual que las suple (RT-03.13).
- **Se agregó:** \par\vspace{0pt plus 10\baselineskip}\penalty-300\vspace{0pt plus -10\baselineskip}
- **Se agregó:** Tabla 4.11: Funciones no disponibles sin enlace y procedimiento manual.
- **Se agregó:** Fuente: elaboración propia a partir de RT-03.13, SD-03 3.4.5 y el diseño de la tienda de esta subsección.\par\nopagebreak
- **Se agregó:** \begin{longtable}{@{}p{0.28\linewidth}p{0.20\linewidth}p{0.44\linewidth}@{}}
- **Se agregó:** \toprule Función & Sin enlace & Procedimiento manual \\
- **Se agregó:** \midrule\endhead\bottomrule\endlastfoot
- **Se agregó:** Originación de tarjetas y ampliación de cupos & No disponible. & La tienda informa al cliente que puede presentar la solicitud al restablecerse el enlace.
- **Se agregó:** \\
- **Se agregó:** Compra con tarjeta propia & No disponible si los topes no se fijan o la prueba falla. & La caja ofrece otro medio de pago habitual.
- **Se agregó:** \\
- **Se agregó:** Consulta de saldo, mora y comportamiento de pago & No disponible. & La tienda informa al cliente que la consulta se responde al volver el enlace.
- **Se agregó:** \\
- **Se agregó:** Emisión tributaria sin modalidad fiscal de contingencia aprobada & No disponible. & Con la modalidad aprobada con el Cliente, el ERP/DTE emite en contingencia y regulariza al volver el enlace.
- **Se agregó:** \\
- **Se agregó:** Existencia de otras tiendas y de otros canales & No disponible. & La caja informa solo la existencia local y confirma la de otros canales al volver el enlace.
- **Se agregó:** \\
- **Se agregó:** Controlador de lockers y aplicaciones móviles & No disponible, porque la autonomía de la tienda no los incluye automáticamente. & La atención se hace en el mesón o en la caja.
- **Se agregó:** \\
- **Se agregó:** Precios y promociones nuevos & No disponible. & Se aplica la última lista aprobada guardada en la tienda.
- **Se agregó:** \\
- **Se agregó:** Analítica en línea de la tienda & No disponible. & Las consultas esperan al restablecimiento del enlace y la venta no las necesita.
- **Se agregó:** \\
- **Se agregó:** \end{longtable}
- **Se agregó:** La Tabla 4.11 muestra que la venta, el cobro con los medios habituales y la consulta de existencia local siguen disponibles, y que cada función que se pierde tiene un procedimiento manual.
- **Se agregó:** La jefatura de tienda ejecuta esos procedimientos, la filial emisora define los dos primeros y todos se acuerdan con el Cliente, se enseñan en la transferencia de conocimiento y constan en el procedimiento operativo.
- **Motivo:** P-02 (opción 1) y agentes: funciones sin enlace y procedimiento manual; Parte 3 (opción 1): términos definidos en su primera mención
- **Base:** S-46; S-46b; RT-03.13; Lector no técnico

### CAM-042 · línea 548 · 4.1.13 Seguridad · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.10 → 4.12)
- **Base:** Comunicado 10

### CAM-043 · línea 552 · 4.1.13 Seguridad · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.10 → 4.12)
- **Base:** Comunicado 10

### CAM-044 · línea 567 · 4.1.13 Seguridad · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.7 → 4.8)
- **Base:** Comunicado 10

### CAM-045 · línea 583 · 4.1.14 Observabilidad · Modificado

- **Se quitó:** X-01 ejecuta su colector, Loki, Tempo, Prometheus y Grafana como cargas propias dentro de sus seis nodos base, sin máquinas auxiliares adicionales.
- **Se quitó:** Sus volúmenes persistentes, identidades y permisos son exclusivos de X-01 y no utilizan los repositorios de Retail ni de la filial emisora.
- **Se quitó:** El reparto de recursos reserva capacidad para el control de cruces y su observabilidad.
- **Se quitó:** La prueba de carga comprueba esa reserva y la continuidad ante la pérdida de un nodo.
- **Se quitó:** La misma definición de cargas y volúmenes se prepara en los seis nodos de espera de X-01 en Brasil.
- **Se agregó:** X-01 ejecuta su colector, Loki, Tempo, Prometheus y Grafana como cargas propias, con volúmenes persistentes, identidades y permisos exclusivos, y no utiliza los repositorios de Retail ni de la filial emisora.
- **Se agregó:** Su dimensionamiento y su copia en Brasil se tratan en la vista física (4.2).
- **Motivo:** C-016: nodos de X-01 quitados de 4.1.14
- **Base:** Criterio incluye/excluye

### CAM-046 · línea 603 · 4.1.15 Tecnologías y capacidades comunes · Agregado

- **Se agregó:** La Figura 4.11 muestra que las capacidades comunes se prestan por separado a cada frente y que lo único que Retail y la filial emisora comparten es la tecnología, no los datos ni los permisos.
- **Motivo:** C-017: explicación de la figura de capacidades comunes
- **Base:** Comunicado 10

### CAM-047 · línea 607 · 4.1.16 Decisiones y condiciones de aceptación · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.11 → 4.13)
- **Base:** Comunicado 10

### CAM-048 · línea 611 · 4.1.16 Decisiones y condiciones de aceptación · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.11 → 4.13)
- **Base:** Comunicado 10

### CAM-049 · línea 619 · 4.1.16 Decisiones y condiciones de aceptación · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.4 → 4.5)
- **Base:** Comunicado 10

### CAM-050 · línea 623 · 4.1.16 Decisiones y condiciones de aceptación · Modificado

- **Se quitó:** ADR-09 analítica & Condicionada. & Fabric, Synapse, Databricks y Azure AI Search como productos de base. & ADLS Gen2, Data Factory, PostgreSQL analítico dedicado y Power BI cubren la carga, el modelo y el informe, y Fabric completo no está disponible en Chile Central (Microsoft, 2026j). & Modelos e indicadores definidos, corte, frescura por indicador y reconstrucción de modelos e índices.
- **Se agregó:** ADR-09 analítica & Condicionada. & Fabric, Synapse, Databricks y Azure AI Search como productos de base. & ADLS Gen2, Data Factory, PostgreSQL analítico dedicado y Power BI cubren la carga, el modelo y el informe, y Fabric completo no está disponible en Chile Central (Microsoft, 2026j). & Capacidad de Power BI en Chile Central, modelos e indicadores definidos, corte, frescura por indicador y reconstrucción de modelos e índices.
- **Motivo:** C-018: condición de Power BI en ADR-09
- **Base:** S-23

### CAM-051 · línea 645 · 4.2 Arquitectura física · Modificado

- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/f44f4f31ae2b.png}
- **Se agregó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/diag-04-12_topologia-general.png}
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa

### CAM-052 · línea 648 · 4.2 Arquitectura física · Modificado

- **Se quitó:** Figura 4.12: Resumen de los sitios de la arquitectura física.
- **Se agregó:** Figura 4.12: Arquitectura física: sitios, conexiones y regiones.
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json

### CAM-053 · línea 650 · 4.2 Arquitectura física · Modificado

- **Se quitó:** En Chile Central, Retail, X-01 y la filial emisora tienen cada uno sus servicios, sus datos y su mensajería, y cada frente se copia a su contraparte en Brazil South.
- **Se agregó:** En Chile Central, Retail, X-01 y la filial emisora tienen cada uno sus servicios y sus datos, Retail y la filial emisora además su mensajería, y cada frente se copia a su contraparte en Brazil South.
- **Motivo:** Sesión A (08-11): introducción de 4.2 (accesos de DC-01, fila de Brasil)
- **Base:** Ver bitácora

### CAM-054 · línea 656 · 4.2 Arquitectura física · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.13 → 4.14)
- **Base:** Comunicado 10

### CAM-055 · línea 660 · 4.2 Arquitectura física · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.13 → 4.14)
- **Base:** Comunicado 10

### CAM-056 · línea 667 · 4.2 Arquitectura física · Modificado

- **Se quitó:** DC-01 & Cuatro racks de 42U, switches y firewall por negocio, dos pares de servidores de integración y los sistemas conservados. & Dos accesos de operador con un túnel por frente. & 0,2 Mbps y 110 Mbps durante una ola de migración. & Unos 2.600 km a Brazil South.
- **Se agregó:** DC-01 & Cuatro racks de 42U, switches y firewall por negocio, dos pares de servidores de integración y los sistemas conservados. & Dos accesos de operador propuestos, por rutas separadas, con un túnel por negocio. & 0,2 Mbps y 110 Mbps durante una ola de migración. & Unos 2.600 km a Brazil South.
- **Motivo:** Sesión A (08-11): introducción de 4.2 (accesos de DC-01, fila de Brasil)
- **Base:** Ver bitácora

### CAM-057 · línea 670 · 4.2 Arquitectura física · Modificado

- **Se quitó:** Brazil South & 50 máquinas virtuales de espera, 4 de Power BI apagadas y las contrapartes de los 12 PostgreSQL y de los dos Service Bus. & Réplica privada desde Chile por producto y entrada propia por frente. & Capacidad de réplica que mide el ensayo. & Es el sitio de recuperación.
- **Se agregó:** Brazil South & 50 máquinas virtuales de espera (40 nodos, 8 de apoyo y 2 sondas), 4 de gateway de Power BI apagadas, las contrapartes de los 12 PostgreSQL y de los dos Service Bus, y tres redes, tres firewalls y dos VPN Gateway. & Réplica privada desde Chile por producto y entrada propia por frente. & Capacidad de réplica que mide el ensayo. & Es el sitio de recuperación.
- **Motivo:** Sesión A (08-11): introducción de 4.2 (accesos de DC-01, fila de Brasil)
- **Base:** Ver bitácora

### CAM-058 · línea 673 · 4.2 Arquitectura física · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.13 → 4.14, 4.21 → 4.23)
- **Base:** Comunicado 10

### CAM-059 · línea 677 · 4.2.1 Especificaciones Implementos a proveer (Hardware y Software) · Modificado

- **Se quitó:** El Cliente ejecuta las canalizaciones, las obras eléctricas y el cableado, y Only Simple Solutions define sus requisitos y coordina su integración con la solución.
- **Se agregó:** El Cliente ejecuta las canalizaciones, las obras eléctricas y el cableado de tiendas y centros, y Only Simple Solutions define sus requisitos y coordina su integración con la solución.
- **Se agregó:** En DC-01, Only Simple Solutions provee además la conectividad, la seguridad y las canalizaciones del recinto técnico (RT-06.33), y el Cliente ejecuta la obra civil y las obras eléctricas.
- **Se agregó:** RT-06.33 se aplica al recinto técnico de DC-01, que es el site principal.
- **Se agregó:** En tiendas y centros de distribución, Only Simple Solutions especifica, configura y certifica la red y las canalizaciones, y el Cliente las compra y las ejecuta, porque el Caso le asigna esas compras y obras (Multitiendas Ancoa S.A., 2026, Caso 09, cap. 11, p. 27).
- **Se agregó:** Allí el proponente responde por los niveles de servicio con esa especificación y con un acta de recepción y un certificado de conformidad por sitio.
- **Se agregó:** El software nuevo y los servicios de nube se detallan en 4.1.1 y 4.2.3.
- **Motivo:** Ciclo 4.2.1 (08-11): H-16, RAID (S-34), CIS y parches (S-35), RT-06.33 (S-37), par de captura del proponente; además, renumeración de tablas o figuras
- **Base:** Ver bitácora

### CAM-060 · línea 679 · 4.2.1 Especificaciones Implementos a proveer (Hardware y Software) · Modificado

- **Se quitó:** Es una decisión de diseño del proponente: un árbitro en la nube no sirve, porque si la tienda pierde el enlace durante las 24 horas que exige RT-03.10 y además falla un servidor, el par quedaría sin árbitro y se detendría.
- **Se agregó:** Es una decisión de diseño del proponente.
- **Se agregó:** Un árbitro en la nube no sirve, porque si la tienda pierde el enlace durante las 24 horas que exige RT-03.10 y además falla un servidor, el par quedaría sin árbitro y se detendría.
- **Se agregó:** En cada servidor, las aplicaciones de cada negocio corren como contenedores separados, con su persistencia y sus agentes en el mismo servidor y sin una máquina virtual por función.
- **Se agregó:** El sistema operativo y el entorno de ejecución se fijan en la implementación.
- **Se agregó:** En tienda no hay hipervisor, porque las aplicaciones corren en contenedores sobre el sistema del servidor.
- **Se agregó:** Los dos discos de cada servidor forman un RAID 1, que es un espejo en que cada disco guarda una copia completa y permite seguir operando si uno falla, de modo que cada servidor ofrece 960 GB útiles de los 1.920 GB brutos.
- **Se agregó:** RAID 1 es el nivel que permiten dos discos por servidor, ya que RAID 5, 6 y 10 exigen más discos.
- **Se agregó:** Como un espejo no es un respaldo, cada negocio conserva además una copia local cifrada, separada de los servidores y con claves propias, que permite recuperar un dato borrado o dañado.
- **Se agregó:** Los servidores y equipos de la tienda se endurecen según los CIS Benchmarks aplicables, se administran de forma remota y centralizada con Intune y reciben parches en una ventana acordada con el Cliente fuera de los congelamientos (RT-03.15 y RT-03.18).
- **Motivo:** Ciclo 4.2.1 (08-11): H-16, RAID (S-34), CIS y parches (S-35), RT-06.33 (S-37), par de captura del proponente
- **Base:** Ver bitácora

### CAM-061 · línea 681 · 4.2.1 Especificaciones Implementos a proveer (Hardware y Software) · Modificado

- **Se quitó:** Retail usa las VLAN 10, 11 y 12, la filial emisora las 20, 21 y 22, X-01 la 23, y los segmentos de apoyo son la 40 para sensores y lockers, la 50 para cámaras, la 60 para los clientes invitados y la 70 para la administración.
- **Se agregó:** Hay segmentos separados para cada negocio, para X-01, para sensores y lockers, para cámaras, para los clientes invitados y para la administración.
- **Motivo:** Ciclo 4.2.1 (08-11): H-16, RAID (S-34), CIS y parches (S-35), RT-06.33 (S-37), par de captura del proponente; además, renumeración de tablas o figuras
- **Base:** Ver bitácora

### CAM-062 · línea 684 · 4.2.1 Especificaciones Implementos a proveer (Hardware y Software) · Modificado

- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/fb4f17cc7840.png}
- **Se agregó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/diag-04-13_tienda-red-servidores.png}
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa

### CAM-063 · línea 687 · 4.2.1 Especificaciones Implementos a proveer (Hardware y Software) · Modificado

- **Se quitó:** Figura 4.19: Tienda tipo, red y servidores locales.
- **Se agregó:** Figura 4.13: Tienda tipo: red, servidores y equipos.
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json

### CAM-064 · línea 689 · 4.2.1 Especificaciones Implementos a proveer (Hardware y Software) · Modificado

- **Se quitó:** Su capacidad mínima es de 5 Mbps sostenidos frente a los 4,8 Mbps del pico de la tienda (SD-05, Tabla 5.19), y se confirma con un estudio de cobertura por sitio.
- **Se agregó:** Su capacidad mínima es de 5 Mbps sostenidos frente a los 4,8 Mbps del pico de la tienda, que ya incluye un margen de 1,5 (SD-05, Tabla 5.19), y se confirma con un estudio de cobertura por sitio.
- **Motivo:** Ciclo 4.2.1 (08-11): H-16, RAID (S-34), CIS y parches (S-35), RT-06.33 (S-37), par de captura del proponente
- **Base:** Ver bitácora

### CAM-065 · línea 691 · 4.2.1 Especificaciones Implementos a proveer (Hardware y Software) · Modificado

- **Se quitó:** Los equipos se alojan en tres racks de 24U, uno para los servidores de Retail, otro para los de la filial emisora y otro para las comunicaciones, con 31 de 72U ocupadas al inicio.
- **Se quitó:** Cada rack tiene dos PDU, que son regletas de distribución eléctrica, conectadas a ramas distintas, y la alimentación viene de dos UPS, que son baterías de respaldo, de 6 kW cada una, capaces de sostener por separado la carga completa durante 30 minutos.
- **Se quitó:** Un transferidor automático conecta un grupo electrógeno inicial de 20 kVA o una fuente del edificio que se acredite, que sostiene la carga esencial mientras dura el corte, y las baterías cubren solo la transferencia.
- **Se quitó:** El cableado nuevo es de categoría 6 con cubierta de baja emisión de humos (LSZH), con un recorrido máximo de 90 metros de enlace permanente, y los recorridos mayores se resuelven con fibra óptica OS2 hacia un armario de distribución y no con cobre más largo.
- **Se agregó:** Los equipos se alojan en tres racks de 24U, uno para los servidores de Retail, otro para los de la filial emisora y otro para las comunicaciones, con 31 de 72U ocupadas al inicio, que son 8 de Retail, 8 de la filial emisora y 15 de comunicaciones.
- **Se agregó:** Cada rack tiene dos PDU, que son regletas de distribución eléctrica, conectadas a ramas distintas, y la alimentación viene de dos UPS, que son baterías de respaldo, de 6 kVA cada una, capaces de sostener por separado la carga completa durante 30 minutos.
- **Se agregó:** Un transferidor automático conecta un grupo electrógeno inicial de 20 kVA o una fuente del edificio que se acredite, que sostiene la carga esencial mientras dura el corte, y las baterías cubren la transferencia y los cortes breves, con 30 minutos como margen de diseño.
- **Se agregó:** El cableado nuevo es de categoría 6 con cubierta de baja emisión de humos, hasta 90 metros por enlace, y los recorridos mayores usan fibra óptica.
- **Motivo:** Parte 7 (opción 1): origen de las 31 de 72U; además, renumeración de tablas o figuras
- **Base:** cierre-inventario/12

### CAM-066 · línea 694 · 4.2.1 Especificaciones Implementos a proveer (Hardware y Software) · Modificado

- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/0c9d8da5748c.png}
- **Se agregó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/diag-04-14_tienda-energia-espacio.png}
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa

### CAM-067 · línea 697 · 4.2.1 Especificaciones Implementos a proveer (Hardware y Software) · Modificado

- **Se quitó:** Figura 4.20: Tienda tipo, energía y espacio.
- **Se agregó:** Figura 4.14: Tienda tipo: energía y espacio.
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json

### CAM-068 · línea 699 · 4.2.1 Especificaciones Implementos a proveer (Hardware y Software) · Modificado

- **Se quitó:** Los servidores son un par local de captura que mantiene la recepción y el despacho cuando falla el enlace y que no duplica el WMS que el Cliente conserva.
- **Se quitó:** La red de cada centro tiene su firewall, su switching, sus puntos de acceso inalámbrico y un router 4G/5G de respaldo, que en CD-02 es el segundo camino del enlace único que describe el Caso, y se propone al Cliente un segundo enlace fijo.
- **Se quitó:** Las cantidades de equipos de red, la cobertura de la nave y los servidores del WMS se fijan en el levantamiento de cada centro, y la Figura 4.26 muestra la disposición de ambos.
- **Se agregó:** Los servidores son un par local de captura que provee Only Simple Solutions y que registra en el propio centro los movimientos de recepción y despacho mientras no hay enlace, con 100 GB útiles de reserva preliminar que se fijan al medir el pico.
- **Se agregó:** En CD-01 no duplica el sistema de gestión de almacenes (WMS) que el Cliente conserva, y CD-02 no tiene WMS.
- **Se agregó:** La red de cada centro tiene su firewall, su switching, sus puntos de acceso inalámbrico y un router 4G/5G de respaldo, y los enlaces de cada centro se describen en 4.3.1.
- **Se agregó:** Las cantidades de equipos de red, la cobertura de la nave y los servidores del WMS se fijan en el levantamiento de cada centro.
- **Motivo:** Ciclo 4.2.1 (08-11): H-16, RAID (S-34), CIS y parches (S-35), RT-06.33 (S-37), par de captura del proponente
- **Base:** Ver bitácora

### CAM-069 · línea 701 · 4.2.1 Especificaciones Implementos a proveer (Hardware y Software) · Modificado

- **Se quitó:** En DC-01 el recinto reserva cuatro racks de 42U, uno para los servidores de Retail, otro para los de la filial emisora, otro para las comunicaciones y otro para el respaldo local, con una reserva inicial de 80 de 168U.
- **Se quitó:** Aloja los sistemas actuales que se conservan, como supuesto que el levantamiento confirma, y dos pares de servidores de integración, uno por negocio, que extraen los datos hacia Azure.
- **Se quitó:** La solución nueva no instala allí datos financieros nuevos, y la zona de Retail y la de la filial emisora tienen redes, switches y firewall propios, como describe la Figura 4.25.
- **Se agregó:** En DC-01, Only Simple Solutions habilita el recinto técnico con cuatro racks de 42U, dos pares de servidores de integración, el de la filial emisora transitorio y el de Retail condicionado a la interfaz del proveedor, y los equipos de conectividad y seguridad de cada negocio.
- **Se agregó:** Los servidores de integración del recinto usan virtualización, y su producto y su licenciamiento a nombre del Cliente se fijan en el levantamiento de la Etapa 1.
- **Se agregó:** La subsección 4.3.1 describe el recinto, su separación por negocio y su energía.
- **Motivo:** Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/correspondencia-figuras.json

### CAM-070 · línea 703 · 4.2.1 Especificaciones Implementos a proveer (Hardware y Software) · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.22 → 4.15)
- **Base:** Comunicado 10

### CAM-071 · línea 707 · 4.2.1 Especificaciones Implementos a proveer (Hardware y Software) · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.22 → 4.15)
- **Base:** Comunicado 10

### CAM-072 · línea 712 · 4.2.1 Especificaciones Implementos a proveer (Hardware y Software) · Modificado

- **Se quitó:** Tienda (red) & Cuatro firewalls, cuatro switches, puntos inalámbricos y cableado de categoría 6 LSZH. & Especificación, configuración de red y verificación de integración y certificaciones. & Compra e instalación de equipos de red y ejecución del cableado con certificación por su instalador.
- **Se agregó:** Tienda (red) & Cuatro firewalls, cuatro switches, puntos inalámbricos y cableado de categoría 6 de baja emisión de humos. & Especificación, configuración de red y verificación de integración y certificaciones. & Compra e instalación de equipos de red y ejecución del cableado con certificación por su instalador.
- **Motivo:** Ciclo 4.2.1 (08-11): H-16, RAID (S-34), CIS y parches (S-35), RT-06.33 (S-37), par de captura del proponente
- **Base:** Ver bitácora

### CAM-073 · línea 714 · 4.2.1 Especificaciones Implementos a proveer (Hardware y Software) · Modificado

- **Se quitó:** Tienda (energía y espacio) & Tres racks de 24U, dos UPS de 6 kW, seis PDU, transferidor, clima y sensores. & Provisión y puesta en servicio de equipos nuevos de energía y recinto, especificación de obras y ensayo de autonomía. & Ejecución de obras civiles, canalizaciones e instalación eléctrica, y fuente del edificio cuando se acredita.
- **Se quitó:** Dispositivos de terreno & POS, terminales de pago, impresoras, lectores y móviles. & Especificación, integración, enrolamiento y administración de la configuración. & Compra y puesta a disposición de equipos, con sus garantías y reparación física.
- **Se quitó:** Centros de distribución & Dos racks de 24U, par local de captura, red y router 4G/5G por centro. & Especificación, configuración, integración y mantenimiento del software nuevo. & Compra e instalación del equipamiento del centro, obras, enlaces, planes de datos y soporte del WMS conservado.
- **Se quitó:** DC-01 & Cuatro racks de 42U, red por negocio y dos pares de integración. & Provisión del cómputo nuevo y habilitación técnica, especificación de obras, configuración e integración. & Espacio, compra e instalación de equipos de red, ejecución de obras y cableado, y sistemas conservados.
- **Se agregó:** Tienda (energía y espacio) & Tres racks de 24U, dos UPS de 6 kVA, seis PDU, transferidor, grupo electrógeno inicial, clima y sensores. & Provisión y puesta en servicio de equipos nuevos de energía y recinto, especificación de obras y ensayo de autonomía. & Ejecución de obras civiles, canalizaciones e instalación eléctrica, y fuente del edificio cuando se acredita.
- **Se agregó:** Dispositivos de terreno & POS, terminales de pago, impresoras, lectores y móviles. & Especificación, integración, enrolamiento y administración de la configuración, con actualización de firmware, bloqueo y borrado remoto (RT-03.18). & Compra y puesta a disposición de equipos, con sus garantías y reparación física.
- **Se agregó:** Centros de distribución & Dos racks de 24U, par local de captura, red y router 4G/5G por centro. & Provisión del par local de captura, especificación, configuración, integración y mantenimiento del software nuevo. & Compra e instalación del resto del equipamiento del centro, obras, enlaces, planes de datos y soporte del WMS conservado.
- **Se agregó:** DC-01 & Cuatro racks de 42U, equipos de conectividad y seguridad por negocio, dos pares de integración y los sistemas de energía, climatización, incendio y acceso del recinto técnico. & Provisión del cómputo nuevo, de los equipos de conectividad y seguridad y de los sistemas del recinto técnico, canalizaciones hasta el rack, habilitación técnica, especificación de obras, configuración e integración. & Espacio, obra civil de separación, obras, cableado y sistemas conservados.
- **Motivo:** P-09 (opción 1): frontera canalizaciones y cableado
- **Base:** S-41; RT-06.33

### CAM-074 · línea 721 · 4.2.1 Especificaciones Implementos a proveer (Hardware y Software) · Modificado

- **Se quitó:** El detalle consta en el Formulario T-11 y en el inventario adj-sd-04\_s2\_inventario-hardware.xlsx, y el ensayo de continuidad de 24 horas valida después el dimensionamiento de los servidores de cada tienda.
- **Se agregó:** El detalle consta en el Formulario T-11, y el ensayo de continuidad de 24 horas valida después el dimensionamiento de los servidores de cada tienda.
- **Motivo:** Ciclo 4.2.1 (08-11): H-16, RAID (S-34), CIS y parches (S-35), RT-06.33 (S-37), par de captura del proponente; además, renumeración de tablas o figuras
- **Base:** Ver bitácora

### CAM-075 · línea 731 · 4.2.2 Supuestos del emplazamiento · Modificado

- **Se quitó:** La Tabla 4.14 ubica cada componente en su sitio sin asignar una ubicación inventada a los sistemas existentes.
- **Se agregó:** Además, el proponente declara la tipología de cada sitio según el capítulo 6 de las Bases Transversales.
- **Se agregó:** DC-01 es sala técnica principal, por alojar sistemas conservados del Cliente (4.3.1).
- **Se agregó:** La tienda tipo y los centros de distribución son sala técnica secundaria o de sitio, porque requieren cómputo local para continuidad sin albergar el núcleo, un criterio más exigente que el gabinete que menciona el Caso.
- **Se agregó:** DC-02 queda sin tipología hasta acreditar su uso.
- **Se agregó:** Las 22 tiendas se diseñan como una tienda tipo, con tres variantes (centro comercial, insignia y Coyhaique) que no tienen cifras propias hasta que el Cliente entregue el padrón de cajas, planos, energía y cobertura móvil.
- **Se agregó:** La Tabla 4.16 ubica cada componente en su sitio y justifica el emplazamiento según el artículo 16.2 de las Bases Administrativas, que pide considerar latencia, criticidad, volumen de datos, restricciones regulatorias, disponibilidad de conectividad y costo total.
- **Se agregó:** El costo se expresa en palabras, sin cifras, y no se asigna una ubicación inventada a los sistemas existentes.
- **Motivo:** Sesión A (08-11): tipología por sitio (S-33) y Tabla de los seis factores del Art. 16.2
- **Base:** Ver bitácora

### CAM-076 · línea 737 · 4.2.2 Supuestos del emplazamiento · Modificado

- **Se quitó:** Tabla 4.14: Emplazamiento de los componentes de la solución.
- **Se quitó:** Fuente: elaboración propia a partir de 4.1, el Caso 09 y SD-03.\par\nopagebreak
- **Se quitó:** \begin{longtable}{@{}p{0.30\linewidth}p{0.26\linewidth}p{0.36\linewidth}@{}}
- **Se quitó:** \toprule Componente lógico & Emplazamiento propuesto & Condición de diseño \\
- **Se agregó:** Tabla 4.16: Emplazamiento de cada componente y su justificación según el artículo 16.2.
- **Se agregó:** Fuente: elaboración propia a partir de 4.1, el Caso 09, RT-03 y SD-03.\par\nopagebreak
- **Se agregó:** \begin{longtable}{@{}p{0.22\linewidth}p{0.19\linewidth}p{0.19\linewidth}p{0.18\linewidth}p{0.20\linewidth}@{}}
- **Se agregó:** \toprule Componente y emplazamiento & Latencia y conectividad & Criticidad y volumen & Regulación & Costo total \\
- **Motivo:** Sesión A (08-11): tipología por sitio (S-33) y Tabla de los seis factores del Art. 16.2
- **Base:** Ver bitácora

### CAM-077 · línea 741 · 4.2.2 Supuestos del emplazamiento · Modificado

- **Se quitó:** Entrada pública, API y servicios propios & Azure Chile Central, con recuperación en Azure Brazil South. & Tres zonas para cargas críticas, acceso privado a aplicación y datos, y recursos propios por frente.
- **Se quitó:** Mensajería (Service Bus) y bases de datos & Bases replicadas en Brazil South y namespace de recuperación por negocio. & RPO y RTO por servicio, recuperación de registros durables y republicación probada.
- **Se quitó:** Analítica Retail y de la filial emisora & Cuentas de almacenamiento y bases analíticas separadas en la nube. & Permisos y claves por frente, y cruce solo por contrato aprobado.
- **Se quitó:** POS y diario de contingencia & Terminal y un par de servidores locales por negocio en cada tienda. & Autonomía de 24 horas sin enlace, discos espejados y retorno conciliado.
- **Se quitó:** Adaptadores a sistemas conservados & Nube o centro de datos según interfaz y ubicación comprobadas. & No fijar ruta ni latencia antes de levantar las catorce interfaces.
- **Se quitó:** ERP/DTE y WMS & Permanecen en sus plataformas actuales, que se suponen en DC-01 y CD-01. & Alojamiento individual y conectividad por verificar.
- **Se quitó:** Marketplace & Externo según el supuesto, con API para vendedores en CLD-01 y adaptador hacia la plataforma. & Se conserva, y su conexión se verifica por interfaz.
- **Se quitó:** Comercio electrónico y fidelización & Externos según el supuesto, con entrada por la API de CLD-01 y adaptadores que les envían precios y existencias. & Conservación o sustitución condicionada a pruebas de Etapa 1.
- **Se agregó:** Entrada pública, en Azure Chile Central y el borde global de Azure. & Disponibilidad en 400 ms de extremo a extremo (RT-09.01), por Internet y enlace privado al origen. & Máxima para el canal digital, con 693 consultas por segundo en el peak. & Filtro contra ataques y políticas separadas por negocio. & Un servicio global Premium con enlace privado y filtro en un solo punto, y un perfil y una puerta por negocio por la línea roja.
- **Se agregó:** Servicios de negocio, en un clúster por frente de Chile Central. & En la misma región que sus bases, sin salto entre regiones. & Máxima, porque ahí corren la venta y el crédito, con 17, 17 y 6 nodos. & Sin compartir nodo entre frentes. & Se pagan nodos de más para resistir la pérdida de una zona.
- **Se agregó:** Bases PostgreSQL, 12 servidores en Chile Central con réplica en Brazil South. & Aplicación y base en la misma región, y réplica con retraso medido. & Máxima, son la fuente de verdad, con 4.500 GiB iniciales. & Una autoridad por dato, separadas por negocio y sin IP pública. & Se paga primario y espera en zonas distintas y una réplica en Brasil por servidor.
- **Se agregó:** Mensajería, un Service Bus Premium por negocio en Chile Central. & En la misma región, con registros durables para recuperar. & Alta, porque desacopla la venta de sus destinos, con 6.667 entregas por segundo en el pico de precios. & Sin puente entre negocios. & Nivel Premium por red privada y capacidad reservada.
- **Se agregó:** Analítica y archivo, con Data Lake, Blob y Power BI en Chile Central. & Sin objetivo propio, por no estar en la ruta de la venta. & Media la analítica y alta el archivo, con 3 y 2 TiB de Data Lake y archivo de 25 y 12 TiB. & Retención del Caso y borrado con segunda persona, en cuentas por negocio. & Archivo inmutable y copia entre regiones, aceptados por exigencia legal.
- **Se agregó:** POS, servidores y diario local, en cada tienda. & Caja a servidores en 10 ms y entre el par en 5 ms, como criterio de ingeniería. & Máxima, con 24 horas sin enlace (RT-03.10) y 4,8 Mbps en peak. & Retail y filial separados, sin datos de cartera en el servidor de Retail. & Cuatro servidores cuestan menos que perder la venta de una tienda en un corte.
- **Se agregó:** Adaptadores y sistemas conservados, en la nube o en DC-01 y CD-01 según la interfaz. & Sin ruta ni latencia fijas hasta levantar las 14 interfaces. & Alta mientras convivan, con el ERP/DTE como único emisor tributario. & Ningún adaptador entrega datos de crédito a Retail. & Se conservan los sistemas, sin costo de reemplazo.
- **Se agregó:** Recuperación, en Azure Brazil South. & Entre 40 y 55 ms estimados desde Chile Central, sin objetivo propio. & Máxima si Chile cae, con 50 máquinas encendidas y 4 apagadas. & Residencia sujeta a la aprobación del Cliente y a la Ley 21.719. & Se pagan los nodos encendidos aunque no atiendan tráfico, para no comprometer el RTO.
- **Se agregó:** Servidores de integración y red del recinto, en DC-01. & Hacia Chile Central por VPN en 100 ms. & Media y alta mientras convivan los sistemas conservados. & Redes y permisos separados para Retail y la filial. & No se compra equipo nuevo más allá de lo que el levantamiento justifique.
- **Se agregó:** \\
- **Se agregó:** Par local de captura, en cada centro de distribución. & Captura al diario local en 10 ms, por validar. & Alta durante los cortes, con 100 GB útiles de reserva preliminar. & Regla de 24 horas sin enlace (RT-03.10). & Dos servidores por centro, sin duplicar el WMS.
- **Se agregó:** \\
- **Se agregó:** Seguridad y observabilidad, por frente en Chile Central y Sentinel en Brazil South. & Sin objetivo propio, salvo el inicio de sesión. & Máxima en identidad y claves. & Sentinel transfiere registros de seguridad sujeto a aprobación. & Se duplican claves y registros por frente para no compartirlos.
- **Se agregó:** \\
- **Motivo:** Sesión A (08-11): tipología por sitio (S-33) y Tabla de los seis factores del Art. 16.2
- **Base:** Ver bitácora

### CAM-078 · línea 754 · 4.2.2 Supuestos del emplazamiento · Modificado

- **Se quitó:** La Tabla 4.14 confirma que solo los servicios nuevos tienen emplazamiento definido, y que los adaptadores quedan sujetos a la ubicación que compruebe el inventario.
- **Se agregó:** La Tabla 4.16 confirma que cada grupo de componentes nuevos tiene un emplazamiento con sus seis factores, reunidos en cinco columnas, y que la Tabla 4.22 detalla sus cantidades.
- **Se agregó:** Los adaptadores quedan sujetos a la ubicación que compruebe el inventario.
- **Motivo:** Sesión A (08-11): tipología por sitio (S-33) y Tabla de los seis factores del Art. 16.2; además, renumeración de tablas o figuras
- **Base:** Ver bitácora

### CAM-079 · línea 758 · 4.2.2 Supuestos del emplazamiento · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.15 → 4.17)
- **Base:** Comunicado 10

### CAM-080 · línea 776 · 4.2.3 Servicios contratados en Azure · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.12 → 4.1, 4.16 → 4.18)
- **Base:** Comunicado 10

### CAM-081 · línea 780 · 4.2.3 Servicios contratados en Azure · Modificado

- **Se quitó:** Por ejemplo, rg-filial-prd-cl-datos contiene las bases de datos, el lago de datos y el almacenamiento inmutable de la filial emisora en producción en Chile Central.
- **Se agregó:** Por ejemplo, rg-filial-prd-cl-datos contiene las bases de datos, el Data Lake y el almacenamiento inmutable de la filial emisora en producción en Chile Central.
- **Motivo:** Cierre parte 2: «Data Lake» en lugar de «lago de datos»
- **Base:** Glosario 08

### CAM-082 · línea 784 · 4.2.3 Servicios contratados en Azure · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.16 → 4.18)
- **Base:** Comunicado 10

### CAM-083 · línea 788 · 4.2.3 Servicios contratados en Azure · Modificado

- **Se quitó:** Entrada y borde & Front Door con firewall de aplicaciones web (la recepción pública), Application Gateway (la puerta privada de cada frente), API Management Premium (la puerta de las interfaces de programación) y DNS público. & Reciben a los clientes y a las contrapartes, filtran ataques y entregan cada petición al frente que corresponde. & Borde de Azure y subred de entrada de Retail y de la filial emisora.
- **Se agregó:** Entrada y borde & Front Door con firewall de aplicaciones web (la recepción pública), Application Gateway (la puerta de cada negocio), API Management Premium (la puerta de las interfaces de programación) DNS público y Azure DDoS Protection (el escudo contra saturación de la entrada). & Reciben a los clientes y a las contrapartes, filtran ataques y entregan cada petición al frente que corresponde. & Borde de Azure y subred de entrada de Retail y de la filial emisora.
- **Motivo:** Sesión A (08-11): servicios contratados (DDoS, External ID, Private Access, Intune, Redis B20, FinOps, reversibilidad)
- **Base:** Ver bitácora

### CAM-084 · línea 791 · 4.2.3 Servicios contratados en Azure · Modificado

- **Se quitó:** Datos y analítica & PostgreSQL Flexible Server (la base de datos), Azure Managed Redis (memoria rápida para consultas frecuentes), Data Lake Storage Gen2, Blob Storage con archivo inmutable, Data Factory y Power BI. & Guardan los datos transaccionales, aceleran las consultas de Retail, conservan la evidencia y alimentan los tableros. & Subredes de datos de cada frente, con Redis solo en Retail y la evidencia vigente solo en la filial emisora.
- **Se quitó:** Seguridad e identidad & Microsoft Entra ID (quién entra), Key Vault y Managed HSM (cajas fuertes de claves), Defender for Cloud y Sentinel (detección de amenazas). & Controlan quién entra, guardan claves y secretos, y detectan y registran amenazas. & Una bóveda y un espacio de registro por frente y, para la filial emisora y X-01, un Managed HSM condicionado a su disponibilidad.
- **Se agregó:** Datos y analítica & PostgreSQL Flexible Server (la base de datos), Azure Managed Redis, nivel Balanced B20 de 24 GB (memoria rápida para consultas frecuentes), Data Lake Storage Gen2, Blob Storage con archivo inmutable, Data Factory y Power BI. & Guardan los datos transaccionales, aceleran las consultas de Retail, conservan la evidencia y alimentan los tableros. & Subredes de datos de cada frente, con Redis solo en Retail y la evidencia vigente solo en la filial emisora.
- **Se agregó:** Seguridad e identidad & Microsoft Entra ID (quién entra), Entra External ID (identidad de los clientes), Entra Private Access, Intune (administración de los dispositivos), Key Vault y Managed HSM (cajas fuertes de claves), Defender for Cloud y Sentinel (detección de amenazas). & Controlan quién entra, guardan claves y secretos, y detectan y registran amenazas. & Una bóveda y un espacio de registro por frente y, para la filial emisora y X-01, un Managed HSM condicionado a su disponibilidad.
- **Motivo:** C-003: Redis B20 verificado
- **Base:** S-26

### CAM-085 · línea 796 · 4.2.3 Servicios contratados en Azure · Modificado

- **Se quitó:** Azure Managed Redis reemplaza a Azure Cache for Redis, que Microsoft retira el 30 de septiembre de 2028, antes del fin del contrato en 2031 (Microsoft, 2026k, 2026t).
- **Se agregó:** Azure Managed Redis reemplaza a Azure Cache for Redis, que Microsoft retira el 30 de septiembre de 2028, antes del fin del contrato en 2031 (Microsoft, 2026k, 2026u).
- **Se agregó:** Los nodos de los clústeres usan máquinas virtuales de la serie Ddsv5 en cuatro tamaños.
- **Se agregó:** Bastion Premium con zonas en Chile Central está en vista previa de Microsoft, y la cuota y la disponibilidad por zona se comprueban en la suscripción.
- **Se agregó:** La gestión de costos sigue prácticas FinOps, con etiquetado obligatorio, presupuestos y alertas de desviación por grupo de administración y un reporte mensual de consumo al Cliente.
- **Se agregó:** La reversibilidad distingue lo portable, que son los contenedores, PostgreSQL, OpenTelemetry, los Data Lake y el software de tienda, de lo propio del proveedor, que son API Management, Service Bus, el borde y la red, las claves, Entra y la observabilidad de Azure, según el Formulario T-11.12.
- **Motivo:** P-01: cita de la tabla de regiones de PostgreSQL; además, renumeración de tablas o figuras
- **Base:** Art. 16.3

### CAM-086 · línea 804 · 4.2.4 Redes y segmentación · Modificado

- **Se quitó:** La Figura 4.13 muestra la red de un frente tipo, que Retail y la filial emisora repiten con su propio rango.
- **Se agregó:** La Figura 4.15 muestra la red de los tres frentes, y Retail y la filial emisora repiten la misma red central con su propio rango.
- **Motivo:** Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/correspondencia-figuras.json

### CAM-087 · línea 807 · 4.2.4 Redes y segmentación · Modificado

- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/10c2ea3cb93b.png}
- **Se agregó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/diag-04-15_red-chile-central.png}
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa

### CAM-088 · línea 810 · 4.2.4 Redes y segmentación · Modificado

- **Se quitó:** Figura 4.13: Red de Azure Chile Central de un frente tipo.
- **Se agregó:** Figura 4.15: Red y entrada de Azure Chile Central por frente, incluida la red de X-01.
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json

### CAM-089 · línea 812 · 4.2.4 Redes y segmentación · Modificado

- **Se quitó:** El VPN Gateway termina los túneles IPsec de las tiendas, los centros de distribución y DC-01, que son conexiones cifradas por Internet, y el Azure Firewall Premium revisa el tráfico que sale del frente y el que llega de los sitios.
- **Se agregó:** El VPN Gateway termina los túneles IPsec de las tiendas, los centros de distribución y DC-01, que son conexiones cifradas por Internet por los puertos UDP 500 y 4500, y el Azure Firewall Premium revisa el tráfico que sale del frente y el que llega de los sitios.
- **Motivo:** Sesión A (08-11): puertos solo en entrada pública, túneles y cruce; Private Link Service (S-11); además, renumeración de tablas o figuras
- **Base:** Ver bitácora

### CAM-090 · línea 814 · 4.2.4 Redes y segmentación · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.17 → 4.19)
- **Base:** Comunicado 10

### CAM-091 · línea 818 · 4.2.4 Redes y segmentación · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.17 → 4.19)
- **Base:** Comunicado 10

### CAM-092 · línea 836 · 4.2.4 Redes y segmentación · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.17 → 4.19)
- **Base:** Comunicado 10

### CAM-093 · línea 838 · 4.2.4 Redes y segmentación · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.13 → 4.15)
- **Base:** Comunicado 10

### CAM-094 · línea 840 · 4.2.4 Redes y segmentación · Modificado

- **Se quitó:** Una compra en línea entra por Front Door, que es la recepción pública de Azure y filtra ataques a las páginas y a las interfaces de programación, y los bots, y llega por Private Link, una conexión privada dentro de Azure, a la subred de entrada del frente.
- **Se quitó:** Front Door Premium ofrece Private Link solo en algunas regiones, entre ellas Brazil South, y Chile Central no figura, por lo que la conexión privada hacia Chile Central se crea en Brazil South, la región compatible más cercana, y se agrega un segundo origen privado del mismo Application Gateway con otra región compatible, East US, con menor prioridad, para que la entrada no dependa de un solo clúster regional de Front Door, como recomienda Microsoft (Microsoft, 2026r).
- **Se agregó:** Una compra en línea entra por Front Door (HTTPS, puerto 443), que es la recepción pública de Azure y filtra ataques a las páginas y a las interfaces de programación, y los bots, y llega por Private Link, una conexión privada dentro de Azure, a la subred de entrada del frente.
- **Se agregó:** Front Door Premium ofrece Private Link solo en algunas regiones, entre ellas Brazil South, y Chile Central no figura, por lo que la conexión privada hacia Chile Central se crea en Brazil South, la región compatible más cercana, y se agrega un segundo punto privado hacia el mismo Application Gateway, por East US y con menor prioridad, para que la entrada no dependa de un solo clúster regional de Front Door, como recomienda Microsoft (Microsoft, 2026r).
- **Se agregó:** Esos puntos privados son puntos de paso del tráfico hacia Chile Central, donde se guardan los datos de la producción habitual.
- **Motivo:** Sesión A (08-11): puertos solo en entrada pública, túneles y cruce; Private Link Service (S-11)
- **Base:** Ver bitácora

### CAM-095 · línea 842 · 4.2.4 Redes y segmentación · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.14 → 4.15)
- **Base:** Comunicado 10

### CAM-096 · línea 844 · 4.2.4 Redes y segmentación · Eliminado

- **Se quitó:** \begin{center}
- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/d0650bf21604.png}
- **Se quitó:** \end{center}
- **Motivo:** Sesión A (08-11): puertos solo en entrada pública, túneles y cruce; Private Link Service (S-11)
- **Base:** Ver bitácora

### CAM-097 · línea 845 · 4.2.4 Redes y segmentación · Modificado

- **Se quitó:** Figura 4.14: Red de X-01, única puerta entre Retail y la filial emisora.
- **Se quitó:** Fuente: elaboración propia a partir de RT-03 y SD-03.
- **Se quitó:** En la Figura 4.14, la única ruta es la compra autorizable, que va del servicio de ventas de Retail a un listener privado de X-01, que es un punto de entrada restringido que solo acepta ese contrato, y de ahí, con los datos mínimos, a la entrada de autorización de la filial emisora.
- **Se quitó:** X-01 tiene su propio hub, firewall, claves y bitácora (pg-x01), no recibe túneles de sitios salvo necesidad acreditada, y la entrada y la salida de X-01 se resuelven con Private Link Service o con un proxy de contrato, según la prueba de viabilidad.
- **Se agregó:** En la Figura 4.15, la única ruta es la compra autorizable, que va por HTTPS privado del servicio de ventas de Retail a un listener privado de X-01, que es un punto de entrada restringido que solo acepta ese contrato, y de ahí, con los datos mínimos, a la entrada de autorización de la filial emisora.
- **Se agregó:** X-01 tiene su propio hub, firewall, claves y bitácora, no recibe túneles de sitios salvo necesidad acreditada, y la entrada y la salida de X-01 se resuelven con Private Link Service sobre el balanceador interno, y con un proxy de contrato solo si falla la prueba de viabilidad.
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11); Cierre parte 2: se quitan nombres internos de recursos; además, renumeración de tablas o figuras
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json; Glosario 08, regla 1

### CAM-098 · línea 849 · 4.2.5 Ambientes · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.15 → 4.16)
- **Base:** Comunicado 10

### CAM-099 · línea 852 · 4.2.5 Ambientes · Modificado

- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/ead70a0335fe.png}
- **Se agregó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/diag-04-16_entrega-ambientes.png}
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa

### CAM-100 · línea 855 · 4.2.5 Ambientes · Modificado

- **Se quitó:** Figura 4.15: Canal de entrega de la solución y registros de imágenes por frente.
- **Se agregó:** Figura 4.16: Canal de entrega y ambientes por frente.
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json

### CAM-101 · línea 857 · 4.2.5 Ambientes · Modificado

- **Se quitó:** Esa imagen se construye una vez y cada frente la publica en su propio registro de imágenes (Azure Container Registry Premium), mediante un agente efímero, que es un ejecutor que se crea para cada tarea y se elimina al terminar, con una identidad federada y sin credenciales permanentes.
- **Se agregó:** Esa imagen se construye una vez y cada frente la publica en su propio registro de imágenes (Azure Container Registry Premium), mediante un agente efímero, que es un ejecutor que se crea para cada tarea y se elimina al terminar, y que corre en un conjunto de escalado de máquinas virtuales de Chile Central, con una identidad federada y sin credenciales permanentes en las conexiones de despliegue, salvo la clave que exige crear el grupo de agentes.
- **Motivo:** Sesión A (08-11): ambientes (S-05), agentes de entrega (S-28), sin marcha blanca
- **Base:** Ver bitácora

### CAM-102 · línea 859 · 4.2.5 Ambientes · Eliminado

- **Se quitó:** \begin{center}
- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/c73b0fee0dfa.png}
- **Se quitó:** \end{center}
- **Se quitó:** Figura 4.16: Ambientes y promoción por frente.
- **Se quitó:** Fuente: elaboración propia a partir de RT-03, RT-04, RT-07 y SD-03.
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json

### CAM-103 · línea 862 · 4.2.5 Ambientes · Modificado

- **Se quitó:** El ambiente de Recuperación ante Desastres reside en CLD-02 y se crea con la misma definición de infraestructura, de modo que es igual al de producción y no se va desviando con el tiempo.
- **Se quitó:** El paso a producción de cada etapa, que son los de los meses 16 y 21, se hace en marcha blanca, en convivencia con la operación vigente, y cae fuera de las cinco ventanas de congelamiento (SD-03, 3.2.2).
- **Se agregó:** El ambiente de Recuperación ante Desastres reside en CLD-02 y se crea con la misma definición de infraestructura, de modo que es igual al de producción y no se va desviando con el tiempo, salvo la alta disponibilidad de PostgreSQL, que en Brasil opera en una sola zona (4.3.2.2).
- **Se agregó:** Desarrollo y QA parten con un nodo por grupo y se apagan fuera de horario, y Preproducción con tres nodos por grupo.
- **Motivo:** Sesión A (08-11): ambientes (S-05), agentes de entrega (S-28), sin marcha blanca
- **Base:** Ver bitácora

### CAM-104 · línea 866 · 4.2.6 Alta disponibilidad, respaldos, conexiones y puntos de falla · Modificado

- **Se quitó:** La Figura 4.17 identifica los puntos de falla de los accesos y el camino alterno de cada uno.
- **Se agregó:** La Figura 4.17 identifica los puntos de falla de los sitios y de la nube, y el camino alterno de cada uno.
- **Motivo:** Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/correspondencia-figuras.json

### CAM-105 · línea 869 · 4.2.6 Alta disponibilidad, respaldos, conexiones y puntos de falla · Modificado

- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/8766211b5707.png}
- **Se agregó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/diag-04-17_puntos-falla.png}
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa

### CAM-106 · línea 872 · 4.2.6 Alta disponibilidad, respaldos, conexiones y puntos de falla · Modificado

- **Se quitó:** Figura 4.17: Puntos de falla de los accesos y contingencias.
- **Se agregó:** Figura 4.17: Puntos de falla de los sitios y de la nube, con su contingencia.
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json

### CAM-107 · línea 874 · 4.2.6 Alta disponibilidad, respaldos, conexiones y puntos de falla · Modificado

- **Se quitó:** La Figura 4.18 identifica los puntos de falla de la nube.
- **Se agregó:** El tiempo de conmutación entre accesos tiene como objetivo 30 segundos, que es un supuesto del proponente, y se mide en el corte provocado de cada acceso (RT-03.17).
- **Motivo:** Texto ajustado a las figuras físicas nuevas (09-11); P-04 (opción 1): objetivo de conmutación de 30 s; además, renumeración de tablas o figuras
- **Base:** diagramas-laminas/correspondencia-figuras.json; S-38; RT-03.17

### CAM-108 · línea 876 · 4.2.6 Alta disponibilidad, respaldos, conexiones y puntos de falla · Eliminado

- **Se quitó:** \begin{center}
- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/35dda40b1bff.png}
- **Se quitó:** \end{center}
- **Motivo:** Sesión A (08-11): 24 horas en centros (Art. 16.4), puntos únicos, conmutación, HSM, copia del Data Lake
- **Base:** Ver bitácora

### CAM-109 · línea 877 · 4.2.6 Alta disponibilidad, respaldos, conexiones y puntos de falla · Modificado

- **Se quitó:** Figura 4.18: Puntos de falla de la nube y conmutación a Brazil South.
- **Se quitó:** Fuente: elaboración propia a partir de RT-03, RT-07 y SD-03.
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11); además, renumeración de tablas o figuras
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json

### CAM-110 · línea 881 · 4.2.6 Alta disponibilidad, respaldos, conexiones y puntos de falla · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.18 → 4.20)
- **Base:** Comunicado 10

### CAM-111 · línea 890 · 4.2.6 Alta disponibilidad, respaldos, conexiones y puntos de falla · Modificado

- **Se quitó:** 6 & Conexión de DC-01 & Dos accesos de operador con un túnel por frente en cada uno. & Conmutación de ruta entre accesos.
- **Se agregó:** 6 & Conexión de DC-01 & Dos accesos de operador con un túnel por negocio en cada uno. & Conmutación de ruta entre accesos.
- **Motivo:** Sesión A (08-11): 24 horas en centros (Art. 16.4), puntos únicos, conmutación, HSM, copia del Data Lake
- **Base:** Ver bitácora

### CAM-112 · línea 896 · 4.2.6 Alta disponibilidad, respaldos, conexiones y puntos de falla · Agregado

- **Se agregó:** 12 & Front Door y entrada pública & El punto privado de tránsito por East US mantiene la entrada hacia Chile Central si falla el de Brazil South. & Prueba de salud con el origen secundario.
- **Se agregó:** \\
- **Se agregó:** 13 & Identidad de Entra ID & Cuentas de emergencia por frente, con custodia dual. & Ensayo de las cuentas de emergencia.
- **Se agregó:** \\
- **Motivo:** P-14 (opción 1) y hilo lógico: origen de Brasil deshabilitado
- **Base:** S-45; RT-07.05

### CAM-113 · línea 900 · 4.2.6 Alta disponibilidad, respaldos, conexiones y puntos de falla · Modificado

- **Se quitó:** Los puntos 1 a 4 son de la tienda, el 5 y el 6 de los enlaces de los centros y de casa matriz, el 7, el 8 y el 11 de la nube, y el 9 y el 10 de plataformas conservadas, que son el ERP/DTE y el WMS, los sistemas de gestión y de almacén que se mantienen.
- **Se quitó:** La continuidad de tienda se dimensiona en 24 horas, conforme al mínimo de RT-03.10, que prevalece sobre las 8 horas que menciona el Caso, y el ensayo mide además el escenario de ocho horas con conciliación en 30 minutos.
- **Se quitó:** El centro de distribución principal debe operar al menos cuatro horas sin enlace según la misma exigencia, para lo cual cuenta con un enlace redundante de dos proveedores, el router 4G/5G y su par local de captura, y la ubicación real de su WMS se comprueba en el inventario (Tabla 4.15).
- **Se agregó:** Los puntos 1 a 4 son de la tienda, el 5 y el 6 de los enlaces de los centros y de casa matriz, el 7, el 8, el 11, el 12 y el 13 de la nube y de los servicios globales, y el 9 y el 10 de plataformas conservadas, que son el ERP/DTE y el WMS, los sistemas de gestión y de almacén que se mantienen.
- **Se agregó:** La continuidad de tienda se dimensiona en 24 horas, conforme al mínimo de RT-03.10, que prevalece sobre las 8 horas que menciona el Caso, y el ensayo mide la conciliación en 30 minutos al restablecerse el enlace tras ese corte de 24 horas.
- **Se agregó:** Los centros de distribución operan al menos 24 horas sin enlace (artículo 16.4 de las Bases Administrativas y RT-03.10), para lo cual cada uno cuenta con su par local de captura y su router 4G/5G, y el centro principal además con un enlace redundante de dos proveedores.
- **Se agregó:** El ensayo mide también un escenario particular de 4 horas, y la ubicación real del WMS del centro principal se comprueba en el inventario (Tabla 4.17).
- **Motivo:** P-16 (opción 1): 24 horas con conciliación en 30 minutos; además, renumeración de tablas o figuras
- **Base:** RT-03.10; RT-03.13

### CAM-114 · línea 902 · 4.2.6 Alta disponibilidad, respaldos, conexiones y puntos de falla · Modificado

- **Se agregó:** Se llama punto único de falla al elemento cuya caída detiene una función sin que otro lo reemplace de inmediato.
- **Se agregó:** Subsisten ocho, y cada uno se acepta por su contingencia.
- **Se agregó:** Entre paréntesis va su número en la Tabla 4.20.
- **Se agregó:** El conjunto de accesos de una tienda (puntos 1 a 4) se cubre con el diario local durante al menos 24 horas.
- **Se agregó:** El enlace único de CD-02 (punto 5) se cubre con su router 4G/5G y 24 horas de operación local.
- **Se agregó:** La conexión de DC-01 (punto 6) no detiene las funciones nuevas, porque DC-01 no guarda sus datos.
- **Se agregó:** La zona de Chile Central (punto 7) la cubren las otras dos y se declara por prudencia, y la región completa (punto 8) la cubre Brazil South.
- **Se agregó:** El ERP/DTE (punto 9) y el WMS (punto 10) conservados son del Cliente y no se reemplazan, y el ERP/DTE emite en modalidad fiscal de contingencia.
- **Se agregó:** El Service Bus de cada negocio (punto 11) se recupera republicando desde los registros durables.
- **Se agregó:** Aparte de esos ocho, cuatro servicios globales dependen de su propio proveedor, que son Front Door, Entra ID, el DNS y la entrega de software (puntos 12 y 13), y en ellos las cuentas de emergencia por frente cubren el bloqueo de administradores, mientras que la caída del propio servicio no la resuelve la conmutación a Brasil y su contingencia se define uno por uno en el diseño detallado.
- **Motivo:** P-03 (opción 2) y revisor de hilo lógico: ocho puntos únicos con criterio y número; además, renumeración de tablas o figuras
- **Base:** RT-02.11; T-12

### CAM-115 · línea 908 · 4.2.6 Alta disponibilidad, respaldos, conexiones y puntos de falla · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.19 → 4.21)
- **Base:** Comunicado 10

### CAM-116 · línea 913 · 4.2.6 Alta disponibilidad, respaldos, conexiones y puntos de falla · Modificado

- **Se quitó:** Service Bus & Redundancia entre zonas donde la región la ofrece, que se comprueba en la suscripción. & Habilitación del namespace del negocio en Brasil y republicación desde los registros durables recuperados, con deduplicación en los consumidores (4.3.2).
- **Se agregó:** Service Bus & Redundancia entre las tres zonas de Chile Central. & Habilitación del namespace del negocio en Brasil y republicación desde los registros durables recuperados, con deduplicación en los consumidores (4.3.2).
- **Motivo:** P-17 (opción 1): Service Bus zonal confirmado por el usuario
- **Base:** RT-07.01

### CAM-117 · línea 918 · 4.2.6 Alta disponibilidad, respaldos, conexiones y puntos de falla · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.19 → 4.21)
- **Base:** Comunicado 10

### CAM-118 · línea 920 · 4.2.6 Alta disponibilidad, respaldos, conexiones y puntos de falla · Modificado

- **Se quitó:** Esta se hace de forma explícita, copiando el almacenamiento entre las cuentas de ambas regiones y manteniendo una segunda bóveda de respaldo en Brazil South.
- **Se quitó:** Para la filial emisora y X-01 se contempla un Managed HSM, condicionado al censo de claves y a que la región admita el producto.
- **Se agregó:** Esta se hace de forma explícita, copiando el almacenamiento entre las cuentas de ambas regiones, con Data Factory o AzCopy programados para los Data Lake y replicación de objetos para las cuentas Blob sin espacio jerárquico, y manteniendo una segunda bóveda de respaldo en Brazil South.
- **Se agregó:** Para la filial emisora y X-01 se contempla un Managed HSM, condicionado al censo de claves y a que su capacidad se confirme en ambas regiones.
- **Motivo:** Sesión A (08-11): 24 horas en centros (Art. 16.4), puntos únicos, conmutación, HSM, copia del Data Lake
- **Base:** Ver bitácora

### CAM-119 · línea 922 · 4.2.6 Alta disponibilidad, respaldos, conexiones y puntos de falla · Modificado

- **Se quitó:** Las Bases exigen una disponibilidad mensual de 99,9 % medida de extremo a extremo para los servicios críticos (RT-10.01), que equivale a unos 43 minutos de indisponibilidad al mes.
- **Se agregó:** Las Bases exigen una disponibilidad mensual de 99,9 % medida de extremo a extremo para los servicios críticos (RT-10.01), que equivale a unos 43 minutos de indisponibilidad al mes, un 0,1 % de un mes de 30 días.
- **Motivo:** Parte 7 (opción 1): origen de los 43 minutos
- **Base:** RT-10.01

### CAM-120 · línea 926 · 4.2.7 Mapeo de componentes a su arquitectura lógica y física · Modificado

- **Se agregó:** Los códigos R, F y X de la primera columna son los de 3.3.2 y 4.1.5, de modo que cada fila se traza con el esquema de solución y con la arquitectura lógica.
- **Motivo:** Sesión A (08-11): mapeo con 3.3.2 y 4.1.5, filas nuevas y plataformas conservadas; además, renumeración de tablas o figuras
- **Base:** Ver bitácora

### CAM-121 · línea 930 · 4.2.7 Mapeo de componentes a su arquitectura lógica y física · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.20 → 4.22)
- **Base:** Comunicado 10

### CAM-122 · línea 938 · 4.2.7 Mapeo de componentes a su arquitectura lógica y física · Modificado

- **Se quitó:** Máquinas auxiliares y sondas & 4.1 & Máquinas virtuales de cada frente, subred de aplicación. & 12 auxiliares (4 gateways de Power BI, 4 SHIR y 4 conectores de acceso privado) y 2 sondas. & Pares en dominios de falla distintos y sondas fuera del clúster que vigilan.
- **Se agregó:** Máquinas auxiliares y sondas & 4.1 & Máquinas virtuales de cada frente, subred de aplicación. & 12 auxiliares de Retail y de la filial emisora, sin ninguna en X-01 (4 gateways de Power BI, 4 SHIR y 4 conectores de acceso privado), y 2 sondas. & Pares en dominios de falla distintos y sondas fuera del clúster que vigilan.
- **Motivo:** Sesión A (08-11): mapeo con 3.3.2 y 4.1.5, filas nuevas y plataformas conservadas
- **Base:** Ver bitácora

### CAM-123 · línea 941 · 4.2.7 Mapeo de componentes a su arquitectura lógica y física · Modificado

- **Se quitó:** Memoria rápida de oferta y disponibilidad & RT-09.02 & Azure Managed Redis, solo en Retail. & Reserva inicial de 16 GiB. & Reconstruible desde la base de oferta.
- **Se quitó:** Almacenamiento y analítica & RT-05.05, RT-07.11 & Data Lake Storage Gen2, Blob de evidencia y archivo inmutable por frente. & Lago de 3 TiB en Retail y 2 TiB en la filial emisora, evidencia de 5 TiB y archivo de 25 y 12 TiB. & Redundancia de zona y copia explícita a Brazil South.
- **Se quitó:** Entrada pública y privada & RT-11.07, RT-11.11, RT-11.12 & Front Door, Application Gateway y API Management Premium. & Un Front Door, un Application Gateway primario y una instancia multirregión de API Management por negocio. & Gateway regional y Application Gateway propios en Brazil South, con origen de menor prioridad.
- **Se quitó:** Red y control del tráfico & RT-03.04, RT-03.17, RT-03.21 & Hub y ramas de cada frente, VPN Gateway, Azure Firewall Premium, Bastion y DNS Private Resolver. & Nueve redes virtuales y tres firewalls, y un VPN Gateway para Retail y otro para la filial emisora. & La VPN por frente es la conexión de DC-01.
- **Se agregó:** Memoria rápida de oferta y disponibilidad & RT-09.02 & Azure Managed Redis, solo en Retail. & Nivel Balanced B20 de 24 GB, para una reserva de diseño de 16 GiB. & Reconstruible desde la base de oferta.
- **Se agregó:** Almacenamiento y analítica & RT-05.05, RT-07.11 & Data Lake Storage Gen2, Blob de evidencia y archivo inmutable por frente, Data Factory y Power BI sobre capacidad en Chile Central. & Lago de 3 TiB en Retail y 2 TiB en la filial emisora, evidencia de 5 TiB y archivo de 25 y 12 TiB. & Redundancia de zona y copia explícita a Brazil South.
- **Se agregó:** Entrada pública y privada & RT-11.07, RT-11.11, RT-11.12 & Front Door, Application Gateway, API Management Premium, DNS público y API Center en East US. & Un Front Door, un Application Gateway primario y una instancia multirregión de API Management por negocio. & Gateway regional y Application Gateway propios en Brazil South, con origen de recuperación de menor prioridad.
- **Se agregó:** Red y control del tráfico & RT-03.04, RT-03.17, RT-03.21 & Hub y ramas de cada frente, VPN Gateway, Azure Firewall Premium, Bastion, DNS Private Resolver y DDoS Protection. & Nueve redes virtuales y tres firewalls, y un VPN Gateway para Retail y otro para la filial emisora. & La VPN por frente es la conexión de DC-01.
- **Motivo:** C-003: Redis B20 verificado
- **Base:** S-26

### CAM-124 · línea 949 · 4.2.7 Mapeo de componentes a su arquitectura lógica y física · Modificado

- **Se quitó:** Innovación de búsqueda multimodal & SD-13 & Servicio de Oferta de Retail y PostgreSQL con vectores (pg-r-vector). & Un servidor de los 6 de Retail. & La de Oferta y la de PostgreSQL.
- **Se agregó:** Innovación de búsqueda multimodal & SD-13 & Servicio de Oferta de Retail y PostgreSQL con vectores. & Un servidor de los 6 de Retail. & La de Oferta y la de PostgreSQL.
- **Motivo:** Cierre parte 2: se quitan nombres internos de recursos
- **Base:** Glosario 08, regla 1

### CAM-125 · línea 951 · 4.2.7 Mapeo de componentes a su arquitectura lógica y física · Modificado

- **Se quitó:** Innovación de lockers & SD-13 & Controlador local en la tienda y servicio de Pedidos. & Según el padrón de cada sitio. & Pedidos en tres zonas, con contrato autenticado y sin acceso directo a la base.
- **Se agregó:** Innovación de lockers & SD-13 & Controlador local en la tienda y servicio de Pedidos. & Según el padrón de cada sitio, que se fija en el levantamiento de la Etapa 2. & Pedidos en tres zonas, con contrato autenticado y sin acceso directo a la base.
- **Motivo:** Sesión A (08-11): mapeo con 3.3.2 y 4.1.5, filas nuevas y plataformas conservadas
- **Base:** Ver bitácora

### CAM-126 · línea 954 · 4.2.7 Mapeo de componentes a su arquitectura lógica y física · Modificado

- **Se quitó:** Centros de distribución y DC-01 & RT-03.10 & Par local de captura en cada centro y dos pares de integración en DC-01. & Un par por centro y un par por negocio en DC-01. & Cada par se respalda a sí mismo, sin duplicar el WMS conservado.
- **Se agregó:** Centros de distribución y DC-01 & RT-03.10 & Par local de captura en cada centro y dos pares de integración en DC-01. & Un par por centro y un par por negocio en DC-01, el de la filial transitorio. & Cada par se respalda a sí mismo, y en CD-01 no duplica el WMS conservado.
- **Se agregó:** Plataformas conservadas, contrapartes y elementos por definir & RT-02.01, Caso cap. 5 & ERP/DTE en DC-01 y WMS en CD-01 por supuesto, y el resto externo. & Sin cantidad propia, con la vista logística en el adaptador de Retail y el WMS conservado en CD-01, las capacidades comunes en el grupo de negocio de cada frente y el control regulatorio (F:C-04) como candidato sin despliegue aprobado. & La de cada plataforma, con adaptadores que reintentan y guardan en cola.
- **Se agregó:** \\
- **Motivo:** Parte 6 (opción 1): nodo de la vista logística y capacidades comunes
- **Base:** S-29; Comunicado 10

### CAM-127 · línea 960 · 4.2.7 Mapeo de componentes a su arquitectura lógica y física · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.20 → 4.22)
- **Base:** Comunicado 10

### CAM-128 · línea 964 · 4.2.8 Dimensionamiento y plan de capacidad · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.21 → 4.23)
- **Base:** Comunicado 10

### CAM-129 · línea 968 · 4.2.8 Dimensionamiento y plan de capacidad · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.21 → 4.23)
- **Base:** Comunicado 10

### CAM-130 · línea 981 · 4.2.8 Dimensionamiento y plan de capacidad · Modificado

- **Se quitó:** Resincronización de tienda tras 24 horas sin enlace & 523,4 MB, que exigen 2,3 Mbps para cerrarla en 30 minutos. & 312,8 MB de ventas y 210,6 MB de bajada, ambos con margen 1,5; plazo de RT-03.13.
- **Se agregó:** Resincronización de tienda tras 24 horas sin enlace & 523,4 MB, que exigen 2,3 Mbps para cerrarla en 30 minutos, plazo que el proponente aplica a 24 horas y no a las 8 del Caso. & 312,8 MB de ventas y 210,6 MB de bajada, ambos con margen 1,5, y el plazo que el Caso fija para la sincronización tras la reconexión.
- **Motivo:** Sesión A (08-11): latencias, cálculo de nodos, pico de Service Bus, retención de registros
- **Base:** Ver bitácora

### CAM-131 · línea 986 · 4.2.8 Dimensionamiento y plan de capacidad · Modificado

- **Se quitó:** En la red, lo que dimensiona el enlace de una tienda no es la venta, que ocupa 0,02 Mbps, sino la bajada de precios y la resincronización después de un corte.
- **Se agregó:** En la red, lo que dimensiona el enlace de una tienda no es la venta, que ocupa 0,02 Mbps, sino la bajada de precios, y la resincronización después de un corte exige menos capacidad que esa bajada.
- **Motivo:** Sesión A (08-11): latencias, cálculo de nodos, pico de Service Bus, retención de registros; además, renumeración de tablas o figuras
- **Base:** Ver bitácora

### CAM-132 · línea 989 · 4.2.8 Dimensionamiento y plan de capacidad · Agregado

- **Se agregó:** Los tiempos de respuesta objetivo, de ida y vuelta, son 10 ms entre la caja y los servidores de la tienda, 5 ms entre los dos servidores de un par, 100 ms entre una tienda y Chile Central por un acceso fijo, 200 ms por el respaldo móvil y 150 ms entre Front Door y su origen.
- **Se agregó:** Entre Chile Central y Brazil South no hay objetivo, y se estiman entre 40 y 55 ms por cálculo.
- **Se agregó:** Salvo esa estimación, son criterios de ingeniería que la prueba de la tienda tipo y la de Preproducción confirman.
- **Se agregó:** Los nodos de cada grupo se calculan como el mayor entre tres y el entero superior de las solicitudes de CPU divididas por la capacidad de un nodo, con un uso objetivo del 70 % y los dos tercios de capacidad que quedan al perder una zona.
- **Se agregó:** Service Bus se dimensiona con el pico de la carga masiva de precios, que es de 6.667 entregas por segundo y llega a 7.802 si coincide con la sincronización de existencia, un solape que es una hipótesis y se mide.
- **Se agregó:** El número de unidades de mensajería se fija con la prueba de carga.
- **Se agregó:** Los registros de seguridad se conservan 12 meses en línea y 24 en archivo.
- **Se agregó:** Las métricas y trazas se conservan 30 días y los registros técnicos 90, con un volumen de partida de 50 GB por día por frente, que se mide en la Etapa 1.
- **Motivo:** Sesión A (08-11): latencias, cálculo de nodos, pico de Service Bus, retención de registros
- **Base:** Ver bitácora

### CAM-133 · línea 1008 · 4.3 Data center · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.23 → 4.24)
- **Base:** Comunicado 10

### CAM-134 · línea 1012 · 4.3 Data center · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.23 → 4.24)
- **Base:** Comunicado 10

### CAM-135 · línea 1022 · 4.3 Data center · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.23 → 4.24)
- **Base:** Comunicado 10

### CAM-136 · línea 1026 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** La región se describe en cuatro figuras, una por parte, y en cada una los tres frentes aparecen separados.
- **Se agregó:** En la región conviven tres frentes, que son espacios propios con sus datos, identidades, redes y claves.
- **Se agregó:** Son Retail, la filial emisora y el Servicio de control de cruces (X-01), que autoriza la única conexión permitida entre los dos negocios.
- **Se agregó:** La Figura 4.12 resume los sitios y las dos regiones, y la región se describe en tres figuras, una por parte, donde los tres frentes aparecen separados.
- **Se agregó:** Los nodos de cada grupo se reparten entre las tres zonas, y cada servidor de PostgreSQL ubica su primario y su espera en zonas distintas, de modo que la pérdida de una zona deja operativos al menos dos tercios de la capacidad.
- **Motivo:** Texto ajustado a las figuras físicas nuevas (09-11); además, renumeración de tablas o figuras
- **Base:** diagramas-laminas/correspondencia-figuras.json

### CAM-137 · línea 1029 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/1688f39f837c.png}
- **Se agregó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/diag-04-18_computo-chile-central.png}
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa

### CAM-138 · línea 1032 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** Figura 4.21: Clústeres de Azure Kubernetes Service de Chile Central por frente.
- **Se agregó:** Figura 4.18: Clústeres de AKS y máquinas de apoyo de Chile Central por frente.
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json

### CAM-139 · línea 1034 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** Cada frente tiene su propio clúster de Azure Kubernetes Service.
- **Se quitó:** En X-01, el servicio y su observabilidad comparten los seis nodos representados, con reservas y volúmenes separados; la figura agrupa estas cargas y no representa cada proceso auxiliar.
- **Se quitó:** El plano de control de cada clúster lo administra Microsoft y no suma a esa cuenta.
- **Se quitó:** Retail agrega un grupo elástico de entre cero y tres nodos para el conteo predictivo, que no está en la ruta de la venta.
- **Se agregó:** Cada frente tiene su propio clúster de Azure Kubernetes Service (AKS), que es la plataforma en que corren los servicios y que reparte su carga entre máquinas virtuales llamadas nodos.
- **Se agregó:** En X-01, el servicio y su observabilidad comparten sus seis nodos, con reservas y volúmenes separados; la figura agrupa estas cargas y no representa cada proceso auxiliar.
- **Se agregó:** El plano de control, que es la parte que administra cada clúster, lo opera Microsoft y no suma a esa cuenta.
- **Se agregó:** Retail agrega un grupo elástico de entre cero y tres nodos, que se enciende solo cuando hay trabajos de conteo predictivo y no está en la ruta de la venta.
- **Motivo:** Ciclo 4.3.1 (06-11): C-053, C-021, C-068, C-070 y ajustes tras los agentes; además, renumeración de tablas o figuras
- **Base:** Ver bitácora

### CAM-140 · línea 1037 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/6e5ec0282f43.png}
- **Se agregó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/diag-04-19_datos-chile-central.png}
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa

### CAM-141 · línea 1040 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** Figura 4.22: Bases PostgreSQL de Chile Central por frente.
- **Se agregó:** Figura 4.19: Bases PostgreSQL, mensajería, almacenamiento y respaldo de Chile Central por frente.
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json

### CAM-142 · línea 1042 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** La Figura 4.23 muestra la mensajería y el almacenamiento.
- **Se agregó:** La misma figura muestra la mensajería, el almacenamiento y las bóvedas de respaldo.
- **Se agregó:** Cada negocio tiene su propio Service Bus y sus propias cuentas de almacenamiento, sin un puente entre buses, y la memoria rápida de Azure Managed Redis atiende solo a Retail.
- **Se agregó:** La filial emisora guarda su evidencia vigente en un almacenamiento propio y ambos negocios tienen archivo inmutable por clase de dato.
- **Se agregó:** X-01 no tiene Service Bus, Data Lake ni cuentas Blob de negocio en esta figura.
- **Se agregó:** Su bitácora reside en PostgreSQL y los volúmenes de su observabilidad pertenecen a las cargas de su clúster.
- **Se agregó:** La Figura 4.20 cierra la región con la identidad, la seguridad, la observabilidad y la entrega.
- **Motivo:** Texto ajustado a las figuras físicas nuevas (09-11); Cierre parte 2: «Data Lake» en lugar de «lago de datos»
- **Base:** diagramas-laminas/correspondencia-figuras.json; Glosario 08

### CAM-143 · línea 1048 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/0dde5557a631.png}
- **Se agregó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/diag-04-20_seguridad-operacion.png}
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa

### CAM-144 · línea 1051 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** Figura 4.23: Mensajería y almacenamiento de Chile Central por frente.
- **Se agregó:** Figura 4.20: Identidad, seguridad, observabilidad y entrega de Chile Central por frente.
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json

### CAM-145 · línea 1053 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** Cada negocio tiene su propio Service Bus y sus propias cuentas de almacenamiento, sin un puente entre buses, y la memoria rápida de Azure Managed Redis atiende solo a Retail.
- **Se quitó:** La filial emisora guarda su evidencia vigente en un almacenamiento propio y ambos negocios tienen archivo inmutable por clase de dato.
- **Se quitó:** X-01 no tiene Service Bus, lago de datos ni cuentas Blob de negocio en esta figura.
- **Se quitó:** Su bitácora reside en PostgreSQL y los volúmenes de su observabilidad pertenecen a las cargas de su clúster.
- **Se quitó:** La Figura 4.24 cierra la región con las máquinas auxiliares y la seguridad.
- **Se agregó:** Retail y la filial emisora tienen cada una seis máquinas auxiliares fuera de los clústeres, que son dos de gateway de Power BI, dos de extracción de datos y dos de acceso privado, y cada una tiene además una sonda independiente que vigila el clúster desde fuera.
- **Se agregó:** Los 40 nodos, las 12 máquinas auxiliares y las 2 sondas suman 54 máquinas virtuales en Chile, sin contar el grupo elástico de Retail.
- **Se agregó:** La pila de observabilidad de X-01 corre dentro de su clúster y no agrega máquinas auxiliares a la Figura 4.18.
- **Se agregó:** Cada frente tiene su propia caja fuerte de claves y su propio espacio de registro.
- **Se agregó:** La detección de amenazas, Sentinel, opera en Brazil South porque Microsoft no la ofrece en Chile Central, y la subsección 4.3.2.1 declara qué datos recibe y bajo qué aprobación del Cliente.
- **Se agregó:** Para la filial emisora y X-01 se contempla un Managed HSM, que es un equipo dedicado a custodiar las claves de mayor valor, condicionado a que el censo de claves lo justifique y a que su capacidad se confirme en Chile Central y en Brazil South al crear el recurso.
- **Se agregó:** Estas cantidades son reservas iniciales de diseño, calculadas con supuestos de consumo y con la pérdida de una zona, y se ajustan con la prueba de carga de Preproducción antes de contratar la capacidad.
- **Se agregó:** La región no tiene región emparejada, que es la región gemela con la que Azure copia los datos por defecto (Microsoft, 2026l), por lo que la protección ante la falla de la región depende de la réplica que la solución configura hacia CLD-02, que es Azure Brazil South.
- **Se agregó:** La disponibilidad de cada recurso en la región se comprueba en la suscripción del proyecto antes de la construcción.
- **Se agregó:** Los sitios propios del Cliente completan el despliegue híbrido que exige el artículo 16 de las Bases Administrativas.
- **Se agregó:** DC-01 permanece en convivencia con la nube por la red privada de cada frente.
- **Se agregó:** Es un recinto propio de 140 m\textsuperscript{2} habilitado en 2011, que cumple solo parcialmente los estándares de las Bases Transversales, y la brecha consta en un informe interno de 2024 que el Cliente entregará al adjudicatario (Multitiendas Ancoa S.A., 2026, Caso 09, cap. 6, p. 14).
- **Se agregó:** El Cliente aporta el espacio y ejecuta la obra civil de separación, que el proponente especifica y coordina (RT-06.06).
- **Se agregó:** Only Simple Solutions habilita el recinto técnico, que es la sala de equipos dentro de él, con su conectividad, su seguridad y sus canalizaciones (RT-06.33), y provee, configura y certifica sus equipos (SD-03, subsección 3.2.3).
- **Se agregó:** La frontera con el Cliente está en el rack, porque el proponente provee las canalizaciones hasta él y el Cliente ejecuta el cableado.
- **Se agregó:** La Figura 4.21 muestra el recinto.
- **Motivo:** Texto ajustado a las figuras físicas nuevas (09-11); P-09 (opción 1): frontera canalizaciones y cableado
- **Base:** diagramas-laminas/correspondencia-figuras.json; S-41; RT-06.33

### CAM-146 · línea 1062 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/69716b9c4e43.png}
- **Se agregó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/diag-04-21_dc01-casa-matriz.png}
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa

### CAM-147 · línea 1065 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** Figura 4.24: Máquinas auxiliares, seguridad y observabilidad de Chile Central por frente.
- **Se quitó:** Fuente: elaboración propia a partir de RT-03 y SD-03.
- **Se agregó:** Figura 4.21: DC-01, casa matriz, con Retail y la filial emisora separados.
- **Se agregó:** Fuente: elaboración propia a partir del Caso 09, RT-06 y SD-03.
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json

### CAM-148 · línea 1067 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** Retail y la filial emisora tienen cada una seis máquinas auxiliares fuera de los clústeres, que son dos de gateway de Power BI, dos de extracción de datos y dos de acceso privado, más una sonda independiente.
- **Se quitó:** Con ellas y las dos sondas, los 40 nodos suman 54 máquinas virtuales en Chile.
- **Se quitó:** La pila de observabilidad de X-01 corre dentro de su clúster y no agrega máquinas auxiliares a la Figura 4.24.
- **Se quitó:** Cada frente tiene su propia caja fuerte de claves y su propio espacio de registro, y su detección de amenazas, Sentinel, opera en Brazil South porque Microsoft no la ofrece en Chile Central, y para la filial emisora y X-01 se contempla un Managed HSM, condicionado a que su región lo admita y a que el censo de claves lo justifique.
- **Se agregó:** El recinto reserva cuatro racks de 42U, uno para los servidores de Retail, otro para los de la filial emisora, otro para las comunicaciones y otro para el respaldo local.
- **Se agregó:** De las 168U hay 80 presupuestadas y 88 libres, y una parte de las 80 es reserva para los sistemas conservados cuyo inventario se desconoce.
- **Se agregó:** Las plataformas actuales se agrupan en una zona Retail y una zona de la filial emisora, cada una con su propia red local, su propio par de switches y su propio firewall con SD-WAN, y los dos negocios comparten solo dos accesos de operadores distintos, que contrata el Cliente y llegan segregados, por rutas físicas separadas y con ingreso al edificio por puntos distintos (RT-06.32 y RT-03.17).
- **Se agregó:** La separación entre ambas zonas se verifica con las pruebas de denegación de accesos cruzados entre frentes que describe 4.1.16.
- **Motivo:** Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/correspondencia-figuras.json

### CAM-149 · línea 1069 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** Estas cantidades son reservas iniciales de diseño, calculadas con supuestos de consumo y con la pérdida de una zona, y se ajustan con la prueba de carga de Preproducción antes de comprar.
- **Se quitó:** La región no tiene región emparejada, que es la región gemela con la que Azure copia los datos por defecto (Microsoft, 2026l), por lo que la protección ante la falla de la región depende de la réplica que la solución configura hacia CLD-02.
- **Se quitó:** La disponibilidad de cada recurso en la región se comprueba en la suscripción del proyecto antes de la construcción.
- **Se agregó:** Dos pares de servidores de integración, uno por negocio, extraen los datos de los sistemas conservados hacia Azure, y el respaldo local mantiene repositorios, identidades y claves separados por negocio.
- **Se agregó:** La solución nueva no instala allí máquinas virtuales de negocio ni bases financieras, porque las Bases no identifican un conjunto de datos financieros nuevos cuya custodia local sea obligatoria.
- **Se agregó:** Si una fuente posterior exigiera esa custodia local, se aloja en la zona de la filial emisora y se dimensiona entonces.
- **Se agregó:** El par de la filial emisora es transitorio y se retira al cerrar la extracción del crédito de 2011, y el de Retail se omite si el proveedor ofrece una interfaz que lo reemplace.
- **Se agregó:** La plataforma de crédito de 2011 permanece en convivencia durante su migración.
- **Se agregó:** El recuadro separado de la Figura 4.21 indica que su ubicación está por acreditar, sin asignarla a DC-01.
- **Motivo:** Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/correspondencia-figuras.json

### CAM-150 · línea 1071 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** DC-01 permanece en convivencia con la nube por la red privada de cada frente.
- **Se quitó:** Es un recinto propio de 140 m\textsuperscript{2} habilitado en 2011, que cumple solo parcialmente los estándares de las Bases Transversales, y la brecha consta en un informe interno de 2024 que el Cliente entregará al adjudicatario (Multitiendas Ancoa S.A., 2026, Caso 09, cap. 6, p. 14).
- **Se quitó:** El Cliente aporta el espacio y ejecuta la obra civil de separación, que el proponente especifica y coordina (RT-06.06).
- **Se quitó:** Only Simple Solutions habilita el recinto técnico, que es la sala de equipos dentro de él, con su conectividad, su seguridad y sus canalizaciones (RT-06.33), y especifica, configura y certifica sus equipos (SP-04 de SD-03).
- **Se quitó:** La Figura 4.25 muestra el recinto.
- **Se agregó:** Only Simple Solutions habilita el recinto técnico, y el Cliente ejecuta las obras civiles y eléctricas que este requiere.
- **Se agregó:** La energía tiene una fuente ininterrumpida de al menos 30 minutos a plena carga, doble alimentación A y B, y generación autónoma de al menos 24 horas continuas con combustible y contrato de reabastecimiento (RT-06.07 y RT-06.08).
- **Se agregó:** La climatización es de precisión con un equipo de reserva (N+1) (RT-06.13).
- **Se agregó:** La seguridad física incluye detección temprana de incendio por aspiración de aire y extinción automática por agente limpio, que apaga el fuego sin dañar los equipos (RT-06.16 y RT-06.17), control de acceso biométrico basado en reconocimiento facial, con identificación por huellas (AFIS) como respaldo (RT-06.20), y videovigilancia con 30 días de imágenes en línea, cuyas grabaciones anteriores se respaldan en un medio secundario recuperable (RT-06.24).
- **Se agregó:** El espacio de operación queda separado de la sala de equipos (RT-06.30).
- **Se agregó:** Al recinto técnico se aplica la tipología de sala técnica principal, que exige íntegramente RT-06.01 a RT-06.24, porque aloja sistemas conservados del Cliente, que se suponen allí, y los dos pares de integración, de modo que concentra cómputo y almacenamiento sustantivos.
- **Se agregó:** El recinto técnico es de uso exclusivo de la solución y de los sistemas conservados con los que convive (RT-06.01).
- **Se agregó:** Las Bases exigen una disponibilidad mensual de 99,95 \% para la energía, la climatización y la red del recinto.
- **Se agregó:** La carga eléctrica proyectada, la ocupación de cada rack y la brecha respecto de los estándares se declaran con el inventario de plataformas y el informe de 2024 del Cliente, y entonces se calcula la capacidad del recinto.
- **Se agregó:** DC-02, la sala de respaldo del Cliente en la misma comuna, no tiene superficie informada y su infraestructura se acredita en el mismo levantamiento.
- **Se agregó:** Los dos centros de distribución completan los sitios del Cliente.
- **Se agregó:** CD-01 conserva su WMS, que es el sistema que gestiona el almacén.
- **Se agregó:** CD-02, el centro de Concepción, no tiene WMS y captura sus movimientos desde los terminales del centro en un par local de registro durable.
- **Se agregó:** Esa captura es una decisión de diseño del proponente y no incorpora a Concepción al WMS, cuya extensión el Caso pide evaluar y costear (Multitiendas Ancoa S.A., 2026, Caso 09, cap. 5, p. 13).
- **Se agregó:** Por eso no se supone allí otro WMS instalado.
- **Se agregó:** Cada centro tiene su propia red y su perímetro, un router celular de respaldo y un par local que mantiene la captura sin enlace.
- **Se agregó:** El enlace actual de CD-02 es único (Multitiendas Ancoa S.A., 2026, Caso 09, cap. 6, p. 14), de modo que el router celular es su segundo camino y se propone al Cliente un segundo enlace fijo.
- **Se agregó:** Ambos centros se conectan solo con Retail.
- **Se agregó:** La Figura 4.22 los muestra.
- **Motivo:** Texto ajustado a las figuras físicas nuevas (09-11); P-08 (opción 1): recinto de uso exclusivo
- **Base:** diagramas-laminas/correspondencia-figuras.json; S-40; RT-06.01

### CAM-151 · línea 1080 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/0b9e54f2ffe9.png}
- **Se agregó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/diag-04-22_centros-distribucion.png}
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa

### CAM-152 · línea 1083 · 4.3.1 Especificaciones Data Center Primaria · Modificado

- **Se quitó:** Figura 4.25: DC-01, casa matriz, con Retail y la filial emisora separados.
- **Se quitó:** Fuente: elaboración propia a partir del Caso 09, RT-06 y SD-03.
- **Se quitó:** El recinto reserva cuatro racks de 42U, uno para los servidores de Retail, otro para los de la filial emisora, otro para las comunicaciones y otro para el respaldo local, con una reserva inicial de 80 de 168U.
- **Se quitó:** Las plataformas actuales se agrupan en una zona Retail y una zona de la filial emisora, cada una con su propia red local, su propio par de switches y su propio firewall con SD-WAN, y los dos negocios comparten solo los dos accesos de los operadores, que llegan segregados.
- **Se quitó:** Dos pares de servidores de integración, uno por negocio, extraen los datos de los sistemas conservados hacia Azure, y el respaldo local mantiene repositorios, identidades y claves separados por negocio.
- **Se quitó:** La solución nueva no instala allí máquinas virtuales de negocio ni bases financieras, porque las Bases no identifican un conjunto de datos financieros nuevos cuya custodia local sea obligatoria.
- **Se quitó:** Si una fuente expresa lo exigiera, esa custodia se aloja en la zona de la filial emisora y se dimensiona entonces.
- **Se quitó:** La plataforma de crédito de 2011 permanece en convivencia durante su migración.
- **Se quitó:** El recuadro separado de la Figura 4.25 indica que su ubicación está por acreditar, sin asignarla a DC-01.
- **Se quitó:** El recinto técnico se habilita con una fuente de energía ininterrumpida de al menos 30 minutos a plena carga, doble alimentación A y B, y generación autónoma de al menos 24 horas continuas con combustible y contrato de reabastecimiento (RT-06.07 y RT-06.08).
- **Se quitó:** Lo completan climatización de precisión con un equipo de reserva (N+1) (RT-06.13), detección temprana de incendio por aspiración de aire y extinción automática por agente limpio (RT-06.16 y RT-06.17), control de acceso biométrico (RT-06.20) y videovigilancia con 30 días de imágenes (RT-06.24).
- **Se quitó:** El espacio de operación queda separado de la sala de equipos (RT-06.30).
- **Se quitó:** Se adopta la tipología de sala técnica principal, a la que se aplican íntegramente RT-06.01 a RT-06.24, y las Bases exigen una disponibilidad mensual de 99,95 \% para la energía, la climatización y la red del recinto.
- **Se quitó:** La carga eléctrica proyectada, la ocupación de cada rack y la brecha respecto de los estándares se declaran con el inventario de plataformas y el informe de 2024 del Cliente, y entonces se calcula la capacidad del recinto.
- **Se quitó:** DC-02 no tiene superficie informada y su infraestructura se acredita en el mismo levantamiento.
- **Se quitó:** Los dos centros de distribución completan los sitios del Cliente.
- **Se quitó:** CD-01 conserva su WMS, que es el sistema que gestiona el almacén, y CD-02 captura sus movimientos en un par local de registro durable, sin que se infiera allí otro WMS instalado.
- **Se quitó:** Cada centro tiene su propia red y su perímetro, un router celular de respaldo y un par local que mantiene la captura sin enlace, y el enlace actual de CD-02 es único, por lo que se propone un segundo.
- **Se quitó:** Ambos centros se conectan solo con Retail.
- **Se quitó:** La Figura 4.26 los muestra.
- **Se quitó:** \begin{center}
- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/eb854151a942.png}
- **Se quitó:** \end{center}
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11); además, renumeración de tablas o figuras
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json

### CAM-153 · línea 1087 · 4.3.2 Especificaciones Data Center Secundario · Modificado

- **Se quitó:** La Figura 4.27 muestra lo que se mantiene allí para cada frente, y la Figura 4.28 muestra X-01 y cómo se conmuta.
- **Se agregó:** Las Figuras 4.23 y 4.24 muestran lo que se mantiene allí para cada frente, y la Figura 4.25 muestra cómo se conmuta.
- **Motivo:** Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/correspondencia-figuras.json

### CAM-154 · línea 1090 · 4.3.2 Especificaciones Data Center Secundario · Modificado

- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/56b9be1eff1b.png}
- **Se agregó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/diag-04-23_brazil-red-entrada.png}
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa

### CAM-155 · línea 1093 · 4.3.2 Especificaciones Data Center Secundario · Modificado

- **Se quitó:** Figura 4.27: Brazil South, recuperación pasiva de un frente.
- **Se agregó:** Figura 4.23: Brazil South: red y entrada de recuperación por frente.
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json

### CAM-156 · línea 1095 · 4.3.2 Especificaciones Data Center Secundario · Modificado

- **Se quitó:** La modalidad es activo-pasivo templado (RT-07.01).
- **Se quitó:** La región de recuperación mantiene una copia al día y se activa solo si la principal falla, como una tienda de reemplazo que abre únicamente si la primera cierra, y templado significa que sus servicios ya están encendidos.
- **Se quitó:** Hay 50 máquinas virtuales de espera, que son los 40 nodos de los tres clústeres, 8 máquinas de integración y acceso y 2 sondas, y 4 máquinas de Power BI que se reproducen apagadas y quedan fuera del tiempo crítico de recuperación.
- **Se quitó:** Se prefiere esta modalidad frente a la activo-activo porque el RTO de cuatro horas la permite, porque cada registro tiene una sola autoridad y escribir a la vez en dos regiones exigiría resolver conflictos, y porque duplicar la carga activa añade costo y complejidad sin mejorar el cumplimiento de RT-07.04.
- **Se agregó:** La Figura 4.23 muestra la red y la entrada de cada frente en Brasil, y la Figura 4.24 muestra su cómputo y sus datos en espera.
- **Motivo:** Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/correspondencia-figuras.json

### CAM-157 · línea 1097 · 4.3.2 Especificaciones Data Center Secundario · Modificado

- **Se quitó:** Front Door llega por Private Link a un Application Gateway propio de cada negocio en Brasil, registrado como segundo origen de menor prioridad, y este lo entrega al gateway regional de la instancia multirregión de API Management de ese negocio.
- **Se quitó:** La región del enlace privado administrado de Front Door hacia el origen se confirma en la suscripción antes de la construcción, porque no todas las regiones lo admiten (Microsoft, 2026r).
- **Se agregó:** \begin{center}
- **Se agregó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/diag-04-24_brazil-computo-datos.png}
- **Se agregó:** \end{center}
- **Se agregó:** Figura 4.24: Brazil South: cómputo y datos en espera por frente.
- **Se agregó:** Fuente: elaboración propia a partir de RT-03, RT-07 y SD-03.
- **Se agregó:** La modalidad es activo-pasivo templado (RT-07.01).
- **Se agregó:** La región de recuperación mantiene una copia al día y se activa solo si la principal falla, como una tienda de reemplazo que abre únicamente si la primera cierra, y templado significa que sus servicios ya están encendidos.
- **Se agregó:** Hay 50 máquinas virtuales de espera, que son los 40 nodos de los tres clústeres, 8 máquinas de integración y acceso y 2 sondas, y 4 máquinas de gateway de Power BI, que son los puentes hacia el servicio y se reproducen apagadas y quedan fuera del tiempo crítico de recuperación.
- **Se agregó:** El grupo elástico de Retail para modelos predictivos, de cero a tres nodos, no se enciende en la espera y se activa solo después de estabilizar la operación.
- **Se agregó:** Se prefiere esta modalidad frente a la activo-activo porque el RTO (tiempo máximo detenido) de cuatro horas la permite, porque cada registro tiene una sola autoridad y escribir a la vez en dos regiones exigiría resolver conflictos, y porque duplicar la carga activa añade complejidad operacional sin que el RTO de cuatro horas lo requiera.
- **Se agregó:** Front Door llega por Private Link a un Application Gateway propio de cada negocio en Brasil, registrado como origen de recuperación, deshabilitado hasta la penúltima etapa del procedimiento de conmutación (4.3.2.2), y este lo entrega al gateway regional de la instancia multirregión de API Management de ese negocio.
- **Se agregó:** Los puntos privados de Front Door en Brazil South y en East US, que llevan la entrada pública hacia Chile Central, constan en 4.2.4, y su disponibilidad se comprueba en la suscripción antes de la construcción (Microsoft, 2026r).
- **Se agregó:** Las tiendas, los centros de distribución y DC-01 reconectan por sus túneles al VPN Gateway de cada negocio en Brazil South, que cada sitio tiene configurado como segundo destino.
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11); P-14 (opción 1) y hilo lógico: origen de Brasil deshabilitado; además, renumeración de tablas o figuras
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json; S-45; RT-07.05

### CAM-158 · línea 1109 · 4.3.2 Especificaciones Data Center Secundario · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.24 → 4.25)
- **Base:** Comunicado 10

### CAM-159 · línea 1115 · 4.3.2 Especificaciones Data Center Secundario · Modificado

- **Se quitó:** Blobs, evidencia y archivo & Copia explícita entre cuentas de ambas regiones, sin almacenamiento geo-redundante. & La integridad de los objetos y su restauración con claves.
- **Se agregó:** Blobs, evidencia y archivo & Copia explícita entre cuentas de ambas regiones, sin almacenamiento geo-redundante. & La integridad de los objetos, el retraso de la copia frente al RPO y su restauración con claves.
- **Motivo:** Ciclo 4.3.2 (06-11): C-074 a C-084 y ajustes tras lector, hilo lógico y PMBOK
- **Base:** Ver bitácora

### CAM-160 · línea 1119 · 4.3.2 Especificaciones Data Center Secundario · Agregado

- **Se agregó:** Conexión de los sitios & Reconexión de tiendas, centros de distribución y DC-01 al VPN Gateway de cada negocio en Brazil South, configurado como segundo destino. & Que cada sitio reconecte dentro del RTO y que las ventas locales se concilien.
- **Se agregó:** \\
- **Motivo:** Ciclo 4.3.2 (06-11): C-074 a C-084 y ajustes tras lector, hilo lógico y PMBOK
- **Base:** Ver bitácora

### CAM-161 · línea 1122 · 4.3.2 Especificaciones Data Center Secundario · Modificado

- **Se quitó:** La réplica de PostgreSQL entre regiones es asíncrona y su retraso puede superar los 15 minutos, de modo que el RPO no queda garantizado por el producto y se mide, se alerta (RT-07.03) y se demuestra en el ensayo (Microsoft, 2026p).
- **Se quitó:** La réplica promovida no hereda la alta disponibilidad, y esta se habilita en Brasil como parte del procedimiento.
- **Se agregó:** La réplica de PostgreSQL entre regiones es asíncrona y su retraso puede superar los 15 minutos, de modo que el RPO (pérdida de datos aceptable) no queda garantizado por el producto y se mide, se alerta (RT-07.03) y se demuestra en el ensayo (Microsoft, 2026p).
- **Se agregó:** Si el retraso supera ese límite, se declara la pérdida potencial y se concilia con los diarios de las tiendas y con los registros durables.
- **Se agregó:** La réplica promovida no hereda la alta disponibilidad, y esta se habilita en Brasil como parte del procedimiento, con una activación automatizada.
- **Se agregó:** El respaldo con la política 3-2-1-1-0 y su prueba mensual de restauración se describen en 4.2.6, y la Tabla 4.26 resume la retención y la copia en Brasil de cada dominio de datos.
- **Motivo:** Ciclo 4.3.2 (06-11): C-074 a C-084 y ajustes tras lector, hilo lógico y PMBOK; además, renumeración de tablas o figuras
- **Base:** Ver bitácora

### CAM-162 · línea 1124 · 4.3.2 Especificaciones Data Center Secundario · Modificado

- **Se quitó:** Cada servicio productor conserva los hechos confirmados que debe comunicar y cada consumidor registra los identificadores de aquellos cuyo efecto ya aplicó.
- **Se agregó:** \par\vspace{0pt plus 10\baselineskip}\penalty-300\vspace{0pt plus -10\baselineskip}
- **Se agregó:** Tabla 4.26: Retención y copia en Brazil South por dominio de datos.
- **Se agregó:** Fuente: elaboración propia a partir de Multitiendas Ancoa S.A.
- **Se agregó:** (2026, Caso 09, cap. 15, requisito RT-05.10, p. 33), RT-07.09 a RT-07.13 y el inventario de datos y custodia.\par\nopagebreak
- **Se agregó:** \begin{longtable}{@{}p{0.27\linewidth}p{0.27\linewidth}p{0.40\linewidth}@{}}
- **Se agregó:** \toprule Dominio & Retención & Copia en Brazil South \\
- **Se agregó:** \midrule\endhead\bottomrule\endlastfoot
- **Se agregó:** Venta, documento tributario y líneas & 6 años. & Réplica y archivo de Retail, con restauración probada.
- **Se agregó:** \\
- **Se agregó:** Precio publicado por canal & 3 años. & Archivo de Retail recuperable.
- **Se agregó:** \\
- **Se agregó:** Inventario y conteo & 6 años. & Copia de Retail.
- **Se agregó:** \\
- **Se agregó:** Crédito, cartera, evaluación, aceptación y cobranza & Plazo de cada crédito más 6 años. & Réplica y archivo de la filial emisora, con el RPO medido.
- **Se agregó:** \\
- **Se agregó:** Grabación y soporte de consentimiento & Plazo del crédito más 6 años. & Copia inmutable de la filial emisora e índice recuperable.
- **Se agregó:** \\
- **Se agregó:** Bitácora del Servicio de control de cruces & La del expediente de crédito o de la venta que cada hecho enlaza. & Copia de X-01.
- **Se agregó:** \\
- **Se agregó:** Videovigilancia & 30 días, con grabación local propia del sitio. & Solo casos y evidencia autorizados, con política por cerrar.
- **Se agregó:** \\
- **Se agregó:** Eventos de seguridad & 12 meses en línea y 24 más en archivo (RT-11.14). & Copia y recuperación por frente.
- **Se agregó:** \\
- **Se agregó:** \end{longtable}
- **Se agregó:** La Tabla 4.26 muestra la retención de cada dominio y su copia en Brasil.
- **Se agregó:** La retención de venta, crédito, precio, inventario y videovigilancia es la que fija el Caso, y la de los eventos de seguridad es la de RT-11.14.
- **Se agregó:** Réplica es la copia continua de una base de datos, archivo es la copia de documentos que ya no cambian y copia inmutable es la que nadie puede borrar sin la aprobación de una segunda persona.
- **Se agregó:** La frecuencia de cada respaldo, la retención de largo plazo de PostgreSQL y el tiempo de restauración de cada dominio se declaran en el diseño detallado, y la prueba mensual de restauración (RT-07.12) mide el tiempo efectivo.
- **Se agregó:** Cada servicio productor conserva los hechos confirmados que debe comunicar y cada consumidor registra los identificadores de aquellos cuyo efecto ya aplicó y los conserva durante la ventana de deduplicación.
- **Se agregó:** El efecto de un hecho y su identificador se confirman en la misma transacción y en el mismo servidor, y el corte común entre los 12 servidores de PostgreSQL se fija por una marca de tiempo.
- **Motivo:** P-10 (opción 1): corte común por marca de tiempo; P-15 (opción 2) y parte 1 del 09-11: ventana de deduplicación; P-06 (tabla en 4.3.2) y agentes: retención y copia por dominio; Cierre parte 3: folio y capítulo del Caso
- **Base:** S-42; RT-02.06; RT-07.04; S-43; S-43b; RT-02.06; RT-07.09 a RT-07.13; Caso cap. 15, p. 33; citas-proyecto

### CAM-163 · línea 1146 · 4.3.2 Especificaciones Data Center Secundario · Modificado

- **Se quitó:** La ventana de deduplicación de los consumidores debe cubrir ese mismo intervalo.
- **Se agregó:** La ventana de deduplicación de los consumidores no es menor que el objetivo de 15 minutos más el RTO de 4 horas, y se amplía con el retraso medido de la réplica.
- **Se agregó:** Las claves de las ventas de tienda se retienen al menos 24 horas, porque los diarios locales se concilian al volver el enlace.
- **Motivo:** P-15 (opción 2) y parte 1 del 09-11: ventana de deduplicación
- **Base:** S-43; S-43b; RT-02.06

### CAM-164 · línea 1148 · 4.3.2 Especificaciones Data Center Secundario · Modificado

- **Se quitó:** El ensayo de recuperación comprueba los mensajes pendientes, los hechos recibidos sin efecto confirmado y los duplicados.
- **Se agregó:** El ensayo de recuperación comprueba los mensajes pendientes, los hechos recibidos sin efecto confirmado y los duplicados dentro de esa ventana.
- **Motivo:** Ciclo 4.3.2 (06-11): C-074 a C-084 y ajustes tras lector, hilo lógico y PMBOK
- **Base:** Ver bitácora

### CAM-165 · línea 1152 · 4.3.2.1 Residencia de los datos y recuperación fuera de Chile · Modificado

- **Se quitó:** Brazil South es el destino de recuperación propuesto para Retail, la filial emisora y X-01, con aprobación de residencia por frente.
- **Se quitó:** Las Figuras 4.27 y 4.28 representan esta arquitectura base, sujeta a las aprobaciones del Cliente, y no una autorización ya obtenida.
- **Se agregó:** Brazil South es el destino de recuperación propuesto para Retail, la filial emisora y X-01, con aprobación de residencia por frente, que el Cliente resuelve antes de cerrar el diseño detallado.
- **Se agregó:** Las Figuras 4.23 a 4.25 representan esta arquitectura base, sujeta a las aprobaciones del Cliente, y no una autorización ya obtenida.
- **Motivo:** Texto ajustado a las figuras físicas nuevas (09-11); P-13 (opción 1): plazo único de aprobación de residencia
- **Base:** diagramas-laminas/correspondencia-figuras.json; Art. 23; Ley 21.719

### CAM-166 · línea 1154 · 4.3.2.1 Residencia de los datos y recuperación fuera de Chile · Modificado

- **Se agregó:** Las dependencias globales del proveedor, como la identidad, el borde de entrada, el DNS, la entrega de software y los operadores de red, no se resuelven con la conmutación a Brasil y se evalúan una por una en el diseño detallado.
- **Motivo:** Ciclo 4.3.2 (06-11): C-074 a C-084 y ajustes tras lector, hilo lógico y PMBOK
- **Base:** Ver bitácora

### CAM-167 · línea 1156 · 4.3.2.1 Residencia de los datos y recuperación fuera de Chile · Modificado

- **Se quitó:** Un sitio propio o de un tercero en otra ciudad de Chile se conserva como alternativa si el Cliente no autoriza la residencia en Brasil.
- **Se quitó:** Esa alternativa requiere su propio diseño de cómputo, datos, claves, conectividad y operación.
- **Motivo:** Ciclo 4.3.2 (06-11): C-074 a C-084 y ajustes tras lector, hilo lógico y PMBOK
- **Base:** Ver bitácora

### CAM-168 · línea 1158 · 4.3.2.1 Residencia de los datos y recuperación fuera de Chile · Modificado

- **Se quitó:** Mientras la Agencia de Protección de Datos Personales no declare países adecuados, la vía es la de las cláusulas contractuales que dan garantías adecuadas, para las que existen cláusulas modelo aprobadas por la Subsecretaría de Economía y Empresas de Menor Tamaño (Resolución Exenta RAEX202503748, de 2025).
- **Se agregó:** Mientras la Agencia de Protección de Datos Personales no declare países adecuados, la vía es la de las cláusulas contractuales que dan garantías adecuadas.
- **Motivo:** P-20 (opción 3): se quita la resolución RAEX202503748
- **Base:** Ley 21.719

### CAM-169 · línea 1160 · 4.3.2.1 Residencia de los datos y recuperación fuera de Chile · Modificado

- **Se quitó:** Los datos se cifran en reposo con claves propias de cada frente y en tránsito con TLS, y las claves de Key Vault no se replican de forma automática, porque Brasil tiene una caja fuerte por frente y un proceso controlado de reinyección.
- **Se quitó:** Brazil South está emparejada con una región de Estados Unidos (Microsoft, 2026l), así que el almacenamiento geo-redundante enviaría copias a ese país, y por eso no se usa y una política de Azure lo impide y lo audita.
- **Se quitó:** Cada frente conserva en Brasil sus propias suscripciones, redes, claves, identidades y registros, sin ninguna ruta entre Retail y la filial emisora, y el acceso se rige por privilegio mínimo, elevación temporal con aprobación y grabación de sesión.
- **Se quitó:** Se replica lo necesario para operar dentro del RTO y del RPO, y las copias analíticas que no son críticas se reconstruyen.
- **Se agregó:** Los datos se cifran en reposo con claves propias de cada frente y en tránsito con TLS, y las claves de Key Vault no se replican de forma automática, porque Brasil tiene una caja fuerte por frente y un proceso controlado de reinyección, que parte de una copia de las claves guardada en el Key Vault de Brasil con custodia dual y que se ensaya.
- **Se agregó:** Brazil South está emparejada con la región South Central US, en Estados Unidos (Microsoft, 2026l), así que el almacenamiento geo-redundante enviaría copias a ese país sin la aprobación del Cliente, y por eso no se usa y una política de Azure lo impide y lo audita.
- **Se agregó:** Cada frente conserva en Brasil sus propias suscripciones, redes, claves, identidades y registros, y el acceso se rige por privilegio mínimo, elevación temporal con aprobación y grabación de sesión.
- **Se agregó:** Se replica lo necesario para operar dentro del RTO y del RPO, y el Data Lake de analítica, que no entra en el RPO de 15 minutos, se copia de forma programada y se reconstruye si hace falta.
- **Motivo:** P-07 (opción 1): origen de la reinyección de claves
- **Base:** S-39; RT-07.10

### CAM-170 · línea 1162 · 4.3.2.1 Residencia de los datos y recuperación fuera de Chile · Modificado

- **Se quitó:** Microsoft procesa los datos de Sentinel en Estados Unidos, así que esta transferencia se declara junto con la de recuperación y queda sujeta a la misma aprobación del Cliente y a las mismas garantías.
- **Se quitó:** Si esa capacidad no se puede contratar en Chile Central, los modelos quedan en la región de origen de esa cuenta, y el Cliente debe aprobar esa residencia antes de la Etapa 1.
- **Se agregó:** Microsoft procesa los datos de Sentinel en Estados Unidos, así que esta transferencia, cuya finalidad es la seguridad, se declara junto con la de recuperación y queda sujeta a la misma aprobación del Cliente y a las mismas garantías.
- **Se agregó:** Si el Cliente no aprueba esa transferencia, la detección se opera con una plataforma propia en Chile sobre el clúster de operación, con más operación del proponente y sin la integración nativa con Defender y Entra.
- **Se agregó:** Además, la entrada pública llega a Chile Central por puntos privados de Front Door en Brazil South y en East US, como describe 4.2.4.
- **Se agregó:** Si esa capacidad no se puede contratar en Chile Central, los modelos quedan en la región de origen de esa cuenta, y el Cliente debe aprobar esa residencia antes de cerrar el diseño detallado.
- **Motivo:** P-13 (opción 1): plazo único de aprobación de residencia
- **Base:** Art. 23; Ley 21.719

### CAM-171 · línea 1164 · 4.3.2.1 Residencia de los datos y recuperación fuera de Chile · Modificado

- **Se quitó:** La filial emisora es además una entidad fiscalizada, y la norma de externalización de servicios de su autoridad del mercado financiero alcanza a los emisores de tarjetas y admite procesar o respaldar fuera del país una actividad crítica cuando el directorio cuenta con un informe independiente y deja constancia del análisis.
- **Se quitó:** Only Simple Solutions entrega el análisis técnico y la matriz de riesgos que el informe necesita.
- **Se agregó:** La filial emisora es además una entidad fiscalizada.
- **Se agregó:** La normativa de externalización de servicios de su autoridad del mercado financiero (Capítulo 20-7 de la Recopilación Actualizada de Normas y Circular N.° 2) alcanza a las empresas emisoras de tarjetas de pago y permite que el directorio exceptúe la exigencia de mantener el procesamiento de datos en Chile para servicios que afectan actividades críticas, siempre que se cumplan los requisitos operacionales, se cuente con un informe de una empresa de reconocido prestigio y se deje constancia del análisis (Comisión para el Mercado Financiero, 2019).
- **Se agregó:** Si el país de destino no tiene calificación de riesgo soberano de grado de inversión, que indica un bajo riesgo de impago del país, esa constancia debe acreditar además que sus leyes de protección y seguridad de datos personales son adecuadas.
- **Se agregó:** Only Simple Solutions entrega el análisis técnico que el informe necesita.
- **Motivo:** Ciclo 4.3.2 (06-11): C-074 a C-084 y ajustes tras lector, hilo lógico y PMBOK
- **Base:** Ver bitácora

### CAM-172 · línea 1166 · 4.3.2.1 Residencia de los datos y recuperación fuera de Chile · Modificado

- **Se agregó:** Ese sitio, propio o de un tercero, requiere su propio diseño de cómputo, datos, claves, conectividad y operación.
- **Motivo:** Ciclo 4.3.2 (06-11): C-074 a C-084 y ajustes tras lector, hilo lógico y PMBOK
- **Base:** Ver bitácora

### CAM-173 · línea 1168 · 4.3.2.1 Residencia de los datos y recuperación fuera de Chile · Modificado

- **Se quitó:** Las figuras actuales siguen describiendo exclusivamente la arquitectura base en Brasil.
- **Se agregó:** La Tabla 4.27 compara el destino propuesto con la alternativa, aspecto por aspecto, para que el Cliente elija entre ambos.
- **Se agregó:** \par\vspace{0pt plus 10\baselineskip}\penalty-300\vspace{0pt plus -10\baselineskip}
- **Se agregó:** Tabla 4.27: Brazil South y sitio alternativo en Chile.
- **Se agregó:** Fuente: elaboración propia a partir de RT-07.02, RT-07.04 y RT-07.07.\par\nopagebreak
- **Se agregó:** \begin{longtable}{@{}p{0.18\linewidth}p{0.38\linewidth}p{0.38\linewidth}@{}}
- **Se agregó:** \toprule Aspecto & Brazil South & Sitio alternativo en Chile \\
- **Se agregó:** \midrule\endhead\bottomrule\endlastfoot
- **Se agregó:** Destino & Región de Azure en São Paulo, propuesta como base. & Sitio propio o de un tercero en otra ciudad de Chile, sin usar DC-02.
- **Se agregó:** \\
- **Se agregó:** Aprobación & Residencia por frente, que el Cliente resuelve antes de cerrar el diseño detallado. & La misma aprobación, que decide entre ambos destinos.
- **Se agregó:** \\
- **Se agregó:** Dimensionamiento & 50 máquinas virtuales de espera encendidas y 4 de Power BI apagadas. & Capacidad equivalente para los servicios críticos, que se dimensiona en el diseño detallado.
- **Se agregó:** \\
- **Se agregó:** Objetivos & RTO de cuatro horas y RPO de quince minutos. & Los mismos objetivos, como compromiso condicionado a su diseño.
- **Se agregó:** \\
- **Se agregó:** Ensayo & Conmutación real al menos dos veces al año (RT-07.07). & Ensayo completo antes de la puesta en producción de la etapa, y después dos veces al año.
- **Se agregó:** \\
- **Se agregó:** Limitación conocida & Alta disponibilidad de PostgreSQL en una sola zona hoy (4.3.2.2). & Plataforma que no se presume equivalente a la de Azure, y que el diseño detallado debe definir.
- **Se agregó:** \\
- **Se agregó:** \end{longtable}
- **Se agregó:** La Tabla 4.27 muestra que la alternativa mantiene los objetivos de recuperación de Brasil y cambia el lugar, de modo que el Cliente decide sobre la residencia y no sobre el nivel de recuperación.
- **Motivo:** P-12 (opción 1) y agentes: tabla Brasil frente a la alternativa nacional; P-13 (opción 1): plazo único de aprobación de residencia
- **Base:** S-44; RT-07.02; RT-07.04; Art. 23; Ley 21.719

### CAM-174 · línea 1192 · 4.3.2.2 Procedimiento de conmutación y retorno · Modificado

- **Se quitó:** Primero, el equipo de operación del proponente declara la contingencia según el criterio acordado con el Cliente.
- **Se quitó:** La identidad y las claves de cada frente se verifican primero, después la red y el DNS, y después los datos y la mensajería, donde se promueve la réplica de cada servidor de PostgreSQL y se habilita su alta disponibilidad, que en Brazil South opera por ahora dentro de una misma zona porque Microsoft mantiene bloqueada allí la alta disponibilidad entre zonas para servidores nuevos, condición que se revisa antes de la construcción.
- **Se quitó:** En la penúltima etapa el equipo de operación activa el origen de Brasil en Front Door, que redirige el tráfico, y en la última una prueba funcional comprueba el servicio, incluida la compra con la tarjeta de la filial emisora a través de X-01 y la conciliación de los diarios locales de las tiendas.
- **Se quitó:** Las tiendas siguen vendiendo con sus pares locales durante todo el procedimiento.
- **Se agregó:** Primero, el equipo de operación del proponente declara la contingencia según el criterio acordado con el Cliente, a partir de al menos dos sondas independientes, una de ellas en Brasil, de métricas de transacción reales y de una verificación humana, y nunca por una sola sonda.
- **Se agregó:** La identidad y las claves de cada frente se verifican primero, después la red y el DNS, donde los sitios reconectan al VPN Gateway de cada negocio en Brasil, y después los datos y la mensajería.
- **Se agregó:** En esta etapa se aísla Chile para impedir escrituras simultáneas, se promueve la réplica de cada servidor de PostgreSQL y se habilita su alta disponibilidad.
- **Se agregó:** En la penúltima etapa el equipo de operación activa el origen de Brasil en Front Door, que hasta entonces permanece deshabilitado para evitar una conmutación por falso positivo y que redirige el tráfico de forma gradual, y en la última una prueba funcional comprueba el servicio, incluida la compra con la tarjeta de la filial emisora a través de X-01 y la conciliación de los diarios locales de las tiendas.
- **Se agregó:** En Brazil South la alta disponibilidad de PostgreSQL opera hoy dentro de una misma zona, porque Microsoft mantiene bloqueada allí la alta disponibilidad entre zonas para servidores nuevos (Microsoft, 2026t).
- **Se agregó:** Es una limitación temporal frente al despliegue multizona que exige el artículo 16 de las Bases Administrativas.
- **Se agregó:** La condición se revisa en la suscripción antes de la Etapa 1 y, si el bloqueo continúa, se evalúa con el Cliente otra región de Sudamérica que admita la alta disponibilidad entre zonas.
- **Se agregó:** Esa alta disponibilidad en una sola zona solo entra en servicio al promover la réplica en una contingencia regional, y la caída simultánea de esa zona y de Chile Central es un evento doble que el diseño no cubre hoy.
- **Se agregó:** Las tiendas siguen vendiendo con sus servidores locales durante todo el procedimiento, con tarjeta propia solo si esa compra no se ha declarado no disponible (4.1.12), y la entrega de nuevo cupo preemitido de la filial emisora a las tiendas se bloquea hasta conocer los consumos registrados.
- **Motivo:** P-14 (opción 1) y hilo lógico: origen de Brasil deshabilitado; P-01: cita de la tabla de regiones de PostgreSQL; además, renumeración de tablas o figuras
- **Base:** S-45; RT-07.05; Art. 16.3

### CAM-175 · línea 1197 · 4.3.2.2 Procedimiento de conmutación y retorno · Modificado

- **Se quitó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/recepcion-20261025/9c0f119a62a5.png}
- **Se agregó:** \includegraphics[width=\linewidth,height=0.82\textheight,keepaspectratio]{figuras/diag-04-25_conmutacion.png}
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa

### CAM-176 · línea 1200 · 4.3.2.2 Procedimiento de conmutación y retorno · Modificado

- **Se quitó:** Figura 4.28: X-01 en Brazil South y orden de arranque de la conmutación.
- **Se agregó:** Figura 4.25: Conmutación a Brazil South: orden de arranque de las siete etapas.
- **Motivo:** Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14; Texto ajustado a las figuras físicas nuevas (09-11)
- **Base:** diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa; diagramas-laminas/correspondencia-figuras.json

### CAM-177 · línea 1202 · 4.3.2.2 Procedimiento de conmutación y retorno · Modificado

- **Se quitó:** La conmutación y el retorno se ensayan al menos dos veces al año, con informe, medición del RTO y del RPO alcanzados y plan de corrección de las brechas (RT-07.07).
- **Se quitó:** Las Bases fijan objetivos de cuatro horas y de 15 minutos solo para los servicios críticos, por lo que los objetivos de los demás servicios se declaran por servicio en el diseño detallado.
- **Se agregó:** Tras la transferencia de conocimiento, el personal del Cliente puede ejecutar el procedimiento de conmutación y el de retorno (RT-07.05).
- **Se agregó:** La conmutación y el retorno se ensayan al menos dos veces al año mediante conmutación real, con informe, medición del RTO y del RPO alcanzados y plan de corrección de las brechas (RT-07.07).
- **Se agregó:** El RTO se cuenta desde la interrupción declarada, como define el plan de calidad (SD-09), y los servicios críticos se identifican con el Cliente en el diseño detallado.
- **Se agregó:** Las Bases fijan objetivos de cuatro horas y de 15 minutos solo para los servicios críticos, por lo que los objetivos de los demás servicios se declaran por servicio en ese mismo diseño.
- **Motivo:** P-05 (opción 1): RTO desde la interrupción declarada
- **Base:** SD-09 L185; RT-07.04

### CAM-178 · línea 1206 · Referencias · Agregado

- **Se agregó:** Comisión para el Mercado Financiero.
- **Se agregó:** (2019, 26 de diciembre).
- **Se agregó:** \textit{CMF publica cambios a normativa sobre externalización de servicios en bancos e instituciones financieras} [Comunicado de prensa].
- **Se agregó:** \url{https://www.cmfchile.cl/portal/prensa/625/w4-article-28049.html}.
- **Motivo:** Referencias de las fuentes nuevas
- **Base:** Ver bitácora

### CAM-179 · línea 1249 · Referencias · Modificado

- **Se agregó:** \textit{What is Azure Database for PostgreSQL flexible server?}.
- **Se agregó:** \url{https://learn.microsoft.com/azure/postgresql/flexible-server/overview}.
- **Se agregó:** Microsoft.
- **Se agregó:** (2026u).
- **Motivo:** P-01: cita de la tabla de regiones de PostgreSQL
- **Base:** Art. 16.3

### CAM-180 · línea 1264 · Declaración de uso de IA · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.25 → 4.28)
- **Base:** Comunicado 10

### CAM-181 · línea 1266 · Declaración de uso de IA · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.25 → 4.28)
- **Base:** Comunicado 10

### CAM-182 · línea 1271 · Declaración de uso de IA · Modificado

- **Se quitó:** 4.1 & Codex & Redacción, revisión de coherencia, selección tecnológica y generación de diagramas lógicos. & Alto & Alto & Manuel Aguilera \\
- **Se quitó:** 4.2 & Codex & Redacción, apoyo a dimensionamiento y generación de diagramas físicos y de sitio. & Alto & Alto & Manuel Aguilera \\
- **Se quitó:** 4.3 & Codex & Redacción de la estrategia de centros de datos. & Alto & Alto & Manuel Aguilera \\
- **Se agregó:** 4.1 & Codex y Claude & Redacción, revisión de coherencia, selección tecnológica y generación de diagramas lógicos. & Alto & Alto & Manuel Aguilera; revisión de noviembre pendiente \\
- **Se agregó:** 4.2 & Codex y Claude & Redacción, apoyo a dimensionamiento y generación de los diagramas físicos y de sitio de las Figuras 4.12 a 4.17. & Alto & Alto & Manuel Aguilera; revisión de noviembre pendiente \\
- **Se agregó:** 4.3 & Codex y Claude & Redacción de la estrategia de centros de datos y generación de los diagramas de las Figuras 4.18 a 4.25. & Alto & Alto & Manuel Aguilera; revisión de noviembre pendiente \\
- **Motivo:** Texto ajustado a las figuras físicas nuevas (09-11); Declaración de uso de IA actualizada con las figuras y la redacción de noviembre
- **Base:** diagramas-laminas/correspondencia-figuras.json; Comunicado 10; skill diagramas-ancoa

### CAM-183 · línea 1279 · Declaración de uso de IA · Renumeración

- Solo cambian números de tabla (1 línea(s)). Correspondencia en `ajustes-otros-documentos.md`.
- **Motivo:** Cierre parte 1: renumeración de tablas o figuras por orden de aparición (4.25 → 4.28)
- **Base:** Comunicado 10

## 2. `80_Artefactos/sd-04_contexto/registro-diseno-fisica/00_registro-de-diseno.md`

### REG-201 · línea 135
- **Se quitó:** \| bus_r, bus_e \| Service Bus de Retail y de la Filial \| Service Bus Premium de cada negocio, con geo-replicación \| C3Z, BR \| propuesto \| Sin puente entre los dos \| 2 \|
- **Se agregó:** \| bus_r, bus_e \| Service Bus de Retail y de la Filial \| Service Bus Premium de cada negocio; en Brazil South se habilita en la contingencia y se republica desde registros durables (sin geo-replicación) \| C3Z, BR \| propuesto \| Sin puente entre los dos \| 2 \|

### REG-202 · línea 256
- **Se quitó:** \| H-17 \| Application Gateway se llama «puerta privada» pero el recorrido privado no pasa por él \| Física \| Corregir descripción o recorrido \| **cerrado en el diseño**: con A+ el recorrido privado sí pasa por Application Gateway (E-04); revisar que el texto no lo llame «puerta privada» \|
- **Se agregó:** \| H-17 \| Application Gateway se llama «puerta privada» pero el recorrido privado no pasa por él \| Física \| Corregir descripción o recorrido \| **reabierto y corregido (06-11)**: E-04 es el recorrido público. El privado entra por VPN Gateway y Azure Firewall directo a API Management (`.tex` 4.1.4). El texto no debe llamar a Application Gateway «puerta privada» \|

## 3. `80_Artefactos/sd-04_contexto/registro-diseno-fisica/01_nodos.md`

### REG-301 · línea 3
- **Se quitó:** **Estado:** en construcción. Empieza por la **tienda tipo** (Lección 1). Siguen: Chile Central, Brazil South, casa matriz, centros de distribución.
- **Se agregó:** **Estado:** completo como borrador sin revisión humana (06-11-2026). Cubre tienda tipo, Chile Central, Brazil South, casa matriz, centros de distribución, contrapartes y servicios globales.

### REG-302 · línea 53
- **Se quitó:** \| Azure Front Door (entrada pública) \| FL-01, FL-02 \| 1, con políticas por negocio \| Front Door → origen ≤150 ms vía Brasil (P-02); consulta de disponibilidad ≤400 ms de extremo a extremo (RT-09.01) \| Máxima para el canal digital. Si cae, los clientes no entran por Internet \| 693 consultas por segundo en el peak (Tabla 4.21); el límite de Microsoft por grupo regional es 7.200 \| Filtro contra ataques (WAF). Políticas separadas por negocio \| Entra por Internet; llega a su origen por enlace privado \| Se acepta el costo de un servicio global de nivel Premium porque es el único que ofrece enlace privado al origen y filtro de ataques en un solo punto \| confirmado D-FIS-15 (A+): enlace privado con dos regiones de Private Link, Brazil South y otra por medir (06, P-05) \|
- **Se agregó:** \| Azure Front Door (entrada pública) \| FL-01, FL-02 \| 2 perfiles (Retail y Filial emisora); Control de cruces sin entrada pública \| Front Door → origen ≤150 ms vía Brasil (P-02); consulta de disponibilidad ≤400 ms de extremo a extremo (RT-09.01) \| Máxima para el canal digital. Si cae, los clientes no entran por Internet \| 693 consultas por segundo en el peak (Tabla 4.21); el límite de Microsoft por grupo regional es 7.200 \| Filtro contra ataques (WAF). Políticas separadas por negocio \| Entra por Internet; llega a su origen por enlace privado \| Se acepta el costo de un servicio global de nivel Premium porque es el único que ofrece enlace privado al origen y filtro de ataques en un solo punto \| confirmado D-FIS-15 (A+): enlace privado con dos regiones de Private Link, Brazil South y otra por medir (06, P-05) \|

### REG-303 · línea 62
- **Se quitó:** \| Azure Bastion (acceso administrativo seguro) \| FL-11 \| 3 (uno por red central) \| — \| Media \| Pocos usuarios \| Acceso con identidad nominal y registro; sin SSH/RDP público \| Desde Internet con autenticación fuerte \| Costo por hora; se acepta por exigencia de acceso seguro \| propuesto; 3 coincide con la ficha de seguridad (F) \|
- **Se quitó:** \| DNS Private Resolver (resuelve nombres internos) \| FL-10 \| 3 (uno por frente) \| — \| Media-alta: sin él no se encuentran los servicios internos \| — \| Zonas privadas separadas por frente \| Entre sitios y red central \| Costo por hora; se acepta por mantener nombres separados por frente \| propuesto; disponibilidad en Chile Central sin lista pública, se confirma en la suscripción (S-22; alternativa: 2 VM DNS por frente) \|
- **Se agregó:** \| Azure Bastion (acceso administrativo seguro) \| FL-11 \| 3 (uno por red central) \| — \| Media \| Pocos usuarios \| Acceso con identidad nominal y registro; sin SSH/RDP público \| Por Entra Private Access, con verificación de identidad y de equipo; el recurso lleva IP pública Standard bajo DDoS Protection (S-27) \| Costo por hora; se acepta por exigencia de acceso seguro \| propuesto; 3 coincide con la ficha de seguridad (F) \|
- **Se agregó:** \| DNS Private Resolver (resuelve nombres internos) \| FL-10 \| 3 (uno por frente) \| — \| Media-alta: sin él no se encuentran los servicios internos \| — \| Zonas privadas separadas por frente \| Entre sitios y red central \| Costo por hora; se acepta por mantener nombres separados por frente \| propuesto; disponible en Chile Central y Brazil South (S-22 verificado) \|

### REG-304 · línea 86
- **Se quitó:** \| Réplicas de las bases en Brazil South \| — \| 1 por base crítica (ver bloque 4) \| Retraso de la réplica: lo mide el ensayo (RPO ≤15 min) \| Máxima para DR \| Igual a la base \| Mantiene la separación por negocio \| Enlace entre regiones \| Costo aceptado de tener una segunda copia viva \| propuesto; se detalla en el bloque 4 \|
- **Se quitó:** \| Service Bus Premium de Retail \| SB-R \| 1 espacio de mensajería \| Misma región \| Alta: desacopla la venta de los destinos \| ~56 mensajes/s promedio, diseñado a 10× (560/s) \| Sin puente hacia la Filial \| Red de datos de Retail \| Nivel Premium por red privada y capacidad reservada \| propuesto \|
- **Se agregó:** \| Réplicas de las bases en Brazil South \| — \| 1 por servidor (12; S-06; ver bloque 4) \| Retraso de la réplica: lo mide el ensayo (RPO ≤15 min) \| Máxima para DR \| Igual a la base \| Mantiene la separación por negocio \| Enlace entre regiones \| Costo aceptado de tener una segunda copia viva \| propuesto; se detalla en el bloque 4 \|
- **Se agregó:** \| Service Bus Premium de Retail \| SB-R \| 1 espacio de mensajería \| Misma región \| Alta: desacopla la venta de los destinos \| 56 mensajes/s de promedio; pico de diseño 6.667 entregas/s en la carga masiva de precios (ver 05) \| Sin puente hacia la Filial \| Red de datos de Retail \| Nivel Premium por red privada y capacidad reservada \| propuesto \|

### REG-305 · línea 134
- **Se quitó:** \| Pipelines de entrega (CI/CD) y agentes efímeros \| CI-CD-R/F/X \| 3 conjuntos de pipelines, sin máquina fija \| Sin objetivo \| Alta: es el único camino a Producción \| Un pipeline por servicio \| SAST, SCA y DAST (análisis estático, de dependencias y dinámico), firma y verificación de procedencia; los desarrolladores no entran directo a Producción \| Agentes con identidad federada, permisos mínimos y acceso privado \| Los agentes efímeros se facturan por uso, sin máquina fija; si el producto exige un agente privado permanente se agrega como máquina \| propuesto; la plataforma de CI/CD no está definida en el inventario \|
- **Se agregó:** \| Pipelines de entrega (CI/CD) y agentes efímeros \| CI-CD-R/F/X \| 3 conjuntos de pipelines, sin máquina fija \| Sin objetivo \| Alta: es el único camino a Producción \| Un pipeline por servicio \| SAST, SCA y DAST (análisis estático, de dependencias y dinámico), firma y verificación de procedencia; los desarrolladores no entran directo a Producción \| Agentes con identidad federada, permisos mínimos y acceso privado \| Los agentes efímeros se facturan por uso, sin máquina fija; si el producto exige un agente privado permanente se agrega como máquina \| propuesto; Azure Pipelines (S-04) con agentes efímeros en conjunto de escalado (S-28) \|

### REG-306 · línea 143
- **Se quitó:** 2. **Plataforma de CI/CD:** el inventario no define producto (repositorio y orquestador). Decidir cuál y si requiere agentes permanentes.
- **Se agregó:** 2. Resuelto: Azure Pipelines con agentes efímeros (S-04, S-28).

### REG-307 · línea 169
- **Se quitó:** \| Service Bus Premium en Brazil South \| BR-R/F \| 2 (uno por negocio), con geo-replicación de datos y metadatos \| Retraso de replicación medido \| Alta \| Igual que Chile \| Sin puente entre negocios \| Red de datos de cada negocio en Brasil \| Costo por unidad de mensajería; se acepta \| propuesto; los consumidores deben tolerar duplicados \|
- **Se agregó:** \| Service Bus Premium en Brazil South \| BR-R/F \| 2 (uno por negocio), habilitados en la contingencia, sin geo-replicación del namespace: los mensajes se republican desde los registros durables de productores y consumidores \| Retraso de replicación medido \| Alta \| Igual que Chile \| Sin puente entre negocios \| Red de datos de cada negocio en Brasil \| Costo por unidad de mensajería; se acepta \| propuesto; los consumidores deben tolerar duplicados (republicación, no réplica; ver H-07 y `.tex` 4.3.2) \|

### REG-308 · línea 182
- **Se quitó:** 3. Qué bases son realmente críticas y cuáles se reconstruyen: las reconstruibles no necesitan réplica viva.
- **Se agregó:** 3. Resuelto por S-06: las 12 bases tienen réplica en Brazil South.

### REG-309 · línea 195
- **Se quitó:** \| Recinto técnico de casa matriz (energía, climatización, incendio, acceso) \| DC-01 (RT-06.xx) \| 4 racks de 42U (Retail, Filial, comunicaciones y respaldo local), reserva inicial 80 de 168U; UPS ≥30 min a plena carga con doble alimentación A y B; generación autónoma ≥24 h; climatización de precisión N+1; detección de incendio por aspiración con extinción por agente limpio; acceso biométrico; videovigilancia con 30 días \| — \| Alta: sin ellos los sistemas conservados quedan sin soporte \| 99,95 % mensual exigido para energía, climatización y red del recinto \| Sala técnica principal: RT-06.01 a RT-06.24 íntegros; hoy el recinto de 2011 cumple solo parcialmente (informe interno 2024 pendiente de entrega) \| Dos accesos de operadores distintos, segregados por negocio \| Costo de habilitación del recinto especificado por OSS; la obra civil de separación la ejecuta el Cliente (RT-06.06) \| propuesto (.tex 4.3.1); brecha real por levantar \|
- **Se agregó:** \| Recinto técnico de casa matriz (energía, climatización, incendio, acceso) \| DC-01 (RT-06.xx) \| 4 racks de 42U (Retail, Filial, comunicaciones y respaldo local), 80 de 168U presupuestadas y 88 libres, con parte de las 80U como reserva para el legado desconocido (`cierre-inventario/10-espacio-racks.md`); UPS ≥30 min a plena carga con doble alimentación A y B; generación autónoma ≥24 h; climatización de precisión N+1; detección de incendio por aspiración con extinción por agente limpio; acceso biométrico; videovigilancia con 30 días \| — \| Alta: sin ellos los sistemas conservados quedan sin soporte \| 99,95 % mensual exigido para energía, climatización y red del recinto \| Sala técnica principal: RT-06.01 a RT-06.24 íntegros; hoy el recinto de 2011 cumple solo parcialmente (informe interno 2024 pendiente de entrega) \| Dos accesos de operadores distintos, segregados por negocio \| Costo de habilitación del recinto especificado por OSS; la obra civil de separación la ejecuta el Cliente (RT-06.06) \| propuesto (.tex 4.3.1); brecha real por levantar \|

### REG-310 · línea 201
- **Se quitó:** \| Centro de distribución de Concepción \| CD-02 \| 1 sitio (9.000 m²) \| — \| Media-alta \| Opera con planillas, sin WMS acreditado \| Se elimina la planilla como registro \| Hoy un solo enlace; RT-03.17 exige segundo proveedor y ruta física \| Segundo enlace aceptado por exigencia \| confirmado por el Caso; captura estructurada por decidir \|
- **Se agregó:** \| Centro de distribución de Concepción \| CD-02 \| 1 sitio (9.000 m²) \| — \| Media-alta \| Opera con planillas, sin WMS acreditado \| Se elimina la planilla como registro \| Hoy un solo enlace; RT-03.17 exige segundo proveedor y ruta física \| Segundo enlace fijo **propuesto** al Cliente (S-10); el router 4G/5G es el segundo camino \| confirmado por el Caso; captura estructurada por decidir \|

### REG-311 · línea 210
- **Se quitó:** 5. Segundo enlace y segunda ruta física de Concepción: exigido por RT-03.17; el operador se define con el Cliente.
- **Se agregó:** 5. Segundo enlace y segunda ruta física de Concepción: RT-03.17 lo exige y el Caso dice enlace único; se propone al Cliente y el router 4G/5G cubre mientras tanto (S-10).

### REG-312 · línea 224
- **Se quitó:** \| Plataforma publicitaria (Retail Media Network) \| EXT-ADS \| 1 contraparte \| Sin objetivo: el canal omite el resultado patrocinado si no responde \| Baja \| Campañas y resultados agregados \| Sin datos financieros (`.tex` 4.1.7) \| Adaptador del grupo de integración de Retail por la salida controlada (E-41, E-45) \| Contrato del tercero \| pendiente; proveedor por elegir \|
- **Se agregó:** \| Plataforma publicitaria (Retail Media Network) \| EXT-ADS \| 1 contraparte \| Sin objetivo: el canal omite el resultado patrocinado si no responde \| Baja \| Campañas y resultados agregados \| Sin datos financieros (`.tex` 4.1.7) \| Adaptador del grupo de integración de Retail por la salida controlada (E-41, E-45) \| Contrato del tercero \| supuesto S-31: Criteo u opción técnicamente equivalente; contrato antes de la Etapa 2 \|

### REG-313 · línea 232
- **Se quitó:** Los pendientes de cada bloque quedan cubiertos por los **supuestos S-01 a S-18** de `06_supuestos-pendientes.md`: cada uno tiene valor adoptado, razón y qué cambia si resulta falso.
- **Se agregó:** Los pendientes de cada bloque quedan cubiertos por los **supuestos S-01 a S-32** de `06_supuestos-pendientes.md`: cada uno tiene valor adoptado, razón y qué cambia si resulta falso.

## 4. `80_Artefactos/sd-04_contexto/registro-diseno-fisica/02_conexiones.md`

### REG-401 · línea 20
- **Se quitó:** \| E-03b \| Azure Front Door → punto privado de Front Door en una segunda región admitida de las Américas (origen privado 2, prioridad menor) \| Private Link \| Cifrado de la plataforma \| Un punto por negocio, región por medir \| Respaldo del origen privado 1; mayor latencia \| D-FIS-15 (A+) \| propuesto; región por elegir \|
- **Se agregó:** \| E-03b \| Azure Front Door → punto privado de Front Door en una segunda región admitida de las Américas (origen privado 2, prioridad menor) \| Private Link \| Cifrado de la plataforma \| Un punto por negocio, región por medir \| Respaldo del origen privado 1; mayor latencia \| D-FIS-15 (A+) \| propuesto; East US con prioridad 2 (S-03) \|

### REG-402 · línea 119
- **Se quitó:** \| E-54 \| PostgreSQL de Chile → réplica en Brazil South \| Réplica asíncrona del producto \| Sí \| Una por base crítica \| Retraso medido; sobre 15 min no se promete el RPO \| C42, FL-12 \| propuesto \|
- **Se quitó:** \| E-55 \| Service Bus de Chile → Service Bus de Brazil South \| Geo-replicación de datos y metadatos \| Sí \| Una por negocio \| Consumidores toleran duplicados \| C42, FL-12 \| propuesto \|
- **Se agregó:** \| E-54 \| PostgreSQL de Chile → réplica en Brazil South \| Réplica asíncrona del producto \| Sí \| Una por servidor (12, S-06) \| Retraso medido; sobre 15 min no se promete el RPO \| C42, FL-12 \| propuesto \|
- **Se agregó:** \| E-55 \| Registros durables de productores y consumidores (con la réplica de PostgreSQL) → Service Bus de Brazil South, habilitado en la contingencia \| Republicación desde un punto de recuperación; sin geo-replicación del namespace \| Sí \| Una por negocio \| Consumidores toleran duplicados y descartan lo ya procesado \| C42, FL-12 \| propuesto; reformulado 06-11 (K-01) \|

## 5. `80_Artefactos/sd-04_contexto/registro-diseno-fisica/03_ambientes.md`

### REG-501 · línea 24
- **Se quitó:** \| Service Bus \| Reducido \| Reducido \| Reducido \| 2 espacios \| 2 con geo-replicación \|
- **Se agregó:** \| Service Bus \| Reducido \| Reducido \| Reducido \| 2 espacios \| 2, habilitados en la contingencia y recuperados por republicación desde registros durables \|

## 6. `80_Artefactos/sd-04_contexto/registro-diseno-fisica/05_capacidad.md`

### REG-601 · línea 40
- **Se quitó:** \| Service Bus (por negocio) \| Entregas por segundo \| Carga de precios: 1,6 M entregas/día; promedio 56/s en 8 h; diseñado a 10× de ráfaga ≈ 560/s \| Unidades de mensajería Premium escalables, por fijar \| **Calculada** (promedio) + **criterio** (10×) \|
- **Se agregó:** \| Service Bus (por negocio) \| Entregas por segundo \| Promedio de 56 entregas/s (1,6 M al día en 8 h). Pico que fija el diseño: carga masiva de precios, 400.000 cambios × 5 tipos de consumidor ÷ 300 s = 6.667 entregas/s (publicados 1.333/s). Sincronización de existencia: 1.135 mensajes/s. Si coinciden: 7.802/s (hipótesis de solape, sin fuente) \| Unidades de mensajería Premium escalables, por fijar con la prueba de carga de Preproducción. El factor 10× sobre el promedio (560/s) queda descartado: no cubre el pico \| **Calculada** (6.667 y 7.802: aritmética sobre SD-05 Tabla 5.18) + **hipótesis** (solape). Capacidad de una unidad de mensajería: no verificada \|

### REG-602 · línea 68
- **Se agregó:** 0. **Service Bus:** recalculado el 06-11. El diseño parte del pico de 6.667 entregas/s y no del 10× sobre el promedio. Falta el dato de capacidad por unidad de mensajería Premium (Microsoft Learn), sin el cual no se fija el número de unidades. La prueba de carga de Preproducción lo mide (RT-09.01, RT-09.03).

## 7. `80_Artefactos/sd-04_contexto/registro-diseno-fisica/06_supuestos-pendientes.md`

### REG-701 · línea 91
- **Se quitó:** \| S-27 \| **Azure Bastion nivel Premium con IP pública Standard con redundancia de zonas, desplegado entre las tres zonas de Chile Central**, bajo Azure DDoS Protection (aprobado por el usuario 02-11) \| **Verificado:** la grabación de sesiones exige Premium; las zonas exigen IP pública Standard con redundancia de zonas; Chile Central figura en las regiones con zonas, **en vista previa**, y Brazil South no (Learn, «Reliability in Azure Bastion», act. 30-09-2026). El `.tex` declara la vista previa \| Si las zonas no están disponibles al desplegar: un Bastion sin zonas en Chile Central, con su riesgo declarado; en Brazil South ya es sin zonas \|
- **Se agregó:** \| S-27 \| **Azure Bastion nivel Premium con IP pública Standard con redundancia de zonas, desplegado entre las tres zonas de Chile Central**, bajo Azure DDoS Protection (aprobado por el usuario 02-11) \| **Verificado:** la grabación de sesiones exige Premium; las zonas exigen IP pública Standard con redundancia de zonas; Chile Central figura en las regiones con zonas, **en vista previa**, y Brazil South no (Learn, «Reliability in Azure Bastion», act. 30-09-2026). El `.tex` aún no declara la vista previa (cotejo 06-11: pendiente de redacción en 4.2.3) \| Si las zonas no están disponibles al desplegar: un Bastion sin zonas en Chile Central, con su riesgo declarado; en Brazil South ya es sin zonas \|

### REG-702 · línea 97
- **Se agregó:** \| S-33 \| **Tipología on-premise por sitio** (Transversales §6.1): DC-01 «sala técnica principal» (S-07, por alojar ERP/DTE y núcleo Retail, cómputo sustantivo del Cliente); tienda tipo y centros de distribución «sala técnica secundaria o de sitio» (cómputo local para continuidad, sin albergar el núcleo); DC-02 sin tipología hasta acreditar su uso. El Caso (RT-06.01) pide «gabinete por tienda»; la tipología secundaria es más exigente y no rebaja nada (06-11) \| Transversales §6.1: declarar la tipología de cada sitio y justificar el dimensionamiento. Tienda: 4 servidores, 2 UPS, clima N+1 y sensores (01, bloque 1), más que un gabinete \| Si el Cliente exige gabinete en tienda, baja el dimensionamiento de energía y clima, sin tocar los servidores \|
- **Se agregó:** \| S-34 \| **Almacenamiento local en RAID 1:** dos discos SSD de 960 GB en espejo por servidor de tienda y de centro, que tolera la falla de un disco. El RAID no es respaldo: la copia local cifrada es aparte (06-11) \| RT-03.14 y Art. 16.4: declarar el nivel RAID y justificarlo. `01`:19-20 ya fija «2 discos de 960 GB en espejo». Con dos discos por servidor y un par de servidores por negocio, RAID 1 es el nivel posible; RAID 5, 6 y 10 exigen más discos \| Con más discos por servidor se reevalúa RAID 10 o 6 y cambia el factor de compra \|
- **Se agregó:** \| S-35 \| **Endurecimiento y parches de los sistemas on-premise:** CIS Benchmarks aplicables, gestión centralizada de parches y ventana de aplicación acordada con el Cliente fuera de los congelamientos; administración remota y centralizada de dispositivos de borde con Intune (06-11) \| RT-03.15, RT-03.18 y Art. 16.4. No se nombra otro producto de parches: el catálogo solo trae Intune y Defender \| Si Intune no cubre servidores Linux de tienda (`01` bloque 3b: licencias y cobertura de Defender en Linux y tienda por confirmar), se agrega otra herramienta de gestión \|
- **Se agregó:** \| S-36 \| **FinOps y reversibilidad en nube:** etiquetado obligatorio (ya en el `.tex`), presupuestos y alertas de desviación por grupo de administración y reporte mensual de consumo al Cliente. Reversibilidad según T-11.12: portables los contenedores, PostgreSQL, OpenTelemetry, Data Lake y software de tienda; propios del proveedor API Management, Service Bus, borde y red, claves, Entra, observabilidad de Azure y Power BI (06-11) \| Art. 16.3 (FinOps, servicios administrados, reversibilidad). Clasificación tomada de T-11.12, Tabla portabilidad \| Si el Cliente fija un formato de reporte, solo cambia el entregable mensual \|
- **Se agregó:** \| S-37 \| **Reparto de RT-06.33 y software de los servidores locales (08-11, decidido por el usuario: alternativa A).** RT-06.33 se aplica al recinto técnico de DC-01 (site principal). En tiendas y centros de distribución el proponente especifica, configura y certifica la red y las canalizaciones, y el Cliente las compra y ejecuta, con acta de recepción y certificado de conformidad por sitio. **Par local de captura de los centros: lo provee el proponente.** Software de los servidores de tienda: aplicaciones en contenedores separados por negocio, con persistencia y agentes del negocio en el mismo servidor y sin una máquina virtual por función; sistema operativo y entorno de ejecución se fijan en la implementación \| Caso 09 cap. 11 y Art. 14.2 (el Cliente adquiere y ejecuta; el proponente especifica). `cierre-inventario/03-tienda.md` L80 (contenedores, sistema operativo y runtime en implementación). SD-03 3.2.5 (acta y certificado por sitio) \| Si el Cliente o el evaluador exigen RT-06.33 en todos los sitios: alternativa B o C del análisis del 08-11 (cambian Tabla 4.22, SD-03, T-11.5 y T-14). Sistema operativo e hipervisor siguen sin fijar \|

### REG-703 · línea 117
- **Se quitó:** \| Service Bus geo-replicación: Premium, datos y metadatos, una región secundaria, sin restricción de pares \| Microsoft Learn, «Azure Service Bus Geo-Replication» (act. 15-10-2026) \| E-55 se mantiene; mensajes grandes y espacios particionados no admitidos o en vista previa \|
- **Se agregó:** \| Service Bus geo-replicación: Premium, datos y metadatos, una región secundaria, sin restricción de pares \| Microsoft Learn, «Azure Service Bus Geo-Replication» (act. 15-10-2026) \| Documentada la geo-replicación, **no se adopta** (decisión 06-11, contrastada con RT-07.03): el `.tex` republica desde registros durables; E-55 reformulado \|

### REG-704 · línea 210
- **Se agregó:** ## Decisiones del 09-11-2026 (de `redaccion-2026-11/pendientes-decisiones.md`)
- **Se agregó:** \| ID \| Supuesto o decisión \| Origen \| `.tex` \|
- **Se agregó:** \| :--- \| :--- \| :--- \| :--- \|
- **Se agregó:** \| S-38 \| Objetivo de tiempo de conmutación entre accesos de tienda: 30 segundos, medido en el corte provocado (RT-03.17) \| P-04, usuario \| 4.2.6 \|
- **Se agregó:** \| S-39 \| Copia de las claves en el Key Vault de Brasil con custodia dual y ensayo, como origen de la reinyección (RT-07.10) \| P-07, usuario \| 4.3.2 \|
- **Se agregó:** \| S-40 \| El recinto técnico de DC-01 es de uso exclusivo de la solución y de los sistemas conservados con que convive (RT-06.01) \| P-08, usuario \| 4.2.1 \|
- **Se agregó:** \| S-41 \| Frontera en el rack: el proponente provee canalizaciones hasta él y el Cliente ejecuta el cableado (RT-06.33) \| P-09, usuario \| 4.2.1, Tabla 4.22 \|
- **Se agregó:** \| S-42 \| Efecto e identificador se confirman en la misma transacción y servidor; corte común entre los 12 servidores por marca de tiempo \| P-10, usuario \| 4.3.2 \|
- **Se agregó:** \| S-43 \| Ventana de deduplicación = retraso máximo de la réplica + RTO (15 min + 4 h) \| P-15, usuario \| 4.3.2 \|
- **Se agregó:** \| S-44 \| Sitio alternativo en Chile con capacidad equivalente a la espera de Brasil para los servicios críticos, a dimensionar en el diseño detallado \| P-12, usuario \| Tabla 4.25 \|
- **Se agregó:** \| S-45 \| Origen de Brasil en Front Door deshabilitado hasta la penúltima etapa y activado por el equipo \| P-14, usuario \| 4.3.2.2 \|
- **Se agregó:** \| S-46 \| Procedimientos manuales de las ocho funciones no disponibles sin enlace (Tabla 4.28): originación y cupos, tarjeta propia sin topes, saldo y mora, emisión tributaria sin modalidad, existencia de otros canales, lockers y móviles, precios nuevos y analítica en línea. Los procedimientos son propuesta del proponente y se acuerdan con el Cliente \| P-02, usuario; RT-03.13 \| 4.1.12 \|
- **Se agregó:** \| S-47 \| Los 25 actores (14 personas y 11 sistemas) salen del diagrama de contexto agrupado, no del análisis UAW del SD-07 (31). Reunidos: AH-03+04, AH-06+08, AH-16+18, AS-09+10, AS-01+11. AH-17 pasa a sistemas y AS-14 es interno \| C-008; decisión del usuario 24-10 y confirmación 06-11 \| 4.1.2 \|
- **Se agregó:** \| S-43b \| Corrección 09-11: la ventana de deduplicación no es menor que 15 min + 4 h y se amplía con el retraso medido de la réplica; las claves de ventas de tienda se retienen al menos 24 h por la conciliación de diarios. Reemplaza la fórmula «retraso máximo + RTO» de S-43 \| Revisor de hilo lógico; pendiente de aprobación del usuario \| 4.3.2 \|
- **Se agregó:** \| S-46b \| La jefatura de tienda ejecuta los procedimientos manuales de la Tabla 4.28 y la filial emisora define los dos primeros. Propuesta, por acordar con el Cliente \| Revisores 09-11 \| 4.1.12 \|

