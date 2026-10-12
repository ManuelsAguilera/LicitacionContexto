> Detalle de la revisión de los formularios (2026-10-12). Borrador. **Nota:** cualquier hallazgo que diga que el Comité de Operación debe iniciar en el mes 16 es un falso positivo: el artículo 71 de las Bases fija «mensual desde el mes 13».

# Revisión de los formularios T-16 (plan de riesgos) y T-18 (implantación, corte y reversión)

Archivos: `02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-16.tex` (T16) y `...-T-18.tex` (T18). Contrastados con sd-08 (S8), sd-07 (S7), sd-05 (S5), sd-03 (S3), T-14, T-12, Bases Administrativas (BA) y Bases Transversales (BT). Solo lectura; no se editó nada.

## Comprobaciones que resultaron correctas

- T16 tiene 37 riesgos, R-01 a R-38 sin R-26, y los mismos 37 que el cap. 8. Las ramas coinciden con S8 8.2 (Proyecto 16, Técnica 8, Organizacional 5, Operación 5, Seguridad 3). Las miradas también (Solución 14, Desarrollo 13, Implantación 14).
- Exposición = P x I en los 37 casos. Las zonas coinciden con la Tabla 8.3 de S8: 3 críticos, 11 altos, 21 medios y 2 bajos. Las Tablas 8.4 y 8.5 de S8 coinciden con T16.2.
- Los valores esperados de la Tabla 8.6 de S8 cuadran: 6.496 h, 29,2 semanas y 59 semanas brutas. La reducción de 2.808 h y la reserva de 3.688 h (6.496 - 2.808) también.
- Las 8 oportunidades de T16.5 coinciden con S8 8.2 y 8.3.
- Las cuentas EDT citadas en T16.4 existen todas en T-14. Ninguna falta.
- La ventana de T16.4 coincide con la de la cuenta principal de T-14 en todos los riesgos salvo R-18 (ver B3). El responsable de T16.3 coincide con el de T-14 en 30 de 37; los otros 7 están en M5.
- Los residuales de los 14 riesgos críticos y altos coinciden con la Tabla 8.10 de S8 (mismos números), salvo la incoherencia aritmética de G1.
- Comité de Operación mensual desde M13 (T18 líneas 131 y 212): correcto (art. 71).
- Las seis condiciones de cierre de la marcha blanca (T18 197-204) reproducen BA 17.3 de forma fiel. El Plan de Reversibilidad a 90 días (T18 227) cumple BA 77.2. Los meses de marcha blanca y producción (13-15/16, 19-20/21), los hitos H1 a H12 y los meses de la Tabla 2 coinciden con BA y T-14.
- T18 usa correctamente la ventana de congelamiento: el 1-nov-2027 para la versión candidata y la certificación en preproducción, el 6 de enero y la última semana de enero a la primera de marzo, y la segunda semana de mayo.

## Hallazgos T-16

### G1 (grave, confirmado): residuales de R-18, R-20, R-24 y R-34 en 0,08 contradicen la reducción de probabilidad del cap. 8

- Ubicación:
  - T16 líneas 304 (R-18), 306 (R-20), 310 (R-24) y 319 (R-34), columna "Exposición residual" = 0,08.
  - S8 Tabla 8.10 (líneas 493, 494, 496 y 499), que repite el 0,08.
- Qué dice: S8 línea 537 afirma que las respuestas de R-02, R-13, R-18, R-20, R-24 y R-34 "reducen la probabilidad solo de 0,60 a 0,40". La Tabla 8.11 es coherente con eso: reducción de un tercio, por ejemplo R-18 720 a 480 h (-240), R-20 -128, R-24 -192 y R-34 -72.
- Debería decir: con P' = 0,40 e I = 0,40, el residual es 0,16, no 0,08. Quedan en zona Media (0,16 sigue siendo Media), pero el número no cuadra. El 0,08 solo se obtendría con P' = 0,20, que es la reducción a un tercio de la probabilidad y no coincide con las horas de la Tabla 8.11.
- Los otros 10 riesgos altos sí cuadran con su reducción de horas: R-12 a P' 0,20 (0,16), R-25, R-01, R-11, R-16, R-23, R-33 y R-37 a P' 0,20 (0,16), y R-02 y R-13 a P' 0,40 (0,32).
- Fuente: S8 líneas 503 y 537, Tabla 8.11. Aritmética verificada con la escala de 8.1 (0,05; 0,20; 0,40; 0,60; 0,85).
- Sugerencia: poner 0,16 en T16.4 para R-18, R-20, R-24 y R-34, y lo mismo en la Tabla 8.10 de S8. Eso deja 0,16 residual en los 14 riesgos críticos y altos salvo R-02 y R-13 (0,32). Conviene ajustar en S8 la frase "a la mitad o a un tercio" (línea 503): para estos cuatro la reducción es de un tercio de la probabilidad, de 0,24 a 0,16.
- Alternativa, no recomendada: si el equipo prefiere 0,08, habría que subir la reducción a P' = 0,20 y recalcular la Tabla 8.11, la reserva de 3.688 h y la simulación.

