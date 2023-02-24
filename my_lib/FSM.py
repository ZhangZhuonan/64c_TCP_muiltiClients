# -*- coding: utf-8 -*-
import time
import numpy as np
from my_lib.settings_tool import *
global receive_status
from my_lib.settings_tool import get_param4json_file
path = 'configuration\data_acquisition_params.json'

# 解包状态机
class FSM:
    def  __init__(self, data_stream):
        # 初始化状态机参数
        self.receive_status = 0  # 接收状态标志位
        self.header_data = []    # 帧头数据
        self.receive_data = []   # 接收数据
        self.receive_cnt = 0     # 接收数据计数
        self.receive_len = 0     # 接收字节数
        self.receive_data_num = 8# 转换完成数据个数
        self.scale_factor = 1       # 缩放系数
        self.LSB =  0.5364          # 权值
        self.gain = 24              # 增益
        self.count = 0              # 状态机获取数据条数量
        self.Is_check = True        # 是否进行校验

        # 获取配置文件中的参数，重启后生效
        try:
            self.LSB = get_param4json_file(path, 7)
            self.gain = get_param4json_file(path, 8)
            self.Is_check = get_param4json_file(path, 9)
        except:
            pass

        self.pull_dataArr = np.zeros([1, self.receive_data_num + 1])# 1个时间戳+8个四字节数据
        self.data_stream = data_stream  # 数据流类，负责解包完成后的数据缓存，等待控制程序获取

    # 接收状态机
    def receive_fsm(self, data):
        for d in data:
            # 0 -- 同步头1
            if self.receive_status == 0:
                if d == 0xAA:
                    self.receive_status = 1
                    self.header_data.append(d)
            # 1 -- 同步头2
            elif self.receive_status == 1:
                if d == 0xAA:
                    self.receive_status = 2
                    self.header_data.append(d)
                else:
                    self.receive_status = 0
                    print('error!!!!!!!!!!!!!!!!!!!!!!!!')
            # 2 -- 同步头3 【标识帧头】
            elif self.receive_status == 2:
                self.receive_status = 3
                self.header_data.append(d)

            # 3 -- 数据长度
            elif self.receive_status == 3:
                self.receive_len = int(d)
                self.receive_status = 4
                self.header_data.append(d)
                self.receive_cnt = 0
                self.receive_data.clear()

            # 4 -- 数据域
            elif self.receive_status == 4:
                if self.receive_cnt >= self.receive_len - 1:
                    self.receive_data.append(d)
                    self.receive_status = 5
                else:
                    self.receive_data.append(d)
                    self.receive_cnt += 1

            # 5 -- 校验字1
            elif self.receive_status == 5:
                if self.Is_check:
                    check_word = self.sum_check(self.header_data + self.receive_data)
                    if d == check_word:
                        self.cmd_execute(self.header_data[2], self.receive_data) # 对接收到的数据进行处理
                else:
                    self.cmd_execute(self.header_data[2], self.receive_data) # 对接收到的数据进行处理
                self.count += 1
                print('get %d mesg, length=%d'%(self.count, len(self.receive_data)))
                self.receive_status = 0  # 接收状态标志位
                self.header_data = []    # 帧头清零
                self.receive_data = []   # 接收数据
                self.receive_cnt = 0     # 接收数据计数
                self.receive_len = 0     # 接收数据个数

    # 接收数据处理
    def cmd_execute(self,header, data):
        my_header = header                      # 标识帧头
        data_len = 4                            # 单数据字节数
        data_num = int(len(data) / data_len)    # 数据总数
        self.pull_dataArr[0, 0] = time.time()   # 第一位是时间戳
        # 8位数据转换
        for i in range(data_num):
            bytes_data = data[i * data_len: (i+1) * data_len]
            uV = self.get_uV(self.bytes2float(bytes_data))
            self.pull_dataArr[0, 1 + i] = uV
        self.data_stream.pull(my_header, self.pull_dataArr) # 向数据流类推送一条数据


    # 校验和计算
    def sum_check(self, data):
        sum_num = np.sum(np.array(data))
        sum_str = hex(sum_num)[-2:]
        check_num = int('0x'+sum_str, 16)
        return check_num

    # 字节数据转换为浮点数据
    def bytes2float(self, data):
        bytes32 = data[3]<<24 | data[2]<<16 | data[1]<<8 | data[0]
        if((bytes32&0x80000000)==0):
            result = bytes32
        else:
            bytes32 = bytes32^0xffffffff
            bytes32 = bytes32+1
            result = -bytes32
        return result

    # 转换为单位为uV的电压值
    def get_uV(self, val):
        uV = self.scale_factor * (val * self.LSB) / self.gain
        return uV

    # 2字节16进制数组转10进制数值
    def hex2_arr2dec_val(self, hex2_arr):
        dec_val = 0                 # 10进制数值
        hex_arr = []                # 16进制单字节数组
        for hex_val in hex2_arr:
            H_val = hex_val // 16   # 两位字节中的高位数值dec
            L_val = hex_val % 16    # 两位字节中的低位数值dec
            hex_arr.append(H_val)
            hex_arr.append(L_val)
        n = len(hex_arr)
        for i in range(n):
            dec_val += hex_arr[n-1-i] * np.power(16, i)
        return dec_val

# 解包状态机复合类
class FSMs():
    def __init__(self,data_stream, FSM_num):
        self.data_stream = data_stream
        self.FSM_list = []          # 状态机列表
        self.bindID_list = []       # 绑定ID列表
        # 初始化状态机列表与绑定ID列表
        for i in range(FSM_num):
            new_FSM = FSM(data_stream)
            self.FSM_list.append(new_FSM)
            self.bindID_list.append(None)
    # == 对外函数 ==

    # 绑定新的ID到空闲状态机
    def bind_ID(self, ID):
        idleFSM_idx = self.get_idleFSM_idx()    # 获取空闲状态机序号
        print('ID:%s成功绑定%d号状态机！'%(ID, idleFSM_idx))
        self.bindID_list[idleFSM_idx] = ID      # 绑定ID与空闲状态机

    # 解绑状态机绑定ID
    def unbind_ID(self, ID):
        idx = self.get_IDidx(ID)            # 获取ID对应序号
        # 让对应序号下的ID列表和状态机列表清零
        self.bindID_list[idx] = None
        print('ID:%s成功解除绑定%d号状态机！'%(ID, idx))
        new_FSM = FSM(self.data_stream)
        self.FSM_list[idx] = new_FSM

    # 获取绑定ID序号
    def get_IDidx(self, aim_ID):
        aim_idx = -1
        for idx, ID in enumerate(self.bindID_list):
            if ID == aim_ID:
                aim_idx = idx
                break
        return aim_idx

    # 根据ID获取对应状态机对象
    def getFSM_byID(self, ID):
        idx = self.get_IDidx(ID)
        print(self.FSM_list[idx])
        return self.FSM_list[idx]

    # == 对内函数 ==

    # == 工具函数 ==

    # 获取空闲状态机序号
    def get_idleFSM_idx(self):
        idleFSM_idx = -1    # 空闲状态机序号
        for idx, ID in enumerate(self.bindID_list):
            if ID is None:
                idleFSM_idx = idx
                break
        return idleFSM_idx







