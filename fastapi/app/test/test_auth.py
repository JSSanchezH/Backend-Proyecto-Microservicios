def test_authenticate_user(client):
    # Primero crea un UserCompany con una API key válida
    client.post("/api/UserCompany", json={"username": "test", "api_key": "abc123"})

    # Ahora intenta acceder a una ruta protegida
    response = client.get("/api/companies", headers={"X-API-KEY": "abc123"})
    assert response.status_code == 200
