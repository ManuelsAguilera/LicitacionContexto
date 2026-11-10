# Costos mensuales y cronograma del SD-07

## Para calcular sueldos

- `HH_matriz_roles_M1_M56.csv` tiene una fila por rol y una columna por mes. Usa los roles de las asignaciones originales y las equivalencias documentadas del T-15.
- `HH_mes_rol.csv` contiene los mismos datos en filas por mes y rol. `HH_detalle_mes_rol_componente.csv` separa trabajo, campo, dirección, inducción y operación.
- Los CSV de valorización usan punto y coma como separador y coma decimal. M1 empieza el 7 de enero de 2027. Cada mes contractual comienza el día 7.
- `Conciliacion_mensual.csv` compara los 56 meses con la figura publicada. Todas las diferencias son 0,00 HH. `Datos_base/` conserva los registros originales. Ejecuta `python calcular_HH_por_mes_y_rol.py` para repetir el cálculo.
- El reparto posterior en los 31 roles, incluidos Front-end y Back-end, fue una propuesta de valorización. En estas tablas se usan las asignaciones fechadas que sustentaron el cálculo.

## Dotación y componentes

| Componente | HH base | Dotación |
|---|---:|---|
| Trabajo técnico y viajes | 67.933,47 | Registros diarios en Datos_base |
| Cobertura presencial M16 | 10.560,00 | 88 implantadores y 88 formadores durante los turnos de cobertura |
| Dirección y PMO | 5.824,00 | Un Jefe de Proyecto y un analista PMO |
| Inducción M20 | 416,00 | 16 HH por cada uno de los 26 integrantes de operación |
| Operación M21–M56 | 149.760,00 | 7 L1, 7 NOC, 7 SOC, 2 L2, 2 L3 y 1 gerente de servicio |
| Total base | 234.493,47 | |

Campo, dirección, PMO e inducción suman **16.800 HH** de dotación fuera de la operación. El supuesto de unas 31.000 HH mezcla conceptos. Los desplazamientos están dentro del trabajo técnico y viajes. La Tabla 7.2 del PDF SD-07 agrupa el esfuerzo por etapa y ámbito. Su línea de operación es de 150.848 HH, que incorpora trabajos específicos además de las 149.760 HH del equipo permanente.

`Dotacion_coberturas.csv` desglosa personas y horas. La dotación de terreno se distribuye en turnos. Los integrantes del retén pertenecen al equipo de proyecto, con 8 de desarrollo y 8 de QA en rotación de 8 personas por semana. `Guardias_mes_rol.csv` tiene las **1.952 unidades de disponibilidad de 12 h**, a valorizar por unidad. La contingencia de **3.688 HH** se valoriza por separado.

## Red de cronograma

`Red_CPM/CPM_y_programacion.csv` contiene las actividades, sus duraciones, fechas tempranas, tardías y programadas, y holguras. `Dependencias_todas.csv` vincula las 1.836 relaciones con los 853 nodos de `Tareas_todas.csv`. Se conserva el nombre original de dependencias `dependencias_T14.csv` y los JSON con calendarios y resultados. Los fines exclusivos indican la fecha posterior a la última jornada.

Para reproducir la comprobación, ejecuta `python Red_CPM/verificar_paquete.py`. El motor incluido recalcula CPM sobre la red guardada. La comprobación valida el escenario de fechas y cuotas personales.

## Archivos de edición y versiones

- `PDF_vigentes/` contiene los cuatro PDF adjuntos del usuario. Son la referencia para contrastar la versión publicada.
- `Fuentes_LaTeX/SD07_borrador_calculado_234493.tex` contiene el último borrador local del escenario de 234.493,47 HH. La Tabla 7.2 del PDF vigente concilia con el mismo escenario. El archivo de Descargas y el SD-07 canónico del repositorio conservan 40.946 HH, por lo que el borrador calculado se entrega como base de trabajo. Falta obtener la fuente exacta que produjo el PDF vigente para incorporar sus ediciones finales.
- `Fuentes_LaTeX/Formularios/` contiene los T-14, T-15 y T-18 editables del repositorio. Los PDF adjuntos permiten contrastar cambios posteriores hechos fuera del repositorio.
- El ZIP es un paquete de trabajo. Para compilar el borrador, hay que recuperar los recursos que figuran en `Referencias_graficas_faltantes.json` y usar la plantilla corporativa. La curva de HH y los recursos disponibles se incluyen.
