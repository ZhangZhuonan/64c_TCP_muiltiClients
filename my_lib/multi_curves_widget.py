from my_lib.curves_widget import *

class My_Widget(QWidget):
    def __init__(self, my_widget):
        super(My_Widget, self).__init__()
        self.conLayout = QHBoxLayout()
        self.conLayout.addWidget(my_widget)
        self.setLayout(self.conLayout)

class MuiltiCurves_Widget(QWidget):
    def __init__(self):
        super(MuiltiCurves_Widget, self).__init__()
        self.eeg_channels = 12
        self.initUI()
    # 初始化界面
    def initUI(self):
        self.curves1 = Curves_Widget()
        self.curves2 = Curves_Widget()
        self.curves1.channel_labels = ['Ⅰ', 'Ⅱ', 'Ⅲ', 'V1', 'V2' ,'V3']
        self.curves2.channel_labels = ['V4', 'V5', 'V6', 'Avr', 'aVL', 'aVF']
        self.curves1.update_plot_scale(1000)
        self.curves2.update_plot_scale(1000)
        self.curves1_widget = My_Widget(self.curves1.plot_widget)
        self.curves2_widget = My_Widget(self.curves2.plot_widget)
        self.conLayout = QHBoxLayout()
        self.conLayout.addWidget(self.curves1_widget)
        self.conLayout.addWidget(self.curves2_widget)
        self.setLayout(self.conLayout)

    # 初始化定时器（内部测试）
    def initTimer(self):
        self.time_now = 0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_loop)
        self.timer.start(1)

    # 定时器响应执行函数（内部测试）
    def update_loop(self):
        shift = 0
        if self.time_now > 500:
            shift = 10
        self.data_plot = np.ones((10, self.eeg_channels)) * np.sin(0.1 * self.time_now + shift) * 500
        self.time_now += 1
        if self.time_now == 1000:
            self.time_now = 0
        self.updata(self.data_plot)

    # 更新显示秒数
    def update_plot_seconds(self, new_seconds):
        self.curves1.update_plot_seconds(new_seconds)
        self.curves2.update_plot_seconds(new_seconds)

    def updata_strem_rate(self, val):
        self.curves1.strem_rate = val
        self.curves2.strem_rate = val

    def updata_Yscale(self, val):
        self.curves1.Yscale = val
        self.curves2.Yscale = val

    # 更新选中显示曲线
    def onSelectionChanged(self, c12_idx_list):
        # 将12通道曲线拆分到两个子窗口中
        c12_idx_arr = np.array(c12_idx_list)
        channels_to_show_idx_1 = c12_idx_arr[np.where(c12_idx_arr < 6)]
        channels_to_show_idx_2 = c12_idx_arr[np.where(c12_idx_arr >= 6)] - 6
        # 若子曲线窗口没有显示曲线，则隐藏该窗口
        if len(channels_to_show_idx_1) == 0:
            self.curves1_widget.setVisible(False)
        else:
            self.curves1_widget.setVisible(True)
        if len(channels_to_show_idx_2) == 0:
            self.curves2_widget.setVisible(False)
        else:
            self.curves2_widget.setVisible(True)
        # 更新子曲线窗口选中所选曲线
        self.curves1.onSelectionChanged_table(list(channels_to_show_idx_1))
        self.curves2.onSelectionChanged_table(list(channels_to_show_idx_2))

    # 更新曲线绘图数据
    def updata(self, updata_plotData):
        updata_plotData1 = updata_plotData[:, 0: 6]
        updata_plotData2 = updata_plotData[:, 6: 12]
        self.curves1.updata(updata_plotData1)
        self.curves2.updata(updata_plotData2)

    # 获取当前绘图数据
    def get_plotDtat(self):
        plot1 = self.curves1.data_plot
        plot2 = self.curves2.data_plot
        return plot1, plot2




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myWin = MuiltiCurves_Widget()
    myWin.show()
    sys.exit(app.exec_())
