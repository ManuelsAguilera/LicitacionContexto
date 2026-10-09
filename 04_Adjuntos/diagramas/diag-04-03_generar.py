"""Vistas lógicas Ancoa, carta horizontal. Iconos del MCP de andrewmoshu.

Los pictogramas de tecnología se obtienen del catálogo de
infrastructure-diagram-mcp-server; las cajas y flechas conservan una
composición SVG propia para respetar el orden visual acordado.
"""
from pathlib import Path
from html import escape
from base64 import b64encode
import importlib.util
import subprocess
import infrastructure_diagram_mcp_server
ROOT=Path(__file__).parent
MCP_RESOURCES=Path(infrastructure_diagram_mcp_server.__file__).resolve().parents[1]/'resources'
MCP_ICONS={
 'pos':'onprem/client/client.png',
 'people':'onprem/client/users.png',
 'data':'programming/flowchart/database.png',
 'cloud':'onprem/network/internet.png',
 'api':'programming/flowchart/input-output.png',
 'event':'programming/flowchart/multiple-documents.png',
 'service':'programming/flowchart/predefined-process.png',
 'antenna':'generic/network/router.png',
 'mobile':'generic/device/mobile.png',
}
def mcp_icon_defs():
 parts=['<defs>']
 for name,relative in MCP_ICONS.items():
  data=b64encode((MCP_RESOURCES/relative).read_bytes()).decode('ascii')
  parts.append(f'<symbol id="mcp_{name}" viewBox="0 0 64 64"><image href="data:image/png;base64,{data}" width="64" height="64" preserveAspectRatio="xMidYMid meet"/></symbol>')
 parts.append('</defs>')
 return ''.join(parts)
spec=importlib.util.spec_from_file_location('icons',ROOT/'diag-04-02_generar.py')
icons=importlib.util.module_from_spec(spec);spec.loader.exec_module(icons)
W,H=1320,1020
STYLE='''<style>text{font-family:DejaVu Sans,Arial,sans-serif;fill:#203747;font-size:18px}.title{font-size:25px;font-weight:700}.head{font-size:19px;font-weight:700}.label{font-size:18px;font-weight:600}.ico{fill:none;stroke:#395c73;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}.flow{fill:none;stroke:#56798e;stroke-width:1.8;marker-end:url(#arrow)}.cross{fill:none;stroke:#b68b3f;stroke-width:2;marker-end:url(#arrowGold)}.dash{stroke-dasharray:5 4}</style>'''
EXTRA='''<defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="#56798e"/></marker><marker id="arrowGold" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="#b68b3f"/></marker><symbol id="mobile" viewBox="0 0 64 64"><rect x="19" y="5" width="27" height="53" rx="5"/><path d="M25 13h15M29 50h8"/></symbol><symbol id="cloud" viewBox="0 0 64 64"><path d="M14 45a12 12 0 0 1-2-24 19 19 0 0 1 36-3 14 14 0 0 1 2 27Z"/></symbol><symbol id="antenna" viewBox="0 0 64 64"><path d="M32 22v36M20 58h24M23 34l9-12 9 12M19 12a19 19 0 0 0 0 25M45 12a19 19 0 0 1 0 25M12 5a29 29 0 0 0 0 40M52 5a29 29 0 0 1 0 40"/></symbol></defs>'''
class C:
 def __init__(self,stage):
  self.a=[f'<svg xmlns="http://www.w3.org/2000/svg" width="11in" height="8.5in" viewBox="0 0 {W} {H}" role="img"><title>Arquitectura lógica Ancoa · Etapa {stage}</title>',icons.DEFS,EXTRA,mcp_icon_defs(),STYLE,f'<rect width="{W}" height="{H}" fill="white"/>']
 def rect(self,x,y,w,h,fill='#fff',stroke='#a0b6c2',dash=False,rx=13):self.a.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.4"'+(' stroke-dasharray="5 4"' if dash else '')+'/>')
 def txt(self,x,y,lines,cls='',anchor='middle'):
  if isinstance(lines,str):lines=[lines]
  self.a.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}">'+''.join(f'<tspan x="{x}" dy="{0 if i==0 else 20}">{escape(t)}</tspan>' for i,t in enumerate(lines))+'</text>')
 def ico(self,x,y,name,size=32):self.a.append(f'<use href="#{"mcp_"+name if name in MCP_ICONS else name}" x="{x}" y="{y}" width="{size}" height="{size}"'+('' if name in MCP_ICONS else ' class="ico"')+'/>')
 def box(self,x,y,w,h,name,icon=None,fill='#fff',dash=False):
  self.rect(x,y,w,h,fill,dash=dash,rx=8)
  lines=name if isinstance(name,list) else [name]
  if icon:self.ico(x+7,y+(h-30)/2,icon,30)
  self.txt(x+w/2+(15 if icon else 0),y+h/2-10*(len(lines)-1)+6,lines)
 def path(self,d,cls='flow'):self.a.append(f'<path d="{d}" class="{cls}"/>')
 def band(self,y,h,label,fill):
  self.rect(24,y,1170,h,fill,stroke='#a9bac5',rx=20);self.txt(105,y+h/2-10*(len(label)-1)+5,label,'label')
 def save(self,stage):
  self.a.append('</svg>');p=ROOT/f'diag-04-03{"a" if stage==1 else "b"}_arquitectura-logica-etapa-{stage}.svg';p.write_text('\n'.join(self.a));subprocess.run(['inkscape',str(p),'--export-type=png','--export-filename='+str(p.with_suffix('.png')),'--export-width=3300','--export-height=2550'],check=True,stdout=subprocess.DEVNULL);print(p)
