"""Genera el cuerpo del Formulario T-15 con la red v3 a partir del .tex del traspaso (234.493,47 HH).

Uso: python3 -I gen_t15.py <dir traspaso> <repo> <salida.tex>
- Preámbulo: el del T-15 del repositorio (plantilla vigente). Cuerpo: el del traspaso, con las tablas recalculadas.
- Las HH por mes se obtienen con el método delta: datos del traspaso, menos las actividades que cambiaron
  (registro diario real) y más su reparto uniforme en la ventana v3. Las coberturas no cambian.
"""
import sys, re, csv, json, collections
from bisect import bisect_left
from decimal import Decimal as D

T, REPO, OUT = sys.argv[1:4]
V = REPO + '/80_Artefactos/sd-07_contexto/red-v3-2026-11-10'
sys.path.insert(0, T + '/Red_CPM/verificacion')
from motor_cpm_verificado_20261105 import Network

rd = lambda p: json.load(open(p, encoding='utf-8-sig'))
cals = rd(T + '/Red_CPM/calendarios.json')
MESES = [(int(m['mes']), m['inicio']) for m in csv.DictReader(open(T + '/Datos_base/dotacion_y_reservas_56_meses.csv', encoding='utf-8-sig'))]
INI = [m[1] for m in MESES]
mes = lambda ds: MESES[bisect_left(INI, ds + 'z') - 1][0]
num = lambda s: D(str(s).replace(',', '.') or '0')
def f2(x):
    return f'{D(x):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
def f1(x):
    return f'{D(x):,.1f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
ddmmyyyy = lambda s: '-'.join(reversed(s.split('-')))

# ---------------- datos v3 ----------------
orig = {r['id']: r for r in rd(T + '/Red_CPM/programacion.json')}
v3 = {r['id']: r for r in csv.DictReader(open(V + '/programacion_v3.csv', encoding='utf-8-sig'), delimiter=';')}
cambiadas = {k for k, r in v3.items() if num(r['HH']) > 0 and (k not in orig or r['inicio'] != orig[k]['start']
             or abs(num(r['HH']) - D(str(orig[k]['hh']))) > D('0.005'))}
edt_of = lambda k: (v3[k]['edt'] if k in v3 else '') or (orig[k].get('edt', '') if k in orig else '') or k.split(':')[0]
stage_of = lambda k: (v3[k]['etapa'] if k in v3 and v3[k]['etapa'] else orig.get(k, {}).get('stage', ''))
COL = {'E1': 'Etapa1', 'MB1': 'Etapa1', 'E1-PROD': 'Etapa1', 'E2': 'Etapa2', 'MB2': 'Etapa2', 'OP': 'Cierre_operacion'}
FRENTE = {'1.1': 1, '1.2': 2, '1.3': 2, '1.4': 3, '1.5': 4, '1.6': 5, '1.7': 5, '1.8': 6, '1.9': 7, '1.10': 8,
          '1.11': 9, '1.12': 9, '1.13': 9, '1.14': 10, '1.15': 11}
rama = lambda e: '.'.join(e.split('.')[:2])

def delta(keyfn):
    """Delta (clave, mes) -> HH entre el traspaso y la v3 para las actividades que cambiaron."""
    q = collections.defaultdict(D)
    for r in csv.DictReader(open(T + '/Red_CPM/personas_trabajo_y_reservas.csv', encoding='utf-8-sig')):
        a = r['actividad']
        if a in cambiadas and a in orig:
            q[(keyfn(a, 'old'), mes(r['fecha']))] -= D(r['HH_trabajo'])
    for k in cambiadas:
        r = v3[k]; ds = cals[r['calendario']]
        dias = ds[bisect_left(ds, r['inicio']):bisect_left(ds, r['fin_exclusivo'])]
        for d in dias:
            q[(keyfn(k, 'new'), mes(d))] += num(r['HH']) / len(dias)
    return q

# columnas por mes (etapa)
base = {int(r['mes']): {k: D(r[k]) for k in ('Etapa1', 'Etapa2', 'Transversal', 'Cierre_operacion', 'Soporte_operacion')}
        for r in csv.DictReader(open(T + '/Datos_base/HH_por_mes_56_meses.csv', encoding='utf-8-sig'))}
for (c, m), v in delta(lambda k, _: COL[(orig[k]['stage'] if _ == 'old' else stage_of(k))]).items():
    base[m][c] += v
# ajuste de céntimos del traspaso v2 (239.250,01 = 234.493,47 + 4.756,54): se carga en Etapa 1, M9
ajuste = D('239250.01') - sum(sum(v.values()) for v in base.values())
base[9]['Etapa1'] += ajuste
tot_mes = {m: sum(base[m].values()) for m in base}
assert abs(sum(tot_mes.values()) - D('239250.01')) < D('0.005')

