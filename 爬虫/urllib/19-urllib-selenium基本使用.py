from selenium import webdriver
from time import sleep

path = 'chromedriver.exe'
browser = webdriver.Chrome()

url = 'https://www.baidu.com/'

browser.get(url)

# sleep(100000)
