'''
Descripttion: 
version: 
Author: LJZ
Date: 2020-04-04 01:16:46
LastEditTime: 2020-11-13 20:07:58
'''
import requests
import json
#分析网页
from lxml import etree

import time
import datetime
#词云
from wordcloud import WordCloud
# import imageio
from jieba import lcut


class spider():
    """ 编写一个爬虫类模板 """

    def __init__(self):
        super().__init__()

    def getHTMLText(self, url):
        """ 爬取网页 """

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

            r = requests.get(url, headers=headers)
            """ 如果状态码不是200 则会引起HTTPerror异常 """
            r.raise_for_status()

            status = r.status_code
            print("状态码为：", status)

            # 编码转换
            # r.encoding = r.apparent_encoding
            r.encoding = 'utf-8'
            #返回网页代码
            return r.text

        except:
            return "产生异常"

    def draw(self, image_name, save_form='.txt'):
        """ 将数据绘成词云 """
        #定义词云参数
        w = WordCloud(
            height=2400,
            width=2400,
            background_color="white",
            max_font_size=400,
            min_font_size=20,
            max_words=500,
            # random_state= 42,
            # collocations=False,

            # mask=mk,
            # font_path="D:/pscc/ps字体/字体/晴圆.ttf"
        )

        # 设置读入的解码方式
        file_path = r'spider_project\data\info' + save_form

        try:
            if save_form == '.txt' or save_form == '.csv':
                with open(file_path, 'r+', encoding='utf-8') as file3:
                    contents = file3.read()
                    # print(contents.rstrip() + "\n")
                    """ 使用jieba库进行中文分词 """
                    text = ' '.join(lcut(contents.rstrip()))
                    # print(text)
            elif save_form == '.json':

                with open(file_path, 'r+', encoding='utf-8') as file4:
                    contents = json.load(file4)

                    """ 使用jieba库进行中文分词 """
                    # 注意要先定义total数据类型
                    total = ''
                    for i in contents:
                        # 将字符串汇聚成一个大字符串
                        total = total + i
                    # 对大字符串进行分割
                    text = ' '.join(lcut(total))

        except:
            print("读取文件产生异常！")
            return

        w.generate(text)

        print("绘制完成!")
        # 保存
        w.to_file(image_name)

    def write_file(self, html_data, save_form=".txt"):
        """ 将处理后的数据写入文件中 """

        file_path = r'spider_project\data\info' + save_form

        try:
            if save_form == '.txt' or save_form == '.csv':
                with open(file_path, 'w', encoding='utf-8') as file1:
                    # 添加时间戳
                    file1.write("时间："+str(datetime.datetime.now())+'\n\n')
                    for i in html_data:
                        file1.write(i)
                        file1.write('\n')                       
            # 当要求json格式时
            elif save_form == '.json':
                list1 = []
                with open(file_path, 'w', encoding='utf-8') as file2:

                    for i in html_data:
                        list1.append(i)

                    json.dump(list1, file2, ensure_ascii=False, indent=4)

        except:
            print("出现异常，无法将数据写入文件")
        else:
            print("写入完成！  共" + str(len(html_data)) + '条信息')

    def deal_data(self, web_data, xpath_input='.//div[@class = "content"]/div[2]/a/text()'):
        self.save_htm(web_data)

        """ 对获取的网页进行解析 """
        try:
            html = etree.HTML(web_data)
            html_data = html.xpath(xpath_input)
        except:
            print("产生异常！")
            return

        if html_data:
            print("xpath输入正常")
        else:
            print("xpath输入不正确！,请检验！")

        return html_data

    def save_htm(self, web_data):
        """ 将返回的网页写入文件便于查错 """
        file_p = r'spider_project\data\html_back.htm'
        try:
            with open(file_p, 'w', encoding='utf-8') as f1:
                f1.write(web_data)
        except:
            print("产生异常！")


if __name__ == "__main__":

    url = "https://www.bilibili.com/v/popular/rank/all"

    # url = 'https://www.bilibili.com/v/technology/?spm_id_from=333.851.b_7072696d6172794368616e6e656c4d656e75.49'
    spider1 = spider()
    web_data = spider1.getHTMLText(url)
    print(web_data)
    
    # html = etree.HTML(web_data)
    # html_data = html.xpath(r'/html/body//*[@class="groom-module"]/a/div[2]/p/text()')
    # print(html_data)
    # print(len(html_data))
    # print("done!")

    # html_data = spider1.deal_data(web_data r'/html/body//*[@class="groom-module"]/a/div[2]/p/text()')
    html_data = spider1.deal_data(web_data)
    spider1.write_file(html_data, '.txt')
    # 设置图片名称
    image_name = r'spider_project\images\info.png'
    """ 绘制词云 """
    spider1.draw(image_name, '.txt')
