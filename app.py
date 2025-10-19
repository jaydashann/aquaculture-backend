from flask import Flask, request, jsonify
from firebase_admin import credentials, initialize_app, db
import time

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred, {
    "databaseURL": "https://aquaculture-1f760-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

@app.route('/api/sensor-data', methods=['POST'])
def receive_sensor_data():
    data = request.get_json()
    try:
        s1, s2, s3, s4 = float(data["s1"]), float(data["s2"]), float(data["s3"]), float(data["s4"])
        if not (0 <= s1 <= 14 and 0 <= s2 <= 50 and 0 <= s3 <= 500 and 0 <= s4 <= 1000):
            raise ValueError("Out of range")
    except (KeyError, ValueError, TypeError):
        return jsonify({"status": "error", "message": "Invalid sensor data"}), 400

    ref = db.reference("sensor_data")
    ref.push({
        "ts": int(time.time() * 1000),
        "s1": s1,
        "s2": s2,
        "s3": s3,
        "s4": s4,
    })
    return jsonify({"status": "success", "message": "Data stored"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
