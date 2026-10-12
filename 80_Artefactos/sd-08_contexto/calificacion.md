# Calificación y respuesta de los 37 riesgos y las 8 oportunidades del sd-08 (F3)

Documento de contexto, no entregable, fechado el 2026-10-12. Aplica las escalas, zonas y reglas aprobadas el 2026-10-11 en `escalas_propuestas.md` a los 37 riesgos de `registro_final.md`.
Es una propuesta de un agente, pendiente de revisión humana: toda calificación, fecha de disparador, semana y hora marcada «est.» es estimación del proponente, no dato del Caso. Las cuentas «(propuesta)» no existen aún en la EDT del sd-07.

Valores: P 0,05 / 0,20 / 0,40 / 0,60 / 0,85; I 0,05 / 0,10 / 0,20 / 0,40 / 0,80. Zonas: crítica ≥ 0,40; alta ≥ 0,20; media ≥ 0,08; baja < 0,08. Las exposiciones se redondean a dos decimales.

## Tabla 1. Calificación

| ID | RBS | Mirada | P (nivel) | P (valor) | I (nivel) | I (valor) | Dimensión | Exposición | Zona | Justificación |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| R-01 | TEC | I | 3 | 0,40 | 5 | 0,80 | Servicio | 0,32 | Alta | El tramo difícil (repactación, cobranza, juicio) migra con una sola marcha blanca de dos meses y una divergencia incumple la restricción 8 y expone ante la CMF, pero el diseño de migración aún está por conciliar con el sd-05. |
| R-02 | PRO | I | 4 | 0,60 | 5 | 0,80 | Plazo (hito mes 16) | 0,48 | Crítica | El evento anual se repite cada año con unas seis semanas de aviso y el sd-07 tiene holgura cero, por lo que un cruce con un despliegue desplaza 3 a 6 semanas de la ruta crítica. Atrasa la ruta crítica, que no tiene holgura, por lo que rige la regla del hito contractual (I = 5). |
| R-03 | SEG | S | 2 | 0,20 | 5 | 0,80 | Servicio (línea roja) | 0,16 | Media | Un cruce sin base quiebra la línea roja (I = 5 por regla), pero el Servicio de control de cruces y el ADR-02 lo bloquean por diseño, de modo que la probabilidad es baja. |
| R-04 | TEC | D, I | 4 | 0,60 | 3 | 0,20 | Servicio | 0,12 | Media | Nadie conoce hoy el mapa de las 14 interfaces punto a punto, pero el inventario del mes 4 (1.2.1) acota el efecto a una degradación con rodeo. |
| R-05 | ORG | I | 5 | 0,85 | 3 | 0,20 | Servicio | 0,17 | Media | La rotación anual del 62 % hace casi segura la pérdida de personal capacitado, con efecto de degradación en caja y rodeos disponibles (Anexo D). |
| R-06 | ORG | S, I | 3 | 0,40 | 3 | 0,20 | Alcance y calidad | 0,08 | Media | La comisión por canal de origen y la información precontractual alargan la venta con tarjeta desde el mes 16, antes de que el Servicio de comisiones llegue en el mes 21, con efecto sobre áreas funcionales clave (colocación y flujo omnicanal). |
| R-07 | TEC | S | 3 | 0,40 | 3 | 0,20 | Esfuerzo | 0,08 | Media | En 56 meses es plausible que API Management Premium clásico, AKS o PostgreSQL lleguen a fin de soporte, y la migración forzada cuesta entre 1 y 2 % de las horas. |
| R-08 | TEC | S | 2 | 0,20 | 4 | 0,40 | Esfuerzo | 0,08 | Media | Salir de Event Hubs, API Management y AKS sería costoso, pero los clientes Kafka (ADR-06 y ADR-07) y la IaC (1.4.1) dejan una salida parcial. |
| R-09 | TEC | S | 3 | 0,40 | 4 | 0,40 | Servicio | 0,16 | Media | Se proyectan 150.000 pedidos en tres días (104.000 en 2026) y se prueba a 225.000, pero la memoria de capacidad aún no está calculada; una saturación cancelaría pedidos como en junio. |
| R-10 | SEG | S | 2 | 0,20 | 5 | 0,80 | Servicio | 0,16 | Media | Una fuga de datos de tarjeta con sanción es de efecto máximo, pero el compromiso requiere vencer los controles de red de tienda y del emisor (1.8.1 y 1.8.6) y existe prueba de penetración (Anexo D 21). |
| R-11 | ORG | D | 3 | 0,40 | 5 | 0,80 | Plazo (hito mes 16) | 0,32 | Alta | El cliente aporta 46 personas para nueve plataformas y debe validar en diez días hábiles; cada validación tardía atrasa 3 a 6 semanas un entregable de la ruta crítica. Atrasa la ruta crítica, que no tiene holgura, por lo que rige la regla del hito contractual (I = 5). |
| R-12 | PRO | I | 4 | 0,60 | 5 | 0,80 | Plazo (hito mes 16) | 0,48 | Crítica | Con inicio en enero de 2027 la marcha blanca de los meses 13 a 15 cae casi entera en los congelamientos (hasta el 6 de enero y desde la última semana de enero a la primera de marzo) y el sd-07 la planifica sin correcciones, lo que arrastra el paso a producción del mes 16. |
| R-13 | PRO | D, I | 4 | 0,60 | 5 | 0,80 | Plazo (hito mes 22) | 0,48 | Crítica | La ventana de migración mide cerca de 197 días intervenibles entre abril y octubre de 2028, con holgura casi nula y el tramo complejo dependiente de la Etapa 2 (mes 21); un atraso cae en el congelamiento y rebasa «antes de 2029». |
| R-14 | PRO | D | 3 | 0,40 | 3 | 0,20 | Servicio | 0,08 | Media | Si la filial no fija los topes o la prueba de corte de 24 h falla en los meses 6 y 7, la venta con crédito en contingencia cae, pero queda el plan B con otro medio de pago. |
| R-15 | TEC | S | 3 | 0,40 | 4 | 0,40 | Servicio | 0,16 | Media | Catorce tiendas sin enlace de respaldo para dimensionar (7 acreditadas por el Caso) y un diario local nuevo hacen posible un cobro doble o un descuadre con ERP/DTE tras el corte, sin llegar a pérdida masiva de datos. |
| R-16 | PRO | S | 3 | 0,40 | 5 | 0,80 | Servicio | 0,32 | Alta | La modalidad fiscal de contingencia no está aprobada por la autoridad tributaria (sd-04 Tabla 4.9, punto 6), y sin ella un corte incumple las restricciones 5 o 6. |
| R-17 | PRO | S | 3 | 0,40 | 4 | 0,40 | Alcance y calidad | 0,16 | Media | La región de recuperación es Azure Brazil South, fuera de Chile, y una objeción de la CMF o de la asesoría jurídica obligaría a rediseñar la recuperación del ámbito fiscalizado. |
| R-18 | TEC | I | 4 | 0,60 | 4 | 0,40 | Alcance y calidad | 0,24 | Alta | Con 12,4 % de discrepancia y 24 instalaciones que no cierran para el corte, la carga inicial hereda errores y el disponible publicado no es confiable al mes 16. |
| R-19 | PRO | S | 3 | 0,40 | 3 | 0,20 | Esfuerzo | 0,08 | Media | La Ley 21.719 rige desde diciembre de 2026 y su reglamentación puede precisar controles, con retrabajo acotado al Servicio de control de cruces y a la evidencia. |
| R-20 | PRO | I | 4 | 0,60 | 4 | 0,40 | Plazo | 0,24 | Alta | El cliente compra el hardware, contrata los enlaces y hace las obras de 14 tiendas, y cada ola depende de ello; un atraso de una ola desplaza el despliegue gradual 3 a 6 semanas. |
| R-21 | PRO | D | 4 | 0,60 | 3 | 0,20 | Alcance y calidad | 0,12 | Media | Es probable que el cliente rechace o matice alguno de los 25 supuestos del 16.1 al validarlos, con cambio de alcance acotado a áreas puntuales antes de la línea base del mes 4. |
| R-22 | OPE | S, I | 4 | 0,60 | 3 | 0,20 | Servicio | 0,12 | Media | Los 1.100 repositores externos y las 640 terminales compartidas para 3.820 personas impiden imponer la herramienta, con conteos incompletos pero con rodeo disponible. |
| R-23 | ORG | D | 3 | 0,40 | 5 | 0,80 | Plazo (hito mes 16) | 0,32 | Alta | Entre 85 profesionales y un núcleo de 16, la salida del jefe de proyecto, del arquitecto o del integrador a mitad de la Etapa 1 atrasaría 3 a 6 semanas la ruta crítica. Atrasa la ruta crítica, que no tiene holgura, por lo que rige la regla del hito contractual (I = 5). |
| R-24 | OPE | I | 4 | 0,60 | 4 | 0,40 | Servicio | 0,24 | Alta | La producción de la Etapa 1 es en abril de 2028 y el Día de la Madre y el evento anual llegan entre 4 y 10 semanas después, con defectos latentes y riesgo de repetir el episodio de junio de 2026. |
| R-25 | PRO | I | 3 | 0,40 | 5 | 0,80 | Servicio (hito mes 22) | 0,32 | Alta | El retiro de la plataforma de 2011 es en octubre de 2028, antes del congelamiento de noviembre a enero, y si algo falla después la corrección queda bloqueada hasta el 7 de enero de 2029; la falla requiere que antes falle algo más, por eso P = 3. |
| R-27 | PRO | D | 3 | 0,40 | 4 | 0,40 | Plazo | 0,16 | Media | Seis proveedores, tres de ellos de plataformas que se reemplazan (2009, 2011 y POS 2014), pueden no documentar interfaces ni sostener la convivencia, con atraso de 3 a 6 semanas en integración y migración. |
| R-28 | PRO | D | 5 | 0,85 | 3 | 0,20 | Alcance y calidad | 0,17 | Media | Hasta el mes 16 las grabaciones se borran a los 90 días y las repactaciones de 2027 se suman a las 1.240 sin evidencia, lo que es casi seguro si no cambia la política del cliente. |
| R-29 | PRO | D | 2 | 0,20 | 3 | 0,20 | Alcance y calidad | 0,04 | Baja | El procedimiento abierto por el SERNAC tras el evento de junio de 2026 puede terminar durante el proyecto, pero no hay dato de que imponga obligaciones fuera del control de cambios (1.1.3). |
| R-30 | TEC | D | 2 | 0,20 | 4 | 0,40 | Plazo | 0,08 | Media | Chile Central no tiene región emparejada y cada servicio Premium está por comprobar, con efecto sobre la plataforma base del mes 10. |
| R-31 | OPE | S | 2 | 0,20 | 5 | 0,80 | Servicio | 0,16 | Media | DC-01 (140 m², habilitado en 2011) aloja ERP/DTE y el crédito de 2011 con respaldo en la misma comuna; un evento local es poco frecuente, pero detiene la emisión tributaria y el crédito (restricciones 5 y 6). El recinto, la obra y el hardware son del cliente, por lo que es un riesgo de contraparte. |
| R-32 | PRO | D | 3 | 0,40 | 3 | 0,20 | Plazo | 0,08 | Media | La ubicación de las plataformas y los enlaces por tienda son supuestos (SUP-27) y el ExpressRoute está por acreditar, con atraso de 1 a 3 semanas en la plataforma base. |
| R-33 | PRO | D | 3 | 0,40 | 5 | 0,80 | Plazo (hitos meses 16 y 21) | 0,32 | Alta | Entre los meses 13 y 15 el mismo equipo sostiene la marcha blanca de la Etapa 1 y construye la Etapa 2; la nivelación del T-15 está parcial (fuente con revisión pendiente). Atrasa la ruta crítica, que no tiene holgura, por lo que rige la regla del hito contractual (I = 5). |
| R-34 | OPE | S | 4 | 0,60 | 4 | 0,40 | Alcance y calidad | 0,24 | Alta | La meta de error de precio es menos de 3 % y el sd-02 calcula que el papel no baja de 2,6 %, con hasta 400.000 cambios al día en campaña, de modo que el margen es estrecho. |
| R-35 | SEG | S | 2 | 0,20 | 5 | 0,80 | Servicio (línea roja) | 0,16 | Media | Con rotación del 62 % y 640 terminales compartidas hay accesos sin revocar, pero el uso indebido que quiebre la segregación exige además que alguien lo explote, y hay revisión de accesos (1.5.14.1). |
| R-36 | PRO | I | 3 | 0,40 | 3 | 0,20 | Alcance y calidad | 0,08 | Media | Transportistas, 310 vendedores de marketplace y medios de pago pueden no adoptar los contratos de estado a tiempo, con efecto sobre la medición de la meta del 97 %. |
| R-37 | ORG | D | 3 | 0,40 | 5 | 0,80 | Plazo (hito mes 16) | 0,32 | Alta | Siete decisiones del cliente deben tomarse antes de cerrar la 4.1 y una demora aplaza 3 a 6 semanas el cierre de arquitectura frente a la línea base del mes 4. Atrasa la ruta crítica, que no tiene holgura, por lo que rige la regla del hito contractual (I = 5). |
| R-38 | OPE | I | 2 | 0,20 | 3 | 0,20 | Servicio | 0,04 | Baja | La tienda insignia vende el 17 % de lo presencial y el clúster de Santiago concentra la mitad de las tiendas, pero la selección de pilotos y olas (1.11.5 y 1.11.1) permite acotar el efecto a una degradación con rodeo. |

