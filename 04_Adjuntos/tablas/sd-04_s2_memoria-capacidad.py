"""Memoria de capacidad del sd-04 (Caso 09, cap. 14.2): seis de las diecisiete dimensiones, con su derivación.

Los datos de partida son del Caso (con folio impreso). Los supuestos son del proponente y están
declarados en SUPUESTOS. Para cambiar un supuesto se edita aquí y se vuelve a ejecutar:
    python3 04_Adjuntos/tablas/sd-04_s2_memoria-capacidad.py
El script escribe sd-04_s2_memoria-capacidad.md junto a este archivo.
"""

from pathlib import Path

# ---- Datos del Caso 09 (proyección a 3 años, cap. 14, núm. 14.1, p. 31) ----
DATOS = {
    "documentos_venta_anio": (36_000_000, "Documentos de venta emitidos al año, proyección a 3 años (p. 31)"),
    "lineas_venta_anio": (83_000_000, "Líneas de venta al año, proyección a 3 años (p. 31)"),
    "pedidos_linea_anio": (3_100_000, "Pedidos del canal en línea al año, proyección a 3 años (p. 31)"),
    "pedidos_evento_3dias": (150_000, "Pedidos en los 3 días del evento anual, proyección a 3 años (p. 31)"),
    "lineas_caja": (430, "Líneas de caja, proyección a 3 años (p. 31); el numeral 14.2 habla de las 380 de hoy"),
    "evaluaciones_anio": (640_000, "Evaluaciones crediticias en el punto de venta al año, proyección a 3 años (p. 31)"),
    "cambios_precio_dia": (400_000, "Cambios de precio en un día de campaña (p. 31)"),
    "plazo_precio_s": (300, "Plazo máximo de propagación de precio a cajas y canal digital: 5 minutos (RT-05.29, p. 34)"),
}

# ---- Supuestos del proponente ----
SUPUESTOS = {
    "horas_venta_dia": (12, "Las tiendas venden 12 horas al día (inferencia del perfil, que muestra apertura a las 10:00 y cierre entre las 20:00 y las 23:00, apéndice B, núm. B.1, p. 48); los pedidos en línea se cuentan aparte, y si ya están en los documentos de venta la cifra sobrestima"),
    "factor_hora_peak": (2.5, "La hora peak normal es 2,5 veces el promedio horario"),
    "frac_evento_dia1": (0.5, "El 50 % de los pedidos del evento cae el primer día"),
    "frac_dia1_en_peak": (0.5, "La mitad del primer día cae en la franja peak digital"),
    "horas_peak_digital": (4, "Peak digital de 18:00 a 22:00 (apéndice B, núm. B.1, p. 48)"),
    "frac_rafaga": (0.1, "El 10 % de los pedidos del evento llega en los primeros 5 minutos de la apertura"),
    "rafaga_s": (300, "Duración de la ráfaga de apertura del evento: 5 minutos"),
    "consultas_por_visita": (50, "Cada visita hace 50 consultas de disponibilidad durante su sesión"),
    "conversion": (0.02, "2 % de las visitas termina en pedido"),
    "sesion_s": (240, "La sesión media dura 4 minutos"),
    "clientes_caja_hora": (60, "Cada línea de caja atiende 60 clientes por hora (uno por minuto) en un sábado de diciembre"),
    "factor_navidad": (3, "El peak de Navidad triplica el promedio diario de evaluaciones crediticias"),
    "horas_peak_presencial": (7, "Peak presencial de 13:00 a 20:00 (apéndice B, núm. B.1, p. 48)"),
    "consumidores_precio": (5, "Consumidores de un cambio de precio: cajas, móviles, canal digital, etiquetas y analítica (supuesto; el Caso menciona cajas, canal digital y 310.000 etiquetas, y RT-05.29 fija 5 minutos por cambio, de modo que exigir los 400.000 cambios en ese plazo es una lectura conservadora)"),
}

d = {k: v[0] for k, v in DATOS.items()}
s = {k: v[0] for k, v in SUPUESTOS.items()}

seg_dia = s["horas_venta_dia"] * 3600
prom = (d["documentos_venta_anio"] + d["pedidos_linea_anio"]) / (365 * seg_dia)
peak_normal = prom * s["factor_hora_peak"]

pedidos_s = d["pedidos_evento_3dias"] * s["frac_evento_dia1"] * s["frac_dia1_en_peak"] / (s["horas_peak_digital"] * 3600)
visitas_s = pedidos_s / s["conversion"]
consultas_s = visitas_s * s["consultas_por_visita"]
rafaga_s = d["pedidos_evento_3dias"] * s["frac_rafaga"] / s["rafaga_s"]
concurrentes = visitas_s * s["sesion_s"]

