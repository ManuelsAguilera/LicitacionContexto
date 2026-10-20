---
id: sd-04_s2_dimensionamiento-nodos
titulo: Memoria de dimensionamiento de nodos del despliegue en nube y en sitio
subdocumento: sd-04
seccion: 4.2 Dimensionamiento y plan de capacidad
estado: borrador
fuentes:
  - 02_Propuesta/latex_final/OSS-Informe 2/Informe 2/OnlySimpleSolutions-Subdocumento5.pdf (Tablas 5.11, 5.12, 5.17 a 5.19)
  - 02_Propuesta/latex_final/sd-04/OnlySimpleSolutions-Subdocumento4.tex (Tablas 4.13 y 4.14)
  - 00_Bases/Bases_Transversales.md (RT-03.02, RT-04.01, RT-04.02, RT-09.01, RT-09.03, RT-11.25)
  - 90_Referencia/clases markdown/FEP01 (diapositivas 78, 93, 99 a 101, 105 a 117)
---

# Memoria de dimensionamiento de nodos

Deriva la capacidad de cada nodo desde la volumetría del Subdocumento 5, como exige RT-09.01 y la diapositiva 78 de FEP01 («la arquitectura física no se inventa: se deriva»). Las cifras son estimaciones y se validan en la prueba de carga de Preproducción antes del hito H5.

## 1. Entradas (SD-05, Tablas 5.18 y 5.19)

| Entrada | Valor de diseño | Valor de prueba (× 1,5) |
|---|---|---|
| Consultas de disponibilidad en la apertura del evento | 693 por segundo | 1.040 por segundo |
| Pedidos en la apertura | 5,8 por segundo | 8,7 por segundo |
| Documentos de venta, sábado de diciembre | 12 por segundo | 18 por segundo |
| Evaluaciones crediticias | 0,2 por segundo | 0,3 por segundo |
| Carga masiva de precios | 1.333 publicados y 6.667 entregados por segundo | igual (escenario de estrés) |
| Sincronización de existencia | 1.135 mensajes por segundo | 1.703 mensajes por segundo |
| Almacenamiento transaccional | 192,6 GB por año provisionados (81,4 Retail, 14,2 Emisor y 3,2 Frontera netos) | — |
| Históricos migrados a la base | Retail 48 GB (12 meses de venta y pedidos, maestros y padrón); Emisor 7,2 GB | — |

## 2. Supuestos de consumo (a validar en la prueba de carga)

| Código | Supuesto | Valor |
|---|---|---|
| S1 | Consultas de lectura atendidas desde caché por vCPU | 200 por segundo |
| S2 | CPU por transacción de escritura (venta o pedido) | 25 ms |
| S3 | CPU por evento consumido | 2 ms |
| S4 | Réplicas mínimas por servicio | 3, una por zona (RT-03.02) |
| S5 | Reserva por réplica | Retail y Emisor 0,5 vCPU y 1 GiB; base tecnológica 0,25 vCPU y 0,5 GiB |
| S6 | Uso máximo de un pool de workers en el peak | 66 %, para que la caída de una zona de tres deje el uso bajo 100 % (FEP01, diap. 101) |
| S7 | Servicios por clúster | Retail 11 (9 de 3.3 y 2 interfaces nuevas); Emisor 4 (3 de 3.3 y su portal); base 11 (X-01 y 10 adaptadores) |

AKS es un servicio administrado: Microsoft opera el plano de control repartido entre zonas (SLA 99,95 %), por lo que no se cotizan masters propios (FEP01, diap. 99). La regla de tres masters se cumple por el servicio.

## 3. Cómputo de AKS (Producción, CLD-01)

| Clúster | Demanda en el peak | Capacidad necesaria (÷ 0,66) | Pool de usuario | Uso en el peak | Uso con una zona caída | Pool de sistema |
|---|---|---|---|---|---|---|
| Retail | 16,5 vCPU base (11 × 3 × 0,5) + 13,3 de la carga de precios (6.667 × 2 ms) = 29,8 vCPU | 45,2 vCPU | 6 × D8ds_v5 (8 vCPU / 32 GiB), 2 por zona, escala hasta 12 | 62 % | 93 % | 3 × D4ds_v5 (4 vCPU / 16 GiB) |
| Emisor | 6,0 base (4 × 3 × 0,5) + 0,5 de evaluaciones = 6,5 vCPU | 9,8 vCPU | 3 × D4ds_v5, 1 por zona, escala hasta 6 | 54 % | 81 % | 3 × D4ds_v5 |
| Base tecnológica | 8,25 base (11 × 3 × 0,25) + 2,3 de sincronización (1.135 × 2 ms) = 10,5 vCPU | 15,9 vCPU | 3 × D8ds_v5, 1 por zona, escala hasta 6 | 44 % | 66 % | 3 × D4ds_v5 |
| Modelos predictivos (Retail) | Entrenamiento nocturno | — | 0 a 2 × D8ds_v5, escala a cero | — | — | (usa el de Retail) |

La carga de precios domina en Retail porque es el único escenario que suma miles de eventos por segundo; la apertura del evento agrega 5,4 vCPU (1.040 ÷ 200 + 8,7 × 25 ms) y no coincide con ella. El crecimiento de tres veces que pide RT-09.03 se absorbe con el escalamiento automático hasta el máximo indicado, sin rediseño.

