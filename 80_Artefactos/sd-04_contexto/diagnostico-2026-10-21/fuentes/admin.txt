# Bases Administrativas para la Preparación de la Propuesta

**Licitación N° TFEP-01/2026 — Pontificia Universidad Católica de Valparaíso, Escuela de Informática**

*Versión 1.0 — Fecha Documento: 18-08-2026*

---

FORMULACIÓN DE PROYECTOS

BASES ADMINISTRATIVAS PARA LA PREPARACIÓN DE LA PROPUESTA

Versión 1.0 Fecha Documento: 18-08-2026

Bases Administrativas

Bases para la preparación de la propuesta técnico-económica

Asignatura Taller de Formulación de Proyectos Informáticos — 1Cl-5444

Unidad académica Escuela de Informática, Pontificia Universidad Católica de Valparaíso

Profesor Antonio Moya Villegas — antonio.moya(pucv.cl

Objeto Diseño, Aesatralla, implementación, puesta en marcha y operación de una plataforma digital de misión crítica

Alcance del documento Común y obligatorio para las trece industrias del llamado

Modalidad Licitación Pública Internacional — etapa única, tres sobres

Duración del contrato 56 meses: implementación en dos etapas y 36 meses de operación

Documento complementario Bases Técnicas del caso asignado a cada empresa proponente

Versión 1.0 — agosto de 2026

Este documento contiene las condiciones administrativas, contractuales y transversales que rigen la licitación para la totalidad de las empresas proponentes, cualquiera sea la industria del caso que se les haya asignado. Las condiciones funcionales y técnicas propias de cada industria se establecen en las Bases Técnicas correspondientes.

Su lectura íntegra es obligatoria. La sola presentación de una oferta implica la aceptación incondicional de todo su contenido.

CONTENIDO

I - Disposiciones generales 1*”-13"

II - Objeto, alcance y requisitos transversales obligatorios 3-5 14*-30" NI! - Requisitos y condiciones de participación 6-8 31” -40* IV + Proceso de licitación 912 41*-53* V - Evaluación y adjudicación 13-17 54” -66* VI - Contratación y ejecución 18-22 67" -82* VII - Disposiciones especiales 23-26 83” - 94

Formularios A-1 a A-6, T-6 a T-22,

VIII - Anexos y formularios A-C E-21 a E-26

Cómo está organizado este documento

Los Títulos | y II! a VI! contienen el articulado administrativo y contractual habitual de un proceso de licitación: quién puede participar, qué garantías debe rendir, cómo se presenta la oferta, cómo se evalúa, cómo se adjudica y bajo qué reglas se ejecuta el contrato.

El Título Il es distinto y merece atención especial. Contiene el objeto de la contratación, el cronograma contractual obligatorio de 56 meses, el modelo de despliegue híbrido exigido, los requisitos transversales que toda solución debe satisfacer con independencia de la industria, y la exigencia de innovación. Es el título que define el nivel técnico mínimo del llamado.

El Título VII! reúne los formularios. Los del Anexo A integran el Sobre N” 1, los del Anexo B el Sobre N? 2 y los del Anexo C el Sobre N” 3.

Advertencia sobre el nivel de exigencia de estas Bases. El CLIENTE ha optado deliberadamente por un pliego exigente. Los requisitos de arquitectura, seguridad,

continuidad, calidad y operación que contiene el Capítulo 4 no son aspiracionales: son el estándar con que hoy se contratan plataformas de misión crítica en la industria. Una propuesta que los aborde de manera superficial no será competitiva, con independencia de su precio.

# I. Disposiciones generales

## Capítulo 1 - ANTECEDENTES Y MARCO NORMATIVO

### Artículo 1. IDENTIFICACIÓN DE LA LICITACIÓN

1.1 La presente Licitación Pública Internacional, identificada como LICITACIÓN N° TFEP-01/2026, tiene por objeto la contratación del diseño, desarrollo, integración, implementación, puesta en marcha, soporte y operación de una plataforma digital de misión crítica, en adelante «el PROYECTO», conforme a las especificaciones administrativas contenidas en las presentes Bases y a las especificaciones funcionales, técnicas y de industria contenidas en las Bases Técnicas del caso asignado a cada PROPONENTE.

1.2 El CLIENTE ha estructurado este llamado bajo la modalidad de licitación por caso. A cada PROPONENTE se le asigna una industria y un caso específico, cuyas Bases Técnicas se publican como documento separado e integrante de este proceso. Las presentes Bases Administrativas y Tecnología Transversales son comunes, íntegras y obligatorias para la totalidad de los casos e industrias del llamado, sin excepción.

1.3 La solución objeto del PROYECTO deberá representar el estado del arte de la industria en materia de arquitectura, seguridad, resiliencia, automatización y experiencia de usuario. El CLIENTE no aceptará propuestas construidas sobre tecnología descontinuada, sin soporte vigente del fabricante, o cuya arquitectura no admita evolución, escalamiento ni sustitución de componentes.

### Artículo 2. ENTIDAD CONVOCANTE

2.1 Para todos los efectos de las presentes Bases, la entidad convocante se denominará «el CLIENTE». El CLIENTE actúa como mandante, dueño del PROYECTO y contraparte técnica y administrativa durante los

procesos de licitación, evaluación, adjudicación, contratación, ejecución, operación y cierre.

2.2 El CLIENTE ejercerá sus facultades a través de la Comisión Evaluadora, del Administrador del Contrato y de la Contraparte Técnica, según se define en estas Bases.

### Artículo 3. DEFINICIONES

Para la correcta interpretación de las presentes Bases, de las Bases Técnicas y del Contrato, se establecen las siguientes definiciones, las que prevalecen sobre cualquier otro uso que los PROPONENTES den a los mismos

términos: ADJUDICATARIO PROPONENTE a quien se adjudica la licitación mediante acto formal del CLIENTE.

Capacidad de la solución de mantener el servicio ante la falla de uno o más de sus

ALTA DISPONIBILIDAD o na A A A componentes, sin intervención manual y sin pérdida de transacciones comprometidas.

Instancia completa e independiente de la solución. El PROYECTO exige, como mínimo, AMBIENTE los ambientes de Desarrollo, QA, Preproducción y Producción, más el ambiente de Recuperación ante Desastres.

Conjunto integrado por las Bases Administrativas, las Bases Técnicas del caso, sus

BASES . . AA anexos, formularios, aclaraciones y modificaciones.

Término Definición

CONSORCIO

CONTRAPARTE TÉCNICA

CONTRATO

ETAPA 1

ETAPA 2

HITO

INNOVACIÓN

MARCHA BLANCA

MTTR

OFERENTE o PROPONENTE

ON-PREMISE

OPERACIÓN

PRODUCCIÓN

PROYECTO

RPO

RTO

SLA / SLO / SLI

SOLUCIÓN HÍBRIDA

ZERO TRUST

Agrupación de dos o más personas jurídicas que presentan una oferta conjunta bajo responsabilidad solidaria.

Equipo designado por el CLIENTE para validar entregables, aprobar avances técnicos y emitir conformidades.

Instrumento que perfecciona la adjudicación y regula la relación entre el CLIENTE y el ADJUDICATARIO.

Primer alcance funcional y de infraestructura del PROYECTO, definido en las Bases Técnicas del caso, cuyo desarrollo se ejecuta entre el mes 1 y el mes 12.

Segundo alcance funcional del PROYECTO, definido en las Bases Técnicas del caso, cuyo desarrollo se ejecuta entre el mes 13 y el mes 13 inclusive.

Punto verificable del cronograma contractual asociado a entregables, criterios de aceptación y, cuando corresponda, a un pago.

Solución, práctica, tecnología o modelo nuevo o significativamente mejorado respecto de la operación actual del CLIENTE, formulada conforme al Capítulo 5 de estas Bases.

Período de operación supervisada de la solución con datos y usuarios reales, en paralelo con la operación vigente, sin que la solución sea todavía el sistema de registro oficial.

Tiempo medio de restauración del servicio, medido desde la detección del incidente hasta la restitución verificada de la operación.

Persona jurídica, consorcio o unión temporal que presenta una propuesta en el proceso. Componentes de la solución desplegados en instalaciones, centros de datos o bordes operacionales bajo control físico del CLIENTE.

Fase de soporte, mantención y operación continua de la plataforma, de 36 meses de duración, que se inicia en el mes 21.

Estado en que la solución constituye el sistema de registro oficial del proceso de negocio y sus datos tienen validez operativa, contable y legal.

Conjunto de servicios, productos, entregables, licencias, infraestructura y obligaciones objeto de la presente licitación.

Punto objetivo de recuperación: máxima pérdida de datos tolerada, expresada en unidades de tiempo.

Tiempo objetivo de recuperación: máximo tiempo tolerado para restituir el servicio tras una interrupción mayor.

Acuerdo, objetivo e indicador de nivel de servicio, respectivamente, conforme a la definición de ITIL 4 e ISO/IEC 20000-1.

Arquitectura en que la carga principal se ejecuta en nube pública y existen componentes obligatorios desplegados on-premise, integrados como un único sistema gobernado.

Modelo de seguridad en que ninguna red, dispositivo, identidad o carga de trabajo es confiable por defecto, y toda solicitud se autentica, autoriza y cifra de forma explícita.

### Artículo 4. MARCO LEGAL, NORMATIVO Y DE ESTÁNDARES

4.1 La presente licitación y el Contrato que de ella derive se regirán por:

1. Las presentes Bases Administrativas, sus anexos, aclaraciones y modificaciones. 2. Las Bases Técnicas del caso asignado y sus anexos.

3: 4

La legislación chilena vigente y aplicable.

. La Ley N” 19.886 de Bases sobre Contratos Administrativos de Suministro y Prestación de Servicios y su

reglamento, en lo que resulte aplicable.

Los principios de igualdad de los oferentes, libre concurrencia, estricta sujeción a las bases, transparencia y probidad.

4.2 El PROPONENTE declara conocer y obligarse a cumplir, en lo que le resulte aplicable, la siguiente normativa

nacional:

Ley N° 21.719 sobre Protección de Datos Personales y la institucionalidad de la Agencia de Protección de Datos Personales; y, mientras mantenga vigencia, la Ley N° 19.628.

Ley N” 21.663, Ley Marco de Ciberseguridad e Infraestructura Crítica de la Información, y las instrucciones de la Agencia Nacional de Ciberseguridad, cuando el caso corresponda a un servicio esencial u operador de importancia vital.

Ley N” 21.459 sobre Delitos Informáticos. Ley N” 19.799 sobre Documentos Electrónicos y Firma Electrónica.

Ley N” 20.393 sobre Responsabilidad Penal de las Personas Jurídicas y Ley N” 21.595 de Delitos Económicos.

Ley N” 20.422 sobre igualdad de oportunidades e inclusión social de personas con discapacidad. Legislación laboral, previsional, tributaria, aduanera y ambiental vigente.

Normativa sectorial específica que las Bases Técnicas del caso identifiquen para la industria correspondiente.

4.3 La solución ofertada deberá diseñarse, construirse y operarse conforme a los siguientes estándares y marcos de referencia, cuyo cumplimiento el PROPONENTE deberá acreditar explícitamente en su Oferta

Técnica:

ISO/IEC 27001 e ISO/IEC 27002; ISO/IEC 27017 (nube); ISO/IEC 27018 (datos

Seguridad de la información | personales en nube); NIST Cybersecurity Framework 2.0; NIST SP 800-207 (Zero

Trust).

OWASP ASVS 4.0 nivel 2 como mínimo; OWASP Top 10 y OWASP API Security Top 10;

Seguridad del software

OWASP SAMM para el proceso; CIS Benchmarks para el endurecimiento de sistemas.

Cadena de suministro de SLSA nivel 3 o superior; SBOM en formato CycloneDX o SPDX por cada artefacto software liberado; firma de artefactos y verificación de procedencia.

Continuidad del negocio

ISO 22301 para el sistema de gestión de continuidad; ISO/IEC 27031 para la continuidad TIC.

Gestión de servicios ISO/IEC 20000-1; prácticas ITIL 4; principios de Site Reliability Engineering. Calidad del producto ISO/IEC 25010 e ISO/IEC 25012 para calidad de datos; ISO/IEC/IEEE 29119 para software pruebas.

ISO/IEC/IEEE 42010 para descripción de arquitectura; TOGAF o equivalente declarado

Arquitectura . s me para el marco de gobierno arquitectónico.

PMBOK Guide (PMI) como marco base, complementado con prácticas ágiles donde el

Eco ate PROPONENTE lo justifique.

Accesibilidad WCAG 2.2 nivel AA como mínimo; EN 301 549 como referencia complementaria.

OpenAPI 3.1 para servicios síncronos; AsyncAPl 2.6 o superior para servicios dirigidos

Interoperabilidad A : Aya o P por eventos; estándares sectoriales que indiquen las Bases Técnicas.

NIST Al Risk Management Framework 1.0 e ISO/IEC 42001, cuando la solución

Gestión de riesgo de lA . ie : e incorpore componentes de inteligencia artificial.

ISO 14001 como referencia y métricas de eficiencia energética declaradas (PUE del

Sostenibilidad E al ld centro de datos, huella de carbono estimada de la operación).

La sola mención de un estándar sin evidencia de cómo la solución lo satisface será evaluada con puntaje cero en el criterio respectivo. El CLIENTE exige trazabilidad entre el estándar invocado, el control implementado y el entregable que lo evidencia.

### Artículo 5. DOCUMENTOS QUE RIGEN LA LICITACIÓN Y ORDEN DE PRECEDENCIA

5.1 Los documentos que rigen el presente proceso, en estricto orden de precedencia, son:

. Bases Administrativas y sus anexos.

. Bases Técnicas del caso asignado y sus anexos.

. Aclaraciones, respuestas a consultas y modificaciones emitidas formalmente por el CLIENTE. . Oferta Técnica del PROPONENTE adjudicado.

. Oferta Económica del PROPONENTE adjudicado.

. Resolución de Adjudicación.

. Contrato y sus anexos.

A

. Informes y presentaciones preparatorias aprobadas.

o

. Otros antecedentes documentados que proporcione el CLIENTE durante el proceso. 5.2 Los documentos señalados conforman un todo integrado y se complementan recíprocamente. Toda

obligación que aparezca en cualquiera de ellos se entenderá parte del Contrato, aunque no se repita en los demás.

5.3 En caso de discrepancia prevalecerá el orden establecido en el numeral 5.1. Si la discrepancia se produce entre disposiciones de un mismo documento, prevalecerá la más exigente para el ADJUDICATARIO.

5.4 Si el PROPONENTE detecta una contradicción, un vacío o una ambigúedad en las Bases, deberá plantearla durante el período de consultas. Presentada la oferta, se entenderá que el PROPONENTE aceptó la interpretación más exigente y no podrá invocar la contradicción como fundamento de mayor precio, mayor plazo o menor alcance.

### Artículo 6. INTERPRETACIÓN DE LAS BASES

6.1 Las Bases se interpretarán conforme a su sentido literal y, en subsidio, conforme a la finalidad del PROYECTO declarada en el Artículo 1”.

6.2 Las expresiones «deberá», «se exige», «obligatorio» y «como mínimo» constituyen requisitos de cumplimiento forzoso cuya omisión afecta la admisibilidad o el puntaje de la oferta. Las expresiones «podrá», «se valorará» y «deseable» identifican elementos que otorgan puntaje diferenciador, pero no condicionan la admisibilidad.

6.3 Toda cifra expresada como mínimo se entiende como umbral inferior. Ofertar por debajo de un mínimo constituye incumplimiento; ofertar por sobre él debe justificarse técnica y económicamente.

## Capítulo 2 - CONDICIONES GENERALES DEL PROCESO

Artículo 7. TIPO Y MODALIDAD DE LICITACIÓN 1. Tipo: Licitación Pública Internacional.

2. Modalidad: etapa única con presentación simultánea de Antecedentes Administrativos, Oferta Técnica y Oferta Económica, en sobres separados.

3. Proceso preparatorio obligatorio: tres informes y tres presentaciones preparatorias con retroalimentación formal del CLIENTE.

4. Sistema de evaluación: ponderación de presentaciones preparatorias, evaluación técnica y evaluación económica, conforme al Título V.

### Artículo 8. IDIOMA OFICIAL

8.1 El idioma oficial del proceso, de la documentación contractual, de los entregables y de la operación es el español.

8.2 Podrán presentarse en inglés, sin traducción, los folletos técnicos de fabricante, los catálogos de producto, las certificaciones internacionales y la documentación de referencia de estándares. En caso de discrepancia prevalecerá la versión en español.

8.3 Toda documentación operativa dirigida a usuarios finales del CLIENTE —manuales, interfaces, mensajes de error, notificaciones y material de capacitación— deberá entregarse íntegramente en español.

### Artículo 9. MONEDA, VALORES E IMPUESTOS

9.1 Las ofertas económicas deberán expresarse simultáneamente en Pesos Chilenos (CLP), Unidades de Fomento (UF) y Dólares de los Estados Unidos de América (USD).

9.2 Todos los valores deberán presentarse desglosados en valor neto, Impuesto al Valor Agregado y total. Los valores del Contrato se entenderán netos, salvo mención expresa en contrario.

9.3 Para efectos de evaluación y de conversión entre monedas se utilizarán exclusivamente los parámetros del Formulario E-24. El uso de tipos de cambio distintos constituye causal de observación grave y, si altera el orden de mérito, causal de inadmisibilidad de la oferta económica.

9.4 Los precios ofertados se entenderán firmes durante la Etapa 1 y la Etapa 2. Para la fase de Operación se admitirá reajustabilidad conforme a lo que el PROPONENTE declare y justifique en su Oferta Económica, la que no podrá superar la variación acumulada del Índice de Precios al Consumidor del período.

Artículo 10. CÓMPUTO Y CARÁCTER DE LOS PLAZOS 1. Los plazos expresados en días se entienden de días hábiles, de lunes a viernes, excluidos los festivos, salvo indicación expresa de días corridos. 2. Los plazos expresados en meses dentro del cronograma contractual se cuentan desde la fecha de inicio del Contrato, entendiéndose el mes 1 como el primer mes completo de ejecución. 3. Los plazos del proceso licitatorio son fatales e improrrogables. Su incumplimiento produce la exclusión automática del PROPONENTE, sin necesidad de declaración previa.

4. Excepcionalmente, y por razones fundadas, el CLIENTE podrá modificar plazos, lo que comunicará a todos los participantes registrados por los canales oficiales.

### Artículo 11. GASTOS DEL PROCESO

11.1 Todos los gastos en que incurran los PROPONENTES con motivo del estudio, preparación, presentación y defensa de sus ofertas serán de su exclusivo cargo, cualquiera sea el resultado del proceso.

11.2 El CLIENTE no efectuará reembolsos ni indemnizaciones por concepto de estudios y análisis, preparación de documentación, garantías y seguros, pruebas de concepto, traducciones, legalizaciones, viajes, traslados ni asesorías externas.

### Artículo 12. COMUNICACIONES OFICIALES

12.1 Toda comunicación del proceso se cursará por escrito, a través del correo electrónico institucional del CLIENTE y del canal formal que se informe al inicio del proceso, dirigido al Representante registrado de cada PROPONENTE.

12.2 El Representante deberá acusar recibo y entendimiento de toda comunicación dentro de las doce horas siguientes a su envío. La falta de acuse no suspende ni altera los plazos.

12.3 Las comunicaciones verbales, las conversaciones informales y los mensajes cursados por canales no oficiales no obligan al CLIENTE ni pueden invocarse como fuente de derechos.

12.4 Es responsabilidad exclusiva del PROPONENTE mantener actualizados los datos de contacto de su Representante. El CLIENTE no responde por comunicaciones no recibidas a causa de datos desactualizados, filtros de correo o buzones sin capacidad.

### Artículo 13. PROBIDAD, CONFLICTOS DE INTERÉS Y CONDUCTA

13.1 Los PROPONENTES deberán abstenerse de toda conducta que afecte la libre concurrencia o la igualdad de los oferentes, incluyendo acuerdos de precios, reparto de mercado, presentación de ofertas de acompañamiento y utilización de información privilegiada.

13.2 El PROPONENTE deberá declarar cualquier vínculo, relación de propiedad, parentesco o dependencia con integrantes de la Comisión Evaluadora o con la contraparte del CLIENTE. La omisión de esta declaración constituye causal de exclusión.

13.3 Se prohíbe todo contacto con integrantes de la Comisión Evaluadora respecto del contenido de las ofertas fuera de los canales y las instancias formales previstas en estas Bases.

13.4 La constatación de plagio, de suplantación de autoría, de falsificación de antecedentes o de presentación de información que no corresponda a la realidad producirá la exclusión inmediata del PROPONENTE y la

ejecución de la Garantía de Seriedad de la Oferta.

13.5 El uso de herramientas de inteligencia artificial generativa en la preparación de la propuesta deberá declararse en el Formulario A-6, indicando en qué secciones se utilizó y con qué finalidad. La declaración no exime al PROPONENTE de la responsabilidad íntegra sobre el contenido, la exactitud y la originalidad de su propuesta.

# II. Objeto, alcance y requisitos transversales obligatorios

## Capítulo 3 - OBJETO Y ESTRUCTURA DE LA CONTRATACIÓN

### Artículo 14. OBJETO DE LA CONTRATACIÓN

14.1 El objeto de la contratación es la provisión integral, llave en mano, de una plataforma digital de misión crítica para el proceso de negocio descrito en las Bases Técnicas del caso asignado, incluyendo el diseño de la

solución, la construcción del software, la provisión y configuración de la infraestructura, la integración con los

sistemas existentes del CLIENTE, la migración de datos, la implantación, la capacitación, la puesta en

producción y la operación de la plataforma por 36 meses.

14.2 El alcance comprende, sin que la enumeración sea taxativa:

Arquitectura de solución: arquitectura lógica, arquitectura física, arquitectura de datos, arquitectura de integración, arquitectura de seguridad y arquitectura de despliegue (Según se requiera o se exija en pauta de evaluación).

Construcción y configuración del software aplicativo, de sus servicios de integración y de sus componentes de borde.

Provisión, dimensionamiento, configuración y endurecimiento de la infraestructura en nube pública y de los componentes on-premise.

Provisión de licenciamiento de software de base, de plataforma y de terceros, a nombre del CLIENTE, por todo el período contractual.

Especificación técnica del hardware de terreno y de los dispositivos operacionales requeridos, indicando marca, modelo de referencia, cantidad y características mínimas, aun cuando su adquisición sea de cargo del CLIENTE.

Migración, saneamiento y validación de los datos históricos que las Bases Técnicas del caso definan. Integraciones con los sistemas internos y externos identificados en las Bases Técnicas del caso.

Plan y ejecución de pruebas: unitarias, de integración, de sistema, de aceptación de usuario, de carga, de estrés, de resiliencia, de recuperación ante desastres y de seguridad ofensiva.

Implantación, marcha blanca, paso a producción y estabilización. Gestión del cambio organizacional, capacitación y transferencia tecnológica. Soporte, mantención correctiva, preventiva y evolutiva, y operación de la plataforma durante 36 meses.

Documentación técnica, operativa y de usuario, y entrega de código fuente y artefactos conforme al Título Vil.

### Artículo 15. ESTRUCTURA DEL SUMINISTRO

15.1 El PROYECTO se estructura en tres componentes contractuales indivisibles. No se admiten ofertas

parciales ni ofertas que excluyan alguno de estos componentes:

Alcance funcional y de infraestructura de primera prioridad Meses 1 a 12 (desarrollo); Etapa 1 — definido en las Bases Técnicas del caso, incluida la plataforma marcha blanca meses 13 a Implementación híbrida completa, la seguridad, la observabilidad y las 15; producción desde el integraciones críticas. mes 16.

Meses 13 a 18 (desarrollo); marcha blanca meses 19 y 20; producción desde el

Segundo alcance funcional definido en las Bases Técnicas del caso, construido sobre la plataforma de la Etapa 1 sin rehacer su arquitectura.

Etapa 2 — Implementación

mes 21. Soporte, mantención correctiva, preventiva y evolutiva, 36 meses continuos, desde Operación y soporte | operación de la plataforma, gestión de la infraestructura y el mes 21 hasta el mes 56 cumplimiento de los niveles de servicio. inclusive.

15.2 La duración total del Contrato es de 56 meses contados desde su fecha de inicio.

### Artículo 16. MODELO DE DESPLIEGUE HÍBRIDO OBLIGATORIO

16.1 La solución deberá ser obligatoriamente híbrida: la carga principal se ejecutará en nube pública y existirán componentes desplegados on-premise en las instalaciones u operaciones del CLIENTE. No se admiten propuestas exclusivamente en nube ni exclusivamente on-premise.

16.2 El PROPONENTE deberá justificar, componente por componente, la decisión de emplazamiento en función de latencia, criticidad operacional, volumen de datos, restricciones regulatorias, disponibilidad de conectividad y costo total de propiedad. Una asignación no justificada será evaluada como observación grave.

16.3 Exigencias del componente en nube

+ Proveedor de nube pública de alcance global con presencia de región o zona en Chile o en Sudamérica, declarando expresamente la región primaria y la región secundaria utilizadas.

+ Despliegue multi-zona de disponibilidad para todos los componentes con requisito de alta disponibilidad; el diseño en una sola zona no será aceptado.

e Infraestructura definida como código, versionada, revisable y reproducible en su totalidad. No se admite infraestructura creada manualmente por consola.

+ Segmentación de red por capas, con subredes privadas para las capas de aplicación y de datos, y exposición pública restringida exclusivamente a la capa de borde.

e Uso de servicios administrados por sobre servicios autoadministrados cuando ello reduzca el riesgo operacional, con justificación explícita en cada caso.

+ Gestión de costos en nube conforme a prácticas FinOps: etiquetado obligatorio de recursos, presupuestos, alertas de desviación y reporte mensual de consumo al CLIENTE.

+ Declaración explícita de la estrategia de reversibilidad y de mitigación del bloqueo por proveedor, identificando qué componentes son portables y cuáles no.

16.4 Exigencias del componente on-premise

e Capacidad de operación autónoma degradada ante la pérdida total del enlace con la nube, por el período mínimo que definan las Bases Técnicas del caso y en ningún caso inferior a 24 horas continuas.

e Sincronización diferida y reconciliación automática de las transacciones generadas durante la operación desconectada, con resolución determinista de conflictos y bitácora de las decisiones aplicadas.

+ Redundancia de los equipos on-premise críticos y esquema de almacenamiento con tolerancia a la falla de al menos un disco, declarando el nivel RAID y su justificación.

* Endurecimiento conforme a CIS Benchmarks, gestión centralizada de parches y control de acceso físico y lógico documentado.

+ Monitoreo del componente on-premise integrado a la misma plataforma de observabilidad que la nube, sin puntos ciegos.

e Enlace de comunicaciones redundante entre el sitio on-premise y la nube, con caminos y proveedores distintos, y conmutación automática.

El CLIENTE evaluará expresamente la coherencia entre la arquitectura lógica, la arquitectura física y la

estructura de costos. Una arquitectura correcta cuyo costo no la refleje, o un costo correcto sin arquitectura

que lo sustente, serán calificados como incoherencia grave de la propuesta.

### Artículo 17. CRONOGRAMA CONTRACTUAL OBLIGATORIO

17.1 El cronograma que se establece a continuación es obligatorio, indivisible y no negociable. Toda oferta que proponga plazos distintos será declarada inadmisible.

Levantamiento y línea base de alcance, diseño de arquitectura, construcción, integraciones, migración de datos, habilitación de los ambientes DEV, QA, PREPROD y PROD, pruebas integrales, pruebas de seguridad y certificación de la solución.

1-12 Etapa 1 - Desarrollo

Tres meses de operación supervisada con datos y usuarios reales, en 13-15 Etapa 1 - Marcha blanca | convivencia con la operación vigente del CLIENTE, con plan de reversión activo y medición diaria de indicadores.

La Etapa 1 pasa a producción y se convierte en el sistema de registro oficial

16 Etapa 1 - Producción - del alcance comprometido.

Desarrollo del segundo alcance funcional, en paralelo con la marcha blanca y 13 - 18 Etapa 2 - Desarrollo la estabilización de la Etapa 1, sin degradar los niveles de servicio comprometidos. Cierre del desarrollo en el mes 18 inclusive.

Dos meses de operación supervisada de la Etapa 2, conviviendo con la Etapa

19-20 Etapa 2 - Marcha blanca di 1 en producción, con integridad de datos garantizada entre ambos alcances. 21 Etapa 2 «Producción la Etapa 2 pasa a producción. Aceptación final del PROYECTO de implementación. o, 36 meses continuos de soporte de la plataforma y de la operación, bajo los 21-56 Operación

niveles de servicio del Artículo 78”.

17.2 Reglas de solapamiento y convivencia:

1. Entre los meses 13 y 15 coexisten la marcha blanca de la Etapa 1 y el desarrollo de la Etapa 2. El PROPONENTE deberá dimensionar dotación y frentes de trabajo suficientes para ambos esfuerzos y demostrarlo en la nivelación de recursos del Formulario T-15.

2. Entre los meses 19 y 20 coexisten la Etapa 1 en producción y la Etapa 2 en marcha blanca. La solución deberá garantizar una única fuente de verdad para los datos compartidos por ambos alcances y evitar toda doble digitación.

3. El paso a producción de la Etapa 2 en el mes 21 no podrá degradar la disponibilidad, el desempeño ni la integridad de los datos de la Etapa 1.

4. El inicio de la fase de Operación en el mes 21 es simultáneo al paso a producción de la Etapa 2 y comprende ambos alcances desde el primer día.

17.3 Condiciones de cierre de cada marcha blanca. Una marcha blanca sólo se dará por concluida y habilitará el paso a producción cuando, de manera copulativa: + No existan incidentes abiertos de severidad crítica ni alta atribuibles a la solución.

+ Se haya alcanzado el volumen de operación real comprometido en el plan de implantación, durante al menos las cuatro últimas semanas del período.

e Los indicadores de disponibilidad y de tiempo de respuesta comprometidos se hayan cumplido de forma sostenida durante ese mismo período.

e La conciliación entre la solución y el sistema o registro vigente no presente diferencias no explicadas. + El personal del CLIENTE haya sido capacitado y certificado conforme al plan de capacitación aprobado.

+ La Contraparte Técnica haya suscrito el acta de aceptación correspondiente.

Si al término del período de marcha blanca no se satisfacen las condiciones anteriores, el ADJUDICATARIO deberá extender la marcha blanca a su costo, sin cargo adicional para el CLIENTE, sin desplazar las fechas contractuales de las fases siguientes y quedando afecto a las multas por atraso del Artículo 80”.

### Artículo 18. HITOS CONTRACTUALES Y CRITERIOS DE ACEPTACIÓN

18.1 Los hitos contractuales, sus entregables y su ponderación en la estructura de pagos se establecen en el Formulario E-25. Cada hito se entiende cumplido únicamente con la suscripción del acta de aceptación por

parte de la Contraparte Técnica.

18.2 Todo entregable sometido a aceptación deberá incorporar: el documento o artefacto en sí, la evidencia objetiva de su verificación, la trazabilidad hacia los requerimientos que satisface y el registro de las observaciones previas resueltas.

18.3 El CLIENTE dispondrá de diez días hábiles para revisar cada entregable y pronunciarse. Formuladas observaciones, el ADJUDICATARIO dispondrá de diez días hábiles para subsanarlas. La segunda presentación de un entregable con observaciones de la misma naturaleza se considerará atraso imputable al ADJUDICATARIO.

18.4 La aceptación de un entregable no libera al ADJUDICATARIO de su responsabilidad por defectos posteriores, ni convalida incumplimientos de requisitos que se detecten con posterioridad.

## Capítulo 4 - REQUISITOS TRANSVERSALES OBLIGATORIOS DE LA SOLUCIÓN

Los requisitos de este Capítulo son exigibles a la totalidad de los casos e industrias del llamado, se suman a los requisitos específicos de las Bases Técnicas y deben acreditarse expresamente en la Oferta Técnica. Cuando las Bases Técnicas del caso establezcan una exigencia superior, prevalecerá esta última.

### Artículo 19. ARQUITECTURA Y DISEÑO

.

Arquitectura modular, con límites de contexto explícitos, acoplamiento débil entre módulos y contratos de interfaz versionados. Se rechazará toda arquitectura monolítica sin capacidad de despliegue independiente de sus componentes críticos.

Descripción de la arquitectura conforme a ISO/IEC/IEEE 42010, con vistas lógica, de procesos, de despliegue, de datos y de seguridad, y con registro de decisiones de arquitectura (ADR) fechado y fundado.

Capa de integración explícita y gobernada, con catálogo de servicios, control de versiones de contratos, política de compatibilidad hacia atrás y desacoplamiento mediante mensajería asíncrona donde el proceso lo admita.

Idempotencia obligatoria en todas las operaciones de escritura expuestas a reintentos, y garantía de entrega al menos una vez con deduplicación en los flujos de eventos.

Diseño para la degradación elegante: ante la indisponibilidad de un componente no crítico, la solución debe seguir operando en modo reducido y no fallar de forma total.

Patrones de resiliencia implementados y demostrables: reintento con retroceso exponencial, cortacircuitos, mamparos de aislamiento, límites de tasa y tiempos de espera explícitos en toda llamada remota.

Escalamiento horizontal automático de las capas de aplicación e integración, con umbrales, límites superiores y costo asociado declarados.

Ausencia de estado en la capa de aplicación; el estado de sesión y el estado de proceso deben residir en almacenes externos con alta disponibilidad.

Multi-tenencia o capacidad de replicar la solución a nuevas unidades, sitios o filiales del CLIENTE sin rediseño, cuando las Bases Técnicas del caso lo señalen.

### Artículo 20. DISPONIBILIDAD, CONTINUIDAD Y RECUPERACIÓN ANTE DESASTRES

Disponibilidad mensual mínima de 99,9 % para los servicios clasificados como críticos, medida sobre la transacción de negocio de extremo a extremo y no sobre la disponibilidad de la infraestructura.

Objetivo de tiempo de recuperación (RTO) máximo de 4 horas y objetivo de punto de recuperación (RPO) máximo de 15 minutos para los servicios críticos, salvo exigencia superior de las Bases Técnicas del caso.

Sitio o región secundaria de recuperación ante desastres, con replicación continua de datos y procedimiento de conmutación documentado y automatizable.

Prueba de recuperación ante desastres al menos semestral durante la fase de Operación, con ejecución real de la conmutación, informe de resultados y plan de corrección de las brechas detectadas.

Política de respaldo con esquema 3-2-1-1-0: tres copias, en dos medios, una fuera de sitio, una inmutable o fuera de línea y cero errores de verificación de restauración.

Respaldos cifrados en reposo y en tránsito, con retención declarada, con copias inmutables protegidas contra borrado y con prueba de restauración documentada al menos mensual.

* Plan de continuidad del negocio conforme a ISO 22301, con análisis de impacto en el negocio, escenarios de contingencia y procedimientos manuales de respaldo para el período de indisponibilidad.

+ Mantenimientos programados fuera de la ventana operacional crítica que definan las Bases Técnicas del caso, con aviso previo mínimo de diez días hábiles y con capacidad de despliegue sin interrupción del servicio.

### Artículo 21. SEGURIDAD DE LA INFORMACIÓN Y CIBERSEGURIDAD

21.1 Principios y gobierno

+ Arquitectura de seguridad basada en Zero Trust conforme a NIST SP 800-207: verificación explícita de cada solicitud, privilegio mínimo y presunción de compromiso.

+ Seguridad incorporada desde el diseño y por defecto, con modelado de amenazas documentado (STRIDE o equivalente) por cada componente y por cada integración externa. e Clasificación de la información del CLIENTE y controles diferenciados por nivel de clasificación.

+ Programa de gestión de vulnerabilidades con plazos máximos de remediación: 7 días corridos para vulnerabilidades críticas, 15 días para altas, 30 días para medias, contados desde su publicación o detección.

21.2 Protección de la capa expuesta

+ Publicación exclusiva a través de una capa de borde con red de distribución de contenidos, cortafuegos de aplicaciones web con reglas gestionadas y personalizadas, y protección contra denegación de servicio distribuida en capas 3, 4 y 7.

e Cifrado en tránsito con TLS 1.3, prohibición de TLS 1.0 y 1.1, conjuntos de cifrado modernos, HSTS con precarga y gestión automatizada de certificados con rotación y alerta anticipada de vencimiento.

e Cifrado en reposo de la totalidad de los datos, con claves gestionadas en un servicio de gestión de claves o módulo de seguridad de hardware, política de rotación declarada y separación de funciones en la custodia de claves.

+ Puerta de enlace de servicios (API gateway) con autenticación, autorización, cuotas, límites de tasa, validación de esquema e inspección de carga útil.

* Protección de bots y de abuso automatizado en los puntos de entrada públicos, con reto progresivo y sin degradar la accesibilidad.

21.3 Detección, respuesta y evidencia

* Registro centralizado e inalterable de eventos de seguridad, con retención mínima de doce meses en línea y veinticuatro meses adicionales en archivo recuperable.

e Correlación de eventos en una plataforma SIEM, con casos de uso de detección definidos para el proceso de negocio del caso y no sólo genéricos de infraestructura.

+ Detección y respuesta en puntos finales y en cargas de trabajo, tanto en nube como on-premise.

* Plan de respuesta a incidentes de seguridad con clasificación, cadena de escalamiento, plazos, responsables y protocolo de comunicación al CLIENTE dentro de las dos horas de detectado un incidente de severidad crítica.

+ Obligación de notificar al CLIENTE toda brecha de seguridad y de datos personales en un plazo no superior a 24 horas desde su detección, con informe preliminar, y de entregar el análisis de causa raíz dentro de los cinco días hábiles siguientes.

+ Pruebas de intrusión anuales por un tercero independiente del ADJUDICATARIO, y previas a cada paso a producción, con entrega íntegra del informe al CLIENTE y plan de remediación con plazos.

21.4 Seguridad del ciclo de desarrollo

e Análisis estático de código, análisis de composición de software, análisis dinámico y escaneo de imágenes de contenedor integrados en el flujo de integración continua, con criterios de bloqueo automático del despliegue.

+ Inventario de componentes de software (SBOM) por cada versión liberada, en formato CycloneDX o SPDX, entregado al CLIENTE.

e Firma de artefactos y verificación de procedencia conforme a SLSA nivel 3 o superior.

e Prohibición absoluta de credenciales, claves o secretos embebidos en el código, en imágenes o en archivos de configuración; uso obligatorio de un gestor de secretos con rotación automática.

+ Prohibición de utilizar datos productivos reales en ambientes no productivos sin anonimización o seudonimización verificable.

### Artículo 22. IDENTIDAD, ACCESO Y GESTIÓN DE SESIONES

+ Gestión de identidad centralizada, con federación mediante OpenID Connect y OAuth 2.1, o SAML 2.0 cuando la integración con el CLIENTE lo requiera, e integración con el directorio corporativo del CLIENTE por LDAP o su equivalente en la nube.

e Inicio de sesión único para todos los módulos de la solución y cierre de sesión propagado.

+ Autenticación multifactor obligatoria para usuarios administradores, para accesos privilegiados y para todo acceso desde fuera de la red corporativa; se valorará el soporte de factores resistentes a la suplantación de identidad (FIDO2 o claves de acceso).

+ Control de acceso basado en roles, complementado con control basado en atributos donde el proceso lo exija, y matriz de segregación de funciones documentada y verificable.

* Gestión de accesos privilegiados con acceso a demanda, elevación temporal, aprobación y grabación de sesión para las operaciones de mayor riesgo.

e Política de sesión declarada: duración máxima, caducidad por inactividad, renovación de credenciales de sesión tras la autenticación, revocación inmediata y control de sesiones concurrentes.

+ Credenciales de sesión firmadas y de vida breve, con credencial de refresco rotatoria; prohibición de transportar identificadores de sesión en la ruta de la dirección web.

+ Registro de auditoría de identidad: creación, modificación, elevación y baja de cuentas, con retención y no repudio.

e Procedimiento de aprovisionamiento y desaprovisionamiento automatizado ligado al ciclo de vida laboral del usuario, con baja efectiva en un plazo no superior a 24 horas desde la desvinculación.

+ Autenticación adecuada al perfil de usuario operacional descrito en las Bases Técnicas del caso, considerando entornos de terreno, guantes, baja alfabetización digital y dispositivos compartidos.

### Artículo 23. DATOS, INTEGRACIÓN E INTEROPERABILIDAD

+ Modelo de datos documentado, normalizado donde corresponda y con diccionario de datos entregable, incluyendo linaje y propietario de cada dominio de información.

e Trazabilidad completa de las operaciones de negocio: toda transacción debe permitir reconstruir quién, qué, cuándo, desde dónde y con qué valores anteriores y posteriores.

e Calidad de datos conforme a ISO/IEC 25012, con reglas de validación en el punto de captura, indicadores de completitud y exactitud, y proceso de saneamiento de los datos migrados.

e Interfaces de programación documentadas en OpenAPl 3.1 y, para los flujos por eventos, en AsyncAPl, con versionado semántico y política de obsolescencia con preaviso mínimo de seis meses.

e Capacidad de exportar la totalidad de la información del CLIENTE en formatos abiertos y documentados, en cualquier momento del Contrato y sin costo adicional.

+ Separación entre el almacenamiento transaccional y el analítico, con una capa analítica que no degrade el desempeño de la operación.

+ Retención, archivado y eliminación de datos conforme a la normativa aplicable y a la política que el CLIENTE apruebe, con procedimiento verificable de eliminación segura.

+ Residencia de datos declarada y sujeta a aprobación del CLIENTE; toda transferencia internacional de datos personales deberá contar con base de licitud y resguardos conforme a la Ley N” 21.719.

### Artículo 24. INGENIERÍA, DEVSECOPS Y CALIDAD

+ Cuatro ambientes obligatorios —Desarrollo, QA, Preproducción y Producción— aislados entre sí, con Preproducción equivalente en topología y configuración a Producción.

+ Integración y entrega continuas con despliegues automatizados, reversión automatizada y ausencia de intervención manual en el paso a producción.

e Estrategia de despliegue sin interrupción del servicio: azul-verde, canario o despliegue progresivo,

declarada y demostrada en Preproducción antes de cada paso a producción.

+ Control de versiones con revisión obligatoria por pares, ramas protegidas y trazabilidad entre requerimiento, cambio de código, prueba y despliegue.

+ Cobertura de pruebas automatizadas mínima del 70 % en el código de lógica de negocio, con umbral bloqueante en el flujo de integración continua, y batería de pruebas de regresión automatizada.

+ Pruebas de carga y de estrés ejecutadas sobre Preproducción con volúmenes equivalentes a 1,5 veces el peak declarado en las Bases Técnicas del caso, con informe de resultados y plan de capacidad.

+ Pruebas de resiliencia mediante inyección controlada de fallas, al menos antes de cada paso a producción y Una vez por semestre durante la Operación.

+ Gestión explícita de la deuda técnica, con registro, cuantificación y presupuesto asignado en la planificación de la Operación.

e Criterios de calidad conforme a ISO/IEC 25010 con umbrales numéricos declarados para funcionalidad, desempeño, compatibilidad, usabilidad, fiabilidad, seguridad, mantenibilidad y portabilidad.

### Artículo 25. OBSERVABILIDAD, OPERACIÓN Y NIVELES DE SERVICIO

+ Observabilidad completa y unificada de nube y on-premise: métricas, registros y trazas distribuidas correlacionadas por identificador único de transacción, con instrumentación conforme a OpenTelemetry.

* Tableros operacionales y de negocio disponibles para el CLIENTE, con indicadores de nivel de servicio medidos sobre la experiencia real del usuario.

e Alertamiento basado en síntomas de negocio y no sólo en umbrales de infraestructura, con supresión de ruido, escalamiento automático y turnos de disponibilidad declarados.

+ Mesa de servicio con canal único de registro, clasificación por severidad, seguimiento del ciclo de vida del incidente y reporte mensual de cumplimiento.

Libros de operación y guías de resolución documentados para cada escenario de falla previsible, con automatización progresiva de las tareas repetitivas.

Gestión de problemas con análisis de causa raíz obligatorio para todo incidente crítico, informe entregable dentro de cinco días hábiles y seguimiento de las acciones correctivas.

Presupuesto de error declarado por servicio y su vinculación con el ritmo de despliegue de cambios.

Gestión de la capacidad con proyección trimestral de crecimiento, alertas anticipadas de agotamiento y propuesta de ajuste de dimensionamiento y de costo.

### Artículo 26. ACCESIBILIDAD, USABILIDAD Y SOSTENIBILIDAD

Cumplimiento de WCAG 2.2 nivel AA en todas las interfaces destinadas a personas usuarias, verificado con herramientas automatizadas y con pruebas manuales, e informe de conformidad entregable.

Diseño centrado en las personas usuarias reales del caso, con investigación de usuario, prototipado y pruebas de usabilidad con participantes del CLIENTE antes de la construcción definitiva.

Indicadores de usabilidad medibles y comprometidos: tiempo máximo de la transacción operacional crítica, número máximo de pasos, tasa de error tolerada y curva de aprendizaje esperada.

Soporte para personas usuarias con baja alfabetización digital y para condiciones de terreno adversas cuando el caso lo requiera: alto contraste, objetivos táctiles amplios, operación con guantes, uso a la intemperie y funcionamiento sin:conexión.

Compatibilidad declarada de navegadores y de dispositivos, con política de soporte de versiones.

Eficiencia energética y sostenibilidad: dimensionamiento ajustado a la demanda, apagado de ambientes no productivos fuera de horario, elección de regiones con menor intensidad de carbono cuando sea viable y estimación de la huella de la operación.

Gestión responsable del ciclo de vida del hardware especificado, incluyendo recomendaciones de reacondicionamiento y disposición final.

### Artículo 27. CUMPLIMIENTO NORMATIVO, AUDITORÍA Y DERECHO DE INSPECCIÓN

Matriz de cumplimiento normativo por cada obligación legal y sectorial aplicable al caso, indicando el control implementado y la evidencia que lo acredita.

Registro de actividades de tratamiento de datos personales, evaluación de impacto en protección de datos cuando corresponda, y designación de una contraparte responsable de la materia.

Derecho del CLIENTE a auditar, por sí o por terceros independientes, la solución, los procesos, los controles de seguridad y las instalaciones del ADJUDICATARIO y de sus subcontratistas, con aviso previo de cinco días hábiles y sin costo para el CLIENTE.

Entrega anual al CLIENTE de los informes de certificación vigentes del ADJUDICATARIO y de sus proveedores de nube, y notificación inmediata de toda pérdida o suspensión de una certificación.

Conservación de la evidencia de cumplimiento por todo el período contractual y por veinticuatro meses adicionales.

## Capítulo 5 - EXIGENCIA DE INNOVACIÓN

### Artículo 28. CARTERA OBLIGATORIA DE CINCO INNOVACIONES

28.1 Cada PROPONENTE deberá formular, justificar y valorizar cinco innovaciones en su propuesta técnico-

económica, una por cada tipo obligatorio. No se admiten dos innovaciones del mismo tipo, ni innovaciones

enunciadas sin justificación técnica y sin valorización económica.

28.2 Las innovaciones deberán ser pertinentes a la industria del caso asignado y trazables con la arquitectura,

con la estructura de descomposición del trabajo y con el flujo de caja de la propuesta.

| me | Tipo deinmovación | Qué debe demostrar el PROPONENTE

Producto o servicio

Proceso

Tecnológica o de arquitectura

Modelo de negocio o de contratación

Experiencia de usuario, sostenibilidad o impacto social

Funcionalidad o servicio nuevo, o significativamente mejorado respecto de la operación actual del CLIENTE. Debe declararse el beneficio para el usuario final y el indicador con que se verificará.

Cambio en la forma de ejecutar el proceso de negocio, o el proceso de desarrollo y operación (automatización, integración, autoservicio, DevOps), con la mejora esperada en tiempo, tasa de error o costo unitario.

Adopción de una tecnología o de un patrón arquitectónico vigente (nube, datos, inteligencia artificial, integración o seguridad), justificada con estándares y fuentes citadas en norma APA 7.2 ed., indicando su nivel de madurez y el riesgo de adopción.

Cambio en la forma de generar o capturar valor: modelo de licenciamiento, pago por uso, servicios gestionados, niveles de servicio o esquema de escalamiento. Debe quedar reflejado en la estructura de costos y en el flujo de caja.

Mejora verificable en accesibilidad, usabilidad, inclusión, eficiencia energética o impacto ambiental y social de la solución, coherente con las restricciones del contexto del caso.

### Artículo 29. DOCUMENTACIÓN EXIGIDA POR CADA INNOVACIÓN

Para cada una de las cinco innovaciones, el PROPONENTE deberá presentar, en el Formulario T-19, los

siguientes elementos. La omisión de cualquiera de ellos reduce la innovación a un enunciado y será evaluada

como tal:

UN

Problema u oportunidad concreta del caso que la innovación resuelve, con el dato o la evidencia que

dimensiona el problema.

genérica.

7.2 edición.

. Tecnología, práctica o modelo que la sustenta, descrita con precisión técnica y no como categoría

. Nivel de madurez de la tecnología o práctica, con la escala utilizada y las fuentes citadas en norma APA

. Diseño de la incorporación: dónde se inserta en la arquitectura, qué paquetes de la estructura de

descomposición del trabajo la ejecutan y en qué mes del cronograma se materializa.

. Impacto económico estimado: inversión requerida, efecto en el costo operacional y beneficio esperado,

reflejado en el flujo de caja de la propuesta.

. Indicador de verificación del beneficio, con línea base, meta y momento de medición.

7. Riesgo de adopción, su probabilidad, su impacto, la estrategia de mitigación y el plan de contingencia si la innovación no rinde lo esperado.

### Artículo 30. EVALUACIÓN Y EXIGIBILIDAD DE LAS INNOVACIONES

30.1 Las innovaciones se evalúan en el subdocumento correspondiente de la Oferta Técnica y, en su dimensión económica, en el Entregable 2 de la Oferta Económica.

30.2 El CLIENTE valorará especialmente la pertinencia al caso por sobre la novedad tecnológica en abstracto. Una innovación de alta sofisticación técnica que no resuelva un problema real del caso obtendrá menor puntaje que una innovación sencilla, bien justificada y con impacto verificable.

30.3 Las innovaciones comprometidas en la propuesta adjudicada forman parte del alcance contractual y son exigibles como cualquier otro requerimiento. Su omisión durante la ejecución será tratada como incumplimiento del alcance.

No se aceptará como innovación: la sola adopción de una tecnología que ya constituye estándar de la industria; la mención de una tendencia sin diseño de incorporación; ni una funcionalidad exigida por las

Bases Técnicas presentada como innovación.

# III. Requisitos y condiciones de participación

## Capítulo 6 - PARTICIPANTES

### Artículo 31. QUIÉNES PUEDEN PARTICIPAR

31.1 Podrán participar en esta licitación personas jurídicas nacionales o extranjeras, consorcios o asociaciones de empresas y uniones temporales de proveedores, que cumplan copulativamente los requisitos de estas Bases.

31.2 Los participantes deberán:

= Tener giro social compatible con el objeto de la licitación.

Acreditar la idoneidad técnica y financiera exigida en el Artículo 34”. * No encontrarse afectos a las prohibiciones e inhabilidades del Artículo 32”.

* Registrarse formalmente como participantes dentro del plazo del calendario, designando un Representante único con poder suficiente.

+ Aceptar íntegramente las Bases, sin reservas, condicionamientos ni contrapropuestas.

31.3 Cada PROPONENTE participa respecto del caso e industria que el CLIENTE le asigne. No se admite presentar oferta para un caso distinto del asignado, ni presentar más de una oferta por caso.

### Artículo 32. PROHIBICIONES E INHABILIDADES

No podrán participar, y serán excluidos en cualquier etapa del proceso, quienes:

e Se encuentren en alguna de las situaciones del Artículo 4” de la Ley N” 19.886.

+ Tengan vigente declaratoria de quiebra, liquidación concursal o se encuentren en procedimiento de reorganización judicial.

- Registren incumplimientos contractuales graves con el CLIENTE en los últimos tres años.
- Mantengan litigios pendientes con el CLIENTE relativos a materias contractuales.

* Hayan sido sancionados por infracciones laborales, previsionales o tributarias graves en los últimos dos años.

+ Hayan sido condenados conforme a la Ley N? 20.393 o a la Ley N” 21.595 por delitos que afecten la probidad, salvo cumplimiento íntegro de la pena y acreditación de un modelo de prevención certificado.

+ Presenten conflictos de interés no declarados con integrantes de la Comisión Evaluadora o con la contraparte del CLIENTE.

* Hayan incurrido en las conductas prohibidas del Artículo 13”.

### Artículo 33. CONSORCIOS Y UNIONES TEMPORALES

Los consorcios y uniones temporales deberán:

1. Designar un representante único con poder suficiente para obligar a todos sus integrantes.

2. Establecer responsabilidad solidaria e indivisible entre todos sus integrantes respecto de la totalidad de las obligaciones del Contrato.

3. Presentar promesa de constitución formal, exigible en caso de adjudicación, con plazo de constitución no superior a quince días hábiles desde la notificación.

4. Indicar la participación porcentual de cada integrante y el aporte técnico concreto de cada uno.

5. Mantener su composición durante todo el proceso; la sustitución de un integrante requiere autorización previa y escrita del CLIENTE y sólo procede por causa grave. Ningún integrante podrá participar en más de un consorcio ni, simultáneamente, de forma individual en la misma licitación. La experiencia y la capacidad se evaluarán considerando la suma de los integrantes, con la ponderación que la Comisión Evaluadora determine según el aporte declarado.

### Artículo 34. REQUISITOS HABILITANTES DE IDONEIDAD TÉCNICA Y FINANCIERA

34.1 Constituyen requisitos habilitantes, cuyo incumplimiento produce la inadmisibilidad de la oferta sin evaluación técnica:

Acreditar al menos tres proyectos de software de misión Experiencia general | crítica finalizados y en operación en los últimos cinco años.

Formulario T-6 con datos verificables de contraparte.

Al menos un proyecto con arquitectura híbrida (nube más Experiencia on-premise) y un proyecto con operación bajo acuerdo de | Formulario T-6 y carta de específica nivel de servicio de disponibilidad igual o superior a 99,5 referencia del mandante. %.

Equipo clave completo y nominado, con dedicación declarada, que cubra al menos los roles de Jefe de Proyecto, Arquitecto de Solución, Encargado de Seguridad de la Información, Líder de Datos, Líder de Calidad y Líder de Operación.

Formulario T-8 con currículos y cartas de compromiso.

Capacidad de equipo

. . Certificación vigente en ISO/IEC 27001 o, en su defecto, ee . Certificaciones OR - Ed Certificado o plan formal firmado A plan de certificación con hitos verificables dentro de los

institucionales . por el representante legal. primeros doce meses del Contrato.

Condición de socio del proveedor de nube ofertado, o acuerdo formal con un socio certificado que participe del PROYECTO.

Certificado del proveedor o carta de compromiso del socio.

Capacidad de proveedor de nube

Estados financieros de los últimos tres ejercicios con

Solvencia . . e Ñ E Estados financieros y certificado . . patrimonio positivo, y capacidad de constituir las . - A financiera ! , bancario de capacidad de emisión. garantías del Capítulo 7. Certificado de la Dirección del Cumplimiento Sin deudas previsionales ni sanciones laborales graves Ñ . a Trabajo y Boletín Laboral y laboral vigentes.

Previsional.

34.2 El CLIENTE se reserva el derecho de verificar directamente con las contrapartes declaradas la efectividad de la experiencia informada. La constatación de información no veraz produce la exclusión inmediata y la ejecución de la Garantía de Seriedad de la Oferta.

## Capítulo 7 - GARANTÍAS Y SEGUROS

### Artículo 35. GARANTÍA DE SERIEDAD DE LA OFERTA

35.1 Cada PROPONENTE deberá entregar una Boleta de Garantía de Seriedad de la Propuesta, tomada en un banco comercial con oficinas en Valparaíso, Chile, a la vista, irrevocable, no endosable y a la orden del CLIENTE, expresada en Dólares de los Estados Unidos de América, por la cantidad de quinientos mil dólares (USD 500.000).

35.2 Glosa obligatoria: «Boleta de Garantía de Seriedad de la Oferta para la Licitación Internacional N° TFEP- 01/2026».

35.3 Vigencia: mínimo ciento cincuenta (150) días corridos contados desde la fecha de entrega de la propuesta, renovable antes de su vencimiento por períodos de a lo menos treinta y cinco (35) días, manteniendo su vigencia durante todo el proceso y hasta el décimo día hábil siguiente a la fecha de inicio del Contrato.

35.4 El CLIENTE podrá hacer efectiva esta garantía, sin necesidad de declaración judicial previa, en cualquiera de los siguientes casos:

+ Que se compruebe que cualquiera de los antecedentes entregados por el PROPONENTE no corresponde a la realidad.

+ Que el PROPONENTE se desista de su propuesta o la retire unilateralmente sin motivo fundado y aceptado por el CLIENTE.

- Que el PROPONENTE no concurra a una instancia obligatoria del proceso sin justificación.
- Que el ADJUDICATARIO no entregue la Garantía de Fiel Cumplimiento en el plazo establecido.
- Que el ADJUDICATARIO no suscriba el Contrato dentro del plazo máximo fijado.

35.5 La garantía se presentará en original, en el Sobre N” 1, en la fecha y hora del Calendario de Actividades (Formulario T-20). Será devuelta a los PROPONENTES no adjudicados a partir del undécimo día hábil siguiente a la firma del Contrato con el ADJUDICATARIO.

### Artículo 36. GARANTÍA DE FIEL CUMPLIMIENTO DEL CONTRATO

36.1 El ADJUDICATARIO deberá entregar una Boleta de Garantía de Fiel Cumplimiento del Contrato, tomada en un banco comercial con oficinas en Valparaíso, Chile, a la vista, irrevocable y a la orden del CLIENTE, conforme a las siguientes condiciones:

Instrumento Boleta bancaria, vale vista o depósito a plazo endosado a la orden del CLIENTE.

Monto USD 1.000.000 (un millón de dólares de los Estados Unidos de América).

Beneficiario El CLIENTE.

Glosa «Garantía de Fiel Cumplimiento del Contrato — Proyecto TFEP-01/2026».

Vigencia Desde la firma del Contrato y hasta doce (12) meses posteriores al término de la fase de Operación.

Plazo de entrega Dentro de los diez (10) días hábiles siguientes a la notificación de la adjudicación.

Efecto Reemplaza a la Garantía de Seriedad de la Oferta, la que se devolverá una vez recibida

conforme.

36.2 Esta garantía caucionará el cumplimiento íntegro y oportuno de todas las obligaciones del Contrato, incluidas las obligaciones laborales y previsionales del ADJUDICATARIO y de sus subcontratistas, y el pago de multas.

36.3 Si el CLIENTE hiciera efectiva parcialmente esta garantía, el ADJUDICATARIO deberá reconstituirla por el monto total dentro de los diez días hábiles siguientes. Su no reconstitución constituye causal de término anticipado del Contrato por incumplimiento grave.

### Artículo 37. GARANTÍA DE CORRECTO FUNCIONAMIENTO

37.1 Al término de la fase de implementación y como condición para la aceptación final del mes 21, el ADJUDICATARIO deberá constituir una Garantía de Correcto Funcionamiento equivalente al cinco por ciento (5 %) del valor total de la fase de implementación, con vigencia de veinticuatro (24) meses.

37.2 Esta garantía caucionará la corrección de defectos que se manifiesten con posterioridad a la aceptación final y que sean imputables al diseño, la construcción o la implantación de la solución.

### Artículo 38. SEGUROS

El ADJUDICATARIO deberá mantener vigentes, durante toda la ejecución del Contrato, y acreditar anualmente ante el CLIENTE, al menos las siguientes coberturas:

CO

R bilidad civil ] Toda la d ión del Ssponsa PEA BA UF 20.000 por evento y en el agregado anual. OCN profesional Contrato.

