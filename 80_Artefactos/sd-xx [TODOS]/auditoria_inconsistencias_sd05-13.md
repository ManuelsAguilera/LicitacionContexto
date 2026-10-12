# Auditoría de inconsistencias: Subdocumentos 5 a 13

Fecha: 2026-10-12. Estado: borrador para decidir con el equipo. Continúa `auditoria_inconsistencias_sd01-04.md`, con el mismo método y la misma escala de gravedad.

## Qué se auditó y qué no

| Subdocumento | Archivo leído | Nota |
| :-- | :-- | :-- |
| sd-05 | `sd-05/OnlySimpleSolutions-Subdocumento5.tex` y `-Anexos.tex` | Archivos de Prism sin trackear |
| sd-06 | Cuerpo: copia de `HEAD` (`OSS-Subdocumento6.tex`); `OnlySimpleSolutions-Subdocumento6-Anexos.tex`, `OSS-Formulario-T-9.tex`, `OSS-Formulario-T-10.tex` | El cuerpo no vino en la carpeta de Prism; falta confirmar que `HEAD` es la última versión |
| sd-07 | `sd-07/OnlySimpleSolutions-Subdocumento7.tex` | Solo 7.1 a 7.3 |
| sd-08 | `sd-08/OnlySimpleSolutions-Subdocumento8.tex` | El registro completo de riesgos está en el T-16, que no se leyó |
| sd-09 | `sd-09/OnlySimpleSolutions-Subdocumento9.tex` | — |
| sd-13 | `sd-13/OnlySimpleSolutions-Subdocumento13.tex` | — |
| sd-10, sd-11, sd-12 | Sin contenido | Solo existe el maestro `.md`; no hay nada que auditar |
| sd-14 | Fuera de alcance | Así se acordó |

Las referencias `Sn:L123` son líneas de esos archivos (`S` cuerpo, `A` anexos, `T9` y `T10` formularios). Las comparaciones externas se hicieron contra el estado actual de los sd-01 a sd-04 (ya reconciliados), el glosario de nombres comunes y las Bases.

## Criterio de gravedad

- **Grave:** cifra, plazo, etapa, alcance, arquitectura o régimen jurídico que se contradice y cambia una decisión o el cronograma de 56 meses.
- **Mediana:** nombres de roles, comités, componentes o IDs; remisiones a lo que no existe; promesas de un subdocumento que otro no cumple. No cambia la decisión.
- **Baja:** variantes de nombre, mayúsculas, redondeos y citas con página distinta.

## Resumen

| Tipo | Graves | Medianas | Bajas |
| :-- | :-: | :-: | :-: |
| Externas | 2 (1 resuelta) | 11 | 5 |
| Internas sd-05 | 0 | 8 | 4 |
| Internas sd-06 | 0 | 6 | 4 |
| Internas sd-07 | 0 | 2 | 4 |
| Internas sd-08 | 0 | 5 | 3 |
| Internas sd-09 | 0 | 5 | 4 |
| Internas sd-13 | 0 | 4 | 3 |

Verificado sin hallazgos: la aritmética de las Tablas 8.6, 8.7 y 8.11 del sd-08; las horas del sd-07 (164 cuentas, 40.946 HH = 12.116 + 28.830, 57 nodos del CPM) y su coherencia con el sd-08 (40.946 + 3.688); el muestreo del sd-09 (n=299, 0,99^299 ≈ 0,0495, riesgo de rechazo 25,9 %); las 51 entidades, 314 campos y 81 relaciones del anexo del sd-05; y la conversión de meses a fechas del sd-07 (mes 16 = abril de 2028, mes 21 = septiembre de 2028, mes 56 = agosto de 2031). Las fechas de cartera del sd-05 (cortes T1 a T3, apagado antes del 31-oct-2028) son coherentes con el sd-03.

Ya resuelto durante la lectura (cambios fuera del alcance de este informe, dejados sin commit):
- **EXT-G-02** (ver abajo): `RNF-22` decía «120 % del peak» y las Bases piden 1,5 veces (RT-09.06). Corregido en el sd-02, los dos Excel y los espejos.
- La matriz A.4 decía «Azure Cache for Redis»; el sd-04 ahora usa «Azure Managed Redis». Corregido.

---

## Estado de resolución (2026-10-12)

| Hallazgo | Estado | Qué se hizo |
| :--- | :--- | :--- |
| EXT-G-01 | Resuelto | sd-07 (L658, L746, L767): último corte de cartera antes del 15-oct-2028 y apagado antes del 31-oct-2028 en lugar de «cierre de migración en M21». Editado en el archivo de Prism sin trackear |
| EXT-G-02 | Resuelto | RNF-22 a 1,5 veces el peak declarado (RT-09.06) en el sd-02, los dos Excel y los espejos |

