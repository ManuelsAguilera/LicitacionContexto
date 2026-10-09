"""Generate focused logical views through andrewmoshu's diagram MCP server.

Run with /workspace/.uv-tools/infrastructure-diagram-mcp-server/bin/python.
Product icons are architecture candidates, not declared existing products.
"""

import asyncio
from pathlib import Path

import anyio
from mcp import ClientSession
from infrastructure_diagram_mcp_server.server import mcp


ROOT = Path(__file__).resolve().parent
HEADER = 'with Diagram("Ancoa · {title} · Etapa {stage}", show=False, direction="LR", graph_attr={{"splines":"spline", "nodesep":"0.55", "ranksep":"0.85", "pad":"0.25", "bgcolor":"white", "fontname":"DejaVu Sans", "fontsize":"18"}}, node_attr={{"fontname":"DejaVu Sans", "fontsize":"12"}}, edge_attr={{"color":"#607d8b", "arrowsize":"0.6"}}):'


def source(block: str, stage: int) -> str:
    title = {
        'tienda': 'Tiendas Físicas',
        'mercaderia': 'Mercadería',
        'venta': 'Venta y cumplimiento',
        'relacion': 'Relación con clientes',
        'credito': 'Crédito y frontera',
        'integracion': 'Integración transversal',
    }[block]
    lines = [HEADER.format(title=title, stage=stage)]
    add = lines.extend

    if block == 'tienda':
        add([
            '    tiendas = Users("Tiendas Físicas")',
            '    pos = Client("POS nuevo")',
            '    local = Database("Cola local · 24 h")',
            '    moviles = Mobile("Móviles sala")',
            '    atencion = Client("Mesón atención")',
            '    gateway = Kong("Gateway Retail")',
            '    eventos = Kafka("Eventos Retail")',
            '    ventas = PredefinedProcess("Ventas")',
            '    existencias = PredefinedProcess("Existencias")',
            '    datos = PostgreSQL("BD Ventas")',
            '    tiendas >> pos >> local >> gateway >> ventas >> datos',
            '    tiendas >> moviles >> gateway >> existencias',
            '    tiendas >> atencion >> gateway',
            '    ventas >> eventos >> existencias',
        ])
        if stage == 1:
            add([
                '    pos_antiguo = Client("POS 2014")',
                '    tiendas >> pos_antiguo >> gateway',
            ])
        else:
            add([
                '    posventa = PredefinedProcess("Posventa")',
                '    gateway >> posventa',
            ])

    elif block == 'mercaderia':
        add([
            '    comercial = Users("Equipo comercial")',
            '    oferta = PredefinedProcess("Oferta comercial")',
            '    existencias = PredefinedProcess("Existencias")',
            '    eventos = Kafka("Eventos Retail")',
            '    datos = PostgreSQL("BD por servicio")',
            '    pos = Client("POS y móviles")',
            '    web = Client("Web y app")',
            '    etiquetas = Document("Etiquetas tienda")',
            '    gestion = Client("Gestión comercial")',
            '    gateway = Kong("Gateway Retail")',
            '    wms = Server("WMS principal")',
            '    lotes = Document("Archivos y lotes")',
            '    concepcion = Document("Carga Concepción")',
            '    comercial >> gestion >> gateway >> oferta >> eventos >> [pos, web, etiquetas]',
            '    oferta >> datos',
            '    wms >> lotes >> existencias >> datos',
            '    concepcion >> lotes',
            '    existencias >> eventos',
        ])
        if stage == 1:
            add([
                '    legado = Server("Retail 2009")',
                '    legado >> lotes',
            ])
        else:
            add([
                '    abastecimiento = PredefinedProcess("Abastecimiento")',
                '    proveedores = Users("Proveedores")',
                '    proveedores >> lotes >> abastecimiento',
                '    abastecimiento >> lotes',
                '    abastecimiento >> datos',
            ])

    elif block == 'venta':
        add([
            '    clientes = Users("Clientes")',
            '    web = Client("Web y app")',
            '    tiendas = Users("Tiendas Físicas")',
            '    pos = Client("POS")',
            '    gateway = Kong("Gateway Retail")',
            '    ventas = PredefinedProcess("Ventas")',
            '    pagos = Server("Medios de pago")',
            '    erp = Server("ERP/DTE")',
            '    adaptador_pago = InputOutput("Adaptador pago")',
            '    adaptador_erp = InputOutput("Adaptador ERP")',
            '    eventos = Kafka("Eventos Retail")',
            '    datos = PostgreSQL("BD Ventas")',
            '    clientes >> web',
            '    tiendas >> pos >> gateway >> ventas >> datos',
            '    ventas >> adaptador_pago >> pagos',
            '    ventas >> adaptador_erp >> erp',
            '    ventas >> eventos',
        ])
        if stage == 1:
            add([
                '    comercio = Server("E-commerce 2019")',
                '    retail = Server("Retail 2009")',
                '    adaptador = InputOutput("Adaptador legado")',
                '    web >> comercio >> gateway >> adaptador >> retail',
            ])
        else:
            add([
                '    pedidos = PredefinedProcess("Pedidos")',
                '    existencias = PredefinedProcess("Existencias")',
                '    tienda = Client("Retiro / despacho tienda")',
                '    wms = Server("WMS principal")',
                '    transporte = Users("Transportistas")',
                '    marketplace = PredefinedProcess("Marketplace")',
                '    plataforma = Server("Marketplace 2022")',
                '    comercio = Server("E-commerce 2019")',
                '    adaptador_logistico = InputOutput("Adaptador logístico")',
                '    adaptador_mp = InputOutput("Adaptador marketplace")',
                '    web >> comercio >> gateway',
                '    gateway >> pedidos >> existencias',
                '    pedidos >> [tienda, marketplace]',
                '    pedidos >> adaptador_logistico >> [wms, transporte]',
                '    marketplace >> adaptador_mp >> plataforma',
                '    pedidos >> eventos',
            ])

    elif block == 'relacion':
        add([
            '    clientes = Users("Clientes")',
            '    web = Client("Web y app")',
            '    tiendas = Users("Tiendas Físicas")',
            '    meson = Client("Mesón atención")',
            '    gateway = Kong("Gateway Retail")',
            '    fidelizacion = Server("Fidelización 2017")',
            '    clientes >> web >> gateway',
            '    tiendas >> meson >> gateway',
        ])
        if stage == 1:
            add([
                '    legado = Document("Registro actual")',
                '    adaptador = InputOutput("Adaptador legado")',
                '    gateway >> adaptador >> [legado, fidelizacion]',
            ])
        else:
            add([
                '    posventa = PredefinedProcess("Posventa")',
                '    clientes_r = PredefinedProcess("Clientes Retail")',
                '    datos = PostgreSQL("BD por servicio")',
                '    vendedor = Users("Vendedores externos")',
                '    portal = Client("Portal vendedor")',
                '    plataforma = Server("Marketplace 2022")',
                '    adaptador = InputOutput("Adaptadores")',
                '    gateway >> [posventa, clientes_r]',
                '    [posventa, clientes_r] >> datos',
                '    clientes_r >> adaptador >> fidelizacion',
                '    vendedor >> portal >> gateway',
                '    posventa >> adaptador >> plataforma',
            ])

    elif block == 'credito':
        add([
            '    titulares = Users("Titulares")',
            '    portal = Client("Portal financiero")',
            '    personal = Users("Personal financiero")',
            '    meson = Client("Mesón financiero")',
            '    terminal = Client("Terminal financiero")',
            '    caja = Client("Caja Retail")',
            '    politica = Firewall("X-01")',
            '    retail = Kong("Gateway Retail")',
            '    emisor = Kong("Gateway Emisor")',
            '    originacion = PredefinedProcess("Originación")',
            '    evidencia = PredefinedProcess("Evidencia")',
            '    cartera = PredefinedProcess("Cartera")',
            '    datos = PostgreSQL("BD Emisor")',
            '    firma = Server("Firma electrónica")',
            '    adaptador_firma = InputOutput("Adaptador firma")',
            '    titulares >> portal >> emisor',
            '    personal >> meson >> emisor',
            '    meson >> terminal >> emisor',
            '    caja >> retail >> Edge(label="autorizar", color="#4b7ca4") >> emisor',
            '    politica >> Edge(label="política", style="dashed", constraint="false") >> emisor',
            '    emisor >> originacion >> evidencia >> datos',
            '    evidencia >> adaptador_firma >> firma',
            '    emisor >> cartera >> datos',
            '    cartera >> Edge(style="dashed", label="repactación", constraint="false") >> evidencia',
        ])
        if stage == 1:
            add([
                '    legado = Server("Crédito 2011")',
                '    cartera >> Edge(label="olas") >> legado',
            ])
    elif block == 'integracion':
        add([
            '    canales = Client("Canales Retail")',
            '    gateway = Kong("Gateway Retail")',
            '    eventos = Kafka("Eventos Retail")',
            '    adaptadores = NiFi("Adaptadores y lotes")',
            '    retail = PredefinedProcess("Servicios Retail")',
            '    terceros = Server("ERP · WMS · Marketplace")',
            '    emisor = Kong("Gateway Emisor")',
            '    politica = Firewall("X-01")',
            '    financiera = PredefinedProcess("Servicios Emisor")',
            '    observabilidad = Grafana("Observabilidad")',
            '    canales >> gateway >> retail >> eventos',
            '    eventos >> adaptadores >> terceros',
            '    gateway >> Edge(constraint="false") >> adaptadores',
            '    gateway >> Edge(label="autorización", color="#4b7ca4") >> emisor >> financiera',
            '    politica >> Edge(style="dashed", constraint="false") >> gateway',
            '    politica >> Edge(style="dashed", constraint="false") >> emisor',
            '    eventos >> Edge(style="dotted", constraint="false") >> observabilidad',
            '    emisor >> Edge(style="dotted", constraint="false") >> observabilidad',
        ])
        if stage == 1:
            add([
                '    legados = Server("Retail 2009 · Crédito 2011")',
                '    adaptadores >> legados',
            ])
        else:
            add([
                '    proveedores = Users("Proveedores y transporte")',
                '    proveedores >> adaptadores',
            ])
    return '\n'.join(lines)


