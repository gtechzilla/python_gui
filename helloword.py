import sys
#imports the needed widgets
#a widget is anything that is diplayed on the window/screen
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        #to initialize the widget
        super().__init__()
        #setting the windows properties
        self.title = 'Helloworld App'
        self.left = 200
        self.top =100
        self.width = 400
        self.height = 200
        #initialize the window from the intUI method
        self.initUI()

    def initUI(self):
        #assigning the set windows properies
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        #using the Qlabel widget to display the given text on the screen
        self.label = QLabel("HelloWorld",self)
        #positioning the text
        self.label.move(60,80)

        #this function displays the window
        self.show()

if __name__ == '__main__':
    #initialize the qt 
    app = QApplication(sys.argv)
    ex = App()
    #this runs the application till the user exits
    sys.exit(app.exec_())

