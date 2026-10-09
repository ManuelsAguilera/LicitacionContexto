"""Genera las figuras 4.1, 4.2 y 4.4 a 4.9 de la arquitectura lógica de SD-04.

Las figuras se producen con el servidor MCP ``infrastructure-diagram-mcp-server``
(herramienta ``generate_diagram``) en una sesión en memoria, sin depender de la
conexión MCP del editor. Cada figura guarda su DSL de ``diagrams`` junto a la
imagen como ``diag-04-NN_<titulo>-mcp.py.txt``; el servidor escribe PNG, DOT y
draw.io en ``generated-diagrams/`` y este script mueve el PNG y el .drawio
finales a esta carpeta con el nombre definitivo.

Ejecución (PowerShell, desde la raíz del repositorio):

    $env:INCLUDE='C:\\Program Files\\Graphviz\\include'
    $env:LIB='C:\\Program Files\\Graphviz\\lib'
    $env:PATH += ';C:\\Program Files\\Graphviz\\bin'
    uvx --from infrastructure-diagram-mcp-server --with "mcp[cli]==1.30.0" \\
        python 04_Adjuntos\\diagramas\\diag-04-logica_generar_mcp.py [NN ...]

Convención visual: línea sólida = arquitectura objetivo (Etapa 2, mes 21);
gris con borde y arista discontinuos = elemento que solo existe en la Etapa 1;
ámbar discontinuo = canal, ruta o contrato por acreditar; punteado dorado =
política X-01 aplicada en cada extremo; azul grueso = autorización de compra con
tarjeta propia, único cruce Retail–Emisor. Las plataformas existentes de Ancoa
usan iconos genéricos (el Caso no declara fabricantes); los iconos Azure
corresponden a la selección de ADR-06 y ADR-07.
"""

import asyncio
import shutil
import sys
from pathlib import Path

import anyio
from mcp import ClientSession
from infrastructure_diagram_mcp_server.server import mcp


ROOT = Path(__file__).resolve().parent
GENERATED = ROOT / 'generated-diagrams'
FONT = 'Arial'
FS = 16  # puntos de rótulo en el lienzo; se comprueba el tamaño impreso tras escalar

# Iconos que el espacio de nombres del servidor no expone directamente se
# declaran como subclases de un icono ya disponible (no se permiten imports).
PRELUDE = '''class AzureMonitor(ApplicationInsights):
    _icon_dir = "resources/azure/monitor"
    _icon = "monitor.png"
class LocalStore(Server):
    _icon_dir = "resources/generic/storage"
    _icon = "storage.png"
'''

STYLE = {
    'n': {},
    # Etapa 1 y por acreditar: caja de texto sin icono, para que el borde contenga el rótulo.
    'e1': {'image': '', 'shape': 'box', 'fixedsize': 'false', 'style': 'dashed,rounded,filled', 'fillcolor': '#EEEEEE',
           'color': '#8E8E8E', 'fontcolor': '#5F5F5F', 'penwidth': '1.6', 'margin': '0.12,0.06'},
    'p': {'image': '', 'shape': 'box', 'fixedsize': 'false', 'style': 'dashed,rounded,filled', 'fillcolor': '#FFF3DF',
          'color': '#C77700', 'fontcolor': '#7A4A00', 'penwidth': '1.6', 'margin': '0.12,0.06'},
}
EDGE = {
    'n': '',
    'e1': 'color="#9E9E9E", style="dashed", penwidth="1.4"',
    'p': 'color="#C77700", style="dashed", penwidth="1.4"',
    'x': 'color="#B08A2E", style="dotted", penwidth="1.6", arrowhead="none", constraint="false"',
    'xc': 'color="#B08A2E", style="dotted", penwidth="1.6", arrowhead="none"',
    'auth': 'color="#2F6EA5", penwidth="2.6"',
    'tel': 'color="#8FA3AE", style="dotted", arrowhead="none", constraint="false"',
    'telc': 'color="#8FA3AE", style="dotted", arrowhead="none"',
    'inv': 'style="invis"',
}
CLUSTER = {
    'retail': '{"bgcolor":"#F3FAF6", "color":"#5E9E86", "style":"rounded", "fontname":"%s", "fontsize":"19", "penwidth":"1.6", "margin":"16"}' % FONT,
    'retail_fila': '{"bgcolor":"#F3FAF6", "color":"#5E9E86", "style":"rounded", "fontname":"%s", "fontsize":"19", "penwidth":"1.6", "margin":"16", "rank":"same"}' % FONT,
    'emisor': '{"bgcolor":"#F8F4FB", "color":"#8E73B0", "style":"rounded", "fontname":"%s", "fontsize":"19", "penwidth":"1.6", "margin":"16"}' % FONT,
    'trans': '{"bgcolor":"#F5F7F9", "color":"#9AA9B4", "style":"rounded", "fontname":"%s", "fontsize":"16", "margin":"16"}' % FONT,
    'fila': '{"style":"invis", "rank":"same", "margin":"0"}',
    'frontera': '{"bgcolor":"#FFF9E6", "color":"#C9A545", "style":"rounded", "fontname":"%s", "fontsize":"16", "margin":"16"}' % FONT,
}


