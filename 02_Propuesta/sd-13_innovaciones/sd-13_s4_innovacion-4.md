---
id: T7-13-13.4
tipo: seccion
parte: T7-13
titulo: Innovación 4
estado: borrador
bases:
  - "Bases Administrativas, artículos 18, 28 a 30 y 72"
  - "Caso 09, capítulo 19"
requisitos: []
depende_de:
  - T7-03
  - T7-05
  - T7-07
adjuntos: []
jira:
  - OSS-104
cifras:
  - produccion_etapa_2_mes
origen: "80_Artefactos/sd-13_contexto/investigacion_cinco_innovaciones.md, sección 5"
actualizado: 2026-10-11
---
## 13.4 Innovación 4

La innovación de modelo de negocio es Retail Media Network. Ancoa comercializa a proveedores del retail campañas de productos patrocinados en su canal digital, con presupuesto, reglas de publicación y reportes de desempeño. Marketing y Comercial gestionan anunciantes y aprueban las campañas; la plataforma presta el servicio de publicación y medición.

### Oportunidad y propuesta de valor

La relación comercial con proveedores y el catálogo del retail permiten ofrecer exposición de productos dentro del recorrido de compra. El ingreso procede del servicio publicitario que contrata el anunciante y se registra separado del margen de venta de mercadería. La captación de anunciantes requiere trabajo comercial de Ancoa. La propuesta no considera como comprometidas marcas que todavía no han contratado campañas.

El diseño cumple la separación entre retail y filial emisora exigida por el Caso. Las campañas no utilizan saldos, mora, cupos, puntajes ni comportamiento de pago. El ámbito financiero conserva sus datos y sus finalidades (Multitiendas Ancoa S.A., 2026b, caps. 13 y 19).

### Tecnología y madurez

El suministro evalúa una plataforma especializada con administración de campañas, productos elegibles, presupuestos y reportes. Criteo es la referencia comercial de productos patrocinados y campañas con pujas y atribución. La documentación distingue cobro por clic y configuración de las ventanas que atribuyen ventas a una campaña (Criteo, s. f.-a, s. f.-b). El desarrollo propio se compara por control, integración, privacidad y soporte, e incluye la conciliación y prevención de cobros inválidos si se selecciona.

La plataforma documentada alcanza el estado comercial de la escala de evidencia. La integración probada exige publicar y conciliar una campaña de prueba. La operación aceptada requiere además anunciante, aprobación comercial y registro de ingresos. La disponibilidad del software no acredita demanda publicitaria para Ancoa.

### Incorporación a arquitectura y EDT

Un adaptador retail conecta el catálogo del servicio de oferta comercial con la plataforma publicitaria y valida disponibilidad mediante el servicio de existencias. El canal distingue el resultado patrocinado y aplica relevancia, elegibilidad y límite de densidad aprobado. La publicidad no bloquea el proceso de compra cuando el proveedor de anuncios falla.

El paquete «Retail Media Network» pertenece a la rama 1.10 Innovaciones. Incluye modelo comercial, selección de plataforma, integración, conciliación y piloto. La preparación se realiza en la Etapa 2, con capacidad técnica disponible desde el mes 21. La activación comercial requiere anunciantes aprobados; si no existen, el canal mantiene resultados orgánicos y el escenario económico registra ausencia de ingreso publicitario.

El alcance inicial utiliza campañas contextuales por consulta o categoría. El perfilamiento personal exige revisión específica de finalidad, base jurídica y tratamiento antes de incorporarse. Una seudonimización no convierte automáticamente datos personales en anónimos. El diseño considera la Ley 21.719, su vigencia durante la operación y los contratos con encargados del tratamiento (Biblioteca del Congreso Nacional de Chile, 2024). Los capítulos 4 y 5 detallan límites de acceso, registros y conservación.

### Impacto económico

La inversión comprende selección e integración, configuración de campañas, medición y conciliación. La operación incluye licencia o comisión de plataforma, soporte y gestión comercial. Los ingresos se calculan con clics válidos facturables multiplicados por la tarifa efectiva, o con impresiones facturables y su tarifa por millar según el producto contratado. La Oferta Económica incorpora demanda, descuentos, devoluciones y costos en escenarios separados, incluido uno sin anunciantes.

El negocio publicitario de Ancoa no modifica por sí mismo los hitos de pago al adjudicatario. Cualquier esquema de participación en ingresos debe comprobar compatibilidad con los artículos 18 y 72 y con E-25 antes de incorporarse. El cuerpo técnico no contiene tarifas ni valores que permitan inferir el monto de la oferta.

### Verificación del beneficio

La línea base del nuevo servicio es su estado sin campañas activadas; el levantamiento identifica también acuerdos publicitarios existentes para distinguir ingresos adicionales de ingresos trasladados. El piloto debe completar publicación, presupuesto, registro de clics o impresiones válidos y conciliación de una campaña contratada.

Se mide ingreso publicitario neto incremental, anunciantes activos, repetición de campañas, conciliaciones y efecto sobre la experiencia de compra. La meta es operar campañas con trazabilidad de presupuesto a reporte y facturación, sin consumir información financiera. El plan comercial fija la meta de captación e ingreso antes del piloto. Las ventas atribuidas a una ventana publicitaria no prueban ventas adicionales; estas se estiman con comparación controlada. La medición comienza en el mes 21 y continúa durante operación.

### Riesgo de adopción y contingencia

La baja captación de anunciantes tiene probabilidad inicial alta e impacto alto sobre el ingreso esperado. Ancoa valida demanda y compromisos comerciales antes de escalar el servicio. Si la demanda no se materializa, se mantiene el canal orgánico y se revisa el escenario económico sin atribuir ingresos inexistentes a la innovación.

El uso indebido de datos tiene probabilidad media e impacto alto. Se mitiga con segmentación contextual, separación de permisos y revisión del contrato de plataforma. Una campaña que incumple finalidad o elegibilidad se suspende y conserva evidencia para investigación. Los cobros inválidos tienen probabilidad media e impacto alto; presupuesto y eventos se concilian antes de facturar. El T-16 incorpora las valoraciones definitivas y sus responsables.
