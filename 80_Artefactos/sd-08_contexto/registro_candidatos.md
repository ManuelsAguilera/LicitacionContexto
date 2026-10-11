# Registro de riesgos candidatos del sd-08 (fase 1)

Documento de trabajo, creado el 2026-10-10. Lista para validar con el usuario antes de calificar. Cada riesgo sale de un documento ya escrito y se redacta como causa, evento y efecto. Sin calificación todavía (fase 3).

Claves de las columnas:
- **RBS:** TEC técnico, ORG organizacional, PRO de proyecto, SEG seguridad, OPE operación, EXT externo (normativo o de terceros; FEP04 · 20 lo separa, el Comunicado no lo nombra y se puede fundir en PRO).
- **Mirada (Informe 2):** S solución, D desarrollo del proyecto, I implantación.
- **Exigido:** CA-n riesgo esperado del Caso cap. 17 (1 a 6); OB-n riesgo nombrado por el Comunicado 10 (1 obsolescencia, 2 bloqueo por proveedor, 3 escalabilidad, 4 ciberseguridad, 5 contrapartes).

## A. Riesgos exigidos por el Caso (cap. 17)

| ID | Causa → evento → efecto | RBS | Mirada | Exigido | Fuente |
| :-- | :-- | :-- | :-- | :-- | :-- |
| R-01 | Cartera viva con cuotas, repactaciones y cobranzas en curso → los saldos migrados por tramos divergen de la plataforma de 2011 → se incumple la restricción 8, hay reclamos y exposición ante la CMF | TEC | I | CA-1 | Caso cap. 10 (8), 13.1, 16.1 (25); sd-03 3.2.2 y 3.2.3. A conciliar con sd-05 |
| R-02 | La fecha del evento anual la fija la asociación gremial con unas seis semanas de aviso → el evento cae con un servicio a medio desplegar o dentro de una marcha blanca → caída de venta digital o congelamiento que desplaza trabajo de la ruta crítica | PRO | I | CA-2 | Caso cap. 10 (9 y 10), 13.2; sd-07 7.3 |
| R-03 | Presión comercial por una vista unificada o un cruce no catalogado → un dato del negocio financiero llega al retail sin base ni registro en el Servicio de control de cruces → infracción a la Ley 21.719 y quiebre de la línea roja | SEG | S | CA-3 | Caso cap. 10 (1), cap. 12, advertencia final cap. 17; sd-04 ADR-02 y vista de seguridad |
| R-04 | Ninguna persona conoce el mapa de las 14 interfaces → aparece en producción una integración no inventariada → falla una operación o un dato queda sin dueño tras el retiro de una plataforma | TEC | D, I | CA-4 | Caso cap. 10 (15); sd-04 4.1 (inventario pendiente antes de cerrar 4.1) |
| R-05 | Rotación anual del 62 % y 1.900 personas de temporada en el congelamiento de fin de año → el personal capacitado se va antes o durante la marcha blanca y la operación → errores en caja, uso de rodeos y caída de los resultados del Anexo D | ORG | I | CA-5 | Caso cap. 10 (13); sd-07 7.3 (capacitación como condición de cierre) |
| R-06 | La comisión se calcula hoy por canal de origen → el vendedor evita el flujo omnicanal que se le pide (retiro en tienda, pedido asistido) → baja adopción y datos de venta incompletos | ORG | S, I | CA-6 | Caso cap. 8 (vendedor de piso), cap. 11 (comisiones); sd-03 Servicio de comisiones (Etapa 2) |

## B. Riesgos nombrados por el Comunicado 10

