# Lo que el UCP no cubre y el segundo método (paso 7, puerta G7)

Documento de contexto, no es entregable. Fecha: 2026-10-08. Estado: propuesta aprobada por el usuario el 2026-10-08, pendiente de la firma del equipo. Método: FEP03, diapositivas 7, 8 y 9 (qué cubre la métrica y qué se suma aparte; estimar con dos métodos independientes y explicar la diferencia). Actualizado tras corregir la EDT (`14_edt_corregida.md`): el segundo método pasó de «por servicio» a «por paquete». Referencia: el UCP con los valores del equipo da **31.850 h** de desarrollo (`10_esfuerzo.md`). Este documento **no estima horas** de lo que el método no cubre: no hay histórico del equipo ni de la empresa, y no se inventan cifras. Deja el método, las unidades de tamaño, los supuestos y la plantilla para que el equipo estime.

## 1. Qué cubre el UCP y qué no

La diapositiva 9 dice que la métrica cubre el análisis, el diseño, la construcción, las pruebas de lo construido, la gestión del desarrollo y la documentación técnica. Con la lectura B, esas actividades están dentro de las 31.850 h. No cubre migración y saneamiento de datos, infraestructura y licencias, capacitación y gestión del cambio, puesta en producción y marcha blanca, operación y niveles de servicio, ni garantías, seguros y costos financieros.

Las ramas de la tabla siguiente son las de la guía de la EDT. En la EDT corregida corresponden así: gestión → 1.1; base tecnológica e infraestructura → 1.4 (el software de la base está en 1.5.14); datos, migración e integraciones → 1.6 y 1.7; seguridad → 1.8; calidad → 1.9; implantación → 1.11, 1.12 y 1.13; innovaciones → 1.10; operación → 1.15; transferencia y reversibilidad → 1.14. La planilla y el mapa usan los códigos de la EDT corregida.

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

- **Hoy:** tres valores (optimista, probable, pesimista) **por paquete** de la EDT corregida, por juicio de expertos. Dos estimadores independientes llenan `12_plantilla_tres_valores.md` sin consultar el UCP. La media de cada fila es (O + 4P + Pe) / 6. Los 73 paquetes de software se comparan con el UCP; los 134 restantes se suman por rama.
- **Descomposición ascendente:** ya es posible, porque existe la EDT corregida (propuesta, pendiente de la firma del equipo). Con ella el método de tres valores se aplica a cada paquete, que es el nivel que pide el Formulario T-15.
- **Descartado:** Punto Función. La clase no da una conversión a horas y habría que importar un parámetro externo sin calibrar.
- **Comparación:** `python3 05_Gestion/scripts/comparar_metodos.py PLANILLA1.md PLANILLA2.md`. Calcula la media por paquete y la compara con el reparto del UCP por paquete (en proporción al UUCW de sus casos), por servicio y en total (31.850 h). El umbral es de ±25 %, firmado el 2026-10-08: entre 23.888 y 39.813 h. Si lo supera, hay que explicar la causa antes de continuar al paso 9. Las horas por paquete que usa el T-15 salen de `repartir_horas_paquetes.py` (`16_horas_por_paquete.md`).

## 3. Decisiones adoptadas por sugerencia (2026-10-08), pendientes de la firma del equipo

1. Se acepta tres valores como segundo método, por paquete de la EDT corregida (antes por servicio).
2. Dos personas estiman por separado y antes de ver el resultado del UCP.
3. Una persona estima cada paquete no cubierto (las ramas 1.1 a 1.4 y 1.6 a 1.15), con revisión cruzada, porque esos paquetes no dependen del UCP.
4. Los costos de infraestructura y licencias se cotizan (oferta económica). En la rama 1.4 solo se estima el esfuerzo de configurarlos.
5. Ninguna cifra de estas ramas entra a la oferta sin una fuente o una estimación del equipo.

## 4. Supuestos y límites

1. Este documento no incluye horas de los paquetes que el UCP no cubre. Las estima el equipo en la plantilla.
2. La capacitación certificada del personal del cliente aparece en la gestión del cambio (1.13) y en la transferencia (1.14). El estimador debe incluirla en una sola.
3. Los 36 meses de operación pueden depender del nivel de servicio del sd-10, que no está redactado.
4. La rama 1.10 depende de la decisión de las cinco innovaciones (sd-13, aún candidatas).
5. La dedicación del equipo (E7 en 0) es un supuesto sin respaldo hasta el sd-12; no afecta a este paso, pero sí a la capacidad (P8.2).

## 5. Lo que se necesita del equipo

- Dos estimadores para los 73 paquetes de software de la planilla.
- Un estimador por cada uno de los 134 paquetes restantes, con revisión cruzada.
- Confirmar el reparto de la capacitación entre las ramas 1.13 y 1.14.