class Fig:
    """Acumula el DSL de una figura con tamaños de nodo fijados para la legibilidad."""

    def __init__(self, title: str, direction: str = 'TB', nodesep: float = 0.88, ranksep: float = 0.35):
        graph = (f'{{"splines":"spline", "nodesep":"{nodesep}", "ranksep":"{ranksep}", "pad":"0.3,0.1", '
                 f'"bgcolor":"white", "dpi":"220", "fontname":"{FONT}", "fontsize":"17", "labelloc":"t", "newrank":"true"}}')
        node = (f'{{"fontname":"{FONT}", "fontsize":"{FS}", "fixedsize":"true", "imagepos":"tc", '
                f'"labelloc":"b", "fontcolor":"#263238"}}')
        edge = f'{{"color":"#546E7A", "arrowsize":"0.7", "penwidth":"1.3", "tailport":"s", "headport":"n", "fontname":"{FONT}", "fontsize":"{FS - 1}"}}'
        self.lines = PRELUDE.splitlines() + [
            f'with Diagram("{title}", show=False, direction="{direction}", graph_attr={graph}, node_attr={node}, edge_attr={edge}):'
        ]
        self.indent = 1

    def _w(self, text: str) -> None:
        self.lines.append('    ' * self.indent + text)

    def cluster(self, label: str, kind: str):
        fig = self

        class _Ctx:
            # kind=None: agrupación sin recuadro, para no ensanchar la figura.
            def __enter__(self_inner):
                if kind:
                    fig._w(f'with Cluster("{label}", graph_attr={CLUSTER[kind]}):')
                    fig.indent += 1

            def __exit__(self_inner, *exc):
                if kind:
                    fig.indent -= 1
        return _Ctx()

    def node(self, var: str, cls: str, label: str, kind: str = 'n', w: float = 0.62) -> None:
        if kind == 'e1':
            label += '\\nEtapa 1'
        lines = label.count('\\n') + 1
        height = w + 0.05 + lines * FS * 1.15 / 72
        # El recuadro del nodo cubre el rótulo: las aristas terminan fuera del texto.
        widest = max(len(t) for t in label.split('\\n'))
        width = w
        attrs = {'width': f'{width:.2f}', 'height': f'{height:.2f}'} if kind == 'n' else {'width': '0', 'height': '0'}
        attrs.update(STYLE[kind])
        args = ', '.join(f'{k}="{v}"' for k, v in attrs.items())
        self._w(f'{var} = {cls}("{label}", {args})')

    def edge(self, src: str, dst: str, kind: str = 'n', label: str = '', extra: str = '') -> None:
        text = f'label="{label}", fontsize="{FS - 1}", fontname="{FONT}"' if label else ''
        parts = [p for p in (EDGE[kind], text, extra) if p]
        if parts:
            self._w(f'{src} >> Edge({", ".join(parts)}) >> {dst}')
        else:
            self._w(f'{src} >> {dst}')

    def code(self) -> str:
        return '\n'.join(self.lines) + '\n'


LEGEND_BLOCK = '\\nsólido: objetivo mes 21 · gris discontinuo: solo Etapa 1 · ámbar discontinuo: por acreditar'


