# Revisión de los formularios T-6 a T-22

Fecha: 2026-10-12. Estado: borrador para decidir con el equipo. Detalle de cada revisión, con línea, fuente y sugerencia, en `revision_formularios_detalle/` (un archivo por formulario o grupo).

## Qué se revisó y cómo

Doce formularios de la carpeta `Formularios/` de Prism (T-6, T-9, T-11, T-12, T-13, T-14, T-15, T-16, T-17, T-18, T-19, T-22) más el T-10 (que vino aparte, en la carpeta del sd-06). Cada uno se comparó con:
1. la definición oficial de las Bases Administrativas (¿pide y contiene lo que debe?);
2. los requisitos de las Bases Técnicas Transversales y del Caso;
3. la verdad vigente del proyecto (sd-01 a sd-04, ya reconciliados, y el glosario);
4. los sd-05 a sd-13.

Cada punto se marca «confirmado» o «por confirmar». Los números de línea son del archivo de Prism, no de `main` (en `main` solo están los formularios T-9, T-10 y T-16, y el T-16 vive en `sd-08/`).

## Una corrección a esta revisión

Los revisores partieron de un resumen de la verdad vigente que decía que el Comité de Operación sesiona desde el mes 16. Es un error mío: el artículo 71 de las Bases dice «mensual desde el mes 13» (ya revertido en el sd-01). Por eso el hallazgo **G-1 del T-9 es un falso positivo**, y cualquier otro que diga «mes 16» para ese comité también lo es. Los formularios T-9, T-18 y los sd-06, sd-07 y sd-08 estaban bien en eso.

## Conteo

| Formulario | Graves | Medianas | Bajas | Veredicto |
| :-- | :-: | :-: | :-: | :-- |
| T-6 | 4 | 9 | 6 | Incompleto frente a las Bases (con T-22) |
| T-9 | 2 (de 3) | 7 | 5 | Cubre lo que pide la letra a; falta alinear |
| T-10 | 0 | 6 | 4 | Razonable; herramientas por alinear |
| T-11 | 8 | 12 | 6 | **Hay que rehacerlo** contra el sd-04 |
| T-12 (1.ª mitad) | 8 | 10 | 5 | **Hay que regenerarlo** |
| T-12 (2.ª mitad) | 31 | 9 | 4 | **Hay que regenerarlo** |
| T-13 y T-17 | 4 | 9 | 5 | Cubren lo pedido; faltan pruebas clave |
| T-14 | 4 | 11 | 8 | Aritmética correcta; faltan anexos |
| T-15 | 5 | 8 | 6 | Aritmética correcta; falta dotación y reserva |
| T-16 y T-18 | 4 | 12 | grupos | T-16 correcto salvo residuales; T-18 incompleto |
| T-19 | 3 | 9 | 7 | Sin precios; metas y arquitectura por alinear |

Lo que sí cuadra (verificado): las 40.946 HH del T-14 y del T-15 (31.058 + 9.888), las 164 cuentas, los 127 paquetes de software, la curva mensual de 56 meses, los 12 hitos con los meses del sd-07, los 37 riesgos del T-16 con su aritmética y las cuentas EDT que cita, los pasos a producción (meses 16 y 21) fuera de congelamientos, las seis condiciones de cierre de la marcha blanca (art. 17.3) y la ausencia de precios en todos los formularios del Sobre 2.

## Lo más importante

