from PyQt5 import QtGui, QtWidgets, QtCore
from ui.gameChoice import Ui_gameChoice
from module.gameAnswerWindow import GameAnswerWindow
from classes.Game import Game
from functools import partial

class GameChoiceWindow(QtWidgets.QMainWindow, Ui_gameChoice):
    def __init__(self, game, parent):
        super(GameChoiceWindow, self).__init__(parent)
        self.setupUi(self, game)
        self.select.clicked.connect(partial(self.selectToPlay,parent))
        _translate = QtCore.QCoreApplication.translate
        self.select.clicked.connect(parent.updateUI)

    def selectToPlay(self,parent):
        self.close()
        print(self.list.currentRow())
        data = self.game.playCategory(self.list.currentRow()*2)
        print(data)
        if not(data[0] == ""):
            self.goToGameAnswer = GameAnswerWindow(data, parent=parent)
            self.goToGameAnswer.show()