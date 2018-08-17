from PyQt5 import QtGui, QtWidgets
from ui.gameChoice import Ui_gameChoice
from module.gameAnswerWindow import GameAnswerWindow
from classes.Game import Game

class GameChoiceWindow(QtWidgets.QMainWindow, Ui_gameChoice):
    def __init__(self, game, parent):
        super(GameChoiceWindow, self).__init__(parent)
        self.setupUi(self, game)
        self.select.clicked.connect(self.selectToPlay)

    def selectToPlay(self):
        self.close()
        categoryChoice = self.selectCategory()
