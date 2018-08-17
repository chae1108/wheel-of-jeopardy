from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui.categoryDelete import Ui_categoryDelete
import os

class CategoryDeleteWindow(QtWidgets.QMainWindow, Ui_categoryDelete):
    def __init__(self, parent):
        super(CategoryDeleteWindow, self).__init__(parent)
        self.setupUi(self)
        self.remove.clicked.connect(self.goToDelete)
        self.cancel.clicked.connect(self.close)
        self.cancel.clicked.connect(parent.show)

    def goToDelete(self):
        ci = self.selectCategory()
        filename = os.path.join('db', ci[0] + '.csv')
        if os.path.exists(filename):

            option = QMessageBox.question(self, "Are you sure?",
                                               "Are you sure you want to delete '" + ci[0] + "'?",
                                               QMessageBox.Yes | QMessageBox.No)
            if option == QMessageBox.Yes:
                os.remove(filename)
                self.list.takeItem(ci[1])
            else:
                pass
