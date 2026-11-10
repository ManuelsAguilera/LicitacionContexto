"""Genera las especificaciones JSON de las figuras físicas del SD-04 (catálogo diagramas-ancoa).

Fuente de los elementos: registro-diseno-fisica/01_nodos.md (inventario completo) y el SD-04.
Regla del usuario (09-11-2026): sin IDs E-NN en las líneas y sin omitir elementos del inventario.
Cada figura respeta el máximo de nodos del estilo; lo que no cabe se reparte en otra figura.

Uso:  python3 generar_laminas.py [ID ...]   (sin argumentos genera todas)
"""
import json
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
FUENTE = "elaboración propia a partir del registro de diseño de la física y del Subdocumento 4."


class Lam:
    def __init__(self, clave, estilo, titulo, fuente=FUENTE):
        self.clave, self.estilo, self.titulo, self.fuente = clave, estilo, titulo, fuente
        self.g, self.n, self.e = [], [], []

    def G(self, id_, et, tipo, disp="fila", padre=None, frente=None, columnas=None):
        d = {"id": id_, "etiqueta": et, "tipo": tipo, "disposicion": disp}
        if padre:
            d["padre"] = padre
        if frente:
            d["frente"] = frente
        if columnas:
            d["columnas"] = columnas
        self.g.append(d)

    def N(self, id_, et, icono, grupo, estado=None, insignia=None):
        d = {"id": id_, "etiqueta": et, "icono": icono, "grupo": grupo}
        if estado:
            d["estado"] = estado
        if insignia is not None:
            d["insignia"] = insignia
        self.n.append(d)

    def E(self, a, b, sem, et):
        self.e.append({"de": a, "a": b, "semantica": sem, "etiqueta": et})

    def spec(self):
        return {"estilo": self.estilo, "figura": "4.99", "titulo": self.titulo, "fuente": self.fuente,
                "grupos": self.g, "nodos": self.n, "enlaces": self.e}


FRENTES = (("r", "Retail", "retail"), ("x", "Control de cruces", "frontera"), ("f", "Filial emisora", "emisor"))


# ---------------------------------------------------------------- A · topología general (F1)
def fig_a():
    L = Lam("A_topologia-general", "F1", "Arquitectura física: sitios, conexiones y regiones")
    L.G("cli", "Sitios del Cliente", "sitio_cliente", "columna")
    L.N("tie", "Tienda tipo ×22\n(+1 de laboratorio en Preproducción)", "sitio", "cli")
    L.N("cd1", "Centro de distribución principal\n(CD-01)", "sitio", "cli")
    L.N("cd2", "Centro de distribución de Concepción\n(CD-02)", "sitio", "cli")
    L.N("dc1", "Centro de datos de casa matriz\n(DC-01)", "centro_datos", "cli")
    L.N("dc2", "Sala de respaldo de casa matriz\n(DC-02)", "centro_datos", "cli")
    L.G("con", "Conexiones", "seccion", "columna")
    L.N("op", "Operadores fijos A y B\n(accesos por sitio)", "router", "con")
    L.N("mov", "Red móvil 4G/5G\n(respaldo de tiendas y centros)", "antena_lte", "con")
    L.N("usu", "Clientes y titulares\n(Internet)", "personas", "con")
    L.N("afd", "Azure Front Door\n(perfil de Retail y de la filial)", "front_door", "con")
    L.G("cl", "Azure Chile Central · producción en 3 zonas", "nube_azure", "columna")
    for p, nom, fr in FRENTES:
        L.G("cl_" + p, nom, "ambito", "fila", "cl", fr)
    L.N("cl_rn", "Red central, AKS\ny datos de Retail", "vnet", "cl_r")
    L.N("cl_xn", "Red central, AKS y bitácora\ndel Control de cruces", "vnet", "cl_x")
    L.N("cl_fn", "Red central, AKS\ny datos de la filial", "vnet", "cl_f")
    L.G("br", "Azure Brazil South · recuperación activo-pasivo templado", "nube_azure", "columna")
    L.N("br_n", "Copia en espera\nde los tres frentes", "aks", "br")
    L.N("sent", "Microsoft Sentinel ×3\n(operación habitual)", "sentinel", "br")
    L.G("glo", "Servicios globales", "seccion", "columna")
    L.N("dnsp", "Azure DNS público", "dns", "glo")
    L.N("ide", "Entra ID, External ID\ne Intune", "entra_id", "glo")
    L.N("dev", "Azure Pipelines\n(agentes efímeros)", "devops", "glo")
    L.N("apc", "Azure API Center ×2\n(East US)", "api_management", "glo")
    L.G("ext", "Plataformas conservadas y contrapartes", "seccion", "columna")
    L.N("erp", "ERP y facturación\nelectrónica", "servidor", "ext", "por_acreditar")
    L.N("wms", "WMS de 2016\n(centro principal)", "servidor", "ext", "por_acreditar")
    L.N("leg", "Sistema central de retail (2009)\ny plataforma de crédito (2011)", "servidor", "ext", "por_acreditar")
    L.N("ter", "Comercio electrónico, marketplace,\nfidelización, pagos, firma,\nproveedores y plataforma publicitaria", "internet", "ext")
    L.E("cli", "op", "enlace", "accesos fijos")
    L.E("cli", "mov", "respaldo", "respaldo móvil")
    L.E("op", "cl", "vpn", "un túnel por negocio")
    L.E("usu", "afd", "enlace", "HTTPS")
    L.E("afd", "cl", "enlace", "punto privado por negocio")
    L.E("cl_rn", "cl_xn", "trafico_inspeccionado", "autorización de compra")
    L.E("cl_xn", "cl_fn", "trafico_inspeccionado", "consulta de cupo")
    L.E("cl", "br", "replica", "réplica asíncrona")
    return L


