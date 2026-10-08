# Maestro de actores (borrador v0)

Documento de contexto, no es entregable. Fecha: 2026-10-08. **Borrador por validar por el equipo.** Relaciona tres capas que hoy viven en lugares distintos: los grupos de interés del sd-02 (sección 2.4), los actores del sistema (roles y sistemas que interactúan con la solución) y su uso en el sd-03 (servicios, secciones 3.3 y 3.4, resultados del Anexo D). Es la base del cálculo de UAW en la estimación por Puntos de Casos de Uso y sirve a los subdocumentos 4, 6, 7 y 12.

Fuentes, en orden: `02_Propuesta/latex_final/sd-02.tex` (2.4, Tabla 2.5 y 2.2.2), `02_Propuesta/latex_final/sd-03.tex` (3.3.1, 3.3.2, 3.4.6), el Anexo B (actor implícito en cada requerimiento) y el Caso (cap. 2.4 «Las personas», cap. 5 «Los sistemas» y cap. 8 entrevistas). Si un dato difiere de los `.tex`, mandan los `.tex`; aquí se declara la diferencia, no se corrige.

## 1. Cómo leerlo

- **Grupo de interés** (sd-02). Conjunto de personas u organismos definido por su influencia e interés en el proyecto. No interactúa necesariamente con el sistema.
- **Actor del sistema** (UCP, FEP03 diap. 26). Rol o sistema que interactúa con la solución. Una persona es un rol (cinco mil vecinos son un solo actor). El tipo UCP depende de la interfaz: 1 sistema por interfaz de programación, 2 sistema por protocolo o archivo, 3 persona con interfaz gráfica.
- **Rol del proyecto** (por ejemplo la Contraparte Técnica o el Comité Ejecutivo). Gobierna el proyecto, no usa el sistema, y por eso no es actor para el UAW.

Convención propuesta para los sistemas externos: se clasifican por la interfaz **objetivo** que ofrecerá la plataforma de integración (interfaz de programación, tipo 1). Hoy la mayoría de las 14 interfaces opera por archivo y lote nocturno (tipo 2, Caso cap. 5). La decisión es del equipo (puerta G1) y se declara en el anexo de estimación.

## 2. Grupos de interés (Tabla 2.5 del sd-02)

| Código | Grupo | Actores principales (sd-02) | Caso, dotación |
| :-- | :-- | :-- | :-- |
| G-01 | Dirección y control | Directorio, Gerencia General, Contraloría | Gerencia General, Contraloría y Cumplimiento (una misma persona ocupa ambos cargos, cap. 8) |
| G-02 | Propiedad | Grupo familiar controlador y fondos de inversión | No aplica |
| G-03 | Negocios y operación | Comercial, Canales Digitales, Logística, Negocio Financiero | Comercial y compras 140, Marketing y canales digitales 60, Logística y planificación 90, Negocio financiero 320 |
| G-04 | Soporte tecnológico y control operacional | TI, Prevención de Pérdidas | TI 46, Prevención de pérdidas 180 |
| G-05 | Operación de tienda | Jefaturas, vendedores, cajeros, reposición y bodega | Vendedores y cajeros 3.820, jefaturas 240, reposición y bodega de tienda 780 |
| G-06 | Clientes y terceros operacionales | Clientes, titulares de tarjeta, vendedores de marketplace, proveedores tecnológicos y logísticos | Repositores externos ≈ 1.100 |
| G-07 | Organismos externos | Autoridad financiera, de protección al consumidor y tributaria | No aplica |

## 3. Actores del sistema

### 3.1 Personas (tipo 3)

