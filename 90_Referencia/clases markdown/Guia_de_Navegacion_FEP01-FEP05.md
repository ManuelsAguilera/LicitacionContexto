# Guía de navegación entre presentaciones — Taller Formulación de Proyectos Informáticos

> **Para qué sirve:** cuando tengas una duda, busca el tema o la palabra clave aquí y la guía te dice **en qué clase (FEP01–FEP05) y en qué diapositivas** está la respuesta. Las referencias como `[FEP03 · 59–61](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-59)` son enlaces a la transcripción en Markdown (archivos `…_transcripcion.md`, que deben estar en la misma carpeta que esta guía).

**Cómo buscar, en orden:**
1. **¿Sabes la palabra exacta?** (por ejemplo, PUE, RTO, UCP o RBS) → ve a la **sección 4, el índice alfabético** (Ctrl+F).
2. **¿Tienes una pregunta concreta?** (por ejemplo, «¿cuánta reserva cargo al precio?») → ve a la **sección 3, preguntas frecuentes**.
3. **¿Quieres estudiar un tema completo?** → ve a la **sección 2, el índice temático**.
4. **¿Estás armando un entregable?** → ve a la **sección 5, rutas por entregable**.
5. **¿Quieres ver todas las láminas de una clase?** → ve al **anexo, el índice completo de diapositivas**.

---

## 1 · Las cinco clases de un vistazo

| Clase | Tema central | Diap. | Pregúntale a esta clase sobre… |
|---|---|---|---|
| **FEP01** · Arquitectura de Software | Diseñar y justificar la solución técnica | 309 | Estilos de arquitectura, lógica vs. física, nube, disponibilidad, continuidad, seguridad, login, ambientes, CI/CD, costeo de la nube |
| **FEP02** · Requisitos, Alcance, Planificación y EDT | Del requisito al plan y al precio | 94 | PMBOK, requisitos, alcance, exclusiones, EDT, cronograma, PERT, ruta crítica, costo y tarifa |
| **FEP03** · Estimación de Software | Cuánto esfuerzo y costo tiene el software | 75 | Punto Función, Punto de Casos de Uso, factores TCF y EF, horas por etapa, ejemplo completo |
| **FEP04** · Gestión de Riesgos TIC | Convertir el riesgo en decisiones de la oferta | 127 | Riesgo, matriz, RBS, registro, valor esperado, reserva, estrategias, riesgos de la licitación |
| **FEP05** · Sala de Servidores | Diseñar la sala física on-premise | 80 | TIER, PUE, recintos, seguridad física, energía, clima, racks, cableado, servidores |

**Caso transversal:** la *Municipalidad de Costa Azul* (licitación 3456-12-LP26, Integra TIC SpA) se usa como ejemplo en [FEP03 · 57–69](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-57) (estimación) y [FEP04 · 13](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-13) y siguientes (riesgos).

---

## 2 · Índice temático

### 2.1 Gestión de proyectos y licitación (base PMBOK)

| Tema | Dónde ir | También en |
|---|---|---|
| Qué es un proyecto vs. una operación | [FEP02 · 3](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-3) | — |
| PMBOK: 5 grupos de procesos y 10 áreas | [FEP02 · 4–7](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-4) | [FEP04 · 16](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-16) (procesos de riesgo) |
| Ciclo de vida predictivo, adaptativo e híbrido | [FEP02 · 8](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-8) | — |
| Triple restricción | [FEP02 · 9](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-9) | — |
| Plan para la dirección y líneas base | [FEP02 · 10](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-10) | [FEP02 · 46](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-46) (línea base del alcance) |
| Interesados, patrocinador, matriz poder–interés | [FEP02 · 11](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-11) | — |
| Documentos de la licitación (bases, consultas, oferta, contrato) | [FEP02 · 12](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-12) | [FEP04 · 72–74](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-72) |
| Línea de tiempo de la licitación y dónde actuar | [FEP04 · 73](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-73) | — |
| Qué se evalúa en la propuesta (pauta, criterios) | [FEP01 · 5](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-5), [FEP01 · 273](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-273) | [FEP04 · 117–121](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-117) |
| Cómo presentar (tiempos) | [FEP01 · 285](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-285) | [FEP04 · 122](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-122) |
| Por qué fallan los proyectos TIC | [FEP04 · 11](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-11) | — |

### 2.2 Requisitos

| Tema | Dónde ir | También en |
|---|---|---|
| Qué es un requisito (IEEE 610.12) | [FEP02 · 15](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-15) | — |
| Por qué importan (costo ×100) | [FEP02 · 16](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-16) | — |
| Ingeniería de requisitos: desarrollo y gestión | [FEP02 · 17](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-17) | — |
| Tipos de requisito (PMBOK) | [FEP02 · 18](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-18) | — |
| Funcionales vs. no funcionales | [FEP02 · 19](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-19) | [FEP01 · 13–15](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-13) (atributos de calidad) |
| FURPS+ | [FEP02 · 20](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-20) | — |
| Quién provee los requisitos | [FEP02 · 21](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-21) | — |
| Técnicas de extracción | [FEP02 · 22–23](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-22) | — |
| Las 4 preguntas del analista | [FEP02 · 24](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-24) | — |
| ERS: qué incluye y qué no | [FEP02 · 25](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-25) | — |
| Características de una buena ERS | [FEP02 · 26–27](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-26) | — |
| Redacción SMART y ambigüedad | [FEP02 · 28–29](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-28) | [FEP01 · 15](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-15) (redactar atributos con número) |
| Priorización (MoSCoW), trazabilidad, línea base | [FEP02 · 30](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-30) | [FEP01 · 277](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-277) (matriz requisito → componente) |
| Requisitos que nacen de un riesgo | [FEP04 · 91](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-91) | — |

### 2.3 Alcance

| Tema | Dónde ir | También en |
|---|---|---|
| Gestión del alcance (todo y sólo lo requerido) | [FEP02 · 33](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-33) | — |
| Alcance del producto vs. del proyecto | [FEP02 · 34](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-34) | — |
| Los 6 procesos del alcance y sus planes | [FEP02 · 35–36](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-35) | — |
| Enunciado del alcance (6 contenidos) | [FEP02 · 37](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-37) | — |
| Entregables y criterios de aceptación | [FEP02 · 38](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-38) | — |
| Exclusiones explícitas | [FEP02 · 39](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-39) | [FEP04 · 81](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-81) (palanca «excluir») |
| Supuestos y restricciones | [FEP02 · 40](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-40) | [FEP04 · 31](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-31), [FEP04 · 80](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-80) |
| Las 11 preguntas de la formulación | [FEP02 · 41–42](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-41) | — |
| Diagrama de contexto | [FEP02 · 43](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-43) | — |
| Validar vs. controlar el alcance | [FEP02 · 44](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-44) | — |
| Scope creep vs. gold plating | [FEP02 · 45](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-45) | — |
| Solicitud de cambio | [FEP02 · 47](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-47) | — |
| Cómo un riesgo cambia el alcance | [FEP04 · 89–90](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-89) | — |

### 2.4 EDT y cronograma

| Tema | Dónde ir | También en |
|---|---|---|
| Qué es la EDT/WBS y para qué sirve | [FEP02 · 50–51](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-50) | — |
| Regla del 100% | [FEP02 · 52](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-52) | — |
| La EDT no tiene secuencia | [FEP02 · 53](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-53) | — |
| Criterios de descomposición y hasta qué nivel | [FEP02 · 54–55](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-54) | — |
| Paquete de trabajo (regla 8/80) | [FEP02 · 56](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-56) | — |
| Diccionario de la EDT y código de cuentas | [FEP02 · 57–58](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-57) | — |
| Los 5 pasos para hacer la EDT | [FEP02 · 59](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-59) | — |
| Matriz RACI | [FEP02 · 60](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-60) | — |
| Procesos y plan del cronograma | [FEP02 · 63–64](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-63) | — |
| Actividades e hitos | [FEP02 · 65–66](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-65) | — |
| Dependencias FS/SS/FF/SF, adelanto y retraso | [FEP02 · 67–69](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-67) | — |
| Diagrama de red | [FEP02 · 70](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-70) | — |
| Esfuerzo vs. duración | [FEP02 · 71–73](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-71) | [FEP03 · 53](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-53), [FEP03 · 72](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-72) |
| Técnicas de estimación de duración | [FEP02 · 74](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-74) | — |
| Tres valores y PERT (con ejemplo) | [FEP02 · 75–76](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-75) | [FEP04 · 52](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-52) |
| Reservas de tiempo | [FEP02 · 77](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-77) | — |
| Ruta crítica, cálculo de fechas y holgura | [FEP02 · 78–81](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-78) | — |
| Comprimir, nivelar, Gantt | [FEP02 · 82](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-82) | — |
| Controlar el cronograma | [FEP02 · 83](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-83) | — |
| Qué plazo comprometer (P80, simulación) | [FEP04 · 53](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-53) | [FEP02 · 76](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-76) |
| Acciones de riesgo dentro de la EDT y el cronograma | [FEP04 · 67](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-67), [FEP04 · 94](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-94) | — |

### 2.5 Estimación, costos y precio

| Tema | Dónde ir | También en |
|---|---|---|
| Por qué medir el tamaño del software | [FEP03 · 3–4](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-3) | — |
| Tamaño → esfuerzo → plazo → costo | [FEP03 · 5](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-5) | [FEP02 · 86](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-86) |
| Métodos de estimación y cuándo usar cada uno | [FEP03 · 7](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-7) | [FEP02 · 88](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-88) |
| En qué momento de la licitación se estima | [FEP03 · 8](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-8) | — |
| Qué queda fuera de la métrica funcional | [FEP03 · 9](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-9) | — |
| Estimación ascendente vs. descendente | [FEP02 · 87](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-87) | — |
| Cono de la incertidumbre | [FEP02 · 89](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-89) | — |
| **Punto Función** (fórmula, categorías, pesos, TCF) | [FEP03 · 13–19](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-13) | — |
| **Punto de Casos de Uso** (fórmulas) | [FEP03 · 22–25](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-22) | — |
| Peso de actores (UAW) | [FEP03 · 26–27](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-26) | — |
| Transacciones y peso de casos de uso (UUCW) | [FEP03 · 28–31](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-28) | — |
| Ejemplo mínimo y errores de conteo | [FEP03 · 32–33](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-32) | — |
| Factores técnicos (TCF) | [FEP03 · 38–41](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-38) | — |
| Factores de ambiente (EF) | [FEP03 · 42–45](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-42) | — |
| Factor de conversión (20 / 28 h) | [FEP03 · 48–50](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-48) | — |
| Distribución por etapas (10/20/40/15/15) y lectura A/B | [FEP03 · 51–52](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-51) | — |
| **Ejemplo completo en 10 pasos** | [FEP03 · 58–69](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-58) | — |
| Análisis de sensibilidad de la estimación | [FEP03 · 68](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-68) | [FEP04 · 54](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-54) |
| De costo a tarifa (cadena) | [FEP02 · 90](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-90) | [FEP03 · 54](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-54) |
| Costos que no son horas (licencias, garantías, seguros) | [FEP02 · 91](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-91) | [FEP04 · 76](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-76) |
| Contingencia vs. reserva de gestión vs. margen | [FEP02 · 92](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-92) | [FEP04 · 49](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-49) |
| Errores de costeo | [FEP02 · 93](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-93) | [FEP03 · 55](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-55) |
| Convertir a UF | [FEP03 · 67](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-67) | — |
| Esfuerzo ≠ plazo, costo ≠ venta | [FEP03 · 72](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-72) | — |
| Reserva de contingencia calculada desde los riesgos | [FEP04 · 47–48](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-47) | — |
| Cómo se refleja el riesgo en la oferta económica | [FEP04 · 97](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-97) | — |
| Costo de la arquitectura en la nube | [FEP01 · 287–298](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-287) | [FEP01 · 139–140](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-139) |
| CAPEX vs. OPEX, costo on-premise | [FEP01 · 92](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-92), [FEP01 · 139](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-139) | [FEP05 · 22](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-22) |

