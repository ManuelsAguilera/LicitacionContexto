import csv
import json
import os
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, 'scripts'))
from rutas import HISTORICO, RUTA_MAPPING_VINCULADO, RUTA_PAYLOAD_PLANO

# Epic = sección numerada del índice (Formulario T-7). El nombre completo se usa
# como "Nombre de Epic" y como "Enlace a Epic" de las tareas (clave de vinculación
# en la importación de Jira). No se trunca: debe coincidir exactamente.
secciones = {
    # ---------------------------------------------------------------- Capítulo 1
    '1. Introducción': [
        {'text': 'Elaborar el resumen del capítulo y su conexión con los demás capítulos, anexos y formularios', 'type': 'Tareas'},
        {'text': 'Revisar qué partes del informe hay que cambiar, dado el nuevo resumen y justificaciones', 'type': 'Tareas'},
    ],
    '1.1 Presentación de la empresa': [
        {'text': 'Ver que cumpla con las 11 preguntas del profe', 'type': 'Tareas'},
        {'text': 'Hacer un diagrama de contexto', 'type': 'Tareas'},
    ],
    '1.2 Estructura Organizacional': [
        {'text': 'Elaborar organigrama de la estructura organizacional', 'type': 'Tareas'},
    ],
    '1.3 Gobierno interno Calidad, Seguridad y Conocimiento': [
        {'text': 'Definir el modelo de gobierno interno de calidad, de seguridad de la información y de gestión del conocimiento: sus políticas, instancias y responsables', 'type': 'Tareas'},
    ],
    '1.4 Experiencia y Certificaciones': [
        {'text': 'Inventar experiencia relevante en la industria del caso y en proyectos de complejidad equivalente', 'type': 'Tareas'},
        {'text': 'Realizar el resumen y análisis del capítulo; el detalle de los proyectos va en el Formulario T-6 (Art. 34°: al menos tres proyectos, uno con arquitectura híbrida y uno con SLA de disponibilidad ≥ 99,5 %).', 'type': 'Trabajo Tecnico'},
        {'text': 'Buscar certificaciones institucionales', 'type': 'Tareas'},
    ],
    '1.5 Estructura para Proyecto': [
        {'text': 'Establecer la estructura para el proyecto: cómo se organiza la empresa para abordar el proyecto. El equipo nominado se desarrolla en el capítulo 12', 'type': 'Tareas'},
    ],
    '1.6 Alianzas': [
        {'text': 'Definir las alianzas tecnológicas vigentes de la empresa  (las alianzas específicas de este proyecto van en 12.3)', 'type': 'Trabajo Tecnico'},
    ],

    # ---------------------------------------------------------------- Capítulo 2
    '2. Introducción': [
        {'text': 'Redactar el resumen del capítulo y su conexión con los demás capítulos, anexos y formularios', 'type': 'Tareas'},
    ],
    '2.1 Resumen Ejecutivo del problema': [
        {'text': 'Elaborar síntesis del problema, su magnitud y los actores afectados', 'type': 'Tareas'},
    ],
    '2.2 Comprensión del problema y de la necesidad': [
        {'text': 'Comprender el problema y la necesidad: hacer el contexto de la industria y sus particularidades operacionales, regulatorias y estacionales.', 'type': 'Spikes'},
    ],
    '2.3 Dimensionamiento del problema': [
        {'text': 'Dimensionar el problema: dimensionar realisticamente la magnitud del problema o desafío, con foco cualitativo y con datos cuantitativos que lo sustenten. Cada cifra debe derivar de las Bases Técnicas del caso o de un cálculo mostrado.', 'type': 'Trabajo Tecnico'},
    ],
    '2.4 Actores y Grupos de Interés': [
        {'text': 'Identificar actores y grupos de interés: actores afectados y grupos de interés, estableciendo nivel de influencia e interés', 'type': 'Tareas'},
    ],
    '2.5 Resumen de Requerimientos, Supuestos, Exclusiones y Restricciones': [
        {'text': 'Crear resumen de requerimientos, supuestos, exclusiones y restricciones', 'type': 'Tareas',
         'desc_extra': 'Detalle: Resumen y análisis de lo que el CLIENTE requiere según las Bases, de los supuestos declarados con su fundamento, y de las exclusiones y restricciones que impone el caso. El detalle va en EMPRESA-Subdocumento2-Anexos.'},
        {'text': 'Crear un detalle llamado ONLYSIMPLESOLUTIONS con: - Listado de requerimientos - Listado de supuestos, exclusiones y restricciones - Otros listados', 'type': 'Tareas'},
    ],

    # ---------------------------------------------------------------- Capítulo 3
    '3. Introducción': [
        {'text': 'Redactar el resumen del capítulo y su conexión con los demás capítulos, anexos y formularios', 'type': 'Tareas'},
    ],
    '3.1 Resumen Ejecutivo de la Solución': [
        {'text': 'Elaborar síntesis de la solución (implementación de etapas 1 y 2; implantación con marchas blancas y pasos a producción; operación de soporte por 36 meses)', 'type': 'Tareas'},
    ],
    '3.2 Alcance': [
        {'text': 'Revisar el alcance, qué tecnologías vamos a pedir o usar, etc.', 'type': 'Tareas'},
        {'text': 'Identificar el alcance de la solución (Etapas, exclusiones, catálogo y criterios)', 'type': 'Tareas',
         'desc_extra': 'Detalle a considerar: - Alcance de la Etapa 1 y de la Etapa 2, con separación explícita y criterios de asignación entre ambas. - Exclusiones explícitas, supuestos y restricciones del alcance. - Catálogo de requerimientos funcionales y no funcionales, priorizado y trazable (trazabilidad completa en el Formulario T-12). - Criterios de aceptación del alcance comprometido.'},
        {'text': 'Anexar el Formulario T-12', 'type': 'Tareas'},
    ],
    '3.3 Esquema de solución': [
        {'text': 'Diagramar uno o varios esquemas de solución, con explicación en texto para cada uno', 'type': 'Trabajo Tecnico'},
        {'text': 'Documentar el esquema de solución, con explicaciones, etc.', 'type': 'Trabajo Tecnico'},
    ],
    '3.4 Explicación de la Solución': [
        {'text': 'Explicar la solución desde la perspectiva operativa/negocio y su conexión con el Cap. 2 (debe mapear al 100 % con la arquitectura lógica del Cap. 4: los componentes tienen el mismo nombre en ambos capítulos)', 'type': 'Tareas'},
    ],

    # ---------------------------------------------------------------- Capítulo 4
    '4. Introducción': [
        {'text': 'Redactar el resumen del capítulo y su conexión con los demás capítulos, anexos y formularios', 'type': 'Tareas'},
    ],
    '4.1 Arquitectura lógica': [
        {'text': 'Analizar inconsistencias con el esquema solución', 'type': 'Spikes'},
        {'text': 'Mirar el esquema solución, explicitar lo de los módulos, en base a lo del ppt. (Consultar definición microservicio)', 'type': 'Trabajo Tecnico'},
        {'text': 'Revisar que los actores y vistas sean consistentes con el informe, y si no lo son registrar las inconsistencias', 'type': 'Tareas'},
        {'text': 'Tomar el diagrama lógico, poner las mismas vistas que el esquema de solución; arreglar inconsistencias generales entre ambos diagramas', 'type': 'Trabajo Tecnico'},
        {'text': 'Diagramar nuevo diagrama lógico', 'type': 'Trabajo Tecnico'},
        {'text': 'Hacer flujos de cómo el actor interactúa con el sistema (al menos 2 dominios)', 'type': 'Trabajo Tecnico'},
        {'text': 'Reescribir subdocumento 4 Parte 1', 'type': 'Tareas'},
    ],
    '4.1.1 Especificaciones Tecnologías de Software a utilizar': [
        {'text': 'Revisar stack tecnológico: lenguajes, marcos, motores, servicios y productos, justificando su selección con las alternativas evaluadas y el criterio de decisión', 'type': 'Tareas'},
    ],
    '4.2 Arquitectura física': [
        {'text': 'Realizar el flujo físico en base al diagrama lógico', 'type': 'Trabajo Tecnico'},
        {'text': 'Reescribir subdocumento 4 Parte 2', 'type': 'Tareas'},
    ],
    '4.2.1 Especificaciones Implementos a proveer (Hardware y Software)': [
        {'text': 'El hardware que ocupemos, anotarlo en un Excel', 'type': 'Tareas'},
        {'text': 'Identificar elementos de hardware que en el caso no se especifiquen, o que debamos proveer nosotros', 'type': 'Tareas'},
    ],
    '4.3 Data center': [
        {'text': 'Investigar tecnologías nube, y hardware del datacenter', 'type': 'Spikes'},
        {'text': 'Redactar la estrategia de centros de datos (texto que precede a 4.3.1 y 4.3.2)', 'type': 'Tareas'},
    ],
    '4.3.1 Especificaciones Data Center Primario': [
        {'text': 'Especificaciones del datacenter primario: identificar proveedor, definir región y zonas de disponibilidad, identificar los servicios, y definir sitio on-premise según corresponda', 'type': 'Tareas'},
    ],
    '4.3.2 Especificaciones Data Center Secundario': [
        {'text': 'Especificaciones del datacenter secundario: definir región o sitio de recuperación, definir estrategia de replicación, establecer el RPO, establecer el RTO, y documentar el procedimiento de conmutación', 'type': 'Tareas'},
    ],

    # ---------------------------------------------------------------- Capítulo 5
    '5. Introducción': [
        {'text': 'Redactar la introducción y el resumen del capítulo, explicando la conexión con los demás capítulos', 'type': 'Tareas'},
    ],
    '5.1 Modelo': [
        {'text': 'Identificar los dominios de información del sistema', 'type': 'Tareas'},
        {'text': 'Diseñar el modelo de datos para cada dominio, con figuras legibles', 'type': 'Trabajo Tecnico'},
        {'text': 'Realizar el diccionario de datos en los anexos', 'type': 'Trabajo Tecnico'},
    ],
    '5.2 Gestión de datos': [
        {'text': 'Selección del motor y del paradigma de persistencia', 'type': 'Trabajo Tecnico'},
        {'text': 'Justificación de la selección considerando: transaccionalidad, consistencia, disponibilidad, relacional o no relacional (teorema CAP)', 'type': 'Tareas'},
        {'text': 'Definir la separación entre almacenamiento transaccional y analítico, y el modelo de explotación de la información: calidad de datos, retención, archivado y eliminación segura', 'type': 'Trabajo Tecnico'},
    ],
    '5.3 Estrategia de migración': [
        {'text': 'Diseñar la estrategia de migración', 'type': 'Tareas'},
        {'text': 'Definir el proceso de saneamiento/limpieza de datos', 'type': 'Trabajo Tecnico'},
        {'text': 'Definir mecanismos de validación de datos migrados', 'type': 'Trabajo Tecnico'},
        {'text': 'Definir el proceso de conciliación entre origen y destino', 'type': 'Tareas'},
        {'text': 'Verificar que la migración y las ventanas de corte sean compatibles con el cronograma', 'type': 'Tareas'},
    ],
    '5.4 Estrategia de desempeño': [
        {'text': 'Definir estrategias de indexación, particionamiento, caché y optimización de consultas', 'type': 'Tareas'},
        {'text': 'Justificar estas decisiones utilizando la volumetría del caso', 'type': 'Tareas'},
    ],

    # --------------------------------------------------------------- Capítulo 13
    '13. Introducción': [
        {'text': 'Redactar el resumen del capítulo y su conexión con los demás capítulos, anexos y formularios', 'type': 'Tareas'},
    ],
    '13.3 Innovación 3 — Tecnológica o de arquitectura': [
        {'text': 'Investigar innovaciones (conocimiento)', 'type': 'Spikes'},
        {'text': 'Desarrollar la innovación de base tecnológica o de arquitectura, con los siete elementos del Art. 29° y fuentes en norma APA 7.ª edición', 'type': 'Trabajo Tecnico'},
        {'text': 'Ligar el conocimiento al esquema solución', 'type': 'Trabajo Tecnico'},
    ],
    '13.4 Innovación 4 — Modelo de negocio o de contratación': [
        {'text': 'Desarrollar la innovación de modelo de negocio o de contratación, con los siete elementos del Art. 29°', 'type': 'Tareas'},
    ],
}


