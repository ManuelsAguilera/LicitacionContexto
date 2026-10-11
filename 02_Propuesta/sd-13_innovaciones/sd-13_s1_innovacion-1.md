---
id: T7-13-13.1
tipo: seccion
parte: T7-13
titulo: Innovación 1
estado: borrador
bases:
  - "Bases Administrativas, artículos 28 a 30"
  - "Bases Transversales, RT-26.01 a RT-26.05"
requisitos: []
depende_de:
  - T7-03
  - T7-04
  - T7-07
adjuntos: []
jira: []
cifras:
  - produccion_etapa_2_mes
origen: "80_Artefactos/sd-13_contexto/investigacion_cinco_innovaciones.md, sección 2"
actualizado: 2026-10-11
---
## 13.1 Innovación 1

La innovación de producto o servicio es Lockers Ancoa 24/7. Agrega al retiro de compras un punto de entrega autónomo para pedidos preparados y pagados, accesible fuera del horario de atención de la tienda. El cliente recibe una credencial de retiro y utiliza el casillero sin pasar por el mesón. La promesa se aplica únicamente a emplazamientos con acceso público continuo y a paquetes compatibles con los compartimentos.

### Problema y beneficio para el cliente

El Caso documenta dificultades de cumplimiento de pedidos y coordinación de la tienda con el canal digital (Multitiendas Ancoa S.A., 2026b, caps. 7–9). Un pedido preparado sigue requiriendo una entrega física. El locker permite efectuar esa entrega sin sincronizar la llegada del cliente con la disponibilidad de un operador. Las cancelaciones causadas por stock incorrecto se atienden mediante el servicio de existencias; el retiro autónomo interviene después de verificar y preparar el pedido.

El levantamiento registra tiempos de atención en mesón, demanda de retiro fuera de horario, distribución de tamaños y permanencia de paquetes. Esos datos determinan la ubicación y configuración de cada batería. En recintos cuyo acceso cierra por la noche, la instalación exige un punto exterior accesible; la sola presencia de casilleros dentro del centro comercial no habilita la promesa 24/7.

### Tecnología y madurez

La solución utiliza gabinetes electrónicos con controlador, identificación de puerta y registro de apertura y cierre. Cleveron 355 constituye la referencia exterior para mercancía voluminosa; el fabricante documenta su uso a la intemperie y configuración modular. Cleveron 302 es interior y queda descartado para ese emplazamiento. Para paquetes pequeños se compara una configuración exterior de mayor densidad antes de fijar el suministro (Cleveron, s. f.-a, s. f.-b).

La integración utiliza el contrato del fabricante. Una alternativa documentada es la API REST sobre HTTPS de Bloq.it (s. f.). Su existencia demuestra una vía de integración, pero no acredita compatibilidad con gabinetes de otra marca. Only Simple Solutions exige una prueba de integración y disponibilidad de repuestos y soporte local antes de aprobar el equipo.

La madurez se evalúa con una escala de evidencia que distingue componente comercial documentado, integración probada y operación aceptada en Ancoa. El gabinete alcanza el primer estado por su documentación comercial. La credencial, la reconciliación y el proceso de entrega deben superar los otros dos estados mediante pruebas; la ficha no atribuye al conjunto un nivel de validación que aún no ha obtenido.

### Incorporación a arquitectura y EDT

Un adaptador en la capa de integración vincula el controlador con el servicio de pedidos. El servicio de existencias confirma la disponibilidad antes de la preparación. La confirmación del bulto cargado y de la puerta cerrada habilita el aviso al cliente. La aplicación registra reserva, carga, disponibilidad, retiro, vencimiento y bloqueo con identificadores que impiden duplicar la entrega.

El paquete «Lockers Ancoa 24/7» se ubica bajo la rama 1.10 Innovaciones del T-14. Incluye selección, emplazamiento, integración, ensayo y capacitación. Infraestructura, seguridad e implantación aportan sus entregables de las ramas habilitantes del capítulo 7. La entrega se acepta durante la marcha blanca de la Etapa 2 y se habilita desde el mes 21. El alcance por tienda se fija con el dimensionamiento, sin asumir una batería idéntica para toda la red.

### Impacto económico

La inversión comprende gabinetes, instalación, alimentación, comunicaciones y adaptación del servicio de pedidos. El costo operacional incluye soporte, repuestos, conectividad, licencias y asistencia ante fallas. El beneficio se calcula con el tiempo de entrega evitado y con el margen de pedidos adicionales atribuibles al horario ampliado. Se descuenta la carga y recuperación de bultos que continúa realizando personal de tienda. La Oferta Económica refleja estos componentes por paquete y período, sin duplicar los beneficios de mejora del inventario.

### Verificación del beneficio

La línea base se obtiene del retiro en mesón, bajo franjas de demanda comparables. Se miden tiempo total de retiro, minutos de personal por entrega, retiros sin asistencia, ocupación, vencimientos y fallas. La meta consiste en completar retiros autorizados fuera del horario de mesón y reducir el tiempo de atención por entrega respecto de la línea base, sin entregas a personas no autorizadas en las pruebas. El acta de diseño fija el umbral de mejora temporal después del levantamiento. Se evalúa en la marcha blanca y durante la operación desde el mes 21.

### Riesgo de adopción y contingencia

La valoración inicial del equipo asigna probabilidad media e impacto alto a la incompatibilidad de tamaños o a un emplazamiento inaccesible. La mitigación consiste en dimensionar por categoría, verificar acceso y ensayar con bultos reales. El retiro convencional atiende mercancías incompatibles.

Los fallos de autorización o conectividad tienen probabilidad media e impacto alto. Un teclado no acredita funcionamiento desconectado. La aceptación exige probar vigencia y consumo único de la credencial, recuperación después de reinicio y reconciliación de eventos. Cuando el controlador no puede verificar la autorización, suspende la apertura automática y activa asistencia. El plan de continuidad incorpora conectividad de respaldo y recuperación al mesón, sin comprometer apertura insegura. El T-16 revisa estas valoraciones con la evidencia del piloto.
