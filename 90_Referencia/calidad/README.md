# Contexto y revisor de calidad

Esta carpeta conserva el material de clases aportado por el usuario y las fuentes investigadas para revisar planes, criterios y matrices de calidad. Es material de lectura y análisis; no sustituye Bases, contrato, diseños vigentes ni evidencia de ejecución.

| Archivo | Uso y procedencia |
| :--- | :--- |
| [contextoCalidad.pdf](contextoCalidad.pdf) | Copia preservada del PDF entregado, 38 páginas, folios impresos 67–104. |
| [contextoCalidad.md](contextoCalidad.md) | Transcripción navegable por `pagina-01` a `pagina-38`, con método y límites de extracción. |
| [contextoCalidad_texto_original.txt](contextoCalidad_texto_original.txt) | Extracción íntegra para contraste de transcripción. |
| [investigacion_calidad.md](investigacion_calidad.md) | Investigación con fuentes primarias, fecha, límites de acceso y distinción entre clase, fuente y recomendación. |
| [validacion_revisor.md](validacion_revisor.md) | Prueba inicial del agente Sol: 14 casos, revisión de 115 criterios y cinco hallazgos nuevos pendientes de corrección. |

La investigación actualiza o acota el material docente: ISO/IEC 25010:2023 tiene nueve características, mientras las Bases conservan ocho títulos contractuales; los cinco principios de clase son una selección de siete; los cinco niveles pedagógicos no son CMMI; las cifras de Boehm/CISQ y 15–25 % no son umbrales del caso. La nota registra la publicación de ISO 9001:2026 y exige volver a comprobar las fichas oficiales al citar ediciones. Mantener la transcripción original permite distinguir qué dijo la clase y qué cambió o requiere matiz.

## Uso del agente

La instrucción canónica es [revisor-calidad/SKILL.md](../../.agents/skills/revisor-calidad/SKILL.md). El wrapper para Claude está en [revisor-calidad.md](../../.claude/agents/revisor-calidad.md) y solo habilita Read, Grep, Glob, WebSearch y WebFetch. Codex y OpenCode pueden leer la skill directamente; no necesitan el wrapper Claude. Si la plataforma no descubre automáticamente la carpeta canónica, abrirla por ruta en la invocación.

Ejemplos:

- «Aplica `.agents/skills/revisor-calidad/SKILL.md` a `80_Artefactos/sd-09_contexto/`, foco diseño de criterios y evidencia futura. No edites archivos».
- «Revisor de calidad: revisa la sección 9.2 del archivo indicado, contra sus fuentes y obligaciones pertinentes. Distingue diseño, ejecución y aceptación».
- «Revisa esta matriz de criterios. Evalúa muestreo y conciliación de cartera; informa los requisitos que no pudiste contrastar con Excel».

Basta ruta y sección/foco opcional. El revisor descubre contexto sin pedir confirmaciones rutinarias. En cada invocación inventaría y lee una vez las 38 páginas de la transcripción y después consulta selectivamente fuentes relacionadas. Cita solo fuentes abiertas y material efectivamente leído. La investigación web usa conceptos genéricos y no transmite contenido privado. Las herramientas de lectura no permiten dar por contrastado un Excel inaccesible: ese límite se reporta.

El invocador elige un modelo válido de su plataforma; Sol y Luna son preferencias de la sesión Codex, no nombres de modelos Claude. Esta configuración guarda instrucciones y fuentes para futuras invocaciones. No modifica pesos, entrena un modelo ni conserva automáticamente el conocimiento de una conversación.

## Criterios de capacitación y validación

La preparación del agente se considera cubierta cuando puede:

1. Inventariar las 38 páginas y usar página PDF/ancla correcta, distinguiendo folio impreso y sin fingir cotejo visual.
2. Distinguir calidad y grado, proceso y producto, QA y QC; mapear ocho categorías contractuales y nueve características de 2023 sin cambiar títulos de Bases.
3. Convertir obligaciones en criterios con método, condiciones, umbral, evidencia, dueño, hito y cláusula/pago cuando verificables.
4. Separar diseño adecuado de ejecución conforme y aceptación humana; valorar evidencia futura en un diseño sin exigir logs aún inexistentes.
5. Detectar certificaciones, madurez, porcentajes, causalidad y reglas jurídicas indebidamente inferidos; conservar fuentes y límites.
6. Identificar pruebas/gates y riesgos de muestra, datos, saldos, consentimiento, separación y máximos, sin sustituir controles obligatorios por heurísticas.
7. Producir hallazgos priorizados con contraprueba, remedio, cierre y responsable; informar cobertura real y lo no verificable.
8. Respetar solo lectura, privacidad, precedencia y revisión humana pendiente.

La prueba inicial utiliza [14 fragmentos](pruebas/casos_revision.md). La [clave del evaluador](pruebas/clave_evaluador.json) está separada: el invocador debe reservarla al evaluador y no facilitarla al agente bajo prueba. Durante esta sesión el revisor recibió únicamente el documento de casos desde `/tmp/`, sin consultar la clave. La prueba debe identificar los doce fragmentos defectuosos, conservar los dos adecuados con sus límites de diseño y evitar exigir evidencia ejecutada en un documento sin implementación. Esa comprobación valida comportamiento en el conjunto, no garantiza desempeño universal ni sustituye prueba sobre el documento real.

El informe tendrá hallazgos con ID interno, prioridad, fuente/ubicación, contraprueba o fundamento, remedio, condición de cierre y responsable; además de cobertura y límites. No genera puntaje T-21, no inventa tablas incompletas y no asigna automáticamente estado revisado o aprobación. Los controles y la revisión humana permanecen a cargo del equipo.

La prueba inicial fue ejecutada por `/root/revisor_calidad` con Sol: las 14 clasificaciones coincidieron con la clave reservada al evaluador. También examinó los 115 criterios de SD09 y produjo cinco hallazgos nuevos, contrastados por la coordinación. Véase el [registro de validación](validacion_revisor.md) para alcance, fuentes y límites. El resultado acredita esa comprobación concreta, sin garantizar desempeño universal.
