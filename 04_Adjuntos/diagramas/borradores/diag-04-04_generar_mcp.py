"""Generate the two logical views with andrewmoshu's diagram MCP server.

Run with /workspace/.uv-tools/infrastructure-diagram-mcp-server/bin/python.
The MCP server writes PNG, DOT, and editable draw.io artifacts in generated-diagrams/.
"""

import asyncio
from pathlib import Path

import anyio
from mcp import ClientSession
from infrastructure_diagram_mcp_server.server import mcp


ROOT = Path(__file__).resolve().parent


def source(stage: int) -> str:
    retail = [
        ("oferta", "Oferta comercial"),
        ("existencias", "Existencias"),
        ("ventas", "Ventas"),
    ]
    if stage == 2:
        retail = [
            ("mercaderia", "Oferta · Abastecimiento · Existencias"),
            ("operaciones", "Pedidos · Ventas · Comisiones · Marketplace"),
            ("relacion", "Posventa · Clientes Retail"),
        ]
    lines = [
        f'with Diagram("Ancoa · arquitectura lógica · Etapa {stage} · mes {16 if stage == 1 else 21}", show=False, direction="LR", graph_attr={{"splines":"spline", "nodesep":"0.28", "ranksep":"0.50", "pad":"0.16", "bgcolor":"white", "fontname":"DejaVu Sans", "fontsize":"18"}}, node_attr={{"fontname":"DejaVu Sans", "fontsize":"13"}}, edge_attr={{"color":"#607d8b", "arrowsize":"0.6"}}):',
        '    with Cluster("Retail", graph_attr={"bgcolor":"#f4faf7", "color":"#79a895", "style":"rounded", "fontname":"DejaVu Sans", "fontsize":"17"}):',
        '        tiendas = Users("Tiendas Físicas")',
        '        clientes = Users("Clientes")',
        '        cd = Datacenter("Centros de distribución")',
        '        pos = Client("POS nuevo")',
        '        cola = Database("Cola local · 24 h")',
        '        web = Client("Web y app")',
        '        atencion = Client("Mesón atención")',
        '        moviles = Mobile("Móviles sala")',
        '        operacion = Client("Operación CD")',
        '        concepcion = Document("Carga Concepción")',
        '        nube = Internet("Plataforma Retail")',
        '        api = InputOutput("API síncrona")',
        '        eventos = MultipleDocuments("Eventos persistentes")',
        '        lotes = Document("Archivos y lotes")',
        '        datos_r = Database("BD por servicio")',
        '        analitica_r = Database("Analítica Retail")',
        '        erp = Server("ERP/DTE")',
        '        wms = Server("WMS principal")',
        '        plataforma_mp = Server("Marketplace 2022")',
        '        fidelizacion = Server("Fidelización")',
        '        pagos = Server("Medios de pago")',
    ]
    if stage == 1:
        lines += [
            '        pos_legacy = Client("POS 2014")',
            '        retail_legacy = Server("Retail 2009")',
        ]
    for var, label in retail:
        wrapped = label.replace(' · ', r'\n') if stage == 2 else label
        lines.append(f'        {var} = PredefinedProcess("{wrapped}")')
    lines += [
        '    with Cluster("Filial emisora", graph_attr={"bgcolor":"#f9f6fb", "color":"#a791ba", "style":"rounded", "fontname":"DejaVu Sans", "fontsize":"17"}):',
        '        titulares = Users("Titulares")',
        '        personal_f = Users("Personal financiero")',
        '        portal_f = Client("Portal financiero")',
        '        meson_f = Client("Mesón financiero")',
        '        terminal_pago = Client("Terminal de pago")',
        '        nube_f = Internet("Plataforma Emisor")',
        '        api_f = InputOutput("API · eventos · lotes")',
        '        originacion = PredefinedProcess("Originación de crédito")',
        '        cartera = PredefinedProcess("Cartera' + (' · por olas' if stage == 1 else '') + '")',
        '        evidencia = PredefinedProcess("Evidencia financiera")',
        '        datos_f = Database("BD Emisor")',
        '        analitica_f = Database("Analítica Emisor")',
    ]
    if stage == 1:
        lines.append('        credito_legacy = Server("Crédito 2011")')
    lines += [
        '    politica = Firewall("X-01 · cruces")',
        '    tiendas >> pos >> cola >> nube',
        '    clientes >> web >> nube',
        '    tiendas >> atencion >> nube',
        '    tiendas >> moviles >> nube',
        '    cd >> operacion >> nube',
        '    cd >> concepcion >> lotes',
        '    nube >> api',
        '    api >> eventos',
        '    api >> lotes >> [erp, wms, plataforma_mp, fidelizacion]',
        '    api >> pagos',
        '    titulares >> portal_f >> nube_f >> api_f',
        '    personal_f >> meson_f >> nube_f',
        '    meson_f >> terminal_pago >> nube_f',
        '    api_f >> [originacion, cartera, evidencia]',
        '    [originacion, cartera, evidencia] >> datos_f',
        '    api_f >> analitica_f',
        '    api >> analitica_r',
        '    politica >> Edge(color="#b99048", style="dashed", label="política", constraint="false") >> api',
        '    politica >> Edge(color="#b99048", style="dashed", label="política", constraint="false") >> api_f',
        '    api >> Edge(color="#4b7ca4", style="dashed", label="autorización", constraint="false") >> api_f',
    ]
    if stage == 1:
        lines += [
            '    tiendas >> pos_legacy >> nube',
            '    lotes >> retail_legacy',
            '    api_f >> credito_legacy',
            '    api >> ventas',
        ]
    else:
        lines.append('    api >> operaciones')
    # Three business-family icons represent the nine Stage 2 services; stores remain service-owned.
    for var, _ in retail:
        lines.append(f'    eventos >> {var} >> datos_r')
    return "\n".join(lines)


async def main() -> None:
    client_send, server_receive = anyio.create_memory_object_stream(100)
    server_send, client_receive = anyio.create_memory_object_stream(100)
    async with client_send, server_receive, server_send, client_receive:
        async with anyio.create_task_group() as group:
            group.start_soon(
                mcp._mcp_server.run,
                server_receive,
                server_send,
                mcp._mcp_server.create_initialization_options(),
            )
            async with ClientSession(client_receive, client_send) as session:
                await session.initialize()
                names = {tool.name for tool in (await session.list_tools()).tools}
                if "generate_diagram" not in names:
                    raise RuntimeError("The MCP server did not expose generate_diagram")
                await session.call_tool("get_diagram_examples", {"diagram_type": "onprem"})
                await session.call_tool("list_icons", {"provider_filter": "onprem"})
                for stage in (1, 2):
                    name = f"diag-04-04{'a' if stage == 1 else 'b'}_arquitectura-logica-etapa-{stage}-mcp"
                    code = source(stage)
                    (ROOT / f"{name}.py.txt").write_text(code + "\n")
                    result = await session.call_tool(
                        "generate_diagram",
                        {"code": code, "filename": name, "workspace_dir": str(ROOT)},
                    )
                    messages = [item.text for item in result.content if item.type == "text"]
                    print("\n".join(messages))
                    if result.isError or any(message.startswith("Error:") for message in messages):
                        raise RuntimeError(f"MCP generation failed for stage {stage}")
            group.cancel_scope.cancel()


if __name__ == "__main__":
    asyncio.run(main())
