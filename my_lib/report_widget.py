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
import pyqtgraph.exporters
import shutil
from my_lib.settings_tool import get_param4json_file
path = 'configuration\curves_params.json'



class Curves_Widget4report():
    def __init__(self, parent=None):
        self.last_time = 0
        self.last_idx = 0
        self.Is_continue = False
        self.init_curves_widget()

    # 初始化曲线窗口
    def init_curves_widget(self):
        self.plot_widget = pg.GraphicsLayoutWidget()
        self.plot_widget.setBackground('#FDEDEC')
        self.main_plot_handler = self.plot_widget.addPlot()
        self.main_plot_handler.setMouseEnabled(x=False, y=False)

        self.grid_item = pg.GridItem(textPen=None)
        self.grid_item.setPen(color=(0,0,0), width=1)
        self.grid_item.setTickSpacing(x=[0.1], y=[100])
        self.main_plot_handler.addItem(self.grid_item)

        # 初始化绘图参数
        self.eeg_channels = 12  # 通道数
        self.strem_rate =  get_param4json_file(path, 0)     # 传输速率
        self.stop_plot = False
        self.scales_range = [
            1, 10, 25, 50, 100, 250, 500, 1000, 2500, 10000, 50000, 75000]
        self.colors = np.array([[255, 0, 0], [0, 0, 0], [0, 0, 255], [255, 255, 0], [0, 255, 255], [255, 0, 255],
                                [128, 100, 100], [0, 128, 0], [0, 128, 128], [128, 128, 0], [255, 128, 128], [128, 0, 128],
                                [128, 255, 0], [255, 128, 0], [0, 255, 128], [128, 0, 255]])
        init_idx = 7
        self.scale = self.scales_range[init_idx]
        # 加载初始设置
        self.seconds_to_show = get_param4json_file(path, 1)
        self.channels_to_show_idx = np.arange(0, self.eeg_channels)
        self.channel_labels = ['Ⅰ', 'Ⅱ', 'Ⅲ', 'V1', 'V2' ,'V3', 'V4', 'V5', 'V6', 'Avr', 'aVL', 'aVF'] #[ V4 V5 V6 Avr aVL aVF']
        values = []
        for x in range(0, len(self.channels_to_show_idx)):
            values.append((-x * self.scale, self.channel_labels[self.channels_to_show_idx[x]]))
        values_axis = []
        values_axis.append(values)
        values_axis.append([])
        self.main_plot_handler.getAxis('left').setTicks(values_axis)
        self.main_plot_handler.setRange(xRange=[0, self.seconds_to_show], yRange=[1.5 * self.scale, -0.5 * self.scale - self.scale * self.eeg_channels])
        self.main_plot_handler.disableAutoRange()
        self.main_plot_handler.showGrid(x=True, y=True)
        self.main_plot_handler.setLabel(axis='left', text=('Scale (mV): ' + str(self.scale / 1000)))
        self.main_plot_handler.setLabel(axis='bottom', text='Time (s)')
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

    def updata(self, updata_plotData):
        self.seconds_to_show = get_param4json_file(path, 1)
        self.Yscale = get_param4json_file(path, 7)          # 纵向缩放
        if updata_plotData is not None:
            for x in range(0, len(self.channels_to_show_idx)):
                y_data = updata_plotData[:, self.channels_to_show_idx[x]]
                y_shift = np.mean(y_data)
                y_data = y_data - y_shift
                self.curve_eeg[x].setData(x=(self.x_ticks), y=(y_data * self.Yscale- x * self.scale))





class Report_Widget(QWidget):
    def __init__(self):
        super(Report_Widget, self).__init__()
        self.curve_widget = Curves_Widget4report()
        self.initUI(self.curve_widget.plot_widget)
        self.timer_init()


    ## =====初始化界面=====
    def initUI(self, my_widget):
        self.resize(1920,1080)
        self.setStyleSheet("QWidget{background:#FDEDEC;\n"
                           "}")
        conLayout = QHBoxLayout()
        conLayout.addWidget(my_widget)
        self.setLayout(conLayout)

    def draw(self, plotData):
        self.curve_widget.updata(plotData)

    def timer_init(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.wait4report)
        self.count = 0

    def wait4report(self):
        print(self.count)
        if self.count == 2:
            self.outPut_report()
            self.timer.stop()
            self.count = 0
            self.close()
        self.count += 1

    def start_saveReport(self, plotData, savePath):
        self.draw(plotData)
        self.show()
        self.timer.start(1000)
        self.savePath = savePath

    def outPut_report(self):
        screen = QApplication.primaryScreen()
        img = screen.grabWindow(self.winId())
        img.save(r'data\report.jpg')
        try:
            shutil.copy(r'data\report.jpg', self.savePath)
        except:
            pass



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    curves_widget = Report_Widget()
    curves_widget.show()

    sys.exit(app.exec_())