| ID | Causa → evento → efecto | RBS | Mirada | Exigido | Fuente |
| :-- | :-- | :-- | :-- | :-- | :-- |
| R-07 | 56 meses de contrato sobre servicios administrados que cambian de versión (API Management Premium clásico, AKS, PostgreSQL) → un servicio llega a fin de soporte durante la operación → migración forzada no planificada | TEC | S | OB-1 | sd-04 4.1.1 (Tabla 4.6: los niveles v2 no están en Chile Central) |
| R-08 | La solución usa servicios propios de Azure (Event Hubs, API Management, AKS) → cambiar de proveedor o de región resulta costoso o imposible → Ancoa queda atada a un proveedor y a sus condiciones | TEC | S | OB-2 | sd-04 ADR-06 y ADR-07 (clientes Kafka como salida parcial) |
| R-09 | El evento anual concentra el equivalente a 22 días de venta en línea en tres días y la memoria de capacidad aún no está calculada → la reserva de existencia o la entrada API se saturan en el peak → pedidos cancelados como en junio | TEC | S | OB-3 | Caso 13.2; RT-09.06; sd-03 (memoria de capacidad pendiente) |
| R-10 | El ámbito de la norma de medios de pago está definido solo para el canal digital y la solución agrega cajas, emisión propia y nube → un compromiso de seguridad en tienda o en el ámbito del emisor → fuga de datos de tarjeta o de clientes y sanción | SEG | S | OB-4 | Caso cap. 12 (medios de pago); sd-04 vista de seguridad |
| R-11 | El cliente aporta 46 personas para nueve plataformas y la filial emisora debe decidir topes, reglas y actas → la Contraparte Técnica o los referentes no validan dentro de los diez días hábiles → se atrasan entregables de la ruta crítica | ORG | D | OB-5 | Caso cap. 17 (46 personas); Bases art. 18.3; sd-06 comités |

## C. Riesgos propios de la solución propuesta

| ID | Causa → evento → efecto | RBS | Mirada | Exigido | Fuente |
| :-- | :-- | :-- | :-- | :-- | :-- |
| R-12 | Con inicio en enero de 2027, la marcha blanca de la Etapa 1 (meses 13 a 15) cae casi entera en los congelamientos (hasta el 6 de enero y de la última semana de enero a la primera de marzo) → no se pueden corregir defectos durante la marcha blanca → el cierre se atrasa y arrastra el paso a producción del mes 16 | PRO | I | — | Caso 13.2; SUP-26; memoria del proyecto |

