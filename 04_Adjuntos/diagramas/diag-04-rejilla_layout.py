"""Layout en rejilla para las figuras Graphviz de SD-04 (4.10 a 4.12).

Lee un .dot con atributos gx,gy en los nodos (columna, fila), mide los nodos con dot y escribe
un .dot con pos/bb listo para `neato -n -Tpdf`. Uso:
    python diag-04-rejilla_layout.py entrada.rejilla.dot salida.dot [gapx gapy pad]
"""
import json,subprocess,sys,re
src,out=sys.argv[1],sys.argv[2]
gapx=float(sys.argv[3]) if len(sys.argv)>3 else 60
gapy=float(sys.argv[4]) if len(sys.argv)>4 else 40
pad=float(sys.argv[5]) if len(sys.argv)>5 else 14
txt=open(src,encoding='utf8').read()
j=json.loads(subprocess.run(['dot','-Tjson0',src],capture_output=True,text=True,encoding='utf8').stdout)
nodes={}
for o in j['objects']:
    if 'gx' in o:
        nodes[o['name']]=dict(gx=float(o['gx']),gy=float(o['gy']),gy2=float(o.get('gy2',o['gy'])),w=float(o['width'])*72,h=float(o['height'])*72)
cols={};rows={}
for n,d in nodes.items():
    cols[d['gx']]=max(cols.get(d['gx'],0),d['w'])
    rows[d['gy']]=max(rows.get(d['gy'],0),d['h'] if d['gy2']==d['gy'] else 0)
    rows.setdefault(d['gy2'],0)
gg=j.get('gxgaps','');gyg=j.get('gygaps','')
xg={int(a):float(b) for a,b in (t.split(':') for t in gg.split(',') if t)}
yg={int(a):float(b) for a,b in (t.split(':') for t in gyg.split(',') if t)}
cx={};x=0
for g in sorted(cols): cx[g]=x+cols[g]/2; x+=cols[g]+xg.get(int(g),gapx)
ry={};y=0
for g in sorted(rows): ry[g]=y+rows[g]/2; y+=rows[g]+yg.get(int(g),gapy)
pos={n:(cx[d['gx']],-(ry[d['gy']]+ry[d['gy2']])/2) for n,d in nodes.items()}
extra=[]
for n,(px,py) in pos.items(): extra.append(f'  {n} [pos="{px:.1f},{py:.1f}"];')
# clusters
clusters={}
def walk(o):
    pass
for o in j['objects']:
    if o['name'].startswith('cluster'):
        names=[j['objects'][i]['name'] for i in o.get('nodes',[])] if 'nodes' in o else []
        clusters[o['name']]=names
minx=1e9;miny=1e9;maxx=-1e9;maxy=-1e9
bbs={}
for c,names in clusters.items():
    ns=[n for n in names if n in pos]
    if not ns: continue
    x0=min(pos[n][0]-nodes[n]['w']/2 for n in ns)-pad
    x1=max(pos[n][0]+nodes[n]['w']/2 for n in ns)+pad
    y0=min(pos[n][1]-nodes[n]['h']/2 for n in ns)-pad
    lab0=[o for o in j['objects'] if o['name']==c][0].get('label','')
    y1=max(pos[n][1]+nodes[n]['h']/2 for n in ns)+pad+12+19*(lab0.count(chr(92)+'n')+1)
    lab=[o for o in j['objects'] if o['name']==c][0]
    need=max(len(t) for t in lab.get('label','').split(chr(92)+'n'))*float(lab.get('fontsize',16))*0.53+24
    if x1-x0<need:
        mid=(x0+x1)/2; x0=mid-need/2; x1=mid+need/2
    bbs[c]=(x0,y0,x1,y1)
for n,(px,py) in pos.items():
    minx=min(minx,px-nodes[n]['w']/2);maxx=max(maxx,px+nodes[n]['w']/2)
    miny=min(miny,py-nodes[n]['h']/2);maxy=max(maxy,py+nodes[n]['h']/2)
for b in bbs.values():
    minx=min(minx,b[0]);maxx=max(maxx,b[2]);miny=min(miny,b[1]);maxy=max(maxy,b[3])
for c,b in bbs.items():
    extra.append(f'  subgraph {c} {{ bb="{b[0]:.1f},{b[1]:.1f},{b[2]:.1f},{b[3]:.1f}"; }}')
extra.append(f'  graph [margin=0, bb="{minx-6:.1f},{miny-6:.1f},{maxx+6:.1f},{maxy+6:.1f}"];')
def _lp(m):
    t,h,f=m.group(1),m.group(3),float(m.group(5))
    (x0,y0),(x1,y1)=pos[t],pos[h]
    return m.group(0).replace('lpf='+m.group(5),'lp="%.1f,%.1f"'%(x0+(x1-x0)*f,y0+(y1-y0)*f+14))
txt=re.sub(r'(\w+)( -> )(\w+) \[([^\]]*?)lpf=([\d.]+)',_lp,txt)
i=txt.rindex('}')
open(out,'w',encoding='utf8').write(txt[:i]+'\n'+'\n'.join(extra)+'\n}\n')
print('size',round(maxx-minx+12),round(maxy-miny+12))
