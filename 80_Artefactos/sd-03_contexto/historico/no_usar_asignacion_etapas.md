> **ARCHIVADO (2026-10-08). No usar como fuente.** Material de trabajo superado por `sd-03.tex`, los Anexos A a D y `ficha_alcance_sd-03.md`. Usa códigos y decisiones antiguas. Se conserva solo por trazabilidad.

# Asignación de entregables a Etapa 1 y Etapa 2 (borrador de trabajo del sd-03)

> **Nomenclatura (2026-10-07):** los nombres y códigos de los servicios de este documento (R-01 a X-01) fueron reemplazados. Rige `divisiones_negocio_servicios_sd-03.md`, que contiene la tabla de equivalencias.

Documento de contexto, no es entregable. Alimenta 3.2.2 y 3.3. Método: seis rondas (A a F); en cada una, sugerencia del asistente, decisión del usuario y justificación por criterio. Criterios en orden: (1) Bases, (2) dependencias técnicas, (3) riesgo e hitos externos, (4) capacidad de absorción del cliente, (5) prioridad del comité. No se redacta riesgo en este documento.

Estado: Rondas A a F cerradas. Falta volcar la asignación a `entregables_alcance.md`, `enunciado_alcance.md` y `plan_3.2.md`.

## Ronda A. Lo que fijan las Bases (cerrada)

Base: Bases Administrativas art. 15 (Etapa 1 = plataforma completa más funcionalidad de primera prioridad; Etapa 2 = segundo alcance funcional sobre esa plataforma, sin rehacer arquitectura) y art. 17 (meses).

### Decisión A1. Integración crítica

Definición aprobada: integración cuya falla rompe una de las promesas del Caso (precio cobrado igual al exhibido, disponibilidad correcta, venta con documento tributario, separación Retail–Emisor). Lista, todas en Etapa 1:

| Integración crítica | Promesa que sostiene |
| :-- | :-- |
| POS con servicio de precios (R-01) | Precio cobrado igual al exhibido |
| POS con ventas y documento tributario (R-05) | Venta con documento tributario |
| WMS con inventario (R-03) | Disponibilidad correcta |
| E-commerce con inventario (R-03) | Disponibilidad correcta (hoy publica disponibilidad errónea) |
| Plataforma financiera con F-01, F-02, F-03 y X-01 | Separación Retail–Emisor |
| ERP/DTE (conexión propia) | Único emisor tributario (Caso cap. 10 n.º 6) |

### Decisión A2. Primera prioridad

Definición inicial aprobada: lo que sostiene existencia y precio, la frontera de datos Retail–Emisor y el inicio de la migración financiera.

**Derivación desde el Caso (2026-10-06, auditoría DEC-36).** El art. 15 dice que la primera prioridad está "definida en las Bases Técnicas del caso", pero el Caso no la define en un solo lugar: la entrega en el 13.1 (preferencia del comité y dos objeciones registradas), el 13.2 (hitos externos), el 13.3 (condiciones de puesta en producción) y las restricciones del cap. 10. El mismo 13.1 aclara que el orden del comité "es una preferencia, no una definición de alcance"; por eso se usa como una de cuatro entradas y no como la respuesta.

Un servicio o entregable es de **primera prioridad** si cumple al menos uno de estos criterios:

| Criterio | Fuente en el Caso |
| :-- | :-- |
| P1. Sostiene una de las dos prioridades del comité: exactitud del inventario y disponibilidad publicada, o precio y su trazabilidad | 13.1; el episodio de junio (2.840 cancelaciones) y el procedimiento abierto (13.2); la fiscalización de febrero (11 % de discrepancia de precio); restricción 4 |
| P2. Es condición de una de las dos objeciones registradas: la frontera de datos Retail–Emisor antes de cualquier vista unificada, o la migración de la cartera de 620.000 clientes antes de 2029 | 13.1; 13.2; 13.3.5 y 13.3.7; restricciones 1 y 8; 17.3 exige hacerse cargo de ambas |
| P3. Es necesario para que la Etapa 1 sea el sistema de registro oficial desde el mes 16: plataforma híbrida completa, seguridad, observabilidad e integraciones críticas, y las restricciones no negociables de operación (la tienda vende sin enlace; el ERP sigue como único emisor tributario) | Bases Admin. art. 15; restricciones 5 y 6 |
| P4. Es dependencia técnica de algo que cumple P1, P2 o P3 | Ronda B |

