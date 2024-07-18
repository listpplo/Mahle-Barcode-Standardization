# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConnectionWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QTimeEdit, QVBoxLayout, QWidget)
import asset_rc

class Ui_ConnectionWindow(object):
    def setupUi(self, ConnectionWindow):
        if not ConnectionWindow.objectName():
            ConnectionWindow.setObjectName(u"ConnectionWindow")
        ConnectionWindow.setWindowModality(Qt.WindowModal)
        ConnectionWindow.resize(551, 514)
        self.verticalLayout = QVBoxLayout(ConnectionWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(ConnectionWindow)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"	font: 700 16pt \"Cascadia Mono\";\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.tabWidget = QTabWidget(ConnectionWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.verticalLayout_2 = QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.tabWidgetPage1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.pushButton_8 = QPushButton(self.tabWidgetPage1)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(166, 0))
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	border-radius:20%;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:2px dashed black;\n"
"}\n"
"QPushButton::hover{\n"
"	border-radius:20%;\n"
"	background-color: rgb(30, 255, 68);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/Assets/icons/icons8-save-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.pushButton_8, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.tabWidgetPage1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(166, 0))
        self.pushButton_2.setMaximumSize(QSize(166, 16777215))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border-radius:20%;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:2px dashed black;\n"
"}\n"
"QPushButton::hover{\n"
"	border-radius:20%;\n"
"	background-color: rgb(255, 103, 106);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Assets/icons/icons8-cross-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(166, 0))
        self.pushButton.setMaximumSize(QSize(166, 16777215))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border-radius:20%;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:2px dashed black;\n"
"}\n"
"QPushButton::hover{\n"
"	border-radius:20%;\n"
"	background-color: rgb(30, 255, 68);\n"
"}")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_5 = QLineEdit(self.tab)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setAlignment(Qt.AlignCenter)
        self.lineEdit_5.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_5, 0, 2, 1, 1)

        self.lineEdit_9 = QLineEdit(self.tab)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_9, 4, 1, 1, 1)

        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_20 = QLabel(self.tab)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 7, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: rgb(71, 255, 20);\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: rgb(71, 255, 20);\n"
"}")
        self.pushButton_3.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton_3, 13, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.tab)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_8, 12, 1, 1, 1)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 12, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.tab)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setAlignment(Qt.AlignCenter)
        self.lineEdit_16.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_16, 8, 2, 1, 1)

        self.label_19 = QLabel(self.tab)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 6, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.tab)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setAlignment(Qt.AlignCenter)
        self.lineEdit_6.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_6, 1, 2, 1, 1)

        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.tab)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: rgb(255, 28, 89);\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color: rgb(255, 28, 89);\n"
