Predictive Maintenance AI Monitoring System

Executive Summary

The Predictive Maintenance AI Monitoring System is a Python-based industrial monitoring solution designed to simulate condition-based maintenance workflows used in industrial environments.

The system monitors multiple assets, evaluates equipment health using temperature and vibration data, calculates health scores, classifies operational status, and generates maintenance recommendations to support reliability-centered maintenance decisions.

This project demonstrates the application of software engineering, industrial analytics, predictive maintenance principles, and intelligent decision-support systems.

---

Problem Statement

Industrial equipment failures often result in:

- Unplanned downtime
- Production losses
- Increased maintenance costs
- Reduced equipment reliability
- Safety risks

Traditional maintenance approaches rely on reactive maintenance after failure or scheduled maintenance regardless of equipment condition.

This project demonstrates a predictive maintenance approach where equipment health is continuously assessed using operational indicators before failure occurs.

---

Project Objectives

The system was designed to:

- Monitor multiple industrial assets
- Simulate real-world sensor readings
- Detect abnormal operating conditions
- Evaluate asset health
- Support maintenance decision-making
- Demonstrate predictive maintenance concepts
- Provide a foundation for future AI and IoT integration

---

System Architecture

Industrial Asset Layer
│
├── Industrial Pump
├── Electric Motor
└── Air Compressor
│
▼
Sensor Simulation Layer
│
├── Temperature Data
└── Vibration Data
│
▼
Analytics Layer
│
├── Moving Average Analysis
├── Health Score Calculation
└── Condition Assessment
│
▼
Decision Engine
│
├── Status Classification
│   ├── NORMAL
│   ├── WARNING
│   └── CRITICAL
│
└── Maintenance Recommendation Engine
│
▼
Monitoring Output Layer

---

Technical Design

Asset Management Module

The system supports multiple industrial assets through a scalable asset registry.

Current assets:

Asset ID| Asset Type
PUMP-MQP-01| Industrial Pump
MOTOR-MQP-02| Electric Motor
COMPRESSOR-MQP-03| Air Compressor

---

Sensor Simulation Module

The system simulates operational sensor readings:

Temperature

Range:

60°C – 100°C

Vibration

Range:

1.0G – 6.0G

These values represent typical condition-monitoring parameters used in rotating equipment environments.

---

Trend Analysis Module

Historical readings are maintained using Python deques.

Moving averages are calculated to:

- Reduce sensor noise
- Identify developing trends
- Improve condition assessment accuracy

---

Health Score Engine

The Health Score Engine converts operating conditions into a normalized score ranging from:

0 – 100

Health categories:

Score| Condition
80 – 100| Healthy
60 – 79| Moderate Risk
0 – 59| High Risk

The score is derived from:

- Temperature conditions
- Vibration conditions

---

Status Classification Engine

The system classifies asset condition into three operational states.

NORMAL

Equipment is operating within acceptable limits.

WARNING

Abnormal conditions are developing and maintenance planning should begin.

CRITICAL

Immediate intervention is recommended to prevent equipment failure.

---

Maintenance Decision Engine

The Maintenance Decision Engine translates equipment condition into actionable maintenance guidance.

Example outputs:

NORMAL

No action required.
Continue routine monitoring.

WARNING

Schedule maintenance inspection.
Monitor asset closely.

CRITICAL

Immediate shutdown required.
Inspect bearings and cooling systems.

---

Intelligent Recommendation Engine

The project supports AI-assisted maintenance recommendations through Hugging Face integration.

When external model services are unavailable, the system automatically falls back to internal recommendation logic, ensuring operational continuity.

This design improves system resilience and fault tolerance.

---

Technologies Used

Programming Language

- Python

Core Libraries

- random
- collections
- os
- huggingface_hub

Development Environment

- Google Colab
- Git
- GitHub

---

Engineering Concepts Demonstrated

Reliability Engineering

- Equipment reliability assessment
- Failure prevention
- Risk reduction

Predictive Maintenance

- Condition-based monitoring
- Trend analysis
- Early fault detection

Software Engineering

- Modular design
- Functional decomposition
- Error handling
- Scalable architecture

Data Analytics

- Moving averages
- Health scoring
- Operational analytics

---

Sample Output

Asset: PUMP-MQP-01

Temperature: 87.45 C
Vibration: 4.92 G

Health Score: 61.80/100

Status: WARNING

Rule-Based Action:
Schedule maintenance inspection and monitor closely.

AI Recommendation:
PUMP-MQP-01 is showing early warning signs.
Schedule preventive maintenance and monitor operational trends.

---

Project Outcomes

The completed system successfully demonstrates:

- Multi-asset monitoring
- Industrial condition assessment
- Health score generation
- Status classification
- Automated maintenance recommendations
- Intelligent decision-support concepts

---

Author

Lethabo Mafihle James Moshabane

GitHub: https://github.com/lordlethabo

LinkedIn: https://linkedin.com/in/lethabo-mafihle-james-moshabane-777545325
