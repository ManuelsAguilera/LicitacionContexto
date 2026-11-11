# Informe de cotejo del SD-04 (Fase 1)

**Fecha:** 2026-11-06. **Estado:** borrador para decisión del usuario. Sin revisión humana. No se editó ningún `.tex`, formulario ni archivo del registro.

**Líneas:** las de `L###` corresponden a `02_Propuesta/latex_final/sd-04/OnlySimpleSolutions-Subdocumento4.tex` a esta fecha. Se mueven al editar.

## 1. Alcance, criterio y cobertura

### 1.1 Criterio aprobado por el usuario

**Propósito.** 4.2 y 4.3 responden «¿dónde se ejecuta cada cosa y sobre qué?» (FEP01·74). 4.1 cubre módulos, interfaces y flujo, independiente del proveedor (FEP01·17). Las clases sirven de criterio; si contradicen las Bases o el Comunicado 10, mandan estos.

**Incluye.** Nodos, ubicación, artefactos, capacidad, conexiones y redundancia. Mapeo al 100 % con la lógica. Emplazamiento justificado por componente (Art. 16). Servicios de nube con producto. Ambientes, redes segmentadas, alta disponibilidad, recuperación y respaldos. Dimensionamiento con cifras derivadas. Frontera entre proponente, Cliente y terceros. 4.2.1 como resumen y análisis, con totales. 4.3 con proveedor, región, zonas, sitio on-premise, replicación, RPO, RTO y conmutación. Supuestos declarados.

**Excluye.** Riesgos (R-NN, O-NN, probabilidad, impacto, estrategia, responsable, residual, remisiones a T-16 o SD-08). Cifras de costo. Hardware fila por fila (T-11). Modelo de datos (Capítulo 5). EDT, plazos y esfuerzo (SD-07). IDs internos y bitácora.

**Casos límite.**
- Fallas sí, riesgos no: puntos de falla, contingencia y amenazas de RT-07.02 se conservan como hecho técnico.
- Sala DC-01: parámetros con unidad solo para lo que provee el proponente. La falta de parámetros del recinto del Cliente (FEP05·77) no es hallazgo.
- Puertos: solo entrada pública, túnel VPN y cruce por Control de cruces. VLAN y OSI fuera.
- 4.1 se coteja con su propio rol.

**Tipos de hallazgo.** (a) elemento del catálogo ausente. (b) afirmación sin respaldo o contradicha. (c) cifra que no coincide. (d) contenido fuera de propósito.

**Gravedad.** `Bases` = incumple o arriesga una exigencia de Bases, Caso o Comunicado. `Contradicción` = dos fuentes vigentes dicen cosas distintas. `Omisión` = falta contenido esperado. `Detalle` = ajuste menor.

### 1.2 Cobertura real de lectura

| Fuente | Lectura real |
| :--- | :--- |
| `.tex` del SD-04, líneas 89 a 1126 | Completa, salvo figuras. **Las 28 figuras no se abrieron** |
| Registro `00` §9 a §13, `01`, `02`, `03`, `04`, `05`, `06`, `08`, `09`, `11` | Completa. `00` §0 a §3: no leído |
| `07_costos-interno.md` | Solo búsqueda de montos con marca de moneda: 0 resultados. El `.tex` no tiene marcas de moneda. **Comparación valor por valor: no hecha** |
| `10_riesgos-para-sd-08.md` | No leído, por criterio |
| `gigante/` y `gigante-fisico/` | Solo el encabezado de `lineas-omitidas.md`. **No cotejados línea a línea** |
| SD-03 y SD-13 | Cuerpo completo; figuras no abiertas |
| SD-05, anexos y SD-07 | Por términos; solo pasajes con coincidencia |
| T-11 (recibida y `sd-04/OSS-`) | **Por términos y estructura, no completas.** El plan decía completas: desviación declarada. La divergencia se midió en 353 líneas de `diff` |
| T-12 | Filas de RT-02.11, 03.10, 03.13, 03.16, 03.17, 03.21, 03.24, 06.01, 06.07, 07.01 a 07.04 |
| T-14 | Rama 1.4 y términos |
| T-9, T-10, T-19, T-22 | Solo términos. Sin contradicción encontrada no significa sin contradicción |
| Bases, Caso, Comunicado 10 | Consulta puntual. **Folios no verificados en PDF** en este informe |
| Rama `codex/revision-redaccion-sd04` | Filas REV-E-01, REV-D-02, 03, 04, 07, 08 (extracto) |

**Línea base.** `verificar-redaccion --parte T7-04`: 0 errores, 0 avisos. `verificar`: T7-04 ok.

## 2. Resumen por subsección

Orden de redacción: 4.3, 4.2, 4.1. Columnas a/b/c/d = número de hallazgos con esa subsección como sede. Los hallazgos globales (C-086) y de transversales no se cuentan aquí.

| Subsección | a | b | c | d | Sugerencia | Por qué | Decisión del usuario |
| :--- | ---: | ---: | ---: | ---: | :--- | :--- | :--- |
| 4.3 intro | 0 | 0 | 0 | 0 | Conservar | Cumple el Comunicado | |
| 4.3.1 | 0 | 2 | 0 | 0 | Ajustar. **Ciclo hecho el 06-11, ver bitácora** | Tipología y Concepción; recibe el detalle de H-16 | |
| 4.3.2 | 2 | 1 | 1 | 0 | Ajustar | Service Bus depende de tu decisión; faltan reconexión y grupo elástico | |
| 4.3.2.1 | 1 | 1 | 0 | 1 | Ajustar | Norma sin cita | |
| 4.3.2.2 | 1 | 1 | 0 | 0 | Ajustar | Art. 16.3 y pasos omitidos | |
| 4.2 intro | 1 | 1 | 0 | 0 | Ajustar | Acotado | |
| 4.2.1 | 4 | 3 | 2 | 2 | **Reescribir** | Duplicación, responsabilidades, nivel de detalle | |
| 4.2.2 | 3 | 0 | 0 | 0 | **Reescribir** | Art. 16.2 no se responde (observación grave) | |
| 4.2.3 | 3 | 1 | 0 | 0 | Ajustar | Faltan servicios en la tabla | |
| 4.2.4 | 1 | 1 | 0 | 0 | Ajustar | Puertos críticos y Private Link Service | |
| 4.2.5 | 1 | 1 | 0 | 1 | Ajustar | Acotado | |
| 4.2.6 | 4 | 1 | 1 | 0 | **Reescribir** parcial | Puntos únicos, tiempo de conmutación, CD 4 h | |
| 4.2.7 | 1 | 0 | 0 | 0 | Ajustar | Mapeo no llega al 100 % ni a 3.3 | |
| 4.2.8 | 3 | 0 | 1 | 0 | Ajustar | Falta cadena demanda a recurso y latencias | |
| 4.1.1 | 0 | 3 | 3 | 0 | Ajustar | Datos ya verificados no reflejados | |
| 4.1.2 | 0 | 1 | 0 | 0 | Ajustar o reescribir tabla | 31 frente a 25 actores | |
| 4.1.3 | 0 | 1 | 0 | 0 | Ajustar | Tenants | |
| 4.1.4 | 0 | 1 | 0 | 0 | Ajustar | Depende de C-010 | |
| 4.1.5 | 0 | 0 | 0 | 0 | Conservar | Sin hallazgos | |
| 4.1.6 | 0 | 0 | 0 | 0 | Conservar | Sin hallazgos | |
| 4.1.7 | 1 | 0 | 0 | 0 | Conservar | Detalle opcional | |
| 4.1.8 | 0 | 0 | 0 | 0 | Conservar | Solo nombres | |
| 4.1.9 | 0 | 0 | 0 | 0 | Conservar | Solo nombres | |
| 4.1.10 | 0 | 0 | 0 | 1 | Conservar | Remisión adelantada | |
| 4.1.11 | 0 | 0 | 0 | 0 | Conservar | RT-02.03 la exige | |
| 4.1.12 | 1 | 0 | 0 | 1 | Conservar | Detalles | |
| 4.1.13 | 0 | 0 | 0 | 0 | Conservar | Sin hallazgos propios | |
| 4.1.14 | 0 | 0 | 0 | 1 | Conservar | Detalle | |
| 4.1.15 | 1 | 0 | 0 | 0 | Ajustar | Figura sin explicación | |
| 4.1.16 | 0 | 1 | 0 | 0 | Ajustar | ADR-09 | |
| Introducción del capítulo | 0 | 0 | 0 | 1 | Ajustar | Remisión a SD-08 | |

