"""Genera el anexo de detalle del registro de cambios del SD-04 a partir de git.

Compara cada archivo con el commit base (antes de la redacción de noviembre) y lista
TODOS los cambios, frase por frase, con su ubicación y el motivo conocido.
Uso (desde la raíz del repo):
    python3 80_Artefactos/sd-04_contexto/redaccion-2026-11/generar_registro_cambios.py
Escribe registro-cambios-detalle.md en la misma carpeta. No edita nada más.
"""
import difflib
import os
import re
import subprocess

BASE = "226bca8"  # último commit antes de la redacción de noviembre (2026-11-06)
AQUI = os.path.dirname(os.path.abspath(__file__))
TEX = "02_Propuesta/latex_final/sd-04/OnlySimpleSolutions-Subdocumento4.tex"
REGISTRO = [
    "80_Artefactos/sd-04_contexto/registro-diseno-fisica/00_registro-de-diseno.md",
    "80_Artefactos/sd-04_contexto/registro-diseno-fisica/01_nodos.md",
    "80_Artefactos/sd-04_contexto/registro-diseno-fisica/02_conexiones.md",
    "80_Artefactos/sd-04_contexto/registro-diseno-fisica/03_ambientes.md",
    "80_Artefactos/sd-04_contexto/registro-diseno-fisica/05_capacidad.md",
    "80_Artefactos/sd-04_contexto/registro-diseno-fisica/06_supuestos-pendientes.md",
]

# Motivo por defecto según la sección (bitácora de la redacción)
POR_SECCION = [
    ("4.3.2", "Ciclo 4.3.2 (06-11): C-074 a C-084 y ajustes tras lector, hilo lógico y PMBOK"),
    ("4.3.1", "Ciclo 4.3.1 (06-11): C-053, C-021, C-068, C-070 y ajustes tras los agentes"),
    ("4.3 ", "Ciclo 4.3 (06-11): introducción del data center"),
    ("4.2.1", "Ciclo 4.2.1 (08-11): H-16, RAID (S-34), CIS y parches (S-35), RT-06.33 (S-37), par de captura del proponente"),
    ("4.2.2", "Sesión A (08-11): tipología por sitio (S-33) y Tabla de los seis factores del Art. 16.2"),
    ("4.2.3", "Sesión A (08-11): servicios contratados (DDoS, External ID, Private Access, Intune, Redis B20, FinOps, reversibilidad)"),
    ("4.2.4", "Sesión A (08-11): puertos solo en entrada pública, túneles y cruce; Private Link Service (S-11)"),
    ("4.2.5", "Sesión A (08-11): ambientes (S-05), agentes de entrega (S-28), sin marcha blanca"),
    ("4.2.6", "Sesión A (08-11): 24 horas en centros (Art. 16.4), puntos únicos, conmutación, HSM, copia del Data Lake"),
    ("4.2.7", "Sesión A (08-11): mapeo con 3.3.2 y 4.1.5, filas nuevas y plataformas conservadas"),
    ("4.2.8", "Sesión A (08-11): latencias, cálculo de nodos, pico de Service Bus, retención de registros"),
    ("4.2 ", "Sesión A (08-11): introducción de 4.2 (accesos de DC-01, fila de Brasil)"),
    ("4.1", "Sesión B (09-11): bloque 4.1 según informe de cotejo"),
    ("Referencias", "Referencias de las fuentes nuevas"),
    ("Declaración de uso de IA", "Declaración de uso de IA"),
]

