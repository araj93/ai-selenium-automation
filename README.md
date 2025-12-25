# AI-Powered Selenium Automation Framework (Python)

This repository contains a **Python Selenium automation framework enhanced with AI concepts** such as **self-healing locators** and **AI-safe fallback logic**.

The goal of this project is to demonstrate how **traditional Selenium automation** can be improved using **AI assistance**, while still remaining stable when AI is unavailable.

---

## Why This Project?

In real-world UI automation:
- Locators break frequently
- Tests fail unnecessarily
- Maintenance cost is high

This framework solves that by:
- Using **AI (or mock AI)** to recover broken locators
- Ensuring **tests never crash due to AI failures**
- Keeping the architecture **simple and interview-ready**

---

## How It Works (Simple Flow)

Test Case
↓
Page Object
↓
BasePage.find()
↓
Selenium tries locator
↓
❌ Locator fails
↓
AI / Mock AI suggests new locator
↓
Selenium retries
↓
✅ Test continues


ai_selenium_automation/
│
├── ai/
│ ├── openai_client.py # AI / Mock AI logic
│ ├── prompt_templates.py # AI prompts
│ ├── locator_healer.py # Self-healing logic
│
├── core/
│ ├── driver_factory.py # WebDriver setup
│ ├── base_page.py # Smart element finder
│
├── pages/
│ └── login_page.py # Page Objects
│
├── tests/
│ ├── test_google.py # Basic Selenium test
│ └── test_login_ai.py # AI-enabled test
│
├── requirements.txt
├── main.py
├── README.md
└── .gitignore