# Pendientes de decisión del SD-04, ordenados por impacto en la nota

**Fecha:** 2026-11-09. **Estado:** parcial; decisiones del usuario aplicadas al `.tex` salvo las bloqueadas (ver «Estado de las decisiones»). Cubre 4.3 y 4.2 (sesión A). 4.1 se agrega en la sesión B. Sin revisión humana.

## Cómo se ordena

| Prioridad | Criterio | Fuente |
| :--- | :--- | :--- |
| 1 | Sanción explícita en las Bases: «observación grave», «no será aceptado», línea roja, cronograma | Art. 16.2, Art. 16.3, RT-02.11, RT-03.13 |
| 2 | RT «Obligatorio» incumplido o sin respuesta | RT-03.17, RT-06.01, RT-06.33, RT-07.04, RT-07.09 a RT-07.12 |
| 3 | Contradicción entre documentos, que el profesor detecta al cruzar secciones | Rúbrica S4-06 a S4-14 y Comunicado 10 |
| 4 | Deseable, legibilidad o autorizaciones | RT «Deseable», formularios |

Dentro de cada nivel van primero las decisiones que desbloquean a otras y después las más baratas de resolver.

**Cómo leer la tabla.** La opción 1 es la que ya está redactada en el `.tex` o la que recomiendo. «Cambios» son pasajes del `.tex` o documentos que se tocan si eliges esa opción: son estimaciones mías, no cuentas exactas. «RT que incumple» aplica solo a la opción indicada. «Origen» dice si la respuesta sale de las Bases, del inventario o de tu decisión.

## Prioridad 1 · Sanción explícita

| ID | Decisión | Base en juego | Opción 1 (recomendada) | Opción 2 | Opción 3 | Cambios | RT que incumple | Desbloquea | Origen |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P-01 | Alta disponibilidad de PostgreSQL en Brasil opera en una sola zona (bloqueo de Microsoft) | Art. 16.3: «una sola zona no será aceptado» | A+B del informe: declarar limitación temporal, revisar en la suscripción antes de la Etapa 1 y evaluar otra región. **Ya redactado** | Cambiar ahora a una región sudamericana con alta disponibilidad entre zonas (no verificada) | Usar la alternativa nacional para PostgreSQL | 1: 0 más. 2: unos 12 pasajes (4.2.4, 4.2.5, 4.3.2, Tablas 4.17, 4.20, 4.24), el catálogo y S-03. 3: diseño nuevo | 1: Art. 16.3 | P-18, P-19 | Tu decisión |
| P-02 | Funciones que **no** están disponibles sin enlace y su procedimiento manual | RT-03.13: «observación grave» si falta | Tabla por función en 4.1.12 con el procedimiento manual (unas 8 filas) | Anexo con la tabla y remisión desde 4.1.12 | Remitir al SD-03 3.4.5 | 1: 1 tabla nueva. 2: 1 anexo. 3: 0 | 3: RT-03.13 | Ninguno | 4.1 (sesión B) |
| P-03 | Puntos únicos de falla que se declaran | RT-02.11: «observación grave» si se omiten | Los cinco grupos redactados en 4.2.6 (DC-01, ERP/DTE, WMS, servicios globales) | Alinear con los ocho de T-12 (enlace de tienda, CD-02, zona, región, ERP/DTE, WMS, bus y conexión de DC-01) | Declarar solo los que no tienen contingencia | 1: 0. 2: 1 párrafo y T-12. 3: 1 párrafo | 3: RT-02.11 si omite alguno | Ninguno | Inventario `04` y `T-12` |

## Prioridad 2 · Obligatorio