## 4. Datos

| Servicio | Cálculo | Nodo y disco | IOPS |
|---|---|---|---|
| PostgreSQL Retail | 158,7 GB por año (82,4 % de 192,6) × 3 años + 48 GB de históricos = 524 GB; triplicado por RT-09.03, 1,6 TB | General Purpose D8ds_v5 (8 vCore / 32 GiB), primario Z1 y espera Z2; Premium SSD P40 de 2 TiB | 7.500 provistos. Demanda de la carga de precios: 1.333 inserciones × 4 E/S = 5.300, más 700 de ventas y movimientos = 6.000 (80 %) |
| PostgreSQL Emisor | 27,7 GB por año × 3 + 7,2 GB = 90 GB; triplicado, 270 GB | General Purpose D4ds_v5 (4 vCore / 16 GiB), Z1 y Z2; Premium SSD P20 de 512 GiB | 2.300 provistos; demanda menor a 100 |
| PostgreSQL de X-01 (bitácora de cruces) | 3,2 GB por año; 56 meses, 15 GB | General Purpose D2ds_v5 (2 vCore / 8 GiB), Z1 y Z2; Premium SSD P10 de 128 GiB | 500 provistos |
| Azure Managed Redis (Retail) | Precio vigente 1,83 millones de filas × 300 B = 0,55 GB; disponibilidad 458.000 × 28 nodos × 100 B = 1,3 GB; total 1,9 GB; triplicado, 5,6 GB | Balanced B5 (6 GB), alta disponibilidad entre zonas | — |
| Event Hubs Premium | Entrada pico 1.333 × 300 B = 0,4 MB/s; salida 2,0 MB/s | Retail 2 unidades de procesamiento; Emisor 1 | — |
| Data Lake Gen2 (ZRS) | Retail: 200 GB de venta histórica + 160 GB por año; Emisor: 30 GB por año | Retail 1 TB a 3 años; Emisor 0,1 TB | — |
| Blob inmutable del Emisor (ZRS) | 1,9 TB por año de grabaciones y evidencia (SD-05) × 4,7 años | 9 TB al cierre; nivel Hot 90 días y luego Cool | — |

## 5. Borde, red y sitios

| Elemento | Dimensionamiento | Fundamento |
|---|---|---|
| Application Gateway v2 | 2 a 10 instancias con escalamiento automático, repartidas entre zonas, por ámbito | 1.040 consultas por segundo caben en 2 instancias; el máximo cubre el crecimiento |
| API Management Premium clásico | 3 unidades por instancia (una por zona), 2 instancias; 1 unidad de gateway en CLD-02 | SD-04, Tabla 4.10 |
| FortiGate-VM | 2 × Standard_F4s_v2 (4 vCPU / 8 GiB), licencia VM04, activo-pasivo en Z1 y Z2 | Túneles de 22 tiendas × 10 Mbps y 2 centros = 240 Mbps cifrados |
| Puerta VPN | VpnGw2AZ, redundante entre zonas | Respaldo del circuito de 200 Mbps |
| Puerta ExpressRoute y circuito | ErGw1AZ; circuito de 200 Mbps | Ola de migración de 110 Mbps (Tabla 4.14) |
| Nodo local de tienda | 2 × (4 núcleos / 16 GB / 2 × SSD de 480 GB en RAID 1) por tienda, 44 en total | 24 horas de la tienda mayor: 1,34 documentos por segundo, 312,8 MB de ventas y unos 3 GB de oferta en caché; el disco deja más de 100 veces de margen |
| Almacenamiento en red de DC-01 (T-11, fila 7.4) | Arranque en RAID 1; datos en RAID 10 con un disco de reserva | Factor de compra × 2,5 sobre la capacidad útil (FEP01, diap. 113 y 114) |

En DC-01 no se cotiza hipervisor: la solución nueva no instala máquinas virtuales en el recinto, que aloja las plataformas actuales del Cliente y el equipo de comunicaciones (FEP01, diap. 103).

## 6. Capacidad por ambiente

| Ambiente | Capacidad respecto de Producción | Datos |
|---|---|---|
| Desarrollo | 15 % | Sintéticos o anonimizados (RT-11.25) |
| QA | 25 % | De prueba controlados y versionados |
| Preproducción | 50 %, con la misma topología y escalamiento temporal al 100 % para las pruebas de carga (RT-04.02) | Representativos y anonimizados |
| Producción | 100 % | Reales |
| Recuperación (CLD-02) | Datos al 100 % (réplicas del mismo tamaño); cómputo de AKS en 0 y creado por código al conmutar | Réplica de Producción |

## 7. Totales de Producción en CLD-01

| Recurso | Cantidad |
|---|---|
| vCPU de AKS | 120 (36 de sistema y 84 de usuario), más 16 del pool predictivo cuando entrena |
| Memoria de AKS | 480 GiB |
| vCore de PostgreSQL | 28 (14 primarios y 14 en espera) |
| Memoria de PostgreSQL | 112 GiB |
| Disco de bloque de PostgreSQL | 2,6 TiB por copia |
| vCPU de FortiGate-VM | 8 |
