# Bitácora de la sesión de redacción del SD-04 (noviembre de 2026)

Fuera del `.tex`, por regla. Estado «revisado» solo lo asigna una persona.

## 2026-11-06 · Fase 1

- Creado `informe-cotejo.md`. Sin cambios en `.tex` ni formularios.
- Decisiones del usuario: aprobó las sugerencias del informe; pidió contrastarlas con las Bases. Resultado en la sección 10 del informe: dos correcciones (zona única en Brasil queda abierta; C-029 pasa a contradicción) y cuatro hallazgos nuevos (C-087 a C-090).
- Autorizado por el usuario («me parecen bien tus sugerencias», punto 10): corrección del catálogo K-01 a K-10. Aplicada en `registro-diseno-fisica/`:
  - K-01 (Service Bus sin geo-replicación): `01` fila de Brazil South; `02` E-55 reescrita; `03` fila Service Bus; `00` §9.1 fila bus_r/bus_e; `06` hallazgo de Learn.
  - K-02 (Front Door, dos perfiles): `01` bloque 2.
  - K-03 (Bastion con Entra Private Access): `01` bloque 2.
  - K-04 (recorrido privado): `00` §9.5, H-17 reabierto y corregido.
  - K-05 (carga de Service Bus): `05` pendiente 0 nuevo. Sin cifras nuevas.
  - K-06 (enlace de Concepción): `01` bloque 5.
  - K-07 (doce réplicas): `02` E-54; `01` bloques 3 y 4.
  - K-08 (supuestos ya resueltos): `01` (DNS Private Resolver, CI/CD, plataforma publicitaria); `02` E-03b.
  - K-09 (encabezado y cierre de `01`): actualizados a S-01 a S-32.
  - K-10 (`06` fila S-27): corregida.
- Copias previas a la edición en `$CLAUDE_JOB_DIR/tmp/*.bak` (se borran con el trabajo). `git diff` muestra todo.
- Pendiente de registrar antes de redactar: tipología por sitio (C-087), RAID (C-088), FinOps y reversibilidad (C-089), CIS y parches (C-090). Son exigencias de las Bases sin supuesto asociado.

## 2026-11-06 · Decisiones del usuario sobre el contraste

- **Registro de C-087 a C-090:** `06` S-33 (tipología por sitio), S-34 (RAID 1), S-35 (CIS, parches, administración remota) y S-36 (FinOps y reversibilidad). Son exigencias de las Bases, no decisiones del Cliente.
- **K-05 recalculado:** `05` fila de Service Bus y pendiente 0; `01` fila del bus de Retail. Pico de diseño 6.667 entregas/s (400.000 × 5 ÷ 300); 7.802/s si coincide con la sincronización de existencia (hipótesis de solape, sin fuente). El número de unidades de mensajería no se fija: falta el dato de capacidad por unidad en Microsoft Learn.
- **Zona única en Brasil:** el usuario preguntó dónde ocurre. Respuesta en la conversación: solo en la alta disponibilidad de PostgreSQL tras promover la réplica (`.tex` L1117, S-25) y en Bastion sin zonas (S-27, no dicho en el `.tex`). Sigue abierta la forma de defenderlo ante el Art. 16.3.
- **Ajustes a otros documentos:** `ajustes-otros-documentos.md`.

## 2026-11-06 · Ciclo 4.3.1 (ajustar)

**Estado:** redactado, `verificar` T7-04 ok, `verificar-redaccion --parte T7-04` 0 errores y 0 avisos. Sin revisión humana. No es «revisado».

