# Primera ola de la EDT (meses 1 a 3): paquetes de trabajo y actividades

Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/generar_ola.py`; no editar a mano. Fecha: 2026-10-08. Estado: **propuesta**, pendiente del visto bueno del equipo. Aplica la planificación gradual de PMBOK 6 aprobada por el usuario: las cuentas de control de `14_edt_corregida.md` activas en los meses 1 a 3 (enero a marzo de 2027) se bajan a elementos de **8 a 80 horas y de un mes como máximo** (FEP02, diapositiva 56; período de reporte mensual por RT-19.06). **Decisión del usuario del 2026-10-08:** en el software el paquete de trabajo es el entregable, uno por caso de uso; es un subproyecto (diap. 56) y supera las 80 h por una excepción declarada. Sus fases son **actividades** del cronograma: por eso el grupo A son actividades de análisis y no paquetes. Los grupos B, C y D sí son paquetes de trabajo. Los códigos tienen un nivel más que los de las cuentas; es una excepción a los cuatro niveles de la guía. Las horas de B, C y D no se inventan: esperan la planilla de tres valores (`21_planilla_ola_1.md`).

## 1. Resumen

| Grupo | Qué es | Cuentas | Elementos | Con horas |
| :-- | :-- | --: | --: | --: |
| A | Actividad de análisis de cada caso de uso (dentro de su paquete de software) | 30 | 84 | 84 |
| B | Trabajo continuo: un paquete por mes | 7 | 21 | 0 |
| C | Cuentas que terminan dentro de la ola, separadas en sus partes | 9 | 25 | 0 |
| D | Cuentas que siguen después: su primera entrega | 30 | 38 | 0 |
| **Total** | | **76** | **168** | **84** |

Elementos con horas: 84 de 168. Entre 8 y 80 h: 84. Fuera de rango: **0**.
Cada elemento tiene un solo mes por construcción. Las actividades de análisis salen del UCP; el resto queda «por estimar» y se verifica al llenar la planilla.

## 2. Elementos de la ola

### Grupo A. Actividad de análisis de cada caso de uso (dentro de su paquete de software)

| Código | Elemento | Cuenta | Mes | Horas | Fuente |
| :-- | :-- | :-- | :-- | --: | :-- |
| 1.5.1.1.1-A | Análisis del caso de uso «Cambiar y propagar un precio» (CU-OF-01) | 1.5.1.1 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.1.1.2-A | Análisis del caso de uso «Entregar la oferta vigente a los canales» (CU-OF-02) | 1.5.1.1 | 2 (feb 2027) | 49 | UCP (actividad de análisis, 10 %) |
| 1.5.1.1.3-A | Análisis del caso de uso «Consultar el precio vigente en línea» (CU-OF-03) | 1.5.1.1 | 3 (mar 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.1.1.4-A | Análisis del caso de uso «Recuperar el precio publicado en un instante» (CU-OF-06) | 1.5.1.1 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.1.2.1-A | Análisis del caso de uso «Registrar el cambio de etiqueta» (CU-OF-04) | 1.5.1.2 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.1.2.2-A | Análisis del caso de uso «Consultar el estado de exhibición de la tienda» (CU-OF-05) | 1.5.1.2 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.1.2.3-A | Análisis del caso de uso «Resolver el precio a cobrar ante diferencia con la etiqueta» (CU-OF-07) | 1.5.1.2 | 3 (mar 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.1.2.4-A | Análisis del caso de uso «Revisar los incidentes de discrepancia de precio» (CU-OF-08) | 1.5.1.2 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.1.5.1-A | Análisis del caso de uso «Aplicar las promociones vigentes en la venta» (CU-OF-09) | 1.5.1.5 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.1.5.2-A | Análisis del caso de uso «Administrar las promociones y su vigencia» (CU-OF-10) | 1.5.1.5 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.1.6.1-A | Análisis del caso de uso «Mantener el maestro de artículos» (CU-OF-11) | 1.5.1.6 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.1.6.2-A | Análisis del caso de uso «Revisar los reportes de calidad del maestro y de publicación» (CU-OF-12) | 1.5.1.6 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.1.1-A | Análisis del caso de uso «Publicar el disponible a los canales» (CU-EX-03) | 1.5.3.1 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.1.2-A | Análisis del caso de uso «Parametrizar el colchón de confianza y la vigencia de la reserva» (CU-EX-08) | 1.5.3.1 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.1.3-A | Análisis del caso de uso «Consultar la traza del cálculo del disponible» (CU-EX-09) | 1.5.3.1 | 3 (mar 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.1.4-A | Análisis del caso de uso «Consultar la disponibilidad para vender en sala» (CU-EX-01) | 1.5.3.1 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.1.5-A | Análisis del caso de uso «Consultar la disponibilidad en línea» (CU-EX-02) | 1.5.3.1 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.2.1-A | Análisis del caso de uso «Reservar una unidad para el canal digital» (CU-EX-04) | 1.5.3.2 | 1 (ene 2027) | 49 | UCP (actividad de análisis, 10 %) |
| 1.5.3.2.2-A | Análisis del caso de uso «Expirar las reservas vencidas» (CU-EX-05) | 1.5.3.2 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.2.3-A | Análisis del caso de uso «Verificar la existencia física antes del cobro» (CU-EX-06) | 1.5.3.2 | 3 (mar 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.2.4-A | Análisis del caso de uso «Resolver el conflicto de existencia comprometida» (CU-EX-07) | 1.5.3.2 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.4.1-A | Análisis del caso de uso «Parametrizar el conteo cíclico» (CU-EX-10) | 1.5.3.4 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.4.2-A | Análisis del caso de uso «Ejecutar el conteo cíclico» (CU-EX-11) | 1.5.3.4 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.4.3-A | Análisis del caso de uso «Consultar la exactitud del inventario y recibir alertas» (CU-EX-12) | 1.5.3.4 | 3 (mar 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.4.4-A | Análisis del caso de uso «Clasificar las diferencias y cerrar el ajuste» (CU-EX-13) | 1.5.3.4 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.4.5-A | Análisis del caso de uso «Emitir el informe mensual de merma» (CU-EX-14) | 1.5.3.4 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.4.6-A | Análisis del caso de uso «Gestionar las unidades en el probador» (CU-EX-15) | 1.5.3.4 | 3 (mar 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.7.1-A | Análisis del caso de uso «Suspender la publicación de una categoría» (CU-EX-16) | 1.5.3.7 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.7.2-A | Análisis del caso de uso «Degradar por cancelaciones» (CU-EX-17) | 1.5.3.7 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.8.1-A | Análisis del caso de uso «Recibir los movimientos del sistema de almacenes» (CU-EX-18) | 1.5.3.8 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.3.8.2-A | Análisis del caso de uso «Cargar las existencias de Concepción» (CU-EX-19) | 1.5.3.8 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.5.1.1-A | Análisis del caso de uso «Registrar y cobrar una venta» (CU-VE-01) | 1.5.5.1 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.5.1.2-A | Análisis del caso de uso «Reversar una venta o un pago» (CU-VE-02) | 1.5.5.1 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.5.1.3-A | Análisis del caso de uso «Cerrar la caja del turno» (CU-VE-03) | 1.5.5.1 | 3 (mar 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.5.1.4-A | Análisis del caso de uso «Desactivar los medios de pago de mayor fricción» (CU-VE-08) | 1.5.5.1 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.5.2.1-A | Análisis del caso de uso «Operar la tienda sin enlace» (CU-VE-04) | 1.5.5.2 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.5.2.2-A | Análisis del caso de uso «Reconciliar las ventas hechas sin enlace» (CU-VE-05) | 1.5.5.2 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.5.2.3-A | Análisis del caso de uso «Revisar el informe de excepciones de la conciliación» (CU-VE-06) | 1.5.5.2 | 3 (mar 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.5.2.4-A | Análisis del caso de uso «Validar las operaciones cursadas sin enlace» (CU-VE-07) | 1.5.5.2 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.5.6.1-A | Análisis del caso de uso «Registrar las ventas del canal digital» (CU-VE-09) | 1.5.5.6 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.5.6.2-A | Análisis del caso de uso «Enrutar los documentos tributarios al ERP/DTE» (CU-VE-10) | 1.5.5.6 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.5.7.1-A | Análisis del caso de uso «Cobrar con la tarjeta de la casa» (CU-VE-11) | 1.5.5.7 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.10.1.1-A | Análisis del caso de uso «Evaluar la solicitud y abrir una tarjeta en el mostrador» (CU-OR-01) | 1.5.10.1 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.10.1.2-A | Análisis del caso de uso «Ofrecer la tarjeta y consultar el resultado» (CU-OR-02) | 1.5.10.1 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.10.1.3-A | Análisis del caso de uso «Controlar los intentos de evaluación» (CU-OR-05) | 1.5.10.1 | 3 (mar 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.10.1.4-A | Análisis del caso de uso «Solicitar la ampliación de un cupo con enlace» (CU-OR-09) | 1.5.10.1 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.10.2.1-A | Análisis del caso de uso «Simular el costo total del crédito» (CU-OR-03) | 1.5.10.2 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.10.2.2-A | Análisis del caso de uso «Mantener la tasa máxima convencional vigente» (CU-OR-04) | 1.5.10.2 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.10.4.1-A | Análisis del caso de uso «Parametrizar los topes y la ventana de enfriamiento» (CU-OR-06) | 1.5.10.4 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.10.4.2-A | Análisis del caso de uso «Autorizar compra a cuotas sin enlace contra el cupo preaprobado» (CU-OR-07) | 1.5.10.4 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.10.4.3-A | Análisis del caso de uso «Mantener el cupo preaprobado en la tienda» (CU-OR-08) | 1.5.10.4 | 3 (mar 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.11.1.1-A | Análisis del caso de uso «Iniciar y registrar una gestión de cobranza» (CU-CA-01) | 1.5.11.1 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.11.1.2-A | Análisis del caso de uso «Calcular la mora y actualizar las cuentas» (CU-CA-05) | 1.5.11.1 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.11.2.1-A | Análisis del caso de uso «Repactar las condiciones de una deuda» (CU-CA-02) | 1.5.11.2 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.11.2.2-A | Análisis del caso de uso «Registrar el pago de una cuota» (CU-CA-04) | 1.5.11.2 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.11.2.3-A | Análisis del caso de uso «Consultar el estado de cuenta y los documentos» (CU-CA-03) | 1.5.11.2 | 3 (mar 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.11.5.1-A | Análisis del caso de uso «Revisar la conciliación diaria de la migración» (CU-CA-06) | 1.5.11.5 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.11.5.2-A | Análisis del caso de uso «Convivir con la plataforma de crédito de 2011» (CU-CA-07) | 1.5.11.5 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.12.1.1-A | Análisis del caso de uso «Entregar la información precontractual del crédito» (CU-EV-01) | 1.5.12.1 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.12.1.2-A | Análisis del caso de uso «Aceptar la información precontractual con firma electrónica» (CU-EV-02) | 1.5.12.1 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.12.1.3-A | Análisis del caso de uso «Consultar la información precontractual del crédito» (CU-EV-08) | 1.5.12.1 | 3 (mar 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.12.2.1-A | Análisis del caso de uso «Registrar el consentimiento de una modificación de condiciones» (CU-EV-03) | 1.5.12.2 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.12.2.2-A | Análisis del caso de uso «Enlazar la repactación con su cobranza y su consentimiento» (CU-EV-07) | 1.5.12.2 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.12.3.1-A | Análisis del caso de uso «Reconstruir el acto de consentimiento» (CU-EV-04) | 1.5.12.3 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.12.3.2-A | Análisis del caso de uso «Recuperar los antecedentes de una operación desde el archivo» (CU-EV-05) | 1.5.12.3 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.13.1.1-A | Análisis del caso de uso «Mantener el inventario de flujos de cruce autorizados» (CU-CC-01) | 1.5.13.1 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.13.1.2-A | Análisis del caso de uso «Revisar los cruces ejecutados y los intentos bloqueados» (CU-CC-03) | 1.5.13.1 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.13.2.1-A | Análisis del caso de uso «Intentar una campaña con atributos de origen financiero» (CU-CC-02) | 1.5.13.2 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.13.2.2-A | Análisis del caso de uso «Intentar un proceso crediticio con atributos de origen Retail» (CU-CC-04) | 1.5.13.2 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.13.3.1-A | Análisis del caso de uso «Resolver la correspondencia de identificadores entre ámbitos» (CU-CC-05) | 1.5.13.3 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.13.3.2-A | Análisis del caso de uso «Evaluar el impacto de una iniciativa sobre la frontera de datos» (CU-CC-06) | 1.5.13.3 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.14.1.1-A | Análisis del caso de uso «Ingresar a una terminal compartida con identidad individual» (CU-BT-01) | 1.5.14.1 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.14.1.2-A | Análisis del caso de uso «Administrar identidades, roles y ámbitos» (CU-BT-12) | 1.5.14.1 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.14.2.1-A | Análisis del caso de uso «Habilitar y revocar funciones según la capacitación normativa» (CU-BT-02) | 1.5.14.2 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.14.2.2-A | Análisis del caso de uso «Patrocinar el acceso temporal de un repositor externo» (CU-BT-03) | 1.5.14.2 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.14.2.3-A | Análisis del caso de uso «Operar como repositor externo con identidad individualizada» (CU-BT-04) | 1.5.14.2 | 3 (mar 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.14.2.4-A | Análisis del caso de uso «Retirar los accesos al término del vínculo» (CU-BT-05) | 1.5.14.2 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.14.2.5-A | Análisis del caso de uso «Conciliar los accesos contra la nómina activa» (CU-BT-06) | 1.5.14.2 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.14.5.1-A | Análisis del caso de uso «Declarar el orden y los criterios de degradación» (CU-BT-07) | 1.5.14.5 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.14.5.2-A | Análisis del caso de uso «Parametrizar las ventanas de congelamiento y bloquear intervenciones» (CU-BT-08) | 1.5.14.5 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.14.6.1-A | Análisis del caso de uso «Convivir con el sistema central de 2009» (CU-BT-09) | 1.5.14.6 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.14.6.2-A | Análisis del caso de uso «Administrar la plataforma de integración» (CU-BT-10) | 1.5.14.6 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.14.7.1-A | Análisis del caso de uso «Observar la operación y atender alertas» (CU-BT-11) | 1.5.14.7 | 1 (ene 2027) | 25 | UCP (actividad de análisis, 10 %) |
| 1.5.14.7.2-A | Análisis del caso de uso «Consultar tableros y exportar informes por ámbito» (CU-BT-13) | 1.5.14.7 | 2 (feb 2027) | 25 | UCP (actividad de análisis, 10 %) |

### Grupo B. Trabajo continuo: un paquete por mes

| Código | Elemento | Cuenta | Mes | Horas | Fuente |
| :-- | :-- | :-- | :-- | --: | :-- |
| 1.1.3.1 | Registro de solicitudes de cambio y su resolución, ene 2027 | 1.1.3 | 1 (ene 2027) | por estimar | por estimar |
| 1.1.3.2 | Registro de solicitudes de cambio y su resolución, feb 2027 | 1.1.3 | 2 (feb 2027) | por estimar | por estimar |
| 1.1.3.3 | Registro de solicitudes de cambio y su resolución, mar 2027 | 1.1.3 | 3 (mar 2027) | por estimar | por estimar |
| 1.1.4.1 | Registros de riesgos, lecciones aprendidas, supuestos y consultas, ene 2027 | 1.1.4 | 1 (ene 2027) | por estimar | por estimar |
| 1.1.4.2 | Registros de riesgos, lecciones aprendidas, supuestos y consultas, feb 2027 | 1.1.4 | 2 (feb 2027) | por estimar | por estimar |
| 1.1.4.3 | Registros de riesgos, lecciones aprendidas, supuestos y consultas, mar 2027 | 1.1.4 | 3 (mar 2027) | por estimar | por estimar |
| 1.1.7.1 | Actas de los comités e informe mensual de avance, ene 2027 | 1.1.7 | 1 (ene 2027) | por estimar | por estimar |
| 1.1.7.2 | Actas de los comités e informe mensual de avance, feb 2027 | 1.1.7 | 2 (feb 2027) | por estimar | por estimar |
| 1.1.7.3 | Actas de los comités e informe mensual de avance, mar 2027 | 1.1.7 | 3 (mar 2027) | por estimar | por estimar |
| 1.1.10.1 | Actas de aceptación por entrega y habilitación de pagos, ene 2027 | 1.1.10 | 1 (ene 2027) | por estimar | por estimar |
| 1.1.10.2 | Actas de aceptación por entrega y habilitación de pagos, feb 2027 | 1.1.10 | 2 (feb 2027) | por estimar | por estimar |
| 1.1.10.3 | Actas de aceptación por entrega y habilitación de pagos, mar 2027 | 1.1.10 | 3 (mar 2027) | por estimar | por estimar |
| 1.1.11.1 | Registro de garantías, seguros y certificados laborales vigentes, ene 2027 | 1.1.11 | 1 (ene 2027) | por estimar | por estimar |
| 1.1.11.2 | Registro de garantías, seguros y certificados laborales vigentes, feb 2027 | 1.1.11 | 2 (feb 2027) | por estimar | por estimar |
| 1.1.11.3 | Registro de garantías, seguros y certificados laborales vigentes, mar 2027 | 1.1.11 | 3 (mar 2027) | por estimar | por estimar |
| 1.2.4.1 | Catálogo de requerimientos y matriz de trazabilidad, ene 2027 | 1.2.4 | 1 (ene 2027) | por estimar | por estimar |
| 1.2.4.2 | Catálogo de requerimientos y matriz de trazabilidad, feb 2027 | 1.2.4 | 2 (feb 2027) | por estimar | por estimar |
| 1.2.4.3 | Catálogo de requerimientos y matriz de trazabilidad, mar 2027 | 1.2.4 | 3 (mar 2027) | por estimar | por estimar |
| 1.14.1.1 | Documentación técnica y funcional con inventario de componentes de software, ene 2027 | 1.14.1 | 1 (ene 2027) | por estimar | por estimar |
| 1.14.1.2 | Documentación técnica y funcional con inventario de componentes de software, feb 2027 | 1.14.1 | 2 (feb 2027) | por estimar | por estimar |
| 1.14.1.3 | Documentación técnica y funcional con inventario de componentes de software, mar 2027 | 1.14.1 | 3 (mar 2027) | por estimar | por estimar |

### Grupo C. Cuentas que terminan dentro de la ola, separadas en sus partes

| Código | Elemento | Cuenta | Mes | Horas | Fuente |
| :-- | :-- | :-- | :-- | --: | :-- |
| 1.1.1.1 | Plan de gestión del ámbito | 1.1.1 | 1 (ene 2027) | por estimar | por estimar |
| 1.1.1.2 | Plan de gestión del cronograma | 1.1.1 | 2 (feb 2027) | por estimar | por estimar |
| 1.1.1.3 | Plan de gestión de los costos | 1.1.1 | 3 (mar 2027) | por estimar | por estimar |
| 1.1.1.4 | Plan de gestión de la calidad | 1.1.1 | 1 (ene 2027) | por estimar | por estimar |
| 1.1.1.5 | Plan de gestión de los riesgos | 1.1.1 | 2 (feb 2027) | por estimar | por estimar |
| 1.1.1.6 | Plan de gestión de las comunicaciones | 1.1.1 | 3 (mar 2027) | por estimar | por estimar |
| 1.1.1.7 | Plan de gestión de los interesados | 1.1.1 | 1 (ene 2027) | por estimar | por estimar |
| 1.1.1.8 | Plan de gestión de las adquisiciones | 1.1.1 | 2 (feb 2027) | por estimar | por estimar |
| 1.1.2.1 | Estructura de descomposición del trabajo | 1.1.2 | 1 (ene 2027) | por estimar | por estimar |
| 1.1.2.2 | Diccionario de paquetes con entregable, criterio de aceptación y responsable | 1.1.2 | 2 (feb 2027) | por estimar | por estimar |
| 1.1.6.1 | Calendario de ventanas de congelamiento y de eventos anuales | 1.1.6 | 1 (ene 2027) | por estimar | por estimar |
| 1.1.6.2 | Declaración de impacto por evento | 1.1.6 | 2 (feb 2027) | por estimar | por estimar |
| 1.1.12.1 | Acta de constitución del proyecto | 1.1.12 | 1 (ene 2027) | por estimar | por estimar |
| 1.1.13.1 | Línea base de costos | 1.1.13 | 1 (ene 2027) | por estimar | por estimar |
| 1.1.13.2 | Presupuesto del proyecto | 1.1.13 | 2 (feb 2027) | por estimar | por estimar |
| 1.2.1.1 | Mapa de las 14 interfaces punto a punto existentes | 1.2.1 | 1 (ene 2027) | por estimar | por estimar |
| 1.2.1.2 | Inventario de las 9 plataformas | 1.2.1 | 2 (feb 2027) | por estimar | por estimar |
| 1.2.1.3 | Inventario de los 6 proveedores y sus dependencias | 1.2.1 | 3 (mar 2027) | por estimar | por estimar |
| 1.2.3.1 | Levantamiento de procesos | 1.2.3 | 1 (ene 2027) | por estimar | por estimar |
| 1.2.3.2 | Catálogo de reglas de negocio | 1.2.3 | 2 (feb 2027) | por estimar | por estimar |
| 1.2.3.3 | Volumetría declarada | 1.2.3 | 3 (mar 2027) | por estimar | por estimar |
| 1.14.6.1 | Plan de Reversibilidad | 1.14.6 | 1 (ene 2027) | por estimar | por estimar |
| 1.14.6.2 | Especificación de la exportación en formatos abiertos | 1.14.6 | 2 (feb 2027) | por estimar | por estimar |
| 1.14.10.1 | Protocolo de aceptación de entregas | 1.14.10 | 1 (ene 2027) | por estimar | por estimar |
| 1.14.10.2 | Protocolo de aceptación del producto final | 1.14.10 | 2 (feb 2027) | por estimar | por estimar |

### Grupo D. Cuentas que siguen después: su primera entrega

| Código | Elemento | Cuenta | Mes | Horas | Fuente |
| :-- | :-- | :-- | :-- | --: | :-- |
| 1.1.14.1 | Primera entrega de: Planes alternativos de las dos condiciones del adelanto del negocio financiero | 1.1.14 | 3 (mar 2027) | por estimar | por estimar |
| 1.2.6.1 | Primera entrega de: Línea base de alcance por etapa, con exclusiones y supuestos | 1.2.6 | 3 (mar 2027) | por estimar | por estimar |
| 1.2.7.1 | Primera entrega de: Estudio de decisión con costeo sobre etiquetas electrónicas de precio | 1.2.7 | 2 (feb 2027) | por estimar | por estimar |
| 1.2.8.1 | Primera entrega de: Estudio de decisión con costeo sobre el sistema de almacenes de Concepción | 1.2.8 | 2 (feb 2027) | por estimar | por estimar |
| 1.2.9.1 | Primera entrega de: Estudio de decisión con costeo sobre el destino de las plataformas | 1.2.9 | 2 (feb 2027) | por estimar | por estimar |
| 1.2.10.1 | Primera entrega de: Propuesta de criterios del cupo preaprobado para la filial emisora | 1.2.10 | 3 (mar 2027) | por estimar | por estimar |
| 1.3.1.1 | Documento de arquitectura | 1.3.1 | 2 (feb 2027) | por estimar | por estimar |
| 1.3.1.2 | Catálogo de decisiones de arquitectura | 1.3.1 | 2 (feb 2027) | por estimar | por estimar |
| 1.3.3.1 | Primera entrega de: Arquitectura física con emplazamiento por componente justificado | 1.3.3 | 2 (feb 2027) | por estimar | por estimar |
| 1.3.4.1 | Primera entrega de: Modelo de datos con dominios segregados Retail y Emisor, frontera documentada y políticas de retención | 1.3.4 | 2 (feb 2027) | por estimar | por estimar |
| 1.3.5.1 | Primera entrega de: Contratos de integración versionados y su gobierno | 1.3.5 | 3 (mar 2027) | por estimar | por estimar |
| 1.3.6.1 | Primera entrega de: Especificación del modo desconectado de 24 horas y de la sincronización tras la reconexión | 1.3.6 | 3 (mar 2027) | por estimar | por estimar |
| 1.3.7.1 | Primera entrega de: Modelo de capacidad y dimensionamiento | 1.3.7 | 3 (mar 2027) | por estimar | por estimar |
| 1.3.8.1 | Primera entrega de: Especificación y costeo de las obras de infraestructura del cliente | 1.3.8 | 3 (mar 2027) | por estimar | por estimar |
| 1.4.1.1 | Primera entrega de: Entorno de nube con infraestructura como código, subredes privadas y etiquetado de costos | 1.4.1 | 3 (mar 2027) | por estimar | por estimar |
| 1.4.4.1 | Primera entrega de: Ambientes de desarrollo, calidad, preproducción, producción y recuperación ante desastres | 1.4.4 | 1 (ene 2027) | por estimar | por estimar |
| 1.4.6.1 | Primera entrega de: Plataforma de integración y entrega continuas con infraestructura como código | 1.4.6 | 3 (mar 2027) | por estimar | por estimar |
| 1.4.7.1 | Primera entrega de: Licenciamiento de terceros a nombre del cliente | 1.4.7 | 2 (feb 2027) | por estimar | por estimar |
| 1.4.8.1 | Primera entrega de: Especificación de hardware y dispositivos de terreno para adquisición del cliente | 1.4.8 | 3 (mar 2027) | por estimar | por estimar |
| 1.4.9.1 | Primera entrega de: Plano y especificación del recinto técnico del centro de datos y coordinación de su obra civil de separación | 1.4.9 | 2 (feb 2027) | por estimar | por estimar |
| 1.4.11.1 | Primera entrega de: Plan de cierre de la brecha del centro de datos frente al informe interno de 2024 | 1.4.11 | 2 (feb 2027) | por estimar | por estimar |
| 1.6.1.1 | Primera entrega de: Catálogo de interfaces rediseñadas con contratos y niveles de servicio de integración | 1.6.1 | 2 (feb 2027) | por estimar | por estimar |
| 1.7.1.1 | Plan de migración | 1.7.1 | 2 (feb 2027) | por estimar | por estimar |
| 1.7.1.2 | Estrategia de corte y de retorno | 1.7.1 | 2 (feb 2027) | por estimar | por estimar |
| 1.7.1.3 | Inventario de datos históricos a migrar | 1.7.1 | 2 (feb 2027) | por estimar | por estimar |
| 1.8.1.1 | Plan de seguridad | 1.8.1 | 1 (ene 2027) | por estimar | por estimar |
| 1.8.1.2 | Matriz de controles | 1.8.1 | 1 (ene 2027) | por estimar | por estimar |
| 1.8.1.3 | Modelo de amenazas | 1.8.1 | 1 (ene 2027) | por estimar | por estimar |
| 1.8.5.1 | Primera entrega de: Modelo de identidad, matriz de roles y segregación de funciones, incluido el ámbito emisor | 1.8.5 | 2 (feb 2027) | por estimar | por estimar |
| 1.8.7.1 | Registro de actividades de tratamiento de datos personales | 1.8.7 | 3 (mar 2027) | por estimar | por estimar |
| 1.8.7.2 | Matriz de cumplimiento normativo | 1.8.7 | 3 (mar 2027) | por estimar | por estimar |
| 1.8.10.1 | Primera entrega de: Informe de diligencia del proveedor de nube | 1.8.10 | 2 (feb 2027) | por estimar | por estimar |
| 1.9.1.1 | Primera entrega de: Plan de pruebas con niveles, tipos, ambientes, datos y calendario | 1.9.1 | 2 (feb 2027) | por estimar | por estimar |
| 1.9.2.1 | Estándares de codificación | 1.9.2 | 1 (ene 2027) | por estimar | por estimar |
| 1.9.2.2 | Lista de revisión por pares | 1.9.2 | 1 (ene 2027) | por estimar | por estimar |
| 1.9.2.3 | Puertas de calidad | 1.9.2 | 1 (ene 2027) | por estimar | por estimar |
| 1.11.1.1 | Primera entrega de: Plan de implantación con procedimiento de despliegue gradual y de reversión probado | 1.11.1 | 3 (mar 2027) | por estimar | por estimar |
| 1.13.1.1 | Primera entrega de: Plan de gestión del cambio con diagnóstico por perfil y medición de adopción | 1.13.1 | 3 (mar 2027) | por estimar | por estimar |

## 3. Regla de descomposición del software

El paquete de trabajo de software es **el entregable que resuelve un caso de uso**: 127 paquetes, de 247 a 494 h (media 251 h). Ninguno cabe en 80 h, porque el UCP con la lectura B ya trae en cada caso su análisis, diseño, pruebas y sobrecarga. Se declara como excepción a la regla 8/80: cada paquete es un subproyecto con su propia descomposición en actividades (FEP02, diapositiva 56). Así cada paquete se traza a un caso de uso, a sus RF y a los resultados del Anexo D, y la EDT no se llena de fases.

Las actividades del cronograma de cada paquete son las cuatro fases de la lectura B: análisis (10 %), diseño (20 %), construcción (40 %) y pruebas (15 %); la sobrecarga (15 %) va a las cuentas de gestión. Cada actividad cumple 8/80 y un mes: si pasa de 80 h, se parte por transacción (o en partes iguales de hasta 80 h si el caso tiene menos transacciones que partes). Con los 127 casos:

| Fase | Actividades en todo el proyecto | Horas de la mayor |
| :-- | --: | --: |
| Análisis | 127 | 49 |
| Diseño | 133 | 49 |
| Construcción | 302 | 49 |
| Pruebas | 127 | 74 |
| **Total** | **689** | |

Esas 689 actividades son del cronograma, no de la EDT, y nunca se ejecutan todas a la vez. En cada ola se programa solo lo que ocurre en ella: la ola 1 tiene los análisis de la Etapa 1 y de la cartera; el diseño y la construcción de la Etapa 1 son actividades de los meses 4 en adelante, y los casos de la Etapa 2 de los meses 13 en adelante.

## 4. Qué falta

1. La planilla de tres valores de los paquetes de los grupos B, C y D (`21_planilla_ola_1.md`): dos estimadores, sin consultar el UCP.
2. La validación del equipo de las partes de los grupos C y D, que salen del nombre de cada cuenta.
3. Si se aprueban cuentas nuevas, las que empiecen en los meses 1 a 3 entran a esta ola.
