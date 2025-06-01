def test_create_country(client):
    # Crear continente primero
    continent = client.post("/api/continents", json={"name": "Europe"}).json()

    # Crear país
    response = client.post(
        "/api/countries",
        json={"name": "Germany", "continent_id": continent["continent_id"]},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Germany"
