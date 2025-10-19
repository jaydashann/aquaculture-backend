import numpy as np
from lstm_model import forecast_next_values

def test_forecast_output_format():
    """✅ BTEST-02: Model returns correct JSON structure"""
    history = np.random.rand(10, 4) * [14, 35, 100, 500]
    result = forecast_next_values(history)
    assert isinstance(result, list)
    assert len(result) == 4

def test_forecast_accuracy_simulation():
    """✅ BTEST-02: Forecast values within acceptable bounds (±10%)"""
    history = np.array([[7.0, 28.0, 30.0, 300.0]] * 10)
    result = forecast_next_values(history)
    for pred, true in zip(result, [7.0, 28.0, 30.0, 300.0]):
        assert abs(pred - true) / true < 0.1  # within ±10%