### G2 (grave, confirmado): R-02, la ventana de 8 semanas y el disparador "menos de 8 semanas de aviso"

- Ubicación: T16 línea 230 (acción y disparador de R-02) y S8 líneas 445 y 465.
- Qué dice: la acción fija 8 semanas sin despliegues antes del evento y el disparador es "fecha del evento con menos de 8 semanas de aviso".
- Problema 1: el Caso fija el aviso en unas 6 semanas (Caso líneas 297, 629 y RT-10.05 801). Con aviso normal de 6 semanas el disparador se cumple siempre, así que no es un evento incierto sino la condición de partida. La probabilidad de 0,60 y el residual de 0,32 pierden sentido, porque el disparador siempre dispara.
- Problema 2: S7 línea 639 reserva menos de 8 semanas (1 de confirmación, 2 de ensayo, 2 de reserva y 1 de congelamiento, es decir 6, coherentes con el aviso) y T-14 1.9.5 usa "dos semanas de reensayo". T16 y S8 piden 8 sin que ningún plan las contenga.
- Problema 3: las 8 semanas chocan con el plan. El paso a producción de abril de 2028 llega 4 a 10 semanas antes del evento (S8 línea 311). Además, la sustitución del POS 2014 tienda por tienda avanza desde el mes 16 (T18 línea 116) y la ventana de correcciones es la segunda a la última semana de marzo (S8 línea 467). Una ventana de 8 semanas sin despliegues antes de un evento "entre mayo y junio" quedaría dentro de abril y marzo.
- Debería decir: alinear a la lógica de S7. El disparador debería medir el hueco real. Ejemplo: "fecha anunciada que deja menos de 6 semanas de preparación o menos de 2 semanas de reserva de reensayo, o un servicio con despliegue en curso dentro de las 6 semanas previas a la fecha más temprana posible". La acción debería decir "reservar el calendario anual con la fecha más temprana posible, mantener la versión ensayada y escalar si el aviso no alcanza".
- Sugerencia: corregir T16.3 y T16.4 y, con ellos, S8 (líneas 445 y 465).
- Estado: confirmado en la incoherencia. Por confirmar el valor que el equipo elija (6 u 8 semanas).

### M1 (mediana, confirmado): R-13, disparador "algún tramo sin corte al 15 de septiembre de 2028"

- Ubicación: T16 línea 241 (S8 línea 469 igual).
- Qué dice: el disparador se activa si algún tramo está sin corte al 15 de septiembre de 2028.
- Debería decir: S5 Tabla 5.14 programa el tramo T3 (cobranza y juicios) para el 1 al 14 de octubre de 2028. Por plan, T3 siempre estará sin corte el 15 de septiembre, así que el disparador salta siempre (mismo defecto que G2).
- Sugerencia: "algún tramo T1 o T2 sin corte al 15 de septiembre, o T3 sin ensayo conforme al 15 de septiembre, o cualquier tramo sin corte al 1 de octubre".
- Fuente: S5 tabla de hitos de migración y su texto (el corte de T3 va del 1 al 14 de octubre; el apagado de la plataforma de 2011 es antes del 31).

### M2 (mediana, por confirmar): R-12, plazo y disparador del 24 de enero de 2028

