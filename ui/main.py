from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main(object):
    # I've changed the GUIs around a bit.  They are no londer resizable.  I've added a WOJ logo
    def setupUi(self, main):
        main.setObjectName("main")
        main.setFixedSize(1000, 550)
        self.logo = QtWidgets.QLabel(main)
        self.logo.setGeometry(QtCore.QRect(75, 40, 1000, 200))
        self.logo.setPixmap(QtGui.QPixmap('WOJlogo.png'))
        self.logo.setObjectName("logo")
        self.newGame = QtWidgets.QPushButton(main)
        self.newGame.setGeometry(QtCore.QRect(350, 300, 300, 70))
        self.newGame.setObjectName("newGame")
        self.categories = QtWidgets.QPushButton(main)
        self.categories.setGeometry(QtCore.QRect(350, 370, 300, 70))
        self.categories.setObjectName("categories")
        self.quit = QtWidgets.QPushButton(main)
        self.quit.setGeometry(QtCore.QRect(350, 440, 300, 70))
        self.quit.setObjectName("quit")

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Wheel of Jeopardy"))
        self.newGame.setText(_translate("main", "New Game"))
        self.categories.setText(_translate("main", "Categories"))
        self.quit.setText(_translate("main", "Quit"))
