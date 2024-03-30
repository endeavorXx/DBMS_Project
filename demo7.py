from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize notification sound
        

        # Setup your GUI here...

    def show_notification(self, message):
        # Show popup message
        QMessageBox.information(self, "Notification", message)

        # Play notification sound
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