def limpiar(texto):
    """Residual de Word -> texto plano: &nbsp; a espacio y colapso de repeticiones."""
    return ' '.join(texto.replace('&nbsp;', ' ').split())


PROYECTO = "OSS"
CLOUD_ID = "b662438c-9aba-4643-a083-82a2fde025f3"
PRIORIDAD = "Medio"  # valor real de Jira en este proyecto (no "Media")

csv_data = [
    ['ID de incidencia', 'Resumen', 'Descripción', 'Tipo de Incidencia',
     'Clave del proyecto', 'Prioridad', 'Nombre de Epic', 'Enlace a Epic']
]

epics = []
tasks = []
siguiente = 1

for epic_name, tasks_de_la_seccion in secciones.items():
    if not tasks_de_la_seccion:
        continue

    epic_ref = len(epics) + 1
    epic_id = siguiente
    siguiente += 1

    # La fila de la épica lleva el nombre en "Nombre de Epic" y "Enlace a Epic" vacío.
    csv_data.append([epic_id, epic_name, f"Sección principal: {epic_name}",
                     "Epicas", PROYECTO, PRIORIDAD, epic_name, ""])
    epics.append({
        'n': epic_id,
        'epicRef': epic_ref,
        'issueType': 'Epicas',
        'summary': epic_name,
        'description': f"Sección principal: {epic_name}",
    })

    for task in tasks_de_la_seccion:
        desc = f"Sección del informe: {epic_name}"
        if task.get('desc_extra'):
            desc += " — " + limpiar(task['desc_extra'])

        # Epic Link se resuelve por el texto del Summary de la épica, no por un ID.
        csv_data.append([
            siguiente, limpiar(task['text']), desc, task['type'],
            PROYECTO, PRIORIDAD, "", epic_name
        ])
        tasks.append({
            'n': siguiente,
            'epicRef': epic_ref,
            'issueType': task['type'],
            'summary': limpiar(task['text']),
            'description': desc,
        })
        siguiente += 1

