import pytest
from app import create_app

@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_employee_pagination(client):
    response = client.get("/api/employees?page=1&limit=10")
    assert response.status_code == 200
    body = response.json

    assert len(body["data"]) == 10
    assert body["pagination"]["page"] == 1
    assert body["pagination"]["total"] == 30
    assert body["pagination"]["total_pages"] == 3

def test_get_employee(client):
    response = client.get("/api/employees/1")
    assert response.status_code == 200
    assert response.json["data"]["id"] == 1

def test_missing_employee(client):
    response = client.get("/api/employees/999")
    assert response.status_code == 404