# ---------------------------------------------------------------- B1 · red y entrada (F2)
def fig_b1():
    L = Lam("B1_red-chile-central", "F2", "Red y entrada de Azure Chile Central por frente")
    L.G("ext", "Entrada desde fuera de la región", "seccion", "columna")
    L.N("pe_br", "Punto privado de tránsito\nen Brazil South (prioridad 1)", "private_link", "ext")
    L.N("afd_r", "Front Door de Retail", "front_door", "ext")
    L.N("pe_us", "Punto privado de tránsito\nen East US (prioridad 2,\nal mismo Application Gateway)", "private_link", "ext")
    L.N("afd_f", "Front Door de la filial\n(mismo recorrido, con\nsus puntos privados)", "front_door", "ext")
    L.N("dnsp", "Azure DNS público", "dns", "ext")
    L.N("ddos", "Azure DDoS Protection\n(IP públicas que queden)", "ddos", "ext")
    L.G("cl", "Azure Chile Central · producción en 3 zonas", "nube_azure", "columna")
    for p, nom, fr in FRENTES:
        L.G(p, nom, "ambito", "fila", "cl", fr)
        L.G(p + "_hub", "Red central", "subred", "rejilla", p, fr, 3)
        L.G(p + "_app", "Red de aplicaciones", "subred", "rejilla", p, fr, 2)
        L.G(p + "_dat", "Red de datos", "subred", "rejilla", p, fr, 1)
    for p in ("r", "f"):
        L.N(p + "_vpn", "VPN Gateway\n(túneles de los sitios)", "vpn_gateway", p + "_hub")
        L.N(p + "_fw", "Azure Firewall\nPremium", "azure_firewall", p + "_hub")
        L.N(p + "_agw", "Application Gateway\ncon firewall web", "app_gateway", p + "_hub")
        L.N(p + "_dns", "DNS Private\nResolver", "dns_resolver", p + "_hub")
        L.N(p + "_bas", "Azure Bastion", "bastion", p + "_hub")
        L.N(p + "_apim", "API Management\nPremium", "api_management", p + "_hub")
    L.N("x_fw", "Azure Firewall\nPremium", "azure_firewall", "x_hub")
    L.N("x_dns", "DNS Private\nResolver", "dns_resolver", "x_hub")
    L.N("x_vpn", "VPN Gateway\n(solo si se acredita)", "vpn_gateway", "x_hub", "por_acreditar")
    L.N("x_bas", "Azure Bastion", "bastion", "x_hub")
    for p, et in (("r", "de Retail"), ("x", "de X-01"), ("f", "de la filial")):
        L.N(p + "_lb", "Balanceador interno\nde AKS", "load_balancer", p + "_app")
        L.N(p + "_aks", "Clúster de AKS\n" + et, "aks", p + "_app")
    L.N("r_pd", "Puntos privados de las\n6 bases PostgreSQL", "private_link", "r_dat")
    L.N("r_pm", "Puntos privados de mensajería,\ncaché y almacenamiento", "private_link", "r_dat")
    L.N("x_pd", "Punto privado de la\nbitácora de cruces", "private_link", "x_dat")
    L.N("x_pm", "Punto privado del\nalmacenamiento de operación", "private_link", "x_dat")
    L.N("f_pd", "Puntos privados de las\n5 bases PostgreSQL", "private_link", "f_dat")
    L.N("f_pm", "Puntos privados de mensajería\ny almacenamiento", "private_link", "f_dat")
    L.E("afd_r", "pe_br", "enlace", "origen privado")
    L.E("afd_r", "pe_us", "enlace", "origen secundario")
    L.E("pe_br", "r_agw", "enlace", "HTTPS privado")
    for p in ("r", "f"):
        L.E(p + "_agw", p + "_apim", "enlace", "rutas de API")
        L.E(p + "_apim", p + "_lb", "enlace", "llamadas autorizadas")
        L.E(p + "_lb", p + "_aks", "enlace", "hacia los servicios")
        L.E(p + "_aks", p + "_pd", "trafico_inspeccionado", "acceso a datos")
    L.E("x_lb", "x_aks", "enlace", "hacia el servicio")
    L.E("x_aks", "x_pd", "trafico_inspeccionado", "bitácora")
    L.E("r_aks", "x_lb", "trafico_inspeccionado", "autorización de compra")
    L.E("x_aks", "f_lb", "trafico_inspeccionado", "consulta de cupo")
    return L


