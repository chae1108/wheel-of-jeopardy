from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView
import os

class Ui_categorySelect(object):

    # I've changed the GUIs around a bit.  They are no londer resizable.  I've added a WOJ logo.  The StandardItemModel
    # adds the categories to select from.
    def setupUi(self, categorySelect):
        categorySelect.setObjectName("categorySelect")
        categorySelect.setFixedSize(1000, 600)
        self.logo = QtWidgets.QLabel(categorySelect)
        self.logo.setGeometry(QtCore.QRect(75, 15, 1000, 100))
        self.logo.setPixmap(QtGui.QPixmap('WOJlogo.png'))
        self.logo.setObjectName("logo")

        self.availableList = QtWidgets.QListView(categorySelect)
        self.availableList.setGeometry(QtCore.QRect(150, 130, 300, 400))
        self.availableList.setObjectName("availableList")
        self.availableList.setEditTriggers(QAbstractItemView.NoEditTriggers)

        categories = self.getCategoryNames()

        self.availableModel = QtGui.QStandardItemModel()
        self.availableList.setModel(self.availableModel)
        for category in categories:
            item = QtGui.QStandardItem(category)
            self.availableModel.appendRow(item)

        self.chosenList = QtWidgets.QListView(categorySelect)
        self.chosenList.setGeometry(QtCore.QRect(550, 130, 300, 400))
        self.chosenList.setObjectName("chosenList")
        self.chosenModel = QtGui.QStandardItemModel()
        self.chosenList.setModel(self.chosenModel)

        self.startGame = QtWidgets.QPushButton(categorySelect)
        self.startGame.setGeometry(QtCore.QRect(150, 530, 300, 70))
        self.startGame.setObjectName("startGame")
        self.cancel = QtWidgets.QPushButton(categorySelect)
        self.cancel.setGeometry(QtCore.QRect(550, 530, 300, 70))
        self.cancel.setObjectName("cancel")

        self.moveToLeftColumn = QtWidgets.QPushButton(categorySelect)
        self.moveToLeftColumn.setGeometry(QtCore.QRect(475, 300, 50, 50))
        self.moveToLeftColumn.setObjectName("moveToLeft")

        self.moveToRightColumn = QtWidgets.QPushButton(categorySelect)
        self.moveToRightColumn.setGeometry(QtCore.QRect(475, 250, 50, 50))
        self.moveToRightColumn.setObjectName("moveToRight")

        self.retranslateUi(categorySelect)
        QtCore.QMetaObject.connectSlotsByName(categorySelect)

    def retranslateUi(self, categorySelect):
        _translate = QtCore.QCoreApplication.translate
        categorySelect.setWindowTitle(_translate("categorySelect", "Wheel of Jeopardy"))
        self.startGame.setText(_translate("categorySelect", "Start Game"))
        self.cancel.setText(_translate("categorySelect", "Cancel"))
        self.moveToLeftColumn.setText(_translate("categorySelect", "<<"))
        self.moveToRightColumn.setText(_translate("categorySelect", ">>"))

    # Removed the .csv extension from the filename
    def getCategoryNames(self):
        categoryNames = []
        fileNames = os.listdir("./db")
        for file in fileNames:
            if file[-4:] == ".csv":
                file = file[:-4]
                categoryNames.append(file)

        return categoryNames
