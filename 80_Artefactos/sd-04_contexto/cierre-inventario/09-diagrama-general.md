# Diagrama físico general 4.52 — matriz ampliada

Fecha: 23-10-2026. Estado: diseño para revisión. Uso de IA Alto.

La entrega vigente usa una vista única ampliada con 46 nodos y 51 conexiones. Los actores Retail y Filial están separados, los dispositivos se alinean con LAN, SD-WAN, VPN/firewall, gateways, AKS, datos y DR. OSI orienta la lectura sin crear bandas. Cada marco representa un sitio o segmento; colores, nombres VLAN/VRF y reglas distinguen los dominios.

La revisión por zonas sigue la nueva referencia visual del usuario: cliente y administración arriba, nube Azure en el bloque central y sitios Ancoa debajo. Dentro de la nube, el borde está a la izquierda, Retail y Filial ocupan bloques paralelos, los hubs quedan junto a sus enlaces de sitio y Brazil South aparece a la derecha. Se conservan los 46 nodos, 51 conexiones, iconos y tamaños de texto. Las coordenadas CSV y las rutas del editable se actualizan conjuntamente. La matriz compacta anterior se conserva como respaldo en `tmp/diagrama52-matriz-previa/` para comparación; la fuente vigente sigue siendo la figura 4.52.

Archivos: [PNG](../../../04_Adjuntos/diagramas/diag-04-52_fisica-general-inventario.png), [SVG](../../../04_Adjuntos/diagramas/diag-04-52_fisica-general-inventario.svg), [draw.io](../../../04_Adjuntos/diagramas/diag-04-52_fisica-general-inventario.drawio), [JSON semántico](../../../04_Adjuntos/diagramas/diag-04-52_fisica-general-inventario.json), [CSV de nodos](../../../04_Adjuntos/diagramas/diag-04-52_csv/nodos.csv), [CSV de conexiones](../../../04_Adjuntos/diagramas/diag-04-52_csv/conexiones.csv), [CSV de zonas](../../../04_Adjuntos/diagramas/diag-04-52_csv/zonas.csv) y [verificación](../../../04_Adjuntos/diagramas/diag-04-52_fisica-general-inventario.verificacion.json).

El usuario autorizó una sola vista ampliada, la paleta y símbolos Cisco. El validador original F1 rechaza 46 nodos porque su máximo es 30; esta entrega registra esa excepción y no afirma conformidad con ese límite. Las posiciones y estilos se conservan en CSV, draw.io y layout.json. El JSON refleja la topología y familias de iconos. Los iconos Cisco/Azure se mantienen; G, ATS y PDU son símbolos eléctricos esquemáticos sin marca. No son saltos IP.

La [ficha 13](13-matriz-red-y-diagrama.md) explica las reglas, el generador y la comprobación geométrica. Se obtuvieron cero rutas sobre iconos/nombres/cabeceras, cero diagonales y cero pares de rutas con coincidencia superior a 80 unidades. La imagen se inspeccionó; la validez gráfica no acredita despliegue, capacidad ni aplicación de ACL. [La matriz de suministro](12-matriz-suministro-costos.md) completa las partidas y sus responsabilidades.

Los pools AKS y los recursos DR continúan agrupados en la general; sus nodos y capacidades están en las fichas A/G. X-01 local permanece aislado en el par Filial, con identidad y bitácora propias, sin quinto host. Los DC/CD representan sistemas conservados e integración; no añaden producción financiera local.

Esta versión sustituye las iteraciones resumidas 4.48/4.52, sin modificar el subdocumento LaTeX. Registrar uso de IA Alto en Tabla 4.17 al incorporarla.
