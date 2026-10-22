# Franjas de capas y segmentación de red — figura 4.26

Estado: borrador para revisión humana. Revisión del 22-10-2026 solicitada por el usuario; sustituye visualmente la figura 4.25. No cambia SD-03 ni inserta figuras en LaTeX.

**Revisión posterior del usuario:** se elimina el bloque final de segmentación y el detalle visible de CIDR/subredes. La versión vigente mantiene las franjas de capas y distingue Retail y Emisor con red privada y suscripción propias. El detalle de este registro queda como antecedente del diseño de SD-04.

Entrega vigente: [PNG](../../../04_Adjuntos/diagramas/diag-04-26_capas-sin-bloque-segmentacion.png), [draw.io](../../../04_Adjuntos/diagramas/diag-04-26_capas-sin-bloque-segmentacion.drawio) y [SVG](../../../04_Adjuntos/diagramas/diag-04-26_capas-sin-bloque-segmentacion.svg). Validación, lint y revisión de los 59 conectores correctos; SD-03 intacto.

**Última revisión de presentación:** se agrupan Front Door, Application Gateway y API Management en un único símbolo por producto; las franjas de ámbito no atraviesan esas columnas. Se retiran las etiquetas extensas de división y el control de cruces se limita a negocio/integración para evitar rodeos artificiales. Se conservan las franjas Retail/Filial, los destinos propios y los 13 servicios funcionales. Es una abstracción gráfica, no una declaración de recursos o redes físicamente compartidos; el diseño de SD-04 permanece sin cambios.

Entrega más reciente: [PNG](../../../04_Adjuntos/diagramas/diag-04-26_borde-agrupado-franjas.png), [draw.io](../../../04_Adjuntos/diagramas/diag-04-26_borde-agrupado-franjas.drawio), [SVG](../../../04_Adjuntos/diagramas/diag-04-26_borde-agrupado-franjas.svg) y [JSON](../../../04_Adjuntos/diagramas/diag-04-26_borde-agrupado-franjas.json). Validación sin errores ni avisos; revisión visual, lint y comprobación de los 57 conectores correctos. Harness: siete ejemplos válidos y 18 rechazos esperados. SD-03 intacto.

**Revisión siguiente:** se retiran el nodo API de vendedor externo y el actor asociado de esta vista, conservando la plataforma marketplace y los adaptadores. No es una eliminación de alcance de SD-03. Entrega vigente: [draw.io](../../../04_Adjuntos/diagramas/diag-04-26_sin-api-vendedor.drawio) y [PNG](../../../04_Adjuntos/diagramas/diag-04-26_sin-api-vendedor.png), con 55 conectores.

