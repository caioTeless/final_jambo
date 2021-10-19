import os
import sys

from PySide2.QtCore import QThread, Signal, QObject, SIGNAL
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QApplication
from aux_classes_gui.first_window import Ui_JamboGui
from helpers.helper_buttons import button_generic

from jambo_browser import JamboBrowser
from jambo_sites import JamboSites
from jambo_results import JamboResults


class Worker(QThread):

    progress = Signal(str)

    def __init__(self):
        super(Worker, self).__init__()

    def run(self):
        self.progress.emit(str)


class JamboHome(QWidget, Ui_JamboGui):
    def __init__(self):
        super(JamboHome, self).__init__()
        self.setupUi(self)

        # Window
        self.setWindowIcon(QIcon(os.path.join(os.getcwd(), '../images/jb_icon')))
        self.setWindowTitle('Home - Jambo')

        # Style Button
        self.searchInputButton.setStyleSheet(button_generic())
        self.openSites.setStyleSheet(button_generic())
        self.openMiniBrowser.setStyleSheet(button_generic())
        #
        # Show another window
        self.browser = JamboBrowser()
        self.sites = JamboSites()
        self.results = JamboResults()

        # Icons

        # View controls
        self.searchInputButton.setDisabled(True)
        self.inputSearch.textChanged.connect(self.disable_button)

        # Operations
        self.start_operations()

        # Threads
        self.thread = None

    def disable_button(self):
        if len(self.inputSearch.text()) > 0:
            self.searchInputButton.setDisabled(False)
        else:
            self.searchInputButton.setDisabled(True)

    def show_browser(self):
        self.browser.show()

    def show_sites(self):
        self.sites.show()

    def show_results(self):
        self.results.show()

    def start_operations(self):
        self.openMiniBrowser.clicked.connect(self.show_browser)
        self.openSites.clicked.connect(self.show_sites)

        # Not implemeted yet
        self.searchInputButton.clicked.connect(self.show_results)


if __name__ == '__main__':
    app = QApplication([])
    home = JamboHome()
    home.show()
    sys.exit(app.exec_())

