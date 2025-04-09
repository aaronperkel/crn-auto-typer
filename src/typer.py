"""
Aaron Perkel
Course Registration CRN Auto-Typer
"""

import time
import pyautogui

# List of CRNs to enter
CRNS = [('12007', 'CS3050 - Software Engineering'),
        ('12435', 'CS3930 - Computing Career Preparation'),
        ('15862', 'MATH3766 - Chaos,Fractals&Dynmcal Syst'),
        ('12568', 'NFS1053L - Basic Concepts of Foods LAB'),
        ('12777', 'NFS1053 - Basic Concepts of Foods')]

def main():
    # Type each CRN and press 'Tab' to move to the next text box
    for crn in CRNS:
        pyautogui.typewrite(crn[0])
        pyautogui.press('tab')  # Move to the next text box
        time.sleep(0.05)  # Small delay for stability

    # Submit the form by pressing 'Enter'
    pyautogui.press('enter')

    # Prints just for sanity sake
    for i, crn in enumerate(CRNS):
        print(f'  {i+1}. {crn[0]} -> {crn[1]}')
        
if __name__ == '__main__':
    main()