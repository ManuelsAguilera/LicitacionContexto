# Especificación reproducible de vistas, nodos y flujos de SD-04

**Fecha:** 8 de octubre de 2026. **Propósito:** fuente de revisión para las figuras lógicas de SD-04 y puente hacia el dimensionamiento físico de 4.2 y T-11. Los códigos funcionales de SD-03 y los IDs de [inventario lógico](inventario_componentes_logicos_sd04.md) prevalecen sobre los alias gráficos de este documento.

## Reglas de lectura

- **S**: solicitud/respuesta síncrona; **A**: hecho confirmado o mensaje diferido; **L**: operación local sin enlace; **F**: archivo o protocolo de convivencia. Una flecha indica transferencia o uso, no una interfaz existente ya inventariada.
- **Sólida**: relación incluida en el alcance; **discontinua**: destino, alojamiento, contrato o enlace por acreditar; **bloqueada**: acceso no autorizado o flujo todavía cerrado.
- La filial emisora es una **entidad y ámbito de autoridad**, no un edificio. El CD principal y el CD de Concepción son centros de **distribución**; DC-01 es el **centro de datos** de casa matriz.
- Un actor UAW es un rol o contraparte del sistema de casos de uso, no necesariamente un proceso o nodo desplegable. AH-17 es vendedor externo por API según la decisión aportada; AS-11 es la interfaz del módulo de remuneraciones de AS-01, no una segunda plataforma ERP. AS-14 es un disparador de procesos, no un broker. AS-06 no se declara.
- El [archivo UAW aportado](../../80_Artefactos/sd-04_contexto/02_actores_uaw.md) registra 31 actores y UAW 69; se usa como contexto de actores. La autoridad de alcance continúa en Bases y [SD-03](../../02_Propuesta/latex_final/sd-03.tex).

## Vistas que debe cubrir SD-04

| Vista | Tipo de RT-02.03 que satisface | Recorrido necesario | Fuente gráfica propuesta |
| :--- | :--- | :--- | :--- |
| V0 · Contexto y capas | Lógica | Actores agrupados → canal → ocho capas RT-02.01 → dominios y plataformas. | `diag-04-01`, `diag-04-02` |
| V1 · Retail | Lógica/procesos | Oferta → existencias/reserva → pedido → venta → ERP/WMS/transportista; conteo y posventa. | `diag-04-02` más recorridos F-01..F-11 |
| V2 · Emisor y frontera | Lógica/seguridad | Titular/ejecutivo → evidencia → originación/cartera; compra con tarjeta por contrato X-01 y denegación de Marketing. | `diag-04-02`, `diag-04-03` |
| V3 · Tienda híbrida | Procesos/despliegue | POS → caché y diario local → sincronizador → nube → conciliación y evento. | `diag-04-03` |
| V4 · Integración y sitios | Procesos/despliegue | Plataformas conservadas, adaptadores, centro de datos, CD y rutas de enlace candidatas. | `diag-04-03`, `diag-04-04` |
| V5 · Datos y analítica | Datos | Autoridad Retail/Emisor → proyección → lagos y BI separados; ML solo propone. | `diag-04-02`, flujos F-12..F-14 |
| V6 · Seguridad transversal | Seguridad | Identidad y permisos por entidad; X-01 gobierna cruces y registra decisiones en extremos. | `diag-04-02`, `diag-04-03` |
| V7 · Puente físico | Despliegue | Cada familia lógica se asigna a sitio propuesto o ubicación actual desconocida. | `diag-04-04` y matriz de sitios |

Los diagramas no deben intentar representar los 31 actores y todas las aristas con letra diminuta en una sola página. Los códigos de nodo y las tablas permiten ampliar o reconstruir cada vista sin adivinar relaciones.

## Nodos de emplazamiento para V7

