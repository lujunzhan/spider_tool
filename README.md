<!--
 * @Descripttion: markdown描述
 * @Author: LJZ
 * @Date: 2020-11-19 20:51:24
 * @LastEditTime: 2020-11-19 23:07:53
-->
## Bilibili排行榜爬取小工具
#### python爬虫小工具，使用pyqt5做UI界面

`环境：Python3.7.6`

#### 安装第三方库


    $ pip install requests
    $ pip install lxml
    $ pip install wordcloud
    $ pip install jieba
    $ pip install PyQt5


#### 目录结构
~~~
SPIDER_TOOL 
├─spider_project        应用目录
│  ├─__pycache__        公共模块目录（可以更改）
│  ├─build              模块目录
│  │
|  ├─data               数据文件夹
|  ├─images             图片文件夹
│  ├─main.py            运行启动入口
│  ├─myThread1.py       线程类1
│  ├─myThread2.py       线程类2
│  ├─save_choice.py     保存按钮文件（未完善）
│  ├─spider_.py         爬虫类
│  └─v1.py              pyqt5布局类

~~~

#### 程序界面
![Alt](https://csgduanzhou-pic.oss-cn-shenzhen.aliyuncs.com/my_self/cover.png)