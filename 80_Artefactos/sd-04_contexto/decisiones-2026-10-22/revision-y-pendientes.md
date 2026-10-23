# Arquitectura lógica: adaptación y pendientes

Estado: propuesta para revisión del equipo. Fecha: 22-10-2026. No constituye revisión humana de la oferta ni certificación de cumplimiento.

Se adaptó la figura anterior al registro y a las dos referencias aportadas por el usuario. La capa de servicios de negocio se agrupa en Mercadería, Venta, Relación con el cliente y Crédito. X-01 queda entre los ámbitos. Las plataformas externas ocupan el espacio inferior de esa misma capa, identificadas como conservadas o en convivencia; sus traductores permanecen en Integración y eventos. Esa ubicación muestra su relación funcional, sin trasladarlas a los clústeres nuevos.

Front Door aparece una sola vez, como símbolo agrupado de los dos perfiles propios de D-11. Cada ruta conserva su ámbito; la agrupación gráfica no crea un perfil compartido.

La entrega contiene el diagrama editable, su imagen y un inventario de conectividad. SD-03 y SD-04 permanecen intactos. Los pendientes documentales siguientes son acciones por realizar, no cambios ya aplicados a esos subdocumentos.

## Archivos

- [Diagrama editable](../../../04_Adjuntos/diagramas/diag-04-27_arquitectura-por-areas-front-door-unico.drawio).
- [Imagen PNG](../../../04_Adjuntos/diagramas/diag-04-27_arquitectura-por-areas-front-door-unico.png) y [SVG ampliable](../../../04_Adjuntos/diagramas/diag-04-27_arquitectura-por-areas-front-door-unico.svg).
- [Especificación validada](../../../04_Adjuntos/diagramas/diag-04-27_arquitectura-por-areas-front-door-unico.json).
- [Inventario de componentes y relaciones](inventario-conectividad.md).
- [Registro recibido, conservado sin cambios](registro-recibido.md).
- [Resultado de comprobaciones](comprobaciones.json).

## Qué se adoptó

| Decisiones | Aplicación en la nueva figura |
| :--- | :--- |
| D-01–D-03, D-54–D-56 | Seis franjas verticales y bandas transversales de Seguridad y Observabilidad; nombres, iconos y agrupación de actores y sistemas. La última instrucción añade las áreas dentro de la capa 4. |
| D-05–D-10 | Portales de tienda y tarjeta separados; app interna por perfiles; caja React servida localmente; simulador CAE dentro del canal de tarjeta. Continuidad de tienda repartida entre servicios, sincronizador y diario local. |
| D-11–D-14, D-17–D-19 | Dos perfiles Front Door con WAF propio; Private Link visible hacia Application Gateway de cada ámbito; dos APIM Premium clásico y dos API Center. Entrada privada de tiendas/CD/DC-01 omite Front Door. X-01 entra por APIM de la Filial. |
| D-16 | API Center representa gobierno de contratos. Su enlace punteado con APIM representa el resultado del pipeline, sin situarlo en el camino de las peticiones. |
| D-21, D-24 | Finanzas abiertas como producto del APIM de la Filial; consentimiento en Evidencia; certificación pendiente declarada en Seguridad. Las sugerencias de IA quedan dentro de Existencias. |
| D-22–D-28 | Servicios comunes separados por ámbito, agrupados como soporte de los servicios existentes. AKS Premium/LTS seleccionado, sujeto a disponibilidad. No se elige motor de flujos. |
| D-29–D-34 | Un Service Bus Premium por ámbito y cuatro familias de traductores. Las cargas masivas son funciones de los traductores. Coordinadores en capa 5 y compensación en cada servicio. |
| D-35–D-39 | Repositorios propios, archivos de retención por ámbito, caché operacional, historial de precios y lagos separados. La alimentación analítica y de archivo sigue abierta. No se representa Brazil South como DR aprobado de la Filial. |
| D-40–D-45 | Identidad, secretos, HSM, seguridad y administración con separación por ámbito. Tenant propio de Filial marcado por confirmar; cupo local en VM y clave de Filial con conexión condicionada. |
| D-47–D-53 | Colector OpenTelemetry, Azure Monitor, métricas/Grafana, Arc y experiencia real. Telemetría separada; no se dibuja un espacio común de datos de negocio. |
| Cinco innovaciones | Conteo predictivo en Mercadería/Existencias; búsqueda y Retail Media en Mercadería/Oferta; lockers en Venta/Pedidos; Modo Tienda y fila virtual en Relación con el cliente/Clientes. Son capacidades de esos servicios. |

