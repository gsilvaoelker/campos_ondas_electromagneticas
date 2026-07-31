"""Relajación de carga y condiciones de borde entre dos medios.

Se usa en las semanas 4 y 6 de la Unidad 1.
"""
import numpy as np

from constantes_fisicas import EPSILON_0


# --------------------------------------------------------------------------
# Relajación de carga en un medio óhmico homogéneo
# --------------------------------------------------------------------------
def tiempo_de_relajacion(permitividad_relativa, conductividad):
    """Constante de tiempo tau = epsilon / sigma [s]."""
    return EPSILON_0 * permitividad_relativa / conductividad


def densidad_de_carga_relajacion(t, densidad_inicial, tau):
    """rho_v(t) = rho_0 exp(-t / tau) [C/m^3]."""
    t = np.asarray(t, dtype=float)
    return densidad_inicial * np.exp(-t / tau)


def divergencia_corriente_relajacion(densidad_carga, tau):
    """div(J) = -d rho_v/dt = rho_v / tau [A/m^3], por la ecuación de continuidad."""
    return densidad_carga / tau


# --------------------------------------------------------------------------
# Interfaz dieléctrico-dieléctrico sin carga libre superficial
# --------------------------------------------------------------------------
def campo_normal_transmitido(campo_normal_1, permitividad_relativa_1, permitividad_relativa_2):
    """E_2n a partir de E_1n usando la continuidad de D_n [V/m].

        eps_1 E_1n = eps_2 E_2n   ->   E_2n = (eps_r1 / eps_r2) E_1n
    """
    return permitividad_relativa_1 / permitividad_relativa_2 * campo_normal_1


def densidad_flujo_normal(campo_normal, permitividad_relativa):
    """D_n = eps_0 eps_r E_n [C/m^2]."""
    return EPSILON_0 * permitividad_relativa * campo_normal


def campo_transmitido(campo_1, permitividad_relativa_1, permitividad_relativa_2, eje_normal=2):
    """Aplica ambas condiciones de borde a un vector E completo.

    La componente indicada por `eje_normal` es la normal a la interfaz (se
    escala); las otras dos son tangenciales y se conservan, porque E_1t = E_2t.
    """
    campo_2 = np.array(campo_1, dtype=float)
    campo_2[eje_normal] = campo_normal_transmitido(
        campo_1[eje_normal], permitividad_relativa_1, permitividad_relativa_2
    )
    return campo_2
