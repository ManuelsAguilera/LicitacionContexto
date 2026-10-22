"""Variante L2 autorizada por el usuario: cinco columnas con iconos y ocho capas RT.

La geometría pertenece a la plantilla; el cliente solo aporta componentes y enlaces JSON.
Los iconos se incrustan desde el catálogo local. SVG autocontenido y PNG vía Inkscape.
"""
import json
from router_ortogonal import enrutar
import base64
import html
import importlib
from pathlib import Path
import shutil
import subprocess
import textwrap
import xml.etree.ElementTree as ET
from _comun import CATALOGO, RAIZ, frente_de_nodo, leyenda

W, H = 2540, 2120
COLS = [(30,340),(410,340),(800,510),(1380,490),(1940,570)]
TEXT = '#1A1A1A'
SLOTS = {
 'presentacion_r':(45,235,310,126,5,1),
 'borde_r':(425,240,310,110,1,1),'api_r':(425,410,310,220,1,1),
 'contratos_r':(425,600,310,140,3,1),
 'servicios_r':(815,235,480,55,9,1),'innovaciones':(815,770,480,70,5,1),
 'datos_r':(1955,235,540,55,12,1),
 'frontera':(1920,1810,570,100,1,1),'datos_x':(1955,1640,540,95,1,1),
 'presentacion_e':(45,1360,310,130,2,1),
 'borde_e':(425,1360,310,100,1,1),'api_e':(425,1510,310,110,1,1),
 'servicios_e':(815,1360,480,90,3,1),'datos_e':(1955,1360,540,90,3,1),
 'integracion_r':(1395,1080,460,125,3,1),'integracion_e':(1395,1540,460,115,2,1),
 'externos':(45,1195,470,80,5,5),
 'seguridad':(45,1810,600,90,3,3),'observabilidad':(45,1920,810,70,3,3),
 'tecnologias':(45,2030,340,55,7,7),
}


def icono_data(tipo):
    ruta = CATALOGO['tipos_nodo_logicos'][tipo].get('icono')
    if not ruta:
        raise ValueError('La composición requiere icono para cada componente: '+tipo)
    if ruta.startswith('assets/'):
        path = RAIZ/ruta
    else:
        module, name = ruta.rsplit('.',1)
        cls = getattr(importlib.import_module(module),name)
        path = Path(cls._load_icon(cls.__new__(cls)))
    return 'data:image/png;base64,'+base64.b64encode(path.read_bytes()).decode('ascii')


