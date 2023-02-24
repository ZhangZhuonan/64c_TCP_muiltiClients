# -*- coding: utf-8 -*-
from my_lib.COM_server import *
from my_lib.TCP_server import *
from my_lib.settings_tool import *
path = 'configuration\data_acquisition_params.json'

class Data_Acquisition():
    def __init__(self):
        self.data_stream = Data_Stream()
        self.com = Com_Server(self.data_stream)
        self.tcp = TCP_Server(self.data_stream)
        self.COM_working = False
        self.TCP_working = False
        self.Is_working = False
        pass

    # 打开串口通道（可直接打开，不用提前关闭）
    def open_COM(self):
        self.close()
        comPort = get_param4json_file(path, 0)
        byteRate = get_param4json_file(path, 1)
        byteSize = get_param4json_file(path, 2)
        stopBits = get_param4json_file(path, 3)
        parity = get_param4json_file(path, 4)
        try:
            self.com.open(comPort, byteRate, byteSize, stopBits, parity)
        except:
            pass
        self.COM_working = self.com.Is_init
        return self.com.Is_init

    # 打开网络通道（可直接打开，不用提前关闭）
    def open_TCP(self):
        self.close()
        ip = get_param4json_file(path, 5)
        port = get_param4json_file(path, 6)
        try:
            self.tcp.open(ip, port)
        except:
            pass
        self.TCP_working = self.tcp.Is_init
        return self.tcp.Is_init

    # 关闭通道
    def close(self):
        if self.COM_working is True:
            self.com.close()
        if self.TCP_working is True:
            self.tcp.close()

    # 获取缓存数据
    def get_receiveData(self):
        return self.data_stream.acquire()

if __name__ == '__main__':
    da = Data_Acquisition()
    da.open_COM()
    time.sleep(1000)