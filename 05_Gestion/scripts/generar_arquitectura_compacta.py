"""Revisión visual autorizada: banda transversal izquierda y datos iconográficos."""
import copy,hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
stage=ROOT/'tmp/ancoa-compacto';stage.mkdir(parents=True,exist_ok=True)
base=ROOT/'04_Adjuntos/diagramas/diag-04-33_arquitectura-datos-transversales.json'
s=copy.deepcopy(json.loads(base.read_text(encoding='utf-8')))
s.update(figura='4.36',titulo='Arquitectura lógica por capas · vista compacta')
s['grupos'].append(dict(id='datos_resumen',etiqueta='Productos de datos · representación agregada',frente='transversal'))
mapping={
 'datos_orig':'datos_credito','datos_cartera':'datos_credito','evid_meta':'datos_credito',
 'mart_r':'analitica','mart_e':'analitica','lake_r':'lake','lake_e':'lake',
 'search_r':'search','search_e':'search','archivo_r':'archivo','archivo_e':'archivo',
}
bundles={
 'datos_credito':('PostgreSQL\nCrédito','base_datos','datos_e','Agrupación visual de repositorios propios de Originación, Cartera y metadatos de Evidencia. No es una base, esquema o autoridad compartidos. Cupo y autorización pertenecen a Originación; cuentas/saldos a Cartera; expediente a Evidencia.'),
 'analitica':('PostgreSQL analítico\nModelos dedicados','base_datos','datos_resumen','Un símbolo para modelos analíticos con instancias, permisos y conexiones propias por ámbito; nunca consultas BI en bases operacionales.'),
 'lake':('ADLS Gen2\nConjuntos versionados','lago_analitica','datos_resumen','Un símbolo para lagos separados por ámbito. Landing, curados e históricos autorizados; distinto de archivo WORM y respaldo.'),
 'search':('OpenSearch\nBúsqueda global','opensearch','datos_resumen','Un símbolo para índices y APIs separados por ámbito, con filtros de identidad y permisos; no reutilizar el índice de catálogo de OpenMetadata.'),
 'archivo':('Azure Blob WORM\nArchivo y evidencia','blob','datos_resumen','Un símbolo para archivos retenidos propios de cada ámbito y clase; no almacenamiento común ni destino inicial de grabación Bastion.'),
}
nodes=[]
for n in s['nodos']:
 if n['id'] in mapping:continue
 nodes.append(n)
for id,(label,tipo,group,description) in bundles.items():nodes.append(dict(id=id,etiqueta=label,tipo=tipo,grupo=group,descripcion=description))
s['nodos']=nodes
labels={
 'datos_merc':'PostgreSQL\nMercadería','datos_venta':'PostgreSQL\nVenta','datos_clientes':'PostgreSQL\nClientes',
 'redis':'Azure Managed Redis\nOferta','historial':'PostgreSQL\nPrecios publicados','vector':'PostgreSQL / pgvector\nOferta multimodal',
 'datos_evid':'Azure Blob Storage\nEvidencia vigente','local_data':'Diario local\nOperaciones de venta','cupo_local':'Cupo preautorizado\nSin enlace',
 'adf':'Azure Data Factory\nCargas y dependencias','metadata':'OpenMetadata\nCatálogo y linaje','mlflow':'MLflow\nModelos de conteo',
 'training':'Python / scikit-learn\nConteo predictivo','powerbi':'Microsoft Power BI\nConsulta analítica',
 'backup':'Azure Backup / PITR\nRecuperación por recurso','bitacora':'PostgreSQL\nBitácora de X-01',
 'security_summary':'7 · Seguridad\nEntra ID P2 · External ID · Intune · Workload Identity\nKey Vault · Managed HSM · PIM · Bastion Premium · Private Access\nDefender for Endpoint · Defender for Cloud · Sentinel',
 'observability_summary':'8 · Observabilidad\nOpenTelemetry Collector · Prometheus · Loki · Tempo\nGrafana · Blackbox Exporter · Azure Monitor / Log Analytics',
}
for n in s['nodos']:
 if n['id'] in labels:n['etiqueta']=labels[n['id']]
 if n['id'] in ['powerbi','redis']:n.pop('estado',None)
edges={};origins=[]
for old in s['enlaces']:
 e=copy.deepcopy(old);e['de']=mapping.get(e['de'],e['de']);e['a']=mapping.get(e['a'],e['a'])
 key=(e['de'],e['a'],e['semantica'])
 origins.append(dict(origen=old,agrupado=dict(de=e['de'],a=e['a'],semantica=e['semantica'])))
 if key not in edges:edges[key]=e
 elif old['etiqueta'] not in edges[key]['etiqueta']:edges[key]['etiqueta']+=' / '+old['etiqueta']
