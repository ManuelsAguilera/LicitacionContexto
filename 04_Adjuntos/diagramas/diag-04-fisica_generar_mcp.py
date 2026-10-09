"""Genera las figuras físicas 4.13 a 4.19 de SD-04 con el MCP de diagramas.

Especificación: 05_Gestion/reportes/especificacion_diagramas_fisicos_sd04.md.
Patrón: diag-04-05_generar_bloques_mcp.py (ClientSession en memoria contra
infrastructure_diagram_mcp_server.server.mcp, herramienta generate_diagram).

Ejecutar (PowerShell, desde la raíz del repositorio):
    $env:INCLUDE='C:\\Program Files\\Graphviz\\include'; $env:LIB='C:\\Program Files\\Graphviz\\lib'
    $env:PATH += ';C:\\Program Files\\Graphviz\\bin'; $env:PYTHONUTF8='1'
    uvx --from infrastructure-diagram-mcp-server --with "mcp[cli]==1.30.0" python 04_Adjuntos\\diagramas\\diag-04-fisica_generar_mcp.py [13 14 ...]

Sin argumentos genera las siete figuras. PYTHONUTF8=1 hace que el servidor
escriba el .drawio en UTF-8 (rótulos con «≤», «²»).

El DSL de cada figura se guarda como diag-04-NN_<titulo>-mcp.py.txt; el PNG y el
.drawio se mueven de generated-diagrams/ a esta carpeta. Los iconos son productos
propuestos (Azure) o genéricos; no declaran productos existentes del Cliente.

Legibilidad (RP-05): los nodos usan etiquetas HTML de Graphviz (icono de la
librería diagrams en celda fija + texto debajo) para que el tamaño del nodo
incluya el texto; letra de 26 pt en el lienzo. Con ancho de texto A4 de 16 cm,
el texto impreso queda >= 9 pt mientras el PNG mida <= 1.747 px de ancho y
<= 2.606 px de alto (96 ppp).
"""

import asyncio
import shutil
import sys
from pathlib import Path

import anyio
# El servidor solo precarga parte de los módulos de iconos y el DSL no admite
# import: se precargan aquí los que el DSL usa con nombre completo.
import diagrams.azure.monitor  # noqa: F401
import diagrams.onprem.client  # noqa: F401
import diagrams.onprem.compute  # noqa: F401
import diagrams.onprem.network  # noqa: F401
from mcp import ClientSession
from infrastructure_diagram_mcp_server.server import mcp


ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'generated-diagrams'

# Preludio común del DSL: estilos de la tabla de convenciones de la especificación.
PRELUDE = r'''
F = "Arial"
AZ = diagrams.azure
GEN = diagrams.generic
OP = diagrams.onprem
BASE = os.path.dirname(os.path.dirname(os.path.abspath(diagrams.__file__))).replace("\\", "/")
PAL = {
    "retail": ("#1565c0", "#e8f1fb"),
    "emisor": ("#7b1fa2", "#f6ecf8"),
    "comun": ("#546e7a", "#f1f4f5"),
    "nube": ("#0078d4", "#fbfdff"),
    "dr": ("#2e7d32", "#f1f8f1"),
    "cliente": ("#6d4c41", "#f8f4f2"),
    "zona": ("#78909c", "#ffffff"),
}
def CL(label, kind="comun"):
    pen, bg = PAL[kind]
    return Cluster(label, graph_attr={"fontsize": "28", "fontname": F + " Bold", "fontcolor": pen, "pencolor": pen, "bgcolor": bg, "penwidth": "3", "style": "rounded", "margin": "14"})
def html(text):
    lines = text.replace("&", "&amp;").split("\n")
    return "<B>" + lines[0] + "</B>" + "".join("<BR/>" + line for line in lines[1:])
def N(cls, text, size=60):
    img = BASE + "/" + cls._icon_dir.replace("\\", "/") + "/" + cls._icon
    label = '<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="1"><TR><TD FIXEDSIZE="TRUE" WIDTH="%d" HEIGHT="%d"><IMG SRC="%s" SCALE="TRUE"/></TD></TR><TR><TD>%s</TD></TR></TABLE>>' % (size, size, img, html(text))
    return diagrams.Node(label, shape="plain", fixedsize="false", width="0", height="0")
def NOTA(text, kind="nota"):
    pen, bg = {"nota": ("#546e7a", "#fffde7"), "falla": ("#c62828", "#fdecea"), "dr": ("#2e7d32", "#f1f8f1")}[kind]
    return diagrams.Node('<<TABLE BORDER="0" CELLPADDING="2"><TR><TD>' + html(text) + '</TD></TR><TR><TD><FONT POINT-SIZE="10"> </FONT></TD></TR></TABLE>>', shape="box", style="rounded,filled", fixedsize="false", width="0", height="0", margin="0.25,0.16", color=pen, fillcolor=bg, penwidth="2.5")
def E(label="", **kw):
    kw.setdefault("fontsize", "26")
    kw.setdefault("fontname", F)
    kw.setdefault("penwidth", "2")
    return Edge(label=label, **kw)
DOBLE = {"color": "#1565c0:#ffffff:#1565c0", "penwidth": "2.5", "fontcolor": "#1565c0"}
AMBAR = {"color": "#e69500", "penwidth": "4.5", "fontcolor": "#9a6200"}
REPLICA = {"color": "#2e7d32", "style": "dashed", "penwidth": "3", "fontcolor": "#2e7d32"}
BLOQ = {"color": "#c62828", "penwidth": "3", "fontcolor": "#c62828", "arrowhead": "tee"}
XCONT = {"color": "#7b1fa2", "penwidth": "2.5", "fontcolor": "#7b1fa2"}
ACRED = {"style": "dashed"}
FALLA = {"color": "#c62828", "style": "dotted", "penwidth": "3", "arrowhead": "none"}
INV = {"style": "invis"}
'''

