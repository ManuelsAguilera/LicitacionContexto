"""Generador mínimo de diagramas .drawio con posiciones explícitas.

Sigue la hoja de estilo de diagramas Azure del proyecto: recuadros anidados
(región ⊃ red virtual ⊃ subred ⊃ componente), íconos con nombre debajo,
líneas ortogonales rotuladas, una familia de azules, sin título ni leyenda.

Uso: cada figura importa este módulo, declara zonas, íconos y aristas, y llama
a `save()`, que escribe el .drawio y exporta PNG/PDF con draw.io desktop.
"""

import html
import shutil
import subprocess
from pathlib import Path

FONT = "Helvetica"
BLUE = "#0078D4"
NAVY = "#1F3A5F"
GRAY = "#8A8A8A"
TEXT = "#1F1F1F"
ACCENT = "#C2185B"  # segundo color: un solo camino destacado por figura

# Íconos: librería oficial azure2 de draw.io y figuras azules de su set Azure.
ICONS = {
    # Red
    "vnet": "img/lib/azure2/networking/Virtual_Networks.svg",
    "subnet": "img/lib/azure2/networking/Subnet.svg",
    "vpngw": "img/lib/azure2/networking/Virtual_Network_Gateways.svg",
    "ercircuit": "img/lib/azure2/networking/ExpressRoute_Circuits.svg",
    "firewall": "img/lib/azure2/networking/Firewalls.svg",
    "frontdoor": "img/lib/azure2/networking/Front_Doors.svg",
    "waf": "img/lib/azure2/networking/Web_Application_Firewall_Policies_WAF.svg",
    "dns": "img/lib/azure2/networking/DNS_Zones.svg",
    "pe": "img/lib/azure2/networking/Private_Endpoint.svg",
    "lb": "img/lib/azure2/networking/Load_Balancers.svg",
    "nsg": "img/lib/azure2/networking/Network_Security_Groups.svg",
    "router": "img/lib/azure2/networking/Local_Network_Gateways.svg",
    "connections": "img/lib/azure2/networking/Connections.svg",
    # Cómputo y contenedores
    "aks": "img/lib/azure2/containers/Kubernetes_Services.svg",
    "acr": "img/lib/azure2/containers/Container_Registries.svg",
    "vm": "img/lib/azure2/compute/Virtual_Machine.svg",
    # Integración y datos
    "apim": "img/lib/azure2/integration/API_Management_Services.svg",
    "eventhubs": "img/lib/azure2/analytics/Event_Hubs.svg",
    "postgres": "img/lib/azure2/databases/Azure_Database_PostgreSQL_Server.svg",
    "redis": "img/lib/azure2/databases/Cache_Redis.svg",
    "storage": "img/lib/azure2/storage/Storage_Accounts.svg",
    "datalake": "img/lib/azure2/storage/Data_Lake_Storage_Gen1.svg",
    # Seguridad, identidad, operación
    "keyvault": "img/lib/azure2/security/Key_Vaults.svg",
    "entra": "img/lib/azure2/identity/Azure_Active_Directory.svg",
    "monitor": "img/lib/azure2/management_governance/Monitor.svg",
    "loganalytics": "img/lib/azure2/analytics/Log_Analytics_Workspaces.svg",
    "backup": "img/lib/azure2/other/Backup_Vault.svg",
    "subscription": "img/lib/azure2/general/Subscriptions.svg",
    "devops": "img/lib/azure2/devops/Azure_DevOps.svg",
    "repo": "img/lib/azure2/general/TFS_VC_Repository.svg",
    "globe": "img/lib/azure2/general/Globe.svg",
    "bastion": "img/lib/azure2/networking/Bastions.svg",
    "fwpolicy": "img/lib/azure2/networking/Azure_Firewall_Policy.svg",
    "ddos": "img/lib/azure2/networking/DDoS_Protection_Plans.svg",
    "dnsresolver": "img/lib/azure2/networking/DNS_Private_Resolver.svg",
    "nat": "img/lib/azure2/networking/NAT.svg",
    "sentinel": "img/lib/azure2/security/Azure_Sentinel.svg",
    "defender": "img/lib/azure2/security/Azure_Defender.svg",
    "condaccess": "img/lib/azure2/security/Conditional_Access.svg",
    "pim": "img/lib/azure2/identity/Entra_Privileged_Identity_Management.svg",
    "privateaccess": "img/lib/azure2/identity/Entra_Private_Access.svg",
    "users": "img/lib/azure2/identity/Users.svg",
    "policy": "img/lib/azure2/management_governance/Policy.svg",
    "arc": "img/lib/azure2/management_governance/Azure_Arc.svg",
    "cost": "img/lib/azure2/management_governance/Cost_Management_and_Billing.svg",
    "hsm": "img/lib/azure2/other/Dedicated_HSM.svg",
    "powerbi": "img/lib/azure2/analytics/Power_BI_Embedded.svg",
    "devpools": "img/lib/azure2/other/Managed_DevOps_Pools.svg",
    "browser": "img/lib/azure2/general/Browser.svg",
    "appgw": "img/lib/azure2/networking/Application_Gateways.svg",
    "mredis": "img/lib/azure2/databases/Azure_Managed_Redis.svg",
    "rguard": "img/lib/azure2/other/Resource_Guard.svg",
}