# --------------------------------------------------------------------------- 4.1 / 4.2
def general(stage: int) -> str:
    e2 = stage == 2
    title = ('Ancoa · arquitectura lógica objetivo · Etapa 2, mes 21' if e2 else
             'Ancoa · arquitectura lógica · Etapa 1, mes 16 · gris discontinuo: convivencia que se retira')
    f = Fig(title, nodesep=0.72, ranksep=0.12)
    with f.cluster('Retail', 'retail'):
        f.node('pos', 'Client', 'POS nuevo y\\nnodo local')
        f.node('sala', 'Tablet', 'Móviles\\ny mesón')
        f.node('web', 'Server', 'Comercio\\nelectrónico*')
        f.node('consola', 'Client', 'Consolas CD\\ny comercial' if not e2 else 'Consolas y\\nportal\\nvendedor')
        if e2:
            f.node('portal_p', 'Client', 'Portal proveedor\\npor validar', 'p')
        else:
            f.node('pos14', 'Client', 'POS 2014', 'e1')
            f.node('planillas', 'Document', 'Planillas CD\\nConcepción', 'e1')
        f.node('apim_r', 'APIManagement', 'API Management\\nRetail')
        with f.cluster('', 'fila'):
            if e2:
                f.node('merc', 'PredefinedProcess', 'Mercadería\\nR:M-01 a 03')
                f.node('rel', 'PredefinedProcess', 'Relación\\nclientes\\nR:CL-01 y 02')
                f.node('venta', 'PredefinedProcess', 'Venta\\nR:V-01 a 04')
            else:
                f.node('merc', 'PredefinedProcess', 'Oferta R:M-01\\nExistencias\\nR:M-03')
                f.node('venta', 'PredefinedProcess', 'Ventas\\nR:V-02')
        f.node('eh_r', 'EventHubs', 'Event Hubs\\nRetail')
        f.node('pg_r', 'DatabaseForPostgresqlServers', 'PostgreSQL\\nRetail')
        f.node('lake_r', 'DataLakeStorage', 'Data Lake y\\nPower BI')
        f.node('ad_r', 'KubernetesServices', 'Adaptadores\\nen AKS')
        f.node('erp', 'Server', 'ERP/DTE\\ny WMS')
        f.node('mkp', 'Server', 'Marketplace\\ny fidelización*')
        f.node('ext', 'Users', 'Medios de pago y\\ntransportistas', 'p')
        if not e2:
            f.node('r09', 'Server', 'Núcleo Retail\\n2009', 'e1')
    f.node('x01', 'Decision', 'X-01\\npolítica\\nen ambos\\nextremos')
    with f.cluster('Filial emisora', 'emisor'):
        f.node('portal_f', 'Client', 'Portal\\nfinanciero')
        f.node('meson_f', 'Client', 'Mesón y\\nsesión\\nfinanciera')
        f.node('apim_f', 'APIManagement', 'API Management\\nEmisor')
        f.node('orig', 'PredefinedProcess', 'Originación\\nF:C-01')
        f.node('cart', 'PredefinedProcess', 'Cartera\\nF:C-02' + ('' if e2 else '\\ntramo 1'))
        f.node('evid', 'PredefinedProcess', 'Evidencia\\nF:C-03')
        f.node('eh_f', 'EventHubs', 'Event Hubs\\nEmisor')
        f.node('pg_f', 'DatabaseForPostgresqlServers', 'PostgreSQL\\nEmisor')
        f.node('lake_f', 'DataLakeStorage', 'Data Lake y\\nPower BI')
        f.node('ad_f', 'KubernetesServices', 'Adaptadores\\nEmisor')
        f.node('firma', 'Server', 'Firma y reporte\\nregulatorio', 'p')
        if not e2:
            f.node('c11', 'Server', 'Crédito 2011', 'e1')
    if e2:
        # En la vista de la Etapa 1 se omiten: la plataforma común es la misma (SD-03, 3.2.2).
        with f.cluster('Transversal\\npor ámbito', 'trans'):
            f.node('entra', 'ActiveDirectory', 'Entra ID')
            f.node('kv', 'KeyVaults', 'Key Vault')
            f.node('mon', 'AzureMonitor', 'Azure Monitor\\nOpenTelemetry')
        for t in ('entra', 'kv', 'mon'):
            f.edge('lake_f', t, 'inv')
    f.edge('apim_r', 'x01', 'inv')
    # Retail
    for c in ('pos', 'sala', 'web', 'consola'):
        f.edge(c, 'apim_r')
    if e2:
        f.edge('apim_r', 'portal_p', 'p', extra='dir="back"')
    else:
        f.edge('apim_r', 'pos14', 'e1', extra='dir="back"')
        f.edge('planillas', 'ad_r', 'e1')
    svc_r = ['merc'] + (['rel'] if e2 else []) + ['venta']
    for u, v in zip(svc_r, svc_r[1:]):
        f.edge(u, v, 'inv', extra='tailport="e", headport="w"')
    for s in svc_r:
        f.edge('apim_r', s)
        f.edge(s, 'eh_r')
        f.edge(s, 'pg_r')
    f.edge('eh_r', 'lake_r')
    f.edge('eh_r', 'ad_r')
    for p in ('erp', 'mkp'):
        f.edge('ad_r', p)
    f.edge('ad_r', 'ext', 'p')
    if not e2:
        f.edge('ad_r', 'r09', 'e1')
    # Emisor
    f.edge('portal_f', 'apim_f')
    f.edge('meson_f', 'apim_f')
    for s in ('orig', 'cart', 'evid'):
        f.edge('apim_f', s)
        f.edge(s, 'pg_f')
    f.edge('orig', 'eh_f')
    f.edge('cart', 'eh_f')
    f.edge('eh_f', 'lake_f')
    f.edge('evid', 'ad_f')
    f.edge('ad_f', 'firma', 'p')
    if not e2:
        f.edge('cart', 'ad_f')
        f.edge('ad_f', 'c11', 'e1', 'olas')
    # Frontera: único cruce y política en los dos extremos
    f.edge('venta', 'apim_f', 'auth', 'autorización\\ncompra', 'constraint="false", tailport="e", headport="w"')
    f.edge('x01', 'venta', 'x', extra='tailport="w", headport="e"')
    f.edge('x01', 'orig', 'x', extra='tailport="e", headport="w"')
    return f.code()