## Tabla 2. Respuesta

Las columnas Semanas y Horas solo se completan para zona crítica o alta, y son estimación del proponente. El responsable es un rol. Los disparadores con fecha son propuestos y se recalculan si cambia SUP-26 (inicio en enero de 2027). El residual se escribe como P×I = valor, tras aplicar la respuesta.

| ID | Estrategia | Acción | Cuenta EDT | Responsable | Disparador | Residual (P×I) | Semanas (est.) | Horas (est.) | Supuesto de la estimación |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| R-01 | Mitigar | Fijar la secuencia de cortes por tramo, con conciliación diaria y criterio de detención por discrepancia acordado con la filial emisora, y reservar el tramo difícil en la marcha blanca de la Etapa 2. | 1.7.1, 1.7.6, 1.7.12, 1.5.40 | Líder de Datos y Migración | Divergencia sin conciliar dos días consecutivos en un tramo (umbral por definir con la filial) | P2×I5 = 0,16 | 4 | 960 | Se repite un corte de tramo con 6 personas dedicadas a 40 h por semana. |
| R-02 | Mitigar | Fijar ocho semanas sin despliegues antes del evento anual y programar las entregas previas fuera de ellas. | 1.1.5, 1.9.5 | Jefe de Proyecto | Recepción de la fecha del evento con menos de 8 semanas de aviso, o servicio a medio desplegar en esa fecha | P3×I5 = 0,32 | 3 | 600 | Se reordenan entregas con 5 personas durante 3 semanas. |
| R-03 | Evitar | Mantener el Servicio de control de cruces como único camino de datos entre retail y filial emisora, con registro de base legal por cada cruce. | 1.5.13.1, 1.5.13.2, 1.5.13.3, 1.3.4, 1.8.7 | Arquitecto de Soluciones | Un solo cruce sin base o sin registro detectado (umbral cero) | P1×I5 = 0,04 | — | — | — |
| R-04 | Mitigar | Cerrar el inventario de las 14 interfaces antes de la línea base y certificar cada integración antes de retirar una plataforma. | 1.2.1, 1.6.1, 1.6.11 | Líder de Integración | Inventario no cerrado al mes 4 (abril de 2027) | P2×I3 = 0,04 | — | — | — |
| R-05 | Mitigar | Hacer de la capacitación condición de cierre de la marcha blanca y repetir la capacitación en el entorno de temporada. | 1.13.2, 1.13.3, 1.13.4, 1.15.8 | Líder de Gestión del Cambio | Personal capacitado bajo el umbral de cierre de marcha blanca (umbral por definir en 1.13.3) | P4×I3 = 0,12 | — | — | — |
| R-06 | Mitigar | Acordar con la filial emisora la regla de comisión del vendedor antes del mes 13 y simplificar la entrega de información precontractual. | 1.13.1 | Jefe de Proyecto | Acta de comisión sin firma al mes 13 (enero de 2028) | P2×I3 = 0,04 | — | — | — |
| R-07 | Mitigar | Llevar un calendario de ciclo de vida de los servicios administrados y planificar cada migración con un año de anticipación. | 1.15.4, 1.4.7 | Arquitecto de Soluciones | Servicio a menos de 12 meses de su fin de soporte | P2×I3 = 0,04 | — | — | — |
| R-08 | Mitigar | Definir la infraestructura como código y el plan de reversibilidad, con clientes Kafka como salida parcial. | 1.4.1, 1.14.6 | Arquitecto de Soluciones | Plan de reversibilidad no aceptado a la fecha de su entrega (por definir en 1.14.6) | P1×I4 = 0,02 | — | — | — |
| R-09 | Mitigar | Calcular la memoria de capacidad con los datos de 2026, probar a 225.000 pedidos y dimensionar la reserva de existencia y la entrada API. | 1.3.7, 1.9.4, 1.9.6 | Líder de Rendimiento y Calidad | Prueba a 225.000 pedidos en tres días sin cumplir antes del mes 16 | P2×I4 = 0,08 | — | — | — |
| R-10 | Mitigar | Delimitar con la CMF y la asesoría jurídica el ámbito de medios de pago, segmentar la red de tienda y ejecutar la prueba de penetración. | 1.8.1, 1.8.6, 1.8.9, 1.4.2 | Responsable de Seguridad | Hallazgo crítico en la prueba de penetración (Anexo D 21) | P1×I5 = 0,04 | — | — | — |
| R-11 | Mitigar | Pactar actas con plazo de diez días hábiles y escalar a la Contraparte Técnica la validación vencida. | 1.1.6, 1.1.8 | Jefe de Proyecto | Acta sin validar al décimo día hábil | P2×I5 = 0,16 | 3 | 360 | Tres personas detenidas tres semanas a 40 h por una validación vencida. |
| R-12 | Evitar | Certificar la Etapa 1 en Preproducción en el mes 12, desplegar en la ventana libre del 7 al 24 de enero de 2028, corregir en la ventana desde la segunda semana de marzo y limitar el congelamiento a correcciones de emergencia autorizadas por el Comité Ejecutivo. | 1.12.1, 1.1.5 | Jefe de Proyecto | Defectos de severidad alta abiertos al 20 de enero de 2028, o despliegue no terminado al 24 de enero | P2×I5 = 0,16 | 4 | 1.280 | Se pierde la ventana de corrección de 3,5 semanas con 8 personas a 40 h por semana. |
| R-13 | Evitar | Fijar desde el mes 16 la secuencia de cortes por tramo, con último corte antes del 15 de octubre de 2028, el tramo complejo en la marcha blanca de la Etapa 2 y escalamiento al Comité Ejecutivo. | 1.7.8, 1.7.9, 1.7.12 | Líder de Datos y Migración | Algún tramo sin corte al 15 de septiembre de 2028 | P3×I5 = 0,32 | 6 | 1.920 | Se rehace un corte de tramo y su conciliación con 8 personas durante 6 semanas. |
| R-14 | Mitigar | Fijar con la filial los topes del cupo preaprobado antes del mes 6 y mantener el plan B de otro medio de pago. | 1.1.14, 1.2.10, 1.5.10.4, 1.9.11, 1.11.5 | Arquitecto de Soluciones | Topes sin fijar al mes 6 (junio de 2027), o prueba de corte de 24 h fallida en los meses 6 y 7 | P2×I3 = 0,04 | — | — | — |
| R-15 | Mitigar | Dimensionar según el inventario de enlaces (entre 7 y 14 tiendas) y probar la sincronización del diario local tras un corte de 24 h. | 1.3.6, 1.5.5.2, 1.9.11 | Arquitecto de Soluciones | Prueba de 24 h con una venta duplicada o perdida | P2×I3 = 0,04 | — | — | — |
| R-16 | Escalar | Gestionar la aprobación de la modalidad fiscal de contingencia con la autoridad tributaria y escalarla al Comité Ejecutivo si no avanza. | 1.6.7 | Jefe de Proyecto | Modalidad sin aprobar al mes 9 (septiembre de 2027), previo a la certificación del mes 12 | P2×I5 = 0,16 | 4 | 640 | Se rediseña la emisión sin enlace con 4 personas durante 4 semanas. |
| R-17 | Mitigar | Obtener el pronunciamiento de la asesoría jurídica y de la CMF sobre la residencia de datos y mantener una alternativa de recuperación dentro de Chile. | 1.8.10 | Responsable de Seguridad | Sin pronunciamiento antes de la línea base del mes 4 | P2×I3 = 0,04 | — | — | — |
| R-18 | Mitigar | Cargar existencias con conteo cíclico y detección de discrepancias, y conciliar las 24 instalaciones antes del corte. | 1.7.2, 1.7.3, 1.5.10 | Líder de Datos y Migración | Diferencia de conteo igual o superior a 2 % en la carga de prueba por categoría (resultado 4 del Anexo D). | P3×I3 = 0,08 | 5 | 1.200 | Se repite la carga y conciliación con 6 personas durante 5 semanas. |
| R-19 | Aceptar | Monitorear la reglamentación de la Ley 21.719 y absorber los ajustes en la matriz de cumplimiento. | 1.8.7 | Responsable de Seguridad | Publicación de una norma o reglamento que cambie un control | P3×I3 = 0,08 | — | — | — |
| R-20 | Transferir | Fijar por contrato las responsabilidades del cliente (hardware, enlaces, obras) con fechas por ola y exigir la certificación de sitio antes de cada ola. | 1.3.7, 1.4.8, 1.11.2 | Líder de Implantación | Certificación de sitio no emitida 8 semanas antes de la ola de una tienda | P3×I3 = 0,08 | 4 | 640 | Se reprograma una ola con 4 personas durante 4 semanas. |
| R-21 | Evitar | Validar los 25 supuestos y los umbrales con el cliente antes de la línea base del mes 4. | 1.2.6, 1.1.4, 1.1.3 | Jefe de Proyecto | Supuestos sin validar al mes 3 (marzo de 2027) | P2×I3 = 0,04 | — | — | — |
| R-22 | Mitigar | Asegurar acceso individualizado por proveedor y turnos de terminales compartidas para el conteo y la verificación de etiquetas. | 1.13.4, 1.5.14.2 | Líder de Gestión del Cambio | Conteos incompletos en el piloto (umbral por definir) | P3×I3 = 0,08 | — | — | — |
| R-23 | Mitigar | Nombrar suplentes de los roles clave, documentar el conocimiento y adelantar la contratación según el plan de recursos. | 1.1.1 | Jefe de Proyecto | Vacante de un rol clave sin cubrir por más de 30 días | P2×I5 = 0,16 | 4 | 480 | Reemplazo y traspaso de un rol clave con tres personas durante cuatro semanas. |
| R-24 | Mitigar | Ampliar el soporte reforzado entre la producción y el Día de la Madre y el evento anual, y cerrar los defectos de severidad alta antes de abril de 2028. | 1.9.5, 1.12.7 | Líder de Operación | Defectos de severidad alta abiertos a 4 semanas del Día de la Madre | P3×I3 = 0,08 | 3 | 960 | Se corrigen defectos en producción con 8 personas durante 3 semanas. |
| R-25 | Evitar | Cortar el último tramo antes del 15 de octubre de 2028, conciliar a diario hasta fin de mes y acordar con el Comité Ejecutivo un plan de retorno para el congelamiento. | 1.7.8, 1.7.9 | Líder de Datos y Migración | Algún tramo sin corte al 15 de octubre de 2028 | P2×I5 = 0,16 | 10 | 2.400 | La corrección se bloquea del 1 de noviembre al 7 de enero con 6 personas en espera y ajuste. |
| R-27 | Mitigar | Firmar con los seis proveedores actuales acuerdos de cooperación y salida, con documentación de interfaces y extracción de datos. | 1.2.1 | Jefe de Proyecto | Documentación de interfaces sin entregar por un proveedor al mes 4 (abril de 2027) | P2×I3 = 0,04 | — | — | — |
| R-28 | Mitigar | Especificar la retención de grabaciones de repactación y acompañar la decisión del cliente de cambiar su política de 90 días. | 1.8.5 | Arquitecto de Datos | Decisión del cliente sin tomar al mes 6 (junio de 2027) | P2×I3 = 0,04 | — | — | — |
| R-29 | Aceptar | Gestionar cualquier obligación nueva por el control de cambios y monitorear el procedimiento. | 1.1.3 | Jefe de Proyecto | Notificación de una obligación nueva del SERNAC | P2×I3 = 0,04 | — | — | — |
| R-30 | Evitar | Probar la creación de cada servicio Premium en Chile Central al inicio del proyecto, antes de construir la plataforma base. | 1.4.1 | Arquitecto de Soluciones | Un servicio no creable en Chile Central en la prueba de recursos | P1×I4 = 0,02 | — | — | — |
| R-31 | Escalar | Resolver con el Comité Ejecutivo qué parte provee el cliente y qué el proponente (inconsistencia I-02), cerrar la brecha de estándares y definir el respaldo fuera de la comuna. | 1.4.11 | Responsable de Infraestructura | Informe de brecha de 2024 sin entregar al mes 4 (abril de 2027) | P1×I5 = 0,04 | — | — | — |
| R-32 | Mitigar | Confirmar con el inventario las ubicaciones y las rutas, y acreditar el ExpressRoute antes del diseño final. | 1.2.1, 1.3.3 | Responsable de Infraestructura | Inventario de sitios con cambios sobre el supuesto SUP-27 | P2×I3 = 0,04 | — | — | — |
| R-33 | Mitigar | Nivelar los recursos de los meses 13 a 15 y reforzar el equipo antes de la marcha blanca de la Etapa 1. | 1.11.3 | Jefe de Proyecto | Carga sobre 100 % de un rol clave en los meses 13 a 15 | P2×I5 = 0,16 | 3 | 600 | Cinco personas reasignadas tres semanas entre la marcha blanca y la Etapa 2. |
| R-34 | Mitigar | Dimensionar las oleadas de cambio de etiquetas para sostener la meta de menos de 3 % y evaluar las etiquetas electrónicas del estudio de decisión. | 1.5.2, 1.2.5 | Líder de Operación | Error de precio igual o superior a 3 % en el piloto | P3×I3 = 0,08 | 3 | 360 | Se rediseña el proceso de etiquetas con 3 personas durante 3 semanas. |
| R-35 | Mitigar | Revisar los accesos de forma periódica y revocar los de ex trabajadores y temporales. | 1.5.14.1, 1.5.14.2 | Responsable de Seguridad | Una cuenta de ex trabajador activa tras la revisión mensual | P1×I5 = 0,04 | — | — | — |
| R-36 | Mitigar | Incorporar transportistas y vendedores de marketplace a los contratos de estado con calendario y medición del 97 % de trazabilidad. | 1.6.3 | Líder de Integración | Transportista sin adoptar los estados a 8 semanas del inicio de pedidos | P2×I3 = 0,04 | — | — | — |
| R-37 | Evitar | Calendarizar las siete decisiones del cliente antes de la línea base y escalar las vencidas. | 1.2.4, 1.1.4, 1.1.3 | Jefe de Proyecto | Decisiones pendientes al mes 3 (marzo de 2027) | P2×I5 = 0,16 | 3 | 360 | Tres personas de arquitectura detenidas tres semanas por una decisión pendiente. |
| R-38 | Aceptar | Seleccionar pilotos y olas fuera del clúster de Santiago al inicio y revisar la concentración cada mes. | 1.11.5, 1.11.1 | Líder de Implantación | Piloto con falla en una tienda del clúster de Santiago | P2×I3 = 0,04 | — | — | — |

