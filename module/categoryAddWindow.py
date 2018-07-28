from PyQt5 import QtGui, QtWidgets
from ui.categoryAdd import Ui_categoryAdd

class CategoryAddWindow(QtWidgets.QMainWindow, Ui_categoryAdd):
    def __init__(self, parent):
        super(CategoryAddWindow, self).__init__(parent)
        self.setupUi(self)
        self.cancel.clicked.connect(self.close)
        self.cancel.clicked.connect(parent.show)
