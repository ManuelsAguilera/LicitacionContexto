"""Exporta la vista compacta validada al importador CSV nativo de draw.io."""
import argparse,csv,hashlib,html,io,json,sys,xml.etree.ElementTree as ET
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'.agents/skills/diagramas-ancoa/scripts'))
from validar import validar
from _comun import CATALOGO
from render_compacto_20261022 import distribucion,CIRCLES

def exportar(origen,salida):
 s=json.loads(origen.with_suffix('.json').read_text(encoding='utf-8'));errors,warnings=validar(s)
 if errors or warnings:raise ValueError((errors,warnings))
 cells={c.get('id'):c for c in ET.parse(origen.with_suffix('.drawio')).getroot().iter('mxCell')}
 W,H,pos,frames,labels,areas=distribucion(s)
 def geo(c):
  g=c.find('mxGeometry');return tuple(float(g.get(k,'0')) for k in ['x','y','width','height'])
 containers={}
 for i,(id,x,y,w,h,name,front) in enumerate(frames):
  alias='capas_transversales' if name=='CAPAS TRANSVERSALES' else 'tecnologias' if name=='TECNOLOGÍAS' else 'externos' if name=='SISTEMAS EXTERNOS' else 'marco_'+str(i)
  containers[id or alias]=dict(label=name,box=(x,y,w,h))
 for id in ['security_summary','observability_summary']:containers[id]=dict(label='7 · SEGURIDAD' if id=='security_summary' else '8 · OBSERVABILIDAD',box=pos[id])
 def parent(box,own=None):
  x,y,w,h=box;options=[]
  for id,v in containers.items():
   if id==own:continue
   xx,yy,ww,hh=v['box']
   if ww*hh>w*h and xx<=x and yy<=y and x+w<=xx+ww and y+h<=yy+hh:options.append((ww*hh,id))
  return min(options)[1] if options else ''
 routes=json.loads(origen.with_suffix('.rutas.json').read_text(encoding='utf-8'))
 keys=['e'+str(i) for i in range(len(s['enlaces']))];ports={};terminales=[];aliases={}
 for key,e,r in zip(keys,s['enlaces'],routes):
  ends=[]
  for name,role in [('de','source'),('a','target')]:
   id=e[name]
   if id not in pos:
    port='puerto_'+key+'_'+name;x,y=r[role]['point'];ports[port]=dict(box=(x-2,y-2,4,4),grupo=id);aliases[port]=id;id=port
   ends.append(id)
  terminales.append((ends[0],ends[1],e['semantica']))
 refs={id:{key:[] for key in keys} for id in list(containers)+list(pos)+list(ports)}
 for key,(a,b,sem) in zip(keys,terminales):refs[a][key].append(b)
 rows=[]
 def row(id,label,box,style,par='',component='',real_parent=False):
  x,y,w,h=box
  if real_parent:px,py,_,_=containers[par]['box'];x-=px;y-=py
  r=dict(id=id,etiqueta=label,parent=par if real_parent else '',agrupacion=par,x=x,y=y,w=w,h=h,estilo=style,componente=component)
  for key in keys:r['a_'+key]=','.join(refs.get(id,{}).get(key,[]))
  rows.append(r)
 row('titulo',html.escape(s['titulo']),(30,30,3440,65),'text;html=1;fontSize=28;fontStyle=1;align=left;')
 legend='Leyenda: azul API / consulta · verde datos propios · naranja publicación · violeta consumo · celeste contrato externo.<br>Gris sin punta: asociación de contratos, lectura/escritura o dependencia. Dorado punteado: gobierno.<br>Las conexiones de área agrupan contratos. Cada servicio y ámbito conserva sus instancias, permisos y datos propios. VPN conservada.'
 row('leyenda',legend,(30,H-95,3440,90),'text;html=1;whiteSpace=wrap;fontSize=16;align=left;')
 # Padres primero, de mayor a menor; las coordenadas conservan el marco de origen.
 for id,v in sorted(containers.items(),key=lambda item:-item[1]['box'][2]*item[1]['box'][3]):
  box=v['box'];label=v['label'];par=parent(box,id)
  if id in ['security_summary','observability_summary']:style='fillColor=none;strokeColor=none;'
  else:
   cell=next(c for c in cells.values() if c.get('vertex')=='1' and geo(c)==box and not c.get('id','').startswith('icon_'))
   style=cell.get('style')
  style+='container=1;transparentBounds=1;groupPadding=0;collapsible=0;recursiveResize=0;arcSize=14;absoluteArcSize=1;verticalAlign=top;align=left;spacingTop=8;spacingLeft=12;fontStyle=1;fontSize=18;'
  row(id,html.escape(label),box,style,par)
 # Dos límites invisibles conservan cada marco transparente, sin anidar los
 # componentes: el enrutador recibe las mismas coordenadas que ve el editor.
 for id,v in containers.items():
  x,y,w,h=v['box']
  for j,(xx,yy) in enumerate([(x,y),(x+w-1,y+h-1)]):row('limite_'+id+'_'+str(j),'',(xx,yy,1,1),'fillColor=none;strokeColor=none;opacity=0;',id,real_parent=True)
 for id,v in ports.items():row(id,'',v['box'],'ellipse;fillColor=#5B6770;strokeColor=none;',component='Puerto de asociación: '+v['grupo'])
 for n in s['nodos']:
  id=n['id']
  if id in ['security_summary','observability_summary']:
   cat='seguridad' if id=='security_summary' else 'observabilidad';x,y,w,h=pos[id];spacing=130 if cat=='seguridad' else 166
   from render_capas_referencia import icono_data
   for j,p in enumerate(CATALOGO['estilos']['L2']['referencia']['banda_transversal_resumida'][cat]):
    uri=icono_data(p['tipo']).replace(';base64,',',')
    style='shape=label;html=1;whiteSpace=wrap;fillColor=none;strokeColor=none;spacingLeft=52;align=left;verticalAlign=middle;fontSize=16;image='+uri+';imageWidth=42;imageHeight=42;imageAlign=left;imageVerticalAlign=middle;'
    row('producto_'+id+'_'+str(j),html.escape(p['etiqueta']),(x,y+70+j*spacing,240,65),style,id,p['etiqueta'])
   continue
  c=cells[id];box=pos[id];style=c.get('style');icon=cells.get('icon_'+id)
  label=c.get('value') or html.escape(n['etiqueta']).replace('\n','<br>')
  if icon is not None:
   uri=icon.get('style').split('image=',1)[1].split(';',1)[0]
   style+='shape=label;image='+uri+';'
  if id in CIRCLES:
   # Label redondeado y perímetro elíptico: icono editable dentro del círculo,
   # texto fuera de su geometría y puertos sobre la circunferencia real.
   style+='rounded=1;arcSize=100;perimeter=ellipsePerimeter;imageWidth=48;imageHeight=48;imageAlign=center;imageVerticalAlign=middle;verticalLabelPosition=bottom;labelPosition=center;align=center;verticalAlign=top;spacingTop=12;spacingLeft=0;spacingRight=0;fontSize=16;labelWidth=230;whiteSpace=wrap;html=1;'
  elif id=='private_link':label='';style+='imageWidth=40;imageHeight=40;imageAlign=center;imageVerticalAlign=middle;'
  else:style+='imageWidth=36;imageHeight=36;imageAlign=left;imageVerticalAlign=middle;'
  row(id,label,box,style,parent(box),n['etiqueta'].replace('\n',' · '))
 header=[
  '## Arquitectura Ancoa: 79 componentes; 53 conexiones por familias; banda transversal izquierda.',
  '## Pegar TODO en Organizar > Insertar > Avanzado > CSV.',
  '## libavoid conserva la composición y ordena rutas; cada conexión usa orthogonalEdgeStyle.',
  '# identity: id','# namespace: ancoa-csv-','# label: %etiqueta%','# style: %estilo%',
  '# parent: parent','# parentstyle: %estilo%',
  '# left: x','# top: y','# width: @w','# height: @h',
  '# nodespacing: 55','# levelspacing: 100','# edgespacing: 20']
 for key,e,r,actual in zip(keys,s['enlaces'],routes,terminales):
  sem=e['semantica']
  d=CATALOGO['semanticas_enlace'][sem];st='edgeStyle=orthogonalEdgeStyle;orthogonalLoop=1;rounded=0;jettySize=auto;strokeWidth=2.2;strokeColor='+d['color']+';endArrow='+('none' if sem=='asociacion' else 'block')+';endFill=1;'
  if d['estilo']=='dashed':st+='dashed=1;'
  elif d['estilo']=='dotted':st+='dashed=1;dashPattern=2 5;'
  for prefix,port,terminal in [('exit',r['source'],actual[0]),('entry',r['target'],actual[1])]:
   ax,ay=port['anchor'];dx,dy=port['offset']
   if terminal in ports:ax=ay=.5;dx=dy=0
   st+=f'{prefix}X={ax};{prefix}Y={ay};{prefix}Dx={dx};{prefix}Dy={dy};{prefix}Perimeter=0;'
  header.append('# connect: '+json.dumps({'from':'a_'+key,'to':'id','style':st,'data':{'semantica':sem}},ensure_ascii=False,separators=(',',':')))
 header+=['# ignore: '+','.join(['estilo','x','y','w','h','parent']+['a_'+key for key in keys]),'# layout: libavoid']
 buf=io.StringIO(newline='');writer=csv.DictWriter(buf,list(rows[0]),lineterminator='\n');writer.writeheader();writer.writerows(rows)
 path=Path(str(salida)+'_conservar-capas.csv');path.write_text('\n'.join(header)+'\n'+buf.getvalue(),encoding='utf-8')
 manifest=dict(origen=str(origen),componentes=len(s['nodos']),filas=len(rows),enlaces=len(s['enlaces']),terminales=terminales,terminales_logicos=[(e['de'],e['a'],e['semantica']) for e in s['enlaces']],puertos=aliases,sha256_json=hashlib.sha256(origen.with_suffix('.json').read_bytes()).hexdigest(),archivo=str(path))
 Path(str(salida)+'_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 return manifest
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--origen',type=Path,required=True);p.add_argument('--salida',type=Path,required=True);a=p.parse_args();print(json.dumps(exportar(a.origen,a.salida),ensure_ascii=False))
