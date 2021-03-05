import os
import time
from govscrapy.settings import INTERVAL_TIME
if __name__ == '__main__':
    # os.system('pwd')
    while True:
        os.system("scrapy crawl spider")
        # 每1个小时执行一次　６０＊60

        # 每2个小时执行一次　６０＊60 * 2 = 7200

        time.sleep(INTERVAL_TIME)
