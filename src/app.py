import sys
import typer
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer

DELAY = 3

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRN Typer")
        self.resize(400, 200)
        layout = QVBoxLayout()

        self.label = QLabel("Click below to start the auto typer.\n\nOnce you start, CLICK on the first CRN box in the add/drop/withdrawl page.\n\nYou will have 3 seconds to do so before the program begins to type.")
        layout.addWidget(self.label)

        self.button = QPushButton("Start")
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.counter = DELAY
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_countdown)

    def on_button_click(self):
        # If the button already says "Close", then close the app.
        if self.button.text() == "Close":
            self.close()
            return

        self.counter = DELAY
        self.timer.start(1000)  # tick every 1 second

    def update_countdown(self):
        if self.counter > 0:
            self.label.setText(f"Starting in {self.counter} second{'s' if self.counter != 1 else ''}...")
            self.counter -= 1
        else:
            self.timer.stop()
            self.label.setText("Typing...")
            # Run typer.typer() in a separate thread to keep the GUI responsive.
            threading.Thread(target=self.run_typer, daemon=True).start()

    def run_typer(self):
        typer.typer()  # This might block, so run it in a thread.
        # Schedule finishing steps in the main thread.
        QTimer.singleShot(0, self.finish_typing)

    def finish_typing(self):
        self.label.setText("CRNs have been entered and the form has been submitted.\n\nFollow me on Instagram @aaronperkel")
        self.button.setText("Close")
        self.button.clicked.disconnect()
        self.button.clicked.connect(self.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())