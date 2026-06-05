import os
import random
from collections import deque
from huggingface_hub import InferenceClient

HF_TOKEN = os.environ.get("HF_TOKEN")

client = InferenceClient(token=HF_TOKEN) if HF_TOKEN else None

AI_MODEL = "mistralai/Mistral-7B-Instruct-v0.3"

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
        return "Immediate shutdown required. Inspect bearings, vibration source, and cooling systems."
    elif status == "WARNING":
        return "Schedule maintenance inspection and monitor the asset closely."
    return "No action required. Continue routine monitoring."


def fallback_ai_recommendation(asset_id, asset_type, avg_temp, avg_vib, status):
    if status == "CRITICAL":
        return (
            f"{asset_id} requires urgent maintenance. "
            f"The {asset_type.lower()} should be stopped and inspected for overheating, excessive vibration, bearing wear, and cooling system faults."
        )

    if status == "WARNING":
        return (
            f"{asset_id} is showing early warning signs. "
            f"Schedule a preventive inspection, monitor temperature and vibration trends, and prepare maintenance resources."
        )

    return (
        f"{asset_id} is operating within normal limits. "
        f"Continue routine monitoring and keep maintenance records updated."
    )


def generate_ai_recommendation(asset_id, asset_type, avg_temp, avg_vib, status):
    if client is None:
        return fallback_ai_recommendation(asset_id, asset_type, avg_temp, avg_vib, status)

    prompt = f"""
You are an industrial maintenance assistant.

Asset ID: {asset_id}
Asset Type: {asset_type}
Average Temperature: {avg_temp:.2f} Celsius
Average Vibration: {avg_vib:.2f}G
Status: {status}

Give a short professional maintenance recommendation in 2 sentences.
"""

    try:
        response = client.chat_completion(
            model=AI_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=80
        )

        return response.choices[0].message.content

    except Exception:
        return fallback_ai_recommendation(asset_id, asset_type, avg_temp, avg_vib, status)


def monitor_asset(asset_id, asset_data):
    temperature, vibration = get_sensor_data()

    asset_data["temp_history"].append(temperature)
    asset_data["vib_history"].append(vibration)

    avg_temp = moving_average(asset_data["temp_history"])
    avg_vib = moving_average(asset_data["vib_history"])

    status = evaluate_status(avg_temp, avg_vib)
    health_score = calculate_health_score(avg_temp, avg_vib)
    rule_based_action = maintenance_action(status)

    ai_recommendation = generate_ai_recommendation(
        asset_id,
        asset_data["type"],
        avg_temp,
        avg_vib,
        status
    )

    print("=" * 70)
    print(f"Asset: {asset_id}")
    print(f"Type: {asset_data['type']}")
    print(f"Temperature: {temperature} C")
    print(f"Vibration: {vibration}G")
    print(f"Average Temperature: {avg_temp:.2f} C")
    print(f"Average Vibration: {avg_vib:.2f}G")
    print(f"Health Score: {health_score}/100")
    print(f"Status: {status}")
    print(f"Rule-Based Action: {rule_based_action}")
    print(f"AI Recommendation: {ai_recommendation}")
    print("=" * 70)


def run_monitoring(cycles=3):
    for cycle in range(cycles):
        print(f"\n--- Monitoring Cycle {cycle + 1}/{cycles} ---")
        for asset_id, asset_data in ASSETS.items():
            monitor_asset(asset_id, asset_data)

run_monitoring()
