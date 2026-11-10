"""Amplía la red CPM del SD-07 con el suministro e instalación física del SD-04.

Lee nodos.json y relaciones.json originales del traspaso y escribe copias ampliadas.
No modifica duraciones, HH ni relaciones existentes; solo agrega nodos y relaciones,
renombra 1.4.2 y 1.4.3 y corrige plazos de 1.4.11/1.4.12 cuando lo exige el suministro.

Supuestos validados por el usuario (2026-11-10):
  - Plazo de entrega: 8 semanas equipamiento estándar; 12 semanas UPS y generación.
  - Instalación: 1 tienda por cuadrilla cada 3 días hábiles; 2 cuadrillas en paralelo.
  - Patrón de la tienda tipo se compra al cerrar H1; lo variable tras el levantamiento del sitio.
  - Piloto en 3 tiendas a la calle, permitido dentro de la envolvente de eventos (calendario LAB).
  - Recuperación en Brazil South a tamaño completo antes de la marcha blanca E1 (encendida desde M13).
  - Levantamiento físico: 1 día por sitio, 2 personas.
Uso: python3 -I ampliar_red.py <Red_CPM origen> <Red_CPM destino>
"""
import sys, json, os

ORI, DST = sys.argv[1], sys.argv[2]
rd = lambda n: json.load(open(f'{ORI}/{n}', encoding='utf-8-sig'))
nodes, edges = rd('nodos.json'), rd('relaciones.json')
N = {n['id']: n for n in nodes}
HHD = 6.8  # HH efectivas por persona y día (escenario más probable del traspaso)

def nodo(id_, edt, nombre, cal, dur, roles, release='2027-01-07', deadline='2031-09-07', fase='FIS'):
    role_hh = {r: round(p * HHD * dur, 2) for r, p in roles.items()}
    n = dict(id=id_, edt=edt, stage='E1', phase=fase, name=nombre, calendar=cal, release=release,
             deadline_exclusive=deadline, duration_days=dur, hh=round(sum(role_hh.values()), 2),
             role_hh=role_hh, productive_hh=round(sum(role_hh.values()), 2), included_coordination_hh=0.0,
             proposed_people=sum(roles.values()), proposed_roles=roles,
             duration_basis='Ampliación física SD-04 (2026-11-10): supuestos validados por el usuario')
    nodes.append(n); N[id_] = n
    return id_

def hito(id_, nombre, deadline='2031-09-07'):
    n = dict(id=id_, name=nombre, calendar='LAB', release='2027-01-07', deadline_exclusive=deadline,
             duration_days=0, hh=0, roles=[])
    nodes.append(n); N[id_] = n
    return id_

def plazo(id_, edt, nombre, dias):
    n = dict(id=id_, edt=edt, stage='E1', phase='SUMINISTRO', name=nombre, calendar='ALL',
             release='2027-01-07', deadline_exclusive='2031-09-07', duration_days=dias, hh=0, roles=[],
             duration_basis='Plazo de entrega del proveedor (supuesto validado; confirmar con T-22)')
    nodes.append(n); N[id_] = n
    return id_

def fs(a, b, base):
    assert a in N and b in N, (a, b)
    edges.append(dict(pred=a, succ=b, type='FS', lag=0, lag_calendar='LAB', basis=base))

LEV = {'Ingeniero infraestructura física': 1, 'Especialista de redes': 1}
CUAD = {'Ingeniero infraestructura física': 2, 'Especialista de redes': 1, 'Implantador': 1}
OC = {'Ingeniero infraestructura física': 1, 'Arquitecto / diseñador técnico': 1}

# 1.4.14 Levantamiento físico por sitio
lev_dc = nodo('F:1.4.14:DC01', '1.4.14', 'Levantamiento físico de DC-01 · FIS', 'LAB', 1, LEV)
lev1 = [lev_dc]
for s in ['PIL1', 'PIL2', 'PIL3', 'LAB']:
    k = nodo(f'F:1.4.14:{s}', '1.4.14', f'Levantamiento físico {s} · FIS', 'LAB', 1, LEV)
    fs(lev1[-1], k, 'Un equipo de levantamiento, un sitio por día'); lev1.append(k)
