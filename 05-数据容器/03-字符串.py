s1 = "itheima and itcast"

# 下标取值
v1 = s1[0]
v2 = s1[-1]
print(v1, v2)

# index
index = s1.index("and")
print(index)

# replace
r = s1.replace(" ", "&")
print(r)

# split
split = r.split("&")
print(split)

# strip
s2 = "  Hello world   "
s3 = "12Hello world211"
strip1 = s2.strip()
strip2 = s3.strip("12")
print(strip1, strip2)

# 统计字符出现次数
count = s1.count("it")
print(count)

# 统计总共字符个数
i = len(s1)
print(i)
