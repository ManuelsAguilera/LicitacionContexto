"""Genera el Formulario T-14 con la red v3 a partir del .tex del traspaso (234.493,47 HH).

Uso: python3 -I gen_t14.py <dir traspaso> <repo> <salida.tex> <meses_v3.json> <meses_old.json>
- Preámbulo: el del T-14 del repositorio (plantilla vigente). Cuerpo: el del traspaso.
- Diccionario: HH de los paquetes que cambiaron entre la red del traspaso y la v3, filas nuevas
  (1.4.14 a 1.4.24 y 1.8.9), compras de 1.10.1 y 1.10.5, capacitación E2 en dos partes y ventanas v3.
- Carta Gantt: 18 láminas diag-07-04 con índice, lectura y conclusión.
"""
import sys, re, csv, json, collections
from decimal import Decimal as D

T, REPO, OUT, MV3, MOLD = sys.argv[1:6]
V = REPO + '/80_Artefactos/sd-07_contexto/red-v3-2026-11-10'
meses_v3, meses_old = json.load(open(MV3)), json.load(open(MOLD))
rd = lambda p: json.load(open(p, encoding='utf-8-sig'))
num = lambda s: D(str(s).replace('.', '').replace(',', '.'))
def f2(x):
    return f'{D(x):,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
ventana = lambda m: '; '.join('M' + p for p in m.split('; '))

L = open(T + '/Fuentes_LaTeX/Formularios/OnlySimpleSolutions-Formulario-T-14.tex', encoding='utf-8').read()
pre = open(REPO + '/02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-14.tex', encoding='utf-8').read()
s = pre[:pre.index('\\begin{document}')] + L[L.index('\\begin{document}'):]

def rep(old, new, n=1):
    global s
    c = s.count(old)
    if c != n:
        raise SystemExit(f'{c} apariciones (esperaba {n}): {old[:90]}')
    s = s.replace(old, new)

# HH por paquete: traspaso vs v3 (misma convención que el T-15)
orig = rd(T + '/Red_CPM/programacion.json')
v3 = list(csv.DictReader(open(V + '/programacion_v3.csv', encoding='utf-8-sig'), delimiter=';'))
old_p, new_p = collections.defaultdict(D), collections.defaultdict(D)
for x in orig:
    old_p[x.get('edt') or x['id'].split(':')[0]] += D(str(x.get('hh', 0)))
for r in v3:
    new_p[r['edt'] or r['id'].split(':')[0]] += D(r['HH'].replace(',', '.') or '0')
# Valores por paquete iguales a los del T-15 (HH_por_paquete_EDT.csv de la v3, que contiene el ajuste de céntimos)
pkg = {r['Paquete EDT']: D(r['HH'].replace(',', '.')) for r in csv.DictReader(open(V + '/HH_por_paquete_EDT.csv', encoding='utf-8-sig'), delimiter=';')}
cambio = {e: pkg[e] for e in new_p if '.' in e and abs(new_p[e] - old_p[e]) > D('0.005')}

# ---------------- textos generales ----------------
rep('El catálogo conserva 275 códigos de paquete, de los cuales 274 corresponden a entregables activos.',
    'El catálogo conserva 287 códigos de paquete, de los cuales 286 corresponden a entregables activos. Los doce paquetes agregados respecto de la versión anterior (1.4.14 a 1.4.24 y 1.8.9) provienen de la arquitectura física del Subdocumento 4.')
rep('La base de planificación suma \\textbf{234.493,47 HH}. La contingencia de 3.688 HH se administra separadamente, con un total de 238.181,47 HH si se considera esa reserva. Las cartas Gantt y la explicación de sus relaciones quedan pendientes de incorporación; la asignación de personas y capacidad corresponde al T-15.',
    'La base de planificación suma \\textbf{239.250,01 HH}. La contingencia de 3.688 HH se administra separadamente, con un total de 242.938,01 HH si se considera esa reserva. La carta Gantt por rama se presenta al final del formulario; la asignación de personas y capacidad corresponde al T-15.')
rep('Los demás paquetes se dimensionan por cantidades, actividades y dedicación por especialidad.',
    'Los demás paquetes se dimensionan por cantidades, actividades y dedicación por especialidad. Los componentes físicos del Subdocumento 4 siguen el mismo método, con la cantidad de unidades por las HH por unidad de tres valores; agregan 4.756,54 HH y se detallan en el Formulario T-15.')

