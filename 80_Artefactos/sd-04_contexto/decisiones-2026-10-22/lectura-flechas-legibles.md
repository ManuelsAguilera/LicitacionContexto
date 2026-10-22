# Figura 4.28: lectura de las rutas y separación lógica/física

Versión del 22-10-2026, para revisión del equipo. Sustituye la figura 4.27 como vista general de lectura. Conserva sus decisiones y pendientes, con las aclaraciones de este archivo. SD-03 y SD-04 no se editaron.

## Símbolos de los productos de entrada

Front Door, Application Gateway, API Management y API Center aparecen una sola vez cada uno. El registro recibido declara dos perfiles/instancias en total por producto, uno para cada ámbito: su cierre de capa 3 dice «App Gateway ×2, APIM Premium clásico ×2, API Center ×2» y D-18 especifica un API Center por ámbito. SD-04, línea 392, también selecciona una instancia de APIM por ámbito.

Por tanto, esta revisión elimina la duplicación **visual**, sin adoptar una única instancia compartida. Las etiquetas conservan Retail/Filial separados. Si el equipo decide compartir un recurso real, eso requiere otra decisión sobre aislamiento, identidad, conectividad, operación y residencia; no se deduce del número de iconos.

## Cómo se limpiaron las flechas

- Los contratos de API, persistencia y publicación se agrupan en el contorno de Mercadería, Venta, Relación con el cliente y Crédito.
- Las áreas son agrupaciones funcionales. No son routers, nuevas bases ni servicios intermediarios. Cada servicio conserva la escritura y los contratos que le corresponden.
- Los recorridos utilizan puertos de borde y codos; el trazado evita tarjetas y títulos. Las líneas de distintas familias se separan cuando el espacio lo permite.
- Se corrigió el obstáculo del título de operación sin enlace: antes bloqueaba el carril de integración y obligaba al consumo de cambios de oferta a rodear toda la capa de datos.
- El control X-01 mantiene su recorrido explícito y el transporte de eventos conserva buses separados. Las conexiones del símbolo agregado de APIM están condicionadas al ámbito, producto e identidad de cada llamada.
- API Center tiene un enlace de gobierno de contratos mediante pipeline. No es un salto adicional de las peticiones de negocio.

La vista pasa de 87 relaciones dibujadas a 63 familias de relaciones. Los trece servicios y las cinco innovaciones se conservan. El [inventario de la figura 4.27](inventario-conectividad.md) mantiene el detalle de referencia anterior a la agrupación; no debe confundirse la ausencia de una flecha individual en esta vista con la eliminación de ese contrato.

## Continuidad: funciones lógicas y despliegue físico

La arquitectura lógica debe mostrar qué hace el software cuando se interrumpe la conectividad. El equipo que ejecuta esas funciones se documenta en la vista física.

| Capa | Responsabilidad lógica conservada | Detalle que corresponde a la física |
| :--- | :--- | :--- |
| Servicios | Operación de tienda sin enlace: venta y consulta de oferta vigente. | Servidor, nodo local, clúster, capacidad e instalación. |
| Integración | Sincronización, reintentos y conciliación de operaciones. | Despliegue del proceso, alta disponibilidad y conectividad. |
| Datos Retail | Diario durable de operaciones pendientes. | Motor, discos, respaldo y réplica local. |
| Datos Filial | Consulta de cupo previamente autorizado, con datos mínimos y vigencia. | VM, red y claves de Filial; protección física. |

Se retiraron de esas tarjetas los iconos de servidor y las etiquetas de VM/on-premise. No se habilita apertura de crédito ni ampliación de cupo sin conexión. La separación de datos del Emisor permanece como restricción lógica aunque su implementación física se documente aparte.

Los productos Azure se mantienen como elecciones tecnológicas del software y la plataforma, conforme a la referencia solicitada. Esta figura no pretende ser un inventario de infraestructura ni un diagrama C4 puro de contenedores: es la vista L2 por ocho capas de la guía del proyecto.

El modelo C4 reserva el mapeo de instancias a servidores, VM y otros nodos de ejecución para el [diagrama de despliegue](https://c4model.com/diagrams/deployment). Su [vista de contenedores](https://c4model.com/diagrams/container) puede mostrar aplicaciones, almacenes, responsabilidades y tecnologías, dejando los detalles de despliegue para otra vista.

## Entrega y comprobaciones

- [Draw.io editable](../../../04_Adjuntos/diagramas/diag-04-28_arquitectura-flechas-legibles.drawio).
- [SVG ampliable](../../../04_Adjuntos/diagramas/diag-04-28_arquitectura-flechas-legibles.svg) y [PNG](../../../04_Adjuntos/diagramas/diag-04-28_arquitectura-flechas-legibles.png).
- [Especificación JSON](../../../04_Adjuntos/diagramas/diag-04-28_arquitectura-flechas-legibles.json).
- [Pendientes técnicos y documentales](revision-y-pendientes.md): siguen abiertos; el cambio de trazado no los resuelve.
- [Comprobaciones de esta revisión](comprobaciones-flechas.json).

La agrupación de una flecha por área explica una familia de contratos. Para revisar una secuencia o un servicio concreto deben usarse el inventario y las vistas de detalle; no se puede interpretar el dibujo como autorización de acceso a todos los destinos del producto agregado.