# --------------------------------------------------------------------------- 4.4 Tiendas
def tiendas() -> str:
    f = Fig('Ancoa · bloque Tiendas físicas' + LEGEND_BLOCK)
    with f.cluster('Retail · tienda', 'retail'):
        f.node('tiendas', 'Users', 'Tiendas físicas\\n22 tiendas')
        f.node('pos', 'Client', 'POS nuevo')
        f.node('pos14', 'Client', 'POS 2014\\ntienda por tienda', 'e1')
        f.node('local', 'LocalStore', 'L-01 caché · L-02 diario\\nL-03 sincronizador 24 h')
        f.node('moviles', 'Tablet', 'Terminales\\nmóviles')
        f.node('meson', 'Client', 'Mesón de\\natención')
        f.node('apim', 'APIManagement', 'API Management\\nRetail')
        f.node('oferta', 'PredefinedProcess', 'Oferta comercial\\nR:M-01')
        f.node('exist', 'PredefinedProcess', 'Existencias\\nR:M-03')
        f.node('ventas', 'PredefinedProcess', 'Ventas\\nR:V-02')
        f.node('posventa', 'PredefinedProcess', 'Posventa\\nR:CL-01')
        f.node('eh', 'EventHubs', 'Event Hubs\\nRetail')
        f.node('pg', 'DatabaseForPostgresqlServers', 'PostgreSQL\\nRetail')
        f.node('r09', 'Server', 'Núcleo Retail 2009\\nmesón en convivencia', 'e1')
    f.edge('tiendas', 'pos')
    f.edge('tiendas', 'pos14', 'e1')
    f.edge('tiendas', 'moviles')
    f.edge('tiendas', 'meson')
    f.edge('pos', 'local', label='sin enlace')
    f.edge('local', 'apim', label='al reconectar')
    f.edge('pos', 'apim')
    f.edge('pos14', 'apim', 'e1')
    f.edge('moviles', 'apim')
    f.edge('meson', 'apim')
    f.edge('meson', 'r09', 'e1')
    f.edge('apim', 'ventas')
    f.edge('apim', 'exist')
    f.edge('apim', 'oferta')
    f.edge('apim', 'posventa')
    f.edge('oferta', 'local', label='oferta vigente', extra='constraint="false", style="dashed"')
    for s in ('ventas', 'exist', 'oferta', 'posventa'):
        f.edge(s, 'pg')
    f.edge('ventas', 'eh')
    f.edge('exist', 'eh')
    return f.code()