Lo que no cumple ninguno queda como segundo alcance funcional (Etapa 2).

Aplicación a los servicios:

| Servicio o componente | Criterio | Etapa |
| :-- | :-- | :-- |
| Plataforma de integración, identidad, observabilidad, infraestructura híbrida, mapa de las 14 integraciones | P3 | 1 |
| R-01 Catálogo, precios y promociones | P1 (precio) y P4 | 1 |
| R-03 Inventario, reservas y disponibilidad | P1 (existencia) | 1 |
| R-05 Registro y conciliación de ventas | P3 (venta con documento tributario y ventas sin conexión) y P1 (precio conciliado) | 1 |
| POS con operación sin conexión | P3 (restricción 5) | 1 |
| X-01 Autorización y auditoría de cruces | P2 (frontera) | 1 |
| F-03 Consentimiento y evidencia | P4 (de F-01 y F-02) y P2 | 1 |
| F-01 Originación y autorización | P2 (financiero) y P3 (el POS nuevo consulta la evaluación de crédito) | 1 |
| F-02 Cartera, cobranza y repactaciones, ola 1 | P2 (migración antes de 2029) | 1 |
| R-02 Abastecimiento y reposición | Ninguno: consume un R-03 estable, pero no es condición de P1 a P3 | 2 |
| R-04 Pedidos y cumplimiento omnicanal | Ninguno: depende de R-03 y R-05 | 2 |
| R-06, R-07, R-08 | Ninguno; el comité pone el marketplace al final | 2 |
| R-09 Clientes y fidelización Retail | Ninguno; la objeción de la frontera se cumple con X-01 en la Etapa 1 | 2 |
| F-02, ola 2 | Ninguno: la segunda parte de la migración (repactaciones y cobranza en curso) | 2 |

Punto sensible: R-02 y R-04 también sostienen las promesas de existencia y de entrega (guía de servicios). Se dejan en la Etapa 2 porque el comité nombra la exactitud y la disponibilidad publicada, no la reposición ni el estado del pedido, y porque ambos necesitan R-03 estable. Si el cliente o la evaluación leyeran la "existencia" como toda la cadena, se revisaría su etapa; ya hay cerca del 70 % del esfuerzo en la Etapa 1 (ver "Ajustes posteriores").

### Decisión A3. Marketplace (R-07)

Integración con el marketplace en Etapa 2. Razones: orden del comité (Caso 13.1, marketplace al final) y dependencia técnica de R-03 estable. Mientras tanto el marketplace sigue operando como hoy (EXC-12). Se deja sin verificar cuánto depende hoy del inventario con datos del Caso; se retoma en la Ronda E si hace falta.

### Fijado por las Bases, sin discusión

Etapa 1: plataforma de coordinación e integración (1.14), plataforma híbrida (1.15), identidad, seguridad y observabilidad, mapa de las 14 integraciones como primera entrega.

## Ronda B. Dependencias técnicas (cerrada)

Orden aprobado por el usuario. Cada capa necesita las anteriores. Sirve como columna "requiere a".

| Capa | Contenido | Requiere a |
| :-- | :-- | :-- |
| 0 | Plataforma de integración, identidad, mapa de las 14 integraciones | (base) |
| 1 | X-01, F-03, R-01 | Capa 0 |
| 2 | R-03, R-05, F-01 | Capa 1 (R-03 y R-05 requieren R-01; F-01 requiere F-03 y X-01) |
| 3 | R-02, R-04, F-02, R-09 | Capa 2 |
| 4 | R-06, R-07, R-08 | Capa 3 |

Dependencias que sostienen el orden: X-01 antes de cualquier vista unificada; F-03 antes de F-01 y F-02; R-01 antes de R-02, R-03, R-04 y R-05; R-03 antes de R-04, R-07 y R-08; R-05 y R-04 antes de R-06.