**Lo primero que conviene decidir:** C-033 (Art. 16.2), C-049 (RT-02.11), C-050 (24 h en centros), C-083 (Art. 16.3), C-087 a C-090 (Art. 16.3 y 16.4) y C-073 (Service Bus). Las Bases califican como observación grave C-033, C-049 y la declaración de funciones no disponibles (RT-03.13).

## 3. Hallazgos por subsección

Columnas: ID · tipo · línea · hallazgo · evidencia · gravedad · acción propuesta.

### Introducción del capítulo

| ID | T | L | Hallazgo | Evidencia | Gravedad | Acción |
| :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| C-001 | d | 95 | «los riesgos en SD-08» | Criterio aprobado: sin remisiones | Detalle | Quitar el inciso |

### 4.3 Data center

**4.3 intro (L975-997): sin hallazgos.** Las amenazas de L981 son hecho técnico exigido por RT-07.02.

**4.3.1**

| ID | T | L | Hallazgo | Evidencia | Gravedad | Acción |
| :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| C-068 | b | 1047, 1045 | Adopta «sala técnica principal» y dice que allí no se instalan máquinas de negocio ni bases financieras | Transversales §6.1: esa tipología aplica cuando el caso requiere cómputo sustantivo en instalaciones del Cliente. S-07 la adopta | Contradicción | Mantener por S-07 y explicar por qué aplica, o revisar la tipología. Decisión tuya |
| C-070 | b | 1049, 677 | Instala en CD-02 un par local de captura, racks y router | SD-03 SP-02: Concepción «se mantiene como está durante el contrato»; SD-03 L451 sigue en planillas; S-29 y `01` sí prevén el par | Contradicción | Decidir. SD-03 no se edita desde aquí |

C-023 (H-16) deja el detalle del recinto en esta subsección. Por criterio, los parámetros ausentes del recinto del Cliente no son hallazgo.

**4.3.2**

| ID | T | L | Hallazgo | Evidencia | Gravedad | Acción |
| :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| C-073 | b | 1078, 1087-1093; 160, 598, 718, 895, 922 | El `.tex` no usa geo-replicación de Service Bus: republica desde registros durables | Contra: `01`:169, E-55, `03`:24, §9.1, `06`:112. A favor: H-07, `04`:46 y :80, T-11 recibida 1.3 | Contradicción | Ver sección 8. Sugiero conservar el `.tex` y corregir el catálogo |
| C-074 | a | 991, 1069 | No dice que tiendas y centros reconectan al VPN Gateway de Brazil South. «reconect»: 0 casos en el cuerpo | E-58, H-25, `01`:164, `03`:37 | Omisión | Agregar. Afecta la promesa de RTO |
| C-075 | a | 1067 | No declara el grupo elástico de 0 a 3 nodos en Brasil, encendido tras estabilizar | H-15 («la redacción debe declararlo»), `01`:177 | Detalle | Agregar una frase |
| C-076 | c | 1069 frente a 809 | «La región del enlace privado se confirma» frente a Brazil South y East US ya adoptadas | S-03, D-FIS-15 | Detalle | Unificar |

**4.3.2.1**

| ID | T | L | Hallazgo | Evidencia | Gravedad | Acción |
| :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| C-079 | b | 1109, 1103 | Afirma qué admite la norma de externalización, sin cita. Cita Resolución Exenta RAEX202503748 sin entrada en catálogo, Caso ni Bases | REV-D-08 abierto. SD-03 L633 cita RAN 20-7 solo como consulta pública «no vigente» | Contradicción | Verificar fuente primaria o declarar como supuesto |
| C-080 | d | 1109 | «la matriz de riesgos que el informe necesita» | Criterio aprobado | Detalle | Reformular como «análisis técnico» |
| C-081 | a | 1107 | No declara la alternativa si el Cliente no aprueba Sentinel (SIEM propio en Chile) | S-19, `01`:113 | Omisión | Agregar |

**4.3.2.2**

| ID | T | L | Hallazgo | Evidencia | Gravedad | Acción |
| :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| C-083 | b | 1117 | Tras conmutar, PostgreSQL opera con alta disponibilidad en una zona. Bastion existe en Brazil South (disponible, verificado en el buscador de productos y en `01`) pero sin zonas; el `.tex` no lo dice | Art. 16.3: «multi-zona de disponibilidad para todos los componentes con requisito de alta disponibilidad; el diseño en una sola zona no será aceptado». S-25, S-27, `04`:53, :96. Una excepción declarada no la hace aceptable | Bases | **Decisión abierta.** Ver sección 10, punto 2 |
| C-084 | a | 1117 | Omite: declaración con dos sondas y verificación humana, aislamiento de Chile antes de promover, tráfico gradual, bloqueo de nueva emisión de autorizaciones | `04`:77, :80, :82, :85 | Omisión | Agregar. El aislamiento evita dos autoridades |

### 4.2 Arquitectura física

**4.2 intro**

