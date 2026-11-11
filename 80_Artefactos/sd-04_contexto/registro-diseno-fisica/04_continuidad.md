# 04 · Continuidad

**Última actualización:** 2026-10-29. **Fuentes:** `.tex` 4.2.6, 4.3, 4.3.2 y Tablas 4.23 y 4.24; `cierre-inventario/07-dr-ambientes.md`; RT-07.01 a RT-07.12, RT-03.10, RT-03.17. D-FIS-15 aplicado. Las cifras de tiempo por componente que no están en las fuentes quedan como «por definir», no se inventan.

## Objetivos y modalidad
- **RTO ≤ 4 h y RPO ≤ 15 min** para servicios críticos (RT-07.04). Disponibilidad mensual 99,9 % de extremo a extremo (RT-10.01). Son máximos contractuales que se aceptan solo si el ensayo los demuestra.
- **Activo-pasivo templado** (RT-07.01): Brazil South tiene todo encendido y probado, pero la escritura de negocio y la publicación a clientes siguen en Chile hasta la conmutación. Se descarta activo-activo porque el RTO lo permite, porque cada registro tiene una sola autoridad y porque escribir en dos regiones exige resolver conflictos.
- **Conmutación y retorno se ensayan al menos dos veces al año** (RT-07.07), con informe y medición de RTO y RPO. Se agregan un ensayo de Brasil sin Chile durante un evento digital y otro con un enlace de tienda caído.

## Niveles de falla
| Nivel | Qué ocurre | Respuesta |
| :--- | :--- | :--- |
| Un pod | El proceso se cae | Kubernetes lo reinicia; mínimo 3 réplicas por servicio |
| Un nodo | Una VM del clúster falla | AKS la reemplaza; los pods se reprograman |
| Una zona de Chile Central | Se pierde 1 de 3 zonas | Los dos tercios restantes absorben la carga (por eso se dimensiona con 2/3); PostgreSQL pasa a su espera en otra zona; sin pérdida de datos |
| La región Chile Central | Se pierde la producción | Conmutación a Brazil South (procedimiento de 7 etapas abajo); las tiendas venden con sus pares locales |
| Un enlace de sitio | Falla un acceso fijo | Pasa al otro acceso; el router 4G/5G es el tercer camino |
| Un sitio entero | Cae una tienda o un centro | Diario local durante 24 h; reconexión y conciliación |

## Puntos de falla por nodo

Cada fila: qué pasa y qué lo contiene. «Por definir» significa que ni las fichas ni el `.tex` fijan un tiempo.

### Tienda
| Nodo | Si falla | Contención |
| :--- | :--- | :--- |
| Servidor activo de Retail o Filial | Falla uno de los dos de un par | Pasa el servidor de espera; el árbitro de la tienda evita que ambos escriban a la vez (fencing) |
| Árbitro de los servidores | Pierde el quórum | Uno por par; si se pierde, se decide con una regla de seguridad que evita doble escritura (el producto del árbitro está sin definir, P-04) |
| Copia local del Control de cruces | Se pierde la instancia | Está dentro de los servidores de la Filial; sigue la suerte del par |
| Un acceso fijo | Un operador cae | El otro acceso fijo lleva el tráfico (≥10 Mbps); si fallan ambos, router 4G/5G (≥5 Mbps) |
| Los tres caminos | Tienda sin enlace | Vende hasta **24 h** con oferta vigente, existencia local, registro durable y sincronización al volver (RT-03.10) |
| UPS | Falla una rama | Dos ramas A y B; la pérdida de una no apaga los equipos |
| Disco de un servidor | Falla un disco | Cada servidor tolera la falla de un disco |
| Borrado o corrupción | Dato dañado | Copia local cifrada, separada de la réplica |

