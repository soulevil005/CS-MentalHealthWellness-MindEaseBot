# CS-MentalHealthWellness-MindEaseBot

# 🌿 MindEase — Conversational Mental-Health Wellness Chatbot

**MindEase** is a privacy-aware, extendable conversational assistant built with **Rasa Open Source** and containerized with **Docker**.  
Its purpose is to provide non-clinical mental-wellness support: mood checks, breathing exercises, journaling prompts, grounding techniques and guided self-care suggestions. MindEase is designed for research, prototyping, and integration into web or mobile frontends — not as a clinical or emergency service.

---

## Key features

- Intent classification & entity extraction using Rasa NLU  
- Dialogue management via Rasa Core (stories, rules, policies)  
- Custom actions for mood logging and guided exercises (actions server)  
- Dockerized for reproducible deployment and easy orchestration  
- Simple to extend: swap NLU pipeline, add pre-trained backbones, connect trackers/databases

---
## Repo structure
cs-project/
├─ actions/
│ └─ actions.py
├─ config.yml
├─ domain.yml
├─ data/
│ ├─ nlu.yml
│ ├─ stories.yml
│ └─ rules.yml
├─ models/
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
├─ README.md
└─ rasa_setup.txt
└─ docker_setup.txt

---

## Quickstart (recommended)

> **Prerequisite:** this project targets **Python 3.10.0**. Create a virtual environment using Python 3.10.0 before installing dependencies.

### Local (development, no Docker)
1. Create & activate venv (Python 3.10.0):
   ```bash
   python3.10 -m venv .venv
   source .venv/bin/activate        # macOS / Linux
   .venv\Scripts\activate           # Windows (PowerShell use: .\.venv\Scripts\Activate.ps1)
