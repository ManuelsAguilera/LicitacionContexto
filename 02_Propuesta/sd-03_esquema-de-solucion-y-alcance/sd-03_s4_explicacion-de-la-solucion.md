---
id: T7-03-3.4
tipo: seccion
parte: T7-03
titulo: Explicación de la Solución
estado: borrador
bases: []
requisitos: []
depende_de: []
adjuntos: []
jira: []
cifras: []
origen: "05_Gestion/migraciones/fuentes/T7-03_Informes4_source.md#bloques-22,48"
actualizado: 2026-09-30
---
# 3.4 Explicación de la Solución



<!-- contenido migrado desde la fuente; permanece en borrador y requiere revisión humana -->



<!-- origen: T7-03_Informes4_source.md | bloque 22 -->

## Módulos funcionales de la solución

<!-- origen: T7-03_Informes4_source.md | bloque 48 -->

## Estrategia para obtener el apoyo de los grupos de interés clave

**Estrategia para el vendedor comisionista:** El vendedor de sala opera  bajo escasez de recursos y su remuneración depende directamente de la fluidez del sistema. Si el nuevo sistema es percibido como un obstáculo este será evadido. La estrategia para este grupo se basa en 3 pilares.

* **Protección de la comisión (M10):** Mediante la implementación del módulo de atribución de venta, se garantiza que el vendedor no pierda su comisión cuando una unidad de su sala sea despachada para un pedido web, ni cuando se realice una venta presencial con inventario en otra sucursal.

* **Reducción de tiempo en la evaluación crediticia:** El principal motivo actual de evasión por parte de los vendedores es que los procesos de cumplimiento normativo son excesivamente lentos. Actualmente, la evaluación crediticia tarda entre 40 segundos y 3 minutos. En un entorno de alta demanda, un cliente apurado con fila detrás frecuentemente prefiere no realizar la compra o cerrarla con otro medio de pago debido al tiempo de espera, lo que se traduce en una pérdida directa de la comisión por colocación financiera. La solución tecnológica propuesta reduce el tiempo de evaluación a ≤ 8 segundos ( M-15) y embebe el registro de la información precontractual y el consentimiento como un requisito sistémico bloqueante, sin añadir clics adicionales ni requerir firmas en papel (M-16). De este modo, el cumplimiento normativo se vuelve "invisible" para el vendedor: ya no le cuesta tiempo, no penaliza su productividad comercial y, por lo tanto, desaparece el incentivo perverso para evitarlo.

**Estrategia para las jefaturas de Tienda:** El dolor principal de los gerentes y jefes de local es la perdida de control sobre sus indicadores. por ejemplo la merma se ve como un número agregado; no puede aislar hurto vs descuadre administrativo , La discrepancia de inventario , Conteo que paraliza la operación.

* **Empoderamiento sobre los KPIs locales (M-02  Gestión de Inventario)**: se apalancará su apoyo demostrando cómo el M-02 les permitirá, por primera vez, aislar el descuadre administrativo del hurto real, protegiendo el indicador de merma de su tienda y su desempeño ante la gerencia.

* **Comisión y venta de la sala protegidas:** La imputación al origen (**M-10, SUP-12 / SUP-14**) resuelve el conflicto del despacho omnicanal. Se elimina la fricción de tener que "sacarle al vendedor de la mano" una unidad para despacharla a otra ciudad, perdiendo la comisión y bajando la venta del local.

* **Control sobre personal externo:** Para mitigar el riesgo de tener decenas de repositores externos operando diariamente en la sala, se delegará el control de accesos a los proveedores a través del IAM (**M-23**). Esto libera a la jefatura de la carga administrativa y de seguridad de gobernar credenciales ajenas.

**Estrategia para los vendedores del marketplace:** El dolor principal de los 310 vendedores externos es operar en un entorno de total oscuridad transaccional no saben que sucede con su pedido después de realizar su despacho. Sufren por devoluciones que quedan inmovilizadas en bodegas de Ancoa sin previo aviso hasta que impactan sus liquidaciones, y por la incertidumbre de su evaluación operativa no existe un método por los cuales los evalúen . Su exigencia es concreta: "saber en qué estado está cada pedido mío, enterarme de una devolución cuando ocurre y saber con qué regla me miden". El apoyo de este grupo se asegurará mediante previsibilidad y transparencia:

* **Estado del pedido y aviso de devolución en tiempo real**: A través del M-14 , se implementa una notificación transaccional que se dispara en el momento exacto de la recepción física del producto en la tienda. Esto resuelve directamente su exigencia de "enterarme de una devolución cuando ocurre" (y no a fin de mes con la nota de crédito), registrando la responsabilidad financiera y física del activo de manera inmediata.

