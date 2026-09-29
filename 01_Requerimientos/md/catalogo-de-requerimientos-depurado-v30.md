# Catalogo de requerimientos depurado v3.0

Fuente oficial de requerimientos del proyecto

> **Espejo en Markdown generado a partir del `.xlsx`.** El archivo oficial es `01_Requerimientos/RequerimientosAtomizados_Depuracion_Alcance.xlsx`: si el `.md` y el Excel difieren, **manda el Excel**. No editar este archivo a mano; se regenera con el script de conversión.

| | |
| :--- | :--- |
| Origen | `01_Requerimientos/RequerimientosAtomizados_Depuracion_Alcance.xlsx` |
| Hojas exportadas | 7 |
| Generado | 2026-09-29 |

## Hojas

1. [0_Lectura](#0-lectura) - 52 filas
2. [1_Catalogo_Atomico](#1-catalogo-atomico) - 307 filas
3. [2_Divisiones](#2-divisiones) - 42 filas
4. [3_Hallazgos_v3](#3-hallazgos-v3) - 8 filas
5. [4_Resumen](#4-resumen) - 9 filas
6. [6_Equivalencia_IDs](#6-equivalencia-ids) - 311 filas
7. [7_Depuracion_Alcance](#7-depuracion-alcance) - 36 filas

---
## 0_Lectura

<!-- hoja: 0_Lectura | filas de datos: 52 -->

CASO 09 — MULTITIENDAS ANCOA S.A. · Licitación TFEP-01/2026

Catálogo atomizado de requerimientos — versión 3.0 (auditoría de atomicidad sobre el catálogo v2.1)

MÉTODO

Entrada

Catálogo v2.1: 202 requerimientos funcionales y 54 no funcionales.

Procedimiento

Cada fila de entrada se evaluó contra las cinco reglas de atomicidad. La que las satisface se conserva con su identificador original; la que las incumple se divide o se reclasifica, y sus resultantes heredan el identificador del padre con sufijo, de modo que la trazabilidad no se rompe.

Identificadores

Los identificadores se renumeraron de forma secuencial y correlativa por tipo: RF-001 a RF-226, RNF-01 a RNF-76 y OP-01 a OP-09, siguiendo el orden de las filas del catálogo. El identificador que cada requerimiento tenía en la versión 3.0 se conserva en la última columna de la hoja 1 y en la hoja 6_Equivalencia_IDs, de modo que la trazabilidad hacia los documentos ya emitidos no se pierde. Toda referencia cruzada dentro del libro fue actualizada al nuevo identificador; las referencias a requerimientos de la versión 2.1 que fueron divididos o reclasificados se mantienen con su código original, porque designan un enunciado que ya no existe como fila del catálogo.

LAS CINCO REGLAS APLICADAS

Regla 1 Conjunción

Un enunciado con «y», «o» o «además» uniendo dos acciones o características se divide.

Regla 2 Verbo único

Cada requerimiento conserva un solo verbo de acción principal.

Regla 3 Testabilidad aislada

Se divide cuando un fallo en una parte oscurece el éxito de otra o cuando no cabe un único caso de prueba Pasa/Falla.

Regla 4 Estructura canónica

[Actor / El Sistema] debe [verbo] [entidad] [condición]. Todo enunciado debe sostenerse solo.

Regla 5 Separación RF/RNF

La funcionalidad no se mezcla con el atributo de calidad. El umbral se extrae a un RNF propio.

Criterio de detención

Para no fragmentar sin límite: se divide cuando cada parte tiene precondición o resultado observable propio; no se divide la enumeración de valores posibles de un mismo campo. Por eso «impedir el acceso anónimo o con credencial compartida» se divide (dos casos negativos distintos) y «registrar el motivo de la devolución: talla, color, expectativa o falla» no se divide (un campo con cuatro valores).

TIPOS

RF

Requerimiento funcional: acción que el sistema ejecuta.

RNF

Requerimiento no funcional: restricción o atributo de calidad, con métrica y método de verificación.

OP

Obligación del PROPONENTE: exigencia de la oferta que no es función del sistema y no admite caso de prueba de software. Se separa del catálogo funcional (ejecuta el hallazgo H-11 de la versión anterior, que lo detectó sin resolverlo).

CÓDIGO DE COLOR DE LA HOJA 1

Amarillo

Requerimiento resultante de una división aplicada en esta pasada.

Naranjo

Requerimiento reclasificado como obligación del PROPONENTE.

Verde

Requerimiento no funcional nuevo, extraído de un funcional por la Regla 5.

Sin color

Requerimiento verificado como atómico y conservado sin cambios.

RESULTADO

Requerimientos funcionales (RF)

226

Requerimientos no funcionales (NFR)

76

Obligaciones del PROPONENTE (OP)

9

Total de filas del catálogo atómico

311

Requerimientos de entrada divididos o reclasificados

41

AVISO: FALTA INFORMACIÓN

Se mantienen los 16 supuestos fundamentados por umbrales ausentes declarados en la versión anterior (hallazgo H-12). Los tres RNF extraídos en esta pasada (RNF-02, RNF-01 y RNF-03) incorporan umbrales propuestos por el PROPONENTE y quedan sujetos a validación en el período de consultas.

Nueve filas del catálogo v2.1 conservan el valor «??» en la columna de revisión, es decir, no fueron confirmadas por el equipo. Se listan en la hoja 3_Hallazgos_v3 y se integran a la RBS como riesgo de requisitos no validados.

## 1_Catalogo_Atomico

<!-- hoja: 1_Catalogo_Atomico | filas de datos: 307 -->

| ID | Tipo | Descripción atómica | Justificación breve de la división | ID de origen | Módulo / Categoría | RN vinculada(s) | Métrica / Umbral | Método de verificación | ID anterior (v3.0) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| RF-001 | RF | El sistema deberá permitir la venta física de la unidad aunque exista una reserva temporal activa en el canal digital. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Ventas en Tienda | RN-10 |  |  | RF-010.6 |
| RF-002 | RF | El sistema deberá exigir credenciales individuales al usuario antes de habilitar cualquier acción. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-044); se verifica el verbo único y se mantiene. | — | Seguridad y Accesos | RN-50, RN-52 |  |  | RF-044.1 |
| RF-003 | RF | El sistema debe impedir el acceso anónimo a una terminal. | La conjunción «o» unía dos controles con casos de prueba negativos distintos: la ausencia de identificación y el uso de una credencial de otra persona. | RF-044.2 | Seguridad y Accesos | RN-50, RN-52 |  |  | RF-044.2a |
| RF-004 | RF | El sistema debe impedir el acceso mediante credencial compartida. | Segundo control del requerimiento original; es el que sostiene RN-50 con 640 terminales para 3.820 personas. | RF-044.2 | Seguridad y Accesos | RN-50, RN-52 |  |  | RF-044.2b |
| RF-005 | RF | El sistema deberá permitir el traspaso de sesión nominativa entre usuarios en una terminal compartida. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-50)); verbo único. No procede división. | — | Seguridad y Accesos | RN-50 |  |  | RF-044.3 |
| RF-006 | RF | El sistema deberá cerrar automáticamente la sesión por inactividad en la terminal compartida. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-50)); verbo único. No procede división. | — | Seguridad y Accesos | RN-50 |  |  | RF-044.4 |
| RF-007 | RF | El sistema deberá impedir la ejecución de la función de originación a un usuario sin capacitación normativa acreditada y vigente. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-53)); verbo único. No procede división. | — | Seguridad y Accesos | RN-53 |  |  | RF-101 |
| RF-008 | RF | El sistema deberá impedir la ejecución de la función de repactación a un usuario sin capacitación normativa acreditada y vigente. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-53)); verbo único. No procede división. | — | Seguridad y Accesos | RN-53 |  |  | RF-102 |
| RF-009 | RF | El sistema deberá revocar automáticamente la habilitación funcional del usuario al vencer su acreditación de capacitación. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-53)); verbo único. No procede división. | — | Seguridad y Accesos | RN-53, RN-52 |  |  | RF-103 |
| RF-010 | RF | El sistema deberá permitir al proveedor patrocinar la habilitación temporal de acceso de su repositor externo, con fecha de término declarada. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-51)); verbo único. No procede división. | — | Seguridad y Accesos | RN-51 |  |  | RF-115 |
| RF-011 | RF | El sistema deberá caducar automáticamente la habilitación de acceso del personal externo al cumplirse su vigencia. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-51)); verbo único. No procede división. | — | Seguridad y Accesos | RN-51 |  |  | RF-116 |
| RF-012 | RF | El sistema deberá registrar de forma individualizada el acceso y la actividad del personal externo. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-51)); verbo único. No procede división. | — | Seguridad y Accesos | RN-51 |  |  | RF-117 |
| RF-013 | RF | El sistema deberá revocar la totalidad de los accesos y credenciales del trabajador a partir del término efectivo de su vínculo. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-52)); verbo único. No procede división. | — | Seguridad y Accesos | RN-52 |  |  | RF-118 |
| RF-014 | RF | El sistema debe conciliar los accesos vigentes contra la nómina activa. | «Conciliar e informar» son dos verbos: el cálculo de la discrepancia y su comunicación. | RF-119 | Seguridad y Accesos | RN-52, RN-51 |  |  | RF-119a |
| RF-015 | RF | El sistema debe informar al oficial de seguridad los accesos huérfanos detectados en la conciliación. | Segunda acción del requerimiento original. | RF-119 | Seguridad y Accesos | RN-52, RN-51 |  |  | RF-119b |
| RF-016 | RF | El sistema deberá propagar el cambio de precio a las 380 líneas de caja. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-006); se verifica el verbo único y se mantiene. | — | Precios y Etiquetado | RN-16, RN-18 |  |  | RF-006.1 |
| RF-017 | RF | El sistema deberá propagar el cambio de precio al canal digital. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-006); se verifica el verbo único y se mantiene. | — | Precios y Etiquetado | RN-16, RN-17 |  |  | RF-006.2 |
| RF-018 | RF | El sistema deberá propagar el cambio de precio a los puntos de exhibición física de cada tienda afectada. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-006); se verifica el verbo único y se mantiene. | — | Precios y Etiquetado | RN-18, RN-19 |  |  | RF-006.3 |
| RF-019 | RF | El sistema deberá permitir al reponedor registrar la referencia y la tienda de la etiqueta cambiada, con el instante del cambio. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-007); se verifica el verbo único y se mantiene. | — | Precios y Etiquetado | RN-19 |  |  | RF-007.1 |
| RF-020 | RF | El sistema deberá registrar la identidad individual del ejecutor del cambio de etiqueta. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-19)); verbo único. No procede división. | — | Precios y Etiquetado | RN-19, RN-50 |  |  | RF-007.2 |
| RF-021 | RF | El sistema deberá permitir al ejecutivo de cumplimiento recuperar el precio publicado de una referencia para una fecha, hora y canal determinados. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Precios y Etiquetado | RN-17 |  |  | RF-008 |
| RF-022 | RF | El sistema deberá obtener el precio vigente de la referencia según el último precio propagado a la etiqueta de esa tienda en la fecha de la venta. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-009); se verifica el verbo único y se mantiene. | — | Precios y Etiquetado | RN-16, RN-18 |  |  | RF-009.1 |
| RF-023 | RF | El sistema deberá cobrar el menor de ambos precios para el consumidor. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-16)); verbo único. No procede división. | — | Precios y Etiquetado | RN-16 |  |  | RF-009.2 |
| RF-024 | RF | El sistema deberá generar un registro de incidente de discrepancia de precio consultable. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-16)); verbo único. No procede división. | — | Precios y Etiquetado | RN-16 |  |  | RF-009.3 |
| OP-01 | OP | El PROPONENTE debe especificar la alternativa de etiquetas electrónicas frente a las demás opciones de resolución de la discrepancia de precio. | No es una función del sistema sino una obligación de la oferta: no admite caso de prueba de software. Además unía «especificar» y «costear». | RF-034 | Obligación del PROPONENTE | RN-59 |  |  | OP-01 |
| OP-02 | OP | El PROPONENTE debe costear la alternativa de etiquetas electrónicas sin asumir su adquisición dentro del alcance. | Segunda obligación del requerimiento original; se verifica en el Entregable 2 de la Oferta Económica. | RF-034 | Obligación del PROPONENTE | RN-59 |  |  | OP-02 |
| RF-027 | RF | El sistema debe generar una alerta operativa al jefe de tienda identificando la etiqueta electrónica no confirmada. | Se retira del enunciado la restricción temporal «antes de la apertura de sala», que es un atributo de calidad y no una función. | RF-042.2 | Precios y Etiquetado | RN-18, RN-59 |  |  | RF-042.2a |
| OP-03 | OP | El PROPONENTE debe especificar la cobertura de despliegue de las etiquetas electrónicas. | Obligación de oferta, no función del sistema. El enunciado unía tres entregables distintos. | RF-043 | Obligación del PROPONENTE | RN-59 |  |  | OP-03 |
| OP-04 | OP | El PROPONENTE debe especificar el hardware requerido por la alternativa de etiquetas electrónicas. | Segundo entregable del requerimiento original. | RF-043 | Obligación del PROPONENTE | RN-59 |  |  | OP-04 |
| OP-05 | OP | El PROPONENTE debe presentar el costo de la alternativa separadamente del resto de la solución. | Tercer entregable; se verifica contra el Formulario E-24. | RF-043 | Obligación del PROPONENTE | RN-59 |  |  | OP-05 |
| RF-028 | RF | El sistema deberá impedir la venta de la referencia al precio nuevo mientras su punto de exhibición no confirme la actualización, salvo que el artículo se encuentre bloqueado para venta. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-18)); verbo único. No procede división. | — | Precios y Etiquetado | RN-18, RN-16 |  |  | RF-064 |
| RF-029 | RF | El sistema deberá generar un indicador diario de puntos de exhibición desactualizados con identificación individual de cada punto. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-18)); verbo único. No procede división. | — | Precios y Etiquetado | RN-18 |  |  | RF-065 |
| RF-030 | RF | El sistema deberá agrupar los cambios de precio de sala en ventanas parametrizadas fuera del horario de atención. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-19)); verbo único. No procede división. | — | Precios y Etiquetado | RN-19 |  |  | RF-066 |
| RF-032 | RF | El sistema deberá evaluar la vigencia de cada promoción al instante de emisión del documento. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-20)); verbo único. No procede división. | — | Precios y Etiquetado | RN-20 |  |  | RF-068 |
| RF-033 | RF | El sistema deberá evaluar la aplicabilidad de la promoción según el canal de la venta. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-20)); verbo único. No procede división. | — | Precios y Etiquetado | RN-20 |  |  | RF-069 |
| RF-034 | RF | El sistema deberá evaluar la aplicabilidad de la promoción según la tienda en que se realiza la venta. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-20)); verbo único. No procede división. | — | Precios y Etiquetado | RN-20 |  |  | RF-070 |
| RF-035 | RF | El sistema deberá crear una reserva temporal para la unidad agregada al carro. | Atómico. Resultado de una consolidación previa; verbo único verificado. | — | Pedidos y Cumplimiento | RN-10 |  |  | RF-010.1 |
| RF-036 | RF | El sistema deberá permitir parametrizar el período de vigencia de la reserva temporal. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Pedidos y Cumplimiento | RN-10 |  |  | RF-010.2 |
| RF-037 | RF | El sistema deberá mantener activa la reserva mientras el cliente mantenga actividad, conforme al período parametrizado. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Pedidos y Cumplimiento | RN-10 |  |  | RF-010.3 |
| RF-038 | RF | El sistema deberá impedir que una misma unidad sea comprometida simultáneamente en más de una operación de venta digital. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Pedidos y Cumplimiento | RN-10, RN-08 |  |  | RF-010.4 |
| RF-039 | RF | El sistema debe liberar la reserva temporal al expirar su período de vigencia. | Unía dos verbos («liberar» y «devolver») sobre dos entidades distintas: la reserva y la unidad. La liberación puede tener éxito mientras la devolución al disponible falla. | RF-010.5 | Pedidos y Cumplimiento | RN-10 |  |  | RF-010.5a |
| RF-040 | RF | El sistema debe devolver la unidad liberada al disponible para vender. | Segunda acción del requerimiento original: el reintegro al ATP se prueba de forma independiente de la liberación de la reserva. | RF-010.5 | Pedidos y Cumplimiento | RN-10 |  |  | RF-010.5b |
| RF-041 | RF | El sistema deberá liberar de inmediato la reserva digital de esa unidad, sin esperar la expiración del período. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Pedidos y Cumplimiento | RN-10 |  |  | RF-010.7 |
| RF-042 | RF | El sistema deberá aplicar el período de vigencia de reserva reducido declarado como parámetro para el evento anual. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-10)); verbo único. No procede división. | — | Pedidos y Cumplimiento | RN-10, RN-57 |  |  | RF-010.8 |
| RF-043 | RF | El sistema deberá preautorizar el medio de pago al aceptar el pedido, sin capturar el cobro. | Atómico tras la reformulación de la versión anterior; verbo único verificado. No procede nueva división. | — | Pedidos y Cumplimiento | RN-21 |  |  | RF-011.1 |
| RF-044 | RF | El sistema deberá verificar la existencia física real de la unidad en el punto asignado antes de habilitar la captura del cobro. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Pedidos y Cumplimiento | RN-21 |  |  | RF-011.2 |
| RF-045 | RF | El sistema deberá capturar el cobro únicamente al registrarse el evento de confirmación de la preparacion física. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-21)); verbo único. No procede división. | — | Pedidos y Cumplimiento | RN-21 |  |  | RF-011.3 |
| RF-046 | RF | El sistema deberá determinar automáticamente la alternativa de resolución aplicable según el motor de reglas (cancelar, sustituir, derivar a tercero o entrega diferida). | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Pedidos y Cumplimiento | RN-23 |  |  | RF-011.4 |
| RF-047 | RF | El sistema deberá requerir la aceptación explícita del cliente antes de capturar el cobro. | Atómico tras la reformulación de la versión anterior; verbo único verificado. No procede nueva división. | — | Pedidos y Cumplimiento | RN-23, RN-21 |  |  | RF-011.5 |
| RF-048 | RF | El sistema deberá anular la preautorización de pago del pedido. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-046 original); se verifica el verbo único y se mantiene. | — | Pedidos y Cumplimiento | RN-21, RN-23 |  |  | RF-011.6 |
| RF-049 | RF | El sistema deberá cancelar el pedido registrando el motivo de la cancelación. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-046 original); se verifica el verbo único y se mantiene. | — | Pedidos y Cumplimiento | RN-23 |  |  | RF-011.7 |
| RF-050 | RF | El sistema deberá generar la conciliación diaria de preautorizaciones vencidas sin captura. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-21)); verbo único. No procede división. | — | Pedidos y Cumplimiento | RN-21 |  |  | RF-011.8 |
| RF-051 | RF | El sistema deberá notificar al cliente el cambio de estado de su pedido antes de efectuar cualquier cobro definitivo. | Atómico. Reclasificado desde RNF-51 en la versión anterior; verbo único verificado. | — | Pedidos y Cumplimiento | RN-23 |  |  | RF-011.9 |
| RF-052 | RF | El sistema deberá permitir a todos los actores consultar el estado del pedido desde una única fuente de verdad. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Pedidos y Cumplimiento | RN-23, RN-28 |  |  | RF-012 |
| RF-053 | RF | El sistema deberá permitir marcar como no elegible para cumplimiento digital el stock de exhibición de las categorías declaradas. | Atómico tras la reformulación de la versión anterior; verbo único verificado. No procede nueva división. | — | Pedidos y Cumplimiento | RN-22, RN-08 |  |  | RF-013 |
| RF-054 | RF | El sistema debe calcular la base de comisión reconociendo al vendedor y a la tienda de origen de la unidad. | El requerimiento unía el cálculo con su validación previa contra inventario. Son dos comportamientos con resultados distintos. | RF-014 | Pedidos y Cumplimiento | RN-54 |  |  | RF-014a |
| RF-055 | RF | El sistema debe condicionar la transmisión de la base de comisión al movimiento real de inventario verificado en bodega. | El control de liberación es la garantía de RN-33 y debe poder fallar sin invalidar el cálculo. | RF-014 | Pedidos y Cumplimiento | RN-54 |  |  | RF-014b |
| RF-056 | RF | El sistema deberá reasignar el pedido a otro punto de despacho con existencia disponible. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-015); se verifica el verbo único y se mantiene. | — | Pedidos y Cumplimiento | RN-23 |  |  | RF-015.1 |
| RF-057 | RF | El sistema deberá impedir una segunda reasignación del mismo pedido. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-23)); verbo único. No procede división. | — | Pedidos y Cumplimiento | RN-23 |  |  | RF-015.2 |
| RF-058 | RF | El sistema deberá acotar la reasignación a la ventana de tiempo parametrizada. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-23)); verbo único. No procede división. | — | Pedidos y Cumplimiento | RN-23 |  |  | RF-015.3 |
| RF-059 | RF | El sistema deberá ofrecer al cliente un producto equivalente. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-23)); verbo único. No procede división. | — | Pedidos y Cumplimiento | RN-23 |  |  | RF-015.4 |
| RF-060 | RF | El sistema deberá ofrecer al cliente la espera compensada con la compensación parametrizada. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-23)); verbo único. No procede división. | — | Pedidos y Cumplimiento | RN-23 |  |  | RF-015.5 |
| RF-061 | RF | El sistema deberá ofrecer al cliente la liberacion del pedido con anulación de la preautorización. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-23)); verbo único. No procede división. | — | Pedidos y Cumplimiento | RN-23, RN-21 |  |  | RF-015.6 |
| RF-062 | RF | El sistema debe monitorear el tiempo restante de cada pedido respecto de su fecha prometida de entrega. | «Monitorear y priorizar» son dos verbos de acción sobre entidades distintas: la medición y la cola de preparación. | RF-035 | Pedidos y Cumplimiento | RN-24 |  |  | RF-035a |
| RF-063 | RF | El sistema debe priorizar la preparación del pedido al alcanzar el umbral parametrizado de tiempo restante. | La priorización es una acción con resultado observable propio. | RF-035 | Pedidos y Cumplimiento | RN-24 |  |  | RF-035b |
| RF-064 | RF | El sistema debe permitir al cliente no autenticado consultar el precio vigente de una referencia. | Unía tres consultas distintas del portal público. Cada una es un caso de prueba independiente. | RF-036A | Pedidos y Cumplimiento | RN-17, RN-11 |  |  | RF-036A.1 |
| RF-065 | RF | El sistema debe permitir al cliente no autenticado consultar la disponibilidad de la referencia por tienda. | Segunda consulta del requerimiento original. | RF-036A | Pedidos y Cumplimiento | RN-17, RN-11 |  |  | RF-036A.2 |
| RF-066 | RF | El sistema debe permitir al cliente no autenticado consultar la disponibilidad de la referencia para despacho. | Tercera consulta del requerimiento original; su fuente de datos difiere de la consulta por tienda. | RF-036A | Pedidos y Cumplimiento | RN-17, RN-11 |  |  | RF-036A.3 |
| RF-067 | RF | El sistema debe permitir al cliente autenticado consultar sus compras. | Unía cuatro consultas sobre entidades distintas, dos de ellas del ámbito fiscalizado. La división es además condición para aplicar la frontera de datos (hallazgo H-04). | RF-037 | Pedidos y Cumplimiento | RN-02, RN-04 |  |  | RF-037.1 |
| RF-068 | RF | El sistema debe permitir al cliente autenticado consultar sus devoluciones. | Segunda consulta del requerimiento original, del ámbito retail. | RF-037 | Pedidos y Cumplimiento | RN-02, RN-04 |  |  | RF-037.2 |
| RF-069 | RF | El sistema debe permitir al cliente autenticado consultar su estado de cuenta. | Tercera consulta, del ámbito de la filial emisora: exige resolución de identidad por la tabla de correspondencia de RF-174. | RF-037 | Pedidos y Cumplimiento | RN-02, RN-04 |  |  | RF-037.3 |
| RF-070 | RF | El sistema debe permitir al cliente autenticado consultar sus documentos. | Cuarta consulta del requerimiento original. | RF-037 | Pedidos y Cumplimiento | RN-02, RN-04 |  |  | RF-037.4 |
| RF-071 | RF | El sistema deberá calcular la base de comisión considerando el canal de origen y el canal de cumplimiento cuando estos difieran. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Pedidos y Cumplimiento | RN-54 |  |  | RF-040 |
| RF-072 | RF | El sistema debe permitir al ejecutivo de mesón consultar el estado real del pedido. | Unía dos consultas y una acción de resolución en una sola fila. | RF-049 | Pedidos y Cumplimiento | RN-16, RN-23 |  |  | RF-049a |
| RF-073 | RF | El sistema debe permitir al ejecutivo de mesón consultar el precio aplicado al pedido. | Segunda consulta del requerimiento original. | RF-049 | Pedidos y Cumplimiento | RN-16, RN-23 |  |  | RF-049b |
| RF-074 | RF | El sistema debe permitir al ejecutivo de mesón ofrecer al cliente las opciones de resolución definidas en RF-059, RF-060 y RF-061. | Acción de resolución, separada de las consultas que la preceden. | RF-049 | Pedidos y Cumplimiento | RN-16, RN-23 |  |  | RF-049c |
| RF-075 | RF | El sistema deberá excluir al centro de distribución de Concepción como origen de promesa de entrega en el canal digital mientras no este acreditado su sistema de gestión de almacenes. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-15)); verbo único. No procede división. | — | Pedidos y Cumplimiento | RN-15 |  |  | RF-057 |
| RF-076 | RF | El sistema deberá calcular el costo total de servir de cada punto de despacho candidato, incorporando costo logístico, costo de oportunidad de sala y plazo comprometido. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-22)); verbo único. No procede división. | — | Pedidos y Cumplimiento | RN-22 |  |  | RF-071 |
| RF-077 | RF | El sistema deberá seleccionar como punto de despacho aquel de menor costo total de servir. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-22)); verbo único. No procede división. | — | Pedidos y Cumplimiento | RN-22 |  |  | RF-072 |
| RF-078 | RF | El sistema deberá registrar el valor de cada término del costo total de servir que fundamento la seleccion. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-22)); verbo único. No procede división. | — | Pedidos y Cumplimiento | RN-22 |  |  | RF-073 |
| RF-079 | RF | El sistema deberá calcular la fecha prometida de entrega en función del punto de despacho, la capacidad de preparacion y el transportista asignado. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-24)); verbo único. No procede división. | — | Pedidos y Cumplimiento | RN-24 |  |  | RF-074 |
| RF-080 | RF | El sistema deberá impedir la publicación de un plazo fijo de catálogo como fecha prometida de entrega. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-24)); verbo único. No procede división. | — | Pedidos y Cumplimiento | RN-24 |  |  | RF-075 |
| RF-081 | RF | El sistema deberá calcular el cumplimiento de la promesa de entrega por pedido individual. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-24)); verbo único. No procede división. | — | Pedidos y Cumplimiento | RN-24 |  |  | RF-076 |
| RF-082 | RF | El sistema deberá detectar la pérdida del enlace externo y conmutar automáticamente la tienda a modo desconectado. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-029); se verifica el verbo único y se mantiene. | — | Operación de Tienda | RN-46 |  |  | RF-029.1 |
| RF-083 | RF | El sistema deberá permitir al cajero registrar una venta en modo desconectado. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-029); se verifica el verbo único y se mantiene. | — | Operación de Tienda | RN-46 |  |  | RF-029.2 |
| RF-084 | RF | El sistema deberá permitir al cajero cobrar la venta en modo desconectado. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-029); se verifica el verbo único y se mantiene. | — | Operación de Tienda | RN-46 |  |  | RF-029.3 |
| RF-085 | RF | El sistema deberá aplicar las promociones vigentes en modo desconectado, evaluadas según RF-032, RF-033 y RF-034. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-029); se verifica el verbo único y se mantiene. | — | Operación de Tienda | RN-46, RN-20 |  |  | RF-029.4 |
| RF-086 | RF | El sistema deberá emitir el documento de venta en contingencia utilizando folios previamente asignados por el sistema de gestión empresarial. | Atómico tras la reformulación de la versión anterior; verbo único verificado. No procede nueva división. | — | Operación de Tienda | RN-46, RN-49 |  |  | RF-029.5 |
| RF-087 | RF | El sistema deberá permitir al vendedor consultar la existencia local de la tienda en modo desconectado. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-029); se verifica el verbo único y se mantiene. | — | Operación de Tienda | RN-46 |  |  | RF-029.6 |
| RF-088 | RF | El sistema deberá detectar el restablecimiento del enlace y conmutar la tienda a modo conectado. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-029); se verifica el verbo único y se mantiene. | — | Operación de Tienda | RN-48 |  |  | RF-029.7 |
| RF-089 | RF | El sistema deberá permitir el otorgamiento de crédito en modo desconectado exclusivamente contra cupo preaprobado vigente almacenado en caché local. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-47)); verbo único. No procede división. | — | Operación de Tienda | RN-47 |  |  | RF-104 |
| RF-090 | RF | El sistema deberá aplicar el tope de monto parametrizado a cada operación de crédito cursada en modo desconectado. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-47)); verbo único. No procede división. | — | Operación de Tienda | RN-47 |  |  | RF-105 |
| RF-091 | RF | El sistema deberá aplicar el tope parametrizado de número de operaciones de crédito en modo desconectado. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-47)); verbo único. No procede división. | — | Operación de Tienda | RN-47 |  |  | RF-106 |
| RF-092 | RF | El sistema deberá impedir la apertura de una tarjeta nueva en modo desconectado. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-47)); verbo único. No procede división. | — | Operación de Tienda | RN-47 |  |  | RF-107 |
| RF-093 | RF | El sistema deberá impedir la ampliación de cupo en modo desconectado. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-47)); verbo único. No procede división. | — | Operación de Tienda | RN-47 |  |  | RF-108 |
| RF-094 | RF | El sistema deberá marcar la operación como cursada en modo desconectado para su validación posterior. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-47)); verbo único. No procede división. | — | Operación de Tienda | RN-47, RN-48 |  |  | RF-109 |
| RF-095 | RF | El sistema debe reconciliar hacia los sistemas centrales la totalidad de las ventas registradas en modo desconectado. | Ventas y documentos tributarios siguen rutas distintas: los documentos los emite el sistema de gestión empresarial (RN-49). | RF-110 | Operación de Tienda | RN-48 |  |  | RF-110a |
| RF-096 | RF | El sistema debe reconciliar hacia los sistemas centrales la totalidad de los documentos emitidos en modo desconectado. | Segunda reconciliación del requerimiento original; resuelve además el hallazgo H-05. | RF-110 | Operación de Tienda | RN-48 |  |  | RF-110b |
| RF-097 | RF | El sistema deberá procesar la reconciliación de forma idempotente, impidiendo la duplicación de ventas o documentos ante reintentos. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-48)); verbo único. No procede división. | — | Operación de Tienda | RN-48 |  |  | RF-111 |
| RF-098 | RF | El sistema deberá resolver el conflicto de existencia comprometida aplicando la regla de precedencia declarada, produciendo el mismo resultado ante repetición. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-48)); verbo único. No procede división. | — | Operación de Tienda | RN-48, RN-08 |  |  | RF-112 |
| RF-099 | RF | El sistema deberá generar un informe de excepciones de la reconciliación, identificando cada conflicto resuelto y su regla aplicada. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-48)); verbo único. No procede división. | — | Operación de Tienda | RN-48 |  |  | RF-113 |
| RF-100 | RF | El sistema deberá enrutar la emisión de todo documento tributario hacia el sistema de gestión empresarial como único emisor. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-49)); verbo único. No procede división. | — | Operación de Tienda | RN-49 |  |  | RF-114 |
| RF-101 | RF | El sistema deberá permitir al vendedor de piso consultar la disponibilidad para vender de una referencia. | Atómico tras la reformulación de la versión anterior; verbo único verificado. No procede nueva división. | — | Operación de Tienda | RN-09, RN-45 (propuesta) |  |  | RF-039 |
| OP-06 | OP | El PROPONENTE debe especificar la cantidad de dispositivos móviles requeridos por tienda y por departamento. | Obligación de oferta derivada de la exclusión del Capítulo 11: el hardware lo adquiere el CLIENTE. No es función del sistema. | RF-120 | Obligación del PROPONENTE | RN-60 |  |  | OP-06 |
| OP-07 | OP | El PROPONENTE debe especificar las características técnicas de los dispositivos móviles requeridos. | Obligación de oferta; se verifica documentalmente y no por prueba de sistema. | RF-121 | Obligación del PROPONENTE | RN-60, RN-50 |  |  | OP-07 |
| OP-08 | OP | El PROPONENTE debe presentar el análisis de hacer o comprar del centro de distribución de Concepción con sus tres alternativas. | Obligación de oferta (PMBOK 6.ª ed., §12.1.3.5). El enunciado unía además el análisis con la declaración de su impacto. | RF-122 | Obligación del PROPONENTE | RN-61, RN-15 |  |  | OP-08 |
| OP-09 | OP | El PROPONENTE debe declarar el impacto de la alternativa seleccionada sobre el cumplimiento de RN-15. | Segunda obligación del requerimiento original. | RF-122 | Obligación del PROPONENTE | RN-61, RN-15 |  |  | OP-09 |
| RF-102 | RF | El sistema debe permitir al vendedor de marketplace declarar la existencia de sus referencias. | «Declarar y actualizar» son dos operaciones con precondiciones distintas (alta inicial frente a modificación). | RF-016A.1 | Marketplace | RN-32 |  |  | RF-016A.1a |
| RF-103 | RF | El sistema debe permitir al vendedor de marketplace actualizar la existencia previamente declarada. | Segunda operación del requerimiento original. | RF-016A.1 | Marketplace | RN-32 |  |  | RF-016A.1b |
| RNF-02 | RNF | La interfaz de declaración de existencia del vendedor de marketplace debe estar disponible de forma continua. | «En cualquier momento» es una restricción de disponibilidad, no una función. Se extrae conforme a la Regla 5. | RF-016A.1 | Disponibilidad | RN-32 | 24x7x365; disponibilidad >= 99,5 % (supuesto fundamentado). | Medición mensual de disponibilidad de la interfaz de sincronización de catálogo. | NFR-36 |
| RF-104 | RF | El sistema deberá registrar cada actualización de existencia declarada con su fecha y hora. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-016A); se verifica el verbo único y se mantiene. | — | Marketplace | RN-32 |  |  | RF-016A.2 |
| RF-105 | RF | El sistema deberá calcular los indicadores de nivel de servicio por vendedor externo según las reglas publicadas. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Marketplace | RN-30 |  |  | RF-016B |
| RF-106 | RF | El sistema deberá notificar al vendedor de marketplace la recepción de la devolución en el momento en que se registra. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-017); se verifica el verbo único y se mantiene. | — | Marketplace | RN-28 |  |  | RF-017.1 |
| RF-107 | RF | El sistema deberá permitir al ejecutivo registrar que parte asume el costo de la devolución. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-017); se verifica el verbo único y se mantiene. | — | Marketplace | RN-28, RN-33 |  |  | RF-017.2 |
| RF-108 | RF | El sistema deberá permitir al ejecutivo registrar la prestación entregada al cliente (reparación, reposición o devolución del precio). | Atómico. División ya aplicada en la versión anterior (Dividido de RF-017); se verifica el verbo único y se mantiene. | — | Marketplace | RN-28, RN-29 |  |  | RF-017.3 |
| RF-109 | RF | El sistema deberá publicar únicamente la existencia declarada en la última actualización vigente del vendedor. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Marketplace | RN-32 |  |  | RF-018 |
| RF-110 | RF | El sistema debe permitir al vendedor de marketplace consultar el estado de cada pedido intermediado. | Unía tres consultas del portal del vendedor con fuentes de datos distintas. | RF-038 | Marketplace | RN-30 |  |  | RF-038.1 |
| RF-111 | RF | El sistema debe permitir al vendedor de marketplace consultar las devoluciones de sus pedidos. | Segunda consulta del requerimiento original. | RF-038 | Marketplace | RN-30 |  |  | RF-038.2 |
| RF-112 | RF | El sistema debe permitir al vendedor de marketplace consultar su evaluación de desempeño vigente. | Tercera consulta; depende del cálculo de RF-105 y falla de forma independiente. | RF-038 | Marketplace | RN-30 |  |  | RF-038.3 |
| RF-113 | RF | El sistema debe identificar visiblemente al vendedor de la unidad en el catálogo, la ficha de producto y el proceso de compra. | «Quién vende» y «quién despacha» son dos datos distintos que pueden diferir en un mismo pedido. | RF-048.1 | Marketplace | RN-43 (propuesta), RN-25 |  |  | RF-048.1a |
| RF-114 | RF | El sistema debe identificar visiblemente a quien despacha la unidad en el catálogo, la ficha de producto y el proceso de compra. | Segundo dato del requerimiento original. | RF-048.1 | Marketplace | RN-43 (propuesta), RN-25 |  |  | RF-048.1b |
| RF-115 | RF | El sistema debe mostrar las condiciones de devolución aplicables a la unidad. | Devolución voluntaria y garantía legal son regímenes jurídicos distintos y no pueden validarse con un mismo caso de prueba. | RF-048.2 | Marketplace | RN-43 (propuesta), RN-26 |  |  | RF-048.2a |
| RF-116 | RF | El sistema debe mostrar las condiciones de garantía legal aplicables a la unidad. | Segundo régimen del requerimiento original (Ley N° 19.496). | RF-048.2 | Marketplace | RN-43 (propuesta), RN-26 |  |  | RF-048.2b |
| RF-117 | RF | El sistema deberá impedir que un pedido intermediado comprometa existencia propia de la compañía. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-25)); verbo único. No procede división. | — | Marketplace | RN-25 |  |  | RF-077 |
| RF-118 | RF | El sistema deberá impedir que una unidad de inventario propio sea asignada al cumplimiento de un pedido de marketplace. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-25)); verbo único. No procede división. | — | Marketplace | RN-25 |  |  | RF-078 |
| RF-119 | RF | El sistema deberá registrar el acuse de conocimiento de las reglas de evaluación por parte de cada vendedor externo. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-30)); verbo único. No procede división. | — | Marketplace | RN-30 |  |  | RF-079 |
| RF-120 | RF | El sistema deberá impedir la aplicación de una regla de evaluación a un vendedor que no tenga acuse de conocimiento previo de esa regla. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-30)); verbo único. No procede división. | — | Marketplace | RN-30 |  |  | RF-080 |
| RF-121 | RF | El sistema deberá determinar la consecuencia escalonada aplicable según la matriz de escalamiento parametrizada (advertencia, restricción de publicación, suspensión). | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-31)); verbo único. No procede división. | — | Marketplace | RN-31 |  |  | RF-081 |
| RF-122 | RF | El sistema deberá requerir la ejecución de la sanción por el rol nominado en la matriz de escalamiento. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-31)); verbo único. No procede división. | — | Marketplace | RN-31 |  |  | RF-082 |
| RF-123 | RF | El sistema deberá registrar la trazabilidad de la sanción aplicada, indicando regla incumplida, consecuencia, rol ejecutor e instante. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-31)); verbo único. No procede división. | — | Marketplace | RN-31 |  |  | RF-083 |
| RF-124 | RF | El sistema deberá despublicar automáticamente la oferta cuyo stock declarado haya superado el plazo de vigencia sin actualización. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-32)); verbo único. No procede división. | — | Marketplace | RN-32 |  |  | RF-084 |
| RF-125 | RF | El sistema deberá calcular e informar al sistema de gestión empresarial la base de comisión de marketplace sobre la venta efectivamente cumplida | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-33)); verbo único. No procede división. | — | Marketplace | RN-33 |  |  | RF-085 |
| RF-126 | RF | El sistema deberá notificar al sistema de gestión empresarial la anulación de la base de comisión calculada cuando ocurra una devolución o cancelación. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-33)); verbo único. No procede división. | — | Marketplace | RN-33 |  |  | RF-086 |
| RF-127 | RF | El sistema deberá calcular la existencia disponible para vender restando de la existencia registrada las reservas vigentes, el comprometido no despachado y el colchón de confianza aplicable. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-001); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-08, RN-09 |  |  | RF-001.1 |
| RF-128 | RF | El sistema deberá determinar el valor del colchón de confianza aplicable en función de la categoría del artículo. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-001); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-09 |  |  | RF-001.2 |
| RF-129 | RF | El sistema deberá determinar el valor del colchón de confianza aplicable en función del punto de existencia. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-001); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-09 |  |  | RF-001.3 |
| RF-130 | RF | El sistema deberá registrar la traza del cálculo del disponible, incluyendo el valor de cada término de la fórmula y la versión de parámetros aplicada. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-09)); verbo único. No procede división. | — | Inventario y Disponibilidad | RN-09 |  |  | RF-001.4 |
| RF-131 | RF | El sistema deberá permitir parametrizar la frecuencia de conteo cíclico por categoría. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-002); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-13 |  |  | RF-002.1 |
| RF-132 | RF | El sistema deberá permitir parametrizar el método de conteo por categoría. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-002); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-13 |  |  | RF-002.2 |
| RF-133 | RF | El sistema deberá permitir parametrizar el criterio de gatillo de recuento extraordinario por categoría. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-002); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-13 |  |  | RF-002.3 |
| RF-134 | RF | El sistema deberá generar la programación de conteos cíclicos según la frecuencia parametrizada de cada categoría. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-002); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-13 |  |  | RF-002.4 |
| RF-135 | RF | El sistema debe permitir registrar el resultado del conteo cíclico. | Se retira «sin bloquear la operación de venta de la sala», que es una restricción de calidad sobre la operación concurrente. | RF-002.5 | Inventario y Disponibilidad | RN-13 |  |  | RF-002.5a |
| RNF-03 | RNF | El registro del conteo cíclico no debe bloquear ni degradar la operación de venta de la sala. | Restricción extraída de RF-002.5 conforme a la Regla 5. | RF-002.5 | Desempeño | RN-13 | 0 bloqueos de la línea de caja durante el conteo; degradación del tiempo de venta <= 5 % respecto de la línea base de RNF-18. | Prueba de conteo cíclico ejecutado en horario de venta con medición simultánea del tiempo de transacción en caja. | NFR-38 |
| RF-136 | RF | El sistema deberá señalar automáticamente los pasillos o referencias que requieren recuento extraordinario. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-002); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-13 |  |  | RF-002.6 |
| RF-137 | RF | El sistema deberá calcular la exactitud de inventario resultante por categoría. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-002); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-13, RN-11 |  |  | RF-002.7 |
| RF-138 | RF | El sistema deberá permitir clasificar cada diferencia detectada en uno de los componentes de merma definidos (pérdida física, daño no dado de baja, error de recepción, unidad mal ubicada, devolución mal reintegrada, error de digitación). | Atómico. División ya aplicada en la versión anterior (Dividido de RF-003); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-12 |  |  | RF-003.1 |
| RF-139 | RF | El sistema deberá impedir el cierre de un ajuste de inventario que no tenga asignado un componente de merma. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-12)); verbo único. No procede división. | — | Inventario y Disponibilidad | RN-12 |  |  | RF-003.2 |
| RF-140 | RF | El sistema deberá cuantificar el monto y la proporción de cada componente de merma sobre el total del período. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-003); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-12 |  |  | RF-003.3 |
| RF-141 | RF | El sistema deberá generar el informe mensual de merma cuya suma de componentes sea igual al total registrado en el período. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-003); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-12 |  |  | RF-003.4 |
| RF-142 | RF | El sistema deberá exigir al analista comercial completar los atributos obligatorios de la referencia (categoría, dimensiones, fragilidad, volumen, restricción de despacho) antes de guardar el registro como apto para uso operativo. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Inventario y Disponibilidad | RN-07 (propuesta) |  |  | RF-004A |
| RF-143 | RF | El sistema deberá impedir la publicación de esa referencia en el canal digital mientras no cuente con los atributos obligatorios completos. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Inventario y Disponibilidad | RN-07 (propuesta) |  |  | RF-004B |
| RF-144 | RF | El sistema deberá generar automáticamente la propuesta diaria de reposición utilizando el disponible para vender calculado en RF-127. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-005); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-08, RN-09 |  |  | RF-005.1 |
| RF-145 | RF | El sistema deberá permitir al planificador de logística ajustar la propuesta de reposición antes de confirmar el envío. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-005); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-09 |  |  | RF-005.2 |
| RF-146 | RF | El sistema deberá registrar el ajuste realizado indicando usuario, valor propuesto, valor confirmado e instante. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-09)); verbo único. No procede división. | — | Inventario y Disponibilidad | RN-09 |  |  | RF-005.3 |
| RF-147 | RF | El sistema debe generar un reporte periódico de referencias con atributos obligatorios incompletos. | La conjunción «o» unía dos reportes de origen distinto: calidad del maestro y errores de publicación. | RF-045 | Inventario y Disponibilidad | RN-07 (propuesta) |  |  | RF-045a |
| RF-148 | RF | El sistema debe generar un reporte periódico de publicaciones fallidas indicando la causa del error. | Segundo reporte del requerimiento original. | RF-045 | Inventario y Disponibilidad | RN-07 (propuesta) |  |  | RF-045b |
| RF-149 | RF | El sistema debe permitir al gerente de logística definir el valor del colchón de confianza por categoría. | La conjunción «o» unía dos configuraciones distintas, cada una con su propia precondición y su propio efecto sobre el cálculo del disponible. | RF-046.1 | Inventario y Disponibilidad | RN-09 |  |  | RF-046.1a |
| RF-150 | RF | El sistema debe permitir al gerente de logística definir el valor del colchón de confianza por punto de existencia. | Segunda configuración; se alinea con la división ya aplicada en RF-128 y RF-129. | RF-046.1 | Inventario y Disponibilidad | RN-09 |  |  | RF-046.1b |
| RF-151 | RF | El sistema deberá registrar quien definio o modifico el colchón, cuando, el valor anterior y el valor nuevo. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-046); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-09 |  |  | RF-046.2 |
| RF-152 | RF | El sistema deberá sugerir un valor de referencia del colchón calculado a partir del histórico de ventas y quiebres de la categoría. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-046); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-09 |  |  | RF-046.3 |
| RF-153 | RF | El sistema deberá permitir al vendedor de piso registrar las unidades que ingresan al probador. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-047); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-42 (propuesta) |  |  | RF-047.1 |
| RF-154 | RF | El sistema deberá excluir del disponible para vender las unidades registradas en probador. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-047); se verifica el verbo único y se mantiene. | — | Inventario y Disponibilidad | RN-42 (propuesta), RN-09 |  |  | RF-047.2 |
| RF-155 | RF | El sistema debe permitir al vendedor de piso confirmar el reingreso a sala de la unidad registrada en probador. | La conjunción «o» unía dos desenlaces excluyentes del ciclo de probador, con efectos distintos sobre el disponible. | RF-047.3 | Inventario y Disponibilidad | RN-42 (propuesta) |  |  | RF-047.3a |
| RF-156 | RF | El sistema debe permitir al vendedor de piso registrar la venta de la unidad registrada en probador. | Segundo desenlace del requerimiento original. | RF-047.3 | Inventario y Disponibilidad | RN-42 (propuesta) |  |  | RF-047.3b |
| RF-157 | RF | El sistema deberá impedir que cualquier canal de venta consuma el saldo bruto de inventario para publicar o comprometer existencia. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-08)); verbo único. No procede división. | — | Inventario y Disponibilidad | RN-08 |  |  | RF-054 |
| RF-158 | RF | El sistema debe calcular el porcentaje de error probable de la referencia en función de su categoría. | Se alinea con la división ya aplicada al colchón de confianza en RF-128 y RF-129: cada dimensión del cálculo se prueba por separado. | RF-058 | Inventario y Disponibilidad | RN-11 |  |  | RF-058a |
| RF-159 | RF | El sistema debe calcular el porcentaje de error probable de la referencia en función de su punto de existencia. | Segunda dimensión del cálculo. | RF-058 | Inventario y Disponibilidad | RN-11 |  |  | RF-058b |
| RF-160 | RF | El sistema deberá mostrar al cliente el porcentaje de error probable calculado en RF-058 junto a la disponibilidad publicada. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-11)); verbo único. No procede división. | — | Inventario y Disponibilidad | RN-11 |  |  | RF-059 |
| RF-161 | RF | El sistema deberá mostrar al vendedor de piso el porcentaje de error probable calculado en RF-058. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-11)); verbo único. No procede división. | — | Inventario y Disponibilidad | RN-11, RN-45 (propuesta) |  |  | RF-060 |
| RF-162 | RF | El sistema deberá generar una alerta interna dirigida al rol facultado cuando la exactitud de una categoría caiga bajo el umbral definido. | Atómico. Reclasificado desde RNF-51 en la versión anterior; verbo único verificado. | — | Inventario y Disponibilidad | RN-11 |  |  | RF-061 |
| RF-163 | RF | El sistema deberá permitir exclusivamente al rol facultado suspender manualmente la publicación de una categoría. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-11 y RN-57)); verbo único. No procede división. | — | Inventario y Disponibilidad | RN-11, RN-57 |  |  | RF-062 |
| RF-164 | RF | El sistema deberá abstenerse de suspender automáticamente la publicación de una categoría que no tenga una regla de degradación declarada y aprobada previamente. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-11)); verbo único. No procede división. | — | Inventario y Disponibilidad | RN-11, RN-57 |  |  | RF-063 |
| RF-165 | RF | El sistema deberá registrar cada cruce de información ejecutado entre ámbitos, indicando el dato cruzado, la finalidad, la base de licitud, la autorización nominada y el instante. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-025); se verifica el verbo único y se mantiene. | — | Gobernanza de Datos | RN-02 |  |  | RF-025.1 |
| RF-166 | RF | El sistema deberá bloquear todo intento de cruce de información que no corresponda a una interfaz declarada en el inventario de flujos autorizados. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-02)); verbo único. No procede división. | — | Gobernanza de Datos | RN-02, RN-05 |  |  | RF-025.2 |
| RF-167 | RF | El sistema deberá registrar el intento de cruce bloqueado con el componente origen, el dato solicitado y el instante. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-02)); verbo único. No procede división. | — | Gobernanza de Datos | RN-02 |  |  | RF-025.3 |
| RF-168 | RF | El sistema debe permitir al oficial de cumplimiento mantener el inventario de interfaces de cruce declaradas. | «Mantener exigiendo» encierra dos comportamientos: la administración del inventario y la validación de completitud. | RF-025.4 | Gobernanza de Datos | RN-02 |  |  | RF-025.4a |
| RF-169 | RF | El sistema debe impedir el registro de una interfaz de cruce que no declare finalidad, base de licitud y autorización nominada. | Validación de completitud con caso de prueba negativo propio (Ley N° 21.719). | RF-025.4 | Gobernanza de Datos | RN-02 |  |  | RF-025.4b |
| RF-170 | RF | El sistema deberá excluir del catálogo de atributos disponibles en el motor de campañas todo atributo de origen financiero (mora, deuda, cupo utilizado, comportamiento de pago). | Atómico. División ya aplicada en la versión anterior (Dividido de RF-032); se verifica el verbo único y se mantiene. | — | Gobernanza de Datos | RN-03 |  |  | RF-032.1 |
| RF-171 | RF | El sistema deberá rechazar la ejecución de toda facilidad comercial que invoque un atributo de origen financiero sin un registro de cruce autorizado asociado. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-032); se verifica el verbo único y se mantiene. | — | Gobernanza de Datos | RN-05, RN-02 |  |  | RF-032.2 |
| RF-172 | RF | El sistema deberá rechazar la ejecución de todo proceso crediticio que invoque un atributo de origen retail sin un registro de cruce autorizado asociado. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-05)); verbo único. No procede división. | — | Gobernanza de Datos | RN-05, RN-02 |  |  | RF-032.3 |
| RF-173 | RF | El sistema deberá asignar a la misma persona un identificador distinto en el ámbito retail y en el ámbito fiscalizado. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-04)); verbo único. No procede división. | — | Gobernanza de Datos | RN-04 |  |  | RF-050 |
| RF-174 | RF | El sistema deberá resolver la correspondencia entre identificadores exclusivamente a través de una tabla de correspondencia custodiada, con acceso nominado y registrado. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-04)); verbo único. No procede división. | — | Gobernanza de Datos | RN-04, RN-02 |  |  | RF-051 |
| RF-175 | RF | El sistema deberá rechazar la persistencia de la clave del ámbito financiero como columna o atributo en cualquier entidad del ámbito retail. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-04)); verbo único. No procede división. | — | Gobernanza de Datos | RN-04, RN-01 |  |  | RF-052 |
| RF-176 | RF | El sistema deberá exigir el registro de la evaluación de impacto sobre la frontera de datos antes de habilitar el estado 'aprobada' de una iniciativa. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-06)); verbo único. No procede división. | — | Gobernanza de Datos | RN-06 |  |  | RF-053 |
| RF-177 | RF | El sistema debe permitir declarar previamente el orden de degradación de los servicios. | «Declarar y parametrizar» son dos operaciones sobre objetos distintos: el orden y los criterios de activación. | RF-026.1 | Evento de Alta Concurrencia | RN-57, RN-11 |  |  | RF-026.1a |
| RF-178 | RF | El sistema debe permitir parametrizar los criterios que activan cada nivel de degradación declarado. | Segunda operación del requerimiento original. | RF-026.1 | Evento de Alta Concurrencia | RN-57, RN-11 |  |  | RF-026.1b |
| RF-179 | RF | El sistema deberá suspender la publicación de la categoría indicada por el orden de degradación declarado. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-026); se verifica el verbo único y se mantiene. | — | Evento de Alta Concurrencia | RN-57, RN-11 |  |  | RF-026.2 |
| RF-180 | RF | El sistema deberá reducir el límite de unidades por cliente al valor declarado. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-026); se verifica el verbo único y se mantiene. | — | Evento de Alta Concurrencia | RN-57 |  |  | RF-026.3 |
| RF-181 | RF | El sistema deberá desactivar temporalmente los medios de pago de mayor fricción operativa declarados. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-026); se verifica el verbo único y se mantiene. | — | Evento de Alta Concurrencia | RN-57 |  |  | RF-026.4 |
| RF-182 | RF | El sistema deberá monitorear en tiempo real la tasa de cancelación por falta de existencia por categoría. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-027); se verifica el verbo único y se mantiene. | — | Evento de Alta Concurrencia | RN-57, RN-09 |  |  | RF-027.1 |
| RF-183 | RF | El sistema deberá activar la acción de degradación declarada para esa categoría en RF-026.1. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-027); se verifica el verbo único y se mantiene. | — | Evento de Alta Concurrencia | RN-57, RN-11 |  |  | RF-027.2 |
| RF-184 | RF | El sistema deberá permitir parametrizar las cinco ventanas de congelamiento (1 nov - 6 ene; evento anual y su semana previa; evento de noviembre; semana del Día de la Madre; última semana de enero a primera de marzo). | Atómico. División ya aplicada en la versión anterior (Dividido de RF-028); se verifica el verbo único y se mantiene. | — | Evento de Alta Concurrencia | RN-55 |  |  | RF-028.1 |
| RF-185 | RF | El sistema deberá impedir la ejecución del despliegue o intervención en producción durante la ventana de congelamiento. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-028); se verifica el verbo único y se mantiene. | — | Evento de Alta Concurrencia | RN-55 |  |  | RF-028.2 |
| RF-186 | RF | El sistema deberá registrar el intento de despliegue bloqueado, indicando componente, solicitante e instante. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-55)); verbo único. No procede división. | — | Evento de Alta Concurrencia | RN-55 |  |  | RF-028.3 |
| RF-187 | RF | El sistema debe permitir al ejecutivo de mesón atender íntegramente el caso de garantía legal en la tienda. | Unía la capacidad de atender con la prohibición de derivar. La prohibición requiere su propio caso de prueba negativo. | RF-019 | Devoluciones y Garantía Legal | RN-26 |  |  | RF-019a |
| RF-188 | RF | El sistema debe impedir que el flujo de atención exija la derivación del consumidor al fabricante, al servicio técnico o al vendedor de marketplace como condición para ser atendido. | Control negativo exigido por la Ley N° 19.496 y por la restricción no negociable N°7. | RF-019 | Devoluciones y Garantía Legal | RN-26 |  |  | RF-019b |
| RF-189 | RF | El sistema deberá permitir al ejecutivo registrar el motivo de la devolución (talla, color, expectativa, falla). | Atómico tras la reformulación de la versión anterior; verbo único verificado. No procede nueva división. | — | Devoluciones y Garantía Legal | RN-14 |  |  | RF-020 |
| RF-190 | RF | El sistema deberá impedir el reingreso de una unidad devuelta al inventario disponible mientras no exista una decisión de aptitud registrada. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-14)); verbo único. No procede división. | — | Devoluciones y Garantía Legal | RN-14 |  |  | RF-055 |
| RF-191 | RF | El sistema deberá permitir al ejecutivo registrar la decisión de aptitud de la unidad devuelta, identificando al responsable de la decisión y su instante. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-14)); verbo único. No procede división. | — | Devoluciones y Garantía Legal | RN-14 |  |  | RF-056 |
| RF-192 | RF | El sistema deberá presentar al ejecutivo las tres opciones de garantía legal (reparación, reposición y devolución del precio) para que el consumidor elija. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-29)); verbo único. No procede división. | — | Devoluciones y Garantía Legal | RN-29 |  |  | RF-087 |
| RF-193 | RF | El sistema debe registrar la opción de garantía legal ofrecida al consumidor. | Lo ofrecido y lo elegido son dos hechos distintos; su divergencia es precisamente la evidencia que exige la fiscalización. | RF-088 | Devoluciones y Garantía Legal | RN-29 |  |  | RF-088a |
| RF-194 | RF | El sistema debe registrar la opción de garantía legal efectivamente elegida por el consumidor. | Segundo hecho del requerimiento original. | RF-088 | Devoluciones y Garantía Legal | RN-29 |  |  | RF-088b |
| RF-195 | RF | El sistema deberá permitir parametrizar el plazo de garantía legal por tipo de producto, sin requerir modificacion de código. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-29)); verbo único. No procede división. | — | Devoluciones y Garantía Legal | RN-29 |  |  | RF-089 |
| RF-196 | RF | El sistema deberá registrar el hito de resolución al consumidor con su fecha propia. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-27)); verbo único. No procede división. | — | Devoluciones y Garantía Legal | RN-27 |  |  | RF-090 |
| RF-197 | RF | El sistema deberá registrar el hito de recuperación contra el tercero responsable con una fecha independiente de la resolución al consumidor. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-27)); verbo único. No procede división. | — | Devoluciones y Garantía Legal | RN-27 |  |  | RF-091 |
| RF-198 | RF | El sistema deberá impedir que el estado de la recuperación contra el tercero condicione el cierre de la resolución al consumidor. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-27)); verbo único. No procede división. | — | Devoluciones y Garantía Legal | RN-27, RN-26 |  |  | RF-092 |
| RF-199 | RF | El sistema deberá exigir la entrega completa de la información precontractual antes de habilitar la evaluación de la solicitud de crédito. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Crédito y Cobranza | RN-34 |  |  | RF-021 |
| RF-200 | RF | El sistema deberá registrar la versión del documento precontractual entregado. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-022A); se verifica el verbo único y se mantiene. | — | Crédito y Cobranza | RN-35 |  |  | RF-022.1 |
| RF-201 | RF | El sistema deberá registrar el instante de entrega de la información precontractual. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-022A); se verifica el verbo único y se mantiene. | — | Crédito y Cobranza | RN-35 |  |  | RF-022.2 |
| RF-202 | RF | El sistema deberá registrar el instante de aceptación del cliente. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-022A); se verifica el verbo único y se mantiene. | — | Crédito y Cobranza | RN-35 |  |  | RF-022.3 |
| RF-203 | RF | El sistema deberá registrar el medio por el cual se entrego y se aceptó la información precontractual. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-35)); verbo único. No procede división. | — | Crédito y Cobranza | RN-35, RN-44 (propuesta) |  |  | RF-022.4 |
| RF-204 | RF | El sistema deberá registrar el contenido exacto aceptado por el cliente o su huella de integridad verificable. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-35)); verbo único. No procede división. | — | Crédito y Cobranza | RN-35, RN-41 |  |  | RF-022.5 |
| RF-205 | RF | El sistema deberá dejar constancia expresa de que el cliente recibió la información antes de aceptar, mediante un mecanismo distinto de la sola firma en papel archivado. | Atómico. Renumerado desde RF-022B en la versión anterior; verbo único verificado. | — | Crédito y Cobranza | RN-34, RN-35 |  |  | RF-022.6 |
| RF-206 | RF | El sistema deberá impedir el registro de la aceptación del crédito mientras no exista acreditación de entrega previa de la información precontractual completa. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-34)); verbo único. No procede división. | — | Crédito y Cobranza | RN-34 |  |  | RF-022.7 |
| RF-207 | RF | El sistema deberá registrar la evidencia del consentimiento expreso e informado del cliente mediante un mecanismo verificable de integridad. | Atómico. División ya aplicada en la versión anterior (Dividido de RF-023); se verifica el verbo único y se mantiene. | — | Crédito y Cobranza | RN-40, RN-41 |  |  | RF-023.1 |
| RF-208 | RF | El sistema deberá impedir el registro de una modificacion de condiciones del crédito que no tenga evidencia de consentimiento asociada. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-40)); verbo único. No procede división. | — | Crédito y Cobranza | RN-40 |  |  | RF-023.2 |
| RF-209 | RF | El sistema deberá reconstruir el acto de consentimiento presentando que se informó, en que versión y que aceptó el cliente. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-41)); verbo único. No procede división. | — | Crédito y Cobranza | RN-41, RN-35 |  |  | RF-023.3 |
| RF-210 | RF | El sistema deberá restaurar desde archivo frío los antecedentes de una operación de crédito de cualquier cohorte dentro del plazo de conservación. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-36)); verbo único. No procede división. | — | Crédito y Cobranza | RN-36 |  |  | RF-023.4 |
| RF-211 | RF | El sistema debe permitir al ejecutivo de cobranza iniciar una gestión de cobranza. | Unía tres comportamientos: iniciar, registrar y restringir. Un fallo del control normativo oscurecía el éxito del registro. | RF-024A | Crédito y Cobranza | RN-40 |  |  | RF-024Aa |
| RF-212 | RF | El sistema debe registrar la gestión de cobranza ejecutada con su medio, su instante y su ejecutor. | El registro es la evidencia exigida por la normativa de cobranza extrajudicial y se prueba por separado. | RF-024A | Crédito y Cobranza | RN-40 |  |  | RF-024Ab |
| RF-213 | RF | El sistema debe impedir la ejecución de una gestión de cobranza fuera de los límites normativos de horario y de medio de contacto. | La restricción normativa es un control funcional con su propio caso Pasa/Falla. | RF-024A | Crédito y Cobranza | RN-40 |  |  | RF-024Ac |
| RF-214 | RF | El sistema debe enlazar el expediente de la repactación con la gestión de cobranza que la originó. | Dos enlaces hacia entidades distintas; cada uno puede existir sin el otro. | RF-024B | Crédito y Cobranza | RN-40, RN-41 |  |  | RF-024Ba |
| RF-215 | RF | El sistema debe enlazar el expediente de la repactación con la evidencia de consentimiento registrada en RF-207. | Segundo enlace del requerimiento original, exigido por RN-40. | RF-024B | Crédito y Cobranza | RN-40, RN-41 |  |  | RF-024Bb |
| RF-216 | RF | El sistema deberá generar un reporte de conciliación diaria de saldos durante todo el proceso de migración. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Crédito y Cobranza | RN-58 |  |  | RF-033 |
| RF-217 | RF | El sistema deberá permitir al cliente no autenticado consultar la información precontractual del crédito. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Crédito y Cobranza | RN-34 |  |  | RF-036B |
| RF-218 | RF | El sistema deberá permitir al cliente no autenticado utilizar un simulador de costo total del crédito. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Crédito y Cobranza | RN-34, RN-37 |  |  | RF-036C |
| RF-219 | RF | El sistema deberá mantener cargada la Tasa Máxima Convencional vigente por tipo y tramo de operación, con su fecha de vigencia. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-37)); verbo único. No procede división. | — | Crédito y Cobranza | RN-37 |  |  | RF-093 |
| RF-220 | RF | El sistema deberá impedir la originación de una operación cuya tasa supere la Tasa Máxima Convencional vigente a la fecha de la operación. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-37)); verbo único. No procede división. | — | Crédito y Cobranza | RN-37 |  |  | RF-094 |
| RF-221 | RF | El sistema deberá determinar el cupo exclusivamente a partir de las variables de la evaluación de capacidad de pago documentada. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-38)); verbo único. No procede división. | — | Crédito y Cobranza | RN-38 |  |  | RF-095 |
| RF-222 | RF | El sistema deberá excluir el monto de la venta en curso del conjunto de variables de asignación de cupo. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-38)); verbo único. No procede división. | — | Crédito y Cobranza | RN-38 |  |  | RF-096 |
| RF-223 | RF | El sistema deberá excluir la solicitud del vendedor del conjunto de variables de asignación de cupo. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-38)); verbo único. No procede división. | — | Crédito y Cobranza | RN-38, RN-39 |  |  | RF-097 |
| RF-224 | RF | El sistema deberá impedir al vendedor alterar el resultado de una evaluación crediticia. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-39)); verbo único. No procede división. | — | Crédito y Cobranza | RN-39 |  |  | RF-098 |
| RF-225 | RF | El sistema deberá impedir la repetición de la evaluación crediticia del mismo cliente dentro de la ventana de enfriamiento parametrizada. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-39)); verbo único. No procede división. | — | Crédito y Cobranza | RN-39 |  |  | RF-099 |
| RF-226 | RF | El sistema deberá registrar cada intento de evaluación con la identidad del solicitante y el resultado obtenido. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-39)); verbo único. No procede división. | — | Crédito y Cobranza | RN-39 |  |  | RF-100 |
| RNF-04 | RNF | El estado de un pedido no debe presentar discrepancias entre canales de consulta. | Atómico. División ya aplicada en la versión anterior (Dividido de RNF-04); se verifica el verbo único y se mantiene. | — | Consistencia de datos | RN-23, RN-28 | 0% de discrepancias en auditoría cruzada. | Prueba de sincronización cruzada entre canales tras cada cambio de estado. | NFR-01 |
| RNF-05 | RNF | La actualización del estado de un pedido debe reflejarse en todos los puntos de consulta dentro del plazo máximo definido. | Atómico. División ya aplicada en la versión anterior (Dividido de RNF-04); se verifica el verbo único y se mantiene. | — | Desempeño | RN-23, RN-28 | Desfase máximo entre cambio real de estado y su reflejo en cualquier canal: POR DEFINIR (propuesta: 30 s). | Medicion de latencia de propagación por canal. | NFR-01.2 |
| RNF-06 | RNF | El tiempo de evaluación de una solicitud de crédito en el punto de venta físico no debe exceder el umbral objetivo. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Desempeño | RN-34 | <= 8 segundos. | Prueba de tiempo de respuesta en punto de venta bajo carga representativa. | NFR-02 |
| RNF-07 | RNF | El tiempo total de originación de crédito en el mesón, con información precontractual acreditada, no debe superar el tiempo del proceso actual. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-34)); verbo único. No procede división. | — | Desempeño / Cumplimiento | RN-34 | <= 3 minutos (tiempo actual declarado en el caso). | Medicion de tiempo de originación extremo a extremo en mesón, con y sin acreditación. | NFR-21 |
| RNF-08 | RNF | La migración de la cartera de crédito viva no debe generar pérdida de datos. | Unía tres garantías independientes; una migración puede conservar los datos y aun así interrumpir el servicio. | NFR-03 | Portabilidad / Migración | RN-58 | 0 registros perdidos respecto del universo de 620.000 clientes con saldo. | Conteo y cuadratura de universos origen y destino en cada corte de migración. | NFR-03.1 |
| RNF-09 | RNF | La migración de la cartera de crédito viva no debe interrumpir el servicio de cobro. | Segunda garantía del requerimiento original. | NFR-03 | Portabilidad / Migración | RN-58 | 0 interrupciones del servicio de cobro durante la ventana de migración. | Monitoreo continuo de disponibilidad del servicio de cobro durante cada etapa de coexistencia. | NFR-03.2 |
| RNF-10 | RNF | La migración de la cartera de crédito viva no debe producir divergencia de saldos. | Tercera garantía; es la que gobierna el criterio de detención del avance. | NFR-03 | Portabilidad / Migración | RN-58 | 0 divergencias no conciliadas en la conciliación diaria; migración completa antes de 2029. | Conciliación diaria automatizada de saldos entre entorno origen y destino (RF-216). | NFR-03.3 |
| RNF-11 | RNF | La separación lógica entre los datos del retail y los del negocio financiero debe estar implementada. | «Implementada, documentada y verificada» son tres estados verificables por evidencias distintas y en momentos distintos. | NFR-04 | Seguridad / Arquitectura | RN-01, RN-06 | Separación lógica operativa en todos los componentes que tratan datos de ambos ámbitos. | Revisión de arquitectura desplegada y prueba de acceso denegado desde el ámbito retail. | NFR-04.1 |
| RNF-12 | RNF | La separación lógica entre ambos ámbitos debe estar documentada. | Segundo estado del requerimiento original; la documentación es la exigencia expresa del acta de directorio. | NFR-04 | Seguridad / Arquitectura | RN-01, RN-06 | Documento de separación vigente y versionado, aprobado por la Contraloría interna. | Revisión documental contra el diseño desplegado. | NFR-04.2 |
| RNF-13 | RNF | La separación lógica entre ambos ámbitos debe ser verificada por auditoría independiente. | Tercer estado; su resultado condiciona la construcción de cualquier vista unificada de cliente. | NFR-04 | Seguridad / Arquitectura | RN-01, RN-06 | Informe de auditoría aprobado con 0 hallazgos críticos abiertos, previo a cualquier vista unificada. | Auditoría independiente con informe formal y seguimiento de hallazgos. | NFR-04.3 |
| RNF-14 | RNF | La separación física entre la infraestructura del retail y la de la filial emisora debe estar implementada y acreditada. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-01)); verbo único. No procede división. | — | Seguridad / Arquitectura | RN-01 | Informe técnico de separación física acreditado; prueba de penetracion que demuestre que un componente del retail no alcanza datos de crédito. | Prueba de penetracion e inspeccion de infraestructura. | NFR-31 |
| RNF-15 | RNF | Toda acción relevante ejecutada en el sistema debe quedar registrada indicando usuario individual, acción e instante. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Auditabilidad | RN-50, RN-51, RN-52 | 100% de acciones relevantes con registro de auditoría. | Auditoría de logs sobre muestra de transacciones. | NFR-05 |
| RNF-16 | RNF | La consulta de disponibilidad en la ficha de producto del canal digital debe responder dentro del umbral definido. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-06); se verifica el verbo único y se mantiene. | — | Desempeño | RN-09 | <= 400 ms. | Prueba de tiempo de respuesta bajo carga representativa. | NFR-06.1 |
| RNF-17 | RNF | La confirmación de un pedido durante el evento anual debe completarse dentro del umbral definido. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-06); se verifica el verbo único y se mantiene. | — | Desempeño | RN-57 | <= 3 s. | Prueba de carga con volumetria del evento anual. | NFR-06.2 |
| RNF-18 | RNF | La venta completa en caja con medio de pago externo debe completarse dentro del umbral definido. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-06); se verifica el verbo único y se mantiene. | — | Desempeño | RN-46 | <= 25 s. | Prueba de tiempo de respuesta en linea de caja. | NFR-06.3 |
| RNF-19 | RNF | La propagación de un cambio de precio a las 380 líneas de caja y al canal digital debe completarse dentro del umbral definido. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-06); se verifica el verbo único y se mantiene. | — | Desempeño | RN-16, RN-18 | <= 5 minutos. | Medicion de latencia de propagación por destino. | NFR-06.4 |
| RNF-20 | RNF | El registro de una devolución en el mesón debe completarse dentro del umbral definido. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-06); se verifica el verbo único y se mantiene. | — | Desempeño | RN-14, RN-26 | <= 60 s. | Prueba de tiempo de respuesta en mesón de atención. | NFR-06.5 |
| RNF-21 | RNF | La consulta de disponibilidad desde una terminal compartida del piso de venta debe responder dentro del umbral definido. | Atómico. Reclasificado desde RF-101 en la versión anterior; verbo único verificado. | — | Desempeño | RN-09, RN-45 (propuesta) | <= 2 s. | Prueba de tiempo de respuesta en terminal de sala. | NFR-06.6 |
| RNF-22 | RNF | La plataforma debe soportar la concurrencia y el volumen del peak digital del evento anual sin degradar los umbrales de NFR-06.x. | El caso describe dos peaks de naturaleza distinta —digital de tres días y presencial de dos meses—; dimensionar para uno no resuelve el otro y no comparten caso de prueba. | NFR-07 | Desempeño / Capacidad | RN-57 | Perfil declarado por el PROPONENTE sobre 104.000 pedidos en 3 días (proyección 150.000), equivalente a 22 días de venta en línea. | Prueba de carga con perfil del evento anual al 120 % del peak proyectado. | NFR-07.1 |
| RNF-23 | RNF | La plataforma debe soportar la concurrencia y el volumen del peak presencial de la campaña de noviembre y diciembre sin degradar los umbrales de NFR-06.x. | Segundo peak del requerimiento original, sostenido sobre 380 líneas de caja y el mesón financiero. | NFR-07 | Desempeño / Capacidad | RN-57 | Perfil declarado por el PROPONENTE sobre 380 líneas de caja (430 proyectadas) en peak de sábado de diciembre. | Prueba de carga con perfil presencial sostenido, independiente de la prueba del peak digital. | NFR-07.2 |
| RNF-24 | RNF | Una tienda debe poder operar sin enlace externo durante el período mínimo definido. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-08); se verifica el verbo único y se mantiene. | — | Disponibilidad | RN-46 | >= 8 horas continuas. | Prueba de desconexion controlada en tienda. | NFR-08.1 |
| RNF-25 | RNF | El centro de distribución principal debe poder operar sin enlace externo durante el período mínimo definido. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-08); se verifica el verbo único y se mantiene. | — | Disponibilidad | RN-46 | >= 4 horas continuas. | Prueba de desconexion controlada en CD. | NFR-08.2 |
| RNF-26 | RNF | La sincronización tras la reconexión no debe superar el plazo definido. | Unía un umbral de tiempo con una garantía de integridad: una sincronización puede ser rápida y perder documentos. | NFR-08.3 | Disponibilidad | RN-48 | <= 30 minutos tras 8 horas de desconexión. | Prueba de reconexión cronometrada tras desconexión programada de 8 horas. | NFR-08.3a |
| RNF-27 | RNF | La sincronización tras la reconexión no debe producir pérdida de ventas ni de documentos. | Segunda garantía del requerimiento original, con evidencia distinta. | NFR-08.3 | Disponibilidad | RN-48 | 0 ventas y 0 documentos perdidos o duplicados. | Cuadratura del universo de transacciones de la ventana desconectada contra el sistema central. | NFR-08.3b |
| RNF-28 | RNF | La operación desconectada autónoma on-premise debe sostenerse durante el período mínimo exigido por las bases técnicas. | Atómico. Requerimiento derivado de regla de negocio (NUEVO); verbo único. No procede división. | — | Disponibilidad | RN-46 | >= 24 horas (bases técnicas transversales), superior al mínimo de 8 h de RN-46. | Prueba de desconexion extendida. | NFR-08.4 |
| RNF-29 | RNF | La operación de tiendas y centros de distribución debe estar disponible en la ventana horaria definida. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-09); se verifica el verbo único y se mantiene. | — | Disponibilidad | RN-46 | 09:00 a 23:00, todos los dias del ano. | Monitoreo continuo de disponibilidad por servicio. | NFR-09.1 |
| RNF-30 | RNF | El canal digital debe estar disponible de forma continua. | Unía dos ámbitos con regímenes de exigencia distintos: el canal digital (retail) y los servicios de la filial fiscalizada. | NFR-09.2 | Disponibilidad | RN-46, RN-58 | 24x7x365; disponibilidad >= 99,5 % (supuesto fundamentado, equivalente a Tier 2). | Medición mensual de disponibilidad contra el nivel de servicio comprometido. | NFR-09.2a |
| RNF-31 | RNF | Los servicios financieros que afectan pagos, estados de cuenta y bloqueo de tarjetas deben estar disponibles de forma continua. | Segundo ámbito; su indisponibilidad tiene consecuencias regulatorias y no solo comerciales. | NFR-09.2 | Disponibilidad | RN-46, RN-58 | 24x7x365; disponibilidad >= 99,5 % (supuesto fundamentado). | Medición mensual segregada por ámbito, informada a la filial emisora. | NFR-09.2b |
| RNF-32 | RNF | La solución debe cumplir los objetivos de recuperación ante desastre exigidos. | Atómico. Requerimiento derivado de regla de negocio (NUEVO); verbo único. No procede división. | — | Recuperabilidad | RN-48, RN-58 | RTO <= 4 h; RPO <= 15 min. | Ensayo de recuperación ante desastre con medicion de RTO y RPO efectivos. | NFR-09.3 |
| RNF-33 | RNF | Los datos de identificación de clientes, la cartera de crédito, el comportamiento de pago y los antecedentes de evaluación crediticia deben cifrarse a nivel de campo. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-10); se verifica el verbo único y se mantiene. | — | Seguridad | RN-01, RN-03 | 100% de campos sensibles cifrados. | Auditoría de esquema de datos y prueba de exfiltracion controlada. | NFR-10.1 |
| RNF-34 | RNF | Los datos de medios de pago no deben almacenarse en claro, sino tokenizarse. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-10); se verifica el verbo único y se mantiene. | — | Seguridad | RN-01 | 0% de datos de medios de pago almacenados sin tokenizar. | Auditoría de esquema y prueba de exfiltracion controlada. | NFR-10.2 |
| RNF-35 | RNF | La red de cajas, la administrativa, la de videovigilancia y la inalámbrica de clientes deben estar segmentadas en las 22 tiendas. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-11); se verifica el verbo único y se mantiene. | — | Seguridad | RN-01 | 22/22 tiendas con segmentacion verificada (hoy 9). | Auditoría de configuracion de red por tienda. | NFR-11.1 |
| RNF-36 | RNF | La red y el ámbito de sistemas de la filial emisora deben estar separados de forma acreditada respecto del retail. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-11); se verifica el verbo único y se mantiene. | — | Seguridad | RN-01 | Separación acreditada mediante informe técnico. | Auditoría de arquitectura de red. | NFR-11.2 |
| RNF-37 | RNF | Debe existir segregación de funciones verificable entre originación, aprobación, modificacion de condiciones y cobranza. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Seguridad | RN-39, RN-53 | 0 usuarios con permisos combinados de originación+aprobación o de modificacion+cobranza sobre un mismo caso. | Auditoría de matriz de roles y permisos. | NFR-12 |
| RNF-38 | RNF | Debe registrarse todo acceso a la cartera de crédito, al comportamiento de pago y a los antecedentes de evaluación crediticia. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Auditabilidad | RN-02, RN-03 | 100% de accesos a información sensible con registro (usuario, dato, finalidad, instante). | Auditoría de logs de acceso sobre muestra representativa. | NFR-13 |
| RNF-39 | RNF | Los actos de crédito de apertura de tarjeta y de repactación deben contar con un mecanismo de consentimiento de integridad verificable. | Unía actos del ámbito fiscalizado con actos del ámbito retail, sujetos a normativa y a plazos de conservación distintos. | NFR-14 | Seguridad / Cumplimiento | RN-35, RN-40, RN-41, RN-44 (propuesta) | 100 % de aperturas y repactaciones con evidencia de integridad verificable, en la modalidad que la normativa admita para cada canal. | Auditoría censal del período y verificación de la huella de integridad por muestreo. | NFR-14.1 |
| RNF-40 | RNF | La conformidad de recepción de mercadería y la constancia de devolución deben contar con un mecanismo de consentimiento de integridad verificable. | Segundo grupo de actos, del ámbito retail (RT-16.14). | NFR-14 | Seguridad / Cumplimiento | RN-35, RN-40, RN-41, RN-44 (propuesta) | 100 % de conformidades y constancias con evidencia de integridad verificable. | Verificación de la validez de la firma y de la integridad del documento por muestreo. | NFR-14.2 |
| RNF-41 | RNF | Los documentos tributarios y antecedentes de venta deben conservarse por el plazo definido. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-15); se verifica el verbo único y se mantiene. | — | Cumplimiento | RN-49 | 6 años. | Auditoría de politicas de retencion por tipo de dato. | NFR-15.1 |
| RNF-42 | RNF | Los antecedentes del crédito deben conservarse por el plazo del crédito más el período posterior exigido. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-15); se verifica el verbo único y se mantiene. | — | Cumplimiento | RN-36 | Plazo del crédito + 6 años (sustituye la practica actual de 90 dias para grabaciones). | Auditoría de retencion y prueba de restauración desde archivo frío. | NFR-15.2 |
| RNF-43 | RNF | La evidencia de consentimiento de originación y repactación debe conservarse por el mismo plazo que el crédito. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-15); se verifica el verbo único y se mantiene. | — | Cumplimiento | RN-35, RN-36, RN-40 | Plazo del crédito + 6 años; recuperable a 10 años según RN-35. | Auditoría de retencion y prueba de recuperación. | NFR-15.3 |
| RNF-44 | RNF | La trazabilidad del precio publicado debe conservarse por el plazo definido. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-15); se verifica el verbo único y se mantiene. | — | Cumplimiento | RN-17 | 3 años. | Auditoría de retencion. | NFR-15.4 |
| RNF-45 | RNF | Los movimientos de inventario y conteos cíclicos deben conservarse por el plazo definido. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-15); se verifica el verbo único y se mantiene. | — | Cumplimiento | RN-13 | 6 años. | Auditoría de retencion. | NFR-15.5 |
| RNF-46 | RNF | Los datos de fidelización deben conservarse por el plazo definido. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-15); se verifica el verbo único y se mantiene. | — | Cumplimiento | RN-03 | Duracion de la relacion + 2 años. | Auditoría de retencion. | NFR-15.6 |
| RNF-47 | RNF | Los registros de videovigilancia deben conservarse por el plazo definido. | Atómico. División ya aplicada en la versión anterior (Dividido de NFR-15); se verifica el verbo único y se mantiene. | — | Cumplimiento | RN-01 | 30 dias. | Auditoría de retencion. | NFR-15.7 |
| RNF-48 | RNF | La solución debe admitir la apertura de una tienda nueva por parametrización, sin desarrollo a medida. | Atómico tras la reformulación de la versión anterior; verbo único verificado. No procede nueva división. | — | Portabilidad / Escalabilidad | - | Alta de tienda por configuracion en <= 10 dias habiles (supuesto fundamentado, compatible con una apertura comercial). | Prueba de aprovisionamiento de una tienda simulada. | NFR-16 |
| RNF-49 | RNF | Las interfaces de sala, caja y mesón financiero deben ser operables por personal recién incorporado con capacitación mínima. | Atómico tras la reformulación de la versión anterior; verbo único verificado. No procede nueva división. | — | Usabilidad | RN-50, RN-53 | Tiempo de capacitación operativa basica <= 4 horas (supuesto fundamentado), medido con personal de temporada. | Prueba de usabilidad con personal recién incorporado en condiciones reales. | NFR-17 |
| RNF-50 | RNF | Toda comunicación relativa al crédito debe cumplir criterios verificables de lenguaje claro, validados con personas usuarias reales. | Atómico. Un solo verbo de acción y un único caso de prueba Pasa/Falla; no procede división. | — | Usabilidad / Cumplimiento | RN-34, RN-41 | 100% de plantillas validadas con pruebas de comprension lectora con usuarios reales. | Prueba de comprension lectora sobre muestra de plantillas. | NFR-18 |
| RNF-51 | RNF | Las notificaciones definidas funcionalmente deben emitirse y registrarse en el 100% de los eventos que las gatillan. | Atómico tras la reformulación de la versión anterior; verbo único verificado. No procede nueva división. | — | Operabilidad | RN-23, RN-28, RN-11 | 100% de eventos definidos con notificacion generada y registrada. | Prueba de disparo de eventos y verificacion del registro. | NFR-19 |
| RNF-52 | RNF | La solución debe adoptar un estándar identificado y justificado para el catálogo e identificación de producto. | El enunciado unía cinco dominios de interoperabilidad con contrapartes distintas; cada uno se acredita por separado. | NFR-20 | Interoperabilidad | RN-49, RN-32 | Estándar identificado por su denominación y justificado en la Oferta Técnica. | Prueba de interoperabilidad con al menos una contraparte real del dominio. | NFR-20.1 |
| RNF-53 | RNF | La solución debe adoptar un estándar identificado y justificado para el intercambio de órdenes y avisos de despacho con los proveedores. | Segundo dominio del requerimiento original (940 proveedores). | NFR-20 | Interoperabilidad | RN-49, RN-32 | Estándar identificado y justificado; 100 % de las interfaces con proveedores mapeadas a él. | Prueba de intercambio con un proveedor piloto. | NFR-20.2 |
| RNF-54 | RNF | La solución debe adoptar un estándar identificado y justificado para el intercambio con los transportistas de última milla. | Tercer dominio del requerimiento original. | NFR-20 | Interoperabilidad | RN-49, RN-32 | Estándar identificado y justificado; trazabilidad del estado del pedido hasta la entrega. | Prueba de integración con un transportista piloto. | NFR-20.3 |
| RNF-55 | RNF | La solución debe adoptar un estándar identificado y justificado para la sincronización de catálogo, existencia y pedido con los vendedores de marketplace. | Cuarto dominio del requerimiento original (310 vendedores). | NFR-20 | Interoperabilidad | RN-49, RN-32 | Estándar identificado y justificado; 100 % de vendedores sincronizados por él. | Prueba de sincronización con un vendedor piloto. | NFR-20.4 |
| RNF-56 | RNF | La solución debe adoptar el formato normativo vigente de documento tributario electrónico. | Quinto dominio; su cumplimiento lo acredita el sistema de gestión empresarial como único emisor. | NFR-20 | Interoperabilidad | RN-49, RN-32 | 100 % de los documentos emitidos conforme al formato vigente de la autoridad tributaria. | Validación de esquema sobre una muestra de documentos emitidos. | NFR-20.5 |
| RNF-57 | RNF | La evidencia completa de consentimiento de una operación arbitraria debe recuperarse dentro del plazo objetivo, a diez años. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-35)); verbo único. No procede división. | — | Auditabilidad / Desempeño | RN-35, RN-41 | Recuperación <= 5 minutos (supuesto fundamentado) sobre operaciones de hasta 10 años de antiguedad. | Simulacro de requerimiento de la autoridad fiscalizadora. | NFR-22 |
| RNF-58 | RNF | La recuperación del precio publicado de una referencia en una fecha, hora y canal arbitrarios debe completarse dentro del plazo objetivo. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-17)); verbo único. No procede división. | — | Desempeño | RN-17 | <= 1 minuto, sobre una ventana de 3 años. | Consulta de auditoría sobre fecha/hora/canal aleatorios. | NFR-23 |
| RNF-59 | RNF | La revocación total de accesos de un trabajador debe completarse dentro del plazo máximo de la política interna. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-52)); verbo único. No procede división. | — | Seguridad | RN-52 | <= 4 horas desde el término efectivo del vínculo (supuesto fundamentado). | Auditoría de accesos vigentes contra nómina activa. | NFR-24 |
| RNF-60 | RNF | El traspaso de sesión nominativa en una terminal compartida debe completarse dentro del plazo objetivo. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-50)); verbo único. No procede división. | — | Usabilidad / Desempeño | RN-50 | <= 5 segundos (supuesto fundamentado). | Medicion de tiempo de traspaso en terminal de sala. | NFR-25 |
| RNF-61 | RNF | La tasa de cancelación de pedidos por falta de existencia no debe superar el umbral comprometido. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-09)); verbo único. No procede división. | — | Efectividad de negocio | RN-09, RN-57 | < 0,3% anual. | Medicion anual sobre el total de pedidos aceptados. | NFR-26 |
| RNF-62 | RNF | El cumplimiento de la promesa de entrega publicada debe alcanzar el umbral comprometido, medido por pedido. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-24)); verbo único. No procede división. | — | Efectividad de negocio | RN-24 | >= 97% (linea base 81%), medido por pedido y no por promedio de canal. | Medicion por pedido sobre el período. | NFR-27 |
| RNF-63 | RNF | La diferencia de inventario por categoría debe reducirse al umbral comprometido. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-13)); verbo único. No procede división. | — | Efectividad de negocio | RN-13, RN-09 | < 2% (linea base 12,4%). | Medicion sobre resultados de conteo cíclico por categoría. | NFR-28 |
| RNF-64 | RNF | El tiempo entre la detección de un quiebre y el aviso al cliente no debe superar el objetivo declarado. | Unía un umbral de latencia con una garantía de negocio que se verifica de otra forma. | NFR-29 | Operabilidad | RN-23 | <= 30 minutos (supuesto fundamentado). | Medición de la latencia entre el evento de quiebre y el envío de la notificación. | NFR-29a |
| RNF-65 | RNF | No debe mantenerse un cobro capturado sobre un pedido declarado no cumplible. | Segunda garantía del requerimiento original; es el criterio de aceptación N°3 del caso. | NFR-29 | Operabilidad | RN-23 | 0 casos de cobro sostenido sobre pedido no cumplible. | Auditoría de conciliación diaria de preautorizaciones y capturas (RF-050). | NFR-29b |
| RNF-66 | RNF | La latencia entre la recepción física de una devolución en tienda y la notificación al vendedor de marketplace no debe superar el objetivo declarado. | Unía un umbral de latencia con un resultado de negocio verificable por otro medio. | NFR-30 | Operabilidad | RN-28 | <= 15 minutos (supuesto fundamentado). | Medición de la latencia entre el registro de recepción y el envío de la notificación. | NFR-30a |
| RNF-67 | RNF | No debe permanecer mercadería de marketplace en bodega sin aviso a su propietario. | Segunda garantía del requerimiento original; responde directamente al levantamiento de la vendedora externa. | NFR-30 | Operabilidad | RN-28 | 0 unidades en bodega sin notificación asociada al cierre de cada día. | Conciliación diaria entre recepciones registradas y notificaciones emitidas. | NFR-30b |
| RNF-68 | RNF | La restauración desde archivo frío de una operación de crédito de la cohorte más antigua debe completarse dentro del plazo objetivo. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-36)); verbo único. No procede división. | — | Recuperabilidad | RN-36 | <= 24 horas (supuesto fundamentado). | Prueba de restauración desde archivo frío. | NFR-32 |
| RNF-69 | RNF | La atención de garantía legal en mesón no debe derivar al consumidor a un tercero como condición de atención, en ninguna tienda. | Atómico. Requerimiento derivado de regla de negocio (NUEVO (deriva de RN-26)); verbo único. No procede división. | — | Cumplimiento | RN-26 | 0 derivaciones como condición de atención, medido con cliente oculto en las 22 tiendas. | Programa de cliente oculto en las 22 tiendas. | NFR-33 |
| RNF-70 | RNF | El ciclo de desarrollo debe producir un inventario de componentes (SBOM) por artefacto desplegado. | Unía cuatro exigencias de seguridad independientes, con evidencias y momentos de verificación distintos. | NFR-34 | Seguridad / DevSecOps | RN-01, RN-06 | SBOM del 100 % de los artefactos desplegados. | Verificación del SBOM en cada liberación. | NFR-34.1 |
| RNF-71 | RNF | La cadena de suministro de software debe alcanzar el nivel SLSA 3 o superior. | Segunda exigencia del requerimiento original. | NFR-34 | Seguridad / DevSecOps | RN-01, RN-06 | Nivel SLSA 3 o superior acreditado. | Atestación de la cadena de construcción por artefacto. | NFR-34.2 |
| RNF-72 | RNF | La capa expuesta debe cumplir el estándar OWASP ASVS en el nivel comprometido. | Tercera exigencia del requerimiento original. | NFR-34 | Seguridad / DevSecOps | RN-01, RN-06 | 0 hallazgos críticos abiertos en el nivel ASVS comprometido. | Análisis estático y dinámico por ciclo y prueba de seguridad ofensiva. | NFR-34.3 |
| RNF-73 | RNF | La arquitectura debe implementar un modelo Zero Trust conforme a NIST SP 800-207. | Cuarta exigencia; es un principio de arquitectura y no una práctica del ciclo de desarrollo. | NFR-34 | Seguridad / DevSecOps | RN-01, RN-06 | Verificación explícita en cada solicitud y denegación por omisión en el 100 % de los puntos de control. | Revisión de arquitectura contra los principios de NIST SP 800-207. | NFR-34.4 |
| RNF-74 | RNF | Todo tratamiento de datos personales debe declarar su finalidad. | Unía tres obligaciones distintas de la Ley N° 21.719, acreditables por evidencias separadas. | NFR-35 | Cumplimiento | RN-02, RN-03, RN-05 | 100 % de los flujos con finalidad declarada. | Revisión del registro de actividades de tratamiento. | NFR-35.1 |
| RNF-75 | RNF | Todo tratamiento de datos personales debe invocar una de las bases de licitud de la Ley N° 21.719. | Segunda obligación del requerimiento original; el consentimiento no puede ser la base por defecto. | NFR-35 | Cumplimiento | RN-02, RN-03, RN-05 | 100 % de los flujos con base de licitud declarada; 0 tratamientos con consentimiento presunto. | Auditoría de conformidad por el oficial de cumplimiento. | NFR-35.2 |
| RNF-76 | RNF | La compañía debe mantener el registro de actividades de tratamiento de datos personales. | Tercera obligación del requerimiento original. | NFR-35 | Cumplimiento | RN-02, RN-03, RN-05 | Registro completo y vigente, actualizado ante cada cambio de flujo. | Revisión documental periódica contra el inventario de interfaces de RF-168. | NFR-35.3 |

