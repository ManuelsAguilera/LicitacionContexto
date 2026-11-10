"""Matriz HH y FTE por rol y mes tras la estabilización.

Para cada actividad movida: resta sus HH reales (registro diario por persona) y suma
sus HH repartidas uniformemente en los días de su calendario en la nueva ventana.
Las actividades no movidas y los demás componentes quedan idénticos.
Uso: python3 -I matriz_estabilizada.py <dir traspaso> <estabilizacion.json> <dir salida>
"""
import sys, json, csv, collections
from decimal import Decimal
from bisect import bisect_left

T, E, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, T + '/Red_CPM/verificacion')
from motor_cpm_verificado_20261105 import Network

COORD = 'Líder técnico / coordinación de desarrollo'
def roles_hh(n):
    """HH por rol de un nodo; la coordinación incluida va al líder técnico."""
    r = dict(n.get('role_hh') or {})
    extra = float(n.get('hh', 0)) - sum(r.values())
    if extra > 0.005:
        r[COORD] = r.get(COORD, 0) + extra
    return r

rd = lambda p: json.load(open(p, encoding='utf-8-sig'))
nodes = rd(T + '/Red_CPM/nodos.json'); cals = rd(T + '/Red_CPM/calendarios.json')
net = Network(nodes, rd(T + '/Red_CPM/relaciones.json'), cals)
names = rd(T + '/Datos_base/equivalencias_nombres_E26.json')
est = rd(E)
num = lambda s: Decimal(s.replace('.', '').replace(',', '.'))

MESES = [(int(m['mes']), m['inicio']) for m in
         csv.DictReader(open(T + '/Datos_base/dotacion_y_reservas_56_meses.csv', encoding='utf-8-sig'))]
INI = [m[1] for m in MESES]
mes = lambda ds: MESES[bisect_left(INI, ds + 'z') - 1][0]

# Matriz original por rol (formato del traspaso)
orig = list(csv.DictReader(open(T + '/HH_matriz_roles_M1_M56.csv', encoding='utf-8-sig'), delimiter=';'))
hh = {r['Rol']: [num(r[f'M{m}']) for m in range(1, 57)] for r in orig}

movidas = est['cambios']
quitado = collections.defaultdict(Decimal); agregado = collections.defaultdict(Decimal)
for r in csv.DictReader(open(T + '/Red_CPM/personas_trabajo_y_reservas.csv', encoding='utf-8-sig')):
    if r['actividad'] in movidas:
        quitado[(names.get(r['perfil'], r['perfil']), mes(r['fecha']))] += Decimal(r['HH_trabajo'])
for k, c in movidas.items():
    n = net.nodes[k]
    ds = cals[n['calendar']]
    fin = net.finish(k, c['despues'])
    dias = ds[bisect_left(ds, c['despues']):bisect_left(ds, fin)]
    for rol, h in roles_hh(n).items():
        for d in dias:
            agregado[(names.get(rol, rol), mes(d))] += Decimal(str(h)) / len(dias)

# Control: lo quitado por actividad debe igualar sus HH
assert abs(sum(quitado.values()) - sum(Decimal(str(net.nodes[k]['hh'])) for k in movidas)) < Decimal('0.05'), \
    (sum(quitado.values()), sum(Decimal(str(net.nodes[k]['hh'])) for k in movidas))
for (rol, m), v in quitado.items():
    hh[rol][m - 1] -= v
for (rol, m), v in agregado.items():
    hh.setdefault(rol, [Decimal(0)] * 56)[m - 1] += v

neg = [(r, m + 1, float(v)) for r, vs in hh.items() for m, v in enumerate(vs) if v < Decimal('-0.01')]
assert not neg, neg[:5]
total = sum(sum(v) for v in hh.values())

fmt = lambda x: f'{x:.2f}'.replace('.', ',')
def escribir(nombre, div):
    with open(f'{OUT}/{nombre}', 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(['Rol'] + [f'M{m}' for m in range(1, 57)] + ['Total' if div != 1 else 'Total HH'])
        for rol in sorted(hh):
            vals = [max(v, Decimal(0)) / div for v in hh[rol]]
            w.writerow([rol] + [fmt(v) for v in vals] + [fmt(sum(vals))])
escribir('HH_matriz_roles_M1_M56_estabilizada.csv', Decimal(1))
escribir('FTE_matriz_roles_M1_M56_estabilizada.csv', Decimal(160))
print(json.dumps(dict(total_HH=float(round(total, 2)), roles=len(hh),
                      HH_reubicadas=float(round(sum(quitado.values()), 2)))))