* **Reglas de medición conocidas y predecibles:**La aceptación digital de políticas fija las reglas del juego y el ranking por cinco KPIs (cancelación, puntualidad, devoluciones, lead time y calidad de catálogo) hace visible y predecible la evaluación que hoy no existe. El vendedor sabe con exactitud qué se le mide y con qué consecuencia, premia a quienes rinden y sanciona de forma sistémica a quienes degradan el servicio, eliminando la arbitrariedad.

**Estrategia para la Gerencia del Negocio Financiero:** La Gerencia del Negocio Financiero y la Contraloría enfrentan una exposición regulatoria crítica debido a que los procesos actuales dependen de la correcta ejecución manual, lo cual imposibilita demostrar la probidad de las operaciones ante el ente fiscalizador. A esto se suma el riesgo sistémico de obsolescencia tecnológica y el vencimiento del plan de remediación normativo fijado para 2029\. Ambas áreas reconocen la tensión estructural entre la necesidad comercial de vender rápidamente en caja y la obligación legal de entregar información previa al contrato.

* **Acreditación inmutable del consentimiento**: Ante la máxima regulatoria de que *"un consentimiento que no se puede acreditar es un consentimiento que no existe"*, el Gestor de Evidencia (M-16) elimina la vulnerabilidad de los 1.240 casos sin respaldo. Implementa un expediente digital estructurado, sellado criptográficamente y custodiado en almacenamiento inmutable por todo el ciclo de vida del crédito más el periodo legal de retención.

* **Frontera de datos técnica y auditable:** Ante la preocupación por el uso comercial del comportamiento de pago, el **Gobierno de Frontera (M-21)** define reglas estrictas: qué se puede cruzar, con qué base legal y bajo qué control técnico. Deniega por omisión cualquier consulta no autorizada y registra cada evento de forma inalterable, cumpliendo la condición fundamental de la contralora: *"que quede escrito y auditable"*.

* **Migración de cartera mitigada:** Asumiendo que trasladar a 620.000 clientes con saldo *"no es una migración de datos: es una operación de alto riesgo"*, el **M-19 (Migración de Cartera)** descarta el corte abrupto. Ejecuta el traslado mediante olas de coexistencia con conciliación diaria, utilizando un umbral de discrepancia como freno automático de avance. Esto asegura el cumplimiento del hito regulatorio de 2029 sin exponer a la entidad financiera.

**Estrategia para la Gerencia de Canales Digitales:** El principal punto de dolor de esta gerencia es la vulnerabilidad de su promesa comercial, al verse forzada a publicar y transaccionar sobre existencias que no tienen respaldo físico real. Esta situación derivó en la crisis operativa del evento de junio, donde miles de pedidos debieron ser cancelados por falta de stock. Se conoce que el registro logístico posee un margen de error basal del 12 %, pero los intentos de restringir la exposición del inventario para evitar quiebres chocan con la resistencia interna por el temor a disminuir las ventas inmediatas.

* **Disponibilidad con grado de confianza:** Para resolver el problema de las ventas sobre inventario inexistente, el Motor de Disponibilidad (M-01) transforma la manera en que se compromete el stock. En lugar de ofrecer unidades a ciegas asumiendo el registro central como absoluto, el motor calcula un colchón dinámico y expone la disponibilidad acompañada de un índice de confianza estadística. Esto le entrega a la gerencia exactamente la palanca de control que requiere: la capacidad de parametrizar el nivel de exposición al riesgo comercial por categoría, tomando decisiones informadas para proteger la promesa de entrega.

* **Gobernanza y depuración del marketplace:** Para solucionar la incapacidad de gestionar el desempeño de los actores externos, el Seller Center (M-12) automatiza el control de calidad y las reglas del ecosistema. El módulo evalúa de forma continua cinco indicadores clave de nivel de servicio de los vendedores externos y ejecuta rutinas de suspensión sistémica escalonada sobre aquellos que degradan la experiencia de compra. Esto protege la reputación del dominio principal y estandariza la calidad exigida para operar bajo la marca de la compañía.

* **Protección proactiva del evento anual masivo:** Considerando que las fechas de los grandes eventos de comercio electrónico son fijadas por entidades gremiales externas con plazos de preaviso acotados y no modificables, la plataforma no puede depender de escalamientos puramente reactivos ante picos de 104.000 pedidos. El módulo de Observabilidad y Degradación Controlada **(M-24)** garantiza que las variaciones extremas de tráfico se gestionen mediante protocolos técnicos predefinidos. Esto asegura que la plataforma degrade funciones accesorias de forma controlada antes de colapsar, protegiendo la transacción y evitando las cancelaciones masivas.