## 2_Divisiones

<!-- hoja: 2_Divisiones | filas de datos: 42 -->

| ID de origen | Tipo original | Enunciado original (v2.1) | Regla(s) de atomicidad aplicada(s) | IDs resultantes | N° resultantes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| RF-044.2 | RF | El sistema deberá impedir el acceso anónimo o con credencial compartida. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RF-003, RF-004 | 2 |
| RF-119 | RF | El sistema deberá conciliar los accesos vigentes contra la nómina activa e informar los accesos huérfanos detectados. | Regla 1 (conjunción); Regla 2 (verbo único) | RF-014, RF-015 | 2 |
| RF-034 | RF | El PROPONENTE deberá especificar y costear la alternativa de etiquetas electrónicas frente a las demás opciones, sin asumir su adquisición como parte del alcance. | Regla 2 (verbo único); Regla 5 (separación RF/RNF); hallazgo H-11 | OP-01, OP-02 | 2 |
| RF-042.2 | RF | El sistema deberá generar una alerta operativa al jefe de tienda identificando la etiqueta no confirmada, antes de la apertura de sala. | Regla 5 (separación RF/RNF) | RF-027, RNF-01 | 2 |
| RF-043 | RF | El PROPONENTE deberá especificar la cobertura de despliegue, el hardware requerido y su costo, separadamente del resto de la solución. | Regla 1 (conjunción); hallazgo H-11 | OP-03, OP-04, OP-05 | 3 |
| RF-010.5 | RF | El sistema deberá liberar automáticamente la reserva y devolver la unidad al disponible para vender. | Regla 1 (conjunción); Regla 2 (verbo único) | RF-039, RF-040 | 2 |
| RF-014 | RF | El sistema deberá calcular la base de comisión reconociendo al vendedor y a la tienda de origen, validando previamente contra el movimiento de inventario real. | Regla 1 (conjunción); Regla 2 (verbo único); Regla 3 (testabilidad aislada) | RF-054, RF-055 | 2 |
| RF-035 | RF | El sistema deberá monitorear el tiempo restante de cada pedido respecto de su fecha prometida y priorizar su preparacion al acercarse al límite. | Regla 1 (conjunción); Regla 2 (verbo único) | RF-062, RF-063 | 2 |
| RF-036A | RF | El sistema deberá permitir al cliente no autenticado consultar el precio vigente y la disponibilidad por tienda y para despacho. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RF-064, RF-065, RF-066 | 3 |
| RF-037 | RF | El sistema deberá permitir al cliente autenticado consultar sus compras, devoluciones, estado de cuenta y documentos. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RF-067, RF-068, RF-069, RF-070 | 4 |
| RF-049 | RF | El sistema deberá permitir al ejecutivo de mesón consultar el estado real del pedido y el precio aplicado, y ofrecer las opciones de resolución definidas en RF-059, RF-060 y RF-061. | Regla 1 (conjunción); Regla 2 (verbo único) | RF-072, RF-073, RF-074 | 3 |
| RF-110 | RF | El sistema deberá reconciliar hacia los sistemas centrales la totalidad de las ventas y documentos registrados en modo desconectado. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RF-095, RF-096 | 2 |
| RF-120 | RF | El PROPONENTE deberá especificar la cantidad de dispositivos móviles que se requerirían por tienda y por departamento. | Hallazgo H-11 | OP-06 | 1 |
| RF-121 | RF | El PROPONENTE deberá especificar las características técnicas de los dispositivos móviles requeridos. | Hallazgo H-11 | OP-07 | 1 |
| RF-122 | RF | El PROPONENTE deberá presentar el análisis de hacer o comprar con las tres alternativas (incorporar al sistema existente, solución propia, mantener planillas) y su impacto sobre RN-15. | Regla 1 (conjunción); hallazgo H-11 | OP-08, OP-09 | 2 |
| RF-016A.1 | RF | El sistema deberá permitir al vendedor de marketplace declarar y actualizar la existencia de sus referencias en cualquier momento. | Regla 1 (conjunción); Regla 5 (separación RF/RNF) | RF-102, RF-103, RNF-02 | 3 |
| RF-038 | RF | El sistema deberá permitir al vendedor de marketplace consultar el estado de cada pedido intermediado, sus devoluciones y su evaluación de desempeño. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RF-110, RF-111, RF-112 | 3 |
| RF-048.1 | RF | El sistema deberá identificar visiblemente en el catálogo, la ficha de producto y el proceso de compra quien vende y quien despacha la unidad. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RF-113, RF-114 | 2 |
| RF-048.2 | RF | El sistema deberá mostrar las condiciones de devolución y de garantía legal aplicables a esa unidad. | Regla 1 (conjunción) | RF-115, RF-116 | 2 |
| RF-002.5 | RF | El sistema deberá permitir registrar el resultado del conteo cíclico sin bloquear la operación de venta de la sala. | Regla 5 (separación RF/RNF) | RF-135, RNF-03 | 2 |
| RF-045 | RF | El sistema deberá generar un reporte periódico de referencias con atributos incompletos, errores de publicación o publicaciones fallidas, indicando la causa del error. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RF-147, RF-148 | 2 |
| RF-046.1 | RF | El sistema deberá permitir al gerente de logística definir el valor del colchón de confianza por categoría o por punto de existencia. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RF-149, RF-150 | 2 |
| RF-047.3 | RF | El sistema deberá permitir al vendedor de piso confirmar el reingreso de la unidad a sala o su venta. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RF-155, RF-156 | 2 |
| RF-058 | RF | El sistema deberá calcular el porcentaje de error probable de la categoría en función de la categoría y del punto de existencia. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RF-158, RF-159 | 2 |
| RF-025.4 | RF | El sistema deberá permitir al oficial de cumplimiento mantener el inventario de interfaces de cruce declaradas, exigiendo finalidad, base de licitud y autorización nominada por cada interfaz. | Regla 1 (conjunción); Regla 2 (verbo único) | RF-168, RF-169 | 2 |
| RF-026.1 | RF | El sistema deberá permitir declarar y parametrizar previamente el orden de degradación y los criterios que lo activan. | Regla 1 (conjunción); Regla 2 (verbo único) | RF-177, RF-178 | 2 |
| RF-019 | RF | El sistema deberá permitir al ejecutivo atender la garantía legal íntegramente en el mesón, sin derivar al cliente al fabricante, al servicio técnico ni al vendedor de marketplace como condición para ser atendido. | Regla 1 (conjunción); Regla 2 (verbo único) | RF-187, RF-188 | 2 |
| RF-088 | RF | El sistema deberá registrar la opción ofrecida al consumidor y la opción efectivamente elegida por el. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RF-193, RF-194 | 2 |
| RF-024A | RF | El sistema deberá permitir al ejecutivo de cobranza iniciar y registrar la gestión de cobranza dentro de los límites normativos de horario y medio de contacto. | Regla 1 (conjunción); Regla 2 (verbo único); Regla 3 (testabilidad aislada) | RF-211, RF-212, RF-213 | 3 |
| RF-024B | RF | El sistema deberá enlazar el expediente de la repactación con la gestión de cobranza que la originó y con la evidencia de consentimiento de RF-207. | Regla 1 (conjunción); Regla 2 (verbo único) | RF-214, RF-215 | 2 |
| NFR-03 | RNF | La migración de la cartera de crédito viva no debe generar pérdida de datos, interrupción del servicio de cobro ni divergencia de saldos. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RNF-08, RNF-09, RNF-10 | 3 |
| NFR-04 | RNF | La separación lógica entre los datos del retail y los del negocio financiero debe estar implementada, documentada y verificada por auditoría independiente. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RNF-11, RNF-12, RNF-13 | 3 |
| NFR-07 | RNF | La plataforma debe soportar la concurrencia y el volumen de los dos peaks descritos sin degradar los umbrales de NFR-06.x. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RNF-22, RNF-23 | 2 |
| NFR-08.3 | RNF | La sincronización tras la reconexión no debe superar el plazo definido. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RNF-26, RNF-27 | 2 |
| NFR-09.2 | RNF | El canal digital y los servicios financieros que afectan pagos, estados de cuenta y bloqueo de tarjetas deben estar disponibles de forma continua. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RNF-30, RNF-31 | 2 |
| NFR-14 | RNF | Debe exigirse un mecanismo de consentimiento con integridad verificable, adecuado al canal, en apertura de tarjeta, repactación, conformidad de recepción de mercadería y constancia de devolución. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RNF-39, RNF-40 | 2 |
| NFR-20 | RNF | La solución debe adoptar estándares identificados y justificados para catálogo de producto, intercambio con los 940 proveedores, transportistas de última milla, sincronización con marketplace y documento tributario electrónico. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RNF-52, RNF-53, RNF-54, RNF-55, RNF-56 | 5 |
| NFR-29 | RNF | El tiempo entre la detección de un quiebre y el aviso al cliente no debe superar el objetivo declarado. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RNF-64, RNF-65 | 2 |
| NFR-30 | RNF | La latencia entre la recepción física de una devolución en tienda y la notificacion al vendedor de marketplace no debe superar el objetivo declarado. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RNF-66, RNF-67 | 2 |
| NFR-34 | RNF | El ciclo de desarrollo debe producir SBOM por artefacto y alcanzar el nivel de integridad de cadena de suministro exigido. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RNF-70, RNF-71, RNF-72, RNF-73 | 4 |
| NFR-35 | RNF | El tratamiento de datos personales debe cumplir la Ley 21.719, incluyendo finalidad declarada, base de licitud y registro de actividades de tratamiento. | Regla 1 (conjunción); Regla 3 (testabilidad aislada) | RNF-74, RNF-75, RNF-76 | 3 |
|  |  |  |  | TOTAL | 96 |

