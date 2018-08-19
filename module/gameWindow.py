from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from ui.game import Ui_game
from classes.Game import Game
from module.gameChoiceWindow import GameChoiceWindow
from module.gameAnswerWindow import GameAnswerWindow
from module.gameOverWindow import GameOverWindow
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
        for cat in categoriesSelected:
            category = self.__getCategory(cat)
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
            self.goToGameChoice.exec_()
            self.spin = self.goToGameChoice.categoryChoice

        # Once it has a category or if the category is spun, brings up the Game Answer window.  Should determine if
        # player answered correctly and adject accordingly.
        if self.spin == 0 or self.spin == 2 or self.spin == 4 or self.spin == 6 or self.spin == 8 or self.spin == 10:
            data = self.game.playCategory(self.spin)
            if not(data[0] == ""):
                self.goToGameAnswer = GameAnswerWindow(data, parent=self)
                self.goToGameAnswer.exec_()
                answerCorrect = self.goToGameAnswer.answerCorrect

                questionValue = data[1]
                if answerCorrect:
                    self.game.playerAnswersCorrect(questionValue)
                else:
                    self.game.playerAnswersIncorrect(questionValue)
        else:
            self.game.playTurn(self.spin)

        gameOver = self.game.isGameOver()
        if gameOver:
            self.updateUI()
            winner = self.game.getWinner()
            score = self.game.getPlayer(winner).getTotalScore()
            goToGaveOver = GameOverWindow(winner, score, parent=self)
            goToGaveOver.exec_()

        self.updateUI()