Toda la duración del

Ciberri bilidad UF 20.000 bertura d tos d tificació iberriesgo y responsabilidad por ), con cobertura de gastos de notificación, ES

datos análisis forense y restitución de datos. . posteriores. Todo rlesgo de equipos y blenes Valor de reposición de los equipos provistos u Desde la instalación A quipos y operados en instalaciones del CLIENTE. hasta la entrega final. Accidentes del trabajo y Toda la duración del

Conforme a la legislación vigente.

responsabilidad patronal Contrato.

## Capítulo 8 - REQUISITOS ADMINISTRATIVOS Y FORMALES

### Artículo 39. DOCUMENTACIÓN ADMINISTRATIVA OBLIGATORIA

Los PROPONENTES deberán presentar, en el Sobre N” 1, la totalidad de los siguientes antecedentes:

1. Identificación y antecedentes legales + Formulario A-1: Identificación del Proponente y de su Representante. + Fotocopia legalizada ante notario de la cédula de identidad del representante legal. + Rol Único Tributario de la empresa. e Certificado de vigencia de la sociedad, con antigúedad no superior a 30 días. + Fotocopia legalizada ante notario de la patente comercial al día. e Escritura de constitución y sus modificaciones. + Poderes vigentes del representante legal. * Individualización completa de los socios y, en caso de consorcio, de sus integrantes y su porcentaje de participación. 2. Antecedentes financieros + Certificado de deudas tributarias.