Pendiente de verificar contra el Caso: el contenido exacto de R-06, R-08 y R-09, que fija su posición en las capas 3 y 4.

## Ronda C. Riesgo e hitos externos (cerrada)

Solo criterio de ubicación; no se redacta riesgo. Hitos que condicionan: fin de soporte de la plataforma de 2011 en enero de 2029; pasos a producción en los meses 16 y 21 (fuera de congelamientos con inicio en enero de 2027, SUP-26 del sd-02).

### Decisión C1. Financiero en la Etapa 1
F-03, F-01 y la primera ola de F-02 en Etapa 1. Razón: objetivo 5 (retirar la plataforma antes de 2029) y objeción del gerente financiero; dejar todo el financiero en la Etapa 2 deja la migración para los meses 13 a 21.

### Decisión C2. Olas de F-02
- **Corrección del 2026-10-06 (auditoría DEC-40):** la división original (activa / cerrada o castigada) se descarta, porque los 620.000 son todos clientes con saldo vigente (Caso cap. 2 y restricción 8). Se divide por complejidad (opción B, decidida por el usuario).
- Primera ola (Etapa 1): clientes con saldo al día, sin repactación ni cobranza en curso, migrados en tramos crecientes (primero un tramo pequeño, luego el resto). Cada tramo avanza solo si se cumplen las condiciones del Caso 13.3.5 como compuerta: convivencia real con la plataforma de 2011, conciliación diaria de saldos sin diferencias no explicadas, procedimiento de retorno probado y plan de comunicación a los clientes del tramo. No hay fecha de corte única.
- Segunda ola (Etapa 2): clientes con repactaciones, cobranza y juicios en curso, que dependen de F-03 madura. Se migran con las mismas condiciones.
- La proporción de cada ola no está en el Caso (≈ 46.000 repactaciones al año sobre 620.000 clientes es la única referencia). Se declara como supuesto, con su "Si no se cumple": si la ola 2 resulta mayor de lo previsto, se revisa el balance de etapas por control de cambios.

### Decisión C3. Retiro de la plataforma de 2011
En Operación, con fecha objetivo octubre de 2028 (mes 22). Razones: la marcha blanca exige conciliar con el sistema vigente (art. 17.3), por lo que la plataforma vieja debe seguir viva hasta el cierre de la marcha blanca de la Etapa 2 (meses 19 y 20); el paso a producción de la segunda ola es el mes 21. Margen de unos tres meses frente a enero de 2029.

**Ajuste del 2026-10-07:** la fecha pasó de diciembre de 2028 (mes 24) a octubre de 2028 (mes 22), porque diciembre cae dentro del congelamiento total del 1 de noviembre al 6 de enero (Caso 13.2).

Condición del usuario: la fecha se acepta siempre que cumpla con las Bases. Verificado: las Bases no fijan fecha de retiro; piden conciliación sin diferencias no explicadas (art. 17.3) y operación entre los meses 21 y 56 (art. 17). Dependencia: el mes 22 = octubre de 2028 solo con inicio en enero de 2027; si el inicio cambia, se recalcula.

## Ronda D. Capacidad de absorción del cliente (cerrada)

Contraste: TI de Ancoa de 46 personas para nueve plataformas, rotación de 62 %, terminales compartidas.

### Decisión D1. Reparto de servicios (aceptado)
- Etapa 1 (7 servicios, más plataforma y POS): R-01, R-03, R-05, F-01, F-02 (primera ola), F-03, X-01.
- Etapa 2 (6 servicios): R-02, R-04, R-06, R-07, R-08, R-09, más F-02 (segunda ola).
- Alivio previsto si la Etapa 1 resulta sobrecargada: mover R-05 o la primera ola de F-02. No se recomienda (R-05 sostiene la venta con documento tributario; F-02 protege el plazo de 2029).

