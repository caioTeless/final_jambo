# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'first_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_JamboGui(object):
    def setupUi(self, JamboGui):
        if not JamboGui.objectName():
            JamboGui.setObjectName(u"JamboGui")
        JamboGui.resize(500, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(250)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(JamboGui.sizePolicy().hasHeightForWidth())
        JamboGui.setSizePolicy(sizePolicy)
        JamboGui.setMinimumSize(QSize(500, 150))
        JamboGui.setMaximumSize(QSize(500, 150))
        self.myGrid2 = QGridLayout(JamboGui)
        self.myGrid2.setObjectName(u"myGrid2")
        self.myGrid2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(JamboGui)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(500, 150))
        self.frame.setMaximumSize(QSize(800, 600))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(63, 217, 93, 255), stop:1 rgba(137, 230, 65, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.projectLoader = QLabel(self.frame)
        self.projectLoader.setObjectName(u"projectLoader")
        self.projectLoader.setMinimumSize(QSize(50, 50))
        self.projectLoader.setMaximumSize(QSize(50, 50))
        self.projectLoader.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.projectLoader.setFrameShadow(QFrame.Plain)
        self.projectLoader.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.projectLoader, 3, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.inputSearch = QLineEdit(self.frame)
        self.inputSearch.setObjectName(u"inputSearch")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.inputSearch.sizePolicy().hasHeightForWidth())
        self.inputSearch.setSizePolicy(sizePolicy2)
        self.inputSearch.setMinimumSize(QSize(180, 32))
        self.inputSearch.setMaximumSize(QSize(350, 32))
        self.inputSearch.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";\n"
"border-radius: 4px;\n"
"padding: 4px;")
        self.inputSearch.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.inputSearch)

        self.searchInputButton = QPushButton(self.frame)
        self.searchInputButton.setObjectName(u"searchInputButton")
        sizePolicy2.setHeightForWidth(self.searchInputButton.sizePolicy().hasHeightForWidth())
        self.searchInputButton.setSizePolicy(sizePolicy2)
        self.searchInputButton.setMinimumSize(QSize(100, 32))
        self.searchInputButton.setMaximumSize(QSize(50, 32))
        self.searchInputButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"font: 10pt \"Courier\";\n"
"color: rgb(255, 255, 255);")
        self.searchInputButton.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.searchInputButton)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 3, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.openSites = QPushButton(self.frame)
        self.openSites.setObjectName(u"openSites")
        self.openSites.setMinimumSize(QSize(100, 32))
        self.openSites.setMaximumSize(QSize(100, 32))
        self.openSites.setSizeIncrement(QSize(100, 32))
        self.openSites.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Courier\";")

        self.horizontalLayout_2.addWidget(self.openSites)

        self.horizontalSpacer_3 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.openMiniBrowser = QPushButton(self.frame)
        self.openMiniBrowser.setObjectName(u"openMiniBrowser")
        sizePolicy2.setHeightForWidth(self.openMiniBrowser.sizePolicy().hasHeightForWidth())
        self.openMiniBrowser.setSizePolicy(sizePolicy2)
        self.openMiniBrowser.setMinimumSize(QSize(100, 32))
        self.openMiniBrowser.setMaximumSize(QSize(100, 32))
        self.openMiniBrowser.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Courier\";")

        self.horizontalLayout_2.addWidget(self.openMiniBrowser, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 6)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 3, 3, 1, 1)


        self.myGrid2.addWidget(self.frame, 0, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(JamboGui)

        QMetaObject.connectSlotsByName(JamboGui)
    # setupUi

    def retranslateUi(self, JamboGui):
        JamboGui.setWindowTitle(QCoreApplication.translate("JamboGui", u"JamboGui", None))
        self.projectLoader.setText("")
        self.inputSearch.setPlaceholderText(QCoreApplication.translate("JamboGui", u"Insira algum dado", None))
        self.searchInputButton.setText(QCoreApplication.translate("JamboGui", u"Pesquisar", None))
        self.openSites.setText(QCoreApplication.translate("JamboGui", u"Sites", None))
        self.openMiniBrowser.setText(QCoreApplication.translate("JamboGui", u"Browser", None))
    # retranslateUi