---

# PARTE 1. Inconsistencias externas

## Graves

### EXT-G-01. Cierre de la migración de cartera: mes 21 (sd-07) frente a mes 22 y fechas exactas (sd-03, sd-05, sd-08)
- **Dice.**
  - `S7:L658`: el retiro de la plataforma de crédito en M22 queda «condicionado al cierre de migración en M21». `S7:L582` (Tabla 7.4): retiro en M22, octubre de 2028. `S7:L767`: migración sin fecha única de corte. No aparece ninguna fecha de octubre.
  - sd-03 (3.2.3): cartera migrada a más tardar en el mes 22; último corte antes del 15-oct-2028; apagado antes del 31-oct-2028.
  - `S5:L617-631` (Tabla 5.14): corte T3 del 1 al 14 de octubre de 2028 (mes 22) y apagado antes del 31 de octubre. `S8:L469`: último corte antes del 15-oct-2028, disparador el 15-sep-2028.
- **Por qué creemos que pasó.** El sd-07 planificó el hito antes de la regla de congelamiento (EXT-G-03 de la auditoría anterior) y no se actualizó.
- **Por qué es grave.** Con «cierre en M21» (septiembre de 2028) el último tramo de cartera debería estar migrado un mes antes de lo que dicen el sd-03 y el sd-05, y la ruta crítica del sd-07 (margen cero en el retiro) no recoge la ventana real de 1-abr a 31-oct-2028.
- **Sugerencia.** En el sd-07 sustituir «cierre de migración en M21» por «último corte de cartera antes del 15-oct-2028 (M22) y apagado antes del 31-oct-2028», y reflejarlo en la Tabla 7.4 y en el hito del T-14. Revisar si la holgura cero sigue siendo la misma.

### EXT-G-02. Prueba de carga: 120 % del peak (sd-02) frente a 1,5 veces (Bases, sd-09, T-10) — **resuelta**
- **Dice.** `A2` RNF-22 (y el catálogo): «prueba de carga con perfil del evento anual al 120 % del peak proyectado». `S9:L331` y `T10:L509-511`: carga a 1,5 veces el peak. Las Bases Transversales RT-09.06 (obligatoria): 1,5 veces el peak declarado.
- **Por qué.** El catálogo conservó un valor propio menor que el mínimo de las Bases; el caso puede endurecer, no rebajar.
- **Qué se hizo.** RNF-22 pasó a «a 1,5 veces el peak declarado (RT-09.06)» en A.4, `catalogo-de-requerimientos-depurado-v30.md`, `sd-03_s2_anexo-b` y los dos Excel (parche directo al XML; no se abrieron en Excel).

## Medianas

### EXT-M-01. Comité de Operación «desde el mes 13» (sd-06, sd-07, sd-08) frente al mes 16 (sd-01)
- **Dice.** `S6:L335, L1250, L1856, L2820`, `S7:L560` y `S8:L119`: mensual desde el mes 13. El sd-01 (corregido el 2026-10-11) lo fija desde el mes 16, cuando la Etapa 1 entra en producción. Además `S6:L1572-1574` dice «desde el mes 21, el Comité de Operación continuará» y `S6:L2837-2853` que «asumirá el seguimiento ordinario» desde el mes 21.
- **Sugerencia.** Una sola regla en los cuatro subdocumentos: mes 16 (o mes 13 si se decide que arranca con la marcha blanca; en ese caso hay que volver a corregir el sd-01). La definición de «seguimiento ordinario desde el mes 21» debe quedar como un cambio de alcance (de Etapa 1 a toda la solución), no como un segundo inicio.

### EXT-M-02. Catálogo de requerimientos v3.0 / 307 (sd-06, sd-09, T-10) frente a v3.1 / 308 (sd-03)
- **Dice.** `S6:L2959, L3641` (223 RF + 75 RNF + 9 OP = 307), `S9:L194` («catálogo oficial v3.0») y `T10:L238` («v3.0»). El sd-03 fija la versión vigente 3.1, de 308 elementos (227 RF, 72 RNF, 9 OP).
- **Sugerencia.** Citar la versión 3.1 y sus cifras en los tres, o aclarar «recibido v3.0; vigente v3.1» como se hizo en el sd-02.

