def test_criar_rifa():
    rifa = {
        "nome": "Rifa do Notebook",
        "quantidade": 100,
        "valor": 10
    }

    assert rifa["nome"] == "Rifa do Notebook"
