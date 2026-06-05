import os
import csv
import random
from datetime import datetime
from collections import deque

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
client = InferenceClient(token=HF_TOKEN)

CSV_FILE = "maintenance_log.csv"

TEMP_WARNING = 80
TEMP_CRITICAL = 90

VIB_WARNING = 4.0
VIB_CRITICAL = 5.0


ASSETS = {
    "PUMP-MQP-01": {
        "type": "Industrial Pump",
        "temp_history": deque(maxlen=5),
        "vib_history": deque(maxlen=5),
    },
    "MOTOR-MQP-02": {
        "type": "Electric Motor",
        "temp_history": deque(maxlen=5),
        "vib_history": deque(maxlen=5),
    },
    "COMPRESSOR-MQP-03": {
        "type": "Air Compressor",
        "temp_history": deque(maxlen=5),
        "vib_history": deque(maxlen=5),
    },
}


def get_sensor_data():
    temperature = random.uniform(60, 100)
    vibration = random.uniform(1.0, 6.0)
    return round(temperature, 2), round(vibration, 2)


def moving_average(values):
    return sum(values) / len(values)


def evaluate_status(avg_temp, avg_vib):
    if avg_temp >= TEMP_CRITICAL or avg_vib >= VIB_CRITICAL:
        return "CRITICAL"
    elif avg_temp >= TEMP_WARNING or avg_vib >= VIB_WARNING:
        return "WARNING"
    return "NORMAL"


def calculate_health_score(avg_temp, avg_vib):
    temp_score = max(0, 100 - ((avg_temp - 60) * 2))
    vibration_score = max(0, 100 - ((avg_vib - 1) * 15))
    return round((temp_score + vibration_score) / 2, 2)


def maintenance_action(status):
    if status == "CRITICAL":
        return "Immediate shutdown required. Inspect bearings, cooling system, and vibration source."
    elif status == "WARNING":
        return "Schedule inspection and continue close monitoring."
    return "No action required. Asset operating normally."


def generate_ai_recommendation(asset_id, asset_type, avg_temp, avg_vib, status):
    prompt = f"""
You are an industrial maintenance assistant.

Asset ID: {asset_id}
Asset Type: {asset_type}
Average Temperature: {avg_temp:.2f} Celsius
Average Vibration: {avg_vib:.2f}G
System Status: {status}

Give a short professional maintenance recommendation in 2 sentences.
"""

    if not HF_TOKEN:
        return "AI recommendation unavailable because HF_TOKEN is not configured."

    try:
        response = client.chat_completion(
            model="HuggingFaceH4/zephyr-7b-beta",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=80,
        )

        return response.choices[0].message["content"]

    except Exception:
        return "AI recommendation unavailable. Follow standard maintenance procedure."


def create_csv_file():
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "timestamp",
            "asset_id",
            "asset_type",
            "temperature",
            "vibration",
            "avg_temperature",
            "avg_vibration",
            "health_score",
            "status",
            "maintenance_action",
            "ai_recommendation"
        ])


def log_to_csv(
    asset_id,
    asset_type,
    temperature,
    vibration,
    avg_temp,
    avg_vib,
    health_score,
    status,
    action,
    ai_recommendation
):
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            asset_id,
            asset_type,
            temperature,
            vibration,
            round(avg_temp, 2),
            round(avg_vib, 2),
            health_score,
            status,
            action,
            ai_recommendation
        ])


def monitor_asset(asset_id, asset_data):
    temperature, vibration = get_sensor_data()

    asset_data["temp_history"].append(temperature)
    asset_data["vib_history"].append(vibration)

    avg_temp = moving_average(asset_data["temp_history"])
    avg_vib = moving_average(asset_data["vib_history"])

    status = evaluate_status(avg_temp, avg_vib)
    health_score = calculate_health_score(avg_temp, avg_vib)
    action = maintenance_action(status)

    ai_recommendation = generate_ai_recommendation(
        asset_id,
        asset_data["type"],
        avg_temp,
        avg_vib,
        status
    )

    print(f"Asset: {asset_id} ({asset_data['type']})")
    print(f"Temperature: {temperature} C | Vibration: {vibration}G")
    print(f"Average Temperature: {avg_temp:.2f} C | Average Vibration: {avg_vib:.2f}G")
    print(f"Health Score: {health_score}/100")
    print(f"Status:
