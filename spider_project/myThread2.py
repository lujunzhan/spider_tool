'''
Descripttion: 线程2
Author: LJZ
Date: 2020-11-19 20:51:24
LastEditTime: 2020-11-19 22:38:47
'''
import time
from PyQt5.QtCore import QThread ,pyqtSignal

""" 线程2 """
class MyThread2(QThread):
    """ 此线程用于执行绘制词云操作 """
    draw_flag = pyqtSignal(int)  # 更新进度条
    

    def __init__(self, spider,image_name,parent=None):
        super().__init__(parent=parent)
        self.spider = spider
        self.image_name = image_name

    
    def run(self):

        self.draw_flag.emit(0)
        self.spider.draw(self.image_name)

        self.draw_flag.emit(1)