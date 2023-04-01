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

# 捕获多个异常
try:
    # print(1/0)
    print(nnnn)
except(NameError, ZeroDivisionError) as e:
    print("出现了变量未定义或除以0的异常")

# 未正确设置异常类型 将无法捕获异常


# 捕获所有异常
try:
    print(12)
    # print(1 / 0)
    # open("D:/123.txt", "r")
except Exception as e:
    print("出现异常")
else:
    print("没有异常")
finally:
    print("无论有无异常,都会执行")
#
