import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_valid_sensor_data(client):
    """✅ BTEST-01: Valid sensor data is accepted and stored"""
    payload = {
        "s1": 7.5,   # pH
        "s2": 28.5,  # temperature
        "s3": 35.0,  # turbidity
        "s4": 300.0  # TDS
    }
    res = client.post("/api/sensor-data", json=payload)
    assert res.status_code == 200
    assert res.json["status"] == "success"

def test_invalid_sensor_data(client):
    """❌ BTEST-01: Invalid data (missing or out of range) is rejected"""
    payload = {"s1": None, "s2": "NaN", "s3": -5, "s4": 99999}
    res = client.post("/api/sensor-data", json=payload)
    assert res.status_code == 400  # Expect rejection
