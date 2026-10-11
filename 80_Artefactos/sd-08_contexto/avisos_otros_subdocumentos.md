# Avisos del sd-08 a otros subdocumentos

Notas generadas al cruzar el registro de riesgos con el resto de la propuesta (`trazabilidad_riesgos.md`). Cada aviso dice qué se encontró, qué se decidió y qué tendría que revisar el responsable. El sd-08 no edita estos `.tex`, salvo indicación expresa del usuario.

## sd-02 · I-01 · Plazo de 2029 (aplicado, 2026-10-10)

Por decisión del usuario se corrigió el párrafo de la cartera en 2.3.4 (`OSS-Subdocumento2.tex` y `sd-02.md`). El plazo pasa a ser «antes de 2029» (Caso cap. 18), con el 31-10-2028 como último día intervenible: 670 días calendario, 191 congelados, 479 intervenibles (≈ 15,7 meses). Antes decía 1.035, 317, 718 y 23,6 meses hasta octubre de 2029. Revisar si alguna figura o anexo del sd-02 repite las cifras antiguas.

## sd-07 · I-03 · Marcha blanca de la Etapa 1 dentro del congelamiento (pendiente del responsable)

**Qué dice el sd-07.** En «Paralelización y sincronización entre etapas» (l. 235) y en «Calendario y anclas del contrato» (l. 273) afirma que la marcha blanca de la Etapa 1, de enero a marzo de 2028, puede desarrollarse dentro del congelamiento porque es «operación supervisada sin cambios en producción».

**Por qué choca.** La restricción 9 del Caso (cap. 10) prohíbe intervenir sistemas desde el 1 de noviembre hasta el 6 de enero y desde la última semana de enero hasta la primera de marzo. Iniciar la marcha blanca es poner en operación sistemas nuevos, y una marcha blanca que no admite correcciones no puede cerrar los defectos que encuentre.

**Qué hace el sd-08.** Lo trata como riesgo R-12 en zona crítica, con esta respuesta:
- Certificación en Preproducción en diciembre de 2027.
- Despliegue de inicio en la ventana libre del 7 al 24 de enero de 2028.
- Correcciones en la ventana libre de marzo, antes del paso a producción de abril.
- Solo correcciones de emergencia autorizadas por el Comité Ejecutivo durante el congelamiento.

**Sugerencia para el sd-07.** Reemplazar la afirmación de que la marcha blanca «puede desarrollarse dentro de un congelamiento» por la secuencia anterior y citar el R-12 del capítulo 8. La cuenta 1.1.6 (calendario de congelamientos) y 1.12.1 (plan de la marcha blanca) deberían nombrar las dos ventanas.

## sd-03 · I-04 · Meta de precio (aplicado en el Anexo D, 2026-10-10; Excel pendiente del equipo)

Por decisión del usuario manda la meta del sd-02 (menos de 3 %, la única con cálculo: D = r·T + e, con oleadas diurnas de etiquetas de papel). Se corrigió la fila 9 del Anexo D (`04_Adjuntos/tablas/sd-03_s2_anexo-d_criterios-aceptacion.md`), que decía «0,5 % o menos». El `.tex` del sd-03 no repetía la cifra.

**Pendiente del equipo:** el Excel `01_Requerimientos/RequerimientosAtomizados_Depuracion_Alcance_v3.1.xlsx`, hoja de criterios de aceptación (sheet10, resultado 9), sigue diciendo «0,5 % o menos». El flujo no edita el Excel, así que hay que cambiarlo a mano.

## Pendientes de decidir con el usuario

- I-05 (volumen del peak, Anexo D 25 frente a RT-09.06 y Caso 14.1).
- I-06 (tiendas sin enlace de respaldo, sd-02 frente a sd-04).
- I-07 (holgura del evento anual en el sd-07).
- I-08 (innovaciones sin redactar).
- Cuentas nuevas de la EDT para R-06, R-27, R-28 y R-36.

## sd-07 · Casos de uso de control de cruces · identidad del cliente (pendiente del responsable, 2026-10-11)

**Qué dice el sd-07.** `80_Artefactos/sd-07_contexto/estimacion/03_casos_de_uso_control-cruces.md`, caso CU-CC-05: «solicitar una correspondencia de identificadores con acceso nominado» y «consultar el registro de accesos a la tabla de correspondencia».

**Qué cambió.** Por EXT-G-05 ya no existe tabla de correspondencia: cada negocio tiene su identificador y la relación solo se resuelve durante un cruce autorizado (sd-03 3.3.2, «Identidad del cliente»; sd-04 ADR-02; RF-174 y RN-04 reescritos).

**Qué revisar.** Redefinir CU-CC-05 (por ejemplo, «verificar que el cruce no deje correspondencia persistente» y «consultar la bitácora de cruces») sin cambiar el recuento de casos de uso, o recalcular el UCP si cambian las transacciones.

## sd-02 · Anexo A.4 · referencias a subdocumentos aún sin redactar (pendiente, 2026-10-11)

La columna «Sección» de la matriz A.4 se normalizó a las secciones que sí existen del sd-03 (3.3.2) y del sd-04 (4.1, 4.2, 4.3). Siguen citando secciones que dependen de cuando se redacte el sd-05 (secciones 5.5 a 5.11, hoy solo existen 5.1 a 5.4) y el sd-13 (Anexos A.1 a A.5). Hay que revisarlas al cerrar esos subdocumentos.