### EXT-M-03. Roles del equipo: diez roles (sd-06, sd-07, sd-09) frente a siete (sd-01)
- **Dice.** `S7` Tabla 7.1 (L144-158) y `S6:L303-307`: Jefe de Proyecto, Líder Funcional, Arquitecto de Solución, Líder de Desarrollo, Líder de Integración, Líder de Datos, Encargado de Seguridad de la Información, Líder de Calidad y Pruebas, Líder de Implantación y Gestión del Cambio, Líder de Operación / SRE. El sd-01 (1.2 y 1.5) lista siete roles de jefatura (Jefe de Proyecto, Arquitecto, Seguridad, Datos, Calidad, Operación, Implantación y Gestión del Cambio) en 16 personas, y dice que la 1.5 usa «los roles del punto 1.2». Faltan en el sd-01 el Líder Funcional, el de Desarrollo y el de Integración. Los nombres también cambian: «Líder de Calidad» (sd-01) frente a «Líder de Calidad y Pruebas» (sd-06, sd-07, sd-09) y «Líder QA» (`S9:L359`); «Líder de Operación» frente a «Líder de Operación / SRE», «Operaciones/SRE» y «Operación/SRE».
- **Por qué.** El sd-01 resume al equipo; los sd-06 y sd-07 trabajan con la estructura de la EDT, que tiene diez responsables.
- **Sugerencia.** Decidir la lista oficial. Lo más simple: el sd-07 (Tabla 7.1) manda sobre la EDT y el sd-01 y el sd-12 la reflejan, con una tabla de equivalencia entre roles de jefatura y las 16 personas. Fijar un nombre por rol («Líder de Calidad y Pruebas», «Líder de Operación»; «SRE» solo como descripción) y agregarlo al glosario.

### EXT-M-04. Marcas Fortinet y Dell en el sd-06 y el T-9 frente al sd-01 y el sd-04
- **Dice.** `T9:L1532-1533`: «Fortinet o equivalente justificado» y «Dell Technologies u opción técnicamente equivalente» como parte de la oferta; `S6:L2293-2295` los presenta como «proveedores y aliados tecnológicos asociados a la solución». `S6:L2426` aclara que la mención de fabricante no acredita una contratación. El sd-01 ya declara solo la alianza con Microsoft Azure (EXT-M-09 de la auditoría anterior) y el sd-04 no nombra esas marcas.
- **Sugerencia.** Mantener «o equivalente justificado» y quitar la calificación de «aliados» en el sd-06. Dejar las marcas como candidatas hasta que el sd-04 y el T-11 cierren la elección.

### EXT-M-05. Cadena de herramientas del T-10 frente al sd-04 y la matriz A.4
- **Dice.** `T10:L454-466` propone GitHub Enterprise y GitHub Actions (ejecutores segregados para el Emisor), SonarQube, Trivy, Syft, Cosign, OWASP ZAP, Pact, Playwright, k6, Azure Container Registry, y deja Ansible, Helm, Argo CD o K3s como candidatas; Terraform «comprometida»; Azure Key Vault y HSM «según clasificación» (HSM para llaves del Emisor). El sd-04 solo fija Terraform y un canal de entrega continua que «reutiliza el del Cliente si cumple», y no selecciona HSM. La matriz A.4 (actualizada el 2026-10-11) dice «herramientas por fijar en el Subdocumento 4 y el Formulario T-11».
- **Sugerencia.** El T-10 es hoy la única fuente de la cadena de herramientas. Adoptarla como propuesta en el sd-04 (con el aviso de que el canal del Cliente se reutiliza si cumple) y actualizar A.4. Decidir si el Emisor lleva HSM (pendiente ya anotado en `avisos_otros_subdocumentos.md`).

### EXT-M-06. El sd-03 delega una decisión al sd-06 que el sd-06 no desarrolla
- **Dice.** sd-03 (3.3.1 y servicio de clientes Retail): «SD-06 programará la decisión de conservar, remediar o sustituir cada plataforma antes de la ola que dependa de ella» y «mecanismo de primera etapa… desarrollado en SD-06». El sd-06 (`S6:L3097-3101`) solo repite que comercio electrónico y fidelización «se mantienen e integran», y ni el sd-06 ni el sd-07 ni el sd-09 tienen una compuerta de decisión ni una fecha.
- **Sugerencia.** Agregar en el sd-06 (6.2) y en el sd-07 un hito de decisión (por ejemplo, tras la marcha blanca de la Etapa 1) para el comercio electrónico y la fidelización, con el criterio de las pruebas con umbral del sd-03. Alternativa: quitar la delegación del sd-03.

