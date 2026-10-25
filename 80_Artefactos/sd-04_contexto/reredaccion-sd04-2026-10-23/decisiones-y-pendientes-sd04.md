# Decisiones y pendientes del SD-04

**Fecha:** 23-10-2026, noche · **Rama:** `feat/sd-04-fisica-revision` · **Uso de IA:** Alto · **Estado:** registro de trabajo para retomar; sin revisión humana.

Este archivo reúne las decisiones tomadas en la re-redacción del subdocumento 4 y lo que quedó abierto. El resumen de qué está hecho está en `estado-2026-10-23-noche.md` (mismo directorio).

## 1. Decisiones del usuario

| # | Decisión | Efecto en el documento |
| :--- | :--- | :--- |
| D1 | **El inventario físico v4 es la fuente que se mantiene.** Si el texto lo contradice, se reescribe el texto. | Se retiraron FortiGate-VM y Route Server de la nube; ExpressRoute pasó a alternativa adicional para DC-01; la VPN por ámbito es la base. |
| D2 | **Los datos de la filial emisora se recuperan en Brazil South**, para asegurar que queden en una infraestructura segura y asegurada contractualmente y que no se pierdan. | Subsección «Residencia de los datos y recuperación fuera de Chile» (4.3.2) y `justificacion-residencia-filial-brasil.md`. |
| D3 | **Respaldo móvil 4G/5G**: un router celular por tienda y por centro de distribución (24), como tercer camino. | Inventario (C53, SUM-33), figuras y texto. Only Simple Solutions adquiere el router; el Cliente contrata los planes de datos. |
| D4 | **15 suscripciones** de Azure: una por ámbito (R, F, X-01) y por ambiente (DEV, QA, PRE, PRD, DR), sin suscripción compartida. | Inventario § 5 y texto de 4.2. |
| D5 | **Las cantidades de la figura física van en una tabla aparte** en 4.2, no en la figura. | «Sitios, equipos, enlaces y anchos de banda» (Tabla 4.13). |
| D6 | **Se renumeran las figuras** por orden de aparición. | 26 figuras (4.1 a 4.26) y 24 tablas (4.1 a 4.24); archivos `diag-04-NN_*`. |
| D7 | **Formato de 800 px, letra de 15 px o más, alto de una página, una figura por parte** (regla RP-05). | Todas las figuras se rehicieron; la general (F01) sale del cuerpo. |
| D8 | **Los porcentajes de capacidad de los ambientes (15, 25 y 50 %) se retiran**: el inventario no los fija. | El tamaño permanente, las cuotas y los horarios se fijan por suite. |

## 2. Decisiones mías que el usuario aún no ha confirmado

| # | Decisión | Por qué | Cómo revertirla |
| :--- | :--- | :--- | :--- |
| P1 | Las notas de fuente de las figuras dicen «a partir del diseño del proyecto» y no citan el inventario ni la matriz CL. | Son documentos internos, no entregables de la propuesta. | Editar el pie en cada generador y regenerar. |
| P2 | Si el Cliente no aprueba la residencia en Brasil, **no se vuelve a DC-02**; el ámbito queda con una desviación declarada en el T-12 y como riesgo en SD-08, y el Cliente elige entre un sitio propio o de un tercero en otra ciudad de Chile y esperar una segunda región de Azure. | DC-02 incumple RT-07.02; sin sitio aprobado no se cumple RT-07.04. | Cambiar el último párrafo de la subsección de residencia. |
| P3 | La residencia en Brasil se fundamenta para los **tres** ámbitos, no solo la filial. | Retail y X-01 también contienen datos personales (revisión de coherencia, hallazgo 3). | Acotar el párrafo de base legal. |
| P4 | La alternativa «sitio propio o de un tercero en otra ciudad de Chile» se descarta como base y se conserva como respuesta ante la no aprobación. | Obligaría a una segunda plataforma durante 56 meses. | Cambiar el párrafo de alternativas. |
| P5 | La figura general F01 queda **solo como plano de consulta** (`diag-04-anexo-1_plano-fisico-general.*`). | Su ancho impide leerla en página. | Decidir si se crea un anexo del SD-04 o se retira la mención (ver § 3, punto 1). |

