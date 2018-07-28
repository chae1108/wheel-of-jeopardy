from PyQt5 import QtGui, QtWidgets
from ui.categoryMenu import Ui_categoryMenu
from module.categoryAddWindow import CategoryAddWindow
from module.categoryEditWindow import CategoryEditWindow
from module.categoryDeleteWindow import CategoryDeleteWindow

class CategoryMenuWindow(QtWidgets.QMainWindow, Ui_categoryMenu):
    def __init__(self, parent):
        super(CategoryMenuWindow, self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.categoryAdd.clicked.connect(self.goToCategoryAdd)
        self.categoryEdit.clicked.connect(self.goToCategoryEdit)
        self.categoryDelete.clicked.connect(self.goToCategoryDelete)
        self.back.clicked.connect(self.close)
        self.back.clicked.connect(self.parent.show)

    def goToCategoryAdd(self):
        self.close()
        self.goToCategoryAdd = CategoryAddWindow(parent=self)
        self.goToCategoryAdd.show()

    def goToCategoryEdit(self):
        self.close()
        self.goToCategoryEdit = CategoryEditWindow(parent=self)
        self.goToCategoryEdit.show()

    def goToCategoryDelete(self):
        self.close()
        self.goToCategoryDelete = CategoryDeleteWindow(parent=self)
        self.goToCategoryDelete.show()