# --------------------------------------------------------------------------- 4.5 Mercadería
def mercaderia() -> str:
    f = Fig('Ancoa · bloque Mercadería' + LEGEND_BLOCK, nodesep=1.0)
    with f.cluster('Retail · mercadería', 'retail'):
        f.node('comercial', 'Users', 'Equipo\\ncomercial')
        f.node('proveedores', 'Users', 'Proveedores')
        f.node('consola', 'Client', 'Consola\\ncomercial')
        f.node('portal', 'Client', 'Portal proveedor\\ncanal por validar', 'p')
        f.node('apim', 'APIManagement', 'API Management\\nRetail')
        f.node('oferta', 'PredefinedProcess', 'Oferta comercial\\nR:M-01')
        f.node('abast', 'PredefinedProcess', 'Abastecimiento\\nR:M-02')
        f.node('exist', 'PredefinedProcess', 'Existencias\\nR:M-03')
        f.node('eh', 'EventHubs', 'Event Hubs\\nRetail')
        f.node('pg', 'DatabaseForPostgresqlServers', 'PostgreSQL\\nRetail')
        f.node('canales', 'Client', 'POS, móviles\\ny web')
        f.node('etiq', 'Document', 'Etiquetas\\nen tienda')
        f.node('verif', 'Tablet', 'Verificación de\\netiquetas en sala')
        f.node('ad', 'KubernetesServices', 'Adaptadores\\nen AKS')
        f.node('wms', 'Server', 'WMS principal')
        f.node('erp', 'Server', 'ERP/DTE')
        f.node('planillas', 'Document', 'Planillas CD\\nConcepción', 'e1')
        f.node('r09', 'Server', 'Núcleo Retail\\n2009', 'e1')
    f.edge('comercial', 'consola')
    f.edge('proveedores', 'portal', 'p')
    f.edge('consola', 'apim')
    f.edge('portal', 'apim', 'p')
    f.edge('apim', 'oferta')
    f.edge('apim', 'abast')
    f.edge('apim', 'exist')
    for s in ('oferta', 'abast', 'exist'):
        f.edge(s, 'pg')
        f.edge(s, 'eh')
    f.edge('eh', 'canales', label='precio y disponible')
    f.edge('eh', 'etiq', label='cambio de precio')
    f.edge('etiq', 'verif')
    f.edge('verif', 'oferta', label='constancia', extra='constraint="false"')
    f.edge('eh', 'ad')
    f.edge('ad', 'wms')
    f.edge('ad', 'erp')
    f.edge('proveedores', 'ad', 'p', 'intercambio por acreditar', 'constraint="false"')
    f.edge('planillas', 'ad', 'e1')
    f.edge('ad', 'r09', 'e1')
    return f.code()


# --------------------------------------------------------------------------- 4.6 Venta
def venta() -> str:
    f = Fig('Ancoa · bloque Venta y cumplimiento' + LEGEND_BLOCK, nodesep=1.0)
    with f.cluster('Retail · venta y cumplimiento', None):
        f.node('clientes', 'Users', 'Clientes')
        f.node('tiendas', 'Users', 'Tiendas físicas')
        f.node('web', 'Server', 'Comercio\\nelectrónico\\n2019*')
        f.node('pos', 'Client', 'POS')
        f.node('retiro', 'Tablet', 'Retiro y despacho\\ndesde tienda')
        f.node('apim', 'APIManagement', 'API Management\\nRetail')
        f.node('pedidos', 'PredefinedProcess', 'Pedidos\\nR:V-01')
        with f.cluster('', 'fila'):
            f.node('ventas', 'PredefinedProcess', 'Ventas R:V-02 y\\ncomisiones R:V-03')
            with f.cluster('Filial emisora', 'emisor'):
                f.node('apim_f', 'APIManagement', 'API Management\\nEmisor')
        f.node('exist', 'PredefinedProcess', 'Existencias\\nR:M-03')
        f.node('mkp_s', 'PredefinedProcess', 'Marketplace\\nR:V-04')
        f.node('eh', 'EventHubs', 'Event Hubs\\nRetail')
        f.node('pg', 'DatabaseForPostgresqlServers', 'PostgreSQL\\nRetail')
        f.node('ad', 'KubernetesServices', 'Adaptadores\\nen AKS')
        f.node('erp', 'Server', 'ERP/DTE')
        f.node('wms', 'Server', 'WMS principal')
        f.node('mkp', 'Server', 'Marketplace\\n2022')
        f.node('pagos', 'Users', 'Medios de pago y\\ntransportistas', 'p')
        f.node('r09', 'Server', 'Núcleo Retail\\n2009', 'e1')
    f.edge('clientes', 'web')
    f.edge('tiendas', 'pos')
    f.edge('tiendas', 'retiro')
    f.edge('web', 'apim')
    f.edge('pos', 'apim')
    f.edge('retiro', 'apim')
    f.edge('apim', 'pedidos')
    f.edge('apim', 'ventas')
    f.edge('pedidos', 'exist', label='reserva')
    f.edge('pedidos', 'mkp_s')
    for s in ('pedidos', 'ventas', 'exist', 'mkp_s'):
        f.edge(s, 'pg')
    f.edge('pedidos', 'eh')
    f.edge('ventas', 'eh')
    f.edge('eh', 'ad')
    f.edge('mkp_s', 'ad')
    f.edge('ad', 'erp', label='DTE')
    f.edge('ad', 'wms', label='preparación')
    f.edge('ad', 'mkp')
    f.edge('ad', 'pagos', 'p')
    f.edge('ad', 'r09', 'e1')
    f.edge('ventas', 'apim_f', 'auth', 'autorización · X-01', 'tailport="w", headport="e"')
    return f.code()


