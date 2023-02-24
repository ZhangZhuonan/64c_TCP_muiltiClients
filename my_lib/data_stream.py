import csv
import time

import numpy as np

class Data_Stream:
    def __init__(self):
        self.buffer_pool = None          # 缓存池
        self.push_lock = 0  # 数据取出线程锁
        self.pull_lock = 0  # 数据存入线程锁
        self.Is_lock = 0    # 是否上线程锁：0-不上锁；1-上锁
        self.data_num = 65  # 数据位（时间戳+64个数据）
        self.singleMsg_len = 9      # 单条信息的有效数据长度【时间戳+8位数据】
        self.this_time = 0          # pool中最新一条数据的时间戳（为0表示空池，等待进来的第一条数据的时间戳作为本值）
        self.max_time_gap = 0.005   # pool单行数据中最大允许时间差
        # 标识帧头对应序号
        self.header_idx = {'F1':0, 'F2':1, 'F3':2, 'F4':3, 'F5':4, 'F6':5, 'F7':6, 'F8':7}

    # == 对外函数 ==

    # 向pool推送数据
    def pull(self,header, buffer_stream):
        if self.pull_lock == 0 :
            self.pull_lock = self.Is_lock
            if self.push_lock == 0 :
                # pool中无数据，将推送的本条数据作为池中的第一条数据
                if self.buffer_pool is None:
                    self.buffer_pool = np.zeros([1, self.data_num])
                    self.this_time = 0
                # 本条推送信息非空
                if buffer_stream is not None:
                    # 数据长度核验
                    if buffer_stream.shape[1] == self.singleMsg_len:
                        new_time = buffer_stream[0] # 新入数据据的时间
                        # 若新条数据的时间与pool最新行时间戳间隔超过设定范围：
                        if abs(new_time-self.this_time) > self.max_time_gap:
                            self.buffer_pool = np.r_[self.buffer_pool, np.zeros([1, self.data_num])]    # pool新增一行
                        col_start, col_end = self.get_colPos_by_header(header)  # 根据帧头获取新数据在Pool中的列坐标
                        # 若存帧头合法
                        if col_end > col_start:
                            self.buffer_pool[-1, col_start: col_end] = buffer_stream
                if self.buffer_pool.shape[0] > 50:
                    self.buffer_pool = None
            else:
                pass
                print('push is lock!')
            self.pull_lock = 0


    # 获取数据池数据
    def acquire(self):
        data_stream = None
        if self.push_lock == 0 :
            s = time.time()
            self.push_lock = self.Is_lock
            if self.pull_lock == 0 :
                if self.buffer_pool is not None:
                    data_stream = self.buffer_pool
                    self.buffer_pool = None
                    print(data_stream.shape)
            else:
                pass
                print('pull is lock!')
            self.push_lock = 0
            e = time.time()
            # print('push cost%f'%(s-e))
        return data_stream

    # 重启
    def re_start(self):
        self.buffer_pool = None          # 缓存池
        self.push_lock = 0  # 数据取出线程锁
        self.pull_lock = 0  # 数据存入线程锁

        # self.init_savedata()

    # 初始化存储数据文件
    def init_savedata(self):#wyz
        self.file = open('data/'+time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())+'.csv','w',newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.file)

    # 停止存储文件
    def stop_savedata(self):
        try:
            self.file.close()
        except:
            pass

    # == 工具函数 ==

    # 根据标识帧头和推入数据长度确定存入pool的列坐标
    def get_colPos_by_header(self, header):
        try:
            idx = self.header_idx[header]
        except:
            print('非法帧头！')
            return 0, 0
        start = idx * 8 + 1
        end = (idx+1) * 8 + 1
        return start, end

if __name__ == '__main__':
    ds = Data_Stream()
    now_time = 0
    headers = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8']
    count = 0
    while True:

        for header in headers:
            msg = np.ones([1, 65]) * time.time()
            start = time.time()
            ds.pull(header, msg)
            end = time.time()
            print('pull cost %fs'%(end-start))
        count += 1
        print('loop%d'%count)
        time.sleep(0.005)










