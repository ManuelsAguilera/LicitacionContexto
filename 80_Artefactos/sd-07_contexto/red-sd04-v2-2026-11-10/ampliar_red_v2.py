"""Red del SD-07 v2: traspaso del SD-04 completo con el método de HH del SD-07.

Método (idéntico al ledger del traspaso):
  HH = cantidad × (O + 4M + P) / 6, con O, M, P en HH por unidad;
  M = personas × días × 8 HH; O = 0,6 M; P = 1,5 M (proporción más usada en el ledger).
  Duración = techo((O_d + 4 M_d + P_d) / 6), con O_d = HH/(n·7,5), M_d = HH/(n·6,8), P_d = HH/(n·5,1).
Parte de la red original del traspaso. Uso: python3 -I ampliar_red_v2.py <Red_CPM origen> <Red_CPM destino>
"""
import sys, json, os, math

ORI, DST = sys.argv[1], sys.argv[2]
rd = lambda n: json.load(open(f'{ORI}/{n}', encoding='utf-8-sig'))
nodes, edges = rd('nodos.json'), rd('relaciones.json')
N = {n['id']: n for n in nodes}
COMP = []  # registro de componentes (para el ledger v2)

def pert_hh(M, O=None, P=None):
    O = 0.6 * M if O is None else O
    P = 1.5 * M if P is None else P
    return (O + 4 * M + P) / 6, O, P

def duracion(hh, n):
    if hh <= 0:
        return 0
    o, m, p = hh / (n * 7.5), hh / (n * 6.8), hh / (n * 5.1)
    return max(1, math.ceil((o + 4 * m + p) / 6))

def nodo(id_, edt, nombre, cal, hh, roles, release='2027-01-07', deadline='2031-09-07', fase='FIS'):
    """roles: {rol: personas}; HH se reparten por personas."""
    n = sum(roles.values())
    role_hh = {r: round(hh * p / n, 2) for r, p in roles.items()}
    nd = dict(id=id_, edt=edt, stage='E1', phase=fase, name=nombre, calendar=cal, release=release,
              deadline_exclusive=deadline, duration_days=duracion(hh, n), hh=round(hh, 2), role_hh=role_hh,
              productive_hh=round(hh, 2), included_coordination_hh=0.0, proposed_people=n, proposed_roles=roles,
              duration_basis='Unidad × PERT(O,M,P); rendimiento 7,5/6,8/5,1 HH efectivas por persona y día')
    nodes.append(nd); N[id_] = nd
    return id_

def hito(id_, nombre):
    nd = dict(id=id_, name=nombre, calendar='LAB', release='2027-01-07', deadline_exclusive='2031-09-07',
              duration_days=0, hh=0, roles=[])
    nodes.append(nd); N[id_] = nd
    return id_

def plazo(id_, edt, nombre, dias):
    nd = dict(id=id_, edt=edt, stage='E1', phase='SUMINISTRO', name=nombre, calendar='ALL', release='2027-01-07',
              deadline_exclusive='2031-09-07', duration_days=dias, hh=0, roles=[],
              duration_basis='Plazo de entrega del proveedor (supuesto validado; confirmar con T-22)')
    nodes.append(nd); N[id_] = nd
    return id_

def fs(a, b, base):
    assert a in N and b in N, (a, b)
    edges.append(dict(pred=a, succ=b, type='FS', lag=0, lag_calendar='LAB', basis=base))

def comp(edt, desc, unidad, q, M, roles_txt, nota, O=None, P=None):
    u, o, p = pert_hh(M, O, P)
    COMP.append(dict(edt=edt, description=desc, unit=unidad, quantity=q, O=round(o, 2), M=M, P=round(p, 2),
                     method='Unidad × PERT(O,M,P)', work_hh=round(q * u, 2), role=roles_txt, note=nota))
    return u  # HH por unidad

