# Plan de trabajo por agentes para cerrar el inventario físico

**Fecha:** 23-10-2026 · **Estado:** ocho encargos ejecutados; H-01/H-02 resueltos en diseño; figura 4.52 exportada · **Uso de IA:** Alto. Las fichas A–H están en [`cierre-inventario/`](cierre-inventario/); la revisión H registra 14 hallazgos y distingue decisiones resueltas de pruebas pendientes.

## Decisiones de partida

1. Retail y Filial producen en Chile Central y se recuperan en Brazil South.
2. Retail, Filial y el cruce X-01 mantienen redes, datos, identidades y permisos separados. Solo X-01 procesa la compra autorizable entre negocios.
3. Decisión final de tienda: **dos hosts Retail y dos hosts Filial** (cuatro por tienda), con redes y administración separadas. La decisión inicial de un host por negocio fue reemplazada para cumplir RT-03.14. X-01 local se ejecuta aislado dentro del par Filial, con identidad, permisos y bitácora propios; solo entrega el resultado mínimo autorizado a Retail durante la desconexión.
4. La operación financiera nueva vive en la nube. En el DC quedan sistemas externos/conservados necesarios para convivencia y los conjuntos de datos cuya custodia local sea obligatoria. La obligación y el conjunto exacto deben acreditarse; no se inferirán por la mera existencia del DC.
5. La nube sigue siendo la carga principal y los componentes locales deben cumplir el Art. 16 de las Bases Administrativas y RT-03 del documento transversal. El caso exige separación auditable de negocios y continuidad de venta ante caída de enlace.

## Método común para todos los encargos

Cada agente recibe una zona y trabaja en **su propio archivo** dentro de `80_Artefactos/sd-04_contexto/cierre-inventario/`, sin editar en paralelo el inventario maestro, el diagrama ni el `.tex`. Entrega una tabla con: ID, sitio, zona/subred, ámbito, ambiente, clase (host, VM, contenedor, PaaS, equipo o configuración), función, cantidad, capacidad, HA, conexiones de entrada/salida, datos, backup/DR, fuente y estado. Añade una matriz de decisiones con alternativa evaluada, elección, razón, supuestos y comprobación pendiente. Debe clasificar cada fila como **decidido por usuario**, **derivado de Bases**, **decisión técnica del agente sustentada**, **sujeto a validación de producto/capacidad**, o **dato del mandante por levantar**.

Para el dimensionamiento, cada agente debe mostrar carga de entrada, fórmula, crecimiento y margen, cuello de botella y ajuste por prueba. Si la volumetría no existe, elige una capacidad inicial defendible para la oferta y declara el supuesto; no la presenta como medición. Para redes, propone CIDR sin solapamiento, subredes/VLAN, rutas y reglas por flujo, y revisa retorno y redundancia. Cita fuentes primarias de producto para SKU y limitaciones; contrasta el contenido contractual con `00_Bases/`. Las propuestas técnicas podrán pasar a «decidido para el diseño» tras revisión cruzada; la configuración final y los datos que solo posee el mandante siguen identificados como validación de implementación.

El coordinador integra resultados, resuelve choques de nombres/recursos y comprueba que las cantidades de VM, pods y PaaS no se sumen dos veces. Solo él actualiza el inventario maestro y, después de cerrarlo, rehace los diagramas bajo la guía `diagramas-ancoa`.

## Distribución y orden de ejecución

El orden permite hasta **tres agentes especialistas en paralelo más un coordinador**. La segunda ronda utiliza las interfaces fijadas por la primera. Los nombres A–H son encargos, no nombres de personas ni chats creados.