**R-12, versión ampliada (decisión del usuario, 2026-10-10, I-03).** Causa: con inicio en enero de 2027 (SUP-26), la marcha blanca de la Etapa 1 (meses 13 a 15, enero a marzo de 2028) coincide con dos congelamientos (hasta el 6 de enero y del 25 de enero al 6 de marzo, aprox.), y la restricción 9 del Caso prohíbe intervenir sistemas en ellos. Evento: un defecto detectado en la marcha blanca no puede corregirse en producción, o el propio inicio de la marcha blanca se considera una intervención prohibida. Efecto: el cierre de la marcha blanca se atrasa y arrastra el paso a producción del mes 16 (abril de 2028). Zona propuesta: crítica, porque toca un hito contractual sin holgura (sd-07, Tabla 7.6).
Respuesta propuesta (evitar):
1. La certificación de la Etapa 1 (mes 12, diciembre de 2027, EDT 1.9.8) se hace en Preproducción, que no es un sistema en producción del cliente, de modo que no choca con el congelamiento.
2. El despliegue que inicia la marcha blanca se ejecuta en la ventana libre del 7 al 24 de enero de 2028 (unas 2,5 semanas), solo con lo certificado.
3. Las correcciones que la marcha blanca acumule se liberan en la ventana libre desde la segunda semana de marzo hasta el 31 de marzo (unas 3,5 semanas), antes del paso a producción de abril.
4. Durante el congelamiento solo se permiten las correcciones de emergencia que autorice el Comité Ejecutivo.
Disparador: defectos abiertos de severidad alta al 20 de enero de 2028, o el despliegue no terminado al 24 de enero. Responsable: jefe de proyecto, con el calendario de la cuenta 1.1.6. Las fechas dependen de SUP-26 y de cómo se lean «última semana de enero» y «primera de marzo», y se recalculan si cambian.
| R-13 | La plataforma de crédito de 2011 se retira en el mes 22 y la remediación vence en el mes 24 → un tramo de la cartera no alcanza a migrar → soporte vencido o incumplimiento ante la CMF | PRO | D, I | OB-1 | Caso 13.1 y 13.2; sd-07 7.3 (fechas sin holgura); ventana medida abajo (EXT-G-03) |
**R-13, ventana de migración medida (EXT-G-03, 2026-10-11).** Se alineó el sd-03 con el sd-02: la cartera debe quedar migrada a más tardar el mes 22 (31 de octubre de 2028), porque el Caso prohíbe pasos a producción, cortes y apagados dentro de las cinco ventanas de congelamiento (Caso 13.2 y 13.3 punto 3; RT-10.05) y el congelamiento total va del 1 de noviembre al 6 de enero. Los meses 23 y 24 solo admiten observación, conciliación en lectura y el cierre documental de la remediación. Datos para calificar:
- Con inicio en enero de 2027 (SUP-26), la ventana va del 1 de abril de 2028 (mes 16) al 31 de octubre: 214 días corridos, de los cuales unos 197 son intervenibles (descontados el Día de la Madre, 7 días, y el evento anual con su semana previa, unos 10). Son cerca de 6,5 meses; el gerente financiero advierte en el Caso que la migración «no se hace en un semestre».
- El tramo con repactaciones, cobranzas y juicios depende de la Etapa 2 (producción en el mes 21, septiembre de 2028). Le queda un mes escaso para el corte, la conciliación y el apagado.
- Solo cabe si los tramos simples cortan desde abril, el tramo complejo convive durante la marcha blanca (meses 19 y 20) y el último corte es antes del 15 de octubre, con conciliación diaria hasta fin de mes y apagado antes del 31 de octubre.
- Efecto: holgura casi nula. Un atraso de un tramo cae en el congelamiento y la corrección queda bloqueada hasta el 7 de enero de 2029, ya fuera de «antes de 2029» (restricción 23 del Caso). Se vincula con R-25 y R-26.
Respuesta propuesta (evitar y mitigar): secuencia de cortes por tramo fijada desde el mes 16; último corte antes del 15 de octubre de 2028; reserva del tramo complejo en la marcha blanca de la Etapa 2; criterio de detención por discrepancia acordado con la filial emisora. Disparador: algún tramo sin corte al 15 de septiembre de 2028. Se recalcula si cambia SUP-26. Queda abierta una consulta al mandante: si «antes de 2029» admite los primeros días de enero de 2029 (hoy no se asume).
| R-14 | La filial emisora no fija los topes del cupo preaprobado o la prueba de corte de 24 h falla en los meses 6 y 7 → la compra con tarjeta propia sin enlace no se habilita → se activa el plan B (otro medio de pago) y cae la venta con crédito en contingencia | PRO | D | — | sd-03 3.2.3 (crédito sin conexión); `fundamentacion_credito_sin_conexion.md` |
| R-15 | Catorce tiendas sin enlace de respaldo acreditado y diario local nuevo → la sincronización tras un corte duplica o pierde ventas → cobros dobles o descuadre con ERP/DTE | TEC | S | — | Caso cap. 10 (5); sd-04 continuidad de 24 h y diario local |
| R-16 | La modalidad fiscal de contingencia para emitir documentos sin enlace no está aprobada por la autoridad tributaria → la tienda no puede emitir durante un corte → se incumple la restricción 5 o la 6 | EXT | S | — | sd-04 4.1 (Tabla 4.9, punto 6) |
| R-17 | La región de recuperación es Azure Brazil South → la asesoría jurídica o la CMF objetan la residencia de datos del emisor fuera de Chile → hay que rediseñar la recuperación del ámbito fiscalizado | EXT | S | — | sd-04 4.2 y 4.3.2; memoria del proyecto (sitio secundario en nube) |
| R-18 | El registro de inventario tiene 12,4 % de discrepancia y hay 24 instalaciones que no cierran para el corte → la carga inicial del Servicio de existencias hereda errores → el disponible publicado sigue sin ser confiable al mes 16 | TEC | I | — | Caso cap. 7 y cap. 17 (plan de trabajo); sd-03 3.2.5 (Anexo D). A conciliar con sd-05 |
| R-19 | La Ley 21.719 rige desde diciembre de 2026 y su reglamentación puede precisar exigencias → aparecen controles de datos personales no previstos → retrabajo en el Servicio de control de cruces y en la evidencia | EXT | S | — | Caso cap. 12; sd-03 Anexo (fundamento normativo) |
| R-20 | El cliente compra el hardware, contrata los enlaces y hace las obras → los equipos o enlaces de una tienda no están listos para su ola → se atrasa el despliegue gradual por tienda | EXT | I | — | Caso cap. 11; sd-03 SP-04 y RC-NN (Anexo A) |
| R-21 | Los 25 supuestos del 16.1 y los umbrales propuestos se validan con el cliente recién al inicio → el cliente rechaza un supuesto → cambio de alcance después de la línea base del mes 4 | PRO | D | — | Caso 16.1 y 17.1; sd-03 Anexo A; ficha sd-03 sección 7 |
| R-22 | 1.100 repositores externos y 640 terminales compartidas para 3.820 personas → no se puede imponer la herramienta ni asegurar acceso → conteos y verificación de etiquetas incompletos | OPE | S, I | — | Caso cap. 10 (11 y 12) |
| R-23 | Salida del jefe de proyecto, del arquitecto o del integrador del proponente en mitad de la Etapa 1 → pérdida de conocimiento → atraso en la ruta crítica | ORG | D | — | sd-06 (dedicación exclusiva del jefe de proyecto); sd-12 |

