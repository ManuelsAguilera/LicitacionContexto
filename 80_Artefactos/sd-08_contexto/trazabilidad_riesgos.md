# Trazabilidad y consistencia de los riesgos candidatos del sd-08

Documento de trabajo, 2026-10-10. Contrasta los 36 riesgos del registro (con las cuatro fusiones propuestas en `registro_candidatos.md`, sección F) con las Bases, el Caso, los sd-01 a sd-07, los Anexos A y D del sd-03 y la EDT de `80_Artefactos/sd-07_contexto/estimacion/14_edt_corregida.md`.

## 1. Método

Para cada riesgo se revisaron cuatro eslabones:
- **Origen:** dónde lo exige o lo funda una Base, el Caso o una restricción.
- **Componente:** servicio, ADR, supuesto o responsabilidad del cliente que lo expone.
- **EDT:** cuenta de control donde vive la respuesta. Así la mitigación tiene horas y fecha, lo que exige FEP04 · 67 y 94.
- **Medida:** resultado del Anexo D o RT con que se comprueba que el riesgo no se materializó.

Estado:
- **OK:** los cuatro eslabones existen y no se contradicen.
- **Hueco:** falta la cuenta de la EDT que ejecutaría la respuesta.
- **Inconsistente:** dos documentos dicen cosas distintas sobre el hecho del que depende el riesgo (sección 3).

Las fuentes con (*) tienen revisión pendiente (sd-05 a sd-07, según el usuario).

## 2. Matriz de trazabilidad

