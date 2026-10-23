"""Construye las tres especificaciones L2 desde los registros del 22-10."""
import copy,hashlib,json
from pathlib import Path

ROOT=Path.cwd();OUT=ROOT/'04_Adjuntos/diagramas';REPORT=ROOT/'80_Artefactos/sd-04_contexto/actualizacion-datos-transversales-2026-10-22'
REPORT.mkdir(parents=True,exist_ok=True)
BASE=json.loads((OUT/'diag-04-31_arquitectura-servicios-y-flujos.json').read_text(encoding='utf-8'))
SOURCES=['80_Artefactos/sd-04_contexto/capa-datos_decisiones-y-precisiones_2026-10-22.md','80_Artefactos/sd-04_contexto/capas-07-08_cambios-y-conexiones_2026-10-22.md']
protected=list((ROOT/'02_Propuesta/latex_final').rglob('*.tex'))+[ROOT/p for p in SOURCES]
if not (REPORT/'hashes-antes.json').exists(): (REPORT/'hashes-antes.json').write_text(json.dumps({str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in protected},indent=2),encoding='utf-8')
def edge(s,a,b,sem,label):s['enlaces'].append(dict(de=a,a=b,semantica=sem,etiqueta=label))
def node(s,id,label,tipo,group,**kw):
 n=dict(id=id,etiqueta=label,tipo=tipo,grupo=group,**kw);s['nodos'].append(n);return n
def new(fig,title):
 return dict(estilo='L2',composicion='bandas_horizontales',figura=fig,titulo=title,fuente='Fuente: elaboración propia a partir de los registros de Datos y capas 7–8 del 22-10-2026, figura 4.31 y especificación de capa 4; diseño propuesto, sin acreditación de despliegue.',grupos=copy.deepcopy(BASE['grupos']),nodos=[],enlaces=[],notas=[])
def save(s,stem):
 (OUT/(stem+'.json')).write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(stem,len(s['nodos']),len(s['enlaces']))

s=copy.deepcopy(BASE);s.update(figura='4.33',titulo='Arquitectura lógica por capas · datos y capacidades transversales',fuente=new('','')['fuente'])
old={'entra','externalid','kv','sentinel','privado','otel','monitor','grafana','rum'}
s['nodos']=[n for n in s['nodos'] if n['id'] not in old]
s['enlaces']=[e for e in s['enlaces'] if e['de'] not in old and e['a'] not in old]
by={n['id']:n for n in s['nodos']}
changes={
 'datos_orig':('PostgreSQL · Filial\nOriginación: evaluación, cupo y autorización',None),
 'datos_cartera':('PostgreSQL · Filial\nCartera: cuentas y saldos',None),
 'datos_evid':('Azure Blob Storage · Filial\nDocumentos de evidencia vigentes',None),
 'archivo_r':('Azure Blob Storage WORM · Retail\nArchivo y evidencia retenida',None),
 'archivo_e':('Azure Blob Storage WORM · Filial\nArchivo y evidencia retenida',None),
 'proy_r':('Java / Spring en AKS · Retail\nIngesta, proyecciones y representaciones',None),
 'proy_e':('Java / Spring en AKS · Filial\nIngesta, proyecciones y conciliación',None),
 'search_r':('OpenSearch · Retail\nBúsqueda global · API propia y filtros','opensearch'),
 'search_e':('OpenSearch · Filial\nBúsqueda global · API propia y filtros','opensearch'),
 'powerbi':('Microsoft Power BI\nModelos y permisos separados por ámbito\nConsulta exclusiva de PostgreSQL analítico',None),
 'vector':('PostgreSQL / pgvector · Oferta\nÍndice multimodal reconstruible',None),
 'cupo_local':('Cupo preautorizado sin enlace\nAsignación exclusiva · caducidad pendiente',None),
 'operacion':('App interna de tienda\n4 perfiles · RN / SQLite / DataWedge\nQR + PIN: un factor',None),
}
for id,(label,tipo) in changes.items():
 by[id]['etiqueta']=label
 if tipo:by[id]['tipo']=tipo;by[id].pop('estado',None)
for id in ['mart_r','mart_e','vector']:
 by[id].pop('estado',None)
