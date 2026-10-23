# Catálogo cerrado de estilos de diagrama — Ancoa / Only Simple Solutions

Once estilos, ninguno más. Cada uno replica una o más figuras del Subdocumento 4 y se alinea con un tipo
de diagrama del Modelo C4 (núcleo o suplementario). La fuente de verdad técnica es `catalogo.json`; este
documento explica cuándo usar cada estilo y trae una plantilla mínima para empezar.

| Id | Estilo | Familia / herramienta | Equivalente C4 | Figuras de referencia |
|----|--------|-----------------------|----------------|-----------------------|
| L1 | Vista lógica general por frentes | lógica · diagrams + Graphviz | Contenedores (2) con contexto | 4.1, 4.2 |
| L2 | Vista por capas | lógica · diagrams + Graphviz | Contenedores agrupados por capa | 4.3 |
| L3 | Bloque funcional | lógica · diagrams + Graphviz | Contenedores/componentes de un área (2–3) | 4.4 a 4.9 |
| L4 | Recorrido de proceso | lógica · diagrams + Graphviz | Dinámico (suplementario) | 4.10 |
| L5 | Autoridad de datos y frontera | lógica · diagrams + Graphviz | Vista de datos (complementaria) | 4.12 |
| L6 | Emplazamiento lógico y rutas | lógica · diagrams + Graphviz | Despliegue abstracto (suplementario) | 4.11 |
| F1 | Topología física de sitios | física · draw.io + íconos Azure | Despliegue, vista general | 4.13 |
| F2 | Red y segmentación hub-spoke | física · draw.io + íconos Azure | Despliegue, red | 4.14 |
| F3 | Ambientes y flujo de despliegue | física · draw.io + íconos Azure | Despliegue por ambiente | 4.15 |
| F4 | Puntos de falla y conmutación | física · draw.io + íconos Azure | Despliegue, continuidad | 4.16, 4.20 |
| F5 | Detalle de sitio | física · draw.io + íconos Azure | Despliegue de un nodo | 4.17, 4.18, 4.19 |

Las imágenes de las figuras originales están en `references/figuras/fig_4_N.png`. Ábralas con la
herramienta de lectura de imágenes antes de dibujar un estilo por primera vez.

## Árbol de decisión

1. ¿El diagrama muestra **dónde** está algo (sitio, región, red, equipo, ambiente)? → familia **F** (o L6 si aún no hay equipos ni enlaces concretos).
   - Varios sitios y sus conexiones → **F1**
   - Subredes, hub, firewall → **F2**
   - Desarrollo → QA → Preproducción → Producción → Recuperación → **F3**
   - Qué falla y cuál es el camino alterno, o conmutación entre regiones → **F4**
   - El interior de un solo sitio → **F5**
2. ¿Muestra **qué hace** la solución y cómo se relacionan sus piezas? → familia **L**.
   - Toda la solución de una etapa → **L1**
   - Las ocho capas de RT-02.01 → **L2**
   - Un bloque funcional → **L3**
   - Un proceso paso a paso (venta, crédito, corte de enlace) → **L4**
   - Quién es autoridad de qué dato y qué cruza la frontera → **L5**
   - Ubicación por sitio sin dimensionar → **L6**
3. ¿No encaja en ninguno? → **No se dibuja.** Se usa una tabla o texto, o se pide al equipo que amplíe el catálogo.

## Formato común de la especificación (JSON)

```json
{
  "estilo": "L3",
  "figura": "4.4",
  "titulo": "Bloque de tiendas",
  "encabezado": "Ancoa · bloque Tiendas físicas",
  "fuente": "elaboración propia a partir de Subdocumento 3 y RT-02/RT-03.",
  "grupos":  [{"id": "...", "etiqueta": "...", "frente": "retail|emisor|frontera|transversal|cliente|azure|externo", "padre": "opcional"}],
  "nodos":   [{"id": "...", "etiqueta": "...", "tipo": "<tipo lógico>", "codigo": "R:V-02", "estado": "objetivo|convivencia|por_acreditar|condicionado", "grupo": "..."}],
  "enlaces": [{"de": "...", "a": "...", "semantica": "<semántica>", "etiqueta": "intención", "paso": 1}]
}
```

En estilos **F**, los grupos llevan `tipo` (nube_azure, sitio_cliente, seccion, ambito, zona, subred) y
`disposicion` (fila, columna, rejilla + `columnas`); los nodos llevan `icono` (clave de `iconos_fisicos`)
en lugar de `tipo`, y en F4 una `insignia` numérica. Nunca se escriben colores, formas, fuentes ni estilos de
línea: los pone el catálogo según `frente`, `estado` y `semantica`.

---

## L1 · Vista lógica general por frentes (Fig. 4.1, 4.2)

