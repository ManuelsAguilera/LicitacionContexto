from math import *
def gc(a,b):
    la1,lo1,la2,lo2=map(radians,(*a,*b))
    d=2*asin(sqrt(sin((la2-la1)/2)**2+cos(la1)*cos(la2)*sin((lo2-lo1)/2)**2))
    return 6371*d
V=200000.0  # km/s luz en fibra (~c/1.5)
SP=(-23.55,-46.63); SCL=(-33.45,-70.67); QRO=(20.59,-100.39)
# (nombre, coord aproximada del datacenter, RTT publicado P50 desde Brazil South)
bz=[("East US (Virginia)",(37.4,-79.5),118),("East US 2 (Virginia)",(36.7,-78.4),117),
("South Central US (Texas)",(29.4,-98.5),139),("Central US (Iowa)",(41.6,-93.6),149),
("Canada Central (Toronto)",(43.7,-79.4),129),("Mexico Central (Queretaro)",QRO,156),
("West US (California)",(37.8,-122.4),169),("West US 2 (Washington)",(47.2,-119.9),177),
("UK South (Londres)",(51.5,-0.1),185),("West Europe (Paises Bajos)",(52.4,4.9),196),
("France Central (Paris)",(48.9,2.4),186),("Germany WC (Frankfurt)",(50.1,8.7),198)]
print("Brazil South ->  | km (circulo maximo) | RTT minimo teorico ms | RTT publicado | factor real/teorico")
fs=[]
for n,c,r in bz:
    d=gc(SP,c); t=2*d/V*1000; f=r/t; fs.append(f)
    print(f"{n:28s} {d:7.0f} {t:7.1f} {r:5d} {f:5.2f}")
print("factor min/mediana/max:",round(min(fs),2),round(sorted(fs)[len(fs)//2],2),round(max(fs),2))
d=gc(SP,SCL); t=2*d/V*1000
print("Santiago-SaoPaulo km",round(d),"teorico ms",round(t,1))
for f in (min(fs),sorted(fs)[len(fs)//2],max(fs)):
    print("  con factor",round(f,2),"->",round(t*f,1),"ms")
# Mexico Central -> South Central US (22 ms) como caso corto
print("Mexico Central-South Central US km",round(gc(QRO,(29.4,-98.5))),"teorico",round(2*gc(QRO,(29.4,-98.5))/V*1000,1),"publ 22")
