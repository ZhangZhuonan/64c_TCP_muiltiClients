import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage,QPixmap
from my_lib.btn_img_widget_UI import Ui_Form
import sys
import cv2


class Btn_Img_Widget(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Btn_Img_Widget, self).__init__()
        self.setupUi(self)
        img = cv2.imread(r'GUI\0.jpg')
        self.draw(img)

    def draw(self, img_src):
        # img_src = cv2.cvtColor(img_src,cv2.COLOR_BGR2RGB)
        # label_width = 300
        img_new = np.empty(img_src.shape)
        img_new[:,:,0] = img_src[:,:,2]
        img_new[:, :, 1] = img_src[:, :, 1]
        img_new[:, :, 2] = img_src[:, :, 0]
        img_src = img_new.astype(np.uint8)
        label_height = 300
        label_width = label_height * (img_src.shape[1] / img_src.shape[0])
        temp_imgSrc = QImage(img_src, img_src.shape[1], img_src.shape[0],img_src.shape[1]*3, QImage.Format_RGB888)
        # 将图片转换为QPixmap方便显示
        pixmap_imgSrc = QPixmap.fromImage(temp_imgSrc).scaled(label_width, label_height)
        # 使用label进行显示
        self.label_img.setPixmap(pixmap_imgSrc)

    def keyPressEvent(self, QKeyEvent):
        img_name = ''
        key_num = QKeyEvent.key()
        # 输入数字0-9
        if key_num >= 48 and key_num <= 57:
            img_name = str(key_num - 48)
        if key_num >= 65 and key_num <=90:
            img_name = chr(key_num-65+97)
        if len(img_name) == 1:
            print('切换图片：%s.jpg'%img_name)
            try:
                img = cv2.imread(r'GUI\%s.jpg'%img_name)
                self.draw(img)
            except:
                print('图片不存在！')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widg = Btn_Img_Widget()
    widg.show()
    # img = cv2.imread(r'GUI\0.jpg')
    # widg.draw(img)
    sys.exit(app.exec_())