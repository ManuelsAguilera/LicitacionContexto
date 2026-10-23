> Detalle de la revisión de los formularios (2026-10-12). Borrador. **Nota:** cualquier hallazgo que diga que el Comité de Operación debe iniciar en el mes 16 es un falso positivo: el artículo 71 de las Bases fija «mensual desde el mes 13».

# Revisión del Formulario T-14 (plan de trabajo, EDT y carta Gantt)

Archivo: `02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-14.tex` (935 líneas). Contraste: Bases Administrativas L2296-2298 y arts. 15-17 (L389-491), sd-07 (`OnlySimpleSolutions-Subdocumento7.tex`), sd-03 (3.2.2, 3.2.3), sd-01, sd-13, T-15 y verdad_proyecto.

## 1. Comprobaciones que pasan (verificadas con script)

- Suma de HH: 164 cuentas, total 40.946 HH. Subtotales por rama coinciden con las filas (1.1=1.423; 1.2=1.087; 1.3=863; 1.4=1.622; 1.5=12.116; 1.6=1.068; 1.7=1.973; 1.8=949; 1.9=1.539; 1.10=9.888; 1.11=795; 1.12=532; 1.13=916; 1.14=969; 1.15=5.206). 12.116 (rama 1.5) + 28.830 (resto) = 40.946; 159 cuentas sin innovación = 31.058 (cuadra con T-15 L103). Innovaciones 1.864+2.336+2.120+1.784+1.784 = 9.888.
- Cuentas por rama (12, 8, 7, 13, 51, 7, 12, 8, 12, 5, 4, 7, 5, 7, 6) = 164, igual que la Tabla 7.1 del sd-07. Rama 1.5: las 51 cuentas declaran 127 casos de uso y cada una trae exactamente tantos CU en la columna de trazas como declara (0 discrepancias).
- Regla del 100 % a nivel de cuentas: las 164 cuentas del diccionario están todas en el cronograma (L578-741), sin cuentas huérfanas ni faltantes, y ventana e hito coinciden 164/164 entre diccionario y cronograma.
- Hitos con sus meses: H1=2, H2=4, H3=6, H4=10, H5=12, H6=13, H8=14, H7=16, H9=17, H10=18, H11=19, H12=21 coinciden con la Tabla 7.6 del sd-07. Calendario: M1=ene 2027, M16=abr 2028, M21=sep 2028, M22=oct 2028, M24=dic 2028, M56=ago 2031 correctos. Gantt cubre 56 meses.
- Red de dependencias: 120 relaciones (L808-927) y 57 nodos (18+35+4), coherente con T-15 L530 y sd-07 L604.
- Pasos a producción (M16 abril 2028, M21 septiembre 2028) no caen en ninguna ventana de congelamiento (el congelamiento de mayo 2028 está en M17-M18).
- Innovaciones: ventanas y esfuerzo coherentes con sd-07 (conteo cíclico 5-12; sombra 13-15; uso 16; resto E2 13-18/19-20/21).
- Cartera: 1.7.6 (620.000), 1.7.12 (compuertas), 1.7.9 (apagado M22) coherentes en meses con sd-07 7.3.3.1 (M22) y verdad_proyecto, con las salvedades de abajo.

## 2. Hallazgos

### Graves