### Decisión D2. POS en dos olas (propuesta del usuario, aceptada)
Entregable 1.16 (POS con operación sin conexión de 24 h instalado en las 22 tiendas), ambas olas en la Etapa 1 y la ola 2 antes del paso a producción del mes 16. Razón: al pasar a producción la Etapa 1 es el registro oficial y la restricción 5 del Caso exige que cada tienda venda sin enlace; el Caso 13.1 pide fundamentar qué entra primero y con qué criterio.

| Ola | Alcance | Cuándo |
| :-- | :-- | :-- |
| 1 | Piloto en 3 tiendas | Dentro del desarrollo de la Etapa 1 |
| 2 | Las otras 19 tiendas, en orden creciente de riesgo (la insignia y las de conectividad más débil, como Coyhaique, al final) | Antes del mes 16 |

**Selección de las tiendas piloto (DEC-43, método integrado el 2026-10-06).** Se fijan **3 tiendas**. El método parte de un texto aportado por el usuario y se ajustó así:
- **Zona:** tiendas del entorno de Santiago, cercanas al centro principal de operación y al centro de distribución de la Región Metropolitana, para facilitar el acompañamiento presencial, la observación de incidentes y el retorno. Depende de SUP-27 del sd-02 (concentración de 11 tiendas en ese entorno), que sigue sin validar con el cliente; si no se valida, se eligen las más cercanas al centro de operación según la ficha de sitios.
- **Volumen:** ventas de nivel medio o bajo, para limitar la exposición inicial. No sustituye la prueba posterior en locales de mayor volumen.
- **Insignia fuera del primer corte:** concentra el 17 % de la venta presencial y tiene un mesón del negocio financiero por piso (Caso cap. 2). Entra en la ola 2, una vez demostrados los criterios de avance.
- **Cobertura:** entre las tres deben cubrir las tres versiones del POS actual y, si es posible, tiendas con y sin enlace de respaldo y con y sin red segmentada. No se elige una tienda a la calle: según el Caso están en ciudades regionales y no cerca de Santiago.
- **Corte de 24 h:** es provocado; puede hacerse en cualquier tienda piloto y prueba la misma autonomía del componente local. La conectividad real más débil (mall sin respaldo, Coyhaique) se observa en la ola 2.

Criterios de la ficha de sitio, a validar antes de fijar los nombres:
1. Ubicación real y distancia operativa para soporte y retorno.
2. Volumen de transacciones y horarios de mayor demanda, para confirmar la clasificación media o baja.
3. Versión de POS, conectividad principal y de respaldo, segmentación de red y disponibilidad de equipos y periféricos.
4. Capacidad de operar sin conexión y de reconciliar ventas, pagos, promociones, documentos e inventario al recuperar el enlace.
5. Procesos cubiertos, dotación y disponibilidad del personal para capacitación, marcha blanca y acompañamiento.
6. Evidencia de pruebas de aceptación, monitoreo y retorno probado antes del corte productivo.

Los identificadores de las tiendas quedan pendientes de la ficha validada de sitios y se fijan en el sd-07 y en el plan de implantación. El avance a la ola 2 depende de la compuerta de abajo.

Compuerta para pasar a la ola 2 (todas, aceptadas):
1. Al menos 4 semanas de operación real en las 3 tiendas, con un fin de semana de venta alta (mismo plazo que el art. 17.3).
2. Venta completa en caja de 25 s o menos, sobre ventas reales.
3. Precio cobrado igual al exhibido: cero diferencias en muestra auditada; cambio de precio en cajas en 5 minutos o menos.
4. Evaluación de crédito de 8 s o menos en el punto de venta.
5. Corte de enlace provocado de 24 h continuas en la tienda 3, con venta, cobro, promociones, documentos y consulta de existencia local funcionando.
6. Ventas del corte conciliadas en 30 minutos o menos tras la reconexión, sin pérdida de transacciones.
7. Cero incidentes críticos o altos abiertos y acta firmada por la Contraparte Técnica.
8. **Retorno probado** (Caso 13.3.1): ensayo real de vuelta al POS anterior en una de las 3 tiendas piloto, con las ventas conciliadas por R-05 al cambiar en ambos sentidos. Tiempo máximo del retorno `[por definir en el sd-07]`. Agregada el 2026-10-06 tras la auditoría (DEC-43).

