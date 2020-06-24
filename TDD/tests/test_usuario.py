from TDD.src.leilao.dominio import Usuario, Leilao
import pytest


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_esse_propor_um_lance():
    vini = Usuario('Vini', 100.0)
    leilao = Leilao('Celular')
    vini.propoe_lance(leilao, 50.0)
    assert vini.carteira == 50.0

def test_deve_permitir_propor_lance_quando_valor_eh_menor_que_o_valor_da_carteira():
    vini = Usuario('Vini', 100.0)
    leilao = Leilao('Celular')
    vini.propoe_lance(leilao, 1.0)
    assert vini.carteira == 99.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira():
    vini = Usuario('Vini', 100.0)
    leilao = Leilao('Celular')
    vini.propoe_lance(leilao, 100.0)
    assert vini.carteira == 0.0

def test_nao_deve_permitir_propor_lance_com_valor_maior_ao_da_carteira():
    with pytest.raises(ValueError):
        vini = Usuario('Vini', 100.0)
        leilao = Leilao('Celular')
        vini.propoe_lance(leilao, 200.0)