import time
from anyio import create_tcp_listener, run
import socket
# 本地文件引用
from my_lib.FSM import FSMs           # 解包状态机

# 异步多客户端TCP服务器端
class TCP_Async_Sever():
    def __init__(self,Data_Stream=None, max_clientNum=1):
        self.Is_liscening = True            # 监听中标志位
        self.data_staream = Data_Stream
        self.max_clientNum = max_clientNum  # 最大连接客户端数量
        self.client_num = 0                 # 客户端连接数量
        self.clientPort_list = []           # 客户端端口列表
        # 开启解包线程与数据流处理接口
        if Data_Stream is not None:
            # 创建解包状态机列表对象
            self.FSMs = FSMs(self.data_staream, max_clientNum)

    # == 对外函数 ==
    # 服务器开启函数
    def open(self, ip, port):
        '''
        TCP客户端开启函数
        :param ip:   本机Ip地址
        :param port: 本机端口
        :return:
                Is_open: 服务器开启成功标志位【T：成功，F：失败】
                error：失败原因（若开启成功为空字符）
        '''
        self.ip = ip
        self.port = port
        # 判定ip、port是否合法
        if self.ip_port_isLeagal(ip, port):
            self.start_liscening()
            # try:
            #     self.start_liscening()              # 开启服务器监听
            # except:
            #     print('服务器打开失败！')
            #     return False, '服务器打开失败！'       # 服务器打开失败
            # else:
            #
            #     return True, ''                     # 开启成功
        else:
            print('地址与端口非法！')
            return False, '地址与端口非法！'           # 输入的ip、port字符非法

    # 服务器关闭函数
    def close(self):
        self.Is_liscening = False

    # == 内部函数 ==

    # 客户端连接中断处理函数
    async def handle(self, client):
        async with client:
            if self.client_num + 1 > self.max_clientNum:            # 若连接客户端数量超过最大连接数，则不响应
                print('连接客户端超过最大连接数量！')
                return
            self.client_num +=  1                                   # 更新连接客户端数量
            client_ip_port = client._raw_socket._sock.getpeername() # 连接客户端ip、port
            print('第%d个客户端连接成功：[ip:%s,port:%s]'              # 打印本次连接客户端的ip、port
                  %(self.client_num, client_ip_port[0], client_ip_port[1]))
            self.FSMs.bind_ID(client_ip_port[1])                    # 通过客户端port绑定状态机
            # 客户端监听循环
            while self.Is_liscening:
                try:
                    recv_msg = await client.receive(1024)               # 接收客户端发送信息
                # 客户端接收信息获取失败：客户端连接已断开
                except:
                    self.FSMs.unbind_ID(client_ip_port[1])              # 解绑状态机绑定ID
                    self.client_num -= 1                                # 客户端数量减一
                    return
                # 客户端成功接收非空信息，向数据流类发送
                else:
                    if self.data_staream is not None:
                        self.FSMs.getFSM_byID \
                            (client_ip_port[1]).receive_fsm(recv_msg)   # 运行解包状态机程序
                                                                        # 解包完成自动像数据量推送数据

    # 开启服务端异步监听
    async def start_sever_liscening_async(self):
        listener = await create_tcp_listener(local_host=self.ip, local_port=self.port)
        await listener.serve(self.handle)

    # 开启服务端监听
    def start_liscening(self):
        run(self.start_sever_liscening_async)

    # == 工具类 ==

    # 获取本地IP地址列表
    def get_localIP(self):
        res = socket.gethostbyname(socket.gethostname())
        if type(res) == str:
            ip_list = res.split()
        elif type(res) == list:
            ip_list = res
        else:
            ip_list = list[res]
        return ip_list

    # 判断IP与端口是否合法
    def ip_port_isLeagal(self, ip, port):
        if type(ip) != str:
            return False
        if len(ip.split('.')) != 4:
            return False
        if type(port) != int:
            return False
        return True



if __name__ == '__main__':
    from my_lib.data_stream import Data_Stream
    data_stream = Data_Stream()
    sever = TCP_Async_Sever(Data_Stream=data_stream,max_clientNum=8)       # 创建TCP服务器
    ip = sever.get_localIP()[0]     # 获取本地IP
    port = 9999                     # 设置端口
    print('ip=%s, port=%d'%(ip, port))
    sever.open(ip, port)            # 打开服务器
    print('ok')
    time.sleep(2)
    sever.open(ip, port)
    print('ok2')



