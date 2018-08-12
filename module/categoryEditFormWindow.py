from PyQt5 import QtGui, QtWidgets
from ui.categoryEdit import Ui_categoryEdit

class CategoryEditFormWindow(QtWidgets.QMainWindow, Ui_categoryEditForm):
    def __init__(self, parent):
        super(CategoryEditFormWindow, self).__init__(parent)
        self.setupUi(self)      
        self.cancel.clicked.connect(self.close)
        self.cancel.clicked.connect(parent.show)