9. **Prueba de factibilidad del crédito sin conexión** (`fundamentacion_credito_sin_conexion.md` §7): durante el corte provocado de 24 h de la condición 5, las compras con cupo en caché se autorizan dentro de los topes del Emisor, el 100 % queda con aceptación recuperable en F-03 y la conciliación termina en 30 minutos o menos sin diferencias no explicadas. Si no pasa o el Emisor no fija los topes (RC-11), la función se declara no disponible.

Convivencia: mientras la ola 2 no termina, las tiendas no migradas siguen con el POS anterior y R-05 concilia ambos (Caso 13.3.1).

Por qué no se parte por la tienda insignia (Caso 17.6 n.º 1 pregunta por insignia, tienda de calle o categoría acotada): el Caso la identifica (una tienda en Santiago de 14.000 m² en cinco pisos, con el 17 % de la venta presencial y un mesón del negocio financiero en cada piso, cap. 2), así que un fallo ahí expone la mayor parte de la venta y de la operación de crédito. La compuerta, además, necesita observar varios perfiles de tienda, no uno solo de alto volumen. [Corregido el 2026-10-06: la versión anterior decía, erróneamente, que el Caso no identifica una insignia.]

**Ventanas de instalación (Caso 13.3.3 y 13.2).** Con inicio en enero de 2027 y fechas aproximadas (el evento anual lo fija la asociación gremial y se conoce con unas seis semanas), las ventanas libres para instalar en tiendas son: del 7 al 24 de enero; del 8 de marzo al 9 de mayo; desde el 17 de mayo hasta el 31 de octubre, salvo la semana previa y los tres días del evento anual. Congelamientos: 1 de noviembre al 6 de enero, última semana de enero a primera de marzo, segunda semana de mayo, última semana de noviembre y el evento anual. Consecuencia para el POS y los gabinetes: piloto en los meses 6 y 7, compuerta en el mes 8 y ola 2 en los meses 8 a 10, es decir, antes del 1 de noviembre de 2027. Respaldo: si la ola 2 no terminara, lo pendiente se instala del 8 de marzo de 2028 hasta el paso a producción del mes 16 (abril de 2028). Es una propuesta de calendario a confirmar en el sd-07; los gabinetes, la red segmentada y los enlaces de las tiendas siguen la misma restricción.

Pasos a producción de las etapas: mes 16 (abril de 2028) y mes 21 (septiembre de 2028) caen fuera de las ventanas. Lo mismo vale para los tramos de la cartera: se programan solo en ventanas libres.

Cierra el pendiente "POS: etapa a o b" de la Ronda F: opción (a), Etapa 1.

## Ronda E. Prioridad del comité (cerrada)

Orden del comité (Caso 13.1): inventario y disponibilidad, precio, financiero, marketplace y analítica. El Caso exige documentar cada desviación; repetir el orden sin criterio se evalúa como falta de criterio.

Coincide con el comité: inventario (R-03) y precio (R-01) en Etapa 1; marketplace (R-07) y analítica en Etapa 2.

### Desviación E1. Financiero en la Etapa 1
El comité lo ubica tercero. Se adelanta por: (a) el soporte de la plataforma de 2011 termina en 2029 (objetivo 5); (b) F-03 es dependencia técnica de F-01 y F-02, por lo que no puede quedar al final; (c) la migración de cartera necesita más de una marcha blanca para conciliarse.

R-04 en Etapa 2 no se documenta como desviación: respeta el orden del comité (depende de R-03 y R-05).

## Ronda F. Casos especiales (cerrada)

Los ajustes posteriores a la auditoría están al final de este documento (sección "Ajustes posteriores").

El POS se resolvió en la Ronda D (decisión D2).

### F1. Sistema central de retail de 2009 (reemplazo firme, SP-01)
- Etapa 1: migra maestro de artículos y precios (R-01) e inventario (R-03).
- Etapa 2: migra órdenes de compra, recepción y base de reposición (R-02) y se retira el sistema.
- El "inventario contable" que hoy está en el sistema central queda en el ERP (R-03 excluye lo contable).