### 1. El T-12 quedó construido sobre el catálogo y la arquitectura anteriores
Es el hallazgo de mayor impacto, porque es la matriz que se evalúa.
- Usa módulos M-01 a M-24, zonas Z1/Z2/Z3, «Site Principal/Secundario», ADR-01 a ADR-12, Kong, Keycloak, Wazuh, OpenTofu, Dell, APC y AWS, que los sd-03 y sd-04 vigentes no tienen. Es la misma deuda de la matriz A.4 del sd-02 antes de que la corrigiéramos.
- Usa el catálogo v3.0: faltan OP-01 a OP-09 y RF-227 a RF-231, y sobran RNF-61 a RNF-63 (reclasificados en la v3.1).
- **Rebaja umbrales:** RT-03.10 y RT-17.01 declaran 8 h de autonomía y la propuesta compromete 24 h. El caso puede endurecer una exigencia transversal, nunca rebajarla.
- Declara «Sí» a una tabla de correspondencia de identificadores (RF-174), que la línea roja prohíbe.
- Declara «Sí» a cosas que el sd-04 no respalda: RNF-25 exige 24 h sin enlace para el centro de distribución principal y el sd-04 compromete 4 h; tampoco aparecen tokenización, SBOM/SLSA/ASVS ni la Ley 19.799; SOC 24x7, DevSecOps, certificaciones y alianza con AWS no tienen sustento.
- 143 RT obligatorios o «según caso» figuran en «No» con «-». No hay «Parcial» ni columna de evidencia.
- Remisiones a secciones del sd-05 (5.5 a 5.11), a «Frente de jefaturas» del sd-01 y a las Tablas 4.9 y 4.11 del sd-04 que no corresponden.
- **Sugerencia:** regenerarlo desde la matriz A.4 del sd-02, que ya tiene los trece servicios y la nomenclatura del sd-04, con un script que valide que cada sección y tabla citada exista (como se propuso para A.4).

### 2. El T-11 contradice el reparto de hardware del sd-04
- El T-11 dice que el proponente provee el nodo local de tienda (44 más 5 repuestos). El sd-04 (Tabla 4.15) dice que el proponente lo especifica, configura y certifica y que el **Cliente lo adquiere**. El T-9 dice lo mismo que el T-11, así que ambos deben alinearse.
- El DC-01 no tiene ningún equipo ni obra especificados, y el T-11 pone «energía, climatización y seguridad física» a cargo del Cliente. El sd-04 y RT-06.33 le asignan al proponente la habilitación del recinto, con sus equipos.
- La red de tienda tiene un conmutador y un firewall; el sd-04 diseña una pila de dos switches y un par de FortiGate. Faltan los puntos de acceso Wi-Fi, el respaldo LTE/5G y dos de las seis VLAN.
- Faltan las estaciones de trabajo (RT-08.07) y los atributos que piden RT-08.01 y RT-08.10 a 08.13 (marca y modelo de referencia, consumo, margen de crecimiento, ciclo de vida).
- Varias cantidades de nube remiten a una «memoria de capacidad» que no las contiene, y las remisiones a las Tablas 4.10 y 4.11 del sd-04 deben ser a la 4.15.
- **Aviso:** el sd-04 nombra FortiGate y productos de Azure (Managed HSM, Application Gateway, Bastion) que el T-11 omite. Eso contradice mi nota anterior de que Fortinet y Dell no estaban decididos: el sd-04 sí fija FortiGate en la tienda y el centro de datos. Hay que revisar el sd-01 (§1.6) y el T-9, que dicen que solo Microsoft está decidida.

### 3. El T-6 no cumple lo que piden las Bases
- Falta el campo «Alcance ejecutado» (el T-6 oficial pide 11 campos y tiene 10).
- Las contrapartes dicen «contacto disponible a solicitud», sin nombre ni contacto. El artículo 34.1 pide datos verificables, y el Informe 1 lo marcó como crítico.
- El proyecto 3 nombra a una empresa chilena real (Hites), que el Informe 1 calificó como causal de exclusión.
- El T-22 afirma que el T-6 quedó corregido, y no es cierto. Al T-22 le faltan las filas de varias observaciones del Informe 1 (T-8, T-11, leyenda de la T-12, dimensiones 14.2).

