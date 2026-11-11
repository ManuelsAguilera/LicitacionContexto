"""Figuras SD-07 · Árboles de la EDT: raíz con las quince ramas (Figura 7.1) y ramas 1.4 y 1.8 (Figuras 7.5 y 7.9).

Reemplazan las imágenes importadas sd07-edt1.0/1.4/1.8.png, que mostraban 13 paquetes en 1.4 y 8 en 1.8.
Datos: red v2/v3 del SD-07 (paquetes 1.4.14 a 1.4.24 y 1.8.9 traspasados desde el SD-04).
El título y la fuente los pone la leyenda del .tex; la imagen no los repite.
Uso: <python con matplotlib> diag-07-06_edt-raiz-y-ramas.py
Salida: diag-07-06_edt-1-0/1-4/1-8.(png|pdf) aquí y sd07-edt1.0/1.4/1.8.png en latex_final/figuras/sd07-figuras/.
"""
import os, shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, '..', '..'))
FIG = os.path.join(RAIZ, '02_Propuesta/latex_final/figuras/sd07-figuras')
NAVY, CAJA, BORDE, LINEA, ACENTO, TEXTO = '#17324D', '#EEF3F8', '#C9D5E2', '#7A8794', '#196197', '#17324D'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 9, 'text.color': TEXTO})

RAMAS = [  # código, nombre, elementos de tercer nivel
    ('1.1', 'Dirección, gobierno y control del proyecto', '12 paquetes'),
    ('1.2', 'Levantamiento y línea base de alcance', '8 paquetes'),
    ('1.3', 'Arquitectura y diseño', '7 paquetes'),
    ('1.4', 'Infraestructura híbrida y plataforma base', '24 paquetes'),
    ('1.5', 'Desarrollo de software', '51 cuentas y 127 paquetes'),
    ('1.6', 'Integraciones', '7 paquetes'),
    ('1.7', 'Migración y saneamiento de datos', '12 paquetes'),
    ('1.8', 'Seguridad, identidad y cumplimiento', '9 paquetes'),
    ('1.9', 'Calidad, pruebas y certificación', '12 paquetes'),
    ('1.10', 'Innovaciones', '5 cuentas y 40 paquetes'),
    ('1.11', 'Implantación y despliegue', '4 paquetes'),
    ('1.12', 'Marchas blancas y aceptación por etapa', '7 paquetes'),
    ('1.13', 'Gestión del cambio y capacitación', '5 paquetes'),
    ('1.14', 'Documentación, transferencia y reversibilidad', '7 paquetes'),
    ('1.15', 'Operación y soporte', '6 paquetes'),
]
R14 = [
    'Entorno de nube (IaC, subredes, etiquetado)',
    'Borde por sitio y red segmentada (25 sitios)',
    'Entorno de Producción y DR de la filial y control de cruces',
    'Ambientes dev/QA/preprod/prod/DR',
    'Observabilidad unificada y catálogo de alertas',
    'Plataforma de integración y entrega continuas',
    'Licenciamiento de terceros a nombre del cliente',
    'Especificación de hardware y dispositivos de terreno',
    'Recinto técnico y obra civil de separación (spec)',
    'Plan de cierre de la brecha del centro de datos',
    'Energía y climatización del centro de datos',
    'Seguridad física del centro de datos',
    'Respaldo en operación con custodia de medios',
    'Levantamiento físico de los 25 sitios',
    'Tienda de laboratorio instalada',
    'Órdenes de compra de DC-01 y del lote 1',
    'Tiendas piloto instaladas',
    'Orden de compra del lote 2 (19 tiendas y 2 CD)',
    'Tiendas y centros de distribución del lote 2 instalados',
    'Recuperación a tamaño completo',
    'Plataforma de datos y analítica',
    'Equipamiento TI y redes de DC-01',
    'Pila local de tienda',
    'Replicación entre regiones',
]
R18 = [
    'Plan de seguridad, controles y amenazas',
    'Superficie de exposición y respuesta a incidentes',
    'Modelo de identidad y segregación de funciones',
    'Cifrado y tokenización de medios de pago',
    'Protección de datos y cumplimiento normativo',
    'Pruebas de intrusión y plan de remediación',
    'Diligencia del proveedor de nube',
    'Atestación de cadena de suministro y confianza cero',
    'Controles de seguridad desplegados',
]


def ajustar(ax, x, y, texto, ancho, **kw):
    """Escribe texto partido en líneas que caben en `ancho` (unidades de datos = pulgadas), midiendo con el renderer."""
    fig = ax.figure; r = fig.canvas.get_renderer()
    def mide(t):
        tt = ax.text(0, 0, t, **kw); w = tt.get_window_extent(renderer=r).width / fig.dpi; tt.remove(); return w
    lineas, actual = [], ''
    for palabra in texto.split():
        prueba = (actual + ' ' + palabra).strip()
        if actual and mide(prueba) > ancho:
            lineas.append(actual); actual = palabra
        else:
            actual = prueba
    lineas.append(actual)
    return ax.text(x, y, '\n'.join(lineas), **kw)


