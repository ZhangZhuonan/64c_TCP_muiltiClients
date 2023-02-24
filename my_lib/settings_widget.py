# -*- coding: gb2312 -*-
from PyQt5.QtGui import QFont
import numpy as np
import sys
from my_lib.settings_widget_ui import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from my_lib.settings_tool import *

class Settings_Widget(QWidget, Ui_Settings_Form):
    roi_material = pyqtSignal(str)
    def __init__(self, parent=None):
        super(Settings_Widget, self).__init__(parent)
        # self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        self.setupUi(self)

    # 参数字典传入初始化函数
    def table_init(self, dict1):
        self.dict1 = dict1
        self.add_section(dict1, self.tableWidget_1)


    def add_section(self, dict, table):
        params_num = dict['params_num'] # 参数个数
        table.setRowCount(params_num)
        table.setColumnCount(3)
        table.verticalHeader().setVisible(True)
        table.setHorizontalHeaderLabels(['参数名', '值', '说明'])
        table.horizontalHeader().setVisible(True)
        font = QFont("黑体", 10)  # 'Arial'
        table.setColumnWidth(0, 150)
        table.setColumnWidth(2, 50)
        table.horizontalHeader().setFont(font)
        table.horizontalHeader().setStretchLastSection(True)
        for i in range(params_num):
            params_dict = dict['p'+str(i)]
            newItem = QTableWidgetItem(params_dict['name'])
            newItem.setFont(font)
            table.setItem(i, 0, newItem)

            if params_dict['type'] == 'bool':
                newItem = QTableWidgetItem()
                if params_dict['val'] is True:
                    newItem.setCheckState(Qt.Checked)
                else:
                    newItem.setCheckState(Qt.Unchecked)
            else:
                newItem = QTableWidgetItem(str(params_dict['val']))
                newItem.setFont(font)
            table.setItem(i, 1, newItem)
            newItem = QTableWidgetItem(params_dict['unit'])
            newItem.setFont(font)
            table.setItem(i, 2, newItem)
            table.setRowHeight(i,35)
        self.resize(375, 35*params_num+35)
        params_title = dict['name']
        self.setWindowTitle(params_title)

    # ==从表格中获取参数数值
    def get_params4tableWidget(self, dict, table):
        params_num = dict['params_num'] # 参数个数
        params_title = dict['name']

        for i in range(params_num):
            param_i = dict['p'+str(i)]
            val_str = table.item(i, 1).text() # 当前参数修改后的值字符串
            val_type = param_i['type']
            if val_type == 'str':
                try:
                    val = val_str
                except:
                    return 'error'
            elif val_type == 'int':
                try:
                    val = int(val_str)
                except:
                    return 'error'
            elif val_type == 'float':
                try:
                    val = float(val_str)
                except:
                    return 'error'
            elif val_type == 'bool':
                check_state = table.item(i, 1).checkState()
                if check_state == Qt.Checked:
                    val = True
                elif check_state == Qt.Unchecked:
                    val = False
                else:
                    return 'error'
            else:
                val = val_str
            param_i['val'] = val
        return dict

    # =窗口属性设置=
    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None
    #
    # def leaveEvent(self, e: QMouseEvent):
    #     # self.outsize = True
    #     self.close()

    def closeEvent(self, QCloseEvent):
        self.dict1 = self.get_params4tableWidget(self.dict1, self.tableWidget_1)
        print(self.dict1)
        save_json_file(self.dict1)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    Table = Settings_Widget()
    calc_dict = load_json_file(r'..\configuration\data_acquisition_params.json')
    Table.table_init(calc_dict)
    Table.show()
    sys.exit(app.exec_())



