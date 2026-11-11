# 10 · Riesgos y oportunidades del diseño de la física (para el sd-08)

**Uso:** insumo para el plan de riesgos (sd-08 y Formulario T-16). No reemplaza el T-16: propone riesgos nuevos y cambios a riesgos que ya existen, con el mismo formato y las mismas escalas. Los formularios recibidos no se editan aquí.

**Reglas aplicadas (decididas por el usuario 02-11):** cada riesgo se clasifica como **amenaza** u **oportunidad** (PMBOK 6) y recibe **una sola** estrategia activa (decidido 02-11). **No se usa «aceptar»**: ni pasiva ni activa. El escalamiento por zona es la regla del apartado 8.1 (zona alta al Comité de Proyecto, crítica al Ejecutivo), no una estrategia: por eso no figura entre las acciones. La contingencia se registra aparte, con su disparador (clase FEP04, diapositivas 58 y 64). Estrategias de amenaza: evitar, transferir, mitigar, escalar. De oportunidad: explotar, mejorar, compartir, escalar.

**Escalas (SD-08, apartado 8.1):** probabilidad 0,05 · 0,20 · 0,40 · 0,60 · 0,85; impacto 0,05 · 0,10 · 0,20 · 0,40 · 0,80, tomando el peor entre plazo, esfuerzo, costo, alcance y servicio. Un hito sin holgura (meses 16, 21, 22 y 56) da impacto 0,80. Zonas: crítica ≥ 0,40 · alta 0,20 a < 0,40 · media 0,08 a < 0,20 · baja < 0,08. **Origen de las cifras:** las calificaciones de abajo son criterio mío justificado con el Caso o con el diseño; no hay datos medidos. La exposición residual es una estimación del efecto de la respuesta. El usuario las valida.

## A. Amenazas nuevas (numeración propuesta R-39 a R-42; R-FIS-04 no es nuevo: amplía R-30, ver B)

### R-FIS-01 · propuesta R-39 · Informe interno de 2024 del centro de datos de casa matriz
- **Tipo y rama:** amenaza · Técnica · mirada Solución.
- **Enunciado:** como el recinto de DC-01 (140 m², de 2011) cumple parcialmente el capítulo 6 de las Bases y el informe que documenta la brecha aún no se entrega, el diseño supone una sala habilitada según el `.tex` (S-07). Puede ocurrir que el informe revele brechas mayores (energía, climatización, incendio, acceso, espacio) y obligue a rehacer decisiones. El efecto sería obra civil mayor, cambio de racks y de ubicación de los dos pares de integración (S-16), y atraso de la plataforma base.
- **Calificación:** probabilidad 0,40 (la brecha existe por el Caso; no se sabe su tamaño) · impacto 0,80 (puede atrasar el mes 16) · exposición **0,32 · zona alta**.
- **Estrategia:** **mitigar**.
- **Acciones de la estrategia (mitigar):** (1) pedir el informe como entrada con fecha límite al mes 4, igual que el disparador de R-31, para reducir la incertidumbre; (2) mantener modular la sala (reserva inicial de 80 de 168U) para que un cambio de racks no obligue a rediseñar.
- **Plan de contingencia:** tener definido un sitio alternativo para los pares de integración y activarlo si el informe lo exige.
- **Disparador del plan de contingencia:** informe sin entregar al mes 4, o con una brecha que exige obra no prevista.
- **Dueño propuesto:** Arquitecto de Solución. **Cuenta del T-14:** 1.4.9 a 1.4.12 (las de R-31).
- **Exposición residual estimada:** 0,08 (probabilidad 0,20 · impacto 0,40).
- **Relación con T-16:** R-31 trata la obra no lista y exige el informe como disparador, pero su enunciado no recoge que el informe cambie decisiones; este riesgo lo agrega.

