# SUBDOCUMENTO 3

## 4 Descripción Lógica de la Solución

### 4.1 Descripción de solución
La solución tecnológica se basa en una arquitectura de micro-servicios, diseñada para mejorar la coordinación entre áreas críticas (almacenamiento, transporte, seguridad, comercial y atención al cliente). Se divide en los siguientes módulos principales:

* **Módulo WMS:** Centraliza la operación interna (recepción, almacenamiento, pedidos, despacho y devoluciones).
* **Módulo TMS:** Gestiona planificación, asignación y monitoreo de transporte.
* **Módulo YMS:** Coordina la gestión de patios, andenes y citas.
* **Módulo de Seguridad:** Integra control de acceso biométrico, cámaras y monitoreo.
* **Módulo de RRHH:** Administra información del personal (turnos, asistencia).
* **Módulo ERP:** Consolida información administrativa y financiera.
* **Módulo Portal B2B:** Facilita la comunicación con clientes y proveedores.

### 4.2 Arquitectura Lógica
La arquitectura sigue lineamientos de TOGAF y se organiza en seis capas principales para asegurar escalabilidad, resiliencia y separación de responsabilidades:

**4.2.1 Capa Cliente**
Punto de contacto directo con los usuarios (operarios, choferes, administrativos, clientes, etc.) a través de dispositivos móviles, handhelds, y PCs.

**4.2.2 Capa de Presentación**
Interfaces desarrolladas con React Native y Expo. Provee los portales de WMS, TMS, Seguridad, RRHH y B2B, cumpliendo estándares WCAG AA.

**4.2.3 Capa Edge**
Opera en el límite entre infraestructura local y la nube. Garantiza autonomía operativa local por 72 horas sin conexión mediante nodos locales, AWS IoT Core y AWS DataSync.

**4.2.4 Capa de Negocio**
Núcleo lógico estructurado en microservicios (Domain-Driven Design). Usa API Gateway y colas de mensajería para orquestar los procesos logísticos y administrativos.

**4.2.5 Capa de Datos**
Modelo híbrido: PostgreSQL para OLTP (local/RDS), Amazon Redshift para OLAP, MongoDB y Amazon Timestream para NoSQL/IoT. 

**4.2.6 Capa Transversal**
Servicios de soporte, seguridad y auditoría (AWS IAM, AWS Shield, WAF, CloudTrail). Garantiza gobernanza tecnológica y alta disponibilidad (99.97%).