**G1. Anexos prometidos que el formulario no contiene (paquetes, estimación y CPM).**
- Ubicación: T-14 L422-426 (criterio de 1.10.1 a 1.10.5: "criterios por paquete en el anexo de estimación"); L795 y tabla L808-927; sd-07 L116, L470, L604, L617, L637, L660, L664.
- Dice: el sd-07 afirma que "el T-14 presenta el detalle por cuenta y por los 127 paquetes de software" (L470), que las innovaciones están "desglosadas en ... paquetes con estimación y ventanas explícitas en el anexo del T-14" (L116, L637) y que "el anexo CPM del T-14 contiene la red y las fechas tempranas, tardías y programadas" (L604, L660). El T-14 solo trae: diccionario de 164 cuentas, cronograma por cuenta, anclas del Gantt y una tabla de 120 relaciones.
- Falta: (a) la lista de los 127 paquetes de software (la rama 1.5 solo los resume como "N casos de uso"); (b) el anexo de estimación de los 35 paquetes de innovaciones 1.10.x.y, con HH y ventana (los IDs 1.10.1.1 a 1.10.5.7 aparecen en la tabla de dependencias L830-921 sin estar definidos en ningún lugar del formulario; los criterios de aceptación de 1.10.1-1.10.5 remiten a un anexo que no existe); (c) la leyenda de nodos de la red (A a K, Z, P1, P2, T1, T2, H7, H12, MG, RET, TR, CI no se explican) y las fechas tempranas/tardías/holgura.
- Además hay contradicción sobre dónde está el CPM: T-14 L795 dice "cálculo CPM presentado en el T-15"; sd-07 dice "anexo CPM del T-14".
- Gravedad: grave (el T-14 es el formulario donde se verifica la regla del 100 % y el sd-07 se apoya en él; quedan referencias a contenido inexistente y la regla del 100 % no se puede comprobar bajo el nivel de cuenta para 1.5 y 1.10). Estado: confirmado.
- Sugerencia: agregar al T-14 un anexo con los 127 paquetes (código, CU, HH, ventana), el anexo de estimación de los 35 paquetes de innovaciones (más los 5 paquetes de seguimiento, ver G2), la leyenda de nodos del CPM con fechas ES/EF/LS/LF y holgura, y alinear la remisión (T-14 o T-15) en un solo sentido, o bien reescribir el sd-07 para que remita a donde realmente está.

**G2. Inconsistencia de conteo de paquetes de innovaciones (40 vs 35).**
- Ubicación: sd-07 L116 dice "desglosadas en 40 paquetes"; sd-07 L543, L604, L656, L761 y T-14 (red de 57 nodos con 35 paquetes) dicen 35, y L761 añade "cinco paquetes de actividades periódicas" de seguimiento (35+5 = 40).
- El T-14 no muestra los 5 paquetes de seguimiento (ni su HH ni su ventana), por lo que 40 vs 35 no se puede conciliar en el formulario.
- Gravedad: grave por afectar el desglose de 9.888 HH (mediana si se resuelve con G1). Estado: confirmado (inconsistencia sd-07/T-14); por confirmar cómo se reparten las 9.888 HH entre 35 y 40 paquetes.
- Sugerencia: en el anexo de G1 mostrar 7 paquetes de implementación + 1 de seguimiento por innovación (40 filas) y que sumen 9.888 HH por innovación.

**G3. Integraciones de la Etapa 1 cerradas en M18 (H10), después del paso a producción de la Etapa 1 (M16).**
- Ubicación: L304 (1.6.2 "Rediseño de las integraciones de la Etapa 1", ventana 5-18, hito H10 mes 18); L308 (1.6.6 certificación de integraciones, 10-18, H10).
- Dice: las integraciones críticas de E1 (precios y existencia, crédito con el ERP, cobranza y prevención de pérdidas) se aceptan en H10 (M18). Art. 15.1 (L395) pone las "integraciones críticas" dentro del alcance de la Etapa 1, y la Etapa 1 se certifica en H5 (M12) y pasa a producción en M16 (H7) con conciliación diaria (sd-03 L302). Un hito de M18 no puede condicionar algo que debe estar probado antes de la marcha blanca M13-15.
- Debería: dividir 1.6.2 y 1.6.6 en tramo E1 (ventana hasta M12, hito H4/H5) y tramo E2 (hasta M18, hito H10), como hacen 1.5.38-1.5.40 y 1.9.3 ("evidencia separada para E1 antes de H5 y para E2 antes de H10").
- Gravedad: grave (etapa y plazo; afecta la condición de entrada a marcha blanca). Estado: por confirmar (la ventana puede reflejar solo el cierre de la certificación de E2, pero el texto del criterio dice "de la Etapa 1").

**G4. Versión del catálogo de requerimientos desactualizada (v3.0).**
- Ubicación: L146 (1.2.3): "Catálogo RF-001..RF-226, RNF-01..RNF-76 y OP-01..OP-09 ... cobertura del 100 %".
- Verdad vigente: catálogo v3.1, 308 elementos (227 RF, 72 RNF, 9 OP) (sd-03 L310; glosario "catálogo de requerimientos"). El mismo T-14 traza RF-227, RF-228, RF-229, RF-230, RF-231 (L263-L265) que quedan fuera de RF-001..RF-226, y los RNF numerados hasta 76 no son 76 elementos (son 72).
- Debería: "Catálogo v3.1 (308 elementos: 227 RF, 72 RNF y 9 OP)" y no declarar rangos contiguos de IDs.
- Gravedad: grave (cifra del catálogo que el formulario declara cubrir al 100 %). Estado: confirmado.