# ---------------------------------------------------------------- B2 · cómputo (F5)
def fig_b2():
    L = Lam("B2_computo-chile-central", "F5", "Cómputo de Azure Chile Central: clústeres de AKS y máquinas de apoyo")
    L.G("cl", "Azure Chile Central · grupos de nodos repartidos en 3 zonas", "nube_azure", "fila")
    for p, nom, fr in FRENTES:
        L.G(p, nom, "ambito", "columna", "cl", fr)
    L.G("r_k", "Clúster de AKS de Retail · 17 nodos base", "subred", "rejilla", "r", "retail", 2)
    L.N("r_cp", "Plano de control\n(AKS Premium)", "aks", "r_k")
    L.N("r_sys", "Grupo de sistema\n3 nodos", "vmss", "r_k")
    L.N("r_biz", "Grupo de negocio\n5 nodos", "vmss", "r_k")
    L.N("r_int", "Grupo de integración\n3 nodos", "vmss", "r_k")
    L.N("r_st", "Grupo de estado, 3 nodos\n(OpenSearch, MLflow\ny OpenMetadata)", "vmss", "r_k")
    L.N("r_ops", "Grupo de operación, 3 nodos\n(pila de observabilidad)", "vmss", "r_k")
    L.N("r_ela", "Grupo elástico de modelos\n0 a 3 nodos", "vmss", "r_k", "condicionado")
    L.G("r_m", "Máquinas de apoyo de Retail (fuera del clúster)", "subred", "rejilla", "r", "retail", 2)
    L.N("r_bi", "Gateways de\nPower BI ×2", "vm", "r_m")
    L.N("r_ir", "Extracción de datos\n(Data Factory) ×2", "vm", "r_m")
    L.N("r_pa", "Conectores de\nacceso privado ×2", "vm", "r_m")
    L.N("r_syn", "Sonda de vigilancia", "vm", "r_m")
    L.G("x_k", "Clúster de AKS de X-01 · 6 nodos", "subred", "rejilla", "x", "frontera", 2)
    L.N("x_cp", "Plano de control\n(AKS Premium)", "aks", "x_k")
    L.N("x_sys", "Grupo de sistema\n3 nodos", "vmss", "x_k")
    L.N("x_biz", "Grupo de negocio, 3 nodos\n(servicio y su observabilidad)", "vmss", "x_k")
    L.G("f_k", "Clúster de AKS de la filial · 17 nodos base", "subred", "rejilla", "f", "emisor", 2)
    L.N("f_cp", "Plano de control\n(AKS Premium)", "aks", "f_k")
    L.N("f_sys", "Grupo de sistema\n3 nodos", "vmss", "f_k")
    L.N("f_biz", "Grupo de negocio\n5 nodos", "vmss", "f_k")
    L.N("f_int", "Grupo de integración\n3 nodos", "vmss", "f_k")
    L.N("f_st", "Grupo de estado, 3 nodos\n(OpenMetadata)", "vmss", "f_k")
    L.N("f_ops", "Grupo de operación, 3 nodos\n(pila de observabilidad)", "vmss", "f_k")
    L.G("f_m", "Máquinas de apoyo de la filial (fuera del clúster)", "subred", "rejilla", "f", "emisor", 2)
    L.N("f_bi", "Gateways de\nPower BI ×2", "vm", "f_m")
    L.N("f_ir", "Extracción de datos\n(Data Factory) ×2", "vm", "f_m")
    L.N("f_pa", "Conectores de\nacceso privado ×2", "vm", "f_m")
    L.N("f_syn", "Sonda de vigilancia", "vm", "f_m")
    return L


# ---------------------------------------------------------------- B3 · datos, mensajería y respaldo (F5)
def fig_b3():
    L = Lam("B3_datos-chile-central", "F5", "Datos, mensajería y respaldo de Azure Chile Central por frente")
    L.G("cl", "Azure Chile Central · datos copiados entre zonas", "nube_azure", "fila")
    for p, nom, fr in FRENTES:
        L.G(p, nom, "ambito", "columna", "cl", fr)
    L.G("r_pg", "Bases PostgreSQL de Retail (6)", "subred", "rejilla", "r", "retail", 3)
    for i, et in enumerate(["Mercadería e\nhistorial de precios", "Venta", "Clientes", "Vectores\n(búsqueda multimodal)", "Analítico", "Técnico"]):
        L.N(f"r_pg{i}", et, "postgresql", "r_pg")
    L.G("r_ms", "Mensajería, caché y almacenamiento de Retail", "subred", "rejilla", "r", "retail", 3)
    L.N("r_sb", "Service Bus Premium\nde Retail", "service_bus", "r_ms")
    L.N("r_rd", "Memoria rápida\n(Redis B20, 24 GB)", "redis", "r_ms")
    L.N("r_dl", "Data Lake de Retail\n(3 TiB)", "data_lake", "r_ms")
    L.N("r_ar", "Archivo inmutable\nde Retail (25 TiB)", "storage", "r_ms")
    L.N("r_op", "Almacenamiento de\noperación (1 TiB)", "storage", "r_ms")
    L.N("r_bk", "Bóveda de respaldo\n(redundante entre zonas)", "backup_vault", "r_ms")
    L.G("x_pg", "Base PostgreSQL de X-01 (1)", "subred", "rejilla", "x", "frontera", 3)
    L.N("x_pg0", "Bitácora de cruces", "postgresql", "x_pg")
    L.G("x_ms", "Almacenamiento y respaldo de X-01", "subred", "rejilla", "x", "frontera", 3)
    L.N("x_op", "Almacenamiento de\noperación (1 TiB)", "storage", "x_ms")
    L.N("x_bk", "Bóveda de respaldo\n(redundante entre zonas)", "backup_vault", "x_ms")
    L.G("f_pg", "Bases PostgreSQL de la filial (5)", "subred", "rejilla", "f", "emisor", 3)
    for i, et in enumerate(["Originación", "Cartera", "Evidencia", "Analítico", "Técnico"]):
        L.N(f"f_pg{i}", et, "postgresql", "f_pg")
    L.G("f_ms", "Mensajería y almacenamiento de la filial", "subred", "rejilla", "f", "emisor", 3)
    L.N("f_sb", "Service Bus Premium\nde la filial", "service_bus", "f_ms")
    L.N("f_dl", "Data Lake de la filial\n(2 TiB)", "data_lake", "f_ms")
    L.N("f_ev", "Evidencia de la filial\n(5 TiB)", "storage", "f_ms")
    L.N("f_ar", "Archivo inmutable\nde la filial (12 TiB)", "storage", "f_ms")
    L.N("f_op", "Almacenamiento de\noperación (1 TiB)", "storage", "f_ms")
    L.N("f_bk", "Bóveda de respaldo\n(redundante entre zonas)", "backup_vault", "f_ms")
    return L


