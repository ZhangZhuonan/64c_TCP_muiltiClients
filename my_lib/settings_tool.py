# -*- coding: utf-8 -*-
import json

# 载入json文件
def load_json_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        dict = json.load(f)
        dict['savePath'] = path
        return dict

# 保存dict至json文件
def save_json_file(dict):
    with open(dict['savePath'], 'w', encoding='utf-8') as f:
        json.dump(dict, f, ensure_ascii=False, indent=4)

# 获取参数配置文件
def get_param4jsonFile(path):
    with open(path, 'r', encoding='utf-8') as f:
        dict = json.load(f)
    return dict

# 获取参数
def get_param(dict, index):
    val = None
    params_num = dict['params_num']
    if index < params_num:
        val = dict['p' + str(index)]['val']
    return val

# 从配置文件获取参数
def get_param4json_file(path, idx):
    dict = load_json_file(path)
    val = get_param(dict, idx)
    return val

def create_acquisition_params(path = '..\configuration\data_acquisition_params.json'):
    dict = {
        'name':'数据获取参数', # 参数组名称
        'params_num':10, # 参数个数
        'savePath':path, # 文件保存路径
        'p0': {'name': '串口号', 'type': 'str', 'unit': '', 'val': 'COM1'},
        'p1': {'name': '波特率', 'type': 'int', 'unit': '', 'val': 41600},
        'p2': {'name': '数据位', 'type': 'int', 'unit': '', 'val': 8},
        'p3': {'name': '停止位', 'type': 'int', 'unit': '1、1.5、2', 'val': 1},
        'p4': {'name': '奇偶校验位', 'type': 'str', 'unit': 'N、E、O', 'val': 'N'},
        'p5': {'name': 'ip地址', 'type': 'str', 'unit': '', 'val': '192.168.3.19'},
        'p6': {'name': '端口号', 'type': 'int', 'unit': '', 'val': 50003},
        'p7': {'name': '权值', 'type': 'float', 'unit': '', 'val': 0.286},
        'p8': {'name': '增益', 'type': 'int', 'unit': '', 'val': 6},
        'p9': {'name': '校验位使能', 'type': 'bool', 'unit': '', 'val': False},

    }
    # 将python字典保存至json文件
    with open(dict['savePath'], 'w', encoding='utf-8') as f:
        json.dump(dict, f, ensure_ascii=False, indent=4)

def create_curves_params(path = '..\configuration\curves_params.json'):
    dict = {
        'name':'波形显示参数', # 参数组名称
        'params_num':8, # 参数个数
        'savePath':path, # 文件保存路径
        'p0': {'name': '采样率', 'type': 'int', 'unit': 'points/s(重启软件后生效)', 'val': 250},
        'p1': {'name': '波形刷新周期', 'type': 'int', 'unit': 's', 'val': 5},
        'p2': {'name': '中值滤波', 'type': 'bool', 'unit': '', 'val': False},
        'p3': {'name': '低通截止频率', 'type': 'float', 'unit': '', 'val': 0.4},
        'p4': {'name': '高通截止频率', 'type': 'float', 'unit': '', 'val':150},
        'p5': {'name': '带通滤波', 'type': 'bool', 'unit': '', 'val': False},
        'p6': {'name': '抗工频干扰', 'type': 'bool', 'unit': '', 'val': False},
        'p7': {'name': '纵向缩放', 'type': 'float', 'unit': '', 'val': 0.5},

    }
    # 将python字典保存至json文件
    with open(dict['savePath'], 'w', encoding='utf-8') as f:
        json.dump(dict, f, ensure_ascii=False, indent=4)

def creat_init_params():
    create_curves_params()
    create_acquisition_params()

if __name__ == '__main__':
    creat_init_params()