"}")
        self.pushButton_6.setCheckable(False)

        self.gridLayout.addWidget(self.pushButton_6, 14, 1, 1, 1)

        self.lineEdit_17 = QLineEdit(self.tab)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setAlignment(Qt.AlignCenter)
        self.lineEdit_17.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_17, 9, 2, 1, 1)

        self.label_18 = QLabel(self.tab)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 2, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton::hover{\n"
"	background-color: rgb(71, 255, 20);\n"
"}\n"
"")
        self.pushButton_4.setCheckable(False)

        self.gridLayout.addWidget(self.pushButton_4, 14, 2, 1, 1)

        self.lineEdit_13 = QLineEdit(self.tab)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_13, 10, 1, 1, 1)

        self.label_17 = QLabel(self.tab)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 9, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.tab)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_15, 9, 1, 1, 1)

        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.lineEdit_21 = QLineEdit(self.tab)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setAlignment(Qt.AlignCenter)
        self.lineEdit_21.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_21, 6, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.tab)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.lineEdit_18 = QLineEdit(self.tab)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_18, 2, 1, 1, 1)

        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 10, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.tab)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_3, 0, 1, 1, 1)

        self.lineEdit_19 = QLineEdit(self.tab)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setAlignment(Qt.AlignCenter)
        self.lineEdit_19.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_19, 2, 2, 1, 1)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 11, 0, 1, 1)

        self.label_16 = QLabel(self.tab)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 8, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton::hover{\n"
"	background-color:  rgb(255, 23, 15);\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"	background-color:  rgb(255, 23, 15);\n"
"}")

        self.gridLayout.addWidget(self.pushButton_5, 13, 2, 1, 1)

        self.lineEdit_11 = QLineEdit(self.tab)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_11, 5, 1, 1, 1)

        self.lineEdit_12 = QLineEdit(self.tab)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setAlignment(Qt.AlignCenter)
        self.lineEdit_12.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_12, 5, 2, 1, 1)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.lineEdit_14 = QLineEdit(self.tab)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_14, 8, 1, 1, 1)

        self.lineEdit_22 = QLineEdit(self.tab)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_22, 7, 1, 1, 1)

        self.lineEdit_7 = QLineEdit(self.tab)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_7, 11, 1, 1, 1)

        self.lineEdit_20 = QLineEdit(self.tab)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_20, 6, 1, 1, 1)

        self.lineEdit_10 = QLineEdit(self.tab)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setAlignment(Qt.AlignCenter)
        self.lineEdit_10.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_10, 4, 2, 1, 1)

        self.label_21 = QLabel(self.tab)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 3, 0, 1, 1)

        self.lineEdit_23 = QLineEdit(self.tab)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lineEdit_23, 3, 1, 1, 1)

        self.lineEdit_24 = QLineEdit(self.tab)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setAlignment(Qt.AlignCenter)
        self.lineEdit_24.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_24, 7, 2, 1, 1)

        self.lineEdit_25 = QLineEdit(self.tab)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setAlignment(Qt.AlignCenter)
        self.lineEdit_25.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_25, 3, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 50))
        self.groupBox_4.setStyleSheet(u"QGroupBox{\n"
"	border:2px dashed black;\n"
"}\n"
"QLabel{\n"
"	border:none;\n"
"}")
        self.formLayout_2 = QFormLayout(self.groupBox_4)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.comboBox = QComboBox(self.groupBox_4)
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox)

        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_12)

        self.comboBox_2 = QComboBox(self.groupBox_4)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBox_2)

        self.frame_4 = QFrame(self.groupBox_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_10 = QPushButton(self.frame_4)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(70, 16777215))
        self.pushButton_10.setStyleSheet(u"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(99, 255, 56);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_10)

        self.pushButton_9 = QPushButton(self.frame_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(70, 16777215))
        self.pushButton_9.setStyleSheet(u"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(99, 255, 56);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_9)

        self.pushButton_11 = QPushButton(self.frame_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(70, 16777215))
        self.pushButton_11.setStyleSheet(u"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(99, 255, 56);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_11)


        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.frame_4)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout.addWidget(self.pushButton_7)


        self.verticalLayout_3.addWidget(self.frame)

        self.tableWidget = QTableWidget(self.tab_2)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_4 = QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.frame_5 = QFrame(self.tab_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(250, 0))
        self.frame_5.setStyleSheet(u"font: 700 12pt \"Cascadia Mono\";")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_5)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.timeEdit = QTimeEdit(self.frame_5)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.timeEdit)

        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_14)

        self.timeEdit_2 = QTimeEdit(self.frame_5)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.timeEdit_2)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_15)

        self.timeEdit_3 = QTimeEdit(self.frame_5)
        self.timeEdit_3.setObjectName(u"timeEdit_3")
        self.timeEdit_3.setAlignment(Qt.AlignCenter)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.timeEdit_3)


        self.verticalLayout_4.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.pushButton_12 = QPushButton(self.tab_3)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(166, 0))
        self.pushButton_12.setMaximumSize(QSize(166, 16777215))
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"	border-radius:20%;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:2px dashed black;\n"
"}\n"
"QPushButton::hover{\n"
"	border-radius:20%;\n"
"	background-color: rgb(30, 255, 68);\n"
"}")
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.pushButton_12, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(ConnectionWindow)
        self.pushButton_2.clicked["bool"].connect(ConnectionWindow.close)
        self.pushButton_5.clicked["bool"].connect(self.pushButton_3.click)
        self.pushButton_6.clicked["bool"].connect(ConnectionWindow.close)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(ConnectionWindow)
    # setupUi

    def retranslateUi(self, ConnectionWindow):
        ConnectionWindow.setWindowTitle(QCoreApplication.translate("ConnectionWindow", u"Connection Window", None))
        self.label.setText(QCoreApplication.translate("ConnectionWindow", u"Connection Settings Window", None))
        self.label_2.setText(QCoreApplication.translate("ConnectionWindow", u"IP   :", None))
        self.label_3.setText(QCoreApplication.translate("ConnectionWindow", u"Port :", None))
        self.pushButton_8.setText(QCoreApplication.translate("ConnectionWindow", u"Test", None))
        self.pushButton_2.setText(QCoreApplication.translate("ConnectionWindow", u"Cancel", None))
        self.pushButton.setText(QCoreApplication.translate("ConnectionWindow", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("ConnectionWindow", u"PLC Settings", None))
        self.label_7.setText(QCoreApplication.translate("ConnectionWindow", u"PLC Comamnd ST-02 :", None))
        self.label_20.setText(QCoreApplication.translate("ConnectionWindow", u"Response Reg. ST-02 :", None))
        self.pushButton_3.setText(QCoreApplication.translate("ConnectionWindow", u"Monitor", None))
        self.label_9.setText(QCoreApplication.translate("ConnectionWindow", u"PLC Timeout (s) : ", None))
        self.label_19.setText(QCoreApplication.translate("ConnectionWindow", u"Serial No. ST-02 :", None))
        self.label_6.setText(QCoreApplication.translate("ConnectionWindow", u"Print Count ST-02 :", None))
        self.pushButton_6.setText(QCoreApplication.translate("ConnectionWindow", u"Close", None))
        self.label_18.setText(QCoreApplication.translate("ConnectionWindow", u"Serial No. ST-01 :", None))
        self.pushButton_4.setText(QCoreApplication.translate("ConnectionWindow", u"Save", None))
        self.label_17.setText(QCoreApplication.translate("ConnectionWindow", u"Barcode St-02 :", None))
        self.label_5.setText(QCoreApplication.translate("ConnectionWindow", u"Print Count ST-01 :", None))
        self.label_10.setText(QCoreApplication.translate("ConnectionWindow", u"Heart Beat Server :", None))
        self.label_8.setText(QCoreApplication.translate("ConnectionWindow", u"Scan Time (s) :", None))
        self.label_16.setText(QCoreApplication.translate("ConnectionWindow", u"Barcode St-01 :", None))
        self.pushButton_5.setText(QCoreApplication.translate("ConnectionWindow", u"Stop", None))
        self.label_4.setText(QCoreApplication.translate("ConnectionWindow", u"PLC Comamnd ST-01 :", None))
        self.label_21.setText(QCoreApplication.translate("ConnectionWindow", u"Response Reg. ST-01 :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ConnectionWindow", u"Data Reg. Setting", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ConnectionWindow", u"Printer Settings for Stations", None))
        self.label_11.setText(QCoreApplication.translate("ConnectionWindow", u"ST-01 Printer :", None))
        self.label_12.setText(QCoreApplication.translate("ConnectionWindow", u"ST-02 Printer :", None))
        self.pushButton_10.setText(QCoreApplication.translate("ConnectionWindow", u"Save", None))
        self.pushButton_9.setText(QCoreApplication.translate("ConnectionWindow", u"Test 1", None))
        self.pushButton_11.setText(QCoreApplication.translate("ConnectionWindow", u"Test 2", None))
        self.pushButton_7.setText(QCoreApplication.translate("ConnectionWindow", u"View Installed Printer", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ConnectionWindow", u"Printer Name", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ConnectionWindow", u"Printer Page", None))
        self.label_13.setText(QCoreApplication.translate("ConnectionWindow", u"Shift A :", None))
        self.label_14.setText(QCoreApplication.translate("ConnectionWindow", u"Shift B :", None))
        self.label_15.setText(QCoreApplication.translate("ConnectionWindow", u"Shift C :", None))
        self.pushButton_12.setText(QCoreApplication.translate("ConnectionWindow", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("ConnectionWindow", u"Shift Settings", None))
    # retranslateUi

