"""Plantilla L2 horizontal: geometría de catálogo, no estilos del cliente."""
import html,json,shutil,subprocess,textwrap,xml.etree.ElementTree as ET
from pathlib import Path
from _comun import CATALOGO,frente_de_nodo
from render_capas_referencia import icono_data
from router_horizontal import enrutar

W,H=3200,3890
MAIN_X,MAIN_W=360,2280
LAYERS=[(370,210,'1 · PRESENTACIÓN'),(650,190,'2 · BORDE Y EXPOSICIÓN'),(940,240,'3 · PUERTA DE ENLACE DE SERVICIOS'),(1210,800,'4 · SERVICIOS DE NEGOCIO'),(2080,460,'5 · INTEGRACIÓN Y EVENTOS'),(2640,740,'6 · DATOS'),(3480,180,'7 · SEGURIDAD TRANSVERSAL'),(3740,170,'8 · OBSERVABILIDAD TRANSVERSAL')]
AREAS={'area_mercaderia':(380,1280,490,590),'area_venta':(900,1280,490,590),'area_clientes':(1420,1280,490,590),'servicios_e':(2100,1280,490,590)}

def posiciones(spec):
    pos={}
    def put(ids,x,y,w,h,step):
        for i,id in enumerate(ids):pos[id]=(x,y+i*step,w,h)
    for i,id in enumerate(['a_cliente','a_tienda','a_cd','a_comercial','a_emisor']):pos[id]=(380+i*450,210,420,90)
    for i,id in enumerate(['web','pos','operacion','logistica','movil','portal_f','meson_f']):pos[id]=(380+i*325,450,300,95)
    pos.update(front_door=(960,715,440,115),private_link=(1135,870,40,40),application_gateway=(960,1000,440,65),api_management=(400,1090,2170,70))
    pos.update(tech_ui=(50,450,250,95),dns=(50,715,250,110),api_center=(50,1010,250,125),tech_java=(50,1350,250,100),tech_spring=(50,1470,250,100),aks_r=(50,1600,250,145))
    put(['oferta','abastecimiento','existencias'],400,1350,450,65,80)
    put(['pedidos','ventas','comisiones','market'],920,1350,450,65,80)
    put(['posventa','clientes'],1440,1350,450,65,80)
    put(['originacion','cartera','evidencia'],2120,1350,450,65,80)
    put(['conteo','busqueda','media'],400,1630,450,60,75)
    pos.update(lockers=(920,1780,450,60),fila=(1440,1630,450,60),local_serv=(920,1685,450,60),x01=(1955,1510,130,155),comunes=(920,1900,1000,75))
    pos.update(bus_r=(400,2180,450,100),bus_e=(2120,2180,450,100),proy_r=(1440,2180,450,100),proy_e=(2120,2310,450,90))
    for i,id in enumerate(['comercio','canales','socios']):pos[id]=(400+i*520,2320,450,85)
    pos.update(credito=(2120,2430,450,70),local_sync=(920,2440,450,65))
    for id,y in [('ext_comercio',1350),('ext_canales',1660),('ext_socios',1970),('ext_credito',2430)]:pos[id]=(2720,y,430,85)
    for i,id in enumerate(['datos_merc','datos_venta','datos_clientes']):pos[id]=(400+i*520,2730,450,95)
    put(['datos_orig','datos_cartera','datos_evid'],2120,2730,450,70,90)
    pos.update(bitacora=(1955,2730,130,115),mart_r=(400,2880,450,100),mart_e=(2120,3000,450,100),archivo_r=(920,2880,450,90),vector=(1440,2880,450,90),redis=(400,3010,450,75),historial=(400,3120,450,75),powerbi=(920,3070,990,95),local_data=(920,3250,450,65),archivo_e=(2120,3120,450,90),cupo_local=(2120,3260,450,65))
    for i,id in enumerate(['entra','externalid','kv','sentinel','privado']):pos[id]=(380+i*450,3530,420,105)
    for i,id in enumerate(['otel','monitor','grafana','rum']):pos[id]=(380+i*565,3790,540,95)
    missing={n['id'] for n in spec['nodos']}-set(pos)
    if missing:raise ValueError('Componentes sin ranura: '+str(missing))
    return {n['id']:(pos[n['id']][0],pos[n['id']][1]-160,pos[n['id']][2],pos[n['id']][3]) for n in spec['nodos']}