def escalar(prefijo, factor, motivo):
    for k, n in N.items():
        if k.startswith(prefijo) and n.get('hh'):
            n['hh'] = round(n['hh'] * factor, 2)
            n['productive_hh'] = round(n.get('productive_hh', n['hh']) * factor, 2)
            n['role_hh'] = {r: round(h * factor, 2) for r, h in (n.get('role_hh') or {}).items()}
            # Igual que el traspaso: «dotación ajustada a ventana disponible, esfuerzo no cambia».
            # La duración se conserva y la dotación crece en la misma proporción.
            if n.get('proposed_roles'):
                n['proposed_roles'] = {r: math.ceil(c * factor) for r, c in n['proposed_roles'].items()}
                n['proposed_people'] = sum(n['proposed_roles'].values())
            n['duration_basis'] = n.get('duration_basis', '') + f' | Escalado ×{factor:.4f} con dotación ajustada: {motivo}'

# ---- 1. Componentes existentes que cambian de cantidad (SD-04: 3 frentes y laboratorio) ----
escalar('1.4.1:', 15 / 10, 'C0168 dominio-ambiente 10→15 (3 frentes × 5 ambientes)')
escalar('1.4.4:', 15 / 10, 'C0171 dominio-ambiente 10→15')
escalar('1.4.13:', 15 / 10, 'C0180 familias × frentes 10→15')
escalar('1.8.4:', 3 / 2, 'C0203 frentes 2→3')
escalar('1.4.8:', 25 / 24, 'C0175 sitios 24→25 (laboratorio)')
# C0170 1.4.3 huellas 2→4: réplica de los nodos de la Filial para el Control de cruces
base3 = {f: next(k for k in N if k.startswith(f'1.4.3:E1:{f}:')) for f in ('PREP', 'PROD', 'CHECK')}
x = {}
for f, k in base3.items():
    nd = dict(N[k], id=f'F:1.4.3:X01:{f}', name=f'Entorno dedicado del Control de cruces · {f}',
              duration_basis='C0170 huellas 2→4: Producción y DR del Control de cruces (SD-04, D-FIS-02)')
    nd.pop('proposed_start', None)
    nodes.append(nd); N[nd['id']] = nd; x[f] = nd['id']
fs(x['PREP'], x['PROD'], 'Preparación antes de intervenir'); fs(x['PROD'], x['CHECK'], 'Comprobación')
for e in [e for e in edges if e['succ'] == base3['PREP'] and not e['pred'].startswith('1.4.3')]:
    edges.append(dict(e, succ=x['PREP']))
for e in [e for e in edges if e['pred'] == base3['CHECK']]:
    edges.append(dict(e, pred=x['CHECK']))
COMP.append(dict(edt='1.4.3', description='Huellas Producción/DR del Control de cruces', unit='huellas',
                 quantity=2, method='Réplica de C0170', work_hh=round(sum(N[v]['hh'] for v in x.values()), 2)))
for k in N:
    if k.startswith('1.4.3:'):
        N[k]['name'] = N[k]['name'].replace('Entorno dedicado del ámbito emisor',
                                            'Entornos dedicados de la Filial y del Control de cruces')
    if k.startswith('1.4.2:'):
        N[k]['name'] = N[k]['name'].replace('(13 tiendas)', '(13 sitios del traspaso)')

# ---- 2. Componentes físicos (paso C con el método del SD-07) ----
LEV = {'Ingeniero infraestructura física': 1, 'Especialista de redes': 1}
OC = {'Ingeniero infraestructura física': 1, 'Arquitecto / diseñador técnico': 1}
FIS = {'Ingeniero infraestructura física': 2, 'Implantador': 1}
RED = {'Especialista de redes': 2, 'Implantador': 1, 'Especialista de seguridad': 1}
PILA = {'SRE / plataforma': 1, 'Implantador': 1}
u_lev = comp('1.4.14', 'Levantamiento físico por sitio', 'sitio', 25, 16, 'Infraestructura física/redes', '2 personas × 1 día')
u_oc = comp('1.4.16/1.4.18', 'Órdenes de compra de equipamiento', 'orden', 3, 16, 'Infraestructura/arquitecto', 'DC-01, lote 1, lote 2')
u_tt = comp('1.4.15/1.4.17/1.4.19', 'Instalación física de la tienda tipo, sin redes', 'sitio', 23, 72, 'Infraestructura física/implantador', '3 personas × 3 días; laboratorio, 3 piloto y 19 tiendas')
u_cd = comp('1.4.19', 'Instalación física de CD', 'sitio', 2, 48, 'Infraestructura física/implantador', '3 personas × 2 días')
u_red = comp('1.4.2', 'Red de sitio en los 12 sitios no incluidos en C0169', 'sitio', 12, 32, 'Redes/implantador/seguridad', 'C0169 13→25; mismo O/M/P por sitio', O=24, P=48)
u_pila = comp('1.4.23', 'Pila local de tienda desplegada y probada', 'sitio', 25, 16, 'SRE/implantador', '2 personas × 1 día')