lev2 = [lev1[-1]]
for i in range(1, 22):
    k = nodo(f'F:1.4.14:S{i:02d}', '1.4.14', f'Levantamiento físico sitio lote 2 #{i} · FIS', 'LAB', 1, LEV)
    fs(lev2[-1], k, 'Un equipo de levantamiento, un sitio por día'); lev2.append(k)

# DC-01: compra anticipada tras su levantamiento (composición fija en SD-04 §4.3)
oc_dc = nodo('F:1.4.16:OC-DC01', '1.4.16', 'Orden de compra DC-01 · FIS', 'LAB', 1, OC)
fs(lev_dc, oc_dc, 'Composición fija de DC-01; se compra tras su levantamiento')
ent_dc = plazo('F:1.4.16:ENT-DC01', '1.4.16', 'Entrega equipamiento DC-01 (12 semanas)', 84)
fs(oc_dc, ent_dc, 'Plazo del proveedor')
for k in ['1.4.11:E1:PROD:343', '1.4.12:E1:PROD:344']:
    fs(ent_dc, k, 'El recinto se habilita con el equipamiento entregado')

# 1.4.16 Lote 1: patrón tras H1; variable tras levantamiento del sitio
oc1 = nodo('F:1.4.16:OC-L1', '1.4.16', 'Orden de compra lote 1 (piloto y laboratorio) · FIS', 'LAB', 1, OC)
fs('A:H1', oc1, 'El patrón de la tienda tipo se compra al cerrar H1')
fs(lev1[-1], oc1, 'Lo variable por sitio requiere su levantamiento')
e1a = plazo('F:1.4.16:ENT-L1-EST', '1.4.16', 'Entrega lote 1, equipamiento estándar (8 semanas)', 56)
e1b = plazo('F:1.4.16:ENT-L1-UPS', '1.4.16', 'Entrega lote 1, UPS y generación (12 semanas)', 84)
fs(oc1, e1a, 'Plazo del proveedor'); fs(oc1, e1b, 'Plazo del proveedor')

# 1.4.15 laboratorio y 1.4.17 piloto: 2 cuadrillas (A: LAB, PIL1; B: PIL2, PIL3)
inst1 = {}
for cuad, sitios in [('A', ['LAB', 'PIL1']), ('B', ['PIL2', 'PIL3'])]:
    prev = None
    for s in sitios:
        edt = '1.4.15' if s == 'LAB' else '1.4.17'
        nombre = ('Tienda de laboratorio instalada en Preproducción' if s == 'LAB'
                  else f'Tienda piloto {s[-1]} instalada y en servicio') + f' (cuadrilla {cuad}) · FIS'
        k = nodo(f'F:{edt}:{s}', edt, nombre, 'LAB', 3, CUAD, deadline='2027-07-07')
        fs(e1a, k, 'Requiere el equipamiento estándar'); fs(e1b, k, 'Requiere UPS y generación')
        if prev: fs(prev, k, f'Cuadrilla {cuad}: un sitio a la vez')
        prev = k; inst1[s] = k
piloto = [k for k in N if k.startswith('1.9.9:')]
for s, k in inst1.items():
    for p in piloto:
        fs(k, p, 'El corte de 24 h se ensaya en tiendas piloto instaladas y contra el laboratorio')