| ID | Sitio o ámbito | Nodos incluidos y límite conocido | Conexión a comprobar en 4.2 |
| :--- | :--- | :--- | :--- |
| SIT-01 | 22 tiendas: 14 en centros comerciales y 8 a la calle | POS nuevo C-01/C-02, terminal compartida, periféricos, caché L-01, diario L-02, sincronizador L-03; redes Retail y Emisor segregadas. | Enlace y respaldo por tienda, rutas reales a nube/DC, energía, folios, capacidad de 24 h. |
| CD-01 | CD principal, Región Metropolitana | AH-07, WMS en operación física, captura logística; el servidor WMS no se ubica por inferencia. | Dos proveedores de enlace existentes; contrato WMS y ruta a servicios nuevos. |
| CD-02 | CD Concepción | AH-07 registra existencias; planillas en transición, captura estructurada propuesta, WMS extendido solo si se aprueba. | Enlace único actual; mecanismo durable y ampliación de conectividad por diseñar. |
| DC-01 | Centro de datos casa matriz, 140 m² | Instalación existente compartida por Retail y Emisor; plataformas individuales solo si inventario confirma alojamiento. | Brecha del informe 2024, enlace con nube, segmentación y adaptadores in situ. |
| DC-02 | Sala de respaldo en la misma comuna | Instalación existente; no acredita por sí sola DR independiente. | Riesgo común con DC-01, funciones y capacidad reales. |
| CLD-01 | Azure Chile Central, nube primaria en Santiago (decisión D-12, 2026-10-09) | B-01/B-02, servicios R/F/X, integración I-01..I-08, D-01..03, A-01..06, M-01..03, S-01/02 y O-01/02, separados por ámbito. | Producto y región, zonas, redes privadas, capacidad, licencias y socio certificado. |
| CLD-02 | Azure Brazil South, región secundaria en São Paulo | Recuperación de componentes nuevos, no sustituto de DC-02. | Aprobación de residencia por conjunto, réplica, RTO/RPO y conmutación. |
| EXT-01 | Contrapartes fuera del límite de solución nueva | ERP/DTE, WMS, marketplace, ecommerce, fidelización, transportistas, pagos, proveedores y autoridades; alojamiento de plataformas por acreditar. | Contratos, sentido, protección, latencia y responsable de cada interfaz. |

Ninguna vista debe dibujar **tienda → CD → DC → nube** como cadena obligatoria: el Caso no documenta esa topología. El enlace de una tienda puede terminar en red corporativa, centro de datos o nube según el levantamiento. Las rutas tentativas se muestran discontinuas. El centro de distribución tampoco es un salto de tránsito de las ventas de tienda.

## Correspondencia de todos los actores UAW

Los códigos de canal se refieren al [inventario lógico](inventario_componentes_logicos_sd04.md): C-01 POS Retail, C-02 sesión financiera, C-03 comercio electrónico, C-04 atención, C-05 acceso financiero; otros terminales se describen por su función sin inventar una plataforma nueva.

