# Campos y Ondas Electromagnéticas

**ICEE1033 — Escuela de Ingeniería, Universidad Mayor**
Profesor: Gerardo Silva-Oelker

---

Este sitio reúne los ejemplos computacionales del curso. Cada notebook resuelve
los mismos problemas que se desarrollan analíticamente en clase, pero permite
además **cambiar los parámetros y ver qué pasa**.

Los notebooks no reemplazan el desarrollo a mano: lo verifican. La idea es que
usted resuelva el problema en papel, lo ejecute aquí, y compare.

## Cómo empezar

Cada notebook tiene arriba un botón que lo abre en Google Colab. No necesita
instalar Python ni ninguna otra herramienta: basta una cuenta de Google y un
navegador. Consulte [Cómo usar este material](uso.md) para los detalles.

## Estructura del curso

El curso se organiza en tres unidades, evaluadas con tres pruebas presenciales.

| Unidad | Semanas | Contenido | Evaluación |
|---|---|---|---|
| **1** | 1–5 | Álgebra y cálculo vectorial, modelo electromagnético, campos cuasiestáticos, ecuaciones de Maxwell y condiciones de borde | Prueba 1 (30 %) |
| 2 | 7–11 | Ondas planas, medios con pérdidas, polarización, reflexión y transmisión | Prueba 2 (35 %) |
| 3 | 12–16 | Líneas de transmisión, ondas estacionarias, adaptación, guías de onda y antenas | Prueba 3 (35 %) |

Por ahora este sitio cubre la **Unidad 1**. Las unidades 2 y 3 se incorporarán
durante el semestre.

## Contenido disponible

### Unidad 1 — Campos estáticos y ecuaciones de Maxwell

| Semana | Notebook | Tema |
|---|---|---|
| 1 | [Álgebra vectorial, coordenadas y gradiente](unidad_01/01_algebra_vectorial_coordenadas_gradiente.ipynb) | Cambio de base cilíndrica–cartesiana; $\mathbf{E} = -\nabla V$ |
| 2 | [Gauss, Stokes, campos y fuentes](unidad_01/02_gauss_stokes_campos_y_fuentes.ipynb) | Esfera cargada; Ampère–Stokes; Ohm; Lorentz |
| 3 | [Capacitancia, inductancia y energía](unidad_01/03_capacitancia_inductancia_energia.ipynb) | Placas paralelas; línea coaxial; $Z_0$ y $u_p$ |
| 4 | [Continuidad, Maxwell y condiciones de borde](unidad_01/04_continuidad_maxwell_condiciones_de_borde.ipynb) | Relajación de carga; refracción del campo |
| 5 | [Repaso para la Prueba 1](unidad_01/05_repaso_prueba_1.ipynb) | Potencial de la esfera; corriente de desplazamiento |
| 6 | [Síntesis de Maxwell y bordes](unidad_01/06_sintesis_maxwell_y_bordes.ipynb) | Auditoría de las cuatro ecuaciones (opcional) |

## Sobre las herramientas

Los cálculos usan NumPy y SciPy, las figuras Matplotlib, las derivadas
simbólicas SymPy y las tablas de resultados pandas. Todas vienen preinstaladas
en Google Colab.

## Referencia

El texto guía del curso es Ulaby & Ravaioli, *Fundamentals of Applied
Electromagnetics*, 7.ª edición. Las demostraciones interactivas citadas en el
calendario corresponden a los módulos que acompañan ese texto.