### R-FIS-02 · propuesta R-40 · Concepción con enlace único
- **Tipo y rama:** amenaza · Operación · mirada Solución.
- **Enunciado:** como el Caso declara que CD-02 tiene un solo enlace y el segundo enlace fijo es solo una propuesta, puede fallar ese enlace o objetarse que el router 4G/5G no cumple la redundancia de RT-03.17 (caminos y proveedores distintos). El efecto sería un centro sin conexión estable a la nube, con captura local pero sin conciliación, y un incumplimiento en la matriz T-12.
- **Calificación:** probabilidad 0,40 (sin tasa de falla conocida) · impacto 0,20 (la demanda del centro es 0,1 Mbps y el camino móvil sostiene 5) · exposición **0,08 · zona media**.
- **Estrategia:** **mitigar**.
- **Acciones de la estrategia (mitigar):** (1) router 4G/5G con dos operadores (doble SIM) para que el segundo camino también sea redundante; (2) ensayo de corte provocado en CD-02, que ya figura en la Tabla 4.18.
- **Plan de contingencia:** si el enlace cae, CD-02 opera con captura local y el camino móvil, y se concilia al volver el enlace.
- **Disparador del plan de contingencia:** enlace caído más de una hora en el ensayo o en producción.
- **Dueño propuesto:** Líder de Implantación. **Cuenta del T-14:** por asignar.
- **Exposición residual estimada:** 0,02 (probabilidad 0,20 · impacto 0,10).
- **Relación con T-16:** R-20 (lo que provee el Cliente) y la oportunidad O-08 (el Cliente contrata los enlaces antes de cada ola).

### R-FIS-03 · propuesta R-41 · Transferencia de registros de seguridad a Sentinel
- **Tipo y rama:** amenaza · Seguridad · mirada Solución.
- **Enunciado:** como Microsoft Sentinel no existe en Chile Central (verificado) y procesa los datos en Estados Unidos, el diseño envía las tablas de seguridad a Brazil South (S-19). Puede ocurrir que el Cliente, su asesoría jurídica o la CMF no aprueben esa transferencia permanente (Ley 21.719). El efecto sería rediseñar el SIEM en Chile, con más operación y sin integración nativa con Defender y Entra.
- **Calificación:** probabilidad 0,40 (la decisión es del Cliente) · impacto 0,40 (rediseño sin tocar hitos) · exposición **0,16 · zona media**.
- **Estrategia:** **mitigar**.
- **Acciones de la estrategia (mitigar):** (1) pedir la decisión de residencia antes de la línea base (mes 3), igual que R-17, para reducir la probabilidad; (2) minimizar el envío a solo tablas de seguridad y seudonimización donde el producto lo permita, para reducir el impacto.
- **Plan de contingencia:** dejar diseñado y presupuestado el SIEM en Chile sobre el clúster de operación y activarlo.
- **Disparador del plan de contingencia:** sin decisión al cierre del mes 3, o rechazo de la transferencia.
- **Dueño propuesto:** Encargado de Seguridad de la Información. **Cuenta del T-14:** 1.8.7 (la de R-17).
- **Exposición residual estimada:** 0,04 (probabilidad 0,20 · impacto 0,20).
- **Relación con T-16:** R-17 (residencia del emisor en Brazil South) y R-19 (Ley 21.719).

### R-FIS-05 · propuesta R-42 · Accesos reales de la tienda de laboratorio
- **Tipo y rama:** amenaza · Proyecto · mirada Implantación.
- **Enunciado:** como el ensayo de Preproducción necesita dos accesos fijos reales de operadores distintos en la tienda de laboratorio (S-02), puede ocurrir que no estén contratados a tiempo. El efecto sería no demostrar el cambio entre operadores antes de las olas y atrasar la aceptación de la conmutación.
- **Calificación:** probabilidad 0,40 · impacto 0,20 · exposición **0,08 · zona media**.
- **Estrategia:** **transferir** (responsabilidad del Cliente con fecha).
- **Acciones de la estrategia (transferir):** (1) fijar por escrito qué contrata el Cliente y para cuándo, como en R-20; (2) pedir los accesos 12 semanas antes del ensayo.
- **Plan de contingencia:** si falta uno, ensayar con un acceso fijo real y el camino móvil real, y declarar la parte no demostrada.
- **Disparador del plan de contingencia:** certificación del sitio no emitida a 8 semanas del ensayo.
- **Dueño propuesto:** Líder de Implantación. **Cuenta del T-14:** por asignar.
- **Exposición residual estimada:** 0,04 (probabilidad 0,20 · impacto 0,20).
- **Relación con T-16:** R-20, con la que podría fusionarse.

## B. Riesgo existente que debe ampliarse