def make(stage):
 c=C(stage)
 c.txt(28,34,f'Ancoa · Arquitectura lógica · Etapa {stage}','title','start')
 c.txt(1180,34,'Mes 16' if stage==1 else 'Mes 21','head','end')
 c.txt(28,67,'Conexiones propuestas · ubicación por validar · Web / fidelización: evaluación E1',anchor='start')
 for x,w,color,name in [(24,694,'#629886','Retail'),(737,105,'#b08a43','Frontera'),(861,435,'#947bac','Filial emisora')]:
  c.rect(x,91,w,885,'none',color,True,13);c.txt(x+w/2,115,name,'head')
 # People and devices at the top.
 for x,w,name,ico in [(42,205,'Tiendas Físicas','pos'),(269,205,['Clientes y','personal'],'people'),(496,205,['Centros de','distribución'],'pos'),(881,191,'Titulares','mobile'),(1090,191,['Personal','financiero'],'people')]:c.box(x,142,w,70,name,ico)
 # Views and local storage.
 for x,w,name,ico in [(42,205,'POS nuevo','pos'),(269,205,'Tienda web','web'),(496,205,'Operación CD','pos'),(881,191,['Portal','financiero'],'web'),(1090,191,['Sesión','financiera'],'pos')]:c.box(x,264,w,66,name,ico)
 c.box(42,345,205,56,['Cola local','24 h'],'data')
 # POS 2014 shares the physical-store entry in Stage 1.
 c.box(496,345,205,56,['Carga','Concepción'],'pos')
 for x in [371,598,977,1185]:c.path(f'M{x} 212V264')
 if stage==1:
  c.box(42,224,205,30,'POS 2014',None,dash=True)
  c.path('M144 212V224')
  c.path('M144 212V216L255 216V297L247 297')
  c.path('M42 239L31 239V476L83 476','flow dash')
 else:c.path('M144 212V264')
 c.path('M144 330V345')
 # Cloud and head-office connections are proposed, not current-location claims.
 c.box(83,449,576,54,'Plataforma Ancoa · Retail','cloud',fill='#edf6f2')
 c.box(884,449,394,54,'Plataforma Ancoa · Emisor','cloud',fill='#f3eef8')
 c.ico(48,460,'antenna',34)
 c.box(496,411,205,30,'Casa matriz',None,dash=True)
 c.path('M144 401V445L371 445V449','flow dash');c.path('M371 330V449','flow dash')
 c.path('M598 401V405L715 405V476L659 476','flow dash');c.path('M598 441V445L371 445V449','flow dash')
 c.path('M598 330L709 330V445L371 445V449','flow dash')
 for x in [977,1185]:c.path(f'M{x} 330V430L1081 430V449','flow dash')
 c.box(83,538,277,65,['API y mediación','Retail'],'api')
 c.box(382,538,277,65,['Eventos y','adaptadores'],'event')
 c.box(884,538,394,65,['Middleware Emisor','API · eventos · adaptadores'],'api')
 for x in [221,520,1081]:c.path(f'M{x} 503V538')
 c.box(83,613,371,44,['ERP/DTE · WMS','Marketplace · Fidelización']);c.box(469,613,190,44,['Analítica','Retail'],'data')
 c.box(884,613,394,44,'Crédito 2011 · Convivencia' if stage==1 else 'Salida contable · ERP',None,dash=stage==1)
 c.path('M520 603V608L269 608V613');c.path('M520 603V613');c.path('M1081 603V613')
 # Data stores: one store per service, represented individually above the service catalog.
 retail=[('R:M-01',['Oferta','comercial']),('R:M-03','Existencias'),('R:V-02','Ventas')] if stage==1 else [('R:M-01',['Oferta','comercial']),('R:M-02','Abastecimiento'),('R:M-03','Existencias'),('R:V-01','Pedidos'),('R:V-02','Ventas'),('R:V-03','Comisiones'),('R:V-04','Marketplace'),('R:CL-01','Posventa'),('R:CL-02',['Clientes','Retail'])]
 for i,(code,name) in enumerate(retail):
  col=i%3;row=i//3;x=62+col*215;y=677+row*35
  store_names={'R:M-01':'Oferta','R:M-02':'Abastecimiento','R:M-03':'Existencias','R:V-01':'Pedidos','R:V-02':'Ventas','R:V-03':'Comisiones','R:V-04':'Marketplace','R:CL-01':'Posventa','R:CL-02':'Clientes Retail'}
  c.box(x,y,191,33,store_names[code],'data')
 # Analytic store stays above all service-store return lanes.
 for i,(code,name) in enumerate([('F:C-01','Originación'),('F:C-02','Cartera'),('F:C-03','Evidencia')]):c.box(917,688+i*32,330,28,name,'data')
 c.box(917,792,330,30,'Analítica Emisor','data')
 # Service catalog forms the final row of the reading, below the stores.
 for i,(code,name) in enumerate(retail):
  col=i%3;row=i//3;x=62+col*215;y=826+row*49
  c.box(x,y,191,44,name,'service',fill='#edf6f2')
  # A dedicated orthogonal return goes from the service to its own store.
  lane=x+197+row*4;db_y=693+row*35
  c.path(f'M{x+191} {y+22}L{lane} {y+22}V{db_y}L{x+191} {db_y}')
 if stage==1:
  c.box(62,735,191,44,['Retail 2009','Convivencia'],None,dash=True)
  c.path('M83 590L48 590V757L62 757')
 for i,name in enumerate([['Originación de crédito'],['Cartera de crédito','Migración por olas'] if stage==1 else ['Cartera de crédito'],['Evidencia financiera']]):
  y=848+i*39;c.box(917,y,330,39,name,'service',fill='#f3eef8',dash=stage==1 and i==1)
  lane=1260+i*8;db_y=702+i*32;c.path(f'M1247 {y+22}L{lane} {y+22}V{db_y}L1247 {db_y}')
 # Middleware reaches business around the data area; it never queries those stores.
 c.path('M83 570L39 570V819L698 819')
 for col in range(3):
  x=62+col*215;last=848 if stage==1 else 946
  c.a.append(f'<path d="M{x-8} 819V{last}" fill="none" stroke="#56798e" stroke-width="1.8"/>')
  for row in range(1 if stage==1 else 3):c.path(f'M{x-8} {848+row*49}L{x} {848+row*49}')
 c.path('M884 570L875 570V837L909 837')
 c.a.append('<path d="M909 837V943" fill="none" stroke="#56798e" stroke-width="1.8"/>')
 for y in [865,904,943]:c.path(f'M909 {y}L917 {y}')
 c.box(743,516,93,119,['X-01','Control','de','cruces'],fill='#fff3dd')
 c.path('M743 574L681 574','cross dash');c.path('M836 574L868 574','cross dash')
 c.ico(664,558,'shield',26);c.ico(862,558,'shield',26)
 c.txt(28,995,'API: síncrono · Eventos / lotes: adaptadores · X-01: política en extremos',anchor='start');c.txt(1290,1016,'Borde · gateway · seguridad · observabilidad',anchor='end')
 c.save(stage)
if __name__=='__main__':
 for stage in (1,2):make(stage)
