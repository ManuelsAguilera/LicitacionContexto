---
name: licitacion-workflow
description: Orchestrates the tender proposal workflow (Licitación N° TFEP-01/2026, Caso 09 Cadena Multitienda). Load at the start of any work on this project and whenever a new phase of the proposal begins (architecture, requirements, planning, risks, economic offer, official forms, presentations). It directs WHICH other skills to activate for each phase.
---

# Workflow de la propuesta técnico-económica

Este proyecto produce la propuesta técnico-económica de una licitación pública ficticia (TFEP-01/2026, Caso 09 Cadena Multitienda). El entregable es documentación tipo oferta en español, no código.

**Regla de uso:** en cuanto identifiques que la tarea pertenece a una de las fases de abajo, **carga la skill indicada** con la herramienta `skill` ANTES de ejecutar el trabajo de esa fase. No esperes a que el usuario lo pida: hazlo de forma proactiva según la fase.

## Fases y qué skill cargar en cada una

| Fase de la propuesta | Qué implicar | Activar skill(s) |
| :--- | :--- | :--- |
| **Arquitectura** (lógica, física, datos, seguridad, despliegue — ISO 42010 y vistas) | Diseñar y describir la solución híbrida nube+on-premise por capas; justificar emplazamiento; diagramar | `architecture-diagrams`, `cloud-architecture`, `sre-practices` |
| **Requerimientos / volumetría** | Leer y procesar `Requerimientos/*.xlsx` (preferir `RequerimientosAtomizados.xlsx`); responder requisitos RT uno a uno (Formulario T-12) | `xlsx` |
| **Estimación de esfuerzo y roles** | Desglosar tareas por rol (BE/FE/QA/DevOps/PM), aplicar factores de riesgo y holguras (nivelación T-15) | `project-estimation`, `xlsx` |
| **Riesgos** (contractuales y técnicos) | Evaluar y clasificar riesgos de la propuesta y el contrato | `legal-risk-assessment`, `risk-assessment` |
| **Oferta económica y flujo de caja** | Valorizar en CLP / UF / USD, desglosar neto+IVA+total, flujo de caja por hito (E-25), 5 innovaciones | `project-estimation`, `xlsx` |
| **Formularios y plantillas oficiales** | Llenar los formularios/plantillas `.docx` de los anexos A/B/C | `docx` |
| **Presentaciones preparatorias** | Preparar las 3 presentaciones (Sobres) | `pptx` |
| **Investigación** (lo que el caso no explica) | Investigar normativa sectorial, estándares, indicadores del mercado retail | `deep-research` |
| **Redacción de documentos técnicos extensos** | Estructurar y redactar los apartados de la oferta | `technical-writing` |
| **Entrega final / exportación** | Generar o conformar la propuesta final en PDF | `pdf-handling` |

## Recordatorios críticos del proyecto (para no repetir errores)

- **Precedencia** (Art. 5° Bases Admin): `Bases_Administrativas.md` > `Bases_Transversales.md` > `Caso_09_Cadena_Multitienda.md`. El caso puede endurecer requisitos transversales, nunca rebajarlos.
- **Despliegue híbrido obligatorio** (Art. 16): nube pública + componentes on-premise. Rechazar propuestas solo-nube o solo-on-premise.
- **Cronograma de 56 meses innegociable** (Art. 17): Etapa 1 (1–15, prod mes 16), Etapa 2 (13–20, prod mes 21), Operación 21–56. Cifras/plazos deben ser consistentes.
- **5 innovaciones obligatorias** (Cap. 5), una por tipo, trazables con arquitectura, EDT y flujo de caja.
- **Línea roja del caso**: la compañía es tienda + emisor de crédito fiscalizado (dos regímenes). No tratar como un solo negocio ni mezclar sus datos.
- **TrabajosAnteriores/** proviene de un caso distinto (logística WMS/TMS/YMS). Usar SOLO como referencia de formato; no relacionar su contenido.
- **Idioma**: todo en español.
