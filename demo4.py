import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QScrollArea
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class SignupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('signup.ui', self)  # Load the UI for signup window
        self.enterButton.clicked.connect(self.register)
        
    def register(self):
        firstname = self.lineEdit.text()
        lastname = self.lineEdit.text()
        phone_no = self.lineEdit.text()
        street = self.lineEdit.text()
        city = self.lineEdit.text()
        state = self.lineEdit.text()
        password = self.lineEdit.text()

        # Upload details to the database
        print(firstname)
        
        # if (firstname == "" or lastname == "" or phone_no == "" or street == "" or city == "" or state == "" or password == ""):
        #     self.enterButton.clicked.connect(self.show_popup)
        # else:
        self.close()
        login_window.show()

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Warning!!")
        msg.setText("Wrong credentials")

        #to show the message box
        x = msg.exec_()


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('login_ui.ui', self)  # Load the UI from the converted Python file

        self.login_button.clicked.connect(self.login)
        self.signup_button.clicked.connect(self.open_signup_window)

    def login(self):
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        # Perform authentication, e.g., check against a database
        if username == 'admin' and password == 'admin123':
            print("Login successful")
            self.close()
            MainWindow.show()

            # You can add further actions here such as opening a new window
        else:
            print("Invalid username or password")

    def open_signup_window(self):
        self.close()
        signup_window.show()

class HomePage(QMainWindow):

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
        items = [("A2Milk-min.jpg", "MILK"), ("eggs.jpeg", "EGGS"), ("butter.jpg", "BUTTER"), ("download.jpg", "BREAD"), ("macaroni.jpg", "PASTA"), ("brown rice.jpg", "BROWN RICE"), ("olive_oil.jpg", "OLIVE OIL")]
        
        for item_image, item_name in items:
            frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            frame.setMinimumSize(QtCore.QSize(200, 200))
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    login_window = LoginWindow()
    signup_window = SignupWindow()

    MainWindow = QtWidgets.QMainWindow()
    home_window = HomePage()
    home_window.setupUi(MainWindow)

    login_window.show()
    sys.exit(app.exec_())