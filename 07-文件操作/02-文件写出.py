"""
文件写出
"""

# w 模式:
# 打开不存在的文件时会创建文件
# 打开已存在的文件时会清空原有内容再写
t = open("writeTest.txt", "w", encoding="UTF-8")
t.write("Hello World!!!")

t.flush()

t.close()  # close自带flush方法
