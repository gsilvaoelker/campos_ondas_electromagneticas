"""Guías de onda rectangulares y antenas elementales.

Se usa en las semanas 15 y 16 de la Unidad 3.
"""
import numpy as np

from constantes_fisicas import VELOCIDAD_LUZ, IMPEDANCIA_VACIO


# --------------------------------------------------------------------------
# Guía de onda rectangular
# --------------------------------------------------------------------------
def frecuencia_de_corte(ancho, alto, m, n, velocidad=VELOCIDAD_LUZ, tipo_modo="TE"):
    """Frecuencia de corte del modo TE_mn o TM_mn [Hz].

        f_c = (u / 2) sqrt( (m/a)^2 + (n/b)^2 )

    Por debajo de esta frecuencia el modo no se propaga: se apaga
    exponencialmente en vez de viajar. TE_00 no existe; en modos TM ambos
    índices deben ser positivos.
    """
    tipo_modo = tipo_modo.upper()
    if ancho <= 0.0 or alto <= 0.0 or velocidad <= 0.0:
        raise ValueError("Las dimensiones y la velocidad deben ser positivas.")
    if not isinstance(m, (int, np.integer)) or not isinstance(n, (int, np.integer)):
        raise ValueError("Los índices modales m y n deben ser enteros.")
    if m < 0 or n < 0 or (m == 0 and n == 0):
        raise ValueError("Los índices modales deben ser no negativos y no ambos cero.")
    if tipo_modo not in {"TE", "TM"}:
        raise ValueError("tipo_modo debe ser 'TE' o 'TM'.")
    if tipo_modo == "TM" and (m == 0 or n == 0):
        raise ValueError("En un modo TM rectangular, m y n deben ser positivos.")
    termino_m = 0.0 if m == 0 else (m / ancho) ** 2
    termino_n = 0.0 if n == 0 else (n / alto) ** 2
    return velocidad / 2.0 * np.sqrt(termino_m + termino_n)


def se_propaga(frecuencia, frecuencia_corte):
    """¿Se propaga el modo a esta frecuencia? Solo si f > f_c."""
    return np.asarray(frecuencia) > np.asarray(frecuencia_corte)


def factor_de_propagacion(frecuencia, frecuencia_corte):
    """sqrt(1 - (fc/f)^2), el factor que aparece en toda la teoría de guías.

    Vale 1 muy por encima del corte y tiende a 0 al acercarse a él. Por debajo
    del corte no está definido —el modo es evanescente, no viaja— y se devuelve
    `nan` sin emitir advertencias.
    """
    razon = np.asarray(frecuencia_corte, dtype=float) / np.asarray(frecuencia, dtype=float)
    with np.errstate(invalid="ignore"):
        return np.sqrt(np.where(razon < 1.0, 1.0 - razon**2, np.nan))


def longitud_onda_guia(frecuencia, frecuencia_corte, velocidad=VELOCIDAD_LUZ):
    """Longitud de onda dentro de la guía [m]: lambda_g = lambda_0 / sqrt(1 - (fc/f)^2).

    Siempre es mayor que en el espacio libre. Por debajo del corte devuelve `nan`.
    """
    return (velocidad / frecuencia) / factor_de_propagacion(frecuencia, frecuencia_corte)


def velocidad_fase_guia(frecuencia, frecuencia_corte, velocidad=VELOCIDAD_LUZ):
    """Velocidad de fase en la guía [m/s]. Es mayor que c, pero no transporta información."""
    return velocidad / factor_de_propagacion(frecuencia, frecuencia_corte)


def velocidad_grupo_guia(frecuencia, frecuencia_corte, velocidad=VELOCIDAD_LUZ):
    """Velocidad de grupo en la guía [m/s]: la que sí lleva la energía. Siempre menor que c."""
    return velocidad * factor_de_propagacion(frecuencia, frecuencia_corte)


# --------------------------------------------------------------------------
# Dipolo hertziano (antena corta)
# --------------------------------------------------------------------------
def resistencia_radiacion_dipolo_corto(longitud_sobre_lambda):
    """Resistencia del elemento hertziano ideal [ohm]: R_r = 80 pi^2 (dl/lambda)^2.

    Es la resistencia equivalente que representa la potencia que la antena
    entrega al espacio, no la que disipa en calor.
    """
    if longitud_sobre_lambda < 0.0:
        raise ValueError("La longitud normalizada no puede ser negativa.")
    return 80.0 * np.pi**2 * longitud_sobre_lambda**2


def eficiencia_antena(resistencia_radiacion, resistencia_perdidas):
    """Eficiencia xi = R_r / (R_r + R_perdidas), adimensional entre 0 y 1."""
    if resistencia_radiacion < 0.0 or resistencia_perdidas < 0.0:
        raise ValueError("Las resistencias no pueden ser negativas.")
    if resistencia_radiacion + resistencia_perdidas == 0.0:
        raise ValueError("Al menos una resistencia debe ser positiva.")
    return resistencia_radiacion / (resistencia_radiacion + resistencia_perdidas)


def ganancia_antena(eficiencia, directividad):
    """Ganancia G = xi D, adimensional. La directividad sola ignora las pérdidas."""
    return eficiencia * directividad


def a_decibelios(ganancia):
    """Convierte una ganancia lineal a dBi: G_dB = 10 log10(G)."""
    return 10.0 * np.log10(ganancia)


def campo_dipolo_hertziano(corriente, longitud, distancia, angulo, numero_de_onda,
                           impedancia=IMPEDANCIA_VACIO):
    """Amplitud de E_theta en la zona lejana [V/m].

        |E_theta| = eta beta I_0 dl sin(theta) / (4 pi r)

    Decae como 1/r, no como 1/r^2: por eso la radiación llega lejos.
    """
    if distancia <= 0.0:
        raise ValueError("La distancia debe ser positiva.")
    return (impedancia * numero_de_onda * abs(corriente) * abs(longitud)
            * np.abs(np.sin(angulo)) / (4.0 * np.pi * distancia))


def potencia_radiada_dipolo(corriente_pico, resistencia_radiacion):
    """Potencia total radiada [W]: P = I_0^2 R_r / 2."""
    return 0.5 * corriente_pico**2 * resistencia_radiacion
