---
estado: borrador
parte: T7-09
---
# Registro de brechas y decisiones

Cada brecha conserva el dueño por rol como propuesta organizativa; aún no hay personas designadas ni decisiones humanas. Resolver implica registrar acuerdo, fuente, versión, criterio afectado y evidencia exigida antes de cerrar compuerta. La prioridad siguiente responde a impacto y dependencia, sin estimar probabilidades.

| Brecha interna | Responsable propuesto | Resolución y momento |
| :--- | :--- | :--- |
| P01 · Carga y reloj crédito | Arquitectura, QA y Emisor | Perfil peak presencial/financiero y límites de medición sin mezclar entrega de información; antes campaña R16/mes 16. |
| P02 · Suficiencia consentimiento | Cumplimiento Emisor y Cartera | Catálogo de soportes, completitud y tratamiento de histórico sin evidencia; antes R18/mes 16, y olas mes 21. |
| P03 · Separación física/lógica | Arquitectura y Cumplimiento | Conciliar RNF-14 y RT-06.01 documentando diseño acreditable; no rebajar requisito unilateralmente; antes R21. |
| P04 · Alcance pentest | Seguridad y tercero independiente | Inventario de superficies, severidad y retest; cerrar hallazgos críticos/altos abiertos antes producción, obligatorio cap. 20.1. |
| P05 · Conciliación cartera | Migración y Emisor | Claves, cortes, aprobación de explicación/corrección y retorno por tramo; antes R24. |
| P06 · Política de sala | Comercial y Tiendas | Plazo de etiqueta, universo de puntos, operación y muestreo; antes R06/R07/R09 mes 16. |
| P07 · Perfil de cambios de precio | Arquitectura y QA | Distribución temporal de 400.000 eventos/día y prueba por destino; máximo 5 min cajas/digital preservado. |
| P08 · Cobro/captura/reversa | Pedidos, Pagos y Contraparte | Conciliar R03 y RNF-65; bloquear captura inválida y definir reversa ante carreras; antes mes 21. |
| B01 · Línea base catálogo | Equipo requerimientos y Contraparte | Decidir vigencia v3.1 frente a v3.0; reconciliar Anexo B y registrar decisiones/IDs exactos antes cierre de etapa. |
| B02 · Indicadores y ventana | QA y responsables de negocio | Ratificar numeradores, denominadores, causas y propuesta de ventana de 3 meses para tasas anuales; antes actas. |
| B03 · Hitos regulador | Cumplimiento Emisor | Obtener plan de remediación y fechas oficiales; supuesto inicio enero 2027 no basta para probar cumplimiento antes 2029. |
| B04 · Cobertura total pendiente | QA y responsables catálogo/T-12 | Ampliar vínculo requisito-historia-prueba-evidencia al catálogo completo y todos RT aplicables; primera matriz no acredita 100 %. |
| B05 · Umbrales propuestos | Contraparte y dueños de servicio | Validar metas del Anexo D marcadas propuesta y tolerancias pendientes; conservar distinción fuente/propuesta. |

## Configuración pendiente por criterios

Las filas siguientes completan el registro central. Los métodos y umbrales descritos existen como diseño de verificación; estos acuerdos condicionan su ejecutabilidad y aceptación. Las referencias de grupo incluyen todos sus subcriterios, salvo cuando se especifica uno.

