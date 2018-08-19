from PyQt5 import QtGui, QtWidgets, QtCore
from ui.gameChoice import Ui_gameChoice
from classes.Game import Game
from functools import partial
from PyQt5.QtWidgets import QMessageBox
from module.gameAnswerWindow import GameAnswerWindow

class GameChoiceWindow(QtWidgets.QDialog, Ui_gameChoice):

    def __init__(self, game, parent):
        modal = True
        super(GameChoiceWindow, self).__init__(parent)
        self.setupUi(self, game)
        self.select.clicked.connect(partial(self.selectToPlay,parent))
        _translate = QtCore.QCoreApplication.translate
        self.select.clicked.connect(parent.updateUI)

    def selectToPlay(self,parent):
        self.close()
        data = self.game.playCategory(self.list.currentRow()*2)
        if not(data[0] == ""):
            self.goToGameAnswer = GameAnswerWindow(data, parent=parent)
            self.goToGameAnswer.show()
            parent.game.playTurn(parent.spin)  
        else:
            message = QMessageBox.information(parent,"Spin Again", "Spin Again. All questions in this category has been answered.")
