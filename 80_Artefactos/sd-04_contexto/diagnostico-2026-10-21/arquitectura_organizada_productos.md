# Arquitectura por capas y productos de plataforma — figura 4.25

Estado: borrador para revisión humana. Reorganización solicitada desde la referencia visual `codex-clipboard-7a1c1381-731b-47de-a702-f16029810377.png`. No modifica SD-03 ni inserta todavía figuras en LaTeX. Sustituye como vista de revisión las figuras 4.23 y 4.24.

## Organización y contenido

- Actores externos a las ocho capas; no se denomina capa Cliente.
- Columnas separadas: 1 Presentación, 2 Borde y Exposición, 3 Puerta de enlace de servicios, 4 Servicios de negocio, 5 Integración y Eventos, 6 Datos. Seguridad y Observabilidad son las bandas 7 y 8.
- Retail y Emisor mantienen autoridad, productos, credenciales y datos separados. El control de cruces usa tarjeta gris y repositorio propio; sin franja amarilla ni códigos visibles.
- Se conservan las 13 autoridades funcionales y las cinco innovaciones. Los iconos de AKS identifican alojamiento y adaptadores; no añaden servicios funcionales. Los repositorios Retail agrupan contextos sin conceder acceso cruzado entre servicios.
- Se reemplazan rótulos genéricos de función por nombres e iconos de los productos propuestos: Azure Front Door Premium, Application Gateway v2, API Management Premium, AKS, Event Hubs Premium, PostgreSQL, Managed Redis, Data Lake Storage Gen2, Power BI, Entra ID P2, Key Vault Premium, Managed HSM, Firewall Premium, DDoS Protection, OpenTelemetry, Azure Monitor y Network Watcher. Los asteriscos conservan selecciones por verificar; no certifican disponibilidad regional ni despliegue.
- Las dos tarjetas Front Door son rutas del mismo perfil global, conforme al inventario de SD-04. Application Gateway y API Management siguen separados por ámbito.
- La API del vendedor externo reproduce el canal de la tabla 4.1 de SD-04; no se introduce un portal nuevo.
- Las conexiones de persistencia son directas. El canal de eventos conserva productores y consumidores por ámbito. Los conectores tienen puertos de borde y recorridos ortogonales iguales en SVG y draw.io. Las familias externas se enumeran en Adaptadores y en la banda de sistemas para evitar líneas largas a través de otro ámbito.

La selección se contrastó con la instantánea de SD-04 de `main@1e097c2`, especialmente tabla 4.1, descripción de capas y tabla 4.13 de recursos, guardada en `fuentes/sd04.txt`. Los nombres de eventos, contratos detallados, dimensionamiento y residencia siguen los pendientes del diagnóstico; esta figura no los cierra.

## Iconos

Los iconos Azure proceden del catálogo local `diagrams`, incorporados como PNG en SVG/draw.io. OpenTelemetry usa [el icono oficial del repositorio CNCF artwork](https://github.com/cncf/artwork/tree/main/projects/opentelemetry), sujeto a su política de marcas. Managed HSM se representa con el icono de familia Key Vault y su nombre explícito, sin afirmar que ambos sean el mismo recurso. El icono Power BI se utiliza para la familia del producto, sin prescribir Power BI Embedded.

## Entrega

- [PNG de revisión](../../../04_Adjuntos/diagramas/diag-04-25_arquitectura-organizada-iconos.png)
- [SVG autocontenido](../../../04_Adjuntos/diagramas/diag-04-25_arquitectura-organizada-iconos.svg)
- [Fuente draw.io](../../../04_Adjuntos/diagramas/diag-04-25_arquitectura-organizada-iconos.drawio)
- [Especificación JSON](../../../04_Adjuntos/diagramas/diag-04-25_arquitectura-organizada-iconos.json)
- [Evidencia geométrica](../../../04_Adjuntos/diagramas/diag-04-25_arquitectura-organizada-iconos.rutas.json)

Generación mediante MCP local `diagramas-ancoa`, variante L2 `columnas_organizadas`. Validación sin errores ni avisos; revisión visual del PNG; comprobación geométrica de 59 conectores y de sus puntos en draw.io; harness de siete ejemplos válidos y 18 casos negativos. Los hashes de SD-03 permanecen iguales. Al incorporar la figura en la propuesta, registrar uso de IA de nivel Alto; no asignar estado revisado sin revisión humana.
