# Lo que el UCP no cubre y el segundo método (paso 7, puerta G7)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta aprobada por el usuario el 2026-10-08, pendiente de la firma del equipo. Método: FEP03, diapositivas 7, 8 y 9 (qué cubre la métrica y qué se suma aparte; estimar con dos métodos independientes y explicar la diferencia). Referencia: el UCP con los valores del equipo da **31.850 h** de desarrollo (`10_esfuerzo.md`). Este documento **no estima horas** de lo que el método no cubre: no hay histórico del equipo ni de la empresa, y no se inventan cifras. Deja el método, las unidades de tamaño, los supuestos y la plantilla para que el equipo estime.

## 1. Qué cubre el UCP y qué no

La diapositiva 9 dice que la métrica cubre el análisis, el diseño, la construcción, las pruebas de lo construido, la gestión del desarrollo y la documentación técnica. Con la lectura B, esas actividades están dentro de las 31.850 h. No cubre migración y saneamiento de datos, infraestructura y licencias, capacitación y gestión del cambio, puesta en producción y marcha blanca, operación y niveles de servicio, ni garantías, seguros y costos financieros.

| Rama de la EDT (`guia_edt.md`) | ¿La cubre el UCP? | Qué falta | Método propuesto | Unidad de tamaño |
| :-- | :-- | :-- | :-- | :-- |
| 3, 4 y 5 Servicios de retail, emisora y frontera | Sí | Nada | UCP | 127 casos de uso (13 servicios y la base) |
| 2 Base tecnológica e infraestructura | Parcial | El software de la base está en el UCP (13 casos BT). Falta la infraestructura en nube y on-premise, las licencias, los ambientes, la especificación del hardware de terreno y los componentes de borde | Descomposición por componente, con tres valores | Nube pública y on-premise; 22 tiendas y 2 centros de distribución |
| 1 Gestión del proyecto | Parcial | La sobrecarga del 15 % cubre la gestión del desarrollo. Falta el gobierno del contrato de 56 meses, el control de cambios, los riesgos y las comunicaciones | Tres valores por rol, durante 56 meses | 56 meses; comités mensuales, quincenales y semanales (sd-01, 1.5) |
| 6 Datos, migración e integraciones | No | Migración de la cartera de crédito, saneamiento y mapa y rediseño de las interfaces | Descomposición por ola de migración y por interfaz, con tres valores | 620.000 clientes por tramos; 14 interfaces entre 9 plataformas |
| 7 Seguridad y cumplimiento | Parcial | El factor T11 y el diseño cubren la seguridad de la funcionalidad. Falta el modelado de amenazas, la prueba de penetración, SBOM y SLSA, ASVS y Zero Trust | Descomposición por control, con tres valores | RNF-70 a RNF-73 y RNF-33 a RNF-38 |
| 8 Calidad y pruebas | Parcial | Las pruebas funcionales están en el 15 %. Faltan carga, estrés, resiliencia, recuperación ante desastres y aceptación formal | Un ensayo por umbral de requisito no funcional, con tres valores | RNF-22, RNF-23, RNF-24 a RNF-28 y RNF-32 |
| 9 Implantación | No | Piloto, despliegue por tienda, dos marchas blancas, reversión, capacitación y gestión del cambio | Descomposición, con la tienda como unidad | Piloto de 3 tiendas; 22 tiendas y 2 centros; marchas blancas en los meses 13 a 15 y 19 a 20; unos 1.100 repositores externos; 1.900 incorporaciones de temporada |
| 10 Innovaciones | No | Cinco innovaciones aún candidatas | Reserva con tres valores hasta que se decidan | 5 innovaciones, una por tipo (art. 29) |
| 11 Operación y soporte | No | Mesa de ayuda, mantención correctiva, preventiva y evolutiva, y gestión de la infraestructura durante 36 meses | Descomposición por nivel de servicio, con tres valores | 36 meses, desde el mes 21 |
| 12 Transferencia y reversibilidad | No | Documentación, código fuente, base de conocimiento, programa de transferencia y Plan de Reversibilidad | Descomposición por entregable del art. 77 | Plan de Reversibilidad dentro de los primeros 90 días y actualizado cada año |

Garantías, seguros y costos financieros no son esfuerzo y van a la oferta económica.

## 2. Segundo método para el desarrollo

- **Hoy:** tres valores (optimista, probable, pesimista) **por servicio**, por juicio de expertos. Dos estimadores independientes llenan `12_plantilla_tres_valores.md` sin consultar el UCP. La media de cada fila es (O + 4P + Pe) / 6.
- **Cuando exista la EDT:** descomposición ascendente por paquete (la clase la considera buena si la EDT es completa). Hoy no se puede: la EDT no está redactada, solo existe su guía.
- **Descartado:** Punto Función. La clase no da una conversión a horas y habría que importar un parámetro externo sin calibrar.
- **Comparación:** `python3 05_Gestion/scripts/comparar_metodos.py PLANILLA1.md PLANILLA2.md`. Calcula la media por servicio y la compara con el total del UCP (31.850 h) y con el reparto del UCP por servicio. El UAW se reparte en proporción al UUCW de cada servicio. El umbral es de ±25 %, firmado el 2026-10-08: entre 23.888 y 39.813 h. Si lo supera, hay que explicar la causa antes de continuar al paso 8. La prueba `test_comparar_metodos.py` cubre el cálculo.

## 3. Decisiones adoptadas por sugerencia (2026-10-08), pendientes de la firma del equipo

1. Se acepta tres valores por servicio como segundo método hoy, y descomposición por paquete cuando exista la EDT.
2. Dos personas estiman por separado y antes de ver el resultado del UCP.
3. Una persona estima cada rama no cubierta (R-), con revisión cruzada, porque esas ramas no dependen del UCP.
4. Los costos de infraestructura y licencias se cotizan (oferta económica). En R-02 solo se estima el esfuerzo de configurarlos.
5. Ninguna cifra de estas ramas entra a la oferta sin una fuente o una estimación del equipo.

## 4. Supuestos y límites

1. Este documento no incluye horas de las ramas R-. Las estima el equipo en la plantilla.
2. La rama 9 (implantación) se solapa con la rama 12 en la capacitación certificada del personal del cliente (art. 77.1). El estimador debe incluirla en una sola.
3. Los 36 meses de operación pueden depender del nivel de servicio del sd-10, que no está redactado.
4. La rama 10 depende de la decisión de las cinco innovaciones (sd-13, aún candidatas).
5. La dedicación del equipo (E7 en 0) es un supuesto sin respaldo hasta el sd-12; no afecta a este paso, pero sí a la capacidad (P8.2).

## 5. Lo que se necesita del equipo

- Dos estimadores para las filas S- de la plantilla.
- Un estimador por cada fila R-.
- Confirmar el reparto de la capacitación entre las ramas 9 y 12.
