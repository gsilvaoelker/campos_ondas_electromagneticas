# Unidad 3 — Líneas de transmisión, guías y antenas

## De qué se trata

Las dos primeras unidades explican qué son los campos y cómo se propagan. Ésta
responde la pregunta práctica: **¿cómo llevo esa onda hasta donde la necesito?**

Hay tres respuestas, y cada una es un tema de la unidad:

- Por un **cable**, si es de baja potencia y corta distancia. Pero cuando el
  cable es comparable a la longitud de onda, deja de comportarse como un cable:
  es una línea de transmisión.
- Por una **guía de onda**, un tubo metálico hueco, cuando la potencia es alta y
  la frecuencia también.
- Por el **aire**, radiándola con una antena.

## Los notebooks

**[Líneas de transmisión](12_lineas_de_transmision.ipynb)**
Cuándo un cable deja de ser un cable. Qué es la impedancia característica y por
qué la línea transforma la impedancia de la carga.

**[Ondas estacionarias y adaptación](13_ondas_estacionarias_y_adaptacion.ipynb)**
Qué patrón aparece cuando parte de la onda vuelve, qué es la ROE, y cómo adaptar
con un tramo de un cuarto de longitud de onda.

**[Carta de Smith y radiación](14_carta_de_smith_y_radiacion.ipynb)**
Cómo leer impedancias sin calcular nada. Y los campos de la antena más simple que
existe: el dipolo hertziano.

**[Guías de onda y antenas](15_guias_de_onda_y_antenas.ipynb)**
Por qué una guía no deja pasar frecuencias bajas, qué es un modo, y qué tan
eficiente es realmente una antena corta.

**[Repaso de la unidad](16_repaso_prueba_3.ipynb)**
Una línea, una guía y una antena en un mismo problema, con una receta para
abordar cualquiera de los tres.

## Al terminar debería poder

- Calcular $Z_0$ y $u_p$ de una línea a partir de $C'$ y $L'$.
- Obtener $\Gamma$, la ROE y $Z_{\text{in}}$ de cualquier carga.
- Hacer el balance de potencia de una línea desadaptada.
- Diseñar un transformador de cuarto de onda.
- Ubicar una impedancia en la carta de Smith y leer $|\Gamma|$ y la ROE.
- Calcular frecuencias de corte y decidir si una guía trabaja en régimen
  monomodo.
- Evaluar la eficiencia y la ganancia de una antena corta.

## Lo que se conecta con las unidades anteriores

Dos cosas que conviene notar:

Primero, $C'$ y $L'$ del cable coaxial son exactamente los que usted calculó en
la semana 3 con electrostática. La estructura es la misma; lo que cambió es la
pregunta.

Segundo, el coeficiente de reflexión de una carga,

$$
\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0},
$$

tiene la misma estructura de adaptación de impedancias que la reflexión en una
interfaz óptica. No se obtiene sustituyendo directamente $n$ por $Z$: para los
medios dieléctricos no magnéticos de la Unidad 2, la impedancia de onda es
inversamente proporcional al índice, $\eta\propto 1/n$. En ambos casos la
reflexión aparece por un desajuste en la frontera.