lev_dc = nodo('F:1.4.14:DC01', '1.4.14', 'Levantamiento físico de DC-01 · FIS', 'LAB', u_lev, LEV)
lev1 = [lev_dc]
for s in ['PIL1', 'PIL2', 'PIL3', 'LAB']:
    k = nodo(f'F:1.4.14:{s}', '1.4.14', f'Levantamiento físico {s} · FIS', 'LAB', u_lev, LEV)
    fs(lev1[-1], k, 'Un equipo de levantamiento, un sitio a la vez'); lev1.append(k)
lev2 = [lev1[-1]]
for i in range(1, 21):
    k = nodo(f'F:1.4.14:S{i:02d}', '1.4.14', f'Levantamiento físico sitio lote 2 #{i} · FIS', 'LAB', u_lev, LEV)
    fs(lev2[-1], k, 'Un equipo de levantamiento, un sitio a la vez'); lev2.append(k)

oc_dc = nodo('F:1.4.16:OC-DC01', '1.4.16', 'Orden de compra DC-01 · FIS', 'LAB', u_oc, OC)
fs(lev_dc, oc_dc, 'Composición fija de DC-01 (decisión aceptada)')
ent_dc = plazo('F:1.4.16:ENT-DC01', '1.4.16', 'Entrega equipamiento DC-01 (12 semanas)', 84)
fs(oc_dc, ent_dc, 'Plazo del proveedor')
for k in ['1.4.11:E1:PROD:343', '1.4.12:E1:PROD:344']:
    fs(ent_dc, k, 'El recinto se habilita con el equipamiento entregado')

oc1 = nodo('F:1.4.16:OC-L1', '1.4.16', 'Orden de compra lote 1 (piloto y laboratorio) · FIS', 'LAB', u_oc, OC)
fs('A:H1', oc1, 'El patrón de la tienda tipo se compra al cerrar H1'); fs(lev1[-1], oc1, 'Lo variable requiere levantamiento')
e1a = plazo('F:1.4.16:ENT-L1-EST', '1.4.16', 'Entrega lote 1, estándar (8 semanas)', 56)
e1b = plazo('F:1.4.16:ENT-L1-UPS', '1.4.16', 'Entrega lote 1, UPS y generación (12 semanas)', 84)
fs(oc1, e1a, 'Plazo del proveedor'); fs(oc1, e1b, 'Plazo del proveedor')

def sitio(s, edt_fis, nombre, cal, deadline, u_fis, cuad, prev, entregas, con_red):
    """Instalación física → red (si corresponde) → pila local, en la misma visita."""
    f = nodo(f'F:{edt_fis}:{s}', edt_fis, f'{nombre} instalado físicamente (cuadrilla {cuad}) · FIS', cal, u_fis, FIS,
             deadline=deadline)
    for e in entregas:
        fs(e, f, 'Requiere el equipamiento entregado')
    if prev:
        fs(prev, f, f'Cuadrilla {cuad}: un sitio a la vez')
    ult = f
    if con_red:
        r = nodo(f'F:1.4.2:RED:{s}', '1.4.2', f'Red de sitio {s} en servicio · FIS', cal, u_red, RED, deadline=deadline)
        fs(f, r, 'La red se configura sobre el equipamiento instalado'); ult = r
    p = nodo(f'F:1.4.23:{s}', '1.4.23', f'Pila local de {s} desplegada y probada · FIS', cal, u_pila, PILA, deadline=deadline)
    fs(ult, p, 'La pila local corre sobre servidores y red en servicio')
    return f, p

