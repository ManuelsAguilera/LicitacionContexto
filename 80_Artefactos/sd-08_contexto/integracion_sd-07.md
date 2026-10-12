# Integración sd-07 ↔ sd-08 (2026-10-12)

Documento de contexto, no entregable. Sirve para responder preguntas de integración entre el plan de trabajo (sd-07) y el plan de riesgos (sd-08) sin releer los dos capítulos. Si difiere de los archivos que cita, mandan los archivos.

## 1. Fuente de verdad del sd-07

- **Rama remota `origin/codex/subdoc7-formularios-entrega`**, commit `22a251a` (12-10-2026, 02:08, alexalfaro-ctrl). Por decisión del usuario, esa rama manda para el sd-07.
- **Qué se tomó de la rama:** el texto del sd-07 (idéntico al `.tex` ya importado, salvo las rutas de las cinco figuras del cronograma y tres líneas de preámbulo que la plantilla rechaza), las 16 figuras de la EDT, y como contexto los formularios T-14, T-15 y T-18, el `sd-07.md` y el README, en `80_Artefactos/entrega-sd07-2026-10-12/`.
- **Qué no se tomó:** copias de `oss.sty` y `recursos/`, los `.drawio` fuente, las cinco imágenes duplicadas y el `sd-07.tex` duplicado de esa carpeta.
- **Dónde vive en el repositorio:** `02_Propuesta/latex_final/sd-07/OSS-Subdocumento7.tex` (importado con `prism-importar --forzar`, respaldo en `latex_final/respaldo/sd-07.20261012T035738Z.tex`), figuras en `latex_final/figuras/` y `latex_final/figuras/sd07-figuras/`. Compila a 31 páginas (verificado el 2026-10-12).
- **Sin revisión humana.** El README de la rama no acredita aprobación técnica ni cierre de pendientes.

## 2. Preguntas de integración y respuesta

| Pregunta | Respuesta | Dónde |
| :-- | :-- | :-- |
| ¿La ruta crítica tiene holgura? | La cadena principal (A a F y H7; G a J y H12) tiene holgura cero. El plan de marcha blanca y la capacitación de administradores tienen 3 meses en la Etapa 1 y 1 mes en la Etapa 2. Los 35 paquetes de implementación de las innovaciones tienen holgura cero. El retiro de 2011 (M22) tiene margen cero | sd-07 7.3.3 y Tabla 7.5; T-15, «Ruta crítica (CPM) y holguras» |
| ¿Cuánto trabajo hay en total? | 40.946 HH planificadas. La base anterior sumaba 31.853 HH; las innovaciones pasan de 795 a 9.888 HH, y las otras 159 cuentas conservan 31.058 HH | T-14, nota de la estimación; figura 7.17 |
| ¿Cuántas cuentas tiene la EDT? | 164 cuentas de control en 15 ramas. El CPM tiene 57 nodos y 120 relaciones y **no cubre las 164 cuentas** | sd-07 7.1; Figura 7.19 |
| ¿Cómo se trata la marcha blanca de la Etapa 1 frente al congelamiento? | Se habilita en la ventana de M13 posterior al 6 de enero y antes del congelamiento de vuelta a clases, con H5 aceptado y retorno activo. La versión candidata se verifica en preproducción antes del 1 de noviembre de 2027 (fin de M10). No se admiten liberaciones funcionales nuevas dentro de un congelamiento | sd-07 7.3.2.1; T-18 |
| ¿Qué hitos hay? | H1 a H12 del Formulario E-25 (M2, M4, M6, M10, M12, M13, M14, M16, M17, M18, M19, M21) | sd-07 Tabla 7.6 |
| ¿Cuántas personas son el peak? | **No está calculado.** El T-15 dice «Por definir por rol» en los cinco tramos. HH/160 no es dotación real. Depende del sd-12 | T-15; README de la rama |
| ¿Qué reservas de capacidad usa el sd-07? | 15 % para deuda técnica (6.2.3.3) y 30 % más para estabilización durante una marcha blanca (6.2.7), calculados sobre la capacidad efectiva. No hay reserva de contingencia por riesgos | T-15, «Reservas de capacidad» |
| ¿Existen las cuatro cuentas de D10 (R-06, R-27, R-28, R-36)? | No hace falta: D10 se revirtió y cada acción usa una cuenta existente (R-06 1.13.1; R-27 1.2.1; R-28 1.8.5; R-36 1.6.3; R-33 1.11.3) | `guia_cuentas_nuevas_sd-07.md` (obsoleta) |
| ¿Hay un cronograma interno con fechas más tempranas que las anclas? | Parcial: la versión candidata de la Etapa 1 antes del 1 de noviembre, y las fechas internas de H4 (M10) y H5 (M12). No hay fechas internas por eslabón para una reserva de contingencia | sd-07 7.3.2.1 y 7.3.3 |

## 3. Qué significa para el sd-08

- **La reserva quedó resuelta (2026-10-12).** La reserva de contingencia deja de presentarse como margen de calendario: el P80 de la simulación (12,5 / 1,7 / 8,5 semanas en los meses 16, 21 y 22; cota en serie 15,3 / 1,7 / 10,0) es la exposición en plazo, y la reserva es de esfuerzo, 3.688 horas (valor esperado residual de los 14 riesgos críticos y altos), para recuperar atrasos agregando capacidad sin mover los hitos. D9 queda cerrada sin cambios al sd-07.
- **Ya no hay contradicción con R-12.** El sd-07 habilita la marcha blanca en la ventana posterior al 6 de enero, que es la respuesta de R-12.
- **Cifras del sd-08 que usan el sd-07:** «las horas de la estimación del apartado 7.2» (porcentajes de esfuerzo) ahora tienen como base 40.946 HH y no 31.850; el 8.3 expresa el esfuerzo en horas de riesgo, no como fracción del total, así que no cambia.
- **Renumeración de la EDT (2026-10-12):** el T-14 vigente renumeró la EDT; la Tabla 8.9 del sd-08 ya usa los códigos vigentes (equivalencia en `calificacion.md`, al final).
- **Dotación:** la reserva en horas (3.688 h de valor esperado residual) se debe contrastar con la capacidad real cuando el sd-12 y el T-15 fijen las personas.
- **Referencias del sd-08 al sd-07:** el CPM está en 7.3.3 (Tabla 7.5); los hitos, en la Tabla 7.6; las cuentas, en 7.1 y en el Formulario T-14.

## 4. Defectos conocidos del sd-07 importado

- **Títulos dentro de las imágenes:** las cinco imágenes del cronograma dicen «FIGURA 7.2» a «7.6», y el `.tex` las numera 7.17 a 7.21 (la «7.2» de la curva choca con la Figura 7.2 de la rama 1.1).
- **Gantt (Figura 7.18):** la imagen mide 2530×5910 px y en la página sale muy pequeña; el detalle no se lee en el PDF.
- **Referencias vacías:** `verificar-redaccion` marca 1 error (RR-04): «Referencias» sin contenido.
- **Seis avisos RR-19** son falsos positivos: las tablas usan `\caption` dentro de `longtable`, que el verificador no reconoce.
- **T-15 usa su versión v2 anterior**, porque no se entregó una nueva (README de la rama).

## 5. Pendientes de integración

1. Calcular el peak de personas del T-15 (sd-12) y revisar la reserva del sd-08 contra esa capacidad.
2. Regenerar las cinco imágenes del cronograma con la numeración del `.tex` y con una Gantt legible.
3. Completar «Referencias» del sd-07.
