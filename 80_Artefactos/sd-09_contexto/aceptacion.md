---
estado: borrador
parte: T7-09
---
# Vista de aceptación y calendario

El expediente futuro deberá contener artefacto, evidencia objetiva, trazabilidad y observaciones resueltas ([Bases Administrativas, art. 18.2](../../00_Bases/Bases_Administrativas.md#L499)). El cliente dispone de diez días hábiles para revisar y el adjudicatario de otros diez para subsanar; repetir observaciones de la misma naturaleza cuenta como atraso imputable ([art. 18.3](../../00_Bases/Bases_Administrativas.md#L501)). La aceptación conserva responsabilidad por defectos posteriores ([art. 18.4](../../00_Bases/Bases_Administrativas.md#L503)). El calendario debe reservar esas ventanas antes de producción y contemplar congelamientos; no desplazar meses 16, 21 o 56 para acomodarlas.

| Compuerta | Resultados / obligaciones | Dueños y dependencias |
| :--- | :--- | :--- |
| Preparación antes de campañas | Criterios y brechas de [todas las fichas](README.md) | QA coordina; Arquitectura, responsables Retail/Emisor y Contraparte validan datos, perfiles, tolerancias y línea base. |
| Mes 16, Etapa 1 | R01/R04 graduales; R06–R09; R16–R22; R24 primera parte; R25 degradación; R28 | Responsables de Existencias, Oferta, Originación, Evidencia y Frontera; integración, separación, consentimiento y QA transversal preceden puesta en producción. |
| Mes 21, Etapa 2 | R02 completo; R03; R04 22 tiendas; R05; R10–R15; R18 cartera migrada; R24 segunda parte; R25 carga; R26–R27 | Pedidos, Marketplace, Posventa, Comisiones y Cartera; requieren maestros, disponible y migración conciliados, campañas completas y observaciones resueltas. |
| Operación, hasta mes 24 supuesto | R23 remediación autoridad antes de 2029 | Emisor y encargado de cumplimiento aportan plan oficial de hitos; informe proponente apoya acta autoridad, sin sustituirla. |
| Primer evento después de mes 21 | R02 y R25; indicadores dependientes del evento real | Canales/Operaciones y QA preservan ensayo previo y medición real. Fecha externa no cambia duración 56 meses. |
| Operación meses 21–56 | Indicadores, retención, seguridad, continuidad y renovaciones aplicables | Operaciones monitorea; Seguridad programa pentest anual y recuperación; QA actualiza trazas; Contraparte verifica compromisos. |

El jefe de proyecto reúne mediciones; QA diseña campañas y verifica expedientes; cada responsable de servicio responde por correcciones. El tercero independiente ejecuta pentest y entrega informe íntegro. La Contraparte Técnica firma aceptación, con participación de la Filial emisora en cartera y controles financieros. No atribuir aprobación humana a un agente.

R02, R04, R09, R15 y R26 tienen responsabilidad compartida. El cliente ejecuta preparación, conteo, cambio de etiquetas, atención del mesón y entrega física; la solución responde por estados, cálculos y controles descritos en [resultados](resultados.md). No excluir el resultado porque una parte depende del cliente: presentar ambas mediciones y acciones acordadas.

Las condiciones de corte incluyen retorno probado, conciliación diaria y comunicación a clientes por tramo. Los ensayos de continuidad no habilitan originación de tarjetas ni ampliación de cupo offline. El crédito contra autorización previa permanece condicionado a decisión de riesgo y contrato, distinta de la prueba de venta Retail.

## Decisión por criterio

Propuesta de operación de la matriz: QA comprueba evidencia y reporta no conformidades; el dueño corrige y el ensayo se repite. La Contraparte y el responsable del ámbito resuelven la compuerta. Un criterio pendiente de umbral, carga o suficiencia jurídica queda bloqueado para aceptación, aunque tenga una ficha completa. El cierre 100 % de trazabilidad de SD06 exige historia, prueba y evidencia para todos los requisitos de la línea base de etapa; esta primera matriz parcial no acredita ese cierre.
