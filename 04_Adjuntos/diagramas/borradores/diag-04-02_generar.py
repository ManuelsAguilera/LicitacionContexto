"""Genera las dos vistas lógicas por etapas desde un estilo SVG compartido.

El MCP infrastructure-diagram-mcp-server generó los borradores *-borrador.*;
esta fuente recompone el artefacto final para lectura impresa.
"""
from html import escape
from pathlib import Path

ROOT = Path(__file__).parent
W, H = 2400, 1580
DEFS = '''<defs>
<marker id="arr" markerWidth="11" markerHeight="11" refX="9" refY="5.5" orient="auto"><path d="M0 0L11 5.5L0 11Z" fill="#57758a"/></marker>
<marker id="arr-teal" markerWidth="11" markerHeight="11" refX="9" refY="5.5" orient="auto"><path d="M0 0L11 5.5L0 11Z" fill="#137d78"/></marker>
<marker id="arr-gold" markerWidth="11" markerHeight="11" refX="9" refY="5.5" orient="auto-start-reverse"><path d="M0 0L11 5.5L0 11Z" fill="#aa7524"/></marker>
<symbol id="pos" viewBox="0 0 64 64"><rect x="10" y="11" width="44" height="29" rx="3"/><path d="M21 50h22M32 40v10M18 18h28v15H18z"/></symbol>
<symbol id="web" viewBox="0 0 64 64"><rect x="7" y="10" width="50" height="43" rx="3"/><path d="M7 22h50M15 16h2m6 0h2m6 0h2M19 32h26M19 40h17"/></symbol>
<symbol id="card" viewBox="0 0 64 64"><rect x="6" y="14" width="52" height="36" rx="5"/><path d="M7 25h50M16 39h13"/></symbol>
<symbol id="warehouse" viewBox="0 0 64 64"><path d="M6 26 32 11l26 15v30H6V26Zm8 30V34h36v22M22 34v22m10-22v22m10-22v22"/></symbol>
<symbol id="shop" viewBox="0 0 64 64"><path d="M9 25h46l-5-13H14L9 25Zm4 0v29h38V25M25 54V36h14v18M9 25c3 8 9 8 13 0 3 8 9 8 13 0 3 8 9 8 13 0 3 8 9 8 13 0"/></symbol>
<symbol id="shield" viewBox="0 0 64 64"><path d="M32 6 54 15v17c0 14-9 22-22 27C19 54 10 46 10 32V15L32 6Zm-9 25 7 7 13-14"/></symbol>
<symbol id="gateway" viewBox="0 0 64 64"><path d="M9 32h21m4 0h21M30 32l-7-7m7 7-7 7M36 32l7-7m-7 7 7 7M32 9v14m0 18v14"/><circle cx="32" cy="32" r="7"/></symbol>
<symbol id="hex" viewBox="0 0 64 64"><path d="M19 10h26l13 22-13 22H19L6 32l13-22Z"/><circle cx="32" cy="32" r="7"/></symbol>
<symbol id="policy" viewBox="0 0 64 64"><path d="M32 6 54 15v17c0 14-9 22-22 27C19 54 10 46 10 32V15L32 6Z"/><path d="M19 32h26m-9-9 9 9-9 9m-8-18-9 9 9 9"/></symbol>
<symbol id="api" viewBox="0 0 64 64"><rect x="5" y="17" width="21" height="30" rx="3"/><rect x="38" y="17" width="21" height="30" rx="3"/><path d="M26 26h12m-12 12h12m-8-16 8 4-8 4m4 4-8 4 8 4"/></symbol>
<symbol id="event" viewBox="0 0 64 64"><path d="M8 18h36m-36 14h36M8 46h36M47 14l9 4-9 4m0 6 9 4-9 4m0 14 9 4-9 4"/></symbol>
<symbol id="file" viewBox="0 0 64 64"><path d="M14 7h27l10 10v40H14V7Zm27 0v11h10M22 29h22M22 38h22M22 47h14"/></symbol>
<symbol id="sync" viewBox="0 0 64 64"><path d="M48 23a19 19 0 0 0-31-8l-5 5m0-11v11h11M16 41a19 19 0 0 0 31 8l5-5m0 11V44H41"/></symbol>
<symbol id="data" viewBox="0 0 64 64"><ellipse cx="32" cy="13" rx="23" ry="8"/><path d="M9 13v37c0 5 10 8 23 8s23-3 23-8V13M9 31c0 5 10 8 23 8s23-3 23-8"/></symbol>
<symbol id="server" viewBox="0 0 64 64"><rect x="10" y="8" width="44" height="13" rx="2"/><rect x="10" y="25" width="44" height="13" rx="2"/><rect x="10" y="42" width="44" height="13" rx="2"/><circle cx="18" cy="14" r="1"/><circle cx="18" cy="31" r="1"/><circle cx="18" cy="48" r="1"/></symbol>
<symbol id="lock" viewBox="0 0 64 64"><rect x="13" y="27" width="38" height="30" rx="4"/><path d="M21 27V18a11 11 0 0 1 22 0v9M32 37v10"/></symbol>
<symbol id="eye" viewBox="0 0 64 64"><path d="M5 32c8-12 18-18 27-18s19 6 27 18c-8 12-18 18-27 18S13 44 5 32Z"/><circle cx="32" cy="32" r="8"/></symbol>
<symbol id="clock" viewBox="0 0 64 64"><circle cx="32" cy="32" r="24"/><path d="M32 17v16l12 8"/></symbol>
<symbol id="tag" viewBox="0 0 64 64"><path d="M8 28 28 8h27v27L35 55 8 28Z"/><circle cx="43" cy="20" r="4"/></symbol>
<symbol id="boxes" viewBox="0 0 64 64"><path d="M8 11h21v20H8zM35 11h21v20H35zM21 36h22v20H21zM8 21h21m6 0h21M21 46h22"/></symbol>
<symbol id="cart" viewBox="0 0 64 64"><path d="M7 12h8l7 31h31l5-23H18M26 52h2m19 0h2"/><circle cx="27" cy="52" r="4"/><circle cx="48" cy="52" r="4"/></symbol>
<symbol id="coins" viewBox="0 0 64 64"><ellipse cx="22" cy="17" rx="13" ry="5"/><path d="M9 17v25c0 4 6 6 13 6s13-2 13-6V17M9 29c0 4 6 6 13 6s13-2 13-6"/><circle cx="45" cy="39" r="13"/><path d="M45 30v18m-5-14h10m-10 10h10"/></symbol>
<symbol id="return" viewBox="0 0 64 64"><path d="M18 20h26a13 13 0 0 1 0 26H21M18 20l10-10M18 20l10 10"/></symbol>
<symbol id="people" viewBox="0 0 64 64"><circle cx="23" cy="22" r="8"/><circle cx="44" cy="25" r="7"/><path d="M6 53c0-11 7-18 17-18s17 7 17 18M35 39c9-3 22 3 23 14"/></symbol>
<symbol id="receipt" viewBox="0 0 64 64"><path d="M14 7h36v50l-8-5-8 5-8-5-8 5-4-5V7ZM21 20h22M21 31h22M21 42h15"/></symbol>
<symbol id="signature" viewBox="0 0 64 64"><path d="M10 50h44M12 38c10 12 15-19 22-13 4 3-4 17 3 18 4 1 8-5 15-5M38 9l17 13-20 23-9 3 2-10L48 15"/></symbol>
<symbol id="chart" viewBox="0 0 64 64"><path d="M8 54h49M15 49V34h9v15M29 49V23h9v26M43 49V12h9v37"/></symbol>
<style>
text{font-family:'DejaVu Sans',Arial,sans-serif;fill:#18334b}.title{font-size:44px;font-weight:700}.subtitle{font-size:32px;fill:#506478}.layer{font-size:32px;font-weight:700;fill:#365269}.area{font-size:34px;font-weight:700}.name{font-size:32px;font-weight:650}.small{font-size:32px;fill:#526879}.systemname{font-size:32px;fill:#526879}.code{font-size:32px;font-weight:700;fill:#506c77}.white{fill:white}
.box{fill:white;stroke:#9eb1c0;stroke-width:2}.blue{fill:#ecf4fa;stroke:#7ca6c5;stroke-width:2}.retail{fill:#eff8f5;stroke:#6aa89b;stroke-width:2}.emisor{fill:#f4effa;stroke:#a28ab9;stroke-width:2}.frontier{fill:#fff5e5;stroke:#c99d51;stroke-width:2}.neutral{fill:#f5f7f9;stroke:#aebbc5;stroke-width:2}.outline{fill:none;stroke:#aebbc5;stroke-width:2}.disabled{fill:#f4f4f4;stroke:#b8c0c7;stroke-width:2;stroke-dasharray:8 6}.railred{fill:#fceff1;stroke:#c27b82;stroke-width:2}.railblue{fill:#eef3f8;stroke:#8da5bb;stroke-width:2}
.ico{fill:none;stroke:#32667d;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}.arrow{fill:none;stroke:#57758a;stroke-width:3;marker-end:url(#arr)}.eventline{fill:none;stroke:#137d78;stroke-width:3;marker-end:url(#arr-teal)}.goldline{fill:none;stroke:#aa7524;stroke-width:3;marker-start:url(#arr-gold);marker-end:url(#arr-gold)}.dashline{fill:none;stroke:#9c8e77;stroke-width:2.8;stroke-dasharray:10 7;marker-end:url(#arr-gold)}
</style></defs>'''

