"""
序列和切片
"""

# 对list进行切片
l = [1, 2, 3, 4, 5, 6]
result_1 = l[1:4]
print(result_1)

# 对tuple进行切片
t = (0, 1, 2, 3, 4, 5, 6)
result2 = t[:]
print(result2)

# 对String进行切片,步长2
s = "0123456"
result3 = s[::2]
print(result3)

# 对String进行切片,步长-1
s = "0123456"
result4 = s[::-1]
print(result4)
