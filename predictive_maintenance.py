import random
import time
from collections import deque

ASSET_ID = "PUMP-MQP-01"

# Thresholds
TEMP_WARNING = 80
TEMP_CRITICAL = 90

VIB_WARNING = 4.0
VIB_CRITICAL = 5.0

# Store last readings for trend analysis
temp_history = deque(maxlen=5)
vib_history = deque(maxlen=5)


def get_sensor_data():
    """
    Simulate pump sensor readings (temperature + vibration)
    """
    temp = random.uniform(60, 100)
    vib = random.uniform(1.0, 6.0)

    return round(temp, 2), round(vib, 2)


def moving_average(values):
    return sum(values) / len(values)


def evaluate_status(avg_temp, avg_vib):
    """
    Determine machine health status
    """
    if avg_temp >= TEMP_CRITICAL or avg_vib >= VIB_CRITICAL:
        return "CRITICAL"
    elif avg_temp >= TEMP_WARNING or avg_vib >= VIB_WARNING:
        return "WARNING"
    else:
        return "NORMAL"


def maintenance_action(status):
    """
    Recommended engineering action based on system status
    """
    if status == "CRITICAL":
        return "IMMEDIATE SHUTDOWN + Inspect bearings and cooling system"
    elif status == "WARNING":
        return "Schedule maintenance inspection and monitor closely"
    else:
        return "No action required"


def run_monitoring():
    print("\n🔧 Predictive Maintenance System Started\n")

    for _ in range(20):  # controlled run (not infinite)

        temp, vib = get_sensor_data()

        temp_history.append(temp)
        vib_history.append(vib)

        avg_temp = moving_average(temp_history)
        avg_vib = moving_average(vib_history)

        status = evaluate_status(avg_temp, avg_vib)
        action = maintenance_action(status)

        print(f"[{status}] {ASSET_ID}")
        print(f"Temp: {temp}°C | Vib: {vib}G")
        print(f"Avg Temp: {avg_temp:.2f}°C | Avg Vib: {avg_vib:.2f}G")
        print(f"Action: {action}\n")

        time.sleep(1)


if __name__ == "__main__":
    run_monitoring()
