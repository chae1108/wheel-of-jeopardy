from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os

class Ui_categoryEdit(object):

    def setupUi(self, categoryEdit):
        categoryEdit.setObjectName("categoryEdit")
        categoryEdit.resize(950, 665)
        self.logo = QtWidgets.QLabel(categoryEdit)
        self.logo.setGeometry(QtCore.QRect(50, 15, 1000, 100))
        self.logo.setPixmap(QtGui.QPixmap('WOJlogo.png'))
        self.logo.setObjectName("logo")

        self.selectList = QtWidgets.QListWidget(categoryEdit)
        self.selectList.setGeometry(QtCore.QRect(190, 120, 580, 460))
        self.selectList.setObjectName("list")

        categories = self.getCategoryNames()

        for category in categories:
            item = QtWidgets.QListWidgetItem(category)
            self.selectList.addItem(item.text())

        self.select = QtWidgets.QPushButton(categoryEdit)
        self.select.setGeometry(QtCore.QRect(240, 600, 211, 51))
        self.select.setObjectName("select")
        self.cancel = QtWidgets.QPushButton(categoryEdit)
        self.cancel.setGeometry(QtCore.QRect(510, 600, 211, 51))
        self.cancel.setObjectName("cancel")

        self.retranslateUi(categoryEdit)
        QtCore.QMetaObject.connectSlotsByName(categoryEdit)

    def retranslateUi(self, categoryEdit):
        _translate = QtCore.QCoreApplication.translate
        categoryEdit.setWindowTitle(_translate("categoryEdit", "Select Category"))
        self.select.setText(_translate("categoryEdit", "Select"))
        self.cancel.setText(_translate("categoryEdit", "Cancel"))

    def getCategoryNames(self):
        categoryNames = []
        fileNames = os.listdir("./db")
        for file in fileNames:
            if file[-4:] == ".csv":
                file = file[:-4]
                categoryNames.append(file)

        return categoryNames

    def selectCategory(self):
        try:
            category = self.selectList.currentItem().text()
        except:
            message = QMessageBox.question(self, "Error",
                                           "Please select a category.",
                                           QMessageBox.Ok)
            if (message == QMessageBox.Ok):
                pass
        else:
            return category