### 2.6 Arquitectura lógica

| Tema | Dónde ir | También en |
|---|---|---|
| Qué es (y no es) la arquitectura | [FEP01 · 7–12](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-7) | — |
| Atributos de calidad ISO/IEC 25010 | [FEP01 · 13–15](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-13) | [FEP01 · 162–175](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-162) |
| Vistas y lógica vs. física | [FEP01 · 16–17](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-16) | — |
| Mapa de estilos | [FEP01 · 20](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-20) | — |
| Monolito y monolito modular | [FEP01 · 21–24](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-21) | — |
| Cliente-servidor | [FEP01 · 25–27](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-25) | — |
| 3 capas / N capas, capas vs. niveles | [FEP01 · 28–31](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-28) | — |
| MVC | [FEP01 · 32–33](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-32) | — |
| Microservicios | [FEP01 · 34–35](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-34), [FEP01 · 41–44](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-41) | — |
| APIs, REST, API Gateway, resiliencia | [FEP01 · 36–40](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-36) | — |
| Eventos (EDA), streaming, CQRS | [FEP01 · 45–48](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-45) | — |
| Hexagonal y limpia | [FEP01 · 49](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-49), [FEP01 · 57](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-57) | — |
| Integración con terceros (contrato, resiliencia, ficha) | [FEP01 · 50–56](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-50) | [FEP04 · 33](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-33) (riesgos de integración) |
| Cómo elegir el estilo | [FEP01 · 58](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-58) | — |
| Cómo dibujar el diagrama (estilos A–D) | [FEP01 · 59–67](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-59) | — |
| Ejemplos de trabajos de años anteriores | [FEP01 · 68–71](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-68) | — |
| Cómo un riesgo cambia la arquitectura | [FEP04 · 92–93](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-92) | — |

### 2.7 Arquitectura física, infraestructura y nube

| Tema | Dónde ir | También en |
|---|---|---|
| Qué es la arquitectura física | [FEP01 · 74](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-74) | — |
| Modelo OSI aplicado | [FEP01 · 75–77](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-75) | [FEP01 · 196](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-196) (seguridad por capa) |
| Del diagrama lógico al de despliegue | [FEP01 · 78](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-78) | — |
| Topología on-premise, DMZ, segmentación | [FEP01 · 79–81](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-79) | — |
| Data center (visión general) | [FEP01 · 82](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-82) | **FEP05 completo** |
| Virtualización, VM vs. contenedor | [FEP01 · 83–85](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-83) | [FEP05 · 74](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-74) |
| Dimensionamiento (CPU, RAM, disco, red) | [FEP01 · 86–88](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-86) | [FEP05 · 58](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-58), [FEP05 · 70](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-70) |
| Motores de BD y tipos de almacenamiento | [FEP01 · 89–91](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-89) | [FEP05 · 75](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-75) |
| On-premise vs. nube; cuándo on-premise | [FEP01 · 93–94](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-93), [FEP01 · 138](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-138) | — |
| Kubernetes: masters, workers, quórum | [FEP01 · 95–101](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-95) | — |
| Hipervisor: cuándo se cotiza | [FEP01 · 102–104](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-102) | — |
| RAID (niveles, factor de compra, hot spare) | [FEP01 · 105–115](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-105) | — |
| Lista de verificación para la oferta | [FEP01 · 116–117](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-116) | — |
| IaaS / PaaS / SaaS y otros *aaS | [FEP01 · 120–126](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-120) | — |
| Modelos de despliegue, regiones, zonas, red virtual | [FEP01 · 127–131](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-127) | — |
| Serverless | [FEP01 · 132–133](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-132), [FEP01 · 147](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-147) | — |
| Contenedores y orquestación | [FEP01 · 134–137](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-134) | — |
| Catálogo de servicios (AWS/Azure) | [FEP01 · 141–145](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-141) | — |
| Modelos de cómputo y cómo elegir | [FEP01 · 146–153](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-146) | — |
| Arquitectura de referencia AWS, Azure e híbrida | [FEP01 · 154–160](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-154) | — |

### 2.8 Calidad de servicio y continuidad

| Tema | Dónde ir | También en |
|---|---|---|
| Escalabilidad vertical/horizontal, autoescalado | [FEP01 · 163–166](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-163) | — |
| Balanceo de carga | [FEP01 · 167](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-167) | — |
| Alta disponibilidad y los «nueves» | [FEP01 · 168–171](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-168) | [FEP05 · 6](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-6), [FEP05 · 12](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-12) (TIER) |
| Observabilidad y rendimiento | [FEP01 · 172–173](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-172) | [FEP01 · 260](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-260) |
| SLA / SLO / SLI | [FEP01 · 174](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-174) | [FEP04 · 95](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-95) |
| Activo-pasivo y activo-activo (frío/tibio/caliente) | [FEP01 · 177–181](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-177) | — |
| RTO y RPO | [FEP01 · 180](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-180) | [FEP05 · 77](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-77) |
| Replicación síncrona/asíncrona y topologías | [FEP01 · 182–187](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-182) | — |
| Failover y failback | [FEP01 · 188](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-188) | — |
| Respaldo vs. replicación, tipos, política, restauración | [FEP01 · 189–192](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-189) | — |
| Redundancia N, N+1, 2N (infraestructura física) | [FEP05 · 7](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-7), [FEP05 · 13](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-13) | — |

### 2.9 Seguridad e identidad

| Tema | Dónde ir | También en |
|---|---|---|
| Defensa en profundidad | [FEP01 · 196](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-196) | [FEP05 · 39](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-39) (seguridad física por capas) |
| Superficie de exposición | [FEP01 · 197](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-197) | — |
| Capa de seguridad de una solución expuesta (WAF, etc.) | [FEP01 · 198](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-198) | — |
| Identidad, acceso y protección de datos | [FEP01 · 199–200](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-199) | — |
| Trabajo mixto / home office / VPN | [FEP01 · 201–204](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-201) | — |
| Monitoreo, incidentes y cumplimiento | [FEP01 · 205–207](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-205) | — |
| Autenticación vs. autorización vs. sesión | [FEP01 · 210–213](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-210) | — |
| Usuarios propios y contraseñas | [FEP01 · 214–216](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-214) | — |
| LDAP / Active Directory | [FEP01 · 217–219](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-217) | — |
| Proveedor de identidad, SAML/OAuth/OIDC, Keycloak | [FEP01 · 220–225](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-220) | — |
| Sesión vs. token, JWT, refresco, cookies, logout | [FEP01 · 226–231](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-226) | — |
| HTTPS y doble factor | [FEP01 · 232–233](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-232) | — |
| Autorización e identidad de sistemas | [FEP01 · 234–235](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-234) | — |
| Cómo elegir identidad para tu caso (ClaveÚnica, etc.) | [FEP01 · 238–239](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-238) | — |
| Seguridad física: acceso, esclusa, sensores | [FEP05 · 37–41](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-37) | — |
| Ley 21.719 de datos personales | [FEP05 · 13](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-13) | [FEP04 · 47](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-47) (R-07), [FEP01 · 205](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-205) |

### 2.10 Entrega y tendencias

| Tema | Dónde ir |
|---|---|
| Por qué varios ambientes; los 4 ambientes; costo | [FEP01 · 242–244](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-242) |
| Datos en ambientes no productivos | [FEP01 · 245](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-245) |
| Promoción entre ambientes, CI/CD, canalización | [FEP01 · 246–249](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-246) |
| Estrategias de despliegue (azul-verde, canario…) | [FEP01 · 250](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-250) |
| Configuración y secretos por ambiente | [FEP01 · 251](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-251) |
| Plataformas, IaC, GitOps, DevSecOps | [FEP01 · 256–259](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-256) |
| Observabilidad, malla de servicios, edge, datos en tiempo real | [FEP01 · 260–263](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-260) |
| IA, MLOps, ética | [FEP01 · 264–266](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-264) |
| FinOps y sostenibilidad | [FEP01 · 267–268](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-267) |
| Cómo proponer innovación sin comprometerse de más | [FEP01 · 270](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-270), [FEP04 · 99](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-99) |

### 2.11 Riesgos

| Tema | Dónde ir | También en |
|---|---|---|
| Incertidumbre, riesgo y problema | [FEP04 · 3](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-3) | — |
| Amenaza vs. oportunidad | [FEP04 · 4](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-4) | [FEP04 · 60](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-60) |
| Riesgo como anexo vs. como decisión | [FEP04 · 5](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-5) | — |
| Los 5 elementos (P, I, exposición, tiempo, disparador) | [FEP04 · 6](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-6) | — |
| Escalas y matriz de exposición | [FEP04 · 7–8](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-7) | [FEP04 · 44](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-44) |
| Apetito, tolerancia y umbral | [FEP04 · 9](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-9) | — |
| Curva incertidumbre / costo de cambiar | [FEP04 · 10](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-10) | [FEP02 · 89](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-89) |
| Riesgo de proyecto, producto y negocio | [FEP04 · 12](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-12) | — |
| Los 7 procesos y el flujo | [FEP04 · 16–17](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-16) | — |
| Plan de gestión de riesgos | [FEP04 · 18](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-18) | — |
| RBS (genérica y TIC) | [FEP04 · 19–20](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-19) | — |
| Registro de riesgos (campos) | [FEP04 · 21](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-21) | [FEP04 · 112](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-112) |
| Variabilidad y ambigüedad | [FEP04 · 22](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-22) | — |
| Técnicas de identificación | [FEP04 · 28–30](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-28) | — |
| Supuestos como fuente de riesgos | [FEP04 · 31](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-31) | — |
| Lectura adversarial de las bases | [FEP04 · 32](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-32) | — |
| Catálogo de riesgos TIC | [FEP04 · 33–35](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-33) | — |
| Cómo redactar un riesgo (ejemplos) | [FEP04 · 36–38](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-36) | — |
| Análisis cualitativo vs. cuantitativo | [FEP04 · 42–45](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-42) | — |
| Valor monetario esperado y registro cuantificado | [FEP04 · 46–47](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-46) | — |
| Reserva de contingencia y de gestión | [FEP04 · 48–49](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-48) | [FEP02 · 77](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-77), [FEP02 · 92](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-92) |
| Árbol de decisión y punto de indiferencia | [FEP04 · 50–51](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-50) | — |
| Tres valores, simulación y sensibilidad | [FEP04 · 52–54](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-52) | — |
| Estrategias ante amenazas y oportunidades | [FEP04 · 59–60](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-59) | — |
| Cómo elegir estrategia y cuánto gastar | [FEP04 · 61–63](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-61) | — |
| Residual, secundario, disparador, contingencia, reversa | [FEP04 · 64–65](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-64) | — |
| Implementar y monitorear | [FEP04 · 67–68](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-67) | — |
| Riesgos de la licitación y del contrato | [FEP04 · 72–77](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-72) | — |
| Las 5 palancas (consultar, suponer, excluir, rediseñar, no ofertar) | [FEP04 · 78–83](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-78) | — |
| Trazabilidad riesgo → solución | [FEP04 · 88–96](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-88) | — |
| Ficha de riesgo completa | [FEP04 · 105](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-105) | — |
| Las 4 etapas de una acción | [FEP04 · 106–111](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-106) | — |
| Gobierno durante el contrato y cierre | [FEP04 · 113–114](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-113) | — |
| Coherencia con la estimación (factor E6) | [FEP03 · 45](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-45) | [FEP03 · 64](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-64) |

