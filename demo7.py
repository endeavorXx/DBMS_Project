from PyQt5 import QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.addItem("Option 1")
        self.comboBox.addItem("Option 2")
        self.comboBox.addItem("Option 3")
        
        self.comboBox.setStyleSheet("""
            QComboBox QAbstractItemView {
                border: 1px solid black;
            }
            # QComboBox::drop-down {
            #     width: 20px;
            #     height: 20px;
            #     border-radius: 10px;
            #     border: 1px solid black;
            # }
            QComboBox::down-arrow, QComboBox::up-arrow {
                image: url(down_arrow.png);
                width: 20px;
                height: 20px;
                border-radius: 10px;
                border: none;
            }
        """)
        
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.comboBox)

app = QtWidgets.QApplication([])
window = MyWindow()
window.show()
app.exec_()
