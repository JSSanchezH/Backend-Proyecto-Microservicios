def test_create_company(client):
    response = client.post(
        "/api/companies",
        json={
            "name": "TestCompany",
            "address": "123 Test St",
            "email": "contact@test.com",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "TestCompany"
