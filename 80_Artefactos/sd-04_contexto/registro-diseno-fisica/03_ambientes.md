# 03 · Ambientes

**Última actualización:** 2026-10-29. **Fuentes:** `.tex` 4.2.3 (Figuras 4.15 y 4.16, párrafos de ambientes); `cierre-inventario/07-dr-ambientes.md`; RT-04.02, RT-04.05, RT-11.25. Esta matriz dice qué existe en cada ambiente; el detalle de cada nodo está en `01_nodos.md`.

## Qué es un ambiente aquí
Un conjunto aislado de recursos, con su propia suscripción de Azure, red, identidades y Key Vault. **Cada frente tiene cinco**: Desarrollo, QA, Preproducción, Producción y Recuperación ante Desastres. Son 15 suscripciones, 3 frentes × 5 ambientes, sin ninguna compartida. La misma imagen de contenedor pasa por los ambientes en orden, y Producción exige aprobación explícita y se despliega por separado para cada frente.

## Reglas comunes (de la fuente)
1. Ningún ambiente no productivo usa datos de producción reales.
2. Cada ambiente de cada frente tiene su propio Key Vault, para que una credencial filtrada en un ambiente no sirva en otro.
3. Preproducción reproduce la topología, la configuración y las versiones de Producción (RT-04.02). Su tamaño permanente no es el de Producción y escala de forma temporal para las pruebas de carga.
4. Recuperación se crea con la misma definición de infraestructura que Producción, para que no se desvíe con el tiempo.
5. Las imágenes llegan a Recuperación copiadas por digest, así que su arranque no depende de Chile.

## Matriz ambiente × tipo de recurso

Lectura: **Sí** = existe con ese propósito; **Reducido** = mismo tipo pero tamaño menor, por medir; **Temporal** = se enciende para pruebas; **Templado** = encendido sin tráfico; **—** = no existe.

| Tipo de recurso | Desarrollo | QA | Preproducción | Producción (Chile Central) | Recuperación (Brazil South) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Clúster de AKS por frente | Reducido, clúster o espacio propio | Reducido | Reducido permanente; escala temporal para carga | Sí: 40 nodos base (Retail 17, Filial 17, Control de cruces 6) | Templado: 40 nodos base |
| Grupo elástico de modelos de conteo | Por definir | Por definir | Por definir | 0 a 3 nodos | 0 a 3, solo tras estabilizar |
| PostgreSQL | Reducido | Reducido | Reducido | 12 servidores, 4.500 GiB | 12, **del mismo tamaño que Producción** (una réplica menor no podría asumir la carga) |
| Service Bus | Reducido | Reducido | Reducido | 2 espacios | 2 con geo-replicación |
| Memoria rápida (Redis) | Por definir | Por definir | Por definir | 1 (Retail) | 1, reconstruible |
| Data Lake y almacenamiento | Reducido | Reducido | Reducido | Por frente | Copia explícita |
| Key Vault | Uno por frente | Uno por frente | Uno por frente | 3 | 3 |
| Managed HSM | — | — | — | 2 si el censo lo exige | 2 si el censo lo exige |
| Entrada (Front Door, Application Gateway, API Management) | Por definir | Por definir | Reproduce la de Producción | Sí | Templado, origen de menor prioridad |
| Red por frente (red central, aplicaciones, datos) | Sí | Sí | Sí | 9 redes | 9 redes |
| Azure Firewall, VPN Gateway, Bastion | Por definir | Por definir | Reproduce Producción | 3 / 2 / 3 | 3 / 2 / 3 |
| Container Registry | Repositorios y permisos distintos de Producción en el registro del frente | Repositorios y permisos distintos de Producción en el registro del frente | Repositorios y permisos distintos de Producción en el registro del frente | 3 (uno por frente; producción y no producción separados por repositorio y RBAC) | Réplicas por digest |
| Estado de Terraform | Cuenta propia por frente | Cuenta propia por frente | Cuenta propia por frente | Cuenta propia por frente | Copia en Brasil |
| Observabilidad y seguridad (Log Analytics, Sentinel, pila del clúster) | Por definir | Por definir | Por definir | Un juego por frente (Log Analytics en Chile; Sentinel en Brazil South, S-19) | Un juego por frente |
| Máquinas de apoyo (Power BI, Data Factory, acceso privado) | — | — | — | 12 | 8 templadas + 4 apagadas |
| Sondas de vigilancia | — | — | — | 2 | 2 |
| Tiendas y centros de distribución | — | — | **1 tienda de laboratorio** (misma composición que la tienda tipo; D-FIS-17) | 22 tiendas, 2 centros | Reconectan al VPN Gateway de Brazil South |
| Datos que contienen | Sintéticos | Sintéticos | Anonimizados o seudonimizados de forma verificable; los de la Filial no se copian | Reales | Réplica de los reales |