| ID | Decisión | Base en juego | Opción 1 (recomendada) | Opción 2 | Opción 3 | Cambios | RT que incumple | Desbloquea | Origen |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P-04 | Tiempo de conmutación entre accesos de tienda | RT-03.17: «tiempo de conmutación declarado» | Declarar un valor objetivo como supuesto (por ejemplo 30 segundos) y medirlo en el corte provocado | Declarar 60 segundos | «El que mida el ensayo» (hoy) | 1 y 2: 1 frase y T-12. 3: 0 | 3: RT-03.17 | Ninguno | Tu decisión (el inventario no fija cifra) |
| P-05 | Desde cuándo corre el RTO, qué servicios son críticos, quién declara la contingencia y con qué umbral | RT-07.04, RT-07.05, RT-10.02 | RTO desde la declaración, servicios críticos según SD-09 y umbral de dos sondas con verificación humana | RTO desde la falla (incluye detección y decisión) | Presupuesto de tiempo por etapa de las siete | 1: 2 frases. 2: 1 frase y revisar la etapa de declaración. 3: tabla de 7 filas | Ninguno si se declara | P-09, P-11 | Tu decisión |
| P-06 | Respaldo 3-2-1-1-0: frecuencia, retención y tiempo de restauración por dominio | RT-07.09 a RT-07.13 | Tabla por dominio en un anexo y remisión desde 4.2.6 | Tabla en 4.3.2 | Remisión sola (hoy) | 1: 1 anexo y 1 frase. 2: 1 tabla de 8 filas. 3: 0 | 3: RT-07.13 | Ninguno | Inventario `04-datos-custodia` |
| P-07 | Origen del material de claves para reinyectar en Brasil | RT-07.10: clave independiente de la infraestructura respaldada | Copia de claves en el Key Vault de Brasil con custodia dual y ensayo | Managed HSM replicado también para Retail (cambia S-14) | Procedimiento manual con custodia fuera de Chile | 1: 1 frase. 2: S-14, Tablas 4.16 y 4.20, T-11. 3: 1 párrafo | 3: RT-07.10 si no hay copia independiente | Ninguno | Tu decisión |
| P-08 | RT-06.01: uso exclusivo de la solución frente a los sistemas conservados alojados en el recinto de DC-01 | RT-06.01 | Declarar el recinto como de uso exclusivo de la solución y de los sistemas con que convive | Separación física (jaula) de los sistemas del Cliente: obra | Reconocer la brecha y cerrarla con el informe de 2024 | 1: 1 frase. 2: 1 párrafo, Tabla 4.22 y T-11. 3: 1 párrafo | 3: RT-06.01 | Ninguno | Tu decisión |
| P-09 | Frontera entre «canalizaciones» (proveedor) y «cableado» (Cliente) en DC-01 | RT-06.33, Caso cap. 11 | Proponente provee canalizaciones y Cliente ejecuta cableado, con la frontera en el rack (hoy, ambigua) | Proponente provee y ejecuta ambos en el recinto | Cliente ejecuta todo y el proponente especifica | 1: 1 frase. 2: Tabla 4.22, SD-03 L311 y T-11. 3: igual | 3: RT-06.33 | Ninguno | Tu decisión |
| P-10 | Punto de recuperación coherente entre los 12 servidores y atomicidad del registro del consumidor | RT-02.06, RT-07.04 | El efecto y su identificador se confirman en la misma transacción y servidor, y el corte común se fija por una marca de tiempo | Marca de agua global coordinada | Reconstruir desde el Data Lake | 1: 2 frases y 4.1.8. 2: 1 párrafo. 3: 1 párrafo y cambia el RPO | 3: RT-07.04 (RPO) | Ninguno | Tu decisión |
| P-11 | Tipología de cada sitio (S-33) | Transversales §6.1 | Tienda y centros: sala técnica secundaria o de sitio (hoy) | Tienda: gabinete, como el Caso | Centros: sala principal | 1: 0. 2: 1 párrafo en 4.2.2 y 4.2.1. 3: 4.3.1 | 2: ninguno, pero dimensiona menos | Ninguno | Tu validación |
| P-12 | Alternativa nacional si el Cliente no aprueba Brasil | RT-07.02, RT-07.04 | Tabla corta que compare Brasil y Chile con dimensionamiento y ensayo mínimos | Diseño completo de la alternativa | Solo declararla (hoy) | 1: 1 tabla. 2: 1 subsección y figura. 3: 0 | 3: RT-07.04 si no se ensaya | Depende de P-01 | Tu decisión |

## Prioridad 3 · Contradicción entre documentos

