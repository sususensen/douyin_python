import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from douyin.config.DataBase import DataBase
from douyin.config.Driver import Driver
from lxml import html, etree

from douyin.pojo.commentDetail import commentDetail
from douyin.pojo.videoDetail import videoDetail
from douyin.util.getComment import getComment
from douyin.util.getFromUrl import getFromUrl
from douyin.util.saveFromGet import saveFromGet


class climb001:
    #为beautifulsoup使用写下源码.html文件
    def write_down(self,url,driver,filename):
        driver.get(url)
        time.sleep(2)
        data = driver.page_source
        fh = open(filename, "w", encoding="utf-8")
        fh.write(data)
        time.sleep(2)
        fh.close()

if __name__ == "__main__":

    driver=Driver().get_driver()
    climb=climb001()

    url="https://www.douyin.com/video/7263308382231137577"
    climb.write_down(url,driver,"dongman.html")

    html_new = BeautifulSoup(open('dongman.html', encoding='utf-8'), features='html.parser')
    getUtil=getFromUrl()
    saveUtil=saveFromGet()
    videoDe=getUtil.get_video(html_new)
    video = requests.get(videoDe.url).content
    saveUtil.save_video(video)

    videoIcon=requests.get(videoDe.iconUrl).content
    saveUtil.save_video_icon(videoIcon)
    comments=getComment().get_comment(html_new)
    db=DataBase()
    for comment in comments:
        db.insert_comment_data(comment)




