# Arquitectura física general por zonas

**Actualización:** la general de trabajo vigente es la [figura 4.52](../cierre-inventario/09-diagrama-general.md), consolidada después del inventario y de la decisión de cuatro hosts por tienda. Este documento conserva la iteración 4.48 como antecedente.

Fecha de actualización: 23-10-2026. Versión de trabajo: 4. Estado: borrador para revisar la vista general antes de desarrollar los detalles por zona. Uso de IA Alto. Sin revisión humana formal ni pruebas de infraestructura ejecutadas.

La vista sigue desde el cliente por Internet o el personal con dispositivos corporativos hasta las zonas de entrada, balanceo, ejecución y datos. Conserva la organización de la referencia aportada por el usuario, con iconos sin tarjetas individuales y nombres debajo. Los marcos delimitan nube, regiones, redes, clústeres, seguridad e instalaciones. La referencia de otro caso solo aporta disposición gráfica; no se trasladan sus componentes AWS ni sus decisiones de infraestructura.

## Entrega vigente

La figura de trabajo 4.48 es la única general vigente de esta iteración. La numeración no cambia el índice ni las fuentes LaTeX de SD-04. Los detalles iniciales con tarjetas se conservaron como borradores temporales y se retiraron de la entrega activa.

- [Imagen PNG](../../../04_Adjuntos/diagramas/diag-04-48_fisica-general-zonas.png).
- [SVG con iconos incorporados](../../../04_Adjuntos/diagramas/diag-04-48_fisica-general-zonas.svg).
- [Editable draw.io](../../../04_Adjuntos/diagramas/diag-04-48_fisica-general-zonas.drawio).
- [Especificación de contenido F1](../../../04_Adjuntos/diagramas/diag-04-48_fisica-general-zonas.json).
- [Inventario de componentes](inventario-servidores.md), [relaciones](relaciones.md), [decisiones nuevas](decisiones-2026-10-23.md) y [verificación](verificacion.json).

El draw.io conserva la disposición final de iconos y las rutas ajustadas. El JSON conserva componentes, agrupaciones y relaciones validados. El render automático original del catálogo utiliza tarjetas; volver a ejecutarlo sin conservar el ajuste del editable restablecería la presentación que el usuario descartó. La geometría final queda también en [geometria.json](geometria.json) y [geometria-editor.json](geometria-editor.json).

## Decisiones confirmadas de emplazamiento

El usuario confirmó producción de Retail y Filial en Chile Central y recuperación de ambos en Brazil South. Brasil ya no se marca como propuesto y la Filial ya no aparece con destino por definir. Esta instrucción prevalece sobre las notas de trabajo anteriores que conservaban esas ubicaciones como pendientes. Las políticas, configuración, retenciones, capacidad y pruebas de restauración siguen requiriendo desarrollo; eso no reabre la decisión de ubicación.

La separación se mantiene en ambos destinos. Una región común no implica una VNet, un clúster, una base de datos o un espacio de seguridad compartido entre Retail y Filial.

## Cómo se recorre la general

El cliente utiliza el perfil Front Door correspondiente a su canal, con WAF y un origen privado del ámbito. La conexión privada llega a Application Gateway. La ruta API continúa por APIM; la ruta web va al backend privado sin convertir el contenido web en una API de negocio. Ambas utilizan el balanceador interno y el Service/VIP autorizado del clúster para alcanzar los pods. El ILB es un recurso de red distinto de APIM y de AKS.

El personal de la empresa utiliza su red, firewall local y VPN del ámbito. El VPN Gateway correspondiente termina el túnel y el Azure Firewall aplica las rutas/políticas híbridas antes del acceso permitido. Los símbolos inferiores agrupan dispositivos y servidores de sitios; no asignan un solo equipo físico a todo Ancoa. Los nodos locales Retail conservan la venta y el diario; la custodia financiera local sigue aislada, con su política de cupo preautorizado y conciliación.

Los sistemas conservados Retail, como ERP/DTE y WMS, se comunican por su integración privada. El inventario y la apertura de cada sitio se desarrollarán en sus vistas particulares. La agrupación de la general no afirma que ERP y WMS residan en una sola máquina ni que el sistema financiero de convivencia se aloje en Retail.

