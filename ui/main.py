# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(1038, 719)
        self.title = QtWidgets.QTextEdit(main)
        self.title.setGeometry(QtCore.QRect(300, 40, 401, 51))
        self.title.setObjectName("title")
        self.newGame = QtWidgets.QPushButton(main)
        self.newGame.setGeometry(QtCore.QRect(360, 420, 311, 71))
        self.newGame.setObjectName("newGame")
        self.categories = QtWidgets.QPushButton(main)
        self.categories.setGeometry(QtCore.QRect(360, 500, 311, 71))
        self.categories.setObjectName("categories")

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Form"))
        self.title.setHtml(_translate("main", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Wheel of Jeopardy</span></p></body></html>"))
        self.newGame.setText(_translate("main", "New Game"))
        self.categories.setText(_translate("main", "Categories"))

