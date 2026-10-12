# Evaluación de la EDT del equipo (paso 8a del plan de estimación)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: evaluación hecha por este trabajo, pendiente del visto bueno del equipo. EDT evaluada: `[ELISEO]-entregables_edt.md` (15 ramas, 110 paquetes), que no se modifica. Criterios: `guia_edt.md` (secciones 3 a 8 y la lista de control de la 11) y `sd-03.tex` (SP-04, elección del escenario B, etapas, operación y retiros), `ficha_alcance_sd-03.md` (autonomía de 24 h), `divisiones_negocio_servicios_sd-03.md` (nombres vigentes), los Anexos A a D y las Bases. Controles mecánicos: `python3 05_Gestion/scripts/verificar_edt.py`, que da 93 hallazgos (51 firmes y 42 posibles) sobre esa EDT.

## 1. Lista de control de la guía (sección 11)

| N.º | Pregunta | Resultado | Detalle |
| :-- | :-- | :-- | :-- |
| 1 | ¿Cada servicio y la base tecnológica tienen paquetes con su rango de requerimientos? | **No** | Los 10 paquetes de la rama 1.5 mezclan servicios y ninguno cita un rango de RF. La base tecnológica no tiene nodo propio |
| 2 | ¿Los 28 resultados del Anexo D se rastrean a un paquete? | **Parcial** | 1.9.4 los nombra, pero no hay traza por paquete. La traza a casos de uso ya existe en `04_trazabilidad_resultados.md` |
| 3 | ¿Aparece cada elemento de la tabla de cobertura de la sección 8? | **Casi** | Faltan el licenciamiento a nombre del cliente (rama de infraestructura) y la base de conocimiento (art. 77.1). Lo demás aparece |
| 4 | ¿Hay un conjunto de paquetes por cada innovación? | **Parcial** | Una sola línea con cinco candidatas de otro equipo; sin tipos confirmados |
| 5 | ¿Ningún nodo es una fase, un hito o una actividad? | **No** | 1.12.1, 1.12.3 y 1.12.5 (marchas blancas y soporte de estabilización), 1.11.5 (convivencia) |
| 6 | ¿Ningún nombre empieza con un verbo? | **Sí** | 0 hallazgos |
| 7 | ¿No hay fechas, meses, horas, costos, duraciones ni dependencias? | **No** | 13 hallazgos firmes: hitos H1 a H12, meses y rangos de meses y «90 días» en títulos de rama y en nombres |
| 8 | ¿Ningún entregable aparece en dos ramas? | **No** | Pruebas de seguridad (1.8.6 y 1.9.3), actas de aceptación (1.1.7, 1.9.5, 1.12.2, 1.12.4, 1.14.5), degradación del evento anual (1.11.4 y la base tecnológica), capacitación (1.13.3, 1.13.4, 1.14.2, 1.15.6), modelo de capacidad (1.3.6) |
| 9 | ¿Nada excluido ni del cliente figura como trabajo propio? | **Parcial** | 1.5.8 desarrolla portales y app, contra la Opción A. 1.4.7, 1.4.16 y 1.11.3 suenan a ejecutar obra o instalar |
| 10 | ¿Cada paquete tiene un responsable único (rol)? | **No aplica aún** | Falta el diccionario (Pendiente 10 de la propia EDT) |
| 11 | ¿Todo criterio de aceptación sale del Anexo B o D? | **No aplica aún** | Falta el diccionario |
| 12 | ¿El total y los paquetes por servicio caen en los rangos? | **Parcial** | 110 paquetes, dentro de 100 a 250. Pero la rama de software tiene 10 paquetes para 14 unidades |
| 13 | ¿Se usaron solo los nombres y códigos vigentes? | **No** | 1.5.1 y 1.5.7 usan nombres antiguos de servicios; 29 nombres traen códigos externos |
| 14 | ¿Hay alguna cifra sin fuente? | **Parcial** | Las cifras del Caso se verificaron (940 proveedores, 268.000 referencias, 140 m², 13 tiendas, 22 tiendas y 2 centros, 380 líneas de caja, esquema 3-2-1-1-0). No se pudo verificar «15 materias» (1.1.4) ni la RAN 20-7 (1.8.7). «25 decisiones» sí tiene respaldo (Caso, numeral 16.1) |

## 2. Hallazgos

Severidad: A alta, M media, B baja. «Efecto» indica cómo toca la estimación: UCP es lo que ya cubren los 127 casos de uso; «tres valores» es lo que el UCP no cubre.

