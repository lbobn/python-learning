str1 = "你好呀"
str2 = "hello"
str3 = "world"


def my_len(data):
    count = 0
    for s in data:
        count += 1
    print(f"字符串{data}的长度是{count}")


my_len(str1)
my_len(str2)
my_len(str3)