**Cambios en el `.tex`** (`git diff` del archivo; 16 inserciones y 8 eliminaciones tras la segunda ronda):
- Primera ronda: C-053 (HSM), C-021 (accesos de DC-01 como requisito), C-068 (tipología), C-070 (Concepción).
- Segunda ronda, tras los tres agentes: definición de frente y X-01 al abrir; reparto por zonas y regla de dos tercios; vista general con la Figura 4.12; AKS, nodo, plano de control y grupo elástico explicados; recuento de 54 máquinas virtuales sin ambigüedad y sin el grupo elástico; Sentinel con remisión a 4.3.2.1; HSM con Chile Central y Brazil South nombradas; «comprar» por «contratar la capacidad»; CLD-02 definido; 80 de 168U aclarado (80 presupuestadas, 88 libres); separación verificada con 4.1.16; par de integración de la Filial transitorio y el de Retail condicional (S-16); sujeto explícito en el recinto técnico; RT-06.20 (facial con AFIS) y RT-06.24 (respaldo de grabaciones) completos; tipología justificada con los sistemas conservados y los dos pares de integración; cita a SD-03 3.2.3 en lugar de SP-04; CD-01 y CD-02 separados, con la fuente de la captura.
- Párrafos de las antiguas líneas 1033, 1045 y 1047 partidos en seis.

**Agentes:** lector no técnico (fases 1 y 2), revisor de hilo lógico y evaluador PMBOK. Humanizer (RR-24) aplicado sin cambios adicionales.

**Registro:** `01_nodos.md` fila de DC-01, 80 de 168U (fuente `cierre-inventario/10-espacio-racks.md`).

**No aplicado en 4.3.1, con destino:**
- Tiempo de conmutación entre enlaces (RT-03.17): 4.2.6, C-051.
- Potencia y capacidad de lo que provee el proponente en el recinto (UPS, clima, generador): 4.2.1; depende del inventario del Cliente.
- Frase de `Tabla 4.22` (DC-01) y de 4.2.1 L655 sobre canalizaciones y cableado, y «sin duplicar el WMS» en L677 y Tabla 4.20 L936 (falso para CD-02): 4.2.1 y 4.2.7. Hilo lógico H1, H2, H4.
- Quién compra el par local de captura de los centros: Tabla 4.22 dice Cliente; tienda dice proponente. Decisión abierta.
- RT-06.01 (uso exclusivo de la solución y acceso independiente) frente a los sistemas conservados alojados en el recinto. Decisión abierta.
- Sentinel en la fila CLD-02 de la Tabla 4.23 (4.3 intro): hilo lógico H8.
- Tipología de tienda, centros y DC-02: 4.2.2, C-087, depende de S-33.
- Término «máquinas auxiliares» frente a «máquinas de apoyo» del glosario: pasada global de nombres, C-086.
- Referencias por línea no verificadas en el PDF visible: Caso 09 cap. 5 p. 13 y cap. 6 p. 14 (confirmadas en el OCR).

## 2026-11-06 · Ciclo 4.3.2 (ajustar, con 4.3.2.1 y 4.3.2.2)

**Estado:** redactado, `verificar` T7-04 ok, `verificar-redaccion --parte T7-04` 0 errores y 0 avisos. Sin revisión humana. No es «revisado».

**Primera ronda (antes de los agentes):** C-074 (reconexión de sitios al VPN Gateway de Brasil y fila nueva en Tabla 4.24), C-075 (grupo elástico), C-076 (puntos privados de Front Door), C-079 (norma de externalización y resolución de cláusulas modelo con entradas nuevas en Referencias), C-080 (sin «matriz de riesgos»), C-081 (alternativa de Sentinel), C-083 (alta disponibilidad en una zona, redactada como limitación temporal frente al Art. 16.3, opción A+B de `informe-cotejo.md` 10.1), C-084 (declaración con dos sondas, aislamiento de Chile, tráfico gradual, bloqueo de nuevo cupo).

