# Insumos del SD-07 para el modelo financiero (Informe 3)

Datos que el Excel necesita, conciliados y validados el 2026-11-10 y completados el 2026-11-11 con los parámetros de las Bases, la estimación por casos de uso y los escenarios de atraso. **Versión v3**: traspaso completo del SD-04 (3 frentes, tienda tipo, DC-01, datos, seguridad y recuperación) calculado con el mismo método de HH del SD-07, más la medida preventiva de la capacitación E2 (30 % adelantado a M17) y la programación estabilizada dentro de las holguras (77 actividades desplazadas, sin mover hitos ni el total de HH). Las cantidades salen de aquí; **los precios, tarifas y tasas los decide el equipo en el Excel**. Origen y método: `80_Artefactos/sd-07_contexto/red-v3-2026-11-10/README.md` (y la v2 que la origina).

**Recordatorio del profesor:** el Excel se trabaja sin manejo directo de IA, por personas. Estos archivos son datos de entrada, no celdas del Excel.

**Formato de los CSV:** separados por punto y coma, con coma decimal y UTF-8. Al abrirlos en Excel, usar *Datos → Desde texto/CSV* y elegir el punto y coma como delimitador. M1 empieza el 7 de enero de 2027 y cada mes contractual comienza el día 7.

## Cifras base

| Concepto | Valor |
| :-- | --: |
| HH totales del proyecto | **239.250,01** |
| Trabajo técnico, campo, dirección e inducción (incluye trabajos puntuales durante la operación y la dirección hasta M56) | 89.490,01 |
| Operación M21–M56 (26 personas × 160 HH × 36 meses) | 149.760,00 |
| Contingencia (se valoriza aparte, no es margen) | 3.688 HH |
| Retén M13–M20 (se valoriza por unidad, no por HH) | 1.952 unidades de 12 h |

## Archivos y hoja del Excel que alimentan

| Archivo | Qué contiene | Hoja de la plantilla |
| :-- | :-- | :-- |
| `FTE_matriz_perfiles_E26_M1_M56.csv` | **Personas equivalentes (HH ÷ 160) por perfil del Formulario E-26 y mes: 21 perfiles × 56 meses, con su rango de costo y tarifa (UF/h).** Usar esta para los sueldos | Costos HH - Sueldos, Costos HH por MES, Costos de operación |
| `HH_matriz_perfiles_E26_M1_M56.csv` | Lo mismo en HH | Control de totales |
| `equivalencias_roles_E26.csv` | Cómo se pasó de los 37 roles del plan a los 21 perfiles del E-26, con la regla de cada uno (1 Arquitecto Experto, Líder Funcional y Líder de Calidad separados, desarrollo Senior, 2 «otros roles» declarados) | Hoja de tarifas (respaldo) |
| `HH_paquete_x_perfil_E26.csv` | HH de cada paquete EDT por perfil. Costo de un paquete = sus HH por la tarifa de cada perfil (Art. 57.2) | Costos (trazabilidad) |
| `FTE_matriz_roles_M1_M56.csv` y `HH_matriz_roles_M1_M56.csv` | Las mismas horas con los 37 roles del plan de trabajo (detalle) | Solo de respaldo |
| `HH_por_paquete_EDT.csv` | HH de cada paquete de la EDT (255) con su ventana de meses. Sirve para trazar cada costo a un código EDT (Art. 57.2) y para las HH de las 5 innovaciones (rama 1.10) | Costos (columna de código EDT), Innovaciones |
| `Dotacion_coberturas.csv` | Personas por componente: campo M16 (88 + 88), dirección y PMO, y las 26 personas de operación por rol | Costos de operación |
| `Guardias_mes_rol.csv` | Unidades de disponibilidad del retén por mes y rol | Costos (partida aparte) |
| `Hitos_contractuales.csv` | H1–H12 con su mes contractual, porcentaje de la implementación (E-25), etapa, fecha y entregable | Ingresos |
| `calendario-compras.md` | Mes de compra, entrega e instalación de cada lote (DC-01, lote 1, lote 2, lockers y tótems), plataforma de datos, seguridad, recuperación y nube | Adquisiciones implementación y operación; Hardware del cliente (informativa) |
| `partidas-sd04-sin-precios.md` | Partidas del SD-04 sin precios: equipos por sitio (SUM-01 a SUM-33) y servicios de nube con su unidad de cobro | Adquisiciones (qué cotizar y cómo se cobra) |
| `parametros-bases.md` | E-24 (tipos de cambio, tasas, tope de la línea, financiamiento, IVA), porcentajes del E-25, garantías (Art. 35–37), seguros (Art. 38), notaría (Art. 68.3), custodia de fuentes (Art. 84.6) y licencias (Art. 84.3), verificados en el PDF de las Bases con su folio | Parámetros, Ingresos, Gastos administrativos |
| `ucp_casos_de_uso.csv` | Los 126 casos de uso activos: paquete EDT (1.5.x.y), nombre, transacciones, peso (5, 10 o 15) y HH del paquete del T-14. UUCW = 640 | PCUESFUERZO |
| `ucp_actores.csv` | Los 29 actores con su tipo y peso. UAW = 64 | PCUESFUERZO |
| `ucp_factores.csv` | Los 13 factores técnicos y 8 de ambiente con peso, valor y justificación. Suma técnica 59 (TCF 1,19) y de ambiente 21,5 (EF 0,755). Con 20 HH/UCP y 40 % de programación: UCP 632,5088 y 31.625,44 HH | PCUESFUERZO |
| `escenarios_atraso.csv` | Los 13 escenarios de atraso del SD-07 §7.3.3.2: efecto, respuesta, HH (853 en total) y recargo de horas extraordinarias (unas 147 HH equivalentes). Se pagan con la contingencia de 3.688 HH | Sensibilidad |