+ Estados financieros auditados de los últimos tres ejercicios.

.

Certificado de antecedentes comerciales.

Boletín Laboral y Previsional de la Dirección del Trabajo.

Certificado bancario que acredite capacidad de emisión de las garantías exigidas.

3. Declaraciones juradas ante notario

e Formulario A-2: no afectación por las prohibiciones del Artículo 4” de la Ley N° 19.886 y del Artículo 32” de estas Bases.

.

Declaración de no encontrarse en quiebra ni en reorganización judicial.

.

Formulario A-3: aceptación íntegra e incondicional de las Bases.

Formulario A-4: declaración de ausencia de conflictos de interés.

+ Constitución de domicilio en la ciudad de Valparaíso.

4. Antecedentes técnicos habilitantes + Carta de presentación del PROPONENTE con la nómina de contratos suscritos por servicios similares. + Cartas compromiso de socios tecnológicos, subcontratistas y proveedores clave. *e Formulario A-5: presentación e índice de antecedentes.

+ Formulario A-6: declaración de uso de herramientas de inteligencia artificial generativa.

Certificaciones institucionales y de fabricante vigentes.

### Artículo 40. REQUISITOS DE FORMA Y PRESENTACIÓN

40.1 Foliación. Todas las páginas deberán numerarse correlativamente, sin saltos ni páginas sin numeración, en zona visible del extremo inferior derecho. La falta de foliación es requisito excluyente y produce la exclusión automática.

