from PyQt5 import QtGui, QtWidgets
from ui.categoryDelete import Ui_categoryDelete
import os
import csv

class CategoryDeleteWindow(QtWidgets.QMainWindow, Ui_categoryDelete):
    def __init__(self, parent):
        super(CategoryDeleteWindow, self).__init__(parent)
        self.setupUi(self)
        for file in os.listdir(os.path.join(os.getcwd(),'db')):
            with open(os.path.join(os.getcwd(),'db',file)) as csvfile:
                ader = csv.reader(csvfile, delimiter='|')
                for row in ader:
                    self.list.addItem(row[0])        
        self.cancel.clicked.connect(self.close)
        self.cancel.clicked.connect(parent.show)
        self.remove.clicked.connect(self.deleteCategory)

    def deleteCategory(self):
        try:
            self.message = QtWidgets.QMessageBox(parent=self)
            for file in os.listdir(os.path.join(os.getcwd(),'db')):
                removal = False
                with open(os.path.join(os.getcwd(),'db',file)) as csvfile:
                    ader = csv.reader(csvfile, delimiter='|')
                    for row in ader:
                        if row[0] == self.list.selectedItems()[0].text():
                            removal = True
                if removal == True:
                    os.remove(os.path.join(os.getcwd(),'db',file))
        except:
            self.message.setWindowTitle("Category Status")
            self.message.setText("The category has not been deleted.")
            self.message.show()
        else:    
            self.message.setWindowTitle("Category Status")
            self.message.setText("The category has been deleted.")
            self.message.show()   