**Segunda ronda (tras lector no técnico fases 1 y 2, revisor de hilo lógico y evaluador PMBOK):**
- RTO y RPO definidos al primer uso; X-01 como Servicio de control de cruces; las 4 máquinas de Power BI son puentes hacia el servicio, que sigue en Chile.
- Se declara qué pasa si el retraso de réplica supera 15 minutos (pérdida potencial, conciliación con diarios y registros durables).
- Remisión al respaldo 3-2-1-1-0 en 4.2.6; activación de la alta disponibilidad automatizada (S-25).
- Dependencias globales del proveedor como parte del análisis de amenazas comunes de RT-07.02.
- La reconexión de sitios se ubica en la etapa de red y DNS (inferencia mía; el catálogo no la asigna a una etapa).
- El personal del Cliente puede ejecutar la conmutación y el retorno tras la transferencia (RT-07.05); los ensayos son con conmutación real (RT-07.07).
- Alternativa en Chile consolidada en un solo párrafo (antes tres); frase repetida sobre la ausencia de ruta Retail–filial eliminada.
- Brazil South emparejada con South Central US (fuente: `04_continuidad.md`).
- La zona única se redactó como «solo entra en servicio al promover» y se reconoce el evento doble no cubierto.
- Rechazo del almacenamiento geo-redundante reformulado como «sin la aprobación del Cliente».
- Tránsito de la entrada pública por puntos privados de Front Door en Brazil South y East US, declarado en 4.3.2.1.
- Cupo preemitido (término de 4.1.12) y condición de compra con tarjeta propia no disponible.
- Tabla 4.24, fila de Blobs: se mide el retraso de la copia frente al RPO.
- Data Lake de analítica fuera del RPO, copia programada (S-21).
- Justificación de activo-pasivo sin argumento de costo.
- Norma CMF con capítulo y circular, y glosa de «grado de inversión».

**Fuentes de internet consultadas hoy** (sin PDF primario): comunicado de la CMF del 26-12-2019 (cmfchile.cl, article 28049) y listado de la BCN de la resolución RAEX202503748, de diciembre de 2025. El emisor exacto de la resolución no se confirmó.

**No aplicado, con razón (decisión tuya):**
- H2 hilo lógico: el texto no dice cómo se fija un punto de recuperación coherente entre 12 servidores ni si el registro del consumidor se confirma con el efecto en la misma transacción. Es una decisión de diseño no registrada.
- H3: la republicación no está en las siete etapas y no se declara desde cuándo corre el RTO (falla o declaración).
- H4: «registro» frente a «ventana de deduplicación» y valor del «intervalo necesario».
- H6: estado inicial del origen de Brasil en Front Door (habilitado de menor prioridad o deshabilitado hasta la etapa seis).
- H10: de dónde sale el material de claves para la reinyección en Brasil y cuánto tarda.
- PMBOK P1-1: umbral y responsable que declara la contingencia; P1-5: qué servicios son críticos; P1-4: presupuesto de tiempo por etapa y fuente de los 2.600 km (cálculo en `calculos/latencia-santiago-sao-paulo.py`, sin cita pública); P1-6: diseño mínimo de la alternativa nacional.
- Para otras subsecciones: 4.2.5 L841 («el ambiente de Recuperación es igual al de producción», choca con la zona única); 4.2.6 L884 (escenario de 8 h frente a los 24 h del SD-03); Tabla 4.19 Service Bus por zona; Sentinel en la fila CLD-02 de la Tabla 4.23.

## 2026-11-08 · Ciclo 4.2.1 (reescribir)

**Estado:** redactado, `verificar` T7-04 ok, `verificar-redaccion --parte T7-04` 0 errores y 0 avisos. Sin revisión humana. No es «revisado». Agentes: lector no técnico (fases 1 y 2), revisor de hilo lógico y evaluador PMBOK, con informes breves.

