import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from douyin.config.Driver import Driver
from lxml import html, etree


class climb001:
    #视频播放链接
    url=''
    def __int__(self):
        self.driver=Driver.get_driver()

    def write_down(self):
        self.driver.get(self.url)
        time.sleep(2)
        data = self.driver.page_source
        fh = open("dongman.html", "w", encoding="utf-8")
        fh.write(data)
        fh.close()
    def set_url(self,url):
        self.url=url
    def get_video(self,html_new):
        soup = html_new.find(name="xg-video-container")
        source = soup.find("source")
        videourl = "https:" + source.get("src")
        video = requests.get(videourl).content
        return video

    def get_content(self,html_new):
        #后续补全
        pass

    def save_video(self,video):
        try:
            # 打开文件夹,将图片存入
            with open('video/' + '1.mp4', 'wb') as f:

                f.write(video)
                print(video)
                # 更改图片名,防止新下载的图片覆盖原图片
            # 若上述代码执行报错,则执行此部分代码
        except Exception as err:
            # 跳过错误代码
            pass

if __name__ == "__main__":
    climb=climb001()
    climb.set_url("https://www.douyin.com/search/%E6%8A%96%E9%9F%B3%E7%99%BE%E5%88%86%E5%A4%A7%E6%88%98?aid=111077d9-dc34-4e50-be5a-a38de14a850e&publish_time=0&sort_type=0&source=recom_search&type=general")
    html_new = BeautifulSoup(open('dongman.html', encoding='utf-8'), features='html.parser')
    video=climb.get_video(html_new)
    climb.save_video(video)