def renderizar(spec,salida):
    out=Path(salida);out.parent.mkdir(parents=True,exist_ok=True)
    pos=posiciones(spec);groups={g['id']:g for g in spec['grupos']};group_boxes={id:(x,y-160,w,h) for id,(x,y,w,h) in AREAS.items()}
    shift_layout=True
    svg=[];background=[];texts=[];cards=[];icons=[];obstacles=[];pal=CATALOGO['frentes']
    def rect(x,y,w,h,fill,stroke,rx=7,dash=False,record=True):
        if shift_layout and y>=160:y-=160
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.3"'+(' stroke-dasharray="7 4"' if dash else '')+'/>')
        if record:background.append(('',f'rounded=1;arcSize=8;fillColor={fill};strokeColor={stroke};',x,y,w,h))
    def text(x,y,s,size=18,bold=False,anchor='start',color='#1A1A1A',record=True):
        if shift_layout and y>=160:y-=160
        svg.append(f'<text x="{x}" y="{y}" font-family="Segoe UI,Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" text-anchor="{anchor}" fill="{color}">{html.escape(s)}</text>')
        if record:
            width=max(45,len(s)*size*.59+12)
            texts.append((s,f'text;html=0;align={"center" if anchor=="middle" else "left"};fontSize={size};fontColor={color};fontStyle={1 if bold else 0};',x-width/2 if anchor=='middle' else x,y-size,width,size+7))
    def note(x,y,w,s,size=16):
        text(x,y,s,size)
        obstacles.append((x-3,y-size-4,x+w,y+8))
    svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
    svg.append('<defs><marker id="flecha" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L7,3 L0,6 Z" fill="context-stroke"/></marker></defs>')
    rect(0,0,W,H,'#FFFFFF','#FFFFFF',0)
    text(30,35,'ONLY SIMPLE SOLUTIONS / MULTITIENDAS ANCOA',20,True)
    text(30,78,spec['titulo'],30,True)
    text(30,105,'Vista L2 · ocho capas · un símbolo por producto, con recursos y permisos propios por ámbito · * por verificar',18)
    rect(30,370,280,3010,pal['transversal']['relleno'],pal['transversal']['borde'])
    text(170,395,'TECNOLOGÍAS',17,True,'middle');text(170,418,'Y GOBIERNO',17,True,'middle')
    colors=['frontera','transversal','retail','capa_servicios','azure','emisor','transversal','transversal']
    for (y,h,name),front in zip(LAYERS,colors):
        fill=pal[front]['relleno'] if not name.startswith('2') else CATALOGO['estados_nodo']['por_acreditar']['relleno']
        rect(MAIN_X,y,MAIN_W,h,fill,pal['transversal']['borde'])
        rect(MAIN_X,y,MAIN_W,46,pal['transversal']['caja'],pal['transversal']['borde'])
        text(MAIN_X+MAIN_W/2,y+31,name,22,True,'middle')
        title_w=len(name)*22*.59+24
        obstacles.append((MAIN_X+MAIN_W/2-title_w/2,y+6,MAIN_X+MAIN_W/2+title_w/2,y+40))
    for id,name,front in [('area_mercaderia','MERCADERÍA','retail'),('area_venta','VENTA','retail'),('area_clientes','RELACIÓN CON EL CLIENTE','retail'),('servicios_e','CRÉDITO · FILIAL','emisor')]:
        x,y,w,h=AREAS[id];rect(x,y,w,h,pal[front]['relleno'],pal[front]['borde'])
        text(x+15,y+30,name,19,True);text(x+15,y+51,'Transacción y outbox por servicio',15)
        obstacles.append((x-2,y+4,x+w+2,y+59))
    rect(2700,1280,470,1260,pal['externo']['relleno'],pal['externo']['borde'])
    text(2720,1312,'SISTEMAS EXTERNOS',21,True)
    note(2720,1335,430,'Conservados / en convivencia',15)
    note(2720,1485,430,'Contratos por contraparte; no son servicios propios.',15)
    note(400,2445,450,'Coordinación durable por ámbito:',15)
    note(400,2470,450,'responsabilidad definida; motor por justificar.',15)
    note(1440,2470,450,'Sin canal de eventos entre Retail y Filial.',15)
    note(400,3355,1500,'BI consulta solo los repositorios analíticos. Archivo, evidencia y respaldo tienen políticas distintas.',16)
    note(2715,2580,450,'Panel externo: autoridad y ubicación propias.',15)
    text(1200,897,'Azure Private Link',15,True)
    obstacles.append((1195,875,1430,905))
    text(30,3970,'Lectura: API azul · datos propios verde · publicación naranja · consumo violeta · integración celeste · gobierno dorado punteado · por validar gris discontinuo.',16)
    text(30,4000,'Fuente: plan y referencia del usuario, 22-10-2026. Data Lake retirado; analítica PostgreSQL por ámbito. Capacidad, región y residencia por acreditar. SD-03/04 intactos.',16)
    obstacles.extend([(0,0,W,150),(0,3930,W,H+160)])
    obstacles=[(l,t-160 if t>=160 else t,r,b-160 if b>=160 else b) for l,t,r,b in obstacles]
    routes=enrutar(pos,spec['enlaces'],obstacles,group_boxes)
    shift_layout=False
    for e,r in zip(spec['enlaces'],routes):
        definition=CATALOGO['semanticas_enlace'][e['semantica']];color=definition['color'];dash=definition['estilo']
        pattern=' stroke-dasharray="7 5"' if dash=='dashed' else ' stroke-dasharray="2 5"' if dash=='dotted' else ''
        d='M'+' L'.join(f'{x},{y}' for x,y in r['points'])
        svg.append(f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-width="5"/>')
        svg.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2.2"{pattern} marker-end="url(#flecha)"><title>{html.escape(e["etiqueta"])}</title></path>')
    for n in spec['nodos']:
        x,y,w,h=pos[n['id']];f=frente_de_nodo(n,groups) or 'transversal'
        p=pal['externo'] if n['tipo']=='sistema_conservado' else pal[f];pending=n.get('estado')=='por_acreditar'
        rect(x,y,w,h,p['caja'],p['borde'],dash=pending,record=False)
        if n['tipo']=='private_link':
            svg.pop()
            uri=icono_data(n['tipo'])
            svg.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{uri}"/>')
            cards.append((n['id'],'','fillColor=none;strokeColor=none;',x,y,w,h))
            icons.append(('icon_'+n['id'],'','shape=image;imageAspect=1;image='+uri.replace(';base64,',',')+';',x,y,w,h))
            continue
        if w<190:
            uri=icono_data(n['tipo']);size=28
            svg.append(f'<image x="{x+(w-size)/2}" y="{y+10}" width="{size}" height="{size}" href="{uri}"/>')
            lines=[]
            for line in n['etiqueta'].split('\n'):lines.extend(textwrap.wrap(line,width=12))
            for j,line in enumerate(lines):text(x+w/2,y+62+j*21,line,16,j==0,'middle',record=False)
            cards.append((n['id'],html.escape(n['etiqueta']).replace('\n','<br>'),f'rounded=1;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;spacingTop=32;spacingLeft=3;fontSize=16;fillColor={p["caja"]};strokeColor={p["borde"]};',x,y,w,h))
            icons.append(('icon_'+n['id'],'','shape=image;imageAspect=1;image='+uri.replace(';base64,',',')+';',x+(w-size)/2,y+10,size,size))
            continue
        size=27 if h<55 else 36 if h<85 else 46
        uri=icono_data(n['tipo'])
        svg.append(f'<image x="{x+10}" y="{y+(h-size)/2}" width="{size}" height="{size}" href="{uri}"/>')
        # Punto de ámbito sin confundirlo con el color de la capa.
        if f in ('retail','emisor'):
            dot=pal['azure' if f=='retail' else 'emisor']['borde']
            rect(x+w-15,y+4,8,8,dot,dot,4)
        lines=[]
        for line in n['etiqueta'].split('\n'):
            lines.extend(textwrap.wrap(line,width=max(12,int((w-size-35)/8.6)),break_long_words=False) or [''])
        if pending:lines[-1]+=' *'
        fs=19 if w>350 else 16
        if len(lines)*(fs+4)>h-6:fs=14
        if len(lines)*(fs+4)>h:raise ValueError('Texto no cabe: '+n['id'])
        top=y+(h-len(lines)*(fs+4))/2+fs
        for j,line in enumerate(lines):text(x+size+22,top+j*(fs+4),line,fs,j==0,record=False)
        cards.append((n['id'],html.escape(n['etiqueta']).replace('\n','<br>')+(' *' if pending else ''),f'rounded=1;whiteSpace=wrap;html=1;align=left;verticalAlign=middle;spacingLeft={size+22};fontSize={fs};fillColor={p["caja"]};strokeColor={p["borde"]};'+('dashed=1;' if pending else ''),x,y,w,h))
        icons.append(('icon_'+n['id'],'','shape=image;imageAspect=1;image='+uri.replace(';base64,',',')+';',x+10,y+(h-size)/2,size,size))

    text(30,137,'Leyenda',16,True)
    for i,(sem,name) in enumerate([('solicitud','API / solicitud'),('persistencia','Persistencia propia'),('publicacion','Publicación'),('consumo','Consumo'),('adaptacion','Contrato externo')]):
        x=360+i*550;color=CATALOGO['semanticas_enlace'][sem]['color']
        svg.append(f'<path d="M{x},130 L{x+30},130" stroke="{color}" stroke-width="3" marker-end="url(#flecha)"/>')
        text(x+40,137,name,16,True,color=color)
    svg.append('</svg>');out.with_suffix('.svg').write_text('\n'.join(svg),encoding='utf-8')
    exe=shutil.which('inkscape') or 'C:/Program Files/Inkscape/bin/inkscape.com'
    subprocess.run([exe,str(out.with_suffix('.svg')),'--export-type=png','--export-filename='+str(out.with_suffix('.png')),'--export-width=4500'],check=True,capture_output=True,timeout=60)
    mx=ET.Element('mxfile',host='diagramas-ancoa',type='device');dg=ET.SubElement(mx,'diagram',name='Capas y servicios de plataforma')
    model=ET.SubElement(dg,'mxGraphModel',page='0',grid='1',gridSize='10');root=ET.SubElement(model,'root')
    ET.SubElement(root,'mxCell',id='0');ET.SubElement(root,'mxCell',id='1',parent='0')
    def cell(id,value,style,x,y,w,h):
        c=ET.SubElement(root,'mxCell',id=id,value=value,style=style,vertex='1',parent='1')
        ET.SubElement(c,'mxGeometry',x=str(x),y=str(y),width=str(w),height=str(h),attrib={'as':'geometry'})
    for i,o in enumerate(background):
        id=next((gid for gid,box in group_boxes.items() if tuple(o[2:])==box),'background'+str(i))
        cell(id,*o)
    for i,(e,r) in enumerate(zip(spec['enlaces'],routes)):
        color=CATALOGO['semanticas_enlace'][e['semantica']]['color']
        line_style=CATALOGO['semanticas_enlace'][e['semantica']]['estilo']
        extra='dashed=1;dashPattern=2 5;' if line_style=='dotted' else 'dashed=1;' if line_style=='dashed' else ''
        sx,sy=r['source']['anchor'];tx,ty=r['target']['anchor'];sdx,sdy=r['source']['offset'];tdx,tdy=r['target']['offset']
        c=ET.SubElement(root,'mxCell',id='edge'+str(i),value='',edge='1',parent='1',source=e['de'],target=e['a'],tooltip=e['etiqueta'],style=f'edgeStyle=none;orthogonal=1;rounded=0;endArrow=block;endFill=1;strokeColor={color};strokeWidth=2.2;{extra}exitX={sx};exitY={sy};entryX={tx};entryY={ty};exitDx={sdx};exitDy={sdy};entryDx={tdx};entryDy={tdy};exitPerimeter=0;entryPerimeter=0;')
        geo=ET.SubElement(c,'mxGeometry',relative='1',attrib={'as':'geometry'});arr=ET.SubElement(geo,'Array',attrib={'as':'points'})
        for x,y in r['points'][1:-1]:ET.SubElement(arr,'mxPoint',x=str(x),y=str(y))
    for o in cards+icons:cell(*o)
    for i,o in enumerate(texts):cell('text'+str(i),*o)
    ET.ElementTree(mx).write(out.with_suffix('.drawio'),encoding='utf-8',xml_declaration=True)
    out.with_suffix('.rutas.json').write_text(json.dumps([dict(enlace=e,**r) for e,r in zip(spec['enlaces'],routes)],ensure_ascii=False,indent=2),encoding='utf-8')

    out.with_suffix('.leyenda.txt').write_text('Figura '+spec['figura']+': '+spec['titulo']+'\nFuente: '+spec['fuente']+'\n\nLeyenda:\n'
        +'Vista sin fila de actores. Franjas 1 Presentación, 2 Borde, 3 Puerta de enlace, 4 Servicios, 5 Integración, 6 Datos; bandas transversales 7 Seguridad y 8 Observabilidad.\n'
        +'Columna izquierda: tecnologías y gobierno. Panel derecho: sistemas externos, con autoridad y ubicación propias. Los nombres del ejemplo no se trasladan.\n'
        +'Verde Retail; lila Filial; amarillo X-01; gris producto agregado o transversal. Un símbolo por producto no equivale a recursos, red, tenant o bases compartidos.\n'
        +'Conectores: azul API, verde persistencia, naranja publicación, violeta consumo, celeste contrato externo, dorado punteado gobierno, gris discontinuo por verificar. Puertos en contornos y rutas ortogonales sin atravesar tarjetas o títulos.\n'
        +'Las flechas de área agrupan contratos por servicio. Cada servicio conserva su transacción y outbox; no hay una base o transacción común por área. X-01 rige el único cruce entre negocios.\n'
        +'Data Lake retirado. Hechos confirmados → Service Bus del ámbito → procesadores de proyecciones → PostgreSQL analítico dedicado → Power BI del ámbito. BI no consulta repositorios operacionales. Conectividad privada de datos, no otra puerta de APIs.\n'
        +'Carga inicial/reconstrucción desde exportación autorizada y punto de corte; el bus no es archivo histórico. Blob separa documentos, evidencia, retención y conjuntos versionados. pgvector contiene un índice reconstruible de Oferta.\n'
        +'Servicios comunes queda reservado para definición futura, sin contratos inventados. La coordinación es responsabilidad de Integración; no se eligen motores por completar el dibujo.\n'
        +'Backup Vault y Arc/Monitor Agent pasan al detalle físico/operativo. Continuidad se expresa como funciones de software y datos, no como hardware o VM.\n'
        +'Las tecnologías son selecciones propuestas; * disponibilidad, capacidad, compatibilidad o decisión pendiente. Tenant y residencia de Filial sin aprobación expresa. SD-03/04 intactos.\n'
        +'Iconos del catálogo local diagrams y OpenTelemetry CNCF; Managed HSM usa icono de familia Key Vault, Managed Redis de Redis, Power BI de la familia Power BI Embedded.\n'
        +'Registrar asistencia IA en nivel Alto en Tabla 4.17 al incorporar la figura a la oferta.\n',encoding='utf-8')
    return out
