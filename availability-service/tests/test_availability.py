from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_list_availabilities():
    response = client.get("/availability/")
    assert response.status_code in [200, 401]  # depende si se prueba con JWT
