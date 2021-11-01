# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_result.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_formResult(object):
    def setupUi(self, formResult):
        if not formResult.objectName():
            formResult.setObjectName(u"formResult")
        formResult.resize(600, 600)
        formResult.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(63, 217, 93, 255), stop:1 rgba(137, 230, 65, 255));")
        self.verticalLayout = QVBoxLayout(formResult)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 20, 10, 10)
        self.listTitle = QLabel(formResult)
        self.listTitle.setObjectName(u"listTitle")
        self.listTitle.setStyleSheet(u"font: 18pt \"Courier\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.listTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.listTitle)

        self.contentPreview = QTextEdit(formResult)
        self.contentPreview.setObjectName(u"contentPreview")
        self.contentPreview.setMinimumSize(QSize(16777215, 120))
        self.contentPreview.setStyleSheet(u"font: 10pt \"Arial\";\n"
"padding: 10px;\n"
"border-radius: 4px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"QScrollBar::vertical{\n"
"	\n"
"	background-color: rgb(0, 85, 0);\n"
"	width: 15px;\n"
"}")

        self.verticalLayout.addWidget(self.contentPreview)

        self.textResults = QTextEdit(formResult)
        self.textResults.setObjectName(u"textResults")
        self.textResults.setStyleSheet(u"font: 10pt \"Arial\";\n"
"padding: 10px;\n"
"border-radius: 4px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"QScrollBar::vertical{\n"
"	\n"
"	background-color: rgb(0, 85, 0);\n"
"	width: 15px;\n"
"}")
        self.textResults.setLineWidth(1)
        self.textResults.setMidLineWidth(0)
        self.textResults.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textResults.setDocumentTitle(u"")
        self.textResults.setLineWrapMode(QTextEdit.WidgetWidth)
        self.textResults.setLineWrapColumnOrWidth(0)
        self.textResults.setCursorWidth(2)
        # self.textResults.setMaximumSize(QSize(16777215, 16777215)) # Changed
        self.textResults.setMinimumSize(QSize(16777215, 350))


        self.verticalLayout.addWidget(self.textResults)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.backListButton = QPushButton(formResult)
        self.backListButton.setObjectName(u"backListButton")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backListButton.sizePolicy().hasHeightForWidth())
        self.backListButton.setSizePolicy(sizePolicy)
        self.backListButton.setMaximumSize(QSize(120, 16777215))
        self.backListButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Courier\";")

        self.horizontalLayout.addWidget(self.backListButton)

        self.saveListButton = QPushButton(formResult)
        self.saveListButton.setObjectName(u"saveListButton")
        self.saveListButton.setMaximumSize(QSize(120, 16777215))
        self.saveListButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Courier\";")

        self.horizontalLayout.addWidget(self.saveListButton)

        self.clearListButton = QPushButton(formResult)
        self.clearListButton.setObjectName(u"clearListButton")
        self.clearListButton.setMinimumSize(QSize(100, 0))
        self.clearListButton.setMaximumSize(QSize(120, 16777215))
        self.clearListButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Courier\";")

        self.horizontalLayout.addWidget(self.clearListButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(formResult)
        self.backListButton.clicked.connect(formResult.hide)

        QMetaObject.connectSlotsByName(formResult)
    # setupUi

    def retranslateUi(self, formResult):
        formResult.setWindowTitle(QCoreApplication.translate("formResult", u"Form", None))
        self.listTitle.setText(QCoreApplication.translate("formResult", u"RESULTADOS", None))
        self.backListButton.setText(QCoreApplication.translate("formResult", u"Voltar", None))
        self.saveListButton.setText(QCoreApplication.translate("formResult", u"Salvar", None))
        self.clearListButton.setText(QCoreApplication.translate("formResult", u"Limpar", None))
    # retranslateUi

