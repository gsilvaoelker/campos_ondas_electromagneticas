"""Constantes físicas del curso Campos y Ondas Electromagnéticas.

Valores CODATA. Se definen una sola vez para todo el curso, de modo que los
resultados numéricos de todos los notebooks sean reproducibles entre sí.
"""
import numpy as np

# Permitividad del vacío [F/m].
EPSILON_0 = 8.8541878128e-12

# Permeabilidad del vacío [H/m].
MU_0 = 4.0e-7 * np.pi

# Velocidad de la luz en el vacío [m/s].
VELOCIDAD_LUZ = 1.0 / np.sqrt(MU_0 * EPSILON_0)

# Impedancia intrínseca del vacío [ohm].
IMPEDANCIA_VACIO = np.sqrt(MU_0 / EPSILON_0)

# Carga elemental [C]. El electrón tiene carga -CARGA_ELEMENTAL.
CARGA_ELEMENTAL = 1.602176634e-19
