import random
import time
from collections import deque

ASSET_ID = "PUMP-MQP-01"

TEMP_LIMIT = 85
VIB_LIMIT = 4.5

# store last few readings (moving average)
temp_history = deque(maxlen=5)
vib_history = deque(maxlen=5)


def get_sensor_data():
    """
    Simulates realistic industrial sensor data with noise
    """

    temperature = random.uniform(60, 100)
    vibration = random.uniform(1.0, 6.0)

    return {
        "asset_id": ASSET_ID,
        "temperature": round(temperature, 2),
        "vibration": round(vibration, 2)
    }


def calculate_average(history):
    return sum(history) / len(history)


def detect_anomaly(data):
    temp_history.append(data["temperature"])
    vib_history.append(data["vibration"])

    avg_temp = calculate_average(temp_history)
    avg_vib = calculate_average(vib_history)

    print(f"Avg Temp: {avg_temp:.2f}°C | Avg Vib: {avg_vib:.2f}G")

    if avg_temp > TEMP_LIMIT or avg_vib > VIB_LIMIT:
        return True

    return False


def alert_system(data):
    print("\n PREDICTIVE MAINTENANCE ALERT ")
    print(f"Asset: {data['asset_id']}")
    print(f"Temperature: {data['temperature']}°C")
    print(f"Vibration: {data['vibration']}G")
    print("Action: Inspect bearings + cooling system immediately\n")


def run():
    print("Starting Pump Monitoring System...\n")

    while True:
        data = get_sensor_data()

        print(f"Pump {data['asset_id']} | Temp: {data['temperature']}°C | Vib: {data['vibration']}G")

        if detect_anomaly(data):
            alert_system(data)

        time.sleep(2)


if __name__ == "__main__":
    run()
