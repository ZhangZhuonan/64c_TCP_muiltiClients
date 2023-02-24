import numpy as np

from my_lib.data_acquisition_module import *
from my_lib.data_processing_module import *
from my_lib.multi_curves_widget import *
from my_lib.curvesFFT_widget import FFT_Curves
from my_lib.settings_widget import *
from my_lib.main_window import *
from my_lib.report_widget import Report_Widget

curves_settingPath = r'configuration\curves_params.json'
link_settingPath = r'configuration\data_acquisition_params.json'

class Main_Widget(MyWindow):
    def __init__(self):
        super(Main_Widget, self).__init__()
        self.refreshheart_count = 0
        self.loadModule()
        self.trig_receiver()
        self.initTimer()


    # 加载模块
    def loadModule(self):
        self.acquisition = Data_Acquisition()       # 数据获取模块
        self.prossesing = Data_Processing_Module()  # 数据处理模块
        self.curves_widget = MuiltiCurves_Widget()  # 多曲线窗口
        self.verticalLayout_curves.addWidget(self.curves_widget)
        self.FFT_obj = FFT_Curves()                 # FFT频谱绘制模块
        self.FFT_widget = self.FFT_obj.plot_widget  # FFT频谱显示窗口
        self.verticalLayout_FFT.addWidget(self.FFT_widget)
        self.linkSet_widget = Settings_Widget()     # 连接设置窗口
        self.report_widget = Report_Widget()        # 报告窗口

    # 各模块信号传入控制器
    def trig_receiver(self):
        self.trig_link_ss.connect(self.control_link_ss)                 # 连接建立-关闭信号
        self.trig_link_setting.connect(self.control_link_setting)       # 连接设置信号
        self.trig_curves_ss.connect(self.control_curves_ss)             # 曲线绘制开始-结束信号
        self.trig_curves_setting.connect(self.control_curves_setting)   # 曲线绘图设置信号
        self.trig_curves_channelsSelected.connect(self.control_curves_channelsTable)    # 曲线通道改变信号
        self.trig_saveData_ss.connect(self.control_saveData_ss)         # 保存数据开始-结束信号
        self.trig_report.connect(self.control_report)                   # 输出报告

    # ==模型信号接收处理函数

    # 通信连接开始-结束信号
    def control_link_ss(self, link_mode, link_state):
        if link_state == True:          # 尝试建立连接
            if link_mode == 'COM':      # 建立COM连接
                Is_open = self.acquisition.open_COM()
            else:
                Is_open = self.acquisition.open_TCP()
            if Is_open is False:        # 连接失败
                self.link_false_callback()  # 向主窗口反馈连接失败信号
                self.show_mesg_box('连接失败，请检查设置！')
        else:                           # 关闭连接
            self.acquisition.close()

    # 打开通信设置菜单信号
    def control_link_setting(self):
        calc_dict = load_json_file(link_settingPath)
        self.linkSet_widget.table_init(calc_dict)
        self.linkSet_widget.show()

    # 曲线绘制开始-结束信号
    def control_curves_ss(self, curves_continue):
        if curves_continue is True:
            second2show = get_param4json_file(curves_settingPath, 1)
            simple_rate = get_param4json_file(curves_settingPath, 0)
            Yscale = get_param4json_file(curves_settingPath, 7)
            self.curves_widget.update_plot_seconds(second2show)
            self.curves_widget.updata_strem_rate(simple_rate)
            self.curves_widget.updata_Yscale(Yscale)
            self.prossesing.init_params()
            self.timer.start(10)
        else:
            self.timer.stop()

    # 打开曲线设置信号菜单信号
    def control_curves_setting(self):
        calc_dict = load_json_file(curves_settingPath)
        self.linkSet_widget.table_init(calc_dict)
        self.linkSet_widget.show()

    # 曲线显示通道变更信号
    def control_curves_channelsTable(self, channels2show_idxList):
        self.curves_widget.onSelectionChanged(channels2show_idxList)
        self.FFT_obj.onSelectionChanged_table(channels2show_idxList)

    # 保存数据开始-结束信号
    def control_saveData_ss(self, state):
        if state == True:   # 开始保存数据
            self.prossesing.start_saveData()
        else:
            self.prossesing.stop_saveData()

    # 输出报告信号
    def control_report(self, savePath):
        if len(savePath) > 3:
            plotData1, plotData2 = self.curves_widget.get_plotDtat()
            try:
                self.report_widget.start_saveReport(np.c_[plotData1, plotData2], savePath)
            except:
                self.show_mesg_box('报告生成失败！')
            else:
                self.show_mesg_box('报告保存成功！')

    # ==周期性刷图处理部分

    # 初始化绘图定时器
    def initTimer(self):
        self.time_now = 0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_loop)

    # 绘图定时器回调函数，在此获取、处理、绘制显示数据
    def update_loop(self):
        rawData = self.acquisition.get_receiveData()        # 尝试从数据获取模块获取缓存池数据
        if rawData is not None:                             # 判断是否有数据
            plotData = \
                self.prossesing.analyze(rawData)            # 对数据进行处理
            self.curves_widget.updata(plotData)             # 更新绘图数据
            if self.refreshheart_count == 5:
                self.refreshheart_count = 0
                plotData1, plotData2 = self.curves_widget.get_plotDtat()
                FFT_amp_half_list, x_freq, heart_beat = self.prossesing.FFT_calc(np.c_[plotData1, plotData2])
                self.FFT_obj.updata(x_freq, FFT_amp_half_list)     # 更新频谱数据
                self.lcdNumber_heart.display(int(heart_beat))
            self.refreshheart_count += 1


if __name__ == '__main__':
    from qt_material import apply_stylesheet
    import sys
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    myWin = Main_Widget()
    myWin.show()
    sys.exit(app.exec_())