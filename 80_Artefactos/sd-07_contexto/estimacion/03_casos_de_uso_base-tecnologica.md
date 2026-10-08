# Casos de uso de la base tecnológica (BT), puerta G3

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta aprobada por el usuario el 2026-10-08, pendiente de la firma del equipo. Prefijo de casos: BT (base tecnológica: identidad y accesos, degradación y congelamiento, integración, observabilidad y capacidad analítica). Reglas: `01_reglas_de_conteo.md`. Actores: `02_actores_uaw.md`. Alcance: sd-03 3.3.1, 3.3.2 y 3.4.4, Anexo A y Anexo B (19 RF de la base, Etapa 1). Las transacciones que el sd-03 no describe son propuestas y se declaran en la columna de supuestos.

## 1. Casos de uso

| Código | Servicio | Caso de uso (objetivo del actor) | Actor principal | Trans. | Origen | Supuestos de flujo |
| :-- | :-- | :-- | :-- | --: | :-- | :-- |
| CU-BT-01 | BT | Ingresar a una terminal compartida con identidad individual | AH-04 | 3 | RF-002 a RF-006 | |
| CU-BT-02 | BT | Habilitar y revocar funciones según la capacitación normativa | AH-16 | 3 | RF-007 a RF-009 | S5, S10 |
| CU-BT-03 | BT | Patrocinar el acceso temporal de un repositor externo | AS-13 | 3 | RF-010, RF-011 | S3, S10 |
| CU-BT-04 | BT | Operar como repositor externo con identidad individualizada | AH-08 | 2 | RF-012 | S3 |
| CU-BT-05 | BT | Retirar los accesos al término del vínculo | AH-16 | 2 | RF-013 | |
| CU-BT-06 | BT | Conciliar los accesos contra la nómina activa | AS-14 | 2 | RF-014, RF-015 | S2, S4 |
| CU-BT-07 | BT | Declarar el orden y los criterios de degradación | AH-16 | 2 | RF-177, RF-178 | S6 |
| CU-BT-08 | BT | Parametrizar las ventanas de congelamiento y bloquear intervenciones | AH-16 | 3 | RF-184 a RF-186 | |
| CU-BT-09 | BT | Convivir con el sistema central de 2009 | AS-09 | 3 | 3.3.1; 3.4.4 | S1, S7 |
| CU-BT-10 | BT | Administrar la plataforma de integración | AH-16 | 3 | 3.3.2 | S1 |
| CU-BT-11 | BT | Observar la operación y atender alertas | AH-16 | 3 | 3.3.2 | S1 |
| CU-BT-12 | BT | Administrar identidades, roles y ámbitos | AH-16 | 3 | 3.3.2 | S1, S8 |
| CU-BT-13 | BT | Consultar tableros y exportar informes por ámbito | AH-18 | 3 | 3.3.2 | S1 |

Resumen. 13 casos, todos simples (1 a 3 transacciones). UUCW provisional del servicio = 13 × 5 = 65.

## 2. Transacciones contadas

