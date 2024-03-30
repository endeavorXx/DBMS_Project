from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 706)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 40, 731, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(30, 20, 30, 20)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")

        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName("widget")

        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 691, 71))
        self.frame.setStyleSheet("background-color: #4CAF50; border-radius: 10px;")
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 10, 591, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: white;")

        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setGeometry(QtCore.QRect(60, 100, 551, 450))
        self.widget1.setObjectName("widget1")

        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(10, 20, 10, 20)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")

        self.labels = [
            "Order ID:", "Transaction ID:", "Combo Text:",
            "Customer:", "Order Date:", "Order Time:",
            "Some Label:", "Total:"
        ]

        self.values = [
            self.order_id, self.transaction_id, self.comboText,
            self.myCustomer["first_name"] + " " + self.myCustomer["last_name"],
            str(self.order_date), str(self.order_time),
            "", str(self.total)
        ]

        for i, (label_text, value_text) in enumerate(zip(self.labels, self.values)):
            label = QtWidgets.QLabel(self.widget1)
            label.setObjectName(f"label_{i}")
            label.setText(label_text)
            label.setWordWrap(True)
            self.gridLayout.addWidget(label, i, 0, 1, 1)

            value = QtWidgets.QLabel(self.widget1)
            value.setObjectName(f"value_{i}")
            value.setText(value_text)
            value.setWordWrap(True)
            self.gridLayout.addWidget(value, i, 1, 1, 1)

        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Order Details"))

# Usage:
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
