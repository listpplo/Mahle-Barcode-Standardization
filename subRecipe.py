# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SubRecipeWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_SubWindow(object):
    def setupUi(self, SubWindow):
        if not SubWindow.objectName():
            SubWindow.setObjectName(u"SubWindow")
        SubWindow.setWindowModality(Qt.ApplicationModal)
        SubWindow.resize(800, 472)
        self.verticalLayout = QVBoxLayout(SubWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(SubWindow)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"	font: 700 16pt \"Cascadia Mono\";\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.tabWidget = QTabWidget(SubWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabBarAutoHide(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox = QCheckBox(self.tab)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 8, 3, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 3, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 3, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 7, 3, 1, 1)

        self.QR_arg5_value = QLineEdit(self.frame)
        self.QR_arg5_value.setObjectName(u"QR_arg5_value")

        self.gridLayout.addWidget(self.QR_arg5_value, 7, 2, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 7, 0, 1, 1)

        self.QR_arg3_value = QLineEdit(self.frame)
        self.QR_arg3_value.setObjectName(u"QR_arg3_value")

        self.gridLayout.addWidget(self.QR_arg3_value, 3, 2, 1, 1)

        self.QR_arg4_value = QLineEdit(self.frame)
        self.QR_arg4_value.setObjectName(u"QR_arg4_value")

        self.gridLayout.addWidget(self.QR_arg4_value, 5, 2, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 10, 3, 1, 1)

        self.QR_arg1_value = QLineEdit(self.frame)
        self.QR_arg1_value.setObjectName(u"QR_arg1_value")

        self.gridLayout.addWidget(self.QR_arg1_value, 0, 2, 1, 1)

        self.QR_arg6_value = QLineEdit(self.frame)
        self.QR_arg6_value.setObjectName(u"QR_arg6_value")

        self.gridLayout.addWidget(self.QR_arg6_value, 8, 2, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)

        self.QR_arg8_value = QLineEdit(self.frame)
        self.QR_arg8_value.setObjectName(u"QR_arg8_value")

        self.gridLayout.addWidget(self.QR_arg8_value, 10, 2, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 5, 3, 1, 1)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 9, 3, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 0, 3, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.QR_arg7_value = QLineEdit(self.frame)
        self.QR_arg7_value.setObjectName(u"QR_arg7_value")

        self.gridLayout.addWidget(self.QR_arg7_value, 9, 2, 1, 1)

        self.QR_arg2_value = QLineEdit(self.frame)
        self.QR_arg2_value.setObjectName(u"QR_arg2_value")

        self.gridLayout.addWidget(self.QR_arg2_value, 2, 2, 1, 1)

        self.QR_arg9_value = QLineEdit(self.frame)
        self.QR_arg9_value.setObjectName(u"QR_arg9_value")

        self.gridLayout.addWidget(self.QR_arg9_value, 0, 5, 1, 1)

        self.QR_arg10_value = QLineEdit(self.frame)
        self.QR_arg10_value.setObjectName(u"QR_arg10_value")

        self.gridLayout.addWidget(self.QR_arg10_value, 2, 5, 1, 1)

        self.QR_arg11_value = QLineEdit(self.frame)
        self.QR_arg11_value.setObjectName(u"QR_arg11_value")

        self.gridLayout.addWidget(self.QR_arg11_value, 3, 5, 1, 1)

        self.QR_arg12_value = QLineEdit(self.frame)
        self.QR_arg12_value.setObjectName(u"QR_arg12_value")

        self.gridLayout.addWidget(self.QR_arg12_value, 5, 5, 1, 1)

        self.QR_arg13_value = QLineEdit(self.frame)
        self.QR_arg13_value.setObjectName(u"QR_arg13_value")

        self.gridLayout.addWidget(self.QR_arg13_value, 7, 5, 1, 1)

        self.QR_arg14_value = QLineEdit(self.frame)
        self.QR_arg14_value.setObjectName(u"QR_arg14_value")

        self.gridLayout.addWidget(self.QR_arg14_value, 8, 5, 1, 1)

        self.QR_arg15_value = QLineEdit(self.frame)
        self.QR_arg15_value.setObjectName(u"QR_arg15_value")

        self.gridLayout.addWidget(self.QR_arg15_value, 9, 5, 1, 1)

        self.QR_arg16_value = QLineEdit(self.frame)
        self.QR_arg16_value.setObjectName(u"QR_arg16_value")

        self.gridLayout.addWidget(self.QR_arg16_value, 10, 5, 1, 1)

        self.QR_arg9 = QComboBox(self.frame)
        self.QR_arg9.addItem("")
        self.QR_arg9.addItem("")
        self.QR_arg9.addItem("")
        self.QR_arg9.addItem("")
        self.QR_arg9.addItem("")
        self.QR_arg9.addItem("")
        self.QR_arg9.setObjectName(u"QR_arg9")

        self.gridLayout.addWidget(self.QR_arg9, 0, 4, 1, 1)

        self.QR_arg10 = QComboBox(self.frame)
        self.QR_arg10.addItem("")
        self.QR_arg10.addItem("")
        self.QR_arg10.addItem("")
        self.QR_arg10.addItem("")
        self.QR_arg10.addItem("")
        self.QR_arg10.addItem("")
        self.QR_arg10.setObjectName(u"QR_arg10")

        self.gridLayout.addWidget(self.QR_arg10, 2, 4, 1, 1)

        self.QR_arg11 = QComboBox(self.frame)
        self.QR_arg11.addItem("")
        self.QR_arg11.addItem("")
        self.QR_arg11.addItem("")
        self.QR_arg11.addItem("")
        self.QR_arg11.addItem("")
        self.QR_arg11.addItem("")
        self.QR_arg11.setObjectName(u"QR_arg11")

        self.gridLayout.addWidget(self.QR_arg11, 3, 4, 1, 1)

        self.QR_arg12 = QComboBox(self.frame)
        self.QR_arg12.addItem("")
        self.QR_arg12.addItem("")
        self.QR_arg12.addItem("")
        self.QR_arg12.addItem("")
        self.QR_arg12.addItem("")
        self.QR_arg12.addItem("")
        self.QR_arg12.setObjectName(u"QR_arg12")

        self.gridLayout.addWidget(self.QR_arg12, 5, 4, 1, 1)

        self.QR_arg13 = QComboBox(self.frame)
        self.QR_arg13.addItem("")
        self.QR_arg13.addItem("")
        self.QR_arg13.addItem("")
        self.QR_arg13.addItem("")
        self.QR_arg13.addItem("")
        self.QR_arg13.addItem("")
        self.QR_arg13.setObjectName(u"QR_arg13")

        self.gridLayout.addWidget(self.QR_arg13, 7, 4, 1, 1)

        self.QR_arg14 = QComboBox(self.frame)
        self.QR_arg14.addItem("")
        self.QR_arg14.addItem("")
        self.QR_arg14.addItem("")
        self.QR_arg14.addItem("")
        self.QR_arg14.addItem("")
        self.QR_arg14.addItem("")
        self.QR_arg14.setObjectName(u"QR_arg14")

        self.gridLayout.addWidget(self.QR_arg14, 8, 4, 1, 1)

        self.QR_arg15 = QComboBox(self.frame)
        self.QR_arg15.addItem("")
        self.QR_arg15.addItem("")
        self.QR_arg15.addItem("")
        self.QR_arg15.addItem("")
        self.QR_arg15.addItem("")
        self.QR_arg15.addItem("")
        self.QR_arg15.setObjectName(u"QR_arg15")

        self.gridLayout.addWidget(self.QR_arg15, 9, 4, 1, 1)

        self.QR_arg16 = QComboBox(self.frame)
        self.QR_arg16.addItem("")
        self.QR_arg16.addItem("")
        self.QR_arg16.addItem("")
        self.QR_arg16.addItem("")
        self.QR_arg16.addItem("")
        self.QR_arg16.addItem("")
        self.QR_arg16.setObjectName(u"QR_arg16")

        self.gridLayout.addWidget(self.QR_arg16, 10, 4, 1, 1)

        self.QR_arg2 = QComboBox(self.frame)
        self.QR_arg2.addItem("")
        self.QR_arg2.addItem("")
        self.QR_arg2.addItem("")
        self.QR_arg2.addItem("")
        self.QR_arg2.addItem("")
        self.QR_arg2.addItem("")
        self.QR_arg2.setObjectName(u"QR_arg2")

        self.gridLayout.addWidget(self.QR_arg2, 2, 1, 1, 1)

        self.QR_arg1 = QComboBox(self.frame)
        self.QR_arg1.addItem("")
        self.QR_arg1.addItem("")
        self.QR_arg1.addItem("")
        self.QR_arg1.addItem("")
        self.QR_arg1.addItem("")
        self.QR_arg1.addItem("")
        self.QR_arg1.setObjectName(u"QR_arg1")

        self.gridLayout.addWidget(self.QR_arg1, 0, 1, 1, 1)

        self.QR_arg3 = QComboBox(self.frame)
        self.QR_arg3.addItem("")
        self.QR_arg3.addItem("")
        self.QR_arg3.addItem("")
        self.QR_arg3.addItem("")
        self.QR_arg3.addItem("")
        self.QR_arg3.addItem("")
        self.QR_arg3.setObjectName(u"QR_arg3")

        self.gridLayout.addWidget(self.QR_arg3, 3, 1, 1, 1)

        self.QR_arg4 = QComboBox(self.frame)
        self.QR_arg4.addItem("")
        self.QR_arg4.addItem("")
        self.QR_arg4.addItem("")
        self.QR_arg4.addItem("")
        self.QR_arg4.addItem("")
        self.QR_arg4.addItem("")
        self.QR_arg4.setObjectName(u"QR_arg4")

        self.gridLayout.addWidget(self.QR_arg4, 5, 1, 1, 1)

        self.QR_arg5 = QComboBox(self.frame)
        self.QR_arg5.addItem("")
        self.QR_arg5.addItem("")
        self.QR_arg5.addItem("")
        self.QR_arg5.addItem("")
        self.QR_arg5.addItem("")
        self.QR_arg5.addItem("")
        self.QR_arg5.setObjectName(u"QR_arg5")

        self.gridLayout.addWidget(self.QR_arg5, 7, 1, 1, 1)

        self.QR_arg6 = QComboBox(self.frame)
        self.QR_arg6.addItem("")
        self.QR_arg6.addItem("")
        self.QR_arg6.addItem("")
        self.QR_arg6.addItem("")
        self.QR_arg6.addItem("")
        self.QR_arg6.addItem("")
        self.QR_arg6.setObjectName(u"QR_arg6")

        self.gridLayout.addWidget(self.QR_arg6, 8, 1, 1, 1)

        self.QR_arg7 = QComboBox(self.frame)
        self.QR_arg7.addItem("")
        self.QR_arg7.addItem("")
        self.QR_arg7.addItem("")
        self.QR_arg7.addItem("")
        self.QR_arg7.addItem("")
        self.QR_arg7.addItem("")
        self.QR_arg7.setObjectName(u"QR_arg7")

        self.gridLayout.addWidget(self.QR_arg7, 9, 1, 1, 1)

        self.QR_arg8 = QComboBox(self.frame)
        self.QR_arg8.addItem("")
        self.QR_arg8.addItem("")
        self.QR_arg8.addItem("")
        self.QR_arg8.addItem("")
        self.QR_arg8.addItem("")
        self.QR_arg8.addItem("")
        self.QR_arg8.setObjectName(u"QR_arg8")

        self.gridLayout.addWidget(self.QR_arg8, 10, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_15 = QFrame(self.tab)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 50))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_148 = QLabel(self.frame_15)
        self.label_148.setObjectName(u"label_148")

        self.horizontalLayout_12.addWidget(self.label_148, 0, Qt.AlignRight)

        self.label_149 = QLabel(self.frame_15)
        self.label_149.setObjectName(u"label_149")

        self.horizontalLayout_12.addWidget(self.label_149, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_15)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignBottom)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_3 = QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox_2 = QCheckBox(self.tab_3)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_3.addWidget(self.checkBox_2)

        self.frame_4 = QFrame(self.tab_3)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_82 = QLabel(self.frame_4)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_6.addWidget(self.label_82, 8, 3, 1, 1)

        self.label_83 = QLabel(self.frame_4)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_6.addWidget(self.label_83, 9, 0, 1, 1)

        self.label_84 = QLabel(self.frame_4)
        self.label_84.setObjectName(u"label_84")

        self.gridLayout_6.addWidget(self.label_84, 2, 3, 1, 1)

        self.label_85 = QLabel(self.frame_4)
        self.label_85.setObjectName(u"label_85")

        self.gridLayout_6.addWidget(self.label_85, 3, 3, 1, 1)

        self.label_86 = QLabel(self.frame_4)
        self.label_86.setObjectName(u"label_86")

        self.gridLayout_6.addWidget(self.label_86, 3, 0, 1, 1)

        self.label_87 = QLabel(self.frame_4)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout_6.addWidget(self.label_87, 0, 0, 1, 1)

        self.label_88 = QLabel(self.frame_4)
        self.label_88.setObjectName(u"label_88")

        self.gridLayout_6.addWidget(self.label_88, 7, 3, 1, 1)

        self.Label1_arg5_value = QLineEdit(self.frame_4)
        self.Label1_arg5_value.setObjectName(u"Label1_arg5_value")

        self.gridLayout_6.addWidget(self.Label1_arg5_value, 7, 2, 1, 1)

        self.label_89 = QLabel(self.frame_4)
        self.label_89.setObjectName(u"label_89")

        self.gridLayout_6.addWidget(self.label_89, 2, 0, 1, 1)

        self.label_90 = QLabel(self.frame_4)
        self.label_90.setObjectName(u"label_90")

        self.gridLayout_6.addWidget(self.label_90, 7, 0, 1, 1)

        self.Label1_arg3_value = QLineEdit(self.frame_4)
        self.Label1_arg3_value.setObjectName(u"Label1_arg3_value")

        self.gridLayout_6.addWidget(self.Label1_arg3_value, 3, 2, 1, 1)

        self.Label1_arg4_value = QLineEdit(self.frame_4)
        self.Label1_arg4_value.setObjectName(u"Label1_arg4_value")

        self.gridLayout_6.addWidget(self.Label1_arg4_value, 5, 2, 1, 1)

        self.label_91 = QLabel(self.frame_4)
        self.label_91.setObjectName(u"label_91")

        self.gridLayout_6.addWidget(self.label_91, 10, 3, 1, 1)

        self.Label1_arg1_value = QLineEdit(self.frame_4)
        self.Label1_arg1_value.setObjectName(u"Label1_arg1_value")

        self.gridLayout_6.addWidget(self.Label1_arg1_value, 0, 2, 1, 1)

        self.Label1_arg6_value = QLineEdit(self.frame_4)
        self.Label1_arg6_value.setObjectName(u"Label1_arg6_value")

        self.gridLayout_6.addWidget(self.Label1_arg6_value, 8, 2, 1, 1)

        self.label_92 = QLabel(self.frame_4)
        self.label_92.setObjectName(u"label_92")

        self.gridLayout_6.addWidget(self.label_92, 8, 0, 1, 1)

        self.Label1_arg8_value = QLineEdit(self.frame_4)
        self.Label1_arg8_value.setObjectName(u"Label1_arg8_value")

        self.gridLayout_6.addWidget(self.Label1_arg8_value, 10, 2, 1, 1)

        self.label_93 = QLabel(self.frame_4)
        self.label_93.setObjectName(u"label_93")

        self.gridLayout_6.addWidget(self.label_93, 10, 0, 1, 1)

        self.label_94 = QLabel(self.frame_4)
        self.label_94.setObjectName(u"label_94")

        self.gridLayout_6.addWidget(self.label_94, 5, 3, 1, 1)

        self.label_95 = QLabel(self.frame_4)
        self.label_95.setObjectName(u"label_95")

        self.gridLayout_6.addWidget(self.label_95, 9, 3, 1, 1)

        self.label_96 = QLabel(self.frame_4)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_6.addWidget(self.label_96, 0, 3, 1, 1)

        self.label_97 = QLabel(self.frame_4)
        self.label_97.setObjectName(u"label_97")

        self.gridLayout_6.addWidget(self.label_97, 5, 0, 1, 1)

        self.Label1_arg7_value = QLineEdit(self.frame_4)
        self.Label1_arg7_value.setObjectName(u"Label1_arg7_value")

        self.gridLayout_6.addWidget(self.Label1_arg7_value, 9, 2, 1, 1)

        self.Label1_arg2_value = QLineEdit(self.frame_4)
        self.Label1_arg2_value.setObjectName(u"Label1_arg2_value")

        self.gridLayout_6.addWidget(self.Label1_arg2_value, 2, 2, 1, 1)

        self.Label1_arg9_value = QLineEdit(self.frame_4)
        self.Label1_arg9_value.setObjectName(u"Label1_arg9_value")

        self.gridLayout_6.addWidget(self.Label1_arg9_value, 0, 5, 1, 1)

        self.Label1_arg10_value = QLineEdit(self.frame_4)
        self.Label1_arg10_value.setObjectName(u"Label1_arg10_value")

        self.gridLayout_6.addWidget(self.Label1_arg10_value, 2, 5, 1, 1)

        self.Label1_arg11_value = QLineEdit(self.frame_4)
        self.Label1_arg11_value.setObjectName(u"Label1_arg11_value")

        self.gridLayout_6.addWidget(self.Label1_arg11_value, 3, 5, 1, 1)

        self.Label1_arg12_value = QLineEdit(self.frame_4)
        self.Label1_arg12_value.setObjectName(u"Label1_arg12_value")

        self.gridLayout_6.addWidget(self.Label1_arg12_value, 5, 5, 1, 1)

        self.Label1_arg13_value = QLineEdit(self.frame_4)
        self.Label1_arg13_value.setObjectName(u"Label1_arg13_value")

        self.gridLayout_6.addWidget(self.Label1_arg13_value, 7, 5, 1, 1)

        self.Label1_arg14_value = QLineEdit(self.frame_4)
        self.Label1_arg14_value.setObjectName(u"Label1_arg14_value")

        self.gridLayout_6.addWidget(self.Label1_arg14_value, 8, 5, 1, 1)

        self.Label1_arg15_value = QLineEdit(self.frame_4)
        self.Label1_arg15_value.setObjectName(u"Label1_arg15_value")

        self.gridLayout_6.addWidget(self.Label1_arg15_value, 9, 5, 1, 1)

        self.Label1_arg16_value = QLineEdit(self.frame_4)
        self.Label1_arg16_value.setObjectName(u"Label1_arg16_value")

        self.gridLayout_6.addWidget(self.Label1_arg16_value, 10, 5, 1, 1)

        self.Label1_arg9 = QComboBox(self.frame_4)
        self.Label1_arg9.addItem("")
        self.Label1_arg9.addItem("")
        self.Label1_arg9.addItem("")
        self.Label1_arg9.addItem("")
        self.Label1_arg9.addItem("")
        self.Label1_arg9.addItem("")
        self.Label1_arg9.setObjectName(u"Label1_arg9")

        self.gridLayout_6.addWidget(self.Label1_arg9, 0, 4, 1, 1)

        self.Label1_arg10 = QComboBox(self.frame_4)
        self.Label1_arg10.addItem("")
        self.Label1_arg10.addItem("")
        self.Label1_arg10.addItem("")
        self.Label1_arg10.addItem("")
        self.Label1_arg10.addItem("")
        self.Label1_arg10.addItem("")
        self.Label1_arg10.setObjectName(u"Label1_arg10")

        self.gridLayout_6.addWidget(self.Label1_arg10, 2, 4, 1, 1)

        self.Label1_arg11 = QComboBox(self.frame_4)
        self.Label1_arg11.addItem("")
        self.Label1_arg11.addItem("")
        self.Label1_arg11.addItem("")
        self.Label1_arg11.addItem("")
        self.Label1_arg11.addItem("")
        self.Label1_arg11.addItem("")
        self.Label1_arg11.setObjectName(u"Label1_arg11")

        self.gridLayout_6.addWidget(self.Label1_arg11, 3, 4, 1, 1)

        self.Label1_arg12 = QComboBox(self.frame_4)
        self.Label1_arg12.addItem("")
        self.Label1_arg12.addItem("")
        self.Label1_arg12.addItem("")
        self.Label1_arg12.addItem("")
        self.Label1_arg12.addItem("")
        self.Label1_arg12.addItem("")
        self.Label1_arg12.setObjectName(u"Label1_arg12")

        self.gridLayout_6.addWidget(self.Label1_arg12, 5, 4, 1, 1)

        self.Label1_arg13 = QComboBox(self.frame_4)
        self.Label1_arg13.addItem("")
        self.Label1_arg13.addItem("")
        self.Label1_arg13.addItem("")
        self.Label1_arg13.addItem("")
        self.Label1_arg13.addItem("")
        self.Label1_arg13.addItem("")
        self.Label1_arg13.setObjectName(u"Label1_arg13")

        self.gridLayout_6.addWidget(self.Label1_arg13, 7, 4, 1, 1)

        self.Label1_arg14 = QComboBox(self.frame_4)
        self.Label1_arg14.addItem("")
        self.Label1_arg14.addItem("")
        self.Label1_arg14.addItem("")
        self.Label1_arg14.addItem("")
        self.Label1_arg14.addItem("")
        self.Label1_arg14.addItem("")
        self.Label1_arg14.setObjectName(u"Label1_arg14")

        self.gridLayout_6.addWidget(self.Label1_arg14, 8, 4, 1, 1)

        self.Label1_arg15 = QComboBox(self.frame_4)
        self.Label1_arg15.addItem("")
        self.Label1_arg15.addItem("")
        self.Label1_arg15.addItem("")
        self.Label1_arg15.addItem("")
        self.Label1_arg15.addItem("")
        self.Label1_arg15.addItem("")
        self.Label1_arg15.setObjectName(u"Label1_arg15")

        self.gridLayout_6.addWidget(self.Label1_arg15, 9, 4, 1, 1)

        self.Label1_arg16 = QComboBox(self.frame_4)
        self.Label1_arg16.addItem("")
        self.Label1_arg16.addItem("")
        self.Label1_arg16.addItem("")
        self.Label1_arg16.addItem("")
        self.Label1_arg16.addItem("")
        self.Label1_arg16.addItem("")
        self.Label1_arg16.setObjectName(u"Label1_arg16")

        self.gridLayout_6.addWidget(self.Label1_arg16, 10, 4, 1, 1)

        self.Label1_arg2 = QComboBox(self.frame_4)
        self.Label1_arg2.addItem("")
        self.Label1_arg2.addItem("")
        self.Label1_arg2.addItem("")
        self.Label1_arg2.addItem("")
        self.Label1_arg2.addItem("")
        self.Label1_arg2.addItem("")
        self.Label1_arg2.setObjectName(u"Label1_arg2")

        self.gridLayout_6.addWidget(self.Label1_arg2, 2, 1, 1, 1)

        self.Label1_arg1 = QComboBox(self.frame_4)
        self.Label1_arg1.addItem("")
        self.Label1_arg1.addItem("")
        self.Label1_arg1.addItem("")
        self.Label1_arg1.addItem("")
        self.Label1_arg1.addItem("")
        self.Label1_arg1.addItem("")
        self.Label1_arg1.setObjectName(u"Label1_arg1")

        self.gridLayout_6.addWidget(self.Label1_arg1, 0, 1, 1, 1)

        self.Label1_arg3 = QComboBox(self.frame_4)
        self.Label1_arg3.addItem("")
        self.Label1_arg3.addItem("")
        self.Label1_arg3.addItem("")
        self.Label1_arg3.addItem("")
        self.Label1_arg3.addItem("")
        self.Label1_arg3.addItem("")
        self.Label1_arg3.setObjectName(u"Label1_arg3")

        self.gridLayout_6.addWidget(self.Label1_arg3, 3, 1, 1, 1)

        self.Label1_arg4 = QComboBox(self.frame_4)
        self.Label1_arg4.addItem("")
        self.Label1_arg4.addItem("")
        self.Label1_arg4.addItem("")
        self.Label1_arg4.addItem("")
        self.Label1_arg4.addItem("")
        self.Label1_arg4.addItem("")
        self.Label1_arg4.setObjectName(u"Label1_arg4")

        self.gridLayout_6.addWidget(self.Label1_arg4, 5, 1, 1, 1)

        self.Label1_arg5 = QComboBox(self.frame_4)
        self.Label1_arg5.addItem("")
        self.Label1_arg5.addItem("")
        self.Label1_arg5.addItem("")
        self.Label1_arg5.addItem("")
        self.Label1_arg5.addItem("")
        self.Label1_arg5.addItem("")
        self.Label1_arg5.setObjectName(u"Label1_arg5")

        self.gridLayout_6.addWidget(self.Label1_arg5, 7, 1, 1, 1)

        self.Label1_arg6 = QComboBox(self.frame_4)
        self.Label1_arg6.addItem("")
        self.Label1_arg6.addItem("")
        self.Label1_arg6.addItem("")
        self.Label1_arg6.addItem("")
        self.Label1_arg6.addItem("")
        self.Label1_arg6.addItem("")
        self.Label1_arg6.setObjectName(u"Label1_arg6")

        self.gridLayout_6.addWidget(self.Label1_arg6, 8, 1, 1, 1)

        self.Label1_arg7 = QComboBox(self.frame_4)
        self.Label1_arg7.addItem("")
        self.Label1_arg7.addItem("")
        self.Label1_arg7.addItem("")
        self.Label1_arg7.addItem("")
        self.Label1_arg7.addItem("")
        self.Label1_arg7.addItem("")
        self.Label1_arg7.setObjectName(u"Label1_arg7")

        self.gridLayout_6.addWidget(self.Label1_arg7, 9, 1, 1, 1)

        self.Label1_arg8 = QComboBox(self.frame_4)
        self.Label1_arg8.addItem("")
        self.Label1_arg8.addItem("")
        self.Label1_arg8.addItem("")
        self.Label1_arg8.addItem("")
        self.Label1_arg8.addItem("")
        self.Label1_arg8.addItem("")
        self.Label1_arg8.setObjectName(u"Label1_arg8")

        self.gridLayout_6.addWidget(self.Label1_arg8, 10, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_16 = QFrame(self.tab_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 50))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_150 = QLabel(self.frame_16)
        self.label_150.setObjectName(u"label_150")

        self.horizontalLayout_13.addWidget(self.label_150, 0, Qt.AlignRight)

        self.label_151 = QLabel(self.frame_16)
        self.label_151.setObjectName(u"label_151")

        self.horizontalLayout_13.addWidget(self.label_151, 0, Qt.AlignLeft)


        self.verticalLayout_3.addWidget(self.frame_16)

        self.frame_3 = QFrame(self.tab_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_16 = QPushButton(self.frame_3)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.horizontalLayout_6.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.frame_3)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.horizontalLayout_6.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.frame_3)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.horizontalLayout_6.addWidget(self.pushButton_18)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_4 = QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox_3 = QCheckBox(self.tab_4)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_4.addWidget(self.checkBox_3)

        self.frame_6 = QFrame(self.tab_4)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_98 = QLabel(self.frame_6)
        self.label_98.setObjectName(u"label_98")

        self.gridLayout_7.addWidget(self.label_98, 8, 3, 1, 1)

        self.label_99 = QLabel(self.frame_6)
        self.label_99.setObjectName(u"label_99")

        self.gridLayout_7.addWidget(self.label_99, 9, 0, 1, 1)

        self.label_100 = QLabel(self.frame_6)
        self.label_100.setObjectName(u"label_100")

        self.gridLayout_7.addWidget(self.label_100, 2, 3, 1, 1)

        self.label_101 = QLabel(self.frame_6)
        self.label_101.setObjectName(u"label_101")

        self.gridLayout_7.addWidget(self.label_101, 3, 3, 1, 1)

        self.label_102 = QLabel(self.frame_6)
        self.label_102.setObjectName(u"label_102")

        self.gridLayout_7.addWidget(self.label_102, 3, 0, 1, 1)

        self.label_103 = QLabel(self.frame_6)
        self.label_103.setObjectName(u"label_103")

        self.gridLayout_7.addWidget(self.label_103, 0, 0, 1, 1)

        self.label_104 = QLabel(self.frame_6)
        self.label_104.setObjectName(u"label_104")

        self.gridLayout_7.addWidget(self.label_104, 7, 3, 1, 1)

        self.Label2_arg5_value = QLineEdit(self.frame_6)
        self.Label2_arg5_value.setObjectName(u"Label2_arg5_value")

        self.gridLayout_7.addWidget(self.Label2_arg5_value, 7, 2, 1, 1)

        self.label_105 = QLabel(self.frame_6)
        self.label_105.setObjectName(u"label_105")

        self.gridLayout_7.addWidget(self.label_105, 2, 0, 1, 1)

        self.label_106 = QLabel(self.frame_6)
        self.label_106.setObjectName(u"label_106")

        self.gridLayout_7.addWidget(self.label_106, 7, 0, 1, 1)

        self.Label2_arg3_value = QLineEdit(self.frame_6)
        self.Label2_arg3_value.setObjectName(u"Label2_arg3_value")

        self.gridLayout_7.addWidget(self.Label2_arg3_value, 3, 2, 1, 1)

        self.Label2_arg4_value = QLineEdit(self.frame_6)
        self.Label2_arg4_value.setObjectName(u"Label2_arg4_value")

        self.gridLayout_7.addWidget(self.Label2_arg4_value, 5, 2, 1, 1)

        self.label_107 = QLabel(self.frame_6)
        self.label_107.setObjectName(u"label_107")

        self.gridLayout_7.addWidget(self.label_107, 10, 3, 1, 1)

        self.Label2_arg1_value = QLineEdit(self.frame_6)
        self.Label2_arg1_value.setObjectName(u"Label2_arg1_value")

        self.gridLayout_7.addWidget(self.Label2_arg1_value, 0, 2, 1, 1)

        self.Label2_arg6_value = QLineEdit(self.frame_6)
        self.Label2_arg6_value.setObjectName(u"Label2_arg6_value")

        self.gridLayout_7.addWidget(self.Label2_arg6_value, 8, 2, 1, 1)

        self.label_108 = QLabel(self.frame_6)
        self.label_108.setObjectName(u"label_108")

        self.gridLayout_7.addWidget(self.label_108, 8, 0, 1, 1)

        self.Label2_arg8_value = QLineEdit(self.frame_6)
        self.Label2_arg8_value.setObjectName(u"Label2_arg8_value")

        self.gridLayout_7.addWidget(self.Label2_arg8_value, 10, 2, 1, 1)

        self.label_109 = QLabel(self.frame_6)
        self.label_109.setObjectName(u"label_109")

        self.gridLayout_7.addWidget(self.label_109, 10, 0, 1, 1)

        self.label_110 = QLabel(self.frame_6)
        self.label_110.setObjectName(u"label_110")

        self.gridLayout_7.addWidget(self.label_110, 5, 3, 1, 1)

        self.label_111 = QLabel(self.frame_6)
        self.label_111.setObjectName(u"label_111")

        self.gridLayout_7.addWidget(self.label_111, 9, 3, 1, 1)

        self.label_112 = QLabel(self.frame_6)
        self.label_112.setObjectName(u"label_112")

        self.gridLayout_7.addWidget(self.label_112, 0, 3, 1, 1)

        self.label_113 = QLabel(self.frame_6)
        self.label_113.setObjectName(u"label_113")

        self.gridLayout_7.addWidget(self.label_113, 5, 0, 1, 1)

        self.Label2_arg7_value = QLineEdit(self.frame_6)
        self.Label2_arg7_value.setObjectName(u"Label2_arg7_value")

        self.gridLayout_7.addWidget(self.Label2_arg7_value, 9, 2, 1, 1)

        self.Label2_arg2_value = QLineEdit(self.frame_6)
        self.Label2_arg2_value.setObjectName(u"Label2_arg2_value")

        self.gridLayout_7.addWidget(self.Label2_arg2_value, 2, 2, 1, 1)

        self.Label2_arg9_value = QLineEdit(self.frame_6)
        self.Label2_arg9_value.setObjectName(u"Label2_arg9_value")

        self.gridLayout_7.addWidget(self.Label2_arg9_value, 0, 5, 1, 1)

        self.Label2_arg10_value = QLineEdit(self.frame_6)
        self.Label2_arg10_value.setObjectName(u"Label2_arg10_value")

        self.gridLayout_7.addWidget(self.Label2_arg10_value, 2, 5, 1, 1)

        self.Label2_arg11_value = QLineEdit(self.frame_6)
        self.Label2_arg11_value.setObjectName(u"Label2_arg11_value")

        self.gridLayout_7.addWidget(self.Label2_arg11_value, 3, 5, 1, 1)

        self.Label2_arg12_value = QLineEdit(self.frame_6)
        self.Label2_arg12_value.setObjectName(u"Label2_arg12_value")

        self.gridLayout_7.addWidget(self.Label2_arg12_value, 5, 5, 1, 1)

        self.Label2_arg13_value = QLineEdit(self.frame_6)
        self.Label2_arg13_value.setObjectName(u"Label2_arg13_value")

        self.gridLayout_7.addWidget(self.Label2_arg13_value, 7, 5, 1, 1)

        self.Label2_arg14_value = QLineEdit(self.frame_6)
        self.Label2_arg14_value.setObjectName(u"Label2_arg14_value")

        self.gridLayout_7.addWidget(self.Label2_arg14_value, 8, 5, 1, 1)

        self.Label2_arg15_value = QLineEdit(self.frame_6)
        self.Label2_arg15_value.setObjectName(u"Label2_arg15_value")

        self.gridLayout_7.addWidget(self.Label2_arg15_value, 9, 5, 1, 1)

        self.Label2_arg16_value = QLineEdit(self.frame_6)
        self.Label2_arg16_value.setObjectName(u"Label2_arg16_value")

        self.gridLayout_7.addWidget(self.Label2_arg16_value, 10, 5, 1, 1)

        self.Label2_arg9 = QComboBox(self.frame_6)
        self.Label2_arg9.addItem("")
        self.Label2_arg9.addItem("")
        self.Label2_arg9.addItem("")
        self.Label2_arg9.addItem("")
        self.Label2_arg9.addItem("")
        self.Label2_arg9.addItem("")
        self.Label2_arg9.setObjectName(u"Label2_arg9")

        self.gridLayout_7.addWidget(self.Label2_arg9, 0, 4, 1, 1)

        self.Label2_arg10 = QComboBox(self.frame_6)
        self.Label2_arg10.addItem("")
        self.Label2_arg10.addItem("")
        self.Label2_arg10.addItem("")
        self.Label2_arg10.addItem("")
        self.Label2_arg10.addItem("")
        self.Label2_arg10.addItem("")
        self.Label2_arg10.setObjectName(u"Label2_arg10")

        self.gridLayout_7.addWidget(self.Label2_arg10, 2, 4, 1, 1)

        self.Label2_arg11 = QComboBox(self.frame_6)
        self.Label2_arg11.addItem("")
        self.Label2_arg11.addItem("")
        self.Label2_arg11.addItem("")
        self.Label2_arg11.addItem("")
        self.Label2_arg11.addItem("")
        self.Label2_arg11.addItem("")
        self.Label2_arg11.setObjectName(u"Label2_arg11")

        self.gridLayout_7.addWidget(self.Label2_arg11, 3, 4, 1, 1)

        self.Label2_arg12 = QComboBox(self.frame_6)
        self.Label2_arg12.addItem("")
        self.Label2_arg12.addItem("")
        self.Label2_arg12.addItem("")
        self.Label2_arg12.addItem("")
        self.Label2_arg12.addItem("")
        self.Label2_arg12.addItem("")
        self.Label2_arg12.setObjectName(u"Label2_arg12")

        self.gridLayout_7.addWidget(self.Label2_arg12, 5, 4, 1, 1)

        self.Label2_arg13 = QComboBox(self.frame_6)
        self.Label2_arg13.addItem("")
        self.Label2_arg13.addItem("")
        self.Label2_arg13.addItem("")
        self.Label2_arg13.addItem("")
        self.Label2_arg13.addItem("")
        self.Label2_arg13.addItem("")
        self.Label2_arg13.setObjectName(u"Label2_arg13")

        self.gridLayout_7.addWidget(self.Label2_arg13, 7, 4, 1, 1)

        self.Label2_arg14 = QComboBox(self.frame_6)
        self.Label2_arg14.addItem("")
        self.Label2_arg14.addItem("")
        self.Label2_arg14.addItem("")
        self.Label2_arg14.addItem("")
        self.Label2_arg14.addItem("")
        self.Label2_arg14.addItem("")
        self.Label2_arg14.setObjectName(u"Label2_arg14")

        self.gridLayout_7.addWidget(self.Label2_arg14, 8, 4, 1, 1)

        self.Label2_arg15 = QComboBox(self.frame_6)
        self.Label2_arg15.addItem("")
        self.Label2_arg15.addItem("")
        self.Label2_arg15.addItem("")
        self.Label2_arg15.addItem("")
        self.Label2_arg15.addItem("")
        self.Label2_arg15.addItem("")
        self.Label2_arg15.setObjectName(u"Label2_arg15")

        self.gridLayout_7.addWidget(self.Label2_arg15, 9, 4, 1, 1)

        self.Label2_arg16 = QComboBox(self.frame_6)
        self.Label2_arg16.addItem("")
        self.Label2_arg16.addItem("")
        self.Label2_arg16.addItem("")
        self.Label2_arg16.addItem("")
        self.Label2_arg16.addItem("")
        self.Label2_arg16.addItem("")
        self.Label2_arg16.setObjectName(u"Label2_arg16")

        self.gridLayout_7.addWidget(self.Label2_arg16, 10, 4, 1, 1)

        self.Label2_arg2 = QComboBox(self.frame_6)
        self.Label2_arg2.addItem("")
        self.Label2_arg2.addItem("")
        self.Label2_arg2.addItem("")
        self.Label2_arg2.addItem("")
        self.Label2_arg2.addItem("")
        self.Label2_arg2.addItem("")
        self.Label2_arg2.setObjectName(u"Label2_arg2")

        self.gridLayout_7.addWidget(self.Label2_arg2, 2, 1, 1, 1)

        self.Label2_arg1 = QComboBox(self.frame_6)
        self.Label2_arg1.addItem("")
        self.Label2_arg1.addItem("")
        self.Label2_arg1.addItem("")
        self.Label2_arg1.addItem("")
        self.Label2_arg1.addItem("")
        self.Label2_arg1.addItem("")
        self.Label2_arg1.setObjectName(u"Label2_arg1")

        self.gridLayout_7.addWidget(self.Label2_arg1, 0, 1, 1, 1)

        self.Label2_arg3 = QComboBox(self.frame_6)
        self.Label2_arg3.addItem("")
        self.Label2_arg3.addItem("")
        self.Label2_arg3.addItem("")
        self.Label2_arg3.addItem("")
        self.Label2_arg3.addItem("")
        self.Label2_arg3.addItem("")
        self.Label2_arg3.setObjectName(u"Label2_arg3")

        self.gridLayout_7.addWidget(self.Label2_arg3, 3, 1, 1, 1)

        self.Label2_arg4 = QComboBox(self.frame_6)
        self.Label2_arg4.addItem("")
        self.Label2_arg4.addItem("")
        self.Label2_arg4.addItem("")
        self.Label2_arg4.addItem("")
        self.Label2_arg4.addItem("")
        self.Label2_arg4.addItem("")
        self.Label2_arg4.setObjectName(u"Label2_arg4")

        self.gridLayout_7.addWidget(self.Label2_arg4, 5, 1, 1, 1)

        self.Label2_arg5 = QComboBox(self.frame_6)
        self.Label2_arg5.addItem("")
        self.Label2_arg5.addItem("")
        self.Label2_arg5.addItem("")
        self.Label2_arg5.addItem("")
        self.Label2_arg5.addItem("")
        self.Label2_arg5.addItem("")
        self.Label2_arg5.setObjectName(u"Label2_arg5")

        self.gridLayout_7.addWidget(self.Label2_arg5, 7, 1, 1, 1)

        self.Label2_arg6 = QComboBox(self.frame_6)
        self.Label2_arg6.addItem("")
        self.Label2_arg6.addItem("")
        self.Label2_arg6.addItem("")
        self.Label2_arg6.addItem("")
        self.Label2_arg6.addItem("")
        self.Label2_arg6.addItem("")
        self.Label2_arg6.setObjectName(u"Label2_arg6")

        self.gridLayout_7.addWidget(self.Label2_arg6, 8, 1, 1, 1)

        self.Label2_arg7 = QComboBox(self.frame_6)
        self.Label2_arg7.addItem("")
        self.Label2_arg7.addItem("")
        self.Label2_arg7.addItem("")
        self.Label2_arg7.addItem("")
        self.Label2_arg7.addItem("")
        self.Label2_arg7.addItem("")
        self.Label2_arg7.setObjectName(u"Label2_arg7")

        self.gridLayout_7.addWidget(self.Label2_arg7, 9, 1, 1, 1)

        self.Label2_arg8 = QComboBox(self.frame_6)
        self.Label2_arg8.addItem("")
        self.Label2_arg8.addItem("")
        self.Label2_arg8.addItem("")
        self.Label2_arg8.addItem("")
        self.Label2_arg8.addItem("")
        self.Label2_arg8.addItem("")
        self.Label2_arg8.setObjectName(u"Label2_arg8")

        self.gridLayout_7.addWidget(self.Label2_arg8, 10, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_17 = QFrame(self.tab_4)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 50))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_152 = QLabel(self.frame_17)
        self.label_152.setObjectName(u"label_152")

        self.horizontalLayout_14.addWidget(self.label_152, 0, Qt.AlignRight)

        self.label_153 = QLabel(self.frame_17)
        self.label_153.setObjectName(u"label_153")

        self.horizontalLayout_14.addWidget(self.label_153, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.frame_17)

        self.frame_5 = QFrame(self.tab_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_19 = QPushButton(self.frame_5)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.horizontalLayout_7.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.frame_5)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_7.addWidget(self.pushButton_20)

        self.pushButton_21 = QPushButton(self.frame_5)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.horizontalLayout_7.addWidget(self.pushButton_21)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_5 = QVBoxLayout(self.tab_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.checkBox_4 = QCheckBox(self.tab_5)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_5.addWidget(self.checkBox_4)

        self.frame_8 = QFrame(self.tab_5)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_114 = QLabel(self.frame_8)
        self.label_114.setObjectName(u"label_114")

        self.gridLayout_8.addWidget(self.label_114, 8, 3, 1, 1)

        self.label_115 = QLabel(self.frame_8)
        self.label_115.setObjectName(u"label_115")

        self.gridLayout_8.addWidget(self.label_115, 9, 0, 1, 1)

        self.label_116 = QLabel(self.frame_8)
        self.label_116.setObjectName(u"label_116")

        self.gridLayout_8.addWidget(self.label_116, 2, 3, 1, 1)

        self.label_117 = QLabel(self.frame_8)
        self.label_117.setObjectName(u"label_117")

        self.gridLayout_8.addWidget(self.label_117, 3, 3, 1, 1)

        self.label_118 = QLabel(self.frame_8)
        self.label_118.setObjectName(u"label_118")

        self.gridLayout_8.addWidget(self.label_118, 3, 0, 1, 1)

        self.label_119 = QLabel(self.frame_8)
        self.label_119.setObjectName(u"label_119")

        self.gridLayout_8.addWidget(self.label_119, 0, 0, 1, 1)

        self.label_120 = QLabel(self.frame_8)
        self.label_120.setObjectName(u"label_120")

        self.gridLayout_8.addWidget(self.label_120, 7, 3, 1, 1)

        self.Label3_arg5_value = QLineEdit(self.frame_8)
        self.Label3_arg5_value.setObjectName(u"Label3_arg5_value")

        self.gridLayout_8.addWidget(self.Label3_arg5_value, 7, 2, 1, 1)

        self.label_121 = QLabel(self.frame_8)
        self.label_121.setObjectName(u"label_121")

        self.gridLayout_8.addWidget(self.label_121, 2, 0, 1, 1)

        self.label_122 = QLabel(self.frame_8)
        self.label_122.setObjectName(u"label_122")

        self.gridLayout_8.addWidget(self.label_122, 7, 0, 1, 1)

        self.Label3_arg3_value = QLineEdit(self.frame_8)
        self.Label3_arg3_value.setObjectName(u"Label3_arg3_value")

        self.gridLayout_8.addWidget(self.Label3_arg3_value, 3, 2, 1, 1)

        self.Label3_arg4_value = QLineEdit(self.frame_8)
        self.Label3_arg4_value.setObjectName(u"Label3_arg4_value")

        self.gridLayout_8.addWidget(self.Label3_arg4_value, 5, 2, 1, 1)

        self.label_123 = QLabel(self.frame_8)
        self.label_123.setObjectName(u"label_123")

        self.gridLayout_8.addWidget(self.label_123, 10, 3, 1, 1)

        self.Label3_arg1_value = QLineEdit(self.frame_8)
        self.Label3_arg1_value.setObjectName(u"Label3_arg1_value")

        self.gridLayout_8.addWidget(self.Label3_arg1_value, 0, 2, 1, 1)

        self.Label3_arg6_value = QLineEdit(self.frame_8)
        self.Label3_arg6_value.setObjectName(u"Label3_arg6_value")

        self.gridLayout_8.addWidget(self.Label3_arg6_value, 8, 2, 1, 1)

        self.label_124 = QLabel(self.frame_8)
        self.label_124.setObjectName(u"label_124")

        self.gridLayout_8.addWidget(self.label_124, 8, 0, 1, 1)

        self.Label3_arg8_value = QLineEdit(self.frame_8)
        self.Label3_arg8_value.setObjectName(u"Label3_arg8_value")

        self.gridLayout_8.addWidget(self.Label3_arg8_value, 10, 2, 1, 1)

        self.label_125 = QLabel(self.frame_8)
        self.label_125.setObjectName(u"label_125")

        self.gridLayout_8.addWidget(self.label_125, 10, 0, 1, 1)

        self.label_126 = QLabel(self.frame_8)
        self.label_126.setObjectName(u"label_126")

        self.gridLayout_8.addWidget(self.label_126, 5, 3, 1, 1)

        self.label_127 = QLabel(self.frame_8)
        self.label_127.setObjectName(u"label_127")

        self.gridLayout_8.addWidget(self.label_127, 9, 3, 1, 1)

        self.label_128 = QLabel(self.frame_8)
        self.label_128.setObjectName(u"label_128")

        self.gridLayout_8.addWidget(self.label_128, 0, 3, 1, 1)

        self.label_129 = QLabel(self.frame_8)
        self.label_129.setObjectName(u"label_129")

        self.gridLayout_8.addWidget(self.label_129, 5, 0, 1, 1)

        self.Label3_arg7_value = QLineEdit(self.frame_8)
        self.Label3_arg7_value.setObjectName(u"Label3_arg7_value")

        self.gridLayout_8.addWidget(self.Label3_arg7_value, 9, 2, 1, 1)

        self.Label3_arg2_value = QLineEdit(self.frame_8)
        self.Label3_arg2_value.setObjectName(u"Label3_arg2_value")

        self.gridLayout_8.addWidget(self.Label3_arg2_value, 2, 2, 1, 1)

        self.Label3_arg9_value = QLineEdit(self.frame_8)
        self.Label3_arg9_value.setObjectName(u"Label3_arg9_value")

        self.gridLayout_8.addWidget(self.Label3_arg9_value, 0, 5, 1, 1)

        self.Label3_arg10_value = QLineEdit(self.frame_8)
        self.Label3_arg10_value.setObjectName(u"Label3_arg10_value")

        self.gridLayout_8.addWidget(self.Label3_arg10_value, 2, 5, 1, 1)

        self.Label3_arg11_value = QLineEdit(self.frame_8)
        self.Label3_arg11_value.setObjectName(u"Label3_arg11_value")

        self.gridLayout_8.addWidget(self.Label3_arg11_value, 3, 5, 1, 1)

        self.Label3_arg12_value = QLineEdit(self.frame_8)
        self.Label3_arg12_value.setObjectName(u"Label3_arg12_value")

        self.gridLayout_8.addWidget(self.Label3_arg12_value, 5, 5, 1, 1)

        self.Label3_arg13_value = QLineEdit(self.frame_8)
        self.Label3_arg13_value.setObjectName(u"Label3_arg13_value")

        self.gridLayout_8.addWidget(self.Label3_arg13_value, 7, 5, 1, 1)

        self.Label3_arg14_value = QLineEdit(self.frame_8)
        self.Label3_arg14_value.setObjectName(u"Label3_arg14_value")

        self.gridLayout_8.addWidget(self.Label3_arg14_value, 8, 5, 1, 1)

        self.Label3_arg15_value = QLineEdit(self.frame_8)
        self.Label3_arg15_value.setObjectName(u"Label3_arg15_value")

        self.gridLayout_8.addWidget(self.Label3_arg15_value, 9, 5, 1, 1)

        self.Label3_arg16_value = QLineEdit(self.frame_8)
        self.Label3_arg16_value.setObjectName(u"Label3_arg16_value")

        self.gridLayout_8.addWidget(self.Label3_arg16_value, 10, 5, 1, 1)

        self.Label3_arg9 = QComboBox(self.frame_8)
        self.Label3_arg9.addItem("")
        self.Label3_arg9.addItem("")
        self.Label3_arg9.addItem("")
        self.Label3_arg9.addItem("")
        self.Label3_arg9.addItem("")
        self.Label3_arg9.addItem("")
        self.Label3_arg9.setObjectName(u"Label3_arg9")

        self.gridLayout_8.addWidget(self.Label3_arg9, 0, 4, 1, 1)

        self.Label3_arg10 = QComboBox(self.frame_8)
        self.Label3_arg10.addItem("")
        self.Label3_arg10.addItem("")
        self.Label3_arg10.addItem("")
        self.Label3_arg10.addItem("")
        self.Label3_arg10.addItem("")
        self.Label3_arg10.addItem("")
        self.Label3_arg10.setObjectName(u"Label3_arg10")

        self.gridLayout_8.addWidget(self.Label3_arg10, 2, 4, 1, 1)

        self.Label3_arg11 = QComboBox(self.frame_8)
        self.Label3_arg11.addItem("")
        self.Label3_arg11.addItem("")
        self.Label3_arg11.addItem("")
        self.Label3_arg11.addItem("")
        self.Label3_arg11.addItem("")
        self.Label3_arg11.addItem("")
        self.Label3_arg11.setObjectName(u"Label3_arg11")

        self.gridLayout_8.addWidget(self.Label3_arg11, 3, 4, 1, 1)

        self.Label3_arg12 = QComboBox(self.frame_8)
        self.Label3_arg12.addItem("")
        self.Label3_arg12.addItem("")
        self.Label3_arg12.addItem("")
        self.Label3_arg12.addItem("")
        self.Label3_arg12.addItem("")
        self.Label3_arg12.addItem("")
        self.Label3_arg12.setObjectName(u"Label3_arg12")

        self.gridLayout_8.addWidget(self.Label3_arg12, 5, 4, 1, 1)

        self.Label3_arg13 = QComboBox(self.frame_8)
        self.Label3_arg13.addItem("")
        self.Label3_arg13.addItem("")
        self.Label3_arg13.addItem("")
        self.Label3_arg13.addItem("")
        self.Label3_arg13.addItem("")
        self.Label3_arg13.addItem("")
        self.Label3_arg13.setObjectName(u"Label3_arg13")

        self.gridLayout_8.addWidget(self.Label3_arg13, 7, 4, 1, 1)

        self.Label3_arg14 = QComboBox(self.frame_8)
        self.Label3_arg14.addItem("")
        self.Label3_arg14.addItem("")
        self.Label3_arg14.addItem("")
        self.Label3_arg14.addItem("")
        self.Label3_arg14.addItem("")
        self.Label3_arg14.addItem("")
        self.Label3_arg14.setObjectName(u"Label3_arg14")

        self.gridLayout_8.addWidget(self.Label3_arg14, 8, 4, 1, 1)

        self.Label3_arg15 = QComboBox(self.frame_8)
        self.Label3_arg15.addItem("")
        self.Label3_arg15.addItem("")
        self.Label3_arg15.addItem("")
        self.Label3_arg15.addItem("")
        self.Label3_arg15.addItem("")
        self.Label3_arg15.addItem("")
        self.Label3_arg15.setObjectName(u"Label3_arg15")

        self.gridLayout_8.addWidget(self.Label3_arg15, 9, 4, 1, 1)

        self.Label3_arg16 = QComboBox(self.frame_8)
        self.Label3_arg16.addItem("")
        self.Label3_arg16.addItem("")
        self.Label3_arg16.addItem("")
        self.Label3_arg16.addItem("")
        self.Label3_arg16.addItem("")
        self.Label3_arg16.addItem("")
        self.Label3_arg16.setObjectName(u"Label3_arg16")

        self.gridLayout_8.addWidget(self.Label3_arg16, 10, 4, 1, 1)

        self.Label3_arg2 = QComboBox(self.frame_8)
        self.Label3_arg2.addItem("")
        self.Label3_arg2.addItem("")
        self.Label3_arg2.addItem("")
        self.Label3_arg2.addItem("")
        self.Label3_arg2.addItem("")
        self.Label3_arg2.addItem("")
        self.Label3_arg2.setObjectName(u"Label3_arg2")

        self.gridLayout_8.addWidget(self.Label3_arg2, 2, 1, 1, 1)

        self.Label3_arg1 = QComboBox(self.frame_8)
        self.Label3_arg1.addItem("")
        self.Label3_arg1.addItem("")
        self.Label3_arg1.addItem("")
        self.Label3_arg1.addItem("")
        self.Label3_arg1.addItem("")
        self.Label3_arg1.addItem("")
        self.Label3_arg1.setObjectName(u"Label3_arg1")

        self.gridLayout_8.addWidget(self.Label3_arg1, 0, 1, 1, 1)

        self.Label3_arg3 = QComboBox(self.frame_8)
        self.Label3_arg3.addItem("")
        self.Label3_arg3.addItem("")
        self.Label3_arg3.addItem("")
        self.Label3_arg3.addItem("")
        self.Label3_arg3.addItem("")
        self.Label3_arg3.addItem("")
        self.Label3_arg3.setObjectName(u"Label3_arg3")

        self.gridLayout_8.addWidget(self.Label3_arg3, 3, 1, 1, 1)

        self.Label3_arg4 = QComboBox(self.frame_8)
        self.Label3_arg4.addItem("")
        self.Label3_arg4.addItem("")
        self.Label3_arg4.addItem("")
        self.Label3_arg4.addItem("")
        self.Label3_arg4.addItem("")
        self.Label3_arg4.addItem("")
        self.Label3_arg4.setObjectName(u"Label3_arg4")

        self.gridLayout_8.addWidget(self.Label3_arg4, 5, 1, 1, 1)

        self.Label3_arg5 = QComboBox(self.frame_8)
        self.Label3_arg5.addItem("")
        self.Label3_arg5.addItem("")
        self.Label3_arg5.addItem("")
        self.Label3_arg5.addItem("")
        self.Label3_arg5.addItem("")
        self.Label3_arg5.addItem("")
        self.Label3_arg5.setObjectName(u"Label3_arg5")

        self.gridLayout_8.addWidget(self.Label3_arg5, 7, 1, 1, 1)

        self.Label3_arg6 = QComboBox(self.frame_8)
        self.Label3_arg6.addItem("")
        self.Label3_arg6.addItem("")
        self.Label3_arg6.addItem("")
        self.Label3_arg6.addItem("")
        self.Label3_arg6.addItem("")
        self.Label3_arg6.addItem("")
        self.Label3_arg6.setObjectName(u"Label3_arg6")

        self.gridLayout_8.addWidget(self.Label3_arg6, 8, 1, 1, 1)

        self.Label3_arg7 = QComboBox(self.frame_8)
        self.Label3_arg7.addItem("")
        self.Label3_arg7.addItem("")
        self.Label3_arg7.addItem("")
        self.Label3_arg7.addItem("")
        self.Label3_arg7.addItem("")
        self.Label3_arg7.addItem("")
        self.Label3_arg7.setObjectName(u"Label3_arg7")

        self.gridLayout_8.addWidget(self.Label3_arg7, 9, 1, 1, 1)

        self.Label3_arg8 = QComboBox(self.frame_8)
        self.Label3_arg8.addItem("")
        self.Label3_arg8.addItem("")
        self.Label3_arg8.addItem("")
        self.Label3_arg8.addItem("")
        self.Label3_arg8.addItem("")
        self.Label3_arg8.addItem("")
        self.Label3_arg8.setObjectName(u"Label3_arg8")

        self.gridLayout_8.addWidget(self.Label3_arg8, 10, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.frame_18 = QFrame(self.tab_5)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 50))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_154 = QLabel(self.frame_18)
        self.label_154.setObjectName(u"label_154")

        self.horizontalLayout_15.addWidget(self.label_154, 0, Qt.AlignRight)

        self.label_155 = QLabel(self.frame_18)
        self.label_155.setObjectName(u"label_155")

        self.horizontalLayout_15.addWidget(self.label_155, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.frame_18)

        self.frame_7 = QFrame(self.tab_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_22 = QPushButton(self.frame_7)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.horizontalLayout_8.addWidget(self.pushButton_22)

        self.pushButton_24 = QPushButton(self.frame_7)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.horizontalLayout_8.addWidget(self.pushButton_24)

        self.pushButton_23 = QPushButton(self.frame_7)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.horizontalLayout_8.addWidget(self.pushButton_23)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_6 = QVBoxLayout(self.tab_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBox_5 = QCheckBox(self.tab_6)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_6.addWidget(self.checkBox_5)

        self.frame_10 = QFrame(self.tab_6)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_130 = QLabel(self.frame_10)
        self.label_130.setObjectName(u"label_130")

        self.gridLayout_9.addWidget(self.label_130, 8, 3, 1, 1)

        self.label_131 = QLabel(self.frame_10)
        self.label_131.setObjectName(u"label_131")

        self.gridLayout_9.addWidget(self.label_131, 9, 0, 1, 1)

        self.label_132 = QLabel(self.frame_10)
        self.label_132.setObjectName(u"label_132")

        self.gridLayout_9.addWidget(self.label_132, 2, 3, 1, 1)

        self.label_133 = QLabel(self.frame_10)
        self.label_133.setObjectName(u"label_133")

        self.gridLayout_9.addWidget(self.label_133, 3, 3, 1, 1)

        self.label_134 = QLabel(self.frame_10)
        self.label_134.setObjectName(u"label_134")

        self.gridLayout_9.addWidget(self.label_134, 3, 0, 1, 1)

        self.label_135 = QLabel(self.frame_10)
        self.label_135.setObjectName(u"label_135")

        self.gridLayout_9.addWidget(self.label_135, 0, 0, 1, 1)

        self.label_136 = QLabel(self.frame_10)
        self.label_136.setObjectName(u"label_136")

        self.gridLayout_9.addWidget(self.label_136, 7, 3, 1, 1)

        self.Label4_arg5_value = QLineEdit(self.frame_10)
        self.Label4_arg5_value.setObjectName(u"Label4_arg5_value")

        self.gridLayout_9.addWidget(self.Label4_arg5_value, 7, 2, 1, 1)

        self.label_137 = QLabel(self.frame_10)
        self.label_137.setObjectName(u"label_137")

        self.gridLayout_9.addWidget(self.label_137, 2, 0, 1, 1)

        self.label_138 = QLabel(self.frame_10)
        self.label_138.setObjectName(u"label_138")

        self.gridLayout_9.addWidget(self.label_138, 7, 0, 1, 1)

        self.Label4_arg3_value = QLineEdit(self.frame_10)
        self.Label4_arg3_value.setObjectName(u"Label4_arg3_value")

        self.gridLayout_9.addWidget(self.Label4_arg3_value, 3, 2, 1, 1)

        self.Label4_arg4_value = QLineEdit(self.frame_10)
        self.Label4_arg4_value.setObjectName(u"Label4_arg4_value")

        self.gridLayout_9.addWidget(self.Label4_arg4_value, 5, 2, 1, 1)

        self.label_139 = QLabel(self.frame_10)
        self.label_139.setObjectName(u"label_139")

        self.gridLayout_9.addWidget(self.label_139, 10, 3, 1, 1)

        self.Label4_arg1_value = QLineEdit(self.frame_10)
        self.Label4_arg1_value.setObjectName(u"Label4_arg1_value")

        self.gridLayout_9.addWidget(self.Label4_arg1_value, 0, 2, 1, 1)

        self.Label4_arg6_value = QLineEdit(self.frame_10)
        self.Label4_arg6_value.setObjectName(u"Label4_arg6_value")

        self.gridLayout_9.addWidget(self.Label4_arg6_value, 8, 2, 1, 1)

        self.label_140 = QLabel(self.frame_10)
        self.label_140.setObjectName(u"label_140")

        self.gridLayout_9.addWidget(self.label_140, 8, 0, 1, 1)

        self.Label4_arg8_value = QLineEdit(self.frame_10)
        self.Label4_arg8_value.setObjectName(u"Label4_arg8_value")

        self.gridLayout_9.addWidget(self.Label4_arg8_value, 10, 2, 1, 1)

        self.label_141 = QLabel(self.frame_10)
        self.label_141.setObjectName(u"label_141")

        self.gridLayout_9.addWidget(self.label_141, 10, 0, 1, 1)

        self.label_142 = QLabel(self.frame_10)
        self.label_142.setObjectName(u"label_142")

        self.gridLayout_9.addWidget(self.label_142, 5, 3, 1, 1)

        self.label_143 = QLabel(self.frame_10)
        self.label_143.setObjectName(u"label_143")

        self.gridLayout_9.addWidget(self.label_143, 9, 3, 1, 1)

        self.label_144 = QLabel(self.frame_10)
        self.label_144.setObjectName(u"label_144")

        self.gridLayout_9.addWidget(self.label_144, 0, 3, 1, 1)

        self.label_145 = QLabel(self.frame_10)
        self.label_145.setObjectName(u"label_145")

        self.gridLayout_9.addWidget(self.label_145, 5, 0, 1, 1)

        self.Label4_arg7_value = QLineEdit(self.frame_10)
        self.Label4_arg7_value.setObjectName(u"Label4_arg7_value")

        self.gridLayout_9.addWidget(self.Label4_arg7_value, 9, 2, 1, 1)

        self.Label4_arg2_value = QLineEdit(self.frame_10)
        self.Label4_arg2_value.setObjectName(u"Label4_arg2_value")

        self.gridLayout_9.addWidget(self.Label4_arg2_value, 2, 2, 1, 1)

        self.Label4_arg9_value = QLineEdit(self.frame_10)
        self.Label4_arg9_value.setObjectName(u"Label4_arg9_value")

        self.gridLayout_9.addWidget(self.Label4_arg9_value, 0, 5, 1, 1)

        self.Label4_arg10_value = QLineEdit(self.frame_10)
        self.Label4_arg10_value.setObjectName(u"Label4_arg10_value")

        self.gridLayout_9.addWidget(self.Label4_arg10_value, 2, 5, 1, 1)

        self.Label4_arg11_value = QLineEdit(self.frame_10)
        self.Label4_arg11_value.setObjectName(u"Label4_arg11_value")

        self.gridLayout_9.addWidget(self.Label4_arg11_value, 3, 5, 1, 1)

        self.Label4_arg12_value = QLineEdit(self.frame_10)
        self.Label4_arg12_value.setObjectName(u"Label4_arg12_value")

        self.gridLayout_9.addWidget(self.Label4_arg12_value, 5, 5, 1, 1)

        self.Label4_arg13_value = QLineEdit(self.frame_10)
        self.Label4_arg13_value.setObjectName(u"Label4_arg13_value")

        self.gridLayout_9.addWidget(self.Label4_arg13_value, 7, 5, 1, 1)

        self.Label4_arg14_value = QLineEdit(self.frame_10)
        self.Label4_arg14_value.setObjectName(u"Label4_arg14_value")

        self.gridLayout_9.addWidget(self.Label4_arg14_value, 8, 5, 1, 1)

        self.Label4_arg15_value = QLineEdit(self.frame_10)
        self.Label4_arg15_value.setObjectName(u"Label4_arg15_value")

        self.gridLayout_9.addWidget(self.Label4_arg15_value, 9, 5, 1, 1)

        self.Label4_arg16_value = QLineEdit(self.frame_10)
        self.Label4_arg16_value.setObjectName(u"Label4_arg16_value")

        self.gridLayout_9.addWidget(self.Label4_arg16_value, 10, 5, 1, 1)

        self.Label4_arg9 = QComboBox(self.frame_10)
        self.Label4_arg9.addItem("")
        self.Label4_arg9.addItem("")
        self.Label4_arg9.addItem("")
        self.Label4_arg9.addItem("")
        self.Label4_arg9.addItem("")
        self.Label4_arg9.addItem("")
        self.Label4_arg9.setObjectName(u"Label4_arg9")

        self.gridLayout_9.addWidget(self.Label4_arg9, 0, 4, 1, 1)

        self.Label4_arg10 = QComboBox(self.frame_10)
        self.Label4_arg10.addItem("")
        self.Label4_arg10.addItem("")
        self.Label4_arg10.addItem("")
        self.Label4_arg10.addItem("")
        self.Label4_arg10.addItem("")
        self.Label4_arg10.addItem("")
        self.Label4_arg10.setObjectName(u"Label4_arg10")

        self.gridLayout_9.addWidget(self.Label4_arg10, 2, 4, 1, 1)

        self.Label4_arg11 = QComboBox(self.frame_10)
        self.Label4_arg11.addItem("")
        self.Label4_arg11.addItem("")
        self.Label4_arg11.addItem("")
        self.Label4_arg11.addItem("")
        self.Label4_arg11.addItem("")
        self.Label4_arg11.addItem("")
        self.Label4_arg11.setObjectName(u"Label4_arg11")

        self.gridLayout_9.addWidget(self.Label4_arg11, 3, 4, 1, 1)

        self.Label4_arg12 = QComboBox(self.frame_10)
        self.Label4_arg12.addItem("")
        self.Label4_arg12.addItem("")
        self.Label4_arg12.addItem("")
        self.Label4_arg12.addItem("")
        self.Label4_arg12.addItem("")
        self.Label4_arg12.addItem("")
        self.Label4_arg12.setObjectName(u"Label4_arg12")

        self.gridLayout_9.addWidget(self.Label4_arg12, 5, 4, 1, 1)

        self.Label4_arg13 = QComboBox(self.frame_10)
        self.Label4_arg13.addItem("")
        self.Label4_arg13.addItem("")
        self.Label4_arg13.addItem("")
        self.Label4_arg13.addItem("")
        self.Label4_arg13.addItem("")
        self.Label4_arg13.addItem("")
        self.Label4_arg13.setObjectName(u"Label4_arg13")

        self.gridLayout_9.addWidget(self.Label4_arg13, 7, 4, 1, 1)

        self.Label4_arg14 = QComboBox(self.frame_10)
        self.Label4_arg14.addItem("")
        self.Label4_arg14.addItem("")
        self.Label4_arg14.addItem("")
        self.Label4_arg14.addItem("")
        self.Label4_arg14.addItem("")
        self.Label4_arg14.addItem("")
        self.Label4_arg14.setObjectName(u"Label4_arg14")

        self.gridLayout_9.addWidget(self.Label4_arg14, 8, 4, 1, 1)

        self.Label4_arg15 = QComboBox(self.frame_10)
        self.Label4_arg15.addItem("")
        self.Label4_arg15.addItem("")
        self.Label4_arg15.addItem("")
        self.Label4_arg15.addItem("")
        self.Label4_arg15.addItem("")
        self.Label4_arg15.addItem("")
        self.Label4_arg15.setObjectName(u"Label4_arg15")

        self.gridLayout_9.addWidget(self.Label4_arg15, 9, 4, 1, 1)

        self.Label4_arg16 = QComboBox(self.frame_10)
        self.Label4_arg16.addItem("")
        self.Label4_arg16.addItem("")
        self.Label4_arg16.addItem("")
        self.Label4_arg16.addItem("")
        self.Label4_arg16.addItem("")
        self.Label4_arg16.addItem("")
        self.Label4_arg16.setObjectName(u"Label4_arg16")

        self.gridLayout_9.addWidget(self.Label4_arg16, 10, 4, 1, 1)

        self.Label4_arg2 = QComboBox(self.frame_10)
        self.Label4_arg2.addItem("")
        self.Label4_arg2.addItem("")
        self.Label4_arg2.addItem("")
        self.Label4_arg2.addItem("")
        self.Label4_arg2.addItem("")
        self.Label4_arg2.addItem("")
        self.Label4_arg2.setObjectName(u"Label4_arg2")

        self.gridLayout_9.addWidget(self.Label4_arg2, 2, 1, 1, 1)

        self.Label4_arg1 = QComboBox(self.frame_10)
        self.Label4_arg1.addItem("")
        self.Label4_arg1.addItem("")
        self.Label4_arg1.addItem("")
        self.Label4_arg1.addItem("")
        self.Label4_arg1.addItem("")
        self.Label4_arg1.addItem("")
        self.Label4_arg1.setObjectName(u"Label4_arg1")

        self.gridLayout_9.addWidget(self.Label4_arg1, 0, 1, 1, 1)

        self.Label4_arg3 = QComboBox(self.frame_10)
        self.Label4_arg3.addItem("")
        self.Label4_arg3.addItem("")
        self.Label4_arg3.addItem("")
        self.Label4_arg3.addItem("")
        self.Label4_arg3.addItem("")
        self.Label4_arg3.addItem("")
        self.Label4_arg3.setObjectName(u"Label4_arg3")

        self.gridLayout_9.addWidget(self.Label4_arg3, 3, 1, 1, 1)

        self.Label4_arg4 = QComboBox(self.frame_10)
        self.Label4_arg4.addItem("")
        self.Label4_arg4.addItem("")
        self.Label4_arg4.addItem("")
        self.Label4_arg4.addItem("")
        self.Label4_arg4.addItem("")
        self.Label4_arg4.addItem("")
        self.Label4_arg4.setObjectName(u"Label4_arg4")

        self.gridLayout_9.addWidget(self.Label4_arg4, 5, 1, 1, 1)

        self.Label4_arg5 = QComboBox(self.frame_10)
        self.Label4_arg5.addItem("")
        self.Label4_arg5.addItem("")
        self.Label4_arg5.addItem("")
        self.Label4_arg5.addItem("")
        self.Label4_arg5.addItem("")
        self.Label4_arg5.addItem("")
        self.Label4_arg5.setObjectName(u"Label4_arg5")

        self.gridLayout_9.addWidget(self.Label4_arg5, 7, 1, 1, 1)

        self.Label4_arg6 = QComboBox(self.frame_10)
        self.Label4_arg6.addItem("")
        self.Label4_arg6.addItem("")
        self.Label4_arg6.addItem("")
        self.Label4_arg6.addItem("")
        self.Label4_arg6.addItem("")
        self.Label4_arg6.addItem("")
        self.Label4_arg6.setObjectName(u"Label4_arg6")

        self.gridLayout_9.addWidget(self.Label4_arg6, 8, 1, 1, 1)

        self.Label4_arg7 = QComboBox(self.frame_10)
        self.Label4_arg7.addItem("")
        self.Label4_arg7.addItem("")
        self.Label4_arg7.addItem("")
        self.Label4_arg7.addItem("")
        self.Label4_arg7.addItem("")
        self.Label4_arg7.addItem("")
        self.Label4_arg7.setObjectName(u"Label4_arg7")

        self.gridLayout_9.addWidget(self.Label4_arg7, 9, 1, 1, 1)

        self.Label4_arg8 = QComboBox(self.frame_10)
        self.Label4_arg8.addItem("")
        self.Label4_arg8.addItem("")
        self.Label4_arg8.addItem("")
        self.Label4_arg8.addItem("")
        self.Label4_arg8.addItem("")
        self.Label4_arg8.addItem("")
        self.Label4_arg8.setObjectName(u"Label4_arg8")

        self.gridLayout_9.addWidget(self.Label4_arg8, 10, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.frame_10)

        self.frame_19 = QFrame(self.tab_6)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 50))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_156 = QLabel(self.frame_19)
        self.label_156.setObjectName(u"label_156")

        self.horizontalLayout_16.addWidget(self.label_156, 0, Qt.AlignRight)

        self.label_157 = QLabel(self.frame_19)
        self.label_157.setObjectName(u"label_157")

        self.horizontalLayout_16.addWidget(self.label_157, 0, Qt.AlignLeft)


        self.verticalLayout_6.addWidget(self.frame_19)

        self.frame_9 = QFrame(self.tab_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_25 = QPushButton(self.frame_9)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.horizontalLayout_9.addWidget(self.pushButton_25)

        self.pushButton_26 = QPushButton(self.frame_9)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.horizontalLayout_9.addWidget(self.pushButton_26)

        self.pushButton_27 = QPushButton(self.frame_9)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.horizontalLayout_9.addWidget(self.pushButton_27)


        self.verticalLayout_6.addWidget(self.frame_9)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.tab_2)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_13)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_3 = QGroupBox(self.frame_13)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_3 = QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_27 = QLabel(self.groupBox_3)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_27)

        self.label_29 = QLabel(self.groupBox_3)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_29)

        self.label_30 = QLabel(self.groupBox_3)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_30)

        self.label_28 = QLabel(self.groupBox_3)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_28)

        self.comboBox = QComboBox(self.groupBox_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.comboBox)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_2)

        self.doubleSpinBox_14 = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_14.setObjectName(u"doubleSpinBox_14")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_14)

        self.doubleSpinBox_15 = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_15.setObjectName(u"doubleSpinBox_15")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.doubleSpinBox_15)


        self.gridLayout_2.addWidget(self.groupBox_3, 0, 2, 1, 1)

        self.groupBox = QGroupBox(self.frame_13)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_19)

        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_20)

        self.label_21 = QLabel(self.groupBox)
        self.label_21.setObjectName(u"label_21")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_21)

        self.label_22 = QLabel(self.groupBox)
        self.label_22.setObjectName(u"label_22")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_22)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_6)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_7)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_8)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.doubleSpinBox_9)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.frame_13)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.formLayout_5 = QFormLayout(self.groupBox_4)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_35 = QLabel(self.groupBox_4)
        self.label_35.setObjectName(u"label_35")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_35)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_3)

        self.label_36 = QLabel(self.groupBox_4)
        self.label_36.setObjectName(u"label_36")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_36)

        self.comboBox_2 = QComboBox(self.groupBox_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.comboBox_2)

        self.label_37 = QLabel(self.groupBox_4)
        self.label_37.setObjectName(u"label_37")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_37)

        self.doubleSpinBox_16 = QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_16.setObjectName(u"doubleSpinBox_16")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_16)

        self.label_38 = QLabel(self.groupBox_4)
        self.label_38.setObjectName(u"label_38")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_38)

        self.doubleSpinBox_17 = QDoubleSpinBox(self.groupBox_4)
        self.doubleSpinBox_17.setObjectName(u"doubleSpinBox_17")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.doubleSpinBox_17)


        self.gridLayout_2.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.frame_13)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.formLayout_7 = QFormLayout(self.groupBox_6)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_43 = QLabel(self.groupBox_6)
        self.label_43.setObjectName(u"label_43")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_43)

        self.label_44 = QLabel(self.groupBox_6)
        self.label_44.setObjectName(u"label_44")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_44)

        self.label_45 = QLabel(self.groupBox_6)
        self.label_45.setObjectName(u"label_45")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.label_45)

        self.label_46 = QLabel(self.groupBox_6)
        self.label_46.setObjectName(u"label_46")

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.label_46)

        self.comboBox_4 = QComboBox(self.groupBox_6)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.comboBox_4)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_5)

        self.doubleSpinBox_20 = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_20.setObjectName(u"doubleSpinBox_20")

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_20)

        self.doubleSpinBox_21 = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_21.setObjectName(u"doubleSpinBox_21")

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.doubleSpinBox_21)


        self.gridLayout_2.addWidget(self.groupBox_6, 1, 2, 1, 1)

        self.groupBox_5 = QGroupBox(self.frame_13)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.formLayout_6 = QFormLayout(self.groupBox_5)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_39 = QLabel(self.groupBox_5)
        self.label_39.setObjectName(u"label_39")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_39)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_4)

        self.label_40 = QLabel(self.groupBox_5)
        self.label_40.setObjectName(u"label_40")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_40)

        self.comboBox_3 = QComboBox(self.groupBox_5)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.comboBox_3)

        self.label_41 = QLabel(self.groupBox_5)
        self.label_41.setObjectName(u"label_41")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_41)

        self.doubleSpinBox_19 = QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_19.setObjectName(u"doubleSpinBox_19")

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_19)

        self.label_42 = QLabel(self.groupBox_5)
        self.label_42.setObjectName(u"label_42")

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_42)

        self.doubleSpinBox_18 = QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_18.setObjectName(u"doubleSpinBox_18")

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.doubleSpinBox_18)


        self.gridLayout_2.addWidget(self.groupBox_5, 1, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.frame_13)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_23 = QLabel(self.groupBox_2)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_23)

        self.doubleSpinBox_10 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_10.setObjectName(u"doubleSpinBox_10")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox_10)

        self.label_25 = QLabel(self.groupBox_2)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_25)

        self.doubleSpinBox_12 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_12.setObjectName(u"doubleSpinBox_12")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBox_12)

        self.label_26 = QLabel(self.groupBox_2)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_26)

        self.doubleSpinBox_13 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_13.setObjectName(u"doubleSpinBox_13")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.doubleSpinBox_13)

        self.label_24 = QLabel(self.groupBox_2)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_24)

        self.doubleSpinBox_11 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_11.setObjectName(u"doubleSpinBox_11")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBox_11)


        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_13)

        self.frame_20 = QFrame(self.tab_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 40))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_18 = QLabel(self.frame_20)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_2.addWidget(self.label_18)

        self.spinBox = QSpinBox(self.frame_20)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(30000)

        self.horizontalLayout_2.addWidget(self.spinBox)

        self.label_31 = QLabel(self.frame_20)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_2.addWidget(self.label_31)

        self.spinBox_2 = QSpinBox(self.frame_20)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(30000)

        self.horizontalLayout_2.addWidget(self.spinBox_2)


        self.verticalLayout_7.addWidget(self.frame_20, 0, Qt.AlignHCenter)

        self.frame_14 = QFrame(self.tab_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_28 = QPushButton(self.frame_14)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.horizontalLayout_11.addWidget(self.pushButton_28)

        self.pushButton_29 = QPushButton(self.frame_14)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.horizontalLayout_11.addWidget(self.pushButton_29)

        self.pushButton_30 = QPushButton(self.frame_14)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.horizontalLayout_11.addWidget(self.pushButton_30)


        self.verticalLayout_7.addWidget(self.frame_14, 0, Qt.AlignBottom)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(SubWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SubWindow)
    # setupUi

    def retranslateUi(self, SubWindow):
        SubWindow.setWindowTitle(QCoreApplication.translate("SubWindow", u"Sub Recipe Window", None))
        self.label.setText(QCoreApplication.translate("SubWindow", u"Recipe Editor", None))
        self.checkBox.setText(QCoreApplication.translate("SubWindow", u"Enable", None))
        self.label_16.setText(QCoreApplication.translate("SubWindow", u"Arg 14", None))
        self.label_5.setText(QCoreApplication.translate("SubWindow", u"Arg 7", None))
        self.label_9.setText(QCoreApplication.translate("SubWindow", u"Arg 10", None))
        self.label_7.setText(QCoreApplication.translate("SubWindow", u"Arg 11", None))
        self.label_12.setText(QCoreApplication.translate("SubWindow", u"Arg 3", None))
        self.label_2.setText(QCoreApplication.translate("SubWindow", u"Arg 1", None))
        self.label_10.setText(QCoreApplication.translate("SubWindow", u"Arg 13", None))
        self.label_11.setText(QCoreApplication.translate("SubWindow", u"Arg 2", None))
        self.label_14.setText(QCoreApplication.translate("SubWindow", u"Arg 5", None))
        self.label_8.setText(QCoreApplication.translate("SubWindow", u"Arg 16", None))
        self.label_4.setText(QCoreApplication.translate("SubWindow", u"Arg 6", None))
        self.label_6.setText(QCoreApplication.translate("SubWindow", u"Arg 8", None))
        self.label_15.setText(QCoreApplication.translate("SubWindow", u"Arg 12", None))
        self.label_17.setText(QCoreApplication.translate("SubWindow", u"Arg 15", None))
        self.label_13.setText(QCoreApplication.translate("SubWindow", u"Arg 9", None))
        self.label_3.setText(QCoreApplication.translate("SubWindow", u"Arg 4", None))
        self.QR_arg9.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.QR_arg9.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.QR_arg9.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.QR_arg9.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.QR_arg9.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.QR_arg9.setItemText(5, QCoreApplication.translate("SubWindow", u"Shift", None))

        self.QR_arg10.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.QR_arg10.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.QR_arg10.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.QR_arg10.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.QR_arg10.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.QR_arg10.setItemText(5, QCoreApplication.translate("SubWindow", u"Shift", None))

        self.QR_arg11.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.QR_arg11.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.QR_arg11.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.QR_arg11.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.QR_arg11.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.QR_arg11.setItemText(5, QCoreApplication.translate("SubWindow", u"Shift", None))

        self.QR_arg12.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.QR_arg12.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.QR_arg12.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.QR_arg12.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.QR_arg12.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.QR_arg12.setItemText(5, QCoreApplication.translate("SubWindow", u"Shift", None))

        self.QR_arg13.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.QR_arg13.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.QR_arg13.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.QR_arg13.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.QR_arg13.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.QR_arg13.setItemText(5, QCoreApplication.translate("SubWindow", u"Shift", None))

        self.QR_arg14.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.QR_arg14.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.QR_arg14.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.QR_arg14.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.QR_arg14.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.QR_arg14.setItemText(5, QCoreApplication.translate("SubWindow", u"Shift", None))

        self.QR_arg15.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.QR_arg15.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.QR_arg15.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.QR_arg15.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.QR_arg15.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.QR_arg15.setItemText(5, QCoreApplication.translate("SubWindow", u"Shift", None))

        self.QR_arg16.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.QR_arg16.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.QR_arg16.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.QR_arg16.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.QR_arg16.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.QR_arg16.setItemText(5, QCoreApplication.translate("SubWindow", u"Shift", None))

        self.QR_arg2.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.QR_arg2.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.QR_arg2.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.QR_arg2.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.QR_arg2.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.QR_arg2.setItemText(5, QCoreApplication.translate("SubWindow", u"Shift", None))

        self.QR_arg1.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.QR_arg1.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.QR_arg1.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.QR_arg1.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.QR_arg1.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.QR_arg1.setItemText(5, QCoreApplication.translate("SubWindow", u"Shift", None))

        self.QR_arg3.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.QR_arg3.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.QR_arg3.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.QR_arg3.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.QR_arg3.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.QR_arg3.setItemText(5, QCoreApplication.translate("SubWindow", u"Shift", None))

        self.QR_arg4.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.QR_arg4.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.QR_arg4.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.QR_arg4.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.QR_arg4.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.QR_arg4.setItemText(5, QCoreApplication.translate("SubWindow", u"Shift", None))

        self.QR_arg5.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.QR_arg5.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.QR_arg5.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.QR_arg5.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.QR_arg5.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.QR_arg5.setItemText(5, QCoreApplication.translate("SubWindow", u"Shift", None))

        self.QR_arg6.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.QR_arg6.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.QR_arg6.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.QR_arg6.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.QR_arg6.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.QR_arg6.setItemText(5, QCoreApplication.translate("SubWindow", u"Shift", None))

        self.QR_arg7.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.QR_arg7.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.QR_arg7.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.QR_arg7.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.QR_arg7.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.QR_arg7.setItemText(5, QCoreApplication.translate("SubWindow", u"Shift", None))

        self.QR_arg8.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.QR_arg8.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.QR_arg8.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.QR_arg8.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.QR_arg8.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.QR_arg8.setItemText(5, QCoreApplication.translate("SubWindow", u"Shift", None))

        self.label_148.setText(QCoreApplication.translate("SubWindow", u"Generated Data :", None))
        self.label_149.setText(QCoreApplication.translate("SubWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("SubWindow", u"Save", None))
        self.pushButton_2.setText(QCoreApplication.translate("SubWindow", u"Reload", None))
        self.pushButton_3.setText(QCoreApplication.translate("SubWindow", u"Generate Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("SubWindow", u"QR Code Argument", None))
        self.checkBox_2.setText(QCoreApplication.translate("SubWindow", u"Enable", None))
        self.label_82.setText(QCoreApplication.translate("SubWindow", u"Arg 14", None))
        self.label_83.setText(QCoreApplication.translate("SubWindow", u"Arg 7", None))
        self.label_84.setText(QCoreApplication.translate("SubWindow", u"Arg 10", None))
        self.label_85.setText(QCoreApplication.translate("SubWindow", u"Arg 11", None))
        self.label_86.setText(QCoreApplication.translate("SubWindow", u"Arg 3", None))
        self.label_87.setText(QCoreApplication.translate("SubWindow", u"Arg 1", None))
        self.label_88.setText(QCoreApplication.translate("SubWindow", u"Arg 13", None))
        self.label_89.setText(QCoreApplication.translate("SubWindow", u"Arg 2", None))
        self.label_90.setText(QCoreApplication.translate("SubWindow", u"Arg 5", None))
        self.label_91.setText(QCoreApplication.translate("SubWindow", u"Arg 16", None))
        self.label_92.setText(QCoreApplication.translate("SubWindow", u"Arg 6", None))
        self.label_93.setText(QCoreApplication.translate("SubWindow", u"Arg 8", None))
        self.label_94.setText(QCoreApplication.translate("SubWindow", u"Arg 12", None))
        self.label_95.setText(QCoreApplication.translate("SubWindow", u"Arg 15", None))
        self.label_96.setText(QCoreApplication.translate("SubWindow", u"Arg 9", None))
        self.label_97.setText(QCoreApplication.translate("SubWindow", u"Arg 4", None))
        self.Label1_arg9.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label1_arg9.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label1_arg9.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label1_arg9.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label1_arg9.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label1_arg9.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label1_arg10.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label1_arg10.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label1_arg10.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label1_arg10.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label1_arg10.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label1_arg10.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label1_arg11.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label1_arg11.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label1_arg11.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label1_arg11.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label1_arg11.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label1_arg11.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label1_arg12.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label1_arg12.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label1_arg12.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label1_arg12.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label1_arg12.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label1_arg12.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label1_arg13.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label1_arg13.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label1_arg13.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label1_arg13.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label1_arg13.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label1_arg13.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label1_arg14.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label1_arg14.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label1_arg14.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label1_arg14.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label1_arg14.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label1_arg14.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label1_arg15.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label1_arg15.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label1_arg15.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label1_arg15.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label1_arg15.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label1_arg15.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label1_arg16.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label1_arg16.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label1_arg16.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label1_arg16.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label1_arg16.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label1_arg16.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label1_arg2.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label1_arg2.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label1_arg2.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label1_arg2.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label1_arg2.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label1_arg2.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label1_arg1.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label1_arg1.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label1_arg1.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label1_arg1.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label1_arg1.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label1_arg1.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label1_arg3.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label1_arg3.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label1_arg3.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label1_arg3.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label1_arg3.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label1_arg3.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label1_arg4.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label1_arg4.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label1_arg4.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label1_arg4.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label1_arg4.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label1_arg4.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label1_arg5.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label1_arg5.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label1_arg5.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label1_arg5.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label1_arg5.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label1_arg5.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label1_arg6.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label1_arg6.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label1_arg6.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label1_arg6.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label1_arg6.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label1_arg6.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label1_arg7.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label1_arg7.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label1_arg7.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label1_arg7.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label1_arg7.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label1_arg7.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label1_arg8.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label1_arg8.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label1_arg8.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label1_arg8.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label1_arg8.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label1_arg8.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.label_150.setText(QCoreApplication.translate("SubWindow", u"Generated Data :", None))
        self.label_151.setText(QCoreApplication.translate("SubWindow", u"TextLabel", None))
        self.pushButton_16.setText(QCoreApplication.translate("SubWindow", u"Save", None))
        self.pushButton_17.setText(QCoreApplication.translate("SubWindow", u"Reload", None))
        self.pushButton_18.setText(QCoreApplication.translate("SubWindow", u"Generate Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("SubWindow", u"Label 1 Argument", None))
        self.checkBox_3.setText(QCoreApplication.translate("SubWindow", u"Enable", None))
        self.label_98.setText(QCoreApplication.translate("SubWindow", u"Arg 14", None))
        self.label_99.setText(QCoreApplication.translate("SubWindow", u"Arg 7", None))
        self.label_100.setText(QCoreApplication.translate("SubWindow", u"Arg 10", None))
        self.label_101.setText(QCoreApplication.translate("SubWindow", u"Arg 11", None))
        self.label_102.setText(QCoreApplication.translate("SubWindow", u"Arg 3", None))
        self.label_103.setText(QCoreApplication.translate("SubWindow", u"Arg 1", None))
        self.label_104.setText(QCoreApplication.translate("SubWindow", u"Arg 13", None))
        self.label_105.setText(QCoreApplication.translate("SubWindow", u"Arg 2", None))
        self.label_106.setText(QCoreApplication.translate("SubWindow", u"Arg 5", None))
        self.label_107.setText(QCoreApplication.translate("SubWindow", u"Arg 16", None))
        self.label_108.setText(QCoreApplication.translate("SubWindow", u"Arg 6", None))
        self.label_109.setText(QCoreApplication.translate("SubWindow", u"Arg 8", None))
        self.label_110.setText(QCoreApplication.translate("SubWindow", u"Arg 12", None))
        self.label_111.setText(QCoreApplication.translate("SubWindow", u"Arg 15", None))
        self.label_112.setText(QCoreApplication.translate("SubWindow", u"Arg 9", None))
        self.label_113.setText(QCoreApplication.translate("SubWindow", u"Arg 4", None))
        self.Label2_arg9.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label2_arg9.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label2_arg9.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label2_arg9.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label2_arg9.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label2_arg9.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label2_arg10.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label2_arg10.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label2_arg10.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label2_arg10.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label2_arg10.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label2_arg10.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label2_arg11.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label2_arg11.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label2_arg11.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label2_arg11.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label2_arg11.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label2_arg11.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label2_arg12.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label2_arg12.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label2_arg12.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label2_arg12.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label2_arg12.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label2_arg12.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label2_arg13.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label2_arg13.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label2_arg13.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label2_arg13.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label2_arg13.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label2_arg13.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label2_arg14.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label2_arg14.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label2_arg14.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label2_arg14.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label2_arg14.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label2_arg14.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label2_arg15.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label2_arg15.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label2_arg15.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label2_arg15.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label2_arg15.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label2_arg15.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label2_arg16.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label2_arg16.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label2_arg16.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label2_arg16.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label2_arg16.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label2_arg16.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label2_arg2.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label2_arg2.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label2_arg2.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label2_arg2.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label2_arg2.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label2_arg2.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label2_arg1.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label2_arg1.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label2_arg1.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label2_arg1.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label2_arg1.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label2_arg1.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label2_arg3.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label2_arg3.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label2_arg3.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label2_arg3.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label2_arg3.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label2_arg3.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label2_arg4.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label2_arg4.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label2_arg4.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label2_arg4.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label2_arg4.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label2_arg4.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label2_arg5.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label2_arg5.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label2_arg5.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label2_arg5.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label2_arg5.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label2_arg5.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label2_arg6.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label2_arg6.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label2_arg6.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label2_arg6.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label2_arg6.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label2_arg6.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label2_arg7.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label2_arg7.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label2_arg7.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label2_arg7.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label2_arg7.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label2_arg7.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label2_arg8.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label2_arg8.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label2_arg8.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label2_arg8.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label2_arg8.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label2_arg8.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.label_152.setText(QCoreApplication.translate("SubWindow", u"Generated Data :", None))
        self.label_153.setText(QCoreApplication.translate("SubWindow", u"TextLabel", None))
        self.pushButton_19.setText(QCoreApplication.translate("SubWindow", u"Save", None))
        self.pushButton_20.setText(QCoreApplication.translate("SubWindow", u"Reload", None))
        self.pushButton_21.setText(QCoreApplication.translate("SubWindow", u"Generate Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("SubWindow", u"Label 2 Argument", None))
        self.checkBox_4.setText(QCoreApplication.translate("SubWindow", u"Enable", None))
        self.label_114.setText(QCoreApplication.translate("SubWindow", u"Arg 14", None))
        self.label_115.setText(QCoreApplication.translate("SubWindow", u"Arg 7", None))
        self.label_116.setText(QCoreApplication.translate("SubWindow", u"Arg 10", None))
        self.label_117.setText(QCoreApplication.translate("SubWindow", u"Arg 11", None))
        self.label_118.setText(QCoreApplication.translate("SubWindow", u"Arg 3", None))
        self.label_119.setText(QCoreApplication.translate("SubWindow", u"Arg 1", None))
        self.label_120.setText(QCoreApplication.translate("SubWindow", u"Arg 13", None))
        self.label_121.setText(QCoreApplication.translate("SubWindow", u"Arg 2", None))
        self.label_122.setText(QCoreApplication.translate("SubWindow", u"Arg 5", None))
        self.label_123.setText(QCoreApplication.translate("SubWindow", u"Arg 16", None))
        self.label_124.setText(QCoreApplication.translate("SubWindow", u"Arg 6", None))
        self.label_125.setText(QCoreApplication.translate("SubWindow", u"Arg 8", None))
        self.label_126.setText(QCoreApplication.translate("SubWindow", u"Arg 12", None))
        self.label_127.setText(QCoreApplication.translate("SubWindow", u"Arg 15", None))
        self.label_128.setText(QCoreApplication.translate("SubWindow", u"Arg 9", None))
        self.label_129.setText(QCoreApplication.translate("SubWindow", u"Arg 4", None))
        self.Label3_arg9.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label3_arg9.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label3_arg9.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label3_arg9.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label3_arg9.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label3_arg9.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label3_arg10.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label3_arg10.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label3_arg10.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label3_arg10.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label3_arg10.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label3_arg10.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label3_arg11.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label3_arg11.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label3_arg11.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label3_arg11.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label3_arg11.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label3_arg11.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label3_arg12.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label3_arg12.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label3_arg12.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label3_arg12.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label3_arg12.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label3_arg12.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label3_arg13.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label3_arg13.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label3_arg13.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label3_arg13.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label3_arg13.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label3_arg13.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label3_arg14.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label3_arg14.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label3_arg14.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label3_arg14.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label3_arg14.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label3_arg14.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label3_arg15.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label3_arg15.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label3_arg15.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label3_arg15.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label3_arg15.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label3_arg15.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label3_arg16.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label3_arg16.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label3_arg16.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label3_arg16.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label3_arg16.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label3_arg16.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label3_arg2.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label3_arg2.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label3_arg2.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label3_arg2.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label3_arg2.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label3_arg2.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label3_arg1.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label3_arg1.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label3_arg1.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label3_arg1.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label3_arg1.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label3_arg1.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label3_arg3.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label3_arg3.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label3_arg3.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label3_arg3.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label3_arg3.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label3_arg3.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label3_arg4.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label3_arg4.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label3_arg4.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label3_arg4.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label3_arg4.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label3_arg4.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label3_arg5.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label3_arg5.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label3_arg5.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label3_arg5.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label3_arg5.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label3_arg5.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label3_arg6.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label3_arg6.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label3_arg6.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label3_arg6.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label3_arg6.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label3_arg6.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label3_arg7.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label3_arg7.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label3_arg7.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label3_arg7.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label3_arg7.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label3_arg7.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label3_arg8.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label3_arg8.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label3_arg8.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label3_arg8.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label3_arg8.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label3_arg8.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.label_154.setText(QCoreApplication.translate("SubWindow", u"Generated Data :", None))
        self.label_155.setText(QCoreApplication.translate("SubWindow", u"TextLabel", None))
        self.pushButton_22.setText(QCoreApplication.translate("SubWindow", u"Save", None))
        self.pushButton_24.setText(QCoreApplication.translate("SubWindow", u"Reload", None))
        self.pushButton_23.setText(QCoreApplication.translate("SubWindow", u"Generate Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("SubWindow", u"Label 3 Argument", None))
        self.checkBox_5.setText(QCoreApplication.translate("SubWindow", u"Enable", None))
        self.label_130.setText(QCoreApplication.translate("SubWindow", u"Arg 14", None))
        self.label_131.setText(QCoreApplication.translate("SubWindow", u"Arg 7", None))
        self.label_132.setText(QCoreApplication.translate("SubWindow", u"Arg 10", None))
        self.label_133.setText(QCoreApplication.translate("SubWindow", u"Arg 11", None))
        self.label_134.setText(QCoreApplication.translate("SubWindow", u"Arg 3", None))
        self.label_135.setText(QCoreApplication.translate("SubWindow", u"Arg 1", None))
        self.label_136.setText(QCoreApplication.translate("SubWindow", u"Arg 13", None))
        self.label_137.setText(QCoreApplication.translate("SubWindow", u"Arg 2", None))
        self.label_138.setText(QCoreApplication.translate("SubWindow", u"Arg 5", None))
        self.label_139.setText(QCoreApplication.translate("SubWindow", u"Arg 16", None))
        self.label_140.setText(QCoreApplication.translate("SubWindow", u"Arg 6", None))
        self.label_141.setText(QCoreApplication.translate("SubWindow", u"Arg 8", None))
        self.label_142.setText(QCoreApplication.translate("SubWindow", u"Arg 12", None))
        self.label_143.setText(QCoreApplication.translate("SubWindow", u"Arg 15", None))
        self.label_144.setText(QCoreApplication.translate("SubWindow", u"Arg 9", None))
        self.label_145.setText(QCoreApplication.translate("SubWindow", u"Arg 4", None))
        self.Label4_arg9.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label4_arg9.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label4_arg9.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label4_arg9.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label4_arg9.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label4_arg9.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label4_arg10.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label4_arg10.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label4_arg10.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label4_arg10.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label4_arg10.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label4_arg10.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label4_arg11.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label4_arg11.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label4_arg11.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label4_arg11.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label4_arg11.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label4_arg11.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label4_arg12.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label4_arg12.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label4_arg12.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label4_arg12.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label4_arg12.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label4_arg12.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label4_arg13.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label4_arg13.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label4_arg13.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label4_arg13.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label4_arg13.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label4_arg13.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label4_arg14.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label4_arg14.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label4_arg14.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label4_arg14.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label4_arg14.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label4_arg14.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label4_arg15.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label4_arg15.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label4_arg15.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label4_arg15.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label4_arg15.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label4_arg15.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label4_arg16.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label4_arg16.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label4_arg16.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label4_arg16.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label4_arg16.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label4_arg16.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label4_arg2.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label4_arg2.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label4_arg2.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label4_arg2.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label4_arg2.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label4_arg2.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label4_arg1.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label4_arg1.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label4_arg1.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label4_arg1.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label4_arg1.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label4_arg1.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label4_arg3.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label4_arg3.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label4_arg3.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label4_arg3.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label4_arg3.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label4_arg3.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label4_arg4.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label4_arg4.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label4_arg4.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label4_arg4.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label4_arg4.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label4_arg4.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label4_arg5.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label4_arg5.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label4_arg5.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label4_arg5.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label4_arg5.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label4_arg5.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label4_arg6.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label4_arg6.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label4_arg6.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label4_arg6.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label4_arg6.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label4_arg6.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label4_arg7.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label4_arg7.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label4_arg7.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label4_arg7.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label4_arg7.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label4_arg7.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.Label4_arg8.setItemText(0, QCoreApplication.translate("SubWindow", u"---", None))
        self.Label4_arg8.setItemText(1, QCoreApplication.translate("SubWindow", u"Date (Enter Date Formate)", None))
        self.Label4_arg8.setItemText(2, QCoreApplication.translate("SubWindow", u"Time (Enter Time Formate)", None))
        self.Label4_arg8.setItemText(3, QCoreApplication.translate("SubWindow", u"Custom Text", None))
        self.Label4_arg8.setItemText(4, QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.Label4_arg8.setItemText(5, QCoreApplication.translate("SubWindow", u"New Item", None))

        self.label_156.setText(QCoreApplication.translate("SubWindow", u"Generated Data :", None))
        self.label_157.setText(QCoreApplication.translate("SubWindow", u"TextLabel", None))
        self.pushButton_25.setText(QCoreApplication.translate("SubWindow", u"Save", None))
        self.pushButton_26.setText(QCoreApplication.translate("SubWindow", u"Reload", None))
        self.pushButton_27.setText(QCoreApplication.translate("SubWindow", u"Generate Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("SubWindow", u"Label 4 Argument", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("SubWindow", u"Label 1", None))
        self.label_27.setText(QCoreApplication.translate("SubWindow", u"Size:", None))
        self.label_29.setText(QCoreApplication.translate("SubWindow", u"Top Space :", None))
        self.label_30.setText(QCoreApplication.translate("SubWindow", u"Left Space :", None))
        self.label_28.setText(QCoreApplication.translate("SubWindow", u"weight :", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("SubWindow", u"normal", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("SubWindow", u"bold", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("SubWindow", u"bolder", None))

        self.groupBox.setTitle(QCoreApplication.translate("SubWindow", u"Page Layout", None))
        self.label_19.setText(QCoreApplication.translate("SubWindow", u"Height :", None))
        self.label_20.setText(QCoreApplication.translate("SubWindow", u"Width :", None))
        self.label_21.setText(QCoreApplication.translate("SubWindow", u"Top Space :", None))
        self.label_22.setText(QCoreApplication.translate("SubWindow", u"Left Space :", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("SubWindow", u"Label 2", None))
        self.label_35.setText(QCoreApplication.translate("SubWindow", u"Size :", None))
        self.label_36.setText(QCoreApplication.translate("SubWindow", u"Weight :", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("SubWindow", u"normal", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("SubWindow", u"bold", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("SubWindow", u"bolder", None))

        self.label_37.setText(QCoreApplication.translate("SubWindow", u"Top Space :", None))
        self.label_38.setText(QCoreApplication.translate("SubWindow", u"Left Space :", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("SubWindow", u"Label 4", None))
        self.label_43.setText(QCoreApplication.translate("SubWindow", u"Size :", None))
        self.label_44.setText(QCoreApplication.translate("SubWindow", u"Width :", None))
        self.label_45.setText(QCoreApplication.translate("SubWindow", u"Top Space :", None))
        self.label_46.setText(QCoreApplication.translate("SubWindow", u"Left Space :", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("SubWindow", u"normal", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("SubWindow", u"bold", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("SubWindow", u"bolder", None))

        self.groupBox_5.setTitle(QCoreApplication.translate("SubWindow", u"Label 3", None))
        self.label_39.setText(QCoreApplication.translate("SubWindow", u"Size :", None))
        self.label_40.setText(QCoreApplication.translate("SubWindow", u"Weight :", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("SubWindow", u"normal", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("SubWindow", u"bold", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("SubWindow", u"bolder", None))

        self.label_41.setText(QCoreApplication.translate("SubWindow", u"Top Space :", None))
        self.label_42.setText(QCoreApplication.translate("SubWindow", u"Left Space :", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SubWindow", u"Barcode Parameter", None))
        self.label_23.setText(QCoreApplication.translate("SubWindow", u"Height :", None))
        self.label_25.setText(QCoreApplication.translate("SubWindow", u"Top Space :", None))
        self.label_26.setText(QCoreApplication.translate("SubWindow", u"Left Space :", None))
        self.label_24.setText(QCoreApplication.translate("SubWindow", u"Width :", None))
        self.label_18.setText(QCoreApplication.translate("SubWindow", u"Serial No.", None))
        self.label_31.setText(QCoreApplication.translate("SubWindow", u"Print Count:", None))
        self.pushButton_28.setText(QCoreApplication.translate("SubWindow", u"Save ", None))
        self.pushButton_29.setText(QCoreApplication.translate("SubWindow", u"Reload", None))
        self.pushButton_30.setText(QCoreApplication.translate("SubWindow", u"Test Print", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("SubWindow", u"Generation Code", None))
    # retranslateUi

