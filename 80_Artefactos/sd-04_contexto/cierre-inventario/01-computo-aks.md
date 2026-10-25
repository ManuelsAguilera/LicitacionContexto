# Cierre técnico A — cómputo AKS y VM auxiliares

**Fecha:** 23-10-2026. **Estado:** decisión técnica para el diseño, sujeta a prueba de carga y disponibilidad de SKU por zona. **Uso de IA:** Alto. Este documento dimensiona una capacidad inicial de oferta; no registra mediciones de producción ni reemplaza el levantamiento del mandante.

## Base y criterio de cálculo

El [Caso 09, §14](../../../00_Bases/Caso_09_Cadena_Multitienda.md) da volumen de negocio (31 millones de documentos de venta/año; 104.000 pedidos en tres días del evento, 150.000 en proyección; 380/430 líneas de caja; 11,8/14 millones de transacciones de tarjeta/año), pero **pide al proponente estimar** TPS, consultas/s y concurrencia. Por tanto, esas cifras de negocio no autorizan a afirmar TPS medidos. Se conserva el catálogo de 9 servicios Retail, 3 financieros y X-01 de la [matriz de despliegue](../revision-fisica-2026-10-22/matriz-despliegue.md); las capacidades comunes son cargas adicionales, no nuevos servicios funcionales. Los cálculos históricos de 693 y 6.510 consultas/s usan horizontes distintos y no se adoptan aquí como una única medición.

Para cada pool: `nodos iniciales = max(3, techo(requests CPU simultáneos / (vCPU por nodo × 0,70 × 2/3)))`. Tres nodos se distribuyen 1 por zona; el factor `2/3` exige que los dos supervivientes absorban la reserva inicial tras perder una zona. La memoria debe pasar el mismo cálculo usando 70 % de RAM **asignable** (después de reservas de sistema y kubelet). El 70 % es un objetivo de diseño, no una recomendación contractual ni un límite del producto. Los *requests* agregados de la tabla siguiente son **presupuestos supuestos** para toda la carga del pool, incluidos sidecars, no mediciones. La admisión impide instalar cargas que excedan ese presupuesto. Los máximos de autoscaling son techos de configuración, no una garantía de tolerar crecimiento 3× junto con caída de AZ; tal escenario se prueba y se recalcula.