### Medianas

**M1. Fechas límite de la cartera de crédito ausentes en el formulario.**
- Ubicación: L335, L338, L341 (1.7.6, 1.7.9, 1.7.12) y L785 (ancla M22 "Objetivo interno de retiro").
- Falta: el último corte de cartera antes del 15-oct-2028 y el apagado de la plataforma de 2011 antes del 31-oct-2028 (verdad_proyecto; sd-03 L302 y L409; sd-07 L658, L746, L767). El ancla M22 lo llama solo "objetivo interno" sin fechas; el congelamiento total desde el 1-nov lo convierte en límite duro de ese año, no en objetivo interno (sd-03 L409: "último día en que puede cortarse una ola de cartera o apagarse la plataforma"). Los criterios de 1.7.6 y 1.7.12 tampoco dicen que ninguna ola cae en congelamiento (sí lo dice 1.7.11).
- Además, 1.7.6 y 1.7.12 terminan en M21 mientras el último corte puede ocurrir en M22 antes del 15-oct (sd-07 L658); el cronograma del propio T-14 sitúa la migración final en M21 y el retiro en M22, lo que es coherente con "migrada a más tardar en M22" pero conviene decirlo.
- Sugerencia: en 1.7.6/1.7.12 agregar "ninguna ola, corte ni apagado se ejecuta dentro de un congelamiento; último corte antes del 15-oct-2028"; en 1.7.9 "apagado antes del 31-oct-2028"; en el ancla M22 reemplazar "Objetivo interno" por "Límite: último corte antes del 15-oct-2028 y apagado antes del 31-oct-2028 (congelamiento desde el 1-nov)". Estado: confirmado.

**M2. Cuenta 1.7.3: "Corte de inventario" en ventana casi totalmente congelada.**
- Ubicación: L332: ventana 11-15 (nov 2027 a mar 2028), hito H7.
- Problema: M11 y M12 están dentro del congelamiento 1-nov a 6-ene; M13 contiene el 1-6 ene y la última semana de enero; M14 (febrero) está dentro del congelamiento de la última semana de enero a la primera de marzo; M15 contiene la primera semana de marzo. Solo quedan libres del 7 al ~24 de enero y del ~8 al 31 de marzo de 2028. El criterio no declara dónde cae el corte ni que respeta congelamientos (sí lo hace 1.7.11).
- Sugerencia: acotar el criterio ("el corte de cada instalación se ejecuta fuera de congelamientos; preparación y conciliación pueden continuar") o fijar la fecha del corte en las ventanas libres. Estado: por confirmar (si "corte" es solo conteo físico y no intervención de sistemas, no aplica).

**M3. Hitos H6 y H11 sin ninguna cuenta asociada.**
- Ubicación: ninguna fila del diccionario (L112-557) usa H6 (mes 13) ni H11 (mes 19); sí aparecen en las anclas (L777, L783) y en la Tabla 7.6 del sd-07 (inicio de marcha blanca con reversión activa).
- Los otros diez hitos tienen entre 5 y 42 cuentas. Un hito de pago (E-25) sin entregable en la EDT rompe la trazabilidad hito-entregable.
- Sugerencia: asociar H6 a 1.11.1 (plan de implantación y reversión activo) y a 1.12.1, y H11 a 1.12.4 y 1.11.3, o declarar qué cuenta respalda cada uno. Estado: confirmado que no hay cuentas; por confirmar a cuál asignar.

**M4. Columna "Hito asociado" con texto que no es un hito (4 cuentas).**
- Ubicación: L118 (1.1.7), L477 (1.12.7), L501 (1.13.4), L525 (1.14.3): "Entrega inicial antes de uso; controles periódicos hasta fin de ventana". También se repite en el cronograma. Además "H12 y pagos mensuales de Operación" (L338-339, 524, 527-528, 550-555) mezcla un hito con una regla de pago, y 1.7.9 (M22) y 1.7.10 (M21-56) quedan atadas a H12 aunque ocurren después de M21.
- Sugerencia: poner el hito real más cercano (p. ej. 1.1.7 a H3, 1.12.7 a H7/H12, 1.13.4 a H7/H12, 1.14.3 a H5/H12) y dejar la regla de pago en otra columna o nota. Estado: confirmado.

