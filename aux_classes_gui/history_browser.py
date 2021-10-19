# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_browser.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModal)
        Form.resize(600, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setLayoutDirection(Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(63, 217, 93, 255), stop:1 rgba(137, 230, 65, 255));")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listHistory = QListWidget(self.frame)
        self.listHistory.setObjectName(u"listHistory")
        self.listHistory.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Arial\";\n"
"border-radius: 4px;\n"
"padding: 4px;")
        self.listHistory.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listHistory.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.listHistory)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.removeHistory = QPushButton(self.frame)
        self.removeHistory.setObjectName(u"removeHistory")
        self.removeHistory.setMinimumSize(QSize(400, 0))
        self.removeHistory.setMaximumSize(QSize(400, 16777215))
        self.removeHistory.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Courier\";")

        self.horizontalLayout.addWidget(self.removeHistory)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.removeHistory.setText(QCoreApplication.translate("Form", u"LIMPAR HIST\u00d3RICO", None))
    # retranslateUi

