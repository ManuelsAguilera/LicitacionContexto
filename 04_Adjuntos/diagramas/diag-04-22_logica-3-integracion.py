"""Vista lógica 3 de 3: capa de integración y resiliencia frente a terceros.

Responde: ¿cómo conversa la solución con lo que no construye y qué pasa cuando un tercero falla?
Sigue FEP01 (diap. 50 a 56): la integración se separa en una capa propia, con adaptadores, contrato y patrones de
resiliencia, sin base de datos compartida; los sistemas externos van con otro color y fuera del borde del sistema.
Fuente: SD-04 (4.1, integración y eventos) y Bases Transversales (RT-02.06 a RT-02.09).
Ejecutar: python3 04_Adjuntos/diagramas/diag-04-22_logica-3-integracion.py
"""

from pathlib import Path

from _alcance import box, container, legend
from _drawio import Diagram

d = Diagram(font=24, zone_font=27)
W = 3

srv = box(d, 20, 140, 330, 900, "Servicios de negocio",
          ["", "Oferta comercial", "Abastecimiento", "Existencias", "Pedidos", "Ventas", "Comisiones", "Marketplace",
           "Posventa", "Clientes Retail", "", "Originación · Cartera", "Evidencia financiera"], lsize=23, icon="services")

cap = container(d, 420, 100, 1150, 980, "Capa de integración")
hechos = box(d, 450, 170, 520, 300, "Hechos confirmados",
             ["Registro de salida por servicio", "Entrega al menos una vez", "Cada consumidor deduplica,", "confirma y reintenta"], lsize=23, icon="exchange")
adapt = box(d, 1000, 170, 540, 300, "Adaptadores por sistema",
            ["Traducen y aíslan el modelo", "de cada sistema externo", "Cada uno declara su contrato:", "autoridad, dirección, frecuencia,", "versión, plazo y conciliación"], lsize=23, icon="gateway")

res = container(d, 450, 520, 1090, 520, "Resiliencia en toda llamada externa")
P = [("Tiempo límite", ["explícito en toda", "llamada remota"]),
     ("Reintento", ["con espera creciente", "y número máximo"]),
     ("Cortacircuitos", ["deja de llamar tras", "fallas seguidas"]),
     ("Idempotencia", ["clave única: un", "reintento no duplica"]),
     ("Mamparos", ["aíslan los recursos", "de cada sistema"]),
     ("Modo degradado", ["sigue con función", "reducida y avisa"]),
     ("Cola de fallidos", ["los errores persistentes", "pasan a revisión"])]
for k, (t, lines) in enumerate(P):
    r, c = divmod(k, 4)
    box(d, 470 + c * 262, 600 + r * 215, 245, 195, t, lines, lsize=21, tsize=24)
d.text(1560 - 280, 1000, 270, 36, "", size=20)

ex = 1650
x1 = box(d, ex, 140, 420, 330, "Sistemas del Cliente\nque se conservan", ["ERP y facturación", "Almacén (WMS)", "Marketplace", "Comercio electrónico*", "Fidelización*"],
         scope="cliente", lsize=23, icon="building")
x2 = box(d, ex, 510, 420, 270, "Plataformas actuales\nen convivencia", ["Núcleo Retail 2009", "Crédito 2011", "Punto de venta 2014"], scope="cliente", dashed=True, lsize=23, icon="server")
x3 = box(d, ex, 820, 420, 300, "Terceros", ["Medios de pago", "Transportistas", "Proveedores", "Fiscalización"], scope="tercero", lsize=23, icon="truck")

legend(d, 20, 1130, 330, extra=[("solid", "#1F1F1F", 3, "Llamada con respuesta"), ("dashed", "#1F1F1F", 3, "Hecho confirmado")])
d.text(430, 1130, 1700, 140,
       "Sin base de datos compartida: todo intercambio con un sistema externo pasa por un adaptador y un contrato.\n"
       "Los patrones de resiliencia protegen cada adaptador: la caída de un tercero no detiene a los servicios de negocio.\n"
       "* Se conservan al inicio; su destino lo decide la Etapa 1.", size=23, align="left")

d.edge(srv, hechos, "", line="dashed", width=W, exit=(1, 0.12), entry=(0, 0.26))
d.edge(srv, adapt, "", width=W, exit=(1, 0.045), entry=(0, 0.2), points=[(385, 181), (385, 135), (985, 135), (985, 230)])
d.edge(hechos, adapt, "", line="dashed", width=W, exit=(1, 0.5), entry=(0, 0.5))
d.edge(res, adapt, "", width=W, exit=(0.9, 0), entry=(0.5, 1))
d.edge(adapt, x1, "", width=W, exit=(1, 0.3), entry=(0, 0.5), points=[(1590, 260), (1590, 305)])
d.edge(adapt, x2, "", width=W, exit=(1, 0.6), entry=(0, 0.5))
d.edge(adapt, x3, "", width=W, exit=(1, 0.9), entry=(0, 0.5), points=[(1600, 440), (1600, 970)])

d.save(Path(__file__).with_suffix(".drawio"), formats=("png", "pdf"), scale=2)