## Cómo se promueve un cambio
Desarrollo → QA → Preproducción → Producción, con la misma imagen (mismo digest). Los pipelines exigen revisión por pares, firma, análisis estático, de dependencias y dinámico (SAST, SCA, DAST). Nadie entra directo a Producción. Después de Producción, la misma definición crea Recuperación.

## Discrepancia detectada entre fuentes (resuelta: D-FIS-16, manda el `.tex`)
- La ficha `07` dice que Preproducción usa **datos sintéticos**. El `.tex` dice que Desarrollo y QA usan sintéticos y que Preproducción usa **datos anonimizados o seudonimizados de forma verificable**, pero que los de la Filial no se copian.
- **Propuesta:** manda el `.tex` (es lo que verá el evaluador) y la ficha se considera desactualizada en ese punto. En la práctica, para la Filial Preproducción terminará con datos sintéticos, porque no puede recibir los reales ni siquiera anonimizados. Lo dejé así en `01_nodos.md`.

## Pendientes
1. Tamaño permanente de Desarrollo, QA y Preproducción, cuotas y horarios: se fija por suite de pruebas (el `.tex` lo deja así).
2. ~~Tienda de laboratorio~~ **Decidido (D-FIS-17):** una en Preproducción. Ubicación decidida (29-10): **sala del Cliente**. Pendiente: sala concreta, si usa dos accesos fijos reales o simulados, y su costo (ver 07). Hay que reflejarla en la redacción del sd-04 y en el T-11.
3. Qué componentes de entrada y de observabilidad existen en Desarrollo y QA: el `.tex` dice que usan «los mismos tipos de componentes que Producción con el tamaño que cada ambiente necesita», sin detallar cuáles.
4. Plataforma de CI/CD (pendiente de elegir, ver bloque 3c).

## Direcciones de Brazil South (02-11, derivadas de la Tabla 4.17 del `.tex`)

**Origen:** no es una cifra nueva. El `.tex` (4.2.5) reserva el bloque 10.64.0.0/12, da un /18 a cada red y asigna 10.64, 10.65 y 10.66 a los tres frentes de Chile y 10.68, 10.69 y 10.70 a los de Brasil, en el mismo orden (Retail, Filial emisora, Control de cruces). La Tabla 4.17 dice que CLD-02 repite la estructura. Los rangos de Brazil South son los de Chile con el segundo número cambiado por 68, 69 y 70. Cálculo, no decisión del Cliente.

| Subred (Retail) | Chile Central | Brazil South |
| :--- | :--- | :--- |
| Puerta de enlace VPN | 10.64.0.0/26 | 10.68.0.0/26 |
| Azure Firewall | 10.64.0.64/26 | 10.68.0.64/26 |
| Azure Bastion | 10.64.0.128/26 | 10.68.0.128/26 |
| DNS de entrada y de salida | 10.64.1.0/27 y 10.64.1.32/27 | 10.68.1.0/27 y 10.68.1.32/27 |
| Gestión | 10.64.2.0/24 | 10.68.2.0/24 |
| Entrada (Application Gateway) | 10.64.64.0/24 | 10.68.64.0/24 |
| API Management | 10.64.65.0/24 | 10.68.65.0/24 |
| Nodos de AKS | 10.64.68.0/21 | 10.68.68.0/21 |
| Power BI, SHIR, acceso privado | 10.64.76.0/27, .32/27, .64/27 | 10.68.76.0/27, .32/27, .64/27 |
| Private Endpoints de datos | 10.64.128.0/24 a 10.64.131.0/24 | 10.68.128.0/24 a 10.68.131.0/24 |

Filial emisora: 10.65 en Chile y 10.69 en Brasil. Control de cruces: 10.66 y 10.70. **Por qué importa:** la réplica de PostgreSQL entre regiones exige que las dos redes no tengan direcciones solapadas (Learn, «Replication across Azure regions and virtual networks»); con 10.64 a 10.66 y 10.68 a 10.70 se cumple. Falta además la zona DNS privada enlazada a ambas redes y el puerto 5432 abierto en los dos sentidos.

