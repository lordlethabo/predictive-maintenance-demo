# Predictive Maintenance AI Monitoring System

## Overview

This project simulates an industrial predictive maintenance system for pumps, motors, and compressors.

It uses Python to generate simulated sensor readings, calculate moving averages, classify asset health, log maintenance data to CSV, and generate AI-powered maintenance recommendations using Hugging Face.

## Features

- Simulated industrial sensor data
- Multiple asset monitoring
- Temperature and vibration analysis
- Moving average trend analysis
- Health score calculation
- Status classification: NORMAL, WARNING, CRITICAL
- Rule-based maintenance actions
- Hugging Face AI maintenance recommendations
- CSV maintenance logging

## Technologies Used

- Python
- Hugging Face Inference API
- python-dotenv
- CSV logging
- Git and GitHub

## Assets Monitored

- Industrial Pump
- Electric Motor
- Air Compressor

## System Logic

1. Generate simulated sensor readings.
2. Store recent temperature and vibration values.
3. Calculate moving averages.
4. Classify asset status.
5. Calculate health score.
6. Generate rule-based maintenance action.
7. Generate AI maintenance recommendation.
8. Save results to CSV.

## Health Status Logic

| Status | Condition |
|---|---|
| NORMAL | Asset operating within safe range |
| WARNING | Elevated temperature or vibration detected |
| CRITICAL | Serious risk detected requiring urgent action |

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