Nota: las filas medias y bajas que no se listan arriba (R-03, R-04, R-05, R-07 a R-10, R-14, R-15, R-17, R-19, R-21, R-22, R-29 a R-32, R-35, R-38) conservan la numeración anterior de la EDT y deben convertirse con la equivalencia del T-14 vigente (tabla al final de este archivo) antes de usarse.

## Tabla 3. Oportunidades

Se califican con la escala de probabilidad y un impacto positivo; no se suman a las reservas (regla 4).

| ID | P (nivel) | Impacto positivo | Estrategia | Acción | Responsable |
| :-- | :-- | :-- | :-- | :-- | :-- |
| O-01 | 3 | Medio (3): se liberan horas de conciliación al retirar antes alguna interfaz por archivo. | Explotar | Priorizar en el inventario de las 14 interfaces (mes 4) las interfaces por archivo retirables. | Líder de Integración |
| O-02 | 3 | Medio (3): la prueba de corte de 24 h se adelanta y libera holgura para la migración de cartera. | Mejorar | Pedir a la filial emisora los topes del cupo preaprobado antes del mes 6. | Jefe de Proyecto |
| O-03 | 3 | Alto (4): la discrepancia del 12,4 % baja antes del corte y se liberan horas de conteo en tienda. | Explotar | Usar el conteo cíclico y la detección de discrepancias de la innovación 2 en la carga inicial. | Líder de Datos y Migración |
| O-04 | 2 | Medio (3): se detiene el borrado a los 90 días y el pasivo de 1.240 repactaciones deja de crecer. | Mejorar | Adelantar la entrada del Servicio de evidencia financiera antes del mes 16. | Arquitecto de Datos |
| O-05 | 3 | Alto (4): queda margen de observación antes del congelamiento de noviembre. | Mejorar | Migrar completa la cartera sin casos difíciles antes del mes 22. | Líder de Datos y Migración |
| O-06 | 4 | Medio (3): se dimensiona con medición y no con margen ciego, y luego se libera capacidad no usada. | Mejorar | Calibrar la memoria de capacidad con los datos del evento anual de 2026 y de ediciones previas. | Líder de Rendimiento y Calidad |
| O-07 | 2 | Medio (3): la integración y la convivencia se adelantan. | Compartir | Acordar con los proveedores actuales la entrega temprana de documentación de interfaces. | Jefe de Proyecto |
| O-08 | 2 | Medio (3): el despliegue gradual se adelanta. | Compartir | Acordar con el cliente fechas tempranas de compra de hardware y contratación de enlaces por ola. | Líder de Implantación |

