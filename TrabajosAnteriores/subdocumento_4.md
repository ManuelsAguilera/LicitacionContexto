# SUBDOCUMENTO 4

## 5 Descripción Física de la Solución

### 5.1 Arquitectura Física de la Solución
Arquitectura híbrida que combina infraestructura on-premise (Data Center local, patios, bodegas) con una VPC en AWS. Se utiliza VPN site-to-site y AWS Direct Connect + AWS Cloud WAN para interconexión segura.

**5.1.2 Segmentación de Arquitectura**
La red se divide en zonas aisladas (VLAN/VRF, firewalls) para aplicar principios de mínimo privilegio:
* Flotas de camiones (externos e internos)
* Zona de seguridad / Patio
* Zona de Bodega Pallets y Productos
* Zona Edge (procesamiento cercano a scanners 3D, AGV)
* Zona de RRHH / Administrativo
* Portal B2B (DMZ lógica)
* Zona de Datos (On-premise y Cloud)

**5.1.3 Zona de Datos (On-Premise)**
Data Center primario con redundancia N+1. 
* Servidores: Dell PowerEdge XR5610 y XR7620 (Rugged).
* Switching: TP-Link JetStream (Core 10G, Acceso PoE+).
* Seguridad: Fortinet FortiGate 100F (HA).
* Energía: UPS 10kVA y generadores para 72h de autonomía.

**5.1.6 Zona de Datos (Cloud) - Región Dividida**
* **São Paulo (Baja Latencia):** Subredes públicas y de aplicación (AWS Lambda, ECS Fargate), Base de datos transaccional (RDS PostgreSQL Multi-AZ), Caché (ElastiCache).
* **N. Virginia (Analítica/Almacenamiento masivo):** Data Lake (Amazon S3), Data Warehouse (Amazon Redshift), Procesamiento ETL (AWS Glue). Aprovecha menores costos para cargas pesadas no sensibles a latencia.

**5.1.7 Especificaciones Tecnológicas de Software**
* **Sistema Operativo:** SUSE Linux Enterprise Server (SLES) 15.
* **Frontend:** Amazon CloudFront + S3 (React/Next.js).
* **Backend:** AWS Lambda, Amazon ECS Fargate, Amazon API Gateway.
* **Seguridad:** AWS IAM, WAF, Shield, GuardDuty, Cognito.
* **CI/CD:** AWS CodeCommit, CodeBuild, CodePipeline, CodeDeploy. Terraform / CloudFormation para IaC.
* **Monitoreo:** Amazon CloudWatch, AWS CloudTrail, Zabbix.
