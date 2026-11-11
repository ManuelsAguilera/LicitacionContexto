"""Equivalencia de roles con el Formulario E-26 (Bases Administrativas, p. 76) sobre la red v2.

Reglas decididas por el usuario (2026-11-10):
  - Arquitecto: 1 Arquitecto Experto (hasta 160 HH al mes) y el resto Arquitecto Senior.
  - Desarrollo: todo Ingeniero Senior.
  - Líder Funcional = Jefe de Análisis y Diseño: hasta 160 HH al mes del análisis de negocio, M1–M20.
  - Líder de Calidad = Analista QA Experto: hasta 160 HH al mes de la ingeniería de pruebas, M1–M21.
  - Otros roles declarados (E-26 los admite): Formador de usuarios y Especialista legal y de privacidad.
Genera: equivalencias_roles_E26.csv, HH/FTE_matriz_perfiles_E26_M1_M56.csv, HH_paquete_x_perfil_E26.csv,
HH_por_paquete_EDT.csv. Uso: python3 -I equivalencia_e26_v2.py <traspaso> <dir red v2> <dir salida>
"""
import sys, csv, json, collections
from decimal import Decimal
from bisect import bisect_left

T, RV, OUT = sys.argv[1:4]
sys.path.insert(0, T + '/Red_CPM/verificacion')
from motor_cpm_verificado_20261105 import Network

E26 = {
    'Jefe de Proyecto': (0.8, 2.1, 1.5, 3.0), 'Jefe de Análisis y Diseño': (0.7, 1.4, 1.0, 2.0),
    'Jefe de Desarrollo': (0.7, 1.4, 1.0, 2.0), 'Jefe de TIC': (0.7, 1.4, 1.0, 2.0),
    'Analista / Diseñador Experto': (0.5, 0.8, 0.8, 1.2), 'Analista / Diseñador Senior': (0.5, 0.7, 0.7, 1.0),
    'Analista / Diseñador Junior': (0.3, 0.6, 0.5, 0.8), 'Ingeniero Experto': (0.6, 1.0, 1.0, 1.5),
    'Ingeniero Senior': (0.6, 0.8, 0.8, 1.2), 'Arquitecto Experto': (0.8, 1.4, 1.5, 2.5),
    'Arquitecto Senior': (0.8, 1.4, 1.2, 2.0), 'Encargado de Seguridad TI': (0.8, 1.4, 1.5, 2.5),
    'Ingeniero de Datos': (0.6, 1.0, 1.0, 1.5), 'Ingeniero DevOps / SRE': (0.6, 1.0, 1.0, 1.5),
    'TIC': (0.6, 1.0, 0.8, 1.5), 'Documentador': (0.3, 0.7, 0.5, 1.0),
    'Analista QA Experto': (0.5, 0.7, 0.8, 1.0), 'Analista QA Senior': (0.4, 0.6, 0.6, 0.8),
    'Analista QA Junior': (0.3, 0.4, 0.4, 0.6),
    'Otro: Formador de usuarios': (0.3, 0.6, 0.5, 0.8),
    'Otro: Especialista legal y de privacidad': (0.5, 0.8, 0.8, 1.2),
}
MAPA = {
    'TIC (NOC)': ('TIC', 'Operación de monitoreo'), 'TIC (mesa de servicio L1)': ('TIC', 'Primer nivel'),
    'TIC (operación SOC)': ('TIC', 'Vigilancia 24/7'), 'TIC (implantación)': ('TIC', 'Instalación y acompañamiento'),
    'Gestor de activos': ('TIC', 'Inventario'),
    'Ingeniero (desarrollo)': ('Ingeniero Senior', 'Construcción de software (decisión: todo Senior)'),
    'Ingeniero infraestructura física': ('Ingeniero Senior', 'Racks, energía y clima'),
    'Especialista de redes': ('Ingeniero Senior', 'Red de sitio'),
    'Ingeniero (IoT y hardware)': ('Ingeniero Senior', 'Lockers y dispositivos'),
    'Especialista de operación': ('Ingeniero Senior', 'Procedimientos de operación'),
    'Ingeniero / Ingeniero de Datos (L3)': ('Ingeniero Experto', 'Tercer nivel de soporte'),
    'Ingeniero DevOps / SRE (L2)': ('Ingeniero DevOps / SRE', 'Equivalencia directa'),
    'Ingeniero DevOps / SRE': ('Ingeniero DevOps / SRE', 'Equivalencia directa'),
    'Ingeniero de Datos (integración y migración)': ('Ingeniero de Datos', 'Equivalencia directa'),
    'Ingeniero de Datos (modelos y ML)': ('Ingeniero de Datos', 'Conteo predictivo y búsqueda'),
    'Arquitecto (solución)': ('Arquitecto Senior', '1 Arquitecto Experto hasta 160 HH/mes; resto Senior'),
    'Analista / Diseñador (negocio)': ('Analista / Diseñador Senior', 'Líder Funcional hasta 160 HH/mes en M1–M20; resto Senior'),
    'Analista PMO': ('Analista / Diseñador Senior', 'Control del proyecto'),
    'Analista / Diseñador (UX)': ('Analista / Diseñador Senior', 'Experiencia de usuario'),
    'Especialista transferencia': ('Analista / Diseñador Senior', 'Traspaso'),
    'Diseñador instruccional': ('Analista / Diseñador Senior', 'Diseño de capacitación'),
    'Gestor del cambio': ('Analista / Diseñador Senior', 'Gestión del cambio'),
    'Facilitador': ('Analista / Diseñador Senior', 'Talleres'),
    'Especialista financiero y de cumplimiento (adicional)': ('Analista / Diseñador Experto', 'Regulación del emisor'),
    'Especialista en procesos logísticos (adicional)': ('Analista / Diseñador Experto', 'Dominio especializado'),
    'Especialista en comunicación y cambio (adicional)': ('Analista / Diseñador Junior', 'Comunicación'),
    'Formador de usuarios (adicional)': ('Otro: Formador de usuarios', 'No está en el E-26; declarado'),
    'Especialista privacidad / legal': ('Otro: Especialista legal y de privacidad', 'No está en el E-26; declarado'),
    'Gerente de servicio': ('Jefe de TIC', 'Dirige la operación TIC'),
    'Jefe de Proyecto': ('Jefe de Proyecto', 'Equivalencia directa'),
    'Jefe de Desarrollo': ('Jefe de Desarrollo', 'Incluye coordinación técnica'),
    'Analista QA (ingeniería de pruebas)': ('Analista QA Senior', 'Líder de Calidad hasta 160 HH/mes en M1–M21; resto Senior'),
    'Analista QA (ejecución de pruebas)': ('Analista QA Junior', 'Ejecuta pruebas'),
    'Especialista de seguridad': ('Encargado de Seguridad TI', 'Controles de seguridad'),
    'Especialista seguridad ofensiva': ('Encargado de Seguridad TI', 'Pruebas de intrusión'),
    'Auditor de seguridad': ('Encargado de Seguridad TI', 'Cumplimiento'),
    'Redactor técnico': ('Documentador', 'Equivalencia directa'),
}
# Roles con un líder de una persona: (perfil líder, meses en que aplica)
LIDER = {'Arquitecto (solución)': ('Arquitecto Experto', range(1, 57)),
         'Analista / Diseñador (negocio)': ('Jefe de Análisis y Diseño', range(1, 21)),
         'Analista QA (ingeniería de pruebas)': ('Analista QA Experto', range(1, 22))}