**Cambios en el `.tex`:**
- H-16 y H-16b resueltos: DC-01 queda como puntero a 4.3.1; los enlaces de los centros ya no se repiten; las Figuras 4.25 y 4.26 solo se citan en 4.3.1.
- «Sin duplicar el WMS» solo para CD-01; CD-02 sin WMS. Par local de captura explicado, con 100 GB útiles de reserva preliminar (`01_nodos.md` bloque 5) y WMS definido.
- Tabla 4.22, DC-01: el proponente provee conectividad, seguridad y los sistemas de energía, climatización, incendio y acceso del recinto; el Cliente, obra civil, obras eléctricas y cableado.
- RAID 1 declarado y justificado (S-34) con 960 GB útiles de 1.920 brutos; copia local cifrada por negocio; CIS, Intune y parches (S-35); firmware, bloqueo y borrado remoto de dispositivos de terreno (RT-03.18).
- UPS en kVA; UPS con 30 minutos como margen de diseño y baterías para transferencia y cortes breves; 5 Mbps frente a 4,8 Mbps con la aclaración del margen de 1,5; grupo electrógeno inicial en la fila de energía.
- Quitados VLAN numeradas, LSZH, OS2 y la cita a un adjunto inexistente. Dos puntos explicativos eliminados (RR-25).
- Remisión al software nuevo en 4.1.1 y 4.2.3. Pares de integración de DC-01: el de la filial transitorio y el de Retail condicionado (S-16).

**No aplicado, para tu decisión:**
- Quién compra los servidores del par local de captura de los centros: la Tabla 4.22 dice Cliente y la tienda dice proponente. Sugerencia: proponente, con el mismo criterio que en tienda.
- «Canalizaciones» las provee el proponente (RT-06.33) pero el cableado lo ejecuta el Cliente. La frontera exacta falta; el SD-03 L311 tiene la misma ambigüedad.
- Por qué RT-06.33 se aplica solo a DC-01 y no a tiendas y centros (hilo lógico, punto 3): el Caso cap. 11 asigna al Cliente la red y las obras de tiendas y centros. Requiere una frase de justificación acordada.
- RAID, CIS y parches en los centros y en DC-01: solo se declaran para la tienda.
- Software y sistema operativo de los servidores de tienda y de DC-01, e hipervisor: el título dice «Software» y no hay lista. Depende del T-11.4.
- Totales de núcleos, memoria y disco, y disco de reserva (FEP01·117).
- Tabla 4.22 con celdas de varias cláusulas (RR-16).
- Carga de 2,57 kW y 3,341 kW y grupo de 20 kVA: sin registro en `01` a `06`. Registrar en `05_capacidad.md` desde `cierre-inventario/11-soporte-fisico.md`.
- Copia local cifrada y las 31 de 72U: no se sabe si está contada.
- Numeración: la Tabla 4.22 aparece antes que la 4.20 y la 4.21. Compilar y revisar el orden.
- Folios del Caso (cap. 6, p. 14) no verificados en el PDF visible: el grep del agente no los halló en el espejo `.md`.

## 2026-11-08 · Decisiones del usuario tras 4.2.1

- **Par local de captura de los centros: lo provee el proponente.** Aplicado en la Tabla 4.22 (fila Centros de distribución) y en 4.2.1. Pendiente en otros documentos: T-11.4 solo cubre la tienda; falta una fila del par de captura de CD-01 y CD-02 (no se editó, requiere autorización por formulario). Anotado en `ajustes-otros-documentos.md`.
- **T-11.4 revisado** (formulario recibido, L304 a L345): coincide con el SD-04 en servidores (88) y árbitros («testigos» en el formulario), RAM, discos y repuestos. Los tres racks, las dos UPS y las seis PDU son del proponente; los 24 routers móviles los adquiere el Cliente, como en la Tabla 4.22. No lista software ni sistema operativo del servidor: la Tabla T-11.5 solo dice «servidor compacto de borde». Sin hipervisor ni sistema operativo en ningún documento: pendiente.
- **Tiendas y centros frente a RT-06.33:** abierto. El usuario pidió evaluar implicaciones y alternativas; ver la respuesta de la conversación (tres alternativas, recomendación A).

## 2026-11-08 · Decisiones del usuario (segunda tanda)