## ¿Se puede avanzar solo con esto?

**Sí, en las cantidades y en el calendario. No, en los valores.** Por hoja:

| Hoja | ¿Alcanza con estos insumos? | Lo que falta (lo decide o busca el equipo) |
| :-- | :-- | :-- |
| Parámetros | Parcial | Valores del E-24 en `parametros-bases.md`. Falta la **tasa exigida por los socios** (decisión del equipo) y la tasa ponderada entre deuda y capital propio, antes de impuestos y mensual, menor que 20 % (comunicado §8) |
| Costos HH (sueldos) | **Sí, en cantidades y en perfiles** | **Costo y tarifa de cada uno de los 21 perfiles**, dentro del rango que trae el archivo (E-26). Reemplazar los 32 roles de la plantilla por estos 21. Para la tarifa, considerar horas productivas (clase FEP02, diapositiva 90) |
| Costos de operación | **Sí, en cantidades** | Lo mismo: costo de los 26 roles de operación. Valor de la unidad de retén |
| Ingresos | **Sí, en estructura** | Porcentajes de H1–H12 en `Hitos_contractuales.csv` (verificados en el PDF). El precio total y la mensualidad de operación salen del cálculo |
| Adquisiciones | Parcial | **Precios**: cotizaciones de equipos (tienda tipo × 22 + laboratorio + 2 CD + DC-01) y de nube (calculadora de Azure con las cantidades de `partidas-sd04-sin-precios.md`). Proveedores del Formulario T-22 |
| Gastos administrativos | Parcial | Montos y vigencias de garantías y seguros en `parametros-bases.md`. Falta el **criterio de cálculo de cada uno**: comisión bancaria de las boletas, prima de los seguros, gasto notarial, costo de la custodia y overhead |
| PCUESFUERZO | **Sí** | `ucp_casos_de_uso.csv`, `ucp_actores.csv` y `ucp_factores.csv`; el resultado debe dar 31.625,44 HH |
| Sensibilidad | Parcial | `escenarios_atraso.csv` da el costo en HH de cada respuesta. Falta elegir las variables a sensibilizar (tarifa, dotación, tipo de cambio, atraso de hitos) y el punto de equilibrio |
| Innovaciones | Parcial | HH por innovación en `HH_por_paquete_EDT.csv` (1.10.x) y compra de lockers y tótems en `calendario-compras.md`; falta su precio y el beneficio esperado |
| Hardware del cliente (informativa) | Parcial | POS, terminales y obra civil (SUM-13 y SUM-31): especificación, marca de referencia y precio |
| Financiamiento, Flujo de caja, Curva S, Indicadores | Se arman con lo anterior | Siguen la nota explicativa del comunicado (`Economica/comunicado_informe_3.md`) |

## Decisiones abiertas que afectan al Excel

1. **Mes de cobro de cada hito:** la fecha del hito marca el inicio del mes siguiente (por ejemplo, H1 = 7 de marzo de 2027 = cierre de M2). Hay que definir en qué mes entra el pago (al aceptar o al mes siguiente) y dejarlo en Parámetros.
2. **Impuesto a la renta en el flujo:** el comunicado mide la rentabilidad sin impuestos; está pendiente de consultar al profesor.
3. **Supuestos declarados (no validados por el cliente):** las 26 personas de operación (el SD-10 y el SD-12 no existen) los plazos de entrega de 8 y 12 semanas y los rendimientos de instalación (3 días por tienda tipo). Ambos deben quedar marcados como supuestos en Parámetros.
4. **Cifra vigente:** 239.250,01 HH, la misma que usan el SD-07 y el Formulario T-15. El Excel debe usar estos insumos.
5. **Si ya cargaron una versión anterior:** las matrices tienen el mismo formato de meses; basta reemplazar los valores. De v1 a v2 cambian M1–M10 y los perfiles; de v2 a v3 se mueven 576 HH de capacitación de M18 a M17 y la estabilización reparte el trabajo de la Etapa 2 entre M13 y M17 (por ejemplo, M15 baja de 52 a 37 personas equivalentes y M16 y M17 suben). El total no cambia, pero sí los valores mes a mes, así que hay que reemplazar las matrices completas.
6. **HH de operación por explicar:** la fila «Operación M21–M56» del T-15 suma 150.848 HH, 1.088 más que las 149.760 de las 26 personas (26 × 160 × 36). La inducción de 416 HH (M20) explica una parte, pero ninguna fuente desglosa la diferencia completa. Usar 149.760 para la dotación fija de operación y registrar la diferencia como pendiente hasta conciliarla con el T-15.
7. **Transacciones de los casos de uso:** `ucp_casos_de_uso.csv` suma 293 transacciones y el T-15 dice 290. Los pesos y el UUCW (640) coinciden, así que no cambia el esfuerzo. Se informa para no copiar la cifra de 290 sin revisarla.