Los pools SYS son de sistema; BIZ, INT, STATE y OPS son de usuario con taints, tolerations y afinidad de ámbito. Se eligen pools **alineados por zona**, un VMSS por combinación pool/zona cuando se necesite control fino de escala, y tres nodos base por función agregados entre las tres zonas. El nombre lógico `R-BIZ` agrupa esos tres VMSS zonales; no representa un único VMSS multizona. Azure permite pools alineados o extendidos entre zonas; la configuración concreta y las cuotas de Chile Central requieren prueba. El plano de control AKS administrado no se cuenta como VM de Ancoa. [Microsoft: zonas de AKS](https://learn.microsoft.com/azure/aks/availability-zones-overview); [pools de sistema](https://learn.microsoft.com/en-us/azure/aks/use-system-pools).

## Inventario de producción en Chile Central

Los tamaños indican capacidad **mínima objetivo por nodo** (vCPU/GiB), no un SKU adjudicado. Se contratará un SKU zonal compatible que alcance o supere el par; RAM asignable, disco temporal, límites de red, cuotas y precio se comprobarán antes de fijarlo. Linux para todos los pools. `CPU presup.` expresa suma máxima inicial de requests de pods; dos nodos supervivientes × 70 % × vCPU dejan la capacidad útil tras caída de una zona.

| ID pool / ámbito | Carga admitida | Nodos base / AZ | Capacidad objetivo por nodo | CPU presup. / útil tras perder AZ | Máximo inicial de autoscaling | Estado |
| --- | --- | ---: | --- | --- | ---: | --- |
| R-SYS / Retail | CoreDNS, métricas, CNI/CSI y controladores de sistema | 3 / 1-1-1 | 4/16 | 4 / 5,6 vCPU | 6 | Diseño; presupuesto supuesto |
| R-BIZ / Retail | Web privada; R:M-01..03, R:V-01..04, R:CL-01..02 y capacidades comunes Retail | 5 / 2-2-1 | 16/64 | 24 / 33,6 | 12 | Diseño; presupuesto supuesto |
| R-INT / Retail | Adaptadores Comercio, Canales, Socios; sincronizador, proyectores, outbox y trabajos | 3 / 1-1-1 | 8/32 | 9 / 11,2 | 9 | Diseño; presupuesto supuesto |
| R-STATE / Retail | OpenSearch, OpenMetadata y MLflow | 3 / 1-1-1 | 16/64 | 17 / 22,4 | 6 | Diseño condicionado a almacenamiento y quórum |
| R-OPS / Retail | OTel gateway, Prometheus, Loki, Tempo, Grafana y Alerting | 3 / 1-1-1 | 8/32 | 9 / 11,2 | 6 | Diseño; presupuesto supuesto |
| F-SYS / Filial | Sistema AKS financiero | 3 / 1-1-1 | 4/16 | 4 / 5,6 | 6 | Diseño; separado de R |
| F-BIZ / Filial | Web tarjeta; F:C-01..03 y capacidades comunes F | 5 / 2-2-1 | 8/32 | 14 / 16,8 | 9 | Diseño; F:C-04 excluido |
| F-INT / Filial | Adaptador Crédito, firma/reportes, proyectores y conciliación | 3 / 1-1-1 | 8/32 | 7 / 11,2 | 9 | Diseño; separado de R |
| F-STATE / Filial | OpenSearch y OpenMetadata propios | 3 / 1-1-1 | 16/64 | 13 / 22,4 | 6 | Diseño condicionado a almacenamiento y quórum |
| F-OPS / Filial | OTel, Prometheus, Loki, Tempo, Grafana y Alerting propios | 3 / 1-1-1 | 8/32 | 8 / 11,2 | 6 | Diseño |
| X-SYS / X-01 | Sistema AKS del enclave | 3 / 1-1-1 | 4/16 | 4 / 5,6 | 6 | Diseño; separado de R/F |
| X-BIZ / X-01 | Control X-01 y acceso exclusivo a pg-x01 | 3 / 1-1-1 | 4/16 | 4 / 5,6 | 6 | Diseño; contrato mínimo R→X→F |
| R-BATCH / Retail | Python/scikit-learn, entrenamiento y conteo | 0; escala 0–3 | 16/64, perfil por ensayo | Jobs admitidos por cuota | 3 | Propuesto, fuera de las 40 VM base |

**Suma:** R 17 + F 17 + X 6 = **40 VM AKS base**. Son 12 pools lógicos de producción, más R-BATCH elástico. La base de tres nodos por pool evita un nodo único y conserva dos tras una falla zonal; no demuestra por sí sola HA de OpenSearch, metadatos ni telemetría. Para STATE, volumen persistente, StorageClass, replicación de aplicación y quórum se validan con D/F. El clúster no aloja PostgreSQL, Service Bus, Redis, Blob ni el plano de control administrado.

## Réplicas, recursos y escalado

La unidad presupuestaria de un servicio BIZ o INT sin estado es **3 pods mínimos**, distribuidos con topology spread y anti-afinidad entre AZ. Cada Deployment tiene readiness/liveness, `PodDisruptionBudget` compatible con conservar 2 réplicas y límites de memoria. Se empieza con requests `0,5 vCPU/1 GiB` para APIs normales, `1 vCPU/2 GiB` para rutas críticas de venta/crédito y `0,25 vCPU/0,5 GiB` para web ligera; son hipótesis **por pod** que se ajustan con perfil real. Nueve servicios Retail × 3 × 0,5 = 13,5 vCPU; dos webs × 3 × 0,25 = 1,5; cuatro capacidades comunes separadas × 3 × 0,5 = 6. El subtotal es 21 vCPU; con 15 % de holgura operativa son 24,15, inferior a los 33,6 vCPU útiles de tres nodos R-BIZ supervivientes. En Filial, tres servicios × 3 × 1 = 9 vCPU, web × 3 × 0,25 = 0,75 y dos capacidades comunes × 3 × 0,5 = 3; con 10 % de holgura, 14,025 vCPU, inferior a los 16,8 útiles de tres nodos F-BIZ supervivientes. Se adoptan **5 nodos BIZ por ámbito**, distribuidos 2-2-1; después de perder cualquiera de las zonas quedan al menos tres. El total base sube de 36 a **40 VM AKS**. Los 15 % y 10 % son márgenes supuestos a comprobar. Los IDs `R-BIZ-01..05` y `F-BIZ-01..05` son posiciones de diseño, no nombres estables de VM.

Se configuran HPA por CPU y latencia/cola según carga, por ejemplo aumentar réplica cuando CPU usada supere 65 % del request durante 5 minutos o p95/edad de cola viole su objetivo dos ventanas; reducir solo tras 30 minutos estables. Cluster Autoscaler agrega nodos cuando pods pendientes no caben y respeta máximos por pool. Estos umbrales se recalibran con prueba; **HPA no suple cupos, retardo de arranque ni quórum de almacenamiento**. SYS mínimo 3; STATE y OPS se escalan con procedimientos específicos para no duplicar ni perder volúmenes. R-BATCH usa Jobs con límites de concurrencia y prioridad inferior al tráfico transaccional, sin desalojar BIZ. Referencia: [fiabilidad de despliegue AKS](https://learn.microsoft.com/en-us/azure/aks/best-practices-app-cluster-reliability).

En la prueba de aceptación se generan, por separado y combinados, sábado de diciembre, evento digital (104.000/150.000 pedidos en tres días), 400.000 cambios de precio en un día, reconexión de 22 tiendas y pérdida de una AZ. Se miden TPS/p95/p99, requests reales, OOM, nodos requeridos, tiempo de scale-out, cola y saturación PostgreSQL/Service Bus. Para crecimiento 3×: `requests_proyectados = requests_medidos × 3` solo sobre la fracción variable; se suma la carga fija y se vuelve a aplicar la fórmula con `2/3`. Se verifican límites por SKU/cuota y que PostgreSQL, PaaS e integración sostengan el mismo escenario. El máximo de la tabla es reserva administrativa provisional.

## VM auxiliares fuera de AKS

| IDs / región / ámbito | Cantidad y objetivo por VM | Servicio, HA y ruta | Estado |
| --- | --- | --- | --- |
| R-BI-01/02 · Chile · R | 2 × Windows, 8 vCPU/16 GiB | Gateway estándar Power BI en clúster HA; salida al servicio y lectura permitida de pg-r-mart por ruta privada | Diseño con tamaño inicial de [guía Microsoft](https://learn.microsoft.com/en-us/power-bi/guidance/gateway-onprem-sizing); carga a medir |
| F-BI-01/02 · Chile · F | 2 × Windows, 8 vCPU/16 GiB | Clúster HA financiero separado; pg-f-mart | Diseño; sin credencial R |
| R-IR-01/02 · Chile · R | 2 × Windows, 8 vCPU/16 GiB | Dos nodos de un SHIR lógico Retail, control ADF por salida y fuentes autorizadas; AZ distintas | Diseño; Microsoft admite [hasta 4 nodos](https://learn.microsoft.com/en-us/azure/data-factory/create-self-hosted-integration-runtime) |
| F-IR-01/02 · Chile · F | 2 × Windows, 8 vCPU/16 GiB | SHIR financiero independiente | Diseño; carga a medir |
| R-PA-01/02 · Chile · R | 2 × Windows, 4 vCPU/16 GiB | Entra Private Access Connector; destinos privados autorizados y salida controlada | Diseño; compatibilidad/PoC de acceso pendiente |
| F-PA-01/02 · Chile · F | 2 × Windows, 4 vCPU/16 GiB | Conectores y red propia F | Diseño; PoC pendiente |
| R-SYN-01 · Chile · R; F-SYN-01 · Chile · F | 2 × Linux, 2 vCPU/4 GiB | Sonda Blackbox fuera del AKS observado, en segmento operativo propio, con salida de alertas; una por ámbito | Decisión de emplazamiento de diseño; segunda región evaluada por G |

**Subtotal Chile de producción para este encargo:** 40 nodos AKS iniciales + 12 VM BI/IR/PA + 2 sondas = **54 VM**. En contingencia, R-BATCH agrega 0–3 nodos. Los 12 auxiliares y dos sondas no son pods AKS; PostgreSQL, ADF, Power BI, Entra, plano de control, Load Balancer, ACR y demás PaaS tampoco se cuentan como VM propias. Las VM auxiliares se distribuyen entre dos AZ; cada par debe probar la HA del software, pues dos VM sanas no garantizan conmutación. El dimensionamiento de BI arranca por encima de la recomendación mínima de 8 núcleos/8 GiB; Microsoft pide medir CPU y memoria para ajustar. La residencia del servicio SaaS Power BI se trata por separado de la VM gateway.

## Decisiones y validación restante

| Decisión | Alternativa y razón | Fuente / estado | Prueba que puede cambiarla |
| --- | --- | --- | --- |
| Tres clústeres R/F/X; identidad, red, datos y pools propios | Un único clúster con namespaces facilitaría operación, pero reduciría aislamiento de administración y fallo | Separación del Caso y decisión de diseño | Revisión de seguridad y costes de operación, sin mezclar ámbitos |
| Pools SYS/BIZ/INT/STATE/OPS; BATCH elástico R | Aísla cómputo crítico, estado y batch; evita que ML afecte venta | Matriz de despliegue y decisión técnica | Perfil de pods, cuotas y requisitos de productos STATE |
| 40 nodos base iniciales y 0–3 batch | Corrige la insuficiencia visible de 36 bajo Deployments separados; mantiene dos zonas supervivientes | Cálculo de este documento; **supuesto de requests** | Prueba con software real y pérdida de AZ |
| 12 VM auxiliares + 2 sondas en Chile | Gateway, SHIR y conectores pares separados por negocio; sonda fuera del clúster | Decisión técnica, guías Microsoft citadas | PoC de Private Access, rendimiento BI/ADF y alertas |
| SKU exacto y discos de nodo/PV | Se compra familia compatible con objetivos, no se fija número de parte sin comprobar disponibilidad por AZ | Sujeto a validación de producto | Quotas, catálogo regional, IOPS, costo y benchmark |
| Brasil y ambientes inferiores | No forman parte de las 54 VM Chile de producción | Encargo G | Inventario DR y pipelines |

**Dependencias para integración:** B fija CIDR/subredes y ruta de egreso de los tres clústeres; D dimensiona PV/IOPS y repositorios STATE; F fija identidades, telemetría, acceso y política de sonda; G replica la capacidad recuperable en Brasil. El coordinador debe trasladar **40/12/2**, conservar el subtotal 54 como capacidad inicial condicionada y eliminar del maestro la aritmética antigua de 36+12 como cifra definitiva. No asignar estado «revisado» sin revisión humana registrada.


