"""
分割字符串

统计有多少个"it"
将空格替换为"|"
按"|"分割得到列表
"""

s = "itheima itcast boxuegu"

count = s.count("it")
print(f"{s}中有{count}个it")

new_s = s.replace(" ", "|")
print(f"{s}被替换后的结果为{new_s}")

l = new_s.split("|")
print(f"{new_s}被分割后为{l}")