- **RT-06.33 en tiendas y centros: alternativa A.** Registrada como S-37 en `06_supuestos-pendientes.md` y redactada en 4.2.1 (sección pasada, antes de 4.2.2), con cita al Caso cap. 11, p. 26 (tomada de T-11.5; folio por verificar en el PDF visible).
- **Software de los servidores:** investigación previa en `cierre-inventario/03-tienda.md` L80 propone contenedores separados por negocio, sin máquina virtual por función, con sistema operativo y runtime fijados en la implementación. Registrado en S-37 y redactado en 4.2.1. Hipervisor y sistema operativo siguen sin fijar; `10-espacio-racks.md` L43 habla de «hosts de integración/virtualización» en DC-01 sin decidir.
- Folio corregido: la sentencia del Caso sobre el hardware está en p. 27, no p. 26 (OCR paginado, línea 1177). Corregido en el SD-04; T-11.5 anotado en `ajustes-otros-documentos.md`.

## 2026-11-08 · Sesión A: bloque 4.2 (intro, 4.2.2 a 4.2.8)

**Estado:** redactado sin agentes por subsección. `verificar` T7-04 ok y `verificar-redaccion` 0 errores y 0 avisos antes de la pasada de agentes del bloque. Sin revisión humana. Decisión del usuario: ordenar los pendientes por impacto en la nota, con una pasada de agentes por bloque. Pendientes en `pendientes-decisiones.md`.

**Cambios:**
- **Hipervisor:** en tienda no hay (contenedores en el sistema del servidor); en DC-01 los servidores de integración usan virtualización, con producto y licencia en el levantamiento.
- **4.2 intro:** DC-01 con accesos propuestos; fila de Brasil de la Tabla 4.13 con VPN Gateway, firewalls y redes.
- **4.2.2:** tipología por sitio (S-33), variantes de tienda (P-01) y **Tabla 4.14 reescrita con los seis factores del Art. 16.2** en 11 filas (el costo, en palabras).
- **4.2.3:** DDoS Protection, External ID, Private Access, Intune, Redis B20 de 24 GB, Ddsv5, Bastion en vista previa, FinOps y reversibilidad.
- **4.2.4:** puertos y protocolos solo en entrada pública, túneles y cruce; Private Link Service con proxy como alternativa (S-11).
- **4.2.5:** quitada la marcha blanca; tamaños de ambientes (S-05); agentes en conjunto de escalado y clave del grupo (S-28); recuperación igual salvo zona única.
- **4.2.6:** centros con 24 horas (Art. 16.4); puntos únicos declarados; tiempo de conmutación medido; filas 12 y 13 en la Tabla 4.18; HSM y copia de Data Lake aclarados.
- **4.2.7:** trazo con 3.3.2 y 4.1.5; DNS, API Center, Data Factory, Power BI, DDoS en las filas; fila de plataformas conservadas y elementos por definir; WMS solo en CD-01; pares de DC-01.
- **4.2.8:** latencias objetivo (P-02), cálculo de nodos, pico de Service Bus (6.667 y 7.802 por segundo) y retención de registros (S-17, S-18).

**Pasada de agentes del bloque 4.2 (lector fases 1 y 2, hilo lógico, evaluador PMBOK):** aplicados los ajustes que se sostienen. Resumen:
- Puntos únicos de falla: DC-01 «no guarda datos de las funciones nuevas» (antes «no aloja funciones nuevas»); las cuentas de emergencia cubren el bloqueo de administradores y no la caída del servicio.
- Front Door: tres caminos con nombres distintos (punto privado por Brazil South, punto privado por East US, origen de recuperación en Brasil). Perfil y puerta por negocio en la Tabla 4.14.
- «Túnel por negocio» unificado (no por frente), ya que X-01 no recibe túneles.
- Tabla 4.21: los 30 minutos de resincronización se declaran como plazo propio aplicado a 24 horas, no a las 8 horas del Caso; la resincronización exige menos capacidad que la bajada de precios.
- 12 auxiliares sin ninguna en X-01; 50 máquinas de espera desglosadas; Service Bus no atribuido a X-01; punto de paso de Front Door aclarado.
- `pendientes-decisiones.md`: se agregan P-21 (anexo de direcciones IP), P-22 (numeración de RT-03.13 entre Caso y Bases) y P-23 (proveedores distintos en DC-01 y CD-02).
- No aplicado: numeración de tablas fuera de orden (se revisa al compilar); filas faltantes en la Tabla 4.14 (entrega y ambientes, respaldos, herramientas con estado, tienda de laboratorio); Tabla 4.13 duplicada con 4.21 en anchos de banda; repeticiones de las 24 horas.

