import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon, QIntValidator
from admin_login import Ui_MainWindow
from connect_database import connectDatabase

class SignupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('signup.ui', self)  # Load the UI for signup window
        self.enterButton.clicked.connect(self.register)
        
    def register(self):
        self.firstname = self.lineEdit.text()
        self.lastname = self.lineEdit.text()
        self.phone_no = self.lineEdit.text()
        self.street = self.lineEdit.text()
        self.city = self.lineEdit.text()
        self.state = self.lineEdit.text()
        self.password = self.lineEdit.text()

        # Upload details to the database  

        # if (self.firstname == "" or self.lastname == "" or self.phone_no == "" or self.street == "" or self.city == "" or self.state == "" or self.password == ""):
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
        if (username == 'admin') and (password == 'admin123'):
            print("Login successful")
            self.close()
            self.MainWindow = QtWidgets.QMainWindow()
            # self.home_window = HomePage()
            # self.home_window.setupUi(self.MainWindow, username)
            # self.MainWindow.show()
            self.adminui = Ui_MainWindow()
            self.adminui.setupUi(self.MainWindow)
            self.MainWindow.show()

            self.db = connectDatabase()
            self.customer_id = self.adminui.lineEdit
            # This will validate that input number is int
            self.customer_id.setValidator(QIntValidator())

            self.first_name = self.adminui.lineEdit_2
            self.last_name = self.adminui.lineEdit_3
            self.phone_no = self.adminui.lineEdit_4
            self.phone_no.setValidator(QIntValidator())
            self.street = self.adminui.lineEdit_5
            self.city = self.adminui.lineEdit_6
            self.state = self.adminui.lineEdit_7
            self.pin_code = self.adminui.lineEdit_8
            self.pin_code.setValidator(QIntValidator())

            self.add_btn = self.adminui.addButton
            self.update_btn = self.adminui.updateButton
            self.select_btn = self.adminui.selectButton
            self.search_btn = self.adminui.searchButton
            self.delete_btn = self.adminui.deleteButton

            self.result_table = self.adminui.tableWidget
            self.result_table.setSortingEnabled(False)
            self.buttons_list = self.adminui.function_frame.findChildren(QPushButton)
            # Initialize signal slot connection

            self.init_signal_slot()

            #populate initial data in the table and state/city dropdowns
            self.search_info()


        else:
            print("Invalid username or password")

    def init_signal_slot(self):
        # Connect button to their respective functions
        self.add_btn.clicked.connect(self.add_info)
        self.delete_btn.clicked.connect(self.delete_info)
        self.search_btn.clicked.connect(self.search_info)
        self.update_btn.clicked.connect(self.update_info)        
        self.select_btn.clicked.connect(self.select_info)              

    def search_info(self):
        # function for searching and populate the student data
        # self.update_street_city_state()
        customer_info = self.get_customer_info()
        print(customer_info)

        customer_result = self.db.search_customer_info(
            customer_id = customer_info["customer_id"],
            first_name = customer_info["first_name"],
            last_name = customer_info["last_name"],
            phone_no = customer_info["phone_no"],
            street = customer_info["street"],
            city = customer_info["city"],
            state = customer_info["state"],
            pin_code = customer_info["pin_code"],
        )

        print(customer_result)
        self.show_data(customer_result)
    
    def show_data(self, result):
        # Function to populate the table with student information
        if result:
            self.result_table.setRowCount(0)
            self.result_table.setRowCount(len(result))

            for row, info in enumerate(result):
                info_list = [
                    info["customer_id"],
                    info["first_name"],
                    info["last_name"],
                    info["phone_no"],
                    info["street"],
                    info["city"],
                    info["state"],
                    info["pin_code"]
                ]

                for column,item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.result_table.setItem(row, column, cell_item)
        else:
            self.result_table.setRowCount(0)
            return 

    def add_info(self):
        # self.disable_buttons()
        customer_info = self.get_customer_info()


    def delete_info(self):
        pass

    def update_info(self):
        pass

    def select_info(self):
        pass
    
    def disable_buttons(self):
        for button in self.buttons_list:
            button.setDisabled(True)

    def enable_buttons(self):
        for button in self.buttons_list:
            button.setDisabled(False)

    def get_customer_info(self):
        #Function to retrive data from the form
        customer_id = self.customer_id.text().strip()
        first_name = self.first_name.text().strip()
        last_name = self.last_name.text().strip()
        phone_no = self.phone_no.text().strip()
        street = self.street.text().strip()
        city = self.city.text().strip()
        state = self.state.text().strip()
        pin_code = self.pin_code.text().strip()

        ## add pincode information later when table in database is changed with extra column for pin code
        customer_info = {
            "customer_id": customer_id,
            "first_name": first_name,
            "last_name" : last_name,
            "phone_no" : phone_no,
            "street" : street,
            "city" : city,
            "state" : state,
            "pin_code" : pin_code
        } 
        return customer_info

    def open_signup_window(self):
        self.close()
        signup_window.show()

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