Los códigos de los trece servicios permanecen en el JSON para comprobar integridad, sin imprimirse en las tarjetas. Se conservan L-01 para caché de oferta local, L-02 para diario y L-03 para sincronizador; no se renumeran según la nueva ubicación gráfica.

## Cómo se resolvieron las contradicciones del registro

- D-22 a D-27 y D-29 a D-34 aparecen duplicadas. Se conservaron sus decisiones una sola vez.
- D-28 ratifica servicios comunes y AKS Premium. No se solicita otra aprobación de selección; sigue pendiente la disponibilidad de AKS en Chile Central.
- D-33 ya aprueba retirar Event Hubs. La entrada posterior «confirmar D-33» de la lista de pendientes está desactualizada.
- D-23 y D-32 ya ubican la coordinación en capa 5. Falta elegir motor y contratos de sagas, no decidir otra vez su capa.
- D-13 conserva Application Gateway en capa 3 y D-19 retira BFF. La lista antigua que mantiene ambos como cuestión abierta está superada.
- D-40 conserva expresamente la necesidad de confirmar la opción B. No se convirtió el «sí» ambiguo en una aprobación de tenant independiente.
- El historial de cargas y borrados en Miro describe trabajo anterior. No se ejecutaron esas instrucciones ni se modificaron tableros.
- F:C-04 aparece en la última imagen organizativa, pero no está aprobado en el registro ni en el catálogo de trece servicios vigente. No se incorporó un nuevo servicio de control regulatorio; los reportes se mantienen en la familia de integración Crédito.

## Componentes sin conexiones

El inventario distingue la ausencia de flechas de la falta de contrato. Una banda transversal o una tarjeta de alojamiento puede tener cero aristas en esta vista sin ser una función olvidada.

### Siete componentes funcionales con cero aristas

| Componente | Lo que falta | Tratamiento |
| :--- | :--- | :--- |
| Servicios comunes Retail | Servicios consumidores, API/eventos y autoridad de datos por función. | Conservar. Definir qué se implementa dentro de cada servicio y qué se comparte dentro del ámbito. |
| Servicios comunes Filial | Los mismos contratos, con permisos y datos propios. | Conservar por separado; ninguna dependencia común entre negocios. |
| Coordinador de procesos Retail | Sagas concretas, participantes, estado, reintentos y compensaciones. | Conservar como responsabilidad. Elegir motor en la física. |
| Coordinador de procesos Filial | Procesos financieros, autoridad del estado y tratamiento de fallos. | Conservar separado. No conectarlo al bus Retail. |
| Archivo de retención Retail | Productores, exportación, objetos retenidos, consulta y ciclo de vida. | Conservar; vincular después de aprobar su contrato de archivo. |
| Archivo de retención Filial | Evidencias, auditoría, región, claves y consulta autorizada. | Conservar; requiere además cierre de residencia. |
| Azure Backup Vault | Recursos realmente protegibles, política, tipo de bóveda y destino de restauración por ámbito. | Revisar producto/cobertura. No representa por sí solo el respaldo de PostgreSQL, blobs, claves y mensajes. |

### Dos lagos conectados a BI, pero sin alimentación definida

Data Lake Retail y Data Lake Filial tienen una salida hacia los espacios BI de su ámbito. Ninguno tiene entrada desde un servicio, adaptador o proceso de ingestión aprobado. Por tanto, Power BI está conectado gráficamente, pero la cadena analítica está incompleta. Falta decidir entre eventos, extracción/CDC u otro proceso autorizado, con tratamiento de duplicados, borrados, linaje y frescura. No se seleccionó Data Factory, Fabric u otro servicio sin una decisión que lo respalde.

### Ocho tarjetas sin flechas por alcance de la vista

AKS; Entra ID; External ID; Key Vault/Managed HSM; Sentinel/Defender; PIM/Bastion/Private Access; Arc/Monitor Agent; pruebas sintéticas/experiencia real.

AKS identifica alojamiento. Las otras siete tarjetas resumen capacidades transversales aplicables por ámbito. Sus dependencias no se dibujan hacia cada caja para conservar la lectura. Eso no prueba su configuración: el detalle físico debe asignar recursos, identidades, destinos y políticas. En pruebas sintéticas/RUM también faltan herramientas y destinos concretos, recogidos en P-17.

## Decisiones y contratos pendientes

Las prioridades indican orden de resolución propuesto. «Confirmar» corresponde a una decisión humana no acreditada; «verificar» pide evidencia técnica o documental. El resto requiere diseñar contratos de detalle.

