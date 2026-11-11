# Red del SD-07 ampliada con la infraestructura física del SD-04 (2026-11-10)

Documento de trabajo, no entregable. Paso C del plan del SD-07: calendario de compras y habilitación (insumo R4 del modelo financiero). Reemplaza como insumo de horas a `../estabilizacion-2026-11-10/`, que no incluía la instalación física.

> **Reemplazado como insumo** por `../red-sd04-v2-2026-11-10/` (traspaso completo del SD-04 con el método de HH del SD-07). Este directorio conserva el paso C.

## Por qué se amplió la red

La red del traspaso (853 nodos) no planificaba la infraestructura física que define el SD-04 vigente (rama `sd04/redaccion-y-figuras-fisicas`: §4.3, Tablas 4.13 y 4.15, registro D-FIS):

| SD-04 | Red del traspaso |
| :-- | :-- |
| 22 tiendas tipo (4 servidores, 2 árbitros, 4 firewalls, 4 switches, 3 racks de 24U, 2 UPS, generación, clima) y 2 CD | 1.4.2 «13 tiendas», 1 día de configuración por sitio; sin compra ni instalación física |
| Tres frentes en la nube, incluido el Control de cruces (D-FIS-02) | Solo el entorno de la Filial (1.4.3) |
| Tienda de laboratorio en Preproducción (D-FIS-17) | No existía |
| Recuperación templada en Brazil South | Sin fecha de encendido completo |
| Levantamiento físico por sitio antes del diseño detallado | No existía |

## Supuestos (validados por el usuario el 2026-11-10)

1. **Plazo de entrega:** 8 semanas para el equipamiento estándar y 12 para UPS y generación. Se confirma con los proveedores del T-22.
2. **Instalación:** 1 tienda por cuadrilla cada 3 días hábiles (CD: 2 días), con 2 cuadrillas en paralelo. Cada cuadrilla tiene 2 ingenieros de infraestructura física, 1 especialista de redes y 1 implantador.
3. **Compras:** el patrón de la tienda tipo, fijo en la oferta (SD-04 §4.3), se compra al cerrar H1. Lo que depende del sitio (cable, gabinetes adicionales, puntos de acceso, generador) se compra tras el levantamiento de ese sitio. El lote masivo se compra después de H2.
4. **Piloto:** 3 tiendas a la calle (no en mall), con instalación permitida dentro de la envolvente de eventos porque el piloto está aislado de producción (calendario LAB).
5. **Recuperación:** se despliega reducida con los ambientes (M3–M4), se escala a tamaño completo antes del congelamiento (1.4.20) y queda **encendida a tamaño completo desde M13**, cuando la marcha blanca E1 opera con datos reales.
6. **Levantamiento físico:** 1 día por sitio y 2 personas (infraestructura física y redes), con 25 sitios en total. No incluye viajes a tiendas remotas.

**Decisión de modelado (aceptada por el usuario el 2026-11-10):** la compra de **DC-01** se adelanta a M1, tras su levantamiento y antes de H1, porque su composición está fija en el SD-04 y el recinto debe habilitarse en abril de 2027 (1.4.11 y 1.4.12) para llegar a H3.

## Cambios en la red

- **64 nodos nuevos y 125 relaciones nuevas** (917 nodos y 1.961 relaciones en total); **+2.610,67 HH**. No cambian las duraciones, HH ni relaciones existentes.
- Paquetes nuevos de la rama 1.4:
  - 1.4.14 levantamiento físico;
  - 1.4.15 tienda de laboratorio;
  - 1.4.16 suministro del lote 1 y de DC-01;
  - 1.4.17 tiendas piloto;
  - 1.4.18 suministro del lote 2;
  - 1.4.19 instalación del lote 2;
  - 1.4.20 recuperación a tamaño completo.
- 1.4.3 se amplía al **Control de cruces** (réplica de las HH del entorno de la Filial). 1.4.2 se renombra «patrón y configuración de borde» y conserva sus 625 HH.
- Relaciones clave: instalaciones del piloto y laboratorio → prueba de corte de 24 h (1.9.9); lote 2 instalado → H6; recuperación completa → H6; entrega de DC-01 → 1.4.11 y 1.4.12.

## Validación

Motor CPM del equipo y las comprobaciones de `verificar_paquete.py` sobre la programación estabilizada:

- 0 actividades tardías y 0 holguras negativas;
- 0 violaciones de precedencia;
- **H1–H12 idénticos a la programación original**;
- 22 tiendas el 7 de abril de 2028;
- marchas blancas E1 y E2 intactas.

Se repitió la estabilización del paso B con un margen mínimo de 10 días (`../estabilizacion-2026-11-10/estabilizar.py`, argumento 10).

**No revalidado:** las cuotas por persona (8, 40 y 160 HH), por la misma razón que en el paso B.

## Calendario de compras y habilitación (R4, sin montos)

| Lote | Qué | Quién compra | Orden de compra | Entrega | Instalación o habilitación | ¿Flujo del proponente? |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Levantamiento | 25 sitios (DC-01, piloto, laboratorio, 19 tiendas, 2 CD) | — | — | — | M1–M2 (7 de enero al 12 de febrero de 2027) | Sí (HH) |
| DC-01 | Racks 42U, pares de integración, energía, clima, incendio, acceso | OSS | **M1** (8 de enero de 2027) | M3 (3 de abril) | M4 (1.4.11 y 1.4.12) | Sí, inversión |
| Nube | Tres frentes × cinco ambientes; Control de cruces en M4 | OSS (consumo) | — | — | M3–M4 reducido; Producción y recuperación completas **desde M13** | Sí, gasto mensual |
| Licencias de terceros | Software base y plataforma (SUM-28) | OSS a nombre del cliente | M4 (1.4.7) | — | M4 | Sí |
| Lote 1 | Patrón de 3 tiendas piloto y de la tienda de laboratorio | OSS | **M3** (8 de marzo de 2027, tras H1) | Estándar M4 (4 de mayo); UPS M5 (1 de junio) | M5–M6 (1 al 9 de junio de 2027) | Sí, inversión |
| Lote 2 | 19 tiendas y 2 CD | OSS | **M5** (7 de mayo de 2027, tras H2) | Estándar M6 (3 de julio); UPS M7 (31 de julio) | M7–M8 (31 de julio al 1 de septiembre de 2027) | Sí, inversión |
| Enlaces de operador | 2 accesos fijos por sitio y router 4G/5G (SUM-08 y SUM-33) | OSS gestiona; renta mensual | Con cada lote | — | Laboratorio y piloto M5–M6; lote 2 M7–M8 | Sí, gasto mensual desde la instalación |
| Recuperación completa | Brazil South a tamaño de Producción | OSS | — | — | Configuración M9; encendido completo M13 | Sí, gasto mensual |
| Lockers y fila virtual | Equipos de las innovaciones (SUM-14, nuevos) | OSS | **M14 (derivado, no modelado en la red)**: 12 semanas antes de la preparación del piloto E2 (8 de mayo de 2028) | M17 | M17–M19 (1.10.1.4 y 1.10.5.5) | Sí, inversión |
| POS, terminales y obra civil | SUM-13 y SUM-31 | **Cliente** | — | — | — | **No.** Va a la hoja informativa (comunicado §9) |

El lote 2 queda instalado el **1 de septiembre de 2027, dos meses antes del congelamiento** del 1 de noviembre.

## Efecto en la dotación (FTE = HH ÷ 160)

| Mes | Antes | Después |
| :-- | --: | --: |
| M1 | 12,5 | 14,5 |
| M4 | 32,0 | 33,0 |
| M5 | 32,6 | 34,1 |
| M7 | 29,1 | 31,4 |
| M8 | 23,6 | 31,6 |

El resto de los meses cambia en menos de 1 FTE. «Antes» es la estabilización del paso B y «después», esta red. **Total de HH: 237.104,14** (234.493,47 + 2.610,67).

## Archivos

| Archivo | Contenido |
| :-- | :-- |
| `ampliar_red.py` | Genera la red ampliada desde el traspaso. Uso: `python3 -I ampliar_red.py <traspaso>/Red_CPM Red_CPM` |
| `Red_CPM/nodos.json`, `Red_CPM/relaciones.json` | Red ampliada (salida del script anterior) |
| `estabilizacion.json` | Inicios preferidos tras estabilizar con margen de 10 días |
| `matriz_red_fisica.py` | Matrices por rol frente a la programación original (resta HH reales, suma las nuevas) |
| `HH_matriz_roles_M1_M56.csv`, `FTE_matriz_roles_M1_M56.csv` | **Insumo de dotación vigente del modelo financiero** (37 roles × 56 meses) |