- Ubicación: T16 líneas 240 y 298 (S8 línea 467 igual).
- Qué dice: plazo "24 de enero de 2028" y ventana de despliegue "del 7 al 24 de enero de 2028".
- Problema: el 24 de enero de 2028 es lunes y la semana del 24 al 30 es la última semana de enero, es decir el primer día del congelamiento de vuelta a clases. S5 Tabla 5.14 (carga para marcha blanca) usa "7 al 23 de enero de 2028".
- Sugerencia: unificar en "23 de enero de 2028" en T16, S8 y T18, o aclarar que "última semana" arranca el 31.
- Estado: por confirmar la definición de la última semana.

### M3 (mediana, confirmado): R-21, "los 25 supuestos"

- Ubicación: T16 líneas 133 y 249.
- Qué dice: "un supuesto de los 25"; "Validar los 25 supuestos".
- Debería decir: los supuestos vigentes son SUP-01 a SUP-28 y SP-01 a SP-04 (verdad del proyecto; S2 Anexos tiene 27 SUP distintos listados y S8 cita SUP-26 y SUP-28). Ninguna fuente sostiene "25".
- Sugerencia: "los supuestos del registro (SUP-01 a SUP-28 y SP-01 a SP-04)" o la cifra que fije S2 Anexo A.5.

### M4 (mediana, por confirmar): R-37, "las siete decisiones del cliente"

- Ubicación: T16 líneas 148 y 264 (S8 líneas 303, 458 y 477).
- Qué dice: "siete decisiones del cliente deben tomarse antes de cerrar el apartado 4.1".
- Problema: S4 solo tiene siete ADR (línea 394), que son decisiones de arquitectura del proponente, no del cliente. No encontré en S2, S3 ni S4 una lista de siete decisiones del Cliente. La cifra "siete" no tiene respaldo localizable.
- Sugerencia: enlazar a la lista (o a las decisiones condicionadas de S4: residencia de datos del Emisor, tarjeta propia sin enlace, etc.) con un número verificable, o decir "las decisiones del Cliente pendientes".

### M5 (mediana, confirmado): R-04, R-16, R-20, R-21, R-27, R-33 y R-37, responsable distinto del de la cuenta principal del T-14

- Ubicación: T16 líneas 214 y 268 afirman que "los responsables son los roles que ejercen la cuenta de control correspondiente en el T-14". Los 7 siguientes difieren (T16 / T-14 cuenta principal):

| Riesgo | T-16 | T-14 (cuenta principal) |
| :-- | :-- | :-- |
| R-04 | Líder de Integración | 1.2.1: Líder Funcional |
| R-16 | Jefe de Proyecto | 1.6.7: Líder de Integración |
| R-20 | Líder de Implantación | 1.3.7: Arquitecto de Solución |
| R-21 | Jefe de Proyecto | 1.2.4: Líder Funcional |
| R-27 | Jefe de Proyecto | 1.2.1: Líder Funcional |
| R-33 | Jefe de Proyecto | 1.11.3: Líder de Implantación |
| R-37 | Jefe de Proyecto | 1.2.4: Líder Funcional |

- Problema: el dueño del riesgo puede diferir del dueño de la cuenta, pero la frase de T16 dice que son lo mismo. S8 líneas 461 ("siete tienen como responsable al Jefe de Proyecto") y 541 dependen de ello.
- Sugerencia: reescribir la frase para decir "el responsable del riesgo es el rol mejor ubicado para actuar sobre su causa; la cuenta puede estar a cargo de otro rol", o alinear los 7.

### M6 (mediana, confirmado): ventana de R-13 y R-25 (14-18) frente a los cortes de cartera

- Ubicación: T16 líneas 299 y 311.
- Qué dice: cuenta principal 1.7.8 (plan de retiro), ventana 14-18. El plazo de la acción es el 15 de octubre de 2028 (mes 22).
- Problema: el trabajo que el riesgo vigila (cortes de T2 y T3, compuertas) corre en 1.7.6 (10-21), 1.7.12 (12-21) y 1.7.9 (22-22). La ventana 14-18 termina en junio de 2028, cuatro meses antes del plazo. Además, T-14 termina 1.7.6 y 1.7.12 en el mes 21 (septiembre de 2028), pero S5 corta T3 en octubre (mes 22).
- Sugerencia: poner como cuenta principal 1.7.12 o 1.7.6 (ventana 12-21) o ampliar a "12-22", y pedir a T-14 que extienda 1.7.6 y 1.7.12 al mes 22.

