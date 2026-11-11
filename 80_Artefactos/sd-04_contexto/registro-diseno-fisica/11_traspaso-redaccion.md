# Traspaso a la sesión de redacción del sd-04

Esta sesión recopiló datos y decisiones. No redactó. Aquí queda todo lo que la sesión de redacción debe aplicar al `.tex` (`02_Propuesta/latex_final/sd-04/OnlySimpleSolutions-Subdocumento4.tex`).

Reglas: no inventar hechos (si el Caso o las Bases dicen X, se declara X; las mejoras se presentan como propuesta). Cifras de costos solo en `07_costos-interno.md`. Formularios T-11, T-12 y T-16 no se editan aquí. Los números de línea son de 06-11-2026 y se mueven al editar.

## A. Duplicación por resolver

| ID | Dónde | Qué pasa | Arreglo propuesto |
| :--- | :--- | :--- | :--- |
| H-16 | 4.2.1 (~línea 665) y 4.3.1 (~línea 1040) | DC-01 se describe dos veces: cuatro racks de 42U, reserva de 80 de 168U, zonas Retail y Filial con red propia y dos pares de servidores de integración. 4.2.1 cita la Figura 4.25 antes de que aparezca | Dejar en 4.2.1 solo lo que se provee y remitir a 4.3.1; dejar el detalle y la figura en 4.3.1 |
| H-16b | 4.2.1 (~línea 677) y 4.3.1 (~línea 1054) | Centros de distribución: el router 4G/5G, el enlace único de CD-02 y el segundo enlace propuesto se dicen en ambas | En 4.2.1 dejar el equipamiento; el enlace en 4.3.1 |

## B. Pasajes que cambié en esta sesión (releer en conjunto)

| Supuesto | Qué dice ahora el `.tex` | Dónde buscar |
| :--- | :--- | :--- |
| S-23 Power BI | Condicional: Microsoft lo ofrece en Chile Central, no el resto de Fabric; si no se contrata esa capacidad, el Cliente aprueba la residencia antes de la Etapa 1 | párrafo de 4.3.2.1 (~línea 1107); Tablas 4.9 y 4.12; ADR-09 (~línea 601) |
| S-10 Concepción | Enlace único tal como dice el Caso; el router 4G/5G es el segundo camino; el segundo enlace fijo es una propuesta al Cliente, no un hecho | CD-02 en Tabla 4.21 (~línea 644), Tabla 4.18 (~línea 875), 4.2.1 y 4.3.1 |
| S-09 ExpressRoute | Retirado; la conexión de DC-01 es una VPN por frente (RT-03.21); GatewaySubnet mínimo /27 | 4.2.4 (~líneas 781 y 791), Tabla 4.18 y mapeo 4.2.7 (~línea 926) |
| S-01 | Justificación agregada de la decisión del árbitro (el testigo en nube falla con el enlace caído y un servidor caído, RT-03.10) | 4.2.1 (~línea 657) |
| S-02 | Tienda de laboratorio con dos accesos fijos reales de operadores distintos, porque el cambio entre accesos solo se demuestra con operadores reales | 4.2.6 (~línea 855) |

Para ubicar cada cambio con exactitud: `git diff` del `.tex` contra la rama base.

## C. Supuestos nuevos que el texto debe reflejar si los nombra

- S-24: VM de la serie Ddsv5 (D2ds, D4ds, D8ds y D16ds v5; relación 1 vCPU por 4 GiB).
- S-25: Brazil South con réplicas PostgreSQL sin alta disponibilidad; se promueve la réplica y luego se activa la alta disponibilidad en la misma zona. El tiempo de activación suma al RTO.
- S-26: Azure Managed Redis Balanced B20, 24 GB.
- S-27: Bastion Premium con IP pública y zonas (zonas en vista previa).
- S-28: agentes efímeros en VMSS; la creación del pool usa una clave de service principal.
- Sentinel opera en Brazil South (no está en Chile Central).
- API Center solo en East US.
- Detalle y evidencia: `06_supuestos-pendientes.md`.

## D. Formularios por conciliar con el retiro de ExpressRoute (no editar aquí)

