"""Exporta una especificación validada y su draw.io a CSV de importación nativa.

No cambia decisiones: conserva terminales, sentidos y semánticas del JSON. Los
estilos e iconos se toman del render ya validado y del catálogo Ancoa.
"""
import argparse,csv,hashlib,html,io,json,sys,xml.etree.ElementTree as ET
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'.agents/skills/diagramas-ancoa/scripts'))
from validar import validar
from _comun import CATALOGO

def geometria(c):
 g=c.find('mxGeometry')
 return tuple(float(g.get(k,'0')) for k in ['x','y','width','height'])

def exportar(origen,salida):
 spec=json.loads(origen.with_suffix('.json').read_text(encoding='utf-8'))
 errors,warnings=validar(spec)
 if errors or warnings:raise ValueError({'errores':errors,'avisos':warnings})
 cells={c.get('id'):c for c in ET.parse(origen.with_suffix('.drawio')).getroot().iter('mxCell')}
 nodes={n['id']:n for n in spec['nodos']}
 containers=[
 ('capa_1','1 · PRESENTACIÓN',(360,210,2280,210)),
 ('capa_2','2 · BORDE Y EXPOSICIÓN',(360,490,2280,190)),
 ('capa_3','3 · PUERTA DE ENLACE DE SERVICIOS',(360,780,2280,240)),
 ('capa_4','4 · SERVICIOS DE NEGOCIO',(360,1050,2280,800)),
 ('capa_5','5 · INTEGRACIÓN Y EVENTOS',(360,1920,2280,560)),
 ('capa_6','6 · DATOS',(360,2580,2280,940)),
 ('capa_7','7 · SEGURIDAD',(3220,210,350,3310)),
 ('capa_8','8 · OBSERVABILIDAD',(3590,210,350,3310)),
 ('tecnologias','BASE TECNOLÓGICA',(30,210,280,3310)),
 ('externos','SISTEMAS EXTERNOS',(2700,1120,470,1260)),
 ]
 if 'security_summary' in nodes:
  containers=[
   ('capa_1','1 · PRESENTACIÓN',(360,210,2280,210)),
   ('capa_2','2 · BORDE Y EXPOSICIÓN',(360,490,2280,190)),
   ('capa_3','3 · PUERTA DE ENLACE DE SERVICIOS',(360,780,2280,240)),
   ('capa_4','4 · SERVICIOS DE NEGOCIO',(360,1050,2280,800)),
   ('capa_5','5 · INTEGRACIÓN Y EVENTOS',(360,1920,2280,660)),
   ('capa_6','6 · DATOS',(360,2660,2280,1200)),
   ('capas_transversales','CAPAS TRANSVERSALES · 7 Seguridad / 8 Observabilidad',(30,3920,3140,270)),
   ('tecnologias','TECNOLOGÍAS Y GOBIERNO',(30,210,280,3650)),
   ('externos','SISTEMAS EXTERNOS',(2700,1120,470,1260)),
  ]
 sems=sorted({e['semantica'] for e in spec['enlaces']})
 special={('area_venta','local_serv'):('operacion_interna','condicionado','exitX=1;exitY=0.783;entryX=1;entryY=0.5;exitPerimeter=0;entryPerimeter=0;'),('area_venta','datos_venta'):('persistencia_venta','persistencia','exitX=1;exitY=0.97;entryX=1;entryY=0.5;exitPerimeter=0;entryPerimeter=0;')}
 keys=sems+[v[0] for v in special.values()]
 refs={i:{s:[] for s in keys} for i in list(nodes)+['area_mercaderia','area_venta','area_clientes','servicios_e']}
 for e in spec['enlaces']:
  key=special.get((e['de'],e['a']),(e['semantica'],))[0]
  refs[e['de']][key].append(e['a'])
 rows=[];boxes={i:g for i,_,g in containers}
 def row(id,label,parent,geo,style,layer='',area='',component='',status=''):
  x,y,w,h=geo
  if parent:px,py,_,_=boxes[parent];x-=px;y-=py
  r=dict(id=id,etiqueta=label,parent=parent,x=x,y=y,w=w,h=h,estilo=style,capa=layer,area=area,componente=component,estado=status)
  for sem in keys:r['a_'+sem]=','.join(refs.get(id,{}).get(sem,[]))
  rows.append(r)
 def frame_style(g):
  match=next((c for c in cells.values() if c.get('vertex')=='1' and geometria(c)==g and not c.get('id','').startswith('icon_')),None)
  if match is None:raise ValueError('No se encontró marco '+str(g))
  return match.get('style')+'container=1;transparentBounds=1;groupPadding=28;collapsible=0;recursiveResize=0;verticalAlign=top;align=center;spacingTop=0;fontStyle=1;fontSize=18;'
 title_cell=next(c for c in cells.values() if c.get('value')==spec['titulo'])
 legend_cell=next(c for c in cells.values() if c.get('value','').startswith(('Lectura:','Leyenda')))
 row('titulo',html.escape(spec['titulo']),'',(360,40,2280,90),title_cell.get('style'))
 legend='Leyenda: azul = API / solicitud; verde = persistencia propia; naranja = publicación; violeta = consumo; celeste = contrato externo.<br>Dorado punteado = gobierno; gris discontinuo = condicionado / por verificar. Verde claro = Retail; lila = Filial; amarillo = X-01.<br>A/C/E/P = auditoría, acceso, exportación y parámetros como diseño propuesto; * = pendiente. Un símbolo por producto conserva instancias por ámbito.'
 row('leyenda',legend,'',(360,4210 if 'security_summary' in nodes else 3550,2280,120),legend_cell.get('style')+'whiteSpace=wrap;html=1;')
 for id,label,g in containers:row(id,html.escape(label),'',g,frame_style(g),layer=id)
 names={'area_mercaderia':'MERCADERÍA','area_venta':'VENTA','area_clientes':'RELACIÓN CON EL CLIENTE','servicios_e':'CRÉDITO · FILIAL'}
 for id,label in names.items():
  boxes[id]=geometria(cells[id])
  style=cells[id].get('style')+'container=1;transparentBounds=1;groupPadding=28;collapsible=0;verticalAlign=top;align=left;spacingTop=6;spacingLeft=10;fontStyle=1;fontSize=16;'
  row(id,label,'capa_4',boxes[id],style,'capa_4',label)
 parents={}
 for id,n in nodes.items():
  x,y,w,h=geometria(cells[id]);cx,cy=x+w/2,y+h/2
  parent=next((cid for cid,_,(px,py,pw,ph) in containers if px<=cx<=px+pw and py<=cy<=py+ph),'')
  if id=='private_link':parent='capa_2'
  if not parent:raise ValueError('Nodo fuera de capa '+id)
  if n['grupo'] in names:parent=n['grupo']
  if id in ['conteo','busqueda','media']:parent='area_mercaderia'
  if id in ['local_serv','lockers']:parent='area_venta'
  if id=='fila':parent='area_clientes'
  parents[id]=parent
  style=cells[id].get('style')
  icon=cells.get('icon_'+id)
  if icon is not None:
   raw=icon.get('style');uri=raw.split('image=',1)[1].split(';',1)[0]
   style+='shape=label;image='+uri+';imageWidth=32;imageHeight=32;imageAlign=left;imageVerticalAlign=middle;imageSpacing=8;'
  label=cells[id].get('value') or html.escape(n['etiqueta']).replace('\n','<br>')
  layer=parent if parent.startswith('capa_') else 'capa_4' if parent in names else parent
  row(id,label,parent,(x,y,w,h),style,layer,names.get(parent,''),n['etiqueta'].split('\n')[0],n.get('estado','objetivo'))
 fields=list(rows[0])
 # El estilo del padre se evalúa sobre el propio padre, antes de borrar los
 # atributos ignorados. Así cada franja conserva su color del catálogo.
 header=[
 f'## Arquitectura Ancoa: {len(nodes)} componentes, 13 servicios vigentes + candidato, VPN conservada.',
 '## Pegar TODO el archivo en Organizar > Insertar > Avanzado > CSV.',
 '# identity: id','# namespace: ancoa-csv-','# label: %etiqueta%',
 '# style: %estilo%','# parent: parent','# parentstyle: %estilo%',
 '# left: x','# top: y','# width: @w','# height: @h',
 '# nodespacing: 70','# levelspacing: 140','# edgespacing: 20',
 ]
 definitions=[(v,v,'') for v in sems]+list(special.values())
 for key,sem,ports in definitions:
  d=CATALOGO['semanticas_enlace'][sem]
  st='edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;endArrow=block;endFill=1;strokeWidth=2.2;strokeColor='+d['color']+';'
  if d['estilo']=='dashed':st+='dashed=1;'
  elif d['estilo']=='dotted':st+='dashed=1;dashPattern=2 5;'
  st+=ports
  header.append('# connect: '+json.dumps(dict(**{'from':'a_'+key,'to':'id'},style=st,data={'semantica':sem}),ensure_ascii=False,separators=(',',':')))
 header.append('# ignore: '+','.join(['estilo','x','y','w','h','parent']+['a_'+x for x in keys]))
 table=io.StringIO(newline='');writer=csv.DictWriter(table,fields,lineterminator='\n');writer.writeheader();writer.writerows(rows)
 paths={}
 for mode,layout in [('auto','auto'),('conservar-capas','libavoid')]:
  path=Path(str(salida)+'_'+mode+'.csv');path.parent.mkdir(parents=True,exist_ok=True)
  path.write_text('\n'.join(header+['# layout: '+layout,'## ---- CSV ----'])+'\n'+table.getvalue(),encoding='utf-8')
  paths[mode]=str(path)
 manifest=dict(origen=str(origen),sha256_json=hashlib.sha256(origen.with_suffix('.json').read_bytes()).hexdigest(),componentes=len(nodes),contenedores=len(containers)+len(names),filas=len(rows),enlaces=len(spec['enlaces']),archivos=paths,semanticas=sems,terminales=[(e['de'],e['a'],e['semantica']) for e in spec['enlaces']],validacion='JSON válido sin avisos; importación draw.io se comprueba aparte')
 Path(str(salida)+'_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 return manifest

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 p.add_argument('--origen',type=Path,default=ROOT/'04_Adjuntos/diagramas/diag-04-31_arquitectura-servicios-y-flujos')
 p.add_argument('--salida',type=Path,default=ROOT/'04_Adjuntos/diagramas/diag-04-32_importacion-csv')
 a=p.parse_args();m=exportar(a.origen,a.salida);print(json.dumps({k:m[k] for k in ['componentes','contenedores','filas','enlaces','archivos']},ensure_ascii=False))