40.2 Firmas. Media firma del representante legal o apoderado en el extremo inferior derecho de cada página y firma completa en la carátula y en los documentos principales.

40.3 Índices. Hoja resumen al inicio de cada sobre, con indicación del folio inicial de cada sección y correspondencia exacta con la foliación.

40.4 Formato de los documentos digitales:

A

PDF con texto seleccionable para los documentos; XLSX para el modelo financiero; los

Rormato documentos 1 y 2 de la Oferta Económica además en DOCX.

Tamaño de página Carta u oficio, orientación vertical, salvo anexos gráficos que podrán ser horizontales. Tipografía Cuerpo no inferior a 11 puntos; en tablas y figuras, no inferior a 9 puntos.

Índice Índice detallado con numeración de páginas en cada documento.

Referencias Norma APA 7.2 edición para toda cita y referencia bibliográfica.

Nomenclatura Conforme a los Artículos 49” a 51”. Un archivo mal nominado se considerará no presentado.

500 MB por sobre digital; los archivos mayores deberán segmentarse y declararse en el

Tamaño máximo za índice.

El CLIENTE no revisará documentos que no consten en el índice, que no estén foliados, que estén protegidos por contraseña no informada o que no puedan abrirse con las herramientas estándar declaradas.

La carga de la correcta presentación recae integramente en el PROPONENTE.

# IV. Proceso de licitación

## Capítulo 9 - OBTENCIÓN DE BASES Y CALENDARIO

### Artículo 41. ADQUISICIÓN DE LAS BASES Y REGISTRO DE PARTICIPANTES

41.1 Las Bases Administrativas, las Bases Técnicas del caso y sus anexos estarán disponibles sin costo desde la fecha indicada en el Calendario de Actividades (Formulario T-20).

41.2 Todo interesado deberá registrarse como participante indicando razón social, Rol Único Tributario, nombre del Representante, correo electrónico y teléfono de contacto. Sólo los participantes registrados recibirán las comunicaciones oficiales, las aclaraciones y las modificaciones.

41.3 La no recepción de una comunicación por no haberse registrado, o por datos de contacto erróneos, no suspende plazos ni genera derecho alguno para el participante.

### Artículo 42. CALENDARIO DEL PROCESO

El Calendario de Actividades es el establecido en el Formulario T-20 de estas Bases. Sus fechas son obligatorias para todos los participantes y sólo podrán modificarse por comunicación formal del CLIENTE.

## Capítulo 10 - CONSULTAS Y ACLARACIONES

### Artículo 43. PERÍODO DE CONSULTAS

43.1 Las consultas deberán formularse exclusivamente durante el período establecido en el Formulario T-20, por escrito y a través del canal oficial.

43.2 Formato obligatorio. Las consultas se presentarán en una planilla con la siguiente estructura:

Columna Contenido

A Número correlativo de la consulta.

B Nombre de la empresa proponente.

Cc Fecha de la consulta.

D Tipo: Administrativa, Técnica o Anexo.

E Documento, sección, artículo y página a que se refiere.

F Consulta detallada, formulada de manera concreta y precisa. G Propuesta de interpretación del proponente, si la tuviere.

43.3 Nomenclatura del archivo: CONSULTAS_[EMPRESA]_AAAAMMDD.XLSX

43.4 Fl CLIENTE responderá únicamente las consultas pertinentes al proceso, concretas y precisas, y que no

involucren información confidencial ni exijan al CLIENTE diseñar la solución en lugar del PROPONENTE.

43.5 Las respuestas se consolidarán en un Acta de Respuestas a Consultas, de conocimiento público para todos los participantes registrados, que pasará a formar parte integrante de las Bases con la precedencia del Artículo 5”. Las consultas se publicarán sin identificar a la empresa que las formuló.

Una consulta bien formulada es en sí misma un antecedente de calidad profesional. El CLIENTE registra qué empresas identifican vacíos, contradicciones y riesgos en las Bases, y qué empresas se limitan a solicitar

aclaraciones sobre materias explícitamente resueltas en el texto.

### Artículo 44. ACLARACIONES Y MODIFICACIONES DE OFICIO

44.1 El CLIENTE podrá emitir aclaraciones de oficio hasta cinco días hábiles antes del cierre de recepción de ofertas.

44.2 El CLIENTE podrá modificar las Bases hasta cinco días corridos antes de la recepción de ofertas. Toda modificación se notificará a los participantes registrados, formará parte integrante de las Bases y, cuando su entidad lo justifique, se acompañará de una prórroga del plazo de presentación.

## Capítulo 11 - INFORMES Y PRESENTACIONES PREPARATORIAS

### Artículo 45. OBLIGATORIEDAD Y CARACTERÍSTICAS

45.1 Con el objeto de asegurar que las propuestas cumplan los objetivos definidos por el CLIENTE, se realizarán tres informes y tres presentaciones preparatorias por cada PROPONENTE, en las fechas del Formulario T-20.

Aspecto Co!

Carácter Obligatorio. La no presentación implica la exclusión automática del proceso de adjudicación. Modalidad Privada, con la contraparte del CLIENTE y los representantes de la empresa.

Duración 15 minutos de exposición y 15 minutos de preguntas y discusión, salvo indicación distinta. Agenda Cerrada. En cada presentación sólo se abordarán los temas definidos en el Formulario T-22.

Deberá exponer más de un integrante del equipo; el CLIENTE podrá designar quién expone cada

Participación o, sección.

El informe escrito deberá entregarse en la fecha del calendario, con anterioridad a la

Entregable previo o presentación.

### Artículo 46. CONTENIDO DE LAS PRESENTACIONES PREPARATORIAS

El contenido exigido en cada instancia se detalla en el Formulario T-22. Cada informe deberá incorporar, además, la resolución explícita de las observaciones formuladas en la instancia anterior, mediante una tabla de trazabilidad observación—respuesta-sección modificada.

### Artículo 47. EFECTOS DE LAS OBSERVACIONES

47.1 Las observaciones formuladas por el CLIENTE en una instancia preparatoria son vinculantes. Su no incorporación en la propuesta final será evaluada como observación grave en el criterio afectado.

47.2 Las presentaciones preparatorias ponderan un diez por ciento del puntaje final, conforme al Artículo 62”.

47.3 La retroalimentación del CLIENTE no constituye aprobación de la solución ni traslada al CLIENTE responsabilidad alguna sobre las decisiones técnicas del PROPONENTE.

## Capítulo 12 - RECEPCIÓN Y APERTURA DE OFERTAS

### Artículo 48. PRESENTACIÓN DE OFERTAS

48.1 Las ofertas se presentarán en tres sobres separados e independientes, en la fecha y hora exactas del Formulario T-20. No se recibirán ofertas fuera de plazo, cualquiera sea la causa.

A

Físico, foliado y firmado, más

N*1 Antecedentes administrativos y Garantía de Seriedad de la Oferta. o respaldo digital.

N*2 Oferta Técnica conforme al Formulario T-7. Electrónico.

N*3 Oferta Económica conforme al Formulario E-21. Electrónico.

48.2 La entrega de los tres sobres es simultánea y copulativa. La falta de cualquiera de ellos hace inadmisible

la oferta en su conjunto.

### Artículo 49. SOBRE N” 1 — ANTECEDENTES ADMINISTRATIVOS

49.1 Carátula del sobre físico, en la que deberá leerse:

LICITACIÓN N° TFEP-01/2026

Proyecto de Plataforma Digital de Misión Crítica — Caso [N.* y nombre de la industria] SOBRE N? 1: ANTECEDENTES DEL OFERENTE

[Nombre del Proponente]

[Nombre del Representante Legal]

[Correo electrónico y teléfono del Representante]

49.2 Contenido: la totalidad de los documentos del Artículo 39”, la Boleta de Garantía de Seriedad en original,

el índice con folio de inicio de cada sección y los documentos foliados y firmados.

49.3 Respaldo digital: SOBRE1_[EMPRESA]_ANTECEDENTES_OFERENTE_AAAAMMDD.ZIP, con los documentos escaneados y con firmas y folios visibles.

Artículo 50. SOBRE N° 2 — OFERTA TÉCNICA 50.1 Contenido obligatorio conforme al Formulario T-7 y a los formularios técnicos del Anexo B.

50.2 Restricción absoluta: la Oferta Técnica no podrá contener información de precios, tarifas, valores unitarios ni cifra alguna que permita inferir el monto de la oferta económica. Su inclusión es causal de exclusión inmediata.

50.3 Nomenclatura: SOBRE2_[EMPRESA]_OFERTA_TECNICA_AAAAMMDD.ZIP

### Artículo 51. SOBRE N° 3 — OFERTA ECONÓMICA

51.1 Contenido obligatorio conforme al Formulario E-21, comprendiendo los tres entregables allí definidos.

51.2 Formato: valores en CLP, UF y USD; valores netos; IVA desglosado; totales por ítem y total general; tipo de cambio del Formulario E-24.

51.3 Nomenclatura: SOBRE3_[EMPRESA]_OFERTA_ECONOMICA_AAAAMMDD.ZIP

51.4 Los valores contenidos en los tres entregables de la Oferta Económica deberán ser idénticos entre sí y coherentes con la Oferta Técnica. Toda discrepancia no explicada es causal de descalificación.

### Artículo 52. ACTO DE APERTURA

1. Apertura del Sobre N” 1 en la fecha de recepción: verificación de la Garantía de Seriedad, revisión de la documentación administrativa y levantamiento de acta con las observaciones detectadas.

2. Exclusión, en el mismo acto, de las ofertas que no cumplan los requisitos esenciales o los requisitos habilitantes del Artículo 34”.

3. Custodia de los Sobres N” 2 y N” 3, que permanecerán cerrados hasta las respectivas etapas de evaluación.

4. Apertura del Sobre N” 2 al inicio de la evaluación técnica, con levantamiento de acta.

5. Apertura del Sobre N? 3 únicamente respecto de los PROPONENTES que hayan obtenido puntaje técnico igual o superior a 60, con levantamiento de acta de los montos ofertados.

Artículo 53. CAUSALES DE INADMISIBILIDAD DE LA OFERTA Serán declaradas inadmisibles, sin evaluación posterior, las ofertas que incurran en cualquiera de las siguientes causales:

+ Presentación fuera del plazo, de la hora o del lugar establecidos.

+ Ausencia de cualquiera de los tres sobres.

+ Ausencia, insuficiencia o defecto formal de la Garantía de Seriedad de la Oferta.

+ Falta de foliación o de firma en los términos del Artículo 40”.

* Incumplimiento de cualquiera de los requisitos habilitantes del Artículo 34”.

* Inclusión de información económica en la Oferta Técnica.

+ Proposición de plazos distintos del cronograma contractual obligatorio del Artículo 17”.

+ Propuesta de arquitectura exclusivamente en nube o exclusivamente on-premise, en contravención del Artículo 16”.

+ Oferta condicionada, con reservas, alternativas no solicitadas o sujeta a contrapropuesta de las Bases. + Discrepancias no explicadas entre los tres entregables de la Oferta Económica. e Información falsa, adulterada o que no corresponda a la realidad.

+ Ausencia de la cartera completa de cinco innovaciones exigida en el Artículo 28”.

La inadmisibilidad opera de pleno derecho y se declarará en acta fundada. El CLIENTE no está obligado a

otorgar plazo de subsanación respecto de estas causales.

# V. Evaluación y adjudicación

## Capítulo 13 - PROCESO DE EVALUACIÓN

### Artículo 54. COMISIÓN EVALUADORA

54.1 La evaluación estará a cargo de una Comisión Evaluadora designada por el CLIENTE, asesorada por una Comisión de Expertos cuya misión es analizar, evaluar y ordenar las ofertas según el cumplimiento de los requerimientos planteados.

54.2 Son atribuciones de la Comisión:

Evaluar las ofertas conforme a los criterios establecidos en estas Bases.

Solicitar aclaraciones a los PROPONENTES, sin que ello permita modificar, mejorar ni completar la oferta presentada.

Verificar directamente la información declarada, incluyendo contacto con las contrapartes de los proyectos informados.

Elaborar el informe de evaluación con la fundamentación de cada puntaje asignado. + Recomendar la adjudicación, la adjudicación parcial o la declaración de licitación desierta.

54.3 Los integrantes de la Comisión deberán declarar la ausencia de conflictos de interés respecto de todos los PROPONENTES.

Artículo 55. EVALUACIÓN ADMINISTRATIVA 55.1 Consiste en la verificación del cumplimiento de los requisitos formales y habilitantes.

55.2 Errores formales subsanables. El CLIENTE podrá otorgar un plazo de veinticuatro horas para subsanar errores estrictamente formales que no afecten la igualdad de los oferentes ni el contenido de la oferta. No son subsanables las garantías, la foliación, la firma, los documentos esenciales ni los requisitos habilitantes.

55.3 Las ofertas que no cumplan los requisitos esenciales serán declaradas inadmisibles conforme al Artículo 52” y no pasarán a evaluación técnica.

## Capítulo 14 - EVALUACIÓN TÉCNICA

