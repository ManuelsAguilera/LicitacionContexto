> Detalle de la revisión de los formularios (2026-10-12). Borrador. **Nota:** cualquier hallazgo que diga que el Comité de Operación debe iniciar en el mes 16 es un falso positivo: el artículo 71 de las Bases fija «mensual desde el mes 13».

# Revisión Formulario T-15 (nivelación de recursos)

Archivo: `02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-15.tex` (716 líneas). Contrastado con Bases Admin. l. 2300-2316, Bases Transversales cap. 15 (l. 654-678), sd-07, T-14, sd-01, sd-08, T-9, T-12.

## Verificaciones aritméticas que CUADRAN (sin hallazgo)
- Suma de ramas (Tabla 2, l. 183-198) = 40.946; 159 cuentas no innovación = 31.058 (= 12.116 + 18.942) + 9.888 innovación = 40.946. T-14 por rama coincide exacto (recalculado desde las 164 cuentas de T-14).
- 127 paquetes de software (l. 214-340) suman 12.116 y, agrupados por cuenta, igualan las HH de cada una de las 51 cuentas 1.5.x de T-14 (0 diferencias).
- Curva mensual (Tabla 3, l. 367-422): 56 meses; suma de columnas = 18.074,92 / 12.415,02 / 2.392,05 / 8.064,20 = 40.946,19 (el redondeo a dos decimales explica 0,19 HH, ya declarado en l. 105). Total mensual (l. 432-487) cuadra fila a fila (tolerancia 0,01) y suma 40.945,9.
- Hijas de la Tabla "Resumen por etapa": E1 desarrollo (M1-12) 17.080,05, MB E1 606,33, E2 desarrollo 11.403,46, MB E2 975,56, operación = 8.064,20 + transversal M21-56 1.278,84 = 9.343,04; más 388,54 (E1 M16-20) + 36 (acta H12 M21) + 1.113,21 (transversal M1-20) = 40.946. Cuadra (diferencias de centésimas).
- Tabla 4 (solapamientos): M13-15 y M19-20 recalculadas, cuadran.
- Máximos: 2.492,78 HH en M16 y 364,63 en M22 (= 15,58 y 2,28 personas equivalentes a 160 HH); coincide con sd-07 (l. 531 y 652). Equivalencias por tramo (12,04; 1,26; 14,30; 3,20; 2,28) correctas.
- Los primeros meses reconstruidos desde T-14 (reparto uniforme de ventanas) reproducen exactamente M1=1.184,86, M2=1.615,03, M4=1.970,71. Transversal M56 = 127,52 se explica por 1.14.5 (32) + 1.14.6 lecciones aprendidas (47, solo M56) + base 48,52.
- CPM: 57 nodos (18 + 35 + 1 compuerta + 3 retiro/transferencia) y 120 relaciones, coherente con sd-07 l. 604 y T-14 l. 795; duraciones y ES-EF/LS-LF/HT de las tablas son internamente coherentes; H7 t=15, H12 t=20, Z t=56 correctos. 15 % + 30 % + 55 % y 85 % (l. 111) aritméticamente correctos.
- 16 personas del sd-01 = 1 + 3 + 2 + 3 + 3 + 2 + 2; siete roles de jefatura y seis áreas de trabajo. Verificado en sd-01 l. 183-199 y 315-330.

## Hallazgos

### GRAVES

**G-1. La reserva de riesgos de 3.688 h no aparece en el T-15, pese a que el sd-08 dice que el T-15 la asigna.**
- Ubicación: T-15 completo (grep "3.688" = 0 resultados; l. 117 habla solo de "40.946 HH incluidas las innovaciones"). Fuente: sd-08 `OnlySimpleSolutions-Subdocumento8.tex` l. 545 ("3.688 horas ... se suman a las 40.946 horas hombre de trabajo base del Formulario T-15, para un esfuerzo comprometido de 44.634"), l. 547 ("La reserva es capacidad de trabajo adicional, asignada por frente y ventana en el Formulario T-15") y l. 549 ("El Formulario T-15 la separa en cuatro frentes para evitar doble conteo").
- Qué debería decir: una tabla/apartado "Reserva de contingencia" con las 3.688 h separadas en los cuatro frentes y ventanas citados, la suma 40.946 + 3.688 = 44.634 y la aclaración de que no duplica las reservas de capacidad del 15 %/30 %.
- Sugerencia: añadir el apartado (o corregir el sd-08 para que no remita al T-15). Si no, la remisión es inexistente y el compromiso de 44.634 h no se puede rastrear. Estado: confirmado. Los "cuatro frentes" no están definidos en ninguna parte revisada: por confirmar con el autor del sd-08.

