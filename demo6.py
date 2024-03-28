import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ItemDetailsWindow(object):
    def setupUi(self, ItemDetailsWindow):
        ItemDetailsWindow.setObjectName("ItemDetailsWindow")
        ItemDetailsWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(ItemDetailsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 70, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        ItemDetailsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ItemDetailsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        ItemDetailsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ItemDetailsWindow)
        self.statusbar.setObjectName("statusbar")
        ItemDetailsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ItemDetailsWindow)
        QtCore.QMetaObject.connectSlotsByName(ItemDetailsWindow)

    def retranslateUi(self, ItemDetailsWindow):
        _translate = QtCore.QCoreApplication.translate
        ItemDetailsWindow.setWindowTitle(_translate("ItemDetailsWindow", "Item Details"))
        self.label.setText(_translate("ItemDetailsWindow", "Item Details Window"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -175, 1222, 1222))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Add multiple items using a for loop
        items = [("A2Milk-min.jpg", "MILK"), ("eggs.jpeg", "EGGS"), ("butter.jpg", "BUTTER"), ("download.jpg", "BREAD"), ("macaroni.jpg", "PASTA")]
        for item_image, item_name in items:
            frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            frame.setMinimumSize(QtCore.QSize(1200, 1200))
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setObjectName("frame")

            # Add item photo
            item_photo = QtWidgets.QLabel(frame)
            item_photo.setGeometry(QtCore.QRect(50, 40, 111, 121))
            item_photo.setText("")
            item_photo.setPixmap(QtGui.QPixmap(item_image))
            item_photo.setScaledContents(True)
            item_photo.setObjectName(f"{item_name.lower()}_photo")

            # Add item label
            item_label = QtWidgets.QLabel(frame)
            item_label.setGeometry(QtCore.QRect(220, 50, 131, 41))
            item_label.setObjectName(f"{item_name.lower()}_label")
            item_label.setText(item_name)

            # Add item button
            item_button = QtWidgets.QPushButton(frame)
            item_button.setGeometry(QtCore.QRect(220, 110, 93, 28))
            item_button.setObjectName(f"{item_name.lower()}_button")
            item_button.setText("BUY NOW")
            item_button.clicked.connect(lambda checked, name=item_name: self.show_item_details(name))

            self.verticalLayout_2.addWidget(frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 26))
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

    def show_item_details(self, item_name):
        self.item_details_window = QtWidgets.QMainWindow()
        self.ui = Ui_ItemDetailsWindow()
        self.ui.setupUi(self.item_details_window)
        self.ui.label.setText(f"Item Details for {item_name}")
        self.item_details_window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