| ID | T | L | Hallazgo | Evidencia | Gravedad | Acción |
| :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| C-021 | b | 645, 876 | DC-01 «dos accesos de operador» como hecho | Caso cap. 6 no lo dice. `01`:193 y E-12: «cuando el sitio sea crítico» | Contradicción | Marcar como propuesta, como CD-02 |
| C-022 | a | 647-648 | Tabla 4.13 omite en Brasil los VPN Gateway, firewalls y redes | `01` bloque 4, H-25 | Detalle | Completar o remitir |

**4.2.1**

| ID | T | L | Hallazgo | Evidencia | Gravedad | Acción |
| :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| C-023 | b | 677, 679 frente a 1045, 1049 | H-16 y H-16b siguen abiertos. Figuras 4.25 y 4.26 citadas antes de su sección | `11` A; Comunicado: cita antes y explica después | Detalle | Equipamiento aquí, recinto y enlace en 4.3.1 |
| C-024 | d | 659 | VLAN numeradas (10 a 70) | Criterio aprobado | Detalle | Describir segmentos sin números |
| C-025 | d | 669 | Detalle de energía y cableado (2,57 kW, 3,341 kW, 20 kVA, clima 5 kW, categoría 6 LSZH, OS2, 90 m). No están en `01` a `06`; origen en `cierre-inventario/11-soporte-fisico.md` | Comunicado 4.2.1: resumen, detalle en T-11. Regla: registrar antes | Omisión | Pasar al registro y resumir |
| C-026 | c | 669, 692 | UPS «6 kW» frente a «2 × 6 kVA; 30 min a 6 kW» | `01`:28. T-11 5.4 dice 6 kW | Detalle | Unificar unidad |
| C-027 | a | 657-669, 689 | Falta la copia local cifrada de la tienda. Solo aparece respaldo local en DC-01 | `01`:30, `04`:34; FEP01·117: RAID no es respaldo | Omisión | Agregar |
| C-028 | b | 655, 689, 692 | Tabla 4.22: el proponente provee servidores, árbitros, racks, UPS y PDU de tienda | SD-03 L140, L311, SP-04: la compañía adquiere el equipamiento de tiendas. T-11 recibida T-11.4 sigue a 4.22 | Contradicción | Decidir. Ver sección 6 |
| C-029 | b | 695 | DC-01: el Cliente compra e instala equipos de red y ejecuta cableado | RT-06.33 (Transversales): el proponente provee conectividad, seguridad y canalizaciones del recinto. Caso cap. 11: el Cliente adquiere el «equipamiento de red» y ejecuta canalizaciones y cableado. El Caso no puede rebajar un obligatorio (precedencia). SD-03 L311 | Contradicción | Corregir la fila: el proponente provee y configura los equipos de conectividad y seguridad del recinto; el Cliente ejecuta la obra civil y el cableado |
| C-030 | c | 679, 936 | Dos pares de integración como firmes | `01`:197-198: Retail condicional, Filial transitorio. `01` pendiente 1b; S-16 | Detalle | Declarar la condición |
| C-088 | a | 657 | No declara el nivel RAID ni lo justifica frente a alternativas (0 casos de «RAID»; solo «discos espejados») | RT-03.14 y Art. 16.4: «declarando el nivel RAID y su justificación». FEP01·116 y 117 | Bases | Declarar RAID 1 en discos de la tienda y justificarlo |
| C-090 | a | 657-669 | No declara endurecimiento CIS ni gestión centralizada de parches de los sistemas on-premise (0 casos) | RT-03.15 y Art. 16.4. RT-03.18: administración remota de dispositivos (Intune aparece solo en la tabla de seguridad) | Bases | Declarar, con ventana de parches acordada con el Cliente |
| C-032 | a | 699 | Cita `adj-sd-04_s2_inventario-hardware.xlsx`. No se encontró en el repositorio | Búsqueda por nombre | Omisión | Crear el adjunto o quitar la cita |

**4.2.2**

| ID | T | L | Hallazgo | Evidencia | Gravedad | Acción |
| :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| C-033 | a | 713-725 | Tabla 4.14 no justifica por componente los seis factores: latencia, criticidad, volumen, regulación, conectividad y costo total. No hay argumento de costo | Art. 16.2: «observación grave». `01` ya tiene las seis columnas; §13 las asigna a 4.2.2 | Bases | Reescribir con los seis factores, por grupos. El detalle puede ir en anexo |
| C-087 | a | 1047, 657, 677, 701-745 | Solo DC-01 declara tipología («sala técnica principal»). Tienda, centros de distribución y DC-02 no la declaran | Transversales §6.1: «declarar expresamente qué tipología adopta en cada sitio» y justificar el dimensionamiento. Caso RT-06.01: «gabinete por tienda» | Bases | Declarar tipología por sitio en 4.2.2 |
| C-034 | a | 703 | «Dos hechos» como supuestos. No declara variantes P-01 (mall, insignia, Coyhaique), S-13, S-16, S-17, S-18, S-24, S-26 a S-32 | §13: los supuestos van declarados | Omisión | Tabla de supuestos que afectan el emplazamiento |

**4.2.3**

| ID | T | L | Hallazgo | Evidencia | Gravedad | Acción |
| :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| C-036 | a | 761-766 | La tabla omite DDoS Protection (0 casos en todo el `.tex`), External ID, Intune, Entra Private Access y Workload Identity | Comunicado: «todos los servicios». `01`:115, S-12, T-11 1.29 | Bases | Completar |
| C-089 | a | 749-769 | Sin FinOps (presupuestos, alertas de desviación, reporte mensual; el etiquetado sí está, L753) y sin estrategia de reversibilidad y de mitigación del bloqueo por proveedor (0 casos en el cuerpo; sí en T-11.12). La justificación de servicios autoadministrados (OpenSearch, OpenMetadata, Grafana) está solo en 4.1.1 | Art. 16.3, viñetas FinOps, servicios administrados y reversibilidad | Bases | Agregar en 4.2.3, con remisión a T-11.12 |
| C-037 | b | 761 | Application Gateway como «la puerta privada» | H-17: revisar. Glosario: «la puerta de cada negocio» | Detalle | Cambiar |
| C-038 | a | 769, 923 | No nombra Ddsv5, Redis B20 de 24 GB ni Bastion con zonas en vista previa. `06`:91 afirma que el `.tex` declara la vista previa: **0 casos** | S-24, S-26, S-27 | Omisión | Declarar y corregir `06` |

**4.2.4**

| ID | T | L | Hallazgo | Evidencia | Gravedad | Acción |
| :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| C-040 | a | 781, 809, 819 | Sin protocolo y puerto en enlaces críticos (HTTPS 443; IPsec/IKE UDP 500 y 4500; cruce HTTPS privado). 0 casos de puertos | Criterio aprobado; E-02, E-09, E-22 | Detalle | Agregar solo esos tres |
| C-042 | b | 819 | «Private Link Service o proxy, según prueba» | S-11: PLS adoptado; proxy solo si falla | Detalle | Precisar |

