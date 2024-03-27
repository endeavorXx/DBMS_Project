# from PyQt5.QtCore import Qt
import database as db
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
   def __init__(self):
      super(MyWindow, self).__init__()
      self.initUI()
      xpos = 200
      ypos = 200
      width = 300
      height = 300
      self.setGeometry(xpos, ypos, width, height)
      self.setWindowTitle("New window")

   ## all the stuff I want ot place in my window will be inside this initUI function
   def initUI(self):
      self.label = QtWidgets.QLabel(self)
      self.label.setText("my first label")
      self.label.move(50,50)

      self.b1 = QtWidgets.QPushButton(self)
      self.b1.setText("Click Me!!")
      self.b1.clicked.connect(self.clicked)
   
   def clicked(self):
      self.label.setText("you pressed the button")
      self.update()

   def update(self):
      self.label.adjustSize()



def window():
   app = QApplication(sys.argv)
   win = MyWindow()                          # This can also be done using Qwidgets
   win.show()
   sys.exit(app.exec_())

window()