ventas_s = d["lineas_caja"] * s["clientes_caja_hora"] / 3600
lineas_s = ventas_s * d["lineas_venta_anio"] / d["documentos_venta_anio"]

eval_dia = d["evaluaciones_anio"] / 365
eval_peak_dia = eval_dia * s["factor_navidad"]
eval_s = eval_peak_dia / (s["horas_peak_presencial"] * 3600)

precios_pub_s = d["cambios_precio_dia"] / d["plazo_precio_s"]
precios_ent_s = precios_pub_s * s["consumidores_precio"]


def f(x, n=1):
    return f"{x:,.{n}f}".replace(",", "X").replace(".", ",").replace("X", ".")


RESULTADOS = [
    ("Transacciones por segundo en régimen normal",
     f"{f(prom)} promedio y {f(peak_normal)} en hora peak",
     "(documentos de venta + pedidos en línea) ÷ (365 días × 12 h × 3.600 s), y la hora peak es 2,5 veces el promedio"),
    ("Transacciones por segundo en el peak del primer día del evento",
     f"{f(pedidos_s)} pedidos por segundo sostenidos y {f(rafaga_s, 0)} en la ráfaga de apertura",
     "150.000 pedidos × 50 % (primer día) × 50 % (franja de 4 h) ÷ 14.400 s, y 150.000 × 10 % ÷ 300 s en la ráfaga"),
    ("Consultas de disponibilidad por segundo y personas concurrentes en ese peak",
     f"{f(consultas_s, 0)} consultas por segundo y unas {f(concurrentes, 0)} personas concurrentes",
     "visitas por segundo (pedidos ÷ 2 %) × 50 consultas por visita, y visitas por segundo × 240 s de sesión"),
    ("Transacciones por segundo un sábado de diciembre, sumando las líneas de caja (430 proyectadas, 380 hoy)",
     f"{f(ventas_s)} ventas por segundo y {f(lineas_s)} líneas por segundo",
     "430 líneas de caja × 60 clientes por hora ÷ 3.600 s, con 2,3 líneas por documento"),
    ("Evaluaciones crediticias por segundo en el peak del punto de venta",
     f"{f(eval_s, 2)} por segundo",
     "640.000 ÷ 365 días × 3 (peak de Navidad) ÷ (7 h × 3.600 s)"),
    ("Eventos por segundo en una carga masiva de precios de campaña",
     f"{f(precios_pub_s, 0)} publicados y {f(precios_ent_s, 0)} entregados por segundo",
     "400.000 cambios ÷ 300 s (plazo de 5 minutos), y cada cambio llega a 5 tipos de consumidor"),
]

md = ["# Memoria de capacidad (sd-04, 4.2)", "",
      "Documento de apoyo del subdocumento 4. Responde a las seis primeras de las diecisiete dimensiones que el Caso 09 pide estimar y declarar como "
      "supuesto en el capítulo 14, numeral 14.2 (p. 32). Las once restantes se derivan en el diseño detallado de la Etapa 1. Son estimaciones y no mediciones. Se corrigen con el "
      "levantamiento y la prueba de carga de la Etapa 1. Para cambiar un supuesto se edita "
      "`sd-04_s2_memoria-capacidad.py` y se vuelve a ejecutar.", "",
      "## Datos de partida del Caso 09", "", "| Dato | Valor |", "| :--- | ---: |"]
md += [f"| {txt} | {f(v, 0)} |" for v, txt in DATOS.values()]
md += ["", "## Supuestos del proponente", "", "| Supuesto | Valor |", "| :--- | ---: |"]
md += [f"| {txt} | {str(v).replace('.', ',')} |" for v, txt in SUPUESTOS.values()]
md += ["", "## Resultados", "", "| Cifra del Caso 14.2 | Valor | Derivación |", "| :--- | :--- | :--- |"]
md += [f"| {a} | {b} | {c} |" for a, b, c in RESULTADOS]
md += ["", "## Uso en el diseño", "",
       "De estas cifras se derivan en el diseño detallado las unidades de API Management, las particiones de Event Hubs, "
       "la capacidad de PostgreSQL, los nodos de AKS, el ancho de banda de cada enlace y el tamaño de cada subred.", ""]
out = Path(__file__).with_suffix(".md")
out.write_text("\n".join(md), encoding="utf-8")
print(out)
for a, b, _ in RESULTADOS:
    print(a, "->", b)
