from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui.categoryEditForm import Ui_categoryEditForm
import os
import csv

class CategoryEditFormWindow(QtWidgets.QMainWindow, Ui_categoryEditForm):
    def __init__(self, category, parent):
        super(CategoryEditFormWindow, self).__init__(parent)
        self.setupUi(self, category)
        self.save.clicked.connect(self.saveCategory)
        self.save.clicked.connect(self.close)
        self.save.clicked.connect(parent.show)
        self.cancel.clicked.connect(self.close)
        self.cancel.clicked.connect(parent.show)

    def saveCategory(self):
        if self.formCompleted():
            filename = os.path.join('db', self.category.text() + '.csv')
            try:
                with open(filename, 'w') as csvfile:
                    rowwriter = csv.writer(csvfile, delimiter='|')
                    rowwriter.writerow([self.category.text(), self.question1.text(), self.answer1.text(),
                                        self.question2.text(), self.answer2.text(), self.question3.text(),
                                        self.answer3.text(), self.question4.text(), self.answer4.text(),
                                        self.question5.text(), self.answer5.text()])
            except:
                message = QMessageBox.question(self, "Error",
                                               "The category has not been saved. Please check the content.",
                                               QMessageBox.Ok)
                if (message == QMessageBox.Ok):
                    self.close()
                else:
                    pass
            else:
                fields = [self.category, self.question1, self.answer1, self.question2, self.answer2,
                          self.question3, self.answer3, self.question4, self.answer4, self.question5, self.answer5]
                for field in fields:
                    field.clear()
                message = QMessageBox.question(self, "Success",
                                               "The category has been saved.",
                                               QMessageBox.Ok)
                if (message == QMessageBox.Ok):
                    self.close()
                else:
                    pass
        else:
            message = QMessageBox.question(self, "Error",
                                           "The category has not been saved. Please check the content.",
                                          QMessageBox.Ok)
            if (message == QMessageBox.Ok):
                self.close()
            else:
                pass

    def formCompleted(self):
        blank = ""
        if self.category.text() == blank or self.question1.text() == blank or self.answer1.text() == blank or \
                self.question2.text() == blank or self.answer2.text() == blank or self.question3.text() == blank or \
                self.answer3.text() == blank or self.question4.text() == blank or self.answer4.text() == blank or \
                self.question5.text() == blank or self.answer5.text() == blank:
            return False
        else:
            return True