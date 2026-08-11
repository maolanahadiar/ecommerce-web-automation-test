# Ecommerce Web Automation Test

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.45-green)
![Pytest](https://img.shields.io/badge/Pytest-9.1-orange)
![Allure](https://img.shields.io/badge/Allure-2.16-red)

This project contains automated test for the [DemoBlaze Ecommerce Website](https://demoblaze.com) built with Python, Selenium, Pytest to demonstrates best practices for web automation testing with Allure reporting, GitHub Actions CI/CD integration, and automated test summary notifications through Telegram.

---

## Project Architecture

- Built using the Page Object Model (POM) design pattern
- Maintains separation of concerns between tests, page objects, and test data
- Follows clean code principles and Python coding standards

---

## Web Automation Testing Coverage

### 🟢 Positive Scenarios

| Module | Scenario | Status |
|:--|:--|:--:|
| **Authentication** | Login with valid credentials | ✅ |
| | Register new account | ✅ |
| | Logout account | ✅ |
| **Product** | View product details | ✅ |
| **Cart** | Add product to cart | ✅ |
| | View product details in cart | ✅ |
| | Remove product from cart | ✅ |
| **Checkout** | Complete checkout process | ✅ |

### 🔴 Negative Scenarios

| Module | Scenario | Status |
|:--|:--|:--:|
| **Authentication** | Login with invalid password | ✅ |
| | Login with empty credentials | ✅ |
| | Login with non-existing account | ✅ |

---

## Setup

1. Clone repository:

```bash
git clone https://github.com/maolanahadiar/ecommerce-web-automation-test.git
```

2. Move to project directory:

```bash
cd ecommerce-web-automation-framework
```

3. Create virtual environment:

```bash
python -m venv venv
```

4. Activate virtual environment:

- macOS/Linux

```bash
source venv/bin/activate
```

- Windows

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run Tests

Run all tests:

```bash
pytest
```

Run specific tests:

```bash
pytest tests/test_login.py
```

Run & generate allure report:

```bash
pytest --alluredir=reports/allure-results
```

Open allure report:

```bash
allure serve reports/allure-results
```

---

## Demo Video
Ecommerce Web Automation: [Watch Demo](https://drive.google.com/file/d/1GMziW4Xoc74GA4weQlrsbmKe9K_sXGHK/view?usp=sharing)

---

## CI/CD

GitHub Actions pipeline automatically runs API tests on:

- Push
- Pull Request
- Manual Trigger

Pipeline flow:

```
Checkout Repository
   |
Setup Python Environment
   |
Install Google Chrome
   |
Install Dependencies
   |
Install Allure CLI
   |
Run Web UI Tests
   |
Generate Allure Report
   |
Deploy Allure Report to GitHub Pages
   |
Upload Test Artifacts
   |
Send Test Summary Notification to Telegram
```

#### Latest Execution Status:

[![Ecommerce Web Automation](https://github.com/maolanahadiar/ecommerce-web-automation-test/actions/workflows/selenium_ci.yml/badge.svg)](https://github.com/maolanahadiar/ecommerce-web-automation-test/actions/workflows/selenium_ci.yml)

---

## Test Report

> Example of test report using allure when all test cases are passed

<p align="center">
<img src="https://github.com/user-attachments/assets/6fb80430-7d5a-4069-b78c-bdaf7a4bff5f" width="900">

> Example of test report using allure when some test cases are failed

<p align="center">
<img src="https://github.com/user-attachments/assets/9c0d6d6b-de06-4ac6-8c94-c7d851bb7232" width="900">

➡️ [Click here to see the Live Allure Report](https://maolanahadiar.github.io/ecommerce-web-automation-test/)