RETAIL = [
    ('R:M-01','Oferta comercial'), ('R:M-02','Abastecimiento'), ('R:M-03','Existencias'),
    ('R:V-01','Pedidos'), ('R:V-02','Ventas'), ('R:V-03','Comisiones'),
    ('R:V-04','Marketplace'), ('R:CL-01','Posventa'), ('R:CL-02','Clientes Retail'),
]
EMISOR = [('F:C-01','Originación de crédito'),('F:C-02','Cartera de crédito'),('F:C-03','Evidencia financiera')]
SERVICE_ICONS = {
    'R:M-01':'tag', 'R:M-02':'boxes', 'R:M-03':'data',
    'R:V-01':'cart', 'R:V-02':'receipt', 'R:V-03':'coins',
    'R:V-04':'shop', 'R:CL-01':'return', 'R:CL-02':'people',
    'F:C-01':'card', 'F:C-02':'data', 'F:C-03':'signature',
}

class Canvas:
    def __init__(self, stage):
        self.s=stage; self.a=[]
        self.add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">')
        self.add(f'<title id="title">Ancoa: arquitectura lógica, etapa {stage}</title>')
        self.add(f'<desc id="desc">Vista por capas con dominios Retail y Filial emisora, frontera X-01, middleware modular y datos separados. Etapa {stage}.</desc>')
        self.add(DEFS); self.add(f'<rect width="{W}" height="{H}" fill="white"/>')
    def add(self, s): self.a.append(s)
    def rect(self,x,y,w,h,cls='box',rx=13): self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}"/>')
    def text(self,x,y,s,cls='name',anchor='start'):
        self.add(f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}">{escape(s)}</text>')
    def icon(self,x,y,name,size=48): self.add(f'<use href="#{name}" x="{x}" y="{y}" width="{size}" height="{size}" class="ico"/>')
    def path(self,d,cls='arrow'): self.add(f'<path d="{d}" class="{cls}"/>')
    def card(self,x,y,w,h,name,icon,cls='box',fs='name'):
        self.rect(x,y,w,h,cls);self.icon(x+15,y+(h-48)/2,icon);self.text(x+76,y+h/2+8,name,fs)
    def service(self,x,y,w,h,code,name,cls='retail',partial=False):
        self.rect(x,y,w,h,'disabled' if partial else cls,10)
        self.icon(x+w-60,y+7,SERVICE_ICONS[code],42)
        self.text(x+16,y+32,code,'code')
        self.text(x+16,y+69,name,'name')
    def done(self,name):
        self.add('</svg>')
        path=ROOT/name
        path.write_text('\n'.join(self.a),encoding='utf-8')
        return path

