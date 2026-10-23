> Detalle de la revisión de los formularios (2026-10-12). Borrador. **Nota:** cualquier hallazgo que diga que el Comité de Operación debe iniciar en el mes 16 es un falso positivo: el artículo 71 de las Bases fija «mensual desde el mes 13».

# Revisión Formulario T-10 (Metodología para el desarrollo)

Archivo: `02_Propuesta/latex_final/sd-06/OSS-Formulario-T-10.tex` (las líneas citadas son de este archivo, salvo que se indique otro).

Nota de método: en el árbol de trabajo no existe el cuerpo del sd-06. `OSS-Subdocumento6.tex` figura como borrado (D) en git y solo está `OnlySimpleSolutions-Subdocumento6-Anexos.tex`. Contrasté contra la versión de HEAD (`git show HEAD:02_Propuesta/latex_final/sd-06/OSS-Subdocumento6.tex`), copiada en `scratchpad/sd6body.tex`. El T-10 remite a numeración 6.2.x de ese cuerpo.

Definición oficial: Bases Administrativas l. 2274-2276 (T-10 solo remite al Subdocumento 6, letra b) y l. 2130-2140 (letra b del T-7: «enfoque coherente con la naturaleza del proyecto, con sus implicancias en gestión de requerimientos, arquitectura evolutiva, refactorización, deuda técnica y tiempo de salida al mercado»; más prácticas DevSecOps/CI-CD/IaC/automatización de pruebas y «ceremonias, artefactos, cadencias y mecanismos de decisión»).

## Resumen
Total 10 hallazgos: 0 graves, 6 medianos, 4 bajos. El formulario es coherente en lo grueso (cifras de desempeño, carga a 1,5 veces el peak, 24 h de autonomía, etapas y meses, Comité de Operación). Los problemas están en la versión del catálogo, el reparto de servicios por equipo, la cadena de herramientas frente al sd-04, la instancia de cruces y los temas de la letra b que no se desarrollan.

## Hallazgos

### 1. Versión del catálogo desactualizada (mediana, confirmado)
- Ubicación: l. 238, «catálogo de requerimientos v3.0».
- Debería decir: versión vigente 3.1 (308 elementos: 227 RF, 72 RNF, 9 OP). Fuente: verdad_proyecto l. 20 y glosario («Versión vigente 3.1 (308 elementos). El sd-02 describe el recibido (3.0)»).
- Arrastre: el cuerpo del sd-06 (HEAD, l. 2959 y referencia l. 3641) también dice v3.0 con 223/75/9 = 307. Conviene corregir los dos a la vez.
- Sugerencia: «catálogo de requerimientos v3.1».

### 2. Asignación de servicios a equipos incoherente con el sd-03 (mediana, confirmado)
- Ubicación: l. 179-180 (Tabla T-10.1).
- Dice: «Retail · Relación con el cliente: Servicios R:CL de Relación con el cliente y pedidos». «Retail · Venta: servicios R:V de Venta».
- Problema: pedidos es R:V-01, del área de Venta. Relación con el cliente solo tiene R:CL-01 (posventa) y R:CL-02 (clientes Retail). El sd-03 (l. 138) pone pedidos, ventas, comisiones y marketplace en Venta. El mismo texto (l. 185) dice que los nueve servicios de Retail se reparten entre los tres equipos, así que la tabla debe cuadrar con el sd-03.
- Sugerencia: Relación con el cliente = R:CL-01 y R:CL-02. Venta = R:V-01 a R:V-04. Mercadería = R:M-01 a R:M-03. La contraparte «Gerencia de Canales Digitales» tendría que reasignarse en consecuencia (pedidos y marketplace tocan canal digital). Esto se puede aclarar en una nota.
- Complemento (baja): la columna «Contexto» usa Retail / Emisor / Plataforma compartida, pero el sd-03 y el glosario hablan de tres frentes (Retail, Filial emisora, Frontera). X-01 está asignado al equipo «Plataforma» sin llamarlo frontera. Aclarar que X-01 pertenece al frente Frontera.