fin1 = []
for cuad, sitios in [('A', ['LAB', 'PIL1']), ('B', ['PIL2', 'PIL3'])]:
    prev = None
    for s in sitios:
        edt = '1.4.15' if s == 'LAB' else '1.4.17'
        nom = 'Tienda de laboratorio' if s == 'LAB' else f'Tienda piloto {s[-1]}'
        f, p = sitio(s, edt, nom, 'LAB', '2027-07-07', u_tt, cuad, prev, [e1a, e1b], True)
        prev = f; fin1.append(p)
for p in fin1:
    for k in [k for k in N if k.startswith('1.9.9:')]:
        fs(p, k, 'El corte de 24 h se ensaya con piloto y laboratorio en servicio')

oc2 = nodo('F:1.4.18:OC-L2', '1.4.18', 'Orden de compra lote 2 (19 tiendas y 2 CD) · FIS', 'LAB', u_oc, OC)
fs('A:H2', oc2, 'Compra masiva tras aprobar la arquitectura'); fs(lev2[-1], oc2, 'Lo variable requiere levantamiento')
e2a = plazo('F:1.4.18:ENT-L2-EST', '1.4.18', 'Entrega lote 2, estándar (8 semanas)', 56)
e2b = plazo('F:1.4.18:ENT-L2-UPS', '1.4.18', 'Entrega lote 2, UPS y generación (12 semanas)', 84)
fs(oc2, e2a, 'Plazo del proveedor'); fs(oc2, e2b, 'Plazo del proveedor')
listo = hito('F:1.4.19:LISTO', 'Lote 2 instalado: 22 tiendas y 2 CD en servicio')
sitios2 = [f'T{i:02d}' for i in range(1, 20)] + ['CD01', 'CD02']
con_red2 = {'CD01', 'CD02'} | {f'T{i:02d}' for i in range(14, 20)}  # 12 sitios de C0169: LAB, 3 piloto, 2 CD, T14–T19
for cuad, sitios in {'A': sitios2[0::2], 'B': sitios2[1::2]}.items():
    prev = None
    for s in sitios:
        u = u_cd if s.startswith('CD') else u_tt
        f, p = sitio(s, '1.4.19', f'Sitio {s}', 'PROD', '2027-11-01', u, cuad, prev, [e2a, e2b], s in con_red2)
        prev = f
        fs(p, listo, 'Sitio completo')
fs(listo, 'A:H6', 'La marcha blanca E1 requiere las 22 tiendas y los 2 CD instalados')

# ---- 3. Cambios E1–E7 de la EDT ----
u_e1 = comp('1.4.21', 'Plataforma de datos y analítica por negocio', 'negocio', 2, 160, 'Ingeniero de datos/SRE', '(15 días datos + 5 SRE) × 8')
u_e2 = comp('1.8.9', 'Controles de seguridad desplegados', 'control-frente', 12, 24, 'Especialista de seguridad', 'Defender 3, Sentinel 3, DDoS 1, HSM 2, External ID 2, Intune 1; 3 días')
u_e3 = comp('1.4.22', 'Equipamiento TI y redes de DC-01', 'recinto', 1, 320, 'Infraestructura física/redes', '4 personas × 10 días')
u_e6 = comp('1.4.24', 'Replicación entre regiones', 'frente', 3, 48, 'SRE', 'PostgreSQL, ACR y Front Door privado; 2 SRE × 3 días')
u_dr = comp('1.4.20', 'Recuperación a tamaño completo', 'frente', 3, 16, 'SRE', '1 SRE × 2 días')
u_e7 = comp('1.10.1/1.10.5', 'Órdenes de compra de lockers y tótems', 'orden', 2, 16, 'IoT/arquitecto', '2 personas × 1 día')