s['enlaces']=list(edges.values())
full_edges=copy.deepcopy(s['enlaces'])
new_groups={'canales_publicos':'transversal','canales_privados':'transversal','datos_retail':'retail','adaptadores_retail':'retail','externos_retail':'externo','cap_comunes':'transversal','datos_oferta':'retail','integracion_asociaciones':'transversal'}
for id,front in new_groups.items():s['grupos'].append(dict(id=id,etiqueta=id,frente=front))
families={}
for old in full_edges:
 e=copy.deepcopy(old);a,b=e['de'],e['a'];sem=e['semantica']
 if a in ['web','portal_f'] and b=='front_door':a='canales_publicos'
 elif a in ['pos','operacion','logistica','movil','meson_f'] and b=='entrada_privada':a='canales_privados'
 elif a=='api_management' and b in ['area_mercaderia','area_venta','area_clientes']:b='servicios_r'
 elif a in ['area_mercaderia','area_venta','area_clientes'] and b=='bus_r':a='servicios_r'
 elif a in ['area_mercaderia','area_venta','area_clientes'] and b in ['datos_merc','datos_venta','datos_clientes']:a,b='servicios_r','datos_retail'
 elif a=='bus_r' and b in ['comercio','canales','socios']:b='adaptadores_retail'
 elif a in ['comercio','canales','socios'] and b in ['ext_comercio','ext_canales','ext_socios']:a,b='adaptadores_retail','externos_retail'
 elif a in ['common_docs','common_notif'] and b=='ext_comunes':a='cap_comunes'
 elif (a=='api_management' and b in ['common_flujos','common_docs']) or (a=='common_admin' and b=='api_management'):a,b,sem='cap_comunes','api_management','asociacion'
 elif a=='area_mercaderia' and b in ['redis','historial','vector']:a,b,sem='area_mercaderia','datos_oferta','asociacion'
 elif a in ['proy_r','proy_e'] and b=='lake' or a=='lake' and b in ['proy_r','proy_e']:a,b,sem='integracion_asociaciones','lake','asociacion'
 elif a in ['proy_r','proy_e'] and b in ['metadata','analitica','search']:a='integracion_asociaciones'
 elif (a,b) in [('training','mlflow'),('mlflow','training')]:a,b,sem='training','mlflow','asociacion'
 key=(a,b,sem)
 if key not in families:families[key]=dict(de=a,a=b,semantica=sem,etiqueta='',miembros=[])
 families[key]['miembros'].append(old)
s['enlaces']=[];associations=[]
for key,value in families.items():
 members=value.pop('miembros');value['etiqueta']=' / '.join(e['etiqueta'] for e in members)
 s['enlaces'].append(value);associations.append(dict(asociacion=copy.deepcopy(value),contratos=members))
s['notas']=['Vista única: capas 1–6 horizontales y una banda vertical izquierda Capas transversales con el resumen de 7 Seguridad y 8 Observabilidad. No hay carriles duplicados de Retail y Filial en esa banda.','Datos usa círculos con icono y etiqueta y agrupaciones de microservicios. Un símbolo PostgreSQL por área no fusiona repositorios ni cambia la autoridad por servicio.','Productos repetidos de analítica, lago, búsqueda y archivo se representan una vez; cada ámbito conserva instancias, credenciales, políticas y datos propios. La correspondencia de nodos y contratos se conserva en el archivo de mapeo.','Se mantienen las decisiones de los dos registros de Datos y capas 7–8. Sus detalles anteriores quedan como documentación complementaria, no como páginas obligatorias de esta vista.','VPN conservada. Sin actores. Trece servicios y cinco innovaciones; F:C-04 candidato sin contratos operacionales. Sin modificación de SD-03/SD-04.']
s['notas'].append('Las conexiones se agrupan por familias de contratos. Línea gris sin punta: asociación de lectura/escritura o dependencia, no secuencia de ejecución. El registro conserva todos los contratos detallados; el CSV usa layout libavoid y conexiones ortogonales.')
(stage/'especificacion.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(stage/'mapeo.json').write_text(json.dumps(dict(antecedente=str(base.relative_to(ROOT)),agrupaciones=mapping,contratos=origins,asociaciones=associations),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
protected=list((ROOT/'02_Propuesta/latex_final').rglob('*.tex'))+[ROOT/'80_Artefactos/sd-04_contexto/capa-datos_decisiones-y-precisiones_2026-10-22.md',ROOT/'80_Artefactos/sd-04_contexto/capas-07-08_cambios-y-conexiones_2026-10-22.md']
if not (stage/'hashes-antes.json').exists():(stage/'hashes-antes.json').write_text(json.dumps({str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in protected},indent=2),encoding='utf-8')
print(len(s['nodos']),'componentes;',len(s['enlaces']),'conectores')