| Actor | Vista o entrada identificable | Destino funcional y sitio inicial |
| :--- | :--- | :--- |
| AH-01 Cliente | C-03, mesón o C-04 | R:M-01/03, R:V-01/02, R:CL-01; SIT-01 o canal digital → Retail. |
| AH-02 Titular de tarjeta | C-05 o C-02 bajo rol financiero | F:C-01/02/03; Emisor separado incluso en SIT-01. |
| AH-03 Vendedor de piso | Terminal móvil compartida y sesión C-02 | R:M-01/03, R:V-01; F:C-01/03 solo bajo rol financiero. |
| AH-04 Cajero | C-01 y, si procede, C-02 | R:V-02, oferta/existencias; resultado financiero mínimo por X-01. |
| AH-05 Jefatura de tienda | Vista de conteos, merma y exhibición | R:M-01/03, R:V-01, M-01/02 como sugerencias. |
| AH-06 Reposición y bodega tienda | Terminal compartida de conteo/recepción/etiqueta física | R:M-01/02/03; SIT-01. |
| AH-07 Personal de centros de distribución | Vista logística en CD-01 y captura en CD-02 | R:M-02/03, R:V-01; WMS solo donde exista. |
| AH-08 Repositor externo | Acceso individual de tareas autorizado | R:M-01/03, limitado a sus funciones y marca. |
| AH-09 Ejecutivo de atención y posventa | C-04 | R:CL-01, R:V-01/02 y R:V-04 cuando corresponda. |
| AH-10 Ejecutivo financiero | C-05 | F:C-01/02/03 bajo autoridad del Emisor. |
| AH-11 Comercial y compras | Consola de oferta/abastecimiento | R:M-01/02 y fidelización por contrato autorizado. |
| AH-12 Planificación de abastecimiento | Consola de reposición | R:M-02/03 y recomendaciones M-01. |
| AH-13 Canales digitales y Marketing | Consola comercial | R:M-01, R:V-01/04, R:CL-02 y fidelización; saldos y pagos denegados. |
| AH-14 Prevención de pérdidas | Vista de diferencias | R:M-03 y clasificación M-02, con confirmación humana. |
| AH-15 Contraloría y Cumplimiento | Consola de fichas/auditoría | X-01 y evidencia F:C-03 únicamente según entidad y finalidad. |
| AH-16 Administrador TI | Consola de accesos y telemetría | S-01/02, O-01/02 e I-04; administración no concede lectura financiera general. |
| AH-17 Vendedor marketplace | API de vendedor externo | R:V-04 y estados permitidos vía B-02/I-06; actor UAW tipo 1. |
| AH-18 Analista de información | A-05 autoservicio BI | A-02 Retail **o** A-03 Emisor por rol; cruce solo mediante X-01. |
| AS-01 ERP/DTE | Contrato I-05 | R:V-02/03, R:M-02, R:CL-01; emisor tributario único. |
| AS-02 WMS principal | Contrato I-05 | R:M-02/03 y R:V-01; ejecución física CD-01. |
| AS-03 Marketplace vigente | Contrato I-06 | R:V-04, oferta, pedidos y posventa; plataforma conservada. |
| AS-04 Comercio electrónico | Contrato I-07 | C-03 con R:M-01/03, R:V-01/02; destino condicionado. |
| AS-05 Fidelización | Contrato I-07 | R:CL-02/R:M-01; puntos y campañas escritos allí en convivencia. |
| AS-07 Transportistas | Contrato I-08 | R:V-01 recibe estados y acuses autorizados. |
| AS-08 Medios y terminales de pago | Contrato de pago por levantar | C-01/C-03 con R:V-02; no equiparar a F:C-01. |
| AS-09 Núcleo Retail 2009 | Archivo/protocolo I-07 de convivencia | Autoridad temporal por dato en migración de Retail. |
| AS-10 Crédito 2011 | Archivo/protocolo I-07 de convivencia | Autoridad temporal del Emisor hasta corte por ola. |
| AS-11 Remuneraciones del ERP | Interfaz I-05 de AS-01 | Recibe base de comisión R:V-03; no plataforma separada. |
| AS-12 Autoridades fiscalizadoras | Archivo/portal bajo contrato permitido | Expediente/reporte Emisor o DTE según obligación y responsable. |
| AS-13 Proveedores de mercadería | Orden/aviso por canal a validar | R:M-02; formato archivo/protocolo todavía por confirmar. |
| AS-14 Temporizador | Disparador de conciliación y sincronización | R:V-02, I-04, L-03 según proceso; no sistema externo autónomo. |

Esta correspondencia declara **puntos de entrada y nodos lógicos**. No promete interfaces técnicas existentes ni fija la ubicación de los AS que el Caso no localiza. La vista de AH-17 es una API por la decisión UAW; no se inventa un portal para ese vendedor.

## Aristas que deben poder reproducirse

