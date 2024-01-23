"""
AAA - A3 - A3

Arange - Act - Assets!
Arrumar - Agir - Garantir!
"""
from pytest import raises
from notas_musicais.escalas import NOTAS, escala

def test_escala_deve_funcionar_com_notas_minusculas():
    #Arrumar
    tonica = 'c'
    tonalidade = 'maior'

    #Act - Chamo o que testar
    result = escala(tonica, tonalidade)

    #Assert
    assert result

def test_escala_deve_retorna_um_erro_dizendo_que_a_nota_nao_exite():
    tonica = 'X'
    tonalidade = 'maior'

    mensagem_de_erro = f'Essa nota não existe, tente uma nota {NOTAS}'

    with raises(ValueError) as error:
        escala(tonica, tonalidade)

    print(error)