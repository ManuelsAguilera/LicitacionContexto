"""Precios de referencia de equipos, nube y licencias para el modelo financiero.

Todos son precios públicos consultados el 2026-11-11, sin cotización. Cantidades: SD-04 (Tablas 4.14, 4.15 y 4.22),
partidas-sd04-sin-precios.md y calendario-compras.md. Lo marcado «estimación sin fuente» es un supuesto del equipo.
Azure: API pública de precios minoristas (prices.azure.com/api/retail/prices), precio de consumo por hora, GB o día.
"""
AZ = 'https://prices.azure.com/api/retail/prices (API de precios minoristas de Azure, consumo, 2026-11-11)'
H_MES = 730      # horas por mes que usa la calculadora de Azure
DIAS = 30

def eq(cat, clave, partida, desc, prov, mon, precio, cant, sitios, mes, fuente, nota=''):
    return dict(cat=cat, clave=clave, partida=partida, desc=desc, prov=prov, mon=mon, precio=precio, unidad='unidad', cant=cant,
                sitios=sitios, tipo='Única', ini=mes, fuente=fuente, nota=nota)
def az(clave, desc, precio, unidad, mult, cant, ini=3, prop=0.3, nota='', fuente=AZ, cat='Nube', prov='Microsoft Azure', partida='Nube (Azure)'):
    return dict(cat=cat, clave=clave, partida=partida, desc=desc, prov=prov, mon='USD', precio=precio, unidad=unidad, mult=mult, cant=cant,
                sitios=1, tipo='Mensual', ini=ini, fin=56, prop=prop, fuente=fuente, nota=nota)

SRV = ('EUR', 4544.49, 'https://aio.lv/en/product--dell-pmc8f--11650302.md (Dell PowerEdge R360, 32 GB, 480 GB)')
UPS = ('USD', 8329.99, 'https://www.cdw.com/product/apc-by-schneider-electric-smart-ups-srt-6000va-rm-230v/3793708')
R24 = ('USD', 1873.99, 'https://www.cdw.com/product/apc-netshelter-sx-24u-600mmx1070mm/1557398')
R42 = ('USD', 2466.00, 'https://www.shi.com/product/16045304/APC-NetShelter-SX-Enclosure-with-Sides')
PDU = ('USD', 1216.99, 'https://www.cdw.com/product/apc-metered-rack-pdu-zerou-2g-power-distribution-strip/2188807')
ATS = ('USD', 1780.99, 'https://www.zones.com/site/product/index.html?id=110846791 (APC AP4423A)')
GEN = ('USD', 17760.48, 'https://www.portlandiaelectric.supply/products/cummins-c20d6-20kw-generator')
CLI = ('USD', 5216.98, 'https://www.avendor.com/products/vertiv-vrc-outdoor-condensing-unit-1 y https://www.ipsecuritydepot.com/3-5kw-split-system-indoor-unit-gravity-drain/acrmd4kt-1/ (unidad exterior 2.873,99 + interior 2.342,99)')
SIN = 'Estimación sin fuente: supuesto del equipo por confirmar con cotización'

