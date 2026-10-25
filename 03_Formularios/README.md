# Formularios oficiales de la propuesta

Formularios exigidos por las Bases Administrativas, agrupados según el sobre en que se entregan
(Capítulo A/B/C y Artículos 39.º a 51.º). Se completan a partir del contenido redactado en
`02_Propuesta/` y se firman para la entrega.

| Anexo | Formularios | Sobre | Contenido |
| :--- | :--- | :--- | :--- |
| `A/` | A-1 a A-6 | Sobre 1 - Antecedentes administrativos | Identificación del proponente, declaraciones juradas, índice de antecedentes y declaración de uso de IA generativa |
| `B/` | T-6 a T-22 | Sobre 2 - Oferta técnica | Formularios técnicos, incluida la matriz de cumplimiento T-12 |
| `C/` | E-21 a E-26 | Sobre 3 - Oferta económica | Estructura de la oferta económica, hitos de pago y rangos de valores por perfil |

## Reglas

- **Fuente oficial:** los textos de los formularios están en `00_Bases/Bases_Administrativas.md`
  (A partir de la línea 1868). No se reinterpreta el formulario: se completa.
- **Nunca versionar datos sensibles en claro:** el Formulario A-1 pide RUT, cédula, domicilio y
  datos bancarios de la contraparte. Revisar antes de commitear.
- **Firmas:** los formularios del Anexo A se presentan firmados por el representante legal y, cuando
  se indique, ante notario (Art. 39.º).
- **Sin precios en el Sobre 2:** el Anexo B no puede contener información de precios (Art. 50.º).
- **Orden:** el índice del Sobre 2 es el Formulario T-7; la correspondencia entre formulario y
  subdocumento está en `02_Propuesta/indice.md` y en la sección *Formularios asociados* de cada
  maestro `sd-NN_*.md`.

## Convención de nombres

`form-<ID>_titulo.<ext>`, por ejemplo `form-T-12_matriz-cumplimiento-tecnico.xlsx`.

## Dónde viven hoy los formularios del Sobre 2

Los formularios técnicos T-6 a T-22 se redactan como `.tex` con Prism y viven en
`02_Propuesta/latex_final/Formularios/` (`OnlySimpleSolutions-Formulario-T-N.tex`). El CLI actual de
`exportar_latex.py` no ofrece una ruta para compilar esta carpeta; la integración disponible tuvo comprobación estática, no certifica PDF de formularios. Las carpetas `A/`, `B/` y `C/`
de aquí quedan para los formularios que se completen en otros formatos (por ejemplo `.docx` o `.xlsx`).

## Estado

Los formularios del Sobre 2 están en `latex_final/Formularios/`. `A/`, `B/` y `C/` quedan para formatos distintos de `.tex`.

- `B/form-T-11_especificaciones-tecnicas-ofertadas.md`: antecedente de redacción, sin revisión humana. El ZIP se integró en `02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-11.tex`; también se conserva `sd-04/OSS-Formulario-T-11.tex`, una copia local divergente. Ninguna se elimina ni se declara versión definitiva de entrega hasta conciliar ambas contra SD-04.
- SD-04 y SD-07 son las referencias más actualizadas para conciliar arquitectura, suministro, EDT, esfuerzo e implantación; las Bases y el Comunicado 10 mantienen su precedencia. Ver la [matriz activa](../80_Artefactos/contexto-activo/matriz-ajustes.md).
