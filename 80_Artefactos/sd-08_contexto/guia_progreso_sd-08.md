# Guía para progresar el sd-08 (Plan de riesgos)

Documento de contexto, no entregable. Creado el 2026-10-11, tras fusionar `main` en `work`. Manda `02_Propuesta/latex_final/sd-08/OSS-Subdocumento8.tex`; si esta guía difiere, está desactualizada.

## 1. Estado actual (2026-10-11)

| Pieza | Estado | Comentario |
| :-- | :-- | :-- |
| `latex_final/sd-08/OSS-Subdocumento8.tex` | Borrador completo, sin revisión humana | Introducción, 8.1 a 8.3 y anexo redactados. |
| Maestro `02_Propuesta/sd-08_plan-de-riesgos/sd-08_plan-de-riesgos.md` | Desactualizado | Dice «Sin redactar» y apunta a `latex_final/sd-08.tex`, ruta que ya no existe. |
| F0 · `ficha_sd-08.md` | Hecha | Fases, fuentes, unidades decididas (P en %, impacto en semanas y horas-persona, costo en % sin pesos). |
| F1 · `registro_candidatos.md` | Hecha, sin validar | 39 candidatos, 36 con las cuatro fusiones. Las cinco preguntas al usuario siguen abiertas. |
| `trazabilidad_riesgos.md` | Hecha | 21 OK, 2 parciales, 4 huecos en la EDT y 9 riesgos tocados por 8 inconsistencias entre subdocumentos. |
| `avisos_otros_subdocumentos.md` | Vivo | I-01 aplicado en sd-02; I-04 aplicado en el Anexo D, falta el Excel; I-03 sigue pendiente en el sd-07. |
| F2 a F6 (8.1, 8.2, 8.3, introducción, T-16, PDF) | Hechas como borrador | — |
| Formulario T-16 | Sin empezar | `03_Formularios/B/` está vacío. |

Plazo según la ficha: **lunes 12-10-2026, 08:00** (Informe 2, que cubre los sd 1 a 9 y el 13; Bases Admin. l. 2444-2450). Confirmar con el equipo si sigue vigente; si lo está, aplicar el plan corto de la sección 6.

### Qué cambió con la fusión de `main`

- **sd-13 ya tiene contenido** en `02_Propuesta/sd-13_innovaciones/` (cinco secciones con «Riesgo de adopción y contingencia»), pero aún no tiene `.tex` (T7-13 «pendiente»). I-08 queda parcialmente resuelta: el 8.2 ya puede remitir a los cinco riesgos de adopción por nombre, sin duplicarlos.
- **sd-07** sigue diciendo que la marcha blanca de la Etapa 1 se hace dentro del congelamiento (`sd-07/OSS-Subdocumento7.tex`, l. 273). I-03 sigue abierta y R-12 se mantiene en zona crítica.
- **sd-05** sigue siendo esqueleto (5.1 a 5.4 sin texto). R-01, R-18 y R-26 siguen «a conciliar con sd-05».
- **sd-04** Tabla 4.11 mantiene que el cliente conserva DC-01 y DC-02. I-02 no tiene decisión registrada.

## 2. Qué se exige (fuentes)

