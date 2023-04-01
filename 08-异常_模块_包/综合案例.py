"""
综合练习
"""

from my_package.my_utils import file_util
from my_package.my_utils import str_util

print(str_util.str_reverse("你好"))
print(str_util.substr("helloworld", 5, 8))

file_util.append_to_file("D:\\Test\\python\\python-learning\\07-文件操作\\test.txt", "测试")
file_util.print_file_info("D:\\Test\\python\\python-learning\\07-文件操作\\test.txt")