## Resumen

Ajustado por el orquestador el 2026-10-12 tras la revisión del usuario: regla del hito contractual aplicada de forma estricta a R-02, R-11, R-23, R-33 y R-37; R-34 corregido a la meta de menos de 3 % (I-04); R-15 y R-31 alineados con D8 y D6.

| Zona | Riesgos | Cantidad |
| :-- | :-- | --: |
| Crítica | R-02, R-12, R-13 | 3 |
| Alta | R-01, R-11, R-16, R-18, R-20, R-23, R-24, R-25, R-33, R-34, R-37 | 11 |
| Media | R-03, R-04, R-05, R-06, R-07, R-08, R-09, R-10, R-14, R-15, R-17, R-19, R-21, R-22, R-27, R-28, R-30, R-31, R-32, R-35, R-36 | 21 |
| Baja | R-29, R-38 | 2 |
| **Total** | | **37** |

Críticos y altos (14): R-02, R-12, R-13, R-01, R-11, R-16, R-18, R-20, R-23, R-24, R-25, R-33, R-34, R-37. Reciben estimación de semanas y horas; el cuerpo del 8.2 los desarrolla junto con los 11 exigidos.

Los 11 exigidos (R-01 a R-11) por zona: crítica 1 (R-02); alta 2 (R-01, R-11); media 8 (R-03, R-04, R-05, R-06, R-07, R-08, R-09, R-10); baja 0 (—).