by['datos_orig']['descripcion']='F:C-01 es autoridad de evaluación, cupo y autorización. F:C-02 conserva cuentas y saldos; contrato atómico de reserva/consumo por definir, sin doble autoridad.'
node(s,'evid_meta','PostgreSQL · Filial\nC-03: metadatos de evidencia','base_datos','datos_e',descripcion='Expediente y metadatos de documentos separados de Originación. Completar acto exige carga, verificación y conciliación con Blob.')
node(s,'lake_r','ADLS Gen2 · Retail\nLanding, curados y conjuntos versionados','lago_analitica','datos_r')
node(s,'lake_e','ADLS Gen2 · Filial\nLanding y curados autorizados','lago_analitica','datos_e')
node(s,'adf','Azure Data Factory\nCargas y dependencias por ámbito','data_factory','tecnologias')
node(s,'metadata','OpenMetadata\nCatálogo, linaje y calidad\nInstancias propias por ámbito','openmetadata','tecnologias')
node(s,'mlflow','MLflow · Retail\nExperimentos y versiones de modelos','mlflow','datos_r')
node(s,'training','Python / scikit-learn en AKS\nConteo: entrenamiento e inferencia','python','datos_r')
node(s,'backup','Azure Backup / PostgreSQL PITR\nCobertura y restauración por recurso','backup_vault','tecnologias')
node(s,'security_summary','7 · Seguridad\nEntra ID P2 · External ID · Intune · Workload Identity\nKey Vault · Managed HSM · PIM · Bastion · Private Access\nDefender for Endpoint / Cloud · Sentinel\nInstancias y permisos por ámbito · detalle: página 3','identidad','seguridad',descripcion='Resumen de productos desglosados en la vista 4.35. Instancias y permisos propios por ámbito; no representa un servicio adicional ni una instancia compartida.')
node(s,'observability_summary','8 · Observabilidad\nOpenTelemetry Collector · Prometheus · Loki · Tempo\nGrafana autogestionado / Alerting · Blackbox Exporter\nAzure Monitor / Log Analytics · colas locales 24 h\nInstancias y permisos por ámbito · detalle: página 3','otel_logo','observabilidad',descripcion='Resumen de productos desglosados en la vista 4.35. No es un colector común de ambos negocios.')
# Retirar flujos de entrenamiento/archivo y consultas ambiguas de la versión anterior.
drop={('proy_r','archivo_r'),('archivo_r','area_mercaderia'),('area_mercaderia','vector'),('mart_r','powerbi'),('mart_e','powerbi'),('api_management','search_r'),('api_management','search_e')}
s['enlaces']=[e for e in s['enlaces'] if (e['de'],e['a']) not in drop]
for e in s['enlaces']:
 if (e['de'],e['a'])==('servicios_e','datos_orig'):e['etiqueta']='Solo Originación F:C-01: repositorio propio de evaluación, cupo y autorización; sin metadatos de C-03.'
edge(s,'servicios_e','evid_meta','persistencia','Solo C-03: expediente y metadatos propios; no datos de Originación.')
for d in ['r','e']:
 edge(s,'adf','lake_'+d,'politica','Solo factory del ámbito: coordina cargas iniciales e incrementales autorizadas, punto de corte y manifiestos; no movimiento entre negocios.')
 edge(s,'proy_'+d,'lake_'+d,'persistencia','Trabajadores propios escriben únicamente conjuntos autorizados; no duplicar todos los hechos por defecto.')
 edge(s,'lake_'+d,'proy_'+d,'flujo','Lectura y validación de conjuntos para transformar y reconstruir modelos; no dependencia del recorrido operacional inmediato.')
 edge(s,'proy_'+d,'metadata','politica','Solo catálogo del ámbito: publicar ejecuciones, propietarios, calidad y linaje por API; ADLS no ofrece linaje nativo por el conector.')
 edge(s,'powerbi','mart_'+d,'solicitud','Solo modelo semántico del ámbito consulta su PostgreSQL analítico mediante conexión privada de datos; DirectQuery / Import.')
 edge(s,'api_management','search_'+d,'solicitud','Solo API de búsqueda del ámbito consulta OpenSearch con filtros de permisos; APIM no abre conexión directa al índice.')
