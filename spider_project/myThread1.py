
'''
Descripttion: 线程1
Author: LJZ
Date: 2020-04-05 21:02:00
LastEditTime: 2020-11-13 19:25:31
'''
import time
from PyQt5.QtCore import QThread ,pyqtSignal

""" 线程1 显示进度条"""
class MyThread1(QThread):
    progressBarValue = pyqtSignal(int)  # 更新进度条
    

    def __init__(self,time_sleep=0.02, parent=None):
        super().__init__(parent=parent)
        self.flag = False
        self.time_sleep = time_sleep

    
    def run(self):
        for i in range(1,101):
            self.progressBarValue.emit(i)  # 发送进度条的值 信号
            time.sleep(self.time_sleep)

            if self.flag == True:
                print("进度条线程运行完\n")
                self.progressBarValue.emit(100)
                break
        
        
