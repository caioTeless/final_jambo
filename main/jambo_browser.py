import os
import sys
from PySide2.QtCore import QUrl, QThread, Signal
from PySide2.QtGui import QIcon
from PySide2.QtWebEngineWidgets import QWebEnginePage
from PySide2.QtWidgets import QApplication, QMainWindow
from aux_classes_gui.mini_browser_gui import Ui_MainWindow
from helpers.helper_buttons import *
from main.jambo_browser_history import JamboBrowserHistory


class Worker(QThread):

    progress = Signal(str)

    def __init__(self):
        super(Worker, self).__init__()
        self.history = JamboBrowserHistory()

    def run(self):
        self.history.read_history()
        self.progress.emit(str)


class JamboBrowser(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(JamboBrowser, self).__init__()
        self.setupUi(self)

        # Window
        self.setWindowIcon(QIcon(os.path.join(os.getcwd(), '../images/jb_icon')))

        # History page
        self.history = JamboBrowserHistory()

        self.lineEdit.setStyleSheet(input_browser())

        self.setStyleSheet(background_generic())
        self.lineEdit.setClearButtonEnabled(True)

        # Button browser style
        self.backButton.setStyleSheet(button_browser())
        self.fowardButton.setStyleSheet(button_browser())
        self.refreshButton.setStyleSheet(button_browser())
        self.historyButton.setStyleSheet(button_browser())

        # Name
        self.backButton.setText('B')
        self.fowardButton.setText('F')
        self.refreshButton.setText('R')
        self.historyButton.setText('H')

        # Size
        self.backButton.setMinimumSize(30, 30)
        self.fowardButton.setMinimumSize(30, 30)
        self.refreshButton.setMinimumSize(30, 30)
        self.historyButton.setMinimumSize(30, 30)

        # Actions
        self.refreshButton.clicked.connect(self.reload)
        self.lineEdit.returnPressed.connect(self.load)
        self.backButton.clicked.connect(self.back)
        self.fowardButton.clicked.connect(self.forward)

        self.webEngineView.page().urlChanged.connect(self.url_changed)
        self.webEngineView.page().urlChanged.connect(self.load_finished)

        self.webEngineView.page().titleChanged.connect(self.setWindowTitle)

        self.historyButton.clicked.connect(self.show_history)

        # Thread
        self.thread = None
        self.history = JamboBrowserHistory()

        # Icons
        self.backButton.setText('')
        self.backButton.setIcon(QIcon(os.path.join(os.getcwd(), '../images/arrow_left.png')))
        # -
        self.fowardButton.setText('')
        self.fowardButton.setIcon(QIcon(os.path.join(os.getcwd(), '../images/arrow_right.png')))
        # -
        self.refreshButton.setText('')
        self.refreshButton.setIcon(QIcon(os.path.join(os.getcwd(), '../images/reload.png')))
        # -
        self.historyButton.setText('')
        self.historyButton.setIcon((QIcon(os.path.join(os.getcwd(), '../images/search_history.png'))))

    def reload(self):
        self.webEngineView.reload()

    def load_finished(self):
        if self.webEngineView.history().canGoBack():
            self.backButton.setEnabled(True)
        else:
            self.backButton.setEnabled(False)
        if self.webEngineView.history().canGoForward():
            self.fowardButton.setEnabled(True)
        else:
            self.fowardButton.setEnabled(False)

    def load(self):
        url = QUrl.fromUserInput(self.lineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)

    def back(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    def url_changed(self, url):
        self.thread = Worker()
        self.lineEdit.setText(url.toString())
        with open('history_data.txt', 'a+') as arquive:
            if self.isVisible():
                arquive.write(self.lineEdit.text())
                arquive.write('\n')
        self.thread.progress.connect(self.history.read_history)
        self.thread.start()

    def show_history(self):
        self.history.show()
        self.thread.progress.disconnect()

