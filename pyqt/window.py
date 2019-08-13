import sys
#imports our widgets
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

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
        #this function displays the window
        self.show()

if __name__ == '__main__':
    #initialize the qt 
    app = QApplication(sys.argv)
    ex = App()
    #this runs the application till the user exits
    sys.exit(app.exec_())