### 3. Cadena de herramientas frente al sd-04 (mediana, confirmado)
- Ubicación: l. 424 y 454-466 (Tabla T-10.7).
- El sd-04 (l. 444) fija «Terraform y canal CI/CD con registro de artefactos y despliegue auditado», con la alternativa «Reutilizar el canal del Cliente… si satisface revisión, firma y trazabilidad» (estado «Por probar»). El sd-04 (l. 537) nombra **Azure Pipelines** y Container Registry como servicios de «Operación y entrega» de CLD-01. Verificado: Azure Pipelines sí aparece en el sd-04, solo en esa línea.
- El T-10 propone **GitHub Enterprise y GitHub Actions** como repositorio y flujo de entrega, y no menciona Azure Pipelines. Hay dos productos de CI/CD distintos entre sd-04 y T-10, sin explicación.
- Terraform: coherente (T-10 «Comprometida»; sd-04 l. 590 y 444).
- Azure Container Registry: coherente con el sd-04 (Container Registry).
- Key Vault: coherente.
- HSM: ver hallazgo 4.
- SonarQube, Trivy, Syft, Cosign, ZAP, Pact, Playwright, k6, Ansible, Helm, Argo CD y K3s no aparecen en ningún sd-01 a sd-04. Según la verdad del proyecto, las herramientas DevSecOps son «producto por definir», por lo que rotularlas «Propuesta» es aceptable. K3s/Helm/Argo/Ansible están bien como «Candidatas».
- Sugerencia: añadir una frase en l. 424 que diga que el canal definitivo (GitHub Actions o Azure Pipelines, o el canal del Cliente) se fija en H2 según el ADR del sd-04, y que Azure Pipelines es la alternativa nativa de Azure. O, si el equipo ya eligió GitHub, corregir el sd-04 l. 537. Por confirmar con el equipo cuál prevalece.

### 4. HSM: nombre y condición (baja, por confirmar)
- Ubicación: l. 465, «Azure Key Vault y HSM… HSM para las llaves del Emisor cuando corresponda; Según clasificación, residencia y separación de funciones».
- El sd-04 (l. 442) dice «Managed HSM» para la filial emisora, en estado «Por probar», condicionado a «la disponibilidad de Managed HSM en la región».
- El T-10 no está en conflicto, porque la decisión sigue abierta. Conviene alinear el nombre («Azure Managed HSM») o decir «HSM por definir, ver sd-04».

### 5. Instancia que aprueba cruces Retail–Emisor sin nombre (mediana, confirmado)
- Ubicación: l. 693 (Tabla T-10.11): «Decide: Instancia competente, con las evaluaciones documentadas; Consulta: Líder de Datos, Encargado de Seguridad y contraparte de cumplimiento; Informa: Comité Ejecutivo».
- Problema: la tabla de decisiones no dice quién decide. El sd-04 (l. 372 y 413) es explícito: «El área de cumplimiento aprueba la ficha de cada cruce» de X-01 (cumplimiento de Ancoa; en T-9 l. 336, Contraloría y Negocio Financiero). El sd-01 asigna al Comité Ejecutivo solo los cambios de alcance. Además, el T-9 l. 485 pone a esas tres figuras como quienes deciden y al Comité de Arquitectura como consultado, de modo que los dos formularios se contradicen entre sí (el T-10 invierte quién decide y quién consulta).
- Sugerencia: decide «Contraparte de cumplimiento de Ancoa (Contraloría y Negocio Financiero) aprueba la ficha del cruce»; consultan Líder de Datos, Encargado de Seguridad y Comité de Arquitectura; informa Comité Ejecutivo. Alinear la tabla de T-9 (l. 485 y 1079, donde también dice «Instancia competente»). La misma fórmula vaga aparece en T-9.

### 6. Roles que no existen en el sd-01 (mediana, por confirmar)
- Ubicación: l. 219-228 (Tabla T-10.2), 365-371 y 690-698.
- El sd-01 (l. 188-324) define Arquitecto de Solución, Encargado de Seguridad de la Información, Líder de Datos, Líder de Calidad, Líder de Operación, Líder de Implantación y Gestión del Cambio y Jefe de Proyecto. El T-10 usa «Líder de Calidad y Pruebas» (el sd-01 dice «Líder de Calidad»; el sd-07 usa los nombres del sd-07), «Líder de Operación / SRE» (el sd-01 dice «Líder de Operación»; el sd-07 y T-9 sí usan «/ SRE»), y «Líder de Desarrollo» y «Líder de Integración» (el sd-01 no los lista; sí el sd-07 l. 145-158: Líder Funcional, Líder de Desarrollo, Líder de Integración). El «Dueño de producto» y «Scrum Master» son roles de Scrum no listados en el sd-01 (se asignan a Ancoa y a OSS, uno por equipo).
- Además, el Jefe de Proyecto no aparece en ninguna tabla del T-10 y es el rol que, según el sd-01, tramita las solicitudes de cambio (hoy la matriz T-10.11 las deja en Comité Ejecutivo y Comité de Proyecto sin dueño).
- Sugerencia: unificar con el glosario del sd-07 y mencionar al Jefe de Proyecto en «Cambio de alcance o de hito» (como quien tramita). Ajustar «Líder de Calidad y Pruebas» a «Líder de Calidad» o aclarar la equivalencia.

