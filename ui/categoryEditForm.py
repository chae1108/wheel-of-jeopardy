# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/categoryEditForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_categoryAdd(object):
    def setupUi(self, categoryAdd):
        categoryAdd.setObjectName("categoryAdd")
        categoryAdd.resize(1000, 700)
        self.title = QtWidgets.QTextEdit(categoryAdd)
        self.title.setGeometry(QtCore.QRect(300, 10, 401, 51))
        self.title.setObjectName("title")
        self.category = QtWidgets.QLineEdit(categoryAdd)
        self.category.setGeometry(QtCore.QRect(280, 80, 621, 41))
        self.category.setObjectName("category")
        self.category_label = QtWidgets.QLabel(categoryAdd)
        self.category_label.setGeometry(QtCore.QRect(100, 80, 171, 41))
        self.category_label.setObjectName("category_label")
        self.question1 = QtWidgets.QLineEdit(categoryAdd)
        self.question1.setGeometry(QtCore.QRect(280, 130, 621, 41))
        self.question1.setObjectName("question1")
        self.q1_label = QtWidgets.QLabel(categoryAdd)
        self.q1_label.setGeometry(QtCore.QRect(100, 130, 171, 41))
        self.q1_label.setObjectName("q1_label")
        self.answer1 = QtWidgets.QLineEdit(categoryAdd)
        self.answer1.setGeometry(QtCore.QRect(280, 180, 621, 41))
        self.answer1.setText("")
        self.answer1.setObjectName("answer1")
        self.a1_label = QtWidgets.QLabel(categoryAdd)
        self.a1_label.setGeometry(QtCore.QRect(100, 180, 171, 41))
        self.a1_label.setObjectName("a1_label")
        self.question2 = QtWidgets.QLineEdit(categoryAdd)
        self.question2.setGeometry(QtCore.QRect(280, 230, 621, 41))
        self.question2.setObjectName("question2")
        self.answer2 = QtWidgets.QLineEdit(categoryAdd)
        self.answer2.setGeometry(QtCore.QRect(280, 280, 621, 41))
        self.answer2.setText("")
        self.answer2.setObjectName("answer2")
        self.a2_label = QtWidgets.QLabel(categoryAdd)
        self.a2_label.setGeometry(QtCore.QRect(100, 280, 171, 41))
        self.a2_label.setObjectName("a2_label")
        self.q2_label = QtWidgets.QLabel(categoryAdd)
        self.q2_label.setGeometry(QtCore.QRect(100, 230, 171, 41))
        self.q2_label.setObjectName("q2_label")
        self.question3 = QtWidgets.QLineEdit(categoryAdd)
        self.question3.setGeometry(QtCore.QRect(280, 330, 621, 41))
        self.question3.setObjectName("question3")
        self.answer3 = QtWidgets.QLineEdit(categoryAdd)
        self.answer3.setGeometry(QtCore.QRect(280, 380, 621, 41))
        self.answer3.setText("")
        self.answer3.setObjectName("answer3")
        self.a3_label = QtWidgets.QLabel(categoryAdd)
        self.a3_label.setGeometry(QtCore.QRect(100, 380, 171, 41))
        self.a3_label.setObjectName("a3_label")
        self.q3_label = QtWidgets.QLabel(categoryAdd)
        self.q3_label.setGeometry(QtCore.QRect(100, 330, 171, 41))
        self.q3_label.setObjectName("q3_label")
        self.question4 = QtWidgets.QLineEdit(categoryAdd)
        self.question4.setGeometry(QtCore.QRect(280, 430, 621, 41))
        self.question4.setObjectName("question4")
        self.answer4 = QtWidgets.QLineEdit(categoryAdd)
        self.answer4.setGeometry(QtCore.QRect(280, 480, 621, 41))
        self.answer4.setText("")
        self.answer4.setObjectName("answer4")
        self.a4_label = QtWidgets.QLabel(categoryAdd)
        self.a4_label.setGeometry(QtCore.QRect(100, 480, 171, 41))
        self.a4_label.setObjectName("a4_label")
        self.q4_label = QtWidgets.QLabel(categoryAdd)
        self.q4_label.setGeometry(QtCore.QRect(100, 430, 171, 41))
        self.q4_label.setObjectName("q4_label")
        self.question5 = QtWidgets.QLineEdit(categoryAdd)
        self.question5.setGeometry(QtCore.QRect(280, 530, 621, 41))
        self.question5.setObjectName("question5")
        self.answer5 = QtWidgets.QLineEdit(categoryAdd)
        self.answer5.setGeometry(QtCore.QRect(280, 580, 621, 41))
        self.answer5.setText("")
        self.answer5.setObjectName("answer5")
        self.a5_label = QtWidgets.QLabel(categoryAdd)
        self.a5_label.setGeometry(QtCore.QRect(100, 580, 171, 41))
        self.a5_label.setObjectName("a5_label")
        self.q5_label = QtWidgets.QLabel(categoryAdd)
        self.q5_label.setGeometry(QtCore.QRect(100, 530, 171, 41))
        self.q5_label.setObjectName("q5_label")
        self.save = QtWidgets.QPushButton(categoryAdd)
        self.save.setGeometry(QtCore.QRect(260, 633, 211, 51))
        self.save.setObjectName("save")
        self.cancel = QtWidgets.QPushButton(categoryAdd)
        self.cancel.setGeometry(QtCore.QRect(510, 630, 211, 51))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(categoryAdd)
        QtCore.QMetaObject.connectSlotsByName(categoryAdd)

    def retranslateUi(self, categoryAdd):
        _translate = QtCore.QCoreApplication.translate
        categoryAdd.setWindowTitle(_translate("categoryAdd", "Form"))
        self.title.setHtml(_translate("categoryAdd", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Wheel of Jeopardy</span></p></body></html>"))
        self.category_label.setText(_translate("categoryAdd", "Category Name"))
        self.q1_label.setText(_translate("categoryAdd", "Question #1"))
        self.a1_label.setText(_translate("categoryAdd", "Answer #1"))
        self.a2_label.setText(_translate("categoryAdd", "Answer #2"))
        self.q2_label.setText(_translate("categoryAdd", "Question #2"))
        self.a3_label.setText(_translate("categoryAdd", "Answer #3"))
        self.q3_label.setText(_translate("categoryAdd", "Question #3"))
        self.a4_label.setText(_translate("categoryAdd", "Answer #4"))
        self.q4_label.setText(_translate("categoryAdd", "Question #4"))
        self.a5_label.setText(_translate("categoryAdd", "Answer #5"))
        self.q5_label.setText(_translate("categoryAdd", "Question #5"))
        self.save.setText(_translate("categoryAdd", "Save"))
        self.cancel.setText(_translate("categoryAdd", "Cancel"))
