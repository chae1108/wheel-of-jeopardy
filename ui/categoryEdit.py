# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/categoryEdit.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_categoryEdit(object):
    def setupUi(self, categoryEdit):
        categoryEdit.setObjectName("categoryEdit")
        categoryEdit.resize(947, 681)
        self.title = QtWidgets.QTextEdit(categoryEdit)
        self.title.setGeometry(QtCore.QRect(290, 20, 401, 51))
        self.title.setObjectName("title")
        self.list = QtWidgets.QListView(categoryEdit)
        self.list.setGeometry(QtCore.QRect(190, 80, 581, 461))
        self.list.setObjectName("list")
        self.select = QtWidgets.QPushButton(categoryEdit)
        self.select.setGeometry(QtCore.QRect(180, 560, 241, 81))
        self.select.setObjectName("select")
        self.cancel = QtWidgets.QPushButton(categoryEdit)
        self.cancel.setGeometry(QtCore.QRect(460, 560, 241, 81))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(categoryEdit)
        QtCore.QMetaObject.connectSlotsByName(categoryEdit)

    def retranslateUi(self, categoryEdit):
        _translate = QtCore.QCoreApplication.translate
        categoryEdit.setWindowTitle(_translate("categoryEdit", "Form"))
        self.title.setHtml(_translate("categoryEdit", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Wheel of Jeopardy</span></p></body></html>"))
        self.select.setText(_translate("categoryEdit", "Select"))
        self.cancel.setText(_translate("categoryEdit", "Cancel"))

