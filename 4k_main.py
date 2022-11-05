# @Author:Water_bros
# @StartDate:2021-11-13(GMT+8:00 19:30)
# @FinishDate:2021-11-20(GMT+8:00 12:52)
# @ProgramName:4K壁纸下载小助手
# @Version:3.0
# @Goal:A birthday gift to author
# @CopyRight © 2021 Water_bros,All Rights Reserved.

from PyQt5 import QtCore, QtGui, QtWidgets  # 导入必要模块
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from random import choice
from time import sleep
from settings import UA, Connect, Pay
import requests
import os
import bs4
import sys

if os.path.exists(r"D:/PicturesDownload") == False:  # 保存文件夹
    os.mkdir(r"D:/PicturesDownload")
else:
    pass

save_path = r"D:/PicturesDownload/"  # 必要参数
mode_list = ["昨日榜单", "三天榜单", "上周榜单", "上月榜单", "三月榜单", "六月榜单", "去年榜单"]
mode_code_list = ['1d', '3d', '1w', '1m', '3m', '6m', '1y']
p_list = []
pt_list = []
key = []
pages_num = []
mode_code_index_ = []
mode_ = []

# tag=[]
tag = ['landscape', 'nature',  # 随机标签
       'anime girls', 'minimalism',
       'mountains', 'digital art',
       'anime', 'cosplay',
       'abstract', 'technology',
       'WLOP', 'artwork',
       '4K', 'Studio Ghibli',
       'pattern', 'video games',
       'sand', 'fractal',
       'fantasy girl', 'Pokémon',
       'national park', 'Naruto Shippuuden',
       'classical art', 'fantasy art',
       'plants', 'cyberpunk',
       'Caitlyn (League of Legends)', 'looking at viewer',
       'Eula (Genshin Impact)', 'simple background',
       'cityscape', 'science fiction',
       'car', 'Neon Genesis Evangelion',
       'Arknights', 'Chainsaw Man',
       'Ginhaha', 'Sakimichan',
       'One Piece', 'Azur Lane',
       'Naruto (anime)', 'Vi (League of Legends)',
       'Wonder Woman', 'fall',
       'Dragon Ball', 'pixel art',
       'school uniform', 'phone',
       'Hu Tao (Genshin Impact)', 'Miia (Monmusu)'
       ]

url = r"https://wallhaven.cc/"
headers = {'User-Agent': choice(UA.ua)}


# headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'} #备用UA