| N.º | Sev. | Paquete(s) | Problema | Evidencia | Acción | Efecto en la estimación |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | A | 1.5.8 | Desarrolla portales (público, cliente, vendedor y proveedor) y app móvil en 5 perfiles; contradice la Opción A y no está en el UCP | `contexto_sd-04.md` D-08 a D-11; `sd-03.tex` no menciona portales ni app. Riesgo: el Caso (RT-17.01) exige la app, así que el sd-03 o el sd-04 deben declarar que la cubre la app existente de AS-04 | Quitar (decidido por el usuario) y dejar anotado el riesgo | Ninguno si sale. Si volviera, sería alcance nuevo fuera del UCP |
| 2 | A | 1.5.1 a 1.5.9 | Cada paquete mezcla servicios (por ejemplo marketplace, posventa y fidelización en 1.5.5) y son 10 para 14 unidades | Guía §6 | Un nodo por servicio con 3 a 8 paquetes (decidido) | Habilita el reparto de las horas del UCP por paquete |
| 3 | A | Títulos de 1.2, 1.3, 1.4, 1.5 y 1.15; 1.8.6, 1.9.5, 1.11.5, 1.12.1 a 1.12.4, 1.14.3 | Hitos, meses y duraciones en nombres y títulos | Guía §7 y control 7 | Quitarlos; irán como atributo cuando exista el cronograma | Ninguno |
| 4 | A | 1.3.5 y Pendiente 7 | «8 h tienda / 4 h CD» contradice el mínimo de 24 h de las Bases Transversales (RT-03.10); el caso solo puede endurecer | Bases Transversales RT-03.10; precedencia en AGENTS.md; ficha de alcance: «24 horas, no existe otro valor» | Corregir a 24 h. El código RT-03.13 significa cosas distintas en el Caso (sincronización tras la reconexión) y en las Transversales (declarar funciones no disponibles): anotarlo | Ninguno en horas; afecta el criterio de aceptación |
| 5 | M | 1.12.1, 1.12.3, 1.12.5, 1.11.5 | Son fases o actividades | Guía §3 y §7 | Reemplazar por entregables: plan de marcha blanca, informe de resultados, evidencia de cierre | Tres valores |
| 6 | M | 1.7.11 y Pendiente 5 | «Condicionado al escenario A o B»: SP-01 está registrado en el Anexo A y el sd-03 ya eligió el escenario B | Anexo A, SP-01; sd-03, elección del escenario B | Quitar la condición | Tres valores |
| 7 | M | 1.6.3, 1.6.5, 1.6.6, 1.6.7 | Los conectores propios de un servicio van en la rama del servicio, y el UCP ya los cuenta en los casos (AS-01, AS-02, AS-04, AS-07 y AS-11) | Guía §6; casos CU-CM-02, CU-PE-15, CU-VE-10 | Mover al servicio y no estimarlos dos veces | **Riesgo de doble conteo**: UCP y tres valores |
| 8 | M | 1.5.10 | La plataforma DevSecOps (CI/CD, IaC) no la cubre el UCP y figura como software | Plan G7 | Moverla a infraestructura | Tres valores |
| 9 | M | 1.8.6 y 1.9.3; 1.1.7, 1.9.5, 1.12.2, 1.12.4 y 1.14.5; 1.11.4; 1.13.3, 1.13.4, 1.14.2 y 1.15.6; 1.3.6 | Entregables duplicados en dos ramas | Guía §7 | Dejar cada uno en una sola rama | Evita doble conteo |
| 10 | M | 29 nombres con códigos, 7 con umbrales o cifras | «Art. 72», «RT-05.11», «≤8 s», «≤5 min», «RPO/RTO = 100 %»; incumple la regla de nombres de la propia EDT | Encabezado de la EDT y guía §6 | Mover al criterio de aceptación | Ninguno |
| 11 | M | 1.2.7, 1.6.2, 1.9.3, 1.9.5, 1.14.1 y otros 29 posibles | Varios entregables en un solo nombre | «Un nombre, un entregable» | Dividir | Aumenta la cantidad de paquetes |
| 12 | M | 1.4.7, 1.4.16, 1.11.3 | `sd-03.tex` (SP-04) ya fija el reparto: el proponente provee el centro de datos con su conectividad, seguridad y canalizaciones (RT-06.33) y el cliente hace la obra civil de separación (RT-06.06, RC-04). En tiendas y centros el cliente adquiere y ejecuta, y el proponente especifica, costea, coordina, certifica y configura (EXC-19). Los paquetes del centro de datos son legítimos; los tres nombrados suenan a obra o instalación | `sd-03.tex` SP-04; Anexo A | Mantener los paquetes del centro de datos; renombrar 1.4.7 como especificación y coordinación de la obra, y 1.4.16 y 1.11.3 como configuración y certificación | Tres valores |
| 13 | M | 1.5.1 a 1.5.7 | Nombres antiguos de los servicios («Catálogo, precios y promociones», «Frontera X-01») | `divisiones_negocio_servicios_sd-03.md` | Renombrar con los nombres vigentes | Ninguno |
| 14 | M | 1.4.5, 1.8.3, 1.5.9 | La base tecnológica no tiene nodo propio y su mecanismo de degradación y congelamiento (RF-177 a RF-186) no aparece. En el UCP la base pesa 65 puntos | sd-03 3.3.1; casos CU-BT-* | Crear un nodo «Base tecnológica» | UCP |
| 15 | M | Rama de infraestructura (1.4) | Falta el licenciamiento a nombre del cliente | Guía §8 (cobertura) | Agregar un paquete de licenciamiento | Tres valores |
| 16 | M | Rama de documentación (1.14) | Falta la base de conocimiento con incidentes, problemas, soluciones y decisiones de diseño | Bases, art. 77.1 | Agregar un paquete | Tres valores |
| 17 | B | 1.8.7 | Cita la RAN 20-7 de la CMF, que no aparece en las Bases ni en el Caso | Búsqueda en Bases y Caso | Verificar la fuente o quitarla | Ninguno |
| 18 | B | 1.1.4 | «25 decisiones» tiene respaldo (Caso, numeral 16.1); «15 materias» no pudo verificarse | Caso 16.1 | Verificar «15 materias» o quitar la cifra | Ninguno |
| 19 | B | 1.10 | Cinco innovaciones aún candidatas, de otro equipo | Guía §5 | Cinco paquetes «innovación por definir», uno por tipo | Tres valores (reserva) |
| 20 | B | Todos | Falta el atributo de Etapa (Pendiente 4 de la EDT) | Pendiente 4 | Asignarla por servicio con el sd-03 | Habilita el reparto por etapa |
| 21 | B | 1.2.4 | El catálogo de requerimientos ya existe (Anexo B del sd-03) | — | Dejar solo su mantención | Ninguno |

