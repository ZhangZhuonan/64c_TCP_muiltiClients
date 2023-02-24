from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage,QPixmap
from my_lib.extern_widget_UI import Ui_extern_widget
from my_lib.btn_img_widget import Btn_Img_Widget
import sys
import numpy as np
import pyqtgraph as pg

class Extern_Widget(QtWidgets.QWidget, Ui_extern_widget):
    def __init__(self):
        super(Extern_Widget, self).__init__()

        self.setupUi(self)
        self.ui_init()

    def ui_init(self):
        self.init_fft_curves()
        self.btn_img_widg = Btn_Img_Widget()
        self.Is_show_btnWidg = False
        self.pushButton_show.clicked.connect(self.show_btn_img_Widg)

    def init_fft_curves(self):
        self.plot_widget = pg.GraphicsLayoutWidget()
        self.plot_widget.setBackground('#ecf4eb')
        self.main_plot_handler = self.plot_widget.addPlot()
        self.main_plot_handler.setMouseEnabled(x=False, y=False)
        self.verticalLayout_FFT.addWidget(self.plot_widget)

        # 初始化绘图参数
        self.eeg_channels = 64  # 通道数
        self.strem_rate = 1000  # 每秒采样率
        self.stop_plot = False
        self.apply_notch = True
        self.apply_bandpass = True
        self.scales_range = [
            1, 10, 25, 50, 100, 250, 500, 1000, 2500, 10000, 50000, 75000]
        self.colors = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [0, 255, 255], [255, 0, 255],
                                [128, 100, 100], [0, 128, 0], [0, 128, 128], [128, 128, 0], [255, 128, 128],
                                [128, 0, 128],
                                [128, 255, 0], [255, 128, 0], [0, 255, 128], [128, 0, 255]])

        init_idx = 4
        self.scale = self.scales_range[init_idx]
        self.channel_labels = []
        values = []
        for x in range(0, self.eeg_channels):
            self.channel_labels.append('CH%02d' % (x + 1))
        for x in range(0, self.eeg_channels):
            values.append((-x * self.scale, self.channel_labels[x]))
        values_axis = []
        values_axis.append(values)
        values_axis.append([])
        idx = 0


        self.main_plot_handler.getAxis('left').setTicks(values_axis)
        self.main_plot_handler.setRange(xRange=[0, int(self.strem_rate/2)],
                                        yRange=[1.5 * self.scale, -0.5 * self.scale - self.scale * self.eeg_channels])
        self.main_plot_handler.disableAutoRange()
        self.main_plot_handler.showGrid(y=True)
        # self.main_plot_handler.setLabel(axis='left', text=('Scale (uV): ' + str(self.scale)))
        self.main_plot_handler.setLabel(axis='bottom', text='Hz')

        self.subsampling_value = self.strem_rate / 128


        self.curve_eeg = []
        for x in range(0, self.eeg_channels):
            self.curve_eeg.append(self.main_plot_handler.plot(pen=(pg.mkColor(self.colors[x % 16, :]))))


    def show_btn_img_Widg(self):
        if self.Is_show_btnWidg is False:
            self.btn_img_widg = Btn_Img_Widget()
            self.verticalLayout_btn_img.addWidget(self.btn_img_widg)
            self.btn_img_widg.show()
            self.Is_show_btnWidg = True
            # self.pushButton_show.setText('折叠')
        else:
            for i in range(self.verticalLayout_btn_img.count()):
                self.verticalLayout_btn_img.itemAt(i).widget().deleteLater()
            self.Is_show_btnWidg = False
            # self.pushButton_show.setText('展开')







if __name__ == '__main__':
    app = QApplication(sys.argv)
    widg = Extern_Widget()
    widg.show()
    sys.exit(app.exec_())