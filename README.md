# Password Generator & Strength Tester (password_tool.py)

An interactive, terminal-based Python application designed to generate highly secure random passwords and evaluate the strength of user-defined credentials. This tool leverages native Python libraries to demonstrate core logic structures, conditional formatting, and algorithmic strength validation.

---

## Technical Overview

The application features an interactive menu-driven interface that allows users to seamlessly switch between password generation and strength auditing. It handles user inputs securely, validates input data types to prevent execution crashes, and applies character-matching logic to check for cryptographic safety.

### Key Features
* **Custom Length Password Generation:** Dynamically combines uppercase letters, lowercase letters, numerical digits, and special punctuation characters to generate unpredictable character sequences.
* **Algorithmic Strength Tester:** Audits any input password against strict cybersecurity criteria (length, character variety, and complexity) to give real-time safety feedback.
* **Input Validation Guardrails:** Prevents software errors by catching invalid integer inputs and protecting against short, insecure password generation requests.

---

## Technology Stack

* Language Platform: Python 3
* Core Built-in Modules:
  * random — Manages cryptographically pseudo-random character selection loops.
  * string — Supplies pre-configured arrays of ASCII letters, numbers, and symbols.

---

## Installation & Setup

1. Open your Anaconda Prompt or standard command line terminal.
2. Change your path to your project folder using the directory command:
   cd OneDrive\Desktop\AI_Agents
3. Launch the script using your Python interpreter:
   python password_tool.py

---

## User Instructions & Options Guide

Once the terminal loop starts, select one of the following menu numbers:

### Option 1: Generate a New Password
Creates a completely randomized string based on your preferred length.
* Selection: 1
* Prompt: Enter desired password length (e.g., 14)
* Output Example: Generated Password: k#9P!mZ_q90rK$

### Option 2: Test a Custom Password
Evaluates an existing password to find out how secure it is against automated attacks.
* Selection: 2
* Prompt: Enter your password to test
* Output Evaluation Scale:
  * Strong 💪 (12+ characters, includes letters, digits, and special symbols)
  * Medium ⚠️ (8+ characters, includes letters and digits)
  * Weak ❌ (Fails to meet basic length or character variety requirements)

### Option 3: Safe Application Exit
Closes the script execution safely.
* Selection: 3
* Output: Shutting down Password Tool. Goodbye!

---

## Logical Flow Chart

[Main Menu Selection] ➔ [Option 1 or 2] ➔ [Run Generation / Run Security Audit] ➔ [Print Result & Strength Rating] ➔ [Loop Back to Menu]
