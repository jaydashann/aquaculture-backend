import numpy as np

def forecast_next_values(sensor_series):
    """
    Simulate LSTM forecasting based on last 10 readings.
    Returns predicted pH, temperature, turbidity, TDS.
    """
    data = np.array(sensor_series[-10:])
    avg = np.mean(data, axis=0)
    noise = np.random.normal(0, 0.05, size=avg.shape)  # simulate model error
    return (avg + noise).round(2).tolist()