## 3_Hallazgos_v3

<!-- hoja: 3_Hallazgos_v3 | filas de datos: 8 -->

| ID | Tipo | Descripción del hallazgo | Impacto | Tratamiento aplicado | Estrategia de riesgo (PMBOK 6.ª ed., §11.5.2.2) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| H-16 | Requerimiento que no es de software | RF-034, RF-043, RF-120, RF-121 y RF-122 exigen al PROPONENTE especificar y costear, no al sistema ejecutar una función. El hallazgo H-11 de la versión anterior lo detectó pero no lo resolvió: las filas siguieron numeradas como RF. | Nueve obligaciones contractuales contaminaban el catálogo funcional y habrían entrado a la EDT como paquetes de desarrollo. | Reclasificadas a OP-01 a OP-09 y separadas del catálogo funcional. Se verifican documentalmente en la Oferta Técnica y en el Entregable 2 de la Oferta Económica. | Evitar |
| H-17 | Mezcla de funcionalidad y calidad | RF-042.2 incorporaba el plazo «antes de la apertura de sala» y RF-002.5 incorporaba «sin bloquear la operación de venta»; RF-016A.1 incorporaba «en cualquier momento», que es disponibilidad. | Un fallo del umbral habría sido reportado como defecto funcional, y el umbral no tenía método de verificación asignado. | Se extraen RNF-01, RNF-03 y RNF-02 conforme a la Regla 5, cada uno con su métrica y su método de verificación. | Mitigar |
| H-18 | Consulta compuesta sobre la frontera de datos | RF-037 unía cuatro consultas del cliente autenticado, dos de ellas (estado de cuenta y documentos) sobre datos de la filial emisora fiscalizada. | Mientras el requerimiento fuera uno solo, era imposible aplicarle un control de cruce distinto a la parte financiera. Agrava el hallazgo H-04 de la versión anterior. | Dividido en RF-067 a RF-070. Las consultas del ámbito financiero quedan sujetas a la resolución de identidad de RF-174 y al registro de cruce de RF-165. | Mitigar |
| H-19 | Requerimientos no confirmados por el equipo | Nueve filas conservan «??» en la columna de revisión: RF-001, RF-018, RF-028, RF-120, RF-170, RF-176, RF-160, RF-181 y RF-183. | Son requerimientos vigentes en el catálogo sin decisión formal de aceptación; dos de ellos (RF-160 y RF-028) tienen impacto directo sobre lo que se publica al consumidor. | Se listan como pendientes de resolución en el período de consultas. Hasta su confirmación se mantienen en el catálogo con la marca de no validados. | Aceptar (activa) |
| H-20 | Referencia normativa incorrecta | RF-002 cita el requisito RT-11.10 del Capítulo 15 como origen. Ese requisito trata del cifrado a nivel de campo, no del control de acceso. La observación ya estaba anotada en el catálogo v2.1 y no se corrigió. | Una cita de origen incorrecta invalida la verificación de trazabilidad que la Comisión de Expertos aplicará al catálogo. | Se propone sustituir la cita por RT-12.11 (autenticación en el perfil operacional), que es el requisito aplicable a terminales compartidas y credenciales individuales. | Evitar |
| H-21 | Indicador de negocio catalogado como atributo de calidad | RNF-61, RNF-62 y RNF-63 expresan metas de negocio (tasa de cancelación, cumplimiento de la promesa y exactitud de inventario), no atributos de calidad del software. | Son criterios de aceptación del Capítulo 18 del caso. Catalogados como RNF, el ADJUDICATARIO queda comprometido a un resultado que depende también de la operación del CLIENTE. | Se conservan por su valor contractual, marcados como efectividad de negocio. Se recomienda declarar explícitamente en la Oferta Técnica qué parte del indicador depende de la solución y qué parte de la operación del CLIENTE. | Transferir |
| H-22 | Dimensión de cálculo no desagregada | RF-058 calculaba el error probable en función de la categoría y del punto de existencia en un solo enunciado, mientras que el colchón de confianza sí estaba desagregado en RF-128 y RF-129. | Inconsistencia de criterio dentro del propio catálogo: dos cálculos equivalentes atomizados con distinto grado de detalle. | Dividido en RF-158 y RF-159 para alinearlo con el criterio ya aplicado al colchón. | Mitigar |
| Los hallazgos H-01 a H-15 de la versión 2.1 se mantienen vigentes y no se reproducen aquí. Esta hoja recoge únicamente lo detectado en la auditoría de atomicidad. |  |  |  |  |  |