La solicitud también pide explicar Front Door → Application Gateway → API Management. La cadena se conserva en la revisión gráfica mientras se explica su condición: SD-04 selecciona Premium clásico interno, que no admite el endpoint privado de entrada simultáneamente con la inyección en VNet. Application Gateway es el puente regional de entrada hacia ese APIM. La alternativa directa Front Door → APIM mediante Private Link exige validar otro modo de red o nivel, región y conectividad privada hacia AKS; no se aprueba por eliminar una caja. También deben distinguirse las llamadas API públicas, la entrega de la interfaz web y la entrada privada de tiendas; el diagrama actual aún no detalla esos tres recorridos. Fuentes verificadas: [Private endpoints de API Management](https://learn.microsoft.com/azure/api-management/private-endpoint), [protección con Application Gateway](https://learn.microsoft.com/en-us/azure/architecture/web-apps/api-management/architectures/protect-apis) y [Front Door hacia APIM por Private Link](https://learn.microsoft.com/en-us/azure/frontdoor/standard-premium/how-to-enable-private-link-apim).

**Decisión posterior aceptada por el usuario:** «agrega ese cambio», referido a la conexión directa privada. Se sustituye Application Gateway por un pequeño símbolo de Azure Private Link/Private Endpoint sobre el enlace Front Door → APIM. Este símbolo es conectividad administrada por Front Door, no otro gateway. APIM se rotula expresamente «Nivel y modo de red por validar», sin conservar la afirmación incompatible de Premium clásico interno ni prescribir v2 sin comprobación regional. Se mantienen 13 autoridades funcionales, cinco innovaciones y los ámbitos separados; SD-03 sigue intacto.

Entrega vigente: [draw.io](../../../04_Adjuntos/diagramas/diag-04-26_entrada-private-link.drawio), [PNG](../../../04_Adjuntos/diagramas/diag-04-26_entrada-private-link.png), [SVG](../../../04_Adjuntos/diagramas/diag-04-26_entrada-private-link.svg) y [JSON](../../../04_Adjuntos/diagramas/diag-04-26_entrada-private-link.json). Se preservan los anclajes de borde y los 55 conectores.

La modificación es una propuesta gráfica condicionada: quedan por validar el nivel/modo APIM, disponibilidad regional, salida privada a AKS, origen y configuración de recuperación en Brazil South y residencia de datos del Emisor. Su adopción debe conciliarse con ADR, SD-04 y T-11; no se han modificado los textos LaTeX ni se acredita una migración/despliegue. La distinción entre entrada de API pública, entrega de interfaz web y tráfico privado de tiendas sigue siendo detalle pendiente de esta vista.

## Franjas y límites

Los fondos tenues continuos delimitan las capas 1–6 desde sus encabezados hasta el final del cuerpo. Seguridad y Observabilidad tienen sus propias bandas horizontales 7–8. Los actores quedan fuera de las capas. Los fondos lógicos no son límites de VNet: Front Door es global, los componentes locales permanecen en tienda y los servicios PaaS se acceden por puntos privados sin atribuirles alojamiento físico en esas subredes.

## Redes declaradas

Se explicita el diseño de Producción ya contenido en SD-04, sección 4.2 y tabla 4.10, conservado en `fuentes/sd04.txt` desde `main@1e097c2`:

| Red distinta | Rango propuesto | Separación |
| --- | --- | --- |
| Hub | `10.10.0.0/22` | Suscripción de Conectividad y Azure Firewall Premium. |
| Retail | `10.10.16.0/20` | Suscripción propia; entrada `10.10.16.0/24`, API `10.10.17.0/28`, AKS `10.10.20.0/22`, acceso privado a datos `10.10.24.0/24`. |
| Filial emisora | `10.10.32.0/20` | Suscripción propia; entrada `10.10.32.0/24`, API `10.10.33.0/28`, AKS `10.10.36.0/22`, acceso privado a datos `10.10.40.0/24`. |
| Base tecnológica | `10.10.48.0/21` | Suscripción propia; aplicación `10.10.48.0/22` y subredes `10.10.52.0/24`, `10.10.53.0/24`, `10.10.54.0/24`. Control de cruces y adaptadores segregados por ámbito. |

Retail y Emisor no son subredes dentro de una red común: son VNets distintas, sin peering directo. Se declara denegación por defecto; solo se permite el cruce de compra aprobado por X-01 e inspeccionado en el hub. Las UDR, reglas de Firewall y NSG materializan la separación conforme a las excepciones de SD-04. Los rangos siguen sujetos a inventario de conectividad y los pendientes de residencia/recuperación del Emisor no quedan cerrados por esta figura.

El recuadro inferior identifica atributos de despliegue de esta vista lógica; no es una novena capa ni sustituye la topología física F2.

## Entrega y comprobación

- [PNG](../../../04_Adjuntos/diagramas/diag-04-26_arquitectura-capas-redes.png)
- [SVG](../../../04_Adjuntos/diagramas/diag-04-26_arquitectura-capas-redes.svg)
- [Draw.io editable](../../../04_Adjuntos/diagramas/diag-04-26_arquitectura-capas-redes.drawio)
- [JSON](../../../04_Adjuntos/diagramas/diag-04-26_arquitectura-capas-redes.json)
- [Rutas de conectores](../../../04_Adjuntos/diagramas/diag-04-26_arquitectura-capas-redes.rutas.json)

Generación por MCP local `diagramas-ancoa`. Validación sin errores ni avisos, revisión visual y comprobación de los 59 conectores, sus anclajes de borde y sus puntos iguales en SVG/draw.io. Se mantienen 13 autoridades funcionales, cinco innovaciones y los hashes de SD-03. Verificar el archivo draw.io con el lint y los ejemplos con el harness de la guía antes de entregar. No asignar estado revisado sin revisión humana; registrar uso de IA de nivel Alto al incorporar en la propuesta.
