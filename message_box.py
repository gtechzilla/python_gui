import sys
#imports our message box widget
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        #to initialize the widget
        super().__init__()
        #setting the windows properties
        self.title = 'Message box Window'
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

        button = QPushButton("Pay",self)
        button.move(100,70)
        button.clicked.connect(self.onClick)
        #this function displays the window
        self.show()
    
    @pyqtSlot()
    def onClick(self):
        #outputs message box when clicked
        buttonReply = QMessageBox.question(self,'Validate Payment',"Confirm Payment?",QMessageBox.Ok | QMessageBox.Cancel ,QMessageBox.Cancel)
        if buttonReply == QMessageBox.Ok :
            print('Payment Confirmed')
        else:
            print('Payment Cancelled')

if __name__ == '__main__':
    #initialize the qt 
    app = QApplication(sys.argv)
    ex = App()
    #this runs the application till the user exits
    sys.exit(app.exec_())