| ID | Prioridad | Componentes | Pendiente y evidencia de cierre | Decisión origen |
| :--- | :--- | :--- | :--- | :--- |
| P-01 | Alta | Entra, conectividad, Sentinel, NOC/SOC | Confirmar expresamente tenant independiente para la Filial. Después fijar administración entre tenants y límites de agregación de incidentes/salud. | D-40, D-48, D-52 |
| P-02 | Alta | Front Door, Private Link, App Gateway, APIM | Verificar origen privado por región y aprobación escrita de tránsito del Emisor. Definir también dónde se sirven los recursos web; la ruta dibujada es la entrada de APIs, no el alojamiento completo de los portales. | D-11–D-14, D-45 |
| P-03 | Alta | TLS y certificados de toda la cadena | Probar TLS 1.3 exclusivo por tramo: cliente/borde, borde/origen, gateways, servicios y repositorios. Incluir renovación y alerta de certificados. La versión mínima del borde no acredita cifrado de extremo a extremo. | D-12, D-49 |
| P-04 | Alta | DR y datos de la Filial | Identificar segundo sitio propio distinto de DC-01, independencia de fallas y estrategia de recuperación. El registro pide tres opciones para SD-08, pero no enumera inequívocamente las tres. Presentarlas y aprobarlas antes de comprometer destino/RTO/RPO. | D-35, D-45 |
| P-05 | Alta | Finanzas abiertas | Precisar rol de la Filial, APIs, terceros participantes, consentimiento/revocación y certificación. Contrastar norma y anexo oficiales; no trasladar automáticamente los plazos ni la aplicabilidad de D-20. | D-20, D-21 |
| P-06 | Alta | X-01, APIM Filial y Crédito | Contrato mínimo de autorización, identidad exclusiva de cruce, servicio financiero que resuelve cada operación, idempotencia, timeout y nuevo correlativo por cruce. No existe enlace bus Retail–bus Filial. | D-17, D-27, D-29, D-48 |
| P-07 | Alta | Servicios comunes de ambos ámbitos | Inventariar funciones, consumidores, APIs/eventos y datos. Evitar un microservicio genérico dueño de reglas de todos los contextos. | D-22, D-28 |
| P-08 | Alta | Coordinadores de procesos | Definir sagas, estado en PostgreSQL por ámbito y compensaciones. Comparar Camunda, Temporal y Flowable según esos procesos. | D-23, D-25, D-32, D-38 |
| P-09 | Alta | Service Bus y outbox | Contratos, productores/consumidores completos, orden, retención/relectura, errores persistentes, capacidad y recuperación. Probar el pico indicado en D-33 antes de reintroducir Event Hubs. No equiparar automáticamente sus garantías de retención y replicación. | D-29, D-33 |
| P-10 | Alta | Cuatro familias de adaptadores | Completar la matriz de catorce interfaces: dirección, autoridad, protocolo, frecuencia, sincronía, carga masiva, confirmación y conciliación. Pagos y otras operaciones síncronas necesitan contratos explícitos; la flecha al bus no los sustituye. | D-30, D-34 |
| P-11 | Alta | Lagos/BI y archivo de retención | Definir productores y pipelines propios por ámbito, histórico consultable, segregación, inmutabilidad, ciclo de vida y capacidad. Separar respaldo recuperable de archivo retenido. | D-36, D-39, D-43 |
| P-12 | Alta | Backup Vault y recuperación | Determinar servicio/mecanismo de respaldo soportado para cada recurso y sus destinos permitidos; probar restauración conjunta con claves, evidencia y mensajes. Mantener tarjeta provisional hasta cerrar cobertura. | D-35, D-36 |
| P-13 | Alta | Managed HSM, cifrado e índices | Verificar región, claves por ámbito, rotación/recuperación y uso criptográfico. Diseñar el índice ciego y su riesgo de correlación; la tokenización queda en el procesador de pagos por contratar. | D-37 |
| P-14 | Alta | VM de cupo de Filial en tienda | Fijar red/identidad/clave propias, vigencia y revocación, actualización segura, protección física y comportamiento sin enlace. No habilitar apertura de crédito ni ampliación de cupo offline. | D-44 |
| P-15 | Media | AKS, PostgreSQL, Redis, HSM y BI | Verificar niveles y capacidades en Chile Central, disponibilidad y pruebas de versiones. AKS Premium ya está seleccionado; su disponibilidad no está acreditada. Validar Java 25/Spring Boot 4 y soporte operativo. | D-26, D-28; lista técnica recibida |
| P-16 | Media | External ID, terminales y acceso remoto | Verificar tenantes externos propios por negocio, dispositivo compartido, QR+PIN en vista previa, alternativa soportada, repositores externos y trabajo remoto/Private Access. Costos/licencias deben provenir de cotización verificable. | D-41, D-42 |
| P-17 | Media | OpenTelemetry, Monitor, Grafana y RUM | Probar exportador, compatibilidad de aplicaciones, pérdida y cola local; decidir herramienta móvil, destinos sintéticos TLS 1.3, anomalías y mecanismo NOC entre tenants. El camino OTLP dibujado está condicionado a esas pruebas. | D-47–D-53 |
| P-18 | Media | Oferta, historial y modo tienda | Precisar versión de precio/promoción, caducidad de caché, publicación de historial, actualización de etiquetas y conciliación local. El diario y el sincronizador preservan sus IDs; falta cerrar persistencia y recuperación de tienda. | D-05, D-38, D-39 |
| P-19 | Media | Lockers, Retail Media y búsqueda | Asignar contraparte y adaptador del controlador de lockers y de la plataforma publicitaria; no aparecen inequívocamente en las cuatro familias de D-30. Definir alimentación del índice vectorial y datos/modelo de conteo. Permanecen dentro de los servicios responsables. | D-24, D-30, D-54 |
| P-20 | Media | Portales, actores y alcance | Delimitar portal/app nuevos frente al e-commerce que SD-03 conserva. Fijar cómo Contraloría, TI y analistas acceden a BI/administración: las cinco familias de actores son una síntesis, no una matriz exhaustiva de perfiles. | D-06, D-09, D-56 |
| P-21 | Alta | SD-04, ADR, T-11/T-12 y SD-08 | Conciliar decisiones adoptadas con servicios/niveles, tabla de interfaces, residencia, réplica, alcance y plan de recuperación. Registrar diferencias de versión de las fuentes antes de editar los textos. | D-04, D-16, D-27, D-33, D-35 |

