"""Selecciona puertos visibles antes de recurrir al enrutado ortogonal A*."""
from router_legible import segmento_libre, simplificar

NORMALS={'left':(-1,0),'right':(1,0),'top':(0,-1),'bottom':(0,1)}

def puerto(box,side,f):
    x,y,w,h=box
    ax,ay={'left':(0,f),'right':(1,f),'top':(f,0),'bottom':(f,1)}[side]
    bx,by=round(x+w*ax,3),round(y+h*ay,3);dx,dy=NORMALS[side]
    return dict(point=(bx+3*dx,by+3*dy),stub=(bx+12*dx,by+12*dy),anchor=(ax,ay),offset=(3*dx,3*dy))

def candidatos_simples(pos,edges,labels,groups):
    allpos=dict(pos,**(groups or {}));real=[(x,y,x+w,y+h) for x,y,w,h in pos.values()]
    selected={};occupied={}
    for i,e in enumerate(edges):
        a,b=e['de'],e['a'];box=allpos[a];other=allpos[b]
        x,y,w,h=box;xx,yy,ww,hh=other
        obstacles=real+list(labels)
        clearance=[(px-6,py-6,px+pw+6,py+ph+6) for id,(px,py,pw,ph) in pos.items() if id not in (a,b)]+list(labels)
        options=[]
        def consider(side,t,pa,pb,points):
            points=simplificar(points)
            if len(points)<2:return
            dx,dy=NORMALS[side];vx,vy=points[1][0]-points[0][0],points[1][1]-points[0][1]
            tx,ty=NORMALS[t];ex,ey=points[-2][0]-points[-1][0],points[-2][1]-points[-1][1]
            if vx*dx+vy*dy<=0 or ex*tx+ey*ty<=0:return
            if not all(segmento_libre(p,q,obstacles) and segmento_libre(p,q,clearance) for p,q in zip(points,points[1:])):return
            length=sum(abs(p[0]-q[0])+abs(p[1]-q[1]) for p,q in zip(points,points[1:]))
            score=length+100*(len(points)-2)
            for id,port in [(a,pa),(b,pb)]:
                for old in occupied.get(id,[]):
                    if abs(old[0]-port['point'][0])+abs(old[1]-port['point'][1])<10:score+=35
            options.append((score,len(points),side,t,pa,pb,points))
        # Rectas horizontales y verticales: alinear ambos puertos sobre una
        # coordenada libre, en vez de fijarlos por separado al centro de cada caja.
        if x+w<=xx or xx+ww<=x:
            lo,hi=max(y,yy)+8,min(y+h,yy+hh)-8
            if lo<=hi:
                levels={(lo+hi)/2,lo,hi}
                for l,top,r,bottom in clearance:
                    levels.update(v for v in [top-1,bottom+1] if lo<=v<=hi)
                side,t=('right','left') if x+w<=xx else ('left','right')
                for v in sorted(levels):
                    pa=puerto(box,side,(v-y)/h);pb=puerto(other,t,(v-yy)/hh)
                    consider(side,t,pa,pb,[pa['point'],pb['point']])
        if y+h<=yy or yy+hh<=y:
            lo,hi=max(x,xx)+8,min(x+w,xx+ww)-8
            if lo<=hi:
                levels={(lo+hi)/2,lo,hi}
                for l,top,r,bottom in clearance:levels.update(v for v in [l-1,r+1] if lo<=v<=hi)
                side,t=('bottom','top') if y+h<=yy else ('top','bottom')
                for v in sorted(levels):
                    pa=puerto(box,side,(v-x)/w);pb=puerto(other,t,(v-xx)/ww)
                    consider(side,t,pa,pb,[pa['point'],pb['point']])
        # Probar salidas por los cuatro bordes y solo un codo. Esto permite
        # salir por debajo cuando evita la vuelta lateral de una columna.
        for side in NORMALS:
            for t in NORMALS:
                for f in [.2,.5,.8]:
                    for ff in [.2,.5,.8]:
                        pa=puerto(box,side,f);pb=puerto(other,t,ff);p,q=pa['point'],pb['point']
                        consider(side,t,pa,pb,[p,(p[0],q[1]),q])
                        consider(side,t,pa,pb,[p,(q[0],p[1]),q])
        if options:
            _,_,_,_,pa,pb,points=min(options,key=lambda o:(o[0],o[1]))
            selected[i]=dict(points=points,source=pa,target=pb)
            occupied.setdefault(a,[]).append(pa['point']);occupied.setdefault(b,[]).append(pb['point'])
    return selected
