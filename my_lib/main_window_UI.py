# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.setWindowModality(QtCore.Qt.WindowModal)
        main_window.resize(1277, 822)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(main_window)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_COM = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_COM.sizePolicy().hasHeightForWidth())
        self.pushButton_COM.setSizePolicy(sizePolicy)
        self.pushButton_COM.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_COM.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton_COM.setStyleSheet("")
        self.pushButton_COM.setObjectName("pushButton_COM")
        self.horizontalLayout.addWidget(self.pushButton_COM)
        self.pushButton_TCP = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_TCP.sizePolicy().hasHeightForWidth())
        self.pushButton_TCP.setSizePolicy(sizePolicy)
        self.pushButton_TCP.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_TCP.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton_TCP.setStyleSheet("")
        self.pushButton_TCP.setObjectName("pushButton_TCP")
        self.horizontalLayout.addWidget(self.pushButton_TCP)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.pushButton_link_setting = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_link_setting.sizePolicy().hasHeightForWidth())
        self.pushButton_link_setting.setSizePolicy(sizePolicy)
        self.pushButton_link_setting.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_link_setting.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_link_setting.setText("")
        self.pushButton_link_setting.setObjectName("pushButton_link_setting")
        self.horizontalLayout_2.addWidget(self.pushButton_link_setting)
        self.pushButton_link_ss = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_link_ss.sizePolicy().hasHeightForWidth())
        self.pushButton_link_ss.setSizePolicy(sizePolicy)
        self.pushButton_link_ss.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_link_ss.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton_link_ss.setText("")
        self.pushButton_link_ss.setObjectName("pushButton_link_ss")
        self.horizontalLayout_2.addWidget(self.pushButton_link_ss)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_curves_setting = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_curves_setting.sizePolicy().hasHeightForWidth())
        self.pushButton_curves_setting.setSizePolicy(sizePolicy)
        self.pushButton_curves_setting.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_curves_setting.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_curves_setting.setText("")
        self.pushButton_curves_setting.setObjectName("pushButton_curves_setting")
        self.horizontalLayout_3.addWidget(self.pushButton_curves_setting)
        self.pushButton_curves_ss = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_curves_ss.sizePolicy().hasHeightForWidth())
        self.pushButton_curves_ss.setSizePolicy(sizePolicy)
        self.pushButton_curves_ss.setMinimumSize(QtCore.QSize(80, 40))
        self.pushButton_curves_ss.setMaximumSize(QtCore.QSize(100, 50))
        self.pushButton_curves_ss.setText("")
        self.pushButton_curves_ss.setObjectName("pushButton_curves_ss")
        self.horizontalLayout_3.addWidget(self.pushButton_curves_ss)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_7 = QtWidgets.QGroupBox(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tableWidget_channels = QtWidgets.QTableWidget(self.groupBox_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_channels.sizePolicy().hasHeightForWidth())
        self.tableWidget_channels.setSizePolicy(sizePolicy)
        self.tableWidget_channels.setMinimumSize(QtCore.QSize(300, 89))
        self.tableWidget_channels.setMaximumSize(QtCore.QSize(16777215, 90))
        self.tableWidget_channels.setObjectName("tableWidget_channels")
        self.tableWidget_channels.setColumnCount(0)
        self.tableWidget_channels.setRowCount(0)
        self.horizontalLayout_8.addWidget(self.tableWidget_channels)
        self.horizontalLayout_4.addWidget(self.groupBox_7)
        self.label_logo = QtWidgets.QLabel(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_logo.sizePolicy().hasHeightForWidth())
        self.label_logo.setSizePolicy(sizePolicy)
        self.label_logo.setMinimumSize(QtCore.QSize(120, 120))
        self.label_logo.setMaximumSize(QtCore.QSize(150, 150))
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.horizontalLayout_4.addWidget(self.label_logo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.widget = QtWidgets.QWidget(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_curves = QtWidgets.QVBoxLayout()
        self.verticalLayout_curves.setObjectName("verticalLayout_curves")
        self.verticalLayout_3.addLayout(self.verticalLayout_curves)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(main_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QtCore.QSize(400, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(500, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 120))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_saveData_ss = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_saveData_ss.sizePolicy().hasHeightForWidth())
        self.pushButton_saveData_ss.setSizePolicy(sizePolicy)
        self.pushButton_saveData_ss.setMinimumSize(QtCore.QSize(120, 40))
        self.pushButton_saveData_ss.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton_saveData_ss.setObjectName("pushButton_saveData_ss")
        self.horizontalLayout_6.addWidget(self.pushButton_saveData_ss)
        self.pushButton_report = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_report.sizePolicy().hasHeightForWidth())
        self.pushButton_report.setSizePolicy(sizePolicy)
        self.pushButton_report.setMinimumSize(QtCore.QSize(120, 40))
        self.pushButton_report.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton_report.setObjectName("pushButton_report")
        self.horizontalLayout_6.addWidget(self.pushButton_report)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 160))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 500))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textEdit_patientImf = QtWidgets.QTextEdit(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_patientImf.sizePolicy().hasHeightForWidth())
        self.textEdit_patientImf.setSizePolicy(sizePolicy)
        self.textEdit_patientImf.setMinimumSize(QtCore.QSize(0, 100))
        self.textEdit_patientImf.setMaximumSize(QtCore.QSize(16777215, 800))
        self.textEdit_patientImf.setObjectName("textEdit_patientImf")
        self.verticalLayout_4.addWidget(self.textEdit_patientImf)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 80))
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.lcdNumber_heart = QtWidgets.QLCDNumber(self.groupBox_5)
        self.lcdNumber_heart.setMinimumSize(QtCore.QSize(100, 30))
        self.lcdNumber_heart.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lcdNumber_heart.setObjectName("lcdNumber_heart")
        self.horizontalLayout_7.addWidget(self.lcdNumber_heart)
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.lcdNumber_heart_2 = QtWidgets.QLCDNumber(self.groupBox_5)
        self.lcdNumber_heart_2.setMinimumSize(QtCore.QSize(100, 30))
        self.lcdNumber_heart_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lcdNumber_heart_2.setObjectName("lcdNumber_heart_2")
        self.horizontalLayout_7.addWidget(self.lcdNumber_heart_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_7.addWidget(self.groupBox_5)
        self.pushButton_fold = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_fold.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_fold.setMaximumSize(QtCore.QSize(16777215, 20))
        self.pushButton_fold.setText("")
        self.pushButton_fold.setObjectName("pushButton_fold")
        self.verticalLayout_7.addWidget(self.pushButton_fold)
        self.groupBox_TFT = QtWidgets.QGroupBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_TFT.sizePolicy().hasHeightForWidth())
        self.groupBox_TFT.setSizePolicy(sizePolicy)
        self.groupBox_TFT.setObjectName("groupBox_TFT")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_TFT)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_FFT = QtWidgets.QVBoxLayout()
        self.verticalLayout_FFT.setObjectName("verticalLayout_FFT")
        self.verticalLayout_6.addLayout(self.verticalLayout_FFT)
        self.verticalLayout_7.addWidget(self.groupBox_TFT)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Form"))
        self.groupBox.setTitle(_translate("main_window", "通信设置"))
        self.pushButton_COM.setText(_translate("main_window", "COM"))
        self.pushButton_TCP.setText(_translate("main_window", "TCP"))
        self.groupBox_2.setTitle(_translate("main_window", "绘图控制"))
        self.groupBox_7.setTitle(_translate("main_window", "通道选择"))
        self.pushButton_saveData_ss.setText(_translate("main_window", "开始保存"))
        self.pushButton_report.setText(_translate("main_window", "导出报告"))
        self.groupBox_4.setTitle(_translate("main_window", "患者信息"))
        self.groupBox_5.setTitle(_translate("main_window", "数据"))
        self.label.setText(_translate("main_window", "心率"))
        self.label_2.setText(_translate("main_window", "HVR"))
        self.groupBox_TFT.setTitle(_translate("main_window", "FFT频谱"))
