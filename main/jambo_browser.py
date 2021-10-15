import sys

from PySide2.QtCore import QSize, QUrl
from PySide2.QtWidgets import QApplication, QMainWindow

from aux_classes_gui.mini_browser_gui import Ui_MainWindow
from helpers.helper_buttons import *


class JamboBrowser(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(JamboBrowser, self).__init__()
        self.setupUi(self)
        self.pushButton.setText('Pesquisar')
        self.pushButton.setStyleSheet(button_generic())
        self.pushButton.setMinimumSize(QSize(100, 35))
        self.lineEdit.setStyleSheet(input_generic())
        self.setStyleSheet(background_generic())
        self.pushButton.clicked.connect(self.return_page)

    def return_page(self):
        url = QUrl(self.lineEdit.text())
        if not url:
            self.load_finished()
        else:
            self.webEngineView.setUrl(url)

    def load_finished(self):
        url = self.webEngineView.url().toString()
        self.lineEdit.setText(url)


if __name__ == '__main__':
    app = QApplication([])
    ui = JamboBrowser()
    ui.show()
    sys.exit(app.exec_())

