# Ajustes que el SD-04 pide a otros documentos

**Fecha:** 2026-11-06. **Estado:** lista para quien edite cada documento. Ninguno se editó desde la sesión del SD-04: el SD-03 es referencia, los formularios requieren tu autorización una por una y SD-05, SD-07 y SD-13 se tocan en sus ciclos. Líneas a esta fecha. Hallazgos del `informe-cotejo.md` entre paréntesis.

## SD-03

| N.º | Línea | Qué dice | Qué pide el SD-04 | Base |
| ---: | ---: | :--- | :--- | :--- |
| 1 | 140, 311 | «la compañía adquiere el equipamiento de las tiendas y de los centros de distribución» | Precisar: el Cliente compra terminales, dispositivos de sala, lectores, impresoras y equipamiento de red. El proponente provee los servidores de tienda y los componentes on-premise (C-028) | Art. 14.2; Caso cap. 11 |
| 2 | 300 (SP-02) | Concepción «se mantiene como está durante el contrato» | Agregar que opera con un par local de captura durable de registros estructurados, sin WMS. L498 del SD-03 ya habla de «registros estructurados» (C-070) | Caso decisión 20; Art. 16.4 |
| 3 | 385, 551, 553, 555, 577, 579, 589, 591, 621, 623, 654, 739, 745 | «ámbito» | El glosario del SD-04 usa «frente», definido en el propio SD-03. Unificar o dejar a criterio del equipo | Glosario 08, regla 4 |
| 4 | 633 | Cita la propuesta de la CMF de abril de 2026 como consulta no vigente | El SD-04 L1109 afirma lo que admite la norma de externalización sin cita (C-079). Acordar una sola fuente y su estado | REV-D-08 |
| 5 | 140 | «El proponente provee el centro de datos on-premise con su conectividad y sus canalizaciones» | Coincide con RT-06.33. La Tabla 4.22 del SD-04 deberá igualarse (C-029) | RT-06.33 |

## SD-05

| N.º | Línea | Qué dice | Qué pide el SD-04 |
| ---: | ---: | :--- | :--- |
| 1 | 392 y 355 | Event Hubs, con retención de 90 días | El SD-04 eligió Service Bus (ADR-06). Sigue abierto REV-E-01 |
| 2 | 355 | PostgreSQL local como diario durable de tienda | El SD-04 4.1.1 dice «Valkey u otro motor local, por decidir» (C-007). Se corrige en el SD-04 |

## SD-07 y T-15

| N.º | Dónde | Qué dice | Qué pide el SD-04 |
| ---: | :--- | :--- | :--- |
| 1 | Tabla de actores (UAW) | 31 actores | El SD-04 usa 25 por el diagrama de contexto. Registrar la fuente (C-008) |
| 2 | Rama 1.4 | Sin tienda de laboratorio | El SD-04 4.2.5 la incluye (D-FIS-17) |
| 3 | 1.4.13 y L830 | «custodia de medios» | El SD-04 no la menciona |
| 4 | L1053 | Despliegue azul-verde | El SD-04 no lo menciona |

## SD-13 y T-19

| N.º | Dónde | Qué dice | Qué pide el SD-04 |
| ---: | :--- | :--- | :--- |
| 1 | L119 | Un adaptador vincula el controlador de lockers con pedidos | E-32: conexión directa con API autenticada |
| 2 | L283-285 | La fila vive en el componente local | E-64 solo cubre tótem a nube; falta en el catálogo el tramo local |
| 3 | L275, L291 | Tótem Zebra KC50 e impresora Epson dentro de la inversión | `01`: lo adquiere el Cliente (Art. 14.2) |
| 4 | L191, L199, L207 | Inferencia y trabajador de representaciones sin lugar físico | Tabla 4.20 L931 solo ubica servicio y base |
| 5 | L201 | Remite la capacidad a «la memoria del subdocumento 4» | Existe en `04_Adjuntos/tablas/sd-04_s2_memoria-capacidad.*`. Contenido no verificado |

## Formularios (requieren tu autorización, uno por uno)

| Formulario | Qué conciliar |
| :--- | :--- |
| T-11 recibida | ExpressRoute en filas 1.19 y 6.6; Sentinel sin separar región (1.13, 3.8); Redis y API Management «por comprobar» (1.4, 1.6); FortiGate en 1.26 frente a «sin fijar fabricantes» en el SD-04; «testigos» en vez de «árbitro»; tienda de laboratorio ausente |
| T-11 OSS (copia local) | Event Hubs con geo-replicación y Kafka; Front Door, Firewall y registro «compartidos» (choca con la línea roja); ExpressRoute como base; firewall Fortinet mínimo 13 |
| T-11(2) | Tercera copia no versionada, con 4 casos de ExpressRoute. Solo se señala |
| T-12 | RT-02.11: ocho puntos con ExpressRoute y remite a «Tabla 4.11» (hoy 4.18, con 11 puntos). RT-03.21: ExpressRoute para DC-01. RT-07.03: geo-replicación de Event Hubs. RT-03.17: tiempo de conmutación y CD-02 |
| T-14 | Falta paquete de tienda de laboratorio. 1.4.3 «segregación física y lógica» frente al «física o lógica» del Caso |

