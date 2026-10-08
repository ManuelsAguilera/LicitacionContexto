# Actores y UAW de la estimación por Puntos de Casos de Uso (puertas G2a y G2)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: aprobado en conversación con el usuario, pendiente de la firma del equipo. Parte de `80_Artefactos/maestro_actores.md` y aplica las convenciones C5, C6 y C9 de `01_reglas_de_conteo.md`. Tipos (FEP03, diap. 26): 1 sistema por interfaz de programación (peso 1), 2 sistema por protocolo o archivo (peso 2), 3 persona con interfaz gráfica (peso 3). Los actores son roles, no personas.

## 1. Personas

| Código | Actor | Tipo | Justificación |
| :-- | :-- | :-- | :-- |
| AH-01 | Cliente | 3 | Usa la interfaz gráfica de los canales y del mesón |
| AH-02 | Titular de tarjeta | 3 | Acepta información y condiciones en pantalla |
| AH-03 | Vendedor de piso | 3 | Consulta disponibilidad y ofrece la tarjeta en terminal |
| AH-04 | Cajero | 3 | Opera el punto de venta |
| AH-05 | Jefatura de tienda o de departamento | 3 | Gestiona conteos, merma y exhibición en pantalla |
| AH-06 | Personal de reposición y bodega de tienda | 3 | Registra conteos y cambios de etiqueta en terminal |
| AH-07 | Personal de centros de distribución | 3 | Prepara pedidos y carga las existencias de Concepción (RC-10) |
| AH-08 | Repositor externo de proveedor | 3 | Accede individualizado a las funciones que le corresponden (RS-12) |
| AH-09 | Ejecutivo de atención y posventa | 3 | Abre y resuelve casos en pantalla |
| AH-10 | Ejecutivo del negocio financiero | 3 | Gestiona repactación y cobranza en pantalla |
| AH-11 | Comercial y compras | 3 | Define precios, promociones y campañas en pantalla |
| AH-12 | Planificación de abastecimiento | 3 | Revisa propuestas de reposición en pantalla |
| AH-13 | Canales digitales y Marketing | 3 | Gestiona marketplace, segmentos y campañas en pantalla |
| AH-14 | Prevención de pérdidas | 3 | Confirma causas de diferencia en pantalla |
| AH-15 | Contraloría y Cumplimiento | 3 | Audita registros y aprueba fichas de cruce en pantalla |
| AH-16 | Administrador de sistemas (TI) | 3 | Administra identidades, accesos y observabilidad. Cubre los casos de administración (C9) |
| AH-17 | Vendedor de marketplace (externo) | 1 | Declara existencia y recibe avisos por interfaz de programación. Decisión del usuario, 2026-10-08 |
| AH-18 | Analista de información | 3 | Usa los tableros de autoservicio (sd-03 3.3.2). Propuesta |

## 2. Sistemas

| Código | Actor | Tipo | Justificación |
| :-- | :-- | :-- | :-- |
| AS-01 | Sistema de gestión empresarial y facturación (ERP/DTE) | 1 | Se mantiene e integra (EXC-01). Interfaz objetivo (C5) |
| AS-02 | Sistema de gestión de almacenes principal (WMS) | 1 | Se mantiene e integra (EXC-12). Interfaz objetivo |
| AS-03 | Plataforma de marketplace | 1 | Se mantiene e integra (EXC-04, EXC-12). Interfaz objetivo |
| AS-04 | Plataforma de comercio electrónico | 1 | Se evalúa e integra (EXC-15). Interfaz objetivo |
| AS-05 | Sistema de fidelización | 1 | Se evalúa e integra (EXC-15). Interfaz objetivo |
| AS-07 | Transportistas de última milla | 1 | Se integran (EXC-07). Interfaz objetivo |
| AS-08 | Medios y terminales de pago | 1 | Integración por procesador, por confirmar. Interfaz objetivo |
| AS-09 | Sistema central de retail (2009) | 2 | En retiro, no ofrece interfaz de programación. Solo interfaces de convivencia |
| AS-10 | Plataforma de originación y cobranza (2011) | 2 | En retiro, opera por archivo. Solo interfaces de convivencia |
| AS-11 | Sistema de remuneraciones (módulo del ERP) | 1 | Conector para entregar la base de comisión (EXC-05). Interfaz objetivo |
| AS-12 | Autoridades fiscalizadoras | 2 | Reciben reportes por archivo o portal, sin interfaz de programación |
| AS-13 | Proveedores de mercadería | 2 | Intercambian órdenes y avisos. Canal por validar. Propuesta |
| AS-14 | Temporizador de procesos periódicos | 1 | Dispara la conciliación diaria y la sincronización. Actor simple declarado (diap. 31, decisión 5). Propuesta |

Fuera de la lista. El centro de distribución de Concepción no es actor sistema (EXC-13, SP-02, RC-10). Su entrega de existencias es un caso de uso de AH-07. Tampoco son actores los roles de gobierno del proyecto (Contraparte Técnica, Comité Ejecutivo), los grupos de propiedad y el directorio de usuarios del cliente (ninguna fuente lo nombra).

## 3. Cálculo del UAW

| Tipo | Actores | Peso | Subtotal |
| :-- | --: | --: | --: |
| 3 (persona con interfaz gráfica) | 17 | 3 | 51 |
| 2 (sistema por protocolo o archivo) | 4 | 2 | 8 |
| 1 (sistema por interfaz de programación) | 10 | 1 | 10 |
| **Total** | **31** | | **UAW = 69** |

Los 10 de tipo 1 son AH-17 y los sistemas AS-01 a AS-05, AS-07, AS-08, AS-11 y AS-14.

## 4. Sensibilidad (propuesta)

| Escenario | UAW |
| :-- | --: |
| Base | 69 |
| Los 8 sistemas externos de tipo 1 (AS-01 a AS-05, AS-07, AS-08, AS-11) pasan a tipo 2, por el archivo actual (C5) | 77 |
| Se retira AS-13 si el equipo no lo valida | 67 |
| Se agrega el directorio de usuarios del cliente (tipo 1 o 2) | 70 a 71 |

## 5. Pruebas de la puerta G2a

`python3 05_Gestion/scripts/verificar_actores.py` informa 0 hallazgos. Para P2a.3 se unificó «Contraloría y Cumplimiento» en el sd-02 (Tabla 2.5) y en el sd-03 (3.4.6). Para P2a.4 se asignó AH-07 al grupo Negocios y operación (Logística) y se aclaró en la Tabla 2.5 del sd-02, sin agregar un grupo nuevo, para no inventar influencia ni interés.

## 6. Preguntas para el equipo

1. ¿Se firma que AH-17 es tipo 1?
2. ¿Se firman AH-18, AS-13 y AS-14 como actores?
3. ¿Los sistemas de 2009 y 2011 cuentan como tipo 2 solo por sus interfaces de convivencia?
4. ¿Se firma que el directorio de usuarios del cliente queda fuera hasta que el sd-04 defina la federación de identidades?
5. ¿Concepción está dentro de las 620 personas de AH-07? (supuesto)
