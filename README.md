#  Predictive Maintenance System (Pump Monitoring Simulation)

## Overview

This project simulates an industrial predictive maintenance system for a mining pump asset (**PUMP-MQP-01**).  
It demonstrates how sensor data (temperature and vibration) can be used to monitor machine health and detect early warning signs of equipment failure.

The system applies basic engineering principles such as trend analysis and threshold-based anomaly detection to classify machine health status.

---

## Features

- Simulated real-time sensor data (temperature & vibration)
- Moving average trend analysis
- Health classification system:
  - NORMAL
  - WARNING
  - CRITICAL
- Automated maintenance recommendations
- Controlled runtime simulation (20 cycles)

---

##  Engineering Concept

The system models a simplified version of industrial predictive maintenance used in:

- Mining equipment monitoring
- Manufacturing machinery health tracking
- Industrial IoT systems

Instead of reacting to breakdowns, the system identifies **early warning signs** using sensor trends.

---

## System Logic

1. Generate sensor data (temperature & vibration)
2. Store recent readings (trend window)
3. Calculate moving averages
4. Evaluate machine health status
5. Trigger maintenance action based on severity

---

## Health Classification

| Status    | Condition |
|-----------|----------|
| NORMAL    | Stable operation |
| WARNING   | Elevated risk detected |
| CRITICAL  | Immediate maintenance required |

---

## Maintenance Actions

- **NORMAL:** No action required  
- **WARNING:** Schedule inspection and monitor system  
- **CRITICAL:** Immediate shutdown and inspect bearings & cooling system  

---

## How to Run

### 1. Clone repository
```bash
git clone https://github.com/lordlethabo/predictive-maintenance-demo.git
