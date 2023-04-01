"""
自定义模块
"""

#
# import mymodule

# mymodule.test(1, 2)


# 导入不同模块的同名功能
# from mymodule import test
# from mymodule1 import test
# test(1, 2)

# __main__变量        在导入模块时不会执行里面的函数
from mymodule import test

# __all__变量   控制导入的*含有的功能
from mymodule import *

test(1, 2)

from mymodule import testB

testB(2, 3)
