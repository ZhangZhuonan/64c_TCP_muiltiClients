# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_widget_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings_Form(object):
    def setupUi(self, Settings_Form):
        Settings_Form.setObjectName("Settings_Form")
        Settings_Form.resize(375, 851)
        Settings_Form.setStyleSheet("QToolBox{background:white;\n"
"    border:2px solid rgb(230, 230, 230);\n"
"    border-top-right-radius:20px;\n"
"    border-bottom-right-radius:20px;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Settings_Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget_1 = QtWidgets.QTableWidget(Settings_Form)
        self.tableWidget_1.setStyleSheet("")
        self.tableWidget_1.setObjectName("tableWidget_1")
        self.tableWidget_1.setColumnCount(0)
        self.tableWidget_1.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget_1)

        self.retranslateUi(Settings_Form)
        QtCore.QMetaObject.connectSlotsByName(Settings_Form)

    def retranslateUi(self, Settings_Form):
        _translate = QtCore.QCoreApplication.translate
        Settings_Form.setWindowTitle(_translate("Settings_Form", "456"))
