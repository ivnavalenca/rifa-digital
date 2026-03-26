def test_healthcheck(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "Rifa Digital" in response.get_data(as_text=True)
