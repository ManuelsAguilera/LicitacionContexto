# Borrador del paso G · texto de las figuras de cronograma del SD-07 (2026-11-10)

Documento de trabajo, no entregable. Texto para insertar en el `.tex` del SD-07 y en el anexo del T-14 cuando se haga el paso T. La numeración de figuras y tablas es provisional y se ajusta al insertar. Las figuras están en `04_Adjuntos/diagramas/diag-07-0*` y las cifras salen de la red v3 (`red-v3-2026-11-10/`).

---

## §7.2.4.1 Capacidad durante los solapamientos · Figura 7.17 (histograma)

**Texto de caída (antes de la figura)**

La programación se estabilizó para que los solapamientos de M13–M15 y M19–M20 no concentren la carga en un solo mes. La estabilización mueve actividades solo dentro de su holgura, entre su inicio temprano y su inicio tardío, de modo que no cambia la ruta crítica ni las fechas contractuales. Se aplicó con un margen mínimo de 10 días hábiles por actividad desplazada, para no convertir en críticas actividades que hoy pueden absorber un atraso. La Figura 7.17 compara la carga mensual antes y después de este ajuste.

**Leyenda**

Figura 7.17: Personas equivalentes por grupo de perfiles, M1–M21, antes y después de la estabilización.
Fuente: elaboración propia a partir de la red del cronograma.

**Cómo leerla**

El panel superior muestra la programación con los inicios propuestos originalmente y el inferior, la programación estabilizada. Ambos usan la misma escala. Cada barra suma las horas del mes divididas por 160 y se separa por grupo de perfiles. Las franjas sombreadas marcan los dos solapamientos que exige el Art. 17.2. La figura incluye solo el trabajo de la red, sin la cobertura de campo de M16, la dirección ni la operación, que tienen dotación fija y no se desplazan.

**Qué se concluye**

El pico de M15 baja de 46,3 a 30,9 personas equivalentes. El desarrollo de la Etapa 2, que antes partía completo el mismo día en que se aprueba su línea base (H8), queda repartido entre M15 y M17. Se movieron 77 actividades y ninguna pasó de su inicio tardío, por lo que H1–H12, el fin de ambas marchas blancas y el ingreso de las 22 tiendas el 7 de abril de 2028 se mantienen. Después del ajuste, el mes de mayor carga pasa a ser M4, con 38,5 personas equivalentes, por la construcción en paralelo de la nube, la arquitectura y la infraestructura antes de H3. Ese pico se dejó como está porque la cadena hacia H3 tiene poco margen, y moverla dejaría al hito expuesto a un atraso como el del escenario S2 (§7.3.3).

---

## §7.3.4 Carta Gantt y relación con los hitos del Anexo E-25

**Texto de caída (introduce las dos figuras)**

El cronograma se presenta en tres niveles de lectura. La Figura 7.18 muestra solo los hitos y las fases del contrato. La Figura 7.19 resume las quince ramas de la EDT. El detalle por paquete de trabajo está en el anexo del Formulario T-14, en una lámina por rama.

### Figura 7.18 (cronograma de hitos)

**Leyenda**

Figura 7.18: Cronograma de hitos H1–H12 y fases del contrato, M1–M21.
Fuente: elaboración propia a partir de la red del cronograma y del Formulario E-25.

**Cómo leerla**

Las barras superiores son las fases del contrato. La operación continúa hasta el 6 de septiembre de 2031, fuera del tramo dibujado. Cada rombo es un hito en su fecha contractual. La línea gris que lo precede va desde la fecha más temprana en que el hito puede cumplirse hasta la fecha comprometida, y su largo es la holgura. Los rombos naranjos son hitos sin holgura. Las franjas grises marcan el congelamiento de fin de año, la vuelta a clases y la envolvente preventiva de eventos (§7.3.2).

**Qué se concluye**

Los hitos de construcción tienen margen. H1 tiene 4 días; H2, 21; H3, 30; H4, 31; H8, 29; y H9, 31. En cambio, H5, H6, H7, H10, H11 y H12 no tienen holgura, porque dependen de ventanas de duración fija, como la marcha blanca de tres meses de la Etapa 1, la de dos meses de la Etapa 2 y la habilitación de las tiendas. Esas ventanas no se pueden acortar, así que el control de plazos se concentra en el trabajo que llega a ellas. La versión candidata de la Etapa 1 se verifica antes del congelamiento del 1 de noviembre (§7.3.2.1), y H4 se formaliza el 7 de noviembre sobre esa versión, sin intervenir producción durante la restricción.

