"""
Aaron Perkel
Course Registration CRN Auto-Typer w/ GUI
"""

import sys
import typer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

DELAY = 3

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRN Typer")
        self.resize(400, 200)
        layout = QVBoxLayout()

        self.label = QLabel("Click below to start the auto typer.")
        layout.addWidget(self.label)

        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def on_button_click(self):
        for i in range(DELAY, 0, -1):
            self.label.setText(f"Starting in {i} second{'s' if i != 1 else ''}...")
        typer.main()
        self.label.setText("CRNs have been entered and the form has been submitted.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())