def make(stage):
    c=Canvas(stage)
    c.text(60,55,f'Arquitectura lógica · Etapa {stage}','title')
    c.text(60,86,'Convivencia controlada · producción mes 16' if stage==1 else 'Objetivo tras migración por olas · producción mes 21','subtitle')
    c.path('M60 121H141','arrow');c.text(158,128,'solicitud / respuesta','small')
    c.path('M590 121H671','dashline');c.text(688,128,'tercero: por validar','small')
    c.path('M1200 121H1281','goldline');c.text(1298,128,'cruce X-01','small')
    c.icon(1620,98,'shield',43);c.text(1675,128,'control en extremos','small')
    if stage==1:
        c.rect(2180,99,45,42,'disabled',5);c.text(2240,128,'Olas','small')
    c.text(80,178,'1 · PRESENTACIÓN','layer')
    channels=[('POS local','pos'),('Tienda web','web'),('Canal financiero','card'),('Operación CD','warehouse'),('Marketplace','shop')]
    for i,(n,ico) in enumerate(channels):c.card(80+i*448,195,420,93,n,ico,'blue')
    c.icon(356,221,'clock',35);c.text(402,255,'24 h','small')
    c.path('M585 288V332','arrow')
    c.text(80,332,'2 · BORDE Y EXPOSICIÓN','layer')
    c.card(80,350,510,96,'Borde protegido','shield','blue')
    c.path('M590 398H633','arrow')
    c.text(650,332,'3 · PUERTA DE ENLACE','layer')
    c.card(650,350,1670,96,'API Gateway','gateway','blue')
    c.rect(1070,367,60,60,'box',30);c.text(1100,410,'R','code','middle')
    c.rect(1840,367,60,60,'box',30);c.text(1870,410,'F','code','middle')
    c.path('M1100 446V508','arrow');c.path('M1870 446V508','arrow')
    c.text(80,502,'4 · SERVICIOS DE NEGOCIO','layer')
    c.rect(80,520,1080,402,'retail');c.text(105,557,'RETAIL','area')
    c.rect(1190,520,220,402,'frontier');c.icon(1265,564,'policy',70);c.text(1300,690,'X-01','area','middle');c.text(1300,735,'Control de','small','middle');c.text(1300,773,'cruces','small','middle')
    c.rect(1440,520,880,402,'emisor');c.text(1465,557,'FILIAL EMISORA','area')
    if stage==1:
        for x,code,name in [(105,'R:M-01','Oferta comercial'),(455,'R:M-03','Existencias'),(805,'R:V-02','Ventas')]:c.service(x,605,330,88,code,name)
    else:
        for i,(code,name) in enumerate(RETAIL):
            col=i%3;row=i//3;c.service(105+col*350,605+row*98,330,88,code,name)
    for i,(code,name) in enumerate(EMISOR):c.service(1470,605+i*98,820,88,code,name,'emisor',partial=(stage==1 and code=='F:C-02'))
    c.icon(1110,561,'shield',39);c.icon(1440,561,'shield',39)
    c.path('M1160 717H1181','goldline');c.path('M1410 717H1431','goldline')
    c.path('M1100 922V976','arrow');c.path('M1870 922V976','arrow')
    c.text(80,969,'5 · INTEGRACIÓN Y EVENTOS','layer')
    c.rect(80,986,2240,120,'blue')
    for x,n,ico in [(110,'Mediación API','api'),(665,'Broker de eventos','event'),(1220,'Adaptadores','file'),(1775,'Conciliación','sync')]:c.card(x,1011,520,70,n,ico,'box','small')
    c.path('M1200 1106V1151','dashline')
    c.text(80,1146,'SISTEMAS CONECTADOS','layer')
    c.rect(80,1155,2240,118,'outline')
    if stage==1:
        systems=[('Retail 2009','server'),('Crédito 2011','card'),('POS 2014','pos'),('ERP/DTE','receipt'),('WMS','warehouse'),('Marketplace','shop'),('Tienda web','web'),('Fidelización','people')]
        for i,(name,icon) in enumerate(systems):
            x=90+i*278;c.rect(x,1172,265,85,'neutral');c.icon(x+12,1194,icon,40);c.text(x+58,1225,name,'systemname')
    else:
        systems=[('ERP/DTE','receipt'),('WMS','warehouse'),('Marketplace','shop'),('Tienda web','web'),('Fidelización','people')]
        for i,(name,icon) in enumerate(systems):c.card(100+i*446,1172,420,85,name,icon,'neutral','small')
    c.text(80,1302,'6 · DATOS POR ÁMBITO','layer')
    c.rect(80,1320,1080,95,'retail');c.text(100,1380,'RETAIL','code')
    c.rect(340,1337,365,61,'box',9);c.icon(350,1347,'data',40);c.text(402,1378,'Transaccional','small')
    c.rect(735,1337,395,61,'box',9);c.icon(745,1347,'chart',40);c.text(797,1378,'Analítica','small')
    c.card(1190,1320,220,95,'X-01','policy','frontier','small')
    c.rect(1440,1320,880,95,'emisor');c.text(1460,1380,'EMISOR','code')
    c.rect(1650,1337,330,61,'box',9);c.icon(1660,1347,'data',40);c.text(1712,1378,'Transaccional','small')
    c.rect(2000,1337,300,61,'box',9);c.icon(2010,1347,'chart',40);c.text(2062,1378,'Analítica','small')
    c.text(80,1452,'7 · SEGURIDAD TRANSVERSAL','layer')
    c.text(1210,1452,'8 · OBSERVABILIDAD TRANSVERSAL','layer')
    c.card(80,1470,1090,73,'Seguridad','lock','railred','small')
    c.card(1210,1470,1110,73,'Observabilidad','eye','railblue','small')
    return c.done(f'diag-04-02{"a" if stage==1 else "b"}_arquitectura-logica-etapa-{stage}.svg')