### Figura 7.19 (resumen por rama)

**Leyenda**

Figura 7.19: Cronograma resumen de las quince ramas de la EDT, M1–M25.
Fuente: elaboración propia a partir de la red del cronograma y de la dotación por componente.

**Cómo leerla**

Cada fila es una rama de la EDT y sus barras unen las ventanas de sus actividades según la etapa. La flecha a la derecha indica que la rama continúa hasta M56. El borde oscuro marca los tramos con actividades sin margen en la programación estabilizada, es decir, actividades cuyo atraso pasa directo al hito que alimentan. La columna «Recibe de» indica las ramas que entregan insumos a cada rama. Se obtuvo siguiendo las relaciones de la red, incluidas las que pasan por un hito o por una revisión intermedia.

**Qué se concluye**

El desarrollo de software recibe insumos de la infraestructura (1.4) y del levantamiento (1.2), por lo que ambos van primero. Las integraciones (1.6) y la migración de datos (1.7) alimentan las innovaciones, la implantación, las marchas blancas, la capacitación y la operación. Son las ramas con más sucesoras, y un atraso en cualquiera de ellas afecta a cinco o seis ramas. Los tramos sin margen se concentran al inicio (levantamiento e infraestructura), en el piloto de junio de 2027 (calidad), en el corte de inventario previo a la marcha blanca E1 (migración) y en las propias marchas blancas. La construcción de la Etapa 2 ocurre durante la marcha blanca de la Etapa 1, y la operación comienza en M21 con las ramas de seguridad, documentación y operación activas hasta el cierre.

---

## Anexo del Formulario T-14 · Gantt detallado por rama (Figuras T14.1 a T14.18)

**Texto de caída**

Las láminas siguientes desarrollan cada rama de la EDT hasta su tercer nivel. Cada fila es un paquete de trabajo o, en las ramas 1.5 y 1.10, una cuenta de control. La Tabla T14.1 indica qué lámina corresponde a cada rama.

**Tabla T14.1: Láminas del Gantt detallado por rama.**

| Rama | Láminas | Elementos de tercer nivel |
| :-- | :-- | --: |
| 1.1 a 1.3 | T14.1 a T14.3 | una lámina por rama |
| 1.4 Infraestructura híbrida y plataforma base | T14.4 y T14.5 | 24 |
| 1.5 Desarrollo de software | T14.6 a T14.8 | 51 cuentas de control |
| 1.6 a 1.15 | T14.9 a T14.18 | una lámina por rama |

Fuente: elaboración propia.

**Cómo leer cada lámina**

La columna HH suma las horas de las actividades del elemento. La ventana indica el primer y el último mes con trabajo. El margen es la cantidad de días hábiles que la actividad más ajustada del elemento puede atrasarse sin mover su sucesora. Un margen 0, en naranja, coincide con el borde oscuro de la barra. Las barras se colorean por etapa. Los elementos sin actividades propias se ejecutan dentro de la dirección del proyecto o del equipo de operación, y sus horas están en esas coberturas.

**Qué se concluye (para el cierre del anexo)**

Con este detalle se puede ubicar cada hora planificada en su paquete y en su mes, y ver qué paquetes no tienen margen. Esos paquetes son los que el Jefe de Proyecto controla semanalmente (§7.3.1) y los primeros en recibir las respuestas de compresión descritas en §7.3.3.

---

## Pendientes para el paso T (no van en el texto final)

1. La figura de distribución mensual de HH de §7.3.3, que hoy no tiene número, debe regenerarse con la red v3 (239.250,01 HH) o reemplazarse por la Figura 7.17.
2. La Tabla 7.8 del PDF de noviembre (láminas en el cuerpo) se reemplaza por la Tabla T14.1 del anexo.
3. Las 22 láminas actuales del cuerpo se retiran; el cuerpo queda con las Figuras 7.17, 7.18 y 7.19.
4. Decidir si se cita el PMBOK al nombrar la estabilización y los tres niveles del cronograma. La regla RR-20 limita las citas a exigencias particulares y datos del Caso 09; hoy el texto nombra las técnicas sin cita.