HEAD = ('with Diagram("", show=False, direction="{d}", graph_attr={{"pad": "0.25", "splines": "{s}", '
        '"nodesep": "{ns}", "ranksep": "{rs}", "fontname": "Arial", "compound": "true"}}, '
        'node_attr={{"fontname": "Arial", "fontsize": "26"}}, '
        'edge_attr={{"fontname": "Arial", "color": "#546e7a"}}):')


def head(d='TB', s='spline', ns='0.35', rs='0.7'):
    return HEAD.format(d=d, s=s, ns=ns, rs=rs)


FIGURES = {}

# ---------------------------------------------------------------- Figura 4.13
FIGURES[13] = ('arquitectura-fisica-general', head('TB', 'spline', '0.2', '0.75') + '''
    ext = N(OP.network.Internet, "EXT-01 · contrapartes externas\\nweb, marketplace, fidelización,\\npagos, transporte, proveedores")
    with CL("CLD-01 · Azure Chile Central · 3 zonas", "nube"):
        with CL("Ámbito Retail", "retail"):
            appr = N(AZ.network.VirtualNetworks, "Aplicación\\nRetail")
            datr = N(AZ.network.VirtualNetworks, "Datos y\\nanalítica Retail")
        with CL("Plataforma compartida", "comun"):
            borde = N(AZ.network.VirtualNetworks, "Borde público\\nFront Door y APIM")
            integ = N(AZ.network.VirtualNetworks, "Integración\\ny eventos")
            hub = N(AZ.network.VirtualNetworks, "Hub de red\\nVPN y ExpressRoute")
        with CL("Ámbito Filial emisora", "emisor"):
            appe = N(AZ.network.VirtualNetworks, "Aplicación\\nEmisor")
            date = N(AZ.network.VirtualNetworks, "Datos y\\nanalítica Emisor")
    with CL("CLD-02 · Azure Brazil South", "dr"):
        rec = N(AZ.migration.RecoveryServicesVaults, "Recuperación\\nde cargas nuevas\\nactivo-pasivo")
    with CL("Sitios del Cliente · on-premise", "cliente"):
        with CL("SIT-01 · 22 tiendas, 11 regiones", "cliente"):
            t8 = N(OP.client.Client, "8 tiendas\\nen centro\\ncomercial,\\ncon respaldo")
            t14 = N(OP.client.Client, "14 tiendas\\nsin respaldo:\\n6 en centro\\ncomercial y\\n8 a la calle")
        cd1 = N(OP.compute.Server, "CD-01\\nprincipal\\nWMS")
        cd2 = N(GEN.device.Tablet, "CD-02\\nConcepción\\ncaptura de\\nexistencias")
        dc2 = N(GEN.place.Datacenter, "DC-02 · sala\\nde respaldo,\\nmisma comuna")
        with CL("DC-01 · casa matriz, 140 m²", "cliente"):
            cred = N(OP.compute.Server, "Crédito 2011\\nFilial emisora")
            erp = N(OP.compute.Server, "ERP/DTE y núcleo\\nRetail 2009")
    ext << E("borde público") >> borde
    borde >> appr
    borde >> appe
    appr << E("solo X-01", constraint="false", **XCONT) >> appe
    appr >> datr
    appe >> date
    borde >> E(**INV) >> integ
    integ << E() >> hub
    appr >> E(**INV) >> integ
    datr >> E("réplica\\nRPO ≤ 15 min", **REPLICA) >> rec
    date >> E("réplica\\ncondicionada\\na residencia", **REPLICA) >> rec
    hub << E("doble enlace", **DOBLE) >> t8
    hub << E("enlace") >> t14
    hub << E("dos\\nproveedores", **DOBLE) >> cd1
    hub << E("enlace\\núnico") >> cd2
    hub << E("Express-\\nRoute\\npropuesto", minlen="2", **ACRED) >> erp
    t8 >> E(**INV) >> dc2
    t14 >> E(**INV) >> cred
    erp << E("C-16 propuesto", constraint="false", **AMBAR) >> dc2
''')