| ID | Riesgo (corto) | Origen | Componente | EDT | Medida | Estado |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| R-01 | Divergencia de saldos al migrar la cartera (tramo difícil en la Etapa 2) | Caso cap. 10 (8), cap. 17; 16.1 n.º 25 | Servicio de cartera de crédito; SUP-25 | 1.7.1, 1.7.7, 1.7.14, 1.5.11.5 | Anexo D 24 | OK; diseño de migración pendiente del sd-05 |
| R-02 | Fecha del evento anual con aviso de seis semanas | Caso cap. 10 (10), 13.2, cap. 17 | Calendario de despliegue | 1.1.6, 1.9.6 | Anexo D 2 y 25 | **Inconsistente** (I-07) |
| R-03 | Cruce indebido entre ámbitos | Caso cap. 10 (1), cap. 12, cap. 17 | Servicio de control de cruces; ADR-02 | 1.5.13.1 a 1.5.13.3, 1.3.4, 1.8.7 | Anexo D 21 y 22 | OK |
| R-04 | Integración no documentada en producción | Caso cap. 10 (15), cap. 17 | Plataforma de integración; ADR-01 | 1.2.1, 1.6.1, 1.6.11 | Certificación de integraciones (1.6.11) | OK |
| R-05 | Rotación del 62 % borra la capacitación | Caso cap. 10 (13), cap. 17 | Personal de tienda | 1.13.2, 1.13.3, 1.13.4, 1.15.8 | Condición de cierre de marcha blanca (1.13.3) | OK |
| R-06 | Remuneración del vendedor compite con el proceso | Caso cap. 17; cap. 8 (vendedor) | Servicios de originación, evidencia y comisiones | 1.5.6.1 a 1.5.6.3 (Etapa 2) | Anexo D 12, 20 y 28 | **Hueco** (ver 4.1, reformular) |
| R-07 | Obsolescencia de servicios administrados | Comunicado 10, 8.2 | ADR-06 (API Management Premium clásico) | 1.15.4, 1.4.7 | — | OK; falta medida |
| R-08 | Bloqueo por proveedor de nube | Comunicado 10, 8.2; Art. 77.2 | ADR-06 y ADR-07 | 1.4.1 (IaC), 1.14.6 (reversibilidad) | Plan de reversibilidad aceptado | OK |
| R-09 | Escalabilidad en el evento anual | Comunicado 10; RT-09.06; Caso 14.1 | Base tecnológica, existencias, pedidos | 1.3.7, 1.9.4, 1.9.6 | Anexo D 25; RT-09.06 | **Inconsistente** (I-05) |
| R-10 | Ciberseguridad y alcance de medios de pago | Comunicado 10; Caso cap. 6 y cap. 12 | Red de tienda; ámbito del Emisor | 1.8.1, 1.8.6, 1.8.9, 1.4.2 | Anexo D 21 (penetración) | OK |
| R-11 | Contrapartes del cliente no validan a tiempo | Comunicado 10; Art. 18.3 | RC-08, RC-09 | 1.1.7, 1.1.10 | Actas dentro de 10 días hábiles | OK |
| R-12 | Marcha blanca de la Etapa 1 dentro del congelamiento | Caso cap. 10 (9), 13.2; SUP-26 | Calendario | 1.12.1, 1.1.6 | Anexo D (cierre de marcha blanca) | OK en el sd-08; aviso al sd-07 (I-03) |
| R-13 | Un tramo de la cartera no alcanza a migrar antes del retiro | Caso 13.1, 13.2 | Servicio de cartera; plataforma 2011 | 1.7.10, 1.7.11, 1.7.14 | Anexo D 23 y 24 | OK (I-01 resuelta) |
| R-14 | Crédito sin enlace: topes no fijados o prueba fallida | Caso 16.1 n.º 7; RT-03.10 | Servicio de originación; SP-03; RC-11 | 1.1.14, 1.2.10, 1.5.10.4, 1.9.11, 1.11.5 | Informe de la prueba de 24 h (1.9.11) | OK |
| R-15 | Sincronización tras corte duplica o pierde ventas | Caso cap. 6 y cap. 10 (5) | Servicio de ventas; ADR-04 | 1.3.6, 1.5.5.2, 1.9.11 | Prueba de 24 h | **Inconsistente** (I-06) |
| R-16 | Modalidad fiscal de contingencia no aprobada | Caso cap. 10 (6) | ERP/DTE; sd-04 Tabla 4.9 n.º 6 | 1.6.12 | Modalidad aprobada y probada | OK |
| R-17 | Residencia de datos del Emisor en Brazil South objetada | RT-07.02; regulación CMF | ADR-07; CLD-02 | 1.8.10 | Aprobación de residencia | OK |
| R-18 | Inventario inicial hereda el 12,4 % de error | Caso cap. 7, cap. 17 | Servicio de existencias | 1.7.3, 1.7.4, 1.5.3.4 | Anexo D 1 y 4 | OK; diseño pendiente del sd-05 |
| R-19 | Ley 21.719 exige controles no previstos | Caso cap. 12 | Servicio de control de cruces | 1.8.7 | Matriz de cumplimiento (1.8.7) | OK |
| R-20 | Hardware, obras y enlaces del cliente atrasados | Caso cap. 11; Art. 14.2 | SP-04; RC-02, RC-04 | 1.3.8, 1.4.8, 1.11.3 | Certificación de sitio (1.11.3) | OK (I-02 resuelta) |
| R-21 | Decisiones y supuestos del cliente sin validar (incluye las 7 decisiones antes de cerrar la 4.1) | Caso 16.1, 17.1 | Anexo A (SP, SUP); sd-04 4.1 | 1.2.6, 1.1.4, 1.1.3 | Línea base del mes 4 | OK |
| R-22 | Repositores externos y terminales compartidas | Caso cap. 10 (11 y 12) | SUP-19; EXC-03; RC-03 | 1.13.4, 1.5.14.2 | Acceso individualizado por proveedor | OK |
| R-23 | Capacidad y continuidad del equipo del proponente | RT-19.02; sd-01 1.5 | 16 profesionales núcleo | 1.1.1 (plan de recursos) | Formulario T-15 | Parcial (*); sd-12 vacío |
| R-24 | Primer peak dos meses después de salir a producción | Caso 13.2 | Existencias y ventas en producción | 1.9.6, 1.12.9 | Anexo D 2 (mes 16 sin meta de cero) y 25 | OK |
| R-25 | Retiro de 2011 justo antes del congelamiento de fin de año | Caso 13.2; cap. 10 (9) | Plataforma 2011 | 1.7.10, 1.7.11 | Anexo D 23 | OK (I-01 resuelta) |
| R-27 | Proveedores actuales no cooperan | Caso cap. 5 (6 proveedores) | ADR-01; SP-01 | 1.2.1 (solo el inventario) | — | **Hueco** (4.2) |
| R-28 | Evidencia de crédito perdida antes del mes 16 | Caso cap. 10 (2); cap. 7 | Servicio de evidencia financiera (mes 16) | — | Anexo D 18 y 19 | **Hueco** (4.3) |
| R-29 | Procedimiento del SERNAC impone obligaciones | sd-02 2.3.1 | Alcance | 1.1.3 | Control de cambios | OK |
| R-30 | Servicio Premium no disponible en Chile Central | ADR-07 | Base tecnológica | 1.4.1 | Prueba de creación de recursos (ADR-07) | OK |
| R-31 | Evento local en DC-01 detiene ERP/DTE o crédito 2011 | RT-07.02; Caso cap. 6 | DC-01 y DC-02 (misma comuna) | 1.4.9, 1.4.11, 1.4.12, 1.4.14 | Recinto certificado (99,95 %, RT-06) | OK (I-02 resuelta) |
| R-32 | Ubicación de plataformas y enlaces supuesta | SUP-27; sd-04 supuestos | Rutas y adaptadores | 1.2.1, 1.3.3 | Inventario de sitios | OK |
| R-33 | Solapamiento de equipo entre los meses 13 y 15 | Art. 17 | Equipo del proponente | Nivelación (T-15) | — | Parcial (*) |
| R-34 | Meta de precio depende del personal de tienda | Caso cap. 10 (4); 14.1 | Servicio de oferta comercial | 1.5.1.2, 1.2.7 | Anexo D 6 y 9 | OK (I-04 resuelta) |
| R-35 | Accesos sin revocar por rotación | SUP-24; RT de identidad | Base tecnológica | 1.5.14.1, 1.5.14.2 | Revisión de accesos | OK |
| R-36 | Terceros no adoptan los contratos de la Etapa 2 | Caso cap. 11; RC-06 | Pedidos y marketplace | 1.6.3, 1.5.4.5, 1.5.7.2 | Anexo D 10, 13 y 14 | **Hueco** parcial (4.4) |
| R-38 | Concentración de venta en el clúster de Santiago | sd-02 2.3; SUP-27 | Selección de pilotos y olas | 1.11.5, 1.11.1 | — | OK |

