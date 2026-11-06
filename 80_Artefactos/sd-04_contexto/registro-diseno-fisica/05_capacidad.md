# 05 · Capacidad y dimensionamiento

**Última actualización:** 2026-10-29. **Fuentes:** `.tex` 4.2.8 y Tabla 4.21 (que usa las cifras de SD-05, Tablas 5.17 a 5.19); `cierre-inventario/01-computo-aks.md` y `04-datos-custodia.md`; RT-03.20, RT-09.01, RT-09.03. No se crean cifras nuevas: esta sección ordena el recorrido **cifra de carga → recurso que dimensiona → cómo → estado**, y declara de dónde viene cada número.

## Etiquetas de origen
- **Calculada:** sale de otra cifra con una fórmula que recalculé aquí.
- **Del Caso / de SD-05:** viene de ese documento; no la recalculo.
- **Criterio:** decisión de diseño, sin cálculo que la sustente.
- **Hipótesis:** supuesto que se mide en la Etapa 1.
Todas las cifras son estimaciones, no mediciones (lo dice el `.tex`). Se validan en el levantamiento y la prueba de carga de Preproducción (RT-09.01).

## 1. Cifras de carga y su origen

| Cifra | Valor | Origen | Comprobación mía |
| :--- | :--- | :--- | :--- |
| Transacciones en régimen normal | 2,2/s promedio; 4,5/s en hora ordinaria | Calculada (35,1 M operaciones/año en 12 h diarias) | 35,1 M ÷ 365 ÷ 12 h ÷ 3.600 = 2,23/s ✓ |
| Peak del primer día del evento | 5,8 pedidos/s en 15 min | Calculada (5.200 pedidos en la apertura) | 5.200 ÷ 900 s = 5,78/s ✓ |
| Consultas de disponibilidad | 693/s; 13.867 personas concurrentes; prueba con 1.040 | Calculada (120 consultas por pedido, 20 s entre consultas, margen de prueba 1,5) | 13.867 ÷ 20 s = 693,35/s ✓. El 1.040 es el margen 1,5 sobre 693 (693 × 1,5 = 1.040) |
| Sábado de diciembre | 11,8 documentos/s; el diseño parte de 12 | Del Caso / SD-05 (promedio de documentos por 6, verificado con 380 cajas y 640 terminales móviles) | No recalculada (depende de SD-05) |
| Evaluaciones de crédito en el punto de venta | 0,2/s; 1,6 en curso a la vez | Calculada (proporción sobre ventas; límite de 8 s) | 0,2 × 8 s = 1,6 ✓ |
| Carga masiva de precios | 1.333 eventos publicados/s; 6.667 entregados/s | Calculada (400.000 cambios en 5 min, 5 tipos de consumidor) | 400.000 ÷ 300 = 1.333; × 5 = 6.667 ✓ |
| Sincronización de existencia | 40,5 movimientos/s; 1.135 mensajes/s | Calculada (106,5 M movimientos/año a 28 destinos) | 40,5 × 28 = 1.134 ✓ (1.135 por redondeo) |
| Ancho de banda de tienda, normal | 0,02 Mbps | Del Caso / SD-05 (tienda grande) | No recalculada |
| Ancho de banda de tienda, peak | 4,8 Mbps | Calculada (120 MB de precios en 5 min = 3,2 Mbps; margen 1,5) | 120 × 8 ÷ 300 = 3,2; × 1,5 = 4,8 ✓ |
| Resincronización tras 24 h sin enlace | 523,4 MB; 2,3 Mbps para cerrarla en 30 min | Calculada (312,8 MB de ventas + 210,6 MB de bajada; plazo RT-03.13) | 523,4 × 8 ÷ 1.800 = 2,33 Mbps ✓ |
| Ancho de banda de centro de distribución | 0,08 Mbps normal; 0,1 Mbps en el pico | Calculada (10 KB/s de movimientos; 40,5 mensajes/s de 300 B) | No recalculada: depende de los 10 KB/s |
| Enlace DC-01 con la nube | 0,2 Mbps en operación; 110 Mbps en ola de migración | Calculada (11,8 documentos/s de 1,8 KB; 264,5 GB en ventana de 8 h, margen 1,5) | 264,5 GB × 8.000 ÷ 28.800 s = 73,5 Mbps; × 1,5 = 110 ✓ |

Todas las que recalculé coinciden con la Tabla 4.21. Las que no recalculé dependen de datos de SD-05 que no tengo en el registro.

## 2. De la cifra al recurso (qué dimensiona qué)

