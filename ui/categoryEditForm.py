from PyQt5 import QtCore, QtGui, QtWidgets
import os
import csv

class Ui_categoryEditForm(object):

    def setupUi(self, categoryEditForm, category):
        categoryEditForm.setObjectName("categoryEditForm")
        categoryEditForm.setFixedSize(950, 525)
        self.logo = QtWidgets.QLabel(categoryEditForm)
        self.logo.setGeometry(QtCore.QRect(50, 15, 1000, 100))
        self.logo.setPixmap(QtGui.QPixmap('WOJlogo.png'))
        self.logo.setObjectName("logo")

        self.category = QtWidgets.QLineEdit(categoryEditForm)
        self.category.setGeometry(QtCore.QRect(250, 120, 640, 25))
        self.category.setObjectName("category")
        self.category_label = QtWidgets.QLabel(categoryEditForm)
        self.category_label.setGeometry(QtCore.QRect(100, 120, 150, 25))
        self.category_label.setObjectName("category_label")

        self.question1 = QtWidgets.QLineEdit(categoryEditForm)
        self.question1.setGeometry(QtCore.QRect(250, 150, 640, 25))
        self.question1.setObjectName("question1")
        self.q1_label = QtWidgets.QLabel(categoryEditForm)
        self.q1_label.setGeometry(QtCore.QRect(100, 150, 150, 25))
        self.q1_label.setObjectName("q1_label")
        self.answer1 = QtWidgets.QLineEdit(categoryEditForm)
        self.answer1.setGeometry(QtCore.QRect(250, 180, 640, 25))
        self.answer1.setObjectName("answer1")
        self.a1_label = QtWidgets.QLabel(categoryEditForm)
        self.a1_label.setGeometry(QtCore.QRect(100, 180, 150, 25))
        self.a1_label.setObjectName("a1_label")

        self.question2 = QtWidgets.QLineEdit(categoryEditForm)
        self.question2.setGeometry(QtCore.QRect(250, 210, 640, 25))
        self.question2.setObjectName("question2")
        self.q2_label = QtWidgets.QLabel(categoryEditForm)
        self.q2_label.setGeometry(QtCore.QRect(100, 210, 150, 25))
        self.q2_label.setObjectName("q2_label")
        self.answer2 = QtWidgets.QLineEdit(categoryEditForm)
        self.answer2.setGeometry(QtCore.QRect(250, 240, 640, 25))
        self.answer2.setObjectName("answer2")
        self.a2_label = QtWidgets.QLabel(categoryEditForm)
        self.a2_label.setGeometry(QtCore.QRect(100, 240, 150, 25))
        self.a2_label.setObjectName("a2_label")

        self.question3 = QtWidgets.QLineEdit(categoryEditForm)
        self.question3.setGeometry(QtCore.QRect(250, 270, 640, 25))
        self.question3.setObjectName("question3")
        self.q3_label = QtWidgets.QLabel(categoryEditForm)
        self.q3_label.setGeometry(QtCore.QRect(100, 270, 150, 25))
        self.q3_label.setObjectName("q3_label")
        self.answer3 = QtWidgets.QLineEdit(categoryEditForm)
        self.answer3.setGeometry(QtCore.QRect(250, 300, 640, 25))
        self.answer3.setObjectName("answer3")
        self.a3_label = QtWidgets.QLabel(categoryEditForm)
        self.a3_label.setGeometry(QtCore.QRect(100, 300, 150, 25))
        self.a3_label.setObjectName("a3_label")

        self.question4 = QtWidgets.QLineEdit(categoryEditForm)
        self.question4.setGeometry(QtCore.QRect(250, 330, 640, 25))
        self.question4.setObjectName("question4")
        self.q4_label = QtWidgets.QLabel(categoryEditForm)
        self.q4_label.setGeometry(QtCore.QRect(100, 330, 150, 25))
        self.q4_label.setObjectName("q4_label")
        self.answer4 = QtWidgets.QLineEdit(categoryEditForm)
        self.answer4.setGeometry(QtCore.QRect(250, 360, 640, 25))
        self.answer4.setObjectName("answer4")
        self.a4_label = QtWidgets.QLabel(categoryEditForm)
        self.a4_label.setGeometry(QtCore.QRect(100, 360, 150, 25))
        self.a4_label.setObjectName("a4_label")

        self.question5 = QtWidgets.QLineEdit(categoryEditForm)
        self.question5.setGeometry(QtCore.QRect(250, 390, 640, 25))
        self.question5.setObjectName("question5")
        self.q5_label = QtWidgets.QLabel(categoryEditForm)
        self.q5_label.setGeometry(QtCore.QRect(100, 390, 150, 25))
        self.q5_label.setObjectName("q5_label")
        self.answer5 = QtWidgets.QLineEdit(categoryEditForm)
        self.answer5.setGeometry(QtCore.QRect(250, 420, 640, 25))
        self.answer5.setObjectName("answer5")
        self.a5_label = QtWidgets.QLabel(categoryEditForm)
        self.a5_label.setGeometry(QtCore.QRect(100, 420, 150, 25))
        self.a5_label.setObjectName("a5_label")

        self.save = QtWidgets.QPushButton(categoryEditForm)
        self.save.setGeometry(QtCore.QRect(260, 460, 211, 51))
        self.save.setObjectName("save")
        self.cancel = QtWidgets.QPushButton(categoryEditForm)
        self.cancel.setGeometry(QtCore.QRect(510, 460, 211, 51))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(categoryEditForm, category)
        QtCore.QMetaObject.connectSlotsByName(categoryEditForm)

    def retranslateUi(self, categoryEditForm, category):
        _translate = QtCore.QCoreApplication.translate
        categoryEditForm.setWindowTitle(_translate("categoryEditForm", "Edit Category"))
        catFull = self.__getFullCategory(category)
        self.category_label.setText(_translate("categoryEditForm", "Category Name"))
        self.q1_label.setText(_translate("categoryEditForm", "Question #1"))
        self.a1_label.setText(_translate("categoryEditForm", "Answer #1"))
        self.a2_label.setText(_translate("categoryEditForm", "Answer #2"))
        self.q2_label.setText(_translate("categoryEditForm", "Question #2"))
        self.a3_label.setText(_translate("categoryEditForm", "Answer #3"))
        self.q3_label.setText(_translate("categoryEditForm", "Question #3"))
        self.a4_label.setText(_translate("categoryEditForm", "Answer #4"))
        self.q4_label.setText(_translate("categoryEditForm", "Question #4"))
        self.a5_label.setText(_translate("categoryEditForm", "Answer #5"))
        self.q5_label.setText(_translate("categoryEditForm", "Question #5"))

        self.category.setText(_translate("categoryEditForm", catFull[0]))
        self.question1.setText(_translate("categoryEditForm", catFull[1]))
        self.answer1.setText(_translate("categoryEditForm", catFull[2]))
        self.question2.setText(_translate("categoryEditForm", catFull[3]))
        self.answer2.setText(_translate("categoryEditForm", catFull[4]))
        self.question3.setText(_translate("categoryEditForm", catFull[5]))
        self.answer3.setText(_translate("categoryEditForm", catFull[6]))
        self.question4.setText(_translate("categoryEditForm", catFull[7]))
        self.answer4.setText(_translate("categoryEditForm", catFull[8]))
        self.question5.setText(_translate("categoryEditForm", catFull[9]))
        self.answer5.setText(_translate("categoryEditForm", catFull[10]))

        self.save.setText(_translate("categoryEditForm", "Save"))
        self.cancel.setText(_translate("categoryEditForm", "Cancel"))


    def __getFullCategory(self, category):
        filename = os.path.join('db', category + '.csv')
        try:
            with open(filename, "r") as csvfile:
                rowReader = csv.reader(csvfile, delimiter='|')
                for row in rowReader:
                    return row
        except:
            message = QMessageBox.question(self, "Error",
                                           "File does not exist",
                                           QMessageBox.Ok)
            if (message == QMessageBox.Ok):
                self.close()
            else:
                pass