## Lista de chequeo: de dónde sale cada parte del flujo

Cada fila del flujo de caja debe tener una fuente: un insumo del plan (P), las Bases o el comunicado (B), o un supuesto del equipo declarado en Parámetros (S). Las etapas siguen a Sapag, cap. 7 (cómo construir los flujos de caja), y las filas A, B y C a la nota explicativa del comunicado.

| Etapa del flujo | Partida | Fuente | Dónde está o qué decidir | ✓ |
| :-- | :-- | :-- | :-- | :-- |
| 1. Ingresos | Hitos H1–H12 (60 % / 40 % de la implementación) | B | `Hitos_contractuales.csv`, `parametros-bases.md` | ☐ |
| 1. Ingresos | 36 pagos mensuales de operación (M21–M56), sin anticipar ni prorratear | B | `parametros-bases.md` (E-25); monto = costo de operación + margen | ☐ |
| 1. Ingresos | Mes de cobro de cada hito (al aceptar o al mes siguiente) | S | Decisión abierta 1 | ☐ |
| 2. Egresos | Sueldos de implementación por perfil y mes | P + S | `FTE_matriz_perfiles_E26_M1_M56.csv` × costo por perfil dentro del E-26 | ☐ |
| 2. Egresos | Dotación de operación (26 personas) y retén M13–M20 | P + S | `Dotacion_coberturas.csv`, `Guardias_mes_rol.csv`; valor de la unidad de retén | ☐ |
| 2. Egresos | Cobertura de campo de M16 (176 personas, 10.560 HH) | P | `Dotacion_coberturas.csv` | ☐ |
| 2. Egresos | Equipos y compras de OSS (DC-01, lotes 1 y 2, lockers y tótems) | P + S | `calendario-compras.md` (mes), `partidas-sd04-sin-precios.md` (qué); precio cotizado | ☐ |
| 2. Egresos | Nube (Azure) por mes | P + S | `partidas-sd04-sin-precios.md` parte 2; calculadora de Azure | ☐ |
| 2. Egresos | Licencias de terceros con su renovación | B + S | Art. 84.3; precio | ☐ |
| 2. Egresos | Proveedores del T-22, sumados a la operación | S | Hoja Proveedores | ☐ |
| 2. Egresos | Gastos administrativos: overhead, garantías, seguros, notaría, custodia | B + S | `parametros-bases.md`; criterio de cálculo de cada uno | ☐ |
| 2. Egresos | Contingencia (3.688 HH), separada del margen | P | `escenarios_atraso.csv` y SD-07 §7.3.3 | ☐ |
| 2. Egresos | Innovaciones (HH de la rama 1.10 y lockers y tótems) | P + S | `HH_por_paquete_EDT.csv` (1.10.x), `calendario-compras.md` | ☐ |
| 3. Gastos no desembolsables | Depreciación de los activos que compra OSS, si se tratan como inversión | S | Decidir si DC-01 y los equipos son inversión (Sapag) o costo del proyecto | ☐ |
| 4. Impuestos | Impuesto a la renta (27 %) después del EBITDA | S | Decisión abierta 2; la rentabilidad del E-24 se mide sin impuestos | ☐ |
| 5. Ajustes | Valor de desecho al mes 56 y capital de trabajo | S | Decidir si existen (los equipos quedan para el cliente) | ☐ |
| Fila A | Flujo del proyecto, sin crédito ni intereses ni cuotas | B | Comunicado, nota §5 y §7. El VAN se calcula sobre esta fila | ☐ |
| Fila B | Financiamiento: crédito (≤ 80 %), cuotas, intereses al 0,9 % y línea al 3 % hasta $50 M | B | `parametros-bases.md` (E-24); el crédito no es ingreso | ☐ |
| Fila C | Neto y acumulado; mes de mayor necesidad de caja | B | Curva S (comunicado, nota §6) | ☐ |
| Indicadores | Tasa ponderada mensual antes de impuestos (< 20 %), VAN, TIR mensual y anual, EBITDA / ingresos ≤ 20 % | B + S | Comunicado §7 y §8 | ☐ |
| Fuera del flujo | Hardware que compra el cliente (POS, terminales, obra civil) en hoja informativa | B + P | Comunicado §9; SUM-13 y SUM-31 de `partidas-sd04-sin-precios.md` | ☐ |

