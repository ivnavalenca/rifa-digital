def test_listar_numeros_disponiveis():
    numeros = ["disponivel", "reservado", "disponivel"]

    disponiveis = [n for n in numeros if n == "disponivel"]

    assert len(disponiveis) == 2


def test_escolher_numero():
    numero = {"id": 1, "status": "disponivel"}

    numero["status"] = "reservado"

    assert numero["status"] == "reservado"


def test_numero_nao_pode_ser_duplo():
    numero_vendido = True

    tentativa_nova_venda = True

    assert not (numero_vendido and tentativa_nova_venda)


def test_cancelar_reserva():
    numero = {"status": "reservado"}

    numero["status"] = "disponivel"

    assert numero["status"] == "disponivel"
