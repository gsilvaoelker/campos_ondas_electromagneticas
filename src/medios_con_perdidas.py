"""Propagación en medios con pérdidas: atenuación, efecto pelicular y potencia.

Se usa en las semanas 8 y 11 de la Unidad 2.
"""
import numpy as np

from constantes_fisicas import EPSILON_0, MU_0


def conductividad_equivalente(frecuencia, permitividad_relativa, tangente_de_perdidas):
    """Conductividad sigma [S/m] que produce la tangente de pérdidas indicada.

        tan(delta) = sigma / (omega epsilon)   ->   sigma = omega epsilon tan(delta)
    """
    omega = 2.0 * np.pi * frecuencia
    return omega * EPSILON_0 * permitividad_relativa * tangente_de_perdidas


def constante_propagacion(frecuencia, permitividad_relativa, conductividad,
                          permeabilidad_relativa=1.0):
    """Constante de propagación compleja gamma = alpha + j beta [1/m].

        gamma = sqrt( j omega mu (sigma + j omega epsilon) )

    La parte real atenúa la onda y la parte imaginaria le da la fase.
    """
    omega = 2.0 * np.pi * frecuencia
    epsilon = EPSILON_0 * permitividad_relativa
    mu = MU_0 * permeabilidad_relativa
    return np.sqrt(1.0j * omega * mu * (conductividad + 1.0j * omega * epsilon))


def impedancia_intrinseca_compleja(frecuencia, permitividad_relativa, conductividad,
                                   permeabilidad_relativa=1.0):
    """Impedancia intrínseca compleja eta [ohm].

        eta = sqrt( j omega mu / (sigma + j omega epsilon) )

    Su fase distinta de cero indica que E y H ya no están en fase.
    """
    omega = 2.0 * np.pi * frecuencia
    epsilon = EPSILON_0 * permitividad_relativa
    mu = MU_0 * permeabilidad_relativa
    return np.sqrt(1.0j * omega * mu / (conductividad + 1.0j * omega * epsilon))


# --------------------------------------------------------------------------
# Buen conductor: sigma >> omega epsilon
# --------------------------------------------------------------------------
def atenuacion_buen_conductor(frecuencia, conductividad, permeabilidad_relativa=1.0):
    """En un buen conductor alpha = beta = sqrt(pi f mu sigma) [1/m]."""
    mu = MU_0 * permeabilidad_relativa
    return np.sqrt(np.pi * frecuencia * mu * conductividad)


def profundidad_de_penetracion(frecuencia, conductividad, permeabilidad_relativa=1.0):
    """Profundidad pelicular delta = 1 / alpha [m].

    Es la distancia en la que la amplitud cae al 36.8 % (un factor 1/e).
    """
    return 1.0 / atenuacion_buen_conductor(frecuencia, conductividad, permeabilidad_relativa)


def impedancia_buen_conductor(frecuencia, conductividad, permeabilidad_relativa=1.0):
    """Impedancia de un buen conductor: eta = (1 + j) sqrt(pi f mu / sigma) [ohm].

    Su fase es siempre 45 grados: H se atrasa un octavo de ciclo respecto de E.
    """
    mu = MU_0 * permeabilidad_relativa
    return (1.0 + 1.0j) * np.sqrt(np.pi * frecuencia * mu / conductividad)


# --------------------------------------------------------------------------
# Potencia
# --------------------------------------------------------------------------
def potencia_promedio(amplitud_campo, impedancia):
    """Vector de Poynting promedio [W/m^2]: S = |E_0|^2 Re(1/eta*) / 2."""
    return 0.5 * abs(amplitud_campo) ** 2 * np.real(1.0 / np.conj(impedancia))


def velocidad_de_fase(frecuencia, gamma):
    """Velocidad de fase [m/s]: u_p = omega / beta, con beta = Im(gamma)."""
    return 2.0 * np.pi * frecuencia / np.imag(gamma)
