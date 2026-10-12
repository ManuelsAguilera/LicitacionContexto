# Diccionario de la EDT por paquete (estructura)

Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/generar_diccionario.py` a partir de `14_edt_corregida.md`; no editar a mano. Los valores que escriben las personas van en `19_diccionario_campos_manuales.md` y se aplican al regenerar. Fecha: 2026-10-08. Estado: **estructura**. Las fichas son de las cuentas de control; en el software el paquete de trabajo es el caso de uso (uno por caso, 127 en total, en `15_mapa_paquetes_ucp.md` y `16_horas_por_paquete.md`) y hereda la ficha de su cuenta. Base: Formulario T-14 y sección 7.1 del Comunicado 10 (entregable, criterio de aceptación y responsable por paquete) y los doce campos de la clase FEP02 (diapositiva 57). Cada valor lleva su estado: **[derivado]** sale de un artefacto del proyecto, **[propuesta]** lo propone este trabajo y debe validarse, **[manual]** lo escribió una persona y **[por definir]** no tiene fuente todavía.

## 1. Estado de llenado

| Campo | Derivado | Propuesta | Manual | Por definir |
| :-- | --: | --: | --: | --: |
| Descripción del trabajo | 51 | 0 | 0 | 113 |
| Queda fuera | 15 | 0 | 0 | 149 |
| Entregable | 51 | 0 | 0 | 113 |
| Criterio de aceptación | 29 | 0 | 0 | 135 |
| Responsable | 0 | 159 | 0 | 5 |
| Hitos asociados | 76 | 0 | 0 | 88 |
| Esfuerzo estimado | 51 | 0 | 0 | 113 |
| Costo estimado | 0 | 0 | 0 | 164 |
| Recursos requeridos | 0 | 0 | 0 | 164 |
| Supuestos | 164 | 0 | 0 | 0 |
| Referencias | 157 | 0 | 0 | 7 |

Los tres campos que exige el Comunicado 10 (entregable, criterio de aceptación y responsable) tienen valor en 29 de 164 paquetes, contando las propuestas, y valor derivado o manual en 0. Una fila «propuesta» todavía no es una decisión del equipo; el responsable es siempre propuesta hasta que el equipo lo valide.

## 2. Cómo se completa

1. Se escribe cada valor en `19_diccionario_campos_manuales.md` (código del paquete, campo, valor y fuente).
2. Se corre `python3 05_Gestion/scripts/generar_diccionario.py` y el valor aparece como **[manual]**.
3. El criterio de aceptación sale del Anexo B (umbrales) o del Anexo D (metas); si no existe, se deja «por definir».
4. El responsable es siempre un rol. Los roles del proponente son los del sd-01, apartado 1.2; la dotación y la dedicación son del sd-12.

## 3. Fichas

### Rama 1.1

#### 1.1.1 Plan de dirección integrado (ámbito, cronograma, costos, calidad, riesgos, comunicaciones, interesados y adquisiciones)

- **Rama y servicio:** 1.1. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 1 a 3 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plan; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 3 (propuesta): plan inicial; se actualiza durante el contrato. [derivado]
- **Referencias:** por definir [por definir]

#### 1.1.2 EDT y diccionario de paquetes con entregable, criterio de aceptación y responsable

- **Rama y servicio:** 1.1. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 1 a 3 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 3 (propuesta): base de la planificación. [derivado]
- **Referencias:** Formulario T-14. [derivado]

#### 1.1.3 Registro de solicitudes de cambio y su resolución

- **Rama y servicio:** 1.1. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 1 a 56 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: registro; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 1 a 56, fijada por el contrato (Art. 72: todo el contrato). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 56 (contrato): Art. 72: todo el contrato. [derivado]
- **Referencias:** Art. 72. [derivado]

#### 1.1.4 Registros de riesgos, lecciones aprendidas, supuestos y consultas

- **Rama y servicio:** 1.1. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 1 a 56 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: registro; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 56 (propuesta): continuo. [derivado]
- **Referencias:** sd-03, 3.2.3 (supuestos y Tabla 3.3). [derivado]

#### 1.1.6 Calendario de ventanas de congelamiento y de eventos anuales con declaración de impacto por evento

- **Rama y servicio:** 1.1. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 1 a 3 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 3 (propuesta): se actualiza cada año antes de la campaña de noviembre. [derivado]
- **Referencias:** sd-03, 3.2.2 y 3.2.3 (ventanas de congelamiento). [derivado]

#### 1.1.7 Actas de los comités e informe mensual de avance

- **Rama y servicio:** 1.1. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 1 a 56 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: acta; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 1 a 56, fijada por el contrato (Art. 71: comités durante todo el contrato; RT-19.06: informe mensual). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 56 (contrato): Art. 71: comités durante todo el contrato; RT-19.06: informe mensual. [derivado]
- **Referencias:** Art. 71; RT-19.06. [derivado]

#### 1.1.9 Reporte mensual de consumo de nube

- **Rama y servicio:** 1.1. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 4 a 56 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 4 a 56 (propuesta): desde el primer entorno de nube. [derivado]
- **Referencias:** Art. 16.3; RT-03.06. [derivado]

#### 1.1.10 Actas de aceptación por entrega y habilitación de pagos

- **Rama y servicio:** 1.1. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 1 a 56 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: acta; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 1 a 56, fijada por el contrato (Art. 18: cada entrega sujeta a aceptación). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 56 (contrato): Art. 18: cada entrega sujeta a aceptación. [derivado]
- **Referencias:** Art. 18; E-25. [derivado]

#### 1.1.11 Registro de garantías, seguros y certificados laborales vigentes

- **Rama y servicio:** 1.1. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 1 a 56 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: registro; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 1 a 56, fijada por el contrato (Art. 75.3). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 56 (contrato): Art. 75.3. [derivado]
- **Referencias:** Art. 75.3. [derivado]

#### 1.1.12 Acta de constitución del proyecto

- **Rama y servicio:** 1.1. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** el mes 1 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: acta; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de el mes 1 (propuesta): mes de inicio. [derivado]
- **Referencias:** por definir [por definir]

#### 1.1.13 Línea base de costos y presupuesto

- **Rama y servicio:** 1.1. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 1 a 3 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 3 (propuesta): base de la planificación. [derivado]
- **Referencias:** Ronda 0: 2.9; los valores viven solo en la oferta económica. [derivado]

#### 1.1.14 Planes alternativos de las dos condiciones del adelanto del negocio financiero

- **Rama y servicio:** 1.1. **Etapa:** 1. **Método:** tres valores.
- **Ventana:** los meses 3 a 5 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plan; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 3 a 5 (propuesta): sd-03, 3.2.3: antes de la prueba del corte de enlace de los meses 6 y 7. [derivado]
- **Referencias:** sd-03, 3.2.3; el detalle se resuelve en el plan de trabajo y en el análisis de riesgos. [derivado]

### Rama 1.2

#### 1.2.1 Mapa de las 14 interfaces e inventario de las 9 plataformas, 6 proveedores y dependencias

- **Rama y servicio:** 1.2. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 1 a 3 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 3 (propuesta): entrega temprana, antes del diseño; antes del diseño. [derivado]
- **Referencias:** sd-03, 3.3.1 (el levantamiento documenta las catorce interfaces y las nueve plataformas). [derivado]

#### 1.2.3 Levantamiento de procesos, reglas de negocio y volumetría declarada

- **Rama y servicio:** 1.2. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 1 a 3 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 3 (propuesta): antes del diseño. [derivado]
- **Referencias:** sd-03, 3.2.4 (reglas de negocio) y 3.4.1 (volumetría del Caso). [derivado]

#### 1.2.4 Catálogo de requerimientos y matriz de trazabilidad

- **Rama y servicio:** 1.2. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 1 a 18 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 18 (propuesta): mientras dura el desarrollo; tras el levantamiento. [derivado]
- **Referencias:** Anexo B del sd-03. [derivado]

#### 1.2.6 Línea base de alcance por etapa, con exclusiones y supuestos

- **Rama y servicio:** 1.2. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 3 a 4 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 3 a 4 (propuesta): cierra el levantamiento. [derivado]
- **Referencias:** sd-03, 3.2.2 y 3.2.3 (reparto por etapa, exclusiones y supuestos; Tablas 3.1 y 3.3). [derivado]

#### 1.2.7 Estudio de decisión con costeo sobre etiquetas electrónicas de precio

- **Rama y servicio:** 1.2. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 2 a 5 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 2 a 5 (propuesta): OP-01 a OP-05. [derivado]
- **Referencias:** OP-01 a OP-05. [derivado]

#### 1.2.8 Estudio de decisión con costeo sobre el sistema de almacenes de Concepción

- **Rama y servicio:** 1.2. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 2 a 6 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 2 a 6 (propuesta): OP-08, OP-09. [derivado]
- **Referencias:** OP-08, OP-09. [derivado]

#### 1.2.9 Estudio de decisión con costeo sobre el destino de las plataformas

- **Rama y servicio:** 1.2. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 2 a 5 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 2 a 5 (propuesta): decide el destino de las plataformas. [derivado]
- **Referencias:** sd-03, 3.2.1 y 3.3.1 (destino de las nueve plataformas; SD-06 programa la decisión). [derivado]

#### 1.2.10 Propuesta de criterios del cupo preaprobado para la filial emisora

- **Rama y servicio:** 1.2. **Etapa:** 1. **Método:** tres valores.
- **Ventana:** los meses 3 a 5 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** RC-11: Fijar el apetito de riesgo del crédito sin conexión (topes, antigüedad del registro local y exclusiones). [derivado]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 3 a 5 (propuesta): sd-03, 3.2.3: la filial emisora fija los criterios antes de la prueba de los meses 6 y 7. [derivado]
- **Referencias:** sd-03, 3.2.3; la filial emisora los fija antes de la prueba (RC-11). [derivado]

### Rama 1.3

#### 1.3.1 Documento de arquitectura con cinco vistas y catálogo de decisiones

- **Rama y servicio:** 1.3. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 2 a 4 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 2 a 4 (propuesta): arquitectura cerrada en el mes 4 (EDT original); idem. [derivado]
- **Referencias:** ISO 42010. [derivado]

#### 1.3.3 Arquitectura física con emplazamiento por componente justificado

- **Rama y servicio:** 1.3. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 2 a 4 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 2 a 4 (propuesta): idem. [derivado]
- **Referencias:** Art. 16.2; zonas a nombrar conforme al sd-04. [derivado]

#### 1.3.4 Modelo de datos con dominios segregados Retail y Emisor, frontera documentada y políticas de retención

- **Rama y servicio:** 1.3. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 2 a 4 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 2 a 4 (propuesta): idem. [derivado]
- **Referencias:** RT-05.10. [derivado]

#### 1.3.5 Contratos de integración versionados y su gobierno

- **Rama y servicio:** 1.3. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 3 a 4 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 3 a 4 (propuesta): idem. [derivado]
- **Referencias:** sd-03, 3.3.2 (contratos y adaptadores de la plataforma común). [derivado]

#### 1.3.6 Especificación del modo desconectado de 24 horas y de la sincronización tras la reconexión

- **Rama y servicio:** 1.3. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 3 a 4 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 3 a 4 (propuesta): idem. [derivado]
- **Referencias:** RT-03.10 de las Bases Transversales; el código RT-03.13 significa cosas distintas en el Caso y en las Transversales. [derivado]

#### 1.3.7 Modelo de capacidad y dimensionamiento

- **Rama y servicio:** 1.3. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 3 a 4 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 3 a 4 (propuesta): idem. [derivado]
- **Referencias:** memoria de capacidad de la sección 3.4.1 del sd-03. [derivado]

#### 1.3.8 Especificación y costeo de las obras de infraestructura del cliente

- **Rama y servicio:** 1.3. **Etapa:** desde el inicio del contrato. **Método:** tres valores.
- **Ventana:** los meses 3 a 6 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** SP-04: El cliente adquiere, ejecuta y contrata, antes de cada instalación en tienda y centro de distribución, lo físico que el proponente especifica. El proponente provee el centro de datos on-premise con su conectividad, su seguridad y sus canalizaciones. [derivado]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 3 a 6 (propuesta): el cliente necesita plazo para ejecutar las obras. [derivado]
- **Referencias:** El cliente ejecuta; el proponente especifica, costea, coordina y certifica (SP-04). [derivado]

### Rama 1.4

#### 1.4.1 Entorno de nube con infraestructura como código, subredes privadas y etiquetado de costos

- **Rama y servicio:** 1.4. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 3 a 6 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: entorno operando; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 3 a 6 (propuesta): plataforma base lista en el mes 6 (EDT original). [derivado]
- **Referencias:** sd-03, 3.1 (despliegue híbrido con la carga principal en nube pública). [derivado]

#### 1.4.2 Configuración del borde por sitio y certificación de la red segmentada en las 13 tiendas que no la tienen

- **Rama y servicio:** 1.4. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 4 a 12 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** SP-04: El cliente adquiere, ejecuta y contrata, antes de cada instalación en tienda y centro de distribución, lo físico que el proponente especifica. El proponente provee el centro de datos on-premise con su conectividad, su seguridad y sus canalizaciones; EXC-19: Proveer o instalar equipamiento físico de tiendas y centros de distribución, ejecutar sus obras ni contratar sus enlaces. [derivado]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 4 a 12 (propuesta): primero las tres tiendas del piloto del punto de venta (meses 6 y 7) y después el resto, antes de la marcha blanca; antes del piloto de tiendas. [derivado]
- **Referencias:** El hardware lo adquiere el cliente (SP-04); El cliente adquiere el hardware y ejecuta las obras (EXC-19, SP-04); RT-03.24 del Caso. [derivado]

#### 1.4.3 Entorno dedicado del ámbito emisor con segregación física y lógica acreditada

- **Rama y servicio:** 1.4. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 4 a 8 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: entorno operando; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 4 a 8 (propuesta): ámbito emisor. [derivado]
- **Referencias:** RNF-14 y RNF-36 (Anexo B): separación física acreditada del ámbito emisor. [derivado]

#### 1.4.4 Ambientes de desarrollo, calidad, preproducción, producción y recuperación ante desastres

- **Rama y servicio:** 1.4. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: entorno operando; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 1 a 12, fijada por el contrato (Art. 17: ambientes habilitados dentro de la Etapa 1 (meses 1 a 12)). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 12 (contrato): Art. 17: ambientes habilitados dentro de la Etapa 1 (meses 1 a 12). [derivado]
- **Referencias:** sd-03, 3.4.1 (pruebas en preproducción a 1,5 veces el peak declarado). [derivado]

#### 1.4.5 Plataforma de observabilidad unificada con catálogo de alertas

- **Rama y servicio:** 1.4. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 4 a 8 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plataforma operando; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 4 a 8 (propuesta): antes de las primeras pruebas. [derivado]
- **Referencias:** frontera con el UCP: aquí el aprovisionamiento; las funciones al actor están en la base tecnológica; sd-03, 3.2.1 y 3.3.2 (observabilidad de la base tecnológica). [derivado]

#### 1.4.6 Plataforma de integración y entrega continuas con infraestructura como código

- **Rama y servicio:** 1.4. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 3 a 5 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plataforma operando; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 3 a 5 (propuesta): antes del desarrollo en curso. [derivado]
- **Referencias:** Antes 1.5.10; no está en el UCP. [derivado]

#### 1.4.7 Licenciamiento de terceros a nombre del cliente

- **Rama y servicio:** 1.4. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 2 a 6 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 2 a 6 (propuesta): a nombre del cliente. [derivado]
- **Referencias:** Agregado desde la guía de la EDT, sección 8. [derivado]

#### 1.4.8 Especificación de hardware y dispositivos de terreno para adquisición del cliente

- **Rama y servicio:** 1.4. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 3 a 6 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 3 a 6 (propuesta): el cliente adquiere después. [derivado]
- **Referencias:** Formulario T-11; OP-06, OP-07. [derivado]

#### 1.4.9 Plano y especificación del recinto técnico del centro de datos y coordinación de su obra civil de separación

- **Rama y servicio:** 1.4. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 2 a 6 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** RC-04: Ejecutar la obra civil de separación del centro de datos y las obras y enlaces de tiendas y centros de distribución, especificados y costeados. [derivado]
- **Entregable:** Por definir. Tipo probable: plan; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 2 a 6 (propuesta): RT-06.03; RT-06.06: el cliente ejecuta la obra. [derivado]
- **Referencias:** Ronda 0: 1.15.3; RT-06.03; El cliente ejecuta la obra (RT-06.06, RC-04); incluye la especificación del blindaje (RT-06.02). [derivado]

#### 1.4.11 Plan de cierre de la brecha del centro de datos frente al informe interno de 2024

- **Rama y servicio:** 1.4. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 2 a 5 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** RC-01: Entregar el informe interno de 2024 sobre la brecha del centro de datos. [derivado]
- **Entregable:** Por definir. Tipo probable: plan; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 2 a 5 (propuesta): informe de 2024. [derivado]
- **Referencias:** Ronda 0: 1.15.4; RC-01 (Anexo A): el cliente entrega el informe de 2024 sobre la brecha del centro de datos. [derivado]

#### 1.4.12 Sistemas de energía y climatización del centro de datos

- **Rama y servicio:** 1.4. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 6 a 12 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: sistema operando; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 6 a 12 (propuesta): listo antes de la marcha blanca; idem. [derivado]
- **Referencias:** RT-06.07, RT-06.08; RT-06.13, RT-06.14. [derivado]

#### 1.4.14 Sistemas de seguridad física del centro de datos y espacio de operación del personal

- **Rama y servicio:** 1.4. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 6 a 12 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: sistema operando; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 6 a 12 (propuesta): idem. [derivado]
- **Referencias:** RT-06.16, RT-06.17; RT-06.20 a RT-06.24; Ronda 0: 1.15.11. [derivado]

#### 1.4.17 Solución de respaldo en operación con custodia de medios

- **Rama y servicio:** 1.4. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 6 a 12 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: sistema operando; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 6 a 12 (propuesta): RT-07.09; RT-06.26. [derivado]
- **Referencias:** RT-07.09; esquema 3-2-1-1-0; RT-06.26. [derivado]

### Rama 1.5

#### 1.5.1.1 Precio: cambio, propagación, consulta e historial

- **Rama y servicio:** 1.5, Servicio de oferta comercial. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-OF-01 Cambiar y propagar un precio; CU-OF-02 Entregar la oferta vigente a los canales; CU-OF-03 Consultar el precio vigente en línea; CU-OF-06 Recuperar el precio publicado en un instante. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de oferta comercial» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 6 del Anexo D: 5 minutos o menos en cajas y canal digital (RT-09.01). En sala, por definir con la política de precios en sala.; Resultado 8 del Anexo D: Recuperación en 1 minuto o menos sobre una ventana de tres años (propuesta del proponente, RNF-44 y RNF-58). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 1.234 h en total (UCP, escenario del equipo): análisis 123 h, diseño 247 h, programación 494 h, pruebas 185 h y sobrecarga 185 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-OF-01 (03_casos_de_uso_oferta-comercial.md): S2, S3, S4; CU-OF-02 (03_casos_de_uso_oferta-comercial.md): S4; CU-OF-03 (03_casos_de_uso_oferta-comercial.md): S1; CU-OF-06 (03_casos_de_uso_oferta-comercial.md): S6; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-016 a RF-018, RF-021, RF-030, RF-064; casos de uso CU-OF-01, CU-OF-02, CU-OF-03, CU-OF-06; resultados del Anexo D: 6, 8. [derivado]

#### 1.5.1.2 Etiquetas de exhibición y discrepancias de precio

- **Rama y servicio:** 1.5, Servicio de oferta comercial. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-OF-04 Registrar el cambio de etiqueta; CU-OF-05 Consultar el estado de exhibición de la tienda; CU-OF-07 Resolver el precio a cobrar ante diferencia con la etiqueta; CU-OF-08 Revisar los incidentes de discrepancia de precio. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de oferta comercial» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 7 del Anexo D: 100 % de los puntos con estado registrado (propuesta del proponente).; Resultado 9 del Anexo D: 0,5 % o menos, verificado por muestreo propio (propuesta del proponente). La política de precios en sala está pendiente (supuestos SUP-08 y SUP-09). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 988 h en total (UCP, escenario del equipo): análisis 99 h, diseño 198 h, programación 395 h, pruebas 148 h y sobrecarga 148 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-OF-04 (03_casos_de_uso_oferta-comercial.md): S6; CU-OF-05 (03_casos_de_uso_oferta-comercial.md): S4; CU-OF-07 (03_casos_de_uso_oferta-comercial.md): S5; CU-OF-08 (03_casos_de_uso_oferta-comercial.md): S5, S8; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-019, RF-020, RF-022 a RF-024, RF-028, RF-029; casos de uso CU-OF-04, CU-OF-05, CU-OF-07, CU-OF-08; resultados del Anexo D: 7, 9. [derivado]

#### 1.5.1.5 Promociones y su vigencia

- **Rama y servicio:** 1.5, Servicio de oferta comercial. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-OF-09 Aplicar las promociones vigentes en la venta; CU-OF-10 Administrar las promociones y su vigencia. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de oferta comercial» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 9 del Anexo D: 0,5 % o menos, verificado por muestreo propio (propuesta del proponente). La política de precios en sala está pendiente (supuestos SUP-08 y SUP-09). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-OF-09 (03_casos_de_uso_oferta-comercial.md): S2, S4; CU-OF-10 (03_casos_de_uso_oferta-comercial.md): S3, S4; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-032 a RF-034; casos de uso CU-OF-09, CU-OF-10; resultados del Anexo D: 9. [derivado]

#### 1.5.1.6 Maestro de artículos y reportes de calidad

- **Rama y servicio:** 1.5, Servicio de oferta comercial. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-OF-11 Mantener el maestro de artículos; CU-OF-12 Revisar los reportes de calidad del maestro y de publicación. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de oferta comercial» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-OF-11 (03_casos_de_uso_oferta-comercial.md): S3; CU-OF-12 (03_casos_de_uso_oferta-comercial.md): S3; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-142, RF-143, RF-147, RF-148; casos de uso CU-OF-11, CU-OF-12. [derivado]

#### 1.5.2.1 Propuesta diaria de reposición y su ajuste

- **Rama y servicio:** 1.5, Servicio de abastecimiento. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-AB-01 Generar la propuesta diaria de reposición; CU-AB-02 Ajustar y confirmar la propuesta de reposición. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de abastecimiento» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-AB-01 (03_casos_de_uso_abastecimiento.md): S2; CU-AB-02 (03_casos_de_uso_abastecimiento.md): S2; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-144 a RF-146; casos de uso CU-AB-01, CU-AB-02. [derivado]

#### 1.5.2.2 Órdenes de reposición a proveedores

- **Rama y servicio:** 1.5, Servicio de abastecimiento. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-AB-03 Colocar y seguir las órdenes a proveedores. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de abastecimiento» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 247 h en total (UCP, escenario del equipo): análisis 25 h, diseño 49 h, programación 99 h, pruebas 37 h y sobrecarga 37 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-AB-03 (03_casos_de_uso_abastecimiento.md): S1, S3, S4; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** casos de uso CU-AB-03. [derivado]

#### 1.5.2.3 Transferencias y recepción de mercadería

- **Rama y servicio:** 1.5, Servicio de abastecimiento. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-AB-04 Gestionar las transferencias entre tiendas y centros de distribución; CU-AB-05 Registrar la recepción de mercadería en la tienda. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de abastecimiento» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-AB-04 (03_casos_de_uso_abastecimiento.md): S1, S5; CU-AB-05 (03_casos_de_uso_abastecimiento.md): S1, S6; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** casos de uso CU-AB-04, CU-AB-05. [derivado]

#### 1.5.3.1 Disponible: cálculo, traza y consulta

- **Rama y servicio:** 1.5, Servicio de existencias. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-EX-03 Publicar el disponible a los canales; CU-EX-08 Parametrizar el colchón de confianza y la vigencia de la reserva; CU-EX-09 Consultar la traza del cálculo del disponible; CU-EX-01 Consultar la disponibilidad para vender en sala; CU-EX-02 Consultar la disponibilidad en línea. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de existencias» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 1 del Anexo D: Cálculo dinámico por categoría y punto (Caso, cap. 7), con tolerancia respecto del conteo por fijar al inicio del proyecto (propuesta del proponente). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 1.234 h en total (UCP, escenario del equipo): análisis 123 h, diseño 247 h, programación 494 h, pruebas 185 h y sobrecarga 185 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-EX-03 (03_casos_de_uso_existencias.md): S3, S7; CU-EX-08 (03_casos_de_uso_existencias.md): S8, S9; CU-EX-09 (03_casos_de_uso_existencias.md): S9; CU-EX-01 (03_casos_de_uso_existencias.md): S2, S7; CU-EX-02 (03_casos_de_uso_existencias.md): S1, S7; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-036, RF-065, RF-066, RF-087, RF-101, RF-127 a RF-130, RF-149 a RF-152, RF-157, RF-160, RF-161; casos de uso CU-EX-03, CU-EX-08, CU-EX-09, CU-EX-01, CU-EX-02; resultados del Anexo D: 1. [derivado]

#### 1.5.3.2 Reservas de existencia para el canal digital

- **Rama y servicio:** 1.5, Servicio de existencias. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-EX-04 Reservar una unidad para el canal digital; CU-EX-05 Expirar las reservas vencidas; CU-EX-06 Verificar la existencia física antes del cobro; CU-EX-07 Resolver el conflicto de existencia comprometida. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de existencias» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 2 del Anexo D: Bajo 0,3 % al año y cero cancelaciones por falta de existencia durante el evento (Caso, cap. 7). Reclasificado desde RNF-61. Mes 16, solo categorías con existencias en producción, medida sin meta de cero. Mes 21, con pedidos, meta completa.; Resultado 3 del Anexo D: Cero casos (propuesta del proponente).; Resultado 26 del Anexo D: Aviso previo al cobro (RT-16.21) y cumplimiento de la fecha de entrega sobre 97 % (Caso, cap. 7). Reclasificado desde RNF-62. [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 1.234 h en total (UCP, escenario del equipo): análisis 123 h, diseño 247 h, programación 494 h, pruebas 185 h y sobrecarga 185 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-EX-04 (03_casos_de_uso_existencias.md): S3; CU-EX-05 (03_casos_de_uso_existencias.md): S4; CU-EX-06 (03_casos_de_uso_existencias.md): S5; CU-EX-07 (03_casos_de_uso_existencias.md): S6; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-035, RF-037 a RF-042, RF-044, RF-098; casos de uso CU-EX-04, CU-EX-05, CU-EX-06, CU-EX-07; resultados del Anexo D: 2, 3, 26. [derivado]

#### 1.5.3.4 Conteo, exactitud del inventario, merma y probador

- **Rama y servicio:** 1.5, Servicio de existencias. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-EX-10 Parametrizar el conteo cíclico; CU-EX-11 Ejecutar el conteo cíclico; CU-EX-12 Consultar la exactitud del inventario y recibir alertas; CU-EX-13 Clasificar las diferencias y cerrar el ajuste; CU-EX-14 Emitir el informe mensual de merma; CU-EX-15 Gestionar las unidades en el probador. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de existencias» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 4 del Anexo D: Diferencia de conteo bajo 2 % (Caso, cap. 7). Reclasificado desde RNF-63.; Resultado 5 del Anexo D: 100 % de los ajustes con causa (propuesta del proponente) y merma bajo 1 % (Caso, cap. 7).; Resultado 27 del Anexo D: 100 % de las diferencias de su tienda con causa atribuida (propuesta del proponente). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 1.481 h en total (UCP, escenario del equipo): análisis 148 h, diseño 296 h, programación 593 h, pruebas 222 h y sobrecarga 222 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-EX-10 (03_casos_de_uso_existencias.md): S8, S9; CU-EX-11 (03_casos_de_uso_existencias.md): S9; CU-EX-12 (03_casos_de_uso_existencias.md): S9; CU-EX-13 (03_casos_de_uso_existencias.md): S9; CU-EX-14 (03_casos_de_uso_existencias.md): S9; CU-EX-15 (03_casos_de_uso_existencias.md): S9; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-131 a RF-141, RF-153 a RF-156, RF-158, RF-159, RF-162; casos de uso CU-EX-10, CU-EX-11, CU-EX-12, CU-EX-13, CU-EX-14, CU-EX-15; resultados del Anexo D: 4, 5, 27. [derivado]

#### 1.5.3.7 Suspensión y degradación de la publicación por categoría

- **Rama y servicio:** 1.5, Servicio de existencias. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-EX-16 Suspender la publicación de una categoría; CU-EX-17 Degradar por cancelaciones. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de existencias» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 2 del Anexo D: Bajo 0,3 % al año y cero cancelaciones por falta de existencia durante el evento (Caso, cap. 7). Reclasificado desde RNF-61. Mes 16, solo categorías con existencias en producción, medida sin meta de cero. Mes 21, con pedidos, meta completa.; Resultado 25 del Anexo D: Orden de degradación declarado y probado (propuesta del proponente) y 104.000 pedidos en tres días (RNF-22). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-EX-16 (03_casos_de_uso_existencias.md): S8, S9; CU-EX-17 (03_casos_de_uso_existencias.md): S4, S9, S10; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-163, RF-164, RF-179, RF-182, RF-183; casos de uso CU-EX-16, CU-EX-17; resultados del Anexo D: 2, 25. [derivado]

#### 1.5.3.8 Integración de existencias con el sistema de almacenes y con las planillas de Concepción

- **Rama y servicio:** 1.5, Servicio de existencias. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-EX-18 Recibir los movimientos del sistema de almacenes; CU-EX-19 Cargar las existencias de Concepción. [derivado]
- **Queda fuera:** EXC-12: Reemplazar el marketplace ni el sistema de almacenes del centro de distribución principal; EXC-13: Incorporar el centro de distribución de Concepción a un sistema de almacenes ni instalar componentes allí; SP-02: El centro de Concepción se mantiene como está durante el contrato y no es origen de la promesa de entrega digital mientras opere con planillas (equivale al SUP-20 del Subdocumento 2); RC-10: Operar Concepción con sus planillas y entregar sus existencias al servicio de existencias. [derivado]
- **Entregable:** Componentes de software de «Servicio de existencias» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-EX-18 (03_casos_de_uso_existencias.md): S9; CU-EX-19 (03_casos_de_uso_existencias.md): S9, S11; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** casos de uso CU-EX-18, CU-EX-19. [derivado]

#### 1.5.4.1 Promesa de entrega, punto de despacho y elegibilidad del stock

- **Rama y servicio:** 1.5, Servicio de pedidos. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-PE-01 Calcular la fecha prometida de entrega; CU-PE-02 Seleccionar el punto de despacho por costo total de servir; CU-PE-14 Parametrizar la elegibilidad del stock y el límite por cliente. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de pedidos» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 2 del Anexo D: Bajo 0,3 % al año y cero cancelaciones por falta de existencia durante el evento (Caso, cap. 7). Reclasificado desde RNF-61. Mes 16, solo categorías con existencias en producción, medida sin meta de cero. Mes 21, con pedidos, meta completa.; Resultado 11 del Anexo D: 100 % de las asignaciones con costo total (propuesta del proponente).; Resultado 25 del Anexo D: Orden de degradación declarado y probado (propuesta del proponente) y 104.000 pedidos en tres días (RNF-22). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 741 h en total (UCP, escenario del equipo): análisis 74 h, diseño 148 h, programación 296 h, pruebas 111 h y sobrecarga 111 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-PE-01 (03_casos_de_uso_pedidos.md): S2, S3; CU-PE-02 (03_casos_de_uso_pedidos.md): S4; CU-PE-14 (03_casos_de_uso_pedidos.md): S11; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-053, RF-075 a RF-080, RF-180; casos de uso CU-PE-01, CU-PE-02, CU-PE-14; resultados del Anexo D: 2, 11, 25. [derivado]

#### 1.5.4.2 Preautorización, cobro y anulación del pago del pedido

- **Rama y servicio:** 1.5, Servicio de pedidos. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-PE-03 Aceptar el pedido y preautorizar el medio de pago; CU-PE-04 Capturar el cobro al confirmarse la preparación; CU-PE-08 Cancelar el pedido y anular la preautorización; CU-PE-09 Conciliar las preautorizaciones vencidas sin captura. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de pedidos» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 2 del Anexo D: Bajo 0,3 % al año y cero cancelaciones por falta de existencia durante el evento (Caso, cap. 7). Reclasificado desde RNF-61. Mes 16, solo categorías con existencias en producción, medida sin meta de cero. Mes 21, con pedidos, meta completa.; Resultado 3 del Anexo D: Cero casos (propuesta del proponente).; Resultado 26 del Anexo D: Aviso previo al cobro (RT-16.21) y cumplimiento de la fecha de entrega sobre 97 % (Caso, cap. 7). Reclasificado desde RNF-62. [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 988 h en total (UCP, escenario del equipo): análisis 99 h, diseño 198 h, programación 395 h, pruebas 148 h y sobrecarga 148 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-PE-03 (03_casos_de_uso_pedidos.md): S5; CU-PE-04 (03_casos_de_uso_pedidos.md): S5, S6; CU-PE-08 (03_casos_de_uso_pedidos.md): S5; CU-PE-09 (03_casos_de_uso_pedidos.md): S5; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-043, RF-045, RF-047 a RF-051; casos de uso CU-PE-03, CU-PE-04, CU-PE-08, CU-PE-09; resultados del Anexo D: 2, 3, 26. [derivado]

#### 1.5.4.3 Resolución de pedidos sin existencia, reasignación y alternativas al cliente

- **Rama y servicio:** 1.5, Servicio de pedidos. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-PE-05 Resolver un pedido cuya unidad no existe; CU-PE-06 Reasignar el pedido a otro punto de despacho; CU-PE-07 Ofrecer al cliente las alternativas de resolución. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de pedidos» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 2 del Anexo D: Bajo 0,3 % al año y cero cancelaciones por falta de existencia durante el evento (Caso, cap. 7). Reclasificado desde RNF-61. Mes 16, solo categorías con existencias en producción, medida sin meta de cero. Mes 21, con pedidos, meta completa.; Resultado 3 del Anexo D: Cero casos (propuesta del proponente).; Resultado 11 del Anexo D: 100 % de las asignaciones con costo total (propuesta del proponente). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 741 h en total (UCP, escenario del equipo): análisis 74 h, diseño 148 h, programación 296 h, pruebas 111 h y sobrecarga 111 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-PE-05 (03_casos_de_uso_pedidos.md): S7; CU-PE-06 (03_casos_de_uso_pedidos.md): S7; CU-PE-07 (03_casos_de_uso_pedidos.md): S8; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-046, RF-056 a RF-061, RF-074; casos de uso CU-PE-05, CU-PE-06, CU-PE-07; resultados del Anexo D: 2, 3, 11. [derivado]

#### 1.5.4.4 Estado único del pedido y sus consultas

- **Rama y servicio:** 1.5, Servicio de pedidos. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-PE-10 Consultar el estado único del pedido; CU-PE-11 Consultar las compras y las devoluciones; CU-PE-12 Atender en el mesón la consulta de un pedido. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de pedidos» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 10 del Anexo D: Estado único y consistente en todos los canales (RT-05.29).; Resultado 26 del Anexo D: Aviso previo al cobro (RT-16.21) y cumplimiento de la fecha de entrega sobre 97 % (Caso, cap. 7). Reclasificado desde RNF-62. [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 741 h en total (UCP, escenario del equipo): análisis 74 h, diseño 148 h, programación 296 h, pruebas 111 h y sobrecarga 111 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-PE-10 (03_casos_de_uso_pedidos.md): S9; CU-PE-11 (03_casos_de_uso_pedidos.md): S9; CU-PE-12 (03_casos_de_uso_pedidos.md): S9; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-052, RF-067, RF-068, RF-072, RF-073; casos de uso CU-PE-10, CU-PE-11, CU-PE-12; resultados del Anexo D: 10, 26. [derivado]

#### 1.5.4.5 Seguimiento y cumplimiento de la promesa de entrega

- **Rama y servicio:** 1.5, Servicio de pedidos. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-PE-13 Priorizar los pedidos próximos a vencer su promesa; CU-PE-15 Seguir el pedido con el transportista hasta la entrega. [derivado]
- **Queda fuera:** EXC-07: Sustituir a los transportistas de última milla. [derivado]
- **Entregable:** Componentes de software de «Servicio de pedidos» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-PE-13 (03_casos_de_uso_pedidos.md): S10; CU-PE-15 (03_casos_de_uso_pedidos.md): S1, S12; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-062, RF-063, RF-081; casos de uso CU-PE-13, CU-PE-15. [derivado]

#### 1.5.5.1 Punto de venta nuevo: registro y cobro de ventas, reversas, cierre de caja y medios de pago

- **Rama y servicio:** 1.5, Servicio de ventas. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-VE-01 Registrar y cobrar una venta; CU-VE-02 Reversar una venta o un pago; CU-VE-03 Cerrar la caja del turno; CU-VE-08 Desactivar los medios de pago de mayor fricción. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de ventas» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 9 del Anexo D: 0,5 % o menos, verificado por muestreo propio (propuesta del proponente). La política de precios en sala está pendiente (supuestos SUP-08 y SUP-09).; Resultado 25 del Anexo D: Orden de degradación declarado y probado (propuesta del proponente) y 104.000 pedidos en tres días (RNF-22). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 988 h en total (UCP, escenario del equipo): análisis 99 h, diseño 198 h, programación 395 h, pruebas 148 h y sobrecarga 148 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-VE-01 (03_casos_de_uso_ventas.md): S1, S3; CU-VE-02 (03_casos_de_uso_ventas.md): S1, S4; CU-VE-03 (03_casos_de_uso_ventas.md): S1, S4; CU-VE-08 (03_casos_de_uso_ventas.md): S7; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-001, RF-181; casos de uso CU-VE-01, CU-VE-02, CU-VE-03, CU-VE-08; resultados del Anexo D: 9, 25. [derivado]

#### 1.5.5.2 Punto de venta con operación sin conexión: reconciliación y validación posterior

- **Rama y servicio:** 1.5, Servicio de ventas. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-VE-04 Operar la tienda sin enlace; CU-VE-05 Reconciliar las ventas hechas sin enlace; CU-VE-06 Revisar el informe de excepciones de la conciliación; CU-VE-07 Validar las operaciones cursadas sin enlace. [derivado]
- **Queda fuera:** EXC-16: Abrir tarjetas ni ampliar cupos sin conexión. [derivado]
- **Entregable:** Componentes de software de «Servicio de ventas» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 988 h en total (UCP, escenario del equipo): análisis 99 h, diseño 198 h, programación 395 h, pruebas 148 h y sobrecarga 148 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-VE-04 (03_casos_de_uso_ventas.md): S1, S2, S6; CU-VE-05 (03_casos_de_uso_ventas.md): S6; CU-VE-06 (03_casos_de_uso_ventas.md): S4; CU-VE-07 (03_casos_de_uso_ventas.md): S5; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-082 a RF-086, RF-088, RF-094 a RF-097, RF-099; casos de uso CU-VE-04, CU-VE-05, CU-VE-06, CU-VE-07. [derivado]

#### 1.5.5.6 Ventas del canal digital y enrutamiento de los documentos tributarios al sistema de gestión empresarial

- **Rama y servicio:** 1.5, Servicio de ventas. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-VE-09 Registrar las ventas del canal digital; CU-VE-10 Enrutar los documentos tributarios al ERP/DTE. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de ventas» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-VE-09 (03_casos_de_uso_ventas.md): S4; CU-VE-10 (03_casos_de_uso_ventas.md): S4; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-100; casos de uso CU-VE-09, CU-VE-10. [derivado]

#### 1.5.5.7 Cobro con la tarjeta de la casa

- **Rama y servicio:** 1.5, Servicio de ventas. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-VE-11 Cobrar con la tarjeta de la casa. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de ventas» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 247 h en total (UCP, escenario del equipo): análisis 25 h, diseño 49 h, programación 99 h, pruebas 37 h y sobrecarga 37 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-VE-11 (03_casos_de_uso_ventas.md): S5, S8; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** casos de uso CU-VE-11. [derivado]

#### 1.5.6.1 Cálculo de la base de comisión

- **Rama y servicio:** 1.5, Servicio de comisiones. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-CM-01 Calcular la base de comisión por vendedor, tienda y canal. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de comisiones» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 12 del Anexo D: 100 % de los despachos desde tienda atribuidos (propuesta del proponente). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 247 h en total (UCP, escenario del equipo): análisis 25 h, diseño 49 h, programación 99 h, pruebas 37 h y sobrecarga 37 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-CM-01 (03_casos_de_uso_comisiones.md): S2; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-054, RF-071; casos de uso CU-CM-01; resultados del Anexo D: 12. [derivado]

#### 1.5.6.2 Entrega de la base de comisión al sistema de remuneraciones

- **Rama y servicio:** 1.5, Servicio de comisiones. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-CM-02 Transmitir la base de comisión al sistema de remuneraciones. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de comisiones» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 12 del Anexo D: 100 % de los despachos desde tienda atribuidos (propuesta del proponente). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 247 h en total (UCP, escenario del equipo): análisis 25 h, diseño 49 h, programación 99 h, pruebas 37 h y sobrecarga 37 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-CM-02 (03_casos_de_uso_comisiones.md): S3; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-055; casos de uso CU-CM-02; resultados del Anexo D: 12. [derivado]

#### 1.5.6.3 Revisión de la atribución de comisiones

- **Rama y servicio:** 1.5, Servicio de comisiones. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-CM-03 Revisar la atribución de una comisión. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de comisiones» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 247 h en total (UCP, escenario del equipo): análisis 25 h, diseño 49 h, programación 99 h, pruebas 37 h y sobrecarga 37 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-CM-03 (03_casos_de_uso_comisiones.md): S1, S4; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** casos de uso CU-CM-03. [derivado]

#### 1.5.7.1 Existencia declarada por el vendedor y su publicación

- **Rama y servicio:** 1.5, Servicio de marketplace. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-MK-01 Declarar y actualizar la existencia del vendedor; CU-MK-02 Publicar la existencia vigente y despublicar la vencida. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de marketplace» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-MK-01 (03_casos_de_uso_marketplace.md): S2; CU-MK-02 (03_casos_de_uso_marketplace.md): S3; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-102 a RF-104, RF-109, RF-124; casos de uso CU-MK-01, CU-MK-02. [derivado]

#### 1.5.7.2 Evaluación de vendedores y su consulta

- **Rama y servicio:** 1.5, Servicio de marketplace. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-MK-03 Consultar los pedidos, las devoluciones y la evaluación; CU-MK-04 Calcular los indicadores de nivel de servicio por vendedor; CU-MK-05 Dar a conocer las reglas de evaluación al vendedor; CU-MK-06 Aplicar la consecuencia escalonada de un incumplimiento. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de marketplace» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 14 del Anexo D: 100 % de los vendedores con nivel de servicio medido (propuesta del proponente). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 988 h en total (UCP, escenario del equipo): análisis 99 h, diseño 198 h, programación 395 h, pruebas 148 h y sobrecarga 148 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-MK-03 (03_casos_de_uso_marketplace.md): S2; CU-MK-04 (03_casos_de_uso_marketplace.md): S4; CU-MK-05 (03_casos_de_uso_marketplace.md): S2; CU-MK-06 (03_casos_de_uso_marketplace.md): S5; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-105, RF-110 a RF-112, RF-119 a RF-123; casos de uso CU-MK-03, CU-MK-04, CU-MK-05, CU-MK-06; resultados del Anexo D: 14. [derivado]

#### 1.5.7.4 Devoluciones, base de comisión y liquidación de marketplace

- **Rama y servicio:** 1.5, Servicio de marketplace. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-MK-07 Gestionar una devolución de producto de marketplace; CU-MK-10 Informar la base de comisión de marketplace al ERP; CU-MK-11 Conciliar la liquidación de un vendedor. [derivado]
- **Queda fuera:** EXC-04: Desarrollar la plataforma de vendedores del marketplace ni operar su logística. [derivado]
- **Entregable:** Componentes de software de «Servicio de marketplace» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 13 del Anexo D: Aviso al vendedor en 15 minutos o menos en cada devolución (propuesta del proponente, RNF-66). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 741 h en total (UCP, escenario del equipo): análisis 74 h, diseño 148 h, programación 296 h, pruebas 111 h y sobrecarga 111 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-MK-07 (03_casos_de_uso_marketplace.md): S6; CU-MK-10 (03_casos_de_uso_marketplace.md): S9; CU-MK-11 (03_casos_de_uso_marketplace.md): S1, S10; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-106 a RF-108, RF-125, RF-126; casos de uso CU-MK-07, CU-MK-10, CU-MK-11; resultados del Anexo D: 13. [derivado]

#### 1.5.7.5 Identificación del vendedor y separación de la existencia propia

- **Rama y servicio:** 1.5, Servicio de marketplace. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-MK-08 Identificar al vendedor y las condiciones en la compra; CU-MK-09 Impedir que un pedido intermediado use existencia propia. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de marketplace» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-MK-08 (03_casos_de_uso_marketplace.md): S7; CU-MK-09 (03_casos_de_uso_marketplace.md): S8; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-113 a RF-118; casos de uso CU-MK-08, CU-MK-09. [derivado]

#### 1.5.8.1 Atención de garantía legal en el mesón, con sus plazos

- **Rama y servicio:** 1.5, Servicio de posventa. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-PV-01 Atender un caso de garantía legal íntegramente en el mesón; CU-PV-02 Ofrecer y registrar la opción de garantía legal; CU-PV-03 Parametrizar el plazo de garantía legal por tipo de producto. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de posventa» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 15 del Anexo D: Cero derivaciones (restricción 7 del Caso). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 741 h en total (UCP, escenario del equipo): análisis 74 h, diseño 148 h, programación 296 h, pruebas 111 h y sobrecarga 111 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-PV-01 (03_casos_de_uso_posventa.md): S1; CU-PV-02 (03_casos_de_uso_posventa.md): S2; CU-PV-03 (03_casos_de_uso_posventa.md): S3; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-187, RF-188, RF-192 a RF-195; casos de uso CU-PV-01, CU-PV-02, CU-PV-03; resultados del Anexo D: 15. [derivado]

#### 1.5.8.2 Devolución y aptitud de la unidad devuelta

- **Rama y servicio:** 1.5, Servicio de posventa. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-PV-04 Reingresar una unidad devuelta según su aptitud. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de posventa» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 5 del Anexo D: 100 % de los ajustes con causa (propuesta del proponente) y merma bajo 1 % (Caso, cap. 7).; Resultado 13 del Anexo D: Aviso al vendedor en 15 minutos o menos en cada devolución (propuesta del proponente, RNF-66). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 247 h en total (UCP, escenario del equipo): análisis 25 h, diseño 49 h, programación 99 h, pruebas 37 h y sobrecarga 37 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-PV-04 (03_casos_de_uso_posventa.md): S4; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-189 a RF-191; casos de uso CU-PV-04; resultados del Anexo D: 5, 13. [derivado]

#### 1.5.8.3 Resolución al consumidor y recuperación contra el tercero responsable

- **Rama y servicio:** 1.5, Servicio de posventa. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-PV-05 Seguir la resolución al consumidor y la recuperación contra el tercero. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de posventa» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 247 h en total (UCP, escenario del equipo): análisis 25 h, diseño 49 h, programación 99 h, pruebas 37 h y sobrecarga 37 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-PV-05 (03_casos_de_uso_posventa.md): S5; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-196 a RF-198; casos de uso CU-PV-05. [derivado]

#### 1.5.9.1 Consolidación de los registros de clientes

- **Rama y servicio:** 1.5, Servicio de clientes Retail. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-CL-01 Consolidar los registros duplicados de un cliente. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de clientes Retail» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 247 h en total (UCP, escenario del equipo): análisis 25 h, diseño 49 h, programación 99 h, pruebas 37 h y sobrecarga 37 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-CL-01 (03_casos_de_uso_clientes-retail.md): S1, S2; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-227; casos de uso CU-CL-01. [derivado]

#### 1.5.9.2 Puntos y sincronización con el sistema de fidelización

- **Rama y servicio:** 1.5, Servicio de clientes Retail. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-CL-02 Mantener los puntos y la fidelización sincronizados. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de clientes Retail» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 247 h en total (UCP, escenario del equipo): análisis 25 h, diseño 49 h, programación 99 h, pruebas 37 h y sobrecarga 37 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-CL-02 (03_casos_de_uso_clientes-retail.md): S1, S3; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-228, RF-231; casos de uso CU-CL-02. [derivado]

#### 1.5.9.3 Segmentos y campañas con atributos comerciales

- **Rama y servicio:** 1.5, Servicio de clientes Retail. **Etapa:** 2. **Método:** UCP.
- **Ventana:** los meses 13 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-CL-03 Construir un segmento con atributos comerciales; CU-CL-04 Ejecutar una campaña sobre un segmento. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de clientes Retail» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 2 (mes 18), marcha blanca de la Etapa 2 (meses 19 y 20) y paso a producción (mes 21) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-CL-03 (03_casos_de_uso_clientes-retail.md): S1, S4; CU-CL-04 (03_casos_de_uso_clientes-retail.md): S1, S5; Ventana de los meses 13 a 18 (contrato): Art. 17: desarrollo de la etapa 2. [derivado]
- **Referencias:** RF-229, RF-230; casos de uso CU-CL-03, CU-CL-04. [derivado]

#### 1.5.10.1 Evaluación crediticia, apertura de tarjeta y ampliación de cupo

- **Rama y servicio:** 1.5, Servicio de originación de crédito. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-OR-01 Evaluar la solicitud y abrir una tarjeta en el mostrador; CU-OR-02 Ofrecer la tarjeta y consultar el resultado; CU-OR-05 Controlar los intentos de evaluación; CU-OR-09 Solicitar la ampliación de un cupo con enlace. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de originación de crédito» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 16 del Anexo D: 8 segundos o menos (RT-09.01 y RNF-06).; Resultado 20 del Anexo D: El proceso impide aceptar un crédito sin la información (propuesta del proponente).; Resultado 23 del Anexo D: Cumplidos antes de 2029 (Caso, cap. 7), es decir, a más tardar en el mes 24 del proyecto.; Resultado 28 del Anexo D: 8 segundos o menos en la evaluación y la información obligatoria antes de aceptar. [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 988 h en total (UCP, escenario del equipo): análisis 99 h, diseño 198 h, programación 395 h, pruebas 148 h y sobrecarga 148 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-OR-01 (03_casos_de_uso_originacion-credito.md): S1, S2, S7; CU-OR-02 (03_casos_de_uso_originacion-credito.md): S7; CU-OR-05 (03_casos_de_uso_originacion-credito.md): S7; CU-OR-09 (03_casos_de_uso_originacion-credito.md): S6; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-220 a RF-226; casos de uso CU-OR-01, CU-OR-02, CU-OR-05, CU-OR-09; resultados del Anexo D: 16, 20, 23, 28. [derivado]

#### 1.5.10.2 Simulación del costo total del crédito con la tasa máxima vigente

- **Rama y servicio:** 1.5, Servicio de originación de crédito. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-OR-03 Simular el costo total del crédito; CU-OR-04 Mantener la tasa máxima convencional vigente. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de originación de crédito» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-OR-03 (03_casos_de_uso_originacion-credito.md): S1; CU-OR-04 (03_casos_de_uso_originacion-credito.md): S7; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-218, RF-219; casos de uso CU-OR-03, CU-OR-04. [derivado]

#### 1.5.10.4 Autorización de compra a cuotas sin enlace y sus topes

- **Rama y servicio:** 1.5, Servicio de originación de crédito. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-OR-06 Parametrizar los topes y la ventana de enfriamiento; CU-OR-07 Autorizar compra a cuotas sin enlace contra el cupo preaprobado; CU-OR-08 Mantener el cupo preaprobado en la tienda. [derivado]
- **Queda fuera:** RC-11: Fijar el apetito de riesgo del crédito sin conexión (topes, antigüedad del registro local y exclusiones); EXC-16: Abrir tarjetas ni ampliar cupos sin conexión. [derivado]
- **Entregable:** Componentes de software de «Servicio de originación de crédito» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 741 h en total (UCP, escenario del equipo): análisis 74 h, diseño 148 h, programación 296 h, pruebas 111 h y sobrecarga 111 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-OR-06 (03_casos_de_uso_originacion-credito.md): S5; CU-OR-07 (03_casos_de_uso_originacion-credito.md): S3, S4; CU-OR-08 (03_casos_de_uso_originacion-credito.md): S3; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-089 a RF-093; casos de uso CU-OR-06, CU-OR-07, CU-OR-08. [derivado]

#### 1.5.11.1 Mora y gestión de cobranza

- **Rama y servicio:** 1.5, Servicio de cartera de crédito. **Etapa:** 1 y 2. **Método:** UCP.
- **Ventana:** los meses 1 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-CA-01 Iniciar y registrar una gestión de cobranza; CU-CA-05 Calcular la mora y actualizar las cuentas. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de cartera de crédito» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Pasos a producción de la Etapa 1 (mes 16) y de la Etapa 2 (mes 21), con la cartera migrada por tramos [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-CA-01 (03_casos_de_uso_cartera-credito.md): S8; CU-CA-05 (03_casos_de_uso_cartera-credito.md): S1; Ventana de los meses 1 a 18 (contrato): Art. 17 y Anexo D 24: cartera migra en las dos etapas. [derivado]
- **Referencias:** RF-211 a RF-213; casos de uso CU-CA-01, CU-CA-05. [derivado]

#### 1.5.11.2 Repactación, pagos y estado de cuenta

- **Rama y servicio:** 1.5, Servicio de cartera de crédito. **Etapa:** 1 y 2. **Método:** UCP.
- **Ventana:** los meses 1 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-CA-02 Repactar las condiciones de una deuda; CU-CA-04 Registrar el pago de una cuota; CU-CA-03 Consultar el estado de cuenta y los documentos. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de cartera de crédito» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 18 del Anexo D: Cero repactaciones sin evidencia (Caso, cap. 7).; Resultado 23 del Anexo D: Cumplidos antes de 2029 (Caso, cap. 7), es decir, a más tardar en el mes 24 del proyecto. [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Pasos a producción de la Etapa 1 (mes 16) y de la Etapa 2 (mes 21), con la cartera migrada por tramos [derivado]
- **Esfuerzo estimado:** 741 h en total (UCP, escenario del equipo): análisis 74 h, diseño 148 h, programación 296 h, pruebas 111 h y sobrecarga 111 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-CA-02 (03_casos_de_uso_cartera-credito.md): S1, S2; CU-CA-04 (03_casos_de_uso_cartera-credito.md): S1, S4, S5; CU-CA-03 (03_casos_de_uso_cartera-credito.md): S3; Ventana de los meses 1 a 18 (contrato): Art. 17 y Anexo D 24: cartera migra en las dos etapas. [derivado]
- **Referencias:** RF-069, RF-070; casos de uso CU-CA-02, CU-CA-04, CU-CA-03; resultados del Anexo D: 18, 23. [derivado]

#### 1.5.11.5 Conciliación diaria y convivencia con la plataforma de crédito de 2011

- **Rama y servicio:** 1.5, Servicio de cartera de crédito. **Etapa:** 1 y 2. **Método:** UCP.
- **Ventana:** los meses 1 a 18 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-CA-06 Revisar la conciliación diaria de la migración; CU-CA-07 Convivir con la plataforma de crédito de 2011. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de cartera de crédito» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 23 del Anexo D: Cumplidos antes de 2029 (Caso, cap. 7), es decir, a más tardar en el mes 24 del proyecto.; Resultado 24 del Anexo D: Cero diferencias sin explicar (restricción 8 del Caso). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Pasos a producción de la Etapa 1 (mes 16) y de la Etapa 2 (mes 21), con la cartera migrada por tramos [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-CA-06 (03_casos_de_uso_cartera-credito.md): S6, S7; CU-CA-07 (03_casos_de_uso_cartera-credito.md): S1, S6; Ventana de los meses 1 a 18 (contrato): Art. 17 y Anexo D 24: cartera migra en las dos etapas. [derivado]
- **Referencias:** RF-216; casos de uso CU-CA-06, CU-CA-07; resultados del Anexo D: 23, 24. [derivado]

#### 1.5.12.1 Información precontractual entregada, aceptada y consultable

- **Rama y servicio:** 1.5, Servicio de evidencia financiera. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-EV-01 Entregar la información precontractual del crédito; CU-EV-02 Aceptar la información precontractual con firma electrónica; CU-EV-08 Consultar la información precontractual del crédito. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de evidencia financiera» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 17 del Anexo D: Registro trazable por operación (Caso, cap. 7).; Resultado 20 del Anexo D: El proceso impide aceptar un crédito sin la información (propuesta del proponente).; Resultado 23 del Anexo D: Cumplidos antes de 2029 (Caso, cap. 7), es decir, a más tardar en el mes 24 del proyecto.; Resultado 28 del Anexo D: 8 segundos o menos en la evaluación y la información obligatoria antes de aceptar. [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 741 h en total (UCP, escenario del equipo): análisis 74 h, diseño 148 h, programación 296 h, pruebas 111 h y sobrecarga 111 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-EV-01 (03_casos_de_uso_evidencia-financiera.md): S4, S8; CU-EV-02 (03_casos_de_uso_evidencia-financiera.md): S1, S4, S8; CU-EV-08 (03_casos_de_uso_evidencia-financiera.md): S2; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-199 a RF-206, RF-217; casos de uso CU-EV-01, CU-EV-02, CU-EV-08; resultados del Anexo D: 17, 20, 23, 28. [derivado]

#### 1.5.12.2 Consentimiento de modificaciones de condiciones y su enlace con la cobranza

- **Rama y servicio:** 1.5, Servicio de evidencia financiera. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-EV-03 Registrar el consentimiento de una modificación de condiciones; CU-EV-07 Enlazar la repactación con su cobranza y su consentimiento. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de evidencia financiera» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 18 del Anexo D: Cero repactaciones sin evidencia (Caso, cap. 7).; Resultado 23 del Anexo D: Cumplidos antes de 2029 (Caso, cap. 7), es decir, a más tardar en el mes 24 del proyecto. [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-EV-03 (03_casos_de_uso_evidencia-financiera.md): S5, S8; CU-EV-07 (03_casos_de_uso_evidencia-financiera.md): S5, S8; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-207, RF-208, RF-214, RF-215; casos de uso CU-EV-03, CU-EV-07; resultados del Anexo D: 18, 23. [derivado]

#### 1.5.12.3 Reconstrucción y recuperación de la evidencia del consentimiento

- **Rama y servicio:** 1.5, Servicio de evidencia financiera. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-EV-04 Reconstruir el acto de consentimiento; CU-EV-05 Recuperar los antecedentes de una operación desde el archivo. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de evidencia financiera» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 19 del Anexo D: Plazo del crédito más seis años, con recuperación a diez años en 5 minutos o menos (propuesta del proponente, RNF-42, RNF-43 y RNF-57). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-EV-04 (03_casos_de_uso_evidencia-financiera.md): S8; CU-EV-05 (03_casos_de_uso_evidencia-financiera.md): S8; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-209, RF-210; casos de uso CU-EV-04, CU-EV-05; resultados del Anexo D: 19. [derivado]

#### 1.5.13.1 Inventario de flujos de cruce autorizados y registro de los cruces

- **Rama y servicio:** 1.5, Servicio de control de cruces. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-CC-01 Mantener el inventario de flujos de cruce autorizados; CU-CC-03 Revisar los cruces ejecutados y los intentos bloqueados. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de control de cruces» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 22 del Anexo D: 100 % de los cruces registrados (RF-165). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-CC-01 (03_casos_de_uso_control-cruces.md): S2, S7; CU-CC-03 (03_casos_de_uso_control-cruces.md): S5, S7; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-165 a RF-169; casos de uso CU-CC-01, CU-CC-03; resultados del Anexo D: 22. [derivado]

#### 1.5.13.2 Rechazo de cruces no autorizados entre los ámbitos

- **Rama y servicio:** 1.5, Servicio de control de cruces. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-CC-02 Intentar una campaña con atributos de origen financiero; CU-CC-04 Intentar un proceso crediticio con atributos de origen Retail. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de control de cruces» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 21 del Anexo D: Implementada y documentada (Caso, cap. 7), con cero hallazgos críticos o altos en la prueba de penetración (propuesta del proponente). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-CC-02 (03_casos_de_uso_control-cruces.md): S3, S7; CU-CC-04 (03_casos_de_uso_control-cruces.md): S4, S7; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-170 a RF-172; casos de uso CU-CC-02, CU-CC-04; resultados del Anexo D: 21. [derivado]

#### 1.5.13.3 Correspondencia de identificadores y evaluación de impacto sobre la frontera

- **Rama y servicio:** 1.5, Servicio de control de cruces. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-CC-05 Resolver la correspondencia de identificadores entre ámbitos; CU-CC-06 Evaluar el impacto de una iniciativa sobre la frontera de datos. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Servicio de control de cruces» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 21 del Anexo D: Implementada y documentada (Caso, cap. 7), con cero hallazgos críticos o altos en la prueba de penetración (propuesta del proponente). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-CC-05 (03_casos_de_uso_control-cruces.md): S6, S7; CU-CC-06 (03_casos_de_uso_control-cruces.md): S7; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-173 a RF-176; casos de uso CU-CC-05, CU-CC-06; resultados del Anexo D: 21. [derivado]

#### 1.5.14.1 Identidad individual y administración de identidades, roles y ámbitos

- **Rama y servicio:** 1.5, Base tecnológica. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-BT-01 Ingresar a una terminal compartida con identidad individual; CU-BT-12 Administrar identidades, roles y ámbitos. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Base tecnológica» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-BT-01 (03_casos_de_uso_base-tecnologica.md): S10; CU-BT-12 (03_casos_de_uso_base-tecnologica.md): S1, S8; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-002 a RF-006; casos de uso CU-BT-01, CU-BT-12. [derivado]

#### 1.5.14.2 Habilitación, revocación y conciliación de accesos

- **Rama y servicio:** 1.5, Base tecnológica. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-BT-02 Habilitar y revocar funciones según la capacitación normativa; CU-BT-03 Patrocinar el acceso temporal de un repositor externo; CU-BT-04 Operar como repositor externo con identidad individualizada; CU-BT-05 Retirar los accesos al término del vínculo; CU-BT-06 Conciliar los accesos contra la nómina activa. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Base tecnológica» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 1.234 h en total (UCP, escenario del equipo): análisis 123 h, diseño 247 h, programación 494 h, pruebas 185 h y sobrecarga 185 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-BT-02 (03_casos_de_uso_base-tecnologica.md): S5, S10; CU-BT-03 (03_casos_de_uso_base-tecnologica.md): S3, S10; CU-BT-04 (03_casos_de_uso_base-tecnologica.md): S3; CU-BT-06 (03_casos_de_uso_base-tecnologica.md): S2, S4; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-007 a RF-015; casos de uso CU-BT-02, CU-BT-03, CU-BT-04, CU-BT-05, CU-BT-06. [derivado]

#### 1.5.14.5 Orden de degradación y ventanas de congelamiento

- **Rama y servicio:** 1.5, Base tecnológica. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-BT-07 Declarar el orden y los criterios de degradación; CU-BT-08 Parametrizar las ventanas de congelamiento y bloquear intervenciones. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Base tecnológica» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 25 del Anexo D: Orden de degradación declarado y probado (propuesta del proponente) y 104.000 pedidos en tres días (RNF-22). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-BT-07 (03_casos_de_uso_base-tecnologica.md): S6; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** RF-177, RF-178, RF-184 a RF-186; casos de uso CU-BT-07, CU-BT-08; resultados del Anexo D: 25. [derivado]

#### 1.5.14.6 Plataforma de integración y convivencia con el sistema central de 2009

- **Rama y servicio:** 1.5, Base tecnológica. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-BT-09 Convivir con el sistema central de 2009; CU-BT-10 Administrar la plataforma de integración. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Base tecnológica» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-BT-09 (03_casos_de_uso_base-tecnologica.md): S1, S7; CU-BT-10 (03_casos_de_uso_base-tecnologica.md): S1; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** casos de uso CU-BT-09, CU-BT-10. [derivado]

#### 1.5.14.7 Observabilidad y capacidad analítica

- **Rama y servicio:** 1.5, Base tecnológica. **Etapa:** 1. **Método:** UCP.
- **Ventana:** los meses 1 a 12 (contrato)
- **Descripción del trabajo:** Análisis, diseño, construcción y pruebas de los casos de uso: CU-BT-11 Observar la operación y atender alertas; CU-BT-13 Consultar tableros y exportar informes por ámbito. [derivado]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Componentes de software de «Base tecnológica» que resuelven esos casos de uso, desplegados y probados. [derivado]
- **Criterio de aceptación:** Resultado 21 del Anexo D: Implementada y documentada (Caso, cap. 7), con cero hallazgos críticos o altos en la prueba de penetración (propuesta del proponente). [derivado]
- **Responsable:** Arquitecto de Solución. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Certificación de la Etapa 1 (mes 12), marcha blanca de la Etapa 1 (meses 13 a 15) y paso a producción (mes 16) [derivado]
- **Esfuerzo estimado:** 494 h en total (UCP, escenario del equipo): análisis 49 h, diseño 99 h, programación 198 h, pruebas 74 h y sobrecarga 74 h. Por perfil: por estimar (sd-12). [derivado]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** CU-BT-11 (03_casos_de_uso_base-tecnologica.md): S1; CU-BT-13 (03_casos_de_uso_base-tecnologica.md): S1; Ventana de los meses 1 a 12 (contrato): Art. 17: desarrollo de la etapa 1. [derivado]
- **Referencias:** casos de uso CU-BT-11, CU-BT-13; resultados del Anexo D: 21. [derivado]

### Rama 1.6

#### 1.6.1 Catálogo de interfaces rediseñadas con contratos y niveles de servicio de integración

- **Rama y servicio:** 1.6. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 2 a 5 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 2 a 5 (propuesta): catálogo de interfaces. [derivado]
- **Referencias:** sd-03, 3.2.1 y 3.3.1 (la plataforma de integración reemplaza las catorce conexiones directas). [derivado]

#### 1.6.2 Rediseño de las integraciones de la Etapa 1 (precios y existencia, crédito con el sistema de gestión empresarial, cobranza y prevención de pérdidas)

- **Rama y servicio:** 1.6. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 5 a 18 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 5 a 18 (propuesta): interfaces de la Etapa 1; cartera: Etapa 1 y 2; interfaz de la Etapa 1. [derivado]
- **Referencias:** sd-03, 3.3.1 (plataforma de integración). [derivado]

#### 1.6.3 Rediseño de las integraciones de la Etapa 2 (pedidos, marketplace y fidelización)

- **Rama y servicio:** 1.6. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 13 a 18 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 13 a 18 (propuesta): interfaz de la Etapa 2. [derivado]
- **Referencias:** sd-03, 3.3.1 (plataforma de integración). [derivado]

#### 1.6.9 Canal de intercambio con los proveedores de mercadería

- **Rama y servicio:** 1.6. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 13 a 18 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 13 a 18 (propuesta): abastecimiento es de la Etapa 2. [derivado]
- **Referencias:** 940 proveedores; frontera con el caso de uso de órdenes a proveedores del UCP; RNF-53 (Anexo B): estándar de intercambio de órdenes y avisos con proveedores. [derivado]

#### 1.6.10 Entrega de reportes a las autoridades fiscalizadoras

- **Rama y servicio:** 1.6. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 8 a 12 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 8 a 12 (propuesta): la filial emisora está en la Etapa 1. [derivado]
- **Referencias:** sd-03, 3.3.1 (los organismos fiscalizadores reciben los reportes). [derivado]

#### 1.6.11 Certificación de las integraciones con evidencia de conciliación

- **Rama y servicio:** 1.6. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 10 a 18 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: acta; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 10 a 18 (propuesta): certificación de las dos etapas. [derivado]
- **Referencias:** sd-03, 3.4.5 (conciliación y retorno ensayado entre sistemas). [derivado]

#### 1.6.12 Modalidad de contingencia tributaria aprobada y probada con el ERP/DTE

- **Rama y servicio:** 1.6. **Etapa:** 1. **Método:** tres valores.
- **Ventana:** los meses 4 a 6 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Arquitecto de Solución, con apoyo del Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 4 a 6 (propuesta): sd-03, 3.4.5: aprobada y probada antes de comprometer la operación sin enlace; antes del piloto. [derivado]
- **Referencias:** sd-03, 3.4.5; antes de comprometer la operación sin enlace. [derivado]

### Rama 1.7

#### 1.7.1 Plan de migración con estrategia de corte y de retorno e inventario de datos históricos

- **Rama y servicio:** 1.7. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 2 a 4 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plan; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 2 a 4 (propuesta): antes de migrar; RT-05.15. [derivado]
- **Referencias:** RT-05.11; RT-05.15. [derivado]

#### 1.7.3 Maestro de artículos saneado y validado (268.000 referencias)

- **Rama y servicio:** 1.7. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 4 a 10 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 4 a 10 (propuesta): antes de la marcha blanca. [derivado]
- **Referencias:** sd-03, 3.2.1 (causa C1: el maestro de artículos) y 3.3.2. [derivado]

#### 1.7.4 Corte de inventario en las 24 instalaciones que no cierran

- **Rama y servicio:** 1.7. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 11 a 15 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 11 a 15 (propuesta): corte antes del paso a producción. [derivado]
- **Referencias:** por definir [por definir]

#### 1.7.5 Migración del histórico comercial (ventas y pedidos)

- **Rama y servicio:** 1.7. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 8 a 15 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** EXC-18: Migrar datos históricos fuera de la lista de RT-05.15. [derivado]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 8 a 15 (propuesta): antes del paso a producción. [derivado]
- **Referencias:** EXC-18 (Anexo A): migrar la lista exigida de datos históricos. [derivado]

#### 1.7.6 Migración del padrón de clientes deduplicado, de los vendedores y de las liquidaciones

- **Rama y servicio:** 1.7. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 14 a 19 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** EXC-18: Migrar datos históricos fuera de la lista de RT-05.15. [derivado]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 14 a 19 (propuesta): clientes Retail es de la Etapa 2. [derivado]
- **Referencias:** EXC-18 (Anexo A): migrar la lista exigida de datos históricos. [derivado]

#### 1.7.7 Migración de la cartera viva (620.000 clientes) con sus actas de conciliación

- **Rama y servicio:** 1.7. **Etapa:** 1 y 2. **Método:** tres valores.
- **Ventana:** los meses 10 a 21 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 10 a 21, fijada por el contrato (Anexo D, resultado 24: primera parte en el mes 16 y segunda en el mes 21; acompaña a la migración). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 10 a 21 (contrato): Anexo D, resultado 24: primera parte en el mes 16 y segunda en el mes 21; acompaña a la migración. [derivado]
- **Referencias:** Resultado 24 del Anexo D; fuera del UCP (rama de migración). [derivado]

#### 1.7.9 Repositorio de consulta de datos históricos no migrados

- **Rama y servicio:** 1.7. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 10 a 16 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** EXC-18: Migrar datos históricos fuera de la lista de RT-05.15. [derivado]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 10 a 16 (propuesta): antes del paso a producción de la Etapa 1. [derivado]
- **Referencias:** Ronda 0: 1.30; EXC-18 (Anexo A): dejar un repositorio de consulta de los datos no migrados. [derivado]

#### 1.7.10 Plan de retiro de la plataforma de originación y cobranza de 2011

- **Rama y servicio:** 1.7. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 14 a 18 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plan; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 14 a 18 (propuesta): antes del retiro. [derivado]
- **Referencias:** Ronda 0: 3.11; sd-03, 3.1 y 3.2.3 (retiro de la plataforma de crédito de 2011 en octubre de 2028). [derivado]

#### 1.7.11 Plataforma de originación y cobranza de 2011 fuera de servicio

- **Rama y servicio:** 1.7. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** el mes 22 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plataforma operando; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de el mes 22, fijada por el contrato (sd-03 (operación): fecha objetivo octubre de 2028 = mes 22). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de el mes 22 (contrato): sd-03 (operación): fecha objetivo octubre de 2028 = mes 22. [derivado]
- **Referencias:** Ronda 0: 1.17b; sd-03, 3.1 y 3.2.3 (retiro de la plataforma de crédito de 2011 en octubre de 2028). [derivado]

#### 1.7.12 Sistema central de retail de 2009 retirado

- **Rama y servicio:** 1.7. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 21 a 56 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** SP-01: El sistema central de 2009 no sostiene los objetivos y se reemplaza por etapas. [derivado]
- **Entregable:** Por definir. Tipo probable: sistema operando; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 21 a 56, fijada por el contrato (sd-03 (operación): se retira durante la operación; fecha por definir). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 21 a 56 (contrato): sd-03 (operación): se retira durante la operación; fecha por definir. [derivado]
- **Referencias:** SP-01 y elección del escenario B en el sd-03. [derivado]

#### 1.7.13 Sustitución del punto de venta de 2014 tienda por tienda y su retiro

- **Rama y servicio:** 1.7. **Etapa:** 1. **Método:** tres valores.
- **Ventana:** los meses 8 a 16 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Implantación y Gestión del Cambio. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 8 a 16 (propuesta): sd-03, 3.3.1: tienda por tienda tras acreditar la operación sin conexión (piloto de los meses 6 y 7) y antes del paso a producción. [derivado]
- **Referencias:** sd-03, 3.3.1; tras acreditar la operación sin conexión y el retorno. [derivado]

#### 1.7.14 Actas de compuerta por tramo de la cartera de crédito

- **Rama y servicio:** 1.7. **Etapa:** 1 y 2. **Método:** tres valores.
- **Ventana:** los meses 12 a 21 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: acta; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Datos. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 12 a 21 (propuesta): sd-03, 3.2.3: la compuerta de cada tramo se cierra antes del paso a producción de la etapa (meses 16 y 21). [derivado]
- **Referencias:** sd-03, 3.2.3; las cierran la Contraparte Técnica y la filial emisora. [derivado]

### Rama 1.8

#### 1.8.1 Plan de seguridad, matriz de controles y modelo de amenazas

- **Rama y servicio:** 1.8. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 1 a 5 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plan; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Encargado de Seguridad de la Información. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 5 (propuesta): base de la seguridad; tras la arquitectura. [derivado]
- **Referencias:** por definir [por definir]

#### 1.8.3 Declaración de superficie de exposición y plan de respuesta a incidentes

- **Rama y servicio:** 1.8. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 4 a 8 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Encargado de Seguridad de la Información. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 4 a 8 (propuesta): tras el diseño; antes de la marcha blanca. [derivado]
- **Referencias:** por definir [por definir]

#### 1.8.5 Modelo de identidad, matriz de roles y segregación de funciones, incluido el ámbito emisor

- **Rama y servicio:** 1.8. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 2 a 5 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Encargado de Seguridad de la Información. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 2 a 5 (propuesta): tras la arquitectura. [derivado]
- **Referencias:** frontera con el UCP: aquí el diseño; la administración al actor está en la base tecnológica; RNF-37 (Anexo B): segregación de funciones entre originación, aprobación, modificación y cobranza. [derivado]

#### 1.8.6 Cifrado y tokenización de los medios de pago

- **Rama y servicio:** 1.8. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 4 a 10 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Encargado de Seguridad de la Información. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 4 a 10 (propuesta): RNF-33, RNF-34. [derivado]
- **Referencias:** RNF-33, RNF-34. [derivado]

#### 1.8.7 Protección de datos personales y matriz de cumplimiento normativo

- **Rama y servicio:** 1.8. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 3 a 8 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Encargado de Seguridad de la Información. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 3 a 8 (propuesta): Ley 21.719; tras el diseño. [derivado]
- **Referencias:** Ley 21.719; RNF-74 a RNF-76; Art. 27. [derivado]

#### 1.8.9 Informe de pruebas de intrusión y plan de remediación

- **Rama y servicio:** 1.8. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 10 a 18 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Encargado de Seguridad de la Información. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 10 a 18 (propuesta): antes de la certificación de cada etapa. [derivado]
- **Referencias:** Anexo D, resultado 21, y RNF-14: informe técnico y prueba de penetración. [derivado]

#### 1.8.10 Informe de diligencia del proveedor de nube

- **Rama y servicio:** 1.8. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 2 a 4 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Encargado de Seguridad de la Información. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 2 a 4 (propuesta): antes de elegir el proveedor de nube. [derivado]
- **Referencias:** Ronda 0: 3.13; fuente de la norma CMF por verificar. [derivado]

#### 1.8.11 Atestación de la cadena de suministro y revisión de la arquitectura de confianza cero

- **Rama y servicio:** 1.8. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 4 a 12 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Encargado de Seguridad de la Información. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 4 a 12 (propuesta): RNF-70, RNF-71; RNF-73. [derivado]
- **Referencias:** RNF-70, RNF-71; agregado desde el catálogo; RNF-73; agregado desde el catálogo. [derivado]

### Rama 1.9

#### 1.9.1 Plan de pruebas con niveles, tipos, ambientes, datos y calendario

- **Rama y servicio:** 1.9. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 2 a 4 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plan; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 2 a 4 (propuesta): antes de probar. [derivado]
- **Referencias:** Formulario T-13. [derivado]

#### 1.9.2 Estándares de codificación, revisión por pares y puertas de calidad

- **Rama y servicio:** 1.9. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 1 a 6 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 6 (propuesta): antes del desarrollo en curso; antes de programar. [derivado]
- **Referencias:** ISO 25010; Ronda 0: 3.2a. [derivado]

#### 1.9.3 Batería de pruebas funcionales y de requisitos no funcionales

- **Rama y servicio:** 1.9. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 5 a 18 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe de pruebas; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 5 a 18 (propuesta): durante el desarrollo de las dos etapas. [derivado]
- **Referencias:** ISO 29119; Anexo B (requisitos no funcionales con umbral y método de verificación). [derivado]

#### 1.9.4 Pruebas de desempeño, resiliencia y recuperación ante desastres

- **Rama y servicio:** 1.9. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 9 a 18 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe de pruebas; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 9 a 18 (propuesta): antes de la certificación de cada etapa; idem. [derivado]
- **Referencias:** RNF-22, RNF-23; ensayos a 1,5 veces el peak (RT-09.06); RNF-32. [derivado]

#### 1.9.6 Ensayo de la estrategia de degradación del evento anual

- **Rama y servicio:** 1.9. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 14 a 21 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe de pruebas; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 14 a 21, fijada por el contrato (Anexo D, resultado 25: ensayo del orden de degradación en el mes 16 y prueba de carga completa en el mes 21). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 14 a 21 (contrato): Anexo D, resultado 25: ensayo del orden de degradación en el mes 16 y prueba de carga completa en el mes 21. [derivado]
- **Referencias:** Resultado 25 del Anexo D; lo cita el servicio y se nombra aquí (guía §6). [derivado]

#### 1.9.7 Informes de aceptación por el usuario y de verificación de los 28 criterios de aceptación del caso

- **Rama y servicio:** 1.9. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 11 a 21 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 11 a 21 (propuesta): aceptación por etapa. [derivado]
- **Referencias:** Anexo D (28 resultados de negocio). [derivado]

#### 1.9.8 Certificación de calidad de la Etapa 1

- **Rama y servicio:** 1.9. **Etapa:** 1. **Método:** tres valores.
- **Ventana:** el mes 12 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: acta; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de el mes 12, fijada por el contrato (Art. 17: la certificación va dentro del desarrollo de la Etapa 1 (meses 1 a 12)). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de el mes 12 (contrato): Art. 17: la certificación va dentro del desarrollo de la Etapa 1 (meses 1 a 12). [derivado]
- **Referencias:** sd-03, 3.2.5 (el equipo del proponente controla la calidad antes de presentar cada entregable). [derivado]

#### 1.9.9 Certificación de calidad de la Etapa 2

- **Rama y servicio:** 1.9. **Etapa:** 2. **Método:** tres valores.
- **Ventana:** el mes 18 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: acta; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de el mes 18, fijada por el contrato (Art. 17: cierre del desarrollo de la Etapa 2 en el mes 18). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de el mes 18 (contrato): Art. 17: cierre del desarrollo de la Etapa 2 en el mes 18. [derivado]
- **Referencias:** sd-03, 3.2.5 (el equipo del proponente controla la calidad antes de presentar cada entregable). [derivado]

#### 1.9.11 Informe de la prueba del corte de enlace provocado de 24 horas con retorno ensayado en el piloto

- **Rama y servicio:** 1.9. **Etapa:** 1. **Método:** tres valores.
- **Ventana:** los meses 6 a 7 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 6 a 7, fijada por el contrato (sd-03, 3.2.3: corte de enlace de 24 horas en una tienda del piloto, en los meses 6 y 7). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 6 a 7 (contrato): sd-03, 3.2.3: corte de enlace de 24 horas en una tienda del piloto, en los meses 6 y 7. [derivado]
- **Referencias:** sd-03, 3.2.3 y 3.4.5; RT-03.10. [derivado]

#### 1.9.12 Informe de evaluación de comercio electrónico y fidelización con las pruebas de la Etapa 1

- **Rama y servicio:** 1.9. **Etapa:** 1. **Método:** tres valores.
- **Ventana:** los meses 9 a 12 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 9 a 12 (propuesta): sd-03, 3.3.1: con las pruebas de la primera etapa y antes de la ola que dependa de la plataforma. [derivado]
- **Referencias:** sd-03, 3.3.1; decide si se conservan, remedian o sustituyen antes de la Etapa 2. [derivado]

#### 1.9.13 Informe de pruebas de tareas del punto de venta con cajeros nuevos y experimentados

- **Rama y servicio:** 1.9. **Etapa:** 1. **Método:** tres valores.
- **Ventana:** los meses 5 a 7 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 5 a 7 (propuesta): sd-03, 3.4.6: antes del despliegue y del piloto. [derivado]
- **Referencias:** sd-03, 3.4.6; antes del despliegue; RNF-49. [derivado]

#### 1.9.14 Informe de pruebas de comprensión de precios, entrega e información crediticia con clientes y titulares

- **Rama y servicio:** 1.9. **Etapa:** 1 y 2. **Método:** tres valores.
- **Ventana:** los meses 12 a 20 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 12 a 20 (propuesta): sd-03, 3.4.6: precios, entrega e información crediticia de las dos etapas. [derivado]
- **Referencias:** sd-03, 3.4.6. [derivado]

### Rama 1.10

#### 1.10.1 Un paquete por innovación, con tipo, indicador, línea base y meta por definir

- **Rama y servicio:** 1.10. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** por definir
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** por definir [por definir]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana por definir. [derivado]
- **Referencias:** RT-26.02; art. 29; candidatas del equipo de innovación por validar (sd-13). [derivado]

#### 1.10.2 Un paquete por innovación, con tipo, indicador, línea base y meta por definir

- **Rama y servicio:** 1.10. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** por definir
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** por definir [por definir]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana por definir. [derivado]
- **Referencias:** RT-26.02; art. 29; candidatas del equipo de innovación por validar (sd-13). [derivado]

#### 1.10.3 Un paquete por innovación, con tipo, indicador, línea base y meta por definir

- **Rama y servicio:** 1.10. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** por definir
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** por definir [por definir]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana por definir. [derivado]
- **Referencias:** RT-26.02; art. 29; candidatas del equipo de innovación por validar (sd-13). [derivado]

#### 1.10.4 Un paquete por innovación, con tipo, indicador, línea base y meta por definir

- **Rama y servicio:** 1.10. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** por definir
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** por definir [por definir]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana por definir. [derivado]
- **Referencias:** RT-26.02; art. 29; candidatas del equipo de innovación por validar (sd-13). [derivado]

#### 1.10.5 Un paquete por innovación, con tipo, indicador, línea base y meta por definir

- **Rama y servicio:** 1.10. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** por definir
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** por definir [por definir]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana por definir. [derivado]
- **Referencias:** RT-26.02; art. 29; candidatas del equipo de innovación por validar (sd-13). [derivado]

### Rama 1.11

#### 1.11.1 Plan de implantación con procedimiento de despliegue gradual y de reversión probado

- **Rama y servicio:** 1.11. **Etapa:** 1 y 2. **Método:** tres valores.
- **Ventana:** los meses 3 a 12 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plan; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Implantación y Gestión del Cambio. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 3 a 12 (propuesta): T-18; se actualiza; antes de la marcha blanca. [derivado]
- **Referencias:** Formulario T-18. [derivado]

#### 1.11.3 Configuración y certificación de los sitios: 22 tiendas, 2 centros de distribución, 380 líneas de caja, 640 terminales y el nodo de borde de cada tienda

- **Rama y servicio:** 1.11. **Etapa:** 1 y 2. **Método:** tres valores.
- **Ventana:** los meses 9 a 18 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** EXC-19: Proveer o instalar equipamiento físico de tiendas y centros de distribución, ejecutar sus obras ni contratar sus enlaces; SP-04: El cliente adquiere, ejecuta y contrata, antes de cada instalación en tienda y centro de distribución, lo físico que el proponente especifica. El proponente provee el centro de datos on-premise con su conectividad, su seguridad y sus canalizaciones. [derivado]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Implantación y Gestión del Cambio. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 9 a 18 (propuesta): sitios de la Etapa 1 antes del mes 13 y de la Etapa 2 antes del mes 19. [derivado]
- **Referencias:** El cliente adquiere y ejecuta (EXC-19, SP-04). [derivado]

#### 1.11.4 Plan de convivencia entre la Etapa 1 y la Etapa 2 con una única fuente de verdad

- **Rama y servicio:** 1.11. **Etapa:** 2. **Método:** tres valores.
- **Ventana:** los meses 15 a 18 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plan; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Implantación y Gestión del Cambio. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 15 a 18 (propuesta): Art. 17.2 fija la convivencia en los meses 19 y 20; el plan va antes. [derivado]
- **Referencias:** sd-03, 3.4.5 (continuidad entre etapas por convivencia, conciliación y retorno ensayado). [derivado]

#### 1.11.5 Piloto del punto de venta en tres tiendas

- **Rama y servicio:** 1.11. **Etapa:** 1. **Método:** tres valores.
- **Ventana:** los meses 6 a 7 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Implantación y Gestión del Cambio. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 6 a 7, fijada por el contrato (sd-03, 3.2.3: el piloto del punto de venta es de los meses 6 y 7). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 6 a 7 (contrato): sd-03, 3.2.3: el piloto del punto de venta es de los meses 6 y 7. [derivado]
- **Referencias:** sd-03, 3.2.3. [derivado]

### Rama 1.12

#### 1.12.1 Plan de la marcha blanca de la Etapa 1

- **Rama y servicio:** 1.12. **Etapa:** 1. **Método:** tres valores.
- **Ventana:** los meses 10 a 12 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plan; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Implantación y Gestión del Cambio, con apoyo del Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 10 a 12 (propuesta): antes de la marcha blanca. [derivado]
- **Referencias:** sd-03, 3.1 y 3.2.2 (marchas blancas de los meses 13 a 15 y 19 a 20). [derivado]

#### 1.12.2 Informe de resultados y evidencia de cierre de la marcha blanca de la Etapa 1

- **Rama y servicio:** 1.12. **Etapa:** 1. **Método:** tres valores.
- **Ventana:** los meses 15 a 16 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Implantación y Gestión del Cambio, con apoyo del Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 15 a 16, fijada por el contrato (Art. 17: la marcha blanca de la Etapa 1 termina en el mes 15; Art. 17.3: condiciones de cierre). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 15 a 16 (contrato): Art. 17: la marcha blanca de la Etapa 1 termina en el mes 15; Art. 17.3: condiciones de cierre. [derivado]
- **Referencias:** Caso, numeral 17.3. [derivado]

#### 1.12.4 Acta de aceptación de la Etapa 1

- **Rama y servicio:** 1.12. **Etapa:** 1. **Método:** tres valores.
- **Ventana:** el mes 16 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: acta; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de el mes 16, fijada por el contrato (Art. 17: paso a producción en el mes 16). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de el mes 16 (contrato): Art. 17: paso a producción en el mes 16. [derivado]
- **Referencias:** sd-03, 3.2.2 (paso a producción de la Etapa 1 en el mes 16). [derivado]

#### 1.12.5 Plan de la marcha blanca de la Etapa 2, en convivencia con la Etapa 1 en producción

- **Rama y servicio:** 1.12. **Etapa:** 2. **Método:** tres valores.
- **Ventana:** los meses 16 a 18 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plan; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Implantación y Gestión del Cambio, con apoyo del Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 16 a 18 (propuesta): antes de la marcha blanca de la Etapa 2. [derivado]
- **Referencias:** sd-03, 3.1 y 3.2.2 (marchas blancas de los meses 13 a 15 y 19 a 20). [derivado]

#### 1.12.6 Informe de resultados de la marcha blanca de la Etapa 2

- **Rama y servicio:** 1.12. **Etapa:** 2. **Método:** tres valores.
- **Ventana:** el mes 20 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Implantación y Gestión del Cambio, con apoyo del Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de el mes 20, fijada por el contrato (Art. 17: la marcha blanca de la Etapa 2 termina en el mes 20). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de el mes 20 (contrato): Art. 17: la marcha blanca de la Etapa 2 termina en el mes 20. [derivado]
- **Referencias:** sd-03, 3.1 y 3.2.2 (marchas blancas de los meses 13 a 15 y 19 a 20). [derivado]

#### 1.12.7 Acta de aceptación final y garantía de correcto funcionamiento

- **Rama y servicio:** 1.12. **Etapa:** 2. **Método:** tres valores.
- **Ventana:** el mes 21 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: acta; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de el mes 21, fijada por el contrato (Art. 17: aceptación final en el mes 21; se activa con la aceptación final). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de el mes 21 (contrato): Art. 17: aceptación final en el mes 21; se activa con la aceptación final. [derivado]
- **Referencias:** sd-03, 3.2.2 (paso a producción de la Etapa 2 en el mes 21). [derivado]

#### 1.12.9 Informe del soporte de estabilización posterior a la puesta en marcha

- **Rama y servicio:** 1.12. **Etapa:** 1 y 2. **Método:** tres valores.
- **Ventana:** los meses 16 a 24 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Implantación y Gestión del Cambio, con apoyo del Líder de Calidad. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 16 a 24 (propuesta): tras cada paso a producción. [derivado]
- **Referencias:** por definir [por definir]

### Rama 1.13

#### 1.13.1 Plan de gestión del cambio con diagnóstico por perfil y medición de adopción

- **Rama y servicio:** 1.13. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 3 a 6 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plan; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Implantación y Gestión del Cambio. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 3 a 6 (propuesta): antes de capacitar. [derivado]
- **Referencias:** Art. 89. [derivado]

#### 1.13.2 Plan de capacitación por rol y materiales editables en español

- **Rama y servicio:** 1.13. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 5 a 8 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plan; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Implantación y Gestión del Cambio. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 5 a 8 (propuesta): antes de capacitar. [derivado]
- **Referencias:** Art. 90. [derivado]

#### 1.13.3 Registro de capacitación ejecutada y certificación de administradores y equipo técnico, condición de cierre de cada marcha blanca

- **Rama y servicio:** 1.13. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 10 a 20 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: registro; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Implantación y Gestión del Cambio. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 10 a 20 (propuesta): Art. 17.3: la capacitación certificada es condición de cierre de cada marcha blanca (meses 15 y 20). [derivado]
- **Referencias:** sd-03, 3.4.6 (capacitación por rol) y Art. 17.3 (condición de cierre de la marcha blanca). [derivado]

#### 1.13.4 Informe de acompañamiento en puesto para el personal de tienda, temporero y externo

- **Rama y servicio:** 1.13. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 13 a 24 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Implantación y Gestión del Cambio. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 13 a 24 (propuesta): tras el paso a producción de cada etapa. [derivado]
- **Referencias:** 62 % de rotación anual, 1.900 temporeros y unos 1.100 externos; sd-03, 3.4.6 (rotación anual de 62 % y unos 1.100 repositores externos). [derivado]

#### 1.13.5 Plan de comunicación a los clientes de la cartera por tramo

- **Rama y servicio:** 1.13. **Etapa:** 1 y 2. **Método:** tres valores.
- **Ventana:** los meses 10 a 21 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plan; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Implantación y Gestión del Cambio. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 10 a 21 (propuesta): sd-03, 3.2.3: antes del primer tramo y de cada compuerta. [derivado]
- **Referencias:** sd-03, 3.2.3; condición de cada compuerta de tramo. [derivado]

### Rama 1.14

#### 1.14.1 Documentación técnica y funcional con inventario de componentes de software

- **Rama y servicio:** 1.14. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 1 a 56 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 56 (propuesta): continua, versión final al cierre; desde el primer artefacto desplegado. [derivado]
- **Referencias:** Art. 91; arquitectura, requerimientos, construcción, pruebas, operación, seguridad, usuario y proyecto; RNF-70. [derivado]

#### 1.14.3 Transferencia tecnológica de código fuente, artefactos de construcción, scripts de infraestructura y procedimientos de despliegue

- **Rama y servicio:** 1.14. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 48 a 56 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto, con apoyo del Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 48 a 56 (propuesta): Art. 77.1: programa de transferencia hacia el cierre. [derivado]
- **Referencias:** Art. 77.1. [derivado]

#### 1.14.4 Base de conocimiento y manuales de operación

- **Rama y servicio:** 1.14. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 10 a 56 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 10 a 56 (propuesta): desde la marcha blanca; antes de operar. [derivado]
- **Referencias:** Art. 77.1; agregado desde la guía. [derivado]

#### 1.14.6 Plan de Reversibilidad con exportación en formatos abiertos

- **Rama y servicio:** 1.14. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 1 a 3 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: plan; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 1 a 3, fijada por el contrato (Art. 77.2: dentro de los primeros noventa días; se actualiza cada año). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 3 (contrato): Art. 77.2: dentro de los primeros noventa días; se actualiza cada año. [derivado]
- **Referencias:** Art. 77.2; se entrega dentro de los primeros noventa días y se actualiza cada año. [derivado]

#### 1.14.7 Acta de cierre, traspaso final y acompañamiento de reversibilidad

- **Rama y servicio:** 1.14. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** el mes 56 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: acta; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de el mes 56, fijada por el contrato (Art. 77.2: noventa días después del cierre, fuera de los 56 meses; cierre del contrato). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de el mes 56 (contrato): Art. 77.2: noventa días después del cierre, fuera de los 56 meses; cierre del contrato. [derivado]
- **Referencias:** Art. 77.2; Art. 87. [derivado]

#### 1.14.9 Informe de lecciones aprendidas del proyecto

- **Rama y servicio:** 1.14. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** el mes 56 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de el mes 56 (propuesta): cierre del contrato. [derivado]
- **Referencias:** por definir [por definir]

#### 1.14.10 Protocolo de aceptación de entregas y del producto final

- **Rama y servicio:** 1.14. **Etapa:** por definir. **Método:** tres valores.
- **Ventana:** los meses 1 a 3 (propuesta)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: documento; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Jefe de Proyecto. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Hitos del Formulario E-25: por definir. [por definir]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 1 a 3 (propuesta): antes de la primera aceptación. [derivado]
- **Referencias:** Formulario T-17; base de las actas de aceptación. [derivado]

### Rama 1.15

#### 1.15.1 Mesa de servicio de tres niveles en operación

- **Rama y servicio:** 1.15. **Etapa:** operación. **Método:** tres valores.
- **Ventana:** los meses 21 a 56 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: servicio operando; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 21 a 56, fijada por el contrato (Art. 17: operación de los meses 21 a 56). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 21 a 56 (contrato): Art. 17: operación de los meses 21 a 56. [derivado]
- **Referencias:** Art. 78. [derivado]

#### 1.15.2 Informes periódicos de nivel de servicio y de certificaciones

- **Rama y servicio:** 1.15. **Etapa:** operación. **Método:** tres valores.
- **Ventana:** los meses 21 a 56 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 21 a 56, fijada por el contrato (Art. 17: operación de los meses 21 a 56). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 21 a 56 (contrato): Art. 17: operación de los meses 21 a 56. [derivado]
- **Referencias:** Art. 79.2; Arts. 27, 74.6. [derivado]

#### 1.15.3 Pruebas periódicas de recuperación ante desastres

- **Rama y servicio:** 1.15. **Etapa:** operación. **Método:** tres valores.
- **Ventana:** los meses 21 a 56 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** Por definir. Tipo probable: informe de pruebas; falta concretar el artefacto. [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 21 a 56, fijada por el contrato (sd-03: la recuperación ante desastres se prueba dos veces al año). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 21 a 56 (contrato): sd-03: la recuperación ante desastres se prueba dos veces al año. [derivado]
- **Referencias:** el sd-03 las fija dos veces al año. [derivado]

#### 1.15.4 Mantención correctiva, preventiva y evolutiva

- **Rama y servicio:** 1.15. **Etapa:** operación. **Método:** tres valores.
- **Ventana:** los meses 21 a 56 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 21 a 56, fijada por el contrato (Art. 17: operación de los meses 21 a 56). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 21 a 56 (contrato): Art. 17: operación de los meses 21 a 56. [derivado]
- **Referencias:** Agregado desde el sd-03 y las Bases; base del sd-11. [derivado]

#### 1.15.6 Infraestructura en operación con su informe de gestión

- **Rama y servicio:** 1.15. **Etapa:** operación. **Método:** tres valores.
- **Ventana:** los meses 21 a 56 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 21 a 56, fijada por el contrato (Art. 17: operación de los meses 21 a 56). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 21 a 56 (contrato): Art. 17: operación de los meses 21 a 56. [derivado]
- **Referencias:** Agregado desde el sd-03. [derivado]

#### 1.15.8 Jornadas anuales de actualización y capacitación de personal nuevo

- **Rama y servicio:** 1.15. **Etapa:** operación. **Método:** tres valores.
- **Ventana:** los meses 21 a 56 (contrato)
- **Descripción del trabajo:** por definir [por definir]
- **Queda fuera:** por definir [por definir]
- **Entregable:** por definir [por definir]
- **Criterio de aceptación:** por definir [por definir]
- **Responsable:** Líder de Operación. Acepta la Contraparte Técnica (Art. 18.1). [propuesta]
- **Hitos asociados:** Ventana de los meses 21 a 56, fijada por el contrato (Art. 17: operación de los meses 21 a 56). [derivado]
- **Esfuerzo estimado:** Por estimar (planilla de tres valores, Formulario T-15). [por definir]
- **Costo estimado:** Por estimar; los montos viven solo en el Sobre Económico. [por definir]
- **Recursos requeridos:** Por definir con el sd-12. [por definir]
- **Supuestos:** Ventana de los meses 21 a 56 (contrato): Art. 17: operación de los meses 21 a 56. [derivado]
- **Referencias:** Art. 90.5. [derivado]
