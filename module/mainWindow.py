from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui.main import Ui_main
from module.gameWindow import GameWindow
from module.categoryMenuWindow import CategoryMenuWindow
from module.categorySelectWindow import CategorySelectWindow

class MainWindow(QtWidgets.QMainWindow, Ui_main):

    # Added a close window button
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.newGame.clicked.connect(self.goToSelectCategory)
        self.categories.clicked.connect(self.goToCategoryMenu)
        self.quit.clicked.connect(self.closeWindow)

    def goToSelectCategory(self):
        self.close()
        self.goToSelectCategory = CategorySelectWindow(parent=self)
        self.goToSelectCategory.show()

    def goToCategoryMenu(self):
        self.close()
        self.goToCategoryMenu = CategoryMenuWindow(parent=self)
        self.goToCategoryMenu.show()

    def closeWindow(self):
        option = QMessageBox.question(self, "Quit Game", "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No)
        if(option == QMessageBox.Yes):
            self.close()
        else:
            pass