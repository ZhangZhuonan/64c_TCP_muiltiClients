import copy
import os
import time

import cv2
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import  QPushButton
import sys
import numpy as np
import pyqtgraph as pg
from my_lib.settings_tool import get_param4json_file
path = 'configuration\curves_params.json'


class FFT_Curves():
    def __init__(self, parent=None):
        self.last_time = 0
        self.last_idx = 0
        self.Is_continue = False
        self.init_curves_widget()

    # 初始化曲线窗口
    def init_curves_widget(self):
        self.plot_widget = pg.GraphicsLayoutWidget()
        self.plot_widget.setBackground('#31363b')
        self.main_plot_handler = self.plot_widget.addPlot()
        self.main_plot_handler.setMouseEnabled(x=False, y=False)

        # 初始化绘图参数
        self.eeg_channels = 12  # 通道数
        self.strem_rate =  get_param4json_file(path, 0)     # 传输速率
        self.stop_plot = False
        self.scales_range = [
            1, 10, 25, 50, 100, 250, 500, 1000, 2500, 10000, 50000, 75000]
        self.colors = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0], [0, 255, 255], [255, 0, 255],
                                [128, 100, 100], [0, 128, 0], [0, 128, 128], [128, 128, 0], [255, 128, 128], [128, 0, 128],
                                [128, 255, 0], [255, 128, 0], [0, 255, 128], [128, 0, 255]])
        init_idx = 7
        self.scale = self.scales_range[init_idx]
        # 加载初始设置
        self.seconds_to_show = 1
        self.channels_to_show_idx = np.arange(0, self.eeg_channels)
        self.channel_labels = ['Ⅰ', 'Ⅱ', 'Ⅲ', 'V1', 'V2' ,'V3', 'V4', 'V5', 'V6', 'Avr', 'aVL', 'aVF'] #[ V4 V5 V6 Avr aVL aVF']
        values = []
        for x in range(0, len(self.channels_to_show_idx)):
            values.append((-x * self.scale, self.channel_labels[self.channels_to_show_idx[x]]))
        values_axis = []
        values_axis.append(values)
        values_axis.append([])
        self.main_plot_handler.getAxis('left').setTicks(values_axis)
        self.main_plot_handler.setRange(xRange=[0, self.strem_rate / 2], yRange=[1.5 * self.scale, -0.5 * self.scale - self.scale * self.eeg_channels])
        self.main_plot_handler.disableAutoRange()
        self.main_plot_handler.showGrid(y=True)
        self.main_plot_handler.setLabel(axis='left', text=('Scale (mV): ' + str(self.scale / 1000)))
        self.main_plot_handler.setLabel(axis='bottom', text='Freq (Hz)')
        self.x_ticks = np.zeros(self.strem_rate * self.seconds_to_show)
        for x in range(0, self.strem_rate * self.seconds_to_show):
            self.x_ticks[x] = x * 1 / float(self.strem_rate)
        self.subsampling_value = self.strem_rate / 5120
        self.data_plot = np.zeros((self.strem_rate * self.seconds_to_show, self.eeg_channels))
        self.data_plot_copy = np.zeros((self.strem_rate * self.seconds_to_show, self.eeg_channels))
        self.curve_eeg = []
        for x in range(0, len(self.channels_to_show_idx)):
            self.curve_eeg.append(self.main_plot_handler.plot(x=(self.x_ticks),
                                                              y=(self.data_plot[:, self.channels_to_show_idx[x]]),
                                                              pen=(pg.mkColor(self.colors[1, :]))))
                                                              # pen=(pg.mkColor(self.colors[self.channels_to_show_idx[x] % 16, :]))))

    def updata(self, x_freq, FFT_amp_half_list):
        if x_freq is not None:
            for x in range(0, len(self.channels_to_show_idx)):
                self.curve_eeg[x].setData(x=x_freq,y=(self.auto_range(FFT_amp_half_list[self.channels_to_show_idx[x]])
                                                      - x * self.scale))

    def auto_range(self, y_data):
        max_val = np.nanmax(y_data)
        scale_k = self.scale / max_val
        return y_data * scale_k


    def repaint(self):
        pass

    def update_plot_scale(self, new_scale):
        if new_scale < 1:
            new_scale = 1
        self.scale = new_scale
        values = []
        for x in range(0, len(self.channels_to_show_idx)):
            values.append((-x * self.scale, self.channel_labels[self.channels_to_show_idx[x]]))
        values_axis = []
        values_axis.append(values)
        values_axis.append([])
        self.main_plot_handler.getAxis('left').setTicks(values_axis)
        self.main_plot_handler.setRange(yRange=[+self.scale, -self.scale * len(self.channels_to_show_idx)])
        self.main_plot_handler.setLabel(axis='left', text=('Scale (mV): ' + str(self.scale / 1000)))
        if not self.stop_plot:
            self.repaint()

    def update_plot_seconds(self, new_seconds):
        if new_seconds != self.seconds_to_show:
            # self.spinBox_time.setValue(new_seconds)
            self.main_plot_handler.setRange(xRange=[0, new_seconds])
            self.x_ticks = np.zeros(self.strem_rate * new_seconds)
            for x in range(0, self.strem_rate * new_seconds):
                self.x_ticks[x] = x * 1 / float(self.strem_rate)
            if new_seconds > self.seconds_to_show:
                padded_signal = np.zeros((self.strem_rate * new_seconds, self.eeg_channels))
                padded_signal[padded_signal.shape[0] - self.data_plot.shape[0]:, :] = self.data_plot
                self.data_plot = padded_signal
            else:
                self.data_plot = self.data_plot[self.data_plot.shape[0] - self.strem_rate * new_seconds:, :]
            self.seconds_to_show = new_seconds
            if not self.stop_plot:
                self.repaint()

    def onSelectionChanged_table(self, channels_to_show_idx):
        for x in range(0, len(self.channels_to_show_idx)):
            self.main_plot_handler.removeItem(self.curve_eeg[x])


        self.channels_to_show_idx = channels_to_show_idx
        self.channels_to_hide_idx = []

        self.curve_eeg = []

        for x in range(0, len(self.channels_to_show_idx)):
            self.curve_eeg.append(self.main_plot_handler.plot(x=(self.x_ticks),
                                                              y=(self.data_plot[:, self.channels_to_show_idx[x]]),
                                                              pen=(self.colors[1, :])))
            self.curve_eeg[(-1)].setDownsampling(ds=(self.subsampling_value), auto=False, method='mean')
        self.update_plot_scale(self.scale)




class Show_Widget(QWidget):
    def __init__(self, my_widget):
        super(Show_Widget, self).__init__()
        self.strem_rate = 500
        self.seconds_to_show = 5
        self.eeg_channels = 6
        Xaxis_length = self.strem_rate * self.seconds_to_show
        self.curve_widget = my_widget
        self.initUI(my_widget.plot_widget)
        self.initTimer()

    ## =====初始化界面=====
    def initUI(self, my_widget):
        conLayout = QHBoxLayout()
        conLayout.addWidget(my_widget)
        self.setLayout(conLayout)

    def initTimer(self):
        self.time_now = 0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_loop)
        self.timer.start(1)

    def update_loop(self):
        self.data_plot = np.ones((10, self.eeg_channels)) * np.sin(0.1 * self.time_now) * 500
        self.time_now += 1
        if self.time_now == 1000:
            self.time_now = 0
        self. curve_widget.updata(self.data_plot)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    curves_widget = Curves_Widget()
    myWin = Show_Widget(curves_widget)
    myWin.show()
    sys.exit(app.exec_())

