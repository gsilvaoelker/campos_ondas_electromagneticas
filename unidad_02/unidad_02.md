# Unidad 2 — Ondas planas y propagación

## De qué se trata

En la Unidad 1 los campos estaban quietos. Acá los dejamos moverse.

Cuando se combinan la ley de Faraday y la de Ampère con corriente de
desplazamiento, aparece algo que no estaba en ninguna de las dos por separado:
una **onda**. Un campo eléctrico que cambia genera uno magnético, que al cambiar
genera uno eléctrico, y así la perturbación se sostiene a sí misma y viaja.

Esta unidad estudia esa onda: cómo se escribe, a qué velocidad va, cómo se apaga
en un material que conduce, en qué dirección apunta su campo, y qué le pasa
cuando choca con un cambio de medio.

No hay ecuaciones nuevas. Son las mismas cuatro de Maxwell, resueltas para otro
caso.

## Los notebooks

**[Fasores y ondas planas](07_fasores_y_ondas_planas.ipynb)**
Cómo escribir una onda de forma compacta, cuánto mide, y por qué $\mathbf{E}$ y
$\mathbf{H}$ están amarrados por un solo número: la impedancia del medio.

**[Medios con pérdidas](08_medios_con_perdidas.ipynb)**
Qué pasa cuando el material conduce. Por qué la onda no entra en el cobre pero sí
atraviesa una pared, y por qué en alta frecuencia la corriente viaja por la
superficie del cable.

**[Polarización y el píxel LCD](09_polarizacion_y_pixel_lcd.ipynb)**
Hacia dónde apunta el campo mientras la onda avanza. Y cómo una pantalla usa eso
para encender y apagar cada píxel.

**[Snell, Fresnel y Brewster](10_snell_fresnel_y_brewster.ipynb)**
Qué pasa cuando la onda llega a una interfaz: cuánto se refleja, cuánto pasa, por
qué la fibra óptica funciona y por qué existen los lentes de sol polarizados.

**[Repaso de la unidad](11_repaso_prueba_2.ipynb)**
Una onda que se apaga en un medio con pérdidas y una interfaz vista justo en el
ángulo de Brewster.

## Al terminar debería poder

- Escribir una onda plana como fasor y volver al dominio del tiempo.
- Calcular $\beta$, $\lambda$ y $\eta$ para cualquier medio.
- Obtener $\gamma = \alpha + j\beta$ en un medio con pérdidas y estimar la
  profundidad de penetración.
- Reconocer si una polarización es lineal, circular o elíptica, y calcular su
  razón axial.
- Aplicar la ley de Snell y los coeficientes de Fresnel, y encontrar los ángulos
  crítico y de Brewster.
- Verificar que la potencia se conserva en cualquier interfaz.

## Lo que se conecta con la Unidad 1

Los coeficientes de Fresnel no son una fórmula nueva que haya que memorizar:
salen de exigir las condiciones de borde de la semana 4 sobre una interfaz. Si
alguna vez las olvida, puede volver a deducirlas.
