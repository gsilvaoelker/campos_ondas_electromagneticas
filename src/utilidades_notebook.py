"""Utilidades comunes a todos los notebooks del curso.

Estilo unificado de las figuras y formato de las tablas de resultados.

La descarga de estos módulos en Google Colab la resuelve la celda de
preparación que abre cada notebook: no puede vivir aquí, porque este archivo
todavía no existe en la máquina de Colab cuando esa celda se ejecuta.
"""
import matplotlib.pyplot as plt
import pandas as pd


def configurar_estilo_graficos():
    """Estilo uniforme para todas las figuras del curso."""
    plt.rcParams.update(
        {
            "figure.figsize": (7.0, 4.3),
            "figure.dpi": 110,
            "axes.grid": True,
            "grid.alpha": 0.25,
            "axes.titlesize": 12,
            "axes.labelsize": 11,
            "legend.frameon": False,
        }
    )


def tabla_resultados(filas):
    """Construye la tabla de resultados numéricos.

    `filas` es una lista de tuplas (magnitud, símbolo, valor, unidad). Los
    valores se muestran con seis cifras significativas y punto decimal.
    """
    tabla = pd.DataFrame(filas, columns=["Magnitud", "Símbolo", "Valor", "Unidad"])
    tabla["Valor"] = tabla["Valor"].map(lambda valor: f"{valor:.6g}")
    return tabla
