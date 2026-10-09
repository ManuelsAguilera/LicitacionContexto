# Prompt del loop de mejora de la EDT

Documento de contexto, no es entregable. Se pega tal cual para correr el loop (por ejemplo con `/loop` en modo dinámico, o como instrucción de una sesión nueva). Creado el 2026-10-08. El tablero es `python3 05_Gestion/scripts/ciclo_edt.py` (metas duras H1 a H9 y blandas S1 a S3); la bitácora es `estimacion/23_bitacora_loop_edt.md`.

## Por qué existe

Las revisiones manuales repetían las mismas comprobaciones y cada vuelta movía una regla y rompía otra. El loop tiene una función objetivo única (el tablero), un orden fijo de prioridades (sd-03 > 8/80 > menos paquetes) y una regla de aceptación: un cambio solo entra si no empeora ninguna meta dura.

## Qué significa «cantidad correcta»

No es un número. Es una cadena de trazas: cada cuenta de control y cada paquete cita el elemento del sd-03 de donde viene (caso de uso, RF, resultado del Anexo D, compromiso, obligación, exclusión o sección), y cada elemento del sd-03 tiene al menos un paquete. Si esa cadena está completa y todo paquete de trabajo con horas cumple 8/80 y un mes, la cantidad queda justificada. Para el software, la cantidad la fija la aritmética: 31.850 h con paquetes de hasta 80 h son unos 690 paquetes de trabajo. La EDT tiene dos niveles: cuentas de control (nivel de gestión, hoy 164) y paquetes de trabajo (nivel 8/80, por ola).

## El prompt

```
Eres quien ejecuta un loop de mejora de la EDT del Caso 09 (Only Simple Solutions). Trabajas sobre
80_Artefactos/sd-07_contexto/estimacion/14_edt_corregida.md. No toques [ELISEO]-entregables_edt.md,
guia_edt.md, los .tex ni la carpeta "[BORRAR DESPUES] sd-01". Trabaja en la rama loop/edt.

OBJETIVO
Que la EDT cumpla, a la vez: (1) cada compromiso del sd-03 tiene entregable; (2) cada paquete de
trabajo con horas está entre 8 y 80 h y cabe en un mes; (3) cada cuenta y cada paquete traza a un
elemento del sd-03 y cada elemento del sd-03 tiene al menos un paquete. La cantidad de paquetes es
una CONSECUENCIA: no la persigas ni la recortes.

PRIORIDAD cuando chocan: sd-03 > 8/80 > menos paquetes. Si 8/80 exige más paquetes, se agregan.
Nunca inventes horas, normas ni cifras: lo que no tenga fuente queda «por estimar» o «por definir».

CADA ITERACIÓN (una sola clase de cambio por vez)
1. Corre `python3 05_Gestion/scripts/ciclo_edt.py --json` y guarda el resultado como «antes».
2. Si todas las metas duras pasan en dos iteraciones seguidas, termina con el informe final.
3. Elige UNA clase de infracción, en este orden fijo:
   a) incoherencia con el sd-03 (H1, H2);
   b) cuenta o paquete sin traza, o elemento del sd-03 sin paquete (H6, H7);
   c) paquete de trabajo con más de 80 h (H8);
   d) paquete con menos de 8 h o de más de un mes (H8);
   e) hallazgos firmes del verificador, mapa o cronograma (H3, H4, H5);
   f) duplicados y nombres con varios entregables (S3).
4. Aplica el cambio mínimo que corrija esa clase: dividir (por transacción o por fase), fusionar
   (mismo responsable, misma etapa, un solo entregable), mover (a la rama del servicio dueño),
   renombrar (sustantivo, sin códigos ni hitos) o agregar una cuenta que cubra un compromiso.
   Cada cambio cita el elemento del sd-03 que lo justifica (sección, RF, caso, resultado o compromiso)
   en el atributo origen: de la cuenta. Verifica en sd-03.tex que la cita sea cierta antes de escribirla.
5. Regenera solo lo necesario (mapa, cronograma, horas) y corre el tablero otra vez: «después».
6. ACEPTA el cambio solo si ninguna meta dura que pasaba deja de pasar y la clase elegida mejora.
   Si no, descártalo con `git checkout -- <archivo>` y anota por qué falló.
7. Si aceptas: un commit con el mensaje «Loop EDT, iteración N: <cambio> (<justificación sd-03>)».
8. Registra la iteración en estimacion/23_bitacora_loop_edt.md: N, clase, cambio, justificación,
   métricas antes y después, decisión.

LÍMITES
- Máximo 12 iteraciones. Detente tras 3 iteraciones seguidas sin mejora de la clase elegida.
- Cada 4 iteraciones detente y muéstrame una tabla con los cambios aceptados y descartados; sigue
  solo si te lo apruebo.
- Una cuenta de control puede superar 80 h (planificación gradual de PMBOK 6); el paquete de trabajo
  no. Los paquetes de software se derivan por regla (fase y transacción) y su cantidad es aritmética.
- Los paquetes sin horas no se dan por buenos: quedan «pendientes de planilla» y cuentan en S2.
- No uses más de un cambio estructural por iteración. No regeneres los diccionarios hasta el final.
- Si una cita del sd-03 no existe, no la inventes: deja la cuenta sin traza y márcala como pregunta.

INFORME FINAL
Tablero final, número de cuentas y de paquetes de trabajo con su justificación, cambios
descartados, pendientes humanos (planillas, validación del equipo) y decisiones que requieren al usuario.
```

## Sugerencias para usarlo

1. **Rama dedicada.** `git switch -c loop/edt` antes de empezar; así los commits del loop no se mezclan con los de la rama de trabajo y se pueden descartar enteros.
2. **Primera iteración esperable.** La clase b (H6): hoy 51 cuentas no citan un elemento del sd-03 (sobre todo gestión, arquitectura, infraestructura e implantación). Algunas se justifican con las Bases y no con el sd-03; en ese caso el loop debe dejarlo escrito como pregunta y no forzar una cita.
3. **Una clase de cambio por iteración, con orden fijo.** Evita que arreglar 8/80 deshaga la coherencia.
4. **El software es aritmética.** No esperes que el loop baje los unos 690 paquetes de trabajo del software; lo que mejora es la estructura de las ramas sin horas.
5. **Para cerrar 8/80 fuera del software** hacen falta horas: las planillas de tres valores (`12_plantilla_tres_valores.md` y `21_planilla_ola_1.md`). Sin ellas, el loop informa «pendiente de planilla».
6. **Revisión independiente al final.** Un agente que no vio el loop revisa el tablero y la bitácora, como en G3.
7. **Costo.** El tablero tarda unos tres segundos; el loop completo son unas 12 corridas dobles. Regenerar los diccionarios y el resto al final.