# ---------------------------------------------------------------- Figura 4.14
FIGURES[14] = ('red-y-segmentacion', head('TB', 'spline', '0.3', '0.75') + '''
    net = N(OP.network.Internet, "Internet\\nclientes y EXT-01")
    with CL("Sitios del Cliente", "cliente"):
        sit = N(GEN.network.Router, "SIT-01, CD-01, CD-02\\nVLAN por función;\\nhoy solo 9 tiendas\\nlas separan")
        dc1 = N(GEN.place.Datacenter, "DC-01\\ncasa matriz")
    er = N(AZ.network.ExpressrouteCircuits, "Circuito\\nExpressRoute")
    with CL("CLD-01 · Azure Chile Central", "nube"):
        with CL("Borde público", "comun"):
            fd = N(AZ.network.FrontDoors, "Front Door y WAF")
            apim = N(AZ.integration.APIManagement, "API Management\\nPremium")
        with CL("Hub · red virtual", "comun"):
            gw = N(AZ.network.VirtualNetworkGateways, "Gateway\\nExpressRoute y VPN")
            fw = N(AZ.network.Firewall, "Azure Firewall")
            dns = N(AZ.network.DNSPrivateZones, "DNS privado")
        with CL("Spoke compartido", "comun"):
            ic = N(AZ.network.Subnets, "Subred ingreso")
            ac = N(AZ.network.Subnets, "Subred integración\\ny operación AKS")
            dc = N(AZ.network.PrivateEndpoint, "Subred datos\\nendpoints privados")
        with CL("Spoke Retail", "retail"):
            ir = N(AZ.network.Subnets, "Subred ingreso")
            ar = N(AZ.network.Subnets, "Subred aplicación\\nAKS")
            dr = N(AZ.network.PrivateEndpoint, "Subred datos\\nendpoints privados")
        with CL("Spoke Filial emisora", "emisor"):
            ie = N(AZ.network.Subnets, "Subred ingreso")
            ae = N(AZ.network.Subnets, "Subred aplicación\\nAKS")
            de = N(AZ.network.PrivateEndpoint, "Subred datos\\nendpoints privados")
    net >> fd >> apim
    apim >> ir
    apim >> ie
    apim >> E(**INV) >> ic
    sit >> E("VPN / SD-WAN\\ndoble enlace\\ndonde existe") >> gw
    dc1 >> E("propuesto", **ACRED) >> er
    er >> E("privado") >> gw
    dc1 >> E("VPN de\\nrespaldo", **ACRED) >> gw
    gw >> fw
    gw >> E(**INV) >> dns
    ir >> ar >> dr
    ic >> ac >> dc
    ie >> ae >> de
    fw >> E(**INV) >> [ic, ir, ie]
    fw >> ac
    fw >> E("peering vía\\nfirewall") >> ar
    fw >> ae
    ar >> E("bloqueado", constraint="false", **BLOQ) >> de
    ar >> E("solo X-01, vía firewall", constraint="false", **XCONT) >> ae
''')