### 2.12 Sala de servidores (infraestructura física)

| Tema | Dónde ir | También en |
|---|---|---|
| Qué es un datacenter y sus 4 funciones | [FEP05 · 2](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-2), [FEP05 · 5](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-5) | [FEP01 · 82](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-82) |
| TIER (niveles y comparación) | [FEP05 · 6](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-6), [FEP05 · 12](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-12) | — |
| Redundancia N, N+1, 2N, 2(N+1) | [FEP05 · 7](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-7), [FEP05 · 13](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-13) | — |
| PUE y DCiE | [FEP05 · 8–10](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-8) | — |
| Tabla de traducción datacenter → sala | [FEP05 · 11](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-11) | — |
| Normas (TIA-942, ASHRAE, NFPA, NCh, Ley 21.719) | [FEP05 · 13](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-13) | [FEP05 · 79](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-79) |
| Principios del programa de recintos | [FEP05 · 15](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-15), [FEP05 · 17](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-17) | — |
| Plano por zonas y líneas de acceso | [FEP05 · 18–20](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-18) | — |
| Sala de servidores, NOC y clima | [FEP05 · 21](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-21) | — |
| Recintos de energía | [FEP05 · 22](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-22) | — |
| MMR, extinción y custodia | [FEP05 · 23](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-23) | — |
| Recintos de apoyo y baños | [FEP05 · 24](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-24) | — |
| Adyacencias | [FEP05 · 26](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-26) | — |
| Los 13 recintos (m²) | [FEP05 · 27](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-27) | — |
| Distribución y ejemplos reales (SONDA, Google) | [FEP05 · 29–36](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-29) | — |
| Control de acceso (4 líneas, esclusa, antipassback) | [FEP05 · 39–40](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-39), [FEP05 · 44](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-44) | — |
| Sensores y monitoreo (VESDA, DCIM) | [FEP05 · 41](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-41) | — |
| Extinción por gas y agentes | [FEP05 · 42–44](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-42) | — |
| Cadena eléctrica | [FEP05 · 47–48](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-47) | — |
| UPS, generador y baterías | [FEP05 · 49](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-49) | — |
| Carga térmica (1 kW = 3.412 BTU/h) | [FEP05 · 50–51](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-50) | — |
| Pasillo frío/caliente | [FEP05 · 52–54](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-52) | — |
| Tecnologías de clima y free cooling | [FEP05 · 55–56](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-55) | — |
| Piso técnico vs. distribución aérea; peso | [FEP05 · 57](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-57) | — |
| Dimensionar carga eléctrica y térmica | [FEP05 · 58](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-58) | — |
| La U y la elevación del rack | [FEP05 · 61–64](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-61) | — |
| Chasis y tipos de gabinete | [FEP05 · 65–66](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-65) | — |
| Cableado, topología TIA-942, medios | [FEP05 · 67–69](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-67) | — |
| Cuántos racks necesito | [FEP05 · 70](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-70) | — |
| Formatos de servidor (rack, blade, HCI) | [FEP05 · 72–73](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-72) | — |
| Virtualización en la sala | [FEP05 · 74](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-74) | [FEP01 · 83–85](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-83) |
| DAS / NAS / SAN | [FEP05 · 75](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-75) | [FEP01 · 91](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-91) |
| Parámetros a declarar en la propuesta | [FEP05 · 77](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-77) | [FEP01 · 278–279](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-278) |

---

## 3 · Preguntas frecuentes: dónde está la respuesta

| Si te preguntas… | Ve a |
|---|---|
| ¿Qué tengo que entregar en el Informe y Presentación 1? | [FEP01 · 5](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-5), [FEP01 · 299](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-299) |
| ¿Cómo justifico por qué elegí esta arquitectura? | [FEP01 · 58](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-58), [FEP01 · 280](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-280) |
| ¿Monolito o microservicios para mi caso? | [FEP01 · 22](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-22), [FEP01 · 41](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-41), [FEP01 · 58](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-58) |
| ¿Cómo dibujo mi diagrama de arquitectura? | [FEP01 · 59–67](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-59) (y ejemplos en 68–71) |
| ¿Cómo escribo un requisito no funcional o atributo con número? | [FEP01 · 15](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-15), [FEP02 · 19](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-19), [FEP02 · 38](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-38) |
| ¿Cuántos servidores, cuánta RAM y cuánto disco necesito? | [FEP01 · 86–88](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-86) |
| ¿Cuántos discos compro con RAID 10? | [FEP01 · 111](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-111), [FEP01 · 114](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-114) |
| ¿Por qué 3 nodos master en Kubernetes? | [FEP01 · 99](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-99) |
| ¿Nube u on-premise? | [FEP01 · 94](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-94), [FEP01 · 138–140](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-138) |
| ¿Qué servicio de nube (VM, contenedores, funciones) uso? | [FEP01 · 153](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-153) |
| ¿Cuánto me cuesta la nube al mes y cómo va al flujo de caja? | [FEP01 · 287–297](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-287) |
| ¿Qué disponibilidad (99,9%…) puedo comprometer? | [FEP01 · 170–171](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-170), [FEP01 · 174](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-174) |
| ¿Cómo se calcula la disponibilidad? | [FEP01 · 171](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-171) |
| ¿Qué es RTO/RPO y cómo lo decido? | [FEP01 · 179–181](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-179) |
| ¿Basta con replicar o necesito respaldo? | [FEP01 · 189–191](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-189) |
| ¿Qué expongo a Internet y qué no? | [FEP01 · 197](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-197) |
| ¿Cómo hago el login (ClaveÚnica, LDAP, Keycloak)? | [FEP01 · 238–239](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-238) |
| ¿Sesión en servidor o JWT? | [FEP01 · 226–229](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-226) |
| ¿Cuántos ambientes cotizo y de qué tamaño? | [FEP01 · 243–244](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-243) |
| ¿Qué es la diferencia entre alcance del producto y del proyecto? | [FEP02 · 34](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-34) |
| ¿Cómo escribo exclusiones y supuestos? | [FEP02 · 39–40](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-39), [FEP04 · 80–81](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-80) |
| ¿Cómo armo la EDT y hasta qué nivel la descompongo? | [FEP02 · 50–59](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-50) |
| ¿Cómo calculo la ruta crítica y la holgura? | [FEP02 · 78–81](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-78) |
| ¿Cómo uso PERT y qué plazo comprometo? | [FEP02 · 75–76](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-75), [FEP04 · 53](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-53) |
| ¿Cómo calculo la tarifa por hora? | [FEP02 · 90](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-90), [FEP03 · 54](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-54) |
| ¿Qué costos se me olvidan además de las horas? | [FEP02 · 91](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-91), [FEP02 · 93](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-93), [FEP03 · 9](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-9) |
| ¿Cuánto esfuerzo tiene mi sistema (UCP paso a paso)? | [FEP03 · 58–69](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-58) |
| ¿Cómo cuento actores y casos de uso? | [FEP03 · 26–33](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-26) |
| ¿Qué valor pongo a los factores técnicos y de ambiente? | [FEP03 · 38–45](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-38) |
| ¿Uso 20 o 28 horas por punto? | [FEP03 · 49–50](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-49), [FEP03 · 64](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-64) |
| ¿El esfuerzo calculado es total o sólo programación? | [FEP03 · 52](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-52), [FEP03 · 65](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-65) |
| ¿Cómo paso de horas a pesos y UF? | [FEP03 · 67](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-67) |
| ¿Cómo escribo bien un riesgo? | [FEP04 · 36–37](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-36) |
| ¿Cuántos riesgos pongo en el registro? | [FEP04 · 38](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-38), [FEP04 · 112](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-112) |
| ¿Cómo calculo la reserva de contingencia? | [FEP04 · 46–48](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-46) |
| ¿Qué estrategia elijo para cada riesgo? | [FEP04 · 59–62](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-59) |
| ¿Qué hago con frases ambiguas de las bases? | [FEP04 · 32](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-32), [FEP04 · 78–79](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-78) |
| ¿Cuándo conviene no presentarse? | [FEP04 · 83](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-83) |
| ¿Cómo muestro que el riesgo cambió mi solución? | [FEP04 · 88–96](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-88) |
| ¿Cómo estructuro el capítulo de riesgos? | [FEP04 · 118–119](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-118) |
| ¿Qué TIER apunto y qué disponibilidad da? | [FEP05 · 6](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-6), [FEP05 · 12](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-12) |
| ¿Qué recintos debe tener mi sala y cuántos m²? | [FEP05 · 27](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-27) |
| ¿Cómo dimensiono UPS, generador y clima? | [FEP05 · 49](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-49), [FEP05 · 51](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-51), [FEP05 · 58](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-58) |
| ¿Cuántos racks dibujo en el plano? | [FEP05 · 70](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-70) |
| ¿Qué parámetros declaro de la sala? | [FEP05 · 77](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-77) |

---

## 4 · Índice alfabético de términos