Notas para la revisión humana:
- R-13 conserva zona alta tras la respuesta (residual 0,32) por la holgura casi nula; se propone escalarlo al Comité Ejecutivo.
- Las semanas y horas son estimaciones del proponente con el supuesto indicado en la Tabla 2; no hay total de proyecto contra el cual contrastarlas.
- R-07 y R-13 llevan ambos OB-1 en el registro; solo R-07 describe la obsolescencia del Comunicado 10.
- Los disparadores con fecha usan SUP-26 (inicio en enero de 2027: mes 4 = abril de 2027, mes 16 = abril de 2028).

## Esfuerzo estimado de las acciones (2026-10-12)

Estimación del proponente, en horas, para el costo-beneficio de las 14 acciones de riesgos críticos y altos. Total de esfuerzo 1.660 h frente a una reducción de 2.808 h (razón 1,7).

| ID | Reducción (h) | Esfuerzo (h) | Razón |
| :-- | --: | --: | --: |
| R-02 | 120 | 80 | 1,5 |
| R-12 | 512 | 160 | 3,2 |
| R-13 | 384 | 240 | 1,6 |
| R-01 | 192 | 160 | 1,2 |
| R-11 | 72 | 40 | 1,8 |
| R-16 | 128 | 80 | 1,6 |
| R-18 | 240 | 240 | 1,0 |
| R-20 | 128 | 80 | 1,6 |
| R-23 | 96 | 120 | 0,8 |
| R-24 | 192 | 160 | 1,2 |
| R-25 | 480 | 120 | 4,0 |
| R-33 | 120 | 60 | 2,0 |
| R-34 | 72 | 80 | 0,9 |
| R-37 | 72 | 40 | 1,8 |

