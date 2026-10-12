# Relevo de sesión del sd-08 (2026-10-12)

Documento de contexto, no entregable. Sustituye al relevo del 2026-10-11 como punto de partida. Si difiere de los archivos que cita, mandan los archivos.

## 1. Estado

- **`02_Propuesta/latex_final/sd-08/OSS-Subdocumento8.tex`:** redactado completo como borrador. Introducción, 8.1, 8.2 (cualitativo y cuantitativo), 8.3, Anexo A (registro, Formulario T-16), Referencias y Declaración de uso de IA.
- **Verificación:** `verificar` ok; `verificar-redaccion` con 0 errores y 8 avisos, todos del anexo (tres tablas de 37 filas, títulos «Tabla A.N» que el verificador no reconoce y anexo casi todo tablas).
- **PDF:** `05_Gestion/reportes/vistas_previas/T7-08_latex_preview.pdf`, 26 páginas. Se revisaron a la vista las páginas 5 a 9 y 12 a 16 de una compilación anterior; el resto (8.1, final del 8.3, anexo y Referencias) no se ha mirado.
- **Maestro:** ruta del `.tex` y estado «Borrador, sin revisión humana». Nadie asignó «revisado».
- **Nada está en git:** todo lo de esta sesión está sin commit (ver sección 6).

Compilar con `py -3.12 05_Gestion/scripts/exportar_latex.py ...`. El `python` del PATH de esta máquina es el de Inkscape y no tiene `pypdf`.

## 2. Decisiones tomadas por el usuario (2026-10-11 y 2026-10-12)

| N.º | Resultado |
| :-- | :-- |
| D1 | Opción A: 37 riesgos y 8 oportunidades en el registro y el T-16; fichas en el cuerpo solo de críticos, altos y los 11 exigidos |
| D2 | EXT se funde en PRO (cinco ramas) |
| D3 | Ocho oportunidades (O-01 a O-08); cuatro desarrolladas (O-02, O-03, O-05, O-06). Descartadas las candidatas de innovaciones y nube |
| D4 | SUP-26: inicio en enero de 2027 |
| D5 | Se fusionan R-01+R-26 y R-23+R-39; R-21 y R-37 separados |
| D6 | El recinto on-premise es del cliente; R-31 es riesgo de contraparte |
| D7 | Peak: 104.000 real, 150.000 proyectado, 225.000 de prueba |
| D8 | 14 tiendas sin enlace de respaldo (7 acreditadas) |
| D9 | Reserva en el 8.3 y una frase en el sd-07 (grado 1) |
| D10 | Cuatro cuentas nuevas se agregan al sd-07 (falta hacerlo) |
| Escalas | Rangos y zonas de la clase FEP04 · 7-9; P = punto medio del rango; I = 0,05 a 0,80 (decisión del equipo) |
| Regla del hito | Estricta: todo riesgo que atrasa la ruta crítica tiene impacto Muy alto |

## 3. Resultados que el capítulo afirma

- Zonas: 3 críticos (R-02, R-12, R-13), 11 altos, 21 medios, 2 bajos.
- Valor esperado de los 14 críticos y altos: 29,2 semanas y 6.496 horas; con respuestas, 3.688 horas (reducción de 43 %).
- FMEA: NPR 144 (R-16), 120 (R-15), 112 (R-09), 60 (R-03), 36 (R-31).
- Simulación (10.000 iteraciones, semilla 20261012, caso base solapado, con respuestas): P80 de 12,5 semanas en el mes 16, 1,7 en el mes 21 y 8,5 en el mes 22. Cota en serie: 15,3, 1,7 y 10,0.

**Todo esto son estimaciones generadas por agentes**: probabilidades, impactos, semanas, horas, puntajes del FMEA y asignación de riesgos a eslabones. Falta la revisión humana.

## 4. Hallazgos del evaluador que siguen abiertos

Evaluación de `evaluador-pmbok` (Sonnet) del 2026-10-12. Se corrigieron dos (residual de R-02, que queda en 0,32 y zona alta, y redacción de R-13). Quedan:

1. **La reserva no cuadra con el sd-07.** 12,5 semanas antes del mes 16 es 19 % de la Etapa 1, y el sd-07 declara holgura cero y no tiene fechas internas. O el sd-07 muestra el cronograma interno (grado 2 de D9), o se revisan las estimaciones de semanas para bajar la reserva. Es el hallazgo más grave.
2. **Falta el costo de las acciones.** El 8.3 mide la reducción del valor esperado, pero no las horas de ejecutar cada acción, así que no hay relación beneficio/esfuerzo. Requiere estimar horas por acción.
3. **Contradicción con el sd-07 l. 273** sobre la marcha blanca y el congelamiento (I-03). Se resuelve en el sd-07.
4. **Acciones sin cuenta o sin dueño.** R-33 apunta a «Nivelación (T-15)», que no es una cuenta; R-36 tiene responsable «por definir con el sd-12»; las cuentas de R-06, R-27, R-28 y R-36 son solo propuestas.
5. **FMEA sin tabla de conversión.** La severidad no sigue de forma uniforme al impacto, y la detección de R-16 se describe como tardía con un puntaje menor que el de R-15.
6. **Forma.** Las Tablas A.3, 8.2 y 8.9 tienen frases completas en las celdas; no hay riesgos secundarios ni plan de reversa declarados (FEP04 · 64).
7. **La frase «once altos a zona media»** del 8.3 debe releerse tras el cambio de R-02 (R-02 es crítico y ahora queda alto; los once altos no cambiaron).

## 5. Pendientes fuera del sd-08

- `guia_cuentas_nuevas_sd-07.md`: cuatro cuentas de control nuevas y la frase de D9 en el 7.3.
- `cambios_por_D4_D8.md` y `cambios_por_D6.md`: correcciones en sd-02, sd-03, sd-04, sd-07 y la EDT.
- `citas_sd-08.md`: 19 folios ubicados en el índice y el OCR; ninguno comprobado en el PDF visible.
- Formulario T-16 en `.docx`: no existe; el registro va como Anexo A del `.tex`, con estructura por confirmar.
- Skill `humanizer` (RR-24): no se aplicó; no estaba disponible.
- `check.py --parte T7-08`: falta el registro de uso de IA de 8.2 y 8.3 en el maestro.
- Suite de pruebas: 238 pruebas, 2 fallos y 1 error en `test_redaccion` (RR-20), `test_prism` (manifiesto) y `test_compilar_humo` (T7-14). Son archivos que esta sesión no tocó; no se comprobó si fallaban antes.

## 6. Archivos de la sesión (sin commit)

- `.tex` del sd-08, maestro del sd-08, `avisos_otros_subdocumentos.md`.
- Figuras: `04_Adjuntos/diagramas/diag-08-0{0,1,2}*` y copias PDF en `02_Propuesta/latex_final/figuras/`.
- Simulación: `05_Gestion/scripts/simular_riesgos_cronograma.py` y su prueba.
- Contexto en `80_Artefactos/sd-08_contexto/`: `registro_final.md`, `calificacion.md`, `escalas_propuestas.md`, `cuantitativo.md`, `citas_sd-08.md`, `cambios_por_*.md`, `guia_cuentas_nuevas_sd-07.md`, `guia_progreso_sd-08.md`, `fragmentos/` y los dos relevos.
- No se tocaron `.opencode/skills/*` ni `tmp/`, que ya estaban modificados.

## 7. Siguiente paso sugerido

1. Revisión humana de `calificacion.md` (columna de semanas y horas) y decisión sobre la reserva (hallazgo 1).
2. Leer el PDF completo, en particular las páginas no revisadas.
3. Commit y push de `work`.
