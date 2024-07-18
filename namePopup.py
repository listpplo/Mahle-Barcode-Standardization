# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'namePopup.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import asset_rc

class Ui_getName(object):
    def setupUi(self, getName):
        if not getName.objectName():
            getName.setObjectName(u"getName")
        getName.setWindowModality(Qt.ApplicationModal)
        getName.resize(350, 202)
        self.horizontalLayout = QHBoxLayout(getName)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(getName)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"QPushButton{\n"
"	border-radius:10%;\n"
"	border:2px dashed black;\n"
"	padding:2px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.stationName = QLabel(self.frame)
        self.stationName.setObjectName(u"stationName")

        self.horizontalLayout_2.addWidget(self.stationName)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignRight|Qt.AlignTop)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	font: 700 14pt \"Segoe UI\";\n"
"}")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.create = QPushButton(self.frame_2)
        self.create.setObjectName(u"create")
        self.create.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: rgb(0, 255, 0);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/Assets/icons/icons8-add-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.create.setIcon(icon)
        self.create.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.create)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Assets/icons/icons8-cross-mark-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(40, 40))

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.groupBox)


        self.retranslateUi(getName)
        self.pushButton_2.clicked.connect(getName.close)

        QMetaObject.connectSlotsByName(getName)
    # setupUi

    def retranslateUi(self, getName):
        getName.setWindowTitle(QCoreApplication.translate("getName", u"Enter The Name of Recipe", None))
        self.groupBox.setTitle(QCoreApplication.translate("getName", u"Enter Name Of Recipe", None))
        self.label.setText(QCoreApplication.translate("getName", u"Station :", None))
        self.stationName.setText(QCoreApplication.translate("getName", u"TextLabel", None))
        self.create.setText(QCoreApplication.translate("getName", u"Create ", None))
        self.pushButton_2.setText(QCoreApplication.translate("getName", u"Cancel", None))
    # retranslateUi