# ---------------------------------------------------------------- B4 · identidad, seguridad, observabilidad y entrega (F5)
def fig_b4():
    L = Lam("B4_seguridad-operacion", "F5", "Identidad, seguridad, observabilidad y entrega de Azure Chile Central")
    L.G("glo", "Servicios globales o fuera de Chile Central", "seccion", "columna")
    L.N("ent", "Microsoft Entra ID con PIM\n(un tenant, permisos por frente)", "entra_id", "glo")
    L.N("exi", "Entra External ID\n(una configuración por negocio)", "external_id", "glo")
    L.N("itn", "Microsoft Intune", "intune", "glo")
    L.N("pip", "Azure Pipelines con agentes\nefímeros (un conjunto por frente)", "devops", "glo")
    L.N("apc", "Azure API Center ×2\n(East US, solo contratos)", "api_management", "glo")
    L.N("sen", "Microsoft Sentinel ×3\n(Brazil South)", "sentinel", "glo")
    L.G("cl", "Azure Chile Central", "nube_azure", "fila")
    for p, nom, fr in FRENTES:
        L.G(p, nom, "ambito", "columna", "cl", fr)
        L.G(p + "_s", "Claves y seguridad", "subred", "rejilla", p, fr, 2)
        L.G(p + "_o", "Observabilidad, datos y entrega", "subred", "rejilla", p, fr, 2)
    for p in ("r", "x", "f"):
        L.N(p + "_kv", "Key Vault", "key_vault", p + "_s")
        if p in ("x", "f"):
            L.N(p + "_hsm", "Managed HSM\n(condicionado al censo)", "hsm", p + "_s", "condicionado")
        L.N(p + "_def", "Microsoft Defender", "defender", p + "_s")
        L.N(p + "_law", "Log Analytics", "log_analytics", p + "_o")
        if p in ("r", "f"):
            L.N(p + "_adf", "Azure Data Factory", "data_factory", p + "_o")
            L.N(p + "_pbi", "Capacidad de Power BI", "power_bi", p + "_o")
        L.N(p + "_acr", "Container Registry\nPremium", "container_registry", p + "_o")
        L.N(p + "_tf", "Estado de Terraform", "storage", p + "_o")
    L.E("r_o", "sen", "enlace", "solo eventos de seguridad")
    return L


# ---------------------------------------------------------------- E1 · entrega y ambientes (F3)
def fig_e1():
    L = Lam("E1_entrega-ambientes", "F3", "Canal de entrega y ambientes por frente")
    L.G("ent", "Entrega", "seccion", "fila")
    L.N("repo", "Repositorio de código", "repositorio", "ent")
    L.N("pip", "Azure Pipelines\n(agentes en conjunto de escalado)", "devops", "ent")
    L.N("acr", "Container Registry Premium\n(uno por frente)", "container_registry", "ent")
    L.N("tf", "Estado de Terraform\n(por frente y ambiente)", "storage", "ent")
    L.G("cl", "Azure Chile Central · 3 grupos de administración y 12 suscripciones", "nube_azure", "fila")
    amb = (("dev", "Desarrollo"), ("qa", "QA"), ("pre", "Preproducción"), ("prd", "Producción"))
    for a, nom in amb:
        L.G(a, nom, "ambito", "columna", "cl")
        for p, fn, _ in FRENTES:
            L.N(f"{a}_{p}", f"Suscripción y Key Vault\n{'de ' + fn if p != 'f' else 'de la filial'}", "key_vault", a)
    L.N("lab", "Tienda de laboratorio\n(4 servidores y 2 árbitros)", "sitio", "pre")
    L.G("br", "Azure Brazil South · 3 suscripciones", "nube_azure", "fila")
    L.G("rec", "Recuperación ante Desastres · misma definición de infraestructura que Producción", "ambito", "fila", "br")
    for p, fn, _ in FRENTES:
        L.N(f"rec_{p}", f"Suscripción y Key Vault\n{'de ' + fn if p != 'f' else 'de la filial'}", "key_vault", "rec")
    L.E("repo", "pip", "despliegue", "cambio revisado")
    L.E("pip", "acr", "despliegue", "imagen firmada")
    L.E("acr", "cl", "despliegue", "despliegue por frente y ambiente")
    for p, _, _ in FRENTES:
        L.E(f"dev_{p}", f"qa_{p}", "despliegue", "promoción")
        L.E(f"qa_{p}", f"pre_{p}", "despliegue", "promoción")
        L.E(f"pre_{p}", f"prd_{p}", "aprobacion", "aprobación del cambio")
    return L


