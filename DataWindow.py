# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTabWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from dataframetable import DataFrameTable
import asset_rc

class Ui_Data_Win(object):
    def setupUi(self, Data_Win):
        if not Data_Win.objectName():
            Data_Win.setObjectName(u"Data_Win")
        Data_Win.resize(1012, 500)
        Data_Win.setMinimumSize(QSize(500, 300))
        self.verticalLayout = QVBoxLayout(Data_Win)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Data_Win)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabBar::tab {\n"
"    padding: 5px;\n"
"	font: 700 12pt \"Cascadia Code\";\n"
"	background-color: rgb(255, 255, 255);\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"	background-color:rgb(71, 255, 108);\n"
"    margin-bottom: -1px; \n"
"}\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.East)
        self.tabWidget.setIconSize(QSize(30, 30))
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_6 = QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.tab_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"QLabel{\n"
"	font: 700 14pt \"Cascadia Code\";\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	padding-left:50px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel{\n"
"	font: 700 14pt \"Cascadia Code\";\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_10)

        self.comboBox_2 = QComboBox(self.frame_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font)

        self.horizontalLayout_4.addWidget(self.comboBox_2)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel{\n"
"	font: 700 14pt \"Cascadia Code\";\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.dateEdit = QDateEdit(self.frame_3)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"QDateEdit{\n"
"	border:2px solid black;\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	padding-left:5px;\n"
"	height:30px;\n"
"	\n"
"	font: 600 12pt \"Cascadia Code SemiBold\";\n"
"	background-color: rgb(0, 255, 255);\n"
"}\n"
"QDateEdit::drop-down{\n"
"	image: url(:/Icons/Assets/icons/icons8-business-64.png);\n"
"	height:20px;\n"
"	width:20px;\n"
"	padding:2.5px;\n"
"}\n"
"QCalendarWidget QToolButton{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	icon-size: 20px;\n"
"	padding-bottom:10px;\n"
"}\n"
"")
        self.dateEdit.setAlignment(Qt.AlignCenter)
        self.dateEdit.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.dateEdit)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"QLabel{\n"
"	font: 700 14pt \"Cascadia Code\";\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.dateEdit_2 = QDateEdit(self.frame_3)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setStyleSheet(u"QDateEdit{\n"
"	border:2px solid black;\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius:10px;\n"
"	padding-left:20px;\n"
"	height:30px;\n"
"	\n"
"	font: 600 12pt \"Cascadia Code SemiBold\";\n"
"	background-color: rgb(0, 255, 255);\n"
"}\n"
"QDateEdit::drop-down{\n"
"	image: url(:/Icons/Assets/icons/icons8-business-64.png);\n"
"	height:20px;\n"
"	width:20px;\n"
"	padding:2.5px;\n"
"}\n"
"QCalendarWidget QToolButton{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"	icon-size: 20px;\n"
"	padding-bottom:10px;\n"
"}\n"
"")
        self.dateEdit_2.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.dateEdit_2)

        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	border-radius:20px;\n"
"	border:2px dashed black;\n"
"	height:30px;\n"
"	width:120px;\n"
"	background-color: rgb(39, 255, 111);\n"
"	\n"
"	font: 600 12pt \"Cascadia Mono SemiBold\";\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(239, 255, 64);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/Assets/icons/icons8-search-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	border-radius:20px;\n"
"	border:2px dashed black;\n"
"	height:30px;\n"
"	width:120px;\n"
"	background-color: rgb(39, 255, 111);\n"
"	\n"
"	font: 600 12pt \"Cascadia Mono SemiBold\";\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(239, 255, 64);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Assets/icons/icons8-menu-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_5)


        self.verticalLayout_6.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.tab_4)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_2 = DataFrameTable(self.frame_4)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"	font: 600 12pt \"Cascadia Mono SemiBold\";\n"
"}")
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSortingEnabled(True)

        self.verticalLayout_7.addWidget(self.tableWidget_2)


        self.verticalLayout_6.addWidget(self.frame_4)

        icon2 = QIcon()
        icon2.addFile(u":/Icons/Assets/icons/icons8-bar-chart-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Data_Win)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Data_Win)
    # setupUi

    def retranslateUi(self, Data_Win):
        Data_Win.setWindowTitle(QCoreApplication.translate("Data_Win", u"View Data Window", None))
        self.label_9.setText(QCoreApplication.translate("Data_Win", u"Station:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Data_Win", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Data_Win", u"2", None))

        self.label_10.setText(QCoreApplication.translate("Data_Win", u"DataType:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Data_Win", u"PrintData", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Data_Win", u"ScannedData", None))

        self.label_7.setText(QCoreApplication.translate("Data_Win", u"Start Date :", None))
        self.label_8.setText(QCoreApplication.translate("Data_Win", u"End Date :", None))
        self.pushButton_4.setText(QCoreApplication.translate("Data_Win", u"Fetch", None))
        self.pushButton_5.setText(QCoreApplication.translate("Data_Win", u"Export", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Data_Win", u"View", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Data_Win", u"Page", None))
    # retranslateUi