| Flujo | Trayecto y tipo | Autoridad / resultado | Estado |
| :--- | :--- | :--- | :--- |
| F-01 · venta conectada | AH-04 → C-01 → B-01/B-02 → R:M-01 y R:M-03 → R:V-02, **S** | Precio/reserva confirmados antes de cobro; R:V-02 escribe venta. | Alcance; contratos por diseñar. |
| F-02 · pago y DTE | R:V-02 ↔ AS-08 y AS-01 por I-05/contrato de pago, **S/A según contraparte** | Pago se concilia; solo AS-01 emite DTE. | Contratos/contingencia por acreditar. |
| F-03 · corte de tienda | AH-04 → C-01 → L-01/L-02, **L** | Venta y hecho pendiente quedan durables; no se confirma recepción en nube. | Alcance 24 h; cobro/DTE sujetos a modalidad aprobada. |
| F-04 · reconexión | L-02 → L-03 → B-02 → R:V-02 → I-03 → I-02, **A** | ACK, reintento, deduplicación y conciliación antes de difundir hecho. | Destino; ruta física por verificar. |
| F-05 · oferta y etiqueta | AH-11 → R:M-01 → POS/C-03 y terminal de AH-06, **S/A** | Versión aprobada de precio; impresión y confirmación de etiqueta física. | Destino; política ante divergencia por aprobar. |
| F-06 · pedido digital | AH-01 → C-03/AS-04 → R:V-01 ↔ R:M-03 → R:V-02, **S** | Reserva y promesa antes del cobro. | AS-04 integrado inicialmente. |
| F-07 · cumplimiento | R:V-01 ↔ I-05/AS-02 y I-08/AS-07, **S/A** | WMS prepara/despacha; transportista informa avance. | Contratos por levantar. |
| F-08 · CD principal | AH-07/CD-01 ↔ AS-02 ↔ I-05 ↔ R:M-02/03 y R:V-01, **S/F/A** | WMS registra ejecución física; existencias nuevas concilian movimientos. | Servidor y conectividad WMS por verificar. |
| F-09 · Concepción | AH-07/CD-02 → captura estructurada → R:M-02/03, **L/S/A** | Se retiran planillas como autoridad; WMS no se presupone. | Mecanismo local y enlace por diseñar. |
| F-10 · conteo/merma | AH-05/06/14 → R:M-03 → I-03/I-02 → M-01/02 → revisión humana → R:M-03, **S/A** | Modelos recomiendan; persona confirma causa/ajuste. | Modelos sujetos a validación. |
| F-11 · posventa | AH-01/09 → C-04 → R:CL-01 ↔ R:V-02/R:M-03/I-06/AS-01, **S/A** | Producto vuelve a disponible solo tras inspección; AS-01 emite nota. | Alcance; contratos por diseñar. |
| F-12 · crédito | AH-02/10 o AH-03 bajo rol financiero → C-02/C-05 → F:C-03 ↔ F:C-01/F:C-02, **S** | Evidencia previa a apertura/repactación; Emisor escribe. | Sin nueva originación ni cupo sin enlace. |
| F-13 · compra con tarjeta | R:V-02 ↔ F:C-01 mediante contrato mínimo X-01, **S** | Extremos aplican política; solo referencia, monto y decisión mínima aprobados. | Alcance sujeto a ficha jurídica. |
| F-14 · consulta denegada | AH-13 → datos de pago/mora F:C-02, **bloqueada** | X-01 registra denegación; Retail no recibe esos datos. | Prohibición. |
| F-15 · analítica | R/F → I-03/I-02 → A-01 → A-02/A-03 → A-04/A-05 → AH-18, **A/S** | Lagos y permisos separados; X-01 solo para dataset cruzado aprobado. | Destino; motor por seleccionar. |
| F-16 · gobierno | AH-15 → X-01 y evidencia permitida; AH-16 → S/O/I-04, **S** | Auditoría y operación sin privilegio comercial/financiero implícito. | Permisos por diseñar. |
| F-17 · vendedor externo | AH-17 → B-02 → R:V-04 → I-06/AS-03, **S/A** | Reglas de vendedor; AS-03 mantiene plataforma de terceros. | API objetivo; contrato por diseñar. |
| F-18 · remuneraciones | R:V-03 → I-05 → AS-11/AS-01, **A/F según contrato** | ERP calcula/paga remuneraciones; nuevo servicio solo base. | Interfaz por levantar. |
| F-19 · fiscalización | F:C-02/03 o AS-01 → AS-12, **F** | Solo reporte/expediente exigido por obligación y entidad. | Contenido, medio y responsable por confirmar. |
| F-20 · tareas periódicas | AS-14 → conciliación R:V-02/I-04 y sincronización L-03, **A/L** | Dispara proceso; no sustituye autoridad de venta. | Cadencia por medir. |

La selección entre Kafka, Event Hubs y Service Bus se registra en un ADR de middleware. Para cualquiera de ellos, los eventos nacidos sin enlace se guardan **antes** de intentar publicar. El broker en DC-01 o SIT-01 solo se añadirá si se acredita intercambio autónomo entre varios consumidores locales; el diario POS ya resuelve la persistencia de su propia operación.

## Traspaso a la arquitectura física

Para cada ID lógico de la [matriz de 56 componentes](inventario_componentes_logicos_sd04.md) se completará en 4.2: sitio, ambiente, entidad propietaria, red/subred, enlace y respaldo, tecnología/SKU, cantidad y capacidad, disponibilidad de zonas, respaldo/retención, conmutación y renglón T-11. Un `SIT`, `CD`, `DC` o `CLD` es contenedor de emplazamiento: no cuenta como microservicio adicional.

Los datos faltantes que impiden dimensionar son: mapa de catorce interfaces y sus dueños; ubicación de ERP/DTE, WMS, marketplace, ecommerce, fidelización y legados; topología WAN real; inventario POS y periféricos; informe de brechas DC 2024; registros de eventos y transacciones de evento; reglas de DTE/pago durante corte; autorización de residencia de datos del Emisor. Esos vacíos se reflejan con línea discontinua en las figuras, no con una ruta supuesta.
