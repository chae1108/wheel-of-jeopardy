from PyQt5 import QtGui, QtWidgets
from ui.categoryDelete import Ui_categoryDelete

class CategoryDeleteWindow(QtWidgets.QMainWindow, Ui_categoryDelete):
    def __init__(self, parent):
        super(CategoryDeleteWindow, self).__init__(parent)
        self.setupUi(self)
        self.cancel.clicked.connect(self.close)
        self.cancel.clicked.connect(parent.show)
