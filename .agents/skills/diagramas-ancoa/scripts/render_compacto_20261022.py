"""Plantillas de catálogo L2 para los registros de Datos y capas transversales."""
import html,json,math,shutil,subprocess,textwrap,xml.etree.ElementTree as ET
from pathlib import Path
from _comun import CATALOGO,frente_de_nodo
from render_capas_referencia import icono_data
from router_horizontal import enrutar

def distribucion(spec):
 from render_revision_registros import distribucion as anterior
 base=json.loads(Path('04_Adjuntos/diagramas/diag-04-33_arquitectura-datos-transversales.json').read_text(encoding='utf-8'))
 _,_,oldpos,_,_,oldareas=anterior(base)
 ids={n['id'] for n in spec['nodos']};pos={id:(x+300,y,w,h) for id,(x,y,w,h) in oldpos.items() if id in ids};frames=[];labels=[]
 def frame(id,x,y,w,h,label,front='transversal'):frames.append((id,x,y,w,h,label,front))
 def put(id,x,y,w=84,h=84):pos[id]=(x,y,w,h)
 for x,y,w,h,label,front in [(660,210,2280,210,'1 · PRESENTACIÓN','frontera'),(660,490,2280,190,'2 · BORDE Y EXPOSICIÓN','transversal'),(660,780,2280,240,'3 · PUERTA DE ENLACE DE SERVICIOS','retail'),(660,1050,2280,800,'4 · SERVICIOS DE NEGOCIO','capa_servicios'),(660,1920,2280,520,'5 · INTEGRACIÓN Y EVENTOS','azure'),(660,2520,2280,820,'6 · DATOS','azure')]:frame('',x,y,w,h,label,front)
 areas={id:(x+300,y,w,h) for id,(x,y,w,h) in oldareas.items()}
 names={'area_mercaderia':'MERCADERÍA','area_venta':'VENTA','area_clientes':'RELACIÓN CON EL CLIENTE','servicios_e':'CRÉDITO'}
 for id,(x,y,w,h) in areas.items():frame(id,x,y,w,h,names[id],'emisor' if id=='servicios_e' else 'retail')
 frame('',330,210,280,3130,'TECNOLOGÍAS','transversal')
 frame('',3000,1120,470,1260,'SISTEMAS EXTERNOS','externo')
 frame('',30,210,280,3130,'CAPAS TRANSVERSALES','transversal')
 put('security_summary',50,300,240,1720);put('observability_summary',50,2080,240,1240)
 for id,x,label,front in [('datos_merc',680,'MERCADERÍA','retail'),('datos_venta',1200,'VENTA','retail'),('datos_clientes',1720,'CLIENTES','retail'),('datos_credito',2400,'CRÉDITO','emisor')]:
  frame('',x,2590,490,220,label,front);put(id,x+203,2640)
 put('bitacora',2255,2640)
 for i,id in enumerate(['redis','historial','vector','search','datos_evid','archivo','local_data','cupo_local']):put(id,748+i*285,2865)
 for i,id in enumerate(['adf','lake','analitica','powerbi','metadata','training','mlflow','backup']):put(id,748+i*285,3120)
 labels.extend([(350,1640,'CAPACIDADES COMUNES',16),(350,1665,'Base tecnológica',14),(700,1880,'Cada servicio conserva su transacción, outbox y repositorios propios.',16),(30,3380,'Los símbolos agrupan productos y repositorios: instancias, permisos y datos propios por ámbito. VPN conservada.',17)])
 for n in spec['nodos']:
  id=n['id']
  if id not in CIRCLES:continue
  x,y,w,h=pos[id];lines=[]
  for line in n['etiqueta'].split('\n'):lines.extend(textwrap.wrap(line,width=22,break_long_words=False) or [''])
  # Etiquetas fuera del círculo: también son obstáculos para las conexiones.
  for j,line in enumerate(lines):labels.append((x+w/2-len(line)*16*.295,y+h+25+j*21,line,16))
 association_boxes={
 'canales_publicos':(670,280,645,115),'canales_privados':(1320,280,1620,115),
 'servicios_r':(670,1110,1550,720),'datos_retail':(670,2580,1550,245),
 'adaptadores_retail':(690,2110,1510,110),'externos_retail':(3010,1180,450,730),
 'cap_comunes':(340,1700,270,900),'datos_oferta':(720,2840,825,190),
 'integracion_asociaciones':(660,1920,2280,520)}
 for id,box in association_boxes.items():
  areas[id]=box
  if id=='integracion_asociaciones':
   frames=[(id if f[5].startswith('5 ·') else f[0],*f[1:]) for f in frames]
  else:frame(id,*box,'','transversal')
 missing=ids-set(pos)
 if missing:raise ValueError('Componentes sin ranura: '+str(missing))
 return 3500,3420,pos,frames,labels,areas

