"""Figuras SD-07 · Gantt con todas las dependencias (vistas de ruta crítica y de detalle), en página apaisada.

Criterios (GAO-16-89G y guía gantt-chart-visualization):
- Una fila por paquete del Formulario T-14 y fase de trabajo; las fases de un paquete van juntas; si una fase se
  repite por sitio, la fila indica cuántas actividades agrupa. Los hitos van en su fecha, antes que las actividades
  del mismo día. Los controles sin duración se dibujan como rombo vacío.
- Se dibujan todas las relaciones de la red entre las filas de la figura. Las que pasan por nodos de control se
  contraen al par de filas que unen. Conectores al estilo MS Project: FI sale del fin de la barra y entra por el inicio
  de la sucesora; II sale del inicio. Si la sucesora empieza antes, el conector rodea por debajo de la fila.
- Las predecesoras que no están en la figura van en la columna «Viene de»; las sucesoras que están en otra parte de la
  misma vista, en la columna «Sigue en» (solo si la vista tiene partes). La parte gráfica no lleva texto.
- Color con significado: rojo = ruta crítica (barras y conectores); gris = holgura 0 por fecha fija; ámbar = holgura
  de 10 días hábiles o menos; azul = más de 10. Conectores no críticos en gris suave.
Tamaño real: 23,2 cm de ancho, el alto útil de la página carta (se inserta rotada, a escala 1).
- Filas agrupadas (varios paquetes): se dibujan dos conectores, la primera relación (el primer paquete que pasa a la
  fila siguiente, sale por el borde de la barra) y la última (la que más empuja al hito).
Uso: <python con matplotlib> diag-07-14_gantt-dependencias.py <dir traspaso con Red_CPM/verificacion>
"""
import csv, json, os, re, sys, shutil, collections
from datetime import date, timedelta
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle, Patch
from matplotlib.lines import Line2D

for _f in ('Lato-Regular.ttf', 'Lato-Bold.ttf'):
    _r = os.path.join('/usr/share/fonts/truetype/lato', _f)
    if os.path.exists(_r):
        font_manager.fontManager.addfont(_r)
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
V = os.path.join(RAIZ, '80_Artefactos/sd-07_contexto/red-v3-2026-11-10')
CALS = os.path.join(RAIZ, '80_Artefactos/sd-07_contexto/traspaso-2026-11-10/Red_CPM/calendarios.json')
FIG = os.path.join(RAIZ, '02_Propuesta/latex_final/figuras/sd07-figuras')
HITOS_CSV = os.path.join(RAIZ, 'Economica/insumos-sd07/Hitos_contractuales.csv')
T14 = os.path.join(RAIZ, '02_Propuesta/latex_final/Formularios/OnlySimpleSolutions-Formulario-T-14.tex')
sys.path.insert(0, os.path.join(sys.argv[1], 'Red_CPM/verificacion'))
from motor_cpm_verificado_20261105 import Network
AZUL, AMBAR, ROJO, GRIS = '#196197', '#eda100', '#d03b3b', '#9aa3ad'
TEXTO, TEXTO2, GRILLA, BANDA, CABECERA, LINK = '#17324D', '#52514e', '#e6e6e3', '#f3f3f0', '#17324D', '#8a8f96'
W = 9.13
MESES_ES = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
plt.rcParams.update({'font.family': 'Lato', 'font.size': 9, 'text.color': TEXTO})
D = date.fromisoformat
rd = lambda p: json.load(open(p, encoding='utf-8-sig'))
NODOS, REL = rd(os.path.join(V, 'Red_CPM/nodos.json')), rd(os.path.join(V, 'Red_CPM/relaciones.json'))
N = {n['id']: n for n in NODOS}
net = Network(NODOS, REL, rd(CALS)); CPM = {r['id']: r for r in net.calculate()}
P = list(csv.DictReader(open(os.path.join(V, 'programacion_v3.csv'), encoding='utf-8-sig'), delimiter=';'))
PID = {r['id']: r for r in P}
HITOS = {r['hito']: D(r['fecha']) for r in csv.DictReader(open(HITOS_CSV, encoding='utf-8-sig'))}
NOMBRE = {m.group(1): m.group(2).strip() for m in re.finditer(r'^(1\.[\d.]+) & ([^&]*) &', open(T14, encoding='utf-8').read(), re.M)}
NOMBRE.setdefault('1.5', 'Desarrollo de software')
HITO_CORTO = {'H1': 'Línea base aprobada', 'H2': 'Arquitectura aprobada', 'H3': 'Infraestructura y ambientes',
              'H4': 'Software E1 para pruebas', 'H5': 'Certificación E1', 'H6': 'Inicio de marcha blanca E1',
              'H7': 'Producción E1', 'H8': 'Línea base y diseño E2', 'H9': 'Software E2 para pruebas',
              'H10': 'Certificación E2', 'H11': 'Inicio de marcha blanca E2', 'H12': 'Producción E2 y aceptación'}
