# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/categoryMenu.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_categoryMenu(object):
    def setupUi(self, categoryMenu):
        categoryMenu.setObjectName("categoryMenu")
        categoryMenu.resize(1000, 700)
        self.title = QtWidgets.QTextEdit(categoryMenu)
        self.title.setGeometry(QtCore.QRect(300, 40, 401, 51))
        self.title.setObjectName("title")
        self.categoryEdit = QtWidgets.QPushButton(categoryMenu)
        self.categoryEdit.setGeometry(QtCore.QRect(360, 420, 311, 71))
        self.categoryEdit.setObjectName("categoryEdit")
        self.back = QtWidgets.QPushButton(categoryMenu)
        self.back.setGeometry(QtCore.QRect(360, 500, 311, 71))
        self.back.setObjectName("back")
        self.categoryDelete = QtWidgets.QPushButton(categoryMenu)
        self.categoryDelete.setGeometry(QtCore.QRect(360, 340, 311, 71))
        self.categoryDelete.setObjectName("categoryDelete")
        self.categoryAdd = QtWidgets.QPushButton(categoryMenu)
        self.categoryAdd.setGeometry(QtCore.QRect(360, 260, 311, 71))
        self.categoryAdd.setObjectName("categoryAdd")

        self.retranslateUi(categoryMenu)
        QtCore.QMetaObject.connectSlotsByName(categoryMenu)

    def retranslateUi(self, categoryMenu):
        _translate = QtCore.QCoreApplication.translate
        categoryMenu.setWindowTitle(_translate("categoryMenu", "Form"))
        self.title.setHtml(_translate("categoryMenu", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Wheel of Jeopardy</span></p></body></html>"))
        self.categoryEdit.setText(_translate("categoryMenu", "Edit Category"))
        self.back.setText(_translate("categoryMenu", "Back"))
        self.categoryDelete.setText(_translate("categoryMenu", "Delete Category"))
        self.categoryAdd.setText(_translate("categoryMenu", "Add Category"))