CIRCLES={'datos_merc','datos_venta','datos_clientes','datos_credito','bitacora','redis','historial','vector','search','datos_evid','archivo','local_data','cupo_local','adf','lake','analitica','powerbi','metadata','training','mlflow','backup'}

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
  p=pal[front]
  if not name:
   rect(id,x,y,w,h,'none',pal['transversal']['borde']);continue
  rect(id or 'frame'+str(i),x,y,w,h,p['relleno'],p['borde']);rect('',x,y,w,46,pal['transversal']['caja'],pal['transversal']['borde'])
  fs=14 if w<400 else 21;text(x+14,y+31,name,fs,True)
  obstacles.append((x+8,y+3,min(x+w-8,x+len(name)*fs*.59+30),y+43))
 for x,y,label,size in labels:
  text(x,y,label,size,True);obstacles.append((x-3,y-size-5,x+len(label)*size*.59+10,y+8))
 routes=enrutar(pos,spec['enlaces'],obstacles,areas)
 # Proyectar los terminales sobre la circunferencia real. Se conserva la
 # orientación ortogonal y el tramo exterior que evitó los demás obstáculos.
 for e,r in zip(spec['enlaces'],routes):
  for end,key,index in [('de','source',0),('a','target',-1)]:
   id=e[end]
   if id not in CIRCLES:continue
   p=r[key];ax,ay=p['anchor'];dx,dy=p['offset'];x,y,w,h=pos[id]
   if ax in (0,1):ax=(1+(-1 if ax==0 else 1)*math.sqrt(max(0,1-(2*ay-1)**2)))/2
   else:ay=(1+(-1 if ay==0 else 1)*math.sqrt(max(0,1-(2*ax-1)**2)))/2
   p['anchor']=(ax,ay);point=(round(x+w*ax+dx,3),round(y+h*ay+dy,3));p['point']=point;r['points'][index]=point

 for e,r in zip(spec['enlaces'],routes):
  definition=CATALOGO['semanticas_enlace'][e['semantica']];color=definition['color'];dash=definition['estilo']
  pattern=' stroke-dasharray="7 5"' if dash=='dashed' else ' stroke-dasharray="2 5"' if dash=='dotted' else ''
  arrow='' if e['semantica']=='asociacion' else ' marker-end="url(#flecha)"'
  d='M'+' L'.join(f'{x},{y}' for x,y in r['points'])
  svg.append(f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-width="5"/>')
  svg.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.2"{pattern}{arrow}><title>{html.escape(e["etiqueta"])}</title></path>')
 for n in spec['nodos']:
  x,y,w,h=pos[n['id']];front=frente_de_nodo(n,groups) or 'transversal';p=pal['externo'] if n['tipo']=='sistema_conservado' else pal[front];pending=n.get('estado')=='por_acreditar'
  if n['id'] in ('security_summary','observability_summary'):
   category='seguridad' if n['id']=='security_summary' else 'observabilidad'
   products=CATALOGO['estilos']['L2']['referencia']['banda_transversal_resumida'][category]
   title='7 · SEGURIDAD' if category=='seguridad' else '8 · OBSERVABILIDAD'
   text(x,y+27,title,20,True)
   spacing=130 if category=='seguridad' else 166
   for j,product in enumerate(products):
    yy=y+70+j*spacing;uri=icono_data(product['tipo']);size=42
    svg.append(f'<image x="{x}" y="{yy}" width="{size}" height="{size}" href="{uri}"/>')
    icons.append(('icon_'+n['id']+'_'+str(j),'','shape=image;imageAspect=1;image='+uri.replace(';base64,',',')+';',x,yy,size,size))
    for k,line in enumerate(textwrap.wrap(product['etiqueta'],width=21,break_long_words=False)):
     text(x+52,yy+18+k*21,line,16,True)
   cards.append((n['id'],'','fillColor=none;strokeColor=none;',x,y,w,h))
   continue
  if n['id'] in CIRCLES:
   uri=icono_data(n['tipo']);size=48
   svg.append(f'<ellipse cx="{x+w/2}" cy="{y+h/2}" rx="{w/2}" ry="{h/2}" fill="{p["caja"]}" stroke="{p["borde"]}" stroke-width="1.6"/>')
   svg.append(f'<image x="{x+(w-size)/2}" y="{y+(h-size)/2}" width="{size}" height="{size}" href="{uri}"/>')
   cards.append((n['id'],'',f'ellipse;html=0;fillColor={p["caja"]};strokeColor={p["borde"]};',x,y,w,h))
   icons.append(('icon_'+n['id'],'','shape=image;imageAspect=1;image='+uri.replace(';base64,',',')+';',x+(w-size)/2,y+(h-size)/2,size,size))
   continue
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
 for i,(sem,name) in enumerate([('solicitud','API / consulta'),('persistencia','Datos propios'),('publicacion','Publicación'),('consumo','Consumo'),('politica','Política / gobierno'),('asociacion','Asociación')]):
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
  c=ET.SubElement(root,'mxCell',id='edge'+str(i),value='',edge='1',parent='1',source=e['de'],target=e['a'],tooltip=e['etiqueta'],style=f'edgeStyle=none;orthogonal=1;rounded=0;endArrow={"none" if e["semantica"]=="asociacion" else "block"};endFill=1;strokeColor={color};strokeWidth=2.2;{extra}exitX={sx};exitY={sy};entryX={tx};entryY={ty};exitDx={sdx};exitDy={sdy};entryDx={tdx};entryDy={tdy};exitPerimeter=0;entryPerimeter=0;')
  geo=ET.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'});arr=ET.SubElement(geo,'Array',attrib={'as':'points'})
  for x,y in r['points'][1:-1]:ET.SubElement(arr,'mxPoint',x=str(x),y=str(y))
 for o in cards+icons:cell(*o)
 for i,o in enumerate(texts):cell('text'+str(i),*o)
 ET.ElementTree(mx).write(out.with_suffix('.drawio'),encoding='utf-8',xml_declaration=True)
 out.with_suffix('.rutas.json').write_text(json.dumps([dict(enlace=e,**r) for e,r in zip(spec['enlaces'],routes)],ensure_ascii=False,indent=2),encoding='utf-8')
 out.with_suffix('.leyenda.txt').write_text('Figura '+spec['figura']+': '+spec['titulo']+'\n'+spec['fuente']+'\n\nLeyenda: verde Retail; lila Filial; gris productos agregados/transversales; amarillo control de cruces. Flechas por semántica de catálogo, sin evidencia documental visible.\n'+'\n'.join(spec['notas'])+'\nConectores anclados al contorno; SVG y draw.io usan los mismos puntos. El diagrama valida estructura gráfica, no despliegue ni cumplimiento. SD-03/04 sin cambios. Uso de IA: Alto, registrar al incorporar a la propuesta.\nIconos de diagrams; OpenSearch y OpenMetadata de sus repositorios oficiales. Datos: círculos con etiqueta inferior; banda transversal izquierda con resumen de productos, sin carriles por negocio. Key Vault y Managed HSM usan icono de familia; Blackbox usa icono de Prometheus.\n',encoding='utf-8')
 return out