## 4_Resumen

<!-- hoja: 4_Resumen | filas de datos: 9 -->

| Indicador | Valor |
| :--- | :--- |
| Requerimientos funcionales (RF) | 223 |
| Requerimientos no funcionales (NFR) | 75 |
| Obligaciones del PROPONENTE (OP) | 9 |
| Total de filas del catálogo atómico | 307 |
| Requerimientos de entrada (catálogo v2.1) | 256 |
| Requerimientos de entrada divididos o reclasificados | 41 |
| Filas conservadas sin división | 212 |
| Incremento neto de filas respecto de v2.1 | 51 |
| Los valores se calculan por fórmula sobre la hoja 1_Catalogo_Atomico; al agregar o quitar filas, el resumen se actualiza. |  |

## 6_Equivalencia_IDs

<!-- hoja: 6_Equivalencia_IDs | filas de datos: 311 -->

| ID nuevo | ID anterior (v3.0) | Tipo | Descripción atómica |
| :--- | :--- | :--- | :--- |
| RF-001 | RF-010.6 | RF | El sistema deberá permitir la venta física de la unidad aunque exista una reserva temporal activa en el canal digital. |
| RF-002 | RF-044.1 | RF | El sistema deberá exigir credenciales individuales al usuario antes de habilitar cualquier acción. |
| RF-003 | RF-044.2a | RF | El sistema debe impedir el acceso anónimo a una terminal. |
| RF-004 | RF-044.2b | RF | El sistema debe impedir el acceso mediante credencial compartida. |
| RF-005 | RF-044.3 | RF | El sistema deberá permitir el traspaso de sesión nominativa entre usuarios en una terminal compartida. |
| RF-006 | RF-044.4 | RF | El sistema deberá cerrar automáticamente la sesión por inactividad en la terminal compartida. |
| RF-007 | RF-101 | RF | El sistema deberá impedir la ejecución de la función de originación a un usuario sin capacitación normativa acreditada y vigente. |
| RF-008 | RF-102 | RF | El sistema deberá impedir la ejecución de la función de repactación a un usuario sin capacitación normativa acreditada y vigente. |
| RF-009 | RF-103 | RF | El sistema deberá revocar automáticamente la habilitación funcional del usuario al vencer su acreditación de capacitación. |
| RF-010 | RF-115 | RF | El sistema deberá permitir al proveedor patrocinar la habilitación temporal de acceso de su repositor externo, con fecha de término declarada. |
| RF-011 | RF-116 | RF | El sistema deberá caducar automáticamente la habilitación de acceso del personal externo al cumplirse su vigencia. |
| RF-012 | RF-117 | RF | El sistema deberá registrar de forma individualizada el acceso y la actividad del personal externo. |
| RF-013 | RF-118 | RF | El sistema deberá revocar la totalidad de los accesos y credenciales del trabajador a partir del término efectivo de su vínculo. |
| RF-014 | RF-119a | RF | El sistema debe conciliar los accesos vigentes contra la nómina activa. |
| RF-015 | RF-119b | RF | El sistema debe informar al oficial de seguridad los accesos huérfanos detectados en la conciliación. |
| RF-016 | RF-006.1 | RF | El sistema deberá propagar el cambio de precio a las 380 líneas de caja. |
| RF-017 | RF-006.2 | RF | El sistema deberá propagar el cambio de precio al canal digital. |
| RF-018 | RF-006.3 | RF | El sistema deberá propagar el cambio de precio a los puntos de exhibición física de cada tienda afectada. |
| RF-019 | RF-007.1 | RF | El sistema deberá permitir al reponedor registrar la referencia y la tienda de la etiqueta cambiada, con el instante del cambio. |
| RF-020 | RF-007.2 | RF | El sistema deberá registrar la identidad individual del ejecutor del cambio de etiqueta. |
| RF-021 | RF-008 | RF | El sistema deberá permitir al ejecutivo de cumplimiento recuperar el precio publicado de una referencia para una fecha, hora y canal determinados. |
| RF-022 | RF-009.1 | RF | El sistema deberá obtener el precio vigente de la referencia según el último precio propagado a la etiqueta de esa tienda en la fecha de la venta. |
| RF-023 | RF-009.2 | RF | El sistema deberá cobrar el menor de ambos precios para el consumidor. |
| RF-024 | RF-009.3 | RF | El sistema deberá generar un registro de incidente de discrepancia de precio consultable. |
| OP-01 | OP-01 | OP | El PROPONENTE debe especificar la alternativa de etiquetas electrónicas frente a las demás opciones de resolución de la discrepancia de precio. |
| OP-02 | OP-02 | OP | El PROPONENTE debe costear la alternativa de etiquetas electrónicas sin asumir su adquisición dentro del alcance. |
| RF-025 | RF-041 | RF | El sistema deberá propagar el cambio de precio a cada etiqueta electrónica de la referencia afectada. |
| RF-026 | RF-042.1 | RF | El sistema deberá detectar la no confirmación del cambio de precio por parte de una etiqueta electrónica. |
| RF-027 | RF-042.2a | RF | El sistema debe generar una alerta operativa al jefe de tienda identificando la etiqueta electrónica no confirmada. |
| RNF-01 | NFR-37 | RNF | La alerta de etiqueta electrónica no confirmada debe emitirse antes de la apertura de sala. |
| OP-03 | OP-03 | OP | El PROPONENTE debe especificar la cobertura de despliegue de las etiquetas electrónicas. |
| OP-04 | OP-04 | OP | El PROPONENTE debe especificar el hardware requerido por la alternativa de etiquetas electrónicas. |
| OP-05 | OP-05 | OP | El PROPONENTE debe presentar el costo de la alternativa separadamente del resto de la solución. |
| RF-028 | RF-064 | RF | El sistema deberá impedir la venta de la referencia al precio nuevo mientras su punto de exhibición no confirme la actualización, salvo que el artículo se encuentre bloqueado para venta. |
| RF-029 | RF-065 | RF | El sistema deberá generar un indicador diario de puntos de exhibición desactualizados con identificación individual de cada punto. |
| RF-030 | RF-066 | RF | El sistema deberá agrupar los cambios de precio de sala en ventanas parametrizadas fuera del horario de atención. |
| RF-031 | RF-067 | RF | El sistema deberá excluir los puntos con etiqueta electrónica de la ventana de agrupamiento definida en RF-030. |
| RF-032 | RF-068 | RF | El sistema deberá evaluar la vigencia de cada promoción al instante de emisión del documento. |
| RF-033 | RF-069 | RF | El sistema deberá evaluar la aplicabilidad de la promoción según el canal de la venta. |
| RF-034 | RF-070 | RF | El sistema deberá evaluar la aplicabilidad de la promoción según la tienda en que se realiza la venta. |
| RF-035 | RF-010.1 | RF | El sistema deberá crear una reserva temporal para la unidad agregada al carro. |
| RF-036 | RF-010.2 | RF | El sistema deberá permitir parametrizar el período de vigencia de la reserva temporal. |
| RF-037 | RF-010.3 | RF | El sistema deberá mantener activa la reserva mientras el cliente mantenga actividad, conforme al período parametrizado. |
| RF-038 | RF-010.4 | RF | El sistema deberá impedir que una misma unidad sea comprometida simultáneamente en más de una operación de venta digital. |
| RF-039 | RF-010.5a | RF | El sistema debe liberar la reserva temporal al expirar su período de vigencia. |
| RF-040 | RF-010.5b | RF | El sistema debe devolver la unidad liberada al disponible para vender. |
| RF-041 | RF-010.7 | RF | El sistema deberá liberar de inmediato la reserva digital de esa unidad, sin esperar la expiración del período. |
| RF-042 | RF-010.8 | RF | El sistema deberá aplicar el período de vigencia de reserva reducido declarado como parámetro para el evento anual. |
| RF-043 | RF-011.1 | RF | El sistema deberá preautorizar el medio de pago al aceptar el pedido, sin capturar el cobro. |
| RF-044 | RF-011.2 | RF | El sistema deberá verificar la existencia física real de la unidad en el punto asignado antes de habilitar la captura del cobro. |
| RF-045 | RF-011.3 | RF | El sistema deberá capturar el cobro únicamente al registrarse el evento de confirmación de la preparacion física. |
| RF-046 | RF-011.4 | RF | El sistema deberá determinar automáticamente la alternativa de resolución aplicable según el motor de reglas (cancelar, sustituir, derivar a tercero o entrega diferida). |
| RF-047 | RF-011.5 | RF | El sistema deberá requerir la aceptación explícita del cliente antes de capturar el cobro. |
| RF-048 | RF-011.6 | RF | El sistema deberá anular la preautorización de pago del pedido. |
| RF-049 | RF-011.7 | RF | El sistema deberá cancelar el pedido registrando el motivo de la cancelación. |
| RF-050 | RF-011.8 | RF | El sistema deberá generar la conciliación diaria de preautorizaciones vencidas sin captura. |
| RF-051 | RF-011.9 | RF | El sistema deberá notificar al cliente el cambio de estado de su pedido antes de efectuar cualquier cobro definitivo. |
| RF-052 | RF-012 | RF | El sistema deberá permitir a todos los actores consultar el estado del pedido desde una única fuente de verdad. |
| RF-053 | RF-013 | RF | El sistema deberá permitir marcar como no elegible para cumplimiento digital el stock de exhibición de las categorías declaradas. |
| RF-054 | RF-014a | RF | El sistema debe calcular la base de comisión reconociendo al vendedor y a la tienda de origen de la unidad. |
| RF-055 | RF-014b | RF | El sistema debe validar la base de comisión calculada contra el movimiento real de inventario antes de liberarla para pago. |
| RF-056 | RF-015.1 | RF | El sistema deberá reasignar el pedido a otro punto de despacho con existencia disponible. |
| RF-057 | RF-015.2 | RF | El sistema deberá impedir una segunda reasignación del mismo pedido. |
| RF-058 | RF-015.3 | RF | El sistema deberá acotar la reasignación a la ventana de tiempo parametrizada. |
| RF-059 | RF-015.4 | RF | El sistema deberá ofrecer al cliente un producto equivalente. |
| RF-060 | RF-015.5 | RF | El sistema deberá ofrecer al cliente la espera compensada con la compensación parametrizada. |
| RF-061 | RF-015.6 | RF | El sistema deberá ofrecer al cliente la liberacion del pedido con anulación de la preautorización. |
| RF-062 | RF-035a | RF | El sistema debe monitorear el tiempo restante de cada pedido respecto de su fecha prometida de entrega. |
| RF-063 | RF-035b | RF | El sistema debe priorizar la preparación del pedido al alcanzar el umbral parametrizado de tiempo restante. |
| RF-064 | RF-036A.1 | RF | El sistema debe permitir al cliente no autenticado consultar el precio vigente de una referencia. |
| RF-065 | RF-036A.2 | RF | El sistema debe permitir al cliente no autenticado consultar la disponibilidad de la referencia por tienda. |
| RF-066 | RF-036A.3 | RF | El sistema debe permitir al cliente no autenticado consultar la disponibilidad de la referencia para despacho. |
| RF-067 | RF-037.1 | RF | El sistema debe permitir al cliente autenticado consultar sus compras. |
| RF-068 | RF-037.2 | RF | El sistema debe permitir al cliente autenticado consultar sus devoluciones. |
| RF-069 | RF-037.3 | RF | El sistema debe permitir al cliente autenticado consultar su estado de cuenta. |
| RF-070 | RF-037.4 | RF | El sistema debe permitir al cliente autenticado consultar sus documentos. |
| RF-071 | RF-040 | RF | El sistema deberá calcular la base de comisión considerando el canal de origen y el canal de cumplimiento cuando estos difieran. |
| RF-072 | RF-049a | RF | El sistema debe permitir al ejecutivo de mesón consultar el estado real del pedido. |
| RF-073 | RF-049b | RF | El sistema debe permitir al ejecutivo de mesón consultar el precio aplicado al pedido. |
| RF-074 | RF-049c | RF | El sistema debe permitir al ejecutivo de mesón ofrecer al cliente las opciones de resolución definidas en RF-059, RF-060 y RF-061. |
| RF-075 | RF-057 | RF | El sistema deberá excluir al centro de distribución de Concepción como origen de promesa de entrega en el canal digital mientras no este acreditado su sistema de gestión de almacenes. |
| RF-076 | RF-071 | RF | El sistema deberá calcular el costo total de servir de cada punto de despacho candidato, incorporando costo logístico, costo de oportunidad de sala y plazo comprometido. |
| RF-077 | RF-072 | RF | El sistema deberá seleccionar como punto de despacho aquel de menor costo total de servir. |
| RF-078 | RF-073 | RF | El sistema deberá registrar el valor de cada término del costo total de servir que fundamento la seleccion. |
| RF-079 | RF-074 | RF | El sistema deberá calcular la fecha prometida de entrega en función del punto de despacho, la capacidad de preparacion y el transportista asignado. |
| RF-080 | RF-075 | RF | El sistema deberá impedir la publicación de un plazo fijo de catálogo como fecha prometida de entrega. |
| RF-081 | RF-076 | RF | El sistema deberá calcular el cumplimiento de la promesa de entrega por pedido individual. |
| RF-082 | RF-029.1 | RF | El sistema deberá detectar la pérdida del enlace externo y conmutar automáticamente la tienda a modo desconectado. |
| RF-083 | RF-029.2 | RF | El sistema deberá permitir al cajero registrar una venta en modo desconectado. |
| RF-084 | RF-029.3 | RF | El sistema deberá permitir al cajero cobrar la venta en modo desconectado. |
| RF-085 | RF-029.4 | RF | El sistema deberá aplicar las promociones vigentes en modo desconectado, evaluadas según RF-032, RF-033 y RF-034. |
| RF-086 | RF-029.5 | RF | El sistema deberá emitir el documento de venta en contingencia utilizando folios previamente asignados por el sistema de gestión empresarial. |
| RF-087 | RF-029.6 | RF | El sistema deberá permitir al vendedor consultar la existencia local de la tienda en modo desconectado. |
| RF-088 | RF-029.7 | RF | El sistema deberá detectar el restablecimiento del enlace y conmutar la tienda a modo conectado. |
| RF-089 | RF-104 | RF | El sistema deberá permitir el otorgamiento de crédito en modo desconectado exclusivamente contra cupo preaprobado vigente almacenado en caché local. |
| RF-090 | RF-105 | RF | El sistema deberá aplicar el tope de monto parametrizado a cada operación de crédito cursada en modo desconectado. |
| RF-091 | RF-106 | RF | El sistema deberá aplicar el tope parametrizado de número de operaciones de crédito en modo desconectado. |
| RF-092 | RF-107 | RF | El sistema deberá impedir la apertura de una tarjeta nueva en modo desconectado. |
| RF-093 | RF-108 | RF | El sistema deberá impedir la ampliación de cupo en modo desconectado. |
| RF-094 | RF-109 | RF | El sistema deberá marcar la operación como cursada en modo desconectado para su validación posterior. |
| RF-095 | RF-110a | RF | El sistema debe reconciliar hacia los sistemas centrales la totalidad de las ventas registradas en modo desconectado. |
| RF-096 | RF-110b | RF | El sistema debe reconciliar hacia los sistemas centrales la totalidad de los documentos emitidos en modo desconectado. |
| RF-097 | RF-111 | RF | El sistema deberá procesar la reconciliación de forma idempotente, impidiendo la duplicación de ventas o documentos ante reintentos. |
| RF-098 | RF-112 | RF | El sistema deberá resolver el conflicto de existencia comprometida aplicando la regla de precedencia declarada, produciendo el mismo resultado ante repetición. |
| RF-099 | RF-113 | RF | El sistema deberá generar un informe de excepciones de la reconciliación, identificando cada conflicto resuelto y su regla aplicada. |
| RF-100 | RF-114 | RF | El sistema deberá enrutar la emisión de todo documento tributario hacia el sistema de gestión empresarial como único emisor. |
| RF-101 | RF-039 | RF | El sistema deberá permitir al vendedor de piso consultar la disponibilidad para vender de una referencia. |
| OP-06 | OP-06 | OP | El PROPONENTE debe especificar la cantidad de dispositivos móviles requeridos por tienda y por departamento. |
| OP-07 | OP-07 | OP | El PROPONENTE debe especificar las características técnicas de los dispositivos móviles requeridos. |
| OP-08 | OP-08 | OP | El PROPONENTE debe presentar el análisis de hacer o comprar del centro de distribución de Concepción con sus tres alternativas. |
| OP-09 | OP-09 | OP | El PROPONENTE debe declarar el impacto de la alternativa seleccionada sobre el cumplimiento de RN-15. |
| RF-102 | RF-016A.1a | RF | El sistema debe permitir al vendedor de marketplace declarar la existencia de sus referencias. |
| RF-103 | RF-016A.1b | RF | El sistema debe permitir al vendedor de marketplace actualizar la existencia previamente declarada. |
| RNF-02 | NFR-36 | RNF | La interfaz de declaración de existencia del vendedor de marketplace debe estar disponible de forma continua. |
| RF-104 | RF-016A.2 | RF | El sistema deberá registrar cada actualización de existencia declarada con su fecha y hora. |
| RF-105 | RF-016B | RF | El sistema deberá calcular los indicadores de nivel de servicio por vendedor externo según las reglas publicadas. |
| RF-106 | RF-017.1 | RF | El sistema deberá notificar al vendedor de marketplace la recepción de la devolución en el momento en que se registra. |
| RF-107 | RF-017.2 | RF | El sistema deberá permitir al ejecutivo registrar que parte asume el costo de la devolución. |
| RF-108 | RF-017.3 | RF | El sistema deberá permitir al ejecutivo registrar la prestación entregada al cliente (reparación, reposición o devolución del precio). |
| RF-109 | RF-018 | RF | El sistema deberá publicar únicamente la existencia declarada en la última actualización vigente del vendedor. |
| RF-110 | RF-038.1 | RF | El sistema debe permitir al vendedor de marketplace consultar el estado de cada pedido intermediado. |
| RF-111 | RF-038.2 | RF | El sistema debe permitir al vendedor de marketplace consultar las devoluciones de sus pedidos. |
| RF-112 | RF-038.3 | RF | El sistema debe permitir al vendedor de marketplace consultar su evaluación de desempeño vigente. |
| RF-113 | RF-048.1a | RF | El sistema debe identificar visiblemente al vendedor de la unidad en el catálogo, la ficha de producto y el proceso de compra. |
| RF-114 | RF-048.1b | RF | El sistema debe identificar visiblemente a quien despacha la unidad en el catálogo, la ficha de producto y el proceso de compra. |
| RF-115 | RF-048.2a | RF | El sistema debe mostrar las condiciones de devolución aplicables a la unidad. |
| RF-116 | RF-048.2b | RF | El sistema debe mostrar las condiciones de garantía legal aplicables a la unidad. |
| RF-117 | RF-077 | RF | El sistema deberá impedir que un pedido intermediado comprometa existencia propia de la compañía. |
| RF-118 | RF-078 | RF | El sistema deberá impedir que una unidad de inventario propio sea asignada al cumplimiento de un pedido de marketplace. |
| RF-119 | RF-079 | RF | El sistema deberá registrar el acuse de conocimiento de las reglas de evaluación por parte de cada vendedor externo. |
| RF-120 | RF-080 | RF | El sistema deberá impedir la aplicación de una regla de evaluación a un vendedor que no tenga acuse de conocimiento previo de esa regla. |
| RF-121 | RF-081 | RF | El sistema deberá determinar la consecuencia escalonada aplicable según la matriz de escalamiento parametrizada (advertencia, restricción de publicación, suspensión). |
| RF-122 | RF-082 | RF | El sistema deberá requerir la ejecución de la sanción por el rol nominado en la matriz de escalamiento. |
| RF-123 | RF-083 | RF | El sistema deberá registrar la trazabilidad de la sanción aplicada, indicando regla incumplida, consecuencia, rol ejecutor e instante. |
| RF-124 | RF-084 | RF | El sistema deberá despublicar automáticamente la oferta cuyo stock declarado haya superado el plazo de vigencia sin actualización. |
| RF-125 | RF-085 | RF | El sistema deberá devengar la comisión de marketplace sobre la venta efectivamente cumplida. |
| RF-126 | RF-086 | RF | El sistema deberá revertir la comisión devengada en el período contable en que ocurre la devolución o cancelación. |
| RF-127 | RF-001.1 | RF | El sistema deberá calcular la existencia disponible para vender restando de la existencia registrada las reservas vigentes, el comprometido no despachado y el colchón de confianza aplicable. |
| RF-128 | RF-001.2 | RF | El sistema deberá determinar el valor del colchón de confianza aplicable en función de la categoría del artículo. |
| RF-129 | RF-001.3 | RF | El sistema deberá determinar el valor del colchón de confianza aplicable en función del punto de existencia. |
| RF-130 | RF-001.4 | RF | El sistema deberá registrar la traza del cálculo del disponible, incluyendo el valor de cada término de la fórmula y la versión de parámetros aplicada. |
| RF-131 | RF-002.1 | RF | El sistema deberá permitir parametrizar la frecuencia de conteo cíclico por categoría. |
| RF-132 | RF-002.2 | RF | El sistema deberá permitir parametrizar el método de conteo por categoría. |
| RF-133 | RF-002.3 | RF | El sistema deberá permitir parametrizar el criterio de gatillo de recuento extraordinario por categoría. |
| RF-134 | RF-002.4 | RF | El sistema deberá generar la programación de conteos cíclicos según la frecuencia parametrizada de cada categoría. |
| RF-135 | RF-002.5a | RF | El sistema debe permitir registrar el resultado del conteo cíclico. |
| RNF-03 | NFR-38 | RNF | El registro del conteo cíclico no debe bloquear ni degradar la operación de venta de la sala. |
| RF-136 | RF-002.6 | RF | El sistema deberá señalar automáticamente los pasillos o referencias que requieren recuento extraordinario. |
| RF-137 | RF-002.7 | RF | El sistema deberá calcular la exactitud de inventario resultante por categoría. |
| RF-138 | RF-003.1 | RF | El sistema deberá permitir clasificar cada diferencia detectada en uno de los componentes de merma definidos (pérdida física, daño no dado de baja, error de recepción, unidad mal ubicada, devolución mal reintegrada, error de digitación). |
| RF-139 | RF-003.2 | RF | El sistema deberá impedir el cierre de un ajuste de inventario que no tenga asignado un componente de merma. |
| RF-140 | RF-003.3 | RF | El sistema deberá cuantificar el monto y la proporción de cada componente de merma sobre el total del período. |
| RF-141 | RF-003.4 | RF | El sistema deberá generar el informe mensual de merma cuya suma de componentes sea igual al total registrado en el período. |
| RF-142 | RF-004A | RF | El sistema deberá exigir al analista comercial completar los atributos obligatorios de la referencia (categoría, dimensiones, fragilidad, volumen, restricción de despacho) antes de guardar el registro como apto para uso operativo. |
| RF-143 | RF-004B | RF | El sistema deberá impedir la publicación de esa referencia en el canal digital mientras no cuente con los atributos obligatorios completos. |
| RF-144 | RF-005.1 | RF | El sistema deberá generar automáticamente la propuesta diaria de reposición utilizando el disponible para vender calculado en RF-127. |
| RF-145 | RF-005.2 | RF | El sistema deberá permitir al planificador de logística ajustar la propuesta de reposición antes de confirmar el envío. |
| RF-146 | RF-005.3 | RF | El sistema deberá registrar el ajuste realizado indicando usuario, valor propuesto, valor confirmado e instante. |
| RF-147 | RF-045a | RF | El sistema debe generar un reporte periódico de referencias con atributos obligatorios incompletos. |
| RF-148 | RF-045b | RF | El sistema debe generar un reporte periódico de publicaciones fallidas indicando la causa del error. |
| RF-149 | RF-046.1a | RF | El sistema debe permitir al gerente de logística definir el valor del colchón de confianza por categoría. |
| RF-150 | RF-046.1b | RF | El sistema debe permitir al gerente de logística definir el valor del colchón de confianza por punto de existencia. |
| RF-151 | RF-046.2 | RF | El sistema deberá registrar quien definio o modifico el colchón, cuando, el valor anterior y el valor nuevo. |
| RF-152 | RF-046.3 | RF | El sistema deberá sugerir un valor de referencia del colchón calculado a partir del histórico de ventas y quiebres de la categoría. |
| RF-153 | RF-047.1 | RF | El sistema deberá permitir al vendedor de piso registrar las unidades que ingresan al probador. |
| RF-154 | RF-047.2 | RF | El sistema deberá excluir del disponible para vender las unidades registradas en probador. |
| RF-155 | RF-047.3a | RF | El sistema debe permitir al vendedor de piso confirmar el reingreso a sala de la unidad registrada en probador. |
| RF-156 | RF-047.3b | RF | El sistema debe permitir al vendedor de piso registrar la venta de la unidad registrada en probador. |
| RF-157 | RF-054 | RF | El sistema deberá impedir que cualquier canal de venta consuma el saldo bruto de inventario para publicar o comprometer existencia. |
| RF-158 | RF-058a | RF | El sistema debe calcular el porcentaje de error probable de la referencia en función de su categoría. |
| RF-159 | RF-058b | RF | El sistema debe calcular el porcentaje de error probable de la referencia en función de su punto de existencia. |
| RF-160 | RF-059 | RF | El sistema deberá mostrar al cliente el porcentaje de error probable calculado en RF-058 junto a la disponibilidad publicada. |
| RF-161 | RF-060 | RF | El sistema deberá mostrar al vendedor de piso el porcentaje de error probable calculado en RF-058. |
| RF-162 | RF-061 | RF | El sistema deberá generar una alerta interna dirigida al rol facultado cuando la exactitud de una categoría caiga bajo el umbral definido. |
| RF-163 | RF-062 | RF | El sistema deberá permitir exclusivamente al rol facultado suspender manualmente la publicación de una categoría. |
| RF-164 | RF-063 | RF | El sistema deberá abstenerse de suspender automáticamente la publicación de una categoría que no tenga una regla de degradación declarada y aprobada previamente. |
| RF-165 | RF-025.1 | RF | El sistema deberá registrar cada cruce de información ejecutado entre ámbitos, indicando el dato cruzado, la finalidad, la base de licitud, la autorización nominada y el instante. |
| RF-166 | RF-025.2 | RF | El sistema deberá bloquear todo intento de cruce de información que no corresponda a una interfaz declarada en el inventario de flujos autorizados. |
| RF-167 | RF-025.3 | RF | El sistema deberá registrar el intento de cruce bloqueado con el componente origen, el dato solicitado y el instante. |
| RF-168 | RF-025.4a | RF | El sistema debe permitir al oficial de cumplimiento mantener el inventario de interfaces de cruce declaradas. |
| RF-169 | RF-025.4b | RF | El sistema debe impedir el registro de una interfaz de cruce que no declare finalidad, base de licitud y autorización nominada. |
| RF-170 | RF-032.1 | RF | El sistema deberá excluir del catálogo de atributos disponibles en el motor de campañas todo atributo de origen financiero (mora, deuda, cupo utilizado, comportamiento de pago). |
| RF-171 | RF-032.2 | RF | El sistema deberá rechazar la ejecución de toda facilidad comercial que invoque un atributo de origen financiero sin un registro de cruce autorizado asociado. |
| RF-172 | RF-032.3 | RF | El sistema deberá rechazar la ejecución de todo proceso crediticio que invoque un atributo de origen retail sin un registro de cruce autorizado asociado. |
| RF-173 | RF-050 | RF | El sistema deberá asignar a la misma persona un identificador distinto en el ámbito retail y en el ámbito fiscalizado. |
| RF-174 | RF-051 | RF | El sistema deberá resolver la correspondencia entre identificadores exclusivamente a través de una tabla de correspondencia custodiada, con acceso nominado y registrado. |
| RF-175 | RF-052 | RF | El sistema deberá rechazar la persistencia de la clave del ámbito financiero como columna o atributo en cualquier entidad del ámbito retail. |
| RF-176 | RF-053 | RF | El sistema deberá exigir el registro de la evaluación de impacto sobre la frontera de datos antes de habilitar el estado 'aprobada' de una iniciativa. |
| RF-177 | RF-026.1a | RF | El sistema debe permitir declarar previamente el orden de degradación de los servicios. |
| RF-178 | RF-026.1b | RF | El sistema debe permitir parametrizar los criterios que activan cada nivel de degradación declarado. |
| RF-179 | RF-026.2 | RF | El sistema deberá suspender la publicación de la categoría indicada por el orden de degradación declarado. |
| RF-180 | RF-026.3 | RF | El sistema deberá reducir el límite de unidades por cliente al valor declarado. |
| RF-181 | RF-026.4 | RF | El sistema deberá desactivar temporalmente los medios de pago de mayor fricción operativa declarados. |
| RF-182 | RF-027.1 | RF | El sistema deberá monitorear en tiempo real la tasa de cancelación por falta de existencia por categoría. |
| RF-183 | RF-027.2 | RF | El sistema deberá activar la acción de degradación declarada para esa categoría en RF-026.1. |
| RF-184 | RF-028.1 | RF | El sistema deberá permitir parametrizar las cinco ventanas de congelamiento (1 nov - 6 ene; evento anual y su semana previa; evento de noviembre; semana del Día de la Madre; última semana de enero a primera de marzo). |
| RF-185 | RF-028.2 | RF | El sistema deberá impedir la ejecución del despliegue o intervención en producción durante la ventana de congelamiento. |
| RF-186 | RF-028.3 | RF | El sistema deberá registrar el intento de despliegue bloqueado, indicando componente, solicitante e instante. |
| RF-187 | RF-019a | RF | El sistema debe permitir al ejecutivo de mesón atender íntegramente el caso de garantía legal en la tienda. |
| RF-188 | RF-019b | RF | El sistema debe impedir que el flujo de atención exija la derivación del consumidor al fabricante, al servicio técnico o al vendedor de marketplace como condición para ser atendido. |
| RF-189 | RF-020 | RF | El sistema deberá permitir al ejecutivo registrar el motivo de la devolución (talla, color, expectativa, falla). |
| RF-190 | RF-055 | RF | El sistema deberá impedir el reingreso de una unidad devuelta al inventario disponible mientras no exista una decisión de aptitud registrada. |
| RF-191 | RF-056 | RF | El sistema deberá permitir al ejecutivo registrar la decisión de aptitud de la unidad devuelta, identificando al responsable de la decisión y su instante. |
| RF-192 | RF-087 | RF | El sistema deberá presentar al ejecutivo las tres opciones de garantía legal (reparación, reposición y devolución del precio) para que el consumidor elija. |
| RF-193 | RF-088a | RF | El sistema debe registrar la opción de garantía legal ofrecida al consumidor. |
| RF-194 | RF-088b | RF | El sistema debe registrar la opción de garantía legal efectivamente elegida por el consumidor. |
| RF-195 | RF-089 | RF | El sistema deberá permitir parametrizar el plazo de garantía legal por tipo de producto, sin requerir modificacion de código. |
| RF-196 | RF-090 | RF | El sistema deberá registrar el hito de resolución al consumidor con su fecha propia. |
| RF-197 | RF-091 | RF | El sistema deberá registrar el hito de recuperación contra el tercero responsable con una fecha independiente de la resolución al consumidor. |
| RF-198 | RF-092 | RF | El sistema deberá impedir que el estado de la recuperación contra el tercero condicione el cierre de la resolución al consumidor. |
| RF-199 | RF-021 | RF | El sistema deberá exigir la entrega completa de la información precontractual antes de habilitar la evaluación de la solicitud de crédito. |
| RF-200 | RF-022.1 | RF | El sistema deberá registrar la versión del documento precontractual entregado. |
| RF-201 | RF-022.2 | RF | El sistema deberá registrar el instante de entrega de la información precontractual. |
| RF-202 | RF-022.3 | RF | El sistema deberá registrar el instante de aceptación del cliente. |
| RF-203 | RF-022.4 | RF | El sistema deberá registrar el medio por el cual se entrego y se aceptó la información precontractual. |
| RF-204 | RF-022.5 | RF | El sistema deberá registrar el contenido exacto aceptado por el cliente o su huella de integridad verificable. |
| RF-205 | RF-022.6 | RF | El sistema deberá dejar constancia expresa de que el cliente recibió la información antes de aceptar, mediante un mecanismo distinto de la sola firma en papel archivado. |
| RF-206 | RF-022.7 | RF | El sistema deberá impedir el registro de la aceptación del crédito mientras no exista acreditación de entrega previa de la información precontractual completa. |
| RF-207 | RF-023.1 | RF | El sistema deberá registrar la evidencia del consentimiento expreso e informado del cliente mediante un mecanismo verificable de integridad. |
| RF-208 | RF-023.2 | RF | El sistema deberá impedir el registro de una modificacion de condiciones del crédito que no tenga evidencia de consentimiento asociada. |
| RF-209 | RF-023.3 | RF | El sistema deberá reconstruir el acto de consentimiento presentando que se informó, en que versión y que aceptó el cliente. |
| RF-210 | RF-023.4 | RF | El sistema deberá restaurar desde archivo frío los antecedentes de una operación de crédito de cualquier cohorte dentro del plazo de conservación. |
| RF-211 | RF-024Aa | RF | El sistema debe permitir al ejecutivo de cobranza iniciar una gestión de cobranza. |
| RF-212 | RF-024Ab | RF | El sistema debe registrar la gestión de cobranza ejecutada con su medio, su instante y su ejecutor. |
| RF-213 | RF-024Ac | RF | El sistema debe impedir la ejecución de una gestión de cobranza fuera de los límites normativos de horario y de medio de contacto. |
| RF-214 | RF-024Ba | RF | El sistema debe enlazar el expediente de la repactación con la gestión de cobranza que la originó. |
| RF-215 | RF-024Bb | RF | El sistema debe enlazar el expediente de la repactación con la evidencia de consentimiento registrada en RF-207. |
| RF-216 | RF-033 | RF | El sistema deberá generar un reporte de conciliación diaria de saldos durante todo el proceso de migración. |
| RF-217 | RF-036B | RF | El sistema deberá permitir al cliente no autenticado consultar la información precontractual del crédito. |
| RF-218 | RF-036C | RF | El sistema deberá permitir al cliente no autenticado utilizar un simulador de costo total del crédito. |
| RF-219 | RF-093 | RF | El sistema deberá mantener cargada la Tasa Máxima Convencional vigente por tipo y tramo de operación, con su fecha de vigencia. |
| RF-220 | RF-094 | RF | El sistema deberá impedir la originación de una operación cuya tasa supere la Tasa Máxima Convencional vigente a la fecha de la operación. |
| RF-221 | RF-095 | RF | El sistema deberá determinar el cupo exclusivamente a partir de las variables de la evaluación de capacidad de pago documentada. |
| RF-222 | RF-096 | RF | El sistema deberá excluir el monto de la venta en curso del conjunto de variables de asignación de cupo. |
| RF-223 | RF-097 | RF | El sistema deberá excluir la solicitud del vendedor del conjunto de variables de asignación de cupo. |
| RF-224 | RF-098 | RF | El sistema deberá impedir al vendedor alterar el resultado de una evaluación crediticia. |
| RF-225 | RF-099 | RF | El sistema deberá impedir la repetición de la evaluación crediticia del mismo cliente dentro de la ventana de enfriamiento parametrizada. |
| RF-226 | RF-100 | RF | El sistema deberá registrar cada intento de evaluación con la identidad del solicitante y el resultado obtenido. |
| RNF-04 | NFR-01 | RNF | El estado de un pedido no debe presentar discrepancias entre canales de consulta. |
| RNF-05 | NFR-01.2 | RNF | La actualización del estado de un pedido debe reflejarse en todos los puntos de consulta dentro del plazo máximo definido. |
| RNF-06 | NFR-02 | RNF | El tiempo de evaluación de una solicitud de crédito en el punto de venta físico no debe exceder el umbral objetivo. |
| RNF-07 | NFR-21 | RNF | El tiempo total de originación de crédito en el mesón, con información precontractual acreditada, no debe superar el tiempo del proceso actual. |
| RNF-08 | NFR-03.1 | RNF | La migración de la cartera de crédito viva no debe generar pérdida de datos. |
| RNF-09 | NFR-03.2 | RNF | La migración de la cartera de crédito viva no debe interrumpir el servicio de cobro. |
| RNF-10 | NFR-03.3 | RNF | La migración de la cartera de crédito viva no debe producir divergencia de saldos. |
| RNF-11 | NFR-04.1 | RNF | La separación lógica entre los datos del retail y los del negocio financiero debe estar implementada. |
| RNF-12 | NFR-04.2 | RNF | La separación lógica entre ambos ámbitos debe estar documentada. |
| RNF-13 | NFR-04.3 | RNF | La separación lógica entre ambos ámbitos debe ser verificada por auditoría independiente. |
| RNF-14 | NFR-31 | RNF | La separación física entre la infraestructura del retail y la de la filial emisora debe estar implementada y acreditada. |
| RNF-15 | NFR-05 | RNF | Toda acción relevante ejecutada en el sistema debe quedar registrada indicando usuario individual, acción e instante. |
| RNF-16 | NFR-06.1 | RNF | La consulta de disponibilidad en la ficha de producto del canal digital debe responder dentro del umbral definido. |
| RNF-17 | NFR-06.2 | RNF | La confirmación de un pedido durante el evento anual debe completarse dentro del umbral definido. |
| RNF-18 | NFR-06.3 | RNF | La venta completa en caja con medio de pago externo debe completarse dentro del umbral definido. |
| RNF-19 | NFR-06.4 | RNF | La propagación de un cambio de precio a las 380 líneas de caja y al canal digital debe completarse dentro del umbral definido. |
| RNF-20 | NFR-06.5 | RNF | El registro de una devolución en el mesón debe completarse dentro del umbral definido. |
| RNF-21 | NFR-06.6 | RNF | La consulta de disponibilidad desde una terminal compartida del piso de venta debe responder dentro del umbral definido. |
| RNF-22 | NFR-07.1 | RNF | La plataforma debe soportar la concurrencia y el volumen del peak digital del evento anual sin degradar los umbrales de NFR-06.x. |
| RNF-23 | NFR-07.2 | RNF | La plataforma debe soportar la concurrencia y el volumen del peak presencial de la campaña de noviembre y diciembre sin degradar los umbrales de NFR-06.x. |
| RNF-24 | NFR-08.1 | RNF | Una tienda debe poder operar sin enlace externo durante el período mínimo definido. |
| RNF-25 | NFR-08.2 | RNF | El centro de distribución principal debe poder operar sin enlace externo durante el período mínimo definido. |
| RNF-26 | NFR-08.3a | RNF | La sincronización tras la reconexión no debe superar el plazo definido. |
| RNF-27 | NFR-08.3b | RNF | La sincronización tras la reconexión no debe producir pérdida de ventas ni de documentos. |
| RNF-28 | NFR-08.4 | RNF | La operación desconectada autónoma on-premise debe sostenerse durante el período mínimo exigido por las bases técnicas. |
| RNF-29 | NFR-09.1 | RNF | La operación de tiendas y centros de distribución debe estar disponible en la ventana horaria definida. |
| RNF-30 | NFR-09.2a | RNF | El canal digital debe estar disponible de forma continua. |
| RNF-31 | NFR-09.2b | RNF | Los servicios financieros que afectan pagos, estados de cuenta y bloqueo de tarjetas deben estar disponibles de forma continua. |
| RNF-32 | NFR-09.3 | RNF | La solución debe cumplir los objetivos de recuperación ante desastre exigidos. |
| RNF-33 | NFR-10.1 | RNF | Los datos de identificación de clientes, la cartera de crédito, el comportamiento de pago y los antecedentes de evaluación crediticia deben cifrarse a nivel de campo. |
| RNF-34 | NFR-10.2 | RNF | Los datos de medios de pago no deben almacenarse en claro, sino tokenizarse. |
| RNF-35 | NFR-11.1 | RNF | La red de cajas, la administrativa, la de videovigilancia y la inalámbrica de clientes deben estar segmentadas en las 22 tiendas. |
| RNF-36 | NFR-11.2 | RNF | La red y el ámbito de sistemas de la filial emisora deben estar separados de forma acreditada respecto del retail. |
| RNF-37 | NFR-12 | RNF | Debe existir segregación de funciones verificable entre originación, aprobación, modificacion de condiciones y cobranza. |
| RNF-38 | NFR-13 | RNF | Debe registrarse todo acceso a la cartera de crédito, al comportamiento de pago y a los antecedentes de evaluación crediticia. |
| RNF-39 | NFR-14.1 | RNF | Los actos de crédito de apertura de tarjeta y de repactación deben contar con un mecanismo de consentimiento de integridad verificable. |
| RNF-40 | NFR-14.2 | RNF | La conformidad de recepción de mercadería y la constancia de devolución deben contar con un mecanismo de consentimiento de integridad verificable. |
| RNF-41 | NFR-15.1 | RNF | Los documentos tributarios y antecedentes de venta deben conservarse por el plazo definido. |
| RNF-42 | NFR-15.2 | RNF | Los antecedentes del crédito deben conservarse por el plazo del crédito más el período posterior exigido. |
| RNF-43 | NFR-15.3 | RNF | La evidencia de consentimiento de originación y repactación debe conservarse por el mismo plazo que el crédito. |
| RNF-44 | NFR-15.4 | RNF | La trazabilidad del precio publicado debe conservarse por el plazo definido. |
| RNF-45 | NFR-15.5 | RNF | Los movimientos de inventario y conteos cíclicos deben conservarse por el plazo definido. |
| RNF-46 | NFR-15.6 | RNF | Los datos de fidelización deben conservarse por el plazo definido. |
| RNF-47 | NFR-15.7 | RNF | Los registros de videovigilancia deben conservarse por el plazo definido. |
| RNF-48 | NFR-16 | RNF | La solución debe admitir la apertura de una tienda nueva por parametrización, sin desarrollo a medida. |
| RNF-49 | NFR-17 | RNF | Las interfaces de sala, caja y mesón financiero deben ser operables por personal recién incorporado con capacitación mínima. |
| RNF-50 | NFR-18 | RNF | Toda comunicación relativa al crédito debe cumplir criterios verificables de lenguaje claro, validados con personas usuarias reales. |
| RNF-51 | NFR-19 | RNF | Las notificaciones definidas funcionalmente deben emitirse y registrarse en el 100% de los eventos que las gatillan. |
| RNF-52 | NFR-20.1 | RNF | La solución debe adoptar un estándar identificado y justificado para el catálogo e identificación de producto. |
| RNF-53 | NFR-20.2 | RNF | La solución debe adoptar un estándar identificado y justificado para el intercambio de órdenes y avisos de despacho con los proveedores. |
| RNF-54 | NFR-20.3 | RNF | La solución debe adoptar un estándar identificado y justificado para el intercambio con los transportistas de última milla. |
| RNF-55 | NFR-20.4 | RNF | La solución debe adoptar un estándar identificado y justificado para la sincronización de catálogo, existencia y pedido con los vendedores de marketplace. |
| RNF-56 | NFR-20.5 | RNF | La solución debe adoptar el formato normativo vigente de documento tributario electrónico. |
| RNF-57 | NFR-22 | RNF | La evidencia completa de consentimiento de una operación arbitraria debe recuperarse dentro del plazo objetivo, a diez años. |
| RNF-58 | NFR-23 | RNF | La recuperación del precio publicado de una referencia en una fecha, hora y canal arbitrarios debe completarse dentro del plazo objetivo. |
| RNF-59 | NFR-24 | RNF | La revocación total de accesos de un trabajador debe completarse dentro del plazo máximo de la política interna. |
| RNF-60 | NFR-25 | RNF | El traspaso de sesión nominativa en una terminal compartida debe completarse dentro del plazo objetivo. |
| RNF-61 | NFR-26 | RNF | La tasa de cancelación de pedidos por falta de existencia no debe superar el umbral comprometido. |
| RNF-62 | NFR-27 | RNF | El cumplimiento de la promesa de entrega publicada debe alcanzar el umbral comprometido, medido por pedido. |
| RNF-63 | NFR-28 | RNF | La diferencia de inventario por categoría debe reducirse al umbral comprometido. |
| RNF-64 | NFR-29a | RNF | El tiempo entre la detección de un quiebre y el aviso al cliente no debe superar el objetivo declarado. |
| RNF-65 | NFR-29b | RNF | No debe mantenerse un cobro capturado sobre un pedido declarado no cumplible. |
| RNF-66 | NFR-30a | RNF | La latencia entre la recepción física de una devolución en tienda y la notificación al vendedor de marketplace no debe superar el objetivo declarado. |
| RNF-67 | NFR-30b | RNF | No debe permanecer mercadería de marketplace en bodega sin aviso a su propietario. |
| RNF-68 | NFR-32 | RNF | La restauración desde archivo frío de una operación de crédito de la cohorte más antigua debe completarse dentro del plazo objetivo. |
| RNF-69 | NFR-33 | RNF | La atención de garantía legal en mesón no debe derivar al consumidor a un tercero como condición de atención, en ninguna tienda. |
| RNF-70 | NFR-34.1 | RNF | El ciclo de desarrollo debe producir un inventario de componentes (SBOM) por artefacto desplegado. |
| RNF-71 | NFR-34.2 | RNF | La cadena de suministro de software debe alcanzar el nivel SLSA 3 o superior. |
| RNF-72 | NFR-34.3 | RNF | La capa expuesta debe cumplir el estándar OWASP ASVS en el nivel comprometido. |
| RNF-73 | NFR-34.4 | RNF | La arquitectura debe implementar un modelo Zero Trust conforme a NIST SP 800-207. |
| RNF-74 | NFR-35.1 | RNF | Todo tratamiento de datos personales debe declarar su finalidad. |
| RNF-75 | NFR-35.2 | RNF | Todo tratamiento de datos personales debe invocar una de las bases de licitud de la Ley N° 21.719. |
| RNF-76 | NFR-35.3 | RNF | La compañía debe mantener el registro de actividades de tratamiento de datos personales. |

