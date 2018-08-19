from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_categoryMenu(object):

    # I've changed the GUIs around a bit.  They are no londer resizable.  I've added a WOJ logo
    def setupUi(self, categoryMenu):
        categoryMenu.setObjectName("categoryMenu")
        categoryMenu.setFixedSize(1000, 600)
        self.logo = QtWidgets.QLabel(categoryMenu)
        self.logo.setGeometry(QtCore.QRect(75, 40, 1000, 200))
        self.logo.setPixmap(QtGui.QPixmap('WOJlogo.png'))
        self.logo.setObjectName("logo")
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
        categoryMenu.setWindowTitle(_translate("categoryMenu", "Wheel of Jeopardy"))
        self.categoryEdit.setText(_translate("categoryMenu", "Edit Category"))
        self.back.setText(_translate("categoryMenu", "Back"))
        self.categoryDelete.setText(_translate("categoryMenu", "Delete Category"))
        self.categoryAdd.setText(_translate("categoryMenu", "Add Category"))