## 2026-11-09 · Decisiones de `pendientes-decisiones.md`

- El usuario eligió opciones para P-01 a P-23. Aplicadas en el `.tex`: P-03, P-04, P-05, P-07, P-08, P-09, P-10 (parcial), P-12, P-13, P-14, P-15, P-16 y P-20. Supuestos S-38 a S-45 en el registro.
- Bloqueadas: P-01 (sin región verificada), P-06 y P-21 (falta archivo de Anexos del SD-04), P-17 (no verificable). Detalle en el md de pendientes.
- Nueva Tabla 4.25; el uso de IA pasa a Tabla 4.26. `verificar` T7-04 ok; `verificar-redaccion` 0 errores, 0 avisos.
- Sin cambios (opción vigente): P-11, P-18, P-19, P-22, P-23. P-02 y 4.1.8 (P-10) quedan para la sesión B.
- P-01: el usuario aportó la tabla y la nota al pie de Microsoft (09-11). Brazil South con «$» bloqueado, Brazil Southeast sin alta disponibilidad entre zonas, Chile Central es la primaria. P-01 queda en el texto vigente. P-17 aplicada por indicación del usuario.

## 2026-11-09 · Sesión B (4.1)

- 4.1.1: API Management (buscador de productos), Redis B20, Managed HSM (capacidad en Brasil), Front Door con perfil propio de Retail y de la filial (sin entrada pública de X-01), Azure Pipelines, motor local PostgreSQL con Valkey descartado por RT-03.11 y RT-03.12.
- 4.1.2: 25 actores (14 personas y 11 sistemas), S-47. 4.1.3: un solo tenant de Entra ID (S-13).
- 4.1.8: P-10. 4.1.10: rótulo de la Figura 4.21 movido a 4.3.1. 4.1.12: fila virtual y Tabla 4.28 (S-46). 4.1.14: nodos de X-01 quitados. 4.1.15: explicación de la Figura 4.11. 4.1.16: condición de Power BI en ADR-09.
- No aplicado: C-011 (Cleveron y Criteo; opcional, se remite a T-11), C-014 (calendario del piloto, se conserva breve), C-010 (recorrido privado directo a API Management; se mantiene el `.tex`, falta corregir H-17 en el catálogo), C-086 (nombres frente al glosario: va al cierre).
- Tabla 4.25 de respaldos en 4.3.2.1 (P-06) y cita Microsoft 2026t sobre el bloqueo de PostgreSQL en Brasil. Título de la referencia por confirmar en la página.

## 2026-11-09 · Ciclo de agentes sobre 4.1 y 4.3.2

