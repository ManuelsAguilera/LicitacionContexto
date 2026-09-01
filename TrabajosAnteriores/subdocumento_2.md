# SUBDOCUMENTO 2

## 3 Alcance del Servicio

### 3.1 Definición del alcance

**3.1.1 Contexto actual**
La empresa DistriProducto se enfoca en el negocio de las bodegas, creada hace varios años, la cual se ha mantenido a lo largo del tiempo realizando sus operaciones de manera manual. Esto ha generado un uso excesivo de tiempo en tareas administrativas y operativas, lo que también ha provocado demoras y dificultades para responder a las crecientes demandas del mercado.

**3.1.2 Problema que busca resolver**
Baja productividad en bodega, procesos lentos y poco eficientes, mala utilización del espacio. Gestión de transporte ineficiente, sin visibilidad en tiempo real. Servicio al cliente lento y con errores frecuentes. Todo esto impacta financieramente a la empresa con altos costos operativos y problemas de cumplimiento normativo.

**3.1.3 Objetivos**
* **General:** Transformar digitalmente las operaciones logísticas de Distriproducto, logrando mayor eficiencia, trazabilidad y calidad de servicio.
* **Específicos:** Implementar WMS, optimizar transporte (TMS), fortalecer trazabilidad de inventario, digitalizar RRHH, implementar portal B2B, implementar control de acceso y seguridad, desarrollar infraestructura escalable en la nube y fomentar sostenibilidad.

**3.1.4 Entregables / Módulos**
* **Hitos Etapa 1:** Kick-off (H1), Diseño aprobado (H2), Ambiente de desarrollo operativo (H3), Módulos core (H4), Infraestructura instalada (H5), Sistema integrado (H6), Usuarios capacitados (H7), Piloto exitoso (H8).
* **Hitos Etapa 2:** 50% ubicaciones en producción (H9), 100% ubicaciones operativas (H10), Proyecto cerrado exitosamente (H11).
* **Módulos:** WMS, Inventario, TMS, Clientes (B2B), RRHH, Seguridad, Administrativo y BI.

**3.1.6 Ventajas y desventajas**
| Ventajas | Desventajas |
| :--- | :--- |
| Incremento de productividad en bodega y transporte | Inversión inicial alta en infraestructura |
| Reducción de costos operativos | Resistencia al cambio |
| Trazabilidad completa de inventarios | Dependencia tecnológica |
| Mayor puntualidad en entregas | Necesidad de gestión de seguridad informática |

### 3.2 Implementación
Metodología híbrida: Cascada para la gestión del proyecto (PMBOK) y desarrollo Ágil (Scrum) para el software. 
* **Fases:** Inicio y planificación, Análisis y diseño, Desarrollo iterativo, Integración y validación, Implementación y migración, Capacitación, Estabilización y cierre.

### 3.4 Operación
* **SLA:** 99.97% en módulos críticos.
* **RTO:** < 1 hora.
* **RPO:** <= 15 minutos.

### Anexo A.1 Listado de Requerimientos Funcionales
* **Gestión de Sesiones:** Autenticación IAM, MFA obligatorio, TLS 1.3, bloqueo por intentos fallidos.
* **WMS:** Procesamiento de ASN, captura RFID, slotting dinámico, picking guiado (AR y voz), validación final antes de despacho.
* **TMS:** Optimización automática multi-criterio, seguimiento GPS en tiempo real, scoring de conducción.
* **YMS:** Control de muelles, asignación de turnos, check-in/check-out.
* **Seguridad:** Control de acceso biométrico, lectura de patentes (LPR), CCTV.
* **RRHH:** Control de turnos, asistencia biométrica.
* **ERP y B2B:** Facturación electrónica, portal B2B para clientes y proveedores, inteligencia de negocios (BI).