| Término | Dónde ir |
|---|---|
| 11 preguntas de la formulación | [FEP02 · 41–42](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-41) |
| 2N / 2(N+1) | [FEP05 · 7](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-7), [FEP05 · 13](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-13) |
| Activo-activo / activo-pasivo | [FEP01 · 177–181](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-177) |
| Actor (UCP) | [FEP03 · 26–27](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-26) |
| Adyacencias (sala) | [FEP05 · 26](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-26) |
| Ambientes (dev, QA, preprod, prod) | [FEP01 · 242–246](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-242) |
| Ambigüedad (requisitos) | [FEP02 · 29](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-29); (riesgo) [FEP04 · 22](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-22) |
| Antipassback / esclusa | [FEP05 · 40](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-40), [FEP05 · 44](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-44) |
| API, REST, API Gateway | [FEP01 · 36–40](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-36) |
| Apetito, tolerancia y umbral | [FEP04 · 9](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-9) |
| Árbol de decisión | [FEP04 · 50–51](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-50) |
| ASHRAE TC 9.9 | [FEP05 · 13](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-13), [FEP05 · 51](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-51) |
| ATS / TTA (transferencia) | [FEP05 · 47–49](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-47) |
| Atributos de calidad | [FEP01 · 13–15](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-13) |
| Autenticación / autorización | [FEP01 · 211](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-211), [FEP01 · 234](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-234) |
| AWS / Azure | [FEP01 · 141–145](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-141), [FEP01 · 157–158](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-157) |
| Azul-verde, canario (despliegue) | [FEP01 · 250](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-250) |
| Bases administrativas / técnicas | [FEP02 · 12](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-12) |
| Baterías (VRLA, litio) | [FEP05 · 49](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-49) |
| Blade / HCI | [FEP05 · 65](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-65), [FEP05 · 73](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-73) |
| Boleta de garantía | [FEP02 · 91](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-91) |
| CAPEX / OPEX | [FEP01 · 139](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-139) |
| Casos de uso (UUCW) | [FEP03 · 28–33](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-28) |
| CI/CD | [FEP01 · 247–249](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-247) |
| Cliente-servidor | [FEP01 · 25–27](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-25) |
| Clima de precisión | [FEP05 · 51](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-51), [FEP05 · 55](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-55) |
| Código de cuentas | [FEP02 · 58](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-58) |
| Cono de la incertidumbre | [FEP02 · 89](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-89) |
| Contenedores | [FEP01 · 84–85](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-84), [FEP01 · 134–137](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-134) |
| Contingencia (plan) | [FEP04 · 65](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-65) |
| Criterios de aceptación | [FEP02 · 38](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-38) |
| CQRS / event sourcing | [FEP01 · 48](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-48) |
| DAS / NAS / SAN | [FEP05 · 75](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-75) |
| DCIM / BMS | [FEP05 · 41](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-41) |
| Dependencias (FS, SS, FF, SF) | [FEP02 · 67–68](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-67) |
| Diagrama de contexto | [FEP02 · 43](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-43) |
| Diccionario de la EDT | [FEP02 · 57](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-57) |
| Disparador | [FEP04 · 64](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-64) |
| Disponibilidad (nueves, fórmula) | [FEP01 · 170–171](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-170) |
| DMZ / segmentación | [FEP01 · 80–81](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-80) |
| Doble factor (2FA) | [FEP01 · 233](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-233) |
| EDA (eventos) | [FEP01 · 45–47](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-45) |
| EDT / WBS | [FEP02 · 50–60](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-50) |
| EF (factor de ambiente) | [FEP03 · 42–45](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-42) |
| Elasticidad / autoescalado | [FEP01 · 166](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-166) |
| Enunciado del alcance | [FEP02 · 37](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-37) |
| ERS | [FEP02 · 25–27](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-25) |
| Escalabilidad | [FEP01 · 163–165](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-163) |
| Esfuerzo vs. duración / plazo | [FEP02 · 71](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-71), [FEP03 · 53](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-53), [FEP03 · 72](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-72) |
| Exclusiones | [FEP02 · 39](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-39), [FEP04 · 81](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-81) |
| Exposición (P × I) | [FEP04 · 6](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-6), [FEP04 · 8](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-8) |
| Extinción (FM-200, Novec, CO₂) | [FEP05 · 42–44](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-42) |
| Factor de conversión (CF) | [FEP03 · 48–50](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-48) |
| Failover / failback | [FEP01 · 188](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-188) |
| FinOps | [FEP01 · 267](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-267) |
| Free cooling | [FEP05 · 56](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-56) |
| FURPS+ | [FEP02 · 20](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-20) |
| Gantt / cronograma de hitos | [FEP02 · 82](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-82) |
| Generador | [FEP05 · 49](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-49) |
| GitOps / IaC | [FEP01 · 258](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-258) |
| Glosarios | [FEP01 · 300–307](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-300), [FEP03 · 73](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-73), [FEP04 · 124–125](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-124), [FEP05 · 78](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-78) |
| Gold plating / scope creep | [FEP02 · 45](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-45) |
| Hexagonal (arquitectura) | [FEP01 · 49](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-49) |
| Hipervisor | [FEP01 · 102–103](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-102) |
| Hitos | [FEP02 · 66](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-66) |
| Holgura | [FEP02 · 78–79](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-78) |
| IaaS / PaaS / SaaS | [FEP01 · 121–125](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-121) |
| IA en la arquitectura / MLOps | [FEP01 · 264–266](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-264) |
| Interesados / patrocinador | [FEP02 · 11](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-11) |
| ISO/IEC 25010 | [FEP01 · 13](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-13) |
| JWT / token de refresco | [FEP01 · 228–229](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-228) |
| Keycloak | [FEP01 · 223](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-223) |
| Kubernetes (master, worker, quórum) | [FEP01 · 95–101](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-95) |
| LDAP / Active Directory | [FEP01 · 217–219](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-217) |
| Lectura adversarial de las bases | [FEP04 · 32](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-32) |
| Ley 21.719 | [FEP05 · 13](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-13) |
| Línea base | [FEP02 · 10](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-10), [FEP02 · 30](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-30), [FEP02 · 46](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-46) |
| Margen | [FEP02 · 92](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-92) |
| Matriz de exposición | [FEP04 · 8](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-8), [FEP04 · 44](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-44) |
| Matriz de trazabilidad | [FEP02 · 30](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-30), [FEP01 · 277](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-277), [FEP04 · 96](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-96) |
| Microservicios | [FEP01 · 34–44](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-34) |
| MMR (acometida de comunicaciones) | [FEP05 · 23](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-23) |
| Monolito / monolito modular | [FEP01 · 21–24](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-21) |
| MoSCoW / priorización | [FEP02 · 30](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-30) |
| MVC | [FEP01 · 32–33](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-32) |
| N+1 | [FEP05 · 7](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-7) |
| NOC | [FEP05 · 21](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-21) |
| Observabilidad | [FEP01 · 172](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-172), [FEP01 · 260](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-260) |
| OpenID Connect / OAuth / SAML | [FEP01 · 221–222](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-221) |
| OSI (modelo) | [FEP01 · 75–77](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-75) |
| Oportunidades (estrategias) | [FEP04 · 60](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-60) |
| Paquete de trabajo (8/80) | [FEP02 · 56](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-56) |
| Pasillo frío / caliente | [FEP05 · 52–54](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-52) |
| PERT / tres valores | [FEP02 · 75–76](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-75) |
| Piso técnico | [FEP05 · 57](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-57) |
| PMBOK | [FEP02 · 4–7](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-4) |
| Punto de indiferencia | [FEP04 · 51](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-51) |
| Punto Función (FP, UFP, EI, EO, EQ, ILF, EIF) | [FEP03 · 13–19](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-13) |
| PUE / DCiE | [FEP05 · 8–10](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-8) |
| RACI | [FEP02 · 60](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-60) |
| RAID | [FEP01 · 105–115](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-105) |
| RBS | [FEP04 · 19–20](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-19) |
| Recintos (13) | [FEP05 · 27](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-27) |
| Registro de riesgos | [FEP04 · 21](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-21), [FEP04 · 47](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-47), [FEP04 · 112](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-112) |
| Replicación síncrona/asíncrona | [FEP01 · 183](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-183) |
| Requisitos (tipos) | [FEP02 · 18–19](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-18) |
| Reserva de contingencia / de gestión | [FEP02 · 77](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-77), [FEP02 · 92](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-92), [FEP04 · 48–49](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-48) |
| Respaldo | [FEP01 · 189–192](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-189) |
| Riesgo residual / secundario | [FEP04 · 64](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-64) |
| RTO / RPO | [FEP01 · 180](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-180) |
| Ruta crítica (CPM) | [FEP02 · 78–81](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-78) |
| Serverless / funciones | [FEP01 · 132–133](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-132), [FEP01 · 147](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-147) |
| Sesión (servidor vs. token) | [FEP01 · 226–227](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-226) |
| SLA / SLO / SLI | [FEP01 · 174](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-174) |
| SMART | [FEP02 · 28](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-28) |
| Solicitud de cambio | [FEP02 · 47](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-47) |
| Supuestos y restricciones | [FEP02 · 40](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-40), [FEP04 · 31](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-31), [FEP04 · 80](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-80) |
| Tarifa por hora | [FEP02 · 90](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-90), [FEP03 · 54](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-54) |
| TCF (factor técnico) | [FEP03 · 19](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-19) (PF), [FEP03 · 38–41](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-38) (UCP) |
| TIA-942 (topología de cableado) | [FEP05 · 68](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-68) |
| TIER I–IV | [FEP05 · 6](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-6), [FEP05 · 12](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-12) |
| ToR / EoR | [FEP05 · 68](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-68) |
| Transacción (Jacobson) | [FEP03 · 28](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-28), [FEP03 · 30](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-30) |
| Triple restricción | [FEP02 · 9](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-9) |
| U (unidad de rack) | [FEP05 · 62–64](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-62) |
| UAW / UUCW / UUCP / UCP | [FEP03 · 24–29](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-24), [FEP03 · 37](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-37) |
| UF | [FEP03 · 67](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-67) |
| UPS | [FEP05 · 48–49](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-48), [FEP05 · 58](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-58) |
| Valor monetario esperado | [FEP04 · 46](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-46) |
| Variabilidad | [FEP04 · 22](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-22) |
| VESDA | [FEP05 · 41](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-41) |
| Virtualización / VM | [FEP01 · 83–85](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-83), [FEP05 · 74](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-74) |
| VPN / trabajo remoto | [FEP01 · 203](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-203) |
| WAF | [FEP01 · 198](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-198) |

---

## 5 · Rutas por entregable

**Arquitectura (Informe 1, RA1):** [FEP01 · 4–5](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-4) (qué se pide) → [FEP01 · 273–274](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-273) (criterios y ruta de 7 pasos) → [FEP01 · 58](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-58) (elegir estilo) → [FEP01 · 59–67](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-59) (dibujar) → [FEP01 · 277](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-277) (trazabilidad) → [FEP01 · 278–279](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-278) (ficha de parámetros) → [FEP01 · 280–282](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-280) (alternativas, estándares, restricciones) → [FEP01 · 287–299](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-287) (costeo) → [FEP01 · 284](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-284) (errores a evitar).

**Alcance y plan de trabajo:** [FEP02 · 37–40](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-37) (enunciado, exclusiones, supuestos) → [FEP02 · 43](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-43) (diagrama de contexto) → [FEP02 · 50–60](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-50) (EDT y RACI) → [FEP02 · 65–81](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-65) (cronograma y ruta crítica) → [FEP04 · 53](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-53) (plazo a comprometer).

**Estimación y oferta económica:** [FEP03 · 58–69](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-58) (los 10 pasos) → [FEP03 · 52](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-52) (declarar la lectura) → [FEP02 · 90–93](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-90) (tarifa y costos que no son horas) → [FEP04 · 47–48](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-47) (reserva de contingencia) → [FEP02 · 92](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-92) (margen y precio) → [FEP03 · 72](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-72) (tres números, tres orígenes).

