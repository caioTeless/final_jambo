import sys

from PySide2.QtGui import QTextBlockFormat
from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtCore import Qt
from aux_classes_gui.list_result import Ui_formResult
from helpers.helper_buttons import *


class JamboResults(QWidget, Ui_formResult):

    def __init__(self):
        super(JamboResults, self).__init__()
        self.setupUi(self)

        # Style Button
        self.backListButton.setStyleSheet(button_generic())
        self.saveListButton.setStyleSheet(button_generic())
        self.clearListButton.setStyleSheet(button_generic())

        # Methods
        self.insert_data()

        self.textResults.setAlignment(Qt.AlignJustify)

        self. save_new_arquive()
        self.operations()

    # Always get a new data
    def insert_data(self):
        with open('teste.txt', 'r+') as arquive:
            self.textResults.setText(str(arquive.read().replace('\n', '')))

    # Write save data
    def get_new_text(self):
        with open('teste.txt', 'w') as arquive:
            arquive.write(self.textResults.toPlainText())

    def save_new_arquive(self):
        self.saveListButton.clicked.connect(self.get_new_text)

    def operations(self):
        self.clearListButton.clicked.connect(self.textResults.clear)


"""
if __name__ == '__main__':
    app = QApplication([])
    ui = JamboResults()
    ui.operations()
    ui.show()
    sys.exit(app.exec_())
"""
