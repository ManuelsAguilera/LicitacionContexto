# Borrador de §7.3.3 con el análisis del paso D (2026-11-10)

Documento de trabajo, no entregable. Texto para insertar en el `.tex` del SD-07 en el paso T. Base del análisis: `compresion-2026-11-10/README.md` y `red-v3-2026-11-10/`. La numeración de tablas y figuras es provisional.

**Qué se conserva del texto de noviembre:** los párrafos del método (rendimientos de 7,5 / 6,8 / 5,1 HH, PERT y CPM), la Tabla 7.7 (la red v3 da las mismas holguras de hitos), el párrafo de las cadenas de holgura cero, la revisión de expedientes y el control semanal del Jefe de Proyecto.

**Qué se reemplaza:**
1. El párrafo que empieza «Las medidas de recuperación priorizarán…» y termina en «…asignaciones de capacidad del T-15». Lo reemplaza la nueva §7.3.3.2.
2. El párrafo y la figura de la distribución mensual de HH (234.493,47 HH). Se reemplazan por el párrafo de abajo, con la curva regenerada desde la red v3.
3. Se agrega la subsección §7.3.3.2, después de §7.3.3.1.

---

## Reemplazo del párrafo de la curva mensual de HH

La distribución mensual de las horas de trabajo y de la dotación suma 239.250,01 HH. La implementación alcanza su mayor carga en M16, cuando se concentra el acompañamiento simultáneo de las veintidós tiendas. Durante M21–M56, el equipo de operación aporta 4.160 HH mensuales, a las que se suman el cierre y los trabajos transversales del período. El desglose por perfil y por mes está en el Formulario T-15.

*(La figura de la curva se regenera desde la red v3 en el paso T, con el mismo formato que las Figuras 7.17 a 7.19.)*

---

## §7.3.3.2 Escenarios de atraso y respuestas de compresión

**Texto de caída**

Los hitos sin holgura dependen de ventanas de duración fija, como las marchas blancas y la habilitación de las tiendas, que no se pueden acortar. Por eso el análisis se hizo sobre el trabajo que llega a esas ventanas. Se agruparon las actividades con 10 días hábiles de margen o menos y se eligieron siete frentes, más una variante en las innovaciones de la Etapa 2. En cada uno se atrasó 10 días hábiles la actividad que lo dispara (14 días corridos cuando el atraso es de un proveedor) y se recalculó la programación estabilizada con la misma red del cronograma.

Se probaron dos respuestas. La intensificación agrega personas, como máximo el doble de las asignadas, y suma un 15 % de horas sobre lo comprimido por coordinación y aprendizaje. La ejecución rápida adelanta una actividad para que empiece cuando su predecesora va a la mitad. Solo se aplica a dependencias discrecionales y suma un 10 % de horas por retrabajo en la actividad adelantada. Cuando ninguna alcanza, se agregan horas extraordinarias de hasta dos horas diarias con el recargo legal del 50 %. La Tabla 7.9 resume el resultado.

**Tabla 7.9: Efecto de un atraso de 10 días hábiles y respuesta que recupera la fecha.**

| Escenario | Efecto sin respuesta | Respuesta | HH adicionales | Riesgo que agrega |
| :-- | :-- | :-- | --: | :-- |
| Levantamiento de procesos (1.2.2) | Expediente de H1 incompleto; 1.2.2 y 1.2.3 terminan 13 días tarde | Intensificación | 137 | Integrar analistas nuevos en el primer mes |
| Nube base (1.4.1) | Ambientes 10 días tarde; H3 en riesgo | Intensificación | 93 | Bajo |
| Construcción de la Etapa 1 (1.5.36) | Lo absorbe el margen | No requiere | 0 | — |
| Entrega de UPS del lote 1 | Prueba de corte del piloto 9 días fuera de M6–M7 | Ejecución rápida de la pila local | 29 | Retrabajo si cambia la instalación |
| Corte de inventario (1.7.3) | Lo absorbe el margen | No requiere | 0 | — |
| Construcción de la Etapa 2 (1.5.22) | Lo absorbe el margen | No requiere | 0 | — |
| Pruebas de Retail Media (1.10.4.6) | H10, H11 y H12 se atrasan 6 días | Intensificación | 30 | Bajo |
| Capacitación de la Etapa 2 (1.13.3) | H11, H12 y el inicio de la operación se atrasan 11 días | Intensificación y horas extraordinarias | 202 | Doble de formadores y fatiga |

Fuente: elaboración propia a partir de la red del cronograma.

**Qué se concluye**

Tres de los ocho atrasos se absorben con el margen de la programación. En los frentes de construcción probados, de la Etapa 1 y de la Etapa 2, un atraso de dos semanas no llega a ningún hito. Los otros cinco tienen una respuesta que recupera la fecha, y la respuesta depende del tipo de atraso. Cuando el trabajo es propio, se intensifica. Cuando el atraso viene de un proveedor, la intensificación no sirve, porque no acelera una entrega, y se usa la ejecución rápida. En la nube base pasa lo contrario. La ejecución rápida no es posible, porque los ambientes requieren la red ya creada, y la única respuesta es intensificar.

La capacitación de la Etapa 2 es el frente más sensible, porque su atraso mueve el inicio de la operación. En la planificación inicial ocupaba 36 personas durante 9 días, entre la entrega del software para pruebas (H9) y el comienzo de la marcha blanca, sin holgura. Para reducir ese riesgo se adelantó a M17 el 30 % de la capacitación, 576 HH que no dependen del software terminado. Esa parte cubre los procesos y reglas de la Etapa 2, los cambios de rol, los módulos compartidos con la Etapa 1 y la formación de formadores, y se apoya en el diseño aprobado en H8. El 70 % restante se dicta desde H9 sobre el software con pruebas superadas. Con este cambio, la capacitación sobre el software gana 3 días de holgura, un atraso de 10 días baja de 14 a 11 días de efecto sobre H11 y H12, y los formadores preparados en M17 quedan disponibles para duplicar la dotación si hace falta. La medida no agrega horas, solo cambia su fecha.

Las respuestas suman 491 HH, más el equivalente a unas 134 HH por el recargo de las horas extraordinarias. Se financian con la reserva de contingencia de 3.688 HH, que se administra por riesgo y se mantiene separada de la holgura temporal y de las asignaciones de capacidad del T-15. El Jefe de Proyecto activa la respuesta cuando el control semanal muestra que el atraso de una actividad supera su margen restante, y registra contra qué riesgo se imputan las horas.

---

## Pendientes para el paso T (no van en el texto final)

1. Cruzar los cinco escenarios con respuesta contra los catorce riesgos del SD-08 que respaldan la contingencia, para que cada imputación tenga su riesgo.
2. Regenerar la figura de la curva mensual de HH desde la red v3.
3. Confirmar la numeración de la Tabla 7.9 al insertar.
