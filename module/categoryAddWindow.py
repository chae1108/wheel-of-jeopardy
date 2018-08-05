from PyQt5 import QtGui, QtWidgets
from ui.categoryAdd import Ui_categoryAdd
import csv
import time

class CategoryAddWindow(QtWidgets.QMainWindow, Ui_categoryAdd):
    def __init__(self, parent):
        super(CategoryAddWindow, self).__init__(parent)
        self.setupUi(self)
        self.cancel.clicked.connect(self.close)
        self.cancel.clicked.connect(parent.show)
        self.save.clicked.connect(self.saveCategory)
        self.save.clicked.connect(self.show)

    def saveCategory(self):
        filename = 'db/' + 'category' + time.strftime("%Y%m%d%H%M%S") + '.csv'
        try:
            with open(filename,'w') as csvfile:
                rowwriter = csv.writer(csvfile, delimiter='|')
                rowwriter.writerow([self.category.text(),self.question1.text(),self.answer1.text(),
                self.question2.text(),self.answer2.text(),self.question3.text(),
                self.answer3.text(),self.question4.text(),self.answer4.text(),
                self.question5.text(),self.answer5.text()])
            self.message = QtWidgets.QMessageBox()
        except:
            self.message.setWindowTitle("Category Status")
            self.message.setText("The category has not saved. Please check the content.")
            self.message.show()
        else:    
            fields = [self.category,self.question1,self.answer1,self.question2,self.answer2,
            self.question3,self.answer3,self.question4,self.answer4,self.question5,self.answer5]
            for field in fields:
                field.clear()                   
            self.message.setWindowTitle("Category Status")
            self.message.setText("The category has been saved.")
            self.message.show()