**4.2.5**

| ID | T | L | Hallazgo | Evidencia | Gravedad | Acción |
| :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| C-045 | d | 843 | Marcha blanca y ventanas de congelamiento | Pertenece a plan (SD-07) | Detalle | Quitar o remitir |
| C-046 | a | 841 | No declara el supuesto de tamaño de ambientes inferiores | S-05 | Omisión | Agregar |
| C-048 | b | 831 | «sin credenciales permanentes» es absoluto | S-28: la conexión que crea el grupo de agentes usa clave de service principal | Detalle | Matizar |

**4.2.6**

| ID | T | L | Hallazgo | Evidencia | Gravedad | Acción |
| :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| C-049 | a | 867-884 | No declara «puntos únicos de falla» que subsisten ni por qué son aceptables (0 casos). Sin dependencias globales (Front Door, Entra ID, DNS, CI/CD) | RT-02.11: «observación grave». `04`:103. T-12 dice 8 puntos; Tabla 4.18 tiene 11 | Bases | Declarar y justificar |
| C-051 | a | 873, 855 | No declara tiempo de conmutación entre enlaces (0 casos) | RT-03.17: «tiempo de conmutación declarado» | Bases | Declarar, con supuesto si no hay medición |
| C-050 | b | 884 | Centro principal con «al menos cuatro horas» | Art. 16.4 (Administrativas): autonomía «en ningún caso inferior a 24 horas continuas». RT-03.10: 24 h «o el mayor que fije el caso»; el 4 h del Caso no puede rebajar. El propio texto aplica 24 h a tiendas. `01`:200, `04`:64. T-12 lo marca «por alinear» | Bases | Declarar 24 h con ensayo particular de 4 h |
| C-053 | c | 902, 765, 1033 | Managed HSM condicionado «a que la región lo admita» | S-20: Chile Central y Brazil South admisibles; queda el censo y la capacidad | Detalle | Precisar |
| C-054 | a | 868-882 | Sin fila: Front Door, punto privado, Application Gateway, API Management, Firewall, VPN Gateway, Bastion, Entra (cuentas de emergencia: 0 casos), Key Vault, Redis, UPS, árbitro, grupo de estado | `04`; FEP01·117 punto 9 | Omisión | Ampliar por grupos |
| C-056 | a | 902, 884 | No distingue copia de Data Lake (Data Factory o AzCopy) de objetos. 4.2.6 no explica la copia local de Control de cruces | S-21; H-09 | Detalle | Agregar |

**4.2.7**

| ID | T | L | Hallazgo | Evidencia | Gravedad | Acción |
| :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| C-058 | a | 913-939 | Tabla sin columnas de esquema (3.3) y lógica (4.1). Sin fila propia: DNS, API Center, Power BI, Data Factory, plataformas conservadas y externas, capacidades comunes, F:C-04, vista logística | Comunicado: mapeo al 100 % y tabla 3.3, 4.1, 4.2 (sugerida). §9.1 | Bases | Reestructurar con §9.1 |

**4.2.8**

| ID | T | L | Hallazgo | Evidencia | Gravedad | Acción |
| :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| C-061 | a | 945-973 | Sin objetivos de latencia (≤10, ≤5, ≤100, ≤200 y ≤150 ms) ni tiempos de respuesta | P-02; FEP01·5 y 273 (CE 1.2) | Omisión | Agregar con su origen |
| C-062 | a | 971 | No muestra la cadena de la carga al recurso: fórmula de nodos con 0,70 y 2/3, pods, autoescalado. Remite al diseño detallado | `05` §2; §13 («copia el cálculo»); FEP01·86, 116 | Omisión | Copiar el cálculo. Explica de dónde salen 40 nodos |
| C-063 | a | 971 | No declara retención ni volumen de registros | S-17, S-18 | Detalle | Agregar |
| C-064 | c | 958, 967 | 6.667 entregas por segundo frente a Service Bus diseñado a 560 por segundo. 6.667 no figura en SD-05, aunque L945 dice usar las mismas cifras | `01`:87, `05`:40 | Contradicción | Ver sección 8 |

### 4.1 Arquitectura lógica

| ID | Sub | T | L | Hallazgo | Evidencia | Gravedad | Acción |
| :--- | :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| C-002 | 4.1.1 | c | 127 | «La documentación consultada no confirma» API Management Premium clásico en las regiones | `06`:113, :122, :130: verificado | Contradicción | Actualizar |
| C-003 | 4.1.1 | c | 144 | Redis: «verificar disponibilidad y nivel» | S-26, `06`:139 | Detalle | Actualizar |
| C-004 | 4.1.1 | c | 149 | Managed HSM: «disponibilidad en la región» | S-20 | Detalle | Actualizar con C-053 |
| C-005 | 4.1.1 | b | 140, 809, 925 | «Un perfil por frente» de Front Door. X-01 no tiene entrada pública: serían dos | `01`:53: uno con políticas. T-11 recibida 1.14: dos perfiles | Contradicción | Ver sección 8 |
| C-006 | 4.1.1 | b | 152 | Canal CI/CD sin producto | L766; S-04, S-28 | Detalle | Nombrar Azure Pipelines |
| C-007 | 4.1.1 | b | 153 | Motor local «Valkey u otro, por decidir» | SD-05 L355: PostgreSQL local | Contradicción | Decidir |
| C-008 | 4.1.2 | b | 168-188 | 31 actores, con fuente «análisis de actores del SD-07» | SD-07 y T-15: 0 casos de actores, UAW o AH-. Nota de memoria del 24-10: el diagrama de contexto fija 25 actores (14 personas y 11 sistemas) | Contradicción | Decidir antes de redactar 4.1. La memoria no es fuente del catálogo: conviene registrarla |
| C-009 | 4.1.3 | b | 198 | Los negocios «no comparten inquilinos de identidad (tenants)» | S-13: un solo tenant, separado por permisos. `01`:106 | Contradicción | Corregir |
| C-010 | 4.1.4 | b | 214, 600 | Recorrido privado directo a API Management | H-17 dice que pasa por Application Gateway | Contradicción | Ver sección 8 |
| C-011 | 4.1.7 | a | 347, 350 | Sin referencias Cleveron 355 ni Criteo | S-30, S-31, SD-13, T-11 | Detalle | Opcional: basta remitir a T-11 |
| C-013 | 4.1.10 | d | 492 | Explica un rótulo de la Figura 4.21, de 4.3.1 | Propósito de 4.1 | Detalle | Mover a 4.3.1 |
| C-014 | 4.1.12 | d | 514 | Calendario del piloto | SD-07; SD-03 también lo cita | Detalle | Conservar breve |
| C-015 | 4.1.12 | a | 506 | La fila virtual local no figura en la continuidad | S-32, L934 | Detalle | Agregar |
| C-016 | 4.1.14 | d | 563 | Nodos y volúmenes de X-01 | Duplica L1009, L1033 | Detalle | Mover a física |
| C-017 | 4.1.15 | a | 573-581 | Figura 4.11 sin explicación posterior | Comunicado: toda figura se explica después | Omisión | Agregar |
| C-018 | 4.1.16 | b | 601 | ADR-09 no recoge la condición de Power BI | `11` B dice que sí; S-23 | Detalle | Agregar |

