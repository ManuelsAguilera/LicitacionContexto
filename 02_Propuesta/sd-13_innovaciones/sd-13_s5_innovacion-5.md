---
id: T7-13-13.5
tipo: seccion
parte: T7-13
titulo: Innovación 5
estado: borrador
bases:
  - "Bases Transversales, RT-13.01, RT-13.03 y RT-13.07"
  - "Caso 09, capítulos 6 y 7"
requisitos: []
depende_de:
  - T7-03
  - T7-04
  - T7-07
adjuntos: []
jira: []
cifras:
  - produccion_etapa_2_mes
origen: "80_Artefactos/sd-13_contexto/investigacion_cinco_innovaciones.md, sección 6; etapas del Servicio de clientes Retail en SD-03"
actualizado: 2026-10-11
---
## 13.5 Innovación 5

La innovación de experiencia de usuario es Modo Tienda con fila virtual de probadores. Permite solicitar un turno desde el móvil o un tótem, consultar su estado y recibir el llamado mientras el cliente continúa recorriendo la tienda. La atención asistida ofrece acceso a quienes no utilizan smartphone. El beneficio se verifica mediante tiempo de espera física, éxito de solicitud y abandono.

### Problema y alcance

El Caso identifica los probadores como una ubicación donde la mercadería pierde visibilidad y retorna de forma irregular al piso de venta (Multitiendas Ancoa S.A., 2026b, caps. 6 y 7). La fila virtual ordena el acceso a ese espacio, pero no identifica cada prenda ni sustituye el control de existencias. El levantamiento mide afluencia, espera y abandono antes de dimensionar el servicio; el Caso no aporta una línea base de estos tiempos.

El cliente selecciona tienda o accede mediante un QR y solicita turno sin que la ubicación geográfica sea condición de acceso. El modo tienda muestra información de zonas y productos a partir de planos y ubicaciones validados. La navegación interior precisa exige un levantamiento y una prueba separados. El cliente conserva la posibilidad de utilizar tótem o atención asistida sin crear una cuenta.

### Tecnología y madurez

El equipo de referencia es Zebra KC50 de 22 pulgadas, con montaje accesible, Ethernet y administración empresarial. La configuración considera una impresora de turnos Epson TM-T20III Ethernet si el flujo de atención requiere papel. Se valida la variante, compatibilidad del SDK, alojamiento físico y accesibilidad del conjunto antes de aprobar la compra (Zebra Technologies, s. f.; Epson, s. f.). El número también se entrega en pantalla y mediante personal si la impresora no está disponible.

Las geovallas o balizas BLE constituyen ayudas opcionales. Android documenta demoras de eventos en segundo plano, y Apple establece condiciones de monitoreo de regiones. Por eso la entrada al modo tienda mantiene selección explícita y QR, y no promete activación automática inmediata ni ubicación exacta solo por instalar balizas (Google, s. f.; Apple, s. f.).

El hardware y las interfaces de ubicación tienen evidencia de componente comercial o documentado. La escala de madurez requiere después integración probada de la fila, recuperación y notificaciones, y operación aceptada con personas usuarias. La prueba incluye el conjunto instalado, ya que una ficha de hardware no demuestra la accesibilidad del montaje ni de la aplicación.

### Incorporación a arquitectura y EDT

El componente local de tienda custodia la fila y el estado de cubículos durante cortes del enlace central. Distingue turno en espera, llamado, presentado, en uso, finalizado, cancelado o ausente, y cubículo libre, reservado, ocupado, en limpieza o fuera de servicio. El personal confirma presentación y liberación. La asignación transaccional impide que dos turnos ocupen el mismo cubículo.

La nube consolida indicadores y configuración. El móvil requiere comunicación con el componente que sirve la fila para obtener estado en vivo. Durante un corte del enlace, el tótem local puede continuar atendiendo; se informa la limitación a móviles que no puedan conectarse y se utiliza el canal asistido. La persistencia permite recuperar turnos tras reinicio y reconciliar eventos después del corte.

El paquete «Modo Tienda con fila virtual de probadores» se ubica en la rama 1.10 Innovaciones. Se vincula al servicio de clientes Retail y al canal móvil, asignados a la Etapa 2 en el subdocumento 3. El levantamiento y las pruebas de interfaz pueden comenzar antes, pero la aceptación integrada corresponde a la marcha blanca de esa etapa y la habilitación al mes 21. Esta asignación evita depender en el mes 16 de un servicio que se entrega después.

### Impacto económico

La inversión comprende tótem, instalación, aplicación, integración y pruebas con usuarios. El costo operacional incluye soporte, mantenimiento y consumibles cuando se utiliza impresión. El beneficio directo se expresa en experiencia y menor abandono; una mejora de conversión se valoriza únicamente si una comparación demuestra su atribución. La Oferta Económica no duplica beneficios ya asignados a búsqueda o publicidad.

### Verificación del beneficio

Se mide por separado tiempo de espera física y tiempo total desde solicitud hasta acceso. La fila virtual permite liberar al cliente de esperar de pie, pero no aumenta por sí sola la cantidad de cubículos. La línea base se registra por franja de demanda y perfil de usuario antes del piloto.

La meta es reducir espera física frente a la línea base, mantener el tiempo total de acceso dentro del criterio acordado y evitar asignaciones duplicadas. El acta de diseño fija el umbral de mejora y las reglas de gracia, reingreso y prioridades con Operación antes del ensayo. Las pruebas manuales y automatizadas verifican WCAG 2.2 AA y acceso equivalente desde móvil, tótem y asistencia conforme a RT-13.01, RT-13.03 y RT-13.07. La marcha blanca evalúa los flujos y desde el mes 21 se sigue abandono, ausencias y disponibilidad del servicio.

### Riesgo de adopción y contingencia

Las ausencias después del llamado y la baja comprensión del turno tienen probabilidad inicial media e impacto medio. Se mitigan mediante estado visible, reglas de reingreso y prueba con usuarios. El personal conserva la gestión asistida y la política de atención accesible.

Los fallos de enlace o reinicio tienen probabilidad media e impacto alto. El ensayo provoca ambas condiciones y verifica persistencia y ausencia de doble asignación. Si el componente local no opera, se utiliza una fila asistida y se informa la indisponibilidad digital. La notificación sonora o móvil no se considera prueba de recepción; el tótem y el personal permiten consultar el llamado. La desactivación del servicio no impide vender ni gestionar inventario.
