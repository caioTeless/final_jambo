import os
import sys

from PySide2.QtCore import QThread, Signal, QSize
from PySide2.QtGui import QIcon, QMovie
from PySide2.QtWidgets import QWidget, QApplication
from aux_classes_gui.first_window import Ui_JamboGui
from crawler.crawler_content import CrawlerContent
from helpers.helper_buttons import button_generic
from jambo_browser import JamboBrowser
from jambo_sites import JamboSites
from jambo_results import JamboResults


class Worker(QThread):

    progress = Signal(str)

    def __init__(self, query='', tot_query=0):
        super(Worker, self).__init__()
        self.query = query
        self.tot_query = tot_query

    def run(self):
        search = CrawlerContent(self.query, self.tot_query)
        # search_api = CrawlerGeneralContent()
        # search_api.query = self.query
        # search_api.get_results()
        search.get_page()
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
        image = os.path.join(os.getcwd(), '../images/loader_search.gif')
        self.movie = QMovie(image)
        self.movie.setScaledSize(QSize(50, 50))

        # View controls
        self.searchInputButton.setDisabled(True)
        self.inputSearch.textChanged.connect(self.disable_button)

        # Operations
        self.start_operations()

        # Threads
        self.thread = None

        # Crawlers
        self.crawler_content = CrawlerContent()

    def disable_button(self):
        if len(self.inputSearch.text()) > 0:
            self.searchInputButton.setDisabled(False)
        else:
            self.searchInputButton.setDisabled(True)

    def show_browser(self):
        self.browser.show()

    def show_sites(self):
        self.sites.show()

    def load_animation(self):
        self.thread = Worker(self.inputSearch.text(), self.selectTotalSites.value())
        self.projectLoader.setMovie(self.movie)
        self.movie.start()
        self.thread.progress.connect(self.show_results)
        self.thread.start()

    def show_results(self):
        self.movie.stop()
        self.projectLoader.clear()
        self.thread.progress.disconnect()
        self.thread = None
        with open('data.txt', 'r', encoding='utf-8') as file:
            res = file.read()
            if len(res) <= 0:
                self.results.textResults.hide()
                self.results.saveListButton.setDisabled(True)
            else:
                self.results.saveListButton.setDisabled(False)
                self.results.textResults.show()
            file.seek(0)
        self.results.insert_data_display()
        self.results.show()

    def start_operations(self):
        self.openMiniBrowser.clicked.connect(self.show_browser)
        self.openSites.clicked.connect(self.show_sites)
        self.searchInputButton.clicked.connect(self.load_animation)


if __name__ == '__main__':
    app = QApplication([])
    home = JamboHome()
    home.show()
    sys.exit(app.exec_())

