"""Escenarios S8–S12 sobre la red v3 con el mismo método de escenarios.py, más la variante de horas extra
(2 h diarias, recargo 50 %: duración × 0,8 y costo equivalente al 10 % de las HH)."""
import sys, json, copy, math
src = open(sys.argv[3], encoding='utf-8').read()
src = src.split("ESC = {")[0]
sys.argv = [sys.argv[0], sys.argv[1], sys.argv[2]]
g = {}; exec(src, g)
NODES, EDGES, programar, impacto = g['NODES'], g['EDGES'], g['programar'], g['impacto']
def escenario(driver, crash=False, extra_h=False):
    nodes = copy.deepcopy(NODES); N = {n['id']: n for n in nodes}; d = N[driver]
    dur = int(math.ceil(float(d['duration_days']))) + 10
    hh = 0.0; rec = 0.0
    if crash:
        dur = max(1, math.ceil(dur * 1.15 / 2)); hh += 0.15 * d['hh']
    if extra_h:
        dur = max(1, math.ceil(dur * 0.8)); rec += 0.10 * d['hh']
    d['duration_days'] = dur
    _, sch = programar(nodes, EDGES)
    imp, otros = impacto(sch)
    return imp, round(hh, 1), round(rec, 1)
ESC = {'Aceptación 28 criterios E1 (1.9.6)': '1.9.6:E1:E1:221', 'Aceptación 28 criterios E2 (1.9.6)': '1.9.6:E2:E2:222',
       'Capacitación E1 (1.13.3)': '1.13.3:E1:E1:236', 'Pruebas lockers (1.10.1.6)': '1.10.1.6:E2:E2:589',
       'Pruebas probadores (1.10.5.6)': '1.10.5.6:E2:E2:682'}
for nombre, k in ESC.items():
    hh = next(n['hh'] for n in NODES if n['id'] == k)
    print(nombre, 'HH', hh)
    for et, kw in [('sin', {}), ('intens', {'crash': True}), ('extra', {'extra_h': True}), ('intens+extra', {'crash': True, 'extra_h': True})]:
        print('  ', et, escenario(k, **kw))
