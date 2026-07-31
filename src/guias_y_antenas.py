"""Guías de onda rectangulares y antenas elementales.

Se usa en las semanas 15 y 16 de la Unidad 3.
"""
import numpy as np

from constantes_fisicas import VELOCIDAD_LUZ, IMPEDANCIA_VACIO


# --------------------------------------------------------------------------
# Guía de onda rectangular
# --------------------------------------------------------------------------
def frecuencia_de_corte(ancho, alto, m, n, velocidad=VELOCIDAD_LUZ):
    """Frecuencia de corte del modo TE_mn o TM_mn [Hz].

        f_c = (u / 2) sqrt( (m/a)^2 + (n/b)^2 )

    Por debajo de esta frecuencia el modo no se propaga: se apaga
    exponencialmente en vez de viajar.
    """
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
    """Resistencia de radiación de un dipolo corto [ohm]: R_r = 80 pi^2 (dl/lambda)^2.

    Es la resistencia equivalente que representa la potencia que la antena
    entrega al espacio, no la que disipa en calor.
    """
    return 80.0 * np.pi**2 * longitud_sobre_lambda**2


def eficiencia_antena(resistencia_radiacion, resistencia_perdidas):
    """Eficiencia xi = R_r / (R_r + R_perdidas), adimensional entre 0 y 1."""
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
    return (impedancia * numero_de_onda * corriente * longitud
            * np.sin(angulo) / (4.0 * np.pi * distancia))


def potencia_radiada_dipolo(corriente_pico, resistencia_radiacion):
    """Potencia total radiada [W]: P = I_0^2 R_r / 2."""
    return 0.5 * corriente_pico**2 * resistencia_radiacion
