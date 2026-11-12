# Parámetros de las Bases para el modelo financiero

Valores que el Excel toma de las Bases Administrativas, no del plan de trabajo. Se verificaron en el PDF (`FEP01.26 Bases Administrativas TFEP-01-2026-3.pdf`), porque el `.md` de `00_Bases/` tiene tablas dañadas por el OCR. La página es el folio impreso. Van en la hoja Parámetros como celdas de entrada, con su fuente al lado.

## Formulario E-24: condiciones de la oferta económica (folio 73)

| Parámetro | Valor |
| :-- | --: |
| Dólar (USD) | $ 900 |
| Euro (EUR) | $ 1.000 |
| Unidad de Fomento (UF) | $ 40.000 |
| Tasa de interés, crédito de consumo | 0,9 % mensual |
| Tasa de interés, línea de crédito | 3,0 % mensual |
| Rentabilidad máxima | 20 % (EBITDA / ingresos netos, sin IVA ni impuestos; comunicado §7) |
| Monto máximo de la línea de crédito | $ 50.000.000 |
| Financiamiento propio, máximo | 20 % |
| Financiamiento bancario, máximo | 80 % |
| IVA | 19 % |
| Horizonte de evaluación | 56 meses |

El tipo de cambio del E-24 es obligatorio. Usar otro es causal de observación grave (Art. 9.3).

## Formulario E-25: hitos de pago (folio 74)

Los porcentajes se aplican sobre el valor total de la fase de implementación. Están también en `Hitos_contractuales.csv`.

| Hito | Mes | % | Hito | Mes | % |
| :-- | --: | --: | :-- | --: | --: |
| H1 | 2 | 8 % | H8 | 14 | 5 % |
| H2 | 4 | 7 % | H9 | 17 | 10 % |
| H3 | 6 | 10 % | H10 | 18 | 10 % |
| H4 | 10 | 10 % | H11 | 19 | 5 % |
| H5 | 12 | 10 % | H12 | 21 | 10 % |
| H6 | 13 | 5 % | **Etapa 2** | | **40 %** |
| H7 | 16 | 10 % | | | |
| **Etapa 1** | | **60 %** | | | |

Operación: 36 pagos mensuales, M21 a M56, pagados dentro de los primeros días del mes siguiente vencido, con descuento de multas por nivel de servicio. No se anticipa ni se prorratea en la implementación.

## Garantías (Art. 35 a 37, folios 23 y 24)

Su costo financiero va en la hoja de gastos administrativos (comunicado §6). El costo lo fija el banco (comisión por período); es un supuesto del equipo.

| Garantía | Monto | Vigencia |
| :-- | :-- | :-- |
| Seriedad de la oferta (Art. 35) | USD 500.000 | Mínimo 150 días corridos desde la entrega de la propuesta, renovable, hasta 10 días hábiles después del inicio del contrato |
| Fiel cumplimiento (Art. 36) | USD 1.000.000 | Desde la firma del contrato hasta 12 meses después del término de la operación. Reemplaza a la de seriedad |
| Correcto funcionamiento (Art. 37) | 5 % del valor total de la implementación | 24 meses desde la aceptación final del mes 21 |

## Seguros (Art. 38, folio 24)

| Póliza | Cobertura mínima | Vigencia |
| :-- | :-- | :-- |
| Responsabilidad civil general y profesional | UF 20.000 por evento y en el agregado anual | Toda la duración del contrato |
| Ciberriesgo y responsabilidad por datos | UF 20.000, con gastos de notificación, análisis forense y restitución de datos | Toda la duración del contrato y 12 meses posteriores |
| Todo riesgo de equipos y bienes | Valor de reposición de los equipos provistos u operados en instalaciones del cliente | Desde la instalación hasta la entrega final |
| Accidentes del trabajo y responsabilidad patronal | Conforme a la legislación vigente | Toda la duración del contrato |

La prima de cada póliza es un supuesto del equipo (cotización o porcentaje de la suma asegurada).

## Otros gastos administrativos

| Concepto | Fuente | Qué dice |
| :-- | :-- | :-- |
| Gastos notariales y de contratación | Art. 68.3 | La firma es en la notaría que designe el cliente y los gastos notariales y de legalización son del adjudicatario |
| Custodia de fuentes ante terceros | Art. 84.6 | Depósito de custodia ante un tercero independiente, con actualización semestral y cláusulas de liberación ante insolvencia o incumplimiento grave |
| Licencias de terceros | Art. 84.3 | A nombre del cliente, vigentes todo el contrato, con el costo de renovación explícito en la oferta económica |
| Overhead de la empresa | Comunicado §6 (E-21, 2.1) | Gerencia, administración, contabilidad y área legal. Criterio de cálculo a declarar |

Los intereses del financiamiento no son gastos administrativos: van solo en la hoja de financiamiento (comunicado §6).

## Formulario E-26: rangos de costo y tarifa (folio 76)

Están por perfil en `FTE_matriz_perfiles_E26_M1_M56.csv` y `equivalencias_roles_E26.csv`. Los roles que no estén en la lista se declaran en la hoja de tarifas con rangos coherentes.
