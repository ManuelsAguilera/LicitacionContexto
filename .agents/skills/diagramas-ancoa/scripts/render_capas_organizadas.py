"""L2 de seis columnas, actores externos y productos con iconos de catálogo."""
import html
import json
from pathlib import Path
import shutil
import subprocess
import textwrap
import xml.etree.ElementTree as ET
from _comun import CATALOGO, frente_de_nodo
from render_capas_referencia import icono_data
from router_ortogonal import enrutar

W,H=3000,2230
COLS=[(30,270),(340,340),(720,300),(1060,330),(1430,540),(2010,430),(2480,490)]


def posiciones(spec):
    pos={}
    def put(ids,x,y,w,h,step):
        for i,id in enumerate(ids):pos[id]=(x,y+i*step,w,h)
    put(['a_cliente','a_venta','a_inventario','a_cd','a_comercial'],45,310,240,95,130)
    put(['web','pos','operacion','logistica','movil'],355,310,310,95,130)
    pos['a_vendedor']=(45,1010,240,95);pos['portal']=(355,1010,310,95)
    pos['typescript']=(355,1150,145,70);pos['react_ui']=(520,1150,145,70)
    pos['borde_r']=(735,370,270,105);pos['appgw_r']=(735,560,270,105)
    pos['apim_r']=(1075,490,300,190)
    pos['aks_r']=(1445,300,510,58)
    put(['oferta','abastecimiento','existencias','pedidos','ventas','comisiones','market','posventa','clientes'],1445,380,510,43,55)
    put(['conteo','lockers','busqueda','media','fila'],1445,960,510,45,52)
    pos['event_r']=(2025,930,400,180);pos['adapt_r']=(2025,1140,400,100)
    pos['datos_merc']=(2495,355,460,110);pos['datos_venta']=(2495,505,460,115)
    pos['datos_clientes']=(2495,660,460,100)
    pos['datos_lectura']=(2495,795,460,75);pos['redis']=(2495,895,460,70)
    pos['lago_r']=(2495,990,460,75);pos['powerbi']=(2495,1090,460,55)
    pos['local_data']=(2495,1170,460,75)
    pos['x01']=(1445,1280,980,70);pos['bitacora']=(2495,1280,460,70)
    put(['a_titular','a_ejecutivo'],45,1440,240,90,140)
    put(['portal_f','meson_f'],355,1440,310,90,140)
    pos['borde_e']=(735,1440,270,105);pos['appgw_e']=(735,1610,270,105)
    pos['apim_e']=(1075,1510,300,150);pos['aks_e']=(1445,1430,510,50)
    put(['originacion','cartera','evidencia'],1445,1505,510,55,80)
    pos['event_e']=(2025,1505,400,105);pos['adapt_e']=(2025,1660,400,75)
    pos['datos_orig']=(2495,1445,460,65);pos['datos_cartera']=(2495,1525,460,65)
    pos['datos_evid']=(2495,1605,460,65);pos['lake_e']=(2495,1690,460,65)
    put(['erp','wms','plataforma_market','ads','controlador'],355,1810,492,70,0)
    for i,id in enumerate(['erp','wms','plataforma_market','ads','controlador']):pos[id]=(355+i*524,1810,492,70)
    for i,id in enumerate(['entra','kv','hsm','zero','ddos']):pos[id]=(355+i*524,1940,492,75)
    for i,id in enumerate(['otel','monitor','vnet']):pos[id]=(355+i*880,2080,852,70)
    pos['a_auditoria']=(45,1940,240,75)
    pos['front_door']=(735,820,270,95)
    pos['application_gateway']=(735,980,270,95)
    pos['api_management']=(1120,820,255,130)
    pos['private_link']=(1040,860,40,40)
    missing={n['id'] for n in spec['nodos']}-set(pos)
    if missing:raise ValueError('Componentes sin ranura: '+str(missing))
    return {n['id']:pos[n['id']] for n in spec['nodos']}