# trabajo técnico por frente y mes (para los solapamientos)
fr = collections.defaultdict(D)
for r in csv.DictReader(open(T + '/Red_CPM/personas_trabajo_y_reservas.csv', encoding='utf-8-sig')):
    m = mes(r['fecha'])
    if m in (13, 14, 15, 19, 20):
        fr[(FRENTE.get(rama(r['actividad'].split(':')[0]), 0), m)] += D(r['HH_trabajo'])
for (f, m), v in delta(lambda k, _: FRENTE.get(rama(edt_of(k)), 0)).items():
    if m in (13, 14, 15, 19, 20):
        fr[(f, m)] += v

# campo y viajes con horario fijo (trabajo técnico del frente 9, sin cambio en la v3)
for r in csv.DictReader(open(T + '/Red_CPM/personas_campo_y_viajes.csv', encoding='utf-8-sig')):
    m = mes(r['fecha'])
    if r['tipo'].startswith('Campo/viaje') and m in (13, 14, 15, 19, 20):
        fr[(9, m)] += D(r['HH_trabajo'])

# coberturas (sin cambio)
cob = collections.defaultdict(D)       # (componente, mes)
cob_rol = collections.defaultdict(D)   # (rol, mes) de coberturas no técnicas
for r in csv.DictReader(open(T + '/HH_detalle_mes_rol_componente.csv', encoding='utf-8-sig'), delimiter=';'):
    if r['Componente'] == 'Trabajo técnico y viajes':
        continue
    v = D(r['HH'].replace('.', '').replace(',', '.')); m = int(r['Mes'][1:])
    cob[(r['Componente'], m)] += v
    if r['Componente'] != 'Cobertura de campo':
        cob_rol[(r['Rol'], m)] += v

hh_rol = {r['Rol']: [num(r[f'M{m}']) for m in range(1, 57)] for r in
          csv.DictReader(open(V + '/HH_matriz_roles_M1_M56.csv', encoding='utf-8-sig'), delimiter=';')}
trab_mes = {m: sum(v[m - 1] for v in hh_rol.values()) - sum(cob[(c, m)] for c in
            ('Cobertura de campo', 'Dirección y PMO', 'Inducción de operación', 'Operación')) for m in range(1, 57)}

# CPM v3
net = Network(rd(V + '/Red_CPM/nodos.json'), rd(V + '/Red_CPM/relaciones.json'), cals)
cpm = {r['id']: r for r in net.calculate()}

# ---------------- utilidades de edición ----------------
L = open(T + '/Fuentes_LaTeX/Formularios/OnlySimpleSolutions-Formulario-T-15.tex', encoding='utf-8').read()
pre = open(REPO + '/02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-15.tex', encoding='utf-8').read()
s = pre[:pre.index('\\begin{document}')] + L[L.index('\\begin{document}'):]

def rep(old, new, n=1):
    global s
    c = s.count(old)
    if c != n:
        raise SystemExit(f'{c} apariciones (esperaba {n}): {old[:90]}')
    s = s.replace(old, new)

def filas_tabla(label, filas):
    """Reemplaza las filas entre \\endlastfoot y \\end{longtable} de la tabla con ese label."""
    global s
    i = s.index('\\label{' + label + '}')
    a = s.index('\\endlastfoot\n', i) + len('\\endlastfoot\n')
    b = s.index('\\end{longtable}', a)
    s = s[:a] + '\n'.join(filas) + '\n' + s[b:]

def filas_de(label):
    i = s.index('\\label{' + label + '}')
    a = s.index('\\endlastfoot\n', i) + len('\\endlastfoot\n')
    b = s.index('\\end{longtable}', a)
    return [l for l in s[a:b].split('\n') if l.strip()]

# ---------------- 1. Cifras globales ----------------
rep('La base asciende a \\textbf{234.493,47 HH}', 'La base asciende a \\textbf{239.250,01 HH}')
rep('El total con contingencia es de \\textbf{238.181,47 HH}.', 'El total con contingencia es de \\textbf{242.938,01 HH}.')
rep('No forma parte de las 234.493,47 HH base', 'No forma parte de las 239.250,01 HH base')
rep('La red de cálculo reúne 853 actividades, hitos y controles de calendario con 1.836 relaciones.',
    'La red de cálculo reúne 978 actividades, hitos y controles de calendario con 2.127 relaciones.')
rep('Su suma concilia 234.493,47 HH.', 'Su suma concilia 239.250,01 HH.')

# ---------------- 2. Componentes físicos del SD-04 ----------------
comp = rd(V + '/../red-sd04-v2-2026-11-10/Red_CPM/componentes_v2.json')
filas = []
for c in comp:
    omp = f"{f2(c['O'])} / {f2(c['M'])} / {f2(c['P'])}" if 'M' in c else c.get('method', '')
    filas.append(f"{c['edt']} & {c['description']} & {c['quantity']} {c['unit']} & {omp} & {f2(c['work_hh'])} \\\\")