FASE = {'PREP': 'preparación', 'PROD': 'intervención', 'CHECK': 'comprobación', 'CERT': 'certificación', 'ACT': 'activación',
        'ACCEPT': 'aceptación', 'DIS': 'diseño', 'DEV': 'construcción', 'QA': 'pruebas', 'FIS': 'instalación física',
        'RED': 'red', 'CORTE': 'corte', 'OBS': 'operación y conciliación'}
ORDEN_FASE = ['', 'DIS', 'PREP', 'FIS', 'RED', 'PROD', 'CORTE', 'OBS', 'DEV', 'QA', 'CHECK', 'CERT', 'ACT', 'ACCEPT']
PRED, SUCC = collections.defaultdict(list), collections.defaultdict(list)
for r in REL:
    PRED[r['succ']].append(r); SUCC[r['pred']].append(r)

def cadena(h):
    vis, pila = {h}, [h]
    while pila:
        k = pila.pop()
        for r in PRED[k]:
            if CPM.get(r['pred'], {}).get('slack_days') == 0 and r['pred'] not in vis:
                vis.add(r['pred']); pila.append(r['pred'])
    return vis
CRITICA = cadena('A:H7') | cadena('A:H12')

def mes_de(d):
    m = (d.year - 2027) * 12 + d.month
    return m if d.day >= 7 else m - 1
def es_hito(k):
    return k.startswith('A:H') and k[3:].isdigit()
def fase(k):
    p = k.split(':')
    if k.startswith('F:'):
        return p[-1] if p[-1] in FASE else 'FIS'
    for x in p[1:]:
        if x in FASE:
            return x
    return ''
def cat(k):
    return 'critica' if k in CRITICA else 'normal'
COLOR = {'critica': ROJO, 'fija': GRIS, 'casi': AMBAR, 'normal': AZUL}
ini = lambda k: D(PID[k]['inicio']) if k in PID else D(CPM[k]['ES'])
fin = lambda k: D(PID[k]['fin_exclusivo']) if k in PID else D(CPM[k]['EF'])
edt_de = lambda k: N.get(k, {}).get('edt') or PID.get(k, {}).get('edt') or ''

ETQ = {('', 'A:ACCEPT:E1:REVIEW'): 'Revisión del cliente de la certificación E1', ('', 'A:ACCEPT:E1:REWORK'): 'Reserva para subsanar observaciones E1',
       ('', 'CONTINUIDAD:MB1'): 'Continuidad del servicio en la marcha blanca E1', ('', 'A:OBSERVACION-28:E1'): 'Cuatro últimas semanas de evidencia E1',
       ('', 'A:REV-FINAL-MB:E1'): 'Revisión progresiva del expediente E1', ('', 'A:EVIDENCE_28:E1'): 'Evidencia completa E1 (control)',
       ('', 'A:ACCEPT:E2:REVIEW'): 'Revisión del cliente de la certificación E2', ('', 'A:ACCEPT:E2:REWORK'): 'Reserva para subsanar observaciones E2',
       ('', 'CONTINUIDAD:E1-PROD'): 'Continuidad del servicio de la Etapa 1 en producción', ('', 'A:OBSERVACION-28:E2'): 'Cuatro últimas semanas de evidencia E2',
       ('', 'A:REV-FINAL-MB:E2'): 'Revisión progresiva del expediente E2', ('', 'A:EVIDENCE_28:E2'): 'Evidencia completa E2 (control)',
       ('', 'E1:CANDIDATA'): 'Versión candidata verificada (control)',
       ('1.11.2', ''): 'Viaje y entrada oficial de las 22 tiendas'}

