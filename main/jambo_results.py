import os
import sys

from PySide2.QtGui import QTextBlockFormat, QIcon
from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtCore import Qt
from aux_classes_gui.list_result import Ui_formResult
from helpers.helper_buttons import *
from main.jambo_browser import JamboBrowser


class JamboResults(QWidget, Ui_formResult):

    def __init__(self):
        super(JamboResults, self).__init__()
        self.setupUi(self)

        # Window
        self.setWindowIcon(QIcon(os.path.join(os.getcwd(), '../images/jb_icon')))
        self.setWindowTitle('Resultados - Jambo')

        # Style Button
        self.backListButton.setStyleSheet(button_generic())
        self.saveListButton.setStyleSheet(button_generic())
        self.clearListButton.setStyleSheet(button_generic())

        # Methods
        self.insert_data_display()

        self.textResults.setAlignment(Qt.AlignJustify)

        self.save_new_arquive()

        # ACtions
        self.clearListButton.clicked.connect(self.clear_results)

        # Browser
        self.browser = JamboBrowser()

    # Always get a new data
    def insert_data_display(self):
        arquive = open('data.txt', 'r', encoding='utf-8')
        self.textResults.setText(str(arquive.read().replace('\n', '')))
        preview = open('../crawler/crawler_general.txt', 'r')
        self.contentPreview.setText(str(preview.read()))
        if self.isVisible():
            arquive.close()
            preview.close()
        arquive.seek(0)
        preview.seek(0)

    # Write save data
    def get_new_text(self):
        self.textResults.setSpacing(10)
        with open('data.txt', 'w+', encoding='utf-8') as arquive:
            arquive.write(self.textResults.toPlainText())

    def save_new_arquive(self):
        self.saveListButton.clicked.connect(self.get_new_text)

    def clear_results(self):
        items = open('data.txt', 'w+', encoding='utf-8')
        items_tips = open('data.txt', 'w+', encoding='utf-8')
        items_tips.write('')
        items.write('')
        items.close()
        items_tips.close()
        self.textResults.clear()
        self.contentPreview.clear()


if __name__ == '__main__':
    app = QApplication([])
    ui = JamboResults()
    ui.show()
    sys.exit(app.exec_())