### R-30 · servicios no disponibles en Chile Central
- **Hoy en el T-16:** probabilidad 0,20 · impacto 0,40 · exposición 0,08 · estrategia evitar (probar cada servicio al inicio).
- **Hallazgo nuevo (02-11):** Learn marca Chile Central como «Power BI only region»; la capacidad Fabric no está comprobada (S-23). Managed DevOps Pools no se confirma en Chile Central (S-28) y las zonas de Bastion están en vista previa (S-27).
- **Cambio propuesto:** subir la probabilidad a 0,40 (exposición 0,16, zona media) y ampliar la lista de servicios que se prueban al inicio con la capacidad de Power BI, Managed DevOps Pools y las zonas de Bastion. Se mantiene **evitar**. **Plan de contingencia:** modelos de Power BI en la región de origen de la cuenta del Cliente con su aprobación, agentes de CI/CD en VMSS y Bastion sin zonas con el riesgo declarado. **Disparador:** un servicio no se puede crear en la prueba al inicio.

## C. Riesgo existente que debe corregirse

- **R-32:** su acción dice «acreditar el ExpressRoute antes del diseño final». ExpressRoute salió del sd-04 (S-09); la acción debe quedar solo en confirmar ubicaciones y rutas con el inventario.

## D. Oportunidades (PMBOK: estrategias de oportunidad)

| ID | Oportunidad | Probabilidad | Estrategia | Acción | Dueño propuesto |
| :--- | :--- | :--- | :--- | :--- | :--- |
| O-FIS-01 | Microsoft habilita la alta disponibilidad entre zonas de PostgreSQL en Brazil South para servidores nuevos (hoy bloqueada «temporalmente») | 0,40 | Compartir | Consultar la fecha con el equipo de la alianza con Microsoft (SD-01) y dejar el parámetro de zona en la definición de infraestructura para cambiarlo en una modificación | Arquitecto de Solución |
| O-FIS-02 | Microsoft Sentinel llega a Chile Central y desaparece la transferencia de R-41 | 0,20 | Compartir | Consultar la hoja de ruta con la alianza y dejar la configuración de Sentinel parametrizada por región | Encargado de Seguridad de la Información |
| O-FIS-03 | La capacidad de Power BI se puede contratar en Chile Central y los modelos quedan en Chile | 0,40 | Explotar | La prueba al inicio de R-30 la confirma; si resulta, se aplica de inmediato y se retira la alternativa | Arquitecto de Solución |
| O-FIS-04 | Managed DevOps Pools disponible en Chile Central: menos operación de agentes | 0,40 | Explotar | Registrar el proveedor `Microsoft.DevOpsInfrastructure` y, si aparece, cambiar los agentes de VMSS | Líder de Operación / SRE |

**Relación con T-16:** la oportunidad O-08 (el Cliente contrata los enlaces antes de cada ola) es la contraparte de R-40 y R-42. Las oportunidades no suman a las reservas (regla 4 del apartado 8.1).

## E. Observación para el sd-08

El T-16 usa **aceptar** en R-19, R-29 y R-38, y el apartado 8.1 prevé aceptación activa para la zona media y pasiva para la baja. Si el criterio es no aceptar ningún riesgo, esas tres respuestas y la regla de zonas deben revisarse en el sd-08. Aquí no se tocan.

## F. Traspaso a la sesión de riesgos (decidido 02-11)

**Regla de esta sesión:** se trabaja la arquitectura lógica y física. Los riesgos que salgan se anotan aquí, sin especificarlos; la corrección y el detalle van en una sesión aparte.

**Quedó anotado, sin resolver:**
1. R-39 a R-42 y R-30 y R-32 (secciones A a C): calificaciones por validar; R-41 mitigar o evitar para la Filial; fusionar R-42 con R-20.
2. **Error de estrategia en el T-16 (`.tex` recibido):** R-31 dice «Mitigar y transferir dependencia» (dos estrategias). Propuesta: dejar solo «transferir» y pasar lo del proponente a la acción o a la contingencia.
3. Segunda estrategia dentro de la acción en R-11, R-13 y R-37 («escalar»), y contingencias mezcladas en R-14 y R-17.
4. R-19, R-29 y R-38 usan «aceptar»; el apartado 8.1 también lo prevé para zonas media y baja.
5. Campos de la diapositiva 58 de FEP04 que faltan en mis fichas: efecto esperado y etapa en que actúa.
6. Conciliar T-11, T-12 y T-16 con la salida de ExpressRoute (ver `06_supuestos-pendientes.md`).
7. Confirmar que el T-16 leído es la versión vigente.

**Fuentes:** T-16 y SD-08 en `02_Propuesta/latex_final/` (`.tex`); clase FEP04 diapositivas 58, 61 y 64; resúmenes web de PMBOK 6 (no se leyó el texto oficial).