class Ui_MainWindow(object):  # GUI界面

    global mode_list
    global save_path

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 450)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(0.9)
        MainWindow.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 415, 245, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(210, 30, 205, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.spinBox = QtWidgets.QSpinBox(self.tab)
        self.spinBox.setGeometry(QtCore.QRect(210, 90, 60, 20))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(20)
        self.spinBox.setObjectName("spinBox")

        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(40, 20, 160, 40))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(40, 80, 160, 40))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")

        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(435, 90, 75, 20))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./icon/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")

        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(355, 80, 60, 40))
        self.label_5.setObjectName("label_5")

        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(100, 150, 400, 200))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("./icon/huaji.jpg"))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")

        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(435, 30, 75, 20))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icon/random1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")

        self.tabWidget.addTab(self.tab, icon, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(140, 30, 200, 20))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")

        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(40, 20, 80, 40))
        self.label_6.setObjectName("label_6")

        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(355, 80, 60, 40))
        self.label_12.setObjectName("label_12")

        self.spinBox_3 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_3.setGeometry(QtCore.QRect(210, 90, 60, 20))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(20)
        self.spinBox_3.setObjectName("spinBox_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(435, 90, 75, 20))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setAutoDefault(True)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")

        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(40, 80, 160, 40))
        self.label_13.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")

        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(100, 150, 400, 200))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("./icon/huaji.jpg"))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")

        self.tabWidget.addTab(self.tab_2, icon1, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 180, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./icon/talking.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(300, 180, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./icon/pay2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setObjectName("pushButton_6")

        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(220, 100, 120, 40))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./icon/talking.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.tabWidget.addTab(self.tab_3, icon2, "")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(285, 415, 290, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.tabWidget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.download_thread)
        self.pushButton_2.clicked.connect(self.random_tag)
        self.pushButton_4.clicked.connect(self.download_topmode_thread)
        self.pushButton_5.clicked.connect(self.connect)
        self.pushButton_6.clicked.connect(self.pay)
        self.lineEdit.editingFinished.connect(self.download_thread)
        self.comboBox.addItems(mode_list)
        self.comboBox.setCurrentIndex(3)
        self.comboBox.currentText()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.thread_1 = simple()
        self.thread_1.sinout.connect(self.download_set)
        self.thread_2 = topmode()
        self.thread_2.sinout.connect(self.download_set)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "4K壁纸下载小助手"))
        self.label.setText(_translate("MainWindow", "无下载任务"))
        self.label_3.setText(_translate("MainWindow", "搜索关键词（仅支持英语）："))
        self.label_4.setText(_translate("MainWindow", "请选择下载页数（1-20）："))
        self.pushButton.setText(_translate("MainWindow", "下载"))
        self.label_5.setText(_translate("MainWindow", "确认下载："))
        self.pushButton_2.setText(_translate("MainWindow", "随机"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "关键词搜索"))
        self.label_6.setText(_translate("MainWindow", "选择榜单模式："))
        self.label_12.setText(_translate("MainWindow", "确认下载："))
        self.pushButton_4.setText(_translate("MainWindow", "下载"))
        self.label_13.setText(_translate("MainWindow", "请选择下载页数（1-20）："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "榜单下载"))
        self.pushButton_5.setText(_translate("MainWindow", "作者微信"))
        self.pushButton_6.setText(_translate("MainWindow", "打赏作者"))
        self.label_16.setText(_translate("MainWindow", "作者：Water_bros"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "联系作者"))
        self.label_2.setText(_translate("MainWindow", "CopyRight © 2021 Water_bros,All Rights Reserved."))

    '''def getTag():#获取tags，已暂时不用
    
        global url
        global tag
        global headers
    
        url_tag_get=url+"tags/popular"
        res_tag=requests.get(url=url_tag_get,headers=headers)
        tag_soup=bs4.BeautifulSoup(res_tag.text,'lxml')
        tag_list=tag_soup.select('a.sfw')
    
        for tags in tag_list:
            tag.append(tags.getText())
        #print(tag)
    '''

    def random_tag(self):  # 随机设置tag

        global tag

        tag_r = choice(tag)
        # print(tag_r)
        self.lineEdit.setText(tag_r)

    def pay(self):  # 打赏页面

        from settings import Pay

        self.p = Pay.Ui_MainWindow()
        self.p.show()

    def connect(self):  # 联系方式
        
        return self.pay()

    def download_thread(self):

        # print("线程1启动")
        key.append(self.lineEdit.text())
        pages_num.append(self.spinBox.value())
        self.thread_1.start()

    def download_topmode_thread(self):

        # print("线程2启动")
        mode_code_index_.append(self.comboBox.currentIndex())
        mode_.append(self.comboBox.currentText())
        pages_num.append(self.spinBox_3.value())
        self.thread_2.start()

    def download_set(self, info):

        try:
            if info == "404":
                self.label.setText("下载失败，请重新尝试")
            else:
                self.label.setText(info)
        except:
            pass
            # print(info)


