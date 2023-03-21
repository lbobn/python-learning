"""
统计itheima出现数量
"""
f = open("word.txt", "r", encoding="UTF-8")
count = 0
# 方式一:
# read = f.read()
# print(read.count("itheima"))

# 方式二
for line in f:
    line = line.strip()
    # line.replace("\n", "")
    s = line.split(" ")
    print(s)
    count += s.count("itheima")

f.close()

print(f"itheima的个数为{count}")