# ---------------- diccionario: filas existentes ----------------
NOMBRE = {'1.4.2': 'Red de sitio y segmentación (25 sitios)', '1.4.3': 'Entornos dedicados de la Filial y del Control de cruces'}
CRITERIO = {
 '1.4.2': 'Red de sitio configurada y segmentada en los 25 sitios (22 tiendas, 2 centros de distribución y la tienda de laboratorio); prueba de conectividad conforme en 25 de 25 sitios.',
 '1.4.3': 'Entornos de producción y recuperación de la Filial y del Control de cruces con segregación física y lógica acreditada; 0 accesos cruzados entre ámbitos.',
}
def fila_dicc(l):
    m = re.match(r'^(1\.[\d.]+) & (.*) \\\\$', l)
    if not m:
        return l
    code = m.group(1); c = l[:-3].rstrip().split(' & ')
    if len(c) != 5:
        return l
    hh = c[3].split('\\newline ')
    if code in NOMBRE:
        c[1] = NOMBRE[code]
    if code in CRITERIO:
        c[2] = CRITERIO[code]
    if code in cambio and hh[0].endswith(' HH') and not hh[0].startswith('Subtotal'):
        hh[0] = f'{f2(cambio[code])} HH'
    if len(hh) > 1 and code in meses_old and code in meses_v3 and hh[1] == ventana(meses_old[code]) and meses_v3[code] != meses_old[code]:
        hh[1] = ventana(meses_v3[code])
    c[3] = '\\newline '.join(hh)
    return ' & '.join(c) + ' \\\\'
s = '\n'.join(fila_dicc(l) for l in s.split('\n'))

# capacitación de la Etapa 2 en dos partes
rep('Registro completo antes del acta de cierre. & ', 'Registro completo antes del acta de cierre. En la Etapa 2, 576 HH se dictan en M17 sobre los procesos y reglas aprobados en H8 y 1.344 HH desde H9 sobre el software con pruebas superadas. & ')
# compras de lockers y tótems
rep('1.10.1 & Lockers Ancoa 24/7 & Aceptación técnica E2 M19–20; habilitación M21; criterios de aceptación en los paquetes de esta rama; seguimiento específico hasta M56. & Subtotal 1.126,67 HH',
    '1.10.1 & Lockers Ancoa 24/7 & Aceptación técnica E2 M19–20; habilitación M21; criterios de aceptación en los paquetes de esta rama; seguimiento específico hasta M56. Incluye la orden de compra de los casilleros (8 de marzo de 2028) y su entrega (5 de mayo de 2028), 16,27 HH. & Subtotal 1.142,94 HH')
rep('1.10.5 & Modo Tienda con fila virtual de probadores & Aceptación técnica E2 M19–20; habilitación M21; criterios de aceptación en los paquetes de esta rama; seguimiento específico hasta M56. & Subtotal 1.409,33 HH',
    '1.10.5 & Modo Tienda con fila virtual de probadores & Aceptación técnica E2 M19–20; habilitación M21; criterios de aceptación en los paquetes de esta rama; seguimiento específico hasta M56. Incluye la orden de compra de los tótems (8 de marzo de 2028) y su entrega (5 de mayo de 2028), 16,27 HH. & Subtotal 1.425,60 HH')

# ---------------- diccionario: filas nuevas ----------------
H3, H4 = 'H3 (mes 6)', 'H4 (mes 10)'
NUEVAS_14 = [
 ('1.4.14', 'Levantamiento físico de 25 sitios', 'Levantamiento físico de los 25 sitios con planos, espacio, energía y conectividad registrados; 25 de 25 fichas aprobadas por la Contraparte Técnica.', H3),
 ('1.4.15', 'Tienda de laboratorio en Preproducción', 'Tienda de laboratorio instalada con el equipamiento de la tienda tipo y su pila local; acta de instalación sin observaciones abiertas antes del piloto técnico.', H3),
 ('1.4.16', 'Suministro de DC-01 y del lote 1', 'Órdenes emitidas el 11 de enero de 2027 (DC-01) y el 8 de marzo de 2027 (lote 1), con cantidades conformes a la especificación de 1.4.8; recepción conforme registrada.', H3),
 ('1.4.17', 'Tres tiendas piloto instaladas', 'Tres tiendas piloto instaladas y probadas antes del 18 de junio de 2027; acta por sitio sin observaciones abiertas.', H3),
 ('1.4.18', 'Suministro del lote 2 (19 tiendas y 2 CD)', 'Orden emitida el 7 de mayo de 2027 para 19 tiendas y 2 centros de distribución, con cantidades conformes a la especificación; recepción conforme registrada.', H4),
 ('1.4.19', 'Instalación del lote 2', '19 tiendas y 2 centros de distribución instalados y en servicio el 19 de septiembre de 2027; acta por sitio sin observaciones abiertas.', H4),
 ('1.4.20', 'Recuperación en Brazil South completa', 'Entorno de recuperación de los tres frentes escalado a tamaño completo y probado; operando a capacidad completa desde M13.', H4),
 ('1.4.21', 'Plataforma de datos y analítica', 'Plataforma de datos y analítica habilitada para los dos negocios con dominios segregados; 0 accesos cruzados en la prueba de autorización.', H3),
 ('1.4.22', 'Equipamiento TI y redes de DC-01', 'Equipamiento TI y redes de DC-01 instalados entre el 16 de abril y el 5 de mayo de 2027 y verificados antes de H3.', H3),
 ('1.4.23', 'Pila local de tienda (25 sitios)', 'Pila local desplegada y probada en los 25 sitios, con la operación desconectada de 24 horas ensayada en el laboratorio y en el piloto.', H4),
 ('1.4.24', 'Replicación entre regiones', 'Replicación entre regiones configurada para los tres frentes, con un RPO de 15 minutos medido en la prueba (RT-07.04).', H4),
]
def nueva(code, nombre, crit, hito, resp):
    return f'{code} & {nombre} & {crit} & {f2(cambio[code])} HH\\newline {ventana(meses_v3[code])}\\newline {hito} & {resp}\\newline Subdocumento 4. \\\\'