## D. Fuera del registro (se citan, no se duplican)

- Riesgos de adopción de las cinco innovaciones: sd-13 (exigencia del art. 29).
- Plan B del crédito y reversión de cada paso a producción: el detalle vive en sd-03 y T-18; el sd-08 solo los usa como respuesta.

## E. Nuevos candidatos (análisis de los subdocumentos, 2026-10-10)

Confiabilidad de la fuente: sd-01 a sd-04 están revisados. sd-06 y sd-07 tienen revisión pendiente: lo que sale de ellos se marca con (*) y se contrasta con el Caso antes de usarlo.

| ID | Causa → evento → efecto | RBS | Mirada | Fuente |
| :-- | :-- | :-- | :-- | :-- |
| R-24 | La Etapa 1 entra en producción en el mes 16 (abril de 2028) y el Día de la Madre (mes 17) y el evento anual (meses 17 y 18) llegan entre 4 y 10 semanas después → los servicios de existencias y ventas enfrentan su primer peak con defectos aún latentes → se repite el episodio de junio de 2026 | OPE | I | Caso 13.2; sd-02 2.2.4; sd-07 (*) l. 273 |
| R-25 | La plataforma de 2011 se retira en el mes 22 (octubre de 2028), justo antes del congelamiento de noviembre a enero, y el cierre de la remediación (mes 24) cae dentro de él → si algo falla después del retiro, la corrección o el retorno quedan bloqueados hasta enero de 2029 → incumplimiento ante la CMF | PRO | I | Caso 10 (9) y 13.2; sd-02 2.3.4 (718 días intervenibles); sd-07 (*) l. 305 |
| R-26 | Los clientes con repactación, cobranza o juicio migran en la Etapa 2, que tiene una sola marcha blanca de dos meses → hay poca convivencia para conciliar los casos más difíciles → divergencia o atraso del último tramo | TEC | I | sd-03 3.2.2 (reparto por tramos) |
| R-27 | Los seis proveedores actuales, en especial los de las plataformas que se reemplazan (2009, 2011 y POS 2014), pierden el contrato con el proyecto → no documentan interfaces, no exponen datos o no sostienen la convivencia → atraso de la integración y de la migración | EXT | D | sd-02 C2; sd-03 SP-01; sd-04 ADR-01 |
| R-28 | Hasta que el Servicio de evidencia financiera opera (mes 16), las grabaciones se siguen borrando a los 90 días → las repactaciones de 2027 se suman a las 1.240 sin evidencia → crece el pasivo de la remediación | EXT | D | sd-02 2.3.4; Caso cap. 10 (2) |
| R-29 | El procedimiento abierto por el SERNAC tras el evento de junio termina durante el proyecto → impone obligaciones nuevas → cambio de alcance después de la línea base | EXT | D | sd-02 2.3.1 |
| R-30 | Chile Central no tiene región emparejada y la creación de cada servicio Premium en la región está por comprobar → un servicio o su capacidad no está disponible al construir → rediseño o atraso de la plataforma base (mes 10, ruta crítica) | TEC | D | sd-04 ADR-07, 4.3.1 |
| R-31 | ERP/DTE, el núcleo de 2009 y el crédito de 2011 siguen en DC-01, con sala de respaldo en la misma comuna y una brecha de estándares cuyo informe de 2024 no se ha entregado → un evento local detiene la emisión tributaria o el crédito durante la convivencia aunque la nube siga → la tienda no emite documentos ni autoriza crédito | OPE | S | sd-04 4.2 y 4.3; rúbrica Informe 1 S4-13 |
| R-32 | La ubicación de las plataformas y los enlaces por tienda son supuestos (sd-04, SUP-27) y el ExpressRoute está por acreditar → el inventario cambia rutas y los plazos de provisión de enlaces → atraso de la plataforma base | EXT | D | sd-04 supuestos del emplazamiento; sd-02 SUP-27 |
| R-33 | Entre los meses 13 y 15 el mismo equipo sostiene la marcha blanca de la Etapa 1 y construye la Etapa 2 → sobreasignación → se atrasa una de las dos ramas críticas | PRO | D | sd-07 (*) l. 235 |
| R-34 | La meta de precio (< 3 %) depende de oleadas diurnas de cambio de etiquetas en papel hechas por el personal de tienda, y en campaña hay hasta 400.000 cambios al día → el personal no alcanza → no se cumple el resultado de precio del Anexo D | OPE | S | sd-02 2.3 y 2.3.2; SUP-09 |
| R-35 | Rotación del 62 %, temporada y terminales compartidas → accesos de ex trabajadores o temporales sin revocar → uso indebido de credenciales y quiebre de la segregación | SEG | S | sd-02 SUP-24 y C4; sd-01 (revisión de accesos) |
| R-36 | Transportistas, 310 vendedores de marketplace y medios de pago deben adoptar los contratos y estados exigidos → no los adoptan a tiempo → el servicio de pedidos no traza la entrega y la meta del 97 % no se puede medir | EXT | I | sd-03 3.4.3 y 3.4.6; Caso cap. 11 |
| R-37 | Siete decisiones del cliente deben tomarse antes de cerrar la 4.1 (aprobación jurídica de cada cruce, política etiqueta-caja, falta de stock posterior a la promesa, modalidad fiscal, decisión de riesgo del crédito sin enlace, memoria de capacidad, inventario de interfaces) → se demoran → la arquitectura no cierra con la línea base del mes 4 | ORG | D | sd-04 4.1 (l. 375); sd-03 3.4.6 (cierre) |
| R-38 | La tienda insignia vende el 17 % de lo presencial y el clúster de Santiago concentra la mitad de las tiendas → una falla del piloto o de una ola en ese clúster → impacto concentrado en la venta | OPE | I | sd-02 2.3 (Figura 2.3) |
| R-39 | El proponente tiene 85 profesionales, 16 en el núcleo, y el volumen estimado exige crecer el equipo → la contratación no llega a tiempo → atraso en el desarrollo de la Etapa 1 | ORG | D | sd-01 1.2 y 1.5; sd-07 (*) estimación |

