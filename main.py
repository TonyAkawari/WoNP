from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import *

import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):       
        super(MainWindow,self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://wheelofnames.com"))
        self.setCentralWidget(self.browser)
        self.show()
        self.initUI()
        
    # New implementation to tidy up a little bit    
    def initUI(self):
        
        # Customizable primary size of the app. The app itself is responsive by default so change it up!
        self.setGeometry(100, 100, 900, 700)
        self.setWindowTitle("Wheel of Names Portable")
        
        # Not working properly. Need some help with this one. Icon shows up on folder but not title of the window.
        self.setWindowIcon(QIcon('wheel.ico'))  
        
app = QApplication(sys.argv)
window = MainWindow()

app.exec_()