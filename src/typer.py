"""
Aaron Perkel
typer.py script
"""

import time
import reader
import pyautogui

# List of CRNs to enter
CRNS = reader.read_crns('./crns.txt')

def typer():
    # Iterate over CRNS with index
    for i, crn in enumerate(CRNS):
        pyautogui.typewrite(crn)
        if i != len(CRNS) - 1:
            pyautogui.press('tab')  # Move to the next text box
            time.sleep(0.05)  # Small delay for stability

    # Submit the form by pressing 'Enter'
    pyautogui.press('enter')

def main():
    print(CRNS)
     
if __name__ == '__main__':
    main()