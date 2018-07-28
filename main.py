from PyQt5 import QtGui, QtWidgets
import sys
from ui.main import Ui_main
from ui.categoryMenu import Ui_categoryMenu
from ui.categoryAdd import Ui_categoryAdd 
import module.mainWindow as mainWindow

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv)
  form = mainWindow.MainWindow()
  form.show()
  app.exec_()