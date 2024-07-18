# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

from loggingtextedit import LoggingTextEdit

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(784, 502)
        self.actionOpen_Recipie_Editor = QAction(MainWindow)
        self.actionOpen_Recipie_Editor.setObjectName(u"actionOpen_Recipie_Editor")
        self.actionConnection_Settings = QAction(MainWindow)
        self.actionConnection_Settings.setObjectName(u"actionConnection_Settings")
        self.actionAbout_Us = QAction(MainWindow)
        self.actionAbout_Us.setObjectName(u"actionAbout_Us")
        self.actionData = QAction(MainWindow)
        self.actionData.setObjectName(u"actionData")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(50, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_19 = QLabel(self.frame_3)
        self.label_19.setObjectName(u"label_19")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_19.setFont(font)

        self.verticalLayout_5.addWidget(self.label_19)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setMinimumSize(QSize(0, 80))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border:2px dashed black;\n"
"	background-color: rgb(255, 0, 0);\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_5.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_5.addWidget(self.pushButton_3)

        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.verticalLayout_5.addWidget(self.label_20)

        self.label_21 = QLabel(self.frame_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 80))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(216, 224, 255);\n"
"	border: 2px dashed black;\n"
"}")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_21)

        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.verticalLayout_5.addWidget(self.label_22)

        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 80))
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(216, 224, 255);\n"
"	border: 2px dashed black;\n"
"}")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_23)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Cascadia Mono"])
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setItalic(False)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel{\n"
"	font: 700 18pt \"Cascadia Mono\";\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        font3 = QFont()
        font3.setBold(False)
        font3.setUnderline(False)
        self.groupBox_3.setFont(font3)
        self.formLayout = QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName(u"formLayout")
        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_15)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setUnderline(False)
        self.label_16.setFont(font4)
        self.label_16.setStyleSheet(u"QLabel{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"}")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_16)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_2 = QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(6, QFormLayout.FieldRole, self.verticalSpacer_2)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_4)

        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font4)
        self.label_24.setStyleSheet(u"QLabel{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"}")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_24)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_31 = QGroupBox(self.frame)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.groupBox_31.setFont(font4)
        self.groupBox_31.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed balck;\n"
"}")
        self.groupBox_31.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_31)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.textEdit = LoggingTextEdit(self.groupBox_31)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit)


        self.verticalLayout.addWidget(self.groupBox_31)


        self.horizontalLayout.addWidget(self.frame)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"border:2px dashed black;")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	font: 700 18pt \"Cascadia Mono\";\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignTop)

        self.groupBox_4 = QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.formLayout_2 = QFormLayout(self.groupBox_4)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_17)

        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"QLabel{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"}")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.label_18)

        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_11)

        self.lineEdit_3 = QLineEdit(self.groupBox_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_12)

        self.lineEdit_4 = QLineEdit(self.groupBox_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setAlignment(Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(True)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lineEdit_4)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"QLabel{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"}")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.label_10)

        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_13)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout_2.setItem(6, QFormLayout.FieldRole, self.verticalSpacer_3)

        self.label_25 = QLabel(self.groupBox_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font4)
        self.label_25.setStyleSheet(u"QLabel{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"}")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.label_25)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.frame_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed balck;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.textEdit_2 = LoggingTextEdit(self.groupBox_5)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.textEdit_2)


        self.verticalLayout_2.addWidget(self.groupBox_5)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 784, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen_Recipie_Editor)
        self.menuFile.addAction(self.actionConnection_Settings)
        self.menuFile.addAction(self.actionData)
        self.menuHelp.addAction(self.actionAbout_Us)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_Recipie_Editor.setText(QCoreApplication.translate("MainWindow", u"Open Recipie Editor", None))
        self.actionConnection_Settings.setText(QCoreApplication.translate("MainWindow", u"Connection Settings", None))
        self.actionAbout_Us.setText(QCoreApplication.translate("MainWindow", u"About Us", None))
        self.actionData.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"PLC Status", None))
        self.pushButton.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"ST_01 QR Status", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"ST_01 QR Status", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Station-01", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Configuration :", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Current Recipe : ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Commad PLC: ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Barcode Recieved :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Printer :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Current Serial No. :", None))
        self.lineEdit.setText("")
        self.groupBox_31.setTitle(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Station-02", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Configuration :", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Current Recipe :", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Commad PLC: ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Barcode Recieved :", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Printer :", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Current Serial No. :", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

