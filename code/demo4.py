import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtMultimedia import QSound
from admin_customer import Ui_MainWindow
from login_ui import LoginMainWindow
from signup import SignUpMainWindow
from admin_selection_ui import SelectOption
from admin_order import AdminOrderWindow
from admin_product import AdminProductWindow
from admin_vendor import AdminVendorWindow
from admin_supply import AdminSupplyWindow
from connect_database import connectDatabase
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QSound
import hashlib
import datetime

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myLoginWindow = QtWidgets.QMainWindow()
        self.loginui = LoginMainWindow()
        self.loginui.setupUi(self.myLoginWindow)
        self.myLoginWindow.show()   
        self.db = connectDatabase()
        self.loginui.login_button.clicked.connect(self.login)
        self.loginui.signup_button.clicked.connect(self.open_signup_window)
        
    def login(self):

        self.username = self.loginui.username_lineEdit.text()
        self.password = self.loginui.password_lineEdit.text()

        # Perform authentication, e.g., check against a database
        print(self.username)
        if (self.username.strip() == 'a') and (self.password.strip() == 'a'):
            print("Login successful")
            self.close()
            self.adminlogin = AdminHomePage()

        else:
            self.authenticate_customer(self.username,self.password)
            print("Welcome Customer")
    
    def authenticate_customer(self,phone,pswd):
        customer_auth = self.db.get_customer_authentication(phone,pswd)

        if customer_auth:
            self.close()
            self.myCustomer = self.db.search_customer_info(None, None, None, self.username)
            self.MainWindow2 = QtWidgets.QMainWindow()
            self.home_window = HomePage(self.myCustomer)          
            self.home_window.setupUi(self.MainWindow2)
            self.MainWindow2.show()
        else:
            ## we can use a pop_up window or something
            print("Wrong credentials!!")

    def open_signup_window(self):
        self.close()
        signup_window.setupUi()

class SignupWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self):
        self.mySignUpWindow = QtWidgets.QMainWindow()
        self.signupui = SignUpMainWindow()
        self.signupui.setupUi(self.mySignUpWindow)
        self.mySignUpWindow.show()   
        self.db = connectDatabase()
        self.signupui.enterButton.clicked.connect(self.register)
        
    def register(self):
        self.firstname = self.signupui.lineEdit.text().strip()
        self.lastname = self.signupui.lineEdit_2.text().strip()
        self.phone_no = self.signupui.lineEdit_3.text().strip()
        self.street = self.signupui.lineEdit_4.text().strip()
        self.city = self.signupui.lineEdit_5.text().strip()
        self.state = self.signupui.lineEdit_6.text().strip()
        self.pin_code = self.signupui.lineEdit_7.text().strip()
        
        self.password = self.signupui.lineEdit_8.text().strip()

        # Upload details to the database -- Complete check aagainst phone_no, phone_must be unique 

        if (self.firstname == "" or self.lastname == "" or self.phone_no == "" or self.street == "" or self.city == "" or self.state == "" or self.password == ""):
            QMessageBox.information(self, "Missing Information", f"Please fill all fields", QMessageBox.StandardButton.Ok)
        else:
            l = self.db.search_customer_info(phone_no=self.phone_no)
            if l:
                QMessageBox.information(self, "Information", f"User already Registered", QMessageBox.StandardButton.Ok)
            else:
                self.db.add_customer_info(self.firstname,self.lastname,self.phone_no,self.street,self.city,self.state, self.pin_code,self.password)
                QMessageBox.information(self, "Registration", f"Registration successful", QMessageBox.StandardButton.Ok)
                self.mySignUpWindow.close()


class AdminHomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.MainWindow = QtWidgets.QMainWindow()
        self.adminchoice = SelectOption()
        self.adminchoice.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.dashboard_btn = self.adminchoice.dashboard_btn
        self.customer_btn = self.adminchoice.customer_btn
        self.product_btn = self.adminchoice.product_btn
        self.supplies_btn = self.adminchoice.supplies_btn
        self.exit_btn = self.adminchoice.exit_btn
        self.vendors_btn = self.adminchoice.vendors_btn
        self.orders_btn = self.adminchoice.order_btn
        self.init_signal_slot()

    def init_signal_slot(self):
        # self.dashboard_btn.clicked.connect(self.showDashboard)
        self.customer_btn.clicked.connect(self.showCustomer)
        self.product_btn.clicked.connect(self.showProducts)        
        self.orders_btn.clicked.connect(self.showOrders)  
        self.vendors_btn.clicked.connect(self.showVendors)  
        self.supplies_btn.clicked.connect(self.showSupplies)  
        self.exit_btn.clicked.connect(self.getExit)  

    # def showDashboard(self):
        
    def showCustomer(self):
        self.adminlogin = AdminCustomerPage()
    def showProducts(self):
        self.adminlogin = AdminProductPage()

    def showOrders(self):
        self.adminlogin = AdminOrdersPage()

    def showVendors(self):
        self.adminlogin = AdminVendorPage()

    def showSupplies(self):
        self.adminlogin = AdminSupplyPage()

    def getExit(self):
        self.MainWindow.close()


class AdminCustomerPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = connectDatabase()

        self.MainWindow = QtWidgets.QMainWindow()
        self.adminui = Ui_MainWindow()
        self.adminui.setupUi(self.MainWindow)
        self.MainWindow.show()

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
        self.clear_btn = self.adminui.clearButton

        self.result_table = self.adminui.tableWidget
        self.result_table.setSortingEnabled(False)
        self.buttons_list = self.adminui.function_frame.findChildren(QPushButton)
        # Initialize signal slot connection

        self.init_signal_slot()

        #populate initial data in the table and state/city dropdowns
        self.search_info()
    
    ## To Intialize button with signals
            
    def init_signal_slot(self):
        # Connect button to their respective functions
        self.add_btn.clicked.connect(self.add_new_customer_info)
        self.search_btn.clicked.connect(self.search_info)
        self.update_btn.clicked.connect(self.update_info)        
        self.select_btn.clicked.connect(self.select_info)  
        self.clear_btn.clicked.connect(self.clear_form_info)            


    ## For ADMIN ANALYSIS OF CUSTOMERS


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

        if pin_code.isdigit():
            pin_code = int(pin_code)
        else:
            print("Not all digits in pin code")

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
        print(customer_info)
        return customer_info
    
    def show_data(self, result):
        # Function to populate the table with student information
        if result:
            self.result_table.setRowCount(0)
            self.result_table.setRowCount(len(result))
            print(result)
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

    def add_new_customer_info(self):
        # self.disable_buttons()
        customer_info = self.get_customer_info()
        self.customer_id.setEnabled(False)

        print(customer_info)
        if customer_info["customer_id"]:
            QMessageBox.information(self, "Alert", f"Customer Id is automatically generated", QMessageBox.StandardButton.Ok)
        if customer_info["first_name"] == "" or customer_info["last_name"] == "" or customer_info["phone_no"] == "" or customer_info["street"] == "" or customer_info["city"]=="" or customer_info["state"]=="" or customer_info["pin_code"]=="":
             ## Alert that some input fields are missing
            QMessageBox.information(self, "Missing Information", f"Please fill all fields", QMessageBox.StandardButton.Ok)
        else:
            add_result = self.db.add_customer_info(
                first_name = customer_info["first_name"],
                last_name = customer_info["last_name"],
                phone_no = customer_info["phone_no"],
                street = customer_info["street"],
                city = customer_info["city"],
                state = customer_info["state"],
                pin_code = customer_info["pin_code"],
                pswd = "0000"                               ## Default password while adding a customer is "0000"
            )

        self.enable_buttons()
        self.customer_id.setEnabled(False)
        self.search_info()

    def update_info(self):
        new_customer_info = self.get_customer_info()
        # print(new_customer_info)

        if new_customer_info["customer_id"]:
            update_result = self.db.update_customer_info(
                customer_id= new_customer_info["customer_id"],
                first_name = new_customer_info["first_name"],
                last_name = new_customer_info["last_name"],
                phone_no = new_customer_info["phone_no"],
                street = new_customer_info["street"],
                city = new_customer_info["city"],
                state = new_customer_info["state"],
                pin_code = new_customer_info["pin_code"]
            )

            if update_result:
                QMessageBox.information(self, "Warning", f"Failed to update information: {update_result}, please try again", QMessageBox.StandardButton.Ok)
            else:
                self.search_info()
        else:
            QMessageBox.information(self, "Warning", "Please select one student information to update")

    def select_info(self):
        
        select_row = self.result_table.currentRow()
        if select_row!=-1:
            self.customer_id.setEnabled(False)
            customer_id = self.result_table.item(select_row, 0).text().strip()
            first_name = self.result_table.item(select_row, 1).text().strip()
            last_name = self.result_table.item(select_row, 2).text().strip()
            phone_no =  self.result_table.item(select_row, 3).text().strip()
            street =  self.result_table.item(select_row, 4).text().strip()
            city =  self.result_table.item(select_row, 5).text().strip()
            state =  self.result_table.item(select_row, 6).text().strip()
            pin_code =  self.result_table.item(select_row, 7).text().strip()

            self.customer_id.setText(customer_id)
            self.first_name.setText(first_name)
            self.last_name.setText(last_name)
            self.phone_no.setText(phone_no)
            self.street.setText(street)
            self.city.setText(city)
            self.state.setText(state)
            self.pin_code.setText(pin_code)
        else:
            QMessageBox.information(self, "Warning", "Please select one student information", QMessageBox.StandardButton.Ok)

    
    def check_customer_id(self, customer_id):

        result = self.db.search_info(customer_id = customer_id)
        return result
    
    def clear_form_info(self):
        self.customer_id.clear()
        self.customer_id.setEnabled(True)
        self.first_name.clear()
        self.last_name.clear()
        self.phone_no.clear()
        self.street.clear()
        self.city.clear()
        self.state.clear()
        self.pin_code.clear()
        self.search_info()
    
    def disable_buttons(self):
        for button in self.buttons_list:
            button.setDisabled(True)

    def enable_buttons(self):
        for button in self.buttons_list:
            button.setDisabled(False)


class AdminProductPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = connectDatabase()

        self.MainWindow = QtWidgets.QMainWindow()
        self.adminproduct = AdminProductWindow()
        self.adminproduct.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.product_id = self.adminproduct.lineEdit

        self.name = self.adminproduct.lineEdit_2
        self.category = self.adminproduct.lineEdit_3
        self.price = self.adminproduct.lineEdit_4
        self.rating = self.adminproduct.lineEdit_6
        self.qty = self.adminproduct.lineEdit_5
        self.description = self.adminproduct.lineEdit_7
        self.url = ""

        self.add_btn = self.adminproduct.addButton
        self.update_btn = self.adminproduct.updateButton
        self.select_btn = self.adminproduct.selectButton
        self.search_btn = self.adminproduct.searchButton
        self.clear_btn = self.adminproduct.clearButton
        self.img_btn = self.adminproduct.imgButton

        self.result_table = self.adminproduct.tableWidget
        self.result_table.setSortingEnabled(False)
        self.buttons_list = self.adminproduct.function_frame.findChildren(QPushButton)
        # Initialize signal slot connection

        self.init_signal_slot()

        #populate initial data in the table and state/city dropdowns
        self.search_info()
    
    ## To Intialize button with signals
            
    def init_signal_slot(self):
        # Connect button to their respective functions
        self.add_btn.clicked.connect(self.add_new_product_info)
        self.search_btn.clicked.connect(self.search_info)
        self.update_btn.clicked.connect(self.update_info)        
        self.select_btn.clicked.connect(self.select_info)  
        self.clear_btn.clicked.connect(self.clear_form_info)
        self.img_btn.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            print("Selected Files:", selected_files) 
            self.url = selected_files[0]

    def add_new_product_info(self):
        product_info = self.get_product_info()
        self.product_id.setEnabled(False)

        print(product_info)
        if product_info["product_id"]:
            QMessageBox.information(self, "Alert", f"Product Id is automatically generated", QMessageBox.StandardButton.Ok)
        
        if product_info["name"] == "" or product_info["category"] == "" or product_info["price"] == "" or product_info["rating"] == "" or product_info["qty"]=="" :
             ## Alert that some input fields are missing
            QMessageBox.information(self, "Missing Information", f"Please fill all fields", QMessageBox.StandardButton.Ok)
        else:
            product_info["rating"] = int(product_info["rating"])
            product_info["price"] = float(product_info["price"])
            product_info["qty"] = int(product_info["qty"])
            print(product_info)
            add_result = self.db.add_product_info(
                name = product_info["name"],
                category = product_info["category"],
                price = product_info["price"],
                rating = product_info["rating"],
                qty = product_info["qty"],
                description = product_info["description"],
                url = product_info["url"],
            )

        self.enable_buttons()
        self.product_id.setEnabled(True)
        self.search_info()

    def get_product_info(self):
        product_id = self.product_id.text().strip()
        name = self.name.text().strip()
        category = self.category.text().strip()
        price = self.price.text().strip()
        rating = self.rating.text().strip()
        qty = self.qty.text().strip()
        description = self.description.text().strip()
        url = self.url.strip()


        ## add pincode information later when table in database is changed with extra column for pin code
        product_info = {
            "product_id": product_id,
            "name": name,
            "category" : category,
            "price" : price,
            "rating" : rating,
            "qty" : qty,
            "description" : description,
            "url" : url
        } 
        # print(product_info)
        return product_info
    
    def search_info(self):
        product_info = self.get_product_info()
        print(product_info)

        product_result = self.db.search_product_info_All(
            product_id = product_info["product_id"],
            product_name = product_info["name"],
            product_category = product_info["category"],
            product_price = product_info["price"],
            product_rating = product_info["rating"],
            product_qty = product_info["qty"],
            product_desc = product_info["description"],
            image_url = product_info["url"],
        )

        print(product_result)
        self.show_data(product_result)

    def show_data(self, result):
        if result:
            self.result_table.setRowCount(0)
            self.result_table.setRowCount(len(result))
            print(result)
            for row, info in enumerate(result):
                info_list = [
                    info["product_id"],
                    info["name"],
                    info["category"],
                    info["price"],
                    info["rating"],
                    info["qty"],
                    info["description"],
                    info["url"]
                ]

                for column,item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.result_table.setItem(row, column, cell_item)
        else:
            self.result_table.setRowCount(0)
            return 
    
    def update_info(self):
        new_product_info = self.get_product_info()
        # print(new_customer_info)

        if new_product_info["product_id"]:
            update_result = self.db.update_product_info(
                product_id= new_product_info["product_id"],
                name = new_product_info["name"],
                category = new_product_info["category"],
                price = new_product_info["price"],
                rating = new_product_info["rating"],
                qty = new_product_info["qty"],
                description = new_product_info["description"],
                url = new_product_info["url"]
            )

            if update_result:
                QMessageBox.information(self, "Warning", f"Failed to update information: {update_result}, please try again", QMessageBox.StandardButton.Ok)
            else:
                self.search_info()
        else:
            QMessageBox.information(self, "Warning", "Please select one student information to update")

    def select_info(self):
        select_row = self.result_table.currentRow()
        if select_row!=-1:
            self.product_id.setEnabled(False)
            product_id = self.result_table.item(select_row, 0).text().strip()
            name = self.result_table.item(select_row, 1).text().strip()
            category = self.result_table.item(select_row, 2).text().strip()
            price =  self.result_table.item(select_row, 3).text().strip()
            rating =  self.result_table.item(select_row, 4).text().strip()
            qty =  self.result_table.item(select_row, 5).text().strip()
            desc =  self.result_table.item(select_row, 6).text().strip()
            url =  self.result_table.item(select_row, 7).text().strip()

            self. product_id.setText(product_id)
            self.name.setText(name)
            self.category.setText(category)
            self.price.setText(price)
            self.rating.setText(rating)
            self.qty.setText(qty)
            self.description.setText(desc)
        else:
            QMessageBox.information(self, "Warning", "Please select one student information", QMessageBox.StandardButton.Ok)

    def enable_buttons(self):
        for button in self.buttons_list:
            button.setDisabled(False)
    
    def disable_buttons(self):
        for button in self.buttons_list:
            button.setDisabled(True)

    def clear_form_info(self):

        self.product_id.clear()
        self.product_id.setEnabled(True)
        self.name.clear()
        self.category.clear()
        self.price.clear()
        self.rating.clear()
        self.qty.clear()
        self.description.clear()
        self.search_info()

class AdminOrdersPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = connectDatabase()

        self.MainWindow = QtWidgets.QMainWindow()
        self.adminorder = AdminOrderWindow()
        self.adminorder.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.order_id = self.adminorder.lineEdit
        self.transaction_id = self.adminorder.lineEdit_2
        self.customer_id = self.adminorder.lineEdit_3

        self.search_btn = self.adminorder.searchButton
        self.clear_btn = self.adminorder.clearButton

        self.result_table = self.adminorder.tableWidget
        self.result_table.setSortingEnabled(False)

        self.init_signal_slot()
        self.search_info()

    def init_signal_slot(self):
        self.search_btn.clicked.connect(self.search_info)
        self.clear_btn.clicked.connect(self.clearForm)

    def get_order_info(self):
        #Function to retrive data from the form
        customer_id = self.customer_id.text().strip()
        order_id = self.order_id.text().strip()
        transaction_id = self.transaction_id.text().strip()

        order_info = {
            "customer_id" : customer_id,
            "order_id" : order_id,
            "transaction_id" : transaction_id
        }
        return order_info
    
    def search_info(self):

        order_info = self.get_order_info()

        order_result = self.db.search_order_info(
            order_id = order_info["order_id"],
            customer_id = order_info["customer_id"],
            transaction_id=order_info["transaction_id"]
        )
        self.show_data(order_result)

    def show_data(self,result):
        if result:
            self.result_table.setRowCount(0)
            self.result_table.setRowCount(len(result))
            for row, info in enumerate(result):
                info_list = [
                    info["order_id"],
                    info["customer_id"],
                    info["payment_method"],
                    info["amount"],
                    info["transaction_id"],
                    info["order_date"],
                    info["order_time"],
                    info["delivery_date"],
                    info["delivery_status"]
                ]

                for column,item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.result_table.setItem(row, column, cell_item)
        else:
            self.result_table.setRowCount(0)
            return 

    def clearForm(self):
        self.customer_id.clear()
        self.transaction_id.clear()
        self.transaction_id.clear()
        self.search_info()

class AdminVendorPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = connectDatabase()

        self.MainWindow = QtWidgets.QMainWindow()
        self.adminvendor = AdminVendorWindow()
        self.adminvendor.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.vendor_id = self.adminvendor.lineEdit
        # This will validate that input number is int
        self.vendor_id.setValidator(QIntValidator())

        self.vendor_name = self.adminvendor.lineEdit_2
        self.street = self.adminvendor.lineEdit_3
        self.city = self.adminvendor.lineEdit_4
        self.state = self.adminvendor.lineEdit_5
        self.phone_no = self.adminvendor.lineEdit_6
        self.phone_no.setValidator(QIntValidator())

        self.add_btn = self.adminvendor.addButton
        self.update_btn = self.adminvendor.updateButton
        self.select_btn = self.adminvendor.selectButton
        self.search_btn = self.adminvendor.searchButton
        self.clear_btn = self.adminvendor.clearButton

        self.result_table = self.adminvendor.tableWidget
        self.result_table.setSortingEnabled(False)
        self.buttons_list = self.adminvendor.function_frame.findChildren(QPushButton)
        # Initialize signal slot connection

        self.init_signal_slot()

        #populate initial data in the table and state/city dropdowns
        self.search_info()
    
    ## To Intialize button with signals
            
    def init_signal_slot(self):
        # Connect button to their respective functions
        self.add_btn.clicked.connect(self.add_new_vendor_info)
        self.search_btn.clicked.connect(self.search_info)
        self.update_btn.clicked.connect(self.update_info)        
        self.select_btn.clicked.connect(self.select_info)  
        self.clear_btn.clicked.connect(self.clear_form_info)            


    ## For ADMIN ANALYSIS OF CUSTOMERS


    def search_info(self):
        # function for searching and populate the student data
        # self.update_street_city_state()
        vendor_info = self.get_vendor_info()
        print(vendor_info)

        vendor_result = self.db.search_vendor_info(
            vendor_id = vendor_info["vendor_id"],
            vendor_name = vendor_info["vendor_name"],
            street = vendor_info["street"],
            city = vendor_info["city"],
            state = vendor_info["state"],
            phone_no = vendor_info["phone_no"],
        )

        print(vendor_result)
        self.show_data(vendor_result)
    
    def get_vendor_info(self):
        #Function to retrive data from the form
        vendor_id = self.vendor_id.text().strip()
        vendor_name = self.vendor_name.text().strip()
        street = self.street.text().strip()
        city = self.city.text().strip()
        state = self.state.text().strip()
        phone_no = self.phone_no.text().strip()

        ## add pincode information later when table in database is changed with extra column for pin code
        vendor_info = {
            "vendor_id": vendor_id,
            "vendor_name": vendor_name,
            "street" : street,
            "city" : city,
            "state" : state,
            "phone_no" : phone_no
        } 
        print(vendor_info)
        return vendor_info
    
    def show_data(self, result):
        # Function to populate the table with student information
        if result:
            self.result_table.setRowCount(0)
            self.result_table.setRowCount(len(result))
            print(result)
            for row, info in enumerate(result):
                info_list = [
                    info["vendor_id"],
                    info["vendor_name"],
                    info["street"],
                    info["city"],
                    info["state"],
                    info["phone_no"]
                ]

                for column,item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.result_table.setItem(row, column, cell_item)
        else:
            self.result_table.setRowCount(0)
            return 

    def add_new_vendor_info(self):
        # self.disable_buttons()
        vendor_info = self.get_vendor_info()
        self.vendor_id.setEnabled(False)

        print(vendor_info)
        if vendor_info["vendor_id"]:
            QMessageBox.information(self, "Alert", f"Customer Id is automatically generated", QMessageBox.StandardButton.Ok)
        if vendor_info["vendor_name"] == "" or  vendor_info["phone_no"] == "" or vendor_info["street"] == "" or vendor_info["city"]=="" or vendor_info["state"]=="":
             ## Alert that some input fields are missing
            QMessageBox.information(self, "Missing Information", f"Please fill all fields", QMessageBox.StandardButton.Ok)
        else:
            add_result = self.db.add_vendor_info(
                vendor_name = vendor_info["vendor_name"],
                street = vendor_info["street"],
                city = vendor_info["city"],
                state = vendor_info["state"],
                phone_no = vendor_info["phone_no"]
            )

        self.enable_buttons()
        self.vendor_id.setEnabled(False)
        self.search_info()

    def update_info(self):
        new_vendor_info = self.get_vendor_info()
        # print(new_customer_info)

        if new_vendor_info["vendor_id"]:
            update_result = self.db.update_vendor_info(
                vendor_id= new_vendor_info["vendor_id"],
                vendor_name = new_vendor_info["vendor_name"],
                street = new_vendor_info["street"],
                city = new_vendor_info["city"],
                state = new_vendor_info["state"],
                phone_no = new_vendor_info["phone_no"]
            )

            if update_result:
                QMessageBox.information(self, "Warning", f"Failed to update information: {update_result}, please try again", QMessageBox.StandardButton.Ok)
            else:
                self.search_info()
        else:
            QMessageBox.information(self, "Warning", "Please select one student information to update")

    def select_info(self):
        
        select_row = self.result_table.currentRow()
        if select_row!=-1:
            self.vendor_id.setEnabled(False)
            vendor_id = self.result_table.item(select_row, 0).text().strip()
            vendor_name = self.result_table.item(select_row, 1).text().strip()
            street =  self.result_table.item(select_row, 2).text().strip()
            city =  self.result_table.item(select_row, 3).text().strip()
            state = self.result_table.item(select_row, 4).text().strip()
            phone_no =  self.result_table.item(select_row, 5).text().strip()

            self.vendor_id.setText(vendor_id)
            self.vendor_name.setText(vendor_name)
            self.phone_no.setText(phone_no)
            self.street.setText(street)
            self.city.setText(city)
            self.state.setText(state)
        else:
            QMessageBox.information(self, "Warning", "Please select one student information", QMessageBox.StandardButton.Ok)

    
    def check_customer_id(self, customer_id):

        result = self.db.search_info(customer_id = customer_id)
        return result
    
    def clear_form_info(self):
        self.vendor_id.clear()
        self.vendor_id.setEnabled(True)
        self.vendor_name.clear()
        self.phone_no.clear()
        self.street.clear()
        self.city.clear()
        self.state.clear()
        self.search_info()
    
    def disable_buttons(self):
        for button in self.buttons_list:
            button.setDisabled(True)

    def enable_buttons(self):
        for button in self.buttons_list:
            button.setDisabled(False)

class AdminSupplyPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = connectDatabase()

        self.MainWindow = QtWidgets.QMainWindow()
        self.adminsupply = AdminSupplyWindow()
        self.adminsupply.setupUi(self.MainWindow)
        self.MainWindow.show()

        self.supply_id = self.adminsupply.lineEdit
        # This will validate that input number is int
        self.supply_id.setValidator(QIntValidator())

        self.vendor_id = self.adminsupply.lineEdit_2
        self.vendor_id.setValidator(QIntValidator())

        self.product_id = self.adminsupply.lineEdit_3
        self.product_id.setValidator(QIntValidator())

        self.qty_supplied = self.adminsupply.lineEdit_4
        self.qty_supplied.setValidator(QIntValidator())

        self.date = self.adminsupply.lineEdit_5
        self.time = self.adminsupply.lineEdit_6
        self.cost_per_piece = self.adminsupply.lineEdit_7
        self.cost_per_piece.setValidator(QIntValidator())
        self.total_cost = self.adminsupply.lineEdit_8
        self.total_cost.setValidator(QIntValidator())
        self.margin_percentage = self.adminsupply.lineEdit_9
        self.margin_percentage.setValidator(QIntValidator())
        

        self.add_btn = self.adminsupply.addButton
        self.delete_btn = self.adminsupply.deleteButton
        self.select_btn = self.adminsupply.selectButton
        self.search_btn = self.adminsupply.searchButton
        self.clear_btn = self.adminsupply.clearButton

        self.result_table = self.adminsupply.tableWidget
        self.result_table.setSortingEnabled(False)
        self.buttons_list = self.adminsupply.function_frame.findChildren(QPushButton)
        # Initialize signal slot connection

        self.init_signal_slot()

        #populate initial data in the table and state/city dropdowns
        self.search_info()
    
    ## To Intialize button with signals
            
    def init_signal_slot(self):
        # Connect button to their respective functions
        self.add_btn.clicked.connect(self.add_new_supply_info)
        self.search_btn.clicked.connect(self.search_info)
        self.select_btn.clicked.connect(self.select_info)
        self.delete_btn.clicked.connect(self.delete_info)         
        self.clear_btn.clicked.connect(self.clear_form_info)            


    ## For ADMIN ANALYSIS OF CUSTOMERS


    def search_info(self):
        # function for searching and populate the student data
        # self.update_street_city_state()
        supply_info = self.get_supply_info()
        print(supply_info)

        supply_result = self.db.search_supply_info(
            supply_id = supply_info["supply_id"],
            vendor_id = supply_info["vendor_id"],
            product_id = supply_info["product_id"],
            date = supply_info["date"]
        )

        print(supply_result)
        self.show_data(supply_result)

    def select_info(self):
        
        select_row = self.result_table.currentRow()
        if select_row!=-1:
            self.supply_id.setEnabled(False)
            supply_id = self.result_table.item(select_row, 0).text().strip()
            vendor_id = self.result_table.item(select_row, 1).text().strip()
            product_id = self.result_table.item(select_row, 2).text().strip()
            qty_supplied = self.result_table.item(select_row, 3).text().strip()
            date =  self.result_table.item(select_row, 4).text().strip()
            time =  self.result_table.item(select_row, 5).text().strip()
            cost_per_piece =  self.result_table.item(select_row, 6).text().strip()
            total_cost =  self.result_table.item(select_row, 7).text().strip()
            margin_percentage =  self.result_table.item(select_row, 8).text().strip()

            self.supply_id.setText(supply_id)
            self.vendor_id.setText(vendor_id)
            self.product_id.setText(product_id)
            self.qty_supplied.setText(qty_supplied)
            self.date.setText(date)
            self.time.setText(time)
            self.cost_per_piece.setText(cost_per_piece)
            self.total_cost.setText(total_cost)
            self.margin_percentage.setText(margin_percentage)
        else:
            QMessageBox.information(self, "Warning", "Please select one student information", QMessageBox.StandardButton.Ok)
    
    def get_supply_info(self):
        #Function to retrive data from the form
        # print(supply_info)
        supply_id = self.supply_id.text().strip()
        vendor_id = self.vendor_id.text().strip()
        product_id = self.product_id.text().strip()
        qty_supplied = self.qty_supplied.text().strip()
        date = self.date.text().strip()
        time = self.time.text().strip()
        cost_per_piece = self.cost_per_piece.text().strip()
        total_cost = self.total_cost.text().strip()
        margin_percentage = self.margin_percentage.text().strip()


        ## add pincode information later when table in database is changed with extra column for pin code
        if supply_id.isdigit():
            supply_id = int(supply_id)
        if vendor_id.isdigit():
            vendor_id = int(vendor_id)
        if product_id.isdigit():
            product_id = int(product_id)
        if qty_supplied.isdigit():
            qty_supplied = int(qty_supplied)
        if cost_per_piece != "":
            cost_per_piece = float(cost_per_piece)
        if total_cost != "":
            total_cost = float(total_cost)
        if margin_percentage != "":
            margin_percentage = float(margin_percentage)

        supply_data = {
            "supply_id": supply_id,
            "vendor_id": vendor_id,
            "product_id" : product_id,
            "qty_supplied" : qty_supplied ,
            "date" : date,
            "time" : time,
            "cost_per_piece" : cost_per_piece,
            "total_cost" : total_cost,
            "margin_percentage" : margin_percentage
        } 
        print(supply_data)
        return supply_data
    
    def show_data(self, result):
        # Function to populate the table with student information
        if result:
            self.result_table.setRowCount(0)
            self.result_table.setRowCount(len(result))
            print(result)
            for row, info in enumerate(result):
                info_list = [
                    info["supply_id"],
                    info["vendor_id"],
                    info["product_id"],
                    info["qty_supplied"],
                    info["date"],
                    info["time"],
                    info["cost_per_piece"],
                    info["total_cost"],
                    info["margin_percentage"]
                ]

                for column,item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    self.result_table.setItem(row, column, cell_item)
        else:
            self.result_table.setRowCount(0)
            return 

    def delete_info(self):
        supply_info = self.get_supply_info()
        # print(supply_info)
        if supply_info["supply_id"]:
            delete_result = self.db.delete_supply_info(
                supply_id = supply_info["supply_id"]
            )
            QMessageBox.information(self, "Info", f"Item successfully deleted !!", QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.information(self, "Alert", f"Please select one supply", QMessageBox.StandardButton.Ok)
        
        self.supply_id.setEnabled(True)
        self.clear_form_info()
        self.search_info()


    def add_new_supply_info(self):
        self.disable_buttons()
        supply_info = self.get_supply_info()
        self.supply_id.setEnabled(False)
        print(supply_info)
        if supply_info["supply_id"]:
            QMessageBox.information(self, "Alert", f"Supply Id is automatically generated", QMessageBox.StandardButton.Ok)
        if supply_info["vendor_id"] == "" or supply_info["product_id"] == "" or supply_info["qty_supplied"] == "" or supply_info["cost_per_piece"] == "" or supply_info["margin_percentage"]=="" :
             ## Alert that some input fields are missing
            QMessageBox.information(self, "Missing Information", f"Please fill all mandatory fields", QMessageBox.StandardButton.Ok)
        else:
            add_result = self.db.add_supply_info(
                vendor_id = supply_info["vendor_id"],
                product_id = supply_info["product_id"],
                qty_supplied = supply_info["qty_supplied"],
                date = datetime.date.today(),    ## fill in current date
                time = datetime.datetime.now(), ## fill in current  time
                cost_per_piece = supply_info["cost_per_piece"],
                total_cost =  supply_info["cost_per_piece"]*supply_info["qty_supplied"],
                margin_percentage = supply_info["margin_percentage"]
            )
        self.enable_buttons()
        self.supply_id.setEnabled(True)
        self.search_info()
    
    def clear_form_info(self):
        self.supply_id.clear()
        self.supply_id.setEnabled(True)
        self.vendor_id.clear()
        self.product_id.clear()
        self.qty_supplied.clear()
        self.date.clear()
        self.time.clear()
        self.cost_per_piece.clear()
        self.total_cost.clear()
        self.margin_percentage.clear()
        self.search_info()
    
    def disable_buttons(self):
        for button in self.buttons_list:
            button.setDisabled(True)

    def enable_buttons(self):
        for button in self.buttons_list:
            button.setDisabled(False)

class Ui_ItemDetailsWindow(QtWidgets.QMainWindow):
    def __init__(self, pd_id, customer_details):
        super().__init__()
        self.db = connectDatabase()
        self.product_id = pd_id
        ## customer_details is a list of dictionaries which is returned by sql when self.con.cursor(dictionary = True)
        self.customer_details = customer_details[0]
        print(self.customer_details)
        self.fetch_product_details()

    def fetch_product_details(self):
        self.item_details = self.db.search_product_info(self.product_id)
        print(self.item_details)
        (self.product_name,self.product_price,self.product_url) = self.item_details[0]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 50, 611, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.imagelabel = QtWidgets.QLabel(self.frame)
        self.imagelabel.setGeometry(QtCore.QRect(40, 40, 91, 101))
        self.imagelabel.setPixmap(QtGui.QPixmap(self.product_url))
        self.imagelabel.setScaledContents(True)
        self.imagelabel.setObjectName("imagelabel")

        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(150, 50, 151, 61))
        self.widget.setObjectName("widget")

        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.titlelabel = QtWidgets.QLabel(self.widget)
        self.titlelabel.setScaledContents(True)
        self.titlelabel.setWordWrap(True)
        self.titlelabel.setText(self.product_name)
        self.titlelabel.setObjectName("product_name")

        self.gridLayout.addWidget(self.titlelabel, 0, 0, 1, 2)

        self.quantitylabel = QtWidgets.QLabel(self.widget)
        self.quantitylabel.setObjectName("quantitylabel")
        self.gridLayout.addWidget(self.quantitylabel, 1, 0, 1, 1)

        self.quantity_spinbox = QtWidgets.QSpinBox(self.widget)
        self.quantity_spinbox.setWrapping(True)
        self.quantity_spinbox.setObjectName("spinBox")
        self.quantity_spinbox.setRange(0,2147483647)
        self.quantity_spinbox.valueChanged.connect(self.calculate_total)
        self.gridLayout.addWidget(self.quantity_spinbox, 1, 1, 1, 1)

        self.pricelabel = QtWidgets.QLabel(self.frame)
        self.pricelabel.setGeometry(QtCore.QRect(320, 60, 55, 16))
        self.pricelabel.setWordWrap(True)
        self.pricelabel.setText("Rs. " + str(self.product_price))
        self.pricelabel.setObjectName("pricelabel")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 270, 221, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 270, 91, 20))
        self.label_5.setObjectName("label_5")

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(440, 240, 231, 131))
        self.widget1.setObjectName("widget1")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label_10 = QtWidgets.QLabel(self.widget1)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_11 = QtWidgets.QLabel(self.widget1)
        self.label_11.setWordWrap(True)
        self.label_11.setText(self.customer_details["first_name"] + " " + self.customer_details["last_name"])
        self.label_11.setObjectName("label_11")

        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setWordWrap(True)
        self.label_7.setText(self.customer_details["phone_no"])
        self.label_7.setObjectName("label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 1, 1, 1)

        self.label_8 = QtWidgets.QLabel(self.widget1)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_9 = QtWidgets.QLabel(self.widget1)
        self.label_9.setWordWrap(True)
        self.label_9.setText(self.customer_details["street"] + " " + self.customer_details["city"] + " " + self.customer_details["state"] + " , pincode - " + str(self.customer_details["pin_code"]))
        self.label_9.setObjectName("label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 1, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 410, 601, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda checked : self.order_product(MainWindow, self.comboBox.currentText(), self.customer_details, [self.product_id], [self.quantity_spinbox.value()], [self.product_price], self.quantity_spinbox.value()*self.product_price))

        MainWindow.setCentralWidget(self.centralwidget)

        
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        self.total_label = QtWidgets.QLabel(self.centralwidget)
        self.total_label.setGeometry(QtCore.QRect(70, 300, 120, 50))
        self.total_label.setWordWrap(True)
        self.total_label.setObjectName("label_5")
        
        # self.total_label.setGeometry(QtCore.QRect(70, 300, 91, 20))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def order_product(self, MainWindow, comboText, customer_details, p_id, qty, price, total):
        total_quantity = 0
        for i in qty:
            total_quantity+=i
        if total_quantity > 0:
            MainWindow.close()
            self.invoice_details_window = QtWidgets.QMainWindow()
            self.ui = Invoice_MainWindow(comboText, customer_details, p_id, qty, price,total)
            self.ui.setupUi(self.invoice_details_window)

            # self.ui.label.setText(f"Item Details for {item_name}")
            self.invoice_details_window.show()
        else:
            self.close()
            self.show_notification()
    def show_notification(self):
        dialog = PopupDialog("Cart is Empty !!", 'red_cross.jpg', self)
        dialog.exec_()   


    def calculate_total(self):
        quantity = self.quantity_spinbox.value()
        total_amount = quantity * self.product_price
        self.total_label.setText(f"Total Amount: {total_amount}")
        print(self.total_label.text())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.quantitylabel.setText(_translate("MainWindow", "Quantity"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Credit Card"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Debit Card"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Cash On Delivery"))
        self.comboBox.setItemText(3, _translate("MainWindow", "UPI"))
        self.label_5.setText(_translate("MainWindow", "Payment Options"))
        self.pushButton.setText(_translate("MainWindow", "PROCEED TO CHECKOUT"))
        self.label_10.setText(_translate("MainWindow", "Receipent\'s name"))
        self.label_6.setText(_translate("MainWindow", "Phone No"))
        self.label_8.setText(_translate("MainWindow", "Address"))


class Invoice_MainWindow(object):
    def __init__(self, comboText, myCustomer, product_id, quantity, price, total):
        self.notification_sound = QSound("notification.wav")
        self.notification_sound.play()
        self.db = connectDatabase()
        self.comboText = comboText
        self.product_id = product_id
        self.paymentMethod = comboText
        self.total = total
        self.quantity = quantity                ## this is a list
        self.price = price                      ## this is a list
        self.myCustomer = myCustomer
        self.order_date = datetime.date.today()
        self.order_time = datetime.datetime.now().time()
        self.transaction_id = self.generate_sha256(str(self.order_date) + str(self.order_time))
        self.delivery_date = self.order_date + datetime.timedelta(days=1)
        self.place_order()

    def place_order(self):
        # pass
        print(self.myCustomer)
        print(self.transaction_id)
        print(self.paymentMethod)
        print(self.total)
        print(self.order_date)
        print(self.order_time)
        print(self.delivery_date)
        self.db.add_order(self.myCustomer["customer_id"], self.paymentMethod, self.total, self.transaction_id, str(self.order_date), str(self.order_time), str(self.delivery_date), "Pending")
        order_details = self.db.search_order_info(transaction_id = self.transaction_id)
        print(order_details)
        self.order_id = order_details[0]["order_id"]

        print(self.product_id)
        print(self.price)
        print(self.quantity)
        for i in range(len(self.product_id)):
            self.db.add_order_details_info(self.order_id, self.product_id[i], self.quantity[i], self.price[i], self.price[i]*self.quantity[i])

        self.db.clearCart(self.myCustomer["customer_id"])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 706)
        MainWindow.setStyleSheet("background-color: white;")  # Set white background color
        
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
        
        labels = [
            "Order ID:", "Transaction ID:", "Payment Method:",
            "Recipient's Name:", "Order Date:", "Order Time:",
            "Delivery Status:", "Total:"
        ]
        
        values = [
            f"#{self.order_id}", self.transaction_id, self.comboText,
            f"{self.myCustomer['first_name']} {self.myCustomer['last_name']}",
            str(self.order_date), str(self.order_time),
            "Pending", str(self.total)
        ]

        for i, (label_text, value_text) in enumerate(zip(labels, values)):
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
        self.label.setText(_translate("MainWindow", "ORDER PLACED SUCCESSFULLY"))

    def generate_sha256(self, input_string):
        # Convert the input string to bytes
        input_bytes = input_string.encode('utf-8')

        # Generate the SHA-256 hash
        sha256_hash = hashlib.sha256(input_bytes).hexdigest()

        return sha256_hash


from PyQt5.QtWidgets import QToolButton, QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtCore import QSize, QTimer, Qt

class CustomToolButton(QToolButton):
    def __init__(self, icon_path, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon(icon_path))
        self.setIconSize(QSize(self.size().width(), self.size().height()))  # Set initial icon size to button size
        self.setStyleSheet("QToolButton { border: 2px solid black; background-color: white; }")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # Dynamically adjust the icon size based on the button size
        icon_size = min(self.width(), self.height()) * 0.8  # Set icon size to 80% of button size
        self.setIconSize(QSize(icon_size, icon_size))

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtCore import QTimer, Qt

class PopupDialog(QDialog):
    def __init__(self, message, icon_path, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Notification")
        self.setWindowFlag(Qt.FramelessWindowHint)  # Remove window frame
        self.setAttribute(Qt.WA_TranslucentBackground)  # Make window transparent
        self.setMinimumSize(200, 200)  # Set minimum size to create a square shape
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        
        # Add icon
        self.icon_label = QLabel()
        self.icon_label.setAlignment(Qt.AlignCenter)  # Align icon in the center
        pixmap = QPixmap(icon_path).scaledToHeight(225)  # Scale pixmap to desired height
        self.icon_label.setPixmap(pixmap)
        layout.addWidget(self.icon_label)
        
        # Add message
        self.message_label = QLabel(message)
        self.message_label.setStyleSheet("font-size: 14px; color: black;")
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setWordWrap(True)  # Enable text wrapping
        layout.addWidget(self.message_label)
        
        self.setLayout(layout)
        
        # Set background color and border
        self.setStyleSheet("background-color: white; border: 2px solid #4CAF50; border-radius: 10px;")

        ## Create a beep - sound after clicking desired Button
        self.notification_sound = QSound("notification.wav")
        self.notification_sound.play()
        
        # Close the dialog after 2 seconds
        QTimer.singleShot(1600, self.close)


class CartPage(QtWidgets.QMainWindow):
    def __init__(self, myCustomer):
        super().__init__()
        self.db = connectDatabase()
        self.customer_details = myCustomer[0]
        self.customer_id = self.customer_details["customer_id"]
        self.cart_items = self.db.get_cart_info(self.customer_id)
        self.qty_spin_boxes = []
        self.item_prices = []
        self.product_ids = []
        self.item_quantities = []
        print(self.cart_items)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #f0f0f0;")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMouseTracking(True)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("background-color: transparent;")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 40, 1222, 1222))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)

        initial_total = 0

        for customer_id, pd_id, item_name, quantity, item_rate, item_total, item_image in self.cart_items:
            frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            frame.setMinimumSize(QtCore.QSize(200, 200))
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setObjectName("frame")
            frame.setStyleSheet("background-color: #ffffff; border-radius: 10px;")

            item_photo = QtWidgets.QLabel(frame)
            item_photo.setGeometry(QtCore.QRect(20, 50, 111, 121))
            item_photo.setText("")
            item_photo.setPixmap(QtGui.QPixmap(item_image))
            item_photo.setScaledContents(True)
            item_photo.setObjectName(f"{item_name.lower()}_photo")

            item_title = QtWidgets.QLabel(frame)
            item_title.setGeometry(QtCore.QRect(150, 30, 131, 41))
            item_title.setObjectName(f"{item_name.lower()}_label")
            item_title.setText(item_name)
            item_title.setWordWrap(True)
            item_title.setStyleSheet("font-weight: bold; font-size: 14px;")

            item_price = QtWidgets.QLabel(frame)
            item_price.setGeometry(QtCore.QRect(150, 60, 131, 41))
            item_price.setObjectName(f"{item_name.lower()}_price_label")
            item_price.setText(f"Rs. {item_rate}")
            item_price.setWordWrap(True)
            item_price.setStyleSheet("font-weight: bold; font-size: 14px;")

            quantity_label = QtWidgets.QLabel(frame)
            quantity_label.setGeometry(QtCore.QRect(150, 90, 131, 41))
            quantity_label.setObjectName(f"{item_name.lower()}_Quantity_label")
            quantity_label.setText(f"Quantity: ")
            quantity_label.setWordWrap(True)
            quantity_label.setStyleSheet("font-weight: bold; font-size: 14px;")

            quantity_spinbox = QtWidgets.QSpinBox(frame)
            quantity_spinbox.setGeometry(QtCore.QRect(240, 90, 131, 41))
            quantity_spinbox.setWrapping(True)
            quantity_spinbox.setObjectName(f"{item_name.lower()}_spinBox")
            quantity_spinbox.setRange(0, 2147483647)
            quantity_spinbox.setValue(quantity)
            quantity_spinbox.setStyleSheet("""
                QSpinBox {
                    border: 1px solid black;
                }
            """)
            initial_total += item_total
            quantity_spinbox.valueChanged.connect(self.calculate_total)
            quantity_spinbox.valueChanged.connect(self.update_quantity_in_db)
            self.qty_spin_boxes.append(quantity_spinbox)
            self.item_prices.append(item_rate)
            self.product_ids.append(pd_id)
            self.item_quantities.append(quantity)
            self.verticalLayout_2.addWidget(frame)

        frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        frame.setMinimumSize(QtCore.QSize(200, 400))
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        frame.setObjectName("frame")
        frame.setStyleSheet("background-color: #ffffff; border-radius: 10px;")

        self.total_amount = initial_total

        self.total_label = QtWidgets.QLabel(frame)
        self.total_label.setGeometry(QtCore.QRect(70, 180, 300, 100))
        self.total_label.setWordWrap(True)
        self.total_label.setObjectName("total_label")
        self.total_label.setStyleSheet("font-weight: bold; font-size: 18px;")
        self.total_label.setText(f"Total : {initial_total}")
        self.verticalLayout_2.addWidget(frame)

        self.comboBox = QtWidgets.QComboBox(frame)
        self.comboBox.setGeometry(QtCore.QRect(170, 120, 221, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setStyleSheet("QComboBox { border: 1px solid black; }")

        self.label_5 = QtWidgets.QLabel(frame)
        self.label_5.setGeometry(QtCore.QRect(70, 120, 100, 70))
        self.label_5.setObjectName("label_5")
        self.label_5.setWordWrap(True)
        self.label_5.setAlignment(QtCore.Qt.AlignLeft)
        self.label_5.setStyleSheet("font-weight: bold; font-size: 12px;")

        self.widget1 = QtWidgets.QWidget(frame)
        self.widget1.setGeometry(QtCore.QRect(460, 100, 300, 131))
        self.widget1.setObjectName("widget1")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label_10 = QtWidgets.QLabel(self.widget1)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_10.setText("Customer Name:")
        self.label_10.setStyleSheet("font-weight: bold; font-size: 12px;")

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_11 = QtWidgets.QLabel(self.widget1)
        self.label_11.setWordWrap(True)
        self.label_11.setText(self.customer_details["first_name"] + " " + self.customer_details["last_name"])
        self.label_11.setObjectName("label_11")

        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_6.setText("Phone Number:")
        self.label_6.setStyleSheet("font-weight: bold; font-size: 12px;")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setWordWrap(True)
        self.label_7.setText(self.customer_details["phone_no"])
        self.label_7.setObjectName("label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 1, 1, 1)

        self.label_8 = QtWidgets.QLabel(self.widget1)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.label_8.setText("Address:")
        self.label_8.setStyleSheet("font-weight: bold; font-size: 12px;")

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_9 = QtWidgets.QLabel(self.widget1)
        self.label_9.setWordWrap(True)
        self.label_9.setText(self.customer_details["street"] + " " + self.customer_details["city"] + " " + self.customer_details["state"] + " , pincode - " + str(self.customer_details["pin_code"]))
        self.label_9.setObjectName("label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 1, 1, 1)

        self.pushButton = QtWidgets.QPushButton(frame)
        self.pushButton.setGeometry(QtCore.QRect(70, 300, 601, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Place Order")
        self.pushButton.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")
        self.pushButton.clicked.connect(lambda checked : self.order_product(MainWindow, self.comboBox.currentText(), self.customer_details, self.product_ids, self.item_quantities, self.item_prices, self.total_amount))

        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def order_product(self, MainWindow, comboText, customer_details, p_id, qty, price, total):
        MainWindow.close()
        total_quantity = 0
        lst = self.db.get_all_product()
        flag = 0
        fault_id = -1
        fault_stock = -1
        for i in range(len(p_id)):
            pd = p_id[i]
            q = qty[i]
            for dic in lst:
                if (dic["product_id"] == pd):
                    if (dic["qty"]<q):
                        flag = 1
                        fault_name = dic["name"]
                        fault_stock = dic["qty"]
                        total_quantity += q
                        break
                    else:
                        total_quantity += q
            if flag == 1:
                break
        
        if p_id:
            if total_quantity > 0 and flag == 0:
                self.invoice_details_window = QtWidgets.QMainWindow()
                self.ui = Invoice_MainWindow(comboText, customer_details, p_id, qty, price,total)
                self.ui.setupUi(self.invoice_details_window)

                # self.ui.label.setText(f"Item Details for {item_name}")
                self.invoice_details_window.show()
            elif total_quantity > 0 and flag == 1:
                self.show_notification(f"{fault_name} Available upto {fault_stock} units !!")
            else:
                ## if total_quantity is zero
                self.show_notification("Cart is Empty!!")
        else:
            ## show pop-up no item Added to cart
            self.show_notification("Cart is Empty!!")

    def show_notification(self, Message):
        dialog = PopupDialog(Message, 'red_cross.jpg', self)
        dialog.exec_()
    
    def update_quantity_in_db(self):
        index = 0
        for qty_boxes in self.qty_spin_boxes:
            qty = qty_boxes.value()
            self.item_quantities[index] = qty
            pd_id = self.product_ids[index]
            item_wise_total = qty*self.item_prices[index]
            self.db.update_cart(self.customer_id, pd_id, qty, item_wise_total)
            index += 1

    def calculate_total(self):
        self.total_amount = 0
        index = 0
        for i in self.qty_spin_boxes:
            quantity = i.value()
            self.total_amount += quantity*self.item_prices[index]
            index += 1

        self.total_label.setText(f"Total : {self.total_amount}")
        print(self.total_label.text())
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Receipent\'s name"))
        self.label_6.setText(_translate("MainWindow", "Phone No"))
        self.label_8.setText(_translate("MainWindow", "Address"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Credit Card"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Debit Card"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Cash On Delivery"))
        self.comboBox.setItemText(3, _translate("MainWindow", "UPI"))
        self.label_5.setText(_translate("MainWindow", "Payment Options"))
        self.pushButton.setText(_translate("MainWindow", "PROCEED TO CHECKOUT"))


class HomePage(QtWidgets.QMainWindow):
    def __init__(self, customer_details):
        super().__init__()
        self.db = connectDatabase()
        self.myCustomer = customer_details
        print(self.myCustomer)
        self.get_product_details()
    
    def get_product_details(self):
        product_details = self.db.get_all_product()
        self.items = []

        for row,info in enumerate(product_details):
            info_tuple = (
                info["product_id"],
                info["name"],
                info["category"],
                info["price"],
                info["rating"],
                info["qty"],
                info["description"],
                info["url"]
            )
            self.items.append(info_tuple)

    def setupUi(self, MainWindow, user = None):
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 40, 1222, 1222))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        # Add margins to the scroll area and its contents
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)  # Set margins
        
        for pd_id, item_name, item_category, item_rate, item_rating,item_stock,item_description,item_image in self.items:
            frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            frame.setMinimumSize(QtCore.QSize(200, 200))
            frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            frame.setFrameShadow(QtWidgets.QFrame.Raised)
            frame.setObjectName("frame")
            frame.setStyleSheet("background-color: 	#ffffff; border-radius: 10px;")  # White background and rounded corners

            # Add item photo
            item_photo = QtWidgets.QLabel(frame)
            item_photo.setGeometry(QtCore.QRect(20, 50, 111, 121))  # Adjusted position
            item_photo.setText("")
            item_photo.setPixmap(QtGui.QPixmap(item_image))
            item_photo.setScaledContents(True)
            item_photo.setObjectName(f"{item_name.lower()}_photo")

            # Add item label
            item_title = QtWidgets.QLabel(frame)
            item_title.setGeometry(QtCore.QRect(150, 30, 131, 41))  # Adjusted position
            item_title.setObjectName(f"{item_name.lower()}_label")
            item_title.setText(item_name)
            item_title.setWordWrap(True)  # Enable word wrapping
            item_title.setStyleSheet("font-weight: bold; font-size: 14px;")  # Bold text
            
            # Add item price 
            item_price = QtWidgets.QLabel(frame)
            item_price.setGeometry(QtCore.QRect(150, 60, 131, 41))  # Adjusted position
            item_price.setObjectName(f"{item_name.lower()}_label")
            item_price.setText(f"price: {item_rate}")
            item_price.setWordWrap(True)  # Enable word wrapping
            item_price.setStyleSheet("font-weight: bold; font-size: 14px;")  # Bold text


            # Add item description 
            item_desc = QtWidgets.QLabel(frame)
            item_desc.setGeometry(QtCore.QRect(290, 30, 400, 120))  # Adjusted position
            item_desc.setObjectName(f"{item_name.lower()}_label")
            item_desc.setText(f"{item_description}")
            item_desc.setWordWrap(True)  # Enable word wrapping
            item_desc.setStyleSheet("font-weight: bold; font-size: 14px;")  # Bold text

            # Add button for Add to cart
            item_addtocart = QtWidgets.QPushButton(frame)
            item_addtocart.setGeometry(QtCore.QRect(150, 100, 120, 28))  # Adjusted position
            item_addtocart.setObjectName(f"{item_name.lower()}_button")
            item_addtocart.setText("ADD TO CART")
            item_addtocart.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px;")  # Styled button
            item_addtocart.clicked.connect(lambda checked, id=pd_id: self.add_to_cart(self.myCustomer[0]["customer_id"], id))

            # Add buy now button
            item_buynow = QtWidgets.QPushButton(frame)
            item_buynow.setGeometry(QtCore.QRect(150, 140, 120, 28))  # Adjusted position
            item_buynow.setObjectName(f"{item_name.lower()}_button")
            item_buynow.setText("BUY NOW")
            item_buynow.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px;")  # Styled button
            item_buynow.clicked.connect(lambda checked, id=pd_id: self.show_item_details(id))
            
            self.verticalLayout_2.addWidget(frame)

        # Add basket icon on the top right corner
        basket_icon = CustomToolButton("basket_icon.jpg", self.centralwidget)
        basket_icon.setGeometry(QtCore.QRect(self.width() + 50, 20, 80, 80))  # Adjusted position and size
        basket_icon.setObjectName("basket_icon")
        basket_icon.setToolTip("View Basket")  # Tooltip for the icon

        self.setCentralWidget(self.centralwidget)
        basket_icon.clicked.connect(self.view_basket)  # Connect the clicked signal to view_basket method
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_to_cart(self,customer_id,product_id):

        cart_result = self.db.get_AllCart_info()
        current_quantity = 0
        price = 0
        flag = False
        for row,info in enumerate(cart_result):
            if info["customer_id"] == customer_id and info["product_id"] == product_id:
                current_quantity = info["quantity"]
                price = info["price"]
                flag = True
                break
        if flag:
            self.db.update_cart(customer_id, product_id, current_quantity+1, price*(current_quantity+1))
        else:
            (name, price, url) = self.db.search_product_info(product_id)[0]
            print(name)
            print(price)
            print(url)
            self.db.add_product_to_cart(customer_id, product_id, name, price, price, 1, url)  # Quantity is set to 1 by default tehrefore initially total is same as price of the 1 product
        
        self.show_notification()
    
    def show_notification(self):
        dialog = PopupDialog("Item added to cart", 'check_icon3.jpg', self)
        dialog.exec_()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    
    def show_item_details(self, pd_id):
        self.close()
        
        self.item_details_window = QtWidgets.QMainWindow()
        self.ui = Ui_ItemDetailsWindow(pd_id, self.myCustomer)
        self.ui.setupUi(self.item_details_window)

        # self.ui.label.setText(f"Item Details for {item_name}")
        self.item_details_window.show()

        
    def view_basket(self):
        # Implement the logic to show the basket contents here
        self.cart_details_window = QtWidgets.QMainWindow()
        self.ui = CartPage(self.myCustomer)
        self.ui.setupUi(self.cart_details_window)
        self.cart_details_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    login_window = LoginWindow()
    signup_window = SignupWindow()
    

    sys.exit(app.exec_())