async def main() -> None:
    client_send, server_receive = anyio.create_memory_object_stream(100)
    server_send, client_receive = anyio.create_memory_object_stream(100)
    async with client_send, server_receive, server_send, client_receive:
        async with anyio.create_task_group() as group:
            group.start_soon(mcp._mcp_server.run, server_receive, server_send, mcp._mcp_server.create_initialization_options())
            async with ClientSession(client_receive, client_send) as session:
                await session.initialize()
                await session.call_tool('get_diagram_examples', {'diagram_type': 'onprem'})
                catalogs = [await session.call_tool('list_icons', {'provider_filter': provider}) for provider in ('onprem', 'generic', 'programming')]
                catalog = ''.join(str(result.structuredContent) + ''.join(item.text for item in result.content if item.type == 'text') for result in catalogs)
                needed = ('Users', 'Client', 'Mobile', 'Database', 'Document', 'InputOutput', 'PredefinedProcess', 'Server', 'Firewall', 'Kong', 'Kafka', 'PostgreSQL', 'NiFi', 'Grafana')
                missing = [name for name in needed if name not in catalog]
                if missing:
                    raise RuntimeError(f'Icons absent from MCP catalog: {missing}')
                for block in ('tienda', 'mercaderia', 'venta', 'relacion', 'credito', 'integracion'):
                    for stage in (1, 2):
                        name = f'diag-04-05_{block}_etapa-{stage}-mcp'
                        code = source(block, stage)
                        (ROOT / f'{name}.py.txt').write_text(code + '\n')
                        result = await session.call_tool('generate_diagram', {'code': code, 'filename': name, 'workspace_dir': str(ROOT)})
                        messages = [item.text for item in result.content if item.type == 'text']
                        if result.isError or any(message.startswith('Error:') for message in messages):
                            raise RuntimeError(f'{name}: {messages}')
                        print(name, 'OK')
            group.cancel_scope.cancel()


if __name__ == '__main__':
    asyncio.run(main())