| Exigencia | Fuente | Dónde va |
| :-- | :-- | :-- |
| Enfoque, roles, escalas de P e I, ciclo de revisión | Comunicado 10, l. 851 | 8.1 |
| RBS y cuantificación de riesgos técnicos, organizacionales, de proyecto, de seguridad y de operación | Comunicado 10, l. 859; Bases Admin. l. 2156 | 8.2 |
| Obsolescencia, bloqueo por proveedor, escalabilidad, ciberseguridad, contrapartes del cliente | Comunicado 10, l. 863; Bases Admin. l. 2160 | 8.2 (R-07 a R-11) |
| Análisis cualitativo y cuantitativo con FMEA, árbol de fallas o simulación | Comunicado 10, l. 867; Bases Admin. l. 2158 | 8.2 |
| Mitigación con costo-beneficio, responsable, plazo y disparador | Comunicado 10, l. 871; RT-19.04 | 8.3 |
| Reservas de contingencia y de gestión y su reflejo en el cronograma | Comunicado 10, l. 871 | 8.3 |
| Reflejo de las reservas «en el flujo de caja» | Bases Admin. l. 2162 | Solo se nombra en el 8.3; el monto va al Sobre 3 (Art. 50.2 prohíbe cifras que permitan inferir el precio) |
| Riesgos de la solución propuesta, no un catálogo genérico | Comunicado 10, l. 846; Bases Admin. l. 2164 y criterio de evaluación l. 1262 | Todo el capítulo |
| Seis riesgos esperados: cartera, evento anual, cruce indebido, integración no documentada, rotación del 62 %, comisión del vendedor | Caso cap. 17, l. 992 | 8.2 (R-01 a R-06) |
| Lo excluido genera dependencias que deben estar «en el plan y en el riesgo» | Caso cap. 11, l. 651 | 8.2 (rama EXT) |
| Análisis de riesgo de la solución, del desarrollo y de la implantación | Bases Admin. l. 2444 (Informe 2) | 8.2, columna «Mirada» S/D/I |
| ISO 31000, registro vivo, revisión en cada Comité de Proyecto | RT-19.04 | 8.1 |
| Registro accesible al cliente; informe mensual con riesgos | RT-19.05, RT-19.06 | 8.1 |
| Fin de soporte antes del mes 56 no es riesgo del cliente | Bases Transv. l. 102 | 8.3 (R-07: estrategia «aceptar y absorber», a cargo del adjudicatario) |
| Riesgo de adopción de cada innovación | RT-26.04; Art. 29 | sd-13; el 8.2 lo cita |
| Si hay IA: NIST AI RMF e ISO/IEC 42001 | RT-18.04 | 8.2, solo si el sd-04 o el sd-13 incorporan IA |
| Comités: Ejecutivo mensual (riesgos mayores), Proyecto quincenal, Arquitectura mensual (riesgos técnicos) | Bases Admin. l. 1446-1454; sd-06 l. 239-243 | 8.1, roles y ciclo |
| Formulario T-16 | Bases Admin. l. 2314 (texto ilegible) | Anexo. Construirlo con los campos de FEP04 · 21 y marcarlo para confirmar |
| Ponderación T-21 | Bases Admin. l. 2404-2406 (ilegible) | No se completa (regla de AGENTS.md) |

Material de clase para evaluar (FEP04, guía de navegación §2.11): 5 elementos del riesgo (· 6), escalas y matriz (· 7-8), RBS TIC (· 19-20), campos del registro (· 21), cómo redactar (· 36-38), valor esperado (· 46-47), reservas (· 48-49), simulación y P80 (· 52-54), estrategias (· 59-63), residual, disparador y reversa (· 64-65), acción en la EDT (· 67, 94), ficha completa (· 105).

## 3. Decisiones pendientes del usuario (bloquean la redacción)

Se toman antes de escribir. Para cada una, la sugerencia está en el documento indicado. La columna «Estado» resume un sondeo de los subdocumentos hecho el 2026-10-11.

