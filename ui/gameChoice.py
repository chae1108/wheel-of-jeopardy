# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/gameChoice.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_gameChoice(object):
    def setupUi(self, gameChoice):
        gameChoice.setObjectName("gameChoice")
        gameChoice.resize(400, 300)
        self.select = QtWidgets.QPushButton(gameChoice)
        self.select.setGeometry(QtCore.QRect(130, 210, 141, 61))
        self.select.setObjectName("select")
        self.list = QtWidgets.QListView(gameChoice)
        self.list.setGeometry(QtCore.QRect(90, 10, 256, 192))
        self.list.setObjectName("list")

        self.retranslateUi(gameChoice)
        QtCore.QMetaObject.connectSlotsByName(gameChoice)

    def retranslateUi(self, gameChoice):
        _translate = QtCore.QCoreApplication.translate
        gameChoice.setWindowTitle(_translate("gameChoice", "Form"))
        self.select.setText(_translate("gameChoice", "Select"))

