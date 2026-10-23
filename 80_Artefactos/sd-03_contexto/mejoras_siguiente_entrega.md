# Aspectos a considerar en la siguiente entrega: hilo lógico de 3.2.1 y 3.2.2

Documento de contexto, no es entregable. Fecha: 2026-10-18. Fuente de la revisión: Informe 2, Subdocumento 3 (PDF del 12-10), secciones 3.2.1 y 3.2.2. No se corrige en esta entrega. Estos puntos se trabajan en la próxima. Para repetir esta revisión en otras secciones se usa el agente `revisor-hilo-logico`.

## Resumen

El razonamiento de fondo se sostiene: promesas, responsabilidades, frentes, áreas, servicios y reparto por etapas con cuatro pruebas. Lo que falla es cómo queda escrito el paso de una idea a la siguiente. No se cambian las decisiones.

## Flujo vigente y dónde se rompe

```
Síntomas y 5 causas raíz (sd-02)
  → 4 promesas
  → 15 responsabilidades (A1-A10, B1-B3, C1-C3)
  → 3 frentes (régimen jurídico)
  → áreas
  → 13 servicios + base tecnológica          ⚠ 1 y 2
  → control de cobertura (Figura 3.3)        ⚠ 3
  → pruebas P1-P4                            ⚠ 4
  → contraste con fechas y comité (cartera por tramos)   ⚠ 5
  → Tabla 3.1                                ⚠ 6
```

## Hallazgos

| N.º | Nivel | Dónde | Qué pasa | Cierre mínimo |
| :-- | :-- | :-- | :-- | :-- |
| 1 | Debilidad de justificación | 3.2.1 | No hay regla escrita de cuándo una responsabilidad se fusiona o se parte. A1 y A2 forman un servicio, A6 y A7 otro, y A5 se divide en ventas y comisiones. | Declarar el criterio de partición: dueño de datos distinto, ciclo de cambio distinto o régimen jurídico distinto. |
| 2 | Inconsistencia de definición | 3.2.1 y Tabla 3.1 | El texto dice que «los servicios y la base cubren todo el producto», pero la Tabla 3.1 asigna también el punto de venta con operación sin conexión, que no es ninguno de los dos. | Declarar las piezas asignables: 13 servicios, la base tecnológica y el punto de venta con sus componentes locales. |
| 3 | Debilidad de justificación | 3.2.1, Figura 3.3 | Las causas raíz se presentan como «la base de la descomposición», pero la división sale de promesas y responsabilidades. La tabla causa → servicio funciona como control de cobertura y estaba rotulada «por validar» en el borrador. Tres causas (C2, C4, C5) las atienden la base, los componentes locales y la capacitación, no servicios. | Presentar las causas como control de cobertura. Subir al texto la tabla promesa → servicio. |
| 4 | Salto de lógica | 3.2.2 | P1 se apoya en qué servicio sostiene cada promesa, pero esa relación no está en el Informe 2. P3 («necesario para ser el registro oficial») es amplia y se aplica con distinta fuerza (ventas y originación). | Incluir la tabla promesa → servicio. Precisar P3 con una lista de lo que es registro oficial. |
| 5 | Inconsistencia de definición | 3.2.2 | La cartera de crédito se parte en tramos. La unidad de asignación deja de ser el servicio y el número de tramos queda por definir. | Declarar la cartera como excepción al criterio y dar el número de tramos o la fecha en que se fija. |
| 6 | Inconsistencia de definición y salto | 3.2.1, 3.2.2 | Las integraciones críticas, el reparto del sistema de 2009 y el retiro de plataformas se asignan en el párrafo y no en la tabla. El sistema de almacenes y el comercio electrónico quedan con «etapa por definir», aunque su integración con existencias sostiene la promesa de disponibilidad, de Etapa 1. | Pasarlas a una segunda tabla de actividades de transición, con etapa fijada. |
| 7 | Debilidad de justificación | 3.2.2 | Abastecimiento y pedidos sostienen las promesas de existencia y de entrega, pero van en la Etapa 2 con una razón que no es una de las cuatro pruebas («el comité no los nombró»). | Declarar la excepción en la tabla y su efecto: la entrega no mejora hasta el mes 21. |
| 8 | Debilidad de justificación | 3.2.2, Figura 3.5 | La figura dice que la Etapa 2 solo requiere servicios de las etapas 1 y 2. Es cierto por construcción. No demuestra que el orden sea el mejor. Además, existencias recibe movimientos de abastecimiento y posventa, y ventas entrega a comisiones, ambos de Etapa 2. | Documentar el adaptador temporal con el sistema de 2009 y su retiro en el mes 21. |
| 9 | Debilidad de justificación | 3.2.2 | Comisiones en la Etapa 2 deja la causa C4 (incentivos) sin atender hasta el mes 21. El texto no lo señala. | Declararlo como riesgo en el sd-08 y como limitación en el sd-03. |
| 10 | Debilidad de justificación | 3.2.2 | La Etapa 1 carga ocho piezas y la migración en 12 meses. La Etapa 2 carga seis servicios en 6 meses con una marcha blanca de 2. El catálogo lo refleja (142 RF contra 81). No se discute el balance de carga (DEC-42, `auditoria_decisiones.md`). | Agregar un indicador de carga por etapa (personas a capacitar, sitios, migraciones) o decir que no se usó. |
| 11 | Inconsistencia | 3.2.4 y 3.3.2 | El catálogo cita 307 y luego 308 elementos. La 3.3.2 dice «plataforma común» y la 3.2.1 «base tecnológica». El índice de tablas repite la Tabla 3.9. | Unificar nombres y cifras. |

## Qué sí se sostiene

- Partir de las promesas y de las responsabilidades de negocio, en vez de los sistemas actuales.
- Separar primero por régimen jurídico (línea roja del Caso).
- Asignar por servicio y no por requerimiento.
- Adelantar el negocio financiero a la Etapa 1, con razones fechadas (2029, 620.000 clientes) y la corrección declarada al orden del comité.
- Cumplir sin excepción las pruebas en nueve de los trece servicios.

## Preguntas que el profesor podría hacer

1. ¿Cómo supieron que necesitaban exactamente estos 13 servicios y no 10 o 18?
2. ¿Por qué comisiones es un servicio aparte de ventas?
3. Si la entrega es una promesa, ¿por qué pedidos entra recién en el mes 21?
4. ¿Qué pasa con la disponibilidad publicada entre los meses 16 y 21 si el comercio electrónico no tiene etapa?
5. ¿Qué criterio equilibra la carga entre las dos etapas?

## Cómo repetir la revisión

Agente `revisor-hilo-logico` (`.claude/agents/revisor-hilo-logico.md`). Se le entregan las rutas de las secciones y la cadena de ideas que se quiere revisar.
