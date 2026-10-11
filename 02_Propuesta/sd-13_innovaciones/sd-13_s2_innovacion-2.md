---
id: T7-13-13.2
tipo: seccion
parte: T7-13
titulo: Innovación 2
estado: borrador
bases:
  - "Caso 09, capítulos 7 y 18"
  - "Bases Transversales, capítulos 18 y 26"
requisitos:
  - RF-131
  - RF-134
  - RF-135
  - RF-136
  - RF-137
depende_de:
  - T7-03
  - T7-05
  - T7-07
adjuntos: []
jira: []
cifras:
  - discrepancia_conteo_ciclico_pct
  - produccion_etapa_1_mes
origen: "80_Artefactos/sd-13_contexto/decision_cartera_equipo.md; investigacion_cinco_innovaciones.md, sección 3"
actualizado: 2026-10-11
---
## 13.2 Innovación 2

La innovación de proceso es Conteo cíclico predictivo. Modifica la selección del trabajo de inventario mediante un modelo que estima el riesgo de discrepancia por referencia, ubicación y período. El responsable revisa la prioridad propuesta y asigna los conteos dentro de la capacidad de la tienda. El beneficio se verifica por diferencias relevantes detectadas por hora de trabajo.

### Problema y aporte sobre el alcance base

El conteo cíclico encuentra diferencias en el 12,4 % de las referencias auditadas. El Caso exige medir exactitud por categoría y contar sin cerrar la tienda (Multitiendas Ancoa S.A., 2026b, caps. 7 y 18). El porcentaje describe referencias auditadas; no identifica por sí solo la proporción de robo ni el error de toda la población de existencias.

RF-131 y RF-134 ya permiten parametrizar frecuencias y generar programas de conteo; RF-135 a RF-137 cubren registro, recuento y exactitud. El aporte de esta innovación es ordenar el trabajo por riesgo y valor de la discrepancia esperada, manteniendo cobertura y frecuencias exigidas. La propuesta reemplaza la candidata de inventario RFID del resumen del equipo y no requiere etiquetas electrónicas de precio ni etiquetado RFID.

### Tecnología y madurez

El desarrollo compara programación vigente, reglas de prioridad y modelos supervisados de árboles con boosting. Como referencia se utiliza HistGradientBoostingClassifier de scikit-learn y un estimador de magnitud de diferencia. La selección se basa en desempeño y trazabilidad con los datos del cliente; el identificador de cada SKU no se convierte sin tratamiento en una categoría de alta cardinalidad (Scikit-learn developers, s. f.-a).

Las variables se calculan con información disponible antes del conteo, como tiempo desde el recuento anterior, recepciones, ventas, devoluciones, ajustes y diferencias verificadas. La etiqueta de entrenamiento es la discrepancia física confirmada, conciliada con movimientos ocurridos durante la medición. El resultado del conteo que se intenta predecir queda fuera de las entradas.

La biblioteca corresponde al estado de componente documentado de la escala de evidencia. El modelo específico requiere evaluación retrospectiva, luego operación en sombra y finalmente aceptación operativa. La partición temporal evita entrenar con información posterior a la que se utiliza para decidir; se evalúa además la transferencia entre tiendas (Scikit-learn developers, s. f.-b). La validación histórica por sí sola no acredita mejora en la ejecución real.

### Incorporación a arquitectura y EDT

El componente predictivo reside en la capa de aplicación del ámbito retail y consume historia del servicio de existencias mediante contratos de datos. El entrenamiento utiliza conjuntos versionados; la inferencia genera una lista ordenada para la aplicación de conteo. La programación puede utilizar probabilidad de discrepancia, magnitud esperada y tiempo previsto de recuento para priorizar detección por hora.

El paquete «Conteo cíclico predictivo» pertenece a la rama 1.10 Innovaciones e incluye preparación de datos, comparación de modelos, integración y ensayo. La construcción se realiza durante el desarrollo de la Etapa 1, la evaluación en sombra durante los meses 13 a 15 y el uso operativo desde el mes 16. Se conserva una muestra aleatoria o estratificada independiente del modelo para medir exactitud general y evitar que la priorización oculte categorías poco exploradas.

El responsable aprueba la lista y valida los ajustes mediante el procedimiento de inventario. El modelo no cambia saldos ni clasifica una discrepancia como hurto. El registro conserva versión, entradas, recomendación y decisión humana. El diseño responde a RT-18.01 a RT-18.09 y utiliza NIST AI RMF e ISO/IEC 42001 para documentar riesgos y gobierno del componente (Tabassi, 2023; International Organization for Standardization, 2023).

### Impacto económico

La inversión comprende perfilado, preparación de historia, desarrollo, evaluación e integración. La operación incluye cómputo, seguimiento de desempeño y reentrenamiento. El beneficio directo proviene de mejorar la cantidad de discrepancias detectadas con las horas disponibles o de reducir horas para una cobertura equivalente. Los ahorros por pérdida evitada requieren evidencia adicional y no se imputan automáticamente al modelo. Estos componentes se valorizan en el flujo de caja con el paquete de innovación separado del conteo obligatorio.

### Verificación del beneficio

El protocolo compara grupos o ventanas equivalentes con la misma capacidad de trabajo. Registra diferencias relevantes por hora, cobertura por categoría, tiempo de conteo y calidad de las probabilidades. La línea base corresponde a la programación vigente. Antes del piloto se fija qué diferencia se considera relevante y se calcula la muestra requerida para comparar ambos procesos.

La meta de aceptación es una mejora demostrada de detección por hora respecto del proceso base, manteniendo cobertura y frecuencias. El umbral contractual de mejora se fija con el levantamiento y se registra en el T-19 antes de ensayar. La muestra independiente verifica que la exactitud general no empeore. La medición durante los meses 13 a 15 permite verificar el aporte antes del mes 16, conforme a RT-26.08; la operación revisa deriva y rendimiento por categoría.

### Riesgo de adopción y contingencia

La historia insuficiente o sesgada tiene probabilidad inicial alta e impacto alto, dada la falta de desglose que describe el Caso. El equipo depura diferencias verificadas, revisa cobertura y mantiene muestreo independiente. Mientras la historia no permite entrenar y evaluar, la tienda utiliza reglas y programación parametrizada.

La deriva tiene probabilidad media e impacto alto. El seguimiento compara desempeño con el proceso base y registra cambios por temporada y tienda. Si la priorización deja de mejorar el conteo o incumple cobertura, se desactiva y vuelve la programación de RF-134. La aplicación de conteo y las reglas de ajuste siguen operativas. Las probabilidades son una valoración inicial que el T-16 revisa tras el perfilado.