tabla_comp = '\n'.join([
    '\\begingroup', '\\small',
    '\\begin{longtable}{@{}p{0.13\\linewidth}p{0.33\\linewidth}p{0.14\\linewidth}p{0.22\\linewidth}p{0.11\\linewidth}@{}}',
    '\\caption[Componentes físicos incorporados desde el Subdocumento 4]{Componentes físicos incorporados desde el Subdocumento 4. Fuente: Elaboración propia.}\\label{tab:t15-sd04}\\\\',
    '\\toprule', '\\textbf{EDT} & \\textbf{Trabajo estimado} & \\textbf{Cantidad} & \\textbf{O / M / P (HH por unidad)} & \\textbf{HH} \\\\',
    '\\midrule', '\\endhead', '\\bottomrule', '\\endlastfoot'] + filas + ['\\end{longtable}', '\\endgroup'])
nuevo_sub = ('\\subsubsection{Componentes físicos incorporados desde el Subdocumento 4}\n\n'
    'La arquitectura física del Subdocumento 4 agrega trabajo que la base anterior no contenía. Comprende el levantamiento y la instalación de los 25 sitios (22 tiendas, 2 centros de distribución y la tienda de laboratorio), las órdenes de compra, el centro de datos DC-01, la pila local de tienda, la replicación entre regiones y los controles de seguridad desplegados. '
    'Se estimó con el mismo método que el resto del trabajo ajeno a UCP. Cada componente multiplica su cantidad por las HH por unidad de tres valores, con $M$ igual a personas por días por ocho horas, $O=0{,}6M$ y $P=1{,}5M$. '
    'Cuando un componente existente aumentó su cantidad, como la red de sitio de 13 a 25 sitios, se mantuvo la duración y se ajustó la dotación a la ventana. La Tabla~\\ref{tab:t15-sd04} resume los componentes.\n\n'
    + tabla_comp + '\n\n'
    'Estos componentes agregan 4.756,54 HH de trabajo técnico. Los paquetes nuevos son 1.4.14 a 1.4.24 y 1.8.9; los paquetes 1.4.1 a 1.4.4, 1.4.8, 1.4.13 y 1.8.4 aumentan su esfuerzo, y las cuentas 1.10.1 y 1.10.5 incorporan las órdenes de compra de lockers y tótems. Las duraciones se calcularon con los mismos rendimientos de 7,5, 6,8 y 5,1 HH por persona y jornada.\n\n')
rep('\\subsection{Conciliación del presupuesto}', nuevo_sub + '\\subsection{Conciliación del presupuesto}')

# ---------------- 3. Conciliación ----------------
filas_tabla('tab:t15-3', [
    'Trabajo técnico y desplazamientos & 72.690,01 \\\\', 'Cobertura presencial de campo & 10.560,00 \\\\',
    'Dirección y PMO & 5.824,00 \\\\', 'Equipo de operación M21--M56 & 149.760,00 \\\\',
    'Inducción del equipo de operación & 416,00 \\\\', 'Base programada & 239.250,01 \\\\',
    'Contingencia separada & 3.688,00 \\\\', 'Total con contingencia & 242.938,01 \\\\'])
pkg_old = collections.defaultdict(D)
for x in orig.values():
    pkg_old[x.get('edt') or x['id'].split(':')[0]] += D(str(x.get('hh', 0)))
pkg_new = collections.defaultdict(D)
for k, r in v3.items():
    pkg_new[r['edt'] or k.split(':')[0]] += num(r['HH'])
delta_rama = collections.defaultdict(D)
for e in set(pkg_old) | set(pkg_new):
    if '.' in e and abs(pkg_new[e] - pkg_old[e]) > D('0.005'):
        delta_rama[rama(e)] += pkg_new[e] - pkg_old[e]
delta_rama['1.4'] += D('0.01')  # ajuste de céntimos: 4.756,54 del traspaso v2
print('delta por rama', {k: str(v) for k, v in delta_rama.items()})
nuevas = []
tt = tc = tb = D(0)
for l in filas_de('tab:t15-4'):
    c = [x.strip().rstrip('\\').strip() for x in l.split('&')]
    if c[0] == 'Total':
        continue
    t_, cap = num(c[1].replace('.', '')), num(c[2].replace('.', ''))
    t_ += delta_rama.get(c[0], 0)
    nuevas.append(f'{c[0]} & {f2(t_)} & {f2(cap)} & {f2(t_ + cap)} \\\\')
    tt += t_; tc += cap
nuevas.append(f'Total & {f2(tt)} & {f2(tc)} & {f2(tt + tc)} \\\\')
assert f2(tt + tc) == '239.250,01', f2(tt + tc)
filas_tabla('tab:t15-4', nuevas)