**Resultado:** 27 OK, 2 parciales (fuentes sin revisión), 4 con hueco y 3 inconsistentes (I-01 a I-04 resueltas o tratadas el 2026-10-10; quedan I-05 a I-08). Las inconsistencias vienen de otros subdocumentos y el sd-08 no las puede resolver solo. Hay que decidir qué versión manda.

## 3. Inconsistencias entre documentos

| ID | Qué dicen | Riesgos afectados | Qué manda y sugerencia |
| :-- | :-- | :-- | :-- |
| I-01 | **Plazo de 2029. RESUELTA (2026-10-10).** Manda el Caso cap. 18 («antes de 2029»). Se corrigió sd-02 2.3.4 (`.tex` y `.md`): último día útil 31-10-2028, 670 días calendario, 191 congelados, 479 intervenibles (≈ 15,7 meses), con el mismo método que daba 1.035, 317 y 718. | R-13, R-25 | El sd-08 usa el mes 24 como plazo y el 31-10-2028 como último día intervenible. |
| I-02 | **Centro de datos on-premise. RESUELTA (2026-10-10).** Decisión del usuario: Ancoa aporta el espacio del recinto en su casa matriz y ejecuta la instalación y la obra civil de separación. Only Simple Solutions hace todo lo demás (especifica, provee equipos, conectividad, seguridad y canalizaciones, configura y certifica). No se compra un recinto. Corregidos sd-04 (Tabla 4.11 y 4.3), sd-03 (3.2.3, SP-04), Anexo A (SP-04, RC-04) y la ficha del sd-03. La EDT 1.4.9 a 1.4.17 ya era coherente. | R-20, R-31 | Queda R-31 con un solo alcance: lo heredado en DC-01 y DC-02 sigue expuesto a un evento local en la misma comuna. |
| I-03 | **Marcha blanca en congelamiento. TRATADA EN EL sd-08 (2026-10-10).** El calendario contractual no cambia. R-12 queda en zona crítica con respuesta de evitar (despliegue en la ventana del 7 al 24 de enero de 2028, correcciones en la ventana de marzo, emergencias solo con el Comité Ejecutivo). Aviso al sd-07 en `avisos_otros_subdocumentos.md`. | R-12 | El sd-07 debe retirar la afirmación de que la marcha blanca puede desarrollarse dentro del congelamiento. |
| I-04 | **Meta de precio. RESUELTA (2026-10-10).** Manda el sd-02 (menos de 3 %, con cálculo). Se corrigió la fila 9 del Anexo D. El Excel v3.1 queda pendiente del equipo (aviso). | R-34 | R-34 se califica contra el 3 % en campaña (hasta 400.000 cambios al día). |
| I-05 | **Volumen del peak.** Caso 14.1: 104.000 pedidos hoy y ≈ 150.000 en tres años. RT-09.06 exige prueba a 1,5 veces el peak. sd-02 calcula 114.520. Anexo D 25 prueba 104.000 sin factor 1,5 ni proyección. | R-09 | Manda el más exigente (memoria del sd-03): 1,5 × 150.000 = 225.000 pedidos en tres días. Sugerencia: R-09 se califica con esa cifra y se avisa que el Anexo D 25 queda bajo RT-09.06. |
| I-06 | **Tiendas sin enlace de respaldo.** Caso cap. 6: 6 de las 14 en centro comercial no tienen respaldo, y de las 8 a la calle solo dice que Coyhaique no lo tiene. sd-02 cuenta 7 sin respaldo. sd-04 supone 14 (las 8 a la calle sin respaldo) y lo declara como supuesto. | R-15 | Sugerencia: el sd-08 usa el rango «entre 7 y 14», con el supuesto del sd-04 como peor caso, y el disparador de R-15 es el inventario de enlaces (1.2.1). |
| I-07 | **Holgura del evento anual.** El Caso cap. 17 exige que el plan «declare y cuantifique la holgura reservada para la fecha del evento anual». sd-07 (*) Tabla 7.6 pone holgura cero en toda la ruta crítica. | R-02 | Sugerencia: la reserva de contingencia del sd-08 en semanas cubre esa exigencia (FEP04 · 53) y el sd-07 la cita. Es el puente más claro entre los dos subdocumentos. |
| I-08 | **Innovaciones.** sd-13 no tiene `.tex` y la EDT 1.10 está «por definir». | Riesgos de adopción | El sd-08 no puede citar riesgos de adopción que no existen. Sugerencia: dejar en la 8.2 una frase que remita al capítulo 13 sin listar riesgos, y completarla cuando exista el sd-13. |