with open(RUTA_MAPPING_VINCULADO, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(csv_data)

with open(RUTA_PAYLOAD_PLANO, 'w', encoding='utf-8') as f:
    json.dump({
        'cloudId': CLOUD_ID,
        'projectKey': PROYECTO,
        'reporterAccountId': '609a0d9f5d67f20069ae5a6e',
        'epics': epics,
        'tasks': tasks,
    }, f, ensure_ascii=False, indent=2)

print(f"CSV + payload generados. Epicas: {len(epics)} | Tareas: {len(tasks)} | Filas CSV: {len(csv_data)}")
for e in epics:
    print(f"  {e['n']:>3}  [{e['epicRef']:>2}]  {e['summary']}")

# --- Tandas de importación -----------------------------------------------
# Lo ya creado en la Fase 1 (prueba) se excluye para no duplicar.
# Se referencia por el ID de incidencia (n), que es inequívoco.
YA_CREADOS = {              # n -> clave Jira creada en la prueba
    4: 'OSS-69',            # épica  1.1 Presentación de la empresa
    5: 'OSS-70',            # tarea  Ver que cumpla con las 11 preguntas del profe
    13: 'OSS-71',           # tarea  Realizar el resumen y análisis del capítulo... (T-6)
}

os.makedirs(HISTORICO, exist_ok=True)

# epicRef -> resumen de la épica, para que cada tanda resuelva el parent.
ref_a_nombre = {e['epicRef']: e['summary'] for e in epics}

claves = []
for e in epics:
    if e['n'] in YA_CREADOS:
        claves.append({'epicRef': e['epicRef'], 'n': e['n'],
                       'resumen': e['summary'], 'clave': YA_CREADOS[e['n']]})

epics_pend = [e for e in epics if e['n'] not in YA_CREADOS]
tasks_pend = []
for t in tasks:
    if t['n'] in YA_CREADOS:
        continue
    tasks_pend.append(dict(t, epicResumen=ref_a_nombre[t['epicRef']]))


def escribir_tanda(nombre, elementos, extra=None):
    ruta = os.path.join(HISTORICO, nombre)
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump({'cloudId': CLOUD_ID, 'projectKey': PROYECTO,
                   'reporterAccountId': '609a0d9f5d67f20069ae5a6e',
                   **(extra or {}), 'items': elementos},
                  f, ensure_ascii=False, indent=2)
    print(f"  {ruta}: {len(elementos)} items")


def repartir(elementos, partes):
    tam = (len(elementos) + partes - 1) // partes
    return [elementos[i:i + tam] for i in range(0, len(elementos), tam)]


escribir_tanda('claves_epicas.json', claves)
escribir_tanda('epicas_1.json', repartir(epics_pend, 2)[0])
escribir_tanda('epicas_2.json', repartir(epics_pend, 2)[1])
for i, tanda in enumerate(repartir(tasks_pend, 3), start=1):
    escribir_tanda(f'tareas_{i}.json', tanda)

print(f"\nPendiente: {len(epics_pend)} epicas + {len(tasks_pend)} tareas "
      f"({len(YA_CREADOS)} ya creados en la prueba)")
