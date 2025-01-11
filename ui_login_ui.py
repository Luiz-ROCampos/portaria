# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(444, 459)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login.sizePolicy().hasHeightForWidth())
        login.setSizePolicy(sizePolicy)
        login.setMinimumSize(QSize(444, 459))
        login.setMaximumSize(QSize(444, 459))
        login.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(login)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(7, 99, 164, 0.4);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(400, 80))
        self.label.setMaximumSize(QSize(400, 80))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.txt_usuario = QLineEdit(self.frame)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setMinimumSize(QSize(0, 40))
        self.txt_usuario.setStyleSheet(u"color: rgb(22, 22, 22);\n"
"background-color: rgb(197, 210, 217);\n"
"border-top: None;\n"
"font: 75 14pt \"Arial\";\n"
"border-left: None;\n"
"border-right: none;\n"
"border-radius: 15px;\n"
"")
        self.txt_usuario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.txt_usuario)

        self.txt_senha = QLineEdit(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setMinimumSize(QSize(0, 40))
        self.txt_senha.setStyleSheet(u"color: rgb(22, 22, 22);\n"
"background-color: rgb(197, 210, 217);\n"
"border-top: None;\n"
"font: 75 14pt \"Arial\";\n"
"border-left: None;\n"
"border-right: none;\n"
"border-radius: 15px;")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.txt_senha)

        self.btn_logar = QPushButton(self.frame)
        self.btn_logar.setObjectName(u"btn_logar")
        self.btn_logar.setEnabled(True)
        self.btn_logar.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.btn_logar.setFont(font1)
        self.btn_logar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(22, 22, 22);\n"
"	background-color: rgb(197, 210, 217);\n"
"	font: 75 14pt \"Arial\";\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(108, 156, 196);\n"
"	color: rgb(22, 22, 22);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.btn_logar)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.label.setText(QCoreApplication.translate("login", u"LOGIN", None))
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("login", u"Usu\u00e1rio", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("login", u"Senha", None))
        self.btn_logar.setText(QCoreApplication.translate("login", u"Logar", None))
    # retranslateUi