# --------------------------------------------------------------------------- 4.7 Relación
def relacion() -> str:
    f = Fig('Ancoa · bloque Relación con clientes' + LEGEND_BLOCK)
    with f.cluster('Retail · relación con clientes', 'retail'):
        f.node('clientes', 'Users', 'Clientes')
        f.node('tiendas', 'Users', 'Tiendas físicas')
        f.node('vend', 'Users', 'Vendedores\\nexternos')
        f.node('web', 'Server', 'Comercio\\nelectrónico 2019*')
        f.node('meson', 'Client', 'Mesón de\\natención')
        f.node('portal', 'Client', 'Portal\\nvendedor')
        f.node('apim', 'APIManagement', 'API Management\\nRetail')
        f.node('posventa', 'PredefinedProcess', 'Posventa\\nR:CL-01')
        f.node('cli', 'PredefinedProcess', 'Clientes Retail\\nR:CL-02')
        f.node('mkp_s', 'PredefinedProcess', 'Marketplace\\nR:V-04')
        f.node('exist', 'PredefinedProcess', 'Existencias\\nR:M-03')
        f.node('pg', 'DatabaseForPostgresqlServers', 'PostgreSQL\\nRetail')
        f.node('ad', 'KubernetesServices', 'Adaptadores\\nen AKS')
        f.node('fid', 'Server', 'Fidelización\\n2017*')
        f.node('mkp', 'Server', 'Marketplace\\n2022')
        f.node('erp', 'Server', 'ERP/DTE')
        f.node('r09', 'Server', 'Núcleo Retail 2009\\ny registro actual', 'e1')
    f.node('x01', 'Decision', 'X-01 · sin datos\\nde pago en perfil')
    f.edge('clientes', 'web')
    f.edge('tiendas', 'meson')
    f.edge('vend', 'portal')
    f.edge('web', 'apim')
    f.edge('meson', 'apim')
    f.edge('portal', 'apim')
    f.edge('meson', 'r09', 'e1')
    f.edge('apim', 'posventa')
    f.edge('apim', 'cli')
    f.edge('apim', 'mkp_s')
    f.edge('posventa', 'exist', label='reintegro tras\\ninspección')
    f.edge('posventa', 'mkp_s', extra='constraint="false"')
    for s in ('posventa', 'cli', 'mkp_s', 'exist'):
        f.edge(s, 'pg')
    f.edge('cli', 'ad')
    f.edge('posventa', 'ad')
    f.edge('mkp_s', 'ad')
    f.edge('ad', 'fid', label='puntos y campañas')
    f.edge('ad', 'mkp')
    f.edge('ad', 'erp', label='nota de crédito')
    f.edge('x01', 'cli', 'x')
    return f.code()