TOPE = Decimal(160)
num = lambda s: Decimal(s.replace(',', '.'))
fmt = lambda x: f'{x:.2f}'.replace('.', ',')
fmtr = lambda x: f'{x:.1f}'.replace('.', ',')

rol_mes = {r['Rol']: [num(r[f'M{m}']) for m in range(1, 57)] for r in
           csv.DictReader(open(f'{RV}/HH_matriz_roles_M1_M56.csv', encoding='utf-8-sig'), delimiter=';')}
assert not set(rol_mes) - set(MAPA), set(rol_mes) - set(MAPA)
# Fracción del líder por rol y mes
frac = {}
for rol, (lid, meses) in LIDER.items():
    frac[rol] = [(min(v, TOPE) / v if v > 0 and (m + 1) in meses else Decimal(0)) for m, v in enumerate(rol_mes[rol])]
def reparto(rol, m, h):
    """Devuelve [(perfil, horas)] para un rol en el mes m (1..56)."""
    base = MAPA[rol][0]
    if rol in LIDER and frac[rol][m - 1] > 0:
        f = frac[rol][m - 1]
        return [(LIDER[rol][0], h * f), (base, h * (1 - f))]
    return [(base, h)]

perf_mes = collections.defaultdict(lambda: [Decimal(0)] * 56)
for rol, vals in rol_mes.items():
    for m, h in enumerate(vals, 1):
        for p, x in reparto(rol, m, h):
            perf_mes[p][m - 1] += x

# Paquete × perfil: actividades de la red v2 en su ventana final + dotación por componente
rd = lambda p: json.load(open(p, encoding='utf-8-sig'))
cals = rd(T + '/Red_CPM/calendarios.json')
net = Network(rd(f'{RV}/Red_CPM/nodos.json'), rd(f'{RV}/Red_CPM/relaciones.json'), cals)
net.calculate()
for k, v in rd(f'{RV}/estabilizacion.json')['proposed_start'].items():
    if v is not None:
        net.result[k]['proposed_start'] = v
final = {r['id']: r for r in net.schedule_preferred()}
nombres = rd(T + '/Datos_base/equivalencias_nombres_E26.json')
MESES = [(int(m['mes']), m['inicio']) for m in
         csv.DictReader(open(T + '/Datos_base/dotacion_y_reservas_56_meses.csv', encoding='utf-8-sig'))]