### EXT-M-07. Prueba del corte de enlace y piloto de los meses 6 y 7: choque posible con el evento anual y omisión en el sd-09
- **Dice.** El sd-03 fija un corte provocado de 24 horas en una de las tres tiendas del piloto, en los meses 6 y 7 (junio y julio de 2027), «fuera de la semana previa y de los tres días del evento anual». `S7:L765`: piloto técnico M6-7 «fuera de congelamientos», pero `S7:L590` incluye el evento anual «de mayo o junio» y su semana previa, y M6 es junio de 2027. `S5:L379` repite «meses 6 y 7». El sd-09 no menciona ni el corte provocado, ni el piloto, ni el perfil de 104.000 pedidos en tres días (solo «ambos peaks del Caso»).
- **Sugerencia.** En el sd-07, ubicar el corte en la primera quincena de julio o después de conocer la fecha del evento, y decirlo igual que el sd-03. En el sd-09, agregar la prueba de crédito sin enlace (con sus criterios) y el perfil del evento anual como caso de la prueba de carga.

### EXT-M-08. El sd-05 atribuye al sd-03 que una porción del núcleo de 2009 sigue activa al final del contrato
- **Dice.** `S5:L685`: «lo que establece el Capítulo 3, donde una porción del núcleo de 2009 puede seguir activa al término del contrato; esa porción no se migra». El sd-03 no dice eso: SP-01 reemplaza el sistema central «por etapas» y el escenario B lo mantiene «hasta que se verifica la transferencia de sus funciones y registros». El sd-04 (ADR-01) lo retira por olas.
- **Sugerencia.** Decidir si hay una porción residual. Si la hay, declararla en el sd-03 (supuesto o exclusión) con su fundamento; si no, quitar la frase y la fila de la Tabla 5.16.

### EXT-M-09. Remisiones del sd-05 a capítulos que no corresponden
- **Dice.** `S5:L696`: los contactos de mesa de ayuda y la dotación operacional «se coordinan con el Capítulo 7 y el Formulario T-15»; el Capítulo 7 es el plan de trabajo, y la mesa de ayuda corresponde al sd-10 (servicios de operación). El anexo (`A5:L437, L1926`) remite a la «sección 5.1.5» (Cliente Retail) para la sensibilidad de los datos y para los datos maestros, y la definición está en 5.1.9.
- **Sugerencia.** Corregir las tres remisiones (sd-10 para la mesa de ayuda; 5.1.9 para la sensibilidad).

### EXT-M-10. La matriz A.4 y el sd-13: anexos, escala TRL y zona inexistentes
- **Dice.** `A2` A.4 (RT-26.01, RT-26.03): «las 5 fichas del Formulario T-19 declaran… capa, zona y módulo» y «Nivel de madurez y escala utilizada (escala TRL)», con remisión a «Subdocumento 13, Anexos A.1 a A.5». El sd-13 no tiene anexos ni T-19, no usa TRL (usa una escala de evidencia de tres estados, `S13:L111`) y solo declara la capa.
- **Sugerencia.** Corregir A.4 con lo que dice el sd-13 (secciones «Tecnología y madurez» e «Incorporación a arquitectura y EDT» de cada innovación) o ajustar el sd-13 a lo que A.4 promete. Lo segundo exige TRL y zona; lo primero es más barato y suficiente para RT-26.03 (pide «la escala utilizada», no TRL).

### EXT-M-11. El sd-13 depende de un «canal móvil» que el sd-03 no define
- **Dice.** `S13:L283` (Modo Tienda): «servicio de clientes Retail y canal móvil asignados a la Etapa 2 en el sd-03». El sd-03 asigna el Servicio de clientes Retail a la Etapa 2, pero no tiene ningún «canal móvil». El sd-13 llama además al mismo canal «canal digital» (`L101, L195`), «canal móvil» (`L283`) y «canal» (innovación 4); el glosario deja «canal digital» como nombre provisional.
- **Sugerencia.** Definir en el sd-03 o el sd-04 si la aplicación móvil del cliente es un canal (hoy solo existen «móviles del personal» y el comercio electrónico) y usar un solo nombre en el sd-13.

## Bajas

### EXT-B-01. «Plataforma de 2011» y «crédito de 2011» en prosa
`S5:L379, L631, L660, L687`, `S8:L161, L265` (plataforma de 2011 a secas) y `S6:L3099` («el crédito de 2011»). El glosario pide «plataforma de crédito de 2011» en prosa y el nombre corto solo en tablas y figuras.

