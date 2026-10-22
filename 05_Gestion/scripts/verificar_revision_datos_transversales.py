"""Comprueba las tres vistas L2 y genera el draw.io con sus tres páginas."""
import hashlib,json,re,sys,xml.etree.ElementTree as ET
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'.agents/skills/diagramas-ancoa/scripts'))
from validar import validar
from router_horizontal import segmento_libre
from _comun import frente_de_nodo

OUT=ROOT/'04_Adjuntos/diagramas';REPORT=ROOT/'80_Artefactos/sd-04_contexto/actualizacion-datos-transversales-2026-10-22'
STEMS=['diag-04-33_arquitectura-datos-transversales','diag-04-34_detalle-datos','diag-04-35_detalle-transversales']

def main():
 results=[];specs=[];book=ET.Element('mxfile',host='diagramas-ancoa',type='device')
 for stem,page in zip(STEMS,['1 · Arquitectura por capas','2 · Datos, gobierno y modelos','3 · Capas transversales']):
  p=OUT/stem;s=json.loads(p.with_suffix('.json').read_text(encoding='utf-8'));specs.append(s)
  errors,warnings=validar(s);assert not errors and not warnings,(errors,warnings)
  doc=ET.parse(p.with_suffix('.drawio')).getroot();diagram=doc.find('diagram');diagram.set('name',page);diagram.set('id',stem);book.append(diagram)
  cells={c.get('id'):c for c in doc.iter('mxCell')};boxes=[]
  # diagram fue añadido al nuevo árbol, pero ElementTree conserva el original.
  for n in s['nodos']:
   g=cells[n['id']].find('mxGeometry');x,y,w,h=[float(g.get(k)) for k in ['x','y','width','height']];boxes.append((x,y,x+w,y+h))
  for i,a in enumerate(boxes):
   for j,b in enumerate(boxes[:i]):
    assert not(max(a[0],b[0])<min(a[2],b[2]) and max(a[1],b[1])<min(a[3],b[3])),('Tarjetas superpuestas',stem,i,j)
  routes=json.loads(p.with_suffix('.rutas.json').read_text(encoding='utf-8'))
  svg=ET.parse(p.with_suffix('.svg')).getroot();ns={'s':'http://www.w3.org/2000/svg'}
  paths=[path for path in svg.findall('s:path',ns) if path.find('s:title',ns) is not None]
  assert len(routes)==len(s['enlaces'])==len(paths)
  groups={g['id']:g for g in s['grupos']};nodes={n['id']:n for n in s['nodos']}
  for i,(e,r,path) in enumerate(zip(s['enlaces'],routes,paths)):
   points=[tuple(p) for p in r['points']]
   assert all(a[0]==b[0] or a[1]==b[1] for a,b in zip(points,points[1:]))
   assert all(segmento_libre(a,b,boxes) for a,b in zip(points,points[1:])),('Tarjeta atravesada',stem,i)
   sg=[tuple(map(float,point.split(','))) for point in re.findall(r'[-\d.]+,[-\d.]+',path.get('d'))];assert sg==points,('SVG distinto',stem,i)
   xml=cells['edge'+str(i)];style=dict(v.split('=',1) for v in xml.get('style').split(';') if '=' in v)
   assert xml.get('source')==e['de'] and xml.get('target')==e['a']
   assert [(float(v.get('x')),float(v.get('y'))) for v in xml.findall('mxGeometry/Array/mxPoint')]==points[1:-1]
   for prefix in ['entry','exit']:assert float(style[prefix+'X']) in (0,1) or float(style[prefix+'Y']) in (0,1)
   front=lambda id:frente_de_nodo(nodes.get(id,{'grupo':id}),groups)
   assert {front(e['de']),front(e['a'])}!={'retail','emisor'},('Cruce directo',stem,i)
  results.append(dict(vista=stem,nodos=len(s['nodos']),conectores=len(routes),errores_validacion=0,avisos=0,solapamientos_tarjetas=0,tarjetas_atravesadas=0,rutas_svg_drawio_coinciden=True))
 principal,data,trans=specs;nodes={n['id']:n for n in principal['nodos']}
 assert len([n for n in principal['nodos'] if n.get('codigo','').startswith(('R:','F:','X-01')) and n['id']!='regulatorio'])==13
 assert nodes['regulatorio']['codigo']=='F:C-04' and nodes['regulatorio']['estado']=='por_acreditar'
 assert not any(e['de']=='regulatorio' or e['a']=='regulatorio' for e in principal['enlaces'])
 assert {'conteo','lockers','busqueda','media','fila'}<=set(nodes)
 assert all(sum(n['id']==id for n in principal['nodos'])==1 for id in ['front_door','application_gateway','api_management','api_center'])
 assert 'VPN' in nodes['entrada_privada']['etiqueta']
 assert not any(n['grupo'].startswith('actores') for n in principal['nodos'])
 for spec in specs:
  for n in spec['nodos']:
   assert not any(x in n['etiqueta'] for x in ['Purview','Databricks','Azure AI Search','Fabric','Synapse','Azure Managed Grafana'])
 pairs=lambda spec:{(e['de'],e['a']) for e in spec['enlaces']}
 for d in ['r','e']:
  assert ('bi_'+d,'mart_'+d) in pairs(data)
  assert not any(e['de']=='bi_'+d and e['a']!='mart_'+d for e in data['enlaces'])
  assert ('otel_'+d,'monitor_'+d) not in pairs(trans)
  for target in ['prom','loki','tempo']:assert ('otel_'+d,target+'_'+d) in pairs(trans)
  for target in ['prom','loki','tempo','monitor']:assert ('grafana_'+d,target+'_'+d) in pairs(trans)
  for a,b in [('admin','private'),('private','resources'),('admin','bastion'),('bastion','resources'),('bastion','stage'),('stage','audit'),('audit','worm')]:assert (a+'_'+d,b+'_'+d) in pairs(trans)
  assert not any(e['de']=='pim_'+d and e['semantica']=='solicitud' for e in trans['enlaces'])
  assert ('x01','audit_'+d) in pairs(trans) and ('x01','otel_'+d) in pairs(trans)
 protected=json.loads((REPORT/'hashes-antes.json').read_text(encoding='utf-8'))
 changed=[p for p,h in protected.items() if hashlib.sha256((ROOT/p).read_bytes()).hexdigest()!=h]
 assert not changed,('Fuentes protegidas cambiaron',changed)
 ET.ElementTree(book).write(OUT/'diag-04-33_arquitectura-actualizada.drawio',encoding='utf-8',xml_declaration=True)
 report=dict(vistas=results,paginas_drawio=3,servicios_vigentes=13,candidato_separado='F:C-04',innovaciones=5,capas=8,banda_compartida='Capas transversales: 7 Seguridad y 8 Observabilidad',archivos_protegidos_verificados=len(protected),archivos_protegidos_alterados=[],alcance='Comprobaciones documentales y gráficas; no pruebas de una plataforma Azure desplegada.')
 (REPORT/'verificacion.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