### M7 (mediana, por confirmar): "hito contractual" del mes 22 en S8 y T16 frente a "objetivos internos" en T18

- Ubicación: T18 línea 257 ("El retiro de la plataforma de crédito de 2011 en el mes 22 y el cierre de la remediación en el mes 24 son objetivos internos anticipados de la oferta").
- Problema: S8 línea 161 incluye "el retiro de la plataforma de 2011 en el mes 22" entre los hitos contractuales sin holgura, y R-13 (crítico) y R-25 son críticos o altos por esa regla; la simulación del mes 22 (Tabla 8.8) también lo trata como hito. BA y el Caso solo fijan 2029. S3 línea 302 lo presenta como compromiso de la oferta.
- Sugerencia: uniformar. Lo correcto es "compromiso de la oferta, inamovible para el proponente, anterior a los vencimientos externos de 2029", y la regla de S8 debe decir "hito comprometido" y no "contractual". Si el mes 22 no es contractual, la clasificación crítica de R-13 depende de una regla del proponente y debe declararse así.

### M8 (mediana, confirmado): R-10 y R-15, disparador posterior al plazo de la acción

- Ubicación: T16 líneas 238 y 296 (R-10) y 243 y 301 (R-15).
- Problema: R-10 tiene plazo "mes 4" pero su disparador es "hallazgo crítico en la prueba de penetración", y la prueba (1.8.6) es en los meses 10-18. R-15 tiene plazo "mes 4" y el disparador es la prueba de 24 h (1.9.9, meses 6-7).
- Sugerencia: separar el plazo del diseño (mes 4) del plazo de la verificación (mes 18 y mes 7), o cambiar los disparadores a indicadores del diseño.

### M9 (mediana, por confirmar): R-16, plazo del mes 9 frente a la ventana de 1.6.7

- Ubicación: T16 líneas 244 y 302.
- Problema: la cuenta principal 1.6.7 (contingencia tributaria probada) termina en el mes 6 (H3). El plazo y disparador del mes 9 queda fuera, aunque está declarado en la acción. Además, S3 línea 713 exige modalidad aprobada "antes de comprometer la operación sin enlace", y la prueba de 24 h es en los meses 6-7: si la modalidad se aprueba recién en el mes 9, no podría ser requisito de esa prueba.
- Sugerencia: aclarar si la prueba de 24 h de los meses 6-7 exige o no la modalidad fiscal aprobada.

### M10 (mediana, confirmado): numeración sin R-26

- Ubicación: T16 líneas 138 y 196. No hay nota que explique el hueco entre R-25 y R-27.
- Sugerencia: añadir una nota ("R-26 fue retirado en la versión X") o renumerar. El lector podría tomarlo por una omisión.

### B1 (baja, confirmado): R-18, ventana de la tabla distinta de la regla declarada

- Ubicación: T16 línea 304: R-18 ventana 4-15. La cuenta principal 1.7.2 tiene 4-10. 4-15 es la unión con 1.7.3 (11-15). El resto de los riesgos usa la ventana de la cuenta principal, tal como lo dice la línea 272.
- Sugerencia: poner 4-10, o declarar que en R-18 la ventana es la unión.

### B2 (baja, confirmado): nombres de rol frente a sd-01 y BT 19.2

- Ubicación: T16 usa "Líder de Gestión del Cambio" (R-05, R-06, R-22) y "Líder de Implantación" (R-20, R-38, O-08). BT 19.2 y sd-01 (línea 198) definen un único rol "Líder de Implantación y Gestión del Cambio". T-14 también separa los dos.
- Sugerencia: unificar en todos los formularios con el nombre de BT 19.2, o declarar en sd-01 que son dos personas.
- Ocurre lo mismo con "Líder de Calidad" (sd-01 y T18 línea 210) y "Líder de Calidad y Pruebas" (T16, T-14, BT).

### B3 (baja): otros puntos de T16