## 4. Huecos: respuestas sin cuenta en la EDT

FEP04 · 67 y 94 piden que la acción de riesgo esté en la EDT y en el cronograma. Cuatro riesgos no la tienen.

1. **R-06 (reformular).** Tal como estaba redactado, R-06 miraba solo el despacho desde tienda (Etapa 2). El Caso cap. 8 y el sd-02 2.4.3 muestran que el conflicto más fuerte es otro: el vendedor deja de ofrecer la tarjeta si la entrega de información precontractual alarga la venta, y eso ocurre desde el mes 16 (Anexo D 20 y 28). El Servicio de comisiones recién llega en el mes 21. Sugerencia: redactar R-06 con las dos caras y proponer como respuesta un acuerdo con la filial emisora sobre la regla de comisión antes del mes 13 (cuenta nueva en 1.13 o en 1.2).
2. **R-27.** No hay cuenta para acordar con los proveedores salientes su cooperación (documentación, extracción de datos, convivencia). Sugerencia: cuenta nueva en 1.2, «Acuerdos de cooperación y salida con los proveedores de las plataformas que se reemplazan», con el cliente como firmante (es su contrato).
3. **R-28.** No hay cuenta que corte la pérdida de evidencia antes del mes 16. Sugerencia: cuenta temprana en 1.7 o 1.8, «Medida transitoria de retención de grabaciones de repactación», que solo especifica y acompaña la decisión del cliente (cambiar su política de 90 días). Es barata y protege el resultado 18.
4. **R-36.** Hay integración (1.6.3) pero no incorporación de terceros. Sugerencia: cuenta en 1.13 o 1.6, «Plan de incorporación de transportistas y vendedores de marketplace a los contratos de estado».

Estas cuentas se proponen al sd-07; el sd-08 las nombra como respuesta y no edita la EDT.

## 5. Ajustes al registro que salen de esta revisión

- R-06 se reformula (4.1).
- R-09 se califica con 225.000 pedidos en tres días (I-05).
- R-13 y R-25 se anclan al mes 24 (I-01).
- R-15 usa el rango de 7 a 14 tiendas (I-06).
- R-34 se califica contra la meta del 3 % (I-04 resuelta).
- R-31 se limita a lo heredado en DC-01 y DC-02 (I-02 resuelta).
- Resultado de la revisión: ningún riesgo del registro carece de origen en las Bases o en el Caso, y ninguno contradice una decisión de los sd-01 a sd-04. Los conflictos están entre subdocumentos, no entre el registro y ellos.

## 6. Preguntas para el usuario, con sugerencia

1. ~~I-02~~ Resuelta por el usuario el 2026-10-10.
2. **¿Se avisa a los responsables de los otros subdocumentos (I-01, I-03, I-04, I-05)?** Sugerencia: sí, con una nota corta por subdocumento en `80_Artefactos/sd-08_contexto/avisos_otros_subdocumentos.md`. No edito sus `.tex`.
3. **¿Se proponen las cuatro cuentas nuevas de la EDT (sección 4)?** Sugerencia: sí, como respuesta en la 8.3 y en el aviso al sd-07. Sin ellas la mitigación no tiene horas, que es lo que el profesor critica.
4. **I-08 (innovaciones sin redactar):** Sugerencia: remitir al capítulo 13 sin listar riesgos de adopción.
