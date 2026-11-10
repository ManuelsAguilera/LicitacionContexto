"""Estabilización de recursos (PMBOK 6.5.2.3) sobre la red CPM del traspaso SD-07.

Mueve actividades solo dentro de [ES, LS] usando proposed_start del motor del equipo.
No cambia duraciones, HH, relaciones ni fechas de hitos. Uso:
  python3 -I estabilizar.py <dir Red_CPM> <dir Datos_base> <archivo salida json> [margen_dias]
"""
import sys, json, csv, collections
from datetime import date, timedelta
from bisect import bisect_left

RED, BASE, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, RED + '/verificacion')
from motor_cpm_verificado_20261105 import Network

COORD = 'Líder técnico / coordinación de desarrollo'
def roles_hh(n):
    """HH por rol de un nodo; la coordinación incluida va al líder técnico."""
    r = dict(n.get('role_hh') or {})
    extra = float(n.get('hh', 0)) - sum(r.values())
    if extra > 0.005:
        r[COORD] = r.get(COORD, 0) + extra
    return r

rd = lambda n: json.load(open(f'{RED}/{n}', encoding='utf-8-sig'))
nodes, edges, cals = rd('nodos.json'), rd('relaciones.json'), rd('calendarios.json')
net = Network(nodes, edges, cals)
cpm = {r['id']: r for r in net.calculate()}

def preferir(k, fecha):
    # schedule_preferred() lee la preferencia desde net.result (copia hecha en calculate()).
    net.nodes[k]['proposed_start'] = fecha
    net.result[k]['proposed_start'] = fecha

MESES = [(int(m['mes']), m['inicio'], m['fin_exclusivo'])
         for m in csv.DictReader(open(f'{BASE}/dotacion_y_reservas_56_meses.csv', encoding='utf-8-sig'))]
INI = [m[1] for m in MESES]
def mes(ds):
    return MESES[bisect_left(INI, ds + 'z') - 1][0]

GRUPO = {'Desarrollador': 'Desarrollo', 'Líder técnico / coordinación de desarrollo': 'Desarrollo',
         'Arquitecto / diseñador técnico': 'Arquitectura', 'Analista de negocio': 'Análisis',
         'Ingeniero QA': 'Calidad', 'QA / probador': 'Calidad', 'Especialista de datos': 'Datos',
         'Científico de datos / ML': 'Datos', 'SRE / plataforma': 'Plataforma'}
grupo = lambda r: GRUPO.get(r, 'Otros')

cache = {}
def carga(k, start, finish):
    """HH por (mes, grupo) repartidas uniformemente en los días de su calendario."""
    key = (k, start)
    if key in cache:
        return cache[key]
    n = net.nodes[k]
    out = collections.defaultdict(float)
    if n.get('hh') and n['duration_days']:
        ds = cals[n['calendar']]
        dias = ds[bisect_left(ds, start):bisect_left(ds, finish)]
        if dias:
            for rol, hh in roles_hh(n).items():
                for d in dias:
                    out[(mes(d), grupo(rol))] += hh / len(dias)
    cache[key] = out
    return out

def perfil(sched):
    tot = collections.defaultdict(float)
    for k, r in sched.items():
        for kk, v in carga(k, r['start'], r['finish']).items():
            tot[kk] += v
    return tot

# Cargas fijas que no son actividades de la red (campo, dirección, inducción, operación)
fijo = collections.defaultdict(float)
for r in csv.DictReader(open(f'{RED}/../HH_detalle_mes_rol_componente.csv', encoding='utf-8-sig'), delimiter=';'):
    if r['Componente'] != 'Trabajo técnico y viajes':
        fijo[int(r['Mes'][1:])] += float(r['HH'].replace('.', '').replace(',', '.'))

def programar():
    return {r['id']: r for r in net.schedule_preferred()}

base = programar()
HITOS = {k: base[k]['finish'] for k in base if k.startswith('A:H') or k == 'A:Z' or 'MB_REAL' in k}