### EXT-B-02. «Frente» para equipos de trabajo
`S6:L448, L1635`, `S7:L462, L494, L498` («once frentes»), `T9:L182, L482, L599` («líderes de frente») y `T10:L182`. El glosario reserva «frente» para los tres frentes de la solución; los equipos de trabajo son «áreas de trabajo».

### EXT-B-03. Mayúsculas y nombres de actores
«CLIENTE», «cliente» y «Cliente» (`S7:L110, L145`, `T9:L333`, `S8:L113`); «contraparte técnica» frente a «Contraparte Técnica»; «jefe de proyecto» frente a «Jefe de Proyecto» (`S7:L537`, `S6`, `S9:L369`); «adjudicatario» (`S7:L787`); «Coordinación de personas» frente a «Gestión de Personas» (`S6`); «dueño de producto» y «product owner» (`S6`).

### EXT-B-04. «Ámbito» y «servicio»
`S6:L3384-3389` clasifica los servicios en «Retail, Emisor y plataforma» y deja X-01 en «plataforma» (sd-03: Frontera). `S6:L3090` llama «servicios» a los códigos de área (R:M, R:V, R:CL, F:C). `S5` rotula la Frontera como «Transversal» (`L202`) y «Local» (`A5:L1773`). `S5` llama «Emisor» a la filial emisora (`L164`).

### EXT-B-05. Cálculo de los «22 días» del evento anual
`S5:L692` dice que 104.000 pedidos equivalen «por cálculo» a unos 22 días de la tasa ordinaria; la cuenta (104.000 / 5.205 por día) da cerca de 20. El Caso dice 22 días. Ajustar la frase a «el Caso lo equipara a 22 días», como ya hace el sd-02.

---

# PARTE 2. Inconsistencias internas

## sd-05 (modelo y gestión de datos)

### Medianas
- **INT-05-M-01. Orígenes de datos a migrar.** `A5:L2070` (Tabla A.59) suma «siete orígenes» para 264,5 GB, el cuerpo dice «ocho filas» (`S5:L568`) y «siete grupos» (`L528`); A.60 perfila solo seis (`A5:L2096-2101`). **Sugerencia:** un solo conteo (la Tabla 5.12 tiene ocho filas) y que A.60 diga qué dos orígenes no perfila.
- **INT-05-M-02. Titulares contados dos veces.** La Tabla 5.12 pone «hasta 620.000 fichas de titulares» en Cartera (`L563`) y «cota supuesta de 1,38 millones de titulares» en el Padrón (`L564`), con posible doble conteo en los 264,5 GB. **Sugerencia:** decir si el padrón incluye a los 620.000 o si se suman.
- **INT-05-M-03. Nodos: 24 o 28.** `A5:L2028` usa 24 nodos (22 tiendas + 2 centros), `A5:L2067` usa «x 28 nodos». El cuerpo (`L731`) aclara que 28 son destinos (con 4 canales). **Sugerencia:** llamar «destinos» a los 28.
- **INT-05-M-04. Supuestos que no están en A.57.** `A5:L1977` afirma que todo supuesto está en A.57, pero faltan 6 cuotas por plan, 12 cuotas por tarjeta, 40 % de compras financiadas, 10 % de denegadas, 2,2 líneas por pedido y 1,3 reservas por línea, 310.000 etiquetas con 12 cambios, entre otros (`A5:L2027-2038`). **Sugerencia:** agregarlos a A.57 o marcarlos «supuesto» en la columna de origen.
- **INT-05-M-05. Quién aprueba la retención.** `A5:L424`: plazo de la bitácora «aprobado por Contraloría»; `S5:L296, L490`: aprobación del área jurídica del Cliente. **Sugerencia:** una sola instancia (el sd-04 pide aprobación jurídica de cada cruce).
- **INT-05-M-06. Postura de disponibilidad.** `A5:L433`: «solo la captura de ventas y la caché priorizan la disponibilidad local»; `S5` Tabla 5.5 marca EM-03 «Disponibilidad condicionada» y la caché «Disponibilidad». **Sugerencia:** alinear el anexo con la Tabla 5.5.
- **INT-05-M-07. Entidades de venta en tienda.** `A5:L422` asigna RE-17 a RE-20 a la captura desconectada; `S5:L369`, RE-17 a RE-19. **Sugerencia:** confirmar si RE-20 (atribución de comisión) va en tienda.
- **INT-05-M-08. Campos de datos personales.** El anexo marca como Personal RE-05, RE-16, RE-19, EM-05, EM-07 y el nombre del nodo (RE-26), mientras el cuerpo (`S5:L454-458`) solo lista RE-07, RE-21, RE-23 y EM-01 a EM-11; EM-11 y EM-01 no tienen campos sensibles en el anexo. **Sugerencia:** conciliar la Tabla 5.8 con el anexo; el nombre de una tienda no es dato personal.

