# 导入 selenium
from selenium import webdriver
# 如果需要指定路径，但是路径在新版本中被重构到 Service 函数中了
from selenium.webdriver.chrome.service import Service
# 配置对象
from selenium.webdriver.chrome.options import Options
# 导入常量对象（可以点进去看看，其实也可以手写）
# from selenium.webdriver.common.by import By
# 导入 定时器
from time import sleep

# 浏览器封装
def share_browser ():
  # 浏览器驱动路径（可以是下载的驱动，也可以直接使用电脑上 Chrome 浏览器的驱动，找到路径就行）
  # win_path = 'chromedriver.exe'
  mac_path = 'chromedriver'

  # 配置对象
  options = Options()
  # options = webdriver.ChromeOptions() # 也可以这样创建 options 对象
  # options.add_experimental_option('detach', True) # 不自动关闭浏览器
  options.add_argument('--headless') # 设置无窗口模式
  options.add_argument('--disable-gpu') # 禁用gpu加速

  # 创建浏览器
  service = Service(mac_path)
  browser = webdriver.Chrome(service=service, options=options)
  # 返回
  return browser

# 创建浏览器
browser = share_browser()

# 打开指定网址
browser.get('https://www.baidu.com')

# 保存快照
browser.save_screenshot('baidu.png')

# 睡眠
sleep(2)

# 退出
browser.quit()
