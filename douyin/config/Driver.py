import time

from selenium import webdriver


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
    def slild_down(driver):
        for w in range(100):
          # 第一个参数x是横向距离，第二个参数y是纵向距离
          js = 'window.scrollBy(0, 200)'  # 90表示滚动条下滑的长度（位置）
          driver.execute_script(js)
          time.sleep(0.2)

