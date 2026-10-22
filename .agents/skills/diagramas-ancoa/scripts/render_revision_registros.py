"""Plantillas de catálogo L2 para los registros de Datos y capas transversales."""
import html,json,shutil,subprocess,textwrap,xml.etree.ElementTree as ET
from pathlib import Path
from _comun import CATALOGO,frente_de_nodo
from render_capas_referencia import icono_data
from router_horizontal import enrutar

def distribucion(spec):
 ids={n['id'] for n in spec['nodos']};pos={};frames=[];labels=[];areas={}
 def frame(id,x,y,w,h,label,front='transversal'):frames.append((id,x,y,w,h,label,front))
 def put(id,x,y,w=450,h=100):pos[id]=(x,y,w,h)
 if 'security_summary' in ids:
  from render_horizontal_capa4 import posiciones,AREAS
  import json as jj
  base=jj.loads(Path('04_Adjuntos/diagramas/diag-04-31_arquitectura-servicios-y-flujos.json').read_text(encoding='utf-8'))
  pos.update({k:v for k,v in posiciones(base).items() if k in ids})
  W,H=3200,4260
  for x,y,w,h,label,front in [(360,210,2280,210,'1 · PRESENTACIÓN','frontera'),(360,490,2280,190,'2 · BORDE Y EXPOSICIÓN','transversal'),(360,780,2280,240,'3 · PUERTA DE ENLACE DE SERVICIOS','retail'),(360,1050,2280,800,'4 · SERVICIOS DE NEGOCIO','capa_servicios'),(360,1920,2280,660,'5 · INTEGRACIÓN Y EVENTOS','azure'),(360,2660,2280,1200,'6 · DATOS','emisor')]:frame('',x,y,w,h,label,front)
  for id,(x,y,w,h) in AREAS.items():
   areas[id]=(x,y-160,w,h)
   name={'area_mercaderia':'MERCADERÍA','area_venta':'VENTA','area_clientes':'RELACIÓN CON EL CLIENTE','servicios_e':'CRÉDITO · FILIAL'}[id]
   frame(id,x,y-160,w,h,name,'emisor' if id=='servicios_e' else 'retail')
  frame('',30,210,280,3650,'TECNOLOGÍAS','transversal')
  frame('',2700,1120,470,1260,'SISTEMAS EXTERNOS','externo')
  frame('',30,3920,3140,270,'CAPAS TRANSVERSALES · controles y recursos propios por ámbito','transversal')
  put('security_summary',360,3990,1300,170);put('observability_summary',1790,3990,1300,170)
  put('adf',400,2480,710,80);put('metadata',1180,2480,710,80);put('backup',50,2940,250,175)
  for i,id in enumerate(['datos_merc','datos_venta','datos_clientes']):put(id,400+i*520,2740,450,100)
  for id,x,y in [('lake_r',400,2910),('archivo_r',920,2910),('vector',1440,2910),('mart_r',400,3080),('redis',920,3080),('historial',1440,3080),('training',400,3260),('mlflow',920,3260),('search_r',1440,3260),('local_data',920,3600)]:put(id,x,y,450,110)
  put('powerbi',400,3450,1490,100);put('bitacora',1955,2740,130,130)
  for i,id in enumerate(['datos_orig','datos_cartera','evid_meta','datos_evid','lake_e','mart_e','archivo_e','search_e','cupo_local']):put(id,2120,2740+i*120,450,85)
  labels.extend([(50,1640,'CAPACIDADES COMUNES',16),(50,1665,'Base tecnológica por ámbito',14),(400,1880,'Cada servicio conserva su transacción y outbox. A/C/E/P: auditoría · acceso · exportación · parámetros.',16),(2720,1290,'Plataformas conservadas / convivencia',14),(400,3820,'Datos: detalle de alimentación, gobierno y modelos en la página 2.',17)])
 elif 'mlflow_pg' in ids:
  W,H=3300,3140
  for suf,name,x,front in [('r','RETAIL',30,'retail'),('e','FILIAL EMISORA',1680,'emisor')]:
   frame('',x,210,1590,2700,name,front)
   frame('',x+15,280,1560,425,'4 · Contextos propietarios / 5 · Integración y eventos',front)
   frame('',x+15,740,1560,1060,'6 · Datos · repositorios y gobierno',front)
   left=x+30
   for id,col,y in [('services',0,355),('oper',1,355),('adf',2,355),('bus',0,550),('workers',1,550),('lake',0,830),('mart',1,830),('bi',2,830),('search_api',0,1060),('search',1,1060),('blob',2,1060),('backup',1,1260),('archive',2,1260),('metadata',0,1510),('metadata_pg',1,1510),('metadata_idx',2,1510)]:put(id+'_'+suf,left+col*530,y,470,130)
  frame('',45,1850,1560,1000,'6 · Datos · conteo predictivo y catálogo multimodal · RETAIL','retail')
  for id,x,y in [('embeddings',60,1950),('vector',590,1950),('training',60,2180),('mlflow',590,2180),('mlflow_pg',1120,2180),('mlflow_blob',1120,2430),('recommendations',60,2700)]:put(id,x,y,470,130)
  put('x01',60,2950,1000,115);put('bitacora_x',1200,2950,1450,115)
  labels.extend([(1740,1970,'Los datos y metadatos permanecen en su ámbito.',23),(1740,2020,'MLflow y scikit-learn se usan solo en Retail.',21),(1740,2070,'El lago no participa en la respuesta operacional inmediata.',20),(1740,2430,'X-01 es referencia al recorrido de la página principal.',18),(1740,2470,'Su bitácora no alimenta una analítica conjunta.',18),(1740,2610,'Catálogo y búsqueda de negocio: índices distintos.',19),(1740,2650,'Modelo de representaciones multimodales por seleccionar.',18)])
 else:
  W,H=3600,3070
  frame('',30,210,3540,2810,'CAPAS TRANSVERSALES · ámbitos, recursos y permisos separados','transversal')
  sec=['entra','external','intune','workload','kv','hsm','endpoint','cloud','pim','bastion','private','sentinel','stage','audit','worm','soc']
  for suf,name,x,front in [('r','RETAIL',60,'retail'),('e','FILIAL EMISORA',1830,'emisor')]:
   frame('',x,285,1710,2350,name,front)
   for i,id in enumerate(['source','admin','platform','resources']):put(id+'_'+suf,x+25+i*425,365,390,120)
   labels.append((x+25,530,'7 · SEGURIDAD',24))
   for i,id in enumerate(sec):put(id+'_'+suf,x+25+(i%4)*425,580+(i//4)*225,390,135)
   labels.append((x+25,1510,'8 · OBSERVABILIDAD',24))
   for i,id in enumerate(['otel','local','monitor','prom','loki','tempo','grafana','blackbox','noc']):put(id+'_'+suf,x+25+(i%3)*565,1580+(i//3)*240,520,145)
  put('x01',330,2840,2940,110)
  labels.extend([(80,2685,'RUM entra por borde/gateway propio. Auditoría durable distinta de registros y trazas. VPN corporativa conservada.',20),(80,2725,'Grafana consulta sus fuentes. Las sondas complementan los SLO y deben sobrevivir a la falla que monitorizan.',20)])
 missing=ids-set(pos)
 if missing:raise ValueError('Componentes sin ranura: '+str(missing))
 return W,H,{id:pos[id] for id in ids},frames,labels,areas

def renderizar(spec,salida):
 out=Path(salida);out.parent.mkdir(parents=True,exist_ok=True)
 W,H,pos,frames,labels,areas=distribucion(spec);groups={g['id']:g for g in spec['grupos']};pal=CATALOGO['frentes']
 svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">','<defs><marker id="flecha" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L7,3 L0,6 Z" fill="context-stroke"/></marker></defs>'];background=[];texts=[];cards=[];icons=[];obstacles=[]
 def rect(id,x,y,w,h,fill,stroke,record=True,dash=False):
  svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{stroke}" stroke-width="1.3"'+(' stroke-dasharray="7 4"' if dash else '')+'/>')
  if record:background.append((id,'',f'rounded=1;fillColor={fill};strokeColor={stroke};',x,y,w,h))
 def text(x,y,s,size=18,bold=False,record=True):
  svg.append(f'<text x="{x}" y="{y}" font-family="Segoe UI,Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="#1A1A1A">{html.escape(s)}</text>')
  if record:texts.append((s,f'text;html=0;align=left;fontSize={size};fontStyle={1 if bold else 0};',x,y-size,len(s)*size*.59+15,size+8))
 rect('',0,0,W,H,'#FFFFFF','#FFFFFF');text(30,35,'ONLY SIMPLE SOLUTIONS / MULTITIENDAS ANCOA',19,True);text(30,80,spec['titulo'],29,True)
 text(30,112,'L2 · diseño objetivo · un símbolo por producto no significa recursos compartidos · * definición / validación pendiente',18)
 obstacles.append((0,0,W,185))
 for i,(id,x,y,w,h,name,front) in enumerate(frames):
  p=pal[front];rect(id or 'frame'+str(i),x,y,w,h,p['relleno'],p['borde']);rect('',x,y,w,46,pal['transversal']['caja'],pal['transversal']['borde'])
  fs=16 if w<400 else 21;text(x+14,y+31,name,fs,True)
  obstacles.append((x+8,y+3,min(x+w-8,x+len(name)*fs*.59+30),y+43))
 for x,y,label,size in labels:
  text(x,y,label,size,True);obstacles.append((x-3,y-size-5,x+len(label)*size*.59+10,y+8))
 routes=enrutar(pos,spec['enlaces'],obstacles,areas)
 for e,r in zip(spec['enlaces'],routes):
  definition=CATALOGO['semanticas_enlace'][e['semantica']];color=definition['color'];dash=definition['estilo']
  pattern=' stroke-dasharray="7 5"' if dash=='dashed' else ' stroke-dasharray="2 5"' if dash=='dotted' else ''
  d='M'+' L'.join(f'{x},{y}' for x,y in r['points'])
  svg.append(f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-width="5"/>')
  svg.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.2"{pattern} marker-end="url(#flecha)"><title>{html.escape(e["etiqueta"])}</title></path>')
 for n in spec['nodos']:
  x,y,w,h=pos[n['id']];front=frente_de_nodo(n,groups) or 'transversal';p=pal['externo'] if n['tipo']=='sistema_conservado' else pal[front];pending=n.get('estado')=='por_acreditar'
  rect('',x,y,w,h,p['caja'],p['borde'],False,pending)
  uri=icono_data(n['tipo']);size=28 if w<190 else 40 if h<100 else 46
  if n['tipo']=='private_link':
   svg.pop();svg.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{uri}"/>');cards.append((n['id'],'','fillColor=none;strokeColor=none;',x,y,w,h));icons.append(('icon_'+n['id'],'','shape=image;imageAspect=1;image='+uri.replace(';base64,',',')+';',x,y,w,h));continue
  narrow=w<190;ix=x+(w-size)/2 if narrow else x+10;iy=y+10 if narrow else y+(h-size)/2
  svg.append(f'<image x="{ix}" y="{iy}" width="{size}" height="{size}" href="{uri}"/>')
  code=n.get('codigo','');badge='A · C · E · P'+(' · candidato' if n['id']=='regulatorio' else '') if code.startswith(('R:','F:')) or n['id']=='x01' and 'security_summary' in {v['id'] for v in spec['nodos']} else ''
  lines=[]
  for line in n['etiqueta'].split('\n'):lines.extend(textwrap.wrap(line,width=12 if narrow else max(12,int((w-size-35)/8.6)),break_long_words=False) or [''])
  if pending:lines[-1]+=' *'
  fs=16 if w<350 else 18
  if len(lines)*(fs+4)+(18 if badge else 0)>h-6:fs=14
  if len(lines)*(fs+4)+(18 if badge else 0)>h:raise ValueError('Texto no cabe: '+n['id'])
  top=y+60 if narrow else y+(h-len(lines)*(fs+4)-(18 if badge else 0))/2+fs
  for j,line in enumerate(lines):text(x+8 if narrow else x+size+22,top+j*(fs+4),line,fs,j==0,False)
  if badge:text(x+8 if narrow else x+size+22,y+h-9,badge,12,True,False)
  value=html.escape(n['etiqueta']).replace('\n','<br>')+(' *' if pending else '')+('<br>'+badge if badge else '')
  style=f'rounded=1;whiteSpace=wrap;html=1;align=left;verticalAlign=middle;spacingLeft={8 if narrow else size+22};'+('spacingTop=35;' if narrow else '')+f'fontSize={fs};fillColor={p["caja"]};strokeColor={p["borde"]};'+('dashed=1;' if pending else '')
  cards.append((n['id'],value,style,x,y,w,h));icons.append(('icon_'+n['id'],'','shape=image;imageAspect=1;image='+uri.replace(';base64,',',')+';',ix,iy,size,size))
 text(30,158,'Leyenda',16,True)
 for i,(sem,name) in enumerate([('solicitud','API / consulta'),('persistencia','Datos propios'),('publicacion','Publicación'),('consumo','Consumo'),('politica','Política / gobierno')]):
  x=220+i*540;color=CATALOGO['semanticas_enlace'][sem]['color'];svg.append(f'<path d="M{x},150 L{x+30},150" stroke="{color}" stroke-width="3" marker-end="url(#flecha)"/>');text(x+40,158,name,16,True)
 svg.append('</svg>');out.with_suffix('.svg').write_text('\n'.join(svg),encoding='utf-8')
 exe=shutil.which('inkscape') or 'C:/Program Files/Inkscape/bin/inkscape.com'
 subprocess.run([exe,str(out.with_suffix('.svg')),'--export-type=png','--export-filename='+str(out.with_suffix('.png')),'--export-width=3600'],check=True,capture_output=True,timeout=60)
 mx=ET.Element('mxfile',host='diagramas-ancoa',type='device');dg=ET.SubElement(mx,'diagram',name=spec['titulo']);model=ET.SubElement(dg,'mxGraphModel',page='0',grid='1',gridSize='10');root=ET.SubElement(model,'root');ET.SubElement(root,'mxCell',id='0');ET.SubElement(root,'mxCell',id='1',parent='0')
 def cell(id,value,style,x,y,w,h):
  c=ET.SubElement(root,'mxCell',id=id,value=value,style=style,vertex='1',parent='1');ET.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
 for i,(id,*o) in enumerate(background):cell(id or 'background'+str(i),*o)
 for i,(e,r) in enumerate(zip(spec['enlaces'],routes)):
  definition=CATALOGO['semanticas_enlace'][e['semantica']];color=definition['color'];ls=definition['estilo'];extra='dashed=1;dashPattern=2 5;' if ls=='dotted' else 'dashed=1;' if ls=='dashed' else ''
  sx,sy=r['source']['anchor'];tx,ty=r['target']['anchor'];sdx,sdy=r['source']['offset'];tdx,tdy=r['target']['offset']
  c=ET.SubElement(root,'mxCell',id='edge'+str(i),value='',edge='1',parent='1',source=e['de'],target=e['a'],tooltip=e['etiqueta'],style=f'edgeStyle=none;orthogonal=1;rounded=0;endArrow=block;endFill=1;strokeColor={color};strokeWidth=2.2;{extra}exitX={sx};exitY={sy};entryX={tx};entryY={ty};exitDx={sdx};exitDy={sdy};entryDx={tdx};entryDy={tdy};exitPerimeter=0;entryPerimeter=0;')
  geo=ET.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'});arr=ET.SubElement(geo,'Array',attrib={'as':'points'})
  for x,y in r['points'][1:-1]:ET.SubElement(arr,'mxPoint',x=str(x),y=str(y))
 for o in cards+icons:cell(*o)
 for i,o in enumerate(texts):cell('text'+str(i),*o)
 ET.ElementTree(mx).write(out.with_suffix('.drawio'),encoding='utf-8',xml_declaration=True)
 out.with_suffix('.rutas.json').write_text(json.dumps([dict(enlace=e,**r) for e,r in zip(spec['enlaces'],routes)],ensure_ascii=False,indent=2),encoding='utf-8')
 out.with_suffix('.leyenda.txt').write_text('Figura '+spec['figura']+': '+spec['titulo']+'\n'+spec['fuente']+'\n\nLeyenda: verde Retail; lila Filial; gris productos agregados/transversales; amarillo control de cruces. Flechas por semántica de catálogo, sin evidencia documental visible.\n'+'\n'.join(spec['notas'])+'\nConectores anclados al contorno; SVG y draw.io usan los mismos puntos. El diagrama valida estructura gráfica, no despliegue ni cumplimiento. SD-03/04 sin cambios. Uso de IA: Alto, registrar al incorporar a la propuesta.\nIconos de diagrams; OpenSearch y OpenMetadata de sus repositorios oficiales. Key Vault y Managed HSM usan icono de familia; Blackbox usa icono de Prometheus.\n',encoding='utf-8')
 return out
