"""Medida preventiva del paso D (escenario S7), decidida por el usuario el 2026-11-10: opción A con B de respaldo.

A: la capacitación E2 (1.13.3, 1.920 HH, 36 personas, 9 días desde H9) se divide en
   - 576 HH (30 %) adelantadas a M17, tras el diseño E2 aprobado (H8): procesos y reglas de E2,
     cambios de rol, módulos compartidos con E1 y formación de formadores; 6 personas (ritmo de E1);
   - 1.344 HH (70 %) desde H9 sobre el software E2 con QA, con las mismas 36 personas.
B: los formadores formados en M17 quedan como reserva para duplicar la dotación si hay atraso (S7).
   No cambia la red.
Método de duración del SD-07: techo((O_d + 4 M_d + P_d) / 6) con 7,5 / 6,8 / 5,1 HH por persona y día.
Uso: python3 -I ajuste_capacitacion_e2.py <Red_CPM v2> <Red_CPM destino>
"""
import sys, json, math, os
ORI, DST = sys.argv[1:3]
rd = lambda n: json.load(open(f'{ORI}/{n}', encoding='utf-8-sig'))
nodes, edges = rd('nodos.json'), rd('relaciones.json')
N = {n['id']: n for n in nodes}
dur = lambda hh, n: max(1, math.ceil((hh / (n * 7.5) + 4 * hh / (n * 6.8) + hh / (n * 5.1)) / 6))

k = '1.13.3:E2:E2:237'
o = N[k]
assert abs(o['hh'] - 1920) < 0.01, o['hh']
FRAC = 0.30
ant_hh = round(o['hh'] * FRAC, 2)
roles_ant = {'Formador': 3, 'Analista de negocio': 3}
ant = dict(id='F:1.13.3:E2-ANT', edt='1.13.3', stage='E2', phase='E2',
           name='Capacitación E2 anticipada: procesos, roles y formación de formadores · E2',
           calendar='LAB', release='2028-05-07', deadline_exclusive='2028-06-07',
           hh=ant_hh, productive_hh=ant_hh, included_coordination_hh=0.0,
           role_hh={r: round(ant_hh * p / 6, 2) for r, p in roles_ant.items()},
           proposed_people=6, proposed_roles=roles_ant, duration_days=dur(ant_hh, 6),
           duration_basis='Paso D, opción A: 30 % de la capacitación E2 que no depende del software (se apoya en H8)')
nodes.append(ant); N[ant['id']] = ant
# El resto queda desde H9 con la misma dotación
f = 1 - FRAC
o['hh'] = round(o['hh'] * f, 2)
o['productive_hh'] = round(o.get('productive_hh', o['hh'] / f) * f, 2)
o['role_hh'] = {r: round(h * f, 2) for r, h in o['role_hh'].items()}
o['duration_days'] = dur(o['hh'], o['proposed_people'])
o['duration_basis'] = o.get('duration_basis', '') + ' | Paso D, opción A: 70 % desde H9; 30 % adelantado a M17'
edges.append(dict(pred='A:H8', succ=ant['id'], type='FS', lag=0, lag_calendar='LAB',
                  basis='El contenido anticipado se basa en el diseño E2 aprobado'))
edges.append(dict(pred=ant['id'], succ=k, type='FS', lag=0, lag_calendar='LAB',
                  basis='La capacitación sobre el software se apoya en la anticipada'))
os.makedirs(DST, exist_ok=True)
json.dump(nodes, open(f'{DST}/nodos.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(edges, open(f'{DST}/relaciones.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(dict(anticipada=dict(hh=ant['hh'], dias=ant['duration_days']),
                      desde_H9=dict(hh=o['hh'], dias=o['duration_days'], personas=o['proposed_people']),
                      total=round(sum(n.get('hh', 0) for n in nodes), 2)), ensure_ascii=False))