### Equivalencia de códigos de la EDT (antiguo a vigente del T-14)

Sin cambio: 1.1.1, 1.1.3, 1.1.4, 1.4.8, 1.7.1, 1.12.1.

| Código antiguo | Código vigente | Cuenta |
| :-- | :-- | :-- |
| 1.1.6 | 1.1.5 | calendario de congelamientos |
| 1.1.7 | 1.1.6 | actas de comités |
| 1.1.10 | 1.1.8 | actas de aceptación |
| 1.2.6 | 1.2.4 | línea base de alcance |
| 1.2.7 | 1.2.5 | estudio de etiquetas electrónicas |
| 1.3.8 | 1.3.7 | obras del cliente |
| 1.5.1.2 | 1.5.2 | etiquetas y discrepancias de precio |
| 1.5.3.4 | 1.5.10 | conteo e inventario |
| 1.5.11.5 | 1.5.40 | conciliación diaria con la plataforma de 2011 |
| 1.6.12 | 1.6.7 | contingencia tributaria |
| 1.7.3 | 1.7.2 | maestro de artículos |
| 1.7.4 | 1.7.3 | corte de inventario |
| 1.7.7 | 1.7.6 | cartera viva |
| 1.7.10 | 1.7.8 | plan de retiro de 2011 |
| 1.7.11 | 1.7.9 | 2011 fuera de servicio |
| 1.7.14 | 1.7.12 | actas de compuerta |
| 1.9.6 | 1.9.5 | ensayo del evento anual |
| 1.11.3 | 1.11.2 | configuración y certificación de sitios |
| 1.12.9 | 1.12.7 | soporte de estabilización |
