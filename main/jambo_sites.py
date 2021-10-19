import sys
import os

from PySide2.QtWidgets import QWidget, QApplication

from aux_classes_gui.sites_result import Ui_resultSites
from helpers.helper_buttons import button_generic, input_generic
from jambo_browser import JamboBrowser


class JamboSites(QWidget, Ui_resultSites):
    def __init__(self):
        super(JamboSites, self).__init__()
        self.setupUi(self)
        # Buttons
        self.removeAll.setEnabled(True)
        self.removeSelection.setStyleSheet(button_generic())
        self.removeAll.setStyleSheet(button_generic())
        self.insertSitesButton.setStyleSheet(button_generic())
        self.backResultSites.setStyleSheet(button_generic())
        self.browserResultSites.setStyleSheet(button_generic())

        # browser
        self.browser = JamboBrowser()
        #
        # Input
        self.insertSites.setStyleSheet(input_generic())

        # Buttons actions
        self.removeSelection.clicked.connect(self.remove_selected)
        self.browserResultSites.clicked.connect(self.show_browser)
        self.insertSitesButton.clicked.connect(self.insert_data)
        self.removeAll.clicked.connect(self.remove_all)

        # ListWidget field
        self.resultSitesList.setWordWrap(True)

        self.get_data()

        # Tests
        self.resultSitesList.itemDoubleClicked.connect(self.take_url)

    def insert_data(self):
        item = self.insertSites.text()
        with open('testes_sites.txt', 'a') as arquive:
            arquive.write(item)
            arquive.write('\n')
        self.resultSitesList.clear()
        self.get_data()

    def get_data(self):
        test = os.path.exists('testes_sites.txt')
        if not test:
            open('testes_sites.txt', 'x')
        else:
            with open('testes_sites.txt', 'r') as arquive:
                self.resultSitesList.addItems(arquive.readlines())

    # remove current item
    def remove_selected(self):
        item = self.resultSitesList.takeItem(self.resultSitesList.currentRow())
        del item
        items = open('testes_sites.txt', 'w')
        for i in range(self.resultSitesList.count()):
            new_word = self.resultSitesList.item(i)
            items.write(new_word.text())
        items.close()

    # Remove all
    def remove_all(self):
        items = open('testes_sites.txt', 'w+')
        items.write('')
        items.close()
        self.resultSitesList.clear()


    def show_browser(self):
        self.browser.show()

    def take_url(self):
        item = self.resultSitesList.currentItem().text()
        self.browser.show()
        self.browser.lineEdit.setText(item)


if __name__ == '__main__':
    app = QApplication([])
    ui = JamboSites()
    ui.show()
    sys.exit(app.exec_())