def caja(ax, x, y, w, h, fc=CAJA, ec=BORDE, lw=0.8):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=0.06',
                                fc=fc, ec=ec, lw=lw, zorder=2))


def raiz_y_ramas():
    cols, filas = 3, 5
    W, bw, bh, gx, gy = 6.3, 1.98, 0.62, 0.18, 0.14
    top_h = 0.5
    H = top_h + 0.35 + filas * bh + (filas - 1) * gy + 0.05
    fig = plt.figure(figsize=(W, H)); ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')
    rw = 4.4
    caja(ax, (W - rw) / 2, H - top_h, rw, top_h, fc=NAVY, ec=NAVY)
    ax.text(W / 2, H - top_h / 2, '1.0 · Solución para Multitiendas Ancoa S.A.', ha='center', va='center',
            color='white', fontsize=9.5, fontweight='bold', zorder=3)
    x0 = (W - (cols * bw + (cols - 1) * gx)) / 2
    ybar = H - top_h - 0.17
    ax.plot([W / 2, W / 2], [H - top_h, ybar], color=LINEA, lw=0.9, zorder=1)
    cxs = [x0 + c * (bw + gx) + bw / 2 for c in range(cols)]
    ax.plot([cxs[0], cxs[-1]], [ybar, ybar], color=LINEA, lw=0.9, zorder=1)
    ytop = ybar - 0.18
    for cx in cxs:
        ax.plot([cx, cx], [ybar, ytop], color=LINEA, lw=0.9, zorder=1)
    for i, (cod, nom, n) in enumerate(RAMAS):
        c, f = divmod(i, filas)
        x = x0 + c * (bw + gx); y = ytop - bh - f * (bh + gy)
        caja(ax, x, y, bw, bh)
        ax.text(x + 0.08, y + bh - 0.08, f'{cod} · {n}', ha='left', va='top', fontsize=7.5,
                fontweight='bold', color=ACENTO, zorder=3)
        ajustar(ax, x + 0.08, y + bh - 0.27, nom, bw - 0.16, ha='left', va='top', fontsize=8,
                linespacing=1.15, zorder=3)
    return fig


def rama(cod, nombre, paquetes, cols, wrap):
    W = 6.3
    gx, gy = 0.1, 0.12
    bw = (W - 0.1 - (cols - 1) * gx) / cols
    filas = -(-len(paquetes) // cols)
    bh = 0.78
    top_h = 0.42
    H = top_h + 0.32 + filas * bh + (filas - 1) * gy + 0.05
    fig = plt.figure(figsize=(W, H)); ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')
    rw = 4.4
    caja(ax, (W - rw) / 2, H - top_h, rw, top_h, fc=NAVY, ec=NAVY)
    ax.text(W / 2, H - top_h / 2, f'{cod} · {nombre}', ha='center', va='center', color='white',
            fontsize=9.5, fontweight='bold', zorder=3)
    x0 = 0.05
    ytop = H - top_h - 0.32
    # tronco y barra horizontal sobre la primera fila; cada fila cuelga de la barra por la izquierda
    ax.plot([W / 2, W / 2], [H - top_h, ytop + 0.14], color=LINEA, lw=0.9, zorder=1)
    cxs = [x0 + c * (bw + gx) + bw / 2 for c in range(cols)]
    ax.plot([cxs[0], cxs[-1]], [ytop + 0.14, ytop + 0.14], color=LINEA, lw=0.9, zorder=1)
    for cx in cxs:
        ax.plot([cx, cx], [ytop + 0.14, ytop], color=LINEA, lw=0.9, zorder=1)
    for i, nom in enumerate(paquetes):
        f, c = divmod(i, cols)
        x = x0 + c * (bw + gx); y = ytop - bh - f * (bh + gy)
        nuevo = (cod == '1.4' and i >= 13) or (cod == '1.8' and i == 8)
        caja(ax, x, y, bw, bh, ec=ACENTO if nuevo else BORDE, lw=1.1 if nuevo else 0.8)
        ax.text(x + 0.06, y + bh - 0.07, f'{cod}.{i + 1}', ha='left', va='top', fontsize=7.5,
                fontweight='bold', color=ACENTO, zorder=3)
        ajustar(ax, x + 0.06, y + bh - 0.22, nom, bw - 0.12, ha='left', va='top', fontsize=7,
                linespacing=1.12, zorder=3)
    return fig


def guardar(fig, nombre, destino):
    base = os.path.join(AQUI, f'diag-07-06_edt-{nombre}')
    fig.savefig(base + '.png', dpi=300)
    fig.savefig(base + '.pdf')
    plt.close(fig)
    shutil.copyfile(base + '.png', os.path.join(FIG, destino))
    print('ok', base)


guardar(raiz_y_ramas(), '1-0', 'sd07-edt1.0.png')
guardar(rama('1.4', 'Infraestructura híbrida y plataforma base', R14, 5, 18), '1-4', 'sd07-edt1.4.png')
guardar(rama('1.8', 'Seguridad, identidad y cumplimiento', R18, 5, 22), '1-8', 'sd07-edt1.8.png')
