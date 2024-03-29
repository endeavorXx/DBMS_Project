from PyQt5.QtWidgets import QApplication, QMainWindow, QSpinBox, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Real-Time Total Calculation")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.item_price = 10  # Example item price

        self.quantity_spinbox = QSpinBox()
        self.quantity_spinbox.setRange(0, 100)  # Set range for quantity
        self.quantity_spinbox.valueChanged.connect(self.calculate_total)

        self.total_label = QLabel()

        layout.addWidget(self.quantity_spinbox)
        layout.addWidget(self.total_label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def calculate_total(self):
        quantity = self.quantity_spinbox.value()
        total_amount = quantity * self.item_price
        self.total_label.setText(f"Total Amount: {total_amount}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
