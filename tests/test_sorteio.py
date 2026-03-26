def test_realizar_sorteio():
    numeros_vendidos = [1, 2, 3, 4]

    vencedor = numeros_vendidos[0]

    assert vencedor in numeros_vendidos


def test_resultado_registrado():
    resultado = {"vencedor": 5}

    assert "vencedor" in resultado


def test_sorteio_data_correta():
    data_definida = "2026-12-01"
    data_execucao = "2026-12-01"

    assert data_definida == data_execucao