### Artículo 56. ESCALA Y CRITERIOS DE ASIGNACIÓN DE PUNTAJE

56.1 Cada ítem del índice de la Oferta Técnica será evaluado en una escala de O a 100 puntos, conforme al siguiente criterio:

Puntaje | terio de asignación

100 El ítem cumple con todo lo solicitado, sin observaciones. 90 El ítem cumple con todo lo solicitado, con una observación menor. 80 El ítem cumple con lo solicitado, pero presenta dos observaciones.

Puntaje Criterio de asignaci

70 El ítem cumple con lo solicitado, pero presenta más de dos observaciones, o una observación grave. 60 El ítem cumple con el mínimo requerido.

50 El ítem cumple con el mínimo requerido, pero presenta observaciones.

40 El ítem menciona levemente lo solicitado, o cumple el mínimo con observaciones graves.

20 El ítem sólo se menciona, sin explicación que aporte valor.

0 El ítem no se encuentra, o no responde a lo solicitado.

56.2 Se entenderá por observación menor una imprecisión que no afecta la viabilidad de la solución; por observación grave, un error que compromete la coherencia técnica, la factibilidad, la seguridad o la trazabilidad de la propuesta.

56.3 Criterios de comparación entre ofertas. Dentro de cada ítem, la mejor propuesta obtendrá 100 puntos, las intermedias se interpolarán y el cumplimiento mínimo obtendrá 60 puntos. Para cumplimiento inferior al exigido, la propuesta más alta del grupo obtendrá 60 puntos y las restantes se interpolarán entre 21 y 59, correspondiendo O al incumplimiento total.

Artículo 57. PONDERACIÓN POR ÍTEM Y PUNTAJE TÉCNICO 57.1 La ponderación de cada ítem de la Oferta Técnica es la establecida en el Formulario T-21. El puntaje técnico

corresponde a la suma de los puntajes de cada ítem multiplicados por su ponderación.

57.2 El CLIENTE evaluará de forma transversal, y podrá descontar puntaje en cualquier ítem, la coherencia entre las secciones de la propuesta. En particular se verificará que: e La arquitectura declarada sostenga el alcance comprometido y esté reflejada en la estructura de costos.

e La estructura de descomposición del trabajo contenga la totalidad del alcance, incluidas las innovaciones y las actividades de seguridad, calidad, migración e implantación.

e El cronograma sea consistente con la estructura de descomposición del trabajo, con la nivelación de recursos y con el cronograma contractual obligatorio.

e La dotación y los perfiles del equipo sean coherentes con las horas hombre estimadas y con la curva de recursos.

e Los riesgos identificados correspondan a la solución efectivamente propuesta y no a un catálogo genérico.

* Los valores del modelo financiero deriven de las cantidades declaradas en la Oferta Técnica.

### Artículo 58. CONDICIONES DE EXCLUSIÓN EN LA EVALUACIÓN TÉCNICA

Serán excluidas de la continuación del proceso las ofertas que:

+ Obtengan un puntaje inferior a 30 en cualquier ítem de la evaluación técnica.

+ Obtengan un puntaje técnico ponderado total inferior a 60 puntos.

Omitan alguno de los subdocumentos obligatorios del Formulario T-7.

No acrediten el cumplimiento de los requisitos transversales obligatorios del Capítulo 4.

## Capítulo 15 - EVALUACIÓN ECONÓMICA

### Artículo 59. APERTURA DE LAS OFERTAS ECONÓMICAS

Sólo se abrirán las ofertas económicas de los PROPONENTES cuyo puntaje técnico ponderado sea igual o superior a 60 puntos. Se levantará acta con los montos ofertados por cada uno.

### Artículo 60. DETERMINACIÓN DEL INTERVALO DE CONFIANZA

60.1 Con el objeto de descartar ofertas anómalas por exceso o por defecto, el CLIENTE determinará un intervalo de confianza sobre el conjunto de los precios admitidos, conforme a la siguiente expresión:

