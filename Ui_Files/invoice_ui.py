# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Asus\Desktop\DBMS Project\Ui_Files\invoice.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 621, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 10, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setGeometry(QtCore.QRect(10, 90, 641, 411))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(10, 20, 10, 20)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget1)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget1)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.widget1)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget1)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget1)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget1)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 5, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget1)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget1)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 6, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget1)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget1)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 7, 1, 1, 1)
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
        self.label_2.setText(_translate("MainWindow", "ORDER ID"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TRANSACTION ID"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "PAYMENT METHOD"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "RECEIPENT\'S NAME"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "ORDER DATE"))
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "ORDER TIME"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "DELIVERY STATUS"))
        self.label_16.setText(_translate("MainWindow", "PENDING"))
        self.label_9.setText(_translate("MainWindow", "TOTAL"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
