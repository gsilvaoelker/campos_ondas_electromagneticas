"""Reflexión y transmisión en una interfaz plana: Snell, Fresnel y Brewster.

Se usa en las semanas 10, 11 y 17.
"""
import numpy as np


# --------------------------------------------------------------------------
# Incidencia normal
# --------------------------------------------------------------------------
def coeficiente_reflexion_normal(n1, n2):
    """Gamma = (n1 - n2) / (n1 + n2), adimensional.

    Es negativo cuando la onda entra a un medio más denso: la onda reflejada
    sale invertida.
    """
    return (n1 - n2) / (n1 + n2)


def coeficiente_transmision_normal(n1, n2):
    """tau = 1 + Gamma, adimensional. El campo total debe ser continuo."""
    return 1.0 + coeficiente_reflexion_normal(n1, n2)


def reflectancia_normal(n1, n2):
    """Fracción de potencia que se devuelve: R = |Gamma|^2."""
    return abs(coeficiente_reflexion_normal(n1, n2)) ** 2


def transmitancia_normal(n1, n2):
    """Fracción de potencia que pasa: T = (n2/n1) |tau|^2. Siempre R + T = 1."""
    return n2 / n1 * abs(coeficiente_transmision_normal(n1, n2)) ** 2


# --------------------------------------------------------------------------
# Incidencia oblicua
# --------------------------------------------------------------------------
def coeficientes_fresnel(n1, n2, angulo_incidencia):
    """Coeficientes de reflexión para las dos polarizaciones.

    `angulo_incidencia` en radianes. Devuelve (r_perpendicular, r_paralelo,
    cos_transmitido). Se usa `np.emath.sqrt` para que el coseno transmitido
    pueda volverse imaginario más allá del ángulo crítico, que es lo que
    describe la reflexión interna total.
    """
    seno_t = n1 / n2 * np.sin(angulo_incidencia)
    coseno_t = np.emath.sqrt(1.0 - seno_t**2)
    coseno_i = np.cos(angulo_incidencia)
    r_perpendicular = (n1 * coseno_i - n2 * coseno_t) / (n1 * coseno_i + n2 * coseno_t)
    r_paralelo = (n2 * coseno_i - n1 * coseno_t) / (n2 * coseno_i + n1 * coseno_t)
    return r_perpendicular, r_paralelo, coseno_t


def angulo_transmitido(n1, n2, angulo_incidencia):
    """Ángulo de refracción [rad] según la ley de Snell: n1 sin(t_i) = n2 sin(t_t)."""
    return np.arcsin(n1 / n2 * np.sin(angulo_incidencia))


def angulo_critico(n1, n2):
    """Ángulo crítico [rad]: sin(theta_c) = n2/n1. Solo existe si n1 > n2."""
    return np.arcsin(n2 / n1)


def angulo_brewster(n1, n2):
    """Ángulo de Brewster [rad]: tan(theta_B) = n2/n1.

    Es el ángulo en que la polarización paralela no se refleja en absoluto.
    """
    return np.arctan(n2 / n1)
