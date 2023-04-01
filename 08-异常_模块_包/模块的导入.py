"""
模块导入
"""

# import 导入python模块  (.py文件)
# import time
# print("你好")
# time.sleep(5)
# print("我好")


# from  导入python模块
# from time import sleep
#
# print("你好")
# sleep(5)
# print("我好")


# 使用*导入模块全部功能
# from time import *
#
# print("你好")
# sleep(5)
# print("我好")

# 使用as给特定功能加上别名
import time as t

print("你好")
t.sleep(5)
print("我好")

from time import sleep as shuimian

print("你好")
shuimian(5)
print("我好")
