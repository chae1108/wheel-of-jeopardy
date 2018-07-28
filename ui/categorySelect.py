# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/categorySelect.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_categorySelect(object):
    def setupUi(self, categorySelect):
        categorySelect.setObjectName("categorySelect")
        categorySelect.resize(947, 681)
        self.title = QtWidgets.QTextEdit(categorySelect)
        self.title.setGeometry(QtCore.QRect(290, 20, 401, 51))
        self.title.setObjectName("title")
        self.availableList = QtWidgets.QListView(categorySelect)
        self.availableList.setGeometry(QtCore.QRect(80, 80, 341, 461))
        self.availableList.setObjectName("availableList")
        self.startGame = QtWidgets.QPushButton(categorySelect)
        self.startGame.setGeometry(QtCore.QRect(180, 560, 241, 81))
        self.startGame.setObjectName("startGame")
        self.cancel = QtWidgets.QPushButton(categorySelect)
        self.cancel.setGeometry(QtCore.QRect(460, 560, 241, 81))
        self.cancel.setObjectName("cancel")
        self.chosenList = QtWidgets.QListView(categorySelect)
        self.chosenList.setGeometry(QtCore.QRect(480, 80, 341, 461))
        self.chosenList.setObjectName("chosenList")

        self.retranslateUi(categorySelect)
        QtCore.QMetaObject.connectSlotsByName(categorySelect)

    def retranslateUi(self, categorySelect):
        _translate = QtCore.QCoreApplication.translate
        categorySelect.setWindowTitle(_translate("categorySelect", "Form"))
        self.title.setHtml(_translate("categorySelect", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Wheel of Jeopardy</span></p></body></html>"))
        self.startGame.setText(_translate("categorySelect", "Start Game"))
        self.cancel.setText(_translate("categorySelect", "Cancel"))