| Ronda / agente | Encargo y decisiones que debe cerrar | Entregable específico | Depende de |
| --- | --- | --- | --- |
| 1 · A — Carga y AKS | Volumetría Retail/Filial/X, tamaño y número inicial de nodos por pool, réplicas/pods, requests/limits, autoscaling, AZ, PV y VM auxiliares BI/IR/PA. Mapear cada servicio y herramienta al pool sin contar un pod como VM. | `01-computo-aks.md`: tabla por clúster/pool/carga, cálculo y umbrales de escalado. | Bases, requisitos, matriz de despliegue y diagrama lógico. |
| 1 · B — Red cloud | Suscripciones/VNet, subredes R/F/X, CIDR, VPN, firewall, DNS, Private Endpoints, entrada Front Door→App Gateway→APIM/ILB y salida. Fijar WAF, NSG, UDR, certificados, puertos y tablas de flujo. | `02-red-cloud.md`: plan IP, matriz origen/destino, segmentación y rutas de producción/DR. | Inventario de conexiones y restricciones de producto. |
| 1 · C — Tienda | Diseñar dos hosts Retail y dos Filial por tienda, con red/VLAN y administración separadas. Distribuir servicios locales, VM o contenedores, diario de venta, cupo autorizado, discos, RAID, respaldo, UPS, seguridad y sincronización. Resolver continuidad durante caída de enlace y falla de host con cuatro hosts explícitos por decisión final del usuario. | `03-tienda.md`: ficha SIT tipo, dibujo lógico de procesos por host, estados de operación, prueba de desconexión, prevención de doble venta/cupo. | Caso, RT-03, inventario y decisión del usuario. |
| 2 · D — Datos y custodia | Dimensionar 12 PostgreSQL, Service Bus, Redis, Blob/ADLS, índices, archivo y telemetría; separar bases/roles, PE y claves. Identificar **con cita exacta** los conjuntos que deban conservarse en DC y distinguir custodia local de operación financiera cloud. Si la fuente no obliga una copia local concreta, registrar decisión de diseño pendiente de política, sin inventar mandato legal. | `04-datos-custodia.md`: inventario de recursos y datasets, cálculos de tamaño/IOPS/retención, matriz de custodia y flujo Chile↔Brasil/DC. | Resultados A–C y fuentes contractuales/regulatorias aplicables. |
| 2 · E — DC, CD y externos | Levantar en documentos los roles de DC-01/DC-02, CD-01/CD-02, ERP/DTE, WMS, crédito 2011 de convivencia, gateways locales y contrapartes. Definir qué sigue, qué se migra y qué se apaga. Separar «sistema externo» de host on-premise real; no atribuir ubicación sin evidencia. | `05-dc-cd-externos.md`: ficha por sitio/sistema, contratos y dependencias, mapa de convivencia/migración, lista de datos que solo mandante puede acreditar. | B y C; coordinación con D para custodia. |
| 2 · F — Seguridad y operación | Cerrar identidades, Key Vault/HSM, Bastion, PA, Defender, Sentinel, telemetría, sondas, backup, agentes, roles, retenciones y administración de X. Definir despliegue de controles en Chile, Brasil y locales, sin compartir privilegios R/F. | `06-seguridad-operacion.md`: matriz de controles por recurso, identidad, flujo administrativo y observabilidad. | A–C; coordinar nombres de recursos con D. |
| 3 · G — Recuperación y entrega | A partir de la pila cerrada, definir capacidad y modo de DR R/F/X en Brazil South, replicación por producto, secuencia de conmutación, RTO/RPO verificables y retorno. Dimensionar DEV/QA/PRE, ACR, agentes, Terraform/estado y dependencias de despliegue. | `07-dr-ambientes.md`: recursos Brasil y ambientes inferiores, runbooks, pruebas y conteos separados de producción. | A–F. |
| 3 · H — Revisión independiente | Revisar de punta a punta separación R/F, cobertura lógica→física, Art. 16, RT-03/06/11/14, redundancia, datos locales, cifras y conexiones. Señalar contradicciones con evidencia y proponer corrección concreta. | `08-revision-cruzada.md`: observaciones clasificadas, evidencia, resolución y veredicto de inventario listo para dibujar. | A–G y primera integración del coordinador. |

