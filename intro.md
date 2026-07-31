# Campos y Ondas Electromagnéticas

**ICEE1033 — Escuela de Ingeniería, Universidad Mayor**
Profesor: Gerardo Silva-Oelker

---

Bienvenido. Acá están los ejemplos del curso convertidos en notebooks que usted
puede ejecutar y modificar.

La idea es simple: **resuelva el problema en papel, ejecútelo acá y compare**.
Si los números coinciden, su desarrollo está bien. Si no, ya sabe dónde buscar.

Cada notebook tiene una celda de parámetros. Cámbielos, vuelva a ejecutar y vea
qué pasa. Eso es lo que estos notebooks hacen mejor que un libro: dejan probar.

## Para empezar

Pulse el botón **Abrir en Google Colab** que aparece al comienzo de cada
notebook. No necesita instalar nada: solo una cuenta de Google y un navegador.

Si es su primera vez, lea [Cómo usar este material](uso.md). Son dos minutos.

## Contenido

### Unidad 1 — Campos estáticos y ecuaciones de Maxwell

| Notebook | De qué trata |
|---|---|
| [Álgebra vectorial, coordenadas y gradiente](unidad_01/01_algebra_vectorial_coordenadas_gradiente.ipynb) | Un mismo vector en dos sistemas de coordenadas, y cómo sacar $\mathbf{E}$ de un potencial |
| [Gauss, Stokes, campos y fuentes](unidad_01/02_gauss_stokes_campos_y_fuentes.ipynb) | Una esfera cargada, un conductor con corriente y la fuerza sobre un electrón |
| [Capacitancia, inductancia y energía](unidad_01/03_capacitancia_inductancia_energia.ipynb) | Cuánta carga y cuánta energía guarda un condensador y un cable coaxial |
| [Continuidad, Maxwell y condiciones de borde](unidad_01/04_continuidad_maxwell_condiciones_de_borde.ipynb) | Por qué la carga se va a la superficie, y qué le pasa al campo al cambiar de material |
| [Repaso de la unidad](unidad_01/05_repaso_prueba_1.ipynb) | Potencial de una esfera y corriente de desplazamiento |
| [Síntesis de Maxwell y bordes](unidad_01/06_sintesis_maxwell_y_bordes.ipynb) | Revisar las cuatro ecuaciones y encontrar cuál está incompleta |

### Unidad 2 — Ondas planas y propagación

| Notebook | De qué trata |
|---|---|
| [Fasores y ondas planas](unidad_02/07_fasores_y_ondas_planas.ipynb) | Cómo escribir una onda, cuánto mide y cómo se relacionan $\mathbf{E}$ y $\mathbf{H}$ |
| [Medios con pérdidas](unidad_02/08_medios_con_perdidas.ipynb) | Por qué la onda no entra en el cobre y sí atraviesa una pared |
| [Polarización y el píxel LCD](unidad_02/09_polarizacion_y_pixel_lcd.ipynb) | Cómo se mueve la punta del campo, y cómo una pantalla lo aprovecha |
| [Snell, Fresnel y Brewster](unidad_02/10_snell_fresnel_y_brewster.ipynb) | Cuánto se refleja, cuánto pasa, y por qué existen los lentes polarizados |
| [Repaso de la unidad](unidad_02/11_repaso_prueba_2.ipynb) | Una onda que se apaga y una interfaz en Brewster |

### Unidad 3 — Líneas, guías y antenas

| Notebook | De qué trata |
|---|---|
| [Líneas de transmisión](unidad_03/12_lineas_de_transmision.ipynb) | Cuándo un cable deja de ser un cable, y por qué transforma impedancias |
| [Ondas estacionarias y adaptación](unidad_03/13_ondas_estacionarias_y_adaptacion.ipynb) | Qué es la ROE y cómo adaptar con un tramo de cuarto de onda |
| [Carta de Smith y radiación](unidad_03/14_carta_de_smith_y_radiacion.ipynb) | Leer impedancias en la carta, y los campos de una antena |
| [Guías de onda y antenas](unidad_03/15_guias_de_onda_y_antenas.ipynb) | Por qué una guía tiene frecuencia de corte, y qué tan eficiente es una antena |
| [Repaso de la unidad](unidad_03/16_repaso_prueba_3.ipynb) | Línea, guía y antena en un solo problema |

### Repaso final

| Notebook | De qué trata |
|---|---|
| [Repaso integrador](repaso_final/17_repaso_integrador.ipynb) | Un problema de cada unidad, y el hilo que las une |

## Herramientas

Los cálculos usan NumPy y SciPy, las figuras Matplotlib, las derivadas
simbólicas SymPy y las tablas pandas. Todas vienen ya instaladas en Colab.

## Texto guía

Ulaby & Ravaioli, *Fundamentals of Applied Electromagnetics*, 7.ª edición.