edge(s,'proy_r','vector','persistencia','Trabajador de representaciones de Oferta: índice reconstruible; modelo de embeddings por seleccionar, no scikit-learn por defecto.')
edge(s,'area_mercaderia','vector','solicitud','Solo Oferta consulta su índice multimodal y confirma precio/disponible con los propietarios.')
edge(s,'lake_r','training','flujo','Conjunto Retail autorizado, versionado y con manifiesto; validación temporal y línea base.')
edge(s,'training','mlflow','persistencia','Registrar experimento, parámetros, métricas y modelo con referencias a código y conjunto de datos.')
edge(s,'mlflow','training','flujo','Obtener versión de modelo promovida por una persona; fallback y deriva implementados por trabajadores.')
edge(s,'training','area_mercaderia','flujo','Recomendaciones de conteo a Existencias; sin ajuste automático de stock.')
edge(s,'backup','mart_r','politica','Cobertura por recurso; PITR no sustituye archivo, retención legal ni pruebas de restauración.')
edge(s,'backup','mart_e','politica','Cobertura y destino propios de Filial; no respaldo común.')
s['notas']=['Vista principal: capas 1–6 horizontales; capas 7–8 en una única banda Capas transversales. Detalles 4.34 y 4.35 en páginas del mismo draw.io.','Un símbolo de producto puede representar instancias propias por ámbito. No significa recursos ni datos compartidos.','ADLS Gen2 se reincorpora por el nuevo registro de Datos, que sustituye su retirada anterior. Región, residencia, capacidad y aceptación siguen por acreditar.','F:C-04 sigue candidato, sin contratos operacionales inventados. VPN conservada.']
save(s,'diag-04-33_arquitectura-datos-transversales')

# Detalle de Datos: carriles paralelos independientes, módulos operativos y analíticos.
d=new('4.34','Detalle lógico de Datos · alimentación, gobierno y modelos')
node(d,'x01','X-01 · control de cruces\nBitácora mínima propia','politica_x01','frontera',codigo='X-01')
node(d,'bitacora_x','PostgreSQL de X-01\nBitácora mínima de cruces · sin perfil unificado','base_datos','datos_x')
edge(d,'x01','bitacora_x','persistencia','Repositorio propio de X-01; no alimenta lago ni modelo analítico conjunto.')
for suffix,name,sg,dg,ig in [('r','Retail','servicios_r','datos_r','integracion_r'),('e','Filial','servicios_e','datos_e','integracion_e')]:
 def nn(id,label,tipo,group=dg,**kw):return node(d,id+'_'+suffix,label+'\n'+name,tipo,group,**kw)
 def ee(a,b,sem,label):edge(d,a+'_'+suffix,b+'_'+suffix,sem,label+'; únicamente '+name)
 nn('services','Servicios y APIs propietarias\nTransacción y outbox por contexto','funcion_logica',sg)
 nn('oper','Azure PostgreSQL Flexible Server\nRepositorios operacionales propios','base_datos')
 nn('bus','Azure Service Bus Premium\nHechos confirmados · reintentos','service_bus',ig)
 nn('adf','Azure Data Factory\nOrquestación · corte · manifiestos','data_factory',ig)
 nn('workers','Java / Spring en AKS\nIngesta, calidad y proyecciones','adaptadores',ig)
 nn('lake','ADLS Gen2\nLanding / curados · versionado','lago_analitica')
 nn('mart','Azure PostgreSQL Flexible Server\nModelos analíticos dedicados','base_datos')
 nn('bi','Microsoft Power BI\nModelos, permisos y conexión privada','power_bi')
 nn('search','OpenSearch autogestionado\nBúsqueda global · índice derivado','opensearch')
 nn('search_api','API de búsqueda global\nIdentidad y filtros por documento','funcion_logica',sg)
 nn('metadata','OpenMetadata autogestionado\nCatálogo, calidad y linaje por API','openmetadata')
 nn('metadata_pg','PostgreSQL de OpenMetadata\nMetadatos propios, sin muestreo libre','base_datos')
 nn('metadata_idx','Buscador compatible de OpenMetadata\nDependencia dedicada · versión por validar','funcion_logica',estado='por_acreditar')
 nn('blob','Azure Blob Storage\nDocumentos y evidencia vigente','blob')
 nn('archive','Azure Blob Storage WORM\nArchivo y evidencia retenida','blob')
 nn('backup','Azure Backup / PostgreSQL PITR\nCobertura y recuperación por recurso','backup_vault')
 ee('services','oper','persistencia','Cada servicio escribe únicamente su contexto')
 ee('services','bus','publicacion','Publicar desde outbox durable, no desde una escritura no confirmada')
 ee('bus','workers','consumo','Deduplicar y aplicar versiones; manejar mensajes fallidos y desorden')
 ee('oper','workers','flujo','Exportación autorizada con corte; cargas históricas, no consultas BI')
 ee('adf','workers','politica','Coordinar cargas y dependencias; factory y runtime con ubicación propia')
 ee('workers','lake','persistencia','Escribir landing, validar y producir curados definidos por finalidad')
 ee('lake','workers','flujo','Reconstrucción desde conjuntos y manifiestos; sin retención infinita de mensajes')
 ee('workers','mart','persistencia','Mantener modelos de lectura, indicadores, punto aplicado y trazabilidad')
 ee('bi','mart','solicitud','Consultar solo modelo analítico: DirectQuery o Import')
 ee('workers','search','persistencia','Actualizar índice y revocar permisos con la fuente')
 ee('search_api','search','solicitud','Consulta con autorización por documento y campo')
 ee('workers','metadata','politica','Publicar linaje de ejecuciones y resultados durables de calidad por API')
 ee('metadata','metadata_pg','persistencia','Persistir catálogo y configuración propia')
 ee('metadata','metadata_idx','solicitud','Índice dedicado soportado por la versión; sin reutilizar búsqueda de negocio')
 ee('services','blob','persistencia','Documentos bajo autoridad del servicio; C-03 verifica completitud')
 ee('workers','archive','persistencia','Copiar, verificar y registrar evidencia/archivo por clase de retención')
 ee('backup','oper','politica','Cobertura de respaldo por recurso y restauración probada con claves')
 ee('backup','mart','politica','Política por recurso; respaldo no equivale a archivo legal')
