# Campos y Ondas Electromagnéticas — sitio del curso

Material computacional del curso **ICEE1033**, Escuela de Ingeniería,
Universidad Mayor. Construido con [Jupyter Book](https://jupyterbook.org) y
publicado en GitHub Pages.

- **Sitio publicado:** https://gsilvaoelker.github.io/campos_ondas_electromagneticas/
- **Cobertura:** las tres unidades del curso, 17 notebooks

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
│   ├── constantes_fisicas.py                    Unidades 1, 2 y 3
│   ├── transformaciones_coordenadas.py          Unidad 1
│   ├── campos_electrostaticos.py                Unidades 1 y 3
│   ├── medios_y_condiciones_de_borde.py         Unidad 1
│   ├── ondas_planas.py                          Unidades 2 y 3
│   ├── medios_con_perdidas.py                   Unidad 2
│   ├── interfaces_planas.py                     Unidad 2 y repaso final
│   ├── lineas_transmision.py                    Unidad 3 y repaso final
│   ├── guias_y_antenas.py                       Unidad 3
│   └── utilidades_notebook.py                   Todas
├── unidad_01/    unidad_01.md + 01..06_*.ipynb
├── unidad_02/    unidad_02.md + 07..11_*.ipynb
├── unidad_03/    unidad_03.md + 12..16_*.ipynb
└── repaso_final/ 17_repaso_integrador.ipynb
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

Para verificar que los 17 notebooks se ejecutan de principio a fin:

```bash
python -m nbclient unidad_0*/*.ipynb repaso_final/*.ipynb
```

o, con más control:

```bash
jupyter nbconvert --to notebook --execute --inplace unidad_0*/*.ipynb repaso_final/*.ipynb
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

Para publicar un cambio basta con:

```bash
git add .
git commit -m "Descripción del cambio"
git push
```

La construcción tarda alrededor de un minuto. Puede seguirla con `gh run watch`
o en la pestaña **Actions** del repositorio.

**Configuración inicial — ya realizada, se documenta por si hay que rehacerla:**

1. Repositorio **público** (obligatorio: si es privado, los botones de Colab
   fallan al descargar los módulos de `src/`):

   ```bash
   gh repo create campos_ondas_electromagneticas --public --source=. --remote=origin
   ```

2. GitHub Pages en modo *GitHub Actions*, no «Deploy from a branch»:

   ```bash
   gh api repos/gsilvaoelker/campos_ondas_electromagneticas/pages -X POST -f build_type=workflow
   ```

   Equivale a **Settings → Pages → Source → GitHub Actions**. Este modo despliega
   por artefacto y no ejecuta Jekyll, que de otro modo ignoraría la carpeta
   `_static/` y dejaría el sitio sin CSS.

3. Primer envío:

   ```bash
   git init -b main && git add . && git commit -m "Sitio del curso"
   git push -u origin main
   ```

**Si publica bajo otra cuenta o con otro nombre de repositorio**, hay que
actualizar tres lugares:

| Archivo | Qué cambiar |
|---|---|
| `_config.yml` | La clave `repository.url` |
| `unidad_0*/*.ipynb`, `repaso_final/*.ipynb` | La constante `URL_SRC` y el enlace del botón de Colab, en la primera celda de cada notebook |
| `README.md` | Los enlaces de este archivo |

---

## 4. Abrir los notebooks en Google Colab

Cada notebook comienza con un botón **Abrir en Google Colab**. El enlace tiene
esta forma:

```
https://colab.research.google.com/github/gsilvaoelker/campos_ondas_electromagneticas/blob/main/CARPETA/NOMBRE.ipynb
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

Cree la carpeta, escriba su portada `unidad_NN.md` y agregue el bloque
correspondiente a `_toc.yml`:

```yaml
  - caption: Unidad 4 — Título de la unidad
    chapters:
      - file: unidad_04/unidad_04
        sections:
          - file: unidad_04/18_primer_tema
```

Los ejemplos fuente originales están en `../Ejemplos Python/semana_NN_*.py` de la
carpeta del curso.

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
