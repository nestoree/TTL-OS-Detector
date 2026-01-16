# 🖧 TTL-OS-Detector

A simple Python tool that estimates the operating system of a remote host by analyzing the **TTL (Time To Live)** value obtained from a ping request.

This project is intended for **educational and networking learning purposes**.

---

## 📌 What is TTL?

TTL (Time To Live) is a value included in IP packets that limits how many network hops a packet can take before being discarded.

Different operating systems typically use different **default TTL values**, which can be used as a basic form of **OS fingerprinting**.

---

## 🔍 How It Works

1. Sends a single `ping` request to a target IP or hostname.
2. Extracts the TTL value from the ping response.
3. Compares the TTL against common defaults.
4. Prints an estimated operating system based on the TTL.

---

## 🧠 TTL-Based OS Estimation

| TTL Value | Estimated System |
|----------|------------------|
| 128      | Windows          |
| 64       | Linux / macOS    |
| 255      | Network device (routers, Cisco, etc.) |

> ⚠️ Note: TTL values can be modified by firewalls, routers, or custom configurations.

---

## 🛠️ Features

- Cross-platform (Windows / Linux / macOS)
- Automatically detects the correct ping syntax
- No external dependencies
- Lightweight and easy to understand
- Beginner-friendly networking script

---

## 📦 Requirements

- Python 3.7+
- `ping` command available in system PATH

No external libraries required.

---

## ▶️ Usage

Run the script from the terminal:

```bash
python ttl_os_detector.py
