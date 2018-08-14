from PyQt5 import QtGui, QtWidgets
from ui.categorySelect import Ui_categorySelect
from module.gameWindow import GameWindow
from PyQt5.QtWidgets import QAbstractItemView,QMessageBox

class CategorySelectWindow(QtWidgets.QMainWindow, Ui_categorySelect):

    # Changed the UI.
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
        if self.chosenList.count() == 12:        
            self.close()
            self.goToGame = GameWindow(parent=self)
            self.goToGame.show()
        else:
            option = QMessageBox.question(self, "Warning.", "You must select 12 categories to play.", QMessageBox.Ok)
            if(option == QMessageBox.Ok):
                pass