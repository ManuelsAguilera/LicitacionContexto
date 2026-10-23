#!/usr/bin/env python3
"""Valida una especificación de diagrama contra el catálogo cerrado de estilos de Ancoa.

Uso:  python3 scripts/validar.py ejemplos/mi_diagrama.json
Sale con código 1 si hay errores. Las advertencias no bloquean, pero deben corregirse o justificarse.
"""
import re
import sys

from _comun import CATALOGO, cargar_spec, frente_de_nodo, grupo_raiz

CLAVES_NODO = {"id", "etiqueta", "tipo", "icono", "codigo", "frente", "estado", "grupo", "insignia", "descripcion", "tecnologia"}
CLAVES_ENLACE = {"de", "a", "semantica", "etiqueta", "paso"}
CLAVES_GRUPO = {"id", "etiqueta", "frente", "tipo", "padre", "disposicion", "columnas"}
CLAVES_SPEC = {"estilo", "figura", "titulo", "fuente", "encabezado", "grupos", "nodos", "enlaces", "notas", "$schema", "composicion"}


def validar(spec):
    errores, avisos = [], []
    E = errores.append
    A = avisos.append

    # --- estilo y metadatos -------------------------------------------------
    estilo_id = spec.get("estilo")
    estilo = CATALOGO["estilos"].get(estilo_id)
    if not estilo:
        E(f"E01 estilo «{estilo_id}» no existe. Permitidos: {', '.join(CATALOGO['estilos'])}. "
          "No se admite ningún otro tipo de diagrama.")
        return errores, avisos
    familia = estilo["familia"]
    referencia = spec.get('composicion') in ('columnas_referencia','columnas_organizadas','columnas_decisiones','columnas_legibles','bandas_horizontales')
    if spec.get('composicion') and not (referencia and estilo_id == 'L2'):
        E('E01 composición no admitida para este estilo')
        return errores, avisos
    if referencia:
        estilo = dict(estilo, tipos_nodo=estilo['referencia']['tipos_nodo'],
                      max_nodos=estilo['referencia']['max_nodos'], prefijo_capa_obligatorio=False)
        requeridos = set(estilo['referencia']['grupos_obligatorios'])
        presentes = {g.get('id') for g in spec.get('grupos', [])}
        if not requeridos.issubset(presentes):
            E('E09 faltan grupos de capas: ' + ', '.join(sorted(requeridos - presentes)))
        admitidos = set(estilo['referencia']['grupos_admitidos'])
        if presentes - admitidos:
            E('E16 grupos fuera de la composición: ' + ', '.join(sorted(presentes-admitidos)))
        if not any(n.get('codigo') == 'X-01' for n in spec.get('nodos', [])):
            E('E10 la composición por capas exige X-01')

    for k in spec:
        if k not in CLAVES_SPEC:
            E(f"E03 clave no admitida en la especificación: «{k}»")
    if not spec.get("titulo"):
        E("E02 falta «titulo» (C4: todo diagrama necesita título con tipo y alcance)")
    if not spec.get("fuente"):
        E("E02 falta «fuente» (convención del Subdocumento 4: «Fuente: elaboración propia a partir de …»)")
    if spec.get("figura") and not re.fullmatch(r"\d+\.\d+", str(spec["figura"])):
        A(f"A17 «figura» debería tener forma 4.N; se recibió «{spec['figura']}»")

    grupos = spec.get("grupos", [])
    nodos = spec.get("nodos", [])
    enlaces = spec.get("enlaces", [])
    gpid = {g.get("id"): g for g in grupos}
    npid = {}

    # --- grupos --------------------------------------------------------------
    vistos = set()
    for g in grupos:
        for k in g:
            if k not in CLAVES_GRUPO:
                E(f"E03 grupo «{g.get('id')}»: atributo no admitido «{k}» (los colores y trazos los fija el catálogo)")
        if not g.get("id") or g["id"] in vistos:
            E(f"E07 grupo con id vacío o repetido: «{g.get('id')}»")
        vistos.add(g.get("id"))
        if g.get("padre") and g["padre"] not in gpid:
            E(f"E07 grupo «{g['id']}»: padre «{g['padre']}» no existe")
        if familia == "logica":
            if g.get("frente") and g["frente"] not in CATALOGO["frentes"]:
                E(f"E16 grupo «{g['id']}»: frente «{g['frente']}» desconocido. Permitidos: {', '.join(CATALOGO['frentes'])}")
            if g.get("tipo"):
                E(f"E16 grupo «{g['id']}»: «tipo» es solo para estilos físicos; en estilos lógicos use «frente»")
        else:
            if g.get("tipo") not in estilo["tipos_grupo"]:
                E(f"E16 grupo «{g['id']}»: tipo «{g.get('tipo')}» no admitido en {estilo_id}. Permitidos: {', '.join(estilo['tipos_grupo'])}")
            if g.get("disposicion") and g["disposicion"] not in ("fila", "columna", "rejilla"):
                E(f"E16 grupo «{g['id']}»: disposición «{g['disposicion']}» no válida (fila, columna, rejilla)")

    # --- nodos ---------------------------------------------------------------
    if len(nodos) > estilo["max_nodos"]:
        E(f"E08 {len(nodos)} nodos superan el máximo de {estilo['max_nodos']} para {estilo_id}. "
          "Divida en varios diagramas del mismo estilo (por ejemplo, un L3 por bloque).")
    regex_codigos = [re.compile(r) for r in CATALOGO["codigos"].values()]
    for n in nodos:
        nid = n.get("id")
        for k in n:
            if k not in CLAVES_NODO:
                E(f"E03 nodo «{nid}»: atributo no admitido «{k}» (colores, formas y estilos los fija el catálogo)")
        if not nid or nid in npid:
            E(f"E07 nodo con id vacío o repetido: «{nid}»")
        npid[nid] = n
        if not n.get("etiqueta"):
            E(f"E07 nodo «{nid}»: falta «etiqueta»")
        if n.get("grupo") and n["grupo"] not in gpid:
            E(f"E07 nodo «{nid}»: grupo «{n['grupo']}» no existe")
        estado = n.get("estado", "objetivo")
        if estado not in CATALOGO["estados_nodo"]:
            E(f"E06 nodo «{nid}»: estado «{estado}» desconocido. Permitidos: {', '.join(CATALOGO['estados_nodo'])}")
        if familia == "logica":
            tipo = n.get("tipo")
            if n.get("icono"):
                E(f"E04 nodo «{nid}»: en estilos lógicos se usa «tipo», no «icono»")
            if tipo not in estilo["tipos_nodo"]:
                E(f"E04 nodo «{nid}»: tipo «{tipo}» no admitido en {estilo_id}. Permitidos: {', '.join(estilo['tipos_nodo'])}")
            if n.get("frente") and n["frente"] not in CATALOGO["frentes"]:
                E(f"E16 nodo «{nid}»: frente «{n['frente']}» desconocido")
            if estado == "propuesto":
                A(f"A06 nodo «{nid}»: «propuesto» es un estado de los estilos físicos; en lógicos use «por_acreditar» o «condicionado»")
            if CATALOGO["tipos_nodo_logicos"].get(tipo, {}).get("requiere_codigo") and not n.get("codigo"):
                E(f"E11 nodo «{nid}»: un «servicio» debe llevar el código del Subdocumento 3 (p. ej. R:V-02, F:C-01)")
            # frente del nodo coherente con el de su grupo
            if n.get("frente") and n.get("grupo"):
                gf = frente_de_nodo({"grupo": n["grupo"]}, gpid)
                if gf and gf not in ("transversal", "externo") and gf != n["frente"]:
                    E(f"E12 nodo «{nid}» (frente {n['frente']}) está dentro de un grupo del frente {gf}: "
                      "Retail y Emisor no comparten contenedor")
        else:
            if n.get("tipo"):
                E(f"E04 nodo «{nid}»: en estilos físicos se usa «icono», no «tipo»")
            if n.get("icono") not in CATALOGO["iconos_fisicos"]:
                E(f"E04 nodo «{nid}»: ícono «{n.get('icono')}» no está en la lista blanca. "
                  f"Permitidos: {', '.join(CATALOGO['iconos_fisicos'])}")
            if estado in ("convivencia",):
                A(f"A06 nodo «{nid}»: «convivencia» es un estado lógico; en físicos use «propuesto» o «condicionado»")
        cod = n.get("codigo")
        if cod and not any(r.fullmatch(cod) for r in regex_codigos):
            E(f"E11 nodo «{nid}»: código «{cod}» no sigue la nomenclatura del proyecto "
              "(R:M-01, F:C-01, X-01, L-01, AH-01, AS-01, SIT/CD/DC/CLD/EXT-01, ADR-01)")
        if n.get("insignia") is not None and estilo_id not in ("F4",):
            A(f"A14 nodo «{nid}»: las insignias numeradas solo se usan en F4 (puntos de falla)")

    # --- reglas de estilo ----------------------------------------------------
    if familia == "logica":
        frentes_presentes = {frente_de_nodo(n, gpid) for n in nodos} | {g.get("frente") for g in grupos}
        for f in estilo.get("grupos_obligatorios", []):
            if f not in frentes_presentes:
                E(f"E09 {estilo_id} exige el frente «{f}» (estilo de referencia: Fig. {', '.join(estilo['figuras_referencia'])})")
        if estilo.get("requiere_x01") and not any(n.get("tipo") == "politica_x01" or n.get("codigo") == "X-01" for n in nodos):
            E(f"E10 {estilo_id} exige dibujar X-01 entre ambos frentes")
        if estilo.get("prefijo_capa_obligatorio"):
            for n in nodos:
                if not re.match(r"^\d · ", n.get("etiqueta", "")) and not n.get("etiqueta", "").upper().startswith("ACTORES"):
                    E(f"E15 nodo «{n.get('id')}»: en L2 cada caja empieza por «N · CAPA» (p. ej. «4 · SERVICIOS RETAIL»)")
    if estilo.get("insignias_obligatorias"):
        ins = sorted(n["insignia"] for n in nodos if n.get("insignia") is not None)
        if not ins:
            E("E14 F4 exige insignias numeradas en los puntos de falla")
        elif ins != list(range(1, len(ins) + 1)):
            E(f"E14 insignias deben ser 1..N sin saltos ni repeticiones; se recibió {ins}")

    # --- enlaces -------------------------------------------------------------
    nivel_cruce = estilo.get("etiqueta_en_cruces", "advertencia")
    for i, a in enumerate(enlaces):
        tag = f"enlace #{i + 1} ({a.get('de')}→{a.get('a')})"
        for k in a:
            if k not in CLAVES_ENLACE:
                E(f"E03 {tag}: atributo no admitido «{k}»")
        extremos_validos = set(npid) | (set(gpid) if familia == "fisica" else (set(gpid) & set(CATALOGO["estilos"]["L2"]["referencia"].get("grupos_conectables", ["area_mercaderia", "area_venta", "area_clientes", "servicios_e"])) if spec.get("composicion") in ("columnas_legibles","bandas_horizontales") else set()))
        if a.get("de") not in extremos_validos or a.get("a") not in extremos_validos:
            E(f"E07 {tag}: origen o destino no existe" + ("" if familia == "fisica" else " (en estilos lógicos solo se unen nodos)"))
            continue
        sem = a.get("semantica")
        if sem not in estilo["semanticas_enlace"]:
            E(f"E05 {tag}: semántica «{sem}» no admitida en {estilo_id}. Permitidas: {', '.join(estilo['semanticas_enlace'])}")
            continue
        etiqueta = (a.get("etiqueta") or "").strip()
        if estilo.get("todas_las_flechas_etiquetadas") and not etiqueta:
            E(f"E13 {tag}: en {estilo_id} toda flecha lleva etiqueta con su intención")
        if familia == "logica":
            f1 = frente_de_nodo(npid.get(a["de"], {"grupo": a["de"]}), gpid)
            f2 = frente_de_nodo(npid.get(a["a"], {"grupo": a["a"]}), gpid)
            if {f1, f2} == {"retail", "emisor"}:
                if sem not in ("compra_autorizable", "denegado"):
                    E(f"E12 {tag}: LÍNEA ROJA. Entre Retail y Emisor solo se dibuja la autorización de compra "
                      "(«compra_autorizable») o, en L5, la solicitud «denegado». Cualquier otro intercambio pasa por X-01.")
            if sem == "denegado" and "DENEGAD" not in etiqueta.upper():
                A(f"A12 {tag}: un enlace «denegado» debería rotularse «… ACCESO DENEGADO»")
            if sem == "compra_autorizable" and not etiqueta:
                E(f"E13 {tag}: la autorización de compra debe rotularse (p. ej. «autorización de compra»)")
            r1 = grupo_raiz(npid.get(a["de"], {"grupo": a["de"]}).get("grupo"), gpid)
            r2 = grupo_raiz(npid.get(a["a"], {"grupo": a["a"]}).get("grupo"), gpid)
            cruza = r1 != r2
        else:
            raiz_de = lambda x: grupo_raiz(x if x in gpid else npid[x].get("grupo"), gpid)
            cruza = raiz_de(a["de"]) != raiz_de(a["a"]) and sem not in ("enlace", "despliegue")
        if cruza and not etiqueta and not estilo.get("todas_las_flechas_etiquetadas"):
            msg = f"{tag}: cruza de un contenedor a otro sin etiqueta (C4: cada flecha describe su intención)"
            (E if nivel_cruce == "error" else A)(("E13 " if nivel_cruce == "error" else "A13 ") + msg)

    if estilo_id == "L4":
        if not any(a.get("paso") for a in enlaces):
            A("A18 L4: se recomienda numerar los pasos («paso»: 1, 2, …) como en un diagrama dinámico C4")

    return errores, avisos


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    spec = cargar_spec(sys.argv[1])
    errores, avisos = validar(spec)
    for e in errores:
        print("ERROR  ", e)
    for a in avisos:
        print("AVISO  ", a)
    if errores:
        print(f"\n✗ {len(errores)} error(es). El diagrama NO cumple el catálogo; corrija la especificación antes de renderizar.")
        sys.exit(1)
    print(f"✓ Especificación válida para el estilo {spec['estilo']} ({CATALOGO['estilos'][spec['estilo']]['nombre']})"
          + (f" con {len(avisos)} aviso(s)." if avisos else "."))


if __name__ == "__main__":
    main()
