from PyQt5 import QtGui, QtWidgets
from ui.main import Ui_main
from module.gameWindow import GameWindow
from module.categoryMenuWindow import CategoryMenuWindow

class MainWindow(QtWidgets.QMainWindow, Ui_main):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.newGame.clicked.connect(self.goToGame)
        self.categories.clicked.connect(self.goToCategoryMenu)

    def goToGame(self):
        self.close()
        self.goToGame = GameWindow(parent=self)
        self.goToGame.show()

    def goToCategoryMenu(self):
        self.close()
        self.goToCategoryMenu = CategoryMenuWindow(parent=self)
        self.goToCategoryMenu.show()