- Dos grupos raíz obligatorios: `retail` y `emisor`. X-01 (`politica_x01`) entre ambos, fuera de los dos.
- Dentro de cada frente, de arriba abajo: canales → API Management → servicios por área → Event Hubs/PostgreSQL → Data Lake/Power BI → adaptadores → plataformas conservadas.
- Grupo `transversal` aparte para Entra ID, Key Vault y Azure Monitor (o se omite y se dice en el texto, como en la Fig. 4.2).
- Único enlace entre frentes: `compra_autorizable`, rotulado «autorización de compra».
- Las flechas son familias de interacción, no interfaces ni rutas físicas: decirlo en el párrafo que acompaña.

## L2 · Vista por capas (Fig. 4.3)

- Solo nodos `caja`. Cada etiqueta empieza por «N · NOMBRE DE CAPA» (p. ej. «4 · SERVICIOS RETAIL (9)»), salvo la caja de ACTORES.
- El color sale del `frente` de la caja: Retail verde, Emisor lila, Frontera ámbar, transversal gris azulado.
- Orden vertical: actores, 1 presentación, 2 borde, 3 puerta de enlace, 4 servicios y frontera, 5 eventos/adaptadores, 6 datos, 7 seguridad, 8 observabilidad.

## L3 · Bloque funcional (Fig. 4.4–4.9)

- Un grupo por frente presente («Retail · tienda», «Filial emisora»). Máximo 25 nodos.
- Conservar los códigos del Subdocumento 3 y la misma convención de trazos de L1.
- Componentes de convivencia (`estado: convivencia`) y por acreditar se dibujan solos como caja discontinua.

## L4 · Recorrido de proceso (Fig. 4.10)

- Actores como `actor` (elipse), pasos como `caja`, registros como `almacen`.
- Grupos por ámbito: «Tienda · operación local durante 24 h», «Azure Chile Central · ámbito Retail», «Filial emisora · ámbito lógico separado, no sitio».
- **Toda** flecha lleva etiqueta. Se recomienda numerar con `paso` (estilo dinámico de C4).
- Sin enlace no se originan tarjetas ni se amplían cupos: si el proceso lo toca, dejarlo en una nota del texto.

## L5 · Autoridad de datos y frontera (Fig. 4.12)

- Tres grupos obligatorios: `retail`, `frontera`, `emisor`. Dirección izquierda→derecha.
- `caja` para servicios (con código) y `almacen` para bases, lagos y bitácoras.
- `compra_autorizable` para el cruce permitido; `denegado` rotulado «… ACCESO DENEGADO» para mostrar lo que no cruza.

## L6 · Emplazamiento lógico y rutas (Fig. 4.11)

- Solo `caja`. Grupos: sedes del Cliente (`cliente`), casa matriz (`transversal`), Microsoft Azure (`azure`), plataformas actuales de alojamiento desconocido (`externo`).
- Rutas no acreditadas con `por_acreditar` rotuladas «ruta por verificar». No se dibuja la filial como sitio.

## F1 · Topología física de sitios (Fig. 4.13)

- Columnas de izquierda a derecha: Sitios del Cliente (`sitio_cliente`) → Exterior / Conexiones (`seccion`) → CLD-01 Chile Central (`nube_azure`, con ámbitos Retail, Base tecnológica, Emisor y Hub) → CLD-02 Brazil South (`nube_azure`).
- Tráfico que atraviesa el firewall con `trafico_inspeccionado` (magenta). ExpressRoute y enlaces no contratados con `enlace_propuesto` y estado `propuesto`.

## F2 · Red y segmentación hub-spoke (Fig. 4.14)

- Hub con subredes con nombre Azure exacto (GatewaySubnet, RouteServerSubnet, AzureFirewallSubnet, AzureBastionSubnet) como grupos `subred`.
- Una rama (`ambito`) por ámbito: Retail, Emisor, Base tecnológica; dentro, columnas Entrada / APIM / Aplicación / Datos como `subred`.

## F3 · Ambientes y flujo de despliegue (Fig. 4.15)

- Raíz en `columna`: sección Entrega (repositorio, entrega continua, registro de imágenes) → CLD-01 con Desarrollo, QA, Preproducción, Producción → CLD-02 Recuperación.
- Cada ambiente es un `ambito` con dos nodos (Retail, Emisor: «suscripción y Key Vault»). `aprobacion` antes de Producción.

## F4 · Puntos de falla y conmutación (Fig. 4.16, 4.20)

- `insignia` 1..N sin saltos en cada punto de falla; el texto y la Tabla de contingencias usan la misma numeración.
- Zonas de disponibilidad como grupos `zona` dentro de la `nube_azure`. Réplicas con `replica` rotuladas («asíncrona», «retraso < 15 min»).

## F5 · Detalle de sitio (Fig. 4.17, 4.18, 4.19)

- Un solo sitio por diagrama. Segmentos (VLAN), zonas o salas como grupos `zona`/`subred`; columna «Hacia Azure» a la derecha.
- Pares activo-pasivo y pilas de switches se dibujan como dos nodos dentro de un `subred` rotulado «Par HA (activo-pasivo)».
