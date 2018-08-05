from PyQt5 import QtGui, QtWidgets
from ui.categoryEdit import Ui_categoryEdit

class CategoryEditWindow(QtWidgets.QMainWindow, Ui_categoryEdit):
    def __init__(self, parent):
        super(CategoryEditWindow, self).__init__(parent)
        self.setupUi(self)
        self.cancel.clicked.connect(self.close)
        self.cancel.clicked.connect(parent.show)        