**M5. Roles responsables que no existen en el equipo del sd-01.**
- Ubicación: L144-149 (Líder Funcional), L232-282 (Líder de Desarrollo), L303-309 (Líder de Integración), L447-450 (Líder de Implantación), L498-502 (Líder de Gestión del Cambio), L471-477 (1.12 con Jefe de Proyecto).
- sd-01 (L180-199) define 16 personas con Jefe de Proyecto, Arquitecto de Solución con 2 Ingenieros de Solución/Desarrollo, Encargado de Seguridad, Líder de Datos, Líder de Calidad, Líder de Operación y un único "Líder de Implantación y Gestión del Cambio"; no existen Líder Funcional, Líder de Desarrollo ni Líder de Integración. El sd-07 Tabla 7.1 usa Líder Funcional, Desarrollo e Integración (así que sd-07 y T-14 coinciden entre sí), pero para 1.11, 1.12 y 1.13 el sd-07 asigna "Líder de Implantación y Gestión del Cambio", mientras el T-14 usa "Líder de Implantación" (1.11), "Líder de Gestión del Cambio" (1.13) y "Jefe de Proyecto" (1.12).
- Sugerencia: unificar con sd-01 (rol único Líder de Implantación y Gestión del Cambio para 1.11-1.13, o corregir el sd-01) y declarar a qué cargo del organigrama corresponden Líder Funcional/Desarrollo/Integración (¿Arquitecto de Solución?). Estado: confirmado para 1.11-1.13; por confirmar para Funcional/Desarrollo/Integración.

**M6. Remisión equivocada a la Figura 7.3.**
- Ubicación: L750 y L754 ("Figura 7.3: Carta Gantt de los 56 meses"). En el sd-07 la Figura 7.3 es la EDT de la rama 1.2 (sd-07 L196) y la carta Gantt es la Figura 7.18 (sd-07 L669). Mismo archivo `sd07-73-gantt.png`.
- Sugerencia: llamarla Figura 7.18 o usar numeración propia del formulario. Estado: confirmado.

**M7. Las anclas del Gantt no muestran explícitamente las ventanas de marcha blanca ni la producción.**
- Ubicación: tabla L769-788. Bases L2298 exigen "mostrar explícitamente las ventanas de marcha blanca, los pasos a producción y el inicio de la fase de Operación". La tabla da rangos para desarrollo E1 (1-12), desarrollo E2 (13-18) y Operación (21-56), pero no hay filas "Marcha blanca E1 M13-15 (ene-mar 2028)", "Marcha blanca E2 M19-20 (jul-ago 2028)" ni "Etapa 1 en producción desde M16". Solo hay los hitos de inicio (H6, H11) y de producción (H7, H12). La figura (no revisable en texto) probablemente sí las dibuja. Orden de filas también desordenado (13-18 listado después de 16).
- Sugerencia: agregar dos filas de marcha blanca y una de producción E1 y reordenar por mes. Estado: confirmado (por confirmar si la imagen las muestra).

**M8. Los congelamientos no figuran en el Gantt ni en las anclas.**
- Ubicación: L748 solo dice que "la fecha real obliga a comprobar nuevamente los congelamientos" y remite a una cita del Caso. No hay fila ni nota con las ventanas (1-nov a 6-ene; última semana de enero a primera de marzo; segunda semana de mayo; evento anual) y su traslape con M11-15, M17-18, M23-24. La cuenta 1.1.5 produce el calendario, pero el formulario no lo muestra. La regla "ninguna intervención productiva en congelamiento" aparece solo en 1.7.11, 1.11.2, 1.11.4 y el párrafo de L563.
- Sugerencia: añadir un cuadro de congelamientos con meses afectados y la declaración de que M16, M21 y M22 (hasta el 31-oct) quedan fuera. Estado: confirmado.

**M9. "Ámbito de imputación" no distingue etapa en 134 cuentas.**
- Ubicación: columna 4 del cronograma (L578-741): 134 cuentas dicen "por tramo", 19 "transversal", 6 "operación", 4 "E2 y operación" y 1 "E1 y operación". Cuentas claramente E2 (1.5.5 a 1.5.7, 1.5.13 a 1.5.34) y E1 (1.5.1, 1.5.8 etc.) tienen el mismo valor, por lo que no se sabe a qué etapa se imputan las HH para T-15 ("T-15 asigna el esfuerzo E2 únicamente desde M13", sd-07 L529).
- Sugerencia: reemplazar "por tramo" por E1 / E2 / E1 y E2 y revisar contra T-15. Estado: por confirmar (contrastar con T-15).