### 4. Pruebas y plazos que faltan
- **T-13 y T-17:** no incluyen la prueba de venta con tarjeta propia sin enlace (meses 6 y 7), ni el ensayo del orden de degradación, ni la prueba del evento anual de 104.000 pedidos (resultado 25 del Anexo D). Los ejercicios de DR de los meses 26, 38 y 50 caen en febrero, dentro del congelamiento. No citan RT-09.06 ni RT-05.13.
- **Contradicción entre documentos:** el sd-04 pone el corte de 24 h en una tienda piloto real y el sd-07 y el T-18 lo ponen en preproducción aislada. Hay que decidir antes de redactar la prueba.
- **T-18:** no responde RT-20.01, 20.02, 20.04, 20.05 ni 20.06, y no trae los cortes de cartera T1 a T3 ni el apagado antes del 31-oct-2028.
- **T-14:** no incluye la fecha de cartera (último corte antes del 15-oct-2028), y las integraciones de la Etapa 1 cierran en H10 (mes 18), después de producción (mes 16). El cuerpo del T-14 cita el catálogo v3.0.

### 5. Riesgos y recursos
- **T-16 y sd-08:** los residuales de R-18, R-20, R-24 y R-34 (0,08) no cuadran con la reducción de probabilidad a 0,40 (daría 0,16). El disparador de R-02 («menos de 8 semanas de aviso») se cumple siempre, porque el aviso del Caso es de unas 6 semanas.
- **T-15:** faltan las 3.688 h de riesgos que el sd-08 dice que el T-15 asigna (el esfuerzo comprometido sería 44.634 h). No hay personas por rol, dedicaciones ni certificaciones: las 16 personas dan 2.560 HH al mes y el pico es del 97 %, sin espacio para las reservas de 15 % y 30 %. Líder de Desarrollo, Funcional e Integración no existen en el sd-01.

### 6. Innovaciones (T-19)
- Las metas del T-19 (−20 %, +20 %, −10 %, tres anunciantes en los meses 21 a 23, −30 %) contradicen al sd-13, que dice que los umbrales se fijan después del levantamiento. Además son compromisos exigibles (art. 30.3).
- Las innovaciones no aparecen en el sd-03 ni en el sd-04, y el campo 8 todavía dice «conciliar con el T-14», que ya tiene los paquetes 1.10.1 a 1.10.5.
- La Ficha 1 aparece duplicada.

### 7. Temas que se repiten en varios formularios
- Catálogo v3.0 (307) en el T-10, T-12 y T-14 en vez de v3.1 (308).
- Marcas Fortinet y Dell (T-9) frente a lo que fija el sd-04.
- «Frente» usado para equipos de trabajo, roles que no están en el sd-01 y variantes de nombre del glosario.
- Cadena de herramientas: el T-10 propone GitHub Actions y el sd-04 menciona Azure Pipelines.

## Decisiones que necesito de ti

1. **Reparto del hardware de tienda y del DC-01:** ¿el proponente provee el nodo local (como dicen T-9 y T-11) o lo adquiere el Cliente (como dice el sd-04)? Y el DC-01, ¿el T-11 debe listar los equipos que el sd-04 le asigna al proponente? Propongo alinear T-9 y T-11 al sd-04.
2. **Corte de 24 h:** ¿tienda piloto real (sd-04) o preproducción aislada (sd-07 y T-18)?
3. **Metas de las innovaciones:** ¿las del T-19 son compromiso (entonces se corrige el sd-13) o umbral de diseño no contractual?
4. **R-02:** ¿aviso de 6 u 8 semanas? Y ¿corrijo los residuales a 0,16 en el sd-08 y el T-16, o prefieres subir la reducción de probabilidad?
5. **T-6:** ¿puedes dar nombres ficticios de clientes y contrapartes? Sin eso no puedo completar el campo ni reemplazar a Hites.
6. **T-12:** ¿lo regenero desde la matriz A.4 del sd-02? Es lo más grande de esta revisión.
7. **Marcas del sd-04:** el sd-04 fija FortiGate. ¿Corregimos el sd-01 (§1.6) y el T-9 para reflejarlo, o se quitan las marcas del sd-04?
