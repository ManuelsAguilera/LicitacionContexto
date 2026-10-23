# Escalas, matriz y umbrales propuestos para el sd-08 (F2)

Documento de contexto, no entregable. Creado el 2026-10-11. Base: FEP04 · 7, 8 y 9 (`90_Referencia/clases markdown/FEP04_Gestion_de_Riesgos_TIC_transcripcion.md`, l. 151-206). Los rangos de la clase se conservan; lo que se adapta al caso está marcado **[adaptación]** y es la parte que el usuario debe aprobar. Sin cifras en pesos (Art. 50.2).

## 1. Escalas (cinco niveles)

Valor numérico de cada nivel para calcular la exposición P × I. Probabilidad: punto medio de cada rango de la clase (FEP04 · 7): 0,05 / 0,20 / 0,40 / 0,60 / 0,85. Impacto: 0,05 / 0,10 / 0,20 / 0,40 / 0,80, **decisión del equipo** (la clase da los rangos y los umbrales de zona, no estos valores; ISO 31000 deja los criterios a cada organización, y no se pudo confirmar que PMBOK fije estos números). Con ellos las zonas de la clase funcionan: 0,60 × 0,80 = 0,48 es crítica y 0,40 × 0,40 = 0,16 es media.

| Nivel | Probabilidad | Impacto en plazo | Impacto en esfuerzo **[adaptación]** | Impacto en costo | Impacto en alcance y calidad | Impacto en servicio **[adaptación]** |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Muy alto (5) | > 70 % | > 6 semanas | > 5 % de las horas del proyecto | > 5 % del contrato | Efecto muy significativo sobre la funcionalidad comprometida | Incumple una restricción del Caso, la separación de los dos negocios o un umbral con sanción (CMF, Ley 21.719); pérdida de datos transaccionales |
| Alto (4) | 51 a 70 % | 3 a 6 semanas | 2 a 5 % | 2 a 5 % | Efecto significativo sobre la funcionalidad comprometida | Interrupción mayor a la autonomía de 24 h en tienda o incumple RTO/RPO |
| Medio (3) | 31 a 50 % | 1 a 3 semanas | 1 a 2 % | 1 a 2 % | Efecto sobre áreas funcionales clave | Degradación visible de un servicio crítico, sin pérdida de datos |
| Bajo (2) | 11 a 30 % | 2 días a 1 semana | 0,5 a 1 % | 0,5 a 1 % | Efecto menor sobre la funcionalidad general | Degradación breve, con rodeo disponible |
| Muy bajo (1) | 1 a 10 % | < 2 días | < 0,5 % | < 0,5 % | Efecto menor sobre funciones secundarias | Sin efecto para el cliente final |

Costo: siempre porcentaje del contrato; el monto vive solo en el Sobre 3. Esfuerzo: porcentaje de las horas de la estimación del sd-07; el equivalente en horas-persona se calcula cuando esa estimación esté cerrada.

### Reglas de calificación **[adaptación, para aprobar]**

1. **Hito contractual.** Si el evento atrasa un hito sin holgura (paso a producción del mes 16, del mes 21, retiro de la plataforma de 2011 en el mes 22, mes 56), el impacto en plazo es **Muy alto** sin importar las semanas, porque la ruta crítica no admite holgura (sd-07, Tabla 7.6) y las salidas son no negociables.
2. **Línea roja.** Cualquier evento que borre la separación de datos entre retail y filial emisora es Muy alto en servicio (Caso, línea roja).
3. **Se califica el peor de los impactos** entre plazo, esfuerzo, costo, alcance y servicio, y la calificación se justifica con un dato del Caso o del subdocumento fuente.
4. **Oportunidades:** se califican con la misma escala de probabilidad y con impacto positivo; no se suman a las reservas.

## 2. Matriz de exposición y zonas

Exposición = P × I (valores numéricos de arriba). Rangos de la clase, FEP04 · 8:

| Zona | Rango | Regla de acción | Dónde se ve en la oferta |
| :-- | :-- | :-- | :-- |
| Crítica | P × I ≥ 0,40 | Se cambia el diseño para que el riesgo deje de existir, o se escala al Comité Ejecutivo; no se acepta | Arquitectura, alcance o exclusión explícita |
| Alta | 0,20 ≤ P × I < 0,40 | Acción de mitigación con costo y plazo dentro del plan de trabajo | Cuenta en la EDT y en el cronograma |
| Media | 0,08 ≤ P × I < 0,20 | Se acepta activamente: reserva de contingencia y disparador definido | Reserva (el monto va al Sobre 3) |
| Baja | P × I < 0,08 | Se acepta pasivamente: observación y revisión mensual | Registro, sin costo asociado |

## 3. Apetito, tolerancia y umbral (FEP04 · 9) **[adaptación]**

- **Apetito:** bajo en lo contractual y regulatorio (hitos, separación de los dos negocios, cumplimiento ante la CMF) y moderado en lo técnico mejorable (rendimiento, adopción), donde se acepta ajustar el diseño mientras no cambie un hito.
- **Tolerancia:** cero atraso en los hitos de los meses 16, 21 y 56; cero cruces de datos sin base; hasta lo que cubra la reserva de contingencia en el resto.
- **Umbral de escalamiento:** todo riesgo en zona crítica va al Comité Ejecutivo (mensual); alta, al Comité de Proyecto (quincenal); técnicos, también al Comité de Arquitectura (mensual). La liberación de la reserva de gestión la decide el Comité Ejecutivo.

## 4. Aprobación

**Aprobado por el usuario el 2026-10-11**: escalas y zonas de la clase con las adaptaciones marcadas, regla del hito contractual, valores numéricos de arriba y apetito y tolerancia. Lo que sigue es el detalle de lo aprobado.

1. Que las escalas y las zonas son las de la clase, con las adaptaciones marcadas.
2. La regla del hito contractual (1 en «Reglas de calificación»): aumenta cuántos riesgos caen en zona crítica, y eso es intencional.
3. Los valores numéricos de P e I (supuesto mío).
4. El apetito y la tolerancia de la sección 3.
