# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.ApplicationModal)
        Form.resize(324, 148)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"	\n"
"	font: 700 20pt \"Cascadia Mono\";\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.conform = QPushButton(Form)
        self.conform.setObjectName(u"conform")
        self.conform.setStyleSheet(u"QPushButton{\n"
"	border:2px dashed black;\n"
"	padding:5px;\n"
"	border-radius:10%;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border:2px dashed black;\n"
"	padding:5px;\n"
"	border-radius:10%;\n"
"	background-color: rgb(216, 255, 124);\n"
"}")

        self.verticalLayout.addWidget(self.conform, 0, Qt.AlignHCenter)


        self.retranslateUi(Form)
        self.conform.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"----", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.conform.setText(QCoreApplication.translate("Form", u"Conform", None))
    # retranslateUi