VENT = range(13, 19)  # E2 y marcha blanca E1: M13–M18
def total_mes(p, m):
    return sum(v for (mm, g), v in p.items() if mm == m) + fijo[m]
def objetivo(sched):
    # Estabilización por tipo de recurso: cada grupo de roles por separado.
    # La cobertura de campo (implantadores y formadores) son otras personas y no entra.
    p = perfil(sched)
    return sum(v ** 2 for (m, g), v in p.items() if m in VENT), p

MARGEN = int(sys.argv[4]) if len(sys.argv) > 4 else 0  # días de su calendario

def margen(k, start):
    """Días del calendario de la actividad entre su inicio y su inicio tardío."""
    dom = net.domains[k]
    return bisect_left(dom, cpm[k]['LS']) - bisect_left(dom, start)

def valido(sched):
    for k, r in sched.items():
        if r.get('late_scheduled') or r['start'] > cpm[k]['LS']:
            return False
        # Una actividad desplazada debe conservar MARGEN días, o al menos el que ya tenía.
        if MARGEN and r['start'] != base[k]['start'] and net.nodes[k].get('duration_days'):
            if margen(k, r['start']) < min(MARGEN, margen(k, base[k]['start'])):
                return False
    return all(sched[k]['finish'] == v for k, v in HITOS.items())

obj0, p0 = objetivo(base)
movibles = [k for k, r in base.items()
            if net.nodes[k].get('hh', 0) > 0 and cpm[k]['slack_days'] > 0
            and (13 <= mes(r['start']) <= 18 or 13 <= mes(cpm[k]['LS']) <= 18)]
movibles.sort(key=lambda k: -net.nodes[k]['hh'])

mejor, sched = obj0, base
for vuelta in range(3):
    cambio = False
    for k in movibles:
        dom = net.domains[k]
        i0, i1 = bisect_left(dom, cpm[k]['ES']), bisect_left(dom, cpm[k]['LS'])
        actual = net.result[k].get('proposed_start', cpm[k]['ES'])
        paso = max(1, (i1 - i0) // 12)
        for i in list(range(i0, i1 + 1, paso)) + [i1]:
            preferir(k, dom[i])
            s = programar()
            if not valido(s):
                continue
            o, _ = objetivo(s)
            if o < mejor - 1e-6:
                mejor, sched, actual, cambio = o, s, dom[i], True
        preferir(k, actual)
    if not cambio:
        break

sched = programar()
assert valido(sched)
p1 = perfil(sched)
movidas = {k: (base[k]['start'], sched[k]['start']) for k in sched if sched[k]['start'] != base[k]['start']}
grupos = sorted({g for (_, g) in list(p0) + list(p1)})
res = dict(
    movibles=len(movibles), movidas=len(movidas),
    hh_movidas=round(sum(net.nodes[k]['hh'] for k in movidas), 2),
    hitos_intactos=all(sched[k]['finish'] == v for k, v in HITOS.items()), hitos=HITOS,
    sobre_LS=sum(sched[k]['start'] > cpm[k]['LS'] for k in sched),
    meses={m: dict(antes=round(total_mes(p0, m), 1), despues=round(total_mes(p1, m), 1),
                   fijo=round(fijo[m], 1),
                   antes_grupo={g: round(p0[(m, g)], 1) for g in grupos},
                   despues_grupo={g: round(p1[(m, g)], 1) for g in grupos}) for m in range(1, 57)},
    cambios={k: dict(antes=a, despues=b, ES=cpm[k]['ES'], LS=cpm[k]['LS'], hh=net.nodes[k]['hh'],
                     nombre=net.nodes[k].get('name', '')) for k, (a, b) in movidas.items()},
    proposed_start={k: net.result[k].get('proposed_start') for k in net.nodes},
)
json.dump(res, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: res[k] for k in ['movibles', 'movidas', 'hh_movidas', 'hitos_intactos', 'sobre_LS']}))
for m in range(12, 20):
    x = res['meses'][m]
    print(f"M{m}: antes {x['antes']/160:5.1f} FTE  después {x['despues']/160:5.1f} FTE  (fijo {x['fijo']/160:5.1f})")