Cada AKS se abre en un pool BIZ y una agrupación de pools técnicos. BIZ aloja servicios y frontend. La agrupación técnica comprende SYS, INT, STATE y OPS, con responsabilidades de sistema, adaptadores/trabajos, herramientas con estado y observabilidad. El siguiente nivel debe abrirlos en VMSS, nodos, zonas de disponibilidad, réplicas y almacenamiento. La general no presenta todos los pools técnicos como una sola VM ni fija asignación permanente de pods a nodos.

Los repositorios y PaaS se muestran fuera de las VNets de aplicación. Los extremos privados y su DNS permiten acceder a los recursos propios del ámbito, con permisos del propietario. El símbolo de Datos resume la persistencia y dependencias PaaS de la general; no transforma PostgreSQL, Service Bus y Storage en un producto común o un servidor compartido.

La compra con tarjeta propia parte de Ventas sobre BIZ Retail, pasa por X-01 y llega a la entrada financiera permitida. X-01 conserva una bitácora mínima propia. No se habilita acceso Retail a la base financiera ni un enlace entre buses. El candidato F:C-04 sigue sin servidor o despliegue aprobado.

## Seguridad que se hace visible

La vista incluye WAF en Front Door, firewalls propios de cada negocio, NSG, rutas UDR y políticas de red de Kubernetes asociadas a sus zonas. Los controles no se dibujan como proxies adicionales en serie.

La banda de seguridad muestra Entra ID/External ID, Key Vault, Managed HSM, Bastion y el workspace de Log Analytics asociado a Sentinel. Los productos conservan instancias y permisos propios por ámbito aunque la general use un símbolo por familia. El icono de Log Analytics identifica el workspace; no se declara que sea el icono nativo de Sentinel. El símbolo HSM del catálogo representa la familia de custodia; la vista de seguridad deberá precisar recurso y variantes.

Workload Identity, Intune y Defender for Cloud/Endpoint se conservan como controles transversales explícitos. Sus conexiones, agentes, planes y responsables se abrirán en la zona de seguridad. La colocación de esos nombres no acredita que estén contratados o configurados. La flecha hacia Bastion resume solo el acceso de un perfil administrativo autorizado; el dispositivo corporativo por sí solo no otorga ese privilegio.

## Referencias de contenido y dibujo

La fuente de alcance, autoridades y razones técnicas es la [explicación del diagrama lógico por columnas](../explicacion-diagrama-columnas-2026-10-23/README.md) con su registro FI01–FI11 y FT01–FT16. El alojamiento previo aporta la [matriz de despliegue](../revision-fisica-2026-10-22/matriz-despliegue.md), la [cobertura lógica a física](../revision-fisica-2026-10-22/cobertura-logica-fisica.md) y la [matriz de rutas](../revision-fisica-2026-10-22/rutas-puertos-y-segmentos.md). Las decisiones nuevas de esta conversación prevalecen sobre los pendientes de ubicación de esos antecedentes.

La guía oficial [Architecture design diagrams](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/design-diagrams) respalda el uso de flechas direccionales, rótulos claros, separación de vistas y representación correcta de servicios administrados respecto de subredes. La colección [Azure architecture icons](https://learn.microsoft.com/en-us/azure/architecture/icons/) indica usar iconos oficiales con nombres cercanos y conservar su forma. Ambas se consultaron el 23-10-2026. La disposición con iconos sin tarjetas responde a la instrucción expresa del usuario; no se atribuye a Microsoft una prohibición de tarjetas que su guía no establece.

El [ejemplo visual recibido](referencia-organizacion.png) conserva únicamente la referencia de organización y conectores. Su contenido y proveedor pertenecen a otro caso.

## Comprobaciones y siguiente iteración

La especificación F1 tiene 30 componentes y 35 relaciones, sin errores ni avisos del validador. El editable pasó el linter; los componentes se verificaron como iconos sin fondo ni borde de tarjeta. No se imprimen números de enlace. Las rutas conservan extremos y coordenadas en el motor draw.io y no atraviesan iconos, nombres ni cabeceras. El SVG incorpora sus imágenes sin depender de URLs de iconos al abrirlo.

Estas comprobaciones son documentales y gráficas. No acreditan capacidad ni despliegue. El siguiente paso será ajustar esta general con el equipo y después abrir cada zona con sus servidores, redes, seguridad y rutas de recuperación, manteniendo el estilo de iconos adoptado.

La asistencia de Codex fue de nivel Alto en texto y diagramas. Registrar ese nivel en la Tabla 4.17 cuando se incorpore la figura a SD-04. Esta entrega no cambia requisitos, plantilla corporativa o subdocumentos LaTeX y no asigna estado revisado.
