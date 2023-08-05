import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


class Driver:
    def __init__(self,updateCookie):
        # 浏览器配置
        option = webdriver.ChromeOptions()
        #加快网页加载速度（不加载js，images等）
        # prefs = {
        #     'profile.default_content_setting_values': {
        #         'images': 2,
        #         'permissions.default.stylesheet': 2,
        #         'javascript': 2
        #     }
        # }
        # option.add_experimental_option('prefs', prefs)
        #判断是否需要更新抖音登录信息
        if(updateCookie==0):
            option.add_argument('--headless')
        else:pass

        # 以root权限运行

        option.add_argument('--no-sandbox')

        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(options=option)

    def get_driver(self):
        return self.driver
    @staticmethod
    def slide_down(driver,slideTime):
        for w in range(slideTime):
          # 第一个参数x是横向距离，第二个参数y是纵向距离
          js = 'window.scrollBy(0, 500)'
          driver.execute_script(js)
          time.sleep(0.3)

    #这个是切换视频-》切换下一个视频
    @staticmethod
    def slide_down2(driver):
        actions = ActionChains(driver)

        # 定位网页元素
        element = driver.find_element(By.CSS_SELECTOR,"body")

        # 示例：向下滚动2次
        for i in range(100):

           actions.move_to_element(element).perform()
           actions.send_keys(Keys.ARROW_DOWN).perform()
           time.sleep(0.4)