def test_registrar_comprador():
    comprador = {"nome": "João", "email": "joao@email.com"}

    assert comprador["nome"] == "João"


def test_registrar_pagamento():
    numero = {"status": "reservado"}

    pagamento_confirmado = True

    if pagamento_confirmado:
        numero["status"] = "vendido"

    assert numero["status"] == "vendido"


def test_nao_vender_sem_pagamento():
    numero = {"status": "reservado"}

    pagamento_confirmado = False

    if pagamento_confirmado:
        numero["status"] = "vendido"

    assert numero["status"] != "vendido"