# ---------------------------------------------------------------- F4 · puntos de falla (F4) — numeración de la tabla de contingencias
def fig_f4():
    L = Lam("F4_puntos-falla", "F4", "Puntos de falla y contingencias de los sitios y de la nube")
    L.G("tie", "Tienda tipo ×22 (túneles IPsec hacia Azure)", "sitio_cliente", "columna")
    L.N("srv", "Par de servidores por negocio\ncon árbitro", "servidor", "tie", insignia=1)
    L.N("acc", "Dos accesos fijos\nde operadores distintos", "router", "tie", insignia=2)
    L.N("lte", "Router 4G/5G\n(tercer camino, 5 Mbps)", "antena_lte", "tie", insignia=3)
    L.N("aut", "Operación local de 24 horas\n(sin ningún enlace)", "sitio", "tie", insignia=4)
    L.G("sit", "Centros y casa matriz", "sitio_cliente", "columna")
    L.N("cd2", "Enlace único de CD-02, con\ncaptura local y router 4G/5G", "antena_lte", "sit", insignia=5)
    L.N("dc1", "Conexión de DC-01\n(dos accesos de operador)", "centro_datos", "sit", insignia=6)
    L.N("erp", "ERP/DTE conservado\n(modalidad fiscal de contingencia)", "servidor", "sit", "por_acreditar", insignia=9)
    L.N("wms", "WMS de CD-01\n(degradación por interfaz)", "servidor", "sit", "por_acreditar", insignia=10)
    L.G("cl", "Azure Chile Central", "nube_azure", "columna")
    L.G("zon", "Tres zonas de disponibilidad", "zona", "fila", "cl")
    L.N("z", "Servicios zonales con\ncontinuidad en las otras dos", "aks", "zon", insignia=7)
    L.N("sb", "Service Bus de un negocio\n(reintento y reproceso)", "service_bus", "cl", insignia=11)
    L.N("reg", "Región completa", "vnet", "cl", insignia=8)
    L.G("br", "Azure Brazil South", "nube_azure", "columna")
    L.N("rec", "Recuperación de los tres frentes\n(RTO 4 h, RPO 15 min)", "aks", "br")
    L.G("glo", "Servicios globales", "seccion", "columna")
    L.N("afd", "Front Door y entrada pública\n(punto privado por East US)", "front_door", "glo", insignia=12)
    L.N("ent", "Entra ID\n(cuentas de emergencia por frente)", "entra_id", "glo", insignia=13)
    L.E("srv", "acc", "enlace", "túneles por negocio")
    L.E("acc", "lte", "respaldo", "si caen ambos accesos")
    L.E("sit", "cl", "vpn", "túneles IPsec de los sitios")
    L.E("reg", "rec", "replica", "conmutación de región")
    return L


# ---------------------------------------------------------------- D1 · tienda: red y servidores (F5)
def fig_d1():
    L = Lam("D1_tienda-red-servidores", "F5", "Tienda tipo: red, servidores y equipos")
    L.G("tie", "Tienda tipo (se repite 22 veces)", "sitio_cliente", "columna")
    L.G("tr", "Retail en la tienda", "ambito", "rejilla", "tie", "retail", 4)
    L.N("pos", "Cajas, impresoras\ny lectores", "pc", "tr")
    L.N("mov", "Terminales móviles", "movil", "tr")
    L.N("tot", "Tótem de Modo Tienda\ny fila virtual", "pc", "tr")
    L.N("lck", "Controlador de lockers\n(tiendas con lockers)", "servidor", "tr")
    L.N("sr1", "Servidor de Retail 1\n(activo)", "servidor", "tr")
    L.N("sr2", "Servidor de Retail 2\n(espera)", "servidor", "tr")
    L.N("ar", "Árbitro de Retail", "servidor", "tr")
    L.N("br", "Copia local cifrada\nde Retail", "storage", "tr")
    L.G("tf", "Filial emisora en la tienda", "ambito", "rejilla", "tie", "emisor", 4)
    L.N("mes", "Terminales del\nmesón de crédito", "pc", "tf")
    L.N("sf1", "Servidor de la filial 1\n(activo)", "servidor", "tf")
    L.N("sf2", "Servidor de la filial 2\n(espera)", "servidor", "tf")
    L.N("af", "Árbitro de la filial", "servidor", "tf")
    L.N("bf", "Copia local cifrada\nde la filial", "storage", "tf")
    L.N("xl", "Copia local del Control de cruces ×2\n(dentro de los servidores de la filial)", "servidor", "tf")
    L.N("bx", "Copia local cifrada\ndel Control de cruces", "storage", "tf")
    L.G("tn", "Red de la tienda", "ambito", "rejilla", "tie", "transversal", 4)
    L.N("fwr", "Firewalls de Retail ×2\ncon SD-WAN", "fortigate", "tn")
    L.N("fwf", "Firewalls de la filial ×2\ncon SD-WAN", "fortigate", "tn")
    L.N("sw", "Switches ×4\n(dos por negocio)", "switch", "tn")
    L.N("ap", "Puntos inalámbricos\ncorporativos", "access_point", "tn")
    L.N("cam", "Cámaras y grabador local\n(30 días)", "camara", "tn")
    L.G("sal", "Salida de la tienda", "seccion", "columna")
    L.N("oa", "Acceso fijo, operador A", "router", "sal")
    L.N("ob", "Acceso fijo, operador B", "router", "sal")
    L.N("lte", "Router de respaldo 4G/5G\n(doble SIM)", "antena_lte", "sal")
    L.G("az", "Hacia Azure Chile Central", "nube_azure", "columna")
    L.N("vr", "VPN Gateway de Retail", "vpn_gateway", "az")
    L.N("vf", "VPN Gateway de la filial", "vpn_gateway", "az")
    L.E("tn", "sal", "enlace", "un túnel por negocio")
    L.E("sal", "vr", "vpn", "túnel de Retail")
    L.E("sal", "vf", "vpn", "túnel de la filial")
    return L