### Nube en Chile Central
| Nodo | Si falla | Contención |
| :--- | :--- | :--- |
| Front Door | Sin entrada pública | Servicio global; por definir su comportamiento ante falla propia |
| Punto privado de Front Door en Brazil South (D-FIS-15) | Si el clúster regional de Front Door en Brazil South no responde, la entrada de Chile se corta aunque Chile esté sano | A+ (D-FIS-15): segundo origen privado con otra región de Private Link en el mismo grupo de orígenes (recomendación de Microsoft); ver 06, P-05 |
| Application Gateway | Un negocio sin entrada | Uno por negocio; la otra no se ve afectada. Redundante entre zonas (Microsoft lo admite en todas las regiones con zonas; verificado 29-10, S-08) |
| API Management | Un negocio sin control de APIs | Instancia multirregión por negocio; gateway regional en Brasil como respaldo |
| Nodos de AKS (por grupo) | Se cae un nodo o una zona | Tres nodos por grupo, uno por zona; base calculada para perder una zona |
| Grupo de estado (OpenSearch, MLflow, OpenMetadata) | Pierde el quórum | Con 3 nodos no se afirma alta disponibilidad real; búsqueda y catálogo pueden degradar sin bloquear caja; volumen persistente y quórum por validar |
| PostgreSQL (cada servidor) | Falla el primario | Espera en otra zona; réplica asíncrona en Brasil |
| Service Bus | Se corta | Premium zonal; los productores conservan registros durables para republicar |
| Redis | Se pierde | Se reconstruye desde la base; la venta continúa con la latencia mayor |
| Data Lake, Blob y archivo | Se pierde una zona | Almacenamiento redundante en zonas; copia explícita a Brasil |
| Key Vault / Managed HSM | No se pueden leer claves | Servicio zonal; Key Vault propio en Brasil, poblado por reinyección. Managed HSM: replicación multirregión nativa de Chile Central a Brazil South (las dos regiones activas, mismas claves y roles, hasta 6 min de retraso en escrituras; verificado 29-10, S-20). El dominio de seguridad y su quórum se custodian igual fuera de Chile |
| Microsoft Entra ID | Nadie inicia sesión | Servicio global; cuentas de emergencia por frente (break-glass) con custodia dual y ensayo |
| Azure Firewall | Se corta el tráfico del frente | Uno por frente; redundante entre zonas por defecto en regiones con zonas (verificado 29-10, S-08) |
| VPN Gateway | Los sitios pierden el túnel | Uno por frente; cada sitio tiene dos accesos y el 4G/5G |
| Azure Bastion | Sin acceso administrativo | Uno por frente; acceso de emergencia por cuentas break-glass. En Chile Central se despliega entre zonas; en Brazil South Bastion no admite zonas (lista de Microsoft, 29-10), así que allí es de una sola zona |
| Log Analytics y Sentinel | Sin registro ni detección | Log Analytics por frente en Chile; Sentinel por frente en Brazil South, porque Chile Central no admite Sentinel (S-19). Si cae Chile, la detección sigue funcionando; si cae Brasil, los registros siguen guardándose en Chile y la detección se reanuda al volver |
| Sondas de vigilancia | Se pierde el monitor | Una caída alerta «sin señal», no salud falsa; hay dos fuera del clúster |
| Container Registry | No se pueden desplegar imágenes | Réplica en Brasil por digest, probada sin acceso a Chile |
| Estado de Terraform | No se puede aplicar infraestructura | Copia en Brasil; bloqueo para evitar dos `apply` |

### Sitios del Cliente
| Nodo | Si falla | Contención |
| :--- | :--- | :--- |
| Centro de datos de casa matriz (DC-01) | Sistemas conservados dejan de responder | Las integraciones se degradan por interfaz; el ERP/DTE emite en **modalidad fiscal de contingencia**; el restablecimiento depende del Cliente. Es la única falla sin recuperación propia en la nube |
| Sala de respaldo (DC-02) | Se pierde un respaldo del Cliente | No afecta la recuperación de las funciones nuevas: no se usa como sitio de recuperación (misma comuna que DC-01) |
| Centro de distribución | Pierde el enlace | Par local con diario durable, probado a 24 h; ensayo particular de 4 h |
| Concepción | Enlace único hoy | RT-03.17 exige segundo proveedor y ruta física |
| Energía de un sitio | Corte | UPS y, en DC-01, generación autónoma ≥24 h |

### Contrapartes externas
| Nodo | Si falla | Contención |
| :--- | :--- | :--- |
| ERP y facturación | Sin emisión tributaria normal | Modalidad fiscal de contingencia; SLA y copia por contrato |
| WMS | Centro sin gestión de almacén | HA y DR del proveedor, por levantar |
| Pagos, firma, proveedores | Se corta un tercero | Método alterno y responsabilidad por contrato |

