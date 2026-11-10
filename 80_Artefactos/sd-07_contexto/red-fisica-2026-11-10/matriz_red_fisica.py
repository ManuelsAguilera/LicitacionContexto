"""Matriz HH y FTE por rol y mes de la red ampliada y estabilizada.

Compara la programación final contra la programación original del traspaso:
  - actividades originales que cambiaron de inicio: resta sus HH reales (registro diario)
    y suma sus HH repartidas uniformemente en su nueva ventana;
  - actividades nuevas (F:*): suma sus HH repartidas uniformemente.
El resto de la matriz original queda idéntico.
Uso: python3 -I matriz_red_fisica.py <dir traspaso> <dir red ampliada (Red_CPM)> <estabilizacion.json> <dir salida>
"""
import sys, json, csv, collections
from decimal import Decimal
from bisect import bisect_left

T, RED, E, OUT = sys.argv[1:5]
sys.path.insert(0, T + '/Red_CPM/verificacion')
from motor_cpm_verificado_20261105 import Network

COORD = 'Líder técnico / coordinación de desarrollo'
def roles_hh(n):
    r = dict(n.get('role_hh') or {})
    extra = float(n.get('hh', 0)) - sum(r.values())
    if extra > 0.005:
        r[COORD] = r.get(COORD, 0) + extra
    return r

rd = lambda p: json.load(open(p, encoding='utf-8-sig'))
cals = rd(T + '/Red_CPM/calendarios.json')
net = Network(rd(RED + '/nodos.json'), rd(RED + '/relaciones.json'), cals)
net.calculate()
for k, v in rd(E)['proposed_start'].items():
    if v is not None:
        net.result[k]['proposed_start'] = v
final = {r['id']: r for r in net.schedule_preferred()}
orig = {r['id']: r for r in rd(T + '/Red_CPM/programacion.json')}
names = rd(T + '/Datos_base/equivalencias_nombres_E26.json')
num = lambda s: Decimal(s.replace('.', '').replace(',', '.'))

MESES = [(int(m['mes']), m['inicio']) for m in
         csv.DictReader(open(T + '/Datos_base/dotacion_y_reservas_56_meses.csv', encoding='utf-8-sig'))]
INI = [m[1] for m in MESES]
mes = lambda ds: MESES[bisect_left(INI, ds + 'z') - 1][0]

hh = {r['Rol']: [num(r[f'M{m}']) for m in range(1, 57)] for r in
      csv.DictReader(open(T + '/HH_matriz_roles_M1_M56.csv', encoding='utf-8-sig'), delimiter=';')}

cambiadas = {k for k in orig if final[k]['start'] != orig[k]['start'] and net.nodes[k].get('hh', 0) > 0}
nuevas = {k for k in final if k not in orig and net.nodes[k].get('hh', 0) > 0}

quitado = collections.defaultdict(Decimal)
for r in csv.DictReader(open(T + '/Red_CPM/personas_trabajo_y_reservas.csv', encoding='utf-8-sig')):
    if r['actividad'] in cambiadas:
        quitado[(names.get(r['perfil'], r['perfil']), mes(r['fecha']))] += Decimal(r['HH_trabajo'])
esperado = sum(Decimal(str(net.nodes[k]['hh'])) for k in cambiadas)
assert abs(sum(quitado.values()) - esperado) < Decimal('0.05'), (sum(quitado.values()), esperado)

agregado = collections.defaultdict(Decimal)
for k in cambiadas | nuevas:
    n = net.nodes[k]; ds = cals[n['calendar']]
    dias = ds[bisect_left(ds, final[k]['start']):bisect_left(ds, final[k]['finish'])]
    for rol, h in roles_hh(n).items():
        for d in dias:
            agregado[(names.get(rol, rol), mes(d))] += Decimal(str(h)) / len(dias)

for (rol, m), v in quitado.items():
    hh[rol][m - 1] -= v
for (rol, m), v in agregado.items():
    hh.setdefault(rol, [Decimal(0)] * 56)[m - 1] += v
neg = [(r, m + 1, float(v)) for r, vs in hh.items() for m, v in enumerate(vs) if v < Decimal('-0.01')]
assert not neg, neg[:5]

fmt = lambda x: f'{x:.2f}'.replace('.', ',')
def escribir(nombre, div):
    with open(f'{OUT}/{nombre}', 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(['Rol'] + [f'M{m}' for m in range(1, 57)] + ['Total HH' if div == 1 else 'Total'])
        for rol in sorted(hh):
            vals = [max(v, Decimal(0)) / div for v in hh[rol]]
            w.writerow([rol] + [fmt(v) for v in vals] + [fmt(sum(vals))])
escribir('HH_matriz_roles_M1_M56.csv', Decimal(1))
escribir('FTE_matriz_roles_M1_M56.csv', Decimal(160))
print(json.dumps(dict(total_HH=float(round(sum(sum(v) for v in hh.values()), 2)), roles=len(hh),
                      actividades_cambiadas=len(cambiadas), actividades_nuevas=len(nuevas),
                      HH_nuevas=float(round(sum(Decimal(str(net.nodes[k]['hh'])) for k in nuevas), 2)))))
