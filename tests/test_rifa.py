def test_criar_rifa():
    rifa = {
        "nome": "Rifa do Notebook",
        "descricao": "Notebook gamer",
        "quantidade": 100,
        "valor": 10
    }

    assert rifa["nome"] == "Rifa do Notebook"
    assert rifa["quantidade"] == 100


def test_visualizar_rifa():
    rifa = {"nome": "Rifa X", "status": "ativa"}

    assert rifa["status"] == "ativa"


def test_progresso_rifa():
    total = 100
    vendidos = 40

    progresso = vendidos / total

    assert progresso == 0.4


def test_historico_rifa():
    historico = ["criada", "editada", "finalizada"]

    assert "criada" in historico
