#!/usr/bin/env python3
"""Exporta un .drawio a PNG para revisión, usando el visor oficial de draw.io en Chromium headless.

Uso:  python3 scripts/previsualizar_drawio.py salida/fig.drawio salida/fig.png [ruta/viewer-static.min.js]
Requiere Playwright + Chromium y acceso a raw.githubusercontent.com (visor e íconos de jgraph/drawio).
Para la entrega final, exportar desde la app draw.io (Archivo → Exportar como → PNG/PDF).
"""
import json
import pathlib
import sys
import urllib.request

from playwright.sync_api import sync_playwright

BASE = "https://raw.githubusercontent.com/jgraph/drawio/dev/src/main/webapp/"


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    drawio = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
    png = sys.argv[2]
    visor = pathlib.Path(sys.argv[3]) if len(sys.argv) > 3 else None
    if visor is None or not visor.exists():
        visor_js = urllib.request.urlopen(BASE + "js/viewer-static.min.js", timeout=60).read().decode()
    else:
        visor_js = visor.read_text(encoding="utf-8")
    cfg = json.dumps({"highlight": "none", "nav": False, "toolbar": "", "xml": drawio, "lightbox": False})
    pagina = ("<!doctype html><html><head><meta charset='utf-8'></head><body style='margin:0;background:#fff'>"
              "<div id='lienzo'></div>"
              "<script>window.DRAWIO_BASE_URL='https://app.local';window.mxImageBasePath='https://app.local/img';</script>"
              "<script src='https://app.local/viewer.js'></script></body></html>")
    cache = {}

    def manejar(route):
        url = route.request.url
        if url.endswith("/viewer.js"):
            return route.fulfill(body=visor_js, content_type="application/javascript")
        if url.startswith("https://app.local/"):
            ruta = url.split("https://app.local/", 1)[1].split("?")[0]
            try:
                if ruta not in cache:
                    cache[ruta] = urllib.request.urlopen(BASE + ruta, timeout=30).read()
                tipo = "image/svg+xml" if ruta.endswith(".svg") else "application/octet-stream"
                return route.fulfill(body=cache[ruta], content_type=tipo)
            except Exception:
                return route.fulfill(status=404, body="")
        if url.startswith("https://viewer.diagrams.net/") or url.startswith("https://app.diagrams.net/"):
            ruta = url.split(".net/", 1)[1].split("?")[0]
            try:
                if ruta not in cache:
                    cache[ruta] = urllib.request.urlopen(BASE + ruta, timeout=30).read()
                return route.fulfill(body=cache[ruta], content_type="image/svg+xml" if ruta.endswith(".svg") else None)
            except Exception:
                return route.fulfill(status=404, body="")
        return route.fulfill(status=404, body="")

    with sync_playwright() as p:
        nav = p.chromium.launch()
        pg = nav.new_page(viewport={"width": 1800, "height": 1400}, device_scale_factor=1.5)
        pg.route("**/*", manejar)
        pg.set_content(pagina, wait_until="networkidle")
        pg.wait_for_function("typeof GraphViewer !== 'undefined'", timeout=30000)
        pg.evaluate("""cfg => { const d = document.createElement('div'); d.className = 'mxgraph';
            d.setAttribute('data-mxgraph', cfg); document.getElementById('lienzo').appendChild(d);
            GraphViewer.processElements(); }""", cfg)
        pg.wait_for_selector("div.mxgraph svg", timeout=30000)
        pg.wait_for_load_state("networkidle")
        pg.wait_for_timeout(1500)
        pg.locator("div.mxgraph").first.screenshot(path=png)
        nav.close()
    print(f"✓ {png}")


if __name__ == "__main__":
    main()
