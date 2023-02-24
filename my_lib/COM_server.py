# -*- coding: utf-8 -*-
import serial
import threading
import time
from my_lib.data_stream import *
from my_lib.FSM import *
from my_lib.stopThreading import stop_thread


class Com_Server():
    def __init__(self, data_stream):
        super(Com_Server, self).__init__()
        self.data_stream = data_stream  # 数据流类
        self.serial = serial.Serial()   # 串口类
        self.Is_init = False            # 串口初始化成功标志位

    # 打开串口函数
    def open(self, comPort, byteRate, byteSize, stopBits, parity):
        ser = self.serial
        ser.port = comPort
        ser.baudrate = byteRate
        ser.bytesize = byteSize
        ser.stopbits = stopBits
        ser.parity = parity
        try:
            ser.close()         # 测试串口是否能打开
            ser.open()
        except:                 # 若出现无法打开的串口
            print('%s打开失败！'%comPort)
            return
        else:
            if ser.isOpen():
                self.Is_init = True
                print('成功打开%s！'%comPort)
        # 初始化状态机
        self.FSM = FSM(self.data_stream)
        # 开启串口监听线程
        self.serve_th = threading.Thread(target=self.com_client_concurrency)
        self.serve_th.setDaemon(True)
        self.serve_th.start()

    # 串口监听线程执行函数
    def com_client_concurrency(self):
        while True:
            num = self.serial.inWaiting()           # 获取当前等待解读数据位数
            if num >= 8:
                data = self.serial.read(int(num))
                self.FSM.receive_fsm(data)          # 交给解包状态机进行解包，并将解包数据推送给数据流类
            time.sleep(0.005)                       # 等待串口接受数据

    # 串口关闭函数
    def close(self):
        try:
            # 关闭串口
            self.serial.close()
            self.Is_init = False
            print('COM closed...')
        except Exception as ret:
            pass
        try:
            stop_thread(self.serve_th)              # 强行结束串口监听线程
        except Exception as ret:
            pass

if __name__ == '__main__':
    import time
    # 参数设置
    comPort = 'COM1'
    byteRate = 460800
    byteSize =  8
    stopBits = 1
    parity = 'N'    # ['N','E','O']

    ds = Data_Stream()
    com = Com_Server(ds)
    com.open(comPort, byteRate, byteSize, stopBits, parity)
    time.sleep(1000)


