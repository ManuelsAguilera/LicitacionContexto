# Handoff · figura de arquitectura física (sd-04) · 2026-10-23

Rama de trabajo: `feat/sd-04-arquitectura-fisica`. Estado: **borrador de diseño**, sin revisión humana. No se modificó ningún `.tex` ni se asignó estado «revisado».

## 1. Qué se hizo y dónde quedó

| Archivo (`04_Adjuntos/diagramas/`) | Qué es | Vigente |
| :--- | :--- | :--- |
| `diag-04-43_fisica-arquitectura-vertical` (`.drawio` `.png` `.pdf` `.py`) | **Figura física vigente.** Lectura de arriba hacia abajo, una petición ejemplo, Brazil South resumido, grilla fija de tres columnas. | **Sí** |
| `diag-04-42_red-tienda-bifurcaciones-prueba` (idem) | Diagrama de red **de prueba** de una tienda tipo (racks, switches, firewalls, DMZ hipotética, terminales, móviles). Tres flujos A/B/C con líneas concéntricas de color. | Prueba |
| `diag-04-41_fisica-escenarios-capas.drawio` | Un `.drawio` con capas «Operación normal» y «Conmutación a Brasil» (la segunda oculta). Sobre el diseño **anterior** (iteración 38). | Anterior |
| `diag-04-40_fisica-conmutacion-brasil`, `diag-04-39_fisica-operacion-normal` | Escenarios exportados del diseño anterior. | Anterior |
| `diag-04-38_fisica-flujo-peticion-osi` | Primer diseño orientado al flujo con zonas, subredes, insignias OSI, matriz por capa y Brasil como sitio secundario (cuatro mejoras). El `.py` genera `unica`, `normal`, `conm` y `capas`. | Anterior |
| `diag-04-37_arquitectura-fisica-general-ordenada` | Reordenamiento de flechas y clusters de la figura 4.52 original. | Superado |

Cada `.py` es autónomo: `python3 <archivo>.py salida.drawio [modo]` genera el `.drawio`. El PNG y el PDF salen con `drawio --no-sandbox -x -f png -s 1.6 -o x.png x.drawio` (el AppImage necesita `--no-sandbox`).

**Fuente editable de la figura 4.52 original: no existe en el repo.** Se reconstruyó desde la imagen y el inventario (`inventario-fisico-integral-2026-10-23.md`, que está **fuera del repo**, en `~/Downloads`).

## 2. Decisiones del usuario, en orden

1. **Evaluar la figura 4.52 y ordenarla:** buscar errores, separar flechas de elementos que el lector necesita libres, y distribuir clusters centrados respetando el encuadre.
2. **Rediseño orientado al flujo:** el usuario no distinguía nodos, subredes ni flujos. Pidió seguir una petición general por cada nodo y zona (cloud / on-premise / Internet / canales), mostrar medidas de seguridad, balanceo y cifrado, y representar las capas OSI. Pidió contornos notorios para Chile, Brasil y on-premise.
3. **Brazil South como sitio secundario** (se aceptaron las cuatro propuestas y la versión de dos capas):
   - banner «SITIO SECUNDARIO» con contorno discontinuo y metas RTO ≤ 4 h / RPO ≤ 15 min (sujetas a ensayo);
   - estado por nodo: ESPERA, RÉPLICA, APAGADO (y ACTIVO, PROMOVIDA, REPRODUCIR en conmutación);
   - flechas de copia gruesas y rotuladas, rutas internas de Brasil tenues;
   - secuencia de arranque D1–D7 del inventario;
   - variante de dos capas en draw.io.
4. **Diagrama de red de prueba** (respuestas a las preguntas previas): foco en una tienda tipo SIT-xx; vista híbrida (topología física por zonas con VLAN rotuladas y racks); datos a seguir: venta POS con tarjeta y consulta de cliente en móvil/web; estilo Cisco clásico, un PNG + `.drawio`. Se permitió no respetar al 100 % la propuesta.
5. **Corrección de rumbo sobre la figura física:** Brasil es una réplica, no debe detallarse servicio a servicio; el flujo era complejo de leer; debe leerse **de arriba hacia abajo, con usuarios arriba y las zonas (on-premise y nube) abajo**, siguiendo una petición general que cruce todas las zonas.
6. **«Ordénalo más dentro de las zonas»:** se pasó a una grilla fija (columnas Retail | compartido / X-01 | Filial, mismas x en on-premise y Azure; filas con etiqueta a la izquierda; una caja por ámbito; encabezados de subred alineados para no tapar entradas).
7. **Pregunta sobre racks:** la numeración «rack 1 / 2 / 3» es **mía**, no del inventario (ver §3).

