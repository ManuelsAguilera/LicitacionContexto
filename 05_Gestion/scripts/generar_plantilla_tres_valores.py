#!/usr/bin/env python3
"""Genera la planilla vacía de tres valores por paquete (paso 8d del plan de estimación).

Una fila por paquete de `14_edt_corregida.md`. Los paquetes del UCP llevan solo su servicio y su cantidad de RF como unidad de
tamaño (no se incluyen casos de uso ni horas, para que el estimador sea independiente del UCP). Los demás llevan la unidad de
tamaño de su rama, tomada de las fuentes. Escribe `12_plantilla_tres_valores.md`.

    python3 05_Gestion/scripts/generar_plantilla_tres_valores.py [--salida RUTA]
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generar_mapa_paquetes as gm  # noqa: E402

SALIDA = gm.DIR / "12_plantilla_tres_valores.md"
UNIDAD_POR_RAMA = {
    "1.1": "56 meses de contrato; comités mensuales, quincenales y semanales (sd-01, 1.5)",
    "1.2": "14 interfaces entre 9 plataformas de 6 proveedores",
    "1.3": "13 servicios y la base tecnológica; arquitectura híbrida",
    "1.4": "Nube pública y on-premise; 22 tiendas y 2 centros de distribución; centro de datos de 140 m²",
    "1.6": "14 interfaces existentes; 940 proveedores",
    "1.7": "620.000 clientes de la cartera por tramos; 268.000 referencias; 24 instalaciones",
    "1.8": "RNF-33 a RNF-38 y RNF-70 a RNF-76 del Anexo B",
    "1.9": "RNF-22 a RNF-28 y RNF-32 del Anexo B; 28 criterios de aceptación",
    "1.10": "5 innovaciones, una por tipo (art. 29)",
    "1.11": "Piloto de 3 tiendas; 22 tiendas y 2 centros; 380 líneas de caja; 640 terminales",
    "1.12": "Dos marchas blancas, una por etapa",
    "1.13": "Unos 1.100 repositores externos; 62 % de rotación; 1.900 incorporaciones de temporada",
    "1.14": "Documentación del art. 77.1; Plan de Reversibilidad dentro de los primeros 90 días, actualizado cada año",
    "1.15": "36 meses de operación",
}


def texto(paquetes):
    ucp = [p for p in paquetes if p["metodo"] == "UCP"]
    otros = [p for p in paquetes if p["metodo"] != "UCP"]
    L = ["# Planilla de tres valores para el segundo método (paso 7, puerta G7)", "",
         "Documento de contexto, no es entregable. Generado por `05_Gestion/scripts/generar_plantilla_tres_valores.py` a partir de `14_edt_corregida.md`; "
         "no editar la estructura a mano. Fecha: 2026-10-08. Plantilla **vacía**: no contiene ninguna hora. Cada estimador la copia a un archivo propio "
         "(por ejemplo `12_tres_valores_estimador1.md`), llena sus horas sin consultar `10_esfuerzo.md`, `07_uucw_uucp.md` ni `15_mapa_paquetes_ucp.md`, y la entrega. "
         "Se comparan con `python3 05_Gestion/scripts/comparar_metodos.py ARCHIVO1.md ARCHIVO2.md`.", "",
         "## Instrucciones", "",
         "1. Estima **horas-hombre de todo el trabajo** del paquete (análisis, diseño, construcción, pruebas y gestión propia), como lo haría un equipo que lo ejecuta de principio a fin. Un número por celda, sin texto.",
         "2. **Optimista** es el valor si todo sale bien (casi sin imprevistos). **Probable** es el más realista. **Pesimista** es el valor si salen mal las cosas que sí pueden salir mal. Debe cumplirse optimista ≤ probable ≤ pesimista.",
         "3. Deja en blanco una fila solo si no puedes estimarla. No inventes: una fila en blanco se informa como pendiente.",
         "4. Estima por separado y sin consultar al otro estimador. La independencia es lo que da valor a la comparación.",
         f"5. Los **{len(ucp)} paquetes de desarrollo de software** (primera tabla) se comparan con el UCP. Los **{len(otros)} restantes** (segunda tabla) no los cubre el UCP: se suman por rama.",
         "6. Si dos paquetes comparten trabajo, pon las horas en uno solo y anótalo debajo. Los conectores de cada servicio y la administración de la base tecnológica ya están en los paquetes de software; no los repitas en las ramas de integración, infraestructura o seguridad.",
         "7. Anota en una línea cada supuesto relevante debajo de las tablas.", "",
         "## Desarrollo de software (se compara con el UCP)", "",
         "| Código | Paquete | Servicio | Unidad de tamaño | Optimista (h) | Probable (h) | Pesimista (h) |",
         "| :-- | :-- | :-- | :-- | --: | --: | --: |"]
    for p in ucp:
        L.append(f"| {p['codigo']} | {p['nombre']} | {p['nodo']} | {len(p['rf'])} RF. Etapa {p['etapa']} | | | |")
    L += ["", "## Lo que el UCP no cubre (se suma por rama, no se compara)", "",
          "| Código | Paquete | Etapa | Unidad de tamaño | Optimista (h) | Probable (h) | Pesimista (h) |",
          "| :-- | :-- | :-- | :-- | --: | --: | --: |"]
    for p in otros:
        L.append(f"| {p['codigo']} | {p['nombre']} | {p['etapa']} | {UNIDAD_POR_RAMA.get(p['rama'], '—')} | | | |")
    L += ["", "## Supuestos del estimador", "", "(Anota aquí una línea por cada supuesto.)", ""]
    return "\n".join(L)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--salida", default=str(SALIDA))
    a = ap.parse_args(argv)
    paquetes, h = gm.cargar()
    if h:
        print("\n".join(h))
        return 1
    Path(a.salida).write_text(texto(paquetes), encoding="utf-8")
    print("escrito en", a.salida)
    return 0


if __name__ == "__main__":
    sys.exit(main())