E = {'d1': sum(base[m]['Etapa1'] for m in range(1, 13)), 'mb1': sum(base[m]['Etapa1'] for m in range(13, 16)),
     'd2': sum(base[m]['Etapa2'] for m in range(13, 19)), 'mb2': sum(base[m]['Etapa2'] for m in range(19, 21)),
     'pe1': sum(base[m]['Etapa1'] for m in range(16, 21)), 'c2': D('117.33'), 'op': D('150848.00'),
     'tr': sum(base[m]['Transversal'] for m in range(1, 57))}
assert sum(base[m]['Etapa2'] for m in list(range(1, 13)) + list(range(21, 57))) == 0
sub5 = E['d1'] + E['mb1'] + E['d2'] + E['mb2'] + E['op']
filas_tabla('tab:t15-5', [
    f"Desarrollo E1 & M1–M12 & {f2(E['d1'])} \\\\", f"Marcha blanca E1 & M13–M15 & {f2(E['mb1'])} \\\\",
    f"Desarrollo E2 & M13–M18 & {f2(E['d2'])} \\\\", f"Marcha blanca E2 & M19–M20 & {f2(E['mb2'])} \\\\",
    f"Operación & M21–M56 & {f2(E['op'])} \\\\", f'Subtotal cinco etapas &  & {f2(sub5)} \\\\',
    f"Producción y estabilización E1 & M16–M20 & {f2(E['pe1'])} \\\\", 'Cierre de implementación E2 & M21–M22 & 117,33 \\\\',
    f"Gestión y documentación transversales & M1–M56 & {f2(E['tr'])} \\\\", 'Total sin duplicaciones & M1--M56 & 239.250,01 \\\\'])
assert f2(sub5 + E['pe1'] + E['c2'] + E['tr']) == '239.250,01'

# ---------------- 4. Tablas de HH por paquete ----------------
meses_v3 = json.load(open(sys.argv[4])) if len(sys.argv) > 4 else {}
meses_old = json.load(open(sys.argv[5])) if len(sys.argv) > 5 else {}
pkg = {r['Paquete EDT']: num(r['HH']) for r in csv.DictReader(open(V + '/HH_por_paquete_EDT.csv', encoding='utf-8-sig'), delimiter=';')}
ESCALA = {'1.4.1', '1.4.2', '1.4.3', '1.4.4', '1.4.8', '1.4.13', '1.8.4'}
NUEVOS_14 = [f'1.4.{i}' for i in range(14, 25)]
def omp_de(e):
    m = e / (D('0.6') + 4 + D('1.5')) * 6
    return D('0.6') * m, m, D('1.5') * m
def fila_omp(code, meses, o, m, p, e):
    return f'{code} & {meses} & {f2(o)} & {f2(m)} & {f2(p)} & {f2(e)} \\\\'
def actualizar_rama(label, extra=()):
    out = []; sub = D(0)
    for l in filas_de(label):
        mm = re.match(r'^(1\.[\d.]+) & ([^&]*) & (.*) \\\\$', l)
        if not mm:
            if l.startswith('Subtotal'):
                continue
            out.append(l); continue
        code, meses, rest = mm.groups(); cells = [x.strip() for x in rest.split('&')]
        if code in meses_old and meses_old[code] == meses and code in meses_v3:
            meses = meses_v3[code]
        if code in ESCALA and len(cells) == 4:
            o, m_, p, e = [num(x.replace('.', '')) for x in cells]
            k = (pkg[code] / e).quantize(D('0.0001'))
            o, m_, p, e = o * k, m_ * k, p * k, pkg[code]
            out.append(fila_omp(code, meses, o, m_, p, e)); sub += e; continue
        out.append(f'{code} & {meses} & {rest} \\\\'); sub += num(cells[-1].replace('.', ''))
    for code in extra:
        e = pkg[code]; o, m_, p = omp_de(e)
        out.append(fila_omp(code, meses_v3.get(code, ''), o, m_, p, e)); sub += e
    return out, sub
for i in range(1, 16):
    label = f'tab:t15-tareas-{i}'
    if label not in s or i == 5:
        continue
    extra = NUEVOS_14 if i == 4 else (['1.8.9'] if i == 8 else (['1.10.1', '1.10.5'] if i == 10 else []))
    rows, sub = actualizar_rama(label, extra)
    old_sub = [l for l in filas_de(label) if l.startswith('Subtotal')]
    if old_sub:
        rows.append(f'Subtotal 1.{i} &  &  &  &  & {f2(sub)} \\\\')
    filas_tabla(label, rows)
# meses de la tabla UCP (sin cambio de HH)
rows = []
for l in filas_de('tab:t15-tareas-5'):
    mm = re.match(r'^(1\.5[\d.]+) & ([^&]*) & (.*)$', l)
    if mm and mm.group(1) in meses_old and meses_old[mm.group(1)] == mm.group(2) and mm.group(1) in meses_v3:
        l = f'{mm.group(1)} & {meses_v3[mm.group(1)]} & {mm.group(3)}'
    rows.append(l)
