"""Genera el plan de reestructuración del backlog OSS.

Deriva la estructura objetivo desde el snapshot tomado del estado real de Jira,
de modo que el plan no dependa de transcripciones manuales.

El proyecto OSS es classic (company-managed): los niveles de jerarquía no se
pueden saltar (Épica 1 -> Historia/Tarea 0 -> Subtarea -1). Por eso el
agrupamiento vive en un único nivel de épica y el detalle de cada sección baja
a Historia -> Subtarea.

Salida: 05_Gestion/jira/plan/restructuracion_2026-09-29_plan.json
"""

import json
import re
from rutas import RUTA_ORIGEN, RUTA_PLAN

SNAPSHOT = RUTA_ORIGEN
SALIDA = RUTA_PLAN

# Agrupadoras. El capítulo 4 se parte en tres porque su temática es distinta:
# arquitectura lógica, arquitectura física e implementos, y data center.
AGRUPADORAS = [
    {
        'id': 'E-1',
        'resumen': '1. Capítulo 1 — Presentación de la Empresa',
        'descripcion': (
            'Épica agrupadora del capítulo 1. Reúne las secciones 1. a 1.6 del '
            'índice del informe (Formulario T-7): quién es la empresa, cómo se '
            'gobierna internamente y qué capacidades acreditan para ejecutar el '
            'proyecto.'
        ),
        'cap': 'cap-1',
        'secciones': ['OSS-72', 'OSS-69', 'OSS-73', 'OSS-74',
                      'OSS-75', 'OSS-76', 'OSS-77'],
    },
    {
        'id': 'E-2',
        'resumen': '2. Capítulo 2 — Problema y Necesidad',
        'descripcion': (
            'Épica agrupadora del capítulo 2. Reúne las secciones 2. a 2.5: '
            'síntesis del problema, comprensión del contexto de la industria, '
            'dimensionamiento, actores e intereses, y el resumen de '
            'requerimientos, supuestos, exclusiones y restricciones.'
        ),
        'cap': 'cap-2',
        'secciones': ['OSS-78', 'OSS-79', 'OSS-80',
                      'OSS-81', 'OSS-82', 'OSS-83'],
    },
    {
        'id': 'E-3',
        'resumen': '3. Capítulo 3 — Alcance y Esquema de la Solución',
        'descripcion': (
            'Épica agrupadora del capítulo 3. Reúne las secciones 3. a 3.4: '
            'resumen ejecutivo de la solución, alcance, esquema de solución y '
            'explicación funcional. El alcance arrastra el Formulario T-12.'
        ),
        'cap': 'cap-3',
        'secciones': ['OSS-84', 'OSS-85', 'OSS-86', 'OSS-87', 'OSS-88'],
    },
    {
        'id': 'E-4',
        'resumen': '4. Capítulo 4 — Arquitectura Lógica',
        'descripcion': (
            'Épica agrupadora (lógica) del capítulo 4. Reúne 4., 4.1 y 4.1.1: '
            'diagrama lógico, módulos, vistas por dominio, flujos de actor y '
            'justificación del stack de software. Debe mapear al 100 % con el '
            'esquema de solución del capítulo 3.'
        ),
        'cap': 'cap-4',
        'secciones': ['OSS-89', 'OSS-90', 'OSS-91'],
    },
    {
        'id': 'E-5',
        'resumen': '4. Capítulo 4 — Arquitectura Física e Implementos',
        'descripcion': (
            'Épica agrupadora (física) del capítulo 4. Reúne 4.2 y 4.2.1: '
            'flujo físico derivado del diagrama lógico, zonas, segmentación de '
            'red e inventario de hardware y software a provisión.'
        ),
        'cap': 'cap-4',
        'secciones': ['OSS-92', 'OSS-93'],
    },
    {
        'id': 'E-6',
        'resumen': '4. Capítulo 4 — Data Center',
        'descripcion': (
            'Épica agrupadora (data center) del capítulo 4. Reúne 4.3, 4.3.1 y '
            '4.3.2: estrategia de centros de datos, datacenter primario y '
            'datacenter secundario. Acá se demuestra el despliegue híbrido '
            'obligatorio (Art. 16° y RT-03) y se fijan RPO, RTO y conmutación.'
        ),
        'cap': 'cap-4',
        'secciones': ['OSS-94', 'OSS-95', 'OSS-96'],
    },
    {
        'id': 'E-7',
        'resumen': '5. Capítulo 5 — Modelo de Datos',
        'descripcion': (
            'Épica agrupadora del capítulo 5. Reúne las secciones 5. a 5.4: '
            'modelo de datos por dominio, gestión de datos, estrategia de '
            'migración y estrategia de desempeño.'
        ),
        'cap': 'cap-5',
        'secciones': ['OSS-97', 'OSS-98', 'OSS-99', 'OSS-100', 'OSS-101'],
    },
    {
        'id': 'E-8',
        'resumen': '13. Capítulo 13 — Innovaciones',
        'descripcion': (
            'Épica agrupadora del capítulo 13. Reúne 13., 13.3 y 13.4. Solo se '
            'cargan las innovaciones 3 y 4: las 1 y 2 todavía no tienen '
            'secciones en el índice del informe y deben agregarse aparte.'
        ),
        'cap': 'cap-13',
        'secciones': ['OSS-102', 'OSS-103', 'OSS-104'],
    },
]

