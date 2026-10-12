"""Genera la figura funcional del SD-13 desde una fuente editable."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
image = Image.new("RGB", (1800, 1050), "white")
draw = ImageDraw.Draw(image)
font_path = Path("C:/Windows/Fonts/arial.ttf")
font = ImageFont.truetype(str(font_path), 28)
small = ImageFont.truetype(str(font_path), 24)
title = ImageFont.truetype(str(font_path), 38)
blue = "#173A63"
draw.text((60, 35), "Cartera de innovaciones en el ámbito retail", font=title, fill=blue)
draw.rounded_rectangle((30, 100, 1770, 900), radius=20, outline=blue, width=4)

def box(bounds, lines, fill):
    draw.rounded_rectangle(bounds, radius=14, fill=fill, outline=blue, width=2)
    x, y, _, _ = bounds
    for index, line in enumerate(lines):
        draw.text((x + 18, y + 20 + index * 38), line, font=font, fill=blue)

def arrow(start, end):
    draw.line((start, end), fill=blue, width=4)
    x, y = end
    draw.polygon([(x, y), (x - 13, y - 18), (x + 13, y - 18)], fill=blue)

box((60, 150, 530, 290), ["Servicio de pedidos", "Preparación y entrega"], "#EAF2FA")
box((665, 150, 1135, 290), ["Servicio de existencias", "Historia y disponibilidad"], "#EAF2FA")
box((1270, 150, 1740, 290), ["Servicio de oferta comercial", "Catálogo y precios"], "#EAF2FA")
box((60, 400, 530, 550), ["13.1 Lockers 24/7", "Retiro autorizado", "Capa de integración / tienda"], "#EAF7EF")
box((665, 400, 1135, 550), ["13.2 Conteo predictivo", "Prioridad de recuento", "Capa de aplicación retail"], "#EAF7EF")
box((1270, 400, 1740, 550), ["13.3 Búsqueda multimodal", "Texto e imagen", "Canal digital / aplicación"], "#EAF7EF")
arrow((295, 290), (295, 400))
arrow((900, 290), (900, 400))
arrow((1505, 290), (1505, 400))
box((60, 680, 530, 830), ["13.5 Modo Tienda", "Clientes Retail / móvil", "Fila local y tótem"], "#EAF7EF")
box((665, 680, 1135, 830), ["Plataforma de integración", "Identidad y auditoría", "Despliegue híbrido"], "#EAF2FA")
box((1270, 680, 1740, 830), ["13.4 Retail Media", "Catálogo y disponibilidad", "Campañas del retail"], "#EAF7EF")
draw.text((55, 925), "Datos financieros fuera del ámbito de esta cartera. Conexiones mediante contratos de servicio.", font=small, fill=blue)
draw.text((55, 970), "Fuente: elaboración propia de Only Simple Solutions. Los cuadros indican ubicación funcional.", font=small, fill=blue)
image.save(ROOT / "diag-13-00_cartera.png")
