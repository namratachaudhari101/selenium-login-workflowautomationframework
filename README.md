
# Selenium Login and Workflow Automation Framework

## Problem Statement

Develop a reusable Selenium automation framework for automating a web application workflow. The framework should open the application, perform login, navigate through the application, perform required actions, validate the result, and maintain a clean and reusable project structure.

The framework uses the Page Object Model (POM) to separate page-related actions from test cases.

## Selenium Login and Workflow Automation Framework

A simple Python-based Selenium framework that automates the login workflow of a web application using Selenium WebDriver and Pytest.

The project is structured so that page actions, test cases, configuration, and WebDriver setup are maintained separately.

## What it does

1. WebDriver Setup – Initializes the Selenium WebDriver required for browser automation.
2. Login Page – Opens the application and enters the required login credentials.
3. Login Validation – Performs the login operation and verifies that the login was successful.
4. Home Page – Handles actions and navigation available after successful login.
5. Test Execution – Uses Pytest to execute the automation workflow.

## Why use Page Object Model?

The Page Object Model keeps the web-page elements and actions separate from the test code.

For example, login-related elements and actions are maintained in `login_page.py`, while the actual test flow is maintained in `test_login_workflow.py`.

This makes the code easier to understand, maintain, and reuse when changes are made to the web application.

## Technologies Used

* Python
* Selenium WebDriver
* Pytest
* Page Object Model (POM)

## Requirements

* Python 3.x
* Google Chrome
* Selenium
* Pytest
* ChromeDriver

The required Python packages can be installed using:


pip install -r requirements.txt
```

## Project Structure

Selenium-Login-Workflow/
│
├── chromedriver.exe
├── README.md
├── requirements.txt
├
│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   └── homepage.py
│
├── reports/
│
├── tests/
│   ├── __init__.py
│   └── test_login_workflow.py
│
└── utils/
    ├── __init__.py
    └── driver_factory.py
```

## How to Run

First, install the required dependencies:

pip install -r requirements.txt
```

Then run the test using:

pytest
```

To run the login workflow test specifically:

pytest tests/test_login_workflow.py
```

## Workflow

The current automation workflow is:

```text
Open Web Application
        ↓
Enter Login Credentials
        ↓
Click Login
        ↓
Navigate to Home Page
        ↓
Validate Successful Login
```

## What happens if the login fails?

The test validates the login workflow. If the expected successful-login condition is not achieved, the test is reported as failed by Pytest.

This helps identify whether the login workflow is working as expected.

## Files in this project

* `chromedriver.exe` – WebDriver executable used for browser automation.
* `config/config.py` – Contains configuration-related information.
* `pages/login_page.py` – Contains login page elements and actions.
* `pages/homepage.py` – Contains home page-related actions.
* `utils/driver_factory.py` – Handles WebDriver creation.
* `tests/test_login_workflow.py` – Contains the login workflow test.
* `requirements.txt` – Lists required Python packages.
* `README.md` – Project documentation.

## Possible Improvements

The framework can be extended in the future with:

* Search page automation
* Additional workflow test cases
* Logout automation
* Explicit waits for better stability
* Test reporting
* Support for multiple browsers
* Configuration for different environments