from PyQt5.QtWidgets import QToolButton, QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize

class CustomToolButton(QToolButton):
    def __init__(self, icon_path, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon(icon_path))
        self.setIconSize(QSize(self.size().width(), self.size().height()))  # Set initial icon size to button size
        self.setStyleSheet("QToolButton { border: none; background-color: transparent; }")  # Set button style

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Dynamically adjust the icon size based on the button size
        icon_size = min(self.width(), self.height()) * 0.8  # Set icon size to 80% of button size
        self.setIconSize(QSize(icon_size, icon_size))


class HomePage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow, user):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #f0f0f0;")  # Set background color

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Adjusted spacing between items in the scroll area
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("background-color: transparent;")  # Transparent background
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -175, 1222, 1222))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        # Add margins to the scroll area and its contents
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)  # Set margins
        
        # Add multiple items using a for loop extract these from database
        items = [("A2Milk-min.jpg", "MILK"), ("eggs.jpeg", "EGGS"), ("butter.jpg", "BUTTER"),
                 ("download.jpg", "BREAD"), ("macaroni.jpg", "PASTA"), ("brown rice.jpg", "BROWN RICE"),
                 ("olive_oil.jpg", "OLIVE OIL")]
        
        for item_image, item_name in items:
            frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            frame.setMinimumSize(QtCore.QSize(200, 200))
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setObjectName("frame")
            frame.setStyleSheet("background-color: #ffffff; border-radius: 10px;")  # White background and rounded corners

            # Add item photo
            item_photo = QtWidgets.QLabel(frame)
            item_photo.setGeometry(QtCore.QRect(20, 20, 111, 121))  # Adjusted position
            item_photo.setText("")
            item_photo.setPixmap(QtGui.QPixmap(item_image))
            item_photo.setScaledContents(True)
            item_photo.setObjectName(f"{item_name.lower()}_photo")

            # Add item label
            item_label = QtWidgets.QLabel(frame)
            item_label.setGeometry(QtCore.QRect(140, 30, 131, 41))  # Adjusted position
            item_label.setObjectName(f"{item_name.lower()}_label")
            item_label.setText(item_name)
            item_label.setStyleSheet("font-weight: bold; font-size: 14px;")  # Bold text

            # Add item button
            item_button = QtWidgets.QPushButton(frame)
            item_button.setGeometry(QtCore.QRect(140, 90, 93, 28))  # Adjusted position
            item_button.setObjectName(f"{item_name.lower()}_button")
            item_button.setText("BUY NOW")
            item_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px;")  # Styled button
            item_button.clicked.connect(lambda checked, name=item_name: self.show_item_details(name))
            
            self.verticalLayout_2.addWidget(frame)

        # Add basket icon on the top right corner
        basket_icon = CustomToolButton("basket_icon.jpg", self.centralwidget)
        basket_icon.setGeometry(QtCore.QRect(self.width(), 10, 80, 80))  # Adjusted position and size
        basket_icon.setObjectName("basket_icon")
        basket_icon.setToolTip("View Basket")  # Tooltip for the icon

        self.setCentralWidget(self.centralwidget)
        basket_icon.clicked.connect(self.view_basket)  # Connect the clicked signal to view_basket method
        
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
        
    def view_basket(self):
        # Implement the logic to show the basket contents here
        self.item_details_window = QtWidgets.QMainWindow()
        self.ui = Ui_ItemDetailsWindow()
        self.ui.setupUi(self.item_details_window)
        self.ui.label.setText(f"Item Details for cart")
        self.item_details_window.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    login_window = LoginWindow()
    signup_window = SignupWindow()
    
    login_window.show()

    sys.exit(app.exec_())