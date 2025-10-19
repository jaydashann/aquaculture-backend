from unittest.mock import patch
from app import app

@patch("app.db.reference")
def test_database_sync(mock_db_ref):
    """✅ BTEST-03: New data triggers database write"""
    client = app.test_client()
    mock_ref = mock_db_ref.return_value
    mock_push = mock_ref.push

    payload = {"s1": 7.0, "s2": 29.0, "s3": 40.0, "s4": 250.0}
    res = client.post("/api/sensor-data", json=payload)

    # check API response
    assert res.status_code == 200
    assert res.json["status"] == "success"

    # check if DB push was called
    mock_push.assert_called_once()
