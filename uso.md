# Cómo usar este material

## Los cuatro pasos

1. Abra un notebook desde el menú de la izquierda.
2. Pulse **Abrir en Google Colab**, arriba de todo.
3. En Colab: *Entorno de ejecución → Ejecutar todas* (o `Ctrl+F9`).
4. Baje a la sección **5. Parámetros modificables**, cambie un número y ejecute
   de nuevo.

No hay que instalar nada. Solo una cuenta de Google y un navegador.

## Todos los notebooks tienen la misma forma

Así usted siempre sabe dónde buscar.

| Sección | Qué hay ahí |
|---|---|
| 1. Objetivos | Qué va a poder hacer al terminar |
| 2. De dónde sale todo esto | El razonamiento detrás de las fórmulas |
| 3. Ecuaciones | El formulario del problema |
| 4. Qué significa físicamente | Para qué sirve cada cosa |
| **5. Parámetros modificables** | **La única celda que conviene tocar** |
| 6. Implementación | Cómo se pasa de la física al código |
| 7. Resultados numéricos | Los valores, en tablas |
| 8. Visualización | Los gráficos |
| 9. Qué nos dicen los resultados | Cómo leer lo que salió |
| 10. Ejercicios | Qué probar después |

## Cómo sacarle provecho

**Prediga antes de ejecutar.** Cuando un ejercicio le pide cambiar un parámetro,
escriba primero qué cree que va a pasar. Después ejecute. Cuando se equivoque,
ahí aprendió algo.

**Cambie un parámetro a la vez.** Si cambia tres, no va a saber cuál causó qué.

**Use los notebooks para revisar sus desarrollos.** Resuelva el problema a mano,
después ejecute y compare. Los resultados numéricos son los mismos que los del
problema hecho en clase.

**Si algo no cuadra, sospeche de sus unidades.** Es el error más frecuente:
metros contra centímetros, grados contra radianes.

## La primera celda de código

Cada notebook empieza con una celda de preparación. Detecta si usted está en
Colab y, si es así, descarga los módulos del curso. Debe ejecutarse antes que las
demás; si usa *Ejecutar todas*, se resuelve sola.

## Las funciones del curso

Las fórmulas que se repiten entre semanas no están escritas dentro de cada
notebook, sino en una carpeta `src/` común:

| Módulo | Qué contiene |
|---|---|
| `constantes_fisicas.py` | $\varepsilon_0$, $\mu_0$, $c$, $\eta_0$, carga elemental |
| `transformaciones_coordenadas.py` | Cambios entre sistemas de coordenadas |
| `campos_electrostaticos.py` | Esfera cargada, condensador, coaxial, energías |
| `medios_y_condiciones_de_borde.py` | Relajación de carga y condiciones de borde |
| `ondas_planas.py` | $\beta$, $\lambda$, $\eta$ y campos en medios sin pérdidas |
| `medios_con_perdidas.py` | Atenuación, efecto pelicular y potencia |
| `interfaces_planas.py` | Snell, Fresnel, ángulos crítico y de Brewster |
| `lineas_transmision.py` | Reflexión, ROE, impedancia de entrada, adaptación |
| `guias_y_antenas.py` | Frecuencias de corte, eficiencia y ganancia |
| `utilidades_notebook.py` | Estilo de las figuras y formato de las tablas |

Esto tiene una ventaja concreta para usted: cuando la semana 12 vuelve a usar el
coaxial de la semana 3, es literalmente el mismo código. Los resultados no pueden
contradecirse.

## Guardar sus cambios

Colab **no guarda** lo que usted modifique. Si quiere conservarlo, use
*Archivo → Guardar una copia en Drive* antes de empezar.

## Punto decimal

Todo el material usa **punto**, como Python: `0.5`, no `0,5`.

## Si algo falla

| Problema | Solución |
|---|---|
| No aparece una figura | Ejecute las celdas en orden desde el principio |
| `NameError` con un parámetro | Le faltó ejecutar la sección 5 |
| `ModuleNotFoundError` | Vuelva a ejecutar la primera celda de código |
| Cualquier otra cosa | *Entorno de ejecución → Reiniciar y ejecutar todas* |
