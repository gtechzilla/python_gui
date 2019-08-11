import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

'''
when a button or widget is clicked ,a signal is sent,we then capture the
signal for that specific widget in a slot.We can then use the slot to do 
our processing or perform some task
'''

class App(QWidget):

    def __init__(self):
        #to initialize the widget
        super().__init__()
        #setting the windows properties
        self.title = 'My First Window'
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

        #adding our button
        button=QPushButton("Click",self)
        button.move(100,70)
        #capture the signal when clicked and call the onClick function
        button.clicked.connect(self.onClick)

        button1=QPushButton("click 2",self)
        button1.move(100,90)
        button1.clicked.connect(self.onClick2)


        #this function displays the window
        self.show()
    
    #creating a slot that call the onClick funtion for button
    @pyqtSlot()
    def onClick(Self):
        print('Button click')
    
    #slot for our second button
    @pyqtSlot()
    def onClick2(self):
        print('Button2 clicked')



if __name__ == '__main__':
    #initialize the qt 
    app = QApplication(sys.argv)
    ex = App()
    #this runs the application till the user exits
    sys.exit(app.exec_())