- T16 línea 258: la estrategia de R-31 es "Mitigar y transferir dependencia", que no es una de las estrategias del apartado 8.3. Dejar "Mitigar" y explicar la transferencia en la acción.
- T16 línea 346: la oportunidad O-02 ("adelantar la prueba de corte de 24 h si la filial fija los topes antes del mes 6") coincide con la acción base de R-14 (fijar los topes antes del mes 6). La prueba además depende de H3 (mes 6). Reformular la oportunidad o fijar qué se adelanta.
- T16 líneas 252 y 310 (R-24): acción "antes de abril de 2028" y disparador "a 4 semanas del Día de la Madre" (segunda semana de mayo, es decir mediados de abril). Alinear.
- Los residuales de los riesgos medios y bajos no se pueden reproducir con las tablas (no hay P' e I' separados). Varios exigen bajar también el impacto, por ejemplo R-15, R-17 y R-27, de 0,40 a 0,04, que implica P' 0,20 e I' 0,20. Agregar una columna o nota con P' e I'.

## Hallazgos T-18

### G3 (grave, confirmado): T18 no responde RT-20.01, RT-20.02, RT-20.04, RT-20.05 ni RT-20.06, que T-12 deja como "No"

- Ubicación: T18 completo; T-12 líneas 1331 a 1341 marca esos cinco requisitos como "No" sin remisión.
- Falta, según BT 20.2:
  - RT-20.01: plan de implantación por sitio y por perfil. T18 no nombra las 22 tiendas, las olas, la tienda insignia, las 11 regiones ni los perfiles. Línea 115: "la propuesta no supone una selección".
  - RT-20.02: criterio de avance entre olas y tiempo de ejecución de la reversión. T18 (líneas 216-227) describe mecanismos (bandera, respaldo, plan 1.11.1) pero no da un solo tiempo de reversión (por componente: aplicación, datos, tienda, cartera).
  - RT-20.04: indicadores diarios y umbrales de avance. Solo hay umbrales de rendimiento del caso (línea 186) y no los de avance entre olas.
  - RT-20.05 y 20.06: acompañamiento en terreno y estabilización con dotación y duración declaradas. La palabra estabilización solo aparece en la línea 145 y no hay dotación ni duración. El Caso 13.3 condición 9 también lo exige (línea 719).
  - Caso 13.3 condiciones 4 y 6 (despliegue por tienda, proceso o categoría; cómo se prueba el cálculo de disponible en un subconjunto de categorías): solo hay generalidades.
- Sugerencia: añadir (a) tabla de olas por sitio y perfil de S7/T-14, con fechas dentro de ventanas libres; (b) tabla de reversión con tiempo máximo de ejecución por componente (aplicación con bandera: minutos; datos por restauración: horas; cartera: dentro de la ventana de corte); (c) tabla de indicadores diarios y umbral de avance entre olas; (d) dotación y duración del acompañamiento y de la estabilización por paso a producción (mes 16 y mes 21), con la curva decreciente. Si estas cifras no están decididas, dejarlas como "por definir en el mes X" con responsable, y actualizar el T-12 de acuerdo.

### G4 (grave, confirmado): T18 no incluye el plan de cortes de la cartera de crédito ni las ventanas de corte

- Ubicación: T18 líneas 136 a 147, 188 y 257.
- Qué dice: solo "cualquier diferencia no explicada detiene el avance de la migración" y que el retiro del mes 22 y el cierre del mes 24 son "objetivos internos".
- Debería decir (S5 5.3.3 y Tabla 5.14; S3 línea 302; verdad del proyecto):
  - Tramos T1 (al día, con la Etapa 1), T2 (repactaciones, con la Etapa 2) y T3 (cobranza y juicios).
  - Cortes: R1/T1 del 18 al 31 de marzo de 2028 (producción en abril); R2/T2 del 18 al 31 de agosto de 2028 (producción en septiembre); T3 del 1 al 14 de octubre de 2028.
  - Último corte antes del 15 de octubre de 2028 y plataforma de 2011 apagada antes del 31 de octubre de 2028. Conciliación diaria hasta el apagado.
  - Compuerta por tramo cerrada por la Contraparte Técnica y la filial emisora (S3 línea 302).
  - Retorno probado y plan de comunicación a los 620.000 clientes (Caso 13.3 condición 5; Caso línea 938 "marcha blanca de la migración de la cartera").
  - No se puede apoyar en el congelamiento del 1 de noviembre al 6 de enero.