## Qué se retira y qué se traslada

| Elemento anterior o de referencia | Tratamiento |
| :--- | :--- |
| Event Hubs | Retirado de la solución base por D-33. Solo vuelve si la prueba de Preproducción lo exige y se registra esa nueva decisión. |
| BFF, DNSSEC, cajas de autoservicio y portal de fiscalizador | Fuera de la nueva figura por D-08, D-15 y D-19. Eliminar el portal fiscalizador no elimina reportes regulatorios. |
| «Cargas masivas» como caja | Eliminada como componente independiente. Función conservada en los traductores por D-31/D-34. |
| API de vendedor externo | Se mantiene retirada conforme a la instrucción previa. La integración de marketplace sigue existiendo; su contrato y cobertura de actores deben conciliarse con SD-03/04. |
| Conexión directa Front Door–APIM de la figura anterior | Sustituida por Front Door–Private Link–Application Gateway–APIM, siguiendo el nuevo registro. |
| Frontera como franja completa, capa Cliente y bloque final de segmentación | No se reintroducen. Se conserva X-01 como componente y la separación por ámbito. |
| Nodo local en Presentación | Trasladado a continuidad en capas 4, 5 y 6. |
| Sistemas externos en banda inferior | Trasladados a la capa 4 por la última instrucción del usuario; siguen fuera de los servicios nuevos y se conectan mediante traductores de capa 5. |
| Motor de flujos, CI/CD y certificaciones de entrega | El motor se selecciona en la arquitectura física; CI/CD y sus controles se desarrollan allí y en Calidad. La responsabilidad de coordinación permanece visible. |
| Agente directo de Application Insights | No incorporado. Se conserva la ruta de colector OpenTelemetry hacia Monitor por D-47. |
| F:C-04 de la referencia de áreas | No incorporado: la imagen aporta disposición, no una decisión de crear otro servicio. |

No hay fundamento para eliminar servicios comunes, coordinadores, lagos, archivos o respaldo por el solo hecho de que les falten flechas. Deben conservarse como responsabilidades pendientes hasta resolver sus contratos, o eliminarse expresamente si se demuestra una duplicación.

## Inconsistencias contrastadas con los archivos vigentes

El registro remite a líneas de otra versión de SD-04. En esta copia, la fuente editable es `02_Propuesta/latex_final/sd-04/OSS-Subdocumento4.tex`; las ubicaciones se comprobaron contra ese archivo, sin editarlo.

