"""
re的常用方法
"""

import re

s = "python njcwekjb opython abjkca dxhbak python"
match = re.match("python", s)  # 从头开始匹配

print(match)
print(match.group())
print(match.span())

search = re.search("opython", s)  # 查找第一子串

print(search)
print(search.group())
print(search.span())

findall = re.findall("python", s)  # 查找所有子串
print(findall)
