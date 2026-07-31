# Cómo usar este material

## Lo mínimo que necesita saber

1. Abra cualquier notebook desde el menú de la izquierda.
2. Pulse el botón **Abrir en Google Colab** que aparece al comienzo de la página.
3. En Colab, elija *Entorno de ejecución → Ejecutar todas* (o `Ctrl+F9`).
4. Baje hasta la sección **5. Parámetros modificables**, cambie un valor y vuelva
   a ejecutar.

No necesita instalar Python, ni Jupyter, ni ninguna biblioteca. Solo una cuenta
de Google y un navegador.

## Estructura de cada notebook

Todos los notebooks siguen el mismo orden, para que usted sepa siempre dónde
buscar:

| Sección | Qué encontrará |
|---|---|
| 1. Objetivos de aprendizaje | Qué debería poder hacer al terminar |
| 2. Fundamentos teóricos | De dónde salen las ecuaciones |
| 3. Ecuaciones relevantes | El formulario del problema |
| 4. Explicación física | Qué significan las ecuaciones |
| **5. Parámetros modificables** | **La única celda que conviene editar** |
| 6. Implementación del código | Cómo se traduce la física a Python |
| 7. Resultados numéricos | Tablas con los valores obtenidos |
| 8. Visualización | Las figuras |
| 9. Interpretación física | Qué dicen los resultados |
| 10. Ejercicios | Qué probar a continuación |

## La celda de preparación del entorno

La primera celda de código de cada notebook detecta si usted está en Colab y, de
ser así, descarga los módulos del curso desde GitHub. Esa celda debe ejecutarse
antes que las demás; si usa *Ejecutar todas*, se resuelve sola.

Si aparece un error de red al ejecutarla, revise su conexión y vuelva a
ejecutarla. Todas las demás dependencias ya están en Colab.

## Los módulos del curso

Las funciones que se repiten entre semanas viven en la carpeta `src/` del
repositorio, no dentro de los notebooks:

| Módulo | Contenido |
|---|---|
| `constantes_fisicas.py` | $\varepsilon_0$, $\mu_0$, $c$, $\eta_0$, carga elemental |
| `transformaciones_coordenadas.py` | Cambios de base entre sistemas coordenados |
| `campos_electrostaticos.py` | Esfera cargada, condensador, línea coaxial, energías |
| `medios_y_condiciones_de_borde.py` | Relajación de carga, condiciones de borde |
| `utilidades_notebook.py` | Estilo de las figuras y formato de las tablas |

Así, cuando la semana 5 vuelve a usar el campo de la esfera cargada de la semana
2, es literalmente el mismo código: los resultados no pueden discrepar.

## Guardar sus cambios

Colab **no guarda** sus modificaciones en este sitio. Si quiere conservarlas, use
*Archivo → Guardar una copia en Drive* antes de empezar a editar.

## Sobre el separador decimal

Todo el material usa **punto** como separador decimal, siguiendo la convención
de Python y de la literatura técnica: `0.5`, no `0,5`.

## Si algo no funciona

- **Una figura no aparece:** ejecute las celdas en orden desde el principio.
- **`NameError` con un parámetro:** ejecutó una celda sin haber ejecutado antes
  la sección 5.
- **`ModuleNotFoundError`:** falló la celda de preparación del entorno;
  ejecútela de nuevo.
- **Cualquier otra cosa:** *Entorno de ejecución → Reiniciar y ejecutar todas*
  resuelve la mayoría de los problemas.