### F2. E-commerce y fidelización (se evalúan e integran, EXC-15)
- Etapa 1: pruebas de e-commerce e integración con R-03; prueba de separación de datos de fidelización antes de cualquier cruce.
- Etapa 2: integración de fidelización con R-09.
- Centro de Concepción: se mantiene como está (decisión posterior del 2026-10-06, SP-02); evaluación y costeo en la Etapa 1 (1.20c); no se instalan componentes ahí (1.15.18 retirado). R-03 modela Concepción como nodo con confianza declarada.

Agregado el 2026-10-06 tras la auditoría (DEC-46), con el Caso 13.3.6 ("todo cambio que afecte la disponibilidad publicada debe probarse primero en un subconjunto acotado de categorías, midiendo la tasa de cancelación antes y después"):
- **Piloto por categorías:** el nuevo cálculo de disponibilidad de R-03 se publica primero en un subconjunto acotado de categorías del e-commerce, y se mide la tasa de cancelación por falta de existencia antes y después. Referencia: 1,9 % en 2025 y meta bajo 0,3 % (Caso cap. 7, indicadores). Las categorías concretas se fijan en el sd-07.
- **Umbrales de las pruebas de e-commerce:** en las categorías piloto, cancelación por falta de existencia menor que la medida antes del cambio y sin superar el 0,3 % al cierre del piloto; disponibilidad publicada actualizada en 30 s o menos tras una venta en cualquier canal; consulta de disponibilidad en 400 ms o menos (RT-09.01). Si no se cumplen, el reemplazo del e-commerce solo entra por control de cambios (EXC-15).
- **Umbrales de la prueba de separación de datos de fidelización:** cero atributos del Emisor en perfiles comerciales y 100 % de los cruces con finalidad, autorización y registro por X-01.

### F3. Corte de inventario
Estrategia declarada (RT-05.15) para el paso a producción de R-03 en 22 tiendas y 2 centros de distribución que no cierran. Etapa 1.

### F4. Gestión (2.x) y documentación (3.x), asignación por proceso
- 2.1 a 2.11 (inicio y planificación): al comienzo.
- 2.12 a 2.15 (seguimiento): continuos.
- 2.16: al cierre.
- 3.5, 3.6, 3.7, 3.9 y 3.10: repetidos en cada etapa.
- 3.11 (plan de retiro de la plataforma de 2011): documento en Etapa 1; el retiro es en Operación (C3).

### F5. Entregables nuevos de la normativa de la CMF
3.12 (plan de salida del proveedor de nube) y 3.13 (diligencia reforzada): Etapa 1. 3.14 (registro I28): condicional, Etapa 1.

## Ajustes posteriores a la auditoría (2026-10-06)

Decididos con el usuario después de `auditoria_decisiones.md`.

- **Cartera de F-02:** opción B (por complejidad y por tramos), ver C2.
- **Novena plataforma:** son las planillas; EXC-14 retirada; cobertura en `descripcion_alcance_producto.md` §4.2.
- **Centro de Concepción:** se mantiene como está (EXC-13, SP-02, RC-10); 1.15.18 retirado.
- **Portal público:** se separa en 1.31a (Etapa 1: catálogo, precio, disponibilidad e información precontractual; depende de R-01, R-03 y F-03) y 1.31b (Etapa 2: consulta de pedido; depende de R-04).
- **Apps de sala (1.36 y 1.38):** piloto en las 3 tiendas del POS en la Etapa 1 y despliegue al resto en la Etapa 2. Razón: el Caso no obliga a tenerlas en las 22 tiendas el mes 16, a diferencia del POS (restricción 5).
- **Carga estimada:** Etapa 1 cerca de 70 % del esfuerzo ponderado (65 a 70 % según pesos), Etapa 2 cerca de 29 % y 1 % en Operación. Por mes, la Etapa 1 es unas 22 % más intensa que la 2 (12 meses de desarrollo frente a 6). Los pesos son supuestos del asistente.
- **Política de retención y custodia de datos (3.15):** nuevo entregable de documentación en la Etapa 1, porque ningún documento de la lista fijaba los plazos de retención de RT-05.10 y RT-16.10. Total vigente: 122 entregables.
- **Obras, equipos y enlaces (tensión RT-06.33 frente al cap. 11):** el CLIENTE provee, instala y contrata lo físico; el proponente especifica, costea, coordina, certifica y configura (SP-04, EXC-19, RC-02, RC-04). Los entregables 1.27 y 1.28 se amplían a calendario de compra y de obras; 1.15.23 pasa a ser acta y certificado de conformidad. El calendario de obras y compras debe calzar con las ventanas libres y con las olas del POS (sd-07).

