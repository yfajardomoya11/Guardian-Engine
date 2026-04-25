# 🛡️ Guardian-Engine: Sentinel Shield
![Mode](https://img.shields.io/badge/Mode-Sentinel_Shield-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Power-Python_3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Status-Active_Defense-red?style=for-the-badge)
![Architecture](https://img.shields.io/badge/Architecture-Event--Driven-purple?style=for-the-badge)
![SIEM](https://img.shields.io/badge/SIEM-Core_System-darkred?style=for-the-badge)

> **"A true defense system doesn't avoid impact — it absorbs, analyzes, and neutralizes threats in real time."**

---

## 🛡️ Project Overview

**Guardian-Engine: Sentinel Shield** is a high-performance **Security Information and Event Management (SIEM)** engine developed in **Python**, designed with an **Event-Driven architecture**.

It acts as a **centralized cyber defense core**, capable of:

- Monitoring logs in real time  
- Detecting anomalous behavior  
- Classifying security events  
- Persisting forensic data for analysis  

Unlike traditional systems, Sentinel Shield is built to **operate under pressure**, transforming high volumes of security events into structured intelligence.

---

![Tests Status](https://github.com/yfajardomoya11/guardian-engine/actions/workflows/python-tests.yml/badge.svg)

---

## 🖼️ Visual Concept

![Guardian Engine](https://github.com/yfajardomoya11/Guardian-Engine/blob/main/assets/guardianengine.png)

Sentinel Shield represents a **defensive cyber layer**, acting as a digital barrier between infrastructure and malicious activity.

---

## 👨‍💻 Author

**Yananth Fajardo Moya**  
Network Infrastructure Technician & Cybersecurity Tool Developer  
Costa Rica 🇨🇷  

---

## ⚠️ Professional Disclaimer

> This project was developed for **educational and demonstration purposes only**.

Guardian-Engine is a **Proof of Concept (PoC)** designed to showcase skills in:

- Python development  
- Event-driven architectures  
- Security monitoring systems  
- Data persistence and analysis  

⚠️ It should not be used as a standalone defense solution in production environments without proper auditing, validation, and security hardening.

The author is not responsible for misuse of this tool.

---

## 📖 Description

**Guardian-Engine** is a security event processing engine that monitors system logs in real time, detects anomalies, and stores structured alerts for further analysis.

This project represents a **core component in a personal cybersecurity ecosystem**, demonstrating practical SIEM capabilities aligned with real-world SOC environments.

---

## 📸 Proof of Concept

<p align="center">
  <img src="assets/PRUEBASIEM1.png" width="100%">
</p>
  <br>
  <i>Real-time detection and classification of security events.</i>
</p>

---

## 🚀 Key Features

### 🔍 Real-Time Monitoring
- Uses `watchdog` to detect file changes instantly via OS signals

### 🧠 Event Analysis Engine
- Processes log streams line-by-line  
- Classifies events into:
  - `INFO`
  - `WARNING`
  - `CRITICAL`

### 🗄️ Forensic Persistence
- SQLite integration for structured storage  
- Enables historical analysis and auditing  

### 🔐 Secure Configuration
- Environment variables (`.env`) for sensitive data protection  

---

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **Database:** SQLite3  
- **Libraries:**  
  - `watchdog`  
  - `python-dotenv`  
  - `pandas`  

- **Architecture:** Event-Driven System  

---

## 📂 Project Structure

```text
GUARDIAN-ENGINE/
├── main.py              # Core engine orchestrator
├── .env                 # Environment configuration (excluded)
├── database/
│   ├── db_manager.py    # Database logic
│   └── logs.db          # Local database
├── processor/           # Log processing engine
└── alerts.log           # Monitored event stream