# ---------------------------------------------------------------- Figura 4.15
FIGURES[15] = ('ambientes-y-despliegue', head('TB', 'spline', '0.3', '0.7') + '''
    with CL("Entrega e infraestructura como código", "comun"):
        repo = N(AZ.devops.Repos, "Repositorio\\ncódigo y Terraform")
        pipe = N(AZ.devops.Pipelines, "Pipeline CI/CD\\nTerraform, revisión\\ny firma")
        acr = N(AZ.compute.ContainerRegistries, "Registro\\nde imágenes")
    with CL("CLD-01 · Azure Chile Central", "nube"):
        with CL("Desarrollo", "comun"):
            dev = N(AZ.general.Subscriptions, "Suscripción")
            kdev = N(AZ.security.KeyVaults, "Key Vault")
        with CL("QA", "comun"):
            qa = N(AZ.general.Subscriptions, "Suscripción")
            kqa = N(AZ.security.KeyVaults, "Key Vault")
        with CL("Preproducción", "comun"):
            pre = N(AZ.general.Subscriptions, "Suscripción")
            kpre = N(AZ.security.KeyVaults, "Key Vault")
        with CL("Producción Retail", "retail"):
            pr = N(AZ.general.Subscriptions, "Suscripción")
            kpr = N(AZ.security.KeyVaults, "Key Vault")
        with CL("Producción Emisor", "emisor"):
            pe = N(AZ.general.Subscriptions, "Suscripción")
            kpe = N(AZ.security.KeyVaults, "Key Vault")
    with CL("CLD-02 · Azure Brazil South · Recuperación ante Desastres", "dr"):
        with CL("DR Retail", "retail"):
            drr = N(AZ.general.Subscriptions, "Suscripción")
            kdrr = N(AZ.security.KeyVaults, "Key Vault")
        with CL("DR Emisor", "emisor"):
            dre = N(AZ.general.Subscriptions, "Suscripción")
            kdre = N(AZ.security.KeyVaults, "Key Vault")
    repo >> E(constraint="false") >> pipe
    pipe >> E(constraint="false") >> acr
    pipe >> E("despliega") >> dev
    dev >> E("promoción") >> qa
    qa >> E("promoción") >> pre
    pre >> E("aprobación") >> pr
    pre >> E("aprobación") >> pe
    pr >> E("misma IaC", **ACRED) >> drr
    pe >> E("misma IaC", **ACRED) >> dre
    pe >> E("datos de producción\\ndel Emisor: bloqueado", constraint="false", **BLOQ) >> pre
''')

# ---------------------------------------------------------------- Figura 4.16
FIGURES[16] = ('conexiones-y-contingencia', head('TB', 'spline', '0.3', '0.55') + '''
    n1 = NOTA("1 · Enlace de tienda\\ndiario local y\\noperación 24 h;\\nreconciliación al\\nvolver (F-03, F-04)", "falla")
    n2 = NOTA("2 · Enlace único\\nde CD-02\\ncaptura local durable;\\nenlace secundario\\npropuesto", "falla")
    n7 = NOTA("7 · WMS\\nprocedimiento de\\ndegradación\\npor interfaz", "falla")
    n6 = NOTA("6 · ERP/DTE\\nmodalidad fiscal\\nde contingencia\\ny conciliación", "falla")
    with CL("Sitios del Cliente", "cliente"):
        tienda = N(OP.client.Client, "SIT-01 · tienda\\nPOS y nodo local")
        cd2 = N(GEN.device.Tablet, "CD-02\\nConcepción")
        cd1 = N(OP.compute.Server, "CD-01\\nWMS")
        dc1 = N(OP.compute.Server, "DC-01\\nERP/DTE")
    with CL("CLD-01 · Azure Chile Central", "nube"):
        gw = N(AZ.network.VirtualNetworkGateways, "Gateway\\nExpressRoute y VPN")
        aks = N(AZ.compute.KubernetesServices, "AKS en tres zonas")
        eh = N(AZ.analytics.EventHubs, "Event Hubs Premium")
    n3 = NOTA("3 · ExpressRoute DC-01\\nVPN de respaldo", "falla")
    n4 = NOTA("4 · Zona de\\ndisponibilidad\\nservicios zonales en\\notra zona de\\nChile Central", "falla")
    n8 = NOTA("8 · Broker\\noutbox en\\nproductores\\ny relectura", "falla")
    n5 = NOTA("5 · Región Chile Central\\nconmutación activo-pasivo\\na Brazil South", "falla")
    with CL("CLD-02 · Azure Brazil South", "dr"):
        rec = N(AZ.migration.RecoveryServicesVaults, "Región en espera")
    n1 >> E(**FALLA) >> tienda
    n2 >> E(**FALLA) >> cd2
    n7 >> E(**FALLA) >> cd1
    n6 >> E(**FALLA) >> dc1
    tienda << E("enlace") >> gw
    cd2 << E("único") >> gw
    cd1 << E("doble", **DOBLE) >> gw
    dc1 << E("ExpressRoute\\ny VPN", **ACRED) >> gw
    gw >> E(minlen="0", **FALLA) >> n3
    gw >> aks
    aks >> E(minlen="0", **FALLA) >> n4
    aks << E() >> eh
    eh >> E(minlen="0", **FALLA) >> n8
    eh >> E("réplica\\nRPO ≤ 15 min", **REPLICA) >> rec
    eh >> E(ltail="cluster_CLD-01 · Azure Chile Central", **FALLA) >> n5
''')

