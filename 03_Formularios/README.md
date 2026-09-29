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

## Estado

Vacío. Los formularios se completan cuando el subdocumento que los alimenta tenga contenido.
