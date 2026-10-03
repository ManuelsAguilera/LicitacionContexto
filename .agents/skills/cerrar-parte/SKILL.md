---
name: cerrar-parte
description: Comprobar preparación de un subdocumento T-7 y generar su estado de cierre para revisión humana.
---

# Cerrar una parte

1. Ejecuta `estado.py --dry-run` y `check.py --parte T7-NN`.
2. Confirma que todas las secciones oficiales existen y están en `revisado`, que no quedan errores ni anexos pendientes y que títulos/orden siguen el Comunicado 10.
3. Si algo falta, entrega la lista de bloqueos y no marques la parte como cerrada.
4. Si todo cumple, prepara un resumen conciso de cierre. La persona responsable cambia estados manualmente; el agente no asigna `revisado` ni `congelado`.
