import sys
sys.path.append('../src/calc')

from calculadora import Calculadora

import pytest


@pytest.fixture
def calc():
    icon_path = "imagem/calculadora_icone.png"
    return Calculadora("Calc", 200, 300, 2, 5, icon_path)


def test_deve_conseguir_inserir_numeros_atraves_dos_botoes(calc):
    calc.button_num('5')
    assert calc._numeros == '5'


def test_nao_deve_conseguir_inserir_botoes_especiais_sem_numero_antes(calc):
    calc.button_special('+')
    tem_caracter = len(calc._numeros)
    assert tem_caracter == 0


def test_nao_deve_conseguir_inserir_zero_sem_numero_antes(calc):
    calc.button_num('0')
    tem_caracter = len(calc._numeros)
    assert tem_caracter == 0


def test_conseguir_somar_dois_numeros(calc):
    calc.button_num('12')
    calc.button_special('+')
    calc.button_num('50')
    calc.button_confirm()
    assert calc._numeros == '62'


def test_conseguir_subtrair_dois_numeros(calc):
    calc.button_num('50')
    calc.button_special('-')
    calc.button_num('5')
    calc.button_confirm()
    assert calc._numeros == '45'


def test_conseguir_multiplicar_dois_numeros(calc):
    calc.button_num('12')
    calc.button_special('*')
    calc.button_num('50')
    calc.button_confirm()
    assert calc._numeros == '600'


def test_conseguir_dividir_dois_numeros(calc):
    calc.button_num('50')
    calc.button_special('/')
    calc.button_num('5')
    calc.button_confirm()
    assert calc._numeros == '10.0'


def test_inverter_valor_sinal(calc):
    calc.button_num('50')
    calc.button_negate()
    assert calc._numeros == '-50.0'


def test_raiz_quadrada(calc):
    calc.button_num('4')
    calc.button_square_root()
    assert calc._numeros == '2.0'


def test_elevar_ao_quadrado(calc):
    calc.button_num('4')
    calc.button_square()
    assert calc._numeros == '16.0'
