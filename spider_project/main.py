import sys
import time
import re

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QMessageBox , QStyleFactory
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt, QThread, QCoreApplication, QSize

from v1 import Ui_mainWindow
from save_choice import Ui_export_form
from spider_ import spider
from myThread1 import MyThread1
from myThread2 import MyThread2


""" 显示另一个窗口 """
windowList = [] 


""" 主窗口 """
class My_Win(QMainWindow, Ui_mainWindow):
    def __init__(self, parent = None):
            super(My_Win, self).__init__(parent)
            self.setupUi(self)
            self.init_ui()
            
    
    def init_ui(self):
        """ 初始化ui函数 """
        #设置制作词云选择标志
        self.wc_sel_flag = False
        self.draw_flag = False
        self.save_form = '.txt'

        # self.setIconSize(QSize(100,100))
        self.setWindowIcon(QIcon(QPixmap(r'spider_project\images\b_icon.png')))
        self.setWindowTitle('抓取小工具')

        """ 显示词云图片 """
        pixmap = QPixmap(r"spider_project\images\spider1.png")
        self.image_show.setPixmap(pixmap)
        self.image_show.setScaledContents(True)

        """ 添加状态栏 """
        self.status = self.statusBar()

        """ 导入按钮 """
        self.export_btn.clicked.connect(self.export_event)
        """ 添加导入小窗口 """
        # 创建新的小窗口
        self.Dialog1 = QWidget()
        self.dial = Ui_export_form()
        self.dial.setupUi(self.Dialog1)
        self.dial.save_txt.toggle()
        print(self.save_form)

        """ 开始按钮 """
        self.start_btn.clicked.connect(self.spider_start)
        
        """ 退出按钮 """
        self.exit_btn.clicked.connect(self.exit)
        """ 重置按钮 """
        self.reset_show.clicked.connect(self.reset)
        """ 制作词云选择 """
        # self.wc_sel.toggle()
        self.wc_sel.stateChanged.connect(self.change_wc_sel)
        """ 选择框链接 """
        # 初始化
        self.combox_setting()
        self.list_choose.activated[str].connect(self.onActivated)

    """------------------------------------------------------------ 此处为分界线1 ---------------------------------------------------------- """
    def export_event(self):
        """ 显示小窗口 """
        print("进入导入按钮")
        print(self.dial)
        
        """ 设置文件格式选择 """
        self.dial.save_txt.toggled.connect(self.choose)
        self.dial.save_csv.toggled.connect(self.choose)
        self.dial.save_json.toggled.connect(self.choose)
        # 两个按钮的信号连接
        self.dial.ok_btn.clicked.connect(self.ok_btn_event)
        self.dial.cancel_btn.clicked.connect(self.Dialog1.close)

        windowList.append(self.Dialog1)

        self.Dialog1.setWindowTitle('设置保存格式')
        self.Dialog1.setWindowIcon(QIcon(r'spider_project\images\b_icon.png'))
        self.Dialog1.show()
    

    def ok_btn_event(self):
        print("OK")
    
    def choose(self):
        """ 选择保存格式 """
        if self.dial.save_txt.isChecked():
            print(".txt:check!")
            self.save_form = '.txt'
            self.dial.save_txt.toggle()

        elif self.dial.save_csv.isChecked():
            self.save_form = '.csv'
            print(".csv:check!")
            self.dial.save_csv.toggle()

        elif self.dial.save_json.isChecked():
            self.save_form = '.json'
            print(".json:check!")
            self.dial.save_json.toggle()

        # elif self.dial.save_excel.isChecked():
        #     pass
    
    """ -----------------------------------------------------------QComboBox -------------------------------------------------------------- """
    def combox_setting(self):
        """ 对QCombox进行初始化设置 """
        self.choose_lsts = ['全站', '番剧', '国产动画', '国创相关', '记录片', '动画', '音乐', '舞蹈', '游戏', '知识', '数码', '生活', '美食', '鬼畜',
         '时尚', '娱乐', '影视','电影','电视剧','原创','新人']
        
        for choose in self.choose_lsts:
            self.list_choose.addItem(choose)


    def onActivated(self, text):
        """ 可以选择的排行榜单url """
        urls = [
        "https://www.bilibili.com/v/popular/rank/all",
        "https://www.bilibili.com/v/popular/rank/bangumi","https://www.bilibili.com/v/popular/rank/guochan",\
        "https://www.bilibili.com/v/popular/rank/guochuang","https://www.bilibili.com/v/popular/rank/documentary",\
        "https://www.bilibili.com/v/popular/rank/douga","https://www.bilibili.com/v/popular/rank/music",\
        "https://www.bilibili.com/v/popular/rank/dance","https://www.bilibili.com/v/popular/rank/game",\
        "https://www.bilibili.com/v/popular/rank/technology","https://www.bilibili.com/v/popular/rank/digital",\
        "https://www.bilibili.com/v/popular/rank/life", "https://www.bilibili.com/v/popular/rank/food", \
        "https://www.bilibili.com/v/popular/rank/kichiku", "https://www.bilibili.com/v/popular/rank/fashion", \
        "https://www.bilibili.com/v/popular/rank/ent", "https://www.bilibili.com/v/popular/rank/cinephile", \
        "https://www.bilibili.com/v/popular/rank/movie", "https://www.bilibili.com/v/popular/rank/tv", \
        "https://www.bilibili.com/v/popular/rank/origin","https://www.bilibili.com/v/popular/rank/rookie",\
        ]
        #选择索引
        index = self.choose_lsts.index(text)
        #打印网址
        print(urls[index])
        #显示在界面上
        self.url_input.setText(urls[index])

    """------------------------------------------------------------ 此处为分界线2 ---------------------------------------------------------- """

    def check_url(self,url = 'https://www.bilibili.com/v/popular/rank/all'):
        """ 对输入的网址进行初步检验 """
        
        # 正则表达式初步判断是否为网址
        reg = r'^([hH][tT]{2}[pP]:\/\/|[hH][tT]{2}[pP][sS]:\/\/)'
        # 分别获取用户输入的网址和xpath规则
        url_get = self.url_input.text()

        # 正则验证网址
        is_url = re.search(reg, url_get)
        # print(url_get)

        """ url网址的输入 """
        if url_get:
            if is_url:
                url = url_get
                print("网址经过检验：",url)
            else:
                self.url_input.setText("输入网址错误，将抓取默认网址~")

        return url

    def check_xpath(self,web_data,spider1):
        """ xpath规则的输入 """

        xpath_get = self.xpath_input.text()
        # 根据获取的xpath调用函数
        if xpath_get:
            xpaht_input = xpath_get
            print("文本框输入的xpath为：",xpath_get)
            html_data = spider1.deal_data(web_data, xpath_get)
        else:
            html_data = spider1.deal_data(web_data)
        
        return html_data


    def spider_start(self):
        """ 开始爬虫 """    
        
        """ 设置一个线程给进度条显示 """
        self.thread1 = MyThread1()
        self.thread1.progressBarValue.connect(self.progerss_change)
        """ 启动进度条 """
        self.thread1.start()

        # 检验网址
        
        url = self.check_url()
        # 新建爬虫
        spider1 = spider()
        web_data = spider1.getHTMLText(url)

        # 检验xpath 并返回处理的数据
        html_data = self.check_xpath(web_data, spider1)
        spider1.write_file(html_data,self.save_form)
        
        # 将爬取的信息打印在显示器上
        count = 1
        for i in html_data:
            info = str(count) + ":" + i    
            self.console_show.append(info)
            count+=1
        
        # 在状态栏上显示完成
        self.show_statusmessage("数据抓取完成！")

        """ 词云绘制 """
        image_name = r'spider_project\images\spider1.png'

        # 检查是否需要绘制词云
        if self.wc_sel_flag:
            """ 用线程2绘制词云 """    
            self.thread2 = MyThread2(spider1, image_name)
            self.thread2.draw_flag.connect(self.draw_progress)
            self.thread2.start()
            """ 再创建线程3更新进度条 """
            self.thread3 = MyThread1(0.35)
            self.thread3.progressBarValue.connect(self.progerss_change)
            self.thread3.start()

            self.show_statusmessage("词云还在绘制，请稍等。。。")

            
        else:
            print("不用绘制词云")

        if self.thread1.isRunning():
            self.thread1.flag = True
            # self.wc_sel.stateChanged.disconnect(self.change_wc_sel)
            # self.thread1.quit()
            # self.thread1.terminate()
        del self.thread1

        self.progerss_change(100)
        print("线程1删除 程序结束")
        
        self.progressBar.setValue(0)          
            
    """------------------------------------------------------------ 此处为分界线3 ---------------------------------------------------------- """
    
    def show_statusmessage(self, message=''):
        """ 状态栏显示进程信息 """
        self.statusBar().showMessage(message)
    
    def reset(self):
        """ 重置显示栏 """
        self.console_show.setText("")
        self.show_statusmessage("显示器已经重置~")

    def change_wc_sel(self, state):
        """ 选择是否制作词云 """

        if state == Qt.Checked:
            self.wc_sel_flag = True
        else:
            self.wc_sel_flag = False

    def progerss_change(self, i):
        """ 进度条更新 """
        self.progressBar.setValue(i)

    def draw_progress(self, draw_flag):
        """ 利用线程进行绘图 """
        self.draw_flag = draw_flag
        if self.draw_flag:
            image_name = r'spider_project\images\spider1.png'
            self.show_statusmessage("词云绘制完成！")
            self.thread3.flag = True
            pixmap = QPixmap(image_name)
            self.image_show.setPixmap(pixmap)
            del self.thread2
            del self.thread3

        else:
            print("还未完成")

    
    def exit(self):
        """ 退出按钮 """
        reply = QMessageBox.question(self, '退出程序', '你确定退出程序吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            w.close()


    """------------------------------------------------------------ 此处为分界线4 ---------------------------------------------------------- """        
        
""" 程序执行 """
if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    w = My_Win()    
    w.show()
    
    sys.exit(app.exec_())