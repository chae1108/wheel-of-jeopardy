from PyQt5 import QtCore, QtGui, QtWidgets
from ui.game import Ui_game
from classes.Game import Game
import module.gameChoiceWindow

from module.gameChoiceWindow import GameChoiceWindow
from ui.gameChoice import Ui_gameChoice

class GameWindow(QtWidgets.QMainWindow, Ui_game):

    def __init__(self, parent):
        super(GameWindow, self).__init__(parent)
        self.setupUi(self)

        # These are test categories.  Once we can select the categories, this will be replaced with those.
        cat0 = ["cat0", "c0q0", "c0a0", "c0q1", "c0a1", "c0q2", "c0a2", "c0q3", "c0a3", "c0q4", "c0a5"]
        cat1 = ["cat1", "c1q0", "c1a0", "c1q1", "c1a1", "c1q2", "c1a2", "c1q3", "c1a3", "c1q4", "c1a4"]
        cat2 = ["cat2", "c2q0", "c2a0", "c2q1", "c2a1", "c2q2", "c2a2", "c2q3", "c2a3", "c2q4", "c2a4"]
        cat3 = ["cat3", "c3q0", "c3a0", "c3q1", "c3a1", "c3q2", "c3a2", "c3q3", "c3a3", "c3q4", "c3a4"]
        cat4 = ["cat4", "c4q0", "c4a0", "c4q1", "c4a1", "c4q2", "c4a2", "c4q3", "c4a3", "c4q4", "c4a4"]
        cat5 = ["cat5", "c5q0", "c5a0", "c5q1", "c5a1", "c5q2", "c5a2", "c5q3", "c5a3", "c5q4", "c5a4"]
        categories = [cat0, cat1, cat2, cat3, cat4, cat5]
        self.game = Game(categories)
        self.updateUI()

        self.runGame()
        self.back.clicked.connect(self.close)
        self.back.clicked.connect(parent.show)

    def runGame(self):
        self.spinner.clicked.connect(self.spinWheel)

    def spinWheel(self):
        spin = self.game.spinWheel()

        # Need to select a category
        if spin == 7 or spin == 9:
            self.goToGameChoice = GameChoiceWindow(parent=self)
            self.goToGameChoice.show()
            #spin = categoryChoice

        self.game.playTurn(spin)
        self.updateUI()

    def updateUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.round.setText(_translate("game", "Round: " + str(self.game.getRound())))
        self.spins.setText(_translate("game", "Spins: " + str(self.game.getSpins())))
        self.contestant1.setText(_translate("game", "Contestant 1: $" + str(self.game.getPlayer(0).getTotalScore())))
        self.contestant2.setText(_translate("game", "Contestant 2: $" + str(self.game.getPlayer(1).getTotalScore())))
        self.contestant3.setText(_translate("game", "Contestant 3: $" + str(self.game.getPlayer(2).getTotalScore())))
