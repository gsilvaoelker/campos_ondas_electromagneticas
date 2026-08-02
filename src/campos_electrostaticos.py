"""Electrostática y magnetostática cuasiestática de la Unidad 1.

Reúne las expresiones cerradas que aparecen en las semanas 2, 3 y 5:
esfera con carga volumétrica uniforme, condensador de placas paralelas y
línea coaxial.
"""
import numpy as np

from constantes_fisicas import EPSILON_0, MU_0


# --------------------------------------------------------------------------
# Esfera con densidad de carga volumétrica uniforme
# --------------------------------------------------------------------------
def carga_total_esfera_uniforme(radio, densidad_carga):
    """Carga encerrada [C] en una esfera de radio `radio` [m] con rho_v uniforme [C/m^3]."""
    return densidad_carga * 4.0 * np.pi * radio**3 / 3.0


def densidad_flujo_esfera_uniforme(r, radio, densidad_carga):
    """Componente radial de D [C/m^2] a la distancia `r` [m].

    Ley de Gauss sobre una superficie esférica de radio r:
        r <  a:  D = rho_v * r / 3
        r >= a:  D = Q / (4 pi r^2)
    """
    r = np.asarray(r, dtype=float)
    carga_total = carga_total_esfera_uniforme(radio, densidad_carga)
    exterior = np.zeros_like(r, dtype=float)
    np.divide(
        carga_total,
        4.0 * np.pi * r**2,
        out=exterior,
        where=r != 0.0,
    )
    return np.where(
        r < radio,
        densidad_carga * r / 3.0,
        exterior,
    )


def campo_esfera_uniforme(r, radio, densidad_carga, permitividad=EPSILON_0):
    """Componente radial de E [V/m] a la distancia `r` [m], con E = D / epsilon."""
    return densidad_flujo_esfera_uniforme(r, radio, densidad_carga) / permitividad


def potencial_esfera_uniforme(r, radio, densidad_carga, permitividad=EPSILON_0):
    """Potencial electrostático [V] con referencia V(infinito) = 0.

        r <  a:  V = rho_v (3 a^2 - r^2) / (6 epsilon)
        r >= a:  V = Q / (4 pi epsilon r)

    En r = a ambas ramas valen rho_v a^2 / (3 epsilon); en r = 0 la rama interior
    vale rho_v a^2 / (2 epsilon).
    """
    r = np.asarray(r, dtype=float)
    carga_total = carga_total_esfera_uniforme(radio, densidad_carga)
    exterior = np.divide(
        carga_total,
        4.0 * np.pi * permitividad * np.where(r == 0.0, 1.0, r),
    )
    return np.where(
        r < radio,
        densidad_carga * (3.0 * radio**2 - r**2) / (6.0 * permitividad),
        exterior,
    )


# --------------------------------------------------------------------------
# Condensador de placas paralelas
# --------------------------------------------------------------------------
def capacitancia_placas_paralelas(area, separacion, permitividad_relativa=1.0):
    """Capacitancia [F] de dos placas de área `area` [m^2] separadas `separacion` [m]."""
    return EPSILON_0 * permitividad_relativa * area / separacion


# --------------------------------------------------------------------------
# Línea coaxial (por unidad de longitud)
# --------------------------------------------------------------------------
def capacitancia_coaxial(radio_interno, radio_externo, permitividad_relativa=1.0):
    """Capacitancia por unidad de longitud C' [F/m] de un coaxial."""
    return 2.0 * np.pi * EPSILON_0 * permitividad_relativa / np.log(radio_externo / radio_interno)


def inductancia_coaxial(radio_interno, radio_externo, permeabilidad_relativa=1.0):
    """Inductancia por unidad de longitud L' [H/m] de un coaxial."""
    return MU_0 * permeabilidad_relativa * np.log(radio_externo / radio_interno) / (2.0 * np.pi)


# --------------------------------------------------------------------------
# Energía almacenada
# --------------------------------------------------------------------------
def energia_electrica(capacitancia, voltaje):
    """Energía electrostática W_e = C V^2 / 2 [J]."""
    return 0.5 * capacitancia * voltaje**2


def energia_magnetica(inductancia, corriente):
    """Energía magnetostática W_m = L I^2 / 2 [J]."""
    return 0.5 * inductancia * corriente**2