| Hallazgo | Evidencia actual | Consecuencia |
| :--- | :--- | :--- |
| Transporte de eventos | SD-04, líneas 213, 236, ADR-06 en 371, tecnologías en 391, continuidad en 490 y conmutación en 609 todavía describen Event Hubs. | D-33 exige revisar publicación, retención, relectura y recuperación en conjunto; cambiar solo el icono sería insuficiente. |
| X-01 como mediador o control lateral | SD-04, línea 288 describe Ventas enviando a APIM Emisor y X-01 registrando; línea 268 habla de la ruta bajo X-01. | El nuevo recorrido explícito Ventas → X-01 → APIM Filial requiere unificar la explicación y la responsabilidad de operación del control. |
| Cupo local y redes de tienda | SD-04, línea 562 separa el mesón financiero y dice que no pasa por el nodo Retail. | D-44 puede convivir con esa separación solo como VM/red/clave propias de Filial. No basta alojar cupos en el diario Retail. |
| Recuperación de Filial | SD-04, líneas 330, 486, 599 y 607 conservan Brazil South condicionado a residencia. | D-35 cambia la base a un segundo sitio propio para Filial. Debe revisarse la continuidad de todos sus componentes. |
| Conservación de e-commerce | SD-03, líneas 110 y 132 mantiene el comercio electrónico y la fidelización existentes. | El portal/app Retail de D-06 no debe interpretarse automáticamente como reemplazo total de esas plataformas. Delimitar canal nuevo y capacidades conservadas. |
| Prohibición de ampliar crédito sin enlace | SD-03, línea 110 excluye apertura y ampliación de cupos sin conexión. | El cupo local de D-44 solo puede consultar un cupo previamente autorizado y vigente, sin ampliar ese alcance. |
| Árbol de 17 suscripciones y perfil global | Las referencias D-40 «SD4:528» y D-11 «SD4:677» no acreditan esas afirmaciones en esta versión local. La selección general actual está en 462 y 595. | Obtener la versión a la que remitía el registro antes de afirmar una contradicción textual específica sobre 17 suscripciones o un único perfil global. La nueva decisión gráfica sí se conserva. |

## Comprobaciones externas puntuales

Se consultaron fuentes primarias el 22-10-2026. Estas comprobaciones acotan riesgos; no sustituyen pruebas en la suscripción ni una revisión de aplicabilidad normativa.

- Microsoft documenta la conexión de Front Door Premium a Application Gateway mediante Private Link. Eso respalda el patrón de conexión, sin acreditar su despliegue en las regiones y ámbitos propuestos. [Microsoft Learn](https://learn.microsoft.com/en-us/azure/frontdoor/how-to-enable-private-link-application-gateway).
- APIM admite OpenAPI 3.1 para importación, con limitaciones en la semántica de esa versión. Se mantiene la decisión de derivar 3.0.3 y probar que no se pierdan contratos o validaciones. [Restricciones oficiales](https://learn.microsoft.com/en-us/azure/api-management/api-management-api-import-restrictions).
- La política TLS del borde y la negociación hacia el origen son aspectos distintos. No se ha probado TLS 1.3 exclusivo en toda la cadena. [Política TLS de Front Door](https://learn.microsoft.com/en-us/azure/frontdoor/tls-policy).
- La CMF publica la NCG 569 como modificación de la NCG 514 e incorporación del Anexo 3. Eso confirma la existencia del instrumento; queda abierta su aplicación concreta y calendario para esta Filial. [Ficha oficial NCG 569](https://www.cmfchile.cl/portal/normativa/624/w4-article-111273.html).
- La publicación CMF del 7-04-2026 citada en D-35 es una **consulta pública** sobre cambios a RAN 20-7. No se usa como prueba de aprobación de esa propuesta ni de su aplicación automática al emisor del caso. [Comunicado oficial](https://www.cmfchile.cl/portal/prensa/625/w4-article-109289.html).

## Orden propuesto de evaluación

1. Resolver tenant, residencia, recuperación y alcance de Finanzas abiertas. Son decisiones que condicionan red, identidad, datos y contratos.
2. Cerrar rutas de autorización y contratos de servicios comunes, sagas e interfaces. Completar quién llama, qué confirma y quién escribe.
3. Definir ingestión, archivo y respaldo por ámbito, con pruebas de restauración. Cerrar continuidad y cupo local.
4. Probar servicios/regiones, TLS, publicación de contratos y capacidad de mensajería; usar el resultado para fijar T-11/T-12.
5. Conciliar SD-04, ADR, SD-05/08 y formularios. Mantener SD-03 sin cambios hasta que exista una decisión explícita sobre cualquier diferencia de alcance.

La figura es una vista lógica de relaciones principales. Las catorce interfaces, los productores/consumidores por evento y las dependencias transversales deben detallarse en inventarios o vistas L3/L4 por bloque. Si se incorpora a la oferta, registrar asistencia de IA en nivel Alto en la Tabla 4.17 de SD-04.