filas_tabla('tab:t15-tareas-5', rows)

# ---------------- 5. Curva y tablas mensuales ----------------
rep('\\includegraphics[width=\\linewidth]{t15-figuras/curva_HH_actualizada.png}',
    '\\includegraphics[width=\\linewidth]{figuras/sd07-figuras/diag-07-05_curva-hh-mensual.pdf}')
pico = max(range(1, 21), key=lambda m: tot_mes[m]); pico_op = max(range(21, 57), key=lambda m: tot_mes[m])
rep('La implementación alcanza su máximo en M16, con 14.944,36 HH,', f'La implementación alcanza su máximo en M{pico}, con {f2(tot_mes[pico])} HH,')
rep('hasta 4.607,11 HH en M22', f'hasta {f2(tot_mes[pico_op])} HH en M{pico_op}')
filas = []
for m in range(1, 21):
    b = base[m]; otros = b['Cierre_operacion'] + b['Soporte_operacion']
    filas.append(f"{m} & {f2(b['Etapa1'])} & {f2(b['Etapa2'] + otros)} & {f2(b['Transversal'])} & {f2(tot_mes[m])} \\\\")
filas.append(f"Total & {f2(sum(base[m]['Etapa1'] for m in range(1,21)))} & {f2(sum(base[m]['Etapa2']+base[m]['Cierre_operacion']+base[m]['Soporte_operacion'] for m in range(1,21)))} & {f2(sum(base[m]['Transversal'] for m in range(1,21)))} & {f2(sum(tot_mes[m] for m in range(1,21)))} \\\\")
old6 = filas_de('tab:t15-6')
if not any(l.startswith('Total') for l in old6):
    filas = filas[:-1]
filas_tabla('tab:t15-6', filas)
filas = []
for m in range(21, 57):
    b = base[m]
    filas.append(f"{m} & {f2(b['Soporte_operacion'])} & {f2(b['Cierre_operacion'] + b['Etapa1'] + b['Etapa2'])} & {f2(b['Transversal'])} & {f2(tot_mes[m])} \\\\")
old7 = filas_de('tab:t15-7')
if any(l.startswith('Total') for l in old7):
    filas.append(f"Total & {f2(sum(base[m]['Soporte_operacion'] for m in range(21,57)))} & {f2(sum(base[m]['Cierre_operacion']+base[m]['Etapa1']+base[m]['Etapa2'] for m in range(21,57)))} & {f2(sum(base[m]['Transversal'] for m in range(21,57)))} & {f2(sum(tot_mes[m] for m in range(21,57)))} \\\\")
filas_tabla('tab:t15-7', filas)

# ---------------- 6. Dotación en personas equivalentes ----------------
fte = lambda h: f1(D(h) / 160)
picos = {'d1': max(base[m]['Etapa1'] for m in range(1, 13)), 'mb1': max(base[m]['Etapa1'] for m in range(13, 16)),
         'd2': max(base[m]['Etapa2'] for m in range(13, 19)), 'mb2': max(base[m]['Etapa2'] for m in range(19, 21)),
         'op': max(base[m]['Soporte_operacion'] + base[m]['Cierre_operacion'] for m in range(21, 57))}
rows = []
claves = ['d1', 'mb1', 'd2', 'mb2', 'op']
for l, k in zip(filas_de('tab:t15-resumen-obligatorio'), claves):
    c = l.split(' & ')
    c[1] = f2(E[k]); c[2] = fte(picos[k])
    rows.append(' & '.join(c))
filas_tabla('tab:t15-resumen-obligatorio', rows)
rep('\\textbf{N.º de personas (peak)}', '\\textbf{Personas equivalentes (pico mensual)}')
rep('Las cinco filas suman 216.301,47 HH.', f'Las cinco filas suman {f2(sub5)} HH.')
rep('elevan la base a 234.493,47', 'elevan la base a 239.250,01')
rows = []
for m in range(1, 57):
    pc = trab_mes[m] + cob[('Cobertura de campo', m)]
    di = cob[('Dirección y PMO', m)]
    op = cob[('Operación', m)] + cob[('Inducción de operación', m)]
    rows.append(f'{m} & {fte(pc)} & {fte(di)} & {fte(op)} & {fte(pc + di + op)} \\\\')
filas_tabla('tab:t15-8', rows)
rep('\\caption[Personas con participación durante cada mes]{Personas con participación durante cada mes. Fuente: Elaboración propia.}',
    '\\caption[Personas equivalentes por mes]{Personas equivalentes por mes (HH del mes divididas por 160). Fuente: Elaboración propia.}')
