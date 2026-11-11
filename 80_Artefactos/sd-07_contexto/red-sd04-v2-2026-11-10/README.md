# Red del SD-07 v2: traspaso completo del SD-04 (2026-11-10)

Documento de trabajo, no entregable. Reemplaza a `../red-fisica-2026-11-10/` (paso C) como insumo vigente de horas, dotación y calendario. Corte del SD-04: rama `sd04/redaccion-y-figuras-fisicas`, commit `1d63376`.

> **Reemplazado como insumo** por `../red-v3-2026-11-10/` (misma red con la capacitación E2 dividida, decisión del paso D). Este directorio conserva el traspaso del SD-04.

## Qué resuelve

1. **Cruce SD-04 → EDT** (regla del 100 % aplicada a la arquitectura, Art. 57.2): de unos 90 componentes del SD-04, el software, las interfaces, la migración y la entrega estaban cubiertos. Faltaban paquetes para la plataforma de datos, los controles de seguridad desplegados, el equipamiento TI de DC-01 y la pila local de tienda. Además, la nube y la recuperación estaban estimadas para 2 frentes en vez de 3.
2. **Mismo método de HH que el SD-07**, tanto para lo nuevo como para lo del paso C, que se recalculó.

## Método (idéntico al ledger del traspaso)

- **HH = cantidad × (O + 4M + P) ÷ 6**, con O, M y P en HH por unidad.
- **M = personas × días × 8 HH**; **O = 0,6 M**; **P = 1,5 M** (la proporción más usada en el ledger, por ejemplo 48/80/120).
- La duración se calcula con 7,5 / 6,8 / 5,1 HH efectivas por persona y día. Cuando un componente existente crece, se aplica la regla del traspaso: **dotación ajustada a la ventana disponible, el esfuerzo no cambia**, es decir, mismas fechas y más personas.

## Cambios (validados por el usuario el 2026-11-10)

**Componentes existentes que cambian de cantidad** (3 frentes y laboratorio):

| Componente | Unidad | Cantidad | HH antes → después |
| :-- | :-- | :-- | --: |
| C0168 · 1.4.1 Fundación de la nube | dominio-ambiente | 10 → 15 | 413,3 → 620,0 |
| C0171 · 1.4.4 Configuración y validación de ambientes | dominio-ambiente | 10 → 15 | 160,0 → 240,0 |
| C0170 · 1.4.3 Huellas de Producción y DR | huella | 2 → 4 (Control de cruces) | 162,7 → 325,3 |
| C0180 · 1.4.13 Respaldo inicial | familia × frente | 10 → 15 | 90,0 → 135,0 |
| C0203 · 1.8.4 Custodia de claves | frente | 2 → 3 | 82,7 → 124,0 |
| C0169 · 1.4.2 Red de sitio | sitio | 13 → 25 | 433,3 → 833,3 |
| C0175 · 1.4.8 Especificación de sitios | sitio | 24 → 25 | 148,0 → 154,2 |

C0169 comparte nodos con C0181 (validación de segmentación), así que no se escala. Se agregan **12 nodos de red de sitio**, después de la instalación física, en el laboratorio, las 3 tiendas piloto, los 2 CD y las tiendas T14–T19. Los 27 nodos originales de abril de 2027 se conservan. **Pendiente para el paso T:** su secuencia frente a la llegada del equipamiento.

**Componentes nuevos:**

| Paquete | Unidad × cantidad | M por unidad | HH |
| :-- | :-- | :-- | --: |
| 1.4.14 Levantamiento físico | 25 sitios | 2 × 1 día = 16 | 406,7 |
| 1.4.16 y 1.4.18 Órdenes de compra | 3 órdenes | 2 × 1 = 16 | 48,8 |
| 1.4.15, 1.4.17 y 1.4.19 Instalación física de la tienda tipo (sin redes) | 23 sitios | 3 × 3 = 72 | 1.683,6 |
| 1.4.19 Instalación física de los CD | 2 sitios | 3 × 2 = 48 | 97,6 |
| 1.4.20 Recuperación a tamaño completo | 3 frentes | 1 × 2 = 16 | 48,8 |
| 1.4.21 Plataforma de datos y analítica (E1) | 2 negocios | (15 + 5) × 8 = 160 | 325,3 |
| 1.8.9 Controles de seguridad desplegados (E2) | 12 controles-frente | 1 × 3 = 24 | 292,8 |
| 1.4.22 Equipamiento TI y redes de DC-01 (E3) | 1 recinto | 4 × 10 = 320 | 325,3 |
| 1.4.23 Pila local de tienda (E4) | 25 sitios | 2 × 1 = 16 | 406,7 |
| 1.4.24 Replicación entre regiones (E6) | 3 frentes | 2 × 3 = 48 | 146,4 |
| 1.10.1 y 1.10.5 Órdenes de compra de lockers y tótems (E7) | 2 órdenes | 2 × 1 = 16 | 32,5 |

