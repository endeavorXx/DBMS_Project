# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cart.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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
        self.titlelabel.setObjectName("titlelabel")
        self.gridLayout.addWidget(self.titlelabel, 0, 0, 1, 2)
        self.quantitylabel = QtWidgets.QLabel(self.widget)
        self.quantitylabel.setObjectName("quantitylabel")
        self.gridLayout.addWidget(self.quantitylabel, 1, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setWrapping(True)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 1, 1, 1, 1)
        self.pricelabel = QtWidgets.QLabel(self.frame)
        self.pricelabel.setGeometry(QtCore.QRect(320, 60, 55, 16))
        self.pricelabel.setWordWrap(True)
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 410, 601, 41))
        self.pushButton.setObjectName("pushButton")
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
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget1)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget1)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget1)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 26))
        self.menubar.setObjectName("menubar")
        self.menume = QtWidgets.QMenu(self.menubar)
        self.menume.setObjectName("menume")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menume.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.imagelabel.setText(_translate("MainWindow", "image"))
        self.titlelabel.setText(_translate("MainWindow", "title"))
        self.quantitylabel.setText(_translate("MainWindow", "Quantity"))
        self.pricelabel.setText(_translate("MainWindow", "price"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Credit Card"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Debit Card"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Cash On Delivery"))
        self.comboBox.setItemText(3, _translate("MainWindow", "UPI"))
        self.label_5.setText(_translate("MainWindow", "Payment Options"))
        self.pushButton.setText(_translate("MainWindow", "PROCEED TO CHECKOUT"))
        self.label_10.setText(_translate("MainWindow", "Receipent\'s name"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Phone No"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "Address"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.menume.setTitle(_translate("MainWindow", "me"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
