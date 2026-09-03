---
name: jira-workflow
description: "Integrar opencode con Jira Cloud vía el servidor MCP oficial de Atlassian (Rovo). Gestiona el ciclo de vida de tareas mientras se trabaja: tomar tarea, marcarla como asignada/en progreso, transicionarla a hecho y registrar comentarios, todo restringido a los permisos del usuario autenticado. Usar cuando el proyecto esté conectado a Jira o cuando el usuario quiera gestionar sus tareas desde opencode."
---

# Jira Workflow (integración MCP)

Este skill orquesta la conexión de opencode con **Jira Cloud** mediante el **Atlassian Rovo MCP Server** (oficial, remoto). Permite gestionar tareas sin salir de la terminal: buscarlas, tomarlas, marcarlas como asignadas/en progreso/completadas, consultar sprints/boards y registrar comentarios.

> Nota de seguridad: el servidor MCP actúa **restingido a los permisos del usuario autenticado**. Nunca puede ver ni modificar en Jira más de lo que ese usuario puede. El token OAuth se guarda localmente en `~/.local/share/opencode/mcp-auth.json`, nunca en el repositorio.

## Cuándo usar

- Cuando el proyecto esté configurado con Jira y haya tareas que gestionar durante el trabajo.
- Cuando el usuario pida tomar tareas, marcarlas, consultar su trabajo pendiente o registrar progreso.
- Después de leer `AGENTS.md`, si el servidor `jira` está activo en la sesión.

## Verificación de disponibilidad (siempre primero)

Antes de prometer cualquier operación sobre Jira, verifica si el MCP está disponible en la sesión:

1. Las herramientas del MCP aparecen con el prefijo `jira_*` (por ejemplo `jira_search_issues`).
2. Si **no** hay herramientas `jira_*` disponibles, el servidor está desactivado o sin cuenta vinculada.

**Si no hay herramientas `jira_*`:** NO bloquees el trabajo. Informa brevemente que la conexión a Jira no está activa, explica cómo activarla (sección "Activación" abajo) y continúa con la tarea normalmente. opencode funciona igual sin Jira.

## Activación (una sola vez por máquina/usuario)

El servidor MCP de Jira está configurado en `opencode.jsonc` con `"enabled": false` por defecto para no interferir si no hay cuenta vinculada. Para activarlo:

1. En `opencode.jsonc` del proyecto, cambia `"enabled": false` → `"enabled": true` para el bloque `jira`.
2. Vuelve a iniciar opencode (los cambios de MCP requieren reiniciar la sesión).
3. Autentica con el flujo OAuth de Atlassian (abre el navegador y autoriza):
   ```bash
   opencode mcp auth jira
   ```
4. Verifica que quedó conectada:
   ```bash
   opencode mcp list
   ```

Requisitos: cuenta **Jira Cloud** (no Server/Data Center), el endpoint oficial es `https://mcp.atlassian.com/v1/mcp/authv2`, y no se necesita crear una app en Atlassian (usa Dynamic Client Registration).

## Ciclo de vida de una tarea

Flujo recomendado al trabajar cada documento/entregable de la propuesta:

### 1. Buscar tareas pendientes asignadas al usuario

Busca las tareas abiertas del usuario actual:

```
Busca mis tareas abiertas en Jira y muéstralas. usa el mcp jira
```

JQL equivalente: `assignee = currentUser() AND statusCategory != Done ORDER BY updated DESC`

### 2. Tomar / asignar una tarea

Si una tarea está sin asignar o asignada a otro y el usuario quiere tomarla, asigna al usuario actual y, de corresponder, transiciónala a **In Progress**:

```
Toma la tarea <CLAVE> y márcala como en progreso. usa el mcp jira
```

El agente debe:
- Confirmar la tarea objetivo (número/CLAVE) antes de escribir en Jira.
- Transicionar al estado correcto según el workflow del proyecto (típicamente **To Do → In Progress**).

### 3. Mientras se trabaja (registrar progreso)

Al avanzar, se puede añadir un comentario breve con lo hecho:

```
Agrega un comentario a <CLAVE> con el avance: <resumen>. usa el mcp jira
```

### 4. Completar la tarea

Al terminar el documento/entregable correspondiente, transicionar a **Done** y añadir un comentario de cierre:

```
Marca <CLAVE> como completada y deja un comentario resumiendo el entregable. usa el mcp jira
```

## Operaciones soportadas (tools `jira_*`)

| Operación | Tool MCP típica | Uso |
| :--- | :--- | :--- |
| Buscar tareas (JQL / filtros) | `jira_search_issues` / `jira_list_issues` | tareas por assignee/status/sprint |
| Listar proyectos | `jira_list_projects` | contexto del proyecto |
| Detalle de una tarea | `jira_get_issue` | comentarios, enlaces, adjuntos |
| Crear tarea / subtarea | `jira_create_issue` | nuevo trabajo o desglose |
| Actualizar campos | `jira_update_issue` | cambios de prioridad, resumen |
| Transicionar estado | `jira_transition_issue` | To Do → In Progress → Done |
| Asignar/desasignar | `jira_assign_issue` | tomar una tarea |
| Comentar | `jira_add_comment` | registrar avance/cierre |
| Boards y sprints | `jira_list_boards` / `jira_list_sprints` / `jira_get_sprint` | consultar sprint actual |

> Las operaciones de **escritura** (crear, transicionar, asignar, comentar) se ejecutan solo con confirmación explícita del usuario sobre la tarea objetivo. Las operaciones de **lectura** se pueden usar con libertad.

## Buenas prácticas

- **Confirmar antes de escribir:** nunca transicionar, asignar ni comentar sin que el usuario indique la tarea y la acción.
- **Una sola llamada por acción:** evita bucles de múltiples llamadas por tarea; agrupa donde tenga sentido (p. ej., transición + comentario).
- **Mantener el contexto liviano:** Jira añade contexto por llamada; usa consultas JQL precisas y no recuperes listas enteras innecesariamente.
- **Al no haber cuenta, no bloquear:** explicar la activación y seguir con el trabajo (ver "Verificación de disponibilidad").