| N.º | Decisión | Sugerencia actual | Estado (2026-10-11) | Dónde |
| :-- | :-- | :-- | :-- | :-- |
| D1 | ¿Cuántos riesgos entran? | 36 en el registro y el T-16; en el cuerpo del 8.2 solo críticos y altos (12 a 15) más los 11 exigidos | **Decidida 2026-10-11: opción A.** 37 riesgos y 8 oportunidades en registro y T-16; fichas en el cuerpo solo de críticos, altos y los 11 exigidos; el resto en matriz y tabla resumen | `registro_candidatos.md`, pregunta 1 |
| D2 | ¿EXT es rama propia de la RBS? | Sí, con sub-ramas normativo y terceros | **Decidida 2026-10-11: se funde en PRO** (cinco ramas, como el Comunicado) | idem, pregunta 2 |
| D3 | ¿Se incluyen oportunidades? | Sí, O-01 y O-02 | **Decidida 2026-10-11: sí, ampliar a O-01..O-08** en el registro y el T-16; en el cuerpo del 8.2 solo O-02, O-03, O-05 y O-06. Se descartaron las candidatas O-09..O-12 (innovaciones y nube) | idem, pregunta 3 |
| D4 | ¿Se confirma SUP-26 (inicio en enero de 2027)? | Sí; R-12, R-13, R-24 y R-25 dependen de él | **Tomada implícitamente**: sd-02 (Anexos l. 3325), sd-03 (l. 234) y sd-07 (l. 249) lo usan como dado, sujeto a confirmación del cliente | idem, pregunta 4 |
| D5 | ¿Se aceptan las fusiones? | Sí | **Decidida 2026-10-11:** se fusionan R-01+R-26 y R-23+R-39; R-21 y R-37 quedan separados (impactos distintos: alcance frente a plazo). Total: 37 riesgos. Ampliación de R-12 tomada antes (I-03) | idem, pregunta 5 |
| D6 | I-02: ¿quién provee el recinto on-premise? | Manda sd-03 y la EDT (lo provee el proponente, RT-06.33 y Art. 16) | **Decidida 2026-10-11: el recinto (DC-01 y DC-02) es del cliente** (Caso l. 330; RT-06.01 y RT-06.31). El cliente ejecuta la obra civil y compra el hardware (RT-06.06; Caso l. 647-649); el proponente especifica, coordina y provee conectividad, seguridad y canalizaciones (RT-06.33) y el espacio del personal (RT-06.29). R-31 = riesgo de contraparte con mitigación; DC-02 se trata como sala de respaldo local y la recuperación real es CLD-02. Cambios pendientes: `cambios_por_D6.md` | `trazabilidad_riesgos.md` §6.1 |
| D7 | I-05: volumen del peak para R-09 | 225.000 pedidos en tres días (1,5 × 150.000) | **Decidida 2026-10-11, con base en el sd-02 (.tex):** evento de 2026 = 104.000 pedidos en 3 días (dato); proyección = 150.000 (Caso 14.1); prueba de carga = 225.000 (1,5 × proyectado, RT-09.06), que cubre el 120 % (180.000) de RNF-22. El «114.520» solo está en `sd-02.md` (contexto, obsoleto). Antes, cuatro versiones: sd-02 114.520 (l. 276); RNF-22 y Anexo B «al 120 % del peak proyectado»; Anexo D 25 104.000; sd-06 y sd-07 «1,5 veces el peak declarado» sin cifra | idem §3 |
| D8 | I-06: tiendas sin enlace de respaldo para R-15 | Rango de 7 a 14, peor caso del sd-04 | **Tomada implícitamente: 14** (sd-02 SUP-28, l. 745, y sd-04 l. 417). Queda un residuo: la tabla de sd-02 (l. 497) dice «7 de 15» | idem §3 |
| D9 | I-07: holgura del evento anual | La reserva de contingencia en semanas del 8.3 la cubre; el sd-07 la cita | **Decidida 2026-10-11: opción A, grado 1** (solo texto: el 8.3 define la reserva; el sd-07 agrega una frase en 7.3 que la cita; sin fechas internas, sin cambios en EDT ni en Tabla 7.6). **Cerrada 2026-10-12: la reserva de contingencia es de esfuerzo (3.688 h) y el P80 es exposición en plazo; no se pide ningún cambio al sd-07.** Antes: sd-07 (l. 277) dice que la ruta crítica «no admite holgura» y no cuantifica ninguna | idem §3 |
| D10 | Cuatro cuentas nuevas de la EDT (R-06, R-27, R-28, R-36) | Proponerlas al sd-07 y nombrarlas en el 8.3 | **Revertida 2026-10-12:** no se agregan cuentas; cada acción se ejecuta en una cuenta existente del T-14 (R-06 1.13.1; R-27 1.2.1; R-28 1.8.5; R-36 1.6.3; R-33 1.11.3) | idem §4 |

## 4. Plan de trabajo por fases

Cada fase termina con un control del usuario, como se hizo en el sd-03. Las herramientas son las del repo: skill `redactar-seccion`, `exportar_latex.py verificar-redaccion --parte T7-08`, `verificar`, `compilar`, y los agentes `evaluador-pmbok`, `revisor-comite-ancoa` y `lector-no-tecnico` para revisar.

### F1b · Cerrar el registro (30 min)

1. Responder D1 a D10.
2. Aplicar fusiones y ajustes (§5 de `trazabilidad_riesgos.md`), renumerar y dejar el registro final en `registro_candidatos.md` (o un `registro_final.md`).
3. Anotar los riesgos de adopción del sd-13 como referencias cruzadas (no como filas propias).

