"""Líneas de transmisión: reflexión, ROE, impedancia de entrada y adaptación.

Se usa en las semanas 12, 13, 14, 16 y 17 de la Unidad 3.

Los parámetros por unidad de longitud de un coaxial (C' y L') están en
`campos_electrostaticos.py`, porque se calculan con la electrostática de la
Unidad 1: son la misma estructura vista con otra pregunta.
"""
import numpy as np


def coeficiente_reflexion(impedancia_carga, impedancia_caracteristica):
    """Gamma = (Z_L - Z_0) / (Z_L + Z_0), adimensional y en general complejo.

    Vale 0 cuando la carga está adaptada, +1 en circuito abierto y -1 en
    cortocircuito.
    """
    return ((impedancia_carga - impedancia_caracteristica)
            / (impedancia_carga + impedancia_caracteristica))


def razon_onda_estacionaria(coeficiente):
    """ROE = (1 + |Gamma|) / (1 - |Gamma|), adimensional.

    Vale 1 con adaptación perfecta. Con reflexión total —cortocircuito, circuito
    abierto o cualquier carga puramente reactiva— se tiene |Gamma| = 1 y la ROE
    es infinita: se devuelve `inf` en vez de fallar, porque ése es el valor
    correcto y es un caso que aparece a menudo.
    """
    modulo = np.abs(coeficiente)
    with np.errstate(divide="ignore", invalid="ignore"):
        resultado = np.where(modulo >= 1.0, np.inf, (1.0 + modulo) / (1.0 - modulo))
    return resultado if np.ndim(coeficiente) else float(resultado)


def impedancia_entrada(impedancia_carga, impedancia_caracteristica, beta_por_longitud):
    """Impedancia vista a la entrada de una línea sin pérdidas [ohm].

        Z_in = Z_0 (Z_L + j Z_0 tan(beta l)) / (Z_0 + j Z_L tan(beta l))

    `beta_por_longitud` es el producto beta*l en radianes (la longitud
    eléctrica de la línea).
    """
    tangente = np.tan(beta_por_longitud)
    return impedancia_caracteristica * (
        (impedancia_carga + 1.0j * impedancia_caracteristica * tangente)
        / (impedancia_caracteristica + 1.0j * impedancia_carga * tangente)
    )


def longitud_electrica(longitud_sobre_lambda):
    """Convierte l/lambda en beta*l [rad]: beta l = 2 pi (l / lambda)."""
    return 2.0 * np.pi * longitud_sobre_lambda


def impedancia_cuarto_de_onda(impedancia_fuente, impedancia_carga):
    """Impedancia del transformador de cuarto de onda: Z_t = sqrt(Z_S Z_L) [ohm]."""
    return np.sqrt(impedancia_fuente * impedancia_carga)


def potencia_incidente(voltaje_rms, impedancia_caracteristica):
    """Potencia que la fuente lanza hacia la carga [W]: P = |V+|^2 / Z_0."""
    return abs(voltaje_rms) ** 2 / impedancia_caracteristica


def voltaje_en_la_linea(voltaje_incidente, coeficiente, distancia_sobre_lambda):
    """Fasor de voltaje a lo largo de la línea, en función de la distancia a la carga.

        V = V+ ( exp(-j 2 pi u) + Gamma exp(+j 2 pi u) ),   u = distancia / lambda

    La suma de la onda que va y la que vuelve produce el patrón de onda
    estacionaria.
    """
    u = np.asarray(distancia_sobre_lambda, dtype=float)
    return voltaje_incidente * (
        np.exp(-1.0j * 2.0 * np.pi * u) + coeficiente * np.exp(1.0j * 2.0 * np.pi * u)
    )
