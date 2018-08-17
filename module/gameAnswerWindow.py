from PyQt5 import QtGui, QtWidgets
from ui.game import Ui_game
from ui.gameAnswer import Ui_gameAnswer

class GameAnswerWindow(QtWidgets.QMainWindow, Ui_gameAnswer):
    def __init__(self, data, parent):
        super(GameAnswerWindow, self).__init__(parent)
        self.setupUi(self, data)
        self.showAnswer.clicked.connect(self.goToAnswer)
        self.right.clicked.connect(self.rightAnswer)
        self.wrong.clicked.connect(self.wrongAnswer)

    def goToAnswer(self):
        self.updateUI()

    def rightAnswer(self):
        self.close()

    def wrongAnswer(self):
        self.close()