**Hecho cuando:** hay una lista cerrada con ID, enunciado causa-evento-efecto, rama RBS, mirada S/D/I y fuente.

### F2 · Redactar el 8.1 Plan de riesgos (1 h)

Contenido mínimo:
- Enfoque: ISO 31000 (RT-19.04), ciclo de los 7 procesos (FEP04 · 16-17) y dónde vive el registro (espacio colaborativo, RT-19.05).
- Roles: dueño del riesgo, jefe de proyecto, Comité de Proyecto quincenal, Comité de Arquitectura mensual (técnicos), Comité Ejecutivo mensual (críticos y liberación de la reserva de gestión), Comité de Operación desde el mes 13. Contrapartes del cliente que validan.
- Escalas: probabilidad en cinco niveles con porcentaje; impacto en plazo (semanas contra los hitos de los meses 16 y 21 y las fechas del Caso 13.2), en esfuerzo (horas-persona), en costo (porcentaje del costo directo, sin pesos), en alcance y calidad, y en servicio (disponibilidad, RTO/RPO, autonomía de 24 h). Una tabla por escala.
- Matriz 5×5 de exposición con zonas crítica, alta, media y baja, y qué obliga cada zona (apetito y umbral, FEP04 · 9).
- Ciclo de revisión: quincenal, mensual, en cada hito y en cada congelamiento; informe mensual (RT-19.06); reevaluación al cambiar SUP-26.

**Control del usuario:** aprueba escalas y umbrales. Sin esto no se puede calificar.

### F3 · 8.2 análisis cualitativo (1,5 h)

1. Figura RBS (seis ramas: TEC, ORG, PRO, SEG, OPE, EXT) con los ID en cada hoja; ninguna rama vacía. Exportar como `04_Adjuntos/diagramas/diag-08-01_rbs.{svg,pdf}` (no Mermaid).
2. Calificar P e I de los 36 con las escalas de F2, justificando cada calificación con un dato del Caso o del subdocumento fuente (es lo que separa este capítulo de un catálogo).
3. Matriz de calor con los ID ubicados (`diag-08-02_matriz-exposicion`).
4. En el cuerpo, fichas cortas solo de críticos, altos y los 11 exigidos: causa-evento-efecto, componente afectado de la solución, mirada S/D/I, P, I, exposición. El resto queda en el T-16.
5. Párrafo que diga explícitamente dónde están las cinco categorías del Comunicado y los cinco riesgos nombrados (OB-1 a OB-5), y que los seis del Caso son R-01 a R-06.

**Control del usuario:** revisa las calificaciones.

### F4 · 8.2 análisis cuantitativo (2 h)

Se exige al menos una técnica; usar dos, porque sirven a preguntas distintas:

- **Simulación Monte Carlo del cronograma** (proyecto): red de la EDT de `80_Artefactos/sd-07_contexto/estimacion/` con los tres valores de `12_plantilla_tres_valores.md` y horas de `16_horas_por_paquete.md`, más los riesgos críticos como eventos discretos (P × impacto en semanas). Medir contra los hitos fijos de los meses 16 y 21, no contra el plazo total, porque la ruta crítica del sd-07 tiene holgura cero (Tabla 7.6). Salida: P50 y P80 de cada hito y semanas de colchón necesarias. Implementar como script en `05_Gestion/scripts/` con prueba en `05_Gestion/tests/`, como los demás cálculos de la estimación, y semilla fija para que sea reproducible.
- **FMEA de la solución en operación**: modos de falla de los componentes de la arquitectura (sd-04): venta sin enlace (R-15), emisión tributaria en contingencia (R-16), DC-01 (R-31), cruce indebido (R-03), saturación en el peak (R-09). Severidad, ocurrencia y detección de 1 a 10 y NPR.
- Opcional: **árbol de fallas** de «la tienda no puede vender durante un corte» (R-14, R-15, R-16, R-31), que muestra por qué la restricción 5 del Caso depende de tres componentes.
- Tabla de valor esperado en horas-persona de los riesgos críticos y altos; su suma es la base de la reserva de contingencia.

**Cuidado con el Art. 50.2:** nada en pesos, UF ni dólares. Horas, semanas y porcentajes.

**Control del usuario:** aprueba supuestos de la simulación (distribuciones, correlaciones, eventos incluidos).