El coordinador puede continuar integrando mientras trabajan A–C y D–F; no modifica sus archivos de entrega. Para evitar decisiones incompatibles, A fija IDs de cargas y B fija IDs de red al fin de la ronda 1; D–F los reutilizan. G trabaja sobre la primera versión integrada, H sobre la segunda. Si se ejecuta con el límite de concurrencia de esta sesión, las rondas tienen tres especialistas simultáneos y el coordinador permanece como cuarto agente.

## Preguntas de arquitectura que el trabajo debe resolver

| Tema | Decisión esperada del especialista | Criterio de aceptación |
| --- | --- | --- |
| Dos hosts por negocio en tienda | Procesos y datos propios por par R/F, OS/virtualización, discos, copias, claves, HA y operación sin enlace. | Cuatro hosts explícitos; conmutación y autonomía requeridas probadas sin mezcla de datos. |
| Custodia en DC | Dataset, autoridad, obligación citada, formato, medio, cifrado, acceso, retención y copia/recuperación. | Ninguna base financiera de producción se traslada al DC por inercia. |
| Crédito 2011 | Ubicación real, rol durante migración, conciliación y fecha/criterio de apagado. | Se distingue sistema conservado de pila nueva cloud. |
| AKS | Cargas por pool, nodos/VM, réplicas/pods, límites y escalado. | Sumas reproducibles y falla de AZ considerada. |
| Red | Segmentos R/F/X por sitio y región, enlaces y puertos necesarios. | No hay ruta R→datos F; X-01 tiene único contrato mínimo. |
| DR | Pila recuperable de ambos negocios, X-01 y claves en Brasil. | Runbook y prueba funcional, incluidos datos y acceso administrativo. |
| Seguridad | Controles en cada región y sitio con dueños claros. | El dispositivo corporativo no concede acceso privilegiado sin identidad/PIM. |
| Terceros | Contrato, endpoint, sentido del tráfico y dueño por interfaz. | Las 14 interfaces actuales no se sustituyen por una flecha genérica sin ficha. |

## Cierre del inventario y nueva diagramación

El coordinador acepta una entrega cuando sus tablas tienen IDs sin duplicados, fuente verificable, cantidades consistentes y cada conexión referencia extremos existentes. Los desacuerdos entre especialistas se resuelven en un registro de decisiones antes de marcar una fila como decidida. Las fuentes del mandante que falten se enumeran con responsable y efecto; no detienen las decisiones técnicas que puedan tomarse con supuestos explícitos.

El resultado integrado será una nueva versión de [`inventario-fisico-integral-2026-10-23.md`](inventario-fisico-integral-2026-10-23.md) y una matriz única de recursos/conexiones. Después se redibuja la general por zonas, se valida su JSON y se revisa el editable con iconos y nombres. Por límite de legibilidad, los nodos y flujos completos se distribuyen en vistas F1/F2/F3/F5 por zona; la general contiene referencias estables a esas vistas. No se asigna estado «revisado» sin la revisión humana registrada que exige el proyecto.

**Fuentes de control:** `00_Bases/Bases_Administrativas.md`, Art. 16; `00_Bases/Bases_Transversales.md`, RT-03, capítulo 6, RT-11 y RT-14; `00_Bases/Caso_09_Cadena_Multitienda.md`, capítulos 4–6 y exigencia de separación; [inventario físico actual](inventario-fisico-integral-2026-10-23.md); [diagrama lógico explicado](explicacion-diagrama-columnas-2026-10-23/README.md); [matriz de despliegue](revision-fisica-2026-10-22/matriz-despliegue.md); [rutas](revision-fisica-2026-10-22/rutas-puertos-y-segmentos.md). La frase del usuario sobre «datos obligatorios en DC» requiere precisar la obligación concreta en el trabajo D; el Caso 09 consultado describe separación y conservación de evidencia, pero no proporciona aquí una lista cerrada de datasets financieros que deban residir físicamente en DC.