rep('\\textbf{Total de personas}', '\\textbf{Total}')
def perfiles(meses_):
    out = []
    for rol in sorted(hh_rol):
        vals = [hh_rol[rol][m - 1] - cob_rol[(rol, m)] for m in meses_]
        if max(vals) < D('8'):
            continue
        out.append(rol + ' & ' + ' & '.join(fte(v) for v in vals) + ' \\\\')
    tot = [sum(hh_rol[r][m - 1] - cob_rol[(r, m)] for r in hh_rol) for m in meses_]
    out.append('Total & ' + ' & '.join(fte(v) for v in tot) + ' \\\\')
    return out
filas_tabla('tab:t15-9', perfiles([13, 14, 15]))
filas_tabla('tab:t15-10', perfiles([16, 19, 20]))
NOMBRE_FR = {1: 'Dirección y gobierno', 2: 'Levantamiento, alcance y arquitectura', 3: 'Infraestructura híbrida', 4: 'Software',
             5: 'Integraciones y datos', 6: 'Seguridad y cumplimiento', 7: 'Calidad y certificación', 8: 'Innovaciones',
             9: 'Implantación, marchas blancas y cambio', 10: 'Documentación y reversibilidad', 11: 'Operación y soporte'}
def frentes(meses_):
    out = []
    for m in meses_:
        for f in range(1, 12):
            h = fr[(f, m)]
            c = {1: cob[('Dirección y PMO', m)], 9: cob[('Cobertura de campo', m)], 11: cob[('Inducción de operación', m)] + cob[('Operación', m)]}.get(f, D(0))
            if h < D('0.5') and c == 0:
                continue
            out.append(f'M{m} & {f} · {NOMBRE_FR[f]} & {fte(h + c)} & {f2(h)} \\\\')
    return out
filas_tabla('tab:t15-frentes-13', frentes([13, 14, 15]))
filas_tabla('tab:t15-frentes-19', frentes([19, 20]))
s = s.replace('\\textbf{Personas del mes}', '\\textbf{Personas equivalentes}')

rep_par = [
 ('El peak se define como el máximo de personas distintas asignadas durante una misma jornada de la etapa',
  'La dotación se expresa en personas equivalentes, es decir, HH del mes divididas por 160 HH nominales. El pico de cada etapa es el mes de mayor carga de esa etapa, sin la dirección del proyecto, que se presenta aparte. Una persona equivalente no es una persona distinta; varias personas con dedicación parcial suman una persona equivalente. Esta medida reemplaza al recuento de personas distintas por jornada de la versión anterior, que incluía turnos, desplazamientos y retén'),
 ('Las cifras mensuales siguientes cuentan personas distintas con alguna asignación, viaje o disponibilidad en el mes.',
  'Las cifras mensuales siguientes expresan en personas equivalentes las HH de cada mes. El retén no se incluye porque su disponibilidad no se registra como HH trabajadas.'),
 ('Muestran personas distintas con participación durante el mes y HH de trabajo técnico asignado;',
  'Muestran personas equivalentes y HH de trabajo técnico asignado; las personas equivalentes incluyen la cobertura de dirección, campo u operación del frente;'),
]
for a, b in rep_par:
    i = s.index(a); j = s.index('\n', i)
    par = s[i:j]
    # reemplaza la primera oración o fragmento y conserva el resto del párrafo cuando aplica
    if a.endswith('.') or a.endswith(';'):
        s = s[:i] + b + s[i + len(a):]
    else:
        k = s.index('.', i + len(a))
        s = s[:i] + b + s[k:]

# frases que dependían del recuento de personas distintas
for a, b in [
    (' No representa presencia simultánea en un mismo instante ni dedicación completa mensual. La marcha blanca E1 alcanza su máximo al movilizar los equipos para la entrada oficial de abril.',
     ' La marcha blanca E1 alcanza su máximo en M13, con la habilitación de las tiendas en enero; el acompañamiento de abril (M16) pertenece a producción y estabilización E1.'),
    ('Los peaks de etapas solapadas no se suman: pueden ocurrir en fechas distintas y compartir recursos en jornadas diferentes.',
     'Los picos de etapas solapadas no se suman, porque pueden ocurrir en meses distintos.'),
    (' No equivalen a puestos simultáneos ni a dedicaciones completas.', ''),
    ('; una persona puede actuar en distintos frentes en jornadas diferentes y no se suma dos veces al obtener la dotación total.', '.'),
    ('las personas equivalentes incluyen la cobertura de dirección, campo u operación del frente.', 'las personas equivalentes incluyen la cobertura de dirección, campo u operación del frente.'),
]:
    assert s.count(a) == 1, a
    s = s.replace(a, b)
for a in ['En particular, M15 incluye a los viajeros que se desplazan el 6 de abril para iniciar el acompañamiento en H7.']:
    if a in s:
        s = s.replace(' ' + a, '').replace(a, '')