# ---------------------------------------------------------------- D2 · tienda: energía y espacio (F5)
def fig_d2():
    L = Lam("D2_tienda-energia-espacio", "F5", "Tienda tipo: energía y espacio")
    L.G("tie", "Tienda tipo · sala técnica de sitio", "sitio_cliente", "fila")
    L.G("rk", "Racks (31 de 72U ocupadas al inicio)", "zona", "columna", "tie")
    L.N("rr", "Rack de 24U de Retail\n(8U, PDU A y B)", "rack", "rk")
    L.N("rf", "Rack de 24U de la filial\n(8U, PDU A y B)", "rack", "rk")
    L.N("rc", "Rack de 24U de comunicaciones\n(15U, PDU A y B)", "rack", "rk")
    L.G("en", "Energía (carga de 2,57 kW; 3,341 kW con margen)", "zona", "columna", "tie")
    L.N("ua", "UPS de 6 kVA, rama A\n(30 minutos)", "ups", "en")
    L.N("ub", "UPS de 6 kVA, rama B\n(30 minutos)", "ups", "en")
    L.N("ats", "Transferidor automático", "ups", "en")
    L.N("gen", "Grupo electrógeno inicial", "ups", "en")
    L.G("am", "Ambiente del recinto", "zona", "columna", "tie")
    L.N("cli", "Climatización y sensores de\ntemperatura, humedad y energía", "monitor", "am")
    L.E("ua", "rk", "enlace", "rama A")
    L.E("ub", "rk", "enlace", "rama B")
    L.E("gen", "ats", "respaldo", "corte prolongado")
    L.E("ats", "ub", "enlace", "alimenta las UPS")
    return L


# ---------------------------------------------------------------- D3 · DC-01 (F5)
def fig_d3():
    L = Lam("D3_dc01-casa-matriz", "F5", "Centro de datos de casa matriz (DC-01)")
    L.G("dc", "DC-01 · recinto propio de 140 m² (2011), sala técnica principal", "sitio_cliente", "fila")
    L.G("rt", "Recinto técnico (provisto por el proponente)", "zona", "rejilla", "dc", columnas=2)
    L.N("k1", "Rack de 42U de Retail", "rack", "rt")
    L.N("k2", "Rack de 42U de la filial", "rack", "rt")
    L.N("k3", "Rack de 42U de\ncomunicaciones", "rack", "rt")
    L.N("k4", "Rack de 42U de\nrespaldo local", "rack", "rt")
    L.N("ups", "UPS de 30 minutos", "ups", "rt")
    L.N("gen", "Generador y transferidor\nautomático (24 h)", "ups", "rt")
    L.N("cli", "Climatización, sensores y\ndetección y extinción de incendio", "monitor", "rt")
    L.N("acc", "Control de acceso\ny videovigilancia", "camara", "rt")
    L.G("rr", "Retail en DC-01", "ambito", "columna", "dc", "retail")
    L.N("nr", "Red y firewall de Retail", "fortigate", "rr")
    L.N("ir", "Nodos de integración de\nData Factory ×2 (propuestos)", "servidor", "rr", "propuesto")
    L.G("rf", "Filial emisora en DC-01", "ambito", "columna", "dc", "emisor")
    L.N("nf", "Red y firewall de la filial", "fortigate", "rf")
    L.N("if", "Nodos de integración de\nData Factory ×2 (transitorios)", "servidor", "rf", "propuesto")
    L.G("sc", "Sistemas conservados (supuesto de dimensionamiento)", "zona", "columna", "dc")
    L.N("erp", "ERP y facturación\nelectrónica", "servidor", "sc", "por_acreditar")
    L.N("c09", "Sistema central de retail\n(2009)", "servidor", "sc", "por_acreditar")
    L.G("pa", "Ubicación por acreditar", "seccion", "columna")
    L.N("c11", "Plataforma de crédito (2011),\nen convivencia durante su migración", "servidor", "pa", "por_acreditar")
    L.G("sal", "Salida", "seccion", "columna")
    L.N("oa", "Acceso de operador A\n(propuesto)", "router", "sal", "propuesto")
    L.N("ob", "Acceso de operador B\n(propuesto, otra ruta)", "router", "sal", "propuesto")
    L.N("dc2", "Sala de respaldo DC-02\n(misma comuna)", "centro_datos", "sal")
    L.G("az", "Hacia Azure Chile Central", "nube_azure", "columna")
    L.N("vr", "VPN Gateway de Retail", "vpn_gateway", "az")
    L.N("vf", "VPN Gateway de la filial", "vpn_gateway", "az")
    L.E("dc", "sal", "enlace", "un túnel por negocio")
    L.E("sal", "vr", "vpn", "túnel de Retail")
    L.E("sal", "vf", "vpn", "túnel de la filial")
    return L