# --------------------------------------------------------------------------- 4.8 Crédito
def credito() -> str:
    f = Fig('Ancoa · bloque Crédito y frontera' + LEGEND_BLOCK, nodesep=1.0)
    with f.cluster('', 'fila'):
        with f.cluster('Retail', 'retail'):
            f.node('caja', 'Client', 'Caja POS\\ntarjeta propia')
            f.node('apim_r', 'APIManagement', 'API Management\\nRetail')
            f.node('ventas', 'PredefinedProcess', 'Ventas\\nR:V-02')
        with f.cluster('Frontera', 'frontera'):
            f.node('x01', 'Decision', 'X-01 · ficha\\ny bitácora')
    with f.cluster('Filial emisora', 'emisor'):
        with f.cluster('', 'fila'):
            f.node('portal', 'Client', 'Portal de\\ntitulares')
            f.node('meson', 'Client', 'Mesón y sesión\\nfinanciera POS')
            f.node('apim_f', 'APIManagement', 'API Management\\nEmisor')
        f.node('orig', 'PredefinedProcess', 'Originación y\\nautorización F:C-01')
        f.node('cart', 'PredefinedProcess', 'Cartera\\nF:C-02')
        f.node('evid', 'PredefinedProcess', 'Evidencia\\nF:C-03')
        f.node('pg', 'DatabaseForPostgresqlServers', 'PostgreSQL\\nEmisor')
        f.node('eh', 'EventHubs', 'Event Hubs\\nEmisor')
        f.node('ad', 'KubernetesServices', 'Adaptadores\\nEmisor')
        f.node('firma', 'Server', 'Firma\\nelectrónica', 'p')
        f.node('reg', 'Server', 'Reporte\\nregulatorio', 'p')
        f.node('c11', 'Server', 'Crédito 2011\\ncartera por olas', 'e1')
    f.edge('caja', 'apim_r')
    f.edge('apim_r', 'ventas')
    f.edge('ventas', 'apim_f', 'auth', 'autorización de compra\\nreferencia e importe')
    f.edge('x01', 'ventas', 'x')
    f.edge('x01', 'apim_f', 'x', 'política')
    f.edge('portal', 'apim_f')
    f.edge('meson', 'apim_f')
    f.edge('apim_f', 'orig')
    f.edge('apim_f', 'cart')
    f.edge('orig', 'evid', label='verifica', extra='constraint="false"')
    f.edge('cart', 'evid', label='repactación', extra='constraint="false"')
    for s in ('orig', 'cart', 'evid'):
        f.edge(s, 'pg')
    f.edge('cart', 'eh')
    f.edge('evid', 'ad')
    f.edge('eh', 'ad', extra='constraint="false"')
    f.edge('ad', 'firma', 'p')
    f.edge('ad', 'reg', 'p')
    f.edge('ad', 'c11', 'e1', 'olas')
    return f.code()


# --------------------------------------------------------------------------- 4.9 Integración
def integracion() -> str:
    f = Fig('Ancoa · bloque Integración transversal' + LEGEND_BLOCK, nodesep=0.62, ranksep=0.12)
    with f.cluster('Retail', 'retail'):
        f.node('can_r', 'Client', 'Canales\\nRetail')
        f.node('apim_r', 'APIManagement', 'API Management\\nRetail')
        f.node('svc_r', 'PredefinedProcess', 'Servicios Retail\\ncon registro\\nde salida')
        f.node('eh_r', 'EventHubs', 'Event Hubs\\nRetail')
        f.node('ad_r', 'KubernetesServices', 'Adaptadores\\nRetail en AKS')
        f.node('plat', 'Server', 'ERP/DTE · WMS\\nmarketplace\\nfidelización')
        f.node('contra', 'Users', 'Pagos, transporte\\ny proveedores', 'p')
        f.node('leg_r', 'Server', 'Núcleo Retail\\n2009', 'e1')
        f.node('id_r', 'ActiveDirectory', 'Entra ID\\nroles Retail')
        f.node('kv_r', 'KeyVaults', 'Key Vault\\nRetail')
        f.node('mon_r', 'AzureMonitor', 'Azure Monitor\\nRetail')
    f.node('x01', 'Decision', 'X-01\\npolítica\\nen ambos\\nextremos')
    with f.cluster('Filial emisora', 'emisor'):
        f.node('can_f', 'Client', 'Canales\\nEmisor')
        f.node('apim_f', 'APIManagement', 'API Management\\nEmisor')
        f.node('svc_f', 'PredefinedProcess', 'Servicios Emisor\\ncon registro\\nde salida')
        f.node('eh_f', 'EventHubs', 'Event Hubs\\nEmisor')
        f.node('ad_f', 'KubernetesServices', 'Adaptadores\\nEmisor')
        f.node('ext_f', 'Server', 'Firma y reporte\\nregulatorio', 'p')
        f.node('leg_f', 'Server', 'Crédito 2011', 'e1')
        f.node('id_f', 'ActiveDirectory', 'Entra ID\\nroles Emisor')
        f.node('kv_f', 'KeyVaults', 'Key Vault\\nEmisor')
        f.node('mon_f', 'AzureMonitor', 'Azure Monitor\\nEmisor')
    f.edge('can_r', 'apim_r')
    f.edge('apim_r', 'svc_r', label='síncrono')
    f.edge('svc_r', 'eh_r', label='hecho\\nconfirmado')
    f.edge('eh_r', 'ad_r')
    f.edge('svc_r', 'ad_r', extra='constraint="false"')
    f.edge('ad_r', 'plat')
    f.edge('ad_r', 'contra', 'p')
    f.edge('ad_r', 'leg_r', 'e1')
    f.edge('id_r', 'apim_r', 'tel', 'token')
    f.edge('kv_r', 'ad_r', 'telc', 'secretos')
    f.edge('svc_r', 'mon_r', 'telc', 'trazas')
    f.edge('can_f', 'apim_f')
    f.edge('apim_f', 'svc_f', label='síncrono')
    f.edge('svc_f', 'eh_f', label='hecho\\nconfirmado')
    f.edge('eh_f', 'ad_f')
    f.edge('ad_f', 'ext_f', 'p')
    f.edge('ad_f', 'leg_f', 'e1')
    f.edge('id_f', 'apim_f', 'tel', 'token')
    f.edge('kv_f', 'ad_f', 'telc', 'secretos')
    f.edge('svc_f', 'mon_f', 'telc', 'trazas')
    f.edge('svc_r', 'apim_f', 'auth', 'autorización\\nde compra', 'constraint="false", tailport="e", headport="w"')
    f.edge('x01', 'svc_r', 'xc')
    f.edge('x01', 'apim_f', 'xc')
    return f.code()