**Capítulo de riesgos:** [FEP04 · 123](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-123) (ruta de 8 pasos) → [FEP04 · 18–21](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-18) (plan, RBS, registro) → [FEP04 · 32–37](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-32) (identificar y redactar) → [FEP04 · 44–48](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-44) (analizar y reservar) → [FEP04 · 59–64](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-59) (responder) → [FEP04 · 78–83](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-78) (palancas de la licitación) → [FEP04 · 96](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-96) (matriz riesgo → solución) → [FEP04 · 105–106](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-105) (ficha y etapa) → [FEP04 · 118–119](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-118) (estructura y lista de cotejo).

**Sala de servidores:** [FEP05 · 11](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-11) (traducción) → [FEP05 · 27](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-27) (recintos) → [FEP05 · 18](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-18) (zonas) → [FEP05 · 40](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-40) (accesos) → [FEP05 · 47–49](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-47) y 58 (energía) → [FEP05 · 51–56](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-51) (clima) → [FEP05 · 61–64](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-61) y 70 (racks) → [FEP05 · 77](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-77) (parámetros) → [FEP05 · 80](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-80) (tarea).

---

## Anexo · Índice completo de diapositivas

Cada número enlaza a la diapositiva en la transcripción. Las líneas **▶** marcan el inicio de cada sección.


### FEP01 · Arquitectura de Software

- [1](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-1) Portada
- [2](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-2) El recorrido
- [3](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-3) El recorrido · continuación 1
- [4](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-4) Por qué esto importa en el curso
- [5](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-5) Lo que se le pedirá en el Informe y Presentación 1

**[6](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-6) ▶ SECCIÓN 1 · Fundamentos**

- [7](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-7) El concepto
- [8](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-8) Definición
- [9](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-9) No responde sólo a requisitos estructurales
- [10](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-10) El objetivo real
- [11](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-11) Tres cosas que se confunden
- [12](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-12) Las decisiones son el producto
- [13](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-13) Atributos de calidad · ISO/IEC 25010
- [14](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-14) Los atributos que se compran y se venden
- [15](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-15) Cómo se escribe un atributo de calidad
- [16](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-16) Las vistas de una arquitectura
- [17](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-17) Arquitectura lógica vs. arquitectura física
- [18](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-18) Recomendaciones para profundizar · Sección 1 · Fundamentos

**[19](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-19) ▶ SECCIÓN 2 · Arquitectura lógica**

- [20](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-20) Mapa de estilos arquitectónicos
- [21](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-21) Arquitectura monolítica
- [22](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-22) Monolito · ventajas y desventajas
- [23](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-23) El punto medio: monolito modular
- [24](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-24) Monolito · en la vida real
- [25](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-25) Arquitectura cliente – servidor
- [26](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-26) Cliente – servidor mejorada
- [27](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-27) Cliente – servidor · en la vida real
- [28](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-28) Arquitectura en 3 capas
- [29](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-29) Capas (layers) y niveles (tiers)
- [30](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-30) Arquitectura N capas
- [31](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-31) Capas y N capas · en la vida real
- [32](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-32) MVC y sus variantes
- [33](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-33) MVC · en la vida real
- [34](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-34) Arquitectura de microservicios
- [35](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-35) Microservicios · vista general
- [36](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-36) API · Application Programming Interface
- [37](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-37) APIs REST
- [38](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-38) Otras formas de comunicar servicios
- [39](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-39) API Gateway
- [40](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-40) Patrones de resiliencia
- [41](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-41) Microservicios · lo que se gana y lo que se paga
- [42](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-42) Microservicios · en la vida real
- [43](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-43) Los datos en una arquitectura distribuida
- [44](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-44) SOA y microservicios
- [45](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-45) Arquitectura basada en eventos (EDA)
- [46](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-46) EDA · beneficios y cuándo usarla
- [47](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-47) Eventos · en la vida real
- [48](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-48) Streaming, CQRS y event sourcing
- [49](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-49) Arquitectura hexagonal y limpia
- [50](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-50) La capa de integración
- [51](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-51) Estilos de integración con terceros
- [52](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-52) Los terceros que suelen aparecer
- [53](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-53) El contrato de integración
- [54](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-54) Resiliencia frente al tercero
- [55](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-55) Seguridad de la integración
- [56](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-56) Ficha de integración para el informe
- [57](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-57) Hexagonal · en la vida real
- [58](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-58) Cómo elegir el estilo
- [59](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-59) No hay una sola forma de dibujarla
- [60](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-60) Cuál estilo conviene
- [61](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-61) Reglas para que el diagrama se entienda
- [62](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-62) Estilo A · actores en columnas, capas en filas
- [63](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-63) Estilo A · cuándo usarlo y qué cuidar
- [64](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-64) Estilo B · bandas por capa, actores arriba
- [65](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-65) Estilo C · capas con microservicios y stack lateral
- [66](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-66) Estilo D · columnas verticales por capa
- [67](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-67) Los cuatro estilos, en una frase
- [68](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-68) Ejemplo de Trabajo de años anteriores
- [69](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-69) Ejemplo de Trabajo de años anteriores
- [70](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-70) Ejemplo de Trabajo de años anteriores
- [71](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-71) Ejemplo de Trabajo de años anteriores
- [72](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-72) Recomendaciones para profundizar · Sección 2 · Arquitectura lógica

**[73](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-73) ▶ SECCIÓN 3 · Arquitectura física**

- [74](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-74) ¿Qué es la arquitectura física?
- [75](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-75) Las 7 capas del modelo OSI
- [76](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-76) Su arquitectura, mapeada sobre OSI
- [77](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-77) Para qué le sirve OSI en la oferta
- [78](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-78) Del diagrama lógico al de despliegue
- [79](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-79) Topología clásica on-premise
- [80](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-80) Segmentación de la red
- [81](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-81) Las zonas de red, en un diagrama
- [82](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-82) El data center
- [83](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-83) Del servidor físico a la virtualización
- [84](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-84) ¿Qué es un contenedor?
- [85](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-85) Máquina virtual vs. contenedor
- [86](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-86) Dimensionar: de la demanda al hardware
- [87](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-87) Parámetros de dimensionamiento
- [88](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-88) Dimensionamiento de la base de datos
- [89](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-89) Motor, base de datos y almacenamiento
- [90](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-90) Motores más usados y cuándo elegir cada uno
- [91](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-91) Tipos de almacenamiento
- [92](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-92) El costo real de una solución on -premise
- [93](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-93) Cómo se dibuja una arquitectura física
- [94](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-94) Cuándo on-premise sigue siendo la respuesta correcta
- [95](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-95) Tres piezas que hay que entender antes
- [96](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-96) Plano de control y plano de trabajo
- [97](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-97) Qué hace exactamente un nodo Master
- [98](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-98) Qué hace exactamente un nodo Worker
- [99](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-99) ¿Por qué tres masters, y no uno ni dos?
- [100](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-100) El quórum, en un diagrama
- [101](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-101) ¿Y cuántos workers?
- [102](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-102) ¿Por qué se necesita un hipervisor?
- [103](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-103) Cuándo sí y cuándo no se cotiza un hipervisor
- [104](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-104) Las capas, de abajo hacia arriba
- [105](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-105) RAID: qué es y qué no es
- [106](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-106) RAID 0 · división en franjas (striping)
- [107](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-107) RAID 1 · espejo (mirroring)
- [108](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-108) RAID 5 · franjas con paridad distribuida
- [109](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-109) RAID 6 · doble paridad
- [110](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-110) RAID 10 · espejo y franjas combinados
- [111](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-111) Los niveles RAID, comparados
- [112](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-112) El disco de reserva (hot spare) y la reconstrucción
- [113](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-113) Tres reglas de disco de un documento real, explicadas
- [114](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-114) Por qué «la mitad de la capacidad total»
- [115](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-115) Cabina compartida o discos en cada servidor
- [116](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-116) Lista de verificación para su oferta
- [117](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-117) Lista de verificación para su oferta · continuación 1
- [118](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-118) Recomendaciones para profundizar · Sección 3 · Arquitectura física y dimensionamiento

**[119](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-119) ▶ SECCIÓN 4 · La nube**

- [120](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-120) Aplicaciones en la nube
- [121](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-121) IaaS · PaaS · SaaS · ¿quién administra qué?
- [122](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-122) Las tres familias, en detalle
- [123](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-123) Otros servicios en la nube
- [124](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-124) Cuándo conviene contratar cada servicio
- [125](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-125) Cuándo conviene contratar cada servicio · continuación 1
- [126](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-126) Cómo se decide entre construir y contratar
- [127](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-127) Modelos de despliegue
- [128](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-128) La geografía de la nube
- [129](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-129) La red virtual
- [130](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-130) Ejemplo · aplicación de tres capas en la nube
- [131](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-131) Los componentes del ejemplo
- [132](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-132) Arquitectura sin servidores · serverless
- [133](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-133) Serverless · cuándo conviene y cuándo no
- [134](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-134) Administrar contenedores · por qué
- [135](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-135) Orquestación de contenedores
- [136](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-136) Ciclo de vida y seguridad de las imágenes
- [137](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-137) ¿Necesita usted un orquestador?
- [138](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-138) On-premise vs. nube · comparación honesta
- [139](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-139) CAPEX, OPEX y el costo total
- [140](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-140) Los costos de la nube que se olvidan
- [141](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-141) Del concepto al nombre del servicio
- [142](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-142) Catálogo 1 · red, entrega y perímetro
- [143](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-143) Catálogo 2 · cómputo y contenedores
- [144](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-144) Catálogo 3 · datos, almacenamiento y observabilidad
- [145](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-145) Catálogo 4 · conectividad híbrida, identidad y secretos
- [146](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-146) Antes de comparar · las cinco palabras
- [147](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-147) ¿«Funciones» es lo mismo que «serverless»?
- [148](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-148) Cuatro modelos de cómputo · quién administra qué
- [149](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-149) Los cuatro modelos, comparados
- [150](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-150) Máquina virtual vs. hosting de contenedores
- [151](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-151) Fargate vs. funciones serverless
- [152](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-152) Cómo se cobra cada modelo
- [153](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-153) Cómo elegir el modelo de cómputo
- [154](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-154) Arquitectura de referencia · primero los conceptos
- [155](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-155) Qué hace cada elemento y por qué está
- [156](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-156) Qué hace cada elemento y por qué está · continuación 1
- [157](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-157) Arquitectura física de referencia · AWS
- [158](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-158) La misma arquitectura, traducida a Azure
- [159](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-159) Arquitectura híbrida · unir la nube con el data center
- [160](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-160) Cómo declarar todo esto en la oferta
- [161](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-161) Recomendaciones para profundizar · Sección 4 · La nube

**[162](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-162) ▶ SECCIÓN 5 · Atributos de calidad**

