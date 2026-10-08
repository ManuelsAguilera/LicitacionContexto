# Fundamentación del crédito sin conexión (borrador por aprobar)

> **Códigos actualizados (2026-10-08)** a la nomenclatura de `divisiones_negocio_servicios_sd-03.md`.

Documento de contexto, no es entregable. Responde a la decisión pendiente del Caso 09, numeral 16.1 n.º 7, a RT-03.10 y a RT-03.13, y cierra DEC-12 de `auditoria_decisiones.md`. Estado: aprobado por el usuario el 2026-10-06 (opción B2 y topes del Emisor). Aplicado en EXC-16, SP-03, RC-11, 1.10 y la compuerta del POS (condición 9).

## 1. Qué hay que resolver

- **Caso 16.1 n.º 7:** "qué ocurre en caja cuando no hay enlace y hay que decidir si se otorga crédito contra un cupo preaprobado en caché, con qué límite y con qué riesgo asumido". Razón que da el Caso: la restricción 5 exige seguir vendiendo y el crédito es el 38 % de la venta de tiendas.
- **Transversales RT-03.10:** autonomía mínima de 24 h; RT-03.11 registro local sin pérdida; RT-03.12 reconciliación determinista con bitácora; **RT-03.13** declarar qué funciones no estarán disponibles y qué procedimiento manual las suple ("la ausencia de esta declaración se evaluará como observación grave").
- El Caso cap. 15 (RT-03.10) dice que el comportamiento del crédito sin conexión "debe resolverse y fundamentarse, no omitirse".

## 2. Dos situaciones distintas

| | A. Apertura de tarjeta o ampliación de cupo | B. Compra con un cupo ya aprobado |
| :-- | :-- | :-- |
| Qué ocurre | Se identifica al cliente, se evalúa su capacidad de pago, se asigna cupo, se entrega la información precontractual y se obtiene la aceptación (Caso 4.10) | El cliente paga con su tarjeta propia dentro del cupo que ya tiene |
| Volumen | ≈ 520.000 evaluaciones al año entre aperturas y ampliaciones (Caso cap. 15); promedio aproximado de 65 por tienda al día (520.000 / 22 / 365, cálculo del asistente) | La tarjeta propia participa en el 38 % de las ventas de tiendas |

La decisión es distinta para cada una.

## 3. Situación A: no se otorga crédito nuevo sin conexión (EXC-16)

Fundamento, con las fuentes del Caso:
1. **Restricción 3:** la información precontractual debe entregarse antes de la aceptación y su entrega debe quedar acreditada de forma estructurada; "ningún requisito de rapidez comercial puede omitirla ni posponerla".
2. **RT-16.14:** firma electrónica exigible en la apertura de la tarjeta y en la aceptación de la información precontractual.
3. **Caso cap. 12:** prevención de lavado de activos aplica "a la originación en el punto de venta" (conocimiento del cliente y conservación de antecedentes), y la evaluación de capacidad de pago depende de datos del Emisor que no están en la tienda (restricción 1, separación de datos).
4. Una ampliación de cupo sin evaluación sería otorgar crédito sin evaluar la capacidad de pago.

Alternativa descartada: capturar la solicitud sin conexión y evaluar después. Obligaría a aceptar sin información acreditada o a posponerla, que la restricción 3 prohíbe.

Procedimiento manual: el vendedor ofrece otro medio de pago; la apertura o ampliación se retoma al restablecerse el enlace.

## 4. Situación B: compra con cupo aprobado

### Opciones comparadas

| Criterio | B1. No autorizar crédito sin conexión | B2. Cupo preaprobado en caché con topes (recomendada) | B3. Un límite fijo bajo para toda la cartera |
| :-- | :-- | :-- | :-- |
| Restricción 5 (seguir vendiendo y cobrando) | Se cobra con otros medios, pero se pierde la venta con tarjeta propia (38 % de la venta de tiendas) durante el corte | Cumple | Cumple |
| Restricción 1 (separación de datos) | Cumple | Cumple solo si el caché guarda el mínimo (ver 5) | Cumple, y sin datos del cliente |
| Exposición al riesgo de crédito | Ninguna | Acotada por los topes | Mayor: autoriza a clientes sin considerar su cupo ni su estado |
| Evidencia (restricción 2 y 3) | No aplica | Registro local de la aceptación, sincronizado con F:C-03 | Ídem |
| Complejidad | Baja | Media | Baja |

Recomendación: **B2**, sujeta a la prueba de factibilidad de la sección 7 y a que el Emisor fije los topes (sección 6). Si la prueba falla o los topes no se fijan, rige B1 y la función se declara no disponible (sección 9). Esto es lo que ya decía F:C-01: "contingencia con cupo ya aprobado sujeta a prueba de factibilidad".