def renderizar(spec,salida):
    out=Path(salida);out.parent.mkdir(parents=True,exist_ok=True)
    pos=posiciones(spec);groups={g['id']:g for g in spec['grupos']}
    svg=[];background=[];texts=[];cards=[];icons=[];obstacles=[]
    pal=CATALOGO['frentes']
    def rect(x,y,w,h,fill,stroke,rx=7,dash=False,record=True):
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.3"'+(' stroke-dasharray="7 4"' if dash else '')+'/>')
        if record:background.append(('',f'rounded=1;arcSize=8;fillColor={fill};strokeColor={stroke};',x,y,w,h))
    def text(x,y,s,size=18,bold=False,anchor='start',color='#1A1A1A',record=True):
        svg.append(f'<text x="{x}" y="{y}" font-family="Segoe UI,Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" text-anchor="{anchor}" fill="{color}">{html.escape(s)}</text>')
        if record:
            width=max(45,len(s)*size*.59+12)
            texts.append((s,f'text;html=0;align={"center" if anchor=="middle" else "left"};fontSize={size};fontColor={color};fontStyle={1 if bold else 0};',x-width/2 if anchor=='middle' else x,y-size,width,size+7))
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
    svg.append('<defs><marker id="flecha" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L7,3 L0,6 Z" fill="context-stroke"/></marker></defs>')
    rect(0,0,W,H,'#FFFFFF','#FFFFFF',0)
    text(30,38,'ONLY SIMPLE SOLUTIONS / MULTITIENDAS ANCOA',21,True)
    text(30,78,spec['titulo'],30,True)
    text(30,108,'Modelo objetivo · productos propuestos y ámbitos separados · nombres funcionales sin códigos visibles',18)
    # Franjas de capa: límites lógicos continuos, distintos de la segmentación de red.
    for i,(x,w) in enumerate(COLS[1:]):
        fill=pal['azure']['relleno'] if i%2==0 else pal['transversal']['relleno']
        rect(x,150,w,1738,fill,pal['transversal']['borde'])
    rect(340,1895,2630,135,pal['azure']['relleno'],pal['transversal']['borde'])
    rect(340,2035,2630,130,pal['transversal']['relleno'],pal['transversal']['borde'])
    headers=[['ACTORES','Fuera de las ocho capas'],['1 · PRESENTACIÓN'],['2 · BORDE Y','EXPOSICIÓN'],['3 · PUERTA DE ENLACE','DE SERVICIOS'],['4 · SERVICIOS DE NEGOCIO'],['5 · INTEGRACIÓN','Y EVENTOS'],['6 · DATOS']]
    for (x,w),lines in zip(COLS,headers):
        rect(x,150,w,73,pal['transversal']['caja'],pal['transversal']['borde'])
        for j,line in enumerate(lines):text(x+w/2,180+j*24,line,18 if j==0 else 17,True,anchor='middle')
    # Ámbitos distinguidos por franjas, dejando continuas las columnas de productos agrupados.
    for y,name,front in [(245,'RETAIL','retail'),(1380,'FILIAL EMISORA','emisor')]:
        p=pal[front]
        rect(340,y,340,45,p['caja'],p['borde'])
        rect(1430,y,1540,45,p['caja'],p['borde'])
        text(2200,y+29,name,19,True,anchor='middle')
        obstacles.extend([(335,y-4,685,y+49),(1430,y-4,2975,y+49)])
    text(1445,935,'Innovaciones dentro de sus servicios responsables',17,True)
    obstacles.append((1440,915,1970,943))
    text(2025,355,'Acceso directo a datos',19,True)
    text(2025,383,'El canal de eventos no intermedia',16)
    text(2025,407,'la persistencia de los servicios.',16)
    obstacles.append((2020,335,2440,417))
    text(2025,855,'Salida transaccional por productor.',16)
    text(2025,879,'Consumo idempotente y reintentos.',16)
    text(2025,903,'Canales separados por ámbito.',16)
    obstacles.append((2020,835,2440,913))
    text(355,1788,'SISTEMAS CONSERVADOS Y SERVICIOS EXTERNOS · conexiones mediante adaptadores del ámbito correspondiente',18,True)
    obstacles.append((350,1765,2970,1798))
    text(355,1920,'7 · SEGURIDAD TRANSVERSAL · recursos y permisos separados por ámbito',19,True)
    obstacles.append((350,1898,2970,1930))
    text(355,2060,'8 · OBSERVABILIDAD TRANSVERSAL · telemetría separada por ámbito',19,True)
    obstacles.append((350,2038,2970,2070))
    text(30,2190,'Lectura: símbolos agrupados por producto, sin fusionar instancias, redes ni contratos. Las franjas de color distinguen los ámbitos.',17)
    text(30,2217,'Fuente: elaboración propia desde SD-03/04/13 y T-11/T-14 main@1e097c2; nueva referencia del usuario. * Selección por verificar. SD-03 intacto.',16)
    obstacles.extend([(0,0,W,230),(0,2160,W,2230)])
    if any(n['id']=='private_link' for n in spec['nodos']):obstacles.append((965,975,1155,1025))
    # Carriles libres en las separaciones entre columnas y en las bandas de ámbito.
    routes=enrutar(pos,spec['enlaces'],obstacles)
    for e,r in zip(spec['enlaces'],routes):
        color=CATALOGO['semanticas_enlace'][e['semantica']]['color']
        d='M'+' L'.join(f'{x},{y}' for x,y in r['points'])
        svg.append(f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-width="5"/>')
        svg.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.2" marker-end="url(#flecha)"><title>{html.escape(e["etiqueta"])}</title></path>')
    for n in spec['nodos']:
        x,y,w,h=pos[n['id']];f=frente_de_nodo(n,groups) or 'transversal'
        p=pal['transversal' if f=='frontera' else f];pending=n.get('estado')=='por_acreditar'
        rect(x,y,w,h,p['caja'],p['borde'],dash=pending,record=False)
        if n['id']=='private_link':
            # Símbolo de conectividad sobre el enlace; sin caja de gateway adicional.
            svg.pop()  # retirar el rectángulo que se acaba de añadir para este nodo
            uri=icono_data(n['tipo'])
            svg.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{uri}"/>')
            text(x+w/2,995,'Azure Private Link',15,True,anchor='middle')
            text(x+w/2,1016,'Private Endpoint *',14,anchor='middle')
            cards.append((n['id'],'','fillColor=none;strokeColor=none;',x,y,w,h))
            icons.append(('icon_'+n['id'],'','shape=image;imageAspect=1;image='+uri.replace(';base64,',',')+';',x,y,w,h))
            continue
        size=27 if h<50 else 38 if h<80 else 48
        uri=icono_data(n['tipo'])
        svg.append(f'<image x="{x+10}" y="{y+(h-size)/2}" width="{size}" height="{size}" href="{uri}"/>')
        lines=[]
        for line in n['etiqueta'].split('\n'):
            lines.extend(textwrap.wrap(line,width=max(12,int((w-size-35)/8.6)),break_long_words=False) or [''])
        if pending:lines[-1]+=' *'
        fs=17 if w>350 else 16
        if len(lines)*(fs+4)>h-6:fs=14
        if len(lines)*(fs+4)>h:raise ValueError('Texto no cabe: '+n['id'])
        top=y+(h-len(lines)*(fs+4))/2+fs
        for j,line in enumerate(lines):text(x+size+22,top+j*(fs+4),line,fs,j==0,record=False)
        cards.append((n['id'],html.escape(n['etiqueta']).replace('\n','<br>')+(' *' if pending else ''),f'rounded=1;whiteSpace=wrap;html=1;align=left;verticalAlign=middle;spacingLeft={size+22};fontSize={fs};fillColor={p["caja"]};strokeColor={p["borde"]};'+('dashed=1;' if pending else ''),x,y,w,h))
        icons.append(('icon_'+n['id'],'','shape=image;imageAspect=1;image='+uri.replace(';base64,',',')+';',x+10,y+(h-size)/2,size,size))
    text(30,131,'Leyenda',16,True)
    for i,(sem,name) in enumerate([('solicitud','API / solicitud'),('persistencia','Persistencia propia'),('publicacion','Publicación'),('consumo','Consumo'),('adaptacion','Contrato externo')]):
        x=400+i*520;color=CATALOGO['semanticas_enlace'][sem]['color']
        svg.append(f'<path d="M{x},125 L{x+30},125" stroke="{color}" stroke-width="3" marker-end="url(#flecha)"/>')
        text(x+42,131,name,16,True,color=color)
    svg.append('</svg>');out.with_suffix('.svg').write_text('\n'.join(svg),encoding='utf-8')
    exe=shutil.which('inkscape') or 'C:/Program Files/Inkscape/bin/inkscape.com'
    subprocess.run([exe,str(out.with_suffix('.svg')),'--export-type=png','--export-filename='+str(out.with_suffix('.png')),'--export-width=4500'],check=True,capture_output=True,timeout=60)
    mx=ET.Element('mxfile',host='diagramas-ancoa',type='device');dg=ET.SubElement(mx,'diagram',name='Capas y servicios de plataforma')
    model=ET.SubElement(dg,'mxGraphModel',page='0',grid='1',gridSize='10');root=ET.SubElement(model,'root')
    ET.SubElement(root,'mxCell',id='0');ET.SubElement(root,'mxCell',id='1',parent='0')
    def cell(id,value,style,x,y,w,h):
        c=ET.SubElement(root,'mxCell',id=id,value=value,style=style,vertex='1',parent='1')
        ET.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
    for i,o in enumerate(background):cell('background'+str(i),*o)
    for i,(e,r) in enumerate(zip(spec['enlaces'],routes)):
        color=CATALOGO['semanticas_enlace'][e['semantica']]['color']
        sx,sy=r['source']['anchor'];tx,ty=r['target']['anchor'];sdx,sdy=r['source']['offset'];tdx,tdy=r['target']['offset']
        c=ET.SubElement(root,'mxCell',id='edge'+str(i),value='',edge='1',parent='1',source=e['de'],target=e['a'],tooltip=e['etiqueta'],style=f'edgeStyle=none;orthogonal=1;rounded=0;endArrow=block;endFill=1;strokeColor={color};strokeWidth=2.2;exitX={sx};exitY={sy};entryX={tx};entryY={ty};exitDx={sdx};exitDy={sdy};entryDx={tdx};entryDy={tdy};exitPerimeter=0;entryPerimeter=0;')
        geo=ET.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'});arr=ET.SubElement(geo,'Array',attrib={'as':'points'})
        for x,y in r['points'][1:-1]:ET.SubElement(arr,'mxPoint',x=str(x),y=str(y))
    for o in cards+icons:cell(*o)
    for i,o in enumerate(texts):cell('text'+str(i),*o)
    ET.ElementTree(mx).write(out.with_suffix('.drawio'),encoding='utf-8',xml_declaration=True)
    out.with_suffix('.rutas.json').write_text(json.dumps([dict(enlace=e,**r) for e,r in zip(spec['enlaces'],routes)],ensure_ascii=False,indent=2),encoding='utf-8')
    out.with_suffix('.leyenda.txt').write_text('Figura '+spec['figura']+': '+spec['titulo']+'\nFuente: '+spec['fuente']+'\n\n'
        +'Actores fuera de las ocho capas. Columnas 1 Presentación, 2 Borde, 3 Puerta de enlace, 4 Servicios, 5 Integración, 6 Datos. Bandas 7 Seguridad y 8 Observabilidad.\n'
        +'Franjas verticales: alcance de capas lógicas 1–6; franjas horizontales: capas 7–8. No representan perímetros de red.\n'
        +'Separación de red implícita en las bandas Retail y Emisor, con red y suscripción propias. Sin bloque final ni rangos CIDR visibles.\n'
        +'Icono y nombre de producto según SD-04; no se acreditan despliegues ni disponibilidad regional. * Por verificar. Sin códigos visibles ni franja amarilla.\n'
        +'Front Door Premium → conexión Azure Private Link/Private Endpoint → API Management, sin Application Gateway. Endpoint administrado por Front Door: conectividad, no otro gateway.\n'
        +'Nivel/modo APIM, acceso privado a AKS y recuperación regional pendientes de validar; no se afirma compatibilidad del Premium clásico interno. Managed HSM usa icono de familia Key Vault.\n'
        +'Verde Retail, lila Emisor, gris control transversal. Flechas: azul API, verde persistencia, naranja publicación, violeta consumo, celeste contratos externos.\n'
        +'Puertos de borde y rutas ortogonales; el canal de eventos no reemplaza la persistencia directa. Datos agrupados por contexto, con autoridad por servicio.\n'
        +'OpenTelemetry: icono oficial CNCF, https://github.com/cncf/artwork; otros iconos desde el catálogo local diagrams.\n',encoding='utf-8')
    return out
