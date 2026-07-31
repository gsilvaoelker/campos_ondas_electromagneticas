# Campos y Ondas Electromagnéticas — sitio del curso

Material computacional del curso **ICEE1033**, Escuela de Ingeniería,
Universidad Mayor. Construido con [Jupyter Book](https://jupyterbook.org) y
publicado en GitHub Pages.

- **Sitio publicado:** https://gsilvaoelker.github.io/campos_ondas_electromagneticas/
- **Cobertura actual:** Unidad 1 (semanas 1 a 6)

---

## Contenido del repositorio

```
.
├── .github/workflows/construir-y-publicar.yml   Build + despliegue automático
├── _config.yml                                  Configuración de Jupyter Book
├── _toc.yml                                     Tabla de contenidos
├── requirements.txt                             Dependencias
├── intro.md                                     Página principal
├── uso.md                                       Instrucciones para estudiantes
├── src/                                         Módulos reutilizables
│   ├── constantes_fisicas.py
│   ├── transformaciones_coordenadas.py
│   ├── campos_electrostaticos.py
│   ├── medios_y_condiciones_de_borde.py
│   └── utilidades_notebook.py
└── unidad_01/                                   Notebooks de la Unidad 1
    ├── unidad_01.md
    └── 01..06_*.ipynb
```

---

## 1. Ejecutar el proyecto localmente

Requiere Python 3.11 o superior.

```bash
git clone https://github.com/gsilvaoelker/campos_ondas_electromagneticas.git
cd campos_ondas_electromagneticas

python3 -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Para abrir un notebook y trabajar en él:

```bash
jupyter lab unidad_01/01_algebra_vectorial_coordenadas_gradiente.ipynb
```

La celda de preparación del entorno detecta que `src/` existe localmente y no
descarga nada. Funciona desde cualquier directorio dentro del repositorio.

Para verificar que los seis notebooks se ejecutan de principio a fin:

```bash
python -m nbclient unidad_01/*.ipynb
```

o, con más control:

```bash
jupyter nbconvert --to notebook --execute --inplace unidad_01/*.ipynb
```

---

## 2. Construir Jupyter Book

```bash
jupyter-book build .
```

El sitio queda en `_build/html/index.html`. Ábralo con:

```bash
open _build/html/index.html          # macOS
xdg-open _build/html/index.html      # Linux
```

`_config.yml` usa `execute_notebooks: force`, de modo que **cada construcción
vuelve a ejecutar los notebooks**. Es lento pero garantiza que el sitio publicado
nunca muestre resultados obsoletos.

Si necesita una construcción rápida sin ejecutar, cambie temporalmente esa opción
a `off`.

Para partir de cero después de un error de construcción:

```bash
jupyter-book clean . --all
jupyter-book build .
```

---

## 3. Publicar en GitHub Pages

El despliegue es automático: cada `push` a `main` dispara el workflow
`.github/workflows/construir-y-publicar.yml`, que instala las dependencias,
construye el libro y lo publica.

**Configuración inicial, una sola vez:**

1. Cree el repositorio en GitHub con el nombre
   `campos_ondas_electromagneticas` y hágalo **público**. El repositorio debe
   ser público para que los botones de Colab funcionen.

   ```bash
   gh repo create campos_ondas_electromagneticas --public --source=. --remote=origin
   ```

2. En GitHub, vaya a **Settings → Pages** y, en *Source*, elija
   **GitHub Actions** (no «Deploy from a branch»).

3. Haga el primer envío:

   ```bash
   git init
   git add .
   git commit -m "Sitio del curso: Unidad 1"
   git branch -M main
   git remote add origin https://github.com/gsilvaoelker/campos_ondas_electromagneticas.git
   git push -u origin main
   ```

4. Siga el progreso en la pestaña **Actions**. La primera construcción tarda
   unos minutos porque instala todo el entorno.

**Si publica bajo otra cuenta o con otro nombre de repositorio**, hay que
actualizar tres lugares:

| Archivo | Qué cambiar |
|---|---|
| `_config.yml` | La clave `repository.url` |
| `unidad_01/*.ipynb` | La constante `URL_SRC` y el enlace del botón de Colab, en la primera celda de cada notebook |
| `README.md` | Los enlaces de este archivo |

---

## 4. Abrir los notebooks en Google Colab

Cada notebook comienza con un botón **Abrir en Google Colab**. El enlace tiene
esta forma:

```
https://colab.research.google.com/github/gsilvaoelker/campos_ondas_electromagneticas/blob/main/unidad_01/NOMBRE.ipynb
```

En Colab, la primera celda de código no encuentra la carpeta `src/` y descarga
los módulos necesarios desde
`https://raw.githubusercontent.com/.../main/src/`. Por eso el repositorio debe
ser **público** y el archivo debe estar ya en `main`.

Las demás dependencias —NumPy, SciPy, Matplotlib, SymPy y pandas— vienen
preinstaladas en Colab. **Los estudiantes no instalan nada.**

---

## 5. Agregar nuevos ejemplos

### 5.1 Un notebook nuevo en una unidad existente

1. Copie un notebook existente como plantilla y renómbrelo siguiendo el patrón
   `NN_tema_descriptivo.ipynb`.
2. Actualice la URL del botón de Colab en la primera celda (el nombre del
   archivo).
3. Actualice la lista `MODULOS` de la celda de preparación con los módulos que
   ese notebook necesite.
4. Respete las diez secciones numeradas; son la razón de que los estudiantes
   sepan siempre dónde buscar.
5. Agregue el archivo a `_toc.yml`, bajo la sección de su unidad.
6. Ejecútelo de principio a fin en un entorno limpio antes de hacer `push`.

### 5.2 Una unidad nueva

```bash
mkdir unidad_02
```

Cree `unidad_02/unidad_02.md` con la portada de la unidad y agregue el bloque
correspondiente a `_toc.yml`:

```yaml
  - caption: Unidad 2 — Ondas planas y propagación
    chapters:
      - file: unidad_02/unidad_02
        sections:
          - file: unidad_02/07_fasores_ondas_sin_perdidas
          - file: unidad_02/08_medios_con_perdidas
```

Los ejemplos fuente están en `../Ejemplos Python/semana_NN_*.py` de la carpeta
del curso.

### 5.3 Funciones reutilizables

Si una función se usa en **dos o más** notebooks, extráigala a `src/` en un
módulo nombrado por tema —no por semana— y añádala a la lista `MODULOS` de los
notebooks que la usen. Los módulos de `src/` no deben importarse entre sí más
allá de `constantes_fisicas`, para que la descarga en Colab siga siendo simple.

---

## Convenciones

- **Punto** como separador decimal en todo el material: `0.5`, nunca `0,5`.
- Nombres de variables, funciones y archivos **en español**, descriptivos.
- Solo NumPy, SciPy, Matplotlib, SymPy y pandas. Sin dependencias exóticas.
- Una sola celda de parámetros por notebook, en la sección 5, claramente rotulada.
- Las constantes físicas viven únicamente en `src/constantes_fisicas.py`.

## Licencia y créditos

Material docente de Gerardo Silva-Oelker, Universidad Mayor, 2026.
Texto guía: Ulaby & Ravaioli, *Fundamentals of Applied Electromagnetics*, 7.ª ed.