### Bajas
- **INT-05-B-01.** El 620.000 se nombra tarjetas (`L131`), clientes (`L528`) y cuentas (`L610`). El Caso dice 1,38 millones de tarjetas, 620.000 con saldo.
- **INT-05-B-02.** Tabla 5.23 está en el índice pero la tabla del cuerpo (`L900`) no tiene título ni etiqueta. `S5:L439` dice «ocho filas» y enumera seis.
- **INT-05-B-03.** Los códigos de entidad LO-01 (diario) y LO-02 (caché) están al revés que los servicios L-01 (caché) y L-02 (diario) del sd-04; L-03 no aparece. Dueños de Venta distintos en `L234` y en la Tabla 5.4.
- **INT-05-B-04.** Redondeos del anexo (192,5 frente a 192,6; 3,25 frente a 3,2) y A.59 citada para dos usos distintos (`S5:L759, L761`).

## sd-06 (metodologías, T-9, T-10)

### Medianas
- **INT-06-M-01. Instancia que aprueba los cruces Retail–Emisor.** `T9:L485`: Líder de Datos + Seguridad + cumplimiento → Comité de Arquitectura → Comité Ejecutivo como instancia final; `T10:L693`: «instancia competente», con el Comité Ejecutivo solo informado; `T9:L1079` exige además «aprobación de Contraloría y del Negocio Financiero». **Sugerencia:** una ruta única, coherente con el sd-04 (aprobación jurídica de cada cruce).
- **INT-06-M-02. Reparto de lo físico.** `T9:L1532` (Fortinet): instalación física «por Ancoa o su integrador cuando corresponda»; `T9:L1536`: conectividad, seguridad y canalizaciones del «centro local» por OSS; `T9:L1537`: canalizaciones de tiendas «según el reparto por sitio». «Centro local» no existe en el glosario (DC-01/DC-02). **Sugerencia:** una tabla de reparto idéntica a la del sd-03 (SP-04) y la Tabla 4.11 del sd-04.
- **INT-06-M-03. Registro de interesados.** `A6:L125-131, L199-205` y `T9:L872-874` definen distintos campos de identificación, clasificación y evaluación; el anexo dice que las planillas «se entregan sin completar» y el T-9 trae la matriz precargada. **Sugerencia:** una definición del registro y decir que el T-9 es la propuesta inicial.
- **INT-06-M-04. Figuras y tablas.** El anexo cita «Figura 1» (`A6:L100, L197`) y el T-9 «Figuras 6.1 y 6.2» (`T9:L810`) para el mismo registro; los números de tabla T-9.n y T-10.n chocan con los de las secciones. **Sugerencia:** una convención.
- **INT-06-M-05. Metas de la Tabla 5.** `S6:L1216` dice que las metas de los indicadores «se fijarán» en H1, pero la Tabla 5 (`L1473-1496`) ya las trae (85 %, 90 %, 4,0, 95 %). **Sugerencia:** decir «se confirman en H1».
- **INT-06-M-06. Agentes de cambio.** `S6:L1195` y la Tabla 5 (`L1488`) comprometen 22 de 22 agentes antes de H6; `L1874` solo «propondrá que Ancoa designe». **Sugerencia:** compromiso de OSS con dependencia del Cliente, escrito igual en los tres lugares.

### Bajas
- **INT-06-B-01.** Remisión imprecisa en la Tabla 1 (`L161`: «6.1.7 y 6.2.7» para la transferencia de conocimiento, que está en 6.1.3.4) y «funciones de aptitud» (`L3119`) sin definir en 6.2.2.
- **INT-06-B-02.** Tres nombres para el mismo periodo: intervalo de planificación, de coordinación y «intervalo» (`A6:L211`, `T9:L227, L947`).
- **INT-06-B-03.** Reservas del 15 % (deuda técnica) y del 30 % (marcha blanca) que dicen no contarse doble sin decir la capacidad total (`S6:L3168, L3559`).
- **INT-06-B-04.** `T9:L346` pone al Líder de Operación en el mes 6 y `T10:L378` no fecha el hito H3 (en el sd-07 es el mes 6); `T10:L238` y la declaración de uso de IA (17 filas con «% PENDIENTE») sin completar.

