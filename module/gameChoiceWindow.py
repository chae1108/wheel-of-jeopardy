from PyQt5 import QtGui, QtWidgets, QtCore
from ui.gameChoice import Ui_gameChoice
from classes.Game import Game

class GameChoiceWindow(QtWidgets.QDialog, Ui_gameChoice):

    def __init__(self, game, parent):
        super(GameChoiceWindow, self).__init__(parent)
        self.setupUi(self, game)
        self.select.clicked.connect(self.selectToPlay)

    def selectToPlay(self):
        self.close()
        self.categoryChoice = self.selectCategory() * 2