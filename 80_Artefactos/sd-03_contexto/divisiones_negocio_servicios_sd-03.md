# Nomenclatura vigente del sd-03 (frentes, áreas y servicios)

Documento de contexto, no es entregable. Fecha: 2026-10-07. Fija los nombres y códigos que usa `02_Propuesta/latex_final/sd-03.tex` y los que deben usar los demás subdocumentos (RR-07). Si un documento de esta carpeta usa un nombre o código distinto (por ejemplo «R-01» o «Catálogo, precios y promociones»), manda este archivo.

## Por qué cambió

Los nombres anteriores eran compuestos con comas y «y» («Catálogo, precios y promociones») y casi repetían el nombre de la responsabilidad de negocio de la que salían, por lo que dos niveles de la descomposición decían lo mismo. Ahora cada nivel dice algo distinto y cada servicio se llama con un solo sustantivo. La clase FEP01 · 34 describe un servicio como una unidad que implementa una sola capacidad del negocio, con despliegue independiente y contratos estables.

## Definiciones

- **Frente.** Parte del problema que responde a un mismo régimen jurídico y de datos. Son tres: retail, filial emisora y frontera.
- **Área.** Sección o división del negocio a la que el servicio pertenece. El frente de frontera no tiene áreas y se conecta directamente con su servicio.
- **Servicio.** Pieza del sistema que se ocupa de un solo tema del negocio, como los pedidos o la cartera de crédito. Es la única autorizada para registrar y corregir la información de ese tema, y las demás piezas la consultan. Es la definición para el lector del documento. En términos técnicos (3.3 y 3.4) es una unidad de software independiente, dueña exclusiva de un conjunto de datos, que los expone solo mediante contratos definidos. Se llama con un solo sustantivo, el del tema del que es dueño.
- **Base tecnológica** (antes «plataforma común»). Plataforma de integración, identidad y gestión de accesos y observabilidad. Conecta los servicios entre sí, controla quién accede a qué y permite vigilar su funcionamiento. No pertenece a ningún negocio y no es un servicio de negocio. El despliegue híbrido es una decisión de arquitectura y se trata en la 3.3, no es un componente de esta lista.
- **Código.** `frente:área-número`. Frente: `R` retail, `F` filial emisora, `X` frontera. Área: `M` mercadería, `V` venta, `CL` relación con el cliente, `C` crédito. La frontera no lleva área.

## Jerarquía y equivalencias

| Frente | Área | Código nuevo | Servicio (nombre vigente) | Código anterior | Nombre anterior |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Retail | Mercadería | R:M-01 | Servicio de oferta comercial | R-01 | Catálogo, precios y promociones |
| Retail | Mercadería | R:M-02 | Servicio de abastecimiento | R-02 | Abastecimiento y reposición |
| Retail | Mercadería | R:M-03 | Servicio de existencias | R-03 | Inventario, reservas y disponibilidad |
| Retail | Venta | R:V-01 | Servicio de pedidos | R-04 | Pedidos y cumplimiento omnicanal |
| Retail | Venta | R:V-02 | Servicio de ventas | R-05 | Registro y conciliación de ventas |
| Retail | Venta | R:V-03 | Servicio de comisiones | R-06 | Atribución de ventas y comisiones |
| Retail | Venta | R:V-04 | Servicio de marketplace | R-07 | Integración y gobierno del marketplace |
| Retail | Relación con el cliente | R:CL-01 | Servicio de posventa | R-08 | Posventa, garantías y devoluciones |
| Retail | Relación con el cliente | R:CL-02 | Servicio de clientes Retail | R-09 | Clientes y fidelización Retail |
| Filial emisora | Crédito | F:C-01 | Servicio de originación de crédito | F-01 | Originación y autorización de crédito |
| Filial emisora | Crédito | F:C-02 | Servicio de cartera de crédito | F-02 | Cartera, cobranza y repactaciones |
| Filial emisora | Crédito | F:C-03 | Servicio de evidencia financiera | F-03 | Consentimiento y evidencia financiera |
| Frontera | (sin área) | X-01 | Servicio de control de cruces | X-01 | Autorización y auditoría de cruces Retail–Emisor |

## Qué incluye cada servicio

Lo que el nombre anterior enumeraba ahora se describe aquí, no en el nombre.

| Servicio | Qué incluye |
| :-- | :-- |
| Servicio de oferta comercial | Maestro de artículos, precios, promociones, vigencias, canales y estado de la etiqueta |
| Servicio de abastecimiento | Órdenes, transferencias, recepciones y propuestas de reposición |
| Servicio de existencias | Existencias por tienda y centro de distribución, conteos, reservas y disponibilidad para vender |
| Servicio de pedidos | Ciclo del pedido en los cuatro canales, nodo de preparación, promesa de entrega, despacho y retiro |
| Servicio de ventas | Registro y conciliación de la venta, su reversa, el pago, la caja y las ventas sin conexión |
| Servicio de comisiones | Atribución de la venta al vendedor y al canal, y base de la comisión |
| Servicio de marketplace | Integración y gobierno de vendedores, ofertas, nivel de servicio, devoluciones y liquidación |
| Servicio de posventa | Casos, inspección, cambios, notas de crédito y garantía |
| Servicio de clientes Retail | Identificación y deduplicación de clientes, y gobierno de los datos de puntos, segmentos y campañas. El sistema de fidelización de 2017 se mantiene y se integra a este servicio (EXC-15) |
| Servicio de originación de crédito | Solicitud, evaluación, cupo, decisión y autorización |
| Servicio de cartera de crédito | Cuenta, saldo, cuotas, pagos, mora, cobranza y repactación |
| Servicio de evidencia financiera | Información precontractual entregada, aceptación, consentimiento y expediente recuperable |
| Servicio de control de cruces | Autorización, minimización y auditoría de cada uso de datos de un negocio por el otro |

## Correspondencia con las responsabilidades de negocio anteriores

Las quince responsabilidades (A1 a A10 de retail, B1 a B3 de la filial emisora, C1 y C2 de frontera) dejan de ser un nivel de la descomposición. Su contenido queda cubierto así.

| Responsabilidad anterior | Servicio que la cumple |
| :-- | :-- |
| A1 catálogo y oferta, A2 precios y promociones | R:M-01 |
| A3 abastecimiento y reposición | R:M-02 |
| A4 inventario, reservas y disponibilidad | R:M-03 |
| A6 canales digitales, A7 pedidos y cumplimiento | R:V-01 |
| A5 venta y conciliación | R:V-02 y R:V-03 (la atribución) |
| A8 marketplace | R:V-04 |
| A9 posventa, cambios y garantías | R:CL-01 |
| A10 clientes y fidelización | R:CL-02 |
| B1 originación y autorización | F:C-01 |
| B2 cartera y cobranza, B3 repactaciones | F:C-02 |
| C1 separación y gobierno de datos | X-01 |
| C2 evidencia y trazabilidad probatoria | F:C-03 y X-01 |

A11 (alta demanda) es un escenario de prueba, no una responsabilidad. La responsabilidad anterior C3 (integración, plataforma y operación técnica) es la base tecnológica.

## Reglas de uso

- En el texto del sd-03 se escribe siempre «Servicio de …» con el nombre vigente. Los códigos se usan en tablas de trazabilidad y no en la prosa.
- Los códigos anteriores (R-01 a X-01) y los nombres anteriores solo se encuentran en los demás archivos de esta carpeta, que no se reescribieron. Se leen con la tabla de equivalencias de arriba.
- «Causa C1» a «causa C5» son las causas raíz del sd-02. El código `F:C-01` usa la C de crédito y no tiene relación con ellas.
