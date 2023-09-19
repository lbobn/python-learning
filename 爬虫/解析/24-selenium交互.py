from selenium import webdriver

chrome = webdriver.Chrome()

url = 'https://www.baidu.com/'
chrome.get(url)

import time

time.sleep(2)

# 获取输入框
input = chrome.find_element_by_id('kw')
# 发送文字
input.send_keys("周杰伦")
time.sleep(2)

# 获取百度按钮
button = chrome.find_element_by_id('su')

button.click()
time.sleep(2)
# 滑到底部
js_bottom = 'document.documentElement.scrollTop=100000'
chrome.execute_script(js_bottom)
time.sleep(2)

# 下一页
next = chrome.find_element_by_xpath('//a[@class="n"]')
next.click()

time.sleep(2)

# 后退
chrome.back()
time.sleep(2)

# 前进
chrome.forward()

# 关闭
chrome.quit()