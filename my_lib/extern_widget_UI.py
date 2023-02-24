# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'extern_widget_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_extern_widget(object):
    def setupUi(self, extern_widget):
        extern_widget.setObjectName("extern_widget")
        extern_widget.resize(500, 875)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(extern_widget.sizePolicy().hasHeightForWidth())
        extern_widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(extern_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(extern_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_FFT = QtWidgets.QVBoxLayout()
        self.verticalLayout_FFT.setObjectName("verticalLayout_FFT")
        self.verticalLayout_2.addLayout(self.verticalLayout_FFT)
        self.verticalLayout.addWidget(self.frame_2)
        self.pushButton_show = QtWidgets.QPushButton(extern_widget)
        self.pushButton_show.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("GUI/UD_fold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_show.setIcon(icon)
        self.pushButton_show.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_show.setFlat(True)
        self.pushButton_show.setObjectName("pushButton_show")
        self.verticalLayout.addWidget(self.pushButton_show)
        self.verticalLayout_btn_img = QtWidgets.QVBoxLayout()
        self.verticalLayout_btn_img.setObjectName("verticalLayout_btn_img")
        self.verticalLayout.addLayout(self.verticalLayout_btn_img)

        self.retranslateUi(extern_widget)
        QtCore.QMetaObject.connectSlotsByName(extern_widget)

    def retranslateUi(self, extern_widget):
        _translate = QtCore.QCoreApplication.translate
        extern_widget.setWindowTitle(_translate("extern_widget", "Form"))