def tienda(sufijo, sitios, mes, lote):
    T = 'Equipos de tienda'
    n = f' ({lote})'
    return [
        eq(T, 'srv_t' + sufijo, 'SUM-07 Servidores de tienda', 'Servidor de tienda, 8 núcleos, 32 GiB, 2 SSD' + n, 'Dell', SRV[0], SRV[1], 4, sitios, mes, SRV[2], '2 de Retail y 2 de la filial emisora por tienda'),
        eq(T, 'arb_t' + sufijo, 'SUM-07 Árbitros', 'Árbitro del par de servidores (equipo compacto)' + n, 'Por definir', 'USD', 900, 2, sitios, mes, SIN),
        eq(T, 'rack_t' + sufijo, 'SUM-05 Racks', 'Rack de 24U' + n, 'APC', R24[0], R24[1], 3, sitios, mes, R24[2]),
        eq(T, 'ups_t' + sufijo, 'SUM-15 UPS', 'UPS en línea de 6 kVA' + n, 'APC', UPS[0], UPS[1], 2, sitios, mes, UPS[2]),
        eq(T, 'pdu_t' + sufijo, 'SUM-16 PDU', 'PDU medida de rack' + n, 'APC', PDU[0], PDU[1], 6, sitios, mes, PDU[2]),
        eq(T, 'ats_t' + sufijo, 'SUM-17 Transferidor', 'Transferidor automático de rack' + n, 'APC', ATS[0], ATS[1], 1, sitios, mes, ATS[2]),
        eq(T, 'gen_t' + sufijo, 'SUM-18 Grupo electrógeno', 'Grupo electrógeno diésel de 20 kW' + n, 'Cummins', GEN[0], GEN[1], 1, sitios, mes, GEN[2],
           'Se presupuesta en todas las tiendas; se omite donde la fuente del edificio se acredite'),
        eq(T, 'clima_t' + sufijo, 'SUM-20 Clima', 'Climatización de sala técnica, 3,5 kW' + n, 'Vertiv / APC', CLI[0], CLI[1], 1, sitios, mes, CLI[2]),
        eq(T, 'sens_t' + sufijo, 'SUM-22 Sensores', 'Sensores ambientales de sala técnica' + n, 'Por definir', 'USD', 600, 1, sitios, mes, SIN),
    ]

