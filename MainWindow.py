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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

from loggingtextedit import LoggingTextEdit

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(918, 710)
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
        self.pushButton_2.setStyleSheet(u"QPushButton:checked{\n"
"	background-color: rgb(85, 255, 0);\n"
"}")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)

        self.verticalLayout_5.addWidget(self.pushButton_2)

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
        font1 = QFont()
        font1.setFamilies([u"Cascadia Mono"])
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel{\n"
"	font: 700 18pt \"Cascadia Mono\";\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        font2 = QFont()
        font2.setBold(False)
        font2.setUnderline(False)
        self.groupBox_3.setFont(font2)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 15, 0, 2)
        self.frame_4 = QFrame(self.groupBox_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_4 = QGroupBox(self.frame_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed black;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 15, 9, 9)
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setUnderline(False)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(216, 224, 255);\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)


        self.horizontalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_6 = QGroupBox(self.frame_4)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed black;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 15, 9, 9)
        self.label_5 = QLabel(self.groupBox_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(216, 224, 255);\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)


        self.horizontalLayout_3.addWidget(self.groupBox_6)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.groupBox_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_7 = QGroupBox(self.frame_5)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed black;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 15, 9, -1)
        self.label_21 = QLabel(self.groupBox_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 0))
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(216, 224, 255);\n"
"}")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_21)


        self.horizontalLayout_5.addWidget(self.groupBox_7)

        self.groupBox_8 = QGroupBox(self.frame_5)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed black;\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, 15, 9, 9)
        self.label_8 = QLabel(self.groupBox_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(216, 224, 255);\n"
"}")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_8)


        self.horizontalLayout_5.addWidget(self.groupBox_8)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.groupBox_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 90))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.groupBox_9 = QGroupBox(self.frame_6)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.groupBox_9.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed black;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 15, 9, -1)
        self.label_24 = QLabel(self.groupBox_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 0))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setUnderline(False)
        self.label_24.setFont(font4)
        self.label_24.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(216, 224, 255);\n"
"}")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_24)


        self.horizontalLayout_6.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.frame_6)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(90, 0))
        self.groupBox_10.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed black;\n"
"}")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, 15, 9, 9)
        self.label_14 = QLabel(self.groupBox_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(216, 224, 255);\n"
"}")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_14)


        self.horizontalLayout_6.addWidget(self.groupBox_10, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_11 = QGroupBox(self.frame)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setFont(font2)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_12.setSpacing(3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 15, 0, 2)
        self.label_2 = QLabel(self.groupBox_11)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	font: 700 18pt \"Cascadia Mono\";\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_2)

        self.frame_10 = QFrame(self.groupBox_11)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.groupBox_18 = QGroupBox(self.frame_10)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed black;\n"
"}")
        self.horizontalLayout_17 = QHBoxLayout(self.groupBox_18)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 15, 9, 9)
        self.label_10 = QLabel(self.groupBox_18)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(216, 224, 255);\n"
"}")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_10)


        self.horizontalLayout_16.addWidget(self.groupBox_18)

        self.groupBox_19 = QGroupBox(self.frame_10)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed black;\n"
"}")
        self.horizontalLayout_18 = QHBoxLayout(self.groupBox_19)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(9, 15, 9, 9)
        self.label_11 = QLabel(self.groupBox_19)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(216, 224, 255);\n"
"}")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_11)


        self.horizontalLayout_16.addWidget(self.groupBox_19)


        self.verticalLayout_12.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.groupBox_11)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.groupBox_20 = QGroupBox(self.frame_11)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed black;\n"
"}")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 15, 9, -1)
        self.label_23 = QLabel(self.groupBox_20)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 0))
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(216, 224, 255);\n"
"}")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_23)


        self.horizontalLayout_19.addWidget(self.groupBox_20)

        self.groupBox_21 = QGroupBox(self.frame_11)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed black;\n"
"}")
        self.horizontalLayout_20 = QHBoxLayout(self.groupBox_21)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(9, 15, 9, 9)
        self.label_12 = QLabel(self.groupBox_21)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(216, 224, 255);\n"
"}")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_12)


        self.horizontalLayout_19.addWidget(self.groupBox_21)


        self.verticalLayout_12.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.groupBox_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 90))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.groupBox_22 = QGroupBox(self.frame_12)
        self.groupBox_22.setObjectName(u"groupBox_22")
        sizePolicy.setHeightForWidth(self.groupBox_22.sizePolicy().hasHeightForWidth())
        self.groupBox_22.setSizePolicy(sizePolicy)
        self.groupBox_22.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed black;\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_22)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 15, 9, -1)
        self.label_26 = QLabel(self.groupBox_22)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 0))
        self.label_26.setFont(font4)
        self.label_26.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(216, 224, 255);\n"
"}")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_26)


        self.horizontalLayout_21.addWidget(self.groupBox_22)

        self.groupBox_23 = QGroupBox(self.frame_12)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setMinimumSize(QSize(90, 0))
        self.groupBox_23.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed black;\n"
"}")
        self.horizontalLayout_22 = QHBoxLayout(self.groupBox_23)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(9, 15, 9, 9)
        self.label_16 = QLabel(self.groupBox_23)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(216, 224, 255);\n"
"}")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_16)


        self.horizontalLayout_21.addWidget(self.groupBox_23, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_12)


        self.verticalLayout.addWidget(self.groupBox_11)


        self.horizontalLayout.addWidget(self.frame)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"border:2px dashed black;")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.groupBox_31 = QGroupBox(self.centralwidget)
        self.groupBox_31.setObjectName(u"groupBox_31")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setUnderline(False)
        self.groupBox_31.setFont(font5)
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


        self.horizontalLayout.addWidget(self.groupBox_31)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 918, 22))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Station-01", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Configuration :", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Printer  : ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Current Recipe:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Current Serial No :", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"PLC Command :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Barcode Recieved :", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Status  :", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Configuration :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Station-02", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"Printer  : ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"Current Recipe:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Current Serial No :", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"PLC Command :", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Barcode Recieved :", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"Status  :", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.groupBox_31.setTitle(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

