"""Enrutamiento ortogonal con puertos de borde y obstáculos rectangulares."""
from bisect import bisect_left
import heapq


def segmento_libre(a, b, obstacles):
    x,y=a;xx,yy=b
    for l,t,r,bt in obstacles:
        if y==yy and t<y<bt and max(min(x,xx),l)<min(max(x,xx),r):return False
        if x==xx and l<x<r and max(min(y,yy),t)<min(max(y,yy),bt):return False
    return True


def simplificar(points):
    out=[]
    for p in points:
        if out and p==out[-1]:continue
        while len(out)>1 and ((out[-2][0]==out[-1][0]==p[0]) or (out[-2][1]==out[-1][1]==p[1])):out.pop()
        out.append(p)
    return out


def enrutar(pos, edges, labels=()):
    sides={};buckets={}
    for i,e in enumerate(edges):
        x,y,w,h=pos[e['de']];xx,yy,ww,hh=pos[e['a']]
        if x+w<=xx:s,t='right','left'
        elif xx+ww<=x:s,t='left','right'
        elif y+h<=yy:s,t='bottom','top'
        else:s,t='top','bottom'
        sides[i]=(s,t)
        buckets.setdefault((e['de'],s),[]).append((i,0))
        buckets.setdefault((e['a'],t),[]).append((i,1))
    ports={}
    normals={'left':(-1,0),'right':(1,0),'top':(0,-1),'bottom':(0,1)}
    for (node,side),es in buckets.items():
        x,y,w,h=pos[node]
        for j,key in enumerate(es):
            f=round(.15+.7*(j+1)/(len(es)+1),4)
            nx,ny={'left':(0,f),'right':(1,f),'top':(f,0),'bottom':(f,1)}[side]
            bx,by=round(x+w*nx,3),round(y+h*ny,3)
            dx,dy=normals[side]
            ports[key]={'point':(bx+3*dx,by+3*dy),'stub':(bx+12*dx,by+12*dy),'anchor':(nx,ny),'offset':(3*dx,3*dy)}
    obstacles=[(x-6,y-6,x+w+6,y+h+6) for x,y,w,h in pos.values()]+list(labels)
    xs={15,385,770,1320,1340,1360,1890,1910,2525};ys={210,715,1290,1785}
    for l,t,r,b in obstacles:xs.update((l,r));ys.update((t,b))
    for p in ports.values():xs.add(p['stub'][0]);ys.add(p['stub'][1])
    xs=sorted(xs);ys=sorted(ys);cache={}
    def allowed(a,b):
        key=tuple(sorted((a,b)))
        if key not in cache:cache[key]=segmento_libre((xs[a[0]],ys[a[1]]),(xs[b[0]],ys[b[1]]),obstacles)
        return cache[key]
    routes=[]
    for i,e in enumerate(edges):
        p,q=ports[i,0],ports[i,1];start=p['stub'];end=q['stub']
        src=(bisect_left(xs,start[0]),bisect_left(ys,start[1]));dst=(bisect_left(xs,end[0]),bisect_left(ys,end[1]))
        def heuristic(v):return abs(xs[v[0]]-end[0])+abs(ys[v[1]]-end[1])
        initial=(src,0);scores={initial:0};prev={};queue=[(heuristic(src),0,src,0)];last=None
        while queue:
            _,cost,v,axis=heapq.heappop(queue)
            if cost>scores.get((v,axis),float('inf')):continue
            if v==dst:last=(v,axis);break
            for dx,dy,newaxis in ((1,0,1),(-1,0,1),(0,1,2),(0,-1,2)):
                z=(v[0]+dx,v[1]+dy)
                if not (0<=z[0]<len(xs) and 0<=z[1]<len(ys)) or not allowed(v,z):continue
                step=abs(xs[z[0]]-xs[v[0]])+abs(ys[z[1]]-ys[v[1]])+(35 if axis and axis!=newaxis else 0)
                nc=cost+step;state=(z,newaxis)
                if nc<scores.get(state,float('inf')):
                    scores[state]=nc;prev[state]=(v,axis);heapq.heappush(queue,(nc+heuristic(z),nc,z,newaxis))
        if last is None:raise ValueError('No hay ruta despejada: '+e['de']+' -> '+e['a'])
        path=[]
        while last!=initial:
            v,_=last;path.append((xs[v[0]],ys[v[1]]));last=prev[last]
        path.append(start);path.reverse()
        points=simplificar([p['point']]+path+[q['point']])
        # La ruta completa no atraviesa ninguna tarjeta, ni siquiera su origen/destino.
        boxes=[(x,y,x+w,y+h) for x,y,w,h in pos.values()]
        if not all(segmento_libre(a,b,boxes+list(labels)) for a,b in zip(points,points[1:])):
            raise ValueError('Ruta invade un elemento: '+e['de']+' -> '+e['a'])
        routes.append({'points':points,'source':p,'target':q})
    return routes