D = 'Equipos de DC-01'
ITEMS = (
    tienda('1', 4, 3, 'lote 1: laboratorio y 3 tiendas piloto, orden en M3')
    + tienda('2', 19, 5, 'lote 2: 19 tiendas, orden en M5')
    + [
        eq('Equipos de centros de distribución', 'srv_cd', 'Par local de captura', 'Servidor del par local de captura (lote 2, orden en M5)', 'Dell', SRV[0], SRV[1], 2, 2, 5, SRV[2]),
        eq(D, 'rack_dc', 'Racks de DC-01', 'Rack de 42U', 'APC', R42[0], R42[1], 4, 1, 1, R42[2], 'Orden de DC-01 el 11 de enero de 2027 (M1)'),
        eq(D, 'srv_dc', 'Pares de integración', 'Servidor de integración, un par por negocio', 'Dell', SRV[0], SRV[1], 4, 1, 1, SRV[2]),
        eq(D, 'fw_dc', 'Seguridad por negocio', 'Firewall con 3 años de protección, par por negocio', 'Fortinet',
           'USD', 11705.33, 4, 1, 1, 'https://datacenter360.ca/shop/network-security/firewall/appliance/fortigate-200f-hardware-plus-3-year-forticare-premium-and-fortiguard-unified-threat-protection-utp-fg-200f-bdl-950-36/'),
        eq(D, 'sw_dc', 'Conectividad por negocio', 'Switch de 48 puertos, par por negocio', 'HPE Aruba',
           'USD', 8159.15, 4, 1, 1, 'https://www.cdw.com/product/hpe-aruba-6300m-switch-48-ports-managed-rack-mountable/5836509 (JL663A)'),
        eq(D, 'ups_dc', 'Energía del recinto', 'UPS en línea de 6 kVA', 'APC', UPS[0], UPS[1], 2, 1, 1, UPS[2], 'Cantidad supuesta'),
        eq(D, 'pdu_dc', 'Energía del recinto', 'PDU medida de rack', 'APC', PDU[0], PDU[1], 8, 1, 1, PDU[2], 'Dos por rack'),
        eq(D, 'clima_dc', 'Climatización del recinto', 'Climatización de precisión, 3,5 kW', 'Vertiv / APC', CLI[0], CLI[1], 2, 1, 1, CLI[2], 'Cantidad supuesta'),
        eq(D, 'inc_dc', 'Incendio del recinto', 'Sistema de extinción con agente limpio', 'Por definir', 'USD', 25000, 1, 1, 1, SIN),
        eq(D, 'acc_dc', 'Acceso del recinto', 'Control de acceso del recinto técnico', 'Por definir', 'USD', 5000, 1, 1, 1, SIN),
        eq('Innovaciones', 'locker', 'Lockers Ancoa 24/7', 'Banco de lockers inteligente para retiro 24/7', 'Por definir', 'USD', 32000, 1, 22, 15,
           'https://www.clickncollect.com/insights/smart-locker-cost (precio medio de un banco)', 'Un banco por tienda es un supuesto; orden el 8 de marzo de 2028 (M15)'),
        eq('Innovaciones', 'locker_inst', 'Lockers Ancoa 24/7', 'Instalación e integración del banco de lockers', 'Por definir', 'USD', 10000, 1, 22, 15,
           'https://www.clickncollect.com/insights/smart-locker-cost (instalación: 3.000 a 25.000 USD)'),
        eq('Innovaciones', 'totem', 'Modo Tienda y fila virtual', 'Tótem táctil de autoservicio', 'Por definir', 'USD', 4500, 2, 22, 15,
           'https://koronapos.com/blog/how-much-do-self-checkout-machines-cost/ (unidad estándar: 4.500 a 8.000 USD)', 'Dos por tienda es un supuesto'),
        # ---- Azure, Chile Central (desde M3 a escala parcial; completa desde el mes de Parámetros)
        az('aks', 'Nodos de AKS, 8 vCPU y 32 GiB (D8s v5, Linux), Chile Central', 0.538, 'hora', H_MES, 40, nota='40 nodos; tamaño de referencia igual para todos los grupos'),
        az('vm_aux8', 'Máquinas auxiliares Windows de 8 vCPU (gateways de Power BI y SHIR)', 0.906, 'hora', H_MES, 8),
        az('vm_aux4', 'Máquinas auxiliares Windows de 4 vCPU (conectores de acceso privado)', 0.453, 'hora', H_MES, 4),
        az('vm_sonda', 'Sondas (B2s, Linux)', 0.0582, 'hora', H_MES, 2),
        az('pg_cpu', 'PostgreSQL Flexible Server, cómputo de propósito general', 0.1246, 'vCore-hora', H_MES, 192, nota='12 servidores × 8 vCore supuestos × 2 por alta disponibilidad zonal'),
        az('pg_disco', 'PostgreSQL Flexible Server, almacenamiento', 0.161, 'GiB-mes', 1, 9000, nota='4.500 GiB × 2 por alta disponibilidad zonal'),
        az('sb', 'Service Bus Premium, unidad de mensajería', 1.2985, 'hora', H_MES, 2),
        az('redis', 'Azure Managed Redis Balanced B20', 0.8806, 'hora', H_MES, 1),
        az('lago', 'Data Lake Storage Gen2, caliente con redundancia de zona', 0.0322, 'GB-mes', 1, 5120, nota='5 TiB'),
        az('evid', 'Blob de evidencia, caliente con redundancia de zona', 0.0322, 'GB-mes', 1, 5120, nota='5 TiB; precio del lago como referencia'),
        az('arch', 'Archivo inmutable, nivel frío con redundancia de zona', 0.0063, 'GB-mes', 1, 37888, nota='37 TiB'),
        az('fd', 'Front Door Premium, tarifa base', 330, 'mes', 1, 1, fuente='https://azure.microsoft.com/pricing/details/frontdoor/ (tarifa base mensual; no consultable por la API regional)'),
        az('agw', 'Application Gateway WAF v2, costo fijo', 0.50292, 'hora', H_MES, 2),
        az('agw_cu', 'Application Gateway WAF v2, unidades de capacidad', 0.020117, 'unidad-hora', H_MES, 20, nota='10 unidades por gateway, supuesto'),
        az('apim', 'API Management Premium, unidad en Chile Central', 3.829, 'hora', H_MES, 2),
        az('fw', 'Azure Firewall Premium, despliegue', 1.75, 'hora', H_MES, 3),
        az('fw_gb', 'Azure Firewall Premium, datos procesados', 0.016, 'GB', 1, 5000, nota='5.000 GB al mes, supuesto'),
        az('vpn', 'VPN Gateway VpnGw2AZ', 0.54, 'hora', H_MES, 2),
        az('bastion', 'Azure Bastion Standard', 0.29, 'hora', H_MES, 3),
        az('hsm', 'Managed HSM (Key Vault HSM Pool, Standard B1)', 3.2, 'hora', H_MES, 1, nota='Candidato para la filial emisora y X-01'),
        az('logs', 'Log Analytics, ingesta', 3.2131, 'GB', DIAS, 50, nota='50 GB al día, supuesto'),
        az('acr', 'Container Registry Premium', 1.6666, 'día', DIAS, 3),
        az('ddos', 'DDoS Network Protection, plan', 4.032258, 'hora', H_MES, 1, nota='Precio de otras regiones; no aparece por región en Chile Central'),
        az('entra', 'Entra ID P2', 9, 'usuario-mes', 1, 200, nota='200 usuarios con acceso privilegiado, supuesto',
           fuente='https://medhacloud.com/tools/m365-license-comparison/plans/entra-id-p2-addon (9 USD por usuario al mes; fuente de terceros)'),
        az('sentinel', 'Microsoft Sentinel, análisis de pago por uso (Brazil South)', 8.6, 'GB', DIAS, 20, nota='20 GB al día, supuesto; Chile Central no ofrece Sentinel'),
        # ---- Azure, Brazil South (pila de espera desde el mes de nube completa)
        az('br_vm', 'Máquinas de espera en Brazil South (D8s v5, Linux)', 0.612, 'hora', H_MES, 50, ini=13, prop=1, nota='50 máquinas encendidas para cumplir el RTO de 4 h'),
        az('br_pg', 'PostgreSQL, réplicas en Brazil South, cómputo', 0.12, 'vCore-hora', H_MES, 96, ini=13, prop=1, nota='12 réplicas × 8 vCore supuestos'),
        az('br_pg_d', 'PostgreSQL, réplicas en Brazil South, almacenamiento', 0.161, 'GiB-mes', 1, 4500, ini=13, prop=1, nota='Precio de Chile Central como referencia'),
        az('br_sb', 'Service Bus Premium en Brazil South', 0.9275, 'hora', H_MES, 2, ini=13, prop=1),
        az('br_apim', 'API Management Premium, gateway regional en Brazil South', 3.829, 'hora', H_MES, 2, ini=13, prop=1),
        az('br_agw', 'Application Gateway WAF v2 en Brazil South, costo fijo', 0.72, 'hora', H_MES, 2, ini=13, prop=1),
        az('br_fw', 'Azure Firewall Premium en Brazil South', 1.75, 'hora', H_MES, 3, ini=13, prop=1),
        az('br_vpn', 'VPN Gateway VpnGw2AZ en Brazil South', 0.54, 'hora', H_MES, 2, ini=13, prop=1),
        az('br_alm', 'Copia del lago y de la evidencia en Brazil South, caliente', 0.0326, 'GB-mes', 1, 10240, ini=13, prop=1, nota='10 TiB'),
        az('br_arch', 'Copia del archivo en Brazil South, nivel frío', 0.0158, 'GB-mes', 1, 37888, ini=13, prop=1, nota='37 TiB'),
        # ---- Licencias y seguridad
        az('edr', 'Protección de servidores (Defender for Servers Plan 2)', 15, 'servidor-mes', 1, 100, ini=5, prop=1, cat='Licencias y seguridad', partida='SUM-23 a 27 Seguridad',
           prov='Microsoft', nota='92 servidores de tienda, 4 de centros y 4 de DC-01',
           fuente='https://azure.microsoft.com/pricing/details/defender-for-cloud/ (unos 15 USD por servidor al mes; cifra de terceros)'),
        az('locker_sw', 'Software y soporte del banco de lockers', 250, 'banco-mes', 1, 22, ini=21, prop=1, cat='Licencias y seguridad', partida='Lockers Ancoa 24/7',
           prov='Por definir', nota='3.000 USD al año por banco (rango 1.500 a 5.000)', fuente='https://www.clickncollect.com/insights/smart-locker-cost'),
    ]
)

