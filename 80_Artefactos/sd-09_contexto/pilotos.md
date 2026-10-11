---
tipo: informe-interno
parte: T7-09
estado: borrador
actualizado: 2026-10-11
origen: "Anexo D; Bases del Caso; catálogo Excel v3.0 y v3.1; SD03 vigente"
---
# Seis pilotos de verificación y aceptación

Estos criterios son propuestas de diseño de prueba. Todos están pendientes de ejecución y de revisión humana. C-Rnn-mm identifica un criterio interno, sin crear requisitos oficiales. La evidencia indicada debe producirse sobre una versión identificada, con ambiente, datos de entrada, reloj sincronizado cuando corresponda, resultado esperado y obtenido, defectos y responsable. Un ensayo satisfactorio aporta evidencia técnica; la Contraparte Técnica conserva la decisión de aceptación. El ensayo informa el máximo observado, que no demuestra una garantía universal fuera del perfil ensayado. Los máximos se comprueban por operación observada; un promedio o percentil favorable no compensa una violación.

<a id="r16"></a>

## R16 · Evaluación crediticia

Fuente: [Anexo D, resultado 16](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md#anexo-d-del-subdocumento-3-criterios-de-aceptación-de-los-resultados-de-negocio), línea 24; [Caso, RT-09.01](../../00_Bases/Caso_09_Cadena_Multitienda.md), línea 799. RNF-06 confirmado en v3.0 hoja `1_Catalogo_Atomico`, fila 238, y v3.1 `1_Catalogo_Vigente`, fila 237. Diseño: [SD03](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex), líneas 450 y 454. Ámbito: Filial emisora, originación y evidencia financiera; la ubicación del POS en Retail no concede acceso comercial a crédito.

| Criterio interno | Escenario y método | Umbral y evidencia prevista |
| :--- | :--- | :--- |
| C-R16-01 | Medir desde envío de solicitud completa habilitada hasta decisión visible en POS; campañas de peak presencial y carga financiera concurrente. | Máximo ≤8 s, fuente Caso; trazas correlacionadas cliente/servidor y listado de cada duración. |
| C-R16-02 | Intentar evaluar sin entrega precontractual completa; prueba negativa de interfaz y API. | RF-199 exige bloqueo previo a evaluación; registro de rechazo y ausencia de decisión. |
| C-R16-03 | Cortar enlace durante solicitud e intentar originar tarjeta o ampliar cupo. | Diseño SD03: ambas acciones bloqueadas; bitácora, estados y prueba del retorno sin duplicidad. |

Aceptación: líder QA ejecuta y responsable de originación del Emisor valida el flujo; Contraparte Técnica firma antes del mes 16. Dependencias: información precontractual versionada, integración plataforma de 2011, cargas y reglas de desconexión. Brecha P01: Arquitectura y Emisor deben fijar perfil presencial, concurrencia financiera, inicio/fin de reloj y datos representativos antes de campaña. Los 8 segundos miden evaluación, sin eliminar el tiempo necesario para informar al cliente; R28 reutiliza C-R16-01 y el control de R20.

<a id="r18"></a>

## R18 · Consentimiento informado de repactación

Fuente: [Anexo D](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md), línea 26; [Caso](../../00_Bases/Caso_09_Cadena_Multitienda.md), líneas 604 y 621. Diseño [SD03](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex), líneas 452–454. Ámbito: Filial emisora; cartera y evidencia financiera. RF-200 a RF-204 describen evidencia precontractual de originación y no se declaran equivalentes a consentimiento de repactación.

| Criterio interno | Escenario y método | Umbral y evidencia prevista |
| :--- | :--- | :--- |
| C-R18-01 | Repactar con evidencia ausente, ilegible o de otro expediente; pruebas negativas API/interfaz. | Cero repactaciones registradas sin evidencia recuperable, fuente Caso; rechazos y comparación de saldos antes/después. |
| C-R18-02 | Repactar con evidencia completa; inspeccionar vínculo acto/cliente/condiciones/instante y recuperar soporte. | Cada acto autorizado enlaza evidencia recuperable; expediente y traza de consulta. |
| C-R18-03 | Alterar soporte y provocar indisponibilidad de custodia al confirmar. | Propuesta: rechazar integridad inválida o evidencia no recuperable; hashes, bitácora y ausencia de modificación. |

Aceptación: QA financiero y responsable cartera del Emisor, con encargado de cumplimiento; Contraparte Técnica firma mes 16 actos nuevos y mes 21 cartera migrada. Dependencias: conservación plazo crédito más seis años (Caso RT-05.10, línea 794), clasificación de soportes, expedientes históricos. Brecha P02: Cumplimiento del Emisor debe definir suficiencia jurídica y catálogo oficial aplicable a repactación; no reconstruir consentimientos históricos inexistentes. R19 define recuperación ≤5 minutos como propuesta del Anexo D, separada del bloqueo funcional.

<a id="r21"></a>

## R21 · Separación Retail / Emisor

Fuente: [Anexo D](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md), línea 29; [Caso](../../00_Bases/Caso_09_Cadena_Multitienda.md), línea 82 y RT-06.01, línea 798. RNF-11 y RNF-14: v3.0 filas 243/246; v3.1 filas 242/245. Diseño [SD03](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex), líneas 458–465 y 515–523. Servicio de control de cruces y controles en ambos extremos; infraestructura común mantiene límites de datos, permisos y auditoría.

| Criterio interno | Escenario y método | Umbral y evidencia prevista |
| :--- | :--- | :--- |
| C-R21-01 | Revisar despliegue, identidades, almacenamiento, backups, analítica y redes frente a mapa de datos. | Separación implementada y documentada, fuente Caso; inventario y configuración contrastados con diseño. |
| C-R21-02 | Desde rol Retail intentar leer saldo/mora/cupo, exportar y usar atributos financieros en campañas por API, analítica y ruta alternativa. | Propuesta: todos los accesos no autorizados denegados; registro de intentos, respuestas y ausencia de datos. |
| C-R21-03 | Pentest de frontera y retest de correcciones. | Sin hallazgos críticos ni altos abiertos, obligatorio [Bases Transversales, cap. 20.1](../../00_Bases/Bases_Transversales.md#L847); informe independiente y retest vinculado a versión. |
| C-R21-04 | Ejecutar cruce autorizado y uno sin finalidad/base/autorización; auditar extremos. | RF-165: registro completo de cada cruce ejecutado; propuesta: rechazo del segundo; decisiones y campos mínimos. |

Aceptación: tercero independiente del adjudicatario ejecuta pentest antes de cada paso a producción y anualmente (RT-11.20, Bases Transversales línea 562). Arquitectura, Seguridad y Cumplimiento del Emisor preparan controles y remediaciones; Contraparte Técnica firma mes 16. Dependencias: catálogo de flujos, roles, contratos y separación de analítica. Brecha P03: Arquitectura/Cumplimiento deben conciliar RNF-14 (separación física) con RT-06.01 (física o lógica acreditada), sin rebajar el catálogo: documentar decisión y controles antes del ensayo. Brecha P04: Seguridad define severidad y alcance independiente del pentest. Un informe de cumplimiento técnico no afirma certificación ISO ni aprobación del regulador.

<a id="r24"></a>

## R24 · Conciliación de cartera migrada

Fuente: [Anexo D](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md), línea 32; [Caso](../../00_Bases/Caso_09_Cadena_Multitienda.md), RT-05.15 línea 795 y numeral 13.3 línea 714. Diseño [SD03](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex), línea 351 y servicio línea 452. Ámbito Emisor; cartera y plataforma de 2011 conviven por olas, con comunicación a 620.000 clientes con saldo.

| Criterio interno | Escenario y método | Umbral y evidencia prevista |
| :--- | :--- | :--- |
| C-R24-01 | Conciliar diariamente fuente/destino por cliente, cuenta y tramo durante ensayo y convivencia. | Cero diferencias sin explicar, fuente Caso; libro de conciliación, saldos y diferencias justificadas. |
| C-R24-02 | Comparar cuotas, repactaciones, garantías, cobranzas y juicios, además de saldos. | Cartera completa, RT-05.15; conteos y controles de completitud por tipo de dato. |
| C-R24-03 | Simular falla de integración y retorno antes de aprobar tramo. | Retorno probado, fuente Caso; evidencia de reversión, saldos y operaciones sin pérdida. |
| C-R24-04 | Realizar operaciones durante convivencia y revisar comunicación a clientes del tramo. | Convivencia real y plan de comunicación, fuente Caso; trazas de operaciones y registro de comunicaciones. |

Aceptación: responsable migración y cartera concilian; QA observa; filial emisora y Contraparte Técnica cierran compuerta por tramo antes de producción mes 16/21. No avanzar con diferencias sin explicar ni integración fallida; gestionar corrección dentro del calendario obligatorio. Brecha P05: Emisor/Migración acuerdan claves, cortes, libro de diferencias, quién valida explicaciones y tratamiento de histórico con evidencia ausente. Una diferencia explicada no autoriza pérdida o saldo incorrecto: documentar corrección o fundamento validado. No aprobar solo por igualdad del total agregado.

<a id="r06"></a>

## R06 · Propagación de precios

Fuente: [Anexo D](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md), línea 14; [Caso](../../00_Bases/Caso_09_Cadena_Multitienda.md), RT-05.29/RT-09.01 líneas 797/799. RNF-19: v3.0 fila 251, v3.1 fila 250. Diseño [SD03](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex), línea 424. Retail: oferta comercial entrega precio; ventas y canal digital lo aplican, sala ejecuta cambio de etiqueta.

| Criterio interno | Escenario y método | Umbral y evidencia prevista |
| :--- | :--- | :--- |
| C-R06-01 | Cambiar precio y medir versión efectivamente aplicada en cada una de las 380 cajas y canal digital. | Cada destino ≤5 min desde cambio, fuente Caso; marcas de tiempo/versiones por destino, incluyendo fallas. |
| C-R06-02 | Propagar bajo campaña de hasta 400.000 eventos de precio/día, reintentos y mensajes fuera de orden. | Mismo máximo; prueba de carga y consistencia de versión vigente. |
| C-R06-03 | Registrar estado de cambio en puntos de exhibición y muestrear precio exhibido/cobrado. | Plazo sala pendiente; estado y auditoría alimentan R07/R09, sin extender 5 min a etiquetas por inferencia. |

Aceptación: QA y responsable oferta comercial con Canales/Tiendas; Contraparte Técnica mes 16. Brecha P06: Comercial/Tiendas definen política de sala, denominador y responsabilidades antes de aceptación. Las 310.000 etiquetas físicas no se suponen electrónicas. Brecha P07: Arquitectura/QA definen distribución temporal de 400.000 cambios y conducta ante destinos desconectados, sin ocultar violaciones del máximo.

<a id="r03"></a>

## R03 · Cobro condicionado al disponible

Fuente: [Anexo D](../../04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md), línea 11; RNF-65 v3.0 fila 297/v3.1 fila 293; RF-050 v3.0 fila 53/v3.1 fila 52. Diseño: [SD03](../../02_Propuesta/latex_final/sd-03/OSS-Subdocumento3.tex), servicio pedidos y existencias. Ámbito Retail; el pago con tarjeta propia cruza solo resultado autorizado bajo frontera, sin publicar saldo o mora.

| Criterio interno | Escenario y método | Umbral y evidencia prevista |
| :--- | :--- | :--- |
| C-R03-01 | Declarar pedido no cumplible antes de captura e intentar cobrar por interfaz/API. | Propuesta: captura bloqueada; traza pedido-reserva-pasarela y rechazo. |
| C-R03-02 | Consumir última unidad en dos canales, duplicar mensajes y caer entre reserva y captura. | Propuesta: cero capturas de unidad no entregable; ensayo de concurrencia e idempotencia, estado único. |
| C-R03-03 | Conciliar diariamente preautorizaciones vencidas/capturas con pedidos no cumplibles. | RNF-65: cero cobros sostenidos; RF-050: conciliación diaria; reporte completo y comprobantes de liberación/reversa. |
| C-R03-04 | Avisar falta de unidad antes de cobrar y recuperar estado por cliente/mesón. | Aviso previo al cobro, R26 y Caso RT-16.21; marcas de aviso/captura y auditoría de canales. |

Aceptación: QA Retail y responsables Pedidos/Pagos; Contraparte Técnica mes 21. Dependencias: disponible confiable, reservas y contrato de pasarela. Brecha P08: Pedidos/Pagos/Contraparte deben conciliar garantía R03 "ningún cobro" con RNF-65 "ningún cobro sostenido": definir captura vs preautorización y reversa ante carrera. La conciliación posterior sola no acredita el bloqueo preventivo. Definir plazo de reversa y conducta ante falla de pasarela sin inventar tiempo aprobado.