# Figuras on-premise en la misma familia azul.
SHAPES = {
    "building": "mxgraph.azure.enterprise",
    "server": "mxgraph.azure.server",
    "computer": "mxgraph.azure.computer",
    "laptop": "mxgraph.azure.laptop",
    "mobile": "mxgraph.azure.mobile",
    "cloud": "mxgraph.azure.cloud",
    # Equipos de sitio (set cisco, mismo azul)
    "fw_site": "mxgraph.cisco.security.ios_firewall",
    "switch": "mxgraph.cisco.switches.layer_3_switch",
    "switch_acc": "mxgraph.cisco.switches.workgroup_switch",
    "router_site": "mxgraph.cisco.routers.router",
    "ap": "mxgraph.cisco.misc.access_point",
    "camera": "mxgraph.cisco.computers_and_peripherals.video_camera",
    "pos": "mxgraph.cisco.computers_and_peripherals.terminal",
    "handheld": "mxgraph.cisco.computers_and_peripherals.scanner",
    "printer": "mxgraph.cisco.computers_and_peripherals.printer",
    "workstation": "mxgraph.cisco.computers_and_peripherals.workstation",
    "ups": "mxgraph.cisco.misc.ups",
    "nvr": "mxgraph.cisco.servers.storage_server",
    "san": "mxgraph.cisco.storage.fc_storage",
    "srv": "mxgraph.cisco.servers.fileserver",
    "antenna": "mxgraph.cisco.wireless.antenna",
    "cell": "mxgraph.cisco.modems_and_phones.cell_phone",
}
CISCO = {k for k, v in SHAPES.items() if "cisco" in v}


def _esc(text):
    return html.escape(text, quote=True).replace("\n", "&#xa;")