# "3. Introducción" (OSS-84) quedó sin tarea en la importación original: el
# script jira_user_story_mapping.py la declaraba, pero nunca llegó a Jira.
# Se recupera acá para no perder el índice.
TAREA_RECUPERADA = {
    'seccion': 'OSS-84',
    'resumen': 'Redactar el resumen del capítulo y su conexión con los demás '
               'capítulos, anexos y formularios',
    'descripcion': 'Sección del informe: 3. Introducción',
    'tipoOriginal': 'Tareas',
    'origenClave': None,
    'etiquetas': ['cap-3', 'sec-3', 'tipo-tarea'],
}

# La importación original dejó tareas sin padre. Se reencuentran por la
# sección que declaran en su descripción, así el reencuadre no depende de
# conocer las claves huérfanas de antemano.
PREFIJO_SECCION = 'Sección del informe: '

TIPOS_A_ETIQUETA = {
    'Trabajo Tecnico': 'tipo-tt',
    'Spikes': 'tipo-spike',
    'Tareas': 'tipo-tarea',
}


def etiqueta_seccion(resumen):
    """'4.1.1 Especificaciones...' -> 'sec-4-1-1';  '13.3 Innovación' -> 'sec-13-3'."""
    m = re.match(r'^(\d+(?:\.\d+)*)\.?\s', resumen)
    if not m:
        return None
    return 'sec-' + m.group(1).replace('.', '-')


def main():
    with open(SNAPSHOT, encoding='utf-8') as f:
        snap = {s['clave']: s for s in json.load(f)}

    plan = {'agrupadoras': [], 'secciones': [], 'subtareas': [], 'aBorrar': []}

    # Tareas huérfanas, indexadas por la sección que declaran en la descripción.
    huerfanas = {}
    for s in snap.values():
        desc = s['descripcion'] or ''
        if s['padre'] is None and desc.startswith(PREFIJO_SECCION):
            huerfanas.setdefault(desc[len(PREFIJO_SECCION):].strip(), []).append(s)

    for ag in AGRUPADORAS:
        cap = ag['cap']
        plan['agrupadoras'].append({
            'id': ag['id'],
            'resumen': ag['resumen'],
            'descripcion': ag['descripcion'],
            'etiquetas': [cap],
            'secciones': ag['secciones'],
        })

        for clave in ag['secciones']:
            sec = snap[clave]
            etiqueta_sec = etiqueta_seccion(sec['resumen'])
            if not etiqueta_sec:
                raise SystemExit(f"No se pudo derivar la etiqueta de {clave}: "
                                 f"{sec['resumen']!r}")

            plan['secciones'].append({
                'clave': clave,
                'resumen': sec['resumen'],
                'agrupadora': ag['id'],
                'tipoActual': sec['tipo'],
                'descripcion': sec['descripcion'],
                'etiquetas': sorted([cap, etiqueta_sec]),
            })

            # Hijas: las que ya tenía, más las huérfanas que declaran esta
            # misma sección en su descripción.
            hijas = [s for s in snap.values() if s['padre'] == clave]
            hijas += huerfanas.pop(sec['resumen'], [])
            for tarea in hijas:
                plan['subtareas'].append({
                    'origenClave': tarea['clave'],
                    'seccion': clave,
                    'resumen': tarea['resumen'],
                    'descripcion': tarea['descripcion'],
                    'tipoOriginal': tarea['tipo'],
                    'etiquetas': sorted([cap, etiqueta_sec,
                                         TIPOS_A_ETIQUETA[tarea['tipo']]]),
                })
                plan['aBorrar'].append(tarea['clave'])

    plan['subtareas'].append(dict(TAREA_RECUPERADA))

    with open(SALIDA, 'w', encoding='utf-8') as f:
        json.dump(plan, f, ensure_ascii=False, indent=2)

    # --- Verificación ------------------------------------------------------
    print(SALIDA)
    print(f"  agrupadoras : {len(plan['agrupadoras'])}")
    print(f"  secciones   : {len(plan['secciones'])}  "
          f"(epicas a convertir: "
          f"{sum(1 for s in plan['secciones'] if s['tipoActual'] == 'Epicas')}, "
          f"ya Historia: "
          f"{sum(1 for s in plan['secciones'] if s['tipoActual'] != 'Epicas')})")
    print(f"  subtareas   : {len(plan['subtareas'])}")
    print(f"  a borrar    : {len(plan['aBorrar'])}")

    claves = [s['clave'] for s in plan['secciones']]
    if len(claves) != len(set(claves)):
        raise SystemExit('Una sección quedó asignada a dos agrupadoras.')
    if len(plan['aBorrar']) != len(set(plan['aBorrar'])):
        raise SystemExit('Hay tareas a borrar repetidas.')

    sin_reencuadrar = [c for hs in huerfanas.values() for h in hs]
    sin_cubrir = [c for c, s in snap.items()
                  if s['padre'] and s['padre'] not in claves]
    if sin_reencuadrar:
        raise SystemExit(f"Huérfanas sin sección conocida: "
                         f"{[h['clave'] for h in sin_reencuadrar]}")
    if sin_cubrir:
        raise SystemExit(f"Tareas cuyo padre no es una sección: {sin_cubrir}")
    print("  huerfanas reencuadradas y sin_tasks_perdidas: OK")

    print()
    for s in plan['secciones']:
        n = sum(1 for t in plan['subtareas'] if t['seccion'] == s['clave'])
        marca = 'E' if s['tipoActual'] == 'Epicas' else 'H'
        print(f"  [{marca}] {s['clave']:>7}  {s['agrupadora']}  "
              f"{n:>2} subt  {s['resumen'][:58]}")


if __name__ == '__main__':
    main()
