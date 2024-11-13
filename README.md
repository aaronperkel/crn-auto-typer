# Course Registration CRN Auto-Typer
**Author:** Aaron Perkel

## Overview
The Course Registration CRN Auto-Typer is a Python script designed to automate the entry of Course Registration Numbers (CRNs) into a university’s online registration form. By utilizing the `pyautogui` library, the script simulates keyboard input to quickly and efficiently input CRNs, navigate between form fields, and submit the registration form.

## Features
- Automated CRN Entry: Automatically types in a list of CRNs into the registration form.
- Form Navigation: Uses the ‘Tab’ key to move between input fields.
- Form Submission: Submits the form by pressing ‘Enter’ after entering all CRNs.
- User-Friendly Countdown: Provides a countdown to allow the user to prepare before the automation begins.
- Confirmation Output: Prints a summary of the CRNs entered and their corresponding course names.

 ## Prerequisites
- Python 3.x: Ensure you have Python 3 installed on your system.
- `pyautogui` Library: Install the `pyautogui` library for simulating keyboard input.
 ```bash
pip install pyautogui
```
- Pillow Library (Optional): Required for certain functionalities of pyautogui.
 ```bash
pip install pillow
```

## Usage
1. Prepare Your Environment
  -	Open your web browser and navigate to your university’s course registration page.
	- Log in to your account and navigate to the page where you input CRNs.
	- Ensure that the first CRN input field is visible and accessible.
2. Update the CRN List
Edit the script to include your specific CRNs and course names:
```python
crns = [
    ('12007', 'CS3050 - Software Engineering'),
    ('12435', 'CS3930 - Computing Career Preparation'),
    ('15862', 'MATH3766 - Chaos,Fractals&Dynmcal Syst'),
    ('12568', 'NFS1053L - Basic Concepts of Foods LAB'),
    ('12777', 'NFS1053 - Basic Concepts of Foods')
]
```
Replace the CRNs and course names with your desired courses.
3. Run the Script
- Open a terminal or command prompt in the directory containing crn_auto_typer.py.
- Run the script using the command:
```bash
python crn_auto_typer.py
```
## Disclaimer
- Compliance with University Policies
	- Before using this script, ensure that automating the registration process does not violate your university’s policies or terms of service.
	- Unauthorized automation may lead to penalties, including account suspension.
- Use at Your Own Risk
	- This script is provided “as is” without warranty of any kind.
	- The author is not responsible for any consequences resulting from the use of this script.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