# Motivo específico por contenido (decisiones del 09-11 y del cierre). Se busca en el texto nuevo o en el quitado.
REGLAS = [
    (r"figuras/diag-04-|Figura 4\.(1[2-9]|2[0-5]): ", "Figuras físicas regeneradas (09-11): sin IDs E-NN y sin omitir elementos del inventario; 17 figuras pasan a 14", "diagramas-laminas/; 01_nodos.md; skill diagramas-ancoa"),
    (r"Figura 4\.(1[2-9]|2[0-5])|Figuras 4\.(1[2-9]|2[0-5])", "Texto ajustado a las figuras físicas nuevas (09-11)", "diagramas-laminas/correspondencia-figuras.json"),
    (r"Codex y Claude|revisión de noviembre pendiente", "Declaración de uso de IA actualizada con las figuras y la redacción de noviembre", "Comunicado 10; skill diagramas-ancoa"),
    (r"30 segundos, que es un supuesto", "P-04 (opción 1): objetivo de conmutación de 30 s", "S-38; RT-03.17"),
    (r"punto único de falla al elemento|Subsisten ocho", "P-03 (opción 2) y revisor de hilo lógico: ocho puntos únicos con criterio y número", "RT-02.11; T-12"),
    (r"interrupción declarada", "P-05 (opción 1): RTO desde la interrupción declarada", "SD-09 L185; RT-07.04"),
    (r"Key Vault de Brasil con custodia dual", "P-07 (opción 1): origen de la reinyección de claves", "S-39; RT-07.10"),
    (r"uso exclusivo de la solución", "P-08 (opción 1): recinto de uso exclusivo", "S-40; RT-06.01"),
    (r"frontera con el Cliente está en el rack|canalizaciones hasta el rack", "P-09 (opción 1): frontera canalizaciones y cableado", "S-41; RT-06.33"),
    (r"marca de tiempo", "P-10 (opción 1): corte común por marca de tiempo", "S-42; RT-02.06; RT-07.04"),
    (r"sitio alternativo en Chile|Limitación conocida|Brazil South y sitio alternativo", "P-12 (opción 1) y agentes: tabla Brasil frente a la alternativa nacional", "S-44; RT-07.02; RT-07.04"),
    (r"antes de cerrar el diseño detallado", "P-13 (opción 1): plazo único de aprobación de residencia", "Art. 23; Ley 21.719"),
    (r"deshabilitado hasta|permanece deshabilitado|punto privado de tránsito", "P-14 (opción 1) y hilo lógico: origen de Brasil deshabilitado", "S-45; RT-07.05"),
    (r"ventana de deduplicación|claves de las ventas de tienda", "P-15 (opción 2) y parte 1 del 09-11: ventana de deduplicación", "S-43; S-43b; RT-02.06"),
    (r"tras ese corte de 24 horas", "P-16 (opción 1): 24 horas con conciliación en 30 minutos", "RT-03.10; RT-03.13"),
    (r"RAEX|Subsecretaría de Economía", "P-20 (opción 3): se quita la resolución RAEX202503748", "Ley 21.719"),
    (r"Redundancia entre las tres zonas", "P-17 (opción 1): Service Bus zonal confirmado por el usuario", "RT-07.01"),
    (r"Retención y copia en Brazil South|retención de cada dominio|Réplica es la copia continua", "P-06 (tabla en 4.3.2) y agentes: retención y copia por dominio", "RT-07.09 a RT-07.13; Caso cap. 15, p. 33"),
    (r"2026t|flexible server|bloqueada allí la alta disponibilidad entre zonas para servidores nuevos \(Microsoft", "P-01: cita de la tabla de regiones de PostgreSQL", "Art. 16.3"),
    (r"veinticinco actores|catorce personas", "C-008 y agentes: 25 actores del diagrama de contexto", "S-47"),
    (r"inquilino de identidad|External ID, que autentica", "C-009 y hilo lógico: un solo tenant; External ID por negocio", "S-13"),
    (r"PostgreSQL como diario|PostgreSQL local de la tienda|PostgreSQL de la nube", "C-007 e hilo lógico: motor local PostgreSQL", "RT-03.11; RT-03.12"),
    (r"Azure Pipelines con registro", "C-006: canal de entrega nombrado", "S-04"),
    (r"Balanced B20", "C-003: Redis B20 verificado", "S-26"),
    (r"capacidad de Managed HSM en Brazil South", "C-004: capacidad de HSM en Brasil", "S-20"),
    (r"sin entrada pública para X-01", "C-005: Front Door con perfil de Retail y de la filial", "K-02"),
    (r"buscador de productos por región", "C-002: existencia de productos verificada", "06 (buscador 02-11)"),
    (r"fila virtual del Modo Tienda", "C-015: fila virtual en la continuidad local", "S-32"),
    (r"Funciones no disponibles sin enlace|funciones que no están disponibles sin enlace|jefatura de tienda ejecuta", "P-02 (opción 1) y agentes: funciones sin enlace y procedimiento manual", "S-46; S-46b; RT-03.13"),
    (r"La Figura 4\.11 muestra", "C-017: explicación de la figura de capacidades comunes", "Comunicado 10"),
    (r"Capacidad de Power BI en Chile Central", "C-018: condición de Power BI en ADR-09", "S-23"),
    (r"índice técnico de OpenMetadata", "C-013: rótulo de la figura movido a 4.3.1", "Criterio incluye/excluye"),
    (r"se tratan en la vista física", "C-016: nodos de X-01 quitados de 4.1.14", "Criterio incluye/excluye"),
    (r"que son 8 de Retail, 8 de la filial", "Parte 7 (opción 1): origen de las 31 de 72U", "cierre-inventario/12"),
    (r"0,1 % de un mes", "Parte 7 (opción 1): origen de los 43 minutos", "RT-10.01"),
    (r"de la Tabla 4\.\d+ se registra con las alternativas", "Parte 5 (opción 1): alcance de las alternativas evaluadas", "FEP01·273"),
    (r"Sin cantidad propia, con la vista logística", "Parte 6 (opción 1): nodo de la vista logística y capacidades comunes", "S-29; Comunicado 10"),
    (r"espacio aislado dentro del servicio|intermediario que transporta|sin que se aplique dos veces|monto de compra que la filial autoriza", "Parte 3 (opción 1): términos definidos en su primera mención", "Lector no técnico"),
    (r"Data Lake y el almacenamiento inmutable|Service Bus, Data Lake ni", "Cierre parte 2: «Data Lake» en lugar de «lago de datos»", "Glosario 08"),
    (r"pg-x01|pg-r-vector", "Cierre parte 2: se quitan nombres internos de recursos", "Glosario 08, regla 1"),
    (r"cap\. 15, requisito RT-05\.10", "Cierre parte 3: folio y capítulo del Caso", "citas-proyecto"),
]