### Global

| ID | T | L | Hallazgo | Evidencia | Gravedad | Acción |
| :--- | :--- | ---: | :--- | :--- | :--- | :--- |
| C-086 | b | Todo | Nombres contra glosario 08 en el cuerpo: X-01 (94 casos), siglas de sitio (130), hub (11), Emisor (12), máquinas auxiliares (6), SHIR (3), pg-* (2), lago de datos (2) | 08, regla 1: siglas nunca. SD-03 usa X-01 y no usa SIT-01 | Contradicción | Decidir: aplicar el glosario completo o conservar los códigos del SD-03 con su nombre legible en la primera mención |

## 4. Cifras

| Cifra | Fuente | `.tex` | Resultado |
| :--- | :--- | :--- | :--- |
| 22 tiendas (14 + 8) | Caso cap. 2 y 6 | L630 | Coincide |
| 88 / 44 / 44 | `01`:40 | L657, L935 | Coincide |
| 40 nodos (17 + 17 + 6); 54 VM (40 + 12 + 2) | `01`, `05` | L941, L1033 | Coincide |
| 50 VM (40 + 8 + 2) más 4 apagadas | `01`:177 | L1067 | Coincide |
| 12 PostgreSQL (6 + 5 + 1); 4.500 GiB (2.250 + 2.150 + 100) | `01`:85 | L921, L941 | Coincide |
| 15 suscripciones; 9 redes; 3 firewalls; 2 VPN | `01` | L751, L926 | Coincide |
| 24 routers | `01`:27 | L651 | Coincide |
| 31 de 72U; 80 de 168U | `01`:29, :195 | L669, L1045 | Coincide |
| RPO 15 min; RTO 4 h; 99,9 %; 99,95 % | RT-07.04, RT-10.01, Transversales | L618, L904, L1047 | Coincide |
| 2,6 mil km | P-02: 2.590 km | L981 | Coincide («unos») |
| 19 capacidades (6 + 13); plataformas 3 + 2 + 3 | Recuento en tablas | L156, L391 | Coincide |
| 2,2; 4,5; 5,8; 693; 13.867; 1.040; 1,6; 1.333; 40,5; 1.135; 4,8; 523,4; 110 | `05`, SD-05 | L953-964 | Coincide (`05` los recalcula) |
| 6.667 por segundo | `05`:21 lo calcula. SD-05: no figura | L958 | No coincide con SD-05 ni con 560/s (C-064) |
| Redis 16 GiB | `01`:89 reserva; S-26 producto 24 GB | L923 | Compatibles; falta el producto (C-038) |
| UPS 6 kW / 6 kVA | `01`:28 | L669 | Unidad difiere (C-026) |
| Centro principal 4 h / 24 h | RT-03.10; `01`:200 | L884 | No coincide (C-050) |
| Puntos de falla 11 / 8 | T-12 RT-02.11 | L871-881 | No coincide (sección 7) |
| Conexiones 64 / 67 | Tu mensaje y `02` | — | `02` tiene 67 IDs. Matriz con 67 |
| §9.1: 40 filas, 79 elementos | §9.1 | — | Suma comprobada |

## 5. Estado del traspaso (`11`)

| Punto | Estado en el `.tex` |
| :--- | :--- |
| A · H-16, H-16b | Abiertos (C-023) |
| B · S-23 | Hecho en L1107. **ADR-09 no** (C-018) |
| B · S-10 | Hecho. El traspaso cita «Tabla 4.21» para CD-02: es la **Tabla 4.13** (L644) |
| B · S-09 | Hecho: 0 casos de ExpressRoute en el `.tex` |
| B · S-01, S-02 | Hechos (L657, L841) |
| C · S-24, S-26, S-27, S-28 | No reflejados (C-038, C-048) |
| C · S-25 | Hecho (L1085, L1117) |
| C · Sentinel, API Center | Hechos (L1107, L235) |
| F · Lockers, Retail Media, fila | Coherente (L347-351) |
| F · Vista logística, comercio electrónico, F:C-04, capacidades comunes | Coherente (L178, L707, L259, L337) |
| F · Informe de 2024 | Declarado (L1037, L1047) |
| F · Latencia y capacidad | Capacidad sí (L971). Latencia no (C-061) |
| H · REV-D-01, D-05, D-06, D-09 | Verificados como resueltos (L685, L679 y L1045, L563 y L1009, L286) |
| H · REV-D-02 | Resuelto en el `.tex`; catálogo sin alinear (C-073) |
| H · REV-D-03 | Resuelto (L123, L894, L925) |
| H · REV-D-04 | Resuelto (L145, L492, L929) |
| H · REV-D-07 | El plano general ya no se promete en 4.2 (L620-628) |
| H · REV-D-08 | **Abierto** (C-079) |
| H · REV-E-01 | Resuelto en `.tex` y T-11 recibida. **Abierto en SD-05, T-11 OSS y T-12** |
| Figuras recibidas con ExpressRoute | **No verificado**: figuras no abiertas |

## 6. Transversales (solo discrepancias)

**SD-03**
- C-028 y C-029: quién provee equipos de tienda y de DC-01.
- C-070: Concepción «se mantiene como está» frente al par local del SD-04.
- Vocabulario: SD-03 usa «ámbito» además de «frente» (L551, L585 y otras).

**SD-13**
- X-S13-1 · L119: un adaptador de integración vincula el controlador de lockers con pedidos. E-32 y L933: conexión directa por contrato autenticado.
- X-S13-2 · L283-285: la fila vive en el componente local. E-64 solo describe tótem a nube. S-32 y L934 sí la ubican en el par local: el catálogo está incompleto.
- X-S13-3 · L275, L291: tótem Zebra KC50 e impresora Epson dentro de la inversión. `01`:32: lo adquiere el Cliente (Art. 14.2).
- X-S13-4 · L191, L199, L207: inferencia y trabajador de representaciones sin lugar físico. Tabla 4.20 L931 solo ubica servicio y base.
- X-S13-5 · L201: remite la capacidad a la «memoria del subdocumento 4». Existe en `04_Adjuntos/tablas/`; **contenido no verificado**.

