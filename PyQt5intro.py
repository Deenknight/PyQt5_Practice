import sys
from PyQt5 import QtWidgets, QtGui, QtCore #not necessary when you specifically do shit later but fuck you
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
""" 
# v0
# Display Basic Window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.resize(500,500)
window.move(0,0) # set starting window pos

# Setting window attributes
window.setWindowTitle("Fuck AirFryerPlus")
window.setWindowIcon(QtGui.QIcon("imgs\\comedy.jpeg.png"))

window.show() # always run at the end
sys.exit(app.exec_())
"""



"""
# v1 buttons and shit
app = QApplication(sys.argv)
window = QWidget()
window.resize(500,500)
window.move(0,0) # set starting window pos

# Setting window attributes
window.setWindowTitle("Fuck AirFryerPlus")
window.setWindowIcon(QIcon("imgs\\comedy.jpeg.png"))

# Adding buttons
layout = QtWidgets.QHBoxLayout() # auto layout in a box form
btn0 = QtWidgets.QPushButton("Hello World!")
layout.addWidget(btn0)
window.setLayout(layout)

# Setting text
btn1 = QPushButton()
btn1.setText("Goodbye")
layout.addWidget(btn1)

# Setting image with button
btn2 = QPushButton()
btn2.setIcon(QIcon("imgs\\comedy.jpeg.png"))
btn2.setShortcut('Ctrl+D')
layout.addWidget(btn2)

# Tool button with functionality
class ToolButton():
    def __init__(self, window=None):

        self.btn = QToolButton(window) #you don't need a layout to put it on the window
        self.btn.setArrowType(Qt.RightArrow)
        self.btn.setCheckable(True)
        self.btn.setChecked(False)
        self.btn.setAutoRaise(True)
        self.btn.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btn.clicked.connect(self.functionality)

    def functionality(self): # button functionality
        # Goes back and forth like a slider menu
        # I pity whoever has to figure out how to make it a smooth animation
        if self.btn.isChecked():
            print("Opened")
            self.btn.setArrowType(Qt.LeftArrow)
            self.btn.move(50, 0)
        else:
            print("Closed")
            self.btn.setArrowType(Qt.RightArrow)
            self.btn.move(0, 0)
       
        
btn3 = ToolButton(window)

window.show() # always run at the end
sys.exit(app.exec_())
"""



""" 
# v2 screen class as well as an edittable text box
class Screen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        width = 500
        height = 500

        self.setWindowTitle("Text On a Scren B)")
        self.resize(width, height)
        self.setWindowIcon(QIcon("imgs\\wey2apaf.bmp"))
        self.move(sizeObject.center()) # set starting window pos to be the center of the screen
        # starting pos is the top-left corner though, so this needs to be fixed

        self.textEdit = QtWidgets.QTextEdit()
        self.btnPress1 = QPushButton("Button 1")
        self.btnPress2 = QPushButton("Button 2")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        self.setLayout(layout)
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)

    def btnPress1_Clicked(self):
        self.textEdit.setPlainText("I love AirFryerPlus")

    def btnPress2_Clicked(self):
        self.textEdit.setHtml("<font color='red' size='6'><red>I hate AirFryerPlus</font>")

# Call-site
if __name__ == '__main__':
    app = QApplication(sys.argv)
    sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
    window = Screen()
    window.show() # always run at the end
    sys.exit(app.exec_()) 
"""