SEP = re.compile(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ«¿(\\])")
TABLA = re.compile(r"((?:Tablas?|Figuras?) )(4\.\d+)")


def git_show(path):
    return subprocess.run(["git", "show", f"{BASE}:{path}"], capture_output=True, text=True).stdout


def leer(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def frases(linea):
    return [f for f in SEP.split(linea.strip()) if f]


def seccion_de(lineas, i):
    for k in range(min(i, len(lineas) - 1), -1, -1):
        m = re.match(r"\\(?:sub)*section\*?\{(.+?)\}", lineas[k])
        if m:
            return m.group(1)
    return "Preámbulo"


def motivo(seccion, texto):
    hits = [(m, b) for patron, m, b in REGLAS if re.search(patron, texto)]
    if hits:
        return "; ".join(h[0] for h in hits), "; ".join(dict.fromkeys(h[1] for h in hits))
    nombre = seccion.split(" ", 1)[0] if seccion[:1].isdigit() else seccion
    for pref, mot in POR_SECCION:
        p = pref.strip()
        if nombre == p or nombre.startswith(p + ".") or (pref.endswith(" ") and nombre == p) or seccion.startswith(pref.strip()):
            return mot, "Ver bitácora"
    return "Ver bitácora", "—"


def solo_renumeracion(a, b):
    norm = lambda t: TABLA.sub(r"\1N", t)
    return a != b and norm(a) == norm(b)


def corto(t, n=10**9):
    t = t.replace("|", "\\|")
    return t if len(t) <= n else t[:n] + " […]"


def detalle_tex():
    viejo = git_show(TEX).splitlines()
    nuevo = leer(TEX).splitlines()
    sm = difflib.SequenceMatcher(None, viejo, nuevo, autojunk=False)
    filas = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        a = [l for l in viejo[i1:i2] if l.strip()]
        b = [l for l in nuevo[j1:j2] if l.strip()]
        if not a and not b:
            continue
        sec = seccion_de(nuevo, j1)
        texto_a, texto_b = "\n".join(a), "\n".join(b)
        if a and b and len(a) == len(b) and all(solo_renumeracion(x, y) for x, y in zip(a, b)):
            pares = sorted({f"{x[1]} → {y[1]}" for x, y in zip(TABLA.findall(texto_a), TABLA.findall(texto_b)) if x[1] != y[1]})
            filas.append((j1 + 1, sec, "Renumeración", [], [], "Cierre parte 1: renumeración de tablas o figuras por orden de aparición (" + ", ".join(pares) + ")", "Comunicado 10", len(a)))
            continue
        fa = [f for l in a for f in frases(l)]
        fb = [f for l in b for f in frases(l)]
        quitadas, agregadas = [], []
        for o2, x1, x2, y1, y2 in difflib.SequenceMatcher(None, fa, fb, autojunk=False).get_opcodes():
            if o2 == "equal":
                continue
            quitadas += fa[x1:x2]
            agregadas += fb[y1:y2]
        # quitar las frases que solo cambian el número de tabla
        an_set = {TABLA.sub(r"\1N", x) for x in agregadas}
        qn_set = {TABLA.sub(r"\1N", q) for q in quitadas}
        ren = bool(an_set & qn_set)
        quitadas = [q for q in quitadas if TABLA.sub(r"\1N", q) not in an_set]
        agregadas = [x for x in agregadas if TABLA.sub(r"\1N", x) not in qn_set]
        pares = sorted({f"{x[1]} → {y[1]}" for x, y in zip(TABLA.findall(texto_a), TABLA.findall(texto_b)) if x[1] != y[1]})
        if ren and not quitadas and not agregadas:
            filas.append((j1 + 1, sec, "Renumeración", [], [], "Cierre parte 1: renumeración de tablas o figuras por orden de aparición (" + ", ".join(pares) + ")", "Comunicado 10", len(b)))
            continue
        tipo = "Agregado" if not a else ("Eliminado" if not b else "Modificado")
        mot, base = motivo(sec, " ".join(agregadas + quitadas))
        if ren:
            mot += "; además, renumeración de tablas o figuras"
        filas.append((j1 + 1, sec, tipo, quitadas, agregadas, mot, base, 0))
    return filas


def detalle_md(path):
    viejo = git_show(path).splitlines()
    nuevo = leer(path).splitlines()
    out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, viejo, nuevo, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        out.append((j1 + 1, [l for l in viejo[i1:i2] if l.strip()], [l for l in nuevo[j1:j2] if l.strip()]))
    return out


def main():
    filas = detalle_tex()
    L = ["# Registro de cambios: detalle completo", "",
         f"**Generado** con `generar_registro_cambios.py` comparando con el commit `{BASE}` (06-11-2026, antes de la redacción de noviembre). "
         "Lista **todos** los cambios, frase por frase. Se regenera; no se edita a mano. El resumen y las decisiones están en `registro-cambios-trazabilidad.md`.", "",
         "Columnas: **ID**; **Línea** del `.tex` actual; **Sección**; **Tipo**; **Se quitó** y **Se agregó** (frases completas); **Motivo** (decisión o ciclo de la bitácora); **Base** (requisito, supuesto o documento).", "",
         f"## 1. `{TEX}`", ""]
    n_ren = 0
    k = 0
    for linea, sec, tipo, q, a, mot, base, nren in filas:
        if tipo == "Renumeración":
            n_ren += 1
        k += 1
        L.append(f"### CAM-{k:03d} · línea {linea} · {sec} · {tipo}")
        L.append("")
        if tipo == "Renumeración":
            L.append(f"- Solo cambian números de tabla ({nren} línea(s)). Correspondencia en `ajustes-otros-documentos.md`.")
        for f in q:
            L.append(f"- **Se quitó:** {corto(f)}")
        for f in a:
            L.append(f"- **Se agregó:** {corto(f)}")
        if nren == 0 and tipo != "Renumeración" and False:
            pass
        L.append(f"- **Motivo:** {mot}")
        L.append(f"- **Base:** {base}")
        L.append("")
    tot = {t: sum(1 for x in filas if x[2] == t) for t in ("Agregado", "Modificado", "Eliminado", "Renumeración")}
    L.insert(8, f"Totales del `.tex`: {len(filas)} cambios ({tot['Agregado']} agregados, {tot['Modificado']} modificados, {tot['Eliminado']} eliminados y {tot['Renumeración']} solo de renumeración).\n")
    sec_n = 2
    for p in REGISTRO:
        d = detalle_md(p)
        if not d:
            continue
        L.append(f"## {sec_n}. `{p}`")
        L.append("")
        for j, (linea, a, b) in enumerate(d, 1):
            L.append(f"### REG-{sec_n}{j:02d} · línea {linea}")
            for x in a:
                L.append(f"- **Se quitó:** {corto(x, 1500)}")
            for x in b:
                L.append(f"- **Se agregó:** {corto(x, 1500)}")
            L.append("")
        sec_n += 1
    # índice decisión → cambios
    idx = {}
    for k2, fila in enumerate(filas, 1):
        defecto = any(fila[5].startswith(m) for _, m in POR_SECCION)
        patron = r"Ciclo 4\.\d\.\d|Ciclo 4\.\d|Sesión [AB]" if defecto else r"P-\d\d|C-\d{3}|K-\d\d|Parte \d|Cierre parte \d"
        for tok in re.findall(patron, fila[5]):
            idx.setdefault(tok, []).append(f"CAM-{k2:03d}")
    I = ["## 0. Índice: decisión o ciclo → cambios del `.tex`", "", "| Decisión o ciclo | Cambios |", "| :--- | :--- |"]
    for tok in sorted(idx, key=lambda t: (t[0], t)):
        I.append(f"| {tok} | {', '.join(dict.fromkeys(idx[tok]))} |")
    I.append("")
    pos = L.index(f"## 1. `{TEX}`")
    L[pos:pos] = I
    with open(os.path.join(AQUI, "registro-cambios-detalle.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(len(filas), tot)


if __name__ == "__main__":
    main()
