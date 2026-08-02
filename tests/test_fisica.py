import sys
from pathlib import Path

import numpy as np
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import campos_electrostaticos as electro
import guias_y_antenas as guias
import interfaces_planas as interfaces
import lineas_transmision as lineas
import medios_y_condiciones_de_borde as bordes


def test_esfera_en_el_origen_no_divide_por_cero():
    with np.errstate(all="raise"):
        flujo = electro.densidad_flujo_esfera_uniforme(0.0, 0.1, 2.0e-6)
    assert flujo == pytest.approx(0.0)


def test_esfera_es_continua_en_la_superficie():
    radio = 0.1
    densidad = 2.0e-6
    interior = densidad * radio / 3.0
    superficie = electro.densidad_flujo_esfera_uniforme(radio, radio, densidad)
    assert superficie == pytest.approx(interior)


def test_borde_dielelectrico_conserva_d_normal():
    e1 = 4.0e3
    e2 = bordes.campo_normal_transmitido(e1, 2.0, 5.0)
    assert bordes.densidad_flujo_normal(e1, 2.0) == pytest.approx(
        bordes.densidad_flujo_normal(e2, 5.0)
    )


def test_fresnel_conserva_potencia_en_incidencia_normal():
    for n1, n2 in ((1.0, 1.5), (1.5, 1.0), (1.0, 1.0)):
        total = interfaces.reflectancia_normal(n1, n2) + interfaces.transmitancia_normal(n1, n2)
        assert total == pytest.approx(1.0)


def test_reflexion_interna_no_inventa_un_angulo_real():
    incidencia = np.deg2rad(50.0)
    transmitido = interfaces.angulo_transmitido(1.5, 1.0, incidencia)
    assert np.iscomplex(transmitido)
    rs, rp, _ = interfaces.coeficientes_fresnel(1.5, 1.0, incidencia)
    assert abs(rs) == pytest.approx(1.0)
    assert abs(rp) == pytest.approx(1.0)


def test_angulo_critico_solo_existe_del_medio_denso_al_menos_denso():
    assert np.isnan(interfaces.angulo_critico(1.0, 1.5))
    assert interfaces.angulo_critico(1.5, 1.0) == pytest.approx(np.arcsin(2.0 / 3.0))


def test_indices_de_refraccion_deben_ser_positivos():
    with pytest.raises(ValueError, match="positivos"):
        interfaces.coeficiente_reflexion_normal(1.0, 0.0)


def test_roe_rechaza_caso_activo_y_conserva_limites_pasivos():
    assert lineas.razon_onda_estacionaria(0.0) == pytest.approx(1.0)
    assert np.isinf(lineas.razon_onda_estacionaria(1.0))
    with pytest.raises(ValueError, match="pasiva"):
        lineas.razon_onda_estacionaria(1.1)


def test_transformador_simple_exige_resistencias_reales_positivas():
    assert lineas.impedancia_cuarto_de_onda(50.0, 100.0) == pytest.approx(np.sqrt(5000.0))
    with pytest.raises(ValueError, match="reales"):
        lineas.impedancia_cuarto_de_onda(50.0, 100.0 + 1.0j)
    with pytest.raises(ValueError, match="positivas"):
        lineas.impedancia_cuarto_de_onda(50.0, -100.0)


def test_guia_rechaza_modos_no_fisicos():
    with pytest.raises(ValueError, match="no ambos cero"):
        guias.frecuencia_de_corte(0.02, 0.01, 0, 0)
    with pytest.raises(ValueError, match="TM"):
        guias.frecuencia_de_corte(0.02, 0.01, 1, 0, tipo_modo="TM")


def test_velocidades_de_guia_cumplen_el_producto():
    fc = guias.frecuencia_de_corte(22.86e-3, 10.16e-3, 1, 0)
    frecuencia = 10.0e9
    fase = guias.velocidad_fase_guia(frecuencia, fc)
    grupo = guias.velocidad_grupo_guia(frecuencia, fc)
    assert fase * grupo == pytest.approx(guias.VELOCIDAD_LUZ**2)


def test_campo_hertziano_reporta_amplitud_no_negativa_y_escala_con_distancia():
    e1 = guias.campo_dipolo_hertziano(0.1, 0.01, 10.0, 1.5 * np.pi, 20.0)
    e2 = guias.campo_dipolo_hertziano(0.1, 0.01, 20.0, 1.5 * np.pi, 20.0)
    assert e1 > 0.0
    assert e2 == pytest.approx(e1 / 2.0)
