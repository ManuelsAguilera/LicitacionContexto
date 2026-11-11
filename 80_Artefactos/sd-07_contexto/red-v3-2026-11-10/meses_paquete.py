import sys,csv,json,re,collections
from bisect import bisect_left
T,V=sys.argv[1:3]
cals=json.load(open(T+'/Red_CPM/calendarios.json',encoding='utf-8-sig'))
MESES=[(int(m['mes']),m['inicio']) for m in csv.DictReader(open(T+'/Datos_base/dotacion_y_reservas_56_meses.csv',encoding='utf-8-sig'))]
INI=[m[1] for m in MESES]; mes=lambda d: MESES[bisect_left(INI,d+'z')-1][0]
def fmt(ms):
    ms=sorted(ms); out=[]; i=0
    while i<len(ms):
        j=i
        while j+1<len(ms) and ms[j+1]==ms[j]+1: j+=1
        out.append(str(ms[i]) if i==j else f'{ms[i]}--{ms[j]}'); i=j+1
    return '; '.join(out)
def meses(prog_rows):
    M=collections.defaultdict(set)
    for r in prog_rows:
        if float(r['HH'] or 0)<=0 or not r['edt']: continue
        ds=cals[r['calendario']]; dias=ds[bisect_left(ds,r['inicio']):bisect_left(ds,r['fin_exclusivo'])]
        for d in dias: M[r['edt']].add(mes(d))
    return {k:fmt(v) for k,v in M.items()}
if __name__=='__main__':
    p=list(csv.DictReader(open(V+'/programacion_v3.csv',encoding='utf-8-sig'),delimiter=';'))
    json.dump(meses(p),open(sys.argv[3],'w'),ensure_ascii=False,indent=0)