# ---------------------------------------------------------------- D4 · centros de distribución (F5)
def fig_d4():
    L = Lam("D4_centros-distribucion", "F5", "Centros de distribución CD-01 y CD-02")
    def centro(c, nom, enl):
        L.G(c, nom, "sitio_cliente", "rejilla", columnas=3)
        L.N(c + "_p1", "Nodo local de captura 1\n(activo)", "servidor", c)
        L.N(c + "_p2", "Nodo local de captura 2\n(espera)", "servidor", c)
        L.N(c + "_t", "Terminales del centro", "movil", c)
        L.N(c + "_fw", "Firewall y switching", "fortigate", c)
        L.N(c + "_ap", "Acceso inalámbrico", "access_point", c)
        L.N(c + "_l", enl, "router", c)
        L.N(c + "_m", "Router 4G/5G", "antena_lte", c)
    centro("c1", "Centro de distribución principal (CD-01, 42.000 m²)", "Enlace redundante\nde dos proveedores")
    L.N("c1_w", "WMS de 2016\n(alojamiento por acreditar)", "servidor", "c1", "por_acreditar")
    L.G("az", "Hacia Azure Chile Central", "nube_azure", "columna")
    L.N("vr", "VPN Gateway de Retail", "vpn_gateway", "az")
    centro("c2", "Centro de distribución de Concepción (CD-02, 9.000 m²)", "Enlace único\n(Caso 09)")
    L.N("c2_l2", "Segundo enlace fijo\n(propuesto al Cliente)", "router", "c2", "propuesto")
    L.E("c1", "vr", "vpn", "túnel de Retail")
    L.E("c2", "vr", "vpn", "túnel de Retail")
    return L


# ---------------------------------------------------------------- C1 · Brazil South: red y entrada (F5)
def fig_c1():
    L = Lam("C1_brazil-red-entrada", "F5", "Azure Brazil South: red y entrada de recuperación por frente")
    L.G("ext", "Desde fuera de la región", "seccion", "columna")
    L.N("afd", "Front Door: origen de recuperación,\ndeshabilitado hasta la etapa 6", "front_door", "ext")
    L.N("sit", "Sitios del Cliente\n(segundo destino del túnel)", "sitio", "ext")
    L.N("cl", "Azure Chile Central\n(primaria)", "vnet", "ext")
    L.G("br", "Azure Brazil South · rangos 10.68, 10.69 y 10.70", "nube_azure", "fila")
    for p, nom, fr in FRENTES:
        L.G(p, nom, "ambito", "rejilla", "br", fr, 2)
    for p in ("r", "f"):
        L.N(p + "_pe", "Punto privado de\nFront Door", "private_link", p)
        L.N(p + "_agw", "Application Gateway\ncon firewall web", "app_gateway", p)
        L.N(p + "_vpn", "VPN Gateway\n(con zonas)", "vpn_gateway", p)
        L.N(p + "_apim", "Gateway regional de\nAPI Management", "api_management", p)
        L.N(p + "_fw", "Azure Firewall\nPremium", "azure_firewall", p)
        L.N(p + "_dns", "DNS Private\nResolver", "dns_resolver", p)
        L.N(p + "_bas", "Azure Bastion\n(sin zonas)", "bastion", p)
    L.N("x_fw", "Azure Firewall\nPremium", "azure_firewall", "x")
    L.N("x_dns", "DNS Private\nResolver", "dns_resolver", "x")
    L.N("x_bas", "Azure Bastion\n(sin zonas)", "bastion", "x")
    L.E("afd", "r_pe", "enlace", "solo tras activarlo")
    for p in ("r", "f"):
        L.E(p + "_pe", p + "_agw", "enlace", "HTTPS privado")
        L.E(p + "_agw", p + "_apim", "enlace", "rutas de API")
    L.E("sit", "r_vpn", "vpn", "reconexión en contingencia")
    L.E("cl", "br", "replica", "réplica privada")
    return L


