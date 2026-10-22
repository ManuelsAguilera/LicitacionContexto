"""Prueba de integración MCP stdio. Deja muestras identificadas en tmp/diagramas-ancoa/."""
import asyncio
from datetime import timedelta
import json
import os
from pathlib import Path
import sys
from uuid import uuid4
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from _comun import RAIZ

ROOT = RAIZ.parents[2]


async def main():
    carpeta = 'tmp/diagramas-ancoa/prueba-' + uuid4().hex[:12]
    env = dict(os.environ)
    env['PYTHONIOENCODING'] = 'utf-8'
    params = StdioServerParameters(command=sys.executable, args=[str(RAIZ / 'scripts/mcp_servidor.py')], env=env)
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write, read_timeout_seconds=timedelta(seconds=30)) as session:
            await session.initialize()
            names = {t.name for t in (await session.list_tools()).tools}
            assert names == {'catalogo_diagramas', 'validar_diagrama', 'renderizar_diagrama'}, names
            for family, name in [('L', 'L4_venta_sin_enlace'), ('F', 'F4_puntos_falla')]:
                spec = json.loads((RAIZ / 'ejemplos' / (name + '.json')).read_text(encoding='utf-8'))
                result = await session.call_tool('renderizar_diagrama', {'especificacion': spec, 'salida': carpeta + '/ejemplo_' + family})
                assert not result.isError, result.content
                data = result.structuredContent or json.loads(result.content[0].text)
                assert data['renderizado'] and all(Path(p).is_file() for p in data['archivos']), data
                print('Render MCP', family, 'OK', flush=True)
            spec = json.loads((RAIZ / 'pruebas/E12_linea_roja.json').read_text(encoding='utf-8'))
            result = await session.call_tool('renderizar_diagrama', {'especificacion': spec, 'salida': carpeta + '/denegado'})
            data = result.structuredContent or json.loads(result.content[0].text)
            assert not data['valido'] and not (ROOT / carpeta / 'denegado.json').exists(), data
            print('Cruce prohibido sin escritura OK', flush=True)
            spec = json.loads((RAIZ / 'ejemplos/F4_puntos_falla.json').read_text(encoding='utf-8'))
            for path in ['../escape', 'AGENTS', carpeta + '/ejemplo_F']:
                result = await session.call_tool('renderizar_diagrama', {'especificacion': spec, 'salida': path})
                assert result.isError, path
            print('Rutas y sobrescritura rechazadas OK', flush=True)
    print('TODO EN ORDEN. Muestras:', carpeta)


if __name__ == '__main__':
    asyncio.run(main())
