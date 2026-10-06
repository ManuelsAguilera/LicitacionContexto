# FEP05 · Sala de Servidores

> Transcripción a Markdown de la presentación original (80 diapositivas). Los diagramas se representan con su texto; los elementos puramente gráficos no se incluyen.

## Índice de secciones

- [SECCIÓN 1 · Datacenter](#diapositiva-4) — diapositiva 4
- [SECCIÓN 2 · El programa de recintos](#diapositiva-14) — diapositiva 14
- [SECCIÓN 3 · Opciones de distribución](#diapositiva-28) — diapositiva 28
- [SECCIÓN 4 · Seguridad, acceso y monitoreo](#diapositiva-37) — diapositiva 37
- [SECCIÓN 5 · Energía y clima](#diapositiva-45) — diapositiva 45
- [SECCIÓN 6 · Rack y cableado](#diapositiva-60) — diapositiva 60
- [SECCIÓN 7 · Servidores, comunicaciones y storage](#diapositiva-71) — diapositiva 71

---

<a id="diapositiva-1"></a>

## Diapositiva 1 · Portada

Pontificia Universidad Católica de Valparaíso Escuela de Informática

**Taller Formulación de Proyectos Informáticos**

**ICI-5444**

**Antonio Moya Villegas**

antonio.moya@pucv.cl

v2.1.0 - 2026

---

<a id="diapositiva-2"></a>

## Diapositiva 2 · Esto es un datacenter

**EL MITO**

**Un edificio completo**

Cientos de racks, megawatts, generadores en fila, turnos 24/7 y redundancia certificada. Es un negocio en sí mismo: se vende espacio, energía y conectividad.

**LA REALIDAD**

**Ustedes diseñan de 1 a 12 gabinetes**

Dentro de un edificio que ya existe y tiene otro uso. Decenas de kW. Operación remota, turnos si se requiere.

---

<a id="diapositiva-3"></a>

## Diapositiva 3 · Lo que vamos a ver

Nueve paradas. Las del medio son el recinto que ustedes tienen que dibujar.

**1**

**2**

**Datacenter**

**Recintos**

Qué es, cómo se clasifica y por qué no van a construir uno.

Las trece salas de una sala de servidores bien hecha.

**5**

**6**

**Energía y clima**

Lo que explica casi todas las caídas y casi todo el costo.

**Rack y cableado**

La U, la elevación del gabinete y el orden de los cables.

**3**

**4**

**Distribución**

**Seguridad**

Cómo se ordenan los racks y los recintos. Cuatro escalas, cuatro esquemas.

Acceso, cámaras, sensores y el gas que puede matar.

**7**

**Equipamiento**

Servidores, comunicaciones y almacenamiento.

---

<a id="diapositiva-4"></a>

## Diapositiva 4 · ▶ SECCIÓN 1 · Datacenter

**1**

**Datacenter**

Cultura general, rápido. Sirve para tener el vocabulario y para saber de dónde viene cada cosa que después van a poner en su sala.

- Qué necesita para funcionar
- Redundancia: N, N+1, 2N
- Cuánto vale un nueve más
- PUE: la cuenta de la luz
- Qué significa cada nivel
- La tabla de traducción

---

<a id="diapositiva-5"></a>

## Diapositiva 5 · Cuatro cosas, todo el tiempo

Un datacenter no es «donde están los servidores». Es donde se garantizan estas cuatro cosas sin parar.

**PRIMERO**

**Energía acondicionada**

Filtrada, sin microcortes y con respaldo. Alimenta desde varias decenas hasta decenas de miles de servidores.

**SEGUNDO**

**Clima controlado**

Sin extracción del calor, el equipamiento agrupado se apaga solo por protección térmica. Temperatura y humedad.

**Y una quinta que no se ve: alguien mirando**

**TERCERO**

**Conectividad**

Fibra óptica de alta velocidad, hoy del orden de varios terabits por segundo, y por más de un camino.

**CUARTO**

**Seguridad física**

Contra intrusión, incendio y agua. La puerta cerrada con acceso controlado es el elemento primordial.

Monitoreo permanente y un procedimiento escrito. Un sensor sin destinatario y sin procedimiento es sólo un pitido en una sala vacía.

Ese es también el orden del diseño y el orden del presupuesto: primero energía, después clima, después red, y sólo entonces los servidores.

---

<a id="diapositiva-6"></a>

## Diapositiva 6 · Cuánto vale un nueve más

La clasificación TIER de ANSI/TIA-942 y del Uptime Institute, traducida a lo único que entiende un gerente: horas caído.

> 🖼️ **Contenido gráfico — Comparativa de disponibilidad y tiempo de inactividad anual por nivel TIER:**

| Nivel | Disponibilidad | Inactividad anual | Descripción |
|---|---|---|---|
| Tier I | 99,671% | 28,8 horas | Infraestructura básica: sin redundancia; hay que detener para mantener y es propenso a interrupciones |
| Tier II | 99,741% | 22,7 horas | Componentes redundantes (N+1): suelo técnico, generadores y UPS |
| Tier III | 99,982% | 1,6 horas | Mantenimiento concurrente: se repara y mantiene sin interrumpir el servicio gracias a múltiples líneas de distribución |
| Tier IV | 99,995% | 26,3 minutos | Tolerancia total a fallos: infraestructura 2(N+1) que mantiene el funcionamiento incluso ante eventos críticos no planificados |

---

<a id="diapositiva-7"></a>

## Diapositiva 7 · Redundancia: la letra lo dice todo

Escribir «sistema redundante» en una propuesta no dice nada. Con la letra, sí.

**N**

**Justo lo necesario**

Sin repuesto. Si falla un componente, el servicio se cae. Sólo para lo que no es crítico.

**N+1**

**Un repuesto**

El equipo adicional asume la carga y además permite mantener sin apagar. Es la configuración típica de una sala de servidores.

**2N**

**Dos sistemas completos**

Independientes entre sí. El segundo continúa solo. Es lo que exige un TIER IV.

**2(N+1)**

**Dos, con repuesto**

Se puede fallar y hacer mantenimiento a la vez. Hiperescala y misión crítica.

Ojo con el trayecto: de poco sirve un segundo UPS si ambos alimentan el mismo tablero por el mismo ducto. La redundancia también es de camino, y se verifica siguiendo el cable, no leyendo la ficha técnica.

---

<a id="diapositiva-8"></a>

## Diapositiva 8 · PUE: por qué la cuenta de la luz importa

Enfriar los servidores cuesta casi lo mismo que alimentarlos. Esa proporción tiene nombre y se puede exigir en las bases.

La eficiencia en el uso de la energía (Power Usage Efectiveness - PUE) es un cálculo utilizado para medir la eficiencia energética de los centros de datos.

La mejora de 2,5 a 1,57 en catorce años no vino de servidores más eficientes: vino de confinar pasillos, tapar huecos y cambiar la forma de enfriar. Eso es diseño de sala, y es exactamente lo que ustedes tienen que proponer.

**2,5**

era el promedio de la industria en 2007, cuando se introdujo la métrica. Por cada watt de cómputo se gastaba otro watt y medio en sostenerlo.

**1,54**

es el promedio mundial que reportó el 2025, (1,57 en 2021) (1,59 en 2020): alrededor del 60% de la energía llega a los equipos TI.

**1%**

del consumo eléctrico mundial se lo llevan los centros de datos. Por eso el PUE dejó de ser una curiosidad técnica y pasó a las bases de licitación.

---

<a id="diapositiva-9"></a>

## Diapositiva 9 · Qué se mide arriba y qué se mide abajo

La fórmula es fácil. Lo difícil es ponerse de acuerdo en dónde se pone el instrumento.

**Numerador · toda la instalación**

Se lee en el medidor de la compañía eléctrica.

Incluye servidores, red, storage, refrigeración e iluminación.

Incluye también las pérdidas del UPS y de los tableros.

Es todo lo que entra al recinto, sin excepciones.

**Denominador · sólo el equipamiento TI**

Se lee habitualmente en las PDU de los racks.

Sólo servidores, almacenamiento y electrónica de red.

No entra el clima, ni la luz, ni las pérdidas del UPS.

Es la energía que efectivamente hace cómputo.

**El ejemplo canónico**

Una instalación que consume 50.000 kWh, de los cuales 40.000 kWh son equipos TI, tiene un PUE de 1,25.

**DCiE: la misma cuenta al revés**

DCiE = energía TI / energía total. En el mismo ejemplo, 80%. Es un porcentaje en vez de un ratio: dice cuánto de lo que se paga hace cómputo.

**PUE 1,0 no existe**

Sería una sala sin clima, sin luz y sin pérdidas. Mientras más cerca de 1, mejor; mientras más alto, más energía se va en algo que no computa.

En la propuesta: declaren el PUE de diseño, digan en qué dos puntos se mide y comprométanse a medirlo. Un PUE sin punto de medición declarado no es un compromiso, es una cifra suelta.

---

<a id="diapositiva-10"></a>

## Diapositiva 10 · Cómo se mide y cómo se baja el PUE · ficha técnica

Lo que hay que escribir en la propuesta, ordenado por cuánto mueve la aguja.

| Medida | Cuánto mueve | Qué implica en el diseño de la sala |
|---|---|---|
| Confinar el pasillo frío | Lo que más | Cerramiento del pasillo y paneles ciegos en toda U vacía del rack |
| Evitar la recirculación de aire | Mucho | Sellar pasadas de piso técnico, tapar huecos y ordenar el cableado trasero |
| Refrigeración de mejor tecnología | Mucho | Precisión con velocidad variable, free cooling cuando el clima lo permite |
| Fuentes, iluminación y detalles | Poco, pero suma | Fuentes de alto rendimiento, luz automática por presencia, cargas parásitas fuera |
| Medir periódicamente | Habilita todo | El consumo cambia con la hora y la estación: una sola medición no sirve de referencia |

**Algunos datos**

La Agencia Internacional de Energía, estimo que la IA consumió alrededor del 0,5 % de la electricidad mundial en 2025

https://www.datacenter-asia.com/blog/how-much-power-does-a-data-center-use .

---

<a id="diapositiva-11"></a>

## Diapositiva 11 · La tabla de traducción

Cada cosa del datacenter tiene un equivalente proporcionado en su sala. Ésta es la lámina bisagra de la clase.

| En el datacenter | Equivalente en su sala de servidores | § |
|---|---|---|
| Salas blancas de cientos de racks | Un recinto de 25 a 45 m² con 4 a 12 gabinetes | 2 · 3 |
| Centro de operaciones con turnos 24/7 | Sala de monitoreo con pantallas y alarmas al celular | 2 · 4 |
| Perímetro con guardias y esclusas múltiples | Tres líneas de acceso: recepción, zona técnica, sala | 4 |
| CCTV con decenas de cámaras y sala de video | Cuatro a ocho cámaras con grabación y retención declarada | 4 |
| Extinción por gas en todas las salas | Extinción por agente limpio sólo en la sala de servidores | 4 |
| Subestación propia y doble alimentador | Empalme único, transferencia automática y generador | 5 |
| Salas de UPS con decenas de módulos | Un UPS N+1 y su banco de baterías en recinto propio | 5 |
| Agua helada y free cooling | Dos unidades de precisión N+1 y confinamiento de pasillo | 5 |
| Pasillos confinados en filas completas | Dos filas enfrentadas: pasillo frío y pasillo caliente | 5 |
| MMR con veinte operadores | Sala de acometida con dos proveedores | 6 |
| Kilómetros de cableado con DCIM | Cableado certificado y etiquetado en una planilla | 6 |
| Miles de servidores | Un clúster de tres a seis nodos virtualizados | 7 |

---

<a id="diapositiva-12"></a>

## Diapositiva 12 · Los cuatro niveles, lado a lado · ficha técnica

La comparación completa. Es la tabla que hay que mirar al elegir el nivel objetivo del caso.

|  | TIER I | TIER II | TIER III | TIER IV |
|---|---|---|---|---|
| Caminos de distribución | Uno | Uno | Uno activo, uno alternativo | Dos activos |
| Componentes redundantes | No | N+1 | N+1 | 2(N+1) |
| Piso técnico | Habitualmente no | Sí | Sí | Sí |
| UPS y generador | No | Sí | Sí | Sí |
| Mantenimiento sin caída | No | No | Sí | Sí |
| Tolera falla imprevista | No | No | Parcialmente | Sí |
| Carga máxima en situación crítica | — | 100% | 90% | 90% |
| Disponibilidad máxima | 99,671% | 99,741% | 99,982% | 99,995% |
| Caída equivalente al año | ≈ 28,8 h | ≈ 22,7 h | ≈ 1,6 h | ≈ 0,4 h |

El TIER no se hereda del proveedor: si su servidor está en un datacenter TIER III pero el enlace de la sucursal es único, la disponibilidad del servicio no es TIER III.

---

<a id="diapositiva-13"></a>

## Diapositiva 13 · Redundancia y normas · ficha técnica

| Configuración | Qué significa | Qué pasa si falla un componente | Dónde se usa |
|---|---|---|---|
| N | Exactamente la capacidad necesaria, sin repuesto | El servicio se cae | Salas pequeñassin criticidad |
| N+1 | Un componente adicional sobre lo necesario | El repuesto asume la carga; no hay caída | La configuración típica de una sala de servidores |
| 2N | Dos sistemas completos e independientes | El segundo sistema continúa solo | Datacenter TIER IV |
| 2(N+1) | Dos sistemas completos, cada uno con repuesto | Se puede fallar y mantener a la vez | Hiperescalay misióncrítica |

| Norma o ley | Qué cubre | Cómo se usa en la propuesta |
|---|---|---|
| ANSI/TIA-942 | Infraestructura de telecomunicaciones y grados de disponibilidad | Justifica el nivel objetivo y la topología del cableado |
| ASHRAE TC 9.9 | Rangos térmicos y de humedad de los equipos de TI | Respalda la temperatura y la humedad declaradas |
| NFPA 75 y NFPA 2001 | Protección contra incendio y sistemas de agente limpio | Respalda la compartimentación y el sistema elegido |
| NCh Elec. 4/2003 · NCh 2777 | Instalaciones eléctricas y grupos electrógenos (Chile) | Obligatorias: tableros, protecciones, tierra, declaración SEC |
| NCh 2527 · NCh 3002 | Áreas de servicio y bienestar · transformadores | Aplican a baños, comedor y a la zona técnica exterior |
| Ley N°21.719 | Datos personales · vigencia plena 1 dic 2026 | Condiciona dónde pueden residir los datos |
| ISO/IEC 27001 A.11 · ISO 22301 | Seguridad física del entorno y continuidad del negocio | Si el mandanteexigecertificacióno auditoría |

---

<a id="diapositiva-14"></a>

## Diapositiva 14 · ▶ SECCIÓN 2 · El programa de recintos

**2**

**El programa de recintos**

Una sala de servidores no es una pieza con servidores. Es un conjunto de recintos con funciones distintas y puertas distintas.

- La idea que ordena todo
- Los baños quedan fuera
- El plano por zonas
- Adyacencias obligadas
- Ficha de cada recinto
- Ficha técnica

---

<a id="diapositiva-15"></a>

## Diapositiva 15 · La idea que ordena todo

**LA IDEA QUE ORDENA TODO**

**Si la sala de servidores es la más visitada, el diseño está mal.**

Cada actividad que exige la entrada de una persona distinta merece un recinto distinto. El proveedor de fibra no tiene por qué pisar la sala. El electricista tampoco. El que repara un disco, menos.

---

<a id="diapositiva-16"></a>

## Diapositiva 16 · Data Center - Recintos

> 🖼️ **Contenido gráfico:** video de Cirion Data Centers (vista aérea de un campus de datacenter). Enlace: https://www.youtube.com/watch?v=VVS68mCsOGQ&t=3s

---

<a id="diapositiva-17"></a>

## Diapositiva 17 · Los cuatro principios

De aquí sale el programa, no de una lista copiada de Internet.

**PRINCIPIO 1**

**Separar por función**

Energía, clima, comunicaciones, cómputo, operación y apoyo son funciones distintas, con riesgos distintos y con proveedores distintos.

**PRINCIPIO 2**

**Separar por acceso**

Cada recinto tiene una lista de quién puede entrar. Mientras más adentro, más corta la lista y más registro de por medio.

**PRINCIPIO 3**

**Separar por riesgo**

Lo que tiene agua, combustible, hidrógeno o fuego no comparte recinto con el cómputo. Ni siquiera muro con puerta directa.

**PRINCIPIO 4**

**Minimizar la visita a la sala**

El buen diseño logra que nadie tenga que entrar a la sala de servidores para operar, monitorear, reparar o recibir a un proveedor.

Consecuencia práctica: la sala más visitada tiene que ser la de acometida de comunicaciones, y por eso queda antes de la última línea de acceso.

---

<a id="diapositiva-18"></a>

## Diapositiva 18 · El plano por zonas

Tres líneas de acceso. Se recorre de izquierda a derecha, igual que camina una visita.

> 🖼️ **Contenido gráfico — Plano por zonas (de izquierda a derecha):**
>
> - **1ª línea · Administrativa:** recepción y control de acceso, sala de reuniones, bodega de insumos, taller de reparación, oficinas y circulación. Baños *fuera del perímetro*.
> - **2ª línea · Técnica:** esclusa/antesala, sala de monitoreo (NOC), acometida de comunicaciones (MMR), acometida eléctrica y tableros, sala de UPS y baterías.
> - **3ª línea · Restringida:** sala de servidores (sala blanca), sala de climatización, sala de extinción.
> - **Exterior:** generador y estanque, condensadoras, empalme eléctrico, llegada de enlaces de los operadores.
>
> *Donde hay artefactos sanitarios hay cañerías. Donde hay cañerías, hay filtraciones.*

---

<a id="diapositiva-19"></a>

## Diapositiva 19 · Un corte real

Los servidores no conviven con las personas ni con los suministros pesados.

**Generadores afuera**

Ruido, calor y gases de escape fuera del núcleo, con estanque y contención de derrames.

**Baterías en recinto propio**

Hidrógeno y peso: ventilación obligatoria y losa verificada.

**Tableros accesibles desde fuera**

Cortar la energía no puede exigir cruzar tres puertas controladas.

**Y los baños nunca tocan la sala**

Ni al lado ni en el piso de arriba. El agua por filtración es de las causas más frecuentes de daño.

---

<a id="diapositiva-20"></a>

## Diapositiva 20 · Pensando en el Plano

Data hall, corredores de servicio, CRAC, UPS, baterías, ATS, sala eléctrica y generadores.

**Léanlo como un recorrido**

**LO QUE HAY QUE VER**

Entrada → staging → seguridad → corredor de servicio → data hall. Cada salto es una puerta con otra lista de personas.

**El data hall está rodeado**

CRAC en los corredores de servicio, chillers afuera, extinción pegada pero separada.

**El staging no es decoración**

Es donde se desembala: el cartón no entra a la sala blanca.

**Ninguno comparte puerta con otro**

Se entra desde un pasillo de servicio, no desde el recinto vecino. Así una falla no se propaga.

**Cada peligro, en su pieza**

Generadores (combustible y gases) · baterías (hidrógeno y peso) · APU y tableros (arco eléctrico) · cilindros de extinción (presión y asfixia) · sala de servidores (lo que hay que proteger).

---

<a id="diapositiva-21"></a>

## Diapositiva 21 · El corazón y sus dos vecinos

Sala de servidores, sala de monitoreo y sala de climatización.

**SALA BLANCA · 3ª LÍNEA**

**Sala de servidores**

Aloja los racks. Es el recinto que todo lo demás existe para proteger.

Quién entra: sólo personal autorizado, registrado y acompañado. Nunca un proveedor solo.

Ojo: sin ventanas al exterior, sin cañerías de agua por encima, sin cartón almacenado.

**NOC · 2ª LÍNEA**

**Sala de monitoreo**

Temperatura, humedad, energía, red, cámaras y alarmas en una sola vista. Aquí se lleva la bitácora.

Quién entra: el equipo de operación. Es su lugar de trabajo.

Ojo: con ventana hacia la sala. Ver sin entrar es todo el objetivo.

**2ª / 3ª LÍNEA**

**Sala de climatización**

Equipos de aire de precisión, bombas, filtros y el tablero del clima.

Quién entra: el proveedor de mantenimiento, acompañado.

Ojo: contigua pero con puerta propia, porque mantener el clima implica agua, filtros y herramientas.

La regla que las une: nadie debería tener que entrar a la sala de servidores para operar, monitorear, reparar ni recibir a un proveedor.

---

<a id="diapositiva-22"></a>

## Diapositiva 22 · Energía: tres recintos, tres riesgos

No es manía de separar. Cada uno tiene un peligro distinto.

**2ª LÍNEA**

**Acometida eléctrica**

Empalme, medidor, tablero general, protecciones y la transferencia automática (ATS/TTA).

Ojo: accesible desde fuera del perímetro. Cortar la energía no puede exigir cruzar tres puertas.

**2ª LÍNEA**

**Sala de UPS y baterías**

Sostiene la carga mientras parte el generador o mientras se apaga ordenadamente.

Ojo: las baterías de plomo pueden liberar hidrógeno. Ventilación obligatoria, recinto separado y losa verificada.

**EXTERIOR**

**Generador y estanque**

Entrega energía cuando la red falla más tiempo del que aguanta el UPS.

Ojo: casi siempre afuera por ruido, vibración, calor y gases. El estanque exige contención de derrames y autorización.

Los tres se dibujan por separado en el plano y se cotizan por separado en el CAPEX. Y los tres tienen mantenimiento periódico, que es OPEX.

---

<a id="diapositiva-23"></a>

## Diapositiva 23 · Los tres recintos que siempre se olvidan

Acometida de comunicaciones, extinción y custodia.

**MMR · 2ª LÍNEA**

**Acometida de comunicaciones**

Aquí llegan físicamente los enlaces de los operadores y se instalan sus equipos. Es la frontera de responsabilidad de cada contrato.

Ojo: es el recinto con más visitas externas, así que queda ANTES de la última línea. Dos operadores, dos ductos distintos.

**2ª LÍNEA**

**Sala de extinción**

Cilindros del agente extintor, tablero de control y señalización.

Ojo: el agente actúa desplazando o inertizando el oxígeno. Es un sistema que atenta contra la vida y por eso tiene preaviso, evacuación y botón de aborto.

**1ª LÍNEA**

**Control de acceso y custodia**

Recibe, identifica, registra y autoriza. Es el filtro que hace que todo lo demás tenga sentido.

Ojo: un control de acceso sin registro auditable no sirve. Y el guardia no puede ser además quien acompaña al proveedor adentro.

Si en su plano no aparece la sala de acometida de comunicaciones, el técnico de fibra va a terminar entrando a la sala blanca. Todos los años pasa.

---

<a id="diapositiva-24"></a>

## Diapositiva 24 · Los de apoyo, que son los más baratos

Taller, bodega, reuniones. Y los baños, que quedan afuera.

**TALLER · 1ª LÍNEA**

**Sala de reparación**

Abrir un servidor genera polvo y exige espacio y herramientas. Nada de eso puede ocurrir junto a los racks en operación.

Mesa antiestática, pulsera de descarga y red aislada de diagnóstico.

**1ª LÍNEA**

**Bodega de insumos**

Repuestos, medios de respaldo, cables, tapas ciegas, filtros y consumibles.

Para que el cartón y el plumavit no terminen dentro de la sala, que es donde siempre terminan.

**1ª LÍNEA**

**Sala de reuniones**

Recibir proveedores, coordinar mantenimientos, auditar y capacitar.

Para que la conversación con el externo ocurra antes de la primera puerta.

**FUERA DEL PERÍMETRO**

**Baños y servicios**

Sin muro compartido con la sala y nunca en el piso superior.

Donde hay artefactos sanitarios hay cañerías, y donde hay cañerías hay filtraciones. Lo mismo vale para cocinas, calderas y estanques.

Los tres primeros suman pocos metros cuadrados y son los que mantienen ordenada la sala. Excluirlos se puede; hacerlo sin decirlo, no.

---

<a id="diapositiva-25"></a>

## Diapositiva 25 · Ejemplos

> 🖼️ **Contenido gráfico:** fotografía del acceso a un datacenter de Telecom, con los perímetros de seguridad marcados sobre la imagen. Video: https://www.youtube.com/watch?v=6tU5Opcsz68&t=1s

---

<a id="diapositiva-26"></a>

## Diapositiva 26 · Adyacencias: qué va junto a qué

El programa no basta. Importa cómo se ordenan entre sí.

**Debe quedar contiguo**

Monitoreo junto a la sala, con ventana: ver sin entrar.

Climatización junto a la sala, con recinto y puerta propios.

UPS cerca del tablero general, para acortar el recorrido de fuerza.

Acometida de comunicaciones cerca, pero antes de la última línea.

Extinción cerca de la sala que protege, con cañería corta.

Bodega y taller cerca del acceso: no cruzar el perímetro con cajas.

**No puede quedar contiguo**

Baños, cocinas o cualquier artefacto de agua junto o sobre la sala.

Estanque de combustible dentro del edificio o pegado a la sala.

Banco de baterías dentro de la sala: hidrógeno y peso.

Bodega de material combustible —papel, cartón, plumavit—.

Generador pegado a la sala: ruido, vibración, calor y gases.

Estacionamientos o bodegas de terceros con muro común.

Una regla que resume casi todas: por encima del cielo de la sala no debe pasar ninguna cañería de agua, salvo la del propio clima, y ésa va con detección de fuga bajo la bandeja.

---

<a id="diapositiva-27"></a>

## Diapositiva 27 · Los trece recintos · ficha técnica

Función, quién entra, línea de acceso y superficie de referencia para una sala de 8 a 12 racks.

| Recinto | Función | Quién entra | Línea | m² |
|---|---|---|---|---|
| Sala de servidores | Aloja los racks: cómputo, almacenamiento y red | Operador autorizado, acompañado | 3ª | 25 –45 |
| Sala de monitoreo (NOC) | Pantallas, consola, alarmas, bitácora | Operación y turno | 2ª | 12 –20 |
| Sala de climatización | Equipos de aire de precisión y su mantenimiento | Proveedor de clima | 2ª/3ª | 10 –18 |
| Sala de extinción | Cilindros de agente limpio y su tablero | Proveedor certificado | 2ª | 4 –8 |
| Control de acceso y custodia | Guardia, credenciales, registro de visitas, CCTV | Todos, al entrar | 1ª | 8 –12 |
| Sala de UPS y baterías | Respaldo de energía y banco de baterías | Eléctrico y proveedor | 2ª | 10 –20 |
| Sala o patio de generador | Grupo electrógeno y estanque de combustible | Proveedor, con permiso | Ext. | 15 –30 |
| Acometida de comunicaciones | Llegada de enlaces y equipos de los operadores | Proveedores externos | 2ª | 8 –12 |
| Acometida eléctrica | Empalme, tablero general, transferencia | Eléctrico autorizado | 2ª | 8 –15 |
| Sala de reparación (taller) | Diagnóstico y armado fuera de la sala blanca | Técnicos | 1ª | 10 –15 |
| Bodega de insumos | Repuestos, medios, herramientas, consumibles | Operación | 1ª | 8 –12 |
| Sala de reuniones | Coordinación, proveedores, auditorías | Con invitación | 1ª | 12 –18 |
| Baños y servicios | Fuera del perímetro técnico, sin muro común | Todos | Fuera | — |

---

<a id="diapositiva-28"></a>

## Diapositiva 28 · ▶ SECCIÓN 3 · Opciones de distribución

**3**

**Opciones de distribución**

El mismo programa de recintos se puede ordenar de muchas maneras. Elegir una y saber por qué es la mitad del trabajo.

- Cuatro escalas de sala
- Las holguras que hay que respetar
- Cuatro esquemas de racks
- Cómo dibujar el plano
- Cuatro formas del recinto
- Ficha técnica

---

<a id="diapositiva-29"></a>

## Diapositiva 29 · La pregunta de la sección

**LA PREGUNTA DE LA SECCIÓN**

**No hay un plano correcto. Hay planos justificados y planos copiados.**

La misma lista de recintos admite media docena de distribuciones. Lo que se evalúa no es cuál eligieron, sino que hayan mirado más de una y sepan qué ganaron y qué perdieron.

---

<a id="diapositiva-30"></a>

## Diapositiva 30 · Primero: ¿de qué tamaño es su sala?

> 🖼️ **Contenido gráfico:** mapa de la zona Valparaíso–Santiago (Quilpué, Limache, Quilicura, Santiago, Puente Alto) para ubicar los datacenters de ejemplo.

---

<a id="diapositiva-31"></a>

## Diapositiva 31 · Ejemplos - SONDA

> 🖼️ **Contenido gráfico:** vista aérea del Datacenter SONDA en Quilicura.

---

<a id="diapositiva-32"></a>

## Diapositiva 32 · Ejemplo - SONDA

> 🖼️ **Contenido gráfico:** cuatro plantas arquitectónicas del datacenter de SONDA, con las salas de racks y los recintos de apoyo.

---

<a id="diapositiva-33"></a>

## Diapositiva 33 · Ejemplo - Google

> 🖼️ **Contenido gráfico:** vista aérea de un datacenter de Google (dos grandes naves con equipos de clima y generación en el perímetro).

---

<a id="diapositiva-34"></a>

## Diapositiva 34 · Ambos

> 🖼️ **Contenido gráfico:** vista aérea donde se ven ambos datacenters (SONDA y Google) para comparar escalas.

---

<a id="diapositiva-35"></a>

## Diapositiva 35 · Data center

Visita virtual de DataCenter de SONDA

https://www.sonda.com/tourvirtual/datacenter-kudos/

---

<a id="diapositiva-36"></a>

## Diapositiva 36 · Pausa · trabajo en grupo

**PAUSA · TRABAJO EN GRUPO**

**El plano de su caso**

**1**

¿En cuál de las cuatro escalas cae su sala, y de qué número salió esa respuesta: de las U contadas o de una impresión?

**2**

¿Qué esquema de racks eligieron y qué perdieron al elegirlo? Toda distribución gana algo y pierde algo: escriban las dos cosas.

**3**

Si el mandante les dice que sólo hay 45 m² disponibles: ¿qué recintos fusionan primero y qué riesgo están aceptando al hacerlo?

---

<a id="diapositiva-37"></a>

## Diapositiva 37 · ▶ SECCIÓN 4 · Seguridad, acceso y monitoreo

**4**

**Seguridad, acceso y monitoreo**

Bloquear el acceso a los servidores y a sus contenidos es el primer elemento de un centro de datos. Todo lo demás viene después.

- Las cuatro capas
- El gas que puede matar
- Esclusa y antipassback
- Quién contesta a las 3 AM
- Cámaras y sensores
- Ficha técnica

---

<a id="diapositiva-38"></a>

## Diapositiva 38 · La pregunta de la sección

**LA PREGUNTA DE LA SECCIÓN**

**¿Quién contesta a las tres de la mañana?**

Toda alarma necesita destinatario, canal, tiempo de respuesta comprometido y procedimiento escrito. Si no lo tiene, es sólo un pitido en una sala vacía.

---

<a id="diapositiva-39"></a>

## Diapositiva 39 · La seguridad es por capas

Ninguna barrera es infalible. Lo que importa es que sean varias y de naturaleza distinta.

No se recomienda que la sala comparta espacio con una oficina administrativa: además del riesgo de acceso, las personas y sus contaminantes dañan los equipos.

> 🖼️ **Contenido gráfico — Capas concéntricas de seguridad:** 1 · Perímetro (cierre, portón, iluminación) → 2 · Edificio (recepción, guardia, credencial) → 3 · Sala (esclusa, biometría, registro) → 4 · Rack (llave y bitácora) → en el centro, **los datos**.

---

<a id="diapositiva-40"></a>

## Diapositiva 40 · Cómo se cruza cada puerta

A mayor profundidad, más factores de autenticación y más registro.

**1ª LÍNEA**

**Guardia y credencial**

Acceso al edificio o al piso. Libro de visitas con nombre, empresa, motivo y horas de entrada y salida.

**Esclusa (mantrap)**

**2ª LÍNEA**

**Tarjeta con perfil**

Zona técnica. Cada credencial habilita recintos determinados y caduca el día que termina el trabajo del contratista.

**Antipassback**

**3ª LÍNEA**

**4ª LÍNEA**

**Doble factor y esclusa**

Sala de servidores. Tarjeta más biometría, esclusa con antipassback, acompañamiento y bitácora de la tarea.

**La puerta del rack**

Cerradura por gabinete. Es la última barrera antes del equipo, y en ambientes compartidos también se registra.

**Nadie solo, todo registrado**

Dos puertas enclavadas: la segunda no abre hasta que la primera cerró. Impide que entren dos personas con una sola credencial.

La credencial que entró no puede volver a entrar sin haber salido. Es lo que corta el préstamo de tarjetas.

El externo entra acompañado, siempre. Y la puerta se cierra sola, con alarma si queda abierta más de X segundos.

Para la propuesta: el control de acceso es un ítem cotizable —lectoras, controladoras, software, credenciales— y su operación es OPEX. Declaren cuántas puertas controladas contempla su diseño.

---

<a id="diapositiva-41"></a>

## Diapositiva 41 · Los sentidos de la sala

El monitoreo ambiental es lo que evita que un problema chico se convierta en uno caro.

**Sensores ambientales**

Aire exclusivo de la sala: que nadie cambie el termostato.

Humedad: condensación por debajo, estática por arriba.

Humo por aspiración (VESDA) y detectores puntuales.

Agua bajo el piso técnico y en la bandeja de condensado.

Oxígeno bajo, en salas con extinción por gas.

Puerta abierta, vibración y presencia fuera de horario.

**Cámaras y registro**

Ver la sala a distancia antes de entrar.

Cobertura: cada puerta y los dos pasillos.

Grabación con fecha y hora; retención declarada.

Que funcionen con la sala a oscuras.

El video es prueba: se custodia y se controla.

Integrado al control de acceso: la puerta marca el video.

Un solo tablero: un sistema DCIM o BMS reúne energía, clima, acceso, video y estado de racks en una sola vista. Es lo que se ve en la sala de monitoreo, y es un ítem cotizable.

---

<a id="diapositiva-42"></a>

## Diapositiva 42 · Sección 4 · lo que hay que entender

**SECCIÓN 4 · LO QUE HAY QUE ENTENDER**

**El sistema que salva los equipos puede matar a quien quedó adentro.**

El agua destruye la electrónica, así que no se apaga con agua: se apaga con gas. Y el gas apaga el fuego quitándole el oxígeno.

---

<a id="diapositiva-43"></a>

## Diapositiva 43 · La secuencia de una descarga

Por eso hay preaviso, tiempo de evacuación y botón de aborto.

> 🖼️ **Contenido gráfico — Secuencia de una descarga de extinción:**
>
> 1. **0 s · Detección cruzada:** dos sensores independientes.
> 2. **+2 s · Prealarma:** sirena y luz estroboscópica.
> 3. **+30 s · Evacuación:** botón de aborto disponible.
> 4. **Descarga · Agente limpio:** sofoca en menos de 10 segundos.
> 5. **Después · Corte de clima:** para retener la concentración.
> 6. **Al final · Ventilación forzada:** antes de volver a entrar.
>
> *NFPA 2001 · NFPA 75 — señalética, capacitación y simulacro no son opcionales. Nunca rociadores de agua sobre equipos energizados.*

---

<a id="diapositiva-44"></a>

## Diapositiva 44 · Agentes de extinción y control de acceso · ficha técnica

Para elegir el agente hay que mirar la columna del medio, no el precio.

| Agente | Cómo apaga | Riesgo para las personas | Uso típico |
|---|---|---|---|
| Agua (rociadores) | Enfría | Bajo | Prohibido sobre equipos energizados; sólo en zonas de apoyo |
| FM-200 / HFC-227ea | Absorbe calor, químico | Tolerable a concentración de diseño; se evacúa igual | Salas pequeñas y medianas |
| Novec 1230 | Absorbe calor | Margen de seguridad amplio; se evacúa igual | Alternativa moderna, menor impacto ambiental |
| IG-541 / IG-55 (inertes) | Baja el oxígeno al 12–14% | Alto: atmósfera no respirable de forma sostenida | Salas grandes; exige evacuación estricta |
| CO₂ | Desplaza el oxígeno | Letal. No se usa en recintos ocupables | Sólo equipos cerrados sin presencia humana |

| Línea | Mecanismo | Registro |
|---|---|---|
| 1ª · edificio | Guardia, credencial visible, libro de visitas | Nombre, empresa, motivo, hora de entrada y salida |
| 2ª · zona técnica | Tarjeta de proximidad con perfil por recinto | Traza electrónica por persona y por puerta |
| 3ª · sala | Doble factor y esclusa con antipassback | Traza, acompañamiento y bitácora de tarea |
| 4ª · rack | Llave o cerradura electrónica por gabinete | Bitácora con número de rack y U intervenida |

Lo que se cotiza y casi nunca aparece: detección cruzada de dos sensores, tablero de control, sirena y luz estroboscópica, botón de aborto, señalética, capacitación, simulacro anual y recarga del agente.

---

<a id="diapositiva-45"></a>

## Diapositiva 45 · ▶ SECCIÓN 5 · Energía y clima

**5**

**Energía y clima**

Los dos subsistemas que explican la mayoría de las caídas y buena parte del costo. Se diseñan antes que los servidores.

- La cadena eléctrica
- Pasillo frío y caliente
- UPS, baterías y generador
- Tecnologías de clima y free cooling
- El calor es la potencia
- Piso técnico y ficha técnica

---

<a id="diapositiva-46"></a>

## Diapositiva 46 · Escenario

**ESCENARIO**

**Se cortó la luz. Tienen diez minutos.**

¿Qué pasa en su sala en esos diez minutos, en qué orden, y quién se entera? Si no pueden responderlo, todavía no diseñaron la energía.

---

<a id="diapositiva-47"></a>

## Diapositiva 47 · La cadena eléctrica

Siete eslabones entre la calle y la fuente del servidor. Cada uno es un punto de falla y una línea del presupuesto.

De nada sirve la doble fuente del servidor si ambas PDU cuelgan del mismo UPS. La redundancia se verifica siguiendo el cable.

> 🖼️ **Contenido gráfico — Cadena eléctrica:** Empalme (red pública) → Tablero general → ATS / transferencia (al que se conecta el **Generador**, 8 a 15 s en tomar carga) → UPS (doble conversión) → Tablero de distribución → PDU A / B (en el rack) → Servidor (doble fuente).
>
> *Corte de red → el UPS sostiene sin microcorte → el ATS conmuta → el generador toma la carga.*

---

<a id="diapositiva-48"></a>

## Diapositiva 48 · Qué protege cada eslabón

Y qué pasa exactamente cuando falla.

| Eslabón | Qué hace | Si falla | Cómo se protege |
|---|---|---|---|
| Empalme | Trae la energía de la distribuidora | Se corta todo el suministro | Generador; en instalaciones mayores, doble alimentador |
| Tablero general | Protege y reparte | Cae toda la instalación | Protecciones selectivas y termografía periódica |
| Transferencia (ATS/TTA) | Conmuta entre red y generador | El generador no toma la carga | Prueba mensual con carga real |
| UPS | Filtra y sostiene sin corte | Corte inmediato de los equipos | Configuración N+1 y bypass manual |
| PDU del rack | Distribuye en el gabinete | Cae el rack completo | Dos PDU, alimentación A y B por caminos distintos |
| Fuente del equipo | Alimenta el servidor | Cae el equipo | Doble fuente conectada a A y a B |

Complementos que se cotizan y casi nunca aparecen: malla de puesta a tierra, protección contra sobretensiones, pararrayos si corresponde, y el apagado ordenado y automático de los servidores cuando la batería baja de un umbral.

---

<a id="diapositiva-49"></a>

## Diapositiva 49 · Tres equipos, tres ventanas de tiempo

El UPS cubre segundos. El generador cubre horas. Y si ninguno alcanza, el apagado ordenado.

**0 A 10 SEGUNDOS**

**UPS**

Sostiene la carga sin corte perceptible y además filtra la energía.

- Standby: para puestos de trabajo, no para una sala. · Línea interactiva: salas muy pequeñas. · Doble conversión (on-line): la única aceptable acá.

Siempre con bypass manual, para poder mantenerlo sin apagar la sala.

**10 SEG A VARIAS HORAS**

**Generador**

Toma la carga por la transferencia automática, típicamente entre 8 y 15 segundos después del corte.

- Debe cubrir el clima, no sólo los servidores. · Estanque dimensionado en horas: 8, 12 o 24. · Contrato de reabastecimiento para cortes largos. · Prueba mensual con carga real y bitácora firmada.

**EL ELEMENTO OLVIDADO**

**Banco de baterías**

Es lo que realmente entrega la autonomía, y condiciona el recinto:

- Plomo VRLA: más barato, más pesado, 3 a 5 años, hidrógeno. · Litio LFP: más caro, la mitad de peso y volumen, 8 a 10 años.

Exige ventilación, control de temperatura y losa verificada.

---

<a id="diapositiva-50"></a>

## Diapositiva 50 · La relación que más se olvida

**LA RELACIÓN QUE MÁS SE OLVIDA**

**1 kW eléctrico consumido = 1 kW de calor a sacar**

≈ 3.412 BTU/h. Un aire de confort de 12.000 BTU no alcanza para un solo rack medianamente poblado — y es exactamente lo que uno encuentra en las salas improvisadas.

---

<a id="diapositiva-51"></a>

## Diapositiva 51 · De dónde viene el calor

La carga térmica no es sólo la de los servidores: hay que sumar todo lo que disipa dentro del recinto.

| Fuente de calor | Cuánto aporta | Comentario |
|---|---|---|
| Equipamiento en los racks | Igual a su consumo eléctrico | Es el 85-90% de la carga en una sala bien hecha |
| UPS y pérdidas de distribución | 3% a8% de la carga TI | Menor si el UPS está en recinto propio y ventilado |
| Iluminación | 10 a 15 W/m² | Poco, pero se suma; con sensores de presencia baja aún más |
| Personas | ≈ 100 W por persona | Marginal, porque la sala está vacía casi siempre |
| Envolvente: muros, techo, radiación | Depende del clima y la orientación | En Valparaíso es bajo; en el norte cambia la ecuación |
| Holgura de crecimiento | 20% a 30% | El clima se dimensiona para la sala llena, no para la de hoy |

**Rangos de operación**

ASHRAE TC 9.9 recomienda 18 a 27 °C y 40% a 60% de humedad relativa en la entrada de aire de los equipos. La medición que importa es la de la toma del servidor, no la del muro.

**Clima de precisión, no de confort**

Un equipo de confort está hecho para personas: apaga y prende, no controla humedad y no trabaja 8.760 horas al año. Se necesita clima de precisión, con redundancia N+1.

---

<a id="diapositiva-52"></a>

## Diapositiva 52 · Pasillo frío y pasillo caliente

Ordenar el aire es la mejora más barata que existe. Y la más ignorada.

Confinar el pasillo y poner tapas ciegas cuesta poco y suele bajar el consumo de clima entre 15% y 30%. Es el ítem con mejor relación costo-beneficio de la sala.

---

<a id="diapositiva-53"></a>

## Diapositiva 53 · Pasillo frío y pasillo caliente

> 🖼️ **Contenido gráfico:** render de una sala con filas de racks enfrentadas (pasillo frío / pasillo caliente). Video: https://www.youtube.com/watch?v=aUb0_75y5SY&t=1s

---

<a id="diapositiva-54"></a>

## Diapositiva 54 · Lo que ordena el aire y lo que lo arruina

Cuatro cosas que hay que hacer siempre y cuatro que echan a perder el mejor diseño térmico.

**Lo que hay que hacer siempre**

Tapas ciegas en toda U vacía del rack: sin ellas el aire caliente recircula por dentro del gabinete.

Sellar los pasos de cables del piso técnico con obturadores.

Baldosas perforadas sólo en el pasillo frío, y en la cantidad calculada.

Confinar el pasillo —frío o caliente— con techo y puertas: mejora el rendimiento sin agrandar el equipo.

**Lo que arruina el diseño térmico**

Todos los racks mirando hacia el mismo lado.

U vacías sin tapa y bandejas de cables que bloquean la descarga trasera.

Cajas, sillas o material almacenado en el pasillo frío.

Bajar el termostato a 16 °C «por si acaso»: gasta más y no resuelve la recirculación.

El confinamiento de pasillo y las tapas ciegas cuestan poco y suelen bajar el consumo de clima entre 15% y 30%. Es el ítem con mejor relación costo-beneficio de toda la sala.

---

<a id="diapositiva-55"></a>

## Diapositiva 55 · Cuatro maneras de sacar el calor

La densidad por rack decide, no el catálogo del proveedor.

> 🖼️ **Contenido gráfico — Cuatro tecnologías de clima según densidad:**
>
> | Densidad | Tecnología | Descripción |
> |---|---|---|
> | Hasta 5 kW/rack | Expansión directa (DX) | Unidad interior y condensadora afuera. Lo habitual en salas medianas |
> | 5 a 15 kW/rack | In-row y puerta trasera | Enfría donde se genera el calor. Muy eficiente, más equipos que mantener |
> | Salas grandes | Agua helada (chiller) | Planta central que enfría agua. Permite free cooling; agua dentro del edificio |
> | Sobre 30 kW/rack | Refrigeración líquida | Placa fría o inmersión. Hoy, cómputo de alto rendimiento e IA |
>
> *Clima de precisión, no de confort: 8.760 horas al año, con control de humedad y redundancia N+1.*

---

<a id="diapositiva-56"></a>

## Diapositiva 56 · Free cooling y lo que hay que declarar

Aprovechar el clima del lugar es un argumento económico, no sólo ambiental.

**Free cooling: aprovechar el clima**

Cuando el aire exterior está más frío que el de retorno, se usa para enfriar y se apaga el compresor.

En la zona central de Chile la temperatura lo permite buena parte del año, sobre todo de noche.

Baja el PUE y por lo tanto la cuenta de la luz: entra directo en el OPEX del flujo de caja.

Exige filtración y control de humedad del aire que entra.

**Lo que hay que declarar del clima**

Carga térmica calculada en kW y la configuración de redundancia (N, N+1, N+2).

Tecnología elegida y por qué, con la densidad por rack como argumento.

Temperatura y humedad objetivo, medidas en la toma de aire del equipo.

Qué pasa si el clima se cae por completo: en cuántos minutos hay que apagar.

---

<a id="diapositiva-57"></a>

## Diapositiva 57 · El suelo y el cielo de la sala

Piso técnico o bandejas aéreas. Las dos son válidas; lo que no es válido es la alfombra.

**Piso técnico (falso o elevado)**

Altura libre de 30 a 60 cm; menos de 30 cm no sirve para distribuir aire.

Baldosas removibles sobre pedestales, con carga puntual declarada.

Se usa como plenum de aire frío y como canalización.

Exige sellado de todos los pasos y detección de agua debajo.

Requiere rampa o escalón de acceso, que hay que dibujar en el plano.

**Distribución superior (sin piso falso)**

Bandejas aéreas: energía por una, datos por otra, separadas.

Impulsión por ductos o unidades en fila entre los racks.

Más barato y más fácil de inspeccionar: hoy es lo habitual.

Exige altura libre suficiente y buen orden: todo queda a la vista.

El piso, aunque no sea técnico, debe ser antiestático y sin alfombra.

Dato de estructura que casi nadie revisa: un rack lleno pesa entre 500 y 900 kg y un banco de baterías puede superar la tonelada. La resistencia de la losa y la ruta de ingreso de los equipos son parte del diseño.

---

<a id="diapositiva-58"></a>

## Diapositiva 58 · Dimensionar la carga eléctrica y térmica · ficha técnica

El ejemplo completo de una sala de ocho racks. El método importa más que los números.

| Paso | Cálculo | Resultado |
|---|---|---|
| 1 · Potencia por rack | Se declara según el equipamiento: 3 kW por rack de cómputo estándar | 3 kW / rack |
| 2 · Racks poblados | 8 racks: 6 con carga plena y 2 parciales | ≈ 21 kW |
| 3 · Carga TI de diseño | Se agrega 25% de holgura para crecimiento a tres años | 26 kW |
| 4 · Capacidad de UPS | Carga TI dividida por 0,8 de factor de utilización | 33 kVA → UPS de 40 kVA |
| 5 · Autonomía | Lo que tarde el generador en tomar carga, más margen de apagado | 10 min con generador · 30 sin él |
| 6 · Carga total del sitio | TI + clima + iluminación + apoyo, con PUE 1,7 | ≈ 44 kW |
| 7 · Generador | Cubre TI y clima, más la partida de motores | 60 kVA |
| 8 · Potencia a contratar | Se declara ante la distribuidora con margen | ≈ 55 kW |

Carga térmica: equipamiento (igual a su consumo) + UPS y pérdidas (3-8%) + iluminación (10-15 W/m²) + personas (≈100 W c/u) + envolvente + 20-30% de holgura. ASHRAE TC 9.9: 18 a 27 °C y 40 a 60% HR medidos en la toma de aire del equipo, no en el muro.

---

<a id="diapositiva-59"></a>

## Diapositiva 59 · Pausa · trabajo en grupo

**PAUSA · TRABAJO EN GRUPO**

**La energía y el clima de su caso**

**1**

Con el equipamiento que tienen pensado, ¿cuánta potencia por rack están asumiendo y de dónde sale ese número?

**2**

¿Cuánto tiempo puede estar caído el sistema de su mandante antes de que el negocio duela de verdad? Con esa respuesta decidan si cotizan generador o sólo UPS.

**3**

Si se corta la luz y el generador no parte: ¿qué ocurre en los primeros diez minutos y quién se entera?

---

<a id="diapositiva-60"></a>

## Diapositiva 60 · ▶ SECCIÓN 6 · Rack y cableado

**6**

**Rack y cableado**

La unidad de medida de esta industria es la U. Todo lo que se compra, se cotiza y se dibuja se cuenta en unidades de rack.

- La U y qué se cuenta en U
- Cableado estructurado
- La elevación del rack
- Topología y etiquetado
- Tipos de gabinete
- Cuántos racks necesita

---

<a id="diapositiva-61"></a>

## Diapositiva 61 · La elevación del rack

Este dibujo, hecho para cada gabinete, es lo que se espera ver en el informe.

**ARRIBA**

**Donde llega la red**

Patch panels de fibra y cobre: ahí termina el cableado estructurado y empieza el equipo activo.

**AL MEDIO**

**El cómputo**

Los servidores van a la altura del pecho: es lo que más se saca y se repone, y se manipula sin agacharse.

**AL FONDO**

**La energía**

UPS y baterías en la base, siempre. Es lo más pesado del rack y no se monta arriba.

**ALTO**

**Los activos de red**

Switches y firewall justo bajo los paneles. Latiguillos cortos —bajo 1,5 m—, ordenados y fáciles de trazar.

**ABAJO**

**El almacenamiento**

**Storage y respaldo: pesados, se mueven poco y su peso baja el centro de gravedad del gabinete.**

**Y SIEMPRE**

**Tapas ciegas y 20% libre**

Toda U vacía lleva tapa ciega, o el aire caliente recircula por dentro del gabinete. Y dos PDU verticales, A y B, en costados opuestos.

---

<a id="diapositiva-62"></a>

## Diapositiva 62 · Todo se mide en U

Una U son 44,45 milímetros. No es una convención simpática: es la razón por la que todo calza con todo.

> 🖼️ **Contenido gráfico:** esquema de un servidor de 1U montado entre rieles de 19 pulgadas. Cifras clave: **44,45 mm** (exactamente 1,75 pulgadas) · **42 U** (el gabinete estándar, ~2 metros) · **1.100 mm** (la profundidad que hoy hace falta) · **75%** (ocupación máxima razonable). *Todo el equipamiento del mundo se fabrica en múltiplos de esa altura.*

---

<a id="diapositiva-63"></a>

## Diapositiva 63 · La elevación del rack

Este dibujo, hecho para cada gabinete, es lo que se espera ver en el informe.

> 🖼️ **Contenido gráfico:** (1) elevación de un armario bastidor de 42U con, de arriba abajo: patch panel, enrutador, panel de conexiones, monitor, teclado, servidores, matriz de discos, regleta, SAI (UPS) y regleta (fuente: rackonline.es). (2) Comparación de densidad por rack: 1U rackmount 30–42 unidades · 2U rackmount 15–20 · chasis GPU 4U 8–10 · chasis blade, hojas agrupadas (fuente: gpuservercase.com).

---

<a id="diapositiva-64"></a>

## Diapositiva 64 · Qué se cuenta en U

| Se cuentaen U | Ejemplo | Consecuencia práctica |
|---|---|---|
| Servidor de rack | 1U, 2U o 4U según discos y expansión | Define cuántos caben por gabinete |
| Switch | 1U casi siempre | Uno o dos por rack en topología ToR |
| Storage | 2U a 4U la controladora, más las bandejas de discos | Es lo que más U consume después de los servidores |
| UPS de rack | 2U a 6U, más las baterías | Va abajo por peso |
| Patch panel | 1U cada 24 puertos | Se calcula desde el número de puntos de red |
| Organizador de cables | 1U entre cada par de equipos activos | Se olvida siempre y después no hay espacio |

---

<a id="diapositiva-65"></a>

## Diapositiva 65 · El chasis: cuántos servidores caben de verdad

El chasis es la caja física del servidor. Define su alto en U, su refrigeración y cuántos entran por rack.

**1U**

**El caballo de batalla**

Chasis de 4,45 cm de alto. Entran 30 a 42 por rack de 42U.

Poco espacio interno: discos pequeños, ventiladores chicos y ruidosos, poca expansión.

Muchos servicios chicos e iguales;

**2U**

**El equilibrado**

El doble de alto: 15 a 20 por rack.

Más discos, más tarjetas, mejor flujo de aire. Es el formato más usado en salas medianas.

Opción por defecto: almacenamiento local, expansión y mantención cómoda

**4U**

**7U**

**El de GPU**

**Chasis blade**

Sólo 8 a 10 por rack. Aloja de 8 a 16 tarjetas GPU y fuentes de 2.000 W o más.

Un chasis de 7U con varias hojas: 14 a 28 hojas por rack.

Aquí ya se habla de refrigeración líquida.

Analítica, visión por computador o modelos; alta densidad eléctrica

Comparten energía, ventilación y red desde el mismo chasis.

Consolidación fuerte en poca superficie, con energía y red compartidas

---

<a id="diapositiva-66"></a>

## Diapositiva 66 · No todos los racks sirven para lo mismo

Y los accesorios no son opcionales: son parte del esquema de seguridad y del térmico.

**CERRADO**

**Gabinete con puertas**

Puertas perforadas delante y detrás, laterales removibles, cerradura. El estándar para servidores.

**ABIERTO**

**Rack de postes**

Sin puertas ni laterales. Barato y accesible, pero sin control de acceso ni de aire. Para salas de comunicaciones internas.

**Se cotiza sí o sí**

Dos PDU verticales por gabinete, alimentación A y B, con medición si se puede.

Tapas ciegas para todas las U libres y organizadores horizontales.

Rieles y kits de montaje: no vienen con el servidor en todas las marcas.

**MURAL**

**Gabinete de pared**

6U a 18U colgado del muro, poco fondo. Para puntos de distribución en pisos o sucursales.

**ESPECIAL**

**Gabinete de operadores**

Reservado a los equipos de cada proveedor de enlace, con llave propia. Va en la sala de acometida.

**Arruina la instalación**

Gabinete de 800 mm de fondo para servidores que necesitan 1.100 mm. Rack no anclado: el marco debe atornillarse al piso para que no vuelque.

Puertas que no abren porque el rack quedó pegado al muro o a la fila vecina.

---

<a id="diapositiva-67"></a>

## Diapositiva 67 · Cableado: disciplina de tráfico

Separar datos de corriente, rotular en ambos extremos y respetar la curvatura de la fibra.

**REGLA 1**

**Datos y corriente, separados**

Bandejas distintas o separación física declarada —del orden de 20 cm—. Si tienen que cruzarse, que sea a 90°. Es un ítem de canalización que casi nadie presupuesta.

**REGLA 3**

**Curvatura protegida**

La fibra tiene radio mínimo de curvatura. Doblarla en la esquina de una bandeja atenúa la señal o quiebra el núcleo, y la falla aparece meses después.

**REGLA 2**

**Rotulado en ambos extremos**

Cada patch cord con su identificador normalizado, del tipo R01-U38-P12. Etiquetar los dos extremos ahorra tiempo y dinero cuando hay que intervenir de noche.

**REGLA 4**

**Certificación con informe**

El cableado nuevo se certifica con equipo y se entrega el informe. Es un entregable del proyecto y tiene costo: cotícenlo.

Nomenclatura declarada + planilla o DCIM con qué ocupa cada U y a qué puerto va cada cable, actualizada el mismo día. Colores por función: gestión, producción, respaldo, DMZ. Topología ENI → MDA → HDA → ZDA → EDA según ANSI/TIA-942.

---

<a id="diapositiva-68"></a>

## Diapositiva 68 · Topología del cableado y etiquetado

ANSI/TIA-942 ordena la sala en distribuidores. Y todo cable se rotula en los dos extremos.

**ENI**

**Entrada de servicios**

**MDA**

**Distribuidor principal**

Donde llegan los enlaces de los operadores. Es la sala de acometida de comunicaciones.

El núcleo del cableado: de aquí sale todo hacia el resto de la sala.

**ToR o EoR: dónde va el switch**

ToR (Top of Rack): un switch por gabinete. Cables cortos dentro del rack y troncal de fibra al distribuidor.

EoR (End of Row): un switch grande al final de la fila. Menos equipos que administrar, mucho más cableado horizontal.

En una sala de 4 a 12 racks, ToR con troncal de fibra es lo más simple de operar y de crecer.

**HDA / ZDA**

**Distribuidor horizontal y de zona**

Un punto por zona o por fila de racks. En una sala chica se funden con el MDA.

**EDA**

**Área de equipo**

El rack mismo: donde el cableado estructurado termina en el patch panel.

**Etiquetado y documentación**

Nomenclatura declarada: sala-rack-U-puerto. Por ejemplo SS1-R03- U24-P07.

Etiqueta en los dos extremos de cada cable, con rotuladora.

Planilla o DCIM con qué ocupa cada U y a qué puerto va cada cable, actualizada el mismo día.

Colores por función: gestión, producción, respaldo, DMZ.

---

<a id="diapositiva-69"></a>

## Diapositiva 69 · Medios de cableado · ficha técnica

Qué cable para qué distancia y a qué velocidad. Cotizar «Cat6» sin decir para qué no significa nada.

| Medio | Velocidad y distancia | Dónde se usa |
|---|---|---|
| Cat 6 U/UTP | 1 Gbps hasta 100 m · 10 Gbps hasta 55 m | Horizontal a puestos y equipos de baja demanda |
| Cat 6A F/UTP | 10 Gbps hasta 100 m, mejor inmunidad | Estándar recomendado hoy para cableado nuevo |
| Cat 7 / Cat 8 | 25 y 40 Gbps a distancias cortas (30 m) | Interconexión dentro del rack o entre racks vecinos |
| Fibra multimodo OM4/OM5 | 10 a 100 Gbps hasta 150–400 m | Troncales entre racks y entre salas del edificio |
| Cables MPO/MTP | Troncal preconectorizado de 12 o 24 hilos | Troncales de alta densidad entre distribuidores |
| Fibra monomodo OS2 | 10 a 400 Gbps, kilómetros | Salida al exterior y enlaces de operadores |
| DAC / twinax | 10 a 100 Gbps hasta 5–7 m | Servidor a switch dentro del mismo rack |

Separación obligatoria entre energía y datos, radio mínimo de curvatura respetado en la fibra, y certificación con informe entregable. Los tres son ítems con costo que hay que cotizar.

---

<a id="diapositiva-70"></a>

## Diapositiva 70 · Cuántos racks necesita su caso · ficha técnica

El cálculo en ocho líneas. De aquí salen los gabinetes, los metros cuadrados y la potencia.

| Paso | Cómo se calcula | Ejemplo |
|---|---|---|
| 1 · U de cómputo | Servidores y nodos del clúster | 6 nodos de 2U = 12 U |
| 2 · U de almacenamiento | Controladora, bandejas y respaldo | 4U + 4U + 4U = 12 U |
| 3 · U de red y seguridad | Switches, firewall, balanceador, consola | 6 U |
| 4 · U de infraestructura | Patch panels, organizadores, PDU, UPS de rack | 14 U |
| 5 · Subtotal | Suma de los cuatro pasos anteriores | 44 U |
| 6 · U utilizables por gabinete | 42U menos 25-30% de reserva de crecimiento | ≈ 30 U por rack |
| 7 · Racks necesarios | Subtotal ÷utilizables, redondeado hacia arriba | 44 ÷30 → 2 racks |
| 8 · Racks del diseño | Se agrega el gabinete de operadores y el de crecimiento | 4 gabinetes en el plano |

De este cálculo salen tres números que se usan en toda la propuesta: cuántos gabinetes se compran, cuántos metros cuadrados ocupa la sala y cuánta potencia hay que alimentar y enfriar. Es el punto donde el diseño técnico y el presupuesto se tocan.

---

<a id="diapositiva-71"></a>

## Diapositiva 71 · ▶ SECCIÓN 7 · Servidores, comunicaciones y storage

**7**

**Servidores, comunicaciones y storage**

Lo que va adentro de los racks. Tres familias de tecnología y, en cada una, una decisión que hay que justificar.

- Formatos de servidor
- La base de datos
- Virtualización y contenedores
- La red, los equipos y los enlaces
- Almacenamiento, RAID y respaldo
- Propia, colocation o nube

---

<a id="diapositiva-72"></a>

## Diapositiva 72 · Antes de elegir marcas

**ANTES DE ELEGIR MARCAS**

**El formato del servidor es una decisión de infraestructura.**

Blade e hiperconvergido concentran mucha potencia por U. Eso cambia el diseño térmico y el eléctrico de la sala entera, no sólo la línea del presupuesto.

---

<a id="diapositiva-73"></a>

## Diapositiva 73 · Cuatro formatos

Y el número que hay que declarar sí o sí: la potencia eléctrica por rack.

**TORRE**

**Servidor de piso**

Gabinete propio. Barato y silencioso, pero no se monta en rack y ocupa superficie.

Una o dos máquinas en una oficina; no en una sala de servidores.

**RACK**

**1U, 2U, 4U**

El formato estándar. Se monta en rieles, se mantiene desde el frente y se cambia sin sacar el rack.

Es la elección por defecto para una sala de 4 a 12 racks.

**BLADE**

**Chasis con hojas**

Un chasis de 6U a 10U aloja varias hojas y comparte energía, ventilación y red.

Muchos servidores en poco espacio; exige alta densidad eléctrica y térmica.

**Hiperconvergido**

Nodos que integran cómputo, almacenamiento y virtualización en una plataforma.

Simplifica la operación y crece agregando nodos iguales.

**HCI**

| Qué se dimensiona | Cómo se justifica en la propuesta |
|---|---|
| Núcleos de CPU | Desde la carga concurrente estimada y el tipo de aplicación, con holgura declarada |
| Memoria RAM | Desde el número de máquinas virtuales o contenedores y su consumo unitario |
| Disco e IOPS | Desde el volumen de datos a tres años y el patrón de acceso de la base de datos |
| Red y fuentes | Dos interfaces en distintos switches; dos fuentes en alimentaciones A y B |

---

<a id="diapositiva-74"></a>

## Diapositiva 74 · Virtualizar es lo que hace posible su sala

Menos servidores físicos, menos U, menos kW, menos clima. Y más riesgo concentrado.

**Máquina virtual**

Cada máquina lleva su propio sistema operativo completo.

Tipo 1 (bare metal): ESXi, Proxmox VE, Hyper-V, KVM, XCP-ng.

Tipo 2 corre sobre un sistema operativo: laboratorio, no sala.

Aísla del todo y permite migrar en caliente sin apagar servicios.

**Contenedor**

Comparte el núcleo y empaqueta sólo la aplicación.

Arranca en segundos y pesa mucho menos que una VM.

Docker empaqueta; Kubernetes, Swarm u OpenShift orquestan.

Aísla menos: exige más cuidado en seguridad.

**El clúster mínimo son tres nodos**

Con dos no hay dónde mover las cargas cuando uno cae o se mantiene, y el ahorro se paga con indisponibilidad.

**El licenciamiento se cotiza aparte**

Cuenta por socket, por núcleo o por nodo según el producto. Es costo recurrente, y a veces pesa más que el hardware.

**En la práctica conviven**

Contenedores corriendo sobre máquinas virtuales. No es «uno u otro»: es cómo se reparte la carga.

---

<a id="diapositiva-75"></a>

## Diapositiva 75 · Tres formas de guardar el dato

DAS, NAS y SAN no compiten: resuelven problemas distintos.

HDD para capacidad y respaldo · SSD para uso general · NVMe para bases de datos e índices. Casi siempre se combinan por niveles.

> 🖼️ **Contenido gráfico:**
>
> | Tipo | Cómo | Qué es | Cuándo |
> |---|---|---|---|
> | DAS | Directo | Discos dentro del servidor o en una bandeja conectada a él | Simple y rápido; no se comparte |
> | NAS | Por archivos | Un equipo entrega archivos por la red (SMB, NFS) | Fácil de compartir; ideal para respaldo |
> | SAN | Por bloques | Red dedicada de almacenamiento (iSCSI o Fibre Channel) | Es lo que usa un clúster de virtualización |

---

<a id="diapositiva-76"></a>

## Diapositiva 76 · Lo que sigue

**LO QUE SIGUE**

**Anexo técnico**

Los parámetros que hay que declarar, el glosario y las fuentes. No se leen en clase: se usan mientras escriben el informe.

---

<a id="diapositiva-77"></a>

## Diapositiva 77 · Los parámetros que hay que declarar · ficha técnica

Números con unidad. Es lo que hace verificable una propuesta.

| Parámetro | Unidad | Ejemplo de una sala mediana |
|---|---|---|
| Superficie de la sala de servidores | m² | 32 m² útiles, más 45 m² de recintos de apoyo |
| Esquema de distribución | tipo y holguras | Dos filas enfrentadas, 1,2 m al frente y 0,9 m atrás |
| Cantidad de racks y ocupación | gabinetes y % de U | 8 gabinetes de 42U, 68% ocupado |
| Potencia por rack | kW | 3 kW promedio, 5 kW el rack de mayor densidad |
| Carga TI de diseño | kW | 26 kW con 25% de holgura a tres años |
| PUE estimado | adimensional | 1,7 |
| Capacidad y topología del UPS | kVA y configuración | 40 kVA doble conversión, N+1, con bypass |
| Autonomía de respaldo | minutos | 10 min a plena carga, con generador |
| Generador | kVA y horas de estanque | 60 kVA, 12 horas de autonomía |
| Carga térmica y clima | kW y configuración | 30 kW, dos unidades de precisión en N+1 |
| Temperatura y humedad | °C y % HR | 18–27 °C y 40–60% HR en la toma de aire |
| Nivel de disponibilidad objetivo | TIER y % | TIER II, 99,74% comprometido |
| Enlaces | Mbps y proveedores | 2 enlaces de 500 Mbps, proveedores distintos |
| RTO y RPO | horas | RTO 4 h, RPO 1 h |

---

<a id="diapositiva-78"></a>

## Diapositiva 78 · Glosario · ficha técnica

Las siglas que van a encontrar en catálogos y cotizaciones.

**ATS / TTA**

**BMS**

**CRAC / CRAH**

**DAS · NAS · SAN**

**DCIM**

**DMZ**

**EDA · HDA · MDA**

**HCI**

**IOPS**

**MMR**

Transferencia automática entre red y generador

Sistema de gestión del edificio (Building Management)

Equipo de aire de precisión para sala de cómputo

Almacenamiento directo, por archivos, por bloques

Gestión de la infraestructura del centro de datos

Segmento donde se publican los servicios expuestos

Área de equipo, distribuidor horizontal y principal

Infraestructura hiperconvergida

Operaciones de entrada y salida por segundo

Sala de encuentro de operadores

**NOC / SOC**

Centro de operación de red y de seguridad

**PAC / PDU**

Aire de precisión · distribución de energía en el rack

**PUE**

Energía total de la instalación ÷ energía TI

**RTO · RPO**

Tiempo y punto objetivo de recuperación

**SLA · SLO**

Acuerdo y objetivo de nivel de servicio

**ToR · EoR**

Switch en la cima del rack o al final de la fila

**U**

Unidad de rack: 44,45 mm de altura

**UPS**

Fuente de poder ininterrumpida

**VESDA**

Detección temprana de humo por aspiración

**White space**

La sala blanca: el recinto donde están los racks

---

<a id="diapositiva-79"></a>

## Diapositiva 79 · Fuentes y para seguir · ficha técnica

De dónde salieron los datos y adónde ir a buscar los suyos.

**NORMAS**

**Estándares de diseño**

ANSI/TIA-942-C · ASHRAE TC 9.9 · NFPA 75 y NFPA 2001 · Uptime Institute Tier Standard · ISO/IEC 27001 anexo A · ISO 22301

**RECORRIDOS**

**Ver antes de dibujar**

sonda.com/tourvirtual/datacenter-kudos/ datacenter.it (Aruba, Roma) 3dwarehouse.sketchup.com — «data center»

https://3dwarehouse.sketchup.com/model/1c57e6e6- dbc3-4890-83e3-527fd15bc5b8/DATA-CENTER

https://3dwarehouse.sketchup.com/model/d3060eae- 36a6-43b6-a252-14fd7aa61d98/DATA- CENTER?hl=es#related

**CHILE**

**Normativa aplicable**

NCh Elec. 4/2003 y declaración SEC · NCh 2777 (grupos electrógenos) · NCh 2527 · NCh 3002 · Ley N° 21.719 · DS 594

**PROVEEDORES**

**Catálogos técnicos**

blackbox.com · bticino.cl · equinix.es · logisa.com · y los distribuidores locales de racks, UPS y clima de precision

**DIVULGACIÓN**

**Lectura de entrada**

noxtel.mx — «Descubriendo el centro de datos» hosting.cl/tutoriales/que-es-un-data-center zensitec.com.ar — FM-200 en data centers

**LINK**

https://www.blackbox.com/en-us/products

https://www.bticino.cl/soluciones/soluciones-de-data- center

https://www.equinix.es/products/data-center-services

https://www.logisa.com/diseno-construccion-data- centers

Las imágenes de planos y renders provienen del material del curso y del informe de LATIOS; las ilustraciones técnicas son de elaboración propia para esta clase.

---

<a id="diapositiva-80"></a>

## Diapositiva 80 · Para la próxima sesión

**PARA LA PRÓXIMA SESIÓN**

**«No gana la propuesta que compra el equipo más caro, sino la que sabe justificar cada tornillo.»**

Tarea: el programa de recintos de su caso con superficies, el esquema de distribución elegido y el plano de zonificación con las líneas de acceso. Media plana de texto y un dibujo.
