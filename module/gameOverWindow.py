from PyQt5 import QtGui, QtWidgets, QtCore
from ui.gameOver import Ui_gameOver

class GameOverWindow(QtWidgets.QDialog, Ui_gameOver):

    def __init__(self, winner, score, parent):
        super(GameOverWindow, self).__init__(parent)
        self.setupUi(self, winner, score)