# Glosario de nombres comunes (sd-01 a sd-04 y siguientes)

Resuelve EXT-B-01 de `auditoria_inconsistencias_sd01-04.md`. El Comunicado 10 pide que los nombres de componentes, módulos y servicios sean idénticos en todos los subdocumentos. Cuando un mismo objeto tiene un nombre formal y uno corto, la regla es: **nombre formal en la primera mención de cada subdocumento, nombre corto después, y nunca una tercera variante**. Fecha: 2026-10-11. Estado: borrador para el equipo.

## Plataformas actuales (Caso 09, capítulo 5)

| Objeto | Nombre formal (primera mención) | Nombre corto | No usar |
| :-- | :-- | :-- | :-- |
| Sistema de 2009 | sistema central de retail de 2009 | núcleo Retail (de 2009) | sistema central (a secas), núcleo de 2009 |
| Crédito de 2011 | plataforma de originación y cobranza de créditos de 2011 | plataforma de crédito de 2011; «crédito de 2011» solo en tablas y figuras | plataforma financiera, plataforma de 2011 (a secas) |
| Punto de venta de 2014 | punto de venta de tienda de 2014 | POS 2014 (el nuevo: POS nuevo) | caja (para el sistema) |
| Comercio electrónico de 2019 | plataforma de comercio electrónico de 2019 | comercio electrónico | canal digital (ver Pendientes) |
| Marketplace de 2022 | plataforma de marketplace de 2022 | marketplace | — |
| Gestión de almacenes de 2016 | sistema de gestión de almacenes del centro de distribución principal | WMS | — |
| Fidelización de 2017 | sistema de fidelización de 2017 | fidelización | — |
| Gestión empresarial | sistema de gestión empresarial y facturación | ERP/DTE (ERP en general) | — |
| Motor de precios y promociones | motor de precios y promociones | motor de precios | «novena plataforma» solo para referirse al Caso |

## Negocios, ámbitos y servicios

| Objeto | Regla |
| :-- | :-- |
| Filial emisora | La **entidad** jurídica que emite el crédito. Usar «filial emisora» (minúscula). «Filial financiera» no se usa. |
| Emisor | El **ámbito** de la solución (datos, identidades, redes y claves propios) que sirve a la filial emisora. Siempre con mayúscula. |
| Retail | El ámbito de la solución que sirve a la tienda. Con mayúscula. |
| Negocio financiero | La **línea de negocio** (originación, servicio, cobranza), no la entidad ni el ámbito. |
| Frente | Solo para los **tres frentes de la solución** (Retail, Filial emisora, Frontera) del sd-03 y sd-04. Los equipos de trabajo del sd-01 se llaman **áreas de trabajo**. |
| Área | Subdivisión de un frente (Mercadería, Venta, Relación con el cliente, Crédito). No confundir con las «áreas de trabajo» del equipo. |
| Servicio de control de cruces | Nombre del servicio; código X-01. No «servicio de control de cruces» y «Gestor de ...» alternados. |
| Servicios | Los trece servicios de la subsección 3.3.2. No se usan los códigos M-xx del sd-02 antiguo. |

## Sitios y zonas (sd-04)

SIT-01 (22 tiendas), CD-01 (centro de distribución principal), CD-02 (centro de distribución de Concepción), DC-01 (centro de datos de casa matriz), DC-02 (sala de respaldo), CLD-01 (Azure Chile Central), CLD-02 (Azure Brazil South), EXT-01 (contrapartes externas). No se usan «Site Principal», «Site Secundario» ni «Z1/Z2/Z3» fuera de la cita de las Bases Técnicas Transversales (capítulo 7, que habla de «site secundario»).

## Portales

| Nombre | Qué es |
| :-- | :-- |
| portal de proveedor | Portal para los proveedores propios (940). Componente por acreditar. |
| portal de vendedor | Portal de los vendedores de marketplace (310), parte de la plataforma de marketplace. |
| portal público | El portal sin autenticación de RT-16.30. |

Son tres objetos distintos. La auditoría los trató como una sola variante, pero no lo son.

## Evento anual

- **Nombre formal:** evento anual de comercio electrónico (Caso, núm. 4.12). Corto: evento anual.
- «Evento de junio» o «evento de junio de 2026» solo para el evento concreto de 2026 (cancelaciones, reclamos, SERNAC), nunca para el evento en general.
- Fecha: «entre mayo y junio», porque la fija un tercero. Cifra de pedidos: 104.000 en tres días.

## Actores del contrato

| Término | Uso |
| :-- | :-- |
| Multitiendas Ancoa S.A. / Ancoa | La empresa. |
| Cliente (CLIENTE en las Bases) | Parte del contrato, en la ejecución y en la operación. |
| mandante | Solo en el proceso de licitación (consultas, aclaraciones, Bases). |
| Contraparte Técnica | Rol del Cliente que valida y firma actas. |
| Comité Ejecutivo | Instancia que aprueba cambios (art. 72). |
| proponente / OSS | Only Simple Solutions; «ADJUDICATARIO» solo al citar las Bases. |
| Jefe de Proyecto | Singular, un solo rol. No «Jefe de Proyectos». |

## Otros

| Término | Regla |
| :-- | :-- |
| tarjeta propia | La tarjeta de la casa comercial. «Tarjeta de casa comercial» solo al citar la regulación. |
| punto de venta / POS | «Punto de venta» en prosa de negocio; «POS» para el sistema y sus periféricos. |
| centro de distribución de Concepción | CD-02 en el sd-04; «el centro de Concepción» como forma corta. |
| catálogo de requerimientos | Versión vigente 3.1 (308 elementos). El sd-02 describe el recibido (3.0). |
| exclusiones, supuestos, restricciones | EXC-nn, SP-nn y SUP-nn, RS-nn (ver sd-02 A.5 y sd-03 Anexo A). |

## Pendientes

- **«Canal digital».** Nombre provisional del servicio que cubre el comercio electrónico vigente (M-11 de la matriz antigua). Hay que fijarlo cuando se defina el destino del comercio electrónico en la Etapa 1.
- Los subdocumentos sd-05 en adelante deben seguir este glosario al redactarse.
