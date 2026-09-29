"""Genera el snapshot del estado de Jira antes de la reestructuración.

Parsea el volcado de una búsqueda JQL (guardado por el MCP de opencode) y
escribe un JSON con clave, tipo, padre, resumen, descripción, estado,
prioridad y etiquetas de cada incidencia del proyecto OSS.

Uso:
    python 05_Gestion/jira/scripts/snapshot_desde_jql.py <archivo_volcado.json> <salida.json>
"""

import json
import sys


def main(entrada, salida):
    with open(entrada, encoding='utf-8') as f:
        crudo = f.read()

    # El volcado del MCP viene envuelto en un bloque ```json ... ```.
    if crudo.lstrip().startswith('```'):
        crudo = crudo.split('```')[1]
        if crudo.lstrip().startswith('json'):
            crudo = crudo.lstrip()[4:]

    datos = json.loads(crudo)
    issues = datos['issues']

    snapshot = []
    for i in issues:
        f = i['fields']
        padre = f.get('parent')
        snapshot.append({
            'clave': i['key'],
            'tipo': f['issuetype']['name'],
            'nivelJerarquia': f['issuetype']['hierarchyLevel'],
            'resumen': f['summary'],
            'descripcion': f.get('description'),
            'padre': padre['key'] if padre else None,
            'estado': f['status']['name'],
            'prioridad': (f.get('priority') or {}).get('name'),
            'etiquetas': f.get('labels') or [],
        })

    snapshot.sort(key=lambda x: int(x['clave'].split('-')[1]))

    with open(salida, 'w', encoding='utf-8') as f:
        json.dump(snapshot, f, ensure_ascii=False, indent=2)

    por_tipo = {}
    for s in snapshot:
        por_tipo[s['tipo']] = por_tipo.get(s['tipo'], 0) + 1
    print(f"{salida}: {len(snapshot)} incidencias")
    for t, n in sorted(por_tipo.items(), key=lambda x: -x[1]):
        print(f"  {n:>3}  {t}")


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
