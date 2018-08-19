from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtWidgets import QMessageBox
from classes.Game import Game

class Ui_gameChoice(object):

    def setupUi(self, gameChoice, game):
        self.game = game
        gameChoice.setObjectName("gameChoice")
        gameChoice.setFixedSize(400, 300)
        self.select = QtWidgets.QPushButton(gameChoice)
        self.select.setGeometry(QtCore.QRect(130, 210, 141, 61))
        self.select.setObjectName("select")
        self.list = QtWidgets.QListWidget(gameChoice)
        self.list.setGeometry(QtCore.QRect(90, 10, 256, 192))
        self.list.setObjectName("list")
        self.list.setEditTriggers(QAbstractItemView.NoEditTriggers)

        categories = self.getCategoryNames()
        for category in categories:
            item = QtWidgets.QListWidgetItem(category)
            self.list.addItem(item.text())

        self.retranslateUi(gameChoice)
        QtCore.QMetaObject.connectSlotsByName(gameChoice)

    def retranslateUi(self, gameChoice):
        _translate = QtCore.QCoreApplication.translate
        gameChoice.setWindowTitle(_translate("gameChoice", "Choose a Category"))
        self.select.setText(_translate("gameChoice", "Select"))

    def getCategoryNames(self):
        categoryNames = []

        for category in self.game.getBoard().getCategories():
            available = category.isAvailable()
            if available:
                name = category.getName()
                categoryNames.append(name)
            else:
                categoryNames.append("<No question left>")

        return categoryNames

    def selectCategory(self):
        try:
            spin = self.list.currentRow()
            return spin
        except:
            message = QMessageBox.question(self, "Error",
                                           "Please select a category.",
                                           QMessageBox.Ok)
            if (message == QMessageBox.Ok):
                pass