"""MCP local de la guía Ancoa: especificaciones JSON, validación antes de renderizar.

No acepta código Python del cliente. Las salidas se limitan al repositorio.
"""
from pathlib import Path
import json
import re

from mcp.server.fastmcp import FastMCP
from _comun import CATALOGO, RAIZ
from validar import validar

PROYECTO = RAIZ.parents[2]
DESTINOS = (PROYECTO / '04_Adjuntos' / 'diagramas', PROYECTO / 'tmp' / 'diagramas-ancoa')
mcp = FastMCP('diagramas-ancoa', instructions=(
    'Consultar catalogo_diagramas y la skill diagramas-ancoa. Enviar especificaciones JSON; '
    'renderizar_diagrama valida antes de generar. La validez gráfica no certifica el contenido.'
))


def comprobar(especificacion: dict) -> dict:
    try:
        errores, avisos = validar(especificacion)
        return {'valido': not errores, 'errores': errores, 'avisos': avisos}
    except (KeyError, TypeError, ValueError, AttributeError, RecursionError) as exc:
        return {'valido': False, 'errores': [f'Especificación mal formada: {type(exc).__name__}'], 'avisos': []}


@mcp.tool()
def catalogo_diagramas() -> dict:
    """Devuelve el catálogo de estilos, códigos, símbolos y semánticas admitidos."""
    return CATALOGO


@mcp.tool()
def validar_diagrama(especificacion: dict) -> dict:
    """Comprueba una especificación sin escribir archivos ni ejecutar código del cliente."""
    return comprobar(especificacion)


@mcp.tool()
def renderizar_diagrama(especificacion: dict, salida: str) -> dict:
    """Valida y genera L→PNG/SVG o F→drawio. salida es una ruta relativa sin extensión.

    Destinos admitidos: 04_Adjuntos/diagramas/ o tmp/diagramas-ancoa/.
    No reemplaza ningún archivo existente. Los avisos requieren revisión.
    """
    resultado = comprobar(especificacion)
    if not resultado['valido']:
        return resultado
    destino = (PROYECTO / salida).resolve()
    if not any(destino.is_relative_to(p.resolve()) for p in DESTINOS):
        raise ValueError('La salida debe permanecer en 04_Adjuntos/diagramas o tmp/diagramas-ancoa')
    if not re.fullmatch(r'[A-Za-z0-9_-]+', destino.name):
        raise ValueError('Usar un nombre sin extensión con letras, números, guion o guion bajo')
    familia = CATALOGO['estilos'][especificacion['estilo']]['familia']
    extensiones = ['.png', '.svg', '.leyenda.txt'] if familia == 'logica' else ['.drawio', '.leyenda.txt']
    if especificacion.get('composicion') in ('columnas_referencia','columnas_organizadas','columnas_decisiones','columnas_legibles','bandas_horizontales'):
        extensiones.append('.drawio')
    extensiones += ['.json']
    archivos = [destino.with_suffix(ext) for ext in extensiones]
    if any(p.exists() for p in archivos) or destino.exists():
        raise ValueError('La salida ya existe; elegir otro nombre para conservar la versión anterior')
    destino.parent.mkdir(parents=True, exist_ok=True)
    spec = destino.with_suffix('.json')
    spec.write_text(json.dumps(especificacion, ensure_ascii=False, indent=2), encoding='utf-8')
    if familia == 'logica':
        from render_logico import renderizar
    else:
        from render_fisico import renderizar
    renderizar(especificacion, destino)
    resultado.update({'renderizado': all(p.exists() for p in archivos),
                      'archivos': [str(p) for p in archivos if p.exists()]})
    return resultado


if __name__ == '__main__':
    mcp.run(transport='stdio')