## 3. Lo que está bien

- La EDT es de entregables y no de fases en casi todas las ramas, con nombres de sustantivos (el verificador no encontró verbos al inicio).
- Cubre seguridad, calidad, migración, implantación, documentación, transferencia, operación e innovaciones (la rama 1.10 queda a medias).
- Las cifras del Caso que cita están bien. Se encontraron por separado los pendientes que la propia EDT lista (códigos provisorios, hitos del E-25, T-21 y diccionario).
- Reconoce el reparto físico del SP-04 en la mayoría de los paquetes (1.3.7, 1.4.6).
- Total de 110 paquetes dentro del rango de control.

## 4. Decisiones del usuario (2026-10-08)

1. La versión corregida va en una copia aparte; el archivo de Eliseo no se modifica.
2. El paquete 1.5.8 sale (Opción A).
3. La rama de software pasa a un nodo por servicio con 3 a 8 paquetes.

## 5. Preguntas abiertas para el equipo, con sugerencia

1. ¿Qué cinco innovaciones se confirman (1.10)? Sugiero dejar cinco paquetes «innovación por definir», uno por tipo, y cerrarlo con el sd-13.
2. ¿La RAN 20-7 de la CMF tiene una fuente en el expediente? Sugiero quitarla del nombre; si se mantiene, citarla solo en el criterio de aceptación con su fuente.
3. ¿Qué son las «15 materias» de 1.1.4? Sugiero quitar la cifra del nombre.
4. ¿Dónde se declara que la app existente de AS-04 cubre RT-17.01? Sugiero una frase en el sd-03 (alcance) o en el sd-04, que remita a la decisión D-08.
5. ¿Se agregan paquetes de licenciamiento y de base de conocimiento? Sugiero que sí: la guía y el art. 77.1 los piden.
6. ¿Quién completa el diccionario por paquete (criterio, responsable en rol, dependencias)? Sugiero dejarlo para el T-14, con «por definir» en lo que dependa del sd-12.

## 6. Qué sigue

El paso 8b: una copia corregida, `14_edt_corregida.md`, aplicando los hallazgos 1 a 16 y con las diferencias frente a la original.
