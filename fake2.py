import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class FileDialogDropExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Dialog with Drag and Drop")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel()
        self.label.setText("Drop Files Here")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        self.button = QPushButton("Open File Dialog")
        self.button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.button)

        # Enable drag and drop events
        self.setAcceptDrops(True)
        

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            print("selected file :", selected_files)
        self.path = selected_files


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileDialogDropExample()
    window.show()
    
    sys.exit(app.exec_())
