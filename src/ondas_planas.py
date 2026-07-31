"""Ondas planas uniformes en medios sin pérdidas.

Se usa en las semanas 7 y 11 de la Unidad 2.
"""
import numpy as np

from constantes_fisicas import EPSILON_0, MU_0, VELOCIDAD_LUZ, IMPEDANCIA_VACIO


def velocidad_propagacion(permitividad_relativa=1.0, permeabilidad_relativa=1.0):
    """Velocidad de la onda en el medio [m/s]: u = c / sqrt(eps_r mu_r)."""
    return VELOCIDAD_LUZ / np.sqrt(permitividad_relativa * permeabilidad_relativa)


def numero_de_onda(frecuencia, permitividad_relativa=1.0, permeabilidad_relativa=1.0):
    """Constante de fase beta [rad/m]: beta = omega / u = 2 pi / lambda."""
    velocidad = velocidad_propagacion(permitividad_relativa, permeabilidad_relativa)
    return 2.0 * np.pi * frecuencia / velocidad


def longitud_de_onda(frecuencia, permitividad_relativa=1.0, permeabilidad_relativa=1.0):
    """Longitud de onda lambda [m]: distancia entre dos crestas consecutivas."""
    velocidad = velocidad_propagacion(permitividad_relativa, permeabilidad_relativa)
    return velocidad / frecuencia


def impedancia_intrinseca(permitividad_relativa=1.0, permeabilidad_relativa=1.0):
    """Impedancia intrínseca eta [ohm]: cuánto vale E dividido por H en el medio."""
    return IMPEDANCIA_VACIO * np.sqrt(permeabilidad_relativa / permitividad_relativa)


def campo_instantaneo(amplitud, frecuencia, z, t, fase_inicial=0.0,
                      permitividad_relativa=1.0, permeabilidad_relativa=1.0):
    """Valor de E(z, t) = E_0 cos(omega t - beta z + fase_inicial) [V/m]."""
    omega = 2.0 * np.pi * frecuencia
    beta = numero_de_onda(frecuencia, permitividad_relativa, permeabilidad_relativa)
    return amplitud * np.cos(omega * t - beta * np.asarray(z, dtype=float) + fase_inicial)
