# network-audit-tool
Python tool for LAN scanning, auditing, and basic security (ping TCP port scan)

## 🛡️ Network Audit Tool

A simple yet effective Python tool to perform basic LAN scanning and security checks.

This is the first step of a personal project aimed at improving my skills in system administration, networking, and cybersecurity through hands-on scripting.

## 🔍 Features

- Host discovery via ICMP ping (`ping3`)
- TCP port scanning on common service ports
- Clean, readable console output
- Modular structure (functions for easy reuse and updates)

---

## ⚙️ Technologies Used

- **Python 3.x**
- [`ping3`](https://pypi.org/project/ping3/) – for sending ICMP echo requests
- Built-in `socket` module – for TCP port connections

---

## 📦 Installation

1. Make sure Python 3.10+ is installed on your system
2. Install dependencies:
    bash
    pip install ping3

---

## 🚀 How to Run

python lan_scanner.py
You can customize the IP range directly in the script.

---

## 🧪 Example Output

🔗 Scanning IP: 192.168.1.1
✅ Host is active
📋 Open ports: [80, 443]
🔗 Scanning IP: 192.168.1.2
❌ Host is not responding

---

## 🧠 Why I Built This

This tool is part of my learning path as I work towards becoming a Network Administrator with a strong focus on cybersecurity.
By creating tools like this from scratch, I'm improving my ability to:

- Automate common IT tasks

- Understand what happens "under the hood" in a network

- Build solid foundations for more advanced security tools

---

## 🛣️ Roadmap (Upcoming Features)

- Export scan results to .txt or .csv

- Alert system via Telegram or email

- Banner grabbing for open ports

- Auto-hardening actions on vulnerable hosts (experimental)

---

## 👨‍💻 Author

Alessandro – aspiring network/system engineer on a mission to break into the world of cybersecurity.


Want to try the tool, contribute, or just give feedback?
Feel free to fork, open an issue, or message me on LinkedIn.