def insertar_y_total(label, filas, total):
    global s
    i = s.index('\\label{' + label + '}')
    j = s.index('\\textbf{Total rama}', i)
    k = s.index('\n', j)
    s = s[:j] + '\n'.join(filas) + '\n' + f'\\textbf{{Total rama}} &  &  & \\textbf{{{total} HH}} &  \\\\' + s[k:]
insertar_y_total('tab:t14-4', [nueva(*x, 'Arquitecto de Solución') for x in NUEVAS_14], '7.099,21')
insertar_y_total('tab:t14-8', [nueva('1.8.9', 'Controles de seguridad desplegados', 'Doce controles desplegados en sus frentes antes de las pruebas de la rama 1.9, con evidencia de configuración por control; 0 controles críticos sin desplegar en H3.', H3, 'Encargado de Seguridad de la Información')], '42.054,13')
rep('\\textbf{Total rama} &  &  & \\textbf{2.709,34 HH} &  \\\\', '', 0)
# total de la rama 1.10
i = s.index('\\label{tab:t14-10}'); j = s.index('\\textbf{Total rama}', i); k = s.index('\n', j)
tot10 = num(re.search(r'\\textbf\{([\d.,]+) HH\}', s[j:k]).group(1)) + D('32.54')
s = s[:j] + f'\\textbf{{Total rama}} &  &  & \\textbf{{{f2(tot10)} HH}} &  \\\\' + s[k:]
assert f2(tot10) == '8.873,90', f2(tot10)

# ---------------- carta Gantt ----------------
RAMAS = {'1.1': 'Dirección, gobierno y control del proyecto', '1.2': 'Levantamiento y línea base de alcance', '1.3': 'Arquitectura y diseño',
         '1.4': 'Infraestructura híbrida y plataforma base', '1.5': 'Desarrollo de software', '1.6': 'Integraciones',
         '1.7': 'Migración y saneamiento de datos', '1.8': 'Seguridad, identidad y cumplimiento', '1.9': 'Calidad, pruebas y certificación',
         '1.10': 'Innovaciones', '1.11': 'Implantación y despliegue', '1.12': 'Marchas blancas y aceptación por etapa',
         '1.13': 'Gestión del cambio y capacitación', '1.14': 'Documentación, transferencia y reversibilidad', '1.15': 'Operación y soporte'}
PARTES = {'1.4': 2, '1.5': 3}
figs = []
for r in RAMAS:
    n = PARTES.get(r, 1)
    for p in range(1, n + 1):
        arch = f"diag-07-04_gantt-rama-{r.replace('.', '-')}" + (f'_{p}' if n > 1 else '')
        cap = f'Cronograma detallado de la rama {r}, {RAMAS[r]}' + (f' (parte {p} de {n})' if n > 1 else '')
        figs.append('\n'.join(['\\begin{figure}[htbp]', '\\centering',
            f'\\includegraphics[width=\\linewidth,height=0.8\\textheight,keepaspectratio]{{figuras/sd07-figuras/{arch}.pdf}}',
            f'\\caption[{cap}]{{{cap}. Fuente: Elaboración propia a partir de la red del cronograma.}}\\label{{fig:t14-{r.replace(".", "-")}-{p}}}',
            '\\end{figure}']))