class Diagram:
    def __init__(self, font=11, zone_font=13):
        self.cells = []
        self.n = 0
        self.font = font
        self.zone_font = zone_font
        self.rects = {}

    def _id(self, prefix):
        self.n += 1
        return f"{prefix}{self.n}"

    # ---------- zonas ----------
    def zone(self, x, y, w, h, label, kind="vnet", align="center", valign="top"):
        """Recuadro anidable. kind: onprem, region, vnet, subnet, band, plain."""
        zf, sf = self.zone_font, self.zone_font - 2
        base = (f"rounded=1;arcSize=4;whiteSpace=wrap;html=1;container=0;"
                f"verticalAlign={valign};align={align};spacingTop=6;spacingBottom=6;spacingLeft=10;"
                f"fontFamily={FONT};fontSize={zf};fontStyle=1;fontColor={TEXT};")
        styles = {
            "onprem": f"strokeColor={NAVY};strokeWidth=1.8;fillColor=#FFFFFF;",
            "region": f"strokeColor={BLUE};strokeWidth=1.8;fillColor=#FFFFFF;",
            "vnet": f"strokeColor={BLUE};strokeWidth=1.6;dashed=1;dashPattern=1 3;fillColor=#FFFFFF;rounded=0;",
            "vnet_cond": f"strokeColor={BLUE};strokeWidth=1.6;dashed=1;dashPattern=8 4;fillColor=#FFFFFF;rounded=0;",
            "subnet": f"strokeColor={GRAY};strokeWidth=1;dashed=1;dashPattern=4 3;fillColor=#F5F5F5;rounded=0;fontSize={sf};",
            "inner": f"strokeColor={BLUE};strokeWidth=1;fillColor=#FFFFFF;rounded=0;fontSize={sf};",
            "band": f"strokeColor={GRAY};strokeWidth=1;fillColor=#F5F5F5;fontSize={sf};",
            "plain": f"strokeColor={GRAY};strokeWidth=1;fillColor=#FFFFFF;",
        }
        cid = self._id("z")
        self.cells.append(
            f'<mxCell id="{cid}" value="{_esc(label)}" style="{base}{styles[kind]}" vertex="1" parent="1">'
            f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
        if kind == "region":  # nube en la esquina, como en los diagramas de Azure
            self.icon(x - 14, y - 16, "cloud", "", size=34, shape_fill=BLUE)
        if kind in ("vnet", "vnet_cond"):  # ícono de red virtual abajo a la derecha
            self.icon(x + w - 26, y + h - 12, "vnet", "", size=22)
        self.rects[cid] = (x, y, w, h)
        return cid

    def fill(self, zid, items, cols=None, size=44, top=34, bottom=8, side=6):
        """Reparte íconos en grilla, centrados dentro de la zona `zid`.

        items: lista de (nombre_icono, rótulo). Devuelve los ids en el mismo orden.
        """
        x, y, w, h = self.rects[zid]
        n = len(items)
        cols = cols or n
        rows = (n + cols - 1) // cols
        cw = (w - 2 * side) / cols
        rh = (h - top - bottom) / rows
        ids = []
        for i, (name, label) in enumerate(items):
            r, c = divmod(i, cols)
            in_row = min(cols, n - r * cols)
            off = (cols - in_row) * cw / 2  # centra filas incompletas
            cx = x + side + off + c * cw + cw / 2
            cy = y + top + r * rh + (rh - size - 2.4 * self.font) / 2
            ids.append(self.icon(round(cx - size / 2), round(cy), name, label, size=size))
        return ids

    def marker(self, x, y, n, color="#107C10", size=30):
        """Círculo numerado para pasos de una secuencia."""
        cid = self._id("m")
        fs = self.font + 4 if size <= 30 else int(size * 0.62)
        style = (f"ellipse;html=1;fillColor={color};strokeColor=none;fontColor=#FFFFFF;"
                 f"fontFamily={FONT};fontSize={fs};fontStyle=1;align=center;verticalAlign=middle;")
        self.cells.append(
            f'<mxCell id="{cid}" value="{n}" style="{style}" vertex="1" parent="1">'
            f'<mxGeometry x="{x}" y="{y}" width="{size}" height="{size}" as="geometry"/></mxCell>')
        return cid

    # ---------- íconos ----------
    def icon(self, x, y, name, label, size=48, shape_fill="#0078D4", label_pos="bottom"):
        cid = self._id("n")
        if name in ICONS:
            style = f"image;aspect=fixed;html=1;image={ICONS[name]};"
        elif name in CISCO:
            style = (f"shape={SHAPES[name]};aspect=fixed;html=1;fillColor={shape_fill};"
                     f"strokeColor=#FFFFFF;")
        else:
            style = (f"shape={SHAPES[name]};aspect=fixed;html=1;fillColor={shape_fill};"
                     f"strokeColor=none;")
        if label_pos == "bottom":
            style += "verticalLabelPosition=bottom;verticalAlign=top;labelPosition=center;align=center;"
        elif label_pos == "right":
            style += "labelPosition=right;verticalLabelPosition=middle;align=left;verticalAlign=middle;spacingLeft=4;"
        elif label_pos == "left":
            style += "labelPosition=left;verticalLabelPosition=middle;align=right;verticalAlign=middle;spacingRight=4;"
        style += f"fontFamily={FONT};fontSize={self.font};fontColor={TEXT};"
        h = size
        self.cells.append(
            f'<mxCell id="{cid}" value="{_esc(label)}" style="{style}" vertex="1" parent="1">'
            f'<mxGeometry x="{x}" y="{y}" width="{size}" height="{h}" as="geometry"/></mxCell>')
        return cid

    def text(self, x, y, w, h, label, size=11, bold=False, align="center", color=TEXT):
        cid = self._id("t")
        style = (f"text;html=1;whiteSpace=wrap;align={align};verticalAlign=middle;"
                 f"fontFamily={FONT};fontSize={size};fontColor={color};fontStyle={1 if bold else 0};")
        self.cells.append(
            f'<mxCell id="{cid}" value="{_esc(label)}" style="{style}" vertex="1" parent="1">'
            f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
        return cid

    # ---------- aristas ----------
    def edge(self, src, dst, label="", line="solid", color=TEXT, width=1.3, both=False,
             points=(), exit=None, entry=None, label_pos=0, label_dy=0):
        """line: solid (camino normal), dashed (propuesto/respaldo), dotted (peering/diagnóstico)."""
        cid = self._id("e")
        style = (f"edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;jettySize=auto;orthogonalLoop=1;"
                 f"strokeColor={color};strokeWidth={width};endArrow=block;endFill=1;endSize=6;"
                 f"fontFamily={FONT};fontSize={self.font};fontColor={TEXT};labelBackgroundColor=#FFFFFF;")
        if line == "dashed":
            style += "dashed=1;dashPattern=6 4;"
        elif line == "dotted":
            style += "dashed=1;dashPattern=1 3;"
        if both:
            style += "startArrow=block;startFill=1;startSize=6;"
        if exit:
            style += f"exitX={exit[0]};exitY={exit[1]};exitDx=0;exitDy=0;"
        if entry:
            style += f"entryX={entry[0]};entryY={entry[1]};entryDx=0;entryDy=0;"
        pts = "".join(f'<mxPoint x="{px}" y="{py}"/>' for px, py in points)
        arr = f'<Array as="points">{pts}</Array>' if pts else ""
        off = f'<mxPoint x="0" y="{label_dy}" as="offset"/>' if label_dy else ""
        self.cells.append(
            f'<mxCell id="{cid}" value="{_esc(label)}" style="{style}" edge="1" parent="1" source="{src}" target="{dst}">'
            f'<mxGeometry x="{label_pos}" relative="1" as="geometry">{arr}{off}</mxGeometry></mxCell>')
        return cid

    # ---------- salida ----------
    def xml(self):
        body = "".join(self.cells)
        return ('<mxfile><diagram name="diagrama"><mxGraphModel grid="0" page="0" background="#FFFFFF">'
                '<root><mxCell id="0"/><mxCell id="1" parent="0"/>' + body +
                '</root></mxGraphModel></diagram></mxfile>')

    def save(self, path, formats=("png",), scale=3):
        path = Path(path)
        path.write_text(self.xml(), encoding="utf-8")
        exe = shutil.which("drawio")
        if not exe:
            raise SystemExit("draw.io desktop no está en el PATH (drawio).")
        for fmt in formats:
            out = path.with_suffix(f".{fmt}")
            cmd = [exe, "--no-sandbox", "-x", "-f", fmt, "-b", "20", "-o", str(out), str(path)]
            if fmt == "png":
                cmd[5:5] = ["-s", str(scale)]
            subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(out)
