for x in "HelloWorld":
    print(x + " ", end='')
print()

# 判断s中字符"a"个数
s = "itheima is a brand of itcast"

count = 0
for i in s:
    if i == "a":
        count += 1
print(count)

"""
Python中range()的用法
"""

range(10)  # 0~9
range(3, 10)  # 3~9
range(3, 10, 2)  # 3, 5, 7, 9

"""
1~100(不含100)范围内有多少偶数
"""
count = 0
for i in range(1, 100):
    if i % 2 == 0:
        count += 1
print(count)

"""
表白送玫瑰
"""

for i in range(1, 101):
    print(f"今天是第{i}天,开始表白")
    for j in range(1, 11):
        print(f"正在送第{j}只玫瑰")