**M10. Prueba de corte de enlace de 24 h sin la exclusión del evento anual.**
- Ubicación: L398 (1.9.9, ventana 6-7). El criterio no dice que la prueba cae fuera de la semana previa y de los tres días del evento anual (verdad_proyecto; sd-03 L300). M6 es junio de 2027, mes en que puede caer el evento. 1.11.4 (L450) dice "fuera de congelamientos" pero no menciona el evento.
- Sugerencia: añadir la cláusula al criterio de 1.9.9. Estado: confirmado.

**M11. Retiro del sistema central de 2009 sin fecha ni regla de congelamiento.**
- Ubicación: L339 (1.7.10, ventana 21-56, "H12 y pagos mensuales"). La ventana de 36 meses atraviesa todos los congelamientos y el criterio no los excluye ni fija una fecha tope; el ADR-01 describe un retiro por olas.
- Sugerencia: definir olas o fecha objetivo y la cláusula "fuera de congelamientos". Estado: por confirmar.

### Bajas

**B1.** L177 y otros: "380 cajas, 640 terminales"; el glosario y el Caso hablan de 380 líneas de caja (RT-05.29 del Caso). Corregir a "380 líneas de caja". Confirmado.

**B2.** L145: "620.000 clientes"; la cifra del Caso es 620.000 clientes con saldo (1.380.000 tarjetas emitidas). Precisar. Confirmado.

**B3.** L331: "discrepancia ≤ 2 %"; el Caso (L350) dice "bajo 2 %". Alinear el umbral (< 2 %). Por confirmar si el criterio de aceptación se endurece.

**B4.** L121 y L112: 1.1.10 "aprobada al inicio del mes 1" asociada a H1 (mes 2), cuando H1 es el hito de levantamiento y línea base (sd-07 Tabla 7.6). Asociar al hito que corresponda. Por confirmar.

**B5.** Referencias "Anexo B" sin indicar el subdocumento (L232-282, 203, 393, 550): el Anexo B del sd-03 es el catálogo de requerimientos; los SLO y SLA (art. 78) no están ahí. Escribir "Anexo B del Subdocumento 3" y remitir los SLA al sd-10/T-9 o al artículo 78 según corresponda. Por confirmar.

**B6.** L202 (1.4.4) y 1.4.5 mezclan "SLO del Anexo B" con alertas; 1.9.4 (L393) no cita la carga a 1,5 veces el peak (RT-09.06; RNF-22). Añadir el umbral al criterio. Confirmado.

**B7.** L101 etc.: títulos de tabla como "Tabla: ..." en texto plano y rotulado "Fuente: Elaboración propia" (formato, sin impacto de contenido).

**B8.** L788 vs L748: texto del Gantt dice que dibuja "las cinco innovaciones" y las anclas no listan M21 como inicio de habilitación de innovaciones E2 (solo en 1.10.x). Opcional.

## 3. Verificación específica solicitada

- **Regla del 100 % de la EDT:** satisfecha a nivel de cuentas (164) y por rama; no verificable bajo la cuenta en 1.5 y 1.10 por G1/G2.
- **Sumas de horas:** cuadran en todas las ramas y en el total (40.946; 12.116 + 28.830; 31.058 + 9.888). Sin discrepancias.
- **Hitos con los meses del sd-07:** coinciden los 12; H6 y H11 no tienen cuentas (M3).
- **Ventanas de congelamiento:** ningún paso a producción ni ola/corte de cartera declarado cae en congelamiento (M16, M21, M22 antes del 31-oct). Riesgo abierto: 1.7.3 (M2) y 1.7.10 (M11) sin cláusula, y 1.7.6 sin cláusula (M1).
- **Fecha de cartera:** el formulario no la declara completa (M1). Los meses (migración hasta M21, retiro M22, cierre de remediación M24) son coherentes con sd-03/sd-07.
- **Definición oficial (Bases L2296-2298):** carta Gantt de 56 meses presente; marchas blancas explícitas solo vía hitos (M7).