**G-2. No se declara el número de personas, ni la dotación por rol ni las dedicaciones: el requisito de las Bases queda cubierto solo con "equivalentes" y con una remisión a un subdocumento aún no entregado.**
- Ubicación: l. 141, 117, 490-494, 148-152. Fuente: Bases Admin. l. 2305-2306 ("Número de personas involucradas en las distintas actividades durante la implementación y durante la operación"); sd-07 l. 531-537 delega "conciliación por equipo, rol e intervalo" al T-15; T-15 la delega al sd-12/SD-10 (que no existen todavía en `latex_final`).
- Qué dice: "La dotación nominal máxima por roles y turnos está pendiente de conciliación con el Subdocumento 12" y "se complementa con la asignación nominal por equipo y rol antes de comprometer la ejecución". sd-07 y T-15 se remiten uno al otro: ninguno contiene la tabla rol x intervalo (HH por rol, dedicación, personas). No hay "Tabla 7.1 de roles" con HH por rol.
- Debería: tabla rol/área x etapa (E1 desarrollo, MB E1, E2 desarrollo, MB E2, operación) con HH, % de dedicación y personas, que sume 40.946; o al menos número de personas por tramo coherente con los 16 del sd-01.
- Estado: confirmado (incumplimiento de la definición oficial del formulario).

**G-3. La capacidad del equipo del sd-01 (16 personas) no cubre el pico y deja sin espacio las reservas de 15 % y 30 %.**
- Cálculo: 16 x 160 = 2.560 HH/mes. Pico 2.492,78 (M16) = 97,4 %. Con la reserva de deuda del 15 % la capacidad usable sería 2.176 (85 %): se exceden M16 (2.492,78) y M17 (2.274,57); con 55 % (1.408) se exceden M13 (1.513,16), M14 (1.783,56) y M15 (2.349,92) si el 30 % de estabilización se aplicara al total (solo aplica a equipos en marcha blanca: ver abajo). Los meses M4-M6 (1.790-1.970) usan 70-77 %.
- Además T-15 l. 494 dice "Los techos aritméticos son 16 y 3", justamente la cifra del sd-01, sin advertir que 15,58 de 16 deja 0 margen para vacaciones, ausencias, 15 % de deuda técnica y reemplazos.
- En operación el sd-01 (l. 196) asigna solo 2 personas (Líder de Operación + Ingeniero DevOps/Soporte) para 2,28 equivalentes (364,63 HH) más mesa de servicio de tres niveles que debe cumplir SLA (T-14 1.15.1: solo 1.065 HH en 36 meses = 29,6 HH/mes, que no sostiene una mesa de tres niveles); queda la advertencia l. 494 ("no se afirma que esos techos basten"), pero el formulario no resuelve la dotación.
- Sugerencia: declarar si las 16 personas son la dotación total o solo las jefaturas/especialistas (sd-01 l. 207: "equipo de liderazgo y especialistas") y cuántos perfiles adicionales se suman; si son los 16 totales, el T-15 incumple su propia regla de reservas en M13-M17. Estado: por confirmar (depende de si hay personal adicional no listado en sd-01); la ambigüedad es en sí misma un hallazgo.