# 1.4.18 Lote 2 y 1.4.19 instalación: 19 tiendas + 2 CD, calendario PROD
oc2 = nodo('F:1.4.18:OC-L2', '1.4.18', 'Orden de compra lote 2 (19 tiendas y 2 CD) · FIS', 'LAB', 1, OC)
fs('A:H2', oc2, 'Compra masiva después de aprobar la arquitectura')
fs(lev2[-1], oc2, 'Lo variable por sitio requiere su levantamiento')
e2a = plazo('F:1.4.18:ENT-L2-EST', '1.4.18', 'Entrega lote 2, equipamiento estándar (8 semanas)', 56)
e2b = plazo('F:1.4.18:ENT-L2-UPS', '1.4.18', 'Entrega lote 2, UPS y generación (12 semanas)', 84)
fs(oc2, e2a, 'Plazo del proveedor'); fs(oc2, e2b, 'Plazo del proveedor')
listo = hito('F:1.4.19:LISTO', 'Lote 2 instalado: 22 tiendas y 2 CD en servicio')
sitios2 = [f'T{i:02d}' for i in range(1, 20)] + ['CD01', 'CD02']
cuadrillas = {'A': sitios2[0::2], 'B': sitios2[1::2]}
for cuad, sitios in cuadrillas.items():
    prev = None
    for s in sitios:
        dur = 2 if s.startswith('CD') else 3
        k = nodo(f'F:1.4.19:{s}', '1.4.19', f'Sitio {s} instalado y en servicio (cuadrilla {cuad}) · FIS',
                 'PROD', dur, CUAD, deadline='2027-11-01')
        fs(e2a, k, 'Requiere el equipamiento estándar'); fs(e2b, k, 'Requiere UPS y generación')
        if prev: fs(prev, k, f'Cuadrilla {cuad}: un sitio a la vez')
        prev = k
    fs(prev, listo, 'Último sitio de la cuadrilla')
fs(listo, 'A:H6', 'La marcha blanca E1 requiere las 22 tiendas y los 2 CD instalados')

# 1.4.3 ampliado: entorno del Control de cruces (mismas HH y fases que el de la Filial)
base3 = {f: next(k for k in N if k.startswith(f'1.4.3:E1:{f}:')) for f in ('PREP', 'PROD', 'CHECK')}
x = {}
for f, k in base3.items():
    o = N[k]
    roles = o.get('role_hh') or {}
    n = dict(o, id=f'F:1.4.3:X01:{f}', name=f'Entorno dedicado del Control de cruces · {f}',
             duration_basis='Réplica del entorno de la Filial para X-01 (SD-04, D-FIS-02)')
    n.pop('proposed_start', None)
    nodes.append(n); N[n['id']] = n; x[f] = n['id']
fs(x['PREP'], x['PROD'], 'Preparación antes de intervenir'); fs(x['PROD'], x['CHECK'], 'Comprobación')
for e in [e for e in edges if e['succ'] == base3['PREP'] and not e['pred'].startswith('1.4.3')]:
    edges.append(dict(e, succ=x['PREP']))
for e in [e for e in edges if e['pred'] == base3['CHECK']]:
    edges.append(dict(e, pred=x['CHECK']))
for k in N:
    if k.startswith('1.4.3:'):
        N[k]['name'] = N[k]['name'].replace('Entorno dedicado del ámbito emisor',
                                            'Entornos dedicados de la Filial y del Control de cruces')
    if k.startswith('1.4.2:'):
        N[k]['name'] = N[k]['name'].replace('(13 tiendas)', '(patrón y configuración de borde)')

# 1.4.20 Recuperación en Brazil South a tamaño completo antes de la marcha blanca E1
dr = nodo('F:1.4.20:DR', '1.4.20', 'Recuperación en Brazil South a tamaño completo · FIS', 'PROD', 5,
          {'SRE / plataforma': 2}, release='2027-09-07', deadline='2027-11-01')
for k in [k for k in N if k.startswith('1.4.4:')]:
    fs(k, dr, 'La recuperación se escala sobre los ambientes creados')
fs(dr, 'A:H6', 'El RTO de 4 h rige desde la operación con datos reales (marcha blanca E1)')

os.makedirs(DST, exist_ok=True)
json.dump(nodes, open(f'{DST}/nodos.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(edges, open(f'{DST}/relaciones.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
nuevos = [n for n in nodes if n['id'].startswith('F:')]
print(json.dumps(dict(nodos=len(nodes), relaciones=len(edges), nodos_nuevos=len(nuevos),
                      HH_nuevas=round(sum(n['hh'] for n in nuevos), 2)), ensure_ascii=False))
