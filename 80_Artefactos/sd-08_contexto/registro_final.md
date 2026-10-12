# Registro final de riesgos del sd-08 (cierre de F1b)

Documento de contexto, no entregable. Creado el 2026-10-11 tras las diez decisiones (D1 a D10, ver `guia_progreso_sd-08.md`). Sin calificación todavía: probabilidad e impacto se asignan en F3 con las escalas de F2. Parte de `registro_candidatos.md`; si difieren en enunciado, manda este. Las líneas de las fuentes son del 2026-10-10 y 2026-10-11 y no se revalidaron.

## Qué cambió respecto de `registro_candidatos.md`

- **D5:** R-26 se absorbe en R-01 y R-39 en R-23. R-21 y R-37 quedan separados. Total: **37 riesgos**.
- **D2:** EXT desaparece como rama. Los 9 riesgos que la tenían pasan a PRO y se marcan en la columna «Ext.» (origen externo: normativo o de terceros). El registro tenía 9, no 10.
- **D3:** se agregan 8 oportunidades (O-01 a O-08), con su riesgo espejo.
- **D6:** R-31 se reformula como riesgo de contraparte (recinto, obra y hardware del cliente).
- **D7 y D8:** R-09 usa 104.000, 150.000 y 225.000; R-15 usa 14 tiendas (7 acreditadas).
- **R-06:** reformulado según `trazabilidad_riesgos.md` §4.1.
- **D1:** los 37 y las 8 oportunidades van al T-16; en el cuerpo del 8.2 solo se desarrollan los críticos, los altos y los 11 exigidos (CA-1 a CA-6 = R-01 a R-06; OB-1 a OB-5 = R-07 a R-11).

Claves: **RBS** TEC técnico, ORG organizacional, PRO de proyecto, SEG seguridad, OPE operación. **Mirada** (Informe 2): S solución, D desarrollo, I implantación. **Exigido:** CA-n riesgo esperado del Caso cap. 17; OB-n riesgo nombrado por el Comunicado 10 (1 obsolescencia, 2 bloqueo por proveedor, 3 escalabilidad, 4 ciberseguridad, 5 contrapartes). (*) fuente con revisión pendiente.

## Riesgos (37)

