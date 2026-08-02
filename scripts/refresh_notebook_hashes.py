"""Actualiza las celdas de preparación con hashes SHA256 de los módulos."""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted(ROOT.glob("unidad_*/*.ipynb")) + sorted(
    ROOT.glob("repaso_final/*.ipynb")
)


def module_names(source: str) -> list[str]:
    tree = ast.parse(source)
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == "MODULOS" for target in node.targets):
                value = ast.literal_eval(node.value)
                return list(value if isinstance(value, list) else value.keys())
    raise ValueError("No se encontró la asignación MODULOS.")


def setup_source(modules: list[str]) -> str:
    entries = []
    for module in modules:
        digest = hashlib.sha256((ROOT / "src" / module).read_bytes()).hexdigest()
        entries.append(f'    "{module}": "{digest}",')
    module_map = "\n".join(entries)
    return f'''# Preparación del entorno: local o Google Colab, con verificación SHA256.
import hashlib
import sys
import urllib.request
from pathlib import Path

MODULOS = {{
{module_map}
}}
URL_SRC = (
    "https://raw.githubusercontent.com/"
    "gsilvaoelker/campos_ondas_electromagneticas/main/src/"
)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


candidatos = [Path.cwd(), *Path.cwd().parents]
raiz_repo = next((p for p in candidatos if (p / ".git").exists()), None)
if raiz_repo is not None:
    for modulo, esperado in MODULOS.items():
        archivo = raiz_repo / "src" / modulo
        if not archivo.exists() or sha256(archivo) != esperado:
            raise RuntimeError(
                f"Hash local desactualizado para {{modulo}}. "
                "Ejecute scripts/refresh_notebook_hashes.py."
            )
    raiz = raiz_repo
else:
    raiz = Path.cwd()
    (raiz / "src").mkdir(exist_ok=True)
    for modulo, esperado in MODULOS.items():
        destino = raiz / "src" / modulo
        if destino.exists() and sha256(destino) == esperado:
            continue
        with urllib.request.urlopen(URL_SRC + modulo, timeout=30) as respuesta:
            datos = respuesta.read()
        obtenido = hashlib.sha256(datos).hexdigest()
        if obtenido != esperado:
            raise RuntimeError(
                f"SHA256 inválido para {{modulo}}: {{obtenido}} != {{esperado}}"
            )
        destino.write_bytes(datos)

sys.path.insert(0, str(raiz / "src"))'''


def main() -> None:
    for path in NOTEBOOKS:
        notebook = json.loads(path.read_text(encoding="utf-8"))
        source = "".join(notebook["cells"][2]["source"])
        notebook["cells"][2]["source"] = setup_source(module_names(source)).splitlines(
            keepends=True
        )
        path.write_text(
            json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )
    print(f"Hashes actualizados en {len(NOTEBOOKS)} notebooks.")


if __name__ == "__main__":
    main()
