from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_gameAnswer(object):
    def setupUi(self, gameAnswer, data):
        self.data = data
        gameAnswer.setObjectName("gameAnswer")
        gameAnswer.setFixedSize(750, 400)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.categoryName = QtWidgets.QLabel(gameAnswer)
        self.categoryName.setAlignment(Qt.AlignCenter)
        self.categoryName.setGeometry(QtCore.QRect(0, 20, 750, 60))
        self.categoryName.setFont(font)
        self.categoryName.setObjectName("categoryName")
        font.setPointSize(12)
        self.value = QtWidgets.QLabel(gameAnswer)
        self.value.setAlignment(Qt.AlignCenter)
        self.value.setGeometry(QtCore.QRect(0, 50, 750, 60))
        self.value.setObjectName("value")
        self.question = QtWidgets.QLabel(gameAnswer)
        self.question.setAlignment(Qt.AlignCenter)
        self.question.setGeometry(QtCore.QRect(0, 80, 750, 120))
        self.question.setFont(font)
        self.question.setObjectName("question")
        self.answer = QtWidgets.QLabel(gameAnswer)
        self.answer.setAlignment(Qt.AlignCenter)
        self.answer.setGeometry(QtCore.QRect(300, 190, 180, 60))
        self.answer.setObjectName("answer")
        self.showAnswer = QtWidgets.QPushButton(gameAnswer)
        self.showAnswer.setGeometry(QtCore.QRect(150, 190, 140, 60))
        self.showAnswer.setObjectName("showAnswer")
        self.right = QtWidgets.QPushButton(gameAnswer)
        self.right.setGeometry(QtCore.QRect(200, 300, 140, 60))
        self.right.setObjectName("right")
        self.wrong = QtWidgets.QPushButton(gameAnswer)
        self.wrong.setGeometry(QtCore.QRect(390, 300, 140, 60))
        self.wrong.setObjectName("wrong")

        self.retranslateUi(gameAnswer)
        QtCore.QMetaObject.connectSlotsByName(gameAnswer)

    def retranslateUi(self, gameAnswer):
        _translate = QtCore.QCoreApplication.translate
        gameAnswer.setWindowTitle(_translate("gameAnswer", "Wheel of Jeopardy"))
        self.categoryName.setText(_translate("gameAnswer", self.data[0]))
        self.value.setText(_translate("gameAnswer", "$" + str(self.data[1])))
        self.question.setText(_translate("gameAnswer", self.data[2]))
        self.answer.setText(_translate("gameAnswer", "Answer"))
        self.showAnswer.setText(_translate("gameAnswer", "Show Answer"))
        self.right.setText(_translate("gameAnswer", "Right"))
        self.wrong.setText(_translate("gameAnswer", "Wrong"))

    def updateUI(self):
        _translate = QtCore.QCoreApplication.translate
        self.answer.setText(_translate("gameAnswer", self.data[3]))
