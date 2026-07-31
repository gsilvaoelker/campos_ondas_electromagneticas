"""Cambios de base entre sistemas coordenados ortogonales.

Los vectores unitarios cilíndricos dependen de la posición:

    a_rho = cos(phi) a_x + sin(phi) a_y
    a_phi = -sin(phi) a_x + cos(phi) a_y
    a_z   = a_z

por lo que un mismo vector tiene componentes distintas según el punto donde se
evalúe. Estas funciones aplican esa rotación de forma explícita.
"""
import numpy as np


def cilindricas_a_cartesianas(componente_rho, componente_phi, componente_z, phi):
    """Convierte (A_rho, A_phi, A_z) evaluado en el ángulo phi [rad] a (A_x, A_y, A_z)."""
    componente_x = componente_rho * np.cos(phi) - componente_phi * np.sin(phi)
    componente_y = componente_rho * np.sin(phi) + componente_phi * np.cos(phi)
    return np.array([componente_x, componente_y, componente_z])


def cartesianas_a_cilindricas(componente_x, componente_y, componente_z, phi):
    """Convierte (A_x, A_y, A_z) a (A_rho, A_phi, A_z) en el ángulo phi [rad]."""
    componente_rho = componente_x * np.cos(phi) + componente_y * np.sin(phi)
    componente_phi = -componente_x * np.sin(phi) + componente_y * np.cos(phi)
    return np.array([componente_rho, componente_phi, componente_z])