| ID | Decisión | Base en juego | Opción 1 (recomendada) | Opción 2 | Opción 3 | Cambios | RT que incumple | Desbloquea | Origen |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| P-13 | Plazo de la aprobación de residencia (hoy tres: antes de la Etapa 1, de habilitar la réplica y de cerrar el diseño detallado) | Art. 23 y Ley 21.719 | Unificar en «antes de cerrar el diseño detallado» (hito de 4.1.16) | Unificar en «antes de la Etapa 1» | Mantener un hito por tipo de dato | 1 y 2: 4 pasajes. 3: 0 | Ninguno | — | Tu decisión |
| P-14 | Estado inicial del origen de Brasil en Front Door: ¿deshabilitado hasta la etapa seis o habilitado con menor prioridad? | RT-07.08 (deseable) y RT-07.05 | Deshabilitado y activado por el equipo (protección contra falso positivo) | Habilitado con menor prioridad, conmutación automática | Habilitado con peso cero | 1: 1 frase. 2: 2 pasajes y 4.2.4. 3: 2 pasajes | Ninguno | Ninguno | Tu decisión |
| P-15 | Registro de identificadores frente a ventana de deduplicación y su intervalo | RT-02.06 | Registro permanente en el servicio consumidor | Ventana igual al retraso máximo más el RTO | Ventana fija de 7 días | 1: 2 pasajes en 4.3.2. 2: 3. 3: 3 | Ninguno | Ninguno | Tu decisión |
| P-16 | Escenario de conciliación: 8 horas en 4.2.6 frente a 24 horas en el SD-03 | RT-03.10, RT-03.13 | Alinear a 24 horas con conciliación en 30 minutos | Mantener ambos escenarios con su umbral | Quitar el de 8 horas | 1: 1 pasaje. 2: 1 frase. 3: 1 pasaje | Ninguno | Ninguno | SD-03 y Bases |
| P-17 | Service Bus zonal: la Tabla 4.19 dice «donde la región la ofrece» y la Tabla 4.18 dice «continuidad» | RT-07.01 | Comprobar en la suscripción y quitar la condición | Declarar la condición también en la Tabla 4.18 | Mantener | 1 y 2: 1 celda | Ninguno | Ninguno | Inventario `01` |
| P-18 | Hipervisor y virtualización en DC-01 | Art. 14.2: licencias a nombre del Cliente | Supuesto declarado: producto y licencia en el levantamiento (hoy) | Fijar el producto ahora | Sin virtualización, equipos físicos | 1: 0. 2: 1 frase, T-11 y la oferta económica. 3: 1 frase y `10-espacio-racks` | Ninguno | Ninguno | Inventario `10`: «hosts de integración/virtualización» sin decidir |
| P-21 | Mover la tabla de direcciones IP (Tabla 4.17) y su párrafo a un anexo | Comunicado 10: «el subdocumento resume, el anexo detalla» (RR-05) | Moverlas a un anexo y dejar una frase y una remisión (lo sugiere el lector no técnico) | Dejarlas y simplificar el párrafo | Dejarlas | 1: 1 anexo, 2 pasajes. 2: 1 pasaje. 3: 0 | Ninguno | Ninguno | Tu decisión |
| P-22 | Numeración de RT-03.13: el Caso 09 la rotula «sincronización tras la reconexión» y las Bases Transversales «funciones no disponibles sin enlace» | RT-03.13 | Citar «el plazo que el Caso fija para la sincronización» sin número (hoy) | Citar «RT-03.12 (Bases) y su valor del Caso» | Citar RT-03.13 con aclaración en nota | 1: 0. 2 y 3: 2 pasajes y T-12 | Ninguno | Ninguno | Bases y Caso |
| P-23 | Proveedores distintos en los dos accesos de DC-01 y segundo enlace de CD-02 (RT-03.17) | RT-03.17: «caminos físicos y proveedores distintos» | Declarar los accesos de DC-01 como propuestos de proveedores distintos y CD-02 con el router móvil como segundo camino (hoy) | Marcar CD-02 como incumplimiento temporal hasta que el Cliente contrate el segundo enlace | Condicionar el contrato del segundo enlace al hito de Etapa 1 | 1: 0. 2: 1 frase y T-12. 3: 1 frase | 1: RT-03.17 parcial en CD-02 | Ninguno | Caso cap. 6, Bases |

## Prioridad 4 · Autorizaciones

| ID | Decisión | Opción 1 (recomendada) | Opción 2 | Opción 3 | Cambios |
| :--- | :--- | :--- | :--- | :--- | :--- |
| P-19 | Editar los formularios T-11, T-12 y T-14 | Autorizar después de cerrar 4.2 y 4.1, uno por uno | Autorizar T-11 ahora | No editarlos | 1: 3 formularios. Ver `ajustes-otros-documentos.md` |
| P-20 | Verificar la resolución RAEX202503748 en el Diario Oficial | Verificar el emisor y la fecha | Citarla como está | Quitarla y citar solo la Ley 21.719 | 1: 1 entrada de Referencias |

## Estado de las decisiones (09-11-2026)