| IC=[P=n'S, P+n-S]

Donde: IC Intervalo de confianza que define la banda de precios aceptados. P Promedio aritmético de los precios ofertados por las ofertas admitidas técnicamente. n Ponderador determinado por el CLIENTE en función de los datos de la muestra. E Desviación estándar muestral de los precios ofertados.

60.2 La desviación estándar se calcula como la raíz cuadrada de la suma de los cuadrados de las diferencias

entre cada precio y el promedio, dividida por el número de observaciones menos uno.

60.3 Las ofertas cuyo precio se sitúe sobre el límite superior o bajo el límite inferior del intervalo serán descartadas del proceso de evaluación económica y obtendrán cero puntos en este criterio.

El intervalo de confianza protege al CLIENTE de dos riesgos simétricos: el precio inflado y el precio

temerariamente bajo. Una oferta muy por debajo del promedio no es una ventaja competitiva, sino una señal de que el alcance no fue comprendido o de que el proyecto no es financieramente sostenible.

### Artículo 61. ASIGNACIÓN DEL PUNTAJE ECONÓMICO

61.1 Para las ofertas situadas dentro del intervalo de confianza, el puntaje económico se asignará conforme a la siguiente fórmula:

Puntaje Precio = 100 - (0,5 x ( Valor Oferente - Valor Mínimo ) / Valor Oferente ) x 100

61.2 El mejor precio dentro del intervalo obtiene 100 puntos. Las ofertas situadas fuera del intervalo obtienen O puntos.

61.3 Para la aplicación de la fórmula se considerará el Valor Total del Proyecto, esto es, la suma del valor de la fase de implementación (Etapas 1 y 2) y del valor de la fase de Operación por los 36 meses, expresado en la moneda de referencia del Formulario E-24.

Bases Administrativas TFEP-01/2026 33 / 77

## Capítulo 16 - EVALUACIÓN FINAL Y ADJUDICACIÓN

### Artículo 62. PUNTAJE FINAL

62.1 El puntaje final se determinará conforme a la siguiente ponderación:

PUNTAJE FINAL = (Presentaciones x 0,10) + (Técnica x 0,70) + (Económica x 0,20)

Informes 1, 2 y 3 y sus presentaciones, conforme al

P taci tori 10%

resentaciones preparatorias % Cormilario7.99 Evaluación técnica 70% Oferta Técnica, conforme a los Formularios T-7 y T-21. Evaluación económica 20% Oferta Económica, conforme a los Artículos 60” y 61”.

Artículo 63. CRITERIOS DE ADJUDICACIÓN Y DESEMPATE 63.1 Se adjudicará al PROPONENTE que obtenga el mayor puntaje final ponderado, siempre que cumpla la totalidad de los requisitos de estas Bases.

63.2 En caso de empate, se resolverá aplicando sucesivamente los siguientes criterios:

1. Mayor puntaje técnico ponderado.

2. Mayor puntaje en el ítem de arquitectura lógica y física. 3. Mayor puntaje en el ítem de innovaciones.

4. Mayor puntaje en el plan de trabajo, EDT y cronograma. 5. Mejor precio dentro del intervalo de confianza.

63.3 El CLIENTE se reserva el derecho de adjudicar parcialmente, de declarar desierta la licitación cuando ninguna oferta satisfaga sus necesidades, y de rechazar todas las ofertas, sin que ello genere derecho a indemnización alguna.

### Artículo 64. NOTIFICACIÓN Y PUBLICACIÓN DE LA ADJUDICACIÓN

64.1 La adjudicación se notificará al ADJUDICATARIO por carta certificada y correo electrónico, y a los demás PROPONENTES por correo electrónico, dentro de los cinco días hábiles siguientes a la resolución.

64.2 Junto con la notificación se publicará el cuadro comparativo de evaluación, con el puntaje de cada PROPONENTE por criterio y la fundamentación de la decisión.

## Capítulo 17 - EVALUACIÓN ACADÉMICA

### Artículo 65. ESCALA DE CALIFICACIÓN ACADÉMICA

65.1 Para efectos académicos, el resultado del proceso se traducirá en calificación conforme a la siguiente tabla:

A

Primer lugar — Existe una propuesta que cumple sobre el 90 % de los requerimientos en todos los

2 : 7,0 Ítems y es superior al resto.

Segundo lugar — Ofertas que cumplen sobre el 80 % de los requerimientos en todos los ítems. 6,3 Tercer lugar — Puntaje final en la evaluación técnica igual o superior a 60 % y puntaje en cada ítem 5.5 superior a 30%. Ñ Cuarto lugar — Puntaje final en la evaluación técnica igual o superior a 60 % y puntaje en cada 45 ítem superior a 30 %. : Quinto lugar e inferiores — Puntaje final en la evaluación técnica igual o superior a 60 % y puntaje 40 en cada ítem superior a 30%. ? No cumple técnicamente — Puntaje técnico inferior a 60 % o algún ítem inferior a 30 %. 3,0 Oferta no aceptada — Incumplimiento formal o administrativo que invalide la oferta. 1,0

### Artículo 66. AJUSTE POR EXCELENCIA DEL PRIMER LUGAR

66.1 Cuando ninguna propuesta alcance la calificación máxima de 7,0 por no superar el 90 % en todos los criterios, pero exista una propuesta que se destaque significativamente del resto, se aplicará un mecanismo de ajuste.

66.2 Condiciones copulativas para aplicar el ajuste: e La propuesta mejor evaluada debe presentar una diferencia mínima de diez puntos porcentuales en el puntaje final ponderado respecto del segundo lugar. + Debe cumplir con todos los requisitos técnicos mínimos establecidos. + Debe haber obtenido al menos el 75 % del puntaje máximo posible en la evaluación técnica.

66.3 Aplicado el ajuste, las demás propuestas se reposicionarán proporcionalmente según las diferencias establecidas.

# VI. Contratación y ejecución

## Capítulo 18 - FORMALIZACIÓN DEL CONTRATO

Artículo 67. DOCUMENTACIÓN PARA CONTRATAR El ADJUDICATARIO deberá presentar, dentro de los diez días hábiles siguientes a la notificación de la adjudicación: 1. Documentación legal e Escritura de constitución y sus modificaciones. e Certificado de vigencia con antigúedad no superior a 30 días. + Poderes vigentes del representante legal. e Inscripciones y publicaciones legales.

e Escritura de constitución del consorcio, cuando corresponda.

2. Documentación tributaria * Inicio de actividades. + Último balance tributario.

e Certificado de cumplimiento tributario.

3. Garantías y seguros * Garantía de Fiel Cumplimiento del Contrato conforme al Artículo 36”.

e Pólizas de seguro conforme al Artículo 38*.

4. Documentación del proyecto + Nómina definitiva del equipo clave, con cartas de compromiso individuales. + Acuerdo de confidencialidad suscrito por la empresa y por cada integrante del equipo clave. * Plan de trabajo detallado de los primeros noventa días.

+ Declaración de subcontratistas y proveedores clave, con sus respectivos acuerdos de confidencialidad.

Artículo 68. PLAZO Y CONDICIONES DE FIRMA 1. Plazo para suscribir el Contrato: diez días hábiles desde la entrega completa de la documentación.

2. Lugar: notaría designada por el CLIENTE. 3. Gastos notariales y de legalización: de cargo del ADJUDICATARIO. 4

. Si el ADJUDICATARIO no suscribe el Contrato en el plazo señalado, el CLIENTE hará efectiva la Garantía de Seriedad de la Oferta y podrá adjudicar al PROPONENTE que le siga en el orden de mérito, o declarar desierta la licitación.

### Artículo 69. CONTENIDO MÍNIMO DEL CONTRATO

El Contrato incorporará, como mínimo:

.

Identificación de las partes y de sus representantes.

Objeto y alcance detallado, con remisión expresa a las Bases y a la oferta adjudicada. Plazo de ejecución y cronograma contractual obligatorio del Artículo 17”. Precio, estructura de hitos y forma de pago conforme al Formulario E-25. Garantías y seguros.

Obligaciones de las partes y gobierno del proyecto.

Niveles de servicio, indicadores, método de medición y reporte.

Régimen de multas y penalidades.

Propiedad intelectual, código fuente, custodia de fuentes y licenciamiento. Confidencialidad y tratamiento de datos personales.

Plan de reversibilidad y salida.

Causales de término y procedimiento.

Mecanismos de solución de controversias.

## Capítulo 19 - GESTIÓN CONTRACTUAL

### Artículo 70. ADMINISTRACIÓN DEL CONTRATO

70.1 El Administrador del Contrato, designado por el CLIENTE, tendrá por función supervisar el cumplimiento

contractual, aprobar los estados de pago, gestionar las modificaciones y aplicar multas y sanciones.

70.2 La Contraparte Técnica, designada por el CLIENTE, tendrá por función validar entregables, aprobar avances

técnicos, coordinar las pruebas y emitir las conformidades que habilitan los hitos de pago.

70.3 El ADJUDICATARIO deberá designar un Jefe de Proyecto con dedicación exclusiva durante la fase de implementación, con facultades para comprometer al ADJUDICATARIO en materias de ejecución.

### Artículo 71. GOBIERNO DEL PROYECTO

Se establecen las siguientes instancias de gobierno, de asistencia obligatoria para ambas partes:

Propósito

Decisiones estratégicas,

Patrocinador del CLIENTE, gerencia del - a escalamiento, aprobación de

Comité Ejecutivo Mensual ADJUDICATARIO, Administrador del . Sel

cambios de alcance y revisión de

Contrato. . riesgos mayores. e Avance del cronograma, estado de Comité de . Contraparte Técnica y Jefe de E a Quincenal entregables, desviaciones y

Proyecto Proyecto del ADJUDICATARIO.

Comité de Arquitectura

decisiones operativas.

Arquitecto de Solución, Encargado de Aprobación de decisiones de Mensual Seguridad, referentes técnicos del arquitectura, revisión de deuda CLIENTE. técnica y de riesgos técnicos.

Cumplimiento de niveles de

Comité de Mensual desde | Líder de Operación, mesa de servicio, A o o. servicio, incidentes, problemas y Operación el mes 13 Contraparte Técnica. Ñ pl plan de mejora continua.

o Coordinación operativa, Reunión de . : - : y

o Semanal Equipos de trabajo de ambas partes. impedimentos y compromisos de la seguimiento

semana.

### Artículo 72. MODIFICACIONES CONTRACTUALES Y CONTROL DE CAMBIOS

1.

Toda modificación requiere acuerdo escrito de ambas partes, previa evaluación de impacto en alcance, plazo, costo, riesgo y niveles de servicio.

. Límite máximo acumulado de modificaciones: 20 % del valor original del Contrato.

. No podrán modificarse el objeto principal, la naturaleza del Contrato, las garantías mínimas ni el

cronograma contractual obligatorio del Artículo 17”.

Todo cambio deberá tramitarse mediante una solicitud formal de cambio, con análisis de impacto, y ser aprobado por el Comité Ejecutivo antes de su ejecución.

. La ejecución de un cambio sin aprobación previa es de cargo y riesgo exclusivo del ADJUDICATARIO y no

da derecho a pago adicional.

### Artículo 73. SUBCONTRATACIÓN

73.1 La subcontratación requiere autorización previa y escrita del CLIENTE y no podrá superar el 40 % del valor

del Contrato.

73.2 No podrá externalizarse el núcleo del negocio: las aplicaciones y la información críticas del CLIENTE no

pueden ser operadas ni custodiadas por terceros no autorizados expresamente.

73.3 El ADJUDICATARIO responde solidariamente por sus subcontratistas, quienes deberán cumplir los mismos estándares de seguridad, confidencialidad, calidad y cumplimiento laboral exigidos al contratista principal.

73.4 Todo subcontratista con acceso a datos del CLIENTE deberá ser declarado, auditado y sujeto a acuerdo de tratamiento de datos conforme a la Ley N° 21.719.

## Capítulo 20 - OBLIGACIONES DEL CONTRATISTA

### Artículo 74. OBLIGACIONES GENERALES

1.

HH p»ppesyN

Ejecutar el PROYECTO conforme a lo ofertado, a las Bases y al Contrato, con la diligencia de un profesional experto en la materia.

Mantener vigentes las garantías y los seguros durante todo el período contractual. Cumplir toda la normativa aplicable y mantener actualizadas sus certificaciones. Mantener confidencialidad absoluta sobre la información del CLIENTE.

Reportar el avance con la periodicidad y el formato acordados, informando oportunamente toda desviación.

Facilitar auditorías, inspecciones y fiscalizaciones del CLIENTE y de la autoridad competente.

7. Advertir por escrito al CLIENTE de toda decisión suya que, a juicio experto del ADJUDICATARIO, comprometa la seguridad, la continuidad o la calidad de la solución.

Artículo 75. OBLIGACIONES LABORALES Y PREVISIONALES 1. Cumplir íntegramente la legislación laboral y previsional vigente.

2. Mantener al día los pagos previsionales y de salud de todo su personal y del personal de sus subcontratistas.

3. Presentar mensualmente los certificados de cumplimiento de obligaciones laborales y previsionales. 4. Responder por los accidentes del trabajo y mantener vigentes los seguros correspondientes.

5. El CLIENTE podrá retener los pagos mientras no se acredite el cumplimiento de estas obligaciones.

Artículo 76. EQUIPO CLAVE, CONTINUIDAD Y REEMPLAZOS 76.1 Los integrantes del equipo clave nominados en la oferta constituyen un elemento determinante de la

adjudicación y no podrán ser reemplazados sin autorización previa y escrita del CLIENTE.

76.2 Todo reemplazo deberá recaer en un profesional de perfil igual o superior, acreditado documentalmente, con un período de traslape mínimo de quince días hábiles y sin costo adicional para el CLIENTE.

76.3 La rotación no autorizada del equipo clave, o una rotación superior al 30 % del equipo clave en un período de doce meses, constituye incumplimiento contractual y da lugar a la multa del Artículo 80”.

76.4 El ADJUDICATARIO deberá mantener documentación y conocimiento distribuidos, de modo que la salida de cualquier integrante no comprometa la continuidad del PROYECTO.

Artículo 77. TRANSFERENCIA TECNOLÓGICA Y REVERSIBILIDAD 77.1 El ADJUDICATARIO deberá ejecutar un programa de transferencia tecnológica que comprenda, como mínimo: * Capacitación completa y certificada del personal del CLIENTE, por perfil y por rol. + Entrega de la documentación técnica, funcional, de arquitectura, de operación y de seguridad, actualizada a la última versión desplegada. + Entrega del código fuente, de los artefactos de construcción, de los scripts de infraestructura como código y de los procedimientos de despliegue. + Base de conocimiento con incidentes, problemas, soluciones y decisiones de diseño. + Manuales de operación, libros de operación y guías de resolución de fallas. 77.2 Plan de reversibilidad y salida. Dentro de los primeros noventa días del Contrato, el ADJUDICATARIO deberá entregar un Plan de Reversibilidad, actualizado anualmente, que permita al CLIENTE o a un tercero asumir la operación sin interrupción del servicio, incluyendo el inventario de activos, el traspaso de

credenciales, la exportación íntegra de los datos en formatos abiertos y un período de acompañamiento de a lo menos noventa días.

77.3 La ejecución del Plan de Reversibilidad al término del Contrato, por cualquier causa, está incluida en el precio ofertado y no da derecho a cobro adicional.

## Capítulo 21 - NIVELES DE SERVICIO Y RÉGIMEN DE PENALIDADES

### Artículo 78. NIVELES DE SERVICIO

78.1 Clasificación de severidad de los incidentes:

Interrupción total del servicio, o afectación de un proceso de negocio crítico sin alternativa

Crítica . o : : operativa, o incidente de seguridad con compromiso de datos. Ale Degradación severa del servicio, o falla de una función crítica con alternativa operativa costosa, o a mm s afectación de un grupo relevante de personas usuarias. Medi Falla de una función no crítica, o degradación que no impide la operación, con alternativa edia . . disponible. Baja Consulta, incidencia menor, defecto cosmético o solicitud de información.

78.2 Niveles de servicio exigidos durante la fase de Operación:

COI

Disponibilidad mensual mínima 99,7% 99,5% 99,0% 98,0%

Tiempo máximo de respuesta 15 minutos 1 hora 4 horas 8 horas

Tiempo máximo de resolución 4 horas 8 horas 24 horas 48 horas

Cobertura de atención 24x7x365 24x7x365 pS aa Horario hábil extendido

Informe de causa raíz 5 días hábiles 10 días hábiles A solicitud No aplica

78.3 Indicadores adicionales exigidos:

Tiempo de respuesta de la transacción Conforme al valor que fijen las Bases Técnicas del caso, medido operacional crítica en el percentil 95 sobre la experiencia real del usuario.

Tiempo medio de restauración (MTTR) de

a des No superior a 4 horas, medido mensualmente. incidentes críticos

Tasa de cambios fallidos en producción No superior al 5 % de los despliegues del mes. Cumplimiento del RPO y del RTO en la prueba 100 % semestral de recuperación o: Vulnerabilidades críticas abiertas por más del Cero.

plazo del Artículo 21.1 Reincidencia de incidentes con la misma causa raíz No superior a un evento por trimestre.

Satisfacción de las personas usuarias con la mesa

MN Igual o superior a 4,0 en escala de 1a 5. de servicio

### Artículo 79. MEDICIÓN, REPORTE Y VERIFICACIÓN

79.1 La medición de los niveles de servicio se realizará sobre la plataforma de observabilidad, cuyos datos deberán estar disponibles para el CLIENTE en tiempo real y ser exportables.

79.2 El ADJUDICATARIO entregará, dentro de los primeros cinco días hábiles de cada mes, un informe de nivel de servicio con el detalle de cada indicador, los incidentes del período, las causas raíz y el plan de acción.

Licitación N° TFEP-01/2026

79.3 El CLIENTE podrá verificar la medición por sus propios medios. Ante discrepancias, prevalecerá la medición del CLIENTE, salvo que el ADJUDICATARIO acredite un error metodológico.

79.4 Las ventanas de mantenimiento programadas y aprobadas no computan como indisponibilidad. Las

ventanas no aprobadas o excedidas sí lo hacen.

### Artículo 80. MULTAS Y PENALIDADES

Incumplimiento CE

Atraso en la entrega de un entregable o hito.

Incumplimiento del nivel de disponibilidad comprometido.

Incumplimiento del tiempo de respuesta o de resolución.

Extensión de una marcha blanca por causa imputable al ADJUDICATARIO.

Vulnerabilidad crítica no remediada dentro del plazo del Artículo 21.1.

Incumplimiento del deber de notificación de un incidente de seguridad o de una brecha de datos.

Reemplazo no autorizado de un integrante del equipo clave.

No entrega o entrega incompleta del informe mensual de nivel de servicio.

Incumplimiento de las obligaciones de confidencialidad.

Incumplimiento de las obligaciones laborales o previsionales.

Procedimiento de aplicación:

0,5 % del valor del hito por cada día corrido de atraso, con tope de 10 % del valor del hito.

1% del valor mensual de la Operación por cada punto porcentual o fracción bajo el nivel comprometido, con tope de 10 % del valor mensual.

5 UF por cada incidente crítico y 2 UF por cada incidente alto que exceda el plazo.

1 % del valor del hito de paso a producción por cada semana de extensión, con tope de 10 %.

20 UF por vulnerabilidad y por cada semana de retraso en la remediación.

100 UF por evento, sin perjuicio de las responsabilidades legales.

50 UF por persona reemplazada.

10 UF por informe. 10% del valor total del Contrato, sin perjuicio de las acciones legales que correspondan.

Retención de pagos hasta su acreditación y multa de 20 UF por mes de incumplimiento.

- Notificación escrita y fundada del incumplimiento al ADJUDICATARIO.

. Plazo de cinco días hábiles para presentar descargos.

1 2 3. Resolución fundada del Administrador del Contrato dentro de los cinco días hábiles siguientes. 4

. Descuento del monto en el siguiente estado de pago o, en su defecto, cobra con cargo a la Garantía de

Fiel Cumplimiento.

Tope global. El total de multas aplicadas en un período de doce meses no podrá exceder el 15 % del valor del Contrato correspondiente a ese período. Superado dicho tope, el CLIENTE podrá poner término anticipado al

Contrato por incumplimiento grave.

## Capítulo 22 - TÉRMINO DEL CONTRATO

### Artículo 81. CAUSALES DE TÉRMINO

1, Ze 3

4,

Término normal por cumplimiento íntegro de las obligaciones de ambas partes.

Término anticipado por mutuo acuerdo, con acta de liquidación.

Término por incumplimiento grave del ADJUDICATARIO: atraso superior a 30 días corridos en un hito contractual; incumplimiento reiterado de los niveles de servicio en tres meses consecutivos; superación del tope global de multas; quiebra o insolvencia; pérdida de certificaciones esenciales; violación de confidencialidad; incidente de seguridad grave imputable a negligencia; no reconstitución de garantías.

Término por causas sobrevinientes: caso fortuito o fuerza mayor, acto de autoridad, o imposibilidad absoluta de cumplimiento.

### Artículo 82. PROCEDIMIENTO DE TÉRMINO Y REVERSIBILIDAD

Jl:

n-poOaNy

Notificación escrita con treinta días corridos de anticipación, salvo incumplimiento grave que ponga en riesgo la operación o la seguridad, caso en el cual el término podrá ser inmediato.

Acta de cierre con el estado de avance, los entregables recibidos y los pendientes. Activación del Plan de Reversibilidad del Artículo 77”, con acompañamiento mínimo de noventa días. Liquidación de pagos pendientes, compensación de multas y determinación de saldos.

Entrega íntegra de la documentación, del código fuente, de los datos en formatos abiertos y de las credenciales.

Devolución de las garantías que procedan, una vez verificado el cumplimiento de las obligaciones pendientes.

# VII. Disposiciones especiales

## Capítulo 23 - CONFIDENCIALIDAD, PROPIEDAD INTELECTUAL Y DATOS PERSONALES

### Artículo 83. CONFIDENCIALIDAD

Toda información del CLIENTE a la que el ADJUDICATARIO acceda con ocasión del proceso o del

Alcance , . . Contrato es confidencial, cualquiera sea su soporte. Vigencia Permanente, incluso después del término del Contrato. o Obliga al ADJUDICATARIO, a su personal, a sus subcontratistas, a sus asesores y a cualquier Extensión

tercero que intervenga.

Sólo información de dominio público por causa no imputable al ADJUDICATARIO, o cuya Excepciones divulgación sea exigida por ley o por resolución de autoridad competente, en cuyo caso deberá notificarse previamente al CLIENTE.

Acuerdo de confidencialidad suscrito por la empresa y por cada integrante del equipo clave,

Instrumentos e a e antes del inicio de la ejecución.

Multa del Artículo 80”, ejecución de la Garantía de Fiel Cumplimiento, término anticipado del

Sanciones A > Contrato y ejercicio de las acciones legales que correspondan.

### Artículo 84. PROPIEDAD INTELECTUAL, CÓDIGO FUENTE Y CUSTODIA

1. Todo desarrollo específico realizado para el PROYECTO, su código fuente, su documentación, sus modelos de datos, sus artefactos de configuración y sus scripts de infraestructura serán de propiedad exclusiva del CLIENTE desde su creación.

2. El ADJUDICATARIO cede al CLIENTE, de forma total, exclusiva, irrevocable y sin límite territorial ni temporal, todos los derechos patrimoniales de autor sobre dichos desarrollos.

3. Las licencias de software de terceros deberán constituirse a nombre del CLIENTE, transferibles y vigentes por todo el período contractual, con el costo de renovación explicitado en la Oferta Económica.

4. Cuando el ADJUDICATARIO incorpore componentes preexistentes de su propiedad, deberá declararlos e individualizarlos, y otorgar al CLIENTE una licencia perpetua, irrevocable y sin costo adicional para su uso, mantención y modificación en el ámbito del PROYECTO.

5. El uso de software de código abierto deberá declararse en el inventario de componentes, con su licencia y su compatibilidad con el.uso previsto. Queda prohibido el uso de componentes con licencias que impongan obligaciones de liberación incompatibles con los intereses del CLIENTE, sin autorización previa y escrita.

6. El código fuente deberá depositarse en el repositorio del CLIENTE, actualizado en cada liberación. Adicionalmente, el ADJUDICATARIO deberá constituir un depósito de custodia de fuentes ante un tercero independiente, con actualización semestral y cláusulas de liberación ante insolvencia o incumplimiento grave.

7. Se prohíbe al ADJUDICATARIO reutilizar los desarrollos específicos del PROYECTO para otros clientes sin autorización previa y escrita del CLIENTE.

8.

Los datos del CLIENTE, en todo momento y en cualquier estado de procesamiento, son de propiedad exclusiva del CLIENTE.

### Artículo 85. PROTECCIÓN DE DATOS PERSONALES

1,

El ADJUDICATARIO actúa como encargado del tratamiento por cuenta del CLIENTE y sólo podrá tratar datos personales conforme a las instrucciones documentadas de éste.

. Deberá suscribirse un acuerdo de tratamiento de datos que precise finalidad, categorías de datos,

categorías de titulares, plazo, medidas de seguridad y régimen de subencargados.

. El ADJUDICATARIO implementará medidas técnicas y organizativas apropiadas, incluyendo

seudonimización, cifrado, control de acceso por privilegio mínimo, registro de accesos y minimización de datos.

. Toda subcontratación que implique tratamiento de datos personales requiere autorización previa y

escrita del CLIENTE, y el subencargado quedará sujeto a las mismas obligaciones.

. El ADJUDICATARIO deberá asistir al CLIENTE en la atención de las solicitudes de ejercicio de derechos de

los titulares, dentro de los plazos legales.

. Toda brecha de datos personales deberá notificarse al CLIENTE dentro de las 24 horas siguientes a su

detección, con la información necesaria para que el CLIENTE cumpla sus obligaciones de notificación a la autoridad y a los titulares,

. Al término del Contrato, el ADJUDICATARIO deberá devolver o eliminar de forma segura y verificable

todos los datos personales, entregando certificado de eliminación.

. La transferencia internacional de datos personales requiere base de licitud, resguardos adecuados y

autorización previa y escrita del CLIENTE.

### Artículo 86. USO DE INTELIGENCIA ARTIFICIAL EN LA SOLUCIÓN

86.1 Cuando la solución incorpore componentes de inteligencia artificial, el ADJUDICATARIO deberá:

.

Declarar el modelo o servicio utilizado, su proveedor, su versión y su ubicación de procesamiento.

Garantizar que los datos del CLIENTE no serán utilizados para entrenar modelos de terceros, salvo autorización expresa y escrita.

Documentar el propósito, los límites de uso, los casos en que el resultado requiere validación humana y el procedimiento de supervisión.

Evaluar y mitigar los riesgos de sesgo, alucinación, fuga de información y uso indebido, conforme al NIST Al Risk Management Framework y a la norma ISO/IEC 42001.

Registrar las interacciones relevantes para efectos de auditoría y trazabilidad.

Proveer un mecanismo de desactivación del componente sin comprometer la operación del resto de la solución.

86.2 La responsabilidad por los resultados de los componentes de inteligencia artificial incorporados a la solución recae integramente en el ADJUDICATARIO.

## Capítulo 24 - SOLUCIÓN DE CONTROVERSIAS

### Artículo 87. MECANISMOS DE RESOLUCIÓN

1. Primera instancia: negociación directa entre las partes, con plazo de treinta días corridos, escalada al Comité Ejecutivo.

2. Segunda instancia: mediación ante el Centro de Arbitraje y Mediación de Santiago, con plazo de treinta días corridos.

3. Tercera instancia: arbitraje de derecho, con árbitro único designado conforme al reglamento del Centro de Arbitraje y Mediación de Santiago, cuyo fallo será obligatorio para ambas partes.

La existencia de una controversia no suspende las obligaciones de ejecución, de continuidad del servicio ni de pago de las prestaciones no controvertidas.

Artículo 88. DOMICILIO Y JURISDICCIÓN + Domicilio: ciudad de Valparaíso, República de Chile. e Legislación aplicable: chilena.

+ Tribunales competentes: ordinarios de Valparaíso, en subsidio del arbitraje pactado. CAPÍTULO 25 - GESTIÓN DEL CAMBIO, CAPACITACIÓN Y DOCUMENTACIÓN

### Artículo 89. GESTIÓN DEL CAMBIO ORGANIZACIONAL

El ADJUDICATARIO deberá presentar y ejecutar un plan de gestión del cambio que contemple:

* Diagnóstico del impacto organizacional del PROYECTO, por área y por perfil. e Estrategia de comunicación a los distintos grupos de interés, con calendario y canales. e Identificación y habilitación de agentes de cambio dentro de la organización del CLIENTE.

+ Identificación anticipada de las resistencias previsibles y estrategias específicas de mitigación, incluidas las que provengan de usuarios expertos apegados a los procedimientos vigentes.

+ Rediseño y documentación de los procedimientos operativos afectados.

+ Medición de la adopción con indicadores objetivos: cobertura de usuarios activos, tasa de uso por función, abandono de los mecanismos manuales previos y satisfacción de las personas usuarias.

e Plan de acción correctiva cuando los indicadores de adopción no alcancen las metas comprometidas.

### Artículo 90. CAPACITACIÓN

90.1 Plan de capacitación integral, dirigido a usuarios finales, usuarios avanzados, administradores, equipo técnico y soporte de niveles 1 y 2.

90.2 Modalidades exigidas: presencial en cada sitio de operación, en línea sincrónica, autoformación en línea

y acompañamiento en puesto de trabajo durante la marcha blanca.

90.3 Materiales exigidos: manuales por perfil, guías rápidas, preguntas frecuentes, videos tutoriales en español y base de conocimiento consultable, todos entregados en formato editable y de propiedad del CLIENTE.

90.4 Certificación: el plan deberá contemplar la evaluación y certificación de los usuarios administradores y del equipo técnico del CLIENTE, como condición para el cierre de cada marcha blanca.

90.5 Refuerzo: durante la fase de Operación, el ADJUDICATARIO deberá ejecutar al menos dos jornadas anuales de actualización y capacitar al personal nuevo del CLIENTE, sin costo adicional.

### Artículo 91. DOCUMENTACIÓN EXIGIBLE

La documentación es un entregable contractual y su ausencia o desactualización impide la aceptación del hito correspondiente. Se exige, como mínimo:

Documento de arquitectura conforme a ISO/IEC/IEEE 42010; registro de decisiones de

Arquitectura 2 em ; SE A 9 arquitectura; diagramas lógico, físico, de datos, de integración y de seguridad.

Catálogo de requerimientos funcionales y no funcionales, matriz de trazabilidad y línea base de

Requerimientos o alcance versionada.

Estándares de codificación, documentación de interfaces (OpenAPI y AsyncAPI), diccionario de

Construcción datos e inventario de componentes (SBOM).

Plan y casos de prueba, evidencia de ejecución, informes de pruebas de carga, de resiliencia y

Pruebas de seguridad. al o Manual de operación, libros de operación, guías de resolución, matriz de escalamiento, plan de jeración 4, $ A úl continuidad y plan de recuperación ante desastres. s idad Política de seguridad de la solución, modelado de amenazas, matriz de controles, informes de egurida, A En Ey a pruebas de intrusión y plan de remediación. Usuario Manuales por perfil, guías rápidas, material de capacitación y base de conocimiento. p a Plan de proyecto, EDT, cronograma, nivelación de recursos, registro de riesgos, registro de royecto

cambios y actas de todos los comités.

## Capítulo 26 - DISPOSICIONES FINALES

### Artículo 92. RELACIÓN CON LAS BASES TÉCNICAS DELCASO

92.1 Las presentes Bases Administrativas son comunes a todos los casos e industrias del llamado. Las Bases Técnicas de cada caso desarrollan el contexto de la industria, el proceso de negocio, los requerimientos funcionales y no funcionales específicos, los volúmenes, las integraciones, los datos y los criterios de aceptación propios de ese caso.

92.2 Cuando las Bases Técnicas establezcan una exigencia superior a la de estas Bases Administrativas, prevalecerá la más exigente. Cuando establezcan una exigencia inferior, se entenderá que rige la de estas Bases Administrativas.

92.3 Ninguna disposición de las Bases Técnicas podrá interpretarse como una dispensa del cronograma contractual obligatorio del Artículo 17”, del modelo híbrido del Artículo 16”, de los requisitos transversales del Capítulo 4 ni de la exigencia de innovación del Capítulo 5.

### Artículo 93. CARÁCTER ACADÉMICO DEL PROCESO

93.1 El presente proceso constituye una simulación con fines formativos, desarrollada en el marco de la asignatura Taller de Formulación de Proyectos Informáticos (ICI-5444) de la Escuela de Informática de la

93.2 Las garantías, montos, obligaciones contractuales y penalidades descritas en estas Bases son elementos del ejercicio y no generan obligaciones jurídicas reales entre las partes. Su rigor es deliberado: reproducen las condiciones a las que se enfrenta una empresa proveedora en un proceso de licitación real.

93.3 Las consecuencias efectivas del incumplimiento de estas Bases son académicas y se expresan en la evaluación conforme al Capítulo 17.

### Artículo 94. VIGENCIA Y ACEPTACIÓN

94.1 Estas Bases rigen desde su publicación y hasta el término del proceso de adjudicación.

94.2 La sola presentación de una oferta implica la aceptación íntegra e incondicional de estas Bases, de las Bases Técnicas del caso, de sus anexos y de las aclaraciones y modificaciones emitidas por el CLIENTE, sin reserva alguna.

ANEXOS Y FORMULARIOS

CAPÍTULO A - FORMULARIOS ADMINISTRATIVOS

Los formularios de este anexo integran el Sobre N? 1. Todos deberán presentarse firmados por el representante legal y, cuando se indique, ante notario.

A-1 Identificación del Proponente y del Representante.

A-2 Declaración jurada de no afectación por prohibiciones e inhabilidades. A-3 Declaración de aceptación íntegra de las Bases.

A-4 Declaración de ausencia de conflictos de interés.

A-5 Presentación e índice de antecedentes.

A-6 Declaración de uso de herramientas de inteligencia artificial generativa.

#### Formulario A-1

IDENTIFICACIÓN DEL PROPONENTE

Razón social

Nombre de fantasía

Rol Único Tributario

Domicilio comercial

Ciudad y región

Giro

Sitio web

Caso e industria asignada

Representante legal

Cédula de identidad

Correo electrónico

Teléfono de contacto

Representante del proceso (contraparte) Correo del representante del proceso Teléfono del representante del proceso Tipo de participación Individual / Consorcio / Unión temporal (marcar)

Integrantes y porcentaje (si aplica)

RS O NN

#### Formulario A-2

DECLARACIÓN JURADA DE NO AFECTACIÓN POR PROHIBICIONES E INHABILIDADES

El suscrito, en su calidad de representante legal de la empresa individualizada en el Formulario A-1, declara bajo juramento que su representada:

1. No se encuentra afecta a ninguna de las situaciones descritas en el Artículo 4” de la Ley N° 19.886 ni en el Artículo 32” de las Bases Administrativas.

2. No tiene vigente declaratoria de quiebra, liquidación concursal ni procedimiento de reorganización judicial.

3. No registra incumplimientos contractuales graves con el CLIENTE en los últimos tres años.

4. No mantiene litigios pendientes con el CLIENTE.

5. No ha sido sancionada por infracciones laborales, previsionales o tributarias graves en los últimos dos años.

6. No ha sido condenada conforme a la Ley N” 20.393 ni a la Ley N° 21.595 por delitos que afecten la probidad.

7. Toda la información contenida en su propuesta corresponde a la realidad y es verificable.

IO MÍN: cirorarnocuzncan inconciente dont tilta icon ta atado

AAA FOCHA: conncnnioninnacinness

#### Formulario A-3

DECLARACIÓN DE ACEPTACIÓN ÍNTEGRA DE LAS BASES

El suscrito, en representación de la empresa individualizada en el Formulario A-1, declara que: 1. Ha estudiado íntegramente las Bases Administrativas, las Bases Técnicas del caso asignado, sus anexos, formularios, aclaraciones y modificaciones.

2. Acepta sin reserva, condicionamiento ni contrapropuesta la totalidad de sus disposiciones, incluido el cronograma contractual obligatorio del Artículo 17? y el modelo de despliegue híbrido del Artículo 16”.

3. Ha considerado en su oferta la totalidad de los costos, riesgos y obligaciones que se derivan de las Bases, y no formulará reclamo alguno fundado en su desconocimiento.

4. Constituye domicilio en la ciudad de Valparaíso para todos los efectos del proceso y del Contrato.

5. Mantendrá vigente su oferta por el plazo mínimo de ciento cincuenta días corridos contados desde su presentación.

NOMBRE: iscisorisicianananina roster rico

Firma: Fecha:

#### Formulario A-4

DECLARACIÓN DE AUSENCIA DE CONFLICTOS DE INTERÉS

El suscrito declara que ni la empresa que representa, ni sus socios, directores, administradores o integrantes del equipo propuesto, mantienen vínculo de propiedad, parentesco, dependencia, sociedad o interés económico con los integrantes de la Comisión Evaluadora, de la Comisión de Expertos o de la contraparte del

CLIENTE, salvo las situaciones que a continuación se declaran expresamente:

rsona Vínculo declarado Con quién

Declara asimismo conocer que la omisión de un vínculo existente constituye causal de exclusión del proceso.

NoOMbTE cra

#### Formulario A-5

PRESENTACIÓN E ÍNDICE DE ANTECEDENTES

El Proponente deberá completar el índice de la totalidad de los documentos incluidos en el Sobre N” 1, indicando el folio de inicio de cada sección. La correspondencia entre este índice y la foliación efectiva es requisito excluyente.

. Folio % ocu (o) Fol io NR Observación término 1

10 all

Hz

#### Formulario A-6

DECLARACIÓN DE USO DE INTELIGENCIA ARTIFICIAL GENERATIVA

Conforme al Artículo 13.5 de las Bases Administrativas, el Proponente declara el uso de herramientas de inteligencia artificial generativa en la preparación de su propuesta:

56 q AREA Revisión humana Sección de la propuesta Herramienta utilizada Finalidad del uso A aplicada

El Proponente declara que asume la responsabilidad íntegra sobre el contenido, la exactitud, la originalidad y la coherencia técnica de su propuesta, con independencia de las herramientas empleadas en su preparación, y que no ha incorporado datos confidenciales del CLIENTE en servicios de terceros sin autorización.

NOMDIOS coccocccnccncon conc

A AN

CAPÍTULO B - FORMULARIOS TÉCNICOS

Los formularios de este anexo integran el Sobre N” 2. Ninguno de ellos podrá contener información de precios.

T-6

T-7

T-8

T-9

T-10 T-11 T-12 1-13 T-14 T-15 T-16 17: T-18 T-19 T-20 T-21

T-22

Experiencia en proyectos similares.

Contenido y estructura de la Propuesta Técnica.

Equipo de trabajo, subcontrataciones y alianzas. Metodología para la administración y gestión del proyecto. Metodología para el desarrollo.

Especificaciones técnicas ofertadas.

Matriz de cumplimiento técnico y trazabilidad de requerimientos. Plan de pruebas y validación.

Plan de trabajo, EDT y carta Gantt.

Nivelación de recursos.

Plan de riesgos.

Protocolo de aceptación.

Propuesta de implantación y puesta en marcha controlada. Cartera de innovaciones.

Calendario de actividades.

Ponderación de la evaluación técnica.

Contenido de los informes y presentaciones preparatorias.

#### Formulario T-6

EXPERIENCIA EN PROYECTOS SIMILARES

Licitación N° TFEP-01/2026

Se deberán declarar al menos tres proyectos finalizados y en operación en los últimos cinco años. El CLIENTE

verificará directamente con las contrapartes declaradas.

Nombre del proyecto Cliente / mandante Industria

Año de inicio y de término Monto del contrato (rango) Alcance ejecutado

Arquitectura (nube / on- premise / híbrida)

Nivel de servicio comprometido

Volumen de operación soportado

Rol de la empresa (principal / socio)

Contraparte de referencia y contacto

#### Formulario T-7 — CONTENIDO Y ESTRUCTURA DE LA PROPUESTA TÉCNICA

La Propuesta Técnica deberá estructurarse en catorce subdocumentos, en el orden que se indica. Cada subdocumento constituye un ítem de evaluación con la ponderación del Formulario T-21.

SUBDOCUMENTO 1 — Presentación de la empresa + Reseña de la trayectoria, capacidades instaladas, líneas de negocio, productos y servicios ofrecidos. e Estructura organizacional, dotación, certificaciones institucionales y alianzas tecnológicas vigentes. + Experiencia relevante en la industria del caso y en proyectos de complejidad equivalente.

+ Modelo de gobierno interno de calidad, seguridad y gestión del conocimiento.

SUBDOCUMENTO 2 — Comprensión del problema y de la necesidad

* Dimensionamiento realista de la magnitud del problema o desafío, con foco cualitativo y con datos cuantitativos que lo sustenten.

+ Comprensión del contexto de la industria, de sus particularidades operacionales, regulatorias y estacionales.

- Identificación de los actores afectados y de los grupos de interés, con su nivel de influencia e interés.
- Supuestos declarados y su fundamento. No mezclar el problema con la solución.

e Información de apoyo adecuadamente referenciada en norma APA 7.2 edición.

SUBDOCUMENTO 3 — Esquema de solución y alcance

+ Descripción de la solución propuesta y su coherencia con el problema definido.

Alcance de la Etapa 1 y de la Etapa 2, con separación explícita y criterios de asignación entre ambas.

Exclusiones explícitas, supuestos y restricciones del alcance.

Catálogo de requerimientos funcionales y no funcionales, priorizado y trazable.

e Estrategia para obtener el apoyo de los grupos de interés clave.

Criterios de aceptación del alcance comprometido.

SUBDOCUMENTO 4 — Arquitectura lógica y física de la solución + Arquitectura lógica: capas, módulos, límites de contexto, responsabilidades e interfaces.

+ Arquitectura física: emplazamiento de cada componente en nube y on-premise, con justificación por componente conforme al Artículo 16”.

+ Arquitectura de integración: servicios, contratos, mensajería, versionado y gobierno. e Arquitectura de seguridad: modelo Zero Trust, capa expuesta, identidad, cifrado y controles.

+ Arquitectura de despliegue: ambientes, redes, alta disponibilidad, recuperación ante desastres y respaldos.

- Dimensionamiento y plan de capacidad, con supuestos de volumen, concurrencia y crecimiento.
- Decisiones de arquitectura registradas, con alternativas evaluadas y criterio de selección.

e La arquitectura debe ser propia de la solución planteada. No se aceptarán diagramas genéricos.

SUBDOCUMENTO 5 — Modelo y gestión de datos

+ Dominio de información.

Selección del motor y del paradigma de persistencia, con justificación: relacional o no relacional, transaccionalidad, consistencia y disponibilidad conforme al teorema CAP.

.

Estrategia de migración, saneamiento, validación y conciliación de los datos históricos.

.

Estrategia de desempeño: indexación, particionamiento, caché y optimización de consultas.

+ Separación entre almacenamiento transaccional y analítico, y modelo de explotación de información.

Calidad de datos, retención, archivado y eliminación segura.

SUBDOCUMENTO 6 — Metodologías

+ Metodología de gestión del proyecto: aplicación del PMBOK adaptada a la complejidad del PROYECTO, integrando enfoques ágiles donde corresponda. Gestión de interesados, comunicaciones, adquisiciones e integración.

+ Metodología de desarrollo: enfoque coherente con la naturaleza del proyecto, con sus implicancias en gestión de requerimientos, arquitectura evolutiva, refactorización, deuda técnica y tiempo de salida al mercado.

e Prácticas de DevSecOps, integración y entrega continuas, infraestructura como código y automatización de pruebas.

+ Ceremonias, artefactos, cadencias y mecanismos de decisión.

SUBDOCUMENTO 7 — Plan de trabajo, EDT, cronograma e implantación

+ Estructura de descomposición del trabajo con el 100 % del alcance, hasta paquetes de trabajo estimables y asignables.

e Diccionario de la EDT con entregable, criterio de aceptación y responsable por paquete. + Secuenciamiento, estimación, ruta crítica identificada y gestión de holguras, con técnicas PERT y CPM.

+ Carta Gantt alineada con el cronograma contractual obligatorio del Artículo 17”, con los hitos del Formulario E-25.

+ Frentes de trabajo, paralelización y sincronización, incluido el solapamiento de los meses 13 a15 y 19 a 20.

e Plan de implantación y puesta en marcha: estrategia de despliegue (azul-verde, canario o progresivo), pruebas de aceptación, pruebas de desempeño y de estrés, criterios de éxito medibles y procedimiento de reversión.

* Plan de marcha blanca de la Etapa 1 y de la Etapa 2, con indicadores de cierre conforme al Artículo 17.3.

SUBDOCUMENTO 8 — Plan de riesgos

* Identificación y cuantificación de riesgos técnicos, organizacionales, de proyecto, de seguridad y de operación.

e Análisis cualitativo y cuantitativo, con técnicas de análisis de modos de falla, árbol de fallas o simulación. e Estrategias de mitigación basadas en análisis costo-beneficio, con responsable, plazo y disparador.

e Riesgos de obsolescencia tecnológica, bloqueo por proveedor, escalabilidad, ciberseguridad y disponibilidad de contrapartes del CLIENTE.

+ Reservas de contingencia y de gestión, y su reflejo en el cronograma y en el flujo de caja.

e Los riesgos deben corresponder a la solución efectivamente propuesta y no a un catálogo genérico.

SUBDOCUMENTO 9 — Plan de calidad

* Marco de aseguramiento de calidad basado en ISO/IEC 25010 y en modelos de madurez.

+ Métricas de calidad del código, cobertura de pruebas, complejidad y acoplamiento, con umbrales bloqueantes.

+ Puertas de calidad, revisiones por pares, análisis estático y dinámico.

e Estrategia de pruebas conforme a ISO/IEC/IEEE 29119: niveles, tipos, ambientes, datos de prueba y automatización.

e Verificación, validación y trazabilidad entre requerimiento, diseño, código, prueba y despliegue.

SUBDOCUMENTO 10 — Servicios de operación y niveles de servicio + Modelo de soporte basado en ITIL 4, con estructura de niveles, canales, horarios y escalamiento. + Definición de indicadores, objetivos y acuerdos de nivel de servicio, coherentes con el Artículo 78”. + Dimensionamiento de la mesa de servicio con fundamento cuantitativo (teoría de colas, modelo Erlang C u otro declarado). + Acuerdos de nivel operacional y contratos de apoyo internos coherentes con los compromisos externos. e Libros de operación, guías de resolución, gestión del conocimiento y automatización progresiva.

+ Observabilidad de extremo a extremo, correlación de eventos y detección proactiva.

SUBDOCUMENTO 11 — Planes en operación

+ Plan de mantención preventiva, correctiva y evolutiva, con criterios de priorización y presupuesto de capacidad.

Estrategia de actualización de dependencias, gestión de deuda técnica y ventana de obsolescencia.

.

Plan de operación conforme a principios de ingeniería de confiabilidad: presupuesto de error, reducción del trabajo manual y análisis retrospectivo sin culpa.

Gestión de la capacidad y optimización de costos en nube conforme a prácticas FinOps.

.

Plan de pruebas periódicas de recuperación ante desastres y de resiliencia.

SUBDOCUMENTO 12 — Equipo de trabajo, subcontrataciones y alianzas e Estructura organizacional del proyecto, con roles, responsabilidades y matriz de asignación.

+ Equipo clave nominado, con currículo, certificaciones, dedicación y período de participación.

Curva de dotación por fase, coherente con la nivelación de recursos del Formulario T-15.

Decisiones de hacer o comprar, con justificación por capacidades, certificaciones y trayectoria.

.

Subcontratistas y socios, su rol, su porcentaje de participación y su régimen de control.

Estrategia de gestión del conocimiento, retención de talento y continuidad ante rotación.

SUBDOCUMIENTO 13 — Innovaciones

+ Cartera obligatoria de cinco innovaciones, una por cada tipo del Artículo 28”, presentada en el Formulario T-19.

* Cada innovación con los siete elementos del Artículo 29”: problema, tecnología, madurez, diseño de incorporación, impacto económico, indicador de verificación y riesgo de adopción.

e Trazabilidad de cada innovación con la arquitectura, con la EDT y con el flujo de caja.

+ Fuentes citadas en norma APA 7.2 edición para las innovaciones de base tecnológica.

SUBDOCUMENTO 14 — Ventajas, beneficios y consolidación

+ Síntesis de la propuesta de valor desde una perspectiva de ingeniería integral.

e Análisis cuantitativo de beneficios para el CLIENTE: mejoras de desempeño, reducción del tiempo de restauración, aumento de disponibilidad y ahorro operacional.

+ Demostración de cómo la solución equilibra alcance, tiempo, costo y calidad. + Coherencia arquitectónica y tecnológica entre todas las secciones de la propuesta. e Trazabilidad de extremo a extremo: requerimiento, diseño, construcción, prueba, implantación y operación. Consideraciones transversales de evaluación

+ Consistencia técnica: todas las secciones deben mantener coherencia arquitectónica y tecnológica.

.

Trazabilidad: mapeo explícito entre requerimientos, diseño, implementación y operación.

.

Fundamentación ingenieril: decisiones respaldadas por análisis cuantitativo, modelos y mejores prácticas.

+ Cumplimiento: consideración de los aspectos regulatorios, de los estándares del Artículo 4.3 y de los marcos de gobierno de tecnologías de información.

#### Formulario T-8 — EQUIPO DE TRABAJO, SUBCONTRATACIONES Y ALIANZAS

Certificaciones

Jefe de Proyecto Arquitecto de Solución

Encargado de Seguridad de la Información

Líder de Datos

Líder de Desarrollo Líder de Calidad

Líder de Operación / SRE

Líder de Implantación y Gestión del Cambio

Otros roles (agregar filas)

Subcontrataciones y alianzas:

Licitación N° TFEP-01/2026

A Meses de Dedicación ST participación

100 %

#### Formulario T-9

METODOLOGÍA PARA LA ADMINISTRACIÓN Y GESTIÓN DEL PROYECTO

El Proponente adjuntará a este formulario la información solicitada en el Subdocumento 6, letra a.

#### Formulario T-10 — METODOLOGÍA PARA EL DESARROLLO

El Proponente adjuntará a este formulario la información solicitada en el Subdocumento 6, letra b.

#### Formulario T-11 — ESPECIFICACIONES TÉCNICAS OFERTADAS

Detalle de los componentes de infraestructura, plataforma, licenciamiento y hardware especificado, con su ubicación / lugar y su justificación.

#### Formulario T-12 — MATRIZ DE CUMPLIMIENTO TÉCNICO Y TRAZABILIDAD

El Proponente deberá declarar el cumplimiento de cada requerimiento de las Bases Técnicas del caso y de los

requisitos transversales del Capítulo 3, indicando dónde se acredita en la propuesta.

A ez Componente que lo AE 1D requerimiento | Descripción Cumple Ñ satisface propuesta

#### Formulario T-13

PLAN DE PRUEBAS Y VALIDACIÓN

El Proponente adjuntará a este formulario el plan de pruebas conforme al Subdocumento 9, incluyendo niveles, tipos, ambientes, datos de prueba, criterios de entrada y salida, automatización y el calendario de las pruebas de carga, de resiliencia, de recuperación ante desastres y de seguridad ofensiva.

#### Formulario T-14 — PLAN DE TRABAJO, EDT Y CARTA GANTT

El Proponente adjuntará a este formulario la información solicitada en el Subdocumento 7. La carta Gantt deberá cubrir los 56 meses del Contrato y mostrar explícitamente las ventanas de marcha blanca, los pasos a producción y el inicio de la fase de Operación.

#### Formulario T-15 — NIVELACIÓN DE RECURSOS El Proponente deberá indicar claramente la siguiente información de planificación, a modo de resumen: e Horas hombre destinadas a cada una de las tareas, paquetes de trabajo y etapas de la implementación.

e Curva de horas hombre programadas para la implementación, por etapa y para el total del proyecto, y en forma separada la curva de la etapa de continuidad operacional.

+ Número de personas involucradas en las distintas actividades durante la implementación y durante la operación.

+ Identificación de la ruta crítica de la implementación y de sus holguras.

+ Cantidad de frentes de trabajo empleados en la ejecución del programa, con especial detalle del período de solapamiento de los meses 13 a 15 y 19 a 20.

Etapa 1 — Desarrollo

Etapa 1 — Marcha blanca 1315 Etapa 2 — Desarrollo 13-18 Etapa 2 — Marcha blanca 19-20 Operación 21-56

#### Formulario T-16 — PLAN DE RIESGOS

po ea a in e L

#### Formulario T-17 — PROTOCOLO DE ACEPTACIÓN

El Proponente adjuntará a este formulario la propuesta de Protocolo de Aceptación de cada hito y del producto final, indicando entregables, criterios de aceptación objetivos, evidencia requerida, plazos de revisión, procedimiento de observaciones y acta de conformidad.

#### Formulario T-18

PROPUESTA DE IMPLANTACIÓN Y PUESTA EN MARCHA CONTROLADA

El Proponente adjuntará a este formulario la propuesta de implantación y puesta en marcha controlada que asegure el éxito del paso a producción, cubriendo por separado la Etapa 1 (marcha blanca de los meses 13 a 15 y producción desde el mes 16) y la Etapa 2 (marcha blanca de los meses 19 y 20 y producción desde el mes 21), con el plan de convivencia entre ambas y el procedimiento de reversión.

#### Formulario T-19 — CARTERA DE INNOVACIONES

Una ficha por cada una de las cinco innovaciones obligatorias del Artículo 28”.

Tipo de innovación (1 a 5)

Nombre de la innovación

Problema u oportunidad del caso que resuelve Tecnología, práctica o modelo que la sustenta Nivel de madurez y escala utilizada

Fuentes citadas (APA 7.2 ed.)

Dónde se inserta en la arquitectura

Paquetes de la EDT que la ejecutan

Mes del cronograma en que se materializa Inversión requerida

Efecto en el costo operacional

Beneficio esperado y su cuantificación Indicador de verificación, línea base y meta Momento de medición

Riesgo de adopción, probabilidad e impacto Estrategia de mitigación

Plan de contingencia si no rinde lo esperado

#### Formulario T-20 — CALENDARIO DE ACTIVIDADES

Las fechas podrán ser ajustadas por el CLIENTE conforme al Artículo 10? de las Bases Administrativas.

il Registro de participantes 14-08-2026 17-08-2026 2 Publicación de las Bases Administrativas 19-08-2026 19-08-2026 3 da de las Bases Técnicas y entrega del caso a cada 19-08-2026 19-08-2026 4 Período de consultas abiertas 20-08-2026 01-09-2026 5 Publicación del Acta de Respuestas a Consultas 07-09-2026 07-09-2026 6 Entrega del Informe 1 07-09-2026 07-09-2026 7 Presentación preparatoria 1 14-09-2026 25-09-2026 8 Entrega del Informe 2 05-10-2026 05-10-2026 9 Presentación preparatoria 2 19-10-2026 02-11-2026 10 Entrega del Informe 3 13-11-2026 13-11-2026 E Presentación preparatoria 3 13-11-2026 20-11-2026

Entrega de propuestas en sobres cerrados (máximo 14:00 h). 12 | Incluye antecedentes administrativos, garantías, Oferta Técnica 25-11-2026 25-11-2026 y Oferta Económica.

13 | Presentación de propuestas ante empresas evaluadoras 27-11-2026 27-11-2026

14 | Entrega de resultados Licitación 01-12-2026 01-12-2026

#### Formulario T-21 — PONDERACIÓN DE LA EVALUACIÓN TÉCNICA

Cada subdocumento del Formulario T-7 se evalúa de O a 100 puntos conforme al Artículo 56” y pondera según la siguiente tabla. En cada subdocumento que requiere un formulario, el documento debe contener un resumen y análisis, el detalle o listado respectivo debe ser complementado en los respectivos formularios.

Formalidad y contenido del documento / Cumplimiento de Instrucciones

Transversal 4% 3% 2%

Presentación de la empresa 4 ; il 4% 3% 1% Formulario T-6

(2: Resumen Ejecutivo, comprensión del problema y de la necesidad 11% 6% 4%

Esquema de solución y alcance

y Ñ 3 Formulario 12 21% 12% 10%

4 Arquitectura lógica y física de la solución

Arquitectura lógica 4.1 a) Esquema Solución 16% 7% 5% b) Arquitectura Lógica de la Solución

