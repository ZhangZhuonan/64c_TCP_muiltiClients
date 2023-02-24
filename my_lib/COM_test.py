# from udp_Logic import *
import serial
import threading
from my_lib.stopThreading import *
from PyQt5.QtCore import pyqtSignal
import time
import numpy as np

from my_lib.data_stream import *

LSB =  0.5364  # 权值
gain = 24      # 增益

class Com_Serve():
    sig_receive_data = pyqtSignal([int])
    def __init__(self, data_stream):
        super(Com_Serve, self).__init__()
        self.data_stream = data_stream
        self.serials = [serial.Serial(), serial.Serial(), serial.Serial(), serial.Serial()]
        # 绘图数据包
        self.channels = 4
        self.pull_dataArr = np.zeros([1, self.channels])
        # 初始化状态机参数
        self.receive_status = 0  # 接收状态标志位
        self.receive_data = []   # 接收数据
        self.receive_cnt = 0     # 接收数据计数
        self.receive_len = 4     # 接收数据个数
        self.cnt_ = 0

    def com_open(self, comPort_list, byteRate):
        """
        功能函数，UDPClient开启的方法
        :return: None
        """

        self.working = True
        for i, com  in enumerate(comPort_list):
            ser = self.serials[i]
            ser.port = com
            ser.baudrate = byteRate
            ser.bytesize = 8
            ser.stopbits = 1
            ser.parity = 'E'
            try:
                ser.close()         # 测试串口是否能打开
                ser.open()
            except:                 # 若出现无法打开的串口
                print('%s打开失败！'%com)
                try:
                    for ser in self.serials:
                        ser.close() # 关闭所有串口
                except:
                    pass
                return
            else:
                if ser.isOpen():
                    print('成功打开%s！'%com)
        self.serve_th = threading.Thread(target=self.com_client_concurrency)
        self.serve_th.setDaemon(True)
        self.serve_th.start()
        self.link = True

    def com_client_concurrency(self):
        """
        创建新线程以供UDPClient持续监听Server的消息
        :return:
        """
        while True:
            if self.working == True:
                np.random.random([4])
                y = np.cos(0.1*self.receive_cnt)
                y2 = np.sin(0.01*self.receive_cnt)
                y = np.uint8(y * 10)
                y2 = np.uint8(y2*10)
                self.receive_cnt += 1
                for ser in self.serials:
                    ser.write(bytes([0XFC, y, y, y, y2, y,y, y, y]))
                time.sleep(0.001)

    def socket_close_u(self):
        '''
        关闭udpsocket以及其相关线程
        :return:
        '''
        try:
            self.working = False
            self.ser.close()
            print('COM closed...')

        except Exception as ret:
            pass
        try:
            stop_thread(self.serve_th)
        except Exception as ret:
            pass

    # 接收状态机
    def receive_fsm(self, data):
        for d in data:
            # 0 -- 同步头1
            if self.receive_status == 0:

                if d == 0xFA:
                    self.receive_status = 1

            # 4 -- 数据域
            elif self.receive_status == 1:
                if self.receive_cnt >= self.receive_len - 1:
                    self.receive_data.append(d)
                    self.receive_status = 2
                else:
                    self.receive_data.append(d)
                    self.receive_cnt += 1

            # 5 -- 校验字1
            elif self.receive_status == 2:
                if d == 0xAF:
                    self.cmd_execute(self.receive_data)
                self.receive_status = 0  # 接收状态标志位
                self.receive_data = []   # 接收数据
                self.receive_cnt = 0     # 接收数据计数
                self.receive_len = 4     # 接收数据个数

    def cmd_execute(self, data):
        data_len = 1          # 数据字节数
        data_num = int(len(data) / data_len)  # 数据总数
        self.pull_dataArr[0, 0] = data[0] # 0位：布尔数据
        self.pull_dataArr[0, 1] = self.bytes2float(data[1]) # 1位：EMG
        for i in range(2,4):
            bytes_data = data[i]
            uV = self.get_uV(self.bytes2float(bytes_data))
            self.pull_dataArr[0, i] = uV                    # 2-3位：加速度
        print(self.pull_dataArr)
        print(time.time())
        # self.cnt_ += 1
        # print(self.cnt_)
        self.data_stream.pull(self.pull_dataArr)





    def clear(self, buffer):
        for i in range(self.channels):
            buffer[0, i] = 0

    def bytes2float(self, data):
        bytes8 = data
        if((bytes8&0x80)==0):
            result = bytes8
        else:
            bytes32 = bytes8^0xff
            bytes32 = bytes32+1
            result = -bytes32

        return result

    def get_uV(self, val):
        global LSB, gain
        uV = (val * LSB) / gain
        return val

if __name__ == '__main__':
    import time
    ds = Data_Stream(None)
    com = Com_Serve(ds)
    com.com_open(['COM11', 'COM5', 'COM7', 'COM9'], 921600)
    time.sleep(1000)


