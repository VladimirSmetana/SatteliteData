# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 658)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 10, 271, 371))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.delta_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.delta_edit.setObjectName("delta_edit")
        self.gridLayout.addWidget(self.delta_edit, 1, 3, 1, 1)
        self.omega_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.omega_edit.setObjectName("omega_edit")
        self.gridLayout.addWidget(self.omega_edit, 3, 3, 1, 1)
        self.kd_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.kd_edit.setObjectName("kd_edit")
        self.gridLayout.addWidget(self.kd_edit, 5, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.q_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.q_edit.setObjectName("q_edit")
        self.gridLayout.addWidget(self.q_edit, 2, 3, 1, 1)
        self.kf_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.kf_edit.setObjectName("kf_edit")
        self.gridLayout.addWidget(self.kf_edit, 4, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.le_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.le_edit.setObjectName("le_edit")
        self.gridLayout.addWidget(self.le_edit, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)
        self.pic_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.pic_edit.setObjectName("pic_edit")
        self.gridLayout.addWidget(self.pic_edit, 6, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 6, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 390, 271, 221))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalSlider = QtWidgets.QSlider(self.gridLayoutWidget_2)
        self.verticalSlider.setMinimum(250)
        self.verticalSlider.setMaximum(400)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout_2.addWidget(self.verticalSlider, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.Hlabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Hlabel.setFont(font)
        self.Hlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.Hlabel.setObjectName("Hlabel")
        self.horizontalLayout_2.addWidget(self.Hlabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_2.addWidget(self.label_28)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_2.addWidget(self.label_29)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(660, 10, 291, 604))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.BEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.BEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.BEdit_7.setObjectName("BEdit_7")
        self.gridLayout_3.addWidget(self.BEdit_7, 0, 1, 1, 1)
        self.s2Edit_19 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.s2Edit_19.setAlignment(QtCore.Qt.AlignCenter)
        self.s2Edit_19.setObjectName("s2Edit_19")
        self.gridLayout_3.addWidget(self.s2Edit_19, 9, 1, 1, 1)
        self.fvzEdit_16 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.fvzEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.fvzEdit_16.setObjectName("fvzEdit_16")
        self.gridLayout_3.addWidget(self.fvzEdit_16, 11, 1, 1, 1)
        self.d2Edit_23 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.d2Edit_23.setAlignment(QtCore.Qt.AlignCenter)
        self.d2Edit_23.setObjectName("d2Edit_23")
        self.gridLayout_3.addWidget(self.d2Edit_23, 16, 1, 1, 1)
        self.rgzEdit_20 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.rgzEdit_20.setAlignment(QtCore.Qt.AlignCenter)
        self.rgzEdit_20.setObjectName("rgzEdit_20")
        self.gridLayout_3.addWidget(self.rgzEdit_20, 13, 1, 1, 1)
        self.mEdit_21 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.mEdit_21.setAlignment(QtCore.Qt.AlignCenter)
        self.mEdit_21.setObjectName("mEdit_21")
        self.gridLayout_3.addWidget(self.mEdit_21, 14, 1, 1, 1)
        self.LtkEdit_24 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.LtkEdit_24.setAlignment(QtCore.Qt.AlignCenter)
        self.LtkEdit_24.setObjectName("LtkEdit_24")
        self.gridLayout_3.addWidget(self.LtkEdit_24, 17, 1, 1, 1)
        self.fekvEdit_11 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.fekvEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.fekvEdit_11.setObjectName("fekvEdit_11")
        self.gridLayout_3.addWidget(self.fekvEdit_11, 6, 1, 1, 1)
        self.DvzEdit_17 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.DvzEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.DvzEdit_17.setObjectName("DvzEdit_17")
        self.gridLayout_3.addWidget(self.DvzEdit_17, 7, 1, 1, 1)
        self.frzEdit_15 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.frzEdit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.frzEdit_15.setObjectName("frzEdit_15")
        self.gridLayout_3.addWidget(self.frzEdit_15, 10, 1, 1, 1)
        self.rvzEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.rvzEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.rvzEdit_8.setObjectName("rvzEdit_8")
        self.gridLayout_3.addWidget(self.rvzEdit_8, 12, 1, 1, 1)
        self.dEdit_18 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.dEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.dEdit_18.setObjectName("dEdit_18")
        self.gridLayout_3.addWidget(self.dEdit_18, 8, 1, 1, 1)
        self.NEdit_12 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.NEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.NEdit_12.setObjectName("NEdit_12")
        self.gridLayout_3.addWidget(self.NEdit_12, 3, 1, 1, 1)
        self.pEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.pEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.pEdit_9.setObjectName("pEdit_9")
        self.gridLayout_3.addWidget(self.pEdit_9, 1, 1, 1, 1)
        self.iEdit_13 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.iEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.iEdit_13.setObjectName("iEdit_13")
        self.gridLayout_3.addWidget(self.iEdit_13, 4, 1, 1, 1)
        self.TEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.TEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.TEdit_10.setObjectName("TEdit_10")
        self.gridLayout_3.addWidget(self.TEdit_10, 2, 1, 1, 1)
        self.d1Edit_22 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.d1Edit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.d1Edit_22.setObjectName("d1Edit_22")
        self.gridLayout_3.addWidget(self.d1Edit_22, 15, 1, 1, 1)
        self.DminEdit_14 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.DminEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.DminEdit_14.setObjectName("DminEdit_14")
        self.gridLayout_3.addWidget(self.DminEdit_14, 5, 1, 1, 1)
        self.DtkEdit_25 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.DtkEdit_25.setAlignment(QtCore.Qt.AlignCenter)
        self.DtkEdit_25.setObjectName("DtkEdit_25")
        self.gridLayout_3.addWidget(self.DtkEdit_25, 18, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 5, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 6, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 7, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 8, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 9, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 10, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 11, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 12, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 13, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 14, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 15, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 16, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 17, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 18, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(320, 560, 331, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calc_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.calc_button.setFont(font)
        self.calc_button.setObjectName("calc_button")
        self.horizontalLayout.addWidget(self.calc_button)
        self.exit_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout.addWidget(self.exit_button)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(319, 9, 331, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.img_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.img_1.setStyleSheet("\n"
"")
        self.img_1.setText("")
        self.img_1.setObjectName("img_1")
        self.verticalLayout_4.addWidget(self.img_1)
        self.img_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.img_2.setStyleSheet("")
        self.img_2.setText("")
        self.img_2.setObjectName("img_2")
        self.verticalLayout_4.addWidget(self.img_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 967, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.delta_edit.setText(_translate("MainWindow", "0.15"))
        self.omega_edit.setText(_translate("MainWindow", "1.76"))
        self.kd_edit.setText(_translate("MainWindow", "1.2"))
        self.label_3.setText(_translate("MainWindow", "q"))
        self.label.setText(_translate("MainWindow", "Lэ, м"))
        self.label_2.setText(_translate("MainWindow", "Δ, м"))
        self.q_edit.setText(_translate("MainWindow", "0.35"))
        self.kf_edit.setText(_translate("MainWindow", "0.25"))
        self.label_5.setText(_translate("MainWindow", "Kf"))
        self.label_4.setText(_translate("MainWindow", "𝜔, гр"))
        self.le_edit.setText(_translate("MainWindow", "1.5"))
        self.label_6.setText(_translate("MainWindow", "Kd"))
        self.pic_edit.setText(_translate("MainWindow", "9"))
        self.label_8.setText(_translate("MainWindow", "lел.п."))
        self.label_7.setText(_translate("MainWindow", "H, км:"))
        self.Hlabel.setText(_translate("MainWindow", "250"))
        self.label_28.setText(_translate("MainWindow", "400"))
        self.label_29.setText(_translate("MainWindow", "250"))
        self.label_9.setText(_translate("MainWindow", "B, км"))
        self.label_10.setText(_translate("MainWindow", "р, км"))
        self.label_11.setText(_translate("MainWindow", "Т, с"))
        self.label_12.setText(_translate("MainWindow", "N, об"))
        self.label_13.setText(_translate("MainWindow", "i, гр"))
        self.label_14.setText(_translate("MainWindow", "Dmin, м"))
        self.label_15.setText(_translate("MainWindow", "fэкв, м"))
        self.label_16.setText(_translate("MainWindow", "Dвз, м"))
        self.label_17.setText(_translate("MainWindow", "d, м"))
        self.label_18.setText(_translate("MainWindow", "s2, м"))
        self.label_19.setText(_translate("MainWindow", "fгз, м"))
        self.label_20.setText(_translate("MainWindow", "fвз, м"))
        self.label_21.setText(_translate("MainWindow", "rвз, м"))
        self.label_22.setText(_translate("MainWindow", "rгз, м"))
        self.label_23.setText(_translate("MainWindow", "m"))
        self.label_24.setText(_translate("MainWindow", "d1, м"))
        self.label_25.setText(_translate("MainWindow", "d2, м"))
        self.label_26.setText(_translate("MainWindow", "Lтк, м"))
        self.label_27.setText(_translate("MainWindow", "Dтк, м"))
        self.calc_button.setText(_translate("MainWindow", "Расчет"))
        self.exit_button.setText(_translate("MainWindow", "Выход"))
