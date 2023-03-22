"""
异常捕获
"""

try:
    f = open("linux.txt", "r", encoding="UTF-8")
except:
    print("出现异常")

# 捕获指定异常
try:
    print(name)
except NameError as e:
    print("变量未定义异常")