- [163](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-163) Escalabilidad
- [164](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-164) Escalamiento vertical · scaling up
- [165](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-165) Escalamiento horizontal · scaling out
- [166](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-166) Elasticidad y autoescalado
- [167](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-167) Balanceo de carga de trabajo
- [168](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-168) Alta disponibilidad
- [169](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-169) Lo que hay que examinar
- [170](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-170) Los «nueves» de la disponibilidad
- [171](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-171) Cómo se calcula la disponibilidad
- [172](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-172) Detección de errores y observabilidad
- [173](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-173) Rendimiento: cómo se mide de verdad
- [174](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-174) SLA, SLO y SLI · lo que se firma
- [175](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-175) Recomendaciones para profundizar · Sección 5 · Atributos de calidad

**[176](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-176) ▶ SECCIÓN 6 · Continuidad**

- [177](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-177) Activo – Pasivo · qué significa
- [178](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-178) Activo – Activo · qué significa
- [179](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-179) Pasivo frío, tibio y caliente
- [180](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-180) RTO y RPO · los dos números
- [181](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-181) Activo-Activo vs. Activo-Pasivo · decidir
- [182](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-182) El problema de sincronizar datos
- [183](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-183) Replicación sincrónica vs. asincrónica
- [184](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-184) Topologías de replicación
- [185](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-185) Escenario A · nube + on-premise
- [186](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-186) Escenario B · nube + nube
- [187](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-187) Conflictos: cuando dos sitios escriben lo mismo
- [188](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-188) Failover y failback · el procedimiento
- [189](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-189) Respaldo no es lo mismo que replicación
- [190](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-190) Tipos de respaldo
- [191](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-191) La política de respaldo
- [192](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-192) Restaurar · lo único que importa
- [193](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-193) Continuidad en la oferta · qué declarar
- [194](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-194) Recomendaciones para profundizar · Sección 6 · Continuidad

**[195](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-195) ▶ SECCIÓN 7 · Seguridad**

- [196](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-196) Defensa en profundidad, capa por capa
- [197](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-197) La superficie de exposición
- [198](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-198) La capa de seguridad de una solución expuesta
- [199](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-199) Identidad y acceso
- [200](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-200) Protección de los datos
- [201](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-201) Caso · empresa con trabajo mixto
- [202](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-202) Dos zonas, dos reglas
- [203](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-203) Cómo se conecta el funcionario desde la casa
- [204](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-204) Una identidad, permisos distintos
- [205](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-205) Monitoreo, incidentes y cumplimiento
- [206](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-206) Monitoreo, incidentes y cumplimiento · continuación 1
- [207](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-207) Seguridad en la oferta · qué declarar
- [208](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-208) Recomendaciones para profundizar · Sección 7 · Seguridad

**[209](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-209) ▶ SECCIÓN 8 · Identidad y sesión de usuarios**

- [210](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-210) El inicio de sesión es arquitectura, no una pantalla
- [211](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-211) Tres preguntas que no son la misma
- [212](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-212) El vocabulario mínimo
- [213](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-213) El flujo básico, paso a paso
- [214](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-214) Alternativa 1 · usuarios propios en su base de datos
- [215](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-215) Cómo se guarda una contraseña
- [216](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-216) Cómo se guarda una contraseña · continuación 1
- [217](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-217) Alternativa 2 · el directorio corporativo (LDAP)
- [218](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-218) Cómo autentica la aplicación contra LDAP
- [219](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-219) LDAP · lo que hay que acordar con el mandante
- [220](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-220) Alternativa 3 · un proveedor de identidad
- [221](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-221) SAML 2.0, OAuth 2.0 y OpenID Connect
- [222](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-222) El flujo de OpenID Connect, en concreto
- [223](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-223) Keycloak
- [224](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-224) Alternativas de producto, comparadas
- [225](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-225) Cómo conviven varias fuentes de identidad
- [226](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-226) La sesión: las dos familias
- [227](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-227) Sesión en servidor o token: cuál elegir
- [228](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-228) Anatomía de un token JWT
- [229](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-229) Token de acceso y token de refresco
- [230](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-230) La cookie de sesión y sus marcas
- [231](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-231) Cerrar sesión de verdad
- [232](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-232) HTTPS: el requisito previo de todo lo anterior
- [233](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-233) Doble factor: no todos valen lo mismo
- [234](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-234) Autorización: dónde se decide qué puede hacer
- [235](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-235) Identidad de los sistemas, no sólo de las personas
- [236](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-236) Los errores que el evaluador busca
- [237](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-237) Los errores que el evaluador busca · continuación 1
- [238](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-238) Cómo elegir para su caso
- [239](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-239) Qué declarar en la oferta
- [240](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-240) Recomendaciones para profundizar · Sección 8 · Identidad y sesión de usuarios

**[241](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-241) ▶ SECCIÓN 9 · Entrega**

- [242](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-242) Por qué varios ambientes
- [243](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-243) Los cuatro ambientes
- [244](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-244) Cuánto cuestan los ambientes
- [245](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-245) Datos en ambientes no productivos
- [246](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-246) La promoción entre ambientes
- [247](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-247) Qué es CI/CD
- [248](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-248) Anatomía de una canalización
- [249](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-249) Cómo montar el ambiente de CI/CD
- [250](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-250) Estrategias de despliegue
- [251](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-251) Configuración y secretos por ambiente
- [252](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-252) Qué comprometer en la oferta
- [253](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-253) Recomendaciones para profundizar · Sección 9 · Entrega

**[254](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-254) ▶ SECCIÓN 10 · Tendencias**

- [255](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-255) Mapa de tendencias
- [256](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-256) Contenedores y orquestación
- [257](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-257) Ingeniería de plataforma
- [258](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-258) Infraestructura como código y GitOps
- [259](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-259) DevOps, DevSecOps y entrega continua
- [260](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-260) Observabilidad, malla de servicios y eBPF
- [261](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-261) Computación en el borde
- [262](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-262) Datos en tiempo real
- [263](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-263) Arquitecturas de datos
- [264](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-264) Inteligencia artificial en la arquitectura
- [265](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-265) IA · lo que cambia en costos, riesgos y ética
- [266](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-266) MLOps y el ciclo de vida de los modelos
- [267](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-267) FinOps · el costo como atributo de diseño
- [268](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-268) Sostenibilidad y eficiencia energética
- [269](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-269) Otras corrientes que conviene conocer
- [270](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-270) Cómo tratar la innovación en su propuesta
- [271](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-271) Recomendaciones para profundizar · Sección 10 · Tendencias

**[272](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-272) ▶ SECCIÓN 11 · De la teoría a su propuesta**