# ---------------------------------------------------------------- Figura 4.17
FIGURES[17] = ('tienda-tipo', head('TB', 'spline', '0.3', '0.6') + '''
    with CL("SIT-01 · tienda tipo", "cliente"):
        with CL("VLAN cajas", "retail"):
            pos = N(OP.client.Client, "Cajas POS\\nimpresora fiscal\\ny lector")
            pago = N(GEN.device.Mobile, "Terminal de pago\\ncontraparte AS-08")
        with CL("VLAN administración", "retail"):
            term = N(GEN.device.Tablet, "Terminales\\ncompartidas")
            mov = N(GEN.device.Mobile, "Móviles\\nde sala")
            mr = N(OP.client.Client, "Mesón\\nRetail")
        with CL("Nodo local redundante ×2", "retail"):
            na = N(GEN.compute.Rack, "Nodo A\\nL-01 caché\\nL-02 diario\\nL-03 sincronizador")
            nb = N(GEN.compute.Rack, "Nodo B\\nréplica de A")
        with CL("VLAN Emisor", "emisor"):
            mf = N(OP.client.Client, "Mesón\\nfinanciero")
        with CL("VLAN video", "comun"):
            cam = NOTA("Cámaras")
        with CL("VLAN clientes", "comun"):
            wifi = N(OP.client.Users, "Wi-Fi\\nclientes")
        sw = N(GEN.network.Switch, "Switch con VLAN\\npor función", size=90)
        fw = N(GEN.network.Firewall, "Router y firewall")
    with CL("CLD-01 · Azure Chile Central", "nube"):
        hr = N(AZ.network.VirtualNetworks, "Spoke Retail")
        he = N(AZ.network.VirtualNetworks, "Spoke Emisor")
    pos >> E("operación local") >> na
    na << E("réplica", constraint="false") >> nb
    term >> E(**INV) >> mf
    mov >> E(**INV) >> cam
    mr >> E(**INV) >> wifi
    na >> E("sincronización al\\nvolver el enlace") >> sw
    nb >> sw
    pago >> E(minlen="2") >> sw
    term >> E(minlen="2") >> sw
    mov >> E(minlen="2") >> sw
    mr >> E(minlen="2") >> sw
    mf >> E("sin nodo\\nlocal Retail", **XCONT) >> sw
    cam >> sw
    wifi >> sw
    sw >> fw
    fw >> E("enlace\\nprincipal") >> hr
    fw >> E("respaldo, donde\\nexista", **ACRED) >> hr
    fw >> E("túnel del\\nEmisor", **XCONT) >> he
''')

