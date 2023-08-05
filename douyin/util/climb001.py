import os.path
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from douyin.config.Cookies import Cookies
from douyin.config.DataBase import DataBase
from douyin.config.Driver import Driver
from lxml import html, etree

from douyin.pojo.commentDetail import commentDetail
from douyin.pojo.videoDetail import videoDetail
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
        DriverClass.slild_down(driver)
        data = driver.page_source
        fh = open(filename, "w", encoding="utf-8")
        fh.write(data)
        time.sleep(2)
        fh.close()


if __name__ == "__main__":
    # 浏览器初始化以及主类实现--不需要更新cookies
    DriverClass = Driver(updateCookie=0)
    driver = DriverClass.get_driver()
    climb = climb001()
    # 文件准备
    url = "https://www.douyin.com/video/7263308382231137577"
    if os.path.exists("video"):
        pass
    else:
        os.makedirs("video")
    # 下载并打开好相关.html
    climb.write_down(url, driver, "video/dongman.html",DriverClass)
    html_new = BeautifulSoup(open('video/dongman.html', encoding='utf-8'), features='html.parser')
    # 工具类创建
    getutil = getUtil()
    saveutil = saveUtil()
    # 获取相关数据
    videoDe = getutil.get_video(html_new)
    video = requests.get(videoDe.url).content
    saveutil.save_video(video)

    videoIcon = requests.get(videoDe.iconUrl).content
    saveutil.save_video_icon(videoIcon)
    comments = getutil.get_comment(html_new)
    #获取完需要的内容然后直接删除.html文件
    os.remove("video/dongman.html")
    # 数据库操作
    db=DataBase()
    for comment in comments:
        db.insert_comment_data(comment)
    db.insert_video_data(videoDe)
