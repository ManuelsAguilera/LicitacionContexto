# Planilla de tres valores para el segundo método (paso 7, puerta G7)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Plantilla **vacía**: no contiene ninguna hora. Cada estimador la copia a un archivo propio (por ejemplo `12_tres_valores_estimador1.md`), llena sus horas sin consultar `10_esfuerzo.md` ni `07_uucw_uucp.md`, y la entrega. Se comparan con `python3 05_Gestion/scripts/comparar_metodos.py ARCHIVO1.md ARCHIVO2.md`.

## Instrucciones

1. Estima **horas-hombre de todo el trabajo** de esa fila (análisis, diseño, construcción, pruebas y gestión propia), como lo haría un equipo que la ejecuta de principio a fin. Un número por celda, sin texto.
2. **Optimista** es el valor si todo sale bien (casi sin imprevistos). **Probable** es el más realista. **Pesimista** es el valor si salen mal las cosas que sí pueden salir mal. Debe cumplirse optimista ≤ probable ≤ pesimista.
3. Deja en blanco una fila solo si no puedes estimarla. No inventes: una fila en blanco se informa como pendiente.
4. Estima por separado y sin consultar al otro estimador. La independencia es lo que da valor a la comparación.
5. Las **filas S-** son los servicios y la base tecnológica (desarrollo de software). Se comparan con el UCP. Las **filas R-** son las ramas de la EDT que el UCP no cubre. No se comparan; se suman.
6. Anota en una línea cada supuesto relevante debajo de la tabla.

## Desarrollo de software (se compara con el UCP)

| Código | Alcance | Unidad de tamaño | Optimista (h) | Probable (h) | Pesimista (h) |
| :-- | :-- | :-- | --: | --: | --: |
| S-EX | Servicio de existencias | 48 RF. Etapa 1 | | | |
| S-OF | Servicio de oferta comercial | 20 RF. Etapa 1 | | | |
| S-VE | Servicio de ventas | 14 RF. Etapa 1 | | | |
| S-OR | Servicio de originación de crédito | 14 RF. Etapa 1 | | | |
| S-EV | Servicio de evidencia financiera | 15 RF. Etapa 1 | | | |
| S-CC | Servicio de control de cruces | 12 RF. Etapa 1 | | | |
| S-CA | Servicio de cartera de crédito | 6 RF. Etapas 1 y 2 | | | |
| S-BT | Base tecnológica (identidad y accesos, degradación y congelamiento, plataforma de integración, observabilidad, capacidad analítica) | 19 RF. Etapa 1 | | | |
| S-AB | Servicio de abastecimiento | 3 RF. Etapa 2 | | | |
| S-PE | Servicio de pedidos | 31 RF. Etapa 2 | | | |
| S-CM | Servicio de comisiones | 3 RF. Etapa 2 | | | |
| S-MK | Servicio de marketplace | 25 RF. Etapa 2 | | | |
| S-PV | Servicio de posventa | 12 RF. Etapa 2 | | | |
| S-CL | Servicio de clientes Retail | 5 RF (por validar). Etapa 2 | | | |

## Lo que el UCP no cubre (se suma, no se compara)

| Código | Alcance | Unidad de tamaño | Optimista (h) | Probable (h) | Pesimista (h) |
| :-- | :-- | :-- | --: | --: | --: |
| R-01 | Gestión del contrato más allá del desarrollo: gobierno, control de cambios, riesgos y comunicaciones | 56 meses de contrato; comités mensuales, quincenales y semanales | | | |
| R-02 | Infraestructura: nube pública, centro de datos on-premise, componentes de borde, ambientes, especificación del hardware de terreno y de los dispositivos | Nube pública y on-premise (híbrido obligatorio); 22 tiendas y 2 centros de distribución | | | |
| R-06 | Datos, migración e integraciones: saneamiento y migración de la cartera, mapa y rediseño de las interfaces | 620.000 clientes por tramos; 14 interfaces entre 9 plataformas | | | |
| R-07 | Seguridad y cumplimiento fuera del desarrollo: modelado de amenazas, prueba de penetración, SBOM, cadena de suministro, Zero Trust | Estándares del Anexo B: RNF-70 a RNF-73 y RNF-33 a RNF-38 | | | |
| R-08 | Calidad y pruebas fuera de las pruebas funcionales: carga, estrés, resiliencia, recuperación ante desastres y aceptación formal | Umbrales de RNF-22, RNF-23, RNF-24 a RNF-28 y RNF-32 | | | |
| R-09 | Implantación: piloto, despliegue por tienda, marchas blancas, reversión, capacitación y gestión del cambio | Piloto de 3 tiendas; 22 tiendas y 2 centros; marchas blancas en los meses 13 a 15 y 19 a 20; unos 1.100 repositores externos y 1.900 incorporaciones de temporada | | | |
| R-10 | Cinco innovaciones obligatorias (aún candidatas) | 5 innovaciones, una por tipo (art. 29) | | | |
| R-11 | Operación y soporte: mesa de ayuda, mantención correctiva, preventiva y evolutiva, gestión de la infraestructura | 36 meses, desde el mes 21 | | | |
| R-12 | Transferencia tecnológica y reversibilidad: documentación, código fuente, base de conocimiento, programa de transferencia y Plan de Reversibilidad | Plan de Reversibilidad dentro de los primeros 90 días y actualizado cada año (art. 77.2) | | | |

## Supuestos del estimador

(Anota aquí una línea por cada supuesto.)
