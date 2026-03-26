from unittest.mock import patch

def test_chat_mockado(client):

    with patch("copilot.ask.ask") as mock_ask:
        mock_ask.return_value = "Resposta simulada"

        response = client.post("/chat", json={
            "question": "Teste"
        })

        data = response.get_json()

        assert data["answer"] == "Resposta simulada"

    data = response.get_json()

    assert len(data["answer"]) > 0