# ---------------------------------------------------------------- Figura 4.18
FIGURES[18] = ('data-center-primario', head('TB', 'spline', '0.3', '0.6') + '''
    with CL("CLD-01 · Azure Chile Central (chilecentral), Santiago", "nube"):
        with CL("Borde e integración", "comun"):
            apim = N(AZ.integration.APIManagement, "API Management Premium\\nclásico, 3 unidades,\\nuna por zona")
            eh = N(AZ.analytics.EventHubs, "Event Hubs Premium\\nredundante entre zonas")
        with CL("Zona 1", "zona"):
            r1 = N(AZ.compute.KubernetesServices, "AKS Retail")
            e1 = N(AZ.compute.KubernetesServices, "AKS Emisor")
        with CL("Zona 2", "zona"):
            r2 = N(AZ.compute.KubernetesServices, "AKS Retail")
            e2 = N(AZ.compute.KubernetesServices, "AKS Emisor")
        with CL("Zona 3", "zona"):
            r3 = N(AZ.compute.KubernetesServices, "AKS Retail")
            e3 = N(AZ.compute.KubernetesServices, "AKS Emisor")
        with CL("Retail · datos y claves", "retail"):
            pgr = N(AZ.database.DatabaseForPostgresqlServers, "PostgreSQL\\nprimario")
            pgr2 = N(AZ.database.DatabaseForPostgresqlServers, "PostgreSQL\\nen espera")
            redis = N(AZ.database.CacheForRedis, "Cache\\nfor Redis")
            dlr = N(AZ.storage.DataLakeStorage, "Data Lake\\nGen2")
            kvr = N(AZ.security.KeyVaults, "Key Vault")
        with CL("Filial emisora · datos y claves", "emisor"):
            pge = N(AZ.database.DatabaseForPostgresqlServers, "PostgreSQL\\nprimario")
            pge2 = N(AZ.database.DatabaseForPostgresqlServers, "PostgreSQL\\nen espera")
            dle = N(AZ.storage.DataLakeStorage, "Data Lake\\nGen2")
            kve = N(AZ.security.KeyVaults, "Key Vault")
        with CL("Identidad, analítica, observabilidad y respaldo", "comun"):
            entra = N(AZ.identity.ActiveDirectory, "Entra ID")
            pbi = N(AZ.analytics.PowerBiEmbedded, "Power BI\\npor ámbito")
            mon = N(diagrams.azure.monitor.Monitor, "Azure\\nMonitor")
            law = N(diagrams.azure.monitor.LogAnalyticsWorkspaces, "Log\\nAnalytics")
            bk = N(AZ.migration.RecoveryServicesVaults, "Copia de\\nseguridad")
    with CL("DC-01 · casa matriz, 140 m² · convivencia", "cliente"):
        erp = N(OP.compute.Server, "ERP/DTE y núcleo\\nRetail 2009")
        cred = N(OP.compute.Server, "Crédito 2011")
    apim >> [r1, r2, r3]
    eh >> E(**INV) >> [e1, e2, e3]
    r1 >> E("endpoint\\nprivado", style="dotted") >> pgr
    r2 >> E(**INV) >> pgr2
    e2 >> E(**INV) >> pge
    e3 >> E("endpoint\\nprivado", style="dotted") >> pge2
    pgr << E("HA entre\\nzonas", constraint="false") >> pgr2
    pge << E("HA entre\\nzonas", constraint="false") >> pge2
    pgr >> E(**INV) >> redis
    pgr2 >> E(**INV) >> dlr
    pgr2 >> E(**INV) >> kvr
    pge >> E(**INV) >> dle
    pge2 >> E(**INV) >> kve
    redis >> E(**INV) >> entra
    dlr >> E(**INV) >> pbi
    dle >> E(**INV) >> law
    kve >> E(**INV) >> bk
    pbi >> E(**INV) >> erp
    law >> E(**INV) >> cred
    mon << E("ExpressRoute · por acreditar", ltail="cluster_CLD-01 · Azure Chile Central (chilecentral), Santiago", **ACRED) >> erp
''')