## 3. Supuestos y pendientes (lo que NO viene de las Bases)

- **Racks:** el inventario (sec. 17) dice «tres racks 24U (servidores R, servidores F y comunicaciones), 8+8+15U». La numeración 1/2/3, la asignación de switches/firewalls al rack de comunicaciones y la de los CPE a ese rack son inferencias. **Pendiente acordado en espíritu, sin ejecutar:** renombrar a «rack de servidores Retail / Filial / de comunicaciones», quitar el rack de las tarjetas de CPE y anotar «ubicación en rack por definir en el levantamiento». Afecta cajas, tarjetas y textos de `diag-04-43` y de `diag-04-42`.
- **Túneles alternativos a Brasil** desde routers y DC: supuesto de diseño; el inventario no fija el mecanismo.
- **TLS sin versión** (las Bases no la fijan). Cifrado de la API local de tienda: «por definir».
- **Bloques IP 10.64–10.70:** reservas de diseño; no hay CIDR por subred.
- **DMZ de tienda** (solo en `diag-04-42`): hipotética, no está en la propuesta.
- **Fuera de la figura 43:** Administración (MFA/PIM) y Socios externos como actores con flecha; testigos de los pares, CPE de los dos operadores con detalle WAN y gestión VLAN 70. Los segmentos auxiliares son una sola tarjeta sin flechas. La cadena Filial y los puestos en gris son vista simplificada.
- **Variante de dos capas sobre el diseño vertical (43): pendiente.** Hoy las capas existen solo sobre la iteración 38. El usuario no la pidió de nuevo tras el rediseño; se ofreció.
- **Flecha W2 hacia Application Gateway Retail:** entra por el costado corriendo por el pasillo entre columnas; funciona pero es larga. Las flechas grises de puestos/AP hacia switches pueden quitarse si se quiere menos ruido.
- Si la figura entra al sd-04: numerarla, citar fuentes según `citas-proyecto` y registrar el uso de IA como «Alto» en la Tabla 4.17.

## 4. Datos del inventario usados (fuente: sec. 6, 7, 9, 11, 14, 17 del inventario)

54 VM de producción en Chile (40 AKS + 12 auxiliares + 2 sondas); 12 PostgreSQL (6 R, 5 F, 1 X); DR activo-pasivo templado con 50 VM de espera y 4 BI apagadas; RTO ≤ 4 h y RPO ≤ 15 min en críticos (sujetos a ensayo); orden de arranque: identidad y claves, red y DNS, datos y mensajería, cómputo y herramientas, servicios, entrada, validación funcional; dos hosts R y dos F por tienda (88 para 22 tiendas), X-01 local dentro del par F; conexiones C01–C52 y relaciones eléctricas P01–P04. La matriz OSI por salto de `diag-04-43` y `diag-04-38` se armó con esas conexiones.

## 5. Hallazgos sobre la figura 4.52 original (para no repetir errores)

El hub terminaba sin salida hacia Application Gateway y había una línea que saltaba VPN y firewall; los hosts no pasaban por switch; DC/CD se conectaba al router de Retail en vez de a los adaptadores; el mismo gris discontinuo significaba identidad, administración, telemetría y cruces; Entra ID aparecía dentro de «Chile Central» siendo global; Brasil tenía un solo ícono pese al rótulo «R/F/X separados»; faltaban X-01 → DR, testigos, CPE y VLAN 70.

## 6. Notas técnicas para quien retome los scripts

- Enrutado ortogonal propio (A* sobre cuadrícula de 10 px): evita tarjetas y encabezados de cluster, reserva carriles, bloquea el interior de subredes para flechas ajenas y deja 3 puertos por lado. Las aristas se anclan a la **tarjeta** (no al ícono) con `exitX/exitY` y puntos intermedios explícitos.
- Los centros de nodo deben ser múltiplos de 10 y la mitad de tarjeta (60) también, o los puertos caen fuera de la rejilla.
- Los encabezados de caja son obstáculos: si un puerto superior cae bajo el texto, la flecha da un rodeo. Se resuelve alineando el encabezado a la derecha o acortándolo.
- Las píldoras numeradas se colocan sobre el tramo más largo libre; si no cabe, se imprime «píldora sin lugar».
- Verificación incluida en cada corrida: `violaciones` (flechas sobre tarjetas o encabezados) y `cruces entre flechas`. Estado de `diag-04-43`: 0 violaciones, 2 cruces.
