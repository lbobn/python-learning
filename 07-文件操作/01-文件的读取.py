"""
文件读取
"""
import time

f = open("test.txt", "r", encoding="UTF-8")

# 读取指定长度字节
read = f.read(10)
print(read)

# 读取一行
readline = f.readline()
print(readline)

# 读取全部行,得到列表
# readlines = f.readlines()
# print(readlines)

# for循环文件行,每次循环获取一行
for line in f:
    print(f"每一行为:{line}")

# 文件 关闭
time.sleep(2)
f.close()
print("-------------------------")

# with open() as f      可以自动关闭文件
with open("test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行为:{line}")
