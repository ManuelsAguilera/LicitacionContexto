"""Llena el modelo financiero (E-21, Entregable 3) a partir de los insumos de Economica/insumos-sd07/.

Uso: python llenar_modelo.py <planilla de entrada .xlsx> <planilla de salida .xlsx>

Conserva la hoja RESUMEN (rótulos de la plantilla) y reescribe el resto solo con fórmulas. Los datos de entrada
quedan en PARÁMETROS y en hojas de entrada (DOTACIÓN, ADQUISICIONES, PCUESFUERZO, HARDWARE CLIENTE). Decisiones del
equipo (2026-11-11): costo por perfil = punto medio del E-26; tarifa = máximo entre costo ÷ (1 − rentabilidad
objetivo) y el mínimo del E-26; el margen de los demás componentes se ajusta para que el proyecto cierre en la
rentabilidad objetivo; precios de equipos y nube de referencia pública, sin cotización.
"""
import csv, os, sys, re, collections
from datetime import date
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Protection
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter as L
from openpyxl.chart import LineChart, Reference, Series
from openpyxl.chart.series import SeriesLabel
from openpyxl.chart.data_source import StrRef
from precios_referencia import ITEMS, HARDWARE_CLIENTE

AQUI = os.path.dirname(os.path.abspath(__file__))
INS = os.path.normpath(os.path.join(AQUI, '..', 'insumos-sd07'))
PLANTILLA = os.path.normpath(os.path.join(AQUI, '..', 'FLUJO-DE-CAJA-VACIO.xlsx'))
N_MESES = 56
num = lambda x: float(x.replace('.', '').replace(',', '.')) if str(x).strip() else 0.0
def leer(nombre, delim=';'):
    return list(csv.reader(open(os.path.join(INS, nombre), encoding='utf-8-sig'), delimiter=delim))

F_BASE = Font(name='Arial', size=10)
F_NEG = Font(name='Arial', size=10, bold=True)
F_TIT = Font(name='Arial', size=13, bold=True)
F_IN = Font(name='Arial', size=10, color='0000FF')
F_CAB = Font(name='Arial', size=10, bold=True, color='FFFFFF')
R_CAB = PatternFill('solid', fgColor='17324D')
R_IN = PatternFill('solid', fgColor='FFF9D6')
R_TOT = PatternFill('solid', fgColor='E8EEF4')
NUM, PCT, ENT = '#,##0.00', '0.00%', '#,##0'
mc = lambda m: L(2 + m)            # columna del mes m en las hojas mensuales (C..BF)
C1, CN = mc(1), mc(N_MESES)
def q(hoja):
    return "'" + hoja + "'!"

def fecha_mes(m):
    y, mm = divmod(m - 1, 12)
    return date(2027 + y, mm + 1, 7)

class Hoja:
    def __init__(self, wb, nombre, titulo, nota=None):
        self.ws = wb.create_sheet(nombre); self.n = nombre
        self.set('A1', titulo, F_TIT)
        if nota:
            self.set('A2', nota)
    def set(self, ref, v, font=F_BASE, fmt=None, fill=None, wrap=False):
        c = self.ws[ref]; c.value = v; c.font = font
        if fmt: c.number_format = fmt
        if fill: c.fill = fill
        if wrap: c.alignment = Alignment(wrap_text=True, vertical='top')
        return c
    def entrada(self, ref, v, fmt=None):
        return self.set(ref, v, F_IN, fmt, R_IN)
    def cab(self, fila, textos, col0=1):
        for k, t in enumerate(textos):
            c = self.ws.cell(fila, col0 + k, t); c.font = F_CAB; c.fill = R_CAB
            c.alignment = Alignment(wrap_text=True, vertical='center')
    def meses(self, fila_fecha=2, fila_mes=3, col_fn=mc, total_col='B'):
        if total_col:
            self.set(f'{total_col}{fila_mes}', 'Total', F_CAB, fill=R_CAB)
        self.set(f'A{fila_mes}', 'Mes', F_CAB, fill=R_CAB)
        self.set(f'A{fila_fecha}', 'Inicio del mes') if self.ws[f'A{fila_fecha}'].value is None else None
        for m in range(1, N_MESES + 1):
            c = self.set(f'{col_fn(m)}{fila_mes}', m, F_CAB, ENT, R_CAB)
            self.set(f'{col_fn(m)}{fila_fecha}', fecha_mes(m), F_BASE, 'DD-MM-YY')
    def fila_mensual(self, fila, rotulo, formula, fmt=NUM, total=True, font=F_BASE, fill=None, col_fn=mc):
        """formula: función (m, col) -> texto de fórmula."""
        self.set(f'A{fila}', rotulo, font, fill=fill)
        for m in range(1, N_MESES + 1):
            self.set(f'{col_fn(m)}{fila}', formula(m, col_fn(m)), font, fmt, fill)
        if total:
            self.set(f'B{fila}', f'=SUM({col_fn(1)}{fila}:{col_fn(N_MESES)}{fila})', F_NEG, fmt, fill or R_TOT)
    def anchos(self, a=42, b=14, resto=11):
        self.ws.column_dimensions['A'].width = a; self.ws.column_dimensions['B'].width = b
        for m in range(1, N_MESES + 1):
            self.ws.column_dimensions[mc(m)].width = resto
        self.ws.freeze_panes = 'C4'

