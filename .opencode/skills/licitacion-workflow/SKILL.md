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
| **Requerimientos / volumetría** | Leer y procesar `01_Requerimientos/*.xlsx` (preferir `RequerimientosAtomizados_Depuracion_Alcance.xlsx`, catálogo v3.0 depurado; `RequerimientosAtomizados.xlsx` v2.1 queda como histórico); responder requisitos RT uno a uno (Formulario T-12) | `xlsx` |
| **Estimación de esfuerzo y roles** | Desglosar tareas por rol (BE/FE/QA/DevOps/PM), aplicar factores de riesgo y holguras (nivelación T-15) | `project-estimation`, `xlsx` |
| **Riesgos** (contractuales y técnicos) | Evaluar y clasificar riesgos de la propuesta y el contrato | `legal-risk-assessment`, `risk-assessment` |
| **Oferta económica y flujo de caja** | Valorizar en CLP / UF / USD, desglosar neto+IVA+total, flujo de caja por hito (E-25), 5 innovaciones | `project-estimation`, `xlsx` |
| **Formularios y plantillas oficiales** | Llenar los formularios/plantillas `.docx` de los anexos A/B/C | `docx` |
| **Presentaciones preparatorias** | Preparar las 3 presentaciones (Sobres) | `pptx` |
| **Investigación** (lo que el caso no explica) | Investigar normativa sectorial, estándares, indicadores del mercado retail | `deep-research` |
| **Redacción de documentos técnicos extensos** | Estructurar y redactar los apartados de la oferta | `technical-writing` |
| **Entrega final / exportación** | Convertir/formatear subdocumentos a LaTeX corporativo y compilar PDF, solo con `05_Gestion/scripts/exportar_latex.py` | `exportar` (`.agents/skills/exportar/`) |

## Recordatorios críticos del proyecto (para no repetir errores)

- **Precedencia** (Art. 5° Bases Admin): `00_Bases/Bases_Administrativas.md` > `00_Bases/Bases_Transversales.md` > `00_Bases/Caso_09_Cadena_Multitienda.md`. El caso puede endurecer requisitos transversales, nunca rebajarlos.
- **Despliegue híbrido obligatorio** (Art. 16): nube pública + componentes on-premise. Rechazar propuestas solo-nube o solo-on-premise.
- **Cronograma de 56 meses innegociable** (Art. 17): Etapa 1 (1–15, prod mes 16), Etapa 2 (13–20, prod mes 21), Operación 21–56. Cifras/plazos deben ser consistentes.
- **5 innovaciones obligatorias** (Cap. 5), una por tipo, trazables con arquitectura, EDT y flujo de caja.
- **Línea roja del caso**: la compañía es tienda + emisor de crédito fiscalizado (dos regímenes). No tratar como un solo negocio ni mezclar sus datos.
- **TrabajosAnteriores_DistriProducto/** (en `90_Referencia/`) proviene de un caso distinto (logística WMS/TMS/YMS). Usar SOLO como referencia de formato; no relacionar su contenido.
- **Formato de los artefactos**: los subdocumentos T-7 ya importados tienen como fuente `02_Propuesta/latex_final/sd-NN.tex`; los `.md` de `02_Propuesta/` quedan solo como contexto. La exportación sigue la regla de `AGENTS.md` ("Regla de exportación").
- **Tablas incompletas**: la tabla de ponderación del T-21 en `00_Bases/` no se puede reconstruir. No hardcodear porcentajes; dejarlos en blanco con nota de pendiente.
- **Idioma**: todo en español.
