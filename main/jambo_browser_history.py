import os.path
import sys

from PySide2.QtWidgets import QWidget, QApplication
from aux_classes_gui.history_browser import Ui_Form
from helpers.helper_buttons import button_generic


class JamboBrowserHistory(QWidget, Ui_Form):

    def __init__(self):
        super(JamboBrowserHistory, self).__init__()
        self.setupUi(self)

        self.removeHistory.setStyleSheet(button_generic())

        # Actions
        self.removeHistory.clicked.connect(self.remove_history)

        self.read_history()

    def read_history(self):
        self.listHistory.clear()
        items = os.path.exists('history_data.txt')
        if items:
            with open('history_data.txt', 'r') as arquive:
                self.listHistory.addItems(arquive.readlines())
        else:
            open('history_data.txt', 'x')

    def remove_history(self):
        items = open('history_data.txt', 'w+')
        items.write('')
        items.close()
        self.listHistory.clear()


if __name__ == '__main__':
    app = QApplication([])
    history = JamboBrowserHistory()
    history.show()
    sys.exit(app.exec_())

