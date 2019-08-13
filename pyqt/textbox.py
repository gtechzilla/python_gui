import sys
#imports our widgets
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        #to initialize the widget
        super().__init__()
        #setting the windows properties
        self.title = 'Kenyan_Wamlambez'
        self.left = 200
        self.top =100
        self.width = 400
        self.height = 200
        #initializethe window
        self.initUI()

    def initUI(self):
        #assigning the set windows properies
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        
        #create a textbox
        self.textbox1 = QLineEdit(self)
        #positon the textbox on the window
        self.textbox1.move(100,70)
        #give the text box width and height
        self.textbox1.resize(200,40)

        self.textbox = QLineEdit(self)
        self.textbox.move(100,120)
        self.textbox.resize(200,40)

        self.buttonLogin = QPushButton("Login",self)
        self.buttonLogin.move(150,170)
        self.buttonLogin.clicked.connect(self.onClick)
        #this function displays the window
        self.show()
    
    @pyqtSlot()
    def onClick(self):
        textbox1Value= self.textbox1.text()
        textboxValue= self.textbox.text()
        if textbox1Value == "Wamlambez" and textboxValue == "Wamnyonyez":
            print("You are Kenyan")

if __name__ == '__main__':
    #initialize the qt 
    app = QApplication(sys.argv)
    ex = App()
    #this runs the application till the user exits
    sys.exit(app.exec_())

