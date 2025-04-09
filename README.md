# CRN Auto-Typer

**Author:** Aaron Perkel

## Overview
This application automates the process of entering Course Registration Numbers (CRNs) into online registration forms. It features a simple GUI for easy operation and uses a text file for flexible CRN configuration.

## Features
- **User-Friendly GUI**: Simple interface with countdown timer and status updates
- **Configurable CRN List**: Edit the `crns.txt` file to customize your course registration numbers
- **Automated Form Navigation**: Automatically tabs between form fields and submits the form
- **Time-Saving**: Quickly enter multiple CRNs without typing each one manually

## Repository Structure
- **src/**
  - **app.py** - Main application with GUI interface
  - **typer.py** - Core automation logic for typing CRNs
  - **reader.py** - Utility for reading CRNs from text file
  - **crns.txt** - User-editable file containing CRNs to be entered
  - **simulator.html** - Test page mimicking a registration form
- **requirements.txt** - Python dependencies

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/aaronperkel/crn-auto-typer.git
cd crn-auto-typer
```

### 2. Create a Python Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

### 1. Configure Your CRNs
Edit the `src/crns.txt` file to include your Course Registration Numbers:
```
# Enter your CRNs below, one per line
# Lines starting with # are ignored

12345
67890
24680
13579
```

### 2. Run the Application
```bash
python src/app.py
```

### 3. Using the Auto-Typer
1. Open your university's course registration page in your browser
2. Click on the first CRN input field to focus it
3. Return to the auto-typer application and click "Start"
4. After the countdown finishes, the application will:
   - Type each CRN in your list
   - Navigate between fields with Tab
   - Submit the form automatically

### Testing with Simulator
Use the included `simulator.html` to test the functionality:
1. Open `src/simulator.html` in your web browser
2. Run the application and follow the steps above

## Disclaimer
- This tool is intended to save time during course registration and should be used in accordance with your university's policies.
- The author is not responsible for any unintended consequences of using this application.
- Test the application with the simulator before using it with your actual registration system.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.