## 3. Pendientes

1. **Anexo del plano general.** El texto de 4.2 lo menciona como plano de consulta del anexo, pero el SD-04 no tiene un anexo que lo contenga. Crear el anexo o retirar la mención (recomendado: retirarla).
2. **Exportación de las figuras con draw.io de escritorio.** La vista previa dibuja como cuadrados los íconos Cisco. Instrucción lista en `instruccion-codex-exportacion-iconos.md`.
3. **Hallazgos de la revisión de coherencia (18).** Corregidos: 4 y 5 (remisiones numéricas), 11 (DC-02), 13 (tiendas en centro comercial), 14 (par local de CD-02), y 1, 2, 3 y 18 en parte (subsección de residencia reescrita). Quedan por corregir:
   - **6.** «Por ámbito» frente a «por negocio»: hay dos Service Bus y dos VPN Gateway, no tres. Líneas aproximadas 430, 508, 542, 585, 587, 781 y 831.
   - **7.** La recuperación de los mensajes de Service Bus se remite a 4.3.2 y allí no se define. Declarar una de dos vías: reconstruir los hechos pendientes desde el registro de salida de cada propietario, o un mecanismo geográfico condicionado a su comprobación.
   - **8.** X-01 aparece con pila de observabilidad completa en la capa lógica, pero solo tiene 6 nodos en AKS-X y ninguna VM auxiliar. Aclarar dónde corre su telemetría.
   - **9.** La instancia local de X-01 en tienda (44 instancias, VLAN 23) no tiene antecedente en 4.1. Explicarla en la continuidad local.
   - **10.** API Management en Brasil se describe con dos modelos distintos (una instancia con gateway regional, o una instancia por negocio). Elegir uno y usar la misma redacción en las cuatro ubicaciones.
   - **12.** OpenSearch y OpenMetadata «de Retail y de la filial emisora» contradicen que la filial no tiene búsqueda global.
   - **15.** El grupo elástico de 0 a 3 nodos de Retail no entra en las cifras de 40 y 54 ni se replica en Brasil. Decirlo.
   - **16.** 4.2.1 cita las figuras de DC-01 y de los CD antes que su sección y describe dos veces el recinto. Remitir a 4.3.1 o quitar la duplicación.
   - **17.** El Application Gateway se llama «puerta privada» y la figura de entrada muestra que el recorrido privado no pasa por él.
4. **Verificación de fuentes normativas.** El texto vigente de la norma de externalización de la CMF (se menciona sin nombre ni número) y la fecha de vigencia de la Ley 21.719. La Resolución Exenta RAEX202503748 se verificó solo en fuentes secundarias.
5. **Otros documentos que describen el diseño anterior:** SD-02 Anexos, SD-05, SD-08, T-9, T-12, T-13 y T-22 (Event Hubs, nodo local de dos servidores, DC-02 como respaldo de la filial). El T-22 y el Anexo T-22 citan «Figuras 4.13 y 4.17» con la numeración anterior.
6. **Revisión humana** del capítulo y estado `revisado` (RR-23); solo lo asigna una persona.

## 4. Cómo se trabajó, para repetirlo

- **Reparto:** Claude hizo las figuras de nube y la residencia; Codex, las de tienda, sitios y capas lógicas; subagentes Sonnet terminaron lo que Codex dejó. Protocolo en `coordinacion/README.md`.
- **Etiquetas provisionales:** durante la redacción las figuras se citan con un código (F02a, L03b…) y las tablas nuevas como «Tabla T-nombre»; la numeración definitiva se asigna al final con un script por orden de aparición.
- **Verificación:** `exportar_latex.py verificar` y `verificar-redaccion` con Python 3.12 (`C:\Users\manu\AppData\Local\Programs\Python\Python312\python.exe`), porque el `python` del PATH es el de Inkscape y no tiene `pypdf`.