## F. Fusiones propuestas

| Fusión | Resultado | Razón |
| :-- | :-- | :-- |
| R-01 + R-26 | R-01 con el tramo difícil como causa principal | Es el mismo evento (divergencia de saldos); R-26 explica por qué es probable |
| R-21 + R-37 | R-21 «decisiones y supuestos del cliente sin validar» | Las dos son decisiones del cliente que bloquean la línea base del mes 4 |
| R-23 + R-39 | R-23 «capacidad y continuidad del equipo del proponente» | Las dos son personas del proponente |
| R-12 se amplía | R-12 incluye que poner en marcha la marcha blanca en enero puede contar como intervención prohibida (Caso cap. 10, n.º 9) | sd-07 la planifica dentro del congelamiento como «operación supervisada sin cambios» y eso no resiste un defecto que haya que corregir |

Con las fusiones quedan **36 riesgos**. Es más que lo usual; ver la pregunta 1.

## G. Hallazgos que no son riesgos, pero afectan al sd-08

- **sd-07, Tabla 7.6:** todos los eslabones de la ruta crítica tienen holgura cero porque están anclados a fechas contractuales. Con esa red, Monte Carlo solo mostraría atraso, nunca holgura. La simulación se arma con la EDT de `80_Artefactos/sd-07_contexto/estimacion/` (164 cuentas, PERT de `12_plantilla_tres_valores.md` y horas de `16_horas_por_paquete.md`) y se mide contra los hitos fijos.
- **sd-07, l. 233 y 273:** planifica la marcha blanca de la Etapa 1 dentro del congelamiento. El sd-08 lo trata como riesgo (R-12) y conviene avisar a quien redacta el sd-07.
- **sd-07, tabla de frentes (l. 225):** la rama de innovaciones dice «por definir». Los riesgos de adopción se citan desde el sd-13 y no desde el sd-07.
- **sd-04:** DC-02 sigue en la misma comuna (la observación P0 S4-13 del profesor). La nube cubre lo nuevo, pero no lo heredado (R-31).
- **sd-05:** vacío. R-01, R-18 y R-26 quedan «a conciliar con sd-05».

