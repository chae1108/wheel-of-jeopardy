# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/gameAnswer.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_gameAnswer(object):
    def setupUi(self, gameAnswer):
        gameAnswer.setObjectName("gameAnswer")
        gameAnswer.resize(758, 417)
        self.categoryName = QtWidgets.QLabel(gameAnswer)
        self.categoryName.setGeometry(QtCore.QRect(270, 40, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.categoryName.setFont(font)
        self.categoryName.setObjectName("categoryName")
        self.question = QtWidgets.QLabel(gameAnswer)
        self.question.setGeometry(QtCore.QRect(280, 110, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.question.setFont(font)
        self.question.setObjectName("question")
        self.showAnswer = QtWidgets.QPushButton(gameAnswer)
        self.showAnswer.setGeometry(QtCore.QRect(120, 183, 141, 61))
        self.showAnswer.setObjectName("showAnswer")
        self.right = QtWidgets.QPushButton(gameAnswer)
        self.right.setGeometry(QtCore.QRect(200, 300, 141, 61))
        self.right.setObjectName("right")
        self.wrong = QtWidgets.QPushButton(gameAnswer)
        self.wrong.setGeometry(QtCore.QRect(390, 300, 141, 61))
        self.wrong.setObjectName("wrong")
        self.answer = QtWidgets.QLabel(gameAnswer)
        self.answer.setGeometry(QtCore.QRect(310, 180, 181, 61))
        self.answer.setObjectName("answer")

        self.retranslateUi(gameAnswer)
        QtCore.QMetaObject.connectSlotsByName(gameAnswer)

    def retranslateUi(self, gameAnswer):
        _translate = QtCore.QCoreApplication.translate
        gameAnswer.setWindowTitle(_translate("gameAnswer", "Form"))
        self.categoryName.setText(_translate("gameAnswer", "Category Name"))
        self.question.setText(_translate("gameAnswer", "Question"))
        self.showAnswer.setText(_translate("gameAnswer", "Show Answer"))
        self.right.setText(_translate("gameAnswer", "Right"))
        self.wrong.setText(_translate("gameAnswer", "Wrong"))
        self.answer.setText(_translate("gameAnswer", "Answer"))

