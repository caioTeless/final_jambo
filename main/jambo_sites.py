import sys

from PySide2.QtWidgets import QWidget, QApplication

from aux_classes_gui.sites_result import Ui_resultSites
from helpers.helper_buttons import button_generic, input_generic


class JamboSites(QWidget, Ui_resultSites):
    def __init__(self):
        super(JamboSites, self).__init__()
        self.setupUi(self)
        # Buttons
        self.removeResultSites.setStyleSheet(button_generic())
        self.insertSitesButton.setStyleSheet(button_generic())
        self.backResultSites.setStyleSheet(button_generic())
        self.browserResultSites.setStyleSheet(button_generic())
        #
        # Input
        self.insertSites.setStyleSheet(input_generic())
        self.insert_data()

    def insert_data(self):
        data = []
        self.resultSitesList.setWordWrap(True)
        with open('teste.txt', 'r') as arquive:
            for n in arquive.readlines():
                data.append(n)
        for j in data:
            self.resultSitesList.addItem(j)


if __name__ == '__main__':
    app = QApplication([])
    ui = JamboSites()
    ui.show()
    sys.exit(app.exec_())