# ---------------------------------------------------------------- Figura 4.19
FIGURES[19] = ('data-center-secundario', head('TB', 'spline', '0.6', '0.55') + '''
    fd = N(AZ.network.FrontDoors, "Front Door global")
    with CL("CLD-01 · Chile Central · activo", "nube"):
        apa = N(AZ.integration.APIManagement, "API Management\\nPremium")
        aka = N(AZ.compute.KubernetesServices, "AKS")
        eha = N(AZ.analytics.EventHubs, "Event Hubs\\nprimario")
        with CL("Retail", "retail"):
            pgra = N(AZ.database.DatabaseForPostgresqlServers, "PostgreSQL")
            sta = N(AZ.storage.DataLakeStorage, "Almacenamiento")
        with CL("Emisor", "emisor"):
            pgea = N(AZ.database.DatabaseForPostgresqlServers, "PostgreSQL")
    with CL("CLD-02 · Brazil South · pasivo", "dr"):
        apb = N(AZ.integration.APIManagement, "Gateway APIM\\nadicional")
        akb = N(AZ.compute.KubernetesServices, "AKS en espera\\no por IaC")
        ehb = N(AZ.analytics.EventHubs, "Event Hubs\\nsecundario")
        with CL("Retail ", "retail"):
            pgrb = N(AZ.database.DatabaseForPostgresqlServers, "Réplica\\nde lectura")
            stb = N(AZ.storage.DataLakeStorage, "Almacenamiento\\nreplicado")
        with CL("Emisor ", "emisor"):
            pgeb = N(AZ.database.DatabaseForPostgresqlServers, "Réplica\\nde lectura")
        kvb = N(AZ.security.KeyVaults, "Key Vault")
        bkb = N(AZ.migration.RecoveryServicesVaults, "Bóveda de\\nrespaldo")
    with CL("Sitios del Cliente", "cliente"):
        dc1 = N(GEN.place.Datacenter, "DC-01\\ncasa matriz")
        dc2 = N(GEN.place.Datacenter, "DC-02 · sala\\nde respaldo; no\\nbasta como única\\nrecuperación")
    obj = NOTA("RTO ≤ 4 h · RPO ≤ 15 min\\nservicios críticos (RT-07.04)\\nactivo-pasivo; conmutación\\nensayada dos veces al año", "dr")
    fd >> E("activo") >> apa
    fd >> E("conmutación", **ACRED) >> apb
    apa >> E(**INV) >> aka >> E(**INV) >> eha >> E(**INV) >> pgra >> E(**INV) >> sta >> E(**INV) >> pgea
    apb >> E(**INV) >> akb >> E(**INV) >> ehb >> E(**INV) >> pgrb >> E(**INV) >> stb >> E(**INV) >> pgeb >> E(**INV) >> kvb
    kvb >> E(**INV) >> bkb
    aka >> E("misma IaC", constraint="false", **ACRED) >> akb
    eha >> E("geo-replicación\\nretraso < 15 min", constraint="false", **REPLICA) >> ehb
    pgra >> E("réplica entre regiones\\nRPO ≤ 15 min", constraint="false", **REPLICA) >> pgrb
    sta >> E("réplica", constraint="false", **REPLICA) >> stb
    pgea >> E("condicionada a residencia", constraint="false", **REPLICA) >> pgeb
    pgea >> E(**INV) >> dc1
    dc1 << E("C-16 propuesto", constraint="false", **AMBAR) >> dc2
    pgea >> E(**INV) >> dc2
''')


def dsl(number: int) -> str:
    return PRELUDE.strip() + '\n' + FIGURES[number][1].strip('\n') + '\n'


async def main(numbers) -> None:
    client_send, server_receive = anyio.create_memory_object_stream(100)
    server_send, client_receive = anyio.create_memory_object_stream(100)
    async with client_send, server_receive, server_send, client_receive:
        async with anyio.create_task_group() as group:
            group.start_soon(mcp._mcp_server.run, server_receive, server_send, mcp._mcp_server.create_initialization_options())
            async with ClientSession(client_receive, client_send) as session:
                await session.initialize()
                for number in numbers:
                    slug = FIGURES[number][0]
                    name = f'diag-04-{number}_{slug}'
                    code = dsl(number)
                    (ROOT / f'{name}-mcp.py.txt').write_text(code, encoding='utf-8')
                    result = await session.call_tool('generate_diagram', {'code': code, 'filename': name, 'workspace_dir': str(ROOT)})
                    messages = [item.text for item in result.content if item.type == 'text']
                    if result.isError or any('"status":"error"' in m.replace(' ', '') or m.startswith('Error') for m in messages):
                        raise RuntimeError(f'{name}: {messages}')
                    for ext in ('png', 'drawio'):
                        src = OUT / f'{name}.{ext}'
                        if not src.exists():
                            raise RuntimeError(f'{name}: falta {src.name}')
                        shutil.move(str(src), str(ROOT / src.name))
                    dot = OUT / f'{name}.dot'
                    if dot.exists():
                        dot.unlink()
                    print(name, 'OK')
            group.cancel_scope.cancel()


if __name__ == '__main__':
    selected = [int(arg) for arg in sys.argv[1:]] or sorted(FIGURES)
    asyncio.run(main(selected))
