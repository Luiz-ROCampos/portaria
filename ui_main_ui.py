# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainPortaria(object):
    def setupUi(self, MainPortaria):
        if not MainPortaria.objectName():
            MainPortaria.setObjectName(u"MainPortaria")
        MainPortaria.resize(1459, 798)
        MainPortaria.setMinimumSize(QSize(1300, 798))
        MainPortaria.setMaximumSize(QSize(1500, 822))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(10)
        MainPortaria.setFont(font)
        self.centralwidget = QWidget(MainPortaria)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_48 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 800))
        self.frame.setMaximumSize(QSize(200, 800))
        self.frame.setStyleSheet(u"background-color: rgb(7, 99, 164);\n"
"QPushButton{\n"
"	border: None;\n"
"	border-radius-left: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(12, 772, 16, 16))
        self.label_2.setMaximumSize(QSize(16777215, 150))
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 201, 110))
        self.horizontalLayout_31 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_31.setSpacing(5)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(15, 20, 20, 20)
        self.lbl_logo = QLabel(self.layoutWidget)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setMinimumSize(QSize(90, 70))
        self.lbl_logo.setMaximumSize(QSize(90, 70))
        font1 = QFont()
        font1.setPointSize(20)
        self.lbl_logo.setFont(font1)
        self.lbl_logo.setPixmap(QPixmap(u":/icons/icons/logo.png"))
        self.lbl_logo.setScaledContents(True)
        self.lbl_logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.lbl_logo)

        self.btn_pg_fornecedor = QPushButton(self.frame)
        self.btn_pg_fornecedor.setObjectName(u"btn_pg_fornecedor")
        self.btn_pg_fornecedor.setGeometry(QRect(10, 208, 190, 40))
        self.btn_pg_fornecedor.setMinimumSize(QSize(190, 40))
        self.btn_pg_fornecedor.setMaximumSize(QSize(190, 40))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.btn_pg_fornecedor.setFont(font2)
        self.btn_pg_fornecedor.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.btn_pg_fornecedor.setIconSize(QSize(40, 40))
        self.btn_pg_fornecedor.setCheckable(True)
        self.btn_pg_fornecedor.setAutoExclusive(True)
        self.btn_pg_home = QPushButton(self.frame)
        self.btn_pg_home.setObjectName(u"btn_pg_home")
        self.btn_pg_home.setGeometry(QRect(10, 138, 190, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pg_home.sizePolicy().hasHeightForWidth())
        self.btn_pg_home.setSizePolicy(sizePolicy)
        self.btn_pg_home.setMinimumSize(QSize(190, 40))
        self.btn_pg_home.setMaximumSize(QSize(190, 40))
        self.btn_pg_home.setFont(font2)
        self.btn_pg_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_pg_home.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.btn_pg_home.setIconSize(QSize(40, 40))
        self.btn_pg_home.setCheckable(True)
        self.btn_pg_home.setAutoExclusive(True)
        self.btn_pg_terceiros = QPushButton(self.frame)
        self.btn_pg_terceiros.setObjectName(u"btn_pg_terceiros")
        self.btn_pg_terceiros.setGeometry(QRect(10, 278, 190, 40))
        self.btn_pg_terceiros.setMinimumSize(QSize(190, 40))
        self.btn_pg_terceiros.setMaximumSize(QSize(190, 40))
        self.btn_pg_terceiros.setFont(font2)
        self.btn_pg_terceiros.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.btn_pg_terceiros.setIconSize(QSize(40, 40))
        self.btn_pg_terceiros.setCheckable(True)
        self.btn_pg_terceiros.setAutoExclusive(True)
        self.btn_pg_colaboradores = QPushButton(self.frame)
        self.btn_pg_colaboradores.setObjectName(u"btn_pg_colaboradores")
        self.btn_pg_colaboradores.setGeometry(QRect(10, 348, 190, 40))
        self.btn_pg_colaboradores.setMinimumSize(QSize(190, 40))
        self.btn_pg_colaboradores.setMaximumSize(QSize(190, 40))
        self.btn_pg_colaboradores.setFont(font2)
        self.btn_pg_colaboradores.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.btn_pg_colaboradores.setIconSize(QSize(40, 40))
        self.btn_pg_colaboradores.setCheckable(True)
        self.btn_pg_colaboradores.setAutoExclusive(True)
        self.btn_pg_materiais = QPushButton(self.frame)
        self.btn_pg_materiais.setObjectName(u"btn_pg_materiais")
        self.btn_pg_materiais.setGeometry(QRect(10, 488, 190, 40))
        self.btn_pg_materiais.setMinimumSize(QSize(190, 40))
        self.btn_pg_materiais.setMaximumSize(QSize(190, 40))
        self.btn_pg_materiais.setFont(font2)
        self.btn_pg_materiais.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.btn_pg_materiais.setIconSize(QSize(40, 40))
        self.btn_pg_materiais.setCheckable(True)
        self.btn_pg_materiais.setAutoExclusive(True)
        self.btn_pg_chave = QPushButton(self.frame)
        self.btn_pg_chave.setObjectName(u"btn_pg_chave")
        self.btn_pg_chave.setGeometry(QRect(10, 418, 190, 40))
        self.btn_pg_chave.setMinimumSize(QSize(190, 40))
        self.btn_pg_chave.setMaximumSize(QSize(190, 40))
        self.btn_pg_chave.setFont(font2)
        self.btn_pg_chave.setStyleSheet(u"QPushButton{\n"
"	border: None;\n"
"	border-bottom-left-radius: 10px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.btn_pg_chave.setIconSize(QSize(40, 40))
        self.btn_pg_chave.setCheckable(True)
        self.btn_pg_chave.setAutoExclusive(True)

        self.horizontalLayout_48.addWidget(self.frame)

        self.paginas = QStackedWidget(self.centralwidget)
        self.paginas.setObjectName(u"paginas")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.paginas.sizePolicy().hasHeightForWidth())
        self.paginas.setSizePolicy(sizePolicy1)
        self.paginas.setMinimumSize(QSize(1100, 790))
        self.paginas.setMaximumSize(QSize(1220, 800))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(11)
        self.paginas.setFont(font3)
        self.paginas.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_13 = QVBoxLayout(self.pg_home)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_3 = QLabel(self.pg_home)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 100))
        font4 = QFont()
        font4.setPointSize(24)
        font4.setBold(True)
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_3)

        self.label_4 = QLabel(self.pg_home)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(16)
        self.label_4.setFont(font5)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setMargin(0)

        self.verticalLayout_13.addWidget(self.label_4)

        self.paginas.addWidget(self.pg_home)
        self.pg_fonecedor = QWidget()
        self.pg_fonecedor.setObjectName(u"pg_fonecedor")
        self.widget_fornecedor = QWidget(self.pg_fonecedor)
        self.widget_fornecedor.setObjectName(u"widget_fornecedor")
        self.widget_fornecedor.setGeometry(QRect(710, 120, 490, 650))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_fornecedor.sizePolicy().hasHeightForWidth())
        self.widget_fornecedor.setSizePolicy(sizePolicy2)
        self.widget_fornecedor.setMinimumSize(QSize(490, 650))
        self.widget_fornecedor.setMaximumSize(QSize(540, 650))
        self.widget_fornecedor.setStyleSheet(u"background-color: rgb(197, 210, 217);")
        self.label_15 = QLabel(self.widget_fornecedor)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 10, 471, 50))
        self.label_15.setMaximumSize(QSize(16777215, 50))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(14)
        self.label_15.setFont(font6)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.tabela_fornecedor = QTableWidget(self.widget_fornecedor)
        if (self.tabela_fornecedor.columnCount() < 4):
            self.tabela_fornecedor.setColumnCount(4)
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setStyleStrategy(QFont.PreferAntialias)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font7);
        self.tabela_fornecedor.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(10)
        font8.setBold(True)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font8);
        self.tabela_fornecedor.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font8);
        self.tabela_fornecedor.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font8);
        self.tabela_fornecedor.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabela_fornecedor.setObjectName(u"tabela_fornecedor")
        self.tabela_fornecedor.setGeometry(QRect(5, 70, 481, 571))
        self.tabela_fornecedor.setMinimumSize(QSize(481, 0))
        self.tabela_fornecedor.setMaximumSize(QSize(481, 16777215))
        self.label_5 = QLabel(self.pg_fonecedor)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(12, 0, 1271, 100))
        self.label_5.setMaximumSize(QSize(16777215, 100))
        self.label_5.setFont(font4)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.layoutWidget1 = QWidget(self.pg_fonecedor)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 126, 682, 661))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, -1, 10, -1)
        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(45, 45))
        self.label_6.setMaximumSize(QSize(45, 45))
        self.label_6.setPixmap(QPixmap(u":/icons/icons/fornecedor.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_6)

        self.cmb_registro_fornecedor = QComboBox(self.layoutWidget1)
        self.cmb_registro_fornecedor.setObjectName(u"cmb_registro_fornecedor")
        self.cmb_registro_fornecedor.setMinimumSize(QSize(0, 35))
        self.cmb_registro_fornecedor.setMaximumSize(QSize(650, 16777215))
        font9 = QFont()
        font9.setFamilies([u"Arial"])
        font9.setPointSize(12)
        self.cmb_registro_fornecedor.setFont(font9)
        self.cmb_registro_fornecedor.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;\n"
"font: 12pt Arial;")
        self.cmb_registro_fornecedor.setInputMethodHints(Qt.ImhNone)
        self.cmb_registro_fornecedor.setEditable(False)

        self.horizontalLayout.addWidget(self.cmb_registro_fornecedor)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, -1, 10, -1)
        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(43, 45))
        self.label_7.setMaximumSize(QSize(45, 45))
        self.label_7.setPixmap(QPixmap(u":/icons/icons/nome.png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.cmb_registro_nome = QComboBox(self.layoutWidget1)
        self.cmb_registro_nome.setObjectName(u"cmb_registro_nome")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(157)
        sizePolicy3.setVerticalStretch(27)
        sizePolicy3.setHeightForWidth(self.cmb_registro_nome.sizePolicy().hasHeightForWidth())
        self.cmb_registro_nome.setSizePolicy(sizePolicy3)
        self.cmb_registro_nome.setMinimumSize(QSize(450, 35))
        self.cmb_registro_nome.setMaximumSize(QSize(450, 16777215))
        self.cmb_registro_nome.setFont(font9)
        self.cmb_registro_nome.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;\n"
"font-size: 12;")
        self.cmb_registro_nome.setInputMethodHints(Qt.ImhNone)
        self.cmb_registro_nome.setEditable(False)

        self.horizontalLayout_2.addWidget(self.cmb_registro_nome)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, 10, -1)
        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(45, 45))
        self.label_10.setMaximumSize(QSize(45, 45))
        self.label_10.setPixmap(QPixmap(u":/icons/icons/cracha.png"))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.txt_registro_cracha = QLineEdit(self.layoutWidget1)
        self.txt_registro_cracha.setObjectName(u"txt_registro_cracha")
        self.txt_registro_cracha.setMinimumSize(QSize(70, 0))
        self.txt_registro_cracha.setMaximumSize(QSize(60, 16777215))
        self.txt_registro_cracha.setFont(font9)
        self.txt_registro_cracha.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")
        self.txt_registro_cracha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_registro_cracha)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, -1, 10, -1)
        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(45, 45))
        self.label_8.setMaximumSize(QSize(45, 45))
        self.label_8.setPixmap(QPixmap(u":/icons/icons/documento.png"))
        self.label_8.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.txt_registro_rg = QLineEdit(self.layoutWidget1)
        self.txt_registro_rg.setObjectName(u"txt_registro_rg")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(157)
        sizePolicy4.setVerticalStretch(27)
        sizePolicy4.setHeightForWidth(self.txt_registro_rg.sizePolicy().hasHeightForWidth())
        self.txt_registro_rg.setSizePolicy(sizePolicy4)
        self.txt_registro_rg.setMinimumSize(QSize(240, 27))
        self.txt_registro_rg.setMaximumSize(QSize(240, 16777215))
        self.txt_registro_rg.setFont(font9)
        self.txt_registro_rg.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_4.addWidget(self.txt_registro_rg)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(15, -1, 10, -1)
        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(45, 45))
        self.label_9.setMaximumSize(QSize(45, 45))
        self.label_9.setPixmap(QPixmap(u":/icons/icons/placa.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.txt_registro_placa = QLineEdit(self.layoutWidget1)
        self.txt_registro_placa.setObjectName(u"txt_registro_placa")
        self.txt_registro_placa.setMinimumSize(QSize(240, 0))
        self.txt_registro_placa.setMaximumSize(QSize(240, 16777215))
        self.txt_registro_placa.setFont(font9)
        self.txt_registro_placa.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_5.addWidget(self.txt_registro_placa)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(5)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(15, -1, 10, -1)
        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(45, 45))
        self.label_11.setMaximumSize(QSize(45, 45))
        self.label_11.setPixmap(QPixmap(u":/icons/icons/departamento.png"))
        self.label_11.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.cmb_registro_departamento = QComboBox(self.layoutWidget1)
        self.cmb_registro_departamento.setObjectName(u"cmb_registro_departamento")
        sizePolicy3.setHeightForWidth(self.cmb_registro_departamento.sizePolicy().hasHeightForWidth())
        self.cmb_registro_departamento.setSizePolicy(sizePolicy3)
        self.cmb_registro_departamento.setMinimumSize(QSize(240, 35))
        self.cmb_registro_departamento.setMaximumSize(QSize(240, 16777215))
        self.cmb_registro_departamento.setFont(font9)
        self.cmb_registro_departamento.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_6.addWidget(self.cmb_registro_departamento)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(15, -1, 10, -1)
        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(45, 45))
        self.label_12.setMaximumSize(QSize(45, 45))
        self.label_12.setPixmap(QPixmap(u":/icons/icons/autorizadopor.png"))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_12)

        self.cmb_registro_autorizadopor = QComboBox(self.layoutWidget1)
        self.cmb_registro_autorizadopor.setObjectName(u"cmb_registro_autorizadopor")
        sizePolicy3.setHeightForWidth(self.cmb_registro_autorizadopor.sizePolicy().hasHeightForWidth())
        self.cmb_registro_autorizadopor.setSizePolicy(sizePolicy3)
        self.cmb_registro_autorizadopor.setMinimumSize(QSize(240, 35))
        self.cmb_registro_autorizadopor.setMaximumSize(QSize(240, 16777215))
        self.cmb_registro_autorizadopor.setFont(font9)
        self.cmb_registro_autorizadopor.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_7.addWidget(self.cmb_registro_autorizadopor)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(15, -1, 15, 0)
        self.btn_registrar_fornecedor = QPushButton(self.layoutWidget1)
        self.btn_registrar_fornecedor.setObjectName(u"btn_registrar_fornecedor")
        self.btn_registrar_fornecedor.setMinimumSize(QSize(0, 45))
        self.btn_registrar_fornecedor.setMaximumSize(QSize(16777215, 45))
        font10 = QFont()
        font10.setFamilies([u"Arial"])
        font10.setPointSize(12)
        font10.setBold(True)
        self.btn_registrar_fornecedor.setFont(font10)
        self.btn_registrar_fornecedor.setStyleSheet(u"QPushButton{\n"
"	color: #161616;\n"
"	background-color: rgb(108, 156, 196);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"	background-color: rgb(116, 164, 191);\n"
"}")
        self.btn_registrar_fornecedor.setCheckable(True)
        self.btn_registrar_fornecedor.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.btn_registrar_fornecedor)

        self.btn_f_limpar = QPushButton(self.layoutWidget1)
        self.btn_f_limpar.setObjectName(u"btn_f_limpar")
        self.btn_f_limpar.setMinimumSize(QSize(0, 45))
        self.btn_f_limpar.setMaximumSize(QSize(16777215, 45))
        self.btn_f_limpar.setFont(font10)
        self.btn_f_limpar.setStyleSheet(u"QPushButton{\n"
"	color: #161616;\n"
"	background-color: rgb(108, 156, 196);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"	background-color: rgb(116, 164, 191);\n"
"}")
        self.btn_f_limpar.setCheckable(True)
        self.btn_f_limpar.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.btn_f_limpar)

        self.btn_pg_novo_fornecedor = QPushButton(self.layoutWidget1)
        self.btn_pg_novo_fornecedor.setObjectName(u"btn_pg_novo_fornecedor")
        self.btn_pg_novo_fornecedor.setMinimumSize(QSize(0, 45))
        self.btn_pg_novo_fornecedor.setMaximumSize(QSize(16777215, 45))
        self.btn_pg_novo_fornecedor.setFont(font10)
        self.btn_pg_novo_fornecedor.setStyleSheet(u"QPushButton{\n"
"	color: #161616;\n"
"	background-color: rgb(108, 156, 196);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"	background-color: rgb(116, 164, 191);\n"
"}")
        self.btn_pg_novo_fornecedor.setCheckable(True)
        self.btn_pg_novo_fornecedor.setAutoExclusive(True)

        self.horizontalLayout_9.addWidget(self.btn_pg_novo_fornecedor)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.paginas.addWidget(self.pg_fonecedor)
        self.pg_novo_fornecedor = QWidget()
        self.pg_novo_fornecedor.setObjectName(u"pg_novo_fornecedor")
        self.label_48 = QLabel(self.pg_novo_fornecedor)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(-2, 0, 1241, 100))
        self.label_48.setMaximumSize(QSize(16777215, 100))
        self.label_48.setFont(font4)
        self.label_48.setAlignment(Qt.AlignCenter)
        self.layoutWidget_4 = QWidget(self.pg_novo_fornecedor)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(340, 130, 611, 641))
        self.verticalLayout_15 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.layoutWidget_4)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMaximumSize(QSize(16777215, 50))
        self.label_55.setFont(font5)
        self.label_55.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_55)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setSpacing(10)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(15, -1, 15, -1)
        self.label_56 = QLabel(self.layoutWidget_4)
        self.label_56.setObjectName(u"label_56")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(45)
        sizePolicy5.setVerticalStretch(70)
        sizePolicy5.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy5)
        self.label_56.setMinimumSize(QSize(45, 45))
        self.label_56.setMaximumSize(QSize(45, 45))
        self.label_56.setPixmap(QPixmap(u":/icons/icons/fornecedor.png"))
        self.label_56.setScaledContents(True)

        self.horizontalLayout_41.addWidget(self.label_56)

        self.txt_novo_fornecedor = QLineEdit(self.layoutWidget_4)
        self.txt_novo_fornecedor.setObjectName(u"txt_novo_fornecedor")
        self.txt_novo_fornecedor.setFont(font9)
        self.txt_novo_fornecedor.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_41.addWidget(self.txt_novo_fornecedor)


        self.verticalLayout_15.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setSpacing(10)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(15, -1, 15, -1)
        self.label_58 = QLabel(self.layoutWidget_4)
        self.label_58.setObjectName(u"label_58")
        sizePolicy5.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy5)
        self.label_58.setMinimumSize(QSize(45, 45))
        self.label_58.setMaximumSize(QSize(45, 45))
        self.label_58.setPixmap(QPixmap(u":/icons/icons/nome.png"))
        self.label_58.setScaledContents(True)

        self.horizontalLayout_44.addWidget(self.label_58)

        self.txt_novo_entregador = QLineEdit(self.layoutWidget_4)
        self.txt_novo_entregador.setObjectName(u"txt_novo_entregador")
        self.txt_novo_entregador.setFont(font9)
        self.txt_novo_entregador.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_44.addWidget(self.txt_novo_entregador)


        self.verticalLayout_15.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setSpacing(10)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(15, -1, 15, -1)
        self.label_62 = QLabel(self.layoutWidget_4)
        self.label_62.setObjectName(u"label_62")
        sizePolicy5.setHeightForWidth(self.label_62.sizePolicy().hasHeightForWidth())
        self.label_62.setSizePolicy(sizePolicy5)
        self.label_62.setMinimumSize(QSize(45, 45))
        self.label_62.setMaximumSize(QSize(45, 45))
        self.label_62.setPixmap(QPixmap(u":/icons/icons/documento.png"))
        self.label_62.setScaledContents(True)

        self.horizontalLayout_45.addWidget(self.label_62)

        self.txt_novo_rg = QLineEdit(self.layoutWidget_4)
        self.txt_novo_rg.setObjectName(u"txt_novo_rg")
        self.txt_novo_rg.setFont(font9)
        self.txt_novo_rg.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_45.addWidget(self.txt_novo_rg)


        self.verticalLayout_15.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setSpacing(10)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(15, -1, 15, -1)
        self.label_63 = QLabel(self.layoutWidget_4)
        self.label_63.setObjectName(u"label_63")
        sizePolicy5.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy5)
        self.label_63.setMinimumSize(QSize(45, 45))
        self.label_63.setMaximumSize(QSize(45, 45))
        self.label_63.setPixmap(QPixmap(u":/icons/icons/placa.png"))
        self.label_63.setScaledContents(True)

        self.horizontalLayout_46.addWidget(self.label_63)

        self.txt_novo_placa = QLineEdit(self.layoutWidget_4)
        self.txt_novo_placa.setObjectName(u"txt_novo_placa")
        self.txt_novo_placa.setFont(font9)
        self.txt_novo_placa.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_46.addWidget(self.txt_novo_placa)


        self.verticalLayout_15.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setSpacing(10)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(20, -1, 20, -1)
        self.btn_novo_fornecedor = QPushButton(self.layoutWidget_4)
        self.btn_novo_fornecedor.setObjectName(u"btn_novo_fornecedor")
        self.btn_novo_fornecedor.setMaximumSize(QSize(16777215, 40))
        self.btn_novo_fornecedor.setFont(font10)
        self.btn_novo_fornecedor.setStyleSheet(u"QPushButton{\n"
"	color: #161616;\n"
"	background-color: rgb(108, 156, 196);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"	background-color: rgb(116, 164, 191);\n"
"}")
        self.btn_novo_fornecedor.setCheckable(True)
        self.btn_novo_fornecedor.setAutoExclusive(True)

        self.horizontalLayout_47.addWidget(self.btn_novo_fornecedor)

        self.btn_limpar_cadastro_fornecedor = QPushButton(self.layoutWidget_4)
        self.btn_limpar_cadastro_fornecedor.setObjectName(u"btn_limpar_cadastro_fornecedor")
        self.btn_limpar_cadastro_fornecedor.setMaximumSize(QSize(16777215, 40))
        self.btn_limpar_cadastro_fornecedor.setFont(font10)
        self.btn_limpar_cadastro_fornecedor.setStyleSheet(u"QPushButton{\n"
"	color: #161616;\n"
"	background-color: rgb(108, 156, 196);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"	background-color: rgb(116, 164, 191);\n"
"}")
        self.btn_limpar_cadastro_fornecedor.setCheckable(True)
        self.btn_limpar_cadastro_fornecedor.setAutoExclusive(True)

        self.horizontalLayout_47.addWidget(self.btn_limpar_cadastro_fornecedor)


        self.verticalLayout_15.addLayout(self.horizontalLayout_47)

        self.btn_voltar_fornecedor = QPushButton(self.pg_novo_fornecedor)
        self.btn_voltar_fornecedor.setObjectName(u"btn_voltar_fornecedor")
        self.btn_voltar_fornecedor.setGeometry(QRect(60, 160, 201, 61))
        font11 = QFont()
        font11.setPointSize(14)
        self.btn_voltar_fornecedor.setFont(font11)
        self.btn_voltar_fornecedor.setStyleSheet(u"QPushButton{\n"
"	color: #161616;\n"
"	background-color: rgb(108, 156, 196);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"	background-color: rgb(116, 164, 191);\n"
"}")
        self.btn_voltar_fornecedor.setCheckable(True)
        self.btn_voltar_fornecedor.setAutoExclusive(True)
        self.paginas.addWidget(self.pg_novo_fornecedor)
        self.pg_terceiros = QWidget()
        self.pg_terceiros.setObjectName(u"pg_terceiros")
        self.frame_3 = QFrame(self.pg_terceiros)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(1, 0, 1291, 791))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.widget_terceiros = QWidget(self.frame_3)
        self.widget_terceiros.setObjectName(u"widget_terceiros")
        self.widget_terceiros.setGeometry(QRect(750, 110, 441, 661))
        self.widget_terceiros.setStyleSheet(u"background-color: rgb(197, 210, 217);")
        self.label_16 = QLabel(self.widget_terceiros)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 10, 421, 50))
        self.label_16.setMaximumSize(QSize(16777215, 50))
        self.label_16.setFont(font6)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.tabela_terceiros = QTableWidget(self.widget_terceiros)
        if (self.tabela_terceiros.columnCount() < 3):
            self.tabela_terceiros.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font8);
        self.tabela_terceiros.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font8);
        self.tabela_terceiros.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font8);
        self.tabela_terceiros.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.tabela_terceiros.setObjectName(u"tabela_terceiros")
        self.tabela_terceiros.setGeometry(QRect(10, 60, 421, 591))
        self.layoutWidget2 = QWidget(self.frame_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(80, 170, 587, 481))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.layoutWidget2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 50))
        self.label_17.setFont(font5)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_17)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(15, -1, 15, -1)
        self.label_18 = QLabel(self.layoutWidget2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(45, 45))
        self.label_18.setMaximumSize(QSize(45, 45))
        self.label_18.setPixmap(QPixmap(u":/icons/icons/prefixo.png"))
        self.label_18.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.label_18)

        self.txt_reg_terceiros_prefixo = QLineEdit(self.layoutWidget2)
        self.txt_reg_terceiros_prefixo.setObjectName(u"txt_reg_terceiros_prefixo")
        self.txt_reg_terceiros_prefixo.setMinimumSize(QSize(500, 35))
        self.txt_reg_terceiros_prefixo.setFont(font9)
        self.txt_reg_terceiros_prefixo.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_11.addWidget(self.txt_reg_terceiros_prefixo)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(15, -1, 15, -1)
        self.label_19 = QLabel(self.layoutWidget2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(45, 45))
        self.label_19.setMaximumSize(QSize(45, 45))
        self.label_19.setPixmap(QPixmap(u":/icons/icons/empresa.png"))
        self.label_19.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.label_19)

        self.cmb_reg_terceiros_viacao = QComboBox(self.layoutWidget2)
        self.cmb_reg_terceiros_viacao.setObjectName(u"cmb_reg_terceiros_viacao")
        self.cmb_reg_terceiros_viacao.setMaximumSize(QSize(500, 35))
        self.cmb_reg_terceiros_viacao.setFont(font9)
        self.cmb_reg_terceiros_viacao.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_12.addWidget(self.cmb_reg_terceiros_viacao)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(40)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(15, -1, 15, -1)
        self.btn_reg_terceiros_entrada = QPushButton(self.layoutWidget2)
        self.btn_reg_terceiros_entrada.setObjectName(u"btn_reg_terceiros_entrada")
        self.btn_reg_terceiros_entrada.setMaximumSize(QSize(16777215, 40))
        self.btn_reg_terceiros_entrada.setFont(font10)
        self.btn_reg_terceiros_entrada.setStyleSheet(u"QPushButton{\n"
"	color: #161616;\n"
"	background-color: rgb(108, 156, 196);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"	background-color: rgb(116, 164, 191);\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_reg_terceiros_entrada)

        self.btn_reg_terceiros_saida = QPushButton(self.layoutWidget2)
        self.btn_reg_terceiros_saida.setObjectName(u"btn_reg_terceiros_saida")
        self.btn_reg_terceiros_saida.setMaximumSize(QSize(16777215, 40))
        self.btn_reg_terceiros_saida.setFont(font10)
        self.btn_reg_terceiros_saida.setStyleSheet(u"QPushButton{\n"
"	color: #161616;\n"
"	background-color: rgb(108, 156, 196);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"	background-color: rgb(116, 164, 191);\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_reg_terceiros_saida)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 0, 1291, 100))
        self.label_14.setMaximumSize(QSize(16777215, 100))
        self.label_14.setFont(font4)
        self.label_14.setAlignment(Qt.AlignCenter)
        self.paginas.addWidget(self.pg_terceiros)
        self.pg_colaboradores = QWidget()
        self.pg_colaboradores.setObjectName(u"pg_colaboradores")
        self.pg_colaboradores.setFont(font9)
        self.layoutWidget3 = QWidget(self.pg_colaboradores)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 0, 1221, 791))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.layoutWidget3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(16777215, 100))
        self.label_32.setFont(font4)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_32)

        self.frame_4 = QFrame(self.layoutWidget3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(1220, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_19.setSpacing(2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(5, 5, 5, 5)
        self.widget_terceiros_2 = QWidget(self.frame_4)
        self.widget_terceiros_2.setObjectName(u"widget_terceiros_2")
        self.widget_terceiros_2.setMinimumSize(QSize(220, 0))
        self.widget_terceiros_2.setMaximumSize(QSize(220, 16777215))
        self.widget_terceiros_2.setStyleSheet(u"background-color: rgb(197, 210, 217);")
        self.widget_terceiros_3 = QWidget(self.widget_terceiros_2)
        self.widget_terceiros_3.setObjectName(u"widget_terceiros_3")
        self.widget_terceiros_3.setGeometry(QRect(130, 370, 231, 691))
        self.widget_terceiros_3.setStyleSheet(u"background-color: rgb(197, 210, 217);")

        self.horizontalLayout_19.addWidget(self.widget_terceiros_2)

        self.widget_terceiros_5 = QWidget(self.frame_4)
        self.widget_terceiros_5.setObjectName(u"widget_terceiros_5")
        self.widget_terceiros_5.setMinimumSize(QSize(300, 0))
        self.widget_terceiros_5.setMaximumSize(QSize(690, 16777215))
        self.widget_terceiros_5.setStyleSheet(u"background-color: None;")
        self.label_59 = QLabel(self.widget_terceiros_5)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(1, 11, 711, 50))
        self.label_59.setMaximumSize(QSize(16777215, 50))
        self.label_59.setFont(font5)
        self.label_59.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.widget_terceiros_5)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 250, 691, 181))
        self.groupBox.setStyleSheet(u"border:None;")
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.ob_colaboradores_entrada = QRadioButton(self.groupBox)
        self.ob_colaboradores_entrada.setObjectName(u"ob_colaboradores_entrada")
        self.ob_colaboradores_entrada.setEnabled(True)
        self.ob_colaboradores_entrada.setGeometry(QRect(100, 30, 101, 28))
        self.ob_colaboradores_entrada.setFont(font10)
        self.ob_colaboradores_entrada.setLayoutDirection(Qt.LeftToRight)
        self.ob_colaboradores_entradaA = QRadioButton(self.groupBox)
        self.ob_colaboradores_entradaA.setObjectName(u"ob_colaboradores_entradaA")
        self.ob_colaboradores_entradaA.setEnabled(True)
        self.ob_colaboradores_entradaA.setGeometry(QRect(100, 110, 205, 28))
        self.ob_colaboradores_entradaA.setFont(font10)
        self.ob_colaboradores_entradaA.setLayoutDirection(Qt.LeftToRight)
        self.ob_colaboradores_entradaA.setCheckable(True)
        self.ob_colaboradores_saidaA = QRadioButton(self.groupBox)
        self.ob_colaboradores_saidaA.setObjectName(u"ob_colaboradores_saidaA")
        self.ob_colaboradores_saidaA.setEnabled(True)
        self.ob_colaboradores_saidaA.setGeometry(QRect(420, 30, 202, 28))
        self.ob_colaboradores_saidaA.setFont(font10)
        self.ob_colaboradores_saida = QRadioButton(self.groupBox)
        self.ob_colaboradores_saida.setObjectName(u"ob_colaboradores_saida")
        self.ob_colaboradores_saida.setEnabled(True)
        self.ob_colaboradores_saida.setGeometry(QRect(420, 110, 109, 28))
        self.ob_colaboradores_saida.setFont(font10)
        self.ob_colaboradores_saida.setCheckable(True)
        self.ob_colaboradores_saida.setChecked(False)
        self.btn_colaboradores_salvar = QPushButton(self.widget_terceiros_5)
        self.btn_colaboradores_salvar.setObjectName(u"btn_colaboradores_salvar")
        self.btn_colaboradores_salvar.setGeometry(QRect(230, 490, 219, 40))
        self.btn_colaboradores_salvar.setMaximumSize(QSize(16777215, 40))
        self.btn_colaboradores_salvar.setFont(font10)
        self.btn_colaboradores_salvar.setStyleSheet(u"QPushButton{\n"
"	color: #161616;\n"
"	background-color: rgb(108, 156, 196);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"	background-color: rgb(116, 164, 191);\n"
"}")
        self.layoutWidget_2 = QWidget(self.widget_terceiros_5)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 86, 681, 61))
        self.horizontalLayout_49 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_49.setSpacing(10)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(15, 0, 15, 0)
        self.label_64 = QLabel(self.layoutWidget_2)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(45, 45))
        self.label_64.setMaximumSize(QSize(45, 45))
        self.label_64.setPixmap(QPixmap(u":/icons/icons/nome.png"))
        self.label_64.setScaledContents(True)

        self.horizontalLayout_49.addWidget(self.label_64)

        self.cmb_colaboradores_departamento = QComboBox(self.layoutWidget_2)
        self.cmb_colaboradores_departamento.setObjectName(u"cmb_colaboradores_departamento")
        sizePolicy4.setHeightForWidth(self.cmb_colaboradores_departamento.sizePolicy().hasHeightForWidth())
        self.cmb_colaboradores_departamento.setSizePolicy(sizePolicy4)
        self.cmb_colaboradores_departamento.setMinimumSize(QSize(500, 35))
        self.cmb_colaboradores_departamento.setMaximumSize(QSize(270, 16777215))
        self.cmb_colaboradores_departamento.setFont(font9)
        self.cmb_colaboradores_departamento.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_49.addWidget(self.cmb_colaboradores_departamento)

        self.layoutWidget_7 = QWidget(self.widget_terceiros_5)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(0, 180, 681, 61))
        self.horizontalLayout_51 = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_51.setSpacing(10)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(15, 0, 15, 0)
        self.label_66 = QLabel(self.layoutWidget_7)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(45, 45))
        self.label_66.setMaximumSize(QSize(45, 45))
        self.label_66.setPixmap(QPixmap(u":/icons/icons/departamento.png"))
        self.label_66.setScaledContents(True)

        self.horizontalLayout_51.addWidget(self.label_66)

        self.cmb_colaboradores_funcionario = QComboBox(self.layoutWidget_7)
        self.cmb_colaboradores_funcionario.setObjectName(u"cmb_colaboradores_funcionario")
        sizePolicy4.setHeightForWidth(self.cmb_colaboradores_funcionario.sizePolicy().hasHeightForWidth())
        self.cmb_colaboradores_funcionario.setSizePolicy(sizePolicy4)
        self.cmb_colaboradores_funcionario.setMinimumSize(QSize(500, 35))
        self.cmb_colaboradores_funcionario.setMaximumSize(QSize(270, 16777215))
        self.cmb_colaboradores_funcionario.setFont(font9)
        self.cmb_colaboradores_funcionario.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_51.addWidget(self.cmb_colaboradores_funcionario)


        self.horizontalLayout_19.addWidget(self.widget_terceiros_5)

        self.widget_terceiros_4 = QWidget(self.frame_4)
        self.widget_terceiros_4.setObjectName(u"widget_terceiros_4")
        self.widget_terceiros_4.setMinimumSize(QSize(220, 0))
        self.widget_terceiros_4.setMaximumSize(QSize(220, 16777215))
        self.widget_terceiros_4.setStyleSheet(u"background-color: rgb(197, 210, 217);")

        self.horizontalLayout_19.addWidget(self.widget_terceiros_4)


        self.verticalLayout_11.addWidget(self.frame_4)

        self.paginas.addWidget(self.pg_colaboradores)
        self.pg_chave = QWidget()
        self.pg_chave.setObjectName(u"pg_chave")
        self.layoutWidget4 = QWidget(self.pg_chave)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(0, 0, 1291, 811))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.layoutWidget4)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(16777215, 100))
        self.label_42.setFont(font4)
        self.label_42.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_42)

        self.frame_5 = QFrame(self.layoutWidget4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.widget_3 = QWidget(self.frame_5)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(650, 0, 570, 671))
        self.widget_3.setMaximumSize(QSize(570, 680))
        self.widget_3.setStyleSheet(u"background-color: rgb(197, 210, 217);")
        self.label_24 = QLabel(self.widget_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(0, 10, 531, 50))
        self.label_24.setMaximumSize(QSize(16777215, 50))
        self.label_24.setFont(font6)
        self.label_24.setAlignment(Qt.AlignCenter)
        self.tabela_chaves = QTableWidget(self.widget_3)
        if (self.tabela_chaves.columnCount() < 5):
            self.tabela_chaves.setColumnCount(5)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabela_chaves.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabela_chaves.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabela_chaves.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabela_chaves.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabela_chaves.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        self.tabela_chaves.setObjectName(u"tabela_chaves")
        self.tabela_chaves.setGeometry(QRect(10, 60, 550, 610))
        self.tabela_chaves.setMaximumSize(QSize(550, 610))
        self.label_35 = QLabel(self.frame_5)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(12, 40, 631, 32))
        self.label_35.setMaximumSize(QSize(16777215, 50))
        self.label_35.setFont(font5)
        self.label_35.setAlignment(Qt.AlignCenter)
        self.layoutWidget5 = QWidget(self.frame_5)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(30, 530, 601, 101))
        self.horizontalLayout_23 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(15, 0, 15, 0)
        self.label_40 = QLabel(self.layoutWidget5)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_23.addWidget(self.label_40)

        self.btn_ch_salvar = QPushButton(self.layoutWidget5)
        self.btn_ch_salvar.setObjectName(u"btn_ch_salvar")
        self.btn_ch_salvar.setMaximumSize(QSize(16777215, 40))
        self.btn_ch_salvar.setFont(font10)
        self.btn_ch_salvar.setStyleSheet(u"QPushButton{\n"
"	color: #161616;\n"
"	background-color: rgb(108, 156, 196);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"	background-color: rgb(116, 164, 191);\n"
"}")

        self.horizontalLayout_23.addWidget(self.btn_ch_salvar)

        self.label_41 = QLabel(self.layoutWidget5)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_23.addWidget(self.label_41)

        self.layoutWidget6 = QWidget(self.frame_5)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(30, 110, 601, 391))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(15, -1, 15, -1)
        self.label_36 = QLabel(self.layoutWidget6)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(45, 45))
        self.label_36.setMaximumSize(QSize(45, 45))
        self.label_36.setPixmap(QPixmap(u":/icons/icons/nome.png"))
        self.label_36.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_36)

        self.txt_chave_nome = QLineEdit(self.layoutWidget6)
        self.txt_chave_nome.setObjectName(u"txt_chave_nome")
        self.txt_chave_nome.setFont(font9)
        self.txt_chave_nome.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_18.addWidget(self.txt_chave_nome)


        self.verticalLayout_2.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(15, -1, 15, -1)
        self.label_37 = QLabel(self.layoutWidget6)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(45, 45))
        self.label_37.setMaximumSize(QSize(45, 45))
        self.label_37.setPixmap(QPixmap(u":/icons/icons/departamento.png"))
        self.label_37.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_37)

        self.cmb_chave_setor = QComboBox(self.layoutWidget6)
        self.cmb_chave_setor.setObjectName(u"cmb_chave_setor")
        self.cmb_chave_setor.setMinimumSize(QSize(300, 35))
        self.cmb_chave_setor.setFont(font9)
        self.cmb_chave_setor.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_21.addWidget(self.cmb_chave_setor)

        self.label_43 = QLabel(self.layoutWidget6)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(45, 45))
        self.label_43.setMaximumSize(QSize(45, 45))
        self.label_43.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_43)

        self.txt_ch_chave = QLineEdit(self.layoutWidget6)
        self.txt_ch_chave.setObjectName(u"txt_ch_chave")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.txt_ch_chave.sizePolicy().hasHeightForWidth())
        self.txt_ch_chave.setSizePolicy(sizePolicy6)
        self.txt_ch_chave.setMinimumSize(QSize(50, 27))
        self.txt_ch_chave.setMaximumSize(QSize(50, 16777215))
        self.txt_ch_chave.setFont(font9)
        self.txt_ch_chave.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")
        self.txt_ch_chave.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.txt_ch_chave)


        self.verticalLayout_2.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(10)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(15, -1, 15, -1)
        self.label_38 = QLabel(self.layoutWidget6)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(45, 45))
        self.label_38.setMaximumSize(QSize(45, 45))
        self.label_38.setPixmap(QPixmap(u":/icons/icons/vigilante.png"))
        self.label_38.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.label_38)

        self.cmb_chave_vigilante = QComboBox(self.layoutWidget6)
        self.cmb_chave_vigilante.setObjectName(u"cmb_chave_vigilante")
        self.cmb_chave_vigilante.setMinimumSize(QSize(300, 35))
        self.cmb_chave_vigilante.setFont(font9)
        self.cmb_chave_vigilante.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_22.addWidget(self.cmb_chave_vigilante)


        self.verticalLayout_2.addLayout(self.horizontalLayout_22)


        self.verticalLayout_12.addWidget(self.frame_5)

        self.paginas.addWidget(self.pg_chave)
        self.pg_materiais = QWidget()
        self.pg_materiais.setObjectName(u"pg_materiais")
        self.layoutWidget7 = QWidget(self.pg_materiais)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(0, 0, 1291, 811))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.layoutWidget7)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(16777215, 100))
        self.label_52.setFont(font4)
        self.label_52.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_52)

        self.frame_6 = QFrame(self.layoutWidget7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_57 = QLabel(self.frame_6)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(273, 521, 16, 16))
        self.widget = QWidget(self.frame_6)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 561, 651))
        self.widget.setStyleSheet(u"background-color: rgb(197, 210, 217);")
        self.layoutWidget_3 = QWidget(self.widget)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(40, 250, 491, 61))
        self.horizontalLayout_26 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(15, 0, 15, 0)
        self.label_45 = QLabel(self.layoutWidget_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(45, 45))
        self.label_45.setMaximumSize(QSize(45, 45))
        self.label_45.setPixmap(QPixmap(u":/icons/icons/nome.png"))
        self.label_45.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.label_45)

        self.txt_m_motorista = QLineEdit(self.layoutWidget_3)
        self.txt_m_motorista.setObjectName(u"txt_m_motorista")
        self.txt_m_motorista.setFont(font9)
        self.txt_m_motorista.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_26.addWidget(self.txt_m_motorista)

        self.layoutWidget_5 = QWidget(self.widget)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(40, 130, 491, 61))
        self.horizontalLayout_25 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_25.setSpacing(10)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(15, 0, 15, 0)
        self.label_44 = QLabel(self.layoutWidget_5)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(45, 45))
        self.label_44.setMaximumSize(QSize(45, 45))
        self.label_44.setPixmap(QPixmap(u":/icons/icons/prefixo.png"))
        self.label_44.setScaledContents(True)

        self.horizontalLayout_25.addWidget(self.label_44)

        self.txt_m_carro = QLineEdit(self.layoutWidget_5)
        self.txt_m_carro.setObjectName(u"txt_m_carro")
        self.txt_m_carro.setFont(font9)
        self.txt_m_carro.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_25.addWidget(self.txt_m_carro)

        self.label_39 = QLabel(self.widget)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(30, 40, 501, 32))
        self.label_39.setMaximumSize(QSize(16777215, 50))
        self.label_39.setFont(font5)
        self.label_39.setAlignment(Qt.AlignCenter)
        self.layoutWidget_11 = QWidget(self.widget)
        self.layoutWidget_11.setObjectName(u"layoutWidget_11")
        self.layoutWidget_11.setGeometry(QRect(100, 360, 431, 91))
        self.horizontalLayout_35 = QHBoxLayout(self.layoutWidget_11)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(20, 0, 0, 0)
        self.ob_m_vassoura = QRadioButton(self.layoutWidget_11)
        self.ob_m_vassoura.setObjectName(u"ob_m_vassoura")
        self.ob_m_vassoura.setFont(font10)
        self.ob_m_vassoura.setLayoutDirection(Qt.LeftToRight)
        self.ob_m_vassoura.setAutoExclusive(False)

        self.horizontalLayout_35.addWidget(self.ob_m_vassoura)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(20, -1, -1, -1)
        self.ob_m_marreta = QRadioButton(self.layoutWidget_11)
        self.ob_m_marreta.setObjectName(u"ob_m_marreta")
        self.ob_m_marreta.setFont(font10)
        self.ob_m_marreta.setAutoExclusive(False)

        self.horizontalLayout_50.addWidget(self.ob_m_marreta)


        self.horizontalLayout_35.addLayout(self.horizontalLayout_50)

        self.layoutWidget_12 = QWidget(self.widget)
        self.layoutWidget_12.setObjectName(u"layoutWidget_12")
        self.layoutWidget_12.setGeometry(QRect(40, 510, 491, 121))
        self.horizontalLayout_52 = QHBoxLayout(self.layoutWidget_12)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.layoutWidget_12)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_52.addWidget(self.label_67)

        self.btn_m_salvar = QPushButton(self.layoutWidget_12)
        self.btn_m_salvar.setObjectName(u"btn_m_salvar")
        self.btn_m_salvar.setMaximumSize(QSize(16777215, 40))
        self.btn_m_salvar.setFont(font10)
        self.btn_m_salvar.setStyleSheet(u"QPushButton{\n"
"	color: #161616;\n"
"	background-color: rgb(108, 156, 196);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"	background-color: rgb(116, 164, 191);\n"
"}")

        self.horizontalLayout_52.addWidget(self.btn_m_salvar)

        self.label_65 = QLabel(self.layoutWidget_12)
        self.label_65.setObjectName(u"label_65")

        self.horizontalLayout_52.addWidget(self.label_65)

        self.horizontalLayout_52.setStretch(0, 10)
        self.horizontalLayout_52.setStretch(1, 20)
        self.horizontalLayout_52.setStretch(2, 10)
        self.widget_2 = QWidget(self.frame_6)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(640, 20, 561, 651))
        self.widget_2.setStyleSheet(u"background-color: rgb(197, 210, 217);")
        self.label_53 = QLabel(self.widget_2)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(32, 40, 511, 32))
        self.label_53.setMaximumSize(QSize(16777215, 50))
        self.label_53.setFont(font5)
        self.label_53.setAlignment(Qt.AlignCenter)
        self.layoutWidget_8 = QWidget(self.widget_2)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(90, 210, 451, 281))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(20, -1, 0, -1)
        self.ob_ma_lavagem = QRadioButton(self.layoutWidget_8)
        self.ob_ma_lavagem.setObjectName(u"ob_ma_lavagem")
        self.ob_ma_lavagem.setFont(font10)
        self.ob_ma_lavagem.setLayoutDirection(Qt.LeftToRight)
        self.ob_ma_lavagem.setAutoExclusive(False)

        self.horizontalLayout_32.addWidget(self.ob_ma_lavagem)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(20, -1, -1, -1)
        self.ob_ma_eletrica = QRadioButton(self.layoutWidget_8)
        self.ob_ma_eletrica.setObjectName(u"ob_ma_eletrica")
        self.ob_ma_eletrica.setFont(font10)
        self.ob_ma_eletrica.setLayoutDirection(Qt.LeftToRight)
        self.ob_ma_eletrica.setAutoExclusive(False)

        self.horizontalLayout_39.addWidget(self.ob_ma_eletrica)


        self.horizontalLayout_32.addLayout(self.horizontalLayout_39)


        self.verticalLayout_7.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(20, -1, -1, -1)
        self.ob_ma_manutencao = QRadioButton(self.layoutWidget_8)
        self.ob_ma_manutencao.setObjectName(u"ob_ma_manutencao")
        self.ob_ma_manutencao.setFont(font10)
        self.ob_ma_manutencao.setLayoutDirection(Qt.LeftToRight)
        self.ob_ma_manutencao.setAutoExclusive(False)

        self.horizontalLayout_36.addWidget(self.ob_ma_manutencao)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(20, -1, -1, -1)
        self.ob_ma_borracharia = QRadioButton(self.layoutWidget_8)
        self.ob_ma_borracharia.setObjectName(u"ob_ma_borracharia")
        self.ob_ma_borracharia.setFont(font10)
        self.ob_ma_borracharia.setLayoutDirection(Qt.LeftToRight)
        self.ob_ma_borracharia.setAutoExclusive(False)

        self.horizontalLayout_38.addWidget(self.ob_ma_borracharia)


        self.horizontalLayout_36.addLayout(self.horizontalLayout_38)


        self.verticalLayout_7.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(20, -1, -1, -1)
        self.ob_ma_mecanica = QRadioButton(self.layoutWidget_8)
        self.ob_ma_mecanica.setObjectName(u"ob_ma_mecanica")
        self.ob_ma_mecanica.setFont(font10)
        self.ob_ma_mecanica.setLayoutDirection(Qt.LeftToRight)
        self.ob_ma_mecanica.setAutoExclusive(False)

        self.horizontalLayout_33.addWidget(self.ob_ma_mecanica)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(20, -1, -1, -1)
        self.ob_ma_funilaria = QRadioButton(self.layoutWidget_8)
        self.ob_ma_funilaria.setObjectName(u"ob_ma_funilaria")
        self.ob_ma_funilaria.setFont(font10)
        self.ob_ma_funilaria.setLayoutDirection(Qt.LeftToRight)
        self.ob_ma_funilaria.setAutoExclusive(False)

        self.horizontalLayout_40.addWidget(self.ob_ma_funilaria)


        self.horizontalLayout_33.addLayout(self.horizontalLayout_40)


        self.verticalLayout_7.addLayout(self.horizontalLayout_33)

        self.layoutWidget_9 = QWidget(self.widget_2)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(40, 130, 491, 61))
        self.horizontalLayout_30 = QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_30.setSpacing(10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_30.setContentsMargins(15, 0, 15, 0)
        self.label_54 = QLabel(self.layoutWidget_9)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(45, 45))
        self.label_54.setMaximumSize(QSize(45, 45))
        self.label_54.setPixmap(QPixmap(u":/icons/icons/prefixo.png"))
        self.label_54.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_54)

        self.txt_ma_carro = QLineEdit(self.layoutWidget_9)
        self.txt_ma_carro.setObjectName(u"txt_ma_carro")
        self.txt_ma_carro.setFont(font9)
        self.txt_ma_carro.setStyleSheet(u"border-left:None;\n"
"border-right:None;\n"
"border-top:None;\n"
"border-bottom: 2px solid #0763a4;")

        self.horizontalLayout_30.addWidget(self.txt_ma_carro)

        self.layoutWidget_10 = QWidget(self.widget_2)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(40, 510, 491, 121))
        self.horizontalLayout_34 = QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.layoutWidget_10)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_34.addWidget(self.label_60)

        self.btn_ma_salvar = QPushButton(self.layoutWidget_10)
        self.btn_ma_salvar.setObjectName(u"btn_ma_salvar")
        self.btn_ma_salvar.setMaximumSize(QSize(16777215, 40))
        self.btn_ma_salvar.setFont(font10)
        self.btn_ma_salvar.setStyleSheet(u"QPushButton{\n"
"	color: #161616;\n"
"	background-color: rgb(108, 156, 196);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"	background-color: rgb(116, 164, 191);\n"
"}")

        self.horizontalLayout_34.addWidget(self.btn_ma_salvar)

        self.label_61 = QLabel(self.layoutWidget_10)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_34.addWidget(self.label_61)

        self.horizontalLayout_34.setStretch(0, 10)
        self.horizontalLayout_34.setStretch(1, 20)
        self.horizontalLayout_34.setStretch(2, 10)

        self.verticalLayout_8.addWidget(self.frame_6)

        self.paginas.addWidget(self.pg_materiais)

        self.horizontalLayout_48.addWidget(self.paginas)

        MainPortaria.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainPortaria)

        self.paginas.setCurrentIndex(5)
        self.cmb_registro_fornecedor.setCurrentIndex(-1)
        self.cmb_registro_nome.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainPortaria)
    # setupUi

    def retranslateUi(self, MainPortaria):
        MainPortaria.setWindowTitle(QCoreApplication.translate("MainPortaria", u"MainWindow", None))
        self.label_2.setText("")
        self.lbl_logo.setText("")
        self.btn_pg_fornecedor.setText(QCoreApplication.translate("MainPortaria", u"Fornecedor", None))
        self.btn_pg_home.setText(QCoreApplication.translate("MainPortaria", u"Inicio", None))
        self.btn_pg_terceiros.setText(QCoreApplication.translate("MainPortaria", u"Terceiros", None))
        self.btn_pg_colaboradores.setText(QCoreApplication.translate("MainPortaria", u"Colaboradores", None))
        self.btn_pg_materiais.setText(QCoreApplication.translate("MainPortaria", u"Materiais", None))
        self.btn_pg_chave.setText(QCoreApplication.translate("MainPortaria", u"Chaves", None))
        self.label_3.setText(QCoreApplication.translate("MainPortaria", u"Seja Bem Vindo a Via\u00e7\u00e3o", None))
        self.label_4.setText(QCoreApplication.translate("MainPortaria", u"Recados", None))
        self.label_15.setText(QCoreApplication.translate("MainPortaria", u"Empresas na Via\u00e7\u00e3o:", None))
        ___qtablewidgetitem = self.tabela_fornecedor.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainPortaria", u"Fornecedor/Visitante", None));
        ___qtablewidgetitem1 = self.tabela_fornecedor.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainPortaria", u"Placa", None));
        ___qtablewidgetitem2 = self.tabela_fornecedor.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainPortaria", u"Entrada", None));
        ___qtablewidgetitem3 = self.tabela_fornecedor.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainPortaria", u"Sa\u00edda", None));
        self.label_5.setText(QCoreApplication.translate("MainPortaria", u"Fornecedor/Visitante", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.label_10.setText("")
        self.txt_registro_cracha.setPlaceholderText(QCoreApplication.translate("MainPortaria", u"Crach\u00e1", None))
        self.label_8.setText("")
        self.txt_registro_rg.setPlaceholderText(QCoreApplication.translate("MainPortaria", u"RG", None))
        self.label_9.setText("")
        self.txt_registro_placa.setPlaceholderText(QCoreApplication.translate("MainPortaria", u"Placa", None))
        self.label_11.setText("")
        self.label_12.setText("")
        self.btn_registrar_fornecedor.setText(QCoreApplication.translate("MainPortaria", u"Salvar", None))
        self.btn_f_limpar.setText(QCoreApplication.translate("MainPortaria", u"Limpar", None))
        self.btn_pg_novo_fornecedor.setText(QCoreApplication.translate("MainPortaria", u"Novo", None))
        self.label_48.setText(QCoreApplication.translate("MainPortaria", u"Novo Fornecedor/Visitante", None))
        self.label_55.setText(QCoreApplication.translate("MainPortaria", u"Novo Cadastro", None))
        self.label_56.setText("")
        self.txt_novo_fornecedor.setPlaceholderText(QCoreApplication.translate("MainPortaria", u"Empresa/Visitante", None))
        self.label_58.setText("")
        self.txt_novo_entregador.setPlaceholderText(QCoreApplication.translate("MainPortaria", u"Nome", None))
        self.label_62.setText("")
        self.txt_novo_rg.setPlaceholderText(QCoreApplication.translate("MainPortaria", u"RG", None))
        self.label_63.setText("")
        self.txt_novo_placa.setPlaceholderText(QCoreApplication.translate("MainPortaria", u"Placa", None))
        self.btn_novo_fornecedor.setText(QCoreApplication.translate("MainPortaria", u"Salvar", None))
        self.btn_limpar_cadastro_fornecedor.setText(QCoreApplication.translate("MainPortaria", u"Limpar", None))
        self.btn_voltar_fornecedor.setText(QCoreApplication.translate("MainPortaria", u"Voltar", None))
        self.label_16.setText(QCoreApplication.translate("MainPortaria", u"Empresas na Parceiras:", None))
        ___qtablewidgetitem4 = self.tabela_terceiros.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainPortaria", u"Via\u00e7\u00e3o", None));
        ___qtablewidgetitem5 = self.tabela_terceiros.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainPortaria", u"Total", None));
        ___qtablewidgetitem6 = self.tabela_terceiros.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainPortaria", u"Quantidade", None));
        self.label_17.setText(QCoreApplication.translate("MainPortaria", u"Registrar Entrada/Sa\u00edda", None))
        self.label_18.setText("")
        self.txt_reg_terceiros_prefixo.setPlaceholderText(QCoreApplication.translate("MainPortaria", u"Prefixo", None))
        self.label_19.setText("")
        self.btn_reg_terceiros_entrada.setText(QCoreApplication.translate("MainPortaria", u"Entrada", None))
        self.btn_reg_terceiros_saida.setText(QCoreApplication.translate("MainPortaria", u"Sa\u00edda", None))
        self.label_14.setText(QCoreApplication.translate("MainPortaria", u"Terceiros", None))
        self.label_32.setText(QCoreApplication.translate("MainPortaria", u"Colaboradores", None))
        self.label_59.setText(QCoreApplication.translate("MainPortaria", u"Registrar Entrada/Sa\u00edda", None))
        self.groupBox.setTitle("")
        self.ob_colaboradores_entrada.setText(QCoreApplication.translate("MainPortaria", u"Entrada", None))
        self.ob_colaboradores_entradaA.setText(QCoreApplication.translate("MainPortaria", u"Entrada do almo\u00e7o", None))
        self.ob_colaboradores_saidaA.setText(QCoreApplication.translate("MainPortaria", u"Sa\u00edda para almo\u00e7o", None))
        self.ob_colaboradores_saida.setText(QCoreApplication.translate("MainPortaria", u"Sa\u00edda", None))
        self.btn_colaboradores_salvar.setText(QCoreApplication.translate("MainPortaria", u"Salvar", None))
        self.label_64.setText("")
        self.label_66.setText("")
        self.label_42.setText(QCoreApplication.translate("MainPortaria", u"Chaves", None))
        self.label_24.setText(QCoreApplication.translate("MainPortaria", u"Chaves em uso:", None))
        ___qtablewidgetitem7 = self.tabela_chaves.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainPortaria", u"Chave", None));
        ___qtablewidgetitem8 = self.tabela_chaves.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainPortaria", u"Setor", None));
        ___qtablewidgetitem9 = self.tabela_chaves.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainPortaria", u"hora", None));
        ___qtablewidgetitem10 = self.tabela_chaves.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainPortaria", u"Respons\u00e1vel", None));
        ___qtablewidgetitem11 = self.tabela_chaves.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainPortaria", u"Devolver", None));
        self.label_35.setText(QCoreApplication.translate("MainPortaria", u"Registrar Retirada", None))
        self.label_40.setText("")
        self.btn_ch_salvar.setText(QCoreApplication.translate("MainPortaria", u"Salvar", None))
        self.label_41.setText("")
        self.label_36.setText("")
        self.txt_chave_nome.setPlaceholderText(QCoreApplication.translate("MainPortaria", u"Nome", None))
        self.label_37.setText("")
        self.label_43.setText("")
        self.txt_ch_chave.setPlaceholderText(QCoreApplication.translate("MainPortaria", u"N\u00ba", None))
        self.label_38.setText("")
        self.label_52.setText(QCoreApplication.translate("MainPortaria", u"Materiais", None))
        self.label_57.setText("")
        self.label_45.setText("")
        self.txt_m_motorista.setPlaceholderText(QCoreApplication.translate("MainPortaria", u"Motorista", None))
        self.label_44.setText("")
        self.txt_m_carro.setPlaceholderText(QCoreApplication.translate("MainPortaria", u"Prefixo", None))
        self.label_39.setText(QCoreApplication.translate("MainPortaria", u"Registrar Marreta/Vassoura", None))
        self.ob_m_vassoura.setText(QCoreApplication.translate("MainPortaria", u"Vassoura", None))
        self.ob_m_marreta.setText(QCoreApplication.translate("MainPortaria", u"Marreta", None))
        self.label_67.setText("")
        self.btn_m_salvar.setText(QCoreApplication.translate("MainPortaria", u"Salvar", None))
        self.label_65.setText("")
        self.label_53.setText(QCoreApplication.translate("MainPortaria", u"Registrar Ficha de Manuten\u00e7\u00e3o", None))
        self.ob_ma_lavagem.setText(QCoreApplication.translate("MainPortaria", u"Lavagem Interna", None))
        self.ob_ma_eletrica.setText(QCoreApplication.translate("MainPortaria", u"El\u00e9trica", None))
        self.ob_ma_manutencao.setText(QCoreApplication.translate("MainPortaria", u"Manuten\u00e7\u00e3o", None))
        self.ob_ma_borracharia.setText(QCoreApplication.translate("MainPortaria", u"Borracharia", None))
        self.ob_ma_mecanica.setText(QCoreApplication.translate("MainPortaria", u"Mec\u00e2nica", None))
        self.ob_ma_funilaria.setText(QCoreApplication.translate("MainPortaria", u"Funilaria", None))
        self.label_54.setText("")
        self.txt_ma_carro.setPlaceholderText(QCoreApplication.translate("MainPortaria", u"Prefixo", None))
        self.label_60.setText("")
        self.btn_ma_salvar.setText(QCoreApplication.translate("MainPortaria", u"Salvar", None))
        self.label_61.setText("")
    # retranslateUi

