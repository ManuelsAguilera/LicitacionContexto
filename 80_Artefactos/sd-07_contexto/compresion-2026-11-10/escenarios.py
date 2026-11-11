"""Paso D: escenarios «¿qué pasa si…?» y compresión (PMBOK 6.5.2.4 y 6.5.2.6) sobre la red v2.

Supuestos validados por el usuario (2026-11-10):
  - Atraso de prueba: 10 días hábiles (14 días corridos en plazos de proveedor).
  - Intensificación: hasta 2× personas; +15 % HH sobre lo comprimido (rendimientos decrecientes, PMBOK p. 197).
  - Ejecución rápida: FS discrecional → SS con desfase del 50 % de la predecesora; +10 % HH de retrabajo en la sucesora.
Uso: python3 -I escenarios.py <traspaso> <dir red v2>
"""
import sys, json, copy, math
T, RV = sys.argv[1:3]
sys.path.insert(0, T + '/Red_CPM/verificacion')
from motor_cpm_verificado_20261105 import Network

rd = lambda p: json.load(open(p, encoding='utf-8-sig'))
NODES = rd(RV + '/Red_CPM/nodos.json'); EDGES = rd(RV + '/Red_CPM/relaciones.json')
CALS = rd(T + '/Red_CPM/calendarios.json'); PREF = rd(RV + '/estabilizacion.json')['proposed_start']
ATRASO = 10

def programar(nodes, edges):
    net = Network(nodes, edges, CALS); net.calculate()
    for k, v in PREF.items():
        if v is not None and k in net.result:
            net.result[k]['proposed_start'] = v
    return net, {r['id']: r for r in net.schedule_preferred()}

base_net, BASE = programar(NODES, EDGES)
HITOS = sorted([k for k in BASE if k.startswith('A:H') and k[3:].isdigit()], key=lambda k: int(k[3:]))
from datetime import date
dias = lambda a, b: (date.fromisoformat(a) - date.fromisoformat(b)).days

def impacto(sch):
    out = {}
    for h in HITOS:
        d = dias(sch[h]['finish'], BASE[h]['finish'])
        if d > 0:
            out[h[2:]] = d
    otros = sum(1 for k, r in sch.items() if r.get('late_scheduled'))
    return out, otros

def escenario(driver, crash=False, fast=False):
    nodes = copy.deepcopy(NODES); edges = copy.deepcopy(EDGES)
    N = {n['id']: n for n in nodes}
    d = N[driver]
    extra = 14 if d['calendar'] == 'ALL' else ATRASO
    hh_extra = 0.0
    dur = int(math.ceil(float(d['duration_days']))) + extra
    if crash and d.get('hh', 0) > 0:
        # El doble de personas; esfuerzo +15 % sobre lo comprimido
        dur = max(1, math.ceil(dur * 1.15 / 2))
        hh_extra += 0.15 * d['hh']
    d['duration_days'] = dur
    if fast:
        for e in edges:
            s = N[e['succ']]
            if e['pred'] == driver and e.get('type', 'FS') == 'FS' and s.get('hh', 0) > 0 \
                    and not e['succ'].startswith('A:'):
                e['type'] = 'SS'; e['lag'] = max(1, math.ceil(dur / 2)); e['lag_calendar'] = 'LAB'
                hh_extra += 0.10 * s['hh']
    _, sch = programar(nodes, edges)
    imp, otros = impacto(sch)
    return imp, otros, round(hh_extra, 1)

ESC = {
    'S1 Levantamiento (1.2.2)': '1.2.2:E1:TRABAJO:006',
    'S2 Nube base (1.4.1)': '1.4.1:E1:E1:151',
    'S3 Construcción E1 (1.5.36.1)': next(k for k in BASE if k.startswith('1.5.36.1:') and ':DEV:' in k),
    'S4 Entrega UPS lote 1': 'F:1.4.16:ENT-L1-UPS',
    'S5 Corte de inventario (1.7.3)': next(k for k in BASE if k.startswith('1.7.3:') and ':PREP:' in k and BASE[k]['start'] < '2027-12-31'),
    'S6 Construcción E2 (1.5.22.1)': next(k for k in BASE if k.startswith('1.5.22.1:')),
    'S6b Innovación E2 (1.10.4.6)': next(k for k in BASE if k.startswith('1.10.4.6:')),
    'S7 Capacitación (1.13.3)': next(k for k in BASE if k.startswith('1.13.3:') and ':E2:' in k),
}
res = {}
for nombre, drv in ESC.items():
    r = {'actividad': drv, 'HH': NODES and next(n['hh'] for n in NODES if n['id'] == drv)}
    for etiqueta, kw in [('sin_respuesta', {}), ('intensificacion', {'crash': True}),
                         ('ejecucion_rapida', {'fast': True}), ('ambas', {'crash': True, 'fast': True})]:
        imp, otros, hhx = escenario(drv, **kw)
        r[etiqueta] = dict(hitos=imp, actividades_tardias=otros, HH_extra=hhx)
    res[nombre] = r
    print(nombre, json.dumps({k: v for k, v in r.items() if k != 'actividad'}, ensure_ascii=False))
json.dump(res, open('escenarios_resultado.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
