# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RecipeWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import asset_rc

class Ui_RecipipWindow(object):
    def setupUi(self, RecipipWindow):
        if not RecipipWindow.objectName():
            RecipipWindow.setObjectName(u"RecipipWindow")
        RecipipWindow.setWindowModality(Qt.ApplicationModal)
        RecipipWindow.resize(716, 482)
        self.verticalLayout = QVBoxLayout(RecipipWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(RecipipWindow)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"	font: 700 16pt \"Cascadia Mono\";\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.frame = QFrame(RecipipWindow)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"	border:2px dashed black;\n"
"	padding:4px;\n"
"	border-radius:20%;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover{\n"
"	border:2px dashed black;\n"
"	padding:4px;\n"
"	border-radius:20%;\n"
"	background-color: rgb(255, 245, 134);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/Icons/Assets/icons/icons8-add-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Assets/icons/icons8-refresh-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_10 = QPushButton(self.frame_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Assets/icons/icons8-delete-200.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon2)
        self.pushButton_10.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.pushButton_10)

        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Assets/icons/icons8-data-mapping-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon3)
        self.pushButton_7.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.pushButton_7)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Assets/icons/icons8-cross-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"	border:2px dashed black;\n"
"	padding:4px;\n"
"	border-radius:20%;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover{\n"
"	border:2px dashed black;\n"
"	padding:4px;\n"
"	border-radius:20%;\n"
"	background-color: rgb(255, 245, 134);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_9 = QPushButton(self.frame_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.frame_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_6)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.tableWidget_2 = QTableWidget(self.tab_2)
        if (self.tableWidget_2.columnCount() < 1):
            self.tableWidget_2.setColumnCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_4.addWidget(self.tableWidget_2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(RecipipWindow)
        self.pushButton_3.clicked.connect(RecipipWindow.close)
        self.pushButton_6.clicked.connect(RecipipWindow.close)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(RecipipWindow)
    # setupUi

    def retranslateUi(self, RecipipWindow):
        RecipipWindow.setWindowTitle(QCoreApplication.translate("RecipipWindow", u"Recipe Window", None))
        self.label.setText(QCoreApplication.translate("RecipipWindow", u"Recipie Window", None))
        self.pushButton.setText(QCoreApplication.translate("RecipipWindow", u"Add ", None))
        self.pushButton_2.setText(QCoreApplication.translate("RecipipWindow", u"Load", None))
        self.pushButton_10.setText(QCoreApplication.translate("RecipipWindow", u"Delete", None))
        self.pushButton_7.setText(QCoreApplication.translate("RecipipWindow", u"Mapping", None))
        self.pushButton_3.setText(QCoreApplication.translate("RecipipWindow", u"Close", None))
        self.label_2.setText(QCoreApplication.translate("RecipipWindow", u"* Please Select the below listed Recipe to load ", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("RecipipWindow", u"Recipe Name", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("RecipipWindow", u"Station 1", None))
        self.pushButton_4.setText(QCoreApplication.translate("RecipipWindow", u"Add ", None))
        self.pushButton_5.setText(QCoreApplication.translate("RecipipWindow", u"Load", None))
        self.pushButton_9.setText(QCoreApplication.translate("RecipipWindow", u"Delete", None))
        self.pushButton_8.setText(QCoreApplication.translate("RecipipWindow", u"Mapping", None))
        self.pushButton_6.setText(QCoreApplication.translate("RecipipWindow", u"Close", None))
        self.label_3.setText(QCoreApplication.translate("RecipipWindow", u"* Please Select the below listed Recipe to load ", None))
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("RecipipWindow", u"Recipe Name", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("RecipipWindow", u"Station 2", None))
    # retranslateUi

