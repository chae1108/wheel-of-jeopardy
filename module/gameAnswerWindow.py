from PyQt5 import QtGui, QtWidgets, QtCore
from ui.game import Ui_game
from ui.gameAnswer import Ui_gameAnswer
from functools import partial

class GameAnswerWindow(QtWidgets.QMainWindow, Ui_gameAnswer):
    def __init__(self, data, parent):
        super(GameAnswerWindow, self).__init__(parent)
        print(parent.__class__)
        self.setupUi(self, data)
        self.showAnswer.clicked.connect(self.goToAnswer)
        self.right.clicked.connect(self.rightAnswer)
        self.wrong.clicked.connect(self.wrongAnswer)
        turn = parent.game.getTurn()
        self.right.clicked.connect(partial(parent.game.getPlayer(turn).updateRoundScore,self.data[1]))
        self.right.clicked.connect(parent.updateUI)
        self.wrong.clicked.connect(parent.updateUI)
        _translate = QtCore.QCoreApplication.translate

    def goToAnswer(self):
        self.updateUI()

    def rightAnswer(self):
        self.close()

    def wrongAnswer(self):
        self.close()
