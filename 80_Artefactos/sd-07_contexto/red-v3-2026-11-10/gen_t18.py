"""Genera el Formulario T-18 desde el .tex del traspaso con el preámbulo vigente y los cambios del paso C/H.
Uso: python3 -I gen_t18.py <tex traspaso> <tex repo> <salida>"""
import sys
Z, R, OUT = sys.argv[1:4]
z = open(Z, encoding='utf-8').read(); r = open(R, encoding='utf-8').read()
s = r[:r.index('\\begin{document}')] + z[z.index('\\begin{document}'):]
def rep(a, b, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(f'{c} apariciones: {a[:80]}')
    s = s.replace(a, b)
rep('Es un piloto técnico en preproducción aislada dentro de la tienda;',
    'Las tres tiendas son tiendas a la calle, que no dependen de la administración de un centro comercial para intervenir su red, su energía o su horario, de modo que el corte de enlace se ensaya sin autorizaciones de terceros. Es un piloto técnico en preproducción aislada dentro de la tienda;')
rep('Piloto técnico, M6--7 & Tres tiendas identificadas en H1;', 'Piloto técnico, M6--7 & Tres tiendas a la calle identificadas en H1;')
rep('El registro de implantación identifica individualmente las 22 tiendas SIT-01, la tienda insignia si no está entre las tres piloto, CD-01, CD-02 y DC-01/DC-02,',
    'El registro de implantación identifica individualmente las 22 tiendas SIT-01, la tienda insignia si no está entre las tres piloto, la tienda de laboratorio, CD-01, CD-02 y DC-01/DC-02,')
rep('La Tabla T-18.3 resume', 'La Tabla~\\ref{tab:t18-3} resume')
rep('La Tabla T-18.6 relaciona', 'La Tabla~\\ref{tab:t18-6} relaciona')
tabla = '\n'.join([
 'La Tabla~\\ref{tab:t18-cierre} indica cómo se mide cada condición y qué umbral debe alcanzar. Las cuatro semanas de evidencia van del 10 de marzo al 6 de abril de 2028 en la Etapa 1 y del 10 de agosto al 6 de septiembre de 2028 en la Etapa 2.', '',
 '\\begin{longtable}{@{}p{0.22\\linewidth}p{0.38\\linewidth}p{0.32\\linewidth}@{}}',
 '\\caption[Medición y umbral de las condiciones de cierre]{Medición y umbral de las condiciones de cierre. Fuente: Elaboración propia a partir del artículo 17.3 y del Caso 09.}\\label{tab:t18-cierre}\\\\',
 '\\toprule', '\\textbf{Condición} & \\textbf{Cómo se mide} & \\textbf{Umbral para cerrar} \\\\', '\\midrule', '\\endhead', '\\bottomrule', '\\endlastfoot',
 'Incidentes críticos y altos & Registro de incidentes atribuibles a la solución & Ninguno abierto \\\\',
 'Volumen real comprometido & Volumen por proceso y sitio registrado en el plan aprobado antes de iniciar la marcha blanca & 100\\,\\% del volumen comprometido en cada una de las cuatro últimas semanas \\\\',
 'Disponibilidad y tiempos de respuesta & Medición diaria por servicio con el percentil del catálogo de requisitos & 99,9\\,\\% mensual en la transacción crítica y umbrales de RT-09.01, sostenidos las cuatro semanas \\\\',
 'Conciliación & Comparación diaria por cuenta, saldo e inventario con el registro vigente & Ninguna diferencia sin explicar \\\\',
 'Capacitación & Registros de asistencia y evaluación del paquete 1.13.3 & 100\\,\\% del personal del plan certificado \\\\',
 'Acta & Revisión del expediente por la Contraparte Técnica & Acta de aceptación suscrita \\\\',
 '\\end{longtable}', '',
 'La condición de capacitación de la Etapa 2 se apoya en la capacitación adelantada a M17, que cubre el 30\\,\\% de las horas sobre los procesos y reglas aprobados en H8; el resto se dicta desde H9 sobre el software con pruebas superadas.', ''])
rep('Si al término del período no se satisfacen las condiciones anteriores, la marcha blanca se extiende',
    tabla + 'Si al término del período no se satisfacen las condiciones anteriores, la marcha blanca se extiende')
rep('Multitiendas Ancoa S.A. (2026). Bases Técnicas del Caso 09 - Cadena Multitienda. Licitación TFEP-01/2026.',
    '\\noindent\\hangindent=1.5em\\hangafter=1 Multitiendas Ancoa S.A. (2026). \\textit{Bases técnicas. Caso 09: Cadena multitienda} (Licitación N.° TFEP-01/2026, versión 1.0).')
rep('Se utilizó OpenAI Codex para asistir en la organización del contenido, la conciliación de fechas y recursos y la revisión de redacción.',
    'Se utilizó OpenAI Codex para asistir en la organización del contenido, la conciliación de fechas y recursos y la revisión de redacción. En esta actualización se utilizó Claude Code (Anthropic) para incorporar el piloto en tiendas a la calle, la tienda de laboratorio, la tabla de medición y umbral de las condiciones de cierre y la capacitación adelantada de la Etapa 2. La revisión humana de esta versión corresponde al equipo autor y se registrará al realizarse.')
open(OUT, 'w', encoding='utf-8').write(s); print('ok')
