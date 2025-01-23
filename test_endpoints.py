from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_wallet_info_endpoint():
    response = client.post("/wallet-info", json={"address": "valid_tron_address"})
    assert (
        response.status_code == 200
        or response.status_code == 404
        or response.status_code == 400
    )


def test_get_wallet_logs_endpoint():
    response = client.get("/wallet-logs")
    assert response.status_code == 200