- Problema: el Caso pide a T-18 expresamente cómo se hace la marcha blanca de la migración de la cartera, qué se concilia, con qué frecuencia y con qué umbral se detiene. T18 no contesta con tramos, fechas ni umbral.
- Problema asociado: el corte de R1 y T1 del 18 al 31 de marzo (S5) cae en las dos últimas semanas de la marcha blanca de la Etapa 1, que BA 17.3 exige sostener "las cuatro últimas semanas" con volumen real. T18 debería explicar cómo se combina el corte con esas 4 semanas, o aclarar que el corte de T1 es posterior al cierre.
- Sugerencia: agregar una subsección "Cortes de datos y de la cartera" con la tabla de S5, el umbral de detención (diferencia no explicada de saldo = 0, dos días seguidos activa el disparador de R-01), el retorno y el calendario frente a los congelamientos.

### M11 (mediana, por confirmar): corte de enlace de 24 h "sin interrumpir la conectividad"

- Ubicación: T18 líneas 115 y 174.
- Qué dice: el piloto "incluye el ensayo de corte de enlace de 24 horas, sin interrumpir la conectividad ni la venta de la operación vigente".
- Problema: S3 línea 300 y la verdad del proyecto describen un "corte de enlace provocado de 24 h en una de las tres tiendas" y aclara que debe quedar fuera de la semana previa y de los tres días del evento. T18 omite esa restricción y la frase sobre conectividad es ambigua: el corte se provoca sobre el POS nuevo aislado, no sobre el enlace de producción.
- También omite los criterios de aprobación: compras dentro del tope autorizadas sin perder transacciones, evidencia recuperable y conciliación en 30 minutos o menos, con acta de la Contraparte Técnica.
- Sugerencia: reescribir "corte provocado de 24 h sobre el POS nuevo de una de las tres tiendas, fuera de la semana previa y de los tres días del evento anual; pasa si ... conciliación <= 30 min; acta de la Contraparte Técnica".

### M12 (mediana, confirmado): evento anual, falta el plan para cada año

- Ubicación: T18 líneas 176 y 179.
- Problema: el Caso 13.3 condición 10 (línea 720) exige declarar qué hace la solución en el evento anual de cada año del proyecto, incluida la posibilidad de congelar componentes ya desplegados. T18 solo cita el ensayo de degradación y dice que se conserva una versión ensayada. No hay tabla año por año (2027: sin producción; 2028: E1 en producción 4 a 10 semanas antes; 2029 a 2031).
- Sugerencia: tabla de 5 filas (2027 a 2031) con estado de la solución, ensayo previo, quién decide congelar y reserva de reensayo (coherente con S7 línea 639 y G2).

### B4 (baja): otros puntos de T18

- Línea 115 ("si el evento anual ocupa la ventana prevista de junio, el piloto se ejecuta en julio"): el evento puede caer en mayo (segunda semana de mayo, mes 5) o en junio. Formular como "si el evento cae en junio, el piloto se desplaza a julio dentro del mes 7".
- Línea 127 ("El dominio financiero permanece segregado en el entorno local"): S4 aloja al Emisor en CLD-01 como ámbito propio (línea 472) y la plataforma de 2011 en DC-01. "Entorno local" induce a error. Decir "ámbito del Emisor, con datos, identidades, redes y claves propios".
- Tabla 2 (líneas 249-250): H8 (mes 14) aparece antes que H7 (mes 16). Es cronológico, pero el orden numérico se rompe. Aceptable; avisar en una nota.
- Línea 276: "Se mantienen sus 64 HH: 48 de acompañamiento y 16 de cierre" cita 1.14.2 y 1.14.5 juntos, pero T-14 asigna 64 HH solo a 1.14.5 (1.14.2 tiene 193 HH). Aclarar a cuál cuenta se refiere.
- Línea 138: la lista de congelamientos está completa (cinco). Correcto. Sin observaciones.
- Línea 105: coherente con BA 17 y la verdad del proyecto. Correcto.

## Resumen de conteo

- Graves: 4 (G1, G2, G3, G4).
- Medianas: 12 (M1 a M12).
- Bajas: 4 grupos (B1 a B4).
- Todos "confirmados" salvo M2, M4, M7, M9 y M11, que quedan "por confirmar", y G2 en el valor elegido.