## Procedimiento de conmutación (7 etapas)
Orden fijado en el `.tex` (Figura 4.28). La suma de las etapas debe caber en 4 h.
1. **Declaración** de la contingencia por el equipo de operación, con dos sondas independientes (una en Brasil), métricas de transacción real y verificación humana. Nunca por una sola sonda.
2. **Identidad y claves** de cada frente verificadas.
3. **Red y DNS.**
4. **Datos y mensajería:** se aísla Chile (fencing), se promueve la réplica de cada servidor de PostgreSQL, se habilita su alta disponibilidad (en la misma zona mientras Microsoft mantenga bloqueada la alta disponibilidad entre zonas de nuevos servidores en Brazil South; ver límites) y se habilita el Service Bus de cada negocio en Brasil; los productores republican desde un punto de recuperación y cada consumidor descarta lo ya procesado.
5. **Cómputo y herramientas:** ya encendidos.
6. **Servicios de cada frente y activación del origen de Brasil en Front Door** (tráfico gradual).
7. **Prueba funcional:** venta, documento, pedido, crédito, compra con tarjeta de la Filial por el Control de cruces y conciliación de los diarios locales de las tiendas.

Las tiendas siguen vendiendo con sus pares locales durante todo el procedimiento. Las autorizaciones preemitidas a tiendas mantienen reserva previa; durante la conmutación se bloquea nueva emisión hasta conocer los consumos.

## Retorno
Con Chile restablecido y los datos en sincronía: replicación en sentido inverso, ventana acordada con el Cliente, conciliación de lo generado durante la contingencia (RT-07.06) y la misma verificación funcional. El retorno se ensaya también.

## Límites honestos (de las fuentes)
- La réplica de PostgreSQL es asíncrona y su retraso puede superar los 15 min: el RPO no queda garantizado por el producto. Se mide, se alerta y se demuestra en el ensayo. Sobre 15 min se declara pérdida potencial y se concilia con diarios de tienda y colas.
- Los hechos ausentes de todas las copias recuperables no pueden reconstruirse.
- Los SLA de Microsoft son compromisos con créditos, no mediciones. Con AKS 99,95 % y PostgreSQL con alta disponibilidad entre zonas 99,99 %, el producto da 99,94 %, ya cerca del límite de 99,9 %.
- Chile Central no tiene región emparejada: la copia a Brasil es explícita. Por eso no existen en Chile Central el almacenamiento geo-redundante (GRS/GZRS exigen región emparejada), el respaldo geo-redundante de Azure Backup ni el respaldo geo-redundante de PostgreSQL (verificado 29-10). Además, el almacenamiento geo-redundante de Brazil South enviaría copias a Estados Unidos (su pareja es South Central US), por eso tampoco se usa allí y una política de Azure lo impide.
- La replicación de objetos de Azure Storage **no funciona en cuentas Data Lake** (con espacio de nombres jerárquico). La copia de los Data Lake a Brasil se hace con Azure Data Factory o AzCopy programados; la replicación de objetos solo sirve para las cuentas Blob sin espacio jerárquico (archivo y evidencia), y no replica borrados ni cambios hacia un destino inmutable (S-21).
- Microsoft tiene **bloqueada temporalmente la alta disponibilidad entre zonas para nuevos servidores PostgreSQL en Brazil South** (tabla de regiones de PostgreSQL, 29-10). Mientras dure, una base promovida en Brasil opera con alta disponibilidad en una sola zona. Se revisa antes de la construcción; no afecta a Chile Central, que sí la admite.
- Si el Cliente no aprueba la residencia en Brasil, alternativa: sitio propio o de un tercero en otra ciudad de Chile (no DC-02), con RTO 4 h y RPO 15 min, dimensionado y ensayado antes de la puesta en producción.

## Respaldo (política 3-2-1-1-0)
Tres copias, en dos medios, una fuera del sitio (Brazil South), una inmutable (borrar exige la aprobación de una segunda persona) y cero errores al verificarlas. Prueba de restauración mensual sobre una muestra representativa, con tiempo efectivo de restauración medido (RT-07.12).

## Dependencias globales fuera de las dos regiones
Front Door, Entra ID, DNS público, CI/CD y operadores de red. Un fallo de cualquiera no lo resuelve la conmutación a Brasil. Se evalúan una por una en el diseño detallado.

## Pendientes
1. **Dependencia nueva de D-FIS-15** (punto privado en Brazil South): resuelta con A+ (D-FIS-15, confirmada 29-10).
2. Redundancia dentro de la región de Application Gateway y Azure Firewall: cerrada (S-08 verificado en la documentación de Microsoft, 29-10).
3. Tiempo de conmutación esperado de cada componente: se mide en el primer ensayo.
4. Objetivos de RTO y RPO de los servicios no críticos: se declaran por servicio en el diseño detallado.
5. Producto del árbitro de la tienda: cerrado por S-01 (práctica de proveedores revisada 29-10).