## Preguntas para el usuario, con sugerencia

1. **¿Cuántos riesgos entran?** Sugerencia: registro completo de 36 en el T-16 y en el registro vivo; en el cuerpo de la 8.2 solo se desarrollan los de zona crítica o alta (unos 12 a 15) y los 11 exigidos (Caso y Comunicado), aunque queden más abajo. Así el capítulo no se vuelve catálogo y se cumple FEP04 · 44 (la matriz decide dónde se gastan horas).
2. **¿EXT como rama propia o fundida en PRO?** Sugerencia: rama propia, EXT, con dos sub-ramas (normativo y terceros). Son 10 riesgos y su respuesta es distinta (no se controlan, se monitorean y se transfieren por contrato). En la 8.2 se dice que las cinco categorías del Comunicado están cubiertas y que EXT es la sexta rama de FEP04 · 20. Alternativa: fundirla en PRO, lo que oculta el peso de los terceros, que el Caso cap. 11 pide hacer visible.
3. **¿Se agrega una oportunidad?** Sugerencia: sí, dos. O-01: el inventario de las 14 interfaces (mes 4) permite retirar antes alguna interfaz por archivo y liberar horas de conciliación. O-02: si la filial fija los topes antes del mes 6, la prueba de crédito sin enlace se adelanta y libera holgura para R-13. Una propuesta solo con amenazas se lee incompleta frente a FEP04 · 4.
4. **¿Se confirma SUP-26 (inicio en enero de 2027)?** Sugerencia: sí, se mantiene, porque los sd-02, sd-03 y sd-07 ya lo usan. En el sd-08 R-12, R-24 y R-25 se escriben dependiendo de él, con una frase que diga que se recalculan si cambia la fecha.
5. **¿Fusiones de la sección F?** Sugerencia: aceptarlas las cuatro.
