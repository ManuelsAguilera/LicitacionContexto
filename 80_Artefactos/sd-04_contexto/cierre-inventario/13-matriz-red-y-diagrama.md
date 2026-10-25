# Matriz de red y diagrama ampliado 4.52

Fecha: 23-10-2026. Estado: diseño para revisión. Uso de IA Alto. La vista contiene 46 nodos y 51 conexiones; no representa infraestructura desplegada ni acredita segmentación aplicada.

## Entradas y reproducción

Las entradas editables son [nodos.csv](../../../04_Adjuntos/diagramas/diag-04-52_csv/nodos.csv), [conexiones.csv](../../../04_Adjuntos/diagramas/diag-04-52_csv/conexiones.csv) y [zonas.csv](../../../04_Adjuntos/diagramas/diag-04-52_csv/zonas.csv). El script `05_Gestion/scripts/generar_matriz_fisica52.py` lee estos datos, aplica coordenadas nuevas y genera draw.io, JSON semántico, geometría y comprobación. La semilla previa se conserva en `tmp/matriz52-original/`; no reejecutar la inicialización para editar posiciones existentes. Las mutaciones de conexiones se registran en [cambios.csv](../../../04_Adjuntos/diagramas/diag-04-52_csv/cambios.csv). Los nuevos nodos se identifican por diferencia respecto de la fuente anterior y se registran en el CSV de cambios de nodos.

`columna` y `fila` expresan la referencia 240×260, con origen (100,140) y posiciones fraccionarias para los ajustes locales; `x_nuevo/y_nuevo` son las coordenadas de aplicación. El icono ocupa 64×64 y el nombre hasta 220×72. Se usan corredores de ancho variable según los obstáculos y puertos. No se reduce texto para encajar más elementos. Los marcos representan sitios/segmentos, no capas OSI. `vista.json` define las cajas de título/leyenda y activa las rutas automáticas para esta composición.

La revisión por zonas conserva los 46 nodos, 51 conexiones, extremos, iconos y tamaños tipográficos. Sigue la referencia aportada por el usuario: actores públicos/administración encima, nube central y sitios Ancoa debajo. Retail y Filial tienen bloques propios en Chile Central, con hubs junto a sus enlaces de sitio; Brazil South permanece a la derecha. Los segmentos auxiliares y energía quedan dentro de las instalaciones, separados de los flujos cloud. La referencia aporta disposición, sin trasladar nombres de sistemas, proveedores ni tecnologías de su imagen.

La topología F1 se amplía por autorización expresa del usuario, incluida una vista única que supera el límite de 30 nodos. Se usan la paleta aprobada y símbolos Cisco. El validador/linter original no admite esas excepciones; la comprobación propia no se presenta como aprobación del catálogo. El JSON semántico conserva familias de recursos; el CSV, el editable y la geometría conservan iconos y posiciones específicas. Las pruebas de producto y de infraestructura siguen pendientes.

## Segmentos y reglas mínimas

Los números VLAN siguientes son una convención inicial de diseño, no IDs descubiertos en la red. Deben contrastarse con IPAM y configuración real antes de implementar. Los CIDR cloud de la ficha B siguen siendo reservas. Ninguna VLAN por sí sola acredita aislamiento: se exigen VRF/ACL/firewall, identidad y pruebas de denegación.

| Segmento | VLAN / VRF | Flujos permitidos | Control de frontera |
| --- | --- | --- | --- |
| Cajas/puestos Retail | 10 / R | Cliente de caja a servicio local R y APIs R autorizadas | Autenticación de dispositivo, 802.1X donde sea compatible, ACL y firewall R |
| Servidores Retail | 11 / R | Réplica R-01/02, sincronización R, contrato mínimo de compra hacia X local | Cuentas y claves R; sin acceso a F ni a su base |
| WLAN corporativa Retail | 12 / R | Dispositivos gestionados a servicios R del perfil | EAP-TLS en equipos gestionados; no PSK general para todo Ancoa |
| Terminales financieros | 20 / F | Servicios locales/cloud F según perfil | Identidad F y posture; sin red de cámaras o invitados |
| Servidores Filial | 21 / F | Réplica F-01/02, libro de reservas y sincronización F | Identidad y almacenamiento F; no admite consultas Retail directas |
| WLAN financiera | 22 / F | Dispositivos autorizados a servicios F | Autenticación propia, EAP-TLS y control F |
| X-01 local | 23 / X | Entrada R→listener X y llamada X→API F de autorización; bitácora hacia X cloud al reconectar | Microsegmento y credenciales X, esquema mínimo, TLS y allowlist; no es peering R-F |
| IoT/lockers | 40 / IoT | Controlador a contrato específico de Pedidos por entrada R | Borde auxiliar con allowlist; no DB, cupo o administración |
| CCTV | 50 / Video | Cámaras al NVR; mantenimiento solo por perfil administrativo | Sin ruta a negocio; retención y acceso propios |
| Invitados | 60 / Guest | Solo salida Internet | Aislamiento entre clientes, prohibición de destinos internos y sin acceso a cloud privado |
| Administración | 70 / Management | Dispositivo conforme a endpoints privados administrativos propios | MFA, PIM, Bastion/Private Access; privilegio temporal |

El símbolo de switch/borde auxiliar agrupa recursos y contextos por finalidad; no da tránsito libre a los segmentos auxiliares. La flecha invitados→Internet expresa únicamente la salida permitida, no una conexión física sin firewall. Las flechas de aplicación R→X local→F expresan contratos L7 y atraviesan el control de frontera; no autorizan conectividad IP general entre VRF. La implementación de sus interfaces se prueba con paquetes, identidades y logs.

## Convención gráfica y comprobación

Retail usa azul `#0072B2`, Filial violeta `#6F42A8`, X naranja `#B85C00`, administración gris `#596579`, copias/DR verde azulado `#008577` discontinuo y energía marrón `#8C613C` punteado. Los fondos suaves y los nombres refuerzan el significado. Los iconos Azure y Cisco conservan su representación; generador, ATS y PDU usan símbolos esquemáticos sin marca (G/ATS/PDU). El suministro generador→ATS→UPS→PDU no es un camino IP ni representa un único equipo para toda la cadena.

La comprobación detecta intersecciones de rutas con iconos, nombres y el área impresa de cabeceras, segmentos diagonales y coincidencias largas entre flechas. Un optimizador separa carriles cuando existe alternativa corta libre de obstáculos; esta composición recalcula las rutas y no reutiliza los carriles fijos de la matriz anterior. Resultado de la versión generada: cero obstáculos atravesados, cero diagonales y cero pares con solapamiento superior a 80 unidades. Los cruces puntuales conservan salto visual; no son uniones eléctricas ni de red. La imagen se inspecciona después de exportar; la comprobación no demuestra una red aplicada.

El registro verificable está en [verificacion.json](../../../04_Adjuntos/diagramas/diag-04-52_fisica-general-inventario.verificacion.json). La [matriz de suministro](12-matriz-suministro-costos.md) identifica qué debe especificarse y presupuestarse, con las excepciones contractuales del cliente y sin precios inventados. Cat 6 LSZH es selección de diseño de OSS; no se atribuye esa frase literal a las Bases.
