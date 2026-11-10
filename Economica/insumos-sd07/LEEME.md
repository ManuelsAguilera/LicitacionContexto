# Insumos del SD-07 para el modelo financiero (Informe 3)

Datos del plan de trabajo que el Excel necesita, conciliados y validados el 2026-11-10. Las cantidades salen de aquí; **los precios, tarifas y tasas los decide el equipo en el Excel**. Origen y método: `80_Artefactos/sd-07_contexto/` (conciliación, estabilización y red física, cada una con su README).

**Recordatorio del profesor:** el Excel se trabaja sin manejo directo de IA, por personas. Estos archivos son datos de entrada, no celdas del Excel.

**Formato de los CSV:** separados por punto y coma, con coma decimal y UTF-8. Al abrirlos en Excel, usar *Datos → Desde texto/CSV* y elegir el punto y coma como delimitador. M1 empieza el 7 de enero de 2027 y cada mes contractual comienza el día 7.

## Cifras base

| Concepto | Valor |
| :-- | --: |
| HH totales del proyecto | **237.104,14** |
| Trabajo técnico, campo, dirección e inducción (incluye trabajos puntuales durante la operación y la dirección hasta M56) | 87.344,14 |
| Operación M21–M56 (26 personas × 160 HH × 36 meses) | 149.760,00 |
| Contingencia (se valoriza aparte, no es margen) | 3.688 HH |
| Retén M13–M20 (se valoriza por unidad, no por HH) | 1.952 unidades de 12 h |

## Archivos y hoja del Excel que alimentan

| Archivo | Qué contiene | Hoja de la plantilla |
| :-- | :-- | :-- |
| `FTE_matriz_roles_M1_M56.csv` | Personas equivalentes (HH ÷ 160) por rol y mes, 37 roles × 56 meses | Costos HH por MES / Costos de operación |
| `HH_matriz_roles_M1_M56.csv` | Lo mismo en HH | Costos HH - Sueldos (control de totales) |
| `HH_por_paquete_EDT.csv` | HH de cada paquete de la EDT con su ventana de meses. Sirve para trazar cada costo a un código EDT (Art. 57.2) y para las HH de las 5 innovaciones (rama 1.10) | Costos (columna de código EDT), Innovaciones |
| `Dotacion_coberturas.csv` | Personas por componente: campo M16 (88 + 88), dirección y PMO, y las 26 personas de operación por rol | Costos de operación |
| `Guardias_mes_rol.csv` | Unidades de disponibilidad del retén por mes y rol | Costos (partida aparte) |
| `Hitos_contractuales.csv` | H1–H12 con su mes contractual, fecha y entregable | Ingresos |
| `calendario-compras.md` | Mes de compra, entrega e instalación de cada lote (DC-01, lote 1, lote 2, lockers), nube y enlaces; quién compra cada cosa | Adquisiciones implementación y operación; Hardware del cliente (informativa) |
| `partidas-sd04-sin-precios.md` | Partidas del SD-04 sin precios: equipos por sitio (SUM-01 a SUM-33) y servicios de nube con su unidad de cobro | Adquisiciones (qué cotizar y cómo se cobra) |

## ¿Se puede avanzar solo con esto?

**Sí, en las cantidades y en el calendario. No, en los valores.** Por hoja:

| Hoja | ¿Alcanza con estos insumos? | Lo que falta (lo decide o busca el equipo) |
| :-- | :-- | :-- |
| Parámetros | Parcial | Valores del E-24 (`00_Bases/Bases_Administrativas.md`, Formulario E-24); **tasa exigida por los socios** (decisión, menor a 20 % anual); conversión a tasa mensual |
| Costos HH (sueldos) | **Sí, en cantidades** | **Costo y tarifa por rol** dentro de los rangos del E-26. Para la tarifa, considerar horas productivas (clase FEP02, diapositiva 90) |
| Costos de operación | **Sí, en cantidades** | Lo mismo: costo de los 26 roles de operación. Valor de la unidad de retén |
| Ingresos | Parcial | **Porcentajes de H1–H12**: verificarlos en el **PDF** de las Bases, porque el `.md` tiene el E-25 dañado por el OCR. Precio total y mensualidad de operación (salen del cálculo) |
| Adquisiciones | Parcial | **Precios**: cotizaciones de equipos (tienda tipo × 22 + laboratorio + 2 CD + DC-01) y de nube (calculadora de Azure con las cantidades de `partidas-sd04-sin-precios.md`). Proveedores del Formulario T-22 |
| Gastos administrativos | No | Overhead, garantías (Art. 35–37), seguros (Art. 38), notaría (Art. 68) y custodia de fuentes (Art. 84.6): **criterio de cálculo de cada uno** |
| Innovaciones | Parcial | HH por innovación en `HH_por_paquete_EDT.csv` (1.10.x); falta su equipamiento (lockers M14) y el beneficio esperado |
| Hardware del cliente (informativa) | Parcial | POS, terminales y obra civil (SUM-13 y SUM-31): especificación, marca de referencia y precio |
| Financiamiento, Flujo de caja, Curva S, Indicadores | Se arman con lo anterior | Siguen la nota explicativa del comunicado (`Economica/comunicado_informe_3.md`) |

## Decisiones abiertas que afectan al Excel

1. **Mes de cobro de cada hito:** la fecha del hito marca el inicio del mes siguiente (por ejemplo, H1 = 7 de marzo de 2027 = cierre de M2). Hay que definir en qué mes entra el pago (al aceptar o al mes siguiente) y dejarlo en Parámetros.
2. **Impuesto a la renta en el flujo:** el comunicado mide la rentabilidad sin impuestos; está pendiente de consultar al profesor.
3. **Supuestos declarados (no validados por el cliente):** las 26 personas de operación (el SD-10 y el SD-12 no existen) y los plazos de entrega de 8 y 12 semanas. Ambos deben quedar marcados como supuestos en Parámetros.
4. **El SD-07 del repositorio todavía dice 40.946 HH.** La cifra vigente es 237.104,14 y la redacción se actualizará después. El Excel debe usar estos insumos.
