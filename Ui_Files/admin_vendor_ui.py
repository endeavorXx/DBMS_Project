# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Asus\Desktop\DBMS Project\Ui_Files\admin_vendor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1019, 855)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(90, 20, 901, 71))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.title_label = QtWidgets.QLabel(self.frame)
        self.title_label.setGeometry(QtCore.QRect(30, 0, 841, 61))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.info_frame = QtWidgets.QFrame(self.centralwidget)
        self.info_frame.setGeometry(QtCore.QRect(90, 110, 911, 191))
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")
        self.layoutWidget = QtWidgets.QWidget(self.info_frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 891, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setContentsMargins(30, 20, 30, 20)
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 2, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.function_frame = QtWidgets.QFrame(self.centralwidget)
        self.function_frame.setGeometry(QtCore.QRect(80, 310, 921, 52))
        self.function_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.function_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.function_frame.setObjectName("function_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.function_frame)
        self.horizontalLayout.setContentsMargins(30, 10, 30, 10)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(self.function_frame)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.updateButton = QtWidgets.QPushButton(self.function_frame)
        self.updateButton.setObjectName("updateButton")
        self.horizontalLayout.addWidget(self.updateButton)
        self.selectButton = QtWidgets.QPushButton(self.function_frame)
        self.selectButton.setObjectName("selectButton")
        self.horizontalLayout.addWidget(self.selectButton)
        self.searchButton = QtWidgets.QPushButton(self.function_frame)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.clearButton = QtWidgets.QPushButton(self.function_frame)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        self.result_frame = QtWidgets.QFrame(self.centralwidget)
        self.result_frame.setGeometry(QtCore.QRect(80, 380, 911, 441))
        self.result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_frame.setObjectName("result_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.result_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.result_frame)
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1019, 26))
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
        self.title_label.setText(_translate("MainWindow", "admin informaton system"))
        self.label_2.setText(_translate("MainWindow", "Vendor Id"))
        self.label_3.setText(_translate("MainWindow", "Vendor Name "))
        self.label_4.setText(_translate("MainWindow", "street"))
        self.label_6.setText(_translate("MainWindow", "city"))
        self.label_8.setText(_translate("MainWindow", "state"))
        self.label_7.setText(_translate("MainWindow", "Phone_no"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.updateButton.setText(_translate("MainWindow", "Update"))
        self.selectButton.setText(_translate("MainWindow", "Select"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Vendor_Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vendor_name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "street"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "city"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "state"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "phone_no"))