node(d,'vector','PostgreSQL / pgvector\nOferta: índice multimodal derivado','base_datos','datos_r')
node(d,'embeddings','Trabajador de representaciones · AKS\nModelo multimodal por seleccionar','adaptadores','integracion_r',estado='por_acreditar')
node(d,'training','Python / scikit-learn · AKS\nConteo: evaluación temporal e inferencia','python','datos_r')
node(d,'mlflow','MLflow autogestionado · Retail\nExperimentos y versiones de modelos','mlflow','datos_r')
node(d,'mlflow_pg','PostgreSQL de MLflow · Retail\nMetadatos de experimentos y modelos','base_datos','datos_r')
node(d,'mlflow_blob','Azure Blob Storage · Retail\nArtefactos de modelos de MLflow','blob','datos_r')
node(d,'recommendations','Existencias · recomendaciones de conteo\nPromoción humana · fallback · sin ajuste de stock','funcion_logica','servicios_r')
for a,b,sem,label in [('services_r','embeddings','flujo','Solo Oferta e imágenes autorizadas'),('embeddings','vector','persistencia','Representaciones y versión del modelo; reconstrucción'),('services_r','vector','solicitud','Solo Oferta consulta; confirma precio y disponible con su autoridad'),('lake_r','training','flujo','Conjunto autorizado versionado y manifiesto de Retail'),('training','mlflow','persistencia','Registrar código, parámetros, métricas, modelo y referencia al conjunto'),('mlflow','mlflow_pg','persistencia','Metadatos propios de MLflow'),('mlflow','mlflow_blob','persistencia','Artefactos versionados; distintos de conjuntos de entrenamiento'),('mlflow','training','flujo','Modelo promovido con aprobación humana; deriva y fallback en trabajadores'),('training','recommendations','flujo','Inferencia controlada; sin ajuste automático de stock')]:edge(d,a,b,sem,label)
d['notas']=['Ámbitos independientes: sin pipelines, catálogos, índices, BI ni credenciales comunes. X-01 se muestra como referencia a la vista principal; su bitácora no es una fuente analítica conjunta.','MLflow y scikit-learn únicamente en Retail. Índice de negocio OpenSearch distinto de dependencia de catálogo.','La operación inmediata no depende de carga del lago ni de Power BI; frescura y restauración deben medirse de extremo a extremo.']
save(d,'diag-04-34_detalle-datos')