# ---------------- 7. Reservas: estabilización ----------------
rep('Una dependencia FS no se sustituye por SS únicamente para acortar el dibujo del cronograma.',
    'Una dependencia FS no se sustituye por SS únicamente para acortar el dibujo del cronograma.\n\n'
    'La programación se estabilizó dentro de las holguras. Se desplazaron 77 actividades, con 10.636,05 HH, entre su inicio temprano y su inicio tardío, sin mover hitos ni fechas contractuales. Cada actividad desplazada conserva al menos 10 días hábiles de margen, o el que ya tenía si era menor, y ninguna actividad de la Etapa 2 empieza antes de M13. '
    'Con el trabajo de la red, el pico de M15 baja de 46,3 a 30,9 personas equivalentes y el desarrollo de la Etapa 2 se reparte entre M15 y M17. El mayor valor queda en M4, con 38,5 personas equivalentes, porque la cadena hacia H3 tiene poco margen. La Figura 7.17 del Subdocumento 7 compara ambas programaciones.')

# ---------------- 8. CPM ----------------
rep('Las relaciones de las tablas incluyen FS, SS y FF conforme a la red;',
    'La prueba de corte de enlace del piloto (1.9.9) tiene 3 días de holgura total, pero queda programada en su inicio tardío para coincidir con la instalación del lote 1; no le queda margen. La capacitación de la Etapa 2 se divide en dos partes. La parte anticipada de M17 (576 HH) no depende del software, y la parte dictada desde H9 (1.344 HH) tiene 3 días de holgura; por eso deja de pertenecer a una cadena vinculante de H12.\n\n'
    'Las relaciones de las tablas incluyen FS, SS y FF conforme a la red;')
rows = [l for l in filas_de('tab:t15-cadenas-H12') if not l.startswith('6 & Capacitación')]
filas_tabla('tab:t15-cadenas-H12', rows)
# ejemplos de margen: holgura v3
rows = []
for l in filas_de('tab:t15-14'):
    c = l.split(' & ')
    cand = [k for k, r in v3.items() if r['edt'] == c[0] and ddmmyyyy(cpm[k]['ES']) == c[2]]
    if cand:
        k = cand[0]; c[3] = ddmmyyyy(cpm[k]['LS']); c[4] = f"{cpm[k]['slack_days']} \\\\"
    rows.append(' & '.join(c))
filas_tabla('tab:t15-14', rows)

# tablas de holguras por rama, regeneradas con la red v3
SIG = {'DIS': 'AD', 'DEV': 'PR', 'QA': 'QA', 'PREP': 'PRE', 'PROD': 'PRO', 'CHECK': 'VER', 'CERT': 'CER', 'ACT': 'ACT',
       'ACCEPT': 'ACE', 'CORTE': 'PRO', 'OBS': 'VER'}
ORDEN = ['T', 'AD', 'PR', 'QA', 'PRE', 'PRO', 'SIT', 'VER', 'CER', 'ACT', 'ACE', 'MB', 'HIT', 'CAP']
SITIO = re.compile(r'^(T\d\d|CD0\d|PIL\d|LAB|DC01|S\d\d|RED|X\d*|R|F)$')
def sigla(k):
    p = k.split(':')
    if k.startswith('F:'):
        return 'SIT' if SITIO.match(p[-1]) or p[1] in ('1.4.2', '1.4.14', '1.4.15', '1.4.17', '1.4.19', '1.4.23') else 'T'
    if 'FIELD_ACT' in k: return 'HIT'
    if 'CAMPO' in k: return 'SIT'
    if 'MB-' in k: return 'MB'
    ph = p[2] if len(p) > 2 else ''
    if ph in SIG: return SIG[ph]
    if p[-2:-1] and p[-2] in SIG: return SIG[p[-2]]
    if 'CORTE' in k: return 'PRO'
    if 'OBS' in k: return 'VER'
    return 'T'
natural = lambda e: [int(x) for x in e.split('.')]
cap_old = collections.defaultdict(list)
for i in range(1, 16):
    lab = f'tab:t15-holguras-{i}'
    if lab in s:
        cap_old[i] = [l for l in filas_de(lab) if '\\newline CAP-' in l]
por_rama = collections.defaultdict(list)
for k, r in v3.items():
    if not r['edt'] or k not in cpm:
        continue
    por_rama[int(r['edt'].split('.')[1])].append(k)
