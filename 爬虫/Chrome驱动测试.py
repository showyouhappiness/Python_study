import time
from selenium import webdriver

browser = webdriver.Chrome()
# 实例化1个谷歌浏览器对象
browser.get('https://www.bing.com/')
time.sleep(5)
browser.close()
