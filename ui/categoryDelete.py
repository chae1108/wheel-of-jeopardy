from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os

class Ui_categoryDelete(object):
    def setupUi(self, categoryDelete):
        categoryDelete.setObjectName("categoryDelete")
        categoryDelete.setFixedSize(950, 665)
        self.logo = QtWidgets.QLabel(categoryDelete)
        self.logo.setGeometry(QtCore.QRect(50, 15, 1000, 100))
        self.logo.setPixmap(QtGui.QPixmap('WOJlogo.png'))
        self.logo.setObjectName("logo")
        self.list = QtWidgets.QListWidget(categoryDelete)
        self.list.setGeometry(QtCore.QRect(190, 120, 580, 460))
        self.list.setObjectName("list")
        self.remove = QtWidgets.QPushButton(categoryDelete)
        self.remove.setGeometry(QtCore.QRect(240, 600, 211, 51))
        self.remove.setObjectName("remove")
        self.cancel = QtWidgets.QPushButton(categoryDelete)
        self.cancel.setGeometry(QtCore.QRect(510, 600, 211, 51))
        self.cancel.setObjectName("cancel")

        categories = self.getCategoryNames()

        for category in categories:
            item = QtWidgets.QListWidgetItem(category)
            self.list.addItem(item.text())

        self.retranslateUi(categoryDelete)
        QtCore.QMetaObject.connectSlotsByName(categoryDelete)

    def retranslateUi(self, categoryDelete):
        _translate = QtCore.QCoreApplication.translate
        categoryDelete.setWindowTitle(_translate("categoryDelete", "Delete Category"))
        self.remove.setText(_translate("categoryDelete", "Delete"))
        self.cancel.setText(_translate("categoryDelete", "Cancel"))

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
            category = self.list.currentItem().text()
            item = self.list.currentRow()
            ci = [category, item]
        except:
            message = QMessageBox.question(self, "Error",
                                           "Please select a category.",
                                           QMessageBox.Ok)
            if (message == QMessageBox.Ok):
                pass
        else:
            return ci