INI = [m[1] for m in MESES]
mes = lambda ds: MESES[bisect_left(INI, ds + 'z') - 1][0]
COORD = 'Líder técnico / coordinación de desarrollo'
paq = collections.defaultdict(Decimal)
ventana = collections.defaultdict(list)
nombre_paq = {p['edt']: p['name'] for p in rd(T + '/Red_CPM/ledger_275_paquetes.json')['packages']}
for k, n in net.nodes.items():
    if not n.get('hh') or not n.get('edt'):
        continue
    e = n['edt']
    nombre_paq.setdefault(e, n.get('name', '').split(' · ')[0])
    r = dict(n.get('role_hh') or {})
    extra = float(n['hh']) - sum(r.values())
    if extra > 0.005:
        r[COORD] = r.get(COORD, 0) + extra
    ds = cals[n['calendar']]
    dias = ds[bisect_left(ds, final[k]['start']):bisect_left(ds, final[k]['finish'])] or [final[k]['start']]
    ventana[e].append((final[k]['start'], final[k]['finish']))
    por_mes = collections.Counter(mes(d) for d in dias)
    for rol, h in r.items():
        rol = nombres.get(rol, rol)
        for m, c in por_mes.items():
            for p, x in reparto(rol, m, Decimal(str(h)) * c / len(dias)):
                paq[(e, p)] += x
DOT = {'Cobertura de campo': '1.11.2', 'Dirección y PMO': '1.1.1', 'Inducción de operación': '1.13.4'}
for r in csv.DictReader(open(T + '/HH_detalle_mes_rol_componente.csv', encoding='utf-8-sig'), delimiter=';'):
    c = r['Componente']
    if c == 'Trabajo técnico y viajes':
        continue
    e = ('1.8.2' if r['Rol'] == 'TIC (operación SOC)' else '1.15') if c == 'Operación' else DOT[c]
    m = int(r['Mes'][1:])
    for p, x in reparto(r['Rol'], m, Decimal(r['HH'].replace('.', '').replace(',', '.'))):
        paq[(e, p)] += x
    ventana[e].append(None)

t_mes, t_paq = sum(sum(v) for v in perf_mes.values()), sum(paq.values())
assert abs(t_mes - t_paq) < Decimal('1'), (t_mes, t_paq)

perfiles = sorted(perf_mes, key=lambda p: -sum(perf_mes[p]))
with open(f'{OUT}/equivalencias_roles_E26.csv', 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f, delimiter=';')
    w.writerow(['Rol del plan', 'Perfil E-26', 'Costo mín UF/h', 'Costo máx UF/h', 'Tarifa mín UF/h',
                'Tarifa máx UF/h', 'HH del rol', 'Regla o razón'])
    for rol in sorted(rol_mes, key=lambda r: (MAPA[r][0], r)):
        p, razon = MAPA[rol]
        perfs = [p] + ([LIDER[rol][0]] if rol in LIDER else [])
        for q in perfs:
            w.writerow([rol, q] + [fmtr(x) for x in E26[q]] + [fmt(sum(rol_mes[rol])), razon])
for nombre, div in [('HH_matriz_perfiles_E26_M1_M56.csv', 1), ('FTE_matriz_perfiles_E26_M1_M56.csv', 160)]:
    with open(f'{OUT}/{nombre}', 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(['Perfil E-26', 'Costo mín UF/h', 'Costo máx UF/h', 'Tarifa mín UF/h', 'Tarifa máx UF/h']
                   + [f'M{m}' for m in range(1, 57)] + ['Total'])
        for p in perfiles:
            vals = [v / div for v in perf_mes[p]]
            w.writerow([p] + [fmtr(x) for x in E26[p]] + [fmt(v) for v in vals] + [fmt(sum(vals))])
clave = lambda e: [int(x) for x in e.split('.') if x.isdigit()]
paquetes = sorted({e for e, _ in paq}, key=clave)
with open(f'{OUT}/HH_paquete_x_perfil_E26.csv', 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f, delimiter=';')
    w.writerow(['Paquete EDT', 'Nombre'] + perfiles + ['Total'])
    for e in paquetes:
        vals = [paq.get((e, p), Decimal(0)) for p in perfiles]
        w.writerow([e, nombre_paq.get(e, '')] + [fmt(v) for v in vals] + [fmt(sum(vals))])
with open(f'{OUT}/HH_por_paquete_EDT.csv', 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f, delimiter=';')
    w.writerow(['Paquete EDT', 'Rama', 'Nombre', 'HH', 'Ventana'])
    for e in paquetes:
        vs = [v for v in ventana[e] if v]
        vent = f'M{mes(min(a for a, b in vs))}–M{mes(max(b for a, b in vs))}' if vs else 'Dotación (ver Dotacion_coberturas.csv)'
        w.writerow([e, '.'.join(e.split('.')[:2]), nombre_paq.get(e, ''),
                    fmt(sum(paq.get((e, p), Decimal(0)) for p in perfiles)), vent])
print(json.dumps(dict(perfiles=len(perfiles), total_mes=float(round(t_mes, 2)), total_paquetes=float(round(t_paq, 2)),
                      paquetes=len(paquetes)), ensure_ascii=False))
