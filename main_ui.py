# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui_uipDLlIF.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, Namora):
        if not Namora.objectName():
            Namora.setObjectName(u"Namora")
        Namora.resize(450, 500)
        Namora.setMaximumSize(QSize(450, 500))
        self.centralwidget = QWidget(Namora)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255,0,0,0.5), stop:1 rgba(255,0,0,0.2));\n"
"}\n"
"\n"
"QLabel{\n"
"	font: italic 35px Times, sans-serif;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"	font-size: 20px;\n"
"	color: white;\n"
"	min-height: 45px;\n"
"	border-radius: 20px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 431, 101))
        self.label.setAlignment(Qt.AlignCenter)
        self.frame_yes = QFrame(self.centralwidget)
        self.frame_yes.setObjectName(u"frame_yes")
        self.frame_yes.setGeometry(QRect(30, 160, 171, 101))
        self.frame_yes.setFrameShape(QFrame.NoFrame)
        self.frame_yes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_yes)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_yes = QPushButton(self.frame_yes)
        self.button_yes.setObjectName(u"button_yes")

        self.horizontalLayout.addWidget(self.button_yes)

        self.frame_no = QFrame(self.centralwidget)
        self.frame_no.setObjectName(u"frame_no")
        self.frame_no.setGeometry(QRect(250, 160, 171, 101))
        self.frame_no.setFrameShape(QFrame.NoFrame)
        self.frame_no.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_no)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_no = QPushButton(self.frame_no)
        self.button_no.setObjectName(u"button_no")

        self.horizontalLayout_2.addWidget(self.button_no)

        Namora.setCentralWidget(self.centralwidget)

        self.retranslateUi(Namora)

        QMetaObject.connectSlotsByName(Namora)
    # setupUi

    def retranslateUi(self, Namora):
        Namora.setWindowTitle(QCoreApplication.translate("Namora", u"Namora", None))
        self.label.setText(QCoreApplication.translate("Namora", u"Quer namorar comigo?", None))
        self.button_yes.setText(QCoreApplication.translate("Namora", u"Sim", None))
        self.button_no.setText(QCoreApplication.translate("Namora", u"N\u00e3o", None))
    # retranslateUi

