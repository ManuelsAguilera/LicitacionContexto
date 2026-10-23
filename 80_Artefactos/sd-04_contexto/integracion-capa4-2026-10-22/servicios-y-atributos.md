# Servicios y atributos

Trece servicios vigentes y un candidato. A/C/E/P son responsabilidades de diseño propuestas: auditoría, control de acceso, exportación y parámetros. Las tablas del adjunto describen estados documentales anteriores; no se revalida el T-12 ni se afirma cumplimiento implementado.

| Servicio | Responsabilidad / despliegue | Tratamiento A/C/E/P |
|---|---|---|
| R:M-01 | Oferta comercial · Artículos, precios y promociones · E1 · despliegue por decidir | Patrón propuesto; ver brechas específicas del adjunto §4.2–4.5 |
| R:M-02 | Abastecimiento · Órdenes, transferencias y recepción · E2 · microservicio | Patrón propuesto; ver brechas específicas del adjunto §4.2–4.5 |
| R:M-03 | Existencias · Movimientos, reservas y disponible · E1 · microservicio | Patrón propuesto; ver brechas específicas del adjunto §4.2–4.5 |
| R:V-01 | Pedidos · Promesa, asignación y estado único · E2 · microservicio | Patrón propuesto; ver brechas específicas del adjunto §4.2–4.5 |
| R:V-02 | Ventas · Venta, pago, reversa y conciliación · E1 · microservicio | Patrón propuesto; ver brechas específicas del adjunto §4.2–4.5 |
| R:V-03 | Comisiones · Regla y base de atribución · E2 · módulo extraíble | Patrón propuesto; ver brechas específicas del adjunto §4.2–4.5 |
| R:V-04 | Marketplace · Reglas de vendedores y coordinación · E2 · módulo extraíble | Patrón propuesto; ver brechas específicas del adjunto §4.2–4.5 |
| R:CL-01 | Posventa · Caso, inspección y destino de devolución · E2 · microservicio | Patrón propuesto; ver brechas específicas del adjunto §4.2–4.5 |
| R:CL-02 | Clientes Retail · Identificación, preferencias y fidelización · E2 · microservicio | Patrón propuesto; ver brechas específicas del adjunto §4.2–4.5 |
| F:C-01 | Originación de crédito · Solicitud, evaluación, cupo y autorización · E1 · microservicio | Patrón propuesto; ver brechas específicas del adjunto §4.2–4.5 |
| F:C-02 | Cartera de crédito · Cuenta, saldo, pago, mora y cobranza · E1/E2 · microservicio | Patrón propuesto; ver brechas específicas del adjunto §4.2–4.5 |
| F:C-03 | Evidencia financiera · Precontrato, aceptación, firma y expediente · E1 · microservicio | Patrón propuesto; ver brechas específicas del adjunto §4.2–4.5 |
| X-01 | Control de cruces | Patrón propuesto; ver brechas específicas del adjunto §4.2–4.5 |
| F:C-04 | Control regulatorio · CANDIDATO · Reportes y prevención de lavado · Alcance, RF y etapa por aprobar | Candidato: definición y aprobación pendientes |

## Reglas de integración

Auditoría: cambio de entidad con identidad, instante/zona, origen, antes/después y correlación; lecturas sensibles registradas; sellado/exportación inmutable por diseñar y probar. Control de acceso: RBAC/ABAC propio por servicio y ámbito, segregación financiera, filtro por tienda/vendedor/titular y sesión nominativa; acceso offline pendiente. Exportación: filtro y permisos preservados, trabajos grandes asíncronos con auditoría y aviso, sin consultas analíticas sobre transaccional. Parámetros: repositorios propios, versionado, segundo perfil para impacto operacional y simulación; no inventar parámetros donde todavía no están definidos.

La figura no afirma que trece bases separadas sean trece servidores físicos. La agrupación de repositorios y el despliegue de módulos se refinan en arquitectura física sin cambiar autoridades. Las cinco innovaciones conservan su servicio responsable. El maestro de tiendas/cajas/unidades no recibe un dueño por inferencia.

## Brechas materiales conservadas

- Abastecimiento y Comisiones: completitud funcional por ampliar; no se reemplaza WMS ni remuneraciones.
- Clientes: RF-227–RF-231 siguen como propuesta v3.1, no catálogo oficial vigente.
- Cartera: imputación de pagos, retracto y gastos de cobranza requieren definición; no se declaran cubiertos al cambiar una etiqueta.
- Firma Retail: recepción/devolución con dueño de negocio propio; proveedor y contratos por verificar.
- F:C-04: regulación, RF, etapa, custodia y contratos no aprobados; sin conexiones operacionales inventadas.
- Administración: maestro de ubicaciones/unidades y matrices de roles pendientes.
- Notificaciones: tres canales, plantillas/preferencias y trazabilidad propuestos; proveedor y evidencia de entrega por validar.
- Búsqueda global: permisos/facetas/tolerancia pendientes de producto y pruebas; pgvector del catálogo no acredita cobertura global.
