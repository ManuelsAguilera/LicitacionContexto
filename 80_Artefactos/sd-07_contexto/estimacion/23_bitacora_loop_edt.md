# Bitácora del loop de mejora de la EDT

Documento de contexto, no es entregable. La llena el loop de `../prompt_loop_edt.md`: una fila por iteración, aceptada o descartada. Tablero: `python3 05_Gestion/scripts/ciclo_edt.py`. Orden de prioridad: sd-03 > 8/80 > menos paquetes.

## Estado inicial (iteración 0, 2026-10-08)

Cubrió los 12 compromisos del sd-03 sin entregable con 11 cuentas nuevas y 2 renombres, y ajustó la ventana de 1.4.2. Commit `14bdefa`.

| Meta | Antes de la iteración 0 | Después |
| :-- | :-- | :-- |
| H1 coherencia mecánica | 7 de 7 | 7 de 7 |
| H2 compromisos del sd-03 | 4 de 16 | 16 de 16 |
| H3 verificador | 0 firmes | 0 firmes |
| H4 mapa | 0 | 0 |
| H5 cronograma | 0 | 0 |
| H6 traza directa | no medida | 51 cuentas sin traza de 164 |
| H7 traza inversa | no medida | cumple |
| H8 8/80 | cumple en la ola 1 | cumple (689 paquetes de software proyectados, de 25 a 74 h) |
| H9 horas del UCP | 31.850 h | 31.850 h |

## Iteraciones

| N.º | Clase | Cambio | Justificación (elemento del sd-03) | Metas antes | Metas después | Decisión |
| --: | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | b (H6, traza directa) | Se agregó a 34 cuentas una cita verificada en `sd-03.tex` o en sus anexos (atributo `origen:`) | Cada cita nombra la sección, la tabla, el RNF, la exclusión o el resultado del sd-03 de donde sale la cuenta; las frases clave se comprobaron con búsqueda en `sd-03.tex` y en los Anexos A, B y D | H6: 51 sin traza; H1 a H5 y H7 a H9 cumplen | H6: 17 sin traza; H1 a H5 y H7 a H9 cumplen | Aceptada |
| 2 | b (H6, traza directa) | Se agregó una cita verificada a 4 cuentas más: 1.4.1 (nube), 1.4.4 (ambientes), 1.9.8 y 1.9.9 (certificaciones de calidad) | sd-03 3.1 (despliegue híbrido con la carga principal en nube pública); 3.4.1 (pruebas en preproducción); 3.2.5 (el equipo del proponente controla la calidad antes de presentar cada entregable) | H6: 17 sin traza; el resto cumple | H6: 13 sin traza; el resto cumple | Aceptada |

## Preguntas abiertas (cuentas sin cita cierta en el sd-03)

Las 13 cuentas siguientes no tienen en `sd-03.tex` ni en sus anexos una frase que las respalde. Se justifican con las Bases o con la guía de la EDT, no con el sd-03. El loop no inventa la cita. Decisión del usuario: ¿se aceptan como cuentas de gestión y de infraestructura respaldadas por las Bases (se les pone esa fuente) o se retiran?

| Cuenta | Nombre | Fuente que sí existe |
| :-- | :-- | :-- |
| 1.1.1 | Plan de dirección integrado | Comunicado 10, 7.1; Formulario T-14 (Bases) |
| 1.1.12 | Acta de constitución del proyecto | Práctica de PMBOK 6; no está en las Bases ni en el sd-03 |
| 1.1.13 | Línea base de costos y presupuesto | Oferta económica (Bases) |
| 1.3.1 | Documento de arquitectura y catálogo de decisiones | Art. 19 de las Bases (descripción conforme a ISO/IEC/IEEE 42010 con vistas lógica, de procesos, de despliegue, de datos y de seguridad, y registro de decisiones de arquitectura) |
| 1.4.6 | Plataforma de integración y entrega continuas | Bases Transversales (RT) |
| 1.4.7 | Licenciamiento de terceros a nombre del cliente | Art. 14.2 de las Bases (licenciamiento de software de base, de plataforma y de terceros a nombre del cliente) |
| 1.7.4 | Corte de inventario en las 24 instalaciones | Caso (22 tiendas y 2 centros) |
| 1.8.1 | Plan de seguridad, controles y modelo de amenazas | Art. 19 de las Bases (arquitectura y diseño, incluida la de seguridad); por verificar |
| 1.8.3 | Superficie de exposición y respuesta a incidentes | Bases Transversales (RT) |
| 1.8.10 | Informe de diligencia del proveedor de nube | Sin fuente en el repositorio (la norma CMF no aparece en las Bases) |
| 1.9.2 | Estándares de codificación, revisión por pares y puertas de calidad | Comunicado 10, 9.3 (actividades de calidad) |
| 1.12.9 | Informe del soporte de estabilización | Art. 14.2 de las Bases (implantación, marcha blanca, paso a producción y estabilización) |
| 1.14.9 | Informe de lecciones aprendidas | Práctica de PMBOK 6 |

## Corrección de la regla de proyección (2026-10-09)

Al cierre se revisó el número de 689 «paquetes de software». Era una proyección de la regla «un paquete por caso y fase (análisis, diseño, construcción y pruebas), partido por transacción», que convertía actividades en nodos de la EDT. El usuario aprobó el cambio: en el software, el paquete de trabajo es el entregable de un caso de uso (127 paquetes de unos 250 h, excepción declarada a 8/80 como subproyectos) y las fases son actividades del cronograma (689, de 25 a 74 h). El tablero ahora cuenta 127 paquetes y 689 actividades (S1) y H8 mide las actividades; H9 comprueba que los 127 paquetes suman las 31.850 h. Ver `20_evaluacion_8_80.md`, sección 5.

## Cierre del loop (2026-10-08)

Se detiene tras 2 iteraciones aceptadas porque no queda un cambio honesto que mejore una meta dura: las 13 cuentas sin traza no tienen una cita cierta en el sd-03, y las demás clases (más de 80 h, menos de 8 h o más de un mes, hallazgos firmes, duplicados) no tienen infractores que corregir. Lo que falta es una decisión humana, listada arriba.