| ID | Elegida | Estado | Dónde |
| :--- | :--- | :--- | :--- |
| P-01 | 2, sin región disponible; se cierra con la 1 (cita de Microsoft agregada, 2026t) | **Verificada en la tabla de Microsoft (09-11):** Brazil South marca «$» (implementaciones nuevas de alta disponibilidad entre zonas bloqueadas temporalmente); Brazil Southeast no la admite y es de acceso restringido; Chile Central sí, pero es la primaria. No hay región a la que cambiar. Texto vigente: limitación temporal, revisión en la suscripción antes de la Etapa 1 y evaluación de otra región. Falta solo la prueba con `az postgres flexible-server list-skus` | 4.3.2.2 |
| P-02 | 1 | Aplicada: Tabla 4.28 con ocho funciones (S-46) | 4.1.12 |
| P-03 | 2 | Aplicada: ocho puntos únicos alineados con T-12 | 4.2.6; T-12 en `ajustes-otros-documentos.md` |
| P-04 | 1 | Aplicada: 30 segundos como objetivo (S-38) | 4.2.6 |
| P-05 | 1 | Aplicada con ajuste: el RTO corre desde la interrupción declarada (SD-09 L185). SD-09 no lista los servicios críticos, así que se identifican con el Cliente en el diseño detallado | 4.3.2.2 |
| P-06 | 1 → tabla en 4.3.2 (decisión del usuario 09-11) | Aplicada: Tabla 4.25 con retención y copia en Brasil por dominio. Frecuencia, retención de largo plazo de PostgreSQL y tiempo de restauración quedan al diseño detallado, porque el inventario no los fija | 4.3.2.1 |
| P-07 | 1 | Aplicada (S-39) | 4.3.2 |
| P-08 | 1 | Aplicada (S-40) | 4.2.1 |
| P-09 | 1 | Aplicada (S-41) | 4.2.1, Tabla 4.22 |
| P-10 | 1 | Aplicada en 4.3.2 y 4.1.8 (S-42) | 4.3.2, 4.1.8 |
| P-11 | 1 | Sin cambios | — |
| P-12 | 1 | Aplicada: Tabla 4.25 (S-44). Depende de P-01 | 4.3.2.1 |
| P-13 | 1 | Aplicada: «antes de cerrar el diseño detallado» | 4.3.2.1 |
| P-14 | 1 | Aplicada (S-45) | 4.3.2.2 |
| P-15 | 2 | Aplicada: ventana = retraso máximo + RTO (S-43) | 4.3.2 |
| P-16 | 1 | Aplicada | 4.2.6 |
| P-17 | 1 | Aplicada: el usuario confirma que Service Bus zonal existe en Chile Central; se quitó la condición | Tabla 4.19 |
| P-18 | 1 | Sin cambios | — |
| P-19 | 1 | Sin cambios: formularios después de 4.1, uno por uno | — |
| P-20 | 3 | Aplicada: quitada RAEX202503748 del texto y de Referencias | 4.3.2.1, Referencias |
| P-21 | 1 → dejar la tabla donde está (decisión del usuario 09-11) | Sin cambios | 4.2.4 |
| P-22 | 1 | Sin cambios | — |
| P-23 | 1 | Sin cambios | — |

Tablas nuevas: 4.25 (respaldos), 4.26 (alternativa en Chile, antes 4.25), 4.27 (uso de IA, antes 4.26) y 4.28 (funciones sin enlace). La numeración global está fuera de orden (4.12 y 4.28 antes que 4.1 y 4.10; 4.22 en 4.2.1) y se ordena en el cierre.

## Resueltas en esta sesión (para trazabilidad)

| Tema | Resolución | Registro |
| :--- | :--- | :--- |
| Quién compra el par local de captura de los centros | Proponente | Tabla 4.22, 4.2.1 |
| RT-06.33 en tiendas y centros | Alternativa A | S-37 |
| Software de los servidores | Contenedores, sin hipervisor en tienda | S-37, 4.2.1 |
| Artículo 16.2: justificar el emplazamiento por componente | Tabla 4.14 con los seis factores | 4.2.2 |
| Tipología, RAID, CIS, FinOps y reversibilidad | Redactadas | S-33 a S-36 |

## Qué falta para completar este archivo

Sesión B hecha el 09-11 para 4.1 (actores 25, tenant único, motor local PostgreSQL, funciones sin enlace, ADR-09, Front Door con dos perfiles, canal de entrega, Redis y HSM). Queda para el cierre: nombres frente al glosario en todo el cuerpo (C-086), numeración de tablas y las transversales (SD-13, SD-05, SD-07).