## Adición del 2026-11-08

| Documento | Qué conciliar |
| :--- | :--- |
| T-11 (T-11.4) | Agregar el par local de captura de CD-01 y CD-02 como suministro del proponente (decisión del usuario, 08-11). Hoy solo hay filas de la tienda. Usar «árbitro» y no «testigo» (glosario 08). Falta sistema operativo e hipervisor de los servidores |

| T-11 (T-11.5) | La cita «cap. 11, p. 26» del Caso debe ser p. 27 (el párrafo del hardware está en la p. 27 del OCR paginado). Corregida en el SD-04; el formulario no se editó |

## Adición del 2026-11-09

| Documento | Qué conciliar |
| :--- | :--- |
| T-12 (RT-02.11) | El SD-04 declara ocho puntos únicos: accesos de tienda, enlace único de CD-02, conexión de DC-01, zona, región, ERP/DTE y WMS, y Service Bus. Cambiar «ExpressRoute a DC-01» por «conexión de DC-01», «bus de eventos» por Service Bus y la remisión «Tabla 4.11» por «Tabla 4.18» |
| T-12 (RT-03.17) | Tiempo de conmutación objetivo de 30 segundos (S-38) |
| T-11 (P-09) | DC-01: el proponente provee canalizaciones hasta el rack y el Cliente ejecuta el cableado (S-41) |
| T-11 / SD-03 | SD-03 L311 sobre canalizaciones debe coincidir con S-41 |

## Renumeración de tablas del SD-04 (2026-11-09)

Las 28 tablas del SD-04 se renumeraron por orden de aparición (4.1 a 4.28). Los documentos siguientes citan números antiguos y **no se editaron**. Varios ya estaban desfasados antes (por ejemplo T-12 cita «Tabla 4.2» 158 veces y «Tabla 4.5» como tabla de ADR). Hay que conciliar cada cita por contenido y no solo por número, y los formularios requieren autorización uno por uno.

| Documento | Citas a tablas del SD-04 |
| :--- | :--- |
| T-12 | 185 |
| T-11 | 51 |
| T-22 | 30 |
| SD-06 | 1 (Tabla 4.11) |
| SD-08 | 1 (Tabla 4.9) |
| T-10 | 1 (Tabla 4.6) |

Correspondencia antigua a nueva (solo las que cambian):

| Antigua | Nueva |
| :--- | :--- |
| 4.12 | 4.1 |
| 4.1 | 4.2 |
| 4.2 | 4.3 |
| 4.3 | 4.4 |
| 4.4 | 4.5 |
| 4.5 | 4.6 |
| 4.6 | 4.7 |
| 4.7 | 4.8 |
| 4.8 | 4.9 |
| 4.9 | 4.10 |
| 4.28 | 4.11 |
| 4.10 | 4.12 |
| 4.11 | 4.13 |
| 4.13 | 4.14 |
| 4.22 | 4.15 |
| 4.14 | 4.16 |
| 4.15 | 4.17 |
| 4.16 | 4.18 |
| 4.17 | 4.19 |
| 4.18 | 4.20 |
| 4.19 | 4.21 |
| 4.20 | 4.22 |
| 4.21 | 4.23 |
| 4.23 | 4.24 |
| 4.24 | 4.25 |
| 4.25 | 4.26 |
| 4.26 | 4.27 |
| 4.27 | 4.28 |

## Decisión del 2026-11-09 sobre transversales

SD-05, SD-07 y SD-13 no se editan desde el SD-04. Las discrepancias de las secciones SD-05, SD-07 y SD-13 de este archivo se resuelven en el ciclo de cada subdocumento. Los formularios T-11, T-12, T-14 y T-22 y las citas de tabla de SD-06, SD-08 y T-10 se concilian después de actualizar los diagramas, con autorización formulario por formulario.

## Renumeración de figuras del SD-04 (2026-11-09)

Las figuras físicas pasaron de 17 a 14 (Figuras 4.12 a 4.25). La correspondencia antigua → nueva está en `registro-diseno-fisica/diagramas-laminas/correspondencia-figuras.json`. Documentos que citan «Figura 4.N» y deben revisarse por contenido (sin editar):

- OnlySimpleSolutions-Formulario-T-11.tex: 4
- OnlySimpleSolutions-Formulario-T-22.tex: 3
