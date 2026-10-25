# Cierre del inventario físico — índice de trabajo

Fecha: 23-10-2026. Estado: diseño consolidado con pruebas y datos del mandante pendientes. Uso de IA Alto. Sin revisión humana formal ni despliegue ejecutado.

| Entrega | Contenido |
| --- | --- |
| [A · Cómputo](01-computo-aks.md) | Pools, cargas, réplicas, cálculos y 54 VM de producción Chile. |
| [B · Red](02-red-cloud.md) | Segmentación R/F/X, reservas IP, rutas, entrada y acceso privado. |
| [C · Tienda](03-tienda.md) | Cuatro hosts por sitio, pares redundantes, X-01 local aislado y continuidad sin enlace. |
| [D · Datos](04-datos-custodia.md) | PostgreSQL, mensajería, almacenamiento, retenciones y custodia. |
| [E · DC/CD y externos](05-dc-cd-externos.md) | Sistemas conservados, convivencia, migración y levantamiento de hosts reales. |
| [F · Seguridad](06-seguridad-operacion.md) | Identidades, claves, administración, observabilidad y protección. |
| [G · Recuperación y ambientes](07-dr-ambientes.md) | Brasil, failover/failback y DEV/QA/PRE/entrega. |
| [H · Revisión cruzada](08-revision-cruzada.md) | 14 hallazgos; H-01/H-02 resueltos en diseño por decisión del usuario. |
| [Diagrama general](09-diagrama-general.md) | Figura 4.52, exportaciones e interpretación de agrupaciones. |

El [inventario maestro](../inventario-fisico-integral-2026-10-23.md) reúne las familias de recursos y conexiones; estas fichas contienen los cálculos y decisiones particulares vigentes. La capacidad inicial se ofrece bajo supuestos explícitos. Faltan mediciones, catálogo regional/cuotas, pruebas de carga/HA/DR, IPAM real, CMDB e interfaces del mandante. Esos datos no se presentan como levantados.

- [10 · Espacio y racks](10-espacio-racks.md): superficies acreditadas, unidades U, pasillos y reservas de sala.
- [11 · Soporte físico](11-soporte-fisico.md): red, UPS, generación, ambiente, seguridad física y deseables.
- [12 · Suministro y costos](12-matriz-suministro-costos.md): 32 partidas con responsabilidades, cantidades, CAPEX/OPEX y aceptación; también [CSV](12-matriz-suministro-costos.csv).
- [13 · Matriz de red y diagrama](13-matriz-red-y-diagrama.md): vista ampliada, reglas de segmentación, CSV de edición y comprobaciones.
