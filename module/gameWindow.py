from PyQt5 import QtGui, QtWidgets
from ui.game import Ui_game

class GameWindow(QtWidgets.QMainWindow, Ui_game):
    def __init__(self, parent):
        super(GameWindow, self).__init__(parent)
        self.setupUi(self)
        self.back.clicked.connect(self.close)
        self.back.clicked.connect(parent.show)
