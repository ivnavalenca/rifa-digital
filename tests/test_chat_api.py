def test_chat_responde(client):
    response = client.post("/chat", json={
        "question": "O que é uma rifa?"
    })

    assert response.status_code == 200

    data = response.get_json()

    assert "answer" in data
    assert isinstance(data["answer"], str)


def test_chat_sem_pergunta(client):
    response = client.post("/chat", json={})

    assert response.status_code == 200

    data = response.get_json()

    assert "answer" in data


def test_chat_pergunta_valida(client):
    response = client.post("/chat", json={
        "question": "Quais testes foram implementados?"
    })

    data = response.get_json()

    assert len(data["answer"]) > 0