**Sin cambio:** F:C-04 (control regulatorio) queda fuera mientras el SD-04 no lo apruebe; API Center queda dentro de 1.3.4.

**Total base: 239.250,01 HH**, es decir, +4.756,54 sobre las 234.493,47 del traspaso. La diferencia de 0,17 HH con 239.249,84 viene del redondeo a dos decimales por rol. Contingencia aparte: 3.688 HH.

## Validación (motor CPM y comprobaciones de `verificar_paquete.py`)

- 0 actividades tardías y 0 holguras negativas;
- 0 violaciones de precedencia;
- **H1–H12 idénticos al original**;
- marchas blancas intactas;
- 22 tiendas el 7 de abril de 2028.

Estabilización con margen mínimo de 10 días: 76 actividades movidas (10.522 HH).

**No revalidado:** las cuotas por persona (registro diario no regenerado).

**Hallazgo para el paso D:** la prueba de corte de 24 h del piloto (1.9.9) **queda sin holgura**. Ahora espera a que el piloto tenga instalación, red y pila local, y parte el 18 de junio de 2027; termina antes del 7 de julio.

## Calendario de compras y habilitación (R4)

| Lote o paquete | Fechas (2027 salvo indicación) |
| :-- | :-- |
| Levantamiento físico | 7 de enero – febrero (M1–M2) |
| DC-01 | Orden 11 de enero; entrega 7 de abril; equipamiento TI 16 de abril – 5 de mayo (antes de H3) |
| Lote 1 (piloto y laboratorio) | Orden 8 de marzo; entrega 5 de mayo y 2 de junio; instalación, red y pila local 2 – 18 de junio |
| Plataforma de datos | 7 – 18 de mayo |
| Controles de seguridad | Hasta el 19 de junio |
| Lote 2 (19 tiendas y 2 CD) | Orden 7 de mayo; entrega 6 de julio y 3 de agosto; en servicio el **19 de septiembre** |
| Replicación y recuperación completa | Julio y septiembre; encendida a tamaño completo desde M13 |
| Lockers y tótems | Orden 8 de marzo de 2028; entrega 5 de mayo de 2028 |

## Perfiles del E-26 (reglas del usuario)

- Un Arquitecto Experto (hasta 160 HH al mes) y el resto Arquitecto Senior.
- Todo el desarrollo como Ingeniero Senior.
- Líder Funcional (Jefe de Análisis y Diseño) y Líder de Calidad (Analista QA Experto), cada uno una persona de hasta 160 HH al mes.
- Dos «otros roles» declarados con rango aprobado.

En total, 21 perfiles. En la vista paquete × perfil, la parte de líder se reparte entre los paquetes en proporción a cada mes.

## Archivos

| Archivo | Contenido |
| :-- | :-- |
| `ampliar_red_v2.py` | Genera la red v2 desde el traspaso |
| `Red_CPM/nodos.json`, `relaciones.json`, `componentes_v2.json` | Red v2 (977 nodos y 2.125 relaciones) y registro de componentes con O/M/P |
| `estabilizar.py`, `estabilizacion.json` | Estabilización (argumento de margen: 10) |
| `matriz_red_fisica.py` | Matriz por rol frente a la programación original (incluye componentes escalados) |
| `equivalencia_e26_v2.py` | Perfiles del E-26 y vista por paquete |
| `HH/FTE_matriz_roles_M1_M56.csv` | 37 roles del plan × 56 meses |
| `HH/FTE_matriz_perfiles_E26_M1_M56.csv` | **21 perfiles del E-26 × 56 meses, con rangos de costo y tarifa** |
| `HH_paquete_x_perfil_E26.csv`, `HH_por_paquete_EDT.csv` | 255 paquetes × perfil, y HH y ventana por paquete |
