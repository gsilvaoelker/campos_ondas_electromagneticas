"""Valida el HTML exacto que se va a publicar."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Inspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.description = False
        self.lang_es = False
        self.plot_alts: list[str | None] = []
        self.resources: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if tag == "html":
            self.lang_es = data.get("lang") == "es"
        elif tag == "meta" and data.get("name", "").lower() == "description":
            self.description = bool(data.get("content", "").strip())
        elif tag == "img" and "_images/" in (data.get("src") or ""):
            self.plot_alts.append(data.get("alt"))
        if tag in {"a", "link"} and data.get("href"):
            self.resources.append(data["href"] or "")
        elif tag in {"img", "script"} and data.get("src"):
            self.resources.append(data["src"] or "")


def local_resource_exists(html: Path, root: Path, reference: str) -> bool:
    parts = urlsplit(reference)
    if parts.scheme or parts.netloc or not parts.path:
        return True
    target = Path(unquote(parts.path))
    target = root / target.relative_to("/") if target.is_absolute() else html.parent / target
    if target.is_dir():
        target = target / "index.html"
    return target.exists()


def public_pages(root: Path) -> list[Path]:
    return sorted(
        path for path in root.rglob("*.html")
        if "_static" not in path.relative_to(root).parts
    )


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    files = public_pages(root)
    if len(files) != 25:
        errors.append(f"Se esperaban exactamente 25 páginas HTML; hay {len(files)}")
    for path in files:
        relative = path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        inspector = Inspector()
        inspector.feed(text)
        if text.count("const THEBE_JS_URL") > 1:
            errors.append(f"{relative}: declaración THEBE duplicada")
        if 'dataset.mode = localStorage.getItem("mode") || "";' in text:
            errors.append(f"{relative}: el tema visual parte de un modo inválido")
        if "FigureCanvasAgg is non-interactive" in text:
            errors.append(f"{relative}: el gráfico no se renderizó")
        if relative.as_posix() != "index.html" and not inspector.description:
            errors.append(f"{relative}: falta meta description")
        if relative.as_posix() != "index.html" and not inspector.lang_es:
            errors.append(f"{relative}: el idioma HTML no es español")
        controls = (
            "Search this book...",
            "Toggle primary sidebar",
            'aria-label="Main"',
            "Launch interactive content",
        )
        if any(control in text for control in controls):
            errors.append(f"{relative}: quedan controles principales en inglés")
        for alt in inspector.plot_alts:
            if not alt or "_images/" in alt or re.fullmatch(r"[0-9a-f_-]+\.png", alt):
                errors.append(f"{relative}: texto alternativo de gráfico inválido: {alt!r}")
        for reference in inspector.resources:
            if not local_resource_exists(path, root, reference):
                errors.append(f"{relative}: recurso local roto: {reference}")
    return errors


if __name__ == "__main__":
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "_build/html")
    failures = validate(root)
    if failures:
        print("\n".join(f"ERROR: {failure}" for failure in failures))
        raise SystemExit(1)
    print(f"Sitio validado: {len(public_pages(root))} páginas públicas")