| Código | Actor (nombre canónico) | Grupo | Servicios con los que interactúa | Fuente |
| :-- | :-- | :-- | :-- | :-- |
| AH-01 | Cliente | G-06 | Oferta comercial, existencias, pedidos, posventa, clientes Retail | sd-02 2.4; sd-03 3.3.1; Anexo B (31 menciones) |
| AH-02 | Titular de tarjeta | G-06 | Originación de crédito, cartera de crédito, evidencia financiera | sd-03 Figura 3.4; sd-02 2.4 |
| AH-03 | Vendedor de piso | G-05 | Ventas, existencias (consulta de disponibilidad), originación de crédito (ofrece la tarjeta), posventa | Caso 2.4; Anexo B (5) |
| AH-04 | Cajero | G-05 | Ventas, originación de crédito, posventa | Caso 2.4; Anexo B (2) |
| AH-05 | Jefatura de tienda o de departamento | G-05 | Existencias (conteos, informe de merma), oferta comercial (estado de exhibición), posventa | Caso 2.4 y entrevista de jefa de tienda; sd-03 3.4.6 |
| AH-06 | Personal de reposición y bodega de tienda | G-05 | Existencias (conteo, probador), oferta comercial (cambio de etiquetas), pedidos (preparación) | Caso 2.4 |
| AH-07 | Personal de centros de distribución (incluye a quien carga las existencias de Concepción, RC-10) | G-03 (Logística) | Abastecimiento, existencias, pedidos | Caso 2.4 (620 personas). Grupo asignado en el sd-02 el 2026-10-08. Trabajan 100 personas en Concepción y 520 en el centro principal (dato del usuario, 2026-10-08) |
| AH-08 | Repositor externo de proveedor | G-06 (sd-02 lo ubica en el cuadrante de menor influencia, fuera de la Tabla 2.5) | Existencias (acceso controlado) | Caso 2.4; sd-02 2.4.2 |
| AH-09 | Ejecutivo de atención y posventa | G-05 | Posventa, pedidos, marketplace | Anexo B («ejecutivo», 11 menciones); sd-03 3.4.6. Por validar el cargo |
| AH-10 | Ejecutivo del negocio financiero | G-03 | Originación de crédito, cartera de crédito (repactación y cobranza), evidencia financiera | Caso 2.4 (originación, servicio al cliente, cobranza); sd-03 3.3.2 |
| AH-11 | Comercial y compras | G-03 | Oferta comercial (precios, promociones, campañas), abastecimiento | Caso 2.4; sd-03 3.4.2 |
| AH-12 | Planificación de abastecimiento (Logística) | G-03 | Abastecimiento, existencias | Caso 2.4; Anexo B («planificador», 1) |
| AH-13 | Canales digitales y Marketing | G-03 | Marketplace, clientes Retail (segmentos y campañas), oferta comercial; solicitudes de cruce al Servicio de control de cruces | Caso 2.4; sd-03 Tabla 3.7 (Marketing) |
| AH-14 | Prevención de pérdidas | G-04 | Existencias (conteos, informe de merma) | Caso 2.4; sd-02 Tabla 2.5; Anexo B |
| AH-15 | Contraloría y Cumplimiento | G-01 | Control de cruces, evidencia financiera (auditoría y acceso) | Caso cap. 8 (una misma persona); sd-02 2.4.3; sd-03 3.4.6 |
| AH-16 | Administrador de sistemas (TI) | G-04 | Base tecnológica (identidad y accesos, observabilidad, integración) y todos los servicios en administración | Caso 2.4; sd-03 3.4.6. **Actor de administración que ningún documento nombra como tal** |
| AH-17 | Vendedor de marketplace (externo) | G-06 | Marketplace, existencias (declaración de la existencia), posventa | Caso cap. 8; Anexo B (9). Decidido: tipo 1 (interfaz de programación), 2026-10-08 |
| AH-18 | Analista de información (autoservicio analítico) | G-03 | Base tecnológica (capacidad analítica), todos los servicios en consulta | sd-03 3.3.2. Propuesta del 2026-10-08 |

### 3.2 Sistemas (tipos 1 y 2; interfaz por definir con el mapa de las 14 interfaces)