| Recurso | Lo dimensiona | Cómo | Resultado hoy | Origen y estado |
| :--- | :--- | :--- | :--- | :--- |
| Nodos de AKS (cada grupo) | Solicitudes de CPU simultáneas | `nodos = máx(3, techo(requests CPU / (vCPU por nodo × 0,70 × 2/3)))`. El 0,70 es objetivo de uso; el 2/3 hace que, perdida una zona, los dos tercios restantes absorban la carga | 40 nodos en Chile (Retail 17, Filial 17, Control de cruces 6) | **Criterio** (0,70 y 2/3) + **hipótesis** (requests por servicio); tamaño por nodo es capacidad mínima, no producto adjudicado |
| Pods por servicio | Disponibilidad | Mínimo 3, repartidos entre zonas; solicitudes tipo: 0,5 vCPU/1 GiB (API normal), 1 vCPU/2 GiB (ruta crítica de venta o crédito), 0,25 vCPU/0,5 GiB (web ligera) | 3 réplicas mínimas | **Criterio** |
| Autoescalado | Carga real | Se agregan réplicas cuando el CPU pasa de 65 % del request durante 5 min; se reducen tras 30 min estables | Máximo inicial por grupo (p. ej. 12 en negocio de Retail) | **Criterio**; se recalibra con la prueba |
| Crecimiento de 3 veces (RT-09.03) | Requests proyectados | `requests proyectados = requests medidos × 3`, absorbido por el escalado dentro de los máximos | Sin rediseño | **Criterio** |
| PostgreSQL (12 servidores) | Volumen de datos y retención | `capacidad = (datos actuales + tasa anual × horizonte) × índices y crecimiento`. Solo ventas está bien fundada: 36 M documentos/año × 2 KiB ≈ 69 GiB/año + líneas ≈ 40 GiB/año; × 6 años ≈ 654 GiB; × 1,5 ≈ 981 GiB | 4.500 GiB iniciales (Retail 2.250; Filial 2.150; Control de cruces 100) | PG-R-VENTA calculada; los demás son **hipótesis** con incertidumbre alta |
| Service Bus (por negocio) | Entregas por segundo | Carga de precios: 1,6 M entregas/día; promedio 56/s en 8 h; diseñado a 10× de ráfaga ≈ 560/s | Unidades de mensajería Premium escalables, por fijar | **Calculada** (promedio) + **criterio** (10×) |
| Redis (Retail) | Conjunto caliente | 650.000 productos × 2 KiB × 2 representaciones ≈ 2,5 GiB; se reservan 16 GiB para índices y sobrecarga | 16 GiB | **Calculada** + **criterio** (reserva) |
| Data Lake | Carga anual × años en línea × factor de versiones + histórico | Retail 3 TiB; Filial 2 TiB de partida | 5 TiB | **Hipótesis** |
| Evidencia financiera | Aperturas con evidencia + audio | ~180.000 expedientes/año × 1 MiB ≈ 176 GiB/año + audio ≈ 29 GiB/año; 10 cohortes ≈ 2 TiB antes de versiones y réplicas | 5 TiB inicial ampliable | **Hipótesis** (20 % de evaluaciones abren con evidencia) |
| Archivo tributario y de venta (Retail) | Documentos × retención | 36 M × 100 KiB × 6 años ≈ 20,6 TiB sin comprimir | 25 TiB inicial | **Calculada** (el formato real domina) |
| Archivo de la Filial | Estados de cuenta × retención | 760.000/mes × 12 × 100 KiB ≈ 0,87 TiB/año; × 10 años ≈ 8,7 TiB | 12 TiB inicial | **Calculada** |
| Operación (telemetría, artefactos) | Sin bytes medidos | Reserva de 1 TiB por frente, con alertas a 70 % y 85 % | 1 TiB por frente | **Criterio** |
| Log Analytics y Sentinel | GB ingeridos por día | Sin cifra | Por medir | **Pendiente**; es el costo que más sube sin filtrar |
| API Management | Solicitudes por segundo | Derivado de 693/s en la entrada | Unidades por fijar | Pendiente: lo fija el diseño detallado |
| Front Door | Solicitudes por segundo y región | Límite de Microsoft: 7.200/s por clúster regional por perfil; nuestro peak es 693/s | Holgado (≈10×) | **Calculada** contra el límite |
| Enlace de tienda | Peak de precios y resincronización | Cada acceso fijo ≥ 10 Mbps (el doble de 4,8); respaldo 4G/5G ≥ 5 Mbps | 10 y 5 Mbps | **Calculada** (4,8 × 2 ≈ 10) + **criterio** (doble) |
| Enlace de centro de distribución | Tráfico propio | Reserva 2 Mbps para la solución; el router 4G/5G lleva lo mismo | 2 Mbps | **Criterio** (la carga es 0,1 Mbps) |
| VPN Gateway en casa matriz | Ola de migración | Dimensionada para 110 Mbps | 110 Mbps | **Calculada** |
| Diarios locales de tienda y de centros | Eventos × horas × margen | `capacidad = 24 × p × b × k × (1 + crecimiento) × margen`; se parte de 100 GB útiles por centro | 100 GB por centro | **Criterio** (reserva preliminar) |

## 3. Qué falta para cerrar la capacidad (y quién lo aporta)
1. **Medir en la Etapa 1:** levantamiento y prueba de carga de Preproducción. Hasta entonces todo es estimación.
2. **Requests reales por servicio**, para validar los 17/17/6 nodos y los máximos de autoescalado.
3. **Datos de muestra** para recalibrar los tamaños de las bases (solo ventas está bien fundada).
4. **Volumen de registros** (GB/día) para Log Analytics y Sentinel.
5. **Unidades de API Management y de Service Bus**: se derivan en el diseño detallado.
6. **Carga eléctrica proyectada de casa matriz** y ocupación de racks: con el informe interno de 2024 del Cliente.
7. **Datos de las 22 tiendas**: padrón real (06, P-01); la capacidad parte de la tienda tipo.

## 4. Pruebas de capacidad previstas (de las fuentes)
Se generan por separado y combinadas: sábado de diciembre, evento digital (104.000 y 150.000 pedidos en tres días), 400.000 cambios de precio en un día, reconexión de las 22 tiendas y pérdida de una zona. Se miden TPS, p95 y p99, requests reales, memoria agotada, nodos requeridos, tiempo de escalado, cola y saturación de PostgreSQL y Service Bus. En operación, la capacidad se revisa con la tendencia de uso y los umbrales de ampliación se fijan con el Cliente.

## Pendientes
1. Los puntos de la sección 3 son entregas del proyecto, no se resuelven aquí.
2. Las unidades de API Management, Service Bus y el tamaño de subredes se derivan en el diseño detallado.
3. Capacidad de la tienda de laboratorio (D-FIS-17): igual a la tienda tipo; no suma a los 88 servidores.
