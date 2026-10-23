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
from router_puertos_libres import enrutar

W,H=3720,2600
COLS=[(30,280),(350,370),(760,320),(1120,350),(1510,940),(2490,500),(3030,660)]

def posiciones(spec):
    pos={}
    def put(ids,x,y,w,h,step):
        for i,id in enumerate(ids):pos[id]=(x,y+i*step,w,h)
    put(['web','pos','operacion','logistica','movil','portal_f','meson_f'],365,400,340,120,170)
    for id,y in [('a_cliente',400),('a_tienda',660),('a_cd',910),('a_comercial',1080),('a_emisor',1340)]:pos[id]=(45,y,250,110)
    pos['dns']=(775,275,290,90)
    pos['pl_r']=(1087,550,26,26);pos['pl_e']=(1087,1300,26,26)
    pos['front_door']=(775,850,290,180)
    for suffix,ys in [('r',[500,720,970]),('e',[1250,1470,1720])]:
        for id,y,h in zip(['appgw_','apim_','apic_'],ys,[120,165,115]):pos[id+suffix]=(1135,y,320,h)
    pos['aks_r']=(1525,275,590,80)
    put(['oferta','abastecimiento','existencias','pedidos','ventas','comisiones','market','posventa','clientes'],1525,400,590,44,54)
    pos['x01']=(1525,930,590,55)
    put(['originacion','cartera','evidencia'],1525,1020,590,50,60)
    put(['comunes_r','comunes_e'],1525,1225,590,65,85)
    put(['conteo','lockers','busqueda','media','fila'],1525,1440,590,65,83)
    pos['local_serv']=(1525,2010,590,110)
    pos['bus_r']=(2185,1120,470,105);pos['bus_e']=(2185,1270,470,105)
    put(['comercio','canales','socios','credito'],2185,1450,470,75,110)
    put(['saga_r','saga_e'],2185,1900,470,65,85)
    pos['local_sync']=(2185,2075,470,65)
    put(['datos_merc','datos_venta','datos_clientes'],2725,400,630,115,160)
    pos['bitacora']=(2725,880,630,65)
    put(['datos_orig','datos_cartera','datos_evid'],2725,990,630,65,90)
    put(['archivo_r','archivo_e','lago_r','lago_e','redis','historial','powerbi','backup'],2725,1260,630,62,85)
    pos['local_data']=(2725,2010,630,60);pos['cupo_local']=(2725,2090,630,60)
    put(['ext_comercio','ext_canales','ext_socios','ext_credito'],365,2210,720,65,0)
    for i,id in enumerate(['ext_comercio','ext_canales','ext_socios','ext_credito']):pos[id]=(365+i*755,2210,720,65)
    for i,id in enumerate(['entra','externalid','kv','sentinel','privado']):pos[id]=(365+i*604,2345,570,95)
    for i,id in enumerate(['otel','monitor','grafana','arc','rum']):pos[id]=(365+i*604,2510,570,95)
    # Revisión del usuario: áreas dentro de capa 4 y plataformas externas en esa capa.
    for id,(x,y,w,h) in list(pos.items()):
        if x>=2170:pos[id]=(x+320,y,w,h)
    pos['aks_r']=(1525,275,910,80)
    put(['oferta','abastecimiento','existencias'],1535,440,270,55,70)
    put(['pedidos','ventas','comisiones','market'],1850,440,270,55,70)
    put(['posventa','clientes'],2165,440,270,55,70)
    put(['conteo','busqueda','media'],1535,680,270,65,80)
    pos['lockers']=(1850,790,270,65);pos['fila']=(2165,680,270,65)
    pos['x01']=(1535,1110,440,75)
    put(['originacion','cartera','evidencia'],2050,1080,370,55,75)
    pos['comunes_r']=(1525,1340,440,75);pos['comunes_e']=(1995,1340,440,75)
    put(['ext_comercio','ext_canales','ext_socios','ext_credito'],1525,1510,910,85,110)
    pos['local_serv']=(1525,2010,910,110)
    for i,id in enumerate(['entra','externalid','kv','sentinel','privado']):pos[id]=(365+i*668,2245,635,95)
    for i,id in enumerate(['otel','monitor','grafana','arc','rum']):pos[id]=(365+i*668,2410,635,95)
    pos['application_gateway']=(1135,600,320,145)
    pos['api_management']=(1135,885,320,190)
    pos['api_center']=(1135,1250,320,135)
    pos['private_link']=(1087,660,26,26)
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
    text(30,108,'Un símbolo por producto · instancias y permisos separados por ámbito · las flechas de área agrupan contratos, no datos',18)
    # Franjas de capa: límites lógicos continuos, distintos de la segmentación de red.
    for i,(x,w) in enumerate(COLS[1:]):
        fill=pal[['frontera','transversal','retail','capa_servicios','azure','emisor'][i]]['relleno']
        if i==1:fill=CATALOGO['estados_nodo']['por_acreditar']['relleno']
        rect(x,150,w,2015,fill,pal['transversal']['borde'])
    rect(350,2200,3340,150,pal['transversal']['relleno'],pal['transversal']['borde'])
    rect(350,2360,3340,160,pal['transversal']['relleno'],pal['transversal']['borde'])
    headers=[['ACTORES','Fuera de las ocho capas'],['1 · PRESENTACIÓN'],['2 · BORDE Y','EXPOSICIÓN'],['3 · PUERTA DE ENLACE','DE SERVICIOS'],['4 · SERVICIOS DE NEGOCIO'],['5 · INTEGRACIÓN','Y EVENTOS'],['6 · DATOS']]
    for (x,w),lines in zip(COLS,headers):
        rect(x,150,w,73,pal['transversal']['caja'],pal['transversal']['borde'])
        for j,line in enumerate(lines):text(x+w/2,180+j*24,line,18 if j==0 else 17,True,anchor='middle')
    # La instancia se identifica por tarjeta; las franjas delimitan capas, no redes.
    for x,w,front,name in [(1520,300,'retail','MERCADERÍA'),(1835,300,'retail','VENTA'),(2150,300,'retail','RELACIÓN CON EL CLIENTE')]:
        rect(x,380,w,555,pal[front]['relleno'],pal[front]['borde'])
        text(x+15,414,name,17,True)
        obstacles.append((x-2,386,x+w+2,424))
    rect(2035,1000,400,310,pal['emisor']['relleno'],pal['emisor']['borde'])
    text(2050,1035,'CRÉDITO · FILIAL EMISORA',18,True)
    obstacles.append((2030,1010,2440,1045))
    for x,y in [(1535,655),(1850,765),(2165,655)]:
        text(x,y,'Innovaciones del área',15,True)
        obstacles.append((x-2,y-18,x+265,y+8))
    text(1525,1465,'PLATAFORMAS EXTERNAS · conservadas o en convivencia',18,True)
    text(1525,1490,'Ubicación funcional; su emplazamiento no pasa al clúster de los servicios.',16)
    obstacles.append((1520,1440,2445,1498))
    text(2505,300,'Flechas agrupadas por área',18,True)
    text(2505,328,'Cada servicio mantiene sus datos propios.',16)
    text(2505,355,'El detalle de contratos está en el inventario.',16)
    obstacles.append((2500,275,2990,365))
    text(1525,1985,'OPERACIÓN SIN ENLACE · funciones lógicas en capas 4, 5 y 6',18,True)
    obstacles.append((1520,1962,2445,1995))
    text(365,2225,'7 · SEGURIDAD TRANSVERSAL · recursos y permisos por ámbito · Certificación de Finanzas abiertas por definir',19,True)
    obstacles.append((350,2202,3690,2235))
    text(365,2388,'8 · OBSERVABILIDAD TRANSVERSAL · colector y espacios por ámbito; sin telemetría de negocio compartida',19,True)
    obstacles.append((350,2365,3690,2398))
    text(30,2545,'Lectura: azul API; verde datos; naranja publicación; violeta consumo; celeste contrato externo; dorado punteado gobierno/capacidad; gris discontinuo por validar.',16)
    text(30,2575,'Fuente: registro e imágenes del usuario, 22-10-2026. Plataformas externas agrupadas en capa 4; adaptadores en capa 5. Pendientes en informe adjunto. SD-03/04 intactos.',16)
    obstacles.extend([(0,0,W,240),(0,2520,W,2600)])
    for cy in (560,):
        text(1100,cy,'Private Link',16,True,anchor='middle')
        text(1100,cy+22,'Por ámbito *',14,anchor='middle')
        obstacles.append((1025,cy-20,1180,cy+29))
    # Carriles libres en las separaciones entre columnas y en las bandas de ámbito.
    group_boxes={'area_mercaderia':(1520,380,300,555),'area_venta':(1835,380,300,555),'area_clientes':(2150,380,300,555),'servicios_e':(2035,1000,400,310)}
    routes=enrutar(pos,spec['enlaces'],obstacles,group_boxes)
    for e,r in zip(spec['enlaces'],routes):
        color=CATALOGO['semanticas_enlace'][e['semantica']]['color']
        dash=CATALOGO['semanticas_enlace'][e['semantica']]['estilo']
        pattern=' stroke-dasharray=\"7 5\"' if dash=='dashed' else ' stroke-dasharray=\"2 5\"' if dash=='dotted' else ''
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
        +'Seis franjas tenues: presentación amarillo, borde naranja, gateway verde, servicios rojo, integración azul, datos violeta. Capas 7 y 8 grises. Actores externos a las capas.\n'
        +'Tarjetas verdes y punto azul: Retail; lilas y punto morado: Filial; control X-01 amarillo; plataformas transversales grises. La agrupación nunca implica recursos o datos compartidos.\n'
        +'Iconos Azure del catálogo local diagrams; Managed Redis usa el icono de familia Redis, Managed HSM el de Key Vault, Power BI el de familia Power BI Embedded. OpenTelemetry: icono CNCF.\n'
        +'Flechas: API azul, persistencia verde, publicación naranja, consumo violeta, contrato externo celeste. Dorado punteado: gobierno/capacidad; gris discontinuo: relación por validar. * decisión, disponibilidad o compatibilidad pendiente.\n'
        +'Azure DNS resuelve nombres, API Center gobierna contratos y AKS aloja cargas: no son saltos adicionales de las peticiones. Capas 7/8 aplican por ámbito sin dibujar todas sus dependencias.\n'
        +'Un símbolo por producto Front Door, Application Gateway, API Management y API Center; el registro mantiene una instancia/perfil por ámbito. Las flechas de área son familias de contratos, con autoridad por servicio.\n'
        +'Un único símbolo Front Door representa dos perfiles propios; host/rutas separados por ámbito, sin tráfico cruzado implícito.\n'
        +'Front Door Premium → Azure Private Link → Application Gateway v2 → APIM Premium clásico. Entrada privada de tiendas/CD/DC-01 omite Front Door. Brazil South y residencia de la Filial condicionados a D-45.\n'
        +'Operación sin enlace: venta/consulta en capa 4, sincronización en 5, diario Retail y cupo preautorizado de Filial en 6. Son funciones y repositorios lógicos; no se representan equipos ni VM. El icono genérico de almacenamiento no selecciona un motor de datos.\n'
        +'Servicios comunes, coordinadores, respaldo, ingestión analítica y archivo conservan contratos pendientes. El inventario adjunto distingue tarjetas sin aristas intencionales y vacíos funcionales.\n'
        +'Servicios de capa 4 agrupados en Mercadería, Venta, Relación con el cliente y Crédito; X-01 media el cruce. Plataformas externas en esta capa por relación funcional, con traductores separados en capa 5. No se incorpora F:C-04 de la referencia.\n'
        +'No se certifica cumplimiento ni se cambian SD-03/04. Registrar asistencia IA nivel Alto en Tabla 4.17 cuando se incorpore a la oferta.\n',encoding='utf-8')
    return out
