import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted(ROOT.glob("unidad_*/*.ipynb")) + sorted(
    ROOT.glob("repaso_final/*.ipynb")
)
MODULES = sorted((ROOT / "src").glob("*.py"))


def source(path: Path) -> str:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    return "\n".join("".join(cell.get("source", [])) for cell in notebook["cells"])


def test_catalogo_tiene_17_notebooks_y_diez_secciones():
    assert len(NOTEBOOKS) == 17
    for path in NOTEBOOKS:
        text = source(path)
        for number in range(1, 11):
            assert f"## {number}." in text, f"Falta la sección {number} en {path}"


def test_cada_notebook_tiene_enlace_colab_directo_y_readme_lo_indexa():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for path in NOTEBOOKS:
        relative = path.relative_to(ROOT).as_posix()
        url = (
            "https://colab.research.google.com/github/"
            "gsilvaoelker/campos_ondas_electromagneticas/blob/main/"
            + relative
        )
        assert url in source(path), path
        assert url in readme, path


def test_descargas_colab_estan_fijadas_por_sha256():
    hashes = {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in MODULES
    }
    for path in NOTEBOOKS:
        text = source(path)
        assert "hashlib.sha256" in text, path
        assert "obtenido != esperado" in text, path
        for module, digest in hashes.items():
            if f'"{module}"' in text:
                assert digest in text, f"Hash obsoleto para {module} en {path}"


def test_no_reaparecen_errores_docentes_conocidos():
    all_text = "\n".join(source(path) for path in NOTEBOOKS)
    forbidden = (
        "Girar 20° o girar 70° da el mismo brillo",
        "theta_transmitido = np.rad2deg(np.arccos(coseno_t.real))",
        "agua de mar es buen conductor en radio AM y buen",
        "son la misma fórmula. Una interfaz óptica",
        "La curva cruza $Z_0$ dos veces por período",
        "la aproximación hertziana es válida, como confirma",
    )
    for claim in forbidden:
        assert claim not in all_text


def test_licencias_delimitan_codigo_contenido_y_notebooks_mixtos():
    scope = (ROOT / "LICENSE").read_text(encoding="utf-8")
    code = (ROOT / "LICENSE-CODE").read_text(encoding="utf-8")
    content = (ROOT / "LICENSE-CONTENT").read_text(encoding="utf-8")
    assert "code cells" in scope and "Markdown cells" in scope
    assert "MIT License" in code
    assert "Creative Commons Attribution 4.0 International" in content
