# Ficha del sd-08 (Plan de riesgos)

Documento de contexto, no es entregable. Creado el 2026-10-10. Manda `02_Propuesta/latex_final/sd-08/sd-08.tex`. Si esta ficha difiere, está desactualizada.

## 1. Plazo y forma de trabajo

- Entrega: lunes 12-10-2026, 08:00.
- Paso a paso como en el sd-03: sugerencia del asistente, decisión del usuario, control al cierre de cada fase.
- Sin commits ni publicación salvo que el usuario lo pida.

| Fase | Contenido | Control del usuario |
| :-- | :-- | :-- |
| F0 | Esta ficha | Fuentes vigentes |
| F1 | Registro de riesgos candidatos (`registro_candidatos.md`) | Valida la lista |
| F2 | 8.1 Plan de riesgos: enfoque, roles, escalas, matriz, ciclo | Aprueba escalas y umbrales |
| F3 | 8.2 cualitativo: calificación, RBS, matriz | Revisa calificaciones |
| F4 | 8.2 cuantitativo: Monte Carlo + FMEA | Aprueba supuestos |
| F5 | 8.3 Plan de acción y reservas | Aprueba estrategias y reservas |
| F6 | Introducción, T-16, referencias, IA, verificación, PDF | Revisión final |

## 2. Estructura obligatoria (Comunicado 10, l. 836-875)

- Introducción: resumen del capítulo y conexión con capítulos, anexos y formularios.
- 8.1: enfoque de gestión, roles, escalas de probabilidad e impacto, ciclo de revisión.
- 8.2: RBS; riesgos técnicos, organizacionales, de proyecto, de seguridad y de operación; obsolescencia, bloqueo por proveedor, escalabilidad, ciberseguridad y disponibilidad de contrapartes del cliente; análisis cualitativo y cuantitativo.
- 8.3: mitigación con costo-beneficio, responsable, plazo y disparador; reservas de contingencia y de gestión y su reflejo en el cronograma.
- Anexo: Formulario T-16 (texto ilegible en las Bases; se construye con FEP04 · 21 y se marca para confirmar).
- Regla: riesgos de la solución propuesta, no un catálogo genérico.

## 3. Lo que exigen además el Caso y las Bases

- **Caso cap. 17, ítem «Plan de riesgos»:** seis riesgos esperados. Divergencia de saldos en la migración de la cartera, evento anual con la solución a medio desplegar, cruce de datos indebido entre ámbitos, integración no documentada que aparece en producción, rotación del 62 % que borra la capacitación, vendedor cuya remuneración compite con el proceso.
- **Caso cap. 11:** lo excluido genera dependencias que deben estar en el plan y en el riesgo.
- **Bases Admin. Informe 2 (l. 2444):** análisis de riesgo de la solución, del desarrollo del proyecto y de la implantación.
- **Art. 50.2:** sin precios ni cifras que permitan inferir el monto. Prevalece sobre la clase.
- **sd-06 (l. 239-243):** ISO 31000, registro vivo revisado en cada Comité de Proyecto (quincenal), cada riesgo con responsable, disparador, respuesta y plazo, respuestas que tocan línea base van a control integrado de cambios. Comités: Ejecutivo mensual (riesgos mayores), Proyecto quincenal, Arquitectura mensual (riesgos técnicos), Operación mensual desde el mes 13.

## 4. Unidades decididas (FEP04 · 6-9, 46-53, ajustadas a Art. 50.2)

- Probabilidad: cinco niveles en porcentaje (FEP04 · 7).
- Impacto en plazo: semanas, medido contra los hitos fijos de los meses 16 y 21 y las fechas 13.2, no contra el plazo total.
- Impacto en esfuerzo: horas-persona, la unidad de la estimación del sd-07.
- Impacto en costo: porcentaje del costo directo, sin pesos.
- Impacto en alcance, calidad y operación: escala cualitativa de FEP04 · 7 y nivel de servicio (disponibilidad, RTO/RPO, autonomía de 24 h).
- Exposición = P × I normalizado; zonas crítica, alta, media y baja con las reglas de FEP04 · 8.
- Valor esperado en horas-persona; reserva de contingencia = suma de los valores esperados, en horas y en semanas de colchón antes de cada hito (P80, FEP04 · 53). Reserva de gestión: solo el concepto y quién la libera (FEP04 · 49); su valor va al Sobre 3.
- FMEA: severidad, ocurrencia y detección de 1 a 10 y NPR, para los modos de falla de la solución en operación.

## 5. Dependencias abiertas

- sd-05 lo escribe Manuel y aún está vacío. Los riesgos de datos y migración se apoyan en el sd-03 y el sd-04 y se marcan «a conciliar con sd-05».
- Riesgos de adopción de las innovaciones: viven en el sd-13. El sd-08 los cita y no los duplica.
- Los `.tex` del sd-01, sd-02 y sd-06 cambiaron a `SUBDOCUMENTO N.tex`. Se comprueba con `exportar_latex.py doctor` en la F6, sin tocarlos.
