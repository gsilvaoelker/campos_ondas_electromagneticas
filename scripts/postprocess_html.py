"""Correcciones deterministas sobre el HTML generado por Jupyter Book 1.x."""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path


ALT_BY_PAGE = {
    "unidad_01/01_algebra_vectorial_coordenadas_gradiente.html": "Mapa de potencial y campo eléctrico obtenido de su gradiente.",
    "unidad_01/02_gauss_stokes_campos_y_fuentes.html": "Campo radial dentro y fuera de una esfera con carga uniforme.",
    "unidad_01/03_capacitancia_inductancia_energia.html": "Energía de un condensador en función del voltaje aplicado.",
    "unidad_01/04_continuidad_maxwell_condiciones_de_borde.html": "Decaimiento exponencial de carga libre medido en tiempos de relajación.",
    "unidad_01/05_repaso_prueba_1.html": "Campo y potencial continuos de una esfera con carga uniforme.",
    "unidad_01/06_sintesis_maxwell_y_bordes.html": "Componentes normales de campo y flujo a ambos lados de una interfaz.",
    "unidad_02/07_fasores_y_ondas_planas.html": "Campos eléctrico y magnético en fase para una onda plana sin pérdidas.",
    "unidad_02/08_medios_con_perdidas.html": "Atenuación en cobre y en un dieléctrico con pérdidas.",
    "unidad_02/09_polarizacion_y_pixel_lcd.html": "Elipse de polarización y transmisión del modelo óptico ideal.",
    "unidad_02/10_snell_fresnel_y_brewster.html": "Reflectancias de Fresnel para ambas polarizaciones y ángulos especiales.",
    "unidad_02/11_repaso_prueba_2.html": "Atenuación espacial y mínimo de Brewster para polarización paralela.",
    "unidad_03/12_lineas_de_transmision.html": "Partes real e imaginaria de la impedancia de entrada de una línea.",
    "unidad_03/13_ondas_estacionarias_y_adaptacion.html": "Onda estacionaria y respuesta en frecuencia de un transformador de cuarto de onda.",
    "unidad_03/14_carta_de_smith_y_radiacion.html": "Carta de Smith simplificada y patrón del elemento hertziano.",
    "unidad_03/15_guias_de_onda_y_antenas.html": "Cortes modales de una guía y patrón de radiación ideal.",
    "unidad_03/16_repaso_prueba_3.html": "Transformación de impedancia y dispersión del modo dominante de una guía.",
    "repaso_final/17_repaso_integrador.html": "Comparación de esfera cargada, interfaz óptica y línea de transmisión.",
}

THEBE_SCRIPT = re.compile(r"\s*<script>const THEBE_JS_URL = .*?</script>", re.DOTALL)
PLOT_IMAGE = re.compile(r'<img\b[^>]*\bsrc="(?:\.\./)*_images/[^"]+"[^>]*>')


def deduplicate_thebe(text: str) -> str:
    seen = False

    def replace(match: re.Match[str]) -> str:
        nonlocal seen
        if seen:
            return ""
        seen = True
        return match.group(0)

    return THEBE_SCRIPT.sub(replace, text)


def add_description(text: str) -> str:
    if re.search(r'<meta\s+name="description"', text, re.IGNORECASE):
        return text
    match = re.search(r"<title>(.*?)</title>", text, re.DOTALL)
    title = re.sub(r"\s+", " ", html.unescape(match.group(1))).strip() if match else "ICEE1033"
    description = html.escape(
        f"Capítulo de ICEE1033 sobre {title}, con formulación, código, resultados y ejercicios.",
        quote=True,
    )
    return text.replace(
        "</head>", f'  <meta name="description" content="{description}" />\n</head>', 1
    )


def add_alt(text: str, alt: str | None) -> str:
    if alt is None:
        return text

    def replace(match: re.Match[str]) -> str:
        tag = match.group(0)
        escaped = html.escape(alt, quote=True)
        if re.search(r'\balt="[^"]*"', tag):
            return re.sub(r'\balt="[^"]*"', f'alt="{escaped}"', tag, count=1)
        return tag[:-1] + f' alt="{escaped}">'

    return PLOT_IMAGE.sub(replace, text)


def localize(text: str) -> str:
    replacements = {
        'document.documentElement.dataset.mode = localStorage.getItem("mode") || "";':
            'document.documentElement.dataset.mode = localStorage.getItem("mode") || "auto";',
        'document.documentElement.dataset.theme = localStorage.getItem("theme") || "";':
            'document.documentElement.dataset.theme = localStorage.getItem("theme") '
            '|| (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");',
        'aria-label="Search this book..."': 'aria-label="Buscar en este libro"',
        'placeholder="Search this book..."': 'placeholder="Buscar en este libro"',
        'title="Toggle primary sidebar"': 'title="Abrir o cerrar la navegación principal"',
        'aria-label="Toggle primary sidebar"': 'aria-label="Abrir o cerrar la navegación principal"',
        'title="Toggle secondary sidebar"': 'title="Abrir o cerrar la navegación secundaria"',
        'aria-label="Toggle secondary sidebar"': 'aria-label="Abrir o cerrar la navegación secundaria"',
        'aria-label="Main"': 'aria-label="Principal"',
        'aria-label="Launch interactive content"': 'aria-label="Abrir contenido interactivo"',
    }
    for original, translated in replacements.items():
        text = text.replace(original, translated)
    return text


def process(directory: Path) -> int:
    files = sorted(
        path for path in directory.rglob("*.html")
        if "_static" not in path.relative_to(directory).parts
    )
    if not files:
        raise SystemExit(f"No se encontraron archivos HTML en {directory}")
    for path in files:
        relative = path.relative_to(directory).as_posix()
        text = path.read_text(encoding="utf-8")
        text = localize(add_alt(add_description(deduplicate_thebe(text)), ALT_BY_PAGE.get(relative)))
        path.write_text(text, encoding="utf-8")
    return len(files)


if __name__ == "__main__":
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "_build/html")
    print(f"HTML posprocesado: {process(root)} archivos")