EST = 'Estimación de referencia sin cotización'
HARDWARE_CLIENTE = [
    ('Firewall de tienda con SD-WAN', 'Par por negocio, con protección contra amenazas', 'Fortinet FortiGate (gama de sucursal)', 4, 22, 1200, EST),
    ('Switch de acceso de tienda', '24 puertos con PoE, administrable', 'HPE Aruba (gama de acceso)', 4, 22, 2500, EST),
    ('Punto de acceso inalámbrico', 'Wi-Fi 6, cantidad según estudio de cobertura', 'Por definir', 8, 22, 600, EST + '; 8 por tienda es un supuesto'),
    ('Router 4G/5G con doble SIM', 'Respaldo móvil de 22 tiendas y 2 centros', 'Por definir', 1, 24, 900, EST),
    ('Cableado estructurado', 'Categoría 6 de baja emisión de humos, certificado', 'Instalador certificado', 1, 22, 15000, EST + ' por tienda'),
    ('Caja (POS)', 'Terminal de punto de venta', 'Por definir', 1, 380, 1500, EST + '; 380 cajas (Caso 09)'),
    ('Terminal de pago', 'Lector de tarjetas con contacto y sin contacto', 'Por definir', 1, 380, 350, EST),
    ('Impresora de boletas', 'Térmica', 'Por definir', 1, 380, 250, EST),
    ('Lector de códigos', 'Lector de mano 2D', 'Por definir', 1, 380, 200, EST),
    ('Dispositivo móvil de vendedor', 'Terminal móvil administrado', 'Por definir', 20, 22, 400, EST + '; 20 por tienda es un supuesto'),
    ('Obra civil de separación', 'Particiones, puertas y permisos de la sala técnica (SUM-31, 32)', 'Contratista del cliente', 1, 22, 20000, EST + ' por tienda'),
    ('Equipamiento de red de los centros', 'Firewall, switching y acceso inalámbrico por centro', 'Por definir', 1, 2, 12000, EST + ' por centro'),
]

