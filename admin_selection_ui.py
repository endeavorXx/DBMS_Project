# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Asus\Desktop\DBMS Project\admin_selection.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class SelectOption(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Dashboard Button
        self.dashboard_btn = QtWidgets.QPushButton(self.centralwidget)
        self.dashboard_btn.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Asus\\Desktop\\DBMS Project\\icons/dashboard-5-xxl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dashboard_btn.setIcon(icon)
        self.dashboard_btn.setIconSize(QtCore.QSize(14, 14))
        self.dashboard_btn.setAutoExclusive(True)
        self.dashboard_btn.setObjectName("dashboard_btn")
        self.dashboard_btn.setVisible(False)
        self.verticalLayout.addWidget(self.dashboard_btn)

        # Customer Button
        self.customer_btn = QtWidgets.QPushButton(self.centralwidget)
        self.customer_btn.setMouseTracking(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Asus\\Desktop\\DBMS Project\\icons/conference-xl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.customer_btn.setIcon(icon1)
        self.customer_btn.setIconSize(QtCore.QSize(14, 14))
        self.customer_btn.setAutoRepeat(True)
        self.customer_btn.setObjectName("customer_btn")
        self.verticalLayout.addWidget(self.customer_btn)

        # Product Button
        self.product_btn = QtWidgets.QPushButton(self.centralwidget)
        self.product_btn.setMouseTracking(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\Asus\\Desktop\\DBMS Project\\icons/product-xl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.product_btn.setIcon(icon2)
        self.product_btn.setIconSize(QtCore.QSize(14, 14))
        self.product_btn.setAutoExclusive(True)
        self.product_btn.setObjectName("product_btn")
        self.product_btn.setVisible(True)
        self.verticalLayout.addWidget(self.product_btn)

        # Order Button
        self.order_btn = QtWidgets.QPushButton(self.centralwidget)
        self.order_btn.setMouseTracking(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\Asus\\Desktop\\DBMS Project\\icons/notepad-xl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.order_btn.setIcon(icon3)
        self.order_btn.setIconSize(QtCore.QSize(14, 14))
        self.order_btn.setAutoExclusive(True)
        self.order_btn.setObjectName("order_btn")
        self.verticalLayout.addWidget(self.order_btn)

        # Supplies Button
        self.supplies_btn = QtWidgets.QPushButton(self.centralwidget)
        self.supplies_btn.setMouseTracking(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\Asus\\Desktop\\DBMS Project\\icons/truck-xxl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.supplies_btn.setIcon(icon4)
        self.supplies_btn.setIconSize(QtCore.QSize(14, 14))
        self.supplies_btn.setAutoExclusive(True)
        self.supplies_btn.setObjectName("supplies_btn")
        self.supplies_btn.setVisible(True)
        self.verticalLayout.addWidget(self.supplies_btn)

        # Vendors Button
        self.vendors_btn = QtWidgets.QPushButton(self.centralwidget)
        self.vendors_btn.setMouseTracking(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("c:\\Users\\Asus\\Desktop\\DBMS Project\\icons/vendor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vendors_btn.setIcon(icon5)
        self.vendors_btn.setIconSize(QtCore.QSize(14, 14))
        self.vendors_btn.setAutoExclusive(True)
        self.vendors_btn.setObjectName("vendors_btn")
        self.vendors_btn.setVisible(True)
        self.verticalLayout.addWidget(self.vendors_btn)

        # Spacer
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        # Exit Button
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setMouseTracking(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("c:\\Users\\Asus\\Desktop\\DBMS Project\\icons/close-window-xl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon6)
        self.exit_btn.setIconSize(QtCore.QSize(14, 14))
        self.exit_btn.setAutoExclusive(True)
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayout_2.addWidget(self.exit_btn)

        # Final setup
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dashboard_btn.setText(_translate("MainWindow", "Dashboard"))
        self.customer_btn.setText(_translate("MainWindow", "Customer"))
        self.product_btn.setText(_translate("MainWindow", "Product"))
        self.order_btn.setText(_translate("MainWindow", "Orders"))
        self.supplies_btn.setText(_translate("MainWindow", "Supplies"))
        self.vendors_btn.setText(_translate("MainWindow", "Vendors"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
