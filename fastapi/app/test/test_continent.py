def test_create_and_get_continents(client):
    # Batch create
    response = client.post(
        "/api/continents/batch",
        json={"continents": [{"name": "Asia"}, {"name": "Africa"}]},
    )
    assert response.status_code == 200
    assert len(response.json()) == 2

    # Get all
    response = client.get("/api/continents")
    assert response.status_code == 200
    assert len(response.json()) >= 2
