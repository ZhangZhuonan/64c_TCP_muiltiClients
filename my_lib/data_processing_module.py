import numpy as np
import time
import csv
from scipy.signal import butter, lfilter, lfiltic, buttord, medfilt
from my_lib.settings_tool import *
path = 'configuration\curves_params.json'

class Data_Processing_Module():
    def __init__(self):
        self.init_params()

    # 初始化参数
    def init_params(self):
        self.channels = 64                                  # 通道数据不包括时间戳
        self.strem_rate =  get_param4json_file(path, 0)     # 传输速率
        self.Is_medianFilt = get_param4json_file(path, 2)   # 是否进行中值滤波
        self.low_pass = get_param4json_file(path, 3)        # 低通截止频率
        self.high_pass = get_param4json_file(path, 4)       # 高通截止频率
        self.Is_bandFilt = get_param4json_file(path, 5)     # 带通滤波
        self.Is__50Hz_notch = get_param4json_file(path, 6)  # 抗工频干扰
        self.init_band_filter()
        self.Is_saveData = False        # 是否保存数据

    # 开始保存数据
    def start_saveData(self):
        self.file = open('data/'+time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())+'.csv','w',newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.file)
        self.Is_saveData = True

    # 停止保存数据
    def stop_saveData(self):
        self.Is_saveData = False
        self.file.close()

    # 对解包的原始数据进行拆分、组合、滤波、计算附加数据、保存
    def analyze(self, data):
        '''
        数据分析
        :param data: [[时间戳，通道1，通道1，...,通道64],[...],[...]...]n行10列的数据矩阵
        :return:
        '''
        plotData = data[:, 1:]
        # 滤波计算
        plotData_12c = self.filter(plotData)
        # 保存数据
        if self.Is_saveData:
            transformed_data = list(map(list, zip(*np.c_[data[:, 0],plotData_12c])))
            untransformed_data = list(map(list, zip(*transformed_data)))
            self.csv_writer.writerows(untransformed_data)
        return plotData_12c

    # 进行频谱分析，返回频谱、心率
    def FFT_calc(self, plotData):
        channels = plotData.shape[1]
        FFT_amp_half_list = []
        N = plotData.shape[0]
        x_freq = self.strem_rate * np.arange(0, int(N / 2)) / N
        for i in range(channels):
            y_data = plotData[:, i]
            y_fft = np.fft.fft(y_data)
            y_fft_amp = np.abs(y_fft) / N * 2
            y_fft_amp_half = (y_fft_amp[0:int(N / 2)])
            FFT_amp_half_list.append(y_fft_amp_half)

        return  FFT_amp_half_list, x_freq

    # 滤波
    def filter(self, plotData):
        for c in range(self.channels):
            good_idx = np.where(plotData[:, c]!=0)
            # 中值滤波
            if self.Is_medianFilt:
                plotData[:, c] = medfilt(plotData[:, c][np.where(plotData[:, c])], 3)
            # 带通滤波
            if self.Is_bandFilt:
                plotData[:, c][good_idx], self.zi[:, c] = lfilter(self.b, self.a, plotData[:, c][good_idx], -1, self.zi[:, c])
            # 抗工频干扰
            if self.Is__50Hz_notch:
                plotData[:, c], self.zi_notch[:, c] = lfilter(self.b_notch, self.a_notch, plotData[:, c],
                                                              -1, self.zi_notch[:, c])
        return plotData

    def init_band_filter(self):
        if self.high_pass > self.strem_rate/2:
            self.high_pass = int(self.strem_rate/2)-1
        self.b, self.a, self.zi = self.butter_bandpass(self.low_pass, self.high_pass, self.strem_rate, self.channels)
        self.b_notch, self.a_notch, self.zi_notch = self.butter_bandstop(48, 52, self.strem_rate, self.channels)

    def butter_bandpass(self, highcut, lowcut, fs, num_ch):
        low = lowcut / (0.5 * fs)
        high = highcut / (0.5 * fs)
        ord = buttord(high, low, 2, 40)
        b, a = butter(1, [high, low], btype='bandpass')
        zi = np.zeros([a.shape[0] - 1, num_ch])
        return (
            b, a, zi)

    def butter_bandstop(self, highcut, lowcut, fs, num_ch):
        low = lowcut / (0.5 * fs)
        high = highcut / (0.5 * fs)
        b, a = butter(2, [high, low], btype='bandstop')
        zi = np.zeros([a.shape[0] - 1, num_ch])
        return (
            b, a, zi)

    def butter_lowpass(self, cut, fs, num_ch):
        cut_ = cut / (0.5 * fs)
        b, a = butter(2, cut_, btype='lowpass')
        zi = np.zeros([a.shape[0] - 1, num_ch])
        return (
            b, a, zi)


