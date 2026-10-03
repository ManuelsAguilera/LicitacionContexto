# Escenarios de flujo con interacción entre actores

## Propósito

Identificar procesos del caso que sirven como candidatos a diagramas de interacción. Este documento es material de análisis: no redefine el catálogo ni agrega requerimientos. Los pasos describen el flujo a nivel de negocio; canales, servicios y sistemas deben representarse en carriles separados de los actores humanos o externos.

## Candidatos

### F-01 · Pedido digital con retiro en tienda

- **Actores:** cliente; personal de tienda que entrega el pedido.
- **Flujo simple:** cliente realiza el pedido → la tienda recibe la preparación → cliente retira y la tienda confirma la entrega.
- **Sistemas relacionados:** canal digital, C-03 Pedido y cumplimiento omnicanal, C-02 Inventario y disponibilidad.
- **Interés para el diagrama:** muy claro y acotado; muestra la transición entre canal digital y tienda.
- **Base:** Caso 09, numerales 4.6 y 9.4; glosario “Retiro en tienda”.

### F-02 · Pedido digital despachado desde una tienda

- **Actores:** cliente; personal de tienda que prepara el pedido; transportista.
- **Flujo simple:** cliente compra → tienda prepara y entrega el paquete → transportista lo lleva al cliente.
- **Sistemas relacionados:** canal digital, C-03, C-02 y seguimiento de transporte.
- **Interés para el diagrama:** representa tres interacciones externas y el cumplimiento omnicanal sin entrar en excepciones.
- **Base:** Caso 09, numerales 4.6, 9.4 y 15.1; glosario “Despacho desde tienda”.

### F-03 · Devolución de una compra marketplace en tienda

- **Actores:** cliente; personal de atención/tienda; vendedor marketplace.
- **Flujo simple:** cliente entrega el producto en tienda → tienda registra y recibe la devolución → Ancoa resuelve frente al cliente y notifica al vendedor.
- **Sistemas relacionados:** C-07 Posventa, garantías y devoluciones; C-06 Gobierno e integración de vendedores; C-02 si el producto vuelve a inventario.
- **Interés para el diagrama:** evidencia que Ancoa atiende al cliente directamente y que la coordinación con el vendedor es un flujo posterior, no una derivación del consumidor.
- **Base:** Caso 09, numerales 4.8 y 9.6; RT-16.21 y RT-16.30; catálogo de servicios, límites de C-06/C-07.

### F-04 · Venta presencial con inventario compartido

- **Actores:** cliente; vendedor o cajero.
- **Flujo simple:** cliente solicita producto → vendedor confirma disponibilidad y precio → cajero registra la venta y entrega comprobante.
- **Sistemas relacionados:** POS/canal de tienda, C-01 Oferta comercial, C-02 Inventario y C-04 Registro y conciliación de ventas; ERP/DTE externo según corresponda.
- **Interés para el diagrama:** explica el camino básico de una venta, aunque tiene menos interacción entre actores que F-02/F-03.
- **Base:** Caso 09, numerales 2.2, 4.3 y 9.1.

### F-05 · Originación de crédito en mesón financiero

- **Actores:** cliente/deudor; ejecutivo financiero; operación/riesgo del Emisor.
- **Flujo simple:** cliente solicita crédito → ejecutivo entrega información y recoge antecedentes/consentimiento → Emisor evalúa y comunica la decisión.
- **Sistemas relacionados:** C-08 Originación y autorización de crédito; C-09 Consentimiento y evidencia financiera.
- **Interés para el diagrama:** adecuado para mostrar el límite separado del Emisor y la evidencia previa a contratar. Mantenerlo independiente del flujo Retail.
- **Base:** Caso 09, numerales 4.9 y 9.7; RT-03.10 y RT-03.13.

### F-06 · Repactación de deuda

- **Actores:** titular/deudor; ejecutivo de cobranza; Emisor.
- **Flujo simple:** Emisor contacta al titular → titular revisa una propuesta y acepta o rechaza → Emisor registra el resultado y conserva evidencia.
- **Sistemas relacionados:** C-08 y C-09; canal de cobranza como medio de contacto.
- **Interés para el diagrama:** útil para representar consentimiento informado y trazabilidad de una modificación contractual.
- **Base:** Caso 09, numerales 4.10 y 9.8; glosario “Repactación”.

### F-07 · Recepción de mercadería y actualización de existencias

- **Actores:** proveedor/transportista que entrega; personal de recepción de tienda o centro de distribución; reposición/logística.
- **Flujo simple:** llega mercadería → recepción verifica y registra diferencias → inventario actualizado queda disponible para la operación.
- **Sistemas relacionados:** C-02; WMS donde exista; registro operacional aprobado donde hoy se usan planillas.
- **Interés para el diagrama:** muestra cómo una operación física actualiza disponibilidad confiable, sin detallar el proceso completo de abastecimiento.
- **Base:** Caso 09, numerales 4.3 y 5.1; RT-05.20 y RT-05.21.

### F-08 · Venta durante una interrupción de conectividad y conciliación

- **Actores:** cliente; cajero; jefatura/finanzas retail.
- **Flujo simple:** cajero registra la venta en modo de continuidad permitido → al volver la conexión se transmite el registro → finanzas/jefatura revisa la conciliación.
- **Sistemas relacionados:** POS con componente local, C-04 y sistema autorizado de documentos tributarios.
- **Interés para el diagrama:** permite mostrar la continuidad y la conciliación posterior. No debe incluir originación de crédito nuevo sin conexión.
- **Base:** Caso 09, numeral 9.1; RT-03.10; catálogo de servicios, límite de C-04/C-08.

## Recomendación

Priorizar **F-02 · Pedido digital despachado desde una tienda** para el primer diagrama: se entiende rápido, involucra tres actores y muestra el paso por preparación y entrega. Si el objetivo principal es explicar una responsabilidad difícil de distinguir, escoger **F-03**, porque hace visible la atención directa de Ancoa al cliente y la coordinación posterior con el vendedor marketplace.

Para mantener el diagrama legible, representar solo el camino normal de un caso, usar verbos breves en las flechas y limitarlo a tres o cuatro actores. Dejar quiebres de stock, reintentos, conciliaciones y otros caminos alternativos para diagramas aparte. Los nombres C-01…C-10 identifican servicios candidatos, no actores.

## Fuentes del repositorio

- `00_Bases/Caso_09_Cadena_Multitienda.md`
- `00_Bases/Bases_Transversales.md`
- `80_Artefactos/catalogo_servicios_candidatos_11.md`
