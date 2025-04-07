# Course Registration CRN Auto-Typer

**Author:** Aaron Perkel

## Overview
This repository contains a Python script that automates the entry of Course Registration Numbers (CRNs) into an online registration form, along with a simulator HTML page for local testing. The Python script, `autocrn.py`, uses the `pyautogui` library to simulate keyboard inputs for entering CRNs and submitting the form. The `simulator.html` file mimics a course registration form, making it easy to test the automation without needing access to the actual registration page.

## Repository Structure
- **autocrn.py** – Python script for automating CRN entry.
- **simulator.html** – A basic HTML page simulating a registration form for testing purposes.
- **LICENSE** – MIT License.
- **README.md** – This file.

## autocrn.py
**Purpose:**  
Automates the process of entering CRNs by simulating keyboard actions.

**Features:**
- **Automated CRN Entry:** Simulates typing each CRN.
- **Form Navigation:** Uses the Tab key to move between text boxes.
- **Countdown Timer:** Provides a countdown to allow you time to focus the first input field.
- **Automatic Submission:** Presses Enter to submit the form after all CRNs have been entered.

**Usage:**
1. Open your course registration page or use the simulator (see below).
2. Update the CRN list in the script as needed.
3. Run the script:
   ```bash
   python autocrn.py
   ```

## simulator.html

**Purpose:**
Acts as a test interface to simulate a course registration form, allowing you to see how the auto-typer interacts with a form.

**Usage:**
1. Open simulator.html in your web browser.
2. Click on the first text box to focus.
3. Run the autocrn.py script to automatically fill in the CRNs and submit the form.

## Prerequisites
- Python 3.x is required.
- `pyautogui` Library:
  ```bash
  pip install pyautogui
  ```
- Pillow Library (Required for some functionalities of pyautogui):
  ```bash
  pip install pillow
  ```

## Disclaimer
- University Policy Compliance:
  - Ensure that using this script does not violate your university’s policies or terms of service.
- Use at Your Own Risk:
  - This tool is provided “as is” without any warranty. The author is not responsible for any consequences arising from its use.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