## 5. Qué guarda el caché (mínimo necesario)

Por tarjeta: identificador opaco, monto máximo autorizado sin conexión (el menor entre el cupo disponible y el tope por cliente), antigüedad del dato y estado de bloqueo. **No guarda** saldo, mora ni comportamiento de pago. Se alimenta periódicamente desde F:C-01 a través de X-01, con el dato mínimo (Caso 16.1 n.º 4; restricción 1). Así el caché no cruza la frontera entre Retail y Emisor.

Exposición máxima: por cada cliente, el tope sin conexión multiplicado por el número de tiendas que visite durante el corte, porque las tiendas no pueden coordinarse sin enlace. Por eso el tope por cliente y el tope por transacción los fija el Emisor.

## 6. Parámetros que decide el Emisor, no el proponente

El apetito de riesgo de crédito es de la filial emisora fiscalizada. El proponente propone el mecanismo y mide el efecto; el Emisor fija:
- tope por transacción sin conexión;
- tope acumulado por cliente en modo desconectado;
- antigüedad máxima del caché antes de dejar de autorizar;
- criterios de exclusión (clientes en mora, bloqueados o con alerta de prevención de lavado).

Se agrega como responsabilidad del cliente (RC-11).

## 7. Prueba de factibilidad

Se ejecuta en las tiendas piloto del POS, con el corte provocado de 24 h (condición 5 de la compuerta, `asignacion_etapas.md` D2). Pasa si se cumple todo:
1. Las compras con cupo del caché se autorizan dentro de los topes fijados por el Emisor, sin pérdida de transacciones.
2. El 100 % de las compras sin conexión queda con aceptación y versión del texto informado recuperables en F:C-03 tras la sincronización.
3. La conciliación al reconectar (R:V-02, F:C-01, F:C-02) termina en 30 minutos o menos y sin diferencias no explicadas.
4. Los sobrecupos que resulten se registran como excedente y los gestiona F:C-02; la venta ya hecha no se anula.

Regla de reconciliación (RT-03.12): orden por hora local y dispositivo, regla documentada y bitácora auditable.

## 8. Punto por verificar

Si cada compra a cuotas con un cupo vigente exige o no nueva información precontractual, depende de la normativa del emisor (Caso cap. 12, protección del consumidor financiero). El Caso no lo dice. Si la exige, la información se muestra en la pantalla antes de la aceptación y se registra localmente con su versión. Se declara como supuesto con "Si no se cumple".

## 9. Declaración RT-03.13 (funciones del crédito)

| Función | Estado sin conexión | Procedimiento manual |
| :-- | :-- | :-- |
| Apertura de tarjeta y ampliación de cupo | No disponible | Otro medio de pago; retomar al reconectar |
| Compra con tarjeta propia dentro del cupo | Disponible con topes, si la prueba pasa; si no, no disponible | Otro medio de pago |
| Repactación o modificación de condiciones | No disponible (exige consentimiento acreditable, restricción 2) | Se agenda al reconectar |
| Consulta de saldo y estado de cuenta | No disponible (son datos del Emisor, restricción 1) | Se informa al reconectar |
| Pago de cuota en caja | Por definir en el diseño | Por definir |
| Devolución con reverso a la tarjeta propia | Por definir en el diseño | Por definir |

Las demás funciones de la tienda (promociones, emisión de documentos, consulta de existencia local) se declaran en el sd-04 (T-12, ítem 4); la emisión de documentos con el ERP como único emisor tributario queda como punto de diseño.

## 10. Si no se cumple

- Si el Emisor no fija los topes o la prueba falla: la compra con tarjeta propia sin conexión no está disponible y se declara en RT-03.13.
- Si la normativa exige acreditar información adicional por cada compra a cuotas y no se puede registrar sin conexión: se limita a las compras de contado diferido que no la exijan, o rige B1.
- Si el Emisor decide ampliar la contingencia a nuevas aperturas: entra por solicitud de cambio (art. 72), con evaluación de normativa y de impacto.

## 11. Cambios aplicados

- EXC-16: reescribir con las fuentes de la sección 3 y la remisión a este documento.
- 1.10 (F:C-01): criterio de aceptación con la prueba de factibilidad.
- Compuerta del POS (1.16): agregar la condición 9, "prueba de factibilidad del crédito sin conexión".
- RC-11: fijar los topes y el apetito de riesgo del crédito sin conexión.
- Nuevo supuesto SP-03 (sección 8) con "Si no se cumple".
- `auditoria_decisiones.md`: DEC-12 de 5 a 8.