### F5 · 8.3 Plan de acción a riesgos (1,5 h)

1. Por cada riesgo crítico y alto: estrategia (evitar, transferir, mitigar, aceptar, escalar; y explotar o mejorar para O-01 y O-02), acción concreta, **cuenta de la EDT** donde vive, responsable, plazo, disparador, plan de contingencia y riesgo residual.
2. Costo-beneficio por riesgo: horas de la acción frente a la reducción del valor esperado (FEP04 · 61-63). Una tabla basta.
3. Reserva de contingencia: suma de valores esperados en horas y colchón en semanas antes de cada hito, tomado del P80 de F4. Explicar cómo se refleja en el cronograma (amortiguadores antes de los meses 16 y 21 y antes del evento anual, que también responde a I-07).
4. Reserva de gestión: concepto, quién la libera (Comité Ejecutivo) y que su valor y el reflejo en el flujo de caja van en el Sobre 3.
5. Nombrar las cuatro cuentas nuevas de la EDT de D10 y registrar el aviso al sd-07.

**Control del usuario:** aprueba estrategias y reservas.

### F6 · Cierre (1,5 h)

1. Introducción del capítulo: resumen y conexión con sd-03 (supuestos y restricciones), sd-04 (ADR), sd-06 (comités), sd-07 (EDT y cronograma), sd-09, sd-13 (adopción), T-16 y Sobre 3.
2. Formulario T-16 como anexo con el registro completo (campos de FEP04 · 21), marcado «estructura por confirmar» porque su texto en las Bases es ilegible.
3. Referencias con la skill `citas-proyecto` (solo Caso 09 con folio impreso; no citar las Bases generales). Declaración de uso de IA.
4. Verificación: `exportar_latex.py verificar-redaccion --parte T7-08`, `verificar`, `compilar`.
5. Revisión independiente con `evaluador-pmbok` y `revisor-comite-ancoa`.
6. Actualizar el maestro: ruta del `.tex`, estado de 8.1 a 8.3, `actualizado:`. El estado `revisado` lo asigna solo una persona.

## 5. Criterios para saber que está bien

- Cada riesgo nombra un componente, una fecha o una cifra del Caso 09. Si el enunciado sirve para otra licitación, se reescribe.
- Los 6 del Caso y los 5 del Comunicado aparecen con su ID y se encuentran en menos de un minuto.
- Las tres miradas del Informe 2 (solución, desarrollo, implantación) tienen riesgos y se dice cuáles.
- Todo riesgo crítico o alto tiene acción con cuenta de la EDT, responsable, plazo, disparador y contingencia.
- La reserva de contingencia sale de un cálculo mostrado y se ve en el cronograma.
- Ninguna cifra monetaria (Art. 50.2).
- Coherencia de fechas con los meses 16 y 21, el retiro de la plataforma de 2011 en el mes 22, «antes de 2029» y las ventanas de congelamiento.

## 6. Plan corto si el plazo es el lunes 12-10, 08:00

Unas 8 horas de trabajo. Orden de prioridad, para que lo que falte al final sea lo menos visible:

1. F1b con las sugerencias por defecto si el usuario no puede decidir todo (dejar constancia).
2. F2 completo (es corto y condiciona el resto).
3. F3 con matriz y fichas de críticos y exigidos; la RBS puede ir como tabla si no hay tiempo para la figura.
4. F4: FMEA y tabla de valor esperado primero; la simulación Monte Carlo después, aunque sea con la red resumida de hitos y no con las 164 cuentas.
5. F5 completo.
6. F6: verificar y compilar siempre; el T-16 puede ir como tabla anexa del mismo `.tex`.

## 7. Pendientes que no son del sd-08 pero lo afectan

- sd-07: corregir l. 273 (I-03) y agregar las cuentas de D10.
- Excel `RequerimientosAtomizados_Depuracion_Alcance_v3.1.xlsx`, criterio 9: cambiar «0,5 % o menos» a «menos de 3 %» (I-04).
- sd-04: Tabla 4.11 y DC-02 en la misma comuna (I-02 y observación P0 S4-13).
- sd-05: estrategia de migración, de la que dependen R-01, R-18 y R-26.
- sd-13: pasarlo a `.tex` para poder citar sus riesgos de adopción por sección.