| Código | Actor (nombre canónico) | Servicios con los que interactúa | Estado según el Caso | Fuente |
| :-- | :-- | :-- | :-- | :-- |
| AS-01 | Sistema de gestión empresarial y facturación (ERP/DTE) | Ventas, abastecimiento, posventa (notas de crédito), comisiones | Se mantiene. Único emisor tributario | Caso cap. 5; sd-03 3.3.2 |
| AS-02 | Sistema de gestión de almacenes del centro de distribución principal (WMS) | Existencias, abastecimiento, pedidos | Se mantiene | Caso cap. 5; sd-03 3.3.2 |
| AS-03 | Plataforma de marketplace (2022) | Marketplace, existencias, pedidos, posventa | Se mantiene | Caso cap. 5 |
| AS-04 | Plataforma de comercio electrónico (2019) | Existencias, pedidos, oferta comercial | Se mantiene o se reemplaza, con justificación | Caso cap. 5; sd-03 3.3.1 |
| AS-05 | Sistema de fidelización (2017) | Clientes Retail, ventas | Se integra inicialmente | Caso cap. 5; sd-03 3.3.2 |
| AS-07 | Transportistas de última milla | Pedidos | Fuera del alcance. Se integran | Caso cap. 11; sd-03 3.3.2 |
| AS-08 | Medios de pago y terminales de pago | Ventas, pedidos | Por confirmar si se integran por procesador | sd-03 Figuras 3.5 y 3.8 |
| AS-09 | Sistema central de retail (2009) | Oferta comercial, abastecimiento, existencias (durante la convivencia) | Se reemplaza por etapas | Caso cap. 5; sd-03 3.3.1 |
| AS-10 | Plataforma de originación y cobranza (2011) | Originación, cartera, evidencia financiera (durante la migración por olas) | Se reemplaza | Caso cap. 5; sd-03 3.3.1 |
| AS-11 | Sistema de remuneraciones (módulo del ERP) | Comisiones | Se mantiene. La solución solo entrega la base de comisión | Caso cap. 11; sd-03 3.3.2 |
| AS-12 | Autoridades fiscalizadoras (financiera, consumidor, tributaria) | Evidencia financiera, control de cruces (reportes y requerimientos) | Reciben reportes. Si no acceden al sistema, no son actor | sd-02 2.4; sd-03 3.3.1 |
| AS-13 | Proveedores de mercadería | Abastecimiento | Por validar | sd-03 3.3.2 (coordinar proveedores). Propuesta del 2026-10-08 |
| AS-14 | Temporizador de procesos periódicos (conciliación diaria y sincronización) | Existencias, ventas, cartera de crédito | Interno | FEP03 diap. 31, decisión 5. Propuesta del 2026-10-08 |

El centro de distribución de Concepción (código AS-06) no es actor sistema. EXC-13 excluye instalar componentes allí, SP-02 lo mantiene con planillas y RC-10 hace que el cliente entregue sus existencias al Servicio de existencias. Esa entrega es un caso de uso de AH-07.

## 4. Equivalencias de nombres (para resolver)

| Concepto | sd-02 | sd-03 | Nombre canónico propuesto |
| :-- | :-- | :-- | :-- |
| Control interno y cumplimiento regulatorio | «Contraloría» | «Cumplimiento» | Contraloría y Cumplimiento (el Caso muestra una sola persona con ambos cargos) |
| Dirección | Directorio, Gerencia General | «la dirección» | Dirección (Directorio y Gerencia General) |
| Negocio financiero | «Negocio Financiero» | «Emisor» y «Negocio Financiero» | Filial emisora, para la entidad. Negocio financiero, para el área funcional |
| Operación de tienda | Un solo grupo | Vendedores, cajeros, jefaturas, repositores | Se abre en AH-03 a AH-08 |
| Prevención de pérdidas | Actor de alta influencia | Una mención | Prevención de pérdidas |
| Autoridades | Tres autoridades | «Organismos fiscalizadores» | Autoridades fiscalizadoras (financiera, protección al consumidor y tributaria) |

## 5. Vacíos y contradicciones detectados

1. El personal de los centros de distribución (620 personas) no tiene grupo en la Tabla 2.5.
2. El administrador de sistemas (TI) no aparece como rol de administración en ningún subdocumento. La clase advierte que olvidar los casos de administración subestima entre 10 % y 20 % (FEP03, diap. 33).
3. Los repositores externos están en la matriz (2.4.2) pero no en la Tabla 2.5.
4. El sd-02 nombra a los entrevistados por su nombre (2.4.3). El maestro usa solo roles.
5. El tipo de interfaz de cada sistema (AS-01 a AS-12) no está documentado: depende del mapa de las 14 interfaces, que el Caso dice que nadie posee.
6. Recuento de plataformas: resuelto el 2026-10-08. Son nueve (ocho sistemas y las planillas y listas impresas como novena, decisión DEC-10). La sección 3.3.1 de `sd-03.tex` se alineó con la 3.2.1 y el sd-02.
7. Las equivalencias de la sección 4 no se aplican a los `.tex`. El equipo decide en cuál de los dos subdocumentos se corrige cada diferencia.

## 6. Pendientes de validación
- Nombres canónicos de la sección 4 (equipo).
- Cargos funcionales por validar: AH-09, AH-10, AH-13.
- Convención de interfaz de los sistemas (puerta G1) y tipo de cada uno (puerta G2).
- Si las autoridades fiscalizadoras y el vendedor de marketplace son actores del sistema o solo destinatarios de reportes.
