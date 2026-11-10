# Registro de diseño de la arquitectura física (sd-04 · 4.2 y 4.3)

Creado: 2026-10-28 · Última actualización: 2026-10-29 · Estado: **borrador completo salvo la sección 9, sin revisión humana** · Uso de IA: alto.

## 0. Control

**Qué es.** Registro de nuestras decisiones de diseño y desarrollo de la arquitectura física. Aquí se diseña; la redacción final vive en el `.tex` (`02_Propuesta/latex_final/sd-04/OnlySimpleSolutions-Subdocumento4.tex`, secciones 4.2 y 4.3).

**Qué NO es.** No coordina los demás subdocumentos (eso lo cubre `80_Artefactos/contexto-activo/`, PR #10). La única excepción es la sección 9 (mapeo lógica ↔ física), que sí servirá para verificar consistencia con otros documentos.

**Reglas rectoras.**
1. Los IDs y siglas del inventario integral y sus derivados son **solo para uso interno de Claude** (trazabilidad). No se usan como nombre en el texto final ni en los diagramas.
2. En texto y diagramas se usan **equivalentes breves que se explican solos**, legibles para quien no es informático. Cada equivalente se registra en [08_glosario-de-equivalentes.md](08_glosario-de-equivalentes.md) antes de usarse.
3. Lo que no viene de las Bases, del Caso o de una decisión del usuario se marca **supuesto**. Nada se inventa.
4. Las **cifras** de costo y las partidas van solo en `07_costos-interno.md` y no se declaran en el sd-04. El **argumento de costo, en palabras y sin cifras**, sí va en el sd-04, porque el Art. 16.2 lo exige (decidido 2026-10-28).
5. Ningún archivo de esta carpeta asigna el estado «revisado»; lo asigna una persona.

**Cómo se responde el Art. 16.2 (aprobado por el usuario el 28-10).** Dos mecanismos: (A) la tabla de nodos de `01_nodos.md` lleva una columna por cada una de las seis preguntas, de modo que una respuesta faltante se ve; (B) las decisiones grandes de emplazamiento tienen además una ficha corta con la pregunta, las alternativas y el criterio de elección (sección 3). No se agrega ninguna regla al harness (`AGENTS.md` u otros).

**Estados.** `confirmado` (Bases, Caso o decisión expresa del usuario) · `propuesto` (diseño nuestro, sin confirmar) · `supuesto` (hecho que no está en las Bases) · `pendiente` (falta dato o decisión).

**Fuentes (de más a menos vigente).**

| Ref. | Fuente | Uso |
| :--- | :--- | :--- |
| F1 | `00_Bases/` (Art. 16 y 17 Bases Administrativas, Comunicado 10 sec. 4.2 y 4.3, Caso 09) | Exigencias; mandan sobre todo lo demás |
| F2 | `.tex` del sd-04, secciones 4.2 y 4.3 | Redacción actual (borrador) |
| F3 | `80_Artefactos/sd-04_contexto/inventario-fisico-integral-2026-10-23.md` y `cierre-inventario/` | Contenido técnico (cantidades, zonas, conexiones). No sus nombres |
| F4 | `80_Artefactos/sd-04_contexto/revision-fisica-2026-10-22/` | Cobertura lógica → física, matriz de despliegue, rutas y puertos |
| F5 | `80_Artefactos/sd-04_contexto/reredaccion-sd04-2026-10-23/decisiones-y-pendientes-sd04.md` y `fisica-general-zonas-2026-10-23/decisiones-2026-10-23.md` | Decisiones del usuario y pendientes heredados |
| F6 | `04_Adjuntos/diagramas/diag-04-43_*` (figura vertical) y `diag-04-42_*` (red de tienda, prueba) | Figuras de trabajo |

**Bitácora.**

| Fecha | Cambio |
| :--- | :--- |
| 2026-10-29 | Se leen 4.2.6 a 4.3.2; se completan 01 a 05; se resuelven 8 discrepancias heredadas (H-06 a H-17); se adoptan supuestos S-01 a S-18 en 06 | 
| 2026-10-28 | Se crea la carpeta, este esqueleto y el glosario de equivalentes. Se leyeron F2 (4.2 hasta 4.2.5), F5 y las cabeceras de F3 y F4. Falta leer 4.2.6 a 4.3.2 y las fichas de `cierre-inventario/`. |

## 1. Qué debe responder el sd-04 (matriz de cumplimiento)

Origen: Comunicado 10 sec. 4.2 y 4.3, T-7 sd-4 y Art. 16 de las Bases Administrativas. «Redactado» significa que el `.tex` tiene texto sobre el punto, no que esté correcto.

| N.º | Debe responder | Dónde en el `.tex` | Estado de la redacción | Dónde se diseña aquí |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Emplazamiento de cada componente en nube u on-premise, con justificación por componente según los seis criterios del Art. 16.2 (latencia, criticidad, volumen, regulación, conectividad, costo total) | 4.2 intro, 4.2.2 (Tablas 4.14 y 4.15) | Redactado; 4.14 ubica por familia, **no justifica por los seis criterios** (por verificar) | `01_nodos.md` |
| 2 | Todos los servicios contratados en nube | 4.2.3 (Tabla 4.16) | Redactado por familia | `01_nodos.md` |
| 3 | Despliegue: cinco ambientes, redes, alta disponibilidad, recuperación ante desastres, respaldos | 4.2.4 redes, 4.2.5 ambientes, 4.2.6 | Redactado (leído 29-10) | `03_ambientes.md`, `04_continuidad.md`, `02_conexiones.md` |
| 4 | Conexiones, puntos de falla y contingencia de cada uno | 4.2.6 | Redactado (leído 29-10) | `02_conexiones.md`, `04_continuidad.md` |
| 5 | Dimensionamiento y plan de capacidad con supuestos de volumen, concurrencia y crecimiento | 4.2.8 | Redactado (leído 29-10) | `05_capacidad.md` |
| 6 | Implementos a proveer (hardware y software), resumen; detalle en T-11 | 4.2.1 (Tablas 4.13 y 4.22) | Redactado | `01_nodos.md` |
| 7 | Mapeo 100 % con la arquitectura lógica (tabla sugerida: esquema 3.3 ↔ lógica 4.1 ↔ física 4.2) | 4.2.7 | Redactado (leído 29-10) | sec. 9 de este archivo |
| 8 | Data center primario y secundario: proveedor, región, zonas, servicios, sitio on-premise; réplica, RPO, RTO, conmutación | 4.3.1, 4.3.2, 4.3.2.1, 4.3.2.2 | Redactado (leído 29-10) | `04_continuidad.md` |

Condiciones del Art. 16 que el diseño debe cumplir (se verifican en la sec. 2 y en `04_continuidad.md`): ver sec. 2.

## 2. Restricciones y principios

| N.º | Restricción | Fuente | Estado |
| :--- | :--- | :--- | :--- |
| R1 | Híbrido obligatorio: carga principal en nube pública y componentes on-premise; no solo-nube ni solo-on-premise | Art. 16.1 | confirmado |
| R2 | Justificar el emplazamiento componente por componente; una asignación no justificada es «observación grave» | Art. 16.2 | confirmado |
| R3 | Declarar región primaria y secundaria | Art. 16.3 | confirmado (Chile Central y Brazil South, decisión del usuario 23-10) |
| R4 | Multi-zona de disponibilidad en todo lo que requiera alta disponibilidad; una sola zona no se acepta | Art. 16.3 | confirmado |
| R5 | Infraestructura como código completa, sin recursos creados a mano en consola | Art. 16.3 | confirmado |
| R6 | Subredes privadas para aplicación y datos; exposición pública solo en el borde | Art. 16.3 | confirmado |
| R7 | Preferir servicios administrados, con justificación | Art. 16.3 | confirmado |
| R8 | Gestión de costos en nube (etiquetado, presupuestos, alertas, reporte mensual) | Art. 16.3 | confirmado |
| R9 | Declarar qué componentes son portables y cuáles no (reversibilidad y bloqueo por proveedor) | Art. 16.3 | confirmado |
| R10 | On-premise: operar degradado sin enlace con la nube **al menos 24 horas continuas** (las Bases del caso pueden exigir más) | Art. 16.4 | confirmado el mínimo; valor del caso por verificar |
| R11 | On-premise: sincronizar y reconciliar después lo hecho sin conexión, con resolución determinista de conflictos y bitácora | Art. 16.4 | confirmado |
| R12 | On-premise: equipos críticos redundantes y discos que toleren la falla de al menos uno, declarando el nivel RAID | Art. 16.4 | confirmado |
| R13 | On-premise: endurecimiento CIS, parches centralizados, control de acceso físico y lógico | Art. 16.4 | confirmado |
| R14 | On-premise: monitoreo integrado con el de la nube, sin puntos ciegos | Art. 16.4 | confirmado |
| R15 | Enlace redundante entre on-premise y nube, con caminos y proveedores distintos y conmutación automática | Bases Administrativas, cap. 4 (línea 440) | confirmado |
| R16 | Línea roja: Retail y Filial emisora son dos negocios con dos regímenes jurídicos; no se mezclan sus datos | AGENTS.md, Caso 09 | confirmado |
| R17 | RPO ≤ 15 min y RTO ≤ 4 h en servicios críticos (RT-07.04) | `.tex` 4.2 | confirmado; «sujeto a ensayo» |
| R18 | La sala DC-02 está en la misma comuna que DC-01, por lo que no sirve como sitio de recuperación | Caso 09, cap. 6, p. 14; `.tex` 4.2 | confirmado |

## 3. Registro de decisiones físicas

Decisiones heredadas. Origen: F5. «Usuario» significa decisión expresa del usuario. «Claude (sin confirmar)» significa una decisión que se tomó sin confirmación y que el usuario debe aceptar o revertir.

| ID interno | Decisión | Origen | Estado |
| :--- | :--- | :--- | :--- |
| D-FIS-01 | El inventario físico v4 es la fuente que se mantiene; si el texto lo contradice, se reescribe el texto | Usuario (D1, 23-10) | confirmado |
| D-FIS-02 | Producción de Retail, Filial y X-01 en Chile Central; recuperación de los tres en Brazil South | Usuario (23-10) | confirmado |
| D-FIS-03 | Los datos de la Filial emisora se recuperan en Brazil South para que queden en infraestructura asegurada contractualmente | Usuario (D2) | confirmado |
| D-FIS-04 | Un router 4G/5G por tienda y por centro de distribución (24) como tercer camino; Only Simple Solutions lo adquiere, el Cliente contrata los planes | Usuario (D3) | confirmado |
| D-FIS-05 | 15 suscripciones de Azure: una por frente (3) y por ambiente (5), sin suscripción compartida | Usuario (D4) | confirmado |
| D-FIS-06 | Cada tienda tiene dos servidores de Retail y dos de la Filial, con redes separadas; X-01 local aislado funciona dentro del par de la Filial (88 servidores en 22 tiendas) | Usuario (corrección del 23-10) | confirmado |
| D-FIS-07 | Las cantidades de la figura física van en una tabla aparte, no en la figura | Usuario (D5) | confirmado |
| D-FIS-08 | Se retiran los porcentajes de capacidad de los ambientes (15, 25, 50 %); el inventario no los fija | Usuario (D8) | confirmado |
| D-FIS-09 | Si el Cliente no aprueba la residencia en Brasil, no se vuelve a DC-02; queda una desviación declarada y el Cliente elige | Claude (P2) | **sin confirmar** |
| D-FIS-10 | La residencia en Brasil se fundamenta para los tres frentes, no solo la Filial | Claude (P3) | **sin confirmar** |
| D-FIS-11 | La alternativa «sitio propio o de tercero en otra ciudad de Chile» se descarta como base y queda como respuesta si no se aprueba Brasil | Claude (P4) | **sin confirmar** |
| D-FIS-12 | La figura general queda solo como plano de consulta | Claude (P5) | **sin confirmar** (pendiente: crear anexo o retirar la mención) |
| D-FIS-13 | Brasil es una réplica resumida en la figura, no se detalla servicio a servicio; la figura se lee de arriba abajo | Usuario (handoff 23-10, decisión 5) | confirmado |
| D-FIS-14 | Reglas de nombres: productos solo por nombre en diagramas y «función (producto)» en la redacción; RPO y RTO con su explicación; «frente» en lugar de «ámbito» (cambiado de «área» el 28-10 por choque con el SD-03) | Usuario (28-10) | confirmado |
| D-FIS-15 | Front Door llega al origen por Private Link. Chile Central no lo admite, así que el punto privado vive en una región admitida. **Versión A+ (confirmada 29-10):** dos orígenes privados en el mismo grupo de orígenes, ambos hacia el Application Gateway de Chile, con regiones de Private Link distintas (Brazil South y otra región admitida de las Américas, por medir), conforme a la recomendación de Microsoft. Sin IP pública en el origen. La alternativa B (origen público cerrado con `AzureFrontDoor.Backend` y `X-Azure-FDID`) queda solo como contingencia manual: no se puede preconfigurar en el mismo grupo, porque Front Door no permite mezclar orígenes públicos y privados. Se agrega Azure DDoS Protection en toda IP pública que quede. Descartados: quitar Front Door (pierde conmutación a Brasil, toca RTO) y borde externo (suma proveedor sin ventaja). Fuentes: documentación de Microsoft consultada 29-10 (06, P-05) | Usuario (29-10) | confirmado |
| D-FIS-16 | Preproducción usa datos anonimizados o seudonimizados de forma verificable (RT-11.25, Ley 21.719); Desarrollo y QA, sintéticos; los de la Filial no se copian. Manda el `.tex` sobre la ficha 07, que decía «sintéticos» | Usuario (29-10) | confirmado |
| D-FIS-17 | Se incluye una **tienda de laboratorio** en Preproducción, con la misma composición que la tienda tipo (4 servidores, 2 árbitros, 2 instancias del Control de cruces, 2 accesos fijos, router 4G/5G), para probar diario local, árbitro y modo sin conexión de 24 h. No cuenta entre las 22 tiendas de Producción ni entre los 88 servidores. Cambio posterior en redacción: sd-04 4.2.3 y Tabla 4.20 (fila «Entrega y ambientes») deben mencionarla; también impacta costos (07) y T-11. Ubicación: sala del Cliente (29-10) | Usuario (29-10) | confirmado |
| D-FIS-18 | Ante la ausencia de respuestas del Cliente en esta etapa (instrucción docente), los huecos se cierran con supuestos explícitos con razón y efecto si fallan (06, S-01 a S-18) | Usuario (29-10) | confirmado |
| D-FIS-19 | **Verificación de disponibilidad contra Microsoft (29-10).** Se revisó cada servicio con la lista de precios oficial por región y Microsoft Learn (06, sección de verificación). Resultado: Sentinel va a Brazil South (S-19), API Center a East US (S-15), Managed HSM con replicación nativa (S-20), copia de Data Lake por Data Factory/AzCopy (S-21); DNS Private Resolver disponible en Chile Central (S-22); CI/CD = Azure Pipelines según el `.tex` (S-04) | Usuario (29-10): aprueba Sentinel en Brazil South, API Center en East US y la corrección del `.tex` | confirmado |

## 9. Mapeo lógica ↔ física

**Para qué sirve.** Es la forma de comprobar, en cada sesión, que lo que dice la arquitectura lógica (qué piezas hay) tiene su lugar en la física (dónde viven) y al revés. Si algo no cuadra, se registra en 9.5 con una acción: agregar, eliminar o modificar, en la lógica o en la física.

**Fuentes de partida.** `revision-fisica-2026-10-22/cobertura-logica-fisica.md` (79 elementos de la figura lógica, ID interno del 22-10) y `matriz-despliegue.md` (13 servicios), contrastados con el `.tex` vigente (4.1.5 a 4.1.10, Tablas 4.3 a 4.9). **Volcado el 29-10.** Las filas con el mismo lugar físico se agrupan; la última columna de cada grupo cuenta sus elementos para comprobar que suman 79.

Abreviaturas solo de esta sección: **C3Z** = Chile Central, repartido en las 3 zonas · **BR** = copia o espera en Brazil South · **T** = cada tienda (22 + la de laboratorio).

### 9.1 Lógico → físico (79 elementos)

| ID interno lógico | Nombre legible | Dónde vive (nodo físico de `01`) | Zona | Estado | Obs. | N.º |
| :--- | :--- | :--- | :--- | :--- | :--- | ---: |
| web, movil | Portal y app de la tienda; consola comercial y de atención | Navegador o app del cliente y PC de atención; interfaz web en el grupo de negocio del Clúster de AKS de Retail, publicada por Application Gateway | C3Z, BR | propuesto | El comercio electrónico de 2019 se supone externo (alojado fuera de nuestro suministro; el Caso no dice dónde reside). Se integra por adaptador y se conserva, remedia o sustituye tras pruebas de la Etapa 1 | 2 |
| portal_f, meson_f | Portal y app de la tarjeta; mesón financiero | Dispositivo del titular o PC del mesón; interfaz web en el grupo de negocio del Clúster de AKS de la Filial | C3Z, BR | propuesto | Red e identidad propias de la Filial | 2 |
| pos, local_serv, local_sync, local_data | Caja y mesón; operación sin enlace; sincronización; diario local | Terminales de caja → Servidores de Retail de la tienda (par activo/espera con árbitro) | T | propuesto | Diario durable y fencing; sincroniza por E-27 | 4 |
| operacion | App interna de tienda | Terminales móviles gestionados, Wi-Fi corporativo, contrato con Retail | T | propuesto | — | 1 |
| logistica | Vista logística | Terminales del centro de distribución y WMS conservado; adaptador de Retail | CD | supuesto | S-29 (06-11): WMS en CD-01 por adaptador; CD-02 con par local propio, sin WMS; hosts e interfaz por acreditar en Etapa 1 | 1 |
| cupo_local | Cupo preautorizado sin enlace | Servidores de la Filial de la tienda (par propio, sin reutilizar el diario de Retail) | T | propuesto | Cerrado por D-FIS-06: va en el par de la Filial, no en VM aparte | 1 |
| dns | DNS público y privado | Azure DNS público (zonas por frente, **nodo agregado 29-10**) y DNS Private Resolver por frente | Global; C3Z, BR | propuesto | S-22 verificado | 1 |
| aks_r | Ejecución aislada por frente | Clústeres de AKS de Retail, Filial y Control de cruces (5 grupos en R y F, 2 en X) | C3Z, BR | propuesto | — | 1 |
| oferta, abastecimiento, existencias, pedidos, ventas, comisiones, market, posventa, clientes | Nueve servicios de Retail (R:M-01 a R:CL-02) | Grupo de negocio del Clúster de AKS de Retail | C3Z, BR | propuesto | Comisiones y marketplace pueden ser módulos; oferta con partición por decidir | 9 |
| originacion, cartera, evidencia | Tres servicios de la Filial (F:C-01 a F:C-03) | Grupo de negocio del Clúster de AKS de la Filial | C3Z, BR | propuesto | — | 3 |
| x01 | Control de cruces | Clúster de AKS del Control de cruces (grupo de negocio) y su copia local en las tiendas | C3Z, BR, T | propuesto | Única ruta Retail → Filial (C7) | 1 |
| regulatorio | Control regulatorio (F:C-04, candidato) | Ninguno: sin despliegue aprobado | — | pendiente explícito | No está en el catálogo vigente de 13 servicios (`.tex` 4.1.5); si se aprueba, iría en el grupo de negocio de la Filial sin equipos nuevos | 1 |
| conteo, training | Conteo cíclico predictivo; entrenamiento | Grupo elástico de modelos predictivos (0 a 3 nodos) del Clúster de Retail, Data Lake de Retail y MLflow | C3Z | propuesto | En BR se enciende tras estabilizar (H-15) | 2 |
| lockers | Lockers Ancoa 24/7 | Controlador y cerraduras en la red IoT de la tienda (**nodo agregado 29-10**); contrato con el servicio de pedidos | T, C3Z | supuesto | S-30 (06-11): Cleveron 355 u equivalente (T-11); API por acreditar en Etapa 2 | 1 |
| busqueda, vector | Búsqueda vectorial multimodal; PostgreSQL con vectores | Servicio de oferta en el grupo de negocio de Retail; base PG-R-VECTOR | C3Z, BR | propuesto | Proyección reconstruible | 2 |
| media | Retail Media Network | Servicio de oferta y adaptador en el grupo de integración de Retail; plataforma publicitaria externa (**nodo agregado 29-10**) | C3Z; externo | supuesto | S-31 (06-11): innovación 4 del SD-13; plataforma de tercero con Criteo de referencia (T-11); contrato antes de la Etapa 2 | 1 |
| fila | Modo Tienda y fila virtual | Servicio de clientes de Retail; tótem en la tienda (**nodo agregado 29-10**) | C3Z, T | propuesto | S-32 (06-11): autonomía sin enlace se prueba en el corte de 24 h del piloto | 1 |
| bus_r, bus_e | Service Bus de Retail y de la Filial | Service Bus Premium de cada negocio; en Brazil South se habilita en la contingencia y se republica desde registros durables (sin geo-replicación) | C3Z, BR | propuesto | Sin puente entre los dos | 2 |
| comercio, canales, socios, proy_r | Adaptadores y trabajadores de Retail | Grupo de integración del Clúster de AKS de Retail | C3Z, BR | propuesto | No se alojan en el Control de cruces | 4 |
| credito, proy_e | Adaptadores y trabajadores de la Filial | Grupo de integración del Clúster de AKS de la Filial | C3Z, BR | propuesto | Interfaces del crédito 2011 por inventariar | 2 |
| datos_merc, historial, datos_venta, datos_clientes | Bases de Retail (mercadería con historial de precios, venta, clientes) | PG-R-MERC, PG-R-VENTA, PG-R-CLIENTES | C3Z, BR | propuesto | Historial de precios dentro de PG-R-MERC | 4 |
| datos_credito | Bases de crédito | PG-F-ORIG, PG-F-CARTERA, PG-F-EVID | C3Z, BR | propuesto | — | 1 |
| bitacora | Bitácora del Control de cruces | PG-X01 | C3Z, BR | propuesto | — | 1 |
| analitica | PostgreSQL analítico | PG-R-MART y PG-F-MART | C3Z, BR | propuesto | PG-R-TECH y PG-F-TECH sirven a MLflow, OpenMetadata y estado técnico | 1 |
| datos_evid, archivo | Evidencia vigente; archivo inmutable | Evidencia y archivo inmutable (Blob, WORM) por frente y clase | C3Z, BR | propuesto | Copia a BR por replicación de objetos (S-21) | 2 |
| lake | Data Lake | Data Lake de Retail y de la Filial | C3Z, BR | propuesto | Copia a BR por Data Factory o AzCopy (S-21) | 1 |
| redis | Memoria rápida de oferta | Memoria rápida (Redis), solo Retail | C3Z, BR | propuesto | Azure Managed Redis Balanced B20, 24 GB (S-26); disponible en Chile Central y Brazil South (buscador, 02-11) | 1 |
| powerbi | Power BI | Servicio Power BI con **capacidad Fabric en Chile Central** (**nodo agregado 29-10**, S-23) y máquinas de apoyo de Power BI por frente | C3Z; global | supuesto | Capacidad en Chile Central por comprobar (S-23, reabierto 02-11); metadatos del tenant quedan en su región de origen | 1 |
| adf | Data Factory | Data Factory por frente (**nodo agregado 29-10**) con nodos de integración en la nube y en casa matriz | C3Z, DC-01 | propuesto | — | 1 |
| metadata, search, mlflow | OpenMetadata, OpenSearch, MLflow | Grupo de estado de cada clúster (OpenSearch y MLflow solo Retail; OpenMetadata uno por negocio) | C3Z, BR | propuesto | Quórum por validar (04) | 3 |
| ext_comercio | ERP/DTE y WMS conservados | Centro de datos de casa matriz y centro de distribución principal (supuesto del `.tex`, Tabla 4.7) | DC-01, CD | pendiente | Hosts por acreditar | 1 |
| ext_canales, ext_socios, ext_credito, ext_comunes | Contrapartes externas | Bloque 6 de `01` | Externo | pendiente | Fuera de nuestros recursos | 4 |
| front_door, application_gateway, api_management, private_link | Borde y puerta de enlace | Azure Front Door, puntos privados (Brazil South y East US), Application Gateway y API Management por negocio | Global; C3Z, BR | propuesto | A+ (D-FIS-15) | 4 |
| api_center | Catálogo de contratos | Azure API Center por negocio en **East US** | East US | propuesto | S-15 aprobado | 1 |
| entrada_privada | Acceso privado corporativo | Firewall de sitio → VPN Gateway por negocio → Azure Firewall | T, CD, DC-01, C3Z | propuesto | Control de cruces sin túnel salvo necesidad | 1 |
| tech_ui, tech_java, tech_spring | Tecnologías de interfaz y servicios | No ocupan nodo: corren dentro de los grupos de cada clúster | — | declarado | No son infraestructura | 3 |
| common_admin, common_flujos, common_docs, common_notif | Capacidades comunes | Grupo de negocio de cada frente | C3Z, BR | pendiente | Productos y proveedores por cerrar | 4 |
| backup | Respaldo | Bóveda de respaldo por frente en Chile (ZRS, **nodo agregado 29-10**) y en Brazil South; recuperación a un punto en el tiempo de cada base | C3Z, BR | propuesto | Sin respaldo geo-redundante en Chile (06) | 1 |
| security_summary | Seguridad | Entra ID, External ID e Intune (globales, **nodos agregados 29-10**), Key Vault, Managed HSM, Bastion, conectores de acceso privado, Defender y Sentinel (Brazil South) | Global; C3Z, BR | propuesto | S-19 aprobado; Bastion Premium con IP pública y zonas, en vista previa (S-27) | 1 |
| observability_summary | Observabilidad | Pila del clúster en el grupo de operación, Log Analytics por frente, sondas de vigilancia | C3Z, BR | propuesto | — | 1 |
| **Total** | | | | | | **79** |

### 9.2 Físico → lógico

| Nodo físico (`01`) | Qué sirve |
| :--- | :--- |
| Servidores de Retail de la tienda, terminales de caja | pos, local_serv, local_sync, local_data |
| Servidores de la Filial de la tienda | cupo_local, mesón local, copia local de x01 |
| Árbitro, UPS, racks, accesos fijos, router 4G/5G, firewalls y switches de tienda | Infraestructura declarada (continuidad y conectividad de la tienda) |
| Copia local cifrada | local_data, cupo_local (respaldo local) |
| Front Door, puntos privados, Application Gateway, API Management, balanceador interno | front_door, private_link, application_gateway, api_management |
| Redes central, de aplicaciones y de datos; Azure Firewall; VPN Gateway | entrada_privada; infraestructura declarada (segmentación por frente) |
| Bastion, conectores de acceso privado | security_summary (acceso administrativo) |
| DNS Private Resolver, Azure DNS público | dns |
| Clústeres de AKS (grupos sistema, negocio, integración, estado, operación) | aks_r y los 13 servicios, adaptadores, trabajadores, capacidades comunes, OpenSearch, MLflow, OpenMetadata, pila de observabilidad |
| Grupo elástico de modelos predictivos | conteo, training |
| Máquinas de apoyo (Power BI, Data Factory, acceso privado) | powerbi, adf, security_summary |
| Sondas de vigilancia | observability_summary |
| 12 bases PostgreSQL | datos_merc, historial, datos_venta, datos_clientes, vector, analitica, datos_credito, bitacora; PG-R-TECH y PG-F-TECH sirven a mlflow y metadata |
| Service Bus Premium ×2 | bus_r, bus_e |
| Redis | redis |
| Data Lake ×2; evidencia y archivo | lake; datos_evid, archivo |
| Key Vault, Managed HSM, Entra ID, Defender, Log Analytics, Sentinel, DDoS Protection | security_summary, observability_summary; DDoS: infraestructura declarada |
| Ambientes DEV, QA, PRE y tienda de laboratorio | Infraestructura declarada (ciclo de entrega, RT-04.02) |
| Container Registry, pipelines, estado de Terraform | Infraestructura declarada (entrega) |
| API Center | api_center |
| Bloque 4 (Brazil South) | Copia de recuperación de todo lo anterior (FL-12) |
| Recinto y redes de casa matriz; nodos de integración de Data Factory | adf; ext_comercio (alojamiento supuesto) |
| Centros de distribución y sus nodos locales | logistica; continuidad del centro |
| Contrapartes externas (bloque 6) | ext_comercio, ext_canales, ext_socios, ext_credito, ext_comunes |

**C2:** todo nodo sirve a un componente o está declarado como infraestructura. Sin hallazgos.

### 9.3 Interfaz lógica → enlace físico

| Interfaz lógica (`.tex` 4.1) | Enlaces (`02`) | Obs. |
| :--- | :--- | :--- |
| Canal público → puerta de enlace → servicio | E-01 a E-08 | A+ (E-03, E-03b) |
| Sitio → entrada privada | E-09 a E-14 | Por negocio (H-06 cerrado) |
| Servicio → su base (autoridad) | E-15, E-24 | Solo su propietario |
| Hecho confirmado → Service Bus del negocio | E-16 | Sin puente entre negocios |
| Cargas → Data Lake, Blob | E-17, E-20 | — |
| Oferta → Redis y vectores; búsqueda y catálogo | E-18, E-19 | — |
| Compra con tarjeta propia (`compra_autorizable`) | E-22, E-23 | Único cruce (C7) |
| Operación sin enlace y sincronización | E-25 a E-31 | — |
| Lockers → pedidos | E-32 | Contrato por cerrar |
| Carga inicial y reconstrucción (Data Factory) | E-37 | — |
| Power BI → PostgreSQL analítico | E-38, E-39 | Capacidad en Chile Central por comprobar (S-23, reabierto 02-11) |
| Adaptadores → plataformas conservadas y terceros | E-40, E-41 | 14 interfaces por inventariar |
| Identidad, administración, salida controlada | E-42 a E-45 | — |
| Observabilidad y detección | E-46 a E-50, E-49b | Sentinel en BR |
| Entrega y contratos | E-51 a E-53b | — |
| Recuperación regional | E-54 a E-59 | — |
| **Fila virtual: tótem → servicio de clientes** | **Ninguno** | **Falta enlace** → H-22 |
| **Retail Media: adaptador → plataforma publicitaria** | Cubierta por E-41 (terceros) | Se nombra en E-41 |

### Resultado de los chequeos (29-10)

| Regla | Resultado |
| :--- | :--- |
| C1 | Cumple tras agregar 8 nodos en `01` (bloque 7 y tienda): DNS público, Data Factory, bóveda de respaldo de Chile, capacidad de Power BI, External ID e Intune, controlador de lockers, tótem, plataforma publicitaria. F:C-04 queda como pendiente declarado |
| C2 | Cumple |
| C3 | Falla en fila virtual (H-22): se agrega E-64 |
| C4 | Los nodos nuevos traen las seis respuestas en `01` |
| C5 | Nodos nuevos con contingencia en su fila; continuidad general sin cambios |
| C6 | Cumple; nuevo S-23 (Power BI) |
| C7 | Cumple: el único cruce es E-22/E-23; los nodos nuevos son por frente |
| C8 | Cifras sin cambio (12 bases, 40/54 VM, 88/44/44); el `.tex` ya dice «árbitros» |
| C9 | Nombres nuevos registrados en 08 |

### 9.4 Reglas de chequeo (se aplican en cada sesión)

| N.º | Regla | Si falla |
| :--- | :--- | :--- |
| C1 | Todo componente lógico tiene al menos un lugar físico, o un pendiente explícito | Registrar en 9.5; decidir si falta algo en la física o sobra algo en la lógica |
| C2 | Todo nodo físico sirve a al menos un componente lógico, o está declarado como infraestructura | Registrar en 9.5; puede sobrar un nodo o faltar un componente lógico |
| C3 | Toda interfaz lógica tiene ruta física | Registrar en 9.5; falta una conexión |
| C4 | Todo emplazamiento trae las seis respuestas del Art. 16.2 en `01_nodos.md` (una columna por pregunta: latencia, criticidad, volumen, regulación, conectividad, costo total). Una celda sin respuesta dice «pendiente» y el motivo; nunca queda vacía ni se rellena con algo inventado. La columna «argumento de costo» va en palabras, sin cifras ni precios, y pasa al sd-04; las cifras y partidas quedan en `07_costos-interno.md` | Completar en `01_nodos.md` |
| C5 | Todo punto de falla trae su contingencia | Completar en `04_continuidad.md` |
| C6 | Todo supuesto está marcado como tal y tiene a quién le toca confirmarlo | Completar en `06_supuestos-pendientes.md` |
| C7 | Retail, Filial y X-01 no comparten nodo ni enlace salvo el cruce autorizado por X-01 | Es la línea roja: corregir antes de seguir |
| C8 | Toda cifra del registro coincide con el `.tex` y con las Bases | Corregir la fuente que corresponda |
| C9 | Todo nombre usado en texto o diagrama está en 08 | Registrar el equivalente antes de usarlo |

### 9.5 Registro de discrepancias

Heredadas de F5 (hallazgos de la revisión de coherencia del 23-10 que quedaron abiertos). Se cierran verificándolas en el `.tex` actual, que cambió con la integración de `main`.

| ID | Hallazgo | Afecta | Acción probable | Estado |
| :--- | :--- | :--- | :--- | :--- |
| H-06 | «Por ámbito» (hoy «por frente») frente a «por negocio»: hay dos Service Bus y dos VPN Gateway, no tres | Física (texto) | Modificar texto | **cerrado** (29-10): túneles y VPN «por negocio» en el `.tex`; «ámbito» reemplazado por «frente» en todo el sd-04 (182 casos) |
| H-07 | La recuperación de los mensajes de Service Bus se remite a 4.3.2 y allí no se define | Física | Decidir entre reconstruir desde el registro de salida de cada propietario o un mecanismo geográfico condicionado | **cerrado**: 4.3.2 ya define la recuperación por registros durables de productores y consumidores |
| H-08 | X-01 tiene pila de observabilidad completa en la lógica pero solo 6 nodos y ninguna máquina auxiliar | Lógica o física | Aclarar dónde corre su telemetría | **cerrado**: `.tex` 4.3.1 declara que la observabilidad de X-01 corre dentro de su clúster, sin máquinas auxiliares |
| H-09 | La instancia local de X-01 en tienda (44 instancias) no tiene antecedente en 4.1 | Lógica | Explicarla en la continuidad local | **cerrado en el registro** (E-29 a E-31 y 04); la redacción de 4.2.6 debe explicar la copia local |
| H-10 | API Management en Brasil se describe con dos modelos distintos | Física (texto) | Elegir uno y unificar | **cerrado**: una instancia multirregión con gateway en cada región (Tabla 4.20 y 4.1) |
| H-12 | OpenSearch y OpenMetadata «de Retail y de la Filial» contradicen que la Filial no tiene búsqueda global | Lógica o física | Aclarar | **cerrado**: `.tex` 4.1.1 aclara que la Filial no tiene búsqueda global; corregida la fila de 01_nodos |
| H-15 | El grupo elástico de 0 a 3 nodos de Retail no entra en las cifras de 40 y 54 ni se replica en Brasil | Física | Declararlo | **cerrado en el registro**: el grupo elástico no entra en 40/54 y en Brasil se enciende solo tras estabilizar; la redacción debe declararlo |
| H-16 | 4.2.1 cita figuras de DC-01 y de los CD antes que su sección y describe dos veces el recinto | Física (texto) | Remitir a 4.3.1 o quitar duplicación | abierto (solo redacción; no verificado en esta ronda) |
| H-17 | Application Gateway se llama «puerta privada» pero el recorrido privado no pasa por él | Física | Corregir descripción o recorrido | **reabierto y corregido (06-11)**: E-04 es el recorrido público. El privado entra por VPN Gateway y Azure Firewall directo a API Management (`.tex` 4.1.4). El texto no debe llamar a Application Gateway «puerta privada» |
| H-18 | El `.tex` (Tabla 4.12, 4.2 y 4.3, Tabla de observabilidad) presenta Sentinel por frente sin región; Chile Central **no admite** Sentinel | Física (texto) y residencia (4.3.2.1) | Declarar Sentinel en Brazil South con solo tablas de seguridad y agregarlo a la residencia y transferencia de 4.3.2.1 (hoy Brasil solo se usa en contingencia) | **cerrado** (29-10): `.tex` corregido en Tablas 4.12 y de observabilidad, 4.2.6 y 4.3.2.1 |
| H-19 | El `.tex` nombra API Center (Tablas 4.12 y de servicios, 4.2.5) sin región; no existe en Chile Central ni Brazil South | Física (texto) | Declarar API Center en East US con solo metadatos de contratos | **cerrado** (29-10): `.tex` corregido en Tablas 4.12 y de la puerta, y su explicación |
| H-20 | El `.tex` (4.3.2) dice que tras promover la réplica de PostgreSQL en Brasil «se habilita su alta disponibilidad»; Microsoft bloquea hoy la alta disponibilidad entre zonas de nuevos servidores en Brazil South | Física (continuidad) | Precisar «alta disponibilidad en la misma zona mientras dure el bloqueo» o verificar antes de la construcción | **cerrado** (29-10): `.tex` 4.3.2 precisa la alta disponibilidad en una zona |
| H-21 | El registro (S-04) suponía GitHub Actions; el `.tex` dice Azure Pipelines | Registro | Corregido en el registro: manda el `.tex` | **cerrado** (29-10) |
| H-22 | La fila virtual (tótem en tienda → servicio de clientes de Retail) no tenía nodo ni enlace físico | Física | Agregar tótem (01) y E-64 | **cerrado** (29-10) |
| H-23 | Ocho componentes lógicos sin nodo propio en `01` (DNS público, Data Factory, bóveda de Chile, Power BI, External ID, Intune, lockers, plataforma publicitaria) | Física | Agregar filas | **cerrado** (29-10) |
| H-24 | Power BI guarda sus modelos en la región de origen del tenant, que no se ha fijado | Física y residencia | Capacidad Fabric en Chile Central (S-23); metadatos del tenant en su región de origen; agregar a 4.3.2.1 del `.tex` | **reabierto** (02-11): Learn marca Chile Central como «Power BI only region» y la capacidad no está comprobada; el `.tex` 4.3.2.1 ya lo declara como supuesto con su alternativa (S-23) |
| H-25 | E-58 y 04 dicen que los sitios reconectan al VPN Gateway de Brazil South, pero `01` no lo tenía | Física | Agregar VPN Gateway ×2 en Brazil South | **cerrado** (29-10, detectado al armar el N3) |

## 10. Diagramas

| Figura | Pregunta que responde | Nivel de detalle | Estado |
| :--- | :--- | :--- | :--- |
| `diag-04-43_fisica-arquitectura-vertical` | ¿Por dónde viaja una venta con tarjeta y qué la protege en cada tramo? | Resumen por servicio (≈ N2) más tabla de encapsulación | Borrador vigente, sin revisión humana |
| `diag-04-42_red-tienda-bifurcaciones-prueba` | ¿Cómo es la red de una tienda tipo? | Equipos de una tienda | De prueba |
| **Diagrama N3** (6 hojas, 29-10) | ¿Qué recursos individuales componen la solución y dónde está cada uno? | **N3** dividido por el máximo de 30 cajas de la skill: hoja 0 conjunto (F1), 1 tienda tipo, 2a Chile red y cómputo, 2b Chile datos y operación, 3 Brazil South, 4 casa matriz y centros (F5). Líneas con su E-NN. Fuente `diagramas-n3/generar_specs.py` → JSON validados → `.drawio` y `.png` en `diagramas-n3/salida/` | Generado y validado; falta ordenar a mano en draw.io las líneas que cruzan cajas |
| **Diagrama atómico gigante** (1 lámina, 29-10) | ¿Cómo se ve todo junto: recursos físicos, clústeres abiertos en sus grupos de nodos y lógica (capas, 13 servicios con código, 5 innovaciones, autoridad de datos, 14 interfaces)? | 226 cajas y 122 líneas con su E-NN (se dibujan solo las conexiones que apoyan el análisis; las 62 omitidas y su motivo están en `diagramas-n3/gigante/lineas-omitidas.md`), en un solo lienzo de ≈4.400 × 3.400 px, con el plano de control de AKS como barra vertical a la izquierda de cada clúster (logo centrado, texto girado; las líneas azules con codos de 90° salen del texto hacia cada grupo de nodos) y las cajas de servicio giradas 90° (de pie, texto vertical) en fila dentro de cada grupo: franja de borde arriba, Chile Central en tres columnas por frente y Brazil South debajo alineado frente a frente (réplicas en vertical). Excepción expresa al catálogo de la skill (usuario, 29-10). Fuente `diagramas-n3/gigante/generar_gigante.py`; salida `.drawio`, `.png` y `.pdf` vectorial | Generado y ordenado (29-10); quedan cruces con saltos que se afinan a mano en draw.io; sin revisión humana |
| **Diagrama atómico gigante, versión solo física** (1 lámina, 29-10) | ¿Cómo se ven todos los recursos físicos y sus conexiones críticas, sin mezclar lógica? | 196 cajas y 107 líneas con su E-NN (una línea por bloque del clúster a «Mensajería y datos» y a «Seguridad, respaldo y operación», y una por bloque en las réplicas a Brasil), ≈3.800 × 2.800 px. Sin servicios de negocio, innovaciones ni capas lógicas: cada clúster de AKS muestra su plano de control y sus grupos de nodos. Carpeta aparte `diagramas-n3/gigante-fisico/` (`.drawio`, `.png`, `.pdf`, `generar_gigante_fisico.py`, `lineas-omitidas.md`) | Generado en la primera ronda del loop; se afina cada 30 min; sin revisión humana |
| **Prueba de trazado con ELK** (Chile Central, 29-10) | ¿Un motor de disposición mejora la legibilidad frente al trazado de draw.io? | Prototipo en `diagramas-n3/elk-prueba/` (`elk_prueba.py`, `layout.js`, `chile-elk.drawio/.png/.pdf`): ELK ordena cada contenedor y traza las líneas con codos de 90° que esquivan cajas; solo Chile Central y solo líneas internas de cada frente | Prueba; no reemplaza a `gigante-fisico/` hasta que se apruebe |

Regla del diagrama grande: la tienda se dibuja una vez como patrón repetido 22 veces; los pods y contenedores no se dibujan; un grupo de servidores se dibuja como una caja con «× N máquinas».

## 13. Salida a redacción

Qué parte del registro alimenta cada subsección del `.tex`. «Copia» = pasa casi igual; «resume» = se condensa; «interno» = no sale del registro.

| Archivo del registro | Subsección del `.tex` | Tratamiento |
| :--- | :--- | :--- |
| `01_nodos.md` | 4.2 (intro), 4.2.1, 4.2.2, 4.2.3 | Resume; los IDs internos no salen |
| `02_conexiones.md` | 4.2.4, 4.2.6 | Resume; puertos y protocolos solo donde el lector los necesite |
| `03_ambientes.md` | 4.2.5 | Resume |
| `04_continuidad.md` | 4.2.6, 4.3.2 | Resume |
| `05_capacidad.md` | 4.2.8 | Copia el cálculo y sus supuestos |
| sec. 9 (mapeo) | 4.2.7 | Resume en la tabla de mapeo |
| `07_costos-interno.md` | ninguna (solo el argumento de costo en palabras pasa a 4.2.2 y 4.3) | Interno |
| `06_supuestos-pendientes.md` | 4.2.2 y notas de pendiente | Los supuestos van declarados en el texto |
