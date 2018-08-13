from PyQt5 import QtGui, QtWidgets
from ui.categorySelect import Ui_categorySelect
from module.gameWindow import GameWindow
from PyQt5.QtWidgets import QAbstractItemView

class CategorySelectWindow(QtWidgets.QMainWindow, Ui_categorySelect):

    # Changed the UI.  Need to ensure there are 12 categories selected in the right field before moving onto the game
    def __init__(self, parent):
        super(CategorySelectWindow, self).__init__(parent)
        self.setupUi(self)
        self.startGame.clicked.connect(self.goToGame)
        self.cancel.clicked.connect(self.close)
        self.cancel.clicked.connect(parent.show)
        self.moveToRightColumn.clicked.connect(self.moveToRight)
        self.moveToLeftColumn.clicked.connect(self.moveToLeft)

    # Moves to the game window
    def goToGame(self):
        self.close()
        self.goToGame = GameWindow(parent=self)
        self.goToGame.show()

    # INCOMPLETE!!!! Need to figure out how to select an item and get it's index/value
    # moves the selected category over to the right field
    def moveToRight(self):
        self.availableModel.removeRow(0)
        item = QtGui.QStandardItem("cat8")
        self.chosenModel.appendRow(item)
        print("Move right")

    # INCOMPLETE!!!! This is the reverse of moveToRight
    def moveToLeft(self):
        self.chosenModel.removeRow(0)