- [273](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-273) Qué se evalúa exactamente
- [274](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-274) La ruta, en siete pasos
- [275](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-275) Pasos 1 y 2 · de las bases al alcance
- [276](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-276) Paso 3 · La arquitectura lógica
- [277](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-277) La matriz de trazabilidad
- [278](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-278) Paso 4 · La ficha de parámetros
- [279](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-279) Paso 4 · La ficha de parámetros · continuación 1
- [280](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-280) Paso 5 · Comparar alternativas
- [281](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-281) Paso 6 · Justificar con estándares y referencias
- [282](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-282) Paso 7 · Las restricciones del contexto
- [283](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-283) De la arquitectura al flujo de caja
- [284](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-284) Errores frecuentes que hunden una propuesta
- [285](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-285) Cómo presentar la arquitectura
- [286](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-286) Qué hacer esta semana
- [287](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-287) Estimar el costo de la solución · el método
- [288](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-288) Las unidades de medida
- [289](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-289) Las unidades de medida · continuación 1
- [290](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-290) El caso de ejemplo
- [291](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-291) Escenario 1 · contenedores sin servidor, una zona
- [292](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-292) Escenario 1 · contenedores sin servidor, una zona · continuación 1
- [293](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-293) Cómo se calcula una línea · las tareas de contenedor
- [294](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-294) Escenario 2 · máquinas virtuales, una zona
- [295](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-295) Los cuatro escenarios, comparados
- [296](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-296) El escenario de peor caso
- [297](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-297) De dólares al mes al flujo de caja
- [298](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-298) Errores frecuentes al estimar
- [299](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-299) Qué debe entregar en el informe
- [300](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-300) Glosario 1 / 8
- [301](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-301) Glosario 2 / 8
- [302](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-302) Glosario 3 / 8
- [303](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-303) Glosario 4 / 8
- [304](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-304) Glosario 5 / 8
- [305](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-305) Glosario 6 / 8
- [306](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-306) Glosario 7 / 8
- [307](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-307) Glosario 8 / 8
- [308](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-308) Referencias
- [309](FEP01_Arquitectura_de_Software_transcripcion.md#diapositiva-309) Arquitectura de Software

### FEP02 · Requisitos, Alcance, Planificación y EDT

- [1](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-1) Portada

**[2](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-2) ▶ SECCIÓN 1 · El proyecto**

- [3](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-3) Qué es un proyecto
- [4](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-4) El PMBOK como marco de referencia
- [5](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-5) Los cinco grupos de procesos
- [6](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-6) Los cinco grupos de procesos
- [7](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-7) Las diez áreas de conocimiento
- [8](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-8) Ciclo de vida predictivo y adaptativo
- [9](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-9) La triple restricción
- [10](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-10) El plan para la dirección del proyecto
- [11](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-11) Interesados y patrocinador
- [12](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-12) Qué documento corresponde a qué
- [13](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-13) Recomendaciones para profundizar · Sección 1 · El proyecto

**[14](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-14) ▶ SECCIÓN 2 · Requisitos**

- [15](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-15) Qué es un requisito · IEEE Std. 610.12 -1990
- [16](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-16) Por qué importan los requisitos
- [17](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-17) Ingeniería de requisitos: desarrollo y gestión
- [18](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-18) Tipos de requisito
- [19](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-19) Requisitos funcionales y no funcionales
- [20](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-20) FURPS+
- [21](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-21) Quién provee los requisitos
- [22](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-22) Técnicas de extracción
- [23](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-23) Las cuatro técnicas más usadas, comparadas
- [24](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-24) Las cuatro preguntas del analista
- [25](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-25) La especificación de requisitos (ERS)
- [26](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-26) Las ocho características de una buena ERS
- [27](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-27) Las cuatro características que más se incumplen
- [28](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-28) SMART y los criterios de redacción
- [29](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-29) La ambigüedad, en un ejemplo
- [30](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-30) Priorización, trazabilidad y línea base
- [31](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-31) Recomendaciones para profundizar · Sección 2 · Requisitos

**[32](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-32) ▶ SECCIÓN 3 · Alcance**

- [33](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-33) Qué es la gestión del alcance
- [34](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-34) Alcance del producto y alcance del proyecto
- [35](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-35) Los seis procesos de la gestión del alcance
- [36](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-36) Los dos planes que salen del primer proceso
- [37](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-37) El enunciado del alcance del proyecto
- [38](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-38) Entregables y criterios de aceptación
- [39](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-39) Exclusiones explícitas
- [40](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-40) Supuestos y restricciones
- [41](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-41) Las once preguntas de la formulación · el esquema
- [42](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-42) Las once preguntas · qué determina cada una
- [43](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-43) El diagrama de contexto
- [44](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-44) Validar el alcance y controlar el alcance
- [45](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-45) Corrupción del alcance y Exceso de funcionalidad
- [46](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-46) La línea base del alcance
- [47](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-47) La solicitud de cambio
- [48](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-48) Recomendaciones para profundizar · Sección 3 · Alcance

**[49](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-49) ▶ SECCIÓN 4 · La EDT**

- [50](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-50) Qué es la EDT / WBS
- [51](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-51) Para qué sirve la EDT
- [52](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-52) La regla del 100 %
- [53](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-53) La EDT no tiene secuencia
- [54](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-54) Criterios de descomposición
- [55](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-55) Hasta qué nivel descomponer
- [56](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-56) El paquete de trabajo
- [57](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-57) El diccionario de la EDT
- [58](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-58) El código de cuentas
- [59](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-59) Los cinco pasos para desarrollar la EDT
- [60](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-60) La EDT como base de todo lo que sigue
- [61](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-61) Recomendaciones para profundizar · Sección 4 · La EDT

**[62](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-62) ▶ SECCIÓN 5 · El cronograma**

- [63](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-63) Los seis procesos de la gestión del cronograma
- [64](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-64) Plan de gestión del cronograma
- [65](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-65) Definir las actividades
- [66](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-66) Los hitos
- [67](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-67) Secuenciar: el método de diagramación por precedencia
- [68](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-68) Tipos de dependencia
- [69](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-69) Adelanto y retraso
- [70](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-70) El diagrama de red del cronograma
- [71](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-71) Esfuerzo y duración no son lo mismo
- [72](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-72) Factores que afectan la duración
- [73](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-73) Motivación del personal
- [74](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-74) Técnicas de estimación de la duración
- [75](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-75) Estimación por tres valores y PERT
- [76](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-76) PERT: el ejemplo
- [77](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-77) Reservas
- [78](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-78) Desarrollar el cronograma: la ruta crítica
- [79](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-79) El cálculo de fechas
- [80](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-80) Ejemplo de ruta crítica · la red
- [81](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-81) Ejemplo de ruta crítica · las fechas
- [82](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-82) Comprimir, nivelar y representar
- [83](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-83) Controlar el cronograma
- [84](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-84) Recomendaciones para profundizar · Sección 5 · El cronograma

**[85](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-85) ▶ SECCIÓN 6 · Estimación y costo**

- [86](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-86) La cadena de la estimación
- [87](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-87) Estimación ascendente y descendente
- [88](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-88) Técnicas de estimación de esfuerzo en software
- [89](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-89) El cono de la incertidumbre
- [90](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-90) De costo a tarifa
- [91](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-91) Los costos que no son horas
- [92](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-92) Contingencia, reserva de gestión y margen
- [93](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-93) Errores de costeo más frecuentes
- [94](FEP02_Requisitos_Alcance_Planificacion_EDT_transcripcion.md#diapositiva-94) Recomendaciones para profundizar · Sección 6 · Estimación y costo

### FEP03 · Estimación de Software

- [1](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-1) Portada

**[2](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-2) ▶ SECCIÓN 1 · Medir el tamaño del software**

- [3](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-3) El problema: cotizar algo que no se puede pesar
- [4](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-4) Para qué sirve medir el tamaño
- [5](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-5) Tamaño, esfuerzo, plazo y costo: la cadena completa
- [6](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-6) La idea común a todas las métricas funcionales
- [7](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-7) Qué métodos de estimación existen y cuándo sirve cada uno
- [8](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-8) En qué momento de una licitación se estima
- [9](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-9) Qué queda dentro de la estimación funcional y qué queda fuera
- [10](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-10) Lo que esta clase va a producir
- [11](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-11) Recomendaciones para profundizar · Sección 1 · Medir el tamaño del software

**[12](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-12) ▶ SECCIÓN 2 · Estimación por Punto Función**

- [13](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-13) Qué es el Punto Función y qué mide
- [14](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-14) La fórmula de Albrecht y sus dos fases
- [15](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-15) El modelo de conteo: la frontera, los datos y las transacciones
- [16](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-16) Las cinco categorías, con su definición
- [17](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-17) Los pesos por categoría y complejidad
- [18](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-18) Las catorce características generales del sistema
- [19](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-19) El factor de complejidad técnica y su rango
- [20](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-20) Recomendaciones para profundizar · Sección 2 · Estimación por Punto Función

**[21](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-21) ▶ SECCIÓN 3 · Punto de Casos de Uso**

- [22](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-22) Qué es el Punto de Casos de Uso
- [23](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-23) La cadena completa del método
- [24](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-24) Las cinco fórmulas del método
- [25](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-25) Puntos de casos de uso sin ajustar
- [26](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-26) Factor de peso de los actores sin ajustar (UAW)
- [27](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-27) Errores frecuentes al contar actores
- [28](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-28) Qué es una transacción y por qué importa
- [29](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-29) Factor de peso de los casos de uso sin ajustar (UUCW)
- [30](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-30) Cómo se cuentan las transacciones de un caso de uso
- [31](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-31) Reglas de conteo que conviene fijar antes de empezar
- [32](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-32) Un ejemplo mínimo, para fijar el procedimiento
- [33](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-33) Errores frecuentes en el conteo de casos de uso
- [34](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-34) Recomendaciones para profundizar · Sección 3 · Punto de Casos de Uso

**[35](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-35) ▶ SECCIÓN 4 · Factores técnicos y de ambiente**

- [36](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-36) Por qué el método ajusta dos veces
- [37](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-37) Puntos de casos de uso ajustados
- [38](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-38) Los trece factores técnicos y sus pesos
- [39](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-39) Qué evalúa cada factor técnico · T1 a T7
- [40](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-40) Qué evalúa cada factor técnico · T8 a T13
- [41](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-41) La escala de los factores técnicos y la fórmula del TCF
- [42](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-42) Los ocho factores de ambiente: qué significa el valor
- [43](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-43) La escala de cada factor de ambiente
- [44](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-44) La fórmula del factor de ambiente y su lectura correcta
- [45](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-45) Errores frecuentes al asignar los factores
- [46](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-46) Recomendaciones para profundizar · Sección 4 · Factores técnicos y de ambiente

**[47](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-47) ▶ SECCIÓN 5 · Del tamaño al esfuerzo**

- [48](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-48) La fórmula del esfuerzo
- [49](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-49) Cómo se decide el factor de conversión
- [50](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-50) El factor de conversión es el punto débil del método
- [51](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-51) La distribución del esfuerzo entre las etapas
- [52](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-52) Las dos lecturas de la distribución, y cuál usa el curso
- [53](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-53) Del esfuerzo al plazo: no es una división
- [54](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-54) Del esfuerzo al costo: la cadena de la tarifa
- [55](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-55) Errores frecuentes al convertir tamaño en esfuerzo
- [56](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-56) Recomendaciones para profundizar · Sección 5 · Del tamaño al esfuerzo

**[57](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-57) ▶ SECCIÓN 6 · Ejemplo completo, paso a paso**

- [58](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-58) El caso que vamos a estimar
- [59](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-59) Paso 1 · Peso de los actores (UAW)
- [60](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-60) Paso 2 · Peso de los casos de uso (UUCW)
- [61](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-61) Paso 3 · Puntos de casos de uso sin ajustar (UUCP)
- [62](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-62) Pasos 4 y 5 · Los dos coeficientes de ajuste
- [63](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-63) Paso 6 · Puntos de casos de uso ajustados (UCP)
- [64](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-64) Paso 7 · Factor de conversión
- [65](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-65) Paso 8 · El esfuerzo
- [66](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-66) Paso 9 · La estimación por etapa
- [67](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-67) Paso 10 · De horas a pesos y a UF
- [68](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-68) Qué tan sensible es el resultado a cada parámetro
- [69](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-69) La cadena completa en una sola lámina
- [70](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-70) Recomendaciones para profundizar · Sección 6 · Ejemplo completo, paso a paso

**[71](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-71) ▶ SECCIÓN 7 · Aclaraciones y glosario**

- [72](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-72) Tres distinciones que hay que tener claras
- [73](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-73) Glosario del método
- [74](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-74) Lo que hay que llevarse de esta clase
- [75](FEP03_Estimacion_de_Software_transcripcion.md#diapositiva-75) Recomendaciones para profundizar · Sección 7 · Aclaraciones y glosario

### FEP04 · Gestión de Riesgos TIC

- [1](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-1) Portada

**[2](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-2) ▶ SECCIÓN 1 · Qué es un riesgo**

- [3](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-3) Incertidumbre, riesgo y problema
- [4](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-4) Definición formal y las dos caras del riesgo
- [5](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-5) La idea rectora de esta clase
- [6](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-6) Los cinco elementos que definen un riesgo
- [7](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-7) Escalas de probabilidad e impacto: hay que definirlas antes
- [8](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-8) La matriz de exposición y las zonas de acción
- [9](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-9) Apetito, tolerancia y umbral: tres palabras que no son sinónimos
- [10](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-10) La curva que gobierna toda la clase
- [11](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-11) Por qué fallan los proyectos TIC
- [12](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-12) Riesgo del proyecto, riesgo del producto y riesgo del negocio
- [13](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-13) El caso que vamos a usar
- [14](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-14) Recomendaciones para profundizar · Sección 1 · Qué es un riesgo

**[15](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-15) ▶ SECCIÓN 2 · El proceso de gestión de riesgos**

- [16](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-16) Los siete procesos de la gestión de riesgos
- [17](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-17) El flujo completo, de la identificación al cierre
- [18](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-18) El plan de gestión de riesgos: qué se decide antes de empezar
- [19](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-19) La estructura de desglose de riesgos (RBS)
- [20](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-20) Una RBS para proyectos TIC de integración
- [21](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-21) El registro de riesgos: los campos que no pueden faltar
- [22](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-22) Riesgo individual, variabilidad y ambigüedad
- [23](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-23) Cómo se adapta el proceso al proyecto
- [24](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-24) Dónde vive el riesgo en el resto del plan del proyecto
- [25](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-25) Cuándo se repite cada proceso
- [26](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-26) Recomendaciones para profundizar · Sección 2 · El proceso de gestión de riesgos

**[27](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-27) ▶ SECCIÓN 3 · Identificar los riesgos**

- [28](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-28) Qué significa identificar bien
- [29](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-29) Técnicas para recopilar riesgos
- [30](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-30) Técnicas de análisis para descubrir riesgos que nadie mencionó
- [31](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-31) Supuestos y restricciones: la fábrica de riesgos de toda propuesta
- [32](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-32) Lectura adversarial: qué frases de las bases producen riesgo
- [33](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-33) Catálogo de riesgos TIC · Solución, tecnología e integración
- [34](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-34) Catálogo de riesgos TIC · Operación del cliente y adopción
- [35](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-35) Catálogo de riesgos TIC · Contrato, entorno y empresa proveedora
- [36](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-36) Cómo se escribe un riesgo para que sirva
- [37](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-37) Ejemplos: así no, así sí
- [38](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-38) Errores frecuentes en la identificación
- [39](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-39) El resultado de la identificación en el caso
- [40](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-40) Recomendaciones para profundizar · Sección 3 · Identificar los riesgos

**[41](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-41) ▶ SECCIÓN 4 · Analizar los riesgos**

- [42](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-42) Dos análisis distintos, con propósitos distintos
- [43](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-43) Qué se evalúa en el análisis cualitativo
- [44](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-44) La matriz de exposición aplicada al caso
- [45](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-45) Cuándo vale la pena el análisis cuantitativo
- [46](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-46) Valor monetario esperado: la fórmula y su lectura correcta
- [47](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-47) El registro cuantificado del caso
- [48](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-48) De la suma de valores esperados a la reserva del precio
- [49](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-49) Reserva de contingencia y reserva de gestión
- [50](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-50) Árbol de decisión: comparar alternativas de solución
- [51](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-51) El punto de indiferencia: hasta dónde aguanta la decisión
- [52](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-52) Estimación de tres valores: poner rango donde había un número
- [53](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-53) Simulación del cronograma: qué plazo conviene comprometer
- [54](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-54) Análisis de sensibilidad: dónde conviene concentrar la gestión
- [55](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-55) Errores frecuentes en el análisis
- [56](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-56) Recomendaciones para profundizar · Sección 4 · Analizar los riesgos

**[57](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-57) ▶ SECCIÓN 5 · Responder a los riesgos**

- [58](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-58) Qué debe contener una respuesta para que exista
- [59](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-59) Las cinco estrategias frente a una amenaza
- [60](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-60) Las cinco estrategias frente a una oportunidad
- [61](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-61) Cómo se elige la estrategia: dos preguntas y una regla
- [62](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-62) Cuánto conviene gastar en una respuesta
- [63](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-63) La escalera de costo de la respuesta
- [64](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-64) Riesgo residual, riesgo secundario y disparador
- [65](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-65) Plan de contingencia y plan de reversa
- [66](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-66) Las respuestas planificadas en el caso
- [67](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-67) Implementar la respuesta: el proceso que más se olvida
- [68](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-68) Monitorear: qué se hace con el registro durante la ejecución
- [69](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-69) Errores frecuentes en la respuesta
- [70](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-70) Recomendaciones para profundizar · Sección 5 · Responder a los riesgos

**[71](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-71) ▶ SECCIÓN 6 · Riesgos de la licitación**

- [72](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-72) Por qué el riesgo de una licitación es un riesgo distinto
- [73](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-73) La línea de tiempo del proceso y dónde se puede actuar
- [74](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-74) Riesgos del proceso mismo, antes de la adjudicación
- [75](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-75) Riesgos del contrato · alcance, aceptación y plazo
- [76](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-76) Riesgos del contrato · dinero, datos y terceros
- [77](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-77) Los riesgos que las bases no cuentan
- [78](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-78) Las cinco palancas de anticipación
- [79](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-79) Palanca 1 · Cómo se escribe una consulta que sirva
- [80](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-80) Palanca 2 · Cómo se declara un supuesto para que proteja
- [81](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-81) Palanca 3 · La exclusión explícita
- [82](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-82) Palanca 4 · Rediseñar para que el riesgo deje de existir
- [83](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-83) Palanca 5 · Cuándo la respuesta correcta es no presentarse
- [84](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-84) El acta de respuestas: el riesgo que aparece después de costear
- [85](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-85) Los riesgos de licitación del caso y la palanca aplicada
- [86](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-86) Recomendaciones para profundizar · Sección 6 · Anticipar los riesgos de la licitación

**[87](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-87) ▶ SECCIÓN 7 · Del riesgo a la solución**

- [88](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-88) La cadena de trazabilidad que se evalúa
- [89](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-89) Los cuatro lugares donde un riesgo cambia la solución
- [90](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-90) Cómo un riesgo cambia el alcance
- [91](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-91) Cómo un riesgo se convierte en un requisito
- [92](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-92) Cómo un riesgo cambia la arquitectura
- [93](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-93) El riesgo en la arquitectura lógica y en la física
- [94](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-94) Cómo un riesgo cambia el plan de trabajo y la implantación
- [95](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-95) Cómo un riesgo cambia la operación y el servicio
- [96](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-96) La matriz de trazabilidad riesgo → solución
- [97](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-97) Cómo se refleja todo esto en la oferta económica
- [98](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-98) El mismo método en otras industrias
- [99](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-99) Innovación y riesgo: cómo proponer algo nuevo sin comprometerse de más
- [100](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-100) Rediseños que no resuelven nada
- [101](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-101) Recomendaciones para profundizar · Sección 7 · Del riesgo a la solución

**[102](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-102) ▶ SECCIÓN 8 · Declarar el riesgo y su etapa**

- [103](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-103) Por qué conviene declarar el riesgo y no esconderlo
- [104](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-104) Dónde se declara cada cosa dentro de la propuesta
- [105](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-105) La ficha de riesgo completa, con un ejemplo lleno
- [106](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-106) Las cuatro etapas en que puede actuar una acción
- [107](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-107) Etapa 1 · Acciones que sólo se pueden tomar en la propuesta
- [108](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-108) Etapa 2 · Acciones durante la implementación
- [109](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-109) Etapa 3 · Acciones durante la implantación
- [110](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-110) Etapa 4 · Acciones durante la operación
- [111](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-111) Cómo se distribuyen las acciones del caso en las cuatro etapas
- [112](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-112) El registro de riesgos que se entrega con la propuesta
- [113](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-113) Gobierno del riesgo durante el contrato
- [114](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-114) Cierre: liberación de reserva y lecciones aprendidas
- [115](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-115) Recomendaciones para profundizar · Sección 8 · Declarar el riesgo y su etapa

**[116](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-116) ▶ SECCIÓN 9 · En su propuesta**

- [117](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-117) Qué productos de la propuesta dependen de este trabajo
- [118](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-118) Estructura recomendada del capítulo de gestión de riesgos
- [119](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-119) Contenido mínimo exigible: lista de cotejo
- [120](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-120) Qué busca el evaluador en cada criterio
- [121](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-121) Los errores que más descuentan
- [122](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-122) Cómo contar el riesgo en tres minutos de presentación
- [123](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-123) La ruta de trabajo, paso a paso
- [124](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-124) Glosario · de amenaza a matriz de exposición
- [125](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-125) Glosario · de oportunidad a valor monetario esperado
- [126](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-126) Lo que hay que llevarse de esta clase
- [127](FEP04_Gestion_de_Riesgos_TIC_transcripcion.md#diapositiva-127) Recomendaciones para profundizar · Sección 9 · En su propuesta

### FEP05 · Sala de Servidores

- [1](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-1) Portada
- [2](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-2) Esto es un datacenter
- [3](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-3) Lo que vamos a ver

**[4](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-4) ▶ SECCIÓN 1 · Datacenter**

- [5](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-5) Cuatro cosas, todo el tiempo
- [6](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-6) Cuánto vale un nueve más
- [7](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-7) Redundancia: la letra lo dice todo
- [8](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-8) PUE: por qué la cuenta de la luz importa
- [9](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-9) Qué se mide arriba y qué se mide abajo
- [10](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-10) Cómo se mide y cómo se baja el PUE · ficha técnica
- [11](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-11) La tabla de traducción
- [12](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-12) Los cuatro niveles, lado a lado · ficha técnica
- [13](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-13) Redundancia y normas · ficha técnica

**[14](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-14) ▶ SECCIÓN 2 · El programa de recintos**

- [15](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-15) La idea que ordena todo
- [16](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-16) Data Center - Recintos
- [17](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-17) Los cuatro principios
- [18](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-18) El plano por zonas
- [19](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-19) Un corte real
- [20](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-20) Pensando en el Plano
- [21](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-21) El corazón y sus dos vecinos
- [22](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-22) Energía: tres recintos, tres riesgos
- [23](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-23) Los tres recintos que siempre se olvidan
- [24](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-24) Los de apoyo, que son los más baratos
- [25](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-25) Ejemplos
- [26](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-26) Adyacencias: qué va junto a qué
- [27](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-27) Los trece recintos · ficha técnica

**[28](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-28) ▶ SECCIÓN 3 · Opciones de distribución**

- [29](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-29) La pregunta de la sección
- [30](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-30) Primero: ¿de qué tamaño es su sala?
- [31](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-31) Ejemplos - SONDA
- [32](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-32) Ejemplo - SONDA
- [33](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-33) Ejemplo - Google
- [34](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-34) Ambos
- [35](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-35) Data center
- [36](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-36) Pausa · trabajo en grupo

**[37](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-37) ▶ SECCIÓN 4 · Seguridad, acceso y monitoreo**

- [38](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-38) La pregunta de la sección
- [39](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-39) La seguridad es por capas
- [40](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-40) Cómo se cruza cada puerta
- [41](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-41) Los sentidos de la sala
- [42](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-42) Sección 4 · lo que hay que entender
- [43](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-43) La secuencia de una descarga
- [44](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-44) Agentes de extinción y control de acceso · ficha técnica

**[45](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-45) ▶ SECCIÓN 5 · Energía y clima**

- [46](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-46) Escenario
- [47](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-47) La cadena eléctrica
- [48](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-48) Qué protege cada eslabón
- [49](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-49) Tres equipos, tres ventanas de tiempo
- [50](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-50) La relación que más se olvida
- [51](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-51) De dónde viene el calor
- [52](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-52) Pasillo frío y pasillo caliente
- [53](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-53) Pasillo frío y pasillo caliente
- [54](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-54) Lo que ordena el aire y lo que lo arruina
- [55](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-55) Cuatro maneras de sacar el calor
- [56](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-56) Free cooling y lo que hay que declarar
- [57](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-57) El suelo y el cielo de la sala
- [58](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-58) Dimensionar la carga eléctrica y térmica · ficha técnica
- [59](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-59) Pausa · trabajo en grupo

**[60](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-60) ▶ SECCIÓN 6 · Rack y cableado**

- [61](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-61) La elevación del rack
- [62](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-62) Todo se mide en U
- [63](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-63) La elevación del rack
- [64](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-64) Qué se cuenta en U
- [65](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-65) El chasis: cuántos servidores caben de verdad
- [66](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-66) No todos los racks sirven para lo mismo
- [67](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-67) Cableado: disciplina de tráfico
- [68](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-68) Topología del cableado y etiquetado
- [69](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-69) Medios de cableado · ficha técnica
- [70](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-70) Cuántos racks necesita su caso · ficha técnica

**[71](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-71) ▶ SECCIÓN 7 · Servidores, comunicaciones y storage**

- [72](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-72) Antes de elegir marcas
- [73](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-73) Cuatro formatos
- [74](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-74) Virtualizar es lo que hace posible su sala
- [75](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-75) Tres formas de guardar el dato
- [76](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-76) Lo que sigue
- [77](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-77) Los parámetros que hay que declarar · ficha técnica
- [78](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-78) Glosario · ficha técnica
- [79](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-79) Fuentes y para seguir · ficha técnica
- [80](FEP05_Sala_de_Servidores_transcripcion.md#diapositiva-80) Para la próxima sesión
