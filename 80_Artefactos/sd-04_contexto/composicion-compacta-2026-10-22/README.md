# Vista compacta y CSV con asociaciones

Estado: borrador, 22-10-2026. Sin revisión humana registrada.

La [recopilación de contexto y cambios del subdocumento lógico](../contexto-arquitectura-y-cambios-logicos_2026-10-22.md) reúne las decisiones vigentes, sus motivos, los pendientes y 25 cambios localizados para conciliar SD-04 con esta arquitectura.

La vista principal mantiene las seis capas horizontales y reúne 7 Seguridad y 8 Observabilidad en una banda vertical izquierda, resumida mediante iconos y nombres, sin carriles duplicados por negocio. Datos usa círculos con icono y etiqueta inferior; los repositorios operacionales se agrupan bajo Mercadería, Venta, Clientes y Crédito.

Se mantienen 79 componentes representados, trece servicios vigentes, cinco innovaciones, la VPN y F:C-04 como candidato sin contratos operacionales. Los símbolos agrupados no fusionan bases, autoridades, credenciales ni instancias entre ámbitos. SD-03, SD-04, los restantes `.tex` y los dos registros de entrada conservan sus hashes originales.

## Archivos de entrega

- [Draw.io editable, validado y renderizado por MCP](../../../04_Adjuntos/diagramas/diag-04-36_arquitectura-compacta.drawio).
- [PNG](../../../04_Adjuntos/diagramas/diag-04-36_arquitectura-compacta.png) y [SVG](../../../04_Adjuntos/diagramas/diag-04-36_arquitectura-compacta.svg) de esa misma composición.
- [JSON validado](../../../04_Adjuntos/diagramas/diag-04-36_arquitectura-compacta.json).
- [CSV preparado para draw.io](../../../04_Adjuntos/diagramas/diag-04-36_csv_conservar-capas.csv).
- [Asociaciones y contratos detallados](asociaciones-y-contratos.json) y [comprobaciones](verificacion.json).

Las conexiones visibles bajan de 88 a 53 (39,8 % menos). Se agrupan entradas públicas/privadas, APIs y hechos por áreas, persistencia, adaptadores y contrapartes. La línea gris sin punta representa una asociación de contratos o dependencia; no debe leerse como una secuencia de ejecución. El mapeo conserva las relaciones originales y su intención.

## Importar el CSV

En draw.io: **Organizar → Insertar → Avanzado → CSV**. Pegar el archivo completo, incluida su configuración inicial.

El CSV declara `layout: libavoid`, `orthogonalEdgeStyle`, puertos de contorno y marcos de asociación. La pertenencia de los componentes se conserva como metadato `agrupacion`; no se fusionan componentes. Los puntos de conexión son elementos gráficos, no servicios nuevos.

**Límite de verificación:** la última versión del CSV se comprobó estructuralmente: IDs únicos, 205 filas, 53 relaciones, 26 puertos gráficos y terminales lógicos coincidentes con el JSON. Su prueba visual final de importación no se ejecutó: la revisión automática no pudo completarse por un límite de uso. No se presenta el draw.io de entrega como resultado de esa última importación CSV. Los exports de intentos anteriores del importador, que no satisfacían la revisión gráfica, se retiraron de la carpeta de entrega.

El JSON y el draw.io producido por el MCP pasaron la validación y el linter; el harness terminó en «TODO EN ORDEN». Eso no acredita una plataforma Azure desplegada, capacidad ni aceptación de residencia. Los pendientes técnicos de los registros siguen vigentes.

Generadores: `05_Gestion/scripts/generar_arquitectura_compacta.py` y `05_Gestion/scripts/exportar_csv_arquitectura_compacta.py`. Plantilla controlada: `.agents/skills/diagramas-ancoa/scripts/render_compacto_20261022.py`.

Uso de IA: Alto. Registrarlo en la Tabla 4.17 al incorporar la figura a la propuesta.
