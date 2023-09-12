from selenium import webdriver
from time import sleep

# path = 'chromedriver.exe'
browser = webdriver.Chrome()

url = 'https://www.baidu.com/'

browser.get(url)

# 根据id来找对象
button = browser.find_element_by_id('su')
# print(button)

# 根据标签属性找对象
input = browser.find_element_by_name('wd')
# print(input)

# 根据Xpath语句获取对象
input1 = browser.find_element_by_xpath('//input[@id="su"]')
# print(input1)

# 根据标签名字来获取对象
inputs = browser.find_elements_by_tag_name('input')
# print(inputs)

# 根据bs4语法来获取对象，即CSS选择器
button1 = browser.find_element_by_css_selector('#su')
# print(button1)

# 获取链接对象
links = browser.find_element_by_link_text('图片')
print(links)