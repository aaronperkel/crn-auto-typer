"""
Aaron Perkel
Course Registration CRN Auto-Typer
"""

import pyautogui
import time

# List of CRNs to enter
crns = [('12007', 'CS3050 - Software Engineering'),
        ('12435', 'CS3930 - Computing Career Preparation'),
        ('15862', 'MATH3766 - Chaos,Fractals&Dynmcal Syst'),
        ('12568', 'NFS1053L - Basic Concepts of Foods LAB'),
        ('12777', 'NFS1053 - Basic Concepts of Foods')]

# Wait for the user to click on the first text box
for i in range(3, 0, -1):
    if i > 1:
        print(f"Starting in {i} seconds...", end='\r')
    else:
        print(f"Starting in {i} second....", end='\r')
    time.sleep(1)

# Type each CRN and press 'Tab' to move to the next text box
for crn in crns:
    pyautogui.typewrite(crn[0])
    pyautogui.press('tab')  # Move to the next text box
    time.sleep(0.05)  # Small delay for stability

# Submit the form by pressing 'Enter'
pyautogui.press('enter')

print("CRNs have been entered and the form has been submitted.")

for i, crn in enumerate(crns):
    print(f'  {i+1}. {crn[0]} -> {crn[1]}')