### 7. Contenidos de la letra b no desarrollados: refactorización y tiempo de salida al mercado (mediana, confirmado)
- Ubicación: ausentes en todo el archivo (búsqueda de «refactor», «salida al mercado», «time to market»: 0 resultados).
- Las Bases (l. 2134) exigen «implicancias en gestión de requerimientos, arquitectura evolutiva, refactorización, deuda técnica y tiempo de salida al mercado». El T-10 cubre deuda técnica (T-10.9), ADR (T-10.13) y una versión mínima de requerimientos (solo la definición de preparado, T-10.3). No hay política de refactorización (cuándo, quién, con cuánta capacidad; la reserva del 15 % de T-10.9 podría ser el vehículo) ni vínculo explícito con el tiempo de salida al mercado (el indicador «Tiempo de entrega» de T-10.12 con meta «Fijada por servicio» es lo más cercano). Tampoco aparece «arquitectura evolutiva» como tal, aunque las «funciones de aptitud» (l. 509 y 792) la insinúan.
- El formulario dice que 6.2 contiene el resumen y el análisis (l. 94), así que el cuerpo del sd-06 (HEAD, 6.2.3.1 «Arquitectura evolutiva») podría cubrirlo. Ver nota de método: el cuerpo no está en el árbol. Sugerencia: añadir un apartado breve (T-10.9 o nuevo) con la regla de refactorización y la lectura de «Tiempo de entrega» como medida del tiempo de salida al mercado, o remitir expresamente a 6.2.x.

### 8. Prueba de autonomía de 24 h: falta el vínculo con el piloto de tienda (baja, confirmado)
- Ubicación: l. 511 (Preproducción · Operación sin enlace).
- Dice: «al menos 24 h continuas de autonomía degradada; tras el escenario de 8 h sin enlace, sincronización automática en ≤ 30 min…». Es correcto con la verdad del proyecto (24 h, el Caso dice 8 h).
- Falta: el sd-04 (l. 388) fija la prueba real como corte provocado de 24 h en una de las tres tiendas piloto en los meses 6 y 7, fuera de la semana previa y de los tres días del evento anual, con conciliación ≤ 30 min tras el retorno y acta de la Contraparte Técnica. En T-10 el tope de 30 min está asociado al escenario de 8 h, mientras el sd-04 lo asocia a la conciliación tras el corte de 24 h.
- Sugerencia: aclarar que el umbral de 30 min aplica también tras el corte de 24 h y citar la prueba piloto (meses 6 y 7). Por confirmar la intención.

### 9. Remisión confusa en la introducción (baja, confirmado)
- Ubicación: l. 94, «Conforme al Formulario T-7 y al Formulario T-21 de las Bases Administrativas…».
- El T-7 define el contenido (letra b); el T-21 es el formulario de evaluación y ponderación (Bases l. 2366-2394). Un formulario no se «conforma» al T-21. Sugerencia: «Conforme al Formulario T-10 y a la letra b del Subdocumento 6 del Formulario T-7».

### 10. Hito H3 y sus contenidos (baja, confirmado)
- Ubicación: l. 378, «El hito H3 entregará los cinco ambientes habilitados y operativos».
- No indica el mes. H3 es mes 6 (sd-07 l. 466 y 690; Bases l. 2644: «H3… 6, 10 %»). Las Bases definen H3 con cuatro ambientes (Desarrollo, QA, Preproducción y Producción) con observabilidad operativa. Los cinco ambientes (con Recuperación ante Desastres) vienen del sd-07 l. 466 y del cuerpo del sd-06, y el sd-04 (l. 594) ubica Recuperación en CLD-02. No hay conflicto, pero conviene decir «H3 (mes 6)» y que Recuperación ante Desastres es adicional a lo exigido por las Bases.
- Menor: la contraparte «Gerencia de Logística y Prevención de Pérdidas» (l. 178) no aparece en T-9 ni en sd-01 a sd-04. El Caso habla de «Prevención de pérdidas». Por confirmar el nombre.

## Verificado y correcto (sin hallazgo)
- Umbrales de desempeño: evaluación crediticia ≤ 8 s, pedido durante el evento ≤ 3 s (RT-09.01 del Caso), precios ≤ 5 min, carga a 1,5 veces el peak (l. 509-510). Coinciden con la verdad y con el cuerpo del sd-06.
- Autonomía: 24 h continuas (el Caso dice 8 h; las Bases piden 24 h o el mayor).
- Ambientes (cinco), con Recuperación ante Desastres que no es paso de promoción: coherente con sd-04 y sd-07.
- Convivencia de etapas (meses 13-15, 19-20, 21) y operación del mes 21 al 56: coherente con el cronograma.
- Hitos H8 (línea base de la Etapa 2) y E-25: correctos (sd-07 l. 694; Bases l. 2146).
- Comité de Operación, Comité de Arquitectura (aprueba decisiones de arquitectura), Comité Ejecutivo (aprueba cambios de alcance), Comité de Proyecto: coherentes con sd-01 l. 333-340. El Comité de Operación mensual desde el mes 13 no figura en el T-10 (no hace falta).
- Sin precios en el formulario (art. 50) y sin Mermaid ni imágenes.
- Remisiones a T-8, T-9, T-13, T-15 y T-18: existen en las Bases con ese contenido (T-8 equipo, T-13 pruebas, T-15 nivelación, T-18 implantación).