**G-4. Certificaciones individuales exigidas (Bases Transversales 15.3, RT-15.07 a RT-15.09) no están cubiertas en el T-15 ni en el sd-01.**
- Exigido (l. 665-675): PMP/PRINCE2 x2, ITIL 4 x5, COBIT x2, cloud profesional x3, seguridad (CISSP/CISM/CEH/OSCP) x2, base de datos del motor ofertado x2, ISTQB x2; personas del equipo asignado "con dedicación declarada" (RT-15.08).
- Hoy: T-15 no menciona certificaciones personales (solo "certificación" de pruebas); sd-01 no contiene ninguna de estas siglas (grep PMP/ITIL/CISSP/ISTQB/COBIT = 0 en `latex_final/sd-01`); T-12 l. 1203 afirma "equipo de jefaturas nominado con dedicación exclusiva ... certificaciones individuales (PMP, Azure Solutions Architect Expert, CISSP/CCSP, CDMP, CTAL-TM, DevOps Engineer Expert, Prosci)" y remite a "sd-01, sección 1.6 Frente de jefaturas asignado y Tabla 1", sección que no existe (1.6 es "Alianzas"; ver `auditoria_inconsistencias_sd01-04.md` l. 199). La lista de T-12 omite ITIL, COBIT y base de datos y no da cantidades (7 certificaciones distintas para 7 jefaturas no pueden sumar 2+5+2+3+2+2+2 = 18 certificaciones, ya que "no puede contarse dos veces").
- Además T-12 dice "dedicación exclusiva", mientras T-15/sd-07 no declara dedicaciones y habla de 160 HH/mes por persona-mes como hipótesis. Contradicción por conciliar.
- Sugerencia: matriz persona x certificación x dedicación (en sd-12 o en T-15) con la cantidad mínima cubierta y quién cumple cada requisito; verificar que las 16 personas alcanzan para ITIL x5 y 18 acreditaciones. Estado: confirmado que falta; la suficiencia, por confirmar.

**G-5. Los roles del plan no coinciden con los siete roles de jefatura / 16 personas del sd-01.**
- T-15 l. 203: "El Líder de Desarrollo responde por cada paquete [127]" y "el Líder de Calidad verifica"; sd-07 Tabla 7.1/7.3 y T-14 usan: Líder de Desarrollo (51 cuentas), Líder Funcional (8), Líder de Integración (7), Líder de Calidad y Pruebas, Líder de Gestión del Cambio (T-14 1.13.4) / Líder de Implantación (1.11.3) / Líder de Implantación y Gestión del Cambio (sd-07), Líder de Operación / SRE.
- sd-01 (l. 183-199, 315-330) solo tiene: Jefe de Proyecto, Arquitecto de Solución, Encargado de Seguridad, Líder de Datos, Líder de Calidad, Líder de Operación, Líder de Implantación y Gestión del Cambio; el desarrollo lo hacen "2 Ingenieros de Solución/Desarrollo" sin líder. No existen en sd-01 Líder de Desarrollo, Líder Funcional ni Líder de Integración (3 roles que son responsables de 66 cuentas y 127 paquetes). Es una contradicción de estructura de equipo (verdad_proyecto: "áreas: arquitectura, datos, seguridad, calidad, operación, gestión del cambio").
- Sugerencia: reasignar esos responsables a roles existentes (p. ej. Líder de Desarrollo -> Arquitecto de Solución o crear el rol y pasar el sd-01 a 17), o ajustar el sd-01. Estado: confirmado. Severidad grave por afectar la nivelación por rol.

### MEDIANAS

**M-1. Líder de Operación "desde el mes 6": ausente y contradicho.**
- T-9 l. 348 y l. 1642 dicen "OSS, desde el mes 6" para el Líder de Operación / SRE; sd-07 Tabla 7.3 (l. 519) y T-14 (1.15.x, ventana 21-56) lo sitúan en M21-56; T-15 no menciona al Líder de Operación ni asigna HH de operación antes de M21 (columna "Operación directa" = 0,00 en M1-M20, l. 367-386), aunque sd-01 l. 326 dice que "preparará y conducirá la operación", el Comité de Operación empieza en M16 y la prueba de corte de 24 h es en M6-M7.
- Sugerencia: reflejar en el T-15 las HH de preparación de operación desde M6 (o imputarlas a las cuentas existentes, indicando cuáles) y reconciliar ventana M21-56 vs "desde M6". Estado: por confirmar cuál es la regla; la contradicción es confirmada.

**M-2. Columna "Personas (peak)" sin método consistente.** (l. 148-152)
- E1 desarrollo 13 usa el total mensual (1.970,71 / 160 = 12,32 -> 13); E2 desarrollo 15 usa solo la columna E2 (2.288,24 / 160 = 14,30 -> 15) y omite que en M16 (dentro de M13-18) el total es 2.492,78 = 15,58 -> 16, cifra que el propio T-15 (l. 494) cita; MB E1 "3" con 202,11 HH (1,26 -> 2), mientras en M13-15 el total mensual llega a 15 personas. Debería: usar la misma base y que 15 -> 16 en E2 desarrollo; para MB E1, 2 (o explicar 3). Estado: confirmado.