| ID | Causa → evento → efecto | RBS | Ext. | Mirada | Exigido | Fuente y notas |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| R-01 | Cartera viva con cuotas, repactaciones y cobranzas en curso, y un tramo difícil (repactación, cobranza, juicio) que migra en la Etapa 2 con una sola marcha blanca de dos meses → los saldos migrados por tramos divergen de la plataforma de 2011 o el último tramo se atrasa → se incumple la restricción 8, hay reclamos y exposición ante la CMF | TEC | — | I | CA-1 | Caso cap. 10 (8), 13.1, 16.1 (25); sd-03 3.2.2 y 3.2.3. A conciliar con sd-05 (absorbe R-26) |
| R-02 | La fecha del evento anual la fija la asociación gremial con unas seis semanas de aviso → el evento cae con un servicio a medio desplegar o dentro de una marcha blanca → caída de venta digital o congelamiento que desplaza trabajo de la ruta crítica | PRO | — | I | CA-2 | Caso cap. 10 (9 y 10), 13.2; sd-07 7.3 |
| R-03 | Presión comercial por una vista unificada o un cruce no catalogado → un dato del negocio financiero llega al retail sin base ni registro en el Servicio de control de cruces → infracción a la Ley 21.719 y quiebre de la línea roja | SEG | — | S | CA-3 | Caso cap. 10 (1), cap. 12, advertencia final cap. 19; sd-04 ADR-02 y vista de seguridad |
| R-04 | Ninguna persona conoce el mapa de las 14 interfaces → aparece en producción una integración no inventariada → falla una operación o un dato queda sin dueño tras el retiro de una plataforma | TEC | — | D, I | CA-4 | Caso cap. 10 (15); sd-04 4.1 (inventario pendiente antes de cerrar 4.1) |
| R-05 | Rotación anual del 62 % y 1.900 personas de temporada en el congelamiento de fin de año → el personal capacitado se va antes o durante la marcha blanca y la operación → errores en caja, uso de rodeos y caída de los resultados del Anexo D | ORG | — | I | CA-5 | Caso cap. 10 (13); sd-07 7.3 (capacitación como condición de cierre) |
| R-06 | La comisión se calcula hoy por canal de origen y la entrega de la información precontractual alarga la venta con tarjeta (desde el mes 16; el Servicio de comisiones llega en el mes 21) → el vendedor deja de ofrecer la tarjeta y evita el flujo omnicanal (retiro en tienda, pedido asistido) → baja colocación y adopción y datos de venta incompletos | ORG | — | S, I | CA-6 | Caso cap. 8 (vendedor de piso), cap. 11 (comisiones); sd-03 Servicio de comisiones (Etapa 2); sd-02 2.4.3. Reformulado según trazabilidad §4.1 |
| R-07 | 56 meses de contrato sobre servicios administrados que cambian de versión (API Management Premium clásico, AKS, PostgreSQL) → un servicio llega a fin de soporte durante la operación → migración forzada no planificada | TEC | — | S | OB-1 | sd-04 4.1.1 (Tabla 4.6: los niveles v2 no están en Chile Central) |
| R-08 | La solución usa servicios propios de Azure (Event Hubs, API Management, AKS) → cambiar de proveedor o de región resulta costoso o imposible → Ancoa queda atada a un proveedor y a sus condiciones | TEC | — | S | OB-2 | sd-04 ADR-06 y ADR-07 (clientes Kafka como salida parcial) |
| R-09 | El evento anual concentró 104.000 pedidos en tres días en 2026 (22 días de venta en línea), se proyectan unos 150.000 y la memoria de capacidad aún no está calculada → la reserva de existencia o la entrada API se saturan en el peak, que se prueba a 225.000 (1,5 × proyección, RT-09.06) → pedidos cancelados como en junio | TEC | — | S | OB-3 | Caso 13.2; RT-09.06; sd-03 (memoria de capacidad pendiente); sd-02 (cifras, D7) |
| R-10 | El ámbito de la norma de medios de pago está definido solo para el canal digital y la solución agrega cajas, emisión propia y nube → un compromiso de seguridad en tienda o en el ámbito del emisor → fuga de datos de tarjeta o de clientes y sanción | SEG | — | S | OB-4 | Caso cap. 12 (medios de pago); sd-04 vista de seguridad |
| R-11 | El cliente aporta 46 personas para nueve plataformas y la filial emisora debe decidir topes, reglas y actas → la Contraparte Técnica o los referentes no validan dentro de los diez días hábiles → se atrasan entregables de la ruta crítica | ORG | — | D | OB-5 | Caso cap. 19 (46 personas); Bases art. 18.3; sd-06 comités |
| R-12 | Con inicio en enero de 2027, la marcha blanca de la Etapa 1 (meses 13 a 15) cae casi entera en los congelamientos (hasta el 6 de enero y de la última semana de enero a la primera de marzo) → no se pueden corregir defectos durante la marcha blanca → el cierre se atrasa y arrastra el paso a producción del mes 16 | PRO | — | I | — | Caso 13.2; SUP-26; memoria del proyecto. Versión ampliada en `registro_candidatos.md` (I-03) |
| R-13 | La plataforma de crédito de 2011 se retira en el mes 22 y la remediación vence en el mes 24 → un tramo de la cartera no alcanza a migrar → soporte vencido o incumplimiento ante la CMF | PRO | — | D, I | OB-1 | Caso 13.1 y 13.2; sd-07 7.3 (fechas sin holgura); ventana medida abajo (EXT-G-03) |
| R-14 | La filial emisora no fija los topes del cupo preaprobado o la prueba de corte de 24 h falla en los meses 6 y 7 → la compra con tarjeta propia sin enlace no se habilita → se activa el plan B (otro medio de pago) y cae la venta con crédito en contingencia | PRO | — | D | — | sd-03 3.2.3 (crédito sin conexión); `fundamentacion_credito_sin_conexion.md` |
| R-15 | Catorce tiendas sin enlace de respaldo para dimensionar (siete acreditadas por el Caso, catorce por SUP-28) y diario local nuevo → la sincronización tras un corte duplica o pierde ventas → cobros dobles o descuadre con ERP/DTE | TEC | — | S | — | Caso cap. 10 (5); sd-04 continuidad de 24 h y diario local; sd-02 SUP-28 (D8) |
| R-16 | La modalidad fiscal de contingencia para emitir documentos sin enlace no está aprobada por la autoridad tributaria → la tienda no puede emitir durante un corte → se incumple la restricción 5 o la 6 | PRO | sí | S | — | sd-04 4.1 (Tabla 4.9, punto 6) |
| R-17 | La región de recuperación es Azure Brazil South → la asesoría jurídica o la CMF objetan la residencia de datos del emisor fuera de Chile → hay que rediseñar la recuperación del ámbito fiscalizado | PRO | sí | S | — | sd-04 4.2 y 4.3.2; memoria del proyecto (sitio secundario en nube) |
| R-18 | El registro de inventario tiene 12,4 % de discrepancia y hay 24 instalaciones que no cierran para el corte → la carga inicial del Servicio de existencias hereda errores → el disponible publicado sigue sin ser confiable al mes 16 | TEC | — | I | — | Caso cap. 7 y cap. 19 (24 instalaciones); sd-03 3.2.5 (Anexo D). A conciliar con sd-05 |
| R-19 | La Ley 21.719 rige desde diciembre de 2026 y su reglamentación puede precisar exigencias → aparecen controles de datos personales no previstos → retrabajo en el Servicio de control de cruces y en la evidencia | PRO | sí | S | — | Caso cap. 12; sd-03 Anexo (fundamento normativo) |
| R-20 | El cliente compra el hardware, contrata los enlaces y hace las obras → los equipos o enlaces de una tienda no están listos para su ola → se atrasa el despliegue gradual por tienda | PRO | sí | I | — | Caso cap. 11; sd-03 SP-04 y RC-NN (Anexo A) |
| R-21 | Los 25 supuestos del 16.1 y los umbrales propuestos se validan con el cliente recién al inicio → el cliente rechaza un supuesto → cambio de alcance después de la línea base del mes 4 | PRO | — | D | — | Caso 16.1 y 17.1; sd-03 Anexo A; ficha sd-03 sección 7 |
| R-22 | 1.100 repositores externos y 640 terminales compartidas para 3.820 personas → no se puede imponer la herramienta ni asegurar acceso → conteos y verificación de etiquetas incompletos | OPE | — | S, I | — | Caso cap. 10 (11 y 12) |
| R-23 | Salida del jefe de proyecto, del arquitecto o del integrador del proponente, o contratación que no llega a tiempo (85 profesionales, 16 en el núcleo, y el volumen exige crecer) → pérdida de conocimiento o falta de capacidad en mitad de la Etapa 1 → atraso en la ruta crítica | ORG | — | D | — | sd-06 (dedicación exclusiva del jefe de proyecto); sd-12; sd-01 1.2 y 1.5; sd-07 (*) estimación (absorbe R-39) |
| R-24 | La Etapa 1 entra en producción en el mes 16 (abril de 2028) y el Día de la Madre (mes 17) y el evento anual (meses 17 y 18) llegan entre 4 y 10 semanas después → los servicios de existencias y ventas enfrentan su primer peak con defectos aún latentes → se repite el episodio de junio de 2026 | OPE | — | I | — | Caso 13.2; sd-02 2.2.4; sd-07 (*) l. 273 |
| R-25 | La plataforma de 2011 se retira en el mes 22 (octubre de 2028), justo antes del congelamiento de noviembre a enero, y el cierre de la remediación (mes 24) cae dentro de él → si algo falla después del retiro, la corrección o el retorno quedan bloqueados hasta enero de 2029 → incumplimiento ante la CMF | PRO | — | I | — | Caso 10 (9) y 13.2; sd-02 2.3.4 (718 días intervenibles); sd-07 (*) l. 305 |
| R-27 | Los seis proveedores actuales, en especial los de las plataformas que se reemplazan (2009, 2011 y POS 2014), pierden el contrato con el proyecto → no documentan interfaces, no exponen datos o no sostienen la convivencia → atraso de la integración y de la migración | PRO | sí | D | — | sd-02 C2; sd-03 SP-01; sd-04 ADR-01 |
| R-28 | Hasta que el Servicio de evidencia financiera opera (mes 16), las grabaciones se siguen borrando a los 90 días → las repactaciones de 2027 se suman a las 1.240 sin evidencia → crece el pasivo de la remediación | PRO | sí | D | — | sd-02 2.3.4; Caso cap. 10 (2) |
| R-29 | El procedimiento abierto por el SERNAC tras el evento de junio termina durante el proyecto → impone obligaciones nuevas → cambio de alcance después de la línea base | PRO | sí | D | — | sd-02 2.3.1 |
| R-30 | Chile Central no tiene región emparejada y la creación de cada servicio Premium en la región está por comprobar → un servicio o su capacidad no está disponible al construir → rediseño o atraso de la plataforma base (mes 10, ruta crítica) | TEC | — | D | — | sd-04 ADR-07, 4.3.1 |
| R-31 | El recinto del cliente (DC-01, 140 m², habilitado en 2011) aloja ERP/DTE, el núcleo de 2009 y el crédito de 2011, con sala de respaldo en la misma comuna, una brecha de estándares cuyo informe de 2024 el cliente aún no entrega, y obra civil y hardware que ejecuta y compra el cliente → un evento local o una obra no lista detiene la emisión tributaria o el crédito durante la convivencia aunque la nube siga → la tienda no emite documentos ni autoriza crédito | OPE | — | S | — | sd-04 4.2 y 4.3; rúbrica Informe 1 S4-13; Caso l. 330; RT-06.06; RT-06.01. Riesgo de contraparte con mitigación del proponente (D6). Comparte causa con R-20 |
| R-32 | La ubicación de las plataformas y los enlaces por tienda son supuestos (sd-04, SUP-27) y el ExpressRoute está por acreditar → el inventario cambia rutas y los plazos de provisión de enlaces → atraso de la plataforma base | PRO | sí | D | — | sd-04 supuestos del emplazamiento; sd-02 SUP-27 |
| R-33 | Entre los meses 13 y 15 el mismo equipo sostiene la marcha blanca de la Etapa 1 y construye la Etapa 2 → sobreasignación → se atrasa una de las dos ramas críticas | PRO | — | D | — | sd-07 (*) l. 235 |
| R-34 | La meta de precio (< 3 %) depende de oleadas diurnas de cambio de etiquetas en papel hechas por el personal de tienda, y en campaña hay hasta 400.000 cambios al día → el personal no alcanza → no se cumple el resultado de precio del Anexo D | OPE | — | S | — | sd-02 2.3 y 2.3.2; SUP-09 |
| R-35 | Rotación del 62 %, temporada y terminales compartidas → accesos de ex trabajadores o temporales sin revocar → uso indebido de credenciales y quiebre de la segregación | SEG | — | S | — | sd-02 SUP-24 y C4; sd-01 (revisión de accesos) |
| R-36 | Transportistas, 310 vendedores de marketplace y medios de pago deben adoptar los contratos y estados exigidos → no los adoptan a tiempo → el servicio de pedidos no traza la entrega y la meta del 97 % no se puede medir | PRO | sí | I | — | sd-03 3.4.3 y 3.4.6; Caso cap. 11 |
| R-37 | Siete decisiones del cliente deben tomarse antes de cerrar la 4.1 (aprobación jurídica de cada cruce, política etiqueta-caja, falta de stock posterior a la promesa, modalidad fiscal, decisión de riesgo del crédito sin enlace, memoria de capacidad, inventario de interfaces) → se demoran → la arquitectura no cierra con la línea base del mes 4 | ORG | — | D | — | sd-04 4.1 (l. 375); sd-03 3.4.6 (cierre) |
| R-38 | La tienda insignia vende el 17 % de lo presencial y el clúster de Santiago concentra la mitad de las tiendas → una falla del piloto o de una ola en ese clúster → impacto concentrado en la venta | OPE | — | I | — | sd-02 2.3 (Figura 2.3) |

