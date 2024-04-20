# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit

class LoginMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 604)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #FFFFFF;")
        self.centralwidget.setObjectName("centralwidget")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(220, 300, 150, 40))
        self.login_button.setStyleSheet("background-color: #4CAF50; color: white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("login_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_button.setIcon(icon)
        self.login_button.setObjectName("login_button")
        self.signup_button = QtWidgets.QPushButton(self.centralwidget)
        self.signup_button.setGeometry(QtCore.QRect(400, 300, 150, 40))
        self.signup_button.setStyleSheet("background-color: #2196F3; color: white;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("signup_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.signup_button.setIcon(icon1)
        self.signup_button.setObjectName("signup_button")
        self.login_info_widget = QtWidgets.QWidget(self.centralwidget)
        self.login_info_widget.setGeometry(QtCore.QRect(150, 120, 500, 150))
        self.login_info_widget.setObjectName("login_info_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.login_info_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.username_label = QtWidgets.QLabel(self.login_info_widget)
        self.username_label.setObjectName("username_label")
        self.verticalLayout.addWidget(self.username_label)
        self.username_lineEdit = QtWidgets.QLineEdit(self.login_info_widget)
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.verticalLayout.addWidget(self.username_lineEdit)
        self.password_label = QtWidgets.QLabel(self.login_info_widget)
        self.password_label.setObjectName("password_label")
        self.verticalLayout.addWidget(self.password_label)
        self.password_lineEdit = QtWidgets.QLineEdit(self.login_info_widget)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.password_lineEdit.setEchoMode(QLineEdit.Password)
        self.verticalLayout.addWidget(self.password_lineEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Window"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.signup_button.setText(_translate("MainWindow", "Signup"))
        self.username_label.setText(_translate("MainWindow", "Username/Phone"))
        self.password_label.setText(_translate("MainWindow", "Password"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())