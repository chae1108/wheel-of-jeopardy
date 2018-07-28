from PyQt5 import QtGui, QtWidgets
from ui.categorySelect import Ui_categorySelect

class CategorySelectWindow(QtWidgets.QMainWindow, Ui_categorySelect):
    def __init__(self, parent):
        super(CategorySelectWindow, self).__init__(parent)
        self.setupUi(self)
        self.cancel.clicked.connect(self.close)
        self.cancel.clicked.connect(parent.show)