def make_flows():
    c=Canvas('flujos')
    c.a[1]='<title id="title">Ancoa: flujos lógicos críticos por etapa</title>'
    c.a[2]='<desc id="desc">Ocho flujos propuestos con extremos y componentes de mediación. Cinco se habilitan en etapa 1 y tres se agregan en etapa 2. El trazo discontinuo indica protocolo de tercero por validar.</desc>'
    c.text(60,58,'Arquitectura lógica · flujos críticos','title')
    c.text(60,96,'Interfaces propuestas · Etapas 1 y 2','subtitle')
    for x,cls,name in [(60,'arrow','Solicitud'),(490,'eventline','Evento'),(850,'dashline','Tercero: por validar'),(1510,'goldline','Cruce X-01')]:
        c.path(f'M{x} 142H{x+75}',cls);c.text(x+95,150,name,'small')
    c.text(60,204,'ETAPA 1 · desde mes 16','layer')
    def row(y,source,source_icon,via,via_icon,target,target_icon,cls='arrow'):
        c.rect(60,y,2260,113,'outline')
        c.card(85,y+13,595,86,source,source_icon,'blue','small')
        c.card(835,y+13,595,86,via,via_icon,'box','small')
        c.card(1585,y+13,710,86,target,target_icon,'retail' if target_icon!='card' else 'emisor','small')
        c.path(f'M680 {y+56}H826',cls);c.path(f'M1430 {y+56}H1576',cls)
    row(220,'Oferta comercial','tag','Broker de eventos','event','POS · Tienda web','pos','eventline')
    row(353,'Ventas','receipt','Broker de eventos','event','Existencias','data','eventline')
    row(486,'POS local','pos','Cola POS local','data','Ventas','receipt','eventline')
    row(619,'Ventas','receipt','X-01 Control de cruces','policy','Originación de crédito','card','goldline')
    row(752,'Ventas','receipt','Adaptador ERP/DTE','file','ERP/DTE','server','dashline')
    c.text(60,938,'ETAPA 2 · desde mes 21','layer')
    row(955,'Pedidos','cart','Mediación API','api','Existencias','data','arrow')
    row(1088,'Pedidos','cart','Adaptador WMS','file','WMS principal','warehouse','dashline')
    y=1221
    c.rect(60,y,2260,113,'outline')
    c.card(85,y+13,595,86,'Posventa','return','blue','small')
    c.card(835,y+13,595,86,'Broker de eventos','event','box','small')
    c.rect(1585,y+13,710,86,'retail')
    c.icon(1600,y+32,'data',45);c.text(1660,y+69,'Existencias','small')
    c.add(f'<path d="M1932 {y+24}v64" stroke="#6aa89b" stroke-width="2"/>')
    c.icon(1950,y+32,'shop',45);c.text(2010,y+69,'Marketplace','small')
    c.path(f'M680 {y+56}H826','eventline');c.path(f'M1430 {y+56}H1576','eventline')
    c.a[0]=c.a[0].replace(f'height="{H}"','height="1420"').replace(f'viewBox="0 0 {W} {H}"',f'viewBox="0 0 {W} 1420"')
    return c.done('diag-04-02c_flujos-logicos-criticos.svg')

if __name__=='__main__':
    for s in (1,2):print(make(s))
    print(make_flows())