# Meses de pago de cada compra única: orden (campo «ini»), entrega e instalación. Salen de calendario-compras.md,
# que sigue al SD-04 y a la red del SD-07; no se mueve ninguna fecha, solo se reparte el pago entre esos hitos.
#   DC-01: orden 11-ene-27 (M1), entrega 7-abr (M4), equipamiento instalado hasta el 5-may (M4).
#   Lote 1: orden 8-mar (M3), última entrega 2-jun (M5), instalación hasta el 18-jun (M6).
#   Lote 2: orden 7-may (M5), última entrega 3-ago (M7), en servicio el 19-sep (M9).
#   Innovaciones: orden 8-mar-28 (M15), entrega 5-may-28 (M16), instalación en sitios piloto 8 y 9-may-28 (M17).
_LOTE1 = ('srv_t1', 'arb_t1', 'rack_t1', 'ups_t1', 'pdu_t1', 'ats_t1', 'gen_t1', 'clima_t1', 'sens_t1')
_LOTE2 = ('srv_t2', 'arb_t2', 'rack_t2', 'ups_t2', 'pdu_t2', 'ats_t2', 'gen_t2', 'clima_t2', 'sens_t2', 'srv_cd')
_DC = ('rack_dc', 'srv_dc', 'fw_dc', 'sw_dc', 'ups_dc', 'pdu_dc', 'clima_dc', 'inc_dc', 'acc_dc')
for _it in ITEMS:
    if _it['tipo'] != 'Única':
        continue
    k = _it['clave']
    if k in _LOTE1: _it['ent'], _it['inst'] = 5, 6
    elif k in _LOTE2: _it['ent'], _it['inst'] = 7, 9
    elif k in _DC: _it['ent'], _it['inst'] = 4, 4
    elif k in ('locker', 'totem'): _it['ent'], _it['inst'] = 16, 17
    elif k == 'locker_inst': _it['ini'] = _it['ent'] = _it['inst'] = 17     # servicio: se paga al instalar
    else: raise KeyError(k)
