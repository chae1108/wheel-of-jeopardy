from PyQt5 import QtCore, QtGui, QtWidgets
from ui.game import Ui_game
from classes.Game import Game
from module.gameChoiceWindow import GameChoiceWindow
from module.gameAnswerWindow import GameAnswerWindow
from ui.gameChoice import Ui_gameChoice
from ui.gameAnswer import Ui_gameAnswer
from PyQt5.QtWidgets import QMessageBox
import os
import csv

class GameWindow(QtWidgets.QMainWindow, Ui_game):

    def __init__(self, categoriesSelected, parent):
        super(GameWindow, self).__init__(parent)
        self.categories = self.getCategories(categoriesSelected)
        self.setupUi(self, self.categories)
        self.game = Game(self.categories)
        self.spin = ""

        self.updateUI()

        self.spinner.clicked.connect(self.spinWheel)
        self.back.clicked.connect(self.close)
        self.back.clicked.connect(parent.show)

    def getCategories(self, categoriesSelected):
        categories = []
        for cat in range(categoriesSelected.count()-1):
            category = self.__getCategory(categoriesSelected.item(cat).text())
            categories.append(category)

        return categories

    def __getCategory(self, cat):
        filename = os.path.join('db', cat + '.csv')
        try:
            with open(filename, "r") as csvfile:
                rowReader = csv.reader(csvfile, delimiter='|')
                for row in rowReader:
                    return row
        except:
            message = QMessageBox.question(self, "Error",
                                           "File does not exist",
                                           QMessageBox.Ok)
            if (message == QMessageBox.Ok):
                self.close()
            else:
                pass

    def spinWheel(self):
        self.spin = self.game.spinWheel()

        # Opens the Game Choice but needs to get the selected category
        if self.spin == 7 or self.spin == 9:
            self.goToGameChoice = GameChoiceWindow(self.game, parent=self)
            self.goToGameChoice.show()

        # Once it has a category or if the category is spun, brings up the Game Answer window.  Should determine if
        # player answered correctly and adject accordingly.
        elif self.spin == 0 or self.spin == 2 or self.spin == 4 or self.spin == 6 or self.spin == 8 or self.spin == 10:
            data = self.game.playCategory(self.spin)
            if not(data[0] == ""):
                self.goToGameAnswer = GameAnswerWindow(data, parent=self)
                self.goToGameAnswer.show()
                self.game.playTurn(self.spin)
            else:
                message = QMessageBox.information(self,"Spin Again", "Spin Again. All questions in this category has been answered.")
        else:
            self.game.playTurn(self.spin)


        if (self.game.getSpins() == 0):
            message = QMessageBox.information(self,"End of Round", "The Round has ended.")
            self.categories[0:5]=self.categories[6:11]
            self.game.nextRound(self.categories[0:5])
            #self.game.getPlayer(0).addRoundScoreToTotal()
            #self.game.getPlayer(1).addRoundScoreToTotal()
            #self.game.getPlayer(2).addRoundScoreToTotal()

        self.updateUI()