- Lector (fase 1), PMBOK e hilo lógico. Aplicado: Tablas 4.25, 4.26 y 4.28 corregidas; ocho puntos únicos con criterio y número de la Tabla 4.18; conteo de actores explícito; origen de recuperación de Brasil deshabilitado (4.3.2 y 4.3.2.2) y «punto privado de tránsito» en la Tabla 4.18; ventana de deduplicación (S-43b); External ID por negocio; motor local PostgreSQL distinguido del de la nube.
- No aplicado, a decisión del usuario: filas «Ninguna otra evaluada todavía» (Tabla 4.12), fila «Plataformas conservadas» de la Tabla 4.20, cifras sin fuente (2.600 km, 40 a 55 ms, 2,57 y 3,341 kW), umbral de 30 minutos frente a «no crea otro plazo de drenaje», vigencia máxima de la lista de precios sin enlace, glosario en primera mención.
- Cierre: numeración de tablas, nombres frente al glosario (C-086), corregir H-17 (K-04).
- Parte 1 (ventana de deduplicación): el usuario elige la opción 1 (09-11). S-43b queda aprobada: no menor que 15 min + 4 h, ampliada por el retraso medido, y claves de venta de tienda a 24 h.
- Parte 2 (tensión en 4.2.6): el usuario indica no aplicar, porque no hay contradicción. Parte 3 (glosario): opción 1, definidos namespace, broker, idempotencia y cupo preemitido en su primera mención.
- Parte 2 (tensión en 4.2.6): el usuario indica no aplicar, porque no hay contradicción. Parte 3 (glosario): opción 1, definidos namespace, broker, idempotencia y cupo preemitido en su primera mención.
- Parte 4 (Tabla 4.26): opción 1, sin cambios. Parte 5 (Tabla 4.12): opción 1, línea 91 precisa «de la Tabla 4.11». Eran 7 filas, no 10.
- Parte 6 (Tabla 4.20, plataformas conservadas): opción 1, nodo del catálogo para vista logística y capacidades comunes; F:C-04 candidato sin despliegue.
- Parte 7 (cifras sin fuente): opción 1, aclaradas 31 de 72U (8+8+15) y 43 minutos (0,1 % de 30 días). Fin de las siete partes; empieza el cierre.
- Cierre, parte 1: tablas del SD-04 renumeradas por orden de aparición (28 tablas, 90 referencias internas actualizadas). Documentos externos sin editar; correspondencia en `ajustes-otros-documentos.md`. Los números de tabla citados en esta bitácora y en `pendientes-decisiones.md` son los anteriores.
- Cierre parte 2 (nombres): opción 1; Data Lake en lugar de lago de datos, quitados pg-x01 y pg-r-vector. «Emisor» y «Frontera» se conservan por consistencia con el SD-03. Parte 3 (referencias): todas las citas tienen entrada y todas las entradas se usan; folio del Caso de la Tabla de respaldos corregido a cap. 15, p. 33. Título de la referencia 2026t por confirmar.
- Cierre parte 3: título de la referencia 2026t confirmado por el usuario («What is Azure Database for PostgreSQL flexible server?»; URL flexible-server/overview por confirmar). Parte 4: transversales sin editar (opción 1), quedan registradas. Parte 5 (formularios) después de los diagramas.
- Lámina B (Chile Central por frente): primera versión generada con el generador generar_laminas.py y estilo F2; en revisión del usuario. Sin E-NN. Archivos en registro-diseno-fisica/diagramas-laminas/salida/.

## 2026-11-09 · Registro de trazabilidad y figuras físicas completas

- Pedido del usuario: registrar todos los cambios para la futura tabla de trazabilidad, sin omitir elementos, y agregar los diagramas que el texto necesite.
- Creados `registro-cambios-trazabilidad.md` (resumen, decisiones, supuestos, tablas, figuras, pendientes) y `registro-cambios-detalle.md` (todos los cambios frase por frase, generado desde `git` con `generar_registro_cambios.py`, base `226bca8`).
- 14 figuras físicas nuevas (Figuras 4.12 a 4.25) en lugar de 17. Sin E-NN y con todo el inventario de `01_nodos.md`. Generador, especificaciones y salidas en `registro-diseno-fisica/diagramas-laminas/`; copias en `04_Adjuntos/diagramas/` y `latex_final/figuras/`. Figuras renumeradas y texto ajustado. `verificar` ok, `verificar-redaccion` 0 y 0, vista previa compilada de 91 páginas.
- Cierre de sesión (09-11): el usuario decide dejar las figuras como están, con leyenda, sin tablas de conexiones ni reducción a 15-20 elementos. Ideas evaluadas (A1-A3, B1-B3, C1-C3 según FEP01·61, ·74 y ·81) quedan como opción futura.
