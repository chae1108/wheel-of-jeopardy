from PyQt5 import QtGui, QtWidgets, QtCore
from ui.gameChoice import Ui_gameChoice
from module.gameAnswerWindow import GameAnswerWindow
from classes.Game import Game

class GameChoiceWindow(QtWidgets.QMainWindow, Ui_gameChoice):
    def __init__(self, game, parent):
        super(GameChoiceWindow, self).__init__(parent)
        self.setupUi(self, game)
        print(self.__class__)
        self.select.clicked.connect(self.selectToPlay)
        _translate = QtCore.QCoreApplication.translate
        self.select.clicked.connect(parent.updateUI)

    def selectToPlay(self):
        self.close()
        categoryChoice = self.selectCategory()