def construir(entrada, salida):
    wb = openpyxl.load_workbook(entrada)
    for n in list(wb.sheetnames):
        if n != 'RESUMEN':
            del wb[n]

    # ------------------------------------------------------------------ PARÁMETROS
    hp = Hoja(wb, 'PARÁMETROS', 'Parámetros y supuestos',
              'Celdas azules con fondo amarillo: datos de entrada. El resto se calcula. Cada dato lleva su fuente.')
    hp.cab(3, ['Parámetro', 'Valor', 'Unidad', 'Fuente o criterio'])
    P = {}; fila = [3]
    PR = q('PARÁMETROS')
    def par(clave, rotulo, valor, unidad='', fuente='', fmt=None, formula=False):
        fila[0] += 1; r = fila[0]
        hp.set(f'A{r}', rotulo)
        (hp.set if formula else hp.entrada)(f'B{r}', valor, **({'fmt': fmt} if fmt else {}))
        if formula and fmt: hp.ws[f'B{r}'].number_format = fmt
        hp.set(f'C{r}', unidad); hp.set(f'D{r}', fuente)
        P[clave] = f'{PR}$B${r}'; P['_' + clave] = f'$B${r}'
        return r
    def seccion(t):
        fila[0] += 2; hp.set(f'A{fila[0]}', t, F_NEG, fill=R_TOT)
    E24 = 'Formulario E-24, Bases Administrativas (folio 73)'
    seccion('Formulario E-24')
    par('usd', 'Dólar (USD)', 900, 'CLP', E24, ENT)
    par('eur', 'Euro (EUR)', 1000, 'CLP', E24, ENT)
    par('uf', 'Unidad de Fomento (UF)', 40000, 'CLP', E24, ENT)
    par('tasa_cred', 'Tasa de interés del crédito', 0.009, 'mensual', E24, '0.00%')
    par('tasa_lc', 'Tasa de interés de la línea de crédito', 0.03, 'mensual', E24, '0.00%')
    par('rent_max', 'Rentabilidad máxima (EBITDA / ingresos netos)', 0.20, '', E24 + '; comunicado §7', PCT)
    par('lc_clp', 'Monto máximo de la línea de crédito', 50000000, 'CLP', E24, ENT)
    par('pct_propio', 'Financiamiento propio', 0.20, '', E24, PCT)
    par('pct_banco', 'Financiamiento bancario', 0.80, '', E24, PCT)
    par('iva', 'IVA (informativo, el modelo va sin IVA)', 0.19, '', E24, PCT)
    par('horizonte', 'Horizonte de evaluación', N_MESES, 'meses', E24 + '; Art. 17', ENT)
    seccion('Calendario y unidades')
    par('hh_mes', 'Horas por persona al mes', 160, 'HH', 'T-15: persona equivalente = 160 HH', ENT)
    par('hh_dia', 'Horas por día de trabajo', 8, 'HH', 'Plantilla del profesor: 8 horas por día', ENT)
    par('meses_anio', 'Meses por año', 12, 'meses', 'Conversión de tasas y primas anuales', ENT)
    par('mes_uno', 'Mes de inicio del contrato', 1, 'mes', 'Art. 17: M1 = 7 de enero de 2027', ENT)
    par('ini_op', 'Mes de inicio de la operación', 21, 'mes', 'Art. 17; E-25: 36 pagos, meses 21 a 56', ENT)
    par('meses_op', 'Meses de operación', 36, 'meses', 'Art. 17', ENT)
    par('desfase', 'Desfase del cobro de cada hito', 0, 'meses', 'Supuesto del equipo: el hito se cobra en su mes del E-25', ENT)
    seccion('Decisiones del equipo')
    par('rent_obj', 'Rentabilidad objetivo del proyecto', 0.18, '', 'Decisión del equipo (2026-11-11), bajo el tope de 20 %', PCT)
    par('tasa_soc_a', 'Tasa exigida por los socios', 0.18, 'anual', 'Decisión del equipo (2026-11-11), menor que 20 %', PCT)
    par('tasa_soc_m', 'Tasa de los socios, mensual', f"=(1+{'$B$' + str(fila[0])})^(1/{P['_meses_anio']})-1", 'mensual', 'Comunicado, nota §3: (1+i)^(1/12)−1', '0.0000%', True)
    par('wacc_m', 'Tasa de descuento ponderada', f"={P['_pct_banco']}*{P['_tasa_cred']}+{P['_pct_propio']}*{P['_tasa_soc_m']}", 'mensual', 'Comunicado §8: deuda y capital propio, antes de impuestos', '0.0000%', True)
    par('wacc_a', 'Tasa de descuento ponderada, anual', f"=(1+{P['_wacc_m']})^{P['_meses_anio']}-1", 'anual', 'Debe ser menor que 20 %', PCT, True)
    par('pago_ant', 'Pago de equipos: anticipo al ordenar', 0.30, '', 'Supuesto del equipo: condiciones de pago habituales de hardware; confirmar con cada proveedor', PCT)
    par('pago_ent', 'Pago de equipos: contra entrega', 0.60, '', 'Supuesto del equipo; el mes de entrega sale de calendario-compras.md', PCT)
    par('pago_ins', 'Pago de equipos: contra instalación', 0.10, '', 'Supuesto del equipo; el mes de instalación sale de calendario-compras.md', PCT)
    par('suma_pago', 'Suma de los tramos de pago de equipos (debe ser 100 %)', f"={P['_pago_ant']}+{P['_pago_ent']}+{P['_pago_ins']}", '', 'Control', PCT, True)
    par('cuotas', 'Cuotas del crédito', 36, 'meses', 'Supuesto del equipo: se paga con las mensualidades de la operación', ENT)
    par('ini_amort', 'Mes de la primera cuota del crédito', 21, 'mes', 'Supuesto del equipo: período de gracia durante la implementación, pagando solo intereses', ENT)
    par('imp_on', 'Incluir impuesto a la renta en el flujo (1 = sí, 0 = no)', 0, '', 'Pendiente de consulta al profesor; la rentabilidad del E-24 se mide sin impuestos', ENT)
    par('imp', 'Impuesto a la renta', 0.27, '', 'Tasa general de primera categoría', PCT)
    seccion('Supuestos de costo (sin respaldo de cotización)')
    SUP = 'Supuesto del equipo, por confirmar con cotización'
    par('reten', 'Valor de la unidad de retén (12 h de disponibilidad)', 0.5, 'UF', SUP, NUM)
    par('cont_hh', 'Contingencia de riesgos', 3688, 'HH', 'SD-07 §7.3.3 y T-15; separada del margen', ENT)
    par('overhead', 'Overhead de la empresa sobre el costo de personas', 0.05, '', SUP + ' (gerencia, administración, contabilidad y legal; E-21, 2.1)', PCT)
    par('com_boleta', 'Comisión bancaria anual de las boletas de garantía', 0.015, 'anual', SUP, PCT)
    par('prima_rc', 'Prima anual de responsabilidad civil sobre la suma asegurada', 0.006, 'anual', SUP, PCT)
    par('prima_ciber', 'Prima anual de ciberriesgo sobre la suma asegurada', 0.012, 'anual', SUP, PCT)
    par('prima_eq', 'Prima anual de todo riesgo sobre el valor de los equipos', 0.004, 'anual', SUP, PCT)
    par('tasa_acc', 'Seguro de accidentes del trabajo sobre el costo de personas', 0.0093, '', 'Cotización básica de la Ley 16.744 (0,93 %)', PCT)
    par('notaria', 'Gastos notariales y de contratación', 800000, 'CLP', SUP + ' (Art. 68.3)', ENT)
    par('custodia', 'Custodia de fuentes ante un tercero', 60, 'UF al año', SUP + ' (Art. 84.6)', NUM)
    seccion('Garantías y seguros (Bases)')
    par('g_ser', 'Garantía de seriedad de la oferta', 500000, 'USD', 'Art. 35 (folio 23)', ENT)
    par('g_ser_m', 'Vigencia de la garantía de seriedad', 5, 'meses', 'Art. 35.3: mínimo 150 días corridos', ENT)
    par('g_fc', 'Garantía de fiel cumplimiento', 1000000, 'USD', 'Art. 36 (folio 23)', ENT)
    par('g_post', 'Meses de vigencia posteriores al contrato (fiel cumplimiento y ciberriesgo)', 12, 'meses', 'Art. 36 y Art. 38', ENT)
    par('g_cf', 'Garantía de correcto funcionamiento sobre la implementación', 0.05, '', 'Art. 37 (folio 24)', PCT)
    par('g_cf_m', 'Vigencia de la garantía de correcto funcionamiento', 24, 'meses', 'Art. 37', ENT)
    par('s_rc', 'Suma asegurada de responsabilidad civil', 20000, 'UF', 'Art. 38 (folio 24)', ENT)
    par('s_ciber', 'Suma asegurada de ciberriesgo', 20000, 'UF', 'Art. 38 (folio 24)', ENT)
    seccion('Nube')
    par('nube_full', 'Mes desde el que la nube opera a tamaño completo', 13, 'mes', 'calendario-compras.md: encendida a tamaño completo desde M13', ENT)
    # hitos
    seccion('Hitos de pago (Formulario E-25, folio 74)')
    fila[0] += 1; hp.cab(fila[0], ['Hito', 'Mes', '% de la implementación', 'Evidencia'])
    HITOS = []
    for r in leer('Hitos_contractuales.csv', ',')[1:]:
        fila[0] += 1; k = fila[0]
        hp.set(f'A{k}', r[0]); hp.entrada(f'B{k}', int(r[2]), ENT); hp.entrada(f'C{k}', int(r[3]) / 100, PCT); hp.set(f'D{k}', r[6])
        HITOS.append((r[0], f'{PR}$B${k}', f'{PR}$C${k}'))
    fila[0] += 1; hp.set(f'A{fila[0]}', 'Suma de porcentajes', F_NEG)
    hp.set(f'C{fila[0]}', f'=SUM(C{fila[0] - 12}:C{fila[0] - 1})', F_NEG, PCT); P['suma_hitos'] = f'{PR}$C${fila[0]}'
    for c, w in zip('ABCD', (62, 16, 12, 90)):
        hp.ws.column_dimensions[c].width = w

    # ------------------------------------------------------------------ DOTACIÓN (HH por perfil y mes)
    M = leer('HH_matriz_perfiles_E26_M1_M56.csv')
    PERF = [(r[0], num(r[1]), num(r[2]), num(r[3]), num(r[4]), [num(x) for x in r[5:5 + N_MESES]]) for r in M[1:]]
    nP = len(PERF); F0 = 5; FT = F0 + nP          # filas de perfiles F0..FT-1; total en FT
    hd = Hoja(wb, 'DOTACIÓN', 'Dotación: horas por perfil del E-26 y por mes (dato de entrada)')
    hd.set('A2', 'Fuente: HH_matriz_perfiles_E26_M1_M56.csv (red del cronograma estabilizada; SD-07 y T-15)')
    hd.meses(fila_fecha=3, fila_mes=4)
    for i, p in enumerate(PERF):
        r = F0 + i; hd.set(f'A{r}', p[0])
        for m in range(1, N_MESES + 1):
            hd.entrada(f'{mc(m)}{r}', p[5][m - 1], NUM)
        hd.set(f'B{r}', f'=SUM({C1}{r}:{CN}{r})', F_NEG, NUM, R_TOT)
    hd.fila_mensual(FT, 'Total de HH', lambda m, c: f'=SUM({c}{F0}:{c}{FT - 1})', font=F_NEG, fill=R_TOT)
    hd.anchos(); hd.ws.freeze_panes = 'C5'
    DOT = q('DOTACIÓN')

    # ------------------------------------------------------------------ Costos HH - Sueldos (tarifas por perfil)
    CO = q('COSTOS'); FI, FO = 20, 21        # filas de banderas de fase en COSTOS
    flagI = lambda c: f'{CO}{c}${FI}'; flagO = lambda c: f'{CO}{c}${FO}'
    rngI = f'{CO}${C1}${FI}:${CN}${FI}'; rngO = f'{CO}${C1}${FO}:${CN}${FO}'
    SU = 'Costos HH - Sueldos'
    hs = Hoja(wb, SU, 'Costo y tarifa por perfil (Formulario E-26)',
              'Costo = punto medio del rango. Tarifa = mayor entre costo ÷ (1 − rentabilidad objetivo) y el mínimo del E-26, sin pasar el máximo.')
    hs.cab(4, ['Perfil E-26', 'Costo mín UF/h', 'Costo máx UF/h', 'Tarifa mín UF/h', 'Tarifa máx UF/h', 'Costo UF/h', 'Tarifa UF/h',
               'Margen sobre tarifa', 'Control del rango', 'Costo mensual UF (por persona)', 'Tarifa mensual UF (por persona)', 'HH del proyecto',
               'Personas (pico del proyecto)', 'Personas (pico en implementación)', 'Personas (pico en operación)', 'Meses con trabajo',
               'Horas por persona', 'Días según Gantt (horas por persona ÷ horas por día)', 'Costo total UF', 'Tarifa total UF'])
    for i, p in enumerate(PERF):
        r = F0 + i; hs.set(f'A{r}', p[0])
        for c, v in zip('BCDE', p[1:5]):
            hs.entrada(f'{c}{r}', v, NUM)
        hs.set(f'F{r}', f'=AVERAGE(B{r}:C{r})', fmt='0.000')
        hs.set(f'G{r}', f"=MIN(MAX(F{r}/(1-{P['rent_obj']}),D{r}),E{r})", fmt='0.000')
        hs.set(f'H{r}', f'=(G{r}-F{r})/G{r}', fmt=PCT)
        hs.set(f'I{r}', f'=IF(AND(F{r}>=B{r},F{r}<=C{r},G{r}>=D{r},G{r}<=E{r}),"Dentro del rango","Fuera del rango")')
        hs.set(f'J{r}', f"=F{r}*{P['hh_mes']}", fmt=NUM); hs.set(f'K{r}', f"=G{r}*{P['hh_mes']}", fmt=NUM)
        hs.set(f'L{r}', f'={DOT}B{r}', fmt=NUM)
        pm = f"{q('Costos HH por MES')}${C1}{r}:${CN}{r}"
        hs.set(f'M{r}', f'=ROUNDUP(MAX({pm}),0)', fmt=ENT)
        hs.set(f'N{r}', f'=ROUNDUP(SUMPRODUCT(MAX({pm}*{rngI})),0)', fmt=ENT)
        hs.set(f'O{r}', f'=ROUNDUP(SUMPRODUCT(MAX({pm}*{rngO})),0)', fmt=ENT)
        hs.set(f'P{r}', f'=COUNTIF({pm},">0")', fmt=ENT)
        hs.set(f'Q{r}', f'=IF(M{r}>0,L{r}/M{r},0)', fmt=NUM)
        hs.set(f'R{r}', f"=Q{r}/{P['hh_dia']}", fmt=NUM)
        hs.set(f'S{r}', f'=L{r}*F{r}', fmt=NUM); hs.set(f'T{r}', f'=L{r}*G{r}', fmt=NUM)
    hs.set(f'A{FT}', 'Total', F_NEG, fill=R_TOT)
    for c in 'LST':
        hs.set(f'{c}{FT}', f'=SUM({c}{F0}:{c}{FT - 1})', F_NEG, NUM, R_TOT)
    hs.set(f'A{FT + 3}', 'Las personas son el pico de personas equivalentes (HH ÷ horas por persona al mes, redondeado hacia arriba) de la hoja Costos HH por MES.')
    hs.set(f'A{FT + 5}', 'Los picos de cada perfil ocurren en meses distintos, por eso no se suman. En operación, las 26 personas son 21 de TIC, 2 de L2, 2 de L3 y 1 gerente; los demás perfiles aparecen por trabajos puntuales.')
    hs.set(f'A{FT + 4}', 'Los días según Gantt son las horas del perfil divididas por sus personas del pico y por las horas de un día de trabajo.')
    hs.set(f'A{FT + 2}', 'Fuente de los rangos: Formulario E-26 (folio 76) y equivalencias_roles_E26.csv.')
    hs.ws.column_dimensions['A'].width = 44
    for c in 'BCDEFGHIJKLMNOPQRST':
        hs.ws.column_dimensions[c].width = 16
    SUR = q(SU)

    # ------------------------------------------------------------------ Costos HH por MES (personas equivalentes)
    hf = Hoja(wb, 'Costos HH por MES', 'Personas equivalentes por perfil y mes (HH ÷ horas por persona al mes)')
    hf.meses(fila_fecha=3, fila_mes=4)
    for i, p in enumerate(PERF):
        hf.fila_mensual(F0 + i, p[0], lambda m, c, r=F0 + i: f"={DOT}{c}{r}/{P['hh_mes']}", total=False)
        hf.set(f'B{F0 + i}', f'=MAX({C1}{F0 + i}:{CN}{F0 + i})', F_NEG, NUM, R_TOT)
    hf.fila_mensual(FT, 'Total de personas equivalentes', lambda m, c: f'=SUM({c}{F0}:{c}{FT - 1})', total=False, font=F_NEG, fill=R_TOT)
    hf.set(f'B{FT}', f'=MAX({C1}{FT}:{CN}{FT})', F_NEG, NUM, R_TOT); hf.set('B4', 'Máximo', F_CAB, fill=R_CAB)
    hf.anchos(); hf.ws.freeze_panes = 'C5'

    # ------------------------------------------------------------------ COSTOS (resumen mensual) — se define antes para las banderas

    # ------------------------------------------------------------------ COSTOS DE OPERACION / TARIFAS DE OPERACION (personas)
    G = collections.defaultdict(float)
    for r in leer('Guardias_mes_rol.csv')[1:]:
        G[int(r[0][1:])] += num(r[2])
    i_form = next(i for i, p in enumerate(PERF) if 'Formador' in p[0])
    def hoja_personas(nombre, titulo, col_tar, es_tarifa):
        h = Hoja(wb, nombre, titulo)
        h.meses(fila_fecha=3, fila_mes=4)
        for i, p in enumerate(PERF):
            h.fila_mensual(F0 + i, p[0], lambda m, c, r=F0 + i: f'={DOT}{c}{r}*{SUR}${col_tar}{r}')
        h.fila_mensual(FT, 'Subtotal de personas (UF)', lambda m, c: f'=SUM({c}{F0}:{c}{FT - 1})', font=F_NEG, fill=R_TOT)
        if not es_tarifa:
            h.set(f'A{FT + 1}', 'Retén: unidades de 12 h (dato de entrada, Guardias_mes_rol.csv)')
            for m in range(1, N_MESES + 1):
                h.entrada(f'{mc(m)}{FT + 1}', G.get(m, 0), ENT)
            h.set(f'B{FT + 1}', f'=SUM({C1}{FT + 1}:{CN}{FT + 1})', F_NEG, ENT, R_TOT)
            h.fila_mensual(FT + 2, 'Retén (UF)', lambda m, c: f"={c}{FT + 1}*{P['reten']}")
        else:
            h.fila_mensual(FT + 2, 'Retén (UF), con el factor de los demás componentes',
                           lambda m, c: f"={q('COSTOS DE OPERACION')}{c}{FT + 2}*{CO}$B$34")
        h.fila_mensual(FT + 3, 'Total de personas y retén (UF)', lambda m, c: f'={c}{FT}+{c}{FT + 2}', font=F_NEG, fill=R_TOT)
        b = FT + 5
        h.set(f'A{b}', 'Personas en implementación (UF)', F_NEG); h.set(f'B{b}', f'=SUMPRODUCT({C1}{FT}:{CN}{FT},{rngI})', F_NEG, NUM)
        h.set(f'A{b + 1}', 'Personas en operación (UF)', F_NEG); h.set(f'B{b + 1}', f'=SUMPRODUCT({C1}{FT}:{CN}{FT},{rngO})', F_NEG, NUM)
        h.set(f'A{b + 2}', 'De ello, formadores en implementación (capacitaciones)', F_NEG)
        h.set(f'B{b + 2}', f'=SUMPRODUCT({C1}{F0 + i_form}:{CN}{F0 + i_form},{rngI})', F_NEG, NUM)
        h.anchos(); h.ws.freeze_panes = 'C5'
        return b
    bP = hoja_personas('COSTOS DE OPERACION', 'Costo de personas por perfil y mes (UF) = HH × costo UF/h', 'F', False)
    hoja_personas('TARIFAS DE OPERACION', 'Tarifa de personas por perfil y mes (UF) = HH × tarifa UF/h', 'G', True)
    CP = q('COSTOS DE OPERACION'); TP = q('TARIFAS DE OPERACION')

    # ------------------------------------------------------------------ ADQUISICIONES
    ha = Hoja(wb, 'ADQUISICIONES', 'Adquisiciones del proponente: equipos, nube y licencias (precios de referencia, sin cotización)',
              'Cada partida: precio público de referencia con su fuente. Tipo «Única» se paga en su mes de inicio; «Mensual», desde el mes de inicio hasta el de fin.')
    gc = lambda m: L(22 + m)          # W..BZ
    CABA = ['Categoría', 'Partida', 'Descripción', 'Proveedor de referencia', 'Moneda', 'Precio unitario', 'Unidad del precio',
            'Unidades por mes o por compra', 'Cantidad', 'N° de sitios', 'Tipo', 'Mes de inicio', 'Mes de fin',
            'Proporción antes de la nube completa', 'Precio unitario UF', 'Cantidad total', 'Costo UF (único o mensual)',
            'Fuente', 'Nota', 'Total del horizonte UF', 'Mes de entrega (pago contra entrega)', 'Mes de instalación (pago contra instalación)']
    ha.cab(4, CABA)
    for m in range(1, N_MESES + 1):
        ha.set(f'{gc(m)}4', m, F_CAB, ENT, R_CAB); ha.ws.column_dimensions[gc(m)].width = 10
    A0 = 5; fila_item = {}
    for k, it in enumerate(ITEMS):
        r = A0 + k; fila_item[it['clave']] = r
        ha.set(f'A{r}', it['cat']); ha.set(f'B{r}', it['partida']); ha.set(f'C{r}', it['desc']); ha.set(f'D{r}', it['prov'])
        ha.entrada(f'E{r}', it['mon']); ha.entrada(f'F{r}', it['precio'], '#,##0.0000'); ha.set(f'G{r}', it['unidad'])
        ha.entrada(f'H{r}', it.get('mult', 1), NUM); ha.entrada(f'I{r}', it['cant'], NUM); ha.entrada(f'J{r}', it.get('sitios', 1), ENT)
        ha.entrada(f'K{r}', it['tipo']); ha.entrada(f'L{r}', it['ini'], ENT); ha.entrada(f'M{r}', it.get('fin', it['ini']), ENT)
        ha.entrada(f'N{r}', it.get('prop', 1), PCT)
        ha.set(f'O{r}', f"=IF(E{r}=\"USD\",F{r}*{P['usd']}/{P['uf']},IF(E{r}=\"EUR\",F{r}*{P['eur']}/{P['uf']},IF(E{r}=\"CLP\",F{r}/{P['uf']},F{r})))", fmt='#,##0.0000')
        ha.set(f'P{r}', f'=H{r}*I{r}*J{r}', fmt=NUM); ha.set(f'Q{r}', f'=O{r}*P{r}', fmt=NUM)
        ha.set(f'R{r}', it['fuente']); ha.set(f'S{r}', it.get('nota', ''))
        ha.set(f'T{r}', f'=SUM({gc(1)}{r}:{gc(N_MESES)}{r})', F_NEG, NUM, R_TOT)
        ha.entrada(f'U{r}', it.get('ent', it['ini']), ENT); ha.entrada(f'V{r}', it.get('inst', it['ini']), ENT)
        for m in range(1, N_MESES + 1):
            c = gc(m)
            ha.set(f'{c}{r}', f"=N($K{r}=\"Única\")*$Q{r}*(N({c}$4=$L{r})*{P['pago_ant']}+N({c}$4=$U{r})*{P['pago_ent']}+N({c}$4=$V{r})*{P['pago_ins']})+N($K{r}=\"Mensual\")*N({c}$4>=$L{r})*N({c}$4<=$M{r})*$Q{r}"
                              f"*(N({c}$4<{P['nube_full']})*$N{r}+N({c}$4>={P['nube_full']}))", fmt=NUM)
    A1_ = A0 + len(ITEMS) - 1
    CATS = ['Equipos de tienda', 'Equipos de centros de distribución', 'Equipos de DC-01', 'Innovaciones', 'Nube', 'Licencias y seguridad']
    rc = A1_ + 3; ha.set(f'A{rc - 1}', 'Totales por categoría (UF por mes)', F_NEG, fill=R_TOT); fila_cat = {}
    for k, cat in enumerate(CATS):
        r = rc + k; fila_cat[cat] = r; ha.set(f'A{r}', cat, F_NEG)
        for m in range(1, N_MESES + 1):
            c = gc(m); ha.set(f'{c}{r}', f'=SUMIF($A${A0}:$A${A1_},$A{r},{c}${A0}:{c}${A1_})', fmt=NUM)
        ha.set(f'T{r}', f'=SUM({gc(1)}{r}:{gc(N_MESES)}{r})', F_NEG, NUM, R_TOT)
    r_eq = rc + len(CATS) + 1; r_eqac = r_eq + 1
    ha.set(f'A{r_eq}', 'Equipos comprados en el mes (tienda, centros, DC-01 e innovaciones)', F_NEG)
    ha.set(f'A{r_eqac}', 'Equipos comprados, acumulado', F_NEG)
    for m in range(1, N_MESES + 1):
        c = gc(m)
        ha.set(f'{c}{r_eq}', f'=SUM({c}{rc}:{c}{rc + 3})', fmt=NUM)
        ha.set(f'{c}{r_eqac}', f'={c}{r_eq}' if m == 1 else f'={gc(m - 1)}{r_eqac}+{c}{r_eq}', fmt=NUM)
    for c, w in zip('ABCDEFGHIJKLMNOPQRSTUV', (26, 30, 46, 22, 9, 13, 16, 12, 10, 9, 10, 8, 8, 12, 12, 12, 14, 50, 50, 14, 14, 14)):
        ha.ws.column_dimensions[c].width = w
    ha.ws.freeze_panes = 'C5'
    AD = q('ADQUISICIONES')

    # ------------------------------------------------------------------ PROVEEDORES (T-22)
    hv = Hoja(wb, 'PROVEEDORES', 'Proveedores y precios de referencia (Formulario T-22)')
    hv.cab(3, ['Proveedor', 'Producto o servicio', 'Tipo de costo', 'Moneda', 'Precio unitario neto', 'Cantidad', 'Precio unitario USD',
               'Costo CLP (único o mensual)', 'Costo UF (único o mensual)', 'Costo del horizonte UF', 'Fuente'])
    for k in range(len(ITEMS)):
        r, a = 4 + k, A0 + k
        hv.set(f'A{r}', f'={AD}D{a}'); hv.set(f'B{r}', f'={AD}C{a}'); hv.set(f'C{r}', f'={AD}K{a}'); hv.set(f'D{r}', f'={AD}E{a}')
        hv.set(f'E{r}', f'={AD}F{a}', fmt='#,##0.0000'); hv.set(f'F{r}', f'={AD}P{a}', fmt=NUM)
        hv.set(f'G{r}', f"={AD}O{a}*{P['uf']}/{P['usd']}", fmt='#,##0.0000')
        hv.set(f'I{r}', f'={AD}Q{a}', fmt=NUM); hv.set(f'H{r}', f"=I{r}*{P['uf']}", fmt=ENT)
        hv.set(f'J{r}', f'={AD}T{a}', fmt=NUM); hv.set(f'K{r}', f'={AD}R{a}')
    rt = 4 + len(ITEMS); hv.set(f'A{rt}', 'Total', F_NEG, fill=R_TOT); hv.set(f'J{rt}', f'=SUM(J4:J{rt - 1})', F_NEG, NUM, R_TOT)
    for c, w in zip('ABCDEFGHIJK', (24, 50, 12, 9, 14, 12, 14, 18, 16, 16, 60)):
        hv.ws.column_dimensions[c].width = w

    # ------------------------------------------------------------------ GASTOS ADMINISTRATIVOS
    GA = q('GASTOS ADMINISTRATIVOS')
    hg = Hoja(wb, 'GASTOS ADMINISTRATIVOS', 'Gastos administrativos por mes (UF)',
              'Comunicado §6. Los intereses del financiamiento no van aquí: están en FINANCIAMIENTO.')
    hg.meses(fila_fecha=3, fila_mes=4)
    ult = lambda c: f"N({c}$4={P['horizonte']})"
    com_m = f"{P['com_boleta']}/{P['meses_anio']}"
    uf_usd = f"{P['usd']}/{P['uf']}"
    BASE_CF = "$B$20"
    filas_g = [
        ('Overhead de la empresa', lambda m, c: f"={CP}{c}{FT}*{P['overhead']}",
         'Porcentaje de overhead sobre el costo de personas del mes.', 'Comunicado §6; E-21, 2.1'),
        ('Garantía de seriedad de la oferta', lambda m, c: f"=N({c}$4={P['mes_uno']})*{P['g_ser']}*{uf_usd}*{com_m}*{P['g_ser_m']}",
         'Monto × comisión bancaria mensual × meses de vigencia, cargado al mes de inicio.', 'Art. 35'),
        ('Garantía de fiel cumplimiento', lambda m, c: f"={P['g_fc']}*{uf_usd}*{com_m}*(1+{ult(c)}*{P['g_post']})",
         'Monto × comisión mensual durante el contrato; los meses posteriores se cargan al último mes.', 'Art. 36'),
        ('Garantía de correcto funcionamiento', lambda m, c: f"=N({c}$4>={P['ini_op']})*N({c}$4<{P['ini_op']}+{P['g_cf_m']})*{P['g_cf']}*{BASE_CF}*{com_m}",
         'Porcentaje del valor de la implementación × comisión mensual, por su vigencia desde el inicio de la operación. '
         'Base: costo directo de implementación ÷ (1 − rentabilidad objetivo), para no depender del precio final.', 'Art. 37'),
        ('Seguro de responsabilidad civil', lambda m, c: f"={P['s_rc']}*{P['prima_rc']}/{P['meses_anio']}",
         'Suma asegurada × prima anual ÷ meses por año.', 'Art. 38'),
        ('Seguro de ciberriesgo y datos', lambda m, c: f"={P['s_ciber']}*{P['prima_ciber']}/{P['meses_anio']}*(1+{ult(c)}*{P['g_post']})",
         'Suma asegurada × prima anual ÷ meses por año; los 12 meses posteriores se cargan al último mes.', 'Art. 38'),
        ('Seguro de todo riesgo de equipos', lambda m, c: f"={flagI(c)}*{AD}{gc(m)}{r_eqac}*{P['prima_eq']}/{P['meses_anio']}",
         'Valor acumulado de los equipos comprados × prima anual ÷ meses por año, hasta la entrega final.', 'Art. 38'),
        ('Seguro de accidentes del trabajo', lambda m, c: f"={CP}{c}{FT}*{P['tasa_acc']}",
         'Tasa legal sobre el costo de personas del mes.', 'Art. 38; Ley 16.744'),
        ('Gastos notariales y de contratación', lambda m, c: f"=N({c}$4={P['mes_uno']})*{P['notaria']}/{P['uf']}",
         'Monto único al firmar el contrato.', 'Art. 68.3'),
        ('Custodia de fuentes ante terceros', lambda m, c: f"={P['custodia']}/{P['meses_anio']}",
         'Tarifa anual del depósito ÷ meses por año.', 'Art. 84.6'),
    ]
    for k, (rot, f, _, _) in enumerate(filas_g):
        hg.fila_mensual(5 + k, rot, f)
    rg = 5 + len(filas_g)
    hg.fila_mensual(rg, 'Total de gastos administrativos', lambda m, c: f'=SUM({c}5:{c}{rg - 1})', font=F_NEG, fill=R_TOT)
    hg.set('A20', 'Base de la garantía de correcto funcionamiento (UF)', F_NEG)
    hg.set('B20', f"={CO}$B$27/(1-{P['rent_obj']})", F_NEG, NUM)
    hg.cab(22, ['Gasto', 'Criterio de cálculo', 'Fuente'])
    for k, (rot, _, crit, fu) in enumerate(filas_g):
        hg.set(f'A{23 + k}', rot); hg.set(f'B{23 + k}', crit); hg.set(f'C{23 + k}', fu)
    hg.anchos(); hg.ws.freeze_panes = 'C5'

    # ------------------------------------------------------------------ COSTOS
    hc = Hoja(wb, 'COSTOS', 'Costos y venta por componente y por mes (UF)')
    hc.meses(fila_fecha=3, fila_mes=4)
    comp = [
        ('Personas (HH por perfil)', lambda m, c: f'={CP}{c}{FT}'),
        ('Retén', lambda m, c: f'={CP}{c}{FT + 2}'),
        ('Equipos de tiendas, centros y DC-01', lambda m, c: f"={AD}{gc(m)}{fila_cat['Equipos de tienda']}+{AD}{gc(m)}{fila_cat['Equipos de centros de distribución']}+{AD}{gc(m)}{fila_cat['Equipos de DC-01']}"),
        ('Equipos de las innovaciones', lambda m, c: f"={AD}{gc(m)}{fila_cat['Innovaciones']}"),
        ('Nube', lambda m, c: f"={AD}{gc(m)}{fila_cat['Nube']}"),
        ('Licencias y seguridad', lambda m, c: f"={AD}{gc(m)}{fila_cat['Licencias y seguridad']}"),
        ('Gastos administrativos', lambda m, c: f'={GA}{c}{rg}'),
        ('Contingencia de riesgos', lambda m, c: f'={flagI(c)}*$B$30*{c}6/$B$29'),
    ]
    for k, (rot, f) in enumerate(comp):
        hc.fila_mensual(6 + k, rot, f)
    hc.set('A5', 'Costos', F_NEG, fill=R_TOT)
    hc.fila_mensual(14, 'Total de costos', lambda m, c: f'=SUM({c}6:{c}13)', font=F_NEG, fill=R_TOT)
    hc.set('A16', 'Venta (devengada)', F_NEG, fill=R_TOT)
    hc.fila_mensual(17, 'Personas, a tarifa', lambda m, c: f'={TP}{c}{FT}')
    hc.fila_mensual(18, 'Demás componentes, con su factor', lambda m, c: f'=({c}14-{c}6)*$B$34')
    hc.fila_mensual(19, 'Total de venta', lambda m, c: f'={c}17+{c}18', font=F_NEG, fill=R_TOT)
    hc.fila_mensual(FI, 'Mes de implementación (1 = sí)', lambda m, c: f"=N({c}$4<{P['ini_op']})", fmt=ENT, total=False)
    hc.fila_mensual(FO, 'Mes de operación (1 = sí)', lambda m, c: f"=N({c}$4>={P['ini_op']})", fmt=ENT, total=False)
    R = f'{C1}{{0}}:{CN}{{0}}'.format
    filas_res = [
        (24, 'Costo de la implementación (UF)', f'=SUMPRODUCT({R(14)},{R(FI)})'),
        (25, 'Costo de la operación (UF)', f'=SUMPRODUCT({R(14)},{R(FO)})'),
        (26, 'Costo total (UF)', '=B24+B25'),
        (27, 'Costo directo de la implementación, sin gastos administrativos ni contingencia (UF)', f'=SUMPRODUCT({R(6)}+{R(7)}+{R(8)}+{R(9)}+{R(10)}+{R(11)},{R(FI)})'),
        (28, 'HH de implementación', f'=SUMPRODUCT({DOT}{R(FT)},{R(FI)})'),
        (29, 'Costo de personas en implementación (UF)', f'=SUMPRODUCT({R(6)},{R(FI)})'),
        (30, 'Contingencia valorizada (UF) = HH de contingencia × costo medio de la HH', f"={P['cont_hh']}*B29/B28"),
        (32, 'Venta de personas, a tarifa (UF)', '=B17'),
        (33, 'Venta total que da la rentabilidad objetivo (UF) = costo total ÷ (1 − rentabilidad)', f"=B26/(1-{P['rent_obj']})"),
        (34, 'Factor de los demás componentes = (venta total − venta de personas) ÷ sus costos', '=(B33-B32)/(B14-B6)'),
        (36, 'Precio de la implementación (UF)', f'=SUMPRODUCT({R(19)},{R(FI)})'),
        (37, 'Precio de la operación (UF)', f'=SUMPRODUCT({R(19)},{R(FO)})'),
        (38, 'Mensualidad de la operación (UF)', f"=B37/{P['meses_op']}"),
        (40, 'Adquisiciones de la implementación (UF)', f'=SUMPRODUCT({R(8)}+{R(9)},{R(FI)})'),
        (41, 'Servicios de la implementación: retén, nube, licencias, gastos administrativos y contingencia (UF)', f'=SUMPRODUCT({R(7)}+{R(10)}+{R(11)}+{R(12)}+{R(13)},{R(FI)})'),
        (42, 'Servicios de la operación: todo lo que no es personas (UF)', f'=SUMPRODUCT({R(14)}-{R(6)},{R(FO)})'),
    ]
    for r, rot, f in filas_res:
        hc.set(f'A{r}', rot, F_NEG); hc.set(f'B{r}', f, F_NEG, '0.0000' if r == 34 else NUM)
    hc.anchos(a=70); hc.ws.freeze_panes = 'C5'

    # ------------------------------------------------------------------ INGRESOS
    IN = q('INGRESOS')
    hi = Hoja(wb, 'INGRESOS', 'Ingresos por mes (UF): hitos H1–H12 del E-25 y 36 mensualidades de operación')
    hi.meses(fila_fecha=3, fila_mes=4)
    for k, (h, mes, pct) in enumerate(HITOS):
        hi.fila_mensual(5 + k, f'{h} (% del precio de implementación)', lambda m, c, mes=mes, pct=pct: f"=N({c}$4={mes}+{P['desfase']})*{pct}*{CO}$B$36")
    hi.fila_mensual(17, 'Mensualidad de la operación', lambda m, c: f"=N({c}$4>={P['ini_op']})*N({c}$4<{P['ini_op']}+{P['meses_op']})*{CO}$B$38")
    hi.fila_mensual(18, 'Total de ingresos', lambda m, c: f'=SUM({c}5:{c}17)', font=F_NEG, fill=R_TOT)
    hi.set('A20', 'Ingresos por hitos (UF)', F_NEG); hi.set('B20', '=SUM(B5:B16)', F_NEG, NUM)
    hi.set('A21', 'Ingresos por operación (UF)', F_NEG); hi.set('B21', '=B17', F_NEG, NUM)
    hi.set('A22', 'Número de mensualidades', F_NEG); hi.set('B22', f'=COUNTIF({C1}17:{CN}17,">0")', F_NEG, ENT)
    hi.anchos(); hi.ws.freeze_panes = 'C5'

    # ------------------------------------------------------------------ FLUJO DE CAJA COMPLETO (Fila A)
    FC = q('FLUJO DE CAJA COMPLETO')
    hx = Hoja(wb, 'FLUJO DE CAJA COMPLETO', 'Flujo de caja del proyecto por mes (UF) — Fila A, sin financiamiento',
              'Sin IVA. El VAN se calcula sobre el flujo del proyecto, sin crédito, cuotas ni intereses (comunicado, nota §7).')
    hx.meses(fila_fecha=3, fila_mes=4)
    hx.fila_mensual(5, 'Ingresos', lambda m, c: f'={IN}{c}18')
    for k, (rot, _) in enumerate(comp):
        hx.fila_mensual(6 + k, 'Egreso: ' + rot, lambda m, c, k=k: f'=-{CO}{c}{6 + k}')
    hx.fila_mensual(14, 'EBITDA (ingresos menos egresos)', lambda m, c: f'=SUM({c}5:{c}13)', font=F_NEG, fill=R_TOT)
    hx.fila_mensual(15, 'Impuesto a la renta (solo si está activado en Parámetros)', lambda m, c: f"=-{P['imp_on']}*{P['imp']}*MAX({c}14,0)")
    hx.fila_mensual(16, 'A. Flujo del proyecto', lambda m, c: f'={c}14+{c}15', font=F_NEG, fill=R_TOT)
    hx.fila_mensual(17, 'A. Flujo del proyecto acumulado', lambda m, c: f'={c}16' if m == 1 else f'={mc(m - 1)}17+{c}16', total=False)
    hx.fila_mensual(18, 'Factor de descuento = (1 + tasa ponderada)^mes', lambda m, c: f"=(1+{P['wacc_m']})^{c}$4", fmt='0.0000', total=False)
    hx.fila_mensual(19, 'Valor presente del flujo', lambda m, c: f'={c}16/{c}18')
    hx.fila_mensual(20, 'VAN acumulado', lambda m, c: f'={c}19' if m == 1 else f'={mc(m - 1)}20+{c}19', total=False)
    hx.fila_mensual(22, 'Año del contrato', lambda m, c: f"=ROUNDUP({c}$4/{P['meses_anio']},0)", fmt=ENT, total=False)
    hx.set('A24', 'Resumen anual (UF)', F_NEG, fill=R_TOT); hx.cab(25, ['Año', 'Ingresos', 'Egresos', 'Flujo del proyecto'])
    for a in range(1, 6):
        r = 25 + a; hx.entrada(f'A{r}', a, ENT)
        hx.set(f'B{r}', f'=SUMIF(${C1}$22:${CN}$22,$A{r},${C1}$5:${CN}$5)', fmt=NUM)
        hx.set(f'D{r}', f'=SUMIF(${C1}$22:${CN}$22,$A{r},${C1}$16:${CN}$16)', fmt=NUM)
        hx.set(f'C{r}', f'=D{r}-B{r}', fmt=NUM)
    hx.anchos(a=58); hx.ws.freeze_panes = 'C5'

    # ------------------------------------------------------------------ FINANCIAMIENTO
    FN = q('FINANCIAMIENTO')
    hn = Hoja(wb, 'FINANCIAMIENTO', 'Financiamiento: crédito bancario, aporte de los socios y línea de crédito (UF)',
              'El crédito y el aporte cubren la mayor necesidad de caja del flujo del proyecto. La línea cubre déficits transitorios hasta su tope.')
    hn.meses(fila_fecha=3, fila_mes=4)
    hn.set('A5', 'Financiamiento requerido: mayor necesidad de caja más los intereses del período de gracia (UF)', F_NEG)
    hn.set('B5', f'=MAX({C1}24:{CN}24)', F_NEG, NUM)
    hn.set('A6', 'Crédito bancario (UF)', F_NEG); hn.set('B6', f"=B5*{P['pct_banco']}", F_NEG, NUM)
    hn.set('A7', 'Aporte de los socios (UF)', F_NEG); hn.set('B7', f"=B5*{P['pct_propio']}", F_NEG, NUM)
    hn.set('A8', 'Cuota mensual del crédito (UF)', F_NEG); hn.set('B8', f"=IF(B6>0,PMT({P['tasa_cred']},{P['cuotas']},-B6),0)", F_NEG, NUM)
    hn.set('A9', 'Tope de la línea de crédito (UF)', F_NEG); hn.set('B9', f"={P['lc_clp']}/{P['uf']}", F_NEG, NUM)
    des = lambda c: f"N({c}$4={P['mes_uno']})"
    hn.fila_mensual(11, 'Desembolso del crédito', lambda m, c: f'={des(c)}*$B$6')
    hn.fila_mensual(12, 'Aporte de los socios', lambda m, c: f'={des(c)}*$B$7')
    hn.fila_mensual(13, 'Saldo inicial del crédito', lambda m, c: f'={L(1 + m)}16', total=False)
    hn.fila_mensual(14, 'Interés del crédito', lambda m, c: f"={c}13*{P['tasa_cred']}")
    hn.fila_mensual(15, 'Amortización del crédito', lambda m, c: f"=N({c}$4>={P['ini_amort']})*N({c}$4<{P['ini_amort']}+{P['cuotas']})*($B$8-{c}14)")
    hn.fila_mensual(16, 'Saldo final del crédito', lambda m, c: f'={c}13+{c}11-{c}15', total=False)
    hn.fila_mensual(18, 'Caja acumulada antes de la línea de crédito',
                    lambda m, c: (f'={FC}{c}16+{c}11+{c}12-{c}14-{c}15' if m == 1 else f'={mc(m - 1)}18+{FC}{c}16+{c}11+{c}12-{c}14-{c}15'), total=False)
    hn.fila_mensual(19, 'Saldo usado de la línea de crédito', lambda m, c: f'=MIN($B$9,MAX(0,-{c}18))', total=False)
    hn.fila_mensual(20, 'Giro neto de la línea (giro menos pago)', lambda m, c: f'={c}19' if m == 1 else f'={c}19-{mc(m - 1)}19')
    hn.fila_mensual(21, 'Interés de la línea de crédito', lambda m, c: f"={L(1 + m)}19*{P['tasa_lc']}")
    hn.fila_mensual(22, 'Déficit que la línea no alcanza a cubrir', lambda m, c: f'=MAX(0,-{c}18-{c}19)')
    hn.fila_mensual(24, 'Necesidad de caja del mes, con los intereses del período de gracia',
                    lambda m, c: f"=MAX(0,-{FC}{c}17)/(1-N({c}$4<{P['ini_amort']})*{P['pct_banco']}*{P['tasa_cred']}*({c}$4-{P['mes_uno']}))", total=False)
    hn.set('A26', 'Criterio: el crédito y el aporte se dimensionan para que la caja no sea negativa en ningún mes, contando los intereses que se pagan antes de la primera cuota.')
    hn.anchos(a=70); hn.ws.freeze_panes = 'C5'

    # ------------------------------------------------------------------ FLUJO DE CAJA NETO (Filas A, B y C)
    NE = q('FLUJO DE CAJA NETO')
    hz = Hoja(wb, 'FLUJO DE CAJA NETO', 'Flujo de caja por mes (UF): A proyecto, B financiamiento, C neto',
              'El crédito no es ingreso del proyecto: entra y sale por la Fila B (comunicado, nota §5).')
    hz.meses(fila_fecha=3, fila_mes=4)
    hz.fila_mensual(5, 'A. Flujo del proyecto', lambda m, c: f'={FC}{c}16', font=F_NEG, fill=R_TOT)
    hz.fila_mensual(7, 'Aporte de los socios', lambda m, c: f'={FN}{c}12')
    hz.fila_mensual(8, 'Desembolso del crédito', lambda m, c: f'={FN}{c}11')
    hz.fila_mensual(9, 'Interés del crédito', lambda m, c: f'=-{FN}{c}14')
    hz.fila_mensual(10, 'Amortización del crédito', lambda m, c: f'=-{FN}{c}15')
    hz.fila_mensual(11, 'Giro neto de la línea de crédito', lambda m, c: f'={FN}{c}20')
    hz.fila_mensual(12, 'Interés de la línea de crédito', lambda m, c: f'=-{FN}{c}21')
    hz.fila_mensual(13, 'B. Flujo del financiamiento', lambda m, c: f'=SUM({c}7:{c}12)', font=F_NEG, fill=R_TOT)
    hz.fila_mensual(15, 'C. Flujo neto (A + B)', lambda m, c: f'={c}5+{c}13', font=F_NEG, fill=R_TOT)
    hz.fila_mensual(16, 'C. Saldo de caja acumulado', lambda m, c: f'={c}15' if m == 1 else f'={mc(m - 1)}16+{c}15', total=False)
    hz.anchos(a=44); hz.ws.freeze_panes = 'C5'

    # ------------------------------------------------------------------ CURVA S
    # Gráfico 1: línea base de costos de la implementación (costo de cada actividad repartido en los meses que dura, acumulado).
    # Gráfico 2: las tres series del comunicado (nota §6) en los 56 meses, sobre el flujo de caja.
    hk = Hoja(wb, 'CURVA S', 'Curva S: línea base de costos de la implementación y flujo acumulado del contrato (UF)',
              'Curva S = costo de cada actividad repartido en los meses que dura y acumulado. La operación es un servicio continuo de costo mensual parejo: acumula en línea recta y se muestra en el segundo gráfico.')
    hk.set('A30', 'Datos de las curvas (UF)', F_NEG, fill=R_TOT)
    hk.meses(fila_fecha=31, fila_mes=32, total_col=None)
    hk.fila_mensual(33, 'Ingresos acumulados', lambda m, c: f'={IN}{c}18' if m == 1 else f'={mc(m - 1)}33+{IN}{c}18', total=False)
    hk.fila_mensual(34, 'Costos acumulados (pagados, más intereses)', lambda m, c: f'={c}36' if m == 1 else f'={mc(m - 1)}34+{c}36', total=False)
    hk.fila_mensual(35, 'Saldo de caja acumulado (Fila C)', lambda m, c: f'={NE}{c}16', total=False)
    hk.fila_mensual(36, 'Costos pagados en el mes: directos más intereses del crédito y de la línea', lambda m, c: f'={CO}{c}14+{FN}{c}14+{FN}{c}21', total=False)
    rI = f'{AD}$K${A0}:$K${A1_}'; rO = f'{AD}$L${A0}:$L${A1_}'; rV = f'{AD}$V${A0}:$V${A1_}'; rQ = f'{AD}$Q${A0}:$Q${A1_}'
    hk.fila_mensual(37, 'Equipos devengados: cada compra repartida entre su mes de orden y su mes de instalación',
                    lambda m, c: f'=SUMPRODUCT(({rI}="Única")*({rO}<={c}$32)*({rV}>={c}$32)*{rQ}/({rV}-{rO}+1))', total=False)
    hk.fila_mensual(38, 'Costo devengado del mes (personas, nube y gastos del mes, más equipos devengados)',
                    lambda m, c: f'={CO}{c}14-{CO}{c}8-{CO}{c}9+{c}37', total=False)
    hk.fila_mensual(39, 'Costo planificado acumulado (línea base de costos)', lambda m, c: f'={c}38' if m == 1 else f'={mc(m - 1)}39+{c}38', total=False)
    hk.fila_mensual(40, 'Ingresos por hitos acumulados', lambda m, c: f'={c}33', total=False)
    def grafico(titulo, ancla, n, filas_color, alto, ancho, suave):
        ch = LineChart(); ch.title = titulo; ch.height, ch.width = alto, ancho
        ch.y_axis.title = 'UF acumuladas'; ch.x_axis.title = 'Mes contractual'
        ch.y_axis.delete = False; ch.x_axis.delete = False; ch.y_axis.number_format = '#,##0'
        for r, color in filas_color:
            se = Series(Reference(hk.ws, min_col=3, max_col=2 + n, min_row=r, max_row=r))
            se.tx = SeriesLabel(strRef=StrRef(f"'CURVA S'!$A${r}")); se.smooth = suave and r == 39   # los hitos son escalones: no se suavizan
            se.graphicalProperties.line.solidFill = color; se.graphicalProperties.line.width = 28575   # color explícito: sin él, LibreOffice las guarda en blanco
            se.marker.symbol = 'none'; ch.series.append(se)
        ch.legend.position = 'b'; ch.set_categories(Reference(hk.ws, min_col=3, max_col=2 + n, min_row=32))
        hk.ws.add_chart(ch, ancla)
    grafico('Curva S de la implementación: costo planificado acumulado, M1 a M21', 'A4', 21, ((39, 'D03B3B'), (40, '196197')), 12.5, 19, True)
    hk.set('A43', 'Flujo acumulado del contrato en 56 meses (comunicado, nota §6): costos pagados con intereses, ingresos y saldo de caja', F_NEG, fill=R_TOT)
    grafico('Costos, ingresos y saldo de caja acumulados, M1 a M56', 'A44', N_MESES, ((33, '196197'), (34, 'D03B3B'), (35, 'EDA100')), 12.5, 30, False)
    hk.anchos(a=38); hk.ws.freeze_panes = None

    # ------------------------------------------------------------------ INDICADORES
    ID = q('INDICADORES')
    hq = Hoja(wb, 'INDICADORES', 'Indicadores del proyecto')
    hq.cab(3, ['Indicador', 'Valor', 'Unidad', 'Cómo se calcula'])
    ind = [
        ('Ingresos netos totales', f'={IN}B18', 'UF', NUM, 'Hitos más mensualidades, sin IVA'),
        ('Costos totales', f'={CO}B14', 'UF', NUM, 'Todos los componentes, sin intereses'),
        ('EBITDA', '=B4-B5', 'UF', NUM, 'Ingresos menos costos'),
        ('Rentabilidad = EBITDA / ingresos netos', '=B6/B4', '', PCT, 'Comunicado §7; sin impuestos ni IVA'),
        ('¿Cumple el tope de rentabilidad?', f"=IF(B7<={P['rent_max']},\"Sí\",\"No\")", '', None, 'Tope del E-24'),
        ('Tasa de descuento ponderada, mensual', f"={P['wacc_m']}", 'mensual', '0.0000%', 'Deuda × su tasa + capital propio × tasa de los socios'),
        ('Tasa de descuento ponderada, anual', f"={P['wacc_a']}", 'anual', PCT, 'Debe ser menor que 20 %'),
        ('VAN del flujo del proyecto (Fila A)', f"=NPV({P['wacc_m']},{FC}{C1}16:{CN}16)", 'UF', NUM, 'Valor presente del flujo mensual sin financiamiento'),
        ('VAN del flujo del proyecto', f"=B11*{P['uf']}", 'CLP', ENT, 'VAN en UF × valor de la UF'),
        ('TIR mensual del flujo del proyecto', f'=IFERROR(IRR({FC}{C1}16:{CN}16),"No definida")', 'mensual', '0.00%', 'El flujo cambia de signo varias veces: puede haber más de una TIR o ninguna'),
        ('TIR anual equivalente', f"=IFERROR((1+B13)^{P['meses_anio']}-1,\"No definida\")", 'anual', PCT, '(1 + TIR mensual)^12 − 1'),
        ('Mayor necesidad de caja del proyecto', f'=MAX(0,-MIN({FC}{C1}17:{CN}17))', 'UF', NUM, 'Mínimo del flujo acumulado de la Fila A, en valor absoluto'),
        ('Mes de la mayor necesidad de caja', f'=INDEX({FC}{C1}4:{CN}4,MATCH(MIN({FC}{C1}17:{CN}17),{FC}{C1}17:{CN}17,0))', 'mes', ENT, 'Mes en que el flujo acumulado toca fondo'),
        ('Crédito bancario', f'={FN}B6', 'UF', NUM, 'Porcentaje bancario × financiamiento requerido (necesidad de caja más intereses del período de gracia)'),
        ('Saldo máximo usado de la línea de crédito', f'=MAX({FN}{C1}19:{CN}19)', 'UF', NUM, 'Tope: línea de crédito del E-24'),
        ('Déficit no cubierto por el financiamiento', f'={FN}B22', 'UF', NUM, 'Debe ser cero'),
        ('VAN del flujo neto de los socios (Fila C)', f"=NPV({P['tasa_soc_m']},{NE}{C1}15:{CN}15)", 'UF', NUM, 'Descontado a la tasa de los socios'),
        ('Precio de la implementación', f'={CO}B36', 'UF', NUM, 'Se cobra por hitos H1–H12'),
        ('Precio de la operación', f'={CO}B37', 'UF', NUM, '36 mensualidades'),
        ('Precio total del proyecto', '=B21+B22', 'UF', NUM, ''),
        ('Precio total del proyecto', f"=B23*{P['uf']}", 'CLP', ENT, ''),
        ('Precio total del proyecto', f"=B24/{P['usd']}", 'USD', ENT, ''),
    ]
    for k, (rot, f, u, fmt, como) in enumerate(ind):
        r = 4 + k; hq.set(f'A{r}', rot); hq.set(f'B{r}', f, F_NEG, fmt); hq.set(f'C{r}', u); hq.set(f'D{r}', como)
    r = 4 + len(ind) + 1; hq.set(f'A{r}', 'Controles de cuadratura', F_NEG, fill=R_TOT)
    ctr = [
        ('HH totales de la dotación (deben ser 239.250,01)', f'={DOT}B{FT}', NUM),
        ('HH de operación de M21 a M56 de los perfiles (informativo)', f'=SUMPRODUCT({DOT}{C1}{FT}:{CN}{FT},{rngO})', NUM),
        ('Suma de porcentajes de los hitos (debe ser 100 %)', f"={P['suma_hitos']}", PCT),
        ('Número de mensualidades de operación (deben ser 36)', f'={IN}B22', ENT),
        ('HH de software por puntos de casos de uso (deben ser 31.625,44)', f"={q('PCUESFUERZO')}U16", NUM),
        ('Perfiles con costo o tarifa fuera del rango del E-26 (debe ser 0)', f'=COUNTIF({SUR}I{F0}:I{FT - 1},"Fuera del rango")', ENT),
        ('Venta devengada menos ingresos cobrados (debe ser 0)', f'={CO}B19-{IN}B18', NUM),
        ('Suma de los tramos de pago de equipos (debe ser 100 %)', f"={P['suma_pago']}", PCT),
        ('Equipos devengados menos equipos pagados en el horizonte (debe ser 0)', f"=SUM({q('CURVA S')}{C1}37:{CN}37)-{CO}B8-{CO}B9", NUM),
        ('Equipos pagados en el horizonte menos su costo total (debe ser 0)', f"={AD}T{rc + 0}+{AD}T{rc + 1}+{AD}T{rc + 2}+{AD}T{rc + 3}-SUMIF({AD}K{A0}:K{A1_},\"Única\",{AD}Q{A0}:Q{A1_})", NUM),
    ]
    for k, (rot, f, fmt) in enumerate(ctr):
        hq.set(f'A{r + 1 + k}', rot); hq.set(f'B{r + 1 + k}', f, F_NEG, fmt)
    for c, w in zip('ABCD', (62, 18, 10, 80)):
        hq.ws.column_dimensions[c].width = w

    # ------------------------------------------------------------------ SENSIBILIDAD
    hsn = Hoja(wb, 'SENSIBILIDAD', 'Sensibilidad (E-21, 2.2)')
    hsn.cab(3, ['Variación de los costos', 'Costos (UF)', 'EBITDA (UF)', 'Rentabilidad'])
    for k, v in enumerate((-0.10, -0.05, 0, 0.05, 0.10, 0.15, 0.20)):
        r = 4 + k; hsn.entrada(f'A{r}', v, PCT)
        hsn.set(f'B{r}', f'={ID}$B$5*(1+A{r})', fmt=NUM); hsn.set(f'C{r}', f'={ID}$B$4-B{r}', fmt=NUM); hsn.set(f'D{r}', f'=C{r}/{ID}$B$4', fmt=PCT)
    hsn.cab(13, ['Variación de los ingresos', 'Ingresos (UF)', 'EBITDA (UF)', 'Rentabilidad'])
    for k, v in enumerate((-0.15, -0.10, -0.05, 0, 0.05)):
        r = 14 + k; hsn.entrada(f'A{r}', v, PCT)
        hsn.set(f'B{r}', f'={ID}$B$4*(1+A{r})', fmt=NUM); hsn.set(f'C{r}', f'=B{r}-{ID}$B$5', fmt=NUM); hsn.set(f'D{r}', f'=C{r}/B{r}', fmt=PCT)
    hsn.set('A21', 'Punto de equilibrio: alza de costos que deja el EBITDA en cero', F_NEG); hsn.set('B21', f'={ID}B4/{ID}B5-1', F_NEG, PCT)
    hsn.set('A22', 'Punto de equilibrio: caída de ingresos que deja el EBITDA en cero', F_NEG); hsn.set('B22', f'=1-{ID}B5/{ID}B4', F_NEG, PCT)
    hsn.set('A24', 'Escenarios de atraso del SD-07 (§7.3.3.2) y su costo', F_NEG, fill=R_TOT)
    hsn.cab(25, ['Escenario', 'Actividad', 'Efecto sin respuesta', 'Respuesta', 'HH de la respuesta', 'HH de recargo', 'Costo UF'])
    E = leer('escenarios_atraso.csv')[1:]
    for k, e in enumerate(E):
        r = 26 + k
        hsn.set(f'A{r}', e[0]); hsn.set(f'B{r}', f'{e[2]} ({e[3]})'); hsn.set(f'C{r}', e[4]); hsn.set(f'D{r}', e[5])
        hsn.entrada(f'E{r}', num(e[6]), NUM); hsn.entrada(f'F{r}', num(e[7]), NUM)
        hsn.set(f'G{r}', f'=(E{r}+F{r})*{CO}$B$29/{CO}$B$28', fmt=NUM)
    r = 26 + len(E)
    hsn.set(f'A{r}', 'Total', F_NEG, fill=R_TOT)
    for c in 'EFG':
        hsn.set(f'{c}{r}', f'=SUM({c}26:{c}{r - 1})', F_NEG, NUM, R_TOT)
    hsn.set(f'A{r + 1}', 'Contingencia disponible (HH)', F_NEG); hsn.set(f'E{r + 1}', f"={P['cont_hh']}", F_NEG, NUM)
    hsn.set(f'A{r + 2}', 'Parte de la contingencia que usan todas las respuestas juntas', F_NEG); hsn.set(f'E{r + 2}', f'=(E{r}+F{r})/E{r + 1}', F_NEG, PCT)
    for c, w in zip('ABCDEFG', (60, 46, 60, 34, 16, 14, 14)):
        hsn.ws.column_dimensions[c].width = w

    # ------------------------------------------------------------------ INNOVACIONES
    hv2 = Hoja(wb, 'INNOVACIONES', 'Las cinco innovaciones obligatorias (E-21, 2.7): esfuerzo, equipos y ventana')
    hv2.cab(3, ['Innovación (rama 1.10)', 'HH (dato de entrada)', 'Costo de personas UF', 'Equipos UF', 'Costo total UF', 'Ventana de trabajo', 'Dónde aparece en el flujo'])
    PK = leer('HH_por_paquete_EDT.csv')[1:]
    nombres = {'1.10.1': 'Lockers Ancoa 24/7', '1.10.2': 'Conteo cíclico predictivo', '1.10.3': 'Búsqueda vectorial multimodal',
               '1.10.4': 'Retail Media Network', '1.10.5': 'Modo Tienda con fila virtual de probadores'}
    meses_re = re.compile(r'M(\d+)')
    for k, (cod, nom) in enumerate(nombres.items()):
        r = 4 + k; sub = [p for p in PK if p[0].startswith(cod + '.')]
        ms = [int(x) for p in sub for x in meses_re.findall(p[4])]
        hv2.set(f'A{r}', f'{cod} {nom}'); hv2.entrada(f'B{r}', round(sum(num(p[3]) for p in sub), 2), NUM)
        hv2.set(f'C{r}', f'=B{r}*{CO}$B$29/{CO}$B$28', fmt=NUM)
        claves = {'1.10.1': ('locker', 'locker_inst'), '1.10.5': ('totem',)}.get(cod, ())
        hv2.set(f'D{r}', '=' + '+'.join(f"{AD}T{fila_item[c]}" for c in claves) if claves else 0, fmt=NUM)
        hv2.set(f'E{r}', f'=C{r}+D{r}', fmt=NUM)
        hv2.set(f'F{r}', f'M{min(ms)}–M{max(ms)}' if ms else '')
        hv2.set(f'G{r}', 'Personas: filas de perfiles (HH de la rama 1.10). Equipos: ADQUISICIONES, categoría Innovaciones.')
    hv2.set('A9', 'Total', F_NEG, fill=R_TOT)
    for c in 'BCDE':
        hv2.set(f'{c}9', f'=SUM({c}4:{c}8)', F_NEG, NUM, R_TOT)
    hv2.set('A11', 'El costo de personas de las innovaciones ya está dentro de DOTACIÓN; esta hoja lo muestra aparte y no lo suma de nuevo al flujo.')
    hv2.set('A12', 'Los lockers se asignan a la innovación 1.10.1 y los tótems a la 1.10.5; su cantidad por tienda es un supuesto hasta el levantamiento de la Etapa 2.')
    for c, w in zip('ABCDEFG', (48, 18, 18, 14, 14, 16, 90)):
        hv2.ws.column_dimensions[c].width = w

    # ------------------------------------------------------------------ PCUESFUERZO
    hu = Hoja(wb, 'PCUESFUERZO', 'Estimación del software por puntos de casos de uso',
              'Fuente: ucp_actores.csv, ucp_casos_de_uso.csv y ucp_factores.csv (Formularios T-14 y T-15).')
    hu.cab(4, ['Actor', 'Nombre', 'Tipo', 'Peso'])
    AC = leer('ucp_actores.csv')[1:]
    for k, a in enumerate(AC):
        r = 5 + k; hu.set(f'A{r}', a[0]); hu.set(f'B{r}', a[1]); hu.entrada(f'C{r}', int(a[2]), ENT); hu.set(f'D{r}', f'=C{r}', fmt=ENT)
    ra = 5 + len(AC); hu.set(f'A{ra}', 'UAW', F_NEG, fill=R_TOT); hu.set(f'D{ra}', f'=SUM(D5:D{ra - 1})', F_NEG, ENT, R_TOT)
    hu.cab(4, ['Paquete EDT', 'Caso de uso', 'Nombre', 'Transacciones', 'Peso', 'HH del paquete (T-14)'], col0=6)
    CU = leer('ucp_casos_de_uso.csv')[1:]
    for k, c in enumerate(CU):
        r = 5 + k; hu.set(f'F{r}', c[0]); hu.set(f'G{r}', c[1]); hu.set(f'H{r}', c[2]); hu.entrada(f'I{r}', int(c[3]), ENT)
        hu.set(f'J{r}', f'=IF(I{r}<=$U$20,$U$22,IF(I{r}<=$U$21,$U$23,$U$24))', fmt=ENT); hu.entrada(f'K{r}', num(c[5]), NUM)
    ru = 5 + len(CU); hu.set(f'F{ru}', 'UUCW', F_NEG, fill=R_TOT); hu.set(f'J{ru}', f'=SUM(J5:J{ru - 1})', F_NEG, ENT, R_TOT)
    hu.set(f'K{ru}', f'=SUM(K5:K{ru - 1})', F_NEG, NUM, R_TOT)
    hu.cab(4, ['Factor', 'Descripción', 'Tipo', 'Peso', 'Valor (0-5)', 'Peso × valor', 'Justificación'], col0=13)
    FA = leer('ucp_factores.csv')[1:]
    for k, f in enumerate(FA):
        r = 5 + k; hu.set(f'M{r}', f[0]); hu.set(f'N{r}', f[1]); hu.set(f'O{r}', f[2]); hu.entrada(f'P{r}', num(f[3]), NUM)
        hu.entrada(f'Q{r}', int(num(f[4])), ENT); hu.set(f'R{r}', f'=P{r}*Q{r}', fmt=NUM); hu.set(f'S{r}', f[6])
    rf = 5 + len(FA) - 1
    hu.cab(4, ['Cálculo', 'Valor'], col0=20)
    calc = [
        (5, 'UAW (actores)', f'=D{ra}', ENT), (6, 'UUCW (casos de uso)', f'=J{ru}', ENT), (7, 'UUCP = UAW + UUCW', '=U5+U6', ENT),
        (8, 'Suma ponderada de factores técnicos', f'=SUMIF(O5:O{rf},"Técnico (TCF)",R5:R{rf})', NUM),
        (9, 'TCF = constante + coeficiente × suma técnica', '=U26+U27*U8', '0.000'),
        (10, 'Suma ponderada de factores de ambiente', f'=SUMIF(O5:O{rf},"Ambiente (EF)",R5:R{rf})', NUM),
        (11, 'EF = constante + coeficiente × suma de ambiente', '=U28+U29*U10', '0.000'),
        (12, 'UCP = UUCP × TCF × EF', '=U7*U9*U11', '#,##0.0000'),
        (13, 'HH de programación por UCP', '=U30', NUM), (14, 'HH de programación', '=U12*U13', NUM),
        (15, 'Participación de la programación en el ciclo', '=U31', PCT), (16, 'HH de software', '=U14/U15', NUM),
    ]
    for r, rot, f, fmt in calc:
        hu.set(f'T{r}', rot, F_NEG); hu.set(f'U{r}', f, F_NEG, fmt)
    hu.set('T19', 'Parámetros del método (clase FEP03; T-15)', F_NEG, fill=R_TOT)
    for r, rot, v, fmt in [(20, 'Transacciones máximas de un caso simple', 3, ENT), (21, 'Transacciones máximas de un caso medio', 7, ENT),
                           (22, 'Peso de un caso simple', 5, ENT), (23, 'Peso de un caso medio', 10, ENT), (24, 'Peso de un caso complejo', 15, ENT),
                           (26, 'Constante del TCF', 0.6, NUM), (27, 'Coeficiente del TCF', 0.01, NUM), (28, 'Constante del EF', 1.4, NUM),
                           (29, 'Coeficiente del EF', -0.03, NUM), (30, 'HH de programación por UCP', 20, ENT), (31, 'Participación de la programación', 0.4, PCT)]:
        hu.set(f'T{r}', rot); hu.entrada(f'U{r}', v, fmt)
    for c, w in zip('ABCDEFGHIJKLMNOPQRSTU', (9, 34, 6, 6, 3, 11, 11, 52, 12, 7, 14, 3, 7, 30, 16, 7, 9, 10, 60, 48, 14)):
        hu.ws.column_dimensions[c].width = w
    hu.ws.freeze_panes = 'A5'

    # ------------------------------------------------------------------ HARDWARE CLIENTE (informativa)
    hh = Hoja(wb, 'HARDWARE CLIENTE', 'Hardware que compra el cliente (hoja informativa, no suma al flujo de caja)',
              'Comunicado §9; SD-04, Tabla 4.15. Costos de referencia estimados, sin cotización.')
    hh.cab(4, ['Equipo', 'Especificación técnica', 'Marca y modelo de referencia', 'Cantidad por sitio', 'N° de sitios', 'Cantidad total',
               'Costo unitario USD', 'Costo total USD', 'Costo total UF', 'Fuente o nota'])
    for k, e in enumerate(HARDWARE_CLIENTE):
        r = 5 + k; hh.set(f'A{r}', e[0]); hh.set(f'B{r}', e[1]); hh.set(f'C{r}', e[2])
        hh.entrada(f'D{r}', e[3], NUM); hh.entrada(f'E{r}', e[4], ENT); hh.set(f'F{r}', f'=D{r}*E{r}', fmt=NUM)
        hh.entrada(f'G{r}', e[5], NUM); hh.set(f'H{r}', f'=F{r}*G{r}', fmt=ENT); hh.set(f'I{r}', f"=H{r}*{P['usd']}/{P['uf']}", fmt=NUM); hh.set(f'J{r}', e[6])
    r = 5 + len(HARDWARE_CLIENTE); hh.set(f'A{r}', 'Total', F_NEG, fill=R_TOT)
    for c in 'HI':
        hh.set(f'{c}{r}', f'=SUM({c}5:{c}{r - 1})', F_NEG, NUM, R_TOT)
    for c, w in zip('ABCDEFGHIJ', (34, 52, 34, 12, 10, 12, 14, 14, 14, 60)):
        hh.ws.column_dimensions[c].width = w

    # ------------------------------------------------------------------ RESUMEN EJECUTIVO
    he = Hoja(wb, 'RESUMEN EJECUTIVO', 'Resumen ejecutivo del modelo financiero')
    he.cab(3, ['Concepto', 'UF', 'CLP', 'USD'])
    filas_e = [('Precio de la implementación (hitos H1–H12)', f'={CO}B36'), ('Precio de la operación (36 mensualidades)', f'={CO}B37'),
               ('Precio total del proyecto', '=B4+B5'), ('Mensualidad de la operación', f'={CO}B38'),
               ('Costo total del proyecto', f'={CO}B26'), ('EBITDA', f'={ID}B6'), ('VAN del flujo del proyecto', f'={ID}B11'),
               ('Mayor necesidad de caja', f'={ID}B15')]
    for k, (rot, f) in enumerate(filas_e):
        r = 4 + k; he.set(f'A{r}', rot, F_NEG if k == 2 else F_BASE); he.set(f'B{r}', f, fmt=NUM)
        he.set(f'C{r}', f"=B{r}*{P['uf']}", fmt=ENT); he.set(f'D{r}', f"=C{r}/{P['usd']}", fmt=ENT)
    otros = [('Rentabilidad (EBITDA / ingresos netos)', f'={ID}B7', PCT), ('Tasa de descuento ponderada, anual', f'={ID}B10', PCT),
             ('TIR anual equivalente', f'={ID}B14', PCT), ('Mes de la mayor necesidad de caja', f'={ID}B16', ENT),
             ('HH totales del proyecto', f'={DOT}B{FT}', NUM), ('Horizonte (meses)', f"={P['horizonte']}", ENT)]
    for k, (rot, f, fmt) in enumerate(otros):
        he.set(f'A{13 + k}', rot); he.set(f'B{13 + k}', f, fmt=fmt)
    he.set('A20', 'Alcance del modelo', F_NEG, fill=R_TOT)
    for k, t in enumerate(['Sin IVA y con el tipo de cambio del Formulario E-24.',
                           'Cantidades (HH, dotación, hitos y calendario de compras): Subdocumento 7 y Formularios T-14 y T-15.',
                           'Precios de equipos y de nube: referencias públicas sin cotización (hoja ADQUISICIONES, columna Fuente).',
                           'Supuestos del equipo: hoja PARÁMETROS, sección «Supuestos de costo».',
                           'El hardware que compra el cliente no entra al flujo: está en la hoja HARDWARE CLIENTE.']):
        he.set(f'A{21 + k}', t)
    for c, w in zip('ABCD', (58, 18, 20, 16)):
        he.ws.column_dimensions[c].width = w

    # IVA desglosado en el resumen ejecutivo (Art. 51.2)
    he.set('A28', 'Precio con IVA desglosado (Art. 51.2 de las Bases)', F_NEG, fill=R_TOT)
    he.cab(29, ['Concepto', 'UF', 'CLP', 'USD'])
    for k, (rot, ref) in enumerate([('Implementación', f'{CO}B36'), ('Operación (36 mensualidades)', f'{CO}B37'), ('Proyecto', f'{CO}B36+{CO}B37')]):
        r0 = 30 + 3 * k
        he.set(f'A{r0}', f'{rot}: valor neto'); he.set(f'B{r0}', f'={ref}', fmt=NUM)
        he.set(f'A{r0 + 1}', f"{rot}: IVA"); he.set(f'B{r0 + 1}', f"=B{r0}*{P['iva']}", fmt=NUM)
        he.set(f'A{r0 + 2}', f'{rot}: total con IVA', F_NEG, fill=R_TOT); he.set(f'B{r0 + 2}', f'=B{r0}+B{r0 + 1}', F_NEG, NUM, R_TOT)
        for rr in (r0, r0 + 1, r0 + 2):
            he.set(f'C{rr}', f"=B{rr}*{P['uf']}", fmt=ENT); he.set(f'D{rr}', f"=C{rr}/{P['usd']}", fmt=ENT)
    he.set('A40', 'El flujo de caja y los indicadores son netos, sin IVA (comunicado, nota §7). El IVA se desglosa aquí solo para la oferta.')

    # ------------------------------------------------------------------ CUADRO MAESTRO: costos y precio con margen por componente (E-21, 2.1)
    hm = Hoja(wb, 'CUADRO MAESTRO', 'Cuadro maestro de costos y precio de venta con el margen de cada componente (E-21, 2.1)',
              'Costos: hoja COSTOS. Venta: personas a la tarifa del E-26; los demás componentes con el factor que lleva el proyecto a la rentabilidad objetivo. Margen % = margen ÷ venta.')
    hm.cab(4, ['Componente', 'Tipo de costo', 'Costo implementación UF', 'Costo operación UF', 'Costo total UF', 'Venta implementación UF', 'Venta operación UF',
               'Venta total UF', 'Margen UF', 'Margen % sobre venta', 'Costo total CLP', 'Costo total USD', 'Venta total CLP', 'Venta total USD', 'Margen CLP', 'Margen USD'])
    cat_m = [('Personas (HH por perfil)', 6, 'Directo', True), ('Retén', 7, 'Directo', False), ('Equipos de tiendas, centros y DC-01', 8, 'Directo', False),
             ('Equipos de las innovaciones', 9, 'Directo', False), ('Nube', 10, 'Directo', False), ('Licencias y seguridad', 11, 'Directo', False),
             ('Gastos administrativos y overhead', 12, 'Indirecto', False), ('Contingencia de riesgos', 13, 'Indirecto', False)]
    for k, (rot, fr, tipo, personas) in enumerate(cat_m):
        r = 5 + k; rr = f'{CO}${C1}${fr}:${CN}${fr}'
        hm.set(f'A{r}', rot); hm.set(f'B{r}', tipo)
        hm.set(f'C{r}', f'=SUMPRODUCT({rr},{rngI})', fmt=NUM); hm.set(f'D{r}', f'=SUMPRODUCT({rr},{rngO})', fmt=NUM); hm.set(f'E{r}', f'=C{r}+D{r}', fmt=NUM)
        if personas:
            tr = f"{TP}${C1}${FT}:${CN}${FT}"
            hm.set(f'F{r}', f'=SUMPRODUCT({tr},{rngI})', fmt=NUM); hm.set(f'G{r}', f'=SUMPRODUCT({tr},{rngO})', fmt=NUM)
        else:
            hm.set(f'F{r}', f'=C{r}*{CO}$B$34', fmt=NUM); hm.set(f'G{r}', f'=D{r}*{CO}$B$34', fmt=NUM)
        hm.set(f'H{r}', f'=F{r}+G{r}', fmt=NUM); hm.set(f'I{r}', f'=H{r}-E{r}', fmt=NUM); hm.set(f'J{r}', f'=IF(H{r}>0,I{r}/H{r},0)', fmt=PCT)
        hm.set(f'K{r}', f"=E{r}*{P['uf']}", fmt=ENT); hm.set(f'L{r}', f"=K{r}/{P['usd']}", fmt=ENT)
        hm.set(f'M{r}', f"=H{r}*{P['uf']}", fmt=ENT); hm.set(f'N{r}', f"=M{r}/{P['usd']}", fmt=ENT)
        hm.set(f'O{r}', f"=I{r}*{P['uf']}", fmt=ENT); hm.set(f'P{r}', f"=O{r}/{P['usd']}", fmt=ENT)
    rT = 5 + len(cat_m); hm.set(f'A{rT}', 'Total del proyecto', F_NEG, fill=R_TOT)
    for c in 'CDEFGHIKLMNOP':
        hm.set(f'{c}{rT}', f'=SUM({c}5:{c}{rT - 1})', F_NEG, NUM if c in 'CDEFGHI' else ENT, R_TOT)
    hm.set(f'J{rT}', f'=IF(H{rT}>0,I{rT}/H{rT},0)', F_NEG, PCT, R_TOT)
    hm.set(f'A{rT + 2}', 'Control: venta total menos precio total de INDICADORES (debe ser 0)', F_NEG); hm.set(f'E{rT + 2}', f'=H{rT}-{ID}B23', F_NEG, NUM)
    hm.set(f'A{rT + 3}', 'Control: margen total menos EBITDA de INDICADORES (debe ser 0)', F_NEG); hm.set(f'E{rT + 3}', f'=I{rT}-{ID}B6', F_NEG, NUM)
    hm.set(f'A{rT + 4}', 'La contingencia se valoriza a costo y se vende con el mismo factor que los demás componentes; no se presenta como margen.')
    hm.ws.column_dimensions['A'].width = 42; hm.ws.column_dimensions['B'].width = 12
    for c in 'CDEFGHIJKLMNOP':
        hm.ws.column_dimensions[c].width = 16
    hm.ws.freeze_panes = 'C5'

    # ------------------------------------------------------------------ documentación de supuestos en cada hoja (E-21, requisitos técnicos)
    NOTAS = {
        'RESUMEN EJECUTIVO': 'Supuestos: valores netos al tipo de cambio del E-24; precios y márgenes salen de COSTOS, INGRESOS e INDICADORES; el IVA se desglosa solo al final.',
        'INDICADORES': 'Supuestos: rentabilidad objetivo y tasas en PARÁMETROS; el VAN usa la tasa ponderada mensual sobre el flujo del proyecto (Fila A); el impuesto está apagado; la TIR puede no ser única.',
        'CURVA S': 'Sin supuestos propios: acumula los ingresos de INGRESOS, los egresos de COSTOS y el saldo de caja de FLUJO DE CAJA NETO.',
        'INGRESOS': 'Supuestos: cada hito cobra su porcentaje del precio de implementación en su mes del E-25 (desfase en PARÁMETROS); la mensualidad de operación es igual en los 36 meses y se cobra en el mes de la prestación.',
        'COSTOS': 'Supuestos: costo de personas = HH × costo por hora del perfil; la contingencia se valoriza al costo medio de la HH de implementación; la venta usa la tarifa por perfil y un factor común para los demás componentes.',
        'SENSIBILIDAD': 'Supuestos: variaciones porcentuales uniformes sobre el total de costos o de ingresos, con el calendario sin cambios; los escenarios de atraso vienen del SD-07 §7.3.3.2.',
        'INNOVACIONES': 'Supuestos: las HH de cada rama 1.10.x son las de la EDT; la cantidad de lockers y tótems por tienda es un supuesto hasta el levantamiento de la Etapa 2.',
        'PROVEEDORES': 'Supuestos: precios públicos de referencia sin cotización; la moneda de cada precio se convierte con el tipo de cambio del E-24.',
        'Costos HH por MES': 'Supuestos: persona equivalente = HH del mes ÷ horas por persona al mes (PARÁMETROS); la dotación viene de la red del cronograma estabilizada.',
        'COSTOS DE OPERACION': 'Supuestos: costo de cada perfil igual al punto medio del rango del E-26; el retén se valoriza por unidad de 12 h (PARÁMETROS).',
        'TARIFAS DE OPERACION': 'Supuestos: tarifa por perfil de la hoja Costos HH - Sueldos (margen objetivo, mínimo del E-26 y máximo del E-26); el retén usa el factor de los demás componentes.',
    }
    for n, t in NOTAS.items():
        if wb[n]['A2'].value is None:
            c = wb[n]['A2']; c.value = t; c.font = F_BASE

    # ------------------------------------------------------------------ validación de datos y protección de fórmulas (E-21, requisitos técnicos)
    def clase(ws, c):
        n = ws.title; col = c.column_letter; fmt = c.number_format; a = ws[f'A{c.row}'].value
        if n == 'ADQUISICIONES':
            if col == 'E': return ('list', '"USD,EUR,CLP,UF"', None, None, 'Elija USD, EUR, CLP o UF.')
            if col == 'K': return ('list', '"Única,Mensual"', None, None, 'Elija Única o Mensual.')
            if col in 'LMUV': return ('whole', 'between', 1, N_MESES, 'Mes entre 1 y 56.')
        if n == 'PARÁMETROS':
            if isinstance(a, str) and re.fullmatch(r'H\d+', a) and col == 'B': return ('whole', 'between', 1, N_MESES, 'Mes entre 1 y 56.')
            if isinstance(a, str) and a.startswith('Incluir impuesto'): return ('list', '"0,1"', None, None, 'Escriba 1 para incluir el impuesto o 0 para excluirlo.')
        if n == 'PCUESFUERZO':
            if col == 'Q': return ('whole', 'between', 0, 5, 'Valor entero de 0 a 5.')
            if col == 'C': return ('whole', 'between', 1, 3, 'Tipo de actor: 1, 2 o 3.')
            if col == 'I': return ('whole', 'greaterThanOrEqual', 1, None, 'Al menos una transacción.')
            if col in 'PU': return ('decimal', 'between', -1000, 1000000, 'Número entre -1.000 y 1.000.000.')
        if n == 'SENSIBILIDAD' and col == 'A': return ('decimal', 'between', -1, 1, 'Variación entre -100 % y 100 %.')
        if '%' in fmt: return ('decimal', 'between', 0, 1, 'Fracción entre 0 y 1; por ejemplo 0,18 para 18 %.')
        if fmt == ENT: return ('whole', 'greaterThanOrEqual', 0, None, 'Número entero mayor o igual que cero.')
        return ('decimal', 'greaterThanOrEqual', 0, None, 'Número mayor o igual que cero.')
    def runs(cols):
        cols = sorted(cols); out = []; ini = prev = None
        for x in cols:
            if ini is None: ini = prev = x
            elif x == prev + 1: prev = x
            else: out.append((ini, prev)); ini = prev = x
        if ini is not None: out.append((ini, prev))
        return out
    n_val = 0
    for ws in wb.worksheets:
        grupos = collections.defaultdict(lambda: collections.defaultdict(list))
        for row in ws.iter_rows():
            for c in row:
                if c.fill is not None and c.fill.fgColor is not None and str(c.fill.fgColor.rgb).endswith('FFF9D6'):
                    c.protection = Protection(locked=False)
                    grupos[clase(ws, c)][c.row].append(c.column)
        for regla, filas_ in grupos.items():
            tipo, op, v1, v2, msg = regla
            if tipo == 'list':
                dv = DataValidation(type='list', formula1=op, allow_blank=True)
            else:
                dv = DataValidation(type=tipo, operator=op, formula1=str(v1), formula2=(str(v2) if v2 is not None else None), allow_blank=True)
            dv.error = msg; dv.errorTitle = 'Dato no válido'; dv.showErrorMessage = True
            dv.prompt = msg; dv.promptTitle = 'Dato de entrada'; dv.showInputMessage = True
            for r, cols in filas_.items():
                for a_, b_ in runs(cols):
                    dv.add(f'{L(a_)}{r}:{L(b_)}{r}' if a_ != b_ else f'{L(a_)}{r}')
            ws.add_data_validation(dv); n_val += 1
        ws.protection.sheet = True; ws.protection.formatColumns = False; ws.protection.formatRows = False
    print('validaciones:', n_val, 'reglas; hojas protegidas sin clave:', len(wb.worksheets))

    # ------------------------------------------------------------------ RESUMEN (rótulos de la plantilla, referencias reconectadas)
    rs = wb['RESUMEN']; tp = openpyxl.load_workbook(PLANTILLA)['RESUMEN']
    for row in tp.iter_rows(min_row=1, max_row=30, max_col=14):
        for c in row:
            if isinstance(c.value, str) and not c.value.startswith('='):
                try: rs[c.coordinate].value = c.value
                except AttributeError: pass
    try: rs['A2'].value = None
    except AttributeError: pass
    UF, USD = P['uf'], P['usd']
    B = {12: f'={CP}B{bP}-{CP}B{bP + 2}', 13: f'={CO}B40', 14: f'={CP}B{bP + 2}', 15: f'={CO}B41', 16: f'={CP}B{bP + 1}', 17: f'={CO}B42'}
    Gt = {12: f'={TP}B{bP}-{TP}B{bP + 2}', 13: f'=B13*{CO}B34', 14: f'={TP}B{bP + 2}', 15: f'=B15*{CO}B34', 16: f'={TP}B{bP + 1}', 17: f'=B17*{CO}B34'}
    for r in range(12, 18):
        rs[f'B{r}'] = B[r]; rs[f'G{r}'] = Gt[r]
    for r in (6, 7, 12, 13, 14, 15, 16, 17):
        rs[f'C{r}'] = f'=B{r}*{UF}'; rs[f'D{r}'] = f'=C{r}/{USD}'; rs[f'H{r}'] = f'=G{r}*{UF}'; rs[f'I{r}'] = f'=H{r}/{USD}'
    for r in (6, 7):
        rs[f'M{r}'] = f'=L{r}*{UF}'; rs[f'N{r}'] = f'=M{r}/{USD}'; rs[f'L{r}'] = f'=+G{r}-B{r}'
    rs['B6'], rs['B7'], rs['G6'], rs['G7'] = '=B18', '=B19', '=G18', '=G19'
    for c in 'BCDGHI':
        rs[f'{c}8'] = f'=SUM({c}6:{c}7)'; rs[f'{c}18'] = f'=SUM({c}12:{c}15)'; rs[f'{c}19'] = f'=SUM({c}16:{c}17)'; rs[f'{c}20'] = f'=SUM({c}18:{c}19)'
    for c in 'LMN':
        rs[f'{c}8'] = f'=SUM({c}6:{c}7)'
    rs['L9'], rs['M9'], rs['N9'] = '=+L8/B8', '=+M8/C8', '=+N8/D8'
    rs['G21'] = f'={ID}B11'; rs['G22'] = f'={ID}B13'
    PCU = q('PCUESFUERZO')
    rs['B25'], rs['B26'], rs['B27'], rs['B28'] = f'={PCU}U12', f'={PCU}U13', f'={PCU}U14', f'={PCU}U16'
    rs['B29'], rs['B30'] = '=G8', '=B8'

    orden = ['RESUMEN', 'RESUMEN EJECUTIVO', 'CUADRO MAESTRO', 'INDICADORES', 'PARÁMETROS', 'CURVA S', 'FLUJO DE CAJA NETO', 'FLUJO DE CAJA COMPLETO',
             'INGRESOS', 'COSTOS', 'FINANCIAMIENTO', 'SENSIBILIDAD', 'INNOVACIONES', 'GASTOS ADMINISTRATIVOS', 'ADQUISICIONES', 'PROVEEDORES',
             'Costos HH - Sueldos', 'Costos HH por MES', 'DOTACIÓN', 'COSTOS DE OPERACION', 'TARIFAS DE OPERACION', 'PCUESFUERZO', 'HARDWARE CLIENTE']
    wb._sheets = [wb[n] for n in orden]
    wb.save(salida)
    print('ok', salida, len(wb.sheetnames), 'hojas')

if __name__ == '__main__':
    construir(sys.argv[1], sys.argv[2])