def filas_de(sel):
    grupos = collections.OrderedDict()
    for k in sorted(sel, key=lambda k: (ini(k), k)):
        if es_hito(k):
            grupos[('H', k)] = [k]; continue
        edt = edt_de(k)
        if edt.startswith('1.5.'):
            edt = '1.5'  # el software se agrupa por fase; su detalle por paquete está en el T-14
        grupos.setdefault((edt, fase(k)) if edt else ('', k), []).append(k)
    ini_paq = {}
    for (edt, f), ks in grupos.items():
        c = edt if edt not in ('', 'H') else (edt, f)
        v = HITOS[f[2:]] if edt == 'H' else min(ini(k) for k in ks)
        ini_paq[c] = min(ini_paq.get(c, date.max), v)
    def orden(item):
        (edt, f), ks = item
        if edt == 'H':
            return (HITOS[f[2:]], 0, [0], 0, date.min)
        c = edt if edt else (edt, f)
        orden_edt = [int(x) for x in edt.split('.')] if edt else [999]
        return (ini_paq[c], 1, orden_edt, ORDEN_FASE.index(f) if f in ORDEN_FASE else 99, min(ini(k) for k in ks))
    filas = []
    for (edt, f), ks in sorted(grupos.items(), key=orden):
        if edt == 'H':
            h = f[2:]; filas.append(dict(id=h, nombre=HITO_CORTO[h], corto=h, ks=ks, hito=True)); continue
        if (edt, f) in ETQ:
            nombre = ETQ[(edt, f)]
        elif ('', ks[0]) in ETQ:
            nombre = ETQ[('', ks[0])]
        elif edt:
            varias = len({fase(x) for x in sel if edt_de(x) == edt or (edt == '1.5' and edt_de(x).startswith('1.5.'))}) > 1 or edt == '1.5'
            nombre = f'{NOMBRE.get(edt, edt)}' + (f' · {FASE[f]}' if f in FASE and varias else '')
            if edt == '1.5':
                nombre += f' ({len({edt_de(x) for x in ks})} paquetes)'
        else:
            nombre = N[ks[0]].get('name') or ks[0]
        if len(ks) > 1 and (edt, f) not in ETQ and edt != '1.5':
            nombre += f' ({len(ks)})'
        filas.append(dict(id=edt or '–', nombre=nombre, corto=edt or nombre.split(' ')[0], ks=ks, hito=False))
    return filas

