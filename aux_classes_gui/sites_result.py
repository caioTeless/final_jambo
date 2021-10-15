# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sites_result.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_resultSites(object):
    def setupUi(self, resultSites):
        if not resultSites.objectName():
            resultSites.setObjectName(u"resultSites")
        resultSites.resize(599, 300)
        resultSites.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(63, 217, 93, 255), stop:1 rgba(137, 230, 65, 255));")
        self.verticalLayout = QVBoxLayout(resultSites)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 5, 15, 5)
        self.insertSites = QLineEdit(resultSites)
        self.insertSites.setObjectName(u"insertSites")
        self.insertSites.setMinimumSize(QSize(0, 32))
        self.insertSites.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";\n"
"border-radius: 4px;\n"
"padding: 4px;")

        self.horizontalLayout_2.addWidget(self.insertSites)

        self.insertSitesButton = QPushButton(resultSites)
        self.insertSitesButton.setObjectName(u"insertSitesButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.insertSitesButton.sizePolicy().hasHeightForWidth())
        self.insertSitesButton.setSizePolicy(sizePolicy)
        self.insertSitesButton.setMinimumSize(QSize(100, 32))
        self.insertSitesButton.setMaximumSize(QSize(150, 16777215))
        self.insertSitesButton.setSizeIncrement(QSize(0, 32))
        self.insertSitesButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Courier\";")

        self.horizontalLayout_2.addWidget(self.insertSitesButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.resultSitesList = QListWidget(resultSites)
        self.resultSitesList.setObjectName(u"resultSitesList")
        self.resultSitesList.setStyleSheet(u"font: 10pt \"Arial\";\n"
"padding: 7px;\n"
"border-radius: 4px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"QScrollBar::vertical{\n"
"	\n"
"	background-color: rgb(0, 85, 0);\n"
"	width: 15px;\n"
"}")

        self.verticalLayout.addWidget(self.resultSitesList)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.backResultSites = QPushButton(resultSites)
        self.backResultSites.setObjectName(u"backResultSites")
        self.backResultSites.setMinimumSize(QSize(100, 32))
        self.backResultSites.setMaximumSize(QSize(150, 32))
        self.backResultSites.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Courier\";")

        self.horizontalLayout.addWidget(self.backResultSites)

        self.removeResultSites = QPushButton(resultSites)
        self.removeResultSites.setObjectName(u"removeResultSites")
        self.removeResultSites.setMinimumSize(QSize(150, 32))
        self.removeResultSites.setMaximumSize(QSize(150, 32))
        self.removeResultSites.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Courier\";")

        self.horizontalLayout.addWidget(self.removeResultSites)

        self.browserResultSites = QPushButton(resultSites)
        self.browserResultSites.setObjectName(u"browserResultSites")
        self.browserResultSites.setMinimumSize(QSize(100, 32))
        self.browserResultSites.setMaximumSize(QSize(150, 32))
        self.browserResultSites.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Courier\";")

        self.horizontalLayout.addWidget(self.browserResultSites)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(resultSites)
        self.removeResultSites.clicked.connect(self.resultSitesList.clearSelection)
        self.backResultSites.clicked.connect(resultSites.hide)

        QMetaObject.connectSlotsByName(resultSites)
    # setupUi

    def retranslateUi(self, resultSites):
        resultSites.setWindowTitle(QCoreApplication.translate("resultSites", u"Form", None))
        self.insertSitesButton.setText(QCoreApplication.translate("resultSites", u"Inserir", None))
        self.backResultSites.setText(QCoreApplication.translate("resultSites", u"Voltar", None))
        self.removeResultSites.setText(QCoreApplication.translate("resultSites", u"Remover", None))
        self.browserResultSites.setText(QCoreApplication.translate("resultSites", u"Browser", None))
    # retranslateUi

