import copy

from udp_Logic import UdpLogic
import numpy as np

LSB =  0.5364  # 权值
gain = 24      # 增益

class UDP_Client():
    def __init__(self, send_file_name):
        with open(send_file_name, 'rb') as send_f:
            f_data = send_f.read()
        self.local_ip = '192.168.3.19'
        self.local_port = 50004
        self.remote_ip = '192.168.3.19'
        self.remote_port = 50004

        # 数据保存参数初始化
        # 本地保存
        self.max_single_packs_num = 1000 # 保存的单条数据包所含帧数量
        self.max_packs_num = 75          # 保存的最大数据包（保存的最大帧数：max_single_packs_num * max_packs_num）
        self.saved_packs_num = 0         # 已保存的数据包数量
        self.save_bytesPacks = b''       # 保存当条字节数据包
        self.save_bytesPacks_list = []   # 字节数据包列表
        # 绘图数据包
        self.channels = 8
        self.draw_data_list = []    # 绘图数据包
        for i in range(self.channels):
            self.draw_data_list.append([])
        self.draw_data_len = 100    # 绘图数据包的数据长度
        self.now_len = 0            # 当前数据长度

        # self.us = UdpLogic()
        # self.us.socket_open_udp(self.local_ip, self.local_port)
        self.receive_fsm(f_data)
        print(len(self.draw_data_list[0]))
        np.save('data.npy', self.draw_data_list)

    # 0 -- 同步头1
    # 1 -- 同步头2
    # 2 -- 同步头3
    # 2 -- 数据长度
    # 3 -- 数据域
    # 4 -- 校验字1
    # 5 -- 校验字2
    # 接收状态机
    def receive_fsm(self, data):
        receive_status = 0  # 接收状态标志位
        header_data = []    # 帧头数据
        receive_data = []   # 接收数据
        receive_verify = [] # 接收校验位
        receive_cnt = 0     # 接收数据计数
        receive_len = 0     # 接收数据个数


        for d in data:
            # 0 -- 同步头1
            if receive_status == 0:
                if d == 0xAA:
                    header_data = []    # 帧头数据

                    receive_status = 1
                    header_data.append(d)
            # 1 -- 同步头2
            elif receive_status == 1:
                if d == 0xAA:
                    receive_status = 2
                    header_data.append(d)
                else:
                    receive_status = 0
            # 2 -- 同步头3
            elif receive_status == 2:
                if d == 0xF1:
                    receive_status = 3
                    header_data.append(d)
                else:
                    receive_status = 0
            # 3 -- 数据长度
            elif receive_status == 3:
                receive_status = 4
                receive_len = int(d)
                header_data.append(d)
                receive_cnt = 0
                receive_data.clear()
                receive_verify.clear()
            # 4 -- 数据域
            elif receive_status == 4:
                if receive_cnt >= receive_len - 1:
                    receive_data.append(d)
                    receive_status = 5
                else:
                    receive_data.append(d)
                    receive_cnt += 1

            # 5 -- 校验字1
            elif receive_status == 5:
                receive_verify.append(d)
                receive_status = 0
                # 校验
                if self.data_verify(header_data + receive_data,  receive_verify):
                    # 执行相应的操作
                    # time.sleep(0.0001)
                    self.cmd_execute(header_data+ receive_data + receive_verify)
        with open(time.strftime("data\%Y_%m_%d_%H_%M_%S", time.localtime()) + '.dat', 'wb') as f:
            f.write(self.save_bytesPacks)
            f.close()
            print('成功保存一个数据包！')


    def data_verify(self, data, v):
        sum_ = np.sum(data)
        verify_str = hex(sum_)[-2:]
        verify_v = int(verify_str, 16)
        if verify_v == v[0]:
            return True
        else:
            return False

    def verify(self, data):
        sum_ = np.sum(data)
        verify_str = hex(sum_)[-2:]
        verify_v = int(verify_str, 16)
        return verify_v

    def cmd_execute(self, data):
        # self.us.data_send_u(self.remote_ip, self.remote_port, data)
        print(0)
        self.save_bytesPacks += bytes(data)
        for i in range(2, 9):
            data_new = copy.deepcopy(data)
            data_new[2] = int('F%d'%i, 16)
            verify_v = self.verify(data_new[0:-1])
            data_new[-1] = verify_v
            self.save_bytesPacks += bytes(data_new)
        pass






if __name__ == '__main__':
    import time
    send_file_name = r'E:\Fish_WorkSpace\Fish_No4\UDP-50004端口数据绘制八路图\wozhang.dat'


    client = UDP_Client(send_file_name)