# Detalle transversal: dos ámbitos, productos separados y relaciones tipadas.
t=new('4.35','Capas transversales · Seguridad y Observabilidad por ámbito')
node(t,'x01','X-01 · bitácora propia\nCorrelación mínima autorizada','politica_x01','frontera',codigo='X-01')
security=[('entra','Microsoft Entra ID P2\nPersonal, MFA y acceso condicional','identidad'),('external','Microsoft Entra External ID\nClientes / titulares del ámbito','external_id'),('intune','Microsoft Intune\nDispositivos compatibles y modo compartido','intune'),('workload','Managed / Workload Identity\nIdentidades de cargas y permisos mínimos','workload_identity'),('kv','Azure Key Vault\nSecretos y certificados','secretos'),('hsm','Azure Managed HSM\nClaves y envoltura de claves de datos','secretos'),('pim','Microsoft Entra PIM\nElevación temporal y aprobación','pim'),('bastion','Azure Bastion Premium\nSalto y grabación de máquinas compatibles','bastion_azure'),('private','Microsoft Entra Private Access\nAcceso administrativo a recursos privados','private_access'),('endpoint','Microsoft Defender for Endpoint\nProtección de equipos compatibles','defender_endpoint'),('cloud','Microsoft Defender for Cloud\nPlanes de cargas expresamente cubiertas','defender_cloud'),('sentinel','Microsoft Sentinel\nSIEM · conectores y eventos seleccionados','sentinel_azure')]
obs=[('otel','OpenTelemetry Collector\nInstrumentación / RUM · colas durables','otel_logo'),('prom','Prometheus\nMétricas · OTLP HTTP / scrape','prometheus'),('loki','Grafana Loki\nRegistros operacionales saneados','loki'),('tempo','Grafana Tempo\nTrazas saneadas','tempo'),('monitor','Azure Monitor / Log Analytics\nDiagnóstico Azure y seguridad necesaria','telemetria'),('grafana','Grafana autogestionado\nConsultas y Grafana Alerting integrado','grafana'),('blackbox','Prometheus Blackbox Exporter\nSondas externas e internas independientes','prometheus')]
for suf,name,sg in [('r','Retail','servicios_r'),('e','Filial','servicios_e')]:
 def nn(id,label,tipo,g,**kw):return node(t,id+'_'+suf,label+'\n'+name,tipo,g,frente='retail' if suf=='r' else 'emisor',**kw)
 def ee(a,b,sem,label):edge(t,a+'_'+suf,b+'_'+suf,sem,label+'; solo '+name)
 nn('source','Canales, servicios, datos y trabajadores\nRUM público entra por borde / APIM propio','funcion_logica',sg)
 nn('admin','Administradores y equipos compatibles\nIdentidad, cumplimiento y privilegios','funcion_logica',sg)
 nn('resources','Recursos privados autorizados\nMáquinas / APIs de administración propias','funcion_logica',sg)
 nn('platform','Recursos Azure y endpoints propios\nPlataforma, tiendas, CI/CD e incidentes','azure',sg)
 for id,label,tipo in security:nn(id,label,tipo,'seguridad')
 for id,label,tipo in obs:nn(id,label,tipo,'observabilidad')
 nn('stage','Azure Blob Storage temporal\nGrabaciones: mutable, sin versionado','blob','seguridad')
 nn('audit','Trabajador durable de auditoría\nCopiar, verificar y registrar integridad','adaptadores','seguridad')
 nn('worm','Azure Blob Storage WORM\nArchivo y evidencia propia del ámbito','blob','seguridad')
 nn('soc','SOC del ámbito · operación 24×7\nAnalistas, escalamiento y respuesta','funcion_logica','seguridad')
 nn('local','OpenTelemetry Collector local\nCola persistente de al menos 24 horas','otel_logo','observabilidad')
 nn('noc','NOC y avisos propios del ámbito\nSalud mínima autorizada; sin payload sensible','funcion_logica','observabilidad')
 for a,b,sem,label in [
 ('source','entra','politica','Autenticación interna; JWT se valida localmente, no consulta por cada solicitud'),('source','external','politica','Autenticación de clientes o titulares con emisor propio'),('intune','admin','politica','Administrar solo equipos compatibles; revocación sin enlace no inmediata'),('source','workload','politica','Tokens de cargas/pods/pipelines con permisos por recurso'),('source','kv','solicitud','Lectura autorizada de secretos y certificados'),('source','hsm','solicitud','Operaciones criptográficas / envoltura DEK por propietario'),('admin','entra','politica','Identidad y MFA de administradores'),('pim','admin','politica','Autorizar elevación temporal; PIM no transporta sesiones'),('admin','private','solicitud','Acceso remoto autorizado por identidad, aplicación y recurso'),('private','resources','solicitud','Ruta autorizada a recursos privados; no sustituye VPN corporativa'),('admin','bastion','solicitud','Sesión administrativa autorizada para máquinas compatibles'),('bastion','resources','solicitud','Salto administrativo a máquinas compatibles; no todas las APIs'),('endpoint','admin','politica','Protección y detección de equipos con agente soportado'),('cloud','platform','politica','Planes y cobertura de cargas declarados'),('entra','sentinel','publicacion','Eventos de identidad por conectores soportados'),('endpoint','sentinel','publicacion','Detecciones seleccionadas'),('cloud','sentinel','publicacion','Detecciones de cargas seleccionadas'),('kv','sentinel','publicacion','Diagnóstico de acceso y operación de claves/secretos'),('hsm','sentinel','publicacion','Auditoría criptográfica soportada'),('sentinel','soc','flujo','Incidentes y correlación con permisos del equipo'),('bastion','stage','persistencia','Destino inicial de grabación mutable, sin política WORM ni versionado'),('stage','audit','flujo','Procesar grabación y verificar copia antes de cerrar retención'),('source','audit','publicacion','Auditoría de negocio durable, distinta de logs muestreados'),('audit','worm','persistencia','Copia verificada, manifiesto e integridad bajo retención propia'),
 ('source','otel','publicacion','Telemetría saneada; RUM público mediante ingreso de borde/gateway autorizado'),('local','otel','publicacion','Drenar cola local tras reconexión por red privada autorizada'),('platform','local','publicacion','Solo componentes locales y heartbeat; diferenciar no observable de fallo confirmado'),('otel','loki','publicacion','Registros mediante OTLP HTTP autenticado'),('otel','tempo','publicacion','Trazas mediante OTLP soportado'),('otel','prom','publicacion','Métricas mediante receptor OTLP HTTP habilitado y protegido'),('prom','platform','solicitud','Scrape de métricas/endpoints/exportadores y registro DORA; evitar doble serie'),('platform','monitor','publicacion','Diagnósticos Azure soportados y fuentes necesarias para seguridad'),('grafana','prom','solicitud','Consultar métricas y SLO con credenciales de lectura'),('grafana','loki','solicitud','Consultar registros operacionales autorizados'),('grafana','tempo','solicitud','Consultar trazas autorizadas'),('grafana','monitor','solicitud','Consultar diagnóstico Azure con autenticación soportada'),('grafana','noc','flujo','Alerting integrado: avisos, agrupación y escalamiento sin payloads sensibles'),('blackbox','platform','solicitud','Probar DNS/TLS/URL segura pública y salud privada desde ubicaciones independientes'),('prom','blackbox','solicitud','Recoger resultados de sondas de endpoints'),('blackbox','noc','flujo','Observador independiente y ruta de aviso sobreviven a la falla monitorizada')]:ee(a,b,sem,label)