class simple(QThread):
    sinout = pyqtSignal(str)

    # print("begin")

    def __init__(self):

        super(simple, self).__init__()

    def run(self):  # 主程序:搜索下载

        # print("1.ok")

        global headers
        global save_path
        global url
        global p_list
        global key
        global pages_num

        kw = key[-1:][0]
        # print(kw)
        max_pages = int(pages_num[-1:][0])
        # print(max_pages)

        # if os.path.exists(save_path+kw)==False:
        # os.mkdir(save_path+kw)
        # else:
        # pass

        for pages in range(1, max_pages + 1):

            url_get = url + "search?q=" + kw + "&page=" + str(pages)
            # print(url_get)
            # print(headers)
            res_get = requests.get(url=url_get, headers=headers)

            if res_get.status_code != requests.codes.ok:
                # print("failed")
                self.sinout.emit("404")

            else:
                # print(res_get.status_code)
                get_soup = bs4.BeautifulSoup(res_get.text, 'lxml')
                img_jpg_urls = get_soup.select('a.preview')
                img_png_urls = get_soup.select('div.thumb-info')

                for png_num in range(len(img_png_urls)):

                    p = img_png_urls[png_num].select('span.png')

                    if p == [] or len(p) == 0:
                        p = 0
                    else:
                        p = 1

                    p_list.append(p)
                # print(p_list)

                for img_index in range(len(img_jpg_urls)):

                    img_id = img_jpg_urls[img_index].get('href')[-6:]
                    img_id2 = str(img_id[:2])

                    if p_list[img_index] == 0:
                        img_name = str(img_id) + ".jpg"
                    else:
                        img_name = str(img_id) + ".png"

                    img_url_get = r"https://w.wallhaven.cc/full/" + img_id2 + r"/wallhaven-" + img_name
                    # print(img_url_get)
                    res_get_img = requests.get(url=img_url_get, headers=headers)
                    self.sinout.emit(img_name + "下载中……")

                    with open(save_path + img_name, "wb") as f:

                        img = res_get_img.content
                        f.write(img)

                    self.sinout.emit(img_name + "下载完成！")
                    # print(img_name+" is saved")

        self.sinout.emit("当前页已全部下载！")


class topmode(QThread):
    sinout = pyqtSignal(str)

    # print("begin")

    def __init__(self):
        super(topmode, self).__init__()

    def run(self):  # 主程序：榜单爬取

        # print("2.ok")

        global headers
        global mode_code_list
        global save_path
        global url
        global pt_list
        global mode_code_index_
        global mode_
        global pages_num

        mode_code_index = mode_code_index_[-1:][0]
        # print(mode_code_index)
        mode = mode_[-1:][0]
        # print(mode)
        mode_code = mode_code_list[mode_code_index]
        # print(mode_code)
        url_top = url + "search?categories=110&purity=100&topRange=" + mode_code + "&sorting=toplist&order=desc&page="
        max_pages = int(pages_num[-1:][0])
        # print(max_pages)
        # if os.path.exists(save_path+mode)==False:
        # os.mkdir(save_path+mode)
        # else:
        # pass

        '''
        url_top_pages=url_top+str(page+1)
        res_page=requests.get(url=url_top_pages,headers=headers)
        html=bs4.BeautifulSoup(res_page.text,'lxml')
        max_pages=html.select('h2')[0].getText()
        max_page=int(max_pages[-3:])
        '''

        for pages in range(1, max_pages + 1):

            url_tops = url_top + str(pages)
            # print(url_tops)
            res_top = requests.get(url=url_tops, headers=headers)

            if res_top.status_code != requests.codes.ok:
                # print("failed")
                self.sinout.emit("404")
            else:
                # print(res_top.status_code)
                top_soup = bs4.BeautifulSoup(res_top.text, 'lxml')
                img_top_urls_list = top_soup.select('a.preview')
                img_top_png_urls = top_soup.select('div.thumb-info')

                for png_num in range(len(img_top_png_urls)):

                    p = img_top_png_urls[png_num].get('span.png')

                    if p == []:
                        p = 0
                    else:
                        p = 1

                    pt_list.append(p)

                for img_top_index in range(len(img_top_urls_list)):

                    img_top_urls = img_top_urls_list[img_top_index].get('href')
                    img_top_id = img_top_urls[-6:]
                    img_top_id2 = img_top_id[:2]

                    if pt_list[img_top_index] == 0:
                        img_top_name = img_top_id + ".jpg"
                    else:
                        img_top_name = img_top_id + ".png"

                    img_top_url = r"https://w.wallhaven.cc/full/" + img_top_id2 + "/wallhaven-" + img_top_name
                    img_top_get = requests.get(url=img_top_url, headers=headers)
                    self.sinout.emit(img_top_name + "下载中……")

                    with open(save_path + img_top_name, "wb") as f:

                        img_top = img_top_get.content
                        f.write(img_top)

                    self.sinout.emit(img_top_name + "下载完成！")
                    # print(img_top_name+" is saved")

        self.sinout.emit("当前页已全部下载！")


if __name__ == "__main__":  # 启动模块

    # getTag()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