| Brecha interna y criterios afectados | Responsable propuesto | Resolución antes de compuerta |
| :--- | :--- | :--- |
| B06 · R01 y R04 | Existencias e Inventario cliente | Fijar tolerancia R01 (sin cifra fuente), fórmula de diferencia, frecuencia, olas y cobertura de conteo; mes 16 y extensión mes 21. |
| B07 · R02/R26 | Pedidos y Operaciones cliente | Clasificar causas técnicas/logísticas, universo/contactos, exclusiones y promesa original; campaña mes 21/evento. |
| B08 · R05/R27 | Existencias e Inventario cliente | Conciliar cinco causas Caso y seis RF-138, fórmula merma y tienda revisora; mes 21. |
| B09 · R07/R08/R09 | Oferta comercial y Precios cliente | Universo puntos y reporte físico, carga consulta histórica y muestra precio exhibido; mes 16, vinculada P06. |
| B10 · R10/R11 | Pedidos, Canales y Logística cliente | Catálogo estados, interfaces y fórmula costo total/efecto sala; mes 21. |
| B11 · R12 | Comisiones y Ventas cliente | Atribución tienda y excepciones comisión; mes 21. |
| B12 · R13/R14 | Marketplace y gerente cliente | Evento inicial/canal/reintentos, indicadores SLA, consecuencias y comunicación conocida por vendedores; mes 21 y renovación anual. |
| B13 · R15 | Posventa/QA y Atención cliente | Capacitación, cobertura 22 tiendas y muestra/frecuencia cliente oculto; mes 21. |
| B14 · R17/R19/R20/R28 | Evidencia/Originación y Cumplimiento Emisor | Material/versiones/medios completos, reloj anterior a aceptación, retención/capacidad/base jurídica; mes 16, vinculada P01/P02. |
| B15 · R22 | Frontera y Cumplimiento cliente | Taxonomía finalidades/bases, muestra de auditoría y acceso autorizado; mes 16 y trimestral. |
| B16 · R25 | Arquitectura, Operaciones y Canales | Orden degradación, estímulos y perfil evento real; mes 16/21, vinculada B03 y capacidad T07. |
| B17 · T01/T02 | QA, Desarrollo y Seguridad | Herramienta, líneas/ramas y exclusiones, población deuda y falsos positivos; antes primer pipeline y cada versión. |
| B18 · T03 | QA y responsable requerimientos | Cadena bidireccional RT/catalogo a historia, prueba, cambio y evidencia; cierre cada etapa 16/21, vinculada B01/B04. |
| B19 · T04 | Seguridad y Cumplimiento | Amenazas, clasificaciones, finalidades y retenciones aprobadas; independencia/alcance pentest y calendario anual; antes 16/21, vinculada P03/P04. |
| B20 · T05 | Operaciones/SRE, Retail y Emisor | Sitios/distancia/amenazas, modo tributario, autorización previa crédito, sondas/exclusiones disponibilidad y retorno 24 h sin duplicidad; antes 16 y durante operación. |
| B21 · T06 | UX/Accesibilidad, QA y dueños canal | Inventario interfaces, usuarios reales y protocolo manual/automático, métricas tarea/perfil; antes 16/21 y liberaciones posteriores. |
| B22 · T07 | Arquitectura rendimiento y Canales | TPS/concurrencia/distribución temporal aprobados, telemetría y crecimiento, máximos por operación; antes campañas 16/21, vinculada P01/P07. |
| B24 · C-T04-03 a C-T04-09 | Seguridad/SOC y Cumplimiento | Inventario eventos, SIEM/EDR, turnos, retención y canales notificación/RCA; antes 16/21. |
| B25 · C-T05-06 a C-T05-08 | SRE/Datos y Operaciones Cliente | Alertamiento, runbooks, capacitación y retorno/conciliación DR; antes 16/21 y operación. |
| B26 · C-T06-03 a C-T06-07 | UX/QA y Operaciones | Dispositivos, tareas/errores, controles táctiles, sistema diseño y aplicabilidad terreno; antes 16/21. |
| B27 · T09 | DevOps/QA/Desarrollo | Ambientes, equivalencia, controles repositorio, secretos, rollback/despliegue y esquema; H3 y antes 16/21. |
| B28 · T10 | QA/Integración/Operaciones y Contraparte | Catálogos de integración/regresión/UAT, actores y resiliencia autónoma antes 16/21 y semestral. |
| B29 · T11 | QA/Arquitectura y Datos/negocio | Marco ocho categorías ISO25010, modelo/escala madurez y umbrales calidad ISO25012; antes línea base. |
| B30 · C-T04-10 / C-T05-09 a 12 / C-T10-06 | Seguridad/Arquitectura/SRE, Operaciones/Cliente e Integración/QA | Completar superficie expuesta, modalidad sitios, clasificación/niveles, BCP/TIC y degradación externa; antes 16/21, Art.78 ilegible como pendiente. |
| B23 · T08 | Datos/Migración y dueños Retail/Emisor | Fuentes/accesos/volúmenes/calidad, transformaciones, ventanas y aprobadores diferencias; dos ensayos completos antes cada corte 16/21, vinculada P05. |

No se atribuye probabilidad ni valoración económica a estos riesgos. La revisión humana debe convertir los responsables por rol en asignaciones nominadas y registrar resoluciones. Los criterios reutilizados de R28 conservan sus brechas de R16/R17/R20, sin duplicar definiciones.