def renderizar(spec, salida):
    out=Path(salida); out.parent.mkdir(parents=True,exist_ok=True)
    gpid={g['id']:g for g in spec['grupos']}
    nodes=spec['nodos']; pos={}; svg=[]; panels=[]
    def rect(x,y,w,h,fill,stroke,rx=8,dash=False):
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.4"'+(' stroke-dasharray="7 4"' if dash else '')+'/>')
    def txt(x,y,t,size=17,bold=False,fill=TEXT,anchor='start'):
        svg.append(f'<text x="{x}" y="{y}" font-family="Segoe UI,Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{fill}" text-anchor="{anchor}">{html.escape(t)}</text>')
    def label(x,y,lines,size=17,bold=False,anchor='start'):
        for i,t in enumerate(lines):txt(x,y+i*(size+5),t,size,bold,anchor=anchor)
    def panel(x,y,w,h,title,sub=None):
        panels.append((x,y,w,h,title,sub))
        pal=CATALOGO['frentes']['transversal'];rect(x,y,w,h,pal['relleno'],pal['borde'])
        rect(x+8,y+8,w-16,42,CATALOGO['frentes']['emisor']['caja'],pal['borde'],5)
        txt(x+w/2,y+35,title,21,True,anchor='middle')
        if sub:txt(x+w/2,y+72,sub,16,anchor='middle')
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
    svg.append('<defs><marker id="flecha" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L7,3 L0,6 Z" fill="context-stroke"/></marker></defs>')
    rect(0,0,W,H,'#FFFFFF','#FFFFFF',0)
    txt(35,40,'ONLY SIMPLE SOLUTIONS  /  MULTITIENDAS ANCOA',21,True)
    txt(35,77,spec['titulo'],29,True)
    txt(35,106,'Arquitectura objetivo · servicios, integración y persistencia · Retail y Emisor separados · RT-02.01',18)
    headings=[('Capa de Presentación','1 · Canales de atención'),('Capa de Negocios','2 · Borde / 3 · Puerta de enlace'),('Capa de Servicios','4 · Funciones e innovaciones'),('Integración y Eventos','5 · Adaptadores y canales propios'),('Capa de Datos','6 · Autoridad por servicio')]
    for (x,w),(title,sub) in zip(COLS,headings):
        panel(x,140,w,1630,title,sub)
        pal=CATALOGO['frentes']['emisor']
        rect(x+5,1300,w-10,463,pal['relleno'],pal['borde'],5)
    txt(45,230,'RETAIL',17,True);txt(45,1335,'EMISOR',17,True)
    txt(815,745,'Innovaciones y capacidades asociadas',18,True)
    txt(1625,730,'Persistencia directa',19,True,anchor='middle')
    txt(1625,760,'Cada servicio accede a sus datos.',17,anchor='middle')
    txt(1625,790,'El bus no intermedia consultas ni escrituras.',16,anchor='middle')
    txt(1395,810,'Publicación, consumo y adaptadores',18,True)
    txt(45,1145,'Salida transaccional por productor; consumidores idempotentes.',16)
    txt(45,1170,'Repositorios lógicos por autoridad · nube principal + persistencia local.',16)
    for key,(x,y,w,step,limit,columns) in SLOTS.items():
        selected=[n for n in nodes if n.get('grupo')==key]
        if len(selected)>limit:raise ValueError(f'{key}: {len(selected)} componentes superan {limit} huecos de plantilla')
        for i,n in enumerate(selected):
            xx=x+i*(w+28) if columns>1 else x
            yy=y if columns>1 else y+i*step
            hh=step-12 if columns==1 else step
            if key=='servicios_r':hh=43
            if key=='innovaciones':hh=60
            if key=='actores_r' or key=='actores_e':hh=83
            if n['id'] in ('datos_lectura','lago_r','local_data'):
                yy={'datos_lectura':830,'lago_r':955,'local_data':1090}[n['id']];hh=88
            if n['id']=='adapt_r':hh=90
            if n['id']=='adapt_e':hh=84
            if n['id']=='event_r':yy=835;hh=210
            if n['id']=='event_e':hh=102
            pos[n['id']]=(xx,yy,w,hh)
    txt(35,1190,'Sistemas conservados y servicios externos',18,True)
    txt(35,1800,'7 · Seguridad transversal',18,True)
    txt(35,1910,'8 · Observabilidad transversal',18,True)
    txt(35,2020,'Tecnologías propuestas · * selección por verificar',17,True)
    for i,(sem,name) in enumerate([('solicitud','Solicitud / API'),('persistencia','Acceso a datos'),('publicacion','Publica evento'),('consumo','Consume evento'),('adaptacion','Sistema externo')]):
        lx=35+i*414;color=CATALOGO['semanticas_enlace'][sem]['color']
        svg.append(f'<path d="M{lx},123 L{lx+28},123" stroke="{color}" stroke-width="3" marker-end="url(#flecha)"/>')
        txt(lx+40,129,name,16,True,fill=color)
    # Puertos fijos en el contorno; mismos codos y puntos en PNG/SVG y draw.io.
    text_obstacles=[(0,0,W,225),(810,724,1310,752),(1405,708,1860,798),
                    (1390,798,1860,819),(35,1125,620,1175),(35,1175,630,1192),
                    (35,1317,180,1340),(35,1780,500,1804),(35,1890,570,1914),
                    (35,2000,670,2024),(35,2085,W,2120)]
    routes=enrutar(pos,spec.get('enlaces',[]),text_obstacles)
    for a,route in zip(spec.get('enlaces',[]),routes):
        sem=CATALOGO['semanticas_enlace'][a['semantica']]
        points=route['points']
        d='M'+ ' L'.join(f'{x},{y}' for x,y in points)
        svg.append(f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-width="5" opacity="0.8"/>')
        svg.append(f'<path d="{d}" fill="none" stroke="{sem["color"]}" stroke-width="2.2" opacity="0.95" marker-end="url(#flecha)"><title>{html.escape(a.get("etiqueta",""))}</title></path>')
    out.with_suffix('.rutas.json').write_text(json.dumps([dict(enlace=e,**r) for e,r in zip(spec['enlaces'],routes)],ensure_ascii=False,indent=2),encoding='utf-8')
    for n in nodes:
        x,y,w,h=pos[n['id']]; frente=frente_de_nodo(n,gpid) or 'transversal';pal=CATALOGO['frentes']['transversal' if frente=='frontera' else frente]
        pending=n.get('estado')=='por_acreditar'
        rect(x,y,w,h,pal['caja'],pal['borde'],7,pending)
        size=23 if h<40 else 37 if h<76 else 44
        href=icono_data(n['tipo'])
        svg.append(f'<image x="{x+9}" y="{y+(h-size)/2}" width="{size}" height="{size}" href="{href}"/>')
        raw=n['etiqueta'].split('\n')
        compacto = h<40
        if compacto:
            raw=[n['etiqueta'].replace('\n',' · ')]
        maxchars=max(14,int((w-size-32)/8.3))
        lines=[]
        for line in raw:lines.extend(textwrap.wrap(line,width=maxchars,break_long_words=False) or [''])
        if pending:lines[-1]+=' *'
        fs=16 if w>180 else 15
        if len(lines)*(fs+4)>h-7:fs=14
        if len(lines)*(fs+4)>h:raise ValueError('Texto no cabe: '+n['id'])
        top=y+(h-len(lines)*(fs+4))/2+fs
        for j,line in enumerate(lines):txt(x+size+20,top+j*(fs+4),line,fs,j==0)
    txt(35,2105,'Fuente: elaboración propia · main@1e097c2 y decisiones aceptadas · SD-03 intacto · códigos conservados en JSON · * selección por verificar.',16)
    svg.append('</svg>')
    svg_path=out.with_suffix('.svg');svg_path.write_text('\n'.join(svg),encoding='utf-8')
    exe=shutil.which('inkscape') or 'C:/Program Files/Inkscape/bin/inkscape.com'
    subprocess.run([exe,str(svg_path),'--export-type=png','--export-filename='+str(out.with_suffix('.png')),'--export-width=3810'],check=True,capture_output=True,timeout=60)
    # Fuente editable por objetos para draw.io; cada icono queda incluido en el XML.
    mx=ET.Element('mxfile',host='diagramas-ancoa',type='device')
    diagram=ET.SubElement(mx,'diagram',name='Arquitectura por capas')
    model=ET.SubElement(diagram,'mxGraphModel',page='0',grid='1',gridSize='10')
    root=ET.SubElement(model,'root');ET.SubElement(root,'mxCell',id='0');ET.SubElement(root,'mxCell',id='1',parent='0')
    def cell(id,value,style,x,y,w,h,parent='1'):
        c=ET.SubElement(root,'mxCell',id=id,value=value,style=style,vertex='1',parent=parent)
        ET.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
    for i,(x,y,w,h,title,sub) in enumerate(panels):
        pal=CATALOGO['frentes']['transversal']
        cell('panel'+str(i),title+('<br>'+sub if sub else ''),
             f'rounded=0;html=1;verticalAlign=top;spacingTop=10;fontStyle=1;fontSize=20;fillColor={pal["relleno"]};strokeColor={pal["borde"]};',x,y,w,h)
    for n in nodes:
        x,y,w,h=pos[n['id']];pal=CATALOGO['frentes']['transversal' if frente_de_nodo(n,gpid)=='frontera' else frente_de_nodo(n,gpid) or 'transversal']
        text=html.escape(n['etiqueta']).replace('\n','<br>')
        cell(n['id'],text,f'rounded=1;html=1;whiteSpace=wrap;align=left;verticalAlign=middle;spacingLeft=62;fontSize=16;fillColor={pal["caja"]};strokeColor={pal["borde"]};'+('dashed=1;' if n.get('estado')=='por_acreditar' else ''),x,y,w,h)
        size=23 if h<40 else 37 if h<76 else 44
        uri=icono_data(n['tipo']).replace(';base64,',',')
        cell('icon_'+n['id'],'','shape=image;imageAspect=1;aspect=fixed;image='+uri+';',9,(h-size)/2,size,size,n['id'])
    for i,(a,route) in enumerate(zip(spec.get('enlaces',[]),routes)):
        sem=CATALOGO['semanticas_enlace'][a['semantica']]
        sx,sy=route['source']['anchor'];tx,ty=route['target']['anchor']
        sdx,sdy=route['source']['offset'];tdx,tdy=route['target']['offset']
        c=ET.SubElement(root,'mxCell',id='edge'+str(i),value='',edge='1',parent='1',source=a['de'],target=a['a'],
                        style=f'edgeStyle=none;orthogonal=1;rounded=0;endArrow=block;endFill=1;strokeColor={sem["color"]};strokeWidth=2.2;exitX={sx};exitY={sy};entryX={tx};entryY={ty};exitDx={sdx};exitDy={sdy};entryDx={tdx};entryDy={tdy};exitPerimeter=0;entryPerimeter=0;')
        c.set('tooltip',a['etiqueta'])
        geo=ET.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'})
        waypoints=ET.SubElement(geo,'Array',attrib={'as':'points'})
        for px,py in route['points'][1:-1]:ET.SubElement(waypoints,'mxPoint',x=str(px),y=str(py))
        for name,pt in [('sourcePoint',route['points'][0]),('targetPoint',route['points'][-1])]:
            ET.SubElement(geo,'mxPoint',x=str(pt[0]),y=str(pt[1]),attrib={'as':name})
    cell('legend','Leyenda: azul API; verde persistencia; naranja publica; violeta consume; celeste contrato externo. Discontinuo: por verificar.',
         'text;html=1;fontSize=16;align=left;',35,2075,2460,25)
    cell('source','Fuente: '+html.escape(spec['fuente']),'text;html=1;fontSize=14;align=left;',35,2100,2460,20)
    edges=[c for c in root if c.get('edge')=='1']
    for c in edges:root.remove(c)
    for i,c in enumerate(edges):root.insert(2+len(panels)+i,c)
    ET.ElementTree(mx).write(out.with_suffix('.drawio'),encoding='utf-8',xml_declaration=True)
    out.with_suffix('.leyenda.txt').write_text('Figura '+str(spec.get('figura','4.N'))+': '+spec['titulo']+'\nFuente: '+spec['fuente']+'\n\n'
        +'Columnas: Presentación, Negocios, Servicios, Integración y Eventos, Datos.\n'
        +'Capas RT: 1 Presentación; 2 Borde; 3 Puerta de enlace; 4 Servicios; 5 Integración; 6 Datos; 7 Seguridad; 8 Observabilidad.\n'
        +'Verde: Retail. Lila: Emisor. Gris azulado: controles separados por ámbito. Flechas: azul API; verde persistencia; naranja publicación; violeta consumo; celeste contratos externos.\n'
        +'Borde discontinuo y *: selección por verificar, conservando el icono del producto de referencia.\n'
        +'Puertos explícitos en los bordes; rutas rectangulares con puntos intermedios comunes a SVG y draw.io.\n'
        +'Las conexiones resumen contratos lógicos; los cruces no dibujados permanecen denegados.\n',encoding='utf-8')
    return out
