# Relevo de sesión del sd-08 (2026-10-11)

Documento de contexto, no entregable. Sirve para retomar el sd-08 desde otra cuenta o dispositivo sin depender del historial de la conversación. Si difiere de los archivos que cita, mandan los archivos.

## 1. Cómo retomar

1. Estar en la rama `work` y traer lo último: `git checkout work && git pull`.
2. Leer, en este orden: `ficha_sd-08.md` (plazo y fases), `guia_progreso_sd-08.md` (estado, exigencias y decisiones), este relevo.
3. El contenido se redacta en `02_Propuesta/latex_final/sd-08/OSS-Subdocumento8.tex` (hoy solo esqueleto). Reglas de exportación y redacción: `AGENTS.md`. Skills de redacción: `.agents/skills/redactar-seccion`.
4. Las skills `risk-assessment` y `legal-risk-assessment` de `.opencode/skills/` son genéricas y de OpenCode; para este capítulo sirven más el material FEP04 de `90_Referencia/clases markdown/` y el agente `evaluador-pmbok`.

## 2. Qué se hizo en esta sesión

- **Fusión de `main` en `work`** (commit `11f4002`). Conflictos resueltos:
  - `02_Propuesta/latex_final/sd-01.tex` quedó reemplazado por `sd-01/OSS-Subdocumento1.tex` (decisión de `main`). El cambio que `work` tenía sobre la tabla de alianzas (carta de compromiso del socio de Microsoft) no se trasladó porque esa tabla ya no existe en el archivo nuevo. **Pendiente: que alguien confirme que no falta.**
  - `80_Artefactos/sd-04_contexto/contexto_sd-04.md`: se combinaron ambos lados. La fila del stack tecnológico informado por el usuario pasó de D-12 a **D-15** (D-12 de `main` es la decisión de Azure como nube definitiva), y la sección 3 «Stack tecnológico» pasó a 4.
- **Investigación del estado del sd-08** frente al Comunicado 10 (l. 836-875) y las Bases (l. 2154-2164, T-16 en l. 2314, T-21 ilegible).
- **Guía de progreso** en `guia_progreso_sd-08.md`: estado, tabla de exigencias con línea de fuente, diez decisiones, fases F1b a F6, plan corto.
- **Sondeo de las diez decisiones** contra los demás subdocumentos (dos agentes). Resultado en la sección 3.

## 3. Estado de las decisiones (2026-10-11)

El usuario aún no respondió ninguna. Los veredictos salen de lo que ya dicen los documentos.

| N.º | Decisión | Estado | Dato clave |
| :-- | :-- | :-- | :-- |
| D4 | SUP-26: inicio en enero de 2027 | Tomada implícitamente; **falta que el usuario la ratifique** | sd-02 Anexos l. 3325, sd-03 l. 234, sd-07 l. 249 la usan. Su texto dice que debe confirmarse con el cliente. Afecta R-12, R-13, R-24 y R-25 |
| D8 | Tiendas sin enlace de respaldo | Tomada implícitamente: 14 | sd-02 SUP-28 (l. 745) y sd-04 (l. 417). Residuo: tabla de sd-02 l. 497 dice «7 de 15» |
| D2 | EXT como rama propia de la RBS | Abierta | Sugerencia: sí, con sub-ramas normativo y terceros |
| D3 | Oportunidades O-01 y O-02 | Abierta | Sugerencia: sí |
| D5 | Fusiones R-01+R-26, R-21+R-37, R-23+R-39 | A medias | La ampliación de R-12 ya está decidida (I-03, 2026-10-10). Faltan las tres fusiones |
| D1 | Cuántos riesgos entran | Abierta | Sugerencia: 36 en registro y T-16; en el cuerpo del 8.2 solo críticos, altos y los 11 exigidos |
| D10 | Cuatro cuentas nuevas de la EDT (R-06, R-27, R-28, R-36) | Abierta | No existen en `14_edt_corregida.md` ni en el diccionario |
| D9 | Holgura del evento anual | Abierta | sd-07 l. 277 dice que la ruta crítica «no admite holgura». Depende del cálculo cuantitativo (F4) |
| D7 | Volumen del peak | Abierta | Cuatro versiones: 114.520 (sd-02), «120 % del peak proyectado» (RNF-22 y Anexo B), 104.000 (Anexo D 25), «1,5 veces el peak declarado» sin cifra (sd-06 y sd-07). Sugerencia: 225.000 en tres días |
| D6 | Quién provee el centro de datos on-premise | Contradictoria | Auditoría sd01-04 EXT-M-03 y sd-03/EDT: el proponente. sd-04 Tabla 4.11 (l. 575): el cliente. DC-02 en la misma comuna sin decisión |

### Orden acordado para revisarlas, de más fácil a más difícil

D4 → D8 → D2 → D3 → D5 → D1 → D10 → D9 → D7 → D6.
D2, D3, D5 y D1 bloquean empezar a redactar. D6 y D7 solo bloquean la calificación de R-31 y R-09.

**Punto exacto donde quedó la conversación:** se había descrito SUP-26 y se preguntaba si se ratificaba D4 para pasar a D8. Sin respuesta.

## 4. Siguiente paso concreto

1. Que el usuario responda D4 y siga con D8, D2, D3, D5 y D1 (cinco respuestas cortas).
2. Con eso, ejecutar F1b: dejar el registro final de riesgos (con fusiones aplicadas) y pasar a F2 (8.1 Plan de riesgos).
3. Plazo de la ficha: **lunes 12-10-2026, 08:00**. Confirmar con el equipo si sigue vigente; si lo está, aplicar el plan corto de la sección 6 de la guía.

## 5. Estado del repositorio al cierre

- Rama `work`, con la fusión de `main` ya confirmada localmente (`11f4002`).
- Archivos nuevos de esta sesión, **sin confirmar** hasta que alguien haga commit: `guia_progreso_sd-08.md` y este relevo.
- Cambios sin preparar que no son de esta sesión y no se tocaron: `.opencode/skills/redactar-seccion/SKILL.md`, `.opencode/skills/revisar-seccion/SKILL.md`, y la carpeta `tmp/`.
- La rama local iba adelantada de `origin/work`. Para seguir desde otro dispositivo hay que hacer `git push` de `work` después de confirmar estos archivos.

## 6. Avisos a otros subdocumentos que siguen vivos

Detalle en `avisos_otros_subdocumentos.md`. Los más relevantes para el sd-08:

- **sd-07 l. 273:** afirma que la marcha blanca de la Etapa 1 cabe dentro del congelamiento (I-03). El sd-08 la trata como R-12 en zona crítica.
- **sd-02 l. 497:** corregir «7 de 15» a la cifra de 14 (D8).
- **sd-04 Tabla 4.11:** alinear con lo que decida D6.
- **Excel de requerimientos v3.1, criterio 9:** sigue en «0,5 % o menos»; manda «menos de 3 %» (I-04).
- **sd-05, sd-13:** el sd-05 sigue como esqueleto; el sd-13 tiene borradores `.md` pero no `.tex`.
