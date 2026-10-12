---
estado: borrador
parte: T7-09
---
# Vista de verificación

La definición de cada criterio reúne escenario, método, umbral y evidencia prevista en su ficha. Los códigos permiten vincular futuras ejecuciones sin duplicar el texto del requisito. La prueba tendrá estados pendiente, ejecutada conforme, ejecutada no conforme o bloqueada; en esta versión todas las ejecuciones están pendientes.

| Grupo | Definición | Método principal |
| :--- | :--- | :--- |
| R01–R15 | [Fichas Retail](resultados.md#r01) y [pilotos R03/R06](pilotos.md#r03) | Prueba funcional, concurrencia, medición temporal y auditoría de indicadores. |
| R16–R20 | [Fichas Emisor](resultados.md#r16) y [pilotos R16/R18](pilotos.md#r16) | Medición, negativos de consentimiento, recuperación e integridad. |
| R21–R22 | [Frontera](pilotos.md#r21) y [registro de cruces](resultados.md#r22) | Inspección del despliegue, accesos denegados, pentest independiente y auditoría. |
| R23–R28 | [Fichas restantes](resultados.md#r23) y [migración R24](pilotos.md#r24) | Conciliación diaria, retorno, carga/degradación y seguimiento operativo. |
| T01–T11 | [Obligaciones transversales](transversales.md) | Inspección, análisis de herramientas, pruebas manuales, fallos y recuperación. |

## Expediente mínimo de ejecución futura

QA debe vincular ID interno y requisito/resultado fuente, versión de diseño y software, ambiente y configuración, datos y perfil de carga, precondiciones, pasos, resultado esperado/obtenido, duración/denominador, evidencia íntegra, defectos y responsable. La verificación exige repetir el ensayo después de corregir un defecto y registrar alcance de regresión. Una evidencia prevista no cuenta como evidencia producida.

Para tasas, documentar numerador, denominador, causa y ventana. Para máximos, conservar todos los valores observados y las violaciones; el máximo observado vale para la muestra y perfil ensayados. Para seguridad y separación, incluir rutas alternativas, exportaciones, analítica y backups. Para conciliación, comprobar registros individuales además de sumas globales. Un resultado compartido distingue capacidad técnica y ejecución operativa del cliente.

## Priorización por impacto

Propuesta: atender primero consentimiento, separación, integridad de saldos y cobro indebido, por daño al cliente y obligaciones del Emisor; después disponibilidad, propagación de precios y continuidad; luego ampliar cobertura restante antes de cerrar etapa. Esta secuencia no elimina requisitos ni asigna probabilidades. QA y Contraparte deben validar prioridades y dependencias con SD08.