**M-3. La tabla de cinco tramos no suma 40.946 sin un párrafo aparte.** (l. 143-156) Suma de filas = 39.408,27; faltan 388,55 + 36,00 + 1.113,19. Las Bases piden horas "por etapa": el lector no puede cuadrar la tabla. Añadir filas "E1 producción M16-20", "acta H12 M21" y "Transversal M1-20" o un total conciliado. Estado: confirmado.

**M-4. Referencias a figuras y archivos que no existen o con numeración ajena.**
- l. 350-354 "Figura 7.2" con imagen `prism-uploads/diag-07-03_curva-hh.png`: ese archivo no está en `latex_final/figuras/` ni existe carpeta `prism-uploads` (puede estar en Prism: por confirmar). En sd-07 la misma curva es la Figura 7.17 (l. 641) y la Figura 7.2 es una rama de la EDT (l. 172); T-14 usa Figura 7.3 para la Gantt (l. 750) frente a la 7.18 del sd-07. Numeración de figuras duplicada/ incoherente entre T-14, T-15 y sd-07.
- Sugerencia: renumerar con la serie del sd-07 o usar numeración propia del formulario. Estado: confirmado (numeración); por confirmar (archivo).

**M-5. Ubicación del anexo CPM contradictoria.** sd-07 l. 550 y 604 dicen "anexo CPM del T-14"; T-14 l. 795 dice "red de 57 nodos del cálculo CPM presentado en el T-15"; la red está en T-15 l. 526-709. Corregir la remisión en sd-07 o decidir dónde vive. Estado: confirmado.

**M-6. Horas por paquete/tarea de las 37 cuentas de otras ramas y de los 40 paquetes de innovación no aparecen.** La definición (Bases l. 2304) pide HH por "tareas, paquetes de trabajo y etapas". T-15 da las 15 ramas, 127 paquetes de software y solo nombra los 40 paquetes de innovación ("el anexo de estimación", l. 345) sin tabla ni referencia con sección o número. Sugerencia: remitir con número de anexo/sección o incluir tabla HH por paquete de innovación (suma 9.888) y por cuenta (T-14 las tiene). Estado: por confirmar si la remisión a T-14 se acepta.

**M-7. "Desde el mes 6" y Comité de Operación en otros documentos**: T-9 dice Comité de Operación "mensual desde el mes 13" (l. 400, 1293) y sd-07 l. 560 "desde M13"; la verdad vigente y sd-01 l. 339 dicen desde el mes 16. No es del T-15, pero afecta la nivelación de operación (M13-15 aún es marcha blanca). Estado: confirmado (corregir en T-9/sd-07).

**M-8. Estabilización/marcha blanca y reservas 15 %/30 %: fórmula sin evidencia numérica.** (l. 111, 115) Se enuncian las reglas y se remiten al intervalo por equipo, pero el T-15 no presenta ni un ejemplo de cálculo (HH disponibles, HH deuda, HH estabilización) para M13-15 ni M19-20. Estado: por confirmar si basta con describir el método.

### BAJAS
- B-1. l. 93-94: comentarios residuales "Anexo para insertar en un informe con el preámbulo OSS. Fuente: Anexos_capitulo_7_tex; versión integrada en FEP-FINAL" dentro del cuerpo del formulario (si se imprimen como texto, quedarían visibles). Eliminar.
- B-2. Mezcla "Subdocumento 12" (l. 107, 141) y "SD-12 / SD-10" (l. 494): unificar la forma.
- B-3. l. 107: "Las cuentas compartidas ... conciliarse con las dedicaciones del Subdocumento 12" y l. 702 "T-15 debe contrastarla con perfiles y dedicaciones": el propio T-15 se declara incompleto (relacionado con G-2). Redacción de trabajo pendiente en un texto de oferta.
- B-4. l. 345 "La instalación supone tres sitios piloto por solución física" sin referencia (Lockers, etc.). Aclarar cuál es la solución física o citar el sd-13.
- B-5. T-14 1.13.4 usa "Líder de Gestión del Cambio" (otro nombre que sd-01 y sd-07; glosario: un solo nombre).
- B-6. l. 113 y 140: "Cada tarea se vincula a una sola cuenta del T-14": no hay tareas en el T-15, solo cuentas y paquetes; usar "paquete".

## Resumen por gravedad
Grave 5 (G-1 a G-5), mediana 8 (M-1 a M-8), baja 6 (B-1 a B-6).