## Oportunidades (8)

Se redactan con condición explícita («si…, entonces…») y no se cuentan en ninguna reserva ni en la simulación. En el cuerpo del 8.2 se desarrollan O-02, O-03, O-05 y O-06; las demás van solo en el T-16. Los riesgos de adopción de las cinco innovaciones se citan desde el sd-13, sin duplicarlos.

| ID | Si… entonces… | Riesgo espejo | Estrategia | Fuente |
| :-- | :-- | :-- | :-- | :-- |
| O-01 | El inventario de las 14 interfaces (mes 4) permite retirar antes alguna interfaz por archivo → se liberan horas de conciliación | R-04 | Explotar | 1.2.1; sd-04 ADR-01 |
| O-02 | La filial emisora fija los topes del cupo preaprobado antes del mes 6 → la prueba de corte de 24 h se adelanta y libera holgura para la ventana de migración de cartera | R-14, R-13 | Mejorar | sd-03 3.2.3 |
| O-03 | La carga inicial de existencias usa el conteo cíclico y la detección de discrepancias de la innovación 2 (y libera horas de conteo en tienda tras la marcha blanca) → la discrepancia del 12,4 % baja antes del corte | R-18 | Explotar | sd-13 innovación 2; Caso cap. 7 |
| O-04 | El Servicio de evidencia financiera entra antes del mes 16 → se detiene el borrado a los 90 días y el pasivo de 1.240 repactaciones deja de crecer | R-28 | Mejorar | sd-02 2.3.4; Caso cap. 10 (2) |
| O-05 | La cartera sin casos difíciles migra completa antes del mes 22 → queda margen de observación antes del congelamiento de noviembre | R-13, R-25 | Mejorar | sd-02 2.3.4; EXT-G-03 |
| O-06 | Los datos del evento anual de 2026 y de ediciones previas calibran la memoria de capacidad antes del evento (y después liberan capacidad no usada) → se dimensiona con medición y no con margen ciego | R-09 | Mejorar | RT-09.06; sd-04 4.2 |
| O-07 | Los proveedores actuales colaboran y entregan documentación de sus interfaces temprano → la integración y la convivencia se adelantan | R-27 | Compartir | sd-03 SP-01; sd-04 ADR-01 |
| O-08 | El cliente compra el hardware y contrata los enlaces antes de la ola de cada tienda → el despliegue gradual se adelanta | R-20 | Compartir | Caso cap. 11; sd-03 SP-04 |

## Conteos

| RBS | Riesgos |
| :-- | --: |
| TEC | 8 |
| ORG | 5 |
| PRO | 16 |
| SEG | 3 |
| OPE | 5 |
| **Total** | **37** |

| Mirada | Riesgos que la tocan (uno puede tocar varias) |
| :-- | --: |
| S | 14 |
| D | 13 |
| I | 14 |

Ninguna rama queda vacía. Riesgos con origen externo (columna «Ext.»): R-16, R-17, R-19, R-20, R-27, R-28, R-29, R-32, R-36.

## Pendientes que arrastra el registro

- R-01 y R-18 quedan «a conciliar con sd-05», que sigue como esqueleto.
- Cuentas nuevas de la EDT para R-06, R-27, R-28 y R-36: `guia_cuentas_nuevas_sd-07.md`.
- Cambios en otros subdocumentos por D4, D6 y D8: `cambios_por_D4_D8.md` y `cambios_por_D6.md`.
- R-07 y R-13 llevan ambos OB-1 en la fuente; revisar al calificar si R-13 debe llevarlo.