# ---------------------------------------------------------------- C2 · Brazil South: cómputo y datos (F5)
def fig_c2():
    L = Lam("C2_brazil-computo-datos", "F5", "Azure Brazil South: cómputo y datos en espera por frente")
    L.G("br", "Azure Brazil South · activo-pasivo templado", "nube_azure", "fila")
    for p, nom, fr in FRENTES:
        L.G(p, nom, "ambito", "rejilla", "br", fr, 2)
    L.N("r_aks", "Clúster de AKS en espera\n17 nodos base, encendido", "aks", "r")
    L.N("r_vm", "Máquinas templadas\n(extracción ×2, acceso\nprivado ×2 y sonda)", "vm", "r")
    L.N("r_bi", "Gateways de Power BI ×2\n(apagadas)", "vm", "r")
    L.N("r_pg", "6 bases PostgreSQL\nde recuperación (réplicas)", "postgresql", "r")
    L.N("r_sb", "Service Bus Premium\n(se habilita en la contingencia)", "service_bus", "r")
    L.N("r_rd", "Memoria rápida (Redis)\n(se reconstruye)", "redis", "r")
    L.N("r_dl", "Data Lake y archivo\n(copia programada)", "data_lake", "r")
    L.N("r_kv", "Key Vault\n(reinyección controlada)", "key_vault", "r")
    L.N("r_acr", "Container Registry\n(copia por digest)", "container_registry", "r")
    L.N("r_bk", "Bóveda de respaldo", "backup_vault", "r")
    L.N("r_se", "Microsoft Sentinel", "sentinel", "r")
    L.N("x_aks", "Clúster de AKS en espera\n6 nodos base, encendido", "aks", "x")
    L.N("x_pg", "Base PostgreSQL de la\nbitácora (réplica)", "postgresql", "x")
    L.N("x_kv", "Key Vault", "key_vault", "x")
    L.N("x_hsm", "Managed HSM\n(réplica multirregión)", "hsm", "x", "condicionado")
    L.N("x_acr", "Container Registry\n(copia por digest)", "container_registry", "x")
    L.N("x_bk", "Bóveda de respaldo", "backup_vault", "x")
    L.N("x_se", "Microsoft Sentinel", "sentinel", "x")
    L.N("f_aks", "Clúster de AKS en espera\n17 nodos base, encendido", "aks", "f")
    L.N("f_vm", "Máquinas templadas\n(extracción ×2, acceso\nprivado ×2 y sonda)", "vm", "f")
    L.N("f_bi", "Gateways de Power BI ×2\n(apagadas)", "vm", "f")
    L.N("f_pg", "5 bases PostgreSQL\nde recuperación (réplicas)", "postgresql", "f")
    L.N("f_sb", "Service Bus Premium\n(se habilita en la contingencia)", "service_bus", "f")
    L.N("f_dl", "Data Lake, evidencia\ny archivo (copia programada)", "data_lake", "f")
    L.N("f_kv", "Key Vault", "key_vault", "f")
    L.N("f_hsm", "Managed HSM\n(réplica multirregión)", "hsm", "f", "condicionado")
    L.N("f_acr", "Container Registry\n(copia por digest)", "container_registry", "f")
    L.N("f_bk", "Bóveda de respaldo", "backup_vault", "f")
    L.N("f_se", "Microsoft Sentinel", "sentinel", "f")
    return L


# ---------------------------------------------------------------- C3 · conmutación (F4)
def fig_c3():
    L = Lam("C3_conmutacion", "F4", "Conmutación a Azure Brazil South: orden de arranque")
    L.G("cl", "Azure Chile Central (primaria)", "nube_azure", "columna")
    L.N("dec", "Declaración de contingencia:\ndos sondas, métricas\ny verificación humana", "personas", "cl")
    L.G("br", "Azure Brazil South · siete etapas, la suma cabe en el RTO de 4 horas", "nube_azure", "fila")
    L.N("e1", "Identidad y claves\nde cada frente", "key_vault", "br", insignia=1)
    L.N("e2", "Red y DNS: los sitios\nreconectan al VPN\nGateway de Brasil", "vpn_gateway", "br", insignia=2)
    L.N("e3", "Datos y mensajería: se\naísla Chile, se promueve\ncada réplica y se habilita\nla alta disponibilidad", "postgresql", "br", insignia=3)
    L.N("e4", "Cómputo y herramientas\n(ya encendidos)", "aks", "br", insignia=4)
    L.N("e5", "Servicios de cada frente", "aks", "br", insignia=5)
    L.N("e6", "Front Door activa el\norigen de Brasil,\ntráfico gradual", "front_door", "br", insignia=6)
    L.N("e7", "Prueba funcional: venta,\ncrédito, compra por X-01\ny conciliación", "personas", "br", insignia=7)
    L.E("dec", "e1", "enlace", "inicio")
    for a, b in (("e1", "e2"), ("e2", "e3"), ("e3", "e4"), ("e4", "e5"), ("e5", "e6"), ("e6", "e7")):
        L.E(a, b, "enlace", "luego")
    return L


FIGURAS = {"A": fig_a, "B1": fig_b1, "B2": fig_b2, "B3": fig_b3, "B4": fig_b4, "E1": fig_e1, "F4": fig_f4,
           "D1": fig_d1, "D2": fig_d2, "D3": fig_d3, "D4": fig_d4, "C1": fig_c1, "C2": fig_c2, "C3": fig_c3}

if __name__ == "__main__":
    claves = sys.argv[1:] or list(FIGURAS)
    for k in claves:
        L = FIGURAS[k]()
        ruta = os.path.join(AQUI, "especificaciones", L.clave + ".json")
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(L.spec(), f, ensure_ascii=False, indent=1)
        print(k, L.clave, len(L.n), "nodos", len(L.e), "enlaces")