| Código | Transacciones (idas y vueltas completas) |
| :-- | :-- |
| CU-BT-01 | T1 autenticar con credencial individual, con rechazo del acceso anónimo y de la credencial compartida. T2 traspasar la sesión nominativa entre usuarios. T3 cerrar la sesión por inactividad |
| CU-BT-02 | T1 registrar la acreditación de capacitación y su vigencia. T2 ejecutar originación o repactación y recibir el rechazo si la acreditación falta o venció. T3 revocar la habilitación al vencer la acreditación |
| CU-BT-03 | T1 patrocinar la habilitación con fecha de término. T2 consultar o retirar el patrocinio. T3 caducar la habilitación al cumplirse la vigencia |
| CU-BT-04 | T1 ingresar con la habilitación vigente, con rechazo si caducó. T2 operar las funciones permitidas con registro individual |
| CU-BT-05 | T1 revocar la totalidad de los accesos y credenciales al término del vínculo. T2 consultar el comprobante de revocación |
| CU-BT-06 | T1 conciliar los accesos vigentes contra la nómina activa. T2 informar al oficial de seguridad los accesos huérfanos |
| CU-BT-07 | T1 declarar el orden de degradación de los servicios. T2 parametrizar los criterios de cada nivel |
| CU-BT-08 | T1 parametrizar las cinco ventanas de congelamiento. T2 intentar un despliegue en ventana y recibir el bloqueo. T3 consultar los intentos bloqueados, con componente, solicitante e instante |
| CU-BT-09 | T1 recibir los datos del sistema de 2009. T2 enviar las operaciones nuevas durante la convivencia. T3 ejecutar el retorno ensayado |
| CU-BT-10 | T1 registrar o versionar el contrato de una interfaz. T2 consultar el envío y su resultado. T3 reprocesar los envíos fallidos |
| CU-BT-11 | T1 consultar el tablero de observabilidad. T2 configurar umbrales de alerta. T3 reconocer y cerrar una alerta |
| CU-BT-12 | T1 definir un rol y sus permisos por ámbito. T2 asignar roles a un usuario. T3 consultar los permisos efectivos |
| CU-BT-13 | T1 consultar un tablero del ámbito. T2 exportar o programar el envío, con rechazo si el conjunto mezcla Retail y Emisor. T3 solicitar la incorporación de un conjunto con ambos ámbitos, que exige aprobación de cruces (la aprobación está en CU-CC-06) |

## 3. Supuestos de flujo (propuestas, salvo indicación)

| ID | Supuesto |
| :-- | :-- |
| S1 | CU-BT-09 a CU-BT-13 no tienen RF. Sus transacciones son propuestas, apoyadas en 3.3.1, 3.3.2 y 3.4.4 |
| S2 | El «oficial de seguridad» de RF-015 se mapea a AH-16 |
| S3 | El patrocinador del repositor (RF-010) es el proveedor. Entra como AS-13, tipo 2, porque el canal sigue por validar en el sd-04 |
| S4 | La nómina de RF-014 viene de AS-11, que no es el actor principal de ese caso |
| S5 | CU-BT-02 usa solo la capacitación registrada. Dictar la capacitación queda fuera del caso, a cargo del cliente (RC) |
| S6 | El orden de degradación lo declara la base. Los RF que lo ejecutan (RF-179, RF-183) están en existencias, RF-180 en pedidos y RF-181 en ventas |
| S7 | CU-BT-09 es el único caso de convivencia con AS-09. No se repite en oferta comercial ni en existencias |
| S8 | La federación de identidades (D-01 de `contexto_sd-04.md`) no cambia los casos. La sensibilidad del UAW por directorio ya está registrada |
| S9 | Los resultados del Anexo D que tocan la base (accesos, congelamiento, observabilidad) se rastrean en la revisión de P3.3 al cerrar G3 |
| S10 | La tercera transacción de CU-BT-02 y de CU-BT-03 (revocación o caducidad automática, disparada por el temporizador) se cuenta porque devuelve un resultado verificable. Si el equipo no la cuenta, ambos casos bajan a 2 transacciones |

## 4. Cobertura de los 19 RF

RF-002 a RF-006 en CU-BT-01. RF-007 a RF-009 en CU-BT-02. RF-010 y RF-011 en CU-BT-03. RF-012 en CU-BT-04. RF-013 en CU-BT-05. RF-014 y RF-015 en CU-BT-06. RF-177 y RF-178 en CU-BT-07. RF-184, RF-185 y RF-186 en CU-BT-08. La comprobación mecánica la hace `05_Gestion/scripts/verificar_casos_uso.py`.

## 5. Decisiones del usuario (2026-10-08)

1. AS-13 patrocina el acceso del repositor (CU-BT-03).
2. AH-16 hace de oficial de seguridad.
3. La capacidad analítica (CU-BT-13) va en la base tecnológica.
4. Las terceras transacciones de CU-BT-02 y CU-BT-03 se cuentan (S10).
