import os.path
import time

import requests
from bs4 import BeautifulSoup

from douyin.config.Cookies import Cookies
from douyin.config.DataBase import DataBase
from douyin.config.Driver import Driver
from douyin.pojo.allResult import allResult
from douyin.util.getUtil import getUtil
from douyin.util.saveUtil import saveUtil


class climb001:
    # 为beautifulsoup使用写下源码.html文件
    def write_down(self, url, driver, filename,DriverClass):
        driver.get(url)
        time.sleep(2)
        #从文件中获得cookie加到浏览器上
        cookies=Cookies.load_cookies()
        for cookie in cookies:
            if 'expiry' in cookie:  # 有的cookie里面有这个参数，有的没有。有的话，需要做处理。
                del cookie['expiry']
            driver.add_cookie(cookie)
        driver.refresh()
        #进入登录后的界面
        time.sleep(2)
        #模拟下拉界面实现加载
        DriverClass.slide_down(driver,slideTime=250)#(这个跟网络有点关系)time(次数)=50:383;100:900条;200:1300条
        data = driver.page_source
        fh = open(filename, "w", encoding="utf-8")
        fh.write(data)
        time.sleep(2)
        fh.close()
    def file_handle_get_html(self):
        if os.path.exists("video"):
            pass
        else:
            os.makedirs("video")
        climb.write_down(url, driver, "video/dongman.html", DriverClass)
        html_new = BeautifulSoup(open('video/dongman.html', encoding='utf-8'), features='html.parser')
        return html_new
    def find_and_get_all(self):
        allresult = allResult()
        getutil = getUtil()
        saveutil = saveUtil()
        # 获取相关数据
        allresult.vidodetail = getutil.get_video(html_new)
        video = requests.get(allresult.vidodetail.url).content
        saveutil.save_video(video)

        videoIcon = requests.get(allresult.vidodetail.iconUrl).content
        saveutil.save_video_icon(videoIcon)
        allresult.commentsdetail = getutil.get_comment(html_new)
        # 获取完需要的内容然后直接删除.html文件
        os.remove("video/dongman.html")
        return allresult
    def db_handle(self):
        db = DataBase()
        for commentdetail in allresult.commentsdetail:
            db.insert_comment_data(commentdetail)
        db.insert_video_data(allresult.vidodetail)


if __name__ == "__main__":
    url = "https://www.douyin.com/video/7246590192927182135"

    # 浏览器初始化以及主类实现--不需要更新cookies设置为0
    DriverClass = Driver(updateCookie=1)
    driver = DriverClass.get_driver()
    climb = climb001()

    # 下载并打开好相关.html
    html_new=climb.file_handle_get_html()
    # 根据.html文件实现信息获取并销毁html
    allresult=climb.find_and_get_all()
    #数据库插入操作
    climb.db_handle()

