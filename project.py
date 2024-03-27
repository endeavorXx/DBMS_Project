import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QScrollArea
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.close()
        login_window.show()


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
            home_window.show()

            # You can add further actions here such as opening a new window
        else:
            print("Invalid username or password")

    def open_signup_window(self):
        self.close()
        signup_window.show()

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('home.ui', self)  # Load the UI from the converted Python file

        # self.setWindowTitle("Scrollable Page")
        # self.setGeometry(100, 100, 800, 600)

        # # Create a scroll area
        # scroll_area = QScrollArea()
        # scroll_area.setWidgetResizable(True)

        # # Create a main widget for the scroll area
        # scroll_widget = QWidget()
        # scroll_area.setWidget(scroll_widget)

        # # Create a vertical layout for the main widget
        # layout = QVBoxLayout(scroll_widget)
        # scroll_widget.setLayout(layout)

        # label = QLabel("")
        # label.setGeometry(QtCore.QRect(80, 70, 111, 121))
        # label.setText("")
        # label.setPixmap(QtGui.QPixmap("A2Milk-min.jpg"))
        # label.setScaledContents(True)
        # layout.addWidget(label)

        # # Add content to the layout
        # for i in range(50):
        #     label = QLabel(f"Label {i}")
        #     layout.addWidget(label)

        # # Set the central widget as the scroll area
        # self.setCentralWidget(scroll_area)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    signup_window = SignupWindow()
    home_window = HomePage()
    login_window.show()
    sys.exit(app.exec_())