Arquitectura física a) Arquitectura Física de la Solución b) Especificaciones Tecnologías de Software a utilizar 4.2 c) Especificaciones Implementos a proveer (Hardware y Software) 16% 12% 10% d) Especificaciones Data Center Primaria e) Especificaciones Data Center Secundario Formulario T-11

5 Modelo y gestión de datos 11% 6% 5%

Metodologías

Metodología de Gestión de Proyectos

Formulario T-9 8% 6% b) Metodología de Desarrollo Software

Formulario T-10

E)

Plan de trabajo, EDT, cronograma e implantación F io T-14 ormu año 15% 12% Formulario T-15 F

ormulario T-18

Plan de riesgos

109 A, Formulario T-16 Ye 2

Plan de calidad 9 Formulario T-13 8% 6% Formulario T-17

10 Servicios de operación y niveles de servicio 8%

Planes en operación a a) Plan Mantención Preventiva / Evolutiva 6% b) Plan Servicios de Operación

Equipo de trabajo, subcontrataciones y alianzas

12 5%

Formulario T-8

13 Innovaciones 17% 10% 8% Formulario T-19 o o >

14 Ventajas, beneficios y consolidación 3%

TOTAL Puntaje técnico ponderado 100 % 100 % 100 %

#### Formulario T-22 — CONTENIDO DE LOS INFORMES Y PRESENTACIONES PREPARATORIAS