**SD-05**
- X-S05-1 · L392 y L355: Event Hubs, con retención de 90 días. SD-04 eligió Service Bus (L160). Sigue abierto REV-E-01.
- X-S05-2 · L355: PostgreSQL local en tienda (C-007).
- Cifras cotejadas coinciden, salvo 6.667 (C-064).

**SD-07** (por términos; sin nombres de producto)
- X-S07-1: la tienda de laboratorio (D-FIS-17, L841) no tiene paquete en SD-07 ni T-14.
- X-S07-2: T-14 1.4.13 y L830 «custodia de medios»; el SD-04 no la menciona.
- X-S07-3: L1053 despliegue azul-verde; el SD-04 no lo menciona.
- Fuera de lo anterior, rama 1.4 y hito H3 no contradicen al SD-04.

## 7. Formularios (no editados; cada edición requiere tu autorización)

**T-11 recibida (`Formularios/…T-11.tex`)**
- Filas 1.19 y 6.6: ExpressRoute como alternativa (S-09).
- Fila 1.13: Log Analytics y Sentinel «en CLD-01 y CLD-02», sin separar que Sentinel opera solo en Brazil South (S-19). La fila 3.8 tampoco lo indica.
- Filas 1.4 y 1.6: disponibilidad y nivel «por comprobar» (S-26, `06`).
- Fila 1.26: FortiGate; L156 del SD-04 dice «sin fijar aún fabricantes».
- L339: «testigos». El glosario aprobó «árbitro».
- T-11.4: repuesto de 10 servidores, sin registro en `01`, `05` ni 4.2.1.
- Sin tienda de laboratorio (`03` pendiente 2 pide reflejarla).

**T-11 OSS (`sd-04/OSS-Formulario-T-11.tex`)**: versión anterior y más divergente.
- Fila 1.3 y otras: Event Hubs Premium con geo-replicación y Kafka.
- Filas 1.14, 1.15, 1.22: Front Door, Firewall y registro «compartidos». **Choca con la línea roja.**
- Filas 1.19, 6.6, L409: ExpressRoute como solución base.
- Fila 5.2: firewall Fortinet, mínimo 13 en total y uno por tienda, frente a cuatro por tienda del SD-04 (L659).

**Tercera copia:** `Formularios/…T-11(2).tex`, no versionada, 4 casos de ExpressRoute. Solo se señala.

**T-12**
- RT-02.11: ocho puntos, incluye «ExpressRoute a DC-01» y remite a «Tabla 4.11»; hoy es la 4.18 con 11 puntos.
- RT-03.21: ExpressRoute para DC-01.
- RT-07.03: «geo-replicación de Event Hubs».
- RT-03.10: ya marcada «Parcial», «por alinear» (C-050).
- RT-03.17: responde «Sí» sin tiempo de conmutación (C-051) y solo nombra Coyhaique. CD-02 cumple por camino móvil según S-10.
- RT-07.02: «Parcial», análisis «antes de aprobar el diseño». L981 y L1099 ya lo declaran.

**T-14**: rama 1.4 sin contradicción. Falta paquete de tienda de laboratorio. Fila 1.4.3 «segregación física y lógica»; el Caso pide física o lógica.

**T-9, T-10, T-19, T-22**: sin contradicción por términos. T-19 coincide con S-30. T-22 1-8 confirma una sola alianza con Azure. **Búsqueda por términos, no lectura.**

## 8. Contradicciones del propio catálogo (decidir antes de redactar)

| ID | Tema | Una fuente | Otra fuente | Sugerencia |
| :--- | :--- | :--- | :--- | :--- |
| K-01 | Service Bus en recuperación | Geo-replicación: `01`:169, E-55, `03`:24, §9.1, `06`:112 | Republicación: `.tex`, H-07, `04`:46, :80, decisión del 23-10 | Mantener republicación y corregir el catálogo. Geo-replicación no protege lo no replicado |
| K-02 | Front Door | 1 con políticas: `01`:53 | Dos perfiles: L809, T-11 1.14 | Dos perfiles, por separación de negocios |
| K-03 | Acceso a Bastion | Desde Internet: `01`:62; IP pública: S-27 | Entra Private Access: L781; E-43 no lo nombra | Aclarar la secuencia; ambas pueden convivir |
| K-04 | Recorrido privado | Por Application Gateway: H-17 cita E-04 | Directo a API Management: L214, L600, §9.1. E-04 es el recorrido público | Mantener `.tex` y corregir H-17 |
| K-05 | Carga de Service Bus | 56/s, diseño 560/s: `01`:87, `05`:40 | 6.667/s y 1.135/s: `05`:21-22, L958 | Rehacer con la cifra mayor: 560/s no la cubre |
| K-06 | Enlace de CD-02 | Segundo enlace aceptado o exigido: `01`:201, :210, E-11, `04`:65 | S-10: se propone | Actualizar con S-10 |
| K-07 | Réplicas | «Una por base crítica»: E-54, `01`:86, :182 | Las 12: S-06 | Actualizar con S-06 |
| K-08 | Datos resueltos que siguen pendientes | DNS Resolver, CI/CD, región de E-03b, plataforma publicitaria: `01`:63, :134, :143, :224, E-03b | S-22, S-04, S-03, S-31 | Actualizar |
| K-09 | Encabezado de `01` | «S-01 a S-18», «en construcción» | S-01 a S-32 | Actualizar |
| K-10 | `06`:91 | «El `.tex` declara la vista previa» | 0 casos | Corregir al redactar |

## 9. Anexo: matriz de cobertura

P = presente · Pa = parcial · A = ausente · n/a = no corresponde por criterio. Línea = mejor referencia, no la única.

### 9.1 Elementos lógicos (§9.1: 40 filas, 79 elementos)