tot_hh = D(0)
for i in range(1, 16):
    lab = f'tab:t15-holguras-{i}'
    if lab not in s:
        continue
    ks = sorted(por_rama[i], key=lambda k: (natural(v3[k]['edt']), ORDEN.index(sigla(k)), cpm[k]['ES'], k))
    ultimo_1419 = [k for k in ks if v3[k]['edt'] == '1.4.19'][-1:] 
    cnt = collections.Counter(); rows = []
    for k in ks:
        e = v3[k]['edt']; sg = sigla(k); cnt[(e, sg)] += 1
        c = cpm[k]; hh = num(v3[k]['HH'])
        if e == '1.13.4' and hh == 0:
            hh = D('416')  # inducción del equipo de operación (cobertura), como en el traspaso
        if k in ultimo_1419:
            hh += D('0.01')  # ajuste de céntimos, igual que en la tabla de la rama 1.4
        tot_hh += hh
        rows.append(f"{e}\\newline {sg}-{cnt[(e, sg)]:02d} & {net.nodes[k].get('duration_days', 0)} & {ddmmyyyy(c['ES'])} & {ddmmyyyy(c['EF'])} & {ddmmyyyy(c['LS'])} & {ddmmyyyy(c['LF'])} & {c['slack_days']} & {f2(hh)} \\\\")
    for l in cap_old[i]:
        tot_hh += num(l.split(' & ')[-1].rstrip('\\ ').replace('.', ''))
    rows = sorted(rows + cap_old[i], key=lambda l: (natural(l.split('\\newline')[0]), ORDEN.index(l.split('\\newline ')[1].split('-')[0])))
    filas_tabla(lab, rows)
print('HH en tablas de holguras:', f2(tot_hh))
assert f2(tot_hh) == '239.250,01', f2(tot_hh)

# ---------------- 9. Contingencia, incrementos, referencias e IA ----------------
rep('Los escenarios de activación del retén no se declaran financiados automáticamente por ella.',
    'Los escenarios de activación del retén no se declaran financiados automáticamente por ella.\n\n'
    'El análisis de escenarios de atraso del Subdocumento 7 (sección 7.3.3.2) atrasó 10 días hábiles la actividad que dispara cada uno de siete frentes, más una variante. Las respuestas que recuperan la fecha suman 491 HH, más el equivalente a unas 134 HH por el recargo de las horas extraordinarias. Se financian con esta reserva y se imputan al riesgo que las origina. El Jefe de Proyecto activa una respuesta cuando el control semanal muestra que el atraso de una actividad supera su margen restante.\n\n'
    '\\subsection{Incrementos y activación de la reserva}\n\n'
    'El plan de incrementos vincula los nueve intervalos de desarrollo con los dominios Retail y Emisor y separa las entregas transversales. Cada intervalo contiene cuatro sprints de catorce días naturales; los días restantes se destinan a integración y revisión. Diseño o construcción sin pruebas terminadas no se declaran incremento aceptado. Los registros entregados identifican EDT, actividad, responsable y criterio de aceptación, conservando las fechas del programa. No se distribuyen las HH uniformemente entre sprints.\n\n'
    'La matriz de riesgos vincula las 3.688 HH residuales a catorce riesgos. Sus cuatro agrupaciones suman 1.920, 600, 512 y 656 HH. Las 1.660 HH preventivas ya incluidas no se suman de nuevo. La activación exige registrar el disparador, la respuesta y su impacto sobre el hito; la reserva no equivale a una garantía de confianza ni cubre automáticamente el escenario extremo del retén.')
rep('\\subsection{Uso de inteligencia artificial}',
    '\\subsection{Referencias}\n\n'
    'Las ventanas de intervención respetan los congelamientos y las condiciones de convivencia del Caso 09 (Multitiendas Ancoa S.A., 2026, Caso 09, cap. 13, núms. 13.2--13.3, pp. 29--30). El inicio del 7 de enero de 2027 y las fechas exactas derivadas corresponden al calendario adoptado por el proponente.\n\n'
    '\\noindent\\hangindent=1.5em\\hangafter=1 Multitiendas Ancoa S.A. (2026). \\textit{Bases técnicas. Caso 09: Cadena multitienda} (Licitación N.° TFEP-01/2026, versión 1.0).\n\n'
    '\\subsection{Declaración de uso de IA}')
rep('PERT, CPM y curva HH & OpenAI Codex & Preparación y comprobación de cálculos y figura & Alta & Alex Alfaro \\\\',
    'PERT, CPM y curva HH & OpenAI Codex & Preparación y comprobación de cálculos y figura & Alta & Alex Alfaro \\\\\n'
    'Actualización con la red ampliada & Claude Code (Anthropic) & Componentes del Subdocumento 4, recálculo de tablas por paquete, mes, dotación y holguras, estabilización, curva y redacción de los cambios & Alta & Pendiente \\\\')
rep('\\ossFinalPage', 'La presente actualización fue asistida por OpenAI Codex y por Claude Code en texto, cálculos y figuras. La revisión humana de esta versión corresponde al equipo autor y se registrará al realizarse. Los responsables indicados en filas anteriores no implican aprobación de los cambios actuales.\n\n\\ossFinalPage')

assert '234.493' not in s and '238.181' not in s, [m.start() for m in re.finditer('234.493|238.181', s)]
open(OUT, 'w', encoding='utf-8').write(s)
print('ok', OUT, 'pico', pico, f2(tot_mes[pico]), 'pico op', pico_op, f2(tot_mes[pico_op]))
