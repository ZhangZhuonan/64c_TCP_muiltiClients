# -*- coding: utf-8 -*-
import socket
import threading
import time
import numpy as np
from my_lib.data_stream import *
from my_lib.FSM import FSM
from my_lib.stopThreading import stop_thread

class TCP_Server():
    def __init__(self, data_stream):
        super(TCP_Server, self).__init__()
        self.data_stream = data_stream
        # TCP参数初始化
        self.server = None     # 代表TCP socket
        self.server_th = None  # 接收线程
        self.con = None
        self.Is_init = False  # 初始化标志位

    # TCP打开函数
    def open(self, ip, port):
        lo_ip = ip
        lo_port = port
        lo_ip_port = (lo_ip, int(lo_port))
        self.BUFSIZE = 4096 * 4
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server.bind(lo_ip_port)  # 绑定地址
        except Exception as ret:
            print('Error:', ret)
            self.close()
        else:
            print('TCP 连接成功建立')
            # 初始化状态机
            self.FSM = FSM(self.data_stream)
            # 建立客户端监听线程
            self.server_th = threading.Thread(target=self.TCP_client_concurrency)
            self.server_th.setDaemon(True)
            self.server_th.start()
            self.Is_init = True

    # TCP客户端监听执行函数
    def TCP_client_concurrency(self):
        # 等待客户端连接
        is_connect = False
        while is_connect is False:
            self.server.listen(1)
            self.con, address = self.server.accept()
            is_connect = True
        # 与连接成功的客户端通信
        while True:
            try:
                recv_msg = self.con.recv(self.BUFSIZE)
            except Exception as ret:
                pass
            else:
                if len(recv_msg)> 5:
                    self.FSM.receive_fsm(recv_msg)
                    time.sleep(0.005)
                else:
                    time.sleep(1)

    # 关闭TCP函数
    def close(self):
        try:
            self.server.close()
            self.Is_init = False
        except Exception as ret:
            pass
        try:
            stop_thread(self.server_th)
        except Exception as ret:
            pass

if __name__ == '__main__':
    import time
    ds = Data_Stream()
    server = TCP_Server(ds)
    server.open('192.168.1.105', 50003)
    time.sleep(1000)