## 7_Depuracion_Alcance

<!-- hoja: 7_Depuracion_Alcance | filas de datos: 36 -->

| ID | Acción propuesta | Enunciado vigente | Motivo de la revisión | Fundamento en el alcance (Cap. III) | Decisión del equipo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| RF-025 | ELIMINAR | El sistema deberá propagar el cambio de precio a cada etiqueta electrónica de la referencia afectada. | Presupone que existe una etiqueta electrónica instalada a la cual propagar el cambio de precio. La solución adoptada en SUP-09 propaga hacia la línea de caja y condiciona la activación al escaneo manual del recambio físico. | X-02 excluye la adquisición e instalación de etiquetas electrónicas; el diseño compensatorio declarado es la retención del precio anterior en el punto de venta hasta el escaneo manual. |  |
| RF-026 | ELIMINAR | El sistema deberá detectar la no confirmación del cambio de precio por parte de una etiqueta electrónica. | Detecta la no confirmación de una etiqueta electrónica que la solución no instala. Su función equivalente sobre etiqueta de papel ya está cubierta por el tablero de desactualización del módulo M-06. | X-02. |  |
| RF-027 | ELIMINAR | El sistema debe generar una alerta operativa al jefe de tienda identificando la etiqueta electrónica no confirmada. | Alerta al jefe de tienda sobre una etiqueta electrónica no confirmada. Misma observación anterior: el objeto de la alerta no existe en el alcance contratado. | X-02. |  |
| RF-031 | ELIMINAR | El sistema deberá excluir los puntos con etiqueta electrónica de la ventana de agrupamiento definida en RF-030. | Excluye del agrupamiento de rutas los puntos con etiqueta electrónica. Sin etiquetas electrónicas en el alcance, la excepción carece de universo de aplicación. | X-02. |  |
| RNF-01 | ELIMINAR | La alerta de etiqueta electrónica no confirmada debe emitirse antes de la apertura de sala. | Fija el umbral temporal de emisión de la alerta de la RF-027. Se elimina por arrastre al eliminarse el requerimiento funcional del que fue extraído. | X-02. |  |
| OP-01 | TRASLADAR | El PROPONENTE debe especificar la alternativa de etiquetas electrónicas frente a las demás opciones de resolución de la discrepancia de precio. | Obligación de la Oferta Técnica, no función del sistema. No admite caso de prueba de software ni entra en la Estructura de Desglose del Trabajo como paquete de desarrollo. | X-02. Corresponde al Subdocumento de evaluación de alternativas y al Entregable 2 de la Oferta Económica. |  |
| OP-02 | TRASLADAR | El PROPONENTE debe costear la alternativa de etiquetas electrónicas sin asumir su adquisición dentro del alcance. | Idéntica naturaleza: costeo de la alternativa, verificable documentalmente. | X-02. |  |
| OP-03 | TRASLADAR | El PROPONENTE debe especificar la cobertura de despliegue de las etiquetas electrónicas. | Especificación de cobertura de despliegue de etiquetas electrónicas. | X-02. |  |
| OP-04 | TRASLADAR | El PROPONENTE debe especificar el hardware requerido por la alternativa de etiquetas electrónicas. | Especificación de hardware de la alternativa de etiquetas electrónicas. | X-02 y X-09. |  |
| OP-05 | TRASLADAR | El PROPONENTE debe presentar el costo de la alternativa separadamente del resto de la solución. | Presentación del costo de la alternativa separado del resto de la solución. | X-02. |  |
| OP-06 | TRASLADAR | El PROPONENTE debe especificar la cantidad de dispositivos móviles requeridos por tienda y por departamento. | Especificación de cantidad de dispositivos móviles por tienda y departamento. | X-03 y X-09: el hardware lo adquiere el CLIENTE conforme a especificación del PROPONENTE. |  |
| OP-07 | TRASLADAR | El PROPONENTE debe especificar las características técnicas de los dispositivos móviles requeridos. | Especificación de características técnicas de los dispositivos móviles. | X-03 y X-09. |  |
| OP-08 | TRASLADAR | El PROPONENTE debe presentar el análisis de hacer o comprar del centro de distribución de Concepción con sus tres alternativas. | Análisis de hacer o comprar del centro de distribución de Concepción. | X-11. Corresponde al Subdocumento de adquisiciones (PMBOK 6.ª ed., §12.1.3.5). |  |
| OP-09 | TRASLADAR | El PROPONENTE debe declarar el impacto de la alternativa seleccionada sobre el cumplimiento de RN-15. | Declaración del impacto de la alternativa seleccionada sobre la promesa de entrega del sur. | X-11. |  |
| RF-071 | CONSOLIDAR | El sistema deberá calcular la base de comisión considerando el canal de origen y el canal de cumplimiento cuando estos difieran. | Calcula la base de comisión considerando canal de origen y canal de cumplimiento. La RF-054 ya calcula la base reconociendo al vendedor y a la tienda de origen con independencia del canal de despacho: el universo cubierto es el mismo enunciado con otras palabras. | Módulo M-10. Se consolida en RF-054 y RF-055, conservando el enunciado más específico. |  |
| RNF-61 | RECLASIFICAR | La tasa de cancelación de pedidos por falta de existencia no debe superar el umbral comprometido. | Expresa una meta de resultado comercial (tasa de cancelación), no un atributo de calidad del software. Su cumplimiento depende también de la ejecución operativa del CLIENTE. | Numeral 3.5.3: indicador compartido. Corresponde al objetivo OE-02 y a los criterios de aceptación, no al catálogo de requerimientos no funcionales. |  |
| RNF-62 | RECLASIFICAR | El cumplimiento de la promesa de entrega publicada debe alcanzar el umbral comprometido, medido por pedido. | Meta de cumplimiento de promesa de entrega, sujeta a la ejecución de la preparación de pedidos por parte del CLIENTE. | Numeral 3.5.3: indicador compartido. Corresponde al objetivo OE-06. |  |
| RNF-63 | RECLASIFICAR | La diferencia de inventario por categoría debe reducirse al umbral comprometido. | Meta de exactitud de inventario, sujeta a la ejecución del conteo por parte del personal de sala. | Numeral 3.5.3: indicador compartido. Corresponde al objetivo OE-01. |  |
| RF-153 | REVISAR | El sistema deberá permitir al vendedor de piso registrar las unidades que ingresan al probador. | Registro de unidades que ingresan al probador. Deriva del vacío V-02, que la introducción del numeral 3.2 anuncia pero cuya sección 3.2.7 no fue incorporada al documento. | Sin fundamento visible en el alcance vigente. Se mantiene si se repone V-02; se elimina si el vacío se descarta. |  |
| RF-154 | REVISAR | El sistema deberá excluir del disponible para vender las unidades registradas en probador. | Exclusión del disponible de las unidades en probador. Mismo origen. | Sin fundamento visible en el alcance vigente. |  |
| RF-155 | REVISAR | El sistema debe permitir al vendedor de piso confirmar el reingreso a sala de la unidad registrada en probador. | Confirmación de reingreso a sala de la unidad del probador. Mismo origen. | Sin fundamento visible en el alcance vigente. |  |
| RF-156 | REVISAR | El sistema debe permitir al vendedor de piso registrar la venta de la unidad registrada en probador. | Registro de la venta de la unidad del probador. Mismo origen. | Sin fundamento visible en el alcance vigente. |  |
| RNF-46 | REVISAR | Los datos de fidelización deben conservarse por el plazo definido. | Fija el plazo de conservación de los datos de fidelización. Ningún módulo del numeral 3.3 declara responsabilidad sobre fidelización, y el sistema de 2017 no aparece en la asignación por etapa del numeral 3.6.3. | Requerimiento huérfano: sin módulo dueño ni asignación de etapa. Debe asignarse a un módulo o eliminarse. |  |
| RF-170 | REVISAR | El sistema deberá excluir del catálogo de atributos disponibles en el motor de campañas todo atributo de origen financiero (mora, deuda, cupo utilizado, comportamiento de pago). | Requerimiento asociado a campañas comerciales. Verificar que el motor de campañas quede efectivamente asignado a un módulo, dado que el numeral 3.3 no lo declara de forma explícita. | Verificar cobertura modular antes de conservar. |  |
| RF-089 | CONDICIONAR | El sistema deberá permitir el otorgamiento de crédito en modo desconectado exclusivamente contra cupo preaprobado vigente almacenado en caché local. | Otorgamiento de crédito desconectado contra cupo preaprobado. En la Etapa 1 depende de que la plataforma de originación de 2011 admita exponer el cupo hacia el nodo local, extremo no verificado. | Supuesto S-C. Conservar con marca de dependencia; su alcance de Etapa 1 cae si la prueba de concepto resulta negativa. |  |
| RF-090 | CONDICIONAR | El sistema deberá aplicar el tope de monto parametrizado a cada operación de crédito cursada en modo desconectado. | Tope de monto por operación en modo desconectado. Misma dependencia. | Supuesto S-C. |  |
| RF-091 | CONDICIONAR | El sistema deberá aplicar el tope parametrizado de número de operaciones de crédito en modo desconectado. | Tope de número de operaciones consecutivas en modo desconectado. Misma dependencia. | Supuesto S-C. |  |
| RF-094 | CONDICIONAR | El sistema deberá marcar la operación como cursada en modo desconectado para su validación posterior. | Marca de operación cursada en contingencia para validación posterior. Misma dependencia. | Supuesto S-C. |  |
| Cómo leer esta hoja |  |  |  |  |  |
| ELIMINAR |  | El requerimiento presupone un componente que el alcance excluye de forma explícita. Mantenerlo compromete al ADJUDICATARIO con una función que no puede construir. |  |  |  |
| TRASLADAR |  | El enunciado es válido pero no es una función del sistema: es una obligación de la Oferta. Sale del catálogo de requerimientos y se documenta en el subdocumento que corresponda. |  |  |  |
| CONSOLIDAR |  | Dos requerimientos cubren el mismo universo con enunciados distintos. Se conserva el más específico. |  |  |  |
| RECLASIFICAR |  | El enunciado es una meta de resultado de negocio y no un atributo de calidad verificable contra el sistema. Migra a objetivos y criterios de aceptación. |  |  |  |
| CONDICIONAR |  | Se conserva, con marca de dependencia sobre un supuesto todavía no verificado. Si la validación falla, el alcance de ese requerimiento cambia de etapa. |  |  |  |
| REVISAR |  | El fundamento que lo justificaba no aparece en la versión vigente del Capítulo III. Requiere decisión del equipo antes de conservarlo o eliminarlo. |  |  |  |
| Efecto sobre el conteo |  | Si se aprueban todas las acciones propuestas, el catálogo pasa de 311 a 302 filas: 5 eliminaciones por tecnología excluida, 9 traslados a la Oferta, 1 consolidación y 3 reclasificaciones, sin contar las 6 filas en revisión. |  |  |  |

