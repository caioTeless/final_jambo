import sys
from PySide2.QtWidgets import QWidget, QApplication
from aux_classes_gui.first_window import Ui_JamboGui
from helpers.helper_buttons import button_generic

from jambo_browser import JamboBrowser
from jambo_sites import JamboSites
from jambo_results import JamboResults


class JamboHome(QWidget, Ui_JamboGui):
    def __init__(self):
        super(JamboHome, self).__init__()
        self.setupUi(self)

        # Style Button
        self.searchInputButton.setStyleSheet(button_generic())
        self.openSites.setStyleSheet(button_generic())
        self.openMiniBrowser.setStyleSheet(button_generic())
        #
        # Show another window
        self.browser = JamboBrowser()
        self.sites = JamboSites()
        self.results = JamboResults()
        #

    def show_browser(self):
        self.browser.show()

    def show_sites(self):
        self.sites.show()

    def show_results(self):
        self.results.show()
    #     if self.results.cleanListButton.sender():
    #         self.results.listResult.clear()

    def start_operations(self):
        self.openMiniBrowser.clicked.connect(self.show_browser)
        self.openSites.clicked.connect(self.show_sites)

        # Not implemeted yet
        self.searchInputButton.clicked.connect(self.show_results)


if __name__ == '__main__':
    app = QApplication([])
    home = JamboHome()
    home.start_operations()
    home.show()
    sys.exit(app.exec_())

