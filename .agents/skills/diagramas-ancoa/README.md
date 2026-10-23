# Harness de diagramas · Ancoa (Only Simple Solutions, TFEP-01/2026)

Restringe a la IA a **11 estilos de diagrama**, sacados de las 20 figuras del Subdocumento 4 y alineados con
el Modelo C4. Un diagrama solo se produce si su especificación JSON pasa el validador. Los renderizadores
aplican la paleta, los trazos, los íconos y la leyenda, y la IA no puede elegirlos.

## Contenido

| Ruta | Para qué sirve |
|------|----------------|
| `SKILL.md` | Instrucciones para la IA: reglas, flujo de trabajo y lista de revisión C4 |
| `catalogo.json` | Única fuente de verdad: estilos, paleta, trazos, estados, íconos permitidos, códigos y prohibiciones |
| `references/estilos.md` | Cuándo usar cada estilo, árbol de decisión y plantilla por estilo |
| `references/figuras/` | Páginas con las figuras 4.1–4.20 originales, como referencia visual |
| `scripts/validar.py` | Valida una especificación (códigos E01–E17) |
| `scripts/render_logico.py` | L1–L6 → PNG + SVG con diagrams + Graphviz (como las Fig. 4.1–4.12) |
| `scripts/render_fisico.py` | F1–F5 → .drawio con íconos oficiales de Azure (como las Fig. 4.13–4.20) |
| `scripts/previsualizar_drawio.py` | Vista previa PNG de un .drawio (Chromium + visor de draw.io) |
| `scripts/lint.py` | Revisa archivos escritos a mano (.py, .drawio, .md) y rechaza formatos prohibidos |
| `scripts/probar_harness.py` | Autoprueba: 5 ejemplos válidos pasan y 18 casos inválidos se rechazan |
| `ejemplos/` | Especificaciones de ejemplo: L3 (Fig. 4.4), L4 (Fig. 4.10), L5 (Fig. 4.12), F3 (Fig. 4.15), F4 (Fig. 4.16) |

## Uso rápido

```bash
pip install diagrams playwright          # requiere Graphviz (dot)
python3 scripts/probar_harness.py        # debe terminar en «TODO EN ORDEN»
python3 scripts/validar.py ejemplos/L3_bloque_tiendas.json
python3 scripts/render_logico.py ejemplos/L3_bloque_tiendas.json salida/fig_4_4
python3 scripts/render_fisico.py ejemplos/F4_puntos_falla.json salida/fig_4_16
```

## Cómo conectarlo a la IA

- **Claude Code:** copiar la carpeta a `.claude/skills/diagramas-ancoa/` del repositorio de la propuesta y
  añadir a `CLAUDE.md` la línea:
  `Todo diagrama se hace con la skill diagramas-ancoa; no se admiten otros estilos ni formatos.`
- **Servidor MCP o script propio** (como el que generó las Fig. 4.1–4.12): exponer `validar.py` como paso
  obligatorio antes del render y entregar al modelo `SKILL.md` + `references/estilos.md` como instrucciones.

## Lo que se encontró en el Subdocumento 4 y cómo lo resuelve el harness

Las figuras ya usan dos familias coherentes: 4.1–4.12 se hicieron con diagrams + Graphviz y 4.13–4.20 con
draw.io e íconos de Azure, según la declaración de uso de IA. Aun así hay inconsistencias que una revisión
con la lista C4 detectaría:

1. **Leyenda desigual.** 4.1 y 4.2 la explican solo en el texto. 4.4–4.9 la ponen en una línea de
   encabezado, 4.10 en un recuadro, 4.12 en el pie y 4.13–4.20 no tienen. El harness genera la leyenda dentro
   de cada figura, solo con lo que esa figura usa.
2. **Mismo significado, dos colores.** La autorización de compra es azul en 4.1 y «azul verdoso» en 4.12.
   El harness la unifica en un único token, `compra_autorizable`.
3. **Mismo color, varios significados.** El rojo es «denegado» en 4.12. El magenta es «tráfico por
   firewall» en 4.13–4.14 y «aprobación» en 4.15. El harness reserva el rojo para `denegado` (solo L5) y el
   magenta para la familia física, y diferencia sus dos usos por el tipo de trazo.
4. **Trazo discontinuo sobrecargado.** En 4.1 significa convivencia, en 4.10 contrato condicionado y en 4.16
   tanto «propuesto» como «réplica». El harness da a cada semántica una combinación única de color y patrón;
   la réplica, por ejemplo, usa trazo largo.
5. **Figuras giradas.** 4.11 y 4.12 están rotadas 90° en la página. L5 y L6 se dibujan de izquierda a
   derecha para que quepan sin girar.
6. **Flechas sin rótulo.** Muchas flechas de 4.1–4.9 no dicen su intención. El harness lo exige en los cruces
   entre contenedores: es error en L4, L5 y L6, y aviso en L1 y L3.

## Limitaciones conocidas

- El trazado automático de draw.io puede cruzar líneas cuando hay nodos alineados; se ajusta a mano en draw.io
  sin cambiar íconos, colores ni trazos (ver Fig. F4 de ejemplo, réplicas a CLD-02).
- Los equipos que no son de Azure (FortiGate, switches, UPS, cámaras…) usan la biblioteca clip-art incluida
  en draw.io, porque los íconos oficiales de Azure no los cubren. Todas las rutas de ícono del catálogo se
  verificaron contra el repositorio jgraph/drawio el 21-10-2026.
- El harness no comprueba que el contenido sea correcto (que un servicio exista o que una ruta esté
  acreditada). Eso sigue siendo revisión humana, como indica la Tabla 4.17.