amb = [k for k in N if k.startswith('1.4.4:')]
for neg in ('R', 'F'):
    k = nodo(f'F:1.4.21:{neg}', '1.4.21', f'Plataforma de datos y analítica ({"Retail" if neg == "R" else "Filial"}) · FIS',
             'LAB', u_e1, {'Especialista de datos': 3, 'SRE / plataforma': 1}, release='2027-05-07', deadline='2027-11-01')
    for a in amb:
        fs(a, k, 'Requiere los ambientes')
    fs(k, 'A:H6', 'Reportes y analítica disponibles en la marcha blanca E1')
pent = sorted(k for k in N if k.startswith('1.8.6:'))[0]
prev = None
for i in range(1, 13):
    k = nodo(f'F:1.8.9:C{i:02d}', '1.8.9', f'Control de seguridad desplegado #{i} · FIS', 'LAB', u_e2,
             {'Especialista de seguridad': 1}, release='2027-04-07', deadline='2027-10-01')
    for a in amb:
        fs(a, k, 'Requiere los ambientes')
    if prev:
        fs(prev, k, 'Un especialista, un control a la vez')
    prev = k
fs(prev, pent, 'La prueba de intrusión verifica los controles desplegados')
dc = nodo('F:1.4.22:DC01', '1.4.22', 'Equipamiento TI y redes de DC-01 instalados · FIS', 'LAB', u_e3,
          {'Ingeniero infraestructura física': 2, 'Especialista de redes': 2}, deadline='2027-07-07')
fs(ent_dc, dc, 'Requiere el equipamiento entregado')
for k in ['1.4.11:E1:PROD:343', '1.4.12:E1:PROD:344']:
    fs(k, dc, 'Recinto con energía, clima y seguridad física')
fs(dc, 'A:H3', 'H3 entrega la infraestructura híbrida')
rep = []
for fr in ('R', 'F', 'X'):
    k = nodo(f'F:1.4.24:{fr}', '1.4.24', f'Replicación entre regiones del frente {fr} · FIS', 'LAB', u_e6,
             {'SRE / plataforma': 2}, release='2027-07-07', deadline='2027-10-01')
    for a in amb:
        fs(a, k, 'Requiere los ambientes de Producción y DR')
    rep.append(k)
prev = None
for fr, r in zip(('R', 'F', 'X'), rep):
    k = nodo(f'F:1.4.20:{fr}', '1.4.20', f'Recuperación del frente {fr} a tamaño completo · FIS', 'PROD', u_dr,
             {'SRE / plataforma': 1}, release='2027-09-07', deadline='2027-11-01')
    fs(r, k, 'Se escala la región ya replicada'); fs(k, 'A:H6', 'El RTO rige desde la marcha blanca E1')
for edt, diseño, piloto, nom in [('1.10.1', '1.10.1.1', '1.10.1.4', 'lockers'), ('1.10.5', '1.10.5.1', '1.10.5.5', 'tótems')]:
    oc = nodo(f'F:{edt}:OC', edt, f'Orden de compra de {nom} · FIS', 'LAB', u_e7,
              {'Especialista IoT / hardware': 1, 'Arquitecto / diseñador técnico': 1})
    ent = plazo(f'F:{edt}:ENT', edt, f'Entrega de {nom} (8 semanas)', 56)
    for k in [k for k in N if N[k].get('edt') == diseño]:
        fs(k, oc, 'Se compra tras el diseño')
    fs(oc, ent, 'Plazo del proveedor')
    for k in [k for k in N if N[k].get('edt') == piloto and ':PREP:' in k]:
        fs(ent, k, 'El piloto requiere los equipos entregados')

os.makedirs(DST, exist_ok=True)
json.dump(nodes, open(f'{DST}/nodos.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(edges, open(f'{DST}/relaciones.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(COMP, open(f'{DST}/componentes_v2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
orig = {n['id'] for n in rd('nodos.json')}
print(json.dumps(dict(nodos=len(nodes), relaciones=len(edges), nodos_nuevos=len(nodes) - len(orig),
                      HH_total=round(sum(n.get('hh', 0) for n in nodes), 2)), ensure_ascii=False))
