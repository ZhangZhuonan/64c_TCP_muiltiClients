from my_lib.main_window_UI import *
# 库引用
# from PyQt5.QtWidgets import QApplication, QMainWindow,  QFileDialog, QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QImage,QPixmap,QIcon
import cv2
import numpy as np


class MyWindow(QWidget, Ui_main_window):
    # 信号必须放在初始化之前作为全局变量，否则无法正确emit
    trig_link_ss = pyqtSignal(object, object)   # 通信连接开始-结束信号[link_mode, link_state]
    trig_link_setting = pyqtSignal()            # 打开通信设置界面信号
    trig_curves_ss = pyqtSignal(object)         # 曲线绘制开始-结束信号
    trig_curves_setting = pyqtSignal()          # 曲线设置信号
    trig_curves_channelsSelected = pyqtSignal(object) # 选中通道信号
    trig_saveData_ss = pyqtSignal(object)       # 保存数据开始-结束信号
    trig_report = pyqtSignal(object)            # 导出报告信号
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.UI_init()
        self.link_mode = 'COM'  # 连接模式
        self.link_state = False # 连接标志位
        self.curves_continue = False    # 曲线连续绘制标志位
        self.saveData_state = False     # 保存数据标志位：T-开始保存，F-停止保存
        self.Is_showTFT = True          # TFT窗口显示

    def UI_init(self):
        self.setWindowTitle('SIBET-12LEAD-GK')
        self.draw()
        # 连接设置按键
            # 按键状态设置
        self.pushButton_COM.setCheckable(True)      # 设置成开关按键
        self.pushButton_TCP.setCheckable(True)
        self.pushButton_COM.setChecked(True)        # 默认选择串口通信模式
            # 设置按键信号连接
        self.pushButton_COM.clicked.connect(self.COM_selected_callback)
        self.pushButton_TCP.clicked.connect(self.TCP_selected_callback)
        self.pushButton_link_ss.clicked.connect(self.link_ss_callback)
        self.pushButton_link_setting.clicked.connect(self.link_setting_callback)
            # 设置按键图标
                # 设置按键
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("GUI/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_link_setting.setIcon(icon1)
        self.pushButton_link_setting.setIconSize(QtCore.QSize(30, 30))
                # 开始结束按键
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("GUI/no_link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_link_ss.setIcon(icon1)
        self.pushButton_link_ss.setIconSize(QtCore.QSize(30, 30))
        # 曲线控制按键
            # 设置按键信号槽连接
        self.pushButton_curves_ss.clicked.connect(self.curves_ss_callback)
        self.pushButton_curves_setting.clicked.connect(self.curves_setting_callback)
            # 设置按键图标
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("GUI/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_curves_setting.setIcon(icon1)
        self.pushButton_curves_setting.setIconSize(QtCore.QSize(30, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("GUI/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_curves_ss.setIcon(icon1)
        self.pushButton_curves_ss.setIconSize(QtCore.QSize(30, 30))
        # 曲线通道选择界面
        self.init_channels_selecter()
        # 附加功能界面
            # 界面绘制
        self.pushButton_saveData_ss.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("GUI/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_saveData_ss.setIcon(icon1)
        self.pushButton_saveData_ss.setIconSize(QtCore.QSize(20, 20))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("GUI/report.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_report.setIcon(icon1)
        self.pushButton_report.setIconSize(QtCore.QSize(20, 20))
            # 信号连接
        self.pushButton_saveData_ss.clicked.connect(self.saveData_ss_callback)
        self.pushButton_report.clicked.connect(self.report_callback)
        # TFT折叠
        self.pushButton_fold.setFlat(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("GUI/ud_fold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_fold.setIcon(icon1)
        self.pushButton_fold.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_fold.clicked.connect(self.fold_TFT_callback)

    # 图标绘制
    def draw(self):
        try:
            img_src = cv2.imread('GUI\logo.jpg')
        except:
            return
        img_new = np.empty(img_src.shape)
        img_new[:,:,0] = img_src[:,:,2]
        img_new[:, :, 1] = img_src[:, :, 1]
        img_new[:, :, 2] = img_src[:, :, 0]
        img_src = img_new.astype(np.uint8)
        label_height = 150
        label_width = label_height * (img_src.shape[1] / img_src.shape[0])
        temp_imgSrc = QImage(img_src, img_src.shape[1], img_src.shape[0],img_src.shape[1]*3, QImage.Format_RGB888)
        # 将图片转换为QPixmap方便显示
        pixmap_imgSrc = QPixmap.fromImage(temp_imgSrc)
        # 使用label进行显示
        self.label_logo.setPixmap(pixmap_imgSrc)

        self.setWindowIcon(QIcon('GUI\logo.jpg'))

    # 串口选择回调函数
    def COM_selected_callback(self):
        if self.link_mode == 'TCP':
            self.pushButton_TCP.setChecked(False)
            self.link_mode = 'COM'
        else:
            self.pushButton_COM.setChecked(True)

    # 网络选择回调函数
    def TCP_selected_callback(self):
        if self.link_mode == 'COM':
            self.pushButton_COM.setChecked(False)
            self.link_mode = 'TCP'
        else:
            self.pushButton_TCP.setChecked(True)

    # 通信开始-结束回调函数
    def link_ss_callback(self):

        if self.link_state is False:
            self.link_state = True
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("GUI/link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_link_ss.setIcon(icon1)
            self.pushButton_link_ss.setIconSize(QtCore.QSize(30, 30))
            self.pushButton_TCP.setEnabled(False)
            self.pushButton_COM.setEnabled(False)
            self.pushButton_link_setting.setEnabled(False)
            self.trig_link_ss.emit(self.link_mode, self.link_state)
        else:
            self.link_state = False
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("GUI/no_link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_link_ss.setIcon(icon1)
            self.pushButton_link_ss.setIconSize(QtCore.QSize(30, 30))
            self.pushButton_TCP.setEnabled(True)
            self.pushButton_COM.setEnabled(True)
            self.pushButton_link_setting.setEnabled(True)
            self.trig_link_ss.emit(self.link_mode, self.link_state)

    # 通信连接失败反馈函数
    def link_false_callback(self):
        self.link_state = False
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("GUI/no_link.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_link_ss.setIcon(icon1)
        self.pushButton_link_ss.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_TCP.setEnabled(True)
        self.pushButton_COM.setEnabled(True)
        self.pushButton_link_setting.setEnabled(True)

    # 通信设置
    def link_setting_callback(self):
        self.trig_link_setting.emit()

    # 曲线开始-结束绘制按键回调函数
    def curves_ss_callback(self):
        if self.curves_continue is False:
            self.curves_continue = True
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("GUI/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_curves_ss.setIcon(icon1)
            self.pushButton_curves_ss.setIconSize(QtCore.QSize(30, 30))
            self.pushButton_curves_setting.setEnabled(False)    # 失效曲线设置按键
            self.trig_curves_ss.emit(self.curves_continue)  #向主控程序传递开始曲线绘制信号
        else:
            self.curves_continue = False
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("GUI/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_curves_ss.setIcon(icon1)
            self.pushButton_curves_ss.setIconSize(QtCore.QSize(30, 30))
            self.pushButton_curves_setting.setEnabled(True)    # 使能曲线设置按键
            self.trig_curves_ss.emit(self.curves_continue)  #向主控程序传递开始曲线绘制信号

    # 曲线设置回调函数
    def curves_setting_callback(self):
        self.trig_curves_setting.emit()

    # 曲线通道选择模块初始化
    def init_channels_selecter(self):
        self.channel_labels = ['Ⅰ', 'Ⅱ', 'Ⅲ', 'V1', 'V2' ,'V3', 'V4', 'V5', 'V6', 'Avr', 'aVL', 'aVF']
        # 通道选择表格
        table = self.tableWidget_channels
        row_num=2
        col_num=6
        table.setRowCount(row_num) # 设置行数
        table.setColumnCount(col_num) # 设置列数
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setVisible(False)
        table.itemSelectionChanged.connect(self.onSelectionChanged_table)
        idx = 0
        for row in range(0, 2):
            self.tableWidget_channels.setRowHeight(row,44)
            for col in range(0, 6):
                if idx < 12:
                    text = self.channel_labels[idx]  # 写入内容（字符串）
                    newItem = QTableWidgetItem(text)
                    self.tableWidget_channels.setItem(row, col, newItem) #
                    self.tableWidget_channels.setColumnWidth(col,49)
                idx += 1

    # 通道表格选中回调函数
    def onSelectionChanged_table(self):
        self.channels_to_show_idx = []
        idx = 0
        for row in range(0, 2):
            for col in range(0, 6):
                if idx < 12:
                    if self.tableWidget_channels.item(row, col) in self.tableWidget_channels.selectedItems():
                        self.channels_to_show_idx.append(idx)
                    idx += 1
        self.trig_curves_channelsSelected.emit(self.channels_to_show_idx)

    # 保存数据回调函数
    def saveData_ss_callback(self):
        if self.saveData_state is False:
            self.saveData_state = True
            self.pushButton_saveData_ss.setText('保存中...')
            self.trig_saveData_ss.emit(self.saveData_state)
        else:
            self.saveData_state = False
            self.pushButton_saveData_ss.setText('开始保存')
            self.trig_saveData_ss.emit(self.saveData_state)

    # 保存报告回调函数
    def report_callback(self):
        try:
            initial_path = r'E:\\'
            filename = QFileDialog.getSaveFileName(self, 'save file', initial_path)
        except:
            QMessageBox.critical(self, "错误", "选择文件夹无效！请重新选择！")

        if len(filename[0]) == 0:  # 如果打开文件选择器后取消，退出调用程序
            return
        savePath = filename[0]
        if savePath[-3:] != '.jpg':
            savePath += '.jpg'
        self.trig_report.emit(savePath)

    # TFT窗口折叠回调函数
    def fold_TFT_callback(self):
        if self.Is_showTFT is False:
            self.Is_showTFT = True
            self.groupBox_TFT.setVisible(True)
        else:
            self.Is_showTFT = False
            self.groupBox_TFT.setVisible(False)

    # 提示弹窗
    def show_mesg_box(self, imf):
        QMessageBox.information(self,
                                        "提示",
                                        imf,
                                        )


## 主函数
if __name__ == '__main__':
    from qt_material import apply_stylesheet
    import sys
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