for suf in ['r','e']:
 for target in ['audit','otel']:
  edge(t,'x01',target+'_'+suf,'publicacion','Solo extremo '+('Retail' if suf=='r' else 'Filial')+' del contrato X-01: auditoría/telemetría propia y correlación mínima autorizada, sin payload ajeno ni colector común.')
for d in ['r','e']:
 edge(t,'workload_'+d,'platform_'+d,'politica','Obtener tokens para recursos Azure compatibles del propio ámbito; permisos por recurso, no secretos estáticos ni acceso universal.')
t['notas']=['Una sola banda de Capas transversales contiene 7 Seguridad y 8 Observabilidad. Recursos y permisos separados por negocio; las relaciones son familias de contratos, no una cadena por solicitud.','No hay Collector → Azure Monitor en la base productiva. Grafana consulta sus fuentes; Loki/Tempo/Prometheus tienen almacenes y políticas propias.','Cada extremo del contrato X-01 emite auditoría/telemetría únicamente a su ámbito; correlación mínima autorizada, sin colector compartido ni agregado de payload financiero.','Seguridad: 12 meses en línea y 24 adicionales de archivo; respaldo, diagnóstico y auditoría de negocio tienen otras políticas. Región, residencia, licencias, capacidad y pruebas siguen pendientes.']
save(t,'diag-04-35_detalle-transversales')
