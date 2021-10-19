from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QAction, QToolBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle('Jambo')
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.backButton = QtWidgets.QPushButton(self.centralWidget)
        self.backButton.setObjectName('backButton')
        self.horizontalLayout.addWidget(self.backButton)
        self.backButton.setEnabled(False)

        self.fowardButton = QtWidgets.QPushButton(self.centralWidget)
        self.fowardButton.setObjectName('fowardButton')
        self.horizontalLayout.addWidget(self.fowardButton)
        self.fowardButton.setEnabled(False)

        self.refreshButton = QtWidgets.QPushButton(self.centralWidget)
        self.fowardButton.setObjectName('refreshButton')
        self.horizontalLayout.addWidget(self.refreshButton)

        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.historyButton = QtWidgets.QPushButton(self.centralWidget)
        self.historyButton.setObjectName('historyButton')
        self.horizontalLayout.addWidget(self.historyButton)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralWidget)
        self.webEngineView.setUrl(QtCore.QUrl("https://www.google.com.br"))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout.addWidget(self.webEngineView)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Button operations

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


from PySide2 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())