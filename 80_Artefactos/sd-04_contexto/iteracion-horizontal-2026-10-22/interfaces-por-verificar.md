# Inventario de interfaces por verificar

El caso describe catorce interfaces punto a punto de nueve plataformas y seis proveedores. No aporta una identificación fiable de cada enlace. Los siguientes son espacios de investigación, no catorce contratos identificados ni nuevos requisitos. Los códigos AS del contexto no se usan como equivalencia automática.

| Espacio | Origen y dueño | Destino y dueño | Contrato, datos y frecuencia | Evidencia | Estado |
|---|---|---|---|---|---|
| I-01 | Por levantar | Por levantar | Por levantar | Sin evidencia del enlace individual | Por verificar |
| I-02 | Por levantar | Por levantar | Por levantar | Sin evidencia del enlace individual | Por verificar |
| I-03 | Por levantar | Por levantar | Por levantar | Sin evidencia del enlace individual | Por verificar |
| I-04 | Por levantar | Por levantar | Por levantar | Sin evidencia del enlace individual | Por verificar |
| I-05 | Por levantar | Por levantar | Por levantar | Sin evidencia del enlace individual | Por verificar |
| I-06 | Por levantar | Por levantar | Por levantar | Sin evidencia del enlace individual | Por verificar |
| I-07 | Por levantar | Por levantar | Por levantar | Sin evidencia del enlace individual | Por verificar |
| I-08 | Por levantar | Por levantar | Por levantar | Sin evidencia del enlace individual | Por verificar |
| I-09 | Por levantar | Por levantar | Por levantar | Sin evidencia del enlace individual | Por verificar |
| I-10 | Por levantar | Por levantar | Por levantar | Sin evidencia del enlace individual | Por verificar |
| I-11 | Por levantar | Por levantar | Por levantar | Sin evidencia del enlace individual | Por verificar |
| I-12 | Por levantar | Por levantar | Por levantar | Sin evidencia del enlace individual | Por verificar |
| I-13 | Por levantar | Por levantar | Por levantar | Sin evidencia del enlace individual | Por verificar |
| I-14 | Por levantar | Por levantar | Por levantar | Sin evidencia del enlace individual | Por verificar |

Para cerrar cada fila: nombre y versión de ambos productos, proveedor/responsable, propósito, autoridad de datos, protocolo/endpoint, autenticación, red, dirección, esquema/versionado, PII/datos financieros, frecuencia/volumen y pico, timeout/reintentos/idempotencia, errores/DLQ, conciliación, SLA, retención, ambiente de prueba, dependencia contractual y ola de migración. Obtener inventario de proveedores, trazas/configuraciones autorizadas y validación de ambos responsables; un nombre de sistema no demuestra un enlace.

## Familias objetivo de la figura

| Adaptador propio | Contrapartes externas conocidas | Incertidumbre |
|---|---|---|
| Comercio | ERP/DTE y WMS conservados | Separar contratos y autoridad por plataforma; ninguna API concreta acreditada |
| Canales | E-commerce, marketplace y fidelización conservados | Inventariar sincronización actual y coexistencia; servicio Marketplace no reemplaza plataforma |
| Socios | Pagos, proveedores y transportistas | Marcas/endpoints pendientes; lockers y publicidad tienen necesidades propias por precisar |
| Crédito | Plataforma 2011 en convivencia; reportes CMF y firma | Migración financiera, rol regulatorio e interfaces de contraparte pendientes |

Una familia puede contener varios contratos; el dibujo agrupa para legibilidad y no fija su número. Los eventos internos tienen inventario propio: VentaConfirmada, PrecioPublicado, MovimientoInventario, DevoluciónAceptada, PedidoCambiado y hechos financieros son nombres de trabajo, pendientes del dueño. No se declaran contratos publicados por inventarlos en esta lista. X-01 mantiene un inventario aparte de solicitudes mínimas y respuestas autorizadas; no habilita un bus entre Retail y Filial.
