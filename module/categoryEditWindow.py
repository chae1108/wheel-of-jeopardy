from PyQt5 import QtGui, QtWidgets
from ui.categoryEdit import Ui_categoryEdit
from module.categoryEditFormWindow import CategoryEditFormWindow

class CategoryEditWindow(QtWidgets.QMainWindow, Ui_categoryEdit):

    def __init__(self, parent):
        super(CategoryEditWindow, self).__init__(parent)
        self.setupUi(self)
        self.select.clicked.connect(self.goToEditForm)
        self.cancel.clicked.connect(self.close)
        self.cancel.clicked.connect(parent.show)

    def goToEditForm(self):
        self.close()
        category = self.selectCategory()
        self.goToEditForm = CategoryEditFormWindow(category, parent=self)
        self.goToEditForm.show()