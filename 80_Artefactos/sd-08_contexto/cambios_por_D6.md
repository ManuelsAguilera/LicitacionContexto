# Cambios que exige D6 (recinto on-premise, decidida 2026-10-11)

Documento de contexto, no entregable. Líneas leídas el 2026-10-11; si el archivo difiere, manda el archivo. Nada de esto se aplicó: cada archivo es de otro subdocumento.

**Decisión.** DC-01 (recinto propio de 140 m² habilitado en 2011 en la casa matriz) y DC-02 (sala de respaldo en la misma comuna) son del cliente (Caso l. 330; RT-06.01 del Caso l. 798; RT-06.31). El cliente ejecuta la obra civil y compra el hardware (RT-06.06; Caso l. 647 y 649). El proponente especifica y coordina, y provee conectividad, seguridad y canalizaciones (RT-06.33) y el espacio de trabajo del personal (RT-06.29).

## A. Cambios en otros subdocumentos

| N.º | Dónde | Cambio |
| :-- | :-- | :-- |
| C-1 | sd-03 (alcance y responsabilidades) y la EDT (`14_edt_corregida.md`) | Donde digan que el proponente «provee» el centro de datos, cambiar por «especifica y coordina; lo ejecuta y compra el cliente». Buscar con `grep -n "centro de datos\|DC-01\|DC-02\|on-premise"` en `sd-03/` y en `80_Artefactos/sd-07_contexto/estimacion/` |
| C-2 | Auditoría sd01-04, hallazgo EXT-M-03 (l. 51) | Corregir la lectura: no resuelve a favor del proponente; queda como lo descrito arriba |
| C-3 | sd-04, Tabla 4.11 (`OSS-Subdocumento4.tex`, l. ~575) | Se mantiene que el cliente conserva DC-01 y DC-02. Agregar quién ejecuta la obra (cliente), quién compra (cliente) y quién especifica y coordina (proponente). Citar RT-06.06 |
| C-4 | sd-04, DC-02 | DC-02 está en la misma comuna que DC-01. Declarar que es sala de respaldo local y no sitio de recuperación ante desastres; el respaldo de las cargas nuevas es CLD-02 (Azure Brazil South). Decisión de arquitectura del sd-04 |
| C-5 | Planilla de consultas al mandante | Consulta posible: alcance de RT-06.33 («proveerá conectividad, seguridad y canalizaciones») frente al Caso l. 647 (las ejecuta el cliente). Confirmar que «proveer» significa diseñar, especificar y garantizar |
| C-6 | EDT, obras | Comprobar que existe una cuenta de especificación y coordinación de la obra civil (RT-06.06). Si no existe, sumarla a la guía `guia_cuentas_nuevas_sd-07.md`. En el T-14 vigente existen 1.3.7 (Especificación y costeo de obras del cliente) y 1.4.9 (Recinto técnico y obra civil de separación), por lo que no hace falta cuenta nueva |

## B. Cambios en el sd-08

- `trazabilidad_riesgos.md` I-02: cerrar con esta decisión.
- R-31: reformular como riesgo de contraparte (obra, hardware e informe de 2024 del cliente) con mitigación del proponente: especificación completa, coordinación y condición explícita de que las pruebas dependen de que el recinto esté listo. Escalar al Comité Ejecutivo si la obra se atrasa.
- R-20 (el cliente compra el hardware y hace las obras) y R-31 comparten causa: referenciar entre sí.
- Folios: comprobar el folio impreso del Caso (ficha del centro de datos, cap. 6) antes de citar.
