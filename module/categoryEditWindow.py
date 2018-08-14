from PyQt5 import QtGui, QtWidgets
from ui.categoryEdit import Ui_categoryEdit
import os
import csv

class CategoryEditWindow(QtWidgets.QMainWindow, Ui_categoryEdit):
    def __init__(self, parent):
        super(CategoryEditWindow, self).__init__(parent)
        self.setupUi(self)
        for file in os.listdir(os.path.join(os.getcwd(),'db')):
            with open(os.path.join(os.getcwd(),'db',file)) as csvfile:
                ader = csv.reader(csvfile, delimiter='|')
                for row in ader:
                    self.list.addItem(row[0])
        self.cancel.clicked.connect(self.close)
        self.cancel.clicked.connect(parent.show)        
        self.select.clicked.connect(self.show)