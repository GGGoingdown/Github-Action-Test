import pytest
import os
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "secret-for-test"}


def test_environment():
    assert os.getenv("ENVIRONMENT") == "test"