| Formulario | Dónde aparece | Qué conciliar |
| :--- | :--- | :--- |
| T-11 | Filas 1.19 y 6.6 y texto de T-11.6 («ExpressRoute, alternativa adicional») | Retirar la alternativa; la VPN es la conexión de DC-01. Hay copia local divergente en `sd-04/OSS-Formulario-T-11.tex`: no elegir por nombre o fecha |
| T-12 | Respuesta de un RT-03 («enlace privado dedicado (Azure ExpressRoute) para DC-01») y la lista de ocho puntos únicos de falla | Responder con VPN IPsec (RT-03.21 la admite) y renombrar el punto único de falla como «conexión de DC-01» |
| T-16 | R-32: «acreditar el ExpressRoute antes del diseño final» | Reformular o retirar; ver sesión de riesgos |

Figuras recibidas (`figuras/recepcion-20261025/`) que podrían mostrar ExpressRoute: no revisadas. Revisar cuando se corrijan las figuras (hay pendiente una sesión paralela de diagramas).

## E. Riesgos

No se tocan aquí. Su traspaso está en `10_riesgos-para-sd-08.md`, sección F.

## F. Pendientes de información que el texto debe declarar como pendiente

- Lockers (S-30), Retail Media Network (S-31) y fila virtual (S-32): ya son supuestos con referencia (Cleveron 355, Criteo, prueba en el corte de 24 h); `.tex` 4.1.7 dice «contrato de la contraparte por cerrar»: coherente.
- Vista logística (S-29): WMS en CD-01 por adaptador; CD-02 sin WMS.
- Comercio electrónico de 2019: se supone externo (el Caso no dice dónde reside); no escribir «contrato externo».
- Control regulatorio (F:C-04): sin despliegue; declarar pendiente explícito.
- Capacidades comunes (administración, flujos, documentos, notificaciones): producto pendiente.
- Informe interno 2024 de DC-01 (el Cliente lo entregará): lo dicho sobre el recinto es supuesto hasta recibirlo (S-07; riesgo R-FIS-01).
- Pruebas de latencia y capacidad (S-05, S-17, S-18, P-02): se miden en la Etapa 1.
- H-24 (Power BI en Chile Central): reabierto; ver S-23.

## G. Verificación al terminar de redactar

- `python3 05_Gestion/scripts/exportar_latex.py verificar`
- `python3 05_Gestion/scripts/exportar_latex.py verificar-redaccion --parte T7-04` (estado al 06-11-2026: 0 errores y 0 avisos)
- Reglas: `05_Gestion/convenciones/reglas-redaccion.md`.
- Citas: skill `citas-proyecto`.

## H. Revisión de redacción previa (rama remota `codex/revision-redaccion-sd04`)

Documento: `80_Artefactos/sd-04_contexto/revision-redaccion-figuras-2026-10-23.md` (solo en esa rama remota; léelo con `git show origin/codex/revision-redaccion-sd04:80_Artefactos/sd-04_contexto/revision-redaccion-figuras-2026-10-23.md`). Revisa el `.tex` del 23-10, no el vigente; sus números de línea ya no coinciden. Estado: hallazgos para revisión humana.

Contiene E-01 a E-10 (errores comprobables), D-01 a D-09 (decisiones con tres alternativas) y L-01 a L-08 (legibilidad para lector no técnico), más un patrón de tres frases para las figuras (antes, después, cierre).

Cruce con lo hecho en esta sesión (a confirmar al redactar, no está verificado punto por punto):
- Parecen resueltos en el `.tex` vigente: D-01 (la Tabla 4.22 separa proponente y Cliente), D-05 (Crédito 2011 «como supuesto que el levantamiento confirma»), D-06 (observabilidad de X-01 en sus seis nodos) y D-09 (Tabla 4.4: diez microservicios, dos módulos, uno abierto).
- Siguen abiertos o sin comprobar: D-02 (recuperación de mensajes de Service Bus), D-03 (API Management en Brasil), D-04 (OpenSearch de la Filial), D-07 (plano anexo), D-08 (residencia y norma sin fuente primaria) y E-01 (Event Hubs frente a Service Bus en T-11 y SD-05).
- Los datos de esta sesión que alimentan esas decisiones están en `06_supuestos-pendientes.md` (S-25 Brazil South, S-15 API Center en East US) y en `03_ambientes.md`.
