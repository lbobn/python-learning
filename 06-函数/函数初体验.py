str1 = "你好呀"
str2 = "hello"
str3 = "world"


def my_len(data):
    """
    求字符串data的长度
    :param data: 字符串data
    :return: None
    """
    count = 0
    for s in data:
        count += 1
    print(f"字符串{data}的长度是{count}")


my_len(str1)
my_len(str2)
my_len(str3)


def get_jiecheng(num):
    """
    求阶乘
    :param num:
    :return:
    """
    if num == 0 or num == 1:
        return 1
    return num * get_jiecheng(num - 1)


jiecheng = get_jiecheng(5)
print(jiecheng)

num = 100


def test_a():
    global num  # global关键字   设置内部定义的变量为全局变量
    num = 200
    print(f"num={num}")


test_a()
print(f"num={num}")
