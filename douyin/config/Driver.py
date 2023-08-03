from selenium import webdriver


class Driver:
    def __init__(self):
        # 浏览器配置
        option = webdriver.ChromeOptions()

        # 不显示窗口
        option.add_argument('--headless')

        # 以root权限运行
        option.add_argument('--no-sandbox')

        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(options=option)

    def get_driver(self):
        return self.driver

