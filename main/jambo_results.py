import os
import sys

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QFileDialog, QApplication
from PySide2.QtCore import Qt
from aux_classes_gui.list_result import Ui_formResult
from helpers.helper_buttons import *
from main.jambo_browser import JamboBrowser
from model import jambo_pdf


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

        self.textResults.setAlignment(Qt.AlignJustify)

        # ACtions
        self.clearListButton.clicked.connect(self.clear_results)
        self.saveListButton.clicked.connect(self.save_content)

        # Browser
        self.browser = JamboBrowser()

    def get_wiki_sites(self):
        for sites in self.wiki_content:
            return sites

    # Always get a new data
    def insert_data_display(self):
        with open('data.txt', 'r', encoding='utf-8') as arquive:
            words = arquive.read().split(' ')
            size = round(len(words) / 0.9)
            arquive.seek(0)
            self.textResults.setText(arquive.read()[:size] + '[...]')
            arquive.seek(0)
        with open('crawler_general.txt', 'r', encoding='utf-8') as preview:
            self.contentPreview.setText(str(preview.read()))
            preview.seek(0)

    def clear_results(self):
        items = open('crawler_general.txt', 'w+', encoding='utf-8')
        items_tips = open('data.txt', 'w+', encoding='utf-8')
        items_tips.write('')
        items.write('')
        items.close()
        items_tips.close()
        self.textResults.clear()
        self.contentPreview.clear()

    def save_content(self):
        if len(self.textResults.toPlainText()) > 0:
            options = QFileDialog.Options()
            # options |= QFileDialog.DontUseNativeDialog
            file_name, _ = QFileDialog.getSaveFileName(self, 'Salvar - Jambo', '', '*.pdf', options=options)
            if file_name:
                with open('data.txt', 'w+', encoding='utf-8') as arquive:
                    arquive.write(self.textResults.toPlainText())
                jb = jambo_pdf.JamboPDF('data.txt', file_name)
                jb.build_pdf()

"""
if __name__ == '__main__':
    app = QApplication([])
    home = JamboResults()
    home.show()
    sys.exit(app.exec_())
"""