## Ronda G. Etapas de lo restante, con los criterios P1 a P4 (2026-10-06)

Se aplicaron los criterios de la decisión A2 a los entregables cuya etapa seguía sugerida. Resultado: una etapa cambia (3.14); las demás se confirman con su criterio. Marca **C** en `entregables_alcance.md`; por confirmar por el usuario.

| Entregable | Criterio | Etapa |
| :-- | :-- | :-- |
| 1.23 Conectores de transporte de última milla | P4 de R-04, que es de la Etapa 2; no es integración crítica | 2 |
| 1.24 Conector con remuneraciones | P4 de R-06 (Etapa 2) | 2 |
| 1.25 Informe de etiquetas electrónicas | P1: la discrepancia de precio en sala es la infracción fiscalizada y el informe define cómo se resuelve; alimenta el estado de etiqueta de R-01 | 1 |
| 1.26 Especificación de dispositivos móviles | P4 de las apps 1.36 y 1.38 (ola 1 en la Etapa 1); el cliente necesita plazo de compra | 1 |
| 1.27 Especificación del hardware | P3: la infraestructura física va en la Etapa 1 y el cliente la compra antes | 1 |
| 1.28 Especificación de obras y enlaces | P3 y P4: las obras preceden a la instalación | 1 |
| 1.30 Repositorio de datos históricos no migrados | P4 de los retiros: debe existir antes de retirar el sistema de 2009 (después de la Etapa 2) y la plataforma de 2011 (Operación) | 2 |
| 1.15.23 Acta y certificado de conformidad | P3, junto con la infraestructura | 1 |
| 1.32 Portal del cliente autenticado | Ninguno; depende de R-04, R-08 y F-02 | 2 |
| 1.33 Vista del vendedor de marketplace | Ninguno; depende de R-07 | 2 |
| 1.34 Portal del proveedor | Ninguno; depende de R-02 | 2 |
| 1.35 App del cliente | Ninguno; depende de R-04 y F-02 | 2 |
| 1.37 App de preparación de pedidos | Ninguno; depende de R-04 | 2 |
| 1.39 App de recepción de mercadería | Ninguno; depende de R-02 (punto sensible: la recepción alimenta el inventario; se deja en la Etapa 2 porque el Caso no la nombra como causa de la discrepancia) | 2 |
| 3.1 a 3.4 (arquitectura, estándares, interfaces, pruebas, seguridad) | P3: la plataforma y la seguridad son de la Etapa 1; P2: el modelo de amenazas cubre la frontera. Emisión en la Etapa 1, actualización en la 2 | 1 y actualiza 2 |
| 3.3c, 3.3d, 3.3e (informes de pruebas) | P3 y art. 17.3: cada marcha blanca exige indicadores medidos. Uno por etapa | 1 y 2 |
| 3.8a y 3.8b (manuales por perfil y gestión del cambio) | Art. 17.3: personal capacitado antes de cerrar cada marcha blanca; los manuales cubren los servicios de cada etapa | 1 y 2 |
| 3.12 Plan de salida del proveedor de nube; 3.13 Diligencia reforzada | P3: la nube es parte de la plataforma híbrida; la diligencia precede a la contratación | 1 |
| **3.14 Registro en formato I28 (condicional)** | Ninguno: es una propuesta de la CMF aún no vigente. **Cambia de la Etapa 1 a la Etapa 2**, condicionada a que la norma se apruebe | 2, condicional |

Efecto en la carga: 3.14 sale de la Etapa 1 (impacto menor, unos 1 a 2 puntos de esfuerzo ponderado).
