from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_gameOver(object):
    def setupUi(self, gameOver, winner, score):
        gameOver.setObjectName("gameOver")
        gameOver.setFixedSize(300, 175)
        self.winner = QtWidgets.QLabel(gameOver)
        self.winner.setAlignment(Qt.AlignCenter)
        self.winner.setGeometry(QtCore.QRect(0, 20, 300, 60))
        self.winner.setObjectName("winner")
        self.winner.setText("The winner is Contestant " + str(winner+1) + " with $" + str(score))