# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/categoryDelete.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_categoryDelete(object):
    def setupUi(self, categoryDelete):
        categoryDelete.setObjectName("categoryDelete")
        categoryDelete.resize(947, 681)
        self.title = QtWidgets.QTextEdit(categoryDelete)
        self.title.setGeometry(QtCore.QRect(290, 20, 401, 51))
        self.title.setObjectName("title")
        self.list = QtWidgets.QListView(categoryDelete)
        self.list.setGeometry(QtCore.QRect(190, 80, 581, 461))
        self.list.setObjectName("list")
        self.remove = QtWidgets.QPushButton(categoryDelete)
        self.remove.setGeometry(QtCore.QRect(180, 560, 241, 81))
        self.remove.setObjectName("remove")
        self.cancel = QtWidgets.QPushButton(categoryDelete)
        self.cancel.setGeometry(QtCore.QRect(460, 560, 241, 81))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(categoryDelete)
        QtCore.QMetaObject.connectSlotsByName(categoryDelete)

    def retranslateUi(self, categoryDelete):
        _translate = QtCore.QCoreApplication.translate
        categoryDelete.setWindowTitle(_translate("categoryDelete", "Form"))
        self.title.setHtml(_translate("categoryDelete", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Wheel of Jeopardy</span></p></body></html>"))
        self.remove.setText(_translate("categoryDelete", "Delete"))
        self.cancel.setText(_translate("categoryDelete", "Cancel"))