TEXT_W, TEXT_H = 498.6, 600.0  # pt: carta con márgenes de 20 mm (plantilla), alto útil aproximado


def legibility(dot: Path) -> str:
    """Informa el tamaño impreso del rótulo al escalar la figura al bloque de texto."""
    import re
    match = re.search(r'bb="0,0,([\d.]+),([\d.]+)"', dot.read_text(encoding='utf-8', errors='ignore'))
    if not match:
        return 'sin bb'
    width, height = (float(v) + 2 * 0.1 * 72 for v in match.groups())  # incluye pad
    scale = min(1.0, TEXT_W / width, 0.88 * 681 / height)
    land = min(1.0, TEXT_H / width, TEXT_W / height)
    return (f'lienzo {width:.0f}x{height:.0f} pt · rótulo vertical {FS * scale:.1f} pt'
            f' · apaisado {FS * land:.1f} pt')


FIGURES = {
    '01': ('diag-04-01_arquitectura-logica-objetivo', lambda: general(2)),
    '02': ('diag-04-02_arquitectura-logica-etapa-1', lambda: general(1)),
    '04': ('diag-04-04_bloque-tiendas', tiendas),
    '05': ('diag-04-05_bloque-mercaderia', mercaderia),
    '06': ('diag-04-06_bloque-venta-y-cumplimiento', venta),
    '07': ('diag-04-07_bloque-relacion-clientes', relacion),
    '08': ('diag-04-08_bloque-credito-y-frontera', credito),
    '09': ('diag-04-09_bloque-integracion', integracion),
}


async def main(selected: list[str]) -> None:
    client_send, server_receive = anyio.create_memory_object_stream(100)
    server_send, client_receive = anyio.create_memory_object_stream(100)
    async with client_send, server_receive, server_send, client_receive:
        async with anyio.create_task_group() as group:
            group.start_soon(mcp._mcp_server.run, server_receive, server_send,
                             mcp._mcp_server.create_initialization_options())
            async with ClientSession(client_receive, client_send) as session:
                await session.initialize()
                names = {tool.name for tool in (await session.list_tools()).tools}
                if 'generate_diagram' not in names:
                    raise RuntimeError('El servidor MCP no expone generate_diagram')
                for key in selected:
                    name, build = FIGURES[key]
                    code = build()
                    (ROOT / f'{name}-mcp.py.txt').write_text(code, encoding='utf-8')
                    result = await session.call_tool(
                        'generate_diagram', {'code': code, 'filename': name, 'workspace_dir': str(ROOT)})
                    messages = [item.text for item in result.content if item.type == 'text']
                    if result.isError or any('error' in m.lower()[:40] for m in messages):
                        raise RuntimeError(f'{name}: {messages}')
                    for ext in ('png', 'drawio'):
                        src = GENERATED / f'{name}.{ext}'
                        if src.exists():
                            shutil.copyfile(src, ROOT / f'{name}.{ext}')
                        else:
                            print(f'{name}: no se generó .{ext}')
                    print(name, 'OK', legibility(GENERATED / f'{name}.dot'))
            group.cancel_scope.cancel()


if __name__ == '__main__':
    asyncio.run(main(sys.argv[1:] or list(FIGURES)))