gantt = '\n'.join([
 '\\subsection{Carta Gantt}', '',
 'Las láminas siguientes desarrollan cada rama de la EDT hasta su tercer nivel. Cada fila es un paquete de trabajo o, en las ramas 1.5 y 1.10, una cuenta de control. La Tabla~\\ref{tab:t14-laminas} indica qué lámina corresponde a cada rama. El cronograma de hitos y el resumen de las quince ramas están en las Figuras 7.19 y 7.20 del Subdocumento 7.', '',
 '\\begingroup', '\\small',
 '\\begin{longtable}{@{}p{0.5\\linewidth}p{0.2\\linewidth}p{0.24\\linewidth}@{}}',
 '\\caption[Láminas del Gantt detallado por rama]{Láminas del Gantt detallado por rama. Fuente: Elaboración propia.}\\label{tab:t14-laminas}\\\\',
 '\\toprule', '\\textbf{Rama} & \\textbf{Láminas} & \\textbf{Elementos de tercer nivel} \\\\', '\\midrule', '\\endhead', '\\bottomrule', '\\endlastfoot',
 '1.1 a 1.3 & T-14.1 a T-14.3 & Una lámina por rama \\\\',
 '1.4 Infraestructura híbrida y plataforma base & T-14.4 y T-14.5 & 24 paquetes \\\\',
 '1.5 Desarrollo de software & T-14.6 a T-14.8 & 51 cuentas de control \\\\',
 '1.6 a 1.15 & T-14.9 a T-14.18 & Una lámina por rama \\\\',
 '\\end{longtable}', '\\endgroup', '',
 'La columna HH suma las horas de las actividades del elemento. La ventana indica el primer y el último mes con trabajo. El margen es la cantidad de días hábiles que la actividad más ajustada del elemento puede atrasarse sin mover su sucesora. Un margen 0, en naranja, coincide con el borde oscuro de la barra. Las barras se colorean por etapa. Los elementos sin actividades propias se ejecutan dentro de la dirección del proyecto o del equipo de operación, y sus horas están en esas coberturas.', '']
 + figs + ['',
 'Con este detalle se puede ubicar cada hora planificada en su paquete y en su mes, y ver qué paquetes no tienen margen. Esos paquetes son los que el Jefe de Proyecto controla semanalmente y los primeros en recibir las respuestas de compresión descritas en la sección 7.3.3.2 del Subdocumento 7. El método de estimación de duraciones, el cálculo CPM y los resultados de holgura se presentan en el Formulario T-15.', ''])
a = s.index('\\subsection{Carta Gantt}'); b = s.index('\\subsection{Referencias}')
s = s[:a] + gantt + s[b:]
rep('\\renewcommand{\\thetable}{T-14.\\arabic{table}}', '\\renewcommand{\\thetable}{T-14.\\arabic{table}}\n\\renewcommand{\\thefigure}{T-14.\\arabic{figure}}')
rep('\\listoftables\n', '\\listoffigures\n\\listoftables\n')

# ---------------- referencias e IA ----------------
rep('Multitiendas Ancoa S.A. (2026). Bases Técnicas del Caso 09 -- Cadena Multitienda. Licitación TFEP-01/2026.',
    'Las ventanas del cronograma respetan los congelamientos y las condiciones de convivencia del Caso 09 (Multitiendas Ancoa S.A., 2026, Caso 09, cap. 13, núms. 13.2--13.3, pp. 29--30).\n\n'
    '\\noindent\\hangindent=1.5em\\hangafter=1 Multitiendas Ancoa S.A. (2026). \\textit{Bases técnicas. Caso 09: Cadena multitienda} (Licitación N.° TFEP-01/2026, versión 1.0).')
rep('Cálculo y anexos & OpenAI Codex & Preparación y comprobación reproducible de estimaciones y precedencias & Alta & Alex Alfaro \\\\',
    'Cálculo y anexos & OpenAI Codex & Preparación y comprobación reproducible de estimaciones y precedencias & Alta & Alex Alfaro \\\\\n'
    'Actualización con la red ampliada & Claude Code (Anthropic) & Paquetes del Subdocumento 4, HH y ventanas de la red v3, láminas de la carta Gantt y redacción de los cambios & Alta & Pendiente \\\\')
rep('\\ossFinalPage', 'La presente actualización fue asistida por OpenAI Codex y por Claude Code en texto, cálculos y figuras. La revisión humana de esta versión corresponde al equipo autor y se registrará al realizarse. Los responsables indicados en filas anteriores no implican aprobación de los cambios actuales.\n\n\\ossFinalPage')

assert '234.493' not in s and '238.181' not in s and '13 tiendas' not in s, 'cifras antiguas'
open(OUT, 'w', encoding='utf-8').write(s)
print('ok', OUT, 'cambios', len(cambio))