Con el objeto de asegurar que el proceso sea exitoso y que las propuestas cumplan los objetivos definidos por el CLIENTE, se realizarán tres presentaciones previas de validación. Tienen carácter obligatorio: la no presentación implica quedar fuera del proceso de adjudicación. En cada instancia sólo se abordarán los temas definidos en la agenda.

Informe y presentación 1

+ Presentación de la empresa: reseña de la trayectoria y de las principales capacidades; actividad a la que se dedica y productos o servicios que ofrece.

+ Presentación del problema y de la necesidad: dimensionamiento realista de la magnitud del desafío, comprensión del contexto y de sus particularidades con foco cualitativo, claridad del planteamiento e identificación correcta de los actores afectados. Debe explicar el tamaño del problema, los supuestos del análisis y aportar datos cuantitativos. No mezclar con la solución. La información de apoyo debe estar referenciada.

+ Presentación del esquema de solución y del alcance: coherencia entre el problema definido y la solución planteada; estrategia de la solución y forma de obtener el apoyo de los involucrados clave.

e Presentación de la arquitectura lógica y física: distinta de la explicación del alcance o del diagrama de solución. Debe tener suficiente detalle para entender cada módulo y cada capa, y ser propia de la solución planteada; no se acepta un diagrama genérico. Debe evidenciar el carácter híbrido exigido en el Artículo 16”.

e Presentación de la cartera de cinco innovaciones: cada una desarrollada en su idea, tecnología, alcance, forma de implementación y resultados esperados. Si alguna requiere investigación adicional, debe declararse; en ningún caso puede presentarse sólo el título de la innovación.

De la Propuesta Técnica corresponde a los subdocumentos: 1, 2, 3, 4, 5 y 13.

Informe y presentación 2 + Correcciones del Informe 1, con tabla de trazabilidad observación—respuesta—-sección modificada. e Análisis de riesgo de la solución. + Análisis de riesgo del desarrollo del proyecto. e Análisis de riesgo de implantación.

+ EDT del proyecto y equipo de trabajo: el equipo debe ser coherente con las actividades en términos concretos de la propuesta.

e Planificación e hitos del proyecto, alineados con el cronograma contractual obligatorio del Artículo 17”. Se evaluará con severidad todo plan de trabajo con actividades genéricas que podrían servir para cualquier proyecto, o incoherente con los objetivos declarados.

De la Propuesta Técnica corresponde a los subdocumentos: 1, 2, 3, 4, 5, 6, 7, 8, 9 y 13.

Informe y presentación 3

+ Proveedores clave de la solución.

+ Adquisiciones clave o relevantes de la solución.

+ Curva S del proyecto.

e Análisis de costos de la solución. Se evaluará con severidad todo presupuesto sobreestimado o subestimado; los ítems presupuestados deben estar justificados y ser coherentes con el plan de actividades.

+ VAN yTIR de la solución.

e Valorización de las cinco innovaciones en el flujo de caja: inversión, costo operacional y beneficio esperado.

Se deberá completar la planilla de cálculo que entregará el CLIENTE con la información económica del

proyecto, desglosada en gastos de operación, gastos de inversión, gastos administrativos y gastos de recursos

humanos. Los gastos asociados a proveedores deben explicitarse en una hoja y sumarse al gasto de operación. Debe incluirse además un flujo de caja mensual con total del mes y monto acumulado.

De la Propuesta Económica corresponde a: el documento de costos frente a venta y la planilla de cálculo.

CAPÍTULO C - FORMULARIOS ECONÓMICOS

Los formularios de este anexo integran el Sobre N? 3,

E-21 Estructura de la propuesta económica.

E-24 Condiciones y parámetros para la preparación de la oferta económica. E-25 Hitos de pago.

E-26 Rango de valores aceptados para perfiles profesionales.

#### Formulario E-21 — ESTRUCTURA DE LA PROPUESTA ECONÓMICA

ADVERTENCIA:

El cumplimiento estricto de estas instrucciones es obligatorio. Cualquier desviación, omisión o error en

el formato, la estructura o el contenido solicitado resultará en la descalificación automática del proceso de licitación.

La Oferta Económica debe entregarse de forma separada e independiente de la Oferta Técnica, en la fecha y hora exactas del Formulario T-20.

La Oferta Económica comprende tres entregables obligatorios que deben presentarse simultáneamente.

Entregable 1 — Propuesta económica formal

Documento ejecutivo con la propuesta comercial definitiva.

1.1 Propuesta de valor económico. Valores totales del proyecto, expresados obligatoriamente en CLP, UF y USD:

+ Valor total de la fase de implementación (Etapa 1 y Etapa 2).

Valor total de la fase de Operación por los.36 meses.

.

Valor total del proyecto, suma de los dos anteriores.

Tipo de cambio referencial utilizado y su fecha de referencia.

Cláusulas de reajustabilidad aplicables.

+ Vigencia de la oferta. 1.2 Estructura de pagos detallada.

+ Hitos de pago de la fase de implementación conforme al Formulario E-25: identificación de cada hito facturable, porcentaje y monto, entregables que gatillan el pago y criterios de aceptación vinculados.

+ Estructura de pagos mensuales de la fase de Operación: servicios incluidos, componentes fijos y variables, métricas que afectan los pagos variables y periodicidad de facturación.

1.3 Resumen ejecutivo de valor.

Matriz de servicios y productos incluidos. Exclusiones explícitas.

Supuestos y dependencias comerciales. Beneficios económicos para el CLIENTE.

Términos y condiciones comerciales relevantes.

Entregable 2 — Análisis económico-financiero

Documento técnico con el modelo de negocio y la justificación económica.

2.1 Análisis comparativo de costos frente a precio: cuadro maestro de costos (directos de implementación, directos de operación, indirectos y overhead, por categoría) y cuadro de precio de venta con los márgenes aplicados por componente, todo en CLP, UF y USD.

2.2 Evaluación financiera: VAN con la tasa de descuento utilizada y su justificación, flujo de caja proyectado completo, TIR, análisis de sensibilidad y punto de equilibrio.

2.3 Curva S: costos acumulados, ingresos acumulados y análisis de flujo de caja mensual.

2.4 Estrategia de adquisiciones: matriz de adquisiciones principales, cronograma de compras alineado con el plan de proyecto, estrategia de negociación, contratos críticos, plan de importaciones si aplica y análisis de hacer o comprar.

2.5 Modelo de costos operacionales: recursos humanos, infraestructura y alojamiento, licenciamiento y suscripciones, conectividad, energía e instalaciones, seguros y garantías, y optimizaciones previstas en el tiempo.

2.6 Estructura de mantención y soporte: modelo de costeo, recursos dedicados frente a compartidos, mantención preventiva programada, provisión para mantención correctiva, presupuesto de mejora continua y costos de actualización tecnológica.

2.7 Valorización de las cinco innovaciones: inversión, costo operacional incremental y beneficio esperado de cada una, reflejados en el flujo de caja.

Entregable 3 — Modelo financiero en planilla de cálculo

Herramienta de cálculo auditable con el modelo económico completo. Deberá contener, al menos, las hojas de Resumen Ejecutivo, Parámetros, Curva S, Costos, Ingresos, Flujo de Caja e Indicadores.

Requisitos técnicos obligatorios del modelo:

.

.

.

Uso correcto de fórmulas financieras. Referencias absolutas y relativas apropiadas. Validación de datos en las celdas de entrada. Protección de las fórmulas críticas. Documentación de los supuestos en cada hoja. Trazabilidad completa de los cálculos.

Ausencia de valores fijos incrustados dentro de las fórmulas.

Criterios de evaluación del modelo: coherencia y consistencia de fórmulas, flexibilidad para el análisis de

escenarios, claridad de la presentación, robustez ante cambios de parámetros, alineación con los documentos

1 y 2 y cumplimiento de la plantilla proporcionada.

Requisitos formales de presentación

.

.

Documentos 1 y 2 en formato PDF y DOCX; modelo financiero en XLSX. Numeración correlativa de páginas e índice detallado en cada documento. Nomenclatura de los archivos, sin excepción: [EMPRESA]_OfertaEconomica_1_[FECHA].pdf [EMPRESA]_AnalisisFinanciero_2_[FECHA].paf [EMPRESA]_ModeloFinanciero_3_[FECHA].xIsx

Los valores de los tres documentos deben ser idénticos; cualquier discrepancia es causal de descalificación.

Es obligatorio presentar todos los valores en las tres monedas, con el tipo de cambio del Formulario E-24 claramente indicado.

La oferta debe incorporar todas las correcciones solicitadas en los informes y presentaciones preparatorias.

Toda la información económica está sujeta al acuerdo de confidencialidad.

RECORDATORIO FINAL:

El incumplimiento de cualquier requisito establecido en estas instrucciones resultará en la descalificación automática del proceso.

No se aceptarán entregas parciales, fuera de plazo, o que no cumplan con el formato especificado.

#### Formulario E-24

Licitación N° TFEP-01/2026

CONDICIONES Y PARÁMETROS PARA LA PREPARACIÓN DE LA OFERTA ECONÓMICA

Dólar de los Estados Unidos (USD)

Euro (EUR)

Unidad de Fomento (UF)

Tasa de interés — crédito de consumo

Tasa de interés — línea de crédito

Rentabilidad máxima a obtener

Monto máximo a utilizar en línea de crédito Porcentaje máximo de financiamiento propio Porcentaje máximo de financiamiento bancario Impuesto al Valor Agregado

Horizonte de evaluación

Valor a utilizar

$ 900

$ 1.000

$ 40.000

0,9 % mensual 3,0% mensual 20%

$ 50.000.000 20%

80%

19%

56 meses

#### Formulario E-25 — HITOS DE PAGO

Estructura obligatoria de hitos de pago de la fase de implementación. Los porcentajes se aplican sobre el valor total de la fase de implementación.

Etapa 1 — Implementación

Em Descripción y entregable que lo gatilla DTS

Cierre del levantamiento y aprobación de la línea base de alcance y de la

89 matriz de trazabilidad de requerimientos. % Aprobación del documento de arquitectura, del plan de seguridad y del

H2 4 7% modelo de datos.

H3 Entrega de la infraestructura híbrida y habilitación de los ambientes de 6 10% Desarrollo, QA, Preproducción y Producción, con observabilidad operativa. o

Ha Entrega del software de la Etapa 1 para pruebas, con QA superado y evidencia 20 10% de cobertura.

HS Certificación de la solución de la Etapa 1: pruebas de aceptación de usuario, de 12 10% carga, de resiliencia y de seguridad ofensiva aprobadas. : Inicio de la marcha blanca de la Etapa 1, con plan de reversión activo

H6 á pnl y 13 5% usuarios capacitados.

H7 Paso a producción de la Etapa 1 y cierre conforme de la marcha blanca. 16 10% Subtotal Etapa 1 60%

Etapa 2 — Implementación

Descripción y entregable que lo gatilla EE]

Aprobación de la línea base de alcance de la Etapa 2 y de su diseño detallado. 5% H9 Entrega del software de la Etapa 2 para pruebas, con QA superado. alo 10% H10 | Certificación de la solución de la Etapa 2 y cierre del desarrollo. 18 10% Inicio de la marcha blanca de la Etapa 2 en convivencia con la Etapa 1 en H11 y 2 úl 19 5% producción. P mm at m2! aso a prodoeción de la Etapa 2 y aceptación final del proyecto de 21 10% implementación. Subtotal Etapa 2 40%

Operación de la solución

CO

Valor mensual fijo más componentes variables, pagado dentro

Hito mensual en de los primeros días del mes siguiente vencido, sujeto al 36 pagos, meses 21 a producción descuento de las multas por incumplimiento de nivel de 56 servicio.

La suma de los hitos de la Etapa 1 y de la Etapa 2 debe totalizar el 100 % del valor de la fase de implementación. La fase de Operación se factura integramente contra los 36 pagos mensuales y no puede anticiparse ni prorratearse en la fase de implementación.

#### Formulario E-26 — RANGO DE VALORES ACEPTADOS PARA PERFILES PROFESIONALES

Rangos permitidos de costo y tarifa horaria para los servicios profesionales, expresados en Unidades de Fomento, que deben considerarse en la preparación de la oferta económica.

CI Es

Director de Proyecto 1,5- 2,8 UF 2,5-4,0UF Gerente de Proyecto 1,5=28 UF 2,5-4,0UF Jefe de Proyecto 0,8-2,1 UF 1,5 - 3,0 UF Jefe de Análisis y Diseño 0,7-1,4 UF 1,0-2,0 UF Jefe de Desarrollo 0,7-1,4 UF 1,0- 2,0 UF Jefe de TIC 0,7-1,4 UF 1,0 - 2,0 UF Analista / Diseñador Experto 0,5-0,8 UF 0,8-1,2UF Analista / Diseñador Senior 0,5-0,7 UF 0,7 — 1,0 UF Analista / Diseñador Junior 0,3-0,6 UF 0,5-—0,8 UF Ingeniero Experto 0,6- 1,0 UF MOSTSUE Ingeniero Senior 0,6-0,8 UF 0,8-1,2 UF Ingeniero Junior 0,4-0,7 UF 0,6- 1,0 UF Arquitecto Experto 0,8- 1,4 UF 1,5-2,5 UF Arquitecto Senior 0,8- 1,4 UF 1,2 - 2,0 UF Arquitecto Junior 0,7 -— 1,0 UF 1,0- 1,5 UF Encargado de Seguridad Tl 0,8- 1,4 UF 1,5-2,5 UF Ingeniero de Datos 0,6-1,0 UF 1,0 - 1,5 UF Ingeniero DevOps / SRE 0,6-1,0 UF 1,0- 1,5 UF TIC 0,6-1,0 UF 0,8-1,5 UF Documentador 0,3-0,7 UF 0,5-1,0 UF Analista QA Experto 0,5—0,7 UF 0,8-1,0UF Analista QA Senior 0,4-0,6 UF 0,6-0,8 UF Analista QA Junior 0,3-0,4 UF 0,4-0,6 UF

Pueden existir otros roles no contenidos en la lista. Deberán declararse en la hoja de tarifas del modelo financiero y respetar rangos coherentes con los aquí indicados.