def dibujar(archivo, filas, x0, x1, otras=()):
    a_min = min(HITOS[f['corto']] if f['hito'] else min(ini(k) for k in f['ks']) for f in filas)
    b_max = max(HITOS[f['corto']] if f['hito'] else max(max(fin(k), ini(k) + timedelta(days=1)) for k in f['ks']) for f in filas)
    x0 = max(x0, a_min - timedelta(days=4)); x0 -= timedelta(days=x0.weekday())
    x1 = min(x1, b_max + timedelta(days=5))
    fila_de = {k: i for i, f in enumerate(filas) for k in f['ks']}
    en_otras = {k: f['corto'] for f in otras for k in f['ks']}
    arcos, primeros, externas, salidas = {}, {}, collections.defaultdict(set), collections.defaultdict(set)
    for i, f in enumerate(filas):
        for k in f['ks']:
            for r in PRED[k]:
                p = r['pred']
                if p in fila_de:
                    continue
                if p in en_otras:
                    externas[i].add(en_otras[p])
                elif es_hito(p):
                    externas[i].add(p[2:])
                elif edt_de(p):
                    externas[i].add(edt_de(p))
                elif p == 'A:INICIO-E2':
                    externas[i].add('inicio de E2')
                elif re.match(r'A:C\d+:S$', p):
                    externas[i].add(f"inicio de M{mes_de(D(N[p]['release']))}")
            pila, vistos = [(r['succ'], r['type']) for r in SUCC[k]], set()
            while pila:
                s, t = pila.pop()
                if s in vistos:
                    continue
                vistos.add(s)
                j = fila_de.get(s)
                if j is None:
                    if s in en_otras:
                        salidas[i].add(en_otras[s])
                    elif es_hito(s):
                        salidas[i].add(s[2:])
                    elif edt_de(s):
                        salidas[i].add(edt_de(s))
                    elif s != 'A:Z':
                        pila.extend((r['succ'], t) for r in SUCC[s])
                    continue
                if j == i:
                    continue
                cand = (t, fin(k) if t == 'FS' else ini(k), ini(s), k in CRITICA and s in CRITICA)
                prev = arcos.get((i, j))
                if prev is None or cand[1] > prev[1]:
                    arcos[(i, j)] = cand
                if t == 'FS':
                    pp = primeros.get((i, j))
                    if pp is None or cand[2] < pp[2] or (cand[2] == pp[2] and cand[1] > pp[1]):
                        primeros[(i, j)] = cand
    n = len(filas)
    hay_sig = any(salidas.values())
    hay_pri = any((len(filas[i]['ks']) > 1 or len(filas[j]['ks']) > 1) and (v[2] - arcos[(i, j)][2]).days <= -1 and arcos[(i, j)][0] == 'FS'
                  for (i, j), v in primeros.items())
    usadas = {cat(k) for f in filas if not f['hito'] for k in f['ks']}
    ley = [(Patch(facecolor=ROJO, label='Ruta crítica'), 'critica'), (Patch(facecolor=GRIS, label='Holgura 0 por fecha fija'), 'fija'),
           (Patch(facecolor=AMBAR, label='Holgura ≤ 10 días hábiles'), 'casi'), (Patch(facecolor=AZUL, label='Fuera de la ruta crítica' if 'critica' in usadas else 'Actividad'), 'normal')]
    ley = [h for h, c in ley if c in usadas] + [
        Line2D([], [], color=LINK, lw=0.8, label='Fin–inicio (FI)'), Line2D([], [], color=LINK, lw=0.8, ls=(0, (3, 2)), label='Inicio–inicio (II)')]
    if any(f['hito'] for f in filas):
        ley.insert(len([1 for _ in ley]) - 2, Line2D([], [], marker='D', color=TEXTO, lw=0, ms=5, label='Hito'))
    if hay_pri:
        ley.append(Line2D([], [], color=AMBAR, lw=1.0, label='Primer paquete que pasa a la fila siguiente'))
    NCOL = 6
    FILA, CAB = 0.28, 0.40
    PIE = 0.08 + 0.19 * -(-len(ley) // NCOL)
    H = CAB + n * FILA + PIE
    fig = plt.figure(figsize=(W, H))
    cols = dict(id=0.0, nom=0.46, vie=2.62)
    cols['sig'] = cols['vie'] + 0.8
    cols['ini'] = cols['sig'] + (0.72 if hay_sig else 0)
    cols['fin'] = cols['ini'] + 0.45
    cols['bar'] = cols['fin'] + 0.47
    top, bot = 1 - CAB / H, PIE / H
    ancho = W - cols['bar'] - 0.05
    tx = fig.add_axes([0, bot, cols['bar'] / W, top - bot]); tx.axis('off')
    ax = fig.add_axes([cols['bar'] / W, bot, ancho / W, top - bot]); ax.axis('off')
    hx = fig.add_axes([0, 1 - CAB / H, 1, CAB / H]); hx.axis('off'); hx.set_xlim(0, W); hx.set_ylim(0, 1)
    for a_ in (tx, ax):
        a_.set_ylim(n - 0.5, -0.5)
    tx.set_xlim(0, cols['bar'])
    X = lambda d: d.toordinal()
    ax.set_xlim(X(x0), X(x1))
    esc = ancho / (X(x1) - X(x0))
    dx = 0.06 / esc
    diaria = (x1 - x0).days <= 50
    hx.add_patch(Rectangle((0, 0.03), cols['bar'] - 0.02, 0.94, color=CABECERA, lw=0))
    encab = [(cols['id'] + 0.05, 'ID', 'left'), (cols['nom'] + 0.03, 'Actividad', 'left'), (cols['vie'] + 0.04, 'Viene de', 'left')] + ([(cols['sig'] + 0.04, 'Sigue en', 'left')] if hay_sig else []) + [
        (cols['ini'] + 0.225, 'Inicio', 'center'), (cols['fin'] + 0.225, 'Fin', 'center')]
    rend = fig.canvas.get_renderer()
    def lista(cods, x, ancho_col, y):
        cods, lim = sorted(cods), (ancho_col - 0.06) * fig.dpi
        for k in range(len(cods), 0, -1):
            resto = f'y {len(cods) - k} más' if k < len(cods) else ''
            for lineas in ([', '.join(cods[:k]) + (' ' + resto if resto else '')],
                           [', '.join(cods[:(k + 1) // 2]) + ',', ', '.join(cods[(k + 1) // 2:k]) + (' ' + resto if resto else '')] if k > 1 else
                           [cods[0], resto] if resto else None):
                if not lineas:
                    continue
                t_ = tx.text(x, y, '\n'.join(lineas), ha='left', va='center', fontsize=6.3, color=TEXTO2, linespacing=0.95)
                if t_.get_window_extent(rend).width <= lim or (k == 1 and len(lineas) == 2):
                    return
                t_.remove()
    for x, t, ha in encab:
        hx.text(x, 0.5, t, ha=ha, va='center', fontsize=8, fontweight='bold', color='white')
    d, k = date(x0.year, x0.month, 1), 0
    while d < x1:
        nxt = date(d.year + d.month // 12, d.month % 12 + 1, 1)
        a, b = max(d, x0), min(nxt, x1)
        xa, xb = cols['bar'] + (X(a) - X(x0)) * esc, cols['bar'] + (X(b) - X(x0)) * esc
        hx.add_patch(Rectangle((xa + 0.004, 0.52), xb - xa - 0.008, 0.45, color='#dfe6ee' if k % 2 else '#eef2f6', lw=0))
        hx.text((xa + xb) / 2, 0.75, f'{MESES_ES[d.month - 1]} {d.year}' if xb - xa > 0.55 else MESES_ES[d.month - 1], ha='center', va='center', fontsize=7)
        d, k = nxt, k + 1
    w, lunes = x0, 0
    salto = 1 if esc * 7 >= 0.17 else 2
    while w < x1:
        if diaria and w.weekday() >= 5:
            ax.axvspan(X(w), X(w) + 1, color=BANDA, zorder=0, lw=0)
        if w.weekday() == 0:
            ax.axvline(X(w), color=GRILLA, lw=0.5, zorder=0)
            if lunes % salto == 0:
                hx.text(cols['bar'] + (X(w) - X(x0)) * esc + 0.015, 0.27, str(w.day), ha='left', va='center', fontsize=6, color=TEXTO2)
            lunes += 1
        w += timedelta(days=1)
    segs = {}
    for i, f in enumerate(filas):
        if i % 2 == 0:
            for a_ in (tx, ax):
                a_.axhspan(i - 0.5, i + 0.5, color='#fafaf8', zorder=0, lw=0)
        if f['hito']:
            dh = HITOS[f['corto']]
            tx.text(cols['id'] + 0.05, i, f['id'], ha='left', va='center', fontsize=7, fontweight='bold')
            tx.text(cols['nom'] + 0.03, i, f['nombre'], ha='left', va='center', fontsize=7, fontweight='bold')
            for c in ('ini', 'fin'):
                tx.text(cols[c] + 0.225, i, dh.strftime('%d-%m-%y'), ha='center', va='center', fontsize=6.7, fontweight='bold')
            ax.plot(X(dh), i, marker='D', ms=7, color=ROJO if f['ks'][0] in CRITICA else TEXTO, zorder=6)
            if salidas.get(i):
                lista(salidas[i], cols['sig'] + 0.04, cols['ini'] - cols['sig'], i)
            continue
        a = min(ini(k) for k in f['ks']); b = max(fin(k) for k in f['ks'])
        tx.text(cols['id'] + 0.05, i, f['id'], ha='left', va='center', fontsize=6.7, color=TEXTO2)
        nombre, tam = f['nombre'], 7.2
        t_ = tx.text(cols['nom'] + 0.03, i, nombre, ha='left', va='center', fontsize=tam)
        lim = (cols['vie'] - cols['nom'] - 0.08) * fig.dpi
        while t_.get_window_extent(rend).width > lim and tam > 7.0:
            tam -= 0.25; t_.set_fontsize(tam)
        if t_.get_window_extent(rend).width > lim:
            pal = nombre.split(' ')
            t_.set_fontsize(6.8)
            def ancho_(txt):
                t_.set_text(txt); return t_.get_window_extent(rend).width
            corte = min(range(1, len(pal)), key=lambda c: max(ancho_(' '.join(pal[:c])), ancho_(' '.join(pal[c:]))))
            l1, l2 = ' '.join(pal[:corte]), ' '.join(pal[corte:])
            t_.set_text(l1 + '\n' + l2); t_.set_fontsize(6.8); t_.set_linespacing(0.95)
        tx.text(cols['ini'] + 0.225, i, a.strftime('%d-%m-%y'), ha='center', va='center', fontsize=6.7)
        tx.text(cols['fin'] + 0.225, i, (b - timedelta(days=1) if b > a else b).strftime('%d-%m-%y'), ha='center', va='center', fontsize=7)
        if a == b:
            ax.plot(X(a), i, marker='D', ms=6, markerfacecolor='white', markeredgecolor=ROJO if f['ks'][0] in CRITICA else TEXTO, zorder=6)
        tramos = sorted((max(ini(kk), x0), min(max(fin(kk), ini(kk) + timedelta(days=1)), x1), cat(kk)) for kk in f['ks'])
        unidos = []
        for p_, q_, c_ in tramos:
            if q_ <= p_ or a == b:
                continue
            if unidos and unidos[-1][2] == c_ and p_ <= unidos[-1][1]:
                unidos[-1][1] = max(unidos[-1][1], q_)
            else:
                unidos.append([p_, q_, c_])
        segs[i] = [(X(p_), X(q_)) for p_, q_, c_ in unidos]
        for p_, q_, c_ in unidos:
            ax.add_patch(Rectangle((X(p_), i - 0.22), X(q_) - X(p_), 0.44, facecolor=COLOR[c_], edgecolor='white', lw=0.3, zorder=3))
        if a < x0:
            ax.plot(X(x0) + dx, i, marker='<', ms=5, color=TEXTO2, zorder=4)
        externas[i].discard(f['id']); salidas[i].discard(f['id'])
        if externas.get(i):
            lista(externas[i], cols['vie'] + 0.04, cols['sig'] - cols['vie'], i)
        if salidas.get(i):
            lista(salidas[i], cols['sig'] + 0.04, cols['ini'] - cols['sig'], i)
    for i in range(n):
        tx.axhline(i + 0.5, color=GRILLA, lw=0.4); ax.axhline(i + 0.5, color=GRILLA, lw=0.4)
    trazos = [((i, j), v, 'ult') for (i, j), v in arcos.items()]
    for (i, j), v in primeros.items():
        u = arcos[(i, j)]
        if (len(filas[i]['ks']) > 1 or len(filas[j]['ks']) > 1) and (v[2] - u[2]).days <= -1 and u[0] == 'FS':
            trazos.append(((i, j), v, 'pri'))
    for (i, j), (t, xo_d, xs_d, critico), modo in sorted(trazos, key=lambda x: x[1][3]):
        col, lw = (ROJO, 1.0) if critico else (LINK, 0.6)
        if modo == 'pri':
            col, lw = AMBAR, 0.9
        xo, xs = X(min(max(xo_d, x0), x1)), X(min(max(xs_d, x0), x1))
        sgn = 1 if j > i else -1
        cuello = 2.6 * dx
        if t == 'FS':
            ruta = [(xo, i), (xo + dx, i)]
            if xs - cuello >= xo + dx:
                xv = min(xo + dx, xs - cuello)
                ruta = [(xo, i), (xv, i), (xv, j), (xs, j)] if xv > xo else ruta + [(xo + dx, j), (xs, j)]
            else:
                ym = j - 0.5 * sgn
                ruta += [(xo + dx, ym), (xs - cuello, ym), (xs - cuello, j), (xs, j)]
        else:
            xv = min(xo - dx, xs - cuello)
            ruta = [(xo, i), (xv, i), (xv, j), (xs, j)]
        dentro = any(a_ < xs - 0.5 and b_ >= xs - 0.5 for a_, b_ in segs.get(j, []))
        if modo == 'pri':
            ym = j - 0.5 * sgn
            if dentro:
                ruta = [(xo, i + 0.22 * sgn), (xo, ym), (xs + 0.5, ym), (xs + 0.5, j - 0.24 * sgn)]
            elif xs - cuello >= xo:
                ruta = [(xo, i + 0.22 * sgn), (xo, j), (xs, j)]
            else:
                ruta = [(xo, i + 0.22 * sgn), (xo, ym), (xs - cuello, ym), (xs - cuello, j), (xs, j)]
        elif dentro:
            ym = j - 0.5 * sgn
            xs2 = xs + 0.5
            ruta = [(xo, i), (xo + dx, i), (xo + dx, ym), (xs2, ym), (xs2, j - 0.24 * sgn)]
        if filas[j]['hito'] or len(filas[j]['ks']) == 1 and ini(filas[j]['ks'][0]) == fin(filas[j]['ks'][0]):
            ms_ = 7 if filas[j]['hito'] else 6
            (xa_, ya_), (xb_, yb_) = ruta[-2], ruta[-1]
            if abs(xb_ - xa_) > 1e-9:
                ruta[-1] = (xb_ - ms_ * 0.62 / 72 / esc, yb_)
            else:
                ruta[-1] = (xb_, yb_)
        xr, yr = zip(*ruta)
        ax.plot(xr, yr, color=col, lw=lw, ls='-' if t == 'FS' else (0, (3, 2)), zorder=5, solid_capstyle='butt')
        (xa_, ya_), (xb_, yb_) = ruta[-2], ruta[-1]
        if abs(xb_ - xa_) > 1e-9:
            punta, cola = (xb_ - 0.1 * dx, yb_), (xb_ - dx, yb_)
        else:
            punta, cola = (xb_, yb_), (xb_, yb_ - 0.15 * (1 if yb_ > ya_ else -1))
        ax.annotate('', xy=punta, xytext=cola,
                    arrowprops=dict(arrowstyle='->,head_length=0.55,head_width=0.3', color=col, lw=lw, shrinkA=0, shrinkB=0), zorder=6)
    fig.legend(handles=ley, loc='lower left', bbox_to_anchor=(0, 0), ncol=NCOL, frameon=False, fontsize=7, handlelength=1.5, columnspacing=0.9)
    base = os.path.join(AQUI, archivo)
    fig.savefig(base + '.png', dpi=300); fig.savefig(base + '.pdf'); plt.close(fig)
    shutil.copyfile(base + '.pdf', os.path.join(FIG, archivo + '.pdf'))
    print('ok', archivo, 'filas', n, 'conectores', len(trazos), dict(collections.Counter(v[0] for v in arcos.values())), 'alto', round(H, 2))

def vista(archivo, ventana, partes):
    filas_p = [filas_de(sel) for sel in partes]
    for m, fp in enumerate(filas_p):
        otras = [f for q, g in enumerate(filas_p) if q != m for f in g if not f['hito']]
        dibujar(archivo if len(partes) == 1 else f'{archivo}_p{m + 1}', fp, ventana[0], ventana[1], otras)

def sel_paq(edts, etapas, a, b, extra=(), fases=None):
    s_ = set()
    for r in P:
        if not r['edt'] or r['etapa'] not in etapas or float(r['HH'] or 0) <= 0:
            continue
        if not any(r['edt'] == e or r['edt'].startswith(e + '.') for e in edts):
            continue
        if not (r['inicio'] < b and r['fin_exclusivo'] >= a):
            continue
        if fases and fase(r['id']) not in fases:
            continue
        s_.add(r['id'])
    return s_ | set(extra)

if __name__ == '__main__':
    E1, E2 = ('E1', 'MB1', 'E1-PROD'), ('E2', 'MB2')
    sinC = lambda c: {k for k in c if not k.startswith(('A:C01', 'A:FIELD_ACT', 'CAMPO:', 'A:CLIENT'))} | ({'CAMPO:003'} if 'CAMPO:003' in c else set())
    vista('diag-07-14_gantt-ruta-critica-h7', (date(2027, 12, 1), date(2028, 4, 14)), [sinC(cadena('A:H7'))])
    vista('diag-07-14_gantt-ruta-critica-h12', (date(2028, 6, 1), date(2028, 9, 14)),
          [{k for k in sinC(cadena('A:H12')) if not k.startswith(('A:ACCEPT:E1', 'A:H5', 'A:H6', 'CONTINUIDAD:MB1'))}])
    a, b = '2027-03-01', '2027-07-12'
    vista('diag-07-14_gantt-infraestructura-h3', (date(2027, 3, 1), date(2027, 7, 12)), [
        sel_paq(['1.3.5', '1.4.1', '1.4.4', '1.4.6', '1.4.3', '1.4.5'], E1, a, b, extra=('A:H2',)),
        sel_paq(['1.4.16', '1.4.11', '1.4.12', '1.4.22'], E1, a, b) | {r['id'] for r in P if r['edt'] == '1.4.2' and r['inicio'] < '2027-05-31' and float(r['HH'] or 0) > 0},
        sel_paq(['1.4.15', '1.4.17', '1.4.23', '1.9.9'], E1, a, b, extra=('A:H3',)) | {r['id'] for r in P if r['edt'] == '1.4.2' and '2027-06-01' <= r['inicio'] < '2027-06-30'}])
    vista('diag-07-14_gantt-certificacion-h5', (date(2027, 9, 24), date(2028, 1, 12)), [
        sel_paq(['1.6.6', '1.10.2.4', '1.10.2.5', '1.10.2.6', '1.9.4', '1.8.6', '1.9.6', '1.7.3', '1.13.3', '1.14.4'], E1, '2027-09-24', '2028-01-12',
                extra=('E1:CANDIDATA', 'A:H4', 'A:H5', 'A:ACCEPT:E1:REVIEW', 'A:ACCEPT:E1:REWORK'))])
    vista('diag-07-14_gantt-diseno-h8', (date(2028, 1, 3), date(2028, 3, 14)), [
        sel_paq(['1.10.1.1', '1.10.3.1', '1.10.4.1', '1.10.5.1', '1.10.2.7', '1.7.3', '1.7.4', '1.7.7', '1.9.5'], E2, '2028-01-03', '2028-03-14', extra=('A:H8',)) |
        sel_paq(['1.5'], E2, '2028-01-03', '2028-03-14', fases=('DIS',))])
    vista('diag-07-14_gantt-construccion-h9', (date(2028, 2, 14), date(2028, 6, 14)), [
        sel_paq(['1.5'], E2, '2028-03-01', '2028-06-14', fases=('DEV', 'QA')) | sel_paq(['1.6.3', '1.6.4', '1.12.4'], E2, '2028-03-01', '2028-06-14') | {'F:1.13.3:E2-ANT', 'A:H9'},
        sel_paq(['1.10.1.2', '1.10.1.3', '1.10.1.4', '1.10.1.5', '1.10.3.2', '1.10.3.3', '1.10.3.4', '1.10.3.5',
                 '1.10.4.2', '1.10.4.3', '1.10.4.4', '1.10.4.5', '1.10.5.2', '1.10.5.3', '1.10.5.4', '1.10.5.5'], E2, '2028-03-01', '2028-06-14')])
    vista('diag-07-14_gantt-certificacion-h10', (date(2028, 5, 1), date(2028, 7, 14)), [
        sel_paq(['1.6.6', '1.9.4', '1.8.6', '1.8.8', '1.9.6', '1.14.3'], ('E2',), '2028-05-01', '2028-07-14') | {'1.13.3:E2:E2:237', 'A:ACCEPT:E2:REVIEW', 'A:ACCEPT:E2:REWORK', 'A:H10', 'A:H11'},
        sel_paq(['1.10.1.6', '1.10.1.7', '1.10.3.6', '1.10.3.7', '1.10.4.6', '1.10.4.7', '1.10.5.6', '1.10.5.7'], ('E2',), '2028-05-01', '2028-07-14')])