| Fila §9.1 | N.º | Estado | Línea o nota |
| :--- | ---: | :--- | :--- |
| web, movil | 2 | P | L204, L916 |
| portal_f, meson_f | 2 | P | L204, L917 |
| pos, local_serv, local_sync, local_data | 4 | P | L506-510, L935 |
| operacion | 1 | Pa | L506; sin fila en 4.20 |
| logistica | 1 | Pa | L178, L677; sin fila en 4.20 |
| cupo_local | 1 | P | L512 |
| dns | 1 | Pa | L224, L761; sin fila en 4.20 |
| aks_r | 1 | P | L916-918 |
| nueve servicios Retail | 9 | P | L269-277, L916 |
| tres servicios Filial | 3 | P | L278-280, L917 |
| x01 | 1 | P | L918, L935 |
| regulatorio | 1 | P | L259, L284: pendiente declarado |
| conteo, training | 2 | P | L919, L930 |
| lockers | 1 | P | L347, L933 |
| busqueda, vector | 2 | P | L931 |
| media | 1 | P | L350, L932 |
| fila | 1 | P | L351, L934 |
| bus_r, bus_e | 2 | Pa | L922; ver K-01 |
| comercio, canales, socios, proy_r | 4 | P | L368, L393, L916 |
| credito, proy_e | 2 | P | L368, L917 |
| datos_merc, historial, datos_venta, datos_clientes | 4 | P | L921, L452 |
| datos_credito | 1 | P | L464, L921 |
| bitacora | 1 | P | L819, L1025 |
| analitica | 1 | P | L476, L921 |
| datos_evid, archivo | 2 | P | L924 |
| lake | 1 | P | L924 |
| redis | 1 | Pa | L923; sin producto |
| powerbi | 1 | Pa | L1107; sin fila en 4.20 |
| adf | 1 | Pa | L764; sin fila en 4.20 |
| metadata, search, mlflow | 3 | P | L929 |
| ext_comercio | 1 | P | L722 |
| ext_canales, ext_socios, ext_credito, ext_comunes | 4 | Pa | L393, L618; sin fila en 4.20 |
| front_door, application_gateway, api_management, private_link | 4 | P | L809, L925 |
| api_center | 1 | Pa | L229, L1107; sin fila en 4.20 |
| entrada_privada | 1 | P | L214, L809 |
| tech_ui, tech_java, tech_spring | 3 | P | L136-137, L573 |
| common_admin, common_flujos, common_docs, common_notif | 4 | Pa | L329-332; sin fila en 4.20 |
| backup | 1 | P | L902, L938 |
| security_summary | 1 | Pa | L927; sin DDoS |
| observability_summary | 1 | P | L928 |
| **Total** | **79** | | |

### 9.2 Nodos físicos (`01`)

| Bloque · nodo | Estado | Línea o nota |
| :--- | :--- | :--- |
| 1 · Servidores de Retail y de la Filial; copia local de Control de cruces; árbitro | P | L657 |
| 1 · Terminales de caja; terminales financieros | Pa | L655, L693 |
| 1 · Firewall y red de tienda; accesos fijos; router 4G/5G | P | L659, L667 |
| 1 · UPS; racks | P | L669 |
| 1 · **Copia local cifrada** | **A** | C-027 |
| 1 · Controlador de lockers | P | L933 |
| 1 · Tótem | Pa | L351 |
| 2 · Front Door; Application Gateway; API Management | P | L809, L925 |
| 2 · Balanceador interno | P | L781 |
| 2 · Redes central, de aplicaciones y de datos | P | L773; nombres (C-086) |
| 2 · Firewall; VPN Gateway; Bastion; DNS Private Resolver | P | L781 |
| 3 · Clústeres; grupo elástico; máquinas de apoyo; sondas | P | L916-920 |
| 3 · 12 PostgreSQL y réplicas | P | L921 |
| 3 · Service Bus ×2; Redis; Data Lake; evidencia y archivo | P | L922-924 |
| 3b · Entra ID; Key Vault; Managed HSM | P | L927 |
| 3b · Conectores de acceso privado | P | L920 |
| 3b · Defender; Log Analytics; Sentinel; pila de observabilidad | P | L150, L928 |
| 3b · **DDoS Protection** | **A** | C-036 |
| 3c · DEV, QA, PRE; Container Registry; pipelines; estado de Terraform | P | L831-841 |
| 3c · Tienda de laboratorio | P | L841 |
| 3c · API Center | P | L235, L1107 |
| 3c · OpenSearch, MLflow, OpenMetadata | P | L929 |
| 3c · Suscripciones y grupos | P | L751 |
| 4 · Clústeres; 8 VM templadas; 4 de BI; sondas | P | L1067 |
| 4 · Redes; Firewall, DNS, Bastion | Pa | L1069 |
| 4 · **VPN Gateway de Brazil South** | **A** | C-074 |
| 4 · Application Gateway; API Management | P | L1069 |
| 4 · Punto privado en Brazil South; segundo en East US | P | L809 |
| 4 · 12 bases; Service Bus | Pa | L1077-1078; K-01 |
| 4 · Data Lake; Redis | Pa | L1079; Redis solo por L923 |
| 4 · Seguridad y registros; registros de imágenes; respaldo | P | L902, L1080-1082 |
| 5 · DC-01; DC-02; recinto técnico | P | L1037-1047 |
| 5 · Redes de DC-01; nodos de integración | P | L1045; condición (C-030) |
| 5 · CD-01; CD-02 y nodos locales | P | L677, L1049 |
| 6 · ERP/DTE; WMS; retail 2009; crédito 2011; comercio, marketplace, fidelización | P | L380-387 |
| 6 · Pagos, firma, proveedores | P | L393 |
| 6 · Plataforma publicitaria | P | L350, L932 |
| 7 · DNS público | P | L761 |
| 7 · Data Factory; bóveda de Chile | P | L764, L902 |
| 7 · Capacidad de Power BI | P | L1107 |
| 7 · External ID; Intune | Pa | L149, L528; no en 4.2.3 |

### 9.3 Conexiones (`02`: 67 IDs)

| E | Estado | Nota |
| :--- | :--- | :--- |
| E-01 | Pa | DNS en L224; sin recorrido |
| E-02 | Pa | L809; sin puerto (C-040) |
| E-03, E-03b, E-04, E-05, E-06, E-07 | P | L781, L809 |
| E-08 | Pa | L781; L916 réplicas |
| E-09, E-10 | Pa | L667, L855; sin puerto |
| E-11, E-12 | P | L809 |
| E-13 | P | L809 |
| E-14 | Pa | L781 |
| E-15, E-16, E-17 | P | L781; L368 |
| E-18, E-19 | Pa | L452 |
| E-20 | Pa | L454 |
| E-21 | Pa | L538 |
| E-22, E-23 | Pa | L819; sin protocolo |
| E-24 | P | L819 |
| E-25, E-27 | P | L508 |
| E-26 | Pa | L657 árbitro; sin copia local |
| E-28 | Pa | L659 |
| E-29, E-30, E-31 | Pa | L657 |
| E-32 | P | L933 |
| E-64 | Pa | L351, L934 |
| E-33 | Pa | L969 |
| E-34 | P | L659 |
| E-35 | Pa | L659 |
| E-36 | Pa | L659 VLAN 70 |
| E-37 | P | L466, L764 |
| E-38, E-39 | Pa | L486, L781 |
| E-40 | P | L393: 14 interfaces por inventariar |
| E-41 | P | L393 |
| E-42 | Pa | L536 |
| E-43, E-44 | P | L781 |
| E-45 | P | L807 |
| E-46, E-47, E-48 | P | L551, L561 |
| E-49 | P | L928 |
| E-49b | P | L1107 |
| E-50 | P | L565 |
| E-51, E-52 | P | L831, L1082 |
| E-53 | P | L831 |
| E-53b | Pa | L235 |
| E-54 | P | L1077 |
| E-55 | Pa | Contradicho (K-01) |
| E-56 | Pa | L1079; S-21 sin detalle |
| E-57 | P | L902, L1105 |
| E-58 | Pa | Front Door sí; sitios no (C-074) |
| E-59 | P | L902 |
| E-60, E-61, E-62, E-63 | P | L669 |

Conteo de IDs de esta tabla: 67.

### 9.4 Supuestos (`06`)

| S | Estado | Nota |
| :--- | :--- | :--- |
| S-01 | P | L657 |
| S-02 | P | L841 |
| S-03 | P | L809 |
| S-04 | P | L766; no en L152 |
| S-05 | A | C-046 |
| S-06 | P | L648 |
| S-07 | P | L1037-1047 |
| S-08 | A | Sin mención de zonas de Application Gateway y Firewall |
| S-09 | P | Retirado: 0 casos, correcto |
| S-10 | P | L644, L855 |
| S-11 | Pa | C-042 |
| S-12 | A | C-036 |
| S-13 | Contradicho | C-009 |
| S-14 | P | L1033 |
| S-15 | P | L235 |
| S-16 | Pa | C-030 |
| S-17 | Pa | Solo seguridad, L928 |
| S-18 | A | C-063 |
| S-19 | P | L1107; sin alternativa (C-081) |
| S-20 | Pa | L1105; C-053 |
| S-21 | Pa | C-056 |
| S-22 | n/a | Producto nombrado, L781; verificación no se declara |
| S-23 | P | L1107 |
| S-24 | A | C-038 |
| S-25 | P | L1085, L1117; C-083 |
| S-26 | A | C-038 |
| S-27 | Pa | Premium en L150; sin zonas (C-038) |
| S-28 | A | C-048 |
| S-29 | P | L178, L677 |
| S-30 | Pa | C-011 |
| S-31 | Pa | C-011 |
| S-32 | Pa | C-015 |

## Bitácora de este informe

- 2026-11-06: creación. Sin cambios en `.tex`, formularios ni registro.

## 10. Decisiones contrastadas con las Bases (2026-11-06)

El usuario aprobó las sugerencias y pidió contrastarlas con las Bases. Resultado: ocho se confirman, dos se corrigen y una queda abierta.

| N.º | Decisión | Contraste con las Bases | Resultado |
| ---: | :--- | :--- | :--- |
| 1 | Service Bus: republicación desde registros, no geo-replicación (C-073) | RT-07.03 pide replicación continua de **datos**, con medición del retraso. Los datos son los registros durables, que viajan con la réplica de PostgreSQL; RT-07.04 fija RTO y RPO | **Confirmada.** Se corrige el catálogo |
| 2 | Alta disponibilidad en una sola zona en Brasil (C-083) | Art. 16.3: «el diseño en una sola zona no será aceptado» para componentes con requisito de alta disponibilidad | **Corregida.** Declararla como excepción temporal no basta. Abierta, ver 10.1 |
| 3 | Equipos de tienda a cargo del proponente (C-028) | Art. 14.2: el proponente provee los «componentes on-premise»; el hardware de terreno lo adquiere el Cliente. Caso cap. 11: Cliente compra terminales, dispositivos de sala, lectores, impresoras y «equipamiento de red y de centro de distribución». Los servidores de tienda no están en esa lista | **Confirmada, con matiz.** La Tabla 4.22 es coherente con Art. 14.2 y Caso en cómputo y red. SD-03 L140 y L311 («la compañía adquiere el equipamiento de las tiendas») es más amplio que el Caso. Se anota el ajuste al SD-03; racks, UPS y PDU quedan como decisión del proponente, no listada por el Caso |
| 4 | Concepción con par local (C-070) | Caso decisión 20: incorporar al WMS, solución propia, o mantener como está; la incorporación «no puede darse por supuesta». Art. 16.4 y RT-03.17: autonomía y enlace redundante aplican al componente on-premise | **Confirmada.** El par es captura local, no WMS. SD-03 L498 ya habla de «registros estructurados». Se anota que SD-03 SP-02 («como está») requiere precisión |
| 5 | 25 actores (C-008) | Las Bases no fijan el número | **Confirmada.** Sin respaldo en Bases; se registra la fuente |
| 6 | Nombres: códigos con nombre legible en la primera mención (C-086) | Sin exigencia de Bases. Comunicado: lector no técnico | **Confirmada** |
| 7 | Motor local de tienda: PostgreSQL (C-007) | RT-03.11 y 03.12: registro local íntegro y sincronización con bitácora. RT-03.14 y Art. 16.4: RAID declarado | **Confirmada.** Obliga a C-088 |
| 8 | Tipología de DC-01: sala técnica principal (C-068) | Transversales §6.1: aplica con «cómputo, almacenamiento y procesamiento sustantivos» del Cliente; sobredimensionar «es tan penalizado como subdimensionar». DC-01 aloja ERP/DTE y núcleo Retail | **Confirmada.** El argumento correcto es la presencia de sistemas conservados, no cómputo nuevo. Obliga a declarar la tipología de los demás sitios (C-087) |
| 9 | Recalcular carga de Service Bus (K-05) | RT-09.01 y RT-09.03 | **Confirmada** |
| 10 | Corregir catálogo K-01 a K-10 | Regla del proyecto: registrar antes de redactar | **Aplicada** (ver bitácora) |
| 11 | Front Door: dos perfiles (K-02) | Art. 16.3 segmentación y línea roja del Caso | **Confirmada** |

### 10.1 Punto abierto: zona única en Brasil (C-083)

Las Bases no aceptan una sola zona para componentes con requisito de alta disponibilidad. Opciones, ninguna verificada:

| Opción | Ventaja | Costo o riesgo |
| :--- | :--- | :--- |
| A. Verificar en la suscripción antes de construir, y mientras tanto declarar el límite de Microsoft y la condición de revisión | Honesta; ya está en L1117 | Sigue siendo una brecha frente al Art. 16.3 si Microsoft mantiene el bloqueo |
| B. Argumentar que la copia de Brasil opera solo en contingencia y que una falla de zona de Brasil coincidente con la caída de Chile Central es un evento doble | Defendible | Las Bases no distinguen estado normal y contingencia |
| C. Evaluar otra región de Brasil o de Sudamérica (por ejemplo Brazil Southeast) con alta disponibilidad entre zonas para PostgreSQL | Cumpliría el Art. 16.3 | No verificado; cambia residencia y catálogo, y exige nueva decisión del Cliente |

**Sugerencia:** A más B en el texto, y C como acción de verificación antes de la Etapa 1. Se necesita tu decisión.
