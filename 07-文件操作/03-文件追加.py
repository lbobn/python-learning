"""
文件追加
"""

# a模式
# 追加模式写出
t = open("writeTest.txt", "a", encoding="UTF-8")

t.write("\n你好世界!!!")

t.flush()

t.close()
