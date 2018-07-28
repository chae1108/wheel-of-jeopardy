from PyQt5 import QtGui, QtWidgets
from ui.game import Ui_game

class GameAnswerWindow(QtWidgets.QMainWindow, Ui_gameAnswer):
    def __init__(self, parent):
        super(GameAnswerWindow, self).__init__(parent)
        self.setupUi(self)