import json
import os
import time

from douyin.config.Driver import Driver


class Cookies:
    @staticmethod
    def get_cookies_save():
        if os.path.exists("../util/cookies"):
            pass
        else:
            os.makedirs("../util/cookies")
        driver=Driver(updateCookie=1).get_driver()
        driver.get("https://www.douyin.com/discover")
        time.sleep(60)
        cookies=driver.get_cookies()
        print(cookies)
        with open('../util/cookies/cookies.json', 'w') as f:
            json.dump(cookies, f)

    @staticmethod
    def load_cookies():
        with open('../util/cookies/cookies.json', 'r') as f:
            return json.load(f)