## sd-07 (plan de trabajo)

### Medianas
- **INT-07-M-01. Hitos en desorden.** La Tabla 7.6 lista H6 (M13) y H8 (M14) antes de H7 (M16); el texto lo reconoce (`L702`). `S7:L468` cita H9 sin mes (la tabla da M17). **Sugerencia:** numerar los hitos por orden de fecha o decir por qué H8 precede a H7.
- **INT-07-M-02. Paquetes de trabajo.** `S7:L116` dice 40 paquetes y `L543/L761` 35 más cinco de seguimiento. **Sugerencia:** decir el desglose en la primera mención.

### Bajas
- **INT-07-B-01.** Cinco variantes de rol y de comité («Encargado de Seguridad», «Líder de Calidad», «comité del proyecto»).
- **INT-07-B-02.** «Mes 1» se define como «primer mes completo desde el inicio» y a la vez como enero de 2027 (`L564`).
- **INT-07-B-03.** La declaración de uso de IA dice «diagramas mermaid» (`L811`); AGENTS.md prohíbe Mermaid en la propuesta.
- **INT-07-B-04.** El capítulo anuncia T-14, T-15 y T-18 dentro del capítulo (`L100`); no están en el archivo.

## sd-08 (plan de riesgos)

### Medianas
- **INT-08-M-01. Residuales de R-18, R-20, R-24 y R-34.** La Tabla 8.10 da residual 0,08 (probabilidad de 0,60 a 0,20), pero `S8:L537` dice que bajan «solo de 0,60 a 0,40» y la Tabla 8.11 usa una reducción de un tercio (P 0,40, residual 0,16). **Sugerencia:** decidir la reducción y recalcular 8.10, 8.11 y los totales de horas (3.688 h).
- **INT-08-M-02. «Cuatro respuestas» que son cinco.** `S8:L541` dice cuatro respuestas de riesgos medios sin cuenta y lista cinco (R-06, R-27, R-28, R-36, R-33), una de ellas R-33, que es un riesgo alto con cuenta 1.11.3.
- **INT-08-M-03. Número de riesgos.** Se declaran 37 (`L97, L204, L252`) y existe R-38; en el texto no aparecen R-14, R-21, R-26, R-30 ni R-35. **Sugerencia:** confirmar contra el T-16.
- **INT-08-M-04. Regla del hito.** `S8:L252` dice que cinco riesgos (R-02, R-11, R-23, R-33, R-37) llegan a impacto 0,80 por la regla del hito, pero R-12 y R-13 también (`L287, L289`). `S8:L186` fija tolerancia cero en los hitos de los meses 16, 21 y 56 y omite el mes 22 que `L161` sí cuenta. **Sugerencia:** listar los siete y agregar el mes 22.
- **INT-08-M-05. Disparador de R-02.** `S8:L465`: el riesgo se activa al «recibir la fecha con menos de ocho semanas de aviso», pero `L285` dice que el aviso es de unas seis semanas, así que se activaría siempre. **Sugerencia:** disparar con «menos de seis semanas» o definir un aviso mínimo con la asociación gremial.

### Bajas
- **INT-08-B-01.** `S8:L349` dice que horas y semanas vienen de «cada ficha del apartado 8.3», que no tiene fichas.
- **INT-08-B-02.** El numeral 7.4 del Caso se cita en la página 16 y en la 17 (`L323, L325`).
- **INT-08-B-03.** «Error de precio menor que 3 %» (`L315, L475`) frente a «discrepancia de precio inferior a 3 %» (`L571`); «servicio de control de cruces» sin X-01; «CLIENTE» y «emisor» en minúscula.

## sd-09 (plan de calidad)

### Medianas
- **INT-09-M-01. Requisito de los ensayos de migración.** `S9:L329` cita RT-05.15 y `L363` RT-05.13 para «al menos dos ensayos completos». Las Bases: RT-05.13 son los dos ensayos; RT-05.15 son los datos históricos. **Sugerencia:** RT-05.13 en ambos.
- **INT-09-M-02. Remisiones a lo que no existe.** «Anexo T-7.09» (`L313, L487`) no está en el archivo; T-18 aparece solo en `L329`; «Anexo D» (`L147, L194`) no dice de qué subdocumento (es el Anexo D del sd-03, 28 resultados).
- **INT-09-M-03. Declaración de uso de IA.** `S9:L472`: «no se reporta revisión humana», pero la Tabla 9.5 nombra a una persona revisora en todas las filas.
- **INT-09-M-04. Mes de arranque de la calidad.** `S9:L113`: «en el primer mes»; `L400`: «preparación desde el mes 2». El sd-07 sitúa la calidad en M1-21.
- **INT-09-M-05. Tres nombres para el mismo rol y para el cronograma.** «Líder de Calidad», «Líder de Calidad y Pruebas» y «Líder QA»; «Capítulo 7», «SD07» y «E1/E2» para el plan de trabajo y las etapas.

### Bajas
- **INT-09-B-01.** Tabla 9.3 (`L175`) aparece antes de la Tabla 9.2 (`L229`).
- **INT-09-B-02.** Los números de figura no coinciden con los de los archivos (Fig. 9.1 = `diag-09-03`, 9.2 = `diag-09-01`, 9.3 = `diag-09-04`, 9.4 = `diag-09-02`).
- **INT-09-B-03.** «380 líneas de caja» (`L143, L157`) y «380 cajas» (`L163`); «Operaciones/SRE», «Operación/SRE» y «Operaciones».
- **INT-09-B-04.** La Tabla 9.1 mezcla en una celda el P95 común a 1,5 veces el peak y los máximos del Caso (`L131` y `L143`).

## sd-13 (innovaciones)

### Medianas
- **INT-13-M-01. T-19 inexistente.** La Tabla 13.1 lista una fila «T-19 / Redacción de los listados» (`L349-L353, L383`), pero el capítulo no contiene ningún T-19; `L93` solo dice que el T-19 «reunirá» las fichas.
- **INT-13-M-02. Figura declarada que no existe.** `S13:L347` dice que se «generó la figura funcional» y todas las filas de la Tabla 13.1 dicen «Diagramas: Ninguno».
- **INT-13-M-03. Dos referentes para la EDT.** `S13:L93`: «rama 1.10 de la EDT del subdocumento 7»; `L117`: «rama 1.10 Innovaciones del T-14». Mezcla de «capítulo N» y «subdocumento N» para el mismo documento (sd-07, sd-08, sd-04).
- **INT-13-M-04. La aceptación se trata distinto por innovación.** La innovación 1 acepta en la marcha blanca de la Etapa 2 (`L117`), la 3 «antes del mes 21» (`L197`) y la 4 no tiene marcha blanca ni aceptación (`L237`). **Sugerencia:** una regla común (aceptación en la marcha blanca de la etapa en que entra).

### Bajas
- **INT-13-B-01.** Los encabezados 13.1 a 13.5 no llevan el nombre de la innovación (solo «Innovación 1»…).
- **INT-13-B-02.** `S13:L141` vs `L173`: RF-134 se presenta como programa de conteo y como vuelta atrás; verificar contra el catálogo 3.1.
- **INT-13-B-03.** Los riesgos de adopción se remiten al «capítulo 8» y al T-16; ambos fuera del archivo.

---

# Descartado o pasa a la auditoría de errores

- **Atribución de RT-09.01 al Caso (sd-06 `L3057-3059`).** No es una contradicción: la tabla del capítulo 15 del Caso fija esos valores, así que citar al Caso es correcto. La mezcla de citas al Caso y a las Bases Transversales es por diseño (el Caso endurece lo transversal).
- **Declaraciones de uso de IA incompletas** (`S6` con «% PENDIENTE», `S13:L351`): cumplimiento del Comunicado 10.
- **«Martín Vásquez» con tilde** (`S13:L345`) frente a «Martin Vasquez» del equipo: ortografía.
- **Pendientes de redacción:** T-14, T-15, T-16, T-18 y T-19 aún no están en los `.tex`; los sd-10, sd-11 y sd-12 no se han redactado.
- **Diferencia PERT de 17,33 HH en el sd-07:** el texto la reconoce.

# Orden sugerido de resolución

1. **EXT-G-01** (cartera en el sd-07) y **EXT-M-07** (corte de enlace y piloto): son plazos y alimentan la ruta crítica y las pruebas.
2. **EXT-M-03** (roles) y **EXT-M-01** (Comité de Operación): se reflejan en los sd-01, sd-06, sd-07, sd-08, sd-09 y en el futuro sd-12.
3. **EXT-M-06, EXT-M-08, EXT-M-10 y EXT-M-11**: promesas de un subdocumento a otro y A.4.
4. **EXT-M-04 y EXT-M-05**: marcas y herramientas, junto con la definición del sd-04 y el T-11.
5. **INT-08-M-01 a INT-08-M-05**: cambian horas de reserva, así que conviene fijarlas antes de la oferta económica.
6. Resto de las medianas internas y de las bajas.
