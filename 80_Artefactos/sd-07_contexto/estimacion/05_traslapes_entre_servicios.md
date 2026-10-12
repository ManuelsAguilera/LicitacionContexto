# Traslapes entre servicios del modelo de casos de uso (puerta G3)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta de este trabajo, pendiente de la firma del equipo. Casos: `03_casos_de_uso_*.md`. Un traslape es una función o un evento que dos casos de servicios distintos describen casi igual y que podría contarse dos veces. Se revisó cada par que comparte dato, evento o regla.

## 1. Cuándo importa un traslape

El UUCW depende de la clase del caso (1 a 3 transacciones = 5, 4 a 7 = 10), no del número exacto. Por eso quitar una transacción solo cambia el resultado si el caso baja de 4 a 3. Tras la revisión independiente de G3 quedan 2 casos medios (CU-EX-04 y CU-OF-02). CU-EX-08 y CU-VE-04 se simplificaron. Un traslape en un caso simple tiene efecto 0 sobre el UUCW. Se registra igual para que la memoria de cálculo no cuente la misma función dos veces.

## 2. Traslapes encontrados

| N.º | Casos | Qué se parece | Tratamiento | Efecto en el UUCW |
| :-- | :-- | :-- | :-- | :-- |
| 1 | CU-EX-02, CU-EX-03 (segunda transacción) | Consulta de disponible desde un canal | Se dejan: EX-02 es la consulta de tienda y de despacho, y EX-03 responde al canal por interfaz. Se declara | 0 |
| 2 | CU-OF-02 (tercera transacción), CU-OF-03 | Consulta del precio vigente | Se dejan: OF-03 es el precio de una referencia y OF-02 la oferta completa del canal | 0 |
| 3 | CU-OF-02 (cuarta transacción), CU-EX-03 (tercera) | Republicar al reconectarse un canal | Mecanismo común con datos distintos (oferta y disponible). Si se funde con su publicación, OF-02 baja a 3 | −5 si se funde |
| 4 | CU-EX-04 (cuarta transacción), CU-PE-08 (primera) | Liberar la reserva al cancelar el pedido | Si la cancelación de pedidos dispara la liberación en la misma ida y vuelta, EX-04 baja a 3 | −5 si se funde |
| 5 | CU-EX-04 (tercera transacción), CU-PE-03 | Confirmar la reserva al aceptar el pedido | La reserva se cuenta en existencias y no en pedidos (supuesto 4 de pedidos) | 0 (el mismo efecto del traslape 4) |
| 6 | CU-EX-06, CU-PE-04 | Verificar la unidad antes del cobro y capturar el cobro | Son eventos distintos: presencia física (RF-044) y confirmación de preparación (RF-045). Se declara | 0 |
| 7 | CU-PE-04 (tercera transacción), CU-VE-09 (primera) | El cobro capturado y el registro de la venta digital | Autoridades distintas: pedidos captura y ventas registra. Se declara | 0 |
| 8 | CU-PE-08, CU-VE-02 | Anular una preautorización y reversar un pago | Antes de la captura es de pedidos y después es de ventas | 0 |
| 9 | CU-VE-02 (segunda transacción), CU-VE-10 (primera) | Documento ante el ERP/DTE | VE-10 emite las ventas nuevas. VE-02 solo ajusta el documento de una reversa | 0 |
| 10 | CU-VE-04 (tercera transacción), CU-VE-10 (segunda) | Documento en contingencia con folios previos | VE-10 entrega los folios y VE-04 los usa en la venta. VE-04 ya es simple, así que fundirlos no cambia su clase | 0 |
| 11 | CU-VE-07, CU-OR-07, CU-OR-08 | Autorizar compra a cuotas sin conexión | Es la sensibilidad de EXC-16: si falla la prueba de factibilidad se retiran los tres casos. CU-VE-11 se mantiene, porque EXC-16 permite autorizar la compra con cupo vigente | −15 si se retiran |
| 12 | CU-VE-11, CU-CC-01, CU-CC-03 | Autorización de cruce Crédito a Ventas | Se cuenta una sola vez, en CU-VE-11 (supuesto 1 de control de cruces) | 0 |
| 13 | CU-CA-02, CU-EV-03 (segunda), CU-EV-07 | Compuerta de evidencia para repactar | La consulta de evidencia se cuenta en EV-03. CA-02 y EV-07 solo la usan (resultado 18) | 0 |
| 14 | CU-OR-01 (tercera), CU-EV-01 (segunda) | Acreditar la evidencia antes de abrir la tarjeta | OR-01 confirma la apertura y EV-01 acredita la entrega de información. Se declara | 0 |
| 15 | CU-CC-02 (primera), CU-CL-03 (primera) | Segmentos y campañas sin atributos financieros | El rechazo se cuenta en CC-02. CL-03 solo construye el segmento comercial | 0 |
| 16 | CU-CC-06, CU-BT-13 (tercera) | Aprobar un conjunto de datos que mezcla ámbitos | La aprobación se cuenta en CC-06 y BT-13 solo la solicita | 0 |
| 17 | CU-BT-07, CU-EX-16, CU-EX-17, CU-PE-14, CU-VE-08 | Degradación del evento anual | BT-07 declara el orden. Los otros cuatro lo ejecutan en su servicio (RF-179 a RF-183) | 0 |
| 18 | CU-EX-18, CU-AB-04, CU-AB-05, CU-BT-09 | Movimientos de almacén, transferencias y recepciones | EX-18 recibe movimientos del WMS. AB-04 y AB-05 son las decisiones y el registro de tienda. BT-09 es solo la convivencia con el sistema de 2009 | 0 |
| 19 | CU-EX-19, CU-AB-05, CU-PE-01 | Concepción | Las existencias de Concepción se cargan solo en EX-19 (RC-10). AB-05 no incluye Concepción y PE-01 la excluye como origen de promesa (SP-02) | 0 |
| 20 | CU-CM-01, CU-MK-10 | Base de comisión | CM-01 es la comisión de la venta propia entre canales. MK-10 es la de marketplace al ERP | 0 |
| 21 | CU-MK-07, CU-PV-01, CU-PV-04 | Devolución y garantía | MK-07 registra costo y prestación de marketplace. PV-04 reingresa la unidad devuelta. PV-01 atiende la garantía en el mesón | 0 |
| 22 | CU-PE-10, CU-PE-11, CU-PE-12, CU-MK-03 (primera) | Consulta del estado del pedido | Misma fuente única (resultado 10), con distinto actor y distinto detalle. Se declara | 0 |
| 23 | CU-MK-08, CU-OF-03, CU-EX-02 | Datos de la ficha de producto y de la compra | Cada uno entrega un dato distinto (vendedor y condiciones, precio, disponibilidad). Se declara | 0 |
| 24 | CU-BT-13, CU-EX-12, CU-EX-14 | Tableros e informes de existencias | BT-13 es la capacidad común y EX-12 y EX-14 son los informes propios del servicio | 0 |
| 25 | CU-PE-01 (segunda transacción), CU-PE-03 (primera) | Aceptar el pedido | PE-01 confirma la promesa y PE-03 preautoriza el pago. Son dos idas y vueltas con distinto destino | 0 |
| 26 | CU-VE-01 (tercera transacción), CU-VE-11 (segunda) | Cerrar la venta | VE-11 cierra la venta con la autorización del Emisor y VE-01 confirma las demás ventas. Se cuenta una sola vez por venta | 0 |

## 3. Resultado

- Ningún traslape exige corregir un caso. Los 26 quedan declarados con su frontera.
- Los traslapes 3 y 4 tocan los dos casos medios que quedan (CU-OF-02 y CU-EX-04). Si el equipo decide fundir esas transacciones, el UUCW baja de 645 a 635 como máximo (−10).
- El traslape 11 es la sensibilidad de EXC-16 (−15 si no resulta factible).
- Los demás tienen efecto 0